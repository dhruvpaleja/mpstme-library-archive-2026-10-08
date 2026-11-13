# Introduction to Database Management System: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 0e1db1928bff

- Departments: Computer Engineering
- Programmes: DIPLOMA IN COMPUTER ENGINEERING - 7073
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER ENGINEERING - 7073/Introduction to Database Management System/ANS_Introduction to Database Management System(701CO0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Database Management System
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
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
Synopti   Basis   File System   DBMS
c   1. Data   High redundancy   Reduced redundancy due to
Redundanc   (duplicate data   centralized control
y   exists)
2. Data   Poor consistency   High consistency
Consistenc   (data mismatch   maintained
y   possible)
3. Data   Limited data   Easy data sharing among
Sharing   sharing   multiple users
4. Data   Less secure   Strong security mechanisms
Security   (authentication,
authorization)
5. Data   No data   Provides logical & physical
Independe   independence   data independence
nce
6. Query   No query language   Uses SQL for efficient data
Processing   support   retrieval
7. Backup   Difficult and   Automatic backup and
&   manual   recovery features
Recovery
********** 1 **********
--- page 2 ---
CO-2,   b.   Describe the following terms with examples: i) Weak Entity ii) [5]
SO-1   Multivalued Attributes
BL-2
Synopti   i) Weak Entity
c   A weak entity is an entity that does not have a primary key of its own
and depends on a strong entity for its identification.
Key Points:
• Cannot be uniquely identified by its own attributes
• Depends on a strong (owner) entity
• Has a partial key (discriminator)
• Represented by double rectangle in ER diagram
Example:
• Employee (Strong Entity) → has Employee_ID
• Dependent (Weak Entity) → attributes: Name, Age
Here, a dependent is identified by:
(Employee_ID + Dependent_Name)
ii) Multivalued Attribute
A multivalued attribute is an attribute that can have multiple values
for a single entity.
Key Points:
•   Stores more than one value
• Represented by double oval in ER diagram
Example:
• Student Entity
o Name: John
o Phone Numbers: 9876543210, 9123456780
Here, Phone_Number is a multivalued attribute.
CO-3;   c.   Explain the concept of normalization in Database Management Systems [5]
SO-1   and discuss the objectives of normalization.
BL- 2;
Synopti   Normalization is the process of organizing data in a database to reduce
c   redundancy and improve data integrity by dividing large tables into
smaller, well-structured tables and defining relationships between
them.
Objectives of Normalization
1. Eliminate Data Redundancy – Avoid duplicate data storage.
2. Ensure Data Consistency – Maintain uniform and accurate
data.
3. Improve Data Integrity – Enforce correct relationships using
keys and constraints.
4. Avoid Anomalies – Prevent insertion, deletion, and update
anomalies.
5. Efficient Data Organization – Structure data logically for
better management.
********** 2 **********
--- page 3 ---
Normalization helps in creating a clean, efficient, and reliable
database structure.
CO-4;   d.   What is constraint in SQL. Explain any two constraints with example.   [5]
SO-1 ;
BL- 2;
Synopti   A constraint in SQL is a rule applied to a table or column to restrict
c   the type of data that can be inserted, updated, or deleted, ensuring data
accuracy and integrity.
1. PRIMARY KEY Constraint
• Uniquely identifies each record in a table
• Cannot contain NULL values
• Each table can have only one primary key
2. FOREIGN KEY Constraint
• Used to link two tables
• Ensures referential integrity
• Value must match a value in the referenced table
Q2   a   Discuss the three-schema architecture of DBMS and explain the role of [10]
CO-1;   each level.
SO-1;
BL-2;
Synopti   The three-schema architecture ensures data abstraction, security, and
c   independence, making DBMS flexible and efficient.
Levels of Three-Schema Architecture
1. External Level (View Level)
• Represents how end users view the data
• Each user can have a different view of the same database
• Focuses only on required data
Example:A student sees only Name and Marks, while an admin sees
full student details.
2. Conceptual Level (Logical Level)
• Describes the overall structure of the database
•   Includes entities, relationships, constraints
• Independent of physical storage
Example:Defines tables like Student (ID, Name, Marks) and their
relationships.
Internal Level (Physical Level)
• Describes how data is actually stored in the system
•   Includes file structure, indexing, storage methods
Example:Data stored in files using indexes, hashing, etc.
Role of Each Level
• External Level: Provides customized views and security
• Conceptual Level: Maintains logical structure and relationships
• Internal Level: Handles efficient storage and retrieval
********** 3 **********
--- page 4 ---
CO2;S   b   Design an ER diagram for the given scenario and convert it into [10]
O-   relational tables.
1;BL-
A hospital plans to develop a database system to manage information
4;
about departments, doctors, and patients.
Each department has a unique dept_ID, dept_name, and location.
Every department employs multiple doctors.
Each doctor has a unique doctor_ID, doctor_name, expertise, and phone
number. A doctor works in exactly one department.
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
4. Convert the ER diagram into relational tables with primary and
foreign keys.
Synopti   1. ER Diagram Design (Textual Representation)
c
Entities & Attributes
1. Department (Strong Entity)
• dept_ID (PK)
• dept_name
•   location
2. Doctor (Strong Entity)
• doctor_ID (PK)
• doctor_name
•   expertise
• phone
3. Patient (Strong Entity)
• patient_ID (PK)
• patient_name (Composite: f_name, l_name)
********** 4 **********
--- page 5 ---
• DOB
• age
•   address
• phone (Multivalued)
4. Attendant (Weak Entity)
• A_Name (Partial Key)
•   relation
• phone
•   address
2. Relationships
1. Department – Doctor
o Relationship: Employs
o 1 : N (One department → many doctors)
o Total participation of Doctor
2. Department – Patient
o Relationship: Assigned_To
o 1 : N (One department → many patients)
o Total participation of Patient
3. Doctor – Patient
o Relationship: Consults
o M : N
4. Patient – Attendant
o Relationship: Has
o 1 : N (One patient → many attendants)
o Total participation of Attendant (weak entity)
3. Cardinality & Participation Constraints
Relationship   Cardinal   Participation
ity
Department–   1 : N   Doctor → Total
Doctor
Department–   1 : N   Patient → Total
Patient
Doctor–Patient M : N   Partial
Patient–   1 : N   Attendant →
Attendant   Total
4. Special Attributes
• Composite Attribute: patient_name → (f_name, l_name)
• Multivalued Attribute: Patient → phone
• Weak Entity: Attendant (depends on Patient)
********** 5 **********
--- page 6 ---
Q3   a   a. Find all the candidate keys of a given relation.   [10]
CO- 3;   R (A, B, C, D)
SO-;   Functional Dependency (FD): {AB->CD, D->B, C->A}
BL4-;
b. Consider the following relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Projects)
EmpID   EmpName   Projects
E101   Raj   AI, DBMS
E102   Simran   ML
E103   Karan   AI, ML, Cloud
Perform the given tasks:
a. Identify whether the given relation is in First Normal Form
(1NF). Justify your answer and write all rules of INF
b. Convert the given relation into 1NF.
c. Identify the primary key(s) in the normalized relation.
Synopti   a. Step 1: Find Candidate Keys
c
A candidate key is a minimal set of attributes whose closure gives all
attributes (A, B, C, D).
Check (AB)⁺
(AB)+={A,B}(AB)^+ = \{A, B\}(AB)+={A,B}
Using FD:
********** 6 **********
--- page 7 ---
• AB → CD ⇒ add C, D
(AB)+={A,B,C,D}(AB)^+ = \{A, B, C, D\}(AB)+={A,B,C,D}
Covers all attributes
AB is a candidate key
Check (AD)⁺
(AD)+={A,D}(AD)^+ = \{A, D\}(AD)+={A,D}
Using FDs:
• D → B ⇒ add B
• Now we have A, B, D
• AB → CD ⇒ add C, D
(AD)+={A,B,C,D}(AD)^+ = \{A, B, C, D\}(AD)+={A,B,C,D}
Covers all attributes
AD is a candidate key
Check (BC)⁺
(BC)+={B,C}(BC)^+ = \{B, C\}(BC)+={B,C}
Using FDs:
• C → A ⇒ add A
• Now we have A, B, C
• AB → CD ⇒ add C, D
(BC)+={A,B,C,D}(BC)^+ = \{A, B, C, D\}(BC)+={A,B,C,D}
Covers all attributes
BC is a candidate key
Check (CD)⁺
(CD)+={C,D}(CD)^+ = \{C, D\}(CD)+={C,D}
Using FDs:
• C → A ⇒ add A
• D → B ⇒ add B
(CD)+={A,B,C,D}(CD)^+ = \{A, B, C, D\}(CD)+={A,B,C,D}
Covers all attributes
CD is a candidate key
Step 2: Check Minimality
All keys:
•   AB, AD, BC, CD
None of their subsets determine all attributes
All are minimal
Final Answer (Model Answer)
Candidate Keys:
{AB, AD, BC, CD}\{AB,\ AD,\ BC,\ CD\}{AB, AD, BC, CD}
b 1. Checking Normal Form
The given relation is NOT in 1NF.
Reason:
********** 7 **********
--- page 8 ---
• The attribute Projects contains multiple values (e.g., "AI,
DBMS").
• 1NF requires all attributes to have atomic (single) values.
2. Conversion to 1NF
To convert into 1NF, we eliminate repeating groups and create
separate rows for each project.
Normalized Relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Project)
3. Primary Key = (EmpID, Project)
CO2;   b   [10]
SO-1;   Explain the different types of outer joins in SQL and write the
BL-3;   corresponding SQL statement syntax.
Synopti   Outer joins are used to retrieve matching records along with non-
c   matching records from one or both tables.
Types of Outer Joins
1. LEFT OUTER JOIN
• Returns all records from the left table and matching records
from the right table
•   If no match, NULL values are returned for the right table
SELECT column_list
FROM table1
LEFT OUTER JOIN table2
ON table1.common_column = table2.common_column;
2. RIGHT OUTER JOIN
• Returns all records from the right table and matching records
from the left table
•   If no match, NULL values are returned for the left table
SELECT column_list
FROM table1
RIGHT OUTER JOIN table2
ON table1.common_column = table2.common_column;
3. FULL OUTER JOIN
• Returns all records from both tables
• NULL values are returned where there is no match
SELECT column_list
********** 8 **********

[Text in pictures on this page, read by OCR]
EmpID_ | EmpName | Project

E101 Raj Al
E101 Raj DBMS
E102 Simran ML
E103 Karan Al
E103 Karan ML

E103 Karan Cloud
--- page 9 ---
FROM table1
FULL OUTER JOIN table2
ON table1.common_column = table2.common_column;
Q4   a   What is Data model? Explain the Relational Data model with example. [10]
CO-3;
SO-1;
BL-2
Synopti   A data model is a collection of concepts used to describe the structure
c   of a database, including data, relationships, constraints, and semantics.
Relational Data Model
The Relational Data Model organizes data in the form of tables
(relations) consisting of rows (tuples) and columns (attributes).
Key Concepts
• Relation (Table): Collection of data organized in rows and
columns
• Tuple (Row): A single record in a table
• Attribute (Column): A property of an entity
• Domain: Set of valid values for an attribute
• Primary Key: Uniquely identifies each record
Student_ID Name   Age   Course
101   Asha   20   CS
102   Ravi   21   IT
103   Neha   19   CS
Explanation
• Table name = Student (Relation)
• Each row = Tuple
• Columns = Attributes (Student_ID, Name, Age, Course)
• Student_ID acts as the Primary Key
The relational model is widely used because it is simple, flexible, and
supports powerful querying using SQL.
Q4   b   Explain the concept of database users? Give the roles and [10]
CO1;   responsibilities of a DBA.
SO-1;
BL-2;
Synopti   Database users are individuals or applications that interact with the
c   database system to store, retrieve, and manage data.
Types of Database Users
1. Naive Users
o Use predefined applications
o Example: Bank customers using ATM
2. Application Programmers
o Write programs to interact with DBMS
o Use SQL and programming languages
********** 9 **********
--- page 10 ---
3. Sophisticated Users
o Use advanced queries for analysis
o Example: Data analysts
4. Database Administrator (DBA)
o Manages and controls the entire database system
Roles and Responsibilities of DBA
1. Database Design
o Define database structure, schema, and relationships
2. Security Management
o Control user access and permissions
3. Backup and Recovery
o Ensure data backup and restore in case of failure
4. Performance Tuning
o Optimize queries and database performance
5. Data Integrity Maintenance
o Enforce constraints and ensure data accuracy
6. User Management
o Create and manage user accounts
7. Monitoring and Maintenance
o Regularly monitor database health and fix issues
Consider a relation R (A, B, C, D) with the following set of functional
dependencies:
FD: {A → B, B → C}
Answer the following:
1. Determine the highest normal form satisfied by the relation and
Q5   justify your answer   [10]
CO3 ;   a   2. Decompose given relation up to 2NF
SO-2 ;
BL-4;
Synopti
c   Step 1: Find Candidate Key(s)
Compute closure of A:
A+={A}A+={A}
Using FDs:
A → B ⇒ add B
B → C ⇒ add C
A+= {A, B, C} A+={A,B,C}
D is missing, so include D
(AD)+={A,D}(AD)+={A,D}
Using FDs:
A → B ⇒ add B
B → C ⇒ add C
(AD)+={A,B,C,D}(AD)+={A,B,C,D}
✔Covers all attributes
Candidate Key: {AD}
1. Highest Normal Form
********** 10 **********
--- page 11 ---
Check 1NF:
All attributes are atomic
Relation is in 1NF
Check 2NF:
Candidate Key = (A, D)
Check for partial dependency:
A → B (A is part of key → partial dependency)
B → C (transitive, but still depends on A indirectly)
Partial dependency exists
Violates 2NF
Check 3NF:
A → B, B → C ⇒ A → C (transitive dependency)
Violates 3NF
Highest Normal Form: 1NF
2. Decomposition into 2NF
Step: Remove partial dependency (A → B)
Create Relations:
R1 (A, B)
From FD: A → B
A is key here
R2 (A, C, D)
Remaining attributes
Check R2 for dependencies:
A → C (since A → B and B → C)
Further decomposition:
R2A (A, C)
A → C
R2B (A, D)
No non-key dependency
Final 2NF Relations
R1 (A, B)
R2A (A, C)
R2B (A, D)
Final Conclusion
Candidate Key: {A, D}
Highest Normal Form: 1NF
After decomposition, relation is in 2NF with:
No partial dependencies
Improved data integrity
CO4;   b   Differentiate between Data Definition Language (DDL) and Data   [10]
SO- 1;   Manipulation Language (DML) in SQL. Provide two commands from
BL-2;   each category along with their syntax.
Synopti   Basis   DDL (Data Definition   DML (Data
c   Language)   Manipulation
Language)
Purpos   Defines and modifies   Manipulates data in
e   database structure   tables
Operati Works on schema (tables,   Works on data (records)
on   structure)
********** 11 **********
--- page 12 ---
Auto   Auto-committed (cannot be   Can be rolled back
Commi   rolled back easily)
t
Exampl CREATE, ALTER, DROP   INSERT, UPDATE,
es   DELETE
Usage   Used during database design   Used during data
handling
DDL Commands (Any Two)
1. CREATE Command
• Used to create a new table
CREATE TABLE Student (
Student_ID INT,
Name VARCHAR(50),
Age INT
);
2. ALTER Command
• Used to modify an existing table
ALTER TABLE Student
ADD Address VARCHAR(100);
DML Commands (Any Two)
1. INSERT Command
• Used to add new records
INSERT INTO Student (Student_ID, Name, Age)
VALUES (101, 'Asha', 20);
2. UPDATE Command
• Used to modify existing records
UPDATE Student
SET Age = 21
WHERE Student_ID = 101;
Q6   a Unit-2   Convert the given ER diagram into relational table and identify the [10]
CO-   relations, attributes primary and foreign keys.
1,2;
SO-1;
BL-3;
********** 12 **********
--- page 13 ---
Synopti
c
CO-4;   b Unit-4   Based on the following schema of the tables, write the SQL statements [10]
SO-2;   for the given queries.
BL-4 ;   Student (student_id, name, age, marks, dept_id)
Department (dept_id, dept_name
a) Display names of students whose names 2nd characters is ‘a’.
b) Find the department-wise average marks where average marks
are greater than 75.
c) Find students whose marks are between 70 and 90.
d) Display student names along with their department names.
e) Display all departments along with student names (include
departments with no students).
Synopti   a. SELECT name FROM STUDENT WHERE name LIKE '_a%';
c   b. SELECT   dept_id, AVG(marks) AS avg_marks FROM
STUDENT
GROUP BY dept_id HAVING AVG(marks) > 75;
c. SELECT * FROM STUDENT WHERE marks BETWEEN 70
AND 90;
d. SELECT s.name, d.dept_name FROM STUDENT s INNER
JOIN DEPARTMENT d ON s.dept_id = d.dept_id;
e. SELECT d.dept_name, s.name FROM DEPARTMENT d LEFT
JOIN STUDENT s ON d.dept_id = s.dept_id;
Q7   a   a) Consider the following two tables from a college database and   [10]
CO3,4;   perform the Natural join and Left outer join operation and
SO-   show the resultant table with count the records.
Student   Department
1;BL-
4;   SID Name   DeptID
1   Asha   10
2   Ravi   20
3   Neha   10
4   Kiran   30
5   Amit   NULL
********** 13 **********

[Text in pictures on this page, read by OCR]
In Many-to-One relationship, two tables will be required-
AR (al ,a2,bl )
B( bl, b2)

NOTE = Here, combined table will be drawn for the entity set A and relationship set R.
--- page 14 ---
b) Define the term Data Redundancy and Data inconsistency.
DeptI
DeptName HOD
D
10   CS   Dr. Rao
10   CS   Dr. Rao
Dr.
20   IT
Mehta
Dr.
40   EXTC
Shah
NULL NA   NA
Synopti   Natural Join =5
c
Left Join=7
b) Data Redundancy: If same data stored in multiple places in same or
different tables it is called Data Redundancy.
Data Inconsistency: When same copies of data have different values in
different place then it is called Data Inconsistency
Due to redundancy table size will be increase it require large memory,
search time increases, System will slow, not very efficient.
********** 14 **********

[Text in pictures on this page, read by OCR]
SID Name S.DeptID | D.DeptID | DeptName | HOD

1 Asha 10 10 cs Dr. Rao

1 Asha 10 10 cs Dr. Rao

3 Neha 10 10 cs Dr. Rao

3 Neha 10 10 cs Dr. Rao

2 Ravi 20 20 IT Dr. Mehta
4 Kiran 30 NULL NULL NULL

5 Amit NULL NULL NULL NULL
--- page 15 ---
CO5;   b   What is NoSQL, and how does it differ from traditional relational [10]
SO- 1;   databases?
BL-4;
Synopti   NoSQL (Not Only SQL) refers to a class of database systems designed
c   to handle large volumes of unstructured or semi-structured data
and provide high scalability and flexibility.
Unlike traditional databases, NoSQL does not rely strictly on tables
and fixed schemas.
Difference between NoSQL and Relational Databases
Basis   NoSQL Database   Relational Database
(RDBMS)
Data   Non-tabular (Key-Value,   Tabular (tables with
Model   Document, Column,   rows & columns)
Graph)
Schema   Flexible / Dynamic schema Fixed / Predefined
schema
Scalabili Horizontally scalable   Vertically scalable
ty   (scale-out)   (scale-up)
Data   Handles unstructured &   Handles structured
Type   semi-structured data   data
Query   No standard query   Uses SQL
Languag language
e
Perform High performance for big   Suitable for complex
ance   data & real-time apps   queries & transactions
Example MongoDB, Cassandra   MySQL, Oracle
s
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 94656aae9e49

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/Introduction to Database Management System/ANS_Introduction to Database Management System(701CO0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Database Management System
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
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
Synopti   Basis   File System   DBMS
c   1. Data   High redundancy   Reduced redundancy due to
Redundanc   (duplicate data   centralized control
y   exists)
2. Data   Poor consistency   High consistency
Consistenc   (data mismatch   maintained
y   possible)
3. Data   Limited data   Easy data sharing among
Sharing   sharing   multiple users
4. Data   Less secure   Strong security mechanisms
Security   (authentication,
authorization)
5. Data   No data   Provides logical & physical
Independe   independence   data independence
nce
6. Query   No query language   Uses SQL for efficient data
Processing   support   retrieval
7. Backup   Difficult and   Automatic backup and
&   manual   recovery features
Recovery
********** 1 **********
--- page 2 ---
CO-2,   b.   Describe the following terms with examples: i) Weak Entity ii) [5]
SO-1   Multivalued Attributes
BL-2
Synopti   i) Weak Entity
c   A weak entity is an entity that does not have a primary key of its own
and depends on a strong entity for its identification.
Key Points:
• Cannot be uniquely identified by its own attributes
• Depends on a strong (owner) entity
• Has a partial key (discriminator)
• Represented by double rectangle in ER diagram
Example:
• Employee (Strong Entity) → has Employee_ID
• Dependent (Weak Entity) → attributes: Name, Age
Here, a dependent is identified by:
(Employee_ID + Dependent_Name)
ii) Multivalued Attribute
A multivalued attribute is an attribute that can have multiple values
for a single entity.
Key Points:
•   Stores more than one value
• Represented by double oval in ER diagram
Example:
• Student Entity
o Name: John
o Phone Numbers: 9876543210, 9123456780
Here, Phone_Number is a multivalued attribute.
CO-3;   c.   Explain the concept of normalization in Database Management Systems [5]
SO-1   and discuss the objectives of normalization.
BL- 2;
Synopti   Normalization is the process of organizing data in a database to reduce
c   redundancy and improve data integrity by dividing large tables into
smaller, well-structured tables and defining relationships between
them.
Objectives of Normalization
1. Eliminate Data Redundancy – Avoid duplicate data storage.
2. Ensure Data Consistency – Maintain uniform and accurate
data.
3. Improve Data Integrity – Enforce correct relationships using
keys and constraints.
4. Avoid Anomalies – Prevent insertion, deletion, and update
anomalies.
5. Efficient Data Organization – Structure data logically for
better management.
********** 2 **********
--- page 3 ---
Normalization helps in creating a clean, efficient, and reliable
database structure.
CO-4;   d.   What is constraint in SQL. Explain any two constraints with example.   [5]
SO-1 ;
BL- 2;
Synopti   A constraint in SQL is a rule applied to a table or column to restrict
c   the type of data that can be inserted, updated, or deleted, ensuring data
accuracy and integrity.
1. PRIMARY KEY Constraint
• Uniquely identifies each record in a table
• Cannot contain NULL values
• Each table can have only one primary key
2. FOREIGN KEY Constraint
• Used to link two tables
• Ensures referential integrity
• Value must match a value in the referenced table
Q2   a   Discuss the three-schema architecture of DBMS and explain the role of [10]
CO-1;   each level.
SO-1;
BL-2;
Synopti   The three-schema architecture ensures data abstraction, security, and
c   independence, making DBMS flexible and efficient.
Levels of Three-Schema Architecture
1. External Level (View Level)
• Represents how end users view the data
• Each user can have a different view of the same database
• Focuses only on required data
Example:A student sees only Name and Marks, while an admin sees
full student details.
2. Conceptual Level (Logical Level)
• Describes the overall structure of the database
•   Includes entities, relationships, constraints
• Independent of physical storage
Example:Defines tables like Student (ID, Name, Marks) and their
relationships.
Internal Level (Physical Level)
• Describes how data is actually stored in the system
•   Includes file structure, indexing, storage methods
Example:Data stored in files using indexes, hashing, etc.
Role of Each Level
• External Level: Provides customized views and security
• Conceptual Level: Maintains logical structure and relationships
• Internal Level: Handles efficient storage and retrieval
********** 3 **********
--- page 4 ---
CO2;S   b   Design an ER diagram for the given scenario and convert it into [10]
O-   relational tables.
1;BL-
A hospital plans to develop a database system to manage information
4;
about departments, doctors, and patients.
Each department has a unique dept_ID, dept_name, and location.
Every department employs multiple doctors.
Each doctor has a unique doctor_ID, doctor_name, expertise, and phone
number. A doctor works in exactly one department.
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
4. Convert the ER diagram into relational tables with primary and
foreign keys.
Synopti   1. ER Diagram Design (Textual Representation)
c
Entities & Attributes
1. Department (Strong Entity)
• dept_ID (PK)
• dept_name
•   location
2. Doctor (Strong Entity)
• doctor_ID (PK)
• doctor_name
•   expertise
• phone
3. Patient (Strong Entity)
• patient_ID (PK)
• patient_name (Composite: f_name, l_name)
********** 4 **********
--- page 5 ---
• DOB
• age
•   address
• phone (Multivalued)
4. Attendant (Weak Entity)
• A_Name (Partial Key)
•   relation
• phone
•   address
2. Relationships
1. Department – Doctor
o Relationship: Employs
o 1 : N (One department → many doctors)
o Total participation of Doctor
2. Department – Patient
o Relationship: Assigned_To
o 1 : N (One department → many patients)
o Total participation of Patient
3. Doctor – Patient
o Relationship: Consults
o M : N
4. Patient – Attendant
o Relationship: Has
o 1 : N (One patient → many attendants)
o Total participation of Attendant (weak entity)
3. Cardinality & Participation Constraints
Relationship   Cardinal   Participation
ity
Department–   1 : N   Doctor → Total
Doctor
Department–   1 : N   Patient → Total
Patient
Doctor–Patient M : N   Partial
Patient–   1 : N   Attendant →
Attendant   Total
4. Special Attributes
• Composite Attribute: patient_name → (f_name, l_name)
• Multivalued Attribute: Patient → phone
• Weak Entity: Attendant (depends on Patient)
********** 5 **********
--- page 6 ---
Q3   a   a. Find all the candidate keys of a given relation.   [10]
CO- 3;   R (A, B, C, D)
SO-;   Functional Dependency (FD): {AB->CD, D->B, C->A}
BL4-;
b. Consider the following relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Projects)
EmpID   EmpName   Projects
E101   Raj   AI, DBMS
E102   Simran   ML
E103   Karan   AI, ML, Cloud
Perform the given tasks:
a. Identify whether the given relation is in First Normal Form
(1NF). Justify your answer and write all rules of INF
b. Convert the given relation into 1NF.
c. Identify the primary key(s) in the normalized relation.
Synopti   a. Step 1: Find Candidate Keys
c
A candidate key is a minimal set of attributes whose closure gives all
attributes (A, B, C, D).
Check (AB)⁺
(AB)+={A,B}(AB)^+ = \{A, B\}(AB)+={A,B}
Using FD:
********** 6 **********
--- page 7 ---
• AB → CD ⇒ add C, D
(AB)+={A,B,C,D}(AB)^+ = \{A, B, C, D\}(AB)+={A,B,C,D}
Covers all attributes
AB is a candidate key
Check (AD)⁺
(AD)+={A,D}(AD)^+ = \{A, D\}(AD)+={A,D}
Using FDs:
• D → B ⇒ add B
• Now we have A, B, D
• AB → CD ⇒ add C, D
(AD)+={A,B,C,D}(AD)^+ = \{A, B, C, D\}(AD)+={A,B,C,D}
Covers all attributes
AD is a candidate key
Check (BC)⁺
(BC)+={B,C}(BC)^+ = \{B, C\}(BC)+={B,C}
Using FDs:
• C → A ⇒ add A
• Now we have A, B, C
• AB → CD ⇒ add C, D
(BC)+={A,B,C,D}(BC)^+ = \{A, B, C, D\}(BC)+={A,B,C,D}
Covers all attributes
BC is a candidate key
Check (CD)⁺
(CD)+={C,D}(CD)^+ = \{C, D\}(CD)+={C,D}
Using FDs:
• C → A ⇒ add A
• D → B ⇒ add B
(CD)+={A,B,C,D}(CD)^+ = \{A, B, C, D\}(CD)+={A,B,C,D}
Covers all attributes
CD is a candidate key
Step 2: Check Minimality
All keys:
•   AB, AD, BC, CD
None of their subsets determine all attributes
All are minimal
Final Answer (Model Answer)
Candidate Keys:
{AB, AD, BC, CD}\{AB,\ AD,\ BC,\ CD\}{AB, AD, BC, CD}
b 1. Checking Normal Form
The given relation is NOT in 1NF.
Reason:
********** 7 **********
--- page 8 ---
• The attribute Projects contains multiple values (e.g., "AI,
DBMS").
• 1NF requires all attributes to have atomic (single) values.
2. Conversion to 1NF
To convert into 1NF, we eliminate repeating groups and create
separate rows for each project.
Normalized Relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Project)
3. Primary Key = (EmpID, Project)
CO2;   b   [10]
SO-1;   Explain the different types of outer joins in SQL and write the
BL-3;   corresponding SQL statement syntax.
Synopti   Outer joins are used to retrieve matching records along with non-
c   matching records from one or both tables.
Types of Outer Joins
1. LEFT OUTER JOIN
• Returns all records from the left table and matching records
from the right table
•   If no match, NULL values are returned for the right table
SELECT column_list
FROM table1
LEFT OUTER JOIN table2
ON table1.common_column = table2.common_column;
2. RIGHT OUTER JOIN
• Returns all records from the right table and matching records
from the left table
•   If no match, NULL values are returned for the left table
SELECT column_list
FROM table1
RIGHT OUTER JOIN table2
ON table1.common_column = table2.common_column;
3. FULL OUTER JOIN
• Returns all records from both tables
• NULL values are returned where there is no match
SELECT column_list
********** 8 **********

[Text in pictures on this page, read by OCR]
EmpID_ | EmpName | Project

E101 Raj Al
E101 Raj DBMS
E102 Simran ML
E103 Karan Al
E103 Karan ML

E103 Karan Cloud
--- page 9 ---
FROM table1
FULL OUTER JOIN table2
ON table1.common_column = table2.common_column;
Q4   a   What is Data model? Explain the Relational Data model with example. [10]
CO-3;
SO-1;
BL-2
Synopti   A data model is a collection of concepts used to describe the structure
c   of a database, including data, relationships, constraints, and semantics.
Relational Data Model
The Relational Data Model organizes data in the form of tables
(relations) consisting of rows (tuples) and columns (attributes).
Key Concepts
• Relation (Table): Collection of data organized in rows and
columns
• Tuple (Row): A single record in a table
• Attribute (Column): A property of an entity
• Domain: Set of valid values for an attribute
• Primary Key: Uniquely identifies each record
Student_ID Name   Age   Course
101   Asha   20   CS
102   Ravi   21   IT
103   Neha   19   CS
Explanation
• Table name = Student (Relation)
• Each row = Tuple
• Columns = Attributes (Student_ID, Name, Age, Course)
• Student_ID acts as the Primary Key
The relational model is widely used because it is simple, flexible, and
supports powerful querying using SQL.
Q4   b   Explain the concept of database users? Give the roles and [10]
CO1;   responsibilities of a DBA.
SO-1;
BL-2;
Synopti   Database users are individuals or applications that interact with the
c   database system to store, retrieve, and manage data.
Types of Database Users
1. Naive Users
o Use predefined applications
o Example: Bank customers using ATM
2. Application Programmers
o Write programs to interact with DBMS
o Use SQL and programming languages
********** 9 **********
--- page 10 ---
3. Sophisticated Users
o Use advanced queries for analysis
o Example: Data analysts
4. Database Administrator (DBA)
o Manages and controls the entire database system
Roles and Responsibilities of DBA
1. Database Design
o Define database structure, schema, and relationships
2. Security Management
o Control user access and permissions
3. Backup and Recovery
o Ensure data backup and restore in case of failure
4. Performance Tuning
o Optimize queries and database performance
5. Data Integrity Maintenance
o Enforce constraints and ensure data accuracy
6. User Management
o Create and manage user accounts
7. Monitoring and Maintenance
o Regularly monitor database health and fix issues
Consider a relation R (A, B, C, D) with the following set of functional
dependencies:
FD: {A → B, B → C}
Answer the following:
1. Determine the highest normal form satisfied by the relation and
Q5   justify your answer   [10]
CO3 ;   a   2. Decompose given relation up to 2NF
SO-2 ;
BL-4;
Synopti
c   Step 1: Find Candidate Key(s)
Compute closure of A:
A+={A}A+={A}
Using FDs:
A → B ⇒ add B
B → C ⇒ add C
A+= {A, B, C} A+={A,B,C}
D is missing, so include D
(AD)+={A,D}(AD)+={A,D}
Using FDs:
A → B ⇒ add B
B → C ⇒ add C
(AD)+={A,B,C,D}(AD)+={A,B,C,D}
✔Covers all attributes
Candidate Key: {AD}
1. Highest Normal Form
********** 10 **********
--- page 11 ---
Check 1NF:
All attributes are atomic
Relation is in 1NF
Check 2NF:
Candidate Key = (A, D)
Check for partial dependency:
A → B (A is part of key → partial dependency)
B → C (transitive, but still depends on A indirectly)
Partial dependency exists
Violates 2NF
Check 3NF:
A → B, B → C ⇒ A → C (transitive dependency)
Violates 3NF
Highest Normal Form: 1NF
2. Decomposition into 2NF
Step: Remove partial dependency (A → B)
Create Relations:
R1 (A, B)
From FD: A → B
A is key here
R2 (A, C, D)
Remaining attributes
Check R2 for dependencies:
A → C (since A → B and B → C)
Further decomposition:
R2A (A, C)
A → C
R2B (A, D)
No non-key dependency
Final 2NF Relations
R1 (A, B)
R2A (A, C)
R2B (A, D)
Final Conclusion
Candidate Key: {A, D}
Highest Normal Form: 1NF
After decomposition, relation is in 2NF with:
No partial dependencies
Improved data integrity
CO4;   b   Differentiate between Data Definition Language (DDL) and Data   [10]
SO- 1;   Manipulation Language (DML) in SQL. Provide two commands from
BL-2;   each category along with their syntax.
Synopti   Basis   DDL (Data Definition   DML (Data
c   Language)   Manipulation
Language)
Purpos   Defines and modifies   Manipulates data in
e   database structure   tables
Operati Works on schema (tables,   Works on data (records)
on   structure)
********** 11 **********
--- page 12 ---
Auto   Auto-committed (cannot be   Can be rolled back
Commi   rolled back easily)
t
Exampl CREATE, ALTER, DROP   INSERT, UPDATE,
es   DELETE
Usage   Used during database design   Used during data
handling
DDL Commands (Any Two)
1. CREATE Command
• Used to create a new table
CREATE TABLE Student (
Student_ID INT,
Name VARCHAR(50),
Age INT
);
2. ALTER Command
• Used to modify an existing table
ALTER TABLE Student
ADD Address VARCHAR(100);
DML Commands (Any Two)
1. INSERT Command
• Used to add new records
INSERT INTO Student (Student_ID, Name, Age)
VALUES (101, 'Asha', 20);
2. UPDATE Command
• Used to modify existing records
UPDATE Student
SET Age = 21
WHERE Student_ID = 101;
Q6   a Unit-2   Convert the given ER diagram into relational table and identify the [10]
CO-   relations, attributes primary and foreign keys.
1,2;
SO-1;
BL-3;
********** 12 **********
--- page 13 ---
Synopti
c
CO-4;   b Unit-4   Based on the following schema of the tables, write the SQL statements [10]
SO-2;   for the given queries.
BL-4 ;   Student (student_id, name, age, marks, dept_id)
Department (dept_id, dept_name
a) Display names of students whose names 2nd characters is ‘a’.
b) Find the department-wise average marks where average marks
are greater than 75.
c) Find students whose marks are between 70 and 90.
d) Display student names along with their department names.
e) Display all departments along with student names (include
departments with no students).
Synopti   a. SELECT name FROM STUDENT WHERE name LIKE '_a%';
c   b. SELECT   dept_id, AVG(marks) AS avg_marks FROM
STUDENT
GROUP BY dept_id HAVING AVG(marks) > 75;
c. SELECT * FROM STUDENT WHERE marks BETWEEN 70
AND 90;
d. SELECT s.name, d.dept_name FROM STUDENT s INNER
JOIN DEPARTMENT d ON s.dept_id = d.dept_id;
e. SELECT d.dept_name, s.name FROM DEPARTMENT d LEFT
JOIN STUDENT s ON d.dept_id = s.dept_id;
Q7   a   a) Consider the following two tables from a college database and   [10]
CO3,4;   perform the Natural join and Left outer join operation and
SO-   show the resultant table with count the records.
Student   Department
1;BL-
4;   SID Name   DeptID
1   Asha   10
2   Ravi   20
3   Neha   10
4   Kiran   30
5   Amit   NULL
********** 13 **********

[Text in pictures on this page, read by OCR]
In Many-to-One relationship, two tables will be required-
AR (al ,a2,bl )
B( bl, b2)

NOTE = Here, combined table will be drawn for the entity set A and relationship set R.
--- page 14 ---
b) Define the term Data Redundancy and Data inconsistency.
DeptI
DeptName HOD
D
10   CS   Dr. Rao
10   CS   Dr. Rao
Dr.
20   IT
Mehta
Dr.
40   EXTC
Shah
NULL NA   NA
Synopti   Natural Join =5
c
Left Join=7
b) Data Redundancy: If same data stored in multiple places in same or
different tables it is called Data Redundancy.
Data Inconsistency: When same copies of data have different values in
different place then it is called Data Inconsistency
Due to redundancy table size will be increase it require large memory,
search time increases, System will slow, not very efficient.
********** 14 **********

[Text in pictures on this page, read by OCR]
SID Name S.DeptID | D.DeptID | DeptName | HOD

1 Asha 10 10 cs Dr. Rao

1 Asha 10 10 cs Dr. Rao

3 Neha 10 10 cs Dr. Rao

3 Neha 10 10 cs Dr. Rao

2 Ravi 20 20 IT Dr. Mehta
4 Kiran 30 NULL NULL NULL

5 Amit NULL NULL NULL NULL
--- page 15 ---
CO5;   b   What is NoSQL, and how does it differ from traditional relational [10]
SO- 1;   databases?
BL-4;
Synopti   NoSQL (Not Only SQL) refers to a class of database systems designed
c   to handle large volumes of unstructured or semi-structured data
and provide high scalability and flexibility.
Unlike traditional databases, NoSQL does not rely strictly on tables
and fixed schemas.
Difference between NoSQL and Relational Databases
Basis   NoSQL Database   Relational Database
(RDBMS)
Data   Non-tabular (Key-Value,   Tabular (tables with
Model   Document, Column,   rows & columns)
Graph)
Schema   Flexible / Dynamic schema Fixed / Predefined
schema
Scalabili Horizontally scalable   Vertically scalable
ty   (scale-out)   (scale-up)
Data   Handles unstructured &   Handles structured
Type   semi-structured data   data
Query   No standard query   Uses SQL
Languag language
e
Perform High performance for big   Suitable for complex
ance   data & real-time apps   queries & transactions
Example MongoDB, Cassandra   MySQL, Oracle
s
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 229aecc94acb

- Departments: Information Technology
- Programmes: DIPLOMA IN INFORMATION TECHNOLOGY - 7075
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN INFORMATION TECHNOLOGY - 7075/Introduction to Database Management System/ANS_Introduction to Database Management System(701CO0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Database Management System
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
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
Synopti   Basis   File System   DBMS
c   1. Data   High redundancy   Reduced redundancy due to
Redundanc   (duplicate data   centralized control
y   exists)
2. Data   Poor consistency   High consistency
Consistenc   (data mismatch   maintained
y   possible)
3. Data   Limited data   Easy data sharing among
Sharing   sharing   multiple users
4. Data   Less secure   Strong security mechanisms
Security   (authentication,
authorization)
5. Data   No data   Provides logical & physical
Independe   independence   data independence
nce
6. Query   No query language   Uses SQL for efficient data
Processing   support   retrieval
7. Backup   Difficult and   Automatic backup and
&   manual   recovery features
Recovery
********** 1 **********
--- page 2 ---
CO-2,   b.   Describe the following terms with examples: i) Weak Entity ii) [5]
SO-1   Multivalued Attributes
BL-2
Synopti   i) Weak Entity
c   A weak entity is an entity that does not have a primary key of its own
and depends on a strong entity for its identification.
Key Points:
• Cannot be uniquely identified by its own attributes
• Depends on a strong (owner) entity
• Has a partial key (discriminator)
• Represented by double rectangle in ER diagram
Example:
• Employee (Strong Entity) → has Employee_ID
• Dependent (Weak Entity) → attributes: Name, Age
Here, a dependent is identified by:
(Employee_ID + Dependent_Name)
ii) Multivalued Attribute
A multivalued attribute is an attribute that can have multiple values
for a single entity.
Key Points:
•   Stores more than one value
• Represented by double oval in ER diagram
Example:
• Student Entity
o Name: John
o Phone Numbers: 9876543210, 9123456780
Here, Phone_Number is a multivalued attribute.
CO-3;   c.   Explain the concept of normalization in Database Management Systems [5]
SO-1   and discuss the objectives of normalization.
BL- 2;
Synopti   Normalization is the process of organizing data in a database to reduce
c   redundancy and improve data integrity by dividing large tables into
smaller, well-structured tables and defining relationships between
them.
Objectives of Normalization
1. Eliminate Data Redundancy – Avoid duplicate data storage.
2. Ensure Data Consistency – Maintain uniform and accurate
data.
3. Improve Data Integrity – Enforce correct relationships using
keys and constraints.
4. Avoid Anomalies – Prevent insertion, deletion, and update
anomalies.
5. Efficient Data Organization – Structure data logically for
better management.
********** 2 **********
--- page 3 ---
Normalization helps in creating a clean, efficient, and reliable
database structure.
CO-4;   d.   What is constraint in SQL. Explain any two constraints with example.   [5]
SO-1 ;
BL- 2;
Synopti   A constraint in SQL is a rule applied to a table or column to restrict
c   the type of data that can be inserted, updated, or deleted, ensuring data
accuracy and integrity.
1. PRIMARY KEY Constraint
• Uniquely identifies each record in a table
• Cannot contain NULL values
• Each table can have only one primary key
2. FOREIGN KEY Constraint
• Used to link two tables
• Ensures referential integrity
• Value must match a value in the referenced table
Q2   a   Discuss the three-schema architecture of DBMS and explain the role of [10]
CO-1;   each level.
SO-1;
BL-2;
Synopti   The three-schema architecture ensures data abstraction, security, and
c   independence, making DBMS flexible and efficient.
Levels of Three-Schema Architecture
1. External Level (View Level)
• Represents how end users view the data
• Each user can have a different view of the same database
• Focuses only on required data
Example:A student sees only Name and Marks, while an admin sees
full student details.
2. Conceptual Level (Logical Level)
• Describes the overall structure of the database
•   Includes entities, relationships, constraints
• Independent of physical storage
Example:Defines tables like Student (ID, Name, Marks) and their
relationships.
Internal Level (Physical Level)
• Describes how data is actually stored in the system
•   Includes file structure, indexing, storage methods
Example:Data stored in files using indexes, hashing, etc.
Role of Each Level
• External Level: Provides customized views and security
• Conceptual Level: Maintains logical structure and relationships
• Internal Level: Handles efficient storage and retrieval
********** 3 **********
--- page 4 ---
CO2;S   b   Design an ER diagram for the given scenario and convert it into [10]
O-   relational tables.
1;BL-
A hospital plans to develop a database system to manage information
4;
about departments, doctors, and patients.
Each department has a unique dept_ID, dept_name, and location.
Every department employs multiple doctors.
Each doctor has a unique doctor_ID, doctor_name, expertise, and phone
number. A doctor works in exactly one department.
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
4. Convert the ER diagram into relational tables with primary and
foreign keys.
Synopti   1. ER Diagram Design (Textual Representation)
c
Entities & Attributes
1. Department (Strong Entity)
• dept_ID (PK)
• dept_name
•   location
2. Doctor (Strong Entity)
• doctor_ID (PK)
• doctor_name
•   expertise
• phone
3. Patient (Strong Entity)
• patient_ID (PK)
• patient_name (Composite: f_name, l_name)
********** 4 **********
--- page 5 ---
• DOB
• age
•   address
• phone (Multivalued)
4. Attendant (Weak Entity)
• A_Name (Partial Key)
•   relation
• phone
•   address
2. Relationships
1. Department – Doctor
o Relationship: Employs
o 1 : N (One department → many doctors)
o Total participation of Doctor
2. Department – Patient
o Relationship: Assigned_To
o 1 : N (One department → many patients)
o Total participation of Patient
3. Doctor – Patient
o Relationship: Consults
o M : N
4. Patient – Attendant
o Relationship: Has
o 1 : N (One patient → many attendants)
o Total participation of Attendant (weak entity)
3. Cardinality & Participation Constraints
Relationship   Cardinal   Participation
ity
Department–   1 : N   Doctor → Total
Doctor
Department–   1 : N   Patient → Total
Patient
Doctor–Patient M : N   Partial
Patient–   1 : N   Attendant →
Attendant   Total
4. Special Attributes
• Composite Attribute: patient_name → (f_name, l_name)
• Multivalued Attribute: Patient → phone
• Weak Entity: Attendant (depends on Patient)
********** 5 **********
--- page 6 ---
Q3   a   a. Find all the candidate keys of a given relation.   [10]
CO- 3;   R (A, B, C, D)
SO-;   Functional Dependency (FD): {AB->CD, D->B, C->A}
BL4-;
b. Consider the following relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Projects)
EmpID   EmpName   Projects
E101   Raj   AI, DBMS
E102   Simran   ML
E103   Karan   AI, ML, Cloud
Perform the given tasks:
a. Identify whether the given relation is in First Normal Form
(1NF). Justify your answer and write all rules of INF
b. Convert the given relation into 1NF.
c. Identify the primary key(s) in the normalized relation.
Synopti   a. Step 1: Find Candidate Keys
c
A candidate key is a minimal set of attributes whose closure gives all
attributes (A, B, C, D).
Check (AB)⁺
(AB)+={A,B}(AB)^+ = \{A, B\}(AB)+={A,B}
Using FD:
********** 6 **********
--- page 7 ---
• AB → CD ⇒ add C, D
(AB)+={A,B,C,D}(AB)^+ = \{A, B, C, D\}(AB)+={A,B,C,D}
Covers all attributes
AB is a candidate key
Check (AD)⁺
(AD)+={A,D}(AD)^+ = \{A, D\}(AD)+={A,D}
Using FDs:
• D → B ⇒ add B
• Now we have A, B, D
• AB → CD ⇒ add C, D
(AD)+={A,B,C,D}(AD)^+ = \{A, B, C, D\}(AD)+={A,B,C,D}
Covers all attributes
AD is a candidate key
Check (BC)⁺
(BC)+={B,C}(BC)^+ = \{B, C\}(BC)+={B,C}
Using FDs:
• C → A ⇒ add A
• Now we have A, B, C
• AB → CD ⇒ add C, D
(BC)+={A,B,C,D}(BC)^+ = \{A, B, C, D\}(BC)+={A,B,C,D}
Covers all attributes
BC is a candidate key
Check (CD)⁺
(CD)+={C,D}(CD)^+ = \{C, D\}(CD)+={C,D}
Using FDs:
• C → A ⇒ add A
• D → B ⇒ add B
(CD)+={A,B,C,D}(CD)^+ = \{A, B, C, D\}(CD)+={A,B,C,D}
Covers all attributes
CD is a candidate key
Step 2: Check Minimality
All keys:
•   AB, AD, BC, CD
None of their subsets determine all attributes
All are minimal
Final Answer (Model Answer)
Candidate Keys:
{AB, AD, BC, CD}\{AB,\ AD,\ BC,\ CD\}{AB, AD, BC, CD}
b 1. Checking Normal Form
The given relation is NOT in 1NF.
Reason:
********** 7 **********
--- page 8 ---
• The attribute Projects contains multiple values (e.g., "AI,
DBMS").
• 1NF requires all attributes to have atomic (single) values.
2. Conversion to 1NF
To convert into 1NF, we eliminate repeating groups and create
separate rows for each project.
Normalized Relation:
EMPLOYEE_PROJECT (EmpID, EmpName, Project)
3. Primary Key = (EmpID, Project)
CO2;   b   [10]
SO-1;   Explain the different types of outer joins in SQL and write the
BL-3;   corresponding SQL statement syntax.
Synopti   Outer joins are used to retrieve matching records along with non-
c   matching records from one or both tables.
Types of Outer Joins
1. LEFT OUTER JOIN
• Returns all records from the left table and matching records
from the right table
•   If no match, NULL values are returned for the right table
SELECT column_list
FROM table1
LEFT OUTER JOIN table2
ON table1.common_column = table2.common_column;
2. RIGHT OUTER JOIN
• Returns all records from the right table and matching records
from the left table
•   If no match, NULL values are returned for the left table
SELECT column_list
FROM table1
RIGHT OUTER JOIN table2
ON table1.common_column = table2.common_column;
3. FULL OUTER JOIN
• Returns all records from both tables
• NULL values are returned where there is no match
SELECT column_list
********** 8 **********

[Text in pictures on this page, read by OCR]
EmpID_ | EmpName | Project

E101 Raj Al
E101 Raj DBMS
E102 Simran ML
E103 Karan Al
E103 Karan ML

E103 Karan Cloud
--- page 9 ---
FROM table1
FULL OUTER JOIN table2
ON table1.common_column = table2.common_column;
Q4   a   What is Data model? Explain the Relational Data model with example. [10]
CO-3;
SO-1;
BL-2
Synopti   A data model is a collection of concepts used to describe the structure
c   of a database, including data, relationships, constraints, and semantics.
Relational Data Model
The Relational Data Model organizes data in the form of tables
(relations) consisting of rows (tuples) and columns (attributes).
Key Concepts
• Relation (Table): Collection of data organized in rows and
columns
• Tuple (Row): A single record in a table
• Attribute (Column): A property of an entity
• Domain: Set of valid values for an attribute
• Primary Key: Uniquely identifies each record
Student_ID Name   Age   Course
101   Asha   20   CS
102   Ravi   21   IT
103   Neha   19   CS
Explanation
• Table name = Student (Relation)
• Each row = Tuple
• Columns = Attributes (Student_ID, Name, Age, Course)
• Student_ID acts as the Primary Key
The relational model is widely used because it is simple, flexible, and
supports powerful querying using SQL.
Q4   b   Explain the concept of database users? Give the roles and [10]
CO1;   responsibilities of a DBA.
SO-1;
BL-2;
Synopti   Database users are individuals or applications that interact with the
c   database system to store, retrieve, and manage data.
Types of Database Users
1. Naive Users
o Use predefined applications
o Example: Bank customers using ATM
2. Application Programmers
o Write programs to interact with DBMS
o Use SQL and programming languages
********** 9 **********
--- page 10 ---
3. Sophisticated Users
o Use advanced queries for analysis
o Example: Data analysts
4. Database Administrator (DBA)
o Manages and controls the entire database system
Roles and Responsibilities of DBA
1. Database Design
o Define database structure, schema, and relationships
2. Security Management
o Control user access and permissions
3. Backup and Recovery
o Ensure data backup and restore in case of failure
4. Performance Tuning
o Optimize queries and database performance
5. Data Integrity Maintenance
o Enforce constraints and ensure data accuracy
6. User Management
o Create and manage user accounts
7. Monitoring and Maintenance
o Regularly monitor database health and fix issues
Consider a relation R (A, B, C, D) with the following set of functional
dependencies:
FD: {A → B, B → C}
Answer the following:
1. Determine the highest normal form satisfied by the relation and
Q5   justify your answer   [10]
CO3 ;   a   2. Decompose given relation up to 2NF
SO-2 ;
BL-4;
Synopti
c   Step 1: Find Candidate Key(s)
Compute closure of A:
A+={A}A+={A}
Using FDs:
A → B ⇒ add B
B → C ⇒ add C
A+= {A, B, C} A+={A,B,C}
D is missing, so include D
(AD)+={A,D}(AD)+={A,D}
Using FDs:
A → B ⇒ add B
B → C ⇒ add C
(AD)+={A,B,C,D}(AD)+={A,B,C,D}
✔Covers all attributes
Candidate Key: {AD}
1. Highest Normal Form
********** 10 **********
--- page 11 ---
Check 1NF:
All attributes are atomic
Relation is in 1NF
Check 2NF:
Candidate Key = (A, D)
Check for partial dependency:
A → B (A is part of key → partial dependency)
B → C (transitive, but still depends on A indirectly)
Partial dependency exists
Violates 2NF
Check 3NF:
A → B, B → C ⇒ A → C (transitive dependency)
Violates 3NF
Highest Normal Form: 1NF
2. Decomposition into 2NF
Step: Remove partial dependency (A → B)
Create Relations:
R1 (A, B)
From FD: A → B
A is key here
R2 (A, C, D)
Remaining attributes
Check R2 for dependencies:
A → C (since A → B and B → C)
Further decomposition:
R2A (A, C)
A → C
R2B (A, D)
No non-key dependency
Final 2NF Relations
R1 (A, B)
R2A (A, C)
R2B (A, D)
Final Conclusion
Candidate Key: {A, D}
Highest Normal Form: 1NF
After decomposition, relation is in 2NF with:
No partial dependencies
Improved data integrity
CO4;   b   Differentiate between Data Definition Language (DDL) and Data   [10]
SO- 1;   Manipulation Language (DML) in SQL. Provide two commands from
BL-2;   each category along with their syntax.
Synopti   Basis   DDL (Data Definition   DML (Data
c   Language)   Manipulation
Language)
Purpos   Defines and modifies   Manipulates data in
e   database structure   tables
Operati Works on schema (tables,   Works on data (records)
on   structure)
********** 11 **********
--- page 12 ---
Auto   Auto-committed (cannot be   Can be rolled back
Commi   rolled back easily)
t
Exampl CREATE, ALTER, DROP   INSERT, UPDATE,
es   DELETE
Usage   Used during database design   Used during data
handling
DDL Commands (Any Two)
1. CREATE Command
• Used to create a new table
CREATE TABLE Student (
Student_ID INT,
Name VARCHAR(50),
Age INT
);
2. ALTER Command
• Used to modify an existing table
ALTER TABLE Student
ADD Address VARCHAR(100);
DML Commands (Any Two)
1. INSERT Command
• Used to add new records
INSERT INTO Student (Student_ID, Name, Age)
VALUES (101, 'Asha', 20);
2. UPDATE Command
• Used to modify existing records
UPDATE Student
SET Age = 21
WHERE Student_ID = 101;
Q6   a Unit-2   Convert the given ER diagram into relational table and identify the [10]
CO-   relations, attributes primary and foreign keys.
1,2;
SO-1;
BL-3;
********** 12 **********
--- page 13 ---
Synopti
c
CO-4;   b Unit-4   Based on the following schema of the tables, write the SQL statements [10]
SO-2;   for the given queries.
BL-4 ;   Student (student_id, name, age, marks, dept_id)
Department (dept_id, dept_name
a) Display names of students whose names 2nd characters is ‘a’.
b) Find the department-wise average marks where average marks
are greater than 75.
c) Find students whose marks are between 70 and 90.
d) Display student names along with their department names.
e) Display all departments along with student names (include
departments with no students).
Synopti   a. SELECT name FROM STUDENT WHERE name LIKE '_a%';
c   b. SELECT   dept_id, AVG(marks) AS avg_marks FROM
STUDENT
GROUP BY dept_id HAVING AVG(marks) > 75;
c. SELECT * FROM STUDENT WHERE marks BETWEEN 70
AND 90;
d. SELECT s.name, d.dept_name FROM STUDENT s INNER
JOIN DEPARTMENT d ON s.dept_id = d.dept_id;
e. SELECT d.dept_name, s.name FROM DEPARTMENT d LEFT
JOIN STUDENT s ON d.dept_id = s.dept_id;
Q7   a   a) Consider the following two tables from a college database and   [10]
CO3,4;   perform the Natural join and Left outer join operation and
SO-   show the resultant table with count the records.
Student   Department
1;BL-
4;   SID Name   DeptID
1   Asha   10
2   Ravi   20
3   Neha   10
4   Kiran   30
5   Amit   NULL
********** 13 **********

[Text in pictures on this page, read by OCR]
In Many-to-One relationship, two tables will be required-
AR (al ,a2,bl )
B( bl, b2)

NOTE = Here, combined table will be drawn for the entity set A and relationship set R.
--- page 14 ---
b) Define the term Data Redundancy and Data inconsistency.
DeptI
DeptName HOD
D
10   CS   Dr. Rao
10   CS   Dr. Rao
Dr.
20   IT
Mehta
Dr.
40   EXTC
Shah
NULL NA   NA
Synopti   Natural Join =5
c
Left Join=7
b) Data Redundancy: If same data stored in multiple places in same or
different tables it is called Data Redundancy.
Data Inconsistency: When same copies of data have different values in
different place then it is called Data Inconsistency
Due to redundancy table size will be increase it require large memory,
search time increases, System will slow, not very efficient.
********** 14 **********

[Text in pictures on this page, read by OCR]
SID Name S.DeptID | D.DeptID | DeptName | HOD

1 Asha 10 10 cs Dr. Rao

1 Asha 10 10 cs Dr. Rao

3 Neha 10 10 cs Dr. Rao

3 Neha 10 10 cs Dr. Rao

2 Ravi 20 20 IT Dr. Mehta
4 Kiran 30 NULL NULL NULL

5 Amit NULL NULL NULL NULL
--- page 15 ---
CO5;   b   What is NoSQL, and how does it differ from traditional relational [10]
SO- 1;   databases?
BL-4;
Synopti   NoSQL (Not Only SQL) refers to a class of database systems designed
c   to handle large volumes of unstructured or semi-structured data
and provide high scalability and flexibility.
Unlike traditional databases, NoSQL does not rely strictly on tables
and fixed schemas.
Difference between NoSQL and Relational Databases
Basis   NoSQL Database   Relational Database
(RDBMS)
Data   Non-tabular (Key-Value,   Tabular (tables with
Model   Document, Column,   rows & columns)
Graph)
Schema   Flexible / Dynamic schema Fixed / Predefined
schema
Scalabili Horizontally scalable   Vertically scalable
ty   (scale-out)   (scale-up)
Data   Handles unstructured &   Handles structured
Type   semi-structured data   data
Query   No standard query   Uses SQL
Languag language
e
Perform High performance for big   Suitable for complex
ance   data & real-time apps   queries & transactions
Example MongoDB, Cassandra   MySQL, Oracle
s
********** 15 **********
````
