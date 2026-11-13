"""Turn every past question paper into text an AI can read, organised by subject and department.

Two stages:

  extract  Download the release bundles that hold question papers (37 bundles, about 19 GiB), rebuild each
           paper, and read its text: straight from the PDF when it has a text layer, otherwise by OCR with
           Tesseract. Bundles are processed one at a time and deleted afterwards, so about 3 GiB of free space
           is enough. Results go to a resumable cache (texts.jsonl); rerunning skips finished work.

  build    Read that cache (or the committed question_bank/extracted_text.jsonl.gz) together with
           subjects/pyq_subject_index.csv and write, for every subject:
             subjects/<Subject>/papers.md        full text of every paper, newest first, with metadata
             subjects/<Subject>/questions.jsonl  one record per question: number, part, text, marks, CO/BL,
                                                 year, exam, semester, programme, department
           plus departments/<Department>/README.md and question_bank/README.md (schema and statistics).

Requirements for extract: Python 3.11+, `pip install pymupdf`, and the Tesseract OCR program on PATH
(Windows: https://github.com/UB-Mannheim/tesseract/wiki; Debian/Ubuntu: apt install tesseract-ocr).
build needs only the standard library.

  python build_question_bank.py extract --work D:/qb_work --manifest full-library-manifest.json
  python build_question_bank.py build --texts D:/qb_work/texts.jsonl
  python build_question_bank.py build                      # rebuild from the committed text cache
"""
from pathlib import Path, PurePosixPath
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
import argparse, csv, gzip, hashlib, io, json, math, os, re, shutil, subprocess, sys, tempfile, threading, time, zipfile

HERE = Path(__file__).resolve().parent
REPO = 'dhruvpaleja/mpstme-library-archive-2026-10-08'
QP_ROOT = '02_Question_Papers/'
INDEX_CSV = HERE / 'subjects' / 'pyq_subject_index.csv'
BANK_DIR = HERE / 'question_bank'
TEXT_CACHE = BANK_DIR / 'extracted_text'          # 16 gzipped JSONL shards
OCR_DPI = 200
MAX_OCR_PIXELS = 3600            # longest side of a rendered page
LOW_OCR_CONFIDENCE = 60          # mean Tesseract confidence below this: handwritten or a poor scan
MIN_TEXT_LETTERS = 80            # fewer letters than this on a PDF page means it is a scan -> OCR

# ============================================================================ text extraction (worker side)


def sniff(data, name=''):
    """File format from its first bytes (a few portal files lost their extension)."""
    head = data[:8]
    if head.startswith(b'%PDF'):
        return 'pdf'
    if head.startswith(b'PK'):
        try:
            names = zipfile.ZipFile(io.BytesIO(data)).namelist()
        except zipfile.BadZipFile:
            return 'unknown'
        if 'word/document.xml' in names:
            return 'docx'
        if any(n.startswith('xl/') for n in names):
            return 'xlsx'
        return 'zip'
    if head.startswith((b'II*\x00', b'MM\x00*')):
        return 'tiff'
    if head.startswith(b'\xff\xd8'):
        return 'jpeg'
    if head.startswith(b'\x89PNG'):
        return 'png'
    suffix = PurePosixPath(name).suffix.lower().lstrip('.')
    return {'tif': 'tiff', 'jpg': 'jpeg'}.get(suffix, suffix or 'unknown')


def ocr_png(png_bytes):
    """OCR one rendered page with Tesseract (layout mode 4 keeps marks on the same line as the question)."""
    with tempfile.TemporaryDirectory() as tmp:
        image = Path(tmp) / 'page.png'
        image.write_bytes(png_bytes)
        base = Path(tmp) / 'out'
        env = dict(os.environ, OMP_THREAD_LIMIT='1')
        subprocess.run(['tesseract', str(image), str(base), '--psm', '4', 'txt', 'tsv'],
                       check=True, capture_output=True, env=env)
        text = base.with_suffix('.txt').read_text(encoding='utf-8', errors='replace')
        confidences = []
        for line in base.with_suffix('.tsv').read_text(encoding='utf-8', errors='replace').splitlines()[1:]:
            cells = line.split('\t')
            if len(cells) == 12 and cells[11].strip():
                try:
                    value = float(cells[10])
                except ValueError:
                    continue
                if value >= 0:
                    confidences.append(value)
    return text, round(math.fsum(confidences) / len(confidences), 1) if confidences else None


def tidy(text):
    """Trim lines and blank runs; keep wide gaps (column breaks) as three spaces, other spacing as one."""
    lines = [re.sub(r'(?<! ) (?! )', ' ', re.sub(r'[ \t]{2,}', '   ', line)).strip()
             for line in text.replace('\r', '').replace('\t', '   ').split('\n')]
    out, blank = [], False
    for line in lines:
        if line.strip():
            out.append(line)
            blank = False
        elif not blank and out:
            out.append('')
            blank = True
    return '\n'.join(out).strip()


def layout_text(page):
    """Rebuild a page's visual rows from word positions so table columns (question, CO/BL tags, marks) stay
    on the same line, separated by wide gaps ('   '), as OCR output does."""
    words = page.get_text('words')
    if not words:
        return ''
    heights = sorted(w[3] - w[1] for w in words)
    tolerance = max(1.5, heights[len(heights) // 2] * 0.45)
    rows = []                                           # [y_centre, [words]]
    for word in sorted(words, key=lambda w: ((w[1] + w[3]) / 2, w[0])):
        centre = (word[1] + word[3]) / 2
        if rows and abs(centre - rows[-1][0]) <= tolerance:
            row = rows[-1]
            row[1].append(word)
            row[0] = sum((w[1] + w[3]) / 2 for w in row[1]) / len(row[1])
        else:
            rows.append([centre, [word]])
    lines = []
    for _, row in rows:
        row.sort(key=lambda w: w[0])
        parts, last_end = [], None
        for x0, _, x1, _, text, *_ in row:
            if last_end is not None:
                char = max(1.0, (x1 - x0) / max(1, len(text)))
                parts.append('   ' if x0 - last_end > 2.5 * char else ' ')
            parts.append(text)
            last_end = x1
        lines.append(''.join(parts))
    return '\n'.join(lines)


def garbled(text):
    """A text layer made of unmapped glyphs reads as symbols, not words."""
    letters = sum(c.isalpha() for c in text)
    words = re.findall(r'[A-Za-z]{3,}', text)
    return letters < MIN_TEXT_LETTERS or len(words) < 10 or sum(not c.isascii() for c in text) > 0.3 * max(1, len(text))


def document_pages(data, fmt):
    """[{page, method, text, ocr_confidence}] for a PDF or image document."""
    import pymupdf
    pages = []
    filetype = None if fmt == 'pdf' else {'tiff': 'tiff', 'jpeg': 'jpeg', 'png': 'png'}.get(fmt, fmt)
    with pymupdf.open(stream=data, filetype=filetype) as doc:
        for number, page in enumerate(doc, 1):
            text = page.get_text('text') if fmt == 'pdf' else ''
            if fmt == 'pdf' and not garbled(text):
                pages.append({'page': number, 'method': 'text', 'text': tidy(layout_text(page))})
                continue
            longest = max(page.rect.width, page.rect.height) or 1
            dpi = max(72, min(OCR_DPI, int(MAX_OCR_PIXELS * 72 / longest)))
            pixmap = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
            text, confidence = ocr_png(pixmap.tobytes('png'))
            pages.append({'page': number, 'method': 'ocr', 'text': tidy(text), 'ocr_confidence': confidence})
    return pages


def docx_text(data):
    xml = zipfile.ZipFile(io.BytesIO(data)).read('word/document.xml').decode('utf-8', errors='replace')
    xml = re.sub(r'</w:tc>', ' | ', xml)
    xml = re.sub(r'</w:p>|<w:br/>|</w:tr>', '\n', xml)
    text = re.sub(r'<[^>]+>', '', xml)
    for entity, char in (('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'), ('&apos;', "'")):
        text = text.replace(entity, char)
    return [{'page': 1, 'method': 'docx', 'text': tidy(text)}]


def read_document(data, name='', depth=0):
    """Text of one file; ZIPs are opened and each paper inside is read."""
    fmt = sniff(data, name)
    record = {'format': fmt}
    try:
        if fmt in ('pdf', 'tiff', 'jpeg', 'png'):
            record['pages'] = document_pages(data, fmt)
        elif fmt == 'docx':
            record['pages'] = docx_text(data)
        elif fmt == 'zip' and depth < 2:
            members = []
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                for info in sorted(archive.infolist(), key=lambda i: i.filename):
                    if info.is_dir() or info.file_size == 0 or '__MACOSX' in info.filename:
                        continue
                    member = read_document(archive.read(info), info.filename, depth + 1)
                    member['name'] = info.filename
                    members.append(member)
            record['members'] = members
        elif fmt == 'xlsx':
            record['note'] = 'spreadsheet data set; no question text'
        else:
            record['note'] = f'unsupported format {fmt}'
    except Exception as error:                     # one broken scan must not stop the run
        record['error'] = f'{type(error).__name__}: {error}'[:300]
    return record


def extract_one(sha, path, name):
    data = Path(path).read_bytes()
    record = read_document(data, name)
    record['sha256'] = sha
    Path(path).unlink()
    return record

# ============================================================================ extract stage (driver side)


def sha256_file(path):
    with open(path, 'rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def download(bundle, target, method):
    """Fetch one release asset and check its size and SHA-256 against the manifest."""
    if target.exists() and target.stat().st_size == bundle['bytes'] and sha256_file(target) == bundle['sha256']:
        return target
    partial = target.with_suffix('.part')
    for attempt in range(5):
        try:
            if method == 'gh':
                tag = PurePosixPath(bundle['url']).parent.name
                subprocess.run(['gh', 'release', 'download', tag, '--repo', REPO, '--pattern', bundle['name'],
                                '--dir', str(partial.parent), '--clobber'], check=True, capture_output=True)
                (partial.parent / bundle['name']).replace(partial)
            else:
                command = ['curl', '-sSfL', '--retry', '3', '-C', '-', '-o', str(partial),
                           '-H', 'Accept: application/octet-stream']
                if os.environ.get('GITHUB_TOKEN'):
                    command += ['-H', 'Authorization: Bearer ' + os.environ['GITHUB_TOKEN']]
                subprocess.run(command + [f"https://api.github.com/repos/{REPO}/releases/assets/{bundle['asset_id']}"],
                               check=True, capture_output=True)
            if partial.stat().st_size == bundle['bytes'] and sha256_file(partial) == bundle['sha256']:
                partial.replace(target)
                return target
            partial.unlink()
        except (subprocess.CalledProcessError, OSError) as error:
            print(f"  download {bundle['name']} attempt {attempt + 1} failed: {error}", flush=True)
        time.sleep(2 ** attempt)
    raise SystemExit(f"Could not download a verified copy of {bundle['name']}")


def cmd_extract(args):
    if not shutil.which('tesseract'):
        raise SystemExit('Tesseract OCR is not on PATH; see the instructions at the top of this file.')
    manifest = json.loads(Path(args.manifest).read_text(encoding='utf-8'))
    work = Path(args.work).resolve()
    work.mkdir(parents=True, exist_ok=True)
    texts = work / 'texts.jsonl'
    done = set()
    if texts.exists():
        with texts.open(encoding='utf-8') as stream:
            for line in stream:
                try:
                    done.add(json.loads(line)['sha256'])
                except (json.JSONDecodeError, KeyError):
                    pass                                # a line cut off by an interrupted run
    papers = {}
    for row in manifest['files']:
        if row['path'].startswith(QP_ROOT):
            papers.setdefault(row['sha256'], row)
    by_bundle = defaultdict(list)
    for sha, row in sorted(papers.items()):
        if sha not in done:
            by_bundle[manifest['chunks'][row['chunks'][0]]['bundle']].append(row)
    bundles = [b for b in manifest['bundles'] if b['name'] in by_bundle]
    if args.limit:
        bundles = bundles[:args.limit]
    print(f'{len(done)} papers already extracted; {sum(len(by_bundle[b["name"]]) for b in bundles)} to go '
          f'in {len(bundles)} bundles.', flush=True)
    stage = work / 'bundles'
    stage.mkdir(exist_ok=True)
    scratch = work / 'papers'
    scratch.mkdir(exist_ok=True)

    prefetched = {}

    def fetch(index):
        if index < len(bundles):
            bundle = bundles[index]
            prefetched[index] = download(bundle, stage / bundle['name'], args.download)

    started = time.time()
    finished = 0
    with texts.open('a', encoding='utf-8') as out, ProcessPoolExecutor(args.workers) as pool:
        fetch(0)
        for index, bundle in enumerate(bundles):
            ahead = threading.Thread(target=fetch, args=(index + 1,), daemon=True)
            ahead.start()                               # download the next bundle while this one is read
            path = prefetched.pop(index, None) or download(bundle, stage / bundle['name'], args.download)
            futures = []
            with zipfile.ZipFile(path) as archive:
                for row in by_bundle[bundle['name']]:
                    data = b''.join(archive.read('objects/' + chunk) for chunk in row['chunks'])
                    if hashlib.sha256(data).hexdigest() != row['sha256']:
                        raise SystemExit(f"Rebuilt paper does not match its checksum: {row['path']}")
                    paper = scratch / row['sha256']
                    paper.write_bytes(data)
                    futures.append(pool.submit(extract_one, row['sha256'], str(paper), PurePosixPath(row['path']).name))
            for future in as_completed(futures):
                out.write(json.dumps(future.result(), ensure_ascii=False) + '\n')
                out.flush()
                finished += 1
            path.unlink()
            ahead.join()
            rate = finished / max(1, time.time() - started)
            print(f"[{index + 1}/{len(bundles)}] {bundle['name']}: {len(futures)} papers; "
                  f"{finished} done this run, {rate * 60:.0f}/min", flush=True)
    print('Extraction finished.', flush=True)


# ============================================================================ departments

PROGRAMME_TYPES = [
    (r'integrated', 'B.Tech Integrated'), (r'mba\s*tech', 'MBA Tech'), (r'master of technology|\bm\s*tech\b', 'M.Tech'),
    (r'master of computer applications|\bmca\b', 'MCA'), (r'diploma', 'Diploma'), (r'pgdm', 'PGDM'),
    (r'\bphd\b', 'PhD'), (r'b\.?\s*tech', 'B.Tech'),
]
DEPARTMENTS = [
    (r'cyber', 'Cyber Security'),
    (r'csbs', 'Computer Science and Business Systems'),
    (r'aiml|machine learning', 'AI and Machine Learning'),
    (r'aids|artificial intelligence & data science|ai & ds', 'AI and Data Science'),
    (r'data scien|\bds\b|cseds', 'Data Science'),
    (r'artifi|\bai\b', 'Artificial Intelligence'),
    (r'master of computer applications|\bmca\b', 'Computer Applications (MCA)'),
    (r'computer science|\bcs\b', 'Computer Science'),
    (r'computer|\bcomp\b', 'Computer Engineering'),
    (r'\bi\s?t\b|information technology', 'Information Technology'),
    (r'extc|telecom', 'Electronics and Telecommunication'),
    (r'electronic', 'Electronics'),
    (r'electrical', 'Electrical'),
    (r'mechatronic', 'Mechatronics'),
    (r'mechanical', 'Mechanical'),
    (r'civil', 'Civil'),
    (r'chemical', 'Chemical'),
    (r'manufactur', 'Manufacturing'),
    (r'industrial automation', 'Industrial Automation'),
    (r'real estate', 'Real Estate and Construction Management'),
    (r'open elective', 'Open Electives'),
    (r'\bphd\b', 'PhD Research'),
]
COMMON = 'Common (all branches)'


def programme_type(programme):
    low = programme.lower()
    return next((name for pattern, name in PROGRAMME_TYPES if re.search(pattern, low)), 'Other')


def department(programme):
    """Department a programme label belongs to; labels without a branch are first-year / all-stream papers."""
    low = programme.lower().replace('_', ' ')
    return next((name for pattern, name in DEPARTMENTS if re.search(pattern, low)), COMMON)

# ============================================================================ reading a paper

FOOTER = re.compile(r'(?i)^\s*(\*{3,}.*\*{3,}|page\s*\d+\s*(of\s*\d+)?|-+\s*\d+\s*-+|\d{1,2}\s*\|\s*page.*|'
                    r'(\*+\s*)?(end of (the )?(question )?paper|all the best|best of luck)(\s*\*+)?)\s*$')
INSTRUCTION = re.compile(r'(?i)compulsory|attempt|figures? (in|to)|full marks|assume|answer(s)? to each|'
                         r'instructions?|candidates? should|carry equal|fresh page|calculators?|'
                         r'question paper contains|in all \d|out of (the )?remaining|to be attempted|answer book|'
                         r'provided for (their|your) use')
# Instruction sentences that never belong to a question (kept out of question text, never drop a question).
BOILERPLATE = re.compile(r'(?i)answer book|provided for (their|your) use|candidates? should read|carry equal marks|'
                         r'to be attempted|fresh page|figures? (in|to|on) (the )?(brackets|right)|is compulsory')
# Paper header lines (who/when/what), skipped when they appear before the first question.
HEADER_LINE = re.compile(r'(?i)^\W{0,3}(svkm|nmims|mukesh|narsee|school of|mpstme|(academic|acad\.?) ?year|'
                         r'program(me)?s?\b|stream|subject|course|date\b|time\b|duration|(max(imum)?\.? ?)?marks|'
                         r'year\b|sem(ester)?\b|trim(ester)?\b|batch|no\.? of pages|(final|re)[\s-]*exam|'
                         r'examination|term end|section\b|part\b|nb\b|note\b)')
TAGS = [
    ('co', re.compile(r'\b[CG]\s?[O0]\s?[-–.:]?\s?(\d{1,2}(?:\s*[,&/]\s*\d{1,2})*)\b[\s;,:]*')),
    ('bl', re.compile(r'\bB\s?L\s?[-–.:]?\s?(\d)\b[\s;,:]*')),
    ('so', re.compile(r'\b[SP]\s?[O0]\s?[-–.:]?\s?([\dlI](?:\s*[,&]\s*\d)*)\b[\s;,:]*')),
]
QUESTION_START = re.compile(       # OCR reads "Q1" as "Ql"/"QI" and "Q5" as "QS"
    r'^(?:Q(?:ue(?:stion|s)?)?\s*[.\-–:]?\s*(?:No\.?\s*[.\-–:]?\s*)?|Q\s*)(\d{1,2}|[lIS](?=[\s.):]|$)|(?:I{2,3}|IV|VI{0,3}|IX|XI{0,2}|V)(?=[\s.):]|$))'
    r'\s*[.):\-]?\s*(.*)$', re.I)
NUMBER_START = re.compile(r'^(\d{1,2})(?:\s*[.)]\s+|\s+(?=[A-Z(\[]))(\S.*)$')   # "1. Explain", "2) ...", "3 (a) ..."
SUBQUESTION_START = re.compile(r'^(\d{1,2})\s*\)\s*(.*)$')          # "1)" inside "Q2 Attempt any 4"
QPART_START = re.compile(r'^(?:Q\.?\s*)?(\d{1,2})\.?\(?([a-hA-H])\)?[\s._):]+(.*)$')   # "1.a", "1b", "2(a)", "Q3a"
ROMAN_QUESTION = re.compile(r'^(I{1,3}|IV|VI{0,3}|IX|X)\s*[.)]\s+(\S.*)$')   # upper-case "II. Attempt any four"
ROMAN_VALUE_Q = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
PART_START = re.compile(   # groups: 1 "(a)"  2 "a." "b)" "B -" "b__|"  3 "c   text" (table cell)  4 "A Write"  5 rest
    r'^[.,\'"`~_\-]*(?:[({\[]\s*([a-hj-k])\s*[)}\]]|([a-hj-k])\s*[.)_~:|\-]+(?=\s|$)|'
    r'([a-hj-k])(?=\s{3})|([a-hj-k])(?=\s[A-Z]))\s*(.*)$', re.I)
ROMAN_START = re.compile(r'^\(?\s*(i{1,3}|iv|vi{0,3}|ix|x)\s*[.)]\s*(.*)$', re.I)
MARKS_END = re.compile(
    r'(?:[\[({|]\s*[0O]?(\d{1,2}(?:\.\d)?)\s*(?:m|marks?)?\s*[\])}|]?'      # [5]  (10)  [04  (5 Marks)
    r'|[0O]?(\d{1,2}(?:\.\d)?)\s*[\])}]'                                     # 04]  5)
    r'|(?<=\s{3})(\d{1,2}(?:\.5)?)'                                           # number alone in a marks column
    r'|\b(\d{1,2})\s*(?:m|marks)\b\.?'                                        # 5M  10 marks
    r'|(?<=[.?):\]’\'"]\s)(\d{1,2}(?:\.5)?)'                                  # "... rank. 6" on scanned papers
    r'|(?<=\s)([0O][1-9S]))\s*$', re.I)                                       # zero-padded "04", OCR "OS" = 05
SEPARATOR = re.compile(r'^\s*(OR|\(?OR\)?)\s*$', re.I)
# A numbered line that is one of the paper's instructions, not a question.
INSTRUCTION_TEXT = re.compile(
    r'(?i)^\W*(?:question\s*(?:no\.?)?\s*\S{1,3}\s+is\s+compulsory|out of (?:the )?remaining|'
    r'attempt any \w+(?: questions?)?\s*(?:out of|from)?\s*(?:the )?remaining|in all \w+ questions|'
    r'all questions (?:carry|are compulsory)|answers? to (?:each|the|every) new question|'
    r'figures? (?:to|in|on) the right|assume (?:any )?suitable|candidates? should|use of .{0,40}calculator|'
    r'this question paper contains|each question (?:carries|is of)|draw neat .{0,40}wherever|'
    r'(?:start|begin) each (?:new )?question)')


def paper_header(text):
    """Max marks, duration, date, exam title, academic year and semester printed at the top of a paper."""
    head = text[:2500]
    info = {}
    match = re.search(r'(?i)(?:max(?:imum)?\.?\s*)?marks\s*[:\-]?\s*(\d{2,3})\b', head)
    if match and 10 <= int(match.group(1)) <= 200:
        info['max_marks'] = int(match.group(1))
    match = (re.search(r'(?i)\(?\s*(\d{1,2})[:.](\d{2})\s*hrs?', head)                       # "(03:00 Hrs.)"
             or re.search(r'(?i)(?:duration|time\s*allowed|time)\s*[:\-]?[^\n]{0,40}?(\d+(?:\.\d+)?)()\s*\(?\s*(?:hrs?|hours?)', head))
    if match:
        hours = float(match.group(1)) + (int(match.group(2)) / 60 if match.group(2) else 0)
        if 0 < hours <= 6:
            info['duration_hours'] = int(hours) if hours.is_integer() else round(hours, 2)
    match = re.search(r'(?i)date\s*[:\-]?\s*(\d{1,2}(?:st|nd|rd|th)?[\s/.,-]+(?:[A-Za-z]{3,9}|\d{1,2})[\s/.,-]+\d{2,4})', head)
    if match:
        info['exam_date'] = re.sub(r'\s+', ' ', match.group(1)).strip(' ,')
    match = re.search(r'(?i)(re[\s-]?exam(?:ination)?|supplementary|final\s+exam(?:ination)?|end[\s-]?sem(?:ester)?|'
                      r'mid[\s-]?(?:term|sem(?:ester)?)|term\s*test|internal|ktc)', head)
    if match:
        info['exam_title'] = re.sub(r'\s+', ' ', match.group(1)).title()
    match = re.search(r'(?i)(?:acad(?:emic)?\.?\s*year|exam year)\s*[:\-]?\s*((?:19|20)\d\d)\s*[-–]\s*(?:19|20)?(\d\d)', head)
    if match:
        start = int(match.group(1))
        if int(match.group(2)) == (start + 1) % 100 and 1995 <= start <= 2030:   # a real consecutive pair
            info['academic_year'] = f'{start}-{match.group(2)}'
    match = re.search(r'(?i)(?:semester|sem|trimester|trim)\s*[:\-]?\s*([IVX]{1,4}|\d{1,2})\b', head)
    if match:
        info['semester_printed'] = match.group(1).upper()
    return info


def number(text):
    text = text.replace('O', '0').replace('o', '0').replace('S', '5').replace('s', '5')
    try:
        value = float(text)
    except ValueError:
        return None
    return int(value) if value.is_integer() else value


# OCR renderings of the CO / SO / BL columns at the start of a line ("SO];", "BE?", "Biel", "C04,").
LEADING_TAG = re.compile(r'^(?:[|!\[\]]\s*)*(?:[CG][O0o][\s\-–.:]*([\dlI]{1,2})|S[O0o](?:[\s\-–.:]*[\dlI\]\[!|]{1,2}|[\-–:])'
                         r'|P[O0][\s\-–.:]*\d{1,2}|B[LlIi1E][\s\-–.:]*([\d?Sel]{0,2})|ae|ee|Bee|See)(?=\W|$)\s*[;,:|]*\s*')


def take_tags(line, item):
    line = re.sub(r'\s+\|\s+|^\|\s*|\s*\|$', '   ', line).strip()      # OCR'd table borders
    while (match := LEADING_TAG.match(line)) and match.end() > 0:
        if item is not None and match.group(1) and match.group(1).isdigit():
            item.setdefault('co', 'CO' + match.group(1))
        if item is not None and match.group(2) and match.group(2).isdigit():
            item.setdefault('bl', 'BL' + match.group(2))
        line = line[match.end():]
    line = re.sub(r'^¢(?=[\s.)|])', 'c', line)                         # OCR reads "c" as "¢"
    line = re.sub(r'(?i)(?:^|\s{3})(?:marks|co|bl|so|q\.?\s*no\.?)(?:\s+(?:marks|co|bl|so))*\s*$', '', line)  # headers
    for key, pattern in TAGS:
        for match in pattern.finditer(line):
            value = re.sub(r'\s+', '', match.group(1)).replace('l', '1').replace('I', '1')
            if key != 'so' and item is not None:
                item.setdefault(key, f"{key.upper()}{value}")
        line = pattern.sub(' ', line)
    return re.sub(r'^[\s;,:|/]+|[\s;,|/]+$', '', re.sub(r'(?:\s*/\s*){2,}', ' ', line))


def take_marks(line):
    line = re.sub(r'(?<=[)\]\d])[\s\\|.,\'`~_]{1,4}$', '', line)      # OCR debris after "(7)"
    alone = re.fullmatch(r'\s*[\[(]?\s*(\d{1,2}(?:\.5)?)\s*[\])]?\s*', line)   # a line that is only "20" or "[10]"
    if alone and 0 < float(alone.group(1)) <= 100:
        return '', number(alone.group(1))
    match = MARKS_END.search(line)
    if not match:
        return line, None
    value = number(next(g for g in match.groups() if g))
    if value is None or not 0 < value <= 100:
        return line, None
    rest = line[:match.start()].rstrip(' ;,:|-')
    if re.search(r'[=+\-*/^]\s*$', rest):            # "... = 10" is part of an equation, not marks
        return line, None
    if re.search(r'(?i)\b(any|of|all|from|attempt|question|questions|q\.?|no\.?|first|last|than)\s*[(\[]?\s*$', rest):
        return line, None                           # "(Attempt any 4)", "Question 3)" are not marks
    return rest, value


def question_number(label, roman=False):
    """'3' -> '3'; OCR 'l'/'I' -> '1', 'S' -> '5'; Roman 'II', 'IV' -> '2', '4'."""
    if label.upper() in ROMAN_VALUE_Q and (roman or label.lower() not in ('l', 'i', 's')):
        return str(ROMAN_VALUE_Q[label.upper()])
    return {'l': '1', 'i': '1', 's': '5'}.get(label.lower(), label)


INSTITUTION = re.compile(r'(?i)svkm|nmims|narsee\s*monjee|mukesh\s*patel')
EXAM_HEADER = re.compile(r'(?i)\bsubject\b|\bmarks\b|instructions?|examination|\bdate\b|\btime\b|\bduration')


def split_papers(text):
    """Split a file holding several papers (e.g. a Final and a Re-exam scanned together) at each new paper header:
    an institution line followed within 15 lines by at least two exam-header lines (Subject, Marks, Date, ...)."""
    lines = text.split('\n')
    starts = [0]
    for index, line in enumerate(lines):
        if index - starts[-1] < 20 or not INSTITUTION.search(line):
            continue
        window = lines[index:index + 15]
        if sum(bool(EXAM_HEADER.search(l)) for l in window) >= 2:
            starts.append(index)
    return ['\n'.join(lines[a:b]) for a, b in zip(starts, starts[1:] + [len(lines)])]


def instructions_end(lines):
    """Index of the first line after the paper's instruction block (0 when there is none).

    The block starts at an "Instructions" heading and continues through its numbered list (1., 2., ...) and
    lines that read like instructions; the first other line is where the questions begin."""
    head = next((i for i, line in enumerate(lines[:60]) if re.match(r'(?i)^\W{0,3}instructions?\b', line.strip())), None)
    if head is None:
        return 0
    expected, index = 1, head + 1
    while index < len(lines):
        line = lines[index].strip()
        numbered = NUMBER_START.match(line)
        if numbered and int(numbered.group(1)) == expected:
            expected += 1
        elif not (INSTRUCTION.search(line) and not ROMAN_QUESTION.match(line)) and not (
                expected > 1 and not numbered and len(line) < 90 and index + 1 < len(lines)
                and NUMBER_START.match(lines[index + 1].strip())
                and int(NUMBER_START.match(lines[index + 1].strip()).group(1)) == expected):
            break                                       # neither a numbered instruction nor a wrapped one
        index += 1
    return index


def parse_questions(text):
    """Split a paper's text into questions and parts with marks and CO/BL tags (best effort)."""
    lines = [l for l in text.split('\n') if l.strip() and not FOOTER.match(l) and not l.startswith('--- page')]
    # Skip the header and instructions: start at the first "Q1"-style line that is not itself an instruction
    # ("Question No. 1 is compulsory"); papers numbered "1." start after the last instruction line instead.
    def instruction_about_q1(rest):                    # "Question No. 1 is compulsory"
        return bool(re.match(r'(?i)(is|carries|will|must|from)\b', rest)) or (
            'compulsory' in rest.lower() and len(rest) < 40)

    # Questions start right after the instructions block. Without an instructions heading, start at the first
    # question marker of any number (a "Q1" can be garbled, and a stray "q I" can sit inside a figure later on).
    start = instructions_end(lines)
    if start == 0:
        first = next(((i, question_number(m.group(1))) for i, line in enumerate(lines)
                      if (m := QUESTION_START.match(take_tags(line.strip(), None)))
                      and not instruction_about_q1(m.group(2))), None)
        if first and first[1] == '1' and not any(
                NUMBER_START.match(take_tags(l.strip(), None)) and not INSTRUCTION.search(l) and not HEADER_LINE.match(l)
                for l in lines[:first[0]]):
            start = first[0]                            # the header runs up to a genuine Q1
    body = lines[start:]

    def sequence_length(pattern):
        """Length of the run 1, 2, 3, ... found in order among lines matching a numbering pattern."""
        expected = 1
        for line in body:
            found = pattern.match(take_tags(line.strip(), None))
            if found and question_number(found.group(1)) == str(expected):
                expected += 1
        return expected - 1

    q_count = sum(1 for l in body if QUESTION_START.match(take_tags(l, None)))
    # Q-numbered unless Q markers are scarce and a clean "1.", "2.", "3.", "4." run exists instead.
    q_style = q_count >= 2 and not (q_count <= 2 and sequence_length(NUMBER_START) >= 4)
    # Papers with "I.", "II." as questions and "1.", "2." under them: Arabic numbers become sub-questions.
    roman_style = not q_style and sum(1 for l in body if ROMAN_QUESTION.match(l.strip())) >= 2
    questions, current, item, sub = [], None, None, ''

    def new_item(part):
        nonlocal item
        item = {'part': f'{sub}.{part}' if sub else part, 'lines': []}
        current['parts'].append(item)
        return item

    def upcoming_label(index):
        """Question number on one of the next three lines, if any (table cells centre the number vertically)."""
        for ahead in body[index + 1:index + 4]:
            pattern = QUESTION_START if q_style else ROMAN_QUESTION if roman_style else NUMBER_START
            found = pattern.match(take_tags(ahead.strip(), None))
            if found:
                return int(question_number(found.group(1), roman_style))
        return None

    for index, raw in enumerate(body):
        line = take_tags(raw.strip(), item)
        if not line:
            continue
        if SEPARATOR.match(line):
            if item is not None:
                item['lines'].append('OR')
            continue
        combined = QPART_START.match(line)
        if combined:
            previous = int(current['question']) if current else 0
            label = combined.group(1)
            if previous < int(label) <= previous + 3:
                current = {'question': label, 'stem': [], 'marks': None, 'parts': []}
                questions.append(current)
                sub = ''
            if int(label) == int(current['question']) if current else False:
                item = None
                new_item(combined.group(2).lower())
                line, marks = take_marks(combined.group(3).strip())
                if marks is not None:
                    item['marks'] = marks
                if line:
                    item['lines'].append(line)
                continue
        if q_style:
            match = QUESTION_START.match(line)
        elif roman_style:
            match = ROMAN_QUESTION.match(line)
        else:
            match = NUMBER_START.match(line)
            alone = re.fullmatch(r'(\d{1,2})\W{0,2}', line)          # the next number alone on a line (table layout)
            if not match and alone and int(alone.group(1)) == (int(current['question']) + 1 if current else 1):
                match = re.match(r'(\d{1,2})()', line)
        if match and not q_style and INSTRUCTION_TEXT.match(match.group(2)):
            # A numbered instruction. Before any real question it means what came before were instructions too,
            # so start over; after real questions (a closing note) just skip the line.
            real = any(q['marks'] or any(p.get('marks') for p in q['parts'])
                       or len(' '.join(q['stem'] + [l for p in q['parts'] for l in p['lines']])) > 200
                       for q in questions)
            if not real:
                questions, current, item, sub = [], None, None, ''
            continue
        if match:
            label = match.group(1)
            label = question_number(label, roman_style)
            previous = int(current['question']) if current else 0
            rest = match.group(2).strip().lstrip('~_-:.;,|\'"` ')
            if previous < int(label) <= previous + 3:   # next question (tolerates a skipped number)
                current = {'question': label, 'stem': [], 'marks': None, 'parts': []}
                questions.append(current)
                item, sub = None, ''
                line = rest
            elif int(label) == previous:                # the same number repeated by a table layout
                line = rest
            if not line:
                continue
        if current is None:
            if HEADER_LINE.match(line) or INSTRUCTION.search(line) or INSTRUCTION_TEXT.match(line) or len(line) < 4:
                continue
            # Text before the first recognised question number (OCR often garbles "Q1"): keep it.
            current = {'question': '0', 'stem': [], 'marks': None, 'parts': [], 'implicit': True}
            questions.append(current)
        numbered = (SUBQUESTION_START.match(line) if q_style
                    else NUMBER_START.match(line) or re.match(r'^(\d{1,2})\s*[.)]\s*(.*)$', line) if roman_style
                    else None)
        if numbered and int(numbered.group(1)) == (int(sub) + 1 if sub else 1):
            sub, item = numbered.group(1), None          # next numbered sub-question; parts become "1.a"
            line = numbered.group(2).strip()
            if not line:
                continue
            new_item('')
            item['part'] = sub
        part = PART_START.match(line)
        if (part and current['parts'] and next(g for g in part.groups()[:4] if g).lower() == 'a'
                and upcoming_label(index) == int(current['question']) + 1):
            # Part (a) of the next question, printed above its centred question number: start that question now.
            current = {'question': str(int(current['question']) + 1), 'stem': [], 'marks': None, 'parts': []}
            questions.append(current)
            item, sub = None, ''
        if part and not part.group(1):
            # Unbracketed letters must follow the sequence: "b." or a table cell may skip up to two letters that
            # OCR lost; "A Write ..." must be exactly the next letter, so "A PLC program ..." opens no part.
            last = item['part'].split('.')[-1].split('(')[0] if item is not None and item['part'] else ''
            letter = next(g for g in part.groups()[:4] if g).lower()
            if len(last) == 1 and last.isalpha():
                allowed = [chr(ord(last) + n) for n in ((1,) if part.group(4) else (1, 2, 3))]
            else:
                allowed = ['a'] if part.group(4) else ['a', 'b', 'c']
            if letter not in allowed:
                part = None
        roman = ROMAN_START.match(line) if not part else None
        if part:
            new_item(next(g for g in part.groups()[:4] if g).lower())
            line = part.group(5)
            inline = ROMAN_START.match(line)            # "c) i) Calculate ..." on one line
            if inline and inline.group(1).lower() == 'i':
                base = item['part']
                new_item('')
                item['part'] = f'{base}(i)'
                line = inline.group(2)
        elif roman:                                     # (i), ii) ... nest under the current lettered part
            base = item['part'].split('(')[0] if item is not None and item['part'] else sub
            new_item('')
            item['part'] = f"{base}({roman.group(1).lower()})"
            line = roman.group(2)
        line, marks = take_marks(line)
        if marks is not None:
            if item is None:
                current['marks'] = current['marks'] or marks
            elif item.get('marks') is None:
                item['marks'] = marks
        line = line.strip()
        if line and line.lower() not in ('marks', 'marks co bl', 'q. no.', 'q.no.', 'question', 'q no') \
                and not (len(line) < 160 and (INSTRUCTION_TEXT.match(line) or BOILERPLATE.search(line))):
            (item['lines'] if item is not None else current['stem']).append(line)
    # Name the implicit question: it is question 1 when the first numbered one found is 2, else unnumbered.
    for position, question in enumerate(questions):
        if question.get('implicit'):
            following = next((q['question'] for q in questions[position + 1:] if not q.get('implicit')), None)
            question['question'] = '1' if following == '2' else None
            question['note'] = ('question number not printed or not readable' if following == '2' else
                                'paper not split into questions' if following is None else
                                'text before the first numbered question')
    out = []
    for question in questions:
        stem = ' '.join(question['stem']).strip()
        parts = [p for p in question['parts'] if ' '.join(p['lines']).strip() or p.get('marks')]
        if question.get('note') and len(stem) + sum(len(' '.join(p['lines'])) for p in parts) < 40:
            continue                                    # a stray fragment, not content
        if not parts:
            if stem:
                record = {'question': question['question'], 'part': None, 'text': stem, 'marks': question['marks']}
                if question.get('note'):
                    record['note'] = question['note']
                out.append(record)
            continue
        if len(stem) > 120:                            # a full question or case text, not just "Answer briefly"
            out.append({'question': question['question'], 'part': None, 'text': stem, 'marks': question['marks'],
                        **({'note': question['note']} if question.get('note') else {})})
        for part in parts:
            record = {'question': question['question'], 'part': part['part'],
                      'text': ' '.join(part['lines']).strip(), 'marks': part.get('marks')}
            if stem and len(stem) <= 120:
                record['question_stem'] = stem
            if question['marks'] is not None:
                record['question_marks'] = question['marks']
            if question.get('note'):
                record['note'] = question['note']
            for key in ('co', 'bl'):
                if part.get(key):
                    record[key] = part[key]
            out.append(record)
    return out


# ============================================================================ build stage

QUESTION_FIELDS = ['subject', 'academic_year', 'exam', 'semester', 'departments', 'paper_id', 'question', 'part',
                   'question_stem', 'text', 'marks', 'question_marks', 'co', 'bl', 'note', 'extraction',
                   'text_quality']
PAPER_FIELDS = ['paper_id', 'subject', 'kind', 'academic_year', 'academic_year_filed', 'exam', 'exam_printed', 'semester', 'departments', 'programme_types',
                'programmes', 'max_marks', 'duration_hours', 'exam_date', 'pages', 'extraction', 'ocr_confidence',
                'questions_extracted', 'papers_in_file', 'text_quality', 'source_path', 'identical_copies', 'text_status']


def load_texts(path):
    """Extracted text by SHA-256 from texts.jsonl, or from the committed shard folder."""
    path = Path(path)
    files = sorted(path.glob('*.jsonl.gz')) if path.is_dir() else [path]
    texts = {}
    for file in files:
        opener = gzip.open if file.name.endswith('.gz') else open
        with opener(file, 'rt', encoding='utf-8') as stream:
            for line in stream:
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue                            # a line cut off by an interrupted extraction
                texts[record['sha256']] = record
    return texts


def save_text_cache(texts, folder=TEXT_CACHE):
    """Committed copy of all extracted text in 16 shards (by first hex digit of the SHA-256), sorted and with a
    fixed gzip timestamp so rebuilds are byte-identical and every file stays far below GitHub's size limits."""
    folder.mkdir(parents=True, exist_ok=True)
    for old in folder.glob('*.jsonl.gz'):
        old.unlink()
    shards = defaultdict(list)
    for sha in sorted(texts):
        shards[sha[0]].append(texts[sha])
    for digit, records in shards.items():
        with open(folder / f'{digit}.jsonl.gz', 'wb') as raw, \
                gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='') as stream:
            for record in records:
                stream.write((json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n').encode('utf-8'))


def documents(record):
    """(label, pages) for each readable document in an extracted file; ZIPs yield one per paper inside."""
    if record.get('pages'):
        yield '', record['pages']
    for member in record.get('members', []):
        for label, pages in documents(member):
            yield (member['name'] + (' / ' + label if label else '')), pages


def page_text(pages):
    return '\n'.join((f'--- page {p["page"]} ---\n' if i else '') + p['text'] for i, p in enumerate(pages))


def extraction_summary(pages):
    methods = Counter(p['method'] for p in pages)
    confidences = [p['ocr_confidence'] for p in pages if p.get('ocr_confidence') is not None]
    method = 'ocr' if methods['ocr'] and not methods['text'] else 'text' if methods['text'] and not methods['ocr'] \
        else 'mixed' if methods['ocr'] else next(iter(methods), 'none')
    return method, (round(math.fsum(confidences) / len(confidences), 1) if confidences else None)


def year_key(year):
    return int(year[:4]) if year[:4].isdigit() else 0


def year_order(year):
    """Sort key for academic years with a deterministic tie-break ('2025' before '2025-26')."""
    return year_key(year), year


def fence(text):
    ticks = '````'
    while ticks in text:
        ticks += '`'
    return ticks


def md_escape(text):
    return str(text).replace('|', '\\|')


def cmd_build(args):
    sys.path.insert(0, str(HERE))
    from organize_by_subject import subject_folders, caseless
    source = Path(args.texts) if args.texts else TEXT_CACHE
    if not source.exists():
        raise SystemExit(f'{source} not found; run extract first or pass --texts.')
    texts = load_texts(source)
    if args.texts:
        save_text_cache(texts)
    drop_ocr_noise(texts, known_words(texts))               # after saving: the cache keeps the raw OCR
    with INDEX_CSV.open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream))
    by_subject = defaultdict(lambda: defaultdict(list))         # subject -> sha -> copies
    for row in rows:
        by_subject[row['subject']][row['sha256']].append(row)
    folders = subject_folders(by_subject)
    stats, summary = Counter(), []
    for subject in sorted(by_subject, key=caseless):
        summary.append(build_subject(subject, by_subject[subject], HERE / 'subjects' / folders[subject], texts, stats))
        summary[-1]['folder'] = folders[subject]
    dept_subjects = defaultdict(list)
    for row in summary:
        for dept in row['departments']:
            dept_subjects[dept].append(row)
    write_department_pages(dept_subjects)
    write_bank_readme(stats, summary, dept_subjects)
    print(f"{len(summary)} subjects; {stats['questions']} questions from {stats['question_papers_read']} question "
          f"papers ({stats['question_papers_split']} split into 3+ questions); "
          f"{stats['papers_not_extracted']} papers not extracted yet.")


def known_words(texts):
    """Words found in at least 3 papers that have an exact PDF text layer: real English and technical vocabulary."""
    papers_with = Counter()
    for record in texts.values():
        seen = set()
        for _, pages in documents(record):
            for page in pages:
                if page['method'] in ('text', 'docx'):
                    seen.update(w.lower() for w in re.findall(r'[A-Za-z]{3,}', page['text']))
        papers_with.update(seen)
    return {word for word, count in papers_with.items() if count >= 3}


def ocr_noise(line, known):
    """An OCR line read from a stamp, scribble or blank area: few real words, or mostly one- and two-letter bits."""
    if re.search(r'(?i)\bQ\.?\s*\d|\bmarks?\b', line):     # question numbers and marks are always kept
        return False
    words = re.findall(r'[A-Za-z]{3,}', line)
    if len(words) >= 4 and sum(w.lower() in known for w in words) < 0.4 * len(words):
        return True
    bits = [b for b in line.split() if not re.fullmatch(r'[\d.,%()+/=\-]+', b)]      # numbers are table data
    if any(len(w) >= 4 and w.lower() in known for w in words):   # "Inorder: A, B, C", "F is conservative"
        return False
    return len(bits) >= 6 and sum(bool(re.fullmatch(r'\W*[A-Za-z]{1,2}\W*', b)) for b in bits) > 0.7 * len(bits)


def drop_ocr_noise(texts, known):
    """Remove noise lines from OCR pages in place, recording how many were dropped on each page."""
    for record in texts.values():
        for _, pages in documents(record):
            for page in pages:
                if page['method'] == 'ocr':
                    lines = page['text'].split('\n')
                    kept = [line for line in lines if not ocr_noise(line, known)]
                    if len(kept) < len(lines):
                        page['omitted_lines'] = len(lines) - len(kept)
                        page['text'] = '\n'.join(kept)


def build_subject(subject, papers, folder, texts, stats):
    """Write papers.md, answer_keys.md, papers.jsonl and questions.jsonl for one subject; return its summary."""
    folder.mkdir(parents=True, exist_ok=True)
    paper_blocks, answer_blocks, paper_lines, question_lines = [], [], [], []
    dept_papers, dept_questions, years = Counter(), Counter(), set()

    def printed_year(sha):
        docs = list(documents(texts[sha])) if sha in texts else []
        return paper_header(page_text(docs[0][1])).get('academic_year') if docs else None

    # The academic year printed on the paper is when it was set; file names often give the batch year instead.
    best_year = {sha: printed_year(sha) or min(copies, key=lambda r: r['path'])['academic_year']
                 for sha, copies in papers.items()}

    def order(item):
        first = min(item[1], key=lambda r: r['path'])
        kind = {'Question paper': 0, 'Answer key': 1}.get(first['kind'], 2)
        return (-year_key(best_year[item[0]]), first['exam'], kind, first['path'])

    for sha, copies in sorted(papers.items(), key=order):
        copies = sorted(copies, key=lambda r: r['path'])
        first = copies[0]
        programmes = sorted({c['programme'] for c in copies}, key=lambda p: (p.lower(), p))
        departments = sorted({department(p) for p in programmes})
        dept_papers.update(departments)
        year = best_year[sha]
        if year:
            years.add(year)
        paper = {'paper_id': sha[:12], 'subject': subject, 'kind': first['kind'], 'academic_year': year,
                 'academic_year_filed': first['academic_year'] if first['academic_year'] != year else None,
                 'exam': first['exam'], 'semester': first['semester'], 'departments': departments,
                 'programme_types': sorted({programme_type(p) for p in programmes}), 'programmes': programmes,
                 'source_path': first['path'], 'identical_copies': len(copies) - 1}
        heading = ' · '.join(b for b in (year or 'Year not stated', first['exam'] or 'Exam not stated',
                                         first['semester'], None if first['kind'] == 'Question paper' else first['kind'])
                             if b) + f' · paper {sha[:12]}'
        meta = [f'- Departments: {", ".join(departments)}', f'- Programmes: {", ".join(programmes)}',
                f'- Source: `{first["path"]}`' + (f' (+{len(copies) - 1} identical copies)' if len(copies) > 1 else '')]
        target = answer_blocks if first['kind'] == 'Answer key' else paper_blocks
        record = texts.get(sha)
        docs = list(documents(record)) if record else []
        if not docs:
            status = 'not extracted yet' if record is None else (record.get('error') or record.get('note')
                                                                 or 'no readable pages')
            stats['papers_not_extracted' if record is None else 'papers_without_text'] += 1
            paper['text_status'] = status
            paper_lines.append(json.dumps({k: paper[k] for k in PAPER_FIELDS if paper.get(k) not in (None, '', [])},
                                          ensure_ascii=False))
            target.append('\n'.join([f'## {heading}', ''] + meta + [f'- Text: none ({status})', '']))
            continue
        for number_in_file, (label, pages) in enumerate(docs):
            text = page_text(pages)
            header = paper_header(text)
            method, confidence = extraction_summary(pages)
            for page in pages:
                stats['pages_' + page['method']] += 1
            stats['answer_keys_read' if first['kind'] == 'Answer key' else 'documents_read'] += 1
            doc = dict(paper, paper_id=sha[:12] + (f'-{number_in_file + 1}' if label else ''),
                       pages=len(pages), extraction=method, ocr_confidence=confidence,
                       **{k: header[k] for k in ('max_marks', 'duration_hours', 'exam_date') if k in header})
            if label:
                doc['source_path'] = f"{first['path']} :: {label}"
            if header.get('exam_title'):
                doc['exam_printed'] = header['exam_title']
                if not doc['exam']:
                    doc['exam'] = header['exam_title']
            printed = [f'{k.replace("_", " ")}: {header[k]}' for k in ('max_marks', 'duration_hours', 'exam_date')
                       if k in header]
            lines = [f'## {heading}' + (f' · {label}' if label else ''), ''] + meta
            if printed:
                lines.append('- Printed on paper: ' + '; '.join(printed))
            lines.append(f'- Text: {method} ({len(pages)} page{"s" if len(pages) != 1 else ""})'
                         + (f', mean OCR confidence {confidence}' if confidence is not None else ''))
            omitted = sum(page.get('omitted_lines', 0) for page in pages)
            if omitted:
                lines.append(f'- {omitted} unreadable OCR line{"s" if omitted != 1 else ""} (stamps, scribbles, '
                             'blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.')
            if confidence is not None and confidence < LOW_OCR_CONFIDENCE:
                doc['text_quality'] = 'low'
                stats['low_quality_' + ('answer_keys' if first['kind'] == 'Answer key' else 'papers')] += 1
                lines.append('- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is '
                             'only partly readable. Restore the original file to read it.')
            ticks = fence(text)
            target.append('\n'.join(lines + ['', ticks + 'text', text, ticks, '']))
            # Papers inside a ZIP are question papers too, unless their file name marks them as answers.
            if first['kind'] == 'Question paper' or (
                    first['kind'] == 'ZIP of papers' and not re.search(r'(?i)\b(ans|answers?|solutions?|key)\b', label)):
                # One file can hold several papers (a Final and a Re-exam scanned together): parse each on its own,
                # with the year and exam its own header prints.
                segments = split_papers(text)
                doc['questions_extracted'] = 0
                if len(segments) > 1:
                    doc['papers_in_file'] = len(segments)
                for number, segment in enumerate(segments, 1):
                    parsed = [q for q in parse_questions(segment) if q['text']]
                    own = paper_header(segment) if len(segments) > 1 else {}
                    printed_exam = own.get('exam_title', '').lower()
                    exam = ('Re-Exam' if printed_exam.startswith('re') else 'Final-Exam' if printed_exam.startswith(('final', 'end'))
                            else doc['exam'])
                    stats['question_papers_read'] += 1
                    stats['question_papers_split'] += len({q['question'] for q in parsed}) >= 3
                    doc['questions_extracted'] += len(parsed)
                    for q in parsed:
                        if q.get('question_stem'):
                            q['question_stem'] = q['question_stem'][:300]
                        entry = dict(q, subject=subject, academic_year=own.get('academic_year') or doc['academic_year'],
                                     exam=exam, semester=doc['semester'], departments=departments,
                                     paper_id=doc['paper_id'] + (f'#{number}' if len(segments) > 1 else ''),
                                     extraction=method, text_quality=doc.get('text_quality'))
                        question_lines.append(json.dumps({k: entry[k] for k in QUESTION_FIELDS
                                                          if entry.get(k) not in (None, '', [])}, ensure_ascii=False))
                        stats['questions'] += 1
                        stats['questions_with_marks'] += q.get('marks') is not None or q.get('question_marks') is not None
                    dept_questions.update({d: len(parsed) for d in departments})
            paper_lines.append(json.dumps({k: doc[k] for k in PAPER_FIELDS if doc.get(k) not in (None, '', [])},
                                          ensure_ascii=False))
    span = (f'{min(years, key=year_order)} to {max(years, key=year_order)}' if years else 'years not stated')
    depts = [d for d, _ in dept_papers.most_common()]
    intro = [f'# {subject}: question papers in full', '',
             f'{len(papers)} unique papers · {span} · {", ".join(depts)}', '',
             'Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned '
             'papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: '
             '[`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) '
             '(one record per paper). Index of files: [`README.md`](README.md).', '']
    (folder / 'papers.md').write_text('\n'.join(intro + (paper_blocks or ['No question papers.', ''])),
                                      encoding='utf-8')
    if answer_blocks:
        (folder / 'answer_keys.md').write_text('\n'.join(
            [f'# {subject}: answer keys', '', 'Answer keys and model answers published on the portal, newest first.',
             ''] + answer_blocks), encoding='utf-8')
    elif (folder / 'answer_keys.md').exists():
        (folder / 'answer_keys.md').unlink()
    for name, lines in (('papers.jsonl', paper_lines), ('questions.jsonl', question_lines)):
        (folder / name).write_text(''.join(line + '\n' for line in lines), encoding='utf-8')
    return {'subject': subject, 'departments': depts, 'papers': len(papers), 'questions': len(question_lines),
            'dept_papers': dept_papers, 'dept_questions': dept_questions,
            'first_year': min(years, key=year_order) if years else '',
            'last_year': max(years, key=year_order) if years else ''}


def write_department_pages(dept_subjects):
    root = HERE / 'departments'
    if root.exists():
        shutil.rmtree(root)
    root.mkdir()
    from organize_by_subject import folder_name
    index = ['# Departments', '', 'Subjects grouped by the department (branch) whose programmes set the papers. A '
             'subject taught to several branches is listed under each, with the number of papers set for that '
             'branch. "Common (all branches)" holds first-year and all-stream papers that name no branch.', '',
             '| Department | Subjects | Papers | Questions |', '| --- | ---: | ---: | ---: |']
    for dept in sorted(dept_subjects):
        rows = dept_subjects[dept]
        papers = sum(r['dept_papers'][dept] for r in rows)
        questions = sum(r['dept_questions'][dept] for r in rows)
        index.append(f'| [{dept}]({quote_path(folder_name(dept))}/README.md) | {len(rows)} | {papers} | {questions} |')
        lines = [f'# {dept}', '',
                 f'{len(rows)} subjects, {papers} papers, {questions} extracted questions. Each subject folder holds '
                 '`papers.md` (full text of every paper) and `questions.jsonl` (one record per question with marks, '
                 f'year and exam). Records carry a `departments` field: keep those containing "{dept}" to see only '
                 'this branch\'s papers.', '',
                 '| Subject | Papers for this branch | Questions | Years | Full text | Questions |',
                 '| --- | ---: | ---: | --- | --- | --- |']
        for row in sorted(rows, key=lambda r: r['subject'].lower()):
            link = '../../subjects/' + quote_path(row['folder'])
            span = (f"{row['first_year']} to {row['last_year']}" if row['first_year'] != row['last_year']
                    else row['first_year'] or '—')
            lines.append(f"| [{md_escape(row['subject'])}]({link}/README.md) | {row['dept_papers'][dept]} | "
                         f"{row['dept_questions'][dept]} | {span} | [papers.md]({link}/papers.md) | "
                         f"[questions.jsonl]({link}/questions.jsonl) |")
        (root / folder_name(dept)).mkdir()
        (root / folder_name(dept) / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    (root / 'README.md').write_text('\n'.join(index) + '\n', encoding='utf-8')


def quote_path(text):
    from urllib.parse import quote
    return quote(text)


def write_bank_readme(stats, summary, dept_subjects):
    BANK_DIR.mkdir(exist_ok=True)
    with (BANK_DIR / 'subjects_summary.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['subject', 'folder', 'departments', 'papers', 'questions', 'first_year', 'last_year'])
        for row in summary:
            writer.writerow([row['subject'], 'subjects/' + row['folder'], '; '.join(row['departments']), row['papers'],
                             row['questions'], row['first_year'], row['last_year']])
    split = stats['question_papers_split']
    read = stats['question_papers_read'] or 1
    lines = [
        '# Question bank', '',
        'Every past question paper in the archive as text, organised by subject and department, so a person or an '
        'AI can read, search and analyse it.', '',
        '## Where things are', '',
        '- `subjects/<Subject>/papers.md`: every paper for the subject in full, newest first, each with academic year, '
        'exam, semester, programmes, departments, max marks, duration and date.',
        '- `subjects/<Subject>/questions.jsonl`: one JSON record per question or sub-question (fields below).',
        '- `subjects/<Subject>/papers.jsonl`: one JSON record per paper: departments, programmes, max marks, '
        'duration, date, pages, how the text was read, and the original file path.',
        '- `subjects/<Subject>/answer_keys.md`: answer keys the portal published (2024-25 onwards).',
        '- `departments/<Department>/README.md`: the subjects of each department, with that branch\'s paper counts.',
        '- `question_bank/subjects_summary.csv`: one row per subject with departments, counts and year range.',
        '- `question_bank/extracted_text/*.jsonl.gz`: raw extracted text of every file, page by page, in 16 shards '
        '(input for `python build_question_bank.py build`).', '',
        '## Coverage', '',
        f'- {len(summary):,} subjects in {len(dept_subjects)} departments.',
        f'- {stats["question_papers_read"]:,} question papers and {stats["answer_keys_read"]:,} answer keys read: '
        f'{stats["pages_text"] + stats["pages_docx"]:,} pages from the PDF text layer and {stats["pages_ocr"]:,} '
        'scanned pages by OCR.',
        f'- {stats["questions"]:,} questions and sub-questions extracted; {stats["questions_with_marks"]:,} with marks. '
        f'{split:,} papers ({100 * split / read:.0f}%) split into 3 or more questions; the rest are kept as full text '
        'in papers.md.',
        f'- {stats["low_quality_papers"]:,} question papers have low OCR quality (mostly handwritten 2004-2010 papers '
        'or poor scans); they and their questions are marked `text_quality: low`.',
        f'- Files with no readable text (corrupt PDFs, spreadsheet data sets): {stats["papers_without_text"]:,}.'
        + (f' Not yet extracted: {stats["papers_not_extracted"]:,}.' if stats['papers_not_extracted'] else ''), '',
        '## questions.jsonl fields', '',
        '| Field | Meaning |', '| --- | --- |',
        '| `subject` | Canonical subject name (same as the folder) |',
        '| `academic_year`, `exam`, `semester` | e.g. `2024-25`, `Final-Exam` / `Re-Exam`, `Sem 5`. The year is the one '
        'printed on the paper when it states one (file names often give the batch year; that is kept in '
        '`papers.jsonl` as `academic_year_filed`) |',
        '| `departments` | Branches the paper was set for |',
        '| `paper_id` | First 12 hex digits of the paper file\'s SHA-256; matches `papers.jsonl` for programmes, max '
        'marks, date and source file |',
        '| `question`, `part` | Question number and part, e.g. `2` and `b`, `1.a`, `a(ii)` |',
        '| `question_stem` | Shared instruction of the question, e.g. "Attempt any four" |',
        '| `text` | The question text |',
        '| `marks`, `question_marks` | Marks for this part, and for the whole question when printed |',
        '| `co`, `bl` | Course outcome and Bloom\'s level tags printed on newer papers |',
        '| `extraction` | `text` (exact, from the PDF) or `ocr` (scanned paper read by Tesseract) |',
        '| `text_quality` | `low` when the scan read poorly (handwritten or faint papers); treat the text with care |', '',
        '## Accuracy', '',
        'Text-layer papers (most 2024-25 and 2025-26 papers) are extracted exactly. Older papers are scans read by OCR: '
        'ordinary text is reliable, but equations, symbols and diagrams are often garbled, and diagrams are not '
        'captured. Splitting into questions is automatic; when a layout defeats it, the paper still appears in full '
        'in papers.md. Treat question counts and marks as a strong guide rather than an exact record.', '',
        '## Using it with an AI', '',
        '- Upload `subjects/<Subject>/questions.jsonl` (or `papers.md`) and ask, for example: "Which topics are asked '
        'most often, with typical marks?", "Group these questions by unit", or "Build a practice paper in the same '
        'pattern".',
        '- For a whole department, start from `departments/<Department>/README.md` and take the subjects you need.',
        '- Filter by year, exam or marks with any JSON tool, e.g. `jq \'select(.marks >= 10)\' questions.jsonl`.', '',
        'Rebuild after changing subjects or the parser: `python build_question_bank.py build` (no OCR needed).', '',
    ]
    (BANK_DIR / 'README.md').write_text('\n'.join(lines), encoding='utf-8')


# ============================================================================ papers kept only inside raw portal ZIPs

RAW_MEMBERS = BANK_DIR / 'raw_zip_members.json'
RAW_RESOLVED = BANK_DIR / 'raw_zip_papers.jsonl'


def cmd_extract_raw(args):
    """Read the papers that exist only inside the original portal ZIPs (00_Original_Downloads).

    The archive's own organiser left these out of 02_Question_Papers ("no unambiguous portal path mapping",
    "not listed under this portal folder", or never recorded). question_bank/raw_zip_members.json lists them.
    Each ZIP is rebuilt from its verified release chunks one at a time; every listed member is hashed, files
    already in 02_Question_Papers are recorded as copies, and new ones are read like any other paper."""
    if not shutil.which('tesseract'):
        raise SystemExit('Tesseract OCR is not on PATH; see the instructions at the top of this file.')
    manifest = json.loads(Path(args.manifest).read_text(encoding='utf-8'))
    members = json.loads(RAW_MEMBERS.read_text(encoding='utf-8'))
    work = Path(args.work).resolve()
    for sub in ('bundles', 'chunks', 'zips', 'papers'):
        (work / sub).mkdir(parents=True, exist_ok=True)
    texts_path, resolved_path = work / 'texts.jsonl', work / 'raw_zip_papers.jsonl'
    done_zips = set()
    if resolved_path.exists():
        done_zips = {json.loads(l)['zip_path'] for l in resolved_path.open(encoding='utf-8') if l.strip()}
    known = {f['sha256'] for f in manifest['files'] if f['path'].startswith(QP_ROOT)}
    if texts_path.exists():
        known |= {json.loads(l)['sha256'] for l in texts_path.open(encoding='utf-8') if l.strip()}
    wanted = defaultdict(set)
    for m in members:
        if m['zip_path'] not in done_zips:
            wanted[m['zip_path']].add(m['member'])
    files = {f['path']: f for f in manifest['files']}
    chunk_bundle = {c: v['bundle'] for c, v in manifest['chunks'].items()}
    bundles = {b['name']: b for b in manifest['bundles']}
    legacy = {b['name']: b for b in manifest['legacy']['bundles']}
    needs = defaultdict(set)                            # bundle -> chunk ids or legacy zip paths
    for zip_path in wanted:
        f = files[zip_path]
        if f.get('legacy_bundle'):
            needs[f['legacy_bundle']].add(zip_path)
        else:
            for chunk in f['chunks']:
                needs[chunk_bundle[chunk]].add(chunk)
    order = sorted(needs, key=lambda n: (n in legacy, n))
    chunk_refs = Counter(c for z in wanted if not files[z].get('legacy_bundle') for c in files[z]['chunks'])
    print(f'{len(wanted)} ZIPs to open, {sum(len(v) for v in wanted.values())} members, {len(order)} bundles.', flush=True)

    def ready(zip_path):
        f = files[zip_path]
        if f.get('legacy_bundle'):
            return (work / 'zips' / Path(zip_path).name).exists()
        return all((work / 'chunks' / c).exists() for c in f['chunks'])

    def assemble(zip_path):
        f = files[zip_path]
        target = work / 'zips' / Path(zip_path).name
        if not f.get('legacy_bundle'):
            with target.open('wb') as out:
                for chunk in f['chunks']:
                    out.write((work / 'chunks' / chunk).read_bytes())
                    chunk_refs[chunk] -= 1
                    if chunk_refs[chunk] <= 0:          # a chunk can be shared by several ZIPs
                        (work / 'chunks' / chunk).unlink()
        if target.stat().st_size != f['bytes'] or sha256_file(target) != f['sha256']:
            raise SystemExit(f'Rebuilt ZIP does not match its checksum: {zip_path}')
        return target

    with texts_path.open('a', encoding='utf-8') as texts_out, resolved_path.open('a', encoding='utf-8') as res_out, \
            ProcessPoolExecutor(args.workers) as pool:
        pending, futures, read = set(wanted), [], 0

        def drain(wait=False):
            nonlocal futures, read
            for future in (as_completed(futures) if wait else [f for f in futures if f.done()]):
                texts_out.write(json.dumps(future.result(), ensure_ascii=False) + '\n')
                read += 1
            futures = [] if wait else [f for f in futures if not f.done()]
            texts_out.flush()

        for index, name in enumerate(order, 1):
            meta = legacy.get(name) or bundles[name]
            if name in legacy:
                meta = dict(meta, url=f"https://github.com/{REPO}/releases/download/{manifest['legacy']['release_tag']}/{name}")
            path = download(meta, work / 'bundles' / name, args.download)
            with zipfile.ZipFile(path) as archive:
                for item in needs[name]:
                    source = item if item in files else 'objects/' + item   # whole ZIP (legacy) or a chunk
                    target = work / ('zips' if item in files else 'chunks') / (Path(item).name if item in files else item)
                    with archive.open(source) as src, target.open('wb') as dst:
                        shutil.copyfileobj(src, dst, 1 << 20)
            path.unlink()
            for zip_path in sorted(z for z in pending if ready(z)):
                pending.discard(zip_path)
                local = assemble(zip_path)
                with zipfile.ZipFile(local) as raw:
                    infos = [i for i in raw.infolist() if not i.is_dir()]
                    names = {i.filename for i in infos}
                    targets = names if '*' in wanted[zip_path] else wanted[zip_path]
                    for member in sorted(targets):
                        if member not in names:
                            res_out.write(json.dumps({'zip_path': zip_path, 'member': member, 'missing': True}) + '\n')
                            continue
                        data = raw.read(member)
                        sha = hashlib.sha256(data).hexdigest()
                        res_out.write(json.dumps({'zip_path': zip_path, 'member': member, 'sha256': sha,
                                                  'bytes': len(data)}, ensure_ascii=False) + '\n')
                        if sha in known:
                            continue
                        known.add(sha)
                        paper = work / 'papers' / sha
                        paper.write_bytes(data)
                        futures.append(pool.submit(extract_one, sha, str(paper), PurePosixPath(member).name))
                res_out.flush()
                local.unlink()
            drain()                                     # OCR keeps running while the next bundle downloads
            print(f'[{index}/{len(order)}] {name}: {read} papers read, {len(futures)} queued; '
                  f'{len(pending)} ZIPs pending', flush=True)
        drain(wait=True)
    print(f'Raw ZIP extraction finished: {read} new papers read.', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('extract', help='download papers and read their text (OCR where needed)')
    p.add_argument('--manifest', required=True, help='verified full-library-manifest.json')
    p.add_argument('--work', required=True, help='working folder for the cache and temporary bundles')
    p.add_argument('--workers', type=int, default=os.cpu_count() or 2)
    p.add_argument('--download', choices=['https', 'gh'], default='gh',
                   help='gh: GitHub CLI (default); https: curl to the API, with GITHUB_TOKEN if set')
    p.add_argument('--limit', type=int, help='only the first N bundles (for a trial run)')
    p.set_defaults(run=cmd_extract)
    p = sub.add_parser('extract-raw', help='read papers that exist only inside the original portal ZIPs')
    p.add_argument('--manifest', required=True, help='verified full-library-manifest.json')
    p.add_argument('--work', required=True, help='working folder (needs about 6 GiB free)')
    p.add_argument('--workers', type=int, default=os.cpu_count() or 2)
    p.add_argument('--download', choices=['https', 'gh'], default='gh')
    p.set_defaults(run=cmd_extract_raw)
    p = sub.add_parser('build', help='write papers.md / questions.jsonl per subject and the department indexes')
    p.add_argument('--texts', help='texts.jsonl from extract (also refreshes the committed text cache); '
                                   'default: question_bank/extracted_text.jsonl.gz')
    p.set_defaults(run=cmd_build)
    args = parser.parse_args()
    args.run(args)


if __name__ == '__main__':
    main()
