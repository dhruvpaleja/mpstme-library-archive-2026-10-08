# Data Engineering: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 9e6a846da1bb

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Data Engineering/ANS_Data Engineering(703DB0C050)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: M. Tech (AI)/M. Tech - DS (BA)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Data Engineering
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions. Each question has 2 sections a and b
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a   What are different ‘Types of data’ in Big Data scenario? Elaborate
each type of data with examples along with challenges in the Data
Ingestion
Ans : In a Big Data scenario, data is categorized as structured,
semi-structured,   and   unstructured.
Structured data is organized in rows and columns, such as data
from   relational   databases   or   transaction   records.
CO-1 ; SO-1.6 ;   [5]
BL-3   Semi-structured data includes partially organized formats like
JSON, XML, or sensor logs that have tags but lack a fixed schema.
Unstructured data includes images, videos, social media posts,
and emails, which are   difficult to store and analyze.
During data ingestion, challenges include handling high data
volume and velocity, managing schema changes, ensuring data
quality, and integrating data from diverse sources in real time
without loss or duplication.
********** 1 **********
--- page 2 ---
b   Explain the role and benefits of hybrid (batch / streaming) data [5]
ingestion in modern data systems.
Ans: Hybrid data ingestion combines both batch and real-time
(streaming) ingestion methods to handle diverse data processing
needs in modern data systems. Batch ingestion processes large
volumes of historical or periodic data efficiently, while real-time
CO-2 ; SO-1,6 ;   ingestion captures and processes data instantly as it is generated.
BL-2
This hybrid approach provides flexibility, allowing organizations to
balance speed and cost. It ensures timely insights for operational
decisions while maintaining completeness and accuracy for
analytical workloads. Benefits include improved data availability,
scalability, and fault tolerance, supporting use cases like IoT
analytics, fraud detection, and dynamic dashboards in cloud and
on-premise environments.
c   Explain different data conversion   / data transformation
techniques. What are the benefits of these techniques in data
science projects
Ans: Data conversion and transformation techniques prepare raw
data for analysis by changing its format, structure, or values.
Common techniques include data cleaning (removing duplicates
and errors), normalization and standardization (scaling data to a
CO-1 ; SO-1.6 ;   [5]
BL-3   uniform range), encoding (converting categorical data into
numerical form), aggregation (summarizing data), and feature
extraction or derivation (creating new variables from existing
ones). These techniques ensure data consistency, quality, and
compatibility across diverse sources. In data science projects, they
enhance model accuracy, processing efficiency, and insight
generation, allowing reliable analysis and effective machine
learning model training based on well-prepared, structured data.
d   You are designing a data pipeline for an organization migrating   [5]
CO3-; SO-1,6;
BL-3   from an on-premises data warehouse to a cloud-based data lake.
********** 2 **********
--- page 3 ---
Explain how the choice between ETL (Extract, Transform, Load)
and ELT (Extract, Load, Transform) impacts performance,
scalability, and data governance. Discuss situations where ELT is
preferable over ETL and vice versa.
ETL (Extract, Transform, Load) transforms data before loading it
into the target system, suitable for structured, on-premises
warehouses where data quality and schema consistency are
crucial. ELT (Extract, Load, Transform) loads raw data first and
performs transformations within powerful cloud environments
like Snowflake or BigQuery, improving   scalability and
performance. ETL ensures cleaner data upfront but can be slower
for large or diverse datasets. ELT is ideal for big data and real-time
analytics, leveraging cloud compute power. Challenges like
complex   transformations,   cost   control,   and   pipeline
orchestration are managed using tools such as Apache Spark,
Airflow, or Databricks
a.   Describe the steps involved in exploratory data analysis (EDA)
with Pandas. Support your answer with code snippet.
Ans: Exploratory Data Analysis (EDA) helps understand data
structure, quality, and patterns before modeling. Key steps include:
1. Loading data using Pandas (pd.read_csv()),
2. Viewing structure (df.head(), df.info()),
Q2   3. Checking summary statistics (df.describe()),
[10]
CO-3; SO-1,6;   4. Identifying missing values (df.isnull().sum()),
BL-3
5. Analyzing distributions and correlations (df.hist(),
df.corr()),
6. Handling outliers and data cleaning as needed.
EDA reveals relationships and data quality issues early.
import pandas as pd
df = pd.read_csv("data.csv")
print(df.info())
********** 3 **********
--- page 4 ---
print(df.describe())
print(df.corr())
df.hist()
These steps ensure cleaner, better-understood data for modeling.
b.   Explain the concept of a Data Catalogue and a Data Dictionary.   [10]
Why is creating a data catalogue important in an organization?
Design a sample data catalogue for a financial company, and
discuss the potential risks or issues that may arise if the data
catalogue is not properly prepared or maintained.
Ans: A data catalogue is a centralized inventory that organizes
and documents an organization’s data assets, while a data
Q2
dictionary defines each data element’s meaning, format, and
CO-3; SO-1,6;
source. Preparing a data catalogue is crucial for ensuring data
BL-4
discoverability, governance, and consistency across teams. For a
financial company, it may include details like Customer_ID,
Account_Balance, Transaction_Date, Branch_Code, and
Data_Source. A well-maintained catalogue helps analysts and
engineers understand and use data accurately. If not properly
prepared, it can lead to data duplication, inconsistent reporting,
compliance risks, and inefficient decision-making due to lack of
transparency in data sources and definitions.
a.   What is the purpose of feature engineering in a machine learning   [10]
project, and how does feature scaling (normalization or
standardization) help improve model performance?
Ans The purpose of feature engineering in a machine learning
Q3
project is to enhance model performance by transforming raw data
CO-3; SO-1.6; BL-
3   into meaningful, relevant inputs. It involves creating, modifying,
or selecting features that help the model capture important
patterns and relationships. Feature scaling, through
normalization or standardization, ensures that all features are
on a similar scale, preventing attributes with larger numerical
********** 4 **********
--- page 5 ---
ranges from dominating the learning process. Scaling improves
model convergence, accuracy, and stability,
b.   Explain cloud storage and on premises storage. Analyze the trade-   [10]
offs between the two storage systems. Give situations where you
will use Cloud, On Prem or hybrid storage.
Ans : Cloud storage stores data on remote servers managed by
providers like AWS or Azure, offering scalability, accessibility,
and reduced maintenance. On-premises storage keeps data within
Q3
an organization’s local infrastructure, providing greater control,
CO-4; SO-1,6; BL-
security, and compliance but requiring higher setup and
4
maintenance costs. Trade-offs include cost, control, and
scalability—cloud offers flexibility and lower upfront costs, while
on-prem provides data sovereignty and faster local access. Cloud
storage suits startups and dynamic workloads, on-premises fits
organizations with strict regulatory or latency requirements, and
hybrid storage is ideal when balancing data security, cost
efficiency, and scalability across diverse business needs.
a.   In the context of modern data systems, explain data protection,   [10]
data privacy, and data security. How would you design a
framework to ensure compliance with government data
regulations? Who will be responsible for data Protection, data
privacy and data security.
Q4   Data protection ensures data is safeguarded from loss or
CO5-; SO-1.6;   corruption, while data privacy focuses on controlling how
BL-4   personal or sensitive data is collected, used, and shared. Data
security involves implementing technical measures like
encryption, access control, and firewalls to prevent unauthorized
access. A compliance framework should include policies, risk
assessments, encryption standards, audit trails, and user
consent management to meet government regulations .
IT/security teams ensure technical safeguards, and
********** 5 **********
--- page 6 ---
business/data owners maintain privacy and responsible data
handling throughout the organization
b.   Describe how a data engineer contributes to Descriptive,   [10]
Diagnostic, Predictive, and Prescriptive Analytics within an
organization. Provide an example illustrating each type of
analytics. Additionally, explain why Data Engineering plays a
critical role in enabling and supporting Artificial Intelligence (AI)
applications.
A data engineer builds the data pipelines and infrastructure that
Q4   power all types of analytics. In descriptive analytics, they collect
CO2-; SO-1,6;   and clean historical data to generate dashboards (e.g., monthly
BL-3   sales summaries). For diagnostic analytics, they integrate and
transform data to identify causes of trends (e.g., sales drop due
to regional demand). In predictive analytics, they prepare
training data for models forecasting future outcomes (e.g.,
predicting customer churn). For prescriptive analytics, they
enable optimization models (e.g., recommending best pricing
strategies). Data engineering is vital for AI, ensuring high-quality,
scalable, and reliable data pipelines that support accurate model
training and deployment
a.   Define Data Analytics and illustrate how it can be implemented   [10]
using Python. Discuss key libraries and tools commonly used in
the data analytics process, and explain their roles with relevant
examples.
Q5
Ans: Data analytics is the process of examining raw data to discover
CO3-; SO-1,6;
BL-4   meaningful insights, patterns, and trends that support decision-
making. In Python, data analytics involves steps like data collection,
cleaning, visualization, and modeling. Libraries such as Pandas and
NumPy are used for data manipulation, Matplotlib and Seaborn for
visualization, and Scikit-learn for statistical analysis and machine
learning. For example:
********** 6 **********
--- page 7 ---
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.describe())
This code analyzes key statistics of sales data. Tools like Jupyter
Notebook and Google Colab make data analysis interactive,
efficient, and visually insightful for analytics projects.
b.   What is data warehouse? A financial company wants to build a   [10]
data warehouse to integrate data from multiple operational
databases and external APIs for real-time analytics. Explain how
you would design the ETL/ELT workflow, data modeling, and
storage layers to support both historical and near real-time
reporting.
A data warehouse is a centralized repository that stores
Q5
integrated data from multiple sources for analysis and reporting.
CO5-; SO-1,6;
For a financial company, the design should include an ELT
BL-3
workflow, where raw data from databases and APIs is loaded
into a staging layer, then transformed within the warehouse for
efficiency. Data modeling can follow a star schema with fact and
dimension tables to simplify analytics. The storage layer should
use columnar storage for faster queries and support incremental
updates for near real-time reporting. Tools like Snowflake,
Redshift, or BigQuery enable scalability, governance, and high-
performance data analytics.
a.   What is data lineage, and why is it important in data   [10]
engineering? How does data lineage help in maintaining data
quality and ensuring regulatory compliance?
Q6
CO4-; SO-1,6;
Data lineage refers to tracking the complete lifecycle of data —
BL-4
from its origin, movement, and transformations to its final
destination. It provides a clear view of how data flows through
various systems in a data pipeline. In data engineering, lineage is
********** 7 **********
--- page 8 ---
crucial for understanding data dependencies, troubleshooting
issues, and ensuring transparency. It helps maintain data quality
by identifying the source of errors or inconsistencies and
verifying data transformations. For regulatory compliance, data
lineage provides audit trails and documentation that
demonstrate data accuracy and integrity, meeting standards such
as GDPR, HIPAA, or financial data governance requirements.
b   What are the challenges handling unstructured data? What is [10]
Metadata? Explain importance of metadata in dealing with
unstructured data? Give examples of metadata.
Ans Handling unstructured data such as emails, videos, images,
or social media posts is challenging due to its lack of predefined
schema, large volume, varied formats, and difficulty in indexing
CO-2 ; SO- 1,6;   and searching. Metadata is data that describes other data—
BL-2   providing context like source, creation date, file type, or author.
It helps in organizing, classifying, and retrieving unstructured
data efficiently. Metadata enables better data governance,
searchability, and integration in analytics systems. Examples
include file size, timestamp, GPS location, content tags, or
document author. Proper metadata management transforms raw
unstructured content into a more discoverable and analyzable
data asset.
a.   Explain the concept of data pipeline in the data orchestration   [10]
process. What are the challenges in establishing data pipeline
from different external sources. Explain with example how will
you establish the data pipeline considering data quality, data
Q7
integrity and data governance challenges. Give sample python
CO-4; SO-1,6;
code to establish data pipeline.
BL-5
Ans: A data pipeline automates the extraction, transformation,
and loading of data from multiple sources, ensuring data quality,
integrity, and governance. Challenges include handling
********** 8 **********
--- page 9 ---
inconsistent schemas, missing data, and integrating APIs, files,
and databases. Using Python and Pandas, we can build a simple
pipeline to concatenate data from different CSV files:
import pandas as pd
from sklearn.pipeline import Pipeline
def load_data():
files = ["sales_jan.csv", "sales_feb.csv"]
return pd.concat([pd.read_csv(f) for f in files],
ignore_index=True)
pipeline = Pipeline([("load_concat", load_data)])
df = pipeline.named_steps["load_concat"]()
print(df.head())
This pipeline ensures unified, validated data flow.
b   What is pivot table? How Pivot table helps in data analysis. You [10]
have a dataset with millions of transaction records containing
fields — Customer ID, Product ID, Purchase Date, Quantity,
Revenue, and Region. Explain how you would design a multi-level
pivot table to analyze customer purchasing behavior across
regions and time periods. Describe how you could incorporate
calculated fields (e.g., average revenue per customer) and filters
to derive deeper insights.
CO-3 ; SO-1,6 ;
BL-4
A pivot table is a powerful data summarization tool used to
aggregate, analyze, and explore large datasets. It helps in data
analysis by allowing users to quickly group, filter, and compute
metrics from complex data. For a dataset with millions of
transactions, a multi-level pivot table can be designed with
Region and Purchase Date (monthly or quarterly) as rows, Product
ID as columns, and aggregated Revenue or Quantity as values. A
calculated field, such as Average Revenue per Customer = Total
********** 9 **********
--- page 10 ---
Revenue / Unique Customers, provides deeper insight. Filters can
refine the analysis by specific regions, products, or time periods.
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 0d2270f5c9dd

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Data Engineering/ANS_Data Engineering(703DB0C050)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: M. Tech (AI)/M. Tech - DS (BA)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Data Engineering
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions. Each question has 2 sections a and b
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a   What are different ‘Types of data’ in Big Data scenario? Elaborate
each type of data with examples along with challenges in the Data
Ingestion
Ans : In a Big Data scenario, data is categorized as structured,
semi-structured,   and   unstructured.
Structured data is organized in rows and columns, such as data
from   relational   databases   or   transaction   records.
CO-1 ; SO-1.6 ;   [5]
BL-3   Semi-structured data includes partially organized formats like
JSON, XML, or sensor logs that have tags but lack a fixed schema.
Unstructured data includes images, videos, social media posts,
and emails, which are   difficult to store and analyze.
During data ingestion, challenges include handling high data
volume and velocity, managing schema changes, ensuring data
quality, and integrating data from diverse sources in real time
without loss or duplication.
********** 1 **********
--- page 2 ---
b   Explain the role and benefits of hybrid (batch / streaming) data [5]
ingestion in modern data systems.
Ans: Hybrid data ingestion combines both batch and real-time
(streaming) ingestion methods to handle diverse data processing
needs in modern data systems. Batch ingestion processes large
volumes of historical or periodic data efficiently, while real-time
CO-2 ; SO-1,6 ;   ingestion captures and processes data instantly as it is generated.
BL-2
This hybrid approach provides flexibility, allowing organizations to
balance speed and cost. It ensures timely insights for operational
decisions while maintaining completeness and accuracy for
analytical workloads. Benefits include improved data availability,
scalability, and fault tolerance, supporting use cases like IoT
analytics, fraud detection, and dynamic dashboards in cloud and
on-premise environments.
c   Explain different data conversion   / data transformation
techniques. What are the benefits of these techniques in data
science projects
Ans: Data conversion and transformation techniques prepare raw
data for analysis by changing its format, structure, or values.
Common techniques include data cleaning (removing duplicates
and errors), normalization and standardization (scaling data to a
CO-1 ; SO-1.6 ;   [5]
BL-3   uniform range), encoding (converting categorical data into
numerical form), aggregation (summarizing data), and feature
extraction or derivation (creating new variables from existing
ones). These techniques ensure data consistency, quality, and
compatibility across diverse sources. In data science projects, they
enhance model accuracy, processing efficiency, and insight
generation, allowing reliable analysis and effective machine
learning model training based on well-prepared, structured data.
d   You are designing a data pipeline for an organization migrating   [5]
CO3-; SO-1,6;
BL-3   from an on-premises data warehouse to a cloud-based data lake.
********** 2 **********
--- page 3 ---
Explain how the choice between ETL (Extract, Transform, Load)
and ELT (Extract, Load, Transform) impacts performance,
scalability, and data governance. Discuss situations where ELT is
preferable over ETL and vice versa.
ETL (Extract, Transform, Load) transforms data before loading it
into the target system, suitable for structured, on-premises
warehouses where data quality and schema consistency are
crucial. ELT (Extract, Load, Transform) loads raw data first and
performs transformations within powerful cloud environments
like Snowflake or BigQuery, improving   scalability and
performance. ETL ensures cleaner data upfront but can be slower
for large or diverse datasets. ELT is ideal for big data and real-time
analytics, leveraging cloud compute power. Challenges like
complex   transformations,   cost   control,   and   pipeline
orchestration are managed using tools such as Apache Spark,
Airflow, or Databricks
a.   Describe the steps involved in exploratory data analysis (EDA)
with Pandas. Support your answer with code snippet.
Ans: Exploratory Data Analysis (EDA) helps understand data
structure, quality, and patterns before modeling. Key steps include:
1. Loading data using Pandas (pd.read_csv()),
2. Viewing structure (df.head(), df.info()),
Q2   3. Checking summary statistics (df.describe()),
[10]
CO-3; SO-1,6;   4. Identifying missing values (df.isnull().sum()),
BL-3
5. Analyzing distributions and correlations (df.hist(),
df.corr()),
6. Handling outliers and data cleaning as needed.
EDA reveals relationships and data quality issues early.
import pandas as pd
df = pd.read_csv("data.csv")
print(df.info())
********** 3 **********
--- page 4 ---
print(df.describe())
print(df.corr())
df.hist()
These steps ensure cleaner, better-understood data for modeling.
b.   Explain the concept of a Data Catalogue and a Data Dictionary.   [10]
Why is creating a data catalogue important in an organization?
Design a sample data catalogue for a financial company, and
discuss the potential risks or issues that may arise if the data
catalogue is not properly prepared or maintained.
Ans: A data catalogue is a centralized inventory that organizes
and documents an organization’s data assets, while a data
Q2
dictionary defines each data element’s meaning, format, and
CO-3; SO-1,6;
source. Preparing a data catalogue is crucial for ensuring data
BL-4
discoverability, governance, and consistency across teams. For a
financial company, it may include details like Customer_ID,
Account_Balance, Transaction_Date, Branch_Code, and
Data_Source. A well-maintained catalogue helps analysts and
engineers understand and use data accurately. If not properly
prepared, it can lead to data duplication, inconsistent reporting,
compliance risks, and inefficient decision-making due to lack of
transparency in data sources and definitions.
a.   What is the purpose of feature engineering in a machine learning   [10]
project, and how does feature scaling (normalization or
standardization) help improve model performance?
Ans The purpose of feature engineering in a machine learning
Q3
project is to enhance model performance by transforming raw data
CO-3; SO-1.6; BL-
3   into meaningful, relevant inputs. It involves creating, modifying,
or selecting features that help the model capture important
patterns and relationships. Feature scaling, through
normalization or standardization, ensures that all features are
on a similar scale, preventing attributes with larger numerical
********** 4 **********
--- page 5 ---
ranges from dominating the learning process. Scaling improves
model convergence, accuracy, and stability,
b.   Explain cloud storage and on premises storage. Analyze the trade-   [10]
offs between the two storage systems. Give situations where you
will use Cloud, On Prem or hybrid storage.
Ans : Cloud storage stores data on remote servers managed by
providers like AWS or Azure, offering scalability, accessibility,
and reduced maintenance. On-premises storage keeps data within
Q3
an organization’s local infrastructure, providing greater control,
CO-4; SO-1,6; BL-
security, and compliance but requiring higher setup and
4
maintenance costs. Trade-offs include cost, control, and
scalability—cloud offers flexibility and lower upfront costs, while
on-prem provides data sovereignty and faster local access. Cloud
storage suits startups and dynamic workloads, on-premises fits
organizations with strict regulatory or latency requirements, and
hybrid storage is ideal when balancing data security, cost
efficiency, and scalability across diverse business needs.
a.   In the context of modern data systems, explain data protection,   [10]
data privacy, and data security. How would you design a
framework to ensure compliance with government data
regulations? Who will be responsible for data Protection, data
privacy and data security.
Q4   Data protection ensures data is safeguarded from loss or
CO5-; SO-1.6;   corruption, while data privacy focuses on controlling how
BL-4   personal or sensitive data is collected, used, and shared. Data
security involves implementing technical measures like
encryption, access control, and firewalls to prevent unauthorized
access. A compliance framework should include policies, risk
assessments, encryption standards, audit trails, and user
consent management to meet government regulations .
IT/security teams ensure technical safeguards, and
********** 5 **********
--- page 6 ---
business/data owners maintain privacy and responsible data
handling throughout the organization
b.   Describe how a data engineer contributes to Descriptive,   [10]
Diagnostic, Predictive, and Prescriptive Analytics within an
organization. Provide an example illustrating each type of
analytics. Additionally, explain why Data Engineering plays a
critical role in enabling and supporting Artificial Intelligence (AI)
applications.
A data engineer builds the data pipelines and infrastructure that
Q4   power all types of analytics. In descriptive analytics, they collect
CO2-; SO-1,6;   and clean historical data to generate dashboards (e.g., monthly
BL-3   sales summaries). For diagnostic analytics, they integrate and
transform data to identify causes of trends (e.g., sales drop due
to regional demand). In predictive analytics, they prepare
training data for models forecasting future outcomes (e.g.,
predicting customer churn). For prescriptive analytics, they
enable optimization models (e.g., recommending best pricing
strategies). Data engineering is vital for AI, ensuring high-quality,
scalable, and reliable data pipelines that support accurate model
training and deployment
a.   Define Data Analytics and illustrate how it can be implemented   [10]
using Python. Discuss key libraries and tools commonly used in
the data analytics process, and explain their roles with relevant
examples.
Q5
Ans: Data analytics is the process of examining raw data to discover
CO3-; SO-1,6;
BL-4   meaningful insights, patterns, and trends that support decision-
making. In Python, data analytics involves steps like data collection,
cleaning, visualization, and modeling. Libraries such as Pandas and
NumPy are used for data manipulation, Matplotlib and Seaborn for
visualization, and Scikit-learn for statistical analysis and machine
learning. For example:
********** 6 **********
--- page 7 ---
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.describe())
This code analyzes key statistics of sales data. Tools like Jupyter
Notebook and Google Colab make data analysis interactive,
efficient, and visually insightful for analytics projects.
b.   What is data warehouse? A financial company wants to build a   [10]
data warehouse to integrate data from multiple operational
databases and external APIs for real-time analytics. Explain how
you would design the ETL/ELT workflow, data modeling, and
storage layers to support both historical and near real-time
reporting.
A data warehouse is a centralized repository that stores
Q5
integrated data from multiple sources for analysis and reporting.
CO5-; SO-1,6;
For a financial company, the design should include an ELT
BL-3
workflow, where raw data from databases and APIs is loaded
into a staging layer, then transformed within the warehouse for
efficiency. Data modeling can follow a star schema with fact and
dimension tables to simplify analytics. The storage layer should
use columnar storage for faster queries and support incremental
updates for near real-time reporting. Tools like Snowflake,
Redshift, or BigQuery enable scalability, governance, and high-
performance data analytics.
a.   What is data lineage, and why is it important in data   [10]
engineering? How does data lineage help in maintaining data
quality and ensuring regulatory compliance?
Q6
CO4-; SO-1,6;
Data lineage refers to tracking the complete lifecycle of data —
BL-4
from its origin, movement, and transformations to its final
destination. It provides a clear view of how data flows through
various systems in a data pipeline. In data engineering, lineage is
********** 7 **********
--- page 8 ---
crucial for understanding data dependencies, troubleshooting
issues, and ensuring transparency. It helps maintain data quality
by identifying the source of errors or inconsistencies and
verifying data transformations. For regulatory compliance, data
lineage provides audit trails and documentation that
demonstrate data accuracy and integrity, meeting standards such
as GDPR, HIPAA, or financial data governance requirements.
b   What are the challenges handling unstructured data? What is [10]
Metadata? Explain importance of metadata in dealing with
unstructured data? Give examples of metadata.
Ans Handling unstructured data such as emails, videos, images,
or social media posts is challenging due to its lack of predefined
schema, large volume, varied formats, and difficulty in indexing
CO-2 ; SO- 1,6;   and searching. Metadata is data that describes other data—
BL-2   providing context like source, creation date, file type, or author.
It helps in organizing, classifying, and retrieving unstructured
data efficiently. Metadata enables better data governance,
searchability, and integration in analytics systems. Examples
include file size, timestamp, GPS location, content tags, or
document author. Proper metadata management transforms raw
unstructured content into a more discoverable and analyzable
data asset.
a.   Explain the concept of data pipeline in the data orchestration   [10]
process. What are the challenges in establishing data pipeline
from different external sources. Explain with example how will
you establish the data pipeline considering data quality, data
Q7
integrity and data governance challenges. Give sample python
CO-4; SO-1,6;
code to establish data pipeline.
BL-5
Ans: A data pipeline automates the extraction, transformation,
and loading of data from multiple sources, ensuring data quality,
integrity, and governance. Challenges include handling
********** 8 **********
--- page 9 ---
inconsistent schemas, missing data, and integrating APIs, files,
and databases. Using Python and Pandas, we can build a simple
pipeline to concatenate data from different CSV files:
import pandas as pd
from sklearn.pipeline import Pipeline
def load_data():
files = ["sales_jan.csv", "sales_feb.csv"]
return pd.concat([pd.read_csv(f) for f in files],
ignore_index=True)
pipeline = Pipeline([("load_concat", load_data)])
df = pipeline.named_steps["load_concat"]()
print(df.head())
This pipeline ensures unified, validated data flow.
b   What is pivot table? How Pivot table helps in data analysis. You [10]
have a dataset with millions of transaction records containing
fields — Customer ID, Product ID, Purchase Date, Quantity,
Revenue, and Region. Explain how you would design a multi-level
pivot table to analyze customer purchasing behavior across
regions and time periods. Describe how you could incorporate
calculated fields (e.g., average revenue per customer) and filters
to derive deeper insights.
CO-3 ; SO-1,6 ;
BL-4
A pivot table is a powerful data summarization tool used to
aggregate, analyze, and explore large datasets. It helps in data
analysis by allowing users to quickly group, filter, and compute
metrics from complex data. For a dataset with millions of
transactions, a multi-level pivot table can be designed with
Region and Purchase Date (monthly or quarterly) as rows, Product
ID as columns, and aggregated Revenue or Quantity as values. A
calculated field, such as Average Revenue per Customer = Total
********** 9 **********
--- page 10 ---
Revenue / Unique Customers, provides deeper insight. Filters can
refine the analysis by specific regions, products, or time periods.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper b85053a76637

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Data Engineering/ANS_Data Engineering(703DB0C050)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: M. Tech (AI)/M. Tech - DS (BA)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: Data Engineering
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions. Each question has 2 sections a and b
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly. Q1 is compulsory.   Marks
a.   Define Data Analytics and illustrate how it can be implemented   [5]
using Python. Discuss key libraries and tools commonly used in
the data analytics process, and explain their roles with relevant
examples.
Ans: Data analytics is the process of examining raw data to
discover meaningful insights, patterns, and trends that support
decision-making. In Python, data analytics involves steps like
data collection, cleaning, visualization, and modelling. Libraries
Q1
CO3-; SO-1,6;   such as Pandas and NumPy are used for data manipulation,
BL-4   Matplotlib and Seaborn for visualization, and Scikit-learn for
statistical analysis and machine learning. For example:
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.describe())
This code analyzes key statistics of sales data. Tools like Jupyter
Notebook and Google Colab make data analysis interactive,
efficient, and visually insightful for analytics projects.
********** 1 **********
--- page 2 ---
b   What is hybrid (batch / streaming) data ingestion in modern data [5]
systems. Explain with example advantages as well as challenges.
Ans: Hybrid data ingestion combines both batch and real-time
(streaming) ingestion methods to handle diverse data processing
needs in modern data systems. Batch ingestion processes large
volumes of historical or periodic data efficiently, while real-time
Q1
CO-2 ; SO-1,6 ;   ingestion captures and processes data instantly as it is generated.
BL-2   This hybrid approach provides flexibility, allowing organizations
to balance speed and cost. It ensures timely insights for operational
decisions while maintaining completeness and accuracy for
analytical workloads. Benefits include improved data availability,
scalability, and fault tolerance, supporting use cases like IoT
analytics, fraud detection, and dynamic dashboards in cloud and
on-premise environments.
c   Explain different data conversion / data transformation techniques.
What are the benefits of these techniques in data science projects
Ans: Data conversion and transformation techniques prepare
raw data for analysis by changing its format, structure, or values.
Common techniques include data cleaning (removing duplicates
and errors), normalization and standardization (scaling data to a
Q1
CO-1 ; SO-1.6 ;   uniform range), encoding (converting categorical data into [5]
BL-3   numerical form), aggregation (summarizing data), and feature
extraction or derivation (creating new variables from existing
ones). These techniques ensure data consistency, quality, and
compatibility across diverse sources. In data science projects, they
enhance model accuracy, processing efficiency, and insight
generation, allowing reliable analysis and effective machine
learning model training based on well-prepared, structured data.
d   Explain ETL and ELT. You are designing a data pipeline for an   [5]
organization migrating from an on-premises data warehouse to a
Q1
CO3-; SO-1,6;   cloud-based data lake. Explain how the choice between ETL
BL-3   (Extract, Transform, Load) and ELT (Extract, Load,
Transform) impacts performance, scalability, and data
********** 2 **********
--- page 3 ---
governance. Discuss situations where ELT is preferable over ETL
and vice versa.
ETL (Extract, Transform, Load) transforms data before loading
it into the target system, suitable for structured, on-premises
warehouses where data quality and schema consistency are crucial.
ELT (Extract, Load, Transform) loads raw data first and
performs transformations within powerful cloud environments like
Snowflake or BigQuery, improving scalability and performance.
ETL ensures cleaner data upfront but can be slower for large or
diverse datasets. ELT is ideal for big data and real-time analytics,
leveraging cloud compute power. Challenges like complex
transformations, cost control, and pipeline orchestration are
managed using tools such as Apache Spark, Airflow, or
Databricks
Section 2: Attempt Any 4 questions
a.   What is EDA? Describe the steps involved in exploratory data
analysis (EDA) with Pandas. Support your answer with code
snippet.
Ans: Exploratory Data Analysis (EDA) helps understand data
structure, quality, and patterns before modelling. Key steps
include:
1. Loading data using Pandas (pd.read_csv()),
2. Viewing structure (df.head(), df.info()),
Q2
3. Checking summary statistics (df.describe()),   [10]
CO-3; SO-1,6;
BL-3   4. Identifying missing values (df.isnull().sum()),
5. Analyzing distributions and correlations (df.hist(),
df.corr()),
6. Handling outliers and data cleaning as needed.
EDA reveals relationships and data quality issues early.
import pandas as pd
df = pd.read_csv("data.csv")
print(df.info())
print(df.describe())
********** 3 **********
--- page 4 ---
print(df.corr())
df.hist()
These steps ensure cleaner, better-understood data for modelling.
b.   Explain the concept of a Data Catalogue and a Data Dictionary.   [10]
Why is creating a data catalogue important in an organization?
Design a sample data catalogue for a financial company, and
discuss the potential risks or issues that may arise if the data
catalogue is not properly prepared or maintained.
Ans: A data catalogue is a centralized inventory that organizes
and documents an organization’s data assets, while a data
Q2
dictionary defines each data element’s meaning, format, and
CO-3; SO-1,6;
source. Preparing a data catalogue is crucial for ensuring data
BL-4
discoverability, governance, and consistency across teams. For a
financial company, it may include details like Customer_ID,
Account_Balance, Transaction_Date, Branch_Code, and
Data_Source. A well-maintained catalogue helps analysts and
engineers understand and use data accurately. If not properly
prepared, it can lead to data duplication, inconsistent reporting,
compliance risks, and inefficient decision-making due to lack of
transparency in data sources and definitions.
a.   What is feature engineering? What is the purpose of feature   [10]
engineering in a machine learning project, and how does feature
scaling (normalization or standardization) help improve model
performance?
Q3   Ans The purpose of feature engineering in a machine learning
CO-3; SO-1.6;   project is to enhance model performance by transforming raw data
BL-3
into meaningful, relevant inputs. It involves creating, modifying,
or selecting features that help the model capture important
patterns and relationships. Feature scaling, through
normalization or standardization, ensures that all features are
on a similar scale, preventing attributes with larger numerical
********** 4 **********
--- page 5 ---
ranges from dominating the learning process. Scaling improves
model convergence, accuracy, and stability,
b.   Explain cloud storage and on premises storage. Analyze the trade-   [10]
offs between the two storage systems. Give situations where you
will use Cloud, On Prem or hybrid storage. What is Edge
computing and how it helps to solve storage and performance
challenges
Ans: Cloud storage stores data on remote servers managed by
providers like AWS or Azure, offering scalability, accessibility,
Q3   and reduced maintenance. On-premises storage keeps data within
CO-4; SO-1,6;   an organization’s local infrastructure, providing greater control,
BL-4   security, and compliance but requiring higher setup and
maintenance costs. Trade-offs include cost, control, and
scalability—cloud offers flexibility and lower upfront costs, while
on-prem provides data sovereignty and faster local access. Cloud
storage suits startups and dynamic workloads, on-premises fits
organizations with strict regulatory or latency requirements, and
hybrid storage is ideal when balancing data security, cost
efficiency, and scalability across diverse business needs.
Edge computing and how it address challenges of data storage.
a.   Explain data protection, data privacy, and data security and why it   [10]
has become important in today’s scenario. How would you design
a framework to ensure compliance with government data
regulations? Who will be responsible for data Protection, data
privacy and data security.
Q4
Data protection ensures data is safeguarded from loss or
CO5-; SO-1.6;
corruption, while data privacy focuses on controlling how
BL-4
personal or sensitive data is collected, used, and shared. Data
security involves implementing technical measures like
encryption, access control, and firewalls to prevent unauthorized
access. A compliance framework should include policies, risk
assessments, encryption standards, audit trails, and user
consent management to meet government regulations.
********** 5 **********
--- page 6 ---
IT/security teams ensure technical safeguards, and business/data
owners maintain privacy and responsible data handling
throughout the organization
b.   Describe how a data engineer contributes to Descriptive,   [10]
Diagnostic, Predictive, and Prescriptive Analytics within an
organization. Provide an example illustrating each type of
analytics. Additionally, explain why Data Engineering plays a
critical role in enabling and supporting Artificial Intelligence
(AI) applications.
A data engineer builds the data pipelines and infrastructure that
Q4   power all types of analytics. In descriptive analytics, they collect
CO2-; SO-1,6;   and clean historical data to generate dashboards (e.g., monthly
BL-3   sales summaries). For diagnostic analytics, they integrate and
transform data to identify causes of trends (e.g., sales drop due to
regional demand). In predictive analytics, they prepare training
data for models forecasting future outcomes (e.g., predicting
customer churn). For prescriptive analytics, they enable
optimization models (e.g., recommending best pricing strategies).
Data engineering is vital for AI, ensuring high-quality, scalable,
and reliable data pipelines that support accurate model training
and deployment
a   What are different ‘Types of data’ in Big Data analytics? Elaborate
different data types with examples along with challenges you may
face in Data Ingestion process.
Ans : In a Big Data scenario, data is categorized as structured,
Q5   semi-structured, and unstructured.
CO-1 ; SO-1.6 ;   [10]
BL-3   Structured data is organized in rows and columns, such as data
from relational databases or transaction records.
Semi-structured data includes partially organized formats like
JSON, XML, or sensor logs that have tags but lack a fixed
schema.
Unstructured data includes images, videos, social media posts,
********** 6 **********
--- page 7 ---
and emails, which are difficult to store and analyze.
During data ingestion, challenges include handling high data
volume and velocity, managing schema changes, ensuring data
quality, and integrating data from diverse sources in real time
without loss or duplication.
b.   What is data warehouse? A financial company wants to build a   [10]
data warehouse to integrate data from multiple operational
databases and external APIs for real-time analytics. Explain how
you would design the ETL/ELT workflow, data modeling, and
storage layers to support both historical and near real-time
reporting.
A data warehouse is a centralized repository that stores
Q5
integrated data from multiple sources for analysis and reporting.
CO5-; SO-1,6;
For a financial company, the design should include an ELT
BL-3
workflow, where raw data from databases and APIs is loaded into
a staging layer, then transformed within the warehouse for
efficiency. Data modeling can follow a star schema with fact
and dimension tables to simplify analytics. The storage layer
should use columnar storage for faster queries and support
incremental updates for near real-time reporting. Tools like
Snowflake, Redshift, or BigQuery enable scalability,
governance, and high-performance data analytics.
a.   What is data lineage, and why is it important in data engineering?   [10]
How does data lineage help in maintaining data quality and
ensuring regulatory compliance?
Data lineage refers to tracking the complete lifecycle of data —
Q6
from its origin, movement, and transformations to its final
CO4-; SO-1,6;
destination. It provides a clear view of how data flows through
BL-4
various systems in a data pipeline. In data engineering, lineage is
crucial for understanding data dependencies, troubleshooting
issues, and ensuring transparency. It helps maintain data quality
by identifying the source of errors or inconsistencies and
verifying data transformations. For regulatory compliance, data
********** 7 **********
--- page 8 ---
lineage provides audit trails and documentation that demonstrate
data accuracy and integrity, meeting standards such as GDPR,
HIPAA, or financial data governance requirements.
b   What are the challenges handling unstructured data? What is [10]
Metadata? Explain importance of metadata in dealing with
unstructured data? Give examples of metadata.
Ans Handling unstructured data such as emails, videos, images,
or social media posts is challenging due to its lack of predefined
schema, large volume, varied formats, and difficulty in
Q6   indexing and searching. Metadata is data that describes other
CO-2 ; SO- 1,6;
BL-2   data—providing context like source, creation date, file type, or
author. It helps in organizing, classifying, and retrieving
unstructured data efficiently. Metadata enables better data
governance, searchability, and integration in analytics systems.
Examples include file size, timestamp, GPS location, content
tags, or document author. Proper metadata management
transforms raw unstructured content into a more discoverable and
analyzable data asset.
a.   Explain the concept of data pipeline in the data orchestration   [10]
process. What are the challenges in establishing data pipeline
from different external sources. Explain with example how will
you establish the data pipeline considering data quality, data
integrity and data governance challenges. Give sample python
code to establish data pipeline.
Q7
Ans: A data pipeline automates the extraction, transformation,
CO-4; SO-1,6;
and loading of data from multiple sources, ensuring data quality,
BL-5
integrity, and governance. Challenges include handling
inconsistent schemas, missing data, and integrating APIs, files,
and databases. Using Python and Pandas, we can build a simple
pipeline to concatenate data from different CSV files:
import pandas as pd
from sklearn.pipeline import Pipeline
def load_data():
********** 8 **********
--- page 9 ---
files = ["sales_jan.csv", "sales_feb.csv"]
return pd.concat([pd.read_csv(f) for f in files],
ignore_index=True)
pipeline = Pipeline([("load_concat", load_data)])
df = pipeline.named_steps["load_concat"]()
print(df.head())
This pipeline ensures unified, validated data flow.
b   What is pivot table? How Pivot table helps in data analysis. You [10]
have a dataset with millions of transaction records containing fields
— Customer ID, Product ID, Purchase Date, Quantity, Revenue,
and Region. Explain how you would design a multi-level pivot
table to analyze customer purchasing behavior across regions
and time periods. Describe how you could incorporate calculated
fields (e.g., average revenue per customer) and filters to derive
deeper insights.
Q7   A pivot table is a powerful data summarization tool used to
CO-3 ; SO-1,6 ;
BL-4   aggregate, analyze, and explore large datasets. It helps in data
analysis by allowing users to quickly group, filter, and compute
metrics from complex data. For a dataset with millions of
transactions, a multi-level pivot table can be designed with Region
and Purchase Date (monthly or quarterly) as rows, Product ID as
columns, and aggregated Revenue or Quantity as values. A
calculated field, such as Average Revenue per Customer = Total
Revenue / Unique Customers, provides deeper insight. Filters can
refine the analysis by specific regions, products, or time periods.
********** 9 **********
````
