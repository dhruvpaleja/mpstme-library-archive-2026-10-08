# Database Management Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper f09131631dc5

- Departments: Commerce
- Programmes: Bachelor of Commerce - 45611
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Final-Exam/Bachelor of Commerce - 45611/Database Management Systems/ANS_Final-Exam_Database Management Systems(NADBM105)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 30; duration hours: 1; exam date: 15 Oct 2025
- Text: text (5 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Commerce
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 15 Oct 2025   Time: 11:30 am - 12:30 pm (01:00 Hrs.)
Max Marks: 30
FINAL EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 5 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
5. All questions are compulsory.
1.   Answer the following question.(Attempt Any 2 Questions)   15
A. (CREATE TABLE 4.5 MKS, ALTER TABLE 1.5 MKS EACH)   7.5
(i)
CREATE TABLE ACCOUNT
(acc_no SMALLINT NOT NULL PRIMARY KEY,
cust_name VARCHAR(22),
account_type VARCHAR(10),
open_date DATE,
balance DECIMAL(9, 2),
status CHAR(1));
(ii) Change data type of balance column to 10 integers 2 decimals
ALTER TABLE ACCOUNT
MODIFY balance decimal(12,2);
(iii) Delete status column
ALTER TABLE ACCOUNT
DROP COLUMN status;
B. Q(i)3mks Q (ii,iii,iv) 1.5 MKS EACH   7.5
Page 1 of 5
--- page 2 ---
(i) Insert 3 records in OFFICE table
INSERT INTO OFFICE (ANO, AccName, Type, Oyear, odate, balance) VALUES
(101, 'Ajay', 'Savings', 2022, '2022-06-10', 150000.00),
(102, 'Neha', 'Current', 2023, '2023-01-14', 90000.00),
(103, 'Suresh', 'Savings', 2021, '2021-11-21', 78000.00);
(ii) Change the account name to “Prakash” in the 3rd record
UPDATE OFFICE
SET AccName = 'Prakash'
WHERE ANO = 103;
(iii) Delete the 2nd row
DELETE FROM OFFICE
WHERE ANO = 102;
(iv) Change the balance of the 1st record to 82000
Page 2 of 5
--- page 3 ---
UPDATE OFFICE
SET balance = 82000.00
WHERE ANO = 101;
C.   7.5
2.   Answer the following question.(Attempt Any 2 Questions)   15
A. (1.5 marks each)   7.5
i. YEAR()
Extracts the year part from a date or datetime value.
YEAR(date)
Example:
SELECT YEAR('2025-09-22') AS YearPart;
ii. UPPER()
Converts all characters in a string to uppercase.
UPPER(string)
Page 3 of 5

[Text in pictures on this page, read by OCR]
)
SELECT WID, WNAME, JOIN DT FROM HCL ORDER BY JOIN_DT ASC;
ii)

SELECT WNAME, WAGE, (WAGE * 0.15) AS HRA FROM HCL;

iii)

SELECT * FROM HCL WHERE WAGE BETWEEN 30000 AND 60000;

iv)

SELECT * FROM HCL WHERE YEAR(JOIN_DT) = 2021;

v)
SELECT WID, WNAME FROM HCL WHERE WNAME LIKE '_ 1%';
--- page 4 ---
Example:
SELECT UPPER('mysql tutorial') AS UppercaseText;
iii. MIN()
Returns the minimum (smallest) value from a column (usually numeric or date).
SELECT MIN(column_name) FROM table_name;
Example:
SELECT MIN(salary) AS LowestSalary FROM employees;
iv. RIGHT()
Returns the rightmost N characters of a string.
RIGHT(string, number_of_characters)
Example:
SELECT RIGHT('MySQLDatabase', 8) AS RightPart;
v. AVG()
Calculates the average (mean) of numeric values in a column (ignores NULLs).
SELECT AVG(column_name) FROM table_name;
Example:
SELECT AVG(salary) AS AverageSalary FROM employees;
B. Each carries 2.5 marks   7.5
i) Display all courses starting between 01-Jan-2020 and 31-Dec-2024.
SELECT * FROM COURSES
WHERE SDATE BETWEEN '2020-01-01' AND '2024-12-31';
ii)
SELECT CNAME, DEPT, SDATE, ENR, FEE, (ENR * FEE) AS Total_Fee
FROM COURSES ;
iii)
SELECT CONCAT('The course ', CNAME, ' started on ', SDATE)
FROM COURSES;
C.   7.5
( 2.5 marks each)
i. SELECT PATIENT.PID, NAME, BP, FEVER
FROM PATIENT, DIAGNOSIS
Page 4 of 5
--- page 5 ---
WHERE PATIENT.PID = DIAGNOSIS.PID;
ii. SELECT NAME, BP
FROM PATIENT
WHERE PATIENT.PID = DIAGNOSIS.PID AND BP > 140;
iii. SELECT NAME, (BP + FEVER) AS SUM
FROM PATIENT, DIAGNOSIS
WHERE PATIENT.PID = DIAGNOSIS.PID;
Page 5 of 5
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 8db66a25892d

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Database Management Systems/ANS_Database Management Systems(703AI0C003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25 Nov 2025
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 25 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data whenever required (Please mentions such data in answer)
Section A: Attempt All Questions (Each Question Carries 5M)
Question 1
Describe the three levels of database architecture with an example.
Three-level architecture:
1. External Level: User views (e.g., student interface).
2. Conceptual Level: Logical schema of the entire DB.
3. Internal Level: Physical data storage (files, indexes).
CO 1;   Example: In a University DB, students view only their info (external), the
SO6;   A.   admin manages the schema (conceptual), and data is stored on disk   5M
BL2   (internal).
Mark Split:
• External Level – 1M
• Conceptual Level – 1M
• Internal Level – 1M
• Diagram - 1M
• Example (Bank DB, etc.) – 1M
Differentiate between strong and weak entities in an ER model with an
example.
CO 1;
SO6;   B.   5M
Strong Entity: Exists independently
BL2
(e.g., Student entity with diagram).
Weak Entity: Depends on a strong entity for identification
********** 1 **********
--- page 2 ---
(e.g., Dependent of Employee entity with diagram).
Differences: A weak entity has a partial key identified by the owner, which
is shown by a double rectangle in ERD.
Mark Split:
• Definition of Strong – 1M
• Definition of Weak – 2M
• Difference (3 points) – 1M
• Example – 1M
Analyse the difference between Join and Cartesian Product in relational
algebra with examples.
Cartesian Product (×): Combines all tuples (A×B).
Example with Tables and Query
Join (⋈): Combines tuples with matching attributes (condition-based).
Example with Tables and Query
CO 2;
SO1;   C.   5M
Compare: EMP × DEPT (m×n tuples); EMP ⋈ DEPT (only matching
BL4
dept_id).
Mark Split:
• Definition of Cartesian – 2M
• Definition of Join – 2M
• Difference – 1M
Analyse the differences between RDBMS and NoSQL in terms of data
structure, scalability, and consistency.
RDBMS: Tabular, normalised, vertically scalable, ACID consistency.
NoSQL: Document/key-value, horizontally scalable, eventual consistency.
CO 4;   Example: MySQL vs MongoDB.
SO7;   D.   5M
BL4
Mark Split: (Any four valid points 5M)
• Data structure – 1.5M
• Scalability – 1.5M
• Consistency – 1M
• Example – 1M
Section B: Attempt Any Four Questions from Questions 2 to 7 (Each Question Carries 20M)
********** 2 **********
--- page 3 ---
Question 2
CO 3;   A.   Define candidate key, Super key, and foreign key with examples. Also,   10M
SO1;   differentiate between a superkey and a candidate key.
BL4
Definition:
A super key is a set of one or more attributes that can uniquely identify each
record in a table.
It may contain extra attributes that are not necessary for uniqueness.
Example:
In STUDENT(StudentID, RollNo, Name, Email),
Super keys can be:
• {StudentID},
• {RollNo},
• {StudentID, Email}, etc.
2️ Candidate Key (2M)
Definition:
A candidate key is the minimal super key — that is, a key with no
unnecessary attributes.
It uniquely identifies each tuple and cannot be reduced further.
Example:
From the above, {StudentID} and {RollNo} are candidate keys.
3️ Foreign Key (2M)
Definition:
A foreign key is an attribute that creates a relationship between two tables
by referencing the primary key of another table.
Example:
DEPARTMENT(DeptID, DeptName)
EMPLOYEE(EmpID, EmpName, DeptID)
→ Here, DeptID in EMPLOYEE is a foreign key referencing DeptID in
DEPARTMENT.
4️ Difference between Super Key and Candidate Key (2M)
Basis   Super Key   Candidate Key
Set of attributes that uniquely   Minimal super key (no extra
Definition
identify a record   attributes)
Uniqueness Ensures unique identification   Ensures unique identification
********** 3 **********
--- page 4 ---
Minimality Not necessarily minimal   Always minimal
Example   {StudentID, Name}   {StudentID}
Mark Split:
• Definitions (2M each ×3 = 6M)
• Example – 2M
• Difference – 2M
CO 1;   B. A university has multiple faculties, such as Engineering, Science, and Arts.   10M
SO6;   Each faculty has several professors. Professors have attributes like Professor
BL5   ID, name, department, and email. Students enroll in multiple courses and
have unique Student IDs, names, addresses, and phone numbers. Each course
has Course ID, course name, and credits. A student can have multiple grades
for different courses.
1. Identify the key entities and their attributes.
2. Specify the relationships between these entities, including cardinality and
participation constraints.
3. Create an Entity-Relationship diagram.
Entity   Attributes
Faculty FacultyID, FacultyName
Professor ProfessorID, Name, Department, Email, FacultyID (FK)
Student StudentID, Name, Address, Phone
Course   CourseID, CourseName, Credits
Grade   GradeID, StudentID (FK), CourseID (FK), GradeValue
Relationship   Cardinality   Participation
1–M (One
Faculty–   Total on Professor side (each professor
faculty → many
Professor   belongs to one faculty)
professors)
Student–Course
M–N   Partial
(Enrollment)
Course–Grade 1–M   Total on Grade side
Student–Grade 1–M   Total on Grade side
********** 4 **********
--- page 5 ---
Final ER Diagram – 3M
Mark Split:
• Identify entities & attributes – 4M
• Relationships & cardinalities – 3M
• ER Diagram – 3M
Question 3
CO 2;   A.   Explain different types of set operations in SQL. Describe all with proper   10M
SO1;   syntax and examples.
BL4
1 UNION (2 Marks)
Definition:
Combines the results of two queries and removes duplicate rows.
Syntax:
SELECT column_name FROM table1
UNION
SELECT column_name FROM table2;
Example:
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers;
➡ Returns unique cities from both tables.
2 UNION ALL (2 Marks)
Definition:
Combines the results of two queries including duplicates.
Syntax:
SELECT column_name FROM table1
UNION ALL
SELECT column_name FROM table2;
Example:
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers;
➡ Returns all cities, including duplicates.
3 INTERSECT (2 Marks)
********** 5 **********
--- page 6 ---
Definition:
Returns only common rows between two result sets.
Syntax:
SELECT column_name FROM table1
INTERSECT
SELECT column_name FROM table2;
Example:
SELECT City FROM Customers
INTERSECT
SELECT City FROM Suppliers;
➡ Returns cities present in both tables.
4 EXCEPT / MINUS (2 Marks)
Definition:
Returns rows from the first query that are not present in the second.
(SQL Server uses EXCEPT; Oracle uses MINUS.)
Syntax:
SELECT column_name FROM table1
EXCEPT
SELECT column_name FROM table2;
Example:
SELECT City FROM Customers
EXCEPT
SELECT City FROM Suppliers;
➡ Returns cities present in Customers but not in Suppliers.
Mark Split:
• Explanation of each (UNION, UNION ALL, INTERSECT, MINUS) – 6M
• Syntax + example – 4M
CO 4;   B.   Define view serializability. Determine whether the following schedule is   10M
SO6;   view serialisable or not. Justify your answer.
BL3   Schedule: R1(X), W2(Y), R3(Y), W1(X), W3(Y)
A schedule is view serialisable if it is view-equivalent to some serial schedule.
Two schedules are view-equivalent when, for every data item:
1. Each transaction reads the same version (same reads-from source) in
both schedules.
********** 6 **********
--- page 7 ---
2. The transaction that performs the final write on the item is the same in
both schedules.
Step 1 — Determine reads-from relationships
• R1(X) — no prior write on X in the schedule → R1(X) reads the
initial value of X (call it DB0).
• W2(Y) — T2 writes Y.
• R3(Y) — the most recent write on Y before R3 is W2(Y), so R3(Y)
reads-from T2.
• W1(X) — T1 writes X.
• W3(Y) — T3 writes Y (this is the last write on Y in the schedule).
Step 2 — Identify final-writes
•   Final writer of X in the schedule: T1 (by W1(X)).
•   Final writer of Y in the schedule: T3 (by W3(Y)).
Step 3 — Derive ordering constraints for a view-equivalent serial schedule
From reads-from and final-write requirements:
1. R3(Y) reads-from T2 ⇒ T2 must appear before T3 in the equivalent
serial order (so that T3 can read the value written by T2).
2. Final-writer on Y is T3 ⇒ among transactions that write Y (T2 and T3),
T3 must come after T2 — same constraint as (1).
3. R1(X) reads the initial value of X (DB0). That requires that no other
transaction that writes X appears before T1 in the serial order. Here,
only T1 writes X, so there is no restriction involving other transactions.
4. Final-writer on X is T1 — since only T1 writes X, this places no extra
restriction beyond T1 being the (only) writer.
So the only mandatory ordering constraint is:
T2 before T3.
T1 has no ordering constraint relative to T2 or T3 from the view conditions.
Therefore, the given schedule is view serialisable. One valid equivalent
serial schedule is T1 → T2️ → T3️
Mark Split:
• Definition – 3M
• Check of view equivalence – 5M
• Conclusion – 2M
Question 4
CO 3;   A.   What are anomalies in database design? Explain insertion, deletion, and   10M
SO1;   update anomalies with examples. Normalise the following relation into 3NF:
BL2   1 Anomalies in Database Design
Definition:
********** 7 **********
--- page 8 ---
Anomalies are problems or inconsistencies that occur in poorly designed
databases (usually due to redundancy). They occur during insertion,
deletion, or update operations.
a) Insertion Anomaly (1.5M)
Occurs when we cannot insert data into a table without having other
unrelated data.
Example:
Consider a table storing students and courses:
StudentID   StudentName CourseID   CourseName Instructor
If no student is enrolled in a new course yet, we cannot insert the course
because StudentID is mandatory.
b) Deletion Anomaly (1.5M)
Occurs when deleting a record unintentionally removes other important data.
Example:
In the same table, if we delete the only student enrolled in a course, the
course information is lost.
c) Update Anomaly (1M)
Occurs when updating a value requires multiple rows to be updated, risking
inconsistency.
Example:
If the instructor of a course changes, we must update every row for that
course. Forgetting any row causes inconsistency.
2 Normalization of Relation R(A, B, C, D, E, F, G)
Step 1 – Find Candidate Keys
AB⁺ = ABCDEFG → AB is a candidate key.
Step 2 – Convert to 1NF and 2NF
Remove partial dependencies
AB → EF (AB is full key) → OK
already 2NF
Step 4 – Convert to 3NF
Remove transitive dependencies
E → CD → transitive dependency
D → G → transitive dependency
Decompose into 3NF:
R1(E, C, D) – for E → C,D
R2(D, G) – for D → G
R3(A, B, E, F) – for AB → EF
Each relation is in 3NF
********** 8 **********
--- page 9 ---
Mark Split:
• Anomalies – 4M
• Step-by-step 3NF normalisation – 6M
CO 2;   B.   Flights (FlightNo, Source, Destination)   10M
SO1;   Passenger (PassengerID, PassengerName, Age)
BL6   Booking (BookingID, PassengerID, FlightNo, Date)
Consider the above data and write Relational algebra queries
1. Find the names of passengers flying from 'Delhi' to 'Mumbai'.
πPassengerName((Passenger⨝Booking⨝Flights)
σSource=′Delhi′∧Destination=′Mumbai′(Flights))
2. Retrieve passengers aged above 60.
πPassengerName,Age(σAge>60(Passenger))
3. List flight numbers booked on '2024-12-25'
πFlightNo(σDate=′2️02️4−12−2️5′(Booking))
Mark Split:
• Correct operators & results – 3×3M
• Syntax correctness – 1M
Question 5
CO 4;   A.   Explain the different storage types of NoSQL databases with examples.   10M
SO7;
BL2   1. Key–Value Stores (2M)
Store data as a collection of key–value pairs.
Each key is unique, and value can be a string, JSON, or binary data.
Used for: Caching, session management, real-time data.
Example (0.5M): Redis, Amazon DynamoDB.
2. Document-Oriented Databases (2M)
Store data as documents (mostly JSON, BSON, or XML).
Each document contains self-describing fields and values.
Schema-free; supports nested data structures.
Used for: Content management systems, e-commerce catalogs.
********** 9 **********
--- page 10 ---
Example (0.5M): MongoDB, CouchDB.
3. Column-Family Stores (2M)
Data stored in column families (instead of rows).
Designed for fast read/write on large datasets.
Suitable for analytical and time-series data.
Used for: Big data and analytics applications.
Example (0.5M): Apache Cassandra, HBase.
4. Graph Databases (2M)
Represent data as nodes (entities) and edges (relationships).
Ideal for highly connected data.
Used for: Social networks, fraud detection, recommendation systems.
Example (0.5M): Neo4j, Amazon Neptune.
Mark Split:
• Explanation (Key-Value, Document, Column, Graph) – 8M
• Example – 2M
CO 2;   B.   Consider the data in Q.4 (B) and write SQL JOIN queries for the given   10M
SO1;   questions.
BL6   1. Display PassengerName, FlightNo, and destination for all bookings.
SELECT p.PassengerName, f.FlightNo, f.Destination
FROM Passenger p
JOIN Booking b ON p.PassengerID = b.PassengerID
JOIN Flights f ON b.FlightNo = f.FlightNo;
2. List passengers who have booked flights to ‘Delhi’.
SELECT DISTINCT p.PassengerName
FROM Passenger p
JOIN Booking b ON p.PassengerID = b.PassengerID
JOIN Flights f ON b.FlightNo = f.FlightNo
WHERE f.Destination = 'Delhi';
3. Find the total number of passengers who booked flights for each
destination.
SELECT f.Destination, COUNT(DISTINCT b.PassengerID) AS
TotalPassengers
********** 10 **********
--- page 11 ---
FROM Flights f
JOIN Booking b ON f.FlightNo = b.FlightNo
GROUP BY f.Destination;
4. Show flights that have no bookings.
SELECT f.FlightNo, f.Source, f.Destination
FROM Flights f
LEFT JOIN Booking b ON f.FlightNo = b.FlightNo
WHERE b.BookingID IS NULL;
Mark Split:
• Each query – 2.5M ×4 = 10M
Question 6
CO 4;   A.   What is the transaction? Describe ACID Properties of Transactions with an   10M
SO6;   example?
BL4
A transaction is a logical unit of work performed within a database that
must be executed entirely or not at all.
ACID Properties (6M):
1. Atomicity (1.5M):
Ensures that all operations of a transaction are completed; if any part
fails, the entire transaction is rolled back.
Example: If money is deducted from one account but not credited to
another, the system must undo the deduction.
2. Consistency (1.5M):
Guarantees that a transaction brings the database from one valid state to
another, maintaining all defined rules, constraints, and relationships.
Example: Total amount of money across accounts remains unchanged
after a transfer.
3. Isolation (1.5M):
Ensures that concurrent transactions do not interfere with each other.
Intermediate results of one transaction are not visible to others.
Example: Two users updating the same record simultaneously should
not cause data inconsistency.
4. Durability (1.5M):
Ensures that once a transaction is committed, its effects are permanently
stored in the database even in case of system failure.
Example: Once funds are transferred, the record remains even if the
system crashes.
********** 11 **********
--- page 12 ---
Example (2M):
Bank Transaction Example:
Transfer ₹1000 from Account A to Account B involves two operations:
1. Debit ₹1000 from Account A
2. Credit ₹1000 to Account B
If both operations succeed → transaction commits.
If any operation fails → transaction rolls back, restoring the previous state.
Mark Split:
• Definition – 2M
• ACID explanation – 6M
• Example – 2M
CO 2;   B.   Consider the data in Q.4 (B) and write SQL sub-queries for the given   10M
SO1;   questions.
BL6   1. List the names of passengers who have booked a flight to the same
destination as ‘Mumbai’.
SELECT PassengerName
FROM Passenger
WHERE PassengerID IN (
SELECT b.PassengerID
FROM Booking b
JOIN Flights f ON b.FlightNo = f.FlightNo
WHERE f.Destination = 'Mumbai'
);
2. Display FlightNo and Destination for flights that have been booked by
more than one passenger.
SELECT f.FlightNo, f.Destination
FROM Flights f
WHERE f.FlightNo IN (
SELECT FlightNo
FROM Booking
GROUP BY FlightNo
HAVING COUNT(PassengerID) > 1
);
3. Find passengers who have not made any booking.
********** 12 **********
--- page 13 ---
SELECT PassengerName
FROM Passenger
WHERE PassengerID NOT IN (
SELECT PassengerID
FROM Booking
);
4. List passengers whose Age is greater than the average Age of all
passengers.
SELECT PassengerName, Age
FROM Passenger
WHERE Age > (
SELECT AVG(Age)
FROM Passenger
);
Mark Split:
• Each query – 2.5M ×4 = 10M
Question 7
Define a Database System and explain its main components.
Database System: A Collection of data and programs that allow users to
create, maintain, and manipulate databases.
Main Components:
1. Query Processor
2. Transaction manager: DBMS, OS, application programs.
CO 1;   3. Data: An organised collection of related information.
SO6;   A.   4. Users: Database administrators, end users, designers.   5M
BL2
Mark Split:
• Definition of Database System – 1M
• Explanation of Components (Hardware, Software, Data, Users, Procedures
– any four) – 3M
• Neat diagram / example – 1M
CO 2;   Explain relational algebra operators like SELECT, PROJECT, and JOIN.
SO2;   B. SELECT (σ): Filters rows that satisfy a given condition.   5M
BL4   Example: σDept='CSE'(STUDENT) → selects students in CSE.
********** 13 **********
--- page 14 ---
PROJECT (π): Chooses specific attributes (columns).
Example: πName,Dept(STUDENT).
JOIN (⋈): Combines related tuples from two relations.
Example: STUDENT ⋈<sub>DeptID</sub> DEPARTMENT → merges data
where DeptID matches.
Mark Split:
• SELECT (σ) – Definition & Example – 1.5M
• PROJECT (π) – Definition & Example – 1.5M
• JOIN (⋈) – Definition & Example – 2M
Write short notes on BCNF with an example.
A relation R is in Boyce–Codd Normal Form (BCNF) if for every non-trivial
functional dependency X → Y, X is a superkey.
BCNF eliminates redundancy and anomalies not removed by 3NF.
CO 3;   Example: R(A, B, C), FDs: A → B, B → C→ B → C violates BCNF since B
SO1;   C.   isn’t a superkey. Decompose: R1(A,B) and R2(B,C). Both in BCNF.   5M
BL4
Mark Split:
• Definition of BCNF – 2M
• Explanation / Need – 1M
• Example relation with FDs – 2M
Illustrate the ER to relational mapping process with a neat diagram.
ER-to-Relational Mapping Steps:
1. Entity → Table (each strong entity becomes a relation).
2. Attributes → Columns (composite attributes split).
3. Primary Key: chosen from key attributes.
CO 1;   4. Relationships → Foreign Keys / Associative Tables.
SO6;   D.   5. Weak Entities & Multivalued Attributes: represented as separate   5M
BL2   tables.
Example: ERD: Student–Course–Enroll
Mark Split:
• Mention of Mapping Steps – 4M
• Example schema – 1M
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 777eda07857b

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_DS_7009/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech (DS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 28 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Diagrams must be neat and legible.
5. Ensure the correct question number is written in the answer sheet.
6. Qt1 is compulsary, attemp any 4 questions from remaining 6 questions.
Q1   Answer the following questions   [20]
CO- 1;   a   What are data models? Explain the Relational Model.   [5]
SO- 2;   1. Definition of Data Models (2 Marks)
BL- 1   A data model   is a conceptual framework that describes how data are structured,
stored, and manipulated in a database system.
It defines the   logical structure   of the database — the relationships among data, the
constraints, and the operations that can be performed.
Common types include:
•   Hierarchical Model
•   Network Model
•   Relational Model
•   Object Oriented Model
2. Relational Model (3 Marks)
The Relational Model organizes data into relations (tables) consisting of rows and
columns .
Each table (relation) represents an entity , each row (tuple) represents a record ,
and each column (attribute) represents a data field .
Every relation has a Primary Key that uniquely identifies each tuple.
Foreign Keys are used to establish relationships between tables.
Data are manipulated using Relational Algebra and the SQL language for operations
like selection, projection, join, and union.
Example:
| StudentID | Name | Branch |
|   |   |   |
| S101   | Riya   | IT   |
| S102   | Arjun | CS   |
Here, StudentID → Primary Key; the table “Student” represents the Student entity .
CO- 2;   b   1. Features of a Good Database Design (4 Marks)   [5]
SO - 2;   Data Integrity and Consistency:
BL- 2   Each piece of data is stored only once (no redundancy), ensuring consistency.
Example: Customer details stored in one CUSTOMER table, not repeated in every ORDER
record.
Minimal Data Redundancy:
Redundant data causes update anomalies and wasted storage.
Example: Instead of repeating department names for every employee, use a separate
DEPARTMENT table with a foreign key reference.
Proper Use of Normalization:
Splitting large tables into smaller ones to remove partial and transitive dependencies (1NF–
3NF).
********** 1 **********
--- page 2 ---
Example:   Separating   EMPLOYEE(EmpID,   EmpName,   DeptID)   and
DEPARTMENT(DeptID, DeptName).
Clear Entity–Relationship Mapping:
Logical relationships (1:1, 1:N, M:N) must be clearly defined using primary and foreign
keys.
Example: One‐to‐many between CUSTOMER and ORDER.
Scalability and Performance:
Well-designed indexes and relationships support fast queries and future data growth.
Example: Indexing OrderID in ORDERS table speeds up retrieval.
2. Conclusion (1 Mark)
A good database design is normalized, non-redundant, and supports data integrity, leading
to efficient storage, accurate information, and simplified maintenance.
CO- 3 ;   c   (a) Superkeys:   [5]
SO - 2;   {RollNo}, {Email}, {AadhaarNo}, {RollNo, Name}, {Email, Phone}, etc.
BL- 2   (b) Candidate Keys:
{RollNo}, {Email}, {AadhaarNo}
(c) Primary Key:
RollNo —unique.
CO- 4 ;   d   What is the significance of CAP theorem in NOSQL   [5]
SO - 2;   The CAP Theorem is a fundamental principle in NoSQL databases that describes the trade-
BL-1   offs among three key properties:
1.   Consistency (C): Every read receives the most recent write or an error.
2.   Availability (A): Every request receives a response, regardless of the state of the
data.
3.   Partition Tolerance (P): The system continues to operate even if network partitions
or communication failures occur.
Significance in NoSQL:
•   NoSQL databases are often distributed systems. The CAP theorem explains that it
is impossible to achieve all three properties simultaneously; a database can only fully
guarantee two out of three.
•   For example:
o   MongoDB prioritizes Consistency + Partition Tolerance (CP) by default.
o   Cassandra prioritizes Availability + Partition Tolerance (AP).
•   This helps developers choose the right database and configure it according to
application needs, balancing consistency, availability, and fault tolerance.
"
Q2   [20]
CO- 1 ;   a   [10]
SO - 2;
BL-2
CO- 2 ;   b   Consider following movie database:   [10]
SO - 2;
BL- 2   users (user_id, full_name, city, contact_no)
restaurants (restaurant_id, name, address, price level, is active)
********** 2 **********
--- page 3 ---
dishes (dish_id, restaurant, name, price, is_veg, is spicy)
ratings (user_id, dish_id, rating, rated_at, feedback)
Write the SQL queries the following question:
i   Add a new column “email” to users table   [2]
Ans:
ALTER TABLE users
ADD COLUMN email VARCHAR (40);
ii   Modify table dishes to enforce business rules “dishes.price must be > 0.” using CHECK   [2]
constraints
Ans:
ALTER TABLE dishes
ADD CONSTRAINT chk_price
CHECK (price > 0);
iii   Select all veg, not-spicy dishes with price <= 250 from active restaurants.   [2]
Ans:
SELECT d.name AS dish, r.name AS restaurant, d.price
FROM dishes d, restaurants r
Where r. restaurant_id = d. restaurant_id and r.is_active = ‘yes’ AND d.is_veg = ‘yes’
AND d.is_spicy is ‘No’ and d. price <= 250
iv   Show each restaurant’s average rating and number of ratings but return only those with at   [2]
least 2 ratings and an average ≥ 4.0.
Ans:
SELECT r.name AS restaurant, ROUND (AVG (rt. rating), 2) AS avg_rating,
COUNT (rt. rating) AS rating_count
FROM restaurants r, dishes d, ratings rt where d. restaurant_id = r. restaurant_id
And rt. dish_id = d. dish_id
GROUP BY r. restaurant_id, r.name
HAVING COUNT (rt. rating) >= 2
AND AVG (rt. rating) >= 4.0
v   Create a view called user_ratings which will show each rating alongside the user who   [2]
gave it.
CREATE OR REPLACE VIEW user_ratings AS
SELECT u.user_id, u. full_name, u. city, u. contact_no, r. dish_id, r. rating, r. rated_at,
r. feedback
FROM ratings r JOIN users u
ON u.user_id = r.user_id;
Q3   [20]
CO- 1 ;   a.   [10]
SO - 2;   Relational Schema Conversion
BL- 2   1. USER
USER(u_id PRIMARY KEY,   name,   email)
2. ADDRESS
ADDRESS(a_id PRIMARY KEY,   city,   state,   country,   u_id FOREIGN
KEY REFERENCES USER(u_id))
Relationship: User – lives in – Address → 1-to-M (one user can have many addresses)
3. ORDER
ORDER(o_no PRIMARY KEY,   order_amount,   order_date,   u_id FOREIGN
KEY REFERENCES USER(u_id))
Relationship: User – places – Order → 1-to-M
4. TRACKING_DETAIL
TRACKING_DETAIL(trac_id PRIMARY KEY,   status,   o_no
FOREIGN KEY REFERENCES ORDER(o_no))
Relationship: Order – contains – Tracking_detail → 1-to-M
5. PRODUCT_CATEGORY
PRODUCT_CATEGORY(cat_id PRIMARY KEY,   cat_name)
6. PRODUCT
PRODUCT(p_id PRIMARY KEY,   p_name,   price,   description,   cat_id
FOREIGN KEY REFERENCES PRODUCT_CATEGORY(cat_id))
********** 3 **********
--- page 4 ---
Relationship: Product – has – Product_Category → M-to-1
7. CART
CART(cart_id PRIMARY KEY)
8. PRODUCT_CART (resolving M-N between Product and Cart)
PRODUCT_CART(p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
cart_id FOREIGN KEY REFERENCES CART(cart_id),
PRIMARY KEY (p_id, cart_id))
Relationship: Product – added to – Cart → M-to-N
9. ORDER_PRODUCT (resolving M-N between Order and Product)
ORDER_PRODUCT(o_no FOREIGN KEY REFERENCES ORDER(o_no),
p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
PRIMARY KEY (o_no, p_id))
Relationship: Order – contains – Product → M-to-N
CO- 3 ;   b.   (i) Partial & Transitive dependencies (3 marks)   [10]
SO - 2;
BL- 3   Candidate key (in SALES): ({OrderID, ProdID})
(Quantity needs both; everything else is determined by either OrderID, CustID, ProdID,
or SalespersonID.)
Partial dependencies (depend on part of composite key)
•   OrderID → OrderDate, CustID, SalespersonID
(These don’t need ProdID.)
•   ProdID → ProdName, UnitPrice
(These don’t need OrderID.)
•   SalespersonID → SalespersonName, SalespersonRegion and
CustID → CustName, CustCity are not on the key, but in the single SALES table
they appear as attributes that are determined by non-key attributes—handled
under transitive below.
Transitive dependencies (key → nonkey → other nonkeys)
•   OrderID → CustID and CustID → CustName, CustCity
⇒ OrderID → CustName, CustCity (transitive).
•   OrderID → SalespersonID and SalespersonID → SalespersonName,
SalespersonRegion
⇒ OrderID → SalespersonName, SalespersonRegion (transitive).
Full dependency:
•   ({OrderID, ProdID} → Quantity) (depends on the whole key, not partial).
(ii) Decomposition to 3NF (step-by-step) (5 marks)
Start:
SALES(OrderID, OrderDate, CustID, CustName, CustCity, ProdID, ProdName,
UnitPrice, Quantity, SalespersonID, SalespersonName, SalespersonRegion)
Step 1: Remove partial dependencies (to reach 2NF)
Create relations on determinants of partial dependencies:
1. ORDER(OrderID, OrderDate, CustID, SalespersonID)
(from OrderID → OrderDate, CustID, SalespersonID)
2. PRODUCT(ProdID, ProdName, UnitPrice)
(from ProdID → ProdName, UnitPrice)
********** 4 **********
--- page 5 ---
3. Keep line items for the fully dependent attribute:
SALES_LINE(OrderID, ProdID, Quantity) with PK (OrderID, ProdID)
Step 2: Remove transitive dependencies (to reach 3NF)
Separate dependents of non-key determinants:
4. CUSTOMER(CustID, CustName, CustCity)
(from CustID → CustName, CustCity)
5. SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
(from SalespersonID → SalespersonName, SalespersonRegion)
Now, in ORDER, CustID and SalespersonID remain as foreign keys only; their
descriptive attributes moved to their own tables, removing transitive dependencies.
All resulting tables are in 3NF:
•   Every non-key attribute depends on the key, the whole key, and nothing but the
key in its table.
(iii) Final set of relations with keys (2 marks)
•   ORDER(OrderID, OrderDate, CustID, SalespersonID)
FK: CustID → CUSTOMER, SalespersonID → SALESPERSON
• CUSTOMER(CustID, CustName, CustCity)
•   SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
• PRODUCT(ProdID, ProdName, UnitPrice)
•   SALES_LINE(OrderID, ProdID, Quantity)
FK: OrderID → ORDER, ProdID → PRODUCT
This decomposition is lossless and preserves the given FDs, with SALES_LINE capturing
the many-to-many between orders and products plus Quantity.
Q4   [20]
CO- 1 ;   a.   Discuss the major difficulties encountered while creating a database from scratch, and   [10]
SO - 2;   illustrate your answer with suitable examples.
BL-2   Building a database from scratch involves several conceptual, technical, and
organizational challenges that must be carefully addressed to ensure efficiency, accuracy,
and long-term usability.
1.   Requirement Analysis:
2.   Data Modeling Challenges:
3.   Data Redundancy and Integrity:
4.   Normalization and Performance Balance:
5.   Security and Access Control:
6.   Scalability and Future Growth:
7.   Backup and Recovery Planning:
CO- 2 ;   b.   Solve the following queries using relational algebra   [10]
SO - 2;   Customer(CustomerID, CustomerName, City)
BL-2   Order(OrderID, OrderDate, CustomerID)
Product(ProductID, ProductName, Price)
Order_Product(OrderID, ProductID, Quantity)
********** 5 **********
--- page 6 ---
(i)   Find the names of customers who have placed at least one order.
(ii)   Get the customer names and order IDs for orders placed after ‘2024-01-01’.
(iii)   List all products ordered by customers who live in ‘Chicago’.
(iv)   List the products that have been ordered by any customer with a quantity greater
than 1
(v)   Find all customers located in New York and have ordered something in month of
October 2024(assume date is in yyyy-mm-dd)
Q5   [20]
CO- 2 ;   a.   Consider the following table:   [10]
SO - 2;   employee (employee_id, first_name , last_name, email, phone_number , hire_date, job_id
BL-2   , salary, commission_pct , manager_id , department_id )
Write the SQL queries the following question:
i   Write a SQL query to find those employees who receive a higher salary than the employee   [3]
with ID 163. Return first name, last name.
Ans:
SELECT first_name, last_name
FROM employees
WHERE salary >
( SELECT salary
FROM employees
WHERE employee_id=163
);
ii   Write a SQL query to find out which employees have the same designation as the employee   [3]
whose ID is 169. Return first name, last name, department ID and job ID.
Ans:
SELECT first_name, last_name, salary, department_id, job_id
FROM employees
WHERE job_id =
( SELECT job_id
FROM employees
WHERE employee_id=169
);
iii   Write a SQL query to find those employees whose salary matches the lowest salary of any   [4]
of the departments. Return first name, last name and department ID
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE salary IN
(SELECT MIN(salary)
FROM employees
GROUP BY department_id
);
CO- 4 ;   b.   [10]
SO - 2;
BL- 2
********** 6 **********
--- page 7 ---
It is not conflict serilizable as the graph is cyclic.
Step   T1   T2   T3
1   T1: Read(A)
2   T1: Write(A)
3   T2: Read(A)
4   T2: Write(A)
5   T2: Read(B)
6   T3: Read(B)
7   T2: Write(B)
8   T3: Write(B)
Serializability ensures that a concurrent execution is equivalent to some serial order of
transactions. This preserves database correctness by preventing anomalies such as lost
updates, dirty reads, non-repeatable reads, and inconsistent results—while still allowing
concurrency for performance.
Q6   [20]
CO- 4 ;   a.   1. Definition of a Transaction   [10]
SO - 2;   A transaction is a logical unit of database processing that consists of one or more database
BL-3   operations such as read, write, insert, update, or delete.
It represents a single, indivisible unit of work that must be executed completely or not at
all.
Example:
T1:
Read(A)
A = A – 100
Write(A)
Read(B)
B = B + 100
Write(B)
This transaction transfers ₹100 from account A to account B.
2. ACID Properties of a Transaction
Property Meaning Example
Atomicity   All operations in a transaction must complete successfully; if any fails,
the entire transaction is rolled back. If the debit from A succeeds but the credit to B fails,
both changes are undone.
Consistency   A transaction transforms the database from one consistent state to
another, maintaining all integrity constraints.The total balance (A + B) remains the same
before and after the transfer.
Isolation Concurrent transactions should not interfere with each other; intermediate states
are invisible to others.   While T1 transfers money, another transaction T2 cannot read
the partially updated balance of A or B.
Durability   Once a transaction commits, its effects are permanently recorded in the
database, even after system failures.   After committing, the ₹100 transfer remains
intact even if the system crashes.
3. Conflict Serializability
A schedule is conflict-serializable if it can be transformed into a serial schedule by
swapping non-conflicting operations.
Two operations conflict if:
1.   They belong to different transactions.
2.   They operate on the same data item.
3.   At least one is a write operation.
********** 7 **********
--- page 8 ---
Example:
Step   Transaction   Operation
1   T1   Read(A)
2   T2   Read(A)
3   T1   Write(A)
4   T2   Write(A)
Here, conflicts occur between T1 and T2 on A.
Precedence graph: T1 → T2 (no cycle) ⇒ Conflict-serializable, equivalent to serial order
T1 → T2.
4. View Serializability
A schedule is view-serializable if it is view-equivalent to some serial schedule, i.e.,
•   Both schedules have the same read-from relationships (who reads whose value).
•   Both have the same final writes on each data item.
•   Both start from the same initial state.
Example:
S1: T1: W(A)
T2: R(A), W(A)
T3: R(A)
If both T2 and T3 read the value of A written by T1 and T2 does the final write,
then S1 is view-equivalent to the serial order T1 → T2 → T3.
5. Difference between Conflict and View Serializability
Aspect Conflict Serializability   View Serializability
Basis   Swapping of non-conflicting operations   Preservation of read-from and final-
write relationships
Detection   Using precedence (serialization) graph   More complex; requires
comparing read/write dependencies
Strictness   Stronger form — every conflict-serializable schedule is view-
serializable   Weaker — some non-conflict-serializable schedules can still be view-
serializable
Ease of Check   Easier to test algorithmically   Harder to test, computationally
expensive
Example Schedule without cycles in precedence graph   Schedule with blind writes
(where a value is overwritten without being read) may still be view-serializable but not
conflict-serializable
CO- 4 ;   b.   Aspect   ACID (RDBMS)   BASE (NoSQL / Distributed   [10]
SO - 2;   Systems)
BL-1   Philosophy   Ensures strict correctness Focuses on scalability and
and reliability   availability
Consistency   Strong consistency – all   Eventual consistency – nodes
Model   nodes see same data   become consistent over time
instantly
System Type   Centralized or small-   Distributed, large-scale, cloud-
scale transactional   based systems
systems
Transaction   Transactions are atomic   Transactions may be broken or
Handling   and isolated   partial across nodes
Availability vs.   Prioritizes consistency   Prioritizes availability over
Consistency   over availability   consistency
Response Time   Slower, due to strict   Faster, as some consistency is
locking and commit   relaxed
protocols
Use Cases   Banking, financial,   Social media feeds, e-commerce
inventory systems   catalogs, IoT data
Error Recovery   Rollback ensures   Recovery through replication
integrity after failures   and eventual updates
CAP Theorem CP systems (Consistency AP systems (Availability +
View   + Partition tolerance)   Partition tolerance)
Examples   Oracle, MySQL,   Cassandra, MongoDB, Amazon
PostgreSQL   DynamoDB
Q7   [20]
********** 8 **********
--- page 9 ---
CO-1 ;   A   Advantages of DBMS [5 Marks]   [5]
SO- 2;   1. Reduces Data Redundancy and Inconsistency
BL-1   – Data is stored centrally, avoiding duplication and ensuring all users see the
same updated information.
2. Improves Data Security
– Access to data is controlled through authentication and authorization,
protecting sensitive information.
3. Ensures Data Integrity and Accuracy
– Integrity constraints like primary keys and foreign keys maintain correctness of
data values.
4. Supports Concurrent Access and Sharing
– Multiple users can work on the same database simultaneously without
conflicts, using concurrency control.
5. Provides Backup and Recovery
– Automatic backup and recovery mechanisms protect data against crashes and
system failures.
CO- 2 ;   b   Joins in SQL [5 Marks]   [5]
SO - 2;   Definition:
BL-2   A JOIN in SQL is used to combine rows from two or more tables based on a related
column (usually a primary–foreign key relationship).
1. INNER JOIN
Returns only the matching rows from both tables.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
INNER JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows students who are enrolled in a course.
2. LEFT JOIN (LEFT OUTER JOIN)
Returns all rows from the left table, and matching rows from the right; non-matching rows
show NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
LEFT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students, even if not enrolled in any course.
3. RIGHT JOIN (RIGHT OUTER JOIN)
Returns all rows from the right table, and matching rows from the left; non-matching rows
show NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
RIGHT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all courses, even if no student has enrolled.
4. FULL JOIN (FULL OUTER JOIN)
Returns all rows from both tables; unmatched rows are filled with NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
FULL JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students and all courses, with NULLs where no match exists.
5. CROSS JOIN
Produces Cartesian product — every row of the first table with every row of the second.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
CROSS JOIN Courses;
Shows all possible combinations of students and courses.
Summary:
Type of Join   Description   Matching/Unmatched Rows
INNER JOIN Common records only   Matching only
LEFT JOIN   All left + matching right   Unmatched right → NULL
RIGHT JOIN   All right + matching left   Unmatched left → NULL
********** 9 **********
--- page 10 ---
FULL JOIN   All rows from both tables Unmatched → NULL
CROSS JOIN Cartesian product   No condition needed
CO- 3;   c   Armstrong’s Axioms [5 Marks]   [5]
SO - 2;   Definition:
BL-3   Armstrong’s Axioms are a set of inference rules used to derive all possible functional
dependencies (FDs) from a given set of FDs in a relational schema.
They form the theoretical foundation for normalization and dependency closure.
1. Basic Axioms
Axiom   Rule Description
a) Reflexivity   If Y ⊆ X, then X → Y. (A set of attributes determines any   If X =
of its subsets.)   B} →
b) Augmentation   If X → Y, then XZ → YZ. (Adding the same attribute(s) to   If A →
both sides preserves the dependency.)   BC.
c) Transitivity   If X → Y and Y → Z, then X → Z. (Dependencies can be   If A →
chained.)   then A
2. Derived (Additional) Axioms
Using the three basic rules, the following can be derived:
Derived Axiom   Meaning
Union (Additivity)   If X → Y and X → Z, then X → YZ
Decomposition (Projectivity)   If X → YZ, then X → Y and X → Z
Pseudo-transitivity   If X → Y and YZ → W, then XZ → W
3. Importance
•   These axioms help in finding attribute closure (X⁺)
•   Used to test dependency preservation and lossless decomposition during
normalization.
CO- 4 ;   d   "Key Value Pair Based   [5]
SO - 2;
BL-1   Data is stored in key/value pairs. It is designed in such a way to handle lots of data and
heavy load.
Key-value pair storage databases store data as a hash table where each key is unique, and
the value can be a JSON, BLOB(Binary Large Objects), string, etc.
For example, a key-value pair may contain a key like ""Website"" associated with a value
like ""Guru99"".
It is one of the most basic types of NoSQL databases. This kind of NoSQL database is
used as a collection, dictionaries, associative arrays, etc. Key value stores help the
developer to store schema-less data. They work best for shopping cart contents.
Redis, Dynamo, Riak are some examples of key-value store DataBases. They are all based
on Amazon's Dynamo paper.
Column-based
Column-oriented databases work on columns and are based on BigTable paper by Google.
Every column is treated separately. Values of single column databases are stored
contiguously.
Column based NoSQL database
They deliver high performance on aggregation queries like SUM, COUNT, AVG, MIN
etc. as the data is readily available in a column.
Column-based NoSQL databases are widely used to manage data warehouses, business
intelligence, CRM, Library card catalogs,
HBase, Cassandra, HBase, Hypertable are examples of column based database.
"
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 445c84a3141b

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MBATech_IT_7041/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech (DS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 28 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Diagrams must be neat and legible.
5. Ensure the correct question number is written in the answer sheet.
6. Qt1 is compulsary, attemp any 4 questions from remaining 6 questions.
Q1   Answer the following questions   [20]
CO- 1;   a   What are data models? Explain the Relational Model.   [5]
SO- 2;   1. Definition of Data Models (2 Marks)
BL- 1   A data model   is a conceptual framework that describes how data are structured,
stored, and manipulated in a database system.
It defines the   logical structure   of the database — the relationships among data, the
constraints, and the operations that can be performed.
Common types include:
•   Hierarchical Model
•   Network Model
•   Relational Model
•   Object Oriented Model
2. Relational Model (3 Marks)
The Relational Model organizes data into relations (tables) consisting of rows and
columns .
Each table (relation) represents an entity , each row (tuple) represents a record ,
and each column (attribute) represents a data field .
Every relation has a Primary Key that uniquely identifies each tuple.
Foreign Keys are used to establish relationships between tables.
Data are manipulated using Relational Algebra and the SQL language for operations
like selection, projection, join, and union.
Example:
| StudentID | Name | Branch |
|   |   |   |
| S101   | Riya   | IT   |
| S102   | Arjun | CS   |
Here, StudentID → Primary Key; the table “Student” represents the Student entity .
CO- 2;   b   1. Features of a Good Database Design (4 Marks)   [5]
SO - 2;   Data Integrity and Consistency:
BL- 2   Each piece of data is stored only once (no redundancy), ensuring consistency.
Example: Customer details stored in one CUSTOMER table, not repeated in every ORDER
record.
Minimal Data Redundancy:
Redundant data causes update anomalies and wasted storage.
Example: Instead of repeating department names for every employee, use a separate
DEPARTMENT table with a foreign key reference.
Proper Use of Normalization:
Splitting large tables into smaller ones to remove partial and transitive dependencies (1NF–
3NF).
********** 1 **********
--- page 2 ---
Example:   Separating   EMPLOYEE(EmpID,   EmpName,   DeptID)   and
DEPARTMENT(DeptID, DeptName).
Clear Entity–Relationship Mapping:
Logical relationships (1:1, 1:N, M:N) must be clearly defined using primary and foreign
keys.
Example: One‐to‐many between CUSTOMER and ORDER.
Scalability and Performance:
Well-designed indexes and relationships support fast queries and future data growth.
Example: Indexing OrderID in ORDERS table speeds up retrieval.
2. Conclusion (1 Mark)
A good database design is normalized, non-redundant, and supports data integrity, leading
to efficient storage, accurate information, and simplified maintenance.
CO- 3 ;   c   (a) Superkeys:   [5]
SO - 2;   {RollNo}, {Email}, {AadhaarNo}, {RollNo, Name}, {Email, Phone}, etc.
BL- 2   (b) Candidate Keys:
{RollNo}, {Email}, {AadhaarNo}
(c) Primary Key:
RollNo —unique.
CO- 4 ;   d   What is the significance of CAP theorem in NOSQL   [5]
SO - 2;   The CAP Theorem is a fundamental principle in NoSQL databases that describes the trade-
BL-1   offs among three key properties:
1.   Consistency (C): Every read receives the most recent write or an error.
2.   Availability (A): Every request receives a response, regardless of the state of the
data.
3.   Partition Tolerance (P): The system continues to operate even if network partitions
or communication failures occur.
Significance in NoSQL:
•   NoSQL databases are often distributed systems. The CAP theorem explains that it
is impossible to achieve all three properties simultaneously; a database can only fully
guarantee two out of three.
•   For example:
o   MongoDB prioritizes Consistency + Partition Tolerance (CP) by default.
o   Cassandra prioritizes Availability + Partition Tolerance (AP).
•   This helps developers choose the right database and configure it according to
application needs, balancing consistency, availability, and fault tolerance.
"
Q2   [20]
CO- 1 ;   a   [10]
SO - 2;
BL-2
CO- 2 ;   b   Consider following movie database:   [10]
SO - 2;
BL- 2   users (user_id, full_name, city, contact_no)
restaurants (restaurant_id, name, address, price level, is active)
********** 2 **********
--- page 3 ---
dishes (dish_id, restaurant, name, price, is_veg, is spicy)
ratings (user_id, dish_id, rating, rated_at, feedback)
Write the SQL queries the following question:
i   Add a new column “email” to users table   [2]
Ans:
ALTER TABLE users
ADD COLUMN email VARCHAR (40);
ii   Modify table dishes to enforce business rules “dishes.price must be > 0.” using CHECK   [2]
constraints
Ans:
ALTER TABLE dishes
ADD CONSTRAINT chk_price
CHECK (price > 0);
iii   Select all veg, not-spicy dishes with price <= 250 from active restaurants.   [2]
Ans:
SELECT d.name AS dish, r.name AS restaurant, d.price
FROM dishes d, restaurants r
Where r. restaurant_id = d. restaurant_id and r.is_active = ‘yes’ AND d.is_veg = ‘yes’
AND d.is_spicy is ‘No’ and d. price <= 250
iv   Show each restaurant’s average rating and number of ratings but return only those with at   [2]
least 2 ratings and an average ≥ 4.0.
Ans:
SELECT r.name AS restaurant, ROUND (AVG (rt. rating), 2) AS avg_rating,
COUNT (rt. rating) AS rating_count
FROM restaurants r, dishes d, ratings rt where d. restaurant_id = r. restaurant_id
And rt. dish_id = d. dish_id
GROUP BY r. restaurant_id, r.name
HAVING COUNT (rt. rating) >= 2
AND AVG (rt. rating) >= 4.0
v   Create a view called user_ratings which will show each rating alongside the user who   [2]
gave it.
CREATE OR REPLACE VIEW user_ratings AS
SELECT u.user_id, u. full_name, u. city, u. contact_no, r. dish_id, r. rating, r. rated_at,
r. feedback
FROM ratings r JOIN users u
ON u.user_id = r.user_id;
Q3   [20]
CO- 1 ;   a.   [10]
SO - 2;   Relational Schema Conversion
BL- 2   1. USER
USER(u_id PRIMARY KEY,   name,   email)
2. ADDRESS
ADDRESS(a_id PRIMARY KEY,   city,   state,   country,   u_id FOREIGN
KEY REFERENCES USER(u_id))
Relationship: User – lives in – Address → 1-to-M (one user can have many addresses)
3. ORDER
ORDER(o_no PRIMARY KEY,   order_amount,   order_date,   u_id FOREIGN
KEY REFERENCES USER(u_id))
Relationship: User – places – Order → 1-to-M
4. TRACKING_DETAIL
TRACKING_DETAIL(trac_id PRIMARY KEY,   status,   o_no
FOREIGN KEY REFERENCES ORDER(o_no))
Relationship: Order – contains – Tracking_detail → 1-to-M
5. PRODUCT_CATEGORY
PRODUCT_CATEGORY(cat_id PRIMARY KEY,   cat_name)
6. PRODUCT
PRODUCT(p_id PRIMARY KEY,   p_name,   price,   description,   cat_id
FOREIGN KEY REFERENCES PRODUCT_CATEGORY(cat_id))
********** 3 **********
--- page 4 ---
Relationship: Product – has – Product_Category → M-to-1
7. CART
CART(cart_id PRIMARY KEY)
8. PRODUCT_CART (resolving M-N between Product and Cart)
PRODUCT_CART(p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
cart_id FOREIGN KEY REFERENCES CART(cart_id),
PRIMARY KEY (p_id, cart_id))
Relationship: Product – added to – Cart → M-to-N
9. ORDER_PRODUCT (resolving M-N between Order and Product)
ORDER_PRODUCT(o_no FOREIGN KEY REFERENCES ORDER(o_no),
p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
PRIMARY KEY (o_no, p_id))
Relationship: Order – contains – Product → M-to-N
CO- 3 ;   b.   (i) Partial & Transitive dependencies (3 marks)   [10]
SO - 2;
BL- 3   Candidate key (in SALES): ({OrderID, ProdID})
(Quantity needs both; everything else is determined by either OrderID, CustID, ProdID,
or SalespersonID.)
Partial dependencies (depend on part of composite key)
•   OrderID → OrderDate, CustID, SalespersonID
(These don’t need ProdID.)
•   ProdID → ProdName, UnitPrice
(These don’t need OrderID.)
•   SalespersonID → SalespersonName, SalespersonRegion and
CustID → CustName, CustCity are not on the key, but in the single SALES table
they appear as attributes that are determined by non-key attributes—handled
under transitive below.
Transitive dependencies (key → nonkey → other nonkeys)
•   OrderID → CustID and CustID → CustName, CustCity
⇒ OrderID → CustName, CustCity (transitive).
•   OrderID → SalespersonID and SalespersonID → SalespersonName,
SalespersonRegion
⇒ OrderID → SalespersonName, SalespersonRegion (transitive).
Full dependency:
•   ({OrderID, ProdID} → Quantity) (depends on the whole key, not partial).
(ii) Decomposition to 3NF (step-by-step) (5 marks)
Start:
SALES(OrderID, OrderDate, CustID, CustName, CustCity, ProdID, ProdName,
UnitPrice, Quantity, SalespersonID, SalespersonName, SalespersonRegion)
Step 1: Remove partial dependencies (to reach 2NF)
Create relations on determinants of partial dependencies:
1. ORDER(OrderID, OrderDate, CustID, SalespersonID)
(from OrderID → OrderDate, CustID, SalespersonID)
2. PRODUCT(ProdID, ProdName, UnitPrice)
(from ProdID → ProdName, UnitPrice)
********** 4 **********
--- page 5 ---
3. Keep line items for the fully dependent attribute:
SALES_LINE(OrderID, ProdID, Quantity) with PK (OrderID, ProdID)
Step 2: Remove transitive dependencies (to reach 3NF)
Separate dependents of non-key determinants:
4. CUSTOMER(CustID, CustName, CustCity)
(from CustID → CustName, CustCity)
5. SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
(from SalespersonID → SalespersonName, SalespersonRegion)
Now, in ORDER, CustID and SalespersonID remain as foreign keys only; their
descriptive attributes moved to their own tables, removing transitive dependencies.
All resulting tables are in 3NF:
•   Every non-key attribute depends on the key, the whole key, and nothing but the
key in its table.
(iii) Final set of relations with keys (2 marks)
•   ORDER(OrderID, OrderDate, CustID, SalespersonID)
FK: CustID → CUSTOMER, SalespersonID → SALESPERSON
• CUSTOMER(CustID, CustName, CustCity)
•   SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
• PRODUCT(ProdID, ProdName, UnitPrice)
•   SALES_LINE(OrderID, ProdID, Quantity)
FK: OrderID → ORDER, ProdID → PRODUCT
This decomposition is lossless and preserves the given FDs, with SALES_LINE capturing
the many-to-many between orders and products plus Quantity.
Q4   [20]
CO- 1 ;   a.   Discuss the major difficulties encountered while creating a database from scratch, and   [10]
SO - 2;   illustrate your answer with suitable examples.
BL-2   Building a database from scratch involves several conceptual, technical, and
organizational challenges that must be carefully addressed to ensure efficiency, accuracy,
and long-term usability.
1.   Requirement Analysis:
2.   Data Modeling Challenges:
3.   Data Redundancy and Integrity:
4.   Normalization and Performance Balance:
5.   Security and Access Control:
6.   Scalability and Future Growth:
7.   Backup and Recovery Planning:
CO- 2 ;   b.   Solve the following queries using relational algebra   [10]
SO - 2;   Customer(CustomerID, CustomerName, City)
BL-2   Order(OrderID, OrderDate, CustomerID)
Product(ProductID, ProductName, Price)
Order_Product(OrderID, ProductID, Quantity)
********** 5 **********
--- page 6 ---
(i)   Find the names of customers who have placed at least one order.
(ii)   Get the customer names and order IDs for orders placed after ‘2024-01-01’.
(iii)   List all products ordered by customers who live in ‘Chicago’.
(iv)   List the products that have been ordered by any customer with a quantity greater
than 1
(v)   Find all customers located in New York and have ordered something in month of
October 2024(assume date is in yyyy-mm-dd)
Q5   [20]
CO- 2 ;   a.   Consider the following table:   [10]
SO - 2;   employee (employee_id, first_name , last_name, email, phone_number , hire_date, job_id
BL-2   , salary, commission_pct , manager_id , department_id )
Write the SQL queries the following question:
i   Write a SQL query to find those employees who receive a higher salary than the employee   [3]
with ID 163. Return first name, last name.
Ans:
SELECT first_name, last_name
FROM employees
WHERE salary >
( SELECT salary
FROM employees
WHERE employee_id=163
);
ii   Write a SQL query to find out which employees have the same designation as the employee   [3]
whose ID is 169. Return first name, last name, department ID and job ID.
Ans:
SELECT first_name, last_name, salary, department_id, job_id
FROM employees
WHERE job_id =
( SELECT job_id
FROM employees
WHERE employee_id=169
);
iii   Write a SQL query to find those employees whose salary matches the lowest salary of any   [4]
of the departments. Return first name, last name and department ID
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE salary IN
(SELECT MIN(salary)
FROM employees
GROUP BY department_id
);
CO- 4 ;   b.   [10]
SO - 2;
BL- 2
********** 6 **********
--- page 7 ---
It is not conflict serilizable as the graph is cyclic.
Step   T1   T2   T3
1   T1: Read(A)
2   T1: Write(A)
3   T2: Read(A)
4   T2: Write(A)
5   T2: Read(B)
6   T3: Read(B)
7   T2: Write(B)
8   T3: Write(B)
Serializability ensures that a concurrent execution is equivalent to some serial order of
transactions. This preserves database correctness by preventing anomalies such as lost
updates, dirty reads, non-repeatable reads, and inconsistent results—while still allowing
concurrency for performance.
Q6   [20]
CO- 4 ;   a.   1. Definition of a Transaction   [10]
SO - 2;   A transaction is a logical unit of database processing that consists of one or more database
BL-3   operations such as read, write, insert, update, or delete.
It represents a single, indivisible unit of work that must be executed completely or not at
all.
Example:
T1:
Read(A)
A = A – 100
Write(A)
Read(B)
B = B + 100
Write(B)
This transaction transfers ₹100 from account A to account B.
2. ACID Properties of a Transaction
Property Meaning Example
Atomicity   All operations in a transaction must complete successfully; if any fails,
the entire transaction is rolled back. If the debit from A succeeds but the credit to B fails,
both changes are undone.
Consistency   A transaction transforms the database from one consistent state to
another, maintaining all integrity constraints.The total balance (A + B) remains the same
before and after the transfer.
Isolation Concurrent transactions should not interfere with each other; intermediate states
are invisible to others.   While T1 transfers money, another transaction T2 cannot read
the partially updated balance of A or B.
Durability   Once a transaction commits, its effects are permanently recorded in the
database, even after system failures.   After committing, the ₹100 transfer remains
intact even if the system crashes.
3. Conflict Serializability
A schedule is conflict-serializable if it can be transformed into a serial schedule by
swapping non-conflicting operations.
Two operations conflict if:
1.   They belong to different transactions.
2.   They operate on the same data item.
3.   At least one is a write operation.
********** 7 **********
--- page 8 ---
Example:
Step   Transaction   Operation
1   T1   Read(A)
2   T2   Read(A)
3   T1   Write(A)
4   T2   Write(A)
Here, conflicts occur between T1 and T2 on A.
Precedence graph: T1 → T2 (no cycle) ⇒ Conflict-serializable, equivalent to serial order
T1 → T2.
4. View Serializability
A schedule is view-serializable if it is view-equivalent to some serial schedule, i.e.,
•   Both schedules have the same read-from relationships (who reads whose value).
•   Both have the same final writes on each data item.
•   Both start from the same initial state.
Example:
S1: T1: W(A)
T2: R(A), W(A)
T3: R(A)
If both T2 and T3 read the value of A written by T1 and T2 does the final write,
then S1 is view-equivalent to the serial order T1 → T2 → T3.
5. Difference between Conflict and View Serializability
Aspect Conflict Serializability   View Serializability
Basis   Swapping of non-conflicting operations   Preservation of read-from and final-
write relationships
Detection   Using precedence (serialization) graph   More complex; requires
comparing read/write dependencies
Strictness   Stronger form — every conflict-serializable schedule is view-
serializable   Weaker — some non-conflict-serializable schedules can still be view-
serializable
Ease of Check   Easier to test algorithmically   Harder to test, computationally
expensive
Example Schedule without cycles in precedence graph   Schedule with blind writes
(where a value is overwritten without being read) may still be view-serializable but not
conflict-serializable
CO- 4 ;   b.   Aspect   ACID (RDBMS)   BASE (NoSQL / Distributed   [10]
SO - 2;   Systems)
BL-1   Philosophy   Ensures strict correctness Focuses on scalability and
and reliability   availability
Consistency   Strong consistency – all   Eventual consistency – nodes
Model   nodes see same data   become consistent over time
instantly
System Type   Centralized or small-   Distributed, large-scale, cloud-
scale transactional   based systems
systems
Transaction   Transactions are atomic   Transactions may be broken or
Handling   and isolated   partial across nodes
Availability vs.   Prioritizes consistency   Prioritizes availability over
Consistency   over availability   consistency
Response Time   Slower, due to strict   Faster, as some consistency is
locking and commit   relaxed
protocols
Use Cases   Banking, financial,   Social media feeds, e-commerce
inventory systems   catalogs, IoT data
Error Recovery   Rollback ensures   Recovery through replication
integrity after failures   and eventual updates
CAP Theorem CP systems (Consistency AP systems (Availability +
View   + Partition tolerance)   Partition tolerance)
Examples   Oracle, MySQL,   Cassandra, MongoDB, Amazon
PostgreSQL   DynamoDB
Q7   [20]
********** 8 **********
--- page 9 ---
CO-1 ;   A   Advantages of DBMS [5 Marks]   [5]
SO- 2;   1. Reduces Data Redundancy and Inconsistency
BL-1   – Data is stored centrally, avoiding duplication and ensuring all users see the
same updated information.
2. Improves Data Security
– Access to data is controlled through authentication and authorization,
protecting sensitive information.
3. Ensures Data Integrity and Accuracy
– Integrity constraints like primary keys and foreign keys maintain correctness of
data values.
4. Supports Concurrent Access and Sharing
– Multiple users can work on the same database simultaneously without
conflicts, using concurrency control.
5. Provides Backup and Recovery
– Automatic backup and recovery mechanisms protect data against crashes and
system failures.
CO- 2 ;   b   Joins in SQL [5 Marks]   [5]
SO - 2;   Definition:
BL-2   A JOIN in SQL is used to combine rows from two or more tables based on a related
column (usually a primary–foreign key relationship).
1. INNER JOIN
Returns only the matching rows from both tables.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
INNER JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows students who are enrolled in a course.
2. LEFT JOIN (LEFT OUTER JOIN)
Returns all rows from the left table, and matching rows from the right; non-matching rows
show NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
LEFT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students, even if not enrolled in any course.
3. RIGHT JOIN (RIGHT OUTER JOIN)
Returns all rows from the right table, and matching rows from the left; non-matching rows
show NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
RIGHT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all courses, even if no student has enrolled.
4. FULL JOIN (FULL OUTER JOIN)
Returns all rows from both tables; unmatched rows are filled with NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
FULL JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students and all courses, with NULLs where no match exists.
5. CROSS JOIN
Produces Cartesian product — every row of the first table with every row of the second.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
CROSS JOIN Courses;
Shows all possible combinations of students and courses.
Summary:
Type of Join   Description   Matching/Unmatched Rows
INNER JOIN Common records only   Matching only
LEFT JOIN   All left + matching right   Unmatched right → NULL
RIGHT JOIN   All right + matching left   Unmatched left → NULL
********** 9 **********
--- page 10 ---
FULL JOIN   All rows from both tables Unmatched → NULL
CROSS JOIN Cartesian product   No condition needed
CO- 3;   c   Armstrong’s Axioms [5 Marks]   [5]
SO - 2;   Definition:
BL-3   Armstrong’s Axioms are a set of inference rules used to derive all possible functional
dependencies (FDs) from a given set of FDs in a relational schema.
They form the theoretical foundation for normalization and dependency closure.
1. Basic Axioms
Axiom   Rule Description
a) Reflexivity   If Y ⊆ X, then X → Y. (A set of attributes determines any   If X =
of its subsets.)   B} →
b) Augmentation   If X → Y, then XZ → YZ. (Adding the same attribute(s) to   If A →
both sides preserves the dependency.)   BC.
c) Transitivity   If X → Y and Y → Z, then X → Z. (Dependencies can be   If A →
chained.)   then A
2. Derived (Additional) Axioms
Using the three basic rules, the following can be derived:
Derived Axiom   Meaning
Union (Additivity)   If X → Y and X → Z, then X → YZ
Decomposition (Projectivity)   If X → YZ, then X → Y and X → Z
Pseudo-transitivity   If X → Y and YZ → W, then XZ → W
3. Importance
•   These axioms help in finding attribute closure (X⁺)
•   Used to test dependency preservation and lossless decomposition during
normalization.
CO- 4 ;   d   "Key Value Pair Based   [5]
SO - 2;
BL-1   Data is stored in key/value pairs. It is designed in such a way to handle lots of data and
heavy load.
Key-value pair storage databases store data as a hash table where each key is unique, and
the value can be a JSON, BLOB(Binary Large Objects), string, etc.
For example, a key-value pair may contain a key like ""Website"" associated with a value
like ""Guru99"".
It is one of the most basic types of NoSQL databases. This kind of NoSQL database is
used as a collection, dictionaries, associative arrays, etc. Key value stores help the
developer to store schema-less data. They work best for shopping cart contents.
Redis, Dynamo, Riak are some examples of key-value store DataBases. They are all based
on Amazon's Dynamo paper.
Column-based
Column-oriented databases work on columns and are based on BigTable paper by Google.
Every column is treated separately. Values of single column databases are stored
contiguously.
Column based NoSQL database
They deliver high performance on aggregation queries like SUM, COUNT, AVG, MIN
etc. as the data is readily available in a column.
Column-based NoSQL databases are widely used to manage data warehouses, business
intelligence, CRM, Library card catalogs,
HBase, Cassandra, HBase, Hypertable are examples of column based database.
"
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper c307c067f119

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIDS_7056/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper fb50b0c62933

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIML_7053/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 64b831f27396

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AI_7012/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper ac61989e284f

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSBS_7036/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 669c0ddb947e

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSE_DS_7011/Database Management System/ANS_Database Management System(702CO0C067)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Database Management System
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Q1. is mandatory. Answer any 4 from the remaining questions.
Q1
Answer the following questions:
A.   5M for all the pointers covering advantages of DBMS in terms of security, availability and
integrity.
B.   -- 1. Display employee names whose salary is greater than 50,000
SELECT emp_name
FROM employee
WHERE salary > 50000;
-- 2. Display employee names working in 'HR' department
SELECT e.emp_name
FROM employee e
JOIN department d ON e.dept_id = d.dept_id
WHERE d.dept_name = 'HR';
-- 3. Display the number of employees in each department
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM department d
LEFT JOIN employee e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name;
Solution can include subquery or any operators also (1+2+2marks)
C.
Specialization+ generalization( Explanation+figure) (2.5m+2.5m)
D.
Active, partially committed, committed, failed, aborted, terminated – explanation (5 marks)
Q2   A.   ER diagram notation with entities, attributes, relationships (4+2+4)
********** 1 **********
--- page 2 ---
B.   ables: Patient(patient_id PK,…), Doctor(doctor_id PK,…, dept_id FK), Department(dept_id
PK,…), Room(room_id PK,…), Appointment(patient_id FK, doctor_id FK, date, time) (weak →
composite PK), Patient_Room(patient_id FK, room_id FK,…).
Cardinalities: Patient–Appointment (1:M), Doctor–Appointment (1:M), Doctor–Department
(M:1), Patient–Room (M:N over time).
Participation: Appointment total (both sides), Doctor total in Department, others mostly partial.
Any other assumptions to be considered (4+3+3 marks)
A.   -- 1. Display the average salary for each department id
SELECT dept_id, AVG(salary) AS avg_salary
FROM Employees
GROUP BY dept_id;
-- 2. Display employee names along with their department names
SELECT e.emp_name, d.dept_name
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;
-- 3. Display employees with a salary higher than the overall average salary
SELECT emp_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
-- 4. Create a view displaying employee id, employee name and salary
Q3
CREATE VIEW emp_salary_view AS
SELECT emp_id, emp_name, salary
FROM Employees;
-- 5. Display departments having more than 5 employees
SELECT dept_id
FROM Employees
GROUP BY dept_id
HAVING COUNT(emp_id) > 5;
Solution can include other ways too- like subqueries or operators. (2 marks each)
B.
DATA TYPE, NOT NULL, DEFAULT, and CHECK constraints. Foreign and Primary key-
explanation and syntax (2 marks each)
********** 2 **********
--- page 3 ---
A.
σauthor=′R.K. Narayan′(BOOK)
ρLIBRARY_BOOK(BOOK)
Q4.   πname(σcity=′Mumbai′(MEMBER))
πname(MEMBER⋈BORROW)
πtitle(σmember_id=′M101′(BORROW)⋈BOOK) (2 marks each)
B.   Left join- all the rows from left and matching from right
Right join- all the rows from right and matching from left
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.common_column = table2.common_column;
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.common_column = table2.common_column; (Explanation, output, sql query –
4+3+3marks)
A.   Solution include finding closures,
Candidate keys- AB,C
Check FD’s for normal forms
Q5
3NF not violating. decompose 3 relations. dependency not preserved. (10 marks for detailed
steps)
B.   Denormalization importance and example- 5 marks
1nf violation explanation and decomposition – 5 marks
A.   Draw the precedence graph
Checking for Blind Writes
Drawing a Dependency Graph
S is not view serializable. (Each step in detail- 3+3+4 marks)
Q6   B.   OLAP: Enables fast multidimensional analysis of data using operations like slice, dice, drill-
down.
ROLLUP: Generates hierarchical → reduces multiple GROUP BY queries.
CUBE: Computes all possible combinations of aggregates across dimensions → avoids writing
many complex aggregation queries.
Explanation+examples- 4+3+3 marks
A.
1. Super key, Candidate key and Primary key with example
Super Key is a set of attributes or columns that uniquely identifies each row table whereas; a
Q7   candidate key is a set of attributes that recognizes the tuples in a relation, or table. Primary Key –
is a column or group of columns in a table that uniquely identify every row in that table.
Candidate Key – is a set of attributes that uniquely identify tuples in a table. [2+2+2]
2. In serial schedules,
********** 3 **********
--- page 4 ---
All the transactions execute serially one after the other.
When one transaction executes, no other transaction is allowed to execute.
In non-serial schedules,
Multiple transactions execute concurrently.
Operations of all the transactions are inter leaved or mixed. (3+3 marks)
3. Indexing – definition, types, uses (4 marks)
4. 3 levels of abstraction with figure and explanation (4 marks).
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper e6fc154baccc

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSE_DS_7057/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper d2d7485d43d8

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CS_7055/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper cdacbfea9a41

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Computer_7002/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 681b67adab78

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_AI_7051/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 71253176b9d7

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_Computer_7047/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 622cd838cf93

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_DS_7052/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 3d433289eae7

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/Integrated_IT_7037/Database Management Systems/ANS_Database Management Systems(702AI0C001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech (DS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 28 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Diagrams must be neat and legible.
5. Ensure the correct question number is written in the answer sheet.
6. Qt1 is compulsary, attemp any 4 questions from remaining 6 questions.
Q1   Answer the following questions   [20]
CO- 1;   a   What are data models? Explain the Relational Model.   [5]
SO- 2;   1. Definition of Data Models (2 Marks)
BL- 1   A data model   is a conceptual framework that describes how data are structured,
stored, and manipulated in a database system.
It defines the   logical structure   of the database — the relationships among data, the
constraints, and the operations that can be performed.
Common types include:
•   Hierarchical Model
•   Network Model
•   Relational Model
•   Object Oriented Model
2. Relational Model (3 Marks)
The Relational Model organizes data into relations (tables) consisting of rows and
columns .
Each table (relation) represents an entity , each row (tuple) represents a record ,
and each column (attribute) represents a data field .
Every relation has a Primary Key that uniquely identifies each tuple.
Foreign Keys are used to establish relationships between tables.
Data are manipulated using Relational Algebra and the SQL language for operations
like selection, projection, join, and union.
Example:
| StudentID | Name | Branch |
|   |   |   |
| S101   | Riya   | IT   |
| S102   | Arjun | CS   |
Here, StudentID → Primary Key; the table “Student” represents the Student entity .
CO- 2;   b   1. Features of a Good Database Design (4 Marks)   [5]
SO - 2;   Data Integrity and Consistency:
BL- 2   Each piece of data is stored only once (no redundancy), ensuring consistency.
Example: Customer details stored in one CUSTOMER table, not repeated in every ORDER
record.
Minimal Data Redundancy:
Redundant data causes update anomalies and wasted storage.
Example: Instead of repeating department names for every employee, use a separate
DEPARTMENT table with a foreign key reference.
Proper Use of Normalization:
Splitting large tables into smaller ones to remove partial and transitive dependencies (1NF–
3NF).
********** 1 **********
--- page 2 ---
Example:   Separating   EMPLOYEE(EmpID,   EmpName,   DeptID)   and
DEPARTMENT(DeptID, DeptName).
Clear Entity–Relationship Mapping:
Logical relationships (1:1, 1:N, M:N) must be clearly defined using primary and foreign
keys.
Example: One‐to‐many between CUSTOMER and ORDER.
Scalability and Performance:
Well-designed indexes and relationships support fast queries and future data growth.
Example: Indexing OrderID in ORDERS table speeds up retrieval.
2. Conclusion (1 Mark)
A good database design is normalized, non-redundant, and supports data integrity, leading
to efficient storage, accurate information, and simplified maintenance.
CO- 3 ;   c   (a) Superkeys:   [5]
SO - 2;   {RollNo}, {Email}, {AadhaarNo}, {RollNo, Name}, {Email, Phone}, etc.
BL- 2   (b) Candidate Keys:
{RollNo}, {Email}, {AadhaarNo}
(c) Primary Key:
RollNo —unique.
CO- 4 ;   d   What is the significance of CAP theorem in NOSQL   [5]
SO - 2;   The CAP Theorem is a fundamental principle in NoSQL databases that describes the trade-
BL-1   offs among three key properties:
1.   Consistency (C): Every read receives the most recent write or an error.
2.   Availability (A): Every request receives a response, regardless of the state of the
data.
3.   Partition Tolerance (P): The system continues to operate even if network partitions
or communication failures occur.
Significance in NoSQL:
•   NoSQL databases are often distributed systems. The CAP theorem explains that it
is impossible to achieve all three properties simultaneously; a database can only fully
guarantee two out of three.
•   For example:
o   MongoDB prioritizes Consistency + Partition Tolerance (CP) by default.
o   Cassandra prioritizes Availability + Partition Tolerance (AP).
•   This helps developers choose the right database and configure it according to
application needs, balancing consistency, availability, and fault tolerance.
"
Q2   [20]
CO- 1 ;   a   [10]
SO - 2;
BL-2
CO- 2 ;   b   Consider following movie database:   [10]
SO - 2;
BL- 2   users (user_id, full_name, city, contact_no)
restaurants (restaurant_id, name, address, price level, is active)
********** 2 **********
--- page 3 ---
dishes (dish_id, restaurant, name, price, is_veg, is spicy)
ratings (user_id, dish_id, rating, rated_at, feedback)
Write the SQL queries the following question:
i   Add a new column “email” to users table   [2]
Ans:
ALTER TABLE users
ADD COLUMN email VARCHAR (40);
ii   Modify table dishes to enforce business rules “dishes.price must be > 0.” using CHECK   [2]
constraints
Ans:
ALTER TABLE dishes
ADD CONSTRAINT chk_price
CHECK (price > 0);
iii   Select all veg, not-spicy dishes with price <= 250 from active restaurants.   [2]
Ans:
SELECT d.name AS dish, r.name AS restaurant, d.price
FROM dishes d, restaurants r
Where r. restaurant_id = d. restaurant_id and r.is_active = ‘yes’ AND d.is_veg = ‘yes’
AND d.is_spicy is ‘No’ and d. price <= 250
iv   Show each restaurant’s average rating and number of ratings but return only those with at   [2]
least 2 ratings and an average ≥ 4.0.
Ans:
SELECT r.name AS restaurant, ROUND (AVG (rt. rating), 2) AS avg_rating,
COUNT (rt. rating) AS rating_count
FROM restaurants r, dishes d, ratings rt where d. restaurant_id = r. restaurant_id
And rt. dish_id = d. dish_id
GROUP BY r. restaurant_id, r.name
HAVING COUNT (rt. rating) >= 2
AND AVG (rt. rating) >= 4.0
v   Create a view called user_ratings which will show each rating alongside the user who   [2]
gave it.
CREATE OR REPLACE VIEW user_ratings AS
SELECT u.user_id, u. full_name, u. city, u. contact_no, r. dish_id, r. rating, r. rated_at,
r. feedback
FROM ratings r JOIN users u
ON u.user_id = r.user_id;
Q3   [20]
CO- 1 ;   a.   [10]
SO - 2;   Relational Schema Conversion
BL- 2   1. USER
USER(u_id PRIMARY KEY,   name,   email)
2. ADDRESS
ADDRESS(a_id PRIMARY KEY,   city,   state,   country,   u_id FOREIGN
KEY REFERENCES USER(u_id))
Relationship: User – lives in – Address → 1-to-M (one user can have many addresses)
3. ORDER
ORDER(o_no PRIMARY KEY,   order_amount,   order_date,   u_id FOREIGN
KEY REFERENCES USER(u_id))
Relationship: User – places – Order → 1-to-M
4. TRACKING_DETAIL
TRACKING_DETAIL(trac_id PRIMARY KEY,   status,   o_no
FOREIGN KEY REFERENCES ORDER(o_no))
Relationship: Order – contains – Tracking_detail → 1-to-M
5. PRODUCT_CATEGORY
PRODUCT_CATEGORY(cat_id PRIMARY KEY,   cat_name)
6. PRODUCT
PRODUCT(p_id PRIMARY KEY,   p_name,   price,   description,   cat_id
FOREIGN KEY REFERENCES PRODUCT_CATEGORY(cat_id))
********** 3 **********
--- page 4 ---
Relationship: Product – has – Product_Category → M-to-1
7. CART
CART(cart_id PRIMARY KEY)
8. PRODUCT_CART (resolving M-N between Product and Cart)
PRODUCT_CART(p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
cart_id FOREIGN KEY REFERENCES CART(cart_id),
PRIMARY KEY (p_id, cart_id))
Relationship: Product – added to – Cart → M-to-N
9. ORDER_PRODUCT (resolving M-N between Order and Product)
ORDER_PRODUCT(o_no FOREIGN KEY REFERENCES ORDER(o_no),
p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
PRIMARY KEY (o_no, p_id))
Relationship: Order – contains – Product → M-to-N
CO- 3 ;   b.   (i) Partial & Transitive dependencies (3 marks)   [10]
SO - 2;
BL- 3   Candidate key (in SALES): ({OrderID, ProdID})
(Quantity needs both; everything else is determined by either OrderID, CustID, ProdID,
or SalespersonID.)
Partial dependencies (depend on part of composite key)
•   OrderID → OrderDate, CustID, SalespersonID
(These don’t need ProdID.)
•   ProdID → ProdName, UnitPrice
(These don’t need OrderID.)
•   SalespersonID → SalespersonName, SalespersonRegion and
CustID → CustName, CustCity are not on the key, but in the single SALES table
they appear as attributes that are determined by non-key attributes—handled
under transitive below.
Transitive dependencies (key → nonkey → other nonkeys)
•   OrderID → CustID and CustID → CustName, CustCity
⇒ OrderID → CustName, CustCity (transitive).
•   OrderID → SalespersonID and SalespersonID → SalespersonName,
SalespersonRegion
⇒ OrderID → SalespersonName, SalespersonRegion (transitive).
Full dependency:
•   ({OrderID, ProdID} → Quantity) (depends on the whole key, not partial).
(ii) Decomposition to 3NF (step-by-step) (5 marks)
Start:
SALES(OrderID, OrderDate, CustID, CustName, CustCity, ProdID, ProdName,
UnitPrice, Quantity, SalespersonID, SalespersonName, SalespersonRegion)
Step 1: Remove partial dependencies (to reach 2NF)
Create relations on determinants of partial dependencies:
1. ORDER(OrderID, OrderDate, CustID, SalespersonID)
(from OrderID → OrderDate, CustID, SalespersonID)
2. PRODUCT(ProdID, ProdName, UnitPrice)
(from ProdID → ProdName, UnitPrice)
********** 4 **********
--- page 5 ---
3. Keep line items for the fully dependent attribute:
SALES_LINE(OrderID, ProdID, Quantity) with PK (OrderID, ProdID)
Step 2: Remove transitive dependencies (to reach 3NF)
Separate dependents of non-key determinants:
4. CUSTOMER(CustID, CustName, CustCity)
(from CustID → CustName, CustCity)
5. SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
(from SalespersonID → SalespersonName, SalespersonRegion)
Now, in ORDER, CustID and SalespersonID remain as foreign keys only; their
descriptive attributes moved to their own tables, removing transitive dependencies.
All resulting tables are in 3NF:
•   Every non-key attribute depends on the key, the whole key, and nothing but the
key in its table.
(iii) Final set of relations with keys (2 marks)
•   ORDER(OrderID, OrderDate, CustID, SalespersonID)
FK: CustID → CUSTOMER, SalespersonID → SALESPERSON
• CUSTOMER(CustID, CustName, CustCity)
•   SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
• PRODUCT(ProdID, ProdName, UnitPrice)
•   SALES_LINE(OrderID, ProdID, Quantity)
FK: OrderID → ORDER, ProdID → PRODUCT
This decomposition is lossless and preserves the given FDs, with SALES_LINE capturing
the many-to-many between orders and products plus Quantity.
Q4   [20]
CO- 1 ;   a.   Discuss the major difficulties encountered while creating a database from scratch, and   [10]
SO - 2;   illustrate your answer with suitable examples.
BL-2   Building a database from scratch involves several conceptual, technical, and
organizational challenges that must be carefully addressed to ensure efficiency, accuracy,
and long-term usability.
1.   Requirement Analysis:
2.   Data Modeling Challenges:
3.   Data Redundancy and Integrity:
4.   Normalization and Performance Balance:
5.   Security and Access Control:
6.   Scalability and Future Growth:
7.   Backup and Recovery Planning:
CO- 2 ;   b.   Solve the following queries using relational algebra   [10]
SO - 2;   Customer(CustomerID, CustomerName, City)
BL-2   Order(OrderID, OrderDate, CustomerID)
Product(ProductID, ProductName, Price)
Order_Product(OrderID, ProductID, Quantity)
********** 5 **********
--- page 6 ---
(i)   Find the names of customers who have placed at least one order.
(ii)   Get the customer names and order IDs for orders placed after ‘2024-01-01’.
(iii)   List all products ordered by customers who live in ‘Chicago’.
(iv)   List the products that have been ordered by any customer with a quantity greater
than 1
(v)   Find all customers located in New York and have ordered something in month of
October 2024(assume date is in yyyy-mm-dd)
Q5   [20]
CO- 2 ;   a.   Consider the following table:   [10]
SO - 2;   employee (employee_id, first_name , last_name, email, phone_number , hire_date, job_id
BL-2   , salary, commission_pct , manager_id , department_id )
Write the SQL queries the following question:
i   Write a SQL query to find those employees who receive a higher salary than the employee   [3]
with ID 163. Return first name, last name.
Ans:
SELECT first_name, last_name
FROM employees
WHERE salary >
( SELECT salary
FROM employees
WHERE employee_id=163
);
ii   Write a SQL query to find out which employees have the same designation as the employee   [3]
whose ID is 169. Return first name, last name, department ID and job ID.
Ans:
SELECT first_name, last_name, salary, department_id, job_id
FROM employees
WHERE job_id =
( SELECT job_id
FROM employees
WHERE employee_id=169
);
iii   Write a SQL query to find those employees whose salary matches the lowest salary of any   [4]
of the departments. Return first name, last name and department ID
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE salary IN
(SELECT MIN(salary)
FROM employees
GROUP BY department_id
);
CO- 4 ;   b.   [10]
SO - 2;
BL- 2
********** 6 **********
--- page 7 ---
It is not conflict serilizable as the graph is cyclic.
Step   T1   T2   T3
1   T1: Read(A)
2   T1: Write(A)
3   T2: Read(A)
4   T2: Write(A)
5   T2: Read(B)
6   T3: Read(B)
7   T2: Write(B)
8   T3: Write(B)
Serializability ensures that a concurrent execution is equivalent to some serial order of
transactions. This preserves database correctness by preventing anomalies such as lost
updates, dirty reads, non-repeatable reads, and inconsistent results—while still allowing
concurrency for performance.
Q6   [20]
CO- 4 ;   a.   1. Definition of a Transaction   [10]
SO - 2;   A transaction is a logical unit of database processing that consists of one or more database
BL-3   operations such as read, write, insert, update, or delete.
It represents a single, indivisible unit of work that must be executed completely or not at
all.
Example:
T1:
Read(A)
A = A – 100
Write(A)
Read(B)
B = B + 100
Write(B)
This transaction transfers ₹100 from account A to account B.
2. ACID Properties of a Transaction
Property Meaning Example
Atomicity   All operations in a transaction must complete successfully; if any fails,
the entire transaction is rolled back. If the debit from A succeeds but the credit to B fails,
both changes are undone.
Consistency   A transaction transforms the database from one consistent state to
another, maintaining all integrity constraints.The total balance (A + B) remains the same
before and after the transfer.
Isolation Concurrent transactions should not interfere with each other; intermediate states
are invisible to others.   While T1 transfers money, another transaction T2 cannot read
the partially updated balance of A or B.
Durability   Once a transaction commits, its effects are permanently recorded in the
database, even after system failures.   After committing, the ₹100 transfer remains
intact even if the system crashes.
3. Conflict Serializability
A schedule is conflict-serializable if it can be transformed into a serial schedule by
swapping non-conflicting operations.
Two operations conflict if:
1.   They belong to different transactions.
2.   They operate on the same data item.
3.   At least one is a write operation.
********** 7 **********
--- page 8 ---
Example:
Step   Transaction   Operation
1   T1   Read(A)
2   T2   Read(A)
3   T1   Write(A)
4   T2   Write(A)
Here, conflicts occur between T1 and T2 on A.
Precedence graph: T1 → T2 (no cycle) ⇒ Conflict-serializable, equivalent to serial order
T1 → T2.
4. View Serializability
A schedule is view-serializable if it is view-equivalent to some serial schedule, i.e.,
•   Both schedules have the same read-from relationships (who reads whose value).
•   Both have the same final writes on each data item.
•   Both start from the same initial state.
Example:
S1: T1: W(A)
T2: R(A), W(A)
T3: R(A)
If both T2 and T3 read the value of A written by T1 and T2 does the final write,
then S1 is view-equivalent to the serial order T1 → T2 → T3.
5. Difference between Conflict and View Serializability
Aspect Conflict Serializability   View Serializability
Basis   Swapping of non-conflicting operations   Preservation of read-from and final-
write relationships
Detection   Using precedence (serialization) graph   More complex; requires
comparing read/write dependencies
Strictness   Stronger form — every conflict-serializable schedule is view-
serializable   Weaker — some non-conflict-serializable schedules can still be view-
serializable
Ease of Check   Easier to test algorithmically   Harder to test, computationally
expensive
Example Schedule without cycles in precedence graph   Schedule with blind writes
(where a value is overwritten without being read) may still be view-serializable but not
conflict-serializable
CO- 4 ;   b.   Aspect   ACID (RDBMS)   BASE (NoSQL / Distributed   [10]
SO - 2;   Systems)
BL-1   Philosophy   Ensures strict correctness Focuses on scalability and
and reliability   availability
Consistency   Strong consistency – all   Eventual consistency – nodes
Model   nodes see same data   become consistent over time
instantly
System Type   Centralized or small-   Distributed, large-scale, cloud-
scale transactional   based systems
systems
Transaction   Transactions are atomic   Transactions may be broken or
Handling   and isolated   partial across nodes
Availability vs.   Prioritizes consistency   Prioritizes availability over
Consistency   over availability   consistency
Response Time   Slower, due to strict   Faster, as some consistency is
locking and commit   relaxed
protocols
Use Cases   Banking, financial,   Social media feeds, e-commerce
inventory systems   catalogs, IoT data
Error Recovery   Rollback ensures   Recovery through replication
integrity after failures   and eventual updates
CAP Theorem CP systems (Consistency AP systems (Availability +
View   + Partition tolerance)   Partition tolerance)
Examples   Oracle, MySQL,   Cassandra, MongoDB, Amazon
PostgreSQL   DynamoDB
Q7   [20]
********** 8 **********
--- page 9 ---
CO-1 ;   A   Advantages of DBMS [5 Marks]   [5]
SO- 2;   1. Reduces Data Redundancy and Inconsistency
BL-1   – Data is stored centrally, avoiding duplication and ensuring all users see the
same updated information.
2. Improves Data Security
– Access to data is controlled through authentication and authorization,
protecting sensitive information.
3. Ensures Data Integrity and Accuracy
– Integrity constraints like primary keys and foreign keys maintain correctness of
data values.
4. Supports Concurrent Access and Sharing
– Multiple users can work on the same database simultaneously without
conflicts, using concurrency control.
5. Provides Backup and Recovery
– Automatic backup and recovery mechanisms protect data against crashes and
system failures.
CO- 2 ;   b   Joins in SQL [5 Marks]   [5]
SO - 2;   Definition:
BL-2   A JOIN in SQL is used to combine rows from two or more tables based on a related
column (usually a primary–foreign key relationship).
1. INNER JOIN
Returns only the matching rows from both tables.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
INNER JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows students who are enrolled in a course.
2. LEFT JOIN (LEFT OUTER JOIN)
Returns all rows from the left table, and matching rows from the right; non-matching rows
show NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
LEFT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students, even if not enrolled in any course.
3. RIGHT JOIN (RIGHT OUTER JOIN)
Returns all rows from the right table, and matching rows from the left; non-matching rows
show NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
RIGHT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all courses, even if no student has enrolled.
4. FULL JOIN (FULL OUTER JOIN)
Returns all rows from both tables; unmatched rows are filled with NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
FULL JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students and all courses, with NULLs where no match exists.
5. CROSS JOIN
Produces Cartesian product — every row of the first table with every row of the second.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
CROSS JOIN Courses;
Shows all possible combinations of students and courses.
Summary:
Type of Join   Description   Matching/Unmatched Rows
INNER JOIN Common records only   Matching only
LEFT JOIN   All left + matching right   Unmatched right → NULL
RIGHT JOIN   All right + matching left   Unmatched left → NULL
********** 9 **********
--- page 10 ---
FULL JOIN   All rows from both tables Unmatched → NULL
CROSS JOIN Cartesian product   No condition needed
CO- 3;   c   Armstrong’s Axioms [5 Marks]   [5]
SO - 2;   Definition:
BL-3   Armstrong’s Axioms are a set of inference rules used to derive all possible functional
dependencies (FDs) from a given set of FDs in a relational schema.
They form the theoretical foundation for normalization and dependency closure.
1. Basic Axioms
Axiom   Rule Description
a) Reflexivity   If Y ⊆ X, then X → Y. (A set of attributes determines any   If X =
of its subsets.)   B} →
b) Augmentation   If X → Y, then XZ → YZ. (Adding the same attribute(s) to   If A →
both sides preserves the dependency.)   BC.
c) Transitivity   If X → Y and Y → Z, then X → Z. (Dependencies can be   If A →
chained.)   then A
2. Derived (Additional) Axioms
Using the three basic rules, the following can be derived:
Derived Axiom   Meaning
Union (Additivity)   If X → Y and X → Z, then X → YZ
Decomposition (Projectivity)   If X → YZ, then X → Y and X → Z
Pseudo-transitivity   If X → Y and YZ → W, then XZ → W
3. Importance
•   These axioms help in finding attribute closure (X⁺)
•   Used to test dependency preservation and lossless decomposition during
normalization.
CO- 4 ;   d   "Key Value Pair Based   [5]
SO - 2;
BL-1   Data is stored in key/value pairs. It is designed in such a way to handle lots of data and
heavy load.
Key-value pair storage databases store data as a hash table where each key is unique, and
the value can be a JSON, BLOB(Binary Large Objects), string, etc.
For example, a key-value pair may contain a key like ""Website"" associated with a value
like ""Guru99"".
It is one of the most basic types of NoSQL databases. This kind of NoSQL database is
used as a collection, dictionaries, associative arrays, etc. Key value stores help the
developer to store schema-less data. They work best for shopping cart contents.
Redis, Dynamo, Riak are some examples of key-value store DataBases. They are all based
on Amazon's Dynamo paper.
Column-based
Column-oriented databases work on columns and are based on BigTable paper by Google.
Every column is treated separately. Values of single column databases are stored
contiguously.
Column based NoSQL database
They deliver high performance on aggregation queries like SUM, COUNT, AVG, MIN
etc. as the data is readily available in a column.
Column-based NoSQL databases are widely used to manage data warehouses, business
intelligence, CRM, Library card catalogs,
HBase, Cassandra, HBase, Hypertable are examples of column based database.
"
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 51d1c2aaacaa

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_Computer_7032/Database Management Systems/ANS_Database Management Systems(702AI0C001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 34d14c534a00

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_DS_7038/Database Management Systems/ANS_Database Management Systems(702AI0C001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 72.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
CO-1 ;   a.   In database Design, describe the steps involved in converting user requirements
[5]
BL-2   into a conceptual E-R model or schema.
Requirement Collection and Analysis (1 Mark)
● The first step is to gather user requirements about the data and
operations required in the database.
● Information is collected through interviews, questionnaires,
and existing documents.
● The goal is to understand what data needs to be stored and
how users interact with it.
2. Identify Entities and Attributes (1 Mark)
Ans.   ● After analyzing requirements, identify main entities (objects) in
the system.
● Determine their attributes that describe each entity.
● Example: In a library system → Book, Member, Publisher.
3. Identify Relationships (1 Mark)
● Determine how entities are related to each other.
● Specify relationship types and cardinality ratios such as:
○ One-to-One , One-to-Many,Many-to-Many.
4. Specify Constraints (1 Mark)
********** 1 **********
--- page 2 ---
● Define various constraints that apply to the data, such as:
○ Key constraints (Primary keys)
○ Participation constraints
○ Domain constraints
● These ensure data integrity and consistency.
5. Create Conceptual Schema (ER Diagram) (1 Mark)
● Finally, represent the design using a conceptual model, usually
an Entity–Relationship (ER) diagram.
● The ER diagram shows entities, attributes, relationships, and
constraints in a graphical form.
Summary:
The process involves requirement analysis → entity identification →
relationship identification → constraint specification → conceptual
schema creation.
CO-2 ;   b.   Enlist the outer joins and explain left outer join with example   [5]
BL-2
Enlist outer joins-1Mark
Left outer join explanation +example[2Marks+2Marks]
Three types of outer joins are:
1. Left Outer Join (⟕)
2. Right Outer Join (⟖)
3. Full Outer Join (⟗)
A Left Outer Join returns:
•   All tuples from the left relation
• Matching tuples from the right relation
•   If there is no match, NULL values are filled for the right
relation attributes
Ans.   Consider two relations Employee and Department
Employee⟕E.DeptID=D.DeptIDDepartment
********** 2 **********
--- page 3 ---
c.   Define Functional Dependency (FD). Explain types of functional
CO-3 ;   [5]
BL-1   dependencies with suitable examples.
DEF: 2 MARKS
TYPES : 2 MARKS
EXAMPLE: 1 MARK
Functional Dependency (FD)
A Functional Dependency (FD) is a constraint between two sets of
attributes in a relation. It specifies that the value of one attribute (or a
set of attributes) uniquely determines the value of another attribute.
Ex: In relation Student(StudentID, Na/me, Dept) | StudentID → Name
| StudentID → Dept
1. Full Functional Dependency
A functional dependency X → Y is said to be full if Y is dependent on
the entire set of attributes in X, and not on any proper subset of X.
Example: Relation: R(StudentID, CourseID, Marks) | FD: (StudentID,
Ans.
CourseID) → Marks
Here, Marks depends on both StudentID and CourseID together. Neither
StudentID nor CourseID alone can determine Marks. Hence, it is a full
functional dependency.
2. Partial Functional Dependency
A functional dependency is partial if a non-prime attribute depends on
only a part of a composite key.
Example: Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
3. Transitive Dependency
A functional dependency is transitive if a non-key attribute depends on
another non-key attribute.
Example: Relation: R(A, B, C) FDs: A → B | B → C
d.   Discuss at least three applications of MongoDB in modern software
CO-4 ;   [5]
BL-2   development.
Applications – 1 Marks each
Examples – 2 Marks
This question assesses the student's understanding of where and why
MongoDB is an appropriate choice in real-world applications. A
complete answer should identify and explain at least five use cases
Ans.
where MongoDB excels:
Content Management Systems (CMS) - flexible schema for diverse
content types (articles, videos, comments) without rigid table structures.
Real-time Analytics and Big Data - high-velocity data ingestion and
aggregation for log data, clickstream analytics, and IoT sensor data.
********** 3 **********
--- page 4 ---
Mobile and Social Media Applications - document model maps
naturally to JSON objects for user profiles, posts, and social graphs
with varying attributes.
E-commerce Product Catalogs - products with different attributes
stored without schema migrations; fast product searches and
recommendations.
Gaming Applications - evolving game features, player profiles, and
inventories with horizontal scalability for millions of concurrent
players.
Other examples include: geospatial applications (location-based
services using MongoDB's geospatial queries), single-page applications
(JSON-based REST APIs), personalization engines (storing user
preferences and behavior), session storage (web application session
management), event logging and monitoring (storing application logs and
metrics), document management systems (storing files with metadata).
a.   Describe all types of database users in brief? Explain DBA roles and
Q2
responsibilities.   [10]
CO-1;
BL-2   Define data models and explain Relational model in detail.
Types of Database users – 3 Marks
DBA Roles and Responsibilities – 2 Marks
Data Model Definition - 2 Marks
Relational Model – 3 Marks
1. Naive Users (1M)
o Use predefined applications (e.g., ATM users, bank clerks)
o Do not have deep DB knowledge
2. Application Programmers (1M)
o Write programs using languages like SQL, Java
o Develop user interfaces to interact with DB
Ans.
3. Sophisticated Users (1M)
o Use query languages directly (SQL)
o Perform complex queries and analysis
4. Specialized Users (1M)
o Develop special applications (AI, CAD, Data Mining)
o Require advanced DB operations
5. Database Administrator (DBA) (1M)
o Manages database security, backup, performance
o Ensures smooth functioning of DBMS
The process of defining the conceptual design of data elements and their inter-
relationships is called data modeling.Any change in the order in which various
data elements are placed results in changes in the application programs using
the data file. The data-base approach uses a common data model for the entire
********** 4 **********
--- page 5 ---
database and the user program is not concerned with the placement of a
particular data element. The database management system (DBMS) acts as an
interface between the database and the user programs.
a. Hierarchical model
b. Network model
c. Relational model
Relational Model:
The most recent and popular model of data-base design is the relational
database model. This model was devel-oped to overcome the problems of
complexity and inflexibility of the earlier two models in handling databases
with many-to-many rela-tionships between entities. In the relational database,
each file is perceived as a flat file (a two dimensional table) consisting of
many lines (records), each record having key and non-key data item(s). The
key item(s) is the data element(s) that identifies the record.
b.   Consider the following relational schema:
BOOK (BID, Title, Author, Genre)
READER (RID, Name, City)
BORROW (RID, BID, Days)
Answer the following using relational algebra queries:
CO-2;   1. Find the names of readers who borrowed books of genre   [10]
BL-3   ‘Fiction’.
2. Find title of book written by author ‘Chetan Bhagat’.
3. Find the names of readers who borrowed books for more than 7
days.
4. Find the titles of books borrowed by readers from Mumbai.
5. Find the ids of readers who have not borrowed any books
Marks [2*5=10M]
1. Find the names of readers who borrowed books of genre
‘Fiction’.
πName((σGenre=’Fiction’(BOOK)⋈BORROW)⋈READER)
Ans.
2. Find title of book written by author ‘Chetan Bhagat’.
πTitle(σAuthor=′Chetan Bhagat′(BOOK))
3. Find the names of readers who borrowed books for more than 7
days.
********** 5 **********

[Text in pictures on this page, read by OCR]
Customer CustomerID | Name | Address | Contact |Amount Due
e

I i _
date ee Invoice_No Customer_id | Date Payment | Delivery
Terms terms
Line Item
File Invoice_No | Serial No. Product_code Quantity
ee

Prod: ——

File “ct [Product_code | Description [Unit of Price per | Stock on
measurement | Unit hand

Fig.9.6 Relational data model for a customer invoicing system
--- page 6 ---
πName((σDays > 7(BORROW)⋈READER))
4. Find the titles of books borrowed by readers from Mumbai.
πTitle((σCity=’Mumbai’(READER)⋈BORROW)⋈BOOK)
5. Find the ids of readers who have not borrowed any books
πRID(READER)−πRID(BORROW)
a.   Consider the set of relations and answer the following SQL queries:
Book(book_id, title, author, price)
Member(member_id, name, join_date)
Borrow(borrow_id, member_id, book_id, borrow_date, return_date)
Q3
[10]
CO-2;   i.   Display member names with borrowed book titles
BL-3
ii.   Display members who borrowed more than 3 books
iii.   Create a view “Expensive_books” to display only those books whose
price is greater than 500
iv.   Find members who have not borrowed any book.
v.   Reduce book price by 5% where price > 1000
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
i.   SELECT m.name, b.title
FROM Member m
JOIN Borrow br ON m.member_id = br.member_id
JOIN Book b ON br.book_id = b.book_id;
ii.   SELECT member_id
FROM Borrow
GROUP BY member_id
HAVING COUNT(*) > 3;
Ans.
iii. CREATE VIEW expensive_books AS
SELECT book_id, title, price
FROM Book
WHERE price > 500;
iv.   SELECT name
FROM Member
WHERE member_id NOT IN (SELECT member_id FROM Borrow);
v. UPDATE Book
SET price = price * 0.95
WHERE price > 1000;
b.   Define and explain Second Normal Form (2NF) and Third Normal Form
CO-3;   (3NF).
[10]
BL-3   Consider Relation R(A, B, C, D, E, F) having
Functional Dependencies:
********** 6 **********
--- page 7 ---
AB → CD | A → E | C → F
Convert the following relation into 3NF, show all steps.
4+6 MARKS
Second Normal Form (2NF)
A relation is said to be in Second Normal Form (2NF) if the relation is
already in First Normal Form (1NF), and there is no partial dependency,
i.e., every non-prime attribute is fully functionally dependent on the
entire candidate key.
Example Relation: R(StudentID, CourseID, StudentName) | StudentID
→ StudentName
Candidate Key: (StudentID, CourseID)
Here, StudentName depends only on StudentID, which is part of the key
⇒ Partial Dependency ⇒ Not in 2NF
Third Normal Form (3NF)
Ans.
A relation is said to be in Third Normal Form (3NF) if the relation is in
Second Normal Form (2NF), and there is no transitive dependency, i.e.,
non-prime attributes do not depend on other non-prime attributes.
Example, Relation: R(A, B, C) | Functional Dependencies: A → B | B
→ C
Here, A → C indirectly through B ⇒ Transitive Dependency ⇒ Not in
3NF
KEY: AB
Final 3NF Decomposition
R1(A, E) | A → E
R2(C, F) | C → F
R3(A, B, C, D) | AB → CD
a.   A company database needs to store information about employees
(identified by SSN, with salary and phone as attributes), departments
(identified by DNO, with dname and budget as attributes), and children
Q4   of employees (with name and age as attributes). Employees work in
departments; each department is managed by an employee; a child must [10]
CO-1;
be identified uniquely by name when the parent (who is an employee;
BL-3
assume that only one parent works for the company) is known. We are
not interested in information about a child once the parent leaves the
company.
Draw an ER diagram that captures this information.
Ans.
Step   Criteria   Marks
********** 7 **********
--- page 8 ---
1   Entity   2.0
Identification
2   Attributes   2.0
3   Primary Keys   1.5
(PK)
4   Foreign Keys   1.5
(FK)
5   Cardinalities   2.0
6   Notation &   1.0
Clarity
b.   What are the different types of constraints in SQL? Explain at least 3
constraints with suitable examples.
Consider the following relations:
Employee
CO-2;   emp_id name   dept_id
BL-2   1   Amit   10   [10]
2   Neha   20
3   Ravi   30
Department
dept_id   dept_name
10   HR
20   IT
40   Sales
********** 8 **********
--- page 9 ---
Interpret the output of:
a) Employee LEFT OUTER JOIN Department
b) Employee FULL OUTER JOIN Department
Give 1 mark each for explaining the constraint; 2 marks for examples. If only
a correct example is written without explanation, marks should still be
awarded.
In SQL, there are 5 main types of constraints:
1. NOT NULL – Ensures a column cannot have NULL values.
Example: name VARCHAR(50) NOT NULL
2. UNIQUE – Ensures all values in a column are different.
Example: email VARCHAR(100) UNIQUE
3. PRIMARY KEY – Uniquely identifies each record (NOT NULL +
UNIQUE).
Example: emp_id INT PRIMARY KEY
4. FOREIGN KEY – Maintains relationship between two tables.
Example:   FOREIGN   KEY   (dept_id)   REFERENCES
Department(dept_id)
5. CHECK – Ensures values satisfy a condition.
Example: salary INT CHECK (salary > 0)
Ans.
Give 2.5 marks to (a) and 2.5 marks to (b) for correct output.
a) LEFT OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
b) FULL OUTER JOIN
emp_id   name   dept_id   dept_name
1   Amit   10   HR
2   Neha   20   IT
3   Ravi   30   NULL
NULL   NULL   40   Sales
a.   a) Define serial and non-serial schedules. Explain with suitable
examples.
b) A schedule S involves three transactions T1, T2, and T3
Q5   executing concurrently. The operations on data items X and Y
are shown in the given schedule.
CO-4;   [10]
Perform the following Tasks:
BL-3
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not.
iii. If it is serializable, write the equivalent serial order of the
transactions.
********** 9 **********
--- page 10 ---
T1   T2   T3
R(X)
R(Y)
R(Y)
W(Y)
W(X)
W(X)
R(X)
W(X)
Define serial and non-serial schedules – 4 Marks
Construct the precedence graph – 3 Marks
Determine conflict serializable – 2 Marks
Equivalent serial order – 1Mark
a) In Database Management Systems, a schedule is the sequence in which
the operations of multiple transactions are executed in the database
system.
1. Serial Schedule
A serial schedule is a schedule in which transactions are executed one
after another without any interleaving of operations. One transaction
completes entirely before the next transaction begins.
Example
Consider two transactions:
Transaction T1
• Read(A)
• A = A + 50
Ans.   • Write(A)
Transaction T2
• Read(A)
• A = A – 30
• Write(A)
Serial Schedule:
Step   Operation
1   T1: Read(A)
2   T1: A = A + 50
3   T1: Write(A)
4   T2: Read(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, T1 completes first and then T2 starts, so no operations are mixed.
This ensures data consistency but reduces concurrency.
2. Non-Serial Schedule
********** 10 **********
--- page 11 ---
A non-serial schedule is a schedule where operations of multiple
transactions   are   interleaved,   meaning   transactions   execute
concurrently.
Example:
Step   Operation
1   T1: Read(A)
2   T2: Read(A)
3   T1: A = A + 50
4   T1: Write(A)
5   T2: A = A – 30
6   T2: Write(A)
Here, operations of T1 and T2 are mixed together, allowing multiple
transactions to execute simultaneously.
B i)
ii) As there is no loop in the graph (the graph is DAG), it is conflict
serializable schedule as well as a serial schedule. Since it is a serial
schedule, we can detect the order of transactions as well.
iii) The order of Transaction: T1 will execute first as there is no incoming
edge on T1. T3 will execute second as it depends on T1 only. T2 will
execute
at last as it depends on both T1 and T3.
So, order of its equivalent serial schedule is : T1->T3->T2
b.   Given relation R(A, B, C, D, E, F, G) with functional dependencies:
F = {A →B,  BC →D,  D →E,  CF →G,  E →A,  G →F}
Answer the following questions:
CO-3;   1. Compute {A}+, {C}+, {AC}+, and {CF}+.
BL-3   2. Find all candidate keys for relation R. Show your work for each   [10]
candidate key verification.
3. Identify prime and non-prime attributes.
4. Determine the highest normal form of R with justification and
convert it till 2NF.
1. 3 marks
2. 2 marks
Ans.   3. 1 mark
4. 4 marks
********** 11 **********
--- page 12 ---
1. Attribute Closures
• A⁺:
A → B → (B,C not available) ⇒ no BC
A⁺ = {A, B}
•   C⁺:
No FD starts with C alone
C⁺ = {C}
• AC⁺:
A → B ⇒ {A, B, C}
BC → D ⇒ {D}
D → E ⇒ {E}
E → A (already)
AC⁺ = {A, B, C, D, E}
• CF⁺:
CF → G ⇒ {G}
G → F (already)
CF⁺ = {C, F, G}
2. Candidate Keys
Check minimal sets:
• (A, C, F)⁺:
A → B, BC → D, D → E, E → A
CF → G, G → F
{A, B, C, D, E, F, G} ✔
(A, C, F) is a candidate key
• No proper subset gives all attributes
Only candidate key: (A, C, F)
3. Prime & Non-Prime Attributes
• Prime: A, C, F
• Non-Prime: B, D, E, G
4. Highest Normal Form
•   Partial dependency exists:
A → B (A is part of key)
Violates 2NF
Highest Normal Form = 1NF
a.   A University’s Research Management System stores information about
Professors, Research Projects, Students, and Funding Agencies.
Requirements:
• Each Professor has ProfID, Name, Department, and Email.
• Each Research Project has ProjectID, Title, StartDate, and
Budget.
• A professor can work on multiple projects, and a project may
Q6
involve multiple professors.
CO-1;   • Each project is funded by one funding agency, but an agency may [10]
BL-3   fund multiple projects.
• Each Funding Agency has AgencyID, AgencyName, and Country.
• Students can participate in research projects. A student may work
on multiple projects.
• For each student’s participation, store Role and Duration.
Tasks:
********** 12 **********
--- page 13 ---
1. Draw the ER diagram including entities, attributes, and
relationships.
2. Identify relationship types and constraints.
3. Convert the ER model into relational tables.
Ans.
1. Draw the ER diagram including entities, attributes, and
relationships. 5 Marks
2. Identify relationship types (1:1, 1:N, M:N) and constraints. 2
Marks
3. Convert the ER model into relational tables. 3 Marks
b.   Read the following scenarios carefully. For each case, determine the
relevant ACID properties and explain how the identified property ensures
reliable and correct transaction processing in a Database Management
CO-4;
BL-2   Systems.   [10]
Case 1:
An online banking system performs a transaction to transfer ₹10,000
from Account A to Account B. The system deducts the amount from
********** 13 **********
--- page 14 ---
Account A, but before the amount is credited to Account B, the server
crashes.
Case 2:
Two users attempt to book the last available seat on a flight at the same
time using an airline reservation system. Both users submit their
booking requests simultaneously.
In the airline reservation example, two users attempt to book the same
last available seat simultaneously. Isolation ensures that when one user's
booking transaction is being processed, the other user's transaction
cannot access or modify the same seat information until the first
transaction is completed.
This mechanism prevents conflicts and inconsistent results, ensuring that
only one user successfully books the seat.
Case 1
Identified ACID Property: Atomicity
Explanation:
The Atomicity property ensures that a transaction is treated as a single
indivisible unit of work. This means that either all operations of the
transaction are completed successfully or none of them are executed.
In the given banking transaction, the process involves two operations:
1. Deduct ₹10,000 from Account A
2. Credit ₹10,000 to Account B
If the system crashes after deducting the amount from Account A but
before crediting it to Account B, the Atomicity property ensures that the
Ans.   entire transaction is rolled back. As a result, the deducted amount is
restored to Account A, preventing partial execution of the transaction.
Thus, Atomicity guarantees that no incomplete transaction is stored in
the database.
Case 2
Identified ACID Property: Isolation
Explanation:
The Isolation property ensures that multiple transactions executing at the
same time do not interfere with each other. Each transaction operates as
if it is the only transaction running in the system.
a.   Compare and contrast NoSQL databases with traditional relational
Q7
databases. Analyze the key differences in data modeling, scalability,
CO-4;   [10]
and consistency models. Justify scenarios where NoSQL would be
BL-2
preferred over RDBMS with appropriate examples.
1. Introduction (1 Mark)
NoSQL databases are non-relational, schema-less systems designed for
scalability and flexibility, whereas RDBMS use structured schemas and tables.
2. Data Modeling (3 Marks)
Ans.   • RDBMS:
o   Structured, table-based (rows & columns)
o Fixed schema, normalization
• NoSQL:
o   Flexible, schema-less (JSON-like documents, key-value, etc.)
********** 14 **********
--- page 15 ---
o Denormalized for faster access
3. Scalability (2 Marks)
• RDBMS: Vertical scaling (increase server capacity)
• NoSQL: Horizontal scaling (add more nodes, distributed systems)
4. Consistency Models (2 Marks)
• RDBMS: Strong consistency (ACID properties)
• NoSQL: Eventual consistency (BASE model), faster but may have
temporary inconsistency
5. Use-case Justification (2 Marks)
• NoSQL Preferred When:
o   Big data applications (e.g., social media, IoT)
o Unstructured or rapidly changing data
o High scalability required
o Example: Real-time analytics, content management systems
• RDBMS Preferred When:
o Structured data with strict relationships
o Need for strong consistency (e.g., banking systems)
b.   Consider the set of relations and answer the following SQL queries:
Doctor(doc_id, name, dept, salary)
Patient(patient_id, name, dob)
Appointment(app_id, patient_id, doc_id, app_date, diagnosis, fees)
CO-2;
i.   Display patient name and doctor name using JOIN   [10]
BL-3
ii.   Find doctors whose salary is greater than average salary
iii.   Display doctors having total fees > 10000
iv.   Find appointments greater than average fees of that doctor
v.   Increase fees by 10% for all appointments
Give 2 marks for each correct SQL query. Multiple correct answers are possible;
evaluate based on logical correctness and proper SQL syntax.
(i)   SELECT p.name, d.name
FROM Patient p
JOIN Appointment a ON p.patient_id = a.patient_id
JOIN Doctor d ON a.doc_id = d.doc_id;
(ii) SELECT * FROM Doctor
WHERE salary > (SELECT AVG(salary) FROM Doctor);
Ans.   (iii) SELECT doc_id, SUM(fees)
FROM Appointment
GROUP BY doc_id
HAVING SUM(fees) > 10000;
(iv) SELECT *
FROM Appointment a
WHERE fees > (
SELECT AVG(fees)
FROM Appointment
WHERE doc_id = a.doc_id
);
********** 15 **********
--- page 16 ---
(v) UPDATE Appointment SET fees = fees * 1.10;

FRR ICR 7 6 AC OH
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper cced86c0ba5d

- Departments: Commerce
- Programmes: Bachelor of Commerce - 45611
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Re-Exam/Bachelor of Commerce - 45611/Database Management Systems/ANS_Re-Exam_Database Management Systems(NADBM105)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 30; duration hours: 1; exam date: 29 Jan 2026
- Text: text (4 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Commerce
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jan 2026   Time: 11:00 am - 12:00 pm (01:00 Hrs.)
Max Marks: 30
RE EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 4 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
5. All questions are compulsory.
1.   Answer the following question.(Attempt Any 2 Questions)   15
A. (CREATE TABLE 4.5 MKS, ALTER TABLE 1.5 MKS EACH)   7.5
(i)
CREATE TABLE PRODUCT (
P_ID SMALLINT AUTO_INCREMENT,
PNAME VARCHAR(20),
CATEGORY VARCHAR(15),
MFG_DATE DATE,
STOCK_QTY SMALLINT,
PRICE DECIMAL(8,2),
PRIMARY KEY (P_ID));
(ii) Change the data type of stock_qty column to integer size 3
ALTER TABLE PRODUCT
MODIFY COLUMN STOCK_QTY SMALLINT(3);
Or
ALTER TABLE PRODUCT
MODIFY STOCK_QTY SMALLINT(3);
(iii) Add a new column SUPPLIER varchar(18).
ALTER TABLE PRODUCT
Page 1 of 4
--- page 2 ---
ADD COLUMN SUPPLIER VARCHAR(18);
B. Q(i)3mks Q (ii,iii,iv) 1.5 MKS EACH   7.5
(i) Insert 3 records in ORDERS table
INSERT INTO ORDERS (OID, Customer, Item, quantity, Odate, amt) VALUES
(1, 'Riya', 'book', 3, '2025-09-01', 300),
(2, 'Vijay', 'Pen', 5, '2025-09-02', 400),
(3, 'Amrita', 'Stapler', 2, '2025-09-03', 350);
(ii) Change the Total amount to 500 in the first record
UPDATE ORDERS
SET amt = 500.00
iii) Alter table order
change customer cust_name char(20);
iv) Delete from order
where OID=3;
C.   7.5
i)
SELECT CID, BRANCH, SALARY FROM IBM;
ii)
SELECT CNAME, (SALARY + 1000) AS New_Salary FROM IBM;
iii)
SELECT * FROM IBM WHERE SALARY < 25000;
iv)
SELECT * FROM IBM WHERE MONTH(JDATE) = 3;
v)
SELECT CID, CNAME FROM IBM WHERE LENGTH(CNAME) > 6;
2.   Answer the following question.(Attempt Any 2 Questions)   15
Page 2 of 4
--- page 3 ---
A.   7.5
(1.5 marks each)
i. DAY()
Extracts the day of the month (1–31) from a date or datetime.
DAY(date)
Example:
SELECT DAY('2025-09-22') AS DayPart;
ii. LENGTH()
Returns the length in bytes of a string. For multi-byte characters, this may differ from
character count.
LENGTH(string)
Example:
SELECT LENGTH('MySQL') AS LengthBytes;
iii.LEFT()
Returns the leftmost N characters of a string.
LEFT(string, number_of_characters)
Example:
SELECT LEFT('MySQLDatabase', 5) AS LeftPart;
iv. SUM()
Returns the sum of numeric values in a column (ignores NULLs).
SELECT SUM(column_name) FROM table_name;
Example:
SELECT SUM(salary) AS TotalSalary FROM employees;
v. MOD()
Returns the remainder of division of one number by another (modulus).
MOD(dividend, divisor)
Example:
SELECT MOD(29, 5) AS Remainder;
B. (2.5 marks each)   7.5
i) SELECT *
FROM FLIGHTS
WHERE TDATE BETWEEN '2015-01-01' AND '2025-01-01';
ii) SELECT FNO, AIRLINE, TDATE, SEATS, FARE, (SEATS * FARE) AS Revenue
FROM FLIGHTS ;
iii) SELECT CONCAT('The fare of ', FNO, ' by ', AIRLINE, ' was ', FARE, ' on ', TDATE)
FROM FLIGHTS;
Page 3 of 4
--- page 4 ---
C. ( 2.5 marks each)   7.5
i. SELECT TNAME, TREES.TID, PDATE
FROM TREES, PLANTING
WHERE TREES.TID = PLANTING.TID;
ii. SELECT TNAME, SPECIES, PID, PDATE
FROM TREES, PLANTING
WHERE TREES.TID = PLANTING.TID
AND HT > 500;
iii. SELECT TNAME, PID, SPECIES, HT
FROM TREES, PLANTING
WHERE TREES.TID = PLANTING.TID AND TNAME LIKE "A%";
Page 4 of 4
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 4007ee405c04

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Database Management Systems/ANS_Database Management Systems(703AI0C003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data whenever required (Please mentions such data in answer)
Section A: Attempt All Questions (Each Question Carries 5M)
Question 1
CO 1;   A.   What are the main types of database users, and what are their roles in a   5M
SO6;   DBMS?
BL2   DBA (1M): Manages database, security, backup, and performance.
Database Designer (1M): Designs schema, relationships, constraints.
Application Programmer (1M): Writes programs that interact with the DB.
End User (1M): Uses applications to access data.
Example (1M): In a bank – DBA (admin), Designer (schema), Programmer
(banking app), User (customer)
Mark Split:
• Map Strong Entities – 1M
• Map Weak Entities – 1M
• Map Relationships – 1M
• Map Attributes & Keys – 1M
• Example Schema – 1M
CO 1;   B.   Explain the steps involved in converting an ER diagram to a relational   5M
SO6;   schema.
BL2   Strong Entity → Table with PK
Weak Entity → Table with FK + PK
1:1 / 1:N / M:N → Foreign keys / Separate relation
********** 1 **********
--- page 2 ---
Multivalued attributes → New relation
Example: STUDENT → STUDENT(StudentID, Name); COURSE →
COURSE(CID, CName); ENROLL(StudentID, CID).
Mark Split:
• Map Strong Entities – 1M
• Map Weak Entities – 1M
• Map Relationships – 2M
• Map Attributes & Keys – 1M
CO 2;   C.   Analyse the difference between Division and Cartesian Product in   5M
SO1;   relational algebra with examples.
BL4   •   Division (÷): Returns tuples in one relation associated with all tuples in
another.
Example: Students ÷ Courses → Students who took all courses.
• Cartesian Product (×): Combines every tuple of one relation with all of
another.
Example: STUDENT × COURSE → All possible pairs.
•   Difference: Division = subset filtering; Cartesian = all combinations.
Mark Split:
• Division Definition & Example – 2M
• Cartesian Product Definition & Example – 2M
• Differences Table / Key Points – 1M
CO 4;   D.   Demonstrate with example commands how to create a database and   5M
SO7;   collection in MongoDB using the shell.
BL4
> use collegeDB   # Create/Use DB
> db.createCollection("students") # Create Collection
> db.students.insert({name:"Ravi", age:20})
> show collections
Mark Split:
• Create Database Command – 1.5M
• Create Collection Command – 1.5M
• Insert Documents Example – 1M
• Explanation of Shell Steps – 1M
********** 2 **********
--- page 3 ---
Section B: Attempt Any Four Questions from Questions 2 to 7 (Each Question Carries 20M)
Question 2
CO 3;   A.   What is Decomposition? Define various properties of decomposition with   10M
SO1;   examples of each.
BL4   •   Definition: Splitting relation into smaller ones to remove redundancy.
•   Properties:
o Lossless Join (2M): No data loss on recombination.
o Dependency Preserving (2M): All FDs retained.
o Example: R(A,B,C) → R1(A,B), R2(B,C) (lossless if common
attribute is key).
Mark Split:
• Definition of Decomposition – 2M
• Lossless Decomposition – 2M
• Dependency Preserving – 2M
• Examples illustrating properties – 4M
CO 1;   B. A library has multiple books, authors, and members. Books have Book ID,   10M
SO6;   title, genre, and publication year. Authors have Author ID, name, and
BL5   nationality. Members have Member ID, name, and contact details. Each
member can borrow multiple books, and each book can be authored by
multiple authors. Borrowing transactions include Transaction ID, borrow
date, return date, and fine, if any.
Entities: Book(BookID, Title, Genre, Year), Author(AuthorID, Name,
Nationality), Member(MemberID, Name, Contact), Borrow(TransactionID,
BorrowDate, ReturnDate, Fine).
Relationships:
• Book–Author: M:N
• Member–Borrow–Book: M:N via Borrow
Cardinality: Member(1,N)–Borrow–Book(1,N).
Diagram: 3 Entities + Relationships + Keys.
Mark Split:
• Key Entities & Attributes – 3M
• Relationships with Cardinality & Participation – 3M
• ER Diagram – 4M
Question 3
********** 3 **********
--- page 4 ---
CO 2;   A.   What is a subquery in SQL? Explain single-line and multi-line subqueries?   10M
SO1;   Also, explain Correlated subqueries with suitable examples. Also discuss
BL4   cases where subqueries are preferred over joins.
Definition: Query inside another query.
Single-line: Uses =, <, >
→ SELECT name FROM emp WHERE deptid=(SELECT deptid FROM dept
WHERE dname='HR');
Multi-line: Uses IN, ANY, ALL
Correlated: Inner query depends on outer query.
Preferred when: Aggregation/Existence check needed.
Mark Split:
• Definition of Subquery – 2M
• Single-line Subquery Example – 2M
• Multi-line Subquery Example – 2M
• Correlated Subquery Example – 2M
• When Subqueries Preferred over Joins – 2M
CO 4;   B.   Explain conflict serializability and its precedence graph (serializability   10M
SO6;   graph)? For the schedule given below, draw the precedence graph and
BL3   check if the schedule is conflict serialisable or not:
Schedule: R1(A), R2(B), W1(B), R3(B), W2(A), W3(B)
Definition (short):
A schedule is conflict serialisable if it is conflict-equivalent to some serial
schedule — i.e., by swapping non-conflicting operations, you can transform
it into a serial order.
To test this, we build the precedence (serializability) graph: nodes =
transactions; add a directed edge Ti → Tj whenever some operation of Ti on
a data item appears before a conflicting operation of Tj on the same item
(conflict = same item and at least one is a write).
If the graph has no cycle, the schedule is conflict-serialisable; if it has a
cycle, it is not.
Precedence graph (edges)
• T1 → T2 (from A)
• T2 → T1 (from B)
• T2 → T3 (from B)
• T1 → T3 (from B)
********** 4 **********
--- page 5 ---
Because the precedence graph contains a cycle (T1 ↔ T2), the schedule is
NOT conflict-serialisable.
No serial order of the transactions can preserve all conflicting operation
orders implied by this schedule.
Mark Split:
• Definition – 2M
• Precedence Graph Explanation – 2M
• Draw Precedence Graph for Schedule – 3M
• Check Conflict Serializability & Conclusion – 3M
Question 4
CO 3;   A.   What is functional dependency? Explain partial, full, and transitive   10M
SO1;   dependency with examples.
BL2   Normalise the following relation into 3NF:
R(A, B, C, D, E, F, G) having FDs AB → CD, E → FG, D → E
Functional Dependency (1M)
A functional dependency (FD) X → Y on relation R means: for any two
tuples of R, if they agree on attributes X they must agree on attributes Y. X
functionally determines Y.
(2) Types of dependencies (3M)
•   Partial dependency (1M)
o Definition: A non-prime attribute depends on part of a
composite primary key.
o Example: In relation R(A,B,C) with key (A,B), if A → C
holds then C is partially dependent on the key because only
part A (not whole (A,B)) determines C.
•   Full dependency (1M)
o Definition: A non-prime attribute depends on the entire
candidate key, not on any proper subset.
o Example: In R(A,B,C) with key (A,B), if (A,B) → C and
neither A → C nor B → C holds, then C is fully dependent on
(A,B).
• Transitive dependency (1M)
o Definition: A → B and B → C (B is non-key) implies A → C
transitively; non-prime attribute depends on another non-
prime attribute.
********** 5 **********
--- page 6 ---
o Example: If A is key and A → D, and D → E, then A → E is
a transitive dependency (should be removed in 3NF/BCNF).
Final decomposition (3NF):
• R1(A, B, C, D) — FD preserved: AB → C,D (key AB). Key: (A,B).
• R2(D, E) — FD preserved: D → E. Key: D.
• R3(E, F, G) — FD preserved: E → F,G. Key: E.
Mark Split:
• Definition of Functional Dependency – 1M
• Partial, Full, Transitive Dependencies – 3M
• Candidate Key Identification – 1M
• Stepwise 3NF Decomposition – 3M
• Final 3NF Relations – 2M
CO 2;   B.   Customer(CustID, CustName, City)   10M
SO1;   Order(OID, CustID, OrderDate)
BL6
Product(PID, ProductName, Price)
OrderDetails(OID, PID, Quantity)
Consider the above data and write Relational algebra queries for the given
questions.
1. List the names of customers who ordered ‘Laptop’.
πCustName(σProductName='Laptop'(Customer ⨝ Order ⨝
OrderDetails ⨝ Product))
2. Retrieve orders placed from ‘Pune' city.
πOID(σCity='Pune'(Customer ⨝ Order))
3. Find the total quantity ordered for ProductID 'P105'.
SUM_Quantity(σPID='P105'(OrderDetails))
Mark Split:
• Customers who ordered 'Laptop' – 3M
• Orders placed from 'Pune' – 3M
• Total quantity for ProductID 'P105' – 3M
• Presentation / Formatting – 1M
Question 5
********** 6 **********
--- page 7 ---
CO 4;   A.   Compare Relational Databases and NoSQL Databases. Explain when   10M
SO7;   NoSQL should be preferred.
BL2
Relational Database
Feature   NoSQL Database
(RDBMS)
Unstructured, semi-structured, or
Structured (tables with
Data Model   structured (JSON, key-value, graph,
rows & columns)
etc.)
Fixed schema (must
Schema   define before inserting   Schema-less or dynamic schema
data)
Vertically scalable (add   Horizontally scalable (add more
Scalability
more power to one server) servers)
Strong consistency using Eventual consistency (CAP
Consistency
ACID properties   theorem)
Query   SQL (Structured Query   No standard query language
Language   Language)   (depends on database type)
MySQL, Oracle,
Examples   MongoDB, Cassandra, Neo4j, Redis
PostgreSQL
When NoSQL Should Be Preferred
• When data is unstructured or rapidly changing (e.g., social media,
IoT).
• When an application needs high scalability and performance across
distributed systems.
• When flexible schema and fast development are required.
• When large volumes of data (Big Data) need to be handled efficiently.
Mark Split:
• Data Structure Differences – 2.5M
• Scalability Differences – 2M
• Consistency Differences – 2M
• When to Prefer NoSQL – 3.5M
CO 2;   B.   Consider the data in Q.4 (B) and write SQL JOIN queries for the given   10M
SO1;   questions.
BL6   1. List all customers from ‘Pune’ along with the products they have
ordered.
SELECT c.CustName, p.ProductName
FROM Customer c
JOIN Order o ON c.CustID=o.CustID
JOIN OrderDetails od ON o.OID=od.OID
********** 7 **********
--- page 8 ---
JOIN Product p ON od.PID=p.PID
WHERE c.City='Pune';
2. Show the total quantity of each product ordered by every customer.
SELECT c.CustName, p.ProductName, SUM(od.Quantity)
FROM ...
GROUP BY c.CustName, p.ProductName;
3. Display customers who have not placed any orders.
SELECT c.CustName
FROM Customer c
LEFT JOIN [Order] o ON c.CustID = o.CustID
WHERE o.OID IS NULL;
4. List each product and the total number of customers who have purchased
it.
SELECT p.ProductName, COUNT(DISTINCT o.CustID) AS
NoOfCustomers
FROM Product p
JOIN OrderDetails od ON p.PID = od.PID
JOIN [Order] o ON od.OID = o.OID
GROUP BY p.ProductName;
Mark Split:
• Customers from Pune with Products – 2.5M
• Total Quantity of Each Product per Customer – 2.5M
• Customers with No Orders – 2.5M
• Products with Total Number of Customers – 2.5M
Question 6
CO 4;   A.   Explain transaction states with a neat diagram. Give examples of each   10M
SO6;   state.
BL4
Active → Partially Committed → Committed → Failed → Aborted.
Diagram: State flow with arrows.
Example: Banking transfer – amount deducted (active), recorded
(committed).
********** 8 **********
--- page 9 ---
Mark Split:
• Active State Explanation & Example – 2M
• Partially Committed State Explanation & Example – 2M
• Failed State Explanation & Example – 2M
• Committed State Explanation & Example – 2M
• Terminated State Explanation & Example – 2M
• Transaction States Diagram
CO 2;   B.   Consider the data in Q.4 (B) and write SQL sub-queries for the given   10M
SO1;   questions.
BL6   1. List the names of customers who have ordered the most expensive
product.
SELECT CustName
FROM Customer
WHERE CustID IN (
SELECT o.CustID
FROM [Order] o
JOIN OrderDetails od ON o.OID = od.OID
JOIN Product p ON od.PID = p.PID
WHERE p.Price = (SELECT MAX(Price) FROM Product)
);
2. Display products whose prices are higher than the average product price.
SELECT ProductName, Price
FROM Product
WHERE Price > (SELECT AVG(Price) FROM Product);
3. Show orders that include products with a quantity greater than the
average quantity ordered across all items.
SELECT DISTINCT OID
FROM OrderDetails
WHERE Quantity > (SELECT AVG(Quantity) FROM
OrderDetails);
4. Display the name and city of customers who have placed more than one
order.
SELECT CustName, City
FROM Customer
WHERE CustID IN (
SELECT CustID
********** 9 **********
--- page 10 ---
FROM [Order]
GROUP BY CustID
HAVING COUNT(OID) > 1
);
Mark Split:
• Customers who ordered most expensive product – 2.5M
• Products priced higher than average – 2.5M
• Orders with quantity > average – 2.5M
• Customers with >1 order – 2.5M
Question 7
CO 1;   A.   Discuss at least five advantages that database systems have over traditional   5M
SO6;   file systems.
BL2   Data redundancy control
Data consistency
Security & concurrency
Data independence
Backup & recovery
Mark Split:
• 5 Points, 1M each – 5M
CO 2;   B.   Explain the role of foreign key constraints in maintaining data integrity.   5M
SO2;   Definition: Field in one table referencing PK in another.
BL4
Ensures referential integrity.
Example: Order(CustID) references Customer(CustID).
Mark Split:
• Definition – 1M
• Example – 2M
• Maintaining Data Integrity – 2M
CO 3;   C.   Discuss Armstrong’s axioms and their use in determining dependencies.   5M
SO1;   Reflexivity: If Y⊆X → X→Y
BL4
Augmentation: X→Y ⇒ XZ→YZ
Transitivity: X→Y, Y→Z ⇒ X→Z
Use: Derive all FDs.
********** 10 **********
--- page 11 ---
Mark Split:
• Definition – 1M
• List of 4 Axioms – 4M
CO 1;   D.   Describe constraints in ER model and their importance.   5M
SO6;   Types:
BL2
• Key constraint: Unique identification.
•   Participation: Total/Partial.
• Cardinality: 1:1, 1:N, M:N.
Importance: Ensures data integrity and consistency.
Mark Split:
• Definition of Constraints – 1M
• Types (Key, Participation, Cardinality) – 2M
• Importance / Examples – 2M
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 4796e8cd7d99

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CyberSecurity_7010/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (14 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech (DS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Diagrams must be neat and legible.
5. Ensure the correct question number is written in the answer sheet.
6. Qt1 is compulsary, attemp any 4 questions from remaining 6 questions.
Q1
Answer the following questions   [20]
a   Discuss the different types of users and describe how these users communicate with the
database
"In a DBMS, users are individuals or applications that interact with the database to perform
operations like querying, updating, or managing data. Depending on their role and
interaction level, they are classified into different types.
1. Types of Database Users
Naïve Users (End Users):
Use pre-defined application interfaces such as ATM software, online forms, or mobile apps.
CO- 1;   No direct interaction with the DBMS; use menu-driven or form-based interfaces.   [5]
SO- 2;
BL- 1   Application Programmers:
Write application programs that communicate with the database using languages like Java,
Python, or C++ through embedded SQL or APIs (e.g., JDBC, ODBC).
Database Designers:
Define the logical and physical structure of the database (schemas, constraints,
relationships).
Database Administrators (DBA):
Manage database access, user permissions, security, and backup.
Responsible for tuning performance and ensuring data integrity.
Sophisticated Users (Analysts / Data Scientists):
********** 1 **********
--- page 2 ---
Write SQL queries directly or use analytical tools to extract insights."
b   Problems with Bad Database Design [5 Marks]
A bad database design fails to properly organize data, leading to redundancy,
inconsistency, and performance issues.
Such designs often arise due to missing normalization or poor understanding of data
relationships.
1. Data Redundancy
•   The same data is stored in multiple places, wasting storage and making updates
difficult.
Example:
If a customer’s address is stored in several tables, updating it in one place but not
others causes mismatched data.
2. Data Inconsistency
• Due to redundancy, the same data may have different values in different tables.
Example:
In one record, a customer’s city is “Mumbai” and in another “Bombay” —
leading to confusion and inaccurate reports.
3. Insertion Anomalies
CO- 2;
SO - 2;   • You cannot insert new data without the presence of other unnecessary data.   [5]
BL- 2   Example:
Cannot add a new course in a table that stores StudentID, StudentName,
CourseName unless a student is enrolled in it.
4. Deletion Anomalies
•   Deleting one record may unintentionally remove valuable information.
Example:
Deleting the last student enrolled in “DBMS” may also delete the course
“DBMS” details.
5. Update Anomalies
•   Updating a value in one place requires multiple updates elsewhere.
Example:
Changing a department name requires updates in all employee records; missing
one leads to inconsistent data.
6. Poor Query Performance
•   Improper indexing and redundant fields slow down data retrieval and increase
maintenance costs.
c   (a) Possible Superkeys:
{EmpID}, {AadharNo}, {Email}, {EmpID, Name}, {AadharNo, Name}, etc.
CO- 3 ;   (b) Candidate Keys:
SO - 2;   [5]
{EmpID}, {AadharNo}, {Email}
BL- 2
(c) Primary Key:
EmpID — Unique
d   What are the advantages of NoSQL over traditional RDBMS and vice-versa?
CO- 4 ;   NoSQL is better than RDBMS because of the following reasons/properities of NoSQL:
SO - 2;   It   supports   semi-structured   data   and   volatile   data   [5]
BL-1   It   does   not   have   schema
Read/Write   throughput   is   very   high
Horizontal   scalability   can   be   achieved   easily
********** 2 **********
--- page 3 ---
Will   support   Bigdata   in   volumes   of   Terra   Bytes &   Peta   Bytes
Provides   good   support   for   Analytic   tools   on   top   of   Bigdata
Can   be   hosted   in   cheaper   hardware   machines
In-memory caching option is available to increase the performance of queries
Faster   development   life   cycles   for   developers
Still, RDBMS is better than NoSQL for the following reasons/properties of RDBMS:
Transactions with ACID properties - Atomicity, Consistency, Isolation & Durability
Adherence   to   Strong   Schema   of   data   being   written/read
Real time query management   ( in case of data size < 10 Tera bytes   )
Execution of complex queries involving join & group by clauses
Q2   [20]
a
CO- 1 ;
SO - 2;   [10]
BL-2
b   Consider following movie database:
movies (movie_id, title, release_year, runtime_min, language, country)
directors (director_id, first_name, birth_year)
actors (actor_id, first_name, birth_year)
movie_direction (movie_id, director_id, billing_order)
CO- 2 ;
SO - 2;   movie_cast (movie_id, actor_id, role_name, billing_order)   [10]
BL- 2
genres (genre_id, genre_name)
movie_genres (movie_id, genre_id)
Write the SQL queries the following question:
i   List the English-language movies released after 2020 with runtime > 140 minutes.
Ans:
SELECT title, release_year, runtime_min
FROM movies WHERE language = 'English' AND release_year > 2020
********** 3 **********
--- page 4 ---
AND runtime_min > 140;
ii   For each director, show the number of movies they directed and the average runtime of
those movies. Include only directors with at least 2 movies.
Ans:
SELECT d.first_name, COUNT (m. movie_id) AS total_movies, ROUND (AVG (m.
runtime_min), 2) AS avg_runtime
FROM directors d, movies m, movie_direction md
Where d. director_id = md. director_id and m. movie_id = md. movie_id
GROUP BY d. director_id, d. first_name
HAVING COUNT (m. movie_id) >= 2;
iii   List movies whose title length ≥ 12 and whose uppercased title starts with 'THE'.
Ans:
SELECT   title, LENGTH (title) AS title_len
FROM movies
WHERE LENGTH(title) >= 12
AND UPPER (title) LIKE 'THE%
iv   Find actors who have acted in more than one movie.
Ans:
SELECT a. actor_id, a. first_name, COUNT (*) AS movie_count
FROM actors a, movie_cast mc
Where mc. actor_id = a.actor_id
GROUP BY a. actor_id, a. first_name
HAVING COUNT (*) > 1;
v   Find movies that belong to multiple genres (two or more).
Ans:
SELECT m. movie_id, m. title, COUNT (mg. genre_id) AS genre_count
FROM movies m, movie_genres mg
GROUP BY m.movie_id, m.title
Having COUNT (m. movie_id) >= 2
Q3   [20]
a.   Here’s the final relational schema (no SQL) derived from your ERD.
CO- 1 ;   PKs are underlined; FKs noted after each table.
SO - 2;   [10]
BL- 2   •   PLAYER(PlayerID, PName, Technique, TeamID)
FK: TeamID → TEAM.TeamID
• TEAM(TeamID, TeamName)
********** 4 **********
--- page 5 ---
• GLOSSARY(Gid, Text, TeamID)
FK: TeamID → TEAM.TeamID
Constraint: 1:1 with TEAM (each team has at most one glossary)
• GAME(GameID, Name, Date)
•   REFEREE(RefID, RName)
• PLAYER_GLOSSARY(PlayerID, Gid)
FKs: PlayerID → PLAYER.PlayerID, Gid → GLOSSARY.Gid
(resolves Player uses Glossary M:N)
• PARTICIPATES(GameID, TeamID, Winner)
FKs: GameID → GAME.GameID, TeamID → TEAM.TeamID
(resolves Team participates in Game; each game has exactly 2 teams; exactly one
row per game with Winner = TRUE)
• GAME_REFEREE(GameID, RefID)
FKs: GameID → GAME.GameID, RefID → REFEREE.RefID
(resolves Game guided by Referee; each game has exactly 3 referees)
b.   Closure of (FacultyID, CourseID):
adds FacultyName, DeptID, DeptName, CourseName, Semester, RoomNo ⇒ all
attributes.
No proper subset (FacultyID alone or CourseID alone) determines all attributes.
Candidate key = {FacultyID, CourseID}. (Only one.)
Is the relation in 3NF? [2M]
3NF requires: for every FD (X\to A), either (X) is a superkey or (A) is prime.
Prime attributes = those in any key = {FacultyID, CourseID}.
Check violations:
•FacultyID → FacultyName, DeptID (X not superkey, RHS non-prime) ⇒ violates 3NF
•DeptID → DeptName (X not superkey, RHS non-prime) ⇒ violates
•CourseID → CourseName (X not superkey, RHS non-prime) ⇒ violates
CO- 3 ;
•RoomNo → DeptID (X not superkey, RHS non-prime) ⇒ violates
SO - 2;   [10]
BL- 3   Hence, relation is not in 3NF.
iii) Decompose to BCNF (step-by-step) [4M]
BCNF requires every non-trivial FD to have a superkey on the LHS.
Start: R(FacultyID, FacultyName, DeptID, DeptName, CourseID, CourseName, Semester,
RoomNo)
1.   Use FacultyID → FacultyName, DeptID (violates BCNF):
•   R1(FacultyID, FacultyName, DeptID) — key: FacultyID (BCNF)
•   R2(FacultyID, DeptID, DeptName, CourseID, CourseName, Semester,
RoomNo)
2.   In R2, DeptID → DeptName violates BCNF:
•   R21(DeptID, DeptName) — key: DeptID (BCNF)
•   R22(FacultyID, DeptID, CourseID, CourseName, Semester, RoomNo)
3.   In R22, CourseID → CourseName violates BCNF:
********** 5 **********
--- page 6 ---
•   R221(CourseID, CourseName) — key: CourseID (BCNF)
•   R222(FacultyID, DeptID, CourseID, Semester, RoomNo)
4.   In R222, RoomNo → DeptID violates BCNF:
•   R2221(RoomNo, DeptID) — key: RoomNo (BCNF)
•   R2222(FacultyID, CourseID, Semester, RoomNo)
Check R2222: (FacultyID, CourseID to Semester, RoomNo) has a superkey LHS
(FacultyID, CourseID is the key of R2222), so BCNF holds.
All resulting relations are now in BCNF.
________________________________________
iv) Final BCNF relations with primary keys [2M]
•   R1(FacultyID, FacultyName, DeptID)
•   R21(DeptID, DeptName)
•   R221(CourseID, CourseName)
•   R2221(RoomNo, DeptID)
•   R2222(FacultyID, CourseID, Semester, RoomNo)
These preserve the original FDs (each determinant appears as a key in some relation) and
the decomposition is lossless via common keys (e.g., DeptID, CourseID, RoomNo,
FacultyID).
Q4   [20]
a.   •   A primary goal of a database system is to retrieve information from and store   [10]
new information into the database. People who work with a database can be categorized
as database users or database administrators
•   Database User:
o   Naive users : are unsophisticated users who interact with the system by invoking
one of the application programs that have been written previously. For example, a clerk in
the university
o   Application programmers are computer professionals who write application
programs. Application programmers can choose from many tools to develop user
interfaces.
CO- 1 ;   o   Sophisticated users interact with the system without writing programs. Instead,
SO - 2;
they form their requests either using a database query language or by using tools such as
BL-2
data analysis software. Analysts who submit queries to explore data in the database fall in
this category.
o   Specialized users are sophisticated users who write specialized database
applications that do not fit into the traditional data-processing framework. Among these
applications are computer-aided design systems, knowledgebase and expert systems,
systems that store data with complex data types (for example, graphics data and audio
data), and environment- modelling systems.
•   The functions of a DBA include:
o   Schema definition. The DBA creates the original database schema by executing a
set of data definition statements in the DDL.
********** 6 **********
--- page 7 ---
o   Storage structure and access-method definition.
o   Schema and physical-organization modification. The DBA carries out changes to
the schema and physical organization to reflect the changing needs of the organization, or
to alter the physical organization to improve performance.
o   Granting of authorization for data access. By granting different types of
authorization, the database administrator can regulate which parts of the database various
users can access.
o   Routine maintenance. Examples of the database administrator’s routine
maintenance activities are:
•   Periodically backing up the database, either onto tapes or onto remote servers, to
prevent loss of data in case of disasters such as flooding.
•   Ensuring that enough free disk space is available for normal operations, and
upgrading disk space as required.
•   Monitoring jobs running on the database and ensuring that performance is not
degraded by very expensive tasks submitted by some users.
b.   Solve the following queries using relational algebra   [10]
Book(book_id, book_title, pub_year, num_pages, language, pub_date, pub_country)
Author(author_id, author_fname, author_lname)
Book_Author(author_id, book_id)
Review(book_id, review_id, review_stars, num_of_reviews)
CO- 2 ;   1.   List book titles along with their authors' names.
SO - 2;
BL-2
2. Get the first and last names of all authors who have written at least one book.
3. Find the book IDs that do not have any associated reviews.
4. determine those years in which there was at least one book that received a rating
of at least four stars.
5. Find books that have received a 5-star review.
Q5   [20]
CO- 2 ;   a.   Consider following e-commerce database:
SO - 2;   [10]
BL-2
********** 7 **********
--- page 8 ---
customers (customer_id, full_name, email, phone, city)
products (product_id   , name, unit_price stock_qty)
orders (order_id, customer_id, order_date, shipping_city, order_total)
order_items (order_id, product_id, qty, unit_price)
Write the SQL queries the following question:
i   Show each product’s total units sold and total revenue from order_items
Ans:
SELECT p. product_id, p.name, SUM (oi.qty), SUM (oi.qty * oi.unit_price) as Total
FROM products p   [3]
JOIN order_items oi ON oi. product_id = p.product_id
GROUP BY p. product_id, p.name
ORDER BY Total DESC;
ii   Show each product’s total units sold and total revenue from order_items. Return only
products with at least 2 units sold
Ans:
SELECT p. product_id, p.name, SUM (oi.qty), SUM (oi.qty * oi. unit_price)
[3]
FROM products p
JOIN order_items oi ON oi. product_id = p. product_id
GROUP BY p. product_id, p.name
HAVING SUM (oi.qty) >= 2
iii   Create the four tables with appropriate PRIMARY KEY constraints and sensible data types
Ans:
CREATE TABLE customers (
customer_id number PRIMARY KEY,
full_name VARCHAR (120) NOT NULL,
email   VARCHAR (180) UNIQUE NOT NULL,
phone   VARCHAR (20),
city   VARCHAR (80)   [4]
);
CREATE TABLE products (
product_id number PRIMARY KEY,
name   VARCHAR (25) NOT NULL,
unit_price NUMERIC (10,2) NOT NULL),
stock_qty INT NOT NULL
********** 8 **********
--- page 9 ---
);
CREATE TABLE orders (
order_id   SERIAL PRIMARY KEY,
customer_id INT NOT NULL,
order_date   date,
shipping_city VARCHAR (80),
order_total number (12,2) NOT NULL
);
CREATE TABLE order_items (
order_id INT NOT NULL,
product_id INT NOT NULL,
qty   INT NOT,
unit_price NUMERIC (10,2) NOT NULL,
PRIMARY KEY (order_id, product_id)
);
b.   Here’s a compact, exam-ready solution.
i) Dependencies on X (showing step references)
Read–Write (RW) (read first, later write on X):
• T1→T2 : (1) R by T1 before (3) W by T2
• T1→T3 : (1) R by T1 before (6) W by T3
• T2→T1 : (2) R by T2 before (5) W by T1
• T2→T3 : (2) R by T2 before (6) W by T3
• T3→T1 : (4) R by T3 before (5) W by T1
Write–Read (WR) (write first, later read on X):
• T2→T3 : (3) W by T2 before (4) R by T3
Write–Write (WW) (write first, later write on X):
• T2→T1 : (3) W by T2 before (5) W by T1
• T1→T3 : (5) W by T1 before (6) W by T3
• T2→T3 : (3) W by T2 before (6) W by T3
ii) Conflict serializability (2M)
Precedence edges from conflicts:
CO- 4 ;
SO - 2;   • T1→T2 (RW), T2→T1 (RW/WW) ⇒ cycle T1 ↔ T2   [10]
BL- 2   • T1→T3 (RW/WW) and T3→T1 (RW) ⇒ cycle T1 ↔ T3
•   (also T2→T3)
Since the graph has cycles, not conflict-serializable.
iii) View serializability (3M)
Identify read-from and final write in the given schedule:
•   (1) T1 reads X from initial value (no prior write) ⇒ T0 → T1
•   (2) T2 reads X from initial value ⇒ T0 → T2
•   (4) T3 reads X from T2’s write at (3) ⇒ T2 → T3
•   Final write on X is by T3 at (6).
For a serial schedule to be view-equivalent:
•   Both T1 and T2 must read initial X. In any serial order, only the first writing
transaction can read initial; the next reader (which also writes) would see the
prior write, not initial. Because both T1 and T2 write X, you cannot place them
serially so that both read the initial value.
Therefore, no serial schedule preserves these read-from relations and the final
write simultaneously.
Hence, not view-serializable.
********** 9 **********
--- page 10 ---
iv) View-equivalent serial schedule (2M)
None exists. Since (iii) fails, there is no serial order that is view-equivalent to the given
schedule.
Q6   [20]
a.   Here’s a clear, exam-ready 10-mark answer divided into two parts   [10]
Q1. States of a Transaction [5 Marks]
A transaction passes through several states during its execution in a DBMS.
1. States of a Transaction
State   Description
Active   The transaction is executing its read/write operations.
Partially
The transaction has executed its final statement but has not yet been p
Committed
All operations are successfully completed, and the changes are perma
Committed
database.
Failed   A fault or error occurs before the transaction commits. Changes made
All changes made by the transaction are rolled back (undone). The da
Aborted
previous consistent state.
CO- 4 ;
SO - 2;   2. State Transition Diagram
BL-3
Explanation:
•   If all steps succeed → transaction commits.
•   If any error/failure occurs → it aborts, and all partial updates are rolled back.
********** 10 **********
--- page 11 ---
Q2. Serializability [5 Marks]
Definition
A schedule is said to be serializable if its effect on the database is equivalent to some
serial execution of the same transactions, i.e., the final database state is the same as if
transactions were executed one after another without overlap.
Types of Serializability
1.   Conflict Serializability – Based on conflicting read/write operations; checked
using a precedence graph.
2. View Serializability – Based on equivalent read-from and final-write
relationships among transactions.
Importance of Serializability
•   Ensures consistency of the database in concurrent execution.
•   Prevents anomalies such as:
o   Lost update
o   Dirty read
o   Non-repeatable read
o   Inconsistent retrievals
•   Allows maximum concurrency while preserving correctness.
In short:
Serializability ensures that concurrent transactions produce the same result as some serial
order, maintaining database consistency and isolation—the core goal of concurrency
control in DBMS.
b.   "   [10]
1.   Document-Based Databases:
o   Description: Store data in JSON-like documents where each document can have
different fields.
o   Example: MongoDB, CouchDB.
o   Use Case: Storing user profiles, product catalogs.
2.   Key-Value Stores:
CO- 4 ;   o   Description: Data is stored as a collection of key-value pairs. Each key is unique
SO - 2;   and maps to a value.
BL-1
o   Example: Redis, Riak.
o   Use Case: Session management, caching.
3.   Column-Family Stores (Wide-Column Stores):
o   Description: Data is stored in columns rather than rows, optimized for queries on
large datasets.
o   Example: Apache Cassandra, HBase.
o   Use Case: Real-time analytics, large-scale data warehousing.
********** 11 **********
--- page 12 ---
4.   Graph Databases:
o   Description: Data is stored as nodes (entities) and edges (relationships), suitable
for connected data.
o   Example: Neo4j, Amazon Neptune.
o   Use Case: Social networks, recommendation engines, fraud detection
"
Q7
[20]
a   Levels of Data Abstraction
Databases hide storage details through three abstraction levels so users see only what they
need:
1. Physical Level (Internal Schema)
o What it shows: How data are stored: file organization, indexes, record
layouts, compression, page size, pointers.
o   Audience: DBMS engineers, DBAs.
o Example: B+-tree index on Emp(ID), heap file vs clustered file.
2. Logical/Conceptual Level (Conceptual Schema)
o What it shows: The global structure of the database: entities, attributes,
relationships, constraints—independent of storage.
o   Audience: Designers, application developers.
CO-1 ;   o Example: Relations EMP(EmpID, Name, DeptID) and DEPT(DeptID,
SO- 2;   DeptName) with FK DeptID.   [5]
BL-1   3. View Level (External Schemas / Views)
o What it shows: User-specific subsets or perspectives of the logical
schema; may hide sensitive or irrelevant attributes.
o   Audience: End users, applications.
o Example: View EmpPublic(EmpID, Name, DeptName) hiding salaries.
Data Independence (Why it matters)
•   Physical Data Independence: Change storage structures (e.g., add index) without
changing the conceptual schema/app code.
•   Logical Data Independence: Change conceptual schema (e.g., split a table)
without changing user views/programs.
b
What is a View?
A view is a named, stored query that presents data from one or more tables as a virtual
table.
It stores query definition, not the data (except materialized views).
Syntax (basic):
CREATE VIEW dept_emp AS
CO- 2 ;   SELECT e.EmpID, e.Name, d.DeptName
SO - 2;   FROM Employee e JOIN Department d USING (DeptID);   [5]
BL-2   Why use views?
•   Security: expose only needed columns/rows.
•   Simplicity: hide complex joins/filters.
•   Consistency: centralize business logic.
•   Logical independence: shield apps from base-table changes.
WITH CHECK OPTION ensures inserts/updates through the view still satisfy its
predicate.
********** 12 **********
--- page 13 ---
Types of Views (common classifications)
1) By data storage
•   Logical (Standard) View / Non-materialized view
o   Stores only the SELECT definition; data fetched at query time.
•   Materialized View (DB-dependent: Oracle, PostgreSQL, etc.)
o   Physically stores result set for speed; needs refresh.
o   Refresh modes: ON DEMAND (manual/scheduled) or ON COMMIT
(where supported); COMPLETE/FAST refresh options depending on
logs.
2) By query complexity
•   Simple View
o Based on one table, no aggregates, no DISTINCT, no GROUP BY/SET
ops.
o   Often updatable (subject to RDBMS rules).
o Example:
o CREATE VIEW active_customers AS
o SELECT CustID, Name, City
o FROM Customer
o WHERE Status = 'ACTIVE'
o WITH CHECK OPTION;
•   Complex View
o Based on multiple tables, joins, aggregates, DISTINCT, GROUP BY,
UNION, etc.
o   Usually read-only (non-updatable).
3) By updatability
•   Updatable View
o You can INSERT/UPDATE/DELETE through it if each row maps to
exactly one base-table row and no disqualifying clauses.
o   Typical conditions (vendor-agnostic): no DISTINCT, GROUP BY,
HAVING, aggregates, set operations, window functions; select all NOT
NULL key columns; no expressions on key columns.
•   Read-only View
o Any view violating the above (e.g., joins + aggregates). Some systems
allow INSTEAD OF triggers to make them updatable.
4) Other common terms (vendor-specific but useful)
•   Inline View: a subquery in the FROM clause used like a temporary view.
•   Partitioned/Indexed View (e.g., SQL Server): view spread over partitions or with
a persisted index for performance (subject to strict rules).
c
CO- 3;
SO - 2;   [5]
BL-3
********** 13 **********

[Text in pictures on this page, read by OCR]
How to compute X * (step-by-step)

Given R, F, and X C R:
1. Initialize: X* < X.
2. Scan FDs repeatedly:
3. Repeat Step 2 until a full pass over JF” adds no new attributes to X + (i.e, fixpoint reached).
4. Result: the final X ~ is the closure.
--- page 14 ---
d   "All the modern applications require big data, fast features development, flexible
deployment, and the older database systems not competent enough, so the MongoDB was
needed.
The primary purpose of building MongoDB is:
CO- 4 ;
SO - 2;   o   Scalability
BL-1   [5]
o   Performance
o   High Availability
o   Scaling from single server deployments to large, complex multi-site
architectures.
"
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper b223e8dbbdfc

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_DS_7009/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (14 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech (DS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Diagrams must be neat and legible.
5. Ensure the correct question number is written in the answer sheet.
6. Qt1 is compulsary, attemp any 4 questions from remaining 6 questions.
Q1
Answer the following questions   [20]
a   Discuss the different types of users and describe how these users communicate with the
database
"In a DBMS, users are individuals or applications that interact with the database to perform
operations like querying, updating, or managing data. Depending on their role and
interaction level, they are classified into different types.
1. Types of Database Users
Naïve Users (End Users):
Use pre-defined application interfaces such as ATM software, online forms, or mobile apps.
CO- 1;   No direct interaction with the DBMS; use menu-driven or form-based interfaces.   [5]
SO- 2;
BL- 1   Application Programmers:
Write application programs that communicate with the database using languages like Java,
Python, or C++ through embedded SQL or APIs (e.g., JDBC, ODBC).
Database Designers:
Define the logical and physical structure of the database (schemas, constraints,
relationships).
Database Administrators (DBA):
Manage database access, user permissions, security, and backup.
Responsible for tuning performance and ensuring data integrity.
Sophisticated Users (Analysts / Data Scientists):
********** 1 **********
--- page 2 ---
Write SQL queries directly or use analytical tools to extract insights."
b   Problems with Bad Database Design [5 Marks]
A bad database design fails to properly organize data, leading to redundancy,
inconsistency, and performance issues.
Such designs often arise due to missing normalization or poor understanding of data
relationships.
1. Data Redundancy
•   The same data is stored in multiple places, wasting storage and making updates
difficult.
Example:
If a customer’s address is stored in several tables, updating it in one place but not
others causes mismatched data.
2. Data Inconsistency
• Due to redundancy, the same data may have different values in different tables.
Example:
In one record, a customer’s city is “Mumbai” and in another “Bombay” —
leading to confusion and inaccurate reports.
3. Insertion Anomalies
CO- 2;
SO - 2;   • You cannot insert new data without the presence of other unnecessary data.   [5]
BL- 2   Example:
Cannot add a new course in a table that stores StudentID, StudentName,
CourseName unless a student is enrolled in it.
4. Deletion Anomalies
•   Deleting one record may unintentionally remove valuable information.
Example:
Deleting the last student enrolled in “DBMS” may also delete the course
“DBMS” details.
5. Update Anomalies
•   Updating a value in one place requires multiple updates elsewhere.
Example:
Changing a department name requires updates in all employee records; missing
one leads to inconsistent data.
6. Poor Query Performance
•   Improper indexing and redundant fields slow down data retrieval and increase
maintenance costs.
c   (a) Possible Superkeys:
{EmpID}, {AadharNo}, {Email}, {EmpID, Name}, {AadharNo, Name}, etc.
CO- 3 ;   (b) Candidate Keys:
SO - 2;   [5]
{EmpID}, {AadharNo}, {Email}
BL- 2
(c) Primary Key:
EmpID — Unique
d   What are the advantages of NoSQL over traditional RDBMS and vice-versa?
CO- 4 ;   NoSQL is better than RDBMS because of the following reasons/properities of NoSQL:
SO - 2;   It   supports   semi-structured   data   and   volatile   data   [5]
BL-1   It   does   not   have   schema
Read/Write   throughput   is   very   high
Horizontal   scalability   can   be   achieved   easily
********** 2 **********
--- page 3 ---
Will   support   Bigdata   in   volumes   of   Terra   Bytes &   Peta   Bytes
Provides   good   support   for   Analytic   tools   on   top   of   Bigdata
Can   be   hosted   in   cheaper   hardware   machines
In-memory caching option is available to increase the performance of queries
Faster   development   life   cycles   for   developers
Still, RDBMS is better than NoSQL for the following reasons/properties of RDBMS:
Transactions with ACID properties - Atomicity, Consistency, Isolation & Durability
Adherence   to   Strong   Schema   of   data   being   written/read
Real time query management   ( in case of data size < 10 Tera bytes   )
Execution of complex queries involving join & group by clauses
Q2   [20]
a
CO- 1 ;
SO - 2;   [10]
BL-2
b   Consider following movie database:
movies (movie_id, title, release_year, runtime_min, language, country)
directors (director_id, first_name, birth_year)
actors (actor_id, first_name, birth_year)
movie_direction (movie_id, director_id, billing_order)
CO- 2 ;
SO - 2;   movie_cast (movie_id, actor_id, role_name, billing_order)   [10]
BL- 2
genres (genre_id, genre_name)
movie_genres (movie_id, genre_id)
Write the SQL queries the following question:
i   List the English-language movies released after 2020 with runtime > 140 minutes.
Ans:
SELECT title, release_year, runtime_min
FROM movies WHERE language = 'English' AND release_year > 2020
********** 3 **********
--- page 4 ---
AND runtime_min > 140;
ii   For each director, show the number of movies they directed and the average runtime of
those movies. Include only directors with at least 2 movies.
Ans:
SELECT d.first_name, COUNT (m. movie_id) AS total_movies, ROUND (AVG (m.
runtime_min), 2) AS avg_runtime
FROM directors d, movies m, movie_direction md
Where d. director_id = md. director_id and m. movie_id = md. movie_id
GROUP BY d. director_id, d. first_name
HAVING COUNT (m. movie_id) >= 2;
iii   List movies whose title length ≥ 12 and whose uppercased title starts with 'THE'.
Ans:
SELECT   title, LENGTH (title) AS title_len
FROM movies
WHERE LENGTH(title) >= 12
AND UPPER (title) LIKE 'THE%
iv   Find actors who have acted in more than one movie.
Ans:
SELECT a. actor_id, a. first_name, COUNT (*) AS movie_count
FROM actors a, movie_cast mc
Where mc. actor_id = a.actor_id
GROUP BY a. actor_id, a. first_name
HAVING COUNT (*) > 1;
v   Find movies that belong to multiple genres (two or more).
Ans:
SELECT m. movie_id, m. title, COUNT (mg. genre_id) AS genre_count
FROM movies m, movie_genres mg
GROUP BY m.movie_id, m.title
Having COUNT (m. movie_id) >= 2
Q3   [20]
a.   Here’s the final relational schema (no SQL) derived from your ERD.
CO- 1 ;   PKs are underlined; FKs noted after each table.
SO - 2;   [10]
BL- 2   •   PLAYER(PlayerID, PName, Technique, TeamID)
FK: TeamID → TEAM.TeamID
• TEAM(TeamID, TeamName)
********** 4 **********
--- page 5 ---
• GLOSSARY(Gid, Text, TeamID)
FK: TeamID → TEAM.TeamID
Constraint: 1:1 with TEAM (each team has at most one glossary)
• GAME(GameID, Name, Date)
•   REFEREE(RefID, RName)
• PLAYER_GLOSSARY(PlayerID, Gid)
FKs: PlayerID → PLAYER.PlayerID, Gid → GLOSSARY.Gid
(resolves Player uses Glossary M:N)
• PARTICIPATES(GameID, TeamID, Winner)
FKs: GameID → GAME.GameID, TeamID → TEAM.TeamID
(resolves Team participates in Game; each game has exactly 2 teams; exactly one
row per game with Winner = TRUE)
• GAME_REFEREE(GameID, RefID)
FKs: GameID → GAME.GameID, RefID → REFEREE.RefID
(resolves Game guided by Referee; each game has exactly 3 referees)
b.   Closure of (FacultyID, CourseID):
adds FacultyName, DeptID, DeptName, CourseName, Semester, RoomNo ⇒ all
attributes.
No proper subset (FacultyID alone or CourseID alone) determines all attributes.
Candidate key = {FacultyID, CourseID}. (Only one.)
Is the relation in 3NF? [2M]
3NF requires: for every FD (X\to A), either (X) is a superkey or (A) is prime.
Prime attributes = those in any key = {FacultyID, CourseID}.
Check violations:
•FacultyID → FacultyName, DeptID (X not superkey, RHS non-prime) ⇒ violates 3NF
•DeptID → DeptName (X not superkey, RHS non-prime) ⇒ violates
•CourseID → CourseName (X not superkey, RHS non-prime) ⇒ violates
CO- 3 ;
•RoomNo → DeptID (X not superkey, RHS non-prime) ⇒ violates
SO - 2;   [10]
BL- 3   Hence, relation is not in 3NF.
iii) Decompose to BCNF (step-by-step) [4M]
BCNF requires every non-trivial FD to have a superkey on the LHS.
Start: R(FacultyID, FacultyName, DeptID, DeptName, CourseID, CourseName, Semester,
RoomNo)
1.   Use FacultyID → FacultyName, DeptID (violates BCNF):
•   R1(FacultyID, FacultyName, DeptID) — key: FacultyID (BCNF)
•   R2(FacultyID, DeptID, DeptName, CourseID, CourseName, Semester,
RoomNo)
2.   In R2, DeptID → DeptName violates BCNF:
•   R21(DeptID, DeptName) — key: DeptID (BCNF)
•   R22(FacultyID, DeptID, CourseID, CourseName, Semester, RoomNo)
3.   In R22, CourseID → CourseName violates BCNF:
********** 5 **********
--- page 6 ---
•   R221(CourseID, CourseName) — key: CourseID (BCNF)
•   R222(FacultyID, DeptID, CourseID, Semester, RoomNo)
4.   In R222, RoomNo → DeptID violates BCNF:
•   R2221(RoomNo, DeptID) — key: RoomNo (BCNF)
•   R2222(FacultyID, CourseID, Semester, RoomNo)
Check R2222: (FacultyID, CourseID to Semester, RoomNo) has a superkey LHS
(FacultyID, CourseID is the key of R2222), so BCNF holds.
All resulting relations are now in BCNF.
________________________________________
iv) Final BCNF relations with primary keys [2M]
•   R1(FacultyID, FacultyName, DeptID)
•   R21(DeptID, DeptName)
•   R221(CourseID, CourseName)
•   R2221(RoomNo, DeptID)
•   R2222(FacultyID, CourseID, Semester, RoomNo)
These preserve the original FDs (each determinant appears as a key in some relation) and
the decomposition is lossless via common keys (e.g., DeptID, CourseID, RoomNo,
FacultyID).
Q4   [20]
a.   •   A primary goal of a database system is to retrieve information from and store   [10]
new information into the database. People who work with a database can be categorized
as database users or database administrators
•   Database User:
o   Naive users : are unsophisticated users who interact with the system by invoking
one of the application programs that have been written previously. For example, a clerk in
the university
o   Application programmers are computer professionals who write application
programs. Application programmers can choose from many tools to develop user
interfaces.
CO- 1 ;   o   Sophisticated users interact with the system without writing programs. Instead,
SO - 2;
they form their requests either using a database query language or by using tools such as
BL-2
data analysis software. Analysts who submit queries to explore data in the database fall in
this category.
o   Specialized users are sophisticated users who write specialized database
applications that do not fit into the traditional data-processing framework. Among these
applications are computer-aided design systems, knowledgebase and expert systems,
systems that store data with complex data types (for example, graphics data and audio
data), and environment- modelling systems.
•   The functions of a DBA include:
o   Schema definition. The DBA creates the original database schema by executing a
set of data definition statements in the DDL.
********** 6 **********
--- page 7 ---
o   Storage structure and access-method definition.
o   Schema and physical-organization modification. The DBA carries out changes to
the schema and physical organization to reflect the changing needs of the organization, or
to alter the physical organization to improve performance.
o   Granting of authorization for data access. By granting different types of
authorization, the database administrator can regulate which parts of the database various
users can access.
o   Routine maintenance. Examples of the database administrator’s routine
maintenance activities are:
•   Periodically backing up the database, either onto tapes or onto remote servers, to
prevent loss of data in case of disasters such as flooding.
•   Ensuring that enough free disk space is available for normal operations, and
upgrading disk space as required.
•   Monitoring jobs running on the database and ensuring that performance is not
degraded by very expensive tasks submitted by some users.
b.   Solve the following queries using relational algebra   [10]
Book(book_id, book_title, pub_year, num_pages, language, pub_date, pub_country)
Author(author_id, author_fname, author_lname)
Book_Author(author_id, book_id)
Review(book_id, review_id, review_stars, num_of_reviews)
CO- 2 ;   1.   List book titles along with their authors' names.
SO - 2;
BL-2
2. Get the first and last names of all authors who have written at least one book.
3. Find the book IDs that do not have any associated reviews.
4. determine those years in which there was at least one book that received a rating
of at least four stars.
5. Find books that have received a 5-star review.
Q5   [20]
CO- 2 ;   a.   Consider following e-commerce database:
SO - 2;   [10]
BL-2
********** 7 **********
--- page 8 ---
customers (customer_id, full_name, email, phone, city)
products (product_id   , name, unit_price stock_qty)
orders (order_id, customer_id, order_date, shipping_city, order_total)
order_items (order_id, product_id, qty, unit_price)
Write the SQL queries the following question:
i   Show each product’s total units sold and total revenue from order_items
Ans:
SELECT p. product_id, p.name, SUM (oi.qty), SUM (oi.qty * oi.unit_price) as Total
FROM products p   [3]
JOIN order_items oi ON oi. product_id = p.product_id
GROUP BY p. product_id, p.name
ORDER BY Total DESC;
ii   Show each product’s total units sold and total revenue from order_items. Return only
products with at least 2 units sold
Ans:
SELECT p. product_id, p.name, SUM (oi.qty), SUM (oi.qty * oi. unit_price)
[3]
FROM products p
JOIN order_items oi ON oi. product_id = p. product_id
GROUP BY p. product_id, p.name
HAVING SUM (oi.qty) >= 2
iii   Create the four tables with appropriate PRIMARY KEY constraints and sensible data types
Ans:
CREATE TABLE customers (
customer_id number PRIMARY KEY,
full_name VARCHAR (120) NOT NULL,
email   VARCHAR (180) UNIQUE NOT NULL,
phone   VARCHAR (20),
city   VARCHAR (80)   [4]
);
CREATE TABLE products (
product_id number PRIMARY KEY,
name   VARCHAR (25) NOT NULL,
unit_price NUMERIC (10,2) NOT NULL),
stock_qty INT NOT NULL
********** 8 **********
--- page 9 ---
);
CREATE TABLE orders (
order_id   SERIAL PRIMARY KEY,
customer_id INT NOT NULL,
order_date   date,
shipping_city VARCHAR (80),
order_total number (12,2) NOT NULL
);
CREATE TABLE order_items (
order_id INT NOT NULL,
product_id INT NOT NULL,
qty   INT NOT,
unit_price NUMERIC (10,2) NOT NULL,
PRIMARY KEY (order_id, product_id)
);
b.   Here’s a compact, exam-ready solution.
i) Dependencies on X (showing step references)
Read–Write (RW) (read first, later write on X):
• T1→T2 : (1) R by T1 before (3) W by T2
• T1→T3 : (1) R by T1 before (6) W by T3
• T2→T1 : (2) R by T2 before (5) W by T1
• T2→T3 : (2) R by T2 before (6) W by T3
• T3→T1 : (4) R by T3 before (5) W by T1
Write–Read (WR) (write first, later read on X):
• T2→T3 : (3) W by T2 before (4) R by T3
Write–Write (WW) (write first, later write on X):
• T2→T1 : (3) W by T2 before (5) W by T1
• T1→T3 : (5) W by T1 before (6) W by T3
• T2→T3 : (3) W by T2 before (6) W by T3
ii) Conflict serializability (2M)
Precedence edges from conflicts:
CO- 4 ;
SO - 2;   • T1→T2 (RW), T2→T1 (RW/WW) ⇒ cycle T1 ↔ T2   [10]
BL- 2   • T1→T3 (RW/WW) and T3→T1 (RW) ⇒ cycle T1 ↔ T3
•   (also T2→T3)
Since the graph has cycles, not conflict-serializable.
iii) View serializability (3M)
Identify read-from and final write in the given schedule:
•   (1) T1 reads X from initial value (no prior write) ⇒ T0 → T1
•   (2) T2 reads X from initial value ⇒ T0 → T2
•   (4) T3 reads X from T2’s write at (3) ⇒ T2 → T3
•   Final write on X is by T3 at (6).
For a serial schedule to be view-equivalent:
•   Both T1 and T2 must read initial X. In any serial order, only the first writing
transaction can read initial; the next reader (which also writes) would see the
prior write, not initial. Because both T1 and T2 write X, you cannot place them
serially so that both read the initial value.
Therefore, no serial schedule preserves these read-from relations and the final
write simultaneously.
Hence, not view-serializable.
********** 9 **********
--- page 10 ---
iv) View-equivalent serial schedule (2M)
None exists. Since (iii) fails, there is no serial order that is view-equivalent to the given
schedule.
Q6   [20]
a.   Here’s a clear, exam-ready 10-mark answer divided into two parts   [10]
Q1. States of a Transaction [5 Marks]
A transaction passes through several states during its execution in a DBMS.
1. States of a Transaction
State   Description
Active   The transaction is executing its read/write operations.
Partially
The transaction has executed its final statement but has not yet been p
Committed
All operations are successfully completed, and the changes are perma
Committed
database.
Failed   A fault or error occurs before the transaction commits. Changes made
All changes made by the transaction are rolled back (undone). The da
Aborted
previous consistent state.
CO- 4 ;
SO - 2;   2. State Transition Diagram
BL-3
Explanation:
•   If all steps succeed → transaction commits.
•   If any error/failure occurs → it aborts, and all partial updates are rolled back.
********** 10 **********
--- page 11 ---
Q2. Serializability [5 Marks]
Definition
A schedule is said to be serializable if its effect on the database is equivalent to some
serial execution of the same transactions, i.e., the final database state is the same as if
transactions were executed one after another without overlap.
Types of Serializability
1.   Conflict Serializability – Based on conflicting read/write operations; checked
using a precedence graph.
2. View Serializability – Based on equivalent read-from and final-write
relationships among transactions.
Importance of Serializability
•   Ensures consistency of the database in concurrent execution.
•   Prevents anomalies such as:
o   Lost update
o   Dirty read
o   Non-repeatable read
o   Inconsistent retrievals
•   Allows maximum concurrency while preserving correctness.
In short:
Serializability ensures that concurrent transactions produce the same result as some serial
order, maintaining database consistency and isolation—the core goal of concurrency
control in DBMS.
b.   "   [10]
1.   Document-Based Databases:
o   Description: Store data in JSON-like documents where each document can have
different fields.
o   Example: MongoDB, CouchDB.
o   Use Case: Storing user profiles, product catalogs.
2.   Key-Value Stores:
CO- 4 ;   o   Description: Data is stored as a collection of key-value pairs. Each key is unique
SO - 2;   and maps to a value.
BL-1
o   Example: Redis, Riak.
o   Use Case: Session management, caching.
3.   Column-Family Stores (Wide-Column Stores):
o   Description: Data is stored in columns rather than rows, optimized for queries on
large datasets.
o   Example: Apache Cassandra, HBase.
o   Use Case: Real-time analytics, large-scale data warehousing.
********** 11 **********
--- page 12 ---
4.   Graph Databases:
o   Description: Data is stored as nodes (entities) and edges (relationships), suitable
for connected data.
o   Example: Neo4j, Amazon Neptune.
o   Use Case: Social networks, recommendation engines, fraud detection
"
Q7
[20]
a   Levels of Data Abstraction
Databases hide storage details through three abstraction levels so users see only what they
need:
1. Physical Level (Internal Schema)
o What it shows: How data are stored: file organization, indexes, record
layouts, compression, page size, pointers.
o   Audience: DBMS engineers, DBAs.
o Example: B+-tree index on Emp(ID), heap file vs clustered file.
2. Logical/Conceptual Level (Conceptual Schema)
o What it shows: The global structure of the database: entities, attributes,
relationships, constraints—independent of storage.
o   Audience: Designers, application developers.
CO-1 ;   o Example: Relations EMP(EmpID, Name, DeptID) and DEPT(DeptID,
SO- 2;   DeptName) with FK DeptID.   [5]
BL-1   3. View Level (External Schemas / Views)
o What it shows: User-specific subsets or perspectives of the logical
schema; may hide sensitive or irrelevant attributes.
o   Audience: End users, applications.
o Example: View EmpPublic(EmpID, Name, DeptName) hiding salaries.
Data Independence (Why it matters)
•   Physical Data Independence: Change storage structures (e.g., add index) without
changing the conceptual schema/app code.
•   Logical Data Independence: Change conceptual schema (e.g., split a table)
without changing user views/programs.
b
What is a View?
A view is a named, stored query that presents data from one or more tables as a virtual
table.
It stores query definition, not the data (except materialized views).
Syntax (basic):
CREATE VIEW dept_emp AS
CO- 2 ;   SELECT e.EmpID, e.Name, d.DeptName
SO - 2;   FROM Employee e JOIN Department d USING (DeptID);   [5]
BL-2   Why use views?
•   Security: expose only needed columns/rows.
•   Simplicity: hide complex joins/filters.
•   Consistency: centralize business logic.
•   Logical independence: shield apps from base-table changes.
WITH CHECK OPTION ensures inserts/updates through the view still satisfy its
predicate.
********** 12 **********
--- page 13 ---
Types of Views (common classifications)
1) By data storage
•   Logical (Standard) View / Non-materialized view
o   Stores only the SELECT definition; data fetched at query time.
•   Materialized View (DB-dependent: Oracle, PostgreSQL, etc.)
o   Physically stores result set for speed; needs refresh.
o   Refresh modes: ON DEMAND (manual/scheduled) or ON COMMIT
(where supported); COMPLETE/FAST refresh options depending on
logs.
2) By query complexity
•   Simple View
o Based on one table, no aggregates, no DISTINCT, no GROUP BY/SET
ops.
o   Often updatable (subject to RDBMS rules).
o Example:
o CREATE VIEW active_customers AS
o SELECT CustID, Name, City
o FROM Customer
o WHERE Status = 'ACTIVE'
o WITH CHECK OPTION;
•   Complex View
o Based on multiple tables, joins, aggregates, DISTINCT, GROUP BY,
UNION, etc.
o   Usually read-only (non-updatable).
3) By updatability
•   Updatable View
o You can INSERT/UPDATE/DELETE through it if each row maps to
exactly one base-table row and no disqualifying clauses.
o   Typical conditions (vendor-agnostic): no DISTINCT, GROUP BY,
HAVING, aggregates, set operations, window functions; select all NOT
NULL key columns; no expressions on key columns.
•   Read-only View
o Any view violating the above (e.g., joins + aggregates). Some systems
allow INSTEAD OF triggers to make them updatable.
4) Other common terms (vendor-specific but useful)
•   Inline View: a subquery in the FROM clause used like a temporary view.
•   Partitioned/Indexed View (e.g., SQL Server): view spread over partitions or with
a persisted index for performance (subject to strict rules).
c
CO- 3;
SO - 2;   [5]
BL-3
********** 13 **********

[Text in pictures on this page, read by OCR]
How to compute X * (step-by-step)

Given R, F, and X C R:
1. Initialize: X* < X.
2. Scan FDs repeatedly:
3. Repeat Step 2 until a full pass over JF” adds no new attributes to X + (i.e, fixpoint reached).
4. Result: the final X ~ is the closure.
--- page 14 ---
d   "All the modern applications require big data, fast features development, flexible
deployment, and the older database systems not competent enough, so the MongoDB was
needed.
The primary purpose of building MongoDB is:
CO- 4 ;
SO - 2;   o   Scalability
BL-1   [5]
o   Performance
o   High Availability
o   Scaling from single server deployments to large, complex multi-site
architectures.
"
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper a5567f387bf1

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_IT_7001/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (14 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech (DS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Diagrams must be neat and legible.
5. Ensure the correct question number is written in the answer sheet.
6. Qt1 is compulsary, attemp any 4 questions from remaining 6 questions.
Q1
Answer the following questions   [20]
a   Discuss the different types of users and describe how these users communicate with the
database
"In a DBMS, users are individuals or applications that interact with the database to perform
operations like querying, updating, or managing data. Depending on their role and
interaction level, they are classified into different types.
1. Types of Database Users
Naïve Users (End Users):
Use pre-defined application interfaces such as ATM software, online forms, or mobile apps.
CO- 1;   No direct interaction with the DBMS; use menu-driven or form-based interfaces.   [5]
SO- 2;
BL- 1   Application Programmers:
Write application programs that communicate with the database using languages like Java,
Python, or C++ through embedded SQL or APIs (e.g., JDBC, ODBC).
Database Designers:
Define the logical and physical structure of the database (schemas, constraints,
relationships).
Database Administrators (DBA):
Manage database access, user permissions, security, and backup.
Responsible for tuning performance and ensuring data integrity.
Sophisticated Users (Analysts / Data Scientists):
********** 1 **********
--- page 2 ---
Write SQL queries directly or use analytical tools to extract insights."
b   Problems with Bad Database Design [5 Marks]
A bad database design fails to properly organize data, leading to redundancy,
inconsistency, and performance issues.
Such designs often arise due to missing normalization or poor understanding of data
relationships.
1. Data Redundancy
•   The same data is stored in multiple places, wasting storage and making updates
difficult.
Example:
If a customer’s address is stored in several tables, updating it in one place but not
others causes mismatched data.
2. Data Inconsistency
• Due to redundancy, the same data may have different values in different tables.
Example:
In one record, a customer’s city is “Mumbai” and in another “Bombay” —
leading to confusion and inaccurate reports.
3. Insertion Anomalies
CO- 2;
SO - 2;   • You cannot insert new data without the presence of other unnecessary data.   [5]
BL- 2   Example:
Cannot add a new course in a table that stores StudentID, StudentName,
CourseName unless a student is enrolled in it.
4. Deletion Anomalies
•   Deleting one record may unintentionally remove valuable information.
Example:
Deleting the last student enrolled in “DBMS” may also delete the course
“DBMS” details.
5. Update Anomalies
•   Updating a value in one place requires multiple updates elsewhere.
Example:
Changing a department name requires updates in all employee records; missing
one leads to inconsistent data.
6. Poor Query Performance
•   Improper indexing and redundant fields slow down data retrieval and increase
maintenance costs.
c   (a) Possible Superkeys:
{EmpID}, {AadharNo}, {Email}, {EmpID, Name}, {AadharNo, Name}, etc.
CO- 3 ;   (b) Candidate Keys:
SO - 2;   [5]
{EmpID}, {AadharNo}, {Email}
BL- 2
(c) Primary Key:
EmpID — Unique
d   What are the advantages of NoSQL over traditional RDBMS and vice-versa?
CO- 4 ;   NoSQL is better than RDBMS because of the following reasons/properities of NoSQL:
SO - 2;   It   supports   semi-structured   data   and   volatile   data   [5]
BL-1   It   does   not   have   schema
Read/Write   throughput   is   very   high
Horizontal   scalability   can   be   achieved   easily
********** 2 **********
--- page 3 ---
Will   support   Bigdata   in   volumes   of   Terra   Bytes &   Peta   Bytes
Provides   good   support   for   Analytic   tools   on   top   of   Bigdata
Can   be   hosted   in   cheaper   hardware   machines
In-memory caching option is available to increase the performance of queries
Faster   development   life   cycles   for   developers
Still, RDBMS is better than NoSQL for the following reasons/properties of RDBMS:
Transactions with ACID properties - Atomicity, Consistency, Isolation & Durability
Adherence   to   Strong   Schema   of   data   being   written/read
Real time query management   ( in case of data size < 10 Tera bytes   )
Execution of complex queries involving join & group by clauses
Q2   [20]
a
CO- 1 ;
SO - 2;   [10]
BL-2
b   Consider following movie database:
movies (movie_id, title, release_year, runtime_min, language, country)
directors (director_id, first_name, birth_year)
actors (actor_id, first_name, birth_year)
movie_direction (movie_id, director_id, billing_order)
CO- 2 ;
SO - 2;   movie_cast (movie_id, actor_id, role_name, billing_order)   [10]
BL- 2
genres (genre_id, genre_name)
movie_genres (movie_id, genre_id)
Write the SQL queries the following question:
i   List the English-language movies released after 2020 with runtime > 140 minutes.
Ans:
SELECT title, release_year, runtime_min
FROM movies WHERE language = 'English' AND release_year > 2020
********** 3 **********
--- page 4 ---
AND runtime_min > 140;
ii   For each director, show the number of movies they directed and the average runtime of
those movies. Include only directors with at least 2 movies.
Ans:
SELECT d.first_name, COUNT (m. movie_id) AS total_movies, ROUND (AVG (m.
runtime_min), 2) AS avg_runtime
FROM directors d, movies m, movie_direction md
Where d. director_id = md. director_id and m. movie_id = md. movie_id
GROUP BY d. director_id, d. first_name
HAVING COUNT (m. movie_id) >= 2;
iii   List movies whose title length ≥ 12 and whose uppercased title starts with 'THE'.
Ans:
SELECT   title, LENGTH (title) AS title_len
FROM movies
WHERE LENGTH(title) >= 12
AND UPPER (title) LIKE 'THE%
iv   Find actors who have acted in more than one movie.
Ans:
SELECT a. actor_id, a. first_name, COUNT (*) AS movie_count
FROM actors a, movie_cast mc
Where mc. actor_id = a.actor_id
GROUP BY a. actor_id, a. first_name
HAVING COUNT (*) > 1;
v   Find movies that belong to multiple genres (two or more).
Ans:
SELECT m. movie_id, m. title, COUNT (mg. genre_id) AS genre_count
FROM movies m, movie_genres mg
GROUP BY m.movie_id, m.title
Having COUNT (m. movie_id) >= 2
Q3   [20]
a.   Here’s the final relational schema (no SQL) derived from your ERD.
CO- 1 ;   PKs are underlined; FKs noted after each table.
SO - 2;   [10]
BL- 2   •   PLAYER(PlayerID, PName, Technique, TeamID)
FK: TeamID → TEAM.TeamID
• TEAM(TeamID, TeamName)
********** 4 **********
--- page 5 ---
• GLOSSARY(Gid, Text, TeamID)
FK: TeamID → TEAM.TeamID
Constraint: 1:1 with TEAM (each team has at most one glossary)
• GAME(GameID, Name, Date)
•   REFEREE(RefID, RName)
• PLAYER_GLOSSARY(PlayerID, Gid)
FKs: PlayerID → PLAYER.PlayerID, Gid → GLOSSARY.Gid
(resolves Player uses Glossary M:N)
• PARTICIPATES(GameID, TeamID, Winner)
FKs: GameID → GAME.GameID, TeamID → TEAM.TeamID
(resolves Team participates in Game; each game has exactly 2 teams; exactly one
row per game with Winner = TRUE)
• GAME_REFEREE(GameID, RefID)
FKs: GameID → GAME.GameID, RefID → REFEREE.RefID
(resolves Game guided by Referee; each game has exactly 3 referees)
b.   Closure of (FacultyID, CourseID):
adds FacultyName, DeptID, DeptName, CourseName, Semester, RoomNo ⇒ all
attributes.
No proper subset (FacultyID alone or CourseID alone) determines all attributes.
Candidate key = {FacultyID, CourseID}. (Only one.)
Is the relation in 3NF? [2M]
3NF requires: for every FD (X\to A), either (X) is a superkey or (A) is prime.
Prime attributes = those in any key = {FacultyID, CourseID}.
Check violations:
•FacultyID → FacultyName, DeptID (X not superkey, RHS non-prime) ⇒ violates 3NF
•DeptID → DeptName (X not superkey, RHS non-prime) ⇒ violates
•CourseID → CourseName (X not superkey, RHS non-prime) ⇒ violates
CO- 3 ;
•RoomNo → DeptID (X not superkey, RHS non-prime) ⇒ violates
SO - 2;   [10]
BL- 3   Hence, relation is not in 3NF.
iii) Decompose to BCNF (step-by-step) [4M]
BCNF requires every non-trivial FD to have a superkey on the LHS.
Start: R(FacultyID, FacultyName, DeptID, DeptName, CourseID, CourseName, Semester,
RoomNo)
1.   Use FacultyID → FacultyName, DeptID (violates BCNF):
•   R1(FacultyID, FacultyName, DeptID) — key: FacultyID (BCNF)
•   R2(FacultyID, DeptID, DeptName, CourseID, CourseName, Semester,
RoomNo)
2.   In R2, DeptID → DeptName violates BCNF:
•   R21(DeptID, DeptName) — key: DeptID (BCNF)
•   R22(FacultyID, DeptID, CourseID, CourseName, Semester, RoomNo)
3.   In R22, CourseID → CourseName violates BCNF:
********** 5 **********
--- page 6 ---
•   R221(CourseID, CourseName) — key: CourseID (BCNF)
•   R222(FacultyID, DeptID, CourseID, Semester, RoomNo)
4.   In R222, RoomNo → DeptID violates BCNF:
•   R2221(RoomNo, DeptID) — key: RoomNo (BCNF)
•   R2222(FacultyID, CourseID, Semester, RoomNo)
Check R2222: (FacultyID, CourseID to Semester, RoomNo) has a superkey LHS
(FacultyID, CourseID is the key of R2222), so BCNF holds.
All resulting relations are now in BCNF.
________________________________________
iv) Final BCNF relations with primary keys [2M]
•   R1(FacultyID, FacultyName, DeptID)
•   R21(DeptID, DeptName)
•   R221(CourseID, CourseName)
•   R2221(RoomNo, DeptID)
•   R2222(FacultyID, CourseID, Semester, RoomNo)
These preserve the original FDs (each determinant appears as a key in some relation) and
the decomposition is lossless via common keys (e.g., DeptID, CourseID, RoomNo,
FacultyID).
Q4   [20]
a.   •   A primary goal of a database system is to retrieve information from and store   [10]
new information into the database. People who work with a database can be categorized
as database users or database administrators
•   Database User:
o   Naive users : are unsophisticated users who interact with the system by invoking
one of the application programs that have been written previously. For example, a clerk in
the university
o   Application programmers are computer professionals who write application
programs. Application programmers can choose from many tools to develop user
interfaces.
CO- 1 ;   o   Sophisticated users interact with the system without writing programs. Instead,
SO - 2;
they form their requests either using a database query language or by using tools such as
BL-2
data analysis software. Analysts who submit queries to explore data in the database fall in
this category.
o   Specialized users are sophisticated users who write specialized database
applications that do not fit into the traditional data-processing framework. Among these
applications are computer-aided design systems, knowledgebase and expert systems,
systems that store data with complex data types (for example, graphics data and audio
data), and environment- modelling systems.
•   The functions of a DBA include:
o   Schema definition. The DBA creates the original database schema by executing a
set of data definition statements in the DDL.
********** 6 **********
--- page 7 ---
o   Storage structure and access-method definition.
o   Schema and physical-organization modification. The DBA carries out changes to
the schema and physical organization to reflect the changing needs of the organization, or
to alter the physical organization to improve performance.
o   Granting of authorization for data access. By granting different types of
authorization, the database administrator can regulate which parts of the database various
users can access.
o   Routine maintenance. Examples of the database administrator’s routine
maintenance activities are:
•   Periodically backing up the database, either onto tapes or onto remote servers, to
prevent loss of data in case of disasters such as flooding.
•   Ensuring that enough free disk space is available for normal operations, and
upgrading disk space as required.
•   Monitoring jobs running on the database and ensuring that performance is not
degraded by very expensive tasks submitted by some users.
b.   Solve the following queries using relational algebra   [10]
Book(book_id, book_title, pub_year, num_pages, language, pub_date, pub_country)
Author(author_id, author_fname, author_lname)
Book_Author(author_id, book_id)
Review(book_id, review_id, review_stars, num_of_reviews)
CO- 2 ;   1.   List book titles along with their authors' names.
SO - 2;
BL-2
2. Get the first and last names of all authors who have written at least one book.
3. Find the book IDs that do not have any associated reviews.
4. determine those years in which there was at least one book that received a rating
of at least four stars.
5. Find books that have received a 5-star review.
Q5   [20]
CO- 2 ;   a.   Consider following e-commerce database:
SO - 2;   [10]
BL-2
********** 7 **********
--- page 8 ---
customers (customer_id, full_name, email, phone, city)
products (product_id   , name, unit_price stock_qty)
orders (order_id, customer_id, order_date, shipping_city, order_total)
order_items (order_id, product_id, qty, unit_price)
Write the SQL queries the following question:
i   Show each product’s total units sold and total revenue from order_items
Ans:
SELECT p. product_id, p.name, SUM (oi.qty), SUM (oi.qty * oi.unit_price) as Total
FROM products p   [3]
JOIN order_items oi ON oi. product_id = p.product_id
GROUP BY p. product_id, p.name
ORDER BY Total DESC;
ii   Show each product’s total units sold and total revenue from order_items. Return only
products with at least 2 units sold
Ans:
SELECT p. product_id, p.name, SUM (oi.qty), SUM (oi.qty * oi. unit_price)
[3]
FROM products p
JOIN order_items oi ON oi. product_id = p. product_id
GROUP BY p. product_id, p.name
HAVING SUM (oi.qty) >= 2
iii   Create the four tables with appropriate PRIMARY KEY constraints and sensible data types
Ans:
CREATE TABLE customers (
customer_id number PRIMARY KEY,
full_name VARCHAR (120) NOT NULL,
email   VARCHAR (180) UNIQUE NOT NULL,
phone   VARCHAR (20),
city   VARCHAR (80)   [4]
);
CREATE TABLE products (
product_id number PRIMARY KEY,
name   VARCHAR (25) NOT NULL,
unit_price NUMERIC (10,2) NOT NULL),
stock_qty INT NOT NULL
********** 8 **********
--- page 9 ---
);
CREATE TABLE orders (
order_id   SERIAL PRIMARY KEY,
customer_id INT NOT NULL,
order_date   date,
shipping_city VARCHAR (80),
order_total number (12,2) NOT NULL
);
CREATE TABLE order_items (
order_id INT NOT NULL,
product_id INT NOT NULL,
qty   INT NOT,
unit_price NUMERIC (10,2) NOT NULL,
PRIMARY KEY (order_id, product_id)
);
b.   Here’s a compact, exam-ready solution.
i) Dependencies on X (showing step references)
Read–Write (RW) (read first, later write on X):
• T1→T2 : (1) R by T1 before (3) W by T2
• T1→T3 : (1) R by T1 before (6) W by T3
• T2→T1 : (2) R by T2 before (5) W by T1
• T2→T3 : (2) R by T2 before (6) W by T3
• T3→T1 : (4) R by T3 before (5) W by T1
Write–Read (WR) (write first, later read on X):
• T2→T3 : (3) W by T2 before (4) R by T3
Write–Write (WW) (write first, later write on X):
• T2→T1 : (3) W by T2 before (5) W by T1
• T1→T3 : (5) W by T1 before (6) W by T3
• T2→T3 : (3) W by T2 before (6) W by T3
ii) Conflict serializability (2M)
Precedence edges from conflicts:
CO- 4 ;
SO - 2;   • T1→T2 (RW), T2→T1 (RW/WW) ⇒ cycle T1 ↔ T2   [10]
BL- 2   • T1→T3 (RW/WW) and T3→T1 (RW) ⇒ cycle T1 ↔ T3
•   (also T2→T3)
Since the graph has cycles, not conflict-serializable.
iii) View serializability (3M)
Identify read-from and final write in the given schedule:
•   (1) T1 reads X from initial value (no prior write) ⇒ T0 → T1
•   (2) T2 reads X from initial value ⇒ T0 → T2
•   (4) T3 reads X from T2’s write at (3) ⇒ T2 → T3
•   Final write on X is by T3 at (6).
For a serial schedule to be view-equivalent:
•   Both T1 and T2 must read initial X. In any serial order, only the first writing
transaction can read initial; the next reader (which also writes) would see the
prior write, not initial. Because both T1 and T2 write X, you cannot place them
serially so that both read the initial value.
Therefore, no serial schedule preserves these read-from relations and the final
write simultaneously.
Hence, not view-serializable.
********** 9 **********
--- page 10 ---
iv) View-equivalent serial schedule (2M)
None exists. Since (iii) fails, there is no serial order that is view-equivalent to the given
schedule.
Q6   [20]
a.   Here’s a clear, exam-ready 10-mark answer divided into two parts   [10]
Q1. States of a Transaction [5 Marks]
A transaction passes through several states during its execution in a DBMS.
1. States of a Transaction
State   Description
Active   The transaction is executing its read/write operations.
Partially
The transaction has executed its final statement but has not yet been p
Committed
All operations are successfully completed, and the changes are perma
Committed
database.
Failed   A fault or error occurs before the transaction commits. Changes made
All changes made by the transaction are rolled back (undone). The da
Aborted
previous consistent state.
CO- 4 ;
SO - 2;   2. State Transition Diagram
BL-3
Explanation:
•   If all steps succeed → transaction commits.
•   If any error/failure occurs → it aborts, and all partial updates are rolled back.
********** 10 **********
--- page 11 ---
Q2. Serializability [5 Marks]
Definition
A schedule is said to be serializable if its effect on the database is equivalent to some
serial execution of the same transactions, i.e., the final database state is the same as if
transactions were executed one after another without overlap.
Types of Serializability
1.   Conflict Serializability – Based on conflicting read/write operations; checked
using a precedence graph.
2. View Serializability – Based on equivalent read-from and final-write
relationships among transactions.
Importance of Serializability
•   Ensures consistency of the database in concurrent execution.
•   Prevents anomalies such as:
o   Lost update
o   Dirty read
o   Non-repeatable read
o   Inconsistent retrievals
•   Allows maximum concurrency while preserving correctness.
In short:
Serializability ensures that concurrent transactions produce the same result as some serial
order, maintaining database consistency and isolation—the core goal of concurrency
control in DBMS.
b.   "   [10]
1.   Document-Based Databases:
o   Description: Store data in JSON-like documents where each document can have
different fields.
o   Example: MongoDB, CouchDB.
o   Use Case: Storing user profiles, product catalogs.
2.   Key-Value Stores:
CO- 4 ;   o   Description: Data is stored as a collection of key-value pairs. Each key is unique
SO - 2;   and maps to a value.
BL-1
o   Example: Redis, Riak.
o   Use Case: Session management, caching.
3.   Column-Family Stores (Wide-Column Stores):
o   Description: Data is stored in columns rather than rows, optimized for queries on
large datasets.
o   Example: Apache Cassandra, HBase.
o   Use Case: Real-time analytics, large-scale data warehousing.
********** 11 **********
--- page 12 ---
4.   Graph Databases:
o   Description: Data is stored as nodes (entities) and edges (relationships), suitable
for connected data.
o   Example: Neo4j, Amazon Neptune.
o   Use Case: Social networks, recommendation engines, fraud detection
"
Q7
[20]
a   Levels of Data Abstraction
Databases hide storage details through three abstraction levels so users see only what they
need:
1. Physical Level (Internal Schema)
o What it shows: How data are stored: file organization, indexes, record
layouts, compression, page size, pointers.
o   Audience: DBMS engineers, DBAs.
o Example: B+-tree index on Emp(ID), heap file vs clustered file.
2. Logical/Conceptual Level (Conceptual Schema)
o What it shows: The global structure of the database: entities, attributes,
relationships, constraints—independent of storage.
o   Audience: Designers, application developers.
CO-1 ;   o Example: Relations EMP(EmpID, Name, DeptID) and DEPT(DeptID,
SO- 2;   DeptName) with FK DeptID.   [5]
BL-1   3. View Level (External Schemas / Views)
o What it shows: User-specific subsets or perspectives of the logical
schema; may hide sensitive or irrelevant attributes.
o   Audience: End users, applications.
o Example: View EmpPublic(EmpID, Name, DeptName) hiding salaries.
Data Independence (Why it matters)
•   Physical Data Independence: Change storage structures (e.g., add index) without
changing the conceptual schema/app code.
•   Logical Data Independence: Change conceptual schema (e.g., split a table)
without changing user views/programs.
b
What is a View?
A view is a named, stored query that presents data from one or more tables as a virtual
table.
It stores query definition, not the data (except materialized views).
Syntax (basic):
CREATE VIEW dept_emp AS
CO- 2 ;   SELECT e.EmpID, e.Name, d.DeptName
SO - 2;   FROM Employee e JOIN Department d USING (DeptID);   [5]
BL-2   Why use views?
•   Security: expose only needed columns/rows.
•   Simplicity: hide complex joins/filters.
•   Consistency: centralize business logic.
•   Logical independence: shield apps from base-table changes.
WITH CHECK OPTION ensures inserts/updates through the view still satisfy its
predicate.
********** 12 **********
--- page 13 ---
Types of Views (common classifications)
1) By data storage
•   Logical (Standard) View / Non-materialized view
o   Stores only the SELECT definition; data fetched at query time.
•   Materialized View (DB-dependent: Oracle, PostgreSQL, etc.)
o   Physically stores result set for speed; needs refresh.
o   Refresh modes: ON DEMAND (manual/scheduled) or ON COMMIT
(where supported); COMPLETE/FAST refresh options depending on
logs.
2) By query complexity
•   Simple View
o Based on one table, no aggregates, no DISTINCT, no GROUP BY/SET
ops.
o   Often updatable (subject to RDBMS rules).
o Example:
o CREATE VIEW active_customers AS
o SELECT CustID, Name, City
o FROM Customer
o WHERE Status = 'ACTIVE'
o WITH CHECK OPTION;
•   Complex View
o Based on multiple tables, joins, aggregates, DISTINCT, GROUP BY,
UNION, etc.
o   Usually read-only (non-updatable).
3) By updatability
•   Updatable View
o You can INSERT/UPDATE/DELETE through it if each row maps to
exactly one base-table row and no disqualifying clauses.
o   Typical conditions (vendor-agnostic): no DISTINCT, GROUP BY,
HAVING, aggregates, set operations, window functions; select all NOT
NULL key columns; no expressions on key columns.
•   Read-only View
o Any view violating the above (e.g., joins + aggregates). Some systems
allow INSTEAD OF triggers to make them updatable.
4) Other common terms (vendor-specific but useful)
•   Inline View: a subquery in the FROM clause used like a temporary view.
•   Partitioned/Indexed View (e.g., SQL Server): view spread over partitions or with
a persisted index for performance (subject to strict rules).
c
CO- 3;
SO - 2;   [5]
BL-3
********** 13 **********

[Text in pictures on this page, read by OCR]
How to compute X * (step-by-step)

Given R, F, and X C R:
1. Initialize: X* < X.
2. Scan FDs repeatedly:
3. Repeat Step 2 until a full pass over JF” adds no new attributes to X + (i.e, fixpoint reached).
4. Result: the final X ~ is the closure.
--- page 14 ---
d   "All the modern applications require big data, fast features development, flexible
deployment, and the older database systems not competent enough, so the MongoDB was
needed.
The primary purpose of building MongoDB is:
CO- 4 ;
SO - 2;   o   Scalability
BL-1   [5]
o   Performance
o   High Availability
o   Scaling from single server deployments to large, complex multi-site
architectures.
"
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper aa8ca68f3ba1

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_IT_7041/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (14 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech (DS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Diagrams must be neat and legible.
5. Ensure the correct question number is written in the answer sheet.
6. Qt1 is compulsary, attemp any 4 questions from remaining 6 questions.
Q1
Answer the following questions   [20]
a   Discuss the different types of users and describe how these users communicate with the
database
"In a DBMS, users are individuals or applications that interact with the database to perform
operations like querying, updating, or managing data. Depending on their role and
interaction level, they are classified into different types.
1. Types of Database Users
Naïve Users (End Users):
Use pre-defined application interfaces such as ATM software, online forms, or mobile apps.
CO- 1;   No direct interaction with the DBMS; use menu-driven or form-based interfaces.   [5]
SO- 2;
BL- 1   Application Programmers:
Write application programs that communicate with the database using languages like Java,
Python, or C++ through embedded SQL or APIs (e.g., JDBC, ODBC).
Database Designers:
Define the logical and physical structure of the database (schemas, constraints,
relationships).
Database Administrators (DBA):
Manage database access, user permissions, security, and backup.
Responsible for tuning performance and ensuring data integrity.
Sophisticated Users (Analysts / Data Scientists):
********** 1 **********
--- page 2 ---
Write SQL queries directly or use analytical tools to extract insights."
b   Problems with Bad Database Design [5 Marks]
A bad database design fails to properly organize data, leading to redundancy,
inconsistency, and performance issues.
Such designs often arise due to missing normalization or poor understanding of data
relationships.
1. Data Redundancy
•   The same data is stored in multiple places, wasting storage and making updates
difficult.
Example:
If a customer’s address is stored in several tables, updating it in one place but not
others causes mismatched data.
2. Data Inconsistency
• Due to redundancy, the same data may have different values in different tables.
Example:
In one record, a customer’s city is “Mumbai” and in another “Bombay” —
leading to confusion and inaccurate reports.
3. Insertion Anomalies
CO- 2;
SO - 2;   • You cannot insert new data without the presence of other unnecessary data.   [5]
BL- 2   Example:
Cannot add a new course in a table that stores StudentID, StudentName,
CourseName unless a student is enrolled in it.
4. Deletion Anomalies
•   Deleting one record may unintentionally remove valuable information.
Example:
Deleting the last student enrolled in “DBMS” may also delete the course
“DBMS” details.
5. Update Anomalies
•   Updating a value in one place requires multiple updates elsewhere.
Example:
Changing a department name requires updates in all employee records; missing
one leads to inconsistent data.
6. Poor Query Performance
•   Improper indexing and redundant fields slow down data retrieval and increase
maintenance costs.
c   (a) Possible Superkeys:
{EmpID}, {AadharNo}, {Email}, {EmpID, Name}, {AadharNo, Name}, etc.
CO- 3 ;   (b) Candidate Keys:
SO - 2;   [5]
{EmpID}, {AadharNo}, {Email}
BL- 2
(c) Primary Key:
EmpID — Unique
d   What are the advantages of NoSQL over traditional RDBMS and vice-versa?
CO- 4 ;   NoSQL is better than RDBMS because of the following reasons/properities of NoSQL:
SO - 2;   It   supports   semi-structured   data   and   volatile   data   [5]
BL-1   It   does   not   have   schema
Read/Write   throughput   is   very   high
Horizontal   scalability   can   be   achieved   easily
********** 2 **********
--- page 3 ---
Will   support   Bigdata   in   volumes   of   Terra   Bytes &   Peta   Bytes
Provides   good   support   for   Analytic   tools   on   top   of   Bigdata
Can   be   hosted   in   cheaper   hardware   machines
In-memory caching option is available to increase the performance of queries
Faster   development   life   cycles   for   developers
Still, RDBMS is better than NoSQL for the following reasons/properties of RDBMS:
Transactions with ACID properties - Atomicity, Consistency, Isolation & Durability
Adherence   to   Strong   Schema   of   data   being   written/read
Real time query management   ( in case of data size < 10 Tera bytes   )
Execution of complex queries involving join & group by clauses
Q2   [20]
a
CO- 1 ;
SO - 2;   [10]
BL-2
b   Consider following movie database:
movies (movie_id, title, release_year, runtime_min, language, country)
directors (director_id, first_name, birth_year)
actors (actor_id, first_name, birth_year)
movie_direction (movie_id, director_id, billing_order)
CO- 2 ;
SO - 2;   movie_cast (movie_id, actor_id, role_name, billing_order)   [10]
BL- 2
genres (genre_id, genre_name)
movie_genres (movie_id, genre_id)
Write the SQL queries the following question:
i   List the English-language movies released after 2020 with runtime > 140 minutes.
Ans:
SELECT title, release_year, runtime_min
FROM movies WHERE language = 'English' AND release_year > 2020
********** 3 **********
--- page 4 ---
AND runtime_min > 140;
ii   For each director, show the number of movies they directed and the average runtime of
those movies. Include only directors with at least 2 movies.
Ans:
SELECT d.first_name, COUNT (m. movie_id) AS total_movies, ROUND (AVG (m.
runtime_min), 2) AS avg_runtime
FROM directors d, movies m, movie_direction md
Where d. director_id = md. director_id and m. movie_id = md. movie_id
GROUP BY d. director_id, d. first_name
HAVING COUNT (m. movie_id) >= 2;
iii   List movies whose title length ≥ 12 and whose uppercased title starts with 'THE'.
Ans:
SELECT   title, LENGTH (title) AS title_len
FROM movies
WHERE LENGTH(title) >= 12
AND UPPER (title) LIKE 'THE%
iv   Find actors who have acted in more than one movie.
Ans:
SELECT a. actor_id, a. first_name, COUNT (*) AS movie_count
FROM actors a, movie_cast mc
Where mc. actor_id = a.actor_id
GROUP BY a. actor_id, a. first_name
HAVING COUNT (*) > 1;
v   Find movies that belong to multiple genres (two or more).
Ans:
SELECT m. movie_id, m. title, COUNT (mg. genre_id) AS genre_count
FROM movies m, movie_genres mg
GROUP BY m.movie_id, m.title
Having COUNT (m. movie_id) >= 2
Q3   [20]
a.   Here’s the final relational schema (no SQL) derived from your ERD.
CO- 1 ;   PKs are underlined; FKs noted after each table.
SO - 2;   [10]
BL- 2   •   PLAYER(PlayerID, PName, Technique, TeamID)
FK: TeamID → TEAM.TeamID
• TEAM(TeamID, TeamName)
********** 4 **********
--- page 5 ---
• GLOSSARY(Gid, Text, TeamID)
FK: TeamID → TEAM.TeamID
Constraint: 1:1 with TEAM (each team has at most one glossary)
• GAME(GameID, Name, Date)
•   REFEREE(RefID, RName)
• PLAYER_GLOSSARY(PlayerID, Gid)
FKs: PlayerID → PLAYER.PlayerID, Gid → GLOSSARY.Gid
(resolves Player uses Glossary M:N)
• PARTICIPATES(GameID, TeamID, Winner)
FKs: GameID → GAME.GameID, TeamID → TEAM.TeamID
(resolves Team participates in Game; each game has exactly 2 teams; exactly one
row per game with Winner = TRUE)
• GAME_REFEREE(GameID, RefID)
FKs: GameID → GAME.GameID, RefID → REFEREE.RefID
(resolves Game guided by Referee; each game has exactly 3 referees)
b.   Closure of (FacultyID, CourseID):
adds FacultyName, DeptID, DeptName, CourseName, Semester, RoomNo ⇒ all
attributes.
No proper subset (FacultyID alone or CourseID alone) determines all attributes.
Candidate key = {FacultyID, CourseID}. (Only one.)
Is the relation in 3NF? [2M]
3NF requires: for every FD (X\to A), either (X) is a superkey or (A) is prime.
Prime attributes = those in any key = {FacultyID, CourseID}.
Check violations:
•FacultyID → FacultyName, DeptID (X not superkey, RHS non-prime) ⇒ violates 3NF
•DeptID → DeptName (X not superkey, RHS non-prime) ⇒ violates
•CourseID → CourseName (X not superkey, RHS non-prime) ⇒ violates
CO- 3 ;
•RoomNo → DeptID (X not superkey, RHS non-prime) ⇒ violates
SO - 2;   [10]
BL- 3   Hence, relation is not in 3NF.
iii) Decompose to BCNF (step-by-step) [4M]
BCNF requires every non-trivial FD to have a superkey on the LHS.
Start: R(FacultyID, FacultyName, DeptID, DeptName, CourseID, CourseName, Semester,
RoomNo)
1.   Use FacultyID → FacultyName, DeptID (violates BCNF):
•   R1(FacultyID, FacultyName, DeptID) — key: FacultyID (BCNF)
•   R2(FacultyID, DeptID, DeptName, CourseID, CourseName, Semester,
RoomNo)
2.   In R2, DeptID → DeptName violates BCNF:
•   R21(DeptID, DeptName) — key: DeptID (BCNF)
•   R22(FacultyID, DeptID, CourseID, CourseName, Semester, RoomNo)
3.   In R22, CourseID → CourseName violates BCNF:
********** 5 **********
--- page 6 ---
•   R221(CourseID, CourseName) — key: CourseID (BCNF)
•   R222(FacultyID, DeptID, CourseID, Semester, RoomNo)
4.   In R222, RoomNo → DeptID violates BCNF:
•   R2221(RoomNo, DeptID) — key: RoomNo (BCNF)
•   R2222(FacultyID, CourseID, Semester, RoomNo)
Check R2222: (FacultyID, CourseID to Semester, RoomNo) has a superkey LHS
(FacultyID, CourseID is the key of R2222), so BCNF holds.
All resulting relations are now in BCNF.
________________________________________
iv) Final BCNF relations with primary keys [2M]
•   R1(FacultyID, FacultyName, DeptID)
•   R21(DeptID, DeptName)
•   R221(CourseID, CourseName)
•   R2221(RoomNo, DeptID)
•   R2222(FacultyID, CourseID, Semester, RoomNo)
These preserve the original FDs (each determinant appears as a key in some relation) and
the decomposition is lossless via common keys (e.g., DeptID, CourseID, RoomNo,
FacultyID).
Q4   [20]
a.   •   A primary goal of a database system is to retrieve information from and store   [10]
new information into the database. People who work with a database can be categorized
as database users or database administrators
•   Database User:
o   Naive users : are unsophisticated users who interact with the system by invoking
one of the application programs that have been written previously. For example, a clerk in
the university
o   Application programmers are computer professionals who write application
programs. Application programmers can choose from many tools to develop user
interfaces.
CO- 1 ;   o   Sophisticated users interact with the system without writing programs. Instead,
SO - 2;
they form their requests either using a database query language or by using tools such as
BL-2
data analysis software. Analysts who submit queries to explore data in the database fall in
this category.
o   Specialized users are sophisticated users who write specialized database
applications that do not fit into the traditional data-processing framework. Among these
applications are computer-aided design systems, knowledgebase and expert systems,
systems that store data with complex data types (for example, graphics data and audio
data), and environment- modelling systems.
•   The functions of a DBA include:
o   Schema definition. The DBA creates the original database schema by executing a
set of data definition statements in the DDL.
********** 6 **********
--- page 7 ---
o   Storage structure and access-method definition.
o   Schema and physical-organization modification. The DBA carries out changes to
the schema and physical organization to reflect the changing needs of the organization, or
to alter the physical organization to improve performance.
o   Granting of authorization for data access. By granting different types of
authorization, the database administrator can regulate which parts of the database various
users can access.
o   Routine maintenance. Examples of the database administrator’s routine
maintenance activities are:
•   Periodically backing up the database, either onto tapes or onto remote servers, to
prevent loss of data in case of disasters such as flooding.
•   Ensuring that enough free disk space is available for normal operations, and
upgrading disk space as required.
•   Monitoring jobs running on the database and ensuring that performance is not
degraded by very expensive tasks submitted by some users.
b.   Solve the following queries using relational algebra   [10]
Book(book_id, book_title, pub_year, num_pages, language, pub_date, pub_country)
Author(author_id, author_fname, author_lname)
Book_Author(author_id, book_id)
Review(book_id, review_id, review_stars, num_of_reviews)
CO- 2 ;   1.   List book titles along with their authors' names.
SO - 2;
BL-2
2. Get the first and last names of all authors who have written at least one book.
3. Find the book IDs that do not have any associated reviews.
4. determine those years in which there was at least one book that received a rating
of at least four stars.
5. Find books that have received a 5-star review.
Q5   [20]
CO- 2 ;   a.   Consider following e-commerce database:
SO - 2;   [10]
BL-2
********** 7 **********
--- page 8 ---
customers (customer_id, full_name, email, phone, city)
products (product_id   , name, unit_price stock_qty)
orders (order_id, customer_id, order_date, shipping_city, order_total)
order_items (order_id, product_id, qty, unit_price)
Write the SQL queries the following question:
i   Show each product’s total units sold and total revenue from order_items
Ans:
SELECT p. product_id, p.name, SUM (oi.qty), SUM (oi.qty * oi.unit_price) as Total
FROM products p   [3]
JOIN order_items oi ON oi. product_id = p.product_id
GROUP BY p. product_id, p.name
ORDER BY Total DESC;
ii   Show each product’s total units sold and total revenue from order_items. Return only
products with at least 2 units sold
Ans:
SELECT p. product_id, p.name, SUM (oi.qty), SUM (oi.qty * oi. unit_price)
[3]
FROM products p
JOIN order_items oi ON oi. product_id = p. product_id
GROUP BY p. product_id, p.name
HAVING SUM (oi.qty) >= 2
iii   Create the four tables with appropriate PRIMARY KEY constraints and sensible data types
Ans:
CREATE TABLE customers (
customer_id number PRIMARY KEY,
full_name VARCHAR (120) NOT NULL,
email   VARCHAR (180) UNIQUE NOT NULL,
phone   VARCHAR (20),
city   VARCHAR (80)   [4]
);
CREATE TABLE products (
product_id number PRIMARY KEY,
name   VARCHAR (25) NOT NULL,
unit_price NUMERIC (10,2) NOT NULL),
stock_qty INT NOT NULL
********** 8 **********
--- page 9 ---
);
CREATE TABLE orders (
order_id   SERIAL PRIMARY KEY,
customer_id INT NOT NULL,
order_date   date,
shipping_city VARCHAR (80),
order_total number (12,2) NOT NULL
);
CREATE TABLE order_items (
order_id INT NOT NULL,
product_id INT NOT NULL,
qty   INT NOT,
unit_price NUMERIC (10,2) NOT NULL,
PRIMARY KEY (order_id, product_id)
);
b.   Here’s a compact, exam-ready solution.
i) Dependencies on X (showing step references)
Read–Write (RW) (read first, later write on X):
• T1→T2 : (1) R by T1 before (3) W by T2
• T1→T3 : (1) R by T1 before (6) W by T3
• T2→T1 : (2) R by T2 before (5) W by T1
• T2→T3 : (2) R by T2 before (6) W by T3
• T3→T1 : (4) R by T3 before (5) W by T1
Write–Read (WR) (write first, later read on X):
• T2→T3 : (3) W by T2 before (4) R by T3
Write–Write (WW) (write first, later write on X):
• T2→T1 : (3) W by T2 before (5) W by T1
• T1→T3 : (5) W by T1 before (6) W by T3
• T2→T3 : (3) W by T2 before (6) W by T3
ii) Conflict serializability (2M)
Precedence edges from conflicts:
CO- 4 ;
SO - 2;   • T1→T2 (RW), T2→T1 (RW/WW) ⇒ cycle T1 ↔ T2   [10]
BL- 2   • T1→T3 (RW/WW) and T3→T1 (RW) ⇒ cycle T1 ↔ T3
•   (also T2→T3)
Since the graph has cycles, not conflict-serializable.
iii) View serializability (3M)
Identify read-from and final write in the given schedule:
•   (1) T1 reads X from initial value (no prior write) ⇒ T0 → T1
•   (2) T2 reads X from initial value ⇒ T0 → T2
•   (4) T3 reads X from T2’s write at (3) ⇒ T2 → T3
•   Final write on X is by T3 at (6).
For a serial schedule to be view-equivalent:
•   Both T1 and T2 must read initial X. In any serial order, only the first writing
transaction can read initial; the next reader (which also writes) would see the
prior write, not initial. Because both T1 and T2 write X, you cannot place them
serially so that both read the initial value.
Therefore, no serial schedule preserves these read-from relations and the final
write simultaneously.
Hence, not view-serializable.
********** 9 **********
--- page 10 ---
iv) View-equivalent serial schedule (2M)
None exists. Since (iii) fails, there is no serial order that is view-equivalent to the given
schedule.
Q6   [20]
a.   Here’s a clear, exam-ready 10-mark answer divided into two parts   [10]
Q1. States of a Transaction [5 Marks]
A transaction passes through several states during its execution in a DBMS.
1. States of a Transaction
State   Description
Active   The transaction is executing its read/write operations.
Partially
The transaction has executed its final statement but has not yet been p
Committed
All operations are successfully completed, and the changes are perma
Committed
database.
Failed   A fault or error occurs before the transaction commits. Changes made
All changes made by the transaction are rolled back (undone). The da
Aborted
previous consistent state.
CO- 4 ;
SO - 2;   2. State Transition Diagram
BL-3
Explanation:
•   If all steps succeed → transaction commits.
•   If any error/failure occurs → it aborts, and all partial updates are rolled back.
********** 10 **********
--- page 11 ---
Q2. Serializability [5 Marks]
Definition
A schedule is said to be serializable if its effect on the database is equivalent to some
serial execution of the same transactions, i.e., the final database state is the same as if
transactions were executed one after another without overlap.
Types of Serializability
1.   Conflict Serializability – Based on conflicting read/write operations; checked
using a precedence graph.
2. View Serializability – Based on equivalent read-from and final-write
relationships among transactions.
Importance of Serializability
•   Ensures consistency of the database in concurrent execution.
•   Prevents anomalies such as:
o   Lost update
o   Dirty read
o   Non-repeatable read
o   Inconsistent retrievals
•   Allows maximum concurrency while preserving correctness.
In short:
Serializability ensures that concurrent transactions produce the same result as some serial
order, maintaining database consistency and isolation—the core goal of concurrency
control in DBMS.
b.   "   [10]
1.   Document-Based Databases:
o   Description: Store data in JSON-like documents where each document can have
different fields.
o   Example: MongoDB, CouchDB.
o   Use Case: Storing user profiles, product catalogs.
2.   Key-Value Stores:
CO- 4 ;   o   Description: Data is stored as a collection of key-value pairs. Each key is unique
SO - 2;   and maps to a value.
BL-1
o   Example: Redis, Riak.
o   Use Case: Session management, caching.
3.   Column-Family Stores (Wide-Column Stores):
o   Description: Data is stored in columns rather than rows, optimized for queries on
large datasets.
o   Example: Apache Cassandra, HBase.
o   Use Case: Real-time analytics, large-scale data warehousing.
********** 11 **********
--- page 12 ---
4.   Graph Databases:
o   Description: Data is stored as nodes (entities) and edges (relationships), suitable
for connected data.
o   Example: Neo4j, Amazon Neptune.
o   Use Case: Social networks, recommendation engines, fraud detection
"
Q7
[20]
a   Levels of Data Abstraction
Databases hide storage details through three abstraction levels so users see only what they
need:
1. Physical Level (Internal Schema)
o What it shows: How data are stored: file organization, indexes, record
layouts, compression, page size, pointers.
o   Audience: DBMS engineers, DBAs.
o Example: B+-tree index on Emp(ID), heap file vs clustered file.
2. Logical/Conceptual Level (Conceptual Schema)
o What it shows: The global structure of the database: entities, attributes,
relationships, constraints—independent of storage.
o   Audience: Designers, application developers.
CO-1 ;   o Example: Relations EMP(EmpID, Name, DeptID) and DEPT(DeptID,
SO- 2;   DeptName) with FK DeptID.   [5]
BL-1   3. View Level (External Schemas / Views)
o What it shows: User-specific subsets or perspectives of the logical
schema; may hide sensitive or irrelevant attributes.
o   Audience: End users, applications.
o Example: View EmpPublic(EmpID, Name, DeptName) hiding salaries.
Data Independence (Why it matters)
•   Physical Data Independence: Change storage structures (e.g., add index) without
changing the conceptual schema/app code.
•   Logical Data Independence: Change conceptual schema (e.g., split a table)
without changing user views/programs.
b
What is a View?
A view is a named, stored query that presents data from one or more tables as a virtual
table.
It stores query definition, not the data (except materialized views).
Syntax (basic):
CREATE VIEW dept_emp AS
CO- 2 ;   SELECT e.EmpID, e.Name, d.DeptName
SO - 2;   FROM Employee e JOIN Department d USING (DeptID);   [5]
BL-2   Why use views?
•   Security: expose only needed columns/rows.
•   Simplicity: hide complex joins/filters.
•   Consistency: centralize business logic.
•   Logical independence: shield apps from base-table changes.
WITH CHECK OPTION ensures inserts/updates through the view still satisfy its
predicate.
********** 12 **********
--- page 13 ---
Types of Views (common classifications)
1) By data storage
•   Logical (Standard) View / Non-materialized view
o   Stores only the SELECT definition; data fetched at query time.
•   Materialized View (DB-dependent: Oracle, PostgreSQL, etc.)
o   Physically stores result set for speed; needs refresh.
o   Refresh modes: ON DEMAND (manual/scheduled) or ON COMMIT
(where supported); COMPLETE/FAST refresh options depending on
logs.
2) By query complexity
•   Simple View
o Based on one table, no aggregates, no DISTINCT, no GROUP BY/SET
ops.
o   Often updatable (subject to RDBMS rules).
o Example:
o CREATE VIEW active_customers AS
o SELECT CustID, Name, City
o FROM Customer
o WHERE Status = 'ACTIVE'
o WITH CHECK OPTION;
•   Complex View
o Based on multiple tables, joins, aggregates, DISTINCT, GROUP BY,
UNION, etc.
o   Usually read-only (non-updatable).
3) By updatability
•   Updatable View
o You can INSERT/UPDATE/DELETE through it if each row maps to
exactly one base-table row and no disqualifying clauses.
o   Typical conditions (vendor-agnostic): no DISTINCT, GROUP BY,
HAVING, aggregates, set operations, window functions; select all NOT
NULL key columns; no expressions on key columns.
•   Read-only View
o Any view violating the above (e.g., joins + aggregates). Some systems
allow INSTEAD OF triggers to make them updatable.
4) Other common terms (vendor-specific but useful)
•   Inline View: a subquery in the FROM clause used like a temporary view.
•   Partitioned/Indexed View (e.g., SQL Server): view spread over partitions or with
a persisted index for performance (subject to strict rules).
c
CO- 3;
SO - 2;   [5]
BL-3
********** 13 **********

[Text in pictures on this page, read by OCR]
How to compute X * (step-by-step)

Given R, F, and X C R:
1. Initialize: X* < X.
2. Scan FDs repeatedly:
3. Repeat Step 2 until a full pass over JF” adds no new attributes to X + (i.e, fixpoint reached).
4. Result: the final X ~ is the closure.
--- page 14 ---
d   "All the modern applications require big data, fast features development, flexible
deployment, and the older database systems not competent enough, so the MongoDB was
needed.
The primary purpose of building MongoDB is:
CO- 4 ;
SO - 2;   o   Scalability
BL-1   [5]
o   Performance
o   High Availability
o   Scaling from single server deployments to large, complex multi-site
architectures.
"
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 6dc9485420c3

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIDS_7056/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 607119565c7a

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIML_7053/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper c9375e7cfe44

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AI_7012/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 9c82336175d7

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSBS_7036/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 1d82d1b89f91

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSE_DS_7057/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 93a5cf7ec882

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CS_7055/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 62731e6646eb

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Computer_7002/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper d0f0a6406a1f

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_AI_7051/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper aba17f576539

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_Computer_7047/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper acdddd7f0cea

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_DS_7052/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 404d9fe9ef90

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_Computer_7032/Database Management Systems/ANS_Database Management Systems(702AI0C001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper eb708bdeff96

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_DS_7038/Database Management Systems/ANS_Database Management Systems(702AI0C001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (16 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/MBA Tech
(AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Database Management Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Questions 1 is compulsory.
3. Solve any four out of remaining five questions.
4. All questions carry equal marks.
5. Assume Suitable data if necessary.
6. Figure in right hand side indicates full marks
7. Answer to each new question to be started on a fresh page.
Q1
Answer briefly:   [20]
a.   Describe the concept of data abstraction in database systems. Explain the
CO-1 ;   [5]
BL-2   three levels of data abstraction.
Each level of abstraction: 1 x 3 = 3 Marks
Concept of abstraction: 1 Mark
Diagram of abstraction: 1 Mark
View Level or External Schema
This level tells the application about how the data should be shown to
the user.
Example NMIMS login and password
Conceptual Level or Logical Level
This level tells how the data is actually stored and structured.
Ans.   Example : any relational model
Physical Level or Internal Schema
As the name suggests, the Physical level tells us that where the data is
actually stored i.e. it tells the actual location of the data that is being
stored by the user.
The Database Administrators (DBA) decide that which data should be
kept at which particular disk drive, how the data has to be fragmented,
where it has to be stored etc.
They decide if the data has to be centralized or distributed.
********** 1 **********
--- page 2 ---
b.   Explain any five operators in Relational Algebra with appropriate
CO-2 ;   [5]
BL-2   symbol.
Each operator 1 Mark *5 = 5 Marks
A procedural language consisting of a set of operations that take one or
two relations as input and produce a new relation as their result.
Six basic operators
•   select: 
Ans.
•   project: 
•   union: 
•   set difference: –
•   Cartesian product: x
• rename: 
CO-3 ;   c.   Define Decomposition. Explain any three desired properties of   [5]
BL-3   decomposition with suitable examples.
Definition (1 Mark)
Decomposition is the process of dividing a relation into two or more smaller
relations such that data redundancy is minimized and data integrity is
preserved.
Desired Properties (Any Three) (3 Marks)
1. Lossless Join Property (1 Mark)
•   After decomposition, joining the relations should give the original
relation without loss of information.
• Example:
R(A, B, C), FDs: A → B
Ans.
Decompose into R1(A, B) and R2(A, C)
Natural join gives original relation → Lossless
2. Dependency Preservation (1 Mark)
•   All functional dependencies should be preserved in decomposed
relations.
• Example:
If A → B exists in original relation, it should be enforceable in one of
the decomposed tables.
3. Minimal Redundancy (1 Mark)
• Decomposition should reduce duplicate data and avoid anomalies.
********** 2 **********

[Text in pictures on this page, read by OCR]

(View Level) | View 1 View 2 View 3 View 4

i ae

(Logical Level) Conceptual Level

l

(Internal Schema) Physical Level

LE
eed
St

Levels of Data Abstraction
--- page 3 ---
Example:
Instead of storing department details repeatedly with each student, separate
tables are created.
d.   What are the various storage types in NoSQL, and what are their use
CO-4 ;
BL-2   cases?
Introduction (1 mark)
NoSQL databases use different storage models to organize data based on
specific use cases, unlike the table-based structure of relational databases.
There are four main storage types:
1. Document Stores (1 mark)
•   Store data as documents in JSON, BSON, or XML format
• Each document is self-contained with flexible schema
•   Ideal for content management and e-commerce
2. Key-Value Stores (1 mark)
•   Simplest model: unique key maps to a value
• Works like hash table or dictionary
Ans.
• Used for caching, session management, and real-time lookups
3. Column-Family Stores (1 mark)
•   Store data in columns rather than rows
• Organized into column families for efficient querying
•   Suitable for analytics, time-series data, and high write throughput
4. Graph Databases (1 mark)
•   Store data as nodes (entities) and edges (relationships)
• Optimized for connected data and relationship queries
• Used in social networks, recommendation engines, and fraud
detection
Q2   a.
Describe the different categories of Database Users. Explain the role and
[10]
CO-1;   responsibilities of a Database Administrator (DBA) in detail.
BL-2
Categories of Database Users (5 marks @ 1 mark each):
1. Naive Users - invoke pre-written application programs; e.g., bank clerk
2. Application Programmers - write application programs; choose
development tools
3. Sophisticated Users - use query languages/data analysis; no programming
needed
4. Specialized Users - write complex custom apps; e.g., CAD systems, expert
systems
Ans.   (any 4 @ 1 mark = 4 marks + 1 for clarity/examples)
Roles and Responsibilities of DBA (5 marks):
1. Schema Definition - creates original database schema using DDL (1 mark)
2. Storage structure and access-method definition (1 mark)
3. Schema and physical-organisation modification (1 mark)
4. Granting of authorisation - regulates user access (1 mark)
5. Routine maintenance - backup, disk space management, performance
monitoring (1 mark)
CO-2;   b.
BL-3   Differentiate between schema and instance of a relation.   [10]
********** 3 **********
--- page 4 ---
Consider below relations R and S
Write result of following relational algebra queries
a) πA (R) − πA (σR.B='y' (R × S))
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
Any 4 differences 1Mark each
Schema   Instance
Structure or blueprint of a relation Actual data stored in the relation
(table)   at a given time
Static (changes rarely)   Dynamic (changes frequently)
Relation name, attributes, data   Set of tuples (rows)
types, constraints
Supplier(sid, sname, city)   {(S1, Ramesh, Mumbai), (S2,
Anil, Delhi)}
Defined at design time   Represents data at a particular
moment
Modified only when design   Changes with insert, delete,
changes   update operations
Ans.
Answer[2*3=06 Marks]
a) πA (R) − πA (σR.B='y' (R × S))
A
1
3
b) R ∪ (πA,B (σC='p' (R ⋈ S)))
A B
1   x
2   y
3   x
a.   Consider the set of relations and write the SQL queries:
Q3
EMP (Emp_no, Dept_no, Emp_name, Gender, Job, MGR, Hiredate, [10]
CO-2;   Commission, Salary)
BL-3   DEPT (Dept_no, Dept_name, Location)
********** 4 **********
--- page 5 ---
1. List the emps whose salary is greater than his managers salary.
2. List the emps Whose Jobs are same as MILLER or Salary is more
than ALLEN.
3. List the details of the emps whose Salary more than the employee
BLAKE.
4. List the Enames those are starting with ‘S’ and with five
characters.
5. In dept table add one column address
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
1. SELECT e.Emp_name
FROM EMP e
JOIN EMP m ON e.MGR = m.Emp_no
WHERE e.Salary > m.Salary;
2. SELECT Emp_name
FROM EMP
WHERE Job = (SELECT Job FROM EMP WHERE Emp_name =
'MILLER')
OR Salary > (SELECT Salary FROM EMP WHERE Emp_name
Ans.   = 'ALLEN');
3. SELECT *
FROM EMP
WHERE Salary > (SELECT Salary FROM EMP WHERE Emp_name
= 'BLAKE');
4. SELECT Emp_name
FROM EMP
WHERE Emp_name LIKE 'S____';
5. ALTER TABLE DEPT
ADD Address VARCHAR(100);
CO-3;   b.   Explain Functional dependency with its formal definition. Explain first,
[10]
BL-1   second and third normal forms with example.
Definition: (2 marks)
Functional Dependency
•   Definition: 𝑋→𝑌, where X determines Y
•   Example: RollNo → Name
First Normal Form with example (2 Marks)
• Atomic attributes, no repeating groups
Ans.   •   Example: Multi-valued subjects split into rows
Second Normal Form with example (3 Marks)
• Must be in 1NF
• Remove partial dependency
•   Example: StudentName separated from composite key relation
Third Normal Form with example (3 Marks)
• Must be in 2NF
• Remove transitive dependency
•   Example: DeptName moved to separate table
********** 5 **********
--- page 6 ---
a.   A sports management system maintains information about matches,
players, and teams.
• Each Match is identified by match_id and has attributes stadium
and date.
• Each Player has attributes name and age. Additionally,
season_score is a derived attribute.
• Each Team has attribute name, and ranking is a derived attribute.
The system maintains the following relationships:
• A player plays in matches. The relationship played stores the
Q4   attribute score representing the player’s score in a particular
CO-1;   match.   [10]
• A team participates in matches through the relationship
BL-2
team_played, which has attributes score and result.
• A player belongs to a team through the relationship player_of.
Each player belongs to one team, while a team can have many
players.
Draw the E-R diagram for the above system and clearly show:
i.   Entities and their attributes with attribute types
ii.   Primary keys
iii.   Relationship sets with attributes
iv.   Cardinality constraints
v.   Mention any assumptions made.
1. Identification of Entities (3 Marks)
• Match → 1 mark
•   Player → 1 mark
• Team → 1 mark
2. Attributes & Primary Keys (2 Marks)
•   Correct attributes for all entities → 1 mark
o Match: match_id, stadium, date
Ans.   o   Player: name, age
o Team: name
•   Primary keys correctly identified → 1 mark
o match_id (Match)
o (assumption: player name or player_id)
o team name or team_id
3. Derived Attributes (1 Mark)
•   season_score (Player) → 0.5 mark
•   ranking (Team) → 0.5 mark
********** 6 **********
--- page 7 ---
4. Relationships with Attributes (2 Marks)
•   played (Match–Player) with attribute score → 1 mark
• team_played (Match–Team) with attributes score, result → 1 mark
5. Cardinality Constraints (1.5 Marks)
• Match–Player → M:N → 0.5 mark
• Team–Match → M:N → 0.5 mark
• Player–Team → 1:M → 0.5 mark
6. Neatness, Notation & Assumptions (0.5 Mark)
•   Proper ER notation (rectangles, diamonds, ovals) → 0.25 mark
•   At least one valid assumption → 0.25 mark
b.   Explain all type of outer joins. Apply outer join operations on the
following relations and show the resulting outputs.
CO-2;
[10]
BL-2
Outer Joins [4 Marks]
LEFT OUTER JOIN
RIGHT OUTER JOIN
Ans.   FULL OUTER JOIN
•   LEFT (OUTER) JOIN: Returns all rows from the left table, and
only the matched rows from the right table
********** 7 **********
--- page 8 ---
•   RIGHT (OUTER) JOIN: Returns all rows from the right table,
and only the matched rows from the left table
•   FULL (OUTER) JOIN: Returns all rows when there is a match
in either the left or right table.
LEFT OUTER JOIN (PATIENT ⟕ DOCTOR) [2Marks]
PI PatientNam DoctorI DoctorNam
D e   D   e
P1 Anil   D1   Dr. Mehta
P2 Sunita   D2   Dr. Sharma
P3 Ravi   D4   NULL
RIGHT OUTER JOIN (PATIENT ⟖ DOCTOR) [2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
NUL
NULL   D3   Dr. Khan
L
FULL OUTER JOIN (PATIENT ⟗ DOCTOR)[2Marks]
PatientNam DoctorI DoctorNam
PID
e   D   e
P1   Anil   D1   Dr. Mehta
P2   Sunita   D2   Dr. Sharma
P3   Ravi   D4   NULL
NUL
NULL   D3   Dr. Khan
L
a.   Explain transaction states with suitable diagram.
A schedule S involving T1, T2, T3 on data items P and Q:
T1   T2   T3
R(P)
R(Q)
Q5
W(P)
CO-4;   [10]
W(Q)
BL-3
R(P)
W(P)
Perform the following task:
i. Construct the precedence graph for the given schedule.
ii. Determine whether the schedule is conflict serializable or not
********** 8 **********
--- page 9 ---
iii. If it is serializable, write the equivalent serial order of the
transactions.
(2 marks)
Explain each Properties with proper examples (3 marks)
➢   Active: the initial state; the transaction stays in this state
while it is executing
➢ Partially committed: after the final statement has been
executed
➢ Failed: after the discovery that normal execution can no
longer proceed
➢ Aborted: after the transaction has been rolled back and the
database has been restored to its state prior to the start of
Ans.
the transaction
➢ Committed: after successful completion
•   Conflicts: 2 Marks
o T1 → T3 (W(P) before R(P))
o T1 → T3 (W(P) before W(P))
o No reverse dependency
• Graph: No cycle (DAG) 2 Marks
• Conclusion:
Conflict Serializable
Serial order: T1 → T3 → T2 (T2 independent) 1 Marks
b.   A bank maintains:
CO-3;   TRANSACTION(TransactionID, TransDate, AccountNo, AccountType, [10]
BL-3   CustomerID, CustomerName, CustomerAddress, BranchCode,
BranchName, BranchCity, Amount, TransType, Balance)
********** 9 **********
--- page 10 ---
Given FDs:
e TransactionID >

TransDate, AccountNo, Amount, TransT ype, Balance
e AccountNo — AccountType, CustomerID, BranchCode
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

1. Prove that TransactionID is the primary key using closure.

2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step.

3. Check if 3NF relations are also in BCNF.

4. Check the decomposition is lossless or lossy.

Ans.

1. Prove that TransactionID is the primary key using closure. (2
marks)
2. Show the progression from 1NF — 2NF — 3NF with schemas at
each step. (4 marks)
3. Check if 3NF relations are also in BCNF. (2 marks)
4. Check the decomposition is lossless or lossy and justify your
answer. (2 marks)
1) Prove that TransactionID is the Primary Key (using closure)
Compute:
TransactionID*

Start with:
{TransactionID}

Apply FDs:
e TransactionID >
TransDate, AccountNo, Amount, TransT ype, Balance
Add:
{TransDate AccountNo Amount’ TransT ype Balance}

Now:
{TransactionID: TransDate AccountNo’ Amount’ TransT ype Balance

e AccountNo — AccountType, CustomerID, BranchCode
Add:
{AccountT ype CustomerID: BranchCode}

e CustomerID > CustomerName, CustomerAddress
Add:
{CustomerName: CustomerAddress}

e BranchCode > BranchName, BranchCity

Add:
{BranchName BranchCity}

Final Closure:

FRR ICR 7 OI HOH
--- page 11 ---
TransactionID*
= {TransactionID, TransDate, AccountNo, AccountT ype, CustomerID

J Contains all attributes

Conclusion:
e TransactionID is a super key
e No smaller subset exists > Primary Key

2) Normalization: UNF — 1NF — 2NF — 3NF

(a) UNF (Unnormalized Form)

Single large relation:

TRANSACTION

(TransactionID: TransDate AccountNo AccountT ype: CustomerID: C

(b) 1NF (Atomic attributes)
All attributes are already atomic — No structural change

(c) 2NF
Condition:
e Remove partial dependencies (on part of a composite key)
Here:
e Primary key = TransactionID (single attribute)
V No partial dependency possible

So:
INF = 2NF

(d) 3NF
Remove transitive dependencies
Identify:
e TransactionID > AccountNo
e AccountNo — CustomerID, BranchCode
— Transitive dependency
e CustomerID > CustomerName, CustomerAddress
e BranchCode > BranchName, BranchCity

Decompose:
1. TRANSACTION
(TransactionID TransDate AccountNo’ Amount TransT ype Balance

2. ACCOUNT
(AccountNo: AccountT ype CustomerID BranchCode)

3. CUSTOMER
(CustomerID: CustomerName Customer Address)

4. BRANCH
(BranchCode: BranchName: BranchCity)

FRI ICR 7 FI OH
--- page 12 ---
3) Check for BCNF
BCNF condition:
For every FD 𝑋→𝑌, X must be a superkey
Check each relation:
(i) TRANSACTION
• 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝐼𝐷→⋯
✔ LHS is key → BCNF satisfied
(ii) ACCOUNT
• 𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo is key → BCNF satisfied
(iii) CUSTOMER
• 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ Key → BCNF satisfied
(iv) BRANCH
• 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ Key → BCNF satisfied
Conclusion:
✔ All 3NF relations are also in BCNF
Lossless Join Criterion
A decomposition is lossless if for any decomposition 𝑅→𝑅1, 𝑅2:
𝑅1 ∩𝑅2 →𝑅1or𝑅2
(i.e., the common attributes functionally determine at least one relation)
Stepwise Verification
1) TRANSACTION ⨝ ACCOUNT
• Common attribute: AccountNo
• From FD:
𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑁𝑜→𝐴𝑐𝑐𝑜𝑢𝑛𝑡𝑇𝑦𝑝𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒
✔ AccountNo determines all attributes of ACCOUNT
⇒ Lossless join
2) ACCOUNT ⨝ CUSTOMER
• Common attribute: CustomerID
• From FD:
𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐼𝐷→𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝑁𝑎𝑚𝑒, 𝐶𝑢𝑠𝑡𝑜𝑚𝑒𝑟𝐴𝑑𝑑𝑟𝑒𝑠𝑠
✔ CustomerID determines all attributes of CUSTOMER
⇒ Lossless join
3) ACCOUNT ⨝ BRANCH
• Common attribute: BranchCode
• From FD:
𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑜𝑑𝑒→𝐵𝑟𝑎𝑛𝑐ℎ𝑁𝑎𝑚𝑒, 𝐵𝑟𝑎𝑛𝑐ℎ𝐶𝑖𝑡𝑦
✔ BranchCode determines all attributes of BRANCH
⇒ Lossless join
********** 12 **********
--- page 13 ---
Final Conclusion
Since each pairwise join satisfies the lossless condition, the overall
decomposition is:
Lossless Join Decomposition
a.
A transportation system manages vehicles, drivers, routes, and trips. Each
vehicle has VehicleID, Type, Capacity, and RegistrationNumber.
Vehicles are assigned to routes. Each route has RouteID, Source,
Destination,   and   Distance.   Drivers   have   DriverID, Name,
LicenseNumber, and Experience. A driver can drive multiple vehicles
over time. Each trip is identified by TripID and includes Date, StartTime,
and EndTime. A trip is associated with one vehicle, one driver, and one
Q6   route. Passengers can book trips. Each passenger has PassengerID, Name,
and Contact. A booking includes SeatNumber and Fare. Additionally,
CO-1;   vehicles are categorized into Electric and Fuel-based. Electric vehicles [10]
BL-3   have BatteryCapacity, while fuel-based vehicles have FuelType.
Draw an ER Diagram and clearly show:
i.   Entities and Primary keys
ii.   Types of attributes
iii.   Cardinality ratios
iv.   Participation constraints
Entities and Primary keys – 2 Marks
Types of attributes – 2 Marks
Cardinality ratios- 3 Marks
Ans.   Participation constraints – 2 Marks
Generalization/Specialization – 1 Mark
********** 13 **********
--- page 14 ---
CO-4;   b.   Consider two transactions executing concurrently on the same data
[10]
BL-2   item. Explain the possible concurrency problems that may arise.
When two or more transactions execute concurrently on the same data
item, several concurrency problems may arise due to improper
coordination. With example 2 Marks
Concurrency Problems (each of 2 Marks)
1. Lost Update Problem
o Occurs when two transactions update the same data item
and one update overwrites the other.
o Example:
Ans.
T1 and T2 read balance ₹100 → T1 updates to ₹150 → T2
updates to ₹130 → final value incorrect
2. Dirty Read Problem (Uncommitted Data)
o A transaction reads data modified by another transaction
that has not yet committed.
o Example:
T1 updates X = 200 but rolls back → T2 already read 200
→ inconsistency
********** 14 **********
--- page 15 ---
3. Unrepeatable Read Problem
o A transaction reads the same data twice and gets different
values due to another transaction’s update.
o Example:
T1 reads X = 100 → T2 updates X to 150 → T1 reads again
→ gets 150
4. Phantom Read Problem
o Occurs when new records are inserted or deleted by
another transaction between two reads.
o Example:
T1 retrieves records → T2 inserts new record → T1
retrieves again → extra record appears
a.   Explain how to implement NoSQL using MongoDB. Describe the
Q7
process of creating and managing databases and collections, inserting
CO-4;   [10]
documents, and finding documents using MongoDB shell with
BL-2
examples.
Introduction to MongoDB (2 marks)
• Document-oriented NoSQL database
•   Stores data in BSON (Binary JSON) format
•   Flexible schema, supports embedded documents and arrays
Creating and Managing Databases (2 marks)
•   use <database_name> - switch/create database
• show dbs - view all databases
• db - check current database
•   db.dropDatabase() - drop database
Creating and Managing Collections (2 marks)
•   db.createCollection("collection_name") - create collection
•   Collections created implicitly on first insert
• show collections - view collections
Ans.   •   db.collection_name.drop() - drop collection
Inserting Documents (2 marks)
•   db.collection.insertOne({field: value}) - insert single document
•   db.collection.insertMany([{}, {}]) - insert multiple documents
•   Example: db.students.insertOne({student_name: "Anish", dept: "CS",
cgpa: 9.1, year: 3})
Finding Documents (2 marks)
•   db.collection.find() or db.collection.find({filter}) - retrieve documents
•   db.collection.findOne({filter}) - retrieve single document
• Can use with comparison operators ($gt, $lt, $in, etc.)
•   Supports projection to show specific fields
• Can chain with .sort() and .limit() for ordering and limiting results
********** 15 **********
--- page 16 ---
b.   Consider the set of relations and answer the following SQL queries:
Hotel(hotel_id, name, city)
Guest(guest_id, name, phone)
CO-2;   Booking(booking_id, guest_id, hotel_id, checkin_date, checkout_date)
[10]
BL-3
i.   Delete bookings where checkout_date is NULL
ii.   Display hotels having more than 5 bookings
iii.   Create a view for hotels in ‘Mumbai’
iv.   Find guest names and their total bookings
v.   Find hotels whose name starts with ‘T’
Give 2 marks for each correct SQL query. Multiple correct answers are
possible; evaluate based on logical correctness and proper SQL syntax.
i. DELETE FROM Booking WHERE checkout_date IS NULL;
ii. SELECT hotel_id
FROM Booking
GROUP BY hotel_id
HAVING COUNT(*) > 5;
Ans.
iii. CREATE VIEW mumbai_hotels AS
SELECT * FROM Hotel WHERE city = 'Mumbai';
iv. SELECT g.name, COUNT(b.booking_id)
FROM Guest g
LEFT JOIN Booking b ON g.guest_id = b.guest_id
GROUP BY g.name;
v. SELECT name FROM Hotel WHERE name LIKE 'T%';
********** 16 **********
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 478f642be37b

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Database Management Systems/ANS_Database Management Systems(703AI0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25 Nov 2024
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester I(Exam Year: 2024-2025)
Subject: Database Management Systems
Date: 25 Nov 2024   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data (if Required) and mention assumed data in answers.
Section A: Attempt All Questions (Each Question Carry 5M)
Question 1
CO 1;   A.   Different types of users (3M)   5M
SO6;   Database Administrators (DBAs)
BL2   Application Programmers
End Users
Database Designers
How their requirements differ (2M)
Database Administrators (DBAs): Focus on managing and maintaining the
database system, ensuring data integrity, security, and performance.
Application Programmers: Require robust APIs and tools for integration,
the ability to write queries, and access to schema design.
End Users: Seek a user-friendly interface for querying data and generating
reports.
CO 1;   B.   Entity-Relationship Diagram (ERD) – (2M)   5M
SO6;   Explain its components – (3M)
BL2   Entity
Attributes
Relationship
CO 2;   C.   Purpose of domain constraints – Any 3 points from below   5M
SO1;   Data Integrity
BL4   Enforcement of Business Rules
Consistency
Error Prevention
Simplification of Queries
Improved Performance
********** 1 **********
--- page 2 ---
CO 4;   D. Any 3 Characteristics of NoSQL Databases (Each carry 2M)   5M
SO7;   Schema Flexibility:
BL4   Horizontal Scalability:
High Performance:
Variety of Data Models:
Distributed Architecture:
Eventual Consistency:
Section B: Attempt Any Four Questions from Questions 2 to 7 (Each Question Carry 20M)
Question 2
CO 3;   A. What is functional Dependency (FD) – 2M   10M
SO1;   Properties of Functional dependencies (2 Marks Each)
BL4   Reflexivity:
Augmentation:
Transitivity:
Union:
Decomposition:
Pseudotransitivity:
CO 1;   B.   1. Identify the key entities and their attributes. (3M)   10M
SO6;   Department (e.g., Cardiology, Neurology, Orthopedics)
BL5   Doctor (Doctor ID, Name, Specialisation, Contact Information)
Patient (Patient ID, Name, Address, Phone Number )
Visit (Visit ID, Date, Diagnosis, Treatment Details)
Insurance Provider (Provider ID, Policy Information, Provider Name)
2. Specify the relationships between these entities, including cardinality
and participation constraints. (3M)
Department - Doctor (One department can have zero or many doctors.)
Patient - Visit (One patient can have zero or many visits.)
Patient - Insurance Provider (One patient can have zero or many insurance
providers.)
Doctor - Visit (One doctor can conduct zero or many visits.)
Department – Patient (One department can serve zero or many patients.)
3. Correct design of Entity-Relationship diagram. (4M)
Question 3
CO 2;   A.   Concept of SQL Joins – 2M   10M
SO1;   Any 2 Types of joins, including their syntax and use cases.- (8M)
BL4   Inner Join
********** 2 **********
--- page 3 ---
Outer Join
Natural Join
CO 4;   B.   Conflict serializability – 4M   10M
SO6;   Definition and one example
BL3   Check whether the below-given schedule is serialisable (6M)
R1(B) , W2(A) , R3(A) , W1(B) , W3(A)
A schedule is serialisable if the conflict graph is acyclic. In our graph
T2 → T3: This does not form a cycle, as no edges are returning to T2 from
T3 or a loop involving T1.
Question 4
CO 3;   A. What is decomposition – 2M   10M
SO1;   Give properties of decomposition - 4M
BL2   Lossless Join
Dependency Preservation
No Repetition
Convert Relation R(A, B, C, D, E, F, G) – 4M
R1 (A, B, C, D)
R2 (E, F, G)
R3 (D, E)
CO 2;   B.   Relational algebra queries   10M
SO1;   1. Name of Female Employees with Salary above 70000 in IT (3M)
BL6   2. Name of all employees Except HR department employees (4M)
3. Male Employees working in Mumbai. (3M)
Question 5
CO 4;   A.   Explain any 5 Steps – Each carry 2M   10M
SO7;   Start the MongoDB Server
BL2   Open the MongoDB Shell
Show Databases
Create a New Database
Drop a Database
Create a Collection
CO 2;   B.   Consider data in Q.4 (B) and write SQL JOIN queries for given questions,   10M
SO1;   1. find the average salary of employees in each department (3M)
BL6   SELECT d.DepartmentName, AVG(e.Salary) AS AverageSalary
FROM Employees e
JOIN Departments d ON e.DeptID = d.DeptID
GROUP BY d.DepartmentName;
2. Show the total salary of employees assigned to each subject.
SELECT s.SubjectName, SUM(e.Salary) AS TotalSalary
FROM Employees e
********** 3 **********
--- page 4 ---
JOIN Subjects s ON e.SubjectID = s.SubjectID
GROUP BY s.SubjectName;
3. List all employees and the subjects to which they are assigned.
SELECT e.Name, s.SubjectName
FROM Employees e
LEFT JOIN Subjects s ON e.SubjectID = s.SubjectID;
4. List each employee and the corresponding subjects they teach.
SELECT e.Name AS EmployeeName, s.SubjectName
FROM Employees e
JOIN Subjects s ON e.SubjectID = s.SubjectID;
Question 6
CO 4;   A. What is the transaction – 2M   10M
SO6;   Analyse the Different States of a Transaction – 4M
BL4   Active
Partially committed
Committed
Failed
Abort
Significance to Each State – 4M
CO 2;   B.   Consider data in Q.4 (B) and write SQL Sub Queries for given questions,   10M
SO1;   1. list the names and salaries of employees who have a salary higher
BL6   than the average salary of all employees.
SELECT Name, Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
2. Find all departments that have more than five employees.
SELECT DepartmentName
FROM Departments
WHERE DeptID IN (SELECT DeptID FROM Employees GROUP BY
DeptID HAVING COUNT(*) > 5);
3. Find the names of employees who are not assigned to any subjects.
SELECT Name
FROM Employees
WHERE SubjectID IS NULL;
4. Find the names and salaries of the highest-paid employees in each
department.
SELECT Name
FROM Employees
WHERE EmployeeID NOT IN (SELECT DISTINCT EmployeeID
FROM Employees WHERE SubjectID IS NOT NULL);
********** 4 **********
--- page 5 ---
Question 7
CO 1;   A.   Purpose of database systems – (1M)   5M
SO6;   Four advantages that database systems (4M)
BL2
CO 2;   B.   Keys interact in a multi-table database example – (3M)   5M
SO2;   Referential integrity – 2M
BL4
CO 3;   C. Any 3 Problems – Each has (2+2+1) marks   5M
SO1;
BL4
CO 1;   D.   The steps of the ER model are reduced to a relational schema   5M
SO6;   1. ER Entity to Table (1M)
BL2   2. ER attributes to columns in the table (2M)
3. Relations into a table (2M)
(Merge Key approach, FK approach, Cross table approach)
********** 5 **********
````

## 2024-25 · Final-Exam · Sem 4 · Answer key · paper 12b4ed199813

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_04/Final-Exam/BTech_CSE_DS_7011/Database Management System/ANS_Database Management System(702CO0C040)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2025
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester IV(Exam Year: 2024-2025)
Subject: Database Management System
Date: 08 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data whenever required (Please mentions such data in answer)
5. Question 1 is compulsory (20 Marks), Attempt any 4 Questions from Question 2 to 7 (80 Marks)
Section A: Attempt All Questions (Each Question Carry 5M)
Question 1
CO1;   A.   Different types of users (3M)   5M
SO1;   Database Administrators (DBAs)
BL2
Application Programmers
End Users
Database Designers
How their requirements differ (2M)
Database Administrators (DBAs): Focus on managing and maintaining the
database system, ensuring data integrity, security, and performance.
Application Programmers: Require robust APIs and tools for integration,
the ability to write queries, and access to schema design.
End Users: Seek a user-friendly interface for querying data and generating
reports.
CO2;   B.   Purpose of domain constraints – Any 3 points from below   5M
SO6;
BL2   Data Integrity
Enforcement of Business Rules
Consistency
Error Prevention
Simplification of Queries
Improved Performance
CO3;   C.   Entity-Relationship Diagram (ERD) – (2M)   5M
SO1;
BL4   Explain its components – (3M)
Entity
Attributes
********** 1 **********
--- page 2 ---
Relationship
CO4;   D.   Definition of ROLLUP and CUBE (2 Marks)   5M
SO7;
BL2   SQL Example for ROLLUP (1 Mark)
SQL Example for CUBE (1 Mark)
Enhancements and benefits in OLAP queries (1 Mark)
Section B: Attempt Any Four Questions from Questions 2 to 7 (Each Question Carry 20M)
Question 2
CO4;   A.   Indexes in a database improve query performance by enabling faster data   10M
SO1;
retrieval. They reduce the number of rows scanned and enhance search
BL4
efficiency. The main types of indexes include:
Primary Index – Automatically created for primary keys; helps in faster
access.
Unique Index – Ensures that all values in a column are distinct.
Clustered Index – Sorts data physically based on key values; only one per
table.
Non-Clustered Index – Stores a separate structure pointing to actual data;
allows multiple per table.
SQL Example
CREATE UNIQUE INDEX idx_unique_email
ON Customers (Email);
Explanation of Indexing & Its Benefits – 2 Marks
Listing Different Types of Indexes – 2 Marks
Correct SQL Query for Unique Index – 1 Mark
CO2;   B.   Relational algebra queries   10M
SO6;
BL5   1. Name of Female Employees with Salary above 70000 in IT (3M)
2. Name of all employees Except HR department employees (4M)
3. Male Employees working in Mumbai. (3M)
Question 3
CO2;   A.   Concept of SQL Joins – 2M   10M
SO1;
BL4   Any 2 Types of joins, including their syntax and use cases.- (8M)
Inner Join
Outer Join
Natural Join
CO4;   B.   What is decomposition – 2M   10M
SO6;
BL5   Give properties of decomposition - 4M
Lossless Join
********** 2 **********
--- page 3 ---
Dependency Preservation
No Repetition
Convert Relation R(A, B, C, D, E, F, G) – 4M
R1 (A, B, C, D)
R2 (E, F, G)
R3 (D, E)
Question 4
CO3;   A.   Identify the key entities and their attributes. (3M)   10M
SO6;
BL6   Department (e.g., Cardiology, Neurology, Orthopedics)
Doctor (Doctor ID, Name, Specialisation, Contact Information)
Patient (Patient ID, Name, Address, Phone Number )
Visit (Visit ID, Date, Diagnosis, Treatment Details)
Insurance Provider (Provider ID, Policy Information, Provider Name)
Specify the relationships between these entities, including cardinality
and participation constraints. (3M)
Department - Doctor (One department can have zero or many doctors.)
Patient - Visit (One patient can have zero or many visits.)
Patient - Insurance Provider (One patient can have zero or many insurance
providers.)
Doctor - Visit (One doctor can conduct zero or many visits.)
Department – Patient (One department can serve zero or many patients.)
Correct design of Entity-Relationship diagram. (4M)
CO2;   B.   1. Create the Books table with the specified columns and set BookID as the   10M
SO6;
primary key. (3 Marks)
BL6
CREATE TABLE Books (
BookID INT PRIMARY KEY,
Title VARCHAR(255),
Author VARCHAR(100),
Genre VARCHAR(50),
Price DECIMAL(8,2),
Stock INT
);
2. Retrieve the details of all orders placed in the last 30 days, including
customer names and book titles. (3 Marks)
SELECT
Orders.OrderID,
Customers.Name AS CustomerName,
Books.Title AS BookTitle, Orders.Quantity,
Orders.OrderDate
FROM Orders
********** 3 **********
--- page 4 ---
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
JOIN Books ON Orders.BookID = Books.BookID
WHERE Orders.OrderDate >= CURDATE() - INTERVAL 30 DAY;
3. List customer names and their total number of orders, sorted by the
highest number of orders first. (4 Marks)
SELECT Customers.Name AS CustomerName,
COUNT(Orders.OrderID) AS TotalOrders
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.Name
ORDER BY TotalOrders DESC;
Question 5
CO 4;   A. A Data Warehouse (DW) is a centralized repository used for reporting and   10M
SO7;
data analysis. It is designed to support decision-making processes by
BL2
integrating data from multiple sources. The key components of a data
warehouse include:
Data Sources (1 Mark)
Extracts data from operational databases, external sources, or legacy
systems.ETL (Extract, Transform, Load) Process (2 Marks)
Extract: Retrieves raw data from multiple sources.
Transform: Cleans, formats, and integrates data.
Load: Stores processed data in the warehouse.
Data Warehouse Database (1 Mark)
A central storage unit that organizes data in a structured way, often using
OLAP (Online Analytical Processing).
Metadata (1 Mark)
Stores information about data (e.g., source, structure, and transformations).
Helps in efficient data retrieval and management.
OLAP Engine (2 Marks)
Enables multidimensional analysis, allowing users to view data from
different perspectives (e.g., drill-down, roll-up).
Data Marts (1 Mark)
Subsets of a data warehouse focused on specific business areas (e.g., sales,
finance).
Business Intelligence (BI) & Reporting Tools (2 Marks)
Supports decision-making by providing dashboards, visualization, and
predictive analytics.
Support for Decision Support Systems (DSS) (2 Marks)
Provides historical and real-time data for trend analysis.
Enhances business intelligence through OLAP and data mining.
********** 4 **********
--- page 5 ---
Helps in forecasting and strategic planning by identifying patterns.
CO2;   B.   Consider data in Q.2 (B) and write SQL Queries for given questions,   10M
SO7;
BL6   1. find the average salary of employees in each department (3M)
SELECT d.DepartmentName, AVG(e.Salary) AS AverageSalary
FROM Employees e
JOIN Departments d ON e.DeptID = d.DeptID
GROUP BY d.DepartmentName;
2. Show the total salary of employees assigned to each subject.
SELECT s.SubjectName, SUM(e.Salary) AS TotalSalary
FROM Employees e
JOIN Subjects s ON e.SubjectID = s.SubjectID
GROUP BY s.SubjectName;
1. Find the names of employees who are not assigned to any subjects.
SELECT Name
FROM Employees
WHERE SubjectID IS NULL;
2. Find the names and salaries of the highest-paid employees in each
department.
SELECT Name
FROM Employees
WHERE EmployeeID NOT IN (SELECT DISTINCT EmployeeID
FROM Employees WHERE SubjectID IS NOT NULL);
Question 6
CO4;   A.   What is functional Dependency (FD) – 2M   10M
SO6;
BL4   Properties of Functional dependencies (2 Marks Each)
Reflexivity:
Augmentation:
Transitivity:
Union:
Decomposition:
Pseudotransitivity:
CO4;   B.   Conflict serializability – 4M   10M
SO6;
BL6   Definition and one example
Check whether the below-given schedule is serialisable (6M)
R1(B) , W2(A) , R3(A) , W1(B) , W3(A)
A schedule is serialisable if the conflict graph is acyclic. In our graph
T2 → T3: This does not form a cycle, as no edges are returning to T2 from
T3 or a loop involving T1.
Question 7
CO1;   Purpose of database systems – (1M)   5M
SO2;   A.
BL2   Four advantages that database systems (4M)
********** 5 **********
--- page 6 ---
CO2;   Introduction to SQL Set Operators (2 Marks) – Defining set operators   5M
SO1;   with a basic explanation.
BL4
Functionality Explanation (4 Marks) – Discussing rules and behaviour of
set operators.
Example with Explanation (4 Marks) – Provide a clear SQL example and
explain its output.
Introduction to SQL Set Operators (2 Marks)
SQL Set Operators are used to combine results from multiple SELECT
queries into a single result set. These operators work similarly to
mathematical set operations and ensure that the final result follows specific
rules.
The main SQL set operators are:
UNION – Combines results of two queries, removing duplicates.
B.
UNION ALL – Similar to UNION but includes duplicates.
INTERSECT – Returns only the common records from both queries.
EXCEPT (or MINUS in some databases)
Functionality of SQL Set Operators (4 Marks)
All queries used in a set operation must have the same number of columns.
Corresponding columns must have compatible data types. The default
behaviour of UNION and INTERSECT is to remove duplicates unless
explicitly stated otherwise (e.g., UNION ALL).
Example of SQL Set Operator (UNION Example) (4 Marks)
SELECT CustomerID, Name, City FROM Customers_US
UNION
SELECT CustomerID, Name, City FROM Customers_UK;
CO3;   The steps of the ER model are reduced to a relational schema   5M
SO1;   1. ER Entity to Table (1M)
BL4
C.   2. ER attributes to columns in the table (2M)
3. Relations into a table (2M)
(Merge Key approach, FK approach, Cross table approach)
CO2;   5M
SO6;   D. Any 3 Problems – Each has (2+2+1) marks
BL2
********** 6 **********
````

## 2024-25 · Final-Exam · Sem 3 · Answer key · paper 0847fa8bb705

- Departments: Cyber Security, Information Technology
- Programmes: BTech CyberSecurity 7010, BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CyberSecurity_7010/Database Management Systems/ANS_Database Management Systems(702AI0C027)_2025-2026.pdf` (+1 identical copies)
- Text: text (12 pages)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025
Program/s: ___BTech IT/MBATech IT/BTech Cyber /BTI IT___   Year: 2 Semester: V/IX
Stream/s : Information Technology
Subject: ___DBMS   Time: _3__ hrs (______to_______)
Date:   /   / 2025   No. of Pages:__3___
Marks: __100_______
Final Examination/Re-Examination ( Re-exam year)
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Figures in brackets on the right hand side indicate full marks.
6) Assume Suitable data if necessary.
SET 1- synoptic
Q1   Answer the following questions   [20]
CO- 1;   a   What are data models? Explain the Relational Model.   [5]
SO- 2;   1. Definition of Data Models (2 Marks)
BL- 1
A data model   is a conceptual framework that describes how data are structured,
stored, and manipulated in a database system.
It defines the   logical structure   of the database — the relationships among data, the
constraints, and the operations that can be performed.
Common types include:
•   Hierarchical Model
•   Network Model
•   Relational Model
•   Object Oriented Model
2. Relational Model (3 Marks)
The Relational Model organizes data into relations (tables) consisting of rows and
columns .
Each table (relation) represents an entity , each row (tuple) represents a record ,
and each column (attribute) represents a data field .
Every relation has a Primary Key that uniquely identifies each tuple.
Foreign Keys are used to establish relationships between tables.
Data are manipulated using Relational Algebra and the SQL language for operations
like selection, projection, join, and union.
--- page 2 ---
Example:
| StudentID | Name   | Branch |
|   |   |   |
| S101   | Riya   | IT   |
| S102   | Arjun | CS   |
Here, StudentID → Primary Key; the table “Student” represents the Student entity .
CO- 2;   b   1. Features of a Good Database Design (4 Marks)   [5]
SO - 2;
BL- 2   Data Integrity and Consistency:
Each piece of data is stored only once (no redundancy), ensuring consistency.
Example: Customer details stored in one CUSTOMER table, not repeated in every ORDER
record.
Minimal Data Redundancy:
Redundant data causes update anomalies and wasted storage.
Example: Instead of repeating department names for every employee, use a separate
DEPARTMENT table with a foreign key reference.
Proper Use of Normalization:
Splitting large tables into smaller ones to remove partial and transitive dependencies (1NF–
3NF).
Example:   Separating   EMPLOYEE(EmpID,   EmpName,   DeptID)   and
DEPARTMENT(DeptID, DeptName).
Clear Entity–Relationship Mapping:
Logical relationships (1:1, 1:N, M:N) must be clearly defined using primary and foreign
keys.
Example: One‐to‐many between CUSTOMER and ORDER.
Scalability and Performance:
Well-designed indexes and relationships support fast queries and future data growth.
Example: Indexing OrderID in ORDERS table speeds up retrieval.
Remove Insert Update Anomalies
2. Conclusion (1 Mark)
A good database design is normalized, non-redundant, and supports data integrity, leading
to efficient storage, accurate information, and simplified maintenance.
CO- 3 ;   c   (a) Superkeys: [2Marks]   [5]
SO - 2;   {RollNo}, {Email}, {AadhaarNo}, {RollNo, Name}, {Email, Phone}, etc.
BL- 2   (b) Candidate Keys: [2Marks] - minimal keys
{RollNo}, {Email}, {AadhaarNo}
(c) Primary Key:   - only one to be written from candidate keys
--- page 3 ---
RollNo —unique. [1Marks]
CO- 4 ;   d   What is the significance of CAP theorem in NOSQL   [5]
SO - 2;   The CAP Theorem is a fundamental principle in NoSQL databases that describes the trade-
BL-1   offs among three key properties:
1.   Consistency (C): Every read receives the most recent write or an error.
2.   Availability (A): Every request receives a response, regardless of the state of the
data.
3.   Partition Tolerance (P): The system continues to operate even if network partitions
or communication failures occur.
Significance in NoSQL:
•   NoSQL databases are often distributed systems. The CAP theorem explains that
it is impossible to achieve all three properties simultaneously; a database can only fully
guarantee two out of three.
•   For example:
o   MongoDB prioritizes Consistency + Partition Tolerance (CP) by default.
o   Cassandra prioritizes Availability + Partition Tolerance (AP).
•   This helps developers choose the right database and configure it according to
application needs, balancing consistency, availability, and fault tolerance.
"
Q2   [20]
CO- 1 ;   a   [10]
SO - 2;   All Entities drawn – 2M
BL-2   All attributes - 2M
Relationships – 2M
Cardinality – 2M
Participation – 2M
CO- 2 ;   b   Consider following movie database:   [10]
SO - 2;
BL- 2   users (user_id, full_name, city, contact_no)
restaurants (restaurant_id, name, address, price level, is active)
dishes (dish_id, restaurant, name, price, is_veg, is spicy)
ratings (user_id, dish_id, rating, rated_at, feedback)
Write the SQL queries the following question:
--- page 4 ---
i   Add a new column “email” to users table   [2]
Ans:
ALTER TABLE users
ADD COLUMN email VARCHAR (40);
ii   Modify table dishes to enforce business rules “dishes.price must be > 0.” using CHECK   [2]
constraints
Ans:
ALTER TABLE dishes
ADD CONSTRAINT chk_price
CHECK (price > 0);
iii   Select all veg, not-spicy dishes with price <= 250 from active restaurants.   [2]
Ans:
SELECT d.name AS dish, r.name AS restaurant, d.price
FROM dishes d, restaurants r
Where r. restaurant_id = d. restaurant_id and r.is_active = ‘yes’ AND d.is_veg = ‘yes’
AND d.is_spicy is ‘No’ and d. price <= 250
iv   Show each restaurant’s average rating and number of ratings but return only those with at   [2]
least 2 ratings and an average ≥ 4.0.
Ans:
SELECT r.name AS restaurant, ROUND (AVG (rt. rating), 2) AS avg_rating,
COUNT (rt. rating) AS rating_count
FROM restaurants r, dishes d, ratings rt where d. restaurant_id = r. restaurant_id
And rt. dish_id = d. dish_id
GROUP BY r. restaurant_id, r.name
HAVING COUNT (rt. rating) >= 2
AND AVG (rt. rating) >= 4.0
v   Create a view called user_ratings which will show each rating alongside the user who   [2]
gave it.
CREATE OR REPLACE VIEW user_ratings AS
SELECT u.user_id, u. full_name, u. city, u. contact_no, r. dish_id, r. rating, r. rated_at,
r. feedback
FROM ratings r JOIN users u
ON u.user_id = r.user_id;
Q3   [20]
CO- 1 ;   a.   Entity /attribute to table/columns - 6 M   [10]
SO - 2;   Resolve Relationships – 2M
BL- 2   Indicate Primary key / foreign key – 2 M
Relational Schema Conversion
1. USER
USER(u_id PRIMARY KEY,   name,   email)
2. ADDRESS
ADDRESS(a_id PRIMARY KEY,   city,   state,   country,   u_id FOREIGN
KEY REFERENCES USER(u_id))
Relationship: User – lives in – Address → 1-to-M (one user can have many addresses)
3. ORDER
ORDER(o_no PRIMARY KEY,   order_amount,   order_date,   u_id FOREIGN
KEY REFERENCES USER(u_id))
Relationship: User – places – Order → 1-to-M
4. TRACKING_DETAIL
--- page 5 ---
TRACKING_DETAIL(trac_id PRIMARY KEY,   status,   o_no
FOREIGN KEY REFERENCES ORDER(o_no))
Relationship: Order – contains – Tracking_detail → 1-to-M
5. PRODUCT_CATEGORY
PRODUCT_CATEGORY(cat_id PRIMARY KEY,   cat_name)
6. PRODUCT
PRODUCT(p_id PRIMARY KEY,   p_name,   price,   description,   cat_id
FOREIGN KEY REFERENCES PRODUCT_CATEGORY(cat_id))
Relationship: Product – has – Product_Category → M-to-1
7. CART
CART(cart_id PRIMARY KEY)
8. PRODUCT_CART (resolving M-N between Product and Cart)
PRODUCT_CART(p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
cart_id FOREIGN KEY REFERENCES CART(cart_id),
PRIMARY KEY (p_id, cart_id))
Relationship: Product – added to – Cart → M-to-N
9. ORDER_PRODUCT (resolving M-N between Order and Product)
ORDER_PRODUCT(o_no FOREIGN KEY REFERENCES ORDER(o_no),
p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
PRIMARY KEY (o_no, p_id))
Relationship: Order – contains – Product → M-to-N
CO- 3 ;   b.   (i) Partial & Transitive dependencies (3 marks)   [10]
SO - 2;
BL- 3   Candidate key (in SALES): ({OrderID, ProdID})
(Quantity needs both; everything else is determined by either OrderID, CustID, ProdID,
or SalespersonID.)
Partial dependencies (depend on part of composite key)
•   OrderID → OrderDate, CustID, SalespersonID
(These don’t need ProdID.)
•   ProdID → ProdName, UnitPrice
(These don’t need OrderID.)
•   SalespersonID → SalespersonName, SalespersonRegion and
CustID → CustName, CustCity are not on the key, but in the single SALES table
they appear as attributes that are determined by non-key attributes—handled
under transitive below.
Transitive dependencies (key → nonkey → other nonkeys)
•   OrderID ⇒   → CustID and CustID → CustName, CustCity
OrderID → CustName, CustCity (transitive).
•   OrderID → SalespersonID and SalespersonID → SalespersonName,
SalespersonRegion ⇒
OrderID → SalespersonName, SalespersonRegion (transitive).
Full dependency:
--- page 6 ---
•   ({OrderID, ProdID} → Quantity) (depends on the whole key, not partial).
(ii) Decomposition to 3NF (step-by-step) (5 marks)
Start:
SALES(OrderID, OrderDate, CustID, CustName, CustCity, ProdID, ProdName,
UnitPrice, Quantity, SalespersonID, SalespersonName, SalespersonRegion)
Step 1: Remove partial dependencies (to reach 2NF)
Create relations on determinants of partial dependencies:
1. ORDER(OrderID, OrderDate, CustID, SalespersonID)
(from OrderID → OrderDate, CustID, SalespersonID)
2. PRODUCT(ProdID, ProdName, UnitPrice)
(from ProdID → ProdName, UnitPrice)
3. Keep line items for the fully dependent attribute:
SALES_LINE(OrderID, ProdID, Quantity) with PK (OrderID, ProdID)
Step 2: Remove transitive dependencies (to reach 3NF)
Separate dependents of non-key determinants:
4. CUSTOMER(CustID, CustName, CustCity)
(from CustID → CustName, CustCity)
5. SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
(from SalespersonID → SalespersonName, SalespersonRegion)
Now, in ORDER, CustID and SalespersonID remain as foreign keys only; their
descriptive attributes moved to their own tables, removing transitive dependencies.
All resulting tables are in 3NF:
•   Every non-key attribute depends on the key, the whole key, and nothing but the
key in its table.
(iii) Final set of relations with keys (2 marks)
•   ORDER(OrderID, OrderDate, CustID, SalespersonID)
FK: CustID → CUSTOMER, SalespersonID → SALESPERSON
• CUSTOMER(CustID, CustName, CustCity)
•   SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
• PRODUCT(ProdID, ProdName, UnitPrice)
•   SALES_LINE(OrderID, ProdID, Quantity)
FK: OrderID → ORDER, ProdID → PRODUCT
This decomposition is lossless and preserves the given FDs, with SALES_LINE capturing
the many-to-many between orders and products plus Quantity.
Q4   [20]
CO- 1 ;   a.   Discuss the major difficulties encountered while creating a database from scratch, and   [10]
SO - 2;   illustrate your answer with suitable examples.
BL-2
--- page 7 ---
Building a database from scratch involves several conceptual, technical, and
organizational challenges that must be carefully addressed to ensure efficiency, accuracy,
and long-term usability.
1.   Requirement Analysis:
2.   Data Modeling Challenges:
3.   Data Redundancy and Integrity:
4.   Normalization and Performance Balance:
5.   Security and Access Control:
6.   Scalability and Future Growth:
7.   Backup and Recovery Planning:
CO- 2 ;   b.   Solve the following queries using relational algebra   [10]
SO - 2;   Customer(CustomerID, CustomerName, City)
BL-2   Order(OrderID, OrderDate, CustomerID)
Product(ProductID, ProductName, Price)
Order_Product(OrderID, ProductID, Quantity)
(i) Find the names of customers who have placed at least one order.
(ii) Get the customer names and order IDs for orders placed after ‘2024-01-01’.
(iii) List all products ordered by customers who live in ‘Chicago’.
(iv) List the products that have been ordered by any customer with a quantity greater than
1
(v) Find all customers located in New York and have ordered something in month of
October 2024(assume date is in yyyy-mm-dd)
Q5   [20]
CO- 2 ;   a.   Consider the following table:   [10]
SO - 2;   employee (employee_id, first_name , last_name, email, phone_number , hire_date, job_id
BL-2   , salary, commission_pct , manager_id , department_id )
Write the SQL queries the following question:
i   Write a SQL query to find those employees who receive a higher salary than the employee   [3]
with ID 163. Return first name, last name.
Ans:
SELECT first_name, last_name
FROM employees
WHERE salary >
( SELECT salary
FROM employees
WHERE employee_id=163
);
ii   Write a SQL query to find out which employees have the same designation as the employee   [3]
whose ID is 169. Return first name, last name, department ID and job ID.
Ans:
SELECT first_name, last_name, salary, department_id, job_id
FROM employees
--- page 8 ---
WHERE job_id =
( SELECT job_id
FROM employees
WHERE employee_id=169
);
iii   Write a SQL query to find those employees whose salary matches the lowest salary of any   [4]
of the departments. Return first name, last name and department ID
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE salary IN
(SELECT MIN(salary)
FROM employees
GROUP BY department_id
);
CO- 4 ;   b.   [10]
SO - 2;
BL- 2
It is not conflict serializable as the graph is cyclic.
Step   T1   T2   T3
1   T1: Read(A)
2   T2: Read(A)
3   T1: Write(A)
4   T2: Write(A)
5   T2: Read(B)
6   T3: Read(B)
7   T2: Write(B)
8   T3: Write(B)
Serializability ensures that a concurrent execution is equivalent to some serial order of
transactions. This preserves database correctness by preventing anomalies such as lost
updates, dirty reads, non-repeatable reads, and inconsistent results—while still
allowing concurrency for performance.
Q6   [20]
CO- 4 ;   a.   1. Definition of a Transaction   [10]
SO - 2;   A transaction is a logical unit of database processing that consists of one or more database
BL-3   operations such as read, write, insert, update, or delete.
It represents a single, indivisible unit of work that must be executed completely or not at
all.
Example:
T1:
Read(A)
A = A – 100
Write(A)
Read(B)
B = B + 100
--- page 9 ---
Write(B)
This transaction transfers ₹100 from account A to account B.
2. ACID Properties of a Transaction
Property Meaning Example
Atomicity   All operations in a transaction must complete successfully; if any fails,
the entire transaction is rolled back. If the debit from A succeeds but the credit to B fails,
both changes are undone.
Consistency   A transaction transforms the database from one consistent state to
another, maintaining all integrity constraints.The total balance (A + B) remains the same
before and after the transfer.
Isolation Concurrent transactions should not interfere with each other; intermediate states
are invisible to others.   While T1 transfers money, another transaction T2 cannot read
the partially updated balance of A or B.
Durability   Once a transaction commits, its effects are permanently recorded in the
database, even after system failures.   After committing, the ₹100 transfer remains
intact even if the system crashes.
3. Conflict Serializability
A schedule is conflict-serializable if it can be transformed into a serial schedule by
swapping non-conflicting operations.
Two operations conflict if:
1.   They belong to different transactions.
2.   They operate on the same data item.
3.   At least one is a write operation.
Example:
Step   Transaction   Operation
1   T1   Read(A)
2   T2   Read(A)
3   T1   Write(A)
4   T2   Write(A)
Here, conflicts occur between T1 and T2 ⇒ on A.
Precedence graph: T1 → T2 (no cycle)   Conflict-serializable, equivalent to serial order
T1 → T2.
4. View Serializability
A schedule is view-serializable if it is view-equivalent to some serial schedule, i.e.,
•   Both schedules have the same read-from relationships (who reads whose value).
•   Both have the same final writes on each data item.
•   Both start from the same initial state.
Example:
S1: T1: W(A)
T2: R(A), W(A)
T3: R(A)
If both T2 and T3 read the value of A written by T1 and T2 does the final write,
then S1 is view-equivalent to the serial order T1 → T2 → T3.
5. Difference between Conflict and View Serializability
Aspect Conflict Serializability   View Serializability
Basis   Swapping of non-conflicting operations   Preservation of read-from and final-
write relationships
Detection   Using precedence (serialization) graph   More complex; requires
comparing read/write dependencies
Strictness   Stronger form — every conflict-serializable schedule is view-
serializable   Weaker — some non-conflict-serializable schedules can still be view-
serializable
Ease of Check   Easier to test algorithmically   Harder to test, computationally
expensive
--- page 10 ---
Example Schedule without cycles in precedence graph   Schedule with blind writes
(where a value is overwritten without being read) may still be view-serializable but not
conflict-serializable
CO- 4 ;   b.   Aspect   ACID (RDBMS)   BASE (NoSQL / Distributed   [10]
SO - 2;   Systems)
BL-1   Philosophy   Ensures strict correctness   Focuses on scalability and
and reliability   availability
Consistency   Strong consistency – all   Eventual consistency – nodes
Model   nodes see same data   become consistent over time
instantly
System Type   Centralized or small-scale   Distributed, large-scale, cloud-
transactional systems   based systems
Transaction   Transactions are atomic   Transactions may be broken or
Handling   and isolated   partial across nodes
Availability   Prioritizes consistency   Prioritizes availability over
vs.   over availability   consistency
Consistency
Response   Slower, due to strict   Faster, as some consistency is
Time   locking and commit   relaxed
protocols
Use Cases   Banking, financial,   Social media feeds, e-
inventory systems   commerce catalogs, IoT data
Error   Rollback ensures integrity   Recovery through replication
Recovery   after failures   and eventual updates
CAP Theorem CP systems (Consistency + AP systems (Availability +
View   Partition tolerance)   Partition tolerance)
Examples   Oracle, MySQL,   Cassandra, MongoDB,
PostgreSQL   Amazon DynamoDB
Q7   [20]
CO-1 ;   A   Advantages of DBMS [5 Marks]   [5]
SO- 2;   1. Reduces Data Redundancy and Inconsistency
BL-1   – Data is stored centrally, avoiding duplication and ensuring all users see the
same updated information.
2. Improves Data Security
– Access to data is controlled through authentication and authorization,
protecting sensitive information.
3. Ensures Data Integrity and Accuracy
– Integrity constraints like primary keys and foreign keys maintain correctness of
data values.
4. Supports Concurrent Access and Sharing
– Multiple users can work on the same database simultaneously without
conflicts, using concurrency control.
5. Provides Backup and Recovery
– Automatic backup and recovery mechanisms protect data against crashes and
system failures.
CO- 2 ;   b   Joins in SQL [5 Marks]   [5]
SO - 2;   Definition:
BL-2   A JOIN in SQL is used to combine rows from two or more tables based on a related
column (usually a primary–foreign key relationship).
1. INNER JOIN
--- page 11 ---
Returns only the matching rows from both tables.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
INNER JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows students who are enrolled in a course.
2. LEFT JOIN (LEFT OUTER JOIN)
Returns all rows from the left table, and matching rows from the right; non-matching
rows show NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
LEFT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students, even if not enrolled in any course.
3. RIGHT JOIN (RIGHT OUTER JOIN)
Returns all rows from the right table, and matching rows from the left; non-matching
rows show NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
RIGHT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all courses, even if no student has enrolled.
4. FULL JOIN (FULL OUTER JOIN)
Returns all rows from both tables; unmatched rows are filled with NULLs.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
FULL JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students and all courses, with NULLs where no match exists.
5. CROSS JOIN
Produces Cartesian product — every row of the first table with every row of the second.
Example:
SELECT Students.Name, Courses.CourseName
FROM Students
CROSS JOIN Courses;
Shows all possible combinations of students and courses.
Summary:
Type of Join   Description   Matching/Unmatched Rows
INNER JOIN Common records only   Matching only
LEFT JOIN   All left + matching right   Unmatched right → NULL
RIGHT JOIN   All right + matching left   Unmatched left → NULL
FULL JOIN   All rows from both tables Unmatched → NULL
CROSS JOIN   Cartesian product   No condition needed
CO- 3;   C   Armstrong’s Axioms [5 Marks]   [5]
SO - 2;   Definition:
BL-3   Armstrong’s Axioms are a set of inference rules used to derive all possible functional
dependencies (FDs) from a given set of FDs in a relational schema.
They form the theoretical foundation for normalization and dependency closure.
1. Basic Axioms
Axiom   Rule Description
--- page 12 ---
⊆
a) Reflexivity   If Y   X, then X → Y. (A set of attributes determines any   If X = {A, B} then {A,
of its subsets.)   B} → {A}.
b) Augmentation   If X → Y, then XZ → YZ. (Adding the same attribute(s) to   If A → B, then AC →
both sides preserves the dependency.)   BC.
c) Transitivity   If X → Y and Y → Z, then X → Z. (Dependencies can be   If A → B and B → C,
chained.)   then A → C.
2. Derived (Additional) Axioms
Using the three basic rules, the following can be derived:
Derived Axiom   Meaning
Union (Additivity)   If X → Y and X → Z, then X → YZ
Decomposition (Projectivity)   If X → YZ, then X → Y and X → Z
Pseudo-transitivity   If X → Y and YZ → W, then XZ → W
3. Importance
•   These axioms help in finding attribute closure (X⁺)
•   Used to test dependency preservation and lossless decomposition during
normalization.
CO- 4 ;   d   "Key Value Pair Based   [5]
SO - 2;
BL-1   Data is stored in key/value pairs. It is designed in such a way to handle lots of data and
heavy load.
Key-value pair storage databases store data as a hash table where each key is unique, and
the value can be a JSON, BLOB(Binary Large Objects), string, etc.
For example, a key-value pair may contain a key like ""Website"" associated with a value
like ""Guru99"".
It is one of the most basic types of NoSQL databases. This kind of NoSQL database is
used as a collection, dictionaries, associative arrays, etc. Key value stores help the
developer to store schema-less data. They work best for shopping cart contents.
Redis, Dynamo, Riak are some examples of key-value store DataBases. They are all
based on Amazon's Dynamo paper.
Column-based
Column-oriented databases work on columns and are based on BigTable paper by
Google. Every column is treated separately. Values of single column databases are stored
contiguously.
Column based NoSQL database
They deliver high performance on aggregation queries like SUM, COUNT, AVG, MIN
etc. as the data is readily available in a column.
Column-based NoSQL databases are widely used to manage data warehouses, business
intelligence, CRM, Library card catalogs,
HBase, Cassandra, HBase, Hypertable are examples of column based database.
"
````

## 2024-25 · Final-Exam · Sem 7 · Answer key · paper 321595f9ea8e

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/Integrated_IT_7037/Database Management Systems/ANS_Database Management Systems(702AI0C001)_2025-2026.docx`
- Text: docx (1 page)

````text
﻿SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF   TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025
|
Program/s: ___BTech IT/MBATech IT/BTech Cyber /BTI IT___
Stream/s : Information Technology
| Year: 2 Semester: V/IX
|
Subject: ___DBMS
| Time: _3__ hrs (______to_______)
|
Date:   /   / 2025
| No. of Pages:__3___
|
Marks: __100_______
|
|
Final Examination/Re-Examination ( Re-exam year)
|
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Figures in brackets on the right hand side indicate full marks.
6) Assume Suitable data if necessary.
SET 1- synoptic

Q1

|
| Answer the following questions
| [20]
|
CO-   1;
SO- 2;
BL- 1
| a
| What are data models? Explain the Relational Model.
1. Definition of Data Models (2 Marks)

A   data model   is a   conceptual framework   that describes how data are   structured, stored, and manipulated   in a database system.
It defines the   logical structure   of the database — the relationships among data, the constraints, and the operations that can be performed.
Common types include:
Hierarchical Model
Network Model
Relational Model
Object Oriented Model

2. Relational Model (3 Marks)

The   Relational Model   organizes data into   relations (tables)   consisting of   rows and columns   .
Each   table (relation)   represents an   entity   , each   row (tuple)   represents a   record   , and each   column (attribute)   represents a   data field   .
Every relation has a   Primary Key   that uniquely identifies each tuple.
Foreign Keys   are used to establish relationships between tables.
Data are manipulated using   Relational Algebra   and the   SQL language   for operations like selection, projection, join, and union.

Example:

| StudentID | Name   | Branch |
|   |   |   |
| S101   | Riya   | IT   |
| S102   | Arjun | CS   |

Here,   StudentID   → Primary Key; the table “Student” represents the   Student entity   .
| [5]
|
CO-   2;
SO - 2;
BL- 2
| b
| 1. Features of a Good Database Design (4 Marks)

Data Integrity and Consistency:

Each piece of data is stored only once (no redundancy), ensuring consistency.

Example: Customer details stored in one CUSTOMER table, not repeated in every ORDER record.

Minimal Data Redundancy:

Redundant data causes update anomalies and wasted storage.

Example: Instead of repeating department names for every employee, use a separate DEPARTMENT table with a foreign key reference.

Proper Use of Normalization:

Splitting large tables into smaller ones to remove partial and transitive dependencies (1NF–3NF).

Example: Separating EMPLOYEE(EmpID, EmpName, DeptID) and DEPARTMENT(DeptID, DeptName).

Clear Entity–Relationship Mapping:

Logical relationships (1:1, 1:N, M:N) must be clearly defined using primary and foreign keys.

Example: One‐to‐many between CUSTOMER and ORDER.

Scalability and Performance:

Well-designed indexes and relationships support fast queries and future data growth.

Example: Indexing OrderID in ORDERS table speeds up retrieval.

Remove Insert Update Anomalies

2. Conclusion (1 Mark)

A good database design is normalized, non-redundant, and supports data integrity, leading to efficient storage, accurate information, and simplified maintenance.
| [5]
|
CO-   3 ;
SO - 2;
BL- 2
| c
| (a) Superkeys: [2Marks]
{RollNo}, {Email}, {AadhaarNo}, {RollNo, Name}, {Email, Phone}, etc.
(b) Candidate Keys: [2Marks]   - minimal keys
{RollNo}, {Email}, {AadhaarNo}
(c) Primary Key:   - only one to be written from candidate keys
RollNo —unique.   [1Marks]
| [5]
|
CO-   4 ;
SO - 2;
BL-1
| d
| What is the significance of CAP theorem in NOSQL
The CAP Theorem is a fundamental principle in NoSQL databases that describes the trade-offs among three key properties:
1.Consistency (C): Every read receives the most recent write or an error.
2.Availability (A): Every request receives a response, regardless of the state of the data.
3.Partition Tolerance (P): The system continues to operate even if network partitions or communication failures occur.
Significance in NoSQL:
•NoSQL databases are often distributed systems. The CAP theorem explains that it is impossible to achieve all three properties simultaneously; a database can only fully guarantee two out of three.
•For example:
oMongoDB prioritizes Consistency + Partition Tolerance (CP) by default.
oCassandra prioritizes Availability + Partition Tolerance (AP).
•This helps developers choose the right database and configure it according to application needs, balancing consistency, availability, and fault tolerance.
"
| [5]
|
Q2
|
|
| [20]
|
CO- 1   ;
SO - 2;
BL-2
| a
|
All Entities drawn – 2M
All attributes   - 2M
Relationships – 2M
Cardinality – 2M
Participation – 2M

| [10]
|
CO- 2   ;
SO - 2;
BL- 2
| b
| Consider following movie database:

users (user_id, full_name, city, contact_no)
restaurants (restaurant_id, name, address, price level, is active)
dishes (dish_id, restaurant, name, price, is_veg, is spicy)
ratings (user_id, dish_id, rating, rated_at, feedback)

Write the SQL queries   the following question:
| [10]
|

| i
| Add a new column “email” to users table
Ans:
ALTER TABLE users
ADD COLUMN email VARCHAR (40);

| [2]
|

| ii
| Modify table dishes to enforce business rules “dishes.price must be > 0.” using CHECK constraints
Ans:
ALTER TABLE dishes
ADD CONSTRAINT chk_price
CHECK (price > 0);
| [2]
|

| iii
| Select all veg, not-spicy dishes with price <= 250 from active restaurants.
Ans:
SELECT d.name AS dish, r.name AS restaurant, d.price
FROM dishes d, restaurants r
Where r. restaurant_id = d. restaurant_id and r.is_active = ‘yes’   AND d.is_veg = ‘yes’   AND d.is_spicy is ‘No’ and d. price <= 250
| [2]
|

| iv
| Show each restaurant’s average rating and number of ratings but return only those with at least 2 ratings and an average ≥ 4.0.
Ans:
SELECT r.name AS restaurant, ROUND (AVG (rt. rating), 2) AS avg_rating,
COUNT (rt. rating) AS rating_count
FROM restaurants r, dishes d, ratings rt where d. restaurant_id = r. restaurant_id
And rt. dish_id = d. dish_id
GROUP BY r. restaurant_id, r.name
HAVING COUNT (rt. rating) >= 2
AND AVG (rt. rating) >= 4.0
| [2]
|

| v
| Create a view called user_ratings which will show each rating alongside the user who gave it.
CREATE OR REPLACE VIEW user_ratings AS
SELECT   u.user_id, u. full_name, u. city, u. contact_no, r. dish_id, r. rating, r. rated_at,
r. feedback
FROM ratings r JOIN users u
ON u.user_id = r.user_id;
| [2]
|
Q3
|
|
| [20]
|
CO-   1 ;
SO - 2;
BL- 2
| a.
| Entity /attribute to table/columns   - 6 M
Resolve Relationships – 2M
Indicate Primary key / foreign key – 2 M

Relational Schema Conversion
1. USER
USER(u_id PRIMARY KEY,   name,   email)
2. ADDRESS
ADDRESS(a_id PRIMARY KEY,   city,   state,   country,   u_id FOREIGN KEY REFERENCES USER(u_id))
Relationship: User – lives in – Address → 1-to-M (one user can have many addresses)

3. ORDER
ORDER(o_no PRIMARY KEY,   order_amount,   order_date,   u_id FOREIGN KEY REFERENCES USER(u_id))
Relationship: User – places – Order → 1-to-M

4. TRACKING_DETAIL
TRACKING_DETAIL(trac_id PRIMARY KEY,   status,   o_no FOREIGN KEY REFERENCES ORDER(o_no))
Relationship: Order – contains – Tracking_detail → 1-to-M

5. PRODUCT_CATEGORY
PRODUCT_CATEGORY(cat_id PRIMARY KEY,   cat_name)

6. PRODUCT
PRODUCT(p_id PRIMARY KEY,   p_name,   price,   description,   cat_id FOREIGN KEY REFERENCES PRODUCT_CATEGORY(cat_id))
Relationship: Product – has – Product_Category → M-to-1

7. CART
CART(cart_id PRIMARY KEY)

8. PRODUCT_CART (resolving M-N between Product and Cart)
PRODUCT_CART(p_id   FOREIGN KEY REFERENCES PRODUCT(p_id),
cart_id FOREIGN KEY REFERENCES CART(cart_id),
PRIMARY KEY (p_id, cart_id))
Relationship: Product – added to – Cart → M-to-N

9. ORDER_PRODUCT (resolving M-N between Order and Product)
ORDER_PRODUCT(o_no FOREIGN KEY REFERENCES ORDER(o_no),
p_id FOREIGN KEY REFERENCES PRODUCT(p_id),
PRIMARY KEY (o_no, p_id))
Relationship: Order – contains – Product → M-to-N

| [10]
|
CO-   3 ;
SO - 2;
BL- 3
| b.

| (i) Partial & Transitive dependencies (3 marks)
Candidate key (in SALES): ({OrderID, ProdID})(Quantity needs both; everything else is determined by either OrderID, CustID, ProdID, or SalespersonID.)
Partial dependencies (depend on part of composite key)
OrderID → OrderDate, CustID, SalespersonID(These don’t need ProdID.)
ProdID → ProdName, UnitPrice(These don’t need OrderID.)
SalespersonID → SalespersonName, SalespersonRegion andCustID → CustName, CustCity are not on the key, but in the single SALES table they appear as attributes that are determined by non-key attributes—handled under transitive below.
Transitive dependencies (key → nonkey → other nonkeys)
OrderID → CustID and CustID → CustName, CustCity⇒ OrderID → CustName, CustCity (transitive).
OrderID → SalespersonID and SalespersonID → SalespersonName, SalespersonRegion⇒ OrderID → SalespersonName, SalespersonRegion (transitive).
Full dependency:
({OrderID, ProdID} → Quantity) (depends on the whole key, not partial).
(ii) Decomposition to 3NF (step-by-step) (5 marks)
Start:SALES(OrderID, OrderDate, CustID, CustName, CustCity, ProdID, ProdName, UnitPrice, Quantity, SalespersonID, SalespersonName, SalespersonRegion)
Step 1: Remove partial dependencies (to reach 2NF)
Create relations on determinants of partial dependencies:
ORDER(OrderID, OrderDate, CustID, SalespersonID)(from OrderID → OrderDate, CustID, SalespersonID)
PRODUCT(ProdID, ProdName, UnitPrice)(from ProdID → ProdName, UnitPrice)
Keep line items for the fully dependent attribute:SALES_LINE(OrderID, ProdID, Quantity) with PK (OrderID, ProdID)
Step 2: Remove transitive dependencies (to reach 3NF)
Separate dependents of non-key determinants:4. CUSTOMER(CustID, CustName, CustCity)(from CustID → CustName, CustCity)5. SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)(from SalespersonID → SalespersonName, SalespersonRegion)
Now, in ORDER, CustID and SalespersonID remain as foreign keys only; their descriptive attributes moved to their own tables, removing transitive dependencies.
All resulting tables are in 3NF:
Every non-key attribute depends on the key, the whole key, and nothing but the key in its table.
(iii) Final set of relations with keys (2 marks)
ORDER(OrderID, OrderDate, CustID, SalespersonID)FK: CustID → CUSTOMER, SalespersonID → SALESPERSON
CUSTOMER(CustID, CustName, CustCity)
SALESPERSON(SalespersonID, SalespersonName, SalespersonRegion)
PRODUCT(ProdID, ProdName, UnitPrice)
SALES_LINE(OrderID, ProdID, Quantity)FK: OrderID → ORDER, ProdID → PRODUCT
This decomposition is lossless and preserves the given FDs, with SALES_LINE capturing the many-to-many between orders and products plus Quantity.
| [10]
|
Q4
|
|
| [20]
|
CO-   1 ;
SO - 2;
BL-2
| a.
| Discuss the major difficulties encountered while creating a database from scratch, and illustrate your answer with suitable examples.
Building a database from scratch involves several conceptual, technical, and organizational challenges that must be carefully addressed to ensure efficiency, accuracy, and long-term usability.
1.Requirement Analysis:
2.Data Modeling Challenges:
3.Data Redundancy and Integrity:
4.Normalization and Performance Balance:
5.Security and Access Control:
6.Scalability and Future Growth:
7.Backup and Recovery Planning:

| [10]
|
CO-   2 ;
SO - 2;
BL-2
| b.
| Solve the following queries using relational algebra
Customer(CustomerID, CustomerName, City)
Order(OrderID, OrderDate, CustomerID)
Product(ProductID, ProductName, Price)
Order_Product(OrderID, ProductID, Quantity)
Find the names of customers who have placed at least one order.

Get the customer names and order IDs for orders placed after ‘2024-01-01’.

List all products ordered by customers who live in ‘Chicago’.

List the products that have been ordered by any customer with a quantity greater than 1

Find all customers located in New York and have ordered something in month of October 2024(assume date is in yyyy-mm-dd)

| [10]
|
Q5
|
|
| [20]
|
CO-   2 ;
SO - 2;
BL-2
| a.
| Consider the following table:
employee (employee_id, first_name , last_name, email, phone_number , hire_date, job_id , salary, commission_pct , manager_id , department_id )

Write the SQL queries   the following question:
| [10]
|

| i
| Write a SQL query to find those employees who receive a higher salary than the employee with ID 163. Return first name, last name.
Ans:
SELECT first_name, last_name
FROM employees
WHERE salary >
( SELECT salary
FROM employees
WHERE employee_id=163
);
| [3]
|

| ii
| Write a SQL query to find out which employees have the same designation as the employee whose ID is 169. Return first name, last name, department ID and job ID.
Ans:
SELECT first_name, last_name, salary, department_id, job_id
FROM employees
WHERE job_id =
( SELECT job_id
FROM employees
WHERE employee_id=169
);
| [3]
|

| iii
| Write a SQL query to find those employees whose salary matches the lowest salary of any of the departments. Return first name, last name and department ID
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE salary IN
(SELECT MIN(salary)
FROM employees
GROUP BY department_id
);
| [4]
|
CO-   4 ;
SO - 2;
BL- 2
| b.
|

It is not conflict serializable as the graph is   cyclic.
Step
| T1
| T2
| T3
|
1
| T1: Read(A)
|
|
|
2
|
| T2: Read(A)
|
|
3
| T1: Write(A)
|
|
|
4
|
| T2: Write(A)
|
|
5
|
| T2: Read(B)
|
|
6
|
|
| T3: Read(B)
|
7
|
| T2: Write(B)
|
|
8
|
|
| T3: Write(B)
|

Serializability ensures that a concurrent execution is equivalent to some serial order of transactions. This preserves database correctness by preventing anomalies such as lost updates, dirty reads, non-repeatable reads, and inconsistent results—while still allowing concurrency for performance.

| [10]
|
Q6
|
|
| [20]
|
CO- 4   ;
SO - 2;
BL-3
| a.
| 1. Definition of a Transaction
A transaction is a logical unit of database processing that consists of one or more database operations such as read, write, insert, update, or delete.
It represents a single, indivisible unit of work that must be executed completely or not at all.
Example:
T1:
Read(A)
A = A – 100
Write(A)
Read(B)
B = B + 100
Write(B)
This transaction transfers ₹100 from account A to account B.
2. ACID Properties of a Transaction
PropertyMeaningExample
AtomicityAll operations in a transaction must complete successfully; if any fails, the entire transaction is rolled back.If the debit from A succeeds but the credit to B fails, both changes are undone.
ConsistencyA transaction transforms the database from one consistent state to another, maintaining all integrity constraints.The total balance (A + B) remains the same before and after the transfer.
IsolationConcurrent transactions should not interfere with each other; intermediate states are invisible to others.While T1 transfers money, another transaction T2 cannot read the partially updated balance of A or B.
DurabilityOnce a transaction commits, its effects are permanently recorded in the database, even after system failures.After committing, the ₹100 transfer remains intact even if the system crashes.
3. Conflict Serializability
A schedule is conflict-serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
Two operations conflict if:
1.They belong to different transactions.
2.They operate on the same data item.
3.At least one is a write operation.
Example:
StepTransactionOperation
1T1Read(A)
2T2Read(A)
3T1Write(A)
4T2Write(A)
Here, conflicts occur between T1 and T2 on A.
Precedence graph: T1 → T2 (no cycle) ⇒ Conflict-serializable, equivalent to serial order T1 → T2.
4. View Serializability
A schedule is view-serializable if it is view-equivalent to some serial schedule, i.e.,
•Both schedules have the same read-from relationships (who reads whose value).
•Both have the same final writes on each data item.
•Both start from the same initial state.
Example:
S1:   T1: W(A)
T2: R(A), W(A)
T3: R(A)
If both T2 and T3 read the value of A written by T1 and T2 does the final write,
then S1 is view-equivalent to the serial order T1 → T2 → T3.
5. Difference between Conflict and View Serializability
AspectConflict SerializabilityView Serializability
BasisSwapping of non-conflicting operationsPreservation of read-from and final-write relationships
DetectionUsing precedence (serialization) graphMore complex; requires comparing read/write dependencies
StrictnessStronger form — every conflict-serializable schedule is view-serializableWeaker — some non-conflict-serializable schedules can still be view-serializable
Ease of CheckEasier to test algorithmicallyHarder to test, computationally expensive
ExampleSchedule without cycles in precedence graphSchedule with blind writes (where a value is overwritten without being read) may still be view-serializable but not conflict-serializable

| [10]
|
CO- 4   ;
SO - 2;
BL-1
| b.
| Aspect
| ACID (RDBMS)
| BASE (NoSQL / Distributed Systems)
|
Philosophy
| Ensures strict correctness and reliability
| Focuses on scalability and availability
|
Consistency Model
| Strong consistency – all nodes see same data instantly
| Eventual consistency – nodes become consistent over time
|
System Type
| Centralized or small-scale transactional systems
| Distributed, large-scale, cloud-based systems
|
Transaction Handling
| Transactions are atomic and isolated
| Transactions may be broken or partial across nodes
|
Availability vs. Consistency
| Prioritizes consistency over availability
| Prioritizes availability over consistency
|
Response Time
| Slower, due to strict locking and commit protocols
| Faster, as some consistency is relaxed
|
Use Cases
| Banking, financial, inventory systems
| Social media feeds, e-commerce catalogs, IoT data
|
Error Recovery
| Rollback ensures integrity after failures
| Recovery through replication and eventual updates
|
CAP Theorem View
| CP systems (Consistency + Partition tolerance)
| AP systems (Availability + Partition tolerance)
|
Examples
| Oracle, MySQL, PostgreSQL
| Cassandra, MongoDB, Amazon DynamoDB
|

| [10]
|
Q7

|
|
| [20]
|
CO-1   ;
SO- 2;
BL-1
| A
| Advantages of DBMS [5 Marks]
Reduces Data Redundancy and Inconsistency– Data is stored centrally, avoiding duplication and ensuring all users see the same updated information.
Improves Data Security– Access to data is controlled through authentication and authorization, protecting sensitive information.
Ensures Data Integrity and Accuracy– Integrity constraints like primary keys and foreign keys maintain correctness of data values.
Supports Concurrent Access and Sharing– Multiple users can work on the same database simultaneously without conflicts, using concurrency control.
Provides Backup and Recovery– Automatic backup and recovery mechanisms protect data against crashes and system failures.

| [5]
|
CO-   2 ;
SO - 2;
BL-2
| b
| Joins in SQL [5 Marks]
Definition:A JOIN in SQL is used to combine rows from two or more tables based on a related column (usually a primary–foreign key relationship).
1. INNER JOIN
Returns only the matching rows from both tables.Example:
SELECT Students.Name, Courses.CourseName
FROM Students
INNER JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows students who are enrolled in a course.
2. LEFT JOIN (LEFT OUTER JOIN)
Returns all rows from the left table, and matching rows from the right; non-matching rows show NULLs.Example:
SELECT Students.Name, Courses.CourseName
FROM Students
LEFT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students, even if not enrolled in any course.
3. RIGHT JOIN (RIGHT OUTER JOIN)
Returns all rows from the right table, and matching rows from the left; non-matching rows show NULLs.Example:
SELECT Students.Name, Courses.CourseName
FROM Students
RIGHT JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all courses, even if no student has enrolled.

4. FULL JOIN (FULL OUTER JOIN)
Returns all rows from both tables; unmatched rows are filled with NULLs.Example:
SELECT Students.Name, Courses.CourseName
FROM Students
FULL JOIN Courses ON Students.CourseID = Courses.CourseID;
Shows all students and all courses, with NULLs where no match exists.
5. CROSS JOIN
Produces Cartesian product — every row of the first table with every row of the second.Example:
SELECT Students.Name, Courses.CourseName
FROM Students
CROSS JOIN Courses;
Shows all possible combinations of students and courses.
Summary:
Type of Join
| Description
| Matching/Unmatched Rows
|
INNER JOIN
| Common records only
| Matching only
|
LEFT JOIN
| All left + matching right
| Unmatched right → NULL
|
RIGHT JOIN
| All right + matching left
| Unmatched left → NULL
|
FULL JOIN
| All rows from both tables
| Unmatched → NULL
|
CROSS JOIN
| Cartesian product
| No condition needed
|

| [5]
|
CO-   3;
SO - 2;
BL-3
| C
| Armstrong’s Axioms [5 Marks]
Definition:Armstrong’s Axioms are a set of inference rules used to derive all possible functional dependencies (FDs) from a given set of FDs in a relational schema.They form the theoretical foundation for normalization and dependency closure.
1. Basic Axioms
Axiom
| Rule Description
| Example
|
a) Reflexivity
| If Y ⊆ X, then X → Y. (A set of attributes determines any of its subsets.)
| If X = {A, B} then {A, B} → {A}.
|
b) Augmentation
| If X → Y, then XZ → YZ. (Adding the same attribute(s) to both sides preserves the dependency.)
| If A → B, then AC → BC.
|
c) Transitivity
| If X → Y and Y → Z, then X → Z. (Dependencies can be chained.)
| If A → B and B → C, then A → C.
|
2. Derived (Additional) Axioms
Using the three basic rules, the following can be derived:
Derived Axiom
| Meaning
|
Union (Additivity)
| If X → Y and X → Z, then X → YZ
|
Decomposition (Projectivity)
| If X → YZ, then X → Y and X → Z
|
Pseudo-transitivity
| If X → Y and YZ → W, then XZ → W
|

3. Importance
These axioms help in finding attribute closure (X⁺)
Used to test dependency preservation and lossless decomposition during normalization.

| [5]
|
CO-   4 ;
SO - 2;
BL-1
| d
| "Key Value Pair Based

Data is stored in key/value pairs. It is designed in such a way to handle lots of data and heavy load.
Key-value pair storage databases store data as a hash table where each key is unique, and the value can be a JSON, BLOB(Binary Large Objects), string, etc.
For example, a key-value pair may contain a key like ""Website"" associated with a value like ""Guru99"".

It is one of the most basic types of NoSQL databases. This kind of NoSQL database is used as a collection, dictionaries, associative arrays, etc. Key value stores help the developer to store schema-less data. They work best for shopping cart contents.
Redis, Dynamo, Riak are some examples of key-value store DataBases. They are all based on Amazon's Dynamo paper.
Column-based
Column-oriented databases work on columns and are based on BigTable paper by Google. Every column is treated separately. Values of single column databases are stored contiguously.

Column based NoSQL database
They deliver high performance on aggregation queries like SUM, COUNT, AVG, MIN etc. as the data is readily available in a column.
Column-based NoSQL databases are widely used to manage data warehouses, business intelligence, CRM, Library card catalogs,
HBase, Cassandra, HBase, Hypertable are examples of column based database.
"
| [5]
|
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 789dfd91c14f

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Database Management Systems/ANS_Database Management Systems(703AI0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Feb 2025
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 1 Re-exam(Exam Year: 2024-2025)
Subject: Database Management Systems
Date: 13 Feb 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data (if Required) and mention assumed data in answers.
Section A: Attempt All Questions (Each Question Carry 5M)
Question 1
CO 1;   A.   Define Database Language – 2M   5M
SO6;   Any 3 Types- 3M
BL2   DML
DDL
DQL
TCL
DCL
CO 1;   B. What are Extended ER features (2M)   5M
SO6;   Aggregation
BL2   Generalisation
Specialisation
Union/Category
Examples of any one feature and how they enhance ER model – 3M
CO 2;   C.   Relational Constraints – 2M   5M
SO1;   Impact on data integrity and consistency – 3M
BL4
CO 4;   D.   Explain the Different Types of NoSQL Databases with Examples.   5M
SO7;   (Any 3 with Examples)
BL4   Document Stores
Key-Value Stores
Column Family Stores
Graph Databases
********** 1 **********
--- page 2 ---
Multi-Model Databases
Section B: Attempt Any Four Questions from Questions 2 to 7 (Each Question Carry 20M)
Question 2
CO 3;   A.   Functional Dependency (FD) – 2M   10M
SO1;   Any 4 Types of Functional dependencies with examples – 8M
BL4   Full Functional Dependency
Partial Functional Dependency
Transitive Functional Dependency
Trivial Functional Dependency
Multivalued Dependency
CO 1;   B.   Identify the key entities and their attributes. (3M)   10M
SO6;   Product(Product ID, Name, Description, Price, Stock Quantity)
BL5   Category(Category ID, Name (e.g., electronics, clothing, home & kitchen)
Customer(Customer ID, Name, Address, Contact Details)
Order(Order ID, Order Date, Total Price)
Order Item (Order Item ID, Order ID, Product ID, Quantity)
Review(Review ID, Customer ID, Product ID, Review Text, Rating)
Specify the relationships between these entities (3M)
Category - Product: One-to-Many (1:M)
Customer - Order: One-to-Many (1:M)
Order - Order Item: One-to-Many (1:M)
Product - Order Item: One-to-Many (1:M)
Customer - Review: One-to-Many (1:M)
Product - Review: One-to-Many (1:M)
Correct design of Entity-Relationship diagram. (4M)
Question 3
CO 2;   A. SQL Views with example and use – 6M   10M
SO1;
BL4   SQL example (4M)
CREATE VIEW CustomerOrderView AS
SELECT c.CustomerID, c.Name AS CustomerName, o.OrderID, o.OrderDate, c.TotalPrice
FROM Customer c
JOIN Order o ON c.CustomerID = o.CustomerID;
CO 4;   B.   Define view serializability – 2M   10M
SO6;   Definition and one example
BL3   Check whether the below-given schedule is serialisable (6M)
R1(A), W2(A), R3(A), W1(A), W3(A)
********** 2 **********
--- page 3 ---
A schedule is serialisable if the conflict graph is acyclic. our graph
forms a cycle (T1 → T3 → T1)
Since there is a cycle in the serialisation graph, the schedule is not
serialisable.
Question 4
CO 3;   A. 1NF – (2M)   10M
SO1;   2NF – (2M)
BL2   3NF – (2M)
Convert Relation R(A, B, C, D, E, F, G) to 3rd normal form – 4M
R1 (A, B, E, F)
R2 (E, C, D)
R3 (F, G)
CO 2;   B.   Write Relational algebra queries for given questions,   10M
SO1;   1. All Students in Computer Science course
BL6   (3 Marks)
2. List the names of all students who have a GPA below 3.0.
(3 Marks)
3. Highest GPA for Female Students
(4 Marks)
Question 5
CO 4;   A.   Process of Inserting Documents (5 Marks)   10M
SO7;   Set Up Your MongoDB Environment:
BL2   Connect to the Database:
Specify the Collection:
Inserting a Single Document:
Inserting Multiple Documents:
Common Scenarios for Data Insertion (5 Marks)
Creating New Records
Bulk Insertion
Data Migration
Log Entries and Events
User Profiles and Configuration Settings
Handling Real-Time Data
CO 2;   B.   Consider data in Q.4 (B) and write SQL JOIN queries for given questions,   10M
SO1;   1. Names of all students, along with the corresponding course names
BL6   for each enrollment. (2M)
SELECT s.Name AS StudentName, c.CourseName AS CourseName
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID;
********** 3 **********
--- page 4 ---
2. Find the total number of students enrolled in each course. (2M)
SELECT c.CourseName, COUNT(e.StudentID) AS TotalStudents
FROM Courses c
LEFT JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseName;
3. Find the average GPA of students grouped by their majors. (3M)
SELECT Major, AVG(GPA) AS AverageGPA
FROM Students
GROUP BY Major;
4. Count the total number of enrollments for male and female students.
(3M)
SELECT s.Gender, COUNT(e.EnrollmentID) AS TotalEnrollments
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID
GROUP BY s.Gender;
Question 6
CO 4;   A.   What is a Transaction – 2M   10M
SO6;   Examine various Properties of Transactions (ACID). – 2M each property
BL4   Atomic– 2M
Consistency– 2M
Isolation– 2M
Durability– 2M
CO 2;   B.   Consider data in Q.4 (B) and write SQL Sub-Queries for given questions,   10M
SO1;   1. List the names and GPAs of students who have a GPA higher than
BL6   the average GPA of all students. (2M)
SELECT Name, GPA
FROM Students
WHERE GPA > (SELECT AVG(GPA) FROM Students);
2. Find all courses that have more than two students enrolled. (2M)
SELECT CourseName
FROM Courses
WHERE CourseID IN (
SELECT CourseID
FROM Enrollments
GROUP BY CourseID
HAVING COUNT(StudentID) > 2
);
3. Find the names of students who are not enrolled in any courses. (3M)
SELECT Name
FROM Students
WHERE StudentID NOT IN (
SELECT StudentID
********** 4 **********
--- page 5 ---
FROM Enrollments );
4. Find the major that has the highest average GPA. (3M)
SELECT Major
FROM Students
GROUP BY Major
HAVING AVG(GPA) = (
SELECT MAX(AverageGPA)
FROM (
SELECT AVG(GPA) AS AverageGPA
FROM Students
GROUP BY Major
) AS AvgGPAByMajor
);
Question 7
CO 1;   A.   Concept of View of Data with Diagram – 3M   5M
SO6;   How does it provide an abstraction – 2M
BL2
CO 2;   B.   Identify and explain the main components of a relational database.   5M
SO2;   Relation – 2M
BL4   Record – 2M
Field – 1M
Domain – 1M
CO 3;   C. Any three key features of a good relational database – 5M   5M
SO1;   No Redundancy
BL4   No data anomalies
No complex data
CO 1;   D.   Entity-Relationship (ER) model – 2M   5M
SO6;   Significance and example – 3M
BL2
********** 5 **********
````

## 2024-25 · Re-Exam · Sem 4 · Answer key · paper e4990ab3c815

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_04/Re-Exam/BTech_CSE_DS_7011/Database Management System/ANS_Database Management System(702CO0C040)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2025
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Sem 4 Re-exam(Exam Year: 2024-2025)
Subject: Database Management System
Date: 10 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data whenever required (Please mentions such data in answer)
5. Question 1 is compulsory (20 Marks), Attempt any 4 Questions from Question 2 to 7 (80 Marks)
Section A: Attempt All Questions (Each Question Carry 5M)
Question 1
CO1;   A.   Three-Tier Architecture (3 Marks)
SO1;   The Three-Tier Architecture in a Database Management System (DBMS)
BL2   divides the system into three logical layers: Presentation Tier, Application
Tier, and Data Tier. This architecture enhances performance, scalability,
security, and maintainability by separating concerns and distributing the
workload efficiently.
How Three-Tier Architecture Enhances Performance (2 Marks)
Load Distribution – Reduces bottlenecks by distributing processing tasks
5M
across different tiers.
Improved Scalability – Can handle large user bases by adding more
application servers.
Security Enhancement – Sensitive data is managed in the database tier,
keeping it separate from users.
Easier Maintenance & Updates – Modifications can be made in one tier
without affecting others.
Faster Query Processing – Optimized queries in the data tier reduce
application load.
CO2;   B.
Relational Constraints – 2M
SO6;   5M
Impact on data integrity and consistency – 3M
BL2
CO3;   C.
What are Extended ER features (2M)
SO1;   5M
Aggregation
BL4
********** 1 **********
--- page 2 ---
Generalization
Specialization
Union/Category
Examples of any one feature and how they enhance ER model – 3M
CO4;   D.   Definition of Data Warehouse (1 Mark)
SO7;   A Data Warehouse is a centralized repository that stores large volumes of
BL2   structured data from multiple sources, optimized for analytical processing
and decision-making rather than transactional processing.
Key Characteristics (4 Marks)
Subject-Oriented (1 Mark)
Data warehouses are designed to focus on specific business subjects (e.g.,
sales, finance) rather than day-to-day transactions.
Integrated (1 Mark)   5M
Combines data from multiple heterogeneous sources into a unified format
for consistency.
Time-Variant (1 Mark)
Maintains historical data over time, enabling trend analysis and long-term
decision-making.
Non-Volatile (1 Mark)
Once stored, data is not frequently updated or deleted, ensuring stability and
consistency for reporting.
Section B: Attempt Any Four Questions from Questions 2 to 7 (Each Question Carry 20M)
Question 2
CO4;   A.   Indexes in a database improve query performance by enabling faster data
SO1;   retrieval. They reduce the number of rows scanned and enhance search
BL4   efficiency. The main types of indexes include:
Primary Index – Automatically created for primary keys; helps in faster
access.
Unique Index – Ensures that all values in a column are distinct.
Clustered Index – Sorts data physically based on key values; only one per
table.
Non-Clustered Index – Stores a separate structure pointing to actual data;   10M
allows multiple per table.
SQL Example
CREATE UNIQUE INDEX idx_unique_email
ON Customers (Email);
Explanation of Indexing & Its Benefits – 2 Marks
Listing Different Types of Indexes – 2 Marks
********** 2 **********
--- page 3 ---
Correct SQL Query for Unique Index – 1 Mark
CO2;   B.   1. All Students in Computer Science or Electronics course
SO6;
3 Marks
BL5
2. List the names of all students who have a GPA below 3.0.
3 Marks   10M
3. Highest GPA for Female Students in each department
4 Marks
Question 3
CO2;   Introduction to Data Definition Language (DDL) (2 Marks)
SO1;   DDL is used to define, modify, and manage the structure of database objects
BL4   such as tables, indexes, and schemas.
Common DDL commands:
CREATE – Creates database objects (tables, views, indexes).
ALTER – Modifies the structure of an existing database object.
DROP – Deletes database objects.
TRUNCATE – Removes all records from a table without logging individual
row deletions.
2. Example of DDL Commands (2 Marks)
-- Creating a table
CREATE TABLE Employees (
EmpID INT PRIMARY KEY,
Name VARCHAR(100),
Department VARCHAR(50),
A.   Salary DECIMAL(10,2)   10M
);
-- Altering a table (adding a new column)
ALTER TABLE Employees ADD COLUMN Email VARCHAR(100);
-- Dropping a table
DROP TABLE Employees;
Introduction to Data Manipulation Language (DML) (2 Marks)
DML is used to manipulate and retrieve data stored in tables.
Common DML commands:
INSERT – Adds new records into a table.
UPDATE – Modifies existing records.
DELETE – Removes specific records from a table.
Example of DML Commands (2 Marks)
-- Inserting data into Employees table
INSERT INTO Employees (EmpID, Name, Department, Salary)
********** 3 **********
--- page 4 ---
VALUES (1, 'John Doe', 'HR', 50000);
-- Updating a record
UPDATE Employees SET Salary = 55000 WHERE EmpID = 1;
-- Deleting a record
DELETE FROM Employees WHERE EmpID = 1;
Difference Between DDL and DML (2 Marks)
CO4;   1NF – (2M)
SO6;   2NF – (2M)
BL5   3NF – (2M)
B.   Convert Relation R(A, B, C, D, E, F, G) to 3rd normal form – 4M   10M
R1 (A, B, E, F)
R2 (E, C, D)
R3 (F, G)
Question 4
CO3;   A.   Identify the key entities and their attributes. (3M)
SO6;   Product(Product ID, Name, Description, Price, Stock Quantity)
BL6   Category(Category ID, Name (e.g., electronics, clothing, home & kitchen)
Customer(Customer ID, Name, Address, Contact Details)
Order(Order ID, Order Date, Total Price)
Order Item (Order Item ID, Order ID, Product ID, Quantity)
Review(Review ID, Customer ID, Product ID, Review Text, Rating)
Specify the relationships between these entities (3M)   10M
Category - Product: One-to-Many (1:M)
Customer - Order: One-to-Many (1:M)
Order - Order Item: One-to-Many (1:M)
Product - Order Item: One-to-Many (1:M)
Customer - Review: One-to-Many (1:M)
Product - Review: One-to-Many (1:M)
Correct design of Entity-Relationship diagram. (4M)
CO2;   B.   1. Create the Books table with the specified columns and set BookID as the
SO6;   primary key. (3 Marks)
BL6   CREATE TABLE Books (
BookID INT PRIMARY KEY,
Title VARCHAR(255),   10M
Author VARCHAR(100),
Genre VARCHAR(50),
Price DECIMAL(8,2),
Stock INT
********** 4 **********
--- page 5 ---
);
2. Update the stock of a book (identified by BookID) after a customer
places an order. (3 Marks)
UPDATE Books
SET Stock = Stock - 1
WHERE BookID = 101;
3. List customer names and their total number of orders, sorted by the
highest number of orders first. (4 Marks)
SELECT c.Name, COUNT(o.OrderID) AS TotalOrders
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.Name
ORDER BY TotalOrders DESC;
Question 5
CO 4;   A.   Explanation of KDD Process Steps - 4 Marks
SO7;
BL2   Importance of KDD in Decision-Making - 3 Marks
Role of Data Mining in DSS - 3 Marks
Knowledge Discovery in Databases (KDD) Process
The Knowledge Discovery in Databases (KDD) process is a systematic
approach to extracting useful patterns and knowledge from large datasets. It
consists of the following steps:
Data Selection
Data Preprocessing
Data Transformation
Data Mining
Pattern Evaluation   10M
Knowledge Representation
Importance of KDD in Decision-Making
Helps businesses make data-driven decisions based on trends and patterns.
Improves efficiency and accuracy by automating knowledge extraction.
Enhances forecasting and strategic planning in various industries
Supports risk management by detecting fraud and anomalies.
Role of Data Mining in Decision Support Systems (DSS)
Predictive Analysis
Classification and Clustering
Association Rule Mining
Anomaly Detection
CO2;   B.   Consider data in Q.2 (B) and write SQL queries for given questions,
SO7;
BL6   1. Display the names of all students along with the corresponding course   10M
names for each enrollment.
SELECT s.Name AS StudentName, c.CourseName AS CourseName
********** 5 **********
--- page 6 ---
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID;
2. Find the total number of students enrolled in each course.
SELECT c.CourseName, COUNT(e.StudentID) AS TotalStudents
FROM Courses c
LEFT JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseName;
3. Find the names of students who are not enrolled in any courses.
SELECT Name
FROM Students
WHERE StudentID NOT IN (
SELECT StudentID
FROM Enrollments );
4. Find the major that has the highest average GPA.
SELECT Major
FROM Students
GROUP BY Major
HAVING AVG(GPA) = (
SELECT MAX(AverageGPA)
FROM (
SELECT AVG(GPA) AS AverageGPA
FROM Students
GROUP BY Major
) AS AvgGPAByMajor
);
Question 6
CO4;   A.   Functional Dependency (FD) – 2M
SO6;   Any 4 Types of Functional dependencies with examples – 8M
BL4   Full Functional Dependency
Partial Functional Dependency
10M
Transitive Functional Dependency
Trivial Functional Dependency
Multivalued Dependency
CO4;   B.   Define view serializability – 2M
SO6;   Definition and one example
BL6   Check whether the below-given schedule is serializable (6M)   10M
R1(A), W2(A), R3(A), W1(A), W3(A)
A schedule is serializable if the conflict graph is acyclic. our graph
********** 6 **********
--- page 7 ---
forms a cycle (T1 → T3 → T1)
Since there is a cycle in the serialization graph, the schedule is not
serializable.
Question 7
CO1;   A.   Concept of View of Data with Diagram – 3M
SO2;   How does it provide an abstraction – 2M   5M
BL2
CO2;   B. SQL Views with example and use – 2M
SO1;   SQL example (3M)
BL4   CREATE VIEW CustomerOrderView AS
SELECT c.CustomerID, c.Name AS CustomerName, o.OrderID,
5M
o.OrderDate, c.TotalPrice
FROM Customer c
JOIN Order o ON c.CustomerID = o.CustomerID;
CO3;   C.   Entity-Relationship (ER) model – 2M
SO1;   Significance and example – 3M   5M
BL4
CO2;   D. Any three key features of a good relational database – 5M
SO6;   No Redundancy
BL2   No data anomalies   5M
No complex data
********** 7 **********
````
