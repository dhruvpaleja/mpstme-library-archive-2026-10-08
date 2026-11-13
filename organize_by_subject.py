"""Sort every MPSTME past question paper (PYQ) into one folder per subject.

The backup keeps question papers in the portal's original hierarchy
(year / semester / exam / programme / subject, or for older papers
programme / year / branch / semester / subject), so one subject is spread over
dozens of folders. This tool assigns every question-paper path a canonical
subject (merging spelling variants such as "APPLIED MATHEMATICES II" and
"Applied Mathematics II") and builds a subject-wise folder tree. Papers that
exist only inside the portal's original ZIP downloads (question_bank/
raw_zip_papers.jsonl) are included as "<zip path> :: <file inside it>"; restore
fetches the ZIP and extracts just that file. The tree looks like:

    PYQs_By_Subject/<Subject>/<Academic year>/<paper>

Requires Python 3.11+. Run it from a checkout of this repository.

  python organize_by_subject.py list                          # every subject with counts
  python organize_by_subject.py list --search "data struct"   # find a subject's exact name
  python organize_by_subject.py restore --destination D:/Study --subject "Data Structures and Algorithms"
  python organize_by_subject.py link --library D:/MPSTME_Library_Restored
  python organize_by_subject.py catalog --manifest full-library-manifest.json   # maintainers

restore  downloads only the chosen subjects' papers from the private release
         (via restore_library.py, so GitHub CLI must be signed in) and then
         builds <destination>/PYQs_By_Subject/.
link     builds the subject tree from a library you already restored, using
         hard links (no extra disk space on NTFS) or --copy.
catalog  regenerates subjects/ (one folder per subject with an index of its
         papers) and subjects/pyq_subject_index.csv from the full manifest.

To correct a subject, add "spelling": "Subject it belongs to" to
subject_aliases.json (spellings are listed under "Also filed as" in each
subject's README) and rerun catalog. To move a single paper the portal filed
under the wrong subject, add its original path to subject_overrides.json.
"""
from pathlib import Path, PurePosixPath
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from urllib.parse import quote
import argparse, csv, hashlib, json, os, re, shutil, subprocess, sys, unicodedata, zipfile

HERE = Path(__file__).resolve().parent
INDEX_DIR = HERE / 'subjects'
INDEX_CSV = INDEX_DIR / 'pyq_subject_index.csv'
ALIASES_FILE = HERE / 'subject_aliases.json'
OVERRIDES_FILE = HERE / 'subject_overrides.json'
MANIFEST_NAME = 'full-library-manifest.json'
REPO = 'dhruvpaleja/mpstme-library-archive-2026-10-08'
TAG = 'complete-library-2026-10-08'
QP_ROOT = '02_Question_Papers/'
RAW_MEMBERS_FILE = HERE / 'question_bank' / 'raw_zip_members.json'   # papers kept only inside raw ZIP downloads
RAW_PAPERS_FILE = HERE / 'question_bank' / 'raw_zip_papers.jsonl'    # their SHA-256 and size, read from the ZIPs
IN_ZIP = ' :: '                                     # "<zip path> :: <member>" names a file inside a ZIP
TREE_NAME = 'PYQs_By_Subject'
KIND_ORDER = {'Question paper': 0, 'Answer key': 1, 'Dataset': 2, 'ZIP of papers': 3, 'Syllabus': 4}   # listing order
SYLLABUS_ROOT = '04_Syllabi_Archive/'
EXAM_FILE = re.compile(          # exam papers by file name: '_Final_Exam_', 'Re_Rexam', 'Fianl_Exam', '_Final_2021-22',
    r'(?i)(?:final|fianl|re|end[\s_\-]*sem(?:ester)?)[\s_\-]*r?exam|^(?:QP|ANS)_|question[\s_\-]*paper'   # 'Sem8_Final',
    r'|(?:^|[_\s\-])(?:final|fianl)(?:[_\s\-]*(?:\d{2}(?:\d{2})?(?:-\d{2,4})?)|[_\s\-]*$)')        # 'Final0001'
CSV_FIELDS = ['subject', 'academic_year', 'exam', 'kind', 'semester', 'programme', 'source', 'bytes', 'sha256',
              'path', 'filed_as', 'note']

# ============================================================================ text normalisation

# Misspellings seen in the portal's folder and file names (penalised when choosing a display name).
TYPOS = {
    'engineeing': 'engineering', 'enginnering': 'engineering', 'enginerring': 'engineering', 'engg': 'engineering',
    'artifical': 'artificial', 'mehtods': 'methods', 'methodes': 'methods', 'statitics': 'statistics',
    'stastistics': 'statistics', 'technnology': 'technology', 'develipment': 'development',
    'intoduction': 'introduction', 'inttroduction': 'introduction', 'introdution': 'introduction',
    'mgmt': 'management', 'mngt': 'management', 'managment': 'management', 'managemrnt': 'management',
    'managemet': 'management', 'mangement': 'management', 'mathematices': 'mathematics', 'mathemetics': 'mathematics',
    'mthematics': 'mathematics', 'streanth': 'strength', 'strengh': 'strength', 'scineces': 'sciences',
    'resaerch': 'research', 'reseach': 'research', 'commmunication': 'communication', 'communcation': 'communication',
    'mechinery': 'machinery', 'machinary': 'machinery', 'emdedded': 'embedded', 'appiled': 'applied',
    'systmes': 'systems', 'systms': 'systems', 'sytem': 'system', 'electromaganetic': 'electromagnetic',
    'filed': 'field', 'desing': 'design', 'industrila': 'industrial', 'transportaion': 'transportation',
    'econimics': 'economics', 'intelilgence': 'intelligence', 'oragansation': 'organization',
    'aconting': 'accounting', 'accountig': 'accounting', 'anomly': 'anomaly', 'anlysis': 'analysis',
    'algoithms': 'algorithms', 'interation': 'interaction', 'managrs': 'managers', 'margers': 'managers',
    'fluide': 'fluid', 'marowave': 'microwave', 'progammimg': 'programming', 'programmimg': 'programming',
    'propogation': 'propagation', 'themodynamics': 'thermodynamics', 'chemcial': 'chemical',
    'beheviores': 'behaviour', 'finanacial': 'financial', 'finacial': 'financial', 'sattellite': 'satellite',
    'acquision': 'acquisition', 'acquistion': 'acquisition', 'instrumentaion': 'instrumentation',
    'internationl': 'international', 'transfert': 'transfer', 'microprocesser': 'microprocessor',
    'prestessed': 'prestressed', 'finaces': 'finances', 'qulaity': 'quality', 'soild': 'solid', 'fuild': 'fluid',
    'machanical': 'mechanical', 'sof': 'soft', 'chemestry': 'chemistry', 'techology': 'technology',
    'forcasting': 'forecasting', 'assesment': 'assessment', 'assessement': 'assessment', 'wast': 'waste',
    'supplychain': 'supply chain', 'theoratical': 'theoretical', 'surveyong': 'surveying',
    'integragrated': 'integrated', 'intergrated': 'integrated', 'iinformation': 'information', 'vedio': 'video',
    'kineties': 'kinetics', 'blackchain': 'blockchain', 'cybersecurty': 'cybersecurity', 'electronicc': 'electronic',
    'mobail': 'mobile', 'manufactruring': 'manufacturing', 'facilites': 'facilities', 'claculations': 'calculations',
    'derivaties': 'derivatives', 'introducation': 'introduction', 'introdcution': 'introduction',
    'virtural': 'virtual', 'enigneering': 'engineering', 'microcontoller': 'microcontroller',
    'manufaturing': 'manufacturing', 'architecure': 'architecture', 'recongnization': 'recognition',
    'croundwater': 'groundwater', 'progamming': 'programming', 'buisness': 'business', 'busienss': 'business',
    'tribiology': 'tribology', 'electornics': 'electronics', 'electornic': 'electronic', 'apporvals': 'approvals',
    'desising': 'designing', 'computional': 'computational', 'applictions': 'applications',
    'complier': 'compiler', 'automative': 'automotive', 'adavnces': 'advances', 'adavnce': 'advance',
    'itl': 'etl', 'medeling': 'modeling', 'acquistion': 'acquisition', 'mangagement': 'management',
}
# Legitimate alternative spellings: merged for comparison but not penalised.
VARIANTS = {'modelling': 'modeling', 'organisation': 'organization', 'organisational': 'organizational',
            'practises': 'practices', 'behaviour': 'behavior', 'behavioural': 'behavioral', 'analyse': 'analyze',
            'programme': 'program'}
# Prefixes that turn a word into a different one (organic / inorganic, linear / nonlinear).
MEANINGFUL_PREFIXES = {'in', 'un', 'non', 'im', 'ir', 'il', 'dis', 'bio', 'geo', 're', 'de', 'anti', 'sub', 'super',
                       'inter', 'trans', 'multi', 'micro', 'macro', 'nano', 'co', 'thermo', 'hydro', 'electro'}
NUMERALS = {'1': 'i', '2': 'ii', '3': 'iii', '4': 'iv', '5': 'v', '6': 'vi', '7': 'vii', '8': 'viii',
            'i': 'i', 'ii': 'ii', 'iii': 'iii', 'iv': 'iv', 'v': 'v', 'vi': 'vi', 'vii': 'vii', 'viii': 'viii'}
ROMAN_VALUE = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7, 'viii': 8, 'ix': 9, 'x': 10,
               'xi': 11, 'xii': 12, 'xiii': 13, 'xiv': 14, 'xv': 15, 'xvi': 16}
STOPWORDS = {'and', 'of', 'the', 'to', 'in', 'for', 'with', 'on', 'a', 'an', 'using', 'its'}
# Words that look alike but name different things; never treated as misspellings of each other.
DISTINCT_STEMS = [('macro', 'micro'), ('electrical', 'electronic'), ('analog', 'digital'), ('econom', 'ergonom'),
                  ('hydrology', 'hydraulic'), ('static', 'statistic'), ('thermal', 'thermo')]
HASH_SUFFIX = re.compile(r'_[0-9a-f]{8}$')                 # portal truncated a long name and appended a hash
UPLOAD_TOKEN = re.compile(r'[\s_-]+(?=[A-Za-z0-9]*\d)(?=[A-Za-z0-9]*[A-Za-z])[A-Za-z0-9]{8,12}$')
# Labels that are never a subject on their own (scanner defaults, generic names).
WEAK_NAMES = {'scan', 'scanned', 'paper', 'question paper', 'qp', 'document', 'doc', 'img', 'image', 'new', 'copy',
              'final', 'exam', 'open elective', 'elective', 'merged', 'file', 'page', 'pdf', 'untitled'}


def ascii_fold(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()


def stem(word):
    if len(word) <= 3 or word in NUMERALS:
        return word
    if word.endswith('ies') and len(word) > 4:
        return word[:-3] + 'y'
    if word.endswith(('sses', 'xes', 'ches', 'shes')):
        return word[:-2]
    if word.endswith('s') and not word.endswith(('ss', 'us', 'is')):
        return word[:-1]
    return word


def words(name):
    text = re.sub(r'c\s*\+\s*\+', 'cplusplus', ascii_fold(name).lower()).replace('&', ' and ')
    return re.sub(r'[^a-z0-9#]+', ' ', text).split()


def tokens(name):
    """Normalised words: lower case, known typos fixed, numerals as roman, light plural stemming."""
    out = []
    for word in words(name):
        word = VARIANTS.get(TYPOS.get(word, word), TYPOS.get(word, word))
        for part in word.split():
            out.append(stem(NUMERALS.get(part, part)))
    return out


def loose_key(name):
    """Comparison key without stopwords or bracketed asides ("(OE)", "(IoT)", "( Shirpur Campus )")."""
    name = re.sub(r'\([^()]*\)\s*$', '', name) or name
    return ' '.join(t for t in tokens(name) if t not in STOPWORDS)


def numerals(key):
    return tuple(t for t in key.split() if t in ROMAN_VALUE or t.isdigit())


def distinct_words(a, b):
    """True when two similar-looking words are known to mean different things."""
    short, long = sorted((a, b), key=len)
    if long.endswith(short) and long[:-len(short)] in MEANINGFUL_PREFIXES:   # organic / inorganic
        return True
    return any((a.startswith(x) and b.startswith(y)) or (a.startswith(y) and b.startswith(x)) for x, y in DISTINCT_STEMS)


def misspelling(a, b):
    """True when word a looks like a misspelling of word b."""
    if a[0] != b[0] or abs(len(a) - len(b)) > 2 or distinct_words(a, b):
        return False
    return SequenceMatcher(None, a, b).ratio() >= 0.8


def join_compounds(ta, tb):
    """Glue adjacent words of ta that appear as one word in tb ("block chain" vs "blockchain")."""
    out, i = [], 0
    while i < len(ta):
        if i + 1 < len(ta) and any(ta[i] + ta[i + 1] == w or misspelling(ta[i] + ta[i + 1], w) for w in tb):
            out.append(ta[i] + ta[i + 1])
            i += 2
        else:
            out.append(ta[i])
            i += 1
    return out


def similar_tokens(a, b):
    """Every word that differs between the two keys must look like a misspelling of a word on the other side."""
    ta, tb = a.split(), b.split()
    ta = join_compounds(ta, tb)
    tb = join_compounds(tb, ta)
    sa, sb = set(ta), set(tb)
    for left, right in ((sa - sb, sb), (sb - sa, sa)):
        for word in left:
            if not any(misspelling(word, other) for other in right):
                return False
    return True


def same_subject(a, b):
    """True when two loose keys are spelling variants of one subject."""
    if a == b or a.replace(' ', '') == b.replace(' ', ''):
        return True
    if numerals(a) != numerals(b) or min(len(a), len(b)) < 8:
        return False
    ca, cb = a.replace(' ', ''), b.replace(' ', '')
    matcher = SequenceMatcher(None, ca, cb)
    if matcher.real_quick_ratio() < 0.86 or matcher.quick_ratio() < 0.86 or matcher.ratio() < 0.86:
        return False
    return similar_tokens(a, b)


UPPER_WORDS = {'ai', 'ml', 'it', 'vlsi', 'dbms', 'rdbms', 'os', 'cad', 'cam', 'cae', 'cim', 'cnc', 'erp', 'crm', 'hr',
               'hrm', 'gis', 'b2b', 'b2c', 'ui', 'ux', 'ar', 'vr', 'nlp', 'sql', 'api', 'etl', 'spss', 'r', 'c', 'dsp',
               'plc', 'scada', 'hvac', 'rcc', 'ic', 'ics', 'pcb', 'rf', 'mems', 'fea', 'cfd', 'ev', 'ipr', 'evs', 'tqm',
               'scm', 'ehv', 'hvdc', 'mis', 'oop', 'oops', 'dsa', 'cn', 'coa', 'gpu', 'cpu', 'gan', 'cnn', 'rnn', 'llm',
               'ii', 'iii', 'iv', 'vi', 'vii', 'viii', 'ix', 'xi', 'xii', 'id', 'pg', 'mba', 'pdc', 'sap', 'gst',
               'ifrs', 'fmcg', 'nosql', 'html', 'css', 'xml', 'php', 'tcp', 'ip', 'lan', 'wan', 'gsm', 'cdma', 'lte',
               'mimo', 'ofdm', 'fpga', 'asic', 'cmos', 'mos', 'bjt', 'fet', 'adc', 'dac', 'pid', 'hci', 'ipv6', 'v',
               'hrd', 'lstm', 'tv', 'uml', 'csr', 'qa', 'cse', 'ece', 'eee', 'iiot', 'ott', 'kpi', 'gdp', 'gnss'}
# Ordinary short words that portal names happen to write in capitals ("WEB Analytics", "AD HOC Networks").
COMMON_SHORT = {'web', 'new', 'big', 'art', 'law', 'gas', 'oil', 'app', 'net', 'end', 'ad', 'hoc', 'use', 'bio',
                'all', 'non', 'pro', 'key', 'one', 'two', 'top', 'raw', 'air', 'sea', 'job', 'lab', 'map', 'aid'}
SMALL_WORDS = {'and', 'of', 'the', 'to', 'in', 'for', 'with', 'on', 'a', 'an', 'using', 'or', 'by', 'via', 'at',
               'from', 'into', 'as'}
FIXED_CASE = {'iot': 'IoT', 'devops': 'DevOps', 'mlops': 'MLOps', 'nosql': 'NoSQL', 'c++': 'C++', 'matlab': 'MATLAB',
              'javascript': 'JavaScript', 'facts': 'FACTS', 'ecommerce': 'eCommerce', 'iiot': 'IIoT', 'ios': 'iOS',
              'sdlc': 'SDLC', 'ieee': 'IEEE', 'r&d': 'R&D', 'cseh': 'CSEH'}


def display_case(name):
    """Readable, consistently cased subject name."""
    name = UPLOAD_TOKEN.sub('', HASH_SUFFIX.sub('', name))
    name = re.sub(r'(?i)\bc\s*\+\s*\+', 'C++', name)
    name = re.sub(r'\b[Ee][\s-]+(?=(?:commerce|business|learning|governance)\b)', 'E-', name, flags=re.I)

    def fix_typo(match):                                # known misspellings, keeping the word's casing
        word, fixed = match.group(0), TYPOS[match.group(0).lower()]
        if word.isupper() and len(word) > 1:
            return fixed.upper()
        return fixed.title() if word[0].isupper() else fixed

    name = re.sub(r'[A-Za-z]+', lambda m: fix_typo(m) if m.group(0).lower() in TYPOS else m.group(0), name)
    name = re.sub(r'\s*&\s*', ' and ', name)
    name = re.sub(r'(?i)\s*-\s*((?:i{1,3}|iv|vi{0,3}|ix|l{1,2})|\d)$', lambda m: ' ' + m.group(1).upper().replace('L', 'I'), name)
    name = re.sub(r'\s+([,.;:)])', r'\1', name)
    name = re.sub(r'([,;])(?=\S)', r'\1 ', name)
    name = re.sub(r'\(\s+', '(', name)
    name = re.sub(r'\s+', ' ', name).strip(' .,-_;:')
    letters = [c for c in name if c.isalpha()]
    shouting = bool(letters) and (all(c.isupper() for c in letters) or all(c.islower() for c in letters))
    out = []
    for index, word in enumerate(name.split(' ')):
        bare = word.lower().strip('()-,.:;')
        if re.fullmatch(r'[A-Z]{2}[a-z]{3,}', word):          # "MAnagement": stuck caps key
            word = word.capitalize()
        mixed = any(c.isupper() for c in word[1:]) and any(c.islower() for c in word)
        if bare in FIXED_CASE:
            out.append(word.lower().replace(bare, FIXED_CASE[bare]))
        elif bare in SMALL_WORDS and index and word.isalpha():
            out.append(word.lower())
        elif not shouting and bare not in COMMON_SHORT and (
                mixed or (word.isupper() and (len(bare) <= 3 or any(c.isdigit() for c in bare)))):
            out.append(word)                                    # keep IoT, eCommerce, AI, SQL...
        elif bare in UPPER_WORDS:
            out.append(word.upper())
        elif bare in SMALL_WORDS and index:
            out.append(word.lower())
        else:                                                   # Title-case, including after hyphens
            out.append(re.sub(r'[A-Za-z][A-Za-z\']*', lambda m: m.group(0)[0].upper() + m.group(0)[1:].lower()
                              if m.group(0).lower() not in SMALL_WORDS or m.start() == 0 else m.group(0).lower(),
                              word))
    text = ' '.join(out)
    return text[:1].upper() + text[1:]


def caseless(text):
    """Sort key: case-insensitive, with a deterministic tie-break."""
    return text.lower(), text


def folder_name(subject):
    """Windows-safe, reasonably short folder name."""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '-', subject)
    name = re.sub(r'\s+', ' ', name).strip(' .')
    if len(name) > 80:
        name = name[:80].rstrip(' .-,')
    if name.upper() in {'CON', 'PRN', 'AUX', 'NUL'} or re.fullmatch(r'(?i)(com|lpt)\d', name):
        name += '_'
    return name or 'Unnamed'

# ============================================================================ reading portal paths

STRUCTURAL = re.compile(
    r'(?ix)^( sem(ester)?[\s_-]*0?[ivx\d]+([\s_-]*(spring|fall|autumn))? | [ivx\d]+(st|nd|rd|th)?[\s_-]*(sem(ester)?|trim(ester)?)'
    r' | trim(ester)?[\s_-]*([ivx]+|\d+)(st|nd|rd|th)? | \d(st|nd|rd|th)?[\s_-]*year | teaching[\s_]*scheme | all[\s_]*streams?'
    r' | common[\w\s]* )$')
FILENAME_STOP = re.compile(
    r'(?ix)[\s,._-]*( \( | \bbatch | \bbacth | \bsem\b | \bsem[-_ ]?[ivx\d]+\b | \bsemester\b | \btrim\b | \bfinal\b | \bfianl\b'
    r' | \bre[-_ ]?ex(am)? | \breexam | \bend[-_ ]?sem | \b(19|20)\d\d | \b\d{2}[-_]\d{2}\b | \bb\.?[\s_]?tech\b | \bmba[\s_]?tech\b'
    r' | \bm[\s_]?tech\b | \bmca\b | \bphd\b | \b\d\s?(st|nd|rd|th)\b | \byear\b | \bexam\b | \bquestion[\s_]paper | ,'
    r' | \s(b|ba|bat|batc)$ )')
YEAR_PAIR = re.compile(r'(?<!\d)((?:19|20)\d\d)\s*[-_/]\s*(\d{4}|\d{2})')
SHORT_PAIR = re.compile(r'(?<![\d-])([0-2]\d)\s*-\s*([0-3]\d)(?![\d-])')       # "16-17", "BATCH 17-18"
LONE_YEAR = re.compile(r'(?<!\d)((?:19|20)\d\d)(?!\d)')


def subject_from_filename(name):
    """Best-effort subject text from a legacy file name such as 'FLUID MACHINERY BATCH 2015-16 RE EXAM.pdf'."""
    text = re.sub(r'\.[A-Za-z0-9]{1,5}$', '', name)
    cut = bool(HASH_SUFFIX.search(text))
    text = UPLOAD_TOKEN.sub('', HASH_SUFFIX.sub('', text)).replace('_', ' ')
    text = re.sub(r'^(?:QP|ANS|ANSWER|SOLUTION|SOL)[\s-]+', '', text, flags=re.I)
    text = re.sub(r'(?<=[A-Za-z\s])\d{4}$|\(\d+\)$', '', text).strip()   # scanner counters: "...Ba0001", "(31)"
    match = FILENAME_STOP.search(text)
    if match:
        text = text[:match.start()]
    elif cut:
        text = text.rsplit(' ', 1)[0]               # name was cut mid-word by the portal
    text = re.sub(r'\s*\d{3,}$', '', text)
    return re.sub(r'\s+', ' ', text).strip(' .,-&')


def subject_from_portal_filename(name):
    """'QP_Introduction to Business Statistics, Analytics & Modeling-I(702BS0C018)_2024-2025.pdf' -> the full name."""
    text = re.sub(r'\.[A-Za-z0-9]{1,5}$', '', name)
    text = re.sub(r'(?i)^(?:QP|ANS|data_set)_', '', HASH_SUFFIX.sub('', text))
    text = re.sub(r'(?i)^(?:final|re)-exam_', '', text)          # names inside the portal's ZIP downloads
    text = re.split(r'_(?:19|20)\d\d-(?:19|20)\d\d', text)[0]
    text = re.sub(r'(?i)_(?:semester|sem)\s*[ivx\d]+$', '', text)
    if '(' in text:                                     # course code "(702BS0C018)", possibly cut short
        text = text[:text.rindex('(')]
    return re.sub(r'\s+', ' ', text).strip(' .,-&_')


def is_weak(name):
    key = ' '.join(t for t in tokens(name) if t not in ROMAN_VALUE and not t.isdigit())
    return len(key.replace(' ', '')) < 3 or key in WEAK_NAMES or not re.search(r'[a-z]{2}', key)


def academic_year(*texts):
    """Latest academic year mentioned, as '2015-16'; falls back to a lone year, else ''."""
    years = []
    for text in texts:
        for first, second in YEAR_PAIR.findall(text):
            start = int(first)
            if (len(second) == 4 and int(second) == start + 1) or (len(second) == 2 and int(second) == (start + 1) % 100):
                years.append(start)
            elif len(second) == 4 and int(second[:2]) == (start + 1) % 100:   # "2011-120001": scan counter follows
                years.append(start)
        for first, second in SHORT_PAIR.findall(text):
            if int(second) == (int(first) + 1) % 100:
                years.append(2000 + int(first))
    years = [y for y in years if 1995 <= y <= 2030]
    if years:
        start = max(years)
        return f'{start}-{(start + 1) % 100:02d}'
    lone = [int(y) for text in texts for y in LONE_YEAR.findall(text) if 1995 <= int(y) <= 2030]
    return str(max(lone)) if lone else ''


def exam_type(text):
    low = text.lower().replace('_', ' ')
    re_exam = bool(re.search(r're[\s-]?ex(am)?\b|reexam|re[\s-]?examination|\bre\b', low))
    final = bool(re.search(r'\bfinal|\bfianl|end[\s-]?sem', low))
    if re_exam and final:
        return 'Final + Re-Exam'
    return 'Re-Exam' if re_exam else 'Final-Exam' if final else ''


def semester_label(parts):
    for part in reversed(parts):
        low = part.lower().replace('_', ' ').replace('-', ' ').strip()
        match = (re.fullmatch(r'sem(?:ester)?\s*0?(\d{1,2}|[ivx]+)(?:\s+\w+)?', low)
                 or re.fullmatch(r'([ivx]+|\d{1,2})\s*sem(?:ester)?', low))
        if match:
            value = match.group(1)
            return f'Sem {int(value) if value.isdigit() else ROMAN_VALUE.get(value, value)}'
        match = (re.fullmatch(r'trim(?:ester)?\s*([ivx]+|\d+)(?:st|nd|rd|th)?', low)
                 or re.fullmatch(r'([ivx]+)\s*trim(?:ester)?', low))
        if match:
            value = match.group(1)
            return f'Trim {int(value) if value.isdigit() else ROMAN_VALUE.get(value, value)}'
    return ''


def kind_of(filename):
    low = filename.lower()
    if low.startswith('qp_'):
        return 'Question paper'
    if low.startswith(('ans_', 'answer', 'solution')) or re.search(r'\b(answer key|solutions?|model answers?)\b', low):
        return 'Answer key'
    if low.startswith('data_set') or low.endswith(('.xlsx', '.xls', '.csv')):
        return 'Dataset'
    if low.endswith(('.zip', '.rar', '.7z')):
        return 'ZIP of papers'
    return 'Question paper'


def read_entry(row):
    """Facts read from one manifest path under 02_Question_Papers/."""
    parts = row['path'].split('/')
    filename = parts[-1]
    if parts[1] != 'Legacy':
        # 02_Question_Papers/<year>/Sem_NN/<exam>/<programme>/<subject>/<file>
        _, folder_year, semester, exam, programme, subject = parts[:6]
        return {
            'folder': subject, 'from_file': subject_from_portal_filename(filename),
            'directory': '/'.join(parts[:-1]), 'portal': True,
            'source': f'Portal {folder_year}', 'exam': exam, 'semester': semester_label([semester]),
            'programme': HASH_SUFFIX.sub('', programme).replace('_', ' ').strip(),
            'academic_year': academic_year(filename) or folder_year, 'kind': kind_of(filename), 'label_folder': False,
        }
    # 02_Question_Papers/Legacy/<programme>/<year>/[<branch>/]<semester>/<subject>/<file>  (depth varies)
    middle = parts[2:-1]
    parent = middle[-1]
    label = bool(STRUCTURAL.match(parent.strip())) or len(middle) == 1
    branch = [p for p in middle[1:-1] if not STRUCTURAL.match(p.strip()) and not re.fullmatch(r'(?i)\d\w*\s*year', p)]
    return {
        'folder': parent, 'from_file': subject_from_filename(filename), 'directory': '/'.join(parts[:-1]),
        'portal': False, 'source': 'Legacy archive', 'exam': exam_type(filename),
        'semester': semester_label(middle), 'programme': ' / '.join([middle[0]] + branch[:1]),
        'academic_year': academic_year(filename), 'kind': kind_of(filename), 'label_folder': label,
    }

# ============================================================================ classification


class Clusters:
    """Greedy clustering of subject spellings; the most common spelling seeds each cluster."""

    def __init__(self):
        self.parent = {}
        self.seeds = defaultdict(list)          # numerals tuple -> seed keys
        self.compact = {}                       # key without spaces -> seed ("I C Engines" == "IC Engines")

    def add(self, key):
        if key not in self.parent:
            seed = self.compact.get(key.replace(' ', '')) or next(
                (s for s in self.seeds[numerals(key)] if same_subject(key, s)), None)
            self.parent[key] = seed or key
            if not seed:
                self.seeds[numerals(key)].append(key)
                self.compact[key.replace(' ', '')] = key
        return self.root(key)

    def join(self, key, into):
        self.parent[self.root(key)] = self.root(into)

    def root(self, key):
        while self.parent[key] != key:
            key = self.parent[key]
        return key


def load_aliases(path=ALIASES_FILE):
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    return {loose_key(k): v for k, v in data.items() if not k.startswith('_')}


def load_overrides(path=OVERRIDES_FILE):
    """Paper-level corrections: original path -> {"subject": ..., "printed": subject printed on the paper}, or
    {"kind": ..., "note": ...} for a file that is not what its name says."""
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    return {k: v if isinstance(v, dict) else {'subject': v} for k, v in data.items() if not k.startswith('_')}


def question_paper_path(location):
    """Where a paper kept only inside a raw ZIP download would sit under 02_Question_Papers/, from the folder the
    ZIP was downloaded from plus the member's path inside it; None for syllabi and anything else."""
    parts = [p for p in location.split('/') if p]
    if len(parts) >= 3 and parts[0] == 'QUESTIONS PAPERS':
        return QP_ROOT + 'Legacy/' + '/'.join(parts[1:])
    if len(parts) >= 4 and parts[0] == 'SYLLABUS' and EXAM_FILE.search(parts[-1]):
        # The portal's syllabus section also holds exam papers ('..._Year_2022-23__Final_Exam_x.pdf') under
        # <programme>/<year of study>/<branch>/<semester>/<subject>/: file them like the legacy papers.
        return QP_ROOT + 'Legacy/' + '/'.join(parts[1:])
    if len(parts) >= 6 and re.fullmatch(r'(?:19|20)\d\d', parts[0]):
        # <year>/Semester <n>/<exam>/<programme - code>/<subject>/<file>; some ZIPs nest a second
        # <exam>/<programme>/<subject> inside the first, so the programme is the last folder with a code.
        programme_at = max((i for i, p in enumerate(parts[:-2]) if i >= 3 and re.search(r' - \d{3,6}$', p)), default=3)
        exam = next((p for p in reversed(parts[2:programme_at]) if re.fullmatch(r'(?i)(final|re)-exam', p)), parts[2])
        printed = re.search(r'(?i)_semester\s+([ivx]+|\d+)_', parts[-1])  # the file's own semester wins
        match = printed or re.fullmatch(r'(?i)semester\s+([ivx]+|\d+)', parts[1])
        number = match and (int(match.group(1)) if match.group(1).isdigit() else ROMAN_VALUE.get(match.group(1).lower()))
        if number:
            return QP_ROOT + f'{parts[0]}/Sem_{number:02d}/{exam}/{parts[programme_at]}/{parts[-2]}/{parts[-1]}'
    return None


def raw_zip_location(entry):
    """Download folder + member path for a ZIP member: the recorded virtual path, else the ZIP's own folder
    ('2024/Semester I/65063__Final-Exam__context_fixed.zip' holds '<programme>/<subject>/<file>')."""
    if entry.get('virtual_path'):
        return entry['virtual_path']
    folder, _, name = entry['zip_path'].removeprefix('00_Original_Downloads/').rpartition('/')
    exam = re.match(r'\d+__((?:Final|Re)-Exam)', name)
    return f"{folder}/{exam.group(1)}/{entry['member']}" if exam else ''


def raw_zip_rows(manifest_files, members_file=RAW_MEMBERS_FILE, papers_file=RAW_PAPERS_FILE):
    """Manifest-style rows for question papers that exist only inside raw ZIP downloads (never extracted into
    02_Question_Papers/). Each row's 'path' is where the paper would sit there (used to classify it) and
    'location' is '<zip path> :: <member>'. Members whose bytes already appear under 02_Question_Papers/ are left
    out: that paper is already listed."""
    if not members_file.exists() or not papers_file.exists():
        return []
    listed = {f['sha256'] for f in manifest_files if f['path'].startswith(QP_ROOT)}
    members = {(m['zip_path'], m['member']): m for m in json.loads(members_file.read_text(encoding='utf-8'))}
    rows, seen = [], set()
    with papers_file.open(encoding='utf-8') as stream:
        for line in stream:
            paper = json.loads(line)
            if paper.get('missing') or paper['sha256'] in listed:
                continue
            entry = members.get((paper['zip_path'], paper['member'])) or {**paper, 'virtual_path': ''}
            path = question_paper_path(raw_zip_location(entry))
            if not path or (path, paper['sha256']) in seen:
                continue
            seen.add((path, paper['sha256']))
            rows.append({'path': path, 'sha256': paper['sha256'], 'bytes': paper['bytes'],
                         'location': paper['zip_path'] + IN_ZIP + paper['member']})
    return rows


def classify(manifest_files, aliases=None, overrides=None, raw_rows=()):
    """Return one record per question-paper path with its canonical subject (raw_rows: see raw_zip_rows)."""
    aliases = aliases or {}
    overrides = overrides or {}
    rows = sorted([r for r in manifest_files if r['path'].startswith(QP_ROOT)] + list(raw_rows),
                  key=lambda r: (r['path'], r.get('location', '')))
    facts = [read_entry(r) for r in rows]

    # Vocabulary: every subject folder that is not a semester / branch label.
    vocabulary = set()
    folder_dirs = defaultdict(set)
    for fact in facts:
        folder = HASH_SUFFIX.sub('', fact['folder']).strip()
        if not fact['label_folder'] and not is_weak(folder):
            vocabulary.add(loose_key(folder))
            folder_dirs[loose_key(folder)].add(fact['directory'])
    by_length = defaultdict(list)
    for key in vocabulary:
        by_length[len(key)].append(key)

    def known(name, besides=None):
        """Is this a subject some folder is named after (other than the spelling `besides`)?"""
        key = loose_key(name)
        if key != besides and key in vocabulary:
            return True
        return any(other != key and other != besides and same_subject(key, other)
                   for size in range(len(key) - 6, len(key) + 7) for other in by_length[size])

    def overlap(a, b):
        return bool((set(loose_key(a).split()) & set(loose_key(b).split())) - set(ROMAN_VALUE))

    # Per directory: do the file names agree on one subject?
    dir_file_subjects = defaultdict(set)
    for fact in facts:
        if fact['from_file'] and not is_weak(fact['from_file']):
            dir_file_subjects[fact['directory']].add(loose_key(fact['from_file']))

    choices = []
    for fact in facts:
        folder_raw = fact['folder']
        folder = HASH_SUFFIX.sub('', folder_raw).strip()
        from_file = fact['from_file']
        truncated = bool(HASH_SUFFIX.search(folder_raw))
        choice, note = folder, ''
        if fact['portal']:
            if truncated and from_file and loose_key(from_file).startswith(loose_key(folder).rsplit(' ', 1)[0]):
                choice = from_file                          # portal cut the folder name; file name has it in full
        elif not from_file or is_weak(from_file):
            if fact['label_folder'] or is_weak(folder):
                choice, note = 'Unsorted papers', 'no subject in its folder or file name'
        elif fact['label_folder'] or is_weak(folder):
            choice, note = from_file, f'folder "{folder}" is a semester/branch label; subject read from file name'
        elif truncated and loose_key(from_file).replace(' ', '').startswith(loose_key(folder).replace(' ', '')[:-2]):
            choice = from_file                              # portal cut the folder name; file name has it in full
        elif not same_subject(loose_key(folder), loose_key(from_file)) and known(from_file):
            # A folder spelling used only here, matching no other subject, whose files all agree, is a typo.
            lone_folder = len(folder_dirs[loose_key(folder)]) == 1 and not known(folder, besides=loose_key(folder))
            consistent = len({k for k in dir_file_subjects[fact['directory']]
                              if not same_subject(k, loose_key(from_file))}) == 0
            if not overlap(folder, from_file):
                choice, note = from_file, f'filed under "{folder}" but the file name says "{from_file}"'
            elif lone_folder and consistent and SequenceMatcher(None, loose_key(folder), loose_key(from_file)).ratio() >= 0.7:
                choice, note = from_file, f'folder "{folder}" looks misspelt; file names say "{from_file}"'
        choices.append((choice, note, truncated and choice == folder))

    # Cluster spellings, most frequent first so the common spelling seeds its cluster.
    clusters = Clusters()
    counts = Counter(loose_key(c) for c, _, _ in choices)
    for key, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        clusters.add(key)
    # Truncated folder names (portal cut them and appended a hash) join the full name they start with.
    seeds = sorted({clusters.root(k) for k in counts}, key=lambda k: (-len(k), k))
    for choice, _, truncated in choices:
        key = loose_key(choice)
        if truncated and clusters.root(key) == key:
            prefix = key.replace(' ', '')[:-2]
            longer = next((s for s in seeds if len(s) > len(key) + 2 and s.replace(' ', '').startswith(prefix)), None)
            if longer:
                clusters.join(key, longer)

    # Display name: the spelling with the fewest rare or misspelt words, then the most used.
    # A word is a likely misspelling when only one subject uses it, or when it is rare and a lookalike word
    # is at least 3x more common.
    word_files, word_subjects = Counter(), defaultdict(set)
    for fact, (choice, _, _) in zip(facts, choices):
        for spelling in (choice, fact['from_file']):
            for word in set(words(spelling)):
                word_subjects[stem(word)].add(loose_key(spelling))
        for word in set(words(choice)) | set(words(fact['from_file'])):
            word_files[stem(word)] += 1
    by_initial = defaultdict(list)
    for word, count in word_files.items():
        if count >= 3 and len(word) > 3:
            by_initial[word[0]].append(word)

    def misspelt(word):
        word = stem(word)
        if len(word) <= 3 or word.isdigit():
            return False
        count = word_files[word]
        return len(word_subjects[word]) <= 1 or (count < 10 and any(
            word_files[other] >= 3 * max(count, 1) and misspelling(word, other)
            for other in by_initial[word[0]] if other != word))
    votes = defaultdict(Counter)
    for fact, (choice, _, truncated) in zip(facts, choices):
        root = clusters.root(loose_key(choice))
        weight = 3 if fact['portal'] else 1
        votes[root][(display_case(choice), truncated)] += weight
        if fact['from_file'] and not is_weak(fact['from_file']) and same_subject(loose_key(fact['from_file']), root):
            votes[root][(display_case(fact['from_file']), False)] += 1

    def oddness(spelling, truncated):
        """Likely misspellings count 1 each, a bracketed aside 1, a cut-off name 10."""
        return (10 if truncated else 0) + ('(' in spelling) + sum(misspelt(w) for w in words(spelling))

    def best_name(cands):
        (spelling, truncated), _ = min(cands.items(), key=lambda kv: (oddness(*kv[0]), -kv[1], kv[0][0]))
        if truncated:                                   # only a cut-off name exists: drop the partial word
            trimmed = spelling.rsplit(' ', 1)[0]
            while trimmed.rsplit(' ', 1)[-1].lower() in SMALL_WORDS and ' ' in trimmed:
                trimmed = trimmed.rsplit(' ', 1)[0]
            spelling = trimmed.rstrip(' ,-')
        return spelling

    names = {root: best_name(cands) for root, cands in votes.items()}

    # subject_aliases.json: a key names either one spelling or a whole subject; the value names the subject
    # to use (any spelling of an existing subject, or a new name).
    def alias_for(key):
        if key in aliases:
            return aliases[key]
        return aliases.get(loose_key(names[clusters.root(key)]))

    unaliased = {loose_key(n): n for root, n in names.items() if loose_key(n) not in aliases and root not in aliases}

    def resolve(target):
        key = loose_key(target)
        if key in unaliased:
            return unaliased[key]
        if key in clusters.parent and loose_key(names[clusters.root(key)]) in unaliased:
            return names[clusters.root(key)]
        return next((n for k, n in unaliased.items() if same_subject(key, k)), display_case(target))

    records = []
    for row, fact, (choice, note, _) in zip(rows, facts, choices):
        key = loose_key(choice)
        target = alias_for(key)
        if target:
            subject = resolve(target)
            note = (note + '; ' if note else '') + 'placed by subject_aliases.json'
        else:
            subject = names[clusters.root(key)]
        records.append({
            'subject': subject, 'academic_year': fact['academic_year'], 'exam': fact['exam'], 'kind': fact['kind'],
            'semester': fact['semester'], 'programme': fact['programme'],
            'source': fact['source'] + (' (ZIP download only)' if row.get('location') else ''),
            'bytes': row['bytes'], 'sha256': row['sha256'], 'path': row.get('location') or row['path'],
            'filed_as': choice, 'note': note,
        })
    # subject_overrides.json: papers whose own header names a different subject. Identical copies of the
    # same file elsewhere follow the same correction.
    # An override can also say what a file really is ("kind" and "note"): e.g. screenshots filed as a paper.
    by_sha = {r['sha256']: overrides[r['path']] for r in records if r['path'] in overrides}
    for record in records:
        fix = by_sha.get(record['sha256'])
        if fix and fix.get('subject'):
            record['subject'] = resolve(fix['subject'])
            printed = fix.get('printed') or fix['subject']
            record['note'] = f'filed under "{record["filed_as"]}" but the paper is headed "{printed}"'
        if fix and fix.get('kind'):
            record['kind'] = fix['kind']
            record['note'] = ((record['note'] + '; ') if record['note'] else '') + fix.get('note', '')
    # A file the portal also lists among the syllabi (the same bytes in 04_Syllabi_Archive/) is a syllabus that
    # was filed with the question papers: it is kept here but not read as a paper. Unless some copy of it, here,
    # there or inside a raw ZIP, is named as an exam paper: the syllabus section holds papers too.
    names = defaultdict(set)
    for r in manifest_files:
        names[r['sha256']].add(r['path'].rsplit('/', 1)[-1])
    if RAW_PAPERS_FILE.exists():
        with RAW_PAPERS_FILE.open(encoding='utf-8') as stream:
            for line in stream:
                member = json.loads(line)
                if member.get('sha256'):
                    names[member['sha256']].add(member['member'].rsplit('/', 1)[-1])
    syllabi = {r['sha256'] for r in manifest_files if r['path'].startswith(SYLLABUS_ROOT)
               and not any(EXAM_FILE.search(n) for n in names[r['sha256']])}
    for record in records:
        if record['sha256'] in syllabi and record['kind'] == 'Question paper':
            record['kind'] = 'Syllabus'
            record['note'] = ((record['note'] + '; ') if record['note'] else '') + \
                'a syllabus filed with the question papers (the same file is in 04_Syllabi_Archive/)'
    return records

# ============================================================================ manifest and index I/O


def sha256_of(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def gh(*args):
    if not shutil.which('gh'):
        raise SystemExit('Install GitHub CLI and run "gh auth login" with an account that can read ' + REPO)
    run = subprocess.run(['gh', *args], capture_output=True, text=True, encoding='utf-8')
    if run.returncode:
        raise SystemExit(run.stderr[-800:])
    return json.loads(run.stdout) if run.stdout.lstrip().startswith(('{', '[')) else run.stdout.strip()


def load_manifest(path=None):
    """Read the full-library manifest, downloading and digest-checking it when no path is given."""
    if path:
        return Path(path), json.loads(Path(path).read_text(encoding='utf-8'))
    path = HERE / MANIFEST_NAME
    release = gh('api', f'repos/{REPO}/releases/tags/{TAG}')
    pages = gh('api', '--paginate', '--slurp', f"repos/{REPO}/releases/{release['id']}/assets?per_page=100")
    asset = next(a for page in pages for a in page if a['name'] == MANIFEST_NAME)
    if not path.exists():
        gh('release', 'download', TAG, '--repo', REPO, '--pattern', MANIFEST_NAME, '--dir', str(HERE))
    if path.stat().st_size != asset['size'] or 'sha256:' + sha256_of(path) != asset['digest']:
        raise SystemExit(f'{path} does not match the release; delete it and run again.')
    return path, json.loads(path.read_text(encoding='utf-8'))


def load_records(manifest=None):
    """Subject records from the committed index, or classified afresh from a manifest."""
    if manifest or not INDEX_CSV.exists():
        _, data = load_manifest(manifest)
        return classify(data['files'], load_aliases(), load_overrides(), raw_zip_rows(data['files']))
    with INDEX_CSV.open(encoding='utf-8', newline='') as stream:
        records = list(csv.DictReader(stream))
    for record in records:
        record['bytes'] = int(record['bytes'])
    return records


def subject_folders(subjects):
    """Unique, Windows-safe folder name per subject (case-insensitive)."""
    used, out = set(), {}
    for subject in sorted(subjects, key=caseless):
        name, n = folder_name(subject), 2
        while name.lower() in used:
            name, n = f'{folder_name(subject)} ({n})', n + 1
        used.add(name.lower())
        out[subject] = name
    return out


def year_span(years):
    years = sorted(y for y in years if y)
    if not years:
        return 'year not stated'
    return years[0] if years[0] == years[-1] else f'{years[0]} to {years[-1]}'

# ============================================================================ commands


def cmd_list(args):
    records = load_records(args.manifest)
    by_subject = defaultdict(list)
    for record in records:
        by_subject[record['subject']].append(record)
    query = loose_key(args.search) if args.search else ''
    shown = 0
    for subject in sorted(by_subject, key=caseless):
        if query and query not in loose_key(subject) and args.search.lower() not in subject.lower():
            continue
        rows = by_subject[subject]
        print(f"{len(rows):6}  {len({r['sha256'] for r in rows}):6}  {year_span({r['academic_year'] for r in rows}):20}  {subject}")
        shown += 1
    print(f'{shown} subjects shown (columns: file paths, unique files, years, subject).')


def pick_subjects(records, wanted):
    names = {r['subject'] for r in records}
    by_key = {loose_key(n): n for n in names}
    chosen = []
    for want in wanted:
        match = next((n for n in sorted(names) if n.lower() == want.lower()), None) or by_key.get(loose_key(want))
        if not match:
            hints = [n for n in sorted(names) if loose_key(want) in loose_key(n) or want.lower() in n.lower()][:15]
            raise SystemExit(f'No subject called "{want}".' + (' Did you mean:\n  ' + '\n  '.join(hints) if hints else
                             ' Use "list --search" to find the exact name.'))
        chosen.append(match)
    return chosen


def target_name(record):
    """File name inside <Subject>/<Year>/: portal papers get exam, type and programme; legacy keep their name."""
    original = PurePosixPath(record['path']).name
    if not record['source'].startswith('Portal'):
        return original
    suffix = PurePosixPath(original).suffix
    kind = {'Question paper': 'QP', 'Answer key': 'Answers', 'Dataset': 'Dataset'}.get(record['kind'], record['kind'])
    programme = re.sub(r'\s+', ' ', record['programme'])[:45].strip()
    return f"{record['exam']} {kind} - {programme}{suffix}"


def safe_name(name, limit=110):
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '-', name).strip(' ')
    stem_part, dot, ext = name.rpartition('.')
    if not dot or len(ext) > 5:
        stem_part, ext = name, ''
    stem_part = stem_part.rstrip(' .')
    if len(name) > limit:
        digest = hashlib.sha1(name.encode()).hexdigest()[:6]
        stem_part = stem_part[:limit - len(ext) - 9].rstrip(' .') + '~' + digest
    return stem_part + ('.' + ext if ext else '')


def build_tree(records, library, out, copy=False):
    """Hard-link (or copy) restored papers into out/<Subject>/<Year>/<name>; identical files appear once."""
    library, out = library.resolve(), out.resolve()
    folders = subject_folders({r['subject'] for r in records})
    placed, missing, linked, copied, extracted, duplicates = {}, [], 0, 0, 0, 0
    taken = set()
    rows = []
    for record in sorted(records, key=lambda r: (r['subject'].lower(), r['academic_year'], r['path'])):
        container, _, member = record['path'].partition(IN_ZIP)
        source = library.joinpath(*PurePosixPath(container).parts)
        if not source.is_file():
            missing.append(record['path'])
            continue
        key = (record['subject'], record['sha256'])
        if key in placed:
            duplicates += 1
            rows.append([record['subject'], placed[key], record['path']])
            continue
        year = record['academic_year'] or 'Year not stated'
        directory = out / folders[record['subject']] / year
        name = safe_name(target_name(record))
        target, n = directory / name, 2
        while str(target).lower() in taken:
            stem_part, dot, ext = name.rpartition('.')
            target = directory / (f'{stem_part} ({n}).{ext}' if dot else f'{name} ({n})')
            n += 1
        taken.add(str(target).lower())
        directory.mkdir(parents=True, exist_ok=True)
        if target.exists():
            if target.stat().st_size != record['bytes'] or sha256_of(target) != record['sha256']:
                raise SystemExit(f'Refusing to overwrite a different file: {target}')
        elif member:                                    # a paper kept only inside a ZIP download
            with zipfile.ZipFile(source) as archive:
                data = archive.read(member)
            if hashlib.sha256(data).hexdigest() != record['sha256']:
                raise SystemExit(f'{member} in {source} does not match the index; restore the ZIP again.')
            partial = target.with_name(target.name + '.partial')
            partial.write_bytes(data)
            partial.replace(target)
            extracted += 1
        elif copy:
            shutil.copy2(source, target)
            copied += 1
        else:
            try:
                os.link(source, target)
                linked += 1
            except OSError:
                shutil.copy2(source, target)
                copied += 1
        relative = target.relative_to(out).as_posix()
        placed[key] = relative
        rows.append([record['subject'], relative, record['path']])
    out.mkdir(parents=True, exist_ok=True)
    with (out / '_subject_tree_index.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['subject', 'file_in_this_tree', 'original_library_path'])
        writer.writerows(rows)
    print(f'{len(placed)} files placed in {out} ({linked} hard links, {copied} copies, {extracted} extracted from '
          f'ZIP downloads); {duplicates} identical duplicates skipped.')
    if missing:
        print(f'{len(missing)} papers are not in {library}; restore them first (first: {missing[0]}).')
    return placed, missing


def cmd_link(args):
    records = load_records(args.manifest)
    if args.subject:
        chosen = set(pick_subjects(records, args.subject))
        records = [r for r in records if r['subject'] in chosen]
    library = Path(args.library)
    if not (library / '02_Question_Papers').is_dir():
        raise SystemExit(f'{library} has no 02_Question_Papers folder; point --library at the restored library root.')
    build_tree(records, library, Path(args.out) if args.out else library / TREE_NAME, args.copy)


def cmd_restore(args):
    if not INDEX_CSV.exists():
        raise SystemExit(f'{INDEX_CSV} is missing; run this from a full checkout of the repository.')
    records = load_records()
    chosen = set(pick_subjects(records, args.subject))
    manifest_path, _ = load_manifest(args.manifest)
    records = [r for r in records if r['subject'] in chosen]
    paths = sorted({r['path'].partition(IN_ZIP)[0] for r in records})
    size = sum({r['sha256']: r['bytes'] for r in records}.values())
    zips = sorted({r['path'].partition(IN_ZIP)[0] for r in records if IN_ZIP in r['path']})
    print(f'Restoring {len(records)} papers ({size / 2**20:.0f} MiB) for: {", ".join(sorted(chosen))}', flush=True)
    if zips:
        print(f'{len(zips)} ZIP download(s) are restored whole because some papers exist only inside them.', flush=True)
    sys.path.insert(0, str(HERE))
    import restore_library
    destination = Path(args.destination)
    argv = ['restore_library.py', '--destination', str(destination), '--manifest', str(manifest_path)]
    if args.staging:
        argv += ['--staging', str(args.staging)]
    for path in paths:
        argv += ['--path', path]
    saved, sys.argv = sys.argv, argv
    try:
        restore_library.main()
    finally:
        sys.argv = saved
    build_tree(records, destination, Path(args.out) if args.out else destination / TREE_NAME, args.copy)


def md_cell(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')


def write_catalog(records, index_dir=INDEX_DIR):
    """Regenerate subjects/: master README, one README per subject, and the CSV index.

    Folders of subjects that no longer exist are removed; in current subject folders only README.md is
    rewritten, so question text written there by build_question_bank.py is kept."""
    by_subject = defaultdict(list)
    for record in records:
        by_subject[record['subject']].append(record)
    folders = subject_folders(by_subject)
    current = set(folders.values())
    if index_dir.exists():
        for child in index_dir.iterdir():
            if child.is_dir() and child.name not in current:
                shutil.rmtree(child)
            elif child.is_file():
                child.unlink()
    index_dir.mkdir(parents=True, exist_ok=True)
    with (index_dir / INDEX_CSV.name).open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for record in sorted(records, key=lambda r: (r['subject'].lower(), r['path'])):
            writer.writerow({k: record[k] for k in CSV_FIELDS})

    def sem_order(label):
        kind, _, number = label.partition(' ')
        return kind, int(number) if number.isdigit() else 99, label

    def joined(values, order=caseless):
        return ', '.join(sorted({v for v in values if v}, key=order))

    summary = []
    for subject, rows in by_subject.items():
        folder = folders[subject]
        papers = defaultdict(list)                      # identical files filed under several programmes
        for record in rows:
            papers[record['sha256']].append(record)
        years = year_span({r['academic_year'] for r in rows})
        programmes = sorted({r['programme'] for r in rows})
        semesters = sorted({r['semester'] for r in rows if r['semester']}, key=sem_order)
        # Spellings merged into this subject; folders of individually moved files are explained in the notes.
        filed_as = sorted({HASH_SUFFIX.sub('', r['filed_as']) for r in rows
                           if not r['note'] and display_case(r['filed_as']) != subject}, key=caseless)
        summary.append((subject, folder, len(rows), len(papers), years, len(programmes)))
        lines = [
            f'# {subject}', '',
            f'**{len(papers)}** unique papers ({len(rows)} copies across programmes) · {years} · '
            f'{len(programmes)} programme{"s" if len(programmes) != 1 else ""}'
            + (f' · {", ".join(semesters)}' if semesters else ''), '',
            'Download only this subject, sorted by academic year:', '',
            '```powershell',
            f'python organize_by_subject.py restore --destination D:/Study --subject "{subject}"',
            '```', '',
            f'Files land in `D:/Study/{TREE_NAME}/{folder}/<academic year>/`. Identical copies of one paper '
            '(the portal often files the same PDF under several programmes) are placed once.', '',
            'Text of the papers, ready for reading or AI analysis: [`papers.md`](papers.md) (every paper in full, '
            'newest first), [`questions.jsonl`](questions.jsonl) (one record per question with marks, year, exam, '
            'semester and department) and [`papers.jsonl`](papers.jsonl) (one record per paper). Answer keys, where '
            'the portal published them, are in `answer_keys.md`. See '
            '[`question_bank/README.md`](../../question_bank/README.md) for the fields.', '',
        ]
        if (index_dir / folder / 'syllabus.md').exists():
            lines += ['Syllabus of this course, every version found in the archive: [`syllabus.md`](syllabus.md) '
                      '(see [`syllabi/`](../../syllabi/README.md) for all programmes).', '']
        if filed_as:
            lines += ['Also filed as: ' + ', '.join(f'`{md_cell(x)}`' for x in filed_as), '']
        lines += ['| Year | Exam | Type | Sem | Programmes | File |', '| --- | --- | --- | --- | --- | --- |']
        notes = []

        def paper_order(copies):
            first = copies[0]
            return (-int((first['academic_year'] or '0')[:4]), first['exam'], KIND_ORDER.get(first['kind'], 9),
                    first['programme'], first['path'])

        for copies in sorted((sorted(c, key=lambda r: r['path']) for c in papers.values()), key=paper_order):
            first = copies[0]
            name = PurePosixPath(first['path']).name
            for note in dict.fromkeys(r['note'] for r in copies if r['note']):
                notes.append(note)
                name += f' [{len(notes)}]'
            lines.append('| ' + ' | '.join(md_cell(x) for x in (
                first['academic_year'] or '—', joined(r['exam'] for r in copies) or '—', first['kind'],
                joined((r['semester'] for r in copies), sem_order), joined(r['programme'] for r in copies),
                name)) + ' |')
        if notes:
            lines += ['', '**Notes on papers placed here from a different folder**', '']
            lines += [f'{i}. {md_cell(n)}' for i, n in enumerate(notes, 1)]
        lines += ['', f'Full original paths are in [`pyq_subject_index.csv`](../{INDEX_CSV.name}). '
                  'If a paper is in the wrong subject, add its spelling to `subject_aliases.json` and rerun '
                  '`python organize_by_subject.py catalog`.', '']
        (index_dir / folder).mkdir(exist_ok=True)
        (index_dir / folder / 'README.md').write_text('\n'.join(lines), encoding='utf-8')

    total_unique = len({r['sha256'] for r in records})
    in_zips = sum(1 for r in records if IN_ZIP in r['path'])
    lines = [
        '# PYQs by subject', '',
        f'All **{len(records):,}** question-paper files in the archive ({total_unique:,} unique) sorted into '
        f'**{len(by_subject):,} subjects**: every file in `02_Question_Papers/`, plus {in_zips:,} papers that exist '
        'only inside the portal\'s original ZIP downloads (listed as `<ZIP> :: <file>`; restore extracts them). '
        'Spelling variants of one subject are merged, '
        'e.g. `APPLIED MATHEMATICES II` and `Applied Mathematics II`. Each folder below has a README listing '
        'every paper for that subject by year, exam, semester and programme.', '',
        'The PDFs themselves stay in the private release (18.6 GiB; too large for git). '
        'To get a subject\'s papers on your machine, sorted into folders:', '',
        '```powershell',
        'gh auth login                     # once, with an account that can read this private repository',
        f'gh repo clone {REPO}',
        f'cd {REPO.split("/")[1]}',
        'python organize_by_subject.py list --search "operating"',
        'python organize_by_subject.py restore --destination D:/Study --subject "Operating Systems" --subject "Computer Networks"',
        '```', '',
        'Already restored the full library? Build the whole subject tree with hard links (no extra space on NTFS):', '',
        '```powershell',
        'python organize_by_subject.py link --library D:/MPSTME_Library_Restored',
        '```', '',
        f'Either way you get `{TREE_NAME}/<Subject>/<Academic year>/<paper>`. Newer portal papers are named '
        '`<Exam> <QP|Answers> - <Programme>.pdf`; older papers keep their original names.', '',
        '| Subject | Files | Unique | Years | Programmes |', '| --- | ---: | ---: | --- | ---: |',
    ]
    for subject, folder, count, unique, years, programmes in sorted(summary, key=lambda s: caseless(s[0])):
        lines.append(f'| [{md_cell(subject)}]({quote(folder)}/README.md) | {count} | {unique} | {years} | {programmes} |')
    lines.append('')
    (index_dir / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote {len(by_subject)} subject folders and {len(records)} index rows to {index_dir}')


def cmd_catalog(args):
    _, data = load_manifest(args.manifest)
    records = classify(data['files'], load_aliases(), load_overrides(), raw_zip_rows(data['files']))
    write_catalog(records)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('list', help='show subjects with paper counts')
    p.add_argument('--search', help='only subjects whose name contains this text')
    p.add_argument('--manifest', help='classify from this manifest instead of the committed index')
    p.set_defaults(run=cmd_list)
    p = sub.add_parser('restore', help='download chosen subjects from the release and sort them by subject')
    p.add_argument('--destination', required=True, help='folder to restore into, e.g. D:/Study')
    p.add_argument('--subject', action='append', required=True, help='exact subject name (repeatable); see list')
    p.add_argument('--out', help=f'subject tree location (default: <destination>/{TREE_NAME})')
    p.add_argument('--copy', action='store_true', help='copy files instead of hard-linking them')
    p.add_argument('--staging', help='temporary download folder on another drive')
    p.add_argument('--manifest', help='use this verified full-library-manifest.json')
    p.set_defaults(run=cmd_restore)
    p = sub.add_parser('link', help='build the subject tree from an already restored library')
    p.add_argument('--library', required=True, help='root of the restored library (contains 02_Question_Papers)')
    p.add_argument('--out', help=f'subject tree location (default: <library>/{TREE_NAME})')
    p.add_argument('--subject', action='append', help='only these subjects (repeatable)')
    p.add_argument('--copy', action='store_true', help='copy files instead of hard-linking them')
    p.add_argument('--manifest', help='classify from this manifest instead of the committed index')
    p.set_defaults(run=cmd_link)
    p = sub.add_parser('catalog', help='regenerate subjects/ from the full manifest (maintainers)')
    p.add_argument('--manifest', help='path to full-library-manifest.json (downloaded if omitted)')
    p.set_defaults(run=cmd_catalog)
    args = parser.parse_args()
    args.run(args)


if __name__ == '__main__':
    main()
