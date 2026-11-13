# Distributed Data Processing — syllabus

3 syllabus section(s) for this course in the archive, newest batch first. Text comes from the PDF (OCR for scanned pages; check figures against the source). All programmes' syllabi: [`syllabi/`](../../syllabi/README.md).

## M Tech · Artificial Intelligence · batch 2026-2028 · Sem 2

- Course as printed: Distributed Data Processing (code 703DB0C067)
- Source: `04_Syllabi_Archive/M Tech/Artificial Intelligence/Batch ( 2026 To 2028 )/Semester - 2.pdf`, page 3-5

````text
Program: M Tech Artificial Intelligence   Semester: II
Course: Distributed Data Processing   Code: 703DB0C067
Teaching Scheme   Evaluation Scheme
Lecture   Practical   Tutorial   Internal Continuous   Term End
(Hours per (Hours per   (Hours per   Credit   Assessment (ICA)   Examinations (TEE)
week)   week)   week)   (Marks - 50)   (Marks- 100)
3   0   0   3   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Basic understanding of distributed computing concepts & Python programming.
Knowledge of SQL and database management systems
Course Objective
This course aims to equip students with practical skills in distributed data processing using Apache Spark.
Students will learn Spark’s architecture, utilize Spark SQL for efficient data processing, deploy Spark
applications on Kubernetes, and implement Spark in real-world applications like machine learning and
streaming. By the end, students will be prepared to manage and optimize large-scale data workflows
effectively.
Course Outcomes
After completion of the course, students will be able to –
1. Understand the architecture of Apache Spark, including its components and task scheduling
mechanisms.
2. Apply Spark SQL for data processing, leveraging functions, joins, and optimization techniques.
3. Identify the core components required to configure Spark in Kubernetes, including the Docker
image, driver, and executor configurations.
4. Implement Spark in real-world scenarios, such as data warehousing, machine learning, and
structured streaming
Detailed Syllabus
Unit   Description   Duration
Spark Architecture
Driver Program - Executor Nodes - Driver-Executor Communication - Task
Scheduling - Executor Failures - Spark application lifecycle - Job scheduling - Task
execution - Result aggregation - Fault tolerance - Overview of Spark deployment
1.   options - Local mode - Standalone mode - YARN mode - Mesos mode - Kubernetes   07
mode - Cluster mode - Driver mode - Installing Spark on a cluster - Installing
Spark on a single machine - Best practices for deploying and managing Spark
installations.
PySpark Essentials
Installing PySpark - Configuring PySpark - Setting up Spark Environment
Variables - Configuring Spark Logging - Troubleshooting PySpark Installation -
2.   Introduction to DataFrames - Pandas Integration - Data Frame Operations -   09
DataFrames vs. RDDs - DataFrames and Data Warehousing - Cluster Mode -
Driver Mode - spark-submit - Spark Cluster Managers - Monitoring and
Debugging.
Signature
(Head of the Department)
M Tech AI /SEMESTER -II/AY 2026-27/Page 3 of 23
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Spark SQL Hands-On
Overview of Spark SQL functions, covering string, numeric, date, timestamp, and
aggregate functions, creating user-defined functions (UDFs), types and
3.   08
optimization of joins, aggregation techniques including grouping, filtering, and
window functions, and partitioning strategies with schemes, dynamic
partitioning, pruning, and best practices for optimization.
Structured Streaming
Introduction to Structured Streaming in Spark, creating and operating on
streaming DataFrames and Datasets, handling late and out-of-order data,
4.   11
deduplication methods and best practices, windowing and watermarking
techniques, managing state with the State Store, and understanding output
modes, including sinks and custom sinks, with best practices.
Deploying & Managing Spark Applications
Overview of Kubernetes and containerization, deploying and configuring Spark
on Kubernetes, best practices, Spark Connect for data ingestion and integration,   10
5.
observability in Spark including monitoring, logging, tracing, and alerting,
change management covering code changes, dependency management, rollback
strategies, and CI/CD for Spark applications.
Total   45
Text Books
1. Matei Zaharia and others, Spark: The Definitive Guide, O'Reilly Media, 2018.
2. Bill Chambers and Matei Zaharia, Spark in Action, Manning Publications, 2018.
Reference Books
1. Jules S. Damji, Learning Spark, Lightning-Fast Data Analytics, 2nd Edition, Shroff/O'Reilly, 2020.
2. Gerard Maas & Francois Garillot, Stream Processing with Apache Spark, O'Reilly Media, 2019.
3. Aurobindo Sarkar, Learning Spark SQL, Packt Publishing, 2017.
Signature
(Head of the Department)
M Tech AI /SEMESTER -II/AY 2026-27/Page 4 of 23
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Program: M Tech Artificial Intelligence   Semester: II
````

## M Tech · Artificial Intelligence · batch 2025-2027 · Sem 2

- Course as printed: Distributed Data Processing (code 703DB0C067)
- Source: `04_Syllabi_Archive/M Tech/Artificial Intelligence/Batch ( 2025 To 2027 )/Semester - 2.pdf`, page 4-6

````text
Program: M Tech Artificial Intelligence   Semester: II
Course: Distributed Data Processing   Code: 703DB0C067
Teaching Scheme   Evaluation Scheme
Lecture   Practical   Tutorial   Internal Continuous   Term End
(Hours per (Hours per   (Hours per   Credit   Assessment (ICA)   Examinations (TEE)
week)   week)   week)   (Marks - 50)   (Marks- 100)
3   0   0   3   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Basic understanding of distributed computing concepts & Python programming.
Knowledge of SQL and database management systems
Course Objective
This course aims to equip students with practical skills in distributed data processing using Apache Spark.
Students will learn Spark’s architecture, utilize Spark SQL for efficient data processing, deploy Spark
applications on Kubernetes, and implement Spark in real-world applications like machine learning and
streaming. By the end, students will be prepared to manage and optimize large-scale data workflows
effectively.
Course Outcomes
After completion of the course, students will be able to –
1. Understand the architecture of Apache Spark, including its components and task scheduling
mechanisms.
2. Apply Spark SQL for data processing, leveraging functions, joins, and optimization techniques.
3. Identify the core components required to configure Spark in Kubernetes, including the Docker
image, driver, and executor configurations.
4. Implement Spark in real-world scenarios, such as data warehousing, machine learning, and
structured streaming.
Detailed Syllabus
Unit   Description   Duration
Spark Architecture
Driver Program - Executor Nodes - Driver-Executor Communication - Task
Scheduling - Executor Failures - Spark application lifecycle - Job scheduling - Task
execution - Result aggregation - Fault tolerance - Overview of Spark deployment
1.   07
options - Local mode - Standalone mode - YARN mode - Mesos mode - Kubernetes
mode - Cluster mode - Driver mode - Installing Spark on a cluster - Installing
Spark on a single machine - Best practices for deploying and managing Spark
installations.
PySpark Essentials
Installing PySpark - Configuring PySpark - Setting up Spark Environment
Variables - Configuring Spark Logging - Troubleshooting PySpark Installation -
2.   Introduction to DataFrames - Pandas Integration - Data Frame Operations -   09
DataFrames vs. RDDs - DataFrames and Data Warehousing - Cluster Mode -
Driver Mode - spark-submit - Spark Cluster Managers - Monitoring and
Debugging.
Spark SQL Hands-On
3.   Overview of Spark SQL functions, covering string, numeric, date, timestamp, and   08
aggregate functions, creating user-defined functions (UDFs), types and
Signature
(Head of the Department)
M Tech AI /SEMESTER -II/AY 2025-26/Page 4 of 24
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
optimization of joins, aggregation techniques including grouping, filtering, and
window functions, and partitioning strategies with schemes, dynamic
partitioning, pruning, and best practices for optimization.
Structured Streaming
Introduction to Structured Streaming in Spark, creating and operating on
streaming DataFrames and Datasets, handling late and out-of-order data,
4.   11
deduplication methods and best practices, windowing and watermarking
techniques, managing state with the State Store, and understanding output
modes, including sinks and custom sinks, with best practices.
Deploying & Managing Spark Applications
Overview of Kubernetes and containerization, deploying and configuring Spark
on Kubernetes, best practices, Spark Connect for data ingestion and integration,
5.   10
observability in Spark including monitoring, logging, tracing, and alerting,
change management covering code changes, dependency management, rollback
strategies, and CI/CD for Spark applications.
Total   45
Text Books
1. Matei Zaharia and others, Spark: The Definitive Guide, O'Reilly Media, 2018.
2. Bill Chambers and Matei Zaharia, Spark in Action, Manning Publications, 2018.
Reference Books
1. Jules S. Damji, Learning Spark, Lightning-Fast Data Analytics, 2nd Edition, Shroff/O'Reilly, 2020.
2. Gerard Maas & Francois Garillot, Stream Processing with Apache Spark, O'Reilly Media, 2019.
3. Aurobindo Sarkar, Learning Spark SQL, Packt Publishing, 2017.
Signature
(Head of the Department)
M Tech AI /SEMESTER -II/AY 2025-26/Page 5 of 24
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Program: M Tech Artificial Intelligence   Semester: II
````

## M Tech · Artificial Intelligence · batch 2024-2026 · Sem 2

- Course as printed: Distributed Data Processing
- Source: `04_Syllabi_Archive/M Tech/Artificial Intelligence/Batch ( 2024 To 2026 )/Semester - 2.pdf`, page 4-6

````text
Program: M Tech Artificial Intelligence   Semester: II
Course: Distributed Data Processing   Code:
Teaching Scheme   Evaluation Scheme
Lecture   Practical   Tutorial   Internal Continuous   Term End
(Hours per (Hours per   (Hours per   Credit   Assessment (ICA)   Examinations (TEE)
week)   week)   week)   (Marks - 50)   (Marks- 100)
3   0   0   3   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Basic understanding of distributed computing concepts & Python programming.
Knowledge of SQL and database management systems
Course Objective
This course aims to equip students with practical skills in distributed data processing using Apache Spark.
Students will learn Spark’s architecture, utilize Spark SQL for efficient data processing, deploy Spark
applications on Kubernetes, and implement Spark in real-world applications like machine learning and
streaming. By the end, students will be prepared to manage and optimize large-scale data workflows
effectively.
Course Outcomes
After completion of the course, students will be able to –
1. Understand the architecture of Apache Spark, including its components and task scheduling
mechanisms.
2. Apply Spark SQL for data processing, leveraging functions, joins, and optimization techniques.
3. Identify the core components required to configure Spark in Kubernetes, including the Docker
image, driver, and executor configurations.
4. Implement Spark in real-world scenarios, such as data warehousing, machine learning, and
structured streaming.
Detailed Syllabus
Unit   Description   Duration
Spark Architecture
Driver Program - Executor Nodes - Driver-Executor Communication - Task
Scheduling - Executor Failures - Spark application lifecycle - Job scheduling - Task
execution - Result aggregation - Fault tolerance - Overview of Spark deployment
1.   07
options - Local mode - Standalone mode - YARN mode - Mesos mode - Kubernetes
mode - Cluster mode - Driver mode - Installing Spark on a cluster - Installing
Spark on a single machine - Best practices for deploying and managing Spark
installations.
PySpark Essentials
Installing PySpark - Configuring PySpark - Setting up Spark Environment
Variables - Configuring Spark Logging - Troubleshooting PySpark Installation -
2.   Introduction to DataFrames - Pandas Integration - Data Frame Operations -   09
DataFrames vs. RDDs - DataFrames and Data Warehousing - Cluster Mode -
Driver Mode - spark-submit - Spark Cluster Managers - Monitoring and
Debugging.
Spark SQL Hands-On
3.   Overview of Spark SQL functions, covering string, numeric, date, timestamp, and   08
aggregate functions, creating user-defined functions (UDFs), types and
Signature
(Head of the Department)
M Tech AI /2024-25/SEM II/Page 4 of 24
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
optimization of joins, aggregation techniques including grouping, filtering, and
window functions, and partitioning strategies with schemes, dynamic
partitioning, pruning, and best practices for optimization.
Structured Streaming
Introduction to Structured Streaming in Spark, creating and operating on
streaming DataFrames and Datasets, handling late and out-of-order data,
4.   11
deduplication methods and best practices, windowing and watermarking
techniques, managing state with the State Store, and understanding output
modes, including sinks and custom sinks, with best practices.
Deploying & Managing Spark Applications
Overview of Kubernetes and containerization, deploying and configuring Spark
on Kubernetes, best practices, Spark Connect for data ingestion and integration,
5.   10
observability in Spark including monitoring, logging, tracing, and alerting,
change management covering code changes, dependency management, rollback
strategies, and CI/CD for Spark applications.
Total   45
Text Books
1. Matei Zaharia and others, Spark: The Definitive Guide, O'Reilly Media, 2018.
2. Bill Chambers and Matei Zaharia, Spark in Action, Manning Publications, 2018.
Reference Books
1. Jules S. Damji, Learning Spark, Lightning-Fast Data Analytics, 2nd Edition, Shroff/O'Reilly, 2020.
2. Gerard Maas & Francois Garillot, Stream Processing with Apache Spark, O'Reilly Media, 2019.
3. Aurobindo Sarkar, Learning Spark SQL, Packt Publishing, 2017.
Signature
(Head of the Department)
M Tech AI /2024-25/SEM II/Page 5 of 24
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Program: M Tech Artificial Intelligence   Semester: II
````
