# CAD

**5** unique papers (5 copies across programmes) · 2007-08 to 2016-17 · 2 programmes · Sem 6, Trim 12

Download only this subject, sorted by academic year:

```powershell
python organize_by_subject.py restore --destination D:/Study --subject "CAD"
```

Files land in `D:/Study/PYQs_By_Subject/CAD/<academic year>/`. Identical copies of one paper (the portal often files the same PDF under several programmes) are placed once.

Text of the papers, ready for reading or AI analysis: [`papers.md`](papers.md) (every paper in full, newest first), [`questions.jsonl`](questions.jsonl) (one record per question with marks, year, exam, semester and department) and [`papers.jsonl`](papers.jsonl) (one record per paper). Answer keys, where the portal published them, are in `answer_keys.md`. See [`question_bank/README.md`](../../question_bank/README.md) for the fields.

| Year | Exam | Type | Sem | Programmes | File |
| --- | --- | --- | --- | --- | --- |
| 2016-17 | Final-Exam | Question paper | Sem 6 | MBA TECH / MECHANICAL | CAD,CAM.CIM 2016-2017 Final exam.pdf [1] |
| 2016-17 | Re-Exam | Question paper | Sem 6 | MBA TECH / MECHANICAL | CAD,CAM,CIM BATCH 2016-2017 Re-exam.pdf [2] |
| 2015-16 | Re-Exam | Question paper | Sem 6 | MBA TECH / MECHANICAL | CAD,CAM,CAE Batch 2015-16 Re Exam.pdf [3] |
| 2011 | — | Question paper | Trim 12 | MBA TECH / CHEMICAL | CAD,OPTIMIZATION & SIMUATION 2011.pdf |
| 2007-08 | — | Question paper | Trim 12 | MBA TECH / CHEMICAL | 2007-2008(134).pdf |

**Notes on papers placed here from a different folder**

1. filed under "CADCAMCIM" but the file name says "CAD"
2. filed under "CADCAMCIM" but the file name says "CAD"
3. filed under "CADCAMCIM" but the file name says "CAD"

Full original paths are in [`pyq_subject_index.csv`](../pyq_subject_index.csv). If a paper is in the wrong subject, add its spelling to `subject_aliases.json` and rerun `python organize_by_subject.py catalog`.
