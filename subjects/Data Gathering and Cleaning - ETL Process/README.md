# Data Gathering and Cleaning - ETL Process

**1** unique papers (2 copies across programmes) · year not stated · 1 programme · Sem 3

Download only this subject, sorted by academic year:

```powershell
python organize_by_subject.py restore --destination D:/Study --subject "Data Gathering and Cleaning - ETL Process"
```

Files land in `D:/Study/PYQs_By_Subject/Data Gathering and Cleaning - ETL Process/<academic year>/`. Identical copies of one paper (the portal often files the same PDF under several programmes) are placed once.

| Year | Exam | Type | Sem | Programmes | File |
| --- | --- | --- | --- | --- | --- |
| — | Final-Exam | Question paper | Sem 3 | B TECH / DATA SCIENCE | DATA GATHERING AND CLEANING ETL PROCESS (DATA SCIENCE) FINAL EXAM.pdf |

Full original paths are in [`pyq_subject_index.csv`](../pyq_subject_index.csv). If a paper is in the wrong subject, add its spelling to `subject_aliases.json` and rerun `python organize_by_subject.py catalog`.
