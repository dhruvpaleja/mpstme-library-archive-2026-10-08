# Advanced Databases

**1** unique papers (1 copies across programmes) · 2017-18 · 1 programme · Sem 1

Download only this subject, sorted by academic year:

```powershell
python organize_by_subject.py restore --destination D:/Study --subject "Advanced Databases"
```

Files land in `D:/Study/PYQs_By_Subject/Advanced Databases/<academic year>/`. Identical copies of one paper (the portal often files the same PDF under several programmes) are placed once.

Text of the papers, ready for reading or AI analysis: [`papers.md`](papers.md) (every paper in full, newest first), [`questions.jsonl`](questions.jsonl) (one record per question with marks, year, exam, semester and department) and [`papers.jsonl`](papers.jsonl) (one record per paper). Answer keys, where the portal published them, are in `answer_keys.md`. See [`question_bank/README.md`](../../question_bank/README.md) for the fields.

| Year | Exam | Type | Sem | Programmes | File |
| --- | --- | --- | --- | --- | --- |
| 2017-18 | — | Question paper | Sem 1 | M TECH / COMPUTER | Adavnces Database 2017-2018.pdf |

Full original paths are in [`pyq_subject_index.csv`](../pyq_subject_index.csv). If a paper is in the wrong subject, add its spelling to `subject_aliases.json` and rerun `python organize_by_subject.py catalog`.
