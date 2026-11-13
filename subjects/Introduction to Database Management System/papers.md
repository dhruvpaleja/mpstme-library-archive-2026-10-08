# Introduction to Database Management System: question papers in full

6 unique papers · 2025-26 to 2025-26 · Computer Engineering, Computer Science, Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 4 · paper eb0d48e00c6e

- Departments: Computer Engineering
- Programmes: DIPLOMA IN COMPUTER ENGINEERING - 7073
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER ENGINEERING - 7073/Introduction to Database Management System/QP_Introduction to Database Management System(701CO0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Database Management System
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
9. Answer to each new question to be started on a fresh page
10. Figure in right hand side indicate full marks
Q1   Answer briefly   [20]
CO1;   a.   Differentiate between File System and DBMS   [5]
SO-1;
BL-2;
CO-2,   b.   Describe the following terms with examples: i) Weak Entity ii) [5]
SO-1   Multivalued Attributes
BL-2
CO-3;   c.   Explain the concept of normalization in Database Management Systems [5]
SO-1   and discuss the objectives of normalization.
BL- 2;
CO-4;   d.   What is constraint in SQL. Explain any two constraints with example.   [5]
SO-1 ;
BL- 3;
Q2   a   Discuss the three-schema architecture of DBMS and explain the role of [10]
CO-1;   each level.
SO-1;
BL-2;
CO2;S   b   Design an ER diagram for the given scenario and convert it into [10]
O-   relational tables.
1;BL-4;
A hospital plans to develop a database system to manage information
about   departments,   doctors,   and   patients.
Each department has a unique dept_ID, dept_name, and location. Every
department employs multiple doctors.
Each doctor has a unique doctor_ID, doctor_name,, expertise and phone
number. A doctor works in exactly one department.
********** 1 **********
--- page 2 ---
The hospital maintains records of all patients. For each patient, the
system stores patient_ID (unique), patient_name (f_name, l_name),
DOB, age, address, and multiple phone numbers.
Each patient is assigned to exactly one department, and a department
can have many patients. Patients can consult multiple doctors, and each
doctor can consult many patients.
The hospital also maintains information about each patient’s attendant.
For every attendant, the system stores A_Name, relation, phone, and
address. Each patient must have at least one attendant, and each
attendant is responsible for exactly one patient.
Tasks to be include in ER diagram:
1. Design the ER diagram with proper notation.
2. Identify   entities,   attributes (including multivalued and
composite), and relationships.
3. Specify cardinality and participation constraints.
Q3   a   a .Find all the candidate keys of a given relation.   [10]
CO-3;   R (A, B, C, D)
SO-1;   Functional Dependency (FD): {AB->CD, D->B, C->A}
BL-4;   b. Consider the following relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Projects)
EmpID EmpName   Projects
E101   Raj   AI, DBMS
E102   Simran   ML
E103   Karan   AI, ML, Cloud
Perform the given tasks:
a. Identify whether the given relation is in First Normal Form
(1NF). Justify your answer and write all rules of INF
b. Convert the given relation into 1NF.
c. Identify the primary key(s) in the normalized relation.
CO2;   b   Explain the different types of Outer Joins in SQL and write the [10]
SO-1;   corresponding SQL statement syntax.
BL-3;
Q4   a   What is Data model? Explain the Relational Data model with example. [10]
CO-3;
SO-11;
BL-2
********** 2 **********
--- page 3 ---
Q4   b   Explain the concept of database users? Give the roles and [10]
CO1;   responsibilities of a DBA.
SO-1;
BL-2;
Consider a relation R (A, B, C, D) with the following set of functional
dependencies:
FD: {A → B, B → C}
Answer the following:
Q5   1. Determine the highest normal form satisfied by the relation and
CO3;   justify your answer   [10]
SO-2;   a   2. Decompose given relation up to 2NF
BL-3;
CO4;   b   Differentiate between Data Definition Language (DDL) and Data [10]
SO-1;   Manipulation Language (DML) in SQL. Provide two commands from
BL-2;   each category along with their syntax.
Q6   a   Convert the given ER diagram into relational table and identify the [10]
CO-1,2;   relations, attributes primary and foreign keys.
SO-1;
BL-3;
CO-4;   b   Based on the following schema of the tables, write the SQL statements [10]
SO-2;   for the given queries.
BL-4;
Student (student_id, name, age, marks, dept_id)
Department (dept_id, dept_name
a) Display names of students whose names 2nd character is ‘a’
b) Find the department-wise average marks where average marks
are greater than 75.
c) Find students whose marks are between 70 and 90.
d) Display student names along with their department names.
e) Display all departments along with student names (include
departments with no students).
Q7   a   a) Consider the following two tables from a college database and [10]
CO,4;   perform the Natural join and Left outer join operation and show
SO-   the resultant table with count the records.
1;BL-3;
********** 3 **********
--- page 4 ---
Student   Department
SID   Name   DeptID   DeptID   DeptN HOD
ame
1   Asha   10
10   CS   Dr. Rao
2   Ravi   20
10   CS   Dr. Rao
3   Neha   10
Dr.
20   IT
4   Kiran   30   Mehta
5   Amit   NULL   40   EXTC   Dr. Shah
NULL   NA   NA
b) Define the term Data Redundancy and Data inconsistency.
CO5;   b   What is NoSQL, and how does it differ from traditional relational [10]
SO-1;   databases?
BL-2;
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 4 · paper 6ce9669e6d1d

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/Introduction to Database Management System/QP_Introduction to Database Management System(701CO0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Database Management System
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
9. Answer to each new question to be started on a fresh page
10. Figure in right hand side indicate full marks
Q1   Answer briefly   [20]
CO1;   a.   Differentiate between File System and DBMS   [5]
SO-1;
BL-2;
CO-2,   b.   Describe the following terms with examples: i) Weak Entity ii) [5]
SO-1   Multivalued Attributes
BL-2
CO-3;   c.   Explain the concept of normalization in Database Management Systems [5]
SO-1   and discuss the objectives of normalization.
BL- 2;
CO-4;   d.   What is constraint in SQL. Explain any two constraints with example.   [5]
SO-1 ;
BL- 3;
Q2   a   Discuss the three-schema architecture of DBMS and explain the role of [10]
CO-1;   each level.
SO-1;
BL-2;
CO2;S   b   Design an ER diagram for the given scenario and convert it into [10]
O-   relational tables.
1;BL-4;
A hospital plans to develop a database system to manage information
about   departments,   doctors,   and   patients.
Each department has a unique dept_ID, dept_name, and location. Every
department employs multiple doctors.
Each doctor has a unique doctor_ID, doctor_name,, expertise and phone
number. A doctor works in exactly one department.
********** 1 **********
--- page 2 ---
The hospital maintains records of all patients. For each patient, the
system stores patient_ID (unique), patient_name (f_name, l_name),
DOB, age, address, and multiple phone numbers.
Each patient is assigned to exactly one department, and a department
can have many patients. Patients can consult multiple doctors, and each
doctor can consult many patients.
The hospital also maintains information about each patient’s attendant.
For every attendant, the system stores A_Name, relation, phone, and
address. Each patient must have at least one attendant, and each
attendant is responsible for exactly one patient.
Tasks to be include in ER diagram:
1. Design the ER diagram with proper notation.
2. Identify   entities,   attributes (including multivalued and
composite), and relationships.
3. Specify cardinality and participation constraints.
Q3   a   a .Find all the candidate keys of a given relation.   [10]
CO-3;   R (A, B, C, D)
SO-1;   Functional Dependency (FD): {AB->CD, D->B, C->A}
BL-4;   b. Consider the following relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Projects)
EmpID EmpName   Projects
E101   Raj   AI, DBMS
E102   Simran   ML
E103   Karan   AI, ML, Cloud
Perform the given tasks:
a. Identify whether the given relation is in First Normal Form
(1NF). Justify your answer and write all rules of INF
b. Convert the given relation into 1NF.
c. Identify the primary key(s) in the normalized relation.
CO2;   b   Explain the different types of Outer Joins in SQL and write the [10]
SO-1;   corresponding SQL statement syntax.
BL-3;
Q4   a   What is Data model? Explain the Relational Data model with example. [10]
CO-3;
SO-11;
BL-2
********** 2 **********
--- page 3 ---
Q4   b   Explain the concept of database users? Give the roles and [10]
CO1;   responsibilities of a DBA.
SO-1;
BL-2;
Consider a relation R (A, B, C, D) with the following set of functional
dependencies:
FD: {A → B, B → C}
Answer the following:
Q5   1. Determine the highest normal form satisfied by the relation and
CO3;   justify your answer   [10]
SO-2;   a   2. Decompose given relation up to 2NF
BL-3;
CO4;   b   Differentiate between Data Definition Language (DDL) and Data [10]
SO-1;   Manipulation Language (DML) in SQL. Provide two commands from
BL-2;   each category along with their syntax.
Q6   a   Convert the given ER diagram into relational table and identify the [10]
CO-1,2;   relations, attributes primary and foreign keys.
SO-1;
BL-3;
CO-4;   b   Based on the following schema of the tables, write the SQL statements [10]
SO-2;   for the given queries.
BL-4;
Student (student_id, name, age, marks, dept_id)
Department (dept_id, dept_name
a) Display names of students whose names 2nd character is ‘a’
b) Find the department-wise average marks where average marks
are greater than 75.
c) Find students whose marks are between 70 and 90.
d) Display student names along with their department names.
e) Display all departments along with student names (include
departments with no students).
Q7   a   a) Consider the following two tables from a college database and [10]
CO,4;   perform the Natural join and Left outer join operation and show
SO-   the resultant table with count the records.
1;BL-3;
********** 3 **********
--- page 4 ---
Student   Department
SID   Name   DeptID   DeptID   DeptN HOD
ame
1   Asha   10
10   CS   Dr. Rao
2   Ravi   20
10   CS   Dr. Rao
3   Neha   10
Dr.
20   IT
4   Kiran   30   Mehta
5   Amit   NULL   40   EXTC   Dr. Shah
NULL   NA   NA
b) Define the term Data Redundancy and Data inconsistency.
CO5;   b   What is NoSQL, and how does it differ from traditional relational [10]
SO-1;   databases?
BL-2;
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 4 · paper efa47863d23e

- Departments: Information Technology
- Programmes: DIPLOMA IN INFORMATION TECHNOLOGY - 7075
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN INFORMATION TECHNOLOGY - 7075/Introduction to Database Management System/QP_Introduction to Database Management System(701CO0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Database Management System
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
9. Answer to each new question to be started on a fresh page
10. Figure in right hand side indicate full marks
Q1   Answer briefly   [20]
CO1;   a.   Differentiate between File System and DBMS   [5]
SO-1;
BL-2;
CO-2,   b.   Describe the following terms with examples: i) Weak Entity ii) [5]
SO-1   Multivalued Attributes
BL-2
CO-3;   c.   Explain the concept of normalization in Database Management Systems [5]
SO-1   and discuss the objectives of normalization.
BL- 2;
CO-4;   d.   What is constraint in SQL. Explain any two constraints with example.   [5]
SO-1 ;
BL- 3;
Q2   a   Discuss the three-schema architecture of DBMS and explain the role of [10]
CO-1;   each level.
SO-1;
BL-2;
CO2;S   b   Design an ER diagram for the given scenario and convert it into [10]
O-   relational tables.
1;BL-4;
A hospital plans to develop a database system to manage information
about   departments,   doctors,   and   patients.
Each department has a unique dept_ID, dept_name, and location. Every
department employs multiple doctors.
Each doctor has a unique doctor_ID, doctor_name,, expertise and phone
number. A doctor works in exactly one department.
********** 1 **********
--- page 2 ---
The hospital maintains records of all patients. For each patient, the
system stores patient_ID (unique), patient_name (f_name, l_name),
DOB, age, address, and multiple phone numbers.
Each patient is assigned to exactly one department, and a department
can have many patients. Patients can consult multiple doctors, and each
doctor can consult many patients.
The hospital also maintains information about each patient’s attendant.
For every attendant, the system stores A_Name, relation, phone, and
address. Each patient must have at least one attendant, and each
attendant is responsible for exactly one patient.
Tasks to be include in ER diagram:
1. Design the ER diagram with proper notation.
2. Identify   entities,   attributes (including multivalued and
composite), and relationships.
3. Specify cardinality and participation constraints.
Q3   a   a .Find all the candidate keys of a given relation.   [10]
CO-3;   R (A, B, C, D)
SO-1;   Functional Dependency (FD): {AB->CD, D->B, C->A}
BL-4;   b. Consider the following relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Projects)
EmpID EmpName   Projects
E101   Raj   AI, DBMS
E102   Simran   ML
E103   Karan   AI, ML, Cloud
Perform the given tasks:
a. Identify whether the given relation is in First Normal Form
(1NF). Justify your answer and write all rules of INF
b. Convert the given relation into 1NF.
c. Identify the primary key(s) in the normalized relation.
CO2;   b   Explain the different types of Outer Joins in SQL and write the [10]
SO-1;   corresponding SQL statement syntax.
BL-3;
Q4   a   What is Data model? Explain the Relational Data model with example. [10]
CO-3;
SO-11;
BL-2
********** 2 **********
--- page 3 ---
Q4   b   Explain the concept of database users? Give the roles and [10]
CO1;   responsibilities of a DBA.
SO-1;
BL-2;
Consider a relation R (A, B, C, D) with the following set of functional
dependencies:
FD: {A → B, B → C}
Answer the following:
Q5   1. Determine the highest normal form satisfied by the relation and
CO3;   justify your answer   [10]
SO-2;   a   2. Decompose given relation up to 2NF
BL-3;
CO4;   b   Differentiate between Data Definition Language (DDL) and Data [10]
SO-1;   Manipulation Language (DML) in SQL. Provide two commands from
BL-2;   each category along with their syntax.
Q6   a   Convert the given ER diagram into relational table and identify the [10]
CO-1,2;   relations, attributes primary and foreign keys.
SO-1;
BL-3;
CO-4;   b   Based on the following schema of the tables, write the SQL statements [10]
SO-2;   for the given queries.
BL-4;
Student (student_id, name, age, marks, dept_id)
Department (dept_id, dept_name
a) Display names of students whose names 2nd character is ‘a’
b) Find the department-wise average marks where average marks
are greater than 75.
c) Find students whose marks are between 70 and 90.
d) Display student names along with their department names.
e) Display all departments along with student names (include
departments with no students).
Q7   a   a) Consider the following two tables from a college database and [10]
CO,4;   perform the Natural join and Left outer join operation and show
SO-   the resultant table with count the records.
1;BL-3;
********** 3 **********
--- page 4 ---
Student   Department
SID   Name   DeptID   DeptID   DeptN HOD
ame
1   Asha   10
10   CS   Dr. Rao
2   Ravi   20
10   CS   Dr. Rao
3   Neha   10
Dr.
20   IT
4   Kiran   30   Mehta
5   Amit   NULL   40   EXTC   Dr. Shah
NULL   NA   NA
b) Define the term Data Redundancy and Data inconsistency.
CO5;   b   What is NoSQL, and how does it differ from traditional relational [10]
SO-1;   databases?
BL-2;
********** 4 **********
````
