"""Every syllabus and teaching scheme in the archive as text, split into courses and filed under subjects.

Sources: 04_Syllabi_Archive/, 01_Current_Electives_2026-27/, and syllabi kept only inside the portal's original
ZIP downloads (SYLLABUS/... members listed in question_bank/raw_zip_members.json).

  extract  Read the text of every syllabus file (PDF text layer, OCR for scans); the same reader as the question
           bank, so it needs PyMuPDF and Tesseract (see build_question_bank.py).
  build    Merge new texts.jsonl files into the committed cache (syllabi/extracted_text/) and write:
             syllabi/README.md                    programmes, then every course with the subject it belongs to
             syllabi/<Programme>/README.md        documents by branch, batch and semester
             syllabi/<Programme>/<Branch>.md      full text of that branch's syllabi and teaching schemes
             syllabi/documents.jsonl              one record per document (paths, programme, batch, semester ...)
             syllabi/courses.jsonl                one record per course section, with its text and subject
             subjects/<Subject>/syllabus.md       every syllabus version of a subject that has past papers
             syllabi/courses/<Course>.md          the same for courses with no past papers in the archive
           and refreshes subjects/<Subject>/README.md so it links syllabus.md.

  python build_syllabi.py extract --work D:/syl_work --manifest full-library-manifest.json
  python build_syllabi.py build --manifest full-library-manifest.json --texts D:/syl_work/texts.jsonl
  python build_syllabi.py build --manifest full-library-manifest.json    # from the committed cache
"""
from pathlib import Path, PurePosixPath
from collections import Counter, defaultdict
from urllib.parse import quote
import argparse, csv, json, re, shutil, sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_question_bank as qb                                    # noqa: E402
import organize_by_subject as org                                   # noqa: E402

PREFIXES = ('04_Syllabi_Archive/', '01_Current_Electives_2026-27/')
OUT = HERE / 'syllabi'
TEXT_CACHE = OUT / 'extracted_text'
COURSES_DIR = OUT / 'courses'
SUBJECTS = HERE / 'subjects'

# "Course : Limit State Design of Reinforced Concrete   Code : BTICI09001", "Course/Module: X Module Code: Y",
# "Subject: Electronic Materials and   Code: BTICO03002", "Name of the Course: X"
COURSE_LINE = re.compile(
    r'(?i)^\W{0,3}(?:name of (?:the )?)?(?:course\s*/\s*module|course|subject|module)(?:\s*(?:name|title))?'
    r'\s*[:\-–]\s*(?P<name>[A-Za-z(].*?)\s*'
    r'(?:(?:(?:module|course|subject)\s*)?code\s*[:\-–.]?\s*(?P<code>[A-Z0-9][A-Z0-9/\-]{2,19}[A-Z0-9])?\s*)?$')
SEMESTER_LINE = re.compile(r'(?i)\b(sem(?:ester)?|trim(?:ester)?)\s*[:\-–.]?\s*([IVX]{1,4}|\d{1,2})\b')
PROGRAM_LINE = re.compile(r'(?i)^\W{0,3}program(?:me)?\s*(?:name)?\s*[:\-–]\s*(.+?)(?:\s{3,}|\s+sem(?:ester)?\b|$)')
CONTINUATION = re.compile(r'^[A-Z][A-Za-z&,\-() ]{2,45}$')
NOT_A_NAME = re.compile(r'(?i)^(teaching|evaluation|lecture|outcomes?|objectives?|pre-?req|credits?|hours|unit\b|'
                        r'detailed|practical|tutorial|theory|course|program|semester|module|total|internal|term|'
                        r'examination|scheme|code|svkm|mukesh|narsee|school|marks?)')
CONNECTOR_END = re.compile(r'(?i)(\band|\bof|\bfor|\bin|\bto|\bwith|&|-|,)$')
BATCH = re.compile(r'(?i)batch\s*\(?\s*((?:19|20)\d\d)\s*(?:-|to)\s*((?:19|20)\d\d)')
SCHEME = re.compile(r'(?i)tea\w*\s*sche\w*|course structure')
LOW_QUALITY = 60                                                       # mean OCR confidence
EXAM_KINDS = ('Exam paper', 'Answer key', 'Exam data set')
ELECTIVE_TAG = re.compile(r'(?i)\s*[(\[][^()\[\]]*\b(?:elective|basket)\b[^()\[\]]*[)\]]')
ELECTIVE_PREFIX = re.compile(
    r'(?i)^\(?\s*(?:(?:open|department(?:al)?|dept\.?|professional|programme|program|institute|interdisciplinary|core)\s*)?'
    r'elective\b(?:\s*course)?\s*[-–:]?\s*(?:[IVXL]{1,4}\b|\d{1,2}\b)?\s*\)?\s*[-–:]?\s*')
TRAILING_JUNK = re.compile(       # OCR specks after a title: "Fluid Mechanics ha", "Radar SS", "Design . OM", "#"
    r'(?:\s+(?:[^\w\s()]+|[a-z]{1,2}|[A-Z][a-z]|(?!AI|ML|IT|OS|UI|UX|II|IV|VI|IX|XI|VR|AR|PM|HR|GD)[A-Z]{2}|'
    r'[ABD-HJ-QS-UWYZ]))+$')
EMBEDDED_CODE = re.compile(r'(?i)\s+(?:(?:module|course|subject)\s*)?(?:code)?\s*[:\-–]\s*[A-Z0-9]*\d[A-Z0-9]*$')
CODE_MARKER = re.compile(        # everything from a "Code:" (OCR: "Codg", "“|Code") or "Time:" marker on is not the name
    r'(?i)[\s|“”"+_~(\-–:;]*\b(?:(?:module|course|subject)\s*)?cod[eg]\b|\s+time\s*:')
CODE_TOKENS = re.compile(r"(?:[\s,;|_]+(?=[A-Za-z0-9'’{}|°]{6,})[A-Za-z'’]*\d[A-Za-z0-9'’{}|°]*)+[\s_~|]*$")  # "BTC101002, BTMA01002"
CATEGORY_TAG = re.compile(r'(?i)^\(\s*(?:BSC|ESC|HSC|HSMC|PCC|PEC|OEC|BS|ES|HS|MC)\s*\)\s*[-–:]?\s*')
ELECTIVE_LABEL = re.compile(r'(?i)^\(?\s*(?:(?:professional|open|department(?:al)?|core|programme|program)\s*)?'
                            r'elective(?:\s*course)?\s*[-–:]?\s*(?:[IVX]{1,4}|\d{1,2})?\s*\)?$')
GENERIC = re.compile(r'(?i)^(?:module|course|subject|code|name|title|elective|open elective|syllabus)s?$')
OCR_NUMERAL = [(re.compile(r'(?<=[a-z])[\s\-–]+(?:lll|Ill|111|IlI)(?:\s+\d)?$'), ' III'),
               (re.compile(r'(?<=[a-z])[\s\-–]+(?:ll|Il|lI|11)(?:\s+\d)?$'), ' II'),
               (re.compile(r'(?<=[a-z])[\s\-–]+(?:l|1)$'), ' I')]


# ============================================================================ documents and their facts


def location_facts(location):
    """Programme, branch, batch, semester and kind from a syllabus path relative to the syllabus root."""
    parts = [re.sub(r'(?i)^trm\b', 'TRIM', p.strip()) for p in location.split('/') if p.strip()]   # "TRM VI"
    name = parts[-1]
    folders = parts[:-1]
    programme = re.sub(r'\s+', ' ', folders[0]) if folders else 'Current electives 2026-27'
    branch = ''
    rest = folders[1:]
    if rest and re.fullmatch(r'(?i)\d\w*\s*year', rest[0]):          # B TECH/2ND YEAR/<branch>/..., PGDM/1st Year
        year_of_study = rest[0].upper()
        rest = rest[1:]
    else:
        year_of_study = ''
    if rest and not BATCH.search(rest[0]) and not SCHEME.search(rest[0]) and not org.semester_label([rest[0]]):
        branch = org.HASH_SUFFIX.sub('', rest[0]).strip()
    filed = branch
    branch = branch_name(branch)
    batch = next((f'{m.group(1)}-{m.group(2)}' for m in map(BATCH.search, folders) if m), '')
    semester = org.semester_label(folders[::-1][:2]) or semester_from_name(name)
    kind = ('Exam paper' if org.EXAM_FILE.search(name) else             # the portal filed some papers here
            'Teaching scheme' if any(SCHEME.search(p) for p in folders + [name]) else 'Syllabus')
    return {'programme': programme, 'branch': branch, 'branch_as_filed': filed, 'year_of_study': year_of_study, 'batch': batch,
            'semester': semester, 'academic_year': org.academic_year(name), 'kind': kind}


def branch_name(raw):
    """Department name used in departments/ ('ELETRICAL' -> 'Electrical', 'CSE Data Science (311)' -> 'Data Science');
    folders naming no branch are 'All branches'."""
    if not raw or re.search(r'(?i)\ball\b|common|stream|management subject|bsh', raw):
        return 'All branches'
    dept = qb.department(raw.replace('ELETRICAL', 'ELECTRICAL').replace('ARTIFICAL', 'ARTIFICIAL')
                         .replace('MECHATORNICS', 'MECHATRONICS').replace('MECHATRONICES', 'MECHATRONICS'))
    if dept != qb.COMMON:
        return dept
    raw = raw.replace('_', ' ').strip()
    return raw if raw.isupper() and len(raw) <= 5 else org.display_case(raw)


def time_label(course_or_doc):
    if course_or_doc['batch']:
        return f"batch {course_or_doc['batch']}"
    return f"AY {course_or_doc['academic_year']}" if course_or_doc['academic_year'] else 'year not stated'


def semester_from_name(name):
    text = re.sub(r'\.[A-Za-z0-9]{1,5}$', '', name).replace('_', ' ')
    match = re.search(r'(?i)\b(sem(?:ester)?|trim(?:ester)?)\s*[-.]*\s*([IVX]{1,4}|\d{1,2})\b', text)
    if not match:
        return ''
    value = match.group(2).lower()
    number = int(value) if value.isdigit() else org.ROMAN_VALUE.get(value)
    label = 'Trim' if match.group(1).lower().startswith('trim') else 'Sem'
    return f'{label} {number}' if number else ''


def syllabus_documents(manifest_files):
    """sha -> {'locations': [...], facts of the first location} for every syllabus file, including those kept
    only inside raw ZIP downloads."""
    docs = {}

    def add(sha, size, location, relative):
        doc = docs.setdefault(sha, {'sha256': sha, 'bytes': size, 'locations': [], **location_facts(relative)})
        doc['locations'].append(location)

    for row in sorted(manifest_files, key=lambda r: r['path']):
        if row['path'].startswith(PREFIXES):
            relative = row['path'].split('/', 1)[1]
            if row['path'].startswith('01_'):
                relative = 'Current electives 2026-27/' + relative
            add(row['sha256'], row['bytes'], row['path'], relative)
    if org.RAW_MEMBERS_FILE.exists() and org.RAW_PAPERS_FILE.exists():
        members = {(m['zip_path'], m['member']): m for m in json.loads(org.RAW_MEMBERS_FILE.read_text(encoding='utf-8'))}
        with org.RAW_PAPERS_FILE.open(encoding='utf-8') as stream:
            for line in stream:
                paper = json.loads(line)
                entry = members.get((paper['zip_path'], paper['member']), {})
                virtual = entry.get('virtual_path', '')
                if paper.get('missing') or not virtual.startswith('SYLLABUS/'):
                    continue
                add(paper['sha256'], paper['bytes'], paper['zip_path'] + org.IN_ZIP + paper['member'],
                    virtual.split('/', 1)[1])
    for doc in docs.values():
        doc['locations'].sort()
    return docs

# ============================================================================ courses inside a document


def clean_course_name(name):
    """The course itself, without codes, elective labels and category tags, and with OCR-misread numerals fixed:
    'Department Elective I - Product Design' -> 'Product Design', 'Engineering Drawing-l' -> 'Engineering Drawing I',
    'Cloud Computing Code: 702IT0C026 702IT0C026' -> 'Cloud Computing', '(BSC) - Polymers in Engineering' ->
    'Polymers in Engineering', 'IV (Pavement Design and Construction)' -> 'Pavement Design and Construction'."""
    text = CODE_MARKER.split(name)[0]
    text = CODE_TOKENS.sub('', EMBEDDED_CODE.sub('', text)).strip()
    text = CATEGORY_TAG.sub('', text).strip()
    text = re.sub(r'[{}]', '', text)
    wrapped = re.fullmatch(r'(?:[IVX1l]{1,4}\s*)?\(([^()]{3,})\)[\W_]*', text)       # "1V (Name)", "(Name) _"
    if wrapped:
        text = wrapped.group(1).strip()
    text = ELECTIVE_TAG.sub('', text).strip()
    text = re.sub(r'(?i)\s*\(\s*elective[^()]*$|\s+elective\s*[-–]?\s*(?:[IVX]{1,4}|\d)?$', '', text).strip()
    text = ELECTIVE_PREFIX.sub('', text).strip() or text
    if text.startswith('(') and (text.endswith(')') or ')' not in text):
        text = text.strip('()').strip()
    for _ in range(2):
        text = TRAILING_JUNK.sub('', text).strip(' .:;-–|,&«»')
    for pattern, numeral in OCR_NUMERAL:
        text = pattern.sub(numeral, text)
    text = re.sub(r'\s+', ' ', text).strip(' .:;-–|,&_~')
    return text if len(re.findall(r'[A-Za-z]', text)) >= 3 else name


def is_course_name(name):
    """Not a label ("Elective", "(Professional Elective Course-3)"), a sentence picked up from the course text, or
    OCR noise ("A Advanced d v a n d Pm-nno+- Computer ...")."""
    words = name.split()
    return (len(re.findall(r'[A-Za-z]', name)) >= 3 and not GENERIC.match(name.strip())
            and not ELECTIVE_LABEL.match(name.strip()) and len(words) <= 10
            and sum(len(w) == 1 and w.isalpha() and w not in 'AI&' for w in words) <= max(1, len(words) // 5))


def course_name(match, lines, index):
    name = re.sub(r'\s+', ' ', match.group('name')).strip(' .:;-–|')
    name = re.split(r'\s{2,}|\s+(?:semester|sem|program(?:me)?|credits?|year)\s*[:\-–]', name, flags=re.I)[0]
    coded = CODE_MARKER.split(name)
    name = coded[0].strip(' .:;-–|')                                    # "X and Code: COA" (two codes defeat COURSE_LINE)
    following = next((l.strip() for l in lines[index + 1:index + 3] if l.strip()), '')
    if (following and (match.group('code') or len(coded) > 1 or CONNECTOR_END.search(name)) and CONTINUATION.match(following)
            and len(following.split()) <= 5 and not NOT_A_NAME.match(following)):
        name = f'{name} {following}'                                    # title wrapped under the code column
    return name.strip(' .:;-–|,&')


def split_courses(pages):
    """[(name, code, semester, first_page, last_page, text)] for each course header found in the pages."""
    lines = []                                                          # (page, line)
    for page in pages:
        lines += [(page['page'], line) for line in page['text'].split('\n')]
    texts = [line for _, line in lines]
    starts = []
    for index, (_, line) in enumerate(lines):
        match = COURSE_LINE.match(line.strip())
        if match and len(match.group('name')) <= 150:
            name = course_name(match, texts, index)
            if len(re.findall(r'[A-Za-z]{2,}', name)) >= 1 and len(name) >= 3:
                starts.append((index, name, match.group('code') or ''))
    courses = []
    for number, (index, name, code) in enumerate(starts):
        end = starts[number + 1][0] if number + 1 < len(starts) else len(lines)
        begin = index
        for back in range(index - 1, max(-1, index - 4), -1):            # "Program: ... Semester: IX" just above
            if PROGRAM_LINE.match(texts[back].strip()) or SEMESTER_LINE.search(texts[back]):
                begin = back
        if number and begin < starts[number - 1][0] + 1:
            begin = index
        nearby = ' '.join(texts[max(0, index - 3):index + 2])
        sem = SEMESTER_LINE.search(nearby)
        semester = ''
        if sem:
            value = sem.group(2).lower()
            value = int(value) if value.isdigit() else org.ROMAN_VALUE.get(value)
            semester = f"{'Trim' if sem.group(1).lower().startswith('trim') else 'Sem'} {value}" if value else ''
        chunk = lines[begin:end]
        courses.append((name, code, semester, chunk[0][0], chunk[-1][0], '\n'.join(l for _, l in chunk).strip()))
    return courses

# ============================================================================ matching courses to subjects


class SubjectMatcher:
    """Find the PYQ subject a course name belongs to: exact spelling (any spelling a paper was filed under, or an
    alias), else a subject that organize_by_subject would merge with it."""

    def __init__(self, rows, aliases):
        votes = defaultdict(Counter)
        for row in rows:
            for spelling in (row['subject'], org.HASH_SUFFIX.sub('', row['filed_as'])):
                votes[org.loose_key(spelling)][row['subject']] += 1
        self.exact = {key: max(c.items(), key=lambda kv: (kv[1], kv[0]))[0] for key, c in votes.items() if key}
        self.aliases = aliases
        self.by_length = defaultdict(list)
        for key in sorted(self.exact):
            self.by_length[len(key)].append(key)
        self.cache = {}

    def __call__(self, name):
        key = org.loose_key(name)
        if key not in self.cache:
            self.cache[key] = self.find(key)
        return self.cache[key]

    def find(self, key):
        if not key or org.is_weak(key):
            return None
        if key in self.aliases:
            target = org.loose_key(self.aliases[key])
            return self.exact.get(target) or self.aliases[key]
        if key in self.exact:
            return self.exact[key]
        for size in sorted(range(len(key) - 6, len(key) + 7), key=lambda s: (abs(s - len(key)), s)):
            for other in self.by_length[size]:
                if org.same_subject(key, other):
                    return self.exact[other]
        return None


def course_groups(names, matcher):
    """Display name for each course spelling that matches no subject; spellings org would merge share a name."""
    seeds, group = [], {}
    counts = Counter(names)
    for name, _ in sorted(counts.items(), key=lambda kv: (-kv[1], org.caseless(kv[0]))):
        key = org.loose_key(name)
        seed = next((s for s in seeds if s[0] == key or org.same_subject(key, s[0])), None)
        if not seed:
            seed = (key, org.display_case(name))
            seeds.append(seed)
        group[name] = seed[1]
    return group

# ============================================================================ writing


def doc_summary(record):
    pages = list(qb.documents(record)) if record else []
    flat = [p for _, ps in pages for p in ps]
    method, confidence = qb.extraction_summary(flat) if flat else ('none', None)
    quality = 'low' if confidence is not None and confidence < LOW_QUALITY else 'ok' if flat else 'unreadable'
    return flat, method, confidence, quality


def sort_key(doc):
    sem = doc['semester']
    number = int(sem.split()[-1]) if sem and sem.split()[-1].isdigit() else 99
    return (doc['programme'].lower(), doc['branch'].lower(), -int((doc['batch'] or doc['academic_year'] or '0')[:4]),
            doc['kind'], number, doc['locations'][0])


def write_outputs(docs, texts, rows, aliases):
    matcher = SubjectMatcher(rows, aliases)
    folders = org.subject_folders({r['subject'] for r in rows})
    paper_subject = {r['sha256']: r['subject'] for r in sorted(rows, key=lambda r: r['path'])[::-1]}
    filed_as = {'Question paper': 'Exam paper', 'ZIP of papers': 'Exam paper', 'Answer key': 'Answer key',
                'Dataset': 'Exam data set'}
    for r in rows:                      # the same file filed as a paper elsewhere: whatever its name, it is one
        if r['kind'] in filed_as and r['sha256'] in docs:
            docs[r['sha256']]['kind'] = filed_as[r['kind']]
    if OUT.exists():
        for child in OUT.iterdir():
            if child != TEXT_CACHE:
                shutil.rmtree(child) if child.is_dir() else child.unlink()
    OUT.mkdir(exist_ok=True)
    for folder in SUBJECTS.iterdir() if SUBJECTS.exists() else []:
        if (folder / 'syllabus.md').exists():
            (folder / 'syllabus.md').unlink()

    doc_lines, course_records, by_programme = [], [], defaultdict(list)
    stats = Counter()
    for doc in sorted(docs.values(), key=sort_key):
        record = texts.get(doc['sha256'])
        pages, method, confidence, quality = doc_summary(record)
        doc.update(pages=len(pages), method=method, ocr_confidence=confidence, text_quality=quality)
        doc['damage'] = (record or {}).get('damage')
        doc['pages_turned_upright'] = sum(1 for p in pages if p.get('rotated')) or None
        doc['courses'] = []
        if doc['kind'] == 'Syllabus' and pages:
            for printed, code, semester, first, last, text in split_courses(pages):
                name = clean_course_name(printed)
                if not is_course_name(name):
                    continue
                course_records.append({
                    'course': name, 'printed_as': printed, 'code': code, 'subject': matcher(name), 'programme': doc['programme'],
                    'branch': doc['branch'], 'batch': doc['batch'], 'academic_year': doc['academic_year'],
                    'semester': semester or doc['semester'], 'pages': f'{first}-{last}' if first != last else str(first),
                    'source_path': doc['locations'][0], 'sha256': doc['sha256'], 'text_quality': quality, 'text': text})
                doc['courses'].append(name)
        stats['documents'] += 1
        stats[f"kind:{doc['kind']}"] += 1
        stats[f'quality:{quality}'] += 1
        stats['pages'] += len(pages)
        by_programme[doc['programme']].append((doc, pages))
        doc_lines.append({k: doc[k] for k in ('sha256', 'locations', 'programme', 'branch', 'branch_as_filed',
                                               'year_of_study', 'batch',
                                               'semester', 'academic_year', 'kind', 'pages', 'method',
                                               'ocr_confidence', 'text_quality', 'pages_turned_upright', 'damage',
                                               'courses', 'bytes')
                          if doc[k] is not None or k not in ('pages_turned_upright', 'damage')})
    unmatched = course_groups([c['course'] for c in course_records if not c['subject']], matcher)
    for course in course_records:
        course['course_group'] = course['subject'] or unmatched[course['course']]

    with (OUT / 'documents.jsonl').open('w', encoding='utf-8', newline='\n') as out:
        for line in doc_lines:
            out.write(json.dumps(line, ensure_ascii=False) + '\n')

    # Per subject (or unmatched course): every syllabus version, newest batch first. Links are relative to syllabi/.
    groups = defaultdict(list)
    for course in course_records:
        groups[course['course_group']].append(course)
    COURSES_DIR.mkdir()
    course_files, used = {}, set()
    for group in sorted(groups, key=org.caseless):
        versions = sorted(groups[group], key=lambda c: (-int((c['batch'] or c['academic_year'] or '0')[:4]),
                                                        c['programme'].lower(), c['branch'].lower(), c['source_path']))
        has_papers = bool(versions[0]['subject'])
        if has_papers:
            path = SUBJECTS / folders[group] / 'syllabus.md'
            link = f'../subjects/{quote(folders[group])}/syllabus.md'
        else:
            name, n = org.safe_name(org.folder_name(group) + '.md'), 2
            while name.casefold() in used:
                name, n = org.safe_name(f'{org.folder_name(group)} ({n}).md'), n + 1
            used.add(name.casefold())
            path = COURSES_DIR / name
            link = f'courses/{quote(name)}'
        course_files[group] = (link, has_papers, versions)
        seen, body = set(), [f'# {group} — syllabus', '',
                             f'{len(versions)} syllabus section(s) for this course in the archive, newest batch first. '
                             'Text comes from the PDF (OCR for scanned pages; check figures against the source). '
                             'All programmes\' syllabi: [`syllabi/`](' + ('../../syllabi/README.md' if has_papers
                                                                          else '../README.md') + ').', '']
        for course in versions:
            key = (course['sha256'], course['pages'])
            if key in seen:
                continue
            seen.add(key)
            body += [f"## {course['programme']} · {course['branch']} · {time_label(course)} · "
                     f"{course['semester'] or 'semester not stated'}", '',
                     f"- Course as printed: {course['printed_as']}" + (f" (code {course['code']})" if course['code'] else ''),
                     f"- Source: `{course['source_path']}`, page {course['pages']}"
                     + (' — low-quality OCR' if course['text_quality'] == 'low' else ''), '']
            fence = qb.fence(course['text'])
            body += [fence + 'text', course['text'], fence, '']
        path.write_text('\n'.join(body), encoding='utf-8')

    # Programme pages: documents by branch, batch and semester. Branch files hold the full text of documents not
    # split into courses (teaching schemes, unsplit syllabi) and link the course files for the rest.
    programme_folders = {}
    for programme in sorted(by_programme, key=org.caseless):
        folder = org.folder_name(programme)
        programme_folders[programme] = folder
        (OUT / folder).mkdir()
        with (OUT / folder / 'courses.jsonl').open('w', encoding='utf-8', newline='\n') as out:
            for course in course_records:
                if course['programme'] == programme:
                    out.write(json.dumps({k: v for k, v in course.items() if k != 'course_group'},
                                         ensure_ascii=False) + '\n')
        entries = by_programme[programme]
        branches, shown = defaultdict(list), {}
        for doc, pages in entries:                                  # "Civil" and "CIVIL" share one file
            key = org.folder_name(doc['branch']).casefold()
            shown.setdefault(key, doc['branch'])
            branches[shown[key]].append((doc, pages))
        lines = [f'# {programme} syllabi', '',
                 f"{len(entries)} documents ({sum(d['kind'] == 'Teaching scheme' for d, _ in entries)} teaching "
                 f"schemes, {sum(d['kind'] in EXAM_KINDS for d, _ in entries)} exam papers and answer keys filed with "
                 "the syllabi). "
                 '[`courses.jsonl`](courses.jsonl) has every course section found in them, with its text. '
                 'Each branch file lists its documents; syllabus documents link to their courses (filed by subject), '
                 'exam papers link to their subject in the question bank, and teaching schemes and other documents '
                 'are given in full.', '']
        for branch in sorted(branches, key=org.caseless):
            name = org.safe_name(org.folder_name(branch) + '.md')
            lines += [f'## {branch}', '', f'Details and text: [`{name}`]({quote(name)})', '',
                      '| Batch | Year | Semester | Kind | Pages | Text | Courses | File |',
                      '| --- | --- | --- | --- | ---: | --- | --- | --- |']
            body = [f'# {programme} — {branch}', '']
            for doc, pages in branches[branch]:
                file_name = PurePosixPath(doc['locations'][0].split(org.IN_ZIP)[-1]).name
                courses = list(dict.fromkeys(doc['courses']))
                listed = ', '.join(courses)
                lines.append('| ' + ' | '.join(org.md_cell(x) for x in (
                    doc['batch'] or '—', doc['academic_year'] or '—', doc['semester'] or '—', doc['kind'],
                    doc['pages'], f"{doc['method']}{' (low quality)' if doc['text_quality'] == 'low' else ''}",
                    (listed[:300] + ' …') if len(listed) > 300 else listed or '—', file_name)) + ' |')
                body += [f'## {file_name}', '',
                         f"- {doc['kind']} · {time_label(doc)} · {doc['semester'] or 'semester not stated'}"
                         f" · {doc['pages']} pages · text from {doc['method']}"
                         + (f", mean OCR confidence {doc['ocr_confidence']}" if doc['ocr_confidence'] is not None else ''),
                         f"- Source: `{doc['locations'][0]}`" + (f" (+{len(doc['locations']) - 1} identical copies)"
                                                                 if len(doc['locations']) > 1 else '')]
                body += [f"- Damaged file: {doc['damage']}"] if doc['damage'] else []
                body += [f"- {doc['pages_turned_upright']} page{'s' if doc['pages_turned_upright'] != 1 else ''} "
                         f"scanned sideways or upside down, turned upright before OCR"] if doc['pages_turned_upright'] else []
                body += ['']
                if doc['kind'] in EXAM_KINDS and doc['sha256'] in paper_subject:
                    subject = paper_subject[doc['sha256']]
                    body += [f"{'An answer key' if doc['kind'] == 'Answer key' else 'An exam paper'} the portal filed "
                             f"with the syllabi. Its text{'' if doc['kind'] == 'Answer key' else ' and questions'} are in the "
                             f"question bank: [{org.md_cell(subject)}](../../subjects/{quote(folders[subject])}/README.md).",
                             '']
                elif courses:
                    groups_here = list(dict.fromkeys(c['course_group'] for c in course_records
                                                     if c['sha256'] == doc['sha256']))
                    body += ['Courses (full text in each course file):', '']
                    body += [f"- [{org.md_cell(g)}](../{course_files[g][0]})" for g in groups_here] + ['']
                else:
                    text = qb.page_text(pages) if pages else '(no text could be read from this file)'
                    fence = qb.fence(text)
                    body += [fence + 'text', text, fence, '']
            lines.append('')
            (OUT / folder / name).write_text('\n'.join(body), encoding='utf-8')
        (OUT / folder / 'README.md').write_text('\n'.join(lines), encoding='utf-8')

    # Master README.
    matched = sum(1 for c in course_records if c['subject'])
    lines = [
        '# Syllabi and teaching schemes', '',
        f"All **{stats['documents']:,}** documents in the archive's syllabus sections ({stats['kind:Syllabus']:,} "
        f"syllabi, {stats['kind:Teaching scheme']:,} teaching schemes, and {sum(stats['kind:' + k] for k in EXAM_KINDS):,} "
        f"exam papers and answer keys "
        f"the portal filed there; {stats['pages']:,} pages) read into text, from `04_Syllabi_Archive/`, "
        '`01_Current_Electives_2026-27/` and syllabi kept only inside the portal\'s ZIP downloads. Syllabus documents '
        f"were split into **{len(course_records):,} course sections**; {matched:,} belong to a subject that has past "
        'papers and are also in that subject\'s folder as `syllabus.md`, next to its question papers.', '',
        '- `<Programme>/courses.jsonl`: one record per course section (course, code, subject, programme, branch, '
        'batch, semester, source, text).',
        '- [`documents.jsonl`](documents.jsonl): one record per document, with every path it is stored under.',
        f"- Text quality: {stats['quality:ok']:,} documents read cleanly, {stats['quality:low']:,} are poor scans "
        f"(mean OCR confidence below {LOW_QUALITY}), {stats['quality:unreadable']:,} gave no text.",
        '- Teaching schemes are mostly scanned tables; their OCR text is kept in full in the branch files '
        '(`<Programme>/<Branch>.md`) but is not split into courses.',
        '- Exam papers and answer keys found among the syllabi (file names such as `..._Final_Exam_...`, or the same '
        'file filed as a paper elsewhere) are not split into courses: each is in the question bank under its subject '
        '(`subjects/`), and its branch-file entry links there.', '',
        '## Programmes', '', '| Programme | Documents | Branches |', '| --- | ---: | --- |']
    for programme in sorted(by_programme, key=org.caseless):
        entries = by_programme[programme]
        branches = sorted({d['branch'] for d, _ in entries}, key=org.caseless)
        lines.append(f"| [{org.md_cell(programme)}]({quote(programme_folders[programme])}/README.md) | {len(entries)} | "
                     f"{org.md_cell(', '.join(branches))} |")
    lines += ['', '## Courses', '',
              'Every course found in the syllabi. Courses with past papers link to the subject folder\'s `syllabus.md`.', '',
              '| Course | Past papers | Versions | Programmes | Batches / years |', '| --- | --- | ---: | --- | --- |']
    for group in sorted(course_files, key=org.caseless):
        link, has_papers, versions = course_files[group]
        batches = sorted({c['batch'] or (f"AY {c['academic_year']}" if c['academic_year'] else '') for c in versions} - {''},
                         key=lambda b: (b.removeprefix('AY ')[:4], b))
        span = (batches[0] if len(batches) == 1 else f'{batches[0]} to {batches[-1]}') if batches else '—'
        papers = f"[yes](../subjects/{quote(folders[group])}/README.md)" if has_papers else '—'
        lines.append(f"| [{org.md_cell(group)}]({link}) | {papers} | {len(versions)} | "
                     f"{org.md_cell(', '.join(sorted({c['programme'] for c in versions}, key=org.caseless)))} | {span} |")
    lines.append('')
    (OUT / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f"{stats['documents']} documents ({stats['pages']} pages); {len(course_records)} course sections, "
          f"{matched} matched to a PYQ subject; {sum(1 for g in course_files.values() if g[1])} subjects got syllabus.md, "
          f"{sum(1 for g in course_files.values() if not g[1])} courses without past papers.")
    return stats

# ============================================================================ commands


def cmd_extract(args):
    args.prefix = list(PREFIXES)
    qb.cmd_extract(args)
    print('Syllabi in raw ZIP downloads are read by: python build_question_bank.py extract-raw (same texts.jsonl format).')


def cmd_build(args):
    _, manifest = org.load_manifest(args.manifest)
    docs = syllabus_documents(manifest['files'])
    texts = qb.load_texts(TEXT_CACHE) if TEXT_CACHE.exists() else {}
    for extra in args.texts or []:
        texts.update({sha: record for sha, record in qb.load_texts(extra).items() if sha in docs})
    texts = {sha: record for sha, record in texts.items() if sha in docs}
    if args.texts:
        qb.save_text_cache(texts, TEXT_CACHE)
    with org.INDEX_CSV.open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream))
    missing = [sha for sha in docs if sha not in texts]
    write_outputs(docs, texts, rows, org.load_aliases())
    org.write_catalog(org.load_records())                               # subject READMEs link syllabus.md
    if missing:
        print(f'{len(missing)} syllabus files have no extracted text yet; run extract (first: {docs[missing[0]]["locations"][0]}).')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('extract', help='read the text of every syllabus file (OCR where needed)')
    p.add_argument('--manifest', required=True, help='verified full-library-manifest.json')
    p.add_argument('--work', required=True, help='working folder for texts.jsonl and temporary bundles')
    p.add_argument('--workers', type=int, default=qb.os.cpu_count() or 2)
    p.add_argument('--download', choices=['https', 'gh'], default='gh')
    p.add_argument('--limit', type=int, help='only the first N bundles (for a trial run)')
    p.set_defaults(run=cmd_extract)
    p = sub.add_parser('build', help='write syllabi/ and subjects/<Subject>/syllabus.md')
    p.add_argument('--manifest', help='full-library-manifest.json (downloaded and verified if omitted)')
    p.add_argument('--texts', action='append', help='texts.jsonl from extract or extract-raw (repeatable)')
    p.set_defaults(run=cmd_build)
    args = parser.parse_args()
    args.run(args)


if __name__ == '__main__':
    main()
