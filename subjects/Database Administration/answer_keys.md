# Database Administration: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper b89dff175107

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Database Administration/ANS_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Database Administration
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the concept of 3-tier architecture in database systems. Describe the role
of each tier in processing user requests.
Ans:
The 3-tier architecture in database systems is a client-server model that
separates an application into three logical layers: Presentation Tier,
Application (Logic) Tier, and Database (Data) Tier. This separation
improves scalability, security, maintainability, and flexibility by distributing
responsibilities across different layers.
Roles of Each Tier in Processing User Requests:
Presentation layer:
• Accepts user request (e.g., login, query form)
CO-1;   • Sends request to the application tier
BL-2   •   Displays the processed output received
Application Tier (Business Logic Layer)
•   Receives request from presentation tier
•   Validates input and applies business logic
•   Converts request into database queries (SQL)
• Sends queries to the database tier
•   Processes results received and formats response
Database Tier (Data Layer)
•   Executes SQL queries sent by application tier
•   Retrieves or updates data
•   Ensures data integrity, security, and concurrency
• Sends results back to application tier
b.   A developer needs to create tables but should not perform backup operations.
CO-2;
How would you apply the principle of least privilege while creating this user?
BL-2
Ans:
********** 1 **********
--- page 2 ---
DBA should create a user account that has only the permissions required to
create and manage tables, and must not grant backup or administrative
privileges.
Only allow : create session, create table and limited storage quota
Why this follows least privilege
• CREATE SESSION allows the developer to log in.
• CREATE TABLE allows table creation only in their own schema.
• No backup-related privileges such as SYSDBA, SYSBACKUP, or other
administrative roles are granted.
• The user is restricted to only what is necessary for development work.
c.   Describe the role of control files in an Oracle database. Describe the type of
information stored in control files and its importance in database startup.
Ans: A control file is a critical binary file in an Oracle Database that
maintains essential information about the physical structure and state of the
database
Information Stored in Control Files:
• Database Identification Information
CO-2;   •   Datafile Information
BL-2   • Redo Log File Information
• Checkpoint Information
• Backup and Recovery Information
Importance During Database Startup:
•   Essential for Mount Stage
•   Locates Physical Files
•   Ensures Database Consistency
•   Supports Recovery Operations
d.   Explain the concept of shared server architecture in Oracle. Describe how it
improves scalability and resource utilization in a multi-user environment.
Ans:
The Shared Server Architecture allows multiple user sessions to share a pool of
server processes instead of each user having a dedicated server process. This
architecture is designed to efficiently handle large numbers of concurrent users.
Working:
•   Client Request Handling
CO-2;   • Queue Mechanism
BL-2   • Shared Server Processing
• Response Delivery
Improvement in Scalability
Supports More Users
• Many users share fewer server processes.
• Reduces system overhead compared to one process per user.
Efficient Handling of Idle Sessions
•   Ideal for environments where users are frequently
a.   A company is deploying an Oracle Database system for a multi-user enterprise
Q2   application. As a database administrator, you are required to illustrate and
CO-1;   explain the Oracle Database Architecture. demonstrate how the database [10]
BL-3   instance (memory structures and background processes) interacts with the
physical database components (data files, control files, and redo log files)
********** 2 **********
--- page 3 ---
Ans:
Oracle architecture consists of two main components:
• Database Instance → Memory structures + background processes
•   Physical Database → Datafiles, Control files, Redo log files
Database Instance Components
Memory Structures
SGA (System Global Area)
• Database Buffer Cache → stores data blocks
• Shared Pool → stores SQL and execution plans
• Redo Log Buffer → stores redo entries
PGA (Program Global Area)
• Private memory for each server process
• Used for sorting, session variables, etc.
Background Processes
1. DBWn (Database Writer)
o Writes modified data (dirty blocks) from buffer cache to
datafiles
2. LGWR (Log Writer)
o Writes redo entries from redo buffer to redo log files
3. CKPT (Checkpoint Process)
o Updates control files and datafile headers with
checkpoint info
4. SMON (System Monitor)
o Performs instance recovery after crashes
5. PMON (Process Monitor)
o Cleans up failed user processes
Physical Database Components
1. Data Files
o Store actual user data (tables, indexes)
2. Control Files
o Store metadata about database structure (file locations,
checkpoints)
3. Redo Log Files
o Store changes made to data for recovery purposes
Interaction Flow
User → SGA (Shared Pool + Buffer Cache + Redo Buffer)
→ Background Processes (DBWn, LGWR, CKPT)
→ Physical Files (Datafiles, Redo Logs, Control Files)
b.   A company observes performance issues due to improper memory allocation.
The DBA decides to modify database initialization parameters. Explain how
initialization parameters are configured and modified in Oracle.
[10]
Ans:
Initialization parameters define how an Oracle instance starts and operates,
especially memory allocation,
********** 3 **********
--- page 4 ---
•   Pfile
text file and
manually editable.
• SPFILE (Server Parameter File)
Binary file managed by Oracle
Preferred in production
Supports dynamic changes using SQL commands
For Dynamic Change (Immediate Effect):
ALTER SYSTEM SET shared_pool_size = 300M;
Persisting Changes:
ALTER SYSTEM SET db_cache_size = 600M SCOPE = SPFILE;
Apply to Both Memory and SPFILE:
ALTER SYSTEM SET pga_aggregate_target = 400M SCOPE = BOTH;
Using PFILE (Manual Editing)
1. Shutdown
2. Edit init.ora file
3. Restart database: STARTUP;
a.   In an organization, a user was mistakenly granted full access to critical database
tables, resulting in potential security risks and violation of access control
policies. Evaluate how a DBA should analyse and correct this situation by
appropriately granting and revoking privileges in an Oracle database system.
Ans:
Check system privileges:
SELECT * FROM DBA_SYS_PRIVS WHERE GRANTEE = 'USER_NAME
Check object privileges:
SELECT * FROM DBA_TAB_PRIVS WHERE GRANTEE =
'USER_NAME';
Check roles assigned:
SELECT * FROM DBA_ROLE_PRIVS WHERE GRANTEE =
'USER_NAME';
Detect risky privileges like SELECT ANY TABLE, DBA, WITH GRANT
Q3
OPTION
CO-2;   [10]
Corrective Actions Using REVOKE
BL-3
• REVOKE SELECT ANY TABLE FROM USER_NAME;
• REVOKE ALL ON employees FROM USER_NAME;
• REVOKE DBA FROM USER_NAME;
Reassigning Correct Privileges
GRANT SELECT ON employees TO USER_NAME;
Or
CREATE ROLE hr_read_only;
GRANT SELECT ON employees TO hr_read_only;
GRANT hr_read_only TO USER_NAME;
Preventive Measures
Implement Role-Based Access Control (RBAC)
Avoid granting powerful system privileges unnecessarily
********** 4 **********
--- page 5 ---
Restrict use of WITH GRANT OPTION
Enable auditing to track privilege usage:
b.   A company uses both traditional client/server applications and web-based
applications to access its Oracle database. Analyze the differences between
these connection architectures. Examine how Oracle Net supports both models
and how each impacts performance and scalability.
Ans:
Aspect   Client/Server (2-Tier)   Web-Based (3-Tier)
Through application
Connection   Direct DB connection
server
Shared / pooled
Server Process Dedicated per user
connections
Scalability   Limited   High
Resource
High   Optimized
Usage
Difficult (client
Maintenance   Easier (centralized)   [10]
updates)
Role of Oracle Net in Both Models:
In Client/Server Model
•   Direct communication using TNS (Transparent Network Substrate)
• Each client establishes its own session
• Uses listener to connect to dedicated server process
In Web-Based Model
•   Oracle Net connects application server to database
•   Supports:
o Connection pooling → reuse of sessions
o Shared Server architecture → multiple users share processes
• Reduces number of active database connections
a.   An enterprise HR application built on Oracle experiences slow query
performance during peak hours. Investigation reveals frequent hard parsing and
high CPU usage, even though the queries are repetitive.
Analyse the possible causes of this issue by examining the role of the Shared
Pool and Library Cache. Suggest how improper memory usage can lead to this
performance problem.
Ans:
Q4   Role of Shared Pool and Library Cache
CO-1.   Shared Pool
[10]
CO2 ;   •   Part of SGA that stores:
BL-4   o SQL statements
o Execution plans
o Data dictionary information
1. Library Cache
• Subcomponent of Shared Pool
•   Stores parsed SQL (cursor) and execution plans
•   Enables reuse of SQL statements to avoid re-parsing
2. Insufficient Shared Pool Size
********** 5 **********
--- page 6 ---
•   Limited memory causes frequent flushing of cached SQL
•   Execution plans are removed before reuse
• Leads to repeated hard parsing
3. Lack of SQL Reusability
4. Library Cache Contention
5. Improper Cursor Management
How Improper Memory Usage Leads to the Issue
•   Small or fragmented Shared Pool → SQL not retained
• High eviction rate → repeated parsing
•   Increased CPU cycles spent on parsing instead of execution
• Reduced throughput under heavy load
Solutions
• Optimize Shared Pool Memory
• Use Bind Variables
• Avoid Frequent Invalidations
• Monitor Library Cache
b.   Analyze the differences between legal and illegal multiplexed redo log
configurations in Oracle. Examine how the placement and structure of redo log
members affect database reliability, fault tolerance, and recovery.
Ans:
A multiplexed redo log configuration in Oracle improves fault tolerance by
maintaining multiple copies (members) of each redo log group. To analyze legal
vs illegal configurations, we evaluate how redo log members are distributed
across storage and how this impacts recovery and availability.
Legal Multiplexed Configuration
• Each redo log group contains multiple members stored on different
physical disks/locations.
• Example:
GROUP 1: /disk1/log1a.rdo, /disk2/log1b.rdo
[10]
GROUP 2: /disk1/log2a.rdo, /disk2/log2b.rdo
•   Ensures redundancy—if one disk fails, another member is still
accessible.
• LGWR writes simultaneously to all members, maintaining consistency.
Illegal Multiplexed Configuration
• Redo log members of the same group are placed on the same disk or
storage device.
• Example:
GROUP 1: /disk1/log1a.rdo, /disk1/log1b.rdo
•   Creates a single point of failure—disk crash results in loss of all
members in the group.
•   Defeats the purpose of multiplexing.
• Compromises data integrity and recovery capability.
********** 6 **********
--- page 7 ---
a.   Scenario
The finance department uses a FIN_TRANSACTIONS table. Incorrect
privilege assignment previously caused accidental deletions.
Roles Required
• FIN_READ_ROLE
• FIN_UPDATE_ROLE
Requirements
1. Junior accountants:
o Can only SELECT records
2. Senior accountants:
o Can UPDATE but cannot DELETE
3. Finance head:
o   Full access
Student Tasks
•   Create roles with granular privileges
•   Assign roles to users
Q5
•   Demonstrate why DELETE privilege should not be granted broadly
CO-2,3;   [10]
• Revoke DELETE from a role and observe impact
BL-5
Ans:
Create Role:
CREATE ROLE FIN_READ_ROLE;
CREATE ROLE FIN_UPDATE_ROLE;
Assign Privileges:
GRANT SELECT ON FIN_TRANSACTIONS TO FIN_READ_ROLE;
GRANT SELECT, UPDATE ON FIN_TRANSACTIONS TO
FIN_UPDATE_ROLE;
GRANT SELECT, INSERT, UPDATE, DELETE ON FIN_TRANSACTIONS
TO FIN_HEAD_ROLE;
Assigning Roles to Users
GRANT FIN_READ_ROLE TO JUNIOR_USER;
GRANT FIN_UPDATE_ROLE TO SENIOR_USER;
GRANT FIN_HEAD_ROLE TO FIN_HEAD_USER;
Revoke DELETE from Role
********** 7 **********
--- page 8 ---
REVOKE DELETE ON FIN_TRANSACTIONS FROM
FIN_UPDATE_ROLE;
b.   A medium-sized company is planning to migrate its existing on-premises
database to the cloud to take advantage of scalability and cost savings. The
company's data is critical for its daily operations.
Question:
• What considerations would you take into account when planning and
executing the migration of the database to the cloud? How would you
ensure data consistency and minimize downtime during the migration
process?
•   Define backup and recovery policy for above organization.   [10]
Answer:
• Understand the backup environment.
• Perform capacity planning.
• Analyze current policies and procedures.
• Determine resource constraints.
•   Create a Backup Recovery Management Plan
• Implement the plan.
• Monitor the management plan.
Evaluate a scenario where frequent redo log switches are degrading database
a.   performance. Critically assess different redo log configuration strategies (such
as log file size, number of groups, and switching frequency), and justify the
most effective approach to optimize performance and maintain system
stability.
Ans:
Frequent redo log switches indicate that redo logs are too small or
insufficient in number, causing Oracle’s LGWR to switch logs rapidly. This
leads to increased checkpoint activity, I/O overhead, and potential
performance degradation.
[10]
• Each log switch triggers a checkpoint (CKPT + DBWn activity).
•   Excessive switches → frequent disk writes → CPU and I/O
Q6   overhead.
CO-2,   • Can cause “log file switch (checkpoint incomplete)” waits, slowing
CO3 ;   transactions.
BL-5,3   •   Impacts overall throughput and response time.
Approaches:
•   Increase Redo Log File Size
•   Increasing Number of Redo Log Groups
• Optimize Checkpoint Behavior
•   Place Logs on High-Speed Storage
b.   Differentiate Proactive Monitoring and Bottleneck Elimination with example.
Ans:
Proactive Monitoring
•   Proactive monitoring usually occurs on a regularly scheduled interval, [10]
where several performance statistics are examined to identify whether
the system behavior and resource usage has changed. Proactive
monitoring can also be considered as proactive tuning.
********** 8 **********
--- page 9 ---
•   Usually, monitoring does not result in configuration changes to the
system, unless the monitoring exposes a serious problem that is
developing. In some situations, experienced performance engineers can
identify potential problems through   statistics alone, although
accompanying performance degradation is usual.
• Experimenting with or tweaking a system when there is no apparent
performance degradation as a proactive action can be a dangerous
activity, resulting in unnecessary performance drops. Tweaking a
system should be considered reactive tuning, and the steps for reactive
tuning should be followed.
• Monitoring is usually part of a larger capacity planning exercise, where
resource consumption is examined to see changes in the way the
application is being used, and the way the application is using the
database and host resources.
Bottleneck Elimination
• Tuning usually implies fixing a performance problem. However, tuning
should be part of the life cycle of an application—through the analysis,
design, coding, production, and maintenance stages. Often, the tuning
phase is left until the database is in production. At this time, tuning
becomes a reactive process, where the most important bottleneck is
identified and fixed.
•   Usually, the purpose for tuning is to reduce resource consumption or to
reduce the elapsed time for an operation to complete. Either way, the
goal is to improve the effective use of a particular resource. In general,
performance problems are caused by the overuse of a particular
resource. The overused resource is the bottleneck in the system. There
are several distinct phases in identifying the bottleneck and the potential
fixes. These are discussed in the sections that follow.
Remember that the different forms of contention are symptoms that can be fixed
by making changes in the following places:
• Changes in the application, or the way the application is used
• Changes in Oracle
• Changes in the host hardware configuration.
a.   Apply your understanding to classify the different types of failures (such as soft
failure, hard failure, and network failure) that may occur in a database system.
Demonstrate how Oracle handles each type of failure using appropriate
recovery mechanisms, including the role of redo logs, undo data, and backups
in restoring the database to a consistent state.
Ans:
Q7
Classification of Failures:
CO-3;   [10]
Soft Failure (Instance Failure)
BL-4
•   Cause: Power failure, OS crash
•   Impact:
o Loss of SGA (memory)
o No damage to datafiles
Hard Failure (Media Failure)
•   Cause: Disk crash, file corruption
********** 9 **********
--- page 10 ---
•   Impact:
o Loss of datafiles, control files, or redo logs
o Permanent data loss unless backup exists
Network Failure
•   Cause: Communication breakdown between client and database
•   Impact:
o Session termination
o Database remains intact
Oracle Recovery Mechanisms:
Recovery for Soft Failure (Instance Recovery)
•   Automatically triggered during next startup by applying redo logs
Recovery for Hard Failure (Media Recovery)
•   Requires DBA intervention
Shutdown
Startup mount
RESTORE DATAFILE '/path/file.dbf';
RECOVER DATAFILE '/path/file.dbf';
ALTER DATABASE OPEN;
b.   Evaluate the process of manually creating control files in Oracle Database.
Under what circumstances would a DBA need to recreate control files, and
what precautions should be taken?
Ans:
Manual creation of control files in Oracle is a critical administrative
operation used when existing control files are lost, corrupted, or inconsistent.
Since control files maintain the physical structure of the database (datafiles,
redo logs, checkpoints), recreating them requires careful evaluation and
precision.
Performed in NOMOUNT mode, as control files are not yet available.
Requires accurate specification of:
•   Database name
•   Datafiles
• Redo log groups and members
[10]
• Followed by: RECOVER DATABASE , ALTER DATABASE OPEN
•   If redo information is incomplete → RESETLOGS option is required.
When Does a DBA Need to Recreate Control Files?
• Loss or Corruption of All Control Files
•   Inconsistent Control Files
•   Structural Changes
•   Database Renaming or Cloning
Precautions:
•   Maintain Control File Backups
•   Multiplex Control Files
•   Verify File Paths and Metadata
• Choose RESETLOGS vs NORESETLOGS Carefully
• Take Full Backup After Recreation
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper e4fcdda66fb1

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Database Administration/ANS_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Database Administration
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the concept of 3-tier architecture in database systems. Describe the role
of each tier in processing user requests.
Ans:
The 3-tier architecture in database systems is a client-server model that
separates an application into three logical layers: Presentation Tier,
Application (Logic) Tier, and Database (Data) Tier. This separation
improves scalability, security, maintainability, and flexibility by distributing
responsibilities across different layers.
Roles of Each Tier in Processing User Requests:
Presentation layer:
• Accepts user request (e.g., login, query form)
CO-1;   • Sends request to the application tier
BL-2   •   Displays the processed output received
Application Tier (Business Logic Layer)
•   Receives request from presentation tier
•   Validates input and applies business logic
•   Converts request into database queries (SQL)
• Sends queries to the database tier
•   Processes results received and formats response
Database Tier (Data Layer)
•   Executes SQL queries sent by application tier
•   Retrieves or updates data
•   Ensures data integrity, security, and concurrency
• Sends results back to application tier
b.   A developer needs to create tables but should not perform backup operations.
CO-2;
How would you apply the principle of least privilege while creating this user?
BL-2
Ans:
********** 1 **********
--- page 2 ---
DBA should create a user account that has only the permissions required to
create and manage tables, and must not grant backup or administrative
privileges.
Only allow : create session, create table and limited storage quota
Why this follows least privilege
• CREATE SESSION allows the developer to log in.
• CREATE TABLE allows table creation only in their own schema.
• No backup-related privileges such as SYSDBA, SYSBACKUP, or other
administrative roles are granted.
• The user is restricted to only what is necessary for development work.
c.   Describe the role of control files in an Oracle database. Describe the type of
information stored in control files and its importance in database startup.
Ans: A control file is a critical binary file in an Oracle Database that
maintains essential information about the physical structure and state of the
database
Information Stored in Control Files:
• Database Identification Information
CO-2;   •   Datafile Information
BL-2   • Redo Log File Information
• Checkpoint Information
• Backup and Recovery Information
Importance During Database Startup:
•   Essential for Mount Stage
•   Locates Physical Files
•   Ensures Database Consistency
•   Supports Recovery Operations
d.   Explain the concept of shared server architecture in Oracle. Describe how it
improves scalability and resource utilization in a multi-user environment.
Ans:
The Shared Server Architecture allows multiple user sessions to share a pool of
server processes instead of each user having a dedicated server process. This
architecture is designed to efficiently handle large numbers of concurrent users.
Working:
•   Client Request Handling
CO-2;   • Queue Mechanism
BL-2   • Shared Server Processing
• Response Delivery
Improvement in Scalability
Supports More Users
• Many users share fewer server processes.
• Reduces system overhead compared to one process per user.
Efficient Handling of Idle Sessions
•   Ideal for environments where users are frequently
a.   A company is deploying an Oracle Database system for a multi-user enterprise
Q2   application. As a database administrator, you are required to illustrate and
CO-1;   explain the Oracle Database Architecture. demonstrate how the database [10]
BL-3   instance (memory structures and background processes) interacts with the
physical database components (data files, control files, and redo log files)
********** 2 **********
--- page 3 ---
Ans:
Oracle architecture consists of two main components:
• Database Instance → Memory structures + background processes
•   Physical Database → Datafiles, Control files, Redo log files
Database Instance Components
Memory Structures
SGA (System Global Area)
• Database Buffer Cache → stores data blocks
• Shared Pool → stores SQL and execution plans
• Redo Log Buffer → stores redo entries
PGA (Program Global Area)
• Private memory for each server process
• Used for sorting, session variables, etc.
Background Processes
1. DBWn (Database Writer)
o Writes modified data (dirty blocks) from buffer cache to
datafiles
2. LGWR (Log Writer)
o Writes redo entries from redo buffer to redo log files
3. CKPT (Checkpoint Process)
o Updates control files and datafile headers with
checkpoint info
4. SMON (System Monitor)
o Performs instance recovery after crashes
5. PMON (Process Monitor)
o Cleans up failed user processes
Physical Database Components
1. Data Files
o Store actual user data (tables, indexes)
2. Control Files
o Store metadata about database structure (file locations,
checkpoints)
3. Redo Log Files
o Store changes made to data for recovery purposes
Interaction Flow
User → SGA (Shared Pool + Buffer Cache + Redo Buffer)
→ Background Processes (DBWn, LGWR, CKPT)
→ Physical Files (Datafiles, Redo Logs, Control Files)
b.   A company observes performance issues due to improper memory allocation.
The DBA decides to modify database initialization parameters. Explain how
initialization parameters are configured and modified in Oracle.
[10]
Ans:
Initialization parameters define how an Oracle instance starts and operates,
especially memory allocation,
********** 3 **********
--- page 4 ---
•   Pfile
text file and
manually editable.
• SPFILE (Server Parameter File)
Binary file managed by Oracle
Preferred in production
Supports dynamic changes using SQL commands
For Dynamic Change (Immediate Effect):
ALTER SYSTEM SET shared_pool_size = 300M;
Persisting Changes:
ALTER SYSTEM SET db_cache_size = 600M SCOPE = SPFILE;
Apply to Both Memory and SPFILE:
ALTER SYSTEM SET pga_aggregate_target = 400M SCOPE = BOTH;
Using PFILE (Manual Editing)
1. Shutdown
2. Edit init.ora file
3. Restart database: STARTUP;
a.   In an organization, a user was mistakenly granted full access to critical database
tables, resulting in potential security risks and violation of access control
policies. Evaluate how a DBA should analyse and correct this situation by
appropriately granting and revoking privileges in an Oracle database system.
Ans:
Check system privileges:
SELECT * FROM DBA_SYS_PRIVS WHERE GRANTEE = 'USER_NAME
Check object privileges:
SELECT * FROM DBA_TAB_PRIVS WHERE GRANTEE =
'USER_NAME';
Check roles assigned:
SELECT * FROM DBA_ROLE_PRIVS WHERE GRANTEE =
'USER_NAME';
Detect risky privileges like SELECT ANY TABLE, DBA, WITH GRANT
Q3
OPTION
CO-2;   [10]
Corrective Actions Using REVOKE
BL-3
• REVOKE SELECT ANY TABLE FROM USER_NAME;
• REVOKE ALL ON employees FROM USER_NAME;
• REVOKE DBA FROM USER_NAME;
Reassigning Correct Privileges
GRANT SELECT ON employees TO USER_NAME;
Or
CREATE ROLE hr_read_only;
GRANT SELECT ON employees TO hr_read_only;
GRANT hr_read_only TO USER_NAME;
Preventive Measures
Implement Role-Based Access Control (RBAC)
Avoid granting powerful system privileges unnecessarily
********** 4 **********
--- page 5 ---
Restrict use of WITH GRANT OPTION
Enable auditing to track privilege usage:
b.   A company uses both traditional client/server applications and web-based
applications to access its Oracle database. Analyze the differences between
these connection architectures. Examine how Oracle Net supports both models
and how each impacts performance and scalability.
Ans:
Aspect   Client/Server (2-Tier)   Web-Based (3-Tier)
Through application
Connection   Direct DB connection
server
Shared / pooled
Server Process Dedicated per user
connections
Scalability   Limited   High
Resource
High   Optimized
Usage
Difficult (client
Maintenance   Easier (centralized)   [10]
updates)
Role of Oracle Net in Both Models:
In Client/Server Model
•   Direct communication using TNS (Transparent Network Substrate)
• Each client establishes its own session
• Uses listener to connect to dedicated server process
In Web-Based Model
•   Oracle Net connects application server to database
•   Supports:
o Connection pooling → reuse of sessions
o Shared Server architecture → multiple users share processes
• Reduces number of active database connections
a.   An enterprise HR application built on Oracle experiences slow query
performance during peak hours. Investigation reveals frequent hard parsing and
high CPU usage, even though the queries are repetitive.
Analyse the possible causes of this issue by examining the role of the Shared
Pool and Library Cache. Suggest how improper memory usage can lead to this
performance problem.
Ans:
Q4   Role of Shared Pool and Library Cache
CO-1.   Shared Pool
[10]
CO2 ;   •   Part of SGA that stores:
BL-4   o SQL statements
o Execution plans
o Data dictionary information
1. Library Cache
• Subcomponent of Shared Pool
•   Stores parsed SQL (cursor) and execution plans
•   Enables reuse of SQL statements to avoid re-parsing
2. Insufficient Shared Pool Size
********** 5 **********
--- page 6 ---
•   Limited memory causes frequent flushing of cached SQL
•   Execution plans are removed before reuse
• Leads to repeated hard parsing
3. Lack of SQL Reusability
4. Library Cache Contention
5. Improper Cursor Management
How Improper Memory Usage Leads to the Issue
•   Small or fragmented Shared Pool → SQL not retained
• High eviction rate → repeated parsing
•   Increased CPU cycles spent on parsing instead of execution
• Reduced throughput under heavy load
Solutions
• Optimize Shared Pool Memory
• Use Bind Variables
• Avoid Frequent Invalidations
• Monitor Library Cache
b.   Analyze the differences between legal and illegal multiplexed redo log
configurations in Oracle. Examine how the placement and structure of redo log
members affect database reliability, fault tolerance, and recovery.
Ans:
A multiplexed redo log configuration in Oracle improves fault tolerance by
maintaining multiple copies (members) of each redo log group. To analyze legal
vs illegal configurations, we evaluate how redo log members are distributed
across storage and how this impacts recovery and availability.
Legal Multiplexed Configuration
• Each redo log group contains multiple members stored on different
physical disks/locations.
• Example:
GROUP 1: /disk1/log1a.rdo, /disk2/log1b.rdo
[10]
GROUP 2: /disk1/log2a.rdo, /disk2/log2b.rdo
•   Ensures redundancy—if one disk fails, another member is still
accessible.
• LGWR writes simultaneously to all members, maintaining consistency.
Illegal Multiplexed Configuration
• Redo log members of the same group are placed on the same disk or
storage device.
• Example:
GROUP 1: /disk1/log1a.rdo, /disk1/log1b.rdo
•   Creates a single point of failure—disk crash results in loss of all
members in the group.
•   Defeats the purpose of multiplexing.
• Compromises data integrity and recovery capability.
********** 6 **********
--- page 7 ---
a.   Scenario
The finance department uses a FIN_TRANSACTIONS table. Incorrect
privilege assignment previously caused accidental deletions.
Roles Required
• FIN_READ_ROLE
• FIN_UPDATE_ROLE
Requirements
1. Junior accountants:
o Can only SELECT records
2. Senior accountants:
o Can UPDATE but cannot DELETE
3. Finance head:
o   Full access
Student Tasks
•   Create roles with granular privileges
•   Assign roles to users
Q5
•   Demonstrate why DELETE privilege should not be granted broadly
CO-2,3;   [10]
• Revoke DELETE from a role and observe impact
BL-5
Ans:
Create Role:
CREATE ROLE FIN_READ_ROLE;
CREATE ROLE FIN_UPDATE_ROLE;
Assign Privileges:
GRANT SELECT ON FIN_TRANSACTIONS TO FIN_READ_ROLE;
GRANT SELECT, UPDATE ON FIN_TRANSACTIONS TO
FIN_UPDATE_ROLE;
GRANT SELECT, INSERT, UPDATE, DELETE ON FIN_TRANSACTIONS
TO FIN_HEAD_ROLE;
Assigning Roles to Users
GRANT FIN_READ_ROLE TO JUNIOR_USER;
GRANT FIN_UPDATE_ROLE TO SENIOR_USER;
GRANT FIN_HEAD_ROLE TO FIN_HEAD_USER;
Revoke DELETE from Role
********** 7 **********
--- page 8 ---
REVOKE DELETE ON FIN_TRANSACTIONS FROM
FIN_UPDATE_ROLE;
b.   A medium-sized company is planning to migrate its existing on-premises
database to the cloud to take advantage of scalability and cost savings. The
company's data is critical for its daily operations.
Question:
• What considerations would you take into account when planning and
executing the migration of the database to the cloud? How would you
ensure data consistency and minimize downtime during the migration
process?
•   Define backup and recovery policy for above organization.   [10]
Answer:
• Understand the backup environment.
• Perform capacity planning.
• Analyze current policies and procedures.
• Determine resource constraints.
•   Create a Backup Recovery Management Plan
• Implement the plan.
• Monitor the management plan.
Evaluate a scenario where frequent redo log switches are degrading database
a.   performance. Critically assess different redo log configuration strategies (such
as log file size, number of groups, and switching frequency), and justify the
most effective approach to optimize performance and maintain system
stability.
Ans:
Frequent redo log switches indicate that redo logs are too small or
insufficient in number, causing Oracle’s LGWR to switch logs rapidly. This
leads to increased checkpoint activity, I/O overhead, and potential
performance degradation.
[10]
• Each log switch triggers a checkpoint (CKPT + DBWn activity).
•   Excessive switches → frequent disk writes → CPU and I/O
Q6   overhead.
CO-2,   • Can cause “log file switch (checkpoint incomplete)” waits, slowing
CO3 ;   transactions.
BL-5,3   •   Impacts overall throughput and response time.
Approaches:
•   Increase Redo Log File Size
•   Increasing Number of Redo Log Groups
• Optimize Checkpoint Behavior
•   Place Logs on High-Speed Storage
b.   Differentiate Proactive Monitoring and Bottleneck Elimination with example.
Ans:
Proactive Monitoring
•   Proactive monitoring usually occurs on a regularly scheduled interval, [10]
where several performance statistics are examined to identify whether
the system behavior and resource usage has changed. Proactive
monitoring can also be considered as proactive tuning.
********** 8 **********
--- page 9 ---
•   Usually, monitoring does not result in configuration changes to the
system, unless the monitoring exposes a serious problem that is
developing. In some situations, experienced performance engineers can
identify potential problems through   statistics alone, although
accompanying performance degradation is usual.
• Experimenting with or tweaking a system when there is no apparent
performance degradation as a proactive action can be a dangerous
activity, resulting in unnecessary performance drops. Tweaking a
system should be considered reactive tuning, and the steps for reactive
tuning should be followed.
• Monitoring is usually part of a larger capacity planning exercise, where
resource consumption is examined to see changes in the way the
application is being used, and the way the application is using the
database and host resources.
Bottleneck Elimination
• Tuning usually implies fixing a performance problem. However, tuning
should be part of the life cycle of an application—through the analysis,
design, coding, production, and maintenance stages. Often, the tuning
phase is left until the database is in production. At this time, tuning
becomes a reactive process, where the most important bottleneck is
identified and fixed.
•   Usually, the purpose for tuning is to reduce resource consumption or to
reduce the elapsed time for an operation to complete. Either way, the
goal is to improve the effective use of a particular resource. In general,
performance problems are caused by the overuse of a particular
resource. The overused resource is the bottleneck in the system. There
are several distinct phases in identifying the bottleneck and the potential
fixes. These are discussed in the sections that follow.
Remember that the different forms of contention are symptoms that can be fixed
by making changes in the following places:
• Changes in the application, or the way the application is used
• Changes in Oracle
• Changes in the host hardware configuration.
a.   Apply your understanding to classify the different types of failures (such as soft
failure, hard failure, and network failure) that may occur in a database system.
Demonstrate how Oracle handles each type of failure using appropriate
recovery mechanisms, including the role of redo logs, undo data, and backups
in restoring the database to a consistent state.
Ans:
Q7
Classification of Failures:
CO-3;   [10]
Soft Failure (Instance Failure)
BL-4
•   Cause: Power failure, OS crash
•   Impact:
o Loss of SGA (memory)
o No damage to datafiles
Hard Failure (Media Failure)
•   Cause: Disk crash, file corruption
********** 9 **********
--- page 10 ---
•   Impact:
o Loss of datafiles, control files, or redo logs
o Permanent data loss unless backup exists
Network Failure
•   Cause: Communication breakdown between client and database
•   Impact:
o Session termination
o Database remains intact
Oracle Recovery Mechanisms:
Recovery for Soft Failure (Instance Recovery)
•   Automatically triggered during next startup by applying redo logs
Recovery for Hard Failure (Media Recovery)
•   Requires DBA intervention
Shutdown
Startup mount
RESTORE DATAFILE '/path/file.dbf';
RECOVER DATAFILE '/path/file.dbf';
ALTER DATABASE OPEN;
b.   Evaluate the process of manually creating control files in Oracle Database.
Under what circumstances would a DBA need to recreate control files, and
what precautions should be taken?
Ans:
Manual creation of control files in Oracle is a critical administrative
operation used when existing control files are lost, corrupted, or inconsistent.
Since control files maintain the physical structure of the database (datafiles,
redo logs, checkpoints), recreating them requires careful evaluation and
precision.
Performed in NOMOUNT mode, as control files are not yet available.
Requires accurate specification of:
•   Database name
•   Datafiles
• Redo log groups and members
[10]
• Followed by: RECOVER DATABASE , ALTER DATABASE OPEN
•   If redo information is incomplete → RESETLOGS option is required.
When Does a DBA Need to Recreate Control Files?
• Loss or Corruption of All Control Files
•   Inconsistent Control Files
•   Structural Changes
•   Database Renaming or Cloning
Precautions:
•   Maintain Control File Backups
•   Multiplex Control Files
•   Verify File Paths and Metadata
• Choose RESETLOGS vs NORESETLOGS Carefully
• Take Full Backup After Recreation
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 22f198376583

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Database Administration/ANS_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Database Administration
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the concept of 3-tier architecture in database systems. Describe the role
of each tier in processing user requests.
Ans:
The 3-tier architecture in database systems is a client-server model that
separates an application into three logical layers: Presentation Tier,
Application (Logic) Tier, and Database (Data) Tier. This separation
improves scalability, security, maintainability, and flexibility by distributing
responsibilities across different layers.
Roles of Each Tier in Processing User Requests:
Presentation layer:
• Accepts user request (e.g., login, query form)
CO-1;   • Sends request to the application tier
BL-2   •   Displays the processed output received
Application Tier (Business Logic Layer)
•   Receives request from presentation tier
•   Validates input and applies business logic
•   Converts request into database queries (SQL)
• Sends queries to the database tier
•   Processes results received and formats response
Database Tier (Data Layer)
•   Executes SQL queries sent by application tier
•   Retrieves or updates data
•   Ensures data integrity, security, and concurrency
• Sends results back to application tier
b.   A developer needs to create tables but should not perform backup operations.
CO-2;
How would you apply the principle of least privilege while creating this user?
BL-2
Ans:
********** 1 **********
--- page 2 ---
DBA should create a user account that has only the permissions required to
create and manage tables, and must not grant backup or administrative
privileges.
Only allow : create session, create table and limited storage quota
Why this follows least privilege
• CREATE SESSION allows the developer to log in.
• CREATE TABLE allows table creation only in their own schema.
• No backup-related privileges such as SYSDBA, SYSBACKUP, or other
administrative roles are granted.
• The user is restricted to only what is necessary for development work.
c.   Describe the role of control files in an Oracle database. Describe the type of
information stored in control files and its importance in database startup.
Ans: A control file is a critical binary file in an Oracle Database that
maintains essential information about the physical structure and state of the
database
Information Stored in Control Files:
• Database Identification Information
CO-2;   •   Datafile Information
BL-2   • Redo Log File Information
• Checkpoint Information
• Backup and Recovery Information
Importance During Database Startup:
•   Essential for Mount Stage
•   Locates Physical Files
•   Ensures Database Consistency
•   Supports Recovery Operations
d.   Explain the concept of shared server architecture in Oracle. Describe how it
improves scalability and resource utilization in a multi-user environment.
Ans:
The Shared Server Architecture allows multiple user sessions to share a pool of
server processes instead of each user having a dedicated server process. This
architecture is designed to efficiently handle large numbers of concurrent users.
Working:
•   Client Request Handling
CO-2;   • Queue Mechanism
BL-2   • Shared Server Processing
• Response Delivery
Improvement in Scalability
Supports More Users
• Many users share fewer server processes.
• Reduces system overhead compared to one process per user.
Efficient Handling of Idle Sessions
•   Ideal for environments where users are frequently
a.   A company is deploying an Oracle Database system for a multi-user enterprise
Q2   application. As a database administrator, you are required to illustrate and
CO-1;   explain the Oracle Database Architecture. demonstrate how the database [10]
BL-3   instance (memory structures and background processes) interacts with the
physical database components (data files, control files, and redo log files)
********** 2 **********
--- page 3 ---
Ans:
Oracle architecture consists of two main components:
• Database Instance → Memory structures + background processes
•   Physical Database → Datafiles, Control files, Redo log files
Database Instance Components
Memory Structures
SGA (System Global Area)
• Database Buffer Cache → stores data blocks
• Shared Pool → stores SQL and execution plans
• Redo Log Buffer → stores redo entries
PGA (Program Global Area)
• Private memory for each server process
• Used for sorting, session variables, etc.
Background Processes
1. DBWn (Database Writer)
o Writes modified data (dirty blocks) from buffer cache to
datafiles
2. LGWR (Log Writer)
o Writes redo entries from redo buffer to redo log files
3. CKPT (Checkpoint Process)
o Updates control files and datafile headers with
checkpoint info
4. SMON (System Monitor)
o Performs instance recovery after crashes
5. PMON (Process Monitor)
o Cleans up failed user processes
Physical Database Components
1. Data Files
o Store actual user data (tables, indexes)
2. Control Files
o Store metadata about database structure (file locations,
checkpoints)
3. Redo Log Files
o Store changes made to data for recovery purposes
Interaction Flow
User → SGA (Shared Pool + Buffer Cache + Redo Buffer)
→ Background Processes (DBWn, LGWR, CKPT)
→ Physical Files (Datafiles, Redo Logs, Control Files)
b.   A company observes performance issues due to improper memory allocation.
The DBA decides to modify database initialization parameters. Explain how
initialization parameters are configured and modified in Oracle.
[10]
Ans:
Initialization parameters define how an Oracle instance starts and operates,
especially memory allocation,
********** 3 **********
--- page 4 ---
•   Pfile
text file and
manually editable.
• SPFILE (Server Parameter File)
Binary file managed by Oracle
Preferred in production
Supports dynamic changes using SQL commands
For Dynamic Change (Immediate Effect):
ALTER SYSTEM SET shared_pool_size = 300M;
Persisting Changes:
ALTER SYSTEM SET db_cache_size = 600M SCOPE = SPFILE;
Apply to Both Memory and SPFILE:
ALTER SYSTEM SET pga_aggregate_target = 400M SCOPE = BOTH;
Using PFILE (Manual Editing)
1. Shutdown
2. Edit init.ora file
3. Restart database: STARTUP;
a.   In an organization, a user was mistakenly granted full access to critical database
tables, resulting in potential security risks and violation of access control
policies. Evaluate how a DBA should analyse and correct this situation by
appropriately granting and revoking privileges in an Oracle database system.
Ans:
Check system privileges:
SELECT * FROM DBA_SYS_PRIVS WHERE GRANTEE = 'USER_NAME
Check object privileges:
SELECT * FROM DBA_TAB_PRIVS WHERE GRANTEE =
'USER_NAME';
Check roles assigned:
SELECT * FROM DBA_ROLE_PRIVS WHERE GRANTEE =
'USER_NAME';
Detect risky privileges like SELECT ANY TABLE, DBA, WITH GRANT
Q3
OPTION
CO-2;   [10]
Corrective Actions Using REVOKE
BL-3
• REVOKE SELECT ANY TABLE FROM USER_NAME;
• REVOKE ALL ON employees FROM USER_NAME;
• REVOKE DBA FROM USER_NAME;
Reassigning Correct Privileges
GRANT SELECT ON employees TO USER_NAME;
Or
CREATE ROLE hr_read_only;
GRANT SELECT ON employees TO hr_read_only;
GRANT hr_read_only TO USER_NAME;
Preventive Measures
Implement Role-Based Access Control (RBAC)
Avoid granting powerful system privileges unnecessarily
********** 4 **********
--- page 5 ---
Restrict use of WITH GRANT OPTION
Enable auditing to track privilege usage:
b.   A company uses both traditional client/server applications and web-based
applications to access its Oracle database. Analyze the differences between
these connection architectures. Examine how Oracle Net supports both models
and how each impacts performance and scalability.
Ans:
Aspect   Client/Server (2-Tier)   Web-Based (3-Tier)
Through application
Connection   Direct DB connection
server
Shared / pooled
Server Process Dedicated per user
connections
Scalability   Limited   High
Resource
High   Optimized
Usage
Difficult (client
Maintenance   Easier (centralized)   [10]
updates)
Role of Oracle Net in Both Models:
In Client/Server Model
•   Direct communication using TNS (Transparent Network Substrate)
• Each client establishes its own session
• Uses listener to connect to dedicated server process
In Web-Based Model
•   Oracle Net connects application server to database
•   Supports:
o Connection pooling → reuse of sessions
o Shared Server architecture → multiple users share processes
• Reduces number of active database connections
a.   An enterprise HR application built on Oracle experiences slow query
performance during peak hours. Investigation reveals frequent hard parsing and
high CPU usage, even though the queries are repetitive.
Analyse the possible causes of this issue by examining the role of the Shared
Pool and Library Cache. Suggest how improper memory usage can lead to this
performance problem.
Ans:
Q4   Role of Shared Pool and Library Cache
CO-1.   Shared Pool
[10]
CO2 ;   •   Part of SGA that stores:
BL-4   o SQL statements
o Execution plans
o Data dictionary information
1. Library Cache
• Subcomponent of Shared Pool
•   Stores parsed SQL (cursor) and execution plans
•   Enables reuse of SQL statements to avoid re-parsing
2. Insufficient Shared Pool Size
********** 5 **********
--- page 6 ---
•   Limited memory causes frequent flushing of cached SQL
•   Execution plans are removed before reuse
• Leads to repeated hard parsing
3. Lack of SQL Reusability
4. Library Cache Contention
5. Improper Cursor Management
How Improper Memory Usage Leads to the Issue
•   Small or fragmented Shared Pool → SQL not retained
• High eviction rate → repeated parsing
•   Increased CPU cycles spent on parsing instead of execution
• Reduced throughput under heavy load
Solutions
• Optimize Shared Pool Memory
• Use Bind Variables
• Avoid Frequent Invalidations
• Monitor Library Cache
b.   Analyze the differences between legal and illegal multiplexed redo log
configurations in Oracle. Examine how the placement and structure of redo log
members affect database reliability, fault tolerance, and recovery.
Ans:
A multiplexed redo log configuration in Oracle improves fault tolerance by
maintaining multiple copies (members) of each redo log group. To analyze legal
vs illegal configurations, we evaluate how redo log members are distributed
across storage and how this impacts recovery and availability.
Legal Multiplexed Configuration
• Each redo log group contains multiple members stored on different
physical disks/locations.
• Example:
GROUP 1: /disk1/log1a.rdo, /disk2/log1b.rdo
[10]
GROUP 2: /disk1/log2a.rdo, /disk2/log2b.rdo
•   Ensures redundancy—if one disk fails, another member is still
accessible.
• LGWR writes simultaneously to all members, maintaining consistency.
Illegal Multiplexed Configuration
• Redo log members of the same group are placed on the same disk or
storage device.
• Example:
GROUP 1: /disk1/log1a.rdo, /disk1/log1b.rdo
•   Creates a single point of failure—disk crash results in loss of all
members in the group.
•   Defeats the purpose of multiplexing.
• Compromises data integrity and recovery capability.
********** 6 **********
--- page 7 ---
a.   Scenario
The finance department uses a FIN_TRANSACTIONS table. Incorrect
privilege assignment previously caused accidental deletions.
Roles Required
• FIN_READ_ROLE
• FIN_UPDATE_ROLE
Requirements
1. Junior accountants:
o Can only SELECT records
2. Senior accountants:
o Can UPDATE but cannot DELETE
3. Finance head:
o   Full access
Student Tasks
•   Create roles with granular privileges
•   Assign roles to users
Q5
•   Demonstrate why DELETE privilege should not be granted broadly
CO-2,3;   [10]
• Revoke DELETE from a role and observe impact
BL-5
Ans:
Create Role:
CREATE ROLE FIN_READ_ROLE;
CREATE ROLE FIN_UPDATE_ROLE;
Assign Privileges:
GRANT SELECT ON FIN_TRANSACTIONS TO FIN_READ_ROLE;
GRANT SELECT, UPDATE ON FIN_TRANSACTIONS TO
FIN_UPDATE_ROLE;
GRANT SELECT, INSERT, UPDATE, DELETE ON FIN_TRANSACTIONS
TO FIN_HEAD_ROLE;
Assigning Roles to Users
GRANT FIN_READ_ROLE TO JUNIOR_USER;
GRANT FIN_UPDATE_ROLE TO SENIOR_USER;
GRANT FIN_HEAD_ROLE TO FIN_HEAD_USER;
Revoke DELETE from Role
********** 7 **********
--- page 8 ---
REVOKE DELETE ON FIN_TRANSACTIONS FROM
FIN_UPDATE_ROLE;
b.   A medium-sized company is planning to migrate its existing on-premises
database to the cloud to take advantage of scalability and cost savings. The
company's data is critical for its daily operations.
Question:
• What considerations would you take into account when planning and
executing the migration of the database to the cloud? How would you
ensure data consistency and minimize downtime during the migration
process?
•   Define backup and recovery policy for above organization.   [10]
Answer:
• Understand the backup environment.
• Perform capacity planning.
• Analyze current policies and procedures.
• Determine resource constraints.
•   Create a Backup Recovery Management Plan
• Implement the plan.
• Monitor the management plan.
Evaluate a scenario where frequent redo log switches are degrading database
a.   performance. Critically assess different redo log configuration strategies (such
as log file size, number of groups, and switching frequency), and justify the
most effective approach to optimize performance and maintain system
stability.
Ans:
Frequent redo log switches indicate that redo logs are too small or
insufficient in number, causing Oracle’s LGWR to switch logs rapidly. This
leads to increased checkpoint activity, I/O overhead, and potential
performance degradation.
[10]
• Each log switch triggers a checkpoint (CKPT + DBWn activity).
•   Excessive switches → frequent disk writes → CPU and I/O
Q6   overhead.
CO-2,   • Can cause “log file switch (checkpoint incomplete)” waits, slowing
CO3 ;   transactions.
BL-5,3   •   Impacts overall throughput and response time.
Approaches:
•   Increase Redo Log File Size
•   Increasing Number of Redo Log Groups
• Optimize Checkpoint Behavior
•   Place Logs on High-Speed Storage
b.   Differentiate Proactive Monitoring and Bottleneck Elimination with example.
Ans:
Proactive Monitoring
•   Proactive monitoring usually occurs on a regularly scheduled interval, [10]
where several performance statistics are examined to identify whether
the system behavior and resource usage has changed. Proactive
monitoring can also be considered as proactive tuning.
********** 8 **********
--- page 9 ---
•   Usually, monitoring does not result in configuration changes to the
system, unless the monitoring exposes a serious problem that is
developing. In some situations, experienced performance engineers can
identify potential problems through   statistics alone, although
accompanying performance degradation is usual.
• Experimenting with or tweaking a system when there is no apparent
performance degradation as a proactive action can be a dangerous
activity, resulting in unnecessary performance drops. Tweaking a
system should be considered reactive tuning, and the steps for reactive
tuning should be followed.
• Monitoring is usually part of a larger capacity planning exercise, where
resource consumption is examined to see changes in the way the
application is being used, and the way the application is using the
database and host resources.
Bottleneck Elimination
• Tuning usually implies fixing a performance problem. However, tuning
should be part of the life cycle of an application—through the analysis,
design, coding, production, and maintenance stages. Often, the tuning
phase is left until the database is in production. At this time, tuning
becomes a reactive process, where the most important bottleneck is
identified and fixed.
•   Usually, the purpose for tuning is to reduce resource consumption or to
reduce the elapsed time for an operation to complete. Either way, the
goal is to improve the effective use of a particular resource. In general,
performance problems are caused by the overuse of a particular
resource. The overused resource is the bottleneck in the system. There
are several distinct phases in identifying the bottleneck and the potential
fixes. These are discussed in the sections that follow.
Remember that the different forms of contention are symptoms that can be fixed
by making changes in the following places:
• Changes in the application, or the way the application is used
• Changes in Oracle
• Changes in the host hardware configuration.
a.   Apply your understanding to classify the different types of failures (such as soft
failure, hard failure, and network failure) that may occur in a database system.
Demonstrate how Oracle handles each type of failure using appropriate
recovery mechanisms, including the role of redo logs, undo data, and backups
in restoring the database to a consistent state.
Ans:
Q7
Classification of Failures:
CO-3;   [10]
Soft Failure (Instance Failure)
BL-4
•   Cause: Power failure, OS crash
•   Impact:
o Loss of SGA (memory)
o No damage to datafiles
Hard Failure (Media Failure)
•   Cause: Disk crash, file corruption
********** 9 **********
--- page 10 ---
•   Impact:
o Loss of datafiles, control files, or redo logs
o Permanent data loss unless backup exists
Network Failure
•   Cause: Communication breakdown between client and database
•   Impact:
o Session termination
o Database remains intact
Oracle Recovery Mechanisms:
Recovery for Soft Failure (Instance Recovery)
•   Automatically triggered during next startup by applying redo logs
Recovery for Hard Failure (Media Recovery)
•   Requires DBA intervention
Shutdown
Startup mount
RESTORE DATAFILE '/path/file.dbf';
RECOVER DATAFILE '/path/file.dbf';
ALTER DATABASE OPEN;
b.   Evaluate the process of manually creating control files in Oracle Database.
Under what circumstances would a DBA need to recreate control files, and
what precautions should be taken?
Ans:
Manual creation of control files in Oracle is a critical administrative
operation used when existing control files are lost, corrupted, or inconsistent.
Since control files maintain the physical structure of the database (datafiles,
redo logs, checkpoints), recreating them requires careful evaluation and
precision.
Performed in NOMOUNT mode, as control files are not yet available.
Requires accurate specification of:
•   Database name
•   Datafiles
• Redo log groups and members
[10]
• Followed by: RECOVER DATABASE , ALTER DATABASE OPEN
•   If redo information is incomplete → RESETLOGS option is required.
When Does a DBA Need to Recreate Control Files?
• Loss or Corruption of All Control Files
•   Inconsistent Control Files
•   Structural Changes
•   Database Renaming or Cloning
Precautions:
•   Maintain Control File Backups
•   Multiplex Control Files
•   Verify File Paths and Metadata
• Choose RESETLOGS vs NORESETLOGS Carefully
• Take Full Backup After Recreation
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper ca6a226a9a56

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_IT_7041/Database Administration/ANS_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Database Administration
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Define the concept of database administration. Discuss the roles and
responsibilities of a DBA in an organization.
Ans:
Database Administration (DBA) refers to the process of managing,
maintaining, securing, and optimizing a database system to ensure it
operates efficiently, reliably, and securely
CO-1;   Roles and Responsibilities of a DBA
BL-2   • Database Installation and Configuration
• Database Design and Creation
•   Security Management
• Backup and Recovery Management
• Performance Monitoring and Tuning
• Data Integrity and Availability
•   Troubleshooting and Maintenance
b.   A DBA wants to check which roles are assigned to a particular user for
auditing purposes. Explain how to query role information in Oracle using data
dictionary views
Ans:
CO-2;   DBA_ROLE_PRIVS
BL-2   •   Contains information about roles granted to users and other roles
• USER_ROLE_PRIVS Shows roles granted to the current logged-in
user
• ALL_ROLE_PRIVS Shows roles accessible to the user based on
privileges
c.   Describe the process of managing database files in Oracle. Describe how data
CO-2;
files are created and maintained within a database system.
BL-3
Ans:
********** 1 **********
--- page 2 ---
Managing database files in Oracle involves handling the creation, storage,
organization, and maintenance of physical files such as data files, control
files, and redo log files to ensure efficient data storage and database
operation.
Types of Database Files
• Data Files → Store actual user data (tables, indexes)
• Control Files → Store metadata about database structure
• Redo Log Files → Store changes made to data for recovery
Creation of Data Files
CREATE TABLESPACE users
DATAFILE '/u01/oradata/users01.dbf'
SIZE 100M;
Maintenance of Data Files
ALTER DATABASE DATAFILE '/u01/oradata/users01.dbf' RESIZE 200M;
Or
ALTER TABLESPACE users
ADD DATAFILE '/u01/oradata/users02.dbf' SIZE 100M;
d.   Explain the role of Oracle Net Services in database connectivity. Describe
how it facilitates communication between client applications and the Oracle
database server.
Ans:
Oracle Net Services is a communication layer in Oracle that enables
connection between client applications and the Oracle database server
over a network. It uses the Transparent Network Substrate (TNS) protocol
to manage data exchange.
Role of Oracle Net Services in Connectivity
CO-2;
•   Acts as an interface between client and database
BL-2
•   Establishes and maintains network sessions
•   Handles connection requests and routing
•   Ensures reliable data transmission across networks
How It Facilitates Communication
•   Connection Request
•   Listener Interaction
•   Session Establishment
• Data Communication
•   Connection Termination
a.   Apply appropriate considerations to explain how factors such as hardware
requirements, operating system   compatibility, storage planning, and
configuration settings influence a successful installation.
Ans:
Hardware Requirements:
• CPU: Multi-core processors improve parallel processing and query
Q2
execution
CO-1;   [10]
• RAM: Adequate memory is required for SGA and PGA allocation
BL-3
• Network:   High-speed   network   supports   faster   client-server
communication
Operating System Compatibility
•   Database software must be installed on a supported OS version
•   Ensure correct kernel parameters and dependencies
Storage Planning
********** 2 **********
--- page 3 ---
•   Allocate sufficient disk space for Datafiles , Redo log files , Control
files
Configuration Settings
•   Set initialization parameters
• Choose database options (ARCHIVELOG mode, block size)
b.   After the system restarts, the database is not fully available to users. The DBA
needs to bring the database online step-by-step. Explain the stages of database
startup (Nomount, Mount, Open) and describe what operations are performed
at each stage
Ans:
NOMOUNT Stage (Instance Initialization)
STARTUP NOMOUNT;
• Reads initialization parameter file (PFILE/SPFILE)
•   Allocates memory structures (SGA)
[10]
•   Starts background processes (DBWn, LGWR, SMON, PMON)
ALTER DATABASE MOUNT;
• Opens and reads control files
•   Identifies Datafiles, Redo log files
•   Verifies database structure
ALTER DATABASE OPEN;
• Opens datafiles and redo log files
•   Performs instance recovery (if required)
• Makes database available for user access
a.   A large organization consists of multiple departments such as HR, Finance, and
Sales, each requiring different levels of access to the Oracle database.
Analyze how a DBA can design and implement role-based access control to
manage user groups efficiently. Explain how roles can be created, assigned, and
managed for different departments for improved security, scalability and ease
of administration.
Ans:
Concept of Role-Based Access Control (RBAC)
RBAC allows the DBA to:
•   Create roles (group of privileges)
•   Assign roles to users based on job responsibilities
•   Simplify administration and improve security
Q3
CREATE ROLE HR_ROLE;
CO-2;   [10]
GRANT SELECT, INSERT, UPDATE ON employees TO HR_ROLE;
BL-3
CREATE ROLE FIN_ROLE;
GRANT SELECT, UPDATE ON transactions TO FIN_ROLE;
CREATE ROLE SALES_ROLE;
GRANT SELECT ON customers TO SALES_ROLE;
Assigning Roles to Users
GRANT HR_ROLE TO HR_USER1;
GRANT FIN_ROLE TO FIN_USER1;
GRANT SALES_ROLE TO SALES_USER1;
********** 3 **********
--- page 4 ---
Modifying Role Privileges
GRANT DELETE ON transactions TO FIN_ROLE;
REVOKE DELETE ON transactions FROM FIN_ROLE;
REVOKE FIN_ROLE FROM FIN_USER1;
Benefits of RBAC
Security
• Implements least privilege principle
•   Prevents unauthorized access
Scalability
• Easy to manage large number of users
• Changes made at role level affect all users
Ease of Administration
• Reduces complexity of privilege management
•   Centralized control of permissions
b.   Compare shared server architecture and dedicated server architecture. A
database server is experiencing high load due to a large number of simultaneous
user connections. Analyze and justify which server architecture can be used to
handle this situation.
Ans:
Dedicated Server Architecture
• Each client connection gets a separate server process
•   One-to-one mapping: Client ↔ Server Process
•   Faster response for individual users
•   Higher memory and CPU usage
•   Suitable for: Low to moderate number of users and Resource-
intensive or long-running queries
[10]
Shared Server Architecture:
•   Multiple clients share a pool of server processes via dispatchers
• Many-to-few mapping: Multiple Clients ↔ Shared Servers
• Uses request and response queues in SGA
• Reduces number of active processes
•   Suitable for: Large number of concurrent users and Applications with
frequent idle time
Solution: Use Shared Server Architecture as it will
• Reduces number of server processes
•   Efficient utilization of memory and CPU
•   Handles large user base effectively
• Minimizes idle resource wastage
a.   Analyze the two fundamental memory structures associated with a database
instance. Examine how each structure contributes to system performance,
resource utilization, and overall database functionality, with appropriate
examples.
Q4
Ans:
CO-1.
An Oracle database instance consists of two fundamental memory structures:   [10]
CO2 ;
• SGA (System Global Area) – Shared memory
BL-4
• PGA (Program Global Area) – Private memory
SGA:
•   Shared among all users
•   Allocated at instance startup
********** 4 **********
--- page 5 ---
Key Components & Contributions
A. Database Buffer Cache
•   Stores frequently accessed data blocks
Performance Impact:
• Reduces disk I/O → faster query execution
Example:
Repeated query on EMPLOYEES table fetches data from cache instead of
disk
B. Shared Pool
•   Stores SQL statements and execution plans
Performance Impact: Enables soft parsing, reducing CPU usage
Example:
Same query reused → avoids repeated parsing
C. Redo Log Buffer
•   Stores redo entries before writing to disk
Functionality Impact: Ensures data recovery and durability
2. Program Global Area (PGA)
•   Private to each server process
• Not shared
Key Components & Contributions
A. Work Areas (Sort, Hash, Join)
Performance Impact:
•   Enables efficient query processing
Example:
Large ORDER BY operation uses PGA for sorting
B. Session Memory
Functionality Impact:
•   Stores session variables and state
b.   How would a DBA create a new control file in case of control file loss or
corruption? Illustrate with an example.
Ans:
In case of control file loss or corruption, the DBA must restore database
metadata either by restoring a backup control file (preferred) or recreating
a new control file manually when no backup is available. Control files are
critical as they store database structure, file locations, and checkpoint
information.
When to Create a New Control File (Evaluation)   [10]
A DBA should choose CREATE CONTROLFILE when:
•   All control file copies are lost/corrupted
• No valid backup is available
•   Datafiles and redo logs are intact
Recreation is risky and requires accurate file information, otherwise
recovery may fail.
Steps to Create a New Control File
Shutdown
********** 5 **********
--- page 6 ---
STARTUP NOMOUNT;
CREATE CONTROLFILE REUSE DATABASE "ORCL" RESETLOGS
NOARCHIVELOG
MAXLOGFILES 16
MAXDATAFILES 100
LOGFILE
GROUP 1 '/u01/app/oracle/oradata/orcl/redo01.log' SIZE 50M,
GROUP 2 '/u01/app/oracle/oradata/orcl/redo02.log' SIZE 50M
DATAFILE
'/u01/app/oracle/oradata/orcl/system01.dbf',
'/u01/app/oracle/oradata/orcl/sysaux01.dbf',
'/u01/app/oracle/oradata/orcl/users01.dbf';
RECOVER DATABASE USING BACKUP CONTROLFILE;
ALTER DATABASE OPEN RESETLOGS;
Alternative which is safe and prefferd:
Restore control file using RMAN:
RESTORE CONTROLFILE FROM AUTOBACKUP;
Preventive Measures
•   Maintain multiplexed control files:
• Regular RMAN backups
• Monitor file integrity
a.   Provide step-by-step SQL commands to execute the following scenario:
• User Raj creates two users: Meera and Karan.
• User Raj grants object privileges to Meera with the GRANT OPTION
(including permissions such as creating tables, selecting data, and
granting privileges to other users).
• User Meera further grants the SELECT privilege to user Karan.
•   Later, if user Raj revokes the granted privileges from Meera, the
privileges should also be automatically revoked from Karan.
•   Finally, user Raj drops the user Karan.
Ans:
Q5   CONN raj/password;
CO-2,3;   CREATE USER meera IDENTIFIED BY meera123;   [10]
BL-5, 2   CREATE USER karan IDENTIFIED BY karan123;
GRANT CREATE SESSION TO meera;
GRANT CREATE SESSION TO karan;
GRANT CREATE TABLE TO meera WITH ADMIN OPTION;
CONN raj/password;
CREATE TABLE emp_data (
emp_id NUMBER,
emp_name VARCHAR2(50),
salary NUMBER
);
********** 6 **********
--- page 7 ---
INSERT INTO emp_data VALUES (1, 'Asha', 50000);
INSERT INTO emp_data VALUES (2, 'Rohan', 60000);
COMMIT;
GRANT SELECT ON emp_data TO meera WITH GRANT OPTION;
CONN meera/meera123;
GRANT SELECT ON raj.emp_data TO karan;
CONN karan/karan123;
SELECT * FROM raj.emp_data;
CONN raj/password;
REVOKE SELECT ON emp_data FROM meera;
CONN karan/karan123;
SELECT * FROM raj.emp_data;
Error: table or view does not exist
CONN system/password;
DROP USER karan CASCADE;
b.   Organization requires continuous database availability and cannot shut down
the system for backups. Apply your knowledge to demonstrate how to perform
online (inconsistent) backups in ARCHIVELOG mode. Explain the role of redo
logs and archived logs in ensuring data consistency during recovery.
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
ALTER DATABASE ARCHIVELOG;
ALTER DATABASE OPEN;
Performing Online Backup
ALTER TABLESPACE users BEGIN BACKUP;
[10]
Copy Datafiles (OS Command)
cp /u01/oradata/users01.dbf /backup/users01.dbf
ALTER TABLESPACE users END BACKUP;
Backup Control File
ALTER DATABASE BACKUP CONTROLFILE TO
'/backup/controlfile.bkp';
Why It Is Called “Inconsistent Backup”
• Data blocks may be partially written during backup
•   Files are not synchronized at the same checkpoint
•   Requires recovery using redo logs
One member of a redo log group becomes corrupted, but the database is still
Q6   a.   running.
CO-2,   •   Write SQL commands to drop the corrupted redo log member.
[10]
CO3 ;   • Add a new member to the same group.
BL-5,3   Explain why the database continues functioning and how multiplexing helps
maintain availability.
********** 7 **********
--- page 8 ---
Ans: Drop the Corrupted Redo Log Member
ALTER DATABASE DROP LOGFILE MEMBER
'/u01/oradata/orcl/redo01.log';
Add a New Member to the Same Group
ALTER DATABASE ADD LOGFILE MEMBER
'/u02/oradata/orcl/redo01_new.log'
TO GROUP 1;
Why Database Continues Functioning
• Redo log groups are designed with multiple members (copies)
•   Oracle writes redo entries simultaneously to all members
•   If one member fails:
o Other members still contain valid redo data
o Database continues normal operations without interruption
Role of Multiplexing in Availability
Concept of Multiplexing
•   Maintaining multiple copies of redo log files in different locations
Benefits
•   Failure of one member does not affect system
•   Failure of one member does not affect system
• Redo information preserved for recovery
b.   What are the key responsibilities and advantages of employing a virtual DBA
(Database Administrator) for managing and maintaining database systems
remotely, and how does this approach compare to traditional in-house DBA
services
Ans:
Remote Database Administration (DBA) and Virtual DBA services are closely
related concepts, often used interchangeably in the context of managing Oracle
databases remotely. However, there are some nuances to consider:
Remote Database Administration (Remote DBA):
• Remote DBA refers to the practice of managing, monitoring, and
maintaining Oracle databases from a location that is separate from the
physical servers housing the databases.
• Remote DBAs may work for an organization but operate from a
different office or location, or they may be contracted from a third-party
service provider.
• Remote DBAs typically handle all aspects of database administration,
including installation, configuration, performance tuning, backup and [10]
recovery, security management, and ongoing maintenance.
Virtual DBA:
•   Virtual DBA is a specific type of remote DBA service where the DBA
functions are outsourced to a third-party provider who offers virtualized
support.
•   Virtual DBAs may not be dedicated full-time employees of the client
organization but rather work on-demand or as part of a contracted
service.
•   Virtual DBAs leverage remote access tools, monitoring software, and
communication channels to provide database administration services
without the need for physical presence at the client's site.
•   Virtual DBAs often offer flexible support options, allowing clients to
scale   their database administration needs according to   their
requirements.
********** 8 **********
--- page 9 ---
a.   After a system crash, the database undergoes instance recovery during startup.
Apply your knowledge to explain the phases of instance recovery and
demonstrate how checkpoints influence recovery time and performance.
Ans:
•   Instance Failure Occurs due to unexpected shutdown (power failure,
system crash)
•   Affects SGA and background process termination
• Impact of Failure
o Uncommitted transactions → Lost from memory
[10]
o Committed but not yet written data (dirty buffers) → Missing
in datafiles
o Database may become inconsistent
• Recovery
Oracle automatically performs Instance Recovery during next startup using
Redo Logs (Roll Forward Phase)
Undo Data (Roll Back Phase)
Automatic Instance Recovery using SMON
b.   A database experiences loss of a datafile due to disk failure. Apply your
Q7   understanding of media recovery to demonstrate the steps required to restore
CO-3;   and recover the damaged datafile using archived redo logs
BL-4   Ans:
(Media Failure)
•   Physical damage to datafile
•   Database may become partially unavailable
•   Requires backup + redo logs for recovery
Step 1: Identify the Damaged Datafile
SELECT file#, name FROM V$DATAFILE;
Step 2: Take Datafile Offline
ALTER DATABASE DATAFILE '/u01/oradata/users01.dbf' OFFLINE;   [10]
Step 3: Restore Datafile from Backup
RESTORE DATAFILE '/u01/oradata/users01.dbf';
RESTORE DATAFILE '/u01/oradata/users01.dbf';
RECOVER DATAFILE '/u01/oradata/users01.dbf';
Bring Datafile Online
ALTER DATABASE DATAFILE '/u01/oradata/users01.dbf' ONLINE;
Role of Archived Redo Logs
•   Store history of all database changes
• Used to roll forward restored datafile
•   Essential for complete recovery
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 10 · Answer key · paper 07d2fe95061c

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Re-Exam/Integrated_IT_7037/Database Administration/ANS_Database Administration(702IT0E038)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Database Administration
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Define the concept of database administration. Discuss the roles and
responsibilities of a DBA in an organization.
Ans:
Database Administration (DBA) refers to the process of managing,
maintaining, securing, and optimizing a database system to ensure it
operates efficiently, reliably, and securely
CO-1;   Roles and Responsibilities of a DBA
BL-2   • Database Installation and Configuration
• Database Design and Creation
•   Security Management
• Backup and Recovery Management
• Performance Monitoring and Tuning
• Data Integrity and Availability
•   Troubleshooting and Maintenance
b.   A DBA wants to check which roles are assigned to a particular user for
auditing purposes. Explain how to query role information in Oracle using data
dictionary views
Ans:
CO-2;   DBA_ROLE_PRIVS
BL-2   •   Contains information about roles granted to users and other roles
• USER_ROLE_PRIVS Shows roles granted to the current logged-in
user
• ALL_ROLE_PRIVS Shows roles accessible to the user based on
privileges
c.   Describe the process of managing database files in Oracle. Describe how data
CO-2;
files are created and maintained within a database system.
BL-3
Ans:
********** 1 **********
--- page 2 ---
Managing database files in Oracle involves handling the creation, storage,
organization, and maintenance of physical files such as data files, control
files, and redo log files to ensure efficient data storage and database
operation.
Types of Database Files
• Data Files → Store actual user data (tables, indexes)
• Control Files → Store metadata about database structure
• Redo Log Files → Store changes made to data for recovery
Creation of Data Files
CREATE TABLESPACE users
DATAFILE '/u01/oradata/users01.dbf'
SIZE 100M;
Maintenance of Data Files
ALTER DATABASE DATAFILE '/u01/oradata/users01.dbf' RESIZE 200M;
Or
ALTER TABLESPACE users
ADD DATAFILE '/u01/oradata/users02.dbf' SIZE 100M;
d.   Explain the role of Oracle Net Services in database connectivity. Describe
how it facilitates communication between client applications and the Oracle
database server.
Ans:
Oracle Net Services is a communication layer in Oracle that enables
connection between client applications and the Oracle database server
over a network. It uses the Transparent Network Substrate (TNS) protocol
to manage data exchange.
Role of Oracle Net Services in Connectivity
CO-2;
•   Acts as an interface between client and database
BL-2
•   Establishes and maintains network sessions
•   Handles connection requests and routing
•   Ensures reliable data transmission across networks
How It Facilitates Communication
•   Connection Request
•   Listener Interaction
•   Session Establishment
• Data Communication
•   Connection Termination
a.   Apply appropriate considerations to explain how factors such as hardware
requirements, operating system   compatibility, storage planning, and
configuration settings influence a successful installation.
Ans:
Hardware Requirements:
• CPU: Multi-core processors improve parallel processing and query
Q2
execution
CO-1;   [10]
• RAM: Adequate memory is required for SGA and PGA allocation
BL-3
• Network:   High-speed   network   supports   faster   client-server
communication
Operating System Compatibility
•   Database software must be installed on a supported OS version
•   Ensure correct kernel parameters and dependencies
Storage Planning
********** 2 **********
--- page 3 ---
•   Allocate sufficient disk space for Datafiles , Redo log files , Control
files
Configuration Settings
•   Set initialization parameters
• Choose database options (ARCHIVELOG mode, block size)
b.   After the system restarts, the database is not fully available to users. The DBA
needs to bring the database online step-by-step. Explain the stages of database
startup (Nomount, Mount, Open) and describe what operations are performed
at each stage
Ans:
NOMOUNT Stage (Instance Initialization)
STARTUP NOMOUNT;
• Reads initialization parameter file (PFILE/SPFILE)
•   Allocates memory structures (SGA)
[10]
•   Starts background processes (DBWn, LGWR, SMON, PMON)
ALTER DATABASE MOUNT;
• Opens and reads control files
•   Identifies Datafiles, Redo log files
•   Verifies database structure
ALTER DATABASE OPEN;
• Opens datafiles and redo log files
•   Performs instance recovery (if required)
• Makes database available for user access
a.   A large organization consists of multiple departments such as HR, Finance, and
Sales, each requiring different levels of access to the Oracle database.
Analyze how a DBA can design and implement role-based access control to
manage user groups efficiently. Explain how roles can be created, assigned, and
managed for different departments for improved security, scalability and ease
of administration.
Ans:
Concept of Role-Based Access Control (RBAC)
RBAC allows the DBA to:
•   Create roles (group of privileges)
•   Assign roles to users based on job responsibilities
•   Simplify administration and improve security
Q3
CREATE ROLE HR_ROLE;
CO-2;   [10]
GRANT SELECT, INSERT, UPDATE ON employees TO HR_ROLE;
BL-3
CREATE ROLE FIN_ROLE;
GRANT SELECT, UPDATE ON transactions TO FIN_ROLE;
CREATE ROLE SALES_ROLE;
GRANT SELECT ON customers TO SALES_ROLE;
Assigning Roles to Users
GRANT HR_ROLE TO HR_USER1;
GRANT FIN_ROLE TO FIN_USER1;
GRANT SALES_ROLE TO SALES_USER1;
********** 3 **********
--- page 4 ---
Modifying Role Privileges
GRANT DELETE ON transactions TO FIN_ROLE;
REVOKE DELETE ON transactions FROM FIN_ROLE;
REVOKE FIN_ROLE FROM FIN_USER1;
Benefits of RBAC
Security
• Implements least privilege principle
•   Prevents unauthorized access
Scalability
• Easy to manage large number of users
• Changes made at role level affect all users
Ease of Administration
• Reduces complexity of privilege management
•   Centralized control of permissions
b.   Compare shared server architecture and dedicated server architecture. A
database server is experiencing high load due to a large number of simultaneous
user connections. Analyze and justify which server architecture can be used to
handle this situation.
Ans:
Dedicated Server Architecture
• Each client connection gets a separate server process
•   One-to-one mapping: Client ↔ Server Process
•   Faster response for individual users
•   Higher memory and CPU usage
•   Suitable for: Low to moderate number of users and Resource-
intensive or long-running queries
[10]
Shared Server Architecture:
•   Multiple clients share a pool of server processes via dispatchers
• Many-to-few mapping: Multiple Clients ↔ Shared Servers
• Uses request and response queues in SGA
• Reduces number of active processes
•   Suitable for: Large number of concurrent users and Applications with
frequent idle time
Solution: Use Shared Server Architecture as it will
• Reduces number of server processes
•   Efficient utilization of memory and CPU
•   Handles large user base effectively
• Minimizes idle resource wastage
a.   Analyze the two fundamental memory structures associated with a database
instance. Examine how each structure contributes to system performance,
resource utilization, and overall database functionality, with appropriate
examples.
Q4
Ans:
CO-1.
An Oracle database instance consists of two fundamental memory structures:   [10]
CO2 ;
• SGA (System Global Area) – Shared memory
BL-4
• PGA (Program Global Area) – Private memory
SGA:
•   Shared among all users
•   Allocated at instance startup
********** 4 **********
--- page 5 ---
Key Components & Contributions
A. Database Buffer Cache
•   Stores frequently accessed data blocks
Performance Impact:
• Reduces disk I/O → faster query execution
Example:
Repeated query on EMPLOYEES table fetches data from cache instead of
disk
B. Shared Pool
•   Stores SQL statements and execution plans
Performance Impact: Enables soft parsing, reducing CPU usage
Example:
Same query reused → avoids repeated parsing
C. Redo Log Buffer
•   Stores redo entries before writing to disk
Functionality Impact: Ensures data recovery and durability
2. Program Global Area (PGA)
•   Private to each server process
• Not shared
Key Components & Contributions
A. Work Areas (Sort, Hash, Join)
Performance Impact:
•   Enables efficient query processing
Example:
Large ORDER BY operation uses PGA for sorting
B. Session Memory
Functionality Impact:
•   Stores session variables and state
b.   How would a DBA create a new control file in case of control file loss or
corruption? Illustrate with an example.
Ans:
In case of control file loss or corruption, the DBA must restore database
metadata either by restoring a backup control file (preferred) or recreating
a new control file manually when no backup is available. Control files are
critical as they store database structure, file locations, and checkpoint
information.
When to Create a New Control File (Evaluation)   [10]
A DBA should choose CREATE CONTROLFILE when:
•   All control file copies are lost/corrupted
• No valid backup is available
•   Datafiles and redo logs are intact
Recreation is risky and requires accurate file information, otherwise
recovery may fail.
Steps to Create a New Control File
Shutdown
********** 5 **********
--- page 6 ---
STARTUP NOMOUNT;
CREATE CONTROLFILE REUSE DATABASE "ORCL" RESETLOGS
NOARCHIVELOG
MAXLOGFILES 16
MAXDATAFILES 100
LOGFILE
GROUP 1 '/u01/app/oracle/oradata/orcl/redo01.log' SIZE 50M,
GROUP 2 '/u01/app/oracle/oradata/orcl/redo02.log' SIZE 50M
DATAFILE
'/u01/app/oracle/oradata/orcl/system01.dbf',
'/u01/app/oracle/oradata/orcl/sysaux01.dbf',
'/u01/app/oracle/oradata/orcl/users01.dbf';
RECOVER DATABASE USING BACKUP CONTROLFILE;
ALTER DATABASE OPEN RESETLOGS;
Alternative which is safe and prefferd:
Restore control file using RMAN:
RESTORE CONTROLFILE FROM AUTOBACKUP;
Preventive Measures
•   Maintain multiplexed control files:
• Regular RMAN backups
• Monitor file integrity
a.   Provide step-by-step SQL commands to execute the following scenario:
• User Raj creates two users: Meera and Karan.
• User Raj grants object privileges to Meera with the GRANT OPTION
(including permissions such as creating tables, selecting data, and
granting privileges to other users).
• User Meera further grants the SELECT privilege to user Karan.
•   Later, if user Raj revokes the granted privileges from Meera, the
privileges should also be automatically revoked from Karan.
•   Finally, user Raj drops the user Karan.
Ans:
Q5   CONN raj/password;
CO-2,3;   CREATE USER meera IDENTIFIED BY meera123;   [10]
BL-5, 2   CREATE USER karan IDENTIFIED BY karan123;
GRANT CREATE SESSION TO meera;
GRANT CREATE SESSION TO karan;
GRANT CREATE TABLE TO meera WITH ADMIN OPTION;
CONN raj/password;
CREATE TABLE emp_data (
emp_id NUMBER,
emp_name VARCHAR2(50),
salary NUMBER
);
********** 6 **********
--- page 7 ---
INSERT INTO emp_data VALUES (1, 'Asha', 50000);
INSERT INTO emp_data VALUES (2, 'Rohan', 60000);
COMMIT;
GRANT SELECT ON emp_data TO meera WITH GRANT OPTION;
CONN meera/meera123;
GRANT SELECT ON raj.emp_data TO karan;
CONN karan/karan123;
SELECT * FROM raj.emp_data;
CONN raj/password;
REVOKE SELECT ON emp_data FROM meera;
CONN karan/karan123;
SELECT * FROM raj.emp_data;
Error: table or view does not exist
CONN system/password;
DROP USER karan CASCADE;
b.   Organization requires continuous database availability and cannot shut down
the system for backups. Apply your knowledge to demonstrate how to perform
online (inconsistent) backups in ARCHIVELOG mode. Explain the role of redo
logs and archived logs in ensuring data consistency during recovery.
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
ALTER DATABASE ARCHIVELOG;
ALTER DATABASE OPEN;
Performing Online Backup
ALTER TABLESPACE users BEGIN BACKUP;
[10]
Copy Datafiles (OS Command)
cp /u01/oradata/users01.dbf /backup/users01.dbf
ALTER TABLESPACE users END BACKUP;
Backup Control File
ALTER DATABASE BACKUP CONTROLFILE TO
'/backup/controlfile.bkp';
Why It Is Called “Inconsistent Backup”
• Data blocks may be partially written during backup
•   Files are not synchronized at the same checkpoint
•   Requires recovery using redo logs
One member of a redo log group becomes corrupted, but the database is still
Q6   a.   running.
CO-2,   •   Write SQL commands to drop the corrupted redo log member.
[10]
CO3 ;   • Add a new member to the same group.
BL-5,3   Explain why the database continues functioning and how multiplexing helps
maintain availability.
********** 7 **********
--- page 8 ---
Ans: Drop the Corrupted Redo Log Member
ALTER DATABASE DROP LOGFILE MEMBER
'/u01/oradata/orcl/redo01.log';
Add a New Member to the Same Group
ALTER DATABASE ADD LOGFILE MEMBER
'/u02/oradata/orcl/redo01_new.log'
TO GROUP 1;
Why Database Continues Functioning
• Redo log groups are designed with multiple members (copies)
•   Oracle writes redo entries simultaneously to all members
•   If one member fails:
o Other members still contain valid redo data
o Database continues normal operations without interruption
Role of Multiplexing in Availability
Concept of Multiplexing
•   Maintaining multiple copies of redo log files in different locations
Benefits
•   Failure of one member does not affect system
•   Failure of one member does not affect system
• Redo information preserved for recovery
b.   What are the key responsibilities and advantages of employing a virtual DBA
(Database Administrator) for managing and maintaining database systems
remotely, and how does this approach compare to traditional in-house DBA
services
Ans:
Remote Database Administration (DBA) and Virtual DBA services are closely
related concepts, often used interchangeably in the context of managing Oracle
databases remotely. However, there are some nuances to consider:
Remote Database Administration (Remote DBA):
• Remote DBA refers to the practice of managing, monitoring, and
maintaining Oracle databases from a location that is separate from the
physical servers housing the databases.
• Remote DBAs may work for an organization but operate from a
different office or location, or they may be contracted from a third-party
service provider.
• Remote DBAs typically handle all aspects of database administration,
including installation, configuration, performance tuning, backup and [10]
recovery, security management, and ongoing maintenance.
Virtual DBA:
•   Virtual DBA is a specific type of remote DBA service where the DBA
functions are outsourced to a third-party provider who offers virtualized
support.
•   Virtual DBAs may not be dedicated full-time employees of the client
organization but rather work on-demand or as part of a contracted
service.
•   Virtual DBAs leverage remote access tools, monitoring software, and
communication channels to provide database administration services
without the need for physical presence at the client's site.
•   Virtual DBAs often offer flexible support options, allowing clients to
scale   their database administration needs according to   their
requirements.
********** 8 **********
--- page 9 ---
a.   After a system crash, the database undergoes instance recovery during startup.
Apply your knowledge to explain the phases of instance recovery and
demonstrate how checkpoints influence recovery time and performance.
Ans:
•   Instance Failure Occurs due to unexpected shutdown (power failure,
system crash)
•   Affects SGA and background process termination
• Impact of Failure
o Uncommitted transactions → Lost from memory
[10]
o Committed but not yet written data (dirty buffers) → Missing
in datafiles
o Database may become inconsistent
• Recovery
Oracle automatically performs Instance Recovery during next startup using
Redo Logs (Roll Forward Phase)
Undo Data (Roll Back Phase)
Automatic Instance Recovery using SMON
b.   A database experiences loss of a datafile due to disk failure. Apply your
Q7   understanding of media recovery to demonstrate the steps required to restore
CO-3;   and recover the damaged datafile using archived redo logs
BL-4   Ans:
(Media Failure)
•   Physical damage to datafile
•   Database may become partially unavailable
•   Requires backup + redo logs for recovery
Step 1: Identify the Damaged Datafile
SELECT file#, name FROM V$DATAFILE;
Step 2: Take Datafile Offline
ALTER DATABASE DATAFILE '/u01/oradata/users01.dbf' OFFLINE;   [10]
Step 3: Restore Datafile from Backup
RESTORE DATAFILE '/u01/oradata/users01.dbf';
RESTORE DATAFILE '/u01/oradata/users01.dbf';
RECOVER DATAFILE '/u01/oradata/users01.dbf';
Bring Datafile Online
ALTER DATABASE DATAFILE '/u01/oradata/users01.dbf' ONLINE;
Role of Archived Redo Logs
•   Store history of all database changes
• Used to roll forward restored datafile
•   Essential for complete recovery
********** 9 **********
````
