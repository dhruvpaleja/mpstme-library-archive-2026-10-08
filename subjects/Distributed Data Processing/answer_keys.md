# Distributed Data Processing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper dfa9a4f82f2d

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Distributed Data Processing/ANS_Distributed Data Processing(703DB0C067)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Distributed Data Processing
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions attempt any 4
6. In total 5 questions needs to be answered
7. All Questions carry equal marks
Q1
(i) Describe the major stages in the Spark application lifecycle, from job submission to result aggregation.
(4 Marks)
A Spark application goes through several stages during execution, starting from submission and ending with
result generation. These stages define how Spark distributes and processes data across the cluster.
The first stage is job submission, where the user submits a Spark application using commands such as spark-
submit. The driver program is launched and initializes the SparkSession or SparkContext, which acts as the
entry point to the Spark framework.
Next, the driver communicates with the cluster manager (Standalone, YARN, Mesos, or Kubernetes) to allocate
resources such as CPU cores and memory for executor processes. Executors are launched on worker nodes
where the actual computation occurs.
After resource allocation, the driver converts the user program into a Directed Acyclic Graph (DAG) of stages.
Each stage contains multiple tasks that operate on partitions of the dataset.
These tasks are distributed to executors, which perform transformations and actions on the data in parallel.
Intermediate results may be cached in memory or written to disk.
Finally, executors send the results back to the driver, where result aggregation occurs. The driver then returns
the final output to the user or stores it in external storage.
(ii) Compare DataFrame API and Spark SQL API for analytical queries. Demonstrate finding top customers
with highest orders. (4 Marks)
Apache Spark provides two common interfaces for performing analytical queries: the DataFrame API and the
Spark SQL API.
The DataFrame API allows developers to perform operations using programmatic transformations similar to
relational operations. It is widely used in PySpark applications and integrates with Spark’s optimization engine.
The Spark SQL API allows users to execute SQL queries on structured datasets. This approach is useful for
analysts familiar with relational database query languages.
Example problem: Find customers with the highest number of orders.
Using DataFrame API
**********   **********
--- page 2 ---
orders_df.groupBy("customer_id") \
.count() \
.orderBy("count", ascending=False) \
.show()
Using Spark SQL
orders_df.createOrReplaceTempView("orders")
spark.sql("""
SELECT customer_id, COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC
""").show()
Both approaches produce the same result because Spark converts them into optimized execution plans using
the Catalyst optimizer. The choice depends on developer preference and application design.
(iii) Calculate final payable amount using numeric functions in Spark SQL/DataFrame. (4 Marks)
Suppose a dataset contains two columns:
• order_amount
•   discount_rate
The final payable amount can be calculated by subtracting the discount from the order amount.
Formula:
Final Amount = order_amount − (order_amount × discount_rate)
Using DataFrame API
from pyspark.sql.functions import col
df = df.withColumn(
"final_amount",
col("order_amount") - (col("order_amount") * col("discount_rate"))
)
Using Spark SQL
SELECT order_amount,
discount_rate,
order_amount - (order_amount * discount_rate) AS final_amount
FROM orders
Spark SQL numeric functions help perform arithmetic operations such as addition, subtraction, multiplication,
division, and rounding.
Using these functions enables efficient distributed calculation of financial metrics across large datasets.
(iv) Describe the read–process–write workflow in Structured Streaming and compare it with batch workflows.
(4 Marks)
Structured Streaming applications typically follow three major steps: read, process, and write.
Read
The streaming application continuously reads incoming data from sources such as Kafka, files, or sockets.
Example:
stream_df = spark.readStream.format("kafka").load()
Process
2
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 3 ---
Spark applies transformations such as filtering, aggregation, and joins on streaming data.
Example:
processed_df = stream_df.filter("amount > 1000")
Write
The processed data is written to output sinks such as databases, Kafka topics, or files.
Example:
processed_df.writeStream.format("console").start()
Difference from Batch Processing
Feature   Batch Processing Streaming Processing
Data nature Static datasets   Continuous data
Execution Runs once   Continuous processing
Latency   High   Low
Structured Streaming allows organizations to process data in real time, whereas batch systems process data
after it has been collected.
(v) Joining streaming and static DataFrames (4 Marks)
In many real-time analytics systems, streaming data must be enriched with additional information stored in
static datasets.
Spark Structured Streaming allows joining a streaming DataFrame with a static DataFrame.
Example:
transactions_stream.join(customers_static,
"customer_id")
In this scenario:
•   Streaming dataset contains incoming transactions.
•   Static dataset contains customer information.
The join operation enriches streaming records with customer attributes such as name or location.
Limitations
• Some join types require watermarking.
•   Streaming-to-streaming joins require additional state management.
•   Large static datasets may increase memory usage.
Despite these limitations, streaming-static joins are widely used in fraud detection, recommendation systems,
and real-time analytics.
Q2
(i) Core components of a Spark application (10 Marks)
A Spark application consists of several core components that coordinate distributed computation across a
cluster.
Driver Program
The driver program contains the main application logic. It creates the SparkSession and coordinates the
execution of tasks across the cluster.
The driver converts user code into execution plans and divides jobs into stages and tasks.
SparkContext / SparkSession
SparkContext acts as the interface between the driver and the cluster. It manages communication with
executors and schedules tasks.
SparkSession provides a unified entry point for Spark SQL, DataFrame operations, and streaming.
3
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 4 ---
Cluster Manager
The cluster manager allocates resources for Spark applications. It manages CPU cores and memory across
worker nodes.
Examples include:
•   Standalone cluster manager
• Hadoop YARN
• Mesos
•   Kubernetes
Worker Nodes
Worker nodes are machines in the cluster that execute Spark tasks. Each worker node runs executor processes.
Executors
Executors are worker processes that perform actual computations. Their responsibilities include:
•   Executing tasks
•   Storing cached data
•   Sending results back to the driver
Execution Flow
1. Application is submitted
2. Driver initializes SparkSession
3. Cluster manager allocates resources
4. Executors process data partitions
5. Results are returned to the driver
These components enable Spark to perform parallel, scalable, and fault-tolerant data processing.
Q3
(i) Resilient Distributed Dataset (RDD) abstraction (10 Marks)
The Resilient Distributed Dataset (RDD) is the fundamental data abstraction in Apache Spark. It represents an
immutable distributed collection of objects that can be processed in parallel across a cluster.
RDDs are partitioned across multiple nodes, allowing tasks to operate on each partition simultaneously.
Key Characteristics
1. Distributed Data Structure
Data is split into partitions stored across cluster nodes.
2. Immutability
RDDs cannot be modified after creation. Instead, transformations create new RDDs.
3. Fault Tolerance
RDDs track lineage information so lost partitions can be recomputed.
Transformations
Transformations are lazy operations that create new RDDs.
Examples:
• map()
•   filter()
•   flatMap()
4
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 5 ---
Actions
Actions trigger computation and return results.
Examples:
•   collect()
•   count()
•   saveAsTextFile()
Importance of RDDs
RDDs provide:
•   Low-level control over distributed computation
•   Fault tolerance through lineage
•   Efficient parallel processing
Although higher-level APIs such as DataFrames are more common today, RDDs remain important for custom
distributed algorithms.
(ii) Fault tolerance in Spark (10 Marks)
Spark ensures fault tolerance through several mechanisms that allow applications to recover from failures.
Lineage-Based Recovery
Spark records the sequence of transformations used to create RDDs. If a partition is lost, Spark recomputes it
using the lineage information.
Task Re-execution
If a task fails due to executor failure or network issues, the driver automatically reschedules the task on another
executor.
Checkpointing
Checkpointing saves intermediate data to reliable storage such as HDFS. This prevents recomputation of long
lineage chains.
Speculative Execution
Spark detects slow tasks and launches duplicate tasks on other nodes. The result from the fastest task is used.
Executor Failure Handling
If an executor crashes, Spark redistributes its tasks across other executors and recomputes lost data partitions.
These mechanisms ensure that Spark applications remain reliable and fault tolerant even in large distributed
clusters.
Q4
(i) Differentiate between Broadcast Hash Join, Shuffle Hash Join, and Shuffle Sort-Merge Join. (10 Marks)
Apache Spark uses different join strategies depending on the size of datasets, available memory, and cluster
configuration. The three commonly used join strategies are Broadcast Hash Join, Shuffle Hash Join, and Shuffle
Sort-Merge Join.
1. Broadcast Hash Join
5
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 6 ---
Broadcast Hash Join is used when one of the datasets involved in the join is small enough to fit in memory. In
this strategy, Spark broadcasts the smaller dataset to all executor nodes. Each executor then performs the join
locally using the broadcasted dataset.
Working Principle
1. Identify the smaller table.
2. Broadcast the smaller dataset to all executors.
3. Each executor joins its partition of the large dataset with the broadcasted dataset using a hash table.
Example:
from pyspark.sql.functions import broadcast
orders.join(broadcast(customers), "customer_id")
Advantages
•   Avoids shuffle operations
•   Faster execution
• Reduced network overhead
Suitable Scenario
When one dataset is very small compared to the other (e.g., dimension tables).
2. Shuffle Hash Join
Shuffle Hash Join is used when both datasets are large but can fit in memory after partitioning.
Working Principle
1. Both datasets are shuffled based on the join key.
2. Each partition builds a hash table for one dataset.
3. The other dataset is probed against this hash table.
Advantages
•   Efficient when partitions fit in memory
•   Faster than sort-merge join when datasets are moderately sized
Limitations
•   Requires sufficient memory
• May cause memory pressure with large datasets
3. Shuffle Sort-Merge Join
Shuffle Sort-Merge Join is used when both datasets are large and cannot fit in memory.
Working Principle
1. Both datasets are shuffled based on the join key.
2. Data within partitions is sorted.
3. The sorted partitions are merged to perform the join.
Advantages
•   Handles very large datasets
•   Stable performance
Limitations
•   Requires sorting operations
•   Higher computational cost than broadcast joins
Comparison
Join Type   Shuffle Required Sorting Required Best Use Case
Broadcast Hash Join   No   No   Small dimension tables
6
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 7 ---
Join Type   Shuffle Required Sorting Required Best Use Case
Shuffle Hash Join   Yes   No   Medium datasets
Shuffle Sort-Merge Join Yes   Yes   Very large datasets
Thus, Spark chooses the join strategy based on dataset size, memory availability, and optimization rules.
(ii) Late Data, Out-of-Order Data and Watermarks in Structured Streaming (10 Marks)
In real-time streaming systems, events may not arrive in chronological order due to network delays, system
failures, or ingestion latency. Such events are known as late data or out-of-order data.
Handling late events is a major challenge in streaming applications, especially when performing window-based
aggregations.
Late Data
Late data refers to records that arrive after their expected event time.
Example:
A transaction that occurred at 10:00 AM may reach the streaming system at 10:10 AM.
Out-of-Order Data
Out-of-order data occurs when events arrive in a sequence different from their actual occurrence time.
Example order of arrival:
10:05 → 10:01 → 10:03
This can affect window computations if not handled correctly.
Watermarks in Structured Streaming
Spark uses watermarks to manage late data while controlling memory usage.
A watermark defines the maximum delay allowed for late events.
Example:
df.withWatermark("timestamp","10 minutes")
This means Spark will accept records arriving within 10 minutes of their event time.
Impact on Window-Based Computations
Consider a 5-minute tumbling window.
•   Spark processes records within each window.
• Watermarks determine when a window is considered complete.
• Once the watermark passes a window, Spark removes state information for that window.
Benefits:
•   Prevents state store from growing indefinitely
•   Allows limited tolerance for late events
• Improves memory efficiency
Thus, watermarks enable accurate streaming analytics while maintaining efficient resource usage.
Q5
(i) Demonstrate different join types supported in Spark (10 Marks)
Spark supports multiple join types similar to relational databases. These joins allow combining datasets based
on a common key.
Assume two datasets:
Orders Table
7
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 8 ---
order_id customer_id
1   101
2   102
3   103
Customers Table
customer_id name
101   Alice
102   Bob
104   David
1. Inner Join
Returns records that have matching keys in both datasets.
orders.join(customers,"customer_id","inner")
Output
order_id customer_id name
1   101   Alice
2   102   Bob
2. Left Outer Join
Returns all rows from the left dataset.
orders.join(customers,"customer_id","left")
Output
order_id customer_id name
1   101   Alice
2   102   Bob
3   103   NULL
3. Right Outer Join
Returns all rows from the right dataset.
4. Full Outer Join
Returns all rows from both datasets.
5. Left Semi Join
Returns rows from the left dataset that have matches in the right dataset.
6. Left Anti Join
Returns rows from the left dataset that do not have matches in the right dataset.
Spark joins are optimized using techniques such as broadcast joins, partitioning, and adaptive query execution
to improve performance.
(ii) Output modes in Structured Streaming (10 Marks)
Structured Streaming supports three output modes:
8
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 9 ---
• Append
• Update
• Complete
These modes determine how results are written to the output sink.
1. Append Mode
In append mode, only new rows are written to the output.
Example:
Streaming logs written to a file.
df.writeStream.outputMode("append")
Use Case
•   Event logging
•   Kafka streaming pipelines
2. Update Mode
In update mode, only updated rows are written to the sink.
Example:
Streaming aggregations where counts change over time.
df.writeStream.outputMode("update")
Use Case
Real-time dashboards.
3. Complete Mode
In complete mode, the entire result table is written after every trigger.
df.writeStream.outputMode("complete")
Use Case
Full aggregation queries.
Comparison
Mode   Output   Suitable For
Append New rows only Event streams
Update   Modified rows Incremental aggregations
Complete Entire table   Global aggregations
Choosing the correct output mode ensures accurate results and efficient streaming performance.
Q6
(i) Spark SQL Query Execution Plan (10 Marks)
When a query is executed in Spark SQL, it goes through several optimization stages.
1. Parsed Logical Plan
Spark parses the SQL query and converts it into a logical representation.
Example:
SELECT * FROM orders WHERE amount > 1000
Spark generates a logical tree representation.
2. Analyzed Logical Plan
9
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 10 ---
Spark validates column names, data types, and table references.
This stage ensures the query is semantically correct.
3. Optimized Logical Plan
The Catalyst Optimizer improves the logical plan using optimization techniques.
Examples:
•   Predicate pushdown
• Column pruning
•   Constant folding
4. Physical Plan
The optimized logical plan is converted into a physical execution plan.
Spark decides:
•   join strategy
•   partitioning
•   execution operators
Example operations:
• Hash Aggregate
•   Broadcast Join
•   Sort Merge Join
These stages ensure Spark queries are executed efficiently with minimal resource usage.
(ii) Spark Deployment Modes (10 Marks)
Spark supports several deployment modes depending on the environment.
1. Local Mode
Runs Spark on a single machine.
Advantages:
•   Easy testing
• No cluster required
Limitations:
• Not suitable for large datasets.
2. Standalone Mode
Spark’s built-in cluster manager.
Advantages:
•   Simple setup
• Good for dedicated clusters.
3. YARN Mode
Spark runs on Hadoop YARN clusters.
Advantages:
• Resource sharing with Hadoop ecosystem
• Good integration with HDFS.
4. Mesos Mode
10
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 11 ---
Apache Mesos manages cluster resources for Spark.
Advantages:
•   Efficient resource sharing.
5. Kubernetes Mode
Spark applications run as containers inside Kubernetes pods.
Advantages:
•   Cloud-native deployment
• Automatic scaling
•   Container orchestration.
Each deployment mode offers different levels of scalability, resource management, and operational
complexity.
Q7
(i) Deploying Spark applications in Kubernetes (10 Marks)
Kubernetes is widely used for deploying containerized Spark applications.
Configuration Parameters
Important Spark configuration parameters include:
--master k8s://
--deploy-mode cluster
--executor-memory
--executor-cores
These parameters define resource allocation for Spark applications.
Container Images
Spark applications are packaged into Docker images.
Example:
spark:3.5.0
Images contain:
•   Spark runtime
•   Application code
• Dependencies
Deployment Strategies
Spark driver and executors run inside Kubernetes pods.
Process:
1. Submit application using spark-submit.
2. Kubernetes creates driver pod.
3. Driver requests executor pods.
4. Executors execute tasks.
Benefits
•   Scalability
• Resource isolation
•   High availability
11
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 12 ---
• Automatic recovery.
Thus, Kubernetes simplifies the management of large-scale Spark deployments.
(ii) Sort Aggregate vs Hash Aggregate in Spark (10 Marks)
Spark uses two major aggregation techniques:
•   Sort Aggregate
• Hash Aggregate
Sort Aggregate
In sort aggregation, data is first sorted based on grouping keys. After sorting, Spark aggregates rows
sequentially.
Steps:
1. Shuffle data based on group keys
2. Sort data within partitions
3. Aggregate rows
Time Complexity
Sorting requires approximately O(n log n) time.
Hash Aggregate
In hash aggregation, Spark builds an in-memory hash table for grouping keys.
Steps:
1. Create hash table
2. Insert rows into hash table
3. Update aggregation values
Time Complexity
Hash operations typically take O(n) time.
Comparison
Feature   Sort Aggregate Hash Aggregate
Operation   Sorting required Uses hash table
Time Complexity O(n log n)   O(n)
Performance   Slower   Faster
Memory usage Lower   Higher
Why Hash Aggregate is Faster
Hash aggregation avoids sorting and directly groups rows using hash tables. Therefore it is generally faster
when memory is sufficient.
However, if memory is limited, Spark may fall back to sort-based aggregation.
12
**********   **********
Sensitivity: LNT Construction Internal Use
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 8babd1af667c

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Distributed Data Processing/ANS_Distributed Data Processing(703DB0C067)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2025
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Distributed Data Processing
Date: 07 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions attempt any 4
6. In total 5 questions needs to be answered
7. All Questions carry equal marks
Synoptic Solutions for Q1 (Compulsory - 5 x 4 Marks = 20 Marks)
(a) Core Components of Apache Spark (CO1, BL2, SO1)
• Driver Program: Manages job execution and distributes tasks.
• Cluster Manager: Allocates resources (Standalone, YARN, Mesos, Kubernetes).
• Executors: Run tasks assigned by the driver, store data in-memory/disk.
• RDDs, DataFrames, and Datasets: Spark’s core abstractions for data handling.
•   Libraries: Includes Spark SQL (structured data), Spark Streaming (real-time), MLlib (ML),
GraphX (graph processing).
(b) Differences Between RDDs, DataFrames, and Datasets (CO2, BL4, SO2)
Feature   RDD   DataFrame   Dataset
API Type   Low-level   High-level   High-level
Schema   No schema   Schema-based   Schema-based
Slower (No   Optimized (Catalyst
Performance   Optimized (Catalyst Optimizer)
optimizations)   Optimizer)
Type Safety No   No (in Python, R)   Yes (in Scala, Java)
Complex   Type-safe, optimized
Use Case   SQL-like processing
transformations   transformations
(c) Working of Spark SQL & Query Optimization (CO3, BL3, BL4, SO3)
• Uses DataFrames & SQL Queries for structured data.
1
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 2 ---
• Optimized by Catalyst Optimizer, which:
o Converts queries into logical plans.
o Generates efficient physical execution plans.
o Uses predicate pushdown and cost-based optimization (CBO).
• Tungsten Execution Engine improves CPU and memory efficiency.
• Example Query:
python
CopyEdit
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.select("column1").filter(df.column2 > 100).show()
(d) Role of Kafka in Spark Streaming & Data Consumption (CO4, BL2, SO4)
• Kafka: A distributed messaging system used for real-time data ingestion.
• Spark Streaming reads Kafka topics using Structured Streaming:
python
CopyEdit
df = spark.readStream.format("kafka").option("subscribe", "topic_name").load()
• Advantages of Kafka-Spark Integration:
o Scalability: Handles large-scale streaming data.
o Fault Tolerance: Uses Kafka offsets for recovery.
o Low Latency: Supports near real-time analytics.
(e) Different Deployment Modes in Spark (CO5, BL5, SO5)
Mode   Best For   Cluster Manager   Scalability
Local   Development/testing   None (Single JVM)   No scalability
Standalone Small dedicated clusters Spark Master ✅ Limited
YARN   Hadoop-based workloads YARN   ✅ High
Kubernetes Cloud-native Spark apps Kubernetes   ✅ Highly scalable
Key Points:
• Local Mode → For debugging, all runs on a single machine.
• Standalone Mode → Spark manages its own cluster (simpler setup).
• YARN Mode → Best for Hadoop ecosystems, dynamic resource allocation.
• Kubernetes Mode → Containerized Spark, auto-scaling, cloud-friendly.
Synoptic Solutions for Q2-Q7 (Each Question Carries 10 Marks)
Q2. Apache Spark Architecture & Operations
(a) Spark Architecture with a Labelled Diagram (CO1, BL2, SO1)
✅ Key Components:
2
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 3 ---
•   Driver Program: Orchestrates execution.
•   Cluster Manager: Allocates resources (Standalone, YARN, Kubernetes, Mesos).
•   Executors: Run tasks on worker nodes.
• RDD/Dataset/DataFrame API: Core data abstractions.
✅ Diagram: Must illustrate Driver, Cluster Manager, Executors.
(b) Spark Transformations & Actions with Examples (CO2, BL3, BL4, SO2)
✅ Transformations (Lazy Execution):
• map(), filter(), groupByKey(), reduceByKey()
•   Example: rdd.map(lambda x: x * 2)
✅ Actions (Trigger Execution):
• collect(), count(), first(), reduce()
•   Example: rdd.count()
✅ Impact: Improves efficiency using lazy execution & lineage graphs.
Q3. Performance Optimization & Execution
(a) Data Partitioning & Its Impact on Performance (CO2, BL4, BL5, SO2)
✅ Partitioning Mechanisms:
• Hash Partitioning → Evenly distributes data based on keys.
• Range Partitioning → Sorts data into ranges (useful for sorting queries).
✅ Impact on Performance:
• Reduces shuffling overhead.
• Improves parallel processing efficiency.
•   Example:
python
CopyEdit
df = df.repartition(4, "column_name")
(b) Jobs, Stages, & Tasks in Spark Execution (CO1, BL2, SO1)
✅ Execution Flow:
•   Job → Set of transformations.
•   Stage → Groups of tasks before a shuffle.
•   Task → A single unit of execution on partitioned data.
✅ Example:
• df.groupBy("category").count()
o Creates one job.
o Divides into two stages (before & after shuffle).
3
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 4 ---
o Executes multiple tasks per stage.
o
Q4. PySpark SQL & Windowed Operations
(a) PySpark SQL Overview (CO3, BL4, SO3)
✅ Features of PySpark SQL:
• Uses DataFrames for SQL-like operations.
•   Supports JDBC, Hive, and NoSQL integrations.
• Optimized by Catalyst Optimizer & Tungsten Engine.
✅ Example Query:
python
CopyEdit
df = spark.sql("SELECT category, COUNT(*) FROM sales GROUP BY category")
df.show()
(b) Windowed Operations in Spark Streaming (CO4, BL3, BL4, SO4)
✅ Types of Windows:
• Tumbling Window → Fixed-length, non-overlapping.
•   Sliding Window → Overlapping windows with a defined slide interval.
•   Session Window → Based on activity gaps.
✅ Example Code:
python
CopyEdit
windowed_df = df.groupBy(window("timestamp", "10 minutes")).count()
Q5. Aggregate Functions & Structured Streaming
(a) Aggregate Functions in Spark SQL with Examples (CO3, BL3, SO2)
✅ Common Aggregates:
• SUM(), AVG(), COUNT(), MAX(), MIN()
✅ Example Query:
python
CopyEdit
df.groupBy("category").agg(sum("sales").alias("total_sales")).show()
(b) Structured Streaming Model & Handling Late Data (CO4, BL4, BL5, SO4)
✅ Key Concepts:
•   Micro-batch Processing → Streams processed in mini-batches.
• Watermarking → Handles late-arriving data.
✅ Example Code:
python
4
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 5 ---
CopyEdit
df.withWatermark("timestamp", "10 minutes").groupBy(window("timestamp", "5
minutes")).count()
Q6. Joins & Cluster Management
(a) Types of Joins & Performance Optimization (CO3, BL3, BL4, SO3)
✅ Types of Joins in Spark SQL:
•   Inner Join → Matches records with common keys.
•   Left/Right Join → Includes unmatched records from one side.
•   Broadcast Join → Optimized for small datasets.
✅ Optimization Techniques:
•   Broadcasting small tables: df1.join(broadcast(df2), "key")
•   Partition Pruning: Ensuring same partitions before joining.
(b) Cluster Managers in Spark (CO5, BL2, SO5)
✅ Types of Cluster Managers:
• Standalone Mode → Spark manages its own cluster.
• YARN Mode → Runs on Hadoop.
• Kubernetes Mode → Cloud-native, auto-scaling.
✅ Example Command:
bash
CopyEdit
spark-submit --master yarn my_spark_app.py
Q7. Managing & Monitoring Spark on Kubernetes (CO5, BL3, SO5)
✅ Kubernetes Features for Spark:
• Dynamic Resource Allocation → Auto-scales executors.
• Pod Auto-recovery → Restarts failed tasks.
•   Monitoring Tools → Prometheus, Grafana, Spark UI.
✅ Monitoring Example:
bash
CopyEdit
kubectl logs spark-executor-1
Q.7 b
PySpark Pseudo-Code for Dataset Analysis
python
CopyEdit
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, corr, desc
5
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 6 ---
# 1. Initialize Spark Session
spark = SparkSession.builder.appName("WineQualityAnalysis").getOrCreate()
# 2. Load the Dataset (Assuming CSV format)
df = spark.read.csv("wine_data.csv", header=True, inferSchema=True)
# 3. Display the Dataset
df.show(5) # Display first 5 rows
# 4. Count the number of rows and columns
num_rows = df.count()
num_cols = len(df.columns)
print(f"Number of Rows: {num_rows}, Number of Columns: {num_cols}")
# 5. Get Column Names and Data Types
df.printSchema()
# 6. Check for Missing Values
missing_values = df.select([count(col(c)).alias(c) for c in df.columns])
missing_values.show()
# 7. Summary Statistics
df.describe().show()
# 8. Filter high-quality wine (quality > 7)
high_quality_wine = df.filter(col("quality") > 7)
high_quality_wine.show()
# 9. Find the most common wine quality
most_common_quality = df.groupBy("quality").count().orderBy(desc("count"))
most_common_quality.show(1) # Show the most frequent quality
# 10. Correlation Analysis between Alcohol and Quality
correlation = df.stat.corr("alcohol", "quality")
print(f"Correlation between Alcohol and Quality: {correlation}")
# 11. Find Average Alcohol Content for Each Quality Rating
avg_alcohol_per_quality =
df.groupBy("quality").agg(avg("alcohol").alias("avg_alcohol"))
avg_alcohol_per_quality.show()
# 12. Check Number of Partitions
print(f"Current Number of Partitions: {df.rdd.getNumPartitions()}")
# 13. Increase Number of Partitions (if needed)
df_repartitioned = df.repartition(10)
print(f"New Number of Partitions: {df_repartitioned.rdd.getNumPartitions()}")
Explanation of Spark Functions Used:
1. spark.read.csv("file.csv", header=True, inferSchema=True) → Reads the dataset from
a CSV file with automatic schema inference.
2. df.show(5) → Displays the first 5 rows.
3. df.count() & len(df.columns) → Counts the number of rows and columns.
4. df.printSchema() → Prints column names and their data types.
5. df.select([count(col(c)).alias(c) for c in df.columns]).show() → Checks for
missing values.
6. df.describe().show() → Provides summary statistics (mean, std, min, max).
7. df.filter(col("quality") > 7) → Filters high-quality wines (quality > 7).
6
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 7 ---
8. df.groupBy("quality").count().orderBy(desc("count")) → Finds the most common
wine quality.
9. df.stat.corr("alcohol", "quality") → Computes correlation between alcohol content and
wine quality.
10. df.groupBy("quality").agg(avg("alcohol").alias("avg_alcohol")) → Finds the
average alcohol content for each quality rating.
11. df.rdd.getNumPartitions() → Gets the number of partitions.
12. df.repartition(10) → Increases the number of partitions for parallel processing.
7
**********   **********
Sensitivity: LNT Construction Internal Use
````
