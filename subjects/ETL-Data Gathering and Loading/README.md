# ETL-Data Gathering and Loading

**7** unique papers (7 copies across programmes) · 2024-25 · 4 programmes · Sem 10

Download only this subject, sorted by academic year:

```powershell
python organize_by_subject.py restore --destination D:/Study --subject "ETL-Data Gathering and Loading"
```

Files land in `D:/Study/PYQs_By_Subject/ETL-Data Gathering and Loading/<academic year>/`. Identical copies of one paper (the portal often files the same PDF under several programmes) are placed once.

Text of the papers, ready for reading or AI analysis: [`papers.md`](papers.md) (every paper in full, newest first), [`questions.jsonl`](questions.jsonl) (one record per question with marks, year, exam, semester and department) and [`papers.jsonl`](papers.jsonl) (one record per paper). Answer keys, where the portal published them, are in `answer_keys.md`. See [`question_bank/README.md`](../../question_bank/README.md) for the fields.

Also filed as: `ETL- Data Gathering and Loading`

| Year | Exam | Type | Sem | Programmes | File |
| --- | --- | --- | --- | --- | --- |
| 2024-25 | Final-Exam | Question paper | Sem 10 | MBATech (MECHANICAL ENGINEERING) - 7046 | QP_ETL-Data Gathering and Loading(703TM0E021)_2024-2025.pdf |
| 2024-25 | Final-Exam | Question paper | Sem 10 | MBATech Computer 7047 | QP_ETL-Data Gathering and Loading(703TM0E021)_2024-2025.pdf |
| 2024-25 | Final-Exam | Question paper | Sem 10 | MBATech IT 7041 | QP_ETL-Data Gathering and Loading(703TM0E021)_2024-2025.pdf |
| 2024-25 | Final-Exam | Answer key | Sem 10 | MBATech (MECHANICAL ENGINEERING) - 7046 | ANS_ETL-Data Gathering and Loading(703TM0E021)_2024-2025.pdf |
| 2024-25 | Final-Exam | Answer key | Sem 10 | MBATech Computer 7047 | ANS_ETL-Data Gathering and Loading(703TM0E021)_2024-2025.pdf |
| 2024-25 | Final-Exam | Answer key | Sem 10 | MBATech IT 7041 | ANS_ETL-Data Gathering and Loading(703TM0E021)_2024-2025.pdf |
| — | — | Question paper | Sem 10 | MBA TECH | ETL-Data Gathering and Loading.pdf |

Full original paths are in [`pyq_subject_index.csv`](../pyq_subject_index.csv). If a paper is in the wrong subject, add its spelling to `subject_aliases.json` and rerun `python organize_by_subject.py catalog`.
