# Computational Statistics: question papers in full

12 unique papers · 2022-23 to 2025-26 · Computer Science and Business Systems

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 3 · paper 869109f529a2

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSBS_7036/Computational Statistics/QP_Computational Statistics(702BS0C074)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: mixed (6 pages), mean OCR confidence 87.4

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Computational Statistics
Date: 28 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure to the right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
a. Based on the following regression output of Sales Employee Performance on Training
Hours and Experience. Answer the following:
Regression Output
Regression Statistics
Multiple R   0.941523
R Square   0.886465
Adjusted R Square   0.857456
Standard Error   3.89432
Observations   10
ANOVA Table
CO-1; SO- 1;
5
BL-1   Source   df   SS   MS   F   Significance F
Regression 2 640.23 320.12 21.12   0.0012
Residual   7 106.10 15.16
Total   9 746.33
Coefficients Table
Variable   Coefficient   Standard   t Stat   P-   Lower   Upper
Error   value   95%   95%
Intercept   35.214   4.513   7.80   0.0001   24.43   46.00
Training Hours   1.852   0.431   4.29   0.0031   0.78   2.92
Experience   2.305   0.645   3.57   0.0096   0.72   3.89
(years)
********** 1 **********
--- page 2 ---
1. What proportion of the variation in Employee Performance is explained by
Training Hours and Experience?
2. Which predictors significantly affect Employee Performance at the 5%
significance level?
3. Interpret the coefficient of Training Hours in the context of the regression
model.
4. Is the overall regression model statistically significant based on the F-test?
b. As a Marketing Analyst, you performed a factor analysis on customer perception
survey data. The rotated factor loadings are given below:
Variable   Factor 1   Factor 2   Factor 3
Product Quality   0.82   0.10   0.15
Product Reliability   0.78   0.12   0.10
Product Design   0.75   0.20   0.05
Brand Image   0.10   0.88   0.15
Advertisement Appeal   0.05   0.82   0.20
Social Media Presence   0.15   0.70   0.25
CO- 1; SO- 1;   Customer Loyalty   0.20   0.10   0.85   5
BL-4   Repeat Purchase Intent   0.10   0.15   0.80
Customer Trust   0.25   0.30   0.75
Price Perception   0.30   0.20   0.65
After-Sales Service   0.10   0.05   0.50
Delivery Speed   0.05   0.10   0.25
1. Identify the variables that load highly on each factor and name the likely
underlying factors.
2. Discuss how these factors can guide marketing strategies for enhancing
customer satisfaction and retention.
CO-2; SO-2;   c. Explain the objective of Linear Discriminant Analysis (LDA).Also discuss the key
5
BL-2   assumptions of LDA.
d. Write a Python code to count how many numbers in the given list are perfect squares.
CO-3; SO-1;
numbers = [4, 9, 16, 20, 25, 40, 49, 55, 64, 81]   5
BL-3
Q2
a.   𝑥1   0   1   0.2 0.1
X=[ 𝑥2 ] ~𝑁3 ([ 1 ] , [ 0.2 2   0.3 ]),
𝑥3   2   0.1 0.3   1
CO- 1; SO-2;
BL-3   Let 𝑦1 = 𝑥1 −𝑥2 + 2𝑥3 & 𝑦2 = 2𝑥1 + 𝑥2 −𝑥3.   10
Check whether y1 & y2 are independent. Also, find the distribution of y2.
b. Given the following measurements on two features, Compute the covariance matrix,
CO- 2; SO-6;   Find eigenvalues and eigenvectors & Determine the percentage of total variance
10
BL-3   captured by each principal component.
********** 2 **********
--- page 3 ---
Variable   Sample Sample 2 Sample 3 Sample 4 Sample 5 Sample
1   6
Feature A   3   4   5   2   6   1
Feature B   5   6   8   4   9   3
Q3
a.   𝑥1   2 5 1 2
X=[ 𝑥2 ] ~𝑁3 ([ 1 ] , [ 1 4 1 ]),
CO-1; SO-1;
𝑥3   0 2 1 3   10
BL-3   Find the conditional distribution of x1 | x2=2, x3=1. Also find the P(x1>3 | x2=2, x3=1).
b. Apply Complete Linkage Agglomerative Hierarchical Clustering to the following
dataset of 2D points: A(1,2),  B(2,3),  C(3,2),  D(6,5),  E(7,6),  F(8,5) .Draw the
CO- 2; SO-6;
dendrogram showing the hierarchy of clusters.   10
BL-3
Q4
a. A real estate analyst is studying how house price (Y, in ₹ lakhs) depends on two
factors:
• X1: Size of the house (in 1000 sq. ft.)
• X2: Number of years since construction
The fitted regression model is: Y=25+8X1−0.7X2
The data collected for 8 houses are:
10
Obs   X₁   X₂   Y (Actual)
1   1   5   32
CO- 1; SO-6;   2   2   3   39
BL-3
3   3   4   46
4   4   2   58
5   5   1   64
6   3   6   45
7   4   5   54
8   2   7   38
1. Compute the predicted values and residuals,
2. Draw a residual plot (residuals vs fitted values).
3. Compute: R2 Adjusted R2 & Standard Error.
Also, Comment on the overall fit of the model.
********** 3 **********
--- page 4 ---
b. A retail company compares two sales branches Branch A and Branch B based on two
performance metrics: Monthly Sales (in ₹ lakhs) and Customer Retention (out of 10).
The data collected are:
Monthly Sales (Variable 1):
• Branch A: 8, 10, 9
CO-1; SO-2;   • Branch B: 6, 5
10
BL-4   Customer Retention (Variable 2):
• Branch A: 7, 6, 8
• Branch B: 4, 5
Calculate Wilks’ Lambda & State whether there is a significant multivariate difference
in performance between the two branches.
Q5
a. A textile factory inspects fabric rolls based on Thickness (mm) and Tensile Strength
(MPa).Two quality groups are:
Thickness   Strength   Quality
0.50   5.2   Accept
0.55   5.5   Accept
10
0.60   5.8   Accept
0.45   5.0   Accept
0.70   6.4   Reject
CO-2; SO-1;   0.75   6.7   Reject
BL-3
0.80   6.9   Reject
Following is the mean and covariance of the groups
Classify a fabric roll with Thickness = 0.60 mm and Strength = 5.8 MPa.
b. List and explain any 5 assumptions of Linear Regression model.
CO- 1; SO-6;
10
BL-2
Q6
a. A business analyst wants to examine the relationship between advertising expenditure
(X) and monthly sales (Y).The following data are collected from 5 months:
CO-1; SO- 1;
10
BL-3
********** 4 **********
--- page 5 ---
Month   Sales   Advertising
(₹ in lakhs, Y)   (₹ in lakhs, X)
1   10   2
2   15   4
3   20   6
4   23   7
5   30   10
Fit the simple linear regression line &Obtain the variance of first fitted value and first
residual.
b. A health researcher wants to differentiate between fit and unfit individuals based on
two measurements blood pressure and heart rate.
CO-2; SO- 1;   •   Fit individuals (Group 1): {(1, 2), (2, 1), (2, 3), (3, 2)}
10
BL-5   •   Unfit individuals (Group 2): {(6, 7), (7, 6), (7, 8), (8, 7)}
Find the Linear Discriminant vector w that best separates the two groups.
Q7
CO-2; SO- 1;   a. Consider the following dataset of points in a 2D space:   10
BL-3   P1(1, 1), P2(2, 1), P3(4, 3), P4(5, 4), P5(7, 5), P6(8, 6)
Apply the K-Means algorithm with k = 2 clusters.
Take P1(1,1) and P5(7,5) as the initial centroids. Perform two iterations.
CO-3; SO- 1;   b. Write a Python class Student that stores a student’s name, roll_number, and   10
BL-2   marks (list of 5 subjects). Include methods to:
1. Compute the total marks
2. Compute the average marks
3. Determine the grade based on average marks (≥90: A, ≥75: B, ≥60: C, else D)
Display all details including name, roll number, total, average, and grade for one
student.
********** 5 **********
--- page 6 ---
STANDARD NORMAL TABLE (Z)

Entries in the table give the area under the curve
between the mean and z standard deviations above
the mean. For example, for z= 1.25 the area under
the curve between the mean (0) and z is 0.3944.

15 2 3

ZN o.00/ 0.01| 0.02] 0.03] 0.04] 0.05| 0.06] 0.07| 0.08] 0.09

0.0} 0.0000 0.0040 0.0080 0.0120 0.0160 0.0190 0.0239 0.0279 0.0319 0.0359

0.1 | 0.0398 0.0438 0.0478 0.0517 0.0557 0.0596 0.0636 0.0675 0.0714 0.0753

0.2 | 0.0793 0.0832 0.0871 0.0910 0.0948 0.0987 0.1026 0.1064 0.1103 0.1141

0.3 | 0.1179 0.1217 0.1255 0.1293 0.1331 0.1368 0.1406 0.1443 0.1480 0.1517

0.4 | 0.1554 0.1591 0.1628 0.1664 0.1700 0.1736 0.1772 0.1808 0.1844 0.1879

0.5/ 0.1915 0.1950 0.1985 0.2019 0.2054 0.2088 0.2123 0.2157 0.2190 0.2224

0.6 | 0.2257 0.2291 0.2324 0.2357 0.2389 0.2422 0.2454 0.2486 0.2517 0.2549

0.7 | 0.2580 0.2611 0.2642 0.2673 0.2704 0.2734 0.2764 0.2794 0.2823 0.2852

0.8 | 0.2881 0.2910 0.2939 0.2969 0.2995 0.3023 0.3051 0.3078 0.3106 0.3133

0.9 | 0.3159 0.3186 0.3212 0.3238 0.3264 0.3289 0.3315 0.3340 0.3365 0.3389

1.0) 0.3413 0.3438 0.3461 0.3485 0.3508 0.3513 0.3554 0.3577 0.3529 0.3621

1.1) 0.3643 0.3665 0.3686 0.3708 0.3729 0.3749 0.3770 0.3790 0.3810 0.3830

1.2 | 0.3849 0.3869 0.3888 0.3907 0.3925 0.3944 0.3962 0.3980 0.3997 0.4015

1.3 | 0.4032 0.4049 0.4066 0.4082 0.4099 0.4115 0.4131 0.4147 0.4162 0.4177

1.4 | 0.4192 0.4207 0.4222 0.4236 0.4251 0.4265 0.4279 0.4292 0.4306 0.4319

1.5) 0.4332 0.4345 0.4357 0.4370 0.4382 0.4394 0.4406 0.4418 0.4429 0.4441

1.6) 0.4452 0.4463 0.4474 0.4484 0.4495 0.4505 0.4515 0.4525 0.4535 0.4545

1.7 | 0.4554 0.4564 0.4573 0.4582 0.4591 0.4599 0.4608 0.4616 0.4625 0.4633

1.8 | 0.4641 0.4649 0.4656 0.4664 0.4671 0.4678 0.4686 0.4693 0.4699 0.4706

1.9) 0.4713 0.4719 0.4726 0.4732 0.4738 0.4744 0.4750 0.4756 0.4761 0.4767

2.0 | 0.4772 0.4778 0.4783 0.4788 0.4793 0.4798 0.4803 0.4808 0.4812 0.4817

2.1 | 0.4821 0.4826 0.4830 0.4834 0.4838 0.4842 0.4846 0.4850 0.4854 0.4857

2.2 | 0.4861 0.4864 0.4868 0.4871 0.4875 0.4878 0.4881 0.4884 0.4887 0.4890

2.3 | 0.4893 0.4896 0.4898 0.4901 0.4904 0.4906 0.4909 0.4911 0.4913 0.4916

2.4| 0.4918 0.4920 0.4922 0.4925 0.4927 0.4929 0.4931 0.4932 0.4934 0.4936

2.5 | 0.4938 0.4940 0.4941 0.4943 0.4945 0.4946 0.4948 0.4949 0.4951 0.4952

2.6 | 0.4953 0.4955 0.4956 0.4957 0.4959 0.4960 0.4961 0.4962 0.4963 0.4964

2.7 | 0.4965 0.4966 0.4967 0.4968 0.4969 0.4970 0.4971 0.4972 0.4973 0.4974

2.8 | 0.4974 0.4975 0.4976 0.4977 0.4977 0.4978 0.4979 0.4979 0.4980 0.4981

2.9 | 0.4981 0.4982 0.4982 0.4983 0.4984 0.4984 0.4985 0.4985 0.4986 0.4986

3.0 | 0.4987 0.4987 0.4987 0.4988 0.4988 0.4989 0.4989 0.4989 0.4990 0.4990

3.1} 0.4990 0.4991 0.4991 0.4991 0.4992 0.4992 0.4992 0.4992 0.4993 0.4993

3.2 | 0.4993 0.4993 0.4994 0.4994 0.4994 0.4994 0.4994 0.4995 0.4995 0.4995

3.3 | 0.4995 0.4995 0.4995 0.4996 0.4996 0.4996 0.4996 0.4996 0.4996 0.4997

3.4 | 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4998

FIC 6 I HF
````

## 2025-26 · Final-Exam · Sem 3 · paper 97cd86c3bb9d

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSBS/SEM-III/COMPUTATIONAL STATISTICS/Computational Statistics, Sem-III, Year 2025-26 Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: ocr (6 pages), mean OCR confidence 88.0

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS) <
Year: II/Semester IJJ(Exam Year: 2025-2026)

Subject: Computational Statistics
Date: 28 Nov 2025 Time: 10:00 am to 01:00 pm (03:00 Hrs.)

Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions:

1. This question paper contains 6 pages.

2. Answer to each new question to be started on a fresh page.

3. Figure to the right hand side indicates full marks.

4. Question No. 1 is compulsory.

5. Out of remaining questions, attempt any 4 questions.

6. All questions carry equal marks.

7. Figures in brackets on the right hand side indicate full marks.
on 8. Assume Suitable data if necessary.

»

a. | Based on the following regression output of Sales Employee Performance on Training
Hours and Experience. Answer the following: ;

Regression Output

Regression Statistics

Multiple R 0.941523
R Square 0.886465
Adjusted R Square 0.857456
Standard Error 3.89432
Observations 10
© ANOVA Table
CO-1; SO- 1; ‘ 5
BL-1 Source | df| SS MS F | Significance F

Regression | 2 | 640.23 | 320.12 | 21.12 0.0012

Residual | 7 | 106.10 | 15.16

Total 9 | 746.33

Coefficients Table

Variable Coefficient | Standard | t Stat P- Lower Upper
Error value 95% 95%
Intercept 35.214 - 4.513 7.80 | 0.0001 | 24.43 46.00
. Training Hours 1.852 0.431 4.29 | 0.0031 0.78 2.92
Experience 2.305 0.645 3.57 | 0.0096 0.72 3.89
(years)

SAR IK kaa
.
--- page 2 ---
1. What proportion of the variation in Employee Performance is explained by
Training Hours and Experience?

2. Which predictors significantly affect Employee Performance at the 5%

significance level? ve
3. Interpret the coefficient of Training Hours in the context of the regression
model.

4. Is the overall regression model Statistically significant based on the F-test?

b. | As a Marketing Analyst, you performed a factor analysis on customer perception
survey data. The rotated factor loadings are given below:

Variable Factor 1 Factor 2 Factor 3
Product Quality 0.82 0.10 0.15
Product Reliability 0.78 0.12 0.10
Product Design 0.75 0.20 0.05
Brand Image 0.10 0.88 0.15
Advertisement Appeal 0.05 0.82 0.20
Social Media Presence 0.15 0.70 0.25
CO- 1; SO- 1; Customer Loyalty 0.20 0.10 0.85 §
BL-4
Repeat Purchase Intent 0.10 0.15 0.80
Customer Trust 0.25 0.30 0.75
Price Perception 0.30 0.20 0.65
After-Sales Service 0.10 0.05 0.50
Delivery Speed 0.05 0.10 0.25
1. Identify the variables that load highly on each factor and name the likely
underlying factors.
2. Discuss how these factors can guide marketing strategies for enhancing
customer satisfaction and retention.
CO-2; SO-2; | c. | Explain the objective of Linear Discriminant Analysis (LDA).Also discuss the key :
a d 5
BL-2 assumptions of LDA.
d. | Write a Python code to count how many numbers in the given list are perfect squares.
e081 SOAs numbers = [4, 9, 16, 20, 25, 40, 49, 55, 64, 81] 5
Q2
x4 OJ J 1 02 O41
X=|%2|~N3 ( 1], e2 2 03)),
x3 21 10.1 03 1
CO- 1; SO-2;
BL-3 Let y1 =X — X2 +2x3 & y2 = 2x, + x2 — 23. 10
Check whether y1 & y2 are independent. Also, find the distribution of y2.
* Lal
f 4 Given the following measurements on two features, Compute the covariance matrix,
CO- 2; SO-6; Find eigenvalues and eigenvectors & Determine the percentage of total variance 10
BL-3 captured by each principal component.

FRA RRR DR HK

.
--- page 3 ---
Variable | Sample | Sample 2 | Sample 3 | Sample 4 | Sample 5 | Sample

1 ul 6
Feature A 3 4 5 2 6 1
Feature B 5 6 8 4 9 3
Q3
xy 2) [5 1 2
=|X2] ~
cCo-1;$0-1; | |*%-/%2}~Ns\]2)]2 4 1)
BL-3 _ «(Xs LO 12 10 31 10
Find the conditional distribution of x: | x2=2, x3=1. Also find the P(x1>3 | x2=2, x3=1).
a Apply Complete Linkage Agglomerative Hierarchical Clustering to the following
. dataset of 2D points: A(1,2), B(2,3), C(3,2), D(6,5), E(7,6), F(8,5) .Draw the
CO- 2; SO-6; f :
BL-3 dendrogram showing the hierarchy of clusters. 10
Q4
A real estate analyst is studying how house price (Y, in % lakhs) depends on two
factors:
e XI: Size of the house (in 1000 sq. ft.)
e X2: Number of years since construction
The fitted regression model is: Y=25+8X1—0.7X2
The data collected for 8 houses are: 10
Ta Obs Xi X2 Y (Actual)
° 1 1. 5 32
CO- 1; SO-6; 2. 2 3 39
BL-3
3 3 4 46
4 4 2 58
5 5 1 64
6 3 6 45
7 4 5 54
8 2 7 38

1. Compute the predicted values and residuals,

2. Draw a residual plot (residuals vs fitted values).

3. Compute: R? Adjusted R? & Standard Error.
Also, Comment on the overall fit of the model.

FIO 3 doi ak &
--- page 4 ---
A retail company compares two sales branches Branch A and Branch B based on two
performance metrics: Monthly Sales (in & lakhs) and Customer Retention (out of 10).

The data collected are:
Monthly Sales (Variable 1):
e Branch A: 8,10, 9

CO-1; SO-2; e Branch B: 6, 5 ~ 10
BL-4 Customer Retention (Variable 2):
¢ Branch A: 7, 6, 8
e Branch B: 4, 5
Calculate Wilks’ Lambda & State whether there is a significant multivariate difference
in performance between the two branches.
~
Q5
a. | A textile factory inspects fabric rolls based on Thickness (mm) and Tensile Strength
(MPa).Two quality groups are: .
Thickness Strength Quality
0.50 Ded Accept
0.55 33 Accept 10
0.60 5.8 Accept
0.45 5.0 Accept
0.70 6.4 Reject
a eee 0.75 6.7 Reject
: 0.80 6.9 Reject -
Following is the mean and covariance of the groups
Ha = (0.525, 5.375), jz = (0.75, 6.67)
C.= 0.0025. 0.012 Cr= 0.0035 0.018 .
4~ {0.012 0.092}° °%*® =| 0.018 0.130
Classify a fabric roll with Thickness = 0.60 mm and Strength = 5.8 MPa.
CO- 1; $0-6; b. | List and explain any 5 assumptions of Linear Regression model. 0
BL-2
Q6
a. | A business analyst wants to examine the relationship between advertising expenditure
(X) and monthly sales (Y).The following data are collected from 5 months:
CO-1; SO- 1; 10
BL-3 +

my

FIR OR RE

. .
--- page 5 ---
Month Sales Advertising
(% in lakhs, Y) | (% in lakhs, X)
1 10 2
F

2 15 4 ~
3 20 6
4 23 7

; 5 30 10

Fit the simple linear regression line &Obtain the variance of first fitted value and first
residual.

A health researcher wants to differentiate between fit and unfit individuals based on
two measurements blood pressure and heart rate.

CO-2; SO- 1; e Fit individuals (Group 1): {(1, 2), (2, 1), (2, 3), (3, 2)} 10
a BL-5 ¢ Unfit individuals (Group 2): {(6, 7), (7, 6), (7, 8), (8, 7)}
Find the Linear Discriminant vector w that best separates the two groups.
Q7
CO-2; SO- 1; Consider the following dataset of points in a 2D space: 10
BL-3 P1(1, 1), P2(2, 1), P3(4, 3), P4(5, 4), P5(7, 5), P6(8, 6)
Apply the K-Means algorithm with k = 2 clusters.
Take P1(1,1) and P5(7,5) as the initial centroids. Perform two iterations.
CO-3; SO- 1; Write a Python class Student that stores a student’s name, roll_number, and 10°
BL-2 marks (list of 5 subjects). Include methods to:
_1. Compute the total marks
> 2. Compute the average marks

3. Determine the grade based on average marks (290: A, >75: B, >60: C, else D)

Display all details including name, roll number, total, average, and grade for one
student.

FIG x
--- page 6 ---
STANDARD NORMAL TABLE (Z)

Entries in the table give the area under the curve
between the mean and z standard deviations above
the mean. For example, for z = 1.25 the aréa under
the curve between the mean (0) and z is 0.3944.

ez 0.00{ 0.01{ 0.02] 0.03] 0.04] 0.05| 0.06] 0.07| 0.08| 0.09
0.0 | 0.0000 0.0040 0.0080 0.0120 0.0160 0.0190 0.0239 0.0279 0.0319 0.0359
0.1 | 0.0398 0.0438 0.0478 0.0517 0.0557 0.0596 0.0636 0.0675 0.0714 0.0753
0.2 | 0.0793 0.0832 0.0871 0.0910 0.0948 0.0987 0.1026 0.1064 0.1103 0.1141
0.3 | 0.1179 0.1217 0.1255 0.1293 0.1331 0.1368 0.1406 0.1443 0.1480 0.1517
0.4 | 0.1554 0.1591 0.1628 0.1664 0.1700 0.1736 0.1772 0.1808 0.1844 0.1879
0.5 | 0.1915 0.1950 0.1985 0.2019 0.2054 0.2088 0.2123 0.2157 0.2190 0.2224
0.6 | 0.2257 0.2291 0.2324 0.2357 0.2389 0.2422 0.2454 0.2486 0.2517 0.2549
0.7 | 0.2580 0.2611 0.2642. 0.2673 0.2704 0.2734 0.2764 0.2794 0.2823 0.2852
0.8 | 0.2881 0.2910 0.2939 0.2969 0.2995 0.3023 0.3051 0.3078 0.3106 0.3133
0.9 | 0.3159 0.3186 0.3212 0.3238 0.3264 0.3289 0.3315 0.3340 0.3365 0.3389
1.0 | 0.3413 0.3438 0.3461 0.3485 0.3508 0.3513 0.3554 0.3577 0.3529 0.3621
1.1 | 0.3643 0.3665 0.3686 0.3708 0.3729 0.3749 0.3770 0.3790 0.3810 0.3830
1.2 | 0.3849 0.3869 0.3888 0.3907 0.3925 0.3944 0.3962 0.3980 0.3997 0.4015
1.3 | 0.4032 0.4049 0.4066 0.4082 0.4099 0.4115 0.4131 0.4147 0.4162 0.4177
1.4 | 0.4192 0.4207 0.4222 0.4236 0.4251 0.4265 0.4279 0.4292 0.4306 0.4319
1.5 | 0.4332 0.4345 0.4357 0.4370 0.4382 0.4394 0.4406 0.4418 0.4429 0.4441
1.6 | 0.4452 0.4463 0.4474 0.4484 0.4495 0.4505 0.4515 0.4525 0.4535 0.4545
1.7 | 0.4554 0.4564 0.4573 0.4582 0.4591 0.4599 0.4608 0.4616 0.4625 0.4633
1.8 | 0.4641 0.4649 0.4656 0.4664 0.4671 0.4678 0.4686 0.4693 0.4699 0.4706
1.9 | 0.4713 0.4719 0.4726 0.4732 0.4738 0.4744 0.4750 0.4756 0.4761 0.4767

2.0 | 0.4772 0.4778 0.4783 0.4788 0.4793 0.4798 0.4803 0.4808 0.4812 0.4817

2.1 | 0.4821 0.4826 0.4830 0.4834 0.4838 0.4842 0.4846 0.4850 0.4854 0.4857
2.2 | 0.4861 0.4864 0.4868 0.4871 0.4875 0.4878 0.4881 0.4884 0.4887 0.4890
2.3 | 0.4893 0.4896 0.4898 0.4901 0.4904 0.4906 0.4909 0.4911 0.4913 0.4916

2.4 | 0.4918 0.4920 0.4922 0.4925 0.4927 0.4929 0.4931 0.4932 0.4934 0.4936

2.5 0.4938 0.4940 0.4941 0.4943 0.4945 0.4946 0.4948 0.4949 0.4951 0.4952

2.6 | 0.4953 0.4955 0.4956 0.4957 0.4959 0.4960 0.4961 0.4962 0.4963 0.4964
2.7 | 0.4965 0.4966 0.4967 0.4968 0.4969 0.4970 0.4971 0.4972 0.4973 0.4974

2.8 | 0.4974 0.4975 0.4976 0.4977 0.4977 0.4978 0.4979 0.4979 0.4980 0.4981

2.9 | 0.4981 0.4982 0.4982 0.4983 0.4984 0.4984 0.4985 0.4985 0.4986 0.4986

3.0 | 0.4987 0.4987 0.4987 0.4988 0.4988 0.4989 0.4989 0.4989 0.4990 0.4990

3.1] 0.4990 0.4991 0.4991 0.4991 0.4992 0.4992 0.4992 0.4992 0.4993 0.4993
3.2 | 0.4993 0.4993 0.4994 0.4994 0.4994 0.4994 0.4994 0.4995 0.4995 0.4995

3.3 | 0.4995 0.4995 0.4995 0.4996 0.4996 0.4996 0.4996 0.4996 0.4996 0.4997

3.4 | 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4998

FICCI 6 a kak
````

## 2025-26 · Re-Exam · Sem 3 · paper fd77a0ab6d8a

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CSBS_7036/Computational Statistics/QP_Computational Statistics(702BS0C074)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (6 pages), mean OCR confidence 87.4

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Computational Statistics
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure to the right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
a. Based on the following regression output of Sales Prediction on Advertising and Price.
Answer the following
Regression Output
Regression Statistics
Multiple R   0.905123
R Square   0.819247
Adjusted R Square   0.780514
Standard Error   12.58391
Observations   12
CO-1; SO- 1;   ANOVA Table   5
BL-1
Source   df   SS   MS   F   Significance F
Regression   2   10560.42   5280.21 33.34   0.0003
Residual   9   1424.10   158.23
Total   11   11984.52
Coefficients Table
Variable   Coeffici   Standard   t Stat   P-value   Lower   Upper
ent   Error   95%   95%
Intercept   45.231   8.120   5.57   0.0004   26.58   63.88
Advertising   2.845   0.495   5.75   0.0003   1.73   3.96
Price   -1.502   0.531   -2.83   0.0189   -2.66   -0.34
********** 1 **********
--- page 2 ---
1. What proportion of the variation in Sales is explained by the independent
variables Advertising and Price?
2. Based on the p-values, which predictors significantly affect Sales at the 5%
level of significance?
3. How does a one-unit increase in Advertising affect Sales, keeping Price
constant?
4. State the regression equation.
b. As an Education Researcher, you conducted a factor analysis on student feedback
about learning experiences. The rotated factor loadings are shown below:
Variable   Factor 1   Factor 2   Factor 3
Concept Understanding   0.80   0.15   0.10
Problem-Solving Skills   0.75   0.20   0.05
Critical Thinking   0.70   0.25   0.10
Instructor Clarity   0.10   0.88   0.15
Teaching Style   0.20   0.85   0.10
Feedback and Support   0.05   0.70   0.25
CO- 1; SO- 1;   Peer Interaction   0.25   0.15   0.85
5
BL-4   Group Projects   0.10   0.10   0.80
Learning Engagement   0.30   0.20   0.75
Motivation to Learn   0.25   0.30   0.65
Attendance   0.15   0.10   0.45
Use of Technology   0.05   0.05   0.25
1. Identify which variables load highly on each factor and name the underlying
factors.
2. Explain how these identified factors can inform strategies to improve teaching
quality and student performance.
c.   State the objective of Principal Component Analysis (PCA) and list its key
CO-2; SO-2;   assumptions.
5
BL-3
d. Write a Python code to count how many numbers in the given list are divisible by both
5 and 7. Return (or print) the count.
CO-3; SO-1;
5
BL-4
numbers = [35, 70, 14, 49, 40, 105, 140, 21, 50, 75]
Q2
a.   𝑥1   0   1   0.2 0.1
X=[ 𝑥2 ] ~𝑁3 ([ 1 ] , [ 0.2 2   0.3 ]),
CO- 1; SO-2;   𝑥3   2   0.1 0.3   1
10
BL-3
Find the distribution of 𝑦= 𝑥1 −𝑥2 + 2𝑥3. Also find the probability of P(y>2)
b. A dataset contains the following 8 observations on two variables X1 and X2. Perform a
CO- 2; SO-6;
Principal Component Analysis (PCA) and determine the proportion of total variance 10
BL-3
explained by each principal component.
********** 2 **********
--- page 3 ---
Variable Obs 1   Obs 2   Obs 3   Obs 4   Obs 5   Obs 6   Obs 7   Obs 8
X₁   4   2   3   5   6   1   2   4
X₂   2   0   1   3   4   -1   1   2
Q3
a. Suppose the IQ scores (X) of fathers and (Y) their sons follow a bivariate normal
distribution. The parameters are:
CO-1; SO-1;   μX=110, σX=15, μY=105, σY=12, ρ=0.7
10
BL-3
1. Find the expected IQ of the son given that the father’s IQ is 130.
2. Find the variance of the son’s IQ given that the father’s IQ is 130.
b. Apply Single Linkage Agglomerative Hierarchical Clustering to the following dataset
of 2D points: A(1,2),  B(2,3),  C(3,2),  D(6,5),  E(7,6),  F(8,5) .Also, Draw the
CO- 2; SO-6;
dendrogram showing the hierarchy of clusters.   10
BL-3
Q4
a. A company records data on 8 sales representatives to study how sales performance
depends on three factors
• X1: Years of experience
• X2: Number of client meetings per week
• X3: Hours spent on follow-ups per week
The fitted regression equation for predicting sales (in ₹ lakhs) is:
Y=5+0.4X1+0.8X2−0.3X3   10
The observed data are:
CO- 1; SO-6;   Obs   X₁   X₂   X₃   Y (Actual)
BL-2
1   1   2   1   7.2
2   2   1   2   7.4
3   3   2   3   8.1
4   4   3   2   9.3
5   3   3   1   9.5
6   5   2   3   9.8
7   4   4   2   10.2
8   6   3   1   11.1
1. Compute the residuals and plot a residual plot (residuals vs fitted values).
2. Compute: R2, Adjusted R2, Standard Error & Interpret whether the regression model
fits the data well.
********** 3 **********
--- page 4 ---
b. A university is assessing student outcomes in two programs Engineering and Business
based on two dependent variables: Mathematics Score and Communication Skill Score.
The data for students are as follows:
Mathematics Scores (Dependent Variable 1):
• Engineering: 85, 90, 88
•   Business: 70, 72
CO-1; SO-2;   Communication Scores (Dependent Variable 2):
10
BL-3   •   Engineering: 60, 65, 70
•   Business: 75, 80
Using this data, Compute Wilks’ Lambda & Conclude whether there is a significant
difference between the two programs in terms of mathematics and communication
skills.
Q5
a. A company monitor’s food packaging quality using two features Seal Strength (N) and
Temperature (°C) to decide if a packet is Good or Defective.
Seal Strength   Temperature   Quality
45   32   Good
47   34   Good
48   33   Good
10
49   35   Good
40   38   Defective
42   36   Defective
CO-2; SO-1;
BL-3   46   40   Defective
These are the mean vectors and covariance matrices of the two groups Good &
defective.
Determine whether a packet with Seal Strength = 45 N and Temperature = 35°C will
be Good or Defective.
b. List and explain the different metrics used to evaluate multiple Linear Regression
CO- 1; SO-6;
model.   10
BL-2
Q6
a. A manager wants to study how the number of training hours (X) affects employee
CO-1; SO- 1;   productivity (Y).The data collected from 5 employees are:
10
BL-3
********** 4 **********
--- page 5 ---
Employee   Productivity   Training
Score (Y)   Hours (X)
1   40   5
2   50   10
3   60   15
4   65   20
5   80   30
Fit a simple linear regression model to predict Productivity (Y) from Training Hours
(X).Also Compute the variance of the OLS coefficients Var(b0) and Var(b1).
b. A bank wants to classify its customers into two groups based on their loan repayment
patterns. The following are the 2D features for each group:
• Group 1 (Good Credit):
CO-2; SO- 1;   {(2, 3), (3, 3), (4, 5), (3, 4)}
10
BL-4   • Group 2 (Bad Credit):
{(6, 8), (7, 9), (8, 7), (7, 8)}
Find the Linear Discriminant vector w that best separates the two groups.
Q7
CO-2; SO- 1;   a. Consider the following dataset of 2D points:   10
BL-3   P1(2, 3), P2(3, 4), P3(4, 2), P4(6, 7), P5(7, 5), P6(8, 6), P7(5, 8)
Apply the K-Means algorithm with k = 3 clusters. Select the initial centroids as:
C₁ = P1(2, 3), C₂ = P4(6, 7), C₃ = P6(8, 6). Perform two iterations.
CO-3; SO- 1;   b. Create a Python class Rectangle with attributes length and width.   10
BL-2   Include the following methods:
• area() to compute the area
• perimeter() to compute the perimeter
• is_square() that returns True if the rectangle is also a square
Write a main program that Creates two Rectangle objects , one square and one
rectangle & Displays their area, perimeter, and whether they are squares.
********** 5 **********
--- page 6 ---
STANDARD NORMAL TABLE (Z)

Entries in the table give the area under the curve
between the mean and z standard deviations above
the mean. For example, for z= 1.25 the area under
the curve between the mean (0) and z is 0.3944.

15 2 3

ZN o.00/ 0.01| 0.02] 0.03] 0.04] 0.05| 0.06] 0.07| 0.08] 0.09

0.0} 0.0000 0.0040 0.0080 0.0120 0.0160 0.0190 0.0239 0.0279 0.0319 0.0359

0.1 | 0.0398 0.0438 0.0478 0.0517 0.0557 0.0596 0.0636 0.0675 0.0714 0.0753

0.2 | 0.0793 0.0832 0.0871 0.0910 0.0948 0.0987 0.1026 0.1064 0.1103 0.1141

0.3 | 0.1179 0.1217 0.1255 0.1293 0.1331 0.1368 0.1406 0.1443 0.1480 0.1517

0.4 | 0.1554 0.1591 0.1628 0.1664 0.1700 0.1736 0.1772 0.1808 0.1844 0.1879

0.5/ 0.1915 0.1950 0.1985 0.2019 0.2054 0.2088 0.2123 0.2157 0.2190 0.2224

0.6 | 0.2257 0.2291 0.2324 0.2357 0.2389 0.2422 0.2454 0.2486 0.2517 0.2549

0.7 | 0.2580 0.2611 0.2642 0.2673 0.2704 0.2734 0.2764 0.2794 0.2823 0.2852

0.8 | 0.2881 0.2910 0.2939 0.2969 0.2995 0.3023 0.3051 0.3078 0.3106 0.3133

0.9 | 0.3159 0.3186 0.3212 0.3238 0.3264 0.3289 0.3315 0.3340 0.3365 0.3389

1.0) 0.3413 0.3438 0.3461 0.3485 0.3508 0.3513 0.3554 0.3577 0.3529 0.3621

1.1) 0.3643 0.3665 0.3686 0.3708 0.3729 0.3749 0.3770 0.3790 0.3810 0.3830

1.2 | 0.3849 0.3869 0.3888 0.3907 0.3925 0.3944 0.3962 0.3980 0.3997 0.4015

1.3 | 0.4032 0.4049 0.4066 0.4082 0.4099 0.4115 0.4131 0.4147 0.4162 0.4177

1.4 | 0.4192 0.4207 0.4222 0.4236 0.4251 0.4265 0.4279 0.4292 0.4306 0.4319

1.5) 0.4332 0.4345 0.4357 0.4370 0.4382 0.4394 0.4406 0.4418 0.4429 0.4441

1.6) 0.4452 0.4463 0.4474 0.4484 0.4495 0.4505 0.4515 0.4525 0.4535 0.4545

1.7 | 0.4554 0.4564 0.4573 0.4582 0.4591 0.4599 0.4608 0.4616 0.4625 0.4633

1.8 | 0.4641 0.4649 0.4656 0.4664 0.4671 0.4678 0.4686 0.4693 0.4699 0.4706

1.9) 0.4713 0.4719 0.4726 0.4732 0.4738 0.4744 0.4750 0.4756 0.4761 0.4767

2.0 | 0.4772 0.4778 0.4783 0.4788 0.4793 0.4798 0.4803 0.4808 0.4812 0.4817

2.1 | 0.4821 0.4826 0.4830 0.4834 0.4838 0.4842 0.4846 0.4850 0.4854 0.4857

2.2 | 0.4861 0.4864 0.4868 0.4871 0.4875 0.4878 0.4881 0.4884 0.4887 0.4890

2.3 | 0.4893 0.4896 0.4898 0.4901 0.4904 0.4906 0.4909 0.4911 0.4913 0.4916

2.4| 0.4918 0.4920 0.4922 0.4925 0.4927 0.4929 0.4931 0.4932 0.4934 0.4936

2.5 | 0.4938 0.4940 0.4941 0.4943 0.4945 0.4946 0.4948 0.4949 0.4951 0.4952

2.6 | 0.4953 0.4955 0.4956 0.4957 0.4959 0.4960 0.4961 0.4962 0.4963 0.4964

2.7 | 0.4965 0.4966 0.4967 0.4968 0.4969 0.4970 0.4971 0.4972 0.4973 0.4974

2.8 | 0.4974 0.4975 0.4976 0.4977 0.4977 0.4978 0.4979 0.4979 0.4980 0.4981

2.9 | 0.4981 0.4982 0.4982 0.4983 0.4984 0.4984 0.4985 0.4985 0.4986 0.4986

3.0 | 0.4987 0.4987 0.4987 0.4988 0.4988 0.4989 0.4989 0.4989 0.4990 0.4990

3.1} 0.4990 0.4991 0.4991 0.4991 0.4992 0.4992 0.4992 0.4992 0.4993 0.4993

3.2 | 0.4993 0.4993 0.4994 0.4994 0.4994 0.4994 0.4994 0.4995 0.4995 0.4995

3.3 | 0.4995 0.4995 0.4995 0.4996 0.4996 0.4996 0.4996 0.4996 0.4996 0.4997

3.4 | 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4998

FIC 6 I HF
````

## 2024-25 · Final + Re-Exam · Sem 3 · paper f402a868b37c

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSBS/SEM-III/COMPUTATIONAL STATISTICS/Computational Statistics, Sem-III, Final Exam 2024-25 & Re Exam 2022-23, 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 86.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025

Program: B Tech Stream : CSBS Year: Il Semester: III

Subject: Computational Statistics Time: 3 hrs (10:00am to 1£00pm)
Date:_04/12/2024 No. of Pages:6

Marks:100 :

Final Examination (2024-2025) /Re Exam 22-23,23-24
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
(© 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi j

a. | What are the assumptions of linearity and independence in a linear regression model?

Additionally, the following four models have been developed, with an increasing number
of predictors in each:

cee | * Model 1 (2 predictors): Adjusted R? = 0.60 5
e Model 2 (4 predictors): Adjusted R? = 0.65
¢ Model 3 (6 predictors): Adjusted R? = 0.67
¢ Model 4 (8 predictors): Adjusted R? = 0.66 .
Based on the Adjusted R? values, which model would you select and why?
b. | As a human resources manager, you have conducted a factor analysis on the data collected
G from applicants, focusing on 12 measured variables. Below are the rotated factor loadings
obtained from your analysis:
| Variable | Factor 1 || Factor 2 l Factor 3 |
[VariableA |] 0.85 || 0.10 || 0.05 |
[ VariableB || 0.80 |[ 0.15 || 0.10]
| VariableC || 0.70 |[ 0.25 || 0.20 |
_ CO- 1; SO- 1; [VariableD || 0.10 || 0.90 || 0.05 | 5
; BL-4 VariableE || 0.15 || 0.85 || 0.10 |
mes [ VariableF || 0.05 |[ 0.70 . 0.25 |
| VariableG || 0.20. || 0.10 || 0.90 |
[VariableH || 0.05 || 0.15 || 0.80 |
_LVariablel [0.30 || 020 || 075 |
[ VariableJ |] 0.25 || 0.30 0.60
[VariableK | 0.10 || 0.05 || 0.50
[VariableL | 0.05 | 0.10 | 020 |

A/V
--- page 2 ---
Analyse the rotated factor loadings and answer the following questions:

1. Identify which variables are strongly associated with each factor based on the
loadings provided.

2. Discuss how the identified factors might influence the hiring decisions in the
human resources depaitment.

: . |¢. | Compare Linear discriminant Analysis (LDA), Principal Component Analysis (PCA) &
ey BD Factor Analysis (FA 5
BL-4 actor Analysis (FA).
d. | Write a Python code to count how many numbers in a given list are divisible by both 3
CO-3; SO-1; and 4. Return the count. 5
BL-5
Given list of numbers: [12, 24, 36, 10, 15,48, 60, 72, 5, 9]
Q2 _ >
* | Given ¥ N3(, Z), where: “
nm] ~ 1 2 0 -1
Y=|m|/, w=|4], B=]0 3 2
Ys =2 -12 4
CO- 1: SO-2: Which of the following random variables are independent?
BL 3 ; a
° ey &Yy
© (M1593) & ye
5 yWskYy + -
Also, find the distribution of 2y; — yo + 3y3.
b. | Conduct principal component analysis (PCA) on the following dataset with 6 observations
and 2 features. Report the total sample variance explained by each of the principal >
components:
CO- 2; SO-6; 5 10
BL-3 8 6 7 9 5 10
45 3 6 7 2
Q3
a. | A company is analysing the sales performance of its three best-selling products: Product
CO-1; SO-1; A, Product B, and Product C. The sales figures (in thousands) for these products follow a 10
BL-3 multivariate normal distribution:

2/6
--- page 3 ---
6 5 wH2 1
Y~N3(u,U), w= {2}, U=}]-2 3 0
8 1 0 6

1. What is the probability that the sales of Product A exceed 7 thousand units?

2. Géiven that the sales of Product B are 0 thousand units and Product C are 5
thousand units, what is the conditional probability that the sales of Product A
exceed 7 thousand units?

3. Determine the probability that two times the sales of Product A, minus the sales of
Product B, plus four times the sales of Product C is less than 50 thousand units.

b. | Apply Single Linkage Agglomerative, Hierarchical Clustering to the following dataset:

oy “7

2 3
5.64
1 2
CO- 2; $0-6; 8 7 0
BL-3 6 8
7 5

Also, Draw the dendrogram to illustrate the clustering process and the hierarchy of the
clusters formed. .

Q4
a. | You are analysing data from a fitness tracker app to predict the number of calories burned

(y) based on the number of kilometres walked (x) in a day.

The data for five different users is as follows: 10
x (Kilometers|| y (Calories

Walked) Burned)
CO- 1; SO-6;
Bee | 1 [150

{2 | 250 ‘|
| 3. | 320
[ 4 | 400 |
| || 450

1. Calculate the coefficient of determination R? and the adjusted R?.

3%6
--- page 4 ---
2. Interpret the meaning of R? in this context, explaining how well the number of
kilometres walked predicts the calories burne ‘a

A company is analysing the performance of employees across two departments based on
two dependent variables: productivity and customer satisfaction. The goal is to determine

if there is a significant difference between the departments in terms of these two measures.
The data for the employees is as follows:

¢ Productivity (Dependent Variable 1):

CO-1; SO-2; o Department 1: 9, 6, 9 10
BL-4 o Department 2: 0, 2
« Customer Satisfaction (Dependent Variable 2):
o Department 1: 3, 2,7
c Department 2: 4, 0
» -
Calculate Wilks' Lambda for the given data & conclude whether there is a significant
difference in productivity and customer satisfaction between the two departments.
Q5 :
a. | A factory is performing quality control on batteries, evaluating each battery based on its
Voltage and Temperature. The goal is to determine if the battery will pass or fail quality
control based on these two measurements. The covariance matrices for the two groups
(Passed and Failed) are provided. Using Linear Discriminant Analysis (LDA), check if a
battery with Voltage = 12.5 and Temperature = 28.5°C will pass or not. °
Voltage (V) Temperature (°C) Quality Control Result
12.3 30.1 . Passed 10
[ 12.8 I 29.5 [ Passed
[ 13.0 I 27.9 ml Passed
a oral [ 12.7 I 28.7 a Passed i,
: [ 11.8 I 31.2 ie Not Passed |
12.1 33.5 Not Passed
13.3 25.0 Not Passed
The covariance matrices for Passed (C';) and Not Passed (C2) batteries are:
C. 0.145 0.180}, _ | 0.212 —().240
f-0.180 1.205 |? | 0.240 L.so4
b. | What are the key criteria used to evaluate the performance and accuracy of a linear
. : regression model?
CO- 1; SO-6; 10
BL-2

“/6
--- page 5 ---
Q6

Attributes:

e Acar has a fuel level that can be consumed by driving and refueled at a gas
station.
e A new instance of the Car class should have 50 units of fuel.

Methods:

e The class should have methods to consume fuel (drive) and gain fuel (refuel).
e drive: Decreases the fuel level by 10 units.
e refuel: Increases the fuel level by 20 units.
e get_fuel: Returns the amount of fuel left. ~

Implement this class for a car that drives once and then refuels. Show the fuel level after
each operation.

3.20
Estimate the variance of first residual for the following data, B = [-025 , where Xj, X2 are
0.35
independent & y is a dependent variable.
CO-1; SO- 1;
BL-2 Xl x2 y 10
3 5 9
6 7 10
2 6 8
5 8 11
A marketing analyst is trying to understand customer preferences based on their purchasing
behaviour. The data is collected from two groups of customers, where each group represents
a different segment.
fF
e Segment 1: {(1, 2), (2, 3), (3, 2y; (4, 5), (5, 4)} represents the first customer
CO-2; SO- 1; segment. ‘, 10
BL-5 ¢ Segment 2: {(7, 8), (8, 7), (9, 8), (10, 6), (6, 9)} represents the second customer
segment.
The analyst wants to determine a Linear Discriminant projection to differentiate between
these two customer segments based on their purchasing data. Find the discriminant vector
that separates the segments.
Q7
CO-2; SO- 1; Consider the following dataset of points in a 2D space: 10
BL-3
A(I,1), B(2,2),C(3,3),D(6,6),E(7,7),F (8,8)
Apply the k-means algorithm with k=2 clusters, Select A and F as the initial centroids.
| CO-3:; SO- I; Create a Python class named Car with the following specifications: 10
BL-2

sya
--- page 6 ---
STANDARD NORMAL TABLE (2)

Entries in the table give the area under the curve
between the mean and z standard deviations above
the mean. For example, for z = 1.25 the area under
the curve between the mean (0) and z is 0.3944.

5 2

0.00] 0.01] 0.02] 0.03[ 0.04[ 0.05| 0.06] 0.07] 0.08] 0.09
0.0 | 0.0000 0.0040 0.0080 0.0120 0.0160 0.0190. 0.02389 0.0279 0.0319 0.0359

0.1 | 0.0398 0.0438 0.0478 0.0517 0.0557 0.0596 0.0636 0.0675 0.0714 0.0753

0.2 | 0.0793 0.0832 0.0871 0.0910 0.0948 0.0987 0.1026 0.1064 0.1103 0.1141

0.3} 0.1179 0.1217 0.1255 0.1293 0.1331 0.1368 0.1406 0.1443 0.1480 0.1517
0.4 | 0.1554 0.1591 0.1628 0.1664 0.1700 0.1736 0.1772 0.1808 0.1844 0.1879

0.5) 0.1915 0.1950 0.1985 0.2019 0.2054 0.2088 0.2123 0.2157 0.2190 0.2224
0.6 | 0.2257 0:2291 0.2324 0.2357 0.2389 0.2422 0.2454 0.2486 0.2517 0.2549

0.7 | 0.2580 0.2611 0.2642 0.2673 0.2704 0.2734 0.2764 0.2794 0.2823 0.2852

0.8 | 0.2881 0.2910 0.2939 0.2969 0.2995 0.3023 0.3051 0.3078 0.3106 0.3133

0.9 | 0.3159 0.3186 0.3212 0.3238 0.3264 0.3289 0.3315 0.3340 0.3365 0.3389

1.0} 0.3413 0.3438 0.3461 0.3485 0.3508 0.3513 0.3554 0.3577 0.3529 0.3621
1.1 | 0.3643 0.3665 0.3686 0.3708 0.3729 0.3749 0.3770 0.3790 0.3810 0.3830

1.2 | 0.3849 0.3869 0.3888 0.3907 0.3925 0.3944" 0.3962 0.3980 0.3997 0.4015

1.3 | 0.4032 0.4049 0.4066 0.4082 0.4099 0.4115 0.4131 0.4147 0.4162 0.4177

1.4] 0.4192 0.4207 0.4222 0.4236 0.4251 0.4265 0.4279 0.4292 0.4306 0.4319

1.5 | 0.4332 0.4345 0.4357 0.4370 0.4382 0.4394 0.4406 0.4418 0.4429 0.4441

1.6] 0.4452 0.4463 0.4474 0.4484 0.4495 0.4505 0.4515 0.4525 0.4535 0.4545

1.7 | 0.4554 0.4564 0.4573 0.4582 0.4591 0.4599 0.4608 0.4616 0.4625 0.4633
1.8] 0.4641 0.4649 0.4656 0.4664 0.4671 0.4678 0.4686 0.4693 0.4699 0.4706

1.9] 0.4713 0.4719 0.4726 0.4732 0.4738 0.4744 0.4750 0.4756 0.4761 0.4767

2.0 | 0.4772 0.4778 0.4783 0.4788 0.4793 0.4798 0.4803 0.4808 0.4812 0.4817

2.1 | 0.4821 0.4826 0.4830 0.4834 0.4838 0.4842 0.4846 0.4850 0.4854 0.4857

2.2 | 0.4861 0.4864 0.4868 0.4871 0.4875 0.4878 0.4881 0.4884 0.4887 0.4890

2.3 | 0.4893 0.4896 0.4898 0.4901 0.4904 0.4906 0.4909 0.4911 0.4913 0.4916

2.4| 0.4918 0.4920 0.4922 0.4925 0.4927 0.4929 0.4931 0.4932 0.4934 0.4936

2.5 | 0.4938 0.4940 0.4941 0.4943 0.4945 0.4946 0.4948 0.4949 0.4951 0.4952

2.6 | 0.4953 0.4955 0.4956 0.4957 0.4959 0.4960 0.4961 0.4962 0.4963 0.4964
2.7 | 0.4965 0.4966 0.4967 0.4968 0.4969 0.4970 0.4971 0.4972 0.4973 0.4974
2.8 | 0.4974 0.4975 0.4976 0.4977 0.4977 0.4978 0.4979 0.4979 0.4980 0.4981

2.9 | 0.4981 0.4982 0.4982 0.4983 0.4984 0.4984 0.4985 0.4985 0.4986 0.4986

3.0 | 0.4987 0.4987 0.4987 0.4988 0.4988 0.4989 0.4989 0.4989 0.4990 0.4990

3.1 | 0.4990 0.4991 0.4991 0.4991 0.4992 0.4992 0.4992 0.4992 0.4993 0.4993
3.2 | 0.4993 0.4993 0.4994 0.4994 0.4994 0.4994 0.4994 0.4995 0.4995 0.4995

3.3 | 0.4995 0.4995 0.4995 0.4996 0.4996 0.4996 0.4996 0.4996 0.4996 0.4997
3.4 | 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4998

6
````

## 2024-25 · Re-Exam · Sem 3 · paper c4ea11970b2c

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSBS/SEM-III/COMPUTATIONAL STATISTICS/Computational Statistics, Sem-II, Batch 2022-23 & 2024-25 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 /2/ 24
- Text: ocr (8 pages), mean OCR confidence 87.3
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025

Program: B Tech Stream : CSBS Year: II Semester: III

Subject: Computational Statistics Time: 3 hrs ( 10: 0panfo £.:00Pry )
Date: 29 /2/ 24~ No. of Pages:6

Marks:100

Re Examination (2024-2025) /Re Exam 22-23,23-24
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory. ~
2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

Ql
a. | Define the assumptions of homoscedasticity and normality in the context of linear
regression. How do these assumptions affect the results of the regression analysis?
Also interpret the following charts for Homoscedasticity & Heteroscedasticity;
i. ii.
CO-1; SO- 1;
BL-1 = Sy
q z
QQ a0
x ° x
b. | A marketing manager conducted factor analysis on survey data related to customer
preferences, with 10 variables representing different product features. The rotated factor
loadings from the analysis are given below:
Feature Factor 1 Factor 2 Factor 3
CO- 1; SO- 1; =
BL-4 Feature X 0.82 0.12 0.05
Feature Y 0.78 0.08 0.15
Feature Z 0.72 0.20 0:25
Feature W 0.10 0.85 0.05

1%
--- page 2 ---
Feature V 0.15 0.80 0.10

Feature U 0.05 O75 0.20
Feature T 0.30 0.10 0.88
Feature S 0.10 O15 0.80
Feature R 0.20 0.05 0.70
Feature Q 0.25 0.25 0.65

Using the rotated factor loadings, answer the following questions:

e Which product features are most strongly associated with each of the three
identified factors?

e Based on the factor loadings, how might these factors represent distinct customer
preferences or product characteristics?

- CO-2; SO-2; | c. | In what situations would you prefer factor analysis over PCA, and vice versa? 5
BL-4
d. | Write a Python program to check if each string in the given list of fruits is longer than 5
characters. If it is, store "long" as the value; otherwise, store "short" as the value in a dictionary.
CO-3; SO-1; : P F " non nn WM eran on " 5
BL-5 Given list of strings: ["apple", "banana", "cherry", "kiwi", "grape"]
Q2
a | Let Z~ N3(y, XD), where:
Zy 3 Re ao)
23 5 (2B. 3}
CO: 1; SO-2; Which of the following random variables are independent? a
BL-3 ee
© (2,22) & 23
© 24 &24+ 23
Also, find the distribution of 4z,; — 2z3 + 25.
b. | Conduct principal component analysis (PCA) on the following dataset with 6 observations
and 2 features. Report the total sample variance explained by each of the principal
components:
CO- 2; SO-6; 10
BL-3

15 20 25 30 10 18
12) 14 13> 16e aH to

“6
--- page 3 ---
Q3

a. | A school is examining the academic performance of students in three subjects:
Mathematics, Science, and English. The scores for these subjects are modeled as a
multivariate normal distribution:

4 D0
Z~N3(u,5), p= }6l, D=|1 5 3
CO-1; SO-1; 5 0 3 4 Abie
BL-3

1. What is the probability that a student's score in Mathematics exceeds 5?

2. Ifa student's score in Science is 7 and in English is 3, what is the conditional
probability that their score in Mathematics is greater than 5?

3. Determine the probability that three times a student's score in Mathematics, plus two
times their score in Science, minus their score in English, is less than 45.

b. | Apply Complete Linkage Agglomerative Hierarchical Clustering to the following dataset:

3.5
97
4 6
Zz 2
5
CO- 2; SO-6; : 8 : 10
BL-3
Explain the systematic process for applying Complete Linkage clustering, including the
initial state and the merging criteria employed.
1. Identify the resulting clusters after conducting the clustering analysis.
2. Draw the dendrogram to represent the clustering process and demonstrate the
hierarchy of the clusters created.
Q4
a. | A company is analysing the return on investment (ROI) from their marketing campaigns.
The ROI (y) is based on the advertising budget (x) spent on digital platforms in thousands
of dollars. The data collected over five campaigns is as follows: 10
x(Ad Spend in $1000s) y (ROI in $1000s)
CO- 1; SO-6; e 2 I, 10 |
BL-2
| a IL 15 |
| 6 | 20 |
| 8 IL 23 |
| 10 [ 28

1. Calculate R* and adjusted R?.

¥6
--- page 4 ---
2. Discuss what the R? value tells you about how well the advertising budget predicts
ROI from marketing campaigns.

the

CO-1; SO-2;

Researchers are evaluating the effectiveness of two different treatments for a medical

condition, based on two dependent variables: recovery time (in days) and quality of life
score (on a scale of 1 to 10). They want to see if there is a significant difference between

the two treatments for both variables. The data is as follows:

e Recovery Time (Dependent Variable 1):
o Treatment 1: 10, 12,9

10

BL-4 o Treatment 2: 15, 13
¢ Quality of Life Score (Dependent Variable 2):
o Treatment 1: 7, 8, 6
o Treatment 2: 4,5
Calculate Wilks' Lambda using the provided data & draw conclusion about the
effectiveness of the treatments based on Wilks' Lambda.
Q5
A manufacturer is performing quality control on medical devices by measuring their
Pressure and Flow Rate. The objective is to determine if the devices are calibrated or not
calibrated based on these two measurements. The covariance matrices for the two groups
(Calibrated and Not Calibrated) are provided. Using Linear Discriminant Analysis (LDA),
check if a device with Pressure = 5.5 and Flow Rate = 18.0 is calibrated or not.
Preseuee (psi) Flow Rate Calibration
P (L/min) Status 10
[ 5.3 | 17.5 | Calibrated |
Ded) 18.4 Calibrated
CO- 1; SO-6; B 5.8 ll 17.2 || Calibrated |
ae [ 6.1 | 16.9 [Calibrated |
4.8 19.5 Not Calibrated
| 4.9 | 20.1 __|[ Not Calibrated _|
[ 5.4 | 15.8 || Not Calibrated |
The covariance matrices for Calibrated (C1) and Not Calibrated (C2) devices are:
Cs 0.120 -0.150 a 0.210   ~0.180
ee PAOCTS OE 10508 ee NRs0 ee 720
CO-2: SO-1: Discuss the relationship between Linear discriminant Analysis (LDA), Principal
BL-4 i Component Analysis (PCA) , Factor Analysis (FA) and multiple regression. How are they | 10
similar and different? :
Q6
_ [azo
CO-1; SO- 1; Estimate‘the variance of first fitted value for the following data, 8 = }—0.25], where xi, 10
BL-2 0.35

x2 are independent & y is dependent variable.

VE
--- page 5 ---
XI x2 y

3 5 9
6 Zi ~ 10
2 6 8
5) 8 1]

A biologist is studying the traits of two species of plants based on their height and leaf
length. The measurements for each species are recorded as follows:

CO-2; SO- 1; ° Species A: {(5, 1), (4, 2), (6, 3), (7, 2), (8, 4)} 10
BL-5 ¢ Species B: {(10, 12), (11, 9), (9, 11), (10, 10), (8, 12)}
The biologist wants to calculate the Linear Discriminant vector to distinguish between
the two species. Use the given data to find the discriminant vector.
Q7
CO-2; SO- 1; Consider the following dataset of points in a 2D space: 10
BL-3
P(2,1), Q(3,2),R(4,3),S(7,6),T(8,7),U(9,8)
Apply the k-means algorithm with k=2 clusters, Select P and T as the initial centroids.
CO-3; SO- 1; Create a Python class named Phone with the following specifications: 10
BL-2

Attributes:

e A phone has a battery level that decreases with usage and increases when charged.
e A new instance of the Phone class should start with 100% battery. i

Methods:

¢ The class should have methods to consume battery (use_phone) and gain battery
(charge_phone).

e _use_phone: Decreases the battery level by 20%.

e charge_phone: Increases the battery level by 30%.

¢   get_battery: Returns the current battery level.

Implement this class for a phone that is used twice and then charged once. Display the
battery level after each operation.

Vo
--- page 6 ---

--- page 7 ---
STANDARD NORMAL TABLE (Z)

Entries in the table give the area under the curve
between the mean and z standard deviations above
the mean. For example, for z= 1.25 the area under
the curve between the mean (0) and z is 0.3944.

0.00| 0.01| 0.02| 0.03] 0.04| 0.05] 0.06] 0.07| 0.08] 0.09
0.0 | 0.0000 0.0040 0.0080 0.0120 0.0160 0.0190 0.0239 0.0279 0.0319 0.0359
0.1 | 0.0398 0.0438 0.0478 0.0517 0.0557 0.0596 0.0636 0.0675 0.0714 0.0753
0.2 | 0.0793 0.0832 0.0871 0.0910 0.0948 0.0987 0.1026 0.1064 0.1103 0.1141
0.3 | 0.1179 0.1217 0.1255 0.1293 0.1331 0.1368 0.1406 0.1443 0.1480 0.1517
0.4 | 0.1554 0.1591 0.1628 0.1664 0.1700 0.1736 0.1772 0.1808 0.1844 0.1879
0.5 | 0.1915 0.1950 0.1985 0.2019 0.2054 0.2088 0.2123 0.2157 0.2190 0.2224
0.6 | 0.2257 0.2291 0.2324 0.2357 0.2389 0.2422 0.2454 0.2486 0.2517 0.2549
0.7 | 0.2580 0.2611 0.2642 0.2673 0.2704 0.2734 0.2764 0.2794 0.2823 0.2852
0.8 | 0.2881 0.2910 0.29389 0.2969 0.2995 0.3023 0.3051 0.3078 0.3106 0.3133
0.9 | 0.3159 0.3186 0.8212 0.3238 0.3264 0.3289 0.3315 0.3340 0.3365 0.3389
1.0 | 0.3413 0.3438 0.3461 0.3485 0.3508 0.3513 0.3554 0.3577 0.3529 0.3621
1.1 | 0.3643 0.3665 0.3686 0.3708 0.3729 0.3749 0.3770 0.3790 0.3810 0.3830
1.2 | 0.3849 0.3869 0.3888 0.3907 0.3925 0.3944 0.3962 0.3980 0.3997 0.4015
1.3 | 0.4032 0.4049 0.4066 0.4082 0.4099 0.4115 0.4131 0.4147 0.4162 0.4177
1.4 | 0.4192 0.4207 0.4222 0.4236 0.4251 0.4265 0.4279 0.4292 0.4306 0.4319
1.5 | 0.4332 0.4345 0.4357 0.4370 0.4382 0.4394 0.4406 0.4418 0.4429 0.4441
1.6 | 0.4452 0.4463 0.4474 0.4484 0.4495 0.4505 0.4515 0.4525 0.4535 0.4545
1.7 | 0.4554 0.4564 0.4573 0.4582 0.4591 0.4599 0.4608 0.4616 0.4625 0.4633
1.8] 0.4641 0.4649 0.4656 0.4664 0.4671 0.4678 0.4686 0.4693 0.4699 0.4706
1.9} 0.4713 0.4719 0.4726 0.4732 0.4738 0.4744 0.4750 0.4756 0.4761 0.4767
2.0 | 0.4772 0.4778 0.4783 0.4788 0.4793 0.4798 0.4803 0.4808 0.4812 0.4817
2.1 | 0.4821 0.4826 0.4830 0.4834 0.4838 0.4842 0.4846 0.4850 0.4854 0.4857
2.2 | 0.4861 0.4864 0.4868 0.4871 0.4875 0.4878 0.4881 0.4884 0.4887 0.4890
2.3 | 0.4893 0.4896 0.4898 0.4901 0.4904 0.4906 0.4909 0.491 1 0.4913 0.4916
2.4| 0.4918 0.4920 0.4922 0.4925 0.4927 0.4929 0.4931 0.4932 0.4934 0.4936
2.5 | 0.4938 0.4940 0.4941 0.4943 0.4945 0.4946 0.4948 0.4949 0.4951 0.4952
2.6 | 0.4953 0.4955 0.4956 0.4957 0.4959 0.4960 0.4961 0.4962 0.4963 90.4964
2.7 | 0.4965 0.4966 0.4967 0.4968 0.4969 0.4970 0.4971 0.4972 0.4973 0.4974
2.8 | 0.4974 0.4975 0.4976 0.4977 0.4977 0.4978 0.4979 0.4979 0.4980 0.4981
2.9 | 0.4981 0.4982 0.4982 0.4983 0.4984 0.4984 0.4985 0.4985 0.4986 0.4986
3.0 | 0.4987 0.4987 0.4987 0.4988 0.4988 0.4989 0.4989 0.4989 0.4990 0.4990
3.1] 0.4990 0.4991 0.4991 0.4991 0.4992 0.4992 0.4992 0.4992 0.4993 0.4993
3.2 | 0.4993 0.4993 0.4994 0.4994 0.4994 0.4994 0.4994 0.4995 0.4995 0.4995
3.3 | 0.4995 0.4995 0.4995 0.4996 0.4996 0.4996 0.4996 0.4996 0.4996 0.4997
3.4 | 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4998

6/6
--- page 8 ---

````

## 2023-24 · Final + Re-Exam · Sem 3 · paper 539df07347ee

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSBS/SEM-III/COMPUTATIONAL STATISTICS/Computational Statistics, Sem-III, Final Exam & Re Exam 2022-23, A Y 20223-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04/12/2023
- Text: ocr (5 pages), mean OCR confidence 85.7

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGIN
Academic Year: 2023-2024 }

Program: B tech Year: II Semester: III

Stream: CSBS *

Subject: Computational Statistics Time: 3 hrs (+0.00 am to 1.00 pm)
Date:04/12/2023 No. of Pages:5

Marks:100

Final Examination/Re-Examination (2022-23)
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
_()_7) Assume Suitable data if necessary.

Ql
a. | Explain the following assumptions of Linear regression model:
e Linearity
CO-1; SO- 1; e Homoscedasticity

BL-I e Independence 5
e Normality
¢ Miulticollinearity

b. | Following is the regression output based on the data to predict driving speed using no. of
occupants & whether wearing seat belt or not:

SUMMARY OUTPUT
Regression Statistics

Multiple R 0.561415721
R Square 0.315187612 “
Adjusted R Square —_0.190676268

> Standard Error 5.464881981
Observations ‘ 14
ANOVA

df ss MS EF Significance F
Regression 2 151.2 75.6 2531396765   0.124636098
. . Residual 11 328.5142857 29.86493506
CO- 1; SO- 1; Total 13 479.7142857 5
BL-4
Coefficients Standard Error __¢ Stat P-value Lower 95% Upper 95%

Intercept 67.62857143 —5.017157945 13.47945833 3.49148E-08   56.58588125 78.6712616
Occupnts -3.214285714   2.190826718 -1.467156525 0.17033373 -8.036262805 _1.607691377
SeatBelt 6.628571429 _3.199907234_-2.071488622_0.062611837__-13.67151976. _0.414376903

i. State the regression equation.
ii. | How much data does the model explain?
iii. State the null and alternate hypothesis for ANOVA and conclude what is accepted
at 5% Level of significance.
iv. Which of the independent variables are significant at 5% Level of significance?
v. Predict driving speed if occupants= 3 & seatbelt=0.
--- page 2 ---
c. | Human resources manager wants to identify the underlying factors that explain the 12
variables that the human resources department measures for each applicant. Following is
the outcome of factor analysis performed on the data. Analyze the following rotated factor
loadings ‘i
Rotated Factor Loadings and Coamunalities eee
Varimax Rotation
Variable Factor! Facter? Factor? Factord Conmunality
Academic record 8.481 8.518 8.086 0.188 0.534
CO-2; SO-2; Appearance o.140 0.738 0.319 0.175 (0.685 5
BL-4 copes ie sar swiss oss ocuee ast
Experience 0.472 0.395 -0.112 e402 0.553
Job Fit 0.844 0.209 6.305 @.215 2.895
Letter o.219 0.052 @.217 0.947 0.998
Likeability 0.261 0.615 0.321 0.208 0.593
Organization 0.217 0.285 8.889 0.086 0.926
Potential 8.645 8.492 0.121 8.2e2 8.714
nesune o.2i8 0.365 0.113 0.789.824
Self-Confidence 0.239 0.743 8.249 8.892 0.679
Variance 2.5153 2.4880 «2.0863 1.9594 9.e491
% Var 8.210 8.207 0.174 @.163 0.754
d. | Write a Python code to create a list of strings based on a given list of numbers according
to the following rules: oN
CO-3: $0-1 e Ifthe number is a multiple of five and odd, the string should be 'five odd’.
BL 5 _ e Ifthe number is a multiple of five and even, the string should be 'five even’. 5
e Ifthe number is odd, the string should be 'odd'.
e Ifthe number is even, the string should be 'even'.
e Given list of numbers: numbers = [1, 3, 4, 6, 81, 80, 100, 95]
Q2
a. 41 3 4 1 2
X~N3(u, 2), where X=|%2],u=]2],y=]1 9 1
hich x3 1 2 1 4
Which of the following random variables are independent?
CO- 1; SO-2; . 7 8 P
BL3 i. x1 & X3 10
ii. (X1,X3) & x2
iii. X1 & 2x1+x2+X3
iv. Find the distribution of 3x1+2x2-x3 *
>
b. | Apply the principal component analysis to the following data with 6 observations &
2 features. State the total sample variance explained by each of the principal components:
CO- 2; SO-6; 10
BL-3 [2 5 7 10 9 6
10 9 8 11 6 7
Q3
a. xy 5 4 -1 0
X~N3(p, 2), where X=|*%2], w=13],y=]-1 4 2
‘ 5 X3 7 0 2 9
ee Find the following probabilities 10

1. P(x1>8)
2. P(x1>8] x2=1,x3=10)
3. P(4x1-3x2+5x3<63)
--- page 3 ---
b. | Apply Single Linkage Agglomerative Hierarchical clustering to the givén dataset to form
clusters. Describe the systematic process, including the initial state, the merging criteria.
and the resulting clusters. Also, draw the dendrogram.

¥

X Y
CO- 2; 80-6; P1 0.40 0.53
BL-3 P2 0.22 0.38 10
. P3 0.35 0.32
P4 0.26 0.19
P5 0.08 0.41
P6 0.45 0.30
Q4
a. | Regression equation for the following data is y=1.6x+8, find R? & adjusted R*. Also, 10
interpret the meaning of R?.
r y
x y
CO- 1; SO-6; (independent variable) (dependent variable)
BL-2 1 9
2 12
3 13
4 14
P) 16
b. | State the hypothesis for one-way MANOVA. Obtain Wilk’s lambda for the following data
and conclude.
Samples with respect to dependent variable 1. |
CO-1; SO-2; Population 1: 9,6,9 | 10
BL-4 Population 2: 0,2
Samples with respect to dependent variable 2.
Population 1: 3,2,7
Population 2: 4,0
@™ Q5 ;
a. | Regression equation for the following data is y=1.6x+8, find the confidence interval for
single value of y at x=6, (Take Level of significance o=5%, ta2,3=3.182) 10
CO- 1; SO-6; x Y
BL-2 (independent variable) (dependent variable)
1 9
2 12
3 13
4 14
5 16
--- page 4 ---
b. | For the following quality control data, the covariance matrices C1 & C2 are as given below.
Using Linear Discriminant analysis, Check if the product with curvature =4, Diameter =3
is passed or not?

Curvature Diameter Quality control ‘
Result:
2.95 6.63 Passed: *
2.53 7.79 Passed
CO-2; SO-1;
3.57 5.65 Passed 10
BL-4
3.16 5.47 Passed
2.58 4.46 Not Passed
2.16 6.22 Not Passed
3.27 3.52 Not Passed
_ 70.166 —0.192 _ 70.259 —0.286
cl= ease 1.349 | » C2 = [cores 2.142 |
Q6
a. . _ [2.55
Estimate the variance of f for the following data, B = Fea , where x1, X2 are |S
-L 0.18
independent & y is dependent variable.
CO-1; SO- 1; XI X2 y 10
BL-2 2 1 4
4 4 2
1 2 3
1 0 1
b. | Compute the Linear Discriminant projection for the following 2-dimensional data:
CO-2; SO- 1; 10
BL-5 Sample for class! {(4,2),(2,4,(2,3),(3,6),(4,4)}
Sample for class2 {(9,10),(6,8),(9,5),(8,7),(10,8)}
Q7
CO-2; SO- 1; | a. | Apply the k-means algorithm to the given dataset: 10
BL-3 AL, 2), B(2, 3), CQ, 5), D3, 2), E(S, 8), F(6, 7), G(8, 3), HY, 2). *
Begin with k=2 and choose initial centroids at A(, 2) and G(8, 3). —_
CO-3; SO- 1; | b. | Define a pyttion class named Calculator with a constructor to initialize two variables and a | -J
BL-2 function to calculate the sum and product of these variables. Implement this class for the

values 5 and 6.
--- page 5 ---
STANDARD NORMAL TABLE (2)

Entries in the table give the area under the curve
between the mean and z standard deviations above
the mean. For example, for z = 1.25 the area under
the curve between the mean (0) and z is 0.3944.

ze 0.00[ 0.01| 0.02] 0.03] 0.04| 0.05| 0.06| 0.07| 0.08| 0.09
0. 0.0000 0.0040 0.0080 0.0120 0.0160 0.0190 0.0239 0.0279 0.0319 0.0359
0.1 | 0.0398 0.0438 0.0478 0.0517 0.0557 0.0596 0.0636 0.0675 0.0714 0.0753
0.2 | 0.0793 0.0832 0.0871 0.0910 0.0948 0.0987 0.1026 0.1064 0.1103 0.1141
0.3} 0.1179 0.1217 0.1255 0.1293 0.1331 0.1368 0.1406 0.1443 0.1480 0.1517
0.4! 0.1554 0.1591 0.1628 0.1664 0.1700 0.1736 0.1772 0.1808 0.1844 0.1879
0.5 | 0.1915 0.1950 0.1985 0.2019 0.2054 0.2088 0.2123 0.2157 0.2190 0.2224
0.6 | 0.2257 0.2291 0.2324 0.2357 0.2389 0.2422 0.2454 0.2486 0.2517 0.2549
0.7 | 0.2580 0.2611 0.2642 0.2673 0.2704 0.2734 0.2764 0.2794 0.2823 0.2852
0.8 | 0.2881 0.2910 0.2939 0.2969 0.2995 0.3023 0.3051 .0.3078 0.3106 0.3133
0.9 | 0.3159 0.3186 0.3212 0.3238 0.3264 0.3289 0.3315 0.3340 0.3365 0.3389
1.0] 0.3413 0.3438 0.3461 0.3485 0.3508 0.3513 0.3554 0.3577 0.3529 0.3621
1.1 | 0.3643 0.3665 0.3686 0.3708 0.3729 0.3749 0.3770 0.3790 0.3810 0.3830
1.2 | 0.3849 0.3869 0.3888 0.3907 0.3925 0.3944 0.3962 0.3980 0.3997 0.4015
1.3 | 0.4032 0.4049 0.4066 0.4082 0.4099 0.4115 0.4131 0.4147 0.4162 0.4177
1.4] 0.4192 0.4207 0.4222 0.4236 0.4251 0.4265 0.4279 0.4292 0.4306 0.4319
1.5] 0.4332 0.4345 0.4357 0.4370 0.4382 0.4394 0.4406 0.4418 0.4429 0.4441
1.6 | 0.4452 0.4463 0.4474. 0.4484 0.4495 0.4505 0.4515 0.4525 0.4535 0.4545
1.7 | 0.4554 0.4564 0.4573 0.4582 0.4591 0.4599 0.4608 0.4616 0.4625 0.4633
1.8 | 0.4641 0.4649 0.4656 0.4664 0.4671 0.4678 0.4686 0.4693 0.4699 0.4706
1.9| 0.4713 0.4719 0.4726 0.4732 0.4738 0.4744 0.4750 0.4756 0.4761 0.4767
2.0 | 0.4772 0.4778 0.4783 0.4788 0.4793 0.4798 0.4803 0.4808 0.4812 0.4817
2.1 | 0.4821 0.4826 0.4830 0.4834 0.4838 0.4842 0.4846 0.4850 0.4854 0.4857
2.2 | 0.4861 0.4864 0.4868 0.4871 0.4875 0.4878 0.4881 0.4884. 0.4887 0.4890
2.3 | 0.4893 0.4896 0.4898 0.4901 0.4904 0.4906 0.4909 0.4911 0.4913 0.4916
2.4| 0.4918 0.4920 0.4922 0.4925 0.4927 0.4929 0.4931 0.4932 0.4934 0.4936
2.5 | 0.4938 0.4940 0.4941 0.4943 0.4945 0.4946 0.4948 0.4949 0.4951 0.4952
2.6 | 0.4953 0.4955 0.4956 0.4957 0.4959 0.4960 0.4961 0.4962 0.4963 0.4964
2.7 | 0.4965 0.4966 0.4967 0.4968 0.4969 0.4970 0.4971 0.4972 0.4973 0.4974
2.8 | 0.4974 0.4975 0.4976 0.4977 0.4977 0.4978 0.4979 0.4979 0.4980 0.4981
2.9 | 0.4981 0.4982 0.4982 0.4983 0.4984 0.4984 0.4985 0.4985 0.4986 0.4986
3.0 | 0.4987 0.4987 0.4987 0.4988 0.4988 0.4989 0.4989 0.4989 0.4990 0.4990
3.1} 0.4990 0.4991 0.4991 0.4991 0.4992 0.4992 0.4992 0.4992 0.4993 0.4993
3.2 | 0.4993 0.4993 0.4994 0.4994 0.4994 0.4994 0.4994 0.4995 0.4995 0.4995

3.3 | 0.4995 0.4995 0.4995 0.4996 0.4996 0.4996 0.4996 0.4996 0.4996 0.4997

3.4 | 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4997 0.4998
````

## 2023-24 · Re-Exam · Sem 3 · paper a262e346aa13

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSBS/SEM-III/COMPUTATIONAL STATISTICS/Computational Statistics, Sem-III, Batch 2023-24, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 86.5

````text
Me

, “
- (4/orJ2g = loren ra Me.
SVKM? S NMIMS \ ,

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024

Program: B.tech Year: II Semester: II}

Stream: CSBS 45

Subject: Computational Statistics Time: 3 hrs (10.60 am to 1.00 pm)
Date: 44] 02 }2024 No. of Pages:5

Marks:100

Re-Examination (2022-23) | 202.8- 24-
Instructions: Candidates ‘should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
© 7) Assume Suitable data if necessary.

Ql
a.
CO-1; SO- 1; ‘ . . .
BL-1 State any 5 assumptions of Multiple Linear regression model. 5
b. | Following is the regression output based on the data to sales using unit price & promotion:
SUMMARY OUTPUT
Regression Statistics
Multiple R 0.97012
R Square 0.941133
Adjusted R Squa 0.926416
Standard Error 515.7254 ‘
(Observations ii
> .
|ANOVA
of SS MS F Significance F
. Regression 2 34017672.79 17008836 63.94955 1.20086E-05
CO- 1; SO- 1; Residual 8 2127781.758 265972.7 5
BL-4 [Total 10 36145454.55

CoefficientsStandard Error _t Stat P-value _ Lower 95% Upper 95% Lower 95.0% Upper 95.0%

intercept 1642.04 1151.801633 -1.42563 0.191804 -4298.10333 1014.015 -4298.1033 1014.01533
Unit Price 9.909374 0.876228512 11.30912 3.36E-06 7.888787251 11.92996 7.88878725 11.9299604
Promotion 8.133162 2.624163278 3.099335 0.014681 2.081830676 14.18449 2.08183068 14.1844934

i. State the regression equation.
on ii. How much data does the model explain?
ili. State the null and alternate hypothesis for ANOVA and conclude what is accepted
at 5% Level of significance.
iv. Which of the independent variables are significant at 5% Level of significance.
v. Predict sales if Unit price= 10 & Promotion=4.
--- page 2 ---
c. | What is Factor analysis?
Following is the outcome of factor analysis performed on the data based on student
participants. Analyze the following rotated factor loadings
Variables
Factors I u md
Vertical jump height Bal -01
CO-2; SO-2; 40-yard (36-meter) dash time ~76 -01 5
BL-4 Standing triple jump distance 7 01
12-minute run distance -.02 77
2-kilometer (1.25-mile) rowing time 7 01 -.70
20-minute cycle distance 01 74
Fast-twitch muscle fiber type percentage & -.34
Body fat percentage “320-34
d. | Write a Python code to find the sum of only the numeric values in a given dictionary.
Consider the dictionary magic_dict, and for each value in the dictionary:
a “1; e Ifthe value is numeric (integer or float), include it in the sum. 59
e Ifthe value is of any other type, exclude it from the sum.
e Given dictionary: magic_dict = dict(vall=44, val2="secret value", val3=55.0, val4=1)
Q2
a. M7. 27 111
X~N3(u,)) , where X=]%2),u“=|-3),0=]1 3 2
Which of the foll va iabl depend
F , : : 7
CO- 1; $0-2: . of t _ . ovine random variables are independent? 7
BL-3 ii, (Xx3) & XD
iii. X1 & X1+X2+X3
iv. Find the distribution of 3x1+2x2+4x3
b. | Apply the principal component analysis to the following data with 6 observations & 2
features .State the total sample variance explained by each of the principal components:
CO- 2; SO-6; 10
BL-3 19 22 6 3 2 | ‘
12 6 9 15 13 5 ;
Q3
a. [%1 51 3 -1 1
XAN3(u.¥), where X=1%2!, w = 3} Y=i-1 + Of.
lx 7 1 0 2
CO-1; SO-1; Find the following probabilities 10
BL-3 1. P(x1>6)
2. P(x1>3.5|x2=0,x3=1)
3. P(x2+ 2x3>4)
b. | Utilize Single Linkage Agglomerative Hierarchical clustering methodology on the provided
CO- 2; SO-6; dataset, outlining the sequential stages involved in the clustering process. Also draw a 10
BL-3 Dendogram.

A (1, 1), BG, 3), CG, 5), D(4.5), E(6,6), and F(7,5)
--- page 3 ---
Fi

Q4

a. | Regression equation for the following data is y=1.6x+6, find R? & adjusted Ri. Also,

interpret the meaning of R?. 10
43
x y
(independent | (dependent
CO- 1; SO-6; variable) variable)
BL-2 rl 7
2 10
3 u
4 12
5 14
b. .
State the hypothesis for one-way MANOVA. Obtain wilk’s lambda for the following data
and conclude.
@ Teaching Method A:
CO-1; SO-2; Population 1: 9,6 10
BL-4 Population 2: 0,2,3
Teaching Method B:
Population 1: 3,2
Population 2: 4,0,7
Q5
a. | Regression equation for the following data is y=1.6x+6, find the confidence interval for
average value of y at x=6. (Take Level of significance a=5%, ta23=3.182)
10
x Y
(independent variable) (dependent variable)
CO- 1; SO-6; l i
( BL-2 2 10
3 11.
4 12
5 14
b.
For the following students performance data, the covariance matrices C1 & C2 are as
given below. Using Linear Discriminant analysis, Check if the student with study time =5
hours, time spent on social media =8 hours is succesful or not?
CO-2; SO-1; 10

BL-4
--- page 4 ---
Study time Time spent on Exam Result

(in hours) social media(in
hours) j
2.95: 6.63 Successful
2.53 7.79 Successful
3.57 5.65 Successful
3.16 5.47 Successful
2.58 4.46 Not Successful
2.16 - | 6.22 Not Successful
3.27 3:52 Not Successful
_ 70.166 —0.192 _ 0.259 —0.286
cl= —0.192 1.349 sabes [ozes 2.142
Q6
a. _ _ . . 4.75
Estimate the variance of y1 and e1 for the following data, where 6 =| 1 |: ;
-1.25 »
xl x2 y
CO-1; SO- 1; py) | 5 10
BL-2 1 3 3
2. 3 8 -
p 1 6
where x1,x2 are independent & y is a dependent variable.
b. | Compute the Linear Discriminant projection for the following 2-dimensional data:
CO-2; SO- 1; 10
BL-5 Sample for class1 {(1,2),(2,4,(1,3),(3,6),(2.4)}
Sample for class2 {(1,3),(6,8),(1,5),(8.7),(5,8)}
Q7
CO-2; SO- 1; | a. | Apply the k-means algorithm to the provided dataset: : 10
BL-3 P(2, 5), QB, 4), RG, 6), S(4, 8). T(6, 7), U(8, 3), V1, 6), wue. 8). >)
Start with k=3 and choose initial centroids P,U & V.
CO-3; SO- 1; | b. | Create a Python class named Dog with the following specifications: 10
BL-2

Attributes:

© Dogs have an energy level that can be consumed by barking and gained by sleeping.

e A fresh instance of the Dog class should have 10 units of energy.
Methods:

e Theclass should have methods to consume energy (bark) and gain energy (sleep).
e bark: Decreases the energy level by 5 units.

e sleep: Increases the energy level by 7 units.

e Doghas a method get_energy which returns the amount of energy left
--- page 5 ---
STANDARD NORMAL TABLE (Z)

Entries in the table give the area under the curve
between the mean and z standard deviations above
the mean. For example, for z = 1.25 the-area under
the curve between the mean (0) and z is 0.3944,

0.00] 0.01] 0.02| 0.03] 0.04] 0.05| 0.06] 007 | 0.08] 0.09
0.0 | 0.0000. 0.0040 0.0080 0.0120 0.0160 0.0190 -0.0239 0.0279 0.0319 0.0359
0.1} 0.0398 0.0438 0.0478 0.0517 0.0557 0.0596 0.0636 0.0675 0.0714 0.0753
0.2 | 0.0793 0.0832 0.0871 0.0910 0.0948 0.0987 0.1026 0.1064 0.1103 0.1141
0.3 | 0.1179 0.1217 0.1255 0.1293 0.1331 0.1368 0.1406 0.1443 0.1480 0.1517
0.4 | 0.1554 0.1591 0.1628 0.1664 0.1700 0.1736 0.1772 0.1808 0.1844 0.1879
0.5 | 0.1915. 0.1950 0.1985 0.2019 0.2054 0.2088 0.2123 0.2157 0.2190 0.2204
0.6 | 0.2257 0.2291 0.2324 0.2357 0.2389 0.2422 0.2454 0.2486 0.2517 0.2549

G.7 | 0.2580 0.2611 0.2642, 0.2673 0.2704 0.2734 0.2764 0.2784 0.2823 0.2852
0.8 | 0.2881 0.2910 0.2939 0.2969 0.2995 0.3023 0.3051 0.3078 0.3106 0.3133

0.9 | 0.3159 0.3186 0.3212 0.3238 0.3264 0.3289 0.3315 0.3340 0.3365 0.3389

1.0] 0.3413 0.3438 0.3461 0.3485 0.3508 0.3513 0.3554 0.3577 0.3529 0.3621
1.1 | 0.3643 0.3665 0.3686 0.3708 0.3729 0.3749 0.3770 0.3790 0.3810 0.3830

1.2] 0.3849 0.3869 0.3888 0.3907 0.3925 0.3944 0.3962 0.3980 0.3997 0.4015
1.3 | 0.4032 0.4049 0.4066 0.4082 0.4099 0.4115 0.4131 0.4147 0.4162 0.4177

1.4 | 0.4192 0.4207 0.4222 0.4236 0.4251 0.4265 0.4279 0.4292 0.4306 0.4319

1.5] 0.4332 0.4345 0.4357 0.4370 0.4382 0.4394 0.4406 0.4418 0.4429 0.4441
1.6 | 0.4452 0.4463 0.4474 0.4484 0.4495 0.4505 0.4515 0.4525 0.4535 0.4545

1.7} 0.4554 0.4564 0.4573 0.4582 0.4591 0.4599 0.4608 0.4616 0.4625 0.4633

1.8 | 0.4641 0.4649 0.4656 0.4664 0.4671 0.4678 0.4686 0.4693 0.4699 0.4706
1.9} 0.4713 0.4719 0.4726 0.4732 0.4738 0.4744 0.4750 0.4756 0.4761 0.4767

2.0 | 0.4772 0.4778 0.4783 0.4788 0.4793 0.4798 0.4803 0.4808 0.4812 0.4817
2.1 | 0.4821 0.4826 0.4830 0.4834 0.4838 0.4842 0.4846 0.4850 0.4854 0.4857

2.2 | 0.4861 0.4864 0.4868 0.4871 0.4875 0.4878 0.4881 0.4884 9.4887 0.4890

2.3 | 0.4893 0.4896 0.4898 0.4901 0.4904 0.4906 0.4909 0.4911 0.4913 0.4916
2.4 | 0.4918 0.4920 0.4922 0.4925 0.4927 0.4929 0.4931 0.4932 0.4934 0.4936

2.5 | 0.4938 0.4940 0.4941 0.4943 0.4945 0.4946 0.4948 . 0.4949 0.4951 0.4952

2.6 | 0.4953 0.4955 0.4956 0.4957 0.4959 0.4960 0.4961 0.4962 0.4963 0.4964
2.7 | 0.4965 0.4966 0.4967 0.4968 0.4968 0.4970 0.4971 0.4972 0.4973 0.4974

2.8 | 0.4974 0.4975 0.4976 0.4977 0.4977 0.4978 0.4979 0.4979 0.4980 0.4981
2.9 | 0.4981 0.4982 0.4982 0.4983 0.4984 0.4984 0.4985 0.4985 0.4986 0.4986

3.0 | 0.4987 0.4987 0.4987 0.4988 0.4988 0.4989 0.4989 0.4989 0.4990° 0.4990

3.1 | 0.4990 0.4991 0.4991 0.4991 0.4992 0.4992 0.4992 0.4992 0.4993 0.4993
3.2 | 0.4993 0.4993 0.4904 0.4994 0.4994 0.4994 0.4994 0.4995 0.4995 0.4995

3.3 | 0.4995 0.4995 0.4995 0.4996 0.4996 0.4996 0.4996 0.4996 0.4996 0.4997
3.4 | 0.4997 0.4997 0.4997 0.4997 _ 0.4997 0.4997 0.4997 0.4997 0.4997 0.4998
````

## 2022-23 · Final-Exam · Sem 3 · paper e79b29f92800

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSBS/SEM-III/COMPUTATIONAL STATISTICS/Computational Statistics, 2nd Year, Sem-III, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (7 pages), mean OCR confidence 80.3
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
; SVKM’s NMIMS
, MUKESH Sieh SCHOOL OF TECHNOLOGY MANAGEMENT & angi RING lL.
A RY SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERIN

Academic Year: 2022-23

| Programme: B. Tech (CSBS ) : . Year: II Semester: III

i

Subject: Computational Statistics

. oo, Marks: 100 -
Daté: 25 November 2022) . Time: 10.00 am - 1.00 pm -
; ; Durations: 3 (Hrs) -

No. of Pages: OF __

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which is provided for their use.

1) Question No. 01 is compulsory.
2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

can
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.
Q1. Answer briefly:
CO:1 | A | Let X be distributed as N3(u,2) where py" = [1,2,—1] and [05]
SO:1 :
BL:3 4 0 -1
Z=/0 3 14.
—1 1 2
; Identify whether (X, + 2X3) and X, are independent.
CO: B | Analyze the following Residual plot: ; [05]
SO:6
CO BL:A :
0.24 . "
_ O14 a
2 00+---------=--- S----- _—
2-014 7
0.24. ° °
0.3 % T - T T T
60 70 80 90 100

Numbcr of Passengers

Interpret whether the Linear regression model is preferred or not.

COT |C/The data in the accompanying table relate grams plant dry weight Y to [05]
SO: 6 ercent soil organic matter X1, and kilograms of supplemental soil
BL.2 Pé 8 , gr PP.

° nitrogen added per 1,000 square meters X2:

Page 1 of 7
--- page 2 ---
Y Xi: X2

78.5 7 2.5
74.3 d. 2.7
105.1 11 5.9

a. Define Y, X and B for the Model.
b. Compute /. Interpret estimated regression coefficient of X1.

CO: | D | Apply K means algorithm to create two clusters. [05]
S0:2 :
BL:3 il
2 : me is B32} -
(1,1)
e @ 23,4)
e505)
t t t t
4 2 3 4
Q2
co:1 [A | Consider the following data on one predictor variable Zi and. two [06]
mas responses Y; and Y2 as given below:
, Za 0 i ) 73 a
YX 3 5 2 : 4 1
Y2 : -1 3 -1 2. 3
Determine the least squares estimates of the parameters in the bivariate
straight-line regression model given as
Y= Zp.
Given that
17 [5 10
e7= lio 30!
CO-3 |B | Design a Python program to visualize the following data set: [06]
SO:1
BL:6 Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
The expected output is shown as below:
Page 2 of 7
--- page 3 ---
Popularity of Programming Language
Worldwide, Oct 2017 compared to a year ago

ce

CH
Javascript

PHP

jeva

Co: 1 Each Delicious candy company store makes 3 size candy: regular (X:), fun | [08]
oe size (X2) and big size (Xs). Assume that the weight (in ounces) of the candy .
. bars (X1, X2, X3) follow a multivariate normal distribution with parameters:
5 4 -1 0
> w= }3) andX=}]-1 4 3
8. 0 3 7
Suppose a store is selected at random. Estimate the probability in each of
the following cases: ;
a. The weight of a regular candy bar is greater than 8 oz, given that
the fun size weighs 1 oz and big size bar weighs 10 oz.
b. P(X, >8)
Given: Area from z=0 to z= 1.5 is 0.4332, Area from z=0 to z= 0.96 is 0.3315.
03
CO:2 Following data set is the ratings of the new mixer on two characteristics | [10]
BL (at a specified price) by a panel of 10 potential purchasers. In rating the
i food mixer, each panel member is implicitly comparing it with products
already on the market. After the product was evaluated, the evaluators
_ were asked to state their buying intentions (“would purchase” or “would
’ not purchase”). Five stated that they would purchase the new mixer and
five said they would not. Apply Linear Discriminant Analysis to find
projection vector for the following two-dimensional dataset.
4223 4 9 6 9 8 10
X= X,=
243 64 10 8 5 7 8
= Corl Given dataset is having actual and predicted dependent variable values. | [10]
— Calculate Residuals, Standard error, RSS, R squared and adjusted R-
- . squared considering three independent variables.
Y 21 21 ms jaa |1is7 Jig1 [143 | 244 | 228 | 19.2
Yhat | 215 21.14 | 261 | 202 [175 |19.7 | 14.9 | 22.5 | 25.1 | 18
Page 3 of7
--- page 4 ---
Q4

CO:1 | A | Let Xi, X2, X3 and X4 be independent N,(u, Z) random vectors. [06]
SO: 1
BL: 2 a. Identify the marginal distributions for each of the random vectors

1, 1, 1, 2
Vy = Gh gkot GX — 3X

4 4 3
and
1 1 2 1
Y= Pees = q%2 + 3% = 4%
b. Find the joint density of the random vectors V, and V2 .
CO:3 B | Design the Python program [06]
SO:1 ;
BL:6 A. To check if all items of a given list of strings is equal to a given
string.

B. To iterate the first 10 numbers and in each iteration, print the sum.
of the current and previous number.

CO:1 C | A designed experiment is done to assess how moisture content and [08]
BO: sweetness of a pastry product affect a taster’s rating of the product.

BL:4 : :
Analyze the below MINITAB Output of multiple regression model.
Regression Analysis: Rating versus Moisture, Sweetness
Analysis of Variance
Source DF Adj 55 Adj MS 2 F-Value
Regression 2 1872.70 936.35 o,000
Moisture 1 1566.45 1566.45 0,000
Sweetness 2 306.25 306.25 0.000
Error 13° 34.30 7.25
Lack-of-Fit 5 37.36 7.4 1.05 0.4530
Pure Error & 57.00 7.13
Total 15 1967.00
Model Summary
5 R-sq R-sq(adj) R-sq(pred)
2.69330 95.218 4.478 92.468
Coefficients
Term Coe= SE Coet P-Value VIF
Constant 37.65 3.00 0.000
Moisture 4.425 0.301 a,000 1.00
Sweethess 4.375 G.673 6.50 0,006 1.00
Q5

Page 4 of 7
--- page 5 ---
CO:2 | A | Analyze the following output of Factor Analysis: [10]

SO:6
BL:4 Scree Plot
wl
ot
s4
Be]
2
2 34
ia
a
id
o|
4 2 3 4 s 6 7 8 3 40 11 12
Factor Number
qm -
Structure Matrix.
Factor
4 2 3
7 i
tems NeTRUE Wer B16 AT1 525
item14 INSTRUC
SCHOLARLY GRASP 086 68 aA
item15. INSTRUCTOR
CONFIDENCE 768 547 587
item16. INSTRUCTOR
FOCUS LECTURES 80 a0F 28
item17 INSTRUCTOR
USES CLEAR 755 872 662 .
RELEVANT EXAMPLES
item13 INSTRUCTOR
SENSITIVE TO 564 824 B05
STUDENTS .
item19 INSTRUCTOR
ALLOWS ME TO ASK 430 754 478
QUESTIONS.
item20 INSTRUCTOR
. IS ACCESSIBLE TO
D> STUDENTS OUTSIDE HBL _ a8
CLASS
item21 INSTRUCTOR
AWARE OF STUDENTS 528 704 649
UNDERSTANDING
item22 | AM SATISFIED
WITH STUDENT <
PERFORMANCE 462 656 a6
EVALUATION
item23 COMPARED TO
OTHER INSTRUCTORS, 778 669 885
THIS INSTRUCTOR IS
item24 COMPARED TO
— OTHER COURSES THIS 582 873 795
COURSE WAS
‘ Exiraction Method: Principal Axis Factoring.
oe] Rotation Method: Promax with Kaiser Normalization.

Page 5 of 7
--- page 6 ---
Total Variance Explained

] Initial Elgenvaluesb Extraction Sums of Squared Loadinget Rotation Sums of Squared Loadings 8
Factora] Total® | % ofVarianced] Cumulative %°| Total _| % ofVariance | Cumulative % | Total | %ofVariance | Cumulative %
1 6.249 52.076 §2.076 5.851 48,759 48.789 2.950 24.583 24.583
2 1.229 10.246 62.322 806 6719 56.478 2.658 22427 48.710
3 ANY §.992 68.313 360 3.000 58.478 1.412 11.769 §8.478
4 B13 $109 | 73423
§ Gt 4876 78.099
6 503 4492 82.291
7 AT 3.927 96.218
8 389 3.240 09.458
9 368 * 3.066 92.524
10 328 2736 95.259
a ils 2.845 97.904
12 252 2.096 100.000

Extraction Method: Principal Axis Factoring.

CO:2 B | Apply the principal component analysis for the data given below: [10]
SO:2
BL3 _fi9 22 6 3 2 20
{12 6 9 15 13.5
Q6
CO:2 |A|For the given distance matrix, apply average linkage hierarchical} [08]
50:2 clustering method.
BL:3
1 [2 [3[4[s
1 0
2 9 0
3 3.7 =O
4 6 5 9 0
5 11 10 2 8 0
CO:2 B | The table below shows the dataset of 7 observations where each [12]
a observation consists of two numerical features Yield, Water and a binary
: response variable Y. An observation with features 49.39 and 29.2 was
added to the data. Classify the new observation as ‘Salty’ or ‘Clay’ by
employing discriminant analysis.
Yield 62.8 45 47.8 52.5 80 54.7 63.5
Water 25.9 15.9 36.1 39 » | 54.2 32.1 25.6
Y Salty Salty Salty Clay Clay Clay Clay
Given:
[90.056 45.233] [146.423 104.166]
‘| 45.233 113.155]? |104.166 138.321]
4,=[46.4 25.967], u,=[62.675 37.725]
Page 6 of 7
--- page 7 ---
Q7
cO:2 | A | Suppose a teacher wants to divide her students into different groups. She [06]
—- has the marks scored by each student in an assignment and based on these
° marks, she wants to segment them into groups. There’s no fixed target
here as to how many groups to have. Since the teacher does not know what
type of students should be assigned to which group, it cannot be solved as
a supervised learning problem. Apply Single Linkage hierarchical
clustering here and segment the’students into different groups. Show your
results by drawing a dendrogram.

StudentID | 1 2 3 4 5
Marks 10 7 28 20 ~| 35
CO:1 |B | Consider the following samples with respect to DVi and DV». [14]

SO: 1
BL:3 DVi ; DV2

Population 1: 10, 5,9 Population 1: 3, 2,7
Population 2: 0,2 Population 2: 4, 0
Population 3: 3, 1, 2 Population 3:8,9,7

Apply MANOA test and infer the results. Given F4,3,0.05= 6.04.

BAER EEE EE ERR A I 5, THE BEST Atte eee eee eRe REET ERE EET

Page 7 of 7
````

## 2022-23 · Re-Exam · Sem 3 · paper 9577ef9008e2

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSBS/SEM-III/COMPUTATIONAL STATISTICS/Computational Statistics, 2nd Year, Sem-III, Year 2022-23, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 February 2023
- Text: ocr (6 pages), mean OCR confidence 85.3
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
t

SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /

Program: B. Tech (CSBS ) Year: I Semester : III
AcademicY ear: 2022-2023

Marks: 100
Date : 01 February 2023 Time: 10.00 am - 1.00 pm
Durations: 3 (Hrs)
No. of Pages: 6
Re-Examination (2022-23)

/ Subject: Computational Statistics

~ Instructions: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which is provided for their use.

1) Question No. 01 is compulsory.

2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Q1 Answer briefly: MM
CO:1 | A | Let X be distributed as N3(u,2) where uw? = [1,—1,2] and [05]
SO:1

4 0 2|

BL: 3
0 5S 2).
—1 2 3

Identify whether (X, — X3) and X2 + 2X; are independent.
@ CO:01_ |B | Consider two models: [05]

SO:2 .
BL:02 *Model 1 uses input variables X1, X2, and X3 to predict Y1.

aS

*Model 2 uses input variables Xi and X2 to predict Y1.

Explain which of the model should be used. Justify your answer.
Information regarding both models is provided below:

Model 1 Model 2

Variables used X1, Xz, Xs, Yi Xr, X2, Yi
R-Squared 0.5923 0.5612
Adjusted R-Squared 0.4231 0.3512

Page 1 of 6
--- page 2 ---
cor [Cc 1 3 5 [05]
SO: 6 LetX¥=]|]1 4) ,Y=]7/)1.
ees 1 7 11

Compute f = Al
1

CO:02 | D | Apply K means Clustering method to the following points (with (x, y) [05]

es representing locations) and create two clusters:
Ax(2, 10), A2(2, 5), Aa(8, 4), Aa(5, 8), As(7, 5)
Q2

CO:1 | A | Consider the following data on one predictor variable Z: and two| [06]

pa responses Y1,and Y2 as given below:
ay 2{|]a2)0)1 72
Yi 5 3 4 2 1
Y2 3 -1 -1 2 3
Determine the least squares estimates of the parameters in the bivariate
straight-line regression model given as
Y= Zp.
Given that
17-1 _f0.2 0
(ZZ) = [ 0 0.1
CO:3 B | Design a Python Program to print the following star pattern using for | [06]
SO:1 loop.
BL:6
CO: 1 Cc 111 [08]
SO: 1 Let X be N3(u,£) with wu? = (2,3,-1) andZ= |1 3 2].
BL:5 i 2 2

a. Identify the distribution of 2X, — 3X, + X3.

b. Determine a (2 x 1) vector a such that X; and X,—a™ ea are
3

independent.

Page 2 of 6
--- page 3 ---
Q3

CO:2 A | Apply the Linear Discriminant Analysis Method to find out projection | [10]
SO: vector for the following two-dimensional dataset.

BL:3
422 3 4 9 69 8 10
X, = ,X, =
243 6 4 1085 7 8
CO1 B | A study is conducted using railway passengers traveling 500 km on | [10]
SO: comparable routes during the same season of the year. The data

Bla displayed in the Table are the costs and associated number of passengers
for twelve passengers. A regression model is developed to predict cost
by number of passengers. Analyze the data and evaluate Standard Error,
Residuals, RSS, R squared and adjusted R-squared.

Number of passengers Actual Cost Predicted Cost
61 4.280 4.053
63 4.080 4.134
67 4.420 4.297
69 40170 4.378
70 4.480 4.419
74 4.300 4.582
76 4.820 4.663
81 4.700 4.867
86 5.110 5.070
91 5.130 5.274
95 5.640 5.436
97 5.560 5.518
Q4

CO:1 | A | Suppose that the weights (Ibs.) and heights (inches) of undergraduate | [06]
SO: 6 college students have a multivariate normal distribution with mean

cae 540 45

45 10!

Estimate the mean and variance of the conditional distribution. Also,
estimate the mean and standard deviation for students with height 70

vector # = [7s 75 | and covariance matrix = = [

inches.
CO:3_ |B | A magic date is a date where the day multiplied by the month is equal to | [06]
a the two-digit year. For example, June 10, 1960 is a magic date because

June is the sixth month, and 6 times 10 is 60, which is equal to the two-

Page 3 of 6
--- page 4 ---
digit year. Apply the knowledge of python programming to build a
function that determines whether or not a date is a magic date. Use your

function to create a main program that finds and displays all of the magic
dates in the 20th century.

CO1 C | The given Peruvian Blood Pressure dataset consists of variables possibly | [08]
a relating to blood pressures of n = 39 Peruvians who have moved from
° rural high-altitude areas to urban lower altitude areas. Responsé variable
in this dataset is systolic blood pressure.
When we run a multiple regression using all nine x-variables as
predictors. The result is given below:
Analysis of Variance
Source DF Adj SS Adj MS F-Value P-Value
Regression 9 4358.85 484.32 6.46 0.000
Error 29 2172.58 74.92
Total 38 6531.44
Model Summary
s R-sq R-sq{adj) R-sq{pred)
8.65544 66.748 56.418 34.458
Coefficients
Term Coef SE Coef T-Value P-Value VIF
Constant 146.8 49.0 3.00 0.006
Age -1.121 0.327, -3.43 0.002 3.21
Years 2.455 0.815 3.01 0.005 34.29
FracLife -115.3 30.2 -3.82 0.001 24.39
Weight 1.414 0.431 3.28 0.003 4.75
Height -0.0346 0.0369 -0.94 0.355 1.91
Chin -0.944 0.741 -1.27 0.213 2.06
Forearm * -1.17 1.19 -0.98 0.335 3.80
Calf -0.159 0.537, -0.30 0.770 -2.41
Pulse 0.115 0.170 0.67 0.507 1.33
Analyze the above MINITAB output.
Q5
CO:2__ | A | Students entering a certain MBA tech Business analytics program must | [10]
an take three required courses - BIG Data technology, Financial Analytics

and Business Analytics. Let Yi, Y2 and Y3 respectively represent a
student's grades in these courses. The available data consist of the grades
of 15 students, we do FA based on these data points. Analyze the
follgwing output of factor analysis.

Page 4 of 6
--- page 5 ---
Results

Total Variance Explained

Initial Eigenvalues. Extraction Sums of Squared Loadings | Rotation Sums of Squared Loadings
Componen : % ot Cumulative % of Cumulative % of Cumulatve
t Total_| _Vanvance % Total Variance % Total Variance %
1 1.982 66.072 66.072 1.982 66.072 66.072 1.980 §6.016 66.015
2 1.002 33.404 99 476 1.002 33.404 99.476 1.604 33.460 99.416
3 016 524 100.000

Extraction Method: Principal Component Analysis.
Rotated Component Matnxa

Component
i 2
bigdata 5 -013 1.000
fa 994 -.056
dsil 996 029

Extraction Method: Principal
Component Analysis.

Rotation Metnod: Varimax with
Kaiser Normalization

a. Rotation converged in 3 iterations.

re B | Apply the principal component analysis for the data given below: [10]
0:2
: 1
BL v(t 222
245 1
Q6
CO;:2 A | Suppose that a biologist wants to determine the subspecies in a [8]
Bee population of birds belonging the same species. A small sample of 7 birds
, is selected as a pilot test. For each of the 7 birds, two characteristics of
their beaks are measured: V1 - length and V2 - width. Design the distance
matrix by using Euclidean and perform single link hierarchical clustering.
Show your results by drawing a dendrogram.
Sr | Sp S3 Se Ss Sé
Vi 3 4 4 2 6 7
V2 2 5 7 7 6 7
CO:2 B | A factory in India produces very expensive and high-quality chip rings] [12]
SO:2

ate that their qualities are measured in terms of curvature and diameter.
: Result of quality control by expert is given in the table below;

Curvature Diameter
Passed 2.95 6.63

Page 5 of 6
--- page 6 ---
Passed 2:53 7.79

Passed 3.57 5.65
Passed 3.16 5.47
Not Passed. 2.58 4.46
Not Passed 2.16 6.22
Not Passed 3.27 3.52

As a consultant to the factory, you get a task to set up the criteria upon
new type of chip rings that even the human experts are argued to each
other. Giver:

* | [0166 -0.192] | [0.259 -0.286
[0.192 1.349 7 | -0.286 2.142
4,=[3.05 6.38], ,=[2.67 4.73]

Solve this problem by employing linear discriminant analysis (LDA).

“07
CO:2 | A | Apply complete link clustering to form two clusters to the given distance | [06]
SO: matrix
BL:3
A 0 4 25 24 9 7
B 4 0 21 20 5 3
Cc 25 21 0 1 16 18
D 24 20 1 0 15 17
E 9 5 16 15 0 2
F 7 3 18 17 2 0
CO:1 |B | Consider the following samples with respect to DV; and DV». [14]
DV; DV,
Population 1: 9, 5, 10 Population 1: 4, 4,7
Population 2: 0, 4 Population 2: 9, 0
Population 3: 6, 2,4 Population 3: 9, 7,8

Apply MANOA test and infer the results. Given F1.,0.05 = 6.04


Page 6 of 6
````

## 2022-23 · Re-Exam · Sem 3 · paper f48ec7ac2ae4

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSBS/SEM-III/COMPUTATIONAL STATISTICS/Computional Statistics, Sem-III, Year 2022-23, Special Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 80.9
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS

Academic Year: 2022-2023

Program: B.Tech. Stream ; CSBS Year: II Semester: III

Time: 03 hrs (LLamto2pnv_)
No. of Pages: 06

Subject: Computational Statistics
Date:_16 Jun/ 23 .
Marks: 100

Special Re- Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any 4 _ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q1 Answer briefly: MM
CO:1 | A | Let X = [X1 X2]? bea multivariate normal random vector where mean [05]
— is u = [1,2]” and covariance matrix
_p 1
aaa 2]
For random variable Y=X)+X2, Evaluate the mean and variance.
CO:01 |B | The equation of the regression line given below is [05]
SO:2
» | BL:03 ¥ = 0.1441.2x
8
> 7. Y
5 : =
B + 2
H =
gi
_—. 0 +
Oo 1 2 3 4 5 6 7
“ Number of lectures per day
Compute the residuals and R squared value.
wl)
--- page 2 ---
CO:1 ‘a 1 2 5 . a . s [05]
SO: 6 LetX= ]1 4] , Y= ]7] with B= lA .Prove that 8 = 3] f
BL: 2 1 6 11 By 1.00.
cO:02 | D | Apply the k-means algorithm and Euclidean distance to create two [05]
Bos clusters from the following dataset:

A (0, 1); B(3, 0); C(2, 4); D(2, 1); EG, 5)
Q2
CO:1 A | Determine the least square estimate, predicted value, residual and | [06]
ae residual sum of squares of the linear regression model for fitting a

| straight line:

xX 0 1 2 13 4

Y 1 4 3 8 9

CO:3 B | Write a Python program to calculate the electricity bill for a residential | [06]
Bee customer. The program should take the number of units consumed as
, input and calculate the bill based on the following conditions:

o For the first 100 units, the rate is $0.10 per unit.

o For the next 200 units, the rate is $0.15 per unit.

o For any additional units, the rate is $0.20 per unit.
o There is also a fixed monthly charge of $10.

CO:1 Cc 111 [08]
SO: 1 Let X be N3(u,2) with yw? = (3,-2,1) andZ= }1 3 2}.
Bid 12 2

a. Identify the distribution of 3X, — 2X2 + X3.
x.
b. Determine a (2 x 1) vector a such that X, and Xz — a’ ( “) are
3

independent.
Q3
CO:2 A | Apply the Linear Discriminant Analysis to estimate the projection vector | [10]
| to the following two-dimensional dataset:

8 6 10 9 4 976 4 8
X= a
53 422 47542
CO:1 B |A specialist in hospital administration stated that the number of | [10]

ae employees in a hospital is estimated by counting the number of beds in
4 the hospital. Develop a regression model to predict the number of

@
--- page 3 ---
employees of a hospital by the number of beds. The data is pregantell i in
sequence, according to the number of beds. %

Number _ of | 23 | 29 | 29 35 42 46 50 54 64 66 76 78
beds

Employees 69 | 95 | 102 | 118 | 126 | 125 | 138 | 178 | 156 | 184 | 176 | 225

Also determine SSE, Standard Error of estimate

Q4
CO:1 | A | Let X1,X2,X3 and X4 be independent and identically distributed (3x1) | [06]
SO: 6 random vectors with
BL: 5
3 3 -1 1
w=|-l|,>=/-1 1 0
1 1 0 2
Consider the linear combinations of random vectors
1 1 1
—%, +5% +S +7%
& %,+%,+%, -3%,
Find the mean vector, and covariance matrix for each linear combination
of vectors and also the covariance between them.
cO:3 |B | Write a python program to create the function uses the following | [06]
a ; conditions to determine if a year is a leap year:

a) If the year is divisible by 4, it is a potential leap year.

b) If the year is divisible by 100, it may not be a leap year, unless it is
also divisible by 400.

c) If the year is divisible by 400, it is definitely a leap year.
--- page 4 ---
;

CO: C | The result of regression analysis done by one of the MBA students groups} [08]
ae in the sports and entertainment economics class is reported in the;table
: below. The dependent variable is the gross revenue from 191 movie show
in theaters. Analyze the results of regression from the given minitab
output.
(Sa ee oe EY
SUMMARY OUTPUT
Regression Statistics
MultipieR O.292252677
RSquare 0.084828322
Adjusted R Square 0.07014622
Standard Error 50181924.73
Observations 4252
ANOVA
oF $s aS a Significance F
Regression 3B 4.36485Fe1G L4S5496E°15 5.777734 0.000845912
Residual 187 64.70908E*17 2.51823E*iS
Total 290   S.24557E+17
Coefficients Stendoard Error eSeor P-value
intercept $2846788.93 24363241.93 0.527302112 9.598669 -
Ticket_Prices. 7483427.727 3206667474 2.333708683 0.020674
Star_Power 2612195892 7605710.943 3.434519024 9.000731
Movie_Rating ~9330073.57   7453336.119 -3.2517983i3 0.212207 -
Q5
CO:2 A | Analyze the following output of factor analysis. [10]
SO:6
BL:4

Component Matrie

im nent :

fem 1: 2 | 3 zt T 5 6 | 7 3
“a | 0.659 | 0.136 | -0.398 | 0.160 | -0.064 | 0.568 | -0.177 | 0.068
2..| 0.300. 0.866.| -0.025 | 0.092 | -0.290 | -0.170 | -0.293 |. -0.003
3 -0.653 | 0.409 | 0.081 | 0.064 | 0.410 | 0.254 | 0.378 | 0,142
a }-9.720°} 0.219" | 0.192 | 0.064 |-0.288 "| -0.089-|-0.563° | -0.137
5 0.650 | 6.096 | -0.215 | o.a6o | 0.443 | -0.326 | -0.092 | -0.010
6 0.572 | 0.185 | 0.675 | 0.031 | 0.107 | 0.176 | -0.058 | -0.369
"7 | 0.718 | 0,044 | 0.453 | -0.006 | -0.090 | -0.051 | 0,025 | 0.516
8 o.s6s | 0.267 | -0.221 | -0.694 | 0.258 | -0.084 | -0.043 | -0.012

Extraction Method: Principal Component Analysis:
--- page 5 ---
Total-Variance Explained: . --: -

: initial Eigenvalues © : : Extraction Sums of Squared Loadings

» Total % of Variance —— Total % of Variance Cumulative % -
D4... |... 3.057 . 38.206. |. 38.206 |. 3.057..]...38.206.°./..).. 38.206
/2   -| 1087 |: 13.536 | -S1.s43 | 1.067 13.336 : 51.543

3 | o958 |: 11980 | '63.523: 0.958 11.980 | : 68.523
-4 | 0736 |: 9.205 | -72.728 | 0.736 9.205: 72.728
(S| 622°]: 7770" “| 180.498: 0,622" 7.770 °°: {°° °° 80.498 °
(6 °| o572 |: 7.135 87.632. 0.571 7135 87.632
/7 :| 0.543 6.788 :94.420- 0,543 6.788 > 94.426

-&---|- O46 -|-- 5.580-- | 100.000 -| - 0.446--|--- 5.580: -:-}--:- -200,000--: - -

- Extraction Method: Principal-Component Analysis. .

Scree Plot

1 1 3 4 5 6 1 8
‘Component Number

CO:2 B | Compute the principal component using PCA Algorithm for the data} [10]

aa generated using your date of birth. For example for DOB as DD-MM-
: YYYY, the row1 is the DDMM and row 2 is YYYY
Q6
CO:2 A | The dimensions of seven iron slabs are measured, length (1) and width [8]
Bee (w). The sample data is given below Construct the distance matrix by

using Euclidean and perform single link hierarchical clustering. Show
your results by drawing a dendrogram.

Clustering fal ajlalca|ca|c | co
Variable
Length (1) 3 4 4 2 6 7 6
Width (w) 2 5 7 7 6 7 4
CO:2 B_ | Suppose you have trained a Linear Discriminant Analysis (LDA) model | [12]
on a dataset with two classes (Class A and Class B) using the LDA
: algorithm.

(5)
--- page 6 ---
Class A: [(2, 4), (3, 6), (4, 8)]

Class B: [(1, 2), (2, 3), (3, 4)]

The model has learned the discriminant function and the projection
vector for the data. Now, given a new data point with features (2,1),
Apply the trained LDA model to predict the class label of the new data

point.
Given:
_/ 0.917 2.083 _| 0.259 -0.286
'} 2.083 4.917 |’? |-0.286 2.142
Q7
CO:2 A | Perform k-means clustering for the following data. [1, 1], [1.5, 2], [3, 4], | [06]
a [5, 71, 3.5, 5), [4.5, 5], [3.5, 4.5]
co:1 |B | Consider the following samples with respect to DV1 and DV2. [14]
SO:2
BL:3 DV1 DV2
Population 1: 9, 6,9 Population 1: 3,2,7
Population 2: 0, 2 Population 2: 4, 0
Population 3: 3,1,2 Population 3: 8,9,7

Apply MANOA test and infer the results. Given F4s,0.05= 7.01

(6)
````
