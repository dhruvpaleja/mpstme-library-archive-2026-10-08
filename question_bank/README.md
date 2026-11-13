# Question bank

Every past question paper in the archive as text, organised by subject and department, so a person or an AI can read, search and analyse it.

## Where things are

- `subjects/<Subject>/papers.md`: every paper for the subject in full, newest first, each with academic year, exam, semester, programmes, departments, max marks, duration and date.
- `subjects/<Subject>/questions.jsonl`: one JSON record per question or sub-question (fields below).
- `subjects/<Subject>/papers.jsonl`: one JSON record per paper: departments, programmes, max marks, duration, date, pages, how the text was read, and the original file path.
- `subjects/<Subject>/answer_keys.md`: answer keys the portal published (2024-25 onwards).
- `departments/<Department>/README.md`: the subjects of each department, with that branch's paper counts.
- `question_bank/subjects_summary.csv`: one row per subject with departments, counts and year range.
- `question_bank/extracted_text/*.jsonl.gz`: raw extracted text of every file, page by page, in 16 shards (input for `python build_question_bank.py build`).

## Coverage

- 1,213 subjects in 29 departments.
- 17,226 question papers and 3,368 answer keys read: 40,891 pages from the PDF text layer and 40,717 scanned pages by OCR.
- 255,907 questions and sub-questions extracted; 187,468 with marks. 16,008 papers (93%) split into 3 or more questions; the rest are kept as full text in papers.md.
- 123 question papers have low OCR quality (mostly handwritten 2004-2010 papers or poor scans); they and their questions are marked `text_quality: low`.
- 5,700 pages carry text from pictures (OCR of pasted scans, worked solutions and tables on text-layer pages, and of pictures in Word files).
- 159 scanned pages were sideways or upside down (landscape tables, phone photos); Tesseract's orientation detection found them and they were read turned upright (`pages_turned_upright` in `papers.jsonl`). Damaged PDFs (truncated downloads, a missing page list) are read as far as they go and say so in `damage`.
- 895 of these files exist only inside the portal's original ZIP downloads (`00_Original_Downloads/`), never extracted into `02_Question_Papers/`; they are included, with a path of the form `<ZIP> :: <file inside it>` and a `source` ending in "(ZIP download only)".
- Files with no readable text: 12 (PDFs the portal serves encrypted, which the archive's own re-download got the same way, and PDFs that hold only a portal error message); their `papers.jsonl` record says which in `text_status`. Data sets given with a paper (`kind: Dataset`) are included: Word and PDF ones in full, spreadsheets as one page per sheet, in full when small, otherwise the column headings and first rows.

## questions.jsonl fields

| Field | Meaning |
| --- | --- |
| `subject` | Canonical subject name (same as the folder) |
| `academic_year`, `exam`, `semester` | e.g. `2024-25`, `Final-Exam` / `Re-Exam`, `Sem 5`. The year is the one printed on the paper when it states one (file names often give the batch year; that is kept in `papers.jsonl` as `academic_year_filed`) |
| `departments` | Branches the paper was set for |
| `paper_id` | First 12 hex digits of the paper file's SHA-256; matches `papers.jsonl` for programmes, max marks, date and source file |
| `question`, `part` | Question number and part, e.g. `2` and `b`, `1.a`, `a(ii)` |
| `question_stem` | Shared instruction of the question, e.g. "Attempt any four" |
| `text` | The question text |
| `marks`, `question_marks` | Marks for this part, and for the whole question when printed |
| `co`, `bl` | Course outcome and Bloom's level tags printed on newer papers |
| `extraction` | `text` (exact, from the PDF) or `ocr` (scanned paper read by Tesseract) |
| `text_quality` | `low` when the scan read poorly (handwritten or faint papers); treat the text with care |

## Accuracy

Text-layer papers (most 2024-25 and 2025-26 papers) are extracted exactly; pictures pasted into them (worked solutions, tables, scanned questions; and pictures in Word files) are read by OCR and added after the page text under "[Text in pictures on this page, read by OCR]". Older papers are scans read by OCR: ordinary text is reliable, but equations, symbols and diagrams are often garbled, and diagrams are not captured. Splitting into questions is automatic; when a layout defeats it, the paper still appears in full in papers.md. Treat question counts and marks as a strong guide rather than an exact record.

## Using it with an AI

- Upload `subjects/<Subject>/questions.jsonl` (or `papers.md`) and ask, for example: "Which topics are asked most often, with typical marks?", "Group these questions by unit", or "Build a practice paper in the same pattern".
- For a whole department, start from `departments/<Department>/README.md` and take the subjects you need.
- Filter by year, exam or marks with any JSON tool, e.g. `jq 'select(.marks >= 10)' questions.jsonl`.

Rebuild after changing subjects or the parser: `python build_question_bank.py build` (no OCR needed).
