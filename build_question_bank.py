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
import argparse, csv, gzip, hashlib, io, json, os, re, shutil, subprocess, sys, tempfile, threading, time, zipfile

HERE = Path(__file__).resolve().parent
REPO = 'dhruvpaleja/mpstme-library-archive-2026-10-08'
QP_ROOT = '02_Question_Papers/'
INDEX_CSV = HERE / 'subjects' / 'pyq_subject_index.csv'
BANK_DIR = HERE / 'question_bank'
TEXT_CACHE = BANK_DIR / 'extracted_text'          # 16 gzipped JSONL shards
OCR_DPI = 200
MAX_OCR_PIXELS = 3600            # longest side of a rendered page
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
    return text, round(sum(confidences) / len(confidences), 1) if confidences else None


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
                         r'instructions?|candidates? should|carry equal|fresh page|neat diagram|calculators?|'
                         r'question paper contains|in all \d|out of (the )?remaining')
TAGS = [
    ('co', re.compile(r'\b[CG]\s?[O0]\s?[-–.:]?\s?(\d{1,2}(?:\s*[,&/]\s*\d{1,2})*)\b[\s;,:]*')),
    ('bl', re.compile(r'\bB\s?L\s?[-–.:]?\s?(\d)\b[\s;,:]*')),
    ('so', re.compile(r'\b[SP]\s?[O0]\s?[-–.:]?\s?([\dlI](?:\s*[,&]\s*\d)*)\b[\s;,:]*')),
]
QUESTION_START = re.compile(       # OCR reads "Q1" as "Ql"/"QI" and "Q5" as "QS"
    r'^(?:Q(?:ue(?:stion|s)?)?\s*\.?\s*(?:No\.?\s*)?|Q\s*)(\d{1,2}|[lIS](?=[\s.):]|$))\s*[.):\-]?\s*(.*)$', re.I)
NUMBER_START = re.compile(r'^(\d{1,2})\s*[.)]\s+(\S.*)$')
SUBQUESTION_START = re.compile(r'^(\d{1,2})\s*\)\s*(.*)$')          # "1)" inside "Q2 Attempt any 4"
PART_START = re.compile(                   # (a)  a.  b)  "c   text"  "A Write"  and OCR forms ".B_ Write", "{c)", "B - Write"
    r'^[.,\'"`~_\-]*(?:[({\[]\s*([a-hj-k])\s*[)}\]]|([a-hj-k])\s*[.)_~:\-]+(?=\s)|([a-hj-k])\s*[.)]|'
    r'([a-hj-k])(?=\s{3}|\s[A-Z]))\s*(.*)$', re.I)
ROMAN_START = re.compile(r'^\(?\s*(i{1,3}|iv|vi{0,3}|ix|x)\s*[.)]\s*(.*)$', re.I)
MARKS_END = re.compile(
    r'(?:[\[({|]\s*[0O]?(\d{1,2}(?:\.\d)?)\s*(?:m|marks?)?\s*[\])}|]?'      # [5]  (10)  [04  (5 Marks)
    r'|[0O]?(\d{1,2}(?:\.\d)?)\s*[\])}]'                                     # 04]  5)
    r'|(?<=\s{3})(\d{1,2}(?:\.5)?)'                                           # number alone in a marks column
    r'|\b(\d{1,2})\s*(?:m|marks)\b\.?'                                        # 5M  10 marks
    r'|(?<=\s)([0O][1-9S]))\s*$', re.I)                                       # zero-padded "04", OCR "OS" = 05
SEPARATOR = re.compile(r'^\s*(OR|\(?OR\)?)\s*$', re.I)


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
        info['academic_year'] = f'{match.group(1)}-{match.group(2)}'
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
LEADING_TAG = re.compile(r'^(?:[|!\[\]]\s*)*(?:[CG][O0o][\s\-–.:]*([\dlI]{1,2})|S[O0o][\s\-–.:]*[\dlI\]\[!|]{1,2}'
                         r'|P[O0][\s\-–.:]*\d{1,2}|B[LlIi1E][\s\-–.:]*([\d?Sel]{0,2})|ae|ee|Bee|See)(?=\W|$)\s*[;,:|]*\s*')


def take_tags(line, item):
    line = re.sub(r'\s+\|\s+|^\|\s*|\s*\|$', '   ', line).strip()      # OCR'd table borders
    while (match := LEADING_TAG.match(line)) and match.end() > 0:
        if item is not None and match.group(1) and match.group(1).isdigit():
            item.setdefault('co', 'CO' + match.group(1))
        if item is not None and match.group(2) and match.group(2).isdigit():
            item.setdefault('bl', 'BL' + match.group(2))
        line = line[match.end():]
    line = re.sub(r'^¢\s*[.)]', 'c.', line)
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
    match = MARKS_END.search(line)
    if not match:
        return line, None
    value = number(next(g for g in match.groups() if g))
    if value is None or not 0 < value <= 100:
        return line, None
    rest = line[:match.start()].rstrip(' ;,:|-')
    if re.search(r'[=+\-*/^]\s*$', rest):            # "... = 10" is part of an equation, not marks
        return line, None
    return rest, value


def parse_questions(text):
    """Split a paper's text into questions and parts with marks and CO/BL tags (best effort)."""
    lines = [l for l in text.split('\n') if l.strip() and not FOOTER.match(l) and not l.startswith('--- page')]
    # Skip the header and instructions: start at the first "Q1"-style line that is not itself an instruction
    # ("Question No. 1 is compulsory"); papers numbered "1." start after the last instruction line instead.
    def instruction_about_q1(rest):                    # "Question No. 1 is compulsory"
        return bool(re.match(r'(?i)(is|carries|will|must|from)\b', rest)) or (
            'compulsory' in rest.lower() and len(rest) < 40)

    start = next((i for i, line in enumerate(lines)
                  if (m := QUESTION_START.match(take_tags(line.strip(), None))) and m.group(1) in ('1', 'l', 'I', 'i')
                  and not instruction_about_q1(m.group(2))), None)
    if start is None:
        start = 0
        for index, line in enumerate(lines[:60]):
            if INSTRUCTION.search(line):
                start = index + 1
    body = lines[start:]
    q_style = sum(1 for l in body if QUESTION_START.match(take_tags(l, None))) >= 2
    questions, current, item, sub = [], None, None, ''

    def new_item(part):
        nonlocal item
        item = {'part': f'{sub}.{part}' if sub else part, 'lines': []}
        current['parts'].append(item)
        return item

    for raw in body:
        line = take_tags(raw.strip(), item)
        if not line:
            continue
        if SEPARATOR.match(line):
            if item is not None:
                item['lines'].append('OR')
            continue
        match = QUESTION_START.match(line) if q_style else NUMBER_START.match(line)
        if match:
            label = {'l': '1', 'i': '1', 's': '5'}.get(match.group(1).lower(), match.group(1))
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
            continue
        numbered = SUBQUESTION_START.match(line) if q_style else None
        if numbered and int(numbered.group(1)) == (int(sub) + 1 if sub else 1):
            sub, item = numbered.group(1), None          # next numbered sub-question; parts become "1.a"
            line = numbered.group(2).strip()
            if not line:
                continue
            new_item('')
            item['part'] = sub
        part = PART_START.match(line)
        if part and (part.group(2) or part.group(4)):
            # Loosely written letters ("A Write", "B - Explain") count only as the next letter in sequence,
            # so a sentence starting "A PLC program ..." does not open part (a).
            last = item['part'].split('.')[-1].split('(')[0] if item is not None and item['part'] else ''
            expected = chr(ord(last) + 1) if len(last) == 1 and last.isalpha() else 'a'
            if (part.group(2) or part.group(4)).lower() not in (expected, 'a' if not last else expected):
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
        if line and line.lower() not in ('marks', 'marks co bl', 'q. no.', 'q.no.', 'question', 'q no'):
            (item['lines'] if item is not None else current['stem']).append(line)
    out = []
    for question in questions:
        stem = ' '.join(question['stem']).strip()
        parts = [p for p in question['parts'] if ' '.join(p['lines']).strip() or p.get('marks')]
        if not parts:
            if stem:
                out.append({'question': question['question'], 'part': None, 'text': stem,
                            'marks': question['marks']})
            continue
        for part in parts:
            record = {'question': question['question'], 'part': part['part'],
                      'text': ' '.join(part['lines']).strip(), 'marks': part.get('marks')}
            if stem:
                record['question_stem'] = stem
            if question['marks'] is not None:
                record['question_marks'] = question['marks']
            for key in ('co', 'bl'):
                if part.get(key):
                    record[key] = part[key]
            out.append(record)
    return out


# ============================================================================ build stage

QUESTION_FIELDS = ['subject', 'academic_year', 'exam', 'semester', 'departments', 'paper_id', 'question', 'part',
                   'question_stem', 'text', 'marks', 'question_marks', 'co', 'bl', 'extraction']
PAPER_FIELDS = ['paper_id', 'subject', 'kind', 'academic_year', 'exam', 'semester', 'departments', 'programme_types',
                'programmes', 'max_marks', 'duration_hours', 'exam_date', 'pages', 'extraction', 'ocr_confidence',
                'questions_extracted', 'source_path', 'identical_copies', 'text_status']


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
    return method, (round(sum(confidences) / len(confidences), 1) if confidences else None)


def year_key(year):
    return int(year[:4]) if year[:4].isdigit() else 0


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


def build_subject(subject, papers, folder, texts, stats):
    """Write papers.md, answer_keys.md, papers.jsonl and questions.jsonl for one subject; return its summary."""
    folder.mkdir(parents=True, exist_ok=True)
    paper_blocks, answer_blocks, paper_lines, question_lines = [], [], [], []
    dept_papers, dept_questions, years = Counter(), Counter(), set()

    def order(item):
        first = min(item[1], key=lambda r: r['path'])
        return (-year_key(first['academic_year']), first['exam'], first['kind'], first['path'])

    for sha, copies in sorted(papers.items(), key=order):
        copies = sorted(copies, key=lambda r: r['path'])
        first = copies[0]
        programmes = sorted({c['programme'] for c in copies}, key=str.lower)
        departments = sorted({department(p) for p in programmes})
        dept_papers.update(departments)
        if first['academic_year']:
            years.add(first['academic_year'])
        paper = {'paper_id': sha[:12], 'subject': subject, 'kind': first['kind'], 'academic_year': first['academic_year'],
                 'exam': first['exam'], 'semester': first['semester'], 'departments': departments,
                 'programme_types': sorted({programme_type(p) for p in programmes}), 'programmes': programmes,
                 'source_path': first['path'], 'identical_copies': len(copies) - 1}
        heading = ' · '.join(b for b in (first['academic_year'] or 'Year not stated', first['exam'] or 'Exam not stated',
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
            stats[f'pages_{method}'] += len(pages)
            doc = dict(paper, paper_id=sha[:12] + (f'-{number_in_file + 1}' if label else ''),
                       pages=len(pages), extraction=method, ocr_confidence=confidence,
                       **{k: header[k] for k in ('max_marks', 'duration_hours', 'exam_date') if k in header})
            if label:
                doc['source_path'] = f"{first['path']} :: {label}"
            if not doc['exam'] and header.get('exam_title'):
                doc['exam'] = header['exam_title']
            if not doc['academic_year'] and header.get('academic_year'):
                doc['academic_year'] = header['academic_year']
            printed = [f'{k.replace("_", " ")}: {header[k]}' for k in ('max_marks', 'duration_hours', 'exam_date')
                       if k in header]
            lines = [f'## {heading}' + (f' · {label}' if label else ''), ''] + meta
            if printed:
                lines.append('- Printed on paper: ' + '; '.join(printed))
            lines.append(f'- Text: {method} ({len(pages)} page{"s" if len(pages) != 1 else ""})'
                         + (f', mean OCR confidence {confidence}' if confidence is not None else ''))
            ticks = fence(text)
            target.append('\n'.join(lines + ['', ticks + 'text', text, ticks, '']))
            if first['kind'] == 'Question paper':
                parsed = [q for q in parse_questions(text) if q['text']]
                stats['question_papers_read'] += 1
                stats['question_papers_split'] += len({q['question'] for q in parsed}) >= 3
                doc['questions_extracted'] = len(parsed)
                for q in parsed:
                    if q.get('question_stem'):
                        q['question_stem'] = q['question_stem'][:300]
                    entry = dict(q, subject=subject, academic_year=doc['academic_year'], exam=doc['exam'],
                                 semester=doc['semester'], departments=departments, paper_id=doc['paper_id'],
                                 extraction=method)
                    question_lines.append(json.dumps({k: entry[k] for k in QUESTION_FIELDS
                                                      if entry.get(k) not in (None, '', [])}, ensure_ascii=False))
                    stats['questions'] += 1
                    stats['questions_with_marks'] += q.get('marks') is not None or q.get('question_marks') is not None
                dept_questions.update({d: len(parsed) for d in departments})
            paper_lines.append(json.dumps({k: doc[k] for k in PAPER_FIELDS if doc.get(k) not in (None, '', [])},
                                          ensure_ascii=False))
    span = (f'{min(years, key=year_key)} to {max(years, key=year_key)}' if years else 'years not stated')
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
            'first_year': min(years, key=year_key) if years else '',
            'last_year': max(years, key=year_key) if years else ''}


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
        f'- {stats["question_papers_read"]:,} question papers read: {stats["pages_text"] + stats["pages_docx"]:,} pages '
        f'from the PDF text layer, {stats["pages_ocr"] + stats["pages_mixed"]:,} pages by OCR (scanned papers).',
        f'- {stats["questions"]:,} questions and sub-questions extracted; {stats["questions_with_marks"]:,} with marks. '
        f'{split:,} papers ({100 * split / read:.0f}%) split into 3 or more questions; the rest are kept as full text '
        'in papers.md.',
        f'- Files with no readable text (corrupt PDFs, spreadsheet data sets): {stats["papers_without_text"]:,}.'
        + (f' Not yet extracted: {stats["papers_not_extracted"]:,}.' if stats['papers_not_extracted'] else ''), '',
        '## questions.jsonl fields', '',
        '| Field | Meaning |', '| --- | --- |',
        '| `subject` | Canonical subject name (same as the folder) |',
        '| `academic_year`, `exam`, `semester` | e.g. `2024-25`, `Final-Exam` / `Re-Exam`, `Sem 5` |',
        '| `departments` | Branches the paper was set for |',
        '| `paper_id` | First 12 hex digits of the paper file\'s SHA-256; matches `papers.jsonl` for programmes, max '
        'marks, date and source file |',
        '| `question`, `part` | Question number and part, e.g. `2` and `b`, `1.a`, `a(ii)` |',
        '| `question_stem` | Shared instruction of the question, e.g. "Attempt any four" |',
        '| `text` | The question text |',
        '| `marks`, `question_marks` | Marks for this part, and for the whole question when printed |',
        '| `co`, `bl` | Course outcome and Bloom\'s level tags printed on newer papers |',
        '| `extraction` | `text` (exact, from the PDF) or `ocr` (scanned paper read by Tesseract) |', '',
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
    p = sub.add_parser('build', help='write papers.md / questions.jsonl per subject and the department indexes')
    p.add_argument('--texts', help='texts.jsonl from extract (also refreshes the committed text cache); '
                                   'default: question_bank/extracted_text.jsonl.gz')
    p.set_defaults(run=cmd_build)
    args = parser.parse_args()
    args.run(args)


if __name__ == '__main__':
    main()
