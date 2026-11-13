# Basic Decision Making with Spreadsheet: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 3e11d55326ff

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (13 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   What is the difference between a formula and a function in Excel?   [5]
SO- ;
Give one example of each.
BL-2
Solution:
Feature   Formula   Function
A   pre-built   command
A user-created equation
Definition   provided by   Excel   to
to perform calculations.
perform specific tasks.
Created by Microsoft and
Created by   the   user,
cannot be modified by the
Creation   combining operators, cell
user, but can be modified by
references, and constants.
the developer.
Requires a specific syntax,
Does not have a specific
usually in the format of
Syntax   syntax, but must start with
=FUNCTION_NAME(argu
an equals sign (=).
ment1, argument2, ...).
Highly customizable and
Limited to the tasks it was
Flexibility flexible   for   custom
designed for.
calculations.
Can be simple or complex Simplifies   complex
Complexity   depending on the user's operations   and   makes
needs.   calculations more efficient.
********** 1 **********
--- page 2 ---
=SUM(A1:A10) (adds   all
values in the range A1
through A10)
=A1+B1 (adds values in
Example
cells A1 and B1)
Other Eg:
Can   be   SUM,
COUNT,MAX, MIN etc.
CO-2;   b.   Mention Key components of CVP Analysis (any 5)   [5]
SO- ;
BL-4
Solution:
Key Components of CVP Analysis:
• Fixed Costs: Costs that remain constant regardless of the production
or sales volume.
• Variable Costs: Costs that change directly with the production or
sales volume.
• Sales Volume: The number of units sold or produced.
• Selling Price: The price at which each unit is sold.
• Contribution Margin: The difference between the selling price per
unit and the variable cost per unit.
• Break-Even Point: The sales volume at which total revenue equals
total costs, resulting in no profit or loss
CO-2 ;   c.   Explain the purpose of Co-relation analysis.   [5]
SO- ;
Explain the difference between positive and negative correlation.
BL-3
Solution:
To determine the strength and direction of the relationship between two
quantitative variables. Co-relation coefficient measures the strength and
direction of a linear relationship between two variables, ranging from -1
to +1
In a positive correlation, variables move in the same direction (e.g.,
income and expenditure).
In a negative correlation, they move in opposite directions (e.g., price and
demand).
********** 2 **********
--- page 3 ---
CO-2 ;   d.   Net Present Value (NPV) and Internal Rate of Return (IRR) are crucial   [5]
SO- ;
tools for evaluating investment proposals. Please elaborate.
BL-4
Elaborate what is NPV and IRR and how to interpret the outcomes of
each.
Solution
NPV
NPV considers the time value of money by discounting future cash flows
back to their present value. It represents the difference between the
present value of cash inflows and the present value of cash outflows.
Interpretation:
A positive NPV indicates that the investment is likely to be profitable,
while a negative NPV suggests it may not be worthwhile.
IRR
IRR is the discount rate at which the NPV of all cash flows from a project
equals zero. It represents the potential return on investment.
Interpretation:
NPV uses a discount rate to calculate the present value of future cash
flows, while IRR determines the discount rate that makes the NPV equal
to zero.
Q2   a.   1) Define the decision variables   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
2) Formulate the objective function
3) Write all constraints
********** 3 **********
--- page 4 ---
4) Solve the LPP equation and find out the minimum cost using LPP
Solver.
x1 = 1, x2 = 0, x3 = 1, x4 = 1, x5 = 1
Minimum cost Z = 0.73
CO-1,2;
b.   [5]
SO-;
BL-1,
BL-3,   1. Using excel formula, find the average experience of all the employees.
-   5.44 years using the AVERAGE Formula
2. Using excel formula, extract only the employee number from the
Employee ID of Amit.
- = RIGHT(Cell Reference, 3) → E101 →101
3. Using excel formula, create employee label of Neha.
Employee Label comprises of Employee ID followed by
‘-‘ followed by the name of the employee, followed by the Department
in brackets. Eg: “E101-Amit (Sales)”
********** 4 **********
--- page 5 ---
= CONCATE(A3, “-”, B3, “ (“, C3,”)”) → “E102 – Neha (HR)”
4. Using excel Nested-IF function, find out total Sales undertaken by the
Sales Department.
= SUMIF(C3:C27,”Sales”,D3:D27)
= 385000
5. Using appropriate LookUP function, find out the number of units sold
by Tanya.
=VLOOKUP(Tanya,B3:B27,4,FALSE)
= 8
Q3   a.   Decision Tree   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to open a medium sized shop as the
EMV is the highest under that option of $18,000.
CO-2;
SO-;   b.   In an experiment of dice roll, A dice is rolled 30 times.   [5]
BL-4,   Probability of rolling a “6” = 1/6.
BL-5
********** 5 **********

[Text in pictures on this page, read by OCR]
Good Market $40,000

Opena 0.3
small shop 0.4 Average Market $20,000

$15,500 9.3 Bad Market -$15,000

ae Good Market $70,000

0.4 Average Market $30,000

Opena
medium-sized shop

Se Bad Market -$50,000

Good Market so
Do not

open a shop

$o

0.4 Average Market $0

0.3 Bad Market
--- page 6 ---
Find
1. Probability of rolling exactly 5 sixes.
=BINOM.DIST(5, 30, 1/6, FALSE) = 0.206
2. Probability of rolling at most 5 sixes.
=BINOM.DIST(5, 30, 1/6, TRUE) = 0.616
3. Probability of rolling atleast 3 sixes
=1 - BINOM.DIST(2, 30, 1/6, TRUE) = 0.8972096263
4. Probability of between 4 and 8 sixes.
=BINOM.DIST.RANGE(30, 1/6, 4, 8)
5. Expected number of sixes.
=30*(1/6) = 5
Q4   a.   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 6 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

~ 7, _f
Dif=%, P(X)=F

Values: 0.15, 0.25, 0.30, 0.20, 0.10

(b) Mean, Variance, SD (6 Marks)
bi fe
p=

“= 3.85
Lif
So fa?
of = Ss _ P= 1.33
hf

o0 =V133=1.15

(c) Excel (4 Marks)

VAR.P = 1.33, STDEV.P = 1.15
VARS = 1.40, STDEV.S = 1.18

(d) Interpretation (2 Marks)

Moderate variation, fairly consistent data
--- page 7 ---
CO-1,2;
SO-;
BL-1;   b.   1. Assign grade using Nested IF (≥80 = A, ≥60 = B, else C).   [5]
BL-3
= IF(B2>=80,"A",IF(B2>=60,"B","C")) → John = B
2. Round Science marks to nearest 10.
=ROUND(C2,-1) = 90
= ROUND(C3,-1) = 90
= ROUND(C4,-1) = 70
= ROUND(C5,-1) = 60
= ROUND(C6,-1) = 40
3. Check if student passed all subjects (upon scoring ≥50) using AND.
=AND(B2>=50,C2>=50,D2>=50) = TRUE
Do this for all students
4. Rank students (ascending) by Math marks.
=RANK(B2,$B$2:$B$6)
Do this for all students
5. Find highest marks for each student.
= MAX (B2:D2)
Do this for all students
Q5   a.   The dataset given below contains banking transaction records including   [15]
CO-2,3;   details such as date, Officer Name, Transaction Type, Account Type, and
SO-;
Region. It is used to analyze transaction patterns, workload distribution,
BL-4;
BL-6   and regional banking behaviour.
No. of   Avg.
Account   Transactio   Officer   Transa Amo   Service
Date Region   Branch   Type   n Type   Name   ctions   unt   Rating
(Refer Dataset file for details)
********** 7 **********
--- page 8 ---
1. Create a Pivot Table showing Officer-wise total Number of
Transactions and sort the results from highest to lowest. Based on
the Pivot Table, identify the officer handling the highest workload
[3 Marks]
2. Insert a Pivot Chart comparing Account Type-wise transaction
activity across regions and interpret which account type is most
active and how banking activity differs region-wise. [3 Marks]
3. Create a Pivot Table showing total Number of Transactions by
Transaction Type and insert a Slicer for Region and state a short
conclusion about regional banking behaviour. [4 Marks]
4.
i. VLOOKUP("AI Guide", A2:D6, 4, FALSE)
Answer: 1200
ii. =HLOOKUP("Excel Master", A1:E5, 3, FALSE)
Answer: 25
b.   1. Using Excel, find the probability that the daily production is less   [5]
CO-2;
SO-;   than 850 units.
BL-4;
Less than 850 =NORM.DIST(850,1000,120,TRUE)
BL-5
2. Using Excel, find the probability that the daily production is more
than 1150 units.
More than 1150 =1-NORM.DIST(1150,1000,120,TRUE)
3. Using Excel, determine the proportion of days when production lies
between 900 and 1100 units.
Between 900 and 1100 =NORM.DIST(1100,1000,120,TRUE)-
NORM.DIST(900,1000,120,TRUE)
********** 8 **********
--- page 9 ---
4. Using Excel, find the production level such that only 2% of days
exceed this value.
=NORM.INV(0.98,1000,120)
5. Based on your analysis, comment on whether 850 units is a suitable
minimum production target.
= 1 - NORM.DIST(850,1000,120,TRUE)
Yes, 850 is a suitable minimum production target since the
probability of achieving this target is 89.44% which mean target is
achievable most of the days
Q6   a.   1. Formulate cost, revenue and profit functions   [15]
CO-2,3;   C(x) = 2,00,000 + 300x
SO-;
R(x) = 500x
BL-4,
BL-5   P(x) = 200x − 2,00,000
2. Calculate Break-even point (units & ₹) using Formula
- BEP (units) = FC / Contribution
= 2,00,000 / 200 = 1,000 units
- BEP (in ₹) = 1,000 × 500 = ₹5,00,000
3. Find profit at 1,500 units by preparing an income statement
= 200 × 1500 − 2,00,000
= 1,00,000
4. Calculate PV Ratio and Margin of Safety (at 1,800 units)
= 200 / 500 = 40%
5. Draw B-E-P graph (can consider different levels of sales)
To evaluate based on actual graphs prepared
********** 9 **********
--- page 10 ---
CO-2,3;
SO-;   b.   1. Using the dataset provided, perform Correlation Analysis using   [5]
BL-4,
Excel Data Analysis ToolPak.
BL-5
Pesti   Soil
cide   Qua Crop
Fertilizer   Rainf   Irriga   Use   lity   Yield
Used   all   tion   Labor   (liters Inde (tons/
(kg/ha)   (mm) Hours Hours   )   x   ha)
Fertilizer Used
(kg/ha)   1.00
Rainfall (mm)   -0.17   1.00
Irrigation
Hours   0.54   -0.31   1.00
Labor Hours   0.09   -0.29   0.66   1.00
Pesticide Use
(liters)   0.03   -0.48   0.53   0.39   1.00
Soil Quality   1.0
Index   0.55   -0.50   0.75   0.46   0.41   0
Crop Yield   0.7
(tons/ha)   0.74   -0.25   0.91   0.56   0.52   9   1.00
2. Identify: The variable with the strongest and weakest correlation
with Crop Yield (tons/ha)
Irrigation Hours (0.91) → very strong positive relationship with
crop yield
Rainfall (−0.25) → weak (and slightly negative) relationship with
crop yield
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.99
R Square   0.98
Adjusted R
Square   0.94
Standard Error   0.28
Observations   10.00
ANOVA
Significan
df   SS   MS   F   ce F
Regression   6.00   12.37   2.06   26.01   0.01
********** 10 **********
--- page 11 ---
Residual   3.00   0.24   0.08
Total   9.00   12.61
Coefficie Standard   Lower
nts   Error   t Stat   P-value 95%
Intercept   0.24   2.14   0.11   0.92   -6.57
Fertilizer Used
(kg/ha)   0.02   0.00   4.05   0.03   0.00
Rainfall (mm)   0.00   0.00   1.99   0.14   0.00
Irrigation Hours   0.03   0.02   1.59   0.21   -0.03
Labor Hours   0.01   0.01   1.45   0.24   -0.01
Pesticide Use
(liters)   0.08   0.03   2.59   0.08   -0.02
Soil Quality Index   0.34   0.24   1.46   0.24   -0.41
4. Write the estimated regression equation.
Crop Yield = 0.24 + 0.02(Fertilizer) + 0.00(Rainfall) + 0.03(Irrigation)
+ 0.01(Labor) + 0.08(Pesticide) + 0.34(Soil Quality)
5. Interpret ANOVA significance of the model.
• R² (Coefficient of Determination):
• R² = 0.98
• Means 98% of variation in crop yield is explained by the
model → very good fit p-value
• Shows significance of variables
• p < 0.05 → significant
• In your model:
- Fertilizer (0.03) → significant
- Others → not significant
Q7   a.   1. Calculate NPV at 8% using Excel.   [15]
CO-3;   Project A: ₹83.70
SO-;
Project B: ₹6.40
BL-4,
BL-5
2. Calculate IRR.
Project A: ≈ 25.2%
Project B: ≈ 8.93%
Project A is preferred (B fails 10% criterion)
********** 11 **********
--- page 12 ---
3. If required return = 10%, which project is preferable?
Project A is preferred (B fails 10% criterion)
CO-1,2;   b.   Dream Homes Pvt. Ltd. (DH) is a builder company specializing in
SO-;
modern flats.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 6,000
•   Salaries of employees = Rs. 36,000
Each flat requires:
• Land cost = Rs. 60,000
• Construction materials = Rs. 40,000
[5]
• Labour = Rs. 20,000
•   Sales commission = Rs. 5,000 per flat
The selling price of each flat is Rs. 150,000.
Classify the above expenses into Fixed and Variable
Fixed Costs
Rent   8000
Utilities   6000
Salaries   36000
50000
Variable Costs
Land   60000
Construction   40000
Labour   20000
Commission   5000
125000
Income statement
Units sold   1
Sales @ 150000   150000
VC   125000
Contribution   25000
FC   50000
Profit/(Loss)   -25000
********** 12 **********
--- page 13 ---
B-E-P using Goal seek = 2 Houses

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper fd0e0f23dc5d

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7057/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (13 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   What is the difference between a formula and a function in Excel?   [5]
SO- ;
Give one example of each.
BL-2
Solution:
Feature   Formula   Function
A   pre-built   command
A user-created equation
Definition   provided by   Excel   to
to perform calculations.
perform specific tasks.
Created by Microsoft and
Created by   the   user,
cannot be modified by the
Creation   combining operators, cell
user, but can be modified by
references, and constants.
the developer.
Requires a specific syntax,
Does not have a specific
usually in the format of
Syntax   syntax, but must start with
=FUNCTION_NAME(argu
an equals sign (=).
ment1, argument2, ...).
Highly customizable and
Limited to the tasks it was
Flexibility flexible   for   custom
designed for.
calculations.
Can be simple or complex Simplifies   complex
Complexity   depending on the user's operations   and   makes
needs.   calculations more efficient.
********** 1 **********
--- page 2 ---
=SUM(A1:A10) (adds   all
values in the range A1
through A10)
=A1+B1 (adds values in
Example
cells A1 and B1)
Other Eg:
Can   be   SUM,
COUNT,MAX, MIN etc.
CO-2;   b.   Mention Key components of CVP Analysis (any 5)   [5]
SO- ;
BL-4
Solution:
Key Components of CVP Analysis:
• Fixed Costs: Costs that remain constant regardless of the production
or sales volume.
• Variable Costs: Costs that change directly with the production or
sales volume.
• Sales Volume: The number of units sold or produced.
• Selling Price: The price at which each unit is sold.
• Contribution Margin: The difference between the selling price per
unit and the variable cost per unit.
• Break-Even Point: The sales volume at which total revenue equals
total costs, resulting in no profit or loss
CO-2 ;   c.   Explain the purpose of Co-relation analysis.   [5]
SO- ;
Explain the difference between positive and negative correlation.
BL-3
Solution:
To determine the strength and direction of the relationship between two
quantitative variables. Co-relation coefficient measures the strength and
direction of a linear relationship between two variables, ranging from -1
to +1
In a positive correlation, variables move in the same direction (e.g.,
income and expenditure).
In a negative correlation, they move in opposite directions (e.g., price and
demand).
********** 2 **********
--- page 3 ---
CO-2 ;   d.   Net Present Value (NPV) and Internal Rate of Return (IRR) are crucial   [5]
SO- ;
tools for evaluating investment proposals. Please elaborate.
BL-4
Elaborate what is NPV and IRR and how to interpret the outcomes of
each.
Solution
NPV
NPV considers the time value of money by discounting future cash flows
back to their present value. It represents the difference between the
present value of cash inflows and the present value of cash outflows.
Interpretation:
A positive NPV indicates that the investment is likely to be profitable,
while a negative NPV suggests it may not be worthwhile.
IRR
IRR is the discount rate at which the NPV of all cash flows from a project
equals zero. It represents the potential return on investment.
Interpretation:
NPV uses a discount rate to calculate the present value of future cash
flows, while IRR determines the discount rate that makes the NPV equal
to zero.
Q2   a.   1) Define the decision variables   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
2) Formulate the objective function
3) Write all constraints
********** 3 **********
--- page 4 ---
4) Solve the LPP equation and find out the minimum cost using LPP
Solver.
x1 = 1, x2 = 0, x3 = 1, x4 = 1, x5 = 1
Minimum cost Z = 0.73
CO-1,2;
b.   [5]
SO-;
BL-1,
BL-3,   1. Using excel formula, find the average experience of all the employees.
-   5.44 years using the AVERAGE Formula
2. Using excel formula, extract only the employee number from the
Employee ID of Amit.
- = RIGHT(Cell Reference, 3) → E101 →101
3. Using excel formula, create employee label of Neha.
Employee Label comprises of Employee ID followed by
‘-‘ followed by the name of the employee, followed by the Department
in brackets. Eg: “E101-Amit (Sales)”
********** 4 **********
--- page 5 ---
= CONCATE(A3, “-”, B3, “ (“, C3,”)”) → “E102 – Neha (HR)”
4. Using excel Nested-IF function, find out total Sales undertaken by the
Sales Department.
= SUMIF(C3:C27,”Sales”,D3:D27)
= 385000
5. Using appropriate LookUP function, find out the number of units sold
by Tanya.
=VLOOKUP(Tanya,B3:B27,4,FALSE)
= 8
Q3   a.   Decision Tree   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to open a medium sized shop as the
EMV is the highest under that option of $18,000.
CO-2;
SO-;   b.   In an experiment of dice roll, A dice is rolled 30 times.   [5]
BL-4,   Probability of rolling a “6” = 1/6.
BL-5
********** 5 **********

[Text in pictures on this page, read by OCR]
Good Market $40,000

Opena 0.3
small shop 0.4 Average Market $20,000

$15,500 9.3 Bad Market -$15,000

ae Good Market $70,000

0.4 Average Market $30,000

Opena
medium-sized shop

Se Bad Market -$50,000

Good Market so
Do not

open a shop

$o

0.4 Average Market $0

0.3 Bad Market
--- page 6 ---
Find
1. Probability of rolling exactly 5 sixes.
=BINOM.DIST(5, 30, 1/6, FALSE) = 0.206
2. Probability of rolling at most 5 sixes.
=BINOM.DIST(5, 30, 1/6, TRUE) = 0.616
3. Probability of rolling atleast 3 sixes
=1 - BINOM.DIST(2, 30, 1/6, TRUE) = 0.8972096263
4. Probability of between 4 and 8 sixes.
=BINOM.DIST.RANGE(30, 1/6, 4, 8)
5. Expected number of sixes.
=30*(1/6) = 5
Q4   a.   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 6 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

~ 7, _f
Dif=%, P(X)=F

Values: 0.15, 0.25, 0.30, 0.20, 0.10

(b) Mean, Variance, SD (6 Marks)
bi fe
p=

“= 3.85
Lif
So fa?
of = Ss _ P= 1.33
hf

o0 =V133=1.15

(c) Excel (4 Marks)

VAR.P = 1.33, STDEV.P = 1.15
VARS = 1.40, STDEV.S = 1.18

(d) Interpretation (2 Marks)

Moderate variation, fairly consistent data
--- page 7 ---
CO-1,2;
SO-;
BL-1;   b.   1. Assign grade using Nested IF (≥80 = A, ≥60 = B, else C).   [5]
BL-3
= IF(B2>=80,"A",IF(B2>=60,"B","C")) → John = B
2. Round Science marks to nearest 10.
=ROUND(C2,-1) = 90
= ROUND(C3,-1) = 90
= ROUND(C4,-1) = 70
= ROUND(C5,-1) = 60
= ROUND(C6,-1) = 40
3. Check if student passed all subjects (upon scoring ≥50) using AND.
=AND(B2>=50,C2>=50,D2>=50) = TRUE
Do this for all students
4. Rank students (ascending) by Math marks.
=RANK(B2,$B$2:$B$6)
Do this for all students
5. Find highest marks for each student.
= MAX (B2:D2)
Do this for all students
Q5   a.   The dataset given below contains banking transaction records including   [15]
CO-2,3;   details such as date, Officer Name, Transaction Type, Account Type, and
SO-;
Region. It is used to analyze transaction patterns, workload distribution,
BL-4;
BL-6   and regional banking behaviour.
No. of   Avg.
Account   Transactio   Officer   Transa Amo   Service
Date Region   Branch   Type   n Type   Name   ctions   unt   Rating
(Refer Dataset file for details)
********** 7 **********
--- page 8 ---
1. Create a Pivot Table showing Officer-wise total Number of
Transactions and sort the results from highest to lowest. Based on
the Pivot Table, identify the officer handling the highest workload
[3 Marks]
2. Insert a Pivot Chart comparing Account Type-wise transaction
activity across regions and interpret which account type is most
active and how banking activity differs region-wise. [3 Marks]
3. Create a Pivot Table showing total Number of Transactions by
Transaction Type and insert a Slicer for Region and state a short
conclusion about regional banking behaviour. [4 Marks]
4.
i. VLOOKUP("AI Guide", A2:D6, 4, FALSE)
Answer: 1200
ii. =HLOOKUP("Excel Master", A1:E5, 3, FALSE)
Answer: 25
b.   1. Using Excel, find the probability that the daily production is less   [5]
CO-2;
SO-;   than 850 units.
BL-4;
Less than 850 =NORM.DIST(850,1000,120,TRUE)
BL-5
2. Using Excel, find the probability that the daily production is more
than 1150 units.
More than 1150 =1-NORM.DIST(1150,1000,120,TRUE)
3. Using Excel, determine the proportion of days when production lies
between 900 and 1100 units.
Between 900 and 1100 =NORM.DIST(1100,1000,120,TRUE)-
NORM.DIST(900,1000,120,TRUE)
********** 8 **********
--- page 9 ---
4. Using Excel, find the production level such that only 2% of days
exceed this value.
=NORM.INV(0.98,1000,120)
5. Based on your analysis, comment on whether 850 units is a suitable
minimum production target.
= 1 - NORM.DIST(850,1000,120,TRUE)
Yes, 850 is a suitable minimum production target since the
probability of achieving this target is 89.44% which mean target is
achievable most of the days
Q6   a.   1. Formulate cost, revenue and profit functions   [15]
CO-2,3;   C(x) = 2,00,000 + 300x
SO-;
R(x) = 500x
BL-4,
BL-5   P(x) = 200x − 2,00,000
2. Calculate Break-even point (units & ₹) using Formula
- BEP (units) = FC / Contribution
= 2,00,000 / 200 = 1,000 units
- BEP (in ₹) = 1,000 × 500 = ₹5,00,000
3. Find profit at 1,500 units by preparing an income statement
= 200 × 1500 − 2,00,000
= 1,00,000
4. Calculate PV Ratio and Margin of Safety (at 1,800 units)
= 200 / 500 = 40%
5. Draw B-E-P graph (can consider different levels of sales)
To evaluate based on actual graphs prepared
********** 9 **********
--- page 10 ---
CO-2,3;
SO-;   b.   1. Using the dataset provided, perform Correlation Analysis using   [5]
BL-4,
Excel Data Analysis ToolPak.
BL-5
Pesti   Soil
cide   Qua Crop
Fertilizer   Rainf   Irriga   Use   lity   Yield
Used   all   tion   Labor   (liters Inde (tons/
(kg/ha)   (mm) Hours Hours   )   x   ha)
Fertilizer Used
(kg/ha)   1.00
Rainfall (mm)   -0.17   1.00
Irrigation
Hours   0.54   -0.31   1.00
Labor Hours   0.09   -0.29   0.66   1.00
Pesticide Use
(liters)   0.03   -0.48   0.53   0.39   1.00
Soil Quality   1.0
Index   0.55   -0.50   0.75   0.46   0.41   0
Crop Yield   0.7
(tons/ha)   0.74   -0.25   0.91   0.56   0.52   9   1.00
2. Identify: The variable with the strongest and weakest correlation
with Crop Yield (tons/ha)
Irrigation Hours (0.91) → very strong positive relationship with
crop yield
Rainfall (−0.25) → weak (and slightly negative) relationship with
crop yield
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.99
R Square   0.98
Adjusted R
Square   0.94
Standard Error   0.28
Observations   10.00
ANOVA
Significan
df   SS   MS   F   ce F
Regression   6.00   12.37   2.06   26.01   0.01
********** 10 **********
--- page 11 ---
Residual   3.00   0.24   0.08
Total   9.00   12.61
Coefficie Standard   Lower
nts   Error   t Stat   P-value 95%
Intercept   0.24   2.14   0.11   0.92   -6.57
Fertilizer Used
(kg/ha)   0.02   0.00   4.05   0.03   0.00
Rainfall (mm)   0.00   0.00   1.99   0.14   0.00
Irrigation Hours   0.03   0.02   1.59   0.21   -0.03
Labor Hours   0.01   0.01   1.45   0.24   -0.01
Pesticide Use
(liters)   0.08   0.03   2.59   0.08   -0.02
Soil Quality Index   0.34   0.24   1.46   0.24   -0.41
4. Write the estimated regression equation.
Crop Yield = 0.24 + 0.02(Fertilizer) + 0.00(Rainfall) + 0.03(Irrigation)
+ 0.01(Labor) + 0.08(Pesticide) + 0.34(Soil Quality)
5. Interpret ANOVA significance of the model.
• R² (Coefficient of Determination):
• R² = 0.98
• Means 98% of variation in crop yield is explained by the
model → very good fit p-value
• Shows significance of variables
• p < 0.05 → significant
• In your model:
- Fertilizer (0.03) → significant
- Others → not significant
Q7   a.   1. Calculate NPV at 8% using Excel.   [15]
CO-3;   Project A: ₹83.70
SO-;
Project B: ₹6.40
BL-4,
BL-5
2. Calculate IRR.
Project A: ≈ 25.2%
Project B: ≈ 8.93%
Project A is preferred (B fails 10% criterion)
********** 11 **********
--- page 12 ---
3. If required return = 10%, which project is preferable?
Project A is preferred (B fails 10% criterion)
CO-1,2;   b.   Dream Homes Pvt. Ltd. (DH) is a builder company specializing in
SO-;
modern flats.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 6,000
•   Salaries of employees = Rs. 36,000
Each flat requires:
• Land cost = Rs. 60,000
• Construction materials = Rs. 40,000
[5]
• Labour = Rs. 20,000
•   Sales commission = Rs. 5,000 per flat
The selling price of each flat is Rs. 150,000.
Classify the above expenses into Fixed and Variable
Fixed Costs
Rent   8000
Utilities   6000
Salaries   36000
50000
Variable Costs
Land   60000
Construction   40000
Labour   20000
Commission   5000
125000
Income statement
Units sold   1
Sales @ 150000   150000
VC   125000
Contribution   25000
FC   50000
Profit/(Loss)   -25000
********** 12 **********
--- page 13 ---
B-E-P using Goal seek = 2 Houses

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper f22c18ccb8f1

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Civil_7005/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (13 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   What is the difference between a formula and a function in Excel?   [5]
SO- ;
Give one example of each.
BL-2
Solution:
Feature   Formula   Function
A   pre-built   command
A user-created equation
Definition   provided by   Excel   to
to perform calculations.
perform specific tasks.
Created by Microsoft and
Created by   the   user,
cannot be modified by the
Creation   combining operators, cell
user, but can be modified by
references, and constants.
the developer.
Requires a specific syntax,
Does not have a specific
usually in the format of
Syntax   syntax, but must start with
=FUNCTION_NAME(argu
an equals sign (=).
ment1, argument2, ...).
Highly customizable and
Limited to the tasks it was
Flexibility flexible   for   custom
designed for.
calculations.
Can be simple or complex Simplifies   complex
Complexity   depending on the user's operations   and   makes
needs.   calculations more efficient.
********** 1 **********
--- page 2 ---
=SUM(A1:A10) (adds   all
values in the range A1
through A10)
=A1+B1 (adds values in
Example
cells A1 and B1)
Other Eg:
Can   be   SUM,
COUNT,MAX, MIN etc.
CO-2;   b.   Mention Key components of CVP Analysis (any 5)   [5]
SO- ;
BL-4
Solution:
Key Components of CVP Analysis:
• Fixed Costs: Costs that remain constant regardless of the production
or sales volume.
• Variable Costs: Costs that change directly with the production or
sales volume.
• Sales Volume: The number of units sold or produced.
• Selling Price: The price at which each unit is sold.
• Contribution Margin: The difference between the selling price per
unit and the variable cost per unit.
• Break-Even Point: The sales volume at which total revenue equals
total costs, resulting in no profit or loss
CO-2 ;   c.   Explain the purpose of Co-relation analysis.   [5]
SO- ;
Explain the difference between positive and negative correlation.
BL-3
Solution:
To determine the strength and direction of the relationship between two
quantitative variables. Co-relation coefficient measures the strength and
direction of a linear relationship between two variables, ranging from -1
to +1
In a positive correlation, variables move in the same direction (e.g.,
income and expenditure).
In a negative correlation, they move in opposite directions (e.g., price and
demand).
********** 2 **********
--- page 3 ---
CO-2 ;   d.   Net Present Value (NPV) and Internal Rate of Return (IRR) are crucial   [5]
SO- ;
tools for evaluating investment proposals. Please elaborate.
BL-4
Elaborate what is NPV and IRR and how to interpret the outcomes of
each.
Solution
NPV
NPV considers the time value of money by discounting future cash flows
back to their present value. It represents the difference between the
present value of cash inflows and the present value of cash outflows.
Interpretation:
A positive NPV indicates that the investment is likely to be profitable,
while a negative NPV suggests it may not be worthwhile.
IRR
IRR is the discount rate at which the NPV of all cash flows from a project
equals zero. It represents the potential return on investment.
Interpretation:
NPV uses a discount rate to calculate the present value of future cash
flows, while IRR determines the discount rate that makes the NPV equal
to zero.
Q2   a.   1) Define the decision variables   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
2) Formulate the objective function
3) Write all constraints
********** 3 **********
--- page 4 ---
4) Solve the LPP equation and find out the minimum cost using LPP
Solver.
x1 = 1, x2 = 0, x3 = 1, x4 = 1, x5 = 1
Minimum cost Z = 0.73
CO-1,2;
b.   [5]
SO-;
BL-1,
BL-3,   1. Using excel formula, find the average experience of all the employees.
-   5.44 years using the AVERAGE Formula
2. Using excel formula, extract only the employee number from the
Employee ID of Amit.
- = RIGHT(Cell Reference, 3) → E101 →101
3. Using excel formula, create employee label of Neha.
Employee Label comprises of Employee ID followed by
‘-‘ followed by the name of the employee, followed by the Department
in brackets. Eg: “E101-Amit (Sales)”
********** 4 **********
--- page 5 ---
= CONCATE(A3, “-”, B3, “ (“, C3,”)”) → “E102 – Neha (HR)”
4. Using excel Nested-IF function, find out total Sales undertaken by the
Sales Department.
= SUMIF(C3:C27,”Sales”,D3:D27)
= 385000
5. Using appropriate LookUP function, find out the number of units sold
by Tanya.
=VLOOKUP(Tanya,B3:B27,4,FALSE)
= 8
Q3   a.   Decision Tree   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to open a medium sized shop as the
EMV is the highest under that option of $18,000.
CO-2;
SO-;   b.   In an experiment of dice roll, A dice is rolled 30 times.   [5]
BL-4,   Probability of rolling a “6” = 1/6.
BL-5
********** 5 **********

[Text in pictures on this page, read by OCR]
Good Market $40,000

Opena 0.3
small shop 0.4 Average Market $20,000

$15,500 9.3 Bad Market -$15,000

ae Good Market $70,000

0.4 Average Market $30,000

Opena
medium-sized shop

Se Bad Market -$50,000

Good Market so
Do not

open a shop

$o

0.4 Average Market $0

0.3 Bad Market
--- page 6 ---
Find
1. Probability of rolling exactly 5 sixes.
=BINOM.DIST(5, 30, 1/6, FALSE) = 0.206
2. Probability of rolling at most 5 sixes.
=BINOM.DIST(5, 30, 1/6, TRUE) = 0.616
3. Probability of rolling atleast 3 sixes
=1 - BINOM.DIST(2, 30, 1/6, TRUE) = 0.8972096263
4. Probability of between 4 and 8 sixes.
=BINOM.DIST.RANGE(30, 1/6, 4, 8)
5. Expected number of sixes.
=30*(1/6) = 5
Q4   a.   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 6 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

~ 7, _f
Dif=%, P(X)=F

Values: 0.15, 0.25, 0.30, 0.20, 0.10

(b) Mean, Variance, SD (6 Marks)
bi fe
p=

“= 3.85
Lif
So fa?
of = Ss _ P= 1.33
hf

o0 =V133=1.15

(c) Excel (4 Marks)

VAR.P = 1.33, STDEV.P = 1.15
VARS = 1.40, STDEV.S = 1.18

(d) Interpretation (2 Marks)

Moderate variation, fairly consistent data
--- page 7 ---
CO-1,2;
SO-;
BL-1;   b.   1. Assign grade using Nested IF (≥80 = A, ≥60 = B, else C).   [5]
BL-3
= IF(B2>=80,"A",IF(B2>=60,"B","C")) → John = B
2. Round Science marks to nearest 10.
=ROUND(C2,-1) = 90
= ROUND(C3,-1) = 90
= ROUND(C4,-1) = 70
= ROUND(C5,-1) = 60
= ROUND(C6,-1) = 40
3. Check if student passed all subjects (upon scoring ≥50) using AND.
=AND(B2>=50,C2>=50,D2>=50) = TRUE
Do this for all students
4. Rank students (ascending) by Math marks.
=RANK(B2,$B$2:$B$6)
Do this for all students
5. Find highest marks for each student.
= MAX (B2:D2)
Do this for all students
Q5   a.   The dataset given below contains banking transaction records including   [15]
CO-2,3;   details such as date, Officer Name, Transaction Type, Account Type, and
SO-;
Region. It is used to analyze transaction patterns, workload distribution,
BL-4;
BL-6   and regional banking behaviour.
No. of   Avg.
Account   Transactio   Officer   Transa Amo   Service
Date Region   Branch   Type   n Type   Name   ctions   unt   Rating
(Refer Dataset file for details)
********** 7 **********
--- page 8 ---
1. Create a Pivot Table showing Officer-wise total Number of
Transactions and sort the results from highest to lowest. Based on
the Pivot Table, identify the officer handling the highest workload
[3 Marks]
2. Insert a Pivot Chart comparing Account Type-wise transaction
activity across regions and interpret which account type is most
active and how banking activity differs region-wise. [3 Marks]
3. Create a Pivot Table showing total Number of Transactions by
Transaction Type and insert a Slicer for Region and state a short
conclusion about regional banking behaviour. [4 Marks]
4.
i. VLOOKUP("AI Guide", A2:D6, 4, FALSE)
Answer: 1200
ii. =HLOOKUP("Excel Master", A1:E5, 3, FALSE)
Answer: 25
b.   1. Using Excel, find the probability that the daily production is less   [5]
CO-2;
SO-;   than 850 units.
BL-4;
Less than 850 =NORM.DIST(850,1000,120,TRUE)
BL-5
2. Using Excel, find the probability that the daily production is more
than 1150 units.
More than 1150 =1-NORM.DIST(1150,1000,120,TRUE)
3. Using Excel, determine the proportion of days when production lies
between 900 and 1100 units.
Between 900 and 1100 =NORM.DIST(1100,1000,120,TRUE)-
NORM.DIST(900,1000,120,TRUE)
********** 8 **********
--- page 9 ---
4. Using Excel, find the production level such that only 2% of days
exceed this value.
=NORM.INV(0.98,1000,120)
5. Based on your analysis, comment on whether 850 units is a suitable
minimum production target.
= 1 - NORM.DIST(850,1000,120,TRUE)
Yes, 850 is a suitable minimum production target since the
probability of achieving this target is 89.44% which mean target is
achievable most of the days
Q6   a.   1. Formulate cost, revenue and profit functions   [15]
CO-2,3;   C(x) = 2,00,000 + 300x
SO-;
R(x) = 500x
BL-4,
BL-5   P(x) = 200x − 2,00,000
2. Calculate Break-even point (units & ₹) using Formula
- BEP (units) = FC / Contribution
= 2,00,000 / 200 = 1,000 units
- BEP (in ₹) = 1,000 × 500 = ₹5,00,000
3. Find profit at 1,500 units by preparing an income statement
= 200 × 1500 − 2,00,000
= 1,00,000
4. Calculate PV Ratio and Margin of Safety (at 1,800 units)
= 200 / 500 = 40%
5. Draw B-E-P graph (can consider different levels of sales)
To evaluate based on actual graphs prepared
********** 9 **********
--- page 10 ---
CO-2,3;
SO-;   b.   1. Using the dataset provided, perform Correlation Analysis using   [5]
BL-4,
Excel Data Analysis ToolPak.
BL-5
Pesti   Soil
cide   Qua Crop
Fertilizer   Rainf   Irriga   Use   lity   Yield
Used   all   tion   Labor   (liters Inde (tons/
(kg/ha)   (mm) Hours Hours   )   x   ha)
Fertilizer Used
(kg/ha)   1.00
Rainfall (mm)   -0.17   1.00
Irrigation
Hours   0.54   -0.31   1.00
Labor Hours   0.09   -0.29   0.66   1.00
Pesticide Use
(liters)   0.03   -0.48   0.53   0.39   1.00
Soil Quality   1.0
Index   0.55   -0.50   0.75   0.46   0.41   0
Crop Yield   0.7
(tons/ha)   0.74   -0.25   0.91   0.56   0.52   9   1.00
2. Identify: The variable with the strongest and weakest correlation
with Crop Yield (tons/ha)
Irrigation Hours (0.91) → very strong positive relationship with
crop yield
Rainfall (−0.25) → weak (and slightly negative) relationship with
crop yield
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.99
R Square   0.98
Adjusted R
Square   0.94
Standard Error   0.28
Observations   10.00
ANOVA
Significan
df   SS   MS   F   ce F
Regression   6.00   12.37   2.06   26.01   0.01
********** 10 **********
--- page 11 ---
Residual   3.00   0.24   0.08
Total   9.00   12.61
Coefficie Standard   Lower
nts   Error   t Stat   P-value 95%
Intercept   0.24   2.14   0.11   0.92   -6.57
Fertilizer Used
(kg/ha)   0.02   0.00   4.05   0.03   0.00
Rainfall (mm)   0.00   0.00   1.99   0.14   0.00
Irrigation Hours   0.03   0.02   1.59   0.21   -0.03
Labor Hours   0.01   0.01   1.45   0.24   -0.01
Pesticide Use
(liters)   0.08   0.03   2.59   0.08   -0.02
Soil Quality Index   0.34   0.24   1.46   0.24   -0.41
4. Write the estimated regression equation.
Crop Yield = 0.24 + 0.02(Fertilizer) + 0.00(Rainfall) + 0.03(Irrigation)
+ 0.01(Labor) + 0.08(Pesticide) + 0.34(Soil Quality)
5. Interpret ANOVA significance of the model.
• R² (Coefficient of Determination):
• R² = 0.98
• Means 98% of variation in crop yield is explained by the
model → very good fit p-value
• Shows significance of variables
• p < 0.05 → significant
• In your model:
- Fertilizer (0.03) → significant
- Others → not significant
Q7   a.   1. Calculate NPV at 8% using Excel.   [15]
CO-3;   Project A: ₹83.70
SO-;
Project B: ₹6.40
BL-4,
BL-5
2. Calculate IRR.
Project A: ≈ 25.2%
Project B: ≈ 8.93%
Project A is preferred (B fails 10% criterion)
********** 11 **********
--- page 12 ---
3. If required return = 10%, which project is preferable?
Project A is preferred (B fails 10% criterion)
CO-1,2;   b.   Dream Homes Pvt. Ltd. (DH) is a builder company specializing in
SO-;
modern flats.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 6,000
•   Salaries of employees = Rs. 36,000
Each flat requires:
• Land cost = Rs. 60,000
• Construction materials = Rs. 40,000
[5]
• Labour = Rs. 20,000
•   Sales commission = Rs. 5,000 per flat
The selling price of each flat is Rs. 150,000.
Classify the above expenses into Fixed and Variable
Fixed Costs
Rent   8000
Utilities   6000
Salaries   36000
50000
Variable Costs
Land   60000
Construction   40000
Labour   20000
Commission   5000
125000
Income statement
Units sold   1
Sales @ 150000   150000
VC   125000
Contribution   25000
FC   50000
Profit/(Loss)   -25000
********** 12 **********
--- page 13 ---
B-E-P using Goal seek = 2 Houses

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper a7e8f6a0ffe6

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (13 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   What is the difference between a formula and a function in Excel?   [5]
SO- ;
Give one example of each.
BL-2
Solution:
Feature   Formula   Function
A   pre-built   command
A user-created equation
Definition   provided by   Excel   to
to perform calculations.
perform specific tasks.
Created by Microsoft and
Created by   the   user,
cannot be modified by the
Creation   combining operators, cell
user, but can be modified by
references, and constants.
the developer.
Requires a specific syntax,
Does not have a specific
usually in the format of
Syntax   syntax, but must start with
=FUNCTION_NAME(argu
an equals sign (=).
ment1, argument2, ...).
Highly customizable and
Limited to the tasks it was
Flexibility flexible   for   custom
designed for.
calculations.
Can be simple or complex Simplifies   complex
Complexity   depending on the user's operations   and   makes
needs.   calculations more efficient.
********** 1 **********
--- page 2 ---
=SUM(A1:A10) (adds   all
values in the range A1
through A10)
=A1+B1 (adds values in
Example
cells A1 and B1)
Other Eg:
Can   be   SUM,
COUNT,MAX, MIN etc.
CO-2;   b.   Mention Key components of CVP Analysis (any 5)   [5]
SO- ;
BL-4
Solution:
Key Components of CVP Analysis:
• Fixed Costs: Costs that remain constant regardless of the production
or sales volume.
• Variable Costs: Costs that change directly with the production or
sales volume.
• Sales Volume: The number of units sold or produced.
• Selling Price: The price at which each unit is sold.
• Contribution Margin: The difference between the selling price per
unit and the variable cost per unit.
• Break-Even Point: The sales volume at which total revenue equals
total costs, resulting in no profit or loss
CO-2 ;   c.   Explain the purpose of Co-relation analysis.   [5]
SO- ;
Explain the difference between positive and negative correlation.
BL-3
Solution:
To determine the strength and direction of the relationship between two
quantitative variables. Co-relation coefficient measures the strength and
direction of a linear relationship between two variables, ranging from -1
to +1
In a positive correlation, variables move in the same direction (e.g.,
income and expenditure).
In a negative correlation, they move in opposite directions (e.g., price and
demand).
********** 2 **********
--- page 3 ---
CO-2 ;   d.   Net Present Value (NPV) and Internal Rate of Return (IRR) are crucial   [5]
SO- ;
tools for evaluating investment proposals. Please elaborate.
BL-4
Elaborate what is NPV and IRR and how to interpret the outcomes of
each.
Solution
NPV
NPV considers the time value of money by discounting future cash flows
back to their present value. It represents the difference between the
present value of cash inflows and the present value of cash outflows.
Interpretation:
A positive NPV indicates that the investment is likely to be profitable,
while a negative NPV suggests it may not be worthwhile.
IRR
IRR is the discount rate at which the NPV of all cash flows from a project
equals zero. It represents the potential return on investment.
Interpretation:
NPV uses a discount rate to calculate the present value of future cash
flows, while IRR determines the discount rate that makes the NPV equal
to zero.
Q2   a.   1) Define the decision variables   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
2) Formulate the objective function
3) Write all constraints
********** 3 **********
--- page 4 ---
4) Solve the LPP equation and find out the minimum cost using LPP
Solver.
x1 = 1, x2 = 0, x3 = 1, x4 = 1, x5 = 1
Minimum cost Z = 0.73
CO-1,2;
b.   [5]
SO-;
BL-1,
BL-3,   1. Using excel formula, find the average experience of all the employees.
-   5.44 years using the AVERAGE Formula
2. Using excel formula, extract only the employee number from the
Employee ID of Amit.
- = RIGHT(Cell Reference, 3) → E101 →101
3. Using excel formula, create employee label of Neha.
Employee Label comprises of Employee ID followed by
‘-‘ followed by the name of the employee, followed by the Department
in brackets. Eg: “E101-Amit (Sales)”
********** 4 **********
--- page 5 ---
= CONCATE(A3, “-”, B3, “ (“, C3,”)”) → “E102 – Neha (HR)”
4. Using excel Nested-IF function, find out total Sales undertaken by the
Sales Department.
= SUMIF(C3:C27,”Sales”,D3:D27)
= 385000
5. Using appropriate LookUP function, find out the number of units sold
by Tanya.
=VLOOKUP(Tanya,B3:B27,4,FALSE)
= 8
Q3   a.   Decision Tree   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to open a medium sized shop as the
EMV is the highest under that option of $18,000.
CO-2;
SO-;   b.   In an experiment of dice roll, A dice is rolled 30 times.   [5]
BL-4,   Probability of rolling a “6” = 1/6.
BL-5
********** 5 **********

[Text in pictures on this page, read by OCR]
Good Market $40,000

Opena 0.3
small shop 0.4 Average Market $20,000

$15,500 9.3 Bad Market -$15,000

ae Good Market $70,000

0.4 Average Market $30,000

Opena
medium-sized shop

Se Bad Market -$50,000

Good Market so
Do not

open a shop

$o

0.4 Average Market $0

0.3 Bad Market
--- page 6 ---
Find
1. Probability of rolling exactly 5 sixes.
=BINOM.DIST(5, 30, 1/6, FALSE) = 0.206
2. Probability of rolling at most 5 sixes.
=BINOM.DIST(5, 30, 1/6, TRUE) = 0.616
3. Probability of rolling atleast 3 sixes
=1 - BINOM.DIST(2, 30, 1/6, TRUE) = 0.8972096263
4. Probability of between 4 and 8 sixes.
=BINOM.DIST.RANGE(30, 1/6, 4, 8)
5. Expected number of sixes.
=30*(1/6) = 5
Q4   a.   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 6 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

~ 7, _f
Dif=%, P(X)=F

Values: 0.15, 0.25, 0.30, 0.20, 0.10

(b) Mean, Variance, SD (6 Marks)
bi fe
p=

“= 3.85
Lif
So fa?
of = Ss _ P= 1.33
hf

o0 =V133=1.15

(c) Excel (4 Marks)

VAR.P = 1.33, STDEV.P = 1.15
VARS = 1.40, STDEV.S = 1.18

(d) Interpretation (2 Marks)

Moderate variation, fairly consistent data
--- page 7 ---
CO-1,2;
SO-;
BL-1;   b.   1. Assign grade using Nested IF (≥80 = A, ≥60 = B, else C).   [5]
BL-3
= IF(B2>=80,"A",IF(B2>=60,"B","C")) → John = B
2. Round Science marks to nearest 10.
=ROUND(C2,-1) = 90
= ROUND(C3,-1) = 90
= ROUND(C4,-1) = 70
= ROUND(C5,-1) = 60
= ROUND(C6,-1) = 40
3. Check if student passed all subjects (upon scoring ≥50) using AND.
=AND(B2>=50,C2>=50,D2>=50) = TRUE
Do this for all students
4. Rank students (ascending) by Math marks.
=RANK(B2,$B$2:$B$6)
Do this for all students
5. Find highest marks for each student.
= MAX (B2:D2)
Do this for all students
Q5   a.   The dataset given below contains banking transaction records including   [15]
CO-2,3;   details such as date, Officer Name, Transaction Type, Account Type, and
SO-;
Region. It is used to analyze transaction patterns, workload distribution,
BL-4;
BL-6   and regional banking behaviour.
No. of   Avg.
Account   Transactio   Officer   Transa Amo   Service
Date Region   Branch   Type   n Type   Name   ctions   unt   Rating
(Refer Dataset file for details)
********** 7 **********
--- page 8 ---
1. Create a Pivot Table showing Officer-wise total Number of
Transactions and sort the results from highest to lowest. Based on
the Pivot Table, identify the officer handling the highest workload
[3 Marks]
2. Insert a Pivot Chart comparing Account Type-wise transaction
activity across regions and interpret which account type is most
active and how banking activity differs region-wise. [3 Marks]
3. Create a Pivot Table showing total Number of Transactions by
Transaction Type and insert a Slicer for Region and state a short
conclusion about regional banking behaviour. [4 Marks]
4.
i. VLOOKUP("AI Guide", A2:D6, 4, FALSE)
Answer: 1200
ii. =HLOOKUP("Excel Master", A1:E5, 3, FALSE)
Answer: 25
b.   1. Using Excel, find the probability that the daily production is less   [5]
CO-2;
SO-;   than 850 units.
BL-4;
Less than 850 =NORM.DIST(850,1000,120,TRUE)
BL-5
2. Using Excel, find the probability that the daily production is more
than 1150 units.
More than 1150 =1-NORM.DIST(1150,1000,120,TRUE)
3. Using Excel, determine the proportion of days when production lies
between 900 and 1100 units.
Between 900 and 1100 =NORM.DIST(1100,1000,120,TRUE)-
NORM.DIST(900,1000,120,TRUE)
********** 8 **********
--- page 9 ---
4. Using Excel, find the production level such that only 2% of days
exceed this value.
=NORM.INV(0.98,1000,120)
5. Based on your analysis, comment on whether 850 units is a suitable
minimum production target.
= 1 - NORM.DIST(850,1000,120,TRUE)
Yes, 850 is a suitable minimum production target since the
probability of achieving this target is 89.44% which mean target is
achievable most of the days
Q6   a.   1. Formulate cost, revenue and profit functions   [15]
CO-2,3;   C(x) = 2,00,000 + 300x
SO-;
R(x) = 500x
BL-4,
BL-5   P(x) = 200x − 2,00,000
2. Calculate Break-even point (units & ₹) using Formula
- BEP (units) = FC / Contribution
= 2,00,000 / 200 = 1,000 units
- BEP (in ₹) = 1,000 × 500 = ₹5,00,000
3. Find profit at 1,500 units by preparing an income statement
= 200 × 1500 − 2,00,000
= 1,00,000
4. Calculate PV Ratio and Margin of Safety (at 1,800 units)
= 200 / 500 = 40%
5. Draw B-E-P graph (can consider different levels of sales)
To evaluate based on actual graphs prepared
********** 9 **********
--- page 10 ---
CO-2,3;
SO-;   b.   1. Using the dataset provided, perform Correlation Analysis using   [5]
BL-4,
Excel Data Analysis ToolPak.
BL-5
Pesti   Soil
cide   Qua Crop
Fertilizer   Rainf   Irriga   Use   lity   Yield
Used   all   tion   Labor   (liters Inde (tons/
(kg/ha)   (mm) Hours Hours   )   x   ha)
Fertilizer Used
(kg/ha)   1.00
Rainfall (mm)   -0.17   1.00
Irrigation
Hours   0.54   -0.31   1.00
Labor Hours   0.09   -0.29   0.66   1.00
Pesticide Use
(liters)   0.03   -0.48   0.53   0.39   1.00
Soil Quality   1.0
Index   0.55   -0.50   0.75   0.46   0.41   0
Crop Yield   0.7
(tons/ha)   0.74   -0.25   0.91   0.56   0.52   9   1.00
2. Identify: The variable with the strongest and weakest correlation
with Crop Yield (tons/ha)
Irrigation Hours (0.91) → very strong positive relationship with
crop yield
Rainfall (−0.25) → weak (and slightly negative) relationship with
crop yield
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.99
R Square   0.98
Adjusted R
Square   0.94
Standard Error   0.28
Observations   10.00
ANOVA
Significan
df   SS   MS   F   ce F
Regression   6.00   12.37   2.06   26.01   0.01
********** 10 **********
--- page 11 ---
Residual   3.00   0.24   0.08
Total   9.00   12.61
Coefficie Standard   Lower
nts   Error   t Stat   P-value 95%
Intercept   0.24   2.14   0.11   0.92   -6.57
Fertilizer Used
(kg/ha)   0.02   0.00   4.05   0.03   0.00
Rainfall (mm)   0.00   0.00   1.99   0.14   0.00
Irrigation Hours   0.03   0.02   1.59   0.21   -0.03
Labor Hours   0.01   0.01   1.45   0.24   -0.01
Pesticide Use
(liters)   0.08   0.03   2.59   0.08   -0.02
Soil Quality Index   0.34   0.24   1.46   0.24   -0.41
4. Write the estimated regression equation.
Crop Yield = 0.24 + 0.02(Fertilizer) + 0.00(Rainfall) + 0.03(Irrigation)
+ 0.01(Labor) + 0.08(Pesticide) + 0.34(Soil Quality)
5. Interpret ANOVA significance of the model.
• R² (Coefficient of Determination):
• R² = 0.98
• Means 98% of variation in crop yield is explained by the
model → very good fit p-value
• Shows significance of variables
• p < 0.05 → significant
• In your model:
- Fertilizer (0.03) → significant
- Others → not significant
Q7   a.   1. Calculate NPV at 8% using Excel.   [15]
CO-3;   Project A: ₹83.70
SO-;
Project B: ₹6.40
BL-4,
BL-5
2. Calculate IRR.
Project A: ≈ 25.2%
Project B: ≈ 8.93%
Project A is preferred (B fails 10% criterion)
********** 11 **********
--- page 12 ---
3. If required return = 10%, which project is preferable?
Project A is preferred (B fails 10% criterion)
CO-1,2;   b.   Dream Homes Pvt. Ltd. (DH) is a builder company specializing in
SO-;
modern flats.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 6,000
•   Salaries of employees = Rs. 36,000
Each flat requires:
• Land cost = Rs. 60,000
• Construction materials = Rs. 40,000
[5]
• Labour = Rs. 20,000
•   Sales commission = Rs. 5,000 per flat
The selling price of each flat is Rs. 150,000.
Classify the above expenses into Fixed and Variable
Fixed Costs
Rent   8000
Utilities   6000
Salaries   36000
50000
Variable Costs
Land   60000
Construction   40000
Labour   20000
Commission   5000
125000
Income statement
Units sold   1
Sales @ 150000   150000
VC   125000
Contribution   25000
FC   50000
Profit/(Loss)   -25000
********** 12 **********
--- page 13 ---
B-E-P using Goal seek = 2 Houses

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 2734d185c45c

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (13 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   What is the difference between a formula and a function in Excel?   [5]
SO- ;
Give one example of each.
BL-2
Solution:
Feature   Formula   Function
A   pre-built   command
A user-created equation
Definition   provided by   Excel   to
to perform calculations.
perform specific tasks.
Created by Microsoft and
Created by   the   user,
cannot be modified by the
Creation   combining operators, cell
user, but can be modified by
references, and constants.
the developer.
Requires a specific syntax,
Does not have a specific
usually in the format of
Syntax   syntax, but must start with
=FUNCTION_NAME(argu
an equals sign (=).
ment1, argument2, ...).
Highly customizable and
Limited to the tasks it was
Flexibility flexible   for   custom
designed for.
calculations.
Can be simple or complex Simplifies   complex
Complexity   depending on the user's operations   and   makes
needs.   calculations more efficient.
********** 1 **********
--- page 2 ---
=SUM(A1:A10) (adds   all
values in the range A1
through A10)
=A1+B1 (adds values in
Example
cells A1 and B1)
Other Eg:
Can   be   SUM,
COUNT,MAX, MIN etc.
CO-2;   b.   Mention Key components of CVP Analysis (any 5)   [5]
SO- ;
BL-4
Solution:
Key Components of CVP Analysis:
• Fixed Costs: Costs that remain constant regardless of the production
or sales volume.
• Variable Costs: Costs that change directly with the production or
sales volume.
• Sales Volume: The number of units sold or produced.
• Selling Price: The price at which each unit is sold.
• Contribution Margin: The difference between the selling price per
unit and the variable cost per unit.
• Break-Even Point: The sales volume at which total revenue equals
total costs, resulting in no profit or loss
CO-2 ;   c.   Explain the purpose of Co-relation analysis.   [5]
SO- ;
Explain the difference between positive and negative correlation.
BL-3
Solution:
To determine the strength and direction of the relationship between two
quantitative variables. Co-relation coefficient measures the strength and
direction of a linear relationship between two variables, ranging from -1
to +1
In a positive correlation, variables move in the same direction (e.g.,
income and expenditure).
In a negative correlation, they move in opposite directions (e.g., price and
demand).
********** 2 **********
--- page 3 ---
CO-2 ;   d.   Net Present Value (NPV) and Internal Rate of Return (IRR) are crucial   [5]
SO- ;
tools for evaluating investment proposals. Please elaborate.
BL-4
Elaborate what is NPV and IRR and how to interpret the outcomes of
each.
Solution
NPV
NPV considers the time value of money by discounting future cash flows
back to their present value. It represents the difference between the
present value of cash inflows and the present value of cash outflows.
Interpretation:
A positive NPV indicates that the investment is likely to be profitable,
while a negative NPV suggests it may not be worthwhile.
IRR
IRR is the discount rate at which the NPV of all cash flows from a project
equals zero. It represents the potential return on investment.
Interpretation:
NPV uses a discount rate to calculate the present value of future cash
flows, while IRR determines the discount rate that makes the NPV equal
to zero.
Q2   a.   1) Define the decision variables   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
2) Formulate the objective function
3) Write all constraints
********** 3 **********
--- page 4 ---
4) Solve the LPP equation and find out the minimum cost using LPP
Solver.
x1 = 1, x2 = 0, x3 = 1, x4 = 1, x5 = 1
Minimum cost Z = 0.73
CO-1,2;
b.   [5]
SO-;
BL-1,
BL-3,   1. Using excel formula, find the average experience of all the employees.
-   5.44 years using the AVERAGE Formula
2. Using excel formula, extract only the employee number from the
Employee ID of Amit.
- = RIGHT(Cell Reference, 3) → E101 →101
3. Using excel formula, create employee label of Neha.
Employee Label comprises of Employee ID followed by
‘-‘ followed by the name of the employee, followed by the Department
in brackets. Eg: “E101-Amit (Sales)”
********** 4 **********
--- page 5 ---
= CONCATE(A3, “-”, B3, “ (“, C3,”)”) → “E102 – Neha (HR)”
4. Using excel Nested-IF function, find out total Sales undertaken by the
Sales Department.
= SUMIF(C3:C27,”Sales”,D3:D27)
= 385000
5. Using appropriate LookUP function, find out the number of units sold
by Tanya.
=VLOOKUP(Tanya,B3:B27,4,FALSE)
= 8
Q3   a.   Decision Tree   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to open a medium sized shop as the
EMV is the highest under that option of $18,000.
CO-2;
SO-;   b.   In an experiment of dice roll, A dice is rolled 30 times.   [5]
BL-4,   Probability of rolling a “6” = 1/6.
BL-5
********** 5 **********

[Text in pictures on this page, read by OCR]
Good Market $40,000

Opena 0.3
small shop 0.4 Average Market $20,000

$15,500 9.3 Bad Market -$15,000

ae Good Market $70,000

0.4 Average Market $30,000

Opena
medium-sized shop

Se Bad Market -$50,000

Good Market so
Do not

open a shop

$o

0.4 Average Market $0

0.3 Bad Market
--- page 6 ---
Find
1. Probability of rolling exactly 5 sixes.
=BINOM.DIST(5, 30, 1/6, FALSE) = 0.206
2. Probability of rolling at most 5 sixes.
=BINOM.DIST(5, 30, 1/6, TRUE) = 0.616
3. Probability of rolling atleast 3 sixes
=1 - BINOM.DIST(2, 30, 1/6, TRUE) = 0.8972096263
4. Probability of between 4 and 8 sixes.
=BINOM.DIST.RANGE(30, 1/6, 4, 8)
5. Expected number of sixes.
=30*(1/6) = 5
Q4   a.   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 6 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

~ 7, _f
Dif=%, P(X)=F

Values: 0.15, 0.25, 0.30, 0.20, 0.10

(b) Mean, Variance, SD (6 Marks)
bi fe
p=

“= 3.85
Lif
So fa?
of = Ss _ P= 1.33
hf

o0 =V133=1.15

(c) Excel (4 Marks)

VAR.P = 1.33, STDEV.P = 1.15
VARS = 1.40, STDEV.S = 1.18

(d) Interpretation (2 Marks)

Moderate variation, fairly consistent data
--- page 7 ---
CO-1,2;
SO-;
BL-1;   b.   1. Assign grade using Nested IF (≥80 = A, ≥60 = B, else C).   [5]
BL-3
= IF(B2>=80,"A",IF(B2>=60,"B","C")) → John = B
2. Round Science marks to nearest 10.
=ROUND(C2,-1) = 90
= ROUND(C3,-1) = 90
= ROUND(C4,-1) = 70
= ROUND(C5,-1) = 60
= ROUND(C6,-1) = 40
3. Check if student passed all subjects (upon scoring ≥50) using AND.
=AND(B2>=50,C2>=50,D2>=50) = TRUE
Do this for all students
4. Rank students (ascending) by Math marks.
=RANK(B2,$B$2:$B$6)
Do this for all students
5. Find highest marks for each student.
= MAX (B2:D2)
Do this for all students
Q5   a.   The dataset given below contains banking transaction records including   [15]
CO-2,3;   details such as date, Officer Name, Transaction Type, Account Type, and
SO-;
Region. It is used to analyze transaction patterns, workload distribution,
BL-4;
BL-6   and regional banking behaviour.
No. of   Avg.
Account   Transactio   Officer   Transa Amo   Service
Date Region   Branch   Type   n Type   Name   ctions   unt   Rating
(Refer Dataset file for details)
********** 7 **********
--- page 8 ---
1. Create a Pivot Table showing Officer-wise total Number of
Transactions and sort the results from highest to lowest. Based on
the Pivot Table, identify the officer handling the highest workload
[3 Marks]
2. Insert a Pivot Chart comparing Account Type-wise transaction
activity across regions and interpret which account type is most
active and how banking activity differs region-wise. [3 Marks]
3. Create a Pivot Table showing total Number of Transactions by
Transaction Type and insert a Slicer for Region and state a short
conclusion about regional banking behaviour. [4 Marks]
4.
i. VLOOKUP("AI Guide", A2:D6, 4, FALSE)
Answer: 1200
ii. =HLOOKUP("Excel Master", A1:E5, 3, FALSE)
Answer: 25
b.   1. Using Excel, find the probability that the daily production is less   [5]
CO-2;
SO-;   than 850 units.
BL-4;
Less than 850 =NORM.DIST(850,1000,120,TRUE)
BL-5
2. Using Excel, find the probability that the daily production is more
than 1150 units.
More than 1150 =1-NORM.DIST(1150,1000,120,TRUE)
3. Using Excel, determine the proportion of days when production lies
between 900 and 1100 units.
Between 900 and 1100 =NORM.DIST(1100,1000,120,TRUE)-
NORM.DIST(900,1000,120,TRUE)
********** 8 **********
--- page 9 ---
4. Using Excel, find the production level such that only 2% of days
exceed this value.
=NORM.INV(0.98,1000,120)
5. Based on your analysis, comment on whether 850 units is a suitable
minimum production target.
= 1 - NORM.DIST(850,1000,120,TRUE)
Yes, 850 is a suitable minimum production target since the
probability of achieving this target is 89.44% which mean target is
achievable most of the days
Q6   a.   1. Formulate cost, revenue and profit functions   [15]
CO-2,3;   C(x) = 2,00,000 + 300x
SO-;
R(x) = 500x
BL-4,
BL-5   P(x) = 200x − 2,00,000
2. Calculate Break-even point (units & ₹) using Formula
- BEP (units) = FC / Contribution
= 2,00,000 / 200 = 1,000 units
- BEP (in ₹) = 1,000 × 500 = ₹5,00,000
3. Find profit at 1,500 units by preparing an income statement
= 200 × 1500 − 2,00,000
= 1,00,000
4. Calculate PV Ratio and Margin of Safety (at 1,800 units)
= 200 / 500 = 40%
5. Draw B-E-P graph (can consider different levels of sales)
To evaluate based on actual graphs prepared
********** 9 **********
--- page 10 ---
CO-2,3;
SO-;   b.   1. Using the dataset provided, perform Correlation Analysis using   [5]
BL-4,
Excel Data Analysis ToolPak.
BL-5
Pesti   Soil
cide   Qua Crop
Fertilizer   Rainf   Irriga   Use   lity   Yield
Used   all   tion   Labor   (liters Inde (tons/
(kg/ha)   (mm) Hours Hours   )   x   ha)
Fertilizer Used
(kg/ha)   1.00
Rainfall (mm)   -0.17   1.00
Irrigation
Hours   0.54   -0.31   1.00
Labor Hours   0.09   -0.29   0.66   1.00
Pesticide Use
(liters)   0.03   -0.48   0.53   0.39   1.00
Soil Quality   1.0
Index   0.55   -0.50   0.75   0.46   0.41   0
Crop Yield   0.7
(tons/ha)   0.74   -0.25   0.91   0.56   0.52   9   1.00
2. Identify: The variable with the strongest and weakest correlation
with Crop Yield (tons/ha)
Irrigation Hours (0.91) → very strong positive relationship with
crop yield
Rainfall (−0.25) → weak (and slightly negative) relationship with
crop yield
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.99
R Square   0.98
Adjusted R
Square   0.94
Standard Error   0.28
Observations   10.00
ANOVA
Significan
df   SS   MS   F   ce F
Regression   6.00   12.37   2.06   26.01   0.01
********** 10 **********
--- page 11 ---
Residual   3.00   0.24   0.08
Total   9.00   12.61
Coefficie Standard   Lower
nts   Error   t Stat   P-value 95%
Intercept   0.24   2.14   0.11   0.92   -6.57
Fertilizer Used
(kg/ha)   0.02   0.00   4.05   0.03   0.00
Rainfall (mm)   0.00   0.00   1.99   0.14   0.00
Irrigation Hours   0.03   0.02   1.59   0.21   -0.03
Labor Hours   0.01   0.01   1.45   0.24   -0.01
Pesticide Use
(liters)   0.08   0.03   2.59   0.08   -0.02
Soil Quality Index   0.34   0.24   1.46   0.24   -0.41
4. Write the estimated regression equation.
Crop Yield = 0.24 + 0.02(Fertilizer) + 0.00(Rainfall) + 0.03(Irrigation)
+ 0.01(Labor) + 0.08(Pesticide) + 0.34(Soil Quality)
5. Interpret ANOVA significance of the model.
• R² (Coefficient of Determination):
• R² = 0.98
• Means 98% of variation in crop yield is explained by the
model → very good fit p-value
• Shows significance of variables
• p < 0.05 → significant
• In your model:
- Fertilizer (0.03) → significant
- Others → not significant
Q7   a.   1. Calculate NPV at 8% using Excel.   [15]
CO-3;   Project A: ₹83.70
SO-;
Project B: ₹6.40
BL-4,
BL-5
2. Calculate IRR.
Project A: ≈ 25.2%
Project B: ≈ 8.93%
Project A is preferred (B fails 10% criterion)
********** 11 **********
--- page 12 ---
3. If required return = 10%, which project is preferable?
Project A is preferred (B fails 10% criterion)
CO-1,2;   b.   Dream Homes Pvt. Ltd. (DH) is a builder company specializing in
SO-;
modern flats.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 6,000
•   Salaries of employees = Rs. 36,000
Each flat requires:
• Land cost = Rs. 60,000
• Construction materials = Rs. 40,000
[5]
• Labour = Rs. 20,000
•   Sales commission = Rs. 5,000 per flat
The selling price of each flat is Rs. 150,000.
Classify the above expenses into Fixed and Variable
Fixed Costs
Rent   8000
Utilities   6000
Salaries   36000
50000
Variable Costs
Land   60000
Construction   40000
Labour   20000
Commission   5000
125000
Income statement
Units sold   1
Sales @ 150000   150000
VC   125000
Contribution   25000
FC   50000
Profit/(Loss)   -25000
********** 12 **********
--- page 13 ---
B-E-P using Goal seek = 2 Houses

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 0325deb4f95f

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_DS_7009/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (13 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   What is the difference between a formula and a function in Excel?   [5]
SO- ;
Give one example of each.
BL-2
Solution:
Feature   Formula   Function
A   pre-built   command
A user-created equation
Definition   provided by   Excel   to
to perform calculations.
perform specific tasks.
Created by Microsoft and
Created by   the   user,
cannot be modified by the
Creation   combining operators, cell
user, but can be modified by
references, and constants.
the developer.
Requires a specific syntax,
Does not have a specific
usually in the format of
Syntax   syntax, but must start with
=FUNCTION_NAME(argu
an equals sign (=).
ment1, argument2, ...).
Highly customizable and
Limited to the tasks it was
Flexibility flexible   for   custom
designed for.
calculations.
Can be simple or complex Simplifies   complex
Complexity   depending on the user's operations   and   makes
needs.   calculations more efficient.
********** 1 **********
--- page 2 ---
=SUM(A1:A10) (adds   all
values in the range A1
through A10)
=A1+B1 (adds values in
Example
cells A1 and B1)
Other Eg:
Can   be   SUM,
COUNT,MAX, MIN etc.
CO-2;   b.   Mention Key components of CVP Analysis (any 5)   [5]
SO- ;
BL-4
Solution:
Key Components of CVP Analysis:
• Fixed Costs: Costs that remain constant regardless of the production
or sales volume.
• Variable Costs: Costs that change directly with the production or
sales volume.
• Sales Volume: The number of units sold or produced.
• Selling Price: The price at which each unit is sold.
• Contribution Margin: The difference between the selling price per
unit and the variable cost per unit.
• Break-Even Point: The sales volume at which total revenue equals
total costs, resulting in no profit or loss
CO-2 ;   c.   Explain the purpose of Co-relation analysis.   [5]
SO- ;
Explain the difference between positive and negative correlation.
BL-3
Solution:
To determine the strength and direction of the relationship between two
quantitative variables. Co-relation coefficient measures the strength and
direction of a linear relationship between two variables, ranging from -1
to +1
In a positive correlation, variables move in the same direction (e.g.,
income and expenditure).
In a negative correlation, they move in opposite directions (e.g., price and
demand).
********** 2 **********
--- page 3 ---
CO-2 ;   d.   Net Present Value (NPV) and Internal Rate of Return (IRR) are crucial   [5]
SO- ;
tools for evaluating investment proposals. Please elaborate.
BL-4
Elaborate what is NPV and IRR and how to interpret the outcomes of
each.
Solution
NPV
NPV considers the time value of money by discounting future cash flows
back to their present value. It represents the difference between the
present value of cash inflows and the present value of cash outflows.
Interpretation:
A positive NPV indicates that the investment is likely to be profitable,
while a negative NPV suggests it may not be worthwhile.
IRR
IRR is the discount rate at which the NPV of all cash flows from a project
equals zero. It represents the potential return on investment.
Interpretation:
NPV uses a discount rate to calculate the present value of future cash
flows, while IRR determines the discount rate that makes the NPV equal
to zero.
Q2   a.   1) Define the decision variables   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
2) Formulate the objective function
3) Write all constraints
********** 3 **********
--- page 4 ---
4) Solve the LPP equation and find out the minimum cost using LPP
Solver.
x1 = 1, x2 = 0, x3 = 1, x4 = 1, x5 = 1
Minimum cost Z = 0.73
CO-1,2;
b.   [5]
SO-;
BL-1,
BL-3,   1. Using excel formula, find the average experience of all the employees.
-   5.44 years using the AVERAGE Formula
2. Using excel formula, extract only the employee number from the
Employee ID of Amit.
- = RIGHT(Cell Reference, 3) → E101 →101
3. Using excel formula, create employee label of Neha.
Employee Label comprises of Employee ID followed by
‘-‘ followed by the name of the employee, followed by the Department
in brackets. Eg: “E101-Amit (Sales)”
********** 4 **********
--- page 5 ---
= CONCATE(A3, “-”, B3, “ (“, C3,”)”) → “E102 – Neha (HR)”
4. Using excel Nested-IF function, find out total Sales undertaken by the
Sales Department.
= SUMIF(C3:C27,”Sales”,D3:D27)
= 385000
5. Using appropriate LookUP function, find out the number of units sold
by Tanya.
=VLOOKUP(Tanya,B3:B27,4,FALSE)
= 8
Q3   a.   Decision Tree   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to open a medium sized shop as the
EMV is the highest under that option of $18,000.
CO-2;
SO-;   b.   In an experiment of dice roll, A dice is rolled 30 times.   [5]
BL-4,   Probability of rolling a “6” = 1/6.
BL-5
********** 5 **********

[Text in pictures on this page, read by OCR]
Good Market $40,000

Opena 0.3
small shop 0.4 Average Market $20,000

$15,500 9.3 Bad Market -$15,000

ae Good Market $70,000

0.4 Average Market $30,000

Opena
medium-sized shop

Se Bad Market -$50,000

Good Market so
Do not

open a shop

$o

0.4 Average Market $0

0.3 Bad Market
--- page 6 ---
Find
1. Probability of rolling exactly 5 sixes.
=BINOM.DIST(5, 30, 1/6, FALSE) = 0.206
2. Probability of rolling at most 5 sixes.
=BINOM.DIST(5, 30, 1/6, TRUE) = 0.616
3. Probability of rolling atleast 3 sixes
=1 - BINOM.DIST(2, 30, 1/6, TRUE) = 0.8972096263
4. Probability of between 4 and 8 sixes.
=BINOM.DIST.RANGE(30, 1/6, 4, 8)
5. Expected number of sixes.
=30*(1/6) = 5
Q4   a.   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 6 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

~ 7, _f
Dif=%, P(X)=F

Values: 0.15, 0.25, 0.30, 0.20, 0.10

(b) Mean, Variance, SD (6 Marks)
bi fe
p=

“= 3.85
Lif
So fa?
of = Ss _ P= 1.33
hf

o0 =V133=1.15

(c) Excel (4 Marks)

VAR.P = 1.33, STDEV.P = 1.15
VARS = 1.40, STDEV.S = 1.18

(d) Interpretation (2 Marks)

Moderate variation, fairly consistent data
--- page 7 ---
CO-1,2;
SO-;
BL-1;   b.   1. Assign grade using Nested IF (≥80 = A, ≥60 = B, else C).   [5]
BL-3
= IF(B2>=80,"A",IF(B2>=60,"B","C")) → John = B
2. Round Science marks to nearest 10.
=ROUND(C2,-1) = 90
= ROUND(C3,-1) = 90
= ROUND(C4,-1) = 70
= ROUND(C5,-1) = 60
= ROUND(C6,-1) = 40
3. Check if student passed all subjects (upon scoring ≥50) using AND.
=AND(B2>=50,C2>=50,D2>=50) = TRUE
Do this for all students
4. Rank students (ascending) by Math marks.
=RANK(B2,$B$2:$B$6)
Do this for all students
5. Find highest marks for each student.
= MAX (B2:D2)
Do this for all students
Q5   a.   The dataset given below contains banking transaction records including   [15]
CO-2,3;   details such as date, Officer Name, Transaction Type, Account Type, and
SO-;
Region. It is used to analyze transaction patterns, workload distribution,
BL-4;
BL-6   and regional banking behaviour.
No. of   Avg.
Account   Transactio   Officer   Transa Amo   Service
Date Region   Branch   Type   n Type   Name   ctions   unt   Rating
(Refer Dataset file for details)
********** 7 **********
--- page 8 ---
1. Create a Pivot Table showing Officer-wise total Number of
Transactions and sort the results from highest to lowest. Based on
the Pivot Table, identify the officer handling the highest workload
[3 Marks]
2. Insert a Pivot Chart comparing Account Type-wise transaction
activity across regions and interpret which account type is most
active and how banking activity differs region-wise. [3 Marks]
3. Create a Pivot Table showing total Number of Transactions by
Transaction Type and insert a Slicer for Region and state a short
conclusion about regional banking behaviour. [4 Marks]
4.
i. VLOOKUP("AI Guide", A2:D6, 4, FALSE)
Answer: 1200
ii. =HLOOKUP("Excel Master", A1:E5, 3, FALSE)
Answer: 25
b.   1. Using Excel, find the probability that the daily production is less   [5]
CO-2;
SO-;   than 850 units.
BL-4;
Less than 850 =NORM.DIST(850,1000,120,TRUE)
BL-5
2. Using Excel, find the probability that the daily production is more
than 1150 units.
More than 1150 =1-NORM.DIST(1150,1000,120,TRUE)
3. Using Excel, determine the proportion of days when production lies
between 900 and 1100 units.
Between 900 and 1100 =NORM.DIST(1100,1000,120,TRUE)-
NORM.DIST(900,1000,120,TRUE)
********** 8 **********
--- page 9 ---
4. Using Excel, find the production level such that only 2% of days
exceed this value.
=NORM.INV(0.98,1000,120)
5. Based on your analysis, comment on whether 850 units is a suitable
minimum production target.
= 1 - NORM.DIST(850,1000,120,TRUE)
Yes, 850 is a suitable minimum production target since the
probability of achieving this target is 89.44% which mean target is
achievable most of the days
Q6   a.   1. Formulate cost, revenue and profit functions   [15]
CO-2,3;   C(x) = 2,00,000 + 300x
SO-;
R(x) = 500x
BL-4,
BL-5   P(x) = 200x − 2,00,000
2. Calculate Break-even point (units & ₹) using Formula
- BEP (units) = FC / Contribution
= 2,00,000 / 200 = 1,000 units
- BEP (in ₹) = 1,000 × 500 = ₹5,00,000
3. Find profit at 1,500 units by preparing an income statement
= 200 × 1500 − 2,00,000
= 1,00,000
4. Calculate PV Ratio and Margin of Safety (at 1,800 units)
= 200 / 500 = 40%
5. Draw B-E-P graph (can consider different levels of sales)
To evaluate based on actual graphs prepared
********** 9 **********
--- page 10 ---
CO-2,3;
SO-;   b.   1. Using the dataset provided, perform Correlation Analysis using   [5]
BL-4,
Excel Data Analysis ToolPak.
BL-5
Pesti   Soil
cide   Qua Crop
Fertilizer   Rainf   Irriga   Use   lity   Yield
Used   all   tion   Labor   (liters Inde (tons/
(kg/ha)   (mm) Hours Hours   )   x   ha)
Fertilizer Used
(kg/ha)   1.00
Rainfall (mm)   -0.17   1.00
Irrigation
Hours   0.54   -0.31   1.00
Labor Hours   0.09   -0.29   0.66   1.00
Pesticide Use
(liters)   0.03   -0.48   0.53   0.39   1.00
Soil Quality   1.0
Index   0.55   -0.50   0.75   0.46   0.41   0
Crop Yield   0.7
(tons/ha)   0.74   -0.25   0.91   0.56   0.52   9   1.00
2. Identify: The variable with the strongest and weakest correlation
with Crop Yield (tons/ha)
Irrigation Hours (0.91) → very strong positive relationship with
crop yield
Rainfall (−0.25) → weak (and slightly negative) relationship with
crop yield
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.99
R Square   0.98
Adjusted R
Square   0.94
Standard Error   0.28
Observations   10.00
ANOVA
Significan
df   SS   MS   F   ce F
Regression   6.00   12.37   2.06   26.01   0.01
********** 10 **********
--- page 11 ---
Residual   3.00   0.24   0.08
Total   9.00   12.61
Coefficie Standard   Lower
nts   Error   t Stat   P-value 95%
Intercept   0.24   2.14   0.11   0.92   -6.57
Fertilizer Used
(kg/ha)   0.02   0.00   4.05   0.03   0.00
Rainfall (mm)   0.00   0.00   1.99   0.14   0.00
Irrigation Hours   0.03   0.02   1.59   0.21   -0.03
Labor Hours   0.01   0.01   1.45   0.24   -0.01
Pesticide Use
(liters)   0.08   0.03   2.59   0.08   -0.02
Soil Quality Index   0.34   0.24   1.46   0.24   -0.41
4. Write the estimated regression equation.
Crop Yield = 0.24 + 0.02(Fertilizer) + 0.00(Rainfall) + 0.03(Irrigation)
+ 0.01(Labor) + 0.08(Pesticide) + 0.34(Soil Quality)
5. Interpret ANOVA significance of the model.
• R² (Coefficient of Determination):
• R² = 0.98
• Means 98% of variation in crop yield is explained by the
model → very good fit p-value
• Shows significance of variables
• p < 0.05 → significant
• In your model:
- Fertilizer (0.03) → significant
- Others → not significant
Q7   a.   1. Calculate NPV at 8% using Excel.   [15]
CO-3;   Project A: ₹83.70
SO-;
Project B: ₹6.40
BL-4,
BL-5
2. Calculate IRR.
Project A: ≈ 25.2%
Project B: ≈ 8.93%
Project A is preferred (B fails 10% criterion)
********** 11 **********
--- page 12 ---
3. If required return = 10%, which project is preferable?
Project A is preferred (B fails 10% criterion)
CO-1,2;   b.   Dream Homes Pvt. Ltd. (DH) is a builder company specializing in
SO-;
modern flats.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 6,000
•   Salaries of employees = Rs. 36,000
Each flat requires:
• Land cost = Rs. 60,000
• Construction materials = Rs. 40,000
[5]
• Labour = Rs. 20,000
•   Sales commission = Rs. 5,000 per flat
The selling price of each flat is Rs. 150,000.
Classify the above expenses into Fixed and Variable
Fixed Costs
Rent   8000
Utilities   6000
Salaries   36000
50000
Variable Costs
Land   60000
Construction   40000
Labour   20000
Commission   5000
125000
Income statement
Units sold   1
Sales @ 150000   150000
VC   125000
Contribution   25000
FC   50000
Profit/(Loss)   -25000
********** 12 **********
--- page 13 ---
B-E-P using Goal seek = 2 Houses

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 55e81902a254

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (13 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   What is the difference between a formula and a function in Excel?   [5]
SO- ;
Give one example of each.
BL-2
Solution:
Feature   Formula   Function
A   pre-built   command
A user-created equation
Definition   provided by   Excel   to
to perform calculations.
perform specific tasks.
Created by Microsoft and
Created by   the   user,
cannot be modified by the
Creation   combining operators, cell
user, but can be modified by
references, and constants.
the developer.
Requires a specific syntax,
Does not have a specific
usually in the format of
Syntax   syntax, but must start with
=FUNCTION_NAME(argu
an equals sign (=).
ment1, argument2, ...).
Highly customizable and
Limited to the tasks it was
Flexibility flexible   for   custom
designed for.
calculations.
Can be simple or complex Simplifies   complex
Complexity   depending on the user's operations   and   makes
needs.   calculations more efficient.
********** 1 **********
--- page 2 ---
=SUM(A1:A10) (adds   all
values in the range A1
through A10)
=A1+B1 (adds values in
Example
cells A1 and B1)
Other Eg:
Can   be   SUM,
COUNT,MAX, MIN etc.
CO-2;   b.   Mention Key components of CVP Analysis (any 5)   [5]
SO- ;
BL-4
Solution:
Key Components of CVP Analysis:
• Fixed Costs: Costs that remain constant regardless of the production
or sales volume.
• Variable Costs: Costs that change directly with the production or
sales volume.
• Sales Volume: The number of units sold or produced.
• Selling Price: The price at which each unit is sold.
• Contribution Margin: The difference between the selling price per
unit and the variable cost per unit.
• Break-Even Point: The sales volume at which total revenue equals
total costs, resulting in no profit or loss
CO-2 ;   c.   Explain the purpose of Co-relation analysis.   [5]
SO- ;
Explain the difference between positive and negative correlation.
BL-3
Solution:
To determine the strength and direction of the relationship between two
quantitative variables. Co-relation coefficient measures the strength and
direction of a linear relationship between two variables, ranging from -1
to +1
In a positive correlation, variables move in the same direction (e.g.,
income and expenditure).
In a negative correlation, they move in opposite directions (e.g., price and
demand).
********** 2 **********
--- page 3 ---
CO-2 ;   d.   Net Present Value (NPV) and Internal Rate of Return (IRR) are crucial   [5]
SO- ;
tools for evaluating investment proposals. Please elaborate.
BL-4
Elaborate what is NPV and IRR and how to interpret the outcomes of
each.
Solution
NPV
NPV considers the time value of money by discounting future cash flows
back to their present value. It represents the difference between the
present value of cash inflows and the present value of cash outflows.
Interpretation:
A positive NPV indicates that the investment is likely to be profitable,
while a negative NPV suggests it may not be worthwhile.
IRR
IRR is the discount rate at which the NPV of all cash flows from a project
equals zero. It represents the potential return on investment.
Interpretation:
NPV uses a discount rate to calculate the present value of future cash
flows, while IRR determines the discount rate that makes the NPV equal
to zero.
Q2   a.   1) Define the decision variables   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
2) Formulate the objective function
3) Write all constraints
********** 3 **********
--- page 4 ---
4) Solve the LPP equation and find out the minimum cost using LPP
Solver.
x1 = 1, x2 = 0, x3 = 1, x4 = 1, x5 = 1
Minimum cost Z = 0.73
CO-1,2;
b.   [5]
SO-;
BL-1,
BL-3,   1. Using excel formula, find the average experience of all the employees.
-   5.44 years using the AVERAGE Formula
2. Using excel formula, extract only the employee number from the
Employee ID of Amit.
- = RIGHT(Cell Reference, 3) → E101 →101
3. Using excel formula, create employee label of Neha.
Employee Label comprises of Employee ID followed by
‘-‘ followed by the name of the employee, followed by the Department
in brackets. Eg: “E101-Amit (Sales)”
********** 4 **********
--- page 5 ---
= CONCATE(A3, “-”, B3, “ (“, C3,”)”) → “E102 – Neha (HR)”
4. Using excel Nested-IF function, find out total Sales undertaken by the
Sales Department.
= SUMIF(C3:C27,”Sales”,D3:D27)
= 385000
5. Using appropriate LookUP function, find out the number of units sold
by Tanya.
=VLOOKUP(Tanya,B3:B27,4,FALSE)
= 8
Q3   a.   Decision Tree   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to open a medium sized shop as the
EMV is the highest under that option of $18,000.
CO-2;
SO-;   b.   In an experiment of dice roll, A dice is rolled 30 times.   [5]
BL-4,   Probability of rolling a “6” = 1/6.
BL-5
********** 5 **********

[Text in pictures on this page, read by OCR]
Good Market $40,000

Opena 0.3
small shop 0.4 Average Market $20,000

$15,500 9.3 Bad Market -$15,000

ae Good Market $70,000

0.4 Average Market $30,000

Opena
medium-sized shop

= Bad Market -$50,000

Good Market so
Do not

open a shop

$o

0.4 Average Market $0

0.3 Bad Market $0
--- page 6 ---
Find
1. Probability of rolling exactly 5 sixes.
=BINOM.DIST(5, 30, 1/6, FALSE) = 0.206
2. Probability of rolling at most 5 sixes.
=BINOM.DIST(5, 30, 1/6, TRUE) = 0.616
3. Probability of rolling atleast 3 sixes
=1 - BINOM.DIST(2, 30, 1/6, TRUE) = 0.8972096263
4. Probability of between 4 and 8 sixes.
=BINOM.DIST.RANGE(30, 1/6, 4, 8)
5. Expected number of sixes.
=30*(1/6) = 5
Q4   a.   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 6 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

~ 7, _f
Dif=%, P(X)=F

Values: 0.15, 0.25, 0.30, 0.20, 0.10

(b) Mean, Variance, SD (6 Marks)
bi fe
p=

“= 3.85
Lif
So fa?
of = Ss _ P= 1.33
hf

o0 =V133=1.15

(c) Excel (4 Marks)

VAR.P = 1.33, STDEV.P = 1.15
VARS = 1.40, STDEV.S = 1.18

(d) Interpretation (2 Marks)

Moderate variation, fairly consistent data
--- page 7 ---
CO-1,2;
SO-;
BL-1;   b.   1. Assign grade using Nested IF (≥80 = A, ≥60 = B, else C).   [5]
BL-3
= IF(B2>=80,"A",IF(B2>=60,"B","C")) → John = B
2. Round Science marks to nearest 10.
=ROUND(C2,-1) = 90
= ROUND(C3,-1) = 90
= ROUND(C4,-1) = 70
= ROUND(C5,-1) = 60
= ROUND(C6,-1) = 40
3. Check if student passed all subjects (upon scoring ≥50) using AND.
=AND(B2>=50,C2>=50,D2>=50) = TRUE
Do this for all students
4. Rank students (ascending) by Math marks.
=RANK(B2,$B$2:$B$6)
Do this for all students
5. Find highest marks for each student.
= MAX (B2:D2)
Do this for all students
Q5   a.   The dataset given below contains banking transaction records including   [15]
CO-2,3;   details such as date, Officer Name, Transaction Type, Account Type, and
SO-;
Region. It is used to analyze transaction patterns, workload distribution,
BL-4;
BL-6   and regional banking behaviour.
No. of   Avg.
Account   Transactio   Officer   Transa Amo   Service
Date Region   Branch   Type   n Type   Name   ctions   unt   Rating
(Refer Dataset file for details)
********** 7 **********
--- page 8 ---
1. Create a Pivot Table showing Officer-wise total Number of
Transactions and sort the results from highest to lowest. Based on
the Pivot Table, identify the officer handling the highest workload
[3 Marks]
2. Insert a Pivot Chart comparing Account Type-wise transaction
activity across regions and interpret which account type is most
active and how banking activity differs region-wise. [3 Marks]
3. Create a Pivot Table showing total Number of Transactions by
Transaction Type and insert a Slicer for Region and state a short
conclusion about regional banking behaviour. [4 Marks]
4.
i. VLOOKUP("AI Guide", A2:D6, 4, FALSE)
Answer: 1200
ii. =HLOOKUP("Excel Master", A1:E5, 3, FALSE)
Answer: 25
b.   1. Using Excel, find the probability that the daily production is less   [5]
CO-2;
SO-;   than 850 units.
BL-4;
Less than 850 =NORM.DIST(850,1000,120,TRUE)
BL-5
2. Using Excel, find the probability that the daily production is more
than 1150 units.
More than 1150 =1-NORM.DIST(1150,1000,120,TRUE)
3. Using Excel, determine the proportion of days when production lies
between 900 and 1100 units.
Between 900 and 1100 =NORM.DIST(1100,1000,120,TRUE)-
NORM.DIST(900,1000,120,TRUE)
********** 8 **********
--- page 9 ---
4. Using Excel, find the production level such that only 2% of days
exceed this value.
=NORM.INV(0.98,1000,120)
5. Based on your analysis, comment on whether 850 units is a suitable
minimum production target.
= 1 - NORM.DIST(850,1000,120,TRUE)
Yes, 850 is a suitable minimum production target since the
probability of achieving this target is 89.44% which mean target is
achievable most of the days
Q6   a.   1. Formulate cost, revenue and profit functions   [15]
CO-2,3;   C(x) = 2,00,000 + 300x
SO-;
R(x) = 500x
BL-4,
BL-5   P(x) = 200x − 2,00,000
2. Calculate Break-even point (units & ₹) using Formula
- BEP (units) = FC / Contribution
= 2,00,000 / 200 = 1,000 units
- BEP (in ₹) = 1,000 × 500 = ₹5,00,000
3. Find profit at 1,500 units by preparing an income statement
= 200 × 1500 − 2,00,000
= 1,00,000
4. Calculate PV Ratio and Margin of Safety (at 1,800 units)
= 200 / 500 = 40%
5. Draw B-E-P graph (can consider different levels of sales)
To evaluate based on actual graphs prepared
********** 9 **********
--- page 10 ---
CO-2,3;
SO-;   b.   1. Using the dataset provided, perform Correlation Analysis using   [5]
BL-4,
Excel Data Analysis ToolPak.
BL-5
Pesti   Soil
cide   Qua Crop
Fertilizer   Rainf   Irriga   Use   lity   Yield
Used   all   tion   Labor   (liters Inde (tons/
(kg/ha)   (mm) Hours Hours   )   x   ha)
Fertilizer Used
(kg/ha)   1.00
Rainfall (mm)   -0.17   1.00
Irrigation
Hours   0.54   -0.31   1.00
Labor Hours   0.09   -0.29   0.66   1.00
Pesticide Use
(liters)   0.03   -0.48   0.53   0.39   1.00
Soil Quality   1.0
Index   0.55   -0.50   0.75   0.46   0.41   0
Crop Yield   0.7
(tons/ha)   0.74   -0.25   0.91   0.56   0.52   9   1.00
2. Identify: The variable with the strongest and weakest correlation
with Crop Yield (tons/ha)
Irrigation Hours (0.91) → very strong positive relationship with
crop yield
Rainfall (−0.25) → weak (and slightly negative) relationship with
crop yield
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.99
R Square   0.98
Adjusted R
Square   0.94
Standard Error   0.28
Observations   10.00
ANOVA
Significan
df   SS   MS   F   ce F
Regression   6.00   12.37   2.06   26.01   0.01
********** 10 **********
--- page 11 ---
Residual   3.00   0.24   0.08
Total   9.00   12.61
Coefficie Standard   Lower
nts   Error   t Stat   P-value 95%
Intercept   0.24   2.14   0.11   0.92   -6.57
Fertilizer Used
(kg/ha)   0.02   0.00   4.05   0.03   0.00
Rainfall (mm)   0.00   0.00   1.99   0.14   0.00
Irrigation Hours   0.03   0.02   1.59   0.21   -0.03
Labor Hours   0.01   0.01   1.45   0.24   -0.01
Pesticide Use
(liters)   0.08   0.03   2.59   0.08   -0.02
Soil Quality Index   0.34   0.24   1.46   0.24   -0.41
4. Write the estimated regression equation.
Crop Yield = 0.24 + 0.02(Fertilizer) + 0.00(Rainfall) + 0.03(Irrigation)
+ 0.01(Labor) + 0.08(Pesticide) + 0.34(Soil Quality)
5. Interpret ANOVA significance of the model.
• R² (Coefficient of Determination):
• R² = 0.98
• Means 98% of variation in crop yield is explained by the
model → very good fit p-value
• Shows significance of variables
• p < 0.05 → significant
• In your model:
- Fertilizer (0.03) → significant
- Others → not significant
Q7   a.   1. Calculate NPV at 8% using Excel.   [15]
CO-3;   Project A: ₹83.70
SO-;
Project B: ₹6.40
BL-4,
BL-5
2. Calculate IRR.
Project A: ≈ 25.2%
Project B: ≈ 8.93%
Project A is preferred (B fails 10% criterion)
********** 11 **********
--- page 12 ---
3. If required return = 10%, which project is preferable?
Project A is preferred (B fails 10% criterion)
CO-1,2;   b.   Dream Homes Pvt. Ltd. (DH) is a builder company specializing in
SO-;
modern flats.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 6,000
•   Salaries of employees = Rs. 36,000
Each flat requires:
• Land cost = Rs. 60,000
• Construction materials = Rs. 40,000
[5]
• Labour = Rs. 20,000
•   Sales commission = Rs. 5,000 per flat
The selling price of each flat is Rs. 150,000.
Classify the above expenses into Fixed and Variable
Fixed Costs
Rent   8000
Utilities   6000
Salaries   36000
50000
Variable Costs
Land   60000
Construction   40000
Labour   20000
Commission   5000
125000
Income statement
Units sold   1
Sales @ 150000   150000
VC   125000
Contribution   25000
FC   50000
Profit/(Loss)   -25000
********** 12 **********
--- page 13 ---
B-E-P using Goal seek = 2 Houses

FIR ICR 7] QI HO
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper ad7f4cdffb1e

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7057/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   Mention few uses of Spreadsheet (any 5)   [5]
SO- ;
-   Prepare Budgets & Forecasts
BL-2
-   Financial statement Preparation & Analysis
- Graphs and Charts
- Data Analytics
-   Inventory Management
-   Etc.
CO-2;   b.   Explain CVP Analysis and Break Even Point Analysis.   [5]
SO- ;
CVP Analysis
BL-4
• Cost-volume-profit (CVP) analysis is a financial tool that
examines the relationship between a company's costs, sales
volume, and profit
•   It helps businesses understand how changes in sales volume,
selling prices, and costs affect their profitability
• CVP analysis is often used to determine the break-even point,
which is the sales volume needed to cover all costs, and to plan
for different profit levels.
********** 1 **********
--- page 2 ---
Breakeven Analysis
•   It refers to the point at which total costs and total revenue are
equal.
• A break-even point analysis is used to determine the number of
units to be produced or overall revenue needed to cover total
costs (fixed and variable costs).
• Break-even analysis is important to business owners and
managers in determining how many units (or revenues) are
needed to cover fixed and variable expenses of the business.
• The formula for break-even analysis is as follows:
Break-Even Quantity = Fixed Costs / (Sales Price per Unit –
Variable Cost Per Unit)
CO-2 ;   c.   What are the types of Co-relation Co-efficient Values?   [5]
SO- ;
Explain how to interpret each type.
BL-3
Correla   Correlation type   Meaning
tion
coeffici
ent
value
1   Perfect positive   When one variable changes, the other
correlation   variables change in the same direction
(linearly). If the correlation coefficient
value is positive, then there is a similar
and identical relation between the two
variables.
0   Zero correlation   There is no relationship between the
variables.
********** 2 **********
--- page 3 ---
-1   Perfect negative   When one variable changes, the other
correlation   variables change in the opposite
direction. If the correlation coefficient
value is negative, it shows dissimilarity
between the two variables
CO-2 ;   d.   What is the difference in the objectivity behind using the Internal Rate of   [5]
SO- ;
Return (IRR) & Net Present Value (NPV) methods for evaluation of
BL-4
investment proposals.
Mention the underlying assumptions under each of the above two
methods of evaluation.
Parameters   NPV   IRR
Objective   Aims   to   maximise   Seeks to find the rate of
investment   value   by   return where cash inflows
comparing cash inflows   and outflows are equal
and outflows
Cash   Flows   Considers   all cash   Assumes a single   initial
Assumption   flows throughout   the   investment followed by a
project's duration   series of cash inflows
Reinvestment   Assumes   that   cash   Assumes that cash inflows
Assumption   inflows are reinvested at   are reinvested at the IRR
the discount rate   itself
Accuracy   It is assumes that future   It assumes that the rate of
Assumption   cash flows are accurately   return shall remain constant
known as of today   for all periods.
********** 3 **********
--- page 4 ---
Q2   a. A hospital is designing a lunch menu using rice, paneer, vegetables,   [15]
CO-3;   yogurt, and juice. The aim is to minimize cost while meeting patient
SO-;
nutritional requirements.
BL-4,
BL-5,   Each meal must satisfy total calories between 500 and 700. At least 20g
BL-6
of protein must be there in the meal. No more than 35% of calories from
fat and at least 50 mg of Vitamin C must be there in the meal. The content
and cost of each item are given below:
Food Item   Fat   Total   Vitamin   Protein   Cost ($)
Calories Calories C (mg)   (g)
Rice   30   200   0   4   0.25
(1 cup)
Paneer   120   250   0   20   1.50
(1 serving)
Vegetables   10   80   30   3   0.40
(1 cup)
Yogurt   50   150   2   6   0.60
(1 cup)
Juice   0   110   90   1   0.50
(1 cup)
1. Define the decision variables
x2 = serving of Paneer
2. Formulate the objective function
********** 4 **********
--- page 5 ---
3. Write all constraints
4. Solve the LPP equation and find out the minimum cost using
Solver
x1 = 1, x2 = 1, x3 = 1, x4 = 0, x5 = 0.5
Minimum cost Z = 2.40
b.   Consider the following data of Salary paid by the company to its   [5]
CO-1,2;
SO-;   employees;
BL-1,
BL-3,
1. Using excel formula, create employee labels;
Employee Label comprises of name of the Employee followed by
********** 5 **********

[Text in pictures on this page, read by OCR]
1. Calorie Constraint

500 < 2002; + 25022 + 8023 + 15024 + 11025 < 700

2. Protein Constraint

Ax, + 20x2 + 323 + 624 + las > 20

3. Vitamin C Constraint

3023 + 224 + 9025 > 50

4. Fat Constraint (< 35%)

302; + 120a2 + 1023 + 50r4 + Ors < 0.35(2002) + 25022 + 8023 + 15024

5. Non-negativity

21, £2,£3,%4,05 > 0
--- page 6 ---
‘-‘ followed by the Department in which the employee works
Eg: “Amit-HR”
. =CONCATE(A2, “ - ”, C2) → Alice - HR
Do the same for all employees
2. Using excel formula, find out the highest salary paid by the
company
= MAX(D2:D6) = 65000
3. Using excel formula, find the average salary expense of the
company.
= AVERAGE(D2:D6) = 55000
4. Find the position of “IT” in the Department column using the
relevant Excel formula.
= MATCH(“IT”, C2:C6, 0) → 3
5. Using excel Nested-IF function, find the total salary of employees
in the IT department.
= SUMIF(C2:C6,”IT”,D2:D6) = 125000
********** 6 **********
--- page 7 ---
Q3   a.   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to opt for Plant-A as the EMV is the
highest under that option of 4,00,000
CO-2;
SO-;   b.   In an exam, A student guesses on 20 MCQs, each with 25% chance being   [5]
BL-4,   correct.
BL-5
Find
1. Probability of exactly 5 correct answers.
=BINOM.DIST(5, 20, 0.25, FALSE) = 0.202
********** 7 **********

[Text in pictures on this page, read by OCR]
High
800000
ct]
o4
Plant-A Moderate
1 300000
0 300000
O2
-200000
0 -200000
o4
High
500000
o4
Moderate
| 250000
QO 250000
O.2
-50000
Qo -50000
No Expansion
a ee oO
--- page 8 ---
2. Probability of at most 5 correct answers.
=BINOM.DIST(5, 20, 0.25, TRUE) = 0.616
3. Probability of at least 10 correct answers.
=1 - BINOM.DIST(9, 20, 0.25, TRUE)
4. Expected number of correct answers.
n x p = 5
=20*0.25
5. Standard deviation of correct answers.
=SQRT(20*0.25*0.75) = 1.94
Q4   a.   Read solution as 1,2,3,4 instead of a,b,c,d   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 8 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

7 = = 7, — f
Sof =25, P(X) = 35

(b) Mean, Variance, SD (6 Marks)

p= 6.96
ao = 1.36
o=117

(c) Excel (4 Marks)

VAR.P = 1.36, STDEV.P = 1.17
VARS = 1.42, STDEV.S = 1.19

(d) Interpretation (2 Marks)

Stable patient inflow
--- page 9 ---
CO-1,2;   b.   Consider the following dataset on project deadlines   [5]
SO-;
Project   Days Left
BL-1;
BL-3   P1   10
P2   25
P3   5
P4   15
P5   20
1. Categorize urgency using Nested IF functions (≤7 = Urgent, ≤15 =
Moderate, else Relaxed).
=IF(B2<=7,"Urgent",IF(B2<=15,"Moderate","Relaxed")) → P1 =
Moderate
2. Find out the Lowest number of days left and mention which Project
it belongs to
=MIN(B2:B6) = 5 Days = P3 [Can also use Index and Match (Min)]
3. Check if project is within 30 days using AND
=AND(B2<=30) → TRUE
4. Rank projects by days left
=RANK(B2,B2:B6) → P1 = 5
5. Average days left (rounded to integer)
=ROUND(AVERAGE(B2:B6),0) → 15
Q5   a.   The dataset given below contains healthcare service records including   [15]
CO-2,3;   hospital, department, doctor, and patient details. It is designed to analyze
SO-;
service load, patient distribution, and operational efficiency across
BL-4;
BL-6   hospitals.
.
No.
Servic   Avg   Satisf
Dat Hospita   Patien Docto   of
Dept e   Billin action
e   l   t Type   r   Patie
Type   g   Rating
nts
(Refer Dataset file for details)
********** 9 **********
--- page 10 ---
1. Create a Pivot Table showing Doctor-wise total number of patients
and sort the results from highest to lowest. Based on the Pivot Table,
identify the doctor handling the highest workload – [3 Marks]
2. Insert a Pivot Chart comparing Service Type-wise patient activity
across hospitals and interpret which service type is most active and
how healthcare activity differs across hospitals – [3 Marks]
3. Create a Pivot Table showing total number of patients by Patient
Type and insert a Slicer for Hospital. State a short conclusion about
hospital-wise patient behavior – [4 Marks]
4. An organization maintains employee records including department,
salary, and bonus details. The Human Resource department
frequently accesses this dataset to process payroll and evaluate
employee compensation
Employee   Department   Salary   Bonus
John   HR   30000   5000
Sara   IT   45000   8000
Mike   Finance   40000   7000
Nina   IT   42000   6000
Raj   HR   35000   5500
(Refer Dataset file for details)
i. Using the VLOOKUP function, retrieve the Salary of employee
"Sara".
=VLOOKUP("Sara", A2:D6, 3, FALSE)
= 45000   [2.5 Marks]
ii. If the dataset is arranged horizontally, use the HLOOKUP
function to find the bonus of "John"
=HLOOKUP("John", A1:E5, 4, FALSE)
=5000   [2.5 Marks]
********** 10 **********
--- page 11 ---
CO-2;   b. A domestic airline company monitors the number of passengers traveling   [5]
SO-;
per flight to optimize seat allocation and pricing strategies. Based on
BL-4;
BL-5   historical data, the number of passengers per flight follows a normal
distribution with a mean of 180 passengers and a standard deviation of
20 passengers. Variations occur due to seasonal demand, ticket pricing,
and travel trends. The airline management wants to analyze this data to
improve capacity planning and avoid overbooking or underutilization.
1. Using Excel, find the probability that fewer than 150 passengers travel
on a flight.
=NORM.DIST(150,180,20,TRUE)
P(X < 150) = 0.0668
2. Find the probability that more than 210 passengers travel.
=1-NORM.DIST(210,180,20,TRUE)
P(X > 210) = 0.0668
3. Determine the probability that passengers are between 160 and 200.
=NORM.DIST(200,180,20,TRUE)-NORM.DIST(160,180,20,TRUE)
P(160 < X < 200) = 0.6826
4. Find the passenger count such that only 5% of flights exceed this
number.
=NORM.INV(0.95,180,20)
=213
5. Should the airline regularly prepare for more than 210 passengers?
No, because the probability of exceeding 210 passengers is only
6.68%, indicating such situations are infrequent and do not justify
regular preparation
Q6   a. A company manufactures gadgets with the following details:   [15]
CO-2,3;   Selling Price = ₹800 per unit
SO-;
Variable Cost = ₹500 per unit
BL-4,
BL-5   Fixed Cost = ₹3,00,000 per month
********** 11 **********
--- page 12 ---
1. Prepare CVP income statement at 1,200 units
Units   1200
SP   800
Sales   960000
(-) VC   600000
Contribution   360000
(-) FC   300000
Profit   60000
2. Calculate Break-even point (units & ₹) using Formula
= 3,00,000 / 300 = 1,000 units
i.e. Fixed Costs / Contribution per unit
3. Prepare income statement at BEP level
Units   1000
SP   800
Sales   800000
(-) VC   500000
Contribution   300000
(-) FC   300000
Profit   0
4. Calculate PV Ratio and Margin of Safety (at 1,500 units)
= 300 / 800 = 37.5%
5. Draw B-E-P graph (can consider different levels of sales)
To be evaluated on actual
CO-2,3;   b.   Average   Customer   [5]
SO-;   Conversion   Delivery Time Monthly Sales
Product   Ratings
BL-4,   Rate (%)   (Days)   Revenue ($)
Price ($)   (1-5)
BL-5   3.64   69.98   3.74   4   138865.23
3.02   61.93   3.58   5   69071.92
3.42   48.93   4.5   5   89212.37
3.42   63.96   4.17   2   127090.24
2.63   40.97   4.69   2   126027.03
4.42   36.07   4.04   4   102120.53
3.54   42.16   3.74   1   136031.57
4.56   46.91   4.67   3   97432.72
4.63   52.87   4.27   2   155072.53
********** 12 **********
--- page 13 ---
3.03   56.53   3.76   2   118065.83
(Refer Dataset file for details)
1. Using the dataset provided, perform Correlation Analysis using
Excel Data Analysis ToolPak.
Convers   Custo   Monthl
ion   Average mer   Deliver   y Sales
Rate   Product   Rating y Time   Revenu
(%)   Price ($)   s (1-5)   (Days)   e ($)
Conversion Rate (%)   1
-
Average Product Price 0.2182
($)   1   1
Customer Ratings (1-   0.2010   -
5)   42   0.45071 1
-
0.0170   0.20753 0.082
Delivery Time (Days)   15   4   4   1
-
Monthly Sales   0.1838   0.08155 0.011   0.7244
Revenue ($)   48   7   858   8   1
2. Identify: The variable with the strongest and weakest correlation
with Monthly Sales Revenue
Strongest factor affecting revenue: Delivery Time (−0.72)
Weakest factor affecting revenue: Customer Ratings (0.01)
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.805052
R Square   0.648109
Adjusted R Square   0.366596
Standard Error   20780.2
Observations   10
ANOVA
Significan
df   SS   MS   F   ce F
9.94E   2.3022
Regression   4   3.98E+09 +08   33   0.192472
4.32E
Residual   5   2.16E+09 +08
Total   9   6.14E+09
********** 13 **********
--- page 14 ---
Coefficient   Standard   P-   Lower
s   Error   t Stat   value   95%
0.706   0.5113
Intercept   74705.04   105719.8 632   55   -197056
Conversion Rate   0.945   0.3877
(%)   9777.88   10341.03 542   99   -16804.6
Average Product   1.043   0.3443
Price ($)   757.8375   725.978   885   57   -1108.35
Customer Ratings   0.129   0.9022
(1-5)   2461.83   19058   176   54   -46528.3
-
Delivery Time   2.914   0.0332
(Days)   -14624.5   5017.714 57   23   -27522.9
4. Write the estimated regression equation.
= 74705.04 + 9777.88(Conversion Rate) + 757.84(Price) +
2461.83(Ratings) −14624.49(Delivery Time)
5. Interpret R Square significance of the model.
Model Quality:
• R² = 0.65 → ~65% variation explained (moderate fit)
• Significance F = 0.19 (> 0.05) → model not strongly significant
Variable Significance (p-values):
• Conversion Rate → 0.38
•   Price → 0.34
• Ratings → 0.90
• Delivery Time → 0.033 ✅ (significant)
Q7   a.   Following are the cash flows of two projects:   [15]
CO-3;
SO-;
BL-4,   Project X
BL-5   Year   0   1   2   3   4
Cash
-300   50   100   150   200
Flow
Project Y
Year   0   1   2   3   4
Cash
-300   150   120   80   60
Flow
********** 14 **********
--- page 15 ---
1. Calculate NPV at 9% using Excel.
Project X: ₹87.55
Project Y: ₹42.90
2. Calculate IRR.
Project X: ≈ 19.19%
Project Y: ≈ 16.57%
3. If required return = 11%, which project is preferable?
Project X is preferred as it gives highest return of 19.19% which is
over and above the required return of 11%
CO-1,2;   b.   Sunrise Builders (SB) is a medium-scale construction company focusing   [5]
SO-;
on affordable housing projects.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 9,000
•   Salaries of employees = Rs. 40,000
Each flat requires:
• Land cost = Rs. 70,000
• Construction materials = Rs. 30,000
• Labour = Rs. 20,000
•   Sales commission = Rs. 8,000 per flat
The selling price of each flat is Rs. 140,000.
Classify the above expenses into Fixed and Variable and Draw an
Income statement for the above parameters. Find out the B-E-P using
Goalseek technique (What-if-Analysis function). Round-off the final
answer if required.
Fixed Costs
Rent   8000
Utilities   9000
Salaries   40000
57000
********** 15 **********
--- page 16 ---
Variable Costs
Land   70000
Construction   30000
Labour   20000
Commission   8000
128000
Income statement
Units sold   1
Sales @ 150000   140000
VC   128000
Contribution   12000
FC   57000
Profit/(Loss)   -45000
BEP Using Goal Seek = 4.75 = 5 units
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper ccd1088f7c26

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   Mention few uses of Spreadsheet (any 5)   [5]
SO- ;
-   Prepare Budgets & Forecasts
BL-2
-   Financial statement Preparation & Analysis
- Graphs and Charts
- Data Analytics
-   Inventory Management
-   Etc.
CO-2;   b.   Explain CVP Analysis and Break Even Point Analysis.   [5]
SO- ;
CVP Analysis
BL-4
• Cost-volume-profit (CVP) analysis is a financial tool that
examines the relationship between a company's costs, sales
volume, and profit
•   It helps businesses understand how changes in sales volume,
selling prices, and costs affect their profitability
• CVP analysis is often used to determine the break-even point,
which is the sales volume needed to cover all costs, and to plan
for different profit levels.
********** 1 **********
--- page 2 ---
Breakeven Analysis
•   It refers to the point at which total costs and total revenue are
equal.
• A break-even point analysis is used to determine the number of
units to be produced or overall revenue needed to cover total
costs (fixed and variable costs).
• Break-even analysis is important to business owners and
managers in determining how many units (or revenues) are
needed to cover fixed and variable expenses of the business.
• The formula for break-even analysis is as follows:
Break-Even Quantity = Fixed Costs / (Sales Price per Unit –
Variable Cost Per Unit)
CO-2 ;   c.   What are the types of Co-relation Co-efficient Values?   [5]
SO- ;
Explain how to interpret each type.
BL-3
Correla   Correlation type   Meaning
tion
coeffici
ent
value
1   Perfect positive   When one variable changes, the other
correlation   variables change in the same direction
(linearly). If the correlation coefficient
value is positive, then there is a similar
and identical relation between the two
variables.
0   Zero correlation   There is no relationship between the
variables.
********** 2 **********
--- page 3 ---
-1   Perfect negative   When one variable changes, the other
correlation   variables change in the opposite
direction. If the correlation coefficient
value is negative, it shows dissimilarity
between the two variables
CO-2 ;   d.   What is the difference in the objectivity behind using the Internal Rate of   [5]
SO- ;
Return (IRR) & Net Present Value (NPV) methods for evaluation of
BL-4
investment proposals.
Mention the underlying assumptions under each of the above two
methods of evaluation.
Parameters   NPV   IRR
Objective   Aims   to   maximise   Seeks to find the rate of
investment   value   by   return where cash inflows
comparing cash inflows   and outflows are equal
and outflows
Cash   Flows   Considers   all cash   Assumes a single   initial
Assumption   flows throughout   the   investment followed by a
project's duration   series of cash inflows
Reinvestment   Assumes   that   cash   Assumes that cash inflows
Assumption   inflows are reinvested at   are reinvested at the IRR
the discount rate   itself
Accuracy   It is assumes that future   It assumes that the rate of
Assumption   cash flows are accurately   return shall remain constant
known as of today   for all periods.
********** 3 **********
--- page 4 ---
Q2   a. A hospital is designing a lunch menu using rice, paneer, vegetables,   [15]
CO-3;   yogurt, and juice. The aim is to minimize cost while meeting patient
SO-;
nutritional requirements.
BL-4,
BL-5,   Each meal must satisfy total calories between 500 and 700. At least 20g
BL-6
of protein must be there in the meal. No more than 35% of calories from
fat and at least 50 mg of Vitamin C must be there in the meal. The content
and cost of each item are given below:
Food Item   Fat   Total   Vitamin   Protein   Cost ($)
Calories Calories C (mg)   (g)
Rice   30   200   0   4   0.25
(1 cup)
Paneer   120   250   0   20   1.50
(1 serving)
Vegetables   10   80   30   3   0.40
(1 cup)
Yogurt   50   150   2   6   0.60
(1 cup)
Juice   0   110   90   1   0.50
(1 cup)
1. Define the decision variables
x2 = serving of Paneer
2. Formulate the objective function
********** 4 **********
--- page 5 ---
3. Write all constraints
4. Solve the LPP equation and find out the minimum cost using
Solver
x1 = 1, x2 = 1, x3 = 1, x4 = 0, x5 = 0.5
Minimum cost Z = 2.40
b.   Consider the following data of Salary paid by the company to its   [5]
CO-1,2;
SO-;   employees;
BL-1,
BL-3,
1. Using excel formula, create employee labels;
Employee Label comprises of name of the Employee followed by
********** 5 **********

[Text in pictures on this page, read by OCR]
1. Calorie Constraint

500 < 2002; + 25022 + 8023 + 15024 + 11025 < 700

2. Protein Constraint

Ax, + 20x2 + 323 + 624 + las > 20

3. Vitamin C Constraint

3023 + 224 + 9025 > 50

4. Fat Constraint (< 35%)

302; + 120a2 + 1023 + 50r4 + Ors < 0.35(2002) + 25022 + 8023 + 15024

5. Non-negativity

21, £2,£3,%4,05 > 0
--- page 6 ---
‘-‘ followed by the Department in which the employee works
Eg: “Amit-HR”
. =CONCATE(A2, “ - ”, C2) → Alice - HR
Do the same for all employees
2. Using excel formula, find out the highest salary paid by the
company
= MAX(D2:D6) = 65000
3. Using excel formula, find the average salary expense of the
company.
= AVERAGE(D2:D6) = 55000
4. Find the position of “IT” in the Department column using the
relevant Excel formula.
= MATCH(“IT”, C2:C6, 0) → 3
5. Using excel Nested-IF function, find the total salary of employees
in the IT department.
= SUMIF(C2:C6,”IT”,D2:D6) = 125000
********** 6 **********
--- page 7 ---
Q3   a.   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to opt for Plant-A as the EMV is the
highest under that option of 4,00,000
CO-2;
SO-;   b.   In an exam, A student guesses on 20 MCQs, each with 25% chance being   [5]
BL-4,   correct.
BL-5
Find
1. Probability of exactly 5 correct answers.
=BINOM.DIST(5, 20, 0.25, FALSE) = 0.202
********** 7 **********

[Text in pictures on this page, read by OCR]
High
800000
ct]
o4
Plant-A Moderate
1 300000
0 300000
O2
-200000
0 -200000
o4
High
500000
o4
Moderate
| 250000
QO 250000
O.2
-50000
Qo -50000
No Expansion
a ee oO
--- page 8 ---
2. Probability of at most 5 correct answers.
=BINOM.DIST(5, 20, 0.25, TRUE) = 0.616
3. Probability of at least 10 correct answers.
=1 - BINOM.DIST(9, 20, 0.25, TRUE)
4. Expected number of correct answers.
n x p = 5
=20*0.25
5. Standard deviation of correct answers.
=SQRT(20*0.25*0.75) = 1.94
Q4   a.   Read solution as 1,2,3,4 instead of a,b,c,d   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 8 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

7 = = 7, — f
Sof =25, P(X) = 35

(b) Mean, Variance, SD (6 Marks)

p= 6.96
ao = 1.36
o=117

(c) Excel (4 Marks)

VAR.P = 1.36, STDEV.P = 1.17
VARS = 1.42, STDEV.S = 1.19

(d) Interpretation (2 Marks)

Stable patient inflow
--- page 9 ---
CO-1,2;   b.   Consider the following dataset on project deadlines   [5]
SO-;
Project   Days Left
BL-1;
BL-3   P1   10
P2   25
P3   5
P4   15
P5   20
1. Categorize urgency using Nested IF functions (≤7 = Urgent, ≤15 =
Moderate, else Relaxed).
=IF(B2<=7,"Urgent",IF(B2<=15,"Moderate","Relaxed")) → P1 =
Moderate
2. Find out the Lowest number of days left and mention which Project
it belongs to
=MIN(B2:B6) = 5 Days = P3 [Can also use Index and Match (Min)]
3. Check if project is within 30 days using AND
=AND(B2<=30) → TRUE
4. Rank projects by days left
=RANK(B2,B2:B6) → P1 = 5
5. Average days left (rounded to integer)
=ROUND(AVERAGE(B2:B6),0) → 15
Q5   a.   The dataset given below contains healthcare service records including   [15]
CO-2,3;   hospital, department, doctor, and patient details. It is designed to analyze
SO-;
service load, patient distribution, and operational efficiency across
BL-4;
BL-6   hospitals.
.
No.
Servic   Avg   Satisf
Dat Hospita   Patien Docto   of
Dept e   Billin action
e   l   t Type   r   Patie
Type   g   Rating
nts
(Refer Dataset file for details)
********** 9 **********
--- page 10 ---
1. Create a Pivot Table showing Doctor-wise total number of patients
and sort the results from highest to lowest. Based on the Pivot Table,
identify the doctor handling the highest workload – [3 Marks]
2. Insert a Pivot Chart comparing Service Type-wise patient activity
across hospitals and interpret which service type is most active and
how healthcare activity differs across hospitals – [3 Marks]
3. Create a Pivot Table showing total number of patients by Patient
Type and insert a Slicer for Hospital. State a short conclusion about
hospital-wise patient behavior – [4 Marks]
4. An organization maintains employee records including department,
salary, and bonus details. The Human Resource department
frequently accesses this dataset to process payroll and evaluate
employee compensation
Employee   Department   Salary   Bonus
John   HR   30000   5000
Sara   IT   45000   8000
Mike   Finance   40000   7000
Nina   IT   42000   6000
Raj   HR   35000   5500
(Refer Dataset file for details)
i. Using the VLOOKUP function, retrieve the Salary of employee
"Sara".
=VLOOKUP("Sara", A2:D6, 3, FALSE)
= 45000   [2.5 Marks]
ii. If the dataset is arranged horizontally, use the HLOOKUP
function to find the bonus of "John"
=HLOOKUP("John", A1:E5, 4, FALSE)
=5000   [2.5 Marks]
********** 10 **********
--- page 11 ---
CO-2;   b. A domestic airline company monitors the number of passengers traveling   [5]
SO-;
per flight to optimize seat allocation and pricing strategies. Based on
BL-4;
BL-5   historical data, the number of passengers per flight follows a normal
distribution with a mean of 180 passengers and a standard deviation of
20 passengers. Variations occur due to seasonal demand, ticket pricing,
and travel trends. The airline management wants to analyze this data to
improve capacity planning and avoid overbooking or underutilization.
1. Using Excel, find the probability that fewer than 150 passengers travel
on a flight.
=NORM.DIST(150,180,20,TRUE)
P(X < 150) = 0.0668
2. Find the probability that more than 210 passengers travel.
=1-NORM.DIST(210,180,20,TRUE)
P(X > 210) = 0.0668
3. Determine the probability that passengers are between 160 and 200.
=NORM.DIST(200,180,20,TRUE)-NORM.DIST(160,180,20,TRUE)
P(160 < X < 200) = 0.6826
4. Find the passenger count such that only 5% of flights exceed this
number.
=NORM.INV(0.95,180,20)
=213
5. Should the airline regularly prepare for more than 210 passengers?
No, because the probability of exceeding 210 passengers is only
6.68%, indicating such situations are infrequent and do not justify
regular preparation
Q6   a. A company manufactures gadgets with the following details:   [15]
CO-2,3;   Selling Price = ₹800 per unit
SO-;
Variable Cost = ₹500 per unit
BL-4,
BL-5   Fixed Cost = ₹3,00,000 per month
********** 11 **********
--- page 12 ---
1. Prepare CVP income statement at 1,200 units
Units   1200
SP   800
Sales   960000
(-) VC   600000
Contribution   360000
(-) FC   300000
Profit   60000
2. Calculate Break-even point (units & ₹) using Formula
= 3,00,000 / 300 = 1,000 units
i.e. Fixed Costs / Contribution per unit
3. Prepare income statement at BEP level
Units   1000
SP   800
Sales   800000
(-) VC   500000
Contribution   300000
(-) FC   300000
Profit   0
4. Calculate PV Ratio and Margin of Safety (at 1,500 units)
= 300 / 800 = 37.5%
5. Draw B-E-P graph (can consider different levels of sales)
To be evaluated on actual
CO-2,3;   b.   Average   Customer   [5]
SO-;   Conversion   Delivery Time Monthly Sales
Product   Ratings
BL-4,   Rate (%)   (Days)   Revenue ($)
Price ($)   (1-5)
BL-5   3.64   69.98   3.74   4   138865.23
3.02   61.93   3.58   5   69071.92
3.42   48.93   4.5   5   89212.37
3.42   63.96   4.17   2   127090.24
2.63   40.97   4.69   2   126027.03
4.42   36.07   4.04   4   102120.53
3.54   42.16   3.74   1   136031.57
4.56   46.91   4.67   3   97432.72
4.63   52.87   4.27   2   155072.53
********** 12 **********
--- page 13 ---
3.03   56.53   3.76   2   118065.83
(Refer Dataset file for details)
1. Using the dataset provided, perform Correlation Analysis using
Excel Data Analysis ToolPak.
Convers   Custo   Monthl
ion   Average mer   Deliver   y Sales
Rate   Product   Rating y Time   Revenu
(%)   Price ($)   s (1-5)   (Days)   e ($)
Conversion Rate (%)   1
-
Average Product Price 0.2182
($)   1   1
Customer Ratings (1-   0.2010   -
5)   42   0.45071 1
-
0.0170   0.20753 0.082
Delivery Time (Days)   15   4   4   1
-
Monthly Sales   0.1838   0.08155 0.011   0.7244
Revenue ($)   48   7   858   8   1
2. Identify: The variable with the strongest and weakest correlation
with Monthly Sales Revenue
Strongest factor affecting revenue: Delivery Time (−0.72)
Weakest factor affecting revenue: Customer Ratings (0.01)
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.805052
R Square   0.648109
Adjusted R Square   0.366596
Standard Error   20780.2
Observations   10
ANOVA
Significan
df   SS   MS   F   ce F
9.94E   2.3022
Regression   4   3.98E+09 +08   33   0.192472
4.32E
Residual   5   2.16E+09 +08
Total   9   6.14E+09
********** 13 **********
--- page 14 ---
Coefficient   Standard   P-   Lower
s   Error   t Stat   value   95%
0.706   0.5113
Intercept   74705.04   105719.8 632   55   -197056
Conversion Rate   0.945   0.3877
(%)   9777.88   10341.03 542   99   -16804.6
Average Product   1.043   0.3443
Price ($)   757.8375   725.978   885   57   -1108.35
Customer Ratings   0.129   0.9022
(1-5)   2461.83   19058   176   54   -46528.3
-
Delivery Time   2.914   0.0332
(Days)   -14624.5   5017.714 57   23   -27522.9
4. Write the estimated regression equation.
= 74705.04 + 9777.88(Conversion Rate) + 757.84(Price) +
2461.83(Ratings) −14624.49(Delivery Time)
5. Interpret R Square significance of the model.
Model Quality:
• R² = 0.65 → ~65% variation explained (moderate fit)
• Significance F = 0.19 (> 0.05) → model not strongly significant
Variable Significance (p-values):
• Conversion Rate → 0.38
•   Price → 0.34
• Ratings → 0.90
• Delivery Time → 0.033 ✅ (significant)
Q7   a.   Following are the cash flows of two projects:   [15]
CO-3;
SO-;
BL-4,   Project X
BL-5   Year   0   1   2   3   4
Cash
-300   50   100   150   200
Flow
Project Y
Year   0   1   2   3   4
Cash
-300   150   120   80   60
Flow
********** 14 **********
--- page 15 ---
1. Calculate NPV at 9% using Excel.
Project X: ₹87.55
Project Y: ₹42.90
2. Calculate IRR.
Project X: ≈ 19.19%
Project Y: ≈ 16.57%
3. If required return = 11%, which project is preferable?
Project X is preferred as it gives highest return of 19.19% which is
over and above the required return of 11%
CO-1,2;   b.   Sunrise Builders (SB) is a medium-scale construction company focusing   [5]
SO-;
on affordable housing projects.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 9,000
•   Salaries of employees = Rs. 40,000
Each flat requires:
• Land cost = Rs. 70,000
• Construction materials = Rs. 30,000
• Labour = Rs. 20,000
•   Sales commission = Rs. 8,000 per flat
The selling price of each flat is Rs. 140,000.
Classify the above expenses into Fixed and Variable and Draw an
Income statement for the above parameters. Find out the B-E-P using
Goalseek technique (What-if-Analysis function). Round-off the final
answer if required.
Fixed Costs
Rent   8000
Utilities   9000
Salaries   40000
57000
********** 15 **********
--- page 16 ---
Variable Costs
Land   70000
Construction   30000
Labour   20000
Commission   8000
128000
Income statement
Units sold   1
Sales @ 150000   140000
VC   128000
Contribution   12000
FC   57000
Profit/(Loss)   -45000
BEP Using Goal Seek = 4.75 = 5 units
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 1e516fa987f8

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CyberSecurity_7010/Basic Decision making with Spreadsheet/ANS_Basic Decision making with Spreadsheet(702DB0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech (DS)/B. Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Basic Decision making with Spreadsheet
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks in Total
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1;   a.   Mention few uses of Spreadsheet (any 5)   [5]
SO- ;
-   Prepare Budgets & Forecasts
BL-2
-   Financial statement Preparation & Analysis
- Graphs and Charts
- Data Analytics
-   Inventory Management
-   Etc.
CO-2;   b.   Explain CVP Analysis and Break Even Point Analysis.   [5]
SO- ;
CVP Analysis
BL-4
• Cost-volume-profit (CVP) analysis is a financial tool that
examines the relationship between a company's costs, sales
volume, and profit
•   It helps businesses understand how changes in sales volume,
selling prices, and costs affect their profitability
• CVP analysis is often used to determine the break-even point,
which is the sales volume needed to cover all costs, and to plan
for different profit levels.
********** 1 **********
--- page 2 ---
Breakeven Analysis
•   It refers to the point at which total costs and total revenue are
equal.
• A break-even point analysis is used to determine the number of
units to be produced or overall revenue needed to cover total
costs (fixed and variable costs).
• Break-even analysis is important to business owners and
managers in determining how many units (or revenues) are
needed to cover fixed and variable expenses of the business.
• The formula for break-even analysis is as follows:
Break-Even Quantity = Fixed Costs / (Sales Price per Unit –
Variable Cost Per Unit)
CO-2 ;   c.   What are the types of Co-relation Co-efficient Values?   [5]
SO- ;
Explain how to interpret each type.
BL-3
Correla   Correlation type   Meaning
tion
coeffici
ent
value
1   Perfect positive   When one variable changes, the other
correlation   variables change in the same direction
(linearly). If the correlation coefficient
value is positive, then there is a similar
and identical relation between the two
variables.
0   Zero correlation   There is no relationship between the
variables.
********** 2 **********
--- page 3 ---
-1   Perfect negative   When one variable changes, the other
correlation   variables change in the opposite
direction. If the correlation coefficient
value is negative, it shows dissimilarity
between the two variables
CO-2 ;   d.   What is the difference in the objectivity behind using the Internal Rate of   [5]
SO- ;
Return (IRR) & Net Present Value (NPV) methods for evaluation of
BL-4
investment proposals.
Mention the underlying assumptions under each of the above two
methods of evaluation.
Parameters   NPV   IRR
Objective   Aims   to   maximise   Seeks to find the rate of
investment   value   by   return where cash inflows
comparing cash inflows   and outflows are equal
and outflows
Cash   Flows   Considers   all cash   Assumes a single   initial
Assumption   flows throughout   the   investment followed by a
project's duration   series of cash inflows
Reinvestment   Assumes   that   cash   Assumes that cash inflows
Assumption   inflows are reinvested at   are reinvested at the IRR
the discount rate   itself
Accuracy   It is assumes that future   It assumes that the rate of
Assumption   cash flows are accurately   return shall remain constant
known as of today   for all periods.
********** 3 **********
--- page 4 ---
Q2   a. A hospital is designing a lunch menu using rice, paneer, vegetables,   [15]
CO-3;   yogurt, and juice. The aim is to minimize cost while meeting patient
SO-;
nutritional requirements.
BL-4,
BL-5,   Each meal must satisfy total calories between 500 and 700. At least 20g
BL-6
of protein must be there in the meal. No more than 35% of calories from
fat and at least 50 mg of Vitamin C must be there in the meal. The content
and cost of each item are given below:
Food Item   Fat   Total   Vitamin   Protein   Cost ($)
Calories Calories C (mg)   (g)
Rice   30   200   0   4   0.25
(1 cup)
Paneer   120   250   0   20   1.50
(1 serving)
Vegetables   10   80   30   3   0.40
(1 cup)
Yogurt   50   150   2   6   0.60
(1 cup)
Juice   0   110   90   1   0.50
(1 cup)
1. Define the decision variables
x2 = serving of Paneer
2. Formulate the objective function
********** 4 **********
--- page 5 ---
3. Write all constraints
4. Solve the LPP equation and find out the minimum cost using
Solver
x1 = 1, x2 = 1, x3 = 1, x4 = 0, x5 = 0.5
Minimum cost Z = 2.40
b.   Consider the following data of Salary paid by the company to its   [5]
CO-1,2;
SO-;   employees;
BL-1,
BL-3,
1. Using excel formula, create employee labels;
Employee Label comprises of name of the Employee followed by
********** 5 **********

[Text in pictures on this page, read by OCR]
1. Calorie Constraint

500 < 2002; + 25022 + 8023 + 15024 + 11025 < 700

2. Protein Constraint

Ax, + 20x2 + 323 + 624 + las > 20

3. Vitamin C Constraint

3023 + 224 + 9025 > 50

4. Fat Constraint (< 35%)

302; + 120a2 + 1023 + 50r4 + Ors < 0.35(2002) + 25022 + 8023 + 15024

5. Non-negativity

21, £2,£3,%4,05 > 0
--- page 6 ---
‘-‘ followed by the Department in which the employee works
Eg: “Amit-HR”
. =CONCATE(A2, “ - ”, C2) → Alice - HR
Do the same for all employees
2. Using excel formula, find out the highest salary paid by the
company
= MAX(D2:D6) = 65000
3. Using excel formula, find the average salary expense of the
company.
= AVERAGE(D2:D6) = 55000
4. Find the position of “IT” in the Department column using the
relevant Excel formula.
= MATCH(“IT”, C2:C6, 0) → 3
5. Using excel Nested-IF function, find the total salary of employees
in the IT department.
= SUMIF(C2:C6,”IT”,D2:D6) = 125000
********** 6 **********
--- page 7 ---
Q3   a.   [15]
CO-3;
SO-;
BL-4,
BL-5,
BL-6
Suggestion / Conclusion: Suggested to opt for Plant-A as the EMV is the
highest under that option of 4,00,000
CO-2;
SO-;   b.   In an exam, A student guesses on 20 MCQs, each with 25% chance being   [5]
BL-4,   correct.
BL-5
Find
1. Probability of exactly 5 correct answers.
=BINOM.DIST(5, 20, 0.25, FALSE) = 0.202
********** 7 **********

[Text in pictures on this page, read by OCR]
High
800000
ct]
o4
Plant-A Moderate
1 300000
0 300000
O2
-200000
0 -200000
o4
High
500000
o4
Moderate
| 250000
QO 250000
O.2
-50000
Qo -50000
No Expansion
a ee oO
--- page 8 ---
2. Probability of at most 5 correct answers.
=BINOM.DIST(5, 20, 0.25, TRUE) = 0.616
3. Probability of at least 10 correct answers.
=1 - BINOM.DIST(9, 20, 0.25, TRUE)
4. Expected number of correct answers.
n x p = 5
=20*0.25
5. Standard deviation of correct answers.
=SQRT(20*0.25*0.75) = 1.94
Q4   a.   Read solution as 1,2,3,4 instead of a,b,c,d   [15]
CO-2;
SO-;
BL-3;
BL-4
********** 8 **********

[Text in pictures on this page, read by OCR]
(a) Probability (3 Marks)

7 = = 7, — f
Sof =25, P(X) = 35

(b) Mean, Variance, SD (6 Marks)

p= 6.96
ao = 1.36
o=117

(c) Excel (4 Marks)

VAR.P = 1.36, STDEV.P = 1.17
VARS = 1.42, STDEV.S = 1.19

(d) Interpretation (2 Marks)

Stable patient inflow
--- page 9 ---
CO-1,2;   b.   Consider the following dataset on project deadlines   [5]
SO-;
Project   Days Left
BL-1;
BL-3   P1   10
P2   25
P3   5
P4   15
P5   20
1. Categorize urgency using Nested IF functions (≤7 = Urgent, ≤15 =
Moderate, else Relaxed).
=IF(B2<=7,"Urgent",IF(B2<=15,"Moderate","Relaxed")) → P1 =
Moderate
2. Find out the Lowest number of days left and mention which Project
it belongs to
=MIN(B2:B6) = 5 Days = P3 [Can also use Index and Match (Min)]
3. Check if project is within 30 days using AND
=AND(B2<=30) → TRUE
4. Rank projects by days left
=RANK(B2,B2:B6) → P1 = 5
5. Average days left (rounded to integer)
=ROUND(AVERAGE(B2:B6),0) → 15
Q5   a.   The dataset given below contains healthcare service records including   [15]
CO-2,3;   hospital, department, doctor, and patient details. It is designed to analyze
SO-;
service load, patient distribution, and operational efficiency across
BL-4;
BL-6   hospitals.
.
No.
Servic   Avg   Satisf
Dat Hospita   Patien Docto   of
Dept e   Billin action
e   l   t Type   r   Patie
Type   g   Rating
nts
(Refer Dataset file for details)
********** 9 **********
--- page 10 ---
1. Create a Pivot Table showing Doctor-wise total number of patients
and sort the results from highest to lowest. Based on the Pivot Table,
identify the doctor handling the highest workload – [3 Marks]
2. Insert a Pivot Chart comparing Service Type-wise patient activity
across hospitals and interpret which service type is most active and
how healthcare activity differs across hospitals – [3 Marks]
3. Create a Pivot Table showing total number of patients by Patient
Type and insert a Slicer for Hospital. State a short conclusion about
hospital-wise patient behavior – [4 Marks]
4. An organization maintains employee records including department,
salary, and bonus details. The Human Resource department
frequently accesses this dataset to process payroll and evaluate
employee compensation
Employee   Department   Salary   Bonus
John   HR   30000   5000
Sara   IT   45000   8000
Mike   Finance   40000   7000
Nina   IT   42000   6000
Raj   HR   35000   5500
(Refer Dataset file for details)
i. Using the VLOOKUP function, retrieve the Salary of employee
"Sara".
=VLOOKUP("Sara", A2:D6, 3, FALSE)
= 45000   [2.5 Marks]
ii. If the dataset is arranged horizontally, use the HLOOKUP
function to find the bonus of "John"
=HLOOKUP("John", A1:E5, 4, FALSE)
=5000   [2.5 Marks]
********** 10 **********
--- page 11 ---
CO-2;   b. A domestic airline company monitors the number of passengers traveling   [5]
SO-;
per flight to optimize seat allocation and pricing strategies. Based on
BL-4;
BL-5   historical data, the number of passengers per flight follows a normal
distribution with a mean of 180 passengers and a standard deviation of
20 passengers. Variations occur due to seasonal demand, ticket pricing,
and travel trends. The airline management wants to analyze this data to
improve capacity planning and avoid overbooking or underutilization.
1. Using Excel, find the probability that fewer than 150 passengers travel
on a flight.
=NORM.DIST(150,180,20,TRUE)
P(X < 150) = 0.0668
2. Find the probability that more than 210 passengers travel.
=1-NORM.DIST(210,180,20,TRUE)
P(X > 210) = 0.0668
3. Determine the probability that passengers are between 160 and 200.
=NORM.DIST(200,180,20,TRUE)-NORM.DIST(160,180,20,TRUE)
P(160 < X < 200) = 0.6826
4. Find the passenger count such that only 5% of flights exceed this
number.
=NORM.INV(0.95,180,20)
=213
5. Should the airline regularly prepare for more than 210 passengers?
No, because the probability of exceeding 210 passengers is only
6.68%, indicating such situations are infrequent and do not justify
regular preparation
Q6   a. A company manufactures gadgets with the following details:   [15]
CO-2,3;   Selling Price = ₹800 per unit
SO-;
Variable Cost = ₹500 per unit
BL-4,
BL-5   Fixed Cost = ₹3,00,000 per month
********** 11 **********
--- page 12 ---
1. Prepare CVP income statement at 1,200 units
Units   1200
SP   800
Sales   960000
(-) VC   600000
Contribution   360000
(-) FC   300000
Profit   60000
2. Calculate Break-even point (units & ₹) using Formula
= 3,00,000 / 300 = 1,000 units
i.e. Fixed Costs / Contribution per unit
3. Prepare income statement at BEP level
Units   1000
SP   800
Sales   800000
(-) VC   500000
Contribution   300000
(-) FC   300000
Profit   0
4. Calculate PV Ratio and Margin of Safety (at 1,500 units)
= 300 / 800 = 37.5%
5. Draw B-E-P graph (can consider different levels of sales)
To be evaluated on actual
CO-2,3;   b.   Average   Customer   [5]
SO-;   Conversion   Delivery Time Monthly Sales
Product   Ratings
BL-4,   Rate (%)   (Days)   Revenue ($)
Price ($)   (1-5)
BL-5   3.64   69.98   3.74   4   138865.23
3.02   61.93   3.58   5   69071.92
3.42   48.93   4.5   5   89212.37
3.42   63.96   4.17   2   127090.24
2.63   40.97   4.69   2   126027.03
4.42   36.07   4.04   4   102120.53
3.54   42.16   3.74   1   136031.57
4.56   46.91   4.67   3   97432.72
4.63   52.87   4.27   2   155072.53
********** 12 **********
--- page 13 ---
3.03   56.53   3.76   2   118065.83
(Refer Dataset file for details)
1. Using the dataset provided, perform Correlation Analysis using
Excel Data Analysis ToolPak.
Convers   Custo   Monthl
ion   Average mer   Deliver   y Sales
Rate   Product   Rating y Time   Revenu
(%)   Price ($)   s (1-5)   (Days)   e ($)
Conversion Rate (%)   1
-
Average Product Price 0.2182
($)   1   1
Customer Ratings (1-   0.2010   -
5)   42   0.45071 1
-
0.0170   0.20753 0.082
Delivery Time (Days)   15   4   4   1
-
Monthly Sales   0.1838   0.08155 0.011   0.7244
Revenue ($)   48   7   858   8   1
2. Identify: The variable with the strongest and weakest correlation
with Monthly Sales Revenue
Strongest factor affecting revenue: Delivery Time (−0.72)
Weakest factor affecting revenue: Customer Ratings (0.01)
3. Run Regression Analysis using Excel Data Analysis ToolPak.
Regression Statistics
Multiple R   0.805052
R Square   0.648109
Adjusted R Square   0.366596
Standard Error   20780.2
Observations   10
ANOVA
Significan
df   SS   MS   F   ce F
9.94E   2.3022
Regression   4   3.98E+09 +08   33   0.192472
4.32E
Residual   5   2.16E+09 +08
Total   9   6.14E+09
********** 13 **********
--- page 14 ---
Coefficient   Standard   P-   Lower
s   Error   t Stat   value   95%
0.706   0.5113
Intercept   74705.04   105719.8 632   55   -197056
Conversion Rate   0.945   0.3877
(%)   9777.88   10341.03 542   99   -16804.6
Average Product   1.043   0.3443
Price ($)   757.8375   725.978   885   57   -1108.35
Customer Ratings   0.129   0.9022
(1-5)   2461.83   19058   176   54   -46528.3
-
Delivery Time   2.914   0.0332
(Days)   -14624.5   5017.714 57   23   -27522.9
4. Write the estimated regression equation.
= 74705.04 + 9777.88(Conversion Rate) + 757.84(Price) +
2461.83(Ratings) −14624.49(Delivery Time)
5. Interpret R Square significance of the model.
Model Quality:
• R² = 0.65 → ~65% variation explained (moderate fit)
• Significance F = 0.19 (> 0.05) → model not strongly significant
Variable Significance (p-values):
• Conversion Rate → 0.38
•   Price → 0.34
• Ratings → 0.90
• Delivery Time → 0.033 ✅ (significant)
Q7   a.   Following are the cash flows of two projects:   [15]
CO-3;
SO-;
BL-4,   Project X
BL-5   Year   0   1   2   3   4
Cash
-300   50   100   150   200
Flow
Project Y
Year   0   1   2   3   4
Cash
-300   150   120   80   60
Flow
********** 14 **********
--- page 15 ---
1. Calculate NPV at 9% using Excel.
Project X: ₹87.55
Project Y: ₹42.90
2. Calculate IRR.
Project X: ≈ 19.19%
Project Y: ≈ 16.57%
3. If required return = 11%, which project is preferable?
Project X is preferred as it gives highest return of 19.19% which is
over and above the required return of 11%
CO-1,2;   b.   Sunrise Builders (SB) is a medium-scale construction company focusing   [5]
SO-;
on affordable housing projects.
BL-2,
BL-3   The company incurs the following monthly expenses:
•   Office rent = Rs. 8,000
•   Utilities and maintenance = Rs. 9,000
•   Salaries of employees = Rs. 40,000
Each flat requires:
• Land cost = Rs. 70,000
• Construction materials = Rs. 30,000
• Labour = Rs. 20,000
•   Sales commission = Rs. 8,000 per flat
The selling price of each flat is Rs. 140,000.
Classify the above expenses into Fixed and Variable and Draw an
Income statement for the above parameters. Find out the B-E-P using
Goalseek technique (What-if-Analysis function). Round-off the final
answer if required.
Fixed Costs
Rent   8000
Utilities   9000
Salaries   40000
57000
********** 15 **********
--- page 16 ---
Variable Costs
Land   70000
Construction   30000
Labour   20000
Commission   8000
128000
Income statement
Units sold   1
Sales @ 150000   140000
VC   128000
Contribution   12000
FC   57000
Profit/(Loss)   -45000
BEP Using Goal Seek = 4.75 = 5 units
********** 16 **********
````
