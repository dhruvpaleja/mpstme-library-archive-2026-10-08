# Building Construction

**6** unique papers (6 copies across programmes) · 2015 to 2018-19 · 1 programme · Trim 1

Download only this subject, sorted by academic year:

```powershell
python organize_by_subject.py restore --destination D:/Study --subject "Building Construction"
```

Files land in `D:/Study/PYQs_By_Subject/Building Construction/<academic year>/`. Identical copies of one paper (the portal often files the same PDF under several programmes) are placed once.

Text of the papers, ready for reading or AI analysis: [`papers.md`](papers.md) (every paper in full, newest first), [`questions.jsonl`](questions.jsonl) (one record per question with marks, year, exam, semester and department) and [`papers.jsonl`](papers.jsonl) (one record per paper). Answer keys, where the portal published them, are in `answer_keys.md`. See [`question_bank/README.md`](../../question_bank/README.md) for the fields.

Syllabus of this course, every version found in the archive: [`syllabus.md`](syllabus.md) (see [`syllabi/`](../../syllabi/README.md) for all programmes).

| Year | Exam | Type | Sem | Programmes | File |
| --- | --- | --- | --- | --- | --- |
| 2018-19 | Final-Exam | Question paper | Trim 1 | PGDM (Real Estate Construction AND Management) | Building Construction 2018-19 Final.pdf |
| 2018-19 | Re-Exam | Question paper | Trim 1 | PGDM (Real Estate Construction AND Management) | Building Construction Batch 2018-19 Re Exam.pdf |
| 2017-18 | Final-Exam | Question paper | Trim 1 | PGDM (Real Estate Construction AND Management) | Building Construction 2017-18 Final.pdf |
| 2017-18 | Re-Exam | Question paper | Trim 1 | PGDM (Real Estate Construction AND Management) | Building Construction Batch 2017-18 Re Exam.pdf |
| 2016-17 | Final-Exam | Question paper | Trim 1 | PGDM (Real Estate Construction AND Management) | Building Construction 2016-17 Final.pdf |
| 2015 | Final-Exam | Question paper | Trim 1 | PGDM (Real Estate Construction AND Management) | Building Construction 2015-17 Final.pdf |

Full original paths are in [`pyq_subject_index.csv`](../pyq_subject_index.csv). If a paper is in the wrong subject, add its spelling to `subject_aliases.json` and rerun `python organize_by_subject.py catalog`.
