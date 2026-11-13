# Database Administration: question papers in full

14 unique papers · 2023-24 to 2025-26 · Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 6 · paper f890f59716bd

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Database Administration/QP_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Database Administration
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1;   a.   Explain the concept of 3-tier architecture in database systems. Describe the role
BL-2   of each tier in processing user requests.
CO-2;   b.   A developer needs to create tables but should not perform backup operations.
BL-2   How would you apply the principle of least privilege while creating this user?
CO-2;   c.   Describe the role of control files in an Oracle database. Describe the type of
BL-3   information stored in control files and its importance in database startup.
CO-2;   d.   Explain the concept of shared server architecture in Oracle. Describe how it
BL-2   improves scalability and resource utilization in a multi-user environment.
a.   A company is deploying an Oracle Database system for a multi-user enterprise
application. As a database administrator, you are required to illustrate and
explain the Oracle Database Architecture. demonstrate how the database [10]
Q2
instance (memory structures and background processes) interacts with the
CO-1;
physical database components (data files, control files, and redo log files)
BL-3
b.   A company observes performance issues due to improper memory allocation.
The DBA decides to modify database initialization parameters. Explain how [10]
initialization parameters are configured and modified in Oracle.
a.   In an organization, a user was mistakenly granted full access to critical database
tables, resulting in potential security risks and violation of access control
[10]
policies. Evaluate how a DBA should analyse and correct this situation by
Q3
appropriately granting and revoking privileges in an Oracle database system.
CO-2;
b.   A company uses both traditional client/server applications and web-based
BL-3
applications to access its Oracle database. Analyse the differences between
[10]
these connection architectures. Examine how Oracle Net supports both models
and how each impacts performance and scalability.
Q4   a.   An enterprise HR application built on Oracle experiences slow query
CO-1.   performance during peak hours. Investigation reveals frequent hard parsing and [10]
CO2 ;   high CPU usage, even though the queries are repetitive.
********** 1 **********
--- page 2 ---
BL-4   Analyse the possible causes of this issue by examining the role of the Shared
Pool and Library Cache. Suggest how improper memory usage can lead to this
performance problem.
b.   Analyze the differences between legal and   illegal multiplexed log
configurations in Oracle. Examine how the placement and structure of redo log [10]
members affect database reliability, fault tolerance, and recovery.
a.   Scenario
The finance department uses a FIN_TRANSACTIONS table. Incorrect
privilege assignment previously caused accidental deletions.
Roles Required
• FIN_READ_ROLE
• FIN_UPDATE_ROLE
Requirements
1. Junior accountants:
o Can only SELECT records
[10]
2. Senior accountants:
o Can UPDATE but cannot DELETE
3. Finance head:
Q5
o   Full access
CO-2,3;
Student Tasks
BL-5
•   Create roles with granular privileges
•   Assign roles to users
•   Demonstrate why DELETE privilege should not be granted broadly
• Revoke DELETE from a role and observe impact
b.   A medium-sized company is planning to migrate its existing on-premises
database to the cloud to take advantage of scalability and cost savings. The
company's data is critical for its daily operations.
Question:
• What considerations would you take into account when planning and [10]
executing the migration of the database to the cloud? How would you
ensure data consistency and minimize downtime during the migration
process?
•   Define backup and recovery policy for above organization.
Evaluate a scenario where frequent redo log switches are degrading database
Q6   a.   performance. Critically assess different redo log configuration strategies (such
[10]
CO-2,   as log file size, number of groups, and switching frequency), and justify the
CO3 ;   most effective approach to optimize performance and maintain system stability.
BL-5,3   b.
Differentiate Proactive Monitoring and Bottleneck Elimination with example.   [10]
a.   Apply your understanding to classify the different types of failures (such as soft
failure, hard failure, and network failure) that may occur in a database system.
Demonstrate how Oracle handles each type of failure using appropriate [10]
Q7
recovery mechanisms, including the role of redo logs, undo data, and backups
CO-3;
in restoring the database to a consistent state.
BL-4
b.   Evaluate the process of manually creating control files in Oracle Database.
Under what circumstances would a DBA need to recreate control files, and   [10]
what precautions should be taken?
********** 2 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 479cc8633a21

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Database Administration/QP_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Database Administration
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1;   a.   Explain the concept of 3-tier architecture in database systems. Describe the role
BL-2   of each tier in processing user requests.
CO-2;   b.   A developer needs to create tables but should not perform backup operations.
BL-2   How would you apply the principle of least privilege while creating this user?
CO-2;   c.   Describe the role of control files in an Oracle database. Describe the type of
BL-3   information stored in control files and its importance in database startup.
CO-2;   d.   Explain the concept of shared server architecture in Oracle. Describe how it
BL-2   improves scalability and resource utilization in a multi-user environment.
a.   A company is deploying an Oracle Database system for a multi-user enterprise
application. As a database administrator, you are required to illustrate and
explain the Oracle Database Architecture. demonstrate how the database [10]
Q2
instance (memory structures and background processes) interacts with the
CO-1;
physical database components (data files, control files, and redo log files)
BL-3
b.   A company observes performance issues due to improper memory allocation.
The DBA decides to modify database initialization parameters. Explain how [10]
initialization parameters are configured and modified in Oracle.
a.   In an organization, a user was mistakenly granted full access to critical database
tables, resulting in potential security risks and violation of access control
[10]
policies. Evaluate how a DBA should analyse and correct this situation by
Q3
appropriately granting and revoking privileges in an Oracle database system.
CO-2;
b.   A company uses both traditional client/server applications and web-based
BL-3
applications to access its Oracle database. Analyse the differences between
[10]
these connection architectures. Examine how Oracle Net supports both models
and how each impacts performance and scalability.
Q4   a.   An enterprise HR application built on Oracle experiences slow query
CO-1.   performance during peak hours. Investigation reveals frequent hard parsing and [10]
CO2 ;   high CPU usage, even though the queries are repetitive.
********** 1 **********
--- page 2 ---
BL-4   Analyse the possible causes of this issue by examining the role of the Shared
Pool and Library Cache. Suggest how improper memory usage can lead to this
performance problem.
b.   Analyze the differences between legal and   illegal multiplexed log
configurations in Oracle. Examine how the placement and structure of redo log [10]
members affect database reliability, fault tolerance, and recovery.
a.   Scenario
The finance department uses a FIN_TRANSACTIONS table. Incorrect
privilege assignment previously caused accidental deletions.
Roles Required
• FIN_READ_ROLE
• FIN_UPDATE_ROLE
Requirements
1. Junior accountants:
o Can only SELECT records
[10]
2. Senior accountants:
o Can UPDATE but cannot DELETE
3. Finance head:
Q5
o   Full access
CO-2,3;
Student Tasks
BL-5
•   Create roles with granular privileges
•   Assign roles to users
•   Demonstrate why DELETE privilege should not be granted broadly
• Revoke DELETE from a role and observe impact
b.   A medium-sized company is planning to migrate its existing on-premises
database to the cloud to take advantage of scalability and cost savings. The
company's data is critical for its daily operations.
Question:
• What considerations would you take into account when planning and [10]
executing the migration of the database to the cloud? How would you
ensure data consistency and minimize downtime during the migration
process?
•   Define backup and recovery policy for above organization.
Evaluate a scenario where frequent redo log switches are degrading database
Q6   a.   performance. Critically assess different redo log configuration strategies (such
[10]
CO-2,   as log file size, number of groups, and switching frequency), and justify the
CO3 ;   most effective approach to optimize performance and maintain system stability.
BL-5,3   b.
Differentiate Proactive Monitoring and Bottleneck Elimination with example.   [10]
a.   Apply your understanding to classify the different types of failures (such as soft
failure, hard failure, and network failure) that may occur in a database system.
Demonstrate how Oracle handles each type of failure using appropriate [10]
Q7
recovery mechanisms, including the role of redo logs, undo data, and backups
CO-3;
in restoring the database to a consistent state.
BL-4
b.   Evaluate the process of manually creating control files in Oracle Database.
Under what circumstances would a DBA need to recreate control files, and   [10]
what precautions should be taken?
********** 2 **********
````

## 2025-26 · Final-Exam · Sem 10 · paper b603e8efad45

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Database Administration/QP_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Database Administration
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1;   a.   Explain the concept of 3-tier architecture in database systems. Describe the role
BL-2   of each tier in processing user requests.
CO-2;   b.   A developer needs to create tables but should not perform backup operations.
BL-2   How would you apply the principle of least privilege while creating this user?
CO-2;   c.   Describe the role of control files in an Oracle database. Describe the type of
BL-3   information stored in control files and its importance in database startup.
CO-2;   d.   Explain the concept of shared server architecture in Oracle. Describe how it
BL-2   improves scalability and resource utilization in a multi-user environment.
a.   A company is deploying an Oracle Database system for a multi-user enterprise
application. As a database administrator, you are required to illustrate and
explain the Oracle Database Architecture. demonstrate how the database [10]
Q2
instance (memory structures and background processes) interacts with the
CO-1;
physical database components (data files, control files, and redo log files)
BL-3
b.   A company observes performance issues due to improper memory allocation.
The DBA decides to modify database initialization parameters. Explain how [10]
initialization parameters are configured and modified in Oracle.
a.   In an organization, a user was mistakenly granted full access to critical database
tables, resulting in potential security risks and violation of access control
[10]
policies. Evaluate how a DBA should analyse and correct this situation by
Q3
appropriately granting and revoking privileges in an Oracle database system.
CO-2;
b.   A company uses both traditional client/server applications and web-based
BL-3
applications to access its Oracle database. Analyse the differences between
[10]
these connection architectures. Examine how Oracle Net supports both models
and how each impacts performance and scalability.
Q4   a.   An enterprise HR application built on Oracle experiences slow query
CO-1.   performance during peak hours. Investigation reveals frequent hard parsing and [10]
CO2 ;   high CPU usage, even though the queries are repetitive.
********** 1 **********
--- page 2 ---
BL-4   Analyse the possible causes of this issue by examining the role of the Shared
Pool and Library Cache. Suggest how improper memory usage can lead to this
performance problem.
b.   Analyze the differences between legal and   illegal multiplexed log
configurations in Oracle. Examine how the placement and structure of redo log [10]
members affect database reliability, fault tolerance, and recovery.
a.   Scenario
The finance department uses a FIN_TRANSACTIONS table. Incorrect
privilege assignment previously caused accidental deletions.
Roles Required
• FIN_READ_ROLE
• FIN_UPDATE_ROLE
Requirements
1. Junior accountants:
o Can only SELECT records
[10]
2. Senior accountants:
o Can UPDATE but cannot DELETE
3. Finance head:
Q5
o   Full access
CO-2,3;
Student Tasks
BL-5
•   Create roles with granular privileges
•   Assign roles to users
•   Demonstrate why DELETE privilege should not be granted broadly
• Revoke DELETE from a role and observe impact
b.   A medium-sized company is planning to migrate its existing on-premises
database to the cloud to take advantage of scalability and cost savings. The
company's data is critical for its daily operations.
Question:
• What considerations would you take into account when planning and [10]
executing the migration of the database to the cloud? How would you
ensure data consistency and minimize downtime during the migration
process?
•   Define backup and recovery policy for above organization.
Evaluate a scenario where frequent redo log switches are degrading database
Q6   a.   performance. Critically assess different redo log configuration strategies (such
[10]
CO-2,   as log file size, number of groups, and switching frequency), and justify the
CO3 ;   most effective approach to optimize performance and maintain system stability.
BL-5,3   b.
Differentiate Proactive Monitoring and Bottleneck Elimination with example.   [10]
a.   Apply your understanding to classify the different types of failures (such as soft
failure, hard failure, and network failure) that may occur in a database system.
Demonstrate how Oracle handles each type of failure using appropriate [10]
Q7
recovery mechanisms, including the role of redo logs, undo data, and backups
CO-3;
in restoring the database to a consistent state.
BL-4
b.   Evaluate the process of manually creating control files in Oracle Database.
Under what circumstances would a DBA need to recreate control files, and   [10]
what precautions should be taken?
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 14fd581ead52

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_IT_7041/Database Administration/QP_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Database Administration
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1;   a.   Define the concept of database administration. Discuss the roles and
BL-2   responsibilities of a DBA in an organization.
b.   A DBA wants to check which roles are assigned to a particular user for
CO-2;
auditing purposes. Explain how to query role information in Oracle using data
BL-2
dictionary views
CO-2;   c.   Describe the process of managing database files in Oracle. Describe how data
BL-3   files are created and maintained within a database system.
d.   Explain the role of Oracle Net Services in database connectivity. Describe
CO-2;
how it facilitates communication between client applications and the Oracle
BL-2
database server.
a.   Apply appropriate considerations to explain how factors such as hardware
requirements, operating system   compatibility, storage planning, and [10]
Q2   configuration settings influence a successful installation.
CO-1;   b.   After the system restarts, the database is not fully available to users. The DBA
BL-3   needs to bring the database online step-by-step. Explain the stages of database
[10]
startup (Nomount, Mount, Open) and describe what operations are performed
at each stage.
a.   A large organization consists of multiple departments such as HR, Finance, and
Sales, each requiring different levels of access to the Oracle database.
Analyze how a DBA can design and implement role-based access control to
[10]
manage user groups efficiently. Explain how roles can be created, assigned, and
Q3
managed for different departments for improved security, scalability and ease
CO-2;
of administration.
BL-3
b.   Compare shared server architecture and dedicated server architecture. A
database server is experiencing high load due to a large number of simultaneous
[10]
user connections. Analyze and justify which server architecture can be used to
handle this situation.
a.
Analyze the two fundamental memory structures associated with a database
Q4   [10]
instance. Examine how each structure contributes to system performance,
********** 1 **********
--- page 2 ---
CO-1.   resource utilization, and overall database functionality, with appropriate
CO2 ;   examples.
BL-4
b.   How would a DBA create a new control file in case of control file loss or
[10]
corruption? Illustrate with an example.
a.   Provide step-by-step SQL commands to execute the following scenario:
• User Raj creates two users: Meera and Karan.
• User Raj grants object privileges to Meera with the GRANT OPTION
(including permissions such as creating tables, selecting data, and
granting privileges to other users).   [10]
Q5   • User Meera further grants the SELECT privilege to user Karan.
CO-2,3;   •   Later, if user Raj revokes the granted privileges from Meera, the
BL-5, 2   privileges should also be automatically revoked from Karan.
•   Finally, user Raj drops the user Karan.
b.   Organization requires continuous database availability and cannot shut down
the system for backups. Apply your knowledge to demonstrate how to perform
[10]
online (inconsistent) backups in ARCHIVELOG mode. Explain the role of redo
logs and archived logs in ensuring data consistency during recovery.
One member of a redo log group becomes corrupted, but the database is still
a.   running.
•   Write SQL commands to drop the corrupted redo log member.
[10]
Q6   • Add a new member to the same group.
CO-2,   Explain why the database continues functioning and how multiplexing helps
CO3 ;   maintain availability.
BL-5,3   b.   What are the key responsibilities and advantages of employing a virtual DBA
(Database Administrator) for managing and maintaining database systems
[10]
remotely, and how does this approach compare to traditional in-house DBA
services.
a.   After a system crash, the database undergoes instance recovery during startup.
Apply your knowledge to explain the phases of instance recovery and [10]
Q7
demonstrate how checkpoints influence recovery time and performance.
CO-3;
b.   A database experiences loss of a datafile due to disk failure. Apply your
BL-4
understanding of media recovery to demonstrate the steps required to restore   [10]
and recover the damaged datafile using archived redo logs.
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 10 · paper 8e32ef54e607

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Re-Exam/Integrated_IT_7037/Database Administration/QP_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Database Administration
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1;   a.   Define the concept of database administration. Discuss the roles and
BL-2   responsibilities of a DBA in an organization.
b.   A DBA wants to check which roles are assigned to a particular user for
CO-2;
auditing purposes. Explain how to query role information in Oracle using data
BL-2
dictionary views
CO-2;   c.   Describe the process of managing database files in Oracle. Describe how data
BL-3   files are created and maintained within a database system.
d.   Explain the role of Oracle Net Services in database connectivity. Describe
CO-2;
how it facilitates communication between client applications and the Oracle
BL-2
database server.
a.   Apply appropriate considerations to explain how factors such as hardware
requirements, operating system   compatibility, storage planning, and [10]
Q2   configuration settings influence a successful installation.
CO-1;   b.   After the system restarts, the database is not fully available to users. The DBA
BL-3   needs to bring the database online step-by-step. Explain the stages of database
[10]
startup (Nomount, Mount, Open) and describe what operations are performed
at each stage.
a.   A large organization consists of multiple departments such as HR, Finance, and
Sales, each requiring different levels of access to the Oracle database.
Analyze how a DBA can design and implement role-based access control to
[10]
manage user groups efficiently. Explain how roles can be created, assigned, and
Q3
managed for different departments for improved security, scalability and ease
CO-2;
of administration.
BL-3
b.   Compare shared server architecture and dedicated server architecture. A
database server is experiencing high load due to a large number of simultaneous
[10]
user connections. Analyze and justify which server architecture can be used to
handle this situation.
a.
Analyze the two fundamental memory structures associated with a database
Q4   [10]
instance. Examine how each structure contributes to system performance,
********** 1 **********
--- page 2 ---
CO-1.   resource utilization, and overall database functionality, with appropriate
CO2 ;   examples.
BL-4
b.   How would a DBA create a new control file in case of control file loss or
[10]
corruption? Illustrate with an example.
a.   Provide step-by-step SQL commands to execute the following scenario:
• User Raj creates two users: Meera and Karan.
• User Raj grants object privileges to Meera with the GRANT OPTION
(including permissions such as creating tables, selecting data, and
granting privileges to other users).   [10]
Q5   • User Meera further grants the SELECT privilege to user Karan.
CO-2,3;   •   Later, if user Raj revokes the granted privileges from Meera, the
BL-5, 2   privileges should also be automatically revoked from Karan.
•   Finally, user Raj drops the user Karan.
b.   Organization requires continuous database availability and cannot shut down
the system for backups. Apply your knowledge to demonstrate how to perform
[10]
online (inconsistent) backups in ARCHIVELOG mode. Explain the role of redo
logs and archived logs in ensuring data consistency during recovery.
One member of a redo log group becomes corrupted, but the database is still
a.   running.
•   Write SQL commands to drop the corrupted redo log member.
[10]
Q6   • Add a new member to the same group.
CO-2,   Explain why the database continues functioning and how multiplexing helps
CO3 ;   maintain availability.
BL-5,3   b.   What are the key responsibilities and advantages of employing a virtual DBA
(Database Administrator) for managing and maintaining database systems
[10]
remotely, and how does this approach compare to traditional in-house DBA
services.
a.   After a system crash, the database undergoes instance recovery during startup.
Apply your knowledge to explain the phases of instance recovery and [10]
Q7
demonstrate how checkpoints influence recovery time and performance.
CO-3;
b.   A database experiences loss of a datafile due to disk failure. Apply your
BL-4
understanding of media recovery to demonstrate the steps required to restore   [10]
and recover the damaged datafile using archived redo logs.
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 2821a460b11c

- Departments: Information Technology
- Programmes: B TECH / I T, B.TECH INTEGRATED / IT, MBA TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/I T/VI SEMESTER/DATABASE ADMINISTRATION/Database Administration Batch 2025-26 Re Exam.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: ocr (2 pages), mean OCR confidence 90.4

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech Intg. (IT)/B. Tech WA B
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exanf{Bxa

Subject: Database Administration (SS) -pgTM®
Date: 04 Jul 2026 ime: 10500 apn 801 00 (03:00 Hrs.)
Max. Marks: 100 oe -

RE EXAMINATION (Acad. Yea

StS

Instructions:
1. This question paper contains 2 pages.
2. Question No. | is compulsory
3. Out of the remaining questions, attempt any 4 questions
4, Inall 5 questions to be attempted

5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.

7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.

| [20]
S an

Answer briefly: .

v

Define the concept of database administration. Discuss the role

responsibilities of a DBA in an organization.

CO-1; la.
BL-2 |

b. A DBA wants to check which roles are assigned to a particular user for
rmation in Oracle using data

oo auditing purposes. Explain how to query role info
dictionary views
c. Describe the process of managing database fi
| files are created and maintained within a database system.
database connectivity. Describe

client applications and the Oracle

les in Oracle. Describe how data

d. Explain the role of Oracle Net Services in
how it facilitates communication between

database server.
Apply appropriate considerations to explain how factors such as hardware

requirements, operating system compatibility, storage planning, and
configuration settings influence a successful installation.

[10]

abase is not fully available to users. The DBA
Explain the stages of database

. [10]
hat operations are performed

b. After the system restarts, the dat:
needs to bring the database online step-by-step.
startup (Nomount, Mount, Open) and describe w

at each stage.

A large organization consists of multiple departments such as HR, Finance, and
Sales, each requiring different levels of access to the Oracle database.

Analyze how a DBA can design and implement role-based access control to [10]
manage user groups efficiently. Explain how roles can be created, assigned, and
* | managed for different departments for improved security, scalability and ease

of administration.

b. Compare shared server architecture and dedicated server architecture. A
database server is experiencing high,load due to a large number of simultaneous [10]
user connections. Analyze and justify which server architecture can be used to

handle this situation.

ructures associated with a database [10]

FA
a Analyze the two fundamental memory st
ntributes to system performance,

Q4 ‘ .
instance. Examine how each structure co

FORK 7] FRR R EE

ms
--- page 2 ---
COo-1. resource utilization, and overall database functionality, with appropriate
CO2.; examples.
BL-4

b. How would a DBA create a new control file in case of control file loss or, [10]
corruption? Illustrate with an example. .

a. Provide step-by-step SQL commands to execute the following scenario:
e User Raj creates two users: Meera and Karan.
¢ User Raj grants object privileges to Meera with the GRANT OPTION
(including permissions such as creating tables, selecting data, and

granting privileges to other users). [10]
Q5 e User Meera further grants the SELECT privilege to user Karan.
CO-2,3; e Later, if user Raj revokes the granted privileges from Meera, the
BL-S, 2 privileges should also be automatically revoked from Karan.

e Finally, user Raj drops the user Karan.

b. Organization requires continuous database availability and cannot shut down
the system for backups. Apply your knowledge to demonstrate how to perform
online (inconsistent) backups in ARCHIVELOG mode. Explain the role of redo
logs and archived logs in ensuring data consistency during recovery.

[10]

One member of a redo log group becomes corrupted, but the database is still

a. running. '
e Write SQL commands to drop the corrupted redo log member. [10]
Q6 e Add anew member to the same group. :
CO-2, Explain why the database continues functioning and how multiplexing helps
C03 ¢ maintain availability.
BL-S5,3 b. What are the key responsibilities and advantages of employing a virtual DBA
(Database Administrator) for managing and maintaining database systems [10]

remotely, and how does this approach compare to traditional in-house DBA °

services.
a. After a system crash, the database undergoes instance recovery during startup.
Q7 Apply your knowledge to explain the phases of instance recovery and | [10]
CO-3: demonstrate how checkpoints influence recovery time and performance.
BL-4 b. A database experiences loss of a datafile due to disk failure. Apply your
understanding of media recovery to demonstrate the steps required to restore [10]

and recover the damaged datafile using archived redo logs.

RRR RRR RR RK DOR RK

my
````

## 2024-25 · Final + Re-Exam · Sem 6 · paper 04c33f419ba8

- Departments: Information Technology
- Programmes: B TECH / I T, MBA TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/I T/VI SEMESTER/DATABASE ADMINISTRATION/Database Administration, Sem VI, Year 2024-25 Final Exam & 2023-24 & 2024-25 Re Exam.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 92.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B. Tech /MBA Tech Year: II Semester: VI

Stream/s: Information Technology

Subject: Database Administration Time: 3 hrs. (2e™to > p™ )
Date:_O 2/05/2025 No. of Pages:_O 3 _

Marks: 100

Finai Examination/Re-Examination023-24)
C 2024-25) :
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

rai
Answer briefly: [20]
CO-1; a, Explain the difference between logical and physical storage structures in an Oracle
BL-1 ; Database.
b. An unauthorized user has gained access to sensitive database objects due to
in excessive privilege grants. How would you identify and revoke unnecessary
privileges to enhance security?
c Analyze the importance of control files in Oracle Database. What would happen if
a control file becomes corrupted, and how can a DBA recover from such a
situation?
CO-2; d. How would you configure Oracle Net service to enable client-server application
BL-2 communication?
a. Differentiate SPFILE and PFILE. How would you apply your knowledge of [10]
Q SPFILE and PFILE to manage initialization parameters effectively?
co-l; b. How would you analyze and optimize the roles of DBWn, LGWR, and CKPT to
BL-2 improve database performance? [10]
Q3 a. Explain shared server architecture. How connection pooling and session [10]
CO-2; multiplexing differs from each other. .
--- page 2 ---
BL-4 b. Analyze the differences between system privileges and object privileges in Oracle
Database security. How would improper assignment of these privileges impact [10]

database security?

= List and explain different database startup modes. Explain in detail specific tasks | [19]
Q4 performed in those startup modes.
CO-l. » |b, Redo log files play a crucial role in maintaining database integrity. How would
oa 2 you analyze the impact of a failed redo log file on database transactions, and what | [10]
steps would you take to resolve the issue?
a. Scenario:
e Mike creates two users: David and Eva.
¢ Mike creates a role called DataAnalyst and grants it the CREATE
TABLE and SELECT ANY TABLE privileges.
¢ Mike assigns the DataAnalyst role to David with the ADMIN OPTION,
Q5 allowing David to grant the role to others. [10]
CO-2; e David grants the DataAnalyst role to Eva.
Bl, ¢ Mike revokes the DataAnalyst role from David, which should
automatically revoke it from Eva.
¢ Mike drops user Eva from the database.
Task: Provide the step-by-step SQL commands to execute the above scenario.
b Explain the key differences between Remote DBA and Virtual DBA. [10]
Assess the advantages and disadvantages of multiplexing control files. Ina high- ©
a. availability environment, what strategies would you recommend for ensuring {10]
control file redundancy and reliability?
Q6 b. A financial institution experiences a system crash during peak business hours,
CO-2, causing database failure. As a DBA, you need to ensure minimal data loss and
CO3 ;

quick recovery.
e Evaluate the best recovery strategy (consistent vs. inconsistent backup).
e Justify whether RMAN or user-managed backup would be more effective

in this scenario.

Q7 a. | List and explain various types of failures that occurs on database server. [10]
--- page 3 ---
CO-3; b. A manufacturing company using Oracle Database faces an issue where one of its
BL-l, 5 redo log groups is lost due to hardware failure. The DBA realizes that the
database is running in NOARCHIVELOG mode.
e Assess the impact of losing redo logs in NOARCHIVELOG mode and [10]
determine possible recovery solutions.
« Recommend the best approach for preventing future redo log failures,

including multiplexing strategies.
--- page 4 ---

````

## 2023-24 · Final-Exam · Sem 6 · paper fe5422155b52

- Departments: Information Technology
- Programmes: B TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/I T/VI SEMESTER/DATABASE ADMINISTRATION/Database Administration, Sem-VI, Year 2023-24, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 91.1

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024

Program: B. Tech /MBA Tech Year: III Semester: VI

Stream :(Information Technology )

Subject: Database Administration Time: 3 hrs. (2:00 pry_to 5:00pm
Date:_20_ /04 / 2024 No. of Pages: 2

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.

2) Out of the remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi te
Answer briefly:
20)
COo- ;1 a. What are the significant use cases and benefits of Background trace files in
BL-1 Oracle database management?
ics x Describe the Order of Precedence in startup command.
a ? c. Explain with example what is system privilege and user defined privilege.
Co- 1; d. , f : :
BL2 Differentiate legal and illegal multiplexed redo log configuration.
a. Provide solution for the following requirement:
e Multiplex control file using a SPFile.
e Create 3 copies of the original control file.
Q2 e Location for all 3 control files respectively:
CO- /oral/oradata/orcl/cnt 1 .ctl, /ora2/oradata/orcl/cnt2.ct2, [2*10
1,CO- /ora3/oradata/orcl/cnt3.ctl =20]
CO2; e Maxlogroup 3, Maxlogmembers 9
BL-4 e Location for all datafiles: c:/oracle/database
b. Draw neat diagram of web client application connection. What are the key
considerations and best practices for establishing secure and reliable
connections from a web client application to backend servers or databases?
Q3 a. Compare and contrast Consistent backup and inconsistent backup. How do | [2*10
CO-3; these backup types affect data integrity and recovery processes in various | __ 20
= 20]
BL-2,3 systems?
--- page 2 ---
5

|

Write short note on Incomplete Recovery and its various options.

Describe Functional organization of DBA. List and explain roles of DBA
associated with it

Provide Step by step commands to execute the given scenario:
e Mike creates user Jessica and Tom

Q4 e Suppose that user Mike grants object privilege to user Jessica with | [2*10
CO-1 a grant option (to create table, Select data, grant privilege to =20]
BL-2,4 another users)
e Jessica grants that privilege to user tom. (select data)
e [fuser Mike revokes that privilege from Jessica, it will be
automatically revoked from tom.
e Mike drops user Tom
Q5 Differentiate Proactive Monitoring and Bottleneck Elimination with [2*10
Co- example. ;
1,CO-3; Explain with suitable example which recovery option to use Import/Export | = 20]
BL-3 Utilities Recovery and Oracle Flashback
What role does a Database Administrator (DBA) play in defining and
implementing network security measures within an organization's database
infrastructure
A medium-sized company is planning to migrate its existing on-premises
Q6 database to the cloud to take advantage of scalability and cost savings. The [2*10
CO- company's data is critical for its daily operations.
2;CO3 Question: = 20]
BL-2,5 e What considerations would you take into account when planning and
executing the migration of the database to the cloud? How would
you ensure data consistency and minimize downtime during the
migration process?
e Define backup and recovery policy for above organization
Q7 What are the sequential steps involved in the Oracle Emergency A
CoO-F Performance Method, and how does this methodology assist database [2*10
CO3; administrators? = 20]
BL-2 Compare and contrast various shutdown options on database server.
````

## 2023-24 · Re-Exam · Sem 6 · paper 3275222e5650

- Departments: Information Technology
- Programmes: B TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/I T/VI SEMESTER/DATABASE ADMINISTRATION/Database Administration, Sem-VI, Year 2023-24, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 87.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2023-2024
Program: B. Tech /MBA Tech |

Stream :(Information Technology )

Year: III Semester: VI

Subject: Database Administration
Date:_22 / e€/ 2024
Marks: 100

Time: 3 hrs.(2e to Spa)
No. of Pages: 2 :

___Re= |Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

of the Answer Book, which is provided for their use. i
1) Question No. 1 is compulsory.
2) Out of the remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.

' 5) Answer each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql : [485 =

Answer briefly:

20]
Her a What is significant use of User trace file.
Co- 1; b. : ps Bee
BL2 List and explain different types of Database Privileges
aoe : a Describe various predefined user accounts used in oracle.
oe . How LGWR reuses the Redo Logfiles
a. Create multiple copies of online redo log files as per following
requirement: :

Create database as “testdata”.
e Create 2 redo log groups.

ce e Each group should contain 3 members. [2*10
L.CO- e Each Group’s member 1-should locate on
C 02: ‘/oral/oradata/testdata/logfilename.log’ = 20]
BL-4 e Each Group’s member 2 should locate on

‘/ora2/oradata/testdata/logfilename.log’

e Each Group’s member 3 should locate on
‘/ora3/oradata/testdata/logfilename.log’

e Size of group should.be 10M each.
--- page 2 ---
Explain shared server architecture. How connection pooling and session

multiplexing differs from each other.

List and explain various types of failures occurs on database server.

[2*10

Q3
CO-3; Write a short note on RMAN and User-Managed Restore and Recovery | _ 99
: : : i}
BL-2,3 option. : ;
What are the two fundamental memory structures associated with an
Instance in database management systems, and how do they contribute to
the overall performance and functionality of the system?
Provide Step by step commands to execute the given scenario:
o4 e Amit creates user Nidhi and Tejas : [2*10
C0-1 e Suppose that user Amit grants object privilege to user Nidhi with a
BL2.4 a ae (to create table, Select data, grant privilege to another | = 20] ~
‘ users
e Nidhi grants that privilege to user Tejas. (select data)
e If user Amit revokes that privilege from Nidhi, it will be
automatically revoked from tom. j :
e Amit drops user Tejas
What are the key responsibilities and advantages of employing a virtual
Q5 DBA (Database Administrator) for managing and maintaining database [2*10
Co- systems remotely, and how does this approach compare to traditional in-
1,CO-3; house DBA services : = 20]
BL-3 Explain with suitable example which recovery option to use Media
Recovery and Oracle Flashback
ae Describe Net Stack Architecture with proper diagram [2*10
2;CO3 Being a DBA define a strategy for backup recovery plan in the event ofa | = 20]
BL-2,5 hardware or software failure of a banking application
Q7 What are the sequential steps involved in the Oracle Performance
Co-1 Improvement Method, and how does this methodology assist database [2*10
C 03: administrators? =20]
; Compare pfile and spfile. Explain startup command behavior according to

these two files.

BL-2
stain
````
