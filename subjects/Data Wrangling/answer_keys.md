# Data Wrangling: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 04c02c45541b

- Departments: AI and Data Science
- Programmes: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA SCIENCE) - 7056
- Source: `00_Original_Downloads/2025/Semester II/76514__Final-Exam.zip :: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA SCIENCE) - 7056/Data Wrangling/ANS_Final-Exam_Data Wrangling(702DB0C036)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 08 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted
6. All questions carry equal marks
7. Answer to each new question to be started on a fresh page
8. Figures in brackets on the right hand side indicate full marks
9. Assume Suitable data if necessary
Q.1a   Explain descriptive question and inferential question with suitable example in context   5
CO1   to data science?
BL2
Understa
nd
Descriptive question -2.5 marks
Inferential question – 2.5 marks
A descriptive question focuses on summarizing and describing the existing
characteristics of a dataset. It answers questions such as what happened or what is
happening in the data. Descriptive analysis uses statistical measures like mean,
median, frequency distribution, and percentages to summarize data.
Example:
A retail company may ask:
“What was the average monthly sales in 2024?”
The analysis will summarize historical sales data to describe overall performance.
Inferential Question
An inferential question uses sample data to make predictions or generalizations about
a larger population. Inferential analysis applies statistical methods such as hypothesis
testing, confidence intervals, and regression analysis.
Example:
“Based on a sample of customers, can we infer that increasing advertising will
increase sales for the entire market?”
Here, the analyst uses sample data to draw conclusions about a broader population.
Q.1b   A company records advertising expenditure (X) and sales revenue (Y) as follows:   5
CO2   (10, 50), (15, 55), (20, 60), (25, 62), (30, 68)
BL2   Draw a scatter plot for the above data and interpret the pattern observed and explain
Understa   the relationship between the variables
nd
Scatter plot-2 marks
********** 1 **********
--- page 2 ---
Interpretation -3 marks
When the given data points are plotted, the points show an upward trend from left to
right.
Interpretation
As advertising expenditure increases, sales revenue also increases.
The points follow an upward pattern, indicating a positive relationship between the
variables. The points are not perfectly aligned but still show a clear upward direction.
Conclusion
Thus, the scatter plot suggests a moderate positive correlation between advertising
expenditure and sales revenue. Increasing advertising expenditure tends to increase
sales.
Q.1c   Differentiate between OLTP and OLAP system?   5
CO5
BL2
Understa
nd
5 differences- 5 marks
OLTP systems are designed to manage day-to-day business transactions efficiently,
such as banking transactions or order processing.
OLAP systems are designed to analyze large volumes of historical data to support
strategic decision-making, such as sales trend analysis or forecasting.
Basis   OLTP   OLAP
Online Transaction
Meaning   Online Analytical Processing
Processing
Handles daily   Used for analytical processing
Purpose
operational transactions and decision making
Data Type Current operational data Historical and aggregated data
Insert, update, delete
Operations   Complex queries and analysis
transactions
Clerks, customers,   Managers, analysts, decision
Users
operational staff   makers
Q.1d   Explain any two characteristics of data warehouse?   5
CO4
BL2
Understa
nd
Any two characteristics -2.5*2=5 marks
One of the most important characteristics of a Data Warehouse is that it is subject-
oriented. This means that data in a Data Warehouse is organized around major
business subjects rather than around individual applications. In operational systems,
data is usually organized based on specific processes such as order processing,
payroll, or inventory management. However, in a Data Warehouse, data is grouped by
subjects such as customers, products, sales, or finance. This subject-oriented
organization helps analysts study business behavior and performance more effectively,
because data related to a single subject is stored together, even if it originally came
from multiple systems. Another defining characteristic of a Data Warehouse is
********** 2 **********
--- page 3 ---
integration. Organizations typically use many different systems that may store data in
different formats, units, or naming conventions. For example, one system may store
gender as “M” and “F”, while another stores it as “Male” and “Female”. A Data
Warehouse resolves these inconsistencies during data integration. All incoming data is
transformed into a consistent format before being stored. This ensures that when users
analyze data, they are working with a unified and reliable version of information
across the entire organization. A Data Warehouse is also time-variant in nature.
Unlike operational systems that store only current data, a Data Warehouse maintains
historical data over long periods, often several years. Each data record is associated
with a time dimension, such as date, month, quarter, or year. This time-stamped data
allows analysts to perform trend analysis, compare performance over different time
periods, and make forecasts. Without time-variant data, it would be impossible to
understand how a business is evolving. The final key characteristic of a Data
Warehouse is that it is non-volatile. Once data is loaded into the warehouse, it is not
frequently updated or deleted. Instead, new data is periodically added in batches. This
stability ensures that analytical results remain consistent over time. Because data does
not change frequently, users can trust that reports generated today will match reports
generated tomorrow for the same time period.
Q.2a   Explain the lifecycle of Data Science and describe how it can be applied to the use   1
CO1   case of student placement prediction in an educational institution.   0
BL3
Apply
Component   Marks
Explanation of Data Science lifecycle concept with diagram 2
Discovery phase applied to placement prediction   2
Data preparation activities   2
Model planning and model building   2
Operationalization and communication of results   2
Total   10
The Data Science Lifecycle consists of multiple phases that guide the development of
data-driven solutions. These phases include Discovery, Data Preparation, Model
Planning, Model Building, Operationalization, and Communication of Results.
In the Discovery Phase, the problem is clearly defined from a real-world perspective.
In the case of student placement prediction, the objective is to identify students who are
likely to get placed so that institutions can provide better guidance and training.
Stakeholders and Data Scientists work together to determine objectives, available
resources, and expected outcomes.
In the Data Preparation Phase, data related to students is collected and cleaned. This
data may include academic records, attendance, and performance indicators. The data
may contain missing values, duplicate records, or inconsistent formats, which must be
corrected. Data is cleaned, transformed, and converted into a suitable format so that it
can be used effectively for modeling.
In the Model Planning Phase, the problem is identified as a classification problem,
where the system predicts whether a student will be placed or not. Suitable algorithms
and evaluation metrics are selected to guide the model-building process.
********** 3 **********
--- page 4 ---
During the Model Building Phase, the dataset is divided into training and testing sets.
The model learns patterns between student attributes and placement outcomes using
training data. The trained model is then tested on unseen data to evaluate its
performance, and parameter tuning may be performed to improve accuracy.
In the Operationalization Phase, the model is integrated into institutional systems where
it can predict placement outcomes using live data. This helps administrators identify
students who may need additional training.
Finally, in the Communication Phase, the results are presented to faculty members and
administrators through reports or dashboards so that they can take appropriate actions
to improve student placement outcomes.
Q.2b   The marks of students are: 55, 57, 56, 58, 60, 59, 95. Detect the outlier using both Z-   1
CO2   score (consider population data) and IQR methods.   0
BL3
Apply
Step   Marks
Mean calculation   2
Standard deviation calculation   2
Z-score calculation for all values   2
Q1, Q3 and IQR calculation   2
Identification of outlier using both methods 2
Mean=62.86
Standard deviation =13.22
Z-scores
Value Z-score
55   -0.59
57   -0.44
56   -0.52
58   -0.37
60   -0.22
59   -0.29
95   2.43
No Z-score outlier.
IQR
Sorted
55, 56, 57, 58, 59, 60, 95
Q1 = 56
Q3 = 60
IQR = 4
Upper bound = 66
95 is an outlier.
Q.3a   What are Label Encoding and One-Hot Encoding techniques in machine learning   1
CO2   preprocessing? A dataset contains a column “Vehicle Type” with categories Car, Bus,   0
BL3   Motorcycle, Bicycle, and Truck. Explain the methods and perform both Label
Apply   Encoding and One-Hot Encoding.
Explanation of Label Encoding – 2 marks
Explanation of One-Hot Encoding – 2 marks
Correct Label Encoding mapping – 3 marks
Correct One-Hot Encoding columns – 3 marks
********** 4 **********
--- page 5 ---
Label Encoding:
Label Encoding converts categorical values into numeric labels, where each category
is assigned a unique integer.
One-Hot Encoding:
One-Hot Encoding converts each category into a separate binary column indicating
presence (1) or absence (0).
Label Encoding
Bicycle → 0
Bus → 1
Car → 2
Motorcycle → 3
Truck → 4
One-Hot Encoding
Vehicle_Bicycle
Vehicle_Bus
Vehicle_Car
Vehicle_Motorcycle
Vehicle_Truck
Each column contains 1 if the record belongs to that category otherwise 0. (Must be shown
in tabular format)
Q.3b   Explain Max-Abs Scaling and Robust Scaling. A column named “Monthly Product   1
CO2   Sales” contains seven values: 40, 55, 70, 65, 90, 60 and 50. Apply Max-Abs Scaling   0
BL3   and Robust Scaling to this data.
Apply
Explanation of Robust Scaling and formula – 3 marks
Explanation of Max-Abs Scaling and formula– 3 marks
Robust scaling calculations – 2 marks
Max-Abs scaling calculations – 2 marks
1. Max-Abs Scaling : Max-Abs Scaling divides every value by the maximum absolute
value, scaling data to the range [-1,1].
x' = {x} / { |x_{max}| }
Maximum value = 90
Scaled values
40 → 0.44
55 → 0.61
70 → 0.78
65 → 0.72
90 → 1
60 → 0.67
50 → 0.56
2. Robust Scaling Robust Scaling uses the median and interquartile range (IQR) to
scale the data, making it less sensitive to outliers.
x' = x - x_{median} /{IQR}
Sorted values
40, 50, 55, 60, 65, 70, 90
Median = 60
Q1 = 50
Q3 = 70
IQR = 20
********** 5 **********
--- page 6 ---
Scaled values
40 → -1
55 → -0.25
70 → 0.50
65 → 0.25
90 → 1.50
60 → 0
50 → -0.50
Q.4a   Write the code and corresponding output for each of the following:   1
CO3   i) Create a NumPy array using arange() from 50 to 53 (included).   0
BL3   ii) Convert the array into 2 × 2 matrix.
Apply   iii) Print the matrix size.
iv) Print the number of dimensions of matrix.
v) Extract the last row of 2 × 2 matrix.
Part   Marks
i   2
ii   2
iii   2
iv   2
v   2
import numpy as np
arr = np.arange(50,54)
matrix = arr.reshape(2,2)
print(matrix.size)
print(matrix.ndim)
print(matrix[1, : : ])
Array
[50 51 52 53]
Matrix
[[50 51]
[52 53]]
Size = 4
Dimensions = 2
Slice [52 53]
Q.4b   Create two 3 × 3 NumPy arrays.   1
CO3   Array A contains 2, 4, 6; 8, 10, 12; 14, 16, 18.   0
BL3   Array B contains 1, 3, 5; 7, 9, 11; 13, 15, 17.
Apply   Using nested for loops, perform following and show the output:
a) Element-wise subtraction (Array A - Array B)
b) Element-wise division (Array A/Array B)
Creating two arrays – 2 marks
Correct nested loop structure – 2 marks
Element-wise subtraction logic – 3 marks
Element-wise divison logic – 3 marks
import numpy as np
A = np.array([[2,4,6],
[8,10,12],
[14,16,18]])
B = np.array([[1,3,5],
[7,9,11],
[13,15,17]])
********** 6 **********
--- page 7 ---
sub = np.zeros((3,3))
div = np.zeros((3,3))
for i in range(3):
for j in range(3):
sub[i][j] = A[i][j] - B[i][j]
div[i][j] = A[i][j] / B[i][j]
print(sub)
print(div)
Subtraction
[[1 1 1]
[1 1 1]
[1 1 1]]
Division (approx)
[[2.00 1.33 1.20]
[1.14 1.11 1.09]
[1.08 1.07 1.06]]
Q.5a   Create a DataFrame employee_df with columns: Employee_ID, Salary, Experience, 1
CO3   Gender, Department   0
BL3   The rows are:
Apply   Rows:
Row1: 201, 50000, 3, Male, HR
Row2: 202, Salary missing, 5, Female, Finance
Row3: 203, 60000, Experience missing, Male, IT
Row4: 204, 55000, 4, Female, Marketing
Row5: 205, 52000, 2, Male, IT
Perform the following with appropriate code:
i) Create the DataFrame
ii) Select Employee_ID, Salary, Department (without loc/iloc)
iii) Write code to check sum of missing values in each column
iv) Replace missing values using mean of the respective column.
Part   Marks
i   4
ii   2
iii   2
iv   2
import pandas as pd
import numpy as np
data = {
"Employee_ID":[201,202,203,204,205],
"Salary":[50000,np.nan,60000,55000,52000],
"Experience":[3,5,np.nan,4,2],
"Gender":["Male","Female","Male","Female","Male"],
"Department":["HR","Finance","IT","Marketing","IT"]
}
employee_df = pd.DataFrame(data)
print(employee_df[["Employee_ID","Salary","Department"]])
print(employee_df.isnull().sum())
employee_df["Salary"].fillna(employee_df["Salary"].mean(), inplace=True)
employee_df["Experience"].fillna(employee_df["Experience"].mean(), inplace=True)
print(employee_df)
********** 7 **********
--- page 8 ---
Q.5b   Given DataFrame employee_df   1
CO3   Emp_ID Salary Experience Gender Department   0
BL3   0   201 50000   3   Male   HR
Apply   1   202 60000   5   Female Finance
2   203 55000   4   Male   IT
3   204 65000   6   Female HR
4   205 52000   2   Male   IT
5   206 58000   4   Female Finance
6   207 62000   5   Male   HR
i) What will be output of print(employee_df.head(4))
ii) What will be output of employee_df.iloc[1:4,1:3]
iii) Write query where Salary > 55000 OR Department = IT. Also write the output.
iv) Write code to Sort dataframe by Salary and show output.
v)Write   code   to   rename   columns   using   rename   function   for:
Emp_ID → EmployeeID, Salary → Income, Experience → Exp.
Part   Marks
i   1
ii   2
iii   3
iv   2
v   2
i) Output
Emp_ID Salary Experience Gender Department
0   201 50000   3 Male   HR
1   202 60000   5 Female Finance
2   203 55000   4 Male   IT
3   204 65000   6 Female   HR
ii) Output
Salary Experience
1 60000   5
2 55000   4
3 65000   6
iii) Query
employee_df[(employee_df["Salary"]>55000) | (employee_df["Department"]=="IT")]
Output
Emp_ID Salary Experience Gender Department
1   202 60000   5 Female Finance
2   203 55000   4 Male   IT
3   204 65000   6 Female   HR
4   205 52000   2 Male   IT
5   206 58000   4 Female Finance
6   207 62000   5 Male   HR
iv) Code
employee_df.sort_values(by="Salary")
Emp_ID Salary Experience Gender Department
0   201 50000   3 Male   HR
4   205 52000   2 Male   IT
2   203 55000   4 Male   IT
********** 8 **********
--- page 9 ---
5   206 58000   4 Female   Finance
1   202 60000   5 Female   Finance
6   207 62000   5 Male   HR
3   204 65000   6 Female HR
v) Code
employee_df.rename(columns={"Emp_ID":"EmployeeID","Salary":"Income","Experi
ence":"Exp"}, inplace=True)
Q.6a   Explain the concept of OLAP systems and their role in analytical processing.   1
CO4   0
BL2
Understa
nd
Definition of OLAP – 2
Characteristics – 4
Role in analysis and example – 4
OLAP (Online Analytical Processing) refers to systems designed to support complex
data analysis rather than routine transaction processing. These systems are mainly
used by managers, analysts, and decision-makers to analyze large volumes of
historical data.
Unlike OLTP systems, which focus on frequent updates and transaction processing,
OLAP systems focus on reading large amounts of data and performing complex
queries. These queries often involve aggregations, summaries, comparisons, and trend
analysis across different dimensions such as time, location, and product category.
OLAP systems usually operate on data stored in data warehouses. The data warehouse
stores integrated historical data collected from multiple operational systems.
For example, business analysts may use OLAP systems to analyze sales performance
across different regions over several years. This type of analysis requires scanning
large datasets and performing complex calculations, which OLAP systems are
designed to handle efficiently.
Thus, OLAP systems play a crucial role in business intelligence and strategic decision-
making.
Q.6b   Explain all the stages of the ETL process.   1
CO5   0
BL2
Understa
nd
Extraction-3
Transformation-4
Loading-3
Extraction is the first stage of the ETL process. It involves identifying and retrieving
data from various source systems so that it can be processed further and loaded into
the data warehouse. Source systems may include operational databases, enterprise
applications, flat files, spreadsheets, or external data feeds. These systems are
designed for operational tasks rather than analytical purposes, so their data structures
may differ significantly. Extraction can be performed in two ways: full extraction and
incremental extraction. Full extraction retrieves all available data from the source
system, while incremental extraction retrieves only new or modified records since the
previous extraction. Incremental extraction is commonly used because it reduces
processing time and system load.
Transformation is the second stage of the ETL process and is considered the most
complex stage. In this stage, extracted data is converted into a consistent and analysis-
ready format before being loaded into the data warehouse. Major transformation
activities include:
********** 9 **********
--- page 10 ---
• Data cleaning – removing duplicates, correcting invalid entries, and handling
missing values.
• Data integration – combining data from different systems into a unified structure.
• Data standardization – converting data into consistent formats such as common date
formats or currencies.
• Aggregation – summarizing detailed transactional data into higher-level metrics such
as monthly or yearly totals.
These transformations ensure that the data warehouse contains reliable and consistent
information suitable for analytical processing.
Loading is the final stage of the ETL process in which transformed data is stored in the
data warehouse. The goal of this stage is to ensure that cleaned and integrated data is
placed correctly into warehouse tables for analytical use. Loading may occur in batch
mode or near real-time mode, depending on business requirements. In batch loading,
large volumes of data are loaded periodically, such as daily or weekly. In real-time
loading, data is updated continuously or at very short intervals. During loading, data is
inserted into fact tables and dimension tables according to the warehouse schema such
as star schema or snowflake schema. Indexes and constraints may also be applied to
improve query performance and maintain data integrity.
Q.7a   What is meant by data quality tool. Explain data profiling and data validation for data 1
CO5   quality tool functions.   0
BL2
Understa
nd
Data Quality tool functions – 2
Data profiling – 4
Data validation – 4
A data quality tool is not a single cleaning program. Instead, it is a comprehensive
software system designed to analyze, control, improve, and continuously monitor the
quality of data used in analytics, reporting, and data science projects. These tools are
widely used in industries such as banking, healthcare, e-commerce, telecom, and
government systems. Data Profiling Data profiling is the starting point of all data
quality activities. Technically, data profiling means examining the structure and actual
content of data before making any changes to it. At this stage, the tool scans each
column of the dataset to understand what kind of values exist, how frequently they
appear, and whether they follow expected patterns. For example, if we consider a
student database, data profiling may reveal that the “Age” column contains values like
18, 19, 20, but also values such as 3 or 150. It may also show that some records have
missing roll numbers or that names appear in different formats. Importantly, profiling
does not correct anything; it only provides visibility into hidden data problems.
Without profiling, organizations work blindly.
Data Validation Once data behavior is understood, the next function is data validation.
Data validation checks whether data conforms to predefined rules. These rules are based
on business logic and domain constraints. For instance, in an academic system,
validation rules ensure that internal marks do not exceed the maximum limit, dates of
admission are not in the future, and semester numbers fall within a valid range. If a
record violates a rule, it is flagged as invalid. Validation acts as a quality gate,
preventing incorrect data from flowing into downstream systems such as data
warehouses or analytics platforms.
Q.7b   Explain the concept of unit testing and system testing in data warehouse?   1
CO4   0
BL2
Understa
nd
Unit testing -5
********** 10 **********
--- page 11 ---
System testing -5
Data warehouse testing is performed at four progressive levels, where each level
checks correctness from a different perspective. These levels move from small
isolated components to complete business validation, ensuring reliability at every
stage. The first level is Unit Testing, where individual components such as ETL jobs,
transformations, and calculations are tested independently. The goal here is to ensure
that each small piece of logic works exactly as intended before it interacts with
anything else. The second level is Integration Testing, where we verify that different
components of the data warehouse work correctly together. This includes checking
data flow from source systems to staging areas and finally into warehouse tables.
Unit testing in data warehousing refers to the process of verifying individual data
warehouse components in isolation. These components typically include ETL jobs,
data transformations, calculations, constraints, and validation rules. At this stage, we
do not test the entire data flow. Instead, we focus on one transformation or one rule at
a time, ensuring it produces the correct output for a given input. This approach helps
identify errors at an early stage, when they are easier and cheaper to fix. For example,
if an ETL job converts sales amounts from dollars to rupees, unit testing ensures that
the conversion formula is mathematically correct and consistently applied. Key Focus
Areas One major focus area of unit testing is data transformations. In a data
warehouse, raw data is rarely used directly. It is transformed according to business
rules-for example, categorizing customers as “Premium” or “Regular” based on
purchase value. Unit testing ensures that these rules are implemented correctly and
consistently. Another important focus area is calculations. Data warehouses store
derived metrics such as total revenue, average order value, profit margin, and growth
percentage. Unit testing verifies the accuracy of these calculations so that reports do
not show misleading numbers. Unit testing also checks data types and formats. This
ensures that date fields, numeric fields, and string fields are stored in the correct
format. For instance, a date should not be stored as text, and numeric fields should not
contain invalid characters. Finally, constraints and validation rules are tested. This
includes checks such as primary key uniqueness, non null constraints, and referential
integrity. These validations prevent incorrect or incomplete data from entering the
warehouse.
System testing is performed to evaluate the complete data warehouse system as a
whole. It ensures that the entire system meets the specified requirements and functions
correctly under realistic conditions.
During system testing, all components such as data extraction, transformation, loading
processes, databases, and reporting tools are tested together. The goal is to ensure that
the entire workflow operates smoothly.
System testing verifies several aspects, including data accuracy, query performance,
and system reliability. For example, testers may run complex analytical queries to
confirm that the system produces correct results within acceptable response times.
Another important aspect of system testing is identifying performance bottlenecks.
Since data warehouses process large volumes of data, system testing ensures that the
system can handle expected workloads.
Thus, system testing ensures that the data warehouse operates effectively as a
complete system.
A real-world example of an online shopping company like Amazon or Flipkart. Data
is coming from customer orders, payment systems, delivery partners, and inventory
databases. System testing checks whether a customer’s order placed today is correctly
reflected in sales dashboards, inventory reports, revenue summaries, and management
analytics - from start to finish, without any breaks or inconsistencies.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper ccbae41db91f

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AIDS_7056/Data Wrangling/ANS_Data Wrangling(702DB0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MBA Tech (DS)
Year: II / III / IV/Semester III/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
a.   • Data wrangling is the process of cleaning, transforming, and organizing raw data   [5]
into a usable format. (1)
• Improves data quality and consistency. (1)
• Fixes missing, duplicate, and erroneous values. (1)
• Makes data ready for analysis and modeling. (1)
• Leads to better decision-making with accurate insights. (1)
b.   • OLTP handles transactional, day-to-day operations; OLAP handles analytical,   [5]
decision-support queries. (1)
• OLTP deals with many small, simple transactions; OLAP handles fewer but
complex queries. (1)
• OLTP   uses   normalized   relational   data;   OLAP   uses
denormalized/multidimensional data. (1)
• OLTP focuses on real-time processing; OLAP often on batch or scheduled
processing. (1)
• OLTP is optimized for speed and concurrency; OLAP is optimized for query
performance and insights. (1)
c.   • Data Owner – Defines rules, ensures correct usage of data. (1)   [5]
• Data Steward – Maintains data accuracy, consistency, and governance. (1)
• ETL Developer – Implements validation and cleaning in ETL pipelines. (1)
• Data Quality Analyst – Profiles, monitors, and reports data quality issues. (1)
• Management – Sets policies, provides resources, ensures compliance. (1)
d.   • Data cleaning (handling missing or invalid values). (1)   [5]
• Data standardization or formatting into consistent structure. (1)
• Data aggregation or summarization for analysis. (1)
• Data merging or joining from multiple sources. (1)
********** 1 **********
--- page 2 ---
• Creation of derived or calculated fields. (1)
Q2   [20]
CO-   a. # Import libraries   [10]
2 ;B   import pandas as pd
L-3   import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("sales_data.csv")
# Basic EDA
df.head()   # first 5 rows
df.tail()   # last 5 rows
df.info()   # data types, nulls
df.describe()   # statistics
# Check missing values
df.isnull().sum()
# Univariate Visualization
plt.hist(df['Sales'])   # histogram of sales
sns.boxplot(x='Region', y='Sales', data=df) # boxplot
# Bivariate Visualization
sns.scatterplot(x='Sales', y='Profit', data=df) # scatter
sns.barplot(x='Region', y='Sales', data=df)   # avg sales by region
# Correlation Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True)
# Show plots
plt.show()
(OR)
# Load data
df <- read.csv("sales_data.csv")
# Display first 10 rows
head(df, 10)
# Display last 5 rows
tail(df, 5)
# Extract only the first column
df[, 1]   # or df[[1]] or df$ColumnName
# Determine data type of the second column
class(df[, 2]) # or str(df[,2]) or typeof(df[,2])
# Convert entire data frame to matrix
mat <- as.matrix(df)
b. # Create vect1 with odd numbers from 100 to 50   [10]
CO-   vect1 <- seq(99, 51, by = -2)
3 ;B   # Arrange in ascending order
vect1 <- sort(vect1)
L-3   # Total number of elements
length(vect1) # Output: 25
# Check dimension
dim(vect1)   # Output: NULL (because it is a 1D vector)
# Index of number 61
which(vect1 == 61)
OR
# Create list1 with odd numbers from 100 to 50
********** 2 **********
--- page 3 ---
list1 = list(range(99, 50, -2))
# Arrange in ascending order
list1.sort()
# Total number of elements
len(list1) # Output: 25
# Check dimension
# Lists in Python are 1D by default
# So dimension = 1D (no rows/columns unless nested)
# Index of number 61
list1.index(61)
o/p
•   vect1: 99, 97, 95, …, 51
• Total elements = 25
• Dimension = NULL (1D vector)
•   Index of 61 = position number in vector
Q3   [20]
CO-   a.   # i. Create dataset and store in DataFrame (2 Marks)   [10]
2 ;   import pandas as pd
BL-3   import numpy as np
df = pd.DataFrame({
'ID':[1,2,3,4,5,6,7,8,9,10],
'Dept':['HR','IT','Fin','IT','HR','Fin','IT','HR','Fin','IT'],
'Exp':[3,6,4,7,2,5,3,4,8,2],
'Salary':[48000,75000,60000,92000,42000,78000,67000,np.nan,87000,62000
],
'Projects':[2,7,5,10,3,6,4,3,9,np.nan],
'Promotion':['No','Yes','No','Yes','No','Yes','No','No','Yes','No']
})
# ii. Mean of Exp (1 Mark)
mean_exp = df['Exp'].mean()
# iii. Fill NaN values with justification (4 Marks)
df['Salary'].fillna(df['Salary'].median(), inplace=True) # Median is robust to
salary outliers
df['Projects'].fillna(df['Projects'].mean(), inplace=True) # Mean reasonable
for project counts
# iv. Dept with highest number of projects (2 Marks)
dept_projects = df.groupby('Dept')['Projects'].sum()
highest_dept = dept_projects.idxmax()
# v. Delete Promotion field (1 Mark)
df.drop('Promotion', axis=1, inplace=True)
# i. Create dataset and store in data frame (2 Marks)
df <- data.frame(
ID = c(1,2,3,4,5,6,7,8,9,10),
Dept = c("HR","IT","Fin","IT","HR","Fin","IT","HR","Fin","IT"),
Exp = c(3,6,4,7,2,5,3,4,8,2),
Salary   =
c(48000,75000,60000,92000,42000,78000,67000,NA,87000,62000),
Projects = c(2,7,5,10,3,6,4,3,9,NA),
Promotion = c("No","Yes","No","Yes","No","Yes","No","No","Yes","No")
********** 3 **********
--- page 4 ---
)
# ii. Mean of Exp (1 Mark)
mean_exp <- mean(df$Exp, na.rm = TRUE)
# iii. Fill NA values with justification (4 Marks)
df$Salary[is.na(df$Salary)] <- median(df$Salary, na.rm = TRUE) # Median
handles salary outliers
df$Projects[is.na(df$Projects)] <- mean(df$Projects, na.rm = TRUE) # Mean
is fine for counts
# iv. Dept with highest number of projects (2 Marks)
dept_projects <- tapply(df$Projects, df$Dept, sum)
highest_dept <- names(which.max(dept_projects))
# v. Delete Promotion field (1 Mark)
df$Promotion <- NULL
O/P
CO-   b.   [10]
3 ;   OR
BL-3   import numpy as np
import string
# Part A: Argsort of an array (2 Marks)
A1 = np.array([1, 2, 3, 40, 50, 80, 200, 500])
A2 = np.array([2, 5, 1, 8, 3])
print(A2.argsort())
# Output: [2 0 4 1 3]
# Explanation: Returns indices that would sort A2 in ascending order (0-based
indexing)
# Part B: Reshape and ravel (2 Marks)
B1 = np.arange(1, 21).reshape(5, 4)
print(B1)
# Output: 5x4 matrix
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]
# [13 14 15 16]
# [17 18 19 20]]
print(B1.ravel(order='F'))
# Output: [ 1 5 9 13 17 2 6 10 14 18 3 7 11 15 19 4 8 12 16 20]
# Explanation: Flatten matrix in **column-major order** ('F')
********** 4 **********
--- page 5 ---
# Part C: Transpose of column vector (2 Marks)
C1 = np.arange(1, 5).reshape(4, 1)
print(C1.T)
# Output: [[1 2 3 4]]
# Explanation: C1 is 4x1 column vector, transpose gives 1x4 row
# Part D: List slicing (2 Marks)
D1 = list(string.ascii_lowercase)
print(D1[-20:-1])
# Output: ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
# Explanation: Negative slicing removes first 6 elements (0-based), includes positions
-20 to -2
# Additional 2 Marks: Code correctness, explanation clarity, and proper use of
libraries
Q4   [20]
CO-   a.   • Data Profiling: Analyzes datasets to identify inconsistencies, patterns,   [5]
2 ;   missing values, and anomalies. (1 mark)
BL-2   • Data Cleansing: Detects and corrects errors such as duplicates, missing
values, or incorrect formats. (1 mark)
• Data Standardization: Ensures uniform formats for dates, addresses, codes,
and other fields. (1 mark)
• Data Validation: Checks data against predefined rules or business logic to
ensure accuracy and consistency. (1 mark)
• Monitoring & Reporting: Tracks data quality over time, generating alerts and
reports for continuous improvement. (1 mark)
CO-   b. ODBC (Open Database Connectivity) in ETL:   [5]
3 ;
BL-2   • ODBC provides a standard interface to connect ETL tools to various data
sources (databases, spreadsheets, etc.).
• ETL tools use ODBC drivers to extract data from heterogeneous sources
without worrying about source-specific APIs.
• Ensures interoperability: the same ETL workflow can connect to SQL
Server, Oracle, MySQL, or other ODBC-compliant sources.
• Supports data extraction, transformation, and loading by enabling ETL
scripts to read/write data consistently.
Example:
1. Configure ODBC DSN (Data Source Name) for the source database.
2. Use ETL tool to connect via the DSN.
3. Extract data, apply transformations, and load into target data warehouse.
CO-   c.   •   Description of layers (6 marks)   [10]
2 ;   • Explanation of ETL (2 marks)
BL-3   • Labeled diagram (2 marks)
Q5   [20]
CO-   a. Importance of Data Warehouse Security Mechanisms:   [5]
2 ;
BL-2   •   Protects sensitive data: Ensures financial, personal, and business-critical data
is safe from unauthorized access. (1 mark)
********** 5 **********
--- page 6 ---
• Access control: Restricts data access based on user roles and responsibilities,
preventing data misuse. (1 mark)
• Data integrity: Prevents unauthorized modifications, ensuring accurate and
reliable data for decision-making. (1 mark)
• Auditing and compliance: Tracks who accessed or modified data, helping
meet legal and regulatory requirements. (1 mark)
• Prevents data breaches: Safeguards against cyber-attacks, maintaining trust
and continuity in business operations. (1 mark)
CO-   b. Temporal Data in Data Warehouse:   [5]
3 ;
BL-2   • Temporal data changes over time, e.g., salary or price history.
• Loading: Initial load inserts current records with start/end dates; incremental
load updates only changes.
• Maintenance:
o SCD Type 1: Overwrite old data (no history).
o SCD Type 2: Add new records to preserve history.
o SCD Type 3: Store limited history in extra columns.
• Purpose: Supports historical analysis and accurate decision-making.
CO-   c.   1. Problem Discovery: Identify and understand the business problem, define   [10]
1 ;B   objectives, and frame it as a data science question.
L-3   2. Data Collection: Gather relevant data from multiple sources such as databases,
APIs, sensors, or external datasets.
3. Data Preparation: Clean, transform, and integrate data; handle missing values,
outliers, and inconsistencies; create features for analysis.
4. Exploratory Data Analysis (EDA): Explore data patterns, correlations, and
distributions; visualize data to gain insights.
5. Model Planning: Select suitable algorithms, define performance metrics, and
design experiments.
6. Model Building: Train machine learning/statistical models on prepared data;
optimize hyperparameters.
7. Model Evaluation: Validate model performance on test/validation sets; check
accuracy, precision, recall, or other relevant metrics.
8. Deployment / Operationalize: Integrate the model into production systems for
real-time or batch predictions.
9. Monitoring and Maintenance: Continuously monitor model performance, retrain
if data distribution changes.
10. Communicate Results: Present findings, visualizations, and actionable insights
to stakeholders; support decision-making.
Q 6   [20]
CO-   a.   • Batch Transfer: Periodically move large volumes of data in scheduled [10]
3 ;   intervals (daily, weekly) from the warehouse to near-line storage.
BL-3
• Incremental Transfer: Only changed or new records are transferred, reducing
bandwidth and storage usage.
• ETL Pipelines: Use Extract, Transform, Load processes to format and clean
data before moving it to near-line storage.
• Data Compression & Archiving: Compress data to save storage and archive
less frequently accessed data.
• Automated Scheduling & Monitoring: Use scripts or ETL tools to automate
transfers, monitor errors, and ensure data consistency.
********** 6 **********
--- page 7 ---
• Purpose: Provides cost-effective storage, preserves historical data, and
maintains accessibility for reporting and analytics.
CO-   b. Definition:   [10]
2 ;
BL-2
• Process of detecting and correcting errors, inconsistencies, or inaccuracies in
data to ensure high-quality datasets. (1 Mark)
Reasons for Data Cleaning:
• Missing values due to incomplete records or human/system errors. (1 Mark)
•   Inaccurate data or typos. (1 Mark)
• Duplicate records causing redundancy. (1 Mark)
•   Inconsistent formats (dates, currencies, units). (1 Mark)
•   Outliers and noisy data affecting analysis. (1 Mark)
Sources of Dirty Data:
• Manual data entry errors. (0.5 Mark)
•   Integration from multiple heterogeneous sources. (0.5 Mark)
• System errors or software/hardware glitches. (0.5 Mark)
•   External data sources (APIs, web scraping, third-party datasets). (0.5 Mark)
Steps Involved in Data Cleaning:
• Data Profiling: Detect missing values, duplicates, and inconsistencies. (1
Mark)
• Handling Missing Values: Impute with mean/median/mode or remove
records. (1 Mark)
•   Correcting Errors: Fix typos and inconsistent formats. (1 Mark)
• Removing Duplicates: Eliminate redundant records. (1 Mark)
•   Standardization: Uniform formats for dates, currencies, and categorical data.
(1 Mark)
• Handling Outliers & Noise: Remove, cap, or transform extreme values. (1
Mark)
•   Validation: Verify cleaned data against rules or source systems. (1 Mark)
Q 7   [20]
CO-   a.   •   Definition:   [10]
2 ;   • Metadata is “data about data” that describes the structure, content, source,
BL-2   and usage of data in the warehouse. (1 Mark)
•   Functions:
• Data Source Description: Documents the origin, type, format, and
relationships of data in the warehouse. (1 Mark)
• ETL Support: Provides rules, mappings, transformations, and lineage
information to guide extraction, transformation, and loading processes. (1
Mark)
• Data Quality Management: Tracks accuracy, completeness, consistency, and
errors in data. (1 Mark)
• Query Optimization: Supplies indexing, aggregation, and summary
information to improve query performance. (1 Mark)
• Business Rules & Definitions: Stores definitions of measures, dimensions,
and metrics to ensure consistent interpretation. (1 Mark)
********** 7 **********
--- page 8 ---
• Audit & Compliance: Maintains information on data access, updates, and
modifications for auditing purposes. (1 Mark)
• Versioning & Change Management: Records changes in data structure,
schema evolution, and historical versions of datasets. (1 Mark)
• User Guidance & Reporting: Helps analysts understand the meaning, source,
and usage of data for reporting and decision-making. (1 Mark)
•   Integration Support: Assists in merging data from heterogeneous sources by
providing structural and semantic metadata. (1 Mark)
• Documentation & Communication: Acts as a central reference for
developers, administrators, and end-users. (1 Mark)
CO-   b.   •   Definition:   •
3 ;   • An ODS is a centralized database that integrates data from multiple
BL-3   operational systems, providing a current, consolidated view of transactional
data.
• Data Characteristics:
• Contains current or near-real-time data.
• Mostly detailed, granular records rather than aggregated summaries.
• Frequently updated, reflecting ongoing operational transactions.
• Core Technology:
•   Built on relational database systems.
• Supports high-speed inserts, updates, and queries.
• Often acts as a staging area for the data warehouse.
• Record Profiling:
• Monitors data for completeness, consistency, and validity.
• Ensures correct data types, ranges, and formats for operational analysis.
•   Classification:
• Type 1: Short-term operational reporting (e.g., daily sales).
• Type 2: Intermediate store between OLTP systems and data warehouse.
• Can be application-specific (HR, Finance, Sales) or enterprise-wide.
• Purpose:
• Provides real-time or near-real-time reporting without impacting source
systems.
• Supports operational decision-making and data quality checks before loading
into the data warehouse.
********** 8 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 040e74e41a72

- Departments: Data Science
- Programmes: BTech CSE DS 7057, BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSE_DS_7057/Data Wrangling/ANS_Data Wrangling(702DB0C036)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100
- Text: mixed (23 pages), mean OCR confidence 47.5
- 92 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
Program: B.Tech/MBATech/BTI   Year: II/II/IV Semester: III/III/VII
Stream: Data Science
Subject: Data Wrangling   Time:
Date:   No. of Pages: 10
Marks: 100
Synoptic Answers
Q1   Answer briefly:   [20]
a.    Data wrangling is the process of cleaning, transforming, and organizing raw data into
a usable format. (1)
 Improves data quality and consistency. (1)
 Fixes missing, duplicate, and erroneous values. (1)   [5]
 Makes data ready for analysis and modeling. (1)
 Leads to better decision-making with accurate insights. (1)
Above are keyword need to check. With detiled explaination marks will be given.
b.
[5]

1
--- page 2 ---
c.
[5]

d.    Data cleaning (handling missing or invalid values). (1)
 Data standardization or formatting into consistent structure. (1)
 Data aggregation or summarization for analysis. (1)   [5]
 Data merging or joining from multiple sources. (1)
 Creation of derived or calculated fields. (1)
Q2   [20]
a. # Import libraries
import pandas as pd
import matplotlib.pyplot as plt
CO-2   import seaborn as sns   [10]
;BL-3
# Load dataset
df = pd.read_csv("sales_data.csv")
# Basic EDA
2
--- page 3 ---
df.head()   # first 5 rows
df.tail()   # last 5 rows
df.info()   # data types, nulls
df.describe()   # statistics
# Check missing values
df.isnull().sum()
# Univariate Visualization
plt.hist(df['Sales'])   # histogram of sales
sns.boxplot(x='Region', y='Sales', data=df) # boxplot
# Bivariate Visualization
sns.scatterplot(x='Sales', y='Profit', data=df) # scatter
sns.barplot(x='Region', y='Sales', data=df) # avg sales by region
# Correlation Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True)
# Show plots
plt.show()
(OR)
# Load data
df <- read.csv("sales_data.csv")
# Display first 10 rows
head(df, 10)
# Display last 5 rows
tail(df, 5)
# Extract only the first column
df[, 1]   # or df[[1]] or df$ColumnName
# Determine data type of the second column
class(df[, 2]) # or str(df[,2]) or typeof(df[,2])
# Convert entire data frame to matrix
mat <- as.matrix(df)
3
--- page 4 ---
b. # Create vect1 with odd numbers from 100 to 50
vect1 <- seq(99, 51, by = -2)
# Arrange in ascending order
vect1 <- sort(vect1)
# Total number of elements
length(vect1) # Output: 25
# Check dimension
dim(vect1)   # Output: NULL (because it is a 1D vector)
# Index of number 61
which(vect1 == 61)
OR
# Create list1 with odd numbers from 100 to 50
list1 = list(range(99, 50, -2))
# Arrange in ascending order
CO-3   [10]
list1.sort()
;BL-3
# Total number of elements
len(list1) # Output: 25
# Check dimension
# Lists in Python are 1D by default
# So dimension = 1D (no rows/columns unless nested)
# Index of number 61
list1.index(61)
o/p
   vect1: 99, 97, 95, …, 51
 Total elements = 25
 Dimension = NULL (1D vector)
   Index of 61 = position number in vector
Q3   [20]
4
--- page 5 ---
a.   # i. Create dataset and store in DataFrame (2 Marks)
import pandas as pd
import numpy as np
df = pd.DataFrame({
'ID':[1,2,3,4,5,6,7,8,9,10],
'Dept':['HR','IT','Fin','IT','HR','Fin','IT','HR','Fin','IT'],
'Exp':[3,6,4,7,2,5,3,4,8,2],
'Salary':[48000,75000,60000,92000,42000,78000,67000,np.nan,87000,62000],
'Projects':[2,7,5,10,3,6,4,3,9,np.nan],
'Promotion':['No','Yes','No','Yes','No','Yes','No','No','Yes','No']
})
# ii. Mean of Exp (1 Mark)
mean_exp = df['Exp'].mean()
# iii. Fill NaN values with justification (4 Marks)
CO-2   df['Salary'].fillna(df['Salary'].median(), inplace=True) # Median is robust to
; BL-   salary outliers   [10]
3   df['Projects'].fillna(df['Projects'].mean(), inplace=True) # Mean reasonable for
project counts
# iv. Dept with highest number of projects (2 Marks)
dept_projects = df.groupby('Dept')['Projects'].sum()
highest_dept = dept_projects.idxmax()
# v. Delete Promotion field (1 Mark)
df.drop('Promotion', axis=1, inplace=True)
# i. Create dataset and store in data frame (2 Marks)
df <- data.frame(
ID = c(1,2,3,4,5,6,7,8,9,10),
Dept = c("HR","IT","Fin","IT","HR","Fin","IT","HR","Fin","IT"),
Exp = c(3,6,4,7,2,5,3,4,8,2),
Salary = c(48000,75000,60000,92000,42000,78000,67000,NA,87000,62000),
Projects = c(2,7,5,10,3,6,4,3,9,NA),
5
--- page 6 ---
Promotion = c("No","Yes","No","Yes","No","Yes","No","No","Yes","No")
)
# ii. Mean of Exp (1 Mark)
mean_exp <- mean(df$Exp, na.rm = TRUE)
# iii. Fill NA values with justification (4 Marks)
df$Salary[is.na(df$Salary)] <- median(df$Salary, na.rm = TRUE) # Median
handles salary outliers
df$Projects[is.na(df$Projects)] <- mean(df$Projects, na.rm = TRUE) # Mean is
fine for counts
# iv. Dept with highest number of projects (2 Marks)
dept_projects <- tapply(df$Projects, df$Dept, sum)
highest_dept <- names(which.max(dept_projects))
# v. Delete Promotion field (1 Mark)
df$Promotion <- NULL
b.
CO-3
; BL-
[10]
3
OR
import numpy as np
import string
# Part A: Argsort of an array (2 Marks)
A1 = np.array([1, 2, 3, 40, 50, 80, 200, 500])
A2 = np.array([2, 5, 1, 8, 3])
print(A2.argsort())
# Output: [2 0 4 1 3]
6
--- page 7 ---
# Explanation: Returns indices that would sort A2 in ascending order (0-based indexing)
# Part B: Reshape and ravel (2 Marks)
B1 = np.arange(1, 21).reshape(5, 4)
print(B1)
# Output: 5x4 matrix
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]
# [13 14 15 16]
# [17 18 19 20]]
print(B1.ravel(order='F'))
# Output: [ 1 5 9 13 17 2 6 10 14 18 3 7 11 15 19 4 8 12 16 20]
# Explanation: Flatten matrix in **column-major order** ('F')
# Part C: Transpose of column vector (2 Marks)
C1 = np.arange(1, 5).reshape(4, 1)
print(C1.T)
# Output: [[1 2 3 4]]
# Explanation: C1 is 4x1 column vector, transpose gives 1x4 row
# Part D: List slicing (2 Marks)
D1 = list(string.ascii_lowercase)
print(D1[-20:-1])
# Output: ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
# Explanation: Negative slicing removes first 6 elements (0-based), includes positions -
20 to -2
# Additional 2 Marks: Code correctness, explanation clarity, and proper use of libraries
Q4   [20]
7
--- page 8 ---
" Q) ligt the Luntions tat a date quality “bool is
expected “te portorm. |
tool Should posted aner
v T dently duplicate Soroyds .
Yonge |
Find Intensislent date |

CO-2 .

Lr Normalise   [ndensistent dala
» date Sune t fen
, . .
--- page 9 ---
Doakalaysos

The Orgned itt

Oxy CoSenis underlging Dakebete Changed
Say From DB2 to oracle - Be, : :

layer cid pot read to be raccdad S
You Surply Change the ODRe cura.
ODRBe   dounens she
co-3 Query PRMS ty eaiStente on i reed
‘Ble Platform. You Com ako use ODRa te access [5]

2 Plot Leleg.
bow Tv tod
Dabebase Bue ee .

mM

Connection Conpeckior

[ETL ter
'

[ opBe Driver

tL?

Sourne   Doakoloase [

|
| =
3

=F

Fig Eopology of ODBC w ETL prolors
--- page 10 ---
ODBC manager’ The ODBC manager Ub oO prograe
eat args Sa. rms ber PTL appa
Seutes, ib pouscte ODBC
dbuber. re he maietont hetaweot
Ayitotion and the ODRC dacuer, :
ODBC cure +. The ODBc doula Ha doe
ODBc cuwsar translates ODEC SQL tb Uae
netwe SQL ef Hy Undoing Aotabose, ©
The drortoack to ODBC's Penibility ts the
UE Cems ak Prrfosments Cost. COvDRC add
Several layers 8 pouoceasing and Parasing ofe
dol tt tthe dotr- Manipulation Procers. Fee
Use ETL poms to utilise dot ira oDRc,*
two Layens are added “¢

CO-2
; BL-

Cc.

Description of layers (6 marks)
Explanation of ETL (2 marks)
Labeled diagram (2 marks)

[10]

10
--- page 11 ---
OF A dodo Wworehouse
fig Dako Wavekouse Ach ee UA

g

éF-|8
2 : a
: acc 25S

LW ONWUKOUSE Mana ger

*

4

Archive | Rackep

Sovytas, These one colle Rely referred tbo as
Source Sysleome.

Stored Un an rrr Collek as dota S vim Ores
Onda ¥ / c wo ined

— Fre Pace dated Rede op syste fee

; inds of Syctums
eared for a rahnwee bot Pot an
i) Some Sy stemrs
a ren
Nt) PS ented enn Senarons.

11
--- page 12 ---
Oferolionel Source :- The Soure of cleta is Sup p lity
AsCol format. Dat Cam alio Cone



so TE erp WF
Ossociated Ustth LL, A p ot opewtions
Womrehouce .

® Denormalisobion. loage totble .
@ Gemenction ef frag reg ation ¢

Barks up X anchiviry of dota , :

4s hrrtid Usin Vinda- .

Clers tools A Custom built Yog Youn . one “
lets is added He Worrhor ses
to Supplement the aggregated dats. ¢
Lightly & Higlty Summarized delai- This stores alé
Quoted lay workers MEABICA. Te raed!

Spard Up the query performance _

Q

12
--- page 13 ---
choke ow Stored foy He purpose of anchivir
oun ak
metadode® Th is “eo i ete or Ophar bi
© Exbredion & (noel aus par peas
Metadote iS Used to map dote Sources |
eS) Warnrhouse monagemet PYOlosd
Metacotr ts sed te atomate the
Pro duction ef Summer toole..
(BD Qusy managemt procers.
Mektideta is used to diet a queyy t
End User ACCC tools: Svamples of Curd User acd
pols ow veportiry and quuy tools, Application

Q5

[20]

13
--- page 14 ---
CO-2

sins) tenes mechautamats : |
User Prévéleges — Foy Dw, the Project
hi _Ditfers & "¥ola” based Secwuhy. A
‘ ‘S Wothung out oe - rn
' aad fecen te for attisttin Ue
(OE the Lol oy g vélags Mary be grantad
ow individual. SE= “Consider Tohu ve our
Chd-user. You have guanttd Gruain pytutle
bb The Users under thy Sole. DAL prtvileses
to ond-ers will he ounlled by Tobe
feo. However, U Some ent pbvyPlege to
Uren only he Gn acted thet One. entra
Dimension table A the Rest of tre ond Wors
’ Counnert,

j @) pass word Pxotectten — Users risa Passwords

a i “Tes (5]
, Bly paounds for Us password
pallors Q the omprry fie Ln 7
Y .
j The dw s SN acetenapts Soe
Fy of 2 Trsold Posed So Urot
ome s) Such ecender,
> sal number Cf
ny O ow be Suspended
adept ( Une tre Dw Urok 1S ) eee
e 3° the pw
‘ ¢
° ¢
BL b. Temporal Data in Data Warehouse: 03]
2

14
--- page 15 ---
_— Loading a tmporal dots mash: — (=
@ Complete Hobush — The data mots ana &


Us ables and then loading the data.agais
The Rey benefit wih this Pdwique & ©
transaction Yepository A yveducos the back-ul
veguiremots , .
You just noed to append te dole §

COo-1
sBL-3

iScovers.c+ Druolves ing date ol tnberrnarh


aka Prepovealnin:~ Dole Com have a let of indensis lendax Likes
& Cap) ore & PrYoCers lok Prior te modelling .
0421 planning i Hew we cetermic dhe method o






> Perattonalise :. Make the é Oo 5
‘ Pura wt, beue pg ;

Commune Cte wesulks- An ae

[10]

15
--- page 16 ---
Q6

CO-3
; BL-
3

@) “Rawat bs cunrsfer .
Mons) brangor the dot uxnul ad

One medium te anothes,. The aduclnes trate
Places a DW monttr that Combiniously monitors
Une Usage of cota. The dota that Te not
Onvrvronmect tS hear Ling Storage. Thes

of tien Provides Pent bt ity & Uses wi niimal
Le .

AF
@ Hierarchical Shor emank CUSMETS
M I
TWis mechanism is phy see a De ae
ts free Mem own human inkaverctton. cl:
Tt meas outtre “Set of dota between Ka, |
Dw and Be neo Une Storage. a

|
a ie ef

“F

i
— Tn cmsm approach, tk & he DW monitmre
Uret Continiovsly monitorc what data [se
Ure end- vsors, ‘s
Used — treq pretty quanies A wenitoss
he Usage OF ak Ue xew level cd
tkak late Can be more furely Lunod

totth tre Warehouse.

B

[20]

[10]

16
--- page 17 ---
b.
Definition:
   Process of detecting and correcting errors, inconsistencies, or inaccuracies in
data to ensure high-quality datasets. (1 Mark)
Reasons for Data Cleaning:
 Missing values due to incomplete records or human/system errors. (1 Mark)
   Inaccurate data or typos. (1 Mark)
   Duplicate records causing redundancy. (1 Mark)
   Inconsistent formats (dates, currencies, units). (1 Mark)
   Outliers and noisy data affecting analysis. (1 Mark)
Sources of Dirty Data:
CO-2
; BL-    Manual data entry errors. (0.5 Mark)   [10]
2      Integration from multiple heterogeneous sources. (0.5 Mark)
 System errors or software/hardware glitches. (0.5 Mark)
   External data sources (APIs, web scraping, third-party datasets). (0.5 Mark)
Steps Involved in Data Cleaning:
 Data Profiling: Detect missing values, duplicates, and inconsistencies. (1 Mark)
 Handling Missing Values: Impute with mean/median/mode or remove records.
(1 Mark)
   Correcting Errors: Fix typos and inconsistent formats. (1 Mark)
 Removing Duplicates: Eliminate redundant records. (1 Mark)
   Standardization: Uniform formats for dates, currencies, and categorical data. (1
Mark)
 Handling Outliers & Noise: Remove, cap, or transform extreme values. (1
Mark)
17
--- page 18 ---
e Validation: Verify cleaned data against rules or source systems. (1 Mark)_



~ Multipurpose Cieldu-
— Contsack?ctug date
— Lnappropriak® use of Address Liss:

= Reuged primary Reys -

Some Systews and ther hose clorments
orn ‘Solated uw target files. 2X- Porsing of
nome Urto first name , middle have , last
Named Parsing addren mte Street nawe,
oky i Stoke , Cosby =
‘ iA —
) ae ‘otek » ul dab ae
One Corvected Using lero, algoritu, S
S€ Condory Agke SovrGa.

18
--- page 19 ---
@ StandardéiZing _

Preuttnes ore used & trams form clot

ute a Cenmsi's tent format Using bo th
Standard, A Custom bucinos surstor,

& Making ~ matching procer Prtrolines, ¢

eliminating duplidokin by Searching


Corrected A standardised dat. Using €


©} Sintlorn nome Q addrecsess. ¢

.y) 4 ¢

© Consolidating — TA Naelues morguirg af Un:


ing R Idoutifurng geolationchs e

rena notched ae MP ¢



Steps. Using di processes Lea motu.

interfaces, Hot Liles, PrP Sessions, dota &




tranfosmakion proces. No end User. accom,

uw oral to He 5 i file. For

©

ao

Q7

[20]

19
--- page 20 ---
CO-2
; BL-

a.

ote dictionary On a dotolose management
System. The Metadata Comporunt stows dete
About thea dala” in Dw.

— The metodote is Often usb Poy building,
Tk ib the ‘pey te iding sors Q develops
Wh OO voadmrap te the Iwlormebion un He
Wanehewe. Th, it forms an essential

Dw envisierment are Hat ib :-,

D Connects th different pants of Dw tewhy
Cickung as a gure Chat Connects all pads,
the DW administrate and other users,

GB) Enables end users te Search for the
Aesisud dole mw ther own busine teams,

— without O& proper motadala UR plage.

dola Stosed iw Warehouse will be
Meanmaless Since the Users will net be able
f Rnew— What, Where, Wh

1 WhY RB how the
dole enuists within the Orgontsalion .

[10]

20
--- page 21 ---
Dota

\22338F0F This String O digi Could either
ee. Salas of any product 0%

O6]oF/ig)— Ths could be either ote of birth
ecthe, meon 6 July ol” ov
HF Tune 2018.

Mekadala Comtous Data about dot

\XRABBEFO|— Sales of T-Shi un wastein Fore
O46107118 —| Refers te sales transaction un
fovmet dd] mm]yy.

a

21
--- page 22 ---
the Dw, an ODS Covikaing Urry Uiwitedk
cent hPstoritol doko . pie Ue dale

dola, the ODS Stores only a rronts old

lela.
— Un i -- Tha ods is CLasignadk

Ot, 4 is designed using deletions) technolo
and Us mest 15 designed Yeing mut .
sLermansonek bechnoleay .
—_ aero fr profile serord o One
dala. A Somple poopie ts Shown below!~

i}
Feuys o slot [eres bs |
SS a)

re — in a
ip profes baping sa bl wing Un es ot hkl

Ha me Ne

22
--- page 23 ---
Very ‘ . Oa the infosmatren os O14

Closses depending Upon how fost Dre deta   @-
Osvrives Gcto Ub | ty
Claw E:- Lt totes a foo niflliseconds fox he et
cata to sou Un ODS. The tm elapsed & Cf
transparent te the Users. Arpplicadren — Applteal ur o-
Coss T:- Tt takes Seenal hours fov the data
® owube Ur ODS, On a tYansadzen the OG
Place. The erd sens Can uisualise thet tans “1
Bw o& time gap betwaor asoual d oceunante. ot
Nome ond addres Change of a Customer. «ih
botweon OCcurente of transaction curd the ee.
Asetwoh of dote Ur ODS. frpplicetien - used et
for applying Soles transaction . el
transaction and its ovvulol uo ODS is a
Wor, Lon 1,0 ur Some Monts ox Years, iH

Others toy be Cwstd Prom output of P|
Speaal yepors or projects. Application — A a
Swwwey 12h   Custowmarr lunging halo Pts, ou

(<a

23
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 7a5d911c11ca

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MBATech_DS_7052/Data Wrangling/ANS_Data Wrangling(702DB0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MBA Tech (DS)
Year: II / III / IV/Semester III/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
a.   • Data wrangling is the process of cleaning, transforming, and organizing raw data   [5]
into a usable format. (1)
• Improves data quality and consistency. (1)
• Fixes missing, duplicate, and erroneous values. (1)
• Makes data ready for analysis and modeling. (1)
• Leads to better decision-making with accurate insights. (1)
b.   • OLTP handles transactional, day-to-day operations; OLAP handles analytical,   [5]
decision-support queries. (1)
• OLTP deals with many small, simple transactions; OLAP handles fewer but
complex queries. (1)
• OLTP   uses   normalized   relational   data;   OLAP   uses
denormalized/multidimensional data. (1)
• OLTP focuses on real-time processing; OLAP often on batch or scheduled
processing. (1)
• OLTP is optimized for speed and concurrency; OLAP is optimized for query
performance and insights. (1)
c.   • Data Owner – Defines rules, ensures correct usage of data. (1)   [5]
• Data Steward – Maintains data accuracy, consistency, and governance. (1)
• ETL Developer – Implements validation and cleaning in ETL pipelines. (1)
• Data Quality Analyst – Profiles, monitors, and reports data quality issues. (1)
• Management – Sets policies, provides resources, ensures compliance. (1)
d.   • Data cleaning (handling missing or invalid values). (1)   [5]
• Data standardization or formatting into consistent structure. (1)
• Data aggregation or summarization for analysis. (1)
• Data merging or joining from multiple sources. (1)
********** 1 **********
--- page 2 ---
• Creation of derived or calculated fields. (1)
Q2   [20]
CO-   a. # Import libraries   [10]
2 ;B   import pandas as pd
L-3   import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("sales_data.csv")
# Basic EDA
df.head()   # first 5 rows
df.tail()   # last 5 rows
df.info()   # data types, nulls
df.describe()   # statistics
# Check missing values
df.isnull().sum()
# Univariate Visualization
plt.hist(df['Sales'])   # histogram of sales
sns.boxplot(x='Region', y='Sales', data=df) # boxplot
# Bivariate Visualization
sns.scatterplot(x='Sales', y='Profit', data=df) # scatter
sns.barplot(x='Region', y='Sales', data=df)   # avg sales by region
# Correlation Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True)
# Show plots
plt.show()
(OR)
# Load data
df <- read.csv("sales_data.csv")
# Display first 10 rows
head(df, 10)
# Display last 5 rows
tail(df, 5)
# Extract only the first column
df[, 1]   # or df[[1]] or df$ColumnName
# Determine data type of the second column
class(df[, 2]) # or str(df[,2]) or typeof(df[,2])
# Convert entire data frame to matrix
mat <- as.matrix(df)
b. # Create vect1 with odd numbers from 100 to 50   [10]
CO-   vect1 <- seq(99, 51, by = -2)
3 ;B   # Arrange in ascending order
vect1 <- sort(vect1)
L-3   # Total number of elements
length(vect1) # Output: 25
# Check dimension
dim(vect1)   # Output: NULL (because it is a 1D vector)
# Index of number 61
which(vect1 == 61)
OR
# Create list1 with odd numbers from 100 to 50
********** 2 **********
--- page 3 ---
list1 = list(range(99, 50, -2))
# Arrange in ascending order
list1.sort()
# Total number of elements
len(list1) # Output: 25
# Check dimension
# Lists in Python are 1D by default
# So dimension = 1D (no rows/columns unless nested)
# Index of number 61
list1.index(61)
o/p
•   vect1: 99, 97, 95, …, 51
• Total elements = 25
• Dimension = NULL (1D vector)
•   Index of 61 = position number in vector
Q3   [20]
CO-   a.   # i. Create dataset and store in DataFrame (2 Marks)   [10]
2 ;   import pandas as pd
BL-3   import numpy as np
df = pd.DataFrame({
'ID':[1,2,3,4,5,6,7,8,9,10],
'Dept':['HR','IT','Fin','IT','HR','Fin','IT','HR','Fin','IT'],
'Exp':[3,6,4,7,2,5,3,4,8,2],
'Salary':[48000,75000,60000,92000,42000,78000,67000,np.nan,87000,62000
],
'Projects':[2,7,5,10,3,6,4,3,9,np.nan],
'Promotion':['No','Yes','No','Yes','No','Yes','No','No','Yes','No']
})
# ii. Mean of Exp (1 Mark)
mean_exp = df['Exp'].mean()
# iii. Fill NaN values with justification (4 Marks)
df['Salary'].fillna(df['Salary'].median(), inplace=True) # Median is robust to
salary outliers
df['Projects'].fillna(df['Projects'].mean(), inplace=True) # Mean reasonable
for project counts
# iv. Dept with highest number of projects (2 Marks)
dept_projects = df.groupby('Dept')['Projects'].sum()
highest_dept = dept_projects.idxmax()
# v. Delete Promotion field (1 Mark)
df.drop('Promotion', axis=1, inplace=True)
# i. Create dataset and store in data frame (2 Marks)
df <- data.frame(
ID = c(1,2,3,4,5,6,7,8,9,10),
Dept = c("HR","IT","Fin","IT","HR","Fin","IT","HR","Fin","IT"),
Exp = c(3,6,4,7,2,5,3,4,8,2),
Salary   =
c(48000,75000,60000,92000,42000,78000,67000,NA,87000,62000),
Projects = c(2,7,5,10,3,6,4,3,9,NA),
Promotion = c("No","Yes","No","Yes","No","Yes","No","No","Yes","No")
********** 3 **********
--- page 4 ---
)
# ii. Mean of Exp (1 Mark)
mean_exp <- mean(df$Exp, na.rm = TRUE)
# iii. Fill NA values with justification (4 Marks)
df$Salary[is.na(df$Salary)] <- median(df$Salary, na.rm = TRUE) # Median
handles salary outliers
df$Projects[is.na(df$Projects)] <- mean(df$Projects, na.rm = TRUE) # Mean
is fine for counts
# iv. Dept with highest number of projects (2 Marks)
dept_projects <- tapply(df$Projects, df$Dept, sum)
highest_dept <- names(which.max(dept_projects))
# v. Delete Promotion field (1 Mark)
df$Promotion <- NULL
O/P
CO-   b.   [10]
3 ;   OR
BL-3   import numpy as np
import string
# Part A: Argsort of an array (2 Marks)
A1 = np.array([1, 2, 3, 40, 50, 80, 200, 500])
A2 = np.array([2, 5, 1, 8, 3])
print(A2.argsort())
# Output: [2 0 4 1 3]
# Explanation: Returns indices that would sort A2 in ascending order (0-based
indexing)
# Part B: Reshape and ravel (2 Marks)
B1 = np.arange(1, 21).reshape(5, 4)
print(B1)
# Output: 5x4 matrix
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]
# [13 14 15 16]
# [17 18 19 20]]
print(B1.ravel(order='F'))
# Output: [ 1 5 9 13 17 2 6 10 14 18 3 7 11 15 19 4 8 12 16 20]
# Explanation: Flatten matrix in **column-major order** ('F')
********** 4 **********
--- page 5 ---
# Part C: Transpose of column vector (2 Marks)
C1 = np.arange(1, 5).reshape(4, 1)
print(C1.T)
# Output: [[1 2 3 4]]
# Explanation: C1 is 4x1 column vector, transpose gives 1x4 row
# Part D: List slicing (2 Marks)
D1 = list(string.ascii_lowercase)
print(D1[-20:-1])
# Output: ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
# Explanation: Negative slicing removes first 6 elements (0-based), includes positions
-20 to -2
# Additional 2 Marks: Code correctness, explanation clarity, and proper use of
libraries
Q4   [20]
CO-   a.   • Data Profiling: Analyzes datasets to identify inconsistencies, patterns,   [5]
2 ;   missing values, and anomalies. (1 mark)
BL-2   • Data Cleansing: Detects and corrects errors such as duplicates, missing
values, or incorrect formats. (1 mark)
• Data Standardization: Ensures uniform formats for dates, addresses, codes,
and other fields. (1 mark)
• Data Validation: Checks data against predefined rules or business logic to
ensure accuracy and consistency. (1 mark)
• Monitoring & Reporting: Tracks data quality over time, generating alerts and
reports for continuous improvement. (1 mark)
CO-   b. ODBC (Open Database Connectivity) in ETL:   [5]
3 ;
BL-2   • ODBC provides a standard interface to connect ETL tools to various data
sources (databases, spreadsheets, etc.).
• ETL tools use ODBC drivers to extract data from heterogeneous sources
without worrying about source-specific APIs.
• Ensures interoperability: the same ETL workflow can connect to SQL
Server, Oracle, MySQL, or other ODBC-compliant sources.
• Supports data extraction, transformation, and loading by enabling ETL
scripts to read/write data consistently.
Example:
1. Configure ODBC DSN (Data Source Name) for the source database.
2. Use ETL tool to connect via the DSN.
3. Extract data, apply transformations, and load into target data warehouse.
CO-   c.   •   Description of layers (6 marks)   [10]
2 ;   • Explanation of ETL (2 marks)
BL-3   • Labeled diagram (2 marks)
Q5   [20]
CO-   a. Importance of Data Warehouse Security Mechanisms:   [5]
2 ;
BL-2   •   Protects sensitive data: Ensures financial, personal, and business-critical data
is safe from unauthorized access. (1 mark)
********** 5 **********
--- page 6 ---
• Access control: Restricts data access based on user roles and responsibilities,
preventing data misuse. (1 mark)
• Data integrity: Prevents unauthorized modifications, ensuring accurate and
reliable data for decision-making. (1 mark)
• Auditing and compliance: Tracks who accessed or modified data, helping
meet legal and regulatory requirements. (1 mark)
• Prevents data breaches: Safeguards against cyber-attacks, maintaining trust
and continuity in business operations. (1 mark)
CO-   b. Temporal Data in Data Warehouse:   [5]
3 ;
BL-2   • Temporal data changes over time, e.g., salary or price history.
• Loading: Initial load inserts current records with start/end dates; incremental
load updates only changes.
• Maintenance:
o SCD Type 1: Overwrite old data (no history).
o SCD Type 2: Add new records to preserve history.
o SCD Type 3: Store limited history in extra columns.
• Purpose: Supports historical analysis and accurate decision-making.
CO-   c.   1. Problem Discovery: Identify and understand the business problem, define   [10]
1 ;B   objectives, and frame it as a data science question.
L-3   2. Data Collection: Gather relevant data from multiple sources such as databases,
APIs, sensors, or external datasets.
3. Data Preparation: Clean, transform, and integrate data; handle missing values,
outliers, and inconsistencies; create features for analysis.
4. Exploratory Data Analysis (EDA): Explore data patterns, correlations, and
distributions; visualize data to gain insights.
5. Model Planning: Select suitable algorithms, define performance metrics, and
design experiments.
6. Model Building: Train machine learning/statistical models on prepared data;
optimize hyperparameters.
7. Model Evaluation: Validate model performance on test/validation sets; check
accuracy, precision, recall, or other relevant metrics.
8. Deployment / Operationalize: Integrate the model into production systems for
real-time or batch predictions.
9. Monitoring and Maintenance: Continuously monitor model performance, retrain
if data distribution changes.
10. Communicate Results: Present findings, visualizations, and actionable insights
to stakeholders; support decision-making.
Q 6   [20]
CO-   a.   • Batch Transfer: Periodically move large volumes of data in scheduled [10]
3 ;   intervals (daily, weekly) from the warehouse to near-line storage.
BL-3
• Incremental Transfer: Only changed or new records are transferred, reducing
bandwidth and storage usage.
• ETL Pipelines: Use Extract, Transform, Load processes to format and clean
data before moving it to near-line storage.
• Data Compression & Archiving: Compress data to save storage and archive
less frequently accessed data.
• Automated Scheduling & Monitoring: Use scripts or ETL tools to automate
transfers, monitor errors, and ensure data consistency.
********** 6 **********
--- page 7 ---
• Purpose: Provides cost-effective storage, preserves historical data, and
maintains accessibility for reporting and analytics.
CO-   b. Definition:   [10]
2 ;
BL-2
• Process of detecting and correcting errors, inconsistencies, or inaccuracies in
data to ensure high-quality datasets. (1 Mark)
Reasons for Data Cleaning:
• Missing values due to incomplete records or human/system errors. (1 Mark)
•   Inaccurate data or typos. (1 Mark)
• Duplicate records causing redundancy. (1 Mark)
•   Inconsistent formats (dates, currencies, units). (1 Mark)
•   Outliers and noisy data affecting analysis. (1 Mark)
Sources of Dirty Data:
• Manual data entry errors. (0.5 Mark)
•   Integration from multiple heterogeneous sources. (0.5 Mark)
• System errors or software/hardware glitches. (0.5 Mark)
•   External data sources (APIs, web scraping, third-party datasets). (0.5 Mark)
Steps Involved in Data Cleaning:
• Data Profiling: Detect missing values, duplicates, and inconsistencies. (1
Mark)
• Handling Missing Values: Impute with mean/median/mode or remove
records. (1 Mark)
•   Correcting Errors: Fix typos and inconsistent formats. (1 Mark)
• Removing Duplicates: Eliminate redundant records. (1 Mark)
•   Standardization: Uniform formats for dates, currencies, and categorical data.
(1 Mark)
• Handling Outliers & Noise: Remove, cap, or transform extreme values. (1
Mark)
•   Validation: Verify cleaned data against rules or source systems. (1 Mark)
Q 7   [20]
CO-   a.   •   Definition:   [10]
2 ;   • Metadata is “data about data” that describes the structure, content, source,
BL-2   and usage of data in the warehouse. (1 Mark)
•   Functions:
• Data Source Description: Documents the origin, type, format, and
relationships of data in the warehouse. (1 Mark)
• ETL Support: Provides rules, mappings, transformations, and lineage
information to guide extraction, transformation, and loading processes. (1
Mark)
• Data Quality Management: Tracks accuracy, completeness, consistency, and
errors in data. (1 Mark)
• Query Optimization: Supplies indexing, aggregation, and summary
information to improve query performance. (1 Mark)
• Business Rules & Definitions: Stores definitions of measures, dimensions,
and metrics to ensure consistent interpretation. (1 Mark)
********** 7 **********
--- page 8 ---
• Audit & Compliance: Maintains information on data access, updates, and
modifications for auditing purposes. (1 Mark)
• Versioning & Change Management: Records changes in data structure,
schema evolution, and historical versions of datasets. (1 Mark)
• User Guidance & Reporting: Helps analysts understand the meaning, source,
and usage of data for reporting and decision-making. (1 Mark)
•   Integration Support: Assists in merging data from heterogeneous sources by
providing structural and semantic metadata. (1 Mark)
• Documentation & Communication: Acts as a central reference for
developers, administrators, and end-users. (1 Mark)
CO-   b.   •   Definition:   •
3 ;   • An ODS is a centralized database that integrates data from multiple
BL-3   operational systems, providing a current, consolidated view of transactional
data.
• Data Characteristics:
• Contains current or near-real-time data.
• Mostly detailed, granular records rather than aggregated summaries.
• Frequently updated, reflecting ongoing operational transactions.
• Core Technology:
•   Built on relational database systems.
• Supports high-speed inserts, updates, and queries.
• Often acts as a staging area for the data warehouse.
• Record Profiling:
• Monitors data for completeness, consistency, and validity.
• Ensures correct data types, ranges, and formats for operational analysis.
•   Classification:
• Type 1: Short-term operational reporting (e.g., daily sales).
• Type 2: Intermediate store between OLTP systems and data warehouse.
• Can be application-specific (HR, Finance, Sales) or enterprise-wide.
• Purpose:
• Provides real-time or near-real-time reporting without impacting source
systems.
• Supports operational decision-making and data quality checks before loading
into the data warehouse.
********** 8 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper a805f9b720e2

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/Integrated_DS_7038/Data Wrangling/ANS_Data Wrangling(702DB0C012)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MBA Tech (DS)
Year: II / III / IV/Semester III/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
a.   • Data wrangling is the process of cleaning, transforming, and organizing raw data   [5]
into a usable format. (1)
• Improves data quality and consistency. (1)
• Fixes missing, duplicate, and erroneous values. (1)
• Makes data ready for analysis and modeling. (1)
• Leads to better decision-making with accurate insights. (1)
b.   • OLTP handles transactional, day-to-day operations; OLAP handles analytical,   [5]
decision-support queries. (1)
• OLTP deals with many small, simple transactions; OLAP handles fewer but
complex queries. (1)
• OLTP   uses   normalized   relational   data;   OLAP   uses
denormalized/multidimensional data. (1)
• OLTP focuses on real-time processing; OLAP often on batch or scheduled
processing. (1)
• OLTP is optimized for speed and concurrency; OLAP is optimized for query
performance and insights. (1)
c.   • Data Owner – Defines rules, ensures correct usage of data. (1)   [5]
• Data Steward – Maintains data accuracy, consistency, and governance. (1)
• ETL Developer – Implements validation and cleaning in ETL pipelines. (1)
• Data Quality Analyst – Profiles, monitors, and reports data quality issues. (1)
• Management – Sets policies, provides resources, ensures compliance. (1)
d.   • Data cleaning (handling missing or invalid values). (1)   [5]
• Data standardization or formatting into consistent structure. (1)
• Data aggregation or summarization for analysis. (1)
• Data merging or joining from multiple sources. (1)
********** 1 **********
--- page 2 ---
• Creation of derived or calculated fields. (1)
Q2   [20]
CO-   a. # Import libraries   [10]
2 ;B   import pandas as pd
L-3   import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("sales_data.csv")
# Basic EDA
df.head()   # first 5 rows
df.tail()   # last 5 rows
df.info()   # data types, nulls
df.describe()   # statistics
# Check missing values
df.isnull().sum()
# Univariate Visualization
plt.hist(df['Sales'])   # histogram of sales
sns.boxplot(x='Region', y='Sales', data=df) # boxplot
# Bivariate Visualization
sns.scatterplot(x='Sales', y='Profit', data=df) # scatter
sns.barplot(x='Region', y='Sales', data=df)   # avg sales by region
# Correlation Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True)
# Show plots
plt.show()
(OR)
# Load data
df <- read.csv("sales_data.csv")
# Display first 10 rows
head(df, 10)
# Display last 5 rows
tail(df, 5)
# Extract only the first column
df[, 1]   # or df[[1]] or df$ColumnName
# Determine data type of the second column
class(df[, 2]) # or str(df[,2]) or typeof(df[,2])
# Convert entire data frame to matrix
mat <- as.matrix(df)
b. # Create vect1 with odd numbers from 100 to 50   [10]
CO-   vect1 <- seq(99, 51, by = -2)
3 ;B   # Arrange in ascending order
vect1 <- sort(vect1)
L-3   # Total number of elements
length(vect1) # Output: 25
# Check dimension
dim(vect1)   # Output: NULL (because it is a 1D vector)
# Index of number 61
which(vect1 == 61)
OR
# Create list1 with odd numbers from 100 to 50
********** 2 **********
--- page 3 ---
list1 = list(range(99, 50, -2))
# Arrange in ascending order
list1.sort()
# Total number of elements
len(list1) # Output: 25
# Check dimension
# Lists in Python are 1D by default
# So dimension = 1D (no rows/columns unless nested)
# Index of number 61
list1.index(61)
o/p
•   vect1: 99, 97, 95, …, 51
• Total elements = 25
• Dimension = NULL (1D vector)
•   Index of 61 = position number in vector
Q3   [20]
CO-   a.   # i. Create dataset and store in DataFrame (2 Marks)   [10]
2 ;   import pandas as pd
BL-3   import numpy as np
df = pd.DataFrame({
'ID':[1,2,3,4,5,6,7,8,9,10],
'Dept':['HR','IT','Fin','IT','HR','Fin','IT','HR','Fin','IT'],
'Exp':[3,6,4,7,2,5,3,4,8,2],
'Salary':[48000,75000,60000,92000,42000,78000,67000,np.nan,87000,62000
],
'Projects':[2,7,5,10,3,6,4,3,9,np.nan],
'Promotion':['No','Yes','No','Yes','No','Yes','No','No','Yes','No']
})
# ii. Mean of Exp (1 Mark)
mean_exp = df['Exp'].mean()
# iii. Fill NaN values with justification (4 Marks)
df['Salary'].fillna(df['Salary'].median(), inplace=True) # Median is robust to
salary outliers
df['Projects'].fillna(df['Projects'].mean(), inplace=True) # Mean reasonable
for project counts
# iv. Dept with highest number of projects (2 Marks)
dept_projects = df.groupby('Dept')['Projects'].sum()
highest_dept = dept_projects.idxmax()
# v. Delete Promotion field (1 Mark)
df.drop('Promotion', axis=1, inplace=True)
# i. Create dataset and store in data frame (2 Marks)
df <- data.frame(
ID = c(1,2,3,4,5,6,7,8,9,10),
Dept = c("HR","IT","Fin","IT","HR","Fin","IT","HR","Fin","IT"),
Exp = c(3,6,4,7,2,5,3,4,8,2),
Salary   =
c(48000,75000,60000,92000,42000,78000,67000,NA,87000,62000),
Projects = c(2,7,5,10,3,6,4,3,9,NA),
Promotion = c("No","Yes","No","Yes","No","Yes","No","No","Yes","No")
********** 3 **********
--- page 4 ---
)
# ii. Mean of Exp (1 Mark)
mean_exp <- mean(df$Exp, na.rm = TRUE)
# iii. Fill NA values with justification (4 Marks)
df$Salary[is.na(df$Salary)] <- median(df$Salary, na.rm = TRUE) # Median
handles salary outliers
df$Projects[is.na(df$Projects)] <- mean(df$Projects, na.rm = TRUE) # Mean
is fine for counts
# iv. Dept with highest number of projects (2 Marks)
dept_projects <- tapply(df$Projects, df$Dept, sum)
highest_dept <- names(which.max(dept_projects))
# v. Delete Promotion field (1 Mark)
df$Promotion <- NULL
O/P
CO-   b.   [10]
3 ;   OR
BL-3   import numpy as np
import string
# Part A: Argsort of an array (2 Marks)
A1 = np.array([1, 2, 3, 40, 50, 80, 200, 500])
A2 = np.array([2, 5, 1, 8, 3])
print(A2.argsort())
# Output: [2 0 4 1 3]
# Explanation: Returns indices that would sort A2 in ascending order (0-based
indexing)
# Part B: Reshape and ravel (2 Marks)
B1 = np.arange(1, 21).reshape(5, 4)
print(B1)
# Output: 5x4 matrix
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]
# [13 14 15 16]
# [17 18 19 20]]
print(B1.ravel(order='F'))
# Output: [ 1 5 9 13 17 2 6 10 14 18 3 7 11 15 19 4 8 12 16 20]
# Explanation: Flatten matrix in **column-major order** ('F')
********** 4 **********
--- page 5 ---
# Part C: Transpose of column vector (2 Marks)
C1 = np.arange(1, 5).reshape(4, 1)
print(C1.T)
# Output: [[1 2 3 4]]
# Explanation: C1 is 4x1 column vector, transpose gives 1x4 row
# Part D: List slicing (2 Marks)
D1 = list(string.ascii_lowercase)
print(D1[-20:-1])
# Output: ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
# Explanation: Negative slicing removes first 6 elements (0-based), includes positions
-20 to -2
# Additional 2 Marks: Code correctness, explanation clarity, and proper use of
libraries
Q4   [20]
CO-   a.   • Data Profiling: Analyzes datasets to identify inconsistencies, patterns,   [5]
2 ;   missing values, and anomalies. (1 mark)
BL-2   • Data Cleansing: Detects and corrects errors such as duplicates, missing
values, or incorrect formats. (1 mark)
• Data Standardization: Ensures uniform formats for dates, addresses, codes,
and other fields. (1 mark)
• Data Validation: Checks data against predefined rules or business logic to
ensure accuracy and consistency. (1 mark)
• Monitoring & Reporting: Tracks data quality over time, generating alerts and
reports for continuous improvement. (1 mark)
CO-   b. ODBC (Open Database Connectivity) in ETL:   [5]
3 ;
BL-2   • ODBC provides a standard interface to connect ETL tools to various data
sources (databases, spreadsheets, etc.).
• ETL tools use ODBC drivers to extract data from heterogeneous sources
without worrying about source-specific APIs.
• Ensures interoperability: the same ETL workflow can connect to SQL
Server, Oracle, MySQL, or other ODBC-compliant sources.
• Supports data extraction, transformation, and loading by enabling ETL
scripts to read/write data consistently.
Example:
1. Configure ODBC DSN (Data Source Name) for the source database.
2. Use ETL tool to connect via the DSN.
3. Extract data, apply transformations, and load into target data warehouse.
CO-   c.   •   Description of layers (6 marks)   [10]
2 ;   • Explanation of ETL (2 marks)
BL-3   • Labeled diagram (2 marks)
Q5   [20]
CO-   a. Importance of Data Warehouse Security Mechanisms:   [5]
2 ;
BL-2   •   Protects sensitive data: Ensures financial, personal, and business-critical data
is safe from unauthorized access. (1 mark)
********** 5 **********
--- page 6 ---
• Access control: Restricts data access based on user roles and responsibilities,
preventing data misuse. (1 mark)
• Data integrity: Prevents unauthorized modifications, ensuring accurate and
reliable data for decision-making. (1 mark)
• Auditing and compliance: Tracks who accessed or modified data, helping
meet legal and regulatory requirements. (1 mark)
• Prevents data breaches: Safeguards against cyber-attacks, maintaining trust
and continuity in business operations. (1 mark)
CO-   b. Temporal Data in Data Warehouse:   [5]
3 ;
BL-2   • Temporal data changes over time, e.g., salary or price history.
• Loading: Initial load inserts current records with start/end dates; incremental
load updates only changes.
• Maintenance:
o SCD Type 1: Overwrite old data (no history).
o SCD Type 2: Add new records to preserve history.
o SCD Type 3: Store limited history in extra columns.
• Purpose: Supports historical analysis and accurate decision-making.
CO-   c.   1. Problem Discovery: Identify and understand the business problem, define   [10]
1 ;B   objectives, and frame it as a data science question.
L-3   2. Data Collection: Gather relevant data from multiple sources such as databases,
APIs, sensors, or external datasets.
3. Data Preparation: Clean, transform, and integrate data; handle missing values,
outliers, and inconsistencies; create features for analysis.
4. Exploratory Data Analysis (EDA): Explore data patterns, correlations, and
distributions; visualize data to gain insights.
5. Model Planning: Select suitable algorithms, define performance metrics, and
design experiments.
6. Model Building: Train machine learning/statistical models on prepared data;
optimize hyperparameters.
7. Model Evaluation: Validate model performance on test/validation sets; check
accuracy, precision, recall, or other relevant metrics.
8. Deployment / Operationalize: Integrate the model into production systems for
real-time or batch predictions.
9. Monitoring and Maintenance: Continuously monitor model performance, retrain
if data distribution changes.
10. Communicate Results: Present findings, visualizations, and actionable insights
to stakeholders; support decision-making.
Q 6   [20]
CO-   a.   • Batch Transfer: Periodically move large volumes of data in scheduled [10]
3 ;   intervals (daily, weekly) from the warehouse to near-line storage.
BL-3
• Incremental Transfer: Only changed or new records are transferred, reducing
bandwidth and storage usage.
• ETL Pipelines: Use Extract, Transform, Load processes to format and clean
data before moving it to near-line storage.
• Data Compression & Archiving: Compress data to save storage and archive
less frequently accessed data.
• Automated Scheduling & Monitoring: Use scripts or ETL tools to automate
transfers, monitor errors, and ensure data consistency.
********** 6 **********
--- page 7 ---
• Purpose: Provides cost-effective storage, preserves historical data, and
maintains accessibility for reporting and analytics.
CO-   b. Definition:   [10]
2 ;
BL-2
• Process of detecting and correcting errors, inconsistencies, or inaccuracies in
data to ensure high-quality datasets. (1 Mark)
Reasons for Data Cleaning:
• Missing values due to incomplete records or human/system errors. (1 Mark)
•   Inaccurate data or typos. (1 Mark)
• Duplicate records causing redundancy. (1 Mark)
•   Inconsistent formats (dates, currencies, units). (1 Mark)
•   Outliers and noisy data affecting analysis. (1 Mark)
Sources of Dirty Data:
• Manual data entry errors. (0.5 Mark)
•   Integration from multiple heterogeneous sources. (0.5 Mark)
• System errors or software/hardware glitches. (0.5 Mark)
•   External data sources (APIs, web scraping, third-party datasets). (0.5 Mark)
Steps Involved in Data Cleaning:
• Data Profiling: Detect missing values, duplicates, and inconsistencies. (1
Mark)
• Handling Missing Values: Impute with mean/median/mode or remove
records. (1 Mark)
•   Correcting Errors: Fix typos and inconsistent formats. (1 Mark)
• Removing Duplicates: Eliminate redundant records. (1 Mark)
•   Standardization: Uniform formats for dates, currencies, and categorical data.
(1 Mark)
• Handling Outliers & Noise: Remove, cap, or transform extreme values. (1
Mark)
•   Validation: Verify cleaned data against rules or source systems. (1 Mark)
Q 7   [20]
CO-   a.   •   Definition:   [10]
2 ;   • Metadata is “data about data” that describes the structure, content, source,
BL-2   and usage of data in the warehouse. (1 Mark)
•   Functions:
• Data Source Description: Documents the origin, type, format, and
relationships of data in the warehouse. (1 Mark)
• ETL Support: Provides rules, mappings, transformations, and lineage
information to guide extraction, transformation, and loading processes. (1
Mark)
• Data Quality Management: Tracks accuracy, completeness, consistency, and
errors in data. (1 Mark)
• Query Optimization: Supplies indexing, aggregation, and summary
information to improve query performance. (1 Mark)
• Business Rules & Definitions: Stores definitions of measures, dimensions,
and metrics to ensure consistent interpretation. (1 Mark)
********** 7 **********
--- page 8 ---
• Audit & Compliance: Maintains information on data access, updates, and
modifications for auditing purposes. (1 Mark)
• Versioning & Change Management: Records changes in data structure,
schema evolution, and historical versions of datasets. (1 Mark)
• User Guidance & Reporting: Helps analysts understand the meaning, source,
and usage of data for reporting and decision-making. (1 Mark)
•   Integration Support: Assists in merging data from heterogeneous sources by
providing structural and semantic metadata. (1 Mark)
• Documentation & Communication: Acts as a central reference for
developers, administrators, and end-users. (1 Mark)
CO-   b.   •   Definition:   •
3 ;   • An ODS is a centralized database that integrates data from multiple
BL-3   operational systems, providing a current, consolidated view of transactional
data.
• Data Characteristics:
• Contains current or near-real-time data.
• Mostly detailed, granular records rather than aggregated summaries.
• Frequently updated, reflecting ongoing operational transactions.
• Core Technology:
•   Built on relational database systems.
• Supports high-speed inserts, updates, and queries.
• Often acts as a staging area for the data warehouse.
• Record Profiling:
• Monitors data for completeness, consistency, and validity.
• Ensures correct data types, ranges, and formats for operational analysis.
•   Classification:
• Type 1: Short-term operational reporting (e.g., daily sales).
• Type 2: Intermediate store between OLTP systems and data warehouse.
• Can be application-specific (HR, Finance, Sales) or enterprise-wide.
• Purpose:
• Provides real-time or near-real-time reporting without impacting source
systems.
• Supports operational decision-making and data quality checks before loading
into the data warehouse.
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper fb72288f1068

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/BTech_AIDS_7056/Data Wrangling/ANS_Data Wrangling(702DB0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted
6. All questions carry equal marks
7. Answer to each new question to be started on a fresh page
8. Figures in brackets on the right hand side indicate full marks
9. Assume Suitable data if necessary
Q.1a   Explain descriptive question and predictive question with suitable example in   5
CO1   context to data science?
BL2
Understan
d
Descriptive question -2.5 marks
Predictive question – 2.5 marks
A descriptive question focuses on summarizing and describing the existing
characteristics of a dataset. It answers questions such as what happened or what is
happening in the data. Descriptive analysis uses statistical measures like mean,
median, frequency distribution, and percentages to summarize data.
Example:
A retail company may ask:
“What was the average monthly sales in 2024?”
The analysis will summarize historical sales data to describe overall performance.
A predictive question aims to forecast future outcomes based on historical data.
Predictive analysis uses techniques such as regression, machine learning models, and
trend analysis.
Example:
"Based on past sales data, what will be the expected sales for the next quarter?"
Here, historical data is used to predict future results.
Thus, descriptive questions summarize past data, while predictive questions use data
to forecast future outcomes.
Q.1b   The following paired observations represent coffee consumption (X) and   5
CO2   productivity score (Y):
BL2   (1, 60), (2, 65), (3, 63), (4, 67), (5, 64)
Understan Draw a scatter plot for the above data and interpret the pattern observed and explain
d   the relationship between the variables
Scatter plot-2 marks
Interpretation -3 marks
********** 1 **********
--- page 2 ---
When the given data points are plotted, the points appear somewhat scattered
without forming a clear upward or downward pattern.
Interpretation
Productivity increases slightly from 1 to 2 cups of coffee. Then it fluctuates slightly
as coffee consumption increases. The points do not follow a consistent linear pattern.
Relationship
This pattern indicates a weak or very low correlation between coffee consumption
and productivity.
Q.1c   What is ETL, explain the transformation phase in ETL process?   5
CO5
BL2
Understan
d
ETL – 2 marks
Transformation phase – 3 marks
ETL stands for Extract, Transform, and Load. It is a process used in data
warehousing to collect data from multiple sources, convert it into a suitable format,
and store it in a data warehouse for analysis.
Phases of ETL
Extract – Data is collected from different source systems such as databases, files, or
applications.
Transform – The extracted data is cleaned, converted, and integrated into a
consistent format.
Load – The transformed data is loaded into the data warehouse.
Transformation is the most complex and intellectually demanding stage of ETL.
During transformation, extracted data is converted into a consistent, clean, and
analysis-ready format. Raw data often contains errors, missing values, duplicates, and
inconsistencies that must be resolved before storage in the data warehouse. One key
transformation activity is data cleaning, which involves removing duplicate records,
handling missing values, and correcting invalid entries. For example, a missing
customer age may be replaced with a default value or derived from other attributes.
Invalid dates or negative quantities are corrected or removed. Another important
transformation task is data integration. Data from different systems may represent the
same entity in different ways. For instance, customer data from multiple systems may
need to be merged into a single unified customer record. Naming conflicts, data type
mismatches, and unit conversions are resolved during this step. Transformation also
includes data standardization, where values are converted into a common format.
Dates may be converted to a standard date format, currencies converted to a single
currency, and text fields standardized for consistency. Business rules are applied
during transformation to ensure data correctness and relevance. In addition,
transformation may involve aggregation, where detailed transactional data is
summarized into
higher-level metrics. For example, daily sales data may be aggregated into monthly or
yearly totals.
Q.1d   Explain the concept of data mart in data warehouse?   5
CO4
********** 2 **********
--- page 3 ---
BL2
Understan
d
Data mart-4 marks
Example -1 marks
A data mart is a smaller, focused subset of a data warehouse that is designed to serve
the analytical needs of a specific business unit or department. Instead of storing data
for the entire organization, a data mart concentrates on a single subject area such as
sales, finance, marketing, or human resources. This focused design makes data marts
easier to understand, faster to query, and more efficient for departmental analysis.
Technically, a data mart contains summarized and relevant data extracted from the
data warehouse. It is structured in a way that supports quick reporting and analysis for
a specific group of users. Because it contains only a portion of the data, it requires less
storage and computing resources compared to a full data warehouse. Example to
Understand a Data Mart Consider a large retail company that operates a centralized
data warehouse storing data related to customers, products, inventory, suppliers, and
sales across all regions. While this warehouse is useful for top-level management, the
sales department may only be interested in sales figures, customer purchase behavior,
and regional performance. For this purpose, a sales data mart is created. This data mart
contains only sales-related data extracted from the data warehouse, organized in a way
that supports sales analysis. Similarly, the finance department may use a finance data
mart containing revenue, expenses, and profit data. Each department works with its
own data mart instead of querying the entire data warehouse.
Q.2a   Explain the lifecycle of Data Science and describe how it can be applied to the use   1
CO1   case of fraud transaction prediction in banking systems.   0
BL3
Apply
Component   Marks
Explanation of Data Science lifecycle with diagram 2
Discovery phase in fraud detection   2
Data preparation using transaction data   2
Model planning and model building   2
Operationalization and communication of results   2
Total   10
The Data Science Lifecycle provides a structured approach for solving real-world
problems using data. It consists of phases such as Discovery, Data Preparation, Model
Planning, Model Building, Operationalization, and Communication of Results.
In the Discovery Phase, the problem is defined clearly. In fraud transaction prediction,
banks aim to detect fraudulent credit card transactions among millions of daily
transactions. Stakeholders and Data Scientists work together to define objectives,
resources, and expected outcomes.
In the Data Preparation Phase, transaction data is collected from banking systems.
Important attributes such as transaction amount, location, time, and frequency are
gathered. The data may contain missing values or inconsistent records, so it must be
cleaned and transformed into a suitable format.
********** 3 **********
--- page 4 ---
In the Model Planning Phase, the approach for solving the problem is decided. Fraud
detection involves analyzing transaction patterns and identifying unusual behaviour.
Suitable algorithms and evaluation metrics are selected to assess model performance.
During the Model Building Phase, the dataset is divided into training and testing
datasets. The model learns patterns of normal transactions from the training data. Once
trained, it is tested on unseen data to evaluate how well it can identify suspicious
activities.
In the Operationalization Phase, the model is deployed into banking systems where it
monitors transactions in real time. The system automatically flags suspicious
transactions for further investigation.
Finally, in the Communication Phase, the results are communicated to security teams
and customers, helping reduce financial losses and improve trust in banking systems.
Q.2b   Weekly temperatures (°C) recorded are: 30, 31, 29, 30, 32, 31, 45. Detect the outlier   1
CO2   using both Z-score (consider population data) and IQR methods.   0
BL3
Apply
Step   Marks
Mean calculation   2
Standard deviation calculation   2
Z-score calculation for all values   2
Q1, Q3 and IQR calculation   2
Identification of outlier using both methods 2
Mean = 32.57
Standard deviation = 5.15
Value Z-score
30   -0.50
31   -0.31
29   -0.69
30   -0.50
32   -0.11
31   -0.31
45   2.41
Z-score result: No outlier
IQR
Sorted
29, 30, 30, 31, 31, 32, 45
Q1 = 30
Q3 = 32
IQR = 2
Upper bound = 35
45 is an outlier.
Q.3a   Define Label Encoding and One-Hot Encoding and explain their role in preparing 1
CO2   categorical data for machine learning models. A column named “Customer Education 0
BL3   Level” contains the categories High School, Diploma, Bachelor’s Degree, Master’s
Apply   Degree, and PhD.
Perform Label Encoding and One-Hot Encoding on this column.
Explanation of Label Encoding – 2 marks
Explanation of One-Hot Encoding – 2 marks
********** 4 **********
--- page 5 ---
Correct Label Encoding mapping – 3 marks
Correct One-Hot Encoding columns – 3 marks
Label Encoding:
Label Encoding converts categorical values into numeric labels, where each category
is assigned a unique integer.
One-Hot Encoding:
One-Hot Encoding converts each category into a separate binary column indicating
presence (1) or absence (0).
Label Encoding
Bachelor → 0
Diploma → 1
High School → 2
Master → 3
PhD → 4
One-Hot Encoding
Edu_HighSchool
Edu_Diploma
Edu_Bachelor
Edu_Master
Edu_PhD
Each column contains 1 if the record belongs to that category otherwise 0. (Must be
shown in tabular format)
Q.3b   Explain Min-Max Scaling and Robust Scaling. A dataset column called “Weekly   1
CO2   Study Hours” contains 5, 8, 10, 6, 12, 9 and 7 hours. Perform both scaling methods.   0
BL3
Apply
Explanation of Robust Scaling and formula – 3 marks
Explanation of Min-Max Scaling and formula– 3 marks
Robust scaling calculations – 2 marks
Min-Max scaling calculations – 2 marks
1. Min-Max Scaling Min-Max Scaling is a normalization technique that rescales
numerical values into a fixed range between 0 and 1 while preserving relationships
among the original values.
x' = x - x_{min} /{x_{max} - x_{min}}
Min-Max Scaling
Minimum = 5
Maximum = 12
Scaled values
5 → 0
8 → 0.43
10 → 0.71
6 → 0.14
12 → 1
9 → 0.57
7 → 0.29
2. Robust Scaling : Robust Scaling uses the median and interquartile range (IQR) to
scale the data, making it less sensitive to outliers.
********** 5 **********
--- page 6 ---
x' = x - x_{median} /{IQR}
Sorted data
5, 6, 7, 8, 9, 10, 12
Median = 8
Q1 = 6
Q3 = 10
IQR = 4
Scaled values
5 → -0.75
8 → 0
10 → 0.50
6 → -0.50
12 → 1
9 → 0.25
7 → -0.25
Q.4a   Write the code and corresponding output for each of the following:   1
CO3   i) Create a NumPy array using arange() from 30 to 38 (included).   0
BL3   ii) Convert the array into 3 × 3 matrix.
Apply   iii) Print the matrix size.
iv) Print the number of dimensions of matrix.
v) Extract the middle row of 3 × 3 matrix using slicing.
Part   Marks
i   2
ii   2
iii   2
iv   2
v   2
import numpy as np
arr = np.arange(30,39)
matrix = arr.reshape(3,3)
print(matrix.size)
print(matrix.ndim)
print(matrix[1, : :])
Array
[30 31 32 33 34 35 36 37 38]
Matrix
[[30 31 32]
[33 34 35]
[36 37 38]]
Size = 9
Dimensions = 2
Slice
[33 34 35]
Q.4b   Create two 3 × 3 NumPy arrays.   1
CO3   Array A contains 3, 6, 9; 12, 15, 18; 21, 24, 27.   0
BL3   Array B contains 1, 2, 3; 4, 5, 6; 7, 8, 9.
Apply   Using nested for loops, perform following and show the output:
a) Element-wise addition (Array A + Array B)
b) Element-wise subtraction (Array A - Array B)
Creating two arrays – 2 marks
Correct nested loop structure – 2 marks
Element-wise subtraction logic – 3 marks
********** 6 **********
--- page 7 ---
Element-wise addition logic – 3 marks
import numpy as np
# Creating arrays
A = np.array([[3,6,9],
[12,15,18],
[21,24,27]])
B = np.array([[1,2,3],
[4,5,6],
[7,8,9]])
# Creating result arrays
add = np.zeros((3,3))
sub = np.zeros((3,3))
# Nested loops
for i in range(3):
for j in range(3):
add[i][j] = A[i][j] + B[i][j]
sub[i][j] = A[i][j] - B[i][j]
# Printing results
print("Array A:\n",A)
print("Array B:\n",B)
print("Addition Result:\n",add)
print("Subtraction Result:\n",sub)
Addition
[[4 8 12]
[16 20 24]
[28 32 36]]
Subtraction
[[2 4 6]
[8 10 12]
[14 16 18]]
Q.5a   Create a DataFrame product_df with columns: Product_ID, Price, Quantity, Category, 1
CO3   Supplier   0
BL3   The rows are:
Apply   Rows:
Row1: 301, 1200, 10, Electronics, SupplierA
Row2: 302, price missing, 15, Electronics, SupplierB
Row3: 303, 900, quantity missing, Furniture, SupplierA
Row4: 304, 1500, 8, Furniture, SupplierC
Row5: 305, 1100, 12, Electronics, SupplierB
Perform the following with appropriate code:
i) Create the DataFrame
ii) Select Product_ID, Price, Category (without loc/iloc)
iii) Write code to check sum of missing values in each column
iv) Replace missing values using mean of the respective column.
Part   Marks
i   4
********** 7 **********
--- page 8 ---
ii   2
iii   2
iv   2
import pandas as pd
import numpy as np
data = {
"Product_ID":[301,302,303,304,305],
"Price":[1200,np.nan,900,1500,1100],
"Quantity":[10,15,np.nan,8,12],
"Category":["Electronics","Electronics","Furniture","Furniture","Electronics"],
"Supplier":["SupplierA","SupplierB","SupplierA","SupplierC","SupplierB"]
}
product_df = pd.DataFrame(data)
print(product_df[["Product_ID","Price","Category"]])
print(product_df.isnull().sum())
product_df["Price"].fillna(product_df["Price"].mean(), inplace=True)
product_df["Quantity"].fillna(product_df["Quantity"].mean(), inplace=True)
print(product_df)
Q.5b   Given DataFrame product_df   1
CO3   Product_ID Price Quantity   Category   Supplier   0
BL3   0   301 1200   10   Electronics   A
Apply   1   302 900   15   Furniture   B
2   303 1500   8   Electronics   A
3   304 1100   12   Furniture   C
4   305 1300   9   Electronics   B
5   306 1000   14   Furniture   A
6   307 1600   7   Electronics   C
i) What will be the output of print(product_df.head(3))
ii) What will be output of product_df.loc[1:3, ['Price','Category']]
iii) Write a query to display products where Price > 1200 AND Category = Electronics.
Also write the respective output.
iv) Write a code to Sort dataframe by Quantity and write its output.
v) Write code to rename columns using rename function for:
Price → Cost, Quantity → Stock, Category → Type.
Part   Marks
i   1
ii   2
iii   3
iv   2
v   2
a) Output
Product_ID Price Quantity   Category Supplier
0   301 1200   10   Electronics   A
1   302 900   15   Furniture   B
2   303 1500   8   Electronics   A
b) Output
********** 8 **********
--- page 9 ---
Price   Category
1 900   Furniture
2 1500 Electronics
3 1100   Furniture
c) Query
product_df[(product_df["Price"]>1200) & (product_df["Category"]=="Electronics")]
Output
Product_ID Price Quantity   Category Supplier
2   303 1500   8 Electronics   A
4   305 1300   9 Electronics   B
6   307 1600   7 Electronics   C
d) Code
product_df.sort_values(by="Quantity")
Output
Product_ID Price Quantity   Category Supplier
6   307 1600   7 Electronics   C
2   303 1500   8 Electronics   A
4   305 1300   9 Electronics   B
0   301 1200   10 Electronics   A
3   304 1100   12   Furniture   C
5   306 1000   14   Furniture   A
1   302 900   15   Furniture   B
e) Rename Code
product_df.rename(columns={"Price":"Cost","Quantity":"Stock","Category":"Type"
}, inplace=True)
Q.6a   Explain why organizations need both OLTP and OLAP systems.   1
CO4   0
BL2
Understan
d
Purpose of OLTP – 5
Purpose of OLAP – 5
Organizations require both OLTP and OLAP systems because they serve different but
complementary purposes.
OLTP systems are responsible for managing day-to-day business transactions such as
deposits, withdrawals, billing, and order processing. These systems must process
transactions quickly and accurately in real time.
OLAP systems, on the other hand, are designed for analytical processing. They
analyze historical data to identify trends, patterns, and relationships that help
organizations make strategic decisions.
Running complex analytical queries directly on OLTP systems would slow down
operational processes. Therefore, OLAP systems operate separately using data stored
in data warehouses.
In modern enterprises, OLTP systems generate raw operational data, while OLAP
systems analyse that data to provide insights for decision-making.
OLTP and OLAP systems serve complementary roles in an organization. Without
OLTP systems, an organization cannot function operationally. Without OLAP
systems, an organization cannot make informed strategic decisions. Modern
enterprises rely on OLTP systems to efficiently handle daily operations and on OLAP
********** 9 **********
--- page 10 ---
systems to analyze data and plan for the future. In the context of Data Science, OLTP
systems act as sources of raw data, while OLAP systems provide structured and
historical data for analysis, reporting, and machine learning.
Q.6b   Explain the different types of metadata used in data warehousing.   1
CO5   0
BL2
Understan
d
Definition of metadata types – 2
Operational metadata – 3
Extraction and transformation metadata – 3
Business metadata – 2
In a data warehousing environment, metadata is generally classified into three main
types: operational metadata, extraction and transformation metadata, and business
metadata.
Operational metadata describes the operational status of ETL processes and the data
warehouse. It includes information such as job schedules, execution time, data load
frequency, and error logs. This metadata helps administrators monitor system
performance.
Extraction and transformation metadata defines how data moves from source systems
to the data warehouse. It includes details about source tables, data types,
transformation rules, and source-to-target mappings. This type of metadata supports
data lineage and traceability.
Business metadata is designed for business users and explains the meaning of data
elements. It includes KPI definitions, business rules, and report descriptions to help
users interpret data correctly.
Together, these metadata types ensure transparency, control, and effective
management of the data warehouse.
Q.7a   What is the significance of data quality tool. Explain data profiling and data   1
CO5   cleansing for data quality tool functions.   0
BL2
Understan
d
Data Quality tool functions – 2
Data profiling – 4
Data cleansing – 4
A data quality tool is not a single cleaning program. Instead, it is a comprehensive
software system designed to analyze, control, improve, and continuously monitor the
quality of data used in analytics, reporting, and data science projects. These tools are
widely used in industries such as banking, healthcare, e-commerce, telecom, and
government systems. Data Profiling Data profiling is the starting point of all data
quality activities. Technically, data profiling means examining the structure and actual
content of data before making any changes to it. At this stage, the tool scans each
column of the dataset to understand what kind of values exist, how frequently they
appear, and whether they follow expected patterns. For example, if we consider a
student database, data profiling may reveal that the “Age” column contains values like
18, 19, 20, but also values such as 3 or 150. It may also show that some records have
missing roll numbers or that names appear in different formats. Importantly, profiling
does not correct anything; it only provides visibility into hidden data problems.
Without profiling, organizations work blindly.
Data Cleansing Data cleansing is the process of removing or correcting errors and
inconsistencies identified during profiling and validation. This is the stage where
data quality is actively improved. In real systems, cleansing may involve correcting
spelling mistakes, replacing invalid values, filling missing data using defined logic,
********** 10 **********
--- page 11 ---
or removing records that cannot be corrected. For example, if a city name appears as
“Chennai”, “Madras”, and “CHN”, cleansing standardizes all values into one
accepted format. This ensures that reports and analysis are accurate.
Q.7b   Explain the concept of unit testing and acceptance testing in data warehouse?   1
CO4   0
BL2
Understan
d
Unit testing -5
Acceptance testing -5
Data warehouse testing is performed at four progressive levels, where each level
checks correctness from a different perspective. These levels move from small isolated
components to complete business validation, ensuring reliability at every stage. The
first level is Unit Testing, where individual components such as ETL jobs,
transformations, and calculations are tested independently. The goal here is to ensure
that each small piece of logic works exactly as intended before it interacts with
anything else.
Unit testing in data warehousing refers to the process of verifying individual data
warehouse components in isolation. These components typically include ETL jobs,
data transformations, calculations, constraints, and validation rules. At this stage, we
do not test the entire data flow. Instead, we focus on one transformation or one rule at
a time, ensuring it produces the correct output for a given input. This approach helps
identify errors at an early stage, when they are easier and cheaper to fix. For example,
if an ETL job converts sales amounts from dollars to rupees, unit testing ensures that
the conversion formula is mathematically correct and consistently applied. Key Focus
Areas One major focus area of unit testing is data transformations. In a data
warehouse, raw data is rarely used directly. It is transformed according to business
rules-for example, categorizing customers as “Premium” or “Regular” based on
purchase value. Unit testing ensures that these rules are implemented correctly and
consistently. Another important focus area is calculations. Data warehouses store
derived metrics such as total revenue, average order value, profit margin, and growth
percentage. Unit testing verifies the accuracy of these calculations so that reports do
not show misleading numbers. Unit testing also checks data types and formats. This
ensures that date fields, numeric fields, and string fields are stored in the correct
format. For instance, a date should not be stored as text, and numeric fields should not
contain invalid characters. Finally, constraints and validation rules are tested. This
includes checks such as primary key uniqueness, non null constraints, and referential
integrity. These validations prevent incorrect or incomplete data from entering the
warehouse.
Acceptance testing is the final stage of testing performed before the data warehouse
system is deployed for actual use. It ensures that the system meets the business
requirements and expectations of end users.
This type of testing is usually performed by business users, analysts, or stakeholders
rather than developers. They evaluate whether the system provides correct reports,
accurate analytics, and meaningful insights.
For example, a marketing analyst may verify whether sales reports generated from the
data warehouse match the expected results based on known data patterns.
Acceptance testing focuses on business functionality rather than technical details. If
the system meets user expectations, it is approved for deployment. Therefore,
acceptance testing ensures that the data warehouse system fulfills its intended purpose
for decision-making.
Types of Acceptance Testing The first type mentioned is User Acceptance Testing
(UAT). Here, actual business users test the system using real-life scenarios. For
example, sales managers verify whether monthly sales reports show correct totals and
********** 11 **********
--- page 12 ---
trends. The second type is Business Acceptance Testing (BAT). This focuses on
validating complete business processes. For instance, management checks whether the
data warehouse supports decision-making processes such as forecasting, budgeting,
and performance analysis. Next is Alpha Testing, which is conducted internally within
the organization. The system is tested by internal teams before being exposed to real
users. Then comes Beta Testing, where a limited number of external or end users test
the system and provide feedback. This helps identify real-world usability issues that
developers might miss.
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper ba25c034c547

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AIDS_7056/Data Wrangling/ANS_Data Wrangling(702DB0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MBA Tech (DS)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO- 1;   a.   1. Structured data is highly organized in tables with rows and columns and can be   [5]
BL-2   easily stored and queried using relational databases (example: SQL databases,
Excel sheets).
2. Semi-structured data does not follow strict tabular structure but uses tags or
markers to separate elements (example: JSON, XML, CSV with variable fields).
3. Unstructured data has no predefined format or model and is difficult to store and
analyze directly (example: text documents, images, audio, video, emails).
4. Structured data is easiest to search and analyze, semi-structured provides
flexibility with some structure, while unstructured offers the most flexibility but
requires complex tools.
5. Structured data fits SQL databases, semi-structured fits NoSQL systems, and
unstructured often requires big data tools, AI, or text mining for analysis.
CO-2 ;   b.   1. Data warehouses store sensitive historical and business-critical information, so   [5]
BL-3   security protects it from unauthorized access.
2. Security measures maintain data integrity by preventing unauthorized changes that
might lead to false analytics.
3. Legal and regulatory compliance (such as GDPR, HIPAA) requires strong security
controls to protect personal and financial data.
4. Security mechanisms like encryption, access control, and monitoring defend
against data breaches and insider threats.
5. Secure data warehouses build trust, ensure reliable decision-making, and support
business continuity.
********** 1 **********
--- page 2 ---
c.   1. Human errors such as spelling mistakes or inconsistent formats can make data   [5]
inaccurate.
2. Duplicate records occur when the same entry is added multiple times from
different sources.
3. Missing or incomplete data leads to gaps that affect accurate analysis.
4. Outdated information, such as old addresses or prices, reduces the reliability of
reports.
5. Data integration from multiple sources with different formats or rules causes
inconsistencies.
Impact: Dirty data results in incorrect reports, poor business decisions, reduced
customer satisfaction, wasted time and money, and loss of trust in the
organization’s data.
d.   1. Data granularity refers to the level of detail or depth of data stored in a system.   [5]
2. High granularity means very detailed data, such as each transaction or each
customer action.
3. Low granularity means summarized or aggregated data, such as daily or monthly
totals.
4. High granularity provides flexibility and deeper analysis but requires more storage
and processing time.
5. Choosing the right granularity is crucial in data warehousing because it affects
storage, performance, and the quality of insights.
Q2   [20]
CO-   a. # 1. Create a list and multiply each element by 10   [10]
2 ;BL-   numbers = [1, 2, 3, 4, 5]
3   multiplied = [num * 10 for num in numbers]
print("After multiplying by 10:", multiplied)
# 2. Filter numbers greater than a certain value
threshold = 3
filtered = [num for num in numbers if num > threshold]
print("Numbers greater than", threshold, ":", filtered)
# 3. Calculate the sum of all numbers
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)
# 4. Find the mode (most frequent number)
from statistics import mode
numbers_with_duplicates = [2, 3, 2, 5, 4, 2, 3]
most_frequent = mode(numbers_with_duplicates)
• print("Mode of the list:", most_frequent)
OUTPUT:
First print: each element multiplied by 10 → [10, 20, 30, 40, 50]
Second print: numbers > 3 → [4, 5]
Third print: sum of numbers → 15
Fourth print: most frequent number in [2,3,2,5,4,2,3] → 2
R Codes:
# 1. Create a vector and multiply each element by 10
numbers <- c(1, 2, 3, 4, 5)
********** 2 **********
--- page 3 ---
multiplied <- numbers * 10
print(multiplied)
# 2. Filter numbers greater than a certain value
threshold <- 3
filtered <- numbers[numbers > threshold]
print(filtered)
# 3. Calculate the sum of all numbers
total_sum <- sum(numbers)
print(total_sum)
# 4. Find the mode (most frequent number)
numbers_with_duplicates <- c(2, 3, 2, 5, 4, 2, 3)
mode_value <- as.numeric(names(sort(table(numbers_with_duplicates), decreasing
= TRUE)[1]))
print(mode_value)
•   First print: [10 20 30 40 50]
• Second print: [4 5]
• Third print: 15
• Fourth print: 2 (most frequent number)
b. import numpy as np   [10]
CO-
3 ;BL-   # 1. Create two 2x2 matrices A and B
A = np.array([[1, 2],
3   [3, 4]])
B = np.array([[5, 6],
[7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
# 2. Addition (A + B)
add_result = A + B
print("\nA + B:\n", add_result)
# 2. Matrix Multiplication (A * B)
mult_result = A.dot(B)
print("\nA x B:\n", mult_result)
# 3. Extract element in second row, first column
print("\nElement A[2,1]:", A[1, 0])
print("Element B[2,1]:", B[1, 0])
# 4. Replace main diagonal with 0
A_diag_zero = A.copy()
B_diag_zero = B.copy()
np.fill_diagonal(A_diag_zero, 0)
np.fill_diagonal(B_diag_zero, 0)
print("\nA with diagonal 0:\n", A_diag_zero)
print("\nB with diagonal 0:\n", B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 = A + 5
B1 = B + 5
print("\nA1 (A + 5):\n", A1)
• print("\nB1 (B + 5):\n", B1)
R:
********** 3 **********
--- page 4 ---
# 1. Create two 2x2 matrices A and B
A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)
B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
# 2. Addition (A + B)
add_result <- A + B
print("A + B:")
print(add_result)
# 2. Matrix multiplication
mult_result <- A %*% B
print("A x B:")
print(mult_result)
# 3. Extract element in second row, first column
print(paste("Element A[2,1]:", A[2,1]))
print(paste("Element B[2,1]:", B[2,1]))
# 4. Replace main diagonal with 0
A_diag_zero <- A
B_diag_zero <- B
diag(A_diag_zero) <- 0
diag(B_diag_zero) <- 0
print("A with diagonal 0:")
print(A_diag_zero)
print("B with diagonal 0:")
print(B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 <- A + 5
B1 <- B + 5
print("A1 (A + 5):")
print(A1)
print("B1 (B + 5):")
print(B1)
Q3   [20]
CO-2 ;   a. import pandas as pd   [10]
BL-3   import numpy as np
# Create dataset
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# 1. Median Experience of Fin Dept
median_exp_fin = df[df["Dept"] == "Fin"]["Experience"].median()
print("\nMedian Experience of Fin Dept:", median_exp_fin)
# 2. Average Bonus of HR Dept
avg_bonus_hr = df[df["Dept"] == "HR"]["Bonus"].mean()
print("Average Bonus of HR Dept:", avg_bonus_hr)
# 3. Fill NaN values
# Justification: Using median for numeric fields to reduce the impact of outliers
df_filled = df.copy()
numerical_cols = ["Training_Hours", "Score"]
for col in numerical_cols:
median_value = df_filled[col].median()
********** 4 **********
--- page 5 ---
df_filled[col].fillna(median_value, inplace=True)
print("\nDataFrame after filling missing values:\n", df_filled)
Or
# Create dataset
print("Original Data Frame:")
print(df)
# 1. Median Experience of Fin Dept
median_exp_fin <- median(df$Experience[df$Dept == "Fin"])
print(paste("Median Experience of Fin Dept:", median_exp_fin))
# 2. Average Bonus of HR Dept
avg_bonus_hr <- mean(df$Bonus[df$Dept == "HR"])
print(paste("Average Bonus of HR Dept:", avg_bonus_hr))
# 3. Fill NA values (using median)
# Justification: Median avoids outlier influence
df_filled <- df
numeric_cols <- c("Training_Hours", "Score")
for (col in numeric_cols) {
med <- median(df_filled[[col]], na.rm = TRUE)
df_filled[[col]][is.na(df_filled[[col]])] <- med
}
print("Data Frame after filling NA values:")
print(df_filled)
CO-3 ; B # 1. Create a vector v1 with EVEN numbers from 500 to 300   [10]
BL-3   v1 <- seq(500, 300, by = -2) # Descending order initially
print("v1 (descending):")
print(v1)
# 2. Arrange the numbers in ascending order
v1 <- sort(v1) # Sort in ascending order
print("v1 (ascending):")
print(v1)
# 3. Total number of elements in v1
total_elements <- length(v1)
print(paste("Total number of elements in v1:", total_elements))
# 4. Check the dimension of v1
dim_v1 <- dim(v1)
# For a vector, dim() is NULL; vectors are 1-dimensional
print("Dimension of v1:")
print(dim_v1)
# 5. Find the index of number 450
index_450 <- which(v1 == 450)
print(paste("Index of number 450 in v1:", index_450))
OR
# 1. Create a list LIS1 with EVEN numbers from 500 to 300
LIS1 = list(range(500, 299, -2)) # Descending order
print("LIS1 (descending):", LIS1)
# 2. Arrange the numbers in ascending order
LIS1.sort()
print("LIS1 (ascending):", LIS1)
# 3. Total number of elements in LIS1
total_elements = len(LIS1)
print("Total number of elements in LIS1:", total_elements)
# 4. Check the dimension of LIS1
# Lists in Python are 1-dimensional
dimension = 1 # By default
print("Dimension of LIS1:", dimension)
********** 5 **********
--- page 6 ---
# 5. Check the index of number 450
index_450 = LIS1.index(450)
print("Index of number 450 in LIS1:", index_450)
Q4   [20]
CO-2 ;   a.   1. Data Profiling – Analyzes data to identify patterns, inconsistencies, and   [5]
BL-2   anomalies.
2. Data Cleansing – Detects and corrects errors such as duplicates, missing values,
or incorrect formats.
3. Data Standardization – Ensures consistency in data formats, units, naming
conventions, and codes.
4. Data Validation – Checks data against defined rules or constraints to ensure
accuracy and completeness.
5. Monitoring and Reporting – Tracks data quality over time and generates reports
for corrective action.
CO-3 ;   b.   1. Data Cleaning – Removes errors, duplicates, or irrelevant data before loading.   [5]
BL-2   2. Data Integration – Combines data from multiple sources into a unified format.
3. Data Aggregation – Summarizes data, e.g., total sales per month or per region.
4. Data Conversion – Converts data types, formats, or units to match target schema.
5. Data Enrichment – Enhances data by adding derived values, calculated fields, or
external information.
CO-2 ;   c.   1. Definition/Role of Metadata – Metadata is “data about data” that describes   [10]
BL-3   structure, meaning, source, and usage of data in the warehouse. It helps in
understanding, managing, and using data efficiently.
Types of Metadata:
2. Business Metadata – Describes meaning of data in business terms (e.g.,
“Customer_ID represents unique customer”).
3. Technical Metadata – Contains technical details about data storage, tables,
columns, data types, and ETL mappings.
4. Operational Metadata – Provides information on data lineage, refresh schedules,
load timings, and ETL process logs.
How Metadata Supports ETL:
5. Guides ETL tools on source-target mapping, transformation rules, and validation.
6. Tracks data lineage to trace back errors to source systems.
7. Ensures consistent and accurate transformations.
How Metadata Supports Decision-Making:
8. Helps business users understand the context and meaning of data.
9. Ensures confidence in reports and analytics by providing source and
transformation information.
10. Enables impact analysis when schema or data changes occur.
Q5   [20]
CO-2 ;   a.   1. Unit Testing – Test individual ETL components or transformations.   [5]
BL-2   2. System Testing – Test the complete end-to-end ETL process.
3. Data Integration Testing – Verify data from multiple sources is correctly
combined.
4. User Acceptance Testing (UAT) – Business users validate reports and dashboards.
5. Regression Testing – Ensure changes do not break existing functionality.
CO-3 ;   b.   1. Initial Load – Extract complete dataset from source systems and load into the data   [5]
BL-2   warehouse.
2. Data Validation – Check for consistency, integrity, and correctness before loading.
3. Incremental Updates – Apply new or modified records based on primary keys or
unique identifiers.
********** 6 **********
--- page 7 ---
4. Data Maintenance – Handle updates, corrections, and deletions in the warehouse
to reflect source changes.
5. Backup and Audit – Maintain history logs, backup data, and audit trails for
accuracy and compliance.
CO-   c.   1. Problem Definition – Understand business objective: predict which customers   [10]
1 ;BL-   will make repeat purchases. Identify success criteria and KPIs.
3   2. Data Collection – Gather data from e-commerce sources: transaction history,
customer profiles, website interactions, product data.
3. Data Cleaning and Preprocessing – Handle missing values, remove duplicates,
standardize formats, and engineer features like purchase frequency or recency.
4. Exploratory Data Analysis (EDA) – Analyze patterns, correlations, and trends in
the data. Visualize customer behavior and purchase patterns.
5. Feature Engineering – Create meaningful features to improve model performance,
e.g., average purchase value, days since last purchase
6. Model Selection – Choose appropriate predictive models (e.g., logistic regression,
decision trees, random forest, or gradient boosting).
7. Model Training and Evaluation – Split data into training and test sets. Train model
and evaluate performance using metrics like accuracy, precision, recall, or ROC-
AUC.
8. Model Tuning and Optimization – Adjust hyperparameters, perform cross-
validation, and improve prediction accuracy.
9. Deployment – Implement the model in production to predict repeat purchases for
new customers.
10. Monitoring and Maintenance – Continuously monitor model performance, update
with new data, and retrain periodically to ensure accuracy.
Q 6   [20]
CO-3 ;   a.   1. Batch Transfer – Move data at scheduled intervals from the warehouse to near-   [10]
BL-3   line storage.
2. Incremental Loading – Transfer only new or updated records to reduce processing
time.
3. Data Archiving – Automatically archive historical data to near-line storage for
cost efficiency.
4. Data Compression – Compress data before transfer to save storage and bandwidth.
5. Data Partitioning – Split large datasets into manageable segments for easier
migration.
6. Automated ETL Jobs – Use ETL workflows to orchestrate data movement to near-
line storage.
7. Replication / Mirroring – Maintain a near-line copy synchronized with the
warehouse.
8. Data Retention Policies – Define rules for how long data stays in the warehouse
before moving.
9. Error Handling & Logging – Monitor transfer failures and ensure reliable
dataflow.
10. Access Control – Secure sensitive data during transfer and storage in near-line
systems.
CO-2 ;   b. Front-Room (Presentation Layer)   [10]
BL-2
1. Query & Reporting Tools – Enable users to access, analyze, and generate reports.
2. OLAP Tools – Provide multidimensional analysis and dashboards.
3. Data Mining Tools – Support predictive analytics and pattern discovery.
4. End-User Interface – Web portals, dashboards, or BI tools for business users.
5. Metadata Access – Provides business definitions and context for users.
Back-Room (Data Storage & ETL Layer)
********** 7 **********
--- page 8 ---
1. Source Systems – Operational databases, ERP, CRM, and external data sources.
2. ETL/ELT Processes – Extract, transform, and load data into the warehouse.
3. Data Staging Area – Temporary storage for cleaning, transformation, and
integration.
4. Data Warehouse Storage – Central repository for structured and historical data.
5. Metadata Repository – Stores technical, business, and operational metadata for
ETL and user access.
Q 7   [20]
CO-2 ;   a.   1. Subject-Oriented – Data is organized around key subjects such as customers,   [10]
BL-2   products, or sales rather than specific applications. This allows for easier analysis
of business processes.
2. Integrated – Combines data from multiple heterogeneous sources (databases, flat
files, external data) into a consistent format with standardized naming
conventions, units, and encoding.
3. Time-Variant – Historical data is maintained to allow analysis over different
periods (daily, monthly, yearly). Each record is associated with a time element to
track changes.
4. Non-Volatile / Read-Only – Once data is loaded into the warehouse, it is not
frequently updated or deleted. This ensures data stability for analysis and
reporting.
5. Accessible / Query-Oriented – Optimized for complex queries, reporting, and
analytical processing rather than transactional processing.
6. Support for Decision-Making – Enables business intelligence, trend analysis, and
strategic decision-making by providing accurate, consistent, and consolidated
data.
7. Metadata-Driven – Metadata provides information about data sources, definitions,
transformations, and usage, which helps users understand and trust the data.
CO-3 ;   b.   1. Type 0: Retain Original – Values never change; history preserved.   [10]
BL-3   2. Type 1: Overwrite – Update value in-place; history lost.
3. Type 2: Add New Row – Insert new row; old row retained with versioning.
4. Type 3: Add New Column – Store previous value in a separate column.
5. Type 4: Historical Table – Maintain separate table for historical data.
6. Type 6: Hybrid – Combines Types 1, 2, 3 for full and partial history.
7. Update Strategy: Compare source and dimension, insert/update according to SCD
type, use surrogate keys and dates for tracking.
8. Significance: Preserves historical accuracy, supports trend analysis, ensures
reliable reporting, and maintains data integrity.
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper d90b49a4139f

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CSE_DS_7057/Data Wrangling/ANS_Data Wrangling(702DB0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (DS)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO- 1;   a.   1. Structured data is highly organized in tables with rows and columns and can be   [5]
BL-2   easily stored and queried using relational databases (example: SQL databases,
Excel sheets).
2. Semi-structured data does not follow strict tabular structure but uses tags or
markers to separate elements (example: JSON, XML, CSV with variable fields).
3. Unstructured data has no predefined format or model and is difficult to store and
analyze directly (example: text documents, images, audio, video, emails).
4. Structured data is easiest to search and analyze, semi-structured provides
flexibility with some structure, while unstructured offers the most flexibility but
requires complex tools.
5. Structured data fits SQL databases, semi-structured fits NoSQL systems, and
unstructured often requires big data tools, AI, or text mining for analysis.
CO-2 ;   b.   1. Data warehouses store sensitive historical and business-critical information, so   [5]
BL-3   security protects it from unauthorized access.
2. Security measures maintain data integrity by preventing unauthorized changes that
might lead to false analytics.
3. Legal and regulatory compliance (such as GDPR, HIPAA) requires strong security
controls to protect personal and financial data.
4. Security mechanisms like encryption, access control, and monitoring defend
against data breaches and insider threats.
5. Secure data warehouses build trust, ensure reliable decision-making, and support
business continuity.
********** 1 **********
--- page 2 ---
c.   1. Human errors such as spelling mistakes or inconsistent formats can make data   [5]
inaccurate.
2. Duplicate records occur when the same entry is added multiple times from
different sources.
3. Missing or incomplete data leads to gaps that affect accurate analysis.
4. Outdated information, such as old addresses or prices, reduces the reliability of
reports.
5. Data integration from multiple sources with different formats or rules causes
inconsistencies.
Impact: Dirty data results in incorrect reports, poor business decisions, reduced
customer satisfaction, wasted time and money, and loss of trust in the
organization’s data.
d.   1. Data granularity refers to the level of detail or depth of data stored in a system.   [5]
2. High granularity means very detailed data, such as each transaction or each
customer action.
3. Low granularity means summarized or aggregated data, such as daily or monthly
totals.
4. High granularity provides flexibility and deeper analysis but requires more storage
and processing time.
5. Choosing the right granularity is crucial in data warehousing because it affects
storage, performance, and the quality of insights.
Q2   [20]
CO-   a. # 1. Create a list and multiply each element by 10   [10]
2 ;BL-   numbers = [1, 2, 3, 4, 5]
3   multiplied = [num * 10 for num in numbers]
print("After multiplying by 10:", multiplied)
# 2. Filter numbers greater than a certain value
threshold = 3
filtered = [num for num in numbers if num > threshold]
print("Numbers greater than", threshold, ":", filtered)
# 3. Calculate the sum of all numbers
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)
# 4. Find the mode (most frequent number)
from statistics import mode
numbers_with_duplicates = [2, 3, 2, 5, 4, 2, 3]
most_frequent = mode(numbers_with_duplicates)
• print("Mode of the list:", most_frequent)
OUTPUT:
First print: each element multiplied by 10 → [10, 20, 30, 40, 50]
Second print: numbers > 3 → [4, 5]
Third print: sum of numbers → 15
Fourth print: most frequent number in [2,3,2,5,4,2,3] → 2
R Codes:
# 1. Create a vector and multiply each element by 10
numbers <- c(1, 2, 3, 4, 5)
********** 2 **********
--- page 3 ---
multiplied <- numbers * 10
print(multiplied)
# 2. Filter numbers greater than a certain value
threshold <- 3
filtered <- numbers[numbers > threshold]
print(filtered)
# 3. Calculate the sum of all numbers
total_sum <- sum(numbers)
print(total_sum)
# 4. Find the mode (most frequent number)
numbers_with_duplicates <- c(2, 3, 2, 5, 4, 2, 3)
mode_value <- as.numeric(names(sort(table(numbers_with_duplicates), decreasing
= TRUE)[1]))
print(mode_value)
•   First print: [10 20 30 40 50]
• Second print: [4 5]
• Third print: 15
• Fourth print: 2 (most frequent number)
b. import numpy as np   [10]
CO-
3 ;BL-   # 1. Create two 2x2 matrices A and B
A = np.array([[1, 2],
3   [3, 4]])
B = np.array([[5, 6],
[7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
# 2. Addition (A + B)
add_result = A + B
print("\nA + B:\n", add_result)
# 2. Matrix Multiplication (A * B)
mult_result = A.dot(B)
print("\nA x B:\n", mult_result)
# 3. Extract element in second row, first column
print("\nElement A[2,1]:", A[1, 0])
print("Element B[2,1]:", B[1, 0])
# 4. Replace main diagonal with 0
A_diag_zero = A.copy()
B_diag_zero = B.copy()
np.fill_diagonal(A_diag_zero, 0)
np.fill_diagonal(B_diag_zero, 0)
print("\nA with diagonal 0:\n", A_diag_zero)
print("\nB with diagonal 0:\n", B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 = A + 5
B1 = B + 5
print("\nA1 (A + 5):\n", A1)
• print("\nB1 (B + 5):\n", B1)
R:
********** 3 **********
--- page 4 ---
# 1. Create two 2x2 matrices A and B
A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)
B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
# 2. Addition (A + B)
add_result <- A + B
print("A + B:")
print(add_result)
# 2. Matrix multiplication
mult_result <- A %*% B
print("A x B:")
print(mult_result)
# 3. Extract element in second row, first column
print(paste("Element A[2,1]:", A[2,1]))
print(paste("Element B[2,1]:", B[2,1]))
# 4. Replace main diagonal with 0
A_diag_zero <- A
B_diag_zero <- B
diag(A_diag_zero) <- 0
diag(B_diag_zero) <- 0
print("A with diagonal 0:")
print(A_diag_zero)
print("B with diagonal 0:")
print(B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 <- A + 5
B1 <- B + 5
print("A1 (A + 5):")
print(A1)
print("B1 (B + 5):")
print(B1)
Q3   [20]
CO-2 ;   a. import pandas as pd   [10]
BL-3   import numpy as np
# Create dataset
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# 1. Median Experience of Fin Dept
median_exp_fin = df[df["Dept"] == "Fin"]["Experience"].median()
print("\nMedian Experience of Fin Dept:", median_exp_fin)
# 2. Average Bonus of HR Dept
avg_bonus_hr = df[df["Dept"] == "HR"]["Bonus"].mean()
print("Average Bonus of HR Dept:", avg_bonus_hr)
# 3. Fill NaN values
# Justification: Using median for numeric fields to reduce the impact of outliers
df_filled = df.copy()
numerical_cols = ["Training_Hours", "Score"]
for col in numerical_cols:
median_value = df_filled[col].median()
********** 4 **********
--- page 5 ---
df_filled[col].fillna(median_value, inplace=True)
print("\nDataFrame after filling missing values:\n", df_filled)
Or
# Create dataset
print("Original Data Frame:")
print(df)
# 1. Median Experience of Fin Dept
median_exp_fin <- median(df$Experience[df$Dept == "Fin"])
print(paste("Median Experience of Fin Dept:", median_exp_fin))
# 2. Average Bonus of HR Dept
avg_bonus_hr <- mean(df$Bonus[df$Dept == "HR"])
print(paste("Average Bonus of HR Dept:", avg_bonus_hr))
# 3. Fill NA values (using median)
# Justification: Median avoids outlier influence
df_filled <- df
numeric_cols <- c("Training_Hours", "Score")
for (col in numeric_cols) {
med <- median(df_filled[[col]], na.rm = TRUE)
df_filled[[col]][is.na(df_filled[[col]])] <- med
}
print("Data Frame after filling NA values:")
print(df_filled)
CO-3 ; B # 1. Create a vector v1 with EVEN numbers from 500 to 300   [10]
BL-3   v1 <- seq(500, 300, by = -2) # Descending order initially
print("v1 (descending):")
print(v1)
# 2. Arrange the numbers in ascending order
v1 <- sort(v1) # Sort in ascending order
print("v1 (ascending):")
print(v1)
# 3. Total number of elements in v1
total_elements <- length(v1)
print(paste("Total number of elements in v1:", total_elements))
# 4. Check the dimension of v1
dim_v1 <- dim(v1)
# For a vector, dim() is NULL; vectors are 1-dimensional
print("Dimension of v1:")
print(dim_v1)
# 5. Find the index of number 450
index_450 <- which(v1 == 450)
print(paste("Index of number 450 in v1:", index_450))
OR
# 1. Create a list LIS1 with EVEN numbers from 500 to 300
LIS1 = list(range(500, 299, -2)) # Descending order
print("LIS1 (descending):", LIS1)
# 2. Arrange the numbers in ascending order
LIS1.sort()
print("LIS1 (ascending):", LIS1)
# 3. Total number of elements in LIS1
total_elements = len(LIS1)
print("Total number of elements in LIS1:", total_elements)
# 4. Check the dimension of LIS1
# Lists in Python are 1-dimensional
dimension = 1 # By default
print("Dimension of LIS1:", dimension)
********** 5 **********
--- page 6 ---
# 5. Check the index of number 450
index_450 = LIS1.index(450)
print("Index of number 450 in LIS1:", index_450)
Q4   [20]
CO-2 ;   a.   1. Data Profiling – Analyzes data to identify patterns, inconsistencies, and   [5]
BL-2   anomalies.
2. Data Cleansing – Detects and corrects errors such as duplicates, missing values,
or incorrect formats.
3. Data Standardization – Ensures consistency in data formats, units, naming
conventions, and codes.
4. Data Validation – Checks data against defined rules or constraints to ensure
accuracy and completeness.
5. Monitoring and Reporting – Tracks data quality over time and generates reports
for corrective action.
CO-3 ;   b.   1. Data Cleaning – Removes errors, duplicates, or irrelevant data before loading.   [5]
BL-2   2. Data Integration – Combines data from multiple sources into a unified format.
3. Data Aggregation – Summarizes data, e.g., total sales per month or per region.
4. Data Conversion – Converts data types, formats, or units to match target schema.
5. Data Enrichment – Enhances data by adding derived values, calculated fields, or
external information.
CO-2 ;   c.   1. Definition/Role of Metadata – Metadata is “data about data” that describes   [10]
BL-3   structure, meaning, source, and usage of data in the warehouse. It helps in
understanding, managing, and using data efficiently.
Types of Metadata:
2. Business Metadata – Describes meaning of data in business terms (e.g.,
“Customer_ID represents unique customer”).
3. Technical Metadata – Contains technical details about data storage, tables,
columns, data types, and ETL mappings.
4. Operational Metadata – Provides information on data lineage, refresh schedules,
load timings, and ETL process logs.
How Metadata Supports ETL:
5. Guides ETL tools on source-target mapping, transformation rules, and validation.
6. Tracks data lineage to trace back errors to source systems.
7. Ensures consistent and accurate transformations.
How Metadata Supports Decision-Making:
8. Helps business users understand the context and meaning of data.
9. Ensures confidence in reports and analytics by providing source and
transformation information.
10. Enables impact analysis when schema or data changes occur.
Q5   [20]
CO-2 ;   a.   1. Unit Testing – Test individual ETL components or transformations.   [5]
BL-2   2. System Testing – Test the complete end-to-end ETL process.
3. Data Integration Testing – Verify data from multiple sources is correctly
combined.
4. User Acceptance Testing (UAT) – Business users validate reports and dashboards.
5. Regression Testing – Ensure changes do not break existing functionality.
CO-3 ;   b.   1. Initial Load – Extract complete dataset from source systems and load into the data   [5]
BL-2   warehouse.
2. Data Validation – Check for consistency, integrity, and correctness before loading.
3. Incremental Updates – Apply new or modified records based on primary keys or
unique identifiers.
********** 6 **********
--- page 7 ---
4. Data Maintenance – Handle updates, corrections, and deletions in the warehouse
to reflect source changes.
5. Backup and Audit – Maintain history logs, backup data, and audit trails for
accuracy and compliance.
CO-   c.   1. Problem Definition – Understand business objective: predict which customers   [10]
1 ;BL-   will make repeat purchases. Identify success criteria and KPIs.
3   2. Data Collection – Gather data from e-commerce sources: transaction history,
customer profiles, website interactions, product data.
3. Data Cleaning and Preprocessing – Handle missing values, remove duplicates,
standardize formats, and engineer features like purchase frequency or recency.
4. Exploratory Data Analysis (EDA) – Analyze patterns, correlations, and trends in
the data. Visualize customer behavior and purchase patterns.
5. Feature Engineering – Create meaningful features to improve model performance,
e.g., average purchase value, days since last purchase
6. Model Selection – Choose appropriate predictive models (e.g., logistic regression,
decision trees, random forest, or gradient boosting).
7. Model Training and Evaluation – Split data into training and test sets. Train model
and evaluate performance using metrics like accuracy, precision, recall, or ROC-
AUC.
8. Model Tuning and Optimization – Adjust hyperparameters, perform cross-
validation, and improve prediction accuracy.
9. Deployment – Implement the model in production to predict repeat purchases for
new customers.
10. Monitoring and Maintenance – Continuously monitor model performance, update
with new data, and retrain periodically to ensure accuracy.
Q 6   [20]
CO-3 ;   a.   1. Batch Transfer – Move data at scheduled intervals from the warehouse to near-   [10]
BL-3   line storage.
2. Incremental Loading – Transfer only new or updated records to reduce processing
time.
3. Data Archiving – Automatically archive historical data to near-line storage for
cost efficiency.
4. Data Compression – Compress data before transfer to save storage and bandwidth.
5. Data Partitioning – Split large datasets into manageable segments for easier
migration.
6. Automated ETL Jobs – Use ETL workflows to orchestrate data movement to near-
line storage.
7. Replication / Mirroring – Maintain a near-line copy synchronized with the
warehouse.
8. Data Retention Policies – Define rules for how long data stays in the warehouse
before moving.
9. Error Handling & Logging – Monitor transfer failures and ensure reliable
dataflow.
10. Access Control – Secure sensitive data during transfer and storage in near-line
systems.
CO-2 ;   b. Front-Room (Presentation Layer)   [10]
BL-2
1. Query & Reporting Tools – Enable users to access, analyze, and generate reports.
2. OLAP Tools – Provide multidimensional analysis and dashboards.
3. Data Mining Tools – Support predictive analytics and pattern discovery.
4. End-User Interface – Web portals, dashboards, or BI tools for business users.
5. Metadata Access – Provides business definitions and context for users.
Back-Room (Data Storage & ETL Layer)
********** 7 **********
--- page 8 ---
1. Source Systems – Operational databases, ERP, CRM, and external data sources.
2. ETL/ELT Processes – Extract, transform, and load data into the warehouse.
3. Data Staging Area – Temporary storage for cleaning, transformation, and
integration.
4. Data Warehouse Storage – Central repository for structured and historical data.
5. Metadata Repository – Stores technical, business, and operational metadata for
ETL and user access.
Q 7   [20]
CO-2 ;   a.   1. Subject-Oriented – Data is organized around key subjects such as customers,   [10]
BL-2   products, or sales rather than specific applications. This allows for easier analysis
of business processes.
2. Integrated – Combines data from multiple heterogeneous sources (databases, flat
files, external data) into a consistent format with standardized naming
conventions, units, and encoding.
3. Time-Variant – Historical data is maintained to allow analysis over different
periods (daily, monthly, yearly). Each record is associated with a time element to
track changes.
4. Non-Volatile / Read-Only – Once data is loaded into the warehouse, it is not
frequently updated or deleted. This ensures data stability for analysis and
reporting.
5. Accessible / Query-Oriented – Optimized for complex queries, reporting, and
analytical processing rather than transactional processing.
6. Support for Decision-Making – Enables business intelligence, trend analysis, and
strategic decision-making by providing accurate, consistent, and consolidated
data.
7. Metadata-Driven – Metadata provides information about data sources, definitions,
transformations, and usage, which helps users understand and trust the data.
CO-3 ;   b.   1. Type 0: Retain Original – Values never change; history preserved.   [10]
BL-3   2. Type 1: Overwrite – Update value in-place; history lost.
3. Type 2: Add New Row – Insert new row; old row retained with versioning.
4. Type 3: Add New Column – Store previous value in a separate column.
5. Type 4: Historical Table – Maintain separate table for historical data.
6. Type 6: Hybrid – Combines Types 1, 2, 3 for full and partial history.
7. Update Strategy: Compare source and dimension, insert/update according to SCD
type, use surrogate keys and dates for tracking.
8. Significance: Preserves historical accuracy, supports trend analysis, ensures
reliable reporting, and maintains data integrity.
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper a7bf272af70e

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_DS_7009/Data Wrangling/ANS_Data Wrangling(702DB0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (DS)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO- 1;   a.   1. Structured data is highly organized in tables with rows and columns and can be   [5]
BL-2   easily stored and queried using relational databases (example: SQL databases,
Excel sheets).
2. Semi-structured data does not follow strict tabular structure but uses tags or
markers to separate elements (example: JSON, XML, CSV with variable fields).
3. Unstructured data has no predefined format or model and is difficult to store and
analyze directly (example: text documents, images, audio, video, emails).
4. Structured data is easiest to search and analyze, semi-structured provides
flexibility with some structure, while unstructured offers the most flexibility but
requires complex tools.
5. Structured data fits SQL databases, semi-structured fits NoSQL systems, and
unstructured often requires big data tools, AI, or text mining for analysis.
CO-2 ;   b.   1. Data warehouses store sensitive historical and business-critical information, so   [5]
BL-3   security protects it from unauthorized access.
2. Security measures maintain data integrity by preventing unauthorized changes that
might lead to false analytics.
3. Legal and regulatory compliance (such as GDPR, HIPAA) requires strong security
controls to protect personal and financial data.
4. Security mechanisms like encryption, access control, and monitoring defend
against data breaches and insider threats.
5. Secure data warehouses build trust, ensure reliable decision-making, and support
business continuity.
********** 1 **********
--- page 2 ---
c.   1. Human errors such as spelling mistakes or inconsistent formats can make data   [5]
inaccurate.
2. Duplicate records occur when the same entry is added multiple times from
different sources.
3. Missing or incomplete data leads to gaps that affect accurate analysis.
4. Outdated information, such as old addresses or prices, reduces the reliability of
reports.
5. Data integration from multiple sources with different formats or rules causes
inconsistencies.
Impact: Dirty data results in incorrect reports, poor business decisions, reduced
customer satisfaction, wasted time and money, and loss of trust in the
organization’s data.
d.   1. Data granularity refers to the level of detail or depth of data stored in a system.   [5]
2. High granularity means very detailed data, such as each transaction or each
customer action.
3. Low granularity means summarized or aggregated data, such as daily or monthly
totals.
4. High granularity provides flexibility and deeper analysis but requires more storage
and processing time.
5. Choosing the right granularity is crucial in data warehousing because it affects
storage, performance, and the quality of insights.
Q2   [20]
CO-   a. # 1. Create a list and multiply each element by 10   [10]
2 ;BL-   numbers = [1, 2, 3, 4, 5]
3   multiplied = [num * 10 for num in numbers]
print("After multiplying by 10:", multiplied)
# 2. Filter numbers greater than a certain value
threshold = 3
filtered = [num for num in numbers if num > threshold]
print("Numbers greater than", threshold, ":", filtered)
# 3. Calculate the sum of all numbers
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)
# 4. Find the mode (most frequent number)
from statistics import mode
numbers_with_duplicates = [2, 3, 2, 5, 4, 2, 3]
most_frequent = mode(numbers_with_duplicates)
• print("Mode of the list:", most_frequent)
OUTPUT:
First print: each element multiplied by 10 → [10, 20, 30, 40, 50]
Second print: numbers > 3 → [4, 5]
Third print: sum of numbers → 15
Fourth print: most frequent number in [2,3,2,5,4,2,3] → 2
R Codes:
# 1. Create a vector and multiply each element by 10
numbers <- c(1, 2, 3, 4, 5)
********** 2 **********
--- page 3 ---
multiplied <- numbers * 10
print(multiplied)
# 2. Filter numbers greater than a certain value
threshold <- 3
filtered <- numbers[numbers > threshold]
print(filtered)
# 3. Calculate the sum of all numbers
total_sum <- sum(numbers)
print(total_sum)
# 4. Find the mode (most frequent number)
numbers_with_duplicates <- c(2, 3, 2, 5, 4, 2, 3)
mode_value <- as.numeric(names(sort(table(numbers_with_duplicates), decreasing
= TRUE)[1]))
print(mode_value)
•   First print: [10 20 30 40 50]
• Second print: [4 5]
• Third print: 15
• Fourth print: 2 (most frequent number)
b. import numpy as np   [10]
CO-
3 ;BL-   # 1. Create two 2x2 matrices A and B
A = np.array([[1, 2],
3   [3, 4]])
B = np.array([[5, 6],
[7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
# 2. Addition (A + B)
add_result = A + B
print("\nA + B:\n", add_result)
# 2. Matrix Multiplication (A * B)
mult_result = A.dot(B)
print("\nA x B:\n", mult_result)
# 3. Extract element in second row, first column
print("\nElement A[2,1]:", A[1, 0])
print("Element B[2,1]:", B[1, 0])
# 4. Replace main diagonal with 0
A_diag_zero = A.copy()
B_diag_zero = B.copy()
np.fill_diagonal(A_diag_zero, 0)
np.fill_diagonal(B_diag_zero, 0)
print("\nA with diagonal 0:\n", A_diag_zero)
print("\nB with diagonal 0:\n", B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 = A + 5
B1 = B + 5
print("\nA1 (A + 5):\n", A1)
• print("\nB1 (B + 5):\n", B1)
R:
********** 3 **********
--- page 4 ---
# 1. Create two 2x2 matrices A and B
A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)
B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
# 2. Addition (A + B)
add_result <- A + B
print("A + B:")
print(add_result)
# 2. Matrix multiplication
mult_result <- A %*% B
print("A x B:")
print(mult_result)
# 3. Extract element in second row, first column
print(paste("Element A[2,1]:", A[2,1]))
print(paste("Element B[2,1]:", B[2,1]))
# 4. Replace main diagonal with 0
A_diag_zero <- A
B_diag_zero <- B
diag(A_diag_zero) <- 0
diag(B_diag_zero) <- 0
print("A with diagonal 0:")
print(A_diag_zero)
print("B with diagonal 0:")
print(B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 <- A + 5
B1 <- B + 5
print("A1 (A + 5):")
print(A1)
print("B1 (B + 5):")
print(B1)
Q3   [20]
CO-2 ;   a. import pandas as pd   [10]
BL-3   import numpy as np
# Create dataset
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# 1. Median Experience of Fin Dept
median_exp_fin = df[df["Dept"] == "Fin"]["Experience"].median()
print("\nMedian Experience of Fin Dept:", median_exp_fin)
# 2. Average Bonus of HR Dept
avg_bonus_hr = df[df["Dept"] == "HR"]["Bonus"].mean()
print("Average Bonus of HR Dept:", avg_bonus_hr)
# 3. Fill NaN values
# Justification: Using median for numeric fields to reduce the impact of outliers
df_filled = df.copy()
numerical_cols = ["Training_Hours", "Score"]
for col in numerical_cols:
median_value = df_filled[col].median()
********** 4 **********
--- page 5 ---
df_filled[col].fillna(median_value, inplace=True)
print("\nDataFrame after filling missing values:\n", df_filled)
Or
# Create dataset
print("Original Data Frame:")
print(df)
# 1. Median Experience of Fin Dept
median_exp_fin <- median(df$Experience[df$Dept == "Fin"])
print(paste("Median Experience of Fin Dept:", median_exp_fin))
# 2. Average Bonus of HR Dept
avg_bonus_hr <- mean(df$Bonus[df$Dept == "HR"])
print(paste("Average Bonus of HR Dept:", avg_bonus_hr))
# 3. Fill NA values (using median)
# Justification: Median avoids outlier influence
df_filled <- df
numeric_cols <- c("Training_Hours", "Score")
for (col in numeric_cols) {
med <- median(df_filled[[col]], na.rm = TRUE)
df_filled[[col]][is.na(df_filled[[col]])] <- med
}
print("Data Frame after filling NA values:")
print(df_filled)
CO-3 ; B # 1. Create a vector v1 with EVEN numbers from 500 to 300   [10]
BL-3   v1 <- seq(500, 300, by = -2) # Descending order initially
print("v1 (descending):")
print(v1)
# 2. Arrange the numbers in ascending order
v1 <- sort(v1) # Sort in ascending order
print("v1 (ascending):")
print(v1)
# 3. Total number of elements in v1
total_elements <- length(v1)
print(paste("Total number of elements in v1:", total_elements))
# 4. Check the dimension of v1
dim_v1 <- dim(v1)
# For a vector, dim() is NULL; vectors are 1-dimensional
print("Dimension of v1:")
print(dim_v1)
# 5. Find the index of number 450
index_450 <- which(v1 == 450)
print(paste("Index of number 450 in v1:", index_450))
OR
# 1. Create a list LIS1 with EVEN numbers from 500 to 300
LIS1 = list(range(500, 299, -2)) # Descending order
print("LIS1 (descending):", LIS1)
# 2. Arrange the numbers in ascending order
LIS1.sort()
print("LIS1 (ascending):", LIS1)
# 3. Total number of elements in LIS1
total_elements = len(LIS1)
print("Total number of elements in LIS1:", total_elements)
# 4. Check the dimension of LIS1
# Lists in Python are 1-dimensional
dimension = 1 # By default
print("Dimension of LIS1:", dimension)
********** 5 **********
--- page 6 ---
# 5. Check the index of number 450
index_450 = LIS1.index(450)
print("Index of number 450 in LIS1:", index_450)
Q4   [20]
CO-2 ;   a.   1. Data Profiling – Analyzes data to identify patterns, inconsistencies, and   [5]
BL-2   anomalies.
2. Data Cleansing – Detects and corrects errors such as duplicates, missing values,
or incorrect formats.
3. Data Standardization – Ensures consistency in data formats, units, naming
conventions, and codes.
4. Data Validation – Checks data against defined rules or constraints to ensure
accuracy and completeness.
5. Monitoring and Reporting – Tracks data quality over time and generates reports
for corrective action.
CO-3 ;   b.   1. Data Cleaning – Removes errors, duplicates, or irrelevant data before loading.   [5]
BL-2   2. Data Integration – Combines data from multiple sources into a unified format.
3. Data Aggregation – Summarizes data, e.g., total sales per month or per region.
4. Data Conversion – Converts data types, formats, or units to match target schema.
5. Data Enrichment – Enhances data by adding derived values, calculated fields, or
external information.
CO-2 ;   c.   1. Definition/Role of Metadata – Metadata is “data about data” that describes   [10]
BL-3   structure, meaning, source, and usage of data in the warehouse. It helps in
understanding, managing, and using data efficiently.
Types of Metadata:
2. Business Metadata – Describes meaning of data in business terms (e.g.,
“Customer_ID represents unique customer”).
3. Technical Metadata – Contains technical details about data storage, tables,
columns, data types, and ETL mappings.
4. Operational Metadata – Provides information on data lineage, refresh schedules,
load timings, and ETL process logs.
How Metadata Supports ETL:
5. Guides ETL tools on source-target mapping, transformation rules, and validation.
6. Tracks data lineage to trace back errors to source systems.
7. Ensures consistent and accurate transformations.
How Metadata Supports Decision-Making:
8. Helps business users understand the context and meaning of data.
9. Ensures confidence in reports and analytics by providing source and
transformation information.
10. Enables impact analysis when schema or data changes occur.
Q5   [20]
CO-2 ;   a.   1. Unit Testing – Test individual ETL components or transformations.   [5]
BL-2   2. System Testing – Test the complete end-to-end ETL process.
3. Data Integration Testing – Verify data from multiple sources is correctly
combined.
4. User Acceptance Testing (UAT) – Business users validate reports and dashboards.
5. Regression Testing – Ensure changes do not break existing functionality.
CO-3 ;   b.   1. Initial Load – Extract complete dataset from source systems and load into the data   [5]
BL-2   warehouse.
2. Data Validation – Check for consistency, integrity, and correctness before loading.
3. Incremental Updates – Apply new or modified records based on primary keys or
unique identifiers.
********** 6 **********
--- page 7 ---
4. Data Maintenance – Handle updates, corrections, and deletions in the warehouse
to reflect source changes.
5. Backup and Audit – Maintain history logs, backup data, and audit trails for
accuracy and compliance.
CO-   c.   1. Problem Definition – Understand business objective: predict which customers   [10]
1 ;BL-   will make repeat purchases. Identify success criteria and KPIs.
3   2. Data Collection – Gather data from e-commerce sources: transaction history,
customer profiles, website interactions, product data.
3. Data Cleaning and Preprocessing – Handle missing values, remove duplicates,
standardize formats, and engineer features like purchase frequency or recency.
4. Exploratory Data Analysis (EDA) – Analyze patterns, correlations, and trends in
the data. Visualize customer behavior and purchase patterns.
5. Feature Engineering – Create meaningful features to improve model performance,
e.g., average purchase value, days since last purchase
6. Model Selection – Choose appropriate predictive models (e.g., logistic regression,
decision trees, random forest, or gradient boosting).
7. Model Training and Evaluation – Split data into training and test sets. Train model
and evaluate performance using metrics like accuracy, precision, recall, or ROC-
AUC.
8. Model Tuning and Optimization – Adjust hyperparameters, perform cross-
validation, and improve prediction accuracy.
9. Deployment – Implement the model in production to predict repeat purchases for
new customers.
10. Monitoring and Maintenance – Continuously monitor model performance, update
with new data, and retrain periodically to ensure accuracy.
Q 6   [20]
CO-3 ;   a.   1. Batch Transfer – Move data at scheduled intervals from the warehouse to near-   [10]
BL-3   line storage.
2. Incremental Loading – Transfer only new or updated records to reduce processing
time.
3. Data Archiving – Automatically archive historical data to near-line storage for
cost efficiency.
4. Data Compression – Compress data before transfer to save storage and bandwidth.
5. Data Partitioning – Split large datasets into manageable segments for easier
migration.
6. Automated ETL Jobs – Use ETL workflows to orchestrate data movement to near-
line storage.
7. Replication / Mirroring – Maintain a near-line copy synchronized with the
warehouse.
8. Data Retention Policies – Define rules for how long data stays in the warehouse
before moving.
9. Error Handling & Logging – Monitor transfer failures and ensure reliable
dataflow.
10. Access Control – Secure sensitive data during transfer and storage in near-line
systems.
CO-2 ;   b. Front-Room (Presentation Layer)   [10]
BL-2
1. Query & Reporting Tools – Enable users to access, analyze, and generate reports.
2. OLAP Tools – Provide multidimensional analysis and dashboards.
3. Data Mining Tools – Support predictive analytics and pattern discovery.
4. End-User Interface – Web portals, dashboards, or BI tools for business users.
5. Metadata Access – Provides business definitions and context for users.
Back-Room (Data Storage & ETL Layer)
********** 7 **********
--- page 8 ---
1. Source Systems – Operational databases, ERP, CRM, and external data sources.
2. ETL/ELT Processes – Extract, transform, and load data into the warehouse.
3. Data Staging Area – Temporary storage for cleaning, transformation, and
integration.
4. Data Warehouse Storage – Central repository for structured and historical data.
5. Metadata Repository – Stores technical, business, and operational metadata for
ETL and user access.
Q 7   [20]
CO-2 ;   a.   1. Subject-Oriented – Data is organized around key subjects such as customers,   [10]
BL-2   products, or sales rather than specific applications. This allows for easier analysis
of business processes.
2. Integrated – Combines data from multiple heterogeneous sources (databases, flat
files, external data) into a consistent format with standardized naming
conventions, units, and encoding.
3. Time-Variant – Historical data is maintained to allow analysis over different
periods (daily, monthly, yearly). Each record is associated with a time element to
track changes.
4. Non-Volatile / Read-Only – Once data is loaded into the warehouse, it is not
frequently updated or deleted. This ensures data stability for analysis and
reporting.
5. Accessible / Query-Oriented – Optimized for complex queries, reporting, and
analytical processing rather than transactional processing.
6. Support for Decision-Making – Enables business intelligence, trend analysis, and
strategic decision-making by providing accurate, consistent, and consolidated
data.
7. Metadata-Driven – Metadata provides information about data sources, definitions,
transformations, and usage, which helps users understand and trust the data.
CO-3 ;   b.   1. Type 0: Retain Original – Values never change; history preserved.   [10]
BL-3   2. Type 1: Overwrite – Update value in-place; history lost.
3. Type 2: Add New Row – Insert new row; old row retained with versioning.
4. Type 3: Add New Column – Store previous value in a separate column.
5. Type 4: Historical Table – Maintain separate table for historical data.
6. Type 6: Hybrid – Combines Types 1, 2, 3 for full and partial history.
7. Update Strategy: Compare source and dimension, insert/update according to SCD
type, use surrogate keys and dates for tracking.
8. Significance: Preserves historical accuracy, supports trend analysis, ensures
reliable reporting, and maintains data integrity.
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 000942f3fc77

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_DS_7052/Data Wrangling/ANS_Data Wrangling(702DB0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (DS)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO- 1;   a.   1. Structured data is highly organized in tables with rows and columns and can be   [5]
BL-2   easily stored and queried using relational databases (example: SQL databases,
Excel sheets).
2. Semi-structured data does not follow strict tabular structure but uses tags or
markers to separate elements (example: JSON, XML, CSV with variable fields).
3. Unstructured data has no predefined format or model and is difficult to store and
analyze directly (example: text documents, images, audio, video, emails).
4. Structured data is easiest to search and analyze, semi-structured provides
flexibility with some structure, while unstructured offers the most flexibility but
requires complex tools.
5. Structured data fits SQL databases, semi-structured fits NoSQL systems, and
unstructured often requires big data tools, AI, or text mining for analysis.
CO-2 ;   b.   1. Data warehouses store sensitive historical and business-critical information, so   [5]
BL-3   security protects it from unauthorized access.
2. Security measures maintain data integrity by preventing unauthorized changes that
might lead to false analytics.
3. Legal and regulatory compliance (such as GDPR, HIPAA) requires strong security
controls to protect personal and financial data.
4. Security mechanisms like encryption, access control, and monitoring defend
against data breaches and insider threats.
5. Secure data warehouses build trust, ensure reliable decision-making, and support
business continuity.
********** 1 **********
--- page 2 ---
c.   1. Human errors such as spelling mistakes or inconsistent formats can make data   [5]
inaccurate.
2. Duplicate records occur when the same entry is added multiple times from
different sources.
3. Missing or incomplete data leads to gaps that affect accurate analysis.
4. Outdated information, such as old addresses or prices, reduces the reliability of
reports.
5. Data integration from multiple sources with different formats or rules causes
inconsistencies.
Impact: Dirty data results in incorrect reports, poor business decisions, reduced
customer satisfaction, wasted time and money, and loss of trust in the
organization’s data.
d.   1. Data granularity refers to the level of detail or depth of data stored in a system.   [5]
2. High granularity means very detailed data, such as each transaction or each
customer action.
3. Low granularity means summarized or aggregated data, such as daily or monthly
totals.
4. High granularity provides flexibility and deeper analysis but requires more storage
and processing time.
5. Choosing the right granularity is crucial in data warehousing because it affects
storage, performance, and the quality of insights.
Q2   [20]
CO-   a. # 1. Create a list and multiply each element by 10   [10]
2 ;BL-   numbers = [1, 2, 3, 4, 5]
3   multiplied = [num * 10 for num in numbers]
print("After multiplying by 10:", multiplied)
# 2. Filter numbers greater than a certain value
threshold = 3
filtered = [num for num in numbers if num > threshold]
print("Numbers greater than", threshold, ":", filtered)
# 3. Calculate the sum of all numbers
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)
# 4. Find the mode (most frequent number)
from statistics import mode
numbers_with_duplicates = [2, 3, 2, 5, 4, 2, 3]
most_frequent = mode(numbers_with_duplicates)
• print("Mode of the list:", most_frequent)
OUTPUT:
First print: each element multiplied by 10 → [10, 20, 30, 40, 50]
Second print: numbers > 3 → [4, 5]
Third print: sum of numbers → 15
Fourth print: most frequent number in [2,3,2,5,4,2,3] → 2
R Codes:
# 1. Create a vector and multiply each element by 10
numbers <- c(1, 2, 3, 4, 5)
********** 2 **********
--- page 3 ---
multiplied <- numbers * 10
print(multiplied)
# 2. Filter numbers greater than a certain value
threshold <- 3
filtered <- numbers[numbers > threshold]
print(filtered)
# 3. Calculate the sum of all numbers
total_sum <- sum(numbers)
print(total_sum)
# 4. Find the mode (most frequent number)
numbers_with_duplicates <- c(2, 3, 2, 5, 4, 2, 3)
mode_value <- as.numeric(names(sort(table(numbers_with_duplicates), decreasing
= TRUE)[1]))
print(mode_value)
•   First print: [10 20 30 40 50]
• Second print: [4 5]
• Third print: 15
• Fourth print: 2 (most frequent number)
b. import numpy as np   [10]
CO-
3 ;BL-   # 1. Create two 2x2 matrices A and B
A = np.array([[1, 2],
3   [3, 4]])
B = np.array([[5, 6],
[7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
# 2. Addition (A + B)
add_result = A + B
print("\nA + B:\n", add_result)
# 2. Matrix Multiplication (A * B)
mult_result = A.dot(B)
print("\nA x B:\n", mult_result)
# 3. Extract element in second row, first column
print("\nElement A[2,1]:", A[1, 0])
print("Element B[2,1]:", B[1, 0])
# 4. Replace main diagonal with 0
A_diag_zero = A.copy()
B_diag_zero = B.copy()
np.fill_diagonal(A_diag_zero, 0)
np.fill_diagonal(B_diag_zero, 0)
print("\nA with diagonal 0:\n", A_diag_zero)
print("\nB with diagonal 0:\n", B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 = A + 5
B1 = B + 5
print("\nA1 (A + 5):\n", A1)
• print("\nB1 (B + 5):\n", B1)
R:
********** 3 **********
--- page 4 ---
# 1. Create two 2x2 matrices A and B
A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)
B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
# 2. Addition (A + B)
add_result <- A + B
print("A + B:")
print(add_result)
# 2. Matrix multiplication
mult_result <- A %*% B
print("A x B:")
print(mult_result)
# 3. Extract element in second row, first column
print(paste("Element A[2,1]:", A[2,1]))
print(paste("Element B[2,1]:", B[2,1]))
# 4. Replace main diagonal with 0
A_diag_zero <- A
B_diag_zero <- B
diag(A_diag_zero) <- 0
diag(B_diag_zero) <- 0
print("A with diagonal 0:")
print(A_diag_zero)
print("B with diagonal 0:")
print(B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 <- A + 5
B1 <- B + 5
print("A1 (A + 5):")
print(A1)
print("B1 (B + 5):")
print(B1)
Q3   [20]
CO-2 ;   a. import pandas as pd   [10]
BL-3   import numpy as np
# Create dataset
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# 1. Median Experience of Fin Dept
median_exp_fin = df[df["Dept"] == "Fin"]["Experience"].median()
print("\nMedian Experience of Fin Dept:", median_exp_fin)
# 2. Average Bonus of HR Dept
avg_bonus_hr = df[df["Dept"] == "HR"]["Bonus"].mean()
print("Average Bonus of HR Dept:", avg_bonus_hr)
# 3. Fill NaN values
# Justification: Using median for numeric fields to reduce the impact of outliers
df_filled = df.copy()
numerical_cols = ["Training_Hours", "Score"]
for col in numerical_cols:
median_value = df_filled[col].median()
********** 4 **********
--- page 5 ---
df_filled[col].fillna(median_value, inplace=True)
print("\nDataFrame after filling missing values:\n", df_filled)
Or
# Create dataset
print("Original Data Frame:")
print(df)
# 1. Median Experience of Fin Dept
median_exp_fin <- median(df$Experience[df$Dept == "Fin"])
print(paste("Median Experience of Fin Dept:", median_exp_fin))
# 2. Average Bonus of HR Dept
avg_bonus_hr <- mean(df$Bonus[df$Dept == "HR"])
print(paste("Average Bonus of HR Dept:", avg_bonus_hr))
# 3. Fill NA values (using median)
# Justification: Median avoids outlier influence
df_filled <- df
numeric_cols <- c("Training_Hours", "Score")
for (col in numeric_cols) {
med <- median(df_filled[[col]], na.rm = TRUE)
df_filled[[col]][is.na(df_filled[[col]])] <- med
}
print("Data Frame after filling NA values:")
print(df_filled)
CO-3 ; B # 1. Create a vector v1 with EVEN numbers from 500 to 300   [10]
BL-3   v1 <- seq(500, 300, by = -2) # Descending order initially
print("v1 (descending):")
print(v1)
# 2. Arrange the numbers in ascending order
v1 <- sort(v1) # Sort in ascending order
print("v1 (ascending):")
print(v1)
# 3. Total number of elements in v1
total_elements <- length(v1)
print(paste("Total number of elements in v1:", total_elements))
# 4. Check the dimension of v1
dim_v1 <- dim(v1)
# For a vector, dim() is NULL; vectors are 1-dimensional
print("Dimension of v1:")
print(dim_v1)
# 5. Find the index of number 450
index_450 <- which(v1 == 450)
print(paste("Index of number 450 in v1:", index_450))
OR
# 1. Create a list LIS1 with EVEN numbers from 500 to 300
LIS1 = list(range(500, 299, -2)) # Descending order
print("LIS1 (descending):", LIS1)
# 2. Arrange the numbers in ascending order
LIS1.sort()
print("LIS1 (ascending):", LIS1)
# 3. Total number of elements in LIS1
total_elements = len(LIS1)
print("Total number of elements in LIS1:", total_elements)
# 4. Check the dimension of LIS1
# Lists in Python are 1-dimensional
dimension = 1 # By default
print("Dimension of LIS1:", dimension)
********** 5 **********
--- page 6 ---
# 5. Check the index of number 450
index_450 = LIS1.index(450)
print("Index of number 450 in LIS1:", index_450)
Q4   [20]
CO-2 ;   a.   1. Data Profiling – Analyzes data to identify patterns, inconsistencies, and   [5]
BL-2   anomalies.
2. Data Cleansing – Detects and corrects errors such as duplicates, missing values,
or incorrect formats.
3. Data Standardization – Ensures consistency in data formats, units, naming
conventions, and codes.
4. Data Validation – Checks data against defined rules or constraints to ensure
accuracy and completeness.
5. Monitoring and Reporting – Tracks data quality over time and generates reports
for corrective action.
CO-3 ;   b.   1. Data Cleaning – Removes errors, duplicates, or irrelevant data before loading.   [5]
BL-2   2. Data Integration – Combines data from multiple sources into a unified format.
3. Data Aggregation – Summarizes data, e.g., total sales per month or per region.
4. Data Conversion – Converts data types, formats, or units to match target schema.
5. Data Enrichment – Enhances data by adding derived values, calculated fields, or
external information.
CO-2 ;   c.   1. Definition/Role of Metadata – Metadata is “data about data” that describes   [10]
BL-3   structure, meaning, source, and usage of data in the warehouse. It helps in
understanding, managing, and using data efficiently.
Types of Metadata:
2. Business Metadata – Describes meaning of data in business terms (e.g.,
“Customer_ID represents unique customer”).
3. Technical Metadata – Contains technical details about data storage, tables,
columns, data types, and ETL mappings.
4. Operational Metadata – Provides information on data lineage, refresh schedules,
load timings, and ETL process logs.
How Metadata Supports ETL:
5. Guides ETL tools on source-target mapping, transformation rules, and validation.
6. Tracks data lineage to trace back errors to source systems.
7. Ensures consistent and accurate transformations.
How Metadata Supports Decision-Making:
8. Helps business users understand the context and meaning of data.
9. Ensures confidence in reports and analytics by providing source and
transformation information.
10. Enables impact analysis when schema or data changes occur.
Q5   [20]
CO-2 ;   a.   1. Unit Testing – Test individual ETL components or transformations.   [5]
BL-2   2. System Testing – Test the complete end-to-end ETL process.
3. Data Integration Testing – Verify data from multiple sources is correctly
combined.
4. User Acceptance Testing (UAT) – Business users validate reports and dashboards.
5. Regression Testing – Ensure changes do not break existing functionality.
CO-3 ;   b.   1. Initial Load – Extract complete dataset from source systems and load into the data   [5]
BL-2   warehouse.
2. Data Validation – Check for consistency, integrity, and correctness before loading.
3. Incremental Updates – Apply new or modified records based on primary keys or
unique identifiers.
********** 6 **********
--- page 7 ---
4. Data Maintenance – Handle updates, corrections, and deletions in the warehouse
to reflect source changes.
5. Backup and Audit – Maintain history logs, backup data, and audit trails for
accuracy and compliance.
CO-   c.   1. Problem Definition – Understand business objective: predict which customers   [10]
1 ;BL-   will make repeat purchases. Identify success criteria and KPIs.
3   2. Data Collection – Gather data from e-commerce sources: transaction history,
customer profiles, website interactions, product data.
3. Data Cleaning and Preprocessing – Handle missing values, remove duplicates,
standardize formats, and engineer features like purchase frequency or recency.
4. Exploratory Data Analysis (EDA) – Analyze patterns, correlations, and trends in
the data. Visualize customer behavior and purchase patterns.
5. Feature Engineering – Create meaningful features to improve model performance,
e.g., average purchase value, days since last purchase
6. Model Selection – Choose appropriate predictive models (e.g., logistic regression,
decision trees, random forest, or gradient boosting).
7. Model Training and Evaluation – Split data into training and test sets. Train model
and evaluate performance using metrics like accuracy, precision, recall, or ROC-
AUC.
8. Model Tuning and Optimization – Adjust hyperparameters, perform cross-
validation, and improve prediction accuracy.
9. Deployment – Implement the model in production to predict repeat purchases for
new customers.
10. Monitoring and Maintenance – Continuously monitor model performance, update
with new data, and retrain periodically to ensure accuracy.
Q 6   [20]
CO-3 ;   a.   1. Batch Transfer – Move data at scheduled intervals from the warehouse to near-   [10]
BL-3   line storage.
2. Incremental Loading – Transfer only new or updated records to reduce processing
time.
3. Data Archiving – Automatically archive historical data to near-line storage for
cost efficiency.
4. Data Compression – Compress data before transfer to save storage and bandwidth.
5. Data Partitioning – Split large datasets into manageable segments for easier
migration.
6. Automated ETL Jobs – Use ETL workflows to orchestrate data movement to near-
line storage.
7. Replication / Mirroring – Maintain a near-line copy synchronized with the
warehouse.
8. Data Retention Policies – Define rules for how long data stays in the warehouse
before moving.
9. Error Handling & Logging – Monitor transfer failures and ensure reliable
dataflow.
10. Access Control – Secure sensitive data during transfer and storage in near-line
systems.
CO-2 ;   b. Front-Room (Presentation Layer)   [10]
BL-2
1. Query & Reporting Tools – Enable users to access, analyze, and generate reports.
2. OLAP Tools – Provide multidimensional analysis and dashboards.
3. Data Mining Tools – Support predictive analytics and pattern discovery.
4. End-User Interface – Web portals, dashboards, or BI tools for business users.
5. Metadata Access – Provides business definitions and context for users.
Back-Room (Data Storage & ETL Layer)
********** 7 **********
--- page 8 ---
1. Source Systems – Operational databases, ERP, CRM, and external data sources.
2. ETL/ELT Processes – Extract, transform, and load data into the warehouse.
3. Data Staging Area – Temporary storage for cleaning, transformation, and
integration.
4. Data Warehouse Storage – Central repository for structured and historical data.
5. Metadata Repository – Stores technical, business, and operational metadata for
ETL and user access.
Q 7   [20]
CO-2 ;   a.   1. Subject-Oriented – Data is organized around key subjects such as customers,   [10]
BL-2   products, or sales rather than specific applications. This allows for easier analysis
of business processes.
2. Integrated – Combines data from multiple heterogeneous sources (databases, flat
files, external data) into a consistent format with standardized naming
conventions, units, and encoding.
3. Time-Variant – Historical data is maintained to allow analysis over different
periods (daily, monthly, yearly). Each record is associated with a time element to
track changes.
4. Non-Volatile / Read-Only – Once data is loaded into the warehouse, it is not
frequently updated or deleted. This ensures data stability for analysis and
reporting.
5. Accessible / Query-Oriented – Optimized for complex queries, reporting, and
analytical processing rather than transactional processing.
6. Support for Decision-Making – Enables business intelligence, trend analysis, and
strategic decision-making by providing accurate, consistent, and consolidated
data.
7. Metadata-Driven – Metadata provides information about data sources, definitions,
transformations, and usage, which helps users understand and trust the data.
CO-3 ;   b.   1. Type 0: Retain Original – Values never change; history preserved.   [10]
BL-3   2. Type 1: Overwrite – Update value in-place; history lost.
3. Type 2: Add New Row – Insert new row; old row retained with versioning.
4. Type 3: Add New Column – Store previous value in a separate column.
5. Type 4: Historical Table – Maintain separate table for historical data.
6. Type 6: Hybrid – Combines Types 1, 2, 3 for full and partial history.
7. Update Strategy: Compare source and dimension, insert/update according to SCD
type, use surrogate keys and dates for tracking.
8. Significance: Preserves historical accuracy, supports trend analysis, ensures
reliable reporting, and maintains data integrity.
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper acff7f5e2e16

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AIML_7053/Data Wrangling/ANS_Data Wrangling(702DB0C012)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (DS)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO- 1;   a.   1. Structured data is highly organized in tables with rows and columns and can be   [5]
BL-2   easily stored and queried using relational databases (example: SQL databases,
Excel sheets).
2. Semi-structured data does not follow strict tabular structure but uses tags or
markers to separate elements (example: JSON, XML, CSV with variable fields).
3. Unstructured data has no predefined format or model and is difficult to store and
analyze directly (example: text documents, images, audio, video, emails).
4. Structured data is easiest to search and analyze, semi-structured provides
flexibility with some structure, while unstructured offers the most flexibility but
requires complex tools.
5. Structured data fits SQL databases, semi-structured fits NoSQL systems, and
unstructured often requires big data tools, AI, or text mining for analysis.
CO-2 ;   b.   1. Data warehouses store sensitive historical and business-critical information, so   [5]
BL-3   security protects it from unauthorized access.
2. Security measures maintain data integrity by preventing unauthorized changes that
might lead to false analytics.
3. Legal and regulatory compliance (such as GDPR, HIPAA) requires strong security
controls to protect personal and financial data.
4. Security mechanisms like encryption, access control, and monitoring defend
against data breaches and insider threats.
5. Secure data warehouses build trust, ensure reliable decision-making, and support
business continuity.
********** 1 **********
--- page 2 ---
c.   1. Human errors such as spelling mistakes or inconsistent formats can make data   [5]
inaccurate.
2. Duplicate records occur when the same entry is added multiple times from
different sources.
3. Missing or incomplete data leads to gaps that affect accurate analysis.
4. Outdated information, such as old addresses or prices, reduces the reliability of
reports.
5. Data integration from multiple sources with different formats or rules causes
inconsistencies.
Impact: Dirty data results in incorrect reports, poor business decisions, reduced
customer satisfaction, wasted time and money, and loss of trust in the
organization’s data.
d.   1. Data granularity refers to the level of detail or depth of data stored in a system.   [5]
2. High granularity means very detailed data, such as each transaction or each
customer action.
3. Low granularity means summarized or aggregated data, such as daily or monthly
totals.
4. High granularity provides flexibility and deeper analysis but requires more storage
and processing time.
5. Choosing the right granularity is crucial in data warehousing because it affects
storage, performance, and the quality of insights.
Q2   [20]
CO-   a. # 1. Create a list and multiply each element by 10   [10]
2 ;BL-   numbers = [1, 2, 3, 4, 5]
3   multiplied = [num * 10 for num in numbers]
print("After multiplying by 10:", multiplied)
# 2. Filter numbers greater than a certain value
threshold = 3
filtered = [num for num in numbers if num > threshold]
print("Numbers greater than", threshold, ":", filtered)
# 3. Calculate the sum of all numbers
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)
# 4. Find the mode (most frequent number)
from statistics import mode
numbers_with_duplicates = [2, 3, 2, 5, 4, 2, 3]
most_frequent = mode(numbers_with_duplicates)
• print("Mode of the list:", most_frequent)
OUTPUT:
First print: each element multiplied by 10 → [10, 20, 30, 40, 50]
Second print: numbers > 3 → [4, 5]
Third print: sum of numbers → 15
Fourth print: most frequent number in [2,3,2,5,4,2,3] → 2
R Codes:
# 1. Create a vector and multiply each element by 10
numbers <- c(1, 2, 3, 4, 5)
********** 2 **********
--- page 3 ---
multiplied <- numbers * 10
print(multiplied)
# 2. Filter numbers greater than a certain value
threshold <- 3
filtered <- numbers[numbers > threshold]
print(filtered)
# 3. Calculate the sum of all numbers
total_sum <- sum(numbers)
print(total_sum)
# 4. Find the mode (most frequent number)
numbers_with_duplicates <- c(2, 3, 2, 5, 4, 2, 3)
mode_value <- as.numeric(names(sort(table(numbers_with_duplicates), decreasing
= TRUE)[1]))
print(mode_value)
•   First print: [10 20 30 40 50]
• Second print: [4 5]
• Third print: 15
• Fourth print: 2 (most frequent number)
b. import numpy as np   [10]
CO-
3 ;BL-   # 1. Create two 2x2 matrices A and B
A = np.array([[1, 2],
3   [3, 4]])
B = np.array([[5, 6],
[7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
# 2. Addition (A + B)
add_result = A + B
print("\nA + B:\n", add_result)
# 2. Matrix Multiplication (A * B)
mult_result = A.dot(B)
print("\nA x B:\n", mult_result)
# 3. Extract element in second row, first column
print("\nElement A[2,1]:", A[1, 0])
print("Element B[2,1]:", B[1, 0])
# 4. Replace main diagonal with 0
A_diag_zero = A.copy()
B_diag_zero = B.copy()
np.fill_diagonal(A_diag_zero, 0)
np.fill_diagonal(B_diag_zero, 0)
print("\nA with diagonal 0:\n", A_diag_zero)
print("\nB with diagonal 0:\n", B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 = A + 5
B1 = B + 5
print("\nA1 (A + 5):\n", A1)
• print("\nB1 (B + 5):\n", B1)
R:
********** 3 **********
--- page 4 ---
# 1. Create two 2x2 matrices A and B
A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)
B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
# 2. Addition (A + B)
add_result <- A + B
print("A + B:")
print(add_result)
# 2. Matrix multiplication
mult_result <- A %*% B
print("A x B:")
print(mult_result)
# 3. Extract element in second row, first column
print(paste("Element A[2,1]:", A[2,1]))
print(paste("Element B[2,1]:", B[2,1]))
# 4. Replace main diagonal with 0
A_diag_zero <- A
B_diag_zero <- B
diag(A_diag_zero) <- 0
diag(B_diag_zero) <- 0
print("A with diagonal 0:")
print(A_diag_zero)
print("B with diagonal 0:")
print(B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 <- A + 5
B1 <- B + 5
print("A1 (A + 5):")
print(A1)
print("B1 (B + 5):")
print(B1)
Q3   [20]
CO-2 ;   a. import pandas as pd   [10]
BL-3   import numpy as np
# Create dataset
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# 1. Median Experience of Fin Dept
median_exp_fin = df[df["Dept"] == "Fin"]["Experience"].median()
print("\nMedian Experience of Fin Dept:", median_exp_fin)
# 2. Average Bonus of HR Dept
avg_bonus_hr = df[df["Dept"] == "HR"]["Bonus"].mean()
print("Average Bonus of HR Dept:", avg_bonus_hr)
# 3. Fill NaN values
# Justification: Using median for numeric fields to reduce the impact of outliers
df_filled = df.copy()
numerical_cols = ["Training_Hours", "Score"]
for col in numerical_cols:
median_value = df_filled[col].median()
********** 4 **********
--- page 5 ---
df_filled[col].fillna(median_value, inplace=True)
print("\nDataFrame after filling missing values:\n", df_filled)
Or
# Create dataset
print("Original Data Frame:")
print(df)
# 1. Median Experience of Fin Dept
median_exp_fin <- median(df$Experience[df$Dept == "Fin"])
print(paste("Median Experience of Fin Dept:", median_exp_fin))
# 2. Average Bonus of HR Dept
avg_bonus_hr <- mean(df$Bonus[df$Dept == "HR"])
print(paste("Average Bonus of HR Dept:", avg_bonus_hr))
# 3. Fill NA values (using median)
# Justification: Median avoids outlier influence
df_filled <- df
numeric_cols <- c("Training_Hours", "Score")
for (col in numeric_cols) {
med <- median(df_filled[[col]], na.rm = TRUE)
df_filled[[col]][is.na(df_filled[[col]])] <- med
}
print("Data Frame after filling NA values:")
print(df_filled)
CO-3 ; B # 1. Create a vector v1 with EVEN numbers from 500 to 300   [10]
BL-3   v1 <- seq(500, 300, by = -2) # Descending order initially
print("v1 (descending):")
print(v1)
# 2. Arrange the numbers in ascending order
v1 <- sort(v1) # Sort in ascending order
print("v1 (ascending):")
print(v1)
# 3. Total number of elements in v1
total_elements <- length(v1)
print(paste("Total number of elements in v1:", total_elements))
# 4. Check the dimension of v1
dim_v1 <- dim(v1)
# For a vector, dim() is NULL; vectors are 1-dimensional
print("Dimension of v1:")
print(dim_v1)
# 5. Find the index of number 450
index_450 <- which(v1 == 450)
print(paste("Index of number 450 in v1:", index_450))
OR
# 1. Create a list LIS1 with EVEN numbers from 500 to 300
LIS1 = list(range(500, 299, -2)) # Descending order
print("LIS1 (descending):", LIS1)
# 2. Arrange the numbers in ascending order
LIS1.sort()
print("LIS1 (ascending):", LIS1)
# 3. Total number of elements in LIS1
total_elements = len(LIS1)
print("Total number of elements in LIS1:", total_elements)
# 4. Check the dimension of LIS1
# Lists in Python are 1-dimensional
dimension = 1 # By default
print("Dimension of LIS1:", dimension)
********** 5 **********
--- page 6 ---
# 5. Check the index of number 450
index_450 = LIS1.index(450)
print("Index of number 450 in LIS1:", index_450)
Q4   [20]
CO-2 ;   a.   1. Data Profiling – Analyzes data to identify patterns, inconsistencies, and   [5]
BL-2   anomalies.
2. Data Cleansing – Detects and corrects errors such as duplicates, missing values,
or incorrect formats.
3. Data Standardization – Ensures consistency in data formats, units, naming
conventions, and codes.
4. Data Validation – Checks data against defined rules or constraints to ensure
accuracy and completeness.
5. Monitoring and Reporting – Tracks data quality over time and generates reports
for corrective action.
CO-3 ;   b.   1. Data Cleaning – Removes errors, duplicates, or irrelevant data before loading.   [5]
BL-2   2. Data Integration – Combines data from multiple sources into a unified format.
3. Data Aggregation – Summarizes data, e.g., total sales per month or per region.
4. Data Conversion – Converts data types, formats, or units to match target schema.
5. Data Enrichment – Enhances data by adding derived values, calculated fields, or
external information.
CO-2 ;   c.   1. Definition/Role of Metadata – Metadata is “data about data” that describes   [10]
BL-3   structure, meaning, source, and usage of data in the warehouse. It helps in
understanding, managing, and using data efficiently.
Types of Metadata:
2. Business Metadata – Describes meaning of data in business terms (e.g.,
“Customer_ID represents unique customer”).
3. Technical Metadata – Contains technical details about data storage, tables,
columns, data types, and ETL mappings.
4. Operational Metadata – Provides information on data lineage, refresh schedules,
load timings, and ETL process logs.
How Metadata Supports ETL:
5. Guides ETL tools on source-target mapping, transformation rules, and validation.
6. Tracks data lineage to trace back errors to source systems.
7. Ensures consistent and accurate transformations.
How Metadata Supports Decision-Making:
8. Helps business users understand the context and meaning of data.
9. Ensures confidence in reports and analytics by providing source and
transformation information.
10. Enables impact analysis when schema or data changes occur.
Q5   [20]
CO-2 ;   a.   1. Unit Testing – Test individual ETL components or transformations.   [5]
BL-2   2. System Testing – Test the complete end-to-end ETL process.
3. Data Integration Testing – Verify data from multiple sources is correctly
combined.
4. User Acceptance Testing (UAT) – Business users validate reports and dashboards.
5. Regression Testing – Ensure changes do not break existing functionality.
CO-3 ;   b.   1. Initial Load – Extract complete dataset from source systems and load into the data   [5]
BL-2   warehouse.
2. Data Validation – Check for consistency, integrity, and correctness before loading.
3. Incremental Updates – Apply new or modified records based on primary keys or
unique identifiers.
********** 6 **********
--- page 7 ---
4. Data Maintenance – Handle updates, corrections, and deletions in the warehouse
to reflect source changes.
5. Backup and Audit – Maintain history logs, backup data, and audit trails for
accuracy and compliance.
CO-   c.   1. Problem Definition – Understand business objective: predict which customers   [10]
1 ;BL-   will make repeat purchases. Identify success criteria and KPIs.
3   2. Data Collection – Gather data from e-commerce sources: transaction history,
customer profiles, website interactions, product data.
3. Data Cleaning and Preprocessing – Handle missing values, remove duplicates,
standardize formats, and engineer features like purchase frequency or recency.
4. Exploratory Data Analysis (EDA) – Analyze patterns, correlations, and trends in
the data. Visualize customer behavior and purchase patterns.
5. Feature Engineering – Create meaningful features to improve model performance,
e.g., average purchase value, days since last purchase
6. Model Selection – Choose appropriate predictive models (e.g., logistic regression,
decision trees, random forest, or gradient boosting).
7. Model Training and Evaluation – Split data into training and test sets. Train model
and evaluate performance using metrics like accuracy, precision, recall, or ROC-
AUC.
8. Model Tuning and Optimization – Adjust hyperparameters, perform cross-
validation, and improve prediction accuracy.
9. Deployment – Implement the model in production to predict repeat purchases for
new customers.
10. Monitoring and Maintenance – Continuously monitor model performance, update
with new data, and retrain periodically to ensure accuracy.
Q 6   [20]
CO-3 ;   a.   1. Batch Transfer – Move data at scheduled intervals from the warehouse to near-   [10]
BL-3   line storage.
2. Incremental Loading – Transfer only new or updated records to reduce processing
time.
3. Data Archiving – Automatically archive historical data to near-line storage for
cost efficiency.
4. Data Compression – Compress data before transfer to save storage and bandwidth.
5. Data Partitioning – Split large datasets into manageable segments for easier
migration.
6. Automated ETL Jobs – Use ETL workflows to orchestrate data movement to near-
line storage.
7. Replication / Mirroring – Maintain a near-line copy synchronized with the
warehouse.
8. Data Retention Policies – Define rules for how long data stays in the warehouse
before moving.
9. Error Handling & Logging – Monitor transfer failures and ensure reliable
dataflow.
10. Access Control – Secure sensitive data during transfer and storage in near-line
systems.
CO-2 ;   b. Front-Room (Presentation Layer)   [10]
BL-2
1. Query & Reporting Tools – Enable users to access, analyze, and generate reports.
2. OLAP Tools – Provide multidimensional analysis and dashboards.
3. Data Mining Tools – Support predictive analytics and pattern discovery.
4. End-User Interface – Web portals, dashboards, or BI tools for business users.
5. Metadata Access – Provides business definitions and context for users.
Back-Room (Data Storage & ETL Layer)
********** 7 **********
--- page 8 ---
1. Source Systems – Operational databases, ERP, CRM, and external data sources.
2. ETL/ELT Processes – Extract, transform, and load data into the warehouse.
3. Data Staging Area – Temporary storage for cleaning, transformation, and
integration.
4. Data Warehouse Storage – Central repository for structured and historical data.
5. Metadata Repository – Stores technical, business, and operational metadata for
ETL and user access.
Q 7   [20]
CO-2 ;   a.   1. Subject-Oriented – Data is organized around key subjects such as customers,   [10]
BL-2   products, or sales rather than specific applications. This allows for easier analysis
of business processes.
2. Integrated – Combines data from multiple heterogeneous sources (databases, flat
files, external data) into a consistent format with standardized naming
conventions, units, and encoding.
3. Time-Variant – Historical data is maintained to allow analysis over different
periods (daily, monthly, yearly). Each record is associated with a time element to
track changes.
4. Non-Volatile / Read-Only – Once data is loaded into the warehouse, it is not
frequently updated or deleted. This ensures data stability for analysis and
reporting.
5. Accessible / Query-Oriented – Optimized for complex queries, reporting, and
analytical processing rather than transactional processing.
6. Support for Decision-Making – Enables business intelligence, trend analysis, and
strategic decision-making by providing accurate, consistent, and consolidated
data.
7. Metadata-Driven – Metadata provides information about data sources, definitions,
transformations, and usage, which helps users understand and trust the data.
CO-3 ;   b.   1. Type 0: Retain Original – Values never change; history preserved.   [10]
BL-3   2. Type 1: Overwrite – Update value in-place; history lost.
3. Type 2: Add New Row – Insert new row; old row retained with versioning.
4. Type 3: Add New Column – Store previous value in a separate column.
5. Type 4: Historical Table – Maintain separate table for historical data.
6. Type 6: Hybrid – Combines Types 1, 2, 3 for full and partial history.
7. Update Strategy: Compare source and dimension, insert/update according to SCD
type, use surrogate keys and dates for tracking.
8. Significance: Preserves historical accuracy, supports trend analysis, ensures
reliable reporting, and maintains data integrity.
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 081c3fb4b052

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/Integrated_DS_7038/Data Wrangling/ANS_Data Wrangling(702DB0C012)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech
Intg. (DS)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (DS)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Data Wrangling
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO- 1;   a.   1. Structured data is highly organized in tables with rows and columns and can be   [5]
BL-2   easily stored and queried using relational databases (example: SQL databases,
Excel sheets).
2. Semi-structured data does not follow strict tabular structure but uses tags or
markers to separate elements (example: JSON, XML, CSV with variable fields).
3. Unstructured data has no predefined format or model and is difficult to store and
analyze directly (example: text documents, images, audio, video, emails).
4. Structured data is easiest to search and analyze, semi-structured provides
flexibility with some structure, while unstructured offers the most flexibility but
requires complex tools.
5. Structured data fits SQL databases, semi-structured fits NoSQL systems, and
unstructured often requires big data tools, AI, or text mining for analysis.
CO-2 ;   b.   1. Data warehouses store sensitive historical and business-critical information, so   [5]
BL-3   security protects it from unauthorized access.
2. Security measures maintain data integrity by preventing unauthorized changes that
might lead to false analytics.
3. Legal and regulatory compliance (such as GDPR, HIPAA) requires strong security
controls to protect personal and financial data.
4. Security mechanisms like encryption, access control, and monitoring defend
against data breaches and insider threats.
5. Secure data warehouses build trust, ensure reliable decision-making, and support
business continuity.
********** 1 **********
--- page 2 ---
c.   1. Human errors such as spelling mistakes or inconsistent formats can make data   [5]
inaccurate.
2. Duplicate records occur when the same entry is added multiple times from
different sources.
3. Missing or incomplete data leads to gaps that affect accurate analysis.
4. Outdated information, such as old addresses or prices, reduces the reliability of
reports.
5. Data integration from multiple sources with different formats or rules causes
inconsistencies.
Impact: Dirty data results in incorrect reports, poor business decisions, reduced
customer satisfaction, wasted time and money, and loss of trust in the
organization’s data.
d.   1. Data granularity refers to the level of detail or depth of data stored in a system.   [5]
2. High granularity means very detailed data, such as each transaction or each
customer action.
3. Low granularity means summarized or aggregated data, such as daily or monthly
totals.
4. High granularity provides flexibility and deeper analysis but requires more storage
and processing time.
5. Choosing the right granularity is crucial in data warehousing because it affects
storage, performance, and the quality of insights.
Q2   [20]
CO-   a. # 1. Create a list and multiply each element by 10   [10]
2 ;BL-   numbers = [1, 2, 3, 4, 5]
3   multiplied = [num * 10 for num in numbers]
print("After multiplying by 10:", multiplied)
# 2. Filter numbers greater than a certain value
threshold = 3
filtered = [num for num in numbers if num > threshold]
print("Numbers greater than", threshold, ":", filtered)
# 3. Calculate the sum of all numbers
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)
# 4. Find the mode (most frequent number)
from statistics import mode
numbers_with_duplicates = [2, 3, 2, 5, 4, 2, 3]
most_frequent = mode(numbers_with_duplicates)
• print("Mode of the list:", most_frequent)
OUTPUT:
First print: each element multiplied by 10 → [10, 20, 30, 40, 50]
Second print: numbers > 3 → [4, 5]
Third print: sum of numbers → 15
Fourth print: most frequent number in [2,3,2,5,4,2,3] → 2
R Codes:
# 1. Create a vector and multiply each element by 10
numbers <- c(1, 2, 3, 4, 5)
********** 2 **********
--- page 3 ---
multiplied <- numbers * 10
print(multiplied)
# 2. Filter numbers greater than a certain value
threshold <- 3
filtered <- numbers[numbers > threshold]
print(filtered)
# 3. Calculate the sum of all numbers
total_sum <- sum(numbers)
print(total_sum)
# 4. Find the mode (most frequent number)
numbers_with_duplicates <- c(2, 3, 2, 5, 4, 2, 3)
mode_value <- as.numeric(names(sort(table(numbers_with_duplicates), decreasing
= TRUE)[1]))
print(mode_value)
•   First print: [10 20 30 40 50]
• Second print: [4 5]
• Third print: 15
• Fourth print: 2 (most frequent number)
b. import numpy as np   [10]
CO-
3 ;BL-   # 1. Create two 2x2 matrices A and B
A = np.array([[1, 2],
3   [3, 4]])
B = np.array([[5, 6],
[7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
# 2. Addition (A + B)
add_result = A + B
print("\nA + B:\n", add_result)
# 2. Matrix Multiplication (A * B)
mult_result = A.dot(B)
print("\nA x B:\n", mult_result)
# 3. Extract element in second row, first column
print("\nElement A[2,1]:", A[1, 0])
print("Element B[2,1]:", B[1, 0])
# 4. Replace main diagonal with 0
A_diag_zero = A.copy()
B_diag_zero = B.copy()
np.fill_diagonal(A_diag_zero, 0)
np.fill_diagonal(B_diag_zero, 0)
print("\nA with diagonal 0:\n", A_diag_zero)
print("\nB with diagonal 0:\n", B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 = A + 5
B1 = B + 5
print("\nA1 (A + 5):\n", A1)
• print("\nB1 (B + 5):\n", B1)
R:
********** 3 **********
--- page 4 ---
# 1. Create two 2x2 matrices A and B
A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)
B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
# 2. Addition (A + B)
add_result <- A + B
print("A + B:")
print(add_result)
# 2. Matrix multiplication
mult_result <- A %*% B
print("A x B:")
print(mult_result)
# 3. Extract element in second row, first column
print(paste("Element A[2,1]:", A[2,1]))
print(paste("Element B[2,1]:", B[2,1]))
# 4. Replace main diagonal with 0
A_diag_zero <- A
B_diag_zero <- B
diag(A_diag_zero) <- 0
diag(B_diag_zero) <- 0
print("A with diagonal 0:")
print(A_diag_zero)
print("B with diagonal 0:")
print(B_diag_zero)
# 5. Add 5 to each element and store as A1 and B1
A1 <- A + 5
B1 <- B + 5
print("A1 (A + 5):")
print(A1)
print("B1 (B + 5):")
print(B1)
Q3   [20]
CO-2 ;   a. import pandas as pd   [10]
BL-3   import numpy as np
# Create dataset
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# 1. Median Experience of Fin Dept
median_exp_fin = df[df["Dept"] == "Fin"]["Experience"].median()
print("\nMedian Experience of Fin Dept:", median_exp_fin)
# 2. Average Bonus of HR Dept
avg_bonus_hr = df[df["Dept"] == "HR"]["Bonus"].mean()
print("Average Bonus of HR Dept:", avg_bonus_hr)
# 3. Fill NaN values
# Justification: Using median for numeric fields to reduce the impact of outliers
df_filled = df.copy()
numerical_cols = ["Training_Hours", "Score"]
for col in numerical_cols:
median_value = df_filled[col].median()
********** 4 **********
--- page 5 ---
df_filled[col].fillna(median_value, inplace=True)
print("\nDataFrame after filling missing values:\n", df_filled)
Or
# Create dataset
print("Original Data Frame:")
print(df)
# 1. Median Experience of Fin Dept
median_exp_fin <- median(df$Experience[df$Dept == "Fin"])
print(paste("Median Experience of Fin Dept:", median_exp_fin))
# 2. Average Bonus of HR Dept
avg_bonus_hr <- mean(df$Bonus[df$Dept == "HR"])
print(paste("Average Bonus of HR Dept:", avg_bonus_hr))
# 3. Fill NA values (using median)
# Justification: Median avoids outlier influence
df_filled <- df
numeric_cols <- c("Training_Hours", "Score")
for (col in numeric_cols) {
med <- median(df_filled[[col]], na.rm = TRUE)
df_filled[[col]][is.na(df_filled[[col]])] <- med
}
print("Data Frame after filling NA values:")
print(df_filled)
CO-3 ; B # 1. Create a vector v1 with EVEN numbers from 500 to 300   [10]
BL-3   v1 <- seq(500, 300, by = -2) # Descending order initially
print("v1 (descending):")
print(v1)
# 2. Arrange the numbers in ascending order
v1 <- sort(v1) # Sort in ascending order
print("v1 (ascending):")
print(v1)
# 3. Total number of elements in v1
total_elements <- length(v1)
print(paste("Total number of elements in v1:", total_elements))
# 4. Check the dimension of v1
dim_v1 <- dim(v1)
# For a vector, dim() is NULL; vectors are 1-dimensional
print("Dimension of v1:")
print(dim_v1)
# 5. Find the index of number 450
index_450 <- which(v1 == 450)
print(paste("Index of number 450 in v1:", index_450))
OR
# 1. Create a list LIS1 with EVEN numbers from 500 to 300
LIS1 = list(range(500, 299, -2)) # Descending order
print("LIS1 (descending):", LIS1)
# 2. Arrange the numbers in ascending order
LIS1.sort()
print("LIS1 (ascending):", LIS1)
# 3. Total number of elements in LIS1
total_elements = len(LIS1)
print("Total number of elements in LIS1:", total_elements)
# 4. Check the dimension of LIS1
# Lists in Python are 1-dimensional
dimension = 1 # By default
print("Dimension of LIS1:", dimension)
********** 5 **********
--- page 6 ---
# 5. Check the index of number 450
index_450 = LIS1.index(450)
print("Index of number 450 in LIS1:", index_450)
Q4   [20]
CO-2 ;   a.   1. Data Profiling – Analyzes data to identify patterns, inconsistencies, and   [5]
BL-2   anomalies.
2. Data Cleansing – Detects and corrects errors such as duplicates, missing values,
or incorrect formats.
3. Data Standardization – Ensures consistency in data formats, units, naming
conventions, and codes.
4. Data Validation – Checks data against defined rules or constraints to ensure
accuracy and completeness.
5. Monitoring and Reporting – Tracks data quality over time and generates reports
for corrective action.
CO-3 ;   b.   1. Data Cleaning – Removes errors, duplicates, or irrelevant data before loading.   [5]
BL-2   2. Data Integration – Combines data from multiple sources into a unified format.
3. Data Aggregation – Summarizes data, e.g., total sales per month or per region.
4. Data Conversion – Converts data types, formats, or units to match target schema.
5. Data Enrichment – Enhances data by adding derived values, calculated fields, or
external information.
CO-2 ;   c.   1. Definition/Role of Metadata – Metadata is “data about data” that describes   [10]
BL-3   structure, meaning, source, and usage of data in the warehouse. It helps in
understanding, managing, and using data efficiently.
Types of Metadata:
2. Business Metadata – Describes meaning of data in business terms (e.g.,
“Customer_ID represents unique customer”).
3. Technical Metadata – Contains technical details about data storage, tables,
columns, data types, and ETL mappings.
4. Operational Metadata – Provides information on data lineage, refresh schedules,
load timings, and ETL process logs.
How Metadata Supports ETL:
5. Guides ETL tools on source-target mapping, transformation rules, and validation.
6. Tracks data lineage to trace back errors to source systems.
7. Ensures consistent and accurate transformations.
How Metadata Supports Decision-Making:
8. Helps business users understand the context and meaning of data.
9. Ensures confidence in reports and analytics by providing source and
transformation information.
10. Enables impact analysis when schema or data changes occur.
Q5   [20]
CO-2 ;   a.   1. Unit Testing – Test individual ETL components or transformations.   [5]
BL-2   2. System Testing – Test the complete end-to-end ETL process.
3. Data Integration Testing – Verify data from multiple sources is correctly
combined.
4. User Acceptance Testing (UAT) – Business users validate reports and dashboards.
5. Regression Testing – Ensure changes do not break existing functionality.
CO-3 ;   b.   1. Initial Load – Extract complete dataset from source systems and load into the data   [5]
BL-2   warehouse.
2. Data Validation – Check for consistency, integrity, and correctness before loading.
3. Incremental Updates – Apply new or modified records based on primary keys or
unique identifiers.
********** 6 **********
--- page 7 ---
4. Data Maintenance – Handle updates, corrections, and deletions in the warehouse
to reflect source changes.
5. Backup and Audit – Maintain history logs, backup data, and audit trails for
accuracy and compliance.
CO-   c.   1. Problem Definition – Understand business objective: predict which customers   [10]
1 ;BL-   will make repeat purchases. Identify success criteria and KPIs.
3   2. Data Collection – Gather data from e-commerce sources: transaction history,
customer profiles, website interactions, product data.
3. Data Cleaning and Preprocessing – Handle missing values, remove duplicates,
standardize formats, and engineer features like purchase frequency or recency.
4. Exploratory Data Analysis (EDA) – Analyze patterns, correlations, and trends in
the data. Visualize customer behavior and purchase patterns.
5. Feature Engineering – Create meaningful features to improve model performance,
e.g., average purchase value, days since last purchase
6. Model Selection – Choose appropriate predictive models (e.g., logistic regression,
decision trees, random forest, or gradient boosting).
7. Model Training and Evaluation – Split data into training and test sets. Train model
and evaluate performance using metrics like accuracy, precision, recall, or ROC-
AUC.
8. Model Tuning and Optimization – Adjust hyperparameters, perform cross-
validation, and improve prediction accuracy.
9. Deployment – Implement the model in production to predict repeat purchases for
new customers.
10. Monitoring and Maintenance – Continuously monitor model performance, update
with new data, and retrain periodically to ensure accuracy.
Q 6   [20]
CO-3 ;   a.   1. Batch Transfer – Move data at scheduled intervals from the warehouse to near-   [10]
BL-3   line storage.
2. Incremental Loading – Transfer only new or updated records to reduce processing
time.
3. Data Archiving – Automatically archive historical data to near-line storage for
cost efficiency.
4. Data Compression – Compress data before transfer to save storage and bandwidth.
5. Data Partitioning – Split large datasets into manageable segments for easier
migration.
6. Automated ETL Jobs – Use ETL workflows to orchestrate data movement to near-
line storage.
7. Replication / Mirroring – Maintain a near-line copy synchronized with the
warehouse.
8. Data Retention Policies – Define rules for how long data stays in the warehouse
before moving.
9. Error Handling & Logging – Monitor transfer failures and ensure reliable
dataflow.
10. Access Control – Secure sensitive data during transfer and storage in near-line
systems.
CO-2 ;   b. Front-Room (Presentation Layer)   [10]
BL-2
1. Query & Reporting Tools – Enable users to access, analyze, and generate reports.
2. OLAP Tools – Provide multidimensional analysis and dashboards.
3. Data Mining Tools – Support predictive analytics and pattern discovery.
4. End-User Interface – Web portals, dashboards, or BI tools for business users.
5. Metadata Access – Provides business definitions and context for users.
Back-Room (Data Storage & ETL Layer)
********** 7 **********
--- page 8 ---
1. Source Systems – Operational databases, ERP, CRM, and external data sources.
2. ETL/ELT Processes – Extract, transform, and load data into the warehouse.
3. Data Staging Area – Temporary storage for cleaning, transformation, and
integration.
4. Data Warehouse Storage – Central repository for structured and historical data.
5. Metadata Repository – Stores technical, business, and operational metadata for
ETL and user access.
Q 7   [20]
CO-2 ;   a.   1. Subject-Oriented – Data is organized around key subjects such as customers,   [10]
BL-2   products, or sales rather than specific applications. This allows for easier analysis
of business processes.
2. Integrated – Combines data from multiple heterogeneous sources (databases, flat
files, external data) into a consistent format with standardized naming
conventions, units, and encoding.
3. Time-Variant – Historical data is maintained to allow analysis over different
periods (daily, monthly, yearly). Each record is associated with a time element to
track changes.
4. Non-Volatile / Read-Only – Once data is loaded into the warehouse, it is not
frequently updated or deleted. This ensures data stability for analysis and
reporting.
5. Accessible / Query-Oriented – Optimized for complex queries, reporting, and
analytical processing rather than transactional processing.
6. Support for Decision-Making – Enables business intelligence, trend analysis, and
strategic decision-making by providing accurate, consistent, and consolidated
data.
7. Metadata-Driven – Metadata provides information about data sources, definitions,
transformations, and usage, which helps users understand and trust the data.
CO-3 ;   b.   1. Type 0: Retain Original – Values never change; history preserved.   [10]
BL-3   2. Type 1: Overwrite – Update value in-place; history lost.
3. Type 2: Add New Row – Insert new row; old row retained with versioning.
4. Type 3: Add New Column – Store previous value in a separate column.
5. Type 4: Historical Table – Maintain separate table for historical data.
6. Type 6: Hybrid – Combines Types 1, 2, 3 for full and partial history.
7. Update Strategy: Compare source and dimension, insert/update according to SCD
type, use surrogate keys and dates for tracking.
8. Significance: Preserves historical accuracy, supports trend analysis, ensures
reliable reporting, and maintains data integrity.
********** 8 **********
````
