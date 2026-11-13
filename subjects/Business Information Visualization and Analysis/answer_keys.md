# Business Information Visualization and Analysis: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 7e6a1bd5c922

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/MBATech_Computer_7047/Business Information Visualization and Analysis/ANS_Business Information Visualization and Analysis(702CO1E002)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTERENGINEERING)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Business Information Visualization and Analysis
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   Marks
a.   Explain the concept of data blending in Tableau and how it
differs from data joining.
Ans: Data Blending vs Joining (5 Marks)
Data Blending: Combines data from multiple sources at
visualization level using a common field. Works like a left
join and keeps sources separate.
CO3,   5
SO6,BL2   Joining: Combines tables at data source level before
visualization (inner, left, right join).
Difference:
Blending → different sources, post-aggregation
Joining → same source, row-level merge
CO1, SO1,   b.   Write a SAS statement to display variables NAME, CITY, and
BL3   SALARY from dataset EMPLOYEE with titles COMPANY and
LOCATION.   5
Ans: title1 "COMPANY";
title2 "LOCATION";
********** 1 **********
--- page 2 ---
proc print data=EMPLOYEE;
var NAME CITY SALARY;
run;
title;
CO4,   c.   What are calculated fields in Tableau? Explain with two
SO1,BL1
examples.
Ans:
• User-defined fields created using formulas.
• Used for dynamic analysis.
5
Examples:
•   Profit Ratio = Profit / Sales
• Age Group = IF AGE > 60 THEN "Senior" ELSE
"Adult" END
CO4,   d.   Explain the role of color theory in data visualization.
SO6,BL2
Ans: • Helps in better interpretation and visual clarity
• Types:
•   Sequential → ordered data   5
• Diverging → highlight extremes
•   Categorical → distinct groups
• Avoid misuse to prevent confusion
A A retail company is analyzing customer purchase
behavior. The dataset includes:
Customer_ID, Age, Gender, Location, Product_Category,
Purchase_Amount, Purchase_Date, Payment_Mode,
Q2   Discount_Applied, Customer_Rating
[10]
CO2,   Answer the following:
SO6,BL6
• Suggest the most suitable visualization to analyze
purchase trends over time across categories. Justify
your answer.
• Explain how filters can be applied in Tableau to:
o View data for specific regions
********** 2 **********
--- page 3 ---
o Analyze purchases above a certain amount
Include steps and any calculated fields if required.
Ans:
Visualization:
• Line chart → shows trends over time across
categories
• Multiple lines for categories
Filters in Tableau:
• Drag Region → Filters → select region
• Create calculated field:
IF Purchase_Amount > 500 THEN "High" END
• Apply as filter
B   Explain the Data Visualization Process Lifecycle, including
stages such as data collection, preprocessing, visualization
design, and interpretation. How does each stage contribute to
better decision-making?
CO1,   Ans:
• Data Collection → gather data   [10]
SO1,BL2   • Preprocessing → clean, handle missing values
• Exploration (EDA) → identify patterns
• Visualization Design → choose charts
• Interpretation → insights for decisions
A   Write any three rules for naming variables in SAS.   [10]
Also, write a SAS program to create a format ‘AgeGroup’:
• Below 18 → Minor
• 18 to 60 → Adult
• Above 60 → Senior
Q3   Apply this format to AGE variable in dataset PEOPLE
while displaying NAME, AGE, and CITY.
CO1,
SO1,BL3   Ans:
Rules:
• Must start with letter or underscore
• No spaces
• Max 32 characters
********** 3 **********
--- page 4 ---
Program:
proc format;
value agefmt
low-17="Minor"
18-60="Adult"
61-high="Senior";
run;
proc print data=people;
format age agefmt.;
var name age city;
run;
B   An environmental agency wants to create a dashboard to   [10]
analyze air pollution trends and weather conditions.
Part A: Identify important dataset variables required. (3
Marks)
Part B: Mention two key insights that should be derived.
(3 Marks)
Part C: Draw and explain a suitable dashboard layout. (4
Marks)
Ans:
Variables:
CO3,
• AQI, Temperature, Humidity, Location, Date
SO6,BL6
Insights:
•   Pollution trend over time
• Impact of weather on AQI
Layout:
• KPI (Avg AQI)
• Line chart (trend)
• Map (location-wise AQI)
A   Write a SAS program to read a file ‘EMPLOYEE.csv’   [10]
from location ‘C:\Data’.
•   File does not contain headers
•   Variables:
Q4   o EMP_ID, NAME (Character, 20 bytes)
CO1,   o JOIN_DATE (Date9.)
SO1, BL3   o SALARY (Numeric)
Additional conditions:
• Data starts from second row
• Format JOIN_DATE as ddmmyy10.
********** 4 **********
--- page 5 ---
• Do not include NAME in output dataset
•   Print only first 5 observations without OBS column
Ans: data sales;
infile 'C:\Data\EMPLOYEE.csv' firstobs=2 dlm=',';
length EMP_ID $20 NAME $20;
input EMP_ID $ NAME $ JOIN_DATE :date9. SALARY;
format JOIN_DATE ddmmyy10.;
drop NAME;
run;
proc print data=sales (obs=5) noobs;
run;
B   Design a Student Performance Dashboard using Tableau.   [10]
•   Include at least 3 KPIs
•   Include charts and insights
• Explain how it helps in decision-making
Ans:
KPIs:
• Avg Marks
CO3,   • Pass %
• Attendance %
SO6,BL6
Charts:
• Bar (subject-wise marks)
• Line (performance trend)
•   Pie (pass/fail)
Use:
• Helps identify weak students & improve decisions
Q5   A A company aims to predict employee attrition using a   [10]
decision tree model based on attributes such as Age,
CO4,   Salary, and Department.
SO1,BL6   Answer the following:
********** 5 **********
--- page 6 ---
(i) Explain the concept of entropy and information gain
in decision trees. How do these measures help in selecting
the root node?
(5 Marks)
(ii) Describe the step-by-step process of constructing a
decision tree, including splitting criteria and stopping
conditions. Illustrate how categorical attributes like Age
and Department are handled.
(5 Marks)
Ans:
Entropy:
• Measure of impurity
• 0 = pure, 1 = mixed
Information Gain:
• Reduction in entropy
•   Select attribute with highest IG as root
Tree Construction:
1. Calculate entropy
2. Compute IG
3. Select best attribute
4. Split dataset
5. Repeat
Stopping:
• Pure node / no attributes
Categorical Handling:
• Each value → separate branch
B   Explain how PROC FREQ is used to generate one-way and two-   [10]
way tables. Include syntax and options used for validation.
Ans:
proc freq data=dataset;
CO4,   tables var1; /* one-way */
tables var1*var2; /* two-way */
SO1,BL4   run;
Options:
• NOPERCENT
• NOROW NOCOL
********** 6 **********
--- page 7 ---
Use:
• Frequency count
• Data validation
A   Design a Profit Analysis Dashboard for a company using   [10]
Tableau.
•   Identify KPIs
• Suggest suitable visualizations
• Explain how trends and outliers can be identified
Ans: KPIs:
•   Total Profit
•   Profit Ratio
•   Sales
Q6
Visuals:
CO3,
SO2,BL 3   • Line (trend)
• Bar (category-wise profit)
•   Scatter (profit vs sales)
Outliers:
• Use scatter plot
•   Highlight extreme values
B   Evaluate the following SAS code and determine the   [10]
output:
data merge_data;
merge emp(in=A) dept(in=B);
by ID;
run;
Explain:
CO4,
SO1,BL5   • Values of A and B
• Conditions for match merging
Ans:
merge emp(in=A) dept(in=B);
A and B:
• A = 1 if record from emp
********** 7 **********
--- page 8 ---
• B = 1 if record from dept
Match Merge Conditions:
• Data must be sorted by BY variable
• Same variable names
• One-to-one or one-to-many
A   Explain the importance of Tableau Stories in presenting data
insights.
Q7   Ans:
• Sequence of dashboards   [5]
CO3,
• Used for storytelling
SO6,BL3
• Helps in decision-making
B   Explain heat map with example.
CO2,   Ans:
• Uses color to represent values   [5]
SO6,BL3
• Example: Sales by region
C   Explain time-series visualization and its applications.
Ans:
CO4,
• Data over time   [5]
SO6,BL4
• Example: monthly sales trend
D   Explain SAS date functions with examples. Which functions
handle date differences?
Ans:
Examples:
CO1, SO1,   • TODAY()
[5]
BL2   • INTNX()
• INTCK() → calculates date difference
Note:
• Dates stored as numeric values
********** 8 **********
````
