# Database System Essentials: question papers in full

10 unique papers · 2023-24 to 2025-26 · Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 6 · paper 5a37ac29a662

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/Integrated_IT_7037/Database System Essentials/QP_Database System Essentials(701IT0C010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Database System Essentials
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No.1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
CO-1 ; SO-2 ;   a. Discuss different types of database users and how each interacts with
[5]
BL-2   the database system.
b. Consider a table EMPLOYEE(EmpID, Name, Email, Phone,
AadharNo).
CO-3 ; SO-2 ;
(a) Identify possible superkeys.   [5]
BL-2
(b) Determine the candidate keys.
(c) Choose an appropriate primary key and justify your choice.
CO-1 ; SO-2 ;   c.   Identify and explain five practical applications of database systems in
[5]
BL-2   different domains.
CO-3; SO-2 ;   d. Explain the 3 Set Operators in Relational algebra with one example
[5]
BL-2   each
Q2   a
What are Constraints in SQL? Explain Primary key, foreign key, Check
CO-3-; SO-2;   [10]
and Unique constraint with example and syntax.
BL-2
b. Draw an E-R Diagram for the problem statement: Problem Statement:
A university offers multiple programs (e.g., B.Tech IT, B.Tech CS).
Each program has a unique Program_ID, name, and duration. Each
program consists of several courses; each course has a Course_Code,
Q2
Course_Name, and credits. A course may be taught by one or more
CO-2; SO-2;   [10]
instructors; each instructor has an Instructor_ID, name, designation,
BL-3
and email. Students enroll in one program and are identified by
Student_ID, name, email, and year_of_admission. Students can
register for multiple courses each semester, and for each registration,
the system stores semester, academic_year, and grade.
a.
Q3   What   is data independence? Explain the two types of data
CO-2; SO-2;   independence. Draw and explain the 3 level architecture to achieve data [10]
BL-2   abstraction
b. Write the Relational Algebra Queries for the below
Q3
employee (eid, name, city)
CO-3; SO-2;   [10]
works (eid, cid, salary)
BL-3
company (cid, cname, location)
********** 1 **********
--- page 2 ---
manager (mid, mname)
1.Find the names of all companies
2.Find the employee IDs who are not working in any company
3.Find the names of employees along with the companies they work
for
4.Find the names of employees who have salary greater than 50000
5.Find the names of companies that have at least one employee
working
Q4   a.
State the importance of Data models. Explain the relational model and
CO-2; SO-2;   [10]
the Hierarchical Model with diagrams .
BL-2
b.
Q4
CO-1; SO-2;   [5]
BL-3
Design the schema for the given ER Model.
c. Explain with syntax and example the following relational algebra
operators
Q4   a. Select
CO-2; SO-2;   b. Natural Join   [5]
BL-2   c. Cartesian Product
d. Project
e. Rename
Q5   a.
Explain Parallel Database Architecture. What is shared Memory
CO-1; SO-2;   [10]
Architecture
BL-2
Q5   b.
What are views in SQL. Write the syntax to create a view with the help
CO-3; SO-2;   [5]
of an example
BL-2
Q5   c.
Compare Tuple Relational Calculus and Domain Relational Calculus.
CO-3; SO-2;   [5]
Give one example queries of each
BL-3
a. Write SQL queries for the given database:
Q6
Student (sid, sname, city)
CO-3; SO-2;   [10]
Enroll (sid, course_id, marks)
BL-3
Course (course_id, course_name, department)
********** 2 **********
--- page 3 ---
i) Give all students enrolled in ‘Data Science’ course a 5% increase in
marks.
ii) Find the total number of students.
iii) Find the student with highest marks.
iv) Find the average marks of students in each course.
v) List the names of students who are not enrolled in any course.
Q6   b. Describe Indexing and Hashing techniques used for data retrieval in
CO-1; SO-2;   databases. Explain different types of indexing and hashing, and state   [10]
BL-2   their advantages and limitations.
a. Online Shopping Database Schema
• customer (cust_id, cust_name, city)
•   orders (order_id, cust_id, product_id)
• product (product_id, product_name, category, supplier_id)
•   supplier (supplier_id, supplier_name)
Constraints:
•   cust_id in orders → FK referencing customer
• product_id in orders → FK referencing product
•   supplier_id in product → FK referencing supplier
customer   Supplier
Q7
CO-3; SO-2;   [10]
BL-3
Product   orders
Questions
i.   How many tuples (rows) will be returned by:
ii.   What is the result of:
iii.   How many tuples are returned by:
********** 3 **********
--- page 4 ---
iv.   Write a relational algebra expression to find names of
suppliers whose products are ordered.
v.   Write a relational algebra expression to find names of
customers who ordered products in ‘Electronics’ category
b. Consider the following EMPLOYEE table description and assume
relevant data is populated.
Employee (employee_id, first_name, last_name, email,
phone_number, hire_date, job_id, salary, commission_pct,
manager_id, department_id)
Write SQL queries to get the respective outputs:
Q7   1. Show all details of employees who are working as Managers and
CO-3; SO-2;   were hired after the year 2015.   [10]
BL-3   2. Display the first name, last name, job_id, and salary of employees
whose salary is greater than 50000. Sort the result in ascending
order of salary.
3. Count the number of employees working in department with ID
30.
4. List the employee names whose salary is between 20000 and
60000.
5. Find the total salary paid to employees in department 10.
********** 4 **********
````

## 2025-26 · Re-Exam · paper 0de4d54a147a

- Departments: Information Technology
- Programmes: B.TECH INTEGRATED / IT
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/3rd YEAR/IT/Database System Essentials/Database System Essentials Batch 2024-25,2025-26 Re Exam.pdf`
- Printed on paper: max marks: 100; exam date: 06 July 2026
- Text: ocr (5 pages), mean OCR confidence 85.2

````text
"Date : 06 July 2026

ai

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING
Academic Year: 2025-26

Program: B Tech Intg (IT)

Subject: Database System Essentials

Marks: 100

Re-Exam (2024-25/2025-26)

Instructions:

1. This question paper contains 4 pages.

2. Question No.1 is compulsory

3. Out of remaining questions, attempt any 4 questions.

4. In all 5 questions to be attempted.

5. All questions carry equal marks.

6. Answer to each new question to be started on a fresh page.

7. Figures in brackets on the right-hand side indicate full marks.
8. Assume suitable data if necessary.

Qi Answer briefly: .

CO-1 ;SO-2; | a.

BL-2 Explain the concept of DBMS and the purpose of using DBMS [5]
CO-3 ; SO-2; | b. | Explain Logical data independence and physical data independence. [5]
BL-2 also explain what are instances and schemas _j
CO-1;SO-2; | c. | Explain five real-world applications where database systems are
[5]
BL-2 used.
d. | Explain with Symbol and example the following relational algebra
operators
; , a. Union
CAs; BG? ; b. Cartesian product {5]
BL-2
c. Intersect
d. Project
e. Minus

a | Consider the following STUDENT table description and assume relevant «
data is populated:
Student(student_id, first_name, last_name, email, phone_number,
admission_date, course_id, marks, scholarship_pct, mentor_id,

a department_id)
WriteSQL queries to get the respective outputs:
Q2 1. Show all details of students who are enrolled in course 'CS101'
CO-3-; SO-2; and were admitted after the year 2020. [10]
BL-2 2. Display the first name, last name, course_id, and marks of
i students whose marks are greater than 75. Sort the result in
descending order of marks.

3. Count the number of students studying in department with ID 20.

4. List the student names whose marks are between 60 and 90.

5. Find the total marks obtain’ed by students in department 10.
Q2 b.
CO-2; SO-2; + Explain the network model and the Object Oriented Model. [10]
BL-3

RRR RRA PORK RRR REE

ay
--- page 2 ---
a.

Draw and clearly specify entity sets, attributes, relationships, and
cardinalities. A hospital maintains data about its doctors, patients, and
appointments. Each doctor has a unique Doctor_ID, a name, e

specialization, and consultation fee. Patients have a unique Patient_ID,

(c) Choose the most appropriate Primary Key and justify your choice

Q3 name, age, address, and contact number. A patient can book multiple
CO-2; SO-2; appointments with different doctors, and each appointment has a [10]
BL-2 unique Appointment_ID, along with date, time, and status (confirmed,
cancelled, completed). Each doctor may attend to multiple patients
over time. The hospital also keeps records of departments — each
department has a Dept_ID and Dept_Name, and every doctor belongs
|_| to exactly one department. _
b. student (sid, name, city)
enroll (sid, course_id, marks)
course (course_id, course_name, faculty_id)
faculty (faculty_id, faculty name)
Write the Relational Algebra Queries for the below
Q3 |. Find the names of all courses offered.
CO-3: 50-2: 2. Find the student IDs who are not enrolled in any course. [10]
BL > 3. Find the names of students along with the courses they are
enrolled in.
4. Find the names of students who have scored more than 80
marks. . cr~
5. Find the names of faculty who are teaching at least one
course. :
Q4 La . ; . .
CO-2: SO-2: What are the 3 levels of data abstraction? Also explain how it helps in [10]
BL-2 achieving Data naan
» eat) Cine)
\
Awarded
Q4 oe
CO-1; SO-2; ae P Galery) [5]
BL-3 “Acted In> Movie |
/ NO | \,
GRID) Chal) C0 yam) eat) Cat 4
Design the schema for the given ER Model
a 2: SQ-2e/ Explain about Tuple relational calculus and Domain relational =
aeer A Calculus. Give one example queries of each [5]
BL-2 ple querie
Q5 a. ' _ . . .
CO-1- SO-2: Explain the differences between 2-tier and 3-tier database architectures [10]
BL-2 , based on structure, usage, ayd advantages.
b. | Consider a table STUDENT(RollNo, Name, Email, Phone, AadhaarNo,
Q5 Dept).
O-3; sh.2; (a) Identify all possible Super Keys. [5]
BL-2 (b) Determine the Candidate Keys.

FOR 0 Fr

ay
--- page 3 ---
=

Explain with syntax the following relational algebra operators

c.
Qs a. Natural Join
CO-3: SO-2: b. Union . 15]
BL3 & Intersect .
d. Project
e. Minus _ ; —
Q6 a. | Differentiate between table and view.
CO-3; SO-2; Also explain the following five string functions in SQL [10]
BL-3 i.lenght ii. Concat iti upper iv Ipad v substr
Q6 b. | What is a Tablespace and why is it important? Explain the concepts of
CO-1; SO-2; Segments, Extents, and Data Blocks with respect to database storage {10]
BL-2 structure.
a. | Library Database Schemw is as below
« member (member_id, first_name, last_name)
¢ borrow (member_id, book_id, issue_date)
¢ book (book_id, title, category, author_id)
e author (author_id, author_name)
Constraints:
« member_id in borrow — FK referencing member
e book_id in borrow — FK referencing book
¢ author_id in book — FK referencing author
member author
member idjfirst_namelast_name| |author_idjauthor name
1 Amit Shah * | {1 Chetan Bhagat
- — =e 2 J.K. Rowling
3 Riva Mehta ™ =
4 Karan Singh 3 Dan Brown
5 Priva Tait 4 Paulo Coelho
Q7
CO-3; SO-2; book borrow [10]
BL-3 book id title category |author id| |member_id|book_idjissue_date
1 Five Point SomeongFiction 1 L 1 2023-01-1
2, Harry Potter Fantasy [2 2 2 2023-02-13)
3 [Da Vinci Code Thriller [3 B3 3 2023-03-21
4 [Alchemist Philosophy|4 1 4 2023-04-05}
5 + |Half Girlfriend Fiction 1 By 5 2023-05-01
Questions ;
F is How many tuples will be returned by:

mw title(book)

i. What is the result of:
Tt member_id(member) - m member_id(borrow)

iii. How many tuples are returned by:
member 1 member.member_id = borrow.member_id borrow

iv. Write a relational algebra expression to find names of
authors whose books are borrowed.
va v. Write a relational algebra expression to find names
of members who have borrowed books in ‘Fiction’
category

FO OR 2 HR Rr
.

iy
--- page 4 ---
a. | Draw and clearly specify entity sets, attributes, relationships, and

cardinalities. A hospital maintains data about its doctors, patients, and F

appointments. Each doctor has a unique Doctor_ID, a name, * [

specialization, and consultation fee. Patients have a unique Patient_ ID, as
Q3 name, age, address, and contact number. A patient can book multiple EE
CO-2; SO-2; appointments with different doctors, and each appointment has a [10] =
BL-2 unique Appointment_ID, along with date, time, and status (confirmed,

cancelled, completed). Each doctor may attend to multiple patients
over time. The hospital also keeps records of departments — each
department has a Dept_ID and Dept_Name, and every doctor belongs
to exactly one department. z

b. student (sid, name, city)
enroll (sid, course_id, marks)
course (course_id, course_name, faculty_id)
faculty (faculty_id, faculty_name)
Write the Relational Algebra Queries for the below

Q3 1. Find the names of all courses offered. t
5 : . 2. Find the student IDs who are not enrolled in any course.
CO-3; SO-2; . . [10]
BL3 3. Find the names of students along with the courses they are
enrolled in. S
4. Find the names of students who have scored more than 80 i
marks. . ih
5. Find the names of faculty who are teaching at least one
course. :
Q4 a. : , : . . .
- ; What are the 3 levels of data abstraction? Also explain how it helps in
CO-2; SO-2; achievine Data ind 4 [10]
BL-2 chieving Data independence i
a
sAwarded
Q4 aw,
CO-1; SO-2; “e Galary) ? [5]
aes a
f SOS a I \
— _—_~
Gad Cao) CPO as) Cia Gating) a
<Directed —
Fl ae
Design the schema for the given ER Model
oF : Wy “ Explain about Tuple relational calculus and Domain relational bem
CO-2; SO-2;/ ; : [5]
BL-2 ¥ Calculus. Give one example queries of each
wa : . a Explain the differences between 2-tier and 3-tier database architectures l _
CO-1; SO-2; = ee [10] ie
BL-2 based on structure, usage, ang advantages. =
b. | Consider a table STUDENT(RollNo, Name, Email, Phone, AadhaarNo, 7
Dept).
0-3; sof; (a) Identify all possible Super Keys. [5]
BL-2 (b) Determine the Candidate Keys.

(c) Choose the most appropriate Primary Key and justify your choice

RRR RAR ARE DK KK

ey
--- page 5 ---
Write SQL queries for the given database:
Patient (pid, pname, city)

Treatment (pid, did, cost) e

Doctor (did, dname, specialization, city) ae
Q7 i) Increase the treatment cost by 15% for patients treated by doctors’
CO-3; SO-2;. with specialization ‘Cardiology’. [10]
BL-3 ii) List the names of patients who have not undergone any treatment,

ili) Find the total number of patients.
iv) Find the patient with the highest treatment cost.
v) Find the average treatment cost for each doctor.

L

i

FR RK RK
````

## 2024-25 · Final + Re-Exam · paper eb1b20c97822

- Departments: Information Technology
- Programmes: B.TECH INTEGRATED / IT
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/3rd YEAR/IT/Database System Essentials/Database System Essentials Batch 2024-25 Final Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 May 2025
- Text: ocr (3 pages), mean OCR confidence 86.6

````text
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLO

Subject: Database
Date: 10 May 2025
Max. Marks: 100

Instructions:

SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

YEARS INTEGRATED PROGRAM »
Year: IlI/Semester VI(Exam Year: 2024-2025) -
System Essentials

Time: 02:00 pm to 05:00 pm (03:00 Hrs.)

FINAL EXAMINATION (Acad. Year:2024-2025)
RE EXAMINATION (Acad: Year: 202.3 - 2.094)

1. This question paper contains 3 pages.

2. Question No.1

is compulsory.

3. Out of remaining questions, attempt any 4 questions.

4. In all 5 questio:
5. All questions c:

ns to be attempted.
arry equal marks.

6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.

8. Assume suitabl

e data if necessary.

Ql

Answer briefly:

re

CO-1 ; SO-2; | a.
BL-2

Distinguish between 2-tier and 3-tier client-server architecture [5]

CO-3 : SO-2: b. | Illustrate the natural join operator in Relational algebra. Also explain [5]
BL-2 left join, right join and full join with symbols
os 380-2; |. Explain any five string functions in SQL [5]
. . | 4d. |For any Database applications, explain the advantages of database
CO-1; SO-2 ; [5]
BL-2 system over file processing system.
- ® | What are Data Models. Explain the Relational model and the Object
CO-2-; SO-2; . - a [10]
BL-2 Oriented Model.
Q2 b . : ro
Explain DDL, DML, DCL and DTL commands in SQL. Explain with
CO-3; SO-2; . . . [10]
BL3 syntax and example foreign key, unique and check constraint
Q3 a .
Describe parallel database architecture. Explain about Shared Memory
CO-1; SO-2; : : [10]
oe Architecture, Shared Disk Architecture , Shared Nothing Architecture
b | A library manages books, members, and staff. Each book has a unique
Q3 ISBN, and members can borrow multiple books. The system should
CO-1: SO-2: track book availability, due dates, fines, and book reservations. For the [5]
BL , ; given application, design a relational database schema for this

application, specifying tables, attributes, and primary/foreign keys.

FORO RIGCR | RR
--- page 2 ---
c | For the Given ER:model below, give the respective relational model
<a> <D) .
Citiveri>) ‘oe
Q3 -
CO-3; SO-2;
O-3; SO-2; reporter >/ [5]
BL-3
a | A Car Insurance Company whose customer s owns one or more cars
Q4 each. Each car has associated with it zero or any number of recorded
CO2-; SO-2; accidents. [10]
BL-3 1. Develop an ER diagram for the above case study
2. Convert to relational Schema
Q4 b
CO-3; SO-2; What are views? Explain with syntax creation and updating of views. | [5]
BL-2
Q4 c
CO-1; SO-2; Describe the transaction servers in DBMS. [5]
BL-2
a | Consider below relational schema and formulate SQL queries for the
following: : ’
Employee (eid,ename, street, city)
Works (eid, cid, salary)
Q5 Company (cid, cname,city)
i) Modify the database so that Jack now lives in ‘Mumbai’
CO-3; SO-2; ii) Give all employees of ‘ANZ corporation ‘ a 10% raise [10]
BL-3 - ~ in salary. : - - _ = =
iii) Find all employee id who live in same cities as the
company for which they work.
iv) Give total number of employees.
v) Find the highest paid employee.
Q5 b . . oo,
Discuss about Indexing and Hashing in DBMS. What are Data
CO-1; SO-2; a Lo. . [10]
Dictionary and Dictionary Views?
BL-2
a | Classify the 4 categories of SQL commands. Also illustrate with syntax
Q6 and example the following command.
CO-3; SO-2; 1. create [10]
BL-3 2. Alter
3. Update

GK ka Re
--- page 3 ---
4. Delete

What are Degrees of data abstraction in DBMS. With respect to ER

Q6
CO-2; SO-2; model explain strong entity set, weak entity set, total and partial* [10]
BL-2 participation
Q7 Differentiate between logical and physical data independence. Also
CO-3; SO-2; . Le, . [10]
BL3 explain any 5 aggregate functions in SQL.
Book( book_id, title,author, cost)
Store(store_no, city, state, inventory_val)
Stock(store_no, book_id,quantity)
Consider above relational schema and formulate relational algebra
Q7 queries for the following(Assume values as per requirement) :
CO-3; SO-2; (i)Modify the cost of DBMS books by 10% [10]
BL-3 (ii)Find the author of the books which are available in Mumbai store

re

(iii)Find the title of the most expensive book

(iv) Find the titles of all books available in stores located in Maharashtra.

(v) Add a new record in Book

FoR 2 RAR RR Re
````

## 2024-25 · Final-Exam · Sem 6 · paper cd4c6027715f

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/Integrated_IT_7037/Database System Essentials/QP_Database System Essentials(701IT0C010)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 May 2025
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Database System Essentials
Date: 10 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 3 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
CO-1 ; SO-2 ;   a. Distinguish between 2-tier and 3-tier client-server architecture   [5]
BL-2
b.   Illustrate the natural join operator in Relational algebra. Also explain
CO-3 ; SO-2 ;   [5]
BL-2   left join, right join and full join with symbols
CO-3 ; SO-2 ;   c. Explain any five string functions in SQL   [5]
BL-2
d. For any Database applications, explain the advantages of database
CO-1; SO-2 ;   [5]
BL-2   system over file processing system.
Q2   a
What are Data Models. Explain the Relational model and the Object
CO-2-; SO-2;   [10]
Oriented Model.
BL-2
Q2   b
Explain DDL, DML, DCL and DTL commands in SQL. Explain with
CO-3; SO-2;   [10]
syntax and example foreign key, unique and check constraint
BL-3
Q3   a
Describe parallel database architecture. Explain about Shared Memory
CO-1; SO-2;   [10]
Architecture, Shared Disk Architecture , Shared Nothing Architecture
BL-2
b A library manages books, members, and staff. Each book has a unique
Q3   ISBN, and members can borrow multiple books. The system should
CO-1; SO-2;   track book availability, due dates, fines, and book reservations. For the [5]
given application, design a relational database schema for this
BL-2   application, specifying tables, attributes, and primary/foreign keys.
********** 1 **********
--- page 2 ---
c   For the Given ER model below, give the respective relational model
Q3
CO-3; SO-2;   [5]
BL-3
a A Car Insurance Company whose customer s owns one or more cars
Q4   each. Each car has associated with it zero or any number of recorded
CO2-; SO-2;   accidents.   [10]
BL-3   1. Develop an ER diagram for the above case study
2. Convert to relational Schema
Q4   b
CO-3; SO-2;   What are views? Explain with syntax creation and updating of views.   [5]
BL-2
Q4   c
CO-1; SO-2;   Describe the transaction servers in DBMS.   [5]
BL-2
a   Consider below relational schema and formulate SQL queries for the
following:
Employee (eid,ename,street,city)
Works (eid, cid, salary)
Company (cid, cname,city)
Q5
i)   Modify the database so that Jack now lives in ‘Mumbai’
CO-3; SO-2;   ii)   Give all employees of ‘ANZ corporation ‘ a 10% raise   [10]
BL-3   in salary.
iii)   Find all employee id who live in same cities as the
company for which they work.
iv)   Give total number of employees.
v)   Find the highest paid employee.
Q5   b
Discuss about Indexing and Hashing in DBMS. What are Data
CO-1; SO-2;   [10]
Dictionary and Dictionary Views?
BL-2
a   Classify the 4 categories of SQL commands. Also illustrate with syntax
Q6   and example the following command.
CO-3; SO-2;   1. create   [10]
BL-3   2. Alter
3. Update
********** 2 **********
--- page 3 ---
4. Delete
Q6   b What are Degrees of data abstraction in DBMS. With respect to ER
CO-2; SO-2;   model explain strong entity set, weak entity set, total and partial [10]
BL-2   participation
Q7   a
Differentiate between logical and physical data independence. Also
CO-3; SO-2;   [10]
explain any 5 aggregate functions in SQL.
BL-3
b   Book( book_id, title,author, cost)
Store(store_no, city, state, inventory_val)
Stock(store_no, book_id,quantity)
Consider above relational schema and formulate relational algebra
Q7   queries for the following(Assume values as per requirement) :
CO-3; SO-2;   (i)Modify the cost of DBMS books by 10%   [10]
BL-3
(ii)Find the author of the books which are available in Mumbai store
(iii)Find the title of the most expensive book
(iv) Find the titles of all books available in stores located in Maharashtra.
(v) Add a new record in Book
********** 3 **********
````

## 2024-25 · Re-Exam · Sem 6 · paper b6c45c8be438

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/Integrated_IT_7037/Database System Essentials/QP_Database System Essentials(701IT0C010)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Jul 2025
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Database System Essentials
Date: 07 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 3 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
CO-1 ; SO-2 ;   a. Explain the cloud based servers in DBMS   [5]
BL-2
b.   Illustrate the following relational algebra operators
a. Project,
CO-3 ; SO-2 ;   b. Natural Join   [5]
BL-2   c. Union
d. Intersect
e. Rename
CO-3 ; SO-2 ;   c. Explain any five aggregate functions in SQL   [5]
BL-2
CO-1; SO-2 ;   d. Summarize any 5 database applications.   [5]
BL-2
Q2   a
Discuss the importance of Data Models. Explain the Hierarchical model
CO-2-; SO-2;   [10]
and the Network Model.
BL-2
Q2   b What are constraints in SQL. Explain with syntax and example
[10]
CO-3; SO-2;   primary key, foreign key, not null and check constraint
BL-3
Q3   a
Describe with help of a neat diagram the complete database system
CO-1; SO-2;   [10]
architecture.
BL-2
b A university course registration system allows students to register for
Q3   courses at the beginning of each semester. The system maintains
CO-1; SO-2;   records of students, courses, instructors, and enrollments. Students can [5]
BL-2   register for multiple courses, but each course has a maximum capacity.
The system should prevent overbooking and ensure that each student
********** 1 **********
--- page 2 ---
meets the prerequisites before enrollment. Design a relational database
schema for this application, specifying tables, attributes, and
primary/foreign keys.
Q3   c
Compare Tuple relational calculus and relational algebra. Also give an
CO-3; SO-2;   [5]
example query of each.
BL-3
a A   hospital   includes   patients,   doctors,   nurses,   departments,
Q4   appointments, and billing. Each patient is assigned a unique patient ID
and may have multiple appointments with different doctors. The system [10]
CO2-; SO-2;
should also track prescribed medications and treatments.
BL-3
1. Develop an ER diagram for the above case study
2. Convert to relational Schema
Q4   b
Compare between tables and views   [5]
CO-3; SO-2;
BL-2
Q4   c
Explain Distributed Database Architecture. What is data partitioning
CO-1; SO-2;   [5]
in distributed database.
BL-2
a   Book( book_id, title,author, cost)
Store(store_no, city, state, inventory_val)
Stock(store_no, book_id,quantity)
Consider above relational schema and formulate SQL queries for the
Q5
following:
CO-3; SO-2;   [10]
BL-3   (i)Modify the cost of DBMS books by 10%
(ii)Find the author of the books which are available in Mumbai store
(iii)Find the title of the most expensive book
(iv)Find the total quantity of books in each store
(v)Add a new record in Book(Assume values as per requirement)
Q5   b
What are Tablespace and explain its significance. Also explain
CO-1; SO-2;   [10]
Segments, Extents and Data block structure.
BL-2
Q6   a
Explain how logical model differs from physical model. with this
CO-3; SO-2;   [10]
context explain data independence and its two types.
BL-3
Q6   b
What are basic building blocks in a data model. Also discuss about the
CO-2; SO-2;   [10]
business rules in DBMS
BL-2
Q7   a   Classify the 4 categories of SQL commands. Also illustrate with
[10]
CO-3; SO-2;   syntax and example the following command.
********** 2 **********
--- page 3 ---
BL-3   1. create 2. Alter 3. Update 4. Delete
b   Solve the following queries using relational algebra
Library (codeno, name, copies)
Person (id, name, age)
Is_member (code, id, date-of-joining)
Books (accn-no, title, author, price)
Borrowed-by (accn-no, id, date-of-borrow)
Q7   a) List all books borrowed on or after 26-01-97 and the names of the
CO-3; SO-2;   borrower, assume yyyymmdd   [10]
BL-3   b) List the details of the book and the student who has borrowed the
book with title ’DBMS’
c) Get names of person who has not borrowed any of the books
d) List the names of persons who has borrowed at least all the books
that are borrowed by person with id 110
e) Add a new record in Book(Assume values as per requirement).
********** 3 **********
````

## 2023-24 · Final-Exam · paper b34ea30397bd

- Departments: Information Technology
- Programmes: B.TECH INTEGRATED / IT
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/3rd YEAR/IT/Database System Essentials/Database System Essentials Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29/4/2024
- Text: ocr (4 pages), mean OCR confidence 89.8

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT ;

Academic Year: 2023-2024

Program: BTECH Integrated Year: II] Semester: VI

Stream: Information Technology

Subject: Database System Essentials Time: 3 hrs. ( 2:00pm, {o Scopes
Date: 29/4/2024 No. of Pag

Marks: 100

Final Examination

of the Answer Book, which is provided for their use.

1) Question No.1] is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: [20]

CO-1 ; SO-2 ; a. ‘ : ; ‘
; ; 2 {5]
BL- Understand Briefly, explain your understanding about Database Architecture ?

CO-2 ; SO-2 ; b. ‘ F an
BL- Understand What is Data Indexing and how it is useful ? [5]

CO-3 ; SO-2 ; ¢. | Which are different types of constraints in database design and what is the [5]
BL- Understand purpose of the same?

d. | i. State SQL key words to.... [2]
1> find table details in terms of structure
CO- 3; SO-2 ; 2> sort output data rows for given query in descending order. [5]
BL- Understand

ii. State three Group Functions in SQL and it’s implication [3]

2 * State various type of Data models and compare any two in terms of structure [10]
CO-1; SO-2; and drawbacks?

BL- Understand

CO-3; SO-2; b. | There is a multinational IT project developer company handling multiple

BL- Apply Projects. We have to develop database to monitor project status of various project [10]

as status and Team handling it. Continued next page....

1|Page
--- page 2 ---
Project details as: Domain like banking, e-commerce, social media etc., project
client, estimated man hours required, dead line, Team assigned with this project,
progress of project, Any issues. -
Team details as : Team lead name, project assigned to them
Engineers: engineer names, their experience, expertise, team belong to.

1. Draw ER diagram for the given case study [5]

2. Draw Schema Diagram [5]

Q3 a.

CO-2;-SO-2;
| BL- Understand

Compare 2- Tier v/s 3 Tier Database Architecture in terms of Structure , [10]
Applications, Benefits?

b. | i. Explain how you should take care of entering Null values in data set and
Why itis vital? [5]
ii. State and explain two functions in SQL to handle null values ; with suitable [10]
examples? [5]

CO-3; SO-2;
BL- Understand

Fo

Q4 oon
CO-2; $O-2; “ [10]
BL- Appl .

ER diagram for exam scheduling.
For the above ER diagram ; draw schema diagram and create Tables using
appropriate queries? [6]
Write a query to list all courses for which exam. is scheduled at 10 o’clock ?

[4]

CO-3; $O-2: b | What is your understanding about “View” in database and how to create the

; in wi i 2 [10]
BL- Understand same; explain with suitable example?
Q5
CO-3; SO-2: a State various objects which can be created in database implementation and [10]

. : aye 5
BL- Understand explate respective utility of the same?

b ; 5 : .
CO-3: SO-2: What is the purpose of Database Systems ? In which scenario one should

BL- Understand opt for file-based data ? [10]
Q6 a

State various Type of Database servers used and elaborate on any Two types?
CO-2; $O-2; YP [10]

BL- Understand

2|Page
--- page 3 ---
Write following queries based on a given “patient” table below.

i. Show the name, address, phone of those patients who has Diabetes
ii. | Modify the phone_no of patient with patient_id 100000010 as

555-025-4434
iii. | Show all the details for patient_id, 100000005 and 100000010

iv. Show the patient_id, phone, insurance_id of “ Tim ”

v. List all patients name having “Asthma” , “Flu” diseases.
patient_id name address phone insurance_id | disease
100000001 | John Smith 42 Foobar 312-441- | 68476213 | Flu
CO-3; SO-2; Lane 6652 [10]
BL- Apply 100000002 | Grace Ritchie] 37 Snafu Drive} 480-632- | 36546321 | Diabetes
7129
100000003 Ronny J. 101 Omgbbq | 718-347- | 65465421 | Asthma
Street 9365
100000004 | Dennis Doe | 1100Foobaz | 312-498- | 68421452 | Diabetes
Avenue 0186
100000005 John K 89, Port 814-473- 68421947 | Epilepsy
Avenue 7523
100000006 Karan M 951 Dye Street | 517-587- 68421101 | Diabetes
8042
100000007 Terry H 11 Floral Park | 555-2048 68421879 Stroke
100000008 Ronaldo J 4548 West 555-1204 - Flu
Drive
100000009 Tim 1031 Stutler | 555-0512 | 68431479 | Asthma
Lane
100000010 Rocky 951 Dye Street | 555-0256 - Epilepsy
{10]
i. Explain with example any two real life applications where database
management system is useful ? [5]
a
ii. What is your understanding about “Schema” and “Instance” in
database? [5]
Q7
CO-2; SO-2; b
BL- Understand Give Relational algebra based expressions for following queries; with respect
to tables given below?
1. List all employee’s name who having salary more than 20000 but
less than 30000.
2. List employees with name and designations who are located in [10]
Mumbai. ;
CO-3; SO-2; 3. Find all employee names located in Delhi and having salary more
BL« Apply than 10000.

4. Find designation of “Mohan”.
5. List all employee’s name working in Account dept.?
Data on next page.....

3|Page
--- page 4 ---
EMP

EMP NO | NAME DESIGNATION

1001 Ankus Clerk

1002 Mohan Sales officer

1003 Raju Manager

1004 Ramesh | Sales officer
DEPT De u no | Dept_name Location

Marketing | Mumbai
a Account Delhi
>
>

4|Page
````

## 2023-24 · Re-Exam · paper 8bf20e893875

- Departments: Information Technology
- Programmes: B.TECH INTEGRATED / IT
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/3rd YEAR/IT/Database System Essentials/Database Systm Essentials Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 2/7/24
- Text: ocr (4 pages), mean OCR confidence 88.2

````text
SVKM’S NMIMS

SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

Program: BTECH Integrated Year: [II Semester: VI
Stream: Information Technology

Subject: Database System Essentials . Time: 3 hrs. (Zpm-to Spu)
Date: 2/7/24 No. of Pages: 4

Marks: 100

Re Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No.1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: [20]
CO-1 ;.SO-2 ; a. : . . . .

5. ; 9 (5]
BL- Understand Briefly, explain your understanding about Client/Server Architecture ?
COZ 380-25 u What is Data Dictionary and how it is useful ? [5]

BL- Understand

CO-3 ; SO-2 ; Gs : F . , ,
{802 2 | (5)
BL- Understand State single row and multi row functions (two each type) with suitable examples?

CO- 3; SO-2 ; d. | Which are DML statements under SQL ; explain each with suitable examples? {5}
BL- Understand

Q2

CO-1; SO-2; a, | Justify as RDBMS is better than other Data model you studied ?
BL- Understand

[10]

b. | A housing society ; there are 20 buildings and each building have 20 flats with
two type of flat A, B with respective carpet area as 350 sq.ft and 450 sq.ft. We
need to maintain data for each flat owner occupying respectively with all family

CO-3; SO-2; members details in terms of sex, DOB, Education, in service / business/house [10]
BL- Apply wife/studying/retired; monthly bill @ rate Rs.30 per sq ft. for A type and @ rate

Rs.50 per sq ft. for B type and also past arrears if any also should be reflected

in bill.

1|[Page
--- page 2 ---
i

1. Draw ER diagram and create suitable Tables and consider,dummy
data [6] “ae

2. Write Queries to generate monthly maintenance bill with full
owner name, flat number, building number and Amount Payable

[4]
Q3 a.
CO-2; SO-2; Compare 1- Tier v/s 3 Tier Database in terms of Applications, Benefits. [10]
BL- Understand
CO-3: SO-2: b. | What is “View” in database and how is it significant from application point of
andes view? How to create the same? [10]
BL- Understand at :
a
on
=
4
CO-2; $O-2; [10]
BL- Apply
For the above ER diagram; Draw schema diagram and build Tables using
appropriate queries? An
CO-3; SO-2; b | How Logical model is different than Physical model of database ; explain with [10] t
BL- Understand suitable example. How it provides Data Independence?
Q5
CO-3: $O-2: a What is Table space and what is the significance of the same? [10]
BL- Un derstan d With suitable diagram, explain Segments, Extents and Data block structure?
b

CO-3; SO-2;
BL- Apply

Suppose you are given the following requirements for a simple database
for the IPL :

ethe IPL has many teams,

¢ each team has a name, a city, a coach, a captain, and a set of players, [10]
e each player belongs to only one team,

¢ each player has a name, a position (such as left wing or goalie), a skill
level, and a set of injury records,

¢ a team captain is also a player,

2|Page
--- page 3 ---
ran

1

e a game is played between two teams (referred to as host_tgam and
guest_team) and has a date (such as April 11th, 2023) and a score.”

(i) Design Entity Relation Diagram for the above Problem statement. [6]

(ii) Convert ER diagram to Relational Schema [4]

Q6

CO-2; SO-2;
BL- Understand

Compare Parallel database v/s Distributed database?

[10]

CO-3; SO-2;
BL- Apply

Consider following Table description and assume relevant data is populated
Write queries to get respective data output?

1. Show all the data of the Clerks who have been hired after the year
2010?

2. Show the last name, job_id, salary and commission of those
employees who earn commission. Sort the data by salary in
descending order?

3. Number of employees working in department with ID 50?

4. List of employee name with salary greater then Rs.10000?

5. In department 20 what is total amount of salary paid?

EMPLOYEES

Column Name Null? Type
EMPLOYEE_ID NOT NULL NUMBER(6)
FIRST_NAME VARCHAR2(20)
LAST_NAME NOT NULL VARCHAR2(25)
EMAIL NOT NULL VARCHAR2(20)
PHONE_NUMBER VARCHAR2(20)
HIRE_DATE NOT NULL DATE
JOB_ID NOT NULL VARCHAR2(10)
SALARY NUMBER(8,2)
COMMISSION_PCT NUMBER(2,2)
MANAGER_ID NUMBER(6)
DEPARTMENT ID NUMBER(4)

[10]

3|Page
--- page 4 ---
i

Q7 a Publications Database Schema details are as followed with data in figure I :

CO-3: SO-2: e author(author id, first name, last name) a
BL- Apply ; ¢ author_pub(author id, pub id, author position)

¢ book(book id, book title, month, year, editor)
. pub(pub id, title, book id)
author_ idi in author_pub is a foreign key referencing author

= pub_idi in author "pub is a foreign key referencing pub
= book_id in pub is a foreign key referencing book
«editor in book is a foreign key referencing
author(author_id)
= Primary keys are underlined
Pubs Database State

r(author) r(author pub)
author idi] fret name | lastname "| [author id | ‘pub-id | author-position
1 Jobo McCarthy T iy T
2 Deanis | Ritchie 2 2 I [10]
3 Ken Thompson 3 2 2
4 Claude ‘Shannoa 4 3 1 as
5 Alan Turing 5 4 T
6 ‘Alonzo | Church 3 i T
7 Perry White 6 6 T
By Moshe Vardi
9 Roy Batty
(book) r(pud)
book Idi book title Ji month ia] year =| editor pe ( title a Ee. | book id
T CACM | April 1960 [ 8 LISP T
2 CACM daly 1974 | 8 7 Unix 2
3 BST July 19s [2 3 Info Theory 3
4 TNS November | 1936 | 7 4 Turing Machines | 4
3 Mind October | 1950 | NULL] [S “Turing Test 3
6 AMS Month | 1941 | NULL | [6 Lambda Calculus | 6
7 AAAL July 2012 | 9
& NPS July 212 {9

Figure 1: Relational Database Schema

1. How many tuples (rows) will be returned by the following
relational algebra query?

TU book title(book)

2. What output the following expression gives?
|7U author id(author) — 7U editor(book)| >

3. How many tuples are returned by the following relational algebra
expression?
author [XJ author id=editor book

4. Write a relational algebra expression that returns the names of all
authors who have at least one publication in the database.

5. Write a relational algebra expression that returns the names of all
authors who are book editors.

CO-2; SO-2; b | Draw detail diagram for “Database System Internals” and explain basic [10]
BL- Understand element of the same?

4|Page
````
