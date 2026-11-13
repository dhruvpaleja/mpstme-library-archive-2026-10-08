# Data Mining and Analytics: question papers in full

14 unique papers · 2016-17 to 2025-26 · Common (all branches), Computer Science and Business Systems, Artificial Intelligence, Computer Engineering, Data Science, Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 9 · paper aaeb869bd0ae

- Departments: Artificial Intelligence, Computer Engineering, Data Science, Information Technology
- Programmes: MBATech AI 7051, MBATech Computer 7047, MBATech DS 7052, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_09/Final-Exam/MBATech_AI_7051/Data Mining and Analytics/QP_Data Mining and Analytics(703TM0E013)_2025-2026.pdf` (+3 identical copies)
- Printed on paper: max marks: 50; duration hours: 2
- Text: ocr (8 pages), mean OCR confidence 85.5
- 3 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2025-2026

Program/s: MBA Tech Year: V__ Semester: IX_
Stream/s : All Streams

Subject: Data Mining & Analytics Time: 2 hrs (2:00pm to 4:00pm)
Date:_20 / 12 / 2025 No. of Pages: 8

Marks: 50

Final Examination/Re-Examination (2025)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) The answers should be in word / pdf file.

6) Figures in brackets on the right hand side indicate full marks.

7) You may assume wherever necessary and clearly mention the assumptions in the answers

8) The data will be provided separately. All questions except Question 7 are based on single case.

9) The instructions about submitting soft copy of the file will be given in the Exam Hall.

10) The answers should contain answers to the questions, any assumptions, codes, outputs and interpretations

11) Plagiarism check will be conducted for the answers and appropriate disciplinary action will be conducted
for copy cases.

Case Analysis : Case Description CHR Data -Csv)

IBM’s Human Resource Analytics Division has collected detailed employee data to understand the factors that lead
to employee attrition — that is, why some employees choose to leave while others stay. The dataset includes
information on employee demographics (age, gender, education), job-related attributes (department, role, income
years at company, job satisfaction, work-life balance), and behavioral variables such as overtime, performance
rating, and career progression.

The company’s management has observed that voluntary attrition is increasing, particularly among mid-level
employees with good performance records. Replacing trained employees incurs significant costs in hiring and
productivity loss, so management wants a data-driven approach to identify employees who are at risk of leaving and
the key drivers influencing this decision.

As an HR Data Analyst, you are required to analyze the IBM HR dataset and provide actionable insights. Your analysis
should help management in designing effective retention strategies, improving employee satisfaction, and aligning
HR policies with long-term organizational goals.

You will explore this case through a series of analytical tasks — from data exploration and model building to

segmentation, association rule mining, and model evaluation — connecting each technique to its managerial
interpretation.

EmplD: Employee ID

Age: Age of the employee

AgeGroup: Age group to which the employee belongs

Attrition: Employee attrition status (whether the employee has left the organization or is still active)
BusinessTravel: Frequency of business travel for the employee

DailyRate: Daily rate of pay for the employee

Department: Department in which the employee works

DistanceFromHome: Distance in miles from the employee’s home to the workplace
Education: Level of education attained by the employee

EducationField: Field of education of the employee

EmployeeCount: Number of employees

EmployeeNumber: Unique identifier for each employee

EnvironmentSatisfaction: Employee’s satisfaction level with the work environment

0
--- page 2 ---
Gender: Gender of the employee
HourlyRate: Hourly rate of pay for the employee
Jobinvolvement: Employee’s level of job involvement
JobLevel: Level of the employee’s job position
JobRole: Role of the employee within the organization
JobSatisfaction: Employee’s satisfaction level with their job
MaritalStatus: Marital status of the employee
Monthlyincome: Monthly income of the employee
SalarySlab: Categorization of monthly income into salary slabs
MonthlyRate: Monthly rate of pay for the employee
NumCompaniesWorked: Number of companies the employee has worked for in the past
Over18: Whether the employee is over 18 years old
OverTime: Whether the employee works overtime or not
PercentSalaryHike: Percentage increase in salary for the employee
PerformanceRating: Performance rating of the employee
RelationshipSatisfaction: Employee's satisfaction level with work relationships
StandardHours: Standard working hours for the employee
StockOptionLevel: Level of stock options granted to the employee
TotalWorkingYears: Total number of years the employee has worked
TrainingTimesLastYear: Number of training sessions attended by the employee in the last year
WorkLifeBalance: Employee’s work-life balance satisfaction level
YearsAtCompany: Number of years the employee has worked at the current company
YearsInCurrentRole: Number of years the employee has been in the current role
YearsSinceLastPromotion: Number of years since the employee’s last promotion
YearsWithCurrManager: Number of years the employee has been working with the current manager
Using this case answer questions 1 to 6. Question 7 is independent of the case.

Exploratory Data Analysis
Perform an exploratory analysis of the dataset. Identify variable types, handle missing

a coz, | Values, and visualize key trends related to the target variable attrition
03; Explore key variables (e.g., Age, MonthlyIncome, JobSatisfaction, YearsAtCompany,
BL WorkLifeBalance, etc.). {10}
Pieri Create new variable “Engagement Index” using following formula
evaluate Engagement Index = (SobSatisfaction + EnvironmentSatisfaction +
RelationshipSatisfaction + WorkLifeBalance) /4
Summarise your findings in the form of insights useful for management.
Logistic Regression with Regularization (Ridge/Lasso)
Q2 Build a logistic regression model to predict Attrition (Yes/No).
co1,cO2, | Use key variables: Age, MonthlyIncome, YearsAtCompany, JobSatisfaction,
“ WorkLifeBalance. 130)
Understand, | Interpret the coefficients and explain their business meaning.
Analyse, Fit logistic regression models with regularization to predict the target variable. Compare
Evaluate model coefficients from Ridge and Lasso and interpret the managerial meaning of
significant predictors.
Q3
c01,C02, | Following is the output of Trees for above case. Answer the questions mentioned at the end of this
603; question
BL- A q [10]
Understand, Classification Tree
Analyse, Model Summary
Evaluate
--- page 3 ---
Atintion

Node O
Category % na
ENO 83.9 1233
mYes 104_237
Tetal_ 100.0 1470

OverTime
Imprevement=0.016

No Miz
Node 4 Node
Category % ategory % on
E No woe o4a No 605 230
WYes 404 440 Myer 305 127
Total 717 1054 Total 283 416
EI =e
TotalWekingYears Monthlytncome
Impravement=() 007 Imptovement=0 017
26 +25 <= 24750 > 2075.0
i
Node 9 Nodes NedeS Nodes
Category % n _ Category % on Category % in * on
nN 070 (68 BN 916 885| |B No m4 24 772 2068
BYes 330 20 Ses a4 _91| |@yYes 806 48 22873)
Total 60 oe Total 057 000 Total a7 23.0 347
at
NumCompaniesWoked JodRole
Improvement=0.002 Improwement=0 007
60;70,50 10:80,3.0;20,0.0,40.0.0 Laboratory Technician, Sales Human Resources; R.

Representative, Sales Executive Scientist, Healtho
Manufacturing Director; Manager;
Resaaroh Direoter

Node? Node S Nodes Node 10
Category % 5 Category % 2 Category % o Category % a
SNe O27 120 Ne 93.3 750 B Ne $33 =Ne e75 175
Total 10.0 156 Total 55.1 610 Teta! 100 147 Total 436 200

MStatus
Improvement=0 008

20. ‘ine 4 arg He | Married
Node 11 Node 12 Node 13 Node 14
Category % nm Category _% a Category % a Category _% of
eNe O71 Be Ne 7Oe 64 mNe goo 618 TR No 723 «76
|S Yes 29 2 |S Yes 201 26 Yet B40 32 Byes 227. 22
Total 48 70 Total 5c 86 Total 34 SO Total os 97
Tree Table
No Yes Total P Primary Independent Variable
a
r
Predi e
Node Po cted n Impr
N Percent N Percent N Categ t Variable ove Split Values
ent Ol N
ny) ment
°o
d
e

O 1233 83.90% 237 16.10% 1470 100% No

0.01

1 944 89.60% 110 10.40% 1054 72% No QO OverTime 6 No
2 289 69.50% 127 30.50% 416 28% No 0 OverTime = Yes

Be 59! 67.00% | 29/| 3300%| 88| 6% |No | 1| (otalWorkin| 000) _),

gYears 7

4 885   9160% 81 840% 966 66% No aefances Working = 0.000 Sars

gYears 7
--- page 4 ---
5 21 30.40% 48

6 268 77.20% 79

U 129 82.70% 27

8 756 93.30% 54

9 93 63.30% 54

10 175 87.50% 25

11 68 97.10% 2

12 61 70.90% 25

13 18 36.00% 32

14 7 77.30% 22

69.60%

22.80%

17.30%

6.70%

36.70%

12.50%

2.90%

29.10%

64.00%

22.70%

69

347

156

810

147

200

70

86

50

5% Yes

24% No

11% No

55% No

10% No

14% No

5% No

6% No

3% Yes

7% No

6

6

Monthlyinc
ome

MonthlyInc
ome

NumCompa
niesWorked

NumCompa
niesWorked

JobRole

JobRole

Environmen
tSatisfaction

Environmen
tSatisfaction

MStatus

MStatus

0.01

0.01

0.00

0.00

0.00

0.00

0.00

0.00

0.00

<= 2475.0

> 2475.0

6.0; 7.0; 5.0

Laboratory
Technician;
Sales

Representative

; Sales
Executive

Human
Resources;
Research
Scientist;
Healthcare
Representa’

tive

Manufacturing |

Director;
Manager;
Research
Director

2.0; 4.0

1.0; 3.0

Single

Divorced;
Married

Growing Method: CRT
Dependent Variable: Attrition
--- page 5 ---
Risk

Method Estimate Std. Error
Resubstitution 133 .009
Cross-Validation -154 -009
Growing Method: CRT
Dependent Variable: Attrition
Classification
Predicted
Observed No Yes Percent Correct
No 1194 39 96.8%
Yes 157 80 33.8%
Overall Percentage 91.9% 8.1% 86.7%
Growing Method: CRT
Dependent Variable: Attrition
Independent Variable Importance
Normalized

Independent Variable Importance Importance
Monthlyincome 024 100.0%
TotalWorkingYears .019 80.8%

| Overtime(OT) .016 68.2%
JobRole 013 53.7%
EnvironmentSatisfaction .008 34.8%
MaritialStatus(Mstatus) .008 31.9%

| MonthlyRate .004 14.6%

| YearsSinceLastPromotion .003 10.8%
DailyRate .003 10.8%

| Department .003 10.7%

| NumCompaniesWorked .003 10.7%

| AgeGroup 002 10.3%
WorkLifeBalance 002 10.0%
EdField 002 7.8%
PercentSalaryHike .002 74%
JobLevel 002 6.9%
YearsInCurrentRole -001 6.1%
TrainingTimesLastYear .001 5.8%
YearsAtCompany .001 4.7%

SalarySlab -001 3.6%
DistanceFromHome .001 3.3%

| RelationshipSatisfaction .001 3.1%

| JobInvolvement 001 2.6%
HourlyRate .000 1.3%
Education -000 0.9%

JobSatisfaction 000 0.6%
PerformanceRating 7.830E-7 0.0%

Growing Method: CRT
Dependent Variable: Attrition

e
--- page 6 ---
Normalized Importance

a 2 40 Co a0 100

Montntyincome:

or

EnvronmentSstafaction

A MontheyRate
a

s DatyRate
=

$§ NumCompaniesvorked

¢€ Werk teBelance

3 PercertSaimyitie

SS YewsrcurertRoe
a

3 YearsAtCompany

£ DistanceFromtome |
dobinvalvement
Education
PertormanceRating |
900% 0.005% onto. 015% 0.020% 0.025%
Importance
Growing Method CRT
Dependent Vanable Attntiont®

Answer following questions
a) Explain the tree output. How many splits the tree has?
b) What is the classification accuracy? Is it adequate?
c) According to this output, which variable contributes maximum to the classification?
d) How would you classify Employee with following values? Also mention probability of

Attrition
Total lial Mont Environme
me ng - P Incom Satisfactio | Status(Mstatus)
years e n
Feature worked
Sales
Yes 4 3 | 5000 | Executiv 3 | Single
Value e
e) How would you classify Employee with following values? Also mention probability of
Attrition
Total — Mont Environme
me ng ma P Incom Satisfactio | Status(Mstatus}
years e n
Feature worked
Sales
No 8 3} 8000 | Representati 4 | Single
Value ve
f) Consider top 5 important features for predicting attrition and give insights useful for
= management
Decision Tree and Random Forest Models
aa Build both a Decision Tree and a Random Forest classifier for predicting Attrition.

co1,coz, | Compare accuracy, identify top predictors, and suggest managerial actions.
Cco3; OR

es Dimensionality Reduction — PCA and PLS

Analyse, Apply Principal Component Analysis (PCA) and Partial Least Squares (PLS) to reduce
pour feature dimensionality. Visualize the explained variance and interpret the components from a

managerial perspective.

[10]
--- page 7 ---
as Beyond Linearity — Polynomial / Non-linear Patterns
co1,coz, | Examine if Age or YearsAtCompany have a non-linear relationship with attrition
BL- probability. [10]

aa Use polynomial logistic regression or plots to visualize the pattern.
Clustering for Employee Segmentation
Use K-Means clustering with variables like Age, MonthlyIncome, YearsAtCompany, and
JobSatisfaction.
a6 Identify and describe 3 employee segments.
ra Oe Association Rule Mining 110]
Understand, | Identify behavioral patterns associated with attrition using association rules.
Analyse Use categorical attributes like OverTime, JobSatisfaction, MaritalStatus, and Department.
Interpret the top 2-3 rules with high lift values.
A CNC machine tool is used to perform a variety of manufacturing operations. The attributes of the
product which are important to customers were identified, and then the levels for each attribute
that the company is willing to design and offer to a customer.
A conjoint analysis was performed for product design of an industrial machine tool.
The three important attributes of a CNC machine tool are:
1. Setup time in minutes. This is the time it takes to prepare or setup the machine for operations.
2. Delivery period in days. This is the time the manufacturer needs to deliver after the customer has
placed an order.
3. Price
These are the three attributes. The levels of these attributes were defined as follows
1. Setup time - 3 minutes, 6 minutes, 9 minutes, 12 minutes (4 levels)
2. Delivery period - 18 days, 22 days, 28 days (3 levels)
3. Price 2000000 2500000 3000000 (3 Levels)
These levels are the options that the manufacturer are willing to consider in design and delivery of
Q7 the machine.
C01, co2, 7
Bl-Apply, || Setup Time | Delivery Price - (10)
Analyse, period Setup Time   X1 X2 x3
Evaluate i
3 minutes | 18 days 2000000 3 minutes 1 0 0
6 minutes _| 22 days 2500000 ane oe
9 minutes _| 28 days 3000000 ue re
| 12 minutes = 12minutes = -1 -1 -1

The variables were coded as follows

Delivery Period x4 x5 Price X6 X7
18 Days 1 0 2000000 1 ()
22 Days 10) 1 2500000 19) 1
28 Days -1 -1 3000000 -1 -1

The output is given below
| Note that the rankings are assumed to be best is highest
--- page 8 ---
Variables Entered/Removed

Variables Variables
Model Entered Removed Method
1 x7, x5, x3, x2, x6, .|Enter
x4, x18

a. All requested variables entered.

Model Summary”

Adjusted R Std. Error of the
Model R R Square Square Estimate Durbin-Waison

1 -998" .996) .994 .27802| 2.478
a. Predictors: (Constant), x7, x5, x3, x2, x6, x4, x1
b. Dependent Variable: y

ANOVA
Model Sum of Squares df Mean Square F Sig.
4 Regression 13113.944 7 1873.421 24237.379 .0004}
Residual 3.556 46 .077
Total 13117.500 §3

a. Predictors: (Constant), x7, x5, x3, x2, x6, x4, x1
b. Dependent Variable: y

Coefficients?
Standardized
Unstandardized Coefficients Coefficients

Model B Std. Error Beta t Sig.

1 (Constant) 23.500 .038! 726.867 .000)
x1 6.000) 054} -.314) = -112.139 .000
x2 .710 -054| -.049 12.44 .034|
x3 -1.500 .038 -.096 -39.647 .000}
x4 12.899 .054 .048 13.344) .044)
x5 2.000) .054 943 336.418 -000}
x6 5,889) .054 047 16.613 .000
x7 1.111 -054| .006 2.077 .043

a. Dependent Variable: y

Answer following
a) Find the utility for each attribute at each level and Comment on the output
b) Find the percentage utility for each attribute.
c) Draw the graph of the utility for each attribute
d) Which of the attribute is most important while considering the tool? Why?
e) If you launched a Machine with setup time 6 minutes, delivery period 22 days, and price
2500000/- What is the utility for this machine? Give business interpretations for this value.

Pererrer rT errr
````

## 2024-25 · Final-Exam · Sem 9 · paper 450c48323389

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data Mining & Analytics, Final Exam 2024-25.pdf`
- Printed on paper: max marks: 50; duration hours: 2
- Text: ocr (12 pages), mean OCR confidence 82.3
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& EN
Academic Year: 2024-2025 ahi Ne
Program/s: MBA Tech Year: V__ Semester: IX_

Stream/s : All Streams ae

Subject: Data Mining & Analytics ; Time: 2 hrs (2:00pm to 4:00pm)
Date:__21/ 12 / 2024 No. of Pages: 12

Marks: 50

Final Examination (2024-25) _

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any 4. __ questions.
3) In all__5_ questions to be attempted.

és 4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate fulHmarks.
7) Assume Suitable data if necessary. a
Qi a.
C01, CO2;
BL- What is the difference between classification trees and regression trees? (3]
Understand,
Analyse
b. A Business school has sought consultancy from an institution specialising in
advisory services to corporates in order to refine the process at the school to
as improve the students chances for a better corporate career. The objective was to
C01, co2: identify factors that drive campus placement annual salary. Among other
BL- variables selected for analysis following two variable information is given below 4
Understand, 7 |
Analyse, . . 7 x
A| evaluate Independent Variable : Gender (Male : M, Female:F)

Dependent Variable : Annual Salary
--- page 2 ---
Gender

BOOOK a

QD
2S500K
oo
2eooK ‘a
=
=
aco00K . ;
sooKk
ox
= m
Min. Annual Avg. Annual Max. Annual Std.dev.of Median Annual 5
Gender salary salary salary Annual salary - salary
F 849,042 1,348,168 2,757,551 502,853 1,145,832
M 849,545 1,384,749 2,926,510 455,195 1,273,046
Give your conclusion about “Gender” variable vs Campus Placement Annual
Salary using these two visualisations. Also mention how the business school can
use this information for improving placement salary, if applicable.
Qu
—, co2 Describe two Business scenarios for using Mann-Whitney U Test
BL- [3]
Understand, iy
Analyse
Q2 What are the advantages of using subset selection methods (like best subset selection)
C01, C02, over regularization methods like Ridge and Lasso?
C03;
BL- [10]
Understand, How does cross-validation help in selecting the tuning parameter for regularization
Analyse methods?
Q3 What are Support Vector Machines? How do you tune SVM parameters, and what are
c01, Co2, ;
= the ke meters to adjust?
BL- y para just [10]
Understand,
Analyse
Qa Explain the concept of basis functions and how they are used in regression models.
C01, Co2
BL- [5]
Understand,
Analyse
Q4 What is a regression spline, and how is it different from polynomial regression?
cO1, Co2
BL- [5]
Understand,

Analyse
--- page 3 ---
an

as

coi, CO2
BL-
Understand,
Analyse,
Evaluate

With increased market fragmentation & price wars in food and beverage sector, it
has become important to gain insights from the customers themselves ‘about the
brand in order to improve customer acquisition & retention. Baskin Robins ice
cream is sold only in the Baskin Robins retail outlets. Therefore it is essential for
them to gauge customer perceptions about the brand so that. they get an
understanding as to how they are placed in the market and what all they can do so
as to improve their position. This paper aims to provide Baskin Robins with useful
information like which all categories of customers prefer Baskin Robins, in what
parameters it lacks behind its competitors and where it is strong. Thus data has been
effectively used to formulate important results for the growth of the business.

The data used is a survey about Baskin Robin’s ice cream to gain insights about the
customer perception of this brand. It has been carried out to basically generate
feedback about the company so that it can improve upon the qualities it lacks.
56 people have participated. The data set involves the detecting Baskin Robins
performance on 12 measures. All these variables involve customers to rate Baskin
Robin for different characteristics on a scale of 1-5.
These brand characteristics in the data sheet are:

e Rate Baskin Robins on taste

e Rate Baskin Robins on number of flavours

e Rate Baskin Robins on Indiag flavours

e Rate Baskin Robins on packaging

e Rate Baskin Robins on availability

e Rate Baskin Robins on promotional offers

e Rate Baskin Robins on service

e Rate Baskin Robins on advertising

e Rate Baskin Robins on value for money

e Rate Baskin Robins on availability in different sizes

e Rate Baskin Robins on expensiveness   «

e Rate Baskin Robins on status symbol

A factor Analysis was done on the data and the output is given below

Factor Analysis
KMO and Bartlett's Test
Kaiser-Meyer-Olkin Measure of Sampling Adequacy. -786
Bartlett's Test of Sphericity Approx. Chi-Square 182.448
df ‘ 36
Sig. .000

[10]
--- page 4 ---
Anti-image Matrices

number | Indian promot Adve | value
of flavour | packa | avail | ional | Servi] rtisin for
taste_| flavours s ging |ability| offers | ce g__|_money
Anti taste 398 -.239| -.020] -.039] .060} -.106] .052 -.051 -.157
- number of -.239 -398} -.083} -.015] -.036 129} -.181] .111 .057
ima flavours : ¥
9 Indian -.020] -.083] 635] -.085] -.216] -.028] .001}-.040] 025
Cov flavours
noe packaging -.039} -.015| -.085| .647] -.097) -.098|-.013] -.064|   -.059
availability .060 -.036| -.216}] -.097] .576} -.130}-.024] .080 -.117
promotional -.106 129} -.028} -.098] -.130: 523 | -.122 | -.076 -.046
offers "
Service .052 ~.181 .001} -.013} -.024] -.122] .429] -.215 -.086
Advertising -.051 111 -.040} -.064] .080] -.076]-.215] .626 -.035
value for -.157 .057 -025| -.059] -.117] -.046 | -.086 |} -.035 569
money
Anti taste 7318 -.601 -.039] -.077} .125] -.232] .125] -.101 -.330
7 number of --601]. .6199} -.165] -.030] -.076] .282]-.439} .222 .119
ima flavours
ae Indian -.039] -.165} .8599] -.132] -.357] -.049] .002]-.063}   .042
fae flavours
on packaging -.077 -.030] -.132] .9287] -.158] -.169] -.024] -.100 -.098
availability 125 -.076] -.357] -.158] .8037} -.236]-.048] .133 -.204
promotional -.232 282] .*.049] -.169] -.236] .819%} -.258} -.132 -.085
offers
Service 125 -.439|» 002] -.024] -.048] -.258].7797| -.415 -.175
Advertising -.101 222] -.063] -.100] .133] -.132]-.415] .7548 -.058
value for -.330 119 042} -.098] -.204] -.085]-.175] -.058 8664
money
a. Measures of Sampling Adequacy(MSA)
Communalities
Initial Extraction
Rate Baskin 1.000 775
Robbins on taste od.
Rate Baskin 1.000 881] >
Robbins on
number of :
flavours .
Rate Baskin 1.000 .650
Robbins on Indian
flavours
Rate Baskin 1.000 -531
Robbins on
packaging
Rate Baskin 1.000 -761
Robbins on
availability
Rate Baskin 1.000 .675
Robbins on
promotional offers
Rate Baskin 1.000 692
Robbins on
Service
Rate Baskin 1.000 .758
Robbins on
Advertising
Rate Baskin 1.000 528
Robbins on value
for money

Extraction Method: Principal Component
Analysis.
--- page 5 ---
Total Variance Explained as

Extraction Sums of Squared Rotation Sums of Squared

Co Initial Eigenvalues Loadings Loadings

mp % of

one Varian | Cumulat |” % of Cumulati % of | Cumulati
ot Total | ce ive % | Total | Variance ve % Total_| Variance| ve % :

4 4.121| 45.789) 45.789] 4.121 45.789| 45.789] 2.175] 24.168] 24.168
2 1.128] 12.533] 58.322] 1.128 12.533| 58.322] 2.090] 23.224] 47.393
3 1.002] 11.131] 69.453} 1.002 11.131] 69.453] 1.985] 22.060] 69.453
4 .675| 7.498} 76.951

5 .577| 6.408] 83.359
6 .483| 5.366] 88.725

7 463| 5.147] 93.872

8 .355} 3.946] 97.818 ao
9 196} 2.182] 100.000 eh,

Extraction Method: Principal Componént Analysis.

Scree Plot

4

4

® 3

in 24

14

4

4 2 3 4 5 6 7 8 a

Component Number
--- page 6 ---
Component Matrix*

Component
4 2 3

Rate Baskin Robbins on taste .731 -.410 -.270
Rate Baskin Robbins on number 622 -.675 -.195

of flavours

Rate Baskin Robbins on Indian 635] + -.163 ATO}
flavours :
Rate Baskin Robbins on 683 . 147 .209
packaging

Rate Baskin Robbins on 649 -050 .580
availability

Rate Baskin Robbins on .706 416 .058
promotional offers p :

Rate Baskin Robbins on Service 771 063 | -.305
Rate Baskin Robbins on 552 519 -.429
Advertising :

Rate Baskin Robbins on value 715 .086 ~-.095

for money

Extraction Method: Principal Component Analysis.

a. 3 components extracted.

Rotated Component Matrix? x
: Component
4 2 3

Rate Baskin Robbins on taste ? 298 .199 804
Rate Baskin Robbins on number 025 -186 919

of flavours

Rate. Baskin Robbins on Indian .055 748 .297
flavours

Rate Baskin Robbins on 406 .577 * 182
packaging

Rate Baskin Robbins on -150 853 -102
availability PY

Rate Baskin Robbins on 667 478 044
promotional offers

Rate Baskin Robbins on Service 646 212 479 ~
Rate Baskin Robbins on .868 -.001 060
Advertising

Rate Baskin Robbins on value 529 349 356
for money

Extraction Method: Principal Component Analysis.
Rotation Method: Varimax with Kaiser Normalization.
a. Rotation converged in 5 iterations.
--- page 7 ---
Component Transformation Matrix

Component 4 2 3

1 599 591 540
2 650 035 ~.759 z

3 -467 806 -.363

Extraction Method: Principal Component Analysis.
Rotation Method: Varimax with Kaiser Normalization.

Answer following questions
a) Identify and name the factors
b) Is there any variable/s which should not be included in the analysis?
Explain with.reasons. A
c) What would you conclude from scree plot?
d) Can you say that factor analysis is relevant in this case? Why?
e) Which factor is most important for this data?

A

Q.6
c01,-CO2,
BL- Apply,
Analyse,
Evaluate

A company entering premium chocolate segment wants to decide the price for
their product. They considered four attributes for this. The attributes and their
levels is given below.

Price Sugar Flavour Type
90 Sugar Nuts Bar
100 No sugar Orange Box
110 Milk Mini

“

The variables were coded as follows

Price X1 X2 Sugar; x3

90 1 0 Added sugar 1

100 0 1 No Added sugar-1

110 “i -1
Flavour x4 x5 Type X6 X7
Nuts 1 0 Bar — 1 0
Orange 0 1 Box 0 1
Milk -1 -1 Mini -1 -1

The SPSS output is given below
Note that the rankings are assumed to be best is highest

[10]
--- page 8 ---
Variables Entered/Removed

Variables Variables
Model Entered Removed Method
1 x7, x5, X3, x2, ./Enter : : ¥
x6, X4, x18

a. All requested variables entered.

Model Summary»

R
Squar Adjusted R Std. Error of the
Model R e Square Estimate Durbin-Watson
i .9989} .996) 994] 27802) 2.478}

a. Predictors: (Constant), x7, x5, x3, x2, x6, x4, x1

b. Dependent Variable: y

ANOVA?
Model Sum of Squares |. - _ df Mean Square F Sig.
1 Regression 13113.944| 7 1873.421 24237.379) 0008
Residual 3.556] 46 .077
Total 13117.500| 53

a. Predictors: (Constant), x7, x5, x3, x2, x6, x4, x1
b. Dependent Variable: y :
Coefficients?

Standardized
Unstandardized Coefficients “Coefficients

Model B Std. Error Beta . t Sig.

4 (Constant) 23.500) .038 726.867, .000}
x1 : 6.000 .054 ' -.314) = -112.139 .000
x2 -710 .054 -.049 12.44) 034
x3 -1.500 .038) -.096 -39.647 .000
x4 2.000 054} 943] 336.418; -000
x5 42.899) 054 .048 13.344 044)
x6 -1.889 054 .047 16.613 .000}
x7 4.111 .054 .006 2.077 .043

a. Dependent Variable: y
Answer following .
a) Find the utility for each attribute at each level and Comment on the
output
b) Find the percentage utility for each attribute.
c) Draw the graph of the utility for each attribute
--- page 9 ---
(|

d) Which of the attribute is most important while considering the chocolate?
Why? , :
e) Ifyou launched a new chocolate with following features, what will be the
utility for this chocolate? Give business interpretations for this value.
Price Sugar Flavour Type i
100 No sugar Orange Box

Q7

coi,
C02,CO3
BL- Apply ,
Analyse,

Evaluate

The success of marketing campaigns can be highly specific to the product, the target
audience, and the campaign methods. In this problem, we examine data from direct
marketing campaigns of a Portuguese banking institution between May. 2008 and
November 2010. The marketing campaigns were based on phone calls. Often, more than
one contact to the same client was required, in order to access if the product (bank term
deposit) would be or not subscribed.

In this analysis, the goal would be predicting the dependent variable y, which takes value
Lif the client subscribed to a term deposit, and 0 otherwise. The data we will be using

bank.csv is a subset of the original data, containing 2500 examples and 20 input variables.
The variable information is as follows:

Variable Description

age _| Age of the customer

job type of job ”

marital marital status ._

education Shows the level of education of each customer

default Whether acustomer has credit in default

housing Does the customer have a housing loan?

loan Does the customer have a personal loan?

contact The contact communication type

month Last contact month of year

day_of_week Last contact day of Week

duration Last contact duration in seconds (Note: this variable is not known
before making the call) ° :

campaign Number of contact performed for the client during the campaign

pdays number of days that passed by after the client was last contacted frd
campaign (value of 999 means the client-was not previously contactd

previous number of contacts performed before this campaign and for this
client :

poutcome outcome of the previous marketing campaign

emp.var.rate employment variation rate - quarterly indicator

cons.price.idx consumer price index - monthly indicator

cons.conf.idx consumer confidence index - monthly indicator

euribor3m euribor 3 month rate - daily indicator

nr.employed number of employees - quarterly indicator

y Output Variable — weather the customer subscribed to

Term Deposit or not? Y= Yes =1

Decision Tree was constructed on this data using 10 fold Cross validation. The output is
given below:

Classification Tree

[10]
--- page 10 ---
y

Noded

Category % fn
prt tt ™ 0.000 87.7 2170 ‘
120.000 | @ 4.000 12.3 306

_ Total 100.0 2475 ‘ od

[=
nremployed
Improvement=0.024

<= 6087.65 > 5087.65

Node 1 ; Node 2
Category % on Category % on
"0.000 588 183] |#o0.000 91.8 19087
4.000 41.2 128] | 4.000 B2 4177
Total 12.6 344 Total 87.4. 2164
ve
Improvement=0.008

989.0; 20.0; 2.0: 7.0; 15.0;12.0 4,0; 6.0; 3. 1.0; 27.0; 13.0; 0.0;
14.0; 5.0; 26.0; 16.0

Node Node 4
Categoy % on Category % on

§0.000 87.4 185 ™0.000 35.0 28

i000 329 76 M4000 65.0 62
Total 93 231 Total 3.2, 80

. Tree Table

Pre
dict
“ed
Cat Paren
: egor t
0 1 Total y Node Primary Independent Variable
Imp
rov
Nod ° Perce . Variabl - em .
e N Percent N nt N Percent : e ent__ Split Values
0 2170 87.7% 305 12.3% 2475 100.0%, + 0
1 183 58.8% 128 41.2% 311 12.6% 0 O nrempl = .02 <= 5087.65
oyed 4
2 1987 91.8% 177 8.2% 2164 87.4% 10} O nrempl .02 > 5087.65
oyed 4
3 155 67.1% 76 .32.9% 231 9.3% 0 “1 pdays -00 999.0; 20.0;
5 2.0; 7.0; 15.0;
12.0
4 28 35.0% 52 65.0% 80 3.2% 1 1 pdays 00 4.0; 6.0; 3.0;
. 5 9.0; 1.0; 27.0;
16.0
Growing Method: CRT
Dependent Variable: y
Classification
Predicted
Observed 0 4 Percent Correct
oO : 2142 28 98.7%
= 4 253 52 17.0%
Overall Percentage 96.8% 3.2% 88.6%

Growing Method: CRT
: Dependent Variable: y

Independent Variable Importance

Normalized
Independent Variable Importance Importance
--- page 11 ---
oe

_nr.employed . 024 100.0%

Suribor3m_ 022 92.3%

_pdays ee _ 2021 87.9% _
poutcome -.018 75.6% i
cons.confidx 011 44.8%

empvarrate .009 38.7% a
cons. price.idx .007 29.1% ~
month .005 21.9%

_previous .005 19.3%

age .003 11.4%

job .002 8.1%

Growing Method: CRT
Dependent Variable: y

Normalized Importance

EJ 0 cy 2 100

ko
f

005% 010% Te Opiex 020% 025%
Importance
Growing Method:CRT
Dependent Varable:y

Classification table for Stepwise Logistic Regression
Classification Table*

Predicted
y

Observed 0 4 Percentage Correct
Step1y oO 2153 17 oe 99,2
_ 1 294 14 3.6
Overall Percentage 87.4
Step2 oO. 2138 32 : 98.5
1 261 44 14.4
Overall Percentage : 88.2
‘Step3 y   O. | 2144 26 98.8
1 _ 266 39 12.8
Overall Percentage 88.2
Step4y oo. 2145 25 98.8
fs 267 38 _ 12.5
Overall Percentage 88.2

a. The cut value is .5600
Answer Following questions
a) Explain the tree output : How many splits the tree has?

b) Explain each split in terms of variables

c) What is the classification accuracy? Is it adequate?

d) According to this output, which variable contributes maximum to the
classification?

e) Astepwise regression classification accuracy is given in the output. Can you say
that the cart model is preferred over logistic regression? Why?

f) For someone with following values, How would you predict the person with
following values? Also mention probability of default.
--- page 12 ---
age 36

job Admin

month Jul |
pdays 999

previous 0. P s
poutcome nonexistent

emp.var.rate 14

cons.price.idx 93.918.

cons.conf.idx . -42.7

euribor3m 4.962

nr.employed 5228.1

g) For someone with following values, How would you predict the person with
following values? Also mention probability of default.

age 49
job housemaid

month May

pdays 14
previous Le 0
poutcome nonexistent | .

emp.var.rate . Bs
cons.price.idx 93.994
cons.conf.idx -36.4
euribor3m 4.86
nr.employed 5000

````

## 2023-24 · Final-Exam · Sem 9 · paper b72d477202a4

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data Mining & Analytics , Final 2023-2024.pdf`
- Text: ocr (8 pages), mean OCR confidence 83.6
- 3 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
fo SVIKM’s NMIMS
" MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS E

Academic Year: 2023-2024

Program: MBA Tech Stream ;_ ALL Streams (Elective) _ Year: VV 1.
Subject: Data Mining & Analytics Time: 2 _ hrs oo y
Date:_15_ / 12 /23 : No. of Pages:_| i

Marks: __50

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No: _1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi a.
C01, C02;
BL- Explain in brief Bagging and Boosting Also differentiate between the two [3]
Understand,
Analyse
b. A bank wants to review some of their loans to understand what causes borrowers to
default. They've constructed a data set from loans issued over a five-year period. They
want you to analyze the data and predict if the loan will be fully paid.
Independent Variable : Address (Years at current Address)
Dependent Variable : Default
default = 1: defaulted
default = 0: not defaulted
Default .
CO 35 @.
Qt 30

C01, C02;

BL- a 6 ‘
Understand, = 4]
Analyse, 20
a
evaluate 3
3
Z is

0
8 : 4
Defauit Median Address Avg.Address Max. Address = Min. Address Std. dev. of Addr..
0 8.00 8.95 34.00 0.00 7.00
1 800 6.39 _ 29.00, 9,00 _, $93
--- page 2 ---
Give your conclusion about “Address” variable vs Default variable using these
two visualisations. Also mention how the bank can use this information, if }
applicable. (4 Marks)

¥

a

You are a branch manager and are conducting a research on the requirement of

loans by your existing account holders. You have considered following variables

1)Age___—‘Years

2) Gender (Male/ Female)

3) May take loan in time(Variable name : Loan Period) (1 week, 1 month, 3
; months, 6 months, more than 6 months, never)

Qi
c01, Coz 4) Possible requirement of loan (Variable name : Loan Amount)
C03; Rs
BL- —— ; 13]
Understand, 5) Have you taken loan before(Variable name : Loan taken)?’
Analyse, (Yes/No)
Evaldate 6) Rate your banking experience with the branch (Variable name : Bank
| Rating)(1 to 10, 1-very bad ... 10-very good)

Suggest a non-parametric test for the following situation, Also mention the null

and alternate hypothesis for the test. :

You want to establish relationship between Loan amount and Loan taken.

State Disadvantages of nonparametric tests.
on 02, - When does regularization becomes necessary in machine learning? Explain the
C03; difference between L1 and L2 regularization. Which of these regularization methods is (10)
BL- more likely to result in sparse solutions? Discuss advantages & disadvantages of these
Understand, methods
Analyse
a3 Critically assess the limitations of the Maximal Margin Classifier and Support
C01, CO2, Vector Machines, particularly in scenarios where data is not linearly separable.
BL- ' What are the common strategies to handle such situations, and what trade-offs do | [10]
pari they involve?
Qa Critically examine the role of polynomial regression, step functions, and basis
Con C0? functions in moving beyond linearity. How do these techniques improve predictive 110)
Understand, |, modeling compared to traditional linear regression?
Analyse

; A Financial analysis firm conducted a study on factors affecting consumers
selection of financial products. The questions in the survey were asked on rating
scale of 1 to 7. The variables considered are listed below
Sr Sr
No | Variable Description No | Variable Description
Depth of products and
con co? services to meet the range Representative knowing your overall
BL- 1 | of your investment needs 6 | situation and needs
Understand, Ability to resolve 110}
Analyse, 2 | problems 7 | Degree to which my provider knows me
Evaluate - a . = ri
Multiple providers' Likelihood to Recommend Primary
3 | products to choose from 8 | Provider to Someone I Know

Likelihood of Continuing to Use
Primary Provider at Least at the Same
4 | Quality of advice 9 | Level as Now

5 | Knowledge of representatives or advisors you deal with

5!
--- page 3 ---
A factor analysis was conducted on the data and the results

KMO and Bartlett's Test

are given below

a

Kaiser-Meyer-Olkin Measure of Sampling Adequacy. 0.811
Approx. Chi-Square 1520.784

Bartlett's Test of

Sphericity at 36
Sig. 0

Communalities
Initial Extraction

Depth of products and services to meet 0.489 0.696 ,

the range of your investment needs

Ability to resolve problems : 0.431 0.516

ae providers’ products to choose 0.444 0.543

Quality of advice 0.546 0.608

Knowledge of representatives or advisors 0.586 0.635

you deal with

Representative knowing your overall 06 0.723

situation and needs

Degree to which my provider knows me 0.576 0.624

Likelihood to Recommend Primary 0.388 0.623

Provider to Someone | Know

Likelihood of Continuing to Use Primary

Provider at Least at the Same Level as 0.357 0.575

Now :

Extraction Method: Principal Axis Factoring.
SCREEPLOT
6

Total Variance Explained

aie tenet Extraction Sums of Squared
Initial Eigenvalues

Rotation Sums of Squared

Loadings Loadings
te ae % of Cumulati
or % of Cumulati % of Cumulativ : umulati
Total Variance ve % Total Variance e% Total Varian ve %
1 3.929 43.657 43.657 3.549 39.432 39.432 2.512 27.91 27.91
2 1.527 16.964 60.62 1.127 12.523 51.955 1.702 | 18.907 46.818
3 1.172 13.024 73.645 0.766 8.512 60.466 1.228 | 13.649 60.466

4 0.519 5.768 79.413
5 0.48 5.339 84.751
6 0.403 4.48 89.232
7 0.389 4.324 93.556
8 0.335 3.728 97.283
9 0.244 2.717 100

3°
--- page 4 ---
Factor Matrix* 4

Factor ¥

; - 1 2 "3
Depth of products and services to meet the range of
your investment needs 0.68 0.076 0.477
Ability to resolve problems 0.654 -0.022 0.297
Multiple providers' products to choose from 0.509 0.056 0.425
Quality of advice 0.725 -0.237 -0.162
Knowledge of representatives or advisors you deal
with 0.768 -0.182 -0.113
Representative knowing your overall situation and 0.754 0.103 -0.38
needs . ° .
Degree to which my provider knows me 0.749 -0.085 -0.237
Likelihood to Recommend Primary Provider to 0.337 0.7 -0.136

Someone | Know
Likelihood of Continuing to Use Primary Provider at

Least at the Same Level as Now 0.209 0.721 -0.105

Rotated Factor Matrix?

Factor
4 2 3

Depth of products and services to meet the

range of your investment needs 0.251 0.786 O24
Ability to resolve problems 0.358 0.62 0.061
Multiple providers' products to choose from 0.151 0.643 0.078
Quality of advice 0.727 0.279 -0.034
Knowledge of representatives or advisors you

deal with 0.718 0.346 0.018
Representative knowing your overall situation

and needs 0.829 0.123 0.145
Degree to which my provider knows me 0.741 0.238 0.132
Likelihood to Recommend Primary Provider to

Someone Know’ 0.131 0.113 0.77
Likelihood of Continuing to Use Primary 0.007 0.065 0.756

Provider at Least at the Same Level as Now

Extraction Method: Principal Axis Factoring. ‘
Answer following questions
a) Interpret the output
b) Identify and name the factors
c)’ Is there any variable/s which should not be included in the analysis?
d) What will you conclude from the Scree plot ?
e) Can you say that factor analysis is relevant in this case? Why?

Q6

co1, CO2,
BL- Apply ,
Analyse,
Evaluate

A Manager wants to understand the price people are ready pay for each of the

| features of a washing machine, before deciding the price for fully automatic

washing machine for a perticular sector of consumers. They considered four
attributes for this. The attributes and their levels is given below.

Price Type Capacity Colour
30000 Top Load 6 Kg Black
20000 Front Load 7 Kg Blue
15000 8Kg White

[10]
--- page 5 ---
The variables were coded as follows

Premium X1 m2 Type ec
30000 1 ) »X3 *
20000 0 1 Top Load 1

15000 “1 afl Front Load -1
Capacity x4 x5” Colour X6 x7
6Kg 1 0 Black 1 0
7 Kg 0 1 Blue :0 aL
8 kg -1 -1 White -1 -1

The SPSS output is given below

Note that the rankings are assumed to be best is highest
Variables Entered/Removed

Variables Variables
Model Entered Removed Method
4 x7, x5, x3, x2, x6, .|Enter
x4, x1?

a. All requested variables entered.
Model Summary”

Adjusted R Std. Error of the
Model R R Square Square Estimate Durbin-Watson

4 998? .996) 994 .27802 2.478
a. Predictors: (Constant), x7, x5, x3, x2, x6, x4, x1
b. Dependent Variable: y

ANOVA?

Model Sum of Squares df Mean Square F Sig.

1 Regression 13113.944 7 1873.421 24237.379 -000#|
Residual 3.556 46 .077
Total 13117.500 53

a. Predictors: (Constant), x7, x5, x3, x2, x6, x4, x1 %

b. Dependent Variable: y

. Coefficients*
Standardized
Unstandardized Coefficients Coefficients

Model B id. Error Beta t Sig.

4 (Constant) 27.500) .038 726.867 .000}
x1 -6.000 .054 -.314 -112.139 .000
x2 -.710} .054 -.049]   ° 12.44 .034
x3 -5.500 038; -.096 -139.647 -000
x4 18.000 054} 943 336.418) .000
xd .899| .054 -048 13.344 .044
x6 .889 054) .047 16.613 .000
x7 111 .054 .006 « 2.077 .043

a. Dependent Variable: y

Answer following
a) Find the utility for each attribute at each level and Comment on the output
b) Find the percentage utility for each attribute.
c) Draw the graph of the utility for each attribute

5
--- page 6 ---
d) Which of the attribute is most important while considering Fully automatic
washing Machine? Why? ;

e) Ifyou launched a machine with price 20000, type: front load, capacity 7
kg, & colour black, what is the utility for this machine? What is the utility
for this machine? Give business interpretations for this value.

A car insurance company, CarZuma, has collected some of the past data about

_ their clients or customers that what are their attributes as well as their insured
vehicles attributes while insuring the same. They have heard a lot about the data
analytics and are very sure that their competitors are also using some of these
techniques to beat the competition. A Classification tree model was developed on
the data to predict if the policy will have claim or not
Claim = 0 => Did not claim

| Claim = 1 => claimed

The independent variables are

con City : The Policy is from which city

€02,C03 CubicCapacity : Cubic Capacity of the vehicle insured

BL- Apply , MfrModel : Manufacturing model of the vehicle insured {10}
eae | Premium : Premium of the policy

Type : Type of the policy Renewal/New

Channel : How was the policy booked direct / Broker
Age group

Cover type

Payment frequency

Gender

' Classification tree was performed on the data to predict claim. The output is given
below :

Classification Tree
--- page 7 ---
Claimsind rae

Node 0
. Categoy %
cape 0.000 556 1344)
ets 4000 444 1073
1.000 Total 1000 2417
H
State ;
Improvement-0,008 ‘
PRADESH; KERALA: Gujarat BENGAL; MADHYA PRADESH;
TAMILNADU; Assam; PUNJAB Maharashtra
Node 4 Node2
Category % on Category % on
0000 51.5 877 Hoo 855 487
{84.000 48.5_ 827 B1000 345 245
Total 70.5704 Total 205 743
H
Gender Dv
Improvement=0.003 Improvement=0.004
Male Female <= 207180.36479 > 207150.26478
Node3 Node 4 Node 5 Node 6
Categoy % on Categoy % nn. Category % 0 Category % n
Bo000 844 643 Ho000 449 234] |@o.000 610 202| #0000 694 285
4000 45.8 540 24.000 66.4 267] |B 4.000 300 128} |B 1000 908 117
Total 48.9182 Total 248 521 | Total 137 334] | Total 15.8 362
| 4 | H
City City
Improvement=0.004 Improvement=0.040
‘VARANASI; JALANDHAR; LUDHIANA
Node 7 Nodes Node @ Node 10
Category % Category % 0 Category % on Categoy % on
0000 672 182 Boo 544 481 Bo000 226 38 0.000 $55 196
4000 32879 21900 89 454 @4000 774 130 24000 445 157 *
Total 10.0 244 Total 300 942 Total 7.0 168 Total 148 353
; u
MfrModel
Improvement=0.003
Tata Safari; Maruti Wagon-R; Maruti Tata Indica; Tata Indigo; Ford Figo;
Swift; Mahindra Scorpio; Honda Civic Honda Accord; Honda City; Hyundai
Santto; Mitsubishi Cedia
‘
Node 14 Node 12
Category % on Category % on
Boo00 508 408 B00 463 283
4.000 402 133 4000 637_328
Total 137 334 Total 253 644
Classification
Predicted
Observed 0 4 Percent Correct
0 287 0 100.0%
4 97 0 0%!
Overall Percentage 100.0% 0% 74.7%
Growing Method: CRT ,

Dependent Variable: ClaimsInd
--- page 8 ---
Tree Table i

Predic} Par rr
ted | ent d
Categ | No °
i 0 1 Total ory | de Primary Independent Variable
Nod Improve
le N {Percent} N Percent} N | Percent Variable} ment Split Values
0) 1344) 55.6%] 1073] 44.4%] 2417} 100.0% 0
1 877} 51.5% 827) 48.5%} 1704) 70.5% 0} O}State .008|NCR;
IMADHYAPRADESH;
UTTAR PRADESH;
KERALA; Gujarat;
TAMILNADU; Assam;
PUNJAB
42 467] 65.5% 246] 34.5%] 713) 29.5% 0} = 0/State _ 008 |Karnataka; HARYANA;
WEST BENGAL;
MADHYA PRADESH;
Maharashtra
3 643} 54.4% 540} 45.6%] 1183) 48.9% 0} 1|Gender -003|Male
4 234] 44.9% 287) 55.1%] 521} 21.6% 1} 1/Gender .003|Female
Ss 202] 61.0% 129] 39.0%} 331] 13.7% Oo} = 2{IDV .001}<= 297150.35479
6 265} 69.4% 117} 30.6%] 382} 15.8% Oo} = 2}IDV .001}+ 297150.35479
7 162| 67.2% 79} 32.8%] 241 10.0% 0} = 3/City -004|CALICUT; CHENNAI;
Guwahati
8 481) 51.1% 461} 48.9%] 942} 39.0% 0} = =3}City .004|NEWDELHI; NOIDA;
INDORE; MATHURA;
AHMEDABAD;
VARANASI;
(JALANDHAR;
LUDHIANA
aK) 38] 22.6% 130] 77.4%] 168 7.0% 1] 41/City -010}INDORE; MATHURA;
CALICUT; CHENNAI;
Guwahati
10 196} 55.5% 157) 44.5%] 353) 14.6% oO} = 4/City -010|NEWDELHI; NOIDA;
AHMEDABAD;
VARANASI;
JALANDHAR;
LUDHIANA
11 198] 59.8% 133] 40.2%] 331 13.7% 0} = 8|Mfr- .003|Tata Safari; Maruti
Model IWagon-R; Maruti Swift;
Mahindra Scerpio;
Honda Civic
12 283} 46.3% 328] 53.7%] 611] 25.3% 1] 8)Mfr- .003}Tata Indica; Tata Indigo;
$ Model Ford Figo; Honda
Accord; Honda City;
Hyundai Santro;
Mitsubishi Cedia
" Growing Method: CRT
Dependent Variable: ClaimsInd
Independent Variable Importance
Independent Normalized
Variable Importance Importance
| |City .007 100.0%
State .006 93.1%
Gender .003) 46.8%
Mfr-Model .001 14.6%
(Cubic Capacity .001 8.7%
IDV -000 4.0%
Age .000 2.6%
Premium -000 1.6%

Growing Method: CRT
Dependent Variable: ClaimsInd
````

## 2022-23 · Final-Exam · Sem 6 · paper b913de391de3

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-VI/DATA MINING AND ANALYTICS/Data Mining & Analytics, Sem-VI, Year 2022-23, Final Exam.pdf`
- Printed on paper: duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 90.9

````text
‘ SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Program/s: BTech
Stream/s ; CSBS

Year: III Semester: VI

Subject: Data Mining and Analytics
Date:_02 /05 / 2023
Marks: 1C0

Time: 03 hrs. (2:00pm to.S!00 pm)

No. of Pages: 4

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.
-~, 2) Out of remaining questions, attempt any 4 questions.
j 3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

a Answer briefly:
Oo A Discuss the applications of data mining. (5 M]
Co- 1 B Explain Symmetric Vs Skewed data with the help of an example
BL-2 ai
CO-3 Cc In a cafe, the customer arrives at a mean rate of 2 per min. Find the
BL-3 probability of arrival of 5 customers in 1 minute using the Poisson | [5 M]
distribution formula.
CO- 3 D : : : ‘ ws ge i : ‘
~|BL2 Explain what is auto correlation Why it required in time series analysis? [5 M]
A
Construct the FP-tree for the below transactions for a minimum support
threshold =3.
TID Items Bought
Q2
CO-1 ; {10 Mj
BL-3,5 100 f.a,c,d,g,i,m,p
200 a,b,¢,f,l,m,o
300 b,f,hj,o
--- page 2 ---
400 b,c,k,s,p

500 af,ce.p,m,n
Co-3 B What is generalized linear model explain with example.
BL-2 mal
Cco-3 Cc Explain What is moving average Identify why it required in time series
BL-2 analysis pel
y
A Discuss Proximity measure for Nominal, Ordinal, Binary and Mixed type
of attribute. Solve the dissimilarity between objects of mixed attribute type
give in the table below.
Q3
CO-1 BL- Testl Test2 Test 3 [10 M]
3 (Nominal) (Ordinal) (Numerical) ;
Code—A Excellent 45
Code —-B Fair 22
Code —C Good 64
Code —D Excellent 28
Co-1 Explain Briefly the steps in data mining process. Differentiate between [10 M]
BL-1l database and data warehouse.
A What is the goal of Regression? List different type of application where
regression can be used.
The following table shows the data of 10 students record where number of
hours studied (independent variable) and their corresponding exam scores
(dependent variable).
Hours Studied (X) Exam Score (Y)
2 60
Q4 3 70
Co-3 4 80 [10 M]
BL-1,3 5 85
6 90
7 95
8 100
9 110
10 120
11 125
--- page 3 ---
We want to find the linear regression equation that best describes the
relationship between the number of hours studied and the exam scores, and
use it to predict the exam score for a student who studies 7.5 hours.

Bh B Explain about autoregressive moving average model with example. [10 M]
A A simple example from the stock market involving only discrete ranges
has profit as categorical attribute, with values {up, down} and the training
data is: Apply decision tree algorithm on following dataset and construct
decision Tree.
Note: Use entropy as selection of attribute
Age Competition Type Profit
Old Yes Software Down
Old No Software Down
Q5 Old No Hardware Down
CO-1 Mild Yes Software Down [10 M]
BL-3 Mild Yes Hardware Down
Mild No Hardware Up
Mild No Software Up
New Yes Software Up
New No Hardware Up
New No Software Up
COo-3 B How a regression model can be used in classification problem? Explain [10 M]
BL-2 with example.
A What are outliers? How can we remove outliers using boxplot?
Construct boxplot for the given data of height of 40 students in DMA class
Q6 59;60;61;62;62;63;63;64;64;64;65;65;65;65;65;65;65;65;65;66;66;67;67;
CO-1 68;68;69;70;70;70;70;70;7 1;71;72;72;73;74;74;75;77 [10 M]
BL-3,6 Solve and Find Minimum, Maximum, Q1, Q3 and IQR value for given
data points
CO-1 B Explain the steps of Apriori algorithm. Demonstrate the process of rule
BL-2,3 generation with example [10 M]
Q7 A . . A —_ 23 :
CO-1 Discuss different measures of attribute selection in decision tree? Give the [5M]
BL-2 equations for the same
B An online retailer wants to investigate the relationship between its monthly
CO-3 advertising expenditure (in dollars) and its monthly sales revenue (in [5M]
BL-3 thousands of dollars). The retailer has collected data on the advertising

expenditure and sales revenue for the past 12 months. The retailer wants to

—————-

3
--- page 4 ---
know whether its advertising expenditure has a significant impact on its
sales revenue, and if so, how much it can expect to increase its revenue for
each additional dollar spent on advertising.

The above problem statement can be solved using which type of data
mining model. Justify your answer.

Sho Cc What is link function why it used in linear regression? [SM]
Sho. |_| What is differencing explain with exampie. [5M]
4
````

## 2022-23 · Final-Exam · Sem 9 · paper 22473b6845d5

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data Mining & Analytics,Final,2022-23.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 20 December 2022
- Text: ocr (7 pages), mean OCR confidence 78.2
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
/

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGI
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEE

Academic Year: 2022-23
Programme: MBA Tech (All Stream) - Year: V Semester:

Subject: Data Mining and Analytics “ : /
Marks: 50 é
Date: 20 December 2022, Time: 10.30 am - 12. 30 pm
Durations: 2 (Hrs)
No. of Pages: _7

Final Examination

Instructions: : Candidates should read carefully the instructions | printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qu

C01, C02 ;

BL- Explain following in brief with examples
Understand,

Analyse

a. Regression Splines [3]

b. Bagging, Random Forests & Boosting (5]

Q2 a
coi, C02,

CO3;

BL- :
Understand,
Analyse

State the advantages of Generalized Additive Models , [5]

Q2 b:

— Coz, Which statistics are used to select best models in stepwise regression/ best subset

BL. regression? Describe any three. What different approach you can consider without using [5]
Understand, these statistics?

Analyse

Q3 What are support vectors? Describe Maximal Margin Classifier? Explain the role of support

ae co2, vectors in a support vector machine. : a

Understand,
Analyse

What are Non-parametric tests? When do you use the non-parametric tests? What are the
a4 , non-parametric tests equivalents for following parametric tests/ Situations? Also State the

a coz possible null and alternate hypothesis for each test 110]
Understand, a) Two Sample.mean —independent samples
Analyse b) Randomness of the sample
c) One Way ANOVA
Q.5
C01, Co2 What are the challenges one can face while using high dimensional data? Describe various
BL- methods to overcome these challenges. Mention advantages & disadvantages for these . [10]
Understand, methods.
Analyse
Q6 ;
anaes A company entering in the life insurance sector wants to decide the price for their
anise, ve life insurance policies. They considered four attributes for this. The attributes and [10]
Evaluate : their levels is given below. :

es) ;
--- page 2 ---
Premium Regular Amount ~ | Assured

return in Insured - | Bonus
Years
10000 4 3 LK. 5%
20000 5 4LK 6%
30000 5 Lk 7%
The variables were coded as follows
Premium X1 x2 Regular return in
10000 1 0 Years
20000 0 1 X3
30000 -1 -1 4 yrs 1
5 yrs -1
Amount insured x4 x5 Assured Bonus x6 x7
ak 4: 0 5% A. 0
21k 0 1 6% te) 1
3 Lk -1 -1 7% -1 -1
The output is given.
Note that the rankings are assumed to be best is highest
Variables Entered/Removed
: Variables Variables
Model Entered Removed Method
41 x7, x5, x3, x2, x6, .|Enter
x4, x18
a. All requested variables entered.
Model Summary”
: Adjusted R Std. Error of the
Model R R Square Square Estimate Durbin-Watson
4 .998? .996 .994 .27802 2.478}
a. Predictors: (Constant), x7, x5, x3, x2, x6, x4, x1.
b. Dependent Variable: y
ANOVA®
Model Sum of Squares df Mean Square F Sig.
1 Regression 13113.944! 7 1873.421 24237.379 .0004
Residual . _ 3.556 46 .077
Total 13117.500) 53}

a. Predictors: (Constant), x7, x5,-x3, x2, x6, x4, x1
b. Dependent Variable: y
--- page 3 ---
van

Coefficients*

Standardized
Unstandardized Coefficients} _ Coefficients

Model B . Std. Error Beta t Sig.

1 (Constant) . 27.500 .038} 726.867 .000}
x1 6.000} .054 -.314)   -112.139 .000}
x2 0.710 .054 -.049} - 12.44 .034|
x3 1.500) .038 -.096 -39.647 .000
x4 -18.000 .054 .943 336.418 .000}
x5 -.899 054 .048 13.344 044
x6 -.889) .054 .047 16.613 .000}
x7 -.111 .054 .006) 2.077 .043

a. Dependent Variable: y

Answer following
a) Find the utility for each attribute at each level and Comment on the output
-b) Find the percentage utility for each attribute.

c) Draw the graph of the utility for each attribute

d) Which of the attribute is most important while considering the Life insurance
policy? Why?

e) Ifyou launched a new insurance product with premium 20000, regular returns in 4
years, amount insured 2 lakhs, and assured bonus 5 What is the utility for this
product? Give business interpretations for this value.

Q7

c01, CO2,
BL- Apply ,
Analyse,
Evaluate

a.

A study was conducted to uncover the. factors that lead to employee aittrition and
explore important questions. Following are the variables used in the study

Attrition - Yes (employee left the

organization), No (employee did not leave MonthlyIncome - Monthly income of the

the organization) employee

BusinessTravel - Non-Travel, :

Travel_Frequently, Travel_Rarely

NumCompaniesWorked

DailyRate OverTime Yes, No
Department - Human Resources, Research &
Development, Sales . PercentSalaryHike
DistanceFromHome PerformanceRating
Education RelationshipSatisfaction
StockOptionLevel — 0 — No-stock, 1 —- Moderate, 2
EducationField —High
EnvironmentSatisfaction Low, Medium, High, | TotalWorkingYears — Total experience of the
Very High employee
TrainingTimesLastYear — no of trainings attended
Gender last year
HourlyRate WorkLifeBalance - Bad, Good, Better, Best
Jobinvolvement - Low, Medium, High, Very
High YearsAtCompany — No of years at the company
JobLevel - Low, Medium, High, Very High YearsInCurrentRole — Years at current role
YearsSinceLastPromotion — Years Since Last
JobRole ° Promotion
JobSatisfaction - Low, Medium, High, Very YearsWithCurrManager — Years With Current
High Manager

| MaritalStatus — Marital Status Age - Age of the employee in years

{10]

8/7
--- page 4 ---
Classification tree was performed on the data to predict Attrition. The output is
given below: ‘

Classification Tree

Attrition
Node
Category % _n
roo71 No 83.9 1233
18No | Byes 16.1 237
aia Total 100.0 1470
OverTime
Improvement=0.018
* a No
Node Node2
Category % in Category % in
TNo 69.5 289 Eno 99 044
Byes 305 127 Byes 10.4110
Total 28.3416 Total 74.7 1054
Monthlylneome TotalWokingYeats |
Improvement=0.017 Improvement=0.007 \
<= 2475.0 > 2475.0 =25 >
Node 3 Node 4 Node S Node @
Categoy % on Category % on Category % in Category % a
TNo 204 24 BNo 772 268| |@No 670 69 No 018 685
Total 4769 Total 22.8 347] | Total 6.0 88 Total 65.7 088
a I El
JobRole ‘ NumCompaniesWonked
Improvement=0.007 Improvement=0.002
Sales Executive: Laboratory Research Scientist, Manufacturing ° === 6.0; 6.0; 7.0. 8.0; 1.0; 9.0; 0.0; 40: 2.0:3.0

Technician; Sales Representative Director; Healthcare Representative;
Manager, Research Director; Human

Resources
Node7 Node8 Node? Node 10
Category % fn Category % A . Category % i Category % n
No 633 93 No 87.5 175 @No 82.7 129 No +933 756
Yes 367 54 Yes 42.5 25 Byes 47327 Yes 67 54
Total 10.0 147 Total 13,6 200 Total 10.6 158 Total 55.1 810

StockOptionLevel

° 1.0 y
Node 44 Node 12

Category % on Category % on
No 403 25] |BNo ~~ 80.0 68]. ‘
WYes 50.7 37] |B Yes 200 17
= Total 42 62 Total 68. 85

=
°

Lip
--- page 5 ---
1.

Tree Table

Pre
dict
ed |Par
Cat] ent
eg | No
No Yes Total ory | de Primary Independent Variable
Impro
No veme
ide } N |Percent} N |Percent] N_ |Percent Variable | nt Split Values
O | 1233) 83.9% 237| 16.1%] 1470) 100.0%|No :
1 289| 69.5%] 127] 30.5%] 416] 28.3%|No| OjOverTime| .016]Yes
2 944) 89.6% 110) 10.4%] 1054) 71.7%|No O}OverTime | .016}No
3 21| 30.4% 48) 69.6% 69] 4.7%lYe 4|MonthlyIn | .017}<= 2475.0
s | |come
4 268] 77.2% 79| 22.8% 347] 23.6%|No 4|MonthlyIn | .017]> 2475.0
. come
5 59| 67.0% 29| 33.0% 88} 6.0%|No 2\TotalWork| .007)<= 2.5
ingYears
6 885] 91.6% 81] 8.4% 966] 65.7%|No 2|TotalWork| .007|> 2.5
ingYears
7 93] 63.3% 54] 36.7%] 147] 10.0%|No}| 4|JobRole .007|Sales Executive;
Laboratory
Technician; Sales
Representative
8 175| 87.5% 25) 12.5%} 200} 13.6%|No} 4{JobRole .007|Research Scientist;
Manufacturing
Director;
Healthcare
Representative;
Manager;
Research Director;
Human Resources
19 129] 82.7% 27| 17.3% 156] 10.6%|No 6|NumCom | .002]6.0; 5.0; 7.0
paniesWo
: tked
10 | 756] 93.3% 54 6.7%! 810] 55.1%|No 6|NumCom | .002)8.0; 1.0; 9.0; .0;
, paniesWo 4.0; 2.0; 3.0
rked
1 25] 40.3% 37| 59.7% 62] 4.2%|Ye 7\StockOpti | .008 0)
s onLevel
12 68} 80.0% 17| 20.0% 85] 5.8%|No 7|StockOpti | .008]1.0; 3.0; 2.0
onLevel
Growing Method: CRT
Dependent Variable: Attrition
Risk
Method Estimate Std. Error
Resubstitution 135 009}
Cross-Validation .153} .009}

Growing Method: CRT

Dependent Variable: Attrition

5/7
--- page 6 ---
Classification Table of Test Set

Predicted

Observed No Yes Percent Correct
No 1187) 46) 96.3%
Yes . 152) 85 35.9%
Overall Percentage 91.1% 8.9% 86.5%
Growing. Method: CRT

Dependent Variable: Attrition

Independent Variable Importance
Normalized

Independent Variable. Importance Importance
MonthlyIncome 024, 100.0%
TotalWorkingYears .019 79.4%)
OverTime .016| 69.5%
JobRole .012 51.3%
Age 010) 42.4%
'StockOptionLevel .008 32.6%
MaritalStatus 008; 32.5%
EnvironmentSatisfaction 005 20.1%
DistanceFromHome .003 14.1%
DailyRate .003 11.7%
Department .003 10.9%
'YearsAtCompany 003} 10.6%|
WorkLifeBalance .002 10.2%
NumCompaniesWorked — 002) 8.6%
EducationField 002 8.0%
TrainingTimesLastYear .001 5.1%
JobLevel .001 4.6%
PercentSalaryHike 001 3.2%
JobSatisfaction .000 TK
HourlyRate 000) 6%
Education : 4.056E-5 2%
RelationshipSatisfaction 2.833E-5 1%
PerformanceRating 7.830E-7 0%

Growing Method: CRT
Dependent Variable: Attrition

Normalized Importance

20 4p =p 8 ke
Monthlyincomet 7 iy
Overtime 5
Ul ———————

» AT |
3 MartelStetus eg —)

5 DistanceFromHomefo I
= Department {——1.
SB Work.iteBalancef—— I

B —EducationFiel {=
2 Jobteve f=
JobSatistaction4

. Eaucationr}

Pertormancerating4
0.000% 0.005% 0.010% 0.015% 0.020% 0.025%

Importance

Growing Method:CRT

Dependent Variable:Attrition

6);
--- page 7 ---
ary

Stepwise Logistic regression classification Table of Test Set
Classification Table*

Predicted
Attrition
Observed No Yes Percentage Correct
Attrition No 1199 34 97.2
. Yes 127 110 46.4
Overall Percentage 89.0

Answer following questions
a) Explain the tree output. How many splits the tree has?

b) Explain each split in terms of variables

c) What is the classification accuracy? Is it adequate?

d) According to this output, which variable contributes maximum to the classification?

e) Astepwise logistic regression classification accuracy is given in the output. Can you
say that the cart model is preferred over logistic regression? Why?

f) Ifan employee selected from the company opts for overtime, has monthly income
>2475, works as a sales representative, has stock option level = 0, what would be
your prediction for this employee?

g) Ifan employee selected from the company opts for overtime, has monthly income
>2475, works as a sales representative, has stock option level more than zero, what
would be your prediction for this employee?

7m


+7
````

## 2022-23 · Re-Exam · Sem 6 · paper 1774e0f9b56d

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-VI/DATA MINING AND ANALYTICS/Data Mining and Analytics Sem-VI, Batch 2022-23 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 81.6

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024 ~25|

Program BTech : Year: II Semester: 6
Stream: CSBS

ject: ini i ime: 2s 5700
Subject: Data Mining and Analytics ; Time: 3 hrs (2: oopento, ey)
Date:_10_/ 5/2025 No. of Pages: 3
Marks: 100

— aici leas

__“7Re-Examination (20222023)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1 is compilsory.

2) Out of remaining questions, attempt any 4___ questions.

3) In all 5_questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
/ Answer briefly:
. . | a. | What is outlier analysis and brief how this can be used in fraud detection with

CO1; SO1; [5]

BLI1 example.

CO3 ; SO3; |b. . | Whatis simple linear regression? How is it useful in trend analysis? [5]
BL2 : :

H SO3; | c. | whatis tree pruning? Brief its types. 1 [5]
oe SO3; | d. Explain ARIMA models. How are they used in time series forecasting? (5]
Q2 a ws . ar . ; :

: How is decision analysis applied in prescriptive analytics? Explain -

CO-1; SO- .. . [10]
1; decision trees with an example.

BL-2
ae SO- |b | Define autocovariance and autocorrelation. Explain their significance in [10]
BL-2 time series analysis.

| Q3 a” | What is logistic regression? Explain the logit transform and interpretation

CO-3; SO- [10]

of parameters.
3; BL-2
--- page 2 ---
b List the limitations of using information gain for attribute selection. Find the
Gain ratio for attribute income for the following data set.

age _| income |student credit_rating buys_computer

<=30 [high no__ {fair no
<=30 [high no__|excellent no
31...40 [high | no [fair yes
>40 [medium | no __ {fair yes
CO-1; SO- >40 [low yes _ [fair yes ;
3; >40 __|low yes_lexcellent no [10]
BL-4 31...40 flow, yes_|excellent yes
<=30 |medium| no _|fair no
<=30 flow yes _|fair yes
>40 medium | _yes_|fair yes
<=30 |medium| yes _|excellent “yes
31...40 [medium |__no excellent. yes
31...40 [high yes _|fair yes
>40 medium | _no__|excellént no
a | John is an investor. His portfolio primarily tracks the performance of the S&P 500
and John wants to add the stock of Apple Inc. Before adding Apple to his portfolio,
he wants to assess the correlation between the stock and the S&P 500 to ensure that
adding the stock won’t increase the systematic risk of his portfolio. Find the
J Q4 coefficient from the data gathered below and give your interpretation.
CO-3; SO- ; ene [10]
3;
BL-4

SO- |b | Describe the Aptiori algorithm for mining association rules. Illustrate how are [10]

BL-1 frequent itemsets generated efficiently with example.
Q5 a
CO-3: SO- Explain the various statistical functions used to measure the dispersion of a data [101
3s , in data mining.
BL-1

To ar cE ae jate the Mi i :
CO-3; SO- b | What is Minkowski distance? List the applications and Calculate the Minkows' [10]

3 distance with p=2.
--- page 3 ---
BL-4 Point | Attributel | Attribute

2.

( X1 2 3
X2 1 2

X3 4 5

x4 3 2,

a__| You have the following data for spam classification:

Word ||Spam||Not Spam

"Buy" |i4 1

Q6 S Gcee
oe pe. ee eee 110]
BL-4 "Free" 14 0

Spam emails = 5, Not Spam = 5
Estimate the probability that an email containing “Buy” and “Free” is

spam using Naive Bayes (with Laplace smoothing).

CO-3;SO- |b | Differentiate between parametric, non-parametric, and semi-parametric
3: ;

? : [10]
BL-3 - | regression models.

Q7 a ;
CO1: §0-1: |: What is data mining and list its applications. Explain the steps in KDD process. [10]

BL-1

CO2;SO2; |b
BL-1 Write a short note on any 2 tools used for data mining. [10]
--- page 4 ---

````

## 2021-22 · Final-Exam · Sem 6 · paper 44407986284b

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-VI/DATA MINING AND ANALYTICS/B Tech, CSBS, Data Mining & Analytics, 3rd Year, Sem-VI, Final Exam, Year 2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 April 2022
- Text: ocr (3 pages), mean OCR confidence 90.7

````text
, SVKM’s NMIMS : :
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

aintiniias OF TECHNOLOGY MANAGEMENT & ENGINEERING were

Academic Year: 2021-22 Stee
Programme: B. Tech (Computer Science & Business Systems) Year: III Semester: VI

Subject: Data Mining and Analytics *
Marks: 100
Date: 16 April 2022. Time: 10.00 am to 1.00 pm
Durations: 3 (hrs)
No. of Pages: 0%
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: [20]
A. a) State any 4 differences between Data Mining and Statistics. 2
b) Discuss pros and cons of Linear Regression 2
B. Justify with the help of an example Data cleaning and Data Reduction is the part 4

of Data preprocessing.

CG. In a store, all vegetables are placed in the same aisle, all dairy items are 4
placed together and cosmetics form another set of such groups. Investing
time and resources on deliberate product placements like this not only
reduces a customer’s shopping time, but also reminds the customer-of what
relevant items (s)he might be interested in buying, thus helping stores cross-
sell in the process. Write a brief note on the technique that helps to uncover
all such relationships between items from huge databases. Also mention the
various metrics that helps us to understand the strength of association
between items.

Dz Write the difference between linear and non-linear regression analysis. 4

E Justify in linear time series analysis model how auto-correlation function 4
and partial auto-correlation function plays an important role.

V/s
--- page 2 ---
Q2

Q3 -

Q4

A

B

A

What are the different Data Mining Techniques?

Explain the concept of steepest descent method for non-line.
help of an example.

[10]

‘ar regression with the [10]

Apply KNN algorithm with K=3, to classify the special into paper into ‘Good’ [10]
or ‘Bad’ with attribute- Acid durability=3 and Strength=7 falls.

Classificat Acid Strength
ion Durability
Bad 7 7
Bad 7 4
Good 3 4
Good 1 4

Solve the following and find the best fit linear regression equation.
The following table represents the cars sold in the last year by a car

dealership company.

Car Age (in years) Price (in dollars)

4 6300
4 5800
5 5700
5 4500
7 4500
7 4200
ey 4100
9 3100
10 2100
11 2500
12 2200

Find the optimal value of the objective function f(x) = 2x
Newton Raphson Method.

3 2x -5 by [10]

a) Ifit takes one hour to train a Decision Tree on a training set
containing | million instances, roughly how much time will it take
to train another Decision Tree on a training set containing 10
million instances? [The time complexity of a Decision Tree is

given by O(n x m log(m))]

b) Why do we require Pruning in Decision Trees? Expiain.

/s
--- page 3 ---
Q5

Q6

A.

A

Explain the following term in Time series analysis with suitable example: - [10]
a. Trend

b. Seasonality
c. Irregularity

d. Cyclical
e. ARand MA
[10]

Day Outlook Temperature Humidity Wind PlayTennis
DI Sunny Hot . High Weak No
D2 Sunny Hot High Strong No
D3 Overcast Hot High Weak Yes
D4 Rain Mild High Weak Yes
D5 Rain Coot Normal Weak Yes
D6 Rain Cooi Normal Strong No
D7 Overcast Cool Normal Strong Yes
D8 Sunny Mild High Weak No
D9 Sunny Cool Normal Weak Yes
DIO Rain Mild Normal Weak Yes
Dit Sunny Mild Normal Strong Yes
DI2 Overcast Mild _——=High Strong Yes

DIB Overcast Hot == Normal = Weak Yes

Calculate whether a kid will be able to play Tennis if Outlook=Sunny,
Temperature=Cool, Humidity=High and Wind Strong.

Justify with the help of an example, task relevant data and background knowledge [10]
is the data mining knowledge representation.

Write short note on the following [10]
1. Generalized linear model
2. Non-Linear Regression analysis
````

## 2019-20 · Final-Exam · Sem 9 · paper 3ac4693cee5e

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data Mining and Analytics , Final 2019-20.pdf`
- Printed on paper: max marks: 70; duration hours: 2; exam date: 11 December 2019
- Text: ocr (4 pages), mean OCR confidence 92.6

````text
a SVKM’'S NMIMS
‘MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2019-2020

Program: MBA Tech ( All Streams) Year: V Semester: IX

Subject: Data Mining and Analytics Time: 10.30 am to 12.30 pm ,-
Date: 11 December 2019 a Duration: 2 (Hrs)

Marks: 70 No. of Pages:4__

Final Examination (2019-20)

MPSTME ~

LIBRAR

1. Question no.1 is compulsory
2. Attempt Any Four from the rest
3. Figures to the right indicate full marks.

compulsory

1 a. 14

Smoothing Splines(4)

Lasso(5)

Boosting(5)
--- page 2 ---
optional r

2
a.
Explain Data visualization in short.(7)
b.
In a study done from various streams of a college 60 students, with equal number
of students drawn from each stream, are we interviewed and their intention to join
the Drama Club of college was noted.
B.Sc. B.A. B.Com M.A. M.Com
No. in each class 5 9 11 16 19
It was expected that 12 students from each class would join the Drama Club. Using the
K-S test to find if there is any difference among student classes with regard to their
intention of joining the Drama Club.(7)
3
a.
Explain any two subset/feature selection techniques in detail.(7)
b.

14

14
--- page 3 ---
4

Explain Stepwise Selection.(7)

Explain shrinkage methods. How it will help in dimensionality reduction?(7)

Explain Ridge method.(7)

Explain Regression Splines.(7)

What do you mean by Local Regression? Explain in detail.(7)

Explain decision tree with advantages and disadvantages.(7)

3/4

14

14
--- page 4 ---
Explain random forest , its advantages and disadvantages.(7)

Explain kernels in SVM.(7)

What is relationship between logistic regression and support vector machines.(7)

4 |

14
````

## 2018-19 · Final-Exam · Sem 9 · paper 72a98766ef23

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data Mining and Analytics Final 2018-19.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 10 December 2018
- Text: ocr (2 pages), mean OCR confidence 92.9

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: MBA Tech ( All Streams) Year: V - Semester: IX

Academic Year: 2018-2019

Subject: Data Mining and Analytics

Marks: 60 -
Time: 2.30pm to 4.30 pm ~
Durations: 2 Hrs

No. of Pages : 62
Final-Examination (2018-19)

Date: 10 December 2018

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of
the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started ona fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q 1A) What is business analytics? What is data mining? How these two are different from each other? (2+2+2)
Q 1B) A data can be categorized based on various terminology & characteristic. Explain this remarks by taking the

consideration of type of data with examples. ’ (4+2)
Q 2A) What is regression, specify the assumptions of the linear regression. (2+4)
Q 2B) Define Variance, bias and explain their relationship with the model complexity. (2+2+2)
Q 3A) Explain the followings error statistics: (2+2+2)

a) Adj R-Sqaure b) AIC c) Mallow’s Cp

Q 3B) What is polynomial regression equations? Can these equations be fit by linear regression? If yes justify your
answer with the help of an example. (24+2+2)

QA) If E(f(x))=5, Var(f(x))=9 and a,b,c are constant, Calculate the values of followings:- (24+34+3+4)
a) E(5f(x)+a)
b) E(5Sc?+f(x))
c) Var(5f(x)+9+b)
d) Var(f(x)+3c2+8)

i Pe
--- page 2 ---
Q 5A) What is multicollinearity? What are it’s impact on the linear regression analysis? Explain the methods by

which we can minimize it. (1+3+3)
Q 5B) What is the basic difference between parametric and non-parametric methods and mention name of two
statistics from both the categories. (1+4)

Q 6A) Explain K-fold cross validation methods in details draw the figures if necessary, also mention the uses of cross

validation. (4+2)
Q 6B) Explain the key difference between forward, backward and hybrid variable selection and thus explain which
one is best among these three. (6)
Q7)
Fourteen adult males between the age of 35 and 50 participated Customer lod CholestereliLevel
in a study to evaluate the effect of diet and exercise on blood _ ee After
cholesterol levels. Total cholesterol was measured in each subject ; o —
initially, and then three months after participating in an aerobic 3 258 227
exercise program and switching to a low-fat diet. The data are a 295 240
given in the accompanying table. Assuming the two distributions 5 251 238
to be continuous, use the Wilcoxon signed-rank test to ascertain 6 245 241
that low-fat diet and aerobic exercise results in reducing blood 7 287 234
cholesterol levels. Use a = 0.05. (Refer Table 1, Assume a = 0.01 3 314 256
with normal approximation to binomial, Woos = 25) (12) 9 260 247
10 279 239
11 283 246
12 240 218
13 238 219
14 225 226

Table 1 : Question 7

Q 8A) Explain the differences between linear models and trees, also provide the examples for your explanations. (6)

Q 8B) Explain the use of step & basic function in case of non-linear model. How these can be used to fit a linear
regression. : (3+3)

22
````

## 2017-18 · Exam not stated · Sem 9 · paper 7ddb58b50303

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data mining & Analytics 2016-17 (All stream).pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 28 May 2018
- Text: ocr (1 page), mean OCR confidence 94.1

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: MBA Tech (ALL STREAM ) Year: V Semester : IX
Academic Year: 2017-2018

Subject: Data Mining And Analytics
. Marks:60
Date: 28 May 2018 Time: 02.00 pm to 04.00 pm
Durations: 2 (hrs)
No. of Pages :
Re-examination (2016-17)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. lis compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume ‘suitable data if necessary.

QI. (a) (i) Applications of data mining with appropriate examples. ; (6 Marks)

(ii) Explain the intuition behind R-square and adjusted R-square.

QI. (b) Difference between bagging and boosting. (6 Marks)
Q2. (a) Explain k-means clustering with any one application. (6 Marks)
Q2. (b) What are different resampling techniques? Explain any two in short. (6 Marks)
Q3. (a) Explain the parameters for choosing the optimal model on basis of adjusting the training error. (6 Marks)
Q3. (b) Explain types of linkages in hierarchical clustering. (6 Marks)
Q4. (a) Explain bootstrap and its application in short. (6 Marks)
Q4. (b) What are iannarumdteis methods? Explain any one in detail. (6 Marks)
QS. (a) What is over fitting? Explain techniques to avoid over fitting in decision trees. (6 Marks)
Q5. (b) Explain supervised and unsupervised learning in detail. (6 Marks)
Q6. Explain different subset/feature selection techniques in detail. (12 Marks)

Yt
````

## 2017-18 · Final-Exam · Sem 9 · paper 05d492c7872b

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data Mining and Analytics 2017-18 Final.pdf`
- Printed on paper: max marks: 60; exam date: 11 December 2017
- Text: text (2 pages)

````text
SVKM~sNMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING
Year.V   Semester: IX
Programme: MB~ Tech ( Al~Streams)
Academic Year: 2017-2018
Subject: Data Mining and Analytics
-:   Marks: 60
Time: 16.30 am to 12.30 pm
Date: 11 December 2017
Duratioris: 2 Hr
No.ofPages:~   --
,<!:(.;,-:
Final-Examinati~n   .
Instructions:   Candidates should read carefully the instructions   printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
I) Question No. Iis compulsory.
2) Out of remaining   questions,   attempt any 4 questions.
3) In ailS questions to be attempted.
LjJ All questions   carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.
QI. (a) Explain shrinkage methods. How it will help in dirnensionality   reduction?   (6 Marks)
Q I. (b) Explain decision trees and its advantages   and disadvantages.   (6 Marks)
Q2. (a) Explain random   forest and its advantages   and disadvantages.   (6 Marks)
Q2. (b) Explain hierarchical   clustering with algorithm   in brief.   (6 Marks)
Q3. (a) Explain k-fold cross validation   approach and validation   set approach.   Justify the better approach.   (6 Marks)
Q3. (b) What are nonparametric   methods?   Explain anyone   in short.   (6 Marks) -
Q4. (a) In case of low population,   which resampling   technique   can be used? Provide supporting   rationale   for the
same.   (6 Marks)
Q4. (b) Short note: Principal component   analysis.   (6 Marks)
--- page 2 ---
..
QS. Explain the parameters used for splitting the nodes in decision trees.   (12 Marks)
Q6. Explain different subset/feature   selection techniques in detail.   (12 Marks)
&6.:.8 The dataset includes 20 variables, based on statistics given below find out the optimum number of variables to be
considered in model and justify.
ep
I)
•   (1   10   1.0
BIC
0
0   5   10   15   20
-20
-40
-60
u   -80
co
-100
-120
-140
-160
Number of Variables
Adjusted R-square
0.6
~
ro 0.5   ~$".e~,,,(l>"~""""~~-("~
~
~ 0.4
er. 0.3   \'$
-0
.8 0.2
VJ
.~ 0.1
-0« 0
o   5   .10   15   20
Number of Variables
````

## 2017-18 · Re-Exam · Sem 9 · paper f149e2bb8c57

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data Mining and Analytics 2016-17 Re-exam.pdf`
- Printed on paper: max marks: 60; exam date: 11 December 2017
- Text: text (4 pages)

````text
SVKM's NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGYMANAG~   & ENGINEERING
Programme: MBA Tech (All Streams)   Year: V   Semester: IX
"',r·   I
Batch: 20J6-17
Academic Year: 2017-2018   ..~""""".-- ..
}   Subject: Data Milling and Analytics   ./~"   1
I   Marks: 60,~ •.•\~'.   fI.
J   Date: 11 December 2017   Time: 10~30jam- 12.30 pm
Durations: 2 'Hrs   .
No. of Pages: -04-
Re-Examination
Answer Question no. 1 and any 4 questions from the rest
All Questions carry equal marks.
Qu 1. Answer any 12 (twelve)
For each of the following, write the relevant data mining task(s):
a. A defense computer must decide immediately whether a blip on the radar is a
flock of geese or an incoming nuclear missile.
b. A political strategist is seeking the best groups to canvass for donations in a
particular county'.
c. A Security official would like to determine whether a certain sequence of .
financial and residence moves implies a tendency to terrorist acts.
d. A NSE analyst has been asked to fmd out the expected change in stock price for a
set of companies with similar price/earnings ratios.
Determine whether the following statements are true or false. If false, explain in short
why the statement is false.
e. The value of the ith principal component equals the ith eigenvalue divided by the
number of variables.
f The second principal component represents any linear combination of the
variables that accounts for the most variability in the data, once the first principal
component has been extracted.
g. For a component weight to be considered of practical significance,   it should'
exceed 0.50 in magnitude.
h. The least-squares line is that line that minimizes the sum of the residuals.
1.   If all the residuals equalzero, then SST=SSR:   : .
J. The best way of determining whether an observation is influential is to see
whether it's Cook'sdistance   exceeds 1.0.
k. In a normality plot, if the distribution is normal, then the bulk of the points should
fall on a straight line.
1/4-
--- page 2 ---
L The chi-square distribution is left-skewed.
m. Small p-values for the Anderson-Darling   test statistic indicate that the data are -
right -skewed.
Fill up the Blanks (Explanation   of the each of the regression terms given at right).
n.   ... ... .....   Represents an overall measure of the error in
prediction resulting from the use of the estimated
regression equation.
o.   ... ... .....   The proportion of the variability in the response that is
explained by the linear relationship between the
predictor and response' variables.
p.   ............   The vertical distance between the predicted response
and the actual response
q.   Represents the total variability in the values of the
response variable alone, without reference to the
predictor.
r.   -...................   Measures_the level of influence of an observation, by
taking into account both the size of the residual and
the amount of leverage for that observation.
2(a) In KNN Algorithm, Make up a set of three records, each with two numeric predictor
variables and one categorical target variable.so that the classification would not change   6
regardless of the value of k.
Refer to Exercise above. Alter your data set so that the classification changes for different
values of k.   ./-
2(b) Using the data in Table, find the k-nearest neighbor for record #10, using k = 3.   b
Record   Age   Marital   Income   Risk
1   22   Single   $46,156.98   Bad Loss
2   33   Married   $24,188.10   Bad Loss
3   28   Other   $28,787.34   Bad Loss
4   51   Other   $23,886.72   Bad Loss
5   25   Single   $47,281.44   Bad Loss
6   39   Single   $33,994.90   Good Risk
7   54   Single   $28,716.50   Good Risk
8   55   Married   $49,186.75   Good Risk
9   50   Married   $46,726.50   Good Risk
10   66   Married   $36,120.34   Good Risk
3(a)   In Dimension Reduction   , Mention the four criteria for choosing how many   b
components to extract. Explain the rationale for each.
3(b)   Explain the difference between principal components analysis and factor analysis.   6
--- page 3 ---
.
",'
4(a) Suppose that we go ahead and perform the PCA, in this case using seven components.
Considering the following information, which variable or variables might we be well
advised to omit from the PCA, and why? If we really need all these variables in the   f>
analysis, then what should we do?
Communalities
fnitlal   Extractkn   :
ZACC1LEN   t.OOO   .606 .
ZVr.M.ILME   1.000   .836
ZDAYCALL   1.000   .528.
· ZOAYCHAR   1.000   .954
ZEVECALL   1.000   .704
ZEVECHAR   1.000   .621
ZN1TECAL   1.000   .543
• ZNI1ECHA   1'.000   .637
· ZINTCALL   1.000   .439
· ZINTCHAR   1.000   .588
·zcsc   1.000   .710
Extractkn M:;thod: Principal Component Analy~ls.
4(b) Based on the following information, how many components should be extracted,
using (a) the eigenvalue criterion and (b) the proportion of variance explained criterion?   b
Inl.tia.lEtgenva!ues.
Component   Total   % of Variance   Cumu tanve %
1.088   fU190   9.&90
2   1.Q55   9.596   19,48e
3:   1.040   9.454   28.939
.;   1023   9296   38.236
5./   1JJO[l   9.094   41.329
5   .989   B.gS7   56.317
7   .972   8.B34   65151
a:   .969   8.811   • 73.961
9   963   875.1   B2.715
to   .961   8.747   91 A62
11   .839   8.539   100.000
Qu.5 (a) For Ensemble Methods: Bagging and Boosting ..
Describe two benefits of using an ensemble of classification models.
Qu5(b)   State the three steps of the bagging algorithm. How does bagging contribute to
a reduction in the prediction error?
Qu6 (a)   State thethree steps of the boosting algorithm.   6
Qu 6(b) The boosting algorithm uses a weighted average of a series of classifiers.
On what do the weights in this weighted average depend?
--- page 4 ---
Qu.7   (a) Discuss the benefits and drawbacks of a binary tree versus a bushier tree.   4
Qu7(b) Consider the data in Table X. The target variable is salary. Start by discretizing salary as   8
follows:
a. Less than $35,000 Level 1
b. $35,000 to less than $45,000 Level 2
c.   $45,000 to less than $55,000 Level 3
d Above $55,000 Level 4
Occupation   Gender   Age   Salary   Level
:
Service   Female   45   $48,000   3
Service   Male   25   $25,000   1
Service   Male   33   $35,000   2
Management   Male   25   $45,000   3
Management   Female   35   $65,000   4
Management   Male   26   $45,000   3
Management   Female   45   $70,000   4
Sales   Female   40   $50,000   3
Sales   .Male   30   $40,000   2
Staff   Female   50   $40,000   2
Staff   Male   25   $25,000   1
Table 1 Records
Construct a classification and regression tree to classify salary based on the other variables. Do as much
as you can by hand.   ./
-
````

## 2016-17 · Final-Exam · Sem 9 · paper 4eabfb835fe5

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/5TH YEAR/ALL STREAM/IX SEMESTER/DATA MINING AND ANALYTICS/Data Mining and Analytics Batch 2016-17 Final.pdf`
- Printed on paper: exam date: 14 December 2016
- Text: ocr (2 pages), mean OCR confidence 92.6
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: MBA Tech (All Streams) Year: V

Semester: IX
Academic Year: 2016-17

Subject: Data Mining and Analytics »
pmytomt. WEpin -
Date:14 December 2016. ; . Dur&tions: 22. Hire

Final Examination Vu

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary

Qla What is dimension reduction in Data Mining? Explain its importance. (2

Qlb What is principal component analysis method? Explain the four methods when you should stop carrying
out further analysis.

Q2 Explain the difference between the sequential sums of squares and the partial sums of squares. For which
procedures do we need these statistics? \2.

Q3 Make up a set of three records, each with two numeric predictor variables and one categorical target
variable, so that the classification would not change regardless of the value of k. {2

Q4 Discuss the benefits and drawbacks of a binary tree versus a bushier tree. (2
"Consider the data in Table 1. The target variable is salary. Start by discretizing salary as follows:

a. Less than $35,000 Level 1

b. $35,000 to less than $45,000 Level 2
ce. $45,000 to less than $55,000 Level 3
d. Above $55,000 Level 4

4}2
--- page 2 ---
TABLE 1 Decision tree data

Occupation Gender Age Salary
Service Female 45 $48,000
Male 25 $25,000
Male 33 $35,000
Management Male 25 $45,000
Female 35 $65,000
Male 26 $45,000
Female 45 $70,000
Sales Female 40 $50,000
Male 30 $40,000
Staff Female 50 $40,000
Male 25 $25,00

Q5 Discuss the use of predictors that turn out to be non-significant in estimating the response. When might this

be appropriate, if at all? Why would this not be appropriate in general? (2

(2

Q6a What is an intuitive idea for the meaning of the centroid of a cluster?

Q6b. Suppose that we have the following data:
(2,0) (1,2) (2,2) G.2) (2,3) 3,3) (2,4) (3,4) (4,4) 3,5)
Identify the cluster by applying the k-means algorithm, with k = 2. Try using initial cluster centers as far apart
as possible.

(2

Q7a State the three steps of the bagging algorithm.

Q7b How does bagging contribute to a reduction in the prediction error?

Q7c What is a downside of using bagging?
````
