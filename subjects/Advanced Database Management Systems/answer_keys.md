# Advanced Database Management Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 265624f4eb28

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CS_7055/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: text (11 pages)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2025-2026
Program: B. Tech Stream: IT/COMPS/DS   Year: IV Semester: VII
Subject: Advanced Database Management Systems   Time: 3 hrs (______to_______)
Date:   /   / 2025   No. of Pages: 3
Marks: 100
Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
1) Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A financial institution needs a database structure to accurately track client
investments. The fundamental object in the system is Security, which is defined by
a unique Security ID, its Name, and its current Market Price. Securities are
categorized as either Stock or Bond, though not every Security needs to fall into one
of these two classifications. Furthermore, a Security cannot be both a Stock and a
Bond. Stock entities are detailed with a Ticker Symbol and a Price-to-Earnings
Ratio. Bond entities, conversely, are described by a Maturity Date and a Coupon
Rate. Separately, all Stocks are further broken down into two types: Preferred Stock
CO1.   and Common Stock. Every Stock must be one of these two types, but never both.
[5]
BL- 5   Preferred Stock includes a Dividend Rate, while Common Stock includes a Voting
Rights Flag. The institution also tracks its clients, each identified by a unique Client
ID, an Address, and a Risk Tolerance Level. In the system, every Security must
belong to exactly one Client's portfolio, and a Client must have at least one Security
in their portfolio, although a client will often hold many Securities.
Design EER for above scenario. Draw EER for the above problem statement.
Ans:
Identification of superclass 1 mark, identification of all entities and their
attributes 3 marks and relations 1 mark
1
--- page 2 ---
b.   Apply type constructors to model a Department that has a name, number, manager,
a set of locations, and a set of employees. Specify suitable constructors and justify
briefly.
Ans:
Suitable constructors 2.5 marks and
Justification 2.5 marks
CO2.
Use the object definition format: (OID, constructor, value). Choose:   [5]
BL- 4
 DNAME, DNUMBER → atom (strings/int).
 LOCATIONS → set of OIDs to atomic city objects (no duplicates).
 EMPLOYEES → set of OIDs to EMPLOYEE objects.
 MGR → OID reference to an EMPLOYEE.
Final tuple:
DEPT = (i, tuple, <dname:i₁, dnumber:i₂, mgr:i₃, locations:i₄, employees:i₅>).
c.   Explain the role of replication in distributed databases. How does synchronous
replication ensure consistency compared to asynchronous replication.
Ans:
CO4. BL-2   Role & Benefits of Replication 2.5 marks   [5]
How does synchronous 2.5 marks
Replication keeps multiple copies of the same data on different nodes/sites to
achieve:
2
--- page 3 ---
 High availability & fault tolerance reads/writes can continue after
node/site failures.
   Low-latency access: serve users from geographically closer replicas.
 Load distribution: spread read traffic; isolate analytics from OLTP.
   Disaster recovery: a remote replica shortens RTO/RPO after an outage
In synchronous Client completes only after replica(s) also persist, where as in
Asynchronous replication, Client completes after primary, replicas catch up later
hence synchronous replication is more consistent.
d.   Compare XML Schema and DTD and analyze how XML Schema overcomes the
limitations of DTD in defining structured data.
Ans:
Comparison 2.5 marks
Analyze 2.5 marks
An XML Schema provides a more powerful and flexible way of defining the
structure and constraints of XML documents compared to DTD (Document Type
Definition).
   Data Typing:
o DTD supports only basic text types like #PCDATA, whereas XML
Schema includes strong data types such as xs:string, xs:integer,
CO3.
xs:date, etc.   [5]
BL-2
   Syntax Compatibility:
o XML Schema is written in XML syntax, allowing it to be processed
by standard XML parsers; DTD uses a non-XML syntax, requiring
specialized processors.
   Order and Cardinality:
o XML Schema allows control over element order, repetition
(minOccurs, maxOccurs), and optional elements, giving greater
modeling precision.
 Namespace and Validation:
o XML Schema supports namespaces and hierarchical validation,
making it suitable for complex web applications.
a.   Explain the difference between the Disjoint and Overlapping constraints in a
specialization. If a specialization hierarchy is both Total and Disjoint, what is the
exact number of subclasses that every entity in the superclass must belong to, justify
with example?
Ans:
Q2   Difference 5 marks
[10]
CO1; BL-1   Justification with example 5 marks
An entity in the superclass can belong
An entity in the superclass can belong
to   more   than   one   subclass
to only one subclass.
simultaneously.
Represented by a “d” inside the Represented by an “o” inside the
specialization circle.   specialization circle.
3
--- page 4 ---
In a company, an Employee can be
A Person can be both a Student and an
either a Manager or an Engineer, but
Employee at the same time.
not both.
Mutually exclusive subclasses   Non-mutually exclusive subclasses
Used when subclasses represent distinct Used when subclasses represent roles
categories.   or multiple associations.
   Total Specialization: Every entity in the superclass must belong to at least
one subclass.
   Disjoint Constraint: Each entity can belong to only one subclass.
   If a specialization hierarchy is both Total and Disjoint, then every entity in
the superclass must belong to exactly one subclass.
Example
Consider specialization of Software_Product into Operating_System and
Application:
 The specialization is Total and Disjoint, meaning every Software Product
must be either an Operating System or an Application, but not both. So, each
product belongs to exactly one subclass.
b.   Describe the purpose of each section (DECLARE, BEGIN, EXCEPTION, END) of
a standard PL/SQL block. Design a single PL/SQL block that demonstrates both a
predefined exception (NO_DATA_FOUND) and a user-defined exception.
Ans:
Purpose 5 marks
Design a single PL/SQL block 5 marks
 DECLARE: This optional section is used to declare variables, constants,
Q2
cursors, and user-defined exceptions that will be used in the block.   [10]
CO2; BL-3
 BEGIN: This is the executable section where the main logic of the program
is written. It includes SQL statements and PL/SQL procedural statements.
 EXCEPTION: This optional section handles errors (exceptions) that occur
in the execution section. Both predefined and user-defined exceptions can
be handled here.
 END This section marks the end of the PL/SQL block. Every PL/SQL block
must end with the keyword END;
4
--- page 5 ---
a.   Design an XML schema for an Online Shopping System that manages data for
Customers, Orders, Products, and Payments. Include elements for order details,
product descriptions, and customer information with attributes such as order ID and
payment status.
Q3   Ans:
[10]
CO3, BL-4   Root structure & major modules (2 marks)
Customer information design (2 marks)
Product description design (2 marks)
Order & order details structure (2 marks)
Payment modelling with status (2 marks)
5
--- page 6 ---
b.   Analyze the roles of valid time and transaction time in temporal databases and
evaluate how bitemporal modeling resolves limitations of single-time designs. Use
a brief example from banking or healthcare to show lifecycle tracking of historical
data.
Ans:
Concept of Temporal Databases: (5 Marks)
Example: (5 Marks)
Q3   • Temporal databases store data that changes over time, allowing for historical
[10]
CO4; BL-3   tracking.
Differences:
• Valid Time: When the data is true in the real world.
• Transaction Time: When the data is stored in the database.
• Bitemporal Data: Combines both valid and transaction time to track data changes
and record history.
Example
• Healthcare: Track patient records where valid time represents when symptoms
occurred, and transaction time shows when the records were updated.
a.   Discuss the concept of encapsulation and tell how it is used to create abstract data
types in object-oriented databases with example.
Ans:
It is related to the concepts of ADTs and information hiding (5 Marks)
Object-oriented databases with example (5 Marks)
Q4
[10]
CO3, BL3      For database applications, the requirement that all objects be completely
encapsulated is too strict.
 One way to relax this requirement is to divide the data members into visible
and hidden attributes (or data members)
   Visible attributes may be accessed(read) by high level query languages or
other external operators
6
--- page 7 ---
 Hidden attributes of an object can be accessed only through predefined
operations
 Most OODBMS use high-level query languages for accessing or reading visible
attributes
   Usually operations that update the state of an object are encapsulated.
 One reason for this is that in many OO data models, few integrity constraints are
predefined in the schema
 So each type of object has its integrity constraints programmed into the
methods that create, delete, and update the objects
For example, a BankAccount class defines operations like deposit() and withdraw(),
while the balance attribute remains hidden.
b.   Analyze how the Voting-based concurrency control method enhances fault tolerance
compared to the Primary Site technique in a distributed database system
Ans:
Analyze with explanation 5 marks
how Voting-based concurrency control method enhances fault tolerance 5
marks
   Primary Site method: Entire system halts if the coordinator site fails.
   Voting method: System continues operation, ensuring availability and
Q4
resilience.   [10]
CO4; BL-3
In Voting-based concurrency control, every copy of a data item participates in the
decision-making process. A transaction obtains a lock only when it secures a
majority of votes from all copies. Unlike the Primary Site technique, which depends
on a single coordinator, the voting method avoids single-point failure by distributing
control among multiple sites.
 Even if some sites fail, as long as a majority of votes are obtained,
transactions can proceed.
   Synchronization and lock consistency are maintained across all active
copies.
a.   How inter-query and intra-query parallelism improve performance in large-scale
database environments. Discuss the trade-offs and implementation challenges.
Ans:
How inter-query and intra-query parallelism improve performance 5 marks
Trade-offs 3 marks
Q5
Implementation Example 2 marks   [10]
CO4, BL-3
Parallelism enhances query performance by dividing tasks across multiple
processors, enabling faster data access and improved throughput.
 Types of Parallelism:
o Inter-Query   Parallelism:   Multiple independent   queries run
simultaneously across processors.
7
--- page 8 ---
   Advantage: Increases system throughput; ideal for transaction-
heavy workloads.
o Intra-Query Parallelism: A single complex query is split into parallel
sub-tasks.
   Advantage: Reduces response time for analytical queries.
   Techniques:
   Intra-Operator Parallelism: A single operator (e.g.,
sort, join) runs concurrently.
   Inter-Operator Parallelism: Multiple operators (e.g.,
select and join) run in a pipelined manner.
   Trade-offs: 3 marks
o High overhead in synchronizing parallel tasks.
o Load imbalance due to skewed data distribution.
o Communication overhead between processors.
 Implementation Example: 2 marks
A data warehouse query performing joins and aggregations can use intra-
query parallelism, where each processor joins a subset of data before merging
results.
b. A university course management system maintains records of courses, students, and
their prerequisites. Each course has attributes such as courseCode, courseTitle,
creditHours, and description. Students have attributes including studentID, name,
email, and major. A student can enroll in multiple courses, but certain courses have
prerequisites that must be completed before enrollment. The system also tracks the
semester in which the student enrolls in a course. Instructions: Develop an ODL
schema for the university course management system.
Ans:
Identifying all classes 3 marks
Identifying all attributes 3 marks
Managing relationships/sets (proper Cardinality) 4 marks
Q5
[10]
CO3;BL-4   class Course {
( extent courses)
attribute string courseCode;
attribute string courseTitle;
attribute short creditHours;
attribute string description;
relationship set Course has_prereqs inverse Course::is_prereq_for;
relationship set Enrollment offered_in inverse Enrollment::enrolled_courses;
};
class Student {
( extent students)
attribute string studentID;
attribute string name;
8
--- page 9 ---
attribute string email;
attribute string major;
relationship set Enrollment enrollments inverse Enrollment::enrolled_by;
};
class Enrollment {
( extent enrollments)
attribute Date enrollmentDate;
relationship Course enrolled_courses inverse Enrollment::offered_in;
relationship Student enrolled_by inverse Enrollment::enrollments;
};
a.   . What are key features of NoSQL? In which situation will NoSQL database not be
suitable to implement?
Ans:
Key Features: 5 marks
Situation based example 5 marks
   Flexible schemas
   Horizontal scaling
   Fast queries due to the data model
 Ease of use for developers
Q6
[10]
CO4; BL-3   If you are required to perform complex and dynamic querying and reporting, then
you should avoid using NoSQL as it has a limited query functionality. For such
requirements, you should prefer SQL only.
NoSQL also lacks in the ability to perform dynamic operations. It can’t guarantee
ACID properties. In such cases like financial transactions, etc., you may go with
SQL databases.
You should also avoid NoSQL if your application needs run-time flexibility.
If consistency is a must and if there aren’t going to be any large-scale changes in
terms of the data volume, then going with the SQL database is a better option.
One should also keep in mind that NoSQL databases won’t support structured query
language. The querying language may vary from one database to another.
b.   Sample Clerk table (CL_ID, First_name, Department_name, Salary, Designation)
Create a PL/SQL procedure called percentage_salary to update Clerks data
 The procedure has two parameters: IN_CL_ID and IN_PERCENT.
 The procedure adjusts the salary of a particular Clerk specified the
IN_CL_ID by a given percentage IN_PERCENT. (salary + salary *
Q6
in_percent / 100)   [10]
CO2, BL-4
   In the procedure body, we use the UPDATE statement to update the salary
information.
   Test the procedure with CL_ID = 175 and IN_PERCENT = 10%
Ans:
Parameter declaration 2 marks
9
--- page 10 ---
Logic implementation 4 marks
SQL statement for update 2 marks
Test the procedure 2 marks
Clerk table (CL_ID, First_name, Department_name, Salary, Designation)
CREATE OR REPLACE PROCEDURE adjust_salary(
in_CL_ID IN Clerk.CL_ID%TYPE,
in_percent IN NUMBER
) IS
BEGIN
-- update Clerk 's salary
UPDATE Clerk
SET salary = salary + salary * in_percent / 100
WHERE CL_ID = in_CL_id;
END;
a.   Explain the Active Database concepts in detail. Discuss the Event-Condition-Action
(ECA) model, its components, and how it enhances traditional database systems.
Give suitable examples of real-world applications where Active Databases are
beneficial.
Ans:
Active Database concepts 3 Marks
Event-Condition-Action (ECA) model 3 Marks
suitable examples 4 Marks
Active DBMS reacts automatically to specified situations.
Rules (triggers) are stored in the catalogue and managed like other schema objects.
Granularity: Statement-level vs row-level firing.
Timing: BEFORE, AFTER, or INSTEAD OF the triggering event.
Q7
ECA Components   [10]
CO4; BL-3
When the Event occurs and Condition is true, execute the Action
   Event:
o Database modification E.g., (insert, delete, update),
   Condition:
o Any true/false expression
   Action:
o Sequence of SQL statements that will be automatically executed
How It Enhance Traditional DBs
   Proactive enforcement:
   Timeliness:
   Consistency & reuse:
   Automation
10
--- page 11 ---
b.   Explain issues in RDBMS such as impedance mismatch, schema inflexibility, and
scalability limitations. Suggest suitable database that can overcome these
challenges and justify your reasoning with examples.
Ans:
Issues: 5 marks
Suitable database 2 marks
Justify : 3 marks
Strengths
1. Structured Storage: Data stored in tables (rows & columns) with clear
relationships.
2. ACID Properties: Ensures data consistency, reliability, and integrity.
3. Query Flexibility: SQL supports complex joins, filters, and aggregations.
4. Schema Safety: Enforces data types, primary/foreign keys, and constraints.
5. Maturity: Long-standing, stable technology with wide tool and vendor
support.
Q7
Weaknesses   [10]
CO4; BL-3
1. Impedance Mismatch: Difficult mapping between object-oriented
code and tables.
2. Schema Inflexibility: Hard to modify structure once database is in
production.
3. Limited Scalability: Supports vertical scaling, but poor horizontal
scaling.
4. Performance Issues: Multiple joins in normalized tables slow down
queries.
5. Not Suitable for Complex Domains: Inefficient for graph or nested data
models.
Alternatives
 Document Databases (MongoDB): Schema-less, handles nested objects
easily.
 Graph Databases (Neo4j): Best for highly connected data (networks).
 Column/Key-Value Stores: High performance and scalability for large
data.
11
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 8ce3b6023510

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIML_7053/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/MBA Tech (DS)
Year: III / IV/Semester VI/Semester VIII(Exam Year: 2025-2026)
Subject: Advanced Database Management Systems
Date: 14 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a. A shared subclass is a subclass that has more than one superclass.
It inherits properties from multiple parent classes, which is a form of
multiple inheritance in object-oriented databases or ER modelling
CO-1;
SO-1;   [5]
BL-2
StarModel is shared subclass it inherits properties from MovieStar and
Model
[explanation-2.5 M, example-2,5M]
********** 1 **********
--- page 2 ---
b   Ans: Suitable Constructors (2.5 M) + Justification (2.5 M)   [5]
Use object definition format: (OID, constructor, value)
Choose:
CO-2;
• LIB_NAME → atom (string)
SO-1;
• LIBRARIAN → OID reference to a LIBRARIAN object
BL-2
• BOOKS → set of OIDs to BOOK objects (no duplicates)
• MEMBERS → set of OIDs to MEMBER objects
Final Tuple:
LIBRARY = (i, tuple, <lib_name:i₁, librarian:i₂, books:i₃, members:i₄>)
c   Explain the advantages of parallel database systems   [5]
Answer
Advantages:
1. Improved Performance (Speedup)
o Queries execute faster due to parallel processing.
CO-2;   2. Scalability
SO-1;   o System can grow by adding more processors or disks.
BL-2   3. High Throughput
o Multiple queries can be processed at the same time.
4. Fault Tolerance
o Failure of one node does not stop the entire system.
5. Efficient Resource Utilization
o CPU, memory, and disk resources are used effectively.
d   Well-Formed XML   [5]
 It must start with an XML declaration to indicate the version of XML
being used—as well as any other relevant attributes.
 It must follow the syntactic guidelines of the tree model.
 XML documents must have a root element
 XML elements must have a closing tag
 XML tags are case sensitive
CO-3;    XML elements must be properly nested
SO-1;
 XML attribute values must be quoted
BL-2
(2 marks)
Valid XML
 A valid XML document is not only well-formed but also adheres to a
defined structure or set of rules specified by a Document Type Definition
(DTD) or an XML Schema (XSD). This type ensures that the content and
structure of the document conform to the defined rules, making it more
reliable for applications that require structured data.
********** 2 **********
--- page 3 ---
 Key Characteristics:
•   It follows the rules of well-formed XML.
•   It references a DTD or XML Schema.
•   Elements, attributes, and their values must conform to the defined structure.
(3 marks)
a. A trigger is a database object that is automatically executed or fired when
a   specified   event   occurs   on   a   table   or   view.
These events include INSERT, UPDATE, or DELETE operations.
Statement-Level Trigger   Row-Level Trigger
Executes once for the entire SQL Executes once for each
statement   row affected
Used when action does not   Used when action
depend on individual rows   depends on each row
Slower (multiple
Q2   Faster (less execution)
executions)
CO-3;   Does not use FOR EACH ROW Uses FOR EACH ROW   [10]
SO-1;
BL-3   Validating each row’s
Logging updates
data
CREATE OR REPLACE TRIGGER prevent_salary_reduction
BEFORE UPDATE OF Salary ON EMP
FOR EACH ROW
BEGIN
IF :NEW.Salary < :OLD.Salary THEN
RAISE_APPLICATION_ERROR(-20001, 'Salary cannot be reduced');
END IF;
END;
/
[what is trigger-2M,Difference 4M, trigger code- 4M]
b.   (Implementation – 5 marks)   [10]
// Enable sharding on database
sh.enableSharding("bankDB")
// Select database
use bankDB
// Shard the collection using customer_id as shard key
Q2
sh.shardCollection("bankDB.customers", { customer_id: 1 })
CO-4;
SO-1;   // Insert sample data
BL-1,4   db.customers.insertMany([
{ customer_id: 1, name: "Amit", city: "Mumbai", balance: 5000 },
{ customer_id: 2, name: "Neha", city: "Delhi", balance: 7000 },
{ customer_id: 3, name: "Raj", city: "Pune", balance: 6000 }
])
(Explanation – 5 marks)
•   Sharding distributes data across multiple servers (shards) using a shard key
(customer_id).
********** 3 **********
--- page 4 ---
• MongoDB divides data into chunks and distributes them evenly, ensuring
load balancing.
•   This improves scalability and performance for large datasets in distributed
environments.
a.   [10]
Q3
CO-1,2;
SO-1;
BL-2,4
Identifying object- 2M
Identifying reference 2M
All diagrammatic representation-6M
b.   Diagram   [10]
Q3
CO-1,2;
SO-1;
BL-1,2
• Shared Nothing
********** 4 **********
--- page 5 ---
Each node is completely independent.
Advantages:
High scalability
No resource contention
Best performance for large systems
Limitations:
Complex query processing
Data distribution challenges
• Shared memory
All processors share common memory and disk.
Advantages:
Easy communication between processors
Simple design
Limitations:
Memory contention
Limited scalability
• Shared Disk
Each processor has its own memory, but disks are shared.
Advantages:
High availability
Easy data access
Limitations:
Disk contention
Synchronization overhead
[diagram -4M,Each architecture with advantages an dlimitation-
2M*3=6M]
a.   (Tree Diagram – 5 marks)   [10]
university
├── course (course_id="CSE101")
│ ├── name → DBMS
│ ├── faculty
│ │ ├── first_name → Raj
│ │ └── last_name → Mehta
Q4
│ └── credits → 4
CO-3;
SO-1;   └── course (course_id="CSE102")
BL-1,4
├── name → AI
├── faculty
│ ├── first_name → Anita
│ └── last_name → Patel
└── credits → 3
(Theory – 5 marks)
•   Attributes provide additional information about elements (e.g., course_id).
********** 5 **********
--- page 6 ---
• They help uniquely identify elements and store metadata without affecting
the hierarchical structure.
b.   Active databases automatically respond to events using ECA rules. An event triggers [10]
a condition check, and if true, an action is executed. (2 marks)
Design and Implementation Issues:- (6 Marks)
 An active database allows users to make the following changes to triggers
(rules)
 Activate
 Deactivate
 Drop
 An event can be considered in 3 ways
 Immediate consideration
 Deferred consideration
 Detached consideration
Q4
 Immediate consideration
CO-4;
SO-1;    Part of the same transaction and can be one of the following
BL-1,2
depending on the situation
 Evaluate the condition before executing the triggering event.
 Evaluate the condition after executing the triggering event.
 Evaluate the condition instead of executing the triggering
event.
 Deferred consideration
 Condition is evaluated at the end of the transaction
 Detached consideration
 Condition is evaluated in a separate transaction
Example: On inserting a record (event), if stock < threshold (condition), generate alert
(action). These rules enable automation and real-time responses. (2 marks)
a.   While most databases tend to model reality at a point in time (at the “current''   [10]
time), temporal databases model the states of the real world across time. it offers
temporal data types and stores information relating to past, present and future time.
Facts in temporal relations have associated times when they are valid, which can be
Q5   represented as a union of intervals.
CO-4;   The transaction time for a fact is the time interval during which the fact is current
SO-1;
BL-1,2   within the database system.
In a temporal relation, each tuple has an associated time when it is true; the time
may be either valid time or transaction time.
A bi-temporal relation stores both valid and transaction time.
. (5 marks)
********** 6 **********
--- page 7 ---
Incorporating Time in Relational Databases
Using Tuple Versioning
 Add to every tuple
 Valid start time
 Valid end time
 Using Transaction Time Relations.
 In a transaction time database, whenever a change is applied to the
database, the actual timestamp of the transaction that applied the
change (insert, delete, or update) is recorded. Draw diagram also (5
marks)
b. NoSQL databases are non-relational databases designed to handle large volumes of [10]
semi-structured or unstructured data. They store data in flexible formats such as key-
value, document, column, or graph models. MongoDB is a document-based NoSQL
Q5   database that stores data in JSON-like (BSON) format. (5 marks)
CO-4;   Key characteristics include schema-less design, horizontal scalability, high
SO-1;
BL-1,4   availability, and BASE properties (eventual consistency). MongoDB allows flexible
schema and efficient handling of large-scale distributed data, making it suitable for
modern web applications. (5 marks)
Elaborate both above points
a.   [10]
Q6
CO-1;
SO-1;
BL-6
[Diagram-identifying entities, attributes, relationship-6M]
Relational schema[4M]
USER(User_ID, Name, Email, Phone)
CUSTOMER(User_ID, Shipping_Address)
********** 7 **********
--- page 8 ---
SELLER(User_ID, Store_Name, GST_Number)
PRODUCT(Product_ID, Product_Name, Price)
ELECTRONICS(Product_ID, Warranty_Period, Brand)
CLOTHING(Product_ID, Size, Material)
ORDERS(Order_ID, Order_Date, User_ID)
ORDER_PRODUCT(Order_ID, Product_ID)
SELLER_PRODUCT(User_ID, Product_ID)
b.   [10]
Consider table EMP(emp_id, emp_name, salary)
DECLARE
CURSOR emp_cursor
IS
SELECT emp_name FROM EMP;
v_name EMP.emp_name%TYPE;
BEGIN
OPEN emp_cursor;
Q6
LOOP
CO-3;   FETCH emp_cursor INTO v_name;
SO-1;
BL-3
EXIT WHEN emp_cursor%NOTFOUND;
DBMS_OUTPUT.PUT_LINE('Employee Name: ' || v_name);
END LOOP;
DBMS_OUTPUT.PUT_LINE('Total Records Processed: ' ||
emp_cursor%ROWCOUNT);
CLOSE emp_cursor;
END;
/
[Concept of Explicit Cursor -3M, Use of %ROWCOUNT - 2 M,
Correct PL/SQL Program- 5 M]
a.   (Explanation of Techniques – 5 marks)   [10]
• Round-robin Partitioning:
Data is distributed sequentially across partitions in a cyclic manner. Each
new record is placed in the next partition. This ensures uniform data
distribution without considering data values.
• Hash Partitioning:
Q7
A hash function is applied to a partitioning key (e.g., ID), and the result
CO-1,2;
SO-1;   determines the partition. This provides balanced distribution and is
BL-1,2
independent of data order.
• Range Partitioning:
Data is divided based on value ranges of a key attribute (e.g., date or
salary). Each partition stores records within a specific range. It preserves
ordering of data.
(Advantages – 5 marks)
********** 8 **********
--- page 9 ---
• Round-robin:
Ensures equal distribution of data and load balancing, simple to implement.
• Hash Partitioning:
Provides efficient data distribution and fast access for equality-based
queries.
• Range Partitioning:
Suitable for range queries, improves query performance when accessing
ordered data.
b.   Persistence by Naming and Persistence by Reachability are the two   [10]
primary mechanisms used in Object-Oriented Database Management
Systems (OODBMS) to make objects persistent (i.e., stored permanently
in the database so they survive after the program terminates).
• Naming Mechanism: Assign an object a unique persistent name
through which it can be retrieved by this and other programs.
•   Reachability Mechanism: Make the object reachable from some
persistent object.
• An object B is said to be reachable from an object A if a sequence
of references in the object graph lead from object A to object B.
Naming example
define class BookSet:
type set(Book);
operations
add_book(b: Book): boolean;
remove_book(b: Book): boolean;
Q7
end BookSet;
CO-1,2;
SO-1;   ...
BL-2,4   persistent name AllBooks: BookSet;
(* AllBooks is a persistent named object of type BookSet *)
Rechability example
define class Library:
type tuple (books: set(Book));
end Library;
...
persistent name CentralLibrary: Library;
(* CentralLibrary is a persistent object *)
...
b1 := create_book;
b2 := create_book;
...
********** 9 **********
--- page 10 ---
CentralLibrary.books := {b1, b2};
[Naming explanation wit example 5 M
Reachability explanation wit example 5 M]
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper ca9cc19a274f

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_DS_7009/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (DS)/B. Tech (IT)/MBA Tech (IT)
Year: III / IV/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Advanced Database Management Systems
Date: 04 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A financial institution needs a database structure to accurately track client
investments. The fundamental object in the system is Security, which is defined
by a unique Security ID, its Name, and its current Market Price. Securities are
categorized as either Stock or Bond, though not every Security needs to fall into
one of these two classifications. Furthermore, a Security cannot be both a Stock
and a Bond. Stock entities are detailed with a Ticker Symbol and a Price-to-
Earnings Ratio. Bond entities, conversely, are described by a Maturity Date and
a Coupon Rate. Separately, all Stocks are further broken down into two types:
CO1.
Preferred Stock and Common Stock. Every Stock must be one of these two types,   [5]
BL- 5
but never both. Preferred Stock includes a Dividend Rate, while Common Stock
includes a Voting Rights Flag. The institution also tracks its clients, each
identified by a unique Client ID, an Address, and a Risk Tolerance Level. In the
system, every Security must belong to exactly one Client's portfolio, and a Client
must have at least one Security in their portfolio, although a client will often hold
many Securities.
Design EER for above scenario. Draw EER for the above problem statement.
Ans:
********** 1 **********
--- page 2 ---
b.   Apply type constructors to model a Department that has a name, number,
manager, a set of locations, and a set of employees. Specify suitable constructors
and justify briefly.
Ans:
Use the object definition format: (OID, constructor, value). Choose:
CO2.
• DNAME, DNUMBER → atom (strings/int).   [5]
BL- 4
• LOCATIONS → set of OIDs to atomic city objects (no duplicates).
• EMPLOYEES → set of OIDs to EMPLOYEE objects.
• MGR → OID reference to an EMPLOYEE.
Final tuple:
DEPT = (i, tuple, <dname:i₁, dnumber:i₂, mgr:i₃, locations:i₄, employees:i₅>).
c.   Explain the role of replication in distributed databases. How does synchronous
replication ensure consistency compared to asynchronous replication.
Ans:
Role & Benefits of Replication
Replication keeps multiple copies of the same data on different nodes/sites to
achieve:
• High availability & fault tolerance reads/writes can continue after
CO4. BL-2   [5]
node/site failures.
• Low-latency access: serve users from geographically closer replicas.
• Load distribution: spread read traffic; isolate analytics from OLTP.
•   Disaster recovery: a remote replica shortens RTO/RPO after an outage
In synchronous Client completes only after replica(s) also persist, where as in
Asynchronous replication, Client completes after primary, replicas catch up
later hence synchronous replication is more consistent.
d.   Compare XML Schema and DTD and analyze how XML Schema overcomes the
limitations of DTD in defining structured data.
CO3.   Ans:
[5]
BL-2   An XML Schema provides a more powerful and flexible way of defining the
structure and constraints of XML documents compared to DTD (Document Type
Definition).
********** 2 **********
--- page 3 ---
• Data Typing:
o DTD supports only basic text types like #PCDATA, whereas
XML Schema includes strong data types such as xs:string,
xs:integer, xs:date, etc.
•   Syntax Compatibility:
o XML Schema is written in XML syntax, allowing it to be
processed by standard XML parsers; DTD uses a non-XML
syntax, requiring specialized processors.
•   Order and Cardinality:
o XML Schema allows control over element order, repetition
(minOccurs, maxOccurs), and optional elements, giving greater
modeling precision.
• Namespace and Validation:
o XML Schema supports namespaces and hierarchical validation,
making it suitable for complex web applications.
a.   Explain the difference between the Disjoint and Overlapping constraints in a
specialization. If a specialization hierarchy is both Total and Disjoint, what is the
exact number of subclasses that every entity in the superclass must belong to,
justify with example?
Ans:
An entity in the superclass can
An entity in the superclass can belong
belong to more than one subclass
to only one subclass.
simultaneously.
Represented by a “d” inside the Represented by an “o” inside the
specialization circle.   specialization circle.
In a company, an Employee can be
A Person can be both a Student and
either a Manager or an Engineer, but
an Employee at the same time.
not both.
Q2
Mutually exclusive subclasses   Non-mutually exclusive subclasses   [10]
CO1; BL-1
Used when   subclasses   represent Used when subclasses represent
distinct categories.   roles or multiple associations.
•   Total Specialization: Every entity in the superclass must belong to at least
one subclass.
•   Disjoint Constraint: Each entity can belong to only one subclass.
•   If a specialization hierarchy is both Total and Disjoint, then every entity
in the superclass must belong to exactly one subclass.
Example
Consider specialization of Software_Product into Operating_System and
Application:
• The specialization is Total and Disjoint, meaning every Software Product
must be either an Operating System or an Application, but not both. So,
each product belongs to exactly one subclass.
b.   Describe the purpose of each section (DECLARE, BEGIN, EXCEPTION, END)
of a standard PL/SQL block. Design a single PL/SQL block that demonstrates
Q2   both a predefined exception (NO_DATA_FOUND) and a user-defined exception.
[10]
CO2; BL-3   Ans:
• DECLARE: This optional section is used to declare variables, constants,
cursors, and user-defined exceptions that will be used in the block.
********** 3 **********
--- page 4 ---
• BEGIN: This is the executable section where the main logic of the
program is written. It includes SQL statements and PL/SQL procedural
statements.
• EXCEPTION: This optional section handles errors (exceptions) that
occur in the execution section. Both predefined and user-defined
exceptions can be handled here.
• END This section marks the end of the PL/SQL block. Every PL/SQL
block must end with the keyword END;
a.   Design an XML schema for an Online Shopping System that manages data for
Customers, Orders, Products, and Payments. Include elements for order details,
Q3
product descriptions, and customer information with attributes such as order ID [10]
CO3, BL-4
and payment status.
Ans:
********** 4 **********
--- page 5 ---
b.   Analyze the roles of valid time and transaction time in temporal databases and
evaluate how bitemporal modeling resolves limitations of single-time designs.
Use a brief example from banking or healthcare to show lifecycle tracking of
historical data.
Ans:
Concept of Temporal Databases:
• Temporal databases store data that changes over time, allowing for historical
Q3   tracking.
[10]
CO4; BL-3   Differences:
• Valid Time: When the data is true in the real world.
• Transaction Time: When the data is stored in the database.
• Bitemporal Data: Combines both valid and transaction time to track data
changes and record history.
Example:
• Healthcare: Track patient records where valid time represents when symptoms
occurred, and transaction time shows when the records were updated.
a.   Discuss the concept of encapsulation and tell how it is used to create abstract data
types in object-oriented databases with example.
Ans:
It is related to the concepts of ADTs and information hiding
• For database applications, the requirement that all objects be completely
encapsulated is too strict.
• One way to relax this requirement is to divide the data members into
visible and hidden attributes (or data members)
•   Visible attributes may be accessed(read) by high level query languages or
Q4   other external operators
[10]
CO3, BL3   • Hidden attributes of an object can be accessed only through predefined
operations
• Most OODBMS use high-level query languages for accessing or reading
visible attributes
•   Usually operations that update the state of an object are encapsulated.
• One reason for this is that in many OO data models, few integrity constraints
are predefined in the schema
• So each type of object has its integrity constraints programmed into the
methods that create, delete, and update the objects
Q4   b.   Analyze how the Voting-based concurrency control method enhances fault
[10]
CO4; BL-3   tolerance compared to the Primary Site technique in a distributed database system
********** 5 **********
--- page 6 ---
Ans:
• Primary Site method: Entire system halts if the coordinator site fails.
• Voting method: System continues operation, ensuring availability and
resilience.
In Voting-based concurrency control, every copy of a data item participates in
the decision-making process. A transaction obtains a lock only when it secures a
majority of votes from all copies. Unlike the Primary Site technique, which
depends on a single coordinator, the voting method avoids single-point failure by
distributing control among multiple sites.
Enhanced Fault Tolerance:
• Even if some sites fail, as long as a majority of votes are obtained,
transactions can proceed.
•   Synchronization and lock consistency are maintained across all active
copies.
a. How inter-query and intra-query parallelism improve performance in large-
scale database environments. Discuss the trade-offs and implementation
challenges.
Ans:
Parallelism enhances query performance by dividing tasks across multiple
processors, enabling faster data access and improved throughput.
• Types of Parallelism:
o Inter-Query Parallelism: Multiple independent queries run
simultaneously across processors.
▪   Advantage:   Increases system   throughput;   ideal   for
transaction-heavy workloads.
o Intra-Query Parallelism: A single complex query is split into
parallel sub-tasks.
Q5
▪   Advantage: Reduces response time for analytical queries.   [10]
CO4, BL-3
▪   Techniques:
▪ Intra-Operator Parallelism: A single operator (e.g.,
sort, join) runs concurrently.
▪   Inter-Operator Parallelism: Multiple operators
(e.g., select and join) run in a pipelined manner.
•   Trade-offs:
o High overhead in synchronizing parallel tasks.
o Load imbalance due to skewed data distribution.
o Communication overhead between processors.
• Implementation Example:
A data warehouse query performing joins and aggregations can use intra-
query parallelism, where each processor joins a subset of data before
merging results.
b. A university course management system maintains records of courses, students,
and their prerequisites. Each course has attributes such as courseCode,
courseTitle, creditHours, and description. Students have attributes including
studentID, name, email, and major. A student can enroll in multiple courses, but
Q5
certain courses have prerequisites that must be completed before enrollment. The [10]
CO3;BL-4
system also tracks the semester in which the student enrolls in a course.
Instructions: Develop an ODL schema for the university course management
system.
Ans:
********** 6 **********
--- page 7 ---
class Course {
( extent courses)
attribute string courseCode;
attribute string courseTitle;
attribute short creditHours;
attribute string description;
relationship set Course has_prereqs inverse Course::is_prereq_for;
relationship set Enrollment offered_in inverse Enrollment::enrolled_courses;
};
class Student {
( extent students)
attribute string studentID;
attribute string name;
attribute string email;
attribute string major;
relationship set Enrollment enrollments inverse Enrollment::enrolled_by;
};
class Enrollment {
( extent enrollments)
attribute Date enrollmentDate;
relationship Course enrolled_courses inverse Enrollment::offered_in;
relationship Student enrolled_by inverse Enrollment::enrollments;
};
a.   . What are key features of NoSQL? In which situation will NoSQL database not
be suitable to implement?
Ans:
Key Features:
•   Flexible schemas
•   Horizontal scaling
•   Fast queries due to the data model
• Ease of use for developers
If you are required to perform complex and dynamic querying and reporting, then
Q6
you should avoid using NoSQL as it has a limited query functionality. For such [10]
CO4; BL-3
requirements, you should prefer SQL only.
NoSQL also lacks in the ability to perform dynamic operations. It can’t guarantee
ACID properties. In such cases like financial transactions, etc., you may go with
SQL databases.
You should also avoid NoSQL if your application needs run-time flexibility.
If consistency is a must and if there aren’t going to be any large-scale changes in
terms of the data volume, then going with the SQL database is a better option.
One should also keep in mind that NoSQL databases won’t support structured
query language. The querying language may vary from one database to another.
b.   Sample Clerk   table (CL_ID,   First_name, Department_name,   Salary,
Designation)
Create a PL/SQL procedure called percentage_salary to update Clerks data
Q6
• The procedure has two parameters: IN_CL_ID and IN_PERCENT.   [10]
CO2, BL-4
• The procedure adjusts the salary of a particular Clerk specified the
IN_CL_ID by a given percentage IN_PERCENT. (salary + salary *
in_percent / 100)
********** 7 **********
--- page 8 ---
•   In the procedure body, we use the UPDATE statement to update the
salary information.
•   Test the procedure with CL_ID = 175 and IN_PERCENT = 10%
Ans:
CREATE OR REPLACE PROCEDURE adjust_salary(
in_employee_id IN EMPLOYEES.EMPLOYEE_ID%TYPE,
in_percent IN NUMBER
) IS
BEGIN
-- update employee's salary
UPDATE employees
SET salary = salary + salary * in_percent / 100
WHERE employee_id = in_employee_id;
END;
a.   Explain the Active Database concepts in detail. Discuss the Event-Condition-
Action (ECA) model, its components, and how it enhances traditional database
systems. Give suitable examples of real-world applications where Active
Databases are beneficial.
Ans:
Active DBMS reacts automatically to specified situations.
Rules (triggers) are stored in the catalogue and managed like other schema
objects.
Granularity: Statement-level vs row-level firing.
Timing: BEFORE, AFTER, or INSTEAD OF the triggering event.
ECA Components
Q7   When the Event occurs and Condition is true, execute the Action
[10]
CO4; BL-3   • Event:
o Database modification E.g., (insert, delete, update),
• Condition:
o Any true/false expression
•   Action:
o Sequence of SQL statements that will be automatically executed
How It Enhance Traditional DBs
•   Proactive enforcement:
•   Timeliness:
•   Consistency & reuse:
• Automation
b.   Explain issues in RDBMS such as impedance mismatch, schema inflexibility,
and scalability limitations. Suggest suitable database that can overcome these
challenges and justify your reasoning with examples.
Ans:
Strengths
Q7   1. Structured Storage: Data stored in tables (rows & columns) with clear
[10]
CO4; BL-3   relationships.
2. ACID Properties: Ensures data consistency, reliability, and integrity.
3. Query   Flexibility: SQL   supports complex   joins,   filters, and
aggregations.
4. Schema Safety: Enforces data types, primary/foreign keys, and
constraints.
********** 8 **********
--- page 9 ---
5. Maturity: Long-standing, stable technology with wide tool and vendor
support.
Weaknesses
1. Impedance Mismatch: Difficult mapping between object-oriented
code and tables.
2. Schema Inflexibility: Hard to modify structure once database is in
production.
3. Limited Scalability: Supports vertical scaling, but poor horizontal
scaling.
4. Performance Issues: Multiple joins in normalized tables slow down
queries.
5. Not Suitable for Complex Domains: Inefficient for graph or nested data
models.
Alternatives
• Document Databases (MongoDB): Schema-less, handles nested objects
easily.
• Graph Databases (Neo4j): Best for highly connected data (networks).
• Column/Key-Value Stores: High performance and scalability for large
data.
********** 9 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 3f061c11bb42

- Departments: Information Technology
- Programmes: BTech IT 7001, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_IT_7001/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.docx` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: docx (1 page)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025
|
Program: B. Tech   Stream: IT/COMPS/DS
| Year: IV Semester: VII
|
Subject: Advanced Database Management Systems
| Time: 3 hrs (______to_______)
|
Date:   /   / 2024
| No. of Pages: 3
|
Marks: 100
|
|
Final Examination
|
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Q1

|
| Answer briefly:
| [20]
|
CO1.
BL- 5
| a.
| A financial institution needs a database structure to accurately track client investments. The fundamental object in the system is Security, which is defined by a unique Security ID, its Name, and its current Market Price. Securities are categorized as either Stock or Bond, though not every Security needs to fall into one of these two classifications. Furthermore, a Security cannot be both a Stock and a Bond. Stock entities are detailed with a Ticker Symbol and a Price-to-Earnings Ratio. Bond entities, conversely, are described by a Maturity Date and a Coupon Rate. Separately, all Stocks are further broken down into two types: Preferred Stock and Common Stock. Every Stock must be one of these two types, but never both. Preferred Stock includes a Dividend Rate, while Common Stock includes a Voting Rights Flag. The institution also tracks its clients, each identified by a unique Client ID, an Address, and a Risk Tolerance Level. In the system, every Security must belong to exactly one Client's portfolio, and a Client must have at least one Security in their portfolio, although a client will often hold many Securities.
Design EER for above scenario. Draw EER for the above problem statement.
Ans:
Identification of superclass 1 mark, identification of all entities and their attributes 3 marks and relations 1 mark

| [5]
|
CO2.
BL- 4
| b.
| Apply type constructors to model a Department that has a name, number, manager, a set of locations, and a set of employees. Specify suitable constructors and justify briefly.
Ans:
Suitable constructors 2.5 marks and
Justification 2.5 marks
Use the object   definition format: (OID, constructor, value). Choose:
DNAME, DNUMBER → atom (strings/int).
LOCATIONS → set of OIDs to atomic city objects (no duplicates).
EMPLOYEES → set of OIDs to EMPLOYEE objects.
MGR → OID reference to an EMPLOYEE.
Final tuple:
DEPT = (i, tuple, <dname:i₁, dnumber:i₂, mgr:i₃, locations:i₄, employees:i₅>).
| [5]
|
CO4. BL-2
| c.
| Explain   the role of replication in distributed databases. How does synchronous replication ensure consistency compared to asynchronous replication.
Ans:
Role & Benefits of Replication 2.5 marks
How does synchronous 2.5 marks
Replication keeps multiple copies of the same data on different nodes/sites to achieve:
High availability & fault tolerance reads/writes can continue after node/site failures.
Low-latency access: serve users from geographically closer replicas.
Load distribution: spread read traffic; isolate analytics from OLTP.
Disaster recovery: a remote replica shortens RTO/RPO after an outage
In synchronous Client completes only after replica(s) also persist, where as in Asynchronous replication, Client completes after primary, replicas catch up later hence synchronous replication is more consistent.
| [5]
|
CO3.
BL-2
| d.
| Compare XML Schema and DTD and analyze how XML Schema overcomes the limitations of DTD in defining structured data.
Ans:
Comparison 2.5 marks
Analyze 2.5 marks
An XML Schema provides a more powerful and flexible way of defining the structure and constraints of XML documents compared to DTD (Document Type Definition).
Data Typing:
DTD supports only basic text types like #PCDATA, whereas XML Schema includes strong data types such as xs:string, xs:integer, xs:date, etc.
Syntax Compatibility:
XML Schema is written in XML syntax, allowing it to be processed by standard XML parsers; DTD uses a non-XML syntax, requiring specialized processors.
Order and Cardinality:
XML Schema allows control over element order, repetition (minOccurs, maxOccurs), and optional elements, giving greater modeling precision.
Namespace and Validation:
XML Schema supports namespaces and hierarchical validation, making it suitable for complex web applications.
| [5]
|
Q2
CO1; BL-1
| a.
| Explain the difference between the Disjoint and Overlapping   constraints in a specialization. If a specialization hierarchy is both Total and Disjoint, what is the exact number of subclasses that every entity in the superclass must belong to, justify with example?
Ans:
Difference 5 marks
Justification with example 5 marks
An entity in the superclass can belong to only one subclass.
| An entity in the superclass can belong to more than one subclass simultaneously.
|
Represented by a “d” inside the specialization circle.
| Represented by an “o” inside the specialization circle.
|
In a company, an Employee can be either a Manager or an Engineer, but not both.
| A Person can be both a Student and an Employee at the same time.
|
Mutually exclusive subclasses
| Non-mutually exclusive subclasses
|
Used when subclasses represent distinct categories.
| Used when subclasses represent roles or multiple associations.
|
Total Specialization: Every entity in the superclass must belong to at least one subclass.
Disjoint Constraint: Each entity can belong to only one subclass.
If a specialization hierarchy is both Total and Disjoint, then every entity in the superclass must belong to exactly one subclass.
Example
Consider specialization of Software_Product into Operating_System and Application:
The specialization is Total and Disjoint, meaning every Software Product must be either an Operating System or an Application, but not both. So, each product belongs to exactly one subclass.
| [10]
|
Q2
CO2; BL-3
| b.
| Describe the purpose of each section (DECLARE, BEGIN, EXCEPTION, END) of a standard PL/SQL block. Design a single PL/SQL block that demonstrates both a predefined exception (NO_DATA_FOUND) and a user-defined exception.
Ans:
Purpose 5 marks
Design a single PL/SQL block 5 marks
DECLARE: This optional section is used to declare variables, constants, cursors, and user-defined exceptions that will be used in the block.
BEGIN: This is the executable section where the main logic of the program is written. It includes SQL statements and PL/SQL procedural statements.
EXCEPTION: This optional section handles errors (exceptions) that occur in the execution section. Both predefined and user-defined exceptions can be handled here.
END This section marks the end of the PL/SQL block. Every PL/SQL block must end with the keyword END;

| [10]
|
Q3
CO3, BL-4
| a.
| Design an XML schema for an Online Shopping System that manages data for Customers, Orders, Products, and Payments. Include elements for order details, product descriptions, and customer information with attributes such as order ID and payment status.
Ans:
Root structure & major modules (2 marks)
Customer information design (2 marks)
Product description design (2 marks)
Order & order details structure (2 marks)
Payment modelling with status (2 marks)

| [10]
|
Q3
CO4; BL-3
| b.
| Analyze the roles of valid time and transaction time in temporal databases and evaluate how bitemporal modeling resolves limitations of single-time designs. Use a brief example from banking or healthcare to show lifecycle tracking of historical data.
Ans:
Concept of Temporal Databases: (5 Marks)
Example: (5 Marks)

• Temporal databases store data that changes over time, allowing for historical tracking.
Differences:
• Valid Time: When the data is true in the real world.
• Transaction Time: When the data is stored in the database.
• Bitemporal Data: Combines both valid and transaction time to track data changes and record history.
Example
• Healthcare: Track patient records where valid time represents when symptoms occurred, and transaction time shows when the records were updated.
| [10]
|
Q4
CO3, BL3
| a.
| Discuss the concept of encapsulation and tell how it is used to create abstract data types in object-oriented databases with example.
Ans:
It is related to the concepts of ADTs and information hiding (5 Marks)
Object-oriented databases with example (5 Marks)

For database applications, the requirement that all objects be completely encapsulated is too strict.
One way to relax this requirement is to divide the data members into visible and hidden attributes (or data members)
Visible attributes may be accessed(read) by high level query languages or other external operators
Hidden attributes of an object can be accessed only through predefined operations
Most OODBMS use high-level query languages for accessing or reading visible attributes
Usually operations that update the state of an object are encapsulated.
One reason for this is that in many OO data models, few integrity constraints are predefined in the schema
So each type of object has its integrity constraints programmed into the methods that create, delete, and update the objects
For example, a BankAccount class defines operations like deposit() and withdraw(), while the balance attribute remains hidden.

| [10]
|
Q4
CO4; BL-3
| b.
| Analyze how the Voting-based concurrency control method enhances fault tolerance compared to the Primary Site technique in a distributed database system
Ans:
Analyze with explanation 5 marks
how Voting-based concurrency control method enhances fault tolerance 5 marks

Primary Site method: Entire system halts if the coordinator site fails.
Voting method: System continues operation, ensuring availability and resilience.
In Voting-based concurrency control, every copy of a data item participates in the decision-making process. A transaction obtains a lock only when it secures a majority of votes from all copies. Unlike the Primary Site technique, which depends on a single coordinator, the voting method avoids single-point failure by distributing control among multiple sites.
Even if some sites fail, as long as a majority of votes are obtained, transactions can proceed.
Synchronization and lock consistency are maintained across all active copies.
| [10]
|
Q5
CO4, BL-3
| a.
| How inter-query and intra-query parallelism improve performance in large-scale database environments. Discuss the trade-offs and implementation challenges.
Ans:
How inter-query and intra-query parallelism improve performance 5 marks
Trade-offs 3 marks
Implementation Example 2 marks
Parallelism enhances query performance by dividing tasks across multiple processors, enabling faster data access and improved throughput.
Types of Parallelism:
Inter-Query Parallelism: Multiple independent queries run simultaneously across processors.
Advantage: Increases system throughput; ideal for transaction-heavy workloads.
Intra-Query Parallelism: A single complex query is split into parallel sub-tasks.
Advantage: Reduces response time for analytical queries.
Techniques:
Intra-Operator Parallelism: A single operator (e.g., sort, join) runs concurrently.
Inter-Operator Parallelism: Multiple operators (e.g., select and join) run in a pipelined manner.
Trade-offs: 3 marks
High overhead in synchronizing parallel tasks.
Load imbalance due to skewed data distribution.
Communication overhead between processors.
Implementation Example: 2 marks
A data warehouse query performing joins and aggregations can use intra-query parallelism, where each processor joins a subset of data before merging results.
| [10]
|
Q5
CO3;BL-4
| b.
| A university course management system maintains records of courses, students, and their prerequisites. Each course has attributes such as courseCode, courseTitle, creditHours, and description. Students have attributes including studentID, name, email, and major. A student can enroll in multiple courses, but certain courses have prerequisites that must be completed before enrollment. The system also tracks the semester in which the student enrolls in a course.   Instructions: Develop an ODL schema for the university course management system.
Ans:
Identifying all classes 3 marks
Identifying all attributes 3 marks
Managing relationships/sets (proper Cardinality) 4 marks

class Course {
( extent courses)
attribute string courseCode;
attribute string courseTitle;
attribute short creditHours;
attribute string description;
relationship set Course has_prereqs inverse Course::is_prereq_for;
relationship set Enrollment offered_in inverse Enrollment::enrolled_courses;
};
class Student {
( extent students)
attribute string studentID;
attribute string name;
attribute string email;
attribute string major;
relationship set Enrollment enrollments inverse Enrollment::enrolled_by;
};
class Enrollment {
( extent enrollments)
attribute Date enrollmentDate;
relationship Course enrolled_courses inverse Enrollment::offered_in;
relationship Student enrolled_by inverse Enrollment::enrollments;
};
| [10]
|
Q6
CO4; BL-3
| a.
| . What are key features of NoSQL? In which situation will NoSQL database not be suitable to implement?
Ans:
Key Features: 5 marks
Situation based example 5 marks

Flexible schemas
Horizontal scaling
Fast queries due to the data model
Ease of use for developers

If you are required to perform complex and dynamic querying and reporting, then you should avoid using NoSQL as it has a limited query functionality. For such requirements, you should prefer SQL only.
NoSQL also lacks in the ability to perform dynamic operations. It can’t guarantee ACID properties. In such cases like financial transactions, etc., you may go with SQL databases.
You should also avoid NoSQL if your application needs run-time flexibility.
If consistency is a must and if there aren’t going to be any large-scale changes in terms of the data volume, then going with the SQL database is a better option.
One should also keep in mind that NoSQL databases won’t support structured query language. The querying language may vary from one database to another.
| [10]
|
Q6
CO2, BL-4
| b.
| Sample Clerk table (CL_ID, First_name, Department_name, Salary, Designation)
Create a PL/SQL procedure called percentage_salary to update Clerks data
The procedure has two parameters: IN_CL_ID and IN_PERCENT.
The procedure adjusts the salary of a particular Clerk specified the IN_CL_ID by a given percentage IN_PERCENT. (salary + salary * in_percent / 100)
In the procedure body, we use the UPDATE statement to update the salary information.
Test the procedure with CL_ID = 175 and IN_PERCENT = 10%
Ans:
Parameter declaration 2 marks
Logic implementation 4 marks
SQL statement for update 2 marks
Test the procedure 2 marks
Clerk table (CL_ID, First_name, Department_name, Salary, Designation)

CREATE OR REPLACE PROCEDURE adjust_salary(
in_CL_ID IN Clerk.CL_ID%TYPE,
in_percent IN NUMBER
) IS
BEGIN
-- update Clerk 's salary
UPDATE Clerk
SET salary = salary + salary * in_percent / 100
WHERE CL_ID = in_CL_id;
END;
| [10]
|
Q7
CO4; BL-3
| a.
| Explain the Active Database concepts in detail. Discuss the Event-Condition-Action (ECA) model, its components, and how it enhances traditional database systems. Give suitable examples of real-world applications where Active Databases are beneficial.
Ans:
Active Database concepts 3 Marks
Event-Condition-Action (ECA) model 3 Marks
suitable examples 4 Marks

Active DBMS reacts automatically to specified situations.
Rules (triggers) are stored in the catalogue and managed like other schema objects.
Granularity: Statement-level vs row-level firing.
Timing: BEFORE, AFTER, or INSTEAD OF the triggering event.
ECA Components
When the Event occurs and Condition is true, execute the Action
Event:
Database modification E.g., (insert, delete, update),
Condition:
Any true/false expression
Action:
Sequence of SQL statements that will be automatically executed
How It Enhance Traditional DBs
Proactive enforcement:
Timeliness:
Consistency & reuse:
Automation

| [10]
|
Q7
CO4; BL-3
| b.
| Explain issues in RDBMS such as impedance mismatch, schema inflexibility, and scalability limitations. Suggest suitable database that can overcome these challenges and justify your reasoning with examples.
Ans:
Issues: 5 marks
Suitable database 2 marks
Justify : 3 marks

Strengths
Structured Storage: Data stored in tables (rows & columns) with clear relationships.
ACID Properties: Ensures data consistency, reliability, and integrity.
Query Flexibility: SQL supports complex joins, filters, and aggregations.
Schema Safety: Enforces data types, primary/foreign keys, and constraints.
Maturity: Long-standing, stable technology with wide tool and vendor support.
Weaknesses
Impedance Mismatch: Difficult mapping between object-oriented code and tables.
Schema Inflexibility: Hard to modify structure once database is in production.
Limited Scalability: Supports vertical scaling, but poor horizontal scaling.
Performance Issues: Multiple joins in normalized tables slow down queries.
Not Suitable for Complex Domains: Inefficient for graph or nested data models.
Alternatives
Document Databases (MongoDB): Schema-less, handles nested objects easily.
Graph Databases (Neo4j): Best for highly connected data (networks).
Column/Key-Value Stores: High performance and scalability for large data.
| [10]
|
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper e99d7c20dfce

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_IT_7001/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (DS)/B. Tech (IT)/MBA Tech (IT)
Year: III / IV/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Advanced Database Management Systems
Date: 04 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A financial institution needs a database structure to accurately track client
investments. The fundamental object in the system is Security, which is defined
by a unique Security ID, its Name, and its current Market Price. Securities are
categorized as either Stock or Bond, though not every Security needs to fall into
one of these two classifications. Furthermore, a Security cannot be both a Stock
and a Bond. Stock entities are detailed with a Ticker Symbol and a Price-to-
Earnings Ratio. Bond entities, conversely, are described by a Maturity Date and
a Coupon Rate. Separately, all Stocks are further broken down into two types:
CO1.
Preferred Stock and Common Stock. Every Stock must be one of these two types,   [5]
BL- 5
but never both. Preferred Stock includes a Dividend Rate, while Common Stock
includes a Voting Rights Flag. The institution also tracks its clients, each
identified by a unique Client ID, an Address, and a Risk Tolerance Level. In the
system, every Security must belong to exactly one Client's portfolio, and a Client
must have at least one Security in their portfolio, although a client will often hold
many Securities.
Design EER for above scenario. Draw EER for the above problem statement.
Ans:
********** 1 **********
--- page 2 ---
b.   Apply type constructors to model a Department that has a name, number,
manager, a set of locations, and a set of employees. Specify suitable constructors
and justify briefly.
Ans:
Use the object definition format: (OID, constructor, value). Choose:
CO2.
• DNAME, DNUMBER → atom (strings/int).   [5]
BL- 4
• LOCATIONS → set of OIDs to atomic city objects (no duplicates).
• EMPLOYEES → set of OIDs to EMPLOYEE objects.
• MGR → OID reference to an EMPLOYEE.
Final tuple:
DEPT = (i, tuple, <dname:i₁, dnumber:i₂, mgr:i₃, locations:i₄, employees:i₅>).
c.   Explain the role of replication in distributed databases. How does synchronous
replication ensure consistency compared to asynchronous replication.
Ans:
Role & Benefits of Replication
Replication keeps multiple copies of the same data on different nodes/sites to
achieve:
• High availability & fault tolerance reads/writes can continue after
CO4. BL-2   [5]
node/site failures.
• Low-latency access: serve users from geographically closer replicas.
• Load distribution: spread read traffic; isolate analytics from OLTP.
•   Disaster recovery: a remote replica shortens RTO/RPO after an outage
In synchronous Client completes only after replica(s) also persist, where as in
Asynchronous replication, Client completes after primary, replicas catch up
later hence synchronous replication is more consistent.
d.   Compare XML Schema and DTD and analyze how XML Schema overcomes the
limitations of DTD in defining structured data.
CO3.   Ans:
[5]
BL-2   An XML Schema provides a more powerful and flexible way of defining the
structure and constraints of XML documents compared to DTD (Document Type
Definition).
********** 2 **********
--- page 3 ---
• Data Typing:
o DTD supports only basic text types like #PCDATA, whereas
XML Schema includes strong data types such as xs:string,
xs:integer, xs:date, etc.
•   Syntax Compatibility:
o XML Schema is written in XML syntax, allowing it to be
processed by standard XML parsers; DTD uses a non-XML
syntax, requiring specialized processors.
•   Order and Cardinality:
o XML Schema allows control over element order, repetition
(minOccurs, maxOccurs), and optional elements, giving greater
modeling precision.
• Namespace and Validation:
o XML Schema supports namespaces and hierarchical validation,
making it suitable for complex web applications.
a.   Explain the difference between the Disjoint and Overlapping constraints in a
specialization. If a specialization hierarchy is both Total and Disjoint, what is the
exact number of subclasses that every entity in the superclass must belong to,
justify with example?
Ans:
An entity in the superclass can
An entity in the superclass can belong
belong to more than one subclass
to only one subclass.
simultaneously.
Represented by a “d” inside the Represented by an “o” inside the
specialization circle.   specialization circle.
In a company, an Employee can be
A Person can be both a Student and
either a Manager or an Engineer, but
an Employee at the same time.
not both.
Q2
Mutually exclusive subclasses   Non-mutually exclusive subclasses   [10]
CO1; BL-1
Used when   subclasses   represent Used when subclasses represent
distinct categories.   roles or multiple associations.
•   Total Specialization: Every entity in the superclass must belong to at least
one subclass.
•   Disjoint Constraint: Each entity can belong to only one subclass.
•   If a specialization hierarchy is both Total and Disjoint, then every entity
in the superclass must belong to exactly one subclass.
Example
Consider specialization of Software_Product into Operating_System and
Application:
• The specialization is Total and Disjoint, meaning every Software Product
must be either an Operating System or an Application, but not both. So,
each product belongs to exactly one subclass.
b.   Describe the purpose of each section (DECLARE, BEGIN, EXCEPTION, END)
of a standard PL/SQL block. Design a single PL/SQL block that demonstrates
Q2   both a predefined exception (NO_DATA_FOUND) and a user-defined exception.
[10]
CO2; BL-3   Ans:
• DECLARE: This optional section is used to declare variables, constants,
cursors, and user-defined exceptions that will be used in the block.
********** 3 **********
--- page 4 ---
• BEGIN: This is the executable section where the main logic of the
program is written. It includes SQL statements and PL/SQL procedural
statements.
• EXCEPTION: This optional section handles errors (exceptions) that
occur in the execution section. Both predefined and user-defined
exceptions can be handled here.
• END This section marks the end of the PL/SQL block. Every PL/SQL
block must end with the keyword END;
a.   Design an XML schema for an Online Shopping System that manages data for
Customers, Orders, Products, and Payments. Include elements for order details,
Q3
product descriptions, and customer information with attributes such as order ID [10]
CO3, BL-4
and payment status.
Ans:
********** 4 **********
--- page 5 ---
b.   Analyze the roles of valid time and transaction time in temporal databases and
evaluate how bitemporal modeling resolves limitations of single-time designs.
Use a brief example from banking or healthcare to show lifecycle tracking of
historical data.
Ans:
Concept of Temporal Databases:
• Temporal databases store data that changes over time, allowing for historical
Q3   tracking.
[10]
CO4; BL-3   Differences:
• Valid Time: When the data is true in the real world.
• Transaction Time: When the data is stored in the database.
• Bitemporal Data: Combines both valid and transaction time to track data
changes and record history.
Example:
• Healthcare: Track patient records where valid time represents when symptoms
occurred, and transaction time shows when the records were updated.
a.   Discuss the concept of encapsulation and tell how it is used to create abstract data
types in object-oriented databases with example.
Ans:
It is related to the concepts of ADTs and information hiding
• For database applications, the requirement that all objects be completely
encapsulated is too strict.
• One way to relax this requirement is to divide the data members into
visible and hidden attributes (or data members)
•   Visible attributes may be accessed(read) by high level query languages or
Q4   other external operators
[10]
CO3, BL3   • Hidden attributes of an object can be accessed only through predefined
operations
• Most OODBMS use high-level query languages for accessing or reading
visible attributes
•   Usually operations that update the state of an object are encapsulated.
• One reason for this is that in many OO data models, few integrity constraints
are predefined in the schema
• So each type of object has its integrity constraints programmed into the
methods that create, delete, and update the objects
Q4   b.   Analyze how the Voting-based concurrency control method enhances fault
[10]
CO4; BL-3   tolerance compared to the Primary Site technique in a distributed database system
********** 5 **********
--- page 6 ---
Ans:
• Primary Site method: Entire system halts if the coordinator site fails.
• Voting method: System continues operation, ensuring availability and
resilience.
In Voting-based concurrency control, every copy of a data item participates in
the decision-making process. A transaction obtains a lock only when it secures a
majority of votes from all copies. Unlike the Primary Site technique, which
depends on a single coordinator, the voting method avoids single-point failure by
distributing control among multiple sites.
Enhanced Fault Tolerance:
• Even if some sites fail, as long as a majority of votes are obtained,
transactions can proceed.
•   Synchronization and lock consistency are maintained across all active
copies.
a. How inter-query and intra-query parallelism improve performance in large-
scale database environments. Discuss the trade-offs and implementation
challenges.
Ans:
Parallelism enhances query performance by dividing tasks across multiple
processors, enabling faster data access and improved throughput.
• Types of Parallelism:
o Inter-Query Parallelism: Multiple independent queries run
simultaneously across processors.
▪   Advantage:   Increases system   throughput;   ideal   for
transaction-heavy workloads.
o Intra-Query Parallelism: A single complex query is split into
parallel sub-tasks.
Q5
▪   Advantage: Reduces response time for analytical queries.   [10]
CO4, BL-3
▪   Techniques:
▪ Intra-Operator Parallelism: A single operator (e.g.,
sort, join) runs concurrently.
▪   Inter-Operator Parallelism: Multiple operators
(e.g., select and join) run in a pipelined manner.
•   Trade-offs:
o High overhead in synchronizing parallel tasks.
o Load imbalance due to skewed data distribution.
o Communication overhead between processors.
• Implementation Example:
A data warehouse query performing joins and aggregations can use intra-
query parallelism, where each processor joins a subset of data before
merging results.
b. A university course management system maintains records of courses, students,
and their prerequisites. Each course has attributes such as courseCode,
courseTitle, creditHours, and description. Students have attributes including
studentID, name, email, and major. A student can enroll in multiple courses, but
Q5
certain courses have prerequisites that must be completed before enrollment. The [10]
CO3;BL-4
system also tracks the semester in which the student enrolls in a course.
Instructions: Develop an ODL schema for the university course management
system.
Ans:
********** 6 **********
--- page 7 ---
class Course {
( extent courses)
attribute string courseCode;
attribute string courseTitle;
attribute short creditHours;
attribute string description;
relationship set Course has_prereqs inverse Course::is_prereq_for;
relationship set Enrollment offered_in inverse Enrollment::enrolled_courses;
};
class Student {
( extent students)
attribute string studentID;
attribute string name;
attribute string email;
attribute string major;
relationship set Enrollment enrollments inverse Enrollment::enrolled_by;
};
class Enrollment {
( extent enrollments)
attribute Date enrollmentDate;
relationship Course enrolled_courses inverse Enrollment::offered_in;
relationship Student enrolled_by inverse Enrollment::enrollments;
};
a.   . What are key features of NoSQL? In which situation will NoSQL database not
be suitable to implement?
Ans:
Key Features:
•   Flexible schemas
•   Horizontal scaling
•   Fast queries due to the data model
• Ease of use for developers
If you are required to perform complex and dynamic querying and reporting, then
Q6
you should avoid using NoSQL as it has a limited query functionality. For such [10]
CO4; BL-3
requirements, you should prefer SQL only.
NoSQL also lacks in the ability to perform dynamic operations. It can’t guarantee
ACID properties. In such cases like financial transactions, etc., you may go with
SQL databases.
You should also avoid NoSQL if your application needs run-time flexibility.
If consistency is a must and if there aren’t going to be any large-scale changes in
terms of the data volume, then going with the SQL database is a better option.
One should also keep in mind that NoSQL databases won’t support structured
query language. The querying language may vary from one database to another.
b.   Sample Clerk   table (CL_ID,   First_name, Department_name,   Salary,
Designation)
Create a PL/SQL procedure called percentage_salary to update Clerks data
Q6
• The procedure has two parameters: IN_CL_ID and IN_PERCENT.   [10]
CO2, BL-4
• The procedure adjusts the salary of a particular Clerk specified the
IN_CL_ID by a given percentage IN_PERCENT. (salary + salary *
in_percent / 100)
********** 7 **********
--- page 8 ---
•   In the procedure body, we use the UPDATE statement to update the
salary information.
•   Test the procedure with CL_ID = 175 and IN_PERCENT = 10%
Ans:
CREATE OR REPLACE PROCEDURE adjust_salary(
in_employee_id IN EMPLOYEES.EMPLOYEE_ID%TYPE,
in_percent IN NUMBER
) IS
BEGIN
-- update employee's salary
UPDATE employees
SET salary = salary + salary * in_percent / 100
WHERE employee_id = in_employee_id;
END;
a.   Explain the Active Database concepts in detail. Discuss the Event-Condition-
Action (ECA) model, its components, and how it enhances traditional database
systems. Give suitable examples of real-world applications where Active
Databases are beneficial.
Ans:
Active DBMS reacts automatically to specified situations.
Rules (triggers) are stored in the catalogue and managed like other schema
objects.
Granularity: Statement-level vs row-level firing.
Timing: BEFORE, AFTER, or INSTEAD OF the triggering event.
ECA Components
Q7   When the Event occurs and Condition is true, execute the Action
[10]
CO4; BL-3   • Event:
o Database modification E.g., (insert, delete, update),
• Condition:
o Any true/false expression
•   Action:
o Sequence of SQL statements that will be automatically executed
How It Enhance Traditional DBs
•   Proactive enforcement:
•   Timeliness:
•   Consistency & reuse:
• Automation
b.   Explain issues in RDBMS such as impedance mismatch, schema inflexibility,
and scalability limitations. Suggest suitable database that can overcome these
challenges and justify your reasoning with examples.
Ans:
Strengths
Q7   1. Structured Storage: Data stored in tables (rows & columns) with clear
[10]
CO4; BL-3   relationships.
2. ACID Properties: Ensures data consistency, reliability, and integrity.
3. Query   Flexibility: SQL   supports complex   joins,   filters, and
aggregations.
4. Schema Safety: Enforces data types, primary/foreign keys, and
constraints.
********** 8 **********
--- page 9 ---
5. Maturity: Long-standing, stable technology with wide tool and vendor
support.
Weaknesses
1. Impedance Mismatch: Difficult mapping between object-oriented
code and tables.
2. Schema Inflexibility: Hard to modify structure once database is in
production.
3. Limited Scalability: Supports vertical scaling, but poor horizontal
scaling.
4. Performance Issues: Multiple joins in normalized tables slow down
queries.
5. Not Suitable for Complex Domains: Inefficient for graph or nested data
models.
Alternatives
• Document Databases (MongoDB): Schema-less, handles nested objects
easily.
• Graph Databases (Neo4j): Best for highly connected data (networks).
• Column/Key-Value Stores: High performance and scalability for large
data.
********** 9 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper f992ee829bd1

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/MBATech_IT_7041/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (DS)/B. Tech (IT)/MBA Tech (IT)
Year: III / IV/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Advanced Database Management Systems
Date: 04 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A financial institution needs a database structure to accurately track client
investments. The fundamental object in the system is Security, which is defined
by a unique Security ID, its Name, and its current Market Price. Securities are
categorized as either Stock or Bond, though not every Security needs to fall into
one of these two classifications. Furthermore, a Security cannot be both a Stock
and a Bond. Stock entities are detailed with a Ticker Symbol and a Price-to-
Earnings Ratio. Bond entities, conversely, are described by a Maturity Date and
a Coupon Rate. Separately, all Stocks are further broken down into two types:
CO1.
Preferred Stock and Common Stock. Every Stock must be one of these two types,   [5]
BL- 5
but never both. Preferred Stock includes a Dividend Rate, while Common Stock
includes a Voting Rights Flag. The institution also tracks its clients, each
identified by a unique Client ID, an Address, and a Risk Tolerance Level. In the
system, every Security must belong to exactly one Client's portfolio, and a Client
must have at least one Security in their portfolio, although a client will often hold
many Securities.
Design EER for above scenario. Draw EER for the above problem statement.
Ans:
********** 1 **********
--- page 2 ---
b.   Apply type constructors to model a Department that has a name, number,
manager, a set of locations, and a set of employees. Specify suitable constructors
and justify briefly.
Ans:
Use the object definition format: (OID, constructor, value). Choose:
CO2.
• DNAME, DNUMBER → atom (strings/int).   [5]
BL- 4
• LOCATIONS → set of OIDs to atomic city objects (no duplicates).
• EMPLOYEES → set of OIDs to EMPLOYEE objects.
• MGR → OID reference to an EMPLOYEE.
Final tuple:
DEPT = (i, tuple, <dname:i₁, dnumber:i₂, mgr:i₃, locations:i₄, employees:i₅>).
c.   Explain the role of replication in distributed databases. How does synchronous
replication ensure consistency compared to asynchronous replication.
Ans:
Role & Benefits of Replication
Replication keeps multiple copies of the same data on different nodes/sites to
achieve:
• High availability & fault tolerance reads/writes can continue after
CO4. BL-2   [5]
node/site failures.
• Low-latency access: serve users from geographically closer replicas.
• Load distribution: spread read traffic; isolate analytics from OLTP.
•   Disaster recovery: a remote replica shortens RTO/RPO after an outage
In synchronous Client completes only after replica(s) also persist, where as in
Asynchronous replication, Client completes after primary, replicas catch up
later hence synchronous replication is more consistent.
d.   Compare XML Schema and DTD and analyze how XML Schema overcomes the
limitations of DTD in defining structured data.
CO3.   Ans:
[5]
BL-2   An XML Schema provides a more powerful and flexible way of defining the
structure and constraints of XML documents compared to DTD (Document Type
Definition).
********** 2 **********
--- page 3 ---
• Data Typing:
o DTD supports only basic text types like #PCDATA, whereas
XML Schema includes strong data types such as xs:string,
xs:integer, xs:date, etc.
•   Syntax Compatibility:
o XML Schema is written in XML syntax, allowing it to be
processed by standard XML parsers; DTD uses a non-XML
syntax, requiring specialized processors.
•   Order and Cardinality:
o XML Schema allows control over element order, repetition
(minOccurs, maxOccurs), and optional elements, giving greater
modeling precision.
• Namespace and Validation:
o XML Schema supports namespaces and hierarchical validation,
making it suitable for complex web applications.
a.   Explain the difference between the Disjoint and Overlapping constraints in a
specialization. If a specialization hierarchy is both Total and Disjoint, what is the
exact number of subclasses that every entity in the superclass must belong to,
justify with example?
Ans:
An entity in the superclass can
An entity in the superclass can belong
belong to more than one subclass
to only one subclass.
simultaneously.
Represented by a “d” inside the Represented by an “o” inside the
specialization circle.   specialization circle.
In a company, an Employee can be
A Person can be both a Student and
either a Manager or an Engineer, but
an Employee at the same time.
not both.
Q2
Mutually exclusive subclasses   Non-mutually exclusive subclasses   [10]
CO1; BL-1
Used when   subclasses   represent Used when subclasses represent
distinct categories.   roles or multiple associations.
•   Total Specialization: Every entity in the superclass must belong to at least
one subclass.
•   Disjoint Constraint: Each entity can belong to only one subclass.
•   If a specialization hierarchy is both Total and Disjoint, then every entity
in the superclass must belong to exactly one subclass.
Example
Consider specialization of Software_Product into Operating_System and
Application:
• The specialization is Total and Disjoint, meaning every Software Product
must be either an Operating System or an Application, but not both. So,
each product belongs to exactly one subclass.
b.   Describe the purpose of each section (DECLARE, BEGIN, EXCEPTION, END)
of a standard PL/SQL block. Design a single PL/SQL block that demonstrates
Q2   both a predefined exception (NO_DATA_FOUND) and a user-defined exception.
[10]
CO2; BL-3   Ans:
• DECLARE: This optional section is used to declare variables, constants,
cursors, and user-defined exceptions that will be used in the block.
********** 3 **********
--- page 4 ---
• BEGIN: This is the executable section where the main logic of the
program is written. It includes SQL statements and PL/SQL procedural
statements.
• EXCEPTION: This optional section handles errors (exceptions) that
occur in the execution section. Both predefined and user-defined
exceptions can be handled here.
• END This section marks the end of the PL/SQL block. Every PL/SQL
block must end with the keyword END;
a.   Design an XML schema for an Online Shopping System that manages data for
Customers, Orders, Products, and Payments. Include elements for order details,
Q3
product descriptions, and customer information with attributes such as order ID [10]
CO3, BL-4
and payment status.
Ans:
********** 4 **********
--- page 5 ---
b.   Analyze the roles of valid time and transaction time in temporal databases and
evaluate how bitemporal modeling resolves limitations of single-time designs.
Use a brief example from banking or healthcare to show lifecycle tracking of
historical data.
Ans:
Concept of Temporal Databases:
• Temporal databases store data that changes over time, allowing for historical
Q3   tracking.
[10]
CO4; BL-3   Differences:
• Valid Time: When the data is true in the real world.
• Transaction Time: When the data is stored in the database.
• Bitemporal Data: Combines both valid and transaction time to track data
changes and record history.
Example:
• Healthcare: Track patient records where valid time represents when symptoms
occurred, and transaction time shows when the records were updated.
a.   Discuss the concept of encapsulation and tell how it is used to create abstract data
types in object-oriented databases with example.
Ans:
It is related to the concepts of ADTs and information hiding
• For database applications, the requirement that all objects be completely
encapsulated is too strict.
• One way to relax this requirement is to divide the data members into
visible and hidden attributes (or data members)
•   Visible attributes may be accessed(read) by high level query languages or
Q4   other external operators
[10]
CO3, BL3   • Hidden attributes of an object can be accessed only through predefined
operations
• Most OODBMS use high-level query languages for accessing or reading
visible attributes
•   Usually operations that update the state of an object are encapsulated.
• One reason for this is that in many OO data models, few integrity constraints
are predefined in the schema
• So each type of object has its integrity constraints programmed into the
methods that create, delete, and update the objects
Q4   b.   Analyze how the Voting-based concurrency control method enhances fault
[10]
CO4; BL-3   tolerance compared to the Primary Site technique in a distributed database system
********** 5 **********
--- page 6 ---
Ans:
• Primary Site method: Entire system halts if the coordinator site fails.
• Voting method: System continues operation, ensuring availability and
resilience.
In Voting-based concurrency control, every copy of a data item participates in
the decision-making process. A transaction obtains a lock only when it secures a
majority of votes from all copies. Unlike the Primary Site technique, which
depends on a single coordinator, the voting method avoids single-point failure by
distributing control among multiple sites.
Enhanced Fault Tolerance:
• Even if some sites fail, as long as a majority of votes are obtained,
transactions can proceed.
•   Synchronization and lock consistency are maintained across all active
copies.
a. How inter-query and intra-query parallelism improve performance in large-
scale database environments. Discuss the trade-offs and implementation
challenges.
Ans:
Parallelism enhances query performance by dividing tasks across multiple
processors, enabling faster data access and improved throughput.
• Types of Parallelism:
o Inter-Query Parallelism: Multiple independent queries run
simultaneously across processors.
▪   Advantage:   Increases system   throughput;   ideal   for
transaction-heavy workloads.
o Intra-Query Parallelism: A single complex query is split into
parallel sub-tasks.
Q5
▪   Advantage: Reduces response time for analytical queries.   [10]
CO4, BL-3
▪   Techniques:
▪ Intra-Operator Parallelism: A single operator (e.g.,
sort, join) runs concurrently.
▪   Inter-Operator Parallelism: Multiple operators
(e.g., select and join) run in a pipelined manner.
•   Trade-offs:
o High overhead in synchronizing parallel tasks.
o Load imbalance due to skewed data distribution.
o Communication overhead between processors.
• Implementation Example:
A data warehouse query performing joins and aggregations can use intra-
query parallelism, where each processor joins a subset of data before
merging results.
b. A university course management system maintains records of courses, students,
and their prerequisites. Each course has attributes such as courseCode,
courseTitle, creditHours, and description. Students have attributes including
studentID, name, email, and major. A student can enroll in multiple courses, but
Q5
certain courses have prerequisites that must be completed before enrollment. The [10]
CO3;BL-4
system also tracks the semester in which the student enrolls in a course.
Instructions: Develop an ODL schema for the university course management
system.
Ans:
********** 6 **********
--- page 7 ---
class Course {
( extent courses)
attribute string courseCode;
attribute string courseTitle;
attribute short creditHours;
attribute string description;
relationship set Course has_prereqs inverse Course::is_prereq_for;
relationship set Enrollment offered_in inverse Enrollment::enrolled_courses;
};
class Student {
( extent students)
attribute string studentID;
attribute string name;
attribute string email;
attribute string major;
relationship set Enrollment enrollments inverse Enrollment::enrolled_by;
};
class Enrollment {
( extent enrollments)
attribute Date enrollmentDate;
relationship Course enrolled_courses inverse Enrollment::offered_in;
relationship Student enrolled_by inverse Enrollment::enrollments;
};
a.   . What are key features of NoSQL? In which situation will NoSQL database not
be suitable to implement?
Ans:
Key Features:
•   Flexible schemas
•   Horizontal scaling
•   Fast queries due to the data model
• Ease of use for developers
If you are required to perform complex and dynamic querying and reporting, then
Q6
you should avoid using NoSQL as it has a limited query functionality. For such [10]
CO4; BL-3
requirements, you should prefer SQL only.
NoSQL also lacks in the ability to perform dynamic operations. It can’t guarantee
ACID properties. In such cases like financial transactions, etc., you may go with
SQL databases.
You should also avoid NoSQL if your application needs run-time flexibility.
If consistency is a must and if there aren’t going to be any large-scale changes in
terms of the data volume, then going with the SQL database is a better option.
One should also keep in mind that NoSQL databases won’t support structured
query language. The querying language may vary from one database to another.
b.   Sample Clerk   table (CL_ID,   First_name, Department_name,   Salary,
Designation)
Create a PL/SQL procedure called percentage_salary to update Clerks data
Q6
• The procedure has two parameters: IN_CL_ID and IN_PERCENT.   [10]
CO2, BL-4
• The procedure adjusts the salary of a particular Clerk specified the
IN_CL_ID by a given percentage IN_PERCENT. (salary + salary *
in_percent / 100)
********** 7 **********
--- page 8 ---
•   In the procedure body, we use the UPDATE statement to update the
salary information.
•   Test the procedure with CL_ID = 175 and IN_PERCENT = 10%
Ans:
CREATE OR REPLACE PROCEDURE adjust_salary(
in_employee_id IN EMPLOYEES.EMPLOYEE_ID%TYPE,
in_percent IN NUMBER
) IS
BEGIN
-- update employee's salary
UPDATE employees
SET salary = salary + salary * in_percent / 100
WHERE employee_id = in_employee_id;
END;
a.   Explain the Active Database concepts in detail. Discuss the Event-Condition-
Action (ECA) model, its components, and how it enhances traditional database
systems. Give suitable examples of real-world applications where Active
Databases are beneficial.
Ans:
Active DBMS reacts automatically to specified situations.
Rules (triggers) are stored in the catalogue and managed like other schema
objects.
Granularity: Statement-level vs row-level firing.
Timing: BEFORE, AFTER, or INSTEAD OF the triggering event.
ECA Components
Q7   When the Event occurs and Condition is true, execute the Action
[10]
CO4; BL-3   • Event:
o Database modification E.g., (insert, delete, update),
• Condition:
o Any true/false expression
•   Action:
o Sequence of SQL statements that will be automatically executed
How It Enhance Traditional DBs
•   Proactive enforcement:
•   Timeliness:
•   Consistency & reuse:
• Automation
b.   Explain issues in RDBMS such as impedance mismatch, schema inflexibility,
and scalability limitations. Suggest suitable database that can overcome these
challenges and justify your reasoning with examples.
Ans:
Strengths
Q7   1. Structured Storage: Data stored in tables (rows & columns) with clear
[10]
CO4; BL-3   relationships.
2. ACID Properties: Ensures data consistency, reliability, and integrity.
3. Query   Flexibility: SQL   supports complex   joins,   filters, and
aggregations.
4. Schema Safety: Enforces data types, primary/foreign keys, and
constraints.
********** 8 **********
--- page 9 ---
5. Maturity: Long-standing, stable technology with wide tool and vendor
support.
Weaknesses
1. Impedance Mismatch: Difficult mapping between object-oriented
code and tables.
2. Schema Inflexibility: Hard to modify structure once database is in
production.
3. Limited Scalability: Supports vertical scaling, but poor horizontal
scaling.
4. Performance Issues: Multiple joins in normalized tables slow down
queries.
5. Not Suitable for Complex Domains: Inefficient for graph or nested data
models.
Alternatives
• Document Databases (MongoDB): Schema-less, handles nested objects
easily.
• Graph Databases (Neo4j): Best for highly connected data (networks).
• Column/Key-Value Stores: High performance and scalability for large
data.
********** 9 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 110cfb5b156f

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_DS_7052/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/MBA Tech (DS)
Year: III / IV/Semester VI/Semester VIII(Exam Year: 2025-2026)
Subject: Advanced Database Management Systems
Date: 14 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a. A shared subclass is a subclass that has more than one superclass.
It inherits properties from multiple parent classes, which is a form of
multiple inheritance in object-oriented databases or ER modelling
CO-1;
SO-1;   [5]
BL-2
StarModel is shared subclass it inherits properties from MovieStar and
Model
[explanation-2.5 M, example-2,5M]
********** 1 **********
--- page 2 ---
b   Ans: Suitable Constructors (2.5 M) + Justification (2.5 M)   [5]
Use object definition format: (OID, constructor, value)
Choose:
CO-2;
• LIB_NAME → atom (string)
SO-1;
• LIBRARIAN → OID reference to a LIBRARIAN object
BL-2
• BOOKS → set of OIDs to BOOK objects (no duplicates)
• MEMBERS → set of OIDs to MEMBER objects
Final Tuple:
LIBRARY = (i, tuple, <lib_name:i₁, librarian:i₂, books:i₃, members:i₄>)
c   Explain the advantages of parallel database systems   [5]
Answer
Advantages:
1. Improved Performance (Speedup)
o Queries execute faster due to parallel processing.
CO-2;   2. Scalability
SO-1;   o System can grow by adding more processors or disks.
BL-2   3. High Throughput
o Multiple queries can be processed at the same time.
4. Fault Tolerance
o Failure of one node does not stop the entire system.
5. Efficient Resource Utilization
o CPU, memory, and disk resources are used effectively.
d   Well-Formed XML   [5]
 It must start with an XML declaration to indicate the version of XML
being used—as well as any other relevant attributes.
 It must follow the syntactic guidelines of the tree model.
 XML documents must have a root element
 XML elements must have a closing tag
 XML tags are case sensitive
CO-3;    XML elements must be properly nested
SO-1;
 XML attribute values must be quoted
BL-2
(2 marks)
Valid XML
 A valid XML document is not only well-formed but also adheres to a
defined structure or set of rules specified by a Document Type Definition
(DTD) or an XML Schema (XSD). This type ensures that the content and
structure of the document conform to the defined rules, making it more
reliable for applications that require structured data.
********** 2 **********
--- page 3 ---
 Key Characteristics:
•   It follows the rules of well-formed XML.
•   It references a DTD or XML Schema.
•   Elements, attributes, and their values must conform to the defined structure.
(3 marks)
a. A trigger is a database object that is automatically executed or fired when
a   specified   event   occurs   on   a   table   or   view.
These events include INSERT, UPDATE, or DELETE operations.
Statement-Level Trigger   Row-Level Trigger
Executes once for the entire SQL Executes once for each
statement   row affected
Used when action does not   Used when action
depend on individual rows   depends on each row
Slower (multiple
Q2   Faster (less execution)
executions)
CO-3;   Does not use FOR EACH ROW Uses FOR EACH ROW   [10]
SO-1;
BL-3   Validating each row’s
Logging updates
data
CREATE OR REPLACE TRIGGER prevent_salary_reduction
BEFORE UPDATE OF Salary ON EMP
FOR EACH ROW
BEGIN
IF :NEW.Salary < :OLD.Salary THEN
RAISE_APPLICATION_ERROR(-20001, 'Salary cannot be reduced');
END IF;
END;
/
[what is trigger-2M,Difference 4M, trigger code- 4M]
b.   (Implementation – 5 marks)   [10]
// Enable sharding on database
sh.enableSharding("bankDB")
// Select database
use bankDB
// Shard the collection using customer_id as shard key
Q2
sh.shardCollection("bankDB.customers", { customer_id: 1 })
CO-4;
SO-1;   // Insert sample data
BL-1,4   db.customers.insertMany([
{ customer_id: 1, name: "Amit", city: "Mumbai", balance: 5000 },
{ customer_id: 2, name: "Neha", city: "Delhi", balance: 7000 },
{ customer_id: 3, name: "Raj", city: "Pune", balance: 6000 }
])
(Explanation – 5 marks)
•   Sharding distributes data across multiple servers (shards) using a shard key
(customer_id).
********** 3 **********
--- page 4 ---
• MongoDB divides data into chunks and distributes them evenly, ensuring
load balancing.
•   This improves scalability and performance for large datasets in distributed
environments.
a.   [10]
Q3
CO-1,2;
SO-1;
BL-2,4
Identifying object- 2M
Identifying reference 2M
All diagrammatic representation-6M
b.   Diagram   [10]
Q3
CO-1,2;
SO-1;
BL-1,2
• Shared Nothing
********** 4 **********
--- page 5 ---
Each node is completely independent.
Advantages:
High scalability
No resource contention
Best performance for large systems
Limitations:
Complex query processing
Data distribution challenges
• Shared memory
All processors share common memory and disk.
Advantages:
Easy communication between processors
Simple design
Limitations:
Memory contention
Limited scalability
• Shared Disk
Each processor has its own memory, but disks are shared.
Advantages:
High availability
Easy data access
Limitations:
Disk contention
Synchronization overhead
[diagram -4M,Each architecture with advantages an dlimitation-
2M*3=6M]
a.   (Tree Diagram – 5 marks)   [10]
university
├── course (course_id="CSE101")
│ ├── name → DBMS
│ ├── faculty
│ │ ├── first_name → Raj
│ │ └── last_name → Mehta
Q4
│ └── credits → 4
CO-3;
SO-1;   └── course (course_id="CSE102")
BL-1,4
├── name → AI
├── faculty
│ ├── first_name → Anita
│ └── last_name → Patel
└── credits → 3
(Theory – 5 marks)
•   Attributes provide additional information about elements (e.g., course_id).
********** 5 **********
--- page 6 ---
• They help uniquely identify elements and store metadata without affecting
the hierarchical structure.
b.   Active databases automatically respond to events using ECA rules. An event triggers [10]
a condition check, and if true, an action is executed. (2 marks)
Design and Implementation Issues:- (6 Marks)
 An active database allows users to make the following changes to triggers
(rules)
 Activate
 Deactivate
 Drop
 An event can be considered in 3 ways
 Immediate consideration
 Deferred consideration
 Detached consideration
Q4
 Immediate consideration
CO-4;
SO-1;    Part of the same transaction and can be one of the following
BL-1,2
depending on the situation
 Evaluate the condition before executing the triggering event.
 Evaluate the condition after executing the triggering event.
 Evaluate the condition instead of executing the triggering
event.
 Deferred consideration
 Condition is evaluated at the end of the transaction
 Detached consideration
 Condition is evaluated in a separate transaction
Example: On inserting a record (event), if stock < threshold (condition), generate alert
(action). These rules enable automation and real-time responses. (2 marks)
a.   While most databases tend to model reality at a point in time (at the “current''   [10]
time), temporal databases model the states of the real world across time. it offers
temporal data types and stores information relating to past, present and future time.
Facts in temporal relations have associated times when they are valid, which can be
Q5   represented as a union of intervals.
CO-4;   The transaction time for a fact is the time interval during which the fact is current
SO-1;
BL-1,2   within the database system.
In a temporal relation, each tuple has an associated time when it is true; the time
may be either valid time or transaction time.
A bi-temporal relation stores both valid and transaction time.
. (5 marks)
********** 6 **********
--- page 7 ---
Incorporating Time in Relational Databases
Using Tuple Versioning
 Add to every tuple
 Valid start time
 Valid end time
 Using Transaction Time Relations.
 In a transaction time database, whenever a change is applied to the
database, the actual timestamp of the transaction that applied the
change (insert, delete, or update) is recorded. Draw diagram also (5
marks)
b. NoSQL databases are non-relational databases designed to handle large volumes of [10]
semi-structured or unstructured data. They store data in flexible formats such as key-
value, document, column, or graph models. MongoDB is a document-based NoSQL
Q5   database that stores data in JSON-like (BSON) format. (5 marks)
CO-4;   Key characteristics include schema-less design, horizontal scalability, high
SO-1;
BL-1,4   availability, and BASE properties (eventual consistency). MongoDB allows flexible
schema and efficient handling of large-scale distributed data, making it suitable for
modern web applications. (5 marks)
Elaborate both above points
a.   [10]
Q6
CO-1;
SO-1;
BL-6
[Diagram-identifying entities, attributes, relationship-6M]
Relational schema[4M]
USER(User_ID, Name, Email, Phone)
CUSTOMER(User_ID, Shipping_Address)
********** 7 **********
--- page 8 ---
SELLER(User_ID, Store_Name, GST_Number)
PRODUCT(Product_ID, Product_Name, Price)
ELECTRONICS(Product_ID, Warranty_Period, Brand)
CLOTHING(Product_ID, Size, Material)
ORDERS(Order_ID, Order_Date, User_ID)
ORDER_PRODUCT(Order_ID, Product_ID)
SELLER_PRODUCT(User_ID, Product_ID)
b.   [10]
Consider table EMP(emp_id, emp_name, salary)
DECLARE
CURSOR emp_cursor
IS
SELECT emp_name FROM EMP;
v_name EMP.emp_name%TYPE;
BEGIN
OPEN emp_cursor;
Q6
LOOP
CO-3;   FETCH emp_cursor INTO v_name;
SO-1;
BL-3
EXIT WHEN emp_cursor%NOTFOUND;
DBMS_OUTPUT.PUT_LINE('Employee Name: ' || v_name);
END LOOP;
DBMS_OUTPUT.PUT_LINE('Total Records Processed: ' ||
emp_cursor%ROWCOUNT);
CLOSE emp_cursor;
END;
/
[Concept of Explicit Cursor -3M, Use of %ROWCOUNT - 2 M,
Correct PL/SQL Program- 5 M]
a.   (Explanation of Techniques – 5 marks)   [10]
• Round-robin Partitioning:
Data is distributed sequentially across partitions in a cyclic manner. Each
new record is placed in the next partition. This ensures uniform data
distribution without considering data values.
• Hash Partitioning:
Q7
A hash function is applied to a partitioning key (e.g., ID), and the result
CO-1,2;
SO-1;   determines the partition. This provides balanced distribution and is
BL-1,2
independent of data order.
• Range Partitioning:
Data is divided based on value ranges of a key attribute (e.g., date or
salary). Each partition stores records within a specific range. It preserves
ordering of data.
(Advantages – 5 marks)
********** 8 **********
--- page 9 ---
• Round-robin:
Ensures equal distribution of data and load balancing, simple to implement.
• Hash Partitioning:
Provides efficient data distribution and fast access for equality-based
queries.
• Range Partitioning:
Suitable for range queries, improves query performance when accessing
ordered data.
b.   Persistence by Naming and Persistence by Reachability are the two   [10]
primary mechanisms used in Object-Oriented Database Management
Systems (OODBMS) to make objects persistent (i.e., stored permanently
in the database so they survive after the program terminates).
• Naming Mechanism: Assign an object a unique persistent name
through which it can be retrieved by this and other programs.
•   Reachability Mechanism: Make the object reachable from some
persistent object.
• An object B is said to be reachable from an object A if a sequence
of references in the object graph lead from object A to object B.
Naming example
define class BookSet:
type set(Book);
operations
add_book(b: Book): boolean;
remove_book(b: Book): boolean;
Q7
end BookSet;
CO-1,2;
SO-1;   ...
BL-2,4   persistent name AllBooks: BookSet;
(* AllBooks is a persistent named object of type BookSet *)
Rechability example
define class Library:
type tuple (books: set(Book));
end Library;
...
persistent name CentralLibrary: Library;
(* CentralLibrary is a persistent object *)
...
b1 := create_book;
b2 := create_book;
...
********** 9 **********
--- page 10 ---
CentralLibrary.books := {b1, b2};
[Naming explanation wit example 5 M
Reachability explanation wit example 5 M]
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 2536dc995170

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_DS_7009/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (DS)/B. Tech (IT)/MBA Tech (IT)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Advanced Database Management Systems
Date: 11 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A software development company requires a database structure to manage its
intellectual property and sales records. The core entity is Software Product,
which is uniquely identified by Product ID and tracked by its Name and Release
Date. All products in the catalog are comprehensively categorized into two
mutually exclusive types: Operating Systems and Applications. Operating
Systems are described by their Minimum RAM Requirement and Kernel Type,
while Applications are detailed by their Version Number and Installation Size.
Applications themselves undergo further classification. They can be designated
as Games or Productivity Tools, though this designation is optional for some
CO1.   [5]
BL- 5   Applications (such as utilities). Importantly, an application cannot fall into both
the Game and Productivity Tool categories. Games require tracking of their
Genre, and Productivity Tools are associated with a Subscription Model.
Separately, the company manages Licenses, each having a unique License Key,
an Activation Date, and a Number of Seats. Every License must be tied to one
and only one Software Product, and every Software Product must have at least
one associated License, though typical products have many. Draw EER for above
mentioned problem statement.
Ans:
********** 1 **********
--- page 2 ---
b.   Explain the concept of object identity in Object-Oriented Databases. How does
it differ from the concept of primary key in relational databases
Ans:
Object identity (OID) in Object-Oriented Databases (OODB) is a system-
generated, permanent, and value-independent   identifier   that uniquely
distinguishes each object. An object keeps the same OID for its entire lifetime—
even if all its attribute values change, other objects can hold direct references
CO2.   [5]
BL- 2   (pointers) to it. Identity is thus about “this exact object instance” (state + behavior
+ identity).
How this differs from a Primary Key (PK) in relational databases
OID provides stable, value-independent identity and pointer-like referencing
suited to rich object graphs; a relational primary key is a value-based identifier
defined in the schema and used with foreign keys and joins for set-oriented
processing.
c.   Analyse how the Shared-Nothing approach improves scalability and performance
compared to the Shared-Disk model. Support your answer with an example of
data partitioning.
CO4. BL-3   Ans:   [5]
In the Shared-Nothing architecture, each processor (node) has its own CPU, main
memory, and disk storage, and communicates with other nodes through a high-
speed network. Unlike the Shared-Disk model, where multiple processors access
********** 2 **********
--- page 3 ---
common storage leading to contention and bandwidth bottlenecks, the shared-
nothing model ensures independent data access and parallel processing.
•   Scalability: Adding new nodes linearly increases both storage capacity
and processing power, achieving linear scale-up and speed-up.
•   Performance: Since there is no disk contention, query operations such as
scanning, sorting, and joins can be performed in parallel on separate
partitions.
• Example: In a banking database, account records can be hash-partitioned
across nodes based on branch_id. Each node handles local queries
independently, minimizing inter-node communication and improving
response time.
d.   Explain the purpose of DTD and XML Schema in validating XML documents
Ans:
Both DTD (Document Type Definition) and XML Schema define the
structure, elements, and constraints of XML documents to ensure validity and
consistency.
Ensures data integrity and validates whether an XML document is well-formed
and valid according to its defined schema.
• Data Typing:
o DTD supports only basic text types like #PCDATA, whereas
XML Schema includes strong data types such as xs:string,
CO2.   xs:integer, xs:date, etc.   [5]
BL-1   • Syntax Compatibility:
o XML Schema is written in XML syntax, allowing it to be
processed by standard XML parsers; DTD uses a non-XML
syntax, requiring specialized processors.
• Order and Cardinality:
o XML Schema allows control over element order, repetition
(minOccurs, maxOccurs), and optional elements, giving greater
modeling precision.
• Namespace and Validation:
o XML Schema   supports namespaces and   hierarchical
validation, making it suitable for complex web applications.
a.   Discuss the concept of User-Defined Abstract Data Types (ADTs) in object-
relational databases with example
Ans:
documents, or nested objects. To handle such requirements, Object-Relational
Databases (ORDBMS) extend the relational model by introducing User-Defined
Q2
Abstract Data Types (ADTs) and Structured Types.   [10]
CO1; BL-1
An Abstract Data Type (ADT) is a user-defined data structure that bundles
together both data and the operations (methods) that can be performed on that
data.
ADTs allow programmers to create new types that behave like built-in data types,
enhancing flexibility and reusability.
********** 3 **********
--- page 4 ---
ADTs support encapsulation, information hiding, and data abstraction
Example [4M]
CREATE TYPE AddressType AS OBJECT (
street VARCHAR2(50),
city VARCHAR2(30),
pincode NUMBER(6)
);
CREATE TABLE Employee (
emp_id NUMBER PRIMARY KEY,
emp_name VARCHAR2(50),
emp_addr AddressType
);
b.   What is the importance of using modular programming with procedures and
functions in large databases?
Ans:
• Improved Code Reusability and Maintainability
Q2   • Enhanced Readability and Manageability
• Improved Performance   [10]
CO3; BL-2
•   Easier Debugging and Testing
•   Better Security and Access Control
• Promotes Collaboration and Scalability
Example:
A stored procedure for validating customer details can be called by different
modules like order processing or billing without rewriting the logic.
a.   Evaluate the different approaches for storing XML documents in databases and
discuss their impact on query performance and data management.
Ans:
• Using a DBMS to store the documents as text:
We can use a relational or object DBMS to store whole XML documents
as text fields within the DBMS records or objects. This approach can be
used if the DBMS has a special module for document processing and
would work for storing schemaless and document-centric XML
documents.
• Using a DBMS to store the document contents as data elements:
Q3   This approach would work for storing a collection of documents that
[10]
follow a specific XML DTD or XML schema. Since all the documents
CO3, BL-3
have the same structure, we can design a relational (or object) database
to store the leaf-level data elements within the XML documents.
• Designing a specialized system for storing native XML data:
A new type of database system based on the hierarchical (tree) model
would be designed and implemented. The system would include
specialized indexing and querying techniques and would work for all
types of XML documents.
•   Creating or publishing customized XML documents from pre-existing
relational databases:
Because there are enormous amounts of data already stored in relational
databases, parts of these data may need to be formatted as documents for
exchanging or displaying over the Web.
Q3   b.   Describe the key features and applications of Temporal, Spatial, and Mobile
CO4;   Databases. Compare their data models. How are these enhanced data models [10]
useful in modern systems such as Geographic Information Systems (GIS)?
BL-3   Ans:
********** 4 **********
--- page 5 ---
Temporal, spatial, and mobile databases extend the classical model with time,
geometry, and motion
• Temporal DBs: capture time-varying facts (valid time, transaction time, or
both → bitemporal).
•   Spatial DBs: manage geometric objects (points, lines, polygons, rasters) and
their topological/metric relations.
• Mobile (Moving-Object) DBs: manage location-changing entities and
context-aware data under mobility, disconnections, and limited resources.
1) Data Models
Temporal
• Time dimensions: valid-time (real-world), transaction-time (DB history),
bitemporal (both).
• Temporal types: time points/intervals; coalesced periods for identical
states.
• Schema idioms: PERIOD FOR columns; versioned rows (start_ts,
end_ts).
•   Semantics: snapshot vs period semantics; Allen’s interval relations
(before, overlaps, meets…).
Spatial
•   Geometries: vector (Point/LineString/Polygon, Multi-*) and raster
(grids).
•   Reference systems: CRS/SRID; topology (touches, within, contains,
intersects).
•   Standards: OGC Simple Features; SQL/MM Spatial; geometry/
geography types.
Mobile
•   Entities: moving objects (trajectories), location-dependent and
location-based data.
•   Models: time-parameterized location functions; spatio-temporal
objects (x,y,t).
•   Context: device state, network state, proximity, user profile.
GIS is inherently spatio-temporal: roads change (temporal), assets have geometry
(spatial), and users/vehicles move (mobile).
Enhanced analytics:
• Temporal: “What was the land-use in ward 14 in 2018 Q2?”
•   Spatial: “Which parcels intersect the proposed buffer?”
•   Mobile: “Live map of ambulances; alert when nearest unit within 3
min ETA.”
Applications:
• urban planning (historical zoning), traffic & logistics (real-time routing,
ETA),
•   disaster response (evacuation per evolving flood polygons),
•   environmental monitoring (moving plume fronts),
• epidemiology (case trajectories & exposure windows).
a.   What is the difference between persistent and transient objects? How is
persistence handled in typical Object-Oriented database systems?
Q4   Ans:
[10]
• Not all objects created by the OOPL are meant to be stored permanently in
CO3, BL3
the database
• Transient objects exist only during the OOPL program execution
********** 5 **********
--- page 6 ---
•   Persistent objects exist after program termination
• The typical mechanism for making an object persistent are naming the
object, or making it reachable.
o Naming Mechanism: Assign an object a unique persistent name
through which it can be retrieved by this and other programs.
b.   Construct a list partitioning example for a table PRODUCT (prod_id, prod_name,
category, price) where products are divided into categories like Electronics,
Furniture, and Clothing.
Explain how list partitioning benefits such categorical data.
Ans:
CREATE TABLE product (
prod_id NUMBER   NOT NULL,
prod_name VARCHAR2(100) NOT NULL,
category VARCHAR2(30) NOT NULL,
price   NUMBER(10,2) NOT NULL,
Q4   CONSTRAINT pk_product PRIMARY KEY (prod_id)
)
CO4;   PARTITION BY LIST (category)   [10]
BL-4   (
PARTITION p_electronics VALUES ('Electronics'),
PARTITION p_furniture VALUES ('Furniture'),
PARTITION p_clothing VALUES ('Clothing'),
PARTITION p_other   VALUES (DEFAULT) -- catches any other category
);
Benefit:
• Maintenance isolation
•   Faster loads
• DEFAULT safety
•   Local indexing & better concurrency
Q5   a.   Being a DBA, define a strategy for backup recovery plan in the event of
[10]
CO4, BL-3   hardware or software failure of online reservation system
********** 6 **********
--- page 7 ---
Ans:
• Understand the backup environment
• Perform capacity planning
• Analyze current policies and procedures
• Determine resource constraints
•   Create a Backup Recovery Management Plan
• Implement the plan
• Monitor the management plan
b. A library management system maintains records of books, library members, and
book borrowing activities. Each book has attributes such as ISBN, title, author,
publication Year, and availability Status. Members have attributes including
memberID, name, phone, and email. A member can borrow multiple books, but
each book has a limited number of copies. If all copies are currently borrowed, a
book is marked as unavailable. The system also tracks borrowing details,
including the date borrowed, return date, and any late fees. Additionally, some
books are marked as reference books and cannot be borrowed. Develop an ODL
schema for the library management system, including methods for checking
availability and borrowing books.
Ans:
class Book {
( extent books)
attribute string ISBN;
attribute string title;
attribute string author;
Q5
attribute short publicationYear;
CO3   attribute enum availabilityStatus { "Available", "Borrowed" };   [10]
attribute boolean isReference;
BL-4
relationship set Borrowing borrowings inverse Borrowing::borrows;
relationship set Book prerequisiteBooks inverse Book::prerequisites_for;
short checkAvailability();
string listPrerequisiteBooks();
boolean updateAvailability(boolean newStatus);
};
class Member {
( extent members)
attribute string memberID;
attribute string name;
attribute string phone;
attribute string email;
relationship set Borrowing borrowings inverse Borrowing::borrowed_by;
boolean borrowBook(string ISBN);
float calculateLateFees();
};
class Borrowing {
( extent borrowings)
attribute Date dateBorrowed;
attribute Date returnDate;
********** 7 **********
--- page 8 ---
attribute float lateFee;
relationship Book borrows inverse Borrowing::borrowings;
relationship Member borrowed_by inverse Borrowing::borrowings;
};
a.   Describe when a NoSQL database (e.g., MongoDB) is preferable to a relational
DB (e.g., MySQL). Include concrete scenarios that showcase NoSQL strengths
Ans:
Use Cases: Suitable for content management systems, real-time analytics, social
media platforms, and e-commerce where the schema frequently changes, or the
application needs to scale quickly.
• Advantages of NoSQL: Provides flexible schema, better horizontal
Q6   scaling, and optimized read/write performance for unstructured or semi-
[10]
CO4; BL-3   structured data.
• Real-World Examples: Applications like Facebook, Amazon, or a real-
time monitoring dashboard would benefit from MongoDB’s dynamic
schema and distributed nature.
Expected Points:
Students should mention specific scenarios where NoSQL’s strengths
(flexibility, scalability, performance) provide clear advantages over relational
databases.
b. A retail company uses a database with two key tables: ORDERS and
INVENTORY.
• ORDERS (order_id, product_id, quantity_ordered, order_date)
• INVENTORY (product_id, stock_level)
Q6
The company needs to automatically update the product's stock level whenever a [10]
CO2, BL-4
new order is placed, and the system must prevent an order from being recorded
if the ordered quantity exceeds the current stock level.
Design triggers to handle the above requirements
Ans:
********** 8 **********
--- page 9 ---
a.   Explain the architecture of mobile databases and discuss the key challenges in
managing data for mobile applications, such as disconnected operations, data
synchronization, and conflict resolution. Provide a real-world example of a
mobile application that benefits from mobile database concepts.
Ans:
Architecture:
•   Client-Server Model: Mobile databases use a client-server approach,
where data is stored on a local device and synchronized with a central
server.
Q7   • Local Storage: Allows for offline access and operations when [10]
CO4; BL-3   disconnected.
•   Synchronization Mechanism: Ensures data consistency between the
device and server.
Key Challenges:
• Disconnected Operations: Managing data availability when the device is
offline.
• Data Synchronization: Ensuring data is up-to-date when reconnecting.
•   Conflict Resolution: Handling data conflicts when multiple changes are
made offline.
Example:
********** 9 **********
--- page 10 ---
•   Evernote: Allows note-taking offline and syncs data across devices. Uses
mobile database architecture to ensure notes are available and consistent.
b.   Given the following four situations, identify which NoSQL type best fits and
explain why in one or two sentences each:
a) A user profile with nested, evolving attributes (preferences, addresses,
settings).
b) Clickstream/time-series event logs ingested at very high write rates.
c) Real-time product recommendations based on multi-hop relationships.
d) Session tokens and feature flags requiring microsecond key lookups.
Ans:
a) Nested, evolving user profile → Document DB
•   Natural document shape (nested addresses/prefs), easy partial updates,
Q7   flexible schema, per-document indexing.
[10]
CO4; BL-3   b) High-rate clickstream/time-series ingestion → Column-Family Store
•   Write-optimized LSM architecture, partition+cluster keys for time-
range scans, linear scale for hot write paths.
c) Real-time recommendations over multi-hop relations → Graph DB
•   Relationship-first model; constant-time neighbor lookups; expressive
traversals (e.g., “friends-of-friends who bought X”).
d) Session tokens & feature flags (microsecond lookups) → Key–Value
Store
•   access by key, in-memory latency, simple get/set with TTL for
sessions/toggles.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 9366e973c201

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_IT_7001/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (DS)/B. Tech (IT)/MBA Tech (IT)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Advanced Database Management Systems
Date: 11 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A software development company requires a database structure to manage its
intellectual property and sales records. The core entity is Software Product,
which is uniquely identified by Product ID and tracked by its Name and Release
Date. All products in the catalog are comprehensively categorized into two
mutually exclusive types: Operating Systems and Applications. Operating
Systems are described by their Minimum RAM Requirement and Kernel Type,
while Applications are detailed by their Version Number and Installation Size.
Applications themselves undergo further classification. They can be designated
as Games or Productivity Tools, though this designation is optional for some
CO1.   [5]
BL- 5   Applications (such as utilities). Importantly, an application cannot fall into both
the Game and Productivity Tool categories. Games require tracking of their
Genre, and Productivity Tools are associated with a Subscription Model.
Separately, the company manages Licenses, each having a unique License Key,
an Activation Date, and a Number of Seats. Every License must be tied to one
and only one Software Product, and every Software Product must have at least
one associated License, though typical products have many. Draw EER for above
mentioned problem statement.
Ans:
********** 1 **********
--- page 2 ---
b.   Explain the concept of object identity in Object-Oriented Databases. How does
it differ from the concept of primary key in relational databases
Ans:
Object identity (OID) in Object-Oriented Databases (OODB) is a system-
generated, permanent, and value-independent   identifier   that uniquely
distinguishes each object. An object keeps the same OID for its entire lifetime—
even if all its attribute values change, other objects can hold direct references
CO2.   [5]
BL- 2   (pointers) to it. Identity is thus about “this exact object instance” (state + behavior
+ identity).
How this differs from a Primary Key (PK) in relational databases
OID provides stable, value-independent identity and pointer-like referencing
suited to rich object graphs; a relational primary key is a value-based identifier
defined in the schema and used with foreign keys and joins for set-oriented
processing.
c.   Analyse how the Shared-Nothing approach improves scalability and performance
compared to the Shared-Disk model. Support your answer with an example of
data partitioning.
CO4. BL-3   Ans:   [5]
In the Shared-Nothing architecture, each processor (node) has its own CPU, main
memory, and disk storage, and communicates with other nodes through a high-
speed network. Unlike the Shared-Disk model, where multiple processors access
********** 2 **********
--- page 3 ---
common storage leading to contention and bandwidth bottlenecks, the shared-
nothing model ensures independent data access and parallel processing.
•   Scalability: Adding new nodes linearly increases both storage capacity
and processing power, achieving linear scale-up and speed-up.
•   Performance: Since there is no disk contention, query operations such as
scanning, sorting, and joins can be performed in parallel on separate
partitions.
• Example: In a banking database, account records can be hash-partitioned
across nodes based on branch_id. Each node handles local queries
independently, minimizing inter-node communication and improving
response time.
d.   Explain the purpose of DTD and XML Schema in validating XML documents
Ans:
Both DTD (Document Type Definition) and XML Schema define the
structure, elements, and constraints of XML documents to ensure validity and
consistency.
Ensures data integrity and validates whether an XML document is well-formed
and valid according to its defined schema.
• Data Typing:
o DTD supports only basic text types like #PCDATA, whereas
XML Schema includes strong data types such as xs:string,
CO2.   xs:integer, xs:date, etc.   [5]
BL-1   • Syntax Compatibility:
o XML Schema is written in XML syntax, allowing it to be
processed by standard XML parsers; DTD uses a non-XML
syntax, requiring specialized processors.
• Order and Cardinality:
o XML Schema allows control over element order, repetition
(minOccurs, maxOccurs), and optional elements, giving greater
modeling precision.
• Namespace and Validation:
o XML Schema   supports namespaces and   hierarchical
validation, making it suitable for complex web applications.
a.   Discuss the concept of User-Defined Abstract Data Types (ADTs) in object-
relational databases with example
Ans:
documents, or nested objects. To handle such requirements, Object-Relational
Databases (ORDBMS) extend the relational model by introducing User-Defined
Q2
Abstract Data Types (ADTs) and Structured Types.   [10]
CO1; BL-1
An Abstract Data Type (ADT) is a user-defined data structure that bundles
together both data and the operations (methods) that can be performed on that
data.
ADTs allow programmers to create new types that behave like built-in data types,
enhancing flexibility and reusability.
********** 3 **********
--- page 4 ---
ADTs support encapsulation, information hiding, and data abstraction
Example [4M]
CREATE TYPE AddressType AS OBJECT (
street VARCHAR2(50),
city VARCHAR2(30),
pincode NUMBER(6)
);
CREATE TABLE Employee (
emp_id NUMBER PRIMARY KEY,
emp_name VARCHAR2(50),
emp_addr AddressType
);
b.   What is the importance of using modular programming with procedures and
functions in large databases?
Ans:
• Improved Code Reusability and Maintainability
Q2   • Enhanced Readability and Manageability
• Improved Performance   [10]
CO3; BL-2
•   Easier Debugging and Testing
•   Better Security and Access Control
• Promotes Collaboration and Scalability
Example:
A stored procedure for validating customer details can be called by different
modules like order processing or billing without rewriting the logic.
a.   Evaluate the different approaches for storing XML documents in databases and
discuss their impact on query performance and data management.
Ans:
• Using a DBMS to store the documents as text:
We can use a relational or object DBMS to store whole XML documents
as text fields within the DBMS records or objects. This approach can be
used if the DBMS has a special module for document processing and
would work for storing schemaless and document-centric XML
documents.
• Using a DBMS to store the document contents as data elements:
Q3   This approach would work for storing a collection of documents that
[10]
follow a specific XML DTD or XML schema. Since all the documents
CO3, BL-3
have the same structure, we can design a relational (or object) database
to store the leaf-level data elements within the XML documents.
• Designing a specialized system for storing native XML data:
A new type of database system based on the hierarchical (tree) model
would be designed and implemented. The system would include
specialized indexing and querying techniques and would work for all
types of XML documents.
•   Creating or publishing customized XML documents from pre-existing
relational databases:
Because there are enormous amounts of data already stored in relational
databases, parts of these data may need to be formatted as documents for
exchanging or displaying over the Web.
Q3   b.   Describe the key features and applications of Temporal, Spatial, and Mobile
CO4;   Databases. Compare their data models. How are these enhanced data models [10]
useful in modern systems such as Geographic Information Systems (GIS)?
BL-3   Ans:
********** 4 **********
--- page 5 ---
Temporal, spatial, and mobile databases extend the classical model with time,
geometry, and motion
• Temporal DBs: capture time-varying facts (valid time, transaction time, or
both → bitemporal).
•   Spatial DBs: manage geometric objects (points, lines, polygons, rasters) and
their topological/metric relations.
• Mobile (Moving-Object) DBs: manage location-changing entities and
context-aware data under mobility, disconnections, and limited resources.
1) Data Models
Temporal
• Time dimensions: valid-time (real-world), transaction-time (DB history),
bitemporal (both).
• Temporal types: time points/intervals; coalesced periods for identical
states.
• Schema idioms: PERIOD FOR columns; versioned rows (start_ts,
end_ts).
•   Semantics: snapshot vs period semantics; Allen’s interval relations
(before, overlaps, meets…).
Spatial
•   Geometries: vector (Point/LineString/Polygon, Multi-*) and raster
(grids).
•   Reference systems: CRS/SRID; topology (touches, within, contains,
intersects).
•   Standards: OGC Simple Features; SQL/MM Spatial; geometry/
geography types.
Mobile
•   Entities: moving objects (trajectories), location-dependent and
location-based data.
•   Models: time-parameterized location functions; spatio-temporal
objects (x,y,t).
•   Context: device state, network state, proximity, user profile.
GIS is inherently spatio-temporal: roads change (temporal), assets have geometry
(spatial), and users/vehicles move (mobile).
Enhanced analytics:
• Temporal: “What was the land-use in ward 14 in 2018 Q2?”
•   Spatial: “Which parcels intersect the proposed buffer?”
•   Mobile: “Live map of ambulances; alert when nearest unit within 3
min ETA.”
Applications:
• urban planning (historical zoning), traffic & logistics (real-time routing,
ETA),
•   disaster response (evacuation per evolving flood polygons),
•   environmental monitoring (moving plume fronts),
• epidemiology (case trajectories & exposure windows).
a.   What is the difference between persistent and transient objects? How is
persistence handled in typical Object-Oriented database systems?
Q4   Ans:
[10]
• Not all objects created by the OOPL are meant to be stored permanently in
CO3, BL3
the database
• Transient objects exist only during the OOPL program execution
********** 5 **********
--- page 6 ---
•   Persistent objects exist after program termination
• The typical mechanism for making an object persistent are naming the
object, or making it reachable.
o Naming Mechanism: Assign an object a unique persistent name
through which it can be retrieved by this and other programs.
b.   Construct a list partitioning example for a table PRODUCT (prod_id, prod_name,
category, price) where products are divided into categories like Electronics,
Furniture, and Clothing.
Explain how list partitioning benefits such categorical data.
Ans:
CREATE TABLE product (
prod_id NUMBER   NOT NULL,
prod_name VARCHAR2(100) NOT NULL,
category VARCHAR2(30) NOT NULL,
price   NUMBER(10,2) NOT NULL,
Q4   CONSTRAINT pk_product PRIMARY KEY (prod_id)
)
CO4;   PARTITION BY LIST (category)   [10]
BL-4   (
PARTITION p_electronics VALUES ('Electronics'),
PARTITION p_furniture VALUES ('Furniture'),
PARTITION p_clothing VALUES ('Clothing'),
PARTITION p_other   VALUES (DEFAULT) -- catches any other category
);
Benefit:
• Maintenance isolation
•   Faster loads
• DEFAULT safety
•   Local indexing & better concurrency
Q5   a.   Being a DBA, define a strategy for backup recovery plan in the event of
[10]
CO4, BL-3   hardware or software failure of online reservation system
********** 6 **********
--- page 7 ---
Ans:
• Understand the backup environment
• Perform capacity planning
• Analyze current policies and procedures
• Determine resource constraints
•   Create a Backup Recovery Management Plan
• Implement the plan
• Monitor the management plan
b. A library management system maintains records of books, library members, and
book borrowing activities. Each book has attributes such as ISBN, title, author,
publication Year, and availability Status. Members have attributes including
memberID, name, phone, and email. A member can borrow multiple books, but
each book has a limited number of copies. If all copies are currently borrowed, a
book is marked as unavailable. The system also tracks borrowing details,
including the date borrowed, return date, and any late fees. Additionally, some
books are marked as reference books and cannot be borrowed. Develop an ODL
schema for the library management system, including methods for checking
availability and borrowing books.
Ans:
class Book {
( extent books)
attribute string ISBN;
attribute string title;
attribute string author;
Q5
attribute short publicationYear;
CO3   attribute enum availabilityStatus { "Available", "Borrowed" };   [10]
attribute boolean isReference;
BL-4
relationship set Borrowing borrowings inverse Borrowing::borrows;
relationship set Book prerequisiteBooks inverse Book::prerequisites_for;
short checkAvailability();
string listPrerequisiteBooks();
boolean updateAvailability(boolean newStatus);
};
class Member {
( extent members)
attribute string memberID;
attribute string name;
attribute string phone;
attribute string email;
relationship set Borrowing borrowings inverse Borrowing::borrowed_by;
boolean borrowBook(string ISBN);
float calculateLateFees();
};
class Borrowing {
( extent borrowings)
attribute Date dateBorrowed;
attribute Date returnDate;
********** 7 **********
--- page 8 ---
attribute float lateFee;
relationship Book borrows inverse Borrowing::borrowings;
relationship Member borrowed_by inverse Borrowing::borrowings;
};
a.   Describe when a NoSQL database (e.g., MongoDB) is preferable to a relational
DB (e.g., MySQL). Include concrete scenarios that showcase NoSQL strengths
Ans:
Use Cases: Suitable for content management systems, real-time analytics, social
media platforms, and e-commerce where the schema frequently changes, or the
application needs to scale quickly.
• Advantages of NoSQL: Provides flexible schema, better horizontal
Q6   scaling, and optimized read/write performance for unstructured or semi-
[10]
CO4; BL-3   structured data.
• Real-World Examples: Applications like Facebook, Amazon, or a real-
time monitoring dashboard would benefit from MongoDB’s dynamic
schema and distributed nature.
Expected Points:
Students should mention specific scenarios where NoSQL’s strengths
(flexibility, scalability, performance) provide clear advantages over relational
databases.
b. A retail company uses a database with two key tables: ORDERS and
INVENTORY.
• ORDERS (order_id, product_id, quantity_ordered, order_date)
• INVENTORY (product_id, stock_level)
Q6
The company needs to automatically update the product's stock level whenever a [10]
CO2, BL-4
new order is placed, and the system must prevent an order from being recorded
if the ordered quantity exceeds the current stock level.
Design triggers to handle the above requirements
Ans:
********** 8 **********
--- page 9 ---
a.   Explain the architecture of mobile databases and discuss the key challenges in
managing data for mobile applications, such as disconnected operations, data
synchronization, and conflict resolution. Provide a real-world example of a
mobile application that benefits from mobile database concepts.
Ans:
Architecture:
•   Client-Server Model: Mobile databases use a client-server approach,
where data is stored on a local device and synchronized with a central
server.
Q7   • Local Storage: Allows for offline access and operations when [10]
CO4; BL-3   disconnected.
•   Synchronization Mechanism: Ensures data consistency between the
device and server.
Key Challenges:
• Disconnected Operations: Managing data availability when the device is
offline.
• Data Synchronization: Ensuring data is up-to-date when reconnecting.
•   Conflict Resolution: Handling data conflicts when multiple changes are
made offline.
Example:
********** 9 **********
--- page 10 ---
•   Evernote: Allows note-taking offline and syncs data across devices. Uses
mobile database architecture to ensure notes are available and consistent.
b.   Given the following four situations, identify which NoSQL type best fits and
explain why in one or two sentences each:
a) A user profile with nested, evolving attributes (preferences, addresses,
settings).
b) Clickstream/time-series event logs ingested at very high write rates.
c) Real-time product recommendations based on multi-hop relationships.
d) Session tokens and feature flags requiring microsecond key lookups.
Ans:
a) Nested, evolving user profile → Document DB
•   Natural document shape (nested addresses/prefs), easy partial updates,
Q7   flexible schema, per-document indexing.
[10]
CO4; BL-3   b) High-rate clickstream/time-series ingestion → Column-Family Store
•   Write-optimized LSM architecture, partition+cluster keys for time-
range scans, linear scale for hot write paths.
c) Real-time recommendations over multi-hop relations → Graph DB
•   Relationship-first model; constant-time neighbor lookups; expressive
traversals (e.g., “friends-of-friends who bought X”).
d) Session tokens & feature flags (microsecond lookups) → Key–Value
Store
•   access by key, in-memory latency, simple get/set with TTL for
sessions/toggles.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper a58c5ef07127

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_DS_7052/Advanced Database Management Systems/ANS_Advanced Database Management Systems(702IT0E026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/MBA Tech (DS)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Advanced Database Management Systems
Date: 10 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a. CREATE OR REPLACE TYPE Address_Type AS OBJECT (
Street VARCHAR2(50),
City VARCHAR2(30),
ZipCode NUMBER
CO-1;   );
SO-1;   CREATE TABLE Customer (   [5]
BL-2   cust_id NUMBER,
cust_name VARCHAR2(50),
address Address_Type
);
[create type -2.5 M, Using in table -2.5M]
b   Type constructors are mechanisms used in object-oriented and advanced   [5]
database systems to build complex data types from simple (atomic) types.
They help in modeling real-world entities with multiple attributes and
relationships.[Definition-1M]
Common Type Constructors:[3M]
Tuple → Combines different attributes
CO-2;   Ex
SO-1;   Student = (RollNo, Name, Age)
BL-2   Set → Collection of unordered, unique elements
Ex. Courses = Set(Course)
List → Ordered collection (duplicates allowed)
Ex
PhoneNumbers = List(Number)
Complex objects are created by combining basic types using these
constructors: [1M]
********** 1 **********
--- page 2 ---
Library = (Name,Books   : Set(Book),Members   : Set(Member),
Issued_Books : List(Book))
c   [5]
1. Node Structure[2.5M]
• Shared-Nothing Architecture:
-Each node is independent and identical (homogeneous)
-Every node has its own: CPU ,Memory ,Disk
-No sharing of resources between nodes
-Designed for symmetry and uniformity
• Distributed Database System:
-Nodes can be heterogeneous
-Different nodes may have:
-Different hardware
-Different operating systems
CO-2;   -Different DBMS
SO-1;   -Data is distributed across multiple locations
BL-2   2. Execution [2.5M]
• Shared-Nothing Architecture:
-Execution is parallel and coordinated
-Query is divided into sub-tasks and executed simultaneously across
nodes
-Focus on performance and speed (parallel query processing)
-High degree of synchronization and control
• Distributed Database System:
-Execution is distributed but not necessarily parallel
-Each site processes its part and results are combined
-Focus on data distribution and autonomy
-Coordination is more complex due to heterogeneity
CO-3;   d   [5]
SO-1;   Any 5 valid points. 1 mark for each.
BL-2
a. CREATE OR REPLACE PROCEDURE calculate_late_fee(p_book_id
NUMBER)
IS
v_issue_date DATE;
v_return_date DATE;
BEGIN
SELECT issue_date, return_date
INTO v_issue_date, v_return_date
Q2   FROM Library
CO-3;   WHERE book_id = p_book_id;   [10]
SO-1;   IF v_return_date > v_issue_date THEN
BL-3   UPDATE Library
SET late_fee = 50
WHERE book_id = p_book_id;
ELSE
UPDATE Library
SET late_fee = 0
WHERE book_id = p_book_id;
END IF;
********** 2 **********
--- page 3 ---
COMMIT;
END;
/
[Procedure Declaration & Syntax -3 M ,Variable Declaration - 2 M,Logic-
5M]
b.   (Implementation – 5 marks)   [10]
use shopDB
// Create index
db.orders.createIndex({ customer: 1 })
// Compound index
Q2
db.orders.createIndex({ customer: 1, amount: -1 })
CO-4;
SO-1;   // Query using index
BL-1,4   db.orders.find({ customer: "Amit" })
(Explanation – 5 marks)
•   Indexes store references to document fields, enabling faster search.
•   Single-field index improves lookup on one attribute.
• Compound index supports queries on multiple fields.
•   Indexing reduces full collection scan, improving efficiency.
a.   class Customer   [10]
(
extent customers
)
{
attribute string customerID;
attribute string name;
attribute string email;
attribute string phoneNumber;
/* A customer can place multiple orders */
relationship set (Order) places inverse Order::placed_by;
Q3
long total_orders();
CO-1,2;   };
SO-1;
BL-2,4   class Order
(
extent orders
)
{
attribute string orderID;
attribute Date orderDate;
attribute float totalAmount;
attribute string orderStatus;
/* Each order is placed by exactly one customer */
relationship Customer placed_by inverse Customer::places;
********** 3 **********
--- page 4 ---
boolean cancel_order();
};
[Customer-5M,order-5M]
b.   Explanations of each below mentioned problem[2*5=10M]   [10]
– Dealing with multiple copies of the data items.
Q3   – Failure of individual sites.
CO-1,2;   – Failure of communication links.
SO-1;   – Distributed commit.
BL-1,2   – Distributed Deadlock
a.   (Tree Diagram – 5 marks)   [10]
company
└── department (dept_id="D1")
├── employee (emp_id="E01")
│ ├── name → Ravi
│ └── designation → Manager
Q4
└── employee (emp_id="E02")
CO-3;
SO-1;   ├── name → Sneha
BL-1,4
└── designation → Developer
(Theory – 5 marks)
• XML allows repeated elements (like multiple <employee> tags) under a
parent node.
•   This helps represent collections of similar data efficiently and maintains a
structured format.
b. A Geographic Information System (GIS) is a system designed to capture, store,   [10]
manage, analyze, and visualize geographically referenced (spatial) data.
It integrates spatial data (location, coordinates) with attribute data (descriptive
information) to represent real-world entities such as roads, buildings, rivers, etc.
GIS supports operations like mapping, spatial analysis, and decision-making in
Q4   domains such as urban planning, agriculture, disaster management, and
CO-4;   transportation. (5 marks)
SO-1;
BL-1,2   Spatial databases play a crucial role in GIS by efficiently storing and managing
spatial objects like points, lines, and polygons.
They provide specialized indexing techniques (e.g., R-trees) and support spatial
queries such as range queries, nearest neighbor, and spatial joins.
This enables fast retrieval and analysis of geographic data, making GIS applications
more efficient and scalable. (5 marks)
Q5   a. A Mobile Database is a database that supports data access and management on   [10]
CO-4;   mobile devices such as smartphones and tablets through wireless communication.
SO-1;
********** 4 **********
--- page 5 ---
BL-1,2   It allows users to access and manipulate data anytime and anywhere, even in
distributed environments.
Mobile databases are widely used in applications like mobile banking, e-commerce,
navigation systems, and field data collection. (5 marks)
Mobile data management faces several challenges such as limited bandwidth,
frequent disconnections, low battery power, and security issues.
These challenges are addressed using techniques like data caching (local storage),
synchronization mechanisms, lightweight protocols, and encryption for
security.
Such solutions ensure data consistency, improve performance, and provide reliable
access in mobile environments. (5 marks)
b.   [10]
(Architecture – 5 marks)
MongoDB follows a document-oriented architecture designed for scalability and
high performance.
• The basic unit of data is a document (stored in BSON format), which
consists of key–value pairs similar to JSON.
• Documents are grouped into collections, which are analogous to tables in
relational databases but do not enforce a fixed schema.
• A MongoDB deployment typically includes:
o Client (Application): Sends requests (queries, inserts, updates).
o MongoDB Server: Processes requests and manages data storage.
o Database: Contains multiple collections.
Q5   • MongoDB supports replica sets (for high availability) and sharding
CO-4;   architecture (for horizontal scaling), where data is distributed across
SO-1;
BL-1,4   multiple servers.
(Key Features – 5 marks)
•   Collections & Documents:
Collections store documents without requiring a predefined schema,
allowing flexibility in data representation. Each document has a unique _id
field.
• Schema Flexibility:
Documents in the same collection can have different structures, making
MongoDB suitable for evolving applications.
•   Scalability (Sharding):
MongoDB distributes data across multiple nodes using sharding, enabling
handling of large-scale data efficiently.
********** 5 **********
--- page 6 ---
• High Availability:
Replica sets maintain multiple copies of data, ensuring fault tolerance and
automatic failover.
•   Efficient Querying & Indexing:
Supports indexing on fields, improving query performance for large
datasets.
a.   [10]
Q6
CO-1;
SO-1;   [Diagram-identifying entities, attributes, relationship-6M]
BL-6   Relational schema[4M]
PERSON(Person_ID, Name, Date_of_Birth, Address)
STUDENT(Person_ID, Roll_No, Program, Year)
FACULTY(Person_ID, Employee_ID, Designation, Dept_ID)
STAFF(Person_ID, Employee_ID, Job_Role, Salary, Dept_ID)
UNDERGRADUATE(Person_ID, Major)
POSTGRADUATE(Person_ID, Specialization, Research_Area)
COURSE(Course_ID, Course_Name)
DEPARTMENT(Dept_ID, Dept_Name)
ENROLLMENT(Person_ID, Course_ID)
TEACHES(Person_ID, Course_ID)
b.   [10]
Q6   Function   Procedure
CO-3;   Must return a value using   Does not return value (can use
SO-1;   RETURN   OUT parameters)
BL-3   Cannot be used directly in SQL
Can be used in SQL queries
queries
********** 6 **********
--- page 7 ---
Performs computation and
Performs action or task
returns result
Only IN parameters   IN, OUT, IN OUT parameters
(generally)   allowed
Used in expressions   Called as standalone statement
CREATE OR REPLACE FUNCTION calc_interest(p_acc_no NUMBER)
RETURN NUMBER
IS
v_balance NUMBER;
v_interest NUMBER;
BEGIN
-- Fetch balance
SELECT balance INTO v_balance
FROM Account
WHERE acc_no = p_acc_no;
v_interest := v_balance * 0.07;
RETURN v_interest;
EXCEPTION
WHEN NO_DATA_FOUND THEN
RETURN 0;
END;
/
[difference-5M, Function code-5M]
a. CREATE TABLE transactions (   [10]
txn_id INT,
account_no INT,
amount DECIMAL(10,2),
transaction_date DATE
) PARTITION BY RANGE (transaction_date);
Q7
CO-1,2;   CREATE TABLE transactions_jan2024
SO-1;
BL-1,2   PARTITION OF transactions
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
CREATE TABLE transactions_feb2024
PARTITION OF transactions
FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
[main table-3M
Jan partition-2M
********** 7 **********
--- page 8 ---
Feb partition-2M
Syntax and correctness-3M]
b.   1. AllDepartments → Persistent   [10]
Because it is declared using:
persistent name AllDepartments: DepartmentSet;
Hence, it is explicitly persistent (Persistence by Naming)
d1 → Persistent
Created as a transient object initially
Becomes persistent when added to AllDepartments:
Q7   AllDepartments.add_dept(d1);
It is reachable from a persistent object
CO-1,2;
So, persistent by Reachability
SO-1;   d2 → NOT Persistent
It is created but not added or referenced by any persistent object
BL-2,4
Therefore AllDepartments,d1 persistent and d2 not persistent object
2. Then object d is removed from AllDepartments:
It is no longer reachable from any persistent object
Therefore Object d is not persistent
[1st question 6M identifying all object and justification]
[2nd question -4marks]
********** 8 **********
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 87c5dfc63a77

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Advanced Database Management System/ANS_Advanced Database Management System(703CO0E018)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2025
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Advanced Database Management System
Date: 08 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks
7. Assume Suitable data if necessary.
Q. l   Answer briefly:   [20]
a.   Design Extended ER diagram for following with suitable example:
CO-1; SO-   [5]
a) Specialization and Generalization
1, BL-2
b) Aggregation
Identify entities (1)
Identify attributes (1)
Generalization / Specialization draw (2)
Aggregation (if possible) (1)
CO-4; so- 1;   b. How Fault Tolerance can be prevents in distributed environment?   [5]
BL-3   Problem (2) solution/Reason: Replication, distribution of data across the
n/w (3)
CO- 3; SO- c.   Discuss OQL and SQL in detail.   [5]
1 ;
BL-2
Any 5 points(5)
CO- 2; SO- d.   Discuss %TYPE and %ROWTYPE in PL/SQL with suitable example.   [5]
1;
BL-2   Explain both in detail.(2)
Take suitable example (3)
%TYPE attribute
variable_name {other_variable_name | table_name.column_name}%TYPE
%ROWTYPE attribute:
variable_name \table_name%ROWTYPE variable_name QUERY LIKE
table_name%ROWTYPE
********** 1 **********
--- page 2 ---
Q2   Design EER diagram for A General Hospital consists of a number of
specialized wards (such as Maternity, Paediatric, Oncology, etc). Each
COl;SO2;   ward hosts a number of patients, who were admitted on the [10]
BL-6
recommendation of their own GP and confirmed by a consultant employed
by the Hospital. On admission, the personal details of every patient are
recorded. A separate register is to be held to store the information of the
tests undertaken and the results of a prescribed treatment. A number of
tests may be conducted for each patient. Each patient is assigned to one
leading consultant but may be examined by another doctor, if required.
Doctors are specialists in some branch of medicine and may be leading
consultants for a number of patients, not necessarily from the same ward.
Note: Consider EER features while designing EER diagram. Assume
suitable data if required.
Identify entities (2)
Identify attributes (2)
Relation (1)
Cardinality (1)
Generalization / Specialization draw (2)
Aggregation (2)
CO-2; SO- b   Refer following Schema:   [10]
2;
BL-2   Employee (eid, ename, eage,edob)
Dept (did, dname, domain)
work(eid, did, achievement)
For above schema, write an anonymous PL/SQL block that
i.   Defines a cursor that points to a record set that contains the
Employee’s names, achievement and dept name where the domain
is ‘Robotics’
ii.   Apply implicit cursor on above given schema (any one of your
choice)
i , ii (5marks each)
Q3   a   [10]
Discuss RDBMS / OODBMS /ORDBMS in detail.
co-3; so-1,
BL-4
********** 2 **********
--- page 3 ---
CO-2;   b   Explain Trigger in brief. Also discuss types of triggers. Write a code to fire [10]
SO-1;   the trigger for INSERT / UPDATE / DELETE operations performed on the
BL-3   table with suitable example.
In PL/SQL, a cursor is a pointer that helps you retrieve multiple rows
from a database query one at a time. Cursors are commonly used in cases
where you need to process each row of a query individually, rather than
retrieving all the rows at once.
There are two main types of cursors in PL/SQL:
1. Implicit Cursor: Automatically created by Oracle for SQL
statements like SELECT INTO, INSERT, UPDATE, and DELETE that
return a single result set. You don't need to explicitly declare or
manage them.
********** 3 **********
--- page 4 ---
2. Explicit Cursor: You declare and control the cursor manually.
This is used when you want to process multiple rows from a
SELECT query.
Q4   a   Write a PL/SQL program with a function to calculate factorial on the   [10]
CO-2;   given number.
SO-2;
BL-3   Syntax (4)
Logic(6)
CREATE [OR REPLACE] FUNCTION function_name
(parameter_name type [, …])
— This statement is must for functions
RETURN return_datatype
{IS | AS}
BEGIN
— program code
[EXCEPTION
exception_section;
END [function_name];
CO-4;   b   Discuss concept of Distributed database. Explain how efficiently query   [10]
processing is handled in distributed database.
SO-1 ;
BL-2   8-10 points (10)
Q5   a   [10]
Create a XML data model and Tree model for Company which deals with
CO-3;
SO-1;   Company, Employee, Department etc.
********** 4 **********
--- page 5 ---
BL-2   company
│
├── department (name="Engineering")
│ ├── employee (id="101")
│ │ ├── name: John Doe
│ │ ├── position: Software Engineer
│ │ ├── salary: 80000
│ ├── employee (id="102")
│   ├── name: Jane Smith
│   ├── position: DevOps Engineer
│   ├── salary: 85000
│
├── department (name="HR")
├── employee (id="201")
├── name: Emily Johnson
├── position: HR Manager
├── salary: 75000
XML data model (5) and Tree model (5)
CO-1;   b Perform following using PL/SQL:   [10]
SO-1 ;
BL-2   i.   Write a PL/SQL Program to find the Armstrong numbers from 2
to 100.
a. [Armstrong numbers: A number that is equal to the sum
of its digits each raised to the power of the number of
digits in the number.]
ii.   Perform following using switch case
• Square of number
• Half value of number
• Square root of number
• Cube of number
Each (5)
declare
-- declare variable n, s,r, len
-- and m of datatype number
n number:=1634;
s number:=0;
r number;
len number;
m number;
begin
m := n;
len := length(to_char(n));
********** 5 **********
--- page 6 ---
-- while loop till n>0
while n>0
loop
r := mod(n , 10);
s := s + power(r , len);
n := trunc(n / 10);
end loop;
if m = s
then
dbms_output.put_line('yes');
else
dbms_output.put_line('no');
end if;
end;
-- End program
---------------------------
CASE selector
WHEN 'value1' THEN S1;
WHEN 'value2' THEN S2;
WHEN 'value3' THEN S3;
...
ELSE Sn; -- default case
END CASE;
Q6   a   [10]
CO-1; SO-   Find out Given number is prime or Not, using GOTO statement in PL/SQL.
1;
GOTO label;
...
...
<< label >>
statement;
Logic (7)
Syntax (3)
BL-2
CO-3;   b   Explain DTD in XML. Discuss features of DTD. Discuss DTD and XML format for [t0]
SO-1;
BL-4   Employee.
Differentiation (3)
3-4 points
XML (3)
DTD (4)
Explain Types of exception handling in PL/SQL. Write a PL/SQL program for   [t0]
a   Exception handling when no Employee with EMPID value em101 is present in
Q7
database. Also write syntax of raising an exception.
CO-1;
Types (1)
SO-1 ;
BL-1   Pre-defined exceptions
NO_DATA_FOUND
********** 6 **********
--- page 7 ---
no data found in SELECT…INTO
TOO_MANY_ROWS
SELECT…INTO produces more than one row
INVALID_CURSOR
Cursor already closed
CURSOR_ALREADY_OPEN
Cursor already open
ZERO_DIVIDE
Division by zero
INVALID_NUMBER
Data is not numeric
DECLARE
e_TooManyStudents   EXCEPTION;
BEGIN
-- process data here
EXCEPTION
WHEN exception_Name1 THEN
statements;
WHEN exception_Name2 THEN
statements;
WHEN OTHERS THEN
statements;
END;/
co 4; so-   b   Discuss an application which following architecture is most suitable:   [10]
1;BL-2   Central Database, Parallel DBMS, Distributed DBMS.
Define all 3 (3)
Application each (7)
********** 7 **********
````

## 2023-24 · Final-Exam · Sem 2 · Answer key · paper 3fe06011e771

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2023/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Advanced Database Management System/ANS_Advanced Database Management System(703CO0E018)_2023-2024.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 Apr 2024
- Text: text (13 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II (Exam Year: 2023-2024)
Subject: Advanced Database Management System
Date: 26 Apr 2024   Time: 10:00 am - 01:00 pm (03:00 Hrs.)
Max Marks:   100
FINAL EXAMINATION(2023-2024)
Instructions:
1. This Synoptic paper contains 13 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1. 1 This is a sample question group   20
5
Page 1 of 13
--- page 2 ---
1. nIn a database for vehicle registration, a vehicle owner can be a PERSON, a BANK (holding a
lien on a vehicle) or a COMPANY.
nA category (UNION type) called OWNER is created to represent a subset of the union of the
three superclasses COMPANY, BANK, and PERSON
nA category member must exist in at least one of its superclasses
5
Page 2 of 13
--- page 3 ---
2.
3. XML semi-structured model organizes data hierarchically and in a nested format. This   5
organization is based on parent-child relationships, where elements can have sub-elements
(children) and attributes. Here's how the XML semi-structured model organizes data:
Hierarchical Structure:
Data is structured in a tree-like hierarchy.
Elements can have parent-child relationships.
Elements closer to the root are considered higher-level or parent elements, while elements
nested within them are lower-level or child elements.
This structure allows for organizing data in a logical and hierarchical manner.
Nested Elements:
Elements can contain other elements, creating a nested structure.
Nested elements represent relationships and dependencies between different parts of the data.
For example, in an XML document representing a book, the <book> element can contain
nested elements like <title>, <author>, <publisher>, and so on.
Page 3 of 13
--- page 4 ---
Attributes:
Elements can have attributes that provide additional information about the element.
Attributes are specified within the start tag of an element and are used to define
characteristics or properties of the element.
Attributes are useful for providing metadata or specific details associated with an element.
For example, in an XML document representing a product, the <product> element may
have attributes like id, name, price, etc., to describe the product's unique identifier, name,
and price.
Example: Any example
4. Object structure (i,c,v)   5
Type Constructors:
In OO databases, the state (current value) of a complex object may be constructed from
other objects (or other values) by using certain type constructors.
The three most basic constructors are atom, tuple, and set.
Other commonly used constructors include list, bag, and array.
The atom constructor is used to represent all basic atomic values, such as integers, real numbers,
character strings, Booleans, and any other basic data types that the system supports directly.
o 1 = (i 1 , atom, ‘Houston’)
o 2 = (i 2 , atom, ‘Bellaire’)
o 3 = (i 3 , atom, ‘Sugarland’)
o 4 = (i 4 , atom, 5)
o 5 = (i 5 , atom, ‘Research’)
o 6 = (i 6 , atom, ‘1988-05-22’)
o 7 = (i 7 , set, {i1, i2, i3})
2. 2 Solve(Attempt Any 4 Questions)   80
1.   20
1. Cursor can be divided into two types based on the condition under which they are created and   10
used:
1. Implicit Cursor
2. Explicit Cursor
Implicit Cursor
Page 4 of 13
--- page 5 ---
The cursor which is automatically created, maintained and closed by the Oracle engine while
execution of any DML(Data Manipulation Language) queries
like INSERT, UPDATE or DELETE are called Implicit Cursor.
Implicit Cursors are controlled by Oracle and programmers cannot access its information.
When a DML statement is executed an implicit cursor is created and attached to it.
Explicit Cursor
The cursor which has to be created, maintained and closed by a program through PL/SQL code
for the execution of any SELECT query that returns more than one row is called Explicit
Cursor.
It is a user-defined cursor declared in the Declare section of PL/SQL block and is used in its
Executable section.
Using Explicit Cursor
To define a cursor, one need to follow the following steps:
DECLARE the Cursor
It is done in the Declare section of the PL/SQL code by writing SQL statement that retrieves
data for processing.
Syntax:
CURSOR <cursor_name> IS <SELECT query>;
Copy
For example, if we have users table with columns id,name and email, then for executing
a SELECT query this is how we can declare a cursor:
CURSOR c_users IS
SELECT id, name, email FROM users;
Copy
OPEN the Cursor
It is done in the Begin section of the PL/SQL code. By opening the cursor, the cursor is
allocated the memory for fetching records.
Syntax:
OPEN <cursor_name>;
Copy
For the c_users cursor declared above, it will be:
OPEN c_users;
Copy
FETCH the Cursor
Page 5 of 13
--- page 6 ---
To fetch the data from the cursor one row at a time into memory variables we use
the FETCH command.
Syntax:
fetch <cursor_name> into <list_of_variables>;
To check whether the cursor is open or not we use the %ISOPEN attribute of the cursor.
Syntax:
if <cursor_name> %ISOPEN
To determine whether fetch was successful or not. This can be done by
using FOUND or NOT FOUND attributes because if fetch command fails to retrieve any
row from cursor then it sets found as false and not found as true.
For processing the data held in the memory variables we need a loop(We will come to this
in a short while).
Use the Exit statement to exit from the loop after the processing is complete.
Then, to Close the cursor, use the CLOSE command.
Syntax:
CLOSE cursorname;
2. 1-Tier Architecture   10
2. 2-Tier Architecture
3. 3-Tier Architecture
2.   20
1. Entity sets, attributes, relationships, Specialization/generalization, union, keys.   10
10
2.   The declaration section allows you to define data types, structures, and variables. You often
declare variables in the declaration section by giving them names, data types, and initial
values.
The execution section is required in a block structure and it must have at least one
statement. The execution section is the place where you put the execution code or business
logic code. You can use both procedural and SQL statements inside the execution section.
The exception handling section is starting with the EXCEPTION keyword. The exception
section is the place that you put the code to handle exceptions. You can either catch or
Page 6 of 13
--- page 7 ---
handle exceptions in the exception section.
Describe each section in detail.
3.   20
1. i) CREATE or REPLACE TRIGGER Before_Update_Stat_product   10
BEFORE
UPDATE ON product
Begin
INSERT INTO product_check
Values('Before update, statement level',sysdate);
END;
/
ii) CREATE or REPLACE TRIGGER Before_Upddate_Row_product
BEFORE
UPDATE ON product
FOR EACH ROW
BEGIN
INSERT INTO product_check
Values('Before update row level',sysdate);
END;
/
2. Creating a Function:   10
Use the CREATE FUNCTION statement to create a new function in the database. Specify the
function name, input parameters (if any), return type, and function body.
Example of creating a simple function:
Page 7 of 13
--- page 8 ---
sql
CREATE FUNCTION calculate_area(radius NUMBER)
RETURN NUMBER
IS
area NUMBER;
BEGIN
area := 3.14 * radius * radius;
RETURN area;
END calculate_area;
In this example, calculate_area is the function name, radius is the input parameter, NUMBER
is the return type, and the function calculates and returns the area of a circle based on the
radius.
Altering a Function:
Use the ALTER FUNCTION statement to modify an existing function's definition.
You can alter a function to change its parameters, return type, or function body.
Example of altering a function (changing return type):
sql
ALTER FUNCTION calculate_area(radius NUMBER)
RETURN VARCHAR2
IS
area_desc VARCHAR2(100);
BEGIN
area_desc := 'The area of the circle is ' || TO_CHAR(3.14 * radius * radius);
RETURN area_desc;
END calculate_area;
In this example, the return type of the calculate_area function is changed from NUMBER to
VARCHAR2, and the function now returns a descriptive string instead of a numerical value.
Dropping a Function:
Use the DROP FUNCTION statement to remove an existing function from the database.
Specify the function name to be dropped.
Example of dropping a function:
sql
DROP FUNCTION calculate_area;
This statement removes the calculate_area function from the database.
4.   20
1. OODBMS   RDBMS   10
Main objectives: data encapsulation and Main objective: ensuring data independence
independence.   from application programs.
Page 8 of 13
--- page 9 ---
Independence of classes: classes can be Data independence: Data can be reorganized
reorganized without affecting the mode of and modified without affecting the mode of
using them.   using them.
OODBMS store data and methods.   RDBMS store only data.
Data partitioning: data can be partitioned
Encapsulation: the data can be used only
depending on the requirements of the users
through their classes’ methods.
and on the specific user’s applications.
Passive data: the data are passive. Certain
Active objects: the objects active. Requests operations, which are   limited, can be
cause objects to execute their methods.   automatically brought into use when the data
are used.
Complexity: the structure of data may be Simplicity: users perceive data as columns,
complex, involving different types of data.   rows/tuples and tables.
Chained data: data can be chained so that the
methods of classes may bring about increased Separate   Tables: each   relation/table   is
performance. Structured data such as BLOBS separate. The Join Operator refers data from
(binary large objects) are used for sound, separate tables.
image, video etc.
Data non-redundancy: data normalization
Non-redundancy of methods: data and
aims   at   eliminating   or reducing   data
methods non-redundancy is achieved through
redundancy.   It is used in the stage of
encapsulation and inheritance. Inheritance
designing the database and not in the stage of
helps to reduce the redundancy of methods.
developing the applications.
Optimizing classes: the data for an object can
be interrelated and stored together, so that RDBMS performance is related to the level
they may all be accessed by the access of complexity of the data structure.
mechanism
2. Fragmentation is a process of dividing the whole or full database into various subtables or sub   10
relations so that data can be stored in different systems.
Horizontal fragmentation refers to the process of dividing a table horizontally by assigning
each row (or a group of rows) of relation to one or more fragments.
Vertical fragmentation refers to the process of decomposing a table vertically by attributes or
columns. In this fragmentation, some of the attributes are stored in one system and the rest are
stored in other systems.
The combination of vertical fragmentation of a table followed by further horizontal
fragmentation of some fragments is called mixed or hybrid fragmentation.
Page 9 of 13
--- page 10 ---
5.   20
10
1. Data Consistency
The Challenge: The most significant issue in a distributed database is maintaining
data consistency across all nodes. If one node updates a piece of data, all other
nodes must reflect this change to avoid conflicting or stale data.
The Solution: One common approach to tackling this is to use consensus
algorithms like Paxos or Raft. These algorithms ensure that operations are
conducted in the same sequence across all nodes, guaranteeing consistency. Some
databases also implement eventual consistency models, which prioritize
availability and partition tolerance over immediate consistency.
2. Partition Tolerance and Network Latency
The Challenge: Network issues like delays or outages can impede the performance
of a distributed database, making it difficult to meet the requirements of the CAP
theorem — which states that it’s impossible for a distributed system to
simultaneously provide consistency, availability, and partition tolerance.
The Solution: Techniques such as data replication and sharding can mitigate this
issue. Replication provides multiple copies of the data, ensuring availability and
fault tolerance. Sharding divides the database into partitions, or “shards,” which
can be hosted on separate servers to reduce latency.
3. Security and Authorization
The Challenge: Distributed databases are often more exposed to security risks due
to their nature. Unauthorized access, data leaks, and other vulnerabilities can
compromise the entire system.
Page 10 of 13
--- page 11 ---
The Solution: Robust authentication mechanisms, encryption, and regular security
audits can significantly enhance security. Solutions like Zero-Knowledge Proofs
can verify the integrity of transactions without exposing actual data.
4. Query Processing and Optimization
The Challenge: Querying a distributed database is far more complex than querying
a centralized one. Data from multiple nodes might need to be combined, and the
query has to be optimized for performance.
The Solution: Advanced query optimization algorithms and cost-based query
planners can optimize query execution. Distributed query execution engines can
break down a query into sub-queries, execute them on appropriate nodes, and then
combine the results.
5. Backup and Recovery
The Challenge: In a distributed database, ensuring that all nodes are backed up
consistently is a non-trivial task. A failure in one node might lead to data loss if
not handled correctly.
The Solution: Distributed backup solutions and real-time replication can be used to
safeguard against data loss. Some systems use log-based or snapshot-based
backups that synchronize across all nodes.
6. Scalability
The Challenge: As the data grows, scaling becomes a considerable challenge. How
do you distribute the load evenly and ensure that the system can handle more data
points or queries?
Page 11 of 13
--- page 12 ---
The Solution: Elasticity, or the ability to add or remove nodes dynamically, can
significantly help with scalability. Auto-sharding features can automatically
redistribute data among nodes as the system scales.
1.
2. XML Schema (XSD), also known as XML Schema Definition, is a more advanced and   10
powerful way to define the structure, elements, data types, and constraints for XML documents
compared to XML DTD (Document Type Definition). It provides a richer set of features for
validating and describing XML documents.
Take with suitable example to describe the XML Schema.
6.   20
1. Approaches to Storing XML Documents   10
Using a DBMS to store the documents as text:
We can use a relational or object DBMS to store whole XML documents as text fields within
the DBMS records or objects. This approach can be used if the DBMS has a special module
for document processing, and would work for storing schemaless and document-centric XML
documents.
Using a DBMS to store the document contents as data elements:
This approach would work for storing a collection of documents that follow a specific XML
DTD or XML schema. Since all the documents have the same structure, we can design a
relational (or object) database to store the leaf-level data elements within the XML documents.
Designing a specialized system for storing native XML data:
A new type of database system based on the hierarchical (tree) model would be designed and
implemented. The system would include specialized indexing and querying techniques, and
would work for all types of XML documents.
Creating or publishing customized XML documents from pre-existing relational databases:
Because there are enormous amounts of data already stored in relational databases, parts of
these data may need to be formatted as documents for exchanging or displaying over the Web.
2. DECLARE   10
t_dt DATE := To_date('&input_a_date', 'DD-MON-YYYY');
t_day VARCHAR2(1);
BEGIN
t_day := To_char(t_dt, 'D');
CASE t_day
WHEN '1' THEN
dbms_output.Put_line ('The date you entered is Sunday.');
Page 12 of 13
--- page 13 ---
WHEN '2' THEN
dbms_output.Put_line ('The date you entered is Monday.');
WHEN '3' THEN
dbms_output.Put_line ('The date you entered is Tuesday.');
WHEN '4' THEN
dbms_output.Put_line ('The date you entered is Wednesday.');
WHEN '5' THEN
dbms_output.Put_line ('The date you entered is Thursday.');
WHEN '6' THEN
dbms_output.Put_line ('The date you entered is Friday.');
WHEN '7' THEN
dbms_output.Put_line ('The date you entered is Saturday.');
END CASE;
END;
/
Page 13 of 13
````
