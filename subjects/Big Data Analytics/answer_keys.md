# Big Data Analytics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper eec9fab53bd4

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIML_7053/Big Data Analytics/ANS_Big Data Analytics(702DB0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (18 pages), mean OCR confidence 39.1
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/MBA Tech (Comp)/MBA Tech (DS)
Year: III / IV/Semester VI/Semester VIII(Exam Year: 2025-2026)
Subject: Big Data Analytics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1
Answer briefly:   [20]
a.   Describe the role of HDFS in Big Data.
Five points each 1 mark.
1. Core Storage and Distributed Architecture
HDFS is the backbone of Hadoop’s storage, providing a way to store massive
amounts of data across a cluster of computers. Instead of relying on a single
large server, it uses a distributed architecture where data is spread across many
nodes, allowing the system to scale from a single server to thousands of
machines.
2. Data Partitioning (Block Storage)
HDFS manages large files by splitting them into smaller, fixed-size units called
blocks.
•   Size: Common block sizes are 128 MB (preferred) or 64 MB.
• Mechanism: For example, a 1 GB file is divided into 8 blocks of 128 MB,
which are then distributed across different machines in the cluster so
CO-1; BL-1   they can be read and processed simultaneously.   [5]
3. Fault Tolerance through Replication
In a Big Data environment using low-cost commodity hardware, machine
failures are common. HDFS ensures data reliability by automatically replicating
each block multiple times—usually 3 replicas—across different nodes. If one
node crashes, the system seamlessly retrieves the data from another node
containing a replica, preventing data loss.
4. High Throughput and Data Locality
HDFS is optimized for batch processing rather than interactive user tasks,
providing high-throughput access to application data. A critical role it plays is
enabling Data Locality: instead of moving massive datasets over the network to
a program, Hadoop moves the processing program to the data stored on the
HDFS nodes. This significantly reduces network traffic and increases processing
speed.
5. Cost-Effectiveness and Management
********** 1 **********
--- page 2 ---
HDFS allows organizations to store Big Data cheaply by running on low-cost,
commodity hardware. It sits on top of local file systems and provides a suite of
HDFS Commands (like put, get, ls, and mkdir) to manage, monitor, and check
the health of the distributed files.
b.   Describe the working of NameNode and DataNode in HDFS.
Working of namenode- 3 marks
Working of datanode- 2 marks
In the Hadoop Distributed File System (HDFS), the architecture follows a
master-slave model where the NameNode acts as the master and DataNodes
act as slaves to manage storage across a cluster.
1. Working of the NameNode (Master)
The NameNode is the "brain" of the HDFS and is responsible for managing the
file system's metadata and governing access.
• Namespace Management: It maintains the hierarchical structure of
files and directories, similar to a Linux file system.
• Metadata Storage: It stores information about the files, such as their
size, permissions, and, most importantly, the mapping of file blocks to
specific DataNodes.
•   Access Control: It regulates client access to files and handles requests
to open, close, rename, or delete files and directories.
• Request Validation: When a client wants to write data, the NameNode
checks for permissions and ensures the file does not already exist
before providing a list of suitable DataNodes for storage.
2. Working of the DataNode (Slave)
CO-3; BL-2   DataNodes are the worker nodes that perform the actual task of storing and   [5]
retrieving data blocks.
•   Block Storage: They store data in fixed-size units called blocks (typically
128MB or 256MB).
• Data Operations: They handle read and write requests from HDFS
clients and perform block creation, deletion, and replication as
instructed by the NameNode.
•   Replication Pipeline: During a write operation, DataNodes work in a
pipeline. DataNode 1 receives data from the client, stores it, and
forwards it to DataNode 2, which then forwards it to DataNode 3 (based
on the replication factor).
• Data Integrity: Each DataNode is responsible for verifying the integrity
of its stored data using checksums during read/write operations to
detect any corruption.
3. Interaction Between NameNode and DataNode
The interaction ensures the system remains reliable and efficient:
• Write Coordination: The NameNode provides the client with the
locations (IP addresses) of DataNodes. The client then streams data
directly to those DataNodes to avoid bottlenecking the NameNode.
• Acknowledgment: Once DataNodes successfully store a block, they
send an acknowledgment (ACK) back through the pipeline to the client,
which then informs the NameNode to finalize the metadata.
********** 2 **********
--- page 3 ---
Fault Tolerance: If a DataNode or a block fails, the NameNode detects this and
coordinates with other DataNodes to create new replicas from healthy copies,
ensuring high availability
c.   Define execution modes used in Apache Pig. Compare Pig with MapReduce.
Execution mode [2 Marks]
Comparison between Pig and MapReduce [3 Marks]
Apache Pig Execution Modes
Local Mode
•   In this mode, all the files are installed and run from your local
host and local file system. There is no need of Hadoop or HDFS.
This mode is generally used for testing purpose.
MapReduce Mode
• MapReduce mode is where we load or process the data that exists
in the Hadoop File System (HDFS) using Apache Pig. In this
mode, whenever we execute the Pig Latin statements to process
the data, a MapReduce job is invoked in the back-end to perform
a particular operation on the data that exists in the HDFS.
Difference between Pig and MapReduce
Apache Pig   MapReduce
It is a compiled
It is a scripting language.   programming
CO-2; BL-3   language.   [5]
Abstraction is at higher   Abstraction is at
level.   lower level.
It have less line of code as
Lines of code is more.
compared to MapReduce.
More development
Less effort is needed for
efforts are required
Apache Pig.
for MapReduce.
As compared to Pig
Code efficiency is less as
efficiency of code is
compared to MapReduce.
higher.
Pig provides built in
Hard to perform data
functions for ordering,
operations.
sorting and union.
********** 3 **********
--- page 4 ---
It allows nested data types   It does not allow
like map, tuple and bag   nested data types
d.   What is cosine similarity in recommendation systems?
Cosine similarity is a measure used in recommendation systems to determine
how similar two users or items are by comparing their rating vectors. It
calculates the cosine of the angle between two vectors.
𝐴⋅𝐵
Cosine Similarity =
∥𝐴∥×∥𝐵∥
Where:
• 𝐴⋅𝐵= dot product of vectors
• ∥𝐴∥, ∥𝐵∥= magnitudes of vectors
Working
Represent users/items as vectors of ratings
CO-2; BL-2   • Compute similarity between vectors   [5]
• Value ranges from 0 to 1:
o 1 → very similar
o 0 → not similar
Example
User A = [5, 4, 0]
User B = [4, 5, 0]
•   Cosine similarity will be high, indicating similar preferences
Used to recommend items liked by similar users.
Applications
•   Collaborative filtering
• Movie and product recommendation systems
a.   Describe data ingestion process using Flume and Sqoop.
Q2
[10]
CO-3; BL-1   Data ingestion with flume and sqoop each 5 marks
********** 4 **********
--- page 5 ---
Data ingestion in Hadoop is the process of collecting data from various sources
(like logs, databases, or sensors) and moving it into a central system like HDFS
for processing and analysis. The specific steps for the two primary tools, Sqoop
and Flume, are as follows:
1. Data Ingestion with Apache Sqoop (Batch/Structured Data)
Sqoop is designed to transfer structured data between Relational Database
Management Systems (RDBMS) and HDFS.
Steps in the Sqoop Workflow:
1. Command Submission: The user issues a Sqoop import or export
command via the client terminal.
2. Job Translation: Sqoop converts the command into a MapReduce job
to enable large-scale parallel data transfer.
3. Framework Trigger: The MapReduce job is submitted to the Hadoop
cluster.
4. Establish Connection: Sqoop uses JDBC to establish a secure
connection with the source RDBMS (e.g., MySQL or Oracle).
5. Data Splitting: The database table is divided into logical "splits" based
on a primary key or specific column.
6. Parallel Transfer: Multiple Mappers (default is 4) independently and
simultaneously pull or push their assigned chunks of data.
7. HDFS Writing/Reading: During an import, the mappers write the data
into HDFS in formats such as text, Avro, or sequence files.
8. Job Completion: Once all mappers finish, Sqoop reports the final status
(success or failure) to the client.
Example: Transferring customer transaction tables from a MySQL database
into an HDFS directory for monthly batch reporting.
2. Data Ingestion with Apache Flume (Streaming/Semi-Structured Data)
Flume is optimized for the continuous collection and movement of log and
event data.
Steps in the Flume Workflow:
1. Event Generation: An external source, such as a web server, produces
a "Flume Event" (a byte array payload with optional headers).
2. Source Reception: The Flume Source component receives these events
from the generator over the network.
3. Channel Buffering: The Source sends the event to a Flume Channel,
which acts as a temporary buffer or store (often using the local file
system for reliability).
4. Sink Extraction: The Flume Sink removes the event from the channel.
5. Centralized Storage: The Sink writes the event to a centralized
repository like HDFS or Apache HBase. In complex setups, the Sink may
forward the event to the Source of another agent in a "multi-hop" flow.
Example: An e-commerce website (like Amazon) streaming live web server logs
into HDFS to perform real-time analysis of customer behavior in a specific
geographic region.
********** 5 **********
--- page 6 ---
b.   Explain user-based and item-based collaborative filtering techniques. Compare
their advantages, limitations, and applications in recommendation systems.
User based and item based collaborative filtering- each 4 marks
Comparison- 2 marks
Collaborative Filtering (CF) is a recommendation technique that predicts user
preferences based on past behavior. It is widely used in systems like Netflix and
Amazon.
Two main approaches are User-Based and Item-Based Collaborative
Filtering.
User-Based Collaborative Filtering
•   Finds users with similar preferences using similarity measures (e.g.,
cosine similarity).
• Recommends items liked by similar users.
Example:
•   If User A and User B have similar movie ratings, and User B likes Movie
X, then Movie X is recommended to User A.
CO-2; BL-2   Advantages:   [10]
• Simple and intuitive
•   Personalized recommendations
Limitations:
• Not scalable for large datasets
•   Suffers from sparsity (few common ratings)
Item-Based Collaborative Filtering
Working Principle:
•   Finds similarity between items instead of users.
• Recommends items similar to those the user has liked.
Example:
•   If a user likes Movie A and Movie A is similar to Movie B, then Movie
B is recommended.
Advantages:
• More scalable and efficient
•   Stable recommendations over time
Limitations:
•   Less personalized than user-based
•   Requires computation of item similarity
********** 6 **********
--- page 7 ---
a.   Draw and explain Hadoop architecture. What are the additional benefits that
YARN brings into Hadoop?
•   Architecture diagram → 2 Marks
• HDFS explanation → 4 Marks
• YARN explanation → 2 Marks
•   Benefits of YARN → 2 Marks
HDFS (Storage Layer)
Components:
• NameNode (Master): Stores metadata (file names, block locations),
Manages file system operations
• DataNode (Slave): Stores actual data blocks, Performs read/write
operations
Key Features:
Data is split into blocks and distributed across nodes
Replication ensures fault tolerance
High scalability and reliability
YARN (Processing Layer)
Components:
• ResourceManager (Master): Allocates cluster resources, Manages
Q3   scheduling
• NodeManager (Slave): Manages resources on each node, Executes   [10]
CO-1; BL-2
tasks
•   ApplicationMaster: Manages a specific application/job, Negotiates
resources from ResourceManager
MapReduce (Processing Model)
Divides job into:
Map tasks → Process input data
Reduce tasks → Aggregate results
Runs on top of YARN for distributed processing
Additional Benefits of YARN in Hadoop
•   Better Resource Management
Separates resource management from job scheduling
Efficient utilization of cluster resources
•   Scalability
Supports large clusters (thousands of nodes)
Handles multiple applications simultaneously
• Improved Performance
Parallel execution of multiple jobs
Reduces bottlenecks of JobTracker (in Hadoop 1.x)
•   Fault Tolerance
Automatically restarts failed tasks
Ensures continuous execution
• Dynamic Resource Allocation
Allocates resources based on demand
Supports container-based execution
********** 7 **********
--- page 8 ---
b.
Write commands and outputs for the following using Hive
•   Create database ‘Sales’ and table ‘Order_Details’and Customer with
(Order_id (int), Customer_id (int), Amount (int), Order_date (date)) and
(Customer_id (int), Name(String), Age (int), City (String)).
•   Insert or load the following data in the respective tables.
• Show number of orders belongs to the same customer id.
•   Find customer name and city who has order amount > 200 and order
after 2023-08-03
Customer_id Name   Age   City
1   Amit   23   Agra
2   Reena   65   Kota
Mumba
3   Shneha   23
i
4   Ritu   58   Delhi
5   Jeet   46   Bihar
Customer_
Order_id   Amount   Order_date
id
101   1   250.00   2023-08-01
102   2   150.00   2023-08-03
103   3   400.00   2023-08-05
104   1   300.00   2023-08-10
105   4   100.00   2023-08-15
106   5   200.00   2023-08-20
CO-2; BL-3   [10]
107   2   180.00   2023-08-25
Creating database and table – 3 Marks
Loading data and showing the output – 3 Marks
Group by with customer id and showing the output – 2 Marks
Finding common customer name and city and showing the output – 2
Marks
CREATE DATABASE Sales;
CREATE TABLE IF NOT EXISTS Order_Details (Order_id int,
Customer_id int, Amount int, Order_date date)
COMMENT ‘Order’
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ‘,’;
CREATE TABLE IF NOT EXISTS Customers (Customer_id int, Name
String, Age int, City String)
COMMENT ‘Customer_Details’
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ‘,’;
INSERT INTO Order_Details values (101,1,250,'2023-08-01');
OR
********** 8 **********
--- page 9 ---
LOAD DATA LOCAL INPATH ‘/home/hive/Order_Details.txt’ INTO
TABLE Order_Details;
Select * from Order_Details;
INSERT INTO Customers values (1,’Amit’,23,'Agra');
OR
LOAD DATA LOCAL INPATH ‘/home/hive/Customers.txt’ INTO
TABLE Customers;
Select * from Customers;
SELECT Count(Order_id) FROM Order_Details GROUP BY
Customer_id;
SELECT c.Name, c.City FROM Customers c JOIN Order_Details o
ON (c.Cutomer_id = o. Cutomer_id) WHERE Amount >200 AND
Order_date >2023-08-03 ;
a.   Explain the major challenges in big data visualization, including scalability, data
volume, velocity, variety, and data complexity. Suggest possible solutions to
overcome these challenges.
Big data visualization challenges with solution- each 2 marks
Scalability:
Challenge: Visualization tools and techniques need to scale effectively as the
size of the data grows.
Technique: Use scalable visualization frameworks and distributed computing
resources. Tools like D3.js and Apache Superset can handle large-scale
Q4   visualizations efficiently.
[10]
CO-1; BL-3
Data Volume:
•   Challenge: Handling and visualizing massive volumes of data
can lead to performance issues and make it difficult to extract
meaningful insights.
•   Technique: Use of sampling methods to represent a subset of
the data, or data reduction techniques like aggregation and
filtering to manage volume.
Data Variety:
•   Challenge: Big data comes in various formats (structured, semi-
structured, unstructured) and from different sources, which can
complicate integration and visualization.
********** 9 **********
--- page 10 ---
•   Technique: Employ data preprocessing techniques to normalize
and integrate diverse data sources, and use visualization tools
that support multiple data formats.
Data Velocity:
•   Challenge: The speed at which data is generated and needs to be
processed can be overwhelming, especially in real-time or near-
real-time applications.
•   Technique: Utilize stream processing and real-time analytics
platforms to handle and visualize live data.
Data Complexity:
Challenge: Complex datasets with multiple dimensions and relationships can be
difficult to represent clearly.
Technique: Apply dimensionality reduction techniques like Principal
Component Analysis (PCA) to simplify the data. Use advanced visualization
methods like multi-dimensional charts or interactive dashboards.
b.   Design the MapReduce architecture to count word occurrences from: “Machine
learning improves data analysis. Data analysis and machine learning are related”
Input: machine learning improves data analysis
data analysis and machine learning are related
Map Phase
Mapper Logic: Each word → (word,1)
(machine,1) (learning,1) (improves,1) (data,1) (analysis,1)
(data,1) (analysis,1) (and,1) (machine,1) (learning,1) (are,1) (related,1)
Shuffle and Sort Phase
Group same words together:
CO-1; BL-2   analysis → (1,1)   [10]
and → (1)
are → (1)
data → (1,1)
improves → (1)
learning → (1,1)
machine → (1,1)
related → (1)
Reduce Phase
Sum values for each word:
(analysis,2)
(and,1)
(are,1)
(data,2)
(improves,1)
********** 10 **********
--- page 11 ---
(learning,2)
(machine,2)
(related,1)
• Mapper: Converts each word into (word,1)
•   Shuffle & Sort: Groups identical words
•   Reducer: Aggregates counts
diagram -2 Mark
Map phase -3 Marks
Shuffle & Sort - 3 Marks
Reduce phase - 2 Marks
a.
Write commands for the following using Pig
• Create table Employee with (Id (int), Name (char array), Age
(int), Gender (char array), Salary (int)).
• Load the data into Employee. (Assume file and path)
• Gropy by the data with age and show the output
• Write a query using FILTER
• Write a query using FOREACH
• Write a query using STORE
Id   Name   Age   Gender   Salary
1201   Gopal   45   Male   50,000
1202   Manisha   40   Female   51,000
1203   Khalil   34   Male   30,000
1204   Prasanth   30   Male   30,000
1205   Kiran   20   Male   40,000
Q5
1206   Laxmi   25   Female   35,000   [10]
CO-2; BL-3
1207   Bhavya   20   Female   15,000
Creating and Load table – 2 Marks
Group by data – 2 Marks
Query using FILTER – 2 Marks
Query using FOREACH – 2 Marks
Query using STORE – 2 Marks
Employee = LOAD 'Pig_Data/employee_data.txt'
USING PigStorage(',') AS ( Id:int, Name:chararray, Age:int,
Gender:chararray, Salary:int);
STORE Employee INTO 'Pig_Output' USING PigStorage (',');
hdfs dfs -ls Pig_Output
hdfs dfs -cat pig_Output/part-m-00000
Group_data = GROUP Employee by Age;
********** 11 **********
--- page 12 ---
Dump Group_data;
Clean_data = FILTER Employee BY Id IS NOT NULL AND Name IS
NOT NULL;
Dump Clean_data;
Record_count = FOREACH (GROUP Clean_data ALL) GENERATE
COUNT(Clean_data);
Dump Record_data;
b.   Discuss various existing data visualization techniques such as bar charts, line
graphs, scatter plots, heatmaps, and dashboards. Compare their suitability for
different types of data.
Data visualization techniques are used to represent data graphically, making it
easier to understand trends, patterns, and relationships in big data analytics.
Types of Visualization Techniques
A. Bar Chart (2 Marks)
• Used to compare values across different categories.
•   Suitable for categorical data.
Example:
• Comparing sales of different products.
Best for discrete comparisons.
CO-1; BL-3   [10]
Line Graph (2 Marks)
• Shows trends over time.
•   Suitable for time-series data.
Example:
•   Stock prices over months.
Best for continuous data and trend analysis.
C. Scatter Plot (2 Marks)
•   Displays relationship between two variables.
•   Suitable for numerical data.
Example:
•   Height vs weight correlation.
Useful for identifying patterns and outliers.
D. Heatmap (2 Marks)
********** 12 **********
--- page 13 ---
• Uses color intensity to represent values.
•   Suitable for matrix or high-dimensional data.
Example:
•   Correlation matrix of variables.
Helps in spotting patterns quickly.
E. Dashboard (2 Marks)
• Combines multiple visualizations into a single interface.
•   Suitable for real-time monitoring and decision-making.
Example:
•   Business KPI dashboard.
Provides comprehensive insights.
a.   Explain classification and clustering with example.
Classification- 5 marks
Clustering- 5 marks
Classification
Classification is a supervised learning technique used to assign data into
predefined classes based on labeled training data.
Working:
• Model is trained on labeled dataset
•   Learns relationship between input and output
•   Predicts class label for new data
Q6
Example:   [10]
CO-2; BL-3
• Email classification: Spam or Not Spam
•   Student result: Pass or Fail
Algorithms Used:
•   Decision Tree
• Naïve Bayes
•   Support Vector Machine
Characteristics:
•   Requires labeled data
•   Predictive in nature
•   Output is discrete (categories)
Clustering
********** 13 **********
--- page 14 ---
Clustering is an unsupervised learning technique that groups similar data points
into clusters without predefined labels.
Working:
•   Finds similarity among data points
• Groups similar objects together
• No prior knowledge of classes
Example:
• Customer segmentation: grouping customers based on buying behavior
• Grouping news articles by topic
Algorithms Used:
• K-means
•   Hierarchical clustering
• DBSCAN
Characteristics:
• No labeled data required
•   Descriptive in nature
•   Output is clusters/groups
b.   Evaluate how spatial-temporal data analytics can improve intelligent
transportation systems, including real-time traffic monitoring and smart city
planning. Compare its performance with conventional statistical approaches.
Spatial-temporal data analytics combines location (spatial) and time-based
(temporal) information to analyze dynamic transportation systems. It plays a
crucial role in enhancing Intelligent Transportation Systems (ITS) and
enabling smart city development.
Role in Intelligent Transportation Systems (ITS)
1. Real-Time Traffic Monitoring
• Uses GPS, sensors, cameras, and mobile data
CO-1; BL-3   [10]
•   Provides live traffic updates (congestion, speed, incidents)
•   Enables dynamic route optimization and navigation
2. Traffic Prediction and Management
•   Analyzes historical + real-time data
•   Predicts traffic congestion and peak hours
•   Helps in adaptive traffic signal control
3. Accident Detection and Response
•   Detects anomalies in traffic patterns
•   Enables quick emergency response and rerouting
Role in Smart City Planning
********** 14 **********
--- page 15 ---
•   Helps in infrastructure planning (roads, flyovers, metro routes)
•   Supports public transport optimization
• Reduces pollution through efficient traffic flow
•   Assists in urban mobility planning and policy decisions
Advantages of Spatial-Temporal Analytics
•   Real-time decision making
•   High accuracy and predictive capability
•   Efficient traffic flow and reduced congestion
•   Better resource utilization
Comparison with Conventional Statistical Approaches
Aspect   Conventional Methods Spatial-Temporal Analytics
Data Type   Static, historical   Real-time + historical
Processing Periodic analysis   Continuous analysis
Accuracy   Moderate   High
Prediction Limited   Advanced predictive models
Adaptability Low   Dynamic and adaptive
introduction -2 Mark
Real-time traffic monitoring - 2 Marks
Traffic prediction / management - 2 Marks
Smart city planning - 2 Marks
Comparison with traditional methods -2 Marks
a.   Evaluate how Big Data is transforming the healthcare industry with respect to
clinical decision support systems, medical imaging analysis, and epidemic
outbreak prediction. Compare it with traditional healthcare data management
approaches.
Big Data is revolutionizing healthcare by enabling advanced analytics and
improving decision-making compared to traditional methods.
Q7
[10]
CO-1; BL-3   Key Transformations:
1. Clinical Decision Support Systems (CDSS)
o Provides data-driven recommendations to doctors
o Improves diagnosis accuracy
2. Medical Imaging Analysis
o Uses AI/ML for analyzing X-rays, MRI, CT scans
o Faster and more accurate detection
********** 15 **********
--- page 16 ---
3. Epidemic Outbreak Prediction
o Analyzes population data to predict disease spread
o Helps in early intervention and planning
Comparison with Traditional Systems:
Aspect   Traditional Approach Big Data Approach
Data Type   Limited, structured   Large, diverse (structured + unstructure
Processing   Manual / slow   Automated / real-time
Accuracy   Moderate   High
Decision Making Reactive   Predictive & proactive
Introduction - 2 Mark
CDSS explanation - 2 Marks
Medical imaging - 2 Marks
Epidemic prediction - 2 Marks
Comparison table - 2 Marks
b.   Discuss the challenges of imbalanced datasets. Explain techniques such as
oversampling, undersampling, SMOTE, and cost-sensitive learning with
examples.
Challenges of imbalanced datasets-4 marks
Techniques -6 marks
An imbalanced dataset is one where the number of instances in different classes
is unequal (e.g., 95% non-fraud and 5% fraud cases). This imbalance can bias
machine learning models toward the majority class.
Challenges of Imbalanced Datasets
CO-2; BL-2   [10]
1. Biased Predictions
• Models tend to favor the majority class.
•   Minority class is often ignored.
2. Accuracy Paradox
• High accuracy but poor performance on minority class.
• Example: 95% accuracy but no fraud detected.
3. Poor Generalization
• Model fails to learn patterns of minority class.
4. Evaluation Issues
• Accuracy is misleading; better metrics needed (precision, recall, F1-
score).
********** 16 **********
--- page 17 ---
Techniques to Handle Imbalanced Data
Oversampling
Description:
•   Increases the number of minority class instances by duplication.
Example:
•   Fraud cases increased from 100 → 500 by repeating samples.
Advantages:
• Improves minority class learning
Disadvantages:
•   Risk of overfitting
Undersampling
Description:
• Reduces the number of majority class samples.
Example:
• Reduce non-fraud cases from 10,000 → 1,000
Advantages:
•   Faster training
Disadvantages:
• Loss of important information
SMOTE (Synthetic Minority Over-sampling Technique)
Description:
•   Generates synthetic minority samples using nearest neighbors.
Example:
•   Creates new fraud cases based on existing ones instead of duplication.
Advantages:
• Reduces overfitting compared to oversampling
Disadvantages:
• May create noisy samples
Cost sensitive learning
Description:
•   Assigns higher cost to misclassifying minority class.
Example:
•   Misclassifying fraud is penalized more than non-fraud.
Advantages:
• Improves minority class detection
********** 17 **********
--- page 18 ---
FR ICR 7] QA HH
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 6716b1b27f44

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_DS_7052/Big Data Analytics/ANS_Big Data Analytics(702DB0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (18 pages), mean OCR confidence 39.1
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/MBA Tech (Comp)/MBA Tech (DS)
Year: III / IV/Semester VI/Semester VIII(Exam Year: 2025-2026)
Subject: Big Data Analytics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1
Answer briefly:   [20]
a.   Describe the role of HDFS in Big Data.
Five points each 1 mark.
1. Core Storage and Distributed Architecture
HDFS is the backbone of Hadoop’s storage, providing a way to store massive
amounts of data across a cluster of computers. Instead of relying on a single
large server, it uses a distributed architecture where data is spread across many
nodes, allowing the system to scale from a single server to thousands of
machines.
2. Data Partitioning (Block Storage)
HDFS manages large files by splitting them into smaller, fixed-size units called
blocks.
•   Size: Common block sizes are 128 MB (preferred) or 64 MB.
• Mechanism: For example, a 1 GB file is divided into 8 blocks of 128 MB,
which are then distributed across different machines in the cluster so
CO-1; BL-1   they can be read and processed simultaneously.   [5]
3. Fault Tolerance through Replication
In a Big Data environment using low-cost commodity hardware, machine
failures are common. HDFS ensures data reliability by automatically replicating
each block multiple times—usually 3 replicas—across different nodes. If one
node crashes, the system seamlessly retrieves the data from another node
containing a replica, preventing data loss.
4. High Throughput and Data Locality
HDFS is optimized for batch processing rather than interactive user tasks,
providing high-throughput access to application data. A critical role it plays is
enabling Data Locality: instead of moving massive datasets over the network to
a program, Hadoop moves the processing program to the data stored on the
HDFS nodes. This significantly reduces network traffic and increases processing
speed.
5. Cost-Effectiveness and Management
********** 1 **********
--- page 2 ---
HDFS allows organizations to store Big Data cheaply by running on low-cost,
commodity hardware. It sits on top of local file systems and provides a suite of
HDFS Commands (like put, get, ls, and mkdir) to manage, monitor, and check
the health of the distributed files.
b.   Describe the working of NameNode and DataNode in HDFS.
Working of namenode- 3 marks
Working of datanode- 2 marks
In the Hadoop Distributed File System (HDFS), the architecture follows a
master-slave model where the NameNode acts as the master and DataNodes
act as slaves to manage storage across a cluster.
1. Working of the NameNode (Master)
The NameNode is the "brain" of the HDFS and is responsible for managing the
file system's metadata and governing access.
• Namespace Management: It maintains the hierarchical structure of
files and directories, similar to a Linux file system.
• Metadata Storage: It stores information about the files, such as their
size, permissions, and, most importantly, the mapping of file blocks to
specific DataNodes.
•   Access Control: It regulates client access to files and handles requests
to open, close, rename, or delete files and directories.
• Request Validation: When a client wants to write data, the NameNode
checks for permissions and ensures the file does not already exist
before providing a list of suitable DataNodes for storage.
2. Working of the DataNode (Slave)
CO-3; BL-2   DataNodes are the worker nodes that perform the actual task of storing and   [5]
retrieving data blocks.
•   Block Storage: They store data in fixed-size units called blocks (typically
128MB or 256MB).
• Data Operations: They handle read and write requests from HDFS
clients and perform block creation, deletion, and replication as
instructed by the NameNode.
•   Replication Pipeline: During a write operation, DataNodes work in a
pipeline. DataNode 1 receives data from the client, stores it, and
forwards it to DataNode 2, which then forwards it to DataNode 3 (based
on the replication factor).
• Data Integrity: Each DataNode is responsible for verifying the integrity
of its stored data using checksums during read/write operations to
detect any corruption.
3. Interaction Between NameNode and DataNode
The interaction ensures the system remains reliable and efficient:
• Write Coordination: The NameNode provides the client with the
locations (IP addresses) of DataNodes. The client then streams data
directly to those DataNodes to avoid bottlenecking the NameNode.
• Acknowledgment: Once DataNodes successfully store a block, they
send an acknowledgment (ACK) back through the pipeline to the client,
which then informs the NameNode to finalize the metadata.
********** 2 **********
--- page 3 ---
Fault Tolerance: If a DataNode or a block fails, the NameNode detects this and
coordinates with other DataNodes to create new replicas from healthy copies,
ensuring high availability
c.   Define execution modes used in Apache Pig. Compare Pig with MapReduce.
Execution mode [2 Marks]
Comparison between Pig and MapReduce [3 Marks]
Apache Pig Execution Modes
Local Mode
•   In this mode, all the files are installed and run from your local
host and local file system. There is no need of Hadoop or HDFS.
This mode is generally used for testing purpose.
MapReduce Mode
• MapReduce mode is where we load or process the data that exists
in the Hadoop File System (HDFS) using Apache Pig. In this
mode, whenever we execute the Pig Latin statements to process
the data, a MapReduce job is invoked in the back-end to perform
a particular operation on the data that exists in the HDFS.
Difference between Pig and MapReduce
Apache Pig   MapReduce
It is a compiled
It is a scripting language.   programming
CO-2; BL-3   language.   [5]
Abstraction is at higher   Abstraction is at
level.   lower level.
It have less line of code as
Lines of code is more.
compared to MapReduce.
More development
Less effort is needed for
efforts are required
Apache Pig.
for MapReduce.
As compared to Pig
Code efficiency is less as
efficiency of code is
compared to MapReduce.
higher.
Pig provides built in
Hard to perform data
functions for ordering,
operations.
sorting and union.
********** 3 **********
--- page 4 ---
It allows nested data types   It does not allow
like map, tuple and bag   nested data types
d.   What is cosine similarity in recommendation systems?
Cosine similarity is a measure used in recommendation systems to determine
how similar two users or items are by comparing their rating vectors. It
calculates the cosine of the angle between two vectors.
𝐴⋅𝐵
Cosine Similarity =
∥𝐴∥×∥𝐵∥
Where:
• 𝐴⋅𝐵= dot product of vectors
• ∥𝐴∥, ∥𝐵∥= magnitudes of vectors
Working
Represent users/items as vectors of ratings
CO-2; BL-2   • Compute similarity between vectors   [5]
• Value ranges from 0 to 1:
o 1 → very similar
o 0 → not similar
Example
User A = [5, 4, 0]
User B = [4, 5, 0]
•   Cosine similarity will be high, indicating similar preferences
Used to recommend items liked by similar users.
Applications
•   Collaborative filtering
• Movie and product recommendation systems
a.   Describe data ingestion process using Flume and Sqoop.
Q2
[10]
CO-3; BL-1   Data ingestion with flume and sqoop each 5 marks
********** 4 **********
--- page 5 ---
Data ingestion in Hadoop is the process of collecting data from various sources
(like logs, databases, or sensors) and moving it into a central system like HDFS
for processing and analysis. The specific steps for the two primary tools, Sqoop
and Flume, are as follows:
1. Data Ingestion with Apache Sqoop (Batch/Structured Data)
Sqoop is designed to transfer structured data between Relational Database
Management Systems (RDBMS) and HDFS.
Steps in the Sqoop Workflow:
1. Command Submission: The user issues a Sqoop import or export
command via the client terminal.
2. Job Translation: Sqoop converts the command into a MapReduce job
to enable large-scale parallel data transfer.
3. Framework Trigger: The MapReduce job is submitted to the Hadoop
cluster.
4. Establish Connection: Sqoop uses JDBC to establish a secure
connection with the source RDBMS (e.g., MySQL or Oracle).
5. Data Splitting: The database table is divided into logical "splits" based
on a primary key or specific column.
6. Parallel Transfer: Multiple Mappers (default is 4) independently and
simultaneously pull or push their assigned chunks of data.
7. HDFS Writing/Reading: During an import, the mappers write the data
into HDFS in formats such as text, Avro, or sequence files.
8. Job Completion: Once all mappers finish, Sqoop reports the final status
(success or failure) to the client.
Example: Transferring customer transaction tables from a MySQL database
into an HDFS directory for monthly batch reporting.
2. Data Ingestion with Apache Flume (Streaming/Semi-Structured Data)
Flume is optimized for the continuous collection and movement of log and
event data.
Steps in the Flume Workflow:
1. Event Generation: An external source, such as a web server, produces
a "Flume Event" (a byte array payload with optional headers).
2. Source Reception: The Flume Source component receives these events
from the generator over the network.
3. Channel Buffering: The Source sends the event to a Flume Channel,
which acts as a temporary buffer or store (often using the local file
system for reliability).
4. Sink Extraction: The Flume Sink removes the event from the channel.
5. Centralized Storage: The Sink writes the event to a centralized
repository like HDFS or Apache HBase. In complex setups, the Sink may
forward the event to the Source of another agent in a "multi-hop" flow.
Example: An e-commerce website (like Amazon) streaming live web server logs
into HDFS to perform real-time analysis of customer behavior in a specific
geographic region.
********** 5 **********
--- page 6 ---
b.   Explain user-based and item-based collaborative filtering techniques. Compare
their advantages, limitations, and applications in recommendation systems.
User based and item based collaborative filtering- each 4 marks
Comparison- 2 marks
Collaborative Filtering (CF) is a recommendation technique that predicts user
preferences based on past behavior. It is widely used in systems like Netflix and
Amazon.
Two main approaches are User-Based and Item-Based Collaborative
Filtering.
User-Based Collaborative Filtering
•   Finds users with similar preferences using similarity measures (e.g.,
cosine similarity).
• Recommends items liked by similar users.
Example:
•   If User A and User B have similar movie ratings, and User B likes Movie
X, then Movie X is recommended to User A.
CO-2; BL-2   Advantages:   [10]
• Simple and intuitive
•   Personalized recommendations
Limitations:
• Not scalable for large datasets
•   Suffers from sparsity (few common ratings)
Item-Based Collaborative Filtering
Working Principle:
•   Finds similarity between items instead of users.
• Recommends items similar to those the user has liked.
Example:
•   If a user likes Movie A and Movie A is similar to Movie B, then Movie
B is recommended.
Advantages:
• More scalable and efficient
•   Stable recommendations over time
Limitations:
•   Less personalized than user-based
•   Requires computation of item similarity
********** 6 **********
--- page 7 ---
a.   Draw and explain Hadoop architecture. What are the additional benefits that
YARN brings into Hadoop?
•   Architecture diagram → 2 Marks
• HDFS explanation → 4 Marks
• YARN explanation → 2 Marks
•   Benefits of YARN → 2 Marks
HDFS (Storage Layer)
Components:
• NameNode (Master): Stores metadata (file names, block locations),
Manages file system operations
• DataNode (Slave): Stores actual data blocks, Performs read/write
operations
Key Features:
Data is split into blocks and distributed across nodes
Replication ensures fault tolerance
High scalability and reliability
YARN (Processing Layer)
Components:
• ResourceManager (Master): Allocates cluster resources, Manages
Q3   scheduling
• NodeManager (Slave): Manages resources on each node, Executes   [10]
CO-1; BL-2
tasks
•   ApplicationMaster: Manages a specific application/job, Negotiates
resources from ResourceManager
MapReduce (Processing Model)
Divides job into:
Map tasks → Process input data
Reduce tasks → Aggregate results
Runs on top of YARN for distributed processing
Additional Benefits of YARN in Hadoop
•   Better Resource Management
Separates resource management from job scheduling
Efficient utilization of cluster resources
•   Scalability
Supports large clusters (thousands of nodes)
Handles multiple applications simultaneously
• Improved Performance
Parallel execution of multiple jobs
Reduces bottlenecks of JobTracker (in Hadoop 1.x)
•   Fault Tolerance
Automatically restarts failed tasks
Ensures continuous execution
• Dynamic Resource Allocation
Allocates resources based on demand
Supports container-based execution
********** 7 **********
--- page 8 ---
b.
Write commands and outputs for the following using Hive
•   Create database ‘Sales’ and table ‘Order_Details’and Customer with
(Order_id (int), Customer_id (int), Amount (int), Order_date (date)) and
(Customer_id (int), Name(String), Age (int), City (String)).
•   Insert or load the following data in the respective tables.
• Show number of orders belongs to the same customer id.
•   Find customer name and city who has order amount > 200 and order
after 2023-08-03
Customer_id Name   Age   City
1   Amit   23   Agra
2   Reena   65   Kota
Mumba
3   Shneha   23
i
4   Ritu   58   Delhi
5   Jeet   46   Bihar
Customer_
Order_id   Amount   Order_date
id
101   1   250.00   2023-08-01
102   2   150.00   2023-08-03
103   3   400.00   2023-08-05
104   1   300.00   2023-08-10
105   4   100.00   2023-08-15
106   5   200.00   2023-08-20
CO-2; BL-3   [10]
107   2   180.00   2023-08-25
Creating database and table – 3 Marks
Loading data and showing the output – 3 Marks
Group by with customer id and showing the output – 2 Marks
Finding common customer name and city and showing the output – 2
Marks
CREATE DATABASE Sales;
CREATE TABLE IF NOT EXISTS Order_Details (Order_id int,
Customer_id int, Amount int, Order_date date)
COMMENT ‘Order’
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ‘,’;
CREATE TABLE IF NOT EXISTS Customers (Customer_id int, Name
String, Age int, City String)
COMMENT ‘Customer_Details’
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ‘,’;
INSERT INTO Order_Details values (101,1,250,'2023-08-01');
OR
********** 8 **********
--- page 9 ---
LOAD DATA LOCAL INPATH ‘/home/hive/Order_Details.txt’ INTO
TABLE Order_Details;
Select * from Order_Details;
INSERT INTO Customers values (1,’Amit’,23,'Agra');
OR
LOAD DATA LOCAL INPATH ‘/home/hive/Customers.txt’ INTO
TABLE Customers;
Select * from Customers;
SELECT Count(Order_id) FROM Order_Details GROUP BY
Customer_id;
SELECT c.Name, c.City FROM Customers c JOIN Order_Details o
ON (c.Cutomer_id = o. Cutomer_id) WHERE Amount >200 AND
Order_date >2023-08-03 ;
a.   Explain the major challenges in big data visualization, including scalability, data
volume, velocity, variety, and data complexity. Suggest possible solutions to
overcome these challenges.
Big data visualization challenges with solution- each 2 marks
Scalability:
Challenge: Visualization tools and techniques need to scale effectively as the
size of the data grows.
Technique: Use scalable visualization frameworks and distributed computing
resources. Tools like D3.js and Apache Superset can handle large-scale
Q4   visualizations efficiently.
[10]
CO-1; BL-3
Data Volume:
•   Challenge: Handling and visualizing massive volumes of data
can lead to performance issues and make it difficult to extract
meaningful insights.
•   Technique: Use of sampling methods to represent a subset of
the data, or data reduction techniques like aggregation and
filtering to manage volume.
Data Variety:
•   Challenge: Big data comes in various formats (structured, semi-
structured, unstructured) and from different sources, which can
complicate integration and visualization.
********** 9 **********
--- page 10 ---
•   Technique: Employ data preprocessing techniques to normalize
and integrate diverse data sources, and use visualization tools
that support multiple data formats.
Data Velocity:
•   Challenge: The speed at which data is generated and needs to be
processed can be overwhelming, especially in real-time or near-
real-time applications.
•   Technique: Utilize stream processing and real-time analytics
platforms to handle and visualize live data.
Data Complexity:
Challenge: Complex datasets with multiple dimensions and relationships can be
difficult to represent clearly.
Technique: Apply dimensionality reduction techniques like Principal
Component Analysis (PCA) to simplify the data. Use advanced visualization
methods like multi-dimensional charts or interactive dashboards.
b.   Design the MapReduce architecture to count word occurrences from: “Machine
learning improves data analysis. Data analysis and machine learning are related”
Input: machine learning improves data analysis
data analysis and machine learning are related
Map Phase
Mapper Logic: Each word → (word,1)
(machine,1) (learning,1) (improves,1) (data,1) (analysis,1)
(data,1) (analysis,1) (and,1) (machine,1) (learning,1) (are,1) (related,1)
Shuffle and Sort Phase
Group same words together:
CO-1; BL-2   analysis → (1,1)   [10]
and → (1)
are → (1)
data → (1,1)
improves → (1)
learning → (1,1)
machine → (1,1)
related → (1)
Reduce Phase
Sum values for each word:
(analysis,2)
(and,1)
(are,1)
(data,2)
(improves,1)
********** 10 **********
--- page 11 ---
(learning,2)
(machine,2)
(related,1)
• Mapper: Converts each word into (word,1)
•   Shuffle & Sort: Groups identical words
•   Reducer: Aggregates counts
diagram -2 Mark
Map phase -3 Marks
Shuffle & Sort - 3 Marks
Reduce phase - 2 Marks
a.
Write commands for the following using Pig
• Create table Employee with (Id (int), Name (char array), Age
(int), Gender (char array), Salary (int)).
• Load the data into Employee. (Assume file and path)
• Gropy by the data with age and show the output
• Write a query using FILTER
• Write a query using FOREACH
• Write a query using STORE
Id   Name   Age   Gender   Salary
1201   Gopal   45   Male   50,000
1202   Manisha   40   Female   51,000
1203   Khalil   34   Male   30,000
1204   Prasanth   30   Male   30,000
1205   Kiran   20   Male   40,000
Q5
1206   Laxmi   25   Female   35,000   [10]
CO-2; BL-3
1207   Bhavya   20   Female   15,000
Creating and Load table – 2 Marks
Group by data – 2 Marks
Query using FILTER – 2 Marks
Query using FOREACH – 2 Marks
Query using STORE – 2 Marks
Employee = LOAD 'Pig_Data/employee_data.txt'
USING PigStorage(',') AS ( Id:int, Name:chararray, Age:int,
Gender:chararray, Salary:int);
STORE Employee INTO 'Pig_Output' USING PigStorage (',');
hdfs dfs -ls Pig_Output
hdfs dfs -cat pig_Output/part-m-00000
Group_data = GROUP Employee by Age;
********** 11 **********
--- page 12 ---
Dump Group_data;
Clean_data = FILTER Employee BY Id IS NOT NULL AND Name IS
NOT NULL;
Dump Clean_data;
Record_count = FOREACH (GROUP Clean_data ALL) GENERATE
COUNT(Clean_data);
Dump Record_data;
b.   Discuss various existing data visualization techniques such as bar charts, line
graphs, scatter plots, heatmaps, and dashboards. Compare their suitability for
different types of data.
Data visualization techniques are used to represent data graphically, making it
easier to understand trends, patterns, and relationships in big data analytics.
Types of Visualization Techniques
A. Bar Chart (2 Marks)
• Used to compare values across different categories.
•   Suitable for categorical data.
Example:
• Comparing sales of different products.
Best for discrete comparisons.
CO-1; BL-3   [10]
Line Graph (2 Marks)
• Shows trends over time.
•   Suitable for time-series data.
Example:
•   Stock prices over months.
Best for continuous data and trend analysis.
C. Scatter Plot (2 Marks)
•   Displays relationship between two variables.
•   Suitable for numerical data.
Example:
•   Height vs weight correlation.
Useful for identifying patterns and outliers.
D. Heatmap (2 Marks)
********** 12 **********
--- page 13 ---
• Uses color intensity to represent values.
•   Suitable for matrix or high-dimensional data.
Example:
•   Correlation matrix of variables.
Helps in spotting patterns quickly.
E. Dashboard (2 Marks)
• Combines multiple visualizations into a single interface.
•   Suitable for real-time monitoring and decision-making.
Example:
•   Business KPI dashboard.
Provides comprehensive insights.
a.   Explain classification and clustering with example.
Classification- 5 marks
Clustering- 5 marks
Classification
Classification is a supervised learning technique used to assign data into
predefined classes based on labeled training data.
Working:
• Model is trained on labeled dataset
•   Learns relationship between input and output
•   Predicts class label for new data
Q6
Example:   [10]
CO-2; BL-3
• Email classification: Spam or Not Spam
•   Student result: Pass or Fail
Algorithms Used:
•   Decision Tree
• Naïve Bayes
•   Support Vector Machine
Characteristics:
•   Requires labeled data
•   Predictive in nature
•   Output is discrete (categories)
Clustering
********** 13 **********
--- page 14 ---
Clustering is an unsupervised learning technique that groups similar data points
into clusters without predefined labels.
Working:
•   Finds similarity among data points
• Groups similar objects together
• No prior knowledge of classes
Example:
• Customer segmentation: grouping customers based on buying behavior
• Grouping news articles by topic
Algorithms Used:
• K-means
•   Hierarchical clustering
• DBSCAN
Characteristics:
• No labeled data required
•   Descriptive in nature
•   Output is clusters/groups
b.   Evaluate how spatial-temporal data analytics can improve intelligent
transportation systems, including real-time traffic monitoring and smart city
planning. Compare its performance with conventional statistical approaches.
Spatial-temporal data analytics combines location (spatial) and time-based
(temporal) information to analyze dynamic transportation systems. It plays a
crucial role in enhancing Intelligent Transportation Systems (ITS) and
enabling smart city development.
Role in Intelligent Transportation Systems (ITS)
1. Real-Time Traffic Monitoring
• Uses GPS, sensors, cameras, and mobile data
CO-1; BL-3   [10]
•   Provides live traffic updates (congestion, speed, incidents)
•   Enables dynamic route optimization and navigation
2. Traffic Prediction and Management
•   Analyzes historical + real-time data
•   Predicts traffic congestion and peak hours
•   Helps in adaptive traffic signal control
3. Accident Detection and Response
•   Detects anomalies in traffic patterns
•   Enables quick emergency response and rerouting
Role in Smart City Planning
********** 14 **********
--- page 15 ---
•   Helps in infrastructure planning (roads, flyovers, metro routes)
•   Supports public transport optimization
• Reduces pollution through efficient traffic flow
•   Assists in urban mobility planning and policy decisions
Advantages of Spatial-Temporal Analytics
•   Real-time decision making
•   High accuracy and predictive capability
•   Efficient traffic flow and reduced congestion
•   Better resource utilization
Comparison with Conventional Statistical Approaches
Aspect   Conventional Methods Spatial-Temporal Analytics
Data Type   Static, historical   Real-time + historical
Processing Periodic analysis   Continuous analysis
Accuracy   Moderate   High
Prediction Limited   Advanced predictive models
Adaptability Low   Dynamic and adaptive
introduction -2 Mark
Real-time traffic monitoring - 2 Marks
Traffic prediction / management - 2 Marks
Smart city planning - 2 Marks
Comparison with traditional methods -2 Marks
a.   Evaluate how Big Data is transforming the healthcare industry with respect to
clinical decision support systems, medical imaging analysis, and epidemic
outbreak prediction. Compare it with traditional healthcare data management
approaches.
Big Data is revolutionizing healthcare by enabling advanced analytics and
improving decision-making compared to traditional methods.
Q7
[10]
CO-1; BL-3   Key Transformations:
1. Clinical Decision Support Systems (CDSS)
o Provides data-driven recommendations to doctors
o Improves diagnosis accuracy
2. Medical Imaging Analysis
o Uses AI/ML for analyzing X-rays, MRI, CT scans
o Faster and more accurate detection
********** 15 **********
--- page 16 ---
3. Epidemic Outbreak Prediction
o Analyzes population data to predict disease spread
o Helps in early intervention and planning
Comparison with Traditional Systems:
Aspect   Traditional Approach Big Data Approach
Data Type   Limited, structured   Large, diverse (structured + unstructure
Processing   Manual / slow   Automated / real-time
Accuracy   Moderate   High
Decision Making Reactive   Predictive & proactive
Introduction - 2 Mark
CDSS explanation - 2 Marks
Medical imaging - 2 Marks
Epidemic prediction - 2 Marks
Comparison table - 2 Marks
b.   Discuss the challenges of imbalanced datasets. Explain techniques such as
oversampling, undersampling, SMOTE, and cost-sensitive learning with
examples.
Challenges of imbalanced datasets-4 marks
Techniques -6 marks
An imbalanced dataset is one where the number of instances in different classes
is unequal (e.g., 95% non-fraud and 5% fraud cases). This imbalance can bias
machine learning models toward the majority class.
Challenges of Imbalanced Datasets
CO-2; BL-2   [10]
1. Biased Predictions
• Models tend to favor the majority class.
•   Minority class is often ignored.
2. Accuracy Paradox
• High accuracy but poor performance on minority class.
• Example: 95% accuracy but no fraud detected.
3. Poor Generalization
• Model fails to learn patterns of minority class.
4. Evaluation Issues
• Accuracy is misleading; better metrics needed (precision, recall, F1-
score).
********** 16 **********
--- page 17 ---
Techniques to Handle Imbalanced Data
Oversampling
Description:
•   Increases the number of minority class instances by duplication.
Example:
•   Fraud cases increased from 100 → 500 by repeating samples.
Advantages:
• Improves minority class learning
Disadvantages:
•   Risk of overfitting
Undersampling
Description:
• Reduces the number of majority class samples.
Example:
• Reduce non-fraud cases from 10,000 → 1,000
Advantages:
•   Faster training
Disadvantages:
• Loss of important information
SMOTE (Synthetic Minority Over-sampling Technique)
Description:
•   Generates synthetic minority samples using nearest neighbors.
Example:
•   Creates new fraud cases based on existing ones instead of duplication.
Advantages:
• Reduces overfitting compared to oversampling
Disadvantages:
• May create noisy samples
Cost sensitive learning
Description:
•   Assigns higher cost to misclassifying minority class.
Example:
•   Misclassifying fraud is penalized more than non-fraud.
Advantages:
• Improves minority class detection
********** 17 **********
--- page 18 ---
FR ICR 7] QA HH
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 898eed67b31f

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AI_7012/Big Data Analytics/ANS_Big Data Analytics(702DB0C029)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05/12/ 2025
- Text: text (17 pages)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
Programs: B Tech, BTI, MBA Tech   Year: IV/VI Semester: VII/ XI
Streams: B Tech CS, DS, CSEDS, AI, BTI CS, AI
Subject: Big Data Analytics   Time: 3 hrs. (02:00pm to 05:00pm)
Date:05/12/ 2025   No. of Pages: 3
Marks: 100
Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Q1
Answer briefly:
A city government collects data from traffic sensors, CCTV cameras, public transport
systems, and   social media   to monitor   traffic flow and   public   safety.
Identify the types of Big Data characteristics in this scenario. Explain how Big Data
Analytics can help improve city planning and reduce congestion.
Big Data Characteristics in the Scenario (2 marks)
The data collected by the city exhibits the 3 Vs of Big Data:
Characteristic   Explanation / Example
Volume   Large amounts of data from traffic sensors, CCTV cameras, and soci
Data is generated and transmitted in real-time (e.g., live traffi
Velocity
updates).
CO- 1; SO- 2; BL-2   Different types of data: structured (sensor readings, transport sch
Variety
structured (logs, JSON from apps), unstructured (videos, social med
Veracity   (optional
Data may contain noise, errors, or inconsistencies from multiple sou
bonus)
Value   Insights can be extracted to improve traffic management and city pla
2. How Big Data Analytics Helps Improve City Planning & Reduce Congestion (3
marks)
1. Traffic Flow Optimization:
o Analyze real-time traffic sensor and CCTV data to detect congestion
[5]
a   points.
--- page 2 ---
o Adjust traffic signals dynamically to reduce bottlenecks.
2. Public Transport Planning:
o Use smart card, GPS, and passenger data to optimize bus and train routes.
o   Identify high-demand areas and adjust schedules.
3. Predictive Analytics:
o   Forecast traffic patterns during peak hours or events using historical data.
o   Proactively manage road closures, detours, and public warnings.
4. Safety & Incident Management:
o   Detect accidents or unusual events from CCTV and social media reports.
o Dispatch emergency services quickly to minimize disruption.
5. Urban Planning Insights:
o Use aggregated data to design new roads, pedestrian zones, or bike lanes.
o Improve long-term infrastructure planning based on actual usage patterns.
Discuss Data Node and Name Node in HDFS.
Introduction to HDFS
HDFS (Hadoop Distributed File System) is the primary storage system of Hadoop.
It follows a Master-Slave architecture:
• Master Node: NameNode
•   Slave Nodes: DataNodes
HDFS stores large files by splitting them into blocks (default 128 MB) and distributing
them across multiple nodes for reliability and scalability.
2. NameNode (Master Node) 2.5 marks
Role: The NameNode is the central controller of HDFS.
Responsibilities:
1. Maintains the metadata of the file system:
o   File names, file permissions
o   Directory structure
o Mapping of blocks to DataNodes
2. Manages namespace operations:
o   Create, delete, rename files/directories
CO-1; SO-2; BL-2   3. Monitors DataNode health via periodic heartbeats.
4. Handles replication:
o Ensures each block is replicated across multiple DataNodes (default 3) for
fault tolerance.
5. Does not store actual data — only metadata.
Important Note: If the NameNode fails, HDFS becomes unavailable unless a Secondary
NameNode or High-Availability setup is used.
3. DataNode (Slave Node)2.5 marks
Role: DataNodes are the storage units of HDFS.
Responsibilities:
1. Store actual data blocks on local disk.
2. Serve read/write requests from clients.
3. Periodically send block reports and heartbeats to the NameNode.
4. Manage replication at the block level (create/delete blocks as instructed by
NameNode).
5. Ensure data durability and availability.
Features:
[5]
b   • Runs on commodity hardware.
--- page 3 ---
• Can be added or removed easily for scalability.
What is the purpose of a Combiner in MapReduce? How does it help optimize
performance? Give an example to illustrate its use.
1. Purpose of a Combiner (2 marks)
• A Combiner is an optional mini-reducer in MapReduce.
•   It aggregates intermediate key-value pairs generated by the Mapper before
sending them to the Reducer.
•   Helps reduce the volume of data transferred over the network (shuffle phase).
Key Point: Combiner does local aggregation on Mapper nodes to optimize performance
but does not guarantee final results (Reducer still does the actual computation).
2. How it Optimizes Performance (2 marks)
• Reduces network I/O: Fewer intermediate key-value pairs are sent from Mappers
to Reducers.
• Speeds up processing: Less data for Reducers to handle.
•   Particularly useful for commutative and associative operations (e.g., sum,
CO- 2; SO-2 ; BL-2   count, max).
3. Example: Word Count(1mark)
Scenario: Counting words in a large text file.
Mapper Output (Intermediate Pairs):
Mapper1: ("data",1), ("science",1), ("data",1)
Mapper2: ("science",1), ("big",1), ("data",1)
Without Combiner:
All intermediate pairs sent to Reducer:
[("data",1), ("science",1), ("data",1), ("science",1), ("big",1), ("data",1)]
With Combiner (local aggregation at Mapper):
Mapper1 Combiner: ("data",2), ("science",1)
Mapper2 Combiner: ("science",1), ("big",1), ("data",1)
• Fewer key-value pairs are sent over the network → less shuffle data → faster
processing.
[5]
c
Explain the major issues that impact the effectiveness of Big Data visualization. (any 5
points 5 marks)
Introduction
Big Data visualization helps in understanding patterns and insights from massive, complex
datasets. However, its effectiveness can be limited by several issues.
2. Major Issues
1. Volume of Data
o Extremely large datasets can overwhelm visualization tools.
CO- 3; SO- 3; BL-2
o Rendering millions of data points can cause performance lags or
crashes.
2. Variety of Data
o Data comes in multiple formats: structured, semi-structured, unstructured.
o   Integrating heterogeneous data into a coherent visualization   is
challenging.
3. Velocity of Data
o Real-time data streams (e.g., IoT sensors, social media) require dynamic
[5]
d   and continuous updates.
--- page 4 ---
o Lag or outdated visuals reduce decision-making effectiveness.
4. Data Quality (Veracity)
o   Inaccurate, incomplete, or noisy data can mislead visual interpretations.
o Requires preprocessing, cleaning, and validation before visualization.
5. Complexity of Analysis
o High-dimensional or multi-variate data can be difficult to represent in
simple charts.
o May require advanced visualization techniques (heatmaps, 3D plots,
dashboards).
6. Scalability of Tools
o Not all visualization tools can handle Big Data efficiently.
o Tools need to scale horizontally or use techniques like sampling or
aggregation.
7. Interpretability
o Overly complex or cluttered visuals can confuse users.
o Choosing the right type of chart/graph is critical for clarity.
An online education platform wants to recommend courses to students based on their
course completion and ratings.
i. Explain how collaborative filtering can help suggest courses to a student.
ii. If two students have rated the same courses similarly, what does high cosine similarity
imply?
iii. Suggest a strategy to recommend courses to a new student with no ratings.
Collaborative Filtering for Course Recommendations (4 marks)
Definition:
•   Collaborative Filtering (CF) is a technique to suggest items (courses) to a user
based on the preferences of other similar users.
• Assumes that students who agreed in the past will agree in the future.
How it works:
1. Collect ratings of courses by all students.
2. Compute similarity between students (user-based CF) or between courses (item-
based CF).
3. Recommend courses that similar students liked but the target student hasn’t
Q2   taken.
CO-3; SO-1; BL-1   Example:
•   Student A rated courses [X=5, Y=4].
•   Student B rated courses [X=5, Y=4, Z=5].
• CF recommends course Z to Student A because Student B with similar ratings
liked it.
ii. High Cosine Similarity Between Two Students (2 marks)
•   Cosine similarity measures the angle between two students’ rating vectors.
• High cosine similarity implies:
1. Students’ ratings across courses are very similar.
2. Their preferences align closely.
3. Courses liked by one student are likely to be relevant to the other.
Example:
•   Student A vector: [5,4,0]
•   Student B vector: [5,4,5]
•   Cosine similarity ≈ 0.99 → strong alignment → CF recommends Student B’s
[10]
a   liked course (Z) to Student A.
--- page 5 ---
iii. Strategy for New Student (Cold Start Problem) (4 marks)
Problem: New students have no prior ratings, so CF cannot be applied.
Strategies:
1. Content-Based Filtering:
o Recommend courses based on the student’s profile: interests, skills, or
demographic data.
o Example: Student interested in “Data Science” → recommend courses in
Python, Machine Learning, etc.
2. Popularity-Based Recommendations:
o Suggest top-rated or most-enrolled courses across the platform.
3. Hybrid Approach:
o Combine content-based and collaborative filtering after initial course
completions/ratings.
4. Onboarding Surveys / Quick Assessment:
o Ask the student to rate a few courses or topics during signup to generate
initial recommendations.
Elaborate at least five file formats in HDFS.( 5 file formats , 2 marks each)
Introduction
HDFS (Hadoop Distributed File System) supports multiple file formats, optimized for
storage, processing, and analytics. The choice of format affects read/write
performance, compression, and compatibility with tools like MapReduce, Hive, and
Spark.
1. Text File (TXT / CSV)
•   Description: Plain-text file format; each line is a record, fields separated by
delimiters (comma, tab).
•   Advantages:
o Easy to read and debug.
CO-1,; SO-; BL-   o Compatible with most tools.
•   Disadvantages:
o No schema; parsing large datasets is inefficient.
• Use Case: Small datasets, log files, or data exchange between systems.
2. Sequence File
•   Description: Binary key-value format used internally by Hadoop. Stores data as
<key, value> pairs.
•   Advantages:
o Optimized for MapReduce processing.
o Supports splitting, enabling parallel processing.
•   Disadvantages:
[10]
b   o Not human-readable.
--- page 6 ---
• Use Case: Intermediate storage for Mapper output, or bulk storage of structured
data.
3. Avro
•   Description: Row-based binary format with schema stored in JSON. Supports
schema evolution.
•   Advantages:
o Compact and fast serialization/deserialization.
o Schema evolution allows adding/removing fields without breaking
applications.
•   Disadvantages:
o Less efficient for analytical queries that need only a few columns.
• Use Case: Streaming data, data exchange between systems, and records requiring
schema evolution.
4. Parquet
•   Description: Columnar storage format designed for analytical workloads. Stores
data column-wise, rather than row-wise.
•   Advantages:
o   Efficient for read-heavy queries.
o   Better compression and reduced I/O for selected columns.
o Supports complex nested data types.
•   Disadvantages:
o Row-wise inserts/updates are less efficient.
• Use Case: Data warehouses, Hive/Spark SQL analytics, OLAP workloads.
5. ORC (Optimized Row Columnar)
•   Description: Columnar format optimized for Hive.
•   Advantages:
o High compression (ZLIB/Snappy).
o   Fast query execution with predicate pushdown.
o   Efficient for large-scale analytical queries.
•   Disadvantages:
o Not ideal for frequent row-level updates.
• Use Case: Hive tables, large-scale analytics, queries with selective columns.
6. JSON
•   Description: Semi-structured text format using key-value pairs, often nested.
•   Advantages:
o Human-readable and widely used for APIs.
o Supports nested and hierarchical data.
•   Disadvantages:
o Larger file size, slower processing compared to binary formats.
• Use Case: Web logs, API data ingestion, semi-structured datasets.
7. XML
•   Description: Semi-structured markup language format.
•   Advantages:
o Supports hierarchical data.
o   Standardized and self-descriptive.
•   Disadvantages:
--- page 7 ---
o Verbose, high storage overhead, slower parsing.
• Use Case: Legacy data exchange, configuration files.
Consider the following dataset :
101 Anjali HR 22
102 Ramesh IT 18
103 Meera Finance 25
104 Tarun IT 20
105 Kavita HR 19
106 Suresh Finance 23
107 Nisha IT 26
Each record represents:
· Employee ID
· Name
· Department
· Days Present (in a month)
Create a PIG script to process the attendance.txt file and answer the following queries:
1. Load the attendance.txt file and display all records.
attendance = LOAD 'attendance.txt' USING PigStorage(',')
AS (EmpID:int, Name:chararray, Department:chararray, DaysPresent:int);
2. Display all employees from the Finance department.
Filter employees in Finance department
finance_employees = FILTER attendance BY Department == 'Finance';
-- Display Finance employees
Q3   DUMP finance_employees;
CO-2; SO-3; BL-4   3. Compute the average attendance for each department.
Group by department
dept_group = GROUP attendance BY Department;
-- Calculate average DaysPresent
avg_attendance = FOREACH dept_group GENERATE
group AS Department,
AVG(attendance.DaysPresent) AS AvgDaysPresent;
-- Display average attendance per department
DUMP avg_attendance;
4. Sort employees by days present in ascending order.
-- Sort employees by DaysPresent
sorted_attendance = ORDER attendance BY DaysPresent ASC;
-- Display sorted employees
DUMP sorted_attendance;
5. Display details of employees who have attendance greater than 22 days.
-- Filter employees with DaysPresent > 22
high_attendance = FILTER attendance BY DaysPresent > 22;
-- Display details
[10]
a DUMP high_attendance;
CO-3; SO-3; BL-   You are a digital marketing intern at a start-up that connects brands with Instagram
3   b   influencers worldwide. Your task is to design a data visualization dashboard to analyse [10]
--- page 8 ---
influencer performance across countries and content categories such as beauty, fitness,
travel, and tech. The dataset includes influencer name, country, followers, engagement
rate, average likes, comments, shares, and monthly follower growth. The goal is to help
brands find the most engaging influencers for collaborations.
Answer the following:
(a) Which visualization techniques would you use to compare influencer performance
across countries? (2 marks)
(b) How would you visualize the relationship between follower count and engagement
rate? (2 marks)
(c) Suggest a suitable visualization to show the most popular content categories. (2
marks)
(d) How can insights from your dashboard help brands choose the best influencers? (4
marks)
Answer:
Visualization to Compare Influencer Performance Across Countries (2 marks)
• Choropleth Map / Geographic Heat Map:
o Shows countries colored by average engagement rate, followers, or
influencer activity.
o Quickly highlights regions with top-performing influencers.
•   Alternative: Bar chart grouped by country for average engagement, likes, or
growth metrics.
(b) Visualize Relationship Between Follower Count and Engagement Rate (2
marks)
•   Scatter Plot:
o   X-axis: Follower count
o   Y-axis: Engagement rate
o Each point represents an influencer.
o Helps identify whether influencers with higher followers maintain high
engagement.
•   Optional: Add color/size to indicate content category or growth rate for more
insight.
(c) Visualize Most Popular Content Categories (2 marks)
•   Pie Chart or Donut Chart:
o Shows proportion of influencers in each content category (Beauty,
Fitness, Travel, Tech).
•   Alternative: Horizontal bar chart ranking categories by average engagement or
number of influencers.
(d) How Insights Help Brands Choose the Best Influencers (4 marks)
1. Targeted Marketing: Brands can identify influencers in specific countries or
regions with high engagement.
2. Category Alignment: Helps choose influencers in relevant content categories to
match brand identity (e.g., beauty brand → beauty influencers).
3. Engagement vs Reach: Scatter plots reveal whether influencers with large
followers maintain high engagement, ensuring marketing ROI.
4. Growth Potential: Monthly follower growth insights allow brands to
collaborate with up-and-coming influencers for long-term campaigns.
--- page 9 ---
Analyze the use of Big Data in predictive maintenance for the manufacturing and
transportation sectors, highlighting the differences in data sources, analytics techniques,
and operational outcomes.
Introduction
Predictive maintenance uses Big Data analytics to anticipate equipment failures and
schedule maintenance before breakdowns occur, reducing downtime and operational
costs. Both manufacturing and transportation sectors leverage Big Data, but differ in
data sources, analytics approaches, and operational outcomes.
1. Manufacturing Sector (4 marks)
Data Sources:
•   Sensor data from machines (vibration, temperature, pressure, humidity)
•   Production logs, machine usage history
•   Maintenance records and warranty data
Analytics Techniques:
•   Descriptive Analytics: Monitors current machine health.
•   Predictive Analytics: Uses machine learning (regression, neural networks) to
forecast failures.
•   Real-time Analytics: Detects anomalies via streaming sensor data.
Operational Outcomes:
• Reduced unplanned downtime and maintenance costs
•   Improved production efficiency and quality
•   Optimized spare parts inventory
Q4   Example: Predicting when a CNC machine or conveyor belt will fail based on vibration
CO-1,; SO-2; BL-3   patterns.
2. Transportation Sector (4 marks)
Data Sources:
•   Telematics from vehicles (engine performance, speed, fuel consumption)
• GPS and route data
•   IoT sensors in fleets and infrastructure (e.g., bridges, tracks)
•   Historical breakdown and maintenance records
Analytics Techniques:
•   Predictive models (time-series analysis, regression, anomaly detection)
•   Fleet-wide optimization using IoT and Big Data platforms
•   Real-time alerts for vehicle performance and safety
Operational Outcomes:
• Reduced vehicle breakdowns and accidents
•   Optimized fleet scheduling and route planning
• Lower operational costs and improved customer satisfaction
Example: Predicting bus or truck engine failure before long trips to prevent delays.
3. Key Differences Between Manufacturing and Transportation (2 marks)
Aspect   Manufacturing   Transportation
Machines, sensors, production
Data Sources   Vehicles, telematics, GPS, IoT d
logs
a   Analytics Focus   Machine-level predictive models Fleet-level and vehicle-level pred[10]
--- page 10 ---
Operational   Maximize   uptime,   quality, Reduce breakdowns, ensure safety, optimize
Outcomes   efficiency   routes
High-frequency machine sensor Mixed frequency:   real-time telemetry +
Data Frequency
data   historical usage
Maintenance Scope   Individual equipment or plant   Entire fleet or infrastructure network
A financial analyst is working with a massive dataset of banking transactions to identify
fraudulent activities. Which data visualization techniques would be most effective to
detect anomalies or outliers in this big data environment? Explain your choice with a use
case.
. Effective Data Visualization Techniques (5 marks)
1. Scatter Plots
o   Plot two variables (e.g., transaction amount vs. transaction frequency).
o   Detects outliers or unusual transactions that deviate from normal
clusters.
2. Box Plots
o Displays median, quartiles, and extreme values.
o   Identifies transactions significantly higher or lower than typical values.
3. Heatmaps
o Shows correlation between variables, such as time of day vs.
transaction type.
o Helps identify suspicious spikes or unusual patterns.
4. Time-Series Plots
o Tracks transactions over time for each account or region.
o Sudden spikes or drops in activity highlight anomalies.
5. Network Graphs / Node-Link Diagrams
o Represents relationships between accounts, transactions, and
locations.
CO-1,; SO-2; BL-   o Useful for detecting fraud rings, money laundering, or circular
3
transactions.
2. Explanation of Choice (3 marks)
•   These techniques are effective for Big Data environments because they reduce
millions of records into visual patterns, enabling quick detection of anomalies.
• They allow analysts to focus on potential fraud cases instead of manually
inspecting the entire dataset.
•   Combination of plots provides a multi-dimensional view of transaction
behavior (amount, frequency, time, and relationships).
3. Use Case Example (2 marks)
•   Scenario: Detect credit card fraud in a dataset of millions of transactions.
•   Implementation:
1. Scatter plot: Transaction amount vs. frequency reveals a few extremely
high-value transactions outside the normal cluster.
2. Time-series plot: Shows that these outliers occur at unusual times (e.g.,
3 AM).
3. Network graph: Connects accounts with suspicious transfers, revealing
a potential fraud ring.
• Outcome: Fraud analysts can prioritize investigation on flagged transactions,
reducing false positives and improving detection efficiency.
[10]
b
--- page 11 ---
Consider the following dataset:
Emp_ID   Name   Department   Rating   Projects
401   Ankit   IT   4.5   5
402   Riya   HR   4.2   3
403   Mohan   Finance   4.8   6
404   Sneha   IT   4.1   4
405   Tara   HR   4.7   5
406   Vivek   Finance   4.3   2
407   Neha   IT   4.9   7
Create a Hive table named employee_performance and load the dataset. Then answer the
following queries:
1. Create the Hive table employee_performance, load data from
employee_performance.txt, and retrieve all records.
CREATE TABLE employee_performance (
EmpID INT,
Name STRING,
Department STRING,
Rating FLOAT,
ProjectsCompleted INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
Q5
CO-2,; SO-3; BL-   STORED AS TEXTFILE;
4
-- Load data from HDFS file
LOAD DATA INPATH '/user/hive/employee_performance.txt' INTO TABLE
employee_performance;
-- Retrieve all records
SELECT * FROM employee_performance;
2. Display all employees from the IT department.
SELECT *
FROM employee_performance
WHERE Department = 'IT';
3. Sort employees based on their rating in descending order.
SELECT *
FROM employee_performance
ORDER BY Rating DESC;
4. Retrieve the names of employees who have worked on more than 4 projects.
SELECT Name
FROM employee_performance
WHERE ProjectsCompleted > 4;
5. Count the number of employees in each department.
SELECT Department, COUNT(*) AS EmployeeCount
FROM employee_performance
[10]
a GROUP BY Department;
An e-commerce company tracks customer clicks, purchase history, and product reviews to
CO-13; SO-3;   recommend products. Identify the Big Data types, explain how analytics supports
BL-4   personalized marketing, and discuss the real-time data processing challenges.
[10]
b   Big Data Types in E-Commerce (3 marks)
--- page 12 ---
The company collects multiple types of Big Data:
1. Structured Data
o Customer purchase history, clicks, product IDs, transaction amounts.
o   Stored in relational databases or data warehouses.
2. Semi-Structured Data
o Logs, JSON/XML clickstream data, user preferences.
o Requires parsing to extract meaningful insights.
3. Unstructured Data
o Product reviews, social media comments, customer feedback.
o Requires natural language processing (NLP) or sentiment analysis.
2. How Analytics Supports Personalized Marketing (4 marks)
1. Recommendation Systems
o Collaborative Filtering: Suggests products liked by similar users.
o Content-Based Filtering: Suggests products similar to previously
viewed/purchased items.
3. Real-Time Data Processing Challenges (3 marks)
1. High Volume and Velocity
o   Millions of clicks and transactions per second require scalable real-time
processing systems.
2. Data Integration
o Combining structured, semi-structured, and unstructured data streams in
real time is complex.
3. Low-Latency Processing
o Recommendations must be generated instantly to influence current
browsing/purchase behavior.
4. Data Quality and Noise
o Clickstream logs and social media data can be incomplete or noisy,
affecting analytics accuracy.
5. Infrastructure & Cost
o Real-time processing requires robust Big Data frameworks like Apache
Kafka, Spark Streaming, or Flink, which can be expensive and complex
to maintain.
An e-commerce company wants to calculate the total sales per product category from
transaction logs stored across multiple servers. Describe how the MapReduce
programming model can be used to compute these totals efficiently. Discuss how
MapReduce ensures scalability when the number of transactions grows.
Using MapReduce to Calculate Total Sales per Product Category (5 marks)
The MapReduce programming model is ideal for processing large datasets distributed
across multiple servers. It works in two main phases: Map and Reduce.
Q6   Step 1: Map Phase
CO-1; SO-2; BL-   • Each mapper reads a portion of the transaction logs.
3
•   For each transaction, the mapper outputs a key-value pair:
•   Key: Product Category
•   Value: Transaction Amount
•   Example: A transaction of $100 for "Electronics" → ("Electronics", 100).
Step 2: Shuffle and Sort
• The framework groups all key-value pairs by key (product category) across all
[10]
a   mappers.
--- page 13 ---
•   All amounts for the same category are sent to the same reducer.
Step 3: Reduce Phase
• Each reducer receives a list of transaction amounts for a category.
• The reducer computes the sum of all amounts for that category.
•   Output: ("Electronics", 45000), ("Clothing", 32000), etc.
2. How MapReduce Ensures Scalability (5 marks)-
1. Parallel Processing
o   Multiple mappers process data simultaneously across different servers,
reducing overall computation time.
2. Data Locality
o MapReduce tries to run mappers close to where the data resides (HDFS
blocks), minimizing network overhead.
3. Automatic Task Distribution
o Hadoop divides data into splits and assigns them to available mappers and
reducers, scaling automatically with more nodes.
4. Fault Tolerance
o   Failed tasks are re-executed on other nodes, ensuring reliability in large-
scale environments.
5. Elastic Growth
o Adding more servers allows the system to handle growing transaction
volumes without redesigning the program.
Example:
•   For 1 million transactions, MapReduce can use 100 mappers.
•   If transactions increase to 10 million, the framework can scale by adding more
nodes and mappers to maintain processing efficiency.
Assess the effectiveness of Big Data analytics in combating climate change. ( anyone
topics from the below in detail is sufficient for 10 marks- big data approach is mandatory)
Introduction
Big Data analytics involves processing massive and complex datasets to extract insights
for decision-making. In the context of climate change, it can be used to monitor, predict,
and mitigate environmental impacts efficiently.
2. Areas Where Big Data Analytics Helps Combat Climate Change
1. Climate Monitoring and Modeling
o Analysis of satellite data, sensor networks, and weather stations to
monitor temperature, CO₂ levels, deforestation, and ocean changes.
o Helps create accurate climate models and forecasts.
CO-1; SO-3; BL-4   2. Energy Optimization
o Smart grid and energy consumption data enable efficient energy use,
reducing carbon footprints.
o   Predictive maintenance for renewable energy plants ensures optimal
energy production.
3. Disaster Prediction and Management
o Big Data from IoT sensors, historical weather, and social media can
predict extreme events like floods, hurricanes, or droughts.
o Enables timely evacuation and resource allocation.
4. Sustainable Agriculture
o Data from soil sensors, drones, and weather forecasts optimize water
usage,   fertilizer   application, and crop   selection,   reducing
[10]
b   environmental impact.
--- page 14 ---
5. Carbon Emission Tracking
o Companies and governments can monitor emissions in real time to
identify high-emission activities and implement reduction strategies.
3. Effectiveness and Benefits
• Informed Policy Making: Data-driven insights support government regulations
and climate policies.
•   Early Warning Systems: Predictive analytics improves resilience to climate
events.
•   Efficiency Improvements: Optimizes energy, transportation, and resource
management.
•   Global Collaboration: Shared datasets and analytics enable coordinated climate
action worldwide.
4. Challenges / Limitations
• Data Volume & Variety: Integrating heterogeneous datasets from satellites,
sensors, and social media is complex.
• Real-Time Processing: High-velocity climate data requires fast processing
frameworks.
• Data Quality & Reliability: Inaccurate or missing data can mislead predictions.
•   Infrastructure & Costs: Big Data platforms and storage for climate datasets are
resource-intensive.
Discuss features of HBase. How is it different from Google Bigtable?
Features of HBase (6 marks)
HBase is a distributed, scalable, NoSQL database built on top of Hadoop HDFS. Its
key features include:
1. Column-Oriented Storage
o Data is stored in column families, enabling efficient reads and writes
for sparse datasets.
Q7
CO-1; SO-1 BL-1   2. Scalability
o   Horizontally scalable across thousands of commodity servers.
3. Real-Time Read/Write Access
o Supports low-latency random reads and writes, unlike HDFS which is
optimized for batch processing.
4. Automatic Sharding (Region Splitting)
o Tables are split into regions, automatically distributed across region
servers to balance load.
5. Versioning of Data
o Each cell can store multiple versions of data identified by timestamps.
6. Integration with Hadoop Ecosystem
o Works seamlessly with MapReduce, Hive, Pig, Spark, and HDFS for
analytics.
[10]
a   7. Fault Tolerance
--- page 15 ---
o Leverages HDFS replication and automatic failover for region servers.
8. Schema Flexibility
o Allows dynamic addition of columns in column families; rows can have
variable columns.
2. Differences Between HBase and Google Bigtable (4 marks)
Feature   HBase   Google Bigtable
Proprietary, cloud-
Open-source, runs
Platform   based (Google
on Hadoop/HDFS
Cloud)
Uses HDFS for   Uses Google File
Storage
persistence   System (GFS)
Proprietary API,
API/Languag Java API, REST,
client libraries in
e Support   Thrift
multiple languages
On-premises or   Managed by Google
Deployment
cloud   Cloud (serverless)
Limited to Google
Hadoop ecosystem:
Ecosystem   Cloud tools
MapReduce, Hive,
Integration   (BigQuery,
Pig, Spark
Dataflow)
Replication & HDFS replication;   Built-in high
Fault   region server   availability, multi-
Tolerance   failover   zone replication
Paid, cloud-based
Cost   Free, open-source
service
Explain the concept of Big Data Analytics. How does it differ from traditional analytics?
Discuss the types of analytics (descriptive, predictive, and prescriptive) with examples.
Concept of Big Data Analytics (1 marks)
Big Data Analytics (BDA) is the process of examining large and complex datasets
(structured, semi-structured, unstructured) to discover patterns, trends, and insights for
better decision-making.
Example: An e-commerce site analyzing clicks, purchases, and reviews to recommend
CO-1; SO-2; BL-   products.
3
2. Difference from Traditional Analytics (1 mark)
Feature   Traditional Analytics Big Data Analytics
Data Volume Small to medium   Massive (TBs to PBs)
Data Type   Structured only   Structured, semi-structured, unstructured
[5]
b   Processing   Batch   Real-time or near real-time
--- page 16 ---
Tools   SQL, Excel   Hadoop, Spark, NoSQL, AI/ML
3. Types of Analytics (1 marks each)
1. Descriptive Analytics: Understand what happened.
o Example: Monthly sales report.
2. Predictive Analytics: Forecast what will happen.
o Example: Predict customer churn.
3. Prescriptive Analytics: Recommend actions to achieve outcomes.
o Example: Optimize pricing strategy in retail.
You are given the ratings of 4 users on 5 movies. Compute the cosine similarity between
User1, User2 and User3. Compute cosine similarity. Check whether User1 is similar to
User2 or User3?( user 1 and user 2 similarity – 2marks, user 1 and user 3 similarity –
2marks, compare and state answer 1 mark)
Movie   User1   User2   User3   User4
M1   5   4   3   5
M2   3   5   2   4
M3   0   2   0   1
M4   1   0   1   0
M5   4   3   5   4
Cosine Similarity Formula
For two users 𝐴and 𝐵:
∑𝑖   (𝐴𝑖⋅𝐵𝑖)
Cosine Similarity =
√∑𝑖   𝐴𝑖 2 ⋅√∑𝑖   𝐵𝑖 2
Where 𝐴𝑖and 𝐵𝑖are ratings for movie 𝑖.
2. User Vectors
CO-1; SO-2; BL-
3   Movie User1 User2 User3
M1   5   4   3
M2   3   5   2
M3   0   2   0
M4   1   0   1
M5   4   3   5
So, vectors are:
• 𝑈1 = [5,3,0,1,4]
• 𝑈2 = [4,5,2,0,3]
• 𝑈3 = [3,2,0,1,5]
3. Compute Cosine Similarity
Step 1: User1 & User2
Dot product:
5 ∗4 + 3 ∗5 + 0 ∗2 + 1 ∗0 + 4 ∗3 = 20 + 15 + 0 + 0 + 12 = 47
Magnitude:
∣∣𝑈1 ∣∣= √52 + 32 + 02 + 12 + 42 = √25 + 9 + 0 + 1 + 16 = √51 ≈7.141
[5]
c   ∣∣𝑈2 ∣∣= √42 + 52 + 22 + 02 + 32 = √16 + 25 + 4 + 0 + 9 = √54 ≈7.348
--- page 17 ---
Cosine Similarity:
47   47
cos⁡(𝑈1, 𝑈2) =   ≈   ≈0.895
7.141 ∗7.348   52.49
Step 2: User1 & User3
Dot product:
5 ∗3 + 3 ∗2 + 0 ∗0 + 1 ∗1 + 4 ∗5 = 15 + 6 + 0 + 1 + 20 = 42
Magnitude:
∣∣𝑈3 ∣∣= √32 + 22 + 02 + 12 + 52 = √9 + 4 + 0 + 1 + 25 = √39 ≈6.245
Cosine Similarity:
42   42
cos⁡(𝑈1, 𝑈3) =   ≈   ≈0.942
7.141 ∗6.245   44.60
4. Interpretation
•   Cosine similarity values range from 0 to 1 (higher = more similar).
cos⁡(𝑈1, 𝑈2) ≈0.895, cos⁡(𝑈1, 𝑈3) ≈0.942
Conclusion: User1 is more similar to User3 than to User2.
Answer:
•   Cosine Similarity:
o User1 & User2 = 0.895
o User1 & User3 = 0.942
• Most similar user to User1: User3
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper be0d35da618c

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7057/Big Data Analytics/ANS_Big Data Analytics(702DB0C029)_2025-2026.docx`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05/12/ 2025
- Text: docx (1 page)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
|
Programs:   B Tech, BTI, MBA Tech
Streams: B Tech CS, DS, CSEDS, AI, BTI CS, AI
| Year:   IV/VI Semester:   VII/ XI
|
Subject:   Big Data Analytics
| Time: 3 hrs. (02:00pm to 05:00pm)
|
Date:05/12/ 2025
| No. of Pages: 3
|
Marks: 100
|
|
Final Examination
|
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q1

|
| Answer briefly:
|
|
CO- 1; SO- 2; BL-2
| a
| A city government collects data from traffic sensors, CCTV cameras, public transport systems, and social media to monitor traffic flow and public safety.
Identify the types of Big Data characteristics in this scenario. Explain how Big Data Analytics can help improve city planning and reduce congestion.
Big Data Characteristics in the Scenario (2 marks)
The data collected by the city exhibits the 3 Vs of Big Data:
Characteristic
| Explanation / Example
|
Volume
| Large amounts of data from traffic sensors, CCTV cameras, and social media posts.
|
Velocity
| Data is generated and transmitted in real-time (e.g., live traffic feed, sensor updates).
|
Variety
| Different types of data: structured (sensor readings, transport schedules), semi-structured (logs, JSON from apps), unstructured (videos, social media posts).
|
Veracity (optional bonus)
| Data may contain noise, errors, or inconsistencies from multiple sources.
|
Value
| Insights can be extracted to improve traffic management and city planning.
|

2. How Big Data Analytics Helps Improve City Planning & Reduce Congestion (3 marks)
Traffic Flow Optimization:
Analyze real-time traffic sensor and CCTV data to detect congestion points.
Adjust traffic signals dynamically to reduce bottlenecks.
Public Transport Planning:
Use smart card, GPS, and passenger data to optimize bus and train routes.
Identify high-demand areas and adjust schedules.
Predictive Analytics:
Forecast traffic patterns during peak hours or events using historical data.
Proactively manage road closures, detours, and public warnings.
Safety & Incident Management:
Detect accidents or unusual events from CCTV and social media reports.
Dispatch emergency services quickly to minimize disruption.
Urban Planning Insights:
Use aggregated data to design new roads, pedestrian zones, or bike lanes.
Improve long-term infrastructure planning based on actual usage patterns.

| [5]
|
CO-1; SO-2; BL-2
| b
| Discuss Data Node and Name Node in HDFS.
Introduction to HDFS
HDFS (Hadoop Distributed File System) is the primary storage system of Hadoop.
It follows a Master-Slave architecture:
Master Node: NameNode
Slave Nodes: DataNodes
HDFS stores large files by splitting them into blocks (default 128 MB) and distributing them across multiple nodes for reliability and scalability.

2. NameNode (Master Node) 2.5 marks
Role: The NameNode is the central controller of HDFS.
Responsibilities:
Maintains the metadata of the file system:
File names, file permissions
Directory structure
Mapping of blocks to DataNodes
Manages namespace operations:
Create, delete, rename files/directories
Monitors DataNode health via periodic heartbeats.
Handles replication:
Ensures each block is replicated across multiple DataNodes (default 3) for fault tolerance.
Does not store actual data — only metadata.
Important Note: If the NameNode fails, HDFS becomes unavailable unless a Secondary NameNode or High-Availability setup is used.

3. DataNode (Slave Node)2.5 marks
Role: DataNodes are the storage units of HDFS.
Responsibilities:
Store actual data blocks on local disk.
Serve read/write requests from clients.
Periodically send block reports and heartbeats to the NameNode.
Manage replication at the block level (create/delete blocks as instructed by NameNode).
Ensure data durability and availability.
Features:
Runs on commodity hardware.
Can be added or removed easily for scalability.

| [5]
|
CO- 2; SO-2 ; BL-2
| c
| What is the purpose of a Combiner in MapReduce? How does it help optimize performance? Give an example to illustrate its use.
1. Purpose of a Combiner (2 marks)
A Combiner is an optional mini-reducer in MapReduce.
It aggregates intermediate key-value pairs generated by the Mapper before sending them to the Reducer.
Helps reduce the volume of data transferred over the network (shuffle phase).
Key Point: Combiner does local aggregation on Mapper nodes to optimize performance but does not guarantee final results (Reducer still does the actual computation).

2. How it Optimizes Performance (2 marks)
Reduces network I/O: Fewer intermediate key-value pairs are sent from Mappers to Reducers.
Speeds up processing: Less data for Reducers to handle.
Particularly useful for commutative and associative operations (e.g., sum, count, max).

3. Example: Word Count(1mark)
Scenario: Counting words in a large text file.
Mapper Output (Intermediate Pairs):
Mapper1: ("data",1), ("science",1), ("data",1)
Mapper2: ("science",1), ("big",1), ("data",1)
Without Combiner:
All intermediate pairs sent to Reducer:
[("data",1), ("science",1), ("data",1), ("science",1), ("big",1), ("data",1)]
With Combiner (local aggregation at Mapper):
Mapper1 Combiner: ("data",2), ("science",1)
Mapper2 Combiner: ("science",1), ("big",1), ("data",1)
Fewer key-value pairs are sent over the network → less shuffle data → faster processing.

| [5]
|
CO- 3; SO- 3; BL-2
| d
| Explain the major issues that impact the effectiveness of Big Data visualization. (any 5 points 5 marks)
Introduction
Big Data visualization helps in understanding patterns and insights from massive, complex datasets. However, its effectiveness can be limited by several issues.

2. Major Issues
Volume of Data
Extremely large datasets can overwhelm visualization tools.
Rendering millions of data points can cause performance lags or crashes.
Variety of Data
Data comes in multiple formats: structured, semi-structured, unstructured.
Integrating heterogeneous data into a coherent visualization is challenging.
Velocity of Data
Real-time data streams (e.g., IoT sensors, social media) require dynamic and continuous updates.
Lag or outdated visuals reduce decision-making effectiveness.
Data Quality (Veracity)
Inaccurate, incomplete, or noisy data can mislead visual interpretations.
Requires preprocessing, cleaning, and validation before visualization.
Complexity of Analysis
High-dimensional or multi-variate data can be difficult to represent in simple charts.
May require advanced visualization techniques (heatmaps, 3D plots, dashboards).
Scalability of Tools
Not all visualization tools can handle Big Data efficiently.
Tools need to scale horizontally or use techniques like sampling or aggregation.
Interpretability
Overly complex or cluttered visuals can confuse users.
Choosing the right type of chart/graph is critical for clarity.

| [5]
|
Q2
CO-3; SO-1; BL-1
| a
| An online education platform wants to recommend courses to students based on their course completion and ratings.
i. Explain how collaborative filtering can help suggest courses to a student.
ii. If two students have rated the same courses similarly, what does high cosine similarity imply?
iii. Suggest a strategy to recommend courses to a new student with no ratings.
Collaborative Filtering for Course Recommendations (4 marks)
Definition:
Collaborative Filtering (CF) is a technique to suggest items (courses) to a user based on the preferences of other similar users.
Assumes that students who agreed in the past will agree in the future.
How it works:
Collect ratings of courses by all students.
Compute similarity between students (user-based CF) or between courses (item-based CF).
Recommend courses that similar students liked but the target student hasn’t taken.
Example:
Student A rated courses [X=5, Y=4].
Student B rated courses [X=5, Y=4, Z=5].
CF recommends course Z to Student A because Student B with similar ratings liked it.

ii. High Cosine Similarity Between Two Students (2 marks)
Cosine similarity measures the angle between two students’ rating vectors.
High cosine similarity implies:
Students’ ratings across courses are very similar.
Their preferences align closely.
Courses liked by one student are likely to be relevant to the other.
Example:
Student A vector: [5,4,0]
Student B vector: [5,4,5]
Cosine similarity ≈ 0.99 → strong alignment → CF recommends Student B’s liked course (Z) to Student A.

iii. Strategy for New Student (Cold Start Problem) (4 marks)
Problem: New students have no prior ratings, so CF cannot be applied.
Strategies:
Content-Based Filtering:
Recommend courses based on the student’s profile: interests, skills, or demographic data.
Example: Student interested in “Data Science” → recommend courses in Python, Machine Learning, etc.
Popularity-Based Recommendations:
Suggest top-rated or most-enrolled courses across the platform.
Hybrid Approach:
Combine content-based and collaborative filtering after initial course completions/ratings.
Onboarding Surveys / Quick Assessment:
Ask the student to rate a few courses or topics during signup to generate initial recommendations.

| [10]
|
CO-1,; SO-; BL-
| b
| Elaborate at least five file formats in HDFS.( 5 file formats , 2 marks each)
Introduction
HDFS (Hadoop Distributed File System) supports multiple file formats, optimized for storage, processing, and analytics. The choice of format affects read/write performance, compression, and compatibility with tools like MapReduce, Hive, and Spark.

1. Text File (TXT / CSV)
Description: Plain-text file format; each line is a record, fields separated by delimiters (comma, tab).
Advantages:
Easy to read and debug.
Compatible with most tools.
Disadvantages:
No schema; parsing large datasets is inefficient.
Use Case: Small datasets, log files, or data exchange between systems.

2. Sequence File
Description: Binary key-value format used internally by Hadoop. Stores data as <key, value> pairs.
Advantages:
Optimized for MapReduce processing.
Supports splitting, enabling parallel processing.
Disadvantages:
Not human-readable.
Use Case: Intermediate storage for Mapper output, or bulk storage of structured data.

3. Avro
Description: Row-based binary format with schema stored in JSON. Supports schema evolution.
Advantages:
Compact and fast serialization/deserialization.
Schema evolution allows adding/removing fields without breaking applications.
Disadvantages:
Less efficient for analytical queries that need only a few columns.
Use Case: Streaming data, data exchange between systems, and records requiring schema evolution.

4. Parquet
Description: Columnar storage format designed for analytical workloads. Stores data column-wise, rather than row-wise.
Advantages:
Efficient for read-heavy queries.
Better compression and reduced I/O for selected columns.
Supports complex nested data types.
Disadvantages:
Row-wise inserts/updates are less efficient.
Use Case: Data warehouses, Hive/Spark SQL analytics, OLAP workloads.

5. ORC (Optimized Row Columnar)
Description: Columnar format optimized for Hive.
Advantages:
High compression (ZLIB/Snappy).
Fast query execution with predicate pushdown.
Efficient for large-scale analytical queries.
Disadvantages:
Not ideal for frequent row-level updates.
Use Case: Hive tables, large-scale analytics, queries with selective columns.

6. JSON
Description: Semi-structured text format using key-value pairs, often nested.
Advantages:
Human-readable and widely used for APIs.
Supports nested and hierarchical data.
Disadvantages:
Larger file size, slower processing compared to binary formats.
Use Case: Web logs, API data ingestion, semi-structured datasets.

7. XML
Description: Semi-structured markup language format.
Advantages:
Supports hierarchical data.
Standardized and self-descriptive.
Disadvantages:
Verbose, high storage overhead, slower parsing.
Use Case: Legacy data exchange, configuration files.

| [10]
|
Q3
CO-2; SO-3; BL-4
| a
| Consider the following dataset :
101 Anjali HR 22
102 Ramesh IT 18
103 Meera Finance 25
104 Tarun IT 20
105 Kavita HR 19
106 Suresh Finance 23
107 Nisha IT 26
Each record represents:
· Employee ID
· Name
· Department
· Days Present (in a month)
Create a PIG script to process the attendance.txt file and answer the following queries:
1. Load the attendance.txt file and display all records.
attendance = LOAD 'attendance.txt' USING PigStorage(',')
AS (EmpID:int, Name:chararray, Department:chararray, DaysPresent:int);
2. Display all employees from the Finance department.
Filter employees in Finance department
finance_employees = FILTER attendance BY Department == 'Finance';

-- Display Finance employees
DUMP finance_employees;
3. Compute the average attendance for each department.
Group by department
dept_group = GROUP attendance BY Department;

-- Calculate average DaysPresent
avg_attendance = FOREACH dept_group GENERATE
group AS Department,
AVG(attendance.DaysPresent) AS AvgDaysPresent;

-- Display average attendance per department
DUMP avg_attendance;
4. Sort employees by days present in ascending order.
-- Sort employees by DaysPresent
sorted_attendance = ORDER attendance BY DaysPresent ASC;

-- Display sorted employees
DUMP sorted_attendance;
5. Display details of employees who have attendance greater than 22 days.
-- Filter employees with DaysPresent > 22
high_attendance = FILTER attendance BY DaysPresent > 22;

-- Display details
DUMP high_attendance;
| [10]
|
CO-3; SO-3; BL-3
| b
| You are a digital marketing intern at a start-up that connects brands with Instagram influencers worldwide. Your task is to design a data visualization dashboard to analyse influencer performance across countries and content categories such as beauty, fitness, travel, and tech. The dataset includes influencer name, country, followers, engagement rate, average likes, comments, shares, and monthly follower growth. The goal is to help brands find the most engaging influencers for collaborations.
Answer the following:
(a) Which visualization techniques would you use to compare influencer performance across countries? (2 marks)
(b) How would you visualize the relationship between follower count and engagement rate? (2 marks)
(c) Suggest a suitable visualization to show the most popular content categories. (2 marks)
(d) How can insights from your dashboard help brands choose the best influencers? (4 marks)
Answer:
Visualization to Compare Influencer Performance Across Countries (2 marks)
Choropleth Map / Geographic Heat Map:
Shows countries colored by average engagement rate, followers, or influencer activity.
Quickly highlights regions with top-performing influencers.
Alternative: Bar chart grouped by country for average engagement, likes, or growth metrics.

(b) Visualize Relationship Between Follower Count and Engagement Rate (2 marks)
Scatter Plot:
X-axis: Follower count
Y-axis: Engagement rate
Each point represents an influencer.
Helps identify whether influencers with higher followers maintain high engagement.
Optional: Add color/size to indicate content category or growth rate for more insight.

(c) Visualize Most Popular Content Categories (2 marks)
Pie Chart or Donut Chart:
Shows proportion of influencers in each content category (Beauty, Fitness, Travel, Tech).
Alternative: Horizontal bar chart ranking categories by average engagement or number of influencers.

(d) How Insights Help Brands Choose the Best Influencers (4 marks)
Targeted Marketing: Brands can identify influencers in specific countries or regions with high engagement.
Category Alignment: Helps choose influencers in relevant content categories to match brand identity (e.g., beauty brand → beauty influencers).
Engagement vs Reach: Scatter plots reveal whether influencers with large followers maintain high engagement, ensuring marketing ROI.
Growth Potential: Monthly follower growth insights allow brands to collaborate with up-and-coming influencers for long-term campaigns.

| [10]
|
Q4
CO-1,; SO-2; BL-3
| a
| Analyze the use of Big Data in predictive maintenance for the manufacturing and transportation sectors, highlighting the differences in data sources, analytics techniques, and operational outcomes.

Introduction
Predictive maintenance uses Big Data analytics to anticipate equipment failures and schedule maintenance before breakdowns occur, reducing downtime and operational costs. Both manufacturing and transportation sectors leverage Big Data, but differ in data sources, analytics approaches, and operational outcomes.

1. Manufacturing Sector (4 marks)
Data Sources:
Sensor data from machines (vibration, temperature, pressure, humidity)
Production logs, machine usage history
Maintenance records and warranty data
Analytics Techniques:
Descriptive Analytics: Monitors current machine health.
Predictive Analytics: Uses machine learning (regression, neural networks) to forecast failures.
Real-time Analytics: Detects anomalies via streaming sensor data.
Operational Outcomes:
Reduced unplanned downtime and maintenance costs
Improved production efficiency and quality
Optimized spare parts inventory
Example: Predicting when a CNC machine or conveyor belt will fail based on vibration patterns.

2. Transportation Sector (4 marks)

Data Sources:
Telematics from vehicles (engine performance, speed, fuel consumption)
GPS and route data
IoT sensors in fleets and infrastructure (e.g., bridges, tracks)
Historical breakdown and maintenance records
Analytics Techniques:
Predictive models (time-series analysis, regression, anomaly detection)
Fleet-wide optimization using IoT and Big Data platforms
Real-time alerts for vehicle performance and safety
Operational Outcomes:
Reduced vehicle breakdowns and accidents
Optimized fleet scheduling and route planning
Lower operational costs and improved customer satisfaction
Example: Predicting bus or truck engine failure before long trips to prevent delays.

3. Key Differences Between Manufacturing and Transportation (2 marks)
Aspect
| Manufacturing
| Transportation
|
Data Sources
| Machines, sensors, production logs
| Vehicles, telematics, GPS, IoT devices
|
Analytics Focus
| Machine-level predictive models
| Fleet-level and vehicle-level predictive models
|
Operational Outcomes
| Maximize uptime, quality, efficiency
| Reduce breakdowns, ensure safety, optimize routes
|
Data Frequency
| High-frequency machine sensor data
| Mixed frequency: real-time telemetry + historical usage
|
Maintenance Scope
| Individual equipment or plant
| Entire fleet or infrastructure network
|

| [10]
|
CO-1,; SO-2; BL-3
| b
| A financial analyst is working with a massive dataset of banking transactions to identify fraudulent activities. Which data visualization techniques would be most effective to detect anomalies or outliers in this big data environment? Explain your choice with a use case.
. Effective Data Visualization Techniques (5 marks)
Scatter Plots
Plot two variables (e.g., transaction amount vs. transaction frequency).
Detects outliers or unusual transactions that deviate from normal clusters.
Box Plots
Displays median, quartiles, and extreme values.
Identifies transactions significantly higher or lower than typical values.
Heatmaps
Shows correlation between variables, such as time of day vs. transaction type.
Helps identify suspicious spikes or unusual patterns.
Time-Series Plots
Tracks transactions over time for each account or region.
Sudden spikes or drops in activity highlight anomalies.
Network Graphs / Node-Link Diagrams
Represents relationships between accounts, transactions, and locations.
Useful for detecting fraud rings, money laundering, or circular transactions.

2. Explanation of Choice (3 marks)
These techniques are effective for Big Data environments because they reduce millions of records into visual patterns, enabling quick detection of anomalies.
They allow analysts to focus on potential fraud cases instead of manually inspecting the entire dataset.
Combination of plots provides a multi-dimensional view of transaction behavior (amount, frequency, time, and relationships).

3. Use Case Example (2 marks)
Scenario: Detect credit card fraud in a dataset of millions of transactions.
Implementation:
Scatter plot: Transaction amount vs. frequency reveals a few extremely high-value transactions outside the normal cluster.
Time-series plot: Shows that these outliers occur at unusual times (e.g., 3 AM).
Network graph: Connects accounts with suspicious transfers, revealing a potential fraud ring.
Outcome: Fraud analysts can prioritize investigation on flagged transactions, reducing false positives and improving detection efficiency.

| [10]
|
Q5
CO-2,; SO-3; BL-4
| a
| Consider the following dataset:
Emp_ID
| Name
| Department
| Rating
| Projects
|
401
| Ankit
| IT
| 4.5
| 5
|
402
| Riya
| HR
| 4.2
| 3
|
403
| Mohan
| Finance
| 4.8
| 6
|
404
| Sneha
| IT
| 4.1
| 4
|
405
| Tara
| HR
| 4.7
| 5
|
406
| Vivek
| Finance
| 4.3
| 2
|
407
| Neha
| IT
| 4.9
| 7
|
Create a Hive table named employee_performance and load the dataset. Then answer the following queries:
1. Create the Hive table employee_performance, load data from employee_performance.txt, and retrieve all records.
CREATE TABLE employee_performance (
EmpID INT,
Name STRING,
Department STRING,
Rating FLOAT,
ProjectsCompleted INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Load data from HDFS file
LOAD DATA INPATH '/user/hive/employee_performance.txt' INTO TABLE employee_performance;

-- Retrieve all records
SELECT * FROM employee_performance;
2. Display all employees from the IT department.
SELECT *
FROM employee_performance
WHERE Department = 'IT';
3. Sort employees based on their rating in descending order.
SELECT *
FROM employee_performance
ORDER BY Rating DESC;
4. Retrieve the names of employees who have worked on more than 4 projects.
SELECT Name
FROM employee_performance
WHERE ProjectsCompleted > 4;
5. Count the number of employees in each department.
SELECT Department, COUNT(*) AS EmployeeCount
FROM employee_performance
GROUP BY Department;
| [10]
|
CO-13; SO-3; BL-4
| b
| An e-commerce company tracks customer clicks, purchase history, and product reviews to recommend products. Identify the Big Data types, explain how analytics supports personalized marketing, and discuss the real-time data processing challenges.
Big Data Types in E-Commerce (3 marks)
The company collects multiple types of Big Data:
Structured Data
Customer purchase history, clicks, product IDs, transaction amounts.
Stored in relational databases or data warehouses.
Semi-Structured Data
Logs, JSON/XML clickstream data, user preferences.
Requires parsing to extract meaningful insights.
Unstructured Data
Product reviews, social media comments, customer feedback.
Requires natural language processing (NLP) or sentiment analysis.

2. How Analytics Supports Personalized Marketing (4 marks)
Recommendation Systems
Collaborative Filtering: Suggests products liked by similar users.
Content-Based Filtering: Suggests products similar to previously viewed/purchased items.

3. Real-Time Data Processing Challenges (3 marks)
High Volume and Velocity
Millions of clicks and transactions per second require scalable real-time processing systems.
Data Integration
Combining structured, semi-structured, and unstructured data streams in real time is complex.
Low-Latency Processing
Recommendations must be generated instantly to influence current browsing/purchase behavior.
Data Quality and Noise
Clickstream logs and social media data can be incomplete or noisy, affecting analytics accuracy.
Infrastructure & Cost
Real-time processing requires robust Big Data frameworks like Apache Kafka, Spark Streaming, or Flink, which can be expensive and complex to maintain.

| [10]
|
Q6
CO-1; SO-2; BL-3
| a
| An e-commerce company wants to calculate the total sales per product category from transaction logs stored across multiple servers. Describe how the MapReduce programming model can be used to compute these totals efficiently. Discuss how MapReduce ensures scalability when the number of transactions grows.
Using MapReduce to Calculate Total Sales per Product Category (5 marks)
The MapReduce programming model is ideal for processing large datasets distributed across multiple servers. It works in two main phases: Map and Reduce.
Step 1: Map Phase
Each mapper reads a portion of the transaction logs.
For each transaction, the mapper outputs a key-value pair:
Key: Product Category
Value: Transaction Amount
Example: A transaction of $100 for "Electronics" → ("Electronics", 100).
Step 2: Shuffle and Sort
The framework groups all key-value pairs by key (product category) across all mappers.
All amounts for the same category are sent to the same reducer.
Step 3: Reduce Phase
Each reducer receives a list of transaction amounts for a category.
The reducer computes the sum of all amounts for that category.
Output: ("Electronics", 45000), ("Clothing", 32000), etc.
2. How MapReduce Ensures Scalability (5 marks)-
Parallel Processing
Multiple mappers process data simultaneously across different servers, reducing overall computation time.
Data Locality
MapReduce tries to run mappers close to where the data resides (HDFS blocks), minimizing network overhead.
Automatic Task Distribution
Hadoop divides data into splits and assigns them to available mappers and reducers, scaling automatically with more nodes.
Fault Tolerance
Failed tasks are re-executed on other nodes, ensuring reliability in large-scale environments.
Elastic Growth
Adding more servers allows the system to handle growing transaction volumes without redesigning the program.
Example:
For 1 million transactions, MapReduce can use 100 mappers.
If transactions increase to 10 million, the framework can scale by adding more nodes and mappers to maintain processing efficiency.

| [10]
|
CO-1; SO-3; BL-4
| b
| Assess the effectiveness of Big Data analytics in combating climate change. ( anyone topics from the below in detail is sufficient for 10 marks- big data approach is mandatory)
Introduction
Big Data analytics involves processing massive and complex datasets to extract insights for decision-making. In the context of climate change, it can be used to monitor, predict, and mitigate environmental impacts efficiently.

2. Areas Where Big Data Analytics Helps Combat Climate Change
Climate Monitoring and Modeling
Analysis of satellite data, sensor networks, and weather stations to monitor temperature, CO₂ levels, deforestation, and ocean changes.
Helps create accurate climate models and forecasts.
Energy Optimization
Smart grid and energy consumption data enable efficient energy use, reducing carbon footprints.
Predictive maintenance for renewable energy plants ensures optimal energy production.
Disaster Prediction and Management
Big Data from IoT sensors, historical weather, and social media can predict extreme events like floods, hurricanes, or droughts.
Enables timely evacuation and resource allocation.
Sustainable Agriculture
Data from soil sensors, drones, and weather forecasts optimize water usage, fertilizer application, and crop selection, reducing environmental impact.
Carbon Emission Tracking
Companies and governments can monitor emissions in real time to identify high-emission activities and implement reduction strategies.

3. Effectiveness and Benefits
Informed Policy Making: Data-driven insights support government regulations and climate policies.
Early Warning Systems: Predictive analytics improves resilience to climate events.
Efficiency Improvements: Optimizes energy, transportation, and resource management.
Global Collaboration: Shared datasets and analytics enable coordinated climate action worldwide.

4. Challenges / Limitations
Data Volume & Variety: Integrating heterogeneous datasets from satellites, sensors, and social media is complex.
Real-Time Processing: High-velocity climate data requires fast processing frameworks.
Data Quality & Reliability: Inaccurate or missing data can mislead predictions.
Infrastructure & Costs: Big Data platforms and storage for climate datasets are resource-intensive.

| [10]
|
Q7
CO-1; SO-1 BL-1
| a
| Discuss features of HBase. How is it different from Google Bigtable?

Features of HBase (6 marks)
HBase is a distributed, scalable, NoSQL database built on top of Hadoop HDFS. Its key features include:
Column-Oriented Storage
Data is stored in column families, enabling efficient reads and writes for sparse datasets.
Scalability
Horizontally scalable across thousands of commodity servers.
Real-Time Read/Write Access
Supports low-latency random reads and writes, unlike HDFS which is optimized for batch processing.
Automatic Sharding (Region Splitting)
Tables are split into regions, automatically distributed across region servers to balance load.
Versioning of Data
Each cell can store multiple versions of data identified by timestamps.
Integration with Hadoop Ecosystem
Works seamlessly with MapReduce, Hive, Pig, Spark, and HDFS for analytics.
Fault Tolerance
Leverages HDFS replication and automatic failover for region servers.
Schema Flexibility
Allows dynamic addition of columns in column families; rows can have variable columns.

2. Differences Between HBase and Google Bigtable (4 marks)
Feature
| HBase
| Google Bigtable
|
Platform
| Open-source, runs on Hadoop/HDFS
| Proprietary, cloud-based (Google Cloud)
|
Storage
| Uses HDFS for persistence
| Uses Google File System (GFS)
|
API/Language Support
| Java API, REST, Thrift
| Proprietary API, client libraries in multiple languages
|
Deployment
| On-premises or cloud
| Managed by Google Cloud (serverless)
|
Ecosystem Integration
| Hadoop ecosystem: MapReduce, Hive, Pig, Spark
| Limited to Google Cloud tools (BigQuery, Dataflow)
|
Replication & Fault Tolerance
| HDFS replication; region server failover
| Built-in high availability, multi-zone replication
|
Cost
| Free, open-source
| Paid, cloud-based service
|

|
|
|

| [10]
|
CO-1; SO-2; BL-3
| b
| Explain the concept of Big Data Analytics. How does it differ from traditional analytics? Discuss the types of analytics (descriptive, predictive, and prescriptive) with examples.
Concept of Big Data Analytics (1 marks)
Big Data Analytics (BDA) is the process of examining large and complex datasets (structured, semi-structured, unstructured) to discover patterns, trends, and insights for better decision-making.
Example: An e-commerce site analyzing clicks, purchases, and reviews to recommend products.

2. Difference from Traditional Analytics (1 mark)
Feature
| Traditional Analytics
| Big Data Analytics
|
Data Volume
| Small to medium
| Massive (TBs to PBs)
|
Data Type
| Structured only
| Structured, semi-structured, unstructured
|
Processing
| Batch
| Real-time or near real-time
|
Tools
| SQL, Excel
| Hadoop, Spark, NoSQL, AI/ML
|

3. Types of Analytics (1 marks each)
Descriptive Analytics: Understand what happened.
Example: Monthly sales report.
Predictive Analytics: Forecast what will happen.
Example: Predict customer churn.
Prescriptive Analytics: Recommend actions to achieve outcomes.
Example: Optimize pricing strategy in retail.
| [5]
|
CO-1; SO-2; BL-3
| c
| You are given the ratings of 4 users on 5 movies. Compute the cosine similarity between User1, User2 and User3. Compute cosine similarity. Check whether User1 is similar to User2 or User3?( user 1 and user 2 similarity – 2marks, user 1 and user 3 similarity – 2marks, compare and state answer 1 mark)
Movie
| User1
| User2
| User3
| User4
|
M1
| 5
| 4
| 3
| 5
|
M2
| 3
| 5
| 2
| 4
|
M3
| 0
| 2
| 0
| 1
|
M4
| 1
| 0
| 1
| 0
|
M5
| 4
| 3
| 5
| 4
|
Cosine Similarity Formula
For two users Aand B:
Cosine Similarity=i(Ai⋅Bi)iAi2⋅iBi2

Where Aiand Biare ratings for movie i.

2. User Vectors
Movie
| User1
| User2
| User3
|
M1
| 5
| 4
| 3
|
M2
| 3
| 5
| 2
|
M3
| 0
| 2
| 0
|
M4
| 1
| 0
| 1
|
M5
| 4
| 3
| 5
|
So, vectors are:
U1=[5,3,0,1,4]
U2=[4,5,2,0,3]
U3=[3,2,0,1,5]

3. Compute Cosine Similarity
Step 1: User1 & User2
Dot product:
5*4+3*5+0*2+1*0+4*3=20+15+0+0+12=47

Magnitude:
∣∣U1∣∣=52+32+02+12+42=25+9+0+1+16=51≈7.141
∣∣U2∣∣=42+52+22+02+32=16+25+4+0+9=54≈7.348

Cosine Similarity:
cos⁡(U1,U2)=477.141*7.348≈4752.49≈0.895

Step 2: User1 & User3
Dot product:
5*3+3*2+0*0+1*1+4*5=15+6+0+1+20=42

Magnitude:
∣∣U3∣∣=32+22+02+12+52=9+4+0+1+25=39≈6.245

Cosine Similarity:
cos⁡(U1,U3)=427.141*6.245≈4244.60≈0.942

4. Interpretation
Cosine similarity values range from 0 to 1 (higher = more similar).
cos⁡(U1,U2)≈0.895,cos⁡(U1,U3)≈0.942
Conclusion: User1 is more similar to User3 than to User2.

Answer:
Cosine Similarity:
User1 & User2 = 0.895
User1 & User3 = 0.942
Most similar user to User1: User3

| [5]
|
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 75fdb4e5d222

- Departments: Computer Engineering, Computer Science
- Programmes: BTech Computer 7002, BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CS_7055/Big Data Analytics/ANS_Big Data Analytics(702DB0C029)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05/12/ 2025
- Text: text (17 pages)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
Programs: B Tech, BTI, MBA Tech   Year: IV/VI Semester: VII/ XI
Streams: B Tech CS, DS, CSEDS, AI, BTI CS, AI
Subject: Big Data Analytics   Time: 3 hrs. (02:00pm to 05:00pm)
Date:05/12/ 2025   No. of Pages: 3
Marks: 100
Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Q1
Answer briefly:
A city government collects data from traffic sensors, CCTV cameras, public transport
systems, and   social media   to   monitor   traffic flow and   public   safety.
Identify the types of Big Data characteristics in this scenario. Explain how Big Data
Analytics can help improve city planning and reduce congestion.
Big Data Characteristics in the Scenario (2 marks)
The data collected by the city exhibits the 3 Vs of Big Data:
Characteristic   Explanation / Example
Volume   Large amounts of data from traffic sensors, CCTV cameras, and social media posts.
Data is generated and transmitted in real-time (e.g., live traffic feed, sensor
Velocity
updates).
CO- 1; SO- 2; BL-2   Different types of data: structured (sensor readings, transport schedules), semi-
Variety
structured (logs, JSON from apps), unstructured (videos, social media posts).
Veracity   (optional
Data may contain noise, errors, or inconsistencies from multiple sources.
bonus)
Value   Insights can be extracted to improve traffic management and city planning.
2. How Big Data Analytics Helps Improve City Planning & Reduce Congestion (3
marks)
1. Traffic Flow Optimization:
o Analyze real-time traffic sensor and CCTV data to detect congestion
[5]
a   points.
--- page 2 ---
o Adjust traffic signals dynamically to reduce bottlenecks.
2. Public Transport Planning:
o Use smart card, GPS, and passenger data to optimize bus and train routes.
o   Identify high-demand areas and adjust schedules.
3. Predictive Analytics:
o   Forecast traffic patterns during peak hours or events using historical data.
o   Proactively manage road closures, detours, and public warnings.
4. Safety & Incident Management:
o   Detect accidents or unusual events from CCTV and social media reports.
o Dispatch emergency services quickly to minimize disruption.
5. Urban Planning Insights:
o Use aggregated data to design new roads, pedestrian zones, or bike lanes.
o Improve long-term infrastructure planning based on actual usage patterns.
Discuss Data Node and Name Node in HDFS.
Introduction to HDFS
HDFS (Hadoop Distributed File System) is the primary storage system of Hadoop.
It follows a Master-Slave architecture:
 Master Node: NameNode
   Slave Nodes: DataNodes
HDFS stores large files by splitting them into blocks (default 128 MB) and distributing
them across multiple nodes for reliability and scalability.
2. NameNode (Master Node) 2.5 marks
Role: The NameNode is the central controller of HDFS.
Responsibilities:
1. Maintains the metadata of the file system:
o   File names, file permissions
o   Directory structure
o Mapping of blocks to DataNodes
2. Manages namespace operations:
o   Create, delete, rename files/directories
CO-1; SO-2; BL-2   3. Monitors DataNode health via periodic heartbeats.
4. Handles replication:
o Ensures each block is replicated across multiple DataNodes (default 3) for
fault tolerance.
5. Does not store actual data — only metadata.
Important Note: If the NameNode fails, HDFS becomes unavailable unless a Secondary
NameNode or High-Availability setup is used.
3. DataNode (Slave Node)2.5 marks
Role: DataNodes are the storage units of HDFS.
Responsibilities:
1. Store actual data blocks on local disk.
2. Serve read/write requests from clients.
3. Periodically send block reports and heartbeats to the NameNode.
4. Manage replication at the block level (create/delete blocks as instructed by
NameNode).
5. Ensure data durability and availability.
Features:
[5]
b    Runs on commodity hardware.
--- page 3 ---
 Can be added or removed easily for scalability.
What is the purpose of a Combiner in MapReduce? How does it help optimize
performance? Give an example to illustrate its use.
1. Purpose of a Combiner (2 marks)
 A Combiner is an optional mini-reducer in MapReduce.
   It aggregates intermediate key-value pairs generated by the Mapper before
sending them to the Reducer.
   Helps reduce the volume of data transferred over the network (shuffle phase).
Key Point: Combiner does local aggregation on Mapper nodes to optimize performance
but does not guarantee final results (Reducer still does the actual computation).
2. How it Optimizes Performance (2 marks)
 Reduces network I/O: Fewer intermediate key-value pairs are sent from Mappers
to Reducers.
 Speeds up processing: Less data for Reducers to handle.
   Particularly useful for commutative and associative operations (e.g., sum,
CO- 2; SO-2 ; BL-2   count, max).
3. Example: Word Count(1mark)
Scenario: Counting words in a large text file.
Mapper Output (Intermediate Pairs):
Mapper1: ("data",1), ("science",1), ("data",1)
Mapper2: ("science",1), ("big",1), ("data",1)
Without Combiner:
All intermediate pairs sent to Reducer:
[("data",1), ("science",1), ("data",1), ("science",1), ("big",1), ("data",1)]
With Combiner (local aggregation at Mapper):
Mapper1 Combiner: ("data",2), ("science",1)
Mapper2 Combiner: ("science",1), ("big",1), ("data",1)
 Fewer key-value pairs are sent over the network → less shuffle data → faster
processing.
[5]
c
Explain the major issues that impact the effectiveness of Big Data visualization. (any 5
points 5 marks)
Introduction
Big Data visualization helps in understanding patterns and insights from massive, complex
datasets. However, its effectiveness can be limited by several issues.
2. Major Issues
1. Volume of Data
o Extremely large datasets can overwhelm visualization tools.
CO- 3; SO- 3; BL-2
o Rendering millions of data points can cause performance lags or
crashes.
2. Variety of Data
o Data comes in multiple formats: structured, semi-structured, unstructured.
o   Integrating heterogeneous data into a coherent visualization   is
challenging.
3. Velocity of Data
o Real-time data streams (e.g., IoT sensors, social media) require dynamic
[5]
d   and continuous updates.
--- page 4 ---
o Lag or outdated visuals reduce decision-making effectiveness.
4. Data Quality (Veracity)
o   Inaccurate, incomplete, or noisy data can mislead visual interpretations.
o Requires preprocessing, cleaning, and validation before visualization.
5. Complexity of Analysis
o High-dimensional or multi-variate data can be difficult to represent in
simple charts.
o May require advanced visualization techniques (heatmaps, 3D plots,
dashboards).
6. Scalability of Tools
o Not all visualization tools can handle Big Data efficiently.
o Tools need to scale horizontally or use techniques like sampling or
aggregation.
7. Interpretability
o Overly complex or cluttered visuals can confuse users.
o Choosing the right type of chart/graph is critical for clarity.
An online education platform wants to recommend courses to students based on their
course completion and ratings.
i. Explain how collaborative filtering can help suggest courses to a student.
ii. If two students have rated the same courses similarly, what does high cosine similarity
imply?
iii. Suggest a strategy to recommend courses to a new student with no ratings.
Collaborative Filtering for Course Recommendations (4 marks)
Definition:
   Collaborative Filtering (CF) is a technique to suggest items (courses) to a user
based on the preferences of other similar users.
 Assumes that students who agreed in the past will agree in the future.
How it works:
1. Collect ratings of courses by all students.
2. Compute similarity between students (user-based CF) or between courses (item-
based CF).
3. Recommend courses that similar students liked but the target student hasn’t
Q2   taken.
CO-3; SO-1; BL-1   Example:
   Student A rated courses [X=5, Y=4].
   Student B rated courses [X=5, Y=4, Z=5].
 CF recommends course Z to Student A because Student B with similar ratings
liked it.
ii. High Cosine Similarity Between Two Students (2 marks)
   Cosine similarity measures the angle between two students’ rating vectors.
 High cosine similarity implies:
1. Students’ ratings across courses are very similar.
2. Their preferences align closely.
3. Courses liked by one student are likely to be relevant to the other.
Example:
   Student A vector: [5,4,0]
   Student B vector: [5,4,5]
   Cosine similarity ≈ 0.99 → strong alignment → CF recommends Student B’s
[10]
a   liked course (Z) to Student A.
--- page 5 ---
iii. Strategy for New Student (Cold Start Problem) (4 marks)
Problem: New students have no prior ratings, so CF cannot be applied.
Strategies:
1. Content-Based Filtering:
o Recommend courses based on the student’s profile: interests, skills, or
demographic data.
o Example: Student interested in “Data Science” → recommend courses in
Python, Machine Learning, etc.
2. Popularity-Based Recommendations:
o Suggest top-rated or most-enrolled courses across the platform.
3. Hybrid Approach:
o Combine content-based and collaborative filtering after initial course
completions/ratings.
4. Onboarding Surveys / Quick Assessment:
o Ask the student to rate a few courses or topics during signup to generate
initial recommendations.
Elaborate at least five file formats in HDFS.( 5 file formats , 2 marks each)
Introduction
HDFS (Hadoop Distributed File System) supports multiple file formats, optimized for
storage, processing, and analytics. The choice of format affects read/write
performance, compression, and compatibility with tools like MapReduce, Hive, and
Spark.
1. Text File (TXT / CSV)
   Description: Plain-text file format; each line is a record, fields separated by
delimiters (comma, tab).
   Advantages:
o Easy to read and debug.
CO-1,; SO-; BL-   o Compatible with most tools.
   Disadvantages:
o No schema; parsing large datasets is inefficient.
 Use Case: Small datasets, log files, or data exchange between systems.
2. Sequence File
   Description: Binary key-value format used internally by Hadoop. Stores data as
<key, value> pairs.
   Advantages:
o Optimized for MapReduce processing.
o Supports splitting, enabling parallel processing.
   Disadvantages:
[10]
b   o Not human-readable.
--- page 6 ---
 Use Case: Intermediate storage for Mapper output, or bulk storage of structured
data.
3. Avro
   Description: Row-based binary format with schema stored in JSON. Supports
schema evolution.
   Advantages:
o Compact and fast serialization/deserialization.
o Schema evolution allows adding/removing fields without breaking
applications.
   Disadvantages:
o Less efficient for analytical queries that need only a few columns.
 Use Case: Streaming data, data exchange between systems, and records requiring
schema evolution.
4. Parquet
   Description: Columnar storage format designed for analytical workloads. Stores
data column-wise, rather than row-wise.
   Advantages:
o   Efficient for read-heavy queries.
o   Better compression and reduced I/O for selected columns.
o Supports complex nested data types.
   Disadvantages:
o Row-wise inserts/updates are less efficient.
 Use Case: Data warehouses, Hive/Spark SQL analytics, OLAP workloads.
5. ORC (Optimized Row Columnar)
   Description: Columnar format optimized for Hive.
   Advantages:
o High compression (ZLIB/Snappy).
o   Fast query execution with predicate pushdown.
o   Efficient for large-scale analytical queries.
   Disadvantages:
o Not ideal for frequent row-level updates.
 Use Case: Hive tables, large-scale analytics, queries with selective columns.
6. JSON
   Description: Semi-structured text format using key-value pairs, often nested.
   Advantages:
o Human-readable and widely used for APIs.
o Supports nested and hierarchical data.
   Disadvantages:
o Larger file size, slower processing compared to binary formats.
 Use Case: Web logs, API data ingestion, semi-structured datasets.
7. XML
   Description: Semi-structured markup language format.
   Advantages:
o Supports hierarchical data.
o   Standardized and self-descriptive.
   Disadvantages:
--- page 7 ---
o Verbose, high storage overhead, slower parsing.
 Use Case: Legacy data exchange, configuration files.
Consider the following dataset :
101 Anjali HR 22
102 Ramesh IT 18
103 Meera Finance 25
104 Tarun IT 20
105 Kavita HR 19
106 Suresh Finance 23
107 Nisha IT 26
Each record represents:
· Employee ID
· Name
· Department
· Days Present (in a month)
Create a PIG script to process the attendance.txt file and answer the following queries:
1. Load the attendance.txt file and display all records.
attendance = LOAD 'attendance.txt' USING PigStorage(',')
AS (EmpID:int, Name:chararray, Department:chararray, DaysPresent:int);
2. Display all employees from the Finance department.
Filter employees in Finance department
finance_employees = FILTER attendance BY Department == 'Finance';
-- Display Finance employees
Q3   DUMP finance_employees;
CO-2; SO-3; BL-4   3. Compute the average attendance for each department.
Group by department
dept_group = GROUP attendance BY Department;
-- Calculate average DaysPresent
avg_attendance = FOREACH dept_group GENERATE
group AS Department,
AVG(attendance.DaysPresent) AS AvgDaysPresent;
-- Display average attendance per department
DUMP avg_attendance;
4. Sort employees by days present in ascending order.
-- Sort employees by DaysPresent
sorted_attendance = ORDER attendance BY DaysPresent ASC;
-- Display sorted employees
DUMP sorted_attendance;
5. Display details of employees who have attendance greater than 22 days.
-- Filter employees with DaysPresent > 22
high_attendance = FILTER attendance BY DaysPresent > 22;
-- Display details
[10]
a DUMP high_attendance;
CO-3; SO-3; BL-   You are a digital marketing intern at a start-up that connects brands with Instagram
3   b   influencers worldwide. Your task is to design a data visualization dashboard to analyse [10]
--- page 8 ---
influencer performance across countries and content categories such as beauty, fitness,
travel, and tech. The dataset includes influencer name, country, followers, engagement
rate, average likes, comments, shares, and monthly follower growth. The goal is to help
brands find the most engaging influencers for collaborations.
Answer the following:
(a) Which visualization techniques would you use to compare influencer performance
across countries? (2 marks)
(b) How would you visualize the relationship between follower count and engagement
rate? (2 marks)
(c) Suggest a suitable visualization to show the most popular content categories. (2
marks)
(d) How can insights from your dashboard help brands choose the best influencers? (4
marks)
Answer:
Visualization to Compare Influencer Performance Across Countries (2 marks)
 Choropleth Map / Geographic Heat Map:
o Shows countries colored by average engagement rate, followers, or
influencer activity.
o Quickly highlights regions with top-performing influencers.
   Alternative: Bar chart grouped by country for average engagement, likes, or
growth metrics.
(b) Visualize Relationship Between Follower Count and Engagement Rate (2
marks)
   Scatter Plot:
o   X-axis: Follower count
o   Y-axis: Engagement rate
o Each point represents an influencer.
o Helps identify whether influencers with higher followers maintain high
engagement.
   Optional: Add color/size to indicate content category or growth rate for more
insight.
(c) Visualize Most Popular Content Categories (2 marks)
   Pie Chart or Donut Chart:
o Shows proportion of influencers in each content category (Beauty,
Fitness, Travel, Tech).
   Alternative: Horizontal bar chart ranking categories by average engagement or
number of influencers.
(d) How Insights Help Brands Choose the Best Influencers (4 marks)
1. Targeted Marketing: Brands can identify influencers in specific countries or
regions with high engagement.
2. Category Alignment: Helps choose influencers in relevant content categories to
match brand identity (e.g., beauty brand → beauty influencers).
3. Engagement vs Reach: Scatter plots reveal whether influencers with large
followers maintain high engagement, ensuring marketing ROI.
4. Growth Potential: Monthly follower growth insights allow brands to
collaborate with up-and-coming influencers for long-term campaigns.
--- page 9 ---
Analyze the use of Big Data in predictive maintenance for the manufacturing and
transportation sectors, highlighting the differences in data sources, analytics techniques,
and operational outcomes.
Introduction
Predictive maintenance uses Big Data analytics to anticipate equipment failures and
schedule maintenance before breakdowns occur, reducing downtime and operational
costs. Both manufacturing and transportation sectors leverage Big Data, but differ in
data sources, analytics approaches, and operational outcomes.
1. Manufacturing Sector (4 marks)
Data Sources:
   Sensor data from machines (vibration, temperature, pressure, humidity)
   Production logs, machine usage history
   Maintenance records and warranty data
Analytics Techniques:
   Descriptive Analytics: Monitors current machine health.
   Predictive Analytics: Uses machine learning (regression, neural networks) to
forecast failures.
   Real-time Analytics: Detects anomalies via streaming sensor data.
Operational Outcomes:
 Reduced unplanned downtime and maintenance costs
   Improved production efficiency and quality
   Optimized spare parts inventory
Q4   Example: Predicting when a CNC machine or conveyor belt will fail based on vibration
CO-1,; SO-2; BL-3   patterns.
2. Transportation Sector (4 marks)
Data Sources:
   Telematics from vehicles (engine performance, speed, fuel consumption)
 GPS and route data
   IoT sensors in fleets and infrastructure (e.g., bridges, tracks)
   Historical breakdown and maintenance records
Analytics Techniques:
   Predictive models (time-series analysis, regression, anomaly detection)
   Fleet-wide optimization using IoT and Big Data platforms
   Real-time alerts for vehicle performance and safety
Operational Outcomes:
 Reduced vehicle breakdowns and accidents
   Optimized fleet scheduling and route planning
 Lower operational costs and improved customer satisfaction
Example: Predicting bus or truck engine failure before long trips to prevent delays.
3. Key Differences Between Manufacturing and Transportation (2 marks)
Aspect   Manufacturing   Transportation
Machines, sensors, production
Data Sources   Vehicles, telematics, GPS, IoT devices
logs
a   Analytics Focus   Machine-level predictive models Fleet-level and vehicle-level predictive [10] models
--- page 10 ---
Operational   Maximize   uptime,   quality, Reduce breakdowns, ensure safety, optimize
Outcomes   efficiency   routes
High-frequency machine sensor Mixed frequency:   real-time telemetry +
Data Frequency
data   historical usage
Maintenance Scope   Individual equipment or plant   Entire fleet or infrastructure network
A financial analyst is working with a massive dataset of banking transactions to identify
fraudulent activities. Which data visualization techniques would be most effective to
detect anomalies or outliers in this big data environment? Explain your choice with a use
case.
. Effective Data Visualization Techniques (5 marks)
1. Scatter Plots
o   Plot two variables (e.g., transaction amount vs. transaction frequency).
o   Detects outliers or unusual transactions that deviate from normal
clusters.
2. Box Plots
o Displays median, quartiles, and extreme values.
o   Identifies transactions significantly higher or lower than typical values.
3. Heatmaps
o Shows correlation between variables, such as time of day vs.
transaction type.
o Helps identify suspicious spikes or unusual patterns.
4. Time-Series Plots
o Tracks transactions over time for each account or region.
o Sudden spikes or drops in activity highlight anomalies.
5. Network Graphs / Node-Link Diagrams
o Represents relationships between accounts, transactions, and
locations.
CO-1,; SO-2; BL-   o Useful for detecting fraud rings, money laundering, or circular
3
transactions.
2. Explanation of Choice (3 marks)
   These techniques are effective for Big Data environments because they reduce
millions of records into visual patterns, enabling quick detection of anomalies.
 They allow analysts to focus on potential fraud cases instead of manually
inspecting the entire dataset.
   Combination of plots provides a multi-dimensional view of transaction
behavior (amount, frequency, time, and relationships).
3. Use Case Example (2 marks)
   Scenario: Detect credit card fraud in a dataset of millions of transactions.
   Implementation:
1. Scatter plot: Transaction amount vs. frequency reveals a few extremely
high-value transactions outside the normal cluster.
2. Time-series plot: Shows that these outliers occur at unusual times (e.g.,
3 AM).
3. Network graph: Connects accounts with suspicious transfers, revealing
a potential fraud ring.
 Outcome: Fraud analysts can prioritize investigation on flagged transactions,
reducing false positives and improving detection efficiency.
[10]
b
--- page 11 ---
Consider the following dataset:
Emp_ID   Name   Department   Rating   Projects
401   Ankit   IT   4.5   5
402   Riya   HR   4.2   3
403   Mohan   Finance   4.8   6
404   Sneha   IT   4.1   4
405   Tara   HR   4.7   5
406   Vivek   Finance   4.3   2
407   Neha   IT   4.9   7
Create a Hive table named employee_performance and load the dataset. Then answer the
following queries:
1. Create the Hive table employee_performance, load data from
employee_performance.txt, and retrieve all records.
CREATE TABLE employee_performance (
EmpID INT,
Name STRING,
Department STRING,
Rating FLOAT,
ProjectsCompleted INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
Q5
CO-2,; SO-3; BL-   STORED AS TEXTFILE;
4
-- Load data from HDFS file
LOAD DATA INPATH '/user/hive/employee_performance.txt' INTO TABLE
employee_performance;
-- Retrieve all records
SELECT * FROM employee_performance;
2. Display all employees from the IT department.
SELECT *
FROM employee_performance
WHERE Department = 'IT';
3. Sort employees based on their rating in descending order.
SELECT *
FROM employee_performance
ORDER BY Rating DESC;
4. Retrieve the names of employees who have worked on more than 4 projects.
SELECT Name
FROM employee_performance
WHERE ProjectsCompleted > 4;
5. Count the number of employees in each department.
SELECT Department, COUNT(*) AS EmployeeCount
FROM employee_performance
[10]
a GROUP BY Department;
An e-commerce company tracks customer clicks, purchase history, and product reviews to
CO-13; SO-3;   recommend products. Identify the Big Data types, explain how analytics supports
BL-4   personalized marketing, and discuss the real-time data processing challenges.
[10]
b   Big Data Types in E-Commerce (3 marks)
--- page 12 ---
The company collects multiple types of Big Data:
1. Structured Data
o Customer purchase history, clicks, product IDs, transaction amounts.
o   Stored in relational databases or data warehouses.
2. Semi-Structured Data
o Logs, JSON/XML clickstream data, user preferences.
o Requires parsing to extract meaningful insights.
3. Unstructured Data
o Product reviews, social media comments, customer feedback.
o Requires natural language processing (NLP) or sentiment analysis.
2. How Analytics Supports Personalized Marketing (4 marks)
1. Recommendation Systems
o Collaborative Filtering: Suggests products liked by similar users.
o Content-Based Filtering: Suggests products similar to previously
viewed/purchased items.
3. Real-Time Data Processing Challenges (3 marks)
1. High Volume and Velocity
o   Millions of clicks and transactions per second require scalable real-time
processing systems.
2. Data Integration
o Combining structured, semi-structured, and unstructured data streams in
real time is complex.
3. Low-Latency Processing
o Recommendations must be generated instantly to influence current
browsing/purchase behavior.
4. Data Quality and Noise
o Clickstream logs and social media data can be incomplete or noisy,
affecting analytics accuracy.
5. Infrastructure & Cost
o Real-time processing requires robust Big Data frameworks like Apache
Kafka, Spark Streaming, or Flink, which can be expensive and complex
to maintain.
An e-commerce company wants to calculate the total sales per product category from
transaction logs stored across multiple servers. Describe how the MapReduce
programming model can be used to compute these totals efficiently. Discuss how
MapReduce ensures scalability when the number of transactions grows.
Using MapReduce to Calculate Total Sales per Product Category (5 marks)
The MapReduce programming model is ideal for processing large datasets distributed
Q6   across multiple servers. It works in two main phases: Map and Reduce.
CO-1; SO-2; BL-
3   Step 1: Map Phase
 Each mapper reads a portion of the transaction logs.
   For each transaction, the mapper outputs a key-value pair:
   Key: Product Category
   Value: Transaction Amount
   Example: A transaction of $100 for "Electronics" → ("Electronics", 100).
[10]
a   Step 2: Shuffle and Sort
--- page 13 ---
 The framework groups all key-value pairs by key (product category) across all
mappers.
   All amounts for the same category are sent to the same reducer.
Step 3: Reduce Phase
 Each reducer receives a list of transaction amounts for a category.
 The reducer computes the sum of all amounts for that category.
   Output: ("Electronics", 45000), ("Clothing", 32000), etc.
2. How MapReduce Ensures Scalability (5 marks)-
1. Parallel Processing
o   Multiple mappers process data simultaneously across different servers,
reducing overall computation time.
2. Data Locality
o MapReduce tries to run mappers close to where the data resides (HDFS
blocks), minimizing network overhead.
3. Automatic Task Distribution
o Hadoop divides data into splits and assigns them to available mappers and
reducers, scaling automatically with more nodes.
4. Fault Tolerance
o   Failed tasks are re-executed on other nodes, ensuring reliability in large-
scale environments.
5. Elastic Growth
o Adding more servers allows the system to handle growing transaction
volumes without redesigning the program.
Example:
   For 1 million transactions, MapReduce can use 100 mappers.
   If transactions increase to 10 million, the framework can scale by adding more
nodes and mappers to maintain processing efficiency.
Assess the effectiveness of Big Data analytics in combating climate change. ( anyone
topics from the below in detail is sufficient for 10 marks- big data approach is mandatory)
Introduction
Big Data analytics involves processing massive and complex datasets to extract insights
for decision-making. In the context of climate change, it can be used to monitor, predict,
and mitigate environmental impacts efficiently.
2. Areas Where Big Data Analytics Helps Combat Climate Change
1. Climate Monitoring and Modeling
o Analysis of satellite data, sensor networks, and weather stations to
monitor temperature, CO₂ levels, deforestation, and ocean changes.
CO-1; SO-3; BL-4
o Helps create accurate climate models and forecasts.
2. Energy Optimization
o Smart grid and energy consumption data enable efficient energy use,
reducing carbon footprints.
o   Predictive maintenance for renewable energy plants ensures optimal
energy production.
3. Disaster Prediction and Management
o Big Data from IoT sensors, historical weather, and social media can
predict extreme events like floods, hurricanes, or droughts.
o Enables timely evacuation and resource allocation.
[10]
b   4. Sustainable Agriculture
--- page 14 ---
o Data from soil sensors, drones, and weather forecasts optimize water
usage,   fertilizer   application, and crop   selection,   reducing
environmental impact.
5. Carbon Emission Tracking
o Companies and governments can monitor emissions in real time to
identify high-emission activities and implement reduction strategies.
3. Effectiveness and Benefits
 Informed Policy Making: Data-driven insights support government regulations
and climate policies.
   Early Warning Systems: Predictive analytics improves resilience to climate
events.
   Efficiency Improvements: Optimizes energy, transportation, and resource
management.
   Global Collaboration: Shared datasets and analytics enable coordinated climate
action worldwide.
4. Challenges / Limitations
 Data Volume & Variety: Integrating heterogeneous datasets from satellites,
sensors, and social media is complex.
 Real-Time Processing: High-velocity climate data requires fast processing
frameworks.
 Data Quality & Reliability: Inaccurate or missing data can mislead predictions.
   Infrastructure & Costs: Big Data platforms and storage for climate datasets are
resource-intensive.
Discuss features of HBase. How is it different from Google Bigtable?
Features of HBase (6 marks)
HBase is a distributed, scalable, NoSQL database built on top of Hadoop HDFS. Its
key features include:
1. Column-Oriented Storage
Q7   o Data is stored in column families, enabling efficient reads and writes
CO-1; SO-1 BL-1   for sparse datasets.
2. Scalability
o   Horizontally scalable across thousands of commodity servers.
3. Real-Time Read/Write Access
o Supports low-latency random reads and writes, unlike HDFS which is
optimized for batch processing.
4. Automatic Sharding (Region Splitting)
o Tables are split into regions, automatically distributed across region
servers to balance load.
5. Versioning of Data
o Each cell can store multiple versions of data identified by timestamps.
[10]
a   6. Integration with Hadoop Ecosystem
--- page 15 ---
o Works seamlessly with MapReduce, Hive, Pig, Spark, and HDFS for
analytics.
7. Fault Tolerance
o Leverages HDFS replication and automatic failover for region servers.
8. Schema Flexibility
o Allows dynamic addition of columns in column families; rows can have
variable columns.
2. Differences Between HBase and Google Bigtable (4 marks)
Feature   HBase   Google Bigtable
Proprietary, cloud-
Open-source, runs
Platform   based (Google
on Hadoop/HDFS
Cloud)
Uses HDFS for   Uses Google File
Storage
persistence   System (GFS)
Proprietary API,
API/Languag Java API, REST,
client libraries in
e Support   Thrift
multiple languages
On-premises or   Managed by Google
Deployment
cloud   Cloud (serverless)
Limited to Google
Hadoop ecosystem:
Ecosystem   Cloud tools
MapReduce, Hive,
Integration   (BigQuery,
Pig, Spark
Dataflow)
Replication & HDFS replication;   Built-in high
Fault   region server   availability, multi-
Tolerance   failover   zone replication
Paid, cloud-based
Cost   Free, open-source
service
Explain the concept of Big Data Analytics. How does it differ from traditional analytics?
Discuss the types of analytics (descriptive, predictive, and prescriptive) with examples.
Concept of Big Data Analytics (1 marks)
Big Data Analytics (BDA) is the process of examining large and complex datasets
(structured, semi-structured, unstructured) to discover patterns, trends, and insights for
CO-1; SO-2; BL-   better decision-making.
3   Example: An e-commerce site analyzing clicks, purchases, and reviews to recommend
products.
2. Difference from Traditional Analytics (1 mark)
Feature   Traditional Analytics Big Data Analytics
[5]
b   Data Volume Small to medium   Massive (TBs to PBs)
--- page 16 ---
Data Type   Structured only   Structured, semi-structured, unstructured
Processing   Batch   Real-time or near real-time
Tools   SQL, Excel   Hadoop, Spark, NoSQL, AI/ML
3. Types of Analytics (1 marks each)
1. Descriptive Analytics: Understand what happened.
o Example: Monthly sales report.
2. Predictive Analytics: Forecast what will happen.
o Example: Predict customer churn.
3. Prescriptive Analytics: Recommend actions to achieve outcomes.
o Example: Optimize pricing strategy in retail.
You are given the ratings of 4 users on 5 movies. Compute the cosine similarity between
User1, User2 and User3. Compute cosine similarity. Check whether User1 is similar to
User2 or User3?( user 1 and user 2 similarity – 2marks, user 1 and user 3 similarity –
2marks, compare and state answer 1 mark)
Movie   User1   User2   User3   User4
M1   5   4   3   5
M2   3   5   2   4
M3   0   2   0   1
M4   1   0   1   0
M5   4   3   5   4
Cosine Similarity Formula
For two users 𝐴and 𝐵:
∑𝑖   (𝐴𝑖⋅𝐵𝑖)
Cosine Similarity =
√∑𝑖   𝐴𝑖 2 ⋅√∑𝑖   𝐵𝑖 2
Where 𝐴𝑖and 𝐵𝑖are ratings for movie 𝑖.
CO-1; SO-2; BL-
3   2. User Vectors
Movie User1 User2 User3
M1   5   4   3
M2   3   5   2
M3   0   2   0
M4   1   0   1
M5   4   3   5
So, vectors are:
 𝑈1 = [5,3,0,1,4]
 𝑈2 = [4,5,2,0,3]
 𝑈3 = [3,2,0,1,5]
3. Compute Cosine Similarity
Step 1: User1 & User2
Dot product:
5 ∗4 + 3 ∗5 + 0 ∗2 + 1 ∗0 + 4 ∗3 = 20 + 15 + 0 + 0 + 12 = 47
[5]
c   Magnitude:
--- page 17 ---
∣∣𝑈1 ∣∣= √52 + 32 + 02 + 12 + 42 = √25 + 9 + 0 + 1 + 16 = √51 ≈7.141
∣∣𝑈2 ∣∣= √42 + 52 + 22 + 02 + 32 = √16 + 25 + 4 + 0 + 9 = √54 ≈7.348
Cosine Similarity:
47   47
cos⁡(𝑈1, 𝑈2) =   ≈   ≈0.895
7.141 ∗7.348   52.49
Step 2: User1 & User3
Dot product:
5 ∗3 + 3 ∗2 + 0 ∗0 + 1 ∗1 + 4 ∗5 = 15 + 6 + 0 + 1 + 20 = 42
Magnitude:
∣∣𝑈3 ∣∣= √32 + 22 + 02 + 12 + 52 = √9 + 4 + 0 + 1 + 25 = √39 ≈6.245
Cosine Similarity:
42   42
cos⁡(𝑈1, 𝑈3) =   ≈   ≈0.942
7.141 ∗6.245   44.60
4. Interpretation
   Cosine similarity values range from 0 to 1 (higher = more similar).
cos⁡(𝑈1, 𝑈2) ≈0.895, cos⁡(𝑈1, 𝑈3) ≈0.942
Conclusion: User1 is more similar to User3 than to User2.
Answer:
   Cosine Similarity:
o User1 & User2 = 0.895
o User1 & User3 = 0.942
 Most similar user to User1: User3
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 0c74d7474b0e

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_Computer_7002/Big Data Analytics/ANS_Big Data Analytics(702DB0C029)_2025-2026.docx`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05/12/ 2025
- Text: docx (1 page)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
|
Programs:   B Tech, BTI, MBA Tech
Streams: B Tech CS, DS, CSEDS, AI, BTI CS, AI
| Year:   IV/VI Semester:   VII/ XI
|
Subject:   Big Data Analytics
| Time: 3 hrs. (02:00pm to 05:00pm)
|
Date:05/12/ 2025
| No. of Pages: 3
|
Marks: 100
|
|
Final Examination
|
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q1

|
| Answer briefly:
|
|
CO- 1; SO- 2; BL-2
| a
| A city government collects data from traffic sensors, CCTV cameras, public transport systems, and social media to monitor traffic flow and public safety.
Identify the types of Big Data characteristics in this scenario. Explain how Big Data Analytics can help improve city planning and reduce congestion.
Big Data Characteristics in the Scenario (2 marks)
The data collected by the city exhibits the 3 Vs of Big Data:
Characteristic
| Explanation / Example
|
Volume
| Large amounts of data from traffic sensors, CCTV cameras, and social media posts.
|
Velocity
| Data is generated and transmitted in real-time (e.g., live traffic feed, sensor updates).
|
Variety
| Different types of data: structured (sensor readings, transport schedules), semi-structured (logs, JSON from apps), unstructured (videos, social media posts).
|
Veracity (optional bonus)
| Data may contain noise, errors, or inconsistencies from multiple sources.
|
Value
| Insights can be extracted to improve traffic management and city planning.
|

2. How Big Data Analytics Helps Improve City Planning & Reduce Congestion (3 marks)
Traffic Flow Optimization:
Analyze real-time traffic sensor and CCTV data to detect congestion points.
Adjust traffic signals dynamically to reduce bottlenecks.
Public Transport Planning:
Use smart card, GPS, and passenger data to optimize bus and train routes.
Identify high-demand areas and adjust schedules.
Predictive Analytics:
Forecast traffic patterns during peak hours or events using historical data.
Proactively manage road closures, detours, and public warnings.
Safety & Incident Management:
Detect accidents or unusual events from CCTV and social media reports.
Dispatch emergency services quickly to minimize disruption.
Urban Planning Insights:
Use aggregated data to design new roads, pedestrian zones, or bike lanes.
Improve long-term infrastructure planning based on actual usage patterns.

| [5]
|
CO-1; SO-2; BL-2
| b
| Discuss Data Node and Name Node in HDFS.
Introduction to HDFS
HDFS (Hadoop Distributed File System) is the primary storage system of Hadoop.
It follows a Master-Slave architecture:
Master Node: NameNode
Slave Nodes: DataNodes
HDFS stores large files by splitting them into blocks (default 128 MB) and distributing them across multiple nodes for reliability and scalability.

2. NameNode (Master Node)
Role: The NameNode is the central controller of HDFS.
Responsibilities:
Maintains the metadata of the file system:
File names, file permissions
Directory structure
Mapping of blocks to DataNodes
Manages namespace operations:
Create, delete, rename files/directories
Monitors DataNode health via periodic heartbeats.
Handles replication:
Ensures each block is replicated across multiple DataNodes (default 3) for fault tolerance.
Does not store actual data — only metadata.
Important Note: If the NameNode fails, HDFS becomes unavailable unless a Secondary NameNode or High-Availability setup is used.

3. DataNode (Slave Node)
Role: DataNodes are the storage units of HDFS.
Responsibilities:
Store actual data blocks on local disk.
Serve read/write requests from clients.
Periodically send block reports and heartbeats to the NameNode.
Manage replication at the block level (create/delete blocks as instructed by NameNode).
Ensure data durability and availability.
Features:
Runs on commodity hardware.
Can be added or removed easily for scalability.

4. Interaction between NameNode and DataNode
Write Operation:
Client requests NameNode to store a file.
NameNode provides the list of DataNodes for block placement.
Client writes blocks to the DataNodes directly.
DataNodes replicate blocks according to NameNode instructions.
Read Operation:
Client asks NameNode for locations of the required blocks.
NameNode returns the DataNode locations.
Client reads the blocks directly from DataNodes.

| [5]
|
CO- 2; SO-2 ; BL-2
| c
| What is the purpose of a Combiner in MapReduce? How does it help optimize performance? Give an example to illustrate its use.
1. Purpose of a Combiner (2 marks)
A Combiner is an optional mini-reducer in MapReduce.
It aggregates intermediate key-value pairs generated by the Mapper before sending them to the Reducer.
Helps reduce the volume of data transferred over the network (shuffle phase).
Key Point: Combiner does local aggregation on Mapper nodes to optimize performance but does not guarantee final results (Reducer still does the actual computation).

2. How it Optimizes Performance (2 marks)
Reduces network I/O: Fewer intermediate key-value pairs are sent from Mappers to Reducers.
Speeds up processing: Less data for Reducers to handle.
Particularly useful for commutative and associative operations (e.g., sum, count, max).

3. Example: Word Count
Scenario: Counting words in a large text file.
Mapper Output (Intermediate Pairs):
Mapper1: ("data",1), ("science",1), ("data",1)
Mapper2: ("science",1), ("big",1), ("data",1)
Without Combiner:
All intermediate pairs sent to Reducer:
[("data",1), ("science",1), ("data",1), ("science",1), ("big",1), ("data",1)]
With Combiner (local aggregation at Mapper):
Mapper1 Combiner: ("data",2), ("science",1)
Mapper2 Combiner: ("science",1), ("big",1), ("data",1)
Fewer key-value pairs are sent over the network → less shuffle data → faster processing.

| [5]
|
CO- 3; SO- 3; BL-2
| d
| Explain the major issues that impact the effectiveness of Big Data visualization.
Introduction
Big Data visualization helps in understanding patterns and insights from massive, complex datasets. However, its effectiveness can be limited by several issues.

2. Major Issues
Volume of Data
Extremely large datasets can overwhelm visualization tools.
Rendering millions of data points can cause performance lags or crashes.
Variety of Data
Data comes in multiple formats: structured, semi-structured, unstructured.
Integrating heterogeneous data into a coherent visualization is challenging.
Velocity of Data
Real-time data streams (e.g., IoT sensors, social media) require dynamic and continuous updates.
Lag or outdated visuals reduce decision-making effectiveness.
Data Quality (Veracity)
Inaccurate, incomplete, or noisy data can mislead visual interpretations.
Requires preprocessing, cleaning, and validation before visualization.
Complexity of Analysis
High-dimensional or multi-variate data can be difficult to represent in simple charts.
May require advanced visualization techniques (heatmaps, 3D plots, dashboards).
Scalability of Tools
Not all visualization tools can handle Big Data efficiently.
Tools need to scale horizontally or use techniques like sampling or aggregation.
Interpretability
Overly complex or cluttered visuals can confuse users.
Choosing the right type of chart/graph is critical for clarity.

| [5]
|
Q2
CO-3; SO-1; BL-1
| a
| An online education platform wants to recommend courses to students based on their course completion and ratings.
i. Explain how collaborative filtering can help suggest courses to a student.
ii. If two students have rated the same courses similarly, what does high cosine similarity imply?
iii. Suggest a strategy to recommend courses to a new student with no ratings.
Collaborative Filtering for Course Recommendations (4 marks)
Definition:
Collaborative Filtering (CF) is a technique to suggest items (courses) to a user based on the preferences of other similar users.
Assumes that students who agreed in the past will agree in the future.
How it works:
Collect ratings of courses by all students.
Compute similarity between students (user-based CF) or between courses (item-based CF).
Recommend courses that similar students liked but the target student hasn’t taken.
Example:
Student A rated courses [X=5, Y=4].
Student B rated courses [X=5, Y=4, Z=5].
CF recommends course Z to Student A because Student B with similar ratings liked it.

ii. High Cosine Similarity Between Two Students (2 marks)
Cosine similarity measures the angle between two students’ rating vectors.
High cosine similarity implies:
Students’ ratings across courses are very similar.
Their preferences align closely.
Courses liked by one student are likely to be relevant to the other.
Example:
Student A vector: [5,4,0]
Student B vector: [5,4,5]
Cosine similarity ≈ 0.99 → strong alignment → CF recommends Student B’s liked course (Z) to Student A.

iii. Strategy for New Student (Cold Start Problem) (4 marks)
Problem: New students have no prior ratings, so CF cannot be applied.
Strategies:
Content-Based Filtering:
Recommend courses based on the student’s profile: interests, skills, or demographic data.
Example: Student interested in “Data Science” → recommend courses in Python, Machine Learning, etc.
Popularity-Based Recommendations:
Suggest top-rated or most-enrolled courses across the platform.
Hybrid Approach:
Combine content-based and collaborative filtering after initial course completions/ratings.
Onboarding Surveys / Quick Assessment:
Ask the student to rate a few courses or topics during signup to generate initial recommendations.

| [10]
|
CO-1,; SO-; BL-
| b
| Elaborate at least five file formats in HDFS.
Introduction
HDFS (Hadoop Distributed File System) supports multiple file formats, optimized for storage, processing, and analytics. The choice of format affects read/write performance, compression, and compatibility with tools like MapReduce, Hive, and Spark.

1. Text File (TXT / CSV)
Description: Plain-text file format; each line is a record, fields separated by delimiters (comma, tab).
Advantages:
Easy to read and debug.
Compatible with most tools.
Disadvantages:
No schema; parsing large datasets is inefficient.
Use Case: Small datasets, log files, or data exchange between systems.

2. Sequence File
Description: Binary key-value format used internally by Hadoop. Stores data as <key, value> pairs.
Advantages:
Optimized for MapReduce processing.
Supports splitting, enabling parallel processing.
Disadvantages:
Not human-readable.
Use Case: Intermediate storage for Mapper output, or bulk storage of structured data.

3. Avro
Description: Row-based binary format with schema stored in JSON. Supports schema evolution.
Advantages:
Compact and fast serialization/deserialization.
Schema evolution allows adding/removing fields without breaking applications.
Disadvantages:
Less efficient for analytical queries that need only a few columns.
Use Case: Streaming data, data exchange between systems, and records requiring schema evolution.

4. Parquet
Description: Columnar storage format designed for analytical workloads. Stores data column-wise, rather than row-wise.
Advantages:
Efficient for read-heavy queries.
Better compression and reduced I/O for selected columns.
Supports complex nested data types.
Disadvantages:
Row-wise inserts/updates are less efficient.
Use Case: Data warehouses, Hive/Spark SQL analytics, OLAP workloads.

5. ORC (Optimized Row Columnar)
Description: Columnar format optimized for Hive.
Advantages:
High compression (ZLIB/Snappy).
Fast query execution with predicate pushdown.
Efficient for large-scale analytical queries.
Disadvantages:
Not ideal for frequent row-level updates.
Use Case: Hive tables, large-scale analytics, queries with selective columns.

6. JSON
Description: Semi-structured text format using key-value pairs, often nested.
Advantages:
Human-readable and widely used for APIs.
Supports nested and hierarchical data.
Disadvantages:
Larger file size, slower processing compared to binary formats.
Use Case: Web logs, API data ingestion, semi-structured datasets.

7. XML
Description: Semi-structured markup language format.
Advantages:
Supports hierarchical data.
Standardized and self-descriptive.
Disadvantages:
Verbose, high storage overhead, slower parsing.
Use Case: Legacy data exchange, configuration files.

| [10]
|
Q3
CO-2; SO-3; BL-4
| a
| Consider the following dataset :
101 Anjali HR 22
102 Ramesh IT 18
103 Meera Finance 25
104 Tarun IT 20
105 Kavita HR 19
106 Suresh Finance 23
107 Nisha IT 26
Each record represents:
· Employee ID
· Name
· Department
· Days Present (in a month)
Create a PIG script to process the attendance.txt file and answer the following queries:
1. Load the attendance.txt file and display all records.
attendance = LOAD 'attendance.txt' USING PigStorage(',')
AS (EmpID:int, Name:chararray, Department:chararray, DaysPresent:int);
2. Display all employees from the Finance department.
Filter employees in Finance department
finance_employees = FILTER attendance BY Department == 'Finance';

-- Display Finance employees
DUMP finance_employees;
3. Compute the average attendance for each department.
Group by department
dept_group = GROUP attendance BY Department;

-- Calculate average DaysPresent
avg_attendance = FOREACH dept_group GENERATE
group AS Department,
AVG(attendance.DaysPresent) AS AvgDaysPresent;

-- Display average attendance per department
DUMP avg_attendance;
4. Sort employees by days present in ascending order.
-- Sort employees by DaysPresent
sorted_attendance = ORDER attendance BY DaysPresent ASC;

-- Display sorted employees
DUMP sorted_attendance;
5. Display details of employees who have attendance greater than 22 days.
-- Filter employees with DaysPresent > 22
high_attendance = FILTER attendance BY DaysPresent > 22;

-- Display details
DUMP high_attendance;
| [10]
|
CO-3; SO-3; BL-3
| b
| You are a digital marketing intern at a start-up that connects brands with Instagram influencers worldwide. Your task is to design a data visualization dashboard to analyse influencer performance across countries and content categories such as beauty, fitness, travel, and tech. The dataset includes influencer name, country, followers, engagement rate, average likes, comments, shares, and monthly follower growth. The goal is to help brands find the most engaging influencers for collaborations.
Answer the following:
(a) Which visualization techniques would you use to compare influencer performance across countries? (2 marks)
(b) How would you visualize the relationship between follower count and engagement rate? (2 marks)
(c) Suggest a suitable visualization to show the most popular content categories. (2 marks)
(d) How can insights from your dashboard help brands choose the best influencers? (4 marks)
Answer:
Visualization to Compare Influencer Performance Across Countries (2 marks)
Choropleth Map / Geographic Heat Map:
Shows countries colored by average engagement rate, followers, or influencer activity.
Quickly highlights regions with top-performing influencers.
Alternative: Bar chart grouped by country for average engagement, likes, or growth metrics.

(b) Visualize Relationship Between Follower Count and Engagement Rate (2 marks)
Scatter Plot:
X-axis: Follower count
Y-axis: Engagement rate
Each point represents an influencer.
Helps identify whether influencers with higher followers maintain high engagement.
Optional: Add color/size to indicate content category or growth rate for more insight.

(c) Visualize Most Popular Content Categories (2 marks)
Pie Chart or Donut Chart:
Shows proportion of influencers in each content category (Beauty, Fitness, Travel, Tech).
Alternative: Horizontal bar chart ranking categories by average engagement or number of influencers.

(d) How Insights Help Brands Choose the Best Influencers (4 marks)
Targeted Marketing: Brands can identify influencers in specific countries or regions with high engagement.
Category Alignment: Helps choose influencers in relevant content categories to match brand identity (e.g., beauty brand → beauty influencers).
Engagement vs Reach: Scatter plots reveal whether influencers with large followers maintain high engagement, ensuring marketing ROI.
Growth Potential: Monthly follower growth insights allow brands to collaborate with up-and-coming influencers for long-term campaigns.

| [10]
|
Q4
CO-1,; SO-2; BL-3
| a
| Analyze the use of Big Data in predictive maintenance for the manufacturing and transportation sectors, highlighting the differences in data sources, analytics techniques, and operational outcomes.

Introduction
Predictive maintenance uses Big Data analytics to anticipate equipment failures and schedule maintenance before breakdowns occur, reducing downtime and operational costs. Both manufacturing and transportation sectors leverage Big Data, but differ in data sources, analytics approaches, and operational outcomes.

1. Manufacturing Sector
Data Sources:
Sensor data from machines (vibration, temperature, pressure, humidity)
Production logs, machine usage history
Maintenance records and warranty data
Analytics Techniques:
Descriptive Analytics: Monitors current machine health.
Predictive Analytics: Uses machine learning (regression, neural networks) to forecast failures.
Real-time Analytics: Detects anomalies via streaming sensor data.
Operational Outcomes:
Reduced unplanned downtime and maintenance costs
Improved production efficiency and quality
Optimized spare parts inventory
Example: Predicting when a CNC machine or conveyor belt will fail based on vibration patterns.

2. Transportation Sector
Data Sources:
Telematics from vehicles (engine performance, speed, fuel consumption)
GPS and route data
IoT sensors in fleets and infrastructure (e.g., bridges, tracks)
Historical breakdown and maintenance records
Analytics Techniques:
Predictive models (time-series analysis, regression, anomaly detection)
Fleet-wide optimization using IoT and Big Data platforms
Real-time alerts for vehicle performance and safety
Operational Outcomes:
Reduced vehicle breakdowns and accidents
Optimized fleet scheduling and route planning
Lower operational costs and improved customer satisfaction
Example: Predicting bus or truck engine failure before long trips to prevent delays.

3. Key Differences Between Manufacturing and Transportation
Aspect
| Manufacturing
| Transportation
|
Data Sources
| Machines, sensors, production logs
| Vehicles, telematics, GPS, IoT devices
|
Analytics Focus
| Machine-level predictive models
| Fleet-level and vehicle-level predictive models
|
Operational Outcomes
| Maximize uptime, quality, efficiency
| Reduce breakdowns, ensure safety, optimize routes
|
Data Frequency
| High-frequency machine sensor data
| Mixed frequency: real-time telemetry + historical usage
|
Maintenance Scope
| Individual equipment or plant
| Entire fleet or infrastructure network
|

| [10]
|
CO-1,; SO-2; BL-3
| b
| A financial analyst is working with a massive dataset of banking transactions to identify fraudulent activities. Which data visualization techniques would be most effective to detect anomalies or outliers in this big data environment? Explain your choice with a use case.
. Effective Data Visualization Techniques (5 marks)
Scatter Plots
Plot two variables (e.g., transaction amount vs. transaction frequency).
Detects outliers or unusual transactions that deviate from normal clusters.
Box Plots
Displays median, quartiles, and extreme values.
Identifies transactions significantly higher or lower than typical values.
Heatmaps
Shows correlation between variables, such as time of day vs. transaction type.
Helps identify suspicious spikes or unusual patterns.
Time-Series Plots
Tracks transactions over time for each account or region.
Sudden spikes or drops in activity highlight anomalies.
Network Graphs / Node-Link Diagrams
Represents relationships between accounts, transactions, and locations.
Useful for detecting fraud rings, money laundering, or circular transactions.

2. Explanation of Choice (3 marks)
These techniques are effective for Big Data environments because they reduce millions of records into visual patterns, enabling quick detection of anomalies.
They allow analysts to focus on potential fraud cases instead of manually inspecting the entire dataset.
Combination of plots provides a multi-dimensional view of transaction behavior (amount, frequency, time, and relationships).

3. Use Case Example (2 marks)
Scenario: Detect credit card fraud in a dataset of millions of transactions.
Implementation:
Scatter plot: Transaction amount vs. frequency reveals a few extremely high-value transactions outside the normal cluster.
Time-series plot: Shows that these outliers occur at unusual times (e.g., 3 AM).
Network graph: Connects accounts with suspicious transfers, revealing a potential fraud ring.
Outcome: Fraud analysts can prioritize investigation on flagged transactions, reducing false positives and improving detection efficiency.

| [10]
|
Q5
CO-2,; SO-3; BL-4
| a
| Consider the following dataset:
Emp_ID
| Name
| Department
| Rating
| Projects
|
401
| Ankit
| IT
| 4.5
| 5
|
402
| Riya
| HR
| 4.2
| 3
|
403
| Mohan
| Finance
| 4.8
| 6
|
404
| Sneha
| IT
| 4.1
| 4
|
405
| Tara
| HR
| 4.7
| 5
|
406
| Vivek
| Finance
| 4.3
| 2
|
407
| Neha
| IT
| 4.9
| 7
|
Create a Hive table named employee_performance and load the dataset. Then answer the following queries:
1. Create the Hive table employee_performance, load data from employee_performance.txt, and retrieve all records.
CREATE TABLE employee_performance (
EmpID INT,
Name STRING,
Department STRING,
Rating FLOAT,
ProjectsCompleted INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Load data from HDFS file
LOAD DATA INPATH '/user/hive/employee_performance.txt' INTO TABLE employee_performance;

-- Retrieve all records
SELECT * FROM employee_performance;
2. Display all employees from the IT department.
SELECT *
FROM employee_performance
WHERE Department = 'IT';
3. Sort employees based on their rating in descending order.
SELECT *
FROM employee_performance
ORDER BY Rating DESC;
4. Retrieve the names of employees who have worked on more than 4 projects.
SELECT Name
FROM employee_performance
WHERE ProjectsCompleted > 4;
5. Count the number of employees in each department.
SELECT Department, COUNT(*) AS EmployeeCount
FROM employee_performance
GROUP BY Department;
| [10]
|
CO-13; SO-3; BL-4
| b
| An e-commerce company tracks customer clicks, purchase history, and product reviews to recommend products. Identify the Big Data types, explain how analytics supports personalized marketing, and discuss the real-time data processing challenges.
Big Data Types in E-Commerce (3 marks)
The company collects multiple types of Big Data:
Structured Data
Customer purchase history, clicks, product IDs, transaction amounts.
Stored in relational databases or data warehouses.
Semi-Structured Data
Logs, JSON/XML clickstream data, user preferences.
Requires parsing to extract meaningful insights.
Unstructured Data
Product reviews, social media comments, customer feedback.
Requires natural language processing (NLP) or sentiment analysis.

2. How Analytics Supports Personalized Marketing (4 marks)
Behavioral Analysis
Analyzing clickstream and purchase patterns to understand customer interests.
Recommendation Systems
Collaborative Filtering: Suggests products liked by similar users.
Content-Based Filtering: Suggests products similar to previously viewed/purchased items.
Customer Segmentation
Clustering customers based on demographics, preferences, and buying behavior.
Targeted Campaigns
Personalized emails, offers, and notifications based on predicted interests.
Outcome: Increased engagement, higher conversion rates, and improved customer satisfaction.

3. Real-Time Data Processing Challenges (3 marks)
High Volume and Velocity
Millions of clicks and transactions per second require scalable real-time processing systems.
Data Integration
Combining structured, semi-structured, and unstructured data streams in real time is complex.
Low-Latency Processing
Recommendations must be generated instantly to influence current browsing/purchase behavior.
Data Quality and Noise
Clickstream logs and social media data can be incomplete or noisy, affecting analytics accuracy.
Infrastructure & Cost
Real-time processing requires robust Big Data frameworks like Apache Kafka, Spark Streaming, or Flink, which can be expensive and complex to maintain.

| [10]
|
Q6
CO-1; SO-2; BL-3
| a
| An e-commerce company wants to calculate the total sales per product category from transaction logs stored across multiple servers. Describe how the MapReduce programming model can be used to compute these totals efficiently. Discuss how MapReduce ensures scalability when the number of transactions grows.
Using MapReduce to Calculate Total Sales per Product Category (5 marks)
The MapReduce programming model is ideal for processing large datasets distributed across multiple servers. It works in two main phases: Map and Reduce.
Step 1: Map Phase
Each mapper reads a portion of the transaction logs.
For each transaction, the mapper outputs a key-value pair:
Key: Product Category
Value: Transaction Amount
Example: A transaction of $100 for "Electronics" → ("Electronics", 100).
Step 2: Shuffle and Sort
The framework groups all key-value pairs by key (product category) across all mappers.
All amounts for the same category are sent to the same reducer.
Step 3: Reduce Phase
Each reducer receives a list of transaction amounts for a category.
The reducer computes the sum of all amounts for that category.
Output: ("Electronics", 45000), ("Clothing", 32000), etc.
Outcome: Efficient computation of total sales per product category across massive, distributed datasets.

2. How MapReduce Ensures Scalability (5 marks)
Parallel Processing
Multiple mappers process data simultaneously across different servers, reducing overall computation time.
Data Locality
MapReduce tries to run mappers close to where the data resides (HDFS blocks), minimizing network overhead.
Automatic Task Distribution
Hadoop divides data into splits and assigns them to available mappers and reducers, scaling automatically with more nodes.
Fault Tolerance
Failed tasks are re-executed on other nodes, ensuring reliability in large-scale environments.
Elastic Growth
Adding more servers allows the system to handle growing transaction volumes without redesigning the program.
Example:
For 1 million transactions, MapReduce can use 100 mappers.
If transactions increase to 10 million, the framework can scale by adding more nodes and mappers to maintain processing efficiency.

| [10]
|
CO-1; SO-3; BL-4
| b
| Assess the effectiveness of Big Data analytics in combating climate change.
Introduction
Big Data analytics involves processing massive and complex datasets to extract insights for decision-making. In the context of climate change, it can be used to monitor, predict, and mitigate environmental impacts efficiently.

2. Areas Where Big Data Analytics Helps Combat Climate Change (5 marks)
Climate Monitoring and Modeling
Analysis of satellite data, sensor networks, and weather stations to monitor temperature, CO₂ levels, deforestation, and ocean changes.
Helps create accurate climate models and forecasts.
Energy Optimization
Smart grid and energy consumption data enable efficient energy use, reducing carbon footprints.
Predictive maintenance for renewable energy plants ensures optimal energy production.
Disaster Prediction and Management
Big Data from IoT sensors, historical weather, and social media can predict extreme events like floods, hurricanes, or droughts.
Enables timely evacuation and resource allocation.
Sustainable Agriculture
Data from soil sensors, drones, and weather forecasts optimize water usage, fertilizer application, and crop selection, reducing environmental impact.
Carbon Emission Tracking
Companies and governments can monitor emissions in real time to identify high-emission activities and implement reduction strategies.

3. Effectiveness and Benefits (3 marks)
Informed Policy Making: Data-driven insights support government regulations and climate policies.
Early Warning Systems: Predictive analytics improves resilience to climate events.
Efficiency Improvements: Optimizes energy, transportation, and resource management.
Global Collaboration: Shared datasets and analytics enable coordinated climate action worldwide.

4. Challenges / Limitations (2 marks)
Data Volume & Variety: Integrating heterogeneous datasets from satellites, sensors, and social media is complex.
Real-Time Processing: High-velocity climate data requires fast processing frameworks.
Data Quality & Reliability: Inaccurate or missing data can mislead predictions.
Infrastructure & Costs: Big Data platforms and storage for climate datasets are resource-intensive.

| [10]
|
Q7
CO-1; SO-1 BL-1
| a
| Discuss features of HBase. How is it different from Google Bigtable?

Features of HBase (6 marks)
HBase is a distributed, scalable, NoSQL database built on top of Hadoop HDFS. Its key features include:
Column-Oriented Storage
Data is stored in column families, enabling efficient reads and writes for sparse datasets.
Scalability
Horizontally scalable across thousands of commodity servers.
Real-Time Read/Write Access
Supports low-latency random reads and writes, unlike HDFS which is optimized for batch processing.
Automatic Sharding (Region Splitting)
Tables are split into regions, automatically distributed across region servers to balance load.
Versioning of Data
Each cell can store multiple versions of data identified by timestamps.
Integration with Hadoop Ecosystem
Works seamlessly with MapReduce, Hive, Pig, Spark, and HDFS for analytics.
Fault Tolerance
Leverages HDFS replication and automatic failover for region servers.
Schema Flexibility
Allows dynamic addition of columns in column families; rows can have variable columns.

2. Differences Between HBase and Google Bigtable (4 marks)
Feature
| HBase
| Google Bigtable
|
Platform
| Open-source, runs on Hadoop/HDFS
| Proprietary, cloud-based (Google Cloud)
|
Storage
| Uses HDFS for persistence
| Uses Google File System (GFS)
|
API/Language Support
| Java API, REST, Thrift
| Proprietary API, client libraries in multiple languages
|
Deployment
| On-premises or cloud
| Managed by Google Cloud (serverless)
|
Ecosystem Integration
| Hadoop ecosystem: MapReduce, Hive, Pig, Spark
| Limited to Google Cloud tools (BigQuery, Dataflow)
|
Replication & Fault Tolerance
| HDFS replication; region server failover
| Built-in high availability, multi-zone replication
|
Cost
| Free, open-source
| Paid, cloud-based service
|

|
|
|

| [10]
|
CO-1; SO-2; BL-3
| b
| Explain the concept of Big Data Analytics. How does it differ from traditional analytics? Discuss the types of analytics (descriptive, predictive, and prescriptive) with examples.
Concept of Big Data Analytics (2 marks)
Big Data Analytics (BDA) is the process of examining large and complex datasets (structured, semi-structured, unstructured) to discover patterns, trends, and insights for better decision-making.
Example: An e-commerce site analyzing clicks, purchases, and reviews to recommend products.

2. Difference from Traditional Analytics (1 mark)
Feature
| Traditional Analytics
| Big Data Analytics
|
Data Volume
| Small to medium
| Massive (TBs to PBs)
|
Data Type
| Structured only
| Structured, semi-structured, unstructured
|
Processing
| Batch
| Real-time or near real-time
|
Tools
| SQL, Excel
| Hadoop, Spark, NoSQL, AI/ML
|

3. Types of Analytics (2 marks)
Descriptive Analytics: Understand what happened.
Example: Monthly sales report.
Predictive Analytics: Forecast what will happen.
Example: Predict customer churn.
Prescriptive Analytics: Recommend actions to achieve outcomes.
Example: Optimize pricing strategy in retail.

| [5]
|
CO-1; SO-2; BL-3
| c
| You are given the ratings of 4 users on 5 movies. Compute the cosine similarity between User1, User2 and User3. Compute cosine similarity. Check whether User1 is similar to User2 or User3?
Movie
| User1
| User2
| User3
| User4
|
M1
| 5
| 4
| 3
| 5
|
M2
| 3
| 5
| 2
| 4
|
M3
| 0
| 2
| 0
| 1
|
M4
| 1
| 0
| 1
| 0
|
M5
| 4
| 3
| 5
| 4
|
Cosine Similarity Formula
For two users Aand B:
Cosine Similarity=i(Ai⋅Bi)iAi2⋅iBi2

Where Aiand Biare ratings for movie i.

2. User Vectors
Movie
| User1
| User2
| User3
|
M1
| 5
| 4
| 3
|
M2
| 3
| 5
| 2
|
M3
| 0
| 2
| 0
|
M4
| 1
| 0
| 1
|
M5
| 4
| 3
| 5
|
So, vectors are:
U1=[5,3,0,1,4]
U2=[4,5,2,0,3]
U3=[3,2,0,1,5]

3. Compute Cosine Similarity
Step 1: User1 & User2
Dot product:
5*4+3*5+0*2+1*0+4*3=20+15+0+0+12=47

Magnitude:
∣∣U1∣∣=52+32+02+12+42=25+9+0+1+16=51≈7.141
∣∣U2∣∣=42+52+22+02+32=16+25+4+0+9=54≈7.348

Cosine Similarity:
cos⁡(U1,U2)=477.141*7.348≈4752.49≈0.895

Step 2: User1 & User3
Dot product:
5*3+3*2+0*0+1*1+4*5=15+6+0+1+20=42

Magnitude:
∣∣U3∣∣=32+22+02+12+52=9+4+0+1+25=39≈6.245

Cosine Similarity:
cos⁡(U1,U3)=427.141*6.245≈4244.60≈0.942

4. Interpretation
Cosine similarity values range from 0 to 1 (higher = more similar).
cos⁡(U1,U2)≈0.895,cos⁡(U1,U3)≈0.942
Conclusion: User1 is more similar to User3 than to User2.

Answer:
Cosine Similarity:
User1 & User2 = 0.895
User1 & User3 = 0.942
Most similar user to User1: User3

| [5]
|
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper de7dded02769

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_Computer_7047/Big Data Analytics/ANS_Big Data Analytics(702DB0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (18 pages), mean OCR confidence 39.1
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/MBA Tech (Comp)/MBA Tech (DS)
Year: III / IV/Semester VI/Semester VIII(Exam Year: 2025-2026)
Subject: Big Data Analytics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1
Answer briefly:   [20]
a.   Describe the role of HDFS in Big Data.
Five points each 1 mark.
1. Core Storage and Distributed Architecture
HDFS is the backbone of Hadoop’s storage, providing a way to store massive
amounts of data across a cluster of computers. Instead of relying on a single
large server, it uses a distributed architecture where data is spread across many
nodes, allowing the system to scale from a single server to thousands of
machines.
2. Data Partitioning (Block Storage)
HDFS manages large files by splitting them into smaller, fixed-size units called
blocks.
•   Size: Common block sizes are 128 MB (preferred) or 64 MB.
• Mechanism: For example, a 1 GB file is divided into 8 blocks of 128 MB,
which are then distributed across different machines in the cluster so
CO-1; BL-1   they can be read and processed simultaneously.   [5]
3. Fault Tolerance through Replication
In a Big Data environment using low-cost commodity hardware, machine
failures are common. HDFS ensures data reliability by automatically replicating
each block multiple times—usually 3 replicas—across different nodes. If one
node crashes, the system seamlessly retrieves the data from another node
containing a replica, preventing data loss.
4. High Throughput and Data Locality
HDFS is optimized for batch processing rather than interactive user tasks,
providing high-throughput access to application data. A critical role it plays is
enabling Data Locality: instead of moving massive datasets over the network to
a program, Hadoop moves the processing program to the data stored on the
HDFS nodes. This significantly reduces network traffic and increases processing
speed.
5. Cost-Effectiveness and Management
********** 1 **********
--- page 2 ---
HDFS allows organizations to store Big Data cheaply by running on low-cost,
commodity hardware. It sits on top of local file systems and provides a suite of
HDFS Commands (like put, get, ls, and mkdir) to manage, monitor, and check
the health of the distributed files.
b.   Describe the working of NameNode and DataNode in HDFS.
Working of namenode- 3 marks
Working of datanode- 2 marks
In the Hadoop Distributed File System (HDFS), the architecture follows a
master-slave model where the NameNode acts as the master and DataNodes
act as slaves to manage storage across a cluster.
1. Working of the NameNode (Master)
The NameNode is the "brain" of the HDFS and is responsible for managing the
file system's metadata and governing access.
• Namespace Management: It maintains the hierarchical structure of
files and directories, similar to a Linux file system.
• Metadata Storage: It stores information about the files, such as their
size, permissions, and, most importantly, the mapping of file blocks to
specific DataNodes.
•   Access Control: It regulates client access to files and handles requests
to open, close, rename, or delete files and directories.
• Request Validation: When a client wants to write data, the NameNode
checks for permissions and ensures the file does not already exist
before providing a list of suitable DataNodes for storage.
2. Working of the DataNode (Slave)
CO-3; BL-2   DataNodes are the worker nodes that perform the actual task of storing and   [5]
retrieving data blocks.
•   Block Storage: They store data in fixed-size units called blocks (typically
128MB or 256MB).
• Data Operations: They handle read and write requests from HDFS
clients and perform block creation, deletion, and replication as
instructed by the NameNode.
•   Replication Pipeline: During a write operation, DataNodes work in a
pipeline. DataNode 1 receives data from the client, stores it, and
forwards it to DataNode 2, which then forwards it to DataNode 3 (based
on the replication factor).
• Data Integrity: Each DataNode is responsible for verifying the integrity
of its stored data using checksums during read/write operations to
detect any corruption.
3. Interaction Between NameNode and DataNode
The interaction ensures the system remains reliable and efficient:
• Write Coordination: The NameNode provides the client with the
locations (IP addresses) of DataNodes. The client then streams data
directly to those DataNodes to avoid bottlenecking the NameNode.
• Acknowledgment: Once DataNodes successfully store a block, they
send an acknowledgment (ACK) back through the pipeline to the client,
which then informs the NameNode to finalize the metadata.
********** 2 **********
--- page 3 ---
Fault Tolerance: If a DataNode or a block fails, the NameNode detects this and
coordinates with other DataNodes to create new replicas from healthy copies,
ensuring high availability
c.   Define execution modes used in Apache Pig. Compare Pig with MapReduce.
Execution mode [2 Marks]
Comparison between Pig and MapReduce [3 Marks]
Apache Pig Execution Modes
Local Mode
•   In this mode, all the files are installed and run from your local
host and local file system. There is no need of Hadoop or HDFS.
This mode is generally used for testing purpose.
MapReduce Mode
• MapReduce mode is where we load or process the data that exists
in the Hadoop File System (HDFS) using Apache Pig. In this
mode, whenever we execute the Pig Latin statements to process
the data, a MapReduce job is invoked in the back-end to perform
a particular operation on the data that exists in the HDFS.
Difference between Pig and MapReduce
Apache Pig   MapReduce
It is a compiled
It is a scripting language.   programming
CO-2; BL-3   language.   [5]
Abstraction is at higher   Abstraction is at
level.   lower level.
It have less line of code as
Lines of code is more.
compared to MapReduce.
More development
Less effort is needed for
efforts are required
Apache Pig.
for MapReduce.
As compared to Pig
Code efficiency is less as
efficiency of code is
compared to MapReduce.
higher.
Pig provides built in
Hard to perform data
functions for ordering,
operations.
sorting and union.
********** 3 **********
--- page 4 ---
It allows nested data types   It does not allow
like map, tuple and bag   nested data types
d.   What is cosine similarity in recommendation systems?
Cosine similarity is a measure used in recommendation systems to determine
how similar two users or items are by comparing their rating vectors. It
calculates the cosine of the angle between two vectors.
𝐴⋅𝐵
Cosine Similarity =
∥𝐴∥×∥𝐵∥
Where:
• 𝐴⋅𝐵= dot product of vectors
• ∥𝐴∥, ∥𝐵∥= magnitudes of vectors
Working
Represent users/items as vectors of ratings
CO-2; BL-2   • Compute similarity between vectors   [5]
• Value ranges from 0 to 1:
o 1 → very similar
o 0 → not similar
Example
User A = [5, 4, 0]
User B = [4, 5, 0]
•   Cosine similarity will be high, indicating similar preferences
Used to recommend items liked by similar users.
Applications
•   Collaborative filtering
• Movie and product recommendation systems
a.   Describe data ingestion process using Flume and Sqoop.
Q2
[10]
CO-3; BL-1   Data ingestion with flume and sqoop each 5 marks
********** 4 **********
--- page 5 ---
Data ingestion in Hadoop is the process of collecting data from various sources
(like logs, databases, or sensors) and moving it into a central system like HDFS
for processing and analysis. The specific steps for the two primary tools, Sqoop
and Flume, are as follows:
1. Data Ingestion with Apache Sqoop (Batch/Structured Data)
Sqoop is designed to transfer structured data between Relational Database
Management Systems (RDBMS) and HDFS.
Steps in the Sqoop Workflow:
1. Command Submission: The user issues a Sqoop import or export
command via the client terminal.
2. Job Translation: Sqoop converts the command into a MapReduce job
to enable large-scale parallel data transfer.
3. Framework Trigger: The MapReduce job is submitted to the Hadoop
cluster.
4. Establish Connection: Sqoop uses JDBC to establish a secure
connection with the source RDBMS (e.g., MySQL or Oracle).
5. Data Splitting: The database table is divided into logical "splits" based
on a primary key or specific column.
6. Parallel Transfer: Multiple Mappers (default is 4) independently and
simultaneously pull or push their assigned chunks of data.
7. HDFS Writing/Reading: During an import, the mappers write the data
into HDFS in formats such as text, Avro, or sequence files.
8. Job Completion: Once all mappers finish, Sqoop reports the final status
(success or failure) to the client.
Example: Transferring customer transaction tables from a MySQL database
into an HDFS directory for monthly batch reporting.
2. Data Ingestion with Apache Flume (Streaming/Semi-Structured Data)
Flume is optimized for the continuous collection and movement of log and
event data.
Steps in the Flume Workflow:
1. Event Generation: An external source, such as a web server, produces
a "Flume Event" (a byte array payload with optional headers).
2. Source Reception: The Flume Source component receives these events
from the generator over the network.
3. Channel Buffering: The Source sends the event to a Flume Channel,
which acts as a temporary buffer or store (often using the local file
system for reliability).
4. Sink Extraction: The Flume Sink removes the event from the channel.
5. Centralized Storage: The Sink writes the event to a centralized
repository like HDFS or Apache HBase. In complex setups, the Sink may
forward the event to the Source of another agent in a "multi-hop" flow.
Example: An e-commerce website (like Amazon) streaming live web server logs
into HDFS to perform real-time analysis of customer behavior in a specific
geographic region.
********** 5 **********
--- page 6 ---
b.   Explain user-based and item-based collaborative filtering techniques. Compare
their advantages, limitations, and applications in recommendation systems.
User based and item based collaborative filtering- each 4 marks
Comparison- 2 marks
Collaborative Filtering (CF) is a recommendation technique that predicts user
preferences based on past behavior. It is widely used in systems like Netflix and
Amazon.
Two main approaches are User-Based and Item-Based Collaborative
Filtering.
User-Based Collaborative Filtering
•   Finds users with similar preferences using similarity measures (e.g.,
cosine similarity).
• Recommends items liked by similar users.
Example:
•   If User A and User B have similar movie ratings, and User B likes Movie
X, then Movie X is recommended to User A.
CO-2; BL-2   Advantages:   [10]
• Simple and intuitive
•   Personalized recommendations
Limitations:
• Not scalable for large datasets
•   Suffers from sparsity (few common ratings)
Item-Based Collaborative Filtering
Working Principle:
•   Finds similarity between items instead of users.
• Recommends items similar to those the user has liked.
Example:
•   If a user likes Movie A and Movie A is similar to Movie B, then Movie
B is recommended.
Advantages:
• More scalable and efficient
•   Stable recommendations over time
Limitations:
•   Less personalized than user-based
•   Requires computation of item similarity
********** 6 **********
--- page 7 ---
a.   Draw and explain Hadoop architecture. What are the additional benefits that
YARN brings into Hadoop?
•   Architecture diagram → 2 Marks
• HDFS explanation → 4 Marks
• YARN explanation → 2 Marks
•   Benefits of YARN → 2 Marks
HDFS (Storage Layer)
Components:
• NameNode (Master): Stores metadata (file names, block locations),
Manages file system operations
• DataNode (Slave): Stores actual data blocks, Performs read/write
operations
Key Features:
Data is split into blocks and distributed across nodes
Replication ensures fault tolerance
High scalability and reliability
YARN (Processing Layer)
Components:
• ResourceManager (Master): Allocates cluster resources, Manages
Q3   scheduling
• NodeManager (Slave): Manages resources on each node, Executes   [10]
CO-1; BL-2
tasks
•   ApplicationMaster: Manages a specific application/job, Negotiates
resources from ResourceManager
MapReduce (Processing Model)
Divides job into:
Map tasks → Process input data
Reduce tasks → Aggregate results
Runs on top of YARN for distributed processing
Additional Benefits of YARN in Hadoop
•   Better Resource Management
Separates resource management from job scheduling
Efficient utilization of cluster resources
•   Scalability
Supports large clusters (thousands of nodes)
Handles multiple applications simultaneously
• Improved Performance
Parallel execution of multiple jobs
Reduces bottlenecks of JobTracker (in Hadoop 1.x)
•   Fault Tolerance
Automatically restarts failed tasks
Ensures continuous execution
• Dynamic Resource Allocation
Allocates resources based on demand
Supports container-based execution
********** 7 **********
--- page 8 ---
b.
Write commands and outputs for the following using Hive
•   Create database ‘Sales’ and table ‘Order_Details’and Customer with
(Order_id (int), Customer_id (int), Amount (int), Order_date (date)) and
(Customer_id (int), Name(String), Age (int), City (String)).
•   Insert or load the following data in the respective tables.
• Show number of orders belongs to the same customer id.
•   Find customer name and city who has order amount > 200 and order
after 2023-08-03
Customer_id Name   Age   City
1   Amit   23   Agra
2   Reena   65   Kota
Mumba
3   Shneha   23
i
4   Ritu   58   Delhi
5   Jeet   46   Bihar
Customer_
Order_id   Amount   Order_date
id
101   1   250.00   2023-08-01
102   2   150.00   2023-08-03
103   3   400.00   2023-08-05
104   1   300.00   2023-08-10
105   4   100.00   2023-08-15
106   5   200.00   2023-08-20
CO-2; BL-3   [10]
107   2   180.00   2023-08-25
Creating database and table – 3 Marks
Loading data and showing the output – 3 Marks
Group by with customer id and showing the output – 2 Marks
Finding common customer name and city and showing the output – 2
Marks
CREATE DATABASE Sales;
CREATE TABLE IF NOT EXISTS Order_Details (Order_id int,
Customer_id int, Amount int, Order_date date)
COMMENT ‘Order’
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ‘,’;
CREATE TABLE IF NOT EXISTS Customers (Customer_id int, Name
String, Age int, City String)
COMMENT ‘Customer_Details’
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ‘,’;
INSERT INTO Order_Details values (101,1,250,'2023-08-01');
OR
********** 8 **********
--- page 9 ---
LOAD DATA LOCAL INPATH ‘/home/hive/Order_Details.txt’ INTO
TABLE Order_Details;
Select * from Order_Details;
INSERT INTO Customers values (1,’Amit’,23,'Agra');
OR
LOAD DATA LOCAL INPATH ‘/home/hive/Customers.txt’ INTO
TABLE Customers;
Select * from Customers;
SELECT Count(Order_id) FROM Order_Details GROUP BY
Customer_id;
SELECT c.Name, c.City FROM Customers c JOIN Order_Details o
ON (c.Cutomer_id = o. Cutomer_id) WHERE Amount >200 AND
Order_date >2023-08-03 ;
a.   Explain the major challenges in big data visualization, including scalability, data
volume, velocity, variety, and data complexity. Suggest possible solutions to
overcome these challenges.
Big data visualization challenges with solution- each 2 marks
Scalability:
Challenge: Visualization tools and techniques need to scale effectively as the
size of the data grows.
Technique: Use scalable visualization frameworks and distributed computing
resources. Tools like D3.js and Apache Superset can handle large-scale
Q4   visualizations efficiently.
[10]
CO-1; BL-3
Data Volume:
•   Challenge: Handling and visualizing massive volumes of data
can lead to performance issues and make it difficult to extract
meaningful insights.
•   Technique: Use of sampling methods to represent a subset of
the data, or data reduction techniques like aggregation and
filtering to manage volume.
Data Variety:
•   Challenge: Big data comes in various formats (structured, semi-
structured, unstructured) and from different sources, which can
complicate integration and visualization.
********** 9 **********
--- page 10 ---
•   Technique: Employ data preprocessing techniques to normalize
and integrate diverse data sources, and use visualization tools
that support multiple data formats.
Data Velocity:
•   Challenge: The speed at which data is generated and needs to be
processed can be overwhelming, especially in real-time or near-
real-time applications.
•   Technique: Utilize stream processing and real-time analytics
platforms to handle and visualize live data.
Data Complexity:
Challenge: Complex datasets with multiple dimensions and relationships can be
difficult to represent clearly.
Technique: Apply dimensionality reduction techniques like Principal
Component Analysis (PCA) to simplify the data. Use advanced visualization
methods like multi-dimensional charts or interactive dashboards.
b.   Design the MapReduce architecture to count word occurrences from: “Machine
learning improves data analysis. Data analysis and machine learning are related”
Input: machine learning improves data analysis
data analysis and machine learning are related
Map Phase
Mapper Logic: Each word → (word,1)
(machine,1) (learning,1) (improves,1) (data,1) (analysis,1)
(data,1) (analysis,1) (and,1) (machine,1) (learning,1) (are,1) (related,1)
Shuffle and Sort Phase
Group same words together:
CO-1; BL-2   analysis → (1,1)   [10]
and → (1)
are → (1)
data → (1,1)
improves → (1)
learning → (1,1)
machine → (1,1)
related → (1)
Reduce Phase
Sum values for each word:
(analysis,2)
(and,1)
(are,1)
(data,2)
(improves,1)
********** 10 **********
--- page 11 ---
(learning,2)
(machine,2)
(related,1)
• Mapper: Converts each word into (word,1)
•   Shuffle & Sort: Groups identical words
•   Reducer: Aggregates counts
diagram -2 Mark
Map phase -3 Marks
Shuffle & Sort - 3 Marks
Reduce phase - 2 Marks
a.
Write commands for the following using Pig
• Create table Employee with (Id (int), Name (char array), Age
(int), Gender (char array), Salary (int)).
• Load the data into Employee. (Assume file and path)
• Gropy by the data with age and show the output
• Write a query using FILTER
• Write a query using FOREACH
• Write a query using STORE
Id   Name   Age   Gender   Salary
1201   Gopal   45   Male   50,000
1202   Manisha   40   Female   51,000
1203   Khalil   34   Male   30,000
1204   Prasanth   30   Male   30,000
1205   Kiran   20   Male   40,000
Q5
1206   Laxmi   25   Female   35,000   [10]
CO-2; BL-3
1207   Bhavya   20   Female   15,000
Creating and Load table – 2 Marks
Group by data – 2 Marks
Query using FILTER – 2 Marks
Query using FOREACH – 2 Marks
Query using STORE – 2 Marks
Employee = LOAD 'Pig_Data/employee_data.txt'
USING PigStorage(',') AS ( Id:int, Name:chararray, Age:int,
Gender:chararray, Salary:int);
STORE Employee INTO 'Pig_Output' USING PigStorage (',');
hdfs dfs -ls Pig_Output
hdfs dfs -cat pig_Output/part-m-00000
Group_data = GROUP Employee by Age;
********** 11 **********
--- page 12 ---
Dump Group_data;
Clean_data = FILTER Employee BY Id IS NOT NULL AND Name IS
NOT NULL;
Dump Clean_data;
Record_count = FOREACH (GROUP Clean_data ALL) GENERATE
COUNT(Clean_data);
Dump Record_data;
b.   Discuss various existing data visualization techniques such as bar charts, line
graphs, scatter plots, heatmaps, and dashboards. Compare their suitability for
different types of data.
Data visualization techniques are used to represent data graphically, making it
easier to understand trends, patterns, and relationships in big data analytics.
Types of Visualization Techniques
A. Bar Chart (2 Marks)
• Used to compare values across different categories.
•   Suitable for categorical data.
Example:
• Comparing sales of different products.
Best for discrete comparisons.
CO-1; BL-3   [10]
Line Graph (2 Marks)
• Shows trends over time.
•   Suitable for time-series data.
Example:
•   Stock prices over months.
Best for continuous data and trend analysis.
C. Scatter Plot (2 Marks)
•   Displays relationship between two variables.
•   Suitable for numerical data.
Example:
•   Height vs weight correlation.
Useful for identifying patterns and outliers.
D. Heatmap (2 Marks)
********** 12 **********
--- page 13 ---
• Uses color intensity to represent values.
•   Suitable for matrix or high-dimensional data.
Example:
•   Correlation matrix of variables.
Helps in spotting patterns quickly.
E. Dashboard (2 Marks)
• Combines multiple visualizations into a single interface.
•   Suitable for real-time monitoring and decision-making.
Example:
•   Business KPI dashboard.
Provides comprehensive insights.
a.   Explain classification and clustering with example.
Classification- 5 marks
Clustering- 5 marks
Classification
Classification is a supervised learning technique used to assign data into
predefined classes based on labeled training data.
Working:
• Model is trained on labeled dataset
•   Learns relationship between input and output
•   Predicts class label for new data
Q6
Example:   [10]
CO-2; BL-3
• Email classification: Spam or Not Spam
•   Student result: Pass or Fail
Algorithms Used:
•   Decision Tree
• Naïve Bayes
•   Support Vector Machine
Characteristics:
•   Requires labeled data
•   Predictive in nature
•   Output is discrete (categories)
Clustering
********** 13 **********
--- page 14 ---
Clustering is an unsupervised learning technique that groups similar data points
into clusters without predefined labels.
Working:
•   Finds similarity among data points
• Groups similar objects together
• No prior knowledge of classes
Example:
• Customer segmentation: grouping customers based on buying behavior
• Grouping news articles by topic
Algorithms Used:
• K-means
•   Hierarchical clustering
• DBSCAN
Characteristics:
• No labeled data required
•   Descriptive in nature
•   Output is clusters/groups
b.   Evaluate how spatial-temporal data analytics can improve intelligent
transportation systems, including real-time traffic monitoring and smart city
planning. Compare its performance with conventional statistical approaches.
Spatial-temporal data analytics combines location (spatial) and time-based
(temporal) information to analyze dynamic transportation systems. It plays a
crucial role in enhancing Intelligent Transportation Systems (ITS) and
enabling smart city development.
Role in Intelligent Transportation Systems (ITS)
1. Real-Time Traffic Monitoring
• Uses GPS, sensors, cameras, and mobile data
CO-1; BL-3   [10]
•   Provides live traffic updates (congestion, speed, incidents)
•   Enables dynamic route optimization and navigation
2. Traffic Prediction and Management
•   Analyzes historical + real-time data
•   Predicts traffic congestion and peak hours
•   Helps in adaptive traffic signal control
3. Accident Detection and Response
•   Detects anomalies in traffic patterns
•   Enables quick emergency response and rerouting
Role in Smart City Planning
********** 14 **********
--- page 15 ---
•   Helps in infrastructure planning (roads, flyovers, metro routes)
•   Supports public transport optimization
• Reduces pollution through efficient traffic flow
•   Assists in urban mobility planning and policy decisions
Advantages of Spatial-Temporal Analytics
•   Real-time decision making
•   High accuracy and predictive capability
•   Efficient traffic flow and reduced congestion
•   Better resource utilization
Comparison with Conventional Statistical Approaches
Aspect   Conventional Methods Spatial-Temporal Analytics
Data Type   Static, historical   Real-time + historical
Processing Periodic analysis   Continuous analysis
Accuracy   Moderate   High
Prediction Limited   Advanced predictive models
Adaptability Low   Dynamic and adaptive
introduction -2 Mark
Real-time traffic monitoring - 2 Marks
Traffic prediction / management - 2 Marks
Smart city planning - 2 Marks
Comparison with traditional methods -2 Marks
a.   Evaluate how Big Data is transforming the healthcare industry with respect to
clinical decision support systems, medical imaging analysis, and epidemic
outbreak prediction. Compare it with traditional healthcare data management
approaches.
Big Data is revolutionizing healthcare by enabling advanced analytics and
improving decision-making compared to traditional methods.
Q7
[10]
CO-1; BL-3   Key Transformations:
1. Clinical Decision Support Systems (CDSS)
o Provides data-driven recommendations to doctors
o Improves diagnosis accuracy
2. Medical Imaging Analysis
o Uses AI/ML for analyzing X-rays, MRI, CT scans
o Faster and more accurate detection
********** 15 **********
--- page 16 ---
3. Epidemic Outbreak Prediction
o Analyzes population data to predict disease spread
o Helps in early intervention and planning
Comparison with Traditional Systems:
Aspect   Traditional Approach Big Data Approach
Data Type   Limited, structured   Large, diverse (structured + unstructure
Processing   Manual / slow   Automated / real-time
Accuracy   Moderate   High
Decision Making Reactive   Predictive & proactive
Introduction - 2 Mark
CDSS explanation - 2 Marks
Medical imaging - 2 Marks
Epidemic prediction - 2 Marks
Comparison table - 2 Marks
b.   Discuss the challenges of imbalanced datasets. Explain techniques such as
oversampling, undersampling, SMOTE, and cost-sensitive learning with
examples.
Challenges of imbalanced datasets-4 marks
Techniques -6 marks
An imbalanced dataset is one where the number of instances in different classes
is unequal (e.g., 95% non-fraud and 5% fraud cases). This imbalance can bias
machine learning models toward the majority class.
Challenges of Imbalanced Datasets
CO-2; BL-2   [10]
1. Biased Predictions
• Models tend to favor the majority class.
•   Minority class is often ignored.
2. Accuracy Paradox
• High accuracy but poor performance on minority class.
• Example: 95% accuracy but no fraud detected.
3. Poor Generalization
• Model fails to learn patterns of minority class.
4. Evaluation Issues
• Accuracy is misleading; better metrics needed (precision, recall, F1-
score).
********** 16 **********
--- page 17 ---
Techniques to Handle Imbalanced Data
Oversampling
Description:
•   Increases the number of minority class instances by duplication.
Example:
•   Fraud cases increased from 100 → 500 by repeating samples.
Advantages:
• Improves minority class learning
Disadvantages:
•   Risk of overfitting
Undersampling
Description:
• Reduces the number of majority class samples.
Example:
• Reduce non-fraud cases from 10,000 → 1,000
Advantages:
•   Faster training
Disadvantages:
• Loss of important information
SMOTE (Synthetic Minority Over-sampling Technique)
Description:
•   Generates synthetic minority samples using nearest neighbors.
Example:
•   Creates new fraud cases based on existing ones instead of duplication.
Advantages:
• Reduces overfitting compared to oversampling
Disadvantages:
• May create noisy samples
Cost sensitive learning
Description:
•   Assigns higher cost to misclassifying minority class.
Example:
•   Misclassifying fraud is penalized more than non-fraud.
Advantages:
• Improves minority class detection
********** 17 **********
--- page 18 ---
FR ICR 7] QA HH
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 73b2f4644308

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_Computer_7047/Big Data Analytics/ANS_Big Data Analytics(702DB0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/MBA Tech (Comp)/MBA Tech (DS)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Big Data Analytics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1
Answer briefly   [20]
a.   Describe the major components of Apache Hadoop architecture and
explain their functions.
Apache Hadoop architecture consists of several key components that work
together to provide a distributed environment for storing and processing large
datasets. According to the sources, the architecture is fundamentally divided
into core layers and supporting utilities:
Core Components
At its core, the Hadoop architecture is built upon two primary layers, though
modern versions include YARN as a critical third layer for resource
management:
1. Hadoop Distributed File System (HDFS): This is the storage layer of the
architecture. It is a distributed file system designed to run on
CO-1; BL-1   commodity hardware, providing high-throughput access to data. HDFS   [5]
splits large files into smaller fixed-size blocks (typically 128 MB) and
distributes them across various nodes in a cluster. It ensures fault
tolerance by automatically creating multiple replicas of these blocks.
2. MapReduce: This is the processing/computation layer. It is a parallel
programming model that divides tasks into two main phases: the Map
phase (which processes data into key-value pairs) and the Reduce phase
(which aggregates those results). It allows for the efficient processing
of multi-terabyte datasets across thousands of nodes.
3. YARN (Yet Another Resource Negotiator): Introduced in later versions
of Hadoop (Hadoop 2.0), YARN serves as the cluster resource
management layer. It is responsible for managing and scheduling
computing resources in the cluster, separating the management of
resources (via the ResourceManager) from task execution (via
NodeManagers).
********** 1 **********
--- page 2 ---
4. Hadoop Common (Utilities): These are the common utilities and
libraries that support the other Hadoop modules.
b.   Illustrate the role of Flume in data ingestion.
Apache Flume is a highly reliable, distributed, and configurable data ingestion
service in the Hadoop ecosystem designed specifically for collecting,
aggregating, and moving large volumes of streaming data into a centralized
data store.
1. Purpose and Data Types
Flume is primarily used to ingest semi-structured data, such as log files and
events, from various sources to HDFS or Apache HBase. It is optimized for high-
speed streaming, making it ideal for:
• Log Data: Copying logs from multiple web servers to Hadoop for
analysis (e.g., customer behavior on e-commerce sites).
•   Social Media Events: Importing huge volumes of data produced by
platforms like Facebook and Twitter.
2. Core Architecture: The Flume Agent
The ingestion process is managed by an independent daemon process called an
Agent (running on a JVM). A Flume Agent consists of three main components:
•   Source: Receives events from external data generators   (like
CO-3; BL-2   WebServers) and processes them into a format Flume understands.   [5]
•   Channel: Acts as a temporary storage or buffer that holds the event
until it is consumed by the sink. It can use the local file system for
storage to ensure data isn't lost.
•   Sink: Removes the event from the channel and stores it in a centralized
repository like HDFS.
3. Reliability and Data Flow
• Mediator Role: When data is produced faster than it can be written to
storage, Flume acts as a mediator to provide a steady, managed flow.
•   Transactional Delivery:   It uses channel-based transactions to
guarantee reliable message delivery between the sender and receiver.
•   Scalability: Flume can be scaled horizontally to handle increasing data
loads from multiple servers immediately into Hadoop.
4. Flexible Data Routing
Flume supports complex data flows, including:
•   Multi-hop flows: Forwarding data through multiple agents.
•   Fan-in/Fan-out: Consolidating data from many sources into one
destination or distributing one source to many destinations.
Contextual Routing: Directing data based on its content or context
c.   Compare Hbase and RDBMS.
CO-2; BL-3   [5]
Feature   Apache HBase   RDBMS
Data Model   Column-oriented (NoSQL)   Table-based (rows & colum
********** 2 **********
--- page 3 ---
Schema   Schema-less / flexible   Predefined schema (fixed)
Scalability   Horizontally scalable (distributed)   Vertically scalable (limited)
Data Type   Handles structured & unstructured data Mainly structured data
Query Language   Uses APIs / commands (no SQL)   Uses SQL
Transactions   Limited (no full ACID)   Full ACID support
Performance   High for large-scale, real-time data   Good for structured, moderate data
d.   What is TF-IDF in text mining?
TF-IDF (Term Frequency – Inverse Document Frequency) is a
statistical measure used in text mining to evaluate how important a word
is in a document relative to a collection of documents (corpus).
Components:
1. Term Frequency (TF)
• Measures how frequently a term appears in a document
• Formula:
Number of times term appears in document
𝑇𝐹=
Total number of terms in document
2. Inverse Document Frequency (IDF)
• Measures how important a term is across all documents
CO-2; BL-2   [5]
• Reduces weight of common words (e.g., “the”, “is”)
• Formula:
Total number of documents
𝐼𝐷𝐹= log⁡( Number of documents containing the term)
TF-IDF Formula:
𝑇𝐹-𝐼𝐷𝐹= 𝑇𝐹× 𝐼𝐷𝐹
Interpretation:
• High TF-IDF: Word is important in that document
• Low TF-IDF: Word is common across documents
Example:
If the word “data” appears frequently in one document but rarely in others,
it will have a high TF-IDF score, indicating high importance.
********** 3 **********
--- page 4 ---
a.   Mention the workflow of storing and processing a file in HDFS from input
to storage.
The workflow for storing and processing a file in HDFS, from its initial input into
the system to its final storage across the cluster, involves a multi-stage process
of ingestion, optimization, and coordinated writing.
Stage 1: Data Ingestion (Input Phase)
Before a file is stored, it must be gathered from various external sources. This
is the "Extract" stage of the ETL/ELT process.
•   Collection: Raw data is gathered from sources like databases, APIs, or
web servers.
•   Tool Selection: Users choose an ingestion tool based on data type.
Apache Sqoop is used for structured data from relational databases
(RDBMS), while Apache Flume is used for streaming log/event data.
•   Routing: Once validated, the data is directed to HDFS for storage.
Stage 2: Preparation (Serialization & Compression)
To optimize storage and processing, the data often undergoes transformation:
• Compression: Data may be compressed using codecs like Gzip, Snappy,
or LZO to reduce storage space and improve I/O efficiency.
•   Serialization: The data is converted into byte streams. Hadoop uses its
Writable framework for internal   transfers, or schema-based
Q2   frameworks like Apache Avro, which is more efficient for large-scale [10]
CO-3; BL-1   processing.
Stage 3: HDFS Write Workflow (Storage Phase)
Once the data is ready to be stored, the HDFS Client and cluster nodes follow a
coordinated 7-step workflow:
1. Create Request: The HDFS Client calls the create() method on the
DistributedFileSystem.
2. NameNode Verification: The client contacts the NameNode, which
verifies the user's permissions and ensures the file name is unique. If
valid, the NameNode returns a list of DataNodes to store the first block.
3. Write   Call:   The   client   begins   writing   data   using
FSDataOutputStream.write(), which splits the data into smaller packets
or blocks (typically 128MB/256MB).
4. Pipeline Write (Replication): To ensure reliability, HDFS uses a pipeline.
The client sends a packet to the first DataNode (DN1), which forwards
it to DN2, which then forwards it to DN3 (assuming a replication factor
of 3).
5. Data Integrity Check: During the pipeline process, each node verifies
checksums before passing the data to the next node to detect and
prevent corruption.
6. Acknowledgment (ACK): Once a packet is stored on all nodes in the
pipeline, acknowledgments are sent back in reverse order (DN3
$\rightarrow$ DN2 $\rightarrow$ DN1 $\rightarrow$ Client). A packet
is only considered successful after the client receives all ACKs.
********** 4 **********
--- page 5 ---
7. Finalization: After all packets are sent, the client calls close() to flush
the remaining data. The NameNode then updates its metadata
(recording block locations and file size) and marks the file as complete.
Stage 4: Post-Storage Reliability
After storage, HDFS maintains the file's integrity through:
•   Replication: Storing copies across different nodes to prevent data loss
if a node fails.
•   Self-healing: The system continuously monitors blocks; if it detects a
corrupted block via checksum mismatch, it automatically replaces it
with a healthy replica from another node.
b.   Explain different information retrieval (IR) models such as Boolean
model, vector space model, and probabilistic model. Compare their
advantages and limitations.
Information Retrieval models define how documents are represented, matched,
and ranked against a user query to retrieve relevant results.
1. Boolean Model
Concept:
• Based on Boolean logic (AND, OR, NOT)
• Documents are either relevant or not relevant (binary result)
Example:
Query: “data AND mining” → retrieves documents containing both terms
Advantages:
CO-2; BL-2   • Simple and easy to implement   [10]
•   Precise control over query formulation
Limitations:
• No ranking of results
•   Rigid (no partial matching)
2. Vector Space Model (VSM)
Concept:
•   Represents documents and queries as vectors of term weights
• Uses similarity measures (e.g., cosine similarity)
Example:
Documents ranked based on similarity score to query
Advantages:
•   Supports ranking of documents
• Allows partial matching and relevance scoring
********** 5 **********
--- page 6 ---
Limitations:
•   Computationally expensive
•   Ignores semantic meaning of words
3. Probabilistic Model
Concept:
• Based on probability of relevance
•   Estimates likelihood that a document is relevant to a query
Example:
Documents ranked by probability score
Advantages:
• More accurate ranking
•   Considers uncertainty and relevance
Limitations:
•   Requires probability estimation
• Complex to implement
Comparison Table
Model   Approach   Output   Advantages
Boolean   Logical matching Exact match (Yes/No) Simple, precise
Vector Space Similarity-based Ranked results   Flexible, partial match
Probabilistic Probability-based Ranked results   High accuracy
a.   Explain the working of the MapReduce programming model in Apache
Hadoop with a suitable example. Illustrate all phases such as Map,
Shuffle, Sort, and Reduce.
Map Phase
Input data is split into key-value pairs
Mapper processes input and generates intermediate key-value pairs
Shuffle Phase
Intermediate data is transferred across nodes
Q3   Groups all values with the same key
Sort Phase   [10]
CO-1; BL-2
Keys are sorted before passing to Reducer
Reduce Phase
Aggregates values for each key
Produces final output
Definition of Mapreduce → 2 Mark
Map phase explanation → 2 Marks
Shuffle & Sort → 2 Marks
Reduce phase → 2 Marks
Example → 2 Marks
CO-2; BL-3   b.   Write the commands for the following using Pig.   [10]
********** 6 **********
--- page 7 ---
Create a file Student.txt with attributes
(RollNo (int), Name (chararray), Marks (int), Grade (chararray), City
(chararray))
•   Load the data into Student (assume file and path)
•   Group the data by City and display the output
•   Write a query using FILTER to select students with Marks > 60
•   Write a query using FOREACH to display Name and Marks
•   Write a query using STORE
Creating and Load table – 2 Marks
Group by data – 2 Marks
Query using FILTER – 2 Marks
Query using FOREACH – 2 Marks
Query using STORE – 2 Marks
Student = LOAD '/data/student.txt'
USING PigStorage(',')
AS   (RollNo:int,   Name:chararray,   Marks:int,   Grade:chararray,
City:chararray);
Group by City
grp_city = GROUP Student BY City;
DUMP grp_city;
FILTER (Marks > 60)
high_marks = FILTER Student BY Marks > 60;
DUMP high_marks;
FOREACH (Display Name and Marks)
result = FOREACH Student GENERATE Name, Marks;
DUMP result;
STORE
STORE result INTO '/output/student_result' USING PigStorage(',');
a.   Describe the steps involved in creating an effective data visualization.
Explain each step with suitable examples.
Q4
[10]
CO-1; BL-3   Creating an effective data visualization involves transforming raw data into
clear, meaningful visuals that communicate insights effectively.
********** 7 **********
--- page 8 ---
1. Define Objective
•   Clearly identify the purpose of visualization
• Decide what question needs to be answered
Example: Analyze monthly sales trends to identify growth patterns
2. Data Collection and Selection
•   Gather relevant data from sources
•   Select only necessary attributes
Example: Collect sales data (month, revenue, region)
3. Data Cleaning and Preparation
• Handle missing values, remove duplicates
•   Convert data into suitable format
Example: Remove incomplete sales records and standardize date formats
4. Choose the Right Visualization Type
•   Select chart based on data nature
o Bar chart → comparison
o Line chart → trends
o Pie chart → proportions
Example: Use a line chart to show monthly sales trend
5. Design and Layout
• Add titles, labels, legends
• Use appropriate colors and scales
• Avoid clutter
Example: Highlight highest sales month using color
6. Add Interactivity (if required)
•   Enable filtering, zooming, drill-down
Example: Dashboard allowing users to filter sales by region
7. Interpretation and Storytelling
•   Highlight key insights
•   Present findings in logical flow
Example: “Sales increased by 20% in Q3 due to festive demand”
8. Evaluation and Refinement
•   Verify accuracy
********** 8 **********
--- page 9 ---
• Improve readability based on feedback
Introduction – 2 marks
Steps explanation – 6 marks
Examples – 2 mark
b.   What is fault tolerance in MapReduce? Explain how Hadoop ensures
reliable execution of jobs in the presence of failures.
Task Failure Handling
o   Failed tasks are restarted on another node
Node Failure Handling
o   If a node fails, tasks are reassigned
Data Replication (HDFS)
o Multiple copies of data stored across nodes
Speculative Execution
o Slow tasks are executed on multiple nodes
CO-1; BL-2   [10]
Benefits:
•   High reliability
•   Continuous processing
• No data loss
•   Definition → 2 Marks
•   Task failure handling → 2 Marks
• Node failure handling → 2 Marks
• Data replication → 2 Marks
•   Speculative execution / benefits → 2 Marks
a.   Explain various data definition and data manipulation operations in
Apache Hive. Illustrate with examples such as CREATE, LOAD,
INSERT, and SELECT queries.
Apache Hive provides SQL-like querying (HiveQL) for data stored in Hadoop.
DDL Operations:
• CREATE TABLE student(id INT, name STRING)
• DROP TABLE student
Q5   • ALTER TABLE
DML Operations:   [10]
CO-2; BL-3
• LOAD DATA INPATH 'data.txt' INTO TABLE student
• INSERT INTO student VALUES (1,'Amit')
• SELECT * FROM student
Key Points:
• Works on HDFS data
•   Converts queries into MapReduce jobs
Definition of Hive – 2
********** 9 **********
--- page 10 ---
DDL operations explanation – 3
DML operations explanation – 3
Examples & explanation – 2
b.   What are challenges in Big data visualizations? Explain different
techniques to overcome these challenges.
Challenges in Big Data Visualization
Big data visualization involves presenting large, complex, and rapidly
changing data in an understandable form. Key challenges include:
1. Data Volume
• Massive datasets are difficult to process and display
• Can cause slow rendering and cluttered visuals
2. Data Velocity
•   Continuous data streams require real-time updates
•   Maintaining performance with frequent updates is difficult
3. Data Variety
• Data exists in multiple formats (text, images, logs, structured tables)
•   Integration and unified visualization are complex
4. High Dimensionality
• Many attributes/features make visualization difficult
CO-1; BL-3   • Hard to represent multi-dimensional data in 2D/3D   [10]
5. Data Quality Issues
•   Missing, inconsistent, or noisy data affects accuracy
6. Scalability and Performance
•   Traditional tools fail with increasing data size
Techniques to Overcome These Challenges
1. Data Reduction Techniques
• Sampling: Use subset of data
•   Aggregation: Summarize data
• Reduces volume and improves performance
2. Dimensionality Reduction
•   Techniques like PCA (Principal Component Analysis)
• Reduces number of variables while preserving information
3. Interactive Visualization
• Zoom, filter, drill-down features
********** 10 **********
--- page 11 ---
• Allows users to explore data dynamically
4. Real-Time Visualization Tools
• Dashboards for streaming data
•   Tools like Power BI, Tableau
5. Data Integration & Preprocessing
•   Cleaning, transforming, and standardizing data
•   Ensures consistency across formats
6. Scalable Technologies
• Use distributed systems (Hadoop, Spark)
•   Enables handling large datasets efficiently
Challenges explanation– 5 marks
Techniques explanation– 5 marks
a.   Explain the concept of collaborative filtering in recommendation systems.
Differentiate between user-based and item-based approaches with
examples.
Collaborative filtering is a technique used in recommendation systems to
suggest items (products, movies, etc.) based on the preferences and behavior
of similar users or items.
It works on the idea: “Users with similar interests in the past will have similar
preferences in the future.”
Q6
[10]
CO-2; BL-3   Types of Collaborative Filtering
1. User-Based Collaborative Filtering
Concept:
•   Finds users with similar tastes
• Recommends items liked by similar users
Working:
1. Identify users similar to the target user
2. Recommend items those similar users liked
Example:
• User A and User B both like Action movies
********** 11 **********
--- page 12 ---
• User B watched a new movie → recommend it to User A
Advantages:
• Simple and intuitive
•   Personalized recommendations
Limitations:
•   Performance issues with large users
•   Suffers from cold start problem
2. Item-Based Collaborative Filtering
Concept:
•   Finds similar items based on user ratings
• Recommends items similar to what the user already likes
Working:
1. Identify items similar to those already liked
2. Recommend similar items
Example:
• User likes Laptop A
• System recommends Laptop B with similar features
Advantages:
• More stable than user-based
• Works well with large datasets
Limitations:
• Needs sufficient item data
•   Less personalized than user-based
Difference Between User-Based and Item-Based
Feature   User-Based   Item-Based
Focus   Similar users   Similar items
Recommendation Based on user similarity   Based on item similarity
Scalability   Less scalable   More scalable
Example   “Users like you also liked…” “Similar items you may like…
• Concept explanation – 2 marks
•   User-based explanation + example – 3 marks
•   Item-based explanation + example – 3 marks
• Comparison – 2 mark
b.   Explain the concept of big data applications. Discuss different domains
CO-1; BL-3   [10]
where big data is widely used.
********** 12 **********
--- page 13 ---
Concept of Big Data Applications
Big data applications refer to the use of advanced data processing and analytics
techniques to extract meaningful insights from large, complex, and diverse
datasets. These applications help organizations in decision-making, prediction,
optimization, and automation.
Big data is characterized by the 3Vs: Volume, Velocity, and Variety, and is
processed using tools like Hadoop, Spark, and machine learning algorithms.
Domains Where Big Data is Widely Used
1. Healthcare
•   Patient data analysis, disease prediction, personalized treatment
• Example: Early detection of diseases using medical records
2. Finance and Banking
•   Fraud detection, risk analysis, customer segmentation
• Example: Identifying suspicious transactions in real-time
3. E-commerce and Retail
• Recommendation systems, customer behavior analysis
• Example: Product suggestions on Amazon/Flipkart
4. Transportation and Smart Cities
•   Traffic management, route optimization, smart infrastructure
• Example: Real-time traffic monitoring using GPS data
5. Social Media
•   Sentiment analysis, trend detection
• Example: Analyzing user opinions on Twitter
6. Agriculture
•   Precision farming, crop monitoring, yield prediction
• Example: Using sensors and weather data for irrigation planning
7. Scientific Research
•   Climate modeling, genomics, space research
• Example: Analyzing satellite data for weather forecasting
********** 13 **********
--- page 14 ---
• Concept explanation – 2 marks
•   Explanation of domains – 6 marks
• Examples – 2 mark
a.   Analyze the applications of big data in healthcare and medical systems.
How does it improve diagnosis, treatment, and patient care?
Big data analytics in healthcare involves analyzing large volumes of medical
data (EHRs, imaging, genomics, sensor data) to improve clinical decisions,
optimize treatments, and enhance patient outcomes.
Applications of Big Data in Healthcare
1. Disease Diagnosis
•   Analyzes patient history, lab reports, and imaging data
• Uses machine learning to detect diseases early (e.g., cancer detection
from MRI scans)
Faster and more accurate diagnosis
2. Personalized Treatment
• Uses genomic and clinical data to tailor treatments
•   Predicts how patients respond to specific drugs
Q7
More effective and targeted therapies   [10]
CO-1; BL-3
3. Predictive Analytics
•   Predicts disease outbreaks and patient risks
•   Identifies high-risk patients (e.g., heart disease, diabetes)
Preventive care and reduced hospital admissions
4. Clinical Decision Support Systems (CDSS)
•   Assists doctors with real-time recommendations
• Combines patient data with medical knowledge
Improved decision-making
5. Remote Monitoring and Wearables
•   Collects real-time health data (heart rate, BP, activity)
•   Enables continuous patient monitoring
Early intervention and reduced hospitalization
6. Hospital Management
********** 14 **********
--- page 15 ---
•   Optimizes resource allocation (beds, staff, equipment)
• Reduces waiting time and operational costs
Efficient healthcare delivery
Improvement in Healthcare Outcomes
Area   Improvement
Diagnosis   Early detection, higher accuracy
Treatment   Personalized and effective care
Patient Care Continuous monitoring and better service
•   Introduction – 2 marks
•   Applications – 5 marks
• Improvements in diagnosis/treatment/care – 3 marks
b.   Discuss any two classification algorithms used in big data analytics.
Compare their working principles and use cases.
Classification Algorithms in Big Data Analytics
Classification is a supervised learning technique used to assign data into
predefined classes. Two commonly used algorithms are Decision Tree and Naïve
Bayes.
1. Decision Tree Algorithm
Working Principle:
•   Represents decisions in a tree structure
•   Splits data based on the best attribute using measures like Information
CO-2; BL-2   Gain or Gini Index   [10]
•   Continues splitting until a stopping condition is reached
Example:
Classifying whether a customer will buy a product based on age and income
Use Cases:
• Customer segmentation
•   Fraud detection
•   Medical diagnosis
Advantages:
• Easy to understand and interpret
•   Handles both categorical and numerical data
2. Naïve Bayes Algorithm
********** 15 **********
--- page 16 ---
Working Principle:
• Based on Bayes’ Theorem with assumption of feature independence
•   Calculates probability of each class and selects the highest
Example:
Classifying emails as spam or not spam based on keywords
Use Cases:
•   Text classification
•   Sentiment analysis
• Document categorization
Advantages:
•   Fast and efficient
• Works well with large datasets
Comparison
Feature   Decision Tree   Naïve Bayes
Approach   Rule-based splitting   Probabilistic
Interpretability High   Moderate
Performance   Good for complex data   Fast for large data
Use Case   Structured decision problems Text/data classification
•   Introduction to classification – 2 marks
•   Decision Tree explanation – 3 marks
• Naïve Bayes explanation – 3 marks
• Comparison – 2 mark
********** 16 **********
````

## 2024-25 · Final-Exam · Sem 3 · Answer key · paper d7b766395418

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_03/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Big Data Analytics/ANS_Big Data Analytics(703DB0E021)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2024
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: 2024-2025)
Subject: Big Data Analytics
Date: 02 Dec 2024   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1; SO-   a   Count number of words in this text “Welcome to Hadoop Class Hadoop is   [5]
2;BL-2   good Hadoop is bad” by using Map Reduce. Show all steps output.
Ans.
CO- 3; SO-   b   Explain Hive Metastore and compare Hive with Pig.   [5]
;BL-1
Hive metastore
 Hive metastore (HMS) is a service that stores metadata related to Apache
Hive and other services, in a backend RDBMS, such as MySQL or
Ans.   PostgreSQL. Impala, Spark, Hive, and other services share the
metastore.
 The connections to and from HMS include HiveServer, Ranger, and the
NameNode that represents HDFS.
********** 1 **********
--- page 2 ---
 Beeline, Hue, JDBC, and Impala shell clients make requests through
thrift or JDBC to HiveServer.
 The HiveServer instance reads/writes data to HMS. By default,
redundant HMS operate in active/active mode.
CO- 1; SO- ;   c   Define spatial Temporal Data? List any four Application of spatial temporal   [5]
BL-1   data.
Spatiotemporal data
•   Spatiotemporal data is use by transport industry in many ways.
New types of geospatial applications are being developed to be
used by position-aware devices installed in vehicles. Large movement
data is produced and is available for analysis. New Spatial databases
are required to handle such data with new techniques .
•   Application domains for moving object databases are expanding and
new challenges are being face.   It is required to propose powerful
Ans.   query predicates .
• GIS applications involving time may also include changes in
regions with the passage of time. Vehicle position tracking may include
cars, trains, aircrafts or vessels that may require monitoring. Similar
evolution is also occurring in the all other fields. It is a difficult to
model such applications having spatial aspects as well as
incorporate newer challenges.
Each application (1 Mark)
CO-2 ; SO- ;   d Compare clustering and classification algorithms? Provide at least one   [5]
BL-2   technique from clustering and classification with their issues.
Comparison (2 Marks), Clustering technique and issues (3 +1 = 4 marks) and
Ans.   Classification technique and issues (3 +1 = 4 marks)
Q2   [20]
a
CO-1; SO-2;   Explain Hadoop ecosystem with suitable diagram. Discuss each components   [10]
BL-1   briefly.
Draw and explain Hadoop ecosystem [5 Marks]. Brief about all components of
Ans.   Hadoop ecosystem.[5 Marks]
********** 2 **********
--- page 3 ---
b   Design MapReduce to separate even and odd numbers from a list of integers.
CO-3; SO-2;   The input list is [1, 2, 3, 4, 5, 6, 7, and 8]. Describe each steps and its output of [10]
BL-3   the execution flow of map reduce.
Ans.
Q3   [20]
a   Write HDFS Commands.
• To create new directory called student in TEMP folder
• Copying a Text File from Local File System to the TEMP folder
CO-1; SO-2;   created in question no.1   [10]
BL-3
•   Listing Contents of a Directory
•   Displaying last 1KB of data
•   Displaying last 200 bytes of data from text file.
********** 3 **********
--- page 4 ---
Each HDFS commands carry [2 Marks]
 hadoop fs -mkdir /user/temp/student
 hadoop fs -copyFromLocal input.txt
Ans.   /user/temp/student/input.txt
 hadoop fs -ls /student
hadoop fs -tail -n 100/path/to/file
CO- 2; SO-2;   b   Explain text data mining and its applications. How text mining is different   [10]
BL-1   from traditional data mining?
Text Data Mining and its Application
 Text data mining, also known as text analytics or text mining, is the
process of extracting useful information and insights from unstructured
text data. This can include emails, social media posts, customer reviews,
and other forms of text. Here are some common applications of text data
mining:
1. Sentiment Analysis: Analyzing text to determine the sentiment
expressed, such as positive, negative, or neutral. This is often used in
social media monitoring, customer feedback analysis, and brand
reputation management.
2. Topic Modeling: Identifying key topics or themes in a collection of text
documents. This can be used for organizing and categorizing large
volumes of text, such as in news articles or research papers.
Text Mining and Data Mining
Data Types:
Text Mining: Primarily deals with unstructured text data, such as emails,
social media posts, articles, and documents.
Ans.
Data Mining: Deals with structured or semi-structured data, such as
databases, spreadsheets, and logs.
Methods:
Text Mining: Relies heavily on natural language processing (NLP)
techniques to process and analyze text data. This includes tasks like
tokenization, stemming, and sentiment analysis.
Data Mining: Uses statistical and machine learning algorithms to analyze
structured or semi-structured data. Common techniques include clustering,
classification, and regression.
Output:
Text Mining: Outputs insights and patterns from text data, such as key
topics, sentiment, and trends.
Data Mining: Outputs patterns and relationships in structured data, such as
customer segments, market trends, and anomaly detection.
********** 4 **********
--- page 5 ---
Applications:
Text Mining: Used in applications such as sentiment analysis, document
categorization, information retrieval, and content recommendation.
Data Mining: Used in applications such as market basket analysis,
customer segmentation, fraud detection, and predictive maintenance.
Q4   [20]
CO-1; SO-2;   a   Explain the impact of big data analytics on Medical and health care filed by   [10]
BL-2   focusing on recommendations and real-time data analysis.
Healthcare Providers (5 Marks)
•   Industry-specific Big Data Challenges
• The healthcare sector has access to huge amounts of data but has been
plagued by failures in utilizing the data to curb the cost of rising
healthcare and by inefficient systems that stifle faster and better
healthcare benefits across the board.
•   This is mainly because electronic data is unavailable, inadequate, or
unusable. Additionally, the healthcare databases that hold health-
related information have made it difficult to link data that can show
patterns useful in the medical field.
•   Other challenges related to Big Data include the exclusion of patients
from the decision-making process and the use of data from different
readily available sensors.
Ans.   Applications of Big Data in the Healthcare Sector (5 Marks)
• Some hospitals, like Beth Israel, are using data collected from a cell
phone app, from millions of patients, to allow doctors to use evidence-
based medicine as opposed to administering several medical/lab tests to
all patients who go to the hospital. A battery of tests can be efficient,
but it can also be expensive and usually ineffective.
•   Free public health data and Google Maps have been used by the
University of Florida to create visual data that allows for faster
identification and efficient analysis of healthcare information, used in
tracking the spread of chronic disease. Obamacare has also utilized Big
Data in a variety of ways. Big Data Providers in this industry include
Recombinant Data, Humedica, Explorys, and Cerner.
CO-2; SO-2;   b How does the integration of big data analytics affect the search functionality?   [10]
BL-1   Discuss usage and evaluation of search engine.
Usage of Search Engine
 Searching for information: People use a search engine to search for any
kind of information present on the internet. For example, Rohit wants
to buy a mobile phone but he does not know which one is the best
mobile phone. So he searches “best mobile phones in 2021” in the
Ans.   search engine and gets the list of best mobile phones along with their
features, reviews, and prices.
 Searching images and videos: Search engines are also used to search
images and videos. There are so many videos and images available on
the internet in different categories like plants, animals, flowers, etc.,
you can search them according to your need.
********** 5 **********
--- page 6 ---
 Searching location: Search engines are also used to find locations. For
example, Seema is on a Goa trip but she doesn’t know the location of
Palolem beach. So she searches “Palolem beach” on the search engine
and then the search engine gives the best route to reach Palolem beach.
 Searching people: Search engines are also used to find people on the
internet around the world.
 Shopping: Search engines are also used for shopping. Search engines
optimize the pages to meet the needs of the user and give the lists of all
the websites that contain the specified product according to the best
price, reviews, free shipping, etc.
 Entertainment: Search engines are also used for entertainment
purposes. It is used to search videos, movies, games, movie trailers,
reviews of movies, social networking sites, etc. For example, Rohan
wants to watch a movie named “Ram”, then he searches this movie on
a search engine and the search engine returns a list of links (of the
websites) that contain the Ram movie.
 Education: Search engines are also used for education. With the help of
search engines, people can learn anything they wanted to learn like
cooking, programming languages, home decorations, etc. It is like an
open school where you can learn anything for free.
Evaluation of search engines
 Five types of search evaluation
 The ideal search evaluation service can depend on the nature of your
search engine, industry of your business or the structure of your
website.
 1. Result evaluation
 One of the most common and most in-demand services is the
evaluation of fetched search results. For this task, you provide a list of
the most common types of search queries you expect to receive on your
site. Evaluators then test your search engine algorithm against those
queries directly on your site or on a custom external platform. Once the
results are fetched, evaluators can rank them in a number of ways:
 Positive or negative: Classify each result as either relevant or not
relevant.
 Ranking: Order the results from top to bottom in order of relevancy.
 Scale: Score the results on a scale of 1-5, five being most relevant, one
being completely irrelevant.
 Side-by-side: From each pair of results, choose which result is more
relevant.
Q5   [20]
a   Write commands for the following using Pig
•   Create table Customer with (Name (char array), Phone No.(int), Salary
CO-3; SO-2;   (int), City (char array))   [10]
BL-3   •   Create file with five records and display
• Write query using LOAD, STORE, FILTER and FOREACH
Create database Student with (Name, RollNo, Marks, City) [2 Marks]
Create file with five records and display [2 Marks]
Ans.   Input character array, write query using LOAD, STORE, FILTER AND
FOREACH[6 Marks]
CO-1; SO-2;   b What are Big data visualization challenges? Illustrate any 4 with an example.   [10]
BL-1
********** 6 **********
--- page 7 ---
Visualization Challenges (2 Marks)
•   It is a large volume, complex dataset. So, such data can not visualize
with the traditional method as the traditional method has many
limitations.
• Perceptual Scalability: Human eyes cannot extract all relevant
information from a large volume of data. Even sometimes desktop
screen has its limitations if the dataset is large. Too many visualizations
are not always possible to fit on a single screen.
Ans.   • Real-time Scalability: It is always expected that all information should
be real-time information, but it is hardly possible as processing the
dataset needs time.
•   Interactive scalability: Interactive data visualization help to
understand what is inside the datasets, but as its volume increases
exponentially, visualizing the datasets take a long time. But the
challenge is sometimes, and the system may freeze or crash while
trying to visualize the datasets.
Each technique with example (2 Marks)
Q6   [20]
a   Write Hive query for following operations.
•   Create database ‘Stu’ and table ‘Student’ with (Name, Sid,
Course, Marks)
CO-3; SO-2;   •   Create four records in table   [10]
BL-3   • Write hive query to load data,
• Display student name with highest marks
• Display student with the same course.
Ans.   Each query with output (1 Marks)
CO-3; SO-2;   b   Explain Pig Architecture in Hadoop ecosystem. Compare Pig and Map   [10]
BL-1   Reduce.
Difference between Pig and MapReduce
Apache Pig   MapReduce
It is a compiled programming
It is a scripting language.
language.
Abstraction is at higher level.   Abstraction is at lower level.
Ans.
It have less line of code as
Lines of code is more.
compared to MapReduce.
Less effort is needed for   More development efforts are
Apache Pig.   required for MapReduce.
********** 7 **********
--- page 8 ---
Code efficiency is less as   As compared to Pig efficiency
compared to MapReduce.   of code is higher.
Pig provides built in functions   Hard to perform data
for ordering, sorting and union.   operations.
It allows nested data types like   It does not allow nested data
map, tuple and bag   types
Pig Architecture
a From the box plot given, find the skewness for ‘Time Slept (hours)’from
Monday to Friday. Draw the skewness for the same. Also, explain the relation
between mean, median and mode for left and right skewed data.
Q7
[10]
CO-1; SO-
3;BL-3
The box plot for Monday is left skew,
Ans.
The box plot for Friday is right skew
********** 8 **********
--- page 9 ---
CO-2; SO-   b
Describe cosine similarity measure with appropriate example. Discuss how   [10]
3;BL-2   cosine similarity measure is used in collaborative filtering.
Ans.
********** 9 **********
````
