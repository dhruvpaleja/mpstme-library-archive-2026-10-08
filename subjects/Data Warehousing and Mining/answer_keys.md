# Data Warehousing and Mining: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper c8c342bbad66

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CyberSecurity_7010/Data Warehousing and Mining/ANS_Data Warehousing and Mining(702IT0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Data Warehousing and Mining
Date: 16 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a. Given the statement: “A data warehouse is an environment, not a   [5]
product.” State whether you agree or disagree with proper justification.
Agree 2M
Correct Explanation -3 M
A data warehouse is an environment, not a product because it integrates
multiple components such as data sources, ETL processes, storage,
CO-1 ; SO-2 ;
metadata, and analytical tools.
BL-2
It supports decision-making through a structured ecosystem rather than
being a standalone software. Hence, the statement is justified.
• A data warehouse consists of multiple integrated components such as
data sources, ETL tools, storage systems, metadata, and analytical tools
• It is not a single software product but a complete ecosystem supporting
decision-making
• It integrates data from heterogeneous sources
b. DATA STAGING :   [5]
Correct explanation of the data staging process in a data warehouse -5
CO-2 ; SO-2 ;   marks
BL-2
After you have extracted data from various operational systems and from
external sources, you have to prepare the data for storing in the data
warehouse. The extracted data coming from several disparate sources needs
********** 1 **********
--- page 2 ---
to be changed, converted, and made ready in a format that is suitable to be
stored for querying and analysis.
Performs ETL
◦   Extraction
⚫ Select data sources, determine filters
⚫ Automatic replicate
⚫ Create intermediary files
◦ Transformation
⚫ Clean, merge, de-duplicate data
⚫ Covert data types
⚫ Calculate derived data
⚫ Resolve synonyms and homonyms
◦ Loading
◦   Initial loading
◦   Incremental loading
c.   Spatial Data Mining.   [5]
Correct explanation of Spatial data Mining - 5 Marks
• Spatial mining is the process of discovering interesting spatial patterns
referring to the domain of geography or space
Spatial data mining involves extracting patterns and knowledge from
CO-3 ; SO-2 ;   spatial datasets
BL-3   • Works on data containing geographical or location-based attributes
• Identifies spatial relationships such as proximity, distance, and
connectivity
• Key tasks include spatial clustering, classification, association rules,
and trend analysis
• Uses data from GIS, satellite images, maps, and remote sensing
systems
d. Explain confusion matrix in the context of classification models. A data   [5]
mining model is developed to classify emails as spam or genuine(not-
spam). The system produces the following confusion matrix values:
TP = 75, FP = 20
FN = 15, TN = 140
Calculate the accuracy and precision of the above model.
CO-3 ; SO-2 ;
BL-2
Confusion Matrix – 3Marks
Accuracy -1 mark
Precision -1mark
• Confusion matrix is used to evaluate classification model performance
• It compares actual vs predicted values
********** 2 **********
--- page 3 ---
Definitions:
• TP (True Positive): Correctly predicted positive cases = 75
• FP (False Positive): Incorrectly predicted positive cases = 20
• FN (False Negative): Missed positive cases = 15
• TN (True Negative): Correctly predicted negative cases = 140
Accuracy calculation:
Accuracy = (TP + TN) / (TP + TN + FP + FN)
= (75 + 140) / (75 + 140 + 20 + 15)
= 215 / 250 = 0.86 → 86%
Precision calculation:
Precision = TP / (TP + FP)
= 75 / (75 + 20)
= 75 / 95 ≈ 0.789 → 78.9%
a. Consider the scenario of a logistics company that manages deliveries [10]
across regions. Each region contains multiple hubs, and each hub serves
several delivery zones. Delivery agents are assigned to zones. The
objective is to track delivery performance at different levels, such as
region, hub, and zone, and count the number of deliveries completed.
Design an Information Package and a STAR schema for the given
scenario, considering granularity for the location hierarchy, delivery
agents, etc. Assumptions made, if any, to be clearly stated.
Information Package – 4marks
STAR schema - 6Marks
Correct identification of Dimensions
Correct identification of Facts
Q2
CO-1; SO-2;
• Information package defines dimensions, measures, and hierarchy
BL-4
• Measures: number of deliveries, delivery time, success rate
• Dimensions: region → hub → zone (location hierarchy), delivery agent,
time
Steps:
Step 1: Identify business process → delivery tracking
Step 2: Define grain → one record per delivery per zone
Step 3: Identify dimensions → region, hub, zone, agent, time
Step 4: Identify measures → delivery count, performance metrics
Step 5: Design fact table → Delivery_Fact (delivery count, time, status)
Step 6: Create dimension tables → Location, Agent, Time
********** 3 **********
--- page 4 ---
b. Discuss the principle and steps to implement the K-means clustering   [10]
algorithm. Apply K-means Clustering to create 2 clusters for the given
dataset x= {1,2,6,7,8,10,11,15,17,18,20,22}. Use Euclidean distance
metric and assume initial centroid as 1 and 22.
Principle and steps to implement the K-means clustering – 4Marks
Kmeans Clustering numerical – 6 marks
Kmeans Clustering:
K-means partitions data into k clusters based on distance
• Objective: minimize intra-cluster variance
A group of data points whose inter-point distances are small compared
with the distances to points outside of the cluster
Q2
CO-3; SO-2;
BL-3
Steps:
Step 1: Initialize centroids → 1 and 22
Step 2: Assign each data point to nearest centroid using Euclidean distance
Step 3: Form clusters
Step 4: Recalculate centroids (mean of cluster points)
Step 5: Repeat assignment and update until convergence
Assign Cluster Centroids - Until Convergence : - Cluster Assignment
Step - Re-assigning Centroid Step
********** 4 **********
--- page 5 ---
Dataset: {1, 2, 6, 7, 8, 10, 11, 15, 17, 18, 20, 22}
• k = 2
• Initial centroids: C1 = 1, C2 = 22
Step 1: Assign points to nearest centroid (Iteration 1)
Distance = |x − centroid|
Cluster 1 (closer to 1):
• 1, 2, 6, 7, 8, 10, 11
Cluster 2 (closer to 22):
• 15, 17, 18, 20, 22
Step 2: Compute new centroids
• C1 = (1 + 2 + 6 + 7 + 8 + 10 + 11) / 7 = 45 / 7 ≈ 6.43
• C2 = (15 + 17 + 18 + 20 + 22) / 5 = 92 / 5 = 18.4
Step 3: Reassign points (Iteration 2)
Check distances to new centroids:
Cluster 1:
• 1, 2, 6, 7, 8
Cluster 2:
• 10, 11, 15, 17, 18, 20, 22
Differentiate between Operational system and Information system –
Q3   a. 6marks
CO-2; SO-2;   [10]
BL-2   Concept of hypercubes in data warehouse – 4marks
********** 5 **********
--- page 6 ---
Operational system:
• Used for daily transactions (OLTP)
• Real-time processing, normalized data
Informational system:
• Used for analysis (OLAP)
• Historical data, denormalized
Hypercube concept:
• Multidimensional data representation
• Each dimension represents a business perspective (time, location,
product)
• Enables slicing, dicing, drill-down, roll-up
Steps:
• Step 1: Define dimensions
• Step 2: Organize data into multidimensional cube
• Step 3: Perform OLAP operations for analysis
b. Naïve Bayes Classification   [10]
• Based on Bayes theorem with independence assumption
• Calculates posterior probability for each class
Q3   Steps:
CO-3; SO-2;   • Step 1: Calculate prior probabilities P(Pass), P(Fail)
BL-3   • Step 2: Compute likelihoods P(attribute | class)
• Step 3: Multiply probabilities for given input X
• Step 4: Compare posterior probabilities
• Step 5: Assign class with highest probability
 Establish the Prior probability P(Cj) for each class.
********** 6 **********
--- page 7 ---
 Derived Probabilities: Establish the probability P(xi| Cj) for each
attribute xi and class Cj (how often each value occurs in the class
in the training data)
 Conditional probability   P(ti|Cj) is calculated
 Posterior probability P(Cj | ti) is then found
 The class with the highest probability is the one chosen for the
tuple.
a. Explain Type 1 and Type 2 slowly changing dimensions (SCD). – 4marks [10]
Characteristics of a Data Warehouse - 6Marks
 Most dimensions are generally constant over time.
 Many dimensions change slowly.
 Though the key does not change other description and attributes
change slowly over time.
 Dimension table attributes are not overwritten in some types of
changes.
Type 1: Correction of errors
Type 2: Preservation of history
SCD Type 1:
• Overwrites old data
• No history maintained
Q4   SCD Type 2:
CO-1; SO-2;   • Maintains history with new records
BL-3   • Uses surrogate keys and timestamps
DW characteristics:
• Subject-oriented → organized by business subjects
• Integrated → consistent data from multiple sources
• Time-variant → stores historical data The time-variant nature of the data in a
data warehouse
❑ Allows for analysis of the past
❑ Relates information to the present
❑ Enables forecasts for the future
• Non-volatile → stable, read-only
 Data once recorded cannot be updated.
 Data warehouse requires two operations in data accessing.
⚫ Initial loading of data
⚫ Incremental loading of data
********** 7 **********
--- page 8 ---
Steps
• Step 1: Collect historical data
• Step 2: Ensure consistency and integration
• Step 3: Enable trend analysis
• Step 4: Support strategic decision-making
b. Decision Tree (DT) algorithm.   [10]
Decision tree disadvantages:
• Overfitting
• Sensitive to noise
• Bias toward attributes with more values
ID3 algorithm:
Q4
• Uses entropy and information gain
CO-2; SO-2;
BL-3
Steps:
Step 1: Compute entropy of dataset
Step 2: Calculate information gain for each attribute
Step 3: Select attribute with highest gain as root
Step 4: Split dataset
Step 5: Repeat recursively
Explain the concept of association rule mining. – 4marks   [10]
a.
Numerical – 6marks
Apriori algorithm
• Used for association rule mining
Q5
• Finds frequent itemsets and strong rules
CO-3; SO-2;
BL-4
Steps:
• Step 1: Generate candidate itemsets
• Step 2: Calculate support
• Step 3: Prune itemsets below threshold
• Step 4: Generate higher-order itemsets
• Step 5: Calculate confidence for rules
• Step 6: Select strong rules
********** 8 **********
--- page 9 ---
Transactions = 5
• Minimum support = 30% → 0.3 × 5 = 1.5 → support count ≥ 2
• Minimum confidence = 60%
Step 1: Generate 1-itemsets (L1)
Count support:
• Shirt → 3 (T1, T2, T4)
• Jeans → 4 (T1, T2, T3, T5)
• Belt → 3 (T1, T4, T5)
• Shoes → 2 (T3, T4)
Frequent 1-itemsets (support ≥ 2):
• {Shirt}, {Jeans}, {Belt}, {Shoes}
Step 2: Generate 2-itemsets (C2 → L2)
Possible pairs and support:
• {Shirt, Jeans} → 2 (T1, T2)
• {Shirt, Belt} → 2 (T1, T4)
• {Shirt, Shoes} → 1 (T4)
• {Jeans, Belt} → 2 (T1, T5)
• {Jeans, Shoes} → 1 (T3)
• {Belt, Shoes} → 1 (T4)
Frequent 2-itemsets:
• {Shirt, Jeans}, {Shirt, Belt}, {Jeans, Belt}
Final frequent itemsets
• L1: {Shirt}, {Jeans}, {Belt}, {Shoes}
Shirt → Belt
Confidence = 2 / 3 ≈ 66.7%
Belt → Jeans
Confidence = 2 / 3 ≈ 66.7%
b. Essential differences between the MOLAP and ROLAP architectural [10]
models alongwith neat diagram – 10 marks
Q5
CO-1,CO-3;
SO-2; BL- 2   MOLAP:
• Data stored in multidimensional cube
• Fast query performance
• Limited scalability
********** 9 **********
--- page 10 ---
ROLAP:
• Data stored in relational tables
• Scalable but slower queries
Steps:
• Step 1: Store data (cube vs relational)
• Step 2: Process queries
• Step 3: Perform OLAP operations
ROLAP
MOLAP
********** 10 **********
--- page 11 ---
ROLAP   MOLAP
Stored as relational tables Stored as relational tables
Detailed   and   light Various summary   data   kept   in
summary   proprietary
data available   databases (MDDBs)
Very large data volumes Moderate data volumes
All data access from the Summary data access from MDDB
warehouse storage.   detailed data access from warehouse.
a. Consider the scenario of a hospital that wants to classify patients as   [10]
high-risk or low-risk based on blood pressure and cholesterol level.
Blood Pressure   Cholesterol   Risk
(X1)   (X2)
150   240   High
145   230   High
Q6
CO-2,CO-3;   110   180   Low
SO-2;   105   170   Low
BL-3
A new patient has Blood Pressure = 120 and Cholesterol = 200.
Apply KNN using Euclidean distance (k = 3) to classify the risk level.
• Instance-based learning algorithm
• Classifies based on nearest neighbors
********** 11 **********
--- page 12 ---
Steps:
• Step 1: Choose k = 3
• Step 2: Calculate Euclidean distance from new point
• Step 3: Identify 3 nearest neighbors
• Step 4: Perform majority voting
• Step 5: Assign class
Outcome: Risk classified as High or Low
Final classification
• Predicted class = Low risk
• The new patient is classified as Low risk based on nearest neighbors
• KNN assigns class based on majority among closest data points
b. Data Mining Techniques ;   [10]
Q6
CO-3; SO-2;
BL- 3
Categorization of data mining techniques – 5 Marks
Regression unknown value prediction – 5 marks
• Models relationship between variables
Steps:
• Step 1: Compute mean of X and Y
• Step 2: Calculate slope (m)
• Step 3: Calculate intercept (c)
• Step 4: Form equation y = mx + c
• Step 5: Predict value at X = 10
Outcome: Predicted relief value
********** 12 **********
--- page 13 ---
a. Web content Mining - 5Marks   [10]
and Web structure mining -5marks
and describe its significance in extracting web data.
Web content mining:
• Extracts information from web pages
• Extends work of basic search engines
•   Search Engines
• IR application
• Keyword based
•   Similarity between query and document
Web structure mining:
Q7
• Analyzes link structure between pages
CO-2,3; SO-2;
BL-2
• Mine structure (links, graph) of the Web
• Techniques
• PageRank
• CLEVER
•   Create a model of the Web organization.
• May be combined with content mining to more effectively retrieve
important pages
Steps:
• Step 1: Collect web data
• Step 2: Preprocess data
• Step 3: Apply mining techniques
• Step 4: Extract patterns
Q7   b. KDD Process   [10]
CO-1,2-; SO-
2; BL-4
********** 13 **********
--- page 14 ---
• Selection: Obtain data from various sources.
• Preprocessing: Cleanse data.
• Transformation: Convert to common format.
Transform to new format.
• Data Mining: Obtain desired results.
• Interpretation/Evaluation: Present results to user
in meaningful manner.
Application (supermarket):
• Analyze purchase data
• Discover buying patterns
• Improve sales strategies
KDD Process- 8marks
KDD Scenario Application - 2marks
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper cf7a162c997d

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_IT_7001/Data Warehousing and Mining/ANS_Data Warehousing and Mining(702IT0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Data Warehousing and Mining
Date: 16 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a. Given the statement: “A data warehouse is an environment, not a   [5]
product.” State whether you agree or disagree with proper justification.
Agree 2M
Correct Explanation -3 M
A data warehouse is an environment, not a product because it integrates
multiple components such as data sources, ETL processes, storage,
CO-1 ; SO-2 ;
metadata, and analytical tools.
BL-2
It supports decision-making through a structured ecosystem rather than
being a standalone software. Hence, the statement is justified.
• A data warehouse consists of multiple integrated components such as
data sources, ETL tools, storage systems, metadata, and analytical tools
• It is not a single software product but a complete ecosystem supporting
decision-making
• It integrates data from heterogeneous sources
b. DATA STAGING :   [5]
Correct explanation of the data staging process in a data warehouse -5
CO-2 ; SO-2 ;   marks
BL-2
After you have extracted data from various operational systems and from
external sources, you have to prepare the data for storing in the data
warehouse. The extracted data coming from several disparate sources needs
********** 1 **********
--- page 2 ---
to be changed, converted, and made ready in a format that is suitable to be
stored for querying and analysis.
Performs ETL
◦   Extraction
⚫ Select data sources, determine filters
⚫ Automatic replicate
⚫ Create intermediary files
◦ Transformation
⚫ Clean, merge, de-duplicate data
⚫ Covert data types
⚫ Calculate derived data
⚫ Resolve synonyms and homonyms
◦ Loading
◦   Initial loading
◦   Incremental loading
c.   Spatial Data Mining.   [5]
Correct explanation of Spatial data Mining - 5 Marks
• Spatial mining is the process of discovering interesting spatial patterns
referring to the domain of geography or space
Spatial data mining involves extracting patterns and knowledge from
CO-3 ; SO-2 ;   spatial datasets
BL-3   • Works on data containing geographical or location-based attributes
• Identifies spatial relationships such as proximity, distance, and
connectivity
• Key tasks include spatial clustering, classification, association rules,
and trend analysis
• Uses data from GIS, satellite images, maps, and remote sensing
systems
d. Explain confusion matrix in the context of classification models. A data   [5]
mining model is developed to classify emails as spam or genuine(not-
spam). The system produces the following confusion matrix values:
TP = 75, FP = 20
FN = 15, TN = 140
Calculate the accuracy and precision of the above model.
CO-3 ; SO-2 ;
BL-2
Confusion Matrix – 3Marks
Accuracy -1 mark
Precision -1mark
• Confusion matrix is used to evaluate classification model performance
• It compares actual vs predicted values
********** 2 **********
--- page 3 ---
Definitions:
• TP (True Positive): Correctly predicted positive cases = 75
• FP (False Positive): Incorrectly predicted positive cases = 20
• FN (False Negative): Missed positive cases = 15
• TN (True Negative): Correctly predicted negative cases = 140
Accuracy calculation:
Accuracy = (TP + TN) / (TP + TN + FP + FN)
= (75 + 140) / (75 + 140 + 20 + 15)
= 215 / 250 = 0.86 → 86%
Precision calculation:
Precision = TP / (TP + FP)
= 75 / (75 + 20)
= 75 / 95 ≈ 0.789 → 78.9%
a. Consider the scenario of a logistics company that manages deliveries [10]
across regions. Each region contains multiple hubs, and each hub serves
several delivery zones. Delivery agents are assigned to zones. The
objective is to track delivery performance at different levels, such as
region, hub, and zone, and count the number of deliveries completed.
Design an Information Package and a STAR schema for the given
scenario, considering granularity for the location hierarchy, delivery
agents, etc. Assumptions made, if any, to be clearly stated.
Information Package – 4marks
STAR schema - 6Marks
Correct identification of Dimensions
Correct identification of Facts
Q2
CO-1; SO-2;
• Information package defines dimensions, measures, and hierarchy
BL-4
• Measures: number of deliveries, delivery time, success rate
• Dimensions: region → hub → zone (location hierarchy), delivery agent,
time
Steps:
Step 1: Identify business process → delivery tracking
Step 2: Define grain → one record per delivery per zone
Step 3: Identify dimensions → region, hub, zone, agent, time
Step 4: Identify measures → delivery count, performance metrics
Step 5: Design fact table → Delivery_Fact (delivery count, time, status)
Step 6: Create dimension tables → Location, Agent, Time
********** 3 **********
--- page 4 ---
b. Discuss the principle and steps to implement the K-means clustering   [10]
algorithm. Apply K-means Clustering to create 2 clusters for the given
dataset x= {1,2,6,7,8,10,11,15,17,18,20,22}. Use Euclidean distance
metric and assume initial centroid as 1 and 22.
Principle and steps to implement the K-means clustering – 4Marks
Kmeans Clustering numerical – 6 marks
Kmeans Clustering:
K-means partitions data into k clusters based on distance
• Objective: minimize intra-cluster variance
A group of data points whose inter-point distances are small compared
with the distances to points outside of the cluster
Q2
CO-3; SO-2;
BL-3
Steps:
Step 1: Initialize centroids → 1 and 22
Step 2: Assign each data point to nearest centroid using Euclidean distance
Step 3: Form clusters
Step 4: Recalculate centroids (mean of cluster points)
Step 5: Repeat assignment and update until convergence
Assign Cluster Centroids - Until Convergence : - Cluster Assignment
Step - Re-assigning Centroid Step
********** 4 **********
--- page 5 ---
Dataset: {1, 2, 6, 7, 8, 10, 11, 15, 17, 18, 20, 22}
• k = 2
• Initial centroids: C1 = 1, C2 = 22
Step 1: Assign points to nearest centroid (Iteration 1)
Distance = |x − centroid|
Cluster 1 (closer to 1):
• 1, 2, 6, 7, 8, 10, 11
Cluster 2 (closer to 22):
• 15, 17, 18, 20, 22
Step 2: Compute new centroids
• C1 = (1 + 2 + 6 + 7 + 8 + 10 + 11) / 7 = 45 / 7 ≈ 6.43
• C2 = (15 + 17 + 18 + 20 + 22) / 5 = 92 / 5 = 18.4
Step 3: Reassign points (Iteration 2)
Check distances to new centroids:
Cluster 1:
• 1, 2, 6, 7, 8
Cluster 2:
• 10, 11, 15, 17, 18, 20, 22
Differentiate between Operational system and Information system –
Q3   a. 6marks
CO-2; SO-2;   [10]
BL-2   Concept of hypercubes in data warehouse – 4marks
********** 5 **********
--- page 6 ---
Operational system:
• Used for daily transactions (OLTP)
• Real-time processing, normalized data
Informational system:
• Used for analysis (OLAP)
• Historical data, denormalized
Hypercube concept:
• Multidimensional data representation
• Each dimension represents a business perspective (time, location,
product)
• Enables slicing, dicing, drill-down, roll-up
Steps:
• Step 1: Define dimensions
• Step 2: Organize data into multidimensional cube
• Step 3: Perform OLAP operations for analysis
b. Naïve Bayes Classification   [10]
• Based on Bayes theorem with independence assumption
• Calculates posterior probability for each class
Q3   Steps:
CO-3; SO-2;   • Step 1: Calculate prior probabilities P(Pass), P(Fail)
BL-3   • Step 2: Compute likelihoods P(attribute | class)
• Step 3: Multiply probabilities for given input X
• Step 4: Compare posterior probabilities
• Step 5: Assign class with highest probability
 Establish the Prior probability P(Cj) for each class.
********** 6 **********
--- page 7 ---
 Derived Probabilities: Establish the probability P(xi| Cj) for each
attribute xi and class Cj (how often each value occurs in the class
in the training data)
 Conditional probability   P(ti|Cj) is calculated
 Posterior probability P(Cj | ti) is then found
 The class with the highest probability is the one chosen for the
tuple.
a. Explain Type 1 and Type 2 slowly changing dimensions (SCD). – 4marks [10]
Characteristics of a Data Warehouse - 6Marks
 Most dimensions are generally constant over time.
 Many dimensions change slowly.
 Though the key does not change other description and attributes
change slowly over time.
 Dimension table attributes are not overwritten in some types of
changes.
Type 1: Correction of errors
Type 2: Preservation of history
SCD Type 1:
• Overwrites old data
• No history maintained
Q4   SCD Type 2:
CO-1; SO-2;   • Maintains history with new records
BL-3   • Uses surrogate keys and timestamps
DW characteristics:
• Subject-oriented → organized by business subjects
• Integrated → consistent data from multiple sources
• Time-variant → stores historical data The time-variant nature of the data in a
data warehouse
❑ Allows for analysis of the past
❑ Relates information to the present
❑ Enables forecasts for the future
• Non-volatile → stable, read-only
 Data once recorded cannot be updated.
 Data warehouse requires two operations in data accessing.
⚫ Initial loading of data
⚫ Incremental loading of data
********** 7 **********
--- page 8 ---
Steps
• Step 1: Collect historical data
• Step 2: Ensure consistency and integration
• Step 3: Enable trend analysis
• Step 4: Support strategic decision-making
b. Decision Tree (DT) algorithm.   [10]
Decision tree disadvantages:
• Overfitting
• Sensitive to noise
• Bias toward attributes with more values
ID3 algorithm:
Q4
• Uses entropy and information gain
CO-2; SO-2;
BL-3
Steps:
Step 1: Compute entropy of dataset
Step 2: Calculate information gain for each attribute
Step 3: Select attribute with highest gain as root
Step 4: Split dataset
Step 5: Repeat recursively
Explain the concept of association rule mining. – 4marks   [10]
a.
Numerical – 6marks
Apriori algorithm
• Used for association rule mining
Q5
• Finds frequent itemsets and strong rules
CO-3; SO-2;
BL-4
Steps:
• Step 1: Generate candidate itemsets
• Step 2: Calculate support
• Step 3: Prune itemsets below threshold
• Step 4: Generate higher-order itemsets
• Step 5: Calculate confidence for rules
• Step 6: Select strong rules
********** 8 **********
--- page 9 ---
Transactions = 5
• Minimum support = 30% → 0.3 × 5 = 1.5 → support count ≥ 2
• Minimum confidence = 60%
Step 1: Generate 1-itemsets (L1)
Count support:
• Shirt → 3 (T1, T2, T4)
• Jeans → 4 (T1, T2, T3, T5)
• Belt → 3 (T1, T4, T5)
• Shoes → 2 (T3, T4)
Frequent 1-itemsets (support ≥ 2):
• {Shirt}, {Jeans}, {Belt}, {Shoes}
Step 2: Generate 2-itemsets (C2 → L2)
Possible pairs and support:
• {Shirt, Jeans} → 2 (T1, T2)
• {Shirt, Belt} → 2 (T1, T4)
• {Shirt, Shoes} → 1 (T4)
• {Jeans, Belt} → 2 (T1, T5)
• {Jeans, Shoes} → 1 (T3)
• {Belt, Shoes} → 1 (T4)
Frequent 2-itemsets:
• {Shirt, Jeans}, {Shirt, Belt}, {Jeans, Belt}
Final frequent itemsets
• L1: {Shirt}, {Jeans}, {Belt}, {Shoes}
Shirt → Belt
Confidence = 2 / 3 ≈ 66.7%
Belt → Jeans
Confidence = 2 / 3 ≈ 66.7%
b. Essential differences between the MOLAP and ROLAP architectural [10]
models alongwith neat diagram – 10 marks
Q5
CO-1,CO-3;
SO-2; BL- 2   MOLAP:
• Data stored in multidimensional cube
• Fast query performance
• Limited scalability
********** 9 **********
--- page 10 ---
ROLAP:
• Data stored in relational tables
• Scalable but slower queries
Steps:
• Step 1: Store data (cube vs relational)
• Step 2: Process queries
• Step 3: Perform OLAP operations
ROLAP
MOLAP
********** 10 **********
--- page 11 ---
ROLAP   MOLAP
Stored as relational tables Stored as relational tables
Detailed   and   light Various summary   data   kept   in
summary   proprietary
data available   databases (MDDBs)
Very large data volumes Moderate data volumes
All data access from the Summary data access from MDDB
warehouse storage.   detailed data access from warehouse.
a. Consider the scenario of a hospital that wants to classify patients as   [10]
high-risk or low-risk based on blood pressure and cholesterol level.
Blood Pressure   Cholesterol   Risk
(X1)   (X2)
150   240   High
145   230   High
Q6
CO-2,CO-3;   110   180   Low
SO-2;   105   170   Low
BL-3
A new patient has Blood Pressure = 120 and Cholesterol = 200.
Apply KNN using Euclidean distance (k = 3) to classify the risk level.
• Instance-based learning algorithm
• Classifies based on nearest neighbors
********** 11 **********
--- page 12 ---
Steps:
• Step 1: Choose k = 3
• Step 2: Calculate Euclidean distance from new point
• Step 3: Identify 3 nearest neighbors
• Step 4: Perform majority voting
• Step 5: Assign class
Outcome: Risk classified as High or Low
Final classification
• Predicted class = Low risk
• The new patient is classified as Low risk based on nearest neighbors
• KNN assigns class based on majority among closest data points
b. Data Mining Techniques ;   [10]
Q6
CO-3; SO-2;
BL- 3
Categorization of data mining techniques – 5 Marks
Regression unknown value prediction – 5 marks
• Models relationship between variables
Steps:
• Step 1: Compute mean of X and Y
• Step 2: Calculate slope (m)
• Step 3: Calculate intercept (c)
• Step 4: Form equation y = mx + c
• Step 5: Predict value at X = 10
Outcome: Predicted relief value
********** 12 **********
--- page 13 ---
a. Web content Mining - 5Marks   [10]
and Web structure mining -5marks
and describe its significance in extracting web data.
Web content mining:
• Extracts information from web pages
• Extends work of basic search engines
•   Search Engines
• IR application
• Keyword based
•   Similarity between query and document
Web structure mining:
Q7
• Analyzes link structure between pages
CO-2,3; SO-2;
BL-2
• Mine structure (links, graph) of the Web
• Techniques
• PageRank
• CLEVER
•   Create a model of the Web organization.
• May be combined with content mining to more effectively retrieve
important pages
Steps:
• Step 1: Collect web data
• Step 2: Preprocess data
• Step 3: Apply mining techniques
• Step 4: Extract patterns
Q7   b. KDD Process   [10]
CO-1,2-; SO-
2; BL-4
********** 13 **********
--- page 14 ---
• Selection: Obtain data from various sources.
• Preprocessing: Cleanse data.
• Transformation: Convert to common format.
Transform to new format.
• Data Mining: Obtain desired results.
• Interpretation/Evaluation: Present results to user
in meaningful manner.
Application (supermarket):
• Analyze purchase data
• Discover buying patterns
• Improve sales strategies
KDD Process- 8marks
KDD Scenario Application - 2marks
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 2c3ec638223b

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_IT_7041/Data Warehousing and Mining/ANS_Data Warehousing and Mining(702IT0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Data Warehousing and Mining
Date: 16 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a. Given the statement: “A data warehouse is an environment, not a   [5]
product.” State whether you agree or disagree with proper justification.
Agree 2M
Correct Explanation -3 M
A data warehouse is an environment, not a product because it integrates
multiple components such as data sources, ETL processes, storage,
CO-1 ; SO-2 ;
metadata, and analytical tools.
BL-2
It supports decision-making through a structured ecosystem rather than
being a standalone software. Hence, the statement is justified.
• A data warehouse consists of multiple integrated components such as
data sources, ETL tools, storage systems, metadata, and analytical tools
• It is not a single software product but a complete ecosystem supporting
decision-making
• It integrates data from heterogeneous sources
b. DATA STAGING :   [5]
Correct explanation of the data staging process in a data warehouse -5
CO-2 ; SO-2 ;   marks
BL-2
After you have extracted data from various operational systems and from
external sources, you have to prepare the data for storing in the data
warehouse. The extracted data coming from several disparate sources needs
********** 1 **********
--- page 2 ---
to be changed, converted, and made ready in a format that is suitable to be
stored for querying and analysis.
Performs ETL
◦   Extraction
⚫ Select data sources, determine filters
⚫ Automatic replicate
⚫ Create intermediary files
◦ Transformation
⚫ Clean, merge, de-duplicate data
⚫ Covert data types
⚫ Calculate derived data
⚫ Resolve synonyms and homonyms
◦ Loading
◦   Initial loading
◦   Incremental loading
c.   Spatial Data Mining.   [5]
Correct explanation of Spatial data Mining - 5 Marks
• Spatial mining is the process of discovering interesting spatial patterns
referring to the domain of geography or space
Spatial data mining involves extracting patterns and knowledge from
CO-3 ; SO-2 ;   spatial datasets
BL-3   • Works on data containing geographical or location-based attributes
• Identifies spatial relationships such as proximity, distance, and
connectivity
• Key tasks include spatial clustering, classification, association rules,
and trend analysis
• Uses data from GIS, satellite images, maps, and remote sensing
systems
d. Explain confusion matrix in the context of classification models. A data   [5]
mining model is developed to classify emails as spam or genuine(not-
spam). The system produces the following confusion matrix values:
TP = 75, FP = 20
FN = 15, TN = 140
Calculate the accuracy and precision of the above model.
CO-3 ; SO-2 ;
BL-2
Confusion Matrix – 3Marks
Accuracy -1 mark
Precision -1mark
• Confusion matrix is used to evaluate classification model performance
• It compares actual vs predicted values
********** 2 **********
--- page 3 ---
Definitions:
• TP (True Positive): Correctly predicted positive cases = 75
• FP (False Positive): Incorrectly predicted positive cases = 20
• FN (False Negative): Missed positive cases = 15
• TN (True Negative): Correctly predicted negative cases = 140
Accuracy calculation:
Accuracy = (TP + TN) / (TP + TN + FP + FN)
= (75 + 140) / (75 + 140 + 20 + 15)
= 215 / 250 = 0.86 → 86%
Precision calculation:
Precision = TP / (TP + FP)
= 75 / (75 + 20)
= 75 / 95 ≈ 0.789 → 78.9%
a. Consider the scenario of a logistics company that manages deliveries [10]
across regions. Each region contains multiple hubs, and each hub serves
several delivery zones. Delivery agents are assigned to zones. The
objective is to track delivery performance at different levels, such as
region, hub, and zone, and count the number of deliveries completed.
Design an Information Package and a STAR schema for the given
scenario, considering granularity for the location hierarchy, delivery
agents, etc. Assumptions made, if any, to be clearly stated.
Information Package – 4marks
STAR schema - 6Marks
Correct identification of Dimensions
Correct identification of Facts
Q2
CO-1; SO-2;
• Information package defines dimensions, measures, and hierarchy
BL-4
• Measures: number of deliveries, delivery time, success rate
• Dimensions: region → hub → zone (location hierarchy), delivery agent,
time
Steps:
Step 1: Identify business process → delivery tracking
Step 2: Define grain → one record per delivery per zone
Step 3: Identify dimensions → region, hub, zone, agent, time
Step 4: Identify measures → delivery count, performance metrics
Step 5: Design fact table → Delivery_Fact (delivery count, time, status)
Step 6: Create dimension tables → Location, Agent, Time
********** 3 **********
--- page 4 ---
b. Discuss the principle and steps to implement the K-means clustering   [10]
algorithm. Apply K-means Clustering to create 2 clusters for the given
dataset x= {1,2,6,7,8,10,11,15,17,18,20,22}. Use Euclidean distance
metric and assume initial centroid as 1 and 22.
Principle and steps to implement the K-means clustering – 4Marks
Kmeans Clustering numerical – 6 marks
Kmeans Clustering:
K-means partitions data into k clusters based on distance
• Objective: minimize intra-cluster variance
A group of data points whose inter-point distances are small compared
with the distances to points outside of the cluster
Q2
CO-3; SO-2;
BL-3
Steps:
Step 1: Initialize centroids → 1 and 22
Step 2: Assign each data point to nearest centroid using Euclidean distance
Step 3: Form clusters
Step 4: Recalculate centroids (mean of cluster points)
Step 5: Repeat assignment and update until convergence
Assign Cluster Centroids - Until Convergence : - Cluster Assignment
Step - Re-assigning Centroid Step
********** 4 **********
--- page 5 ---
Dataset: {1, 2, 6, 7, 8, 10, 11, 15, 17, 18, 20, 22}
• k = 2
• Initial centroids: C1 = 1, C2 = 22
Step 1: Assign points to nearest centroid (Iteration 1)
Distance = |x − centroid|
Cluster 1 (closer to 1):
• 1, 2, 6, 7, 8, 10, 11
Cluster 2 (closer to 22):
• 15, 17, 18, 20, 22
Step 2: Compute new centroids
• C1 = (1 + 2 + 6 + 7 + 8 + 10 + 11) / 7 = 45 / 7 ≈ 6.43
• C2 = (15 + 17 + 18 + 20 + 22) / 5 = 92 / 5 = 18.4
Step 3: Reassign points (Iteration 2)
Check distances to new centroids:
Cluster 1:
• 1, 2, 6, 7, 8
Cluster 2:
• 10, 11, 15, 17, 18, 20, 22
Differentiate between Operational system and Information system –
Q3   a. 6marks
CO-2; SO-2;   [10]
BL-2   Concept of hypercubes in data warehouse – 4marks
********** 5 **********
--- page 6 ---
Operational system:
• Used for daily transactions (OLTP)
• Real-time processing, normalized data
Informational system:
• Used for analysis (OLAP)
• Historical data, denormalized
Hypercube concept:
• Multidimensional data representation
• Each dimension represents a business perspective (time, location,
product)
• Enables slicing, dicing, drill-down, roll-up
Steps:
• Step 1: Define dimensions
• Step 2: Organize data into multidimensional cube
• Step 3: Perform OLAP operations for analysis
b. Naïve Bayes Classification   [10]
• Based on Bayes theorem with independence assumption
• Calculates posterior probability for each class
Q3   Steps:
CO-3; SO-2;   • Step 1: Calculate prior probabilities P(Pass), P(Fail)
BL-3   • Step 2: Compute likelihoods P(attribute | class)
• Step 3: Multiply probabilities for given input X
• Step 4: Compare posterior probabilities
• Step 5: Assign class with highest probability
 Establish the Prior probability P(Cj) for each class.
********** 6 **********
--- page 7 ---
 Derived Probabilities: Establish the probability P(xi| Cj) for each
attribute xi and class Cj (how often each value occurs in the class
in the training data)
 Conditional probability   P(ti|Cj) is calculated
 Posterior probability P(Cj | ti) is then found
 The class with the highest probability is the one chosen for the
tuple.
a. Explain Type 1 and Type 2 slowly changing dimensions (SCD). – 4marks [10]
Characteristics of a Data Warehouse - 6Marks
 Most dimensions are generally constant over time.
 Many dimensions change slowly.
 Though the key does not change other description and attributes
change slowly over time.
 Dimension table attributes are not overwritten in some types of
changes.
Type 1: Correction of errors
Type 2: Preservation of history
SCD Type 1:
• Overwrites old data
• No history maintained
Q4   SCD Type 2:
CO-1; SO-2;   • Maintains history with new records
BL-3   • Uses surrogate keys and timestamps
DW characteristics:
• Subject-oriented → organized by business subjects
• Integrated → consistent data from multiple sources
• Time-variant → stores historical data The time-variant nature of the data in a
data warehouse
❑ Allows for analysis of the past
❑ Relates information to the present
❑ Enables forecasts for the future
• Non-volatile → stable, read-only
 Data once recorded cannot be updated.
 Data warehouse requires two operations in data accessing.
⚫ Initial loading of data
⚫ Incremental loading of data
********** 7 **********
--- page 8 ---
Steps
• Step 1: Collect historical data
• Step 2: Ensure consistency and integration
• Step 3: Enable trend analysis
• Step 4: Support strategic decision-making
b. Decision Tree (DT) algorithm.   [10]
Decision tree disadvantages:
• Overfitting
• Sensitive to noise
• Bias toward attributes with more values
ID3 algorithm:
Q4
• Uses entropy and information gain
CO-2; SO-2;
BL-3
Steps:
Step 1: Compute entropy of dataset
Step 2: Calculate information gain for each attribute
Step 3: Select attribute with highest gain as root
Step 4: Split dataset
Step 5: Repeat recursively
Explain the concept of association rule mining. – 4marks   [10]
a.
Numerical – 6marks
Apriori algorithm
• Used for association rule mining
Q5
• Finds frequent itemsets and strong rules
CO-3; SO-2;
BL-4
Steps:
• Step 1: Generate candidate itemsets
• Step 2: Calculate support
• Step 3: Prune itemsets below threshold
• Step 4: Generate higher-order itemsets
• Step 5: Calculate confidence for rules
• Step 6: Select strong rules
********** 8 **********
--- page 9 ---
Transactions = 5
• Minimum support = 30% → 0.3 × 5 = 1.5 → support count ≥ 2
• Minimum confidence = 60%
Step 1: Generate 1-itemsets (L1)
Count support:
• Shirt → 3 (T1, T2, T4)
• Jeans → 4 (T1, T2, T3, T5)
• Belt → 3 (T1, T4, T5)
• Shoes → 2 (T3, T4)
Frequent 1-itemsets (support ≥ 2):
• {Shirt}, {Jeans}, {Belt}, {Shoes}
Step 2: Generate 2-itemsets (C2 → L2)
Possible pairs and support:
• {Shirt, Jeans} → 2 (T1, T2)
• {Shirt, Belt} → 2 (T1, T4)
• {Shirt, Shoes} → 1 (T4)
• {Jeans, Belt} → 2 (T1, T5)
• {Jeans, Shoes} → 1 (T3)
• {Belt, Shoes} → 1 (T4)
Frequent 2-itemsets:
• {Shirt, Jeans}, {Shirt, Belt}, {Jeans, Belt}
Final frequent itemsets
• L1: {Shirt}, {Jeans}, {Belt}, {Shoes}
Shirt → Belt
Confidence = 2 / 3 ≈ 66.7%
Belt → Jeans
Confidence = 2 / 3 ≈ 66.7%
b. Essential differences between the MOLAP and ROLAP architectural [10]
models alongwith neat diagram – 10 marks
Q5
CO-1,CO-3;
SO-2; BL- 2   MOLAP:
• Data stored in multidimensional cube
• Fast query performance
• Limited scalability
********** 9 **********
--- page 10 ---
ROLAP:
• Data stored in relational tables
• Scalable but slower queries
Steps:
• Step 1: Store data (cube vs relational)
• Step 2: Process queries
• Step 3: Perform OLAP operations
ROLAP
MOLAP
********** 10 **********
--- page 11 ---
ROLAP   MOLAP
Stored as relational tables Stored as relational tables
Detailed   and   light Various summary   data   kept   in
summary   proprietary
data available   databases (MDDBs)
Very large data volumes Moderate data volumes
All data access from the Summary data access from MDDB
warehouse storage.   detailed data access from warehouse.
a. Consider the scenario of a hospital that wants to classify patients as   [10]
high-risk or low-risk based on blood pressure and cholesterol level.
Blood Pressure   Cholesterol   Risk
(X1)   (X2)
150   240   High
145   230   High
Q6
CO-2,CO-3;   110   180   Low
SO-2;   105   170   Low
BL-3
A new patient has Blood Pressure = 120 and Cholesterol = 200.
Apply KNN using Euclidean distance (k = 3) to classify the risk level.
• Instance-based learning algorithm
• Classifies based on nearest neighbors
********** 11 **********
--- page 12 ---
Steps:
• Step 1: Choose k = 3
• Step 2: Calculate Euclidean distance from new point
• Step 3: Identify 3 nearest neighbors
• Step 4: Perform majority voting
• Step 5: Assign class
Outcome: Risk classified as High or Low
Final classification
• Predicted class = Low risk
• The new patient is classified as Low risk based on nearest neighbors
• KNN assigns class based on majority among closest data points
b. Data Mining Techniques ;   [10]
Q6
CO-3; SO-2;
BL- 3
Categorization of data mining techniques – 5 Marks
Regression unknown value prediction – 5 marks
• Models relationship between variables
Steps:
• Step 1: Compute mean of X and Y
• Step 2: Calculate slope (m)
• Step 3: Calculate intercept (c)
• Step 4: Form equation y = mx + c
• Step 5: Predict value at X = 10
Outcome: Predicted relief value
********** 12 **********
--- page 13 ---
a. Web content Mining - 5Marks   [10]
and Web structure mining -5marks
and describe its significance in extracting web data.
Web content mining:
• Extracts information from web pages
• Extends work of basic search engines
•   Search Engines
• IR application
• Keyword based
•   Similarity between query and document
Web structure mining:
Q7
• Analyzes link structure between pages
CO-2,3; SO-2;
BL-2
• Mine structure (links, graph) of the Web
• Techniques
• PageRank
• CLEVER
•   Create a model of the Web organization.
• May be combined with content mining to more effectively retrieve
important pages
Steps:
• Step 1: Collect web data
• Step 2: Preprocess data
• Step 3: Apply mining techniques
• Step 4: Extract patterns
Q7   b. KDD Process   [10]
CO-1,2-; SO-
2; BL-4
********** 13 **********
--- page 14 ---
• Selection: Obtain data from various sources.
• Preprocessing: Cleanse data.
• Transformation: Convert to common format.
Transform to new format.
• Data Mining: Obtain desired results.
• Interpretation/Evaluation: Present results to user
in meaningful manner.
Application (supermarket):
• Analyze purchase data
• Discover buying patterns
• Improve sales strategies
KDD Process- 8marks
KDD Scenario Application - 2marks
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper f16f8bbe4af1

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_IT_7037/Data Warehousing and Mining/ANS_Data Warehousing and Mining(702IT0C012)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Data Warehousing and Mining
Date: 16 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a. Given the statement: “A data warehouse is an environment, not a   [5]
product.” State whether you agree or disagree with proper justification.
Agree 2M
Correct Explanation -3 M
A data warehouse is an environment, not a product because it integrates
multiple components such as data sources, ETL processes, storage,
CO-1 ; SO-2 ;
metadata, and analytical tools.
BL-2
It supports decision-making through a structured ecosystem rather than
being a standalone software. Hence, the statement is justified.
• A data warehouse consists of multiple integrated components such as
data sources, ETL tools, storage systems, metadata, and analytical tools
• It is not a single software product but a complete ecosystem supporting
decision-making
• It integrates data from heterogeneous sources
b. DATA STAGING :   [5]
Correct explanation of the data staging process in a data warehouse -5
CO-2 ; SO-2 ;   marks
BL-2
After you have extracted data from various operational systems and from
external sources, you have to prepare the data for storing in the data
warehouse. The extracted data coming from several disparate sources needs
********** 1 **********
--- page 2 ---
to be changed, converted, and made ready in a format that is suitable to be
stored for querying and analysis.
Performs ETL
◦   Extraction
⚫ Select data sources, determine filters
⚫ Automatic replicate
⚫ Create intermediary files
◦ Transformation
⚫ Clean, merge, de-duplicate data
⚫ Covert data types
⚫ Calculate derived data
⚫ Resolve synonyms and homonyms
◦ Loading
◦   Initial loading
◦   Incremental loading
c.   Spatial Data Mining.   [5]
Correct explanation of Spatial data Mining - 5 Marks
• Spatial mining is the process of discovering interesting spatial patterns
referring to the domain of geography or space
Spatial data mining involves extracting patterns and knowledge from
CO-3 ; SO-2 ;   spatial datasets
BL-3   • Works on data containing geographical or location-based attributes
• Identifies spatial relationships such as proximity, distance, and
connectivity
• Key tasks include spatial clustering, classification, association rules,
and trend analysis
• Uses data from GIS, satellite images, maps, and remote sensing
systems
d. Explain confusion matrix in the context of classification models. A data   [5]
mining model is developed to classify emails as spam or genuine(not-
spam). The system produces the following confusion matrix values:
TP = 75, FP = 20
FN = 15, TN = 140
Calculate the accuracy and precision of the above model.
CO-3 ; SO-2 ;
BL-2
Confusion Matrix – 3Marks
Accuracy -1 mark
Precision -1mark
• Confusion matrix is used to evaluate classification model performance
• It compares actual vs predicted values
********** 2 **********
--- page 3 ---
Definitions:
• TP (True Positive): Correctly predicted positive cases = 75
• FP (False Positive): Incorrectly predicted positive cases = 20
• FN (False Negative): Missed positive cases = 15
• TN (True Negative): Correctly predicted negative cases = 140
Accuracy calculation:
Accuracy = (TP + TN) / (TP + TN + FP + FN)
= (75 + 140) / (75 + 140 + 20 + 15)
= 215 / 250 = 0.86 → 86%
Precision calculation:
Precision = TP / (TP + FP)
= 75 / (75 + 20)
= 75 / 95 ≈ 0.789 → 78.9%
a. Consider the scenario of a logistics company that manages deliveries [10]
across regions. Each region contains multiple hubs, and each hub serves
several delivery zones. Delivery agents are assigned to zones. The
objective is to track delivery performance at different levels, such as
region, hub, and zone, and count the number of deliveries completed.
Design an Information Package and a STAR schema for the given
scenario, considering granularity for the location hierarchy, delivery
agents, etc. Assumptions made, if any, to be clearly stated.
Information Package – 4marks
STAR schema - 6Marks
Correct identification of Dimensions
Correct identification of Facts
Q2
CO-1; SO-2;
• Information package defines dimensions, measures, and hierarchy
BL-4
• Measures: number of deliveries, delivery time, success rate
• Dimensions: region → hub → zone (location hierarchy), delivery agent,
time
Steps:
Step 1: Identify business process → delivery tracking
Step 2: Define grain → one record per delivery per zone
Step 3: Identify dimensions → region, hub, zone, agent, time
Step 4: Identify measures → delivery count, performance metrics
Step 5: Design fact table → Delivery_Fact (delivery count, time, status)
Step 6: Create dimension tables → Location, Agent, Time
********** 3 **********
--- page 4 ---
b. Discuss the principle and steps to implement the K-means clustering   [10]
algorithm. Apply K-means Clustering to create 2 clusters for the given
dataset x= {1,2,6,7,8,10,11,15,17,18,20,22}. Use Euclidean distance
metric and assume initial centroid as 1 and 22.
Principle and steps to implement the K-means clustering – 4Marks
Kmeans Clustering numerical – 6 marks
Kmeans Clustering:
K-means partitions data into k clusters based on distance
• Objective: minimize intra-cluster variance
A group of data points whose inter-point distances are small compared
with the distances to points outside of the cluster
Q2
CO-3; SO-2;
BL-3
Steps:
Step 1: Initialize centroids → 1 and 22
Step 2: Assign each data point to nearest centroid using Euclidean distance
Step 3: Form clusters
Step 4: Recalculate centroids (mean of cluster points)
Step 5: Repeat assignment and update until convergence
Assign Cluster Centroids - Until Convergence : - Cluster Assignment
Step - Re-assigning Centroid Step
********** 4 **********
--- page 5 ---
Dataset: {1, 2, 6, 7, 8, 10, 11, 15, 17, 18, 20, 22}
• k = 2
• Initial centroids: C1 = 1, C2 = 22
Step 1: Assign points to nearest centroid (Iteration 1)
Distance = |x − centroid|
Cluster 1 (closer to 1):
• 1, 2, 6, 7, 8, 10, 11
Cluster 2 (closer to 22):
• 15, 17, 18, 20, 22
Step 2: Compute new centroids
• C1 = (1 + 2 + 6 + 7 + 8 + 10 + 11) / 7 = 45 / 7 ≈ 6.43
• C2 = (15 + 17 + 18 + 20 + 22) / 5 = 92 / 5 = 18.4
Step 3: Reassign points (Iteration 2)
Check distances to new centroids:
Cluster 1:
• 1, 2, 6, 7, 8
Cluster 2:
• 10, 11, 15, 17, 18, 20, 22
Differentiate between Operational system and Information system –
Q3   a. 6marks
CO-2; SO-2;   [10]
BL-2   Concept of hypercubes in data warehouse – 4marks
********** 5 **********
--- page 6 ---
Operational system:
• Used for daily transactions (OLTP)
• Real-time processing, normalized data
Informational system:
• Used for analysis (OLAP)
• Historical data, denormalized
Hypercube concept:
• Multidimensional data representation
• Each dimension represents a business perspective (time, location,
product)
• Enables slicing, dicing, drill-down, roll-up
Steps:
• Step 1: Define dimensions
• Step 2: Organize data into multidimensional cube
• Step 3: Perform OLAP operations for analysis
b. Naïve Bayes Classification   [10]
• Based on Bayes theorem with independence assumption
• Calculates posterior probability for each class
Q3   Steps:
CO-3; SO-2;   • Step 1: Calculate prior probabilities P(Pass), P(Fail)
BL-3   • Step 2: Compute likelihoods P(attribute | class)
• Step 3: Multiply probabilities for given input X
• Step 4: Compare posterior probabilities
• Step 5: Assign class with highest probability
 Establish the Prior probability P(Cj) for each class.
********** 6 **********
--- page 7 ---
 Derived Probabilities: Establish the probability P(xi| Cj) for each
attribute xi and class Cj (how often each value occurs in the class
in the training data)
 Conditional probability   P(ti|Cj) is calculated
 Posterior probability P(Cj | ti) is then found
 The class with the highest probability is the one chosen for the
tuple.
a. Explain Type 1 and Type 2 slowly changing dimensions (SCD). – 4marks [10]
Characteristics of a Data Warehouse - 6Marks
 Most dimensions are generally constant over time.
 Many dimensions change slowly.
 Though the key does not change other description and attributes
change slowly over time.
 Dimension table attributes are not overwritten in some types of
changes.
Type 1: Correction of errors
Type 2: Preservation of history
SCD Type 1:
• Overwrites old data
• No history maintained
Q4   SCD Type 2:
CO-1; SO-2;   • Maintains history with new records
BL-3   • Uses surrogate keys and timestamps
DW characteristics:
• Subject-oriented → organized by business subjects
• Integrated → consistent data from multiple sources
• Time-variant → stores historical data The time-variant nature of the data in a
data warehouse
❑ Allows for analysis of the past
❑ Relates information to the present
❑ Enables forecasts for the future
• Non-volatile → stable, read-only
 Data once recorded cannot be updated.
 Data warehouse requires two operations in data accessing.
⚫ Initial loading of data
⚫ Incremental loading of data
********** 7 **********
--- page 8 ---
Steps
• Step 1: Collect historical data
• Step 2: Ensure consistency and integration
• Step 3: Enable trend analysis
• Step 4: Support strategic decision-making
b. Decision Tree (DT) algorithm.   [10]
Decision tree disadvantages:
• Overfitting
• Sensitive to noise
• Bias toward attributes with more values
ID3 algorithm:
Q4
• Uses entropy and information gain
CO-2; SO-2;
BL-3
Steps:
Step 1: Compute entropy of dataset
Step 2: Calculate information gain for each attribute
Step 3: Select attribute with highest gain as root
Step 4: Split dataset
Step 5: Repeat recursively
Explain the concept of association rule mining. – 4marks   [10]
a.
Numerical – 6marks
Apriori algorithm
• Used for association rule mining
Q5
• Finds frequent itemsets and strong rules
CO-3; SO-2;
BL-4
Steps:
• Step 1: Generate candidate itemsets
• Step 2: Calculate support
• Step 3: Prune itemsets below threshold
• Step 4: Generate higher-order itemsets
• Step 5: Calculate confidence for rules
• Step 6: Select strong rules
********** 8 **********
--- page 9 ---
Transactions = 5
• Minimum support = 30% → 0.3 × 5 = 1.5 → support count ≥ 2
• Minimum confidence = 60%
Step 1: Generate 1-itemsets (L1)
Count support:
• Shirt → 3 (T1, T2, T4)
• Jeans → 4 (T1, T2, T3, T5)
• Belt → 3 (T1, T4, T5)
• Shoes → 2 (T3, T4)
Frequent 1-itemsets (support ≥ 2):
• {Shirt}, {Jeans}, {Belt}, {Shoes}
Step 2: Generate 2-itemsets (C2 → L2)
Possible pairs and support:
• {Shirt, Jeans} → 2 (T1, T2)
• {Shirt, Belt} → 2 (T1, T4)
• {Shirt, Shoes} → 1 (T4)
• {Jeans, Belt} → 2 (T1, T5)
• {Jeans, Shoes} → 1 (T3)
• {Belt, Shoes} → 1 (T4)
Frequent 2-itemsets:
• {Shirt, Jeans}, {Shirt, Belt}, {Jeans, Belt}
Final frequent itemsets
• L1: {Shirt}, {Jeans}, {Belt}, {Shoes}
Shirt → Belt
Confidence = 2 / 3 ≈ 66.7%
Belt → Jeans
Confidence = 2 / 3 ≈ 66.7%
b. Essential differences between the MOLAP and ROLAP architectural [10]
models alongwith neat diagram – 10 marks
Q5
CO-1,CO-3;
SO-2; BL- 2   MOLAP:
• Data stored in multidimensional cube
• Fast query performance
• Limited scalability
********** 9 **********
--- page 10 ---
ROLAP:
• Data stored in relational tables
• Scalable but slower queries
Steps:
• Step 1: Store data (cube vs relational)
• Step 2: Process queries
• Step 3: Perform OLAP operations
ROLAP
MOLAP
********** 10 **********
--- page 11 ---
ROLAP   MOLAP
Stored as relational tables Stored as relational tables
Detailed   and   light Various summary   data   kept   in
summary   proprietary
data available   databases (MDDBs)
Very large data volumes Moderate data volumes
All data access from the Summary data access from MDDB
warehouse storage.   detailed data access from warehouse.
a. Consider the scenario of a hospital that wants to classify patients as   [10]
high-risk or low-risk based on blood pressure and cholesterol level.
Blood Pressure   Cholesterol   Risk
(X1)   (X2)
150   240   High
145   230   High
Q6
CO-2,CO-3;   110   180   Low
SO-2;   105   170   Low
BL-3
A new patient has Blood Pressure = 120 and Cholesterol = 200.
Apply KNN using Euclidean distance (k = 3) to classify the risk level.
• Instance-based learning algorithm
• Classifies based on nearest neighbors
********** 11 **********
--- page 12 ---
Steps:
• Step 1: Choose k = 3
• Step 2: Calculate Euclidean distance from new point
• Step 3: Identify 3 nearest neighbors
• Step 4: Perform majority voting
• Step 5: Assign class
Outcome: Risk classified as High or Low
Final classification
• Predicted class = Low risk
• The new patient is classified as Low risk based on nearest neighbors
• KNN assigns class based on majority among closest data points
b. Data Mining Techniques ;   [10]
Q6
CO-3; SO-2;
BL- 3
Categorization of data mining techniques – 5 Marks
Regression unknown value prediction – 5 marks
• Models relationship between variables
Steps:
• Step 1: Compute mean of X and Y
• Step 2: Calculate slope (m)
• Step 3: Calculate intercept (c)
• Step 4: Form equation y = mx + c
• Step 5: Predict value at X = 10
Outcome: Predicted relief value
********** 12 **********
--- page 13 ---
a. Web content Mining - 5Marks   [10]
and Web structure mining -5marks
and describe its significance in extracting web data.
Web content mining:
• Extracts information from web pages
• Extends work of basic search engines
•   Search Engines
• IR application
• Keyword based
•   Similarity between query and document
Web structure mining:
Q7
• Analyzes link structure between pages
CO-2,3; SO-2;
BL-2
• Mine structure (links, graph) of the Web
• Techniques
• PageRank
• CLEVER
•   Create a model of the Web organization.
• May be combined with content mining to more effectively retrieve
important pages
Steps:
• Step 1: Collect web data
• Step 2: Preprocess data
• Step 3: Apply mining techniques
• Step 4: Extract patterns
Q7   b. KDD Process   [10]
CO-1,2-; SO-
2; BL-4
********** 13 **********
--- page 14 ---
• Selection: Obtain data from various sources.
• Preprocessing: Cleanse data.
• Transformation: Convert to common format.
Transform to new format.
• Data Mining: Obtain desired results.
• Interpretation/Evaluation: Present results to user
in meaningful manner.
Application (supermarket):
• Analyze purchase data
• Discover buying patterns
• Improve sales strategies
KDD Process- 8marks
KDD Scenario Application - 2marks
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 1030ab6dbbc1

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_IT_7001/Data Warehousing and Mining/ANS_Data Warehousing and Mining(702IT0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Data Warehousing and Mining
Date: 11 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a. Web crawler in data mining   [5]
• Robot (spider) traverses the hypertext sructure in the Web.
•   Collect information from visited pages
• Used to construct indexes for search engines
CO-3 ; SO-
2 ;   •   Traditional Crawler – visits entire Web (?) and replaces index
BL-2   •   Periodic Crawler – visits portions of the Web and updates subset of
index
•   Incremental Crawler – selectively searches the Web and incrementally
modifies index
b. Data acquisition phase in Data Warehouse architecture.   [5]
CO-2 ; SO-   Production data: data from various operational systems
2 ;   External data: for finding trends and comparisons againstother
BL-2   organizations.
Internal data: private confidential data important to an organization
Archived data:   for getting some historical information
CO-2,3 ;   c.
SO-2 ;   • 100 fraud correctly identified → TP = 100   [5]
BL-3   • 10 genuine marked as fraud → FP = 10
********** 1 **********
--- page 2 ---
• 5 fraud missed → FN = 5
• 50 genuine correctly identified → TN = 50
Accuracy ≈ 90.9% , Precision ≈ 90.9%, Recall = 95.24%
Discuss the following characteristics of a Data Warehouse:   [5]
d.   i)   Subject Oriented – 2.5 marks
ii)   Non-Volatile – 2.5 marks
Subject Oriented
CO-1 ; SO-
2 ; BL-2
Non Volatile :
 Data once recorded cannot be updated.
 Data warehouse requires two operations in
data accessing.
⚫ Initial loading of data
⚫ Incremental loading of data
********** 2 **********
--- page 3 ---
a. Consider a hotel chain that wants to analyze room bookings considering [10]
dimensions such as Room Type, Customer, etc. as well as measures such as
booking count, revenue. Develop an information package and design a star
schema for the given scenario. Assumptions made, if any, should be clearly
stated.
Information Package – 4Marks
Star Schema – 6marks
nformation package (hotel booking analysis)
• Business process → room booking analysis
• Grain → one record per booking transaction
Q2
CO-2; SO-   Dimensions
2;
BL-3   • Room Type → standard, deluxe, suite
• Customer → customer id, name, category
• Time → date, month, year
• Hotel/Location → city, branch
• Booking Channel → online, agent, walk-in
Measures
• Booking count
• Revenue (room charges)
• Number of nights stayed
Steps to develop information package
• Step 1: Identify business objective → analyze bookings and revenue
• Step 2: Define grain → per booking per customer per date
• Step 3: Identify dimensions → room, customer, time, location
********** 3 **********
--- page 4 ---
• Step 4: Identify measures → count, revenue
• Step 5: Validate consistency across dimensions
Dimension tables
Room_Dimension
• Room_Type_ID (PK)
• Room_Type
• Price_Category
Customer_Dimension
• Customer_ID (PK)
• Name
• Age
• Customer_Type
Time_Dimension
• Time_ID (PK)
• Date
• Month
• Year
Location_Dimension
• Location_ID (PK)
• City
• Hotel_Name
b. Explain the advantages and disadvantages of Naïve Bayes algorithm.-   [10]
Q2
2marks
CO-3; SO-
Apply Naïve Bayes Algorithm and classify the following unknown data
2;
sample
BL-4
X = (bad, low, none, >35K) – 8marks
********** 4 **********
--- page 5 ---
Advantages of Naïve Bayes
• Simple and easy to implement
• Requires less training data compared to other algorithms
• Fast in training and prediction (computationally efficient)
• Works well with high-dimensional data (e.g., text classification)
• Suitable for real-time applications (spam filtering, sentiment analysis)
Disadvantages of Naïve Bayes
• Assumes independence among features, which is often unrealistic
• Performance decreases when features are highly correlated
Total = 14
Target: Credit Risk
Class Count
High   6
Moderate 3
Low   5
Step 2: Prior Probabilities
Step 3: Likelihood Tables
********** 5 **********
--- page 6 ---
Class = High (6 records)
Feature   Value
Credit History bad = 2/6, unknown = 3/6, good = 1/6
Debt   high = 4/6, low = 2/6
Collateral   none = 6/6, adequate = 0
Income   0–15K = 3/6, 15–35K = 2/6, >35K = 1/6
Class = Moderate (3 records)
Feature   Value
Credit History unknown = 1/3, bad = 1/3, good = 1/3
Debt   low = 2/3, high = 1/3
Collateral   none = 2/3, adequate = 1/3
Income   15–35K = 2/3, >35K = 1/3
Class = Low (5 records)
Feature   Value
Credit History unknown = 3/5, good = 2/5
Debt   low = 3/5, high = 2/5
Collateral   none = 3/5, adequate = 2/5
Income   >35K = 4/5, 0–15K = 1/5
Step 4: Classify Unseen Samples
1. X = (bad, low, none, >35K)
High
Moderate
Low
Result → MODERATE
2. X = (unknown, low, none, 0–15K)
********** 6 **********
--- page 7 ---
Result → HIGH
3. X = (good, high, adequate, 15–35K)
Result → MODERATE
a. Explain any 2 real-world applications of clustering. – 4marks
Customer segmentation
Q3   Medical Diagnosis
CO-2; SO-   [10]
Kmeans Clustering – 6marks
2; BL-3
Consider the scenario of a retail analyst who wants to segment customers
based on their spending behavior. Using the following data points, form 2
clusters using the K-Means algorithm up to two iterations with Euclidean
distance. Take P and R as initial centroids.
********** 7 **********
--- page 8 ---
Point X   Y
P   2   2
Q   2   1
R   1   3
S   5   6
T   6   7
Given
• Points:
P(2,2), Q(2,1), R(1,3), S(5,6), T(6,7)
• k = 2
• Initial centroids: P(2,2) and R(1,3)
Step 1: Compute distances
Step 2: Assign clusters
Step 3: Compute new centroids
Step 4: Recompute distances
b. MOLAP 5m   [10]
ROLAP 5m
MOLAP:
• Data stored in multidimensional cube
• Fast query performance
• Limited scalability
ROLAP:
Q3   • Data stored in relational tables
CO-3; SO-   • Scalable but slower queries
2; BL-3
Steps:
• Step 1: Store data (cube vs relational)
• Step 2: Process queries
• Step 3: Perform OLAP operations
ROLAP
********** 8 **********
--- page 9 ---
MOLAP
ROLAP   MOLAP
Stored as relational tables Stored as relational tables
Detailed   and   light Various summary   data   kept   in
summary   proprietary
data available   databases (MDDBs)
********** 9 **********
--- page 10 ---
Very large data volumes Moderate data volumes
All data access from the Summary data access from MDDB
warehouse storage.   detailed data access from warehouse.
Metadata and its types in a data warehouse. – 4marks   [10]
a.
Data about data in the datawarehouse Metadata can be of 3 types
◦   Extraction and transformation metadata: Details pertaining   to
extraction frequencies, extraction methods, business   rules for
data extraction
◦ End-user metadata: navigational map of DW
◦   Operational metadata:   contains   operational data sources
Data loading and data transformation techniques in the ETL process of
Data warehousing. – 6marks
Transformation means to integrate or consolidate data from various
Q4   sources.
CO-1,2;   Basic tasks:
SO-2;   ❑ Selection
BL-3   ❑ Splitting/joining
❑ Conversion
❑ Summarization
❑ Enrichment
Data Loading
❑ Determine when (time) and how (as a whole or in chunks) to load
data.
❑ Phrases used in data loading,
❑ Initial load : Populating the DW for the very first time.
❑ Incremental load: Applying the ongoing changes as required.
❑ Full refresh : Completely erasing earlier contents and
reloading data.
********** 10 **********
--- page 11 ---
b. Differentiate between supervised and unsupervised mining techniques   [10]
3Marks
Q4
CO-3; SO-
2;
BL-4
Apply the ID3 Classification Algorithm for the given data to decide the
best split. (Calculate the root node)
- 6marks
Part 2: ID3 algorithm (6 marks)
Step 1: Compute overall entropy
• Total = 10
• Yes = 6, No = 4
********** 11 **********
--- page 12 ---
Step 2: Compute information gain
Step 3: Select root node
Final answer
• Best attribute (root node) = A1
• A1 provides maximum information gain
********** 12 **********
--- page 13 ---
Apriori   [10]
Explain the principle of the Apriori algorithm – 3marks
a.
Numerical – 7 marks
Apriori is used for association rule mining
• Based on Apriori property
Steps of Apriori algorithm
• Step 1: Generate candidate 1-itemsets (C1)
• Step 2: Calculate support and form L1 (frequent itemsets)
• Step 3: Generate candidate k-itemsets (Ck) from Lk-1
• Step 4: Prune itemsets with support < minimum support
• Step 5: Repeat until no new frequent itemsets
Q5   • Step 6: Generate rules and compute confidence
CO-1,CO-
3; SO-2;
BL-3
Given
Transactions:
• T1 → {laptop, wireless mouse, keyboard}
• T2 → {laptop, wireless mouse}
• T3 → {keyboard, wireless mouse}
• Min support count = 2
• Min confidence = 80%
Step 1: Generate 1-itemsets (L1)
Count support:
• laptop → 2 (T1, T2)
• wireless mouse → 3 (T1, T2, T3)
• keyboard → 2 (T1, T3)
********** 13 **********
--- page 14 ---
Frequent itemsets L1:
• {laptop}, {wireless mouse}, {keyboard}
Step 2: Generate 2-itemsets (L2)
• {laptop, wireless mouse} → 2 (T1, T2)
• {laptop, keyboard} → 1
• {wireless mouse, keyboard} → 2 (T1, T3)
Frequent itemsets L2:
• {laptop, wireless mouse}, {wireless mouse, keyboard}
• L1: {laptop}, {wireless mouse}, {keyboard}
• L2: {laptop, wireless mouse}, {wireless mouse, keyboard}
Step 4: Generate association rules
From {laptop, wireless mouse}
• laptop → wireless mouse
Confidence = 2 / 2 = 100%
keyboard → wireless mouse
b. KNN   [10]
K-Nearest Neighbors (KNN) classification algorithm 8marks
Relevant example – 2marks
 Training set includes classes.
 Examine K items near item to be classified.
Q5    New item placed in class with the most number of close items.
CO-1,CO-
3; SO-2;   • KNN is a supervised learning algorithm used for classification and
BL- 2   regression
• Classification is based on similarity (distance) between data points
• Uses distance metrics such as Euclidean distance
For classification problems, a class label is assigned on the basis of a
majority vote—i.e. the label that is most frequently represented around a
given data point is used.
********** 14 **********
--- page 15 ---
• Step 1: Choose value of k (number of neighbors)
• Step 2: Calculate distance between new point and all training points
• Step 3: Sort distances in ascending order
• Step 4: Select k nearest neighbors
• Step 5: Perform majority voting
• Step 6: Assign the class
********** 15 **********
--- page 16 ---
a. An energy company studies how electricity consumption varies with temperature.   [10]
The data collected is:
Temperature
20   25   30   35   40
(°C)
Consumption   200   220   260   300   340
Find the regression equation and analyze how temperature affects consumption at
temperature =42.
Q6
• X (Temperature) = 20, 25, 30, 35, 40
CO-1,CO-   • Y (Consumption) = 200, 220, 260, 300, 340
3; SO-2;
BL-4   • n = 5
• ΣX = 20 + 25 + 30 + 35 + 40 = 150
• ΣY = 200 + 220 + 260 + 300 + 340 = 1320
• ΣX² = 400 + 625 + 900 + 1225 + 1600 = 4750
y = mx + c
Regression equation: y = 7.2x + 48
• Predicted consumption at 42°C = 350.4
b. Discuss the following data mining techniques:   [10]
i. Web Content Mining – 5marks
ii. Web Structure Mining – 5marks
Web Content Mining
• Extends work of basic search engines
• Search Engines
• IR application
• Keyword based
•   Similarity between query and document
Q6 CO-
2,CO-3;
SO-2;
Web Structure Mining
BL- 3
• Mine structure (links, graph) of the Web
• Techniques
• PageRank
• CLEVER
•   Create a model of the Web organization.
• May be combined with content mining to more effectively retrieve
important pages.
Q7   a.   [10]
CO-1; SO-
2;
********** 16 **********
--- page 17 ---
BL-2   Casual or Novice User. Uses the data warehouse occasionally, not daily.
Needs a very intuitive information interface.
Regular User. Uses the data warehouse almost daily. Comfortable with
computing options but cannot create own reports and queries from scratch.
Needs query templates and predefined reports.
Power User. Is highly proficient with technology. Can create reports and
queries from scratch. Some can write their own macros and scripts. Can
import data into spreadsheets and other applications.
User types by the way they wish to interact to obtain information.
Preprocessed Reports. Use routine reports run and delivered at regular
intervals.
Predefined Queries and Templates. Enter own set of parameters and run
queries with predefined templates and reports with predefined formats.
Limited ad hoc Access. Create from scratch and run limited number and
simple types of queries and analysis.
Technical Analysts. Look for complex analysis, statistical analysis, drill-down
and slicedice capabilities, and freedom to access the entire data warehouse.
Business Analysts. Although comfortable with technology, are not quite adept
at creating queries and reports from scratch. Predefined navigation is helpful.
Want to look at the results in many different ways. To some extent, can
modify and customize predefined reports.
Business-Oriented Users.
b.   [10]
Knowledge Discovery in Databases (KDD) process with the help of a neat
Q7
diagram. 7Marks
CO2; SO2;
Discuss the issues related to KDD – 3 Marks
BL-2
KDD PROCESS
********** 17 **********
--- page 18 ---
• Selection: Obtain data from various sources.
• Preprocessing: Cleanse data.
• Transformation: Convert to common format.
Transform to new format.
• Data Mining: Obtain desired results.
• Interpretation/Evaluation: Present results to user
in meaningful manner.
KDD Issues
• Human Interaction
•   Overfitting
•   Outliers
•   Interpretation
•   Visualization
• Large Datasets
• High Dimensionality
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 386184c9a1fe

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_IT_7041/Data Warehousing and Mining/ANS_Data Warehousing and Mining(702IT0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Data Warehousing and Mining
Date: 11 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a. Web crawler in data mining   [5]
• Robot (spider) traverses the hypertext sructure in the Web.
•   Collect information from visited pages
• Used to construct indexes for search engines
CO-3 ; SO-
2 ;   •   Traditional Crawler – visits entire Web (?) and replaces index
BL-2   •   Periodic Crawler – visits portions of the Web and updates subset of
index
•   Incremental Crawler – selectively searches the Web and incrementally
modifies index
b. Data acquisition phase in Data Warehouse architecture.   [5]
CO-2 ; SO-   Production data: data from various operational systems
2 ;   External data: for finding trends and comparisons againstother
BL-2   organizations.
Internal data: private confidential data important to an organization
Archived data:   for getting some historical information
CO-2,3 ;   c.
SO-2 ;   • 100 fraud correctly identified → TP = 100   [5]
BL-3   • 10 genuine marked as fraud → FP = 10
********** 1 **********
--- page 2 ---
• 5 fraud missed → FN = 5
• 50 genuine correctly identified → TN = 50
Accuracy ≈ 90.9% , Precision ≈ 90.9%, Recall = 95.24%
Discuss the following characteristics of a Data Warehouse:   [5]
d.   i)   Subject Oriented – 2.5 marks
ii)   Non-Volatile – 2.5 marks
Subject Oriented
CO-1 ; SO-
2 ; BL-2
Non Volatile :
 Data once recorded cannot be updated.
 Data warehouse requires two operations in
data accessing.
⚫ Initial loading of data
⚫ Incremental loading of data
********** 2 **********
--- page 3 ---
a. Consider a hotel chain that wants to analyze room bookings considering [10]
dimensions such as Room Type, Customer, etc. as well as measures such as
booking count, revenue. Develop an information package and design a star
schema for the given scenario. Assumptions made, if any, should be clearly
stated.
Information Package – 4Marks
Star Schema – 6marks
nformation package (hotel booking analysis)
• Business process → room booking analysis
• Grain → one record per booking transaction
Q2
CO-2; SO-   Dimensions
2;
BL-3   • Room Type → standard, deluxe, suite
• Customer → customer id, name, category
• Time → date, month, year
• Hotel/Location → city, branch
• Booking Channel → online, agent, walk-in
Measures
• Booking count
• Revenue (room charges)
• Number of nights stayed
Steps to develop information package
• Step 1: Identify business objective → analyze bookings and revenue
• Step 2: Define grain → per booking per customer per date
• Step 3: Identify dimensions → room, customer, time, location
********** 3 **********
--- page 4 ---
• Step 4: Identify measures → count, revenue
• Step 5: Validate consistency across dimensions
Dimension tables
Room_Dimension
• Room_Type_ID (PK)
• Room_Type
• Price_Category
Customer_Dimension
• Customer_ID (PK)
• Name
• Age
• Customer_Type
Time_Dimension
• Time_ID (PK)
• Date
• Month
• Year
Location_Dimension
• Location_ID (PK)
• City
• Hotel_Name
b. Explain the advantages and disadvantages of Naïve Bayes algorithm.-   [10]
Q2
2marks
CO-3; SO-
Apply Naïve Bayes Algorithm and classify the following unknown data
2;
sample
BL-4
X = (bad, low, none, >35K) – 8marks
********** 4 **********
--- page 5 ---
Advantages of Naïve Bayes
• Simple and easy to implement
• Requires less training data compared to other algorithms
• Fast in training and prediction (computationally efficient)
• Works well with high-dimensional data (e.g., text classification)
• Suitable for real-time applications (spam filtering, sentiment analysis)
Disadvantages of Naïve Bayes
• Assumes independence among features, which is often unrealistic
• Performance decreases when features are highly correlated
Total = 14
Target: Credit Risk
Class Count
High   6
Moderate 3
Low   5
Step 2: Prior Probabilities
Step 3: Likelihood Tables
********** 5 **********
--- page 6 ---
Class = High (6 records)
Feature   Value
Credit History bad = 2/6, unknown = 3/6, good = 1/6
Debt   high = 4/6, low = 2/6
Collateral   none = 6/6, adequate = 0
Income   0–15K = 3/6, 15–35K = 2/6, >35K = 1/6
Class = Moderate (3 records)
Feature   Value
Credit History unknown = 1/3, bad = 1/3, good = 1/3
Debt   low = 2/3, high = 1/3
Collateral   none = 2/3, adequate = 1/3
Income   15–35K = 2/3, >35K = 1/3
Class = Low (5 records)
Feature   Value
Credit History unknown = 3/5, good = 2/5
Debt   low = 3/5, high = 2/5
Collateral   none = 3/5, adequate = 2/5
Income   >35K = 4/5, 0–15K = 1/5
Step 4: Classify Unseen Samples
1. X = (bad, low, none, >35K)
High
Moderate
Low
Result → MODERATE
2. X = (unknown, low, none, 0–15K)
********** 6 **********
--- page 7 ---
Result → HIGH
3. X = (good, high, adequate, 15–35K)
Result → MODERATE
a. Explain any 2 real-world applications of clustering. – 4marks
Customer segmentation
Q3   Medical Diagnosis
CO-2; SO-   [10]
Kmeans Clustering – 6marks
2; BL-3
Consider the scenario of a retail analyst who wants to segment customers
based on their spending behavior. Using the following data points, form 2
clusters using the K-Means algorithm up to two iterations with Euclidean
distance. Take P and R as initial centroids.
********** 7 **********
--- page 8 ---
Point X   Y
P   2   2
Q   2   1
R   1   3
S   5   6
T   6   7
Given
• Points:
P(2,2), Q(2,1), R(1,3), S(5,6), T(6,7)
• k = 2
• Initial centroids: P(2,2) and R(1,3)
Step 1: Compute distances
Step 2: Assign clusters
Step 3: Compute new centroids
Step 4: Recompute distances
b. MOLAP 5m   [10]
ROLAP 5m
MOLAP:
• Data stored in multidimensional cube
• Fast query performance
• Limited scalability
ROLAP:
Q3   • Data stored in relational tables
CO-3; SO-   • Scalable but slower queries
2; BL-3
Steps:
• Step 1: Store data (cube vs relational)
• Step 2: Process queries
• Step 3: Perform OLAP operations
ROLAP
********** 8 **********
--- page 9 ---
MOLAP
ROLAP   MOLAP
Stored as relational tables Stored as relational tables
Detailed   and   light Various summary   data   kept   in
summary   proprietary
data available   databases (MDDBs)
********** 9 **********
--- page 10 ---
Very large data volumes Moderate data volumes
All data access from the Summary data access from MDDB
warehouse storage.   detailed data access from warehouse.
Metadata and its types in a data warehouse. – 4marks   [10]
a.
Data about data in the datawarehouse Metadata can be of 3 types
◦   Extraction and transformation metadata: Details pertaining   to
extraction frequencies, extraction methods, business   rules for
data extraction
◦ End-user metadata: navigational map of DW
◦   Operational metadata:   contains   operational data sources
Data loading and data transformation techniques in the ETL process of
Data warehousing. – 6marks
Transformation means to integrate or consolidate data from various
Q4   sources.
CO-1,2;   Basic tasks:
SO-2;   ❑ Selection
BL-3   ❑ Splitting/joining
❑ Conversion
❑ Summarization
❑ Enrichment
Data Loading
❑ Determine when (time) and how (as a whole or in chunks) to load
data.
❑ Phrases used in data loading,
❑ Initial load : Populating the DW for the very first time.
❑ Incremental load: Applying the ongoing changes as required.
❑ Full refresh : Completely erasing earlier contents and
reloading data.
********** 10 **********
--- page 11 ---
b. Differentiate between supervised and unsupervised mining techniques   [10]
3Marks
Q4
CO-3; SO-
2;
BL-4
Apply the ID3 Classification Algorithm for the given data to decide the
best split. (Calculate the root node)
- 6marks
Part 2: ID3 algorithm (6 marks)
Step 1: Compute overall entropy
• Total = 10
• Yes = 6, No = 4
********** 11 **********
--- page 12 ---
Step 2: Compute information gain
Step 3: Select root node
Final answer
• Best attribute (root node) = A1
• A1 provides maximum information gain
********** 12 **********
--- page 13 ---
Apriori   [10]
Explain the principle of the Apriori algorithm – 3marks
a.
Numerical – 7 marks
Apriori is used for association rule mining
• Based on Apriori property
Steps of Apriori algorithm
• Step 1: Generate candidate 1-itemsets (C1)
• Step 2: Calculate support and form L1 (frequent itemsets)
• Step 3: Generate candidate k-itemsets (Ck) from Lk-1
• Step 4: Prune itemsets with support < minimum support
• Step 5: Repeat until no new frequent itemsets
Q5   • Step 6: Generate rules and compute confidence
CO-1,CO-
3; SO-2;
BL-3
Given
Transactions:
• T1 → {laptop, wireless mouse, keyboard}
• T2 → {laptop, wireless mouse}
• T3 → {keyboard, wireless mouse}
• Min support count = 2
• Min confidence = 80%
Step 1: Generate 1-itemsets (L1)
Count support:
• laptop → 2 (T1, T2)
• wireless mouse → 3 (T1, T2, T3)
• keyboard → 2 (T1, T3)
********** 13 **********
--- page 14 ---
Frequent itemsets L1:
• {laptop}, {wireless mouse}, {keyboard}
Step 2: Generate 2-itemsets (L2)
• {laptop, wireless mouse} → 2 (T1, T2)
• {laptop, keyboard} → 1
• {wireless mouse, keyboard} → 2 (T1, T3)
Frequent itemsets L2:
• {laptop, wireless mouse}, {wireless mouse, keyboard}
• L1: {laptop}, {wireless mouse}, {keyboard}
• L2: {laptop, wireless mouse}, {wireless mouse, keyboard}
Step 4: Generate association rules
From {laptop, wireless mouse}
• laptop → wireless mouse
Confidence = 2 / 2 = 100%
keyboard → wireless mouse
b. KNN   [10]
K-Nearest Neighbors (KNN) classification algorithm 8marks
Relevant example – 2marks
 Training set includes classes.
 Examine K items near item to be classified.
Q5    New item placed in class with the most number of close items.
CO-1,CO-
3; SO-2;   • KNN is a supervised learning algorithm used for classification and
BL- 2   regression
• Classification is based on similarity (distance) between data points
• Uses distance metrics such as Euclidean distance
For classification problems, a class label is assigned on the basis of a
majority vote—i.e. the label that is most frequently represented around a
given data point is used.
********** 14 **********
--- page 15 ---
• Step 1: Choose value of k (number of neighbors)
• Step 2: Calculate distance between new point and all training points
• Step 3: Sort distances in ascending order
• Step 4: Select k nearest neighbors
• Step 5: Perform majority voting
• Step 6: Assign the class
********** 15 **********
--- page 16 ---
a. An energy company studies how electricity consumption varies with temperature.   [10]
The data collected is:
Temperature
20   25   30   35   40
(°C)
Consumption   200   220   260   300   340
Find the regression equation and analyze how temperature affects consumption at
temperature =42.
Q6
• X (Temperature) = 20, 25, 30, 35, 40
CO-1,CO-   • Y (Consumption) = 200, 220, 260, 300, 340
3; SO-2;
BL-4   • n = 5
• ΣX = 20 + 25 + 30 + 35 + 40 = 150
• ΣY = 200 + 220 + 260 + 300 + 340 = 1320
• ΣX² = 400 + 625 + 900 + 1225 + 1600 = 4750
y = mx + c
Regression equation: y = 7.2x + 48
• Predicted consumption at 42°C = 350.4
b. Discuss the following data mining techniques:   [10]
i. Web Content Mining – 5marks
ii. Web Structure Mining – 5marks
Web Content Mining
• Extends work of basic search engines
• Search Engines
• IR application
• Keyword based
•   Similarity between query and document
Q6 CO-
2,CO-3;
SO-2;
Web Structure Mining
BL- 3
• Mine structure (links, graph) of the Web
• Techniques
• PageRank
• CLEVER
•   Create a model of the Web organization.
• May be combined with content mining to more effectively retrieve
important pages.
Q7   a.   [10]
CO-1; SO-
2;
********** 16 **********
--- page 17 ---
BL-2   Casual or Novice User. Uses the data warehouse occasionally, not daily.
Needs a very intuitive information interface.
Regular User. Uses the data warehouse almost daily. Comfortable with
computing options but cannot create own reports and queries from scratch.
Needs query templates and predefined reports.
Power User. Is highly proficient with technology. Can create reports and
queries from scratch. Some can write their own macros and scripts. Can
import data into spreadsheets and other applications.
User types by the way they wish to interact to obtain information.
Preprocessed Reports. Use routine reports run and delivered at regular
intervals.
Predefined Queries and Templates. Enter own set of parameters and run
queries with predefined templates and reports with predefined formats.
Limited ad hoc Access. Create from scratch and run limited number and
simple types of queries and analysis.
Technical Analysts. Look for complex analysis, statistical analysis, drill-down
and slicedice capabilities, and freedom to access the entire data warehouse.
Business Analysts. Although comfortable with technology, are not quite adept
at creating queries and reports from scratch. Predefined navigation is helpful.
Want to look at the results in many different ways. To some extent, can
modify and customize predefined reports.
Business-Oriented Users.
b.   [10]
Knowledge Discovery in Databases (KDD) process with the help of a neat
Q7
diagram. 7Marks
CO2; SO2;
Discuss the issues related to KDD – 3 Marks
BL-2
KDD PROCESS
********** 17 **********
--- page 18 ---
• Selection: Obtain data from various sources.
• Preprocessing: Cleanse data.
• Transformation: Convert to common format.
Transform to new format.
• Data Mining: Obtain desired results.
• Interpretation/Evaluation: Present results to user
in meaningful manner.
KDD Issues
• Human Interaction
•   Overfitting
•   Outliers
•   Interpretation
•   Visualization
• Large Datasets
• High Dimensionality
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper e745743b0cae

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_IT_7037/Data Warehousing and Mining/ANS_Data Warehousing and Mining(702IT0C012)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Data Warehousing and Mining
Date: 11 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a. Web crawler in data mining   [5]
• Robot (spider) traverses the hypertext sructure in the Web.
•   Collect information from visited pages
• Used to construct indexes for search engines
CO-3 ; SO-
2 ;   •   Traditional Crawler – visits entire Web (?) and replaces index
BL-2   •   Periodic Crawler – visits portions of the Web and updates subset of
index
•   Incremental Crawler – selectively searches the Web and incrementally
modifies index
b. Data acquisition phase in Data Warehouse architecture.   [5]
CO-2 ; SO-   Production data: data from various operational systems
2 ;   External data: for finding trends and comparisons againstother
BL-2   organizations.
Internal data: private confidential data important to an organization
Archived data:   for getting some historical information
CO-2,3 ;   c.
SO-2 ;   • 100 fraud correctly identified → TP = 100   [5]
BL-3   • 10 genuine marked as fraud → FP = 10
********** 1 **********
--- page 2 ---
• 5 fraud missed → FN = 5
• 50 genuine correctly identified → TN = 50
Accuracy ≈ 90.9% , Precision ≈ 90.9%, Recall = 95.24%
Discuss the following characteristics of a Data Warehouse:   [5]
d.   i)   Subject Oriented – 2.5 marks
ii)   Non-Volatile – 2.5 marks
Subject Oriented
CO-1 ; SO-
2 ; BL-2
Non Volatile :
 Data once recorded cannot be updated.
 Data warehouse requires two operations in
data accessing.
⚫ Initial loading of data
⚫ Incremental loading of data
********** 2 **********
--- page 3 ---
a. Consider a hotel chain that wants to analyze room bookings considering [10]
dimensions such as Room Type, Customer, etc. as well as measures such as
booking count, revenue. Develop an information package and design a star
schema for the given scenario. Assumptions made, if any, should be clearly
stated.
Information Package – 4Marks
Star Schema – 6marks
nformation package (hotel booking analysis)
• Business process → room booking analysis
• Grain → one record per booking transaction
Q2
CO-2; SO-   Dimensions
2;
BL-3   • Room Type → standard, deluxe, suite
• Customer → customer id, name, category
• Time → date, month, year
• Hotel/Location → city, branch
• Booking Channel → online, agent, walk-in
Measures
• Booking count
• Revenue (room charges)
• Number of nights stayed
Steps to develop information package
• Step 1: Identify business objective → analyze bookings and revenue
• Step 2: Define grain → per booking per customer per date
• Step 3: Identify dimensions → room, customer, time, location
********** 3 **********
--- page 4 ---
• Step 4: Identify measures → count, revenue
• Step 5: Validate consistency across dimensions
Dimension tables
Room_Dimension
• Room_Type_ID (PK)
• Room_Type
• Price_Category
Customer_Dimension
• Customer_ID (PK)
• Name
• Age
• Customer_Type
Time_Dimension
• Time_ID (PK)
• Date
• Month
• Year
Location_Dimension
• Location_ID (PK)
• City
• Hotel_Name
b. Explain the advantages and disadvantages of Naïve Bayes algorithm.-   [10]
Q2
2marks
CO-3; SO-
Apply Naïve Bayes Algorithm and classify the following unknown data
2;
sample
BL-4
X = (bad, low, none, >35K) – 8marks
********** 4 **********
--- page 5 ---
Advantages of Naïve Bayes
• Simple and easy to implement
• Requires less training data compared to other algorithms
• Fast in training and prediction (computationally efficient)
• Works well with high-dimensional data (e.g., text classification)
• Suitable for real-time applications (spam filtering, sentiment analysis)
Disadvantages of Naïve Bayes
• Assumes independence among features, which is often unrealistic
• Performance decreases when features are highly correlated
Total = 14
Target: Credit Risk
Class Count
High   6
Moderate 3
Low   5
Step 2: Prior Probabilities
Step 3: Likelihood Tables
********** 5 **********
--- page 6 ---
Class = High (6 records)
Feature   Value
Credit History bad = 2/6, unknown = 3/6, good = 1/6
Debt   high = 4/6, low = 2/6
Collateral   none = 6/6, adequate = 0
Income   0–15K = 3/6, 15–35K = 2/6, >35K = 1/6
Class = Moderate (3 records)
Feature   Value
Credit History unknown = 1/3, bad = 1/3, good = 1/3
Debt   low = 2/3, high = 1/3
Collateral   none = 2/3, adequate = 1/3
Income   15–35K = 2/3, >35K = 1/3
Class = Low (5 records)
Feature   Value
Credit History unknown = 3/5, good = 2/5
Debt   low = 3/5, high = 2/5
Collateral   none = 3/5, adequate = 2/5
Income   >35K = 4/5, 0–15K = 1/5
Step 4: Classify Unseen Samples
1. X = (bad, low, none, >35K)
High
Moderate
Low
Result → MODERATE
2. X = (unknown, low, none, 0–15K)
********** 6 **********
--- page 7 ---
Result → HIGH
3. X = (good, high, adequate, 15–35K)
Result → MODERATE
a. Explain any 2 real-world applications of clustering. – 4marks
Customer segmentation
Q3   Medical Diagnosis
CO-2; SO-   [10]
Kmeans Clustering – 6marks
2; BL-3
Consider the scenario of a retail analyst who wants to segment customers
based on their spending behavior. Using the following data points, form 2
clusters using the K-Means algorithm up to two iterations with Euclidean
distance. Take P and R as initial centroids.
********** 7 **********
--- page 8 ---
Point X   Y
P   2   2
Q   2   1
R   1   3
S   5   6
T   6   7
Given
• Points:
P(2,2), Q(2,1), R(1,3), S(5,6), T(6,7)
• k = 2
• Initial centroids: P(2,2) and R(1,3)
Step 1: Compute distances
Step 2: Assign clusters
Step 3: Compute new centroids
Step 4: Recompute distances
b. MOLAP 5m   [10]
ROLAP 5m
MOLAP:
• Data stored in multidimensional cube
• Fast query performance
• Limited scalability
ROLAP:
Q3   • Data stored in relational tables
CO-3; SO-   • Scalable but slower queries
2; BL-3
Steps:
• Step 1: Store data (cube vs relational)
• Step 2: Process queries
• Step 3: Perform OLAP operations
ROLAP
********** 8 **********
--- page 9 ---
MOLAP
ROLAP   MOLAP
Stored as relational tables Stored as relational tables
Detailed   and   light Various summary   data   kept   in
summary   proprietary
data available   databases (MDDBs)
********** 9 **********
--- page 10 ---
Very large data volumes Moderate data volumes
All data access from the Summary data access from MDDB
warehouse storage.   detailed data access from warehouse.
Metadata and its types in a data warehouse. – 4marks   [10]
a.
Data about data in the datawarehouse Metadata can be of 3 types
◦   Extraction and transformation metadata: Details pertaining   to
extraction frequencies, extraction methods, business   rules for
data extraction
◦ End-user metadata: navigational map of DW
◦   Operational metadata:   contains   operational data sources
Data loading and data transformation techniques in the ETL process of
Data warehousing. – 6marks
Transformation means to integrate or consolidate data from various
Q4   sources.
CO-1,2;   Basic tasks:
SO-2;   ❑ Selection
BL-3   ❑ Splitting/joining
❑ Conversion
❑ Summarization
❑ Enrichment
Data Loading
❑ Determine when (time) and how (as a whole or in chunks) to load
data.
❑ Phrases used in data loading,
❑ Initial load : Populating the DW for the very first time.
❑ Incremental load: Applying the ongoing changes as required.
❑ Full refresh : Completely erasing earlier contents and
reloading data.
********** 10 **********
--- page 11 ---
b. Differentiate between supervised and unsupervised mining techniques   [10]
3Marks
Q4
CO-3; SO-
2;
BL-4
Apply the ID3 Classification Algorithm for the given data to decide the
best split. (Calculate the root node)
- 6marks
Part 2: ID3 algorithm (6 marks)
Step 1: Compute overall entropy
• Total = 10
• Yes = 6, No = 4
********** 11 **********
--- page 12 ---
Step 2: Compute information gain
Step 3: Select root node
Final answer
• Best attribute (root node) = A1
• A1 provides maximum information gain
********** 12 **********
--- page 13 ---
Apriori   [10]
Explain the principle of the Apriori algorithm – 3marks
a.
Numerical – 7 marks
Apriori is used for association rule mining
• Based on Apriori property
Steps of Apriori algorithm
• Step 1: Generate candidate 1-itemsets (C1)
• Step 2: Calculate support and form L1 (frequent itemsets)
• Step 3: Generate candidate k-itemsets (Ck) from Lk-1
• Step 4: Prune itemsets with support < minimum support
• Step 5: Repeat until no new frequent itemsets
Q5   • Step 6: Generate rules and compute confidence
CO-1,CO-
3; SO-2;
BL-3
Given
Transactions:
• T1 → {laptop, wireless mouse, keyboard}
• T2 → {laptop, wireless mouse}
• T3 → {keyboard, wireless mouse}
• Min support count = 2
• Min confidence = 80%
Step 1: Generate 1-itemsets (L1)
Count support:
• laptop → 2 (T1, T2)
• wireless mouse → 3 (T1, T2, T3)
• keyboard → 2 (T1, T3)
********** 13 **********
--- page 14 ---
Frequent itemsets L1:
• {laptop}, {wireless mouse}, {keyboard}
Step 2: Generate 2-itemsets (L2)
• {laptop, wireless mouse} → 2 (T1, T2)
• {laptop, keyboard} → 1
• {wireless mouse, keyboard} → 2 (T1, T3)
Frequent itemsets L2:
• {laptop, wireless mouse}, {wireless mouse, keyboard}
• L1: {laptop}, {wireless mouse}, {keyboard}
• L2: {laptop, wireless mouse}, {wireless mouse, keyboard}
Step 4: Generate association rules
From {laptop, wireless mouse}
• laptop → wireless mouse
Confidence = 2 / 2 = 100%
keyboard → wireless mouse
b. KNN   [10]
K-Nearest Neighbors (KNN) classification algorithm 8marks
Relevant example – 2marks
 Training set includes classes.
 Examine K items near item to be classified.
Q5    New item placed in class with the most number of close items.
CO-1,CO-
3; SO-2;   • KNN is a supervised learning algorithm used for classification and
BL- 2   regression
• Classification is based on similarity (distance) between data points
• Uses distance metrics such as Euclidean distance
For classification problems, a class label is assigned on the basis of a
majority vote—i.e. the label that is most frequently represented around a
given data point is used.
********** 14 **********
--- page 15 ---
• Step 1: Choose value of k (number of neighbors)
• Step 2: Calculate distance between new point and all training points
• Step 3: Sort distances in ascending order
• Step 4: Select k nearest neighbors
• Step 5: Perform majority voting
• Step 6: Assign the class
********** 15 **********
--- page 16 ---
a. An energy company studies how electricity consumption varies with temperature.   [10]
The data collected is:
Temperature
20   25   30   35   40
(°C)
Consumption   200   220   260   300   340
Find the regression equation and analyze how temperature affects consumption at
temperature =42.
Q6
• X (Temperature) = 20, 25, 30, 35, 40
CO-1,CO-   • Y (Consumption) = 200, 220, 260, 300, 340
3; SO-2;
BL-4   • n = 5
• ΣX = 20 + 25 + 30 + 35 + 40 = 150
• ΣY = 200 + 220 + 260 + 300 + 340 = 1320
• ΣX² = 400 + 625 + 900 + 1225 + 1600 = 4750
y = mx + c
Regression equation: y = 7.2x + 48
• Predicted consumption at 42°C = 350.4
b. Discuss the following data mining techniques:   [10]
i. Web Content Mining – 5marks
ii. Web Structure Mining – 5marks
Web Content Mining
• Extends work of basic search engines
• Search Engines
• IR application
• Keyword based
•   Similarity between query and document
Q6 CO-
2,CO-3;
SO-2;
Web Structure Mining
BL- 3
• Mine structure (links, graph) of the Web
• Techniques
• PageRank
• CLEVER
•   Create a model of the Web organization.
• May be combined with content mining to more effectively retrieve
important pages.
Q7   a.   [10]
CO-1; SO-
2;
********** 16 **********
--- page 17 ---
BL-2   Casual or Novice User. Uses the data warehouse occasionally, not daily.
Needs a very intuitive information interface.
Regular User. Uses the data warehouse almost daily. Comfortable with
computing options but cannot create own reports and queries from scratch.
Needs query templates and predefined reports.
Power User. Is highly proficient with technology. Can create reports and
queries from scratch. Some can write their own macros and scripts. Can
import data into spreadsheets and other applications.
User types by the way they wish to interact to obtain information.
Preprocessed Reports. Use routine reports run and delivered at regular
intervals.
Predefined Queries and Templates. Enter own set of parameters and run
queries with predefined templates and reports with predefined formats.
Limited ad hoc Access. Create from scratch and run limited number and
simple types of queries and analysis.
Technical Analysts. Look for complex analysis, statistical analysis, drill-down
and slicedice capabilities, and freedom to access the entire data warehouse.
Business Analysts. Although comfortable with technology, are not quite adept
at creating queries and reports from scratch. Predefined navigation is helpful.
Want to look at the results in many different ways. To some extent, can
modify and customize predefined reports.
Business-Oriented Users.
b.   [10]
Knowledge Discovery in Databases (KDD) process with the help of a neat
Q7
diagram. 7Marks
CO2; SO2;
Discuss the issues related to KDD – 3 Marks
BL-2
KDD PROCESS
********** 17 **********
--- page 18 ---
• Selection: Obtain data from various sources.
• Preprocessing: Cleanse data.
• Transformation: Convert to common format.
Transform to new format.
• Data Mining: Obtain desired results.
• Interpretation/Evaluation: Present results to user
in meaningful manner.
KDD Issues
• Human Interaction
•   Overfitting
•   Outliers
•   Interpretation
•   Visualization
• Large Datasets
• High Dimensionality
********** 18 **********
````
