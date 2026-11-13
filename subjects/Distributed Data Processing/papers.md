# Distributed Data Processing: question papers in full

5 unique papers · 2024-25 to 2025-26 · Artificial Intelligence

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 2 · paper 78f8486ed491

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Distributed Data Processing/QP_Distributed Data Processing(703DB0C067)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Distributed Data Processing
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions attempt any 4
6. In total 5 questions needs to be answered
7. All Questions carry equal marks
Q1   (i)   Describe the major stages in the Spark application lifecycle, from   4
job submission to result aggregation.
CO1
BL-2
CO2   (ii)   Compare the DataFrame API and Spark SQL API for performing   4
BL-2,3,4   analytical queries. Demonstrate how a query such as finding the top
customers with the highest number of orders can be implemented
using both approaches.
CO3   (iii) A dataset contains the columns order_amount and discount_rate.   4
BL-3,4   Apply appropriate numeric functions in Spark SQL and spark Data
frame to calculate the final payable amount for each order.
CO4   (iv) A Spark Structured Streaming application follows three major steps: 4
BL-2,3   read, process, and write.
Describe these three steps and explain how they differ from batch
processing workflows.
CO5   (v) A streaming application needs to enrich incoming transaction data   4
BL-5   with customer information stored in a static dataset. Evaluate how a
streaming DataFrame can be joined with a static DataFrame and
assess the limitations of different join types.
Q2   (i)   Explain the core components of a Spark application. How do these   10
components interact to perform distributed data processing?
CO1
BL-2
CO2   (ii)   Analyze the workflow of working with DataFrames in PySpark and   10
BL-3,4   demonstrate the process of:
• loading data into a DataFrame
• applying transformations
• writing results back to storage.
Provide examples of commonly used DataFrame reader formats.
Q3   (i)   Analyze the Resilient Distributed Dataset (RDD) abstraction and   10
examine its significance in Spark.
CO2
BL-4
**********   **********
--- page 2 ---
CO1   (ii)   Explain how Spark ensures fault tolerance during application   10
BL-2   execution. Discuss mechanisms used to handle executor failures and
task re-execution.
Q4   (i)   Differentiate between the following Spark join strategies:   10
• Broadcast Hash Join
CO3   • Shuffle Hash Join
BL-3,4   • Shuffle Sort-Merge Join
Analyze their working principles and identify scenarios where each
strategy is suitable.
CO4   (ii)   Analyze the challenges of late data and out-of-order data in   10
BL-3,4   streaming applications and demonstrate how watermarks handle
these issues in Structured Streaming. Examine their impact on
window-based computations.
Q5   (i)   Demonstrate the different types of joins supported in Spark using an 10
example dataset and show the output produced by each join.
CO3
BL-3
CO4   (ii)   Compare the different output modes in Structured Streaming   10
BL-4   (Append, Update, and Complete). Analyze their suitability for
different streaming use cases and examine how the choice of sink
and output mode affects streaming application performance and
correctness.
Q6   (i)   Analyze the stages involved in the Spark SQL query execution plan, 10
including:
CO3   • Parsed Logical Plan
BL-3,4
• Analyzed Logical Plan
• Optimized Logical Plan
• Physical Plan.
CO5   (ii)   Describe the different Spark deployment modes. Explain the   10
BL-2   working principles, advantages, and limitations of:
• Local Mode
• Standalone Mode
• YARN Mode
• Mesos Mode
• Kubernetes Mode.
Q7   (i)   Apply configuration techniques to deploy Spark applications in   10
Kubernetes environments, demonstrating the use of configuration
CO5   parameters, container images, and deployment strategies.
BL-3
CO3   (ii)   Compare and analyze Sort Aggregate and Hash Aggregate   10
BL-3,4,5   operations in Spark. Evaluate their time complexities and
demonstrate why Hash Aggregate is usually faster than Sort
Aggregate.
2
**********   **********
Sensitivity: LNT Construction Internal Use
````

## 2024-25 · Final-Exam · Sem 2 · paper f1f67ea529f9

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Distributed Data Processing/QP_Distributed Data Processing(703DB0C067)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2025
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Distributed Data Processing
Date: 07 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions attempt any 4
6. In total 5 questions needs to be answered
7. All Questions carry equal marks
Q.1   1.   Explain the core components of Apache Spark and their role in   4
CO1   distributed computing.
BL-2
CO2   2.   What are the differences between RDDs, Dataframes, and Datasets 4
BL-2,3,4   in Spark?
CO3   3.   Describe the working of Spark SQL. How does it optimize query 4
BL-3,4   execution?
CO4   4.   What is the role of Kafka in Spark Streaming? How does Spark 4
BL-2,3   consume data from Kafka?
CO5   5.   Explain different Deployment modes in spark.   4
BL-5
Q.2   a.   Explain the architecture of Apache Spark with a labelled diagram.   10
CO1
BL-2
CO2   b.   What are Spark transformations and actions? Provide examples.   10
BL-3,4
Q.3   a.   Discuss Data Partitioning and its impact on performance.   10
CO2
BL-4
CO1   b.   Explain the role of Jobs, Stages, and Tasks in Spark application   10
BL-2   execution.
Q.4   a.   Discuss PySpark SQL in detail.   10
CO3
BL-3,4
CO4   b.   Explain windowed operations in Spark Streaming with examples.   10
BL-3,4
Q.5   a.   Discuss the various aggregate functions available in Spark SQL with 10
CO3   examples
BL-3
********** 1 **********
Sensitivity: LNT Construction Internal Use
--- page 2 ---
CO4   b.   Describe the structured streaming model in Spark. How does it 10
BL-4   handle late and out-of-order data?
Q.6   a.   Explain different types of joins in Spark SQL. How can we optimize 10
CO3   join performance?
BL-3,4
CO5   b.   What are the various cluster managers in spark describe them in 10
BL-2   detail?
Q.7   a.   Explain how to manage and monitor spark on Kubernetes.   10
CO5
BL-3
CO3   b.   For the dataset shown in the image below, write a PySpark pseudo- 10
BL-3,4,5   code to answer each question. Clearly mention the Spark functions
used. Explain the logic behind your approach.
• Load and display the dataset
• Count the number of rows and columns
• Get column names and data types
• Check for missing values
• Summary statistics
•   Filter high-quality wine (quality > 7)
• Find the most common wine quality
• Correlation analysis between alcohol and quality
• Find the average alcohol content for each wine quality rating
• Find the number of partitions, what if you were to increase the number of partitions
2
**********   **********
Sensitivity: LNT Construction Internal Use
````

## 2024-25 · Final-Exam · Sem 2 · paper 4ebd29ea5fbc

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/Distributed Data Processing/Distributed Data Processing Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2025
- Text: ocr (2 pages), mean OCR confidence 84.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGEN
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Distributed Data Processing

- Date: 07 May 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100

FINAL EXAMINATION (Acad. Year:2024-2025)

Instructions:

1. This question paper contains 2 pages.

2. Answer to each new question to be started on a fresh page.

3. Figure in right hand side indicates full marks

4. Question No.1 is compulsory

5. Out of remaining questions attempt any 4

6. In total 5 questions needs to be answered

a 7. All Questions carry equal marks
Q.1 1. | Explain the core components of Apache Spark and their role in 4
Col distributed computing. oo
BL-2
CO2 2. | What are the differences between RDDs, Dataframes, and Datasets | 4
BL-2,3,4 in Spark?
CO3 3. | Describe the working of Spark SQL. How does it optimize query | 4
BL-3,4 execution?
CO4 4. | What is the role of Kafka in Spark Streaming? How does Spark | 4
BL-2,3 consume data from Kafka? ; ‘
CO5 5. | Explain different Deployment modes in spark. 4
BL-5
Q.2 a. | Explain the architecture of Apache Spark with a labelled diagram. j 10
col
BL-2
CO2 b. | What are Spark transformations and actions? Provide examples. 10
BL-3,4
Q.3 a. | Discuss Data Partitioning and its impact on performance. 10
CO2
BL-4
col b. | Explain the role of Jobs, Stages, and Tasks in Spark application 10
BL-2 execution.
Q.4 a. | Discuss PySpark SQL in detail. 10
CO3
BL-3,4 :
CO4 b. | Explain windowed operations in Spark Streaming with examples. 10
BL-3,4 -
Q.5 a. | Discuss the various aggregate functions available in Spark SQL with | 10 |
co examples
BL-3

FICK 7] kk ke

Sensitivity: LNT Construction Internal Use
--- page 2 ---
CO4 b. | Describe the structured streaming model in Spark. How does it | 10

BL-4 handle late and out-of-order data?

Q.6 a. | Explain different types of joins in Spark SQL. How can we optimize 10

CO3 join performance?

BL-3,4

COS b. | What are the various cluster managers in spark describe them in | 10

BL-2 detail?

Q.7 a. | Explain how to manage and monitor spark on Kubernetes. 10

COS

BL-3

CO3 b. | For the dataset shown in the image below, write a PySpark pseudo- | 10
7 BL-3,4,5 code to answer each question. Clearly mention the Spark functions

used. Explain the logic behind your approach.

fi ined acidity volatile acidity citricacid| residual su sugar chlorides free sulfur dioxide total sulfur dioxide density [pH sulphates alcohol 7 quality

74) 0.7] 0 19 9.076) li 34] 0.9978} 3.51) 0.56 9.4) 5
7.8] 0.88] i) 2.6 0.098 25} 67| 0.9968) 3.2} 0.68 9.8 5
78 . 0.76| 0.04, 2.3 0.092| i 54] 0.997] 3.26] 0.65 9.8 5
11.2 0.28| 0.56] 19] 0.075 “i 60] 0.998] 3.16] 0.58] 3.8 6
74 0.7] ty) 19 0.076) 14 34) 0.9978} 3.51] 0.56 3.4) 5
74 0.66 0 18 0.075) 13) 40} 0.9978) 3.51] 0.56 94| SI
79) 0.6) 0.06) 16) 0.069) 15) 59] 0.9964) 3.3 0,46 94 5
7.3) 0.65 i) 12 0.065) ph) 21) 0.9946} 3.39) 0.47| 10) 7
7.8) 0.58} 0.02} 2 0.073 3 18] 0.9968) 3.36| 9.57 3.5 7
75 0.5 0.36 6.1 0.071 17 102| 0.9978] 3.35 0.8) 10.5 5
6.7 0.58| 0.08| 18 0.097, b - 65| 0.9959] 3.28] 0.54] 9.2) 5
75 0.5 0.36) 6.1 0.071 V7 102) 0.9978} 3.35 5.8 * 10.5 5
5.6] 0.615) i] 1.6) 0.089] 16) 59] _0,9943) 3.58) 0.52| 3.9 5
7.8} 0.61 0.29) 16} 0.114 9 29| 0.9974 3.26] 156 9.1) 5
8.9) 0.62) 0.18] 3.8 0.176] - 52 145} 0.9986] 3.16) 0.88] 9.2 5
8.9 0.62| 0.19) 3.9 9.17] 51 148] 0.9986] 3.17 9.93 3.2) 5
85 0.28) 0.56) 18) 0.092) 35) 103| 0.9969] 3.3 0,75) 10.5 7

e Load and display the dataset
¢ Count the number of rows and columns
e Get column names and data types
e Check for missing values
e Summary statistics
e Filter high-quality wine (quality > 7)
¢ Find the most common wine quality
¢ Correlation analysis between alcohol and quality
¢ Find the average alcohol content for each wine quality rating
. © Find the number of partitions, what if you were to increase the number of partitions

2


Sensitivity: LNT Construction Internal Use
````
