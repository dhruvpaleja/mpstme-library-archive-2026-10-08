# Database System Essentials: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 6447687644ff

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/Integrated_IT_7037/Database System Essentials/ANS_Database System Essentials(701IT0C010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
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
1. This question paper contains 15 pages.
2. Question No.1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a.   Discuss different types of database users and how each interacts with the
database system.
Answer:
CO-1 ; SO-2 ;   Naïve Users: Use predefined queries (e.g., bank clerk)   [5]
BL-2
Application Programmers: Write programs using DB
Database Administrators (DBA): Manage security, backup, tuning
Sophisticated Users: Analysts using complex queries
Specialized Users: Scientists, engineers using DB tools
b. Consider a table EMPLOYEE(EmpID, Name, Email, Phone, AadharNo).
(a) Identify possible superkeys.
(b) Determine the candidate keys.
(c) Choose an appropriate primary key and justify your choice.
(a) Superkeys:
{EmpID}, {Email}, {Phone}, {AadharNo}, combinations
CO-3 ; SO-2 ;   [5]
BL-2   (b) Candidate Keys:
EmpID, Email, AadharNo
(c) Primary Key:
EmpID
👉 Unique, stable, minimal
********** 1 **********
--- page 2 ---
(d)
c.   Identify and explain five practical applications of database systems
in different domains.
Answer:
CO-1 ; SO-2 ;   • Banking (transactions)   [5]
BL-2   •   Healthcare (patient records)
• E-commerce (orders, inventory)
• Education (student records)
• Telecom (call records)
d. Explain the 3 Set Operators in Relational algebra with one example
each
• Union (∪): Combine tuples
CO-3; SO-2 ;   •   Intersection (∩): Common tuples
[5]
BL-2   •   Difference (−): Remove tuples
Example:
R(A,B) ∪ S(A,B)
a What are Constrainst in SQL? Explain Primary key,foreign key,Check
and Unique constraint with example and syntax.
• Primary Key: Unique + not null
PRIMARY KEY (id)
Q2   • Foreign Key: Reference
CO-3-; SO-2;   FOREIGN KEY (dept_id) REFERENCES Dept(id)   [10]
BL-2
• Check: Condition
CHECK (salary > 0)
• Unique: No duplicates
UNIQUE(email)
b. Draw an E-R Diagram for the problem statement: Problem Statement: A
university offers multiple programs (e.g., B.Tech IT, B.Tech CS). Each
Q2   program has a unique Program_ID, name, and duration. Each program
consists of several courses; each course has a Course_Code, Course_Name,   [10]
CO-2; SO-2;   and credits. A course may be taught by one or more instructors; each
BL-3   instructor has an Instructor_ID, name, designation, and email. Students
enroll in one program and are identified by Student_ID, name, email, and
year_of_admission. Students can register for multiple courses each semester,
********** 2 **********
--- page 3 ---
and for each registration, the system stores semester, academic_year, and
grade.
a. What is data independence? Explain the two types of data
independence. Draw and explain the 3 level architecture to achieve
data abstraction
Answer:
Q3
•   Physical: Change storage without affecting schema
CO-2; SO-2;   •   Logical: Change schema without affecting application   [10]
BL-2
3-Level Architecture:
•   External
• Conceptual
•   Internal
b.   employee (eid, name, city)
Q3   works (eid, cid, salary)
CO-3; SO-2;   company (cid, cname, location)   [10]
BL-3   manager (mid, mname)
Write the Relational Algebra Queries for the below
********** 3 **********
--- page 4 ---
1.Find the names of all companies
2.Find the employee IDs who are not working in any company
3.Find the names of employees along with the companies they work
for
4.Find the names of employees who have salary greater than 50000
5.Find the names of companies that have at least one employee
working
a.   State the importance of Data models. Explain the relational model and
the Hierarchical Model with diagrams .
Importance of Data Models
Data models are essential in database design as they define how data is
structured, stored, and related.
Importance:
Data Organization: Provides a clear structure for storing data
Data Abstraction: Hides complex details from users
Data Integrity: Ensures consistency and accuracy
Database Design: Helps in designing efficient schemas
Communication Tool: Acts as a bridge between users and developers
Flexibility: Supports modification without affecting applications
Relational Model
The Relational Model organizes data in the form of tables (relations)
consisting of rows and columns.
Q4
CO-2; SO-2;   Key Concepts:   [10]
Relation: Table
BL-2
Tuple: Row
Attribute: Column
Primary Key: Unique identifier
Foreign Key: Establishes relationships
Diagram (Relational Model)
Example:
********** 4 **********
--- page 5 ---
Student Table
SID Name Course
1   Rahul IT
2   Neha CS
Advantages:
Simple and easy to use
Supports powerful queries (SQL)
Ensures data integrity
Hierarchical Model
The Hierarchical Model organizes data in a tree-like structure, where
each child has only one parent.
Key Features:
Parent-child relationship
One-to-many mapping
Data stored in hierarchy
Diagram (Hierarchical Model)
Example:
Department
├── Employee 1
├── Employee 2
└── Employee 3
Advantages:
Fast data access
Simple structure for hierarchical data
Limitations:
Difficult to represent many-to-many relationships
Less flexible compared to relational model
********** 5 **********
--- page 6 ---
b.
Design the schema for the given ER Model
Relational Schema
1. Flight
Flight(
flno PRIMARY KEY,
origin,
dest,
dist,
Q4   arrives,
CO-1; SO-2;   departs,   [5]
BL-3   num FOREIGN KEY REFERENCES Airplane(num)
)
2. Airplane
Airplane(
num PRIMARY KEY,
type_id FOREIGN KEY REFERENCES Aircraft_Type(id)
)
3. Aircraft_Type
Aircraft_Type(
id PRIMARY KEY,
name,
range
)
4. Employee
Employee(
id PRIMARY KEY,
name,
salary
)
5. Certified (for "Is Certified" relationship)
Certified(
emp_id FOREIGN KEY REFERENCES Employee(id),
type_id FOREIGN KEY REFERENCES Aircraft_Type(id),
PRIMARY KEY(emp_id, type_id)
)
c. Explain with syntax and example the following relational algebra
Q4   operators   [5]
a. Select
********** 6 **********
--- page 7 ---
CO-2; SO-2;   b. Natural Join
BL-2   c. Cartesian Product
d. Project
e. Rename
a. Explain Parallel Database Architecture. What is shared Memory
Architecture
Answer:
Introduction of Parallel Database
Parallel Databases and then will emphasize their needs and
advantages, and then finally, will cover the performance measurement
factor-like Speedup and Scale-up with examples. Let’s discuss it one
by one.
Parallel Databases :
Nowadays organizations need to handle a huge amount of data with a
high transfer rate. For such requirements, the client-server or
centralized system is not efficient. With the need to improve the
efficiency of the system, the concept of the parallel database comes in
picture. A parallel database system seeks to improve the performance
of the system through parallelizing concept.
Need :
Multiple resources like CPUs and Disks are used in parallel. The
operations are performed simultaneously, as opposed to serial
processing. A parallel server can allow access to a single database by
Q5   users on multiple machines. It also performs many parallelization
operations like data loading, query processing, building indexes, and   [10]
CO-1; SO-2;
evaluating queries.
BL-2
Advantages :
Here, we will discuss the advantages of parallel databases. Let’s have
a look.
1.   Performance Improvement –
By connecting multiple resources like CPU and disks in parallel we
can significantly increase the performance of the system.
2.   High availability –
In the parallel database, nodes have less contact with each other, so
the failure of one node doesn’t cause for failure of the entire system.
This amounts to significantly higher database availability.
3.   Proper resource utilization –
Due to parallel execution, the CPU will never be idle. Thus, proper
utilization of resources is there.
4.   Increase Reliability –
When one site fails, the execution can continue with another available
site which is having a copy of data. Making the system more reliable.
********** 7 **********
--- page 8 ---
A parallel DBMS is a DBMS that runs across multiple processors or
CPUs and is mainly designed to execute query operations in parallel,
wherever possible. The parallel DBMS link a number of smaller
machines to achieve the same throughput as expected from a single
large machine.
In Parallel Databases, mainly there are three architectural designs for
parallel DBMS. They are as follows:
1.   Shared Memory Architecture
2.   Shared Disk Architecture
3.   Shared Nothing Architecture
Let’s discuss them one by one:
1.   Shared Memory Architecture- In Shared Memory Architecture,
there are multiple CPUs that are attached to an interconnection
network. They are able to share a single or global main memory and
common disk arrays. It is to be noted that, In this architecture, a single
copy of a multi-threaded operating system and multithreaded DBMS
can support these multiple CPUs. Also, the shared memory is a solid
coupled architecture in which multiple CPUs share their memory. It is
also known as Symmetric multiprocessing (SMP). This architecture
has a very wide range which starts from personal workstations that
support a few microprocessors in parallel via RISC.
Shared Memory Architecture
Advantages :
1.   It has high-speed data access for a limited number of
processors.
2.   The communication is efficient.
Disadvantages :
1.   It cannot use beyond 80 or 100 CPUs in parallel.
2.   The bus or the interconnection network gets block due to the
increment of the large number of CPUs.
Q5   b.
What are views in SQL. Write the syntax to create a view with the help [5]
CO-3; SO-2;
of an example
BL-2
********** 8 **********
--- page 9 ---
Answer:
Virtual table
CREATE VIEW emp_view AS
SELECT name, salary FROM Employee;
c. Compare Tuple relational calculus and Domain relational Calculus.
Give one example queries of each
• TRC: Uses tuples
• DRC: Uses domains
Example:
TRC: {t.name | Employee(t)}
DRC: {<name> | ∃id(Employee(id,name))}
Tuple Relational   Domain Relational Calculus
Basis
Calculus (TRC)   (DRC)
Q5
Variable
CO-3; SO-2;   Tuple variables   Domain (attribute) variables   [5]
Type
BL-3   Focus   Entire row (tuple) Individual attributes
Representatio
t.Attribute   Separate variables for each field
n
Easier to
Simplicity   More mathematical
understand
Query
Compact   Slightly complex
Writing
Example
STUDENT(t)   STUDENT(r, n, a)
Style
a. Write SQL queries for the given database:
Student (sid, sname, city)
Enroll (sid, course_id, marks)
Q6
Course (course_id, course_name, department)
CO-3; SO-2;   [10]
BL-3   i) Give all students enrolled in ‘Data Science’ course a 5% increase in
marks.
ii) Find the total number of students.
********** 9 **********
--- page 10 ---
iii) Find the student with highest marks.
iv) Find the average marks of students in each course.
v) List the names of students who are not enrolled in any course.
i)
UPDATE Enroll
SET marks = marks * 1.05
WHERE course_id = 'Data Science';
ii)
SELECT COUNT(*) FROM Student;
iii)
SELECT sname FROM Student s, Enroll e
WHERE s.sid=e.sid
AND marks = (SELECT MAX(marks) FROM Enroll);
iv)
SELECT course_id, AVG(marks)
FROM Enroll GROUP BY course_id;
v)
SELECT sname FROM Student
WHERE sid NOT IN (SELECT sid FROM Enroll);
b. Describe Indexing and Hashing techniques used for data retrieval in
databases. Explain different types of indexing and hashing, and state their
advantages and limitations.
Answer:
Indexing and Hashing Techniques for Data Retrieval
Efficient data retrieval is a key requirement in database systems. Two
major techniques used to improve search performance are Indexing and
Q6   Hashing.
CO-1; SO-2;   [10]
1. Indexing
BL-2   Indexing is a technique used to speed up data retrieval operations by
creating a separate data structure (index) that stores key values and
pointers to the actual records.
Instead of scanning the entire table, the database searches the index to
quickly locate data.
Working
Index contains:
********** 10 **********
--- page 11 ---
Search key
Pointer to record/block
Similar to a book index, where topics point to page numbers
Types of Indexing
1. Primary Index
Created on primary key
Data file is sorted
Usually sparse index (not every record has entry)
Advantages
Fast access for ordered data
Less storage (sparse)
Limitations
Requires sorted file
Insert/Delete operations are costly
2. Secondary Index
Created on non-primary key
Does not require sorted file
Usually dense index (entry for each record)
Advantages
Allows search on non-key attributes
Faster query flexibility
Limitations
Requires more storage
Maintenance overhead
3. Clustered Index
Records are physically stored in order
One clustered index per table
Advantages
Very efficient for range queries
Better data locality
Limitations
Only one allowed
Reorganization required on updates
4. Non-Clustered Index
Separate structure with pointers to actual data
Advantages
Multiple indexes possible
Improves search on different attributes
********** 11 **********
--- page 12 ---
Limitations
Extra lookup required
Slightly slower than clustered
5. Multilevel Index
Index on index (hierarchical)
Reduces search complexity
Advantages
Very fast search (logarithmic time)
Suitable for large databases
Limitations
Complex structure
Extra storage
Advantages of Indexing
Reduces search time
Improves query performance
Efficient for range queries
Limitations of Indexing
Requires extra storage
Maintenance overhead (insert/update/delete)
Slower write operations
2. Hashing
Hashing is a technique where a hash function is applied to a key to
compute a memory location (bucket) where the record is stored.
Working
Hash Function:
h(key) → address
Direct access to data without searching
Types of Hashing
1. Static Hashing
Fixed number of buckets
Uses hash function for mapping
Advantages
Simple and fast
Direct access
Limitations
Overflow problem
Poor performance when data grows
2. Dynamic Hashing
Buckets can grow/shrink dynamically
Examples: Extendible hashing, Linear hashing
Advantages
********** 12 **********
--- page 13 ---
Efficient memory utilization
Reduces overflow
Limitations
Complex implementation
Extra overhead
Collision Handling Techniques
Chaining (linked list in bucket)
Open Addressing (probing)
Advantages of Hashing
Very fast data access (O(1) average)
Suitable for exact match queries
Limitations of Hashing
Not suitable for range queries
Collision handling required
Performance depends on hash function
a.   Online Shopping Database Schema
•   customer (cust_id, cust_name, city)
•   orders (order_id, cust_id, product_id)
•   product (product_id, product_name, category, supplier_id)
•   supplier (supplier_id, supplier_name)
Constraints:
•   cust_id in orders → FK referencing customer
•   product_id in orders → FK referencing product
•   supplier_id in product → FK referencing supplier
customer   Supplier
Q7
CO-3; SO-2;   [10]
BL-3
Product   orders
Questions
********** 13 **********
--- page 14 ---
i.   How many tuples (rows) will be returned by:
ii.   What is the result of:
iii.   How many tuples are returned by:
iv.   Write a relational algebra expression to find names of suppliers whose
products are ordered.
v.   Write a relational algebra expression to find names of customers
who ordered products in ‘Electronics’ category
b. Consider the following EMPLOYEE table description and assume
relevant data is populated.
Employee(employee_id, first_name, last_name, email, phone_number,
hire_date, job_id, salary, commission_pct, manager_id, department_id)
Write SQL queries to get the respective outputs:
1. Show all details of employees who are working as Managers and
were hired after the year 2015.
2. Display the first name, last name, job_id, and salary of
employees whose salary is greater than 50000. Sort the result in
ascending order of salary.
Q7
3. Count the number of employees working in department with ID
CO-3; SO-2;   30.   [10]
BL-3   4. List the employee names whose salary is between 20000 and
60000.
5. Find the total salary paid to employees in department 10.
1.
SELECT * FROM Employee
WHERE job_id='Manager'
AND hire_date > '2015-01-01';
2.
SELECT first_name, last_name, job_id, salary
FROM Employee
WHERE salary > 50000
ORDER BY salary ASC;
********** 14 **********
--- page 15 ---
3.
SELECT COUNT(*) FROM Employee
WHERE department_id = 30;
4.
SELECT first_name FROM Employee
WHERE salary BETWEEN 20000 AND 60000;
5.
SELECT SUM(salary) FROM Employee
WHERE department_id = 10;
********** 15 **********
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 55b350eca92e

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/Integrated_IT_7037/Database System Essentials/ANS_Database System Essentials(701IT0C010)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 May 2025
- Text: text (5 pages)

````text
SYNOPTICS
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
1. This question paper contains 5 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a. At least 5 points of difference between 2-tier and 3-tier client-server
CO-1 ; SO-2 ;   [5]
BL-2   architecture
b.   Illustrate the natural join operator in Relational algebra. Also explain left
join,right join and full join with symbols
CO-3 ; SO-2 ;   [5]
BL-2   Natural Join-2 marks
3 types-1 mark each
CO-3 ; SO-2 ;   c. Explain any five string functions in SQL (5 functions,1 mark each)   [5]
BL-2
d. For any Database applications, explain the advantages of database
CO-1; SO-2 ;   system over file processing system.   [5]
BL-2
At least 5 points 1 mark each
a What are Data Models. Explain the Relational model and the Object
Q2   Oriented Model.
CO-2-; SO-2;   Data amodels-4 marks   [10]
BL-2   Relational -3 marks
Object Oriented -3 marks
Q2   b   Explain DDL, DML, DCL and DTL commands in SQL. Explain with
CO-3; SO-2;   syntax and example foreign key, unique and check constraint.   [10]
BL-3   DDL, DML, DCL and DTL-1 mark each
********** 1 **********
--- page 2 ---
foreign key, unique and check constraint-2 mark each
a   Describe parallel database architecture. Explain about Shared Memory
Q3   Architecture, Shared Disk Architecture , Shared Nothing Architecture
CO-1; SO-2;   parallel database architecture-4 marks   [10]
BL-2   Shared Memory Architecture, Shared Disk Architecture , Shared
Nothing Architecture-2 marks each
b A library manages books, members, and staff. Each book has a unique
ISBN, and members can borrow multiple books. The system should
track book availability, due dates, fines, and book reservations. Design
a relational database schema for this application, specifying tables,
attributes, and primary/foreign keys.
Q3   Book(ISBN, title, author, publisher, edition, category, total_copies,
CO-1; SO-2;   available_copies)   [5]
Member(member_id, name, email, phone, address, membership_type,
BL-2   date_of_joining)
Staff(staff_id, name, email, phone, role, salary)
Borrow(borrow_id, member_id, ISBN, borrow_date, due_date,
return_date, fine)
Reservation(reservation_id, member_id, ISBN, reservation_date,
status)
Fine(fine_id, member_id, amount, status, date_issued, date_paid)
c   For the Given ER model below, give the respective relational model
Q3   Person(driver_id, name, address)
Car(license, model, year)
CO-3; SO-2;   Owns(driver_id, license)   [5]
BL-3   Accident(report_number, location, date)
Participated(license, report_number, driver_id, damage_amount)
a A Car Insurance Company whose customer s owns one or more cars
each. Each car has associated with it zero or any number of recorded
accidents.
1. Develop an ER diagram for the above case study
Q4
CO2-; SO-2;   [10]
BL-3
2. Convert to relational Schema
Person(driver_id, name, address)
********** 2 **********
--- page 3 ---
Car(license, model, year, driver_id)
Accident(accident_id, date, location)
Participated(license_no, accident_id, damage_amount)
Owns(driver_id, license)
b What are views? Explain in details with syntax creation and updating
Q4   of views.
CO-3; SO-2;   Views-2 marks   [5]
BL-2   Create view-2 marks
Update view -1 marks
Q4   c
CO-1; SO-2;   Explanation of transaction servers in DBMS.-5 marks   [5]
BL-2
a   Consider below relational schema and formulate SQL queries for the
following:
Employee (eid,ename,street,city)
Works (eid, cid, salary)
Company (cid, cname,city)
(i) Modify the database so that Jack now lives in ‘Mumbai’
UPDATE Employee
SET city = 'Mumbai'
WHERE ename = 'Jack';
(ii) Give all employees of ‘ANZ Corporation’ a 10% raise in salary.
UPDATE Works
SET salary = salary * 1.10
Q5   WHERE cid IN (SELECT cid FROM Company WHERE cname =
'ANZ Corporation');   [10]
CO-3; SO-2;
BL-3   (iii) Find all employee IDs who live in the same city as the company
for which they work.
SELECT DISTINCT w.eid
FROM Works w
JOIN Employee e ON w.eid = e.eid
JOIN Company c ON w.cid = c.cid
WHERE e.city = c.city;
(iv) Give the total number of employees.
SELECT COUNT(*) AS total_employees FROM Employee;
(v) Find the highest-paid employee.
SELECT w.eid, e.ename, w.salary
FROM Works w
JOIN Employee e ON w.eid = e.eid
********** 3 **********
--- page 4 ---
WHERE w.salary = (SELECT MAX(salary) FROM Works);
b   Discuss about Indexing and Hashing in DBMS. What are Data
Q5
Dictionary and Dictionary Views?
CO-1; SO-2;   [10]
Indexing and Hashing- 6 arks
BL-2
Data Dictionary and Dictionary Views-4 marks
a   Classify the 4 categories of SQL commands. Also illustrate with syntax
and example the following command.
Q6
1. create 2. Alter 3. Update 4. Delete
CO-3; SO-2;   [10]
4 categories of SQL commands-4 marks
BL-3
create 2 marks, Alter- 2 marks. Update-1 mark, Delete-1 mark
b What are Degrees of data abstraction in DBMS. With respect to ER
Q6   model explain strong entity set, weak entity set, total and partial
CO-2; SO-2;   participation   [10]
BL-2   Degrees of data abstraction-6 marks
strong entity set, weak entity set, total and partial participation-4 marks
a   Differentiate between logical and physical data independence. Also
Q7   explain any 5 aggregate functions in SQL.
CO-3; SO-2;   5points of diffrenec between logical and physical data independence-5   [10]
BL-3   marks
5 aggregate functions-1 mark each
b   Book( book_id, title,author, cost)
Store(store_no, city, state, inventory_val)
Stock(store_no, book_id,quantity)
Consider above relational schema and formulate relational algebra queries
for the following:
Q7
CO-3; SO-2;   [10]
BL-3   (i) Modify the cost of DBMS books by 10%
π_book_id, title, author, cost * 1.10 (σ_title='DBMS'(Book))
(ii) Find the author of the books which are available in Mumbai
π_author ( (σ_city='Mumbai' (Store)) ⨝ Stock ⨝ Book )
(iii) Find the title of the most expensive book
π_title (σ_cost = MAX(cost)(Book))
********** 4 **********
--- page 5 ---
(iv) Find the titles of all books available in stores located in
Maharashtra.
π_title ( (σ_state='Maharashtra' (Store)) ⨝ Stock ⨝ Book ))
(v) Add a new record in Book (Assume values as per requirement)
Book ← Book ∪ {(101, 'Machine Learning', 'Andrew Ng', 1500)}
********** 5 **********
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper 97941730f637

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/Integrated_IT_7037/Database System Essentials/ANS_Database System Essentials(701IT0C010)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Jul 2025
- Text: mixed (5 pages), mean OCR confidence 72.0

````text
SYNOPTICS
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
1. This question paper contains 5 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
CO-1 ; SO-2 ;   a. Explanation of cloud based servers in DBMS –5marks   [5]
BL-2
b.   Illustrate the following relational algebra operators (1 mark each)
CO-3 ; SO-2 ;   [5]
BL-2   a. Project , b. Natural Join, c. Union, d. Intersect, e. Rename
CO-3 ; SO-2 ;   c. Explain any five aggregate functions in SQL (5 functions,1 mark each) [5]
BL-2
d. Summarize any 5 database applications.
CO-1; SO-2 ;   [5]
BL-2   Any 5 application with short explanation, 1 mark each)
a   Discuss the importance of Data Models. Explain the Hierarchical model
Q2   and the Network Model.
CO-2-; SO-2;   Importance-4 marks   [10]
BL-2   Hierarchical-3 marks
Network-3 marks
b What are constraints in SQL. Explain with syntax and example
primary key, foreign key, not null and check constraint
Q2   Constraints – 2 marks
[10]
CO-3; SO-2;   primary key-2 marks, foreign key-2 marks, not null-2 marks and check
BL-3
constraint-2 marks
********** 1 **********
--- page 2 ---
a   Describe with help of a neat diagram the complete database system
Q3
architecture.
CO-1; SO-2;   [10]
Diagram -4 marks
BL-2
Explanation of each component-6 marks
b A university course registration system allows students to register for
courses at the beginning of each semester. The system maintains
records of students, courses, instructors, and enrollments. Students can
register for multiple courses, but each course has a maximum
capacity. The system should prevent overbooking and ensure that each
Q3   student meets the prerequisites before enrollment. Design a relational
database schema for this application, specifying tables, attributes, and   [5]
CO-1; SO-2;   primary/foreign keys
BL-2   Student(StudentID, Name, Email, Phone, Address, DOB)
Course(CourseID, CourseName, Credits, Capacity, PrerequisiteID)
Instructor(InstructorID, Name, Email, Department)
Enrollment(EnrollmentID, StudentID, CourseID, Semester, Grade)
Teaches(InstructorID, CourseID)
Prerequisites(CourseID, PrereqID).
Q3   c Compare Tuple relational calculus and relational algebra. Also give an
CO-3; SO-2;   example query of each   [5]
BL-3   At least 4 to 5 points of difference
a A   hospital   includes   patients,   doctors,   nurses,   departments,
appointments, and billing. Each patient is assigned a unique patient ID
and may have multiple appointments with different doctors. The system
should also track prescribed medications and treatments.
1. Develop an ER diagram for the above case study
2. Convert to relational Schema
Q4
CO2-; SO-2;   [10]
BL-3
Patients(ssn,   name,   insurance,   date_admitted,
date_checked_out)
Doctors(dssn, name, specialization)
Test(test_id, test_name, date, time, result)
Test_Log(ssn, test_id)
Performed_By(test_id, dssn)
********** 2 **********
--- page 3 ---
Dr_Patient(ssn, dssn)
Q4   b Compare between tables and views
[5]
CO-3; SO-2;   At least 5 points of differences
BL-2
c   Explain Distributed Database Architecture. What is data partitioning
Q4
in distributed database.
CO-1; SO-2;   [5]
Explanation Distributed DB architecture-2 marks
BL-2
Horizontal Fragmentation and Vertical Fragmentation -3 marks
a   Book( book_id, title,author, cost)
Store(store_no, city, state, inventory_val)
Stock(store_no, book_id,quantity)
(i) Modify the cost of DBMS books by 10%
UPDATE Book
SET cost = cost * 1.10
WHERE title LIKE '%DBMS%';
(ii) Find the author of the books which are available in Mumbai store
SELECT DISTINCT B.author
FROM Book B
JOIN Stock S ON B.book_id = S.book_id
Q5   JOIN Store St ON S.store_no = St.store_no
CO-3; SO-2;   WHERE St.city = 'Mumbai';   [10]
BL-3
(iii) Find the title of the most expensive book
SELECT title
FROM Book
WHERE cost = (SELECT MAX(cost) FROM Book);
(iv) Find the total quantity of books in each store
SELECT S.store_no, SUM(S.quantity) AS total_books
FROM Stock S
GROUP BY S.store_no;
(v) Add a new record in Book (Assume values as per requirement)
INSERT INTO Book (book_id, title, author, cost)
VALUES (101, 'Database Systems', 'Ramez Elmasri', 750);
b What are Tablespace and explain its significance. Also explain
Q5
Segments, Extents and Data block structure.
CO-1; SO-2;   [10]
Tablespace-4 marks
BL-2
Segments, Extents and Data block structure-2 marks each
********** 3 **********
--- page 4 ---
a   Explain how logical model differs from physical model. with this
Q6   context explain data independence and its two types.
CO-3; SO-2;   Difference betwenn logical physical model-4 marks   [10]
BL-3   Data independence-2 marks
LDI and PDI -2 marks each
b What are basic building blocks in a data model. Also discuss about the
Q6
business rules in DBMS
CO-2; SO-2;   [10]
5 building blocks-1 mark each
BL-2
Business rules-5 marks
a   Classify the 4 categories of SQL commands. Also illustrate with
Q7   syntax and example the following command.
CO-3; SO-2;   1. create 2. Alter 3. Update 4. Delete   [10]
BL-3   DDL,DML,DCL,DTL-1 mark each
Create-1 mark,alter-2 marks,update 1mark,delete-1 mark
b   Solve the foll using relational algebra
Library (codeno, name, copies)
Person (id, name, age)
Is_member (code, id, date-of-joining)
Books (accn-no, title, author, price)
Borrowed-by (accn-no, id, date-of-borrow)
(a) List all books borrowed on or after 26-01-97 and the names of the
borrower
Filtered_Borrows ← σ date-of-borrow >= '1997-01-26' (Borrowed-by)
Result ← π title, name (Filtered_Borrows ⨝ Books ⨝ Person)
(b) List the details of the book and the student who has borrowed the
Q7   book with title 'DBMS'
CO-3; SO-2;   [10]
DBMS_Books ← σ title='DBMS' (Books)
BL-3
Borrowed_DBMS ← DBMS_Books ⨝ Borrowed-by
Result ← Borrowed_DBMS ⨝ Person
(c) Get names of persons who have not borrowed any books
Borrowers ← π id (Borrowed-by)
Non_Borrowers ← π id, name (Person) - Borrowers
(d) List the names of persons who have borrowed at least all the books
that are borrowed by the person with id 110
Books_Borrowed_By_110 ← π accn-no (σ id=110 (Borrowed-by))
Borrowers ← π id (Borrowed-by ⨝ Books_Borrowed_By_110)
Result ← π name (Person ⨝ Borrowers)
********** 4 **********
--- page 5 ---
(e) Add a new record in Books

Books < Books U { ('B123', ‘Operating Systems’, 'Galvin', 650) }

FIC DI EH ar
````
