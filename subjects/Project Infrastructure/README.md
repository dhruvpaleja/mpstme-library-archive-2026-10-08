# Project Infrastructure

**3** unique papers (3 copies across programmes) · 2015-16 to 2018-19 · 1 programme · Sem 10

Download only this subject, sorted by academic year:

```powershell
python organize_by_subject.py restore --destination D:/Study --subject "Project Infrastructure"
```

Files land in `D:/Study/PYQs_By_Subject/Project Infrastructure/<academic year>/`. Identical copies of one paper (the portal often files the same PDF under several programmes) are placed once.

Text of the papers, ready for reading or AI analysis: [`papers.md`](papers.md) (every paper in full, newest first), [`questions.jsonl`](questions.jsonl) (one record per question with marks, year, exam, semester and department) and [`papers.jsonl`](papers.jsonl) (one record per paper). Answer keys, where the portal published them, are in `answer_keys.md`. See [`question_bank/README.md`](../../question_bank/README.md) for the fields.

| Year | Exam | Type | Sem | Programmes | File |
| --- | --- | --- | --- | --- | --- |
| 2018-19 | Final-Exam | Question paper | Sem 10 | MBA TECH | Project Infrastructure...Final 18-19.pdf |
| 2016-17 | Final-Exam | Question paper | Sem 10 | MBA TECH | Project Infrastructure and Finance 2016-17 Final.pdf |
| 2015-16 | Final-Exam | Question paper | Sem 10 | MBA TECH | Project_Infrastructure_and_Finance_Batch_2015-16_Final.pdf |

Full original paths are in [`pyq_subject_index.csv`](../pyq_subject_index.csv). If a paper is in the wrong subject, add its spelling to `subject_aliases.json` and rerun `python organize_by_subject.py catalog`.
