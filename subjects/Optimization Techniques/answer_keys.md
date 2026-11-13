# Optimization Techniques: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 2c59e9f531be

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIDS_7056/Optimization Techniques/ANS_Optimization Techniques(702AI0C031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (11 pages), mean OCR confidence 78.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Optimization Techniques
Date: 08 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [10]
CO-1,4;   a.   5
BL-
Apply
********** 1 **********
--- page 2 ---
CO-1,3;   b. By applying NWCM, we have initial solution   5
BL-   Plant Distribution Center   Supply
Apply
D1   D2   D3   D4
P1   2   6   3   11   7   6
P2   1   0   6   1   1
1
P3   5   8   5   15   3   9   2   10
Demand   7   5   3   2   17
Since number of occupied cells = 5 and m+n-1 = 6.
So, solution is degenerate.
CO-1,2;   c.   (i)   Maximin criterion   5
BL-   Summer   Flavor of the soft drink
Apply   Condition   Orange   Normal   Lime
Growth
Mild   16   13   11
Moderate   10   12   14
Severe   12   9   15
Very Severe   7   9   14
Column   7   9   11
Minimum
Maximin = Maximum (column Minimum) = 11.   (2 marks)
Best Strategy Chosen to launch is Lime.   (0.5 marks)
(ii)   Hurwicz Criterion
Given the coefficient of optimism, α equal to 0.7, the coefficient of
pessimism is 1- 0.7 = 0.3. then according to this criterion, select best
(Maximum) payoff and worst (Minimum) payoff. As we know that,
Hurwicz = α x maximum payoff + (1 – α) x Minimum payoff
Alternative   Maximum   Minimum   Hurwicz
Investment   Payoff   Payoff
Orange   16   7   13.3
Mango   13   9   11.8
Lime   15   11   13.8
(2 marks)
Best Strategy (Course of Action) Chosen to launch is Lime. (0.5 marks)
CO-1,2;   d.   5
BL-   Row   Minimum
Analyze   A1   -2
A2   -2
A3   -3
A4   -2
Maximin = max (-2, -2, -3, -2) = -2 [Marks: 1.5]
Column   Maximum
B1   3
B2   2
B3   2
B4   2
Minimax = min (3, 2, 2, 2) = 2 [Marks: 1.5]
A game is fair if value of the game is 0. [Marks=1]
********** 2 **********
--- page 3 ---
Q2   [20]
CO-1,2; a   (i) Pessimistic or Maximin criterion:   10
BL-   Strategy   State of Nature   Row
Analyze   N1   N2   N3   N4   minimum
S1   4,000   -100   6,000 18,000   -100
S2   20,000   5,000   400   0   0
S3   20,000 15,000 -2,000   1,000   -2000
Maximin = max (row minimum) = 0.
So, Best Strategy Chosen is S2.
(ii)   Optimistic or Maximax Criterion
Strategy   State of Nature   Row
N1   N2   N3   N4   maximum
S1   4,000   -100   6,000 18,000   18000
S2   20,000   5,000   400   0   20000
S3   20,000 15,000 -2,000   1,000   20000
Maximax = max (row maximum) = 20000.
So, Best Strategy Chosen is S2 or S3.
(iii)   Hurwicz criterion
Given the coefficient of optimism, α equal to 0.7, the coefficient of
pessimism is 1- 0.7 = 0.3. then according to this criterion, select best
(Maximum) payoff and worst (Minimum) payoff. As we know that,
Hurwicz = α x maximum payoff + (1 – α) x Minimum payoff
Strategy   Row maximum Row minimum   Hurwicz
S1   18000   -100   12570
S2   20000   0   14000
S3   20000   -2000   13400
Best of Hurwicz criterion = 14000
Therefore, best strategy chosen is S2.
(iv)   Minimax Regret criterion:
Regret table is given below:
Strategy   State of Nature   Row
N1   N2   N3   N4   maximum
S1   20000-4,000   15000-(-100)   6,000 -6000   18,000 –   16000
= 16000   = 15100   = 0   18000 = 0
S2   20,000-20000   15000-5,000   6000-400   18000   18000
= 0   = 10000   =5600
S3   20,000-20000 15000-15,000   6000-(-   18000-1,000   17000
= 0   = 0   2,000) =   = 17000
8000
Minimax = min (row maximum) = 16000
So, Best Strategy Chosen is S1.
CO-1,4; b   Decision Variables-----------------1M   10
BL-   Let: x = quantity of milk (in 1000 litres) ,   y = quantity of butter (in 100 kg)
Apply   Objective function:---------------------1M
Min Z =(15000+18000)x+(26000+28000)y=33000x+54000y
Constraints:--------------------3M
********** 3 **********
--- page 4 ---
Plant | time constraint

3c +y <16
Plant Il time constraint
22+ 1by < 16

Demand constraints

e>4

y>2
Non-negativity

zy20

Graphical solution

x1 x2 RHS
33000 54000

Constraint 1 3 1 = 16

Constraint 2 2 15 <= 16

Constraint 3 1 0 >= 4

Constraint 4 0 1 = 2

Solution-> 4 2 240000
Q3 [20]
CO-1,4; a Maximize 10
BL Z = 102, + 6x2 + 423 + 0s; +0

= 10x, + 6x2 + 4x3 + 08) + O82

Apply

Subject to:
ay +ao+23+ 81 = 100
22, + 2xy + 6x3 + So = 300

©1,€2,€3, 81,82 >0

FIC 7) IC HOH
--- page 5 ---
Writing std form---------------2M
Iteration 1(table, cj-zj, KC, KR etc)-----------------3M
Calculations for iteration2--------------3M
Iteration2 (table, cj-zj)----------------1M
Final ans----------------1M
CO-1,2; b   Given from question,   10
BL-   • Cost price (C) = Rs 2
Analyze   •   Selling price (SP) = Rs 4
So, Profit cases:
Sold vaccine dose profit = 4 - 2 = Rs 2
Unsold dose loss = Rs 2 loss
Q \ D   20   25   40   60
Prob.   0.1   0.3   0.5   0.1
20   40   40   40   40
25   30   50   50   50
40   0   20   80   80
60   -40   -20   40   120
So, EMV for each option is calculated as,
EMV (20)   40 x 0.1+ 40 x 0.3+40x0.5+40x 0.1 = 40
EMV (25)   30x0.1+50 x0.3 + 50x0.5+50x0.1 = 48
EMV (40)   0 x 0.1 + 20x0.3+80x0.5+80x0.1 = 54
EMV (60)   -40 x 0.1 + (-20) x 0.3 + 40 x 0.5+120 x 0.1 = 22
Best EMV = 54.
So, Best Strategy to stock doses is 40.
(ii) EOL
Max payoff for each demand:
Demand   Max payoff
20   40
25   50
40   80
60   120
********** 5 **********

[Text in pictures on this page, read by OCR]
io)

Iteration 1
it}
it}

Iteration 2
10
it}

Basic 10 6 2B 0 0

Variables Quantity Xt x2 slack 1 slack 2
slack 1 100
slack 2 300 2 2 6 0 1
z 0 0 0 0 0 0
cz)
100
slack 2 100 0 0 4 2 1
z 1,000 10 10 10 10 0

cj oO -4 6 10 0
--- page 6 ---
Regret or Opportunity Loss table is calculated as:
Q\D   20   25   40   60
Prob.   0.1   0.3   0.5   0.1
20   0   10   40   80
25   10   0   30   70
40   40   30   0   40
60   80   70   40   0
Expected Opportunity loss is calculated for each option:
EOL (20) = 0(0.1) +10(0.3) +40 (0.5) +80(0.1) = 31
EOL (25) = 10(0.1) +0(0.3) +30 (0.5) +70(0.1) = 23
EOL (40) = 40(0.1) +30(0.3) +0 (0.5) +40(0.1) = 17
EOL (60) = 80(0.1) +70(0.3) +40 (0.5) +0(0.1) = 49
Minimum Expected Opportunity Loss (EOL) = Rs 17
Best strategy chosen is stock of 40 doses.
Q4   [20]
CO-1,4; a   10
BL-
Apply
Iteration-1(for given table calculation of zj, cj-zj, KC, KR etc)----------------- 4M
Calculations for iteration-2--------------3M
Iteration-2 (table, zj, cj-zj)----------------2M
Final Ans----------------1M
CO-1,4; b   Solve LP Relaxation: [3 Marks]   10
BL-
Ignore the integer restriction first.
Analyze
Solving the problem, A graphically, we find that:
gives: X₁ =3, X₂ =2.5 which is an LP optimal solution
Solving Sub-Problem B: 2 Marks
Solving Sub-Problem C: 1 Marks
Solving Sub-Problem D: 2 Marks
Solving Sub-Problem E: 1 Marks
********** 6 **********

[Text in pictures on this page, read by OCR]
a. mene t

}-~——,~——3 | 0 ig I 0 1 ya
-_ 2 2 1 Y) = 0 0 jundefined|
0 e avi \cao 1 0 1 0 a

rF 10 =—M -M-10 0 -M

Prseegine 0 M+12 M+10 0 0

, : _|

2 % 3 0 1 1 0
. 2 | 2 0 al 0

| 0 S; 1 0 a iF i

| Zz 6 10 12 2 0
52% 0 0 2 0 =|

Since all entries in the C)-
solution is arrived at and is aken wy
*1 = 10, xp»

Problem 3.9& A» ac. rn.

row are either zero or negative, the optimum

-
--- page 7 ---
Branch and bound algorithm thus terminated and the optimal integer solution is:
ZD=26 and X₁ =3, X₂ =2 [1 Marks]
Q5   [20]
CO-   a   10
1,3;
BL-
Analyze
********** 7 **********
--- page 8 ---
CO-   b Step 1: Row Dominance (1 Marks)   10
1,2;   • Row2 dominates Row3 → remove Row3.
BL-   Step 2 Column Dominance (1 Marks)
Analyze   • Col1 dominates Col3 → remove Col3
Reduced Matrix (1 Marks)
I   II   IV
1   3   5   2
2   6   4   5
4   5   2   4
Step 3: Row Dominance (1 Marks)
Row2 dominates Row4 → remove Row4
I   II   IV
1   3   5   2
2   6   4   5
Column Dominance (1 Marks)
B4 dominates B1 → remove B1
II   IV
1   5   2
2   4   5
Check Saddle Point (1 Marks)
Maximin is not equal to Minimax
• Saddle Point does not exist
Finding the Probability for Y (1.5)
1 = 1/4
2 = 3/4
Finding the Probability for X (1.5)
II= ¾
IV= ¼
Value of the Game=4.25 (1 Marks)
Q6   [20]
CO-1,3; a   10
BL-   Step1. Row reduction Matrix:
Apply   Operators
1   2   3   4   5   Row
minimum
A   2   4   7   4   0   7
Jobs
B   0   9   7   7   4   6
C   6   7   0   2   2   6
D   2   0   1   3   0   9
E   0   5   7   3   7   7
Step 2: Column reduction matrix:
Operators
1   2   3   4   5
A   2   4   7   2   0
Jobs   B   0   9   7   5   4
C   6   7   0   0   2
D   2   0   1   1   0
E   0   5   7   1   7
Column   0   0   0   2   0
minimum
Step 3: Make assignment on modified matrix by applying row scanning and then column
scanning:
********** 8 **********
--- page 9 ---
Optimal   Operator   Operator   Operator   Operator   Operator
solution   1   2   3   4   5
value = 38
Job A   9   11   14   11   Assign 7
Job B   Assign 6   15   13   13   10
Job C   12   13   Assign 6   8   8
Job D   11   Assign 9   10   12   9
Job E   7   12   14   Assign 10   14
JOB   Assigned to   Cost
Job A   Operator 5   7
Job B   Operator 1   6
Job C   Operator 3   6
Job D   Operator 2   9
Job E   Operator 4   10
Total   38
•   Correct cost matrix formulation → 1 Mark
• Row reduction → 2 Marks
• Column reduction → 2 Marks
•   Optimality check (covering zeros) → 2 Marks
•   Final optimal assignment → 2 Mark
•   Total minimum cost (23) → 1 Mark
CO-1,4; b   10
BL-   Iteration 1: Adding Cj-Zj row (02 Marks]
Analyze   Cj   5   2   0   0
CB   Basis   x1   x2   S1   S2   RHS
5   x1   1   0   0.5   -0.5   1.5
2   x2   0   1   -0.5   1.5   2.5
Zj   Z=12.5   5   2   1.5   0.5
Cj-Zj   0   0   -1.5   -0.5
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=1.5,x2=2.5, Max Z=12.5
Add Gomory Cut [02 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut,
with the help of x1-row as follows:
1.5=1x1+0.5S1-0.5S2
The fractional cut will become
-0.5=Sg1-0.5S1-0.5S2→ (Cut-1)
Adding this additional constraint at the bottom of optimal simplex table. The new table
so obtained is [03 Marks]
Cj   5   2   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1 RHS
5   x1   1   0   0.5   -0.5   0   1.5
2   x2   0   1   -0.5   1.5   0   2.5
0   Sg1   0   0   -0.5   (-0.5)   1   -
0.5→
Z=12.5   Zj   5   2   1.5   0.5   0
********** 9 **********
--- page 10 ---
Cj-Zj   0   0   -1.5   -0.5   0
Ratio=Cj-Zj   --   --   3   1↑   --
/Sg1,j
and Sg1,j<0
Most negative RHS is -0.5 and its row index is 3. So, the leaving basis variable is Sg1.
Least positive ratio is 1 and its column index is 4. So, the entering variable is S2.
Iteration 2 [02 Marks]
Cj   5   2   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1   RHS
5   x1   1   0   1   0   -1   2
2   x2   0   1   -2   0   3   1
0   S2   0   0   1   1   -2   1
Z=12   Zj   5   2   1   0   1
Cj-Zj   0   0   -1   0   -1
Ratio
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as:
x1=2, x2=1, Max Z=12 [01 Marks]
Q7   [20]
CO-1,3; a   Since no. of rows is not equal to no. of column, so this unbalanced. So, add Dummy   8
BL-   column to make problem balanced.
Analyze   Optimal   A   B   C   D
solution
value = 35
1   (Assign) 9   26   15   0
2   13   27   (Assign) 6   0
3   35   (Assign) 20   15   0
4   18   30   20   (Assign) 0
Machine   Assigned to Jobs   Cost
1   A   9
2   C   6
3   B   20
4   D   0
Total   35
CO-1,4; b   6
BL-
Apply
-------------------4M
-------------------2M
********** 10 **********
--- page 11 ---
CO-1,4; c   6
BL-   1. Concept [01 Marks]
Apply   In some linear programming problems, the optimal solution obtained from LP relaxation
contains fractional values, whereas the problem requires integer solutions.
The Branch and Bound method are used to systematically find the best integer solution.
2. Short Example (can be any) [01 Marks]
Maximize
Z=3x+2y
Subject to
2x + y ≤ 7, x + 2y ≤7,
x, y ≥ 0
LP relaxation solution:
x=2.33, y=2.33(fractional)
3. Branching [01 Marks]
Choose a fractional variable (say x=2.33):
Create two branches:
• Branch 1: x≤2
• Branch 2: x≥3
4. Solving Subproblems [01 Marks]
Each branch is solved as a new LP:
• Branch 1 may give a feasible integer or fractional solution
• Branch 2 is solved similarly
If a solution is still fractional → further branching is done
5. Bounding [01 Marks]
• Keep track of the best integer solution found
•   If a branch gives a worse objective value than the current best → discard (fathom)
that branch
6. Termination [01 Marks]
The process continues until:
•   All branches are either explored or eliminated
• The best remaining solution is integer and optimal
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 084c21ef5dc9

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIML_7053/Optimization Techniques/ANS_Optimization Techniques(702AI0C031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (11 pages), mean OCR confidence 78.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Optimization Techniques
Date: 08 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [10]
CO-1,4;   a.   5
BL-
Apply
********** 1 **********
--- page 2 ---
CO-1,3;   b. By applying NWCM, we have initial solution   5
BL-   Plant Distribution Center   Supply
Apply
D1   D2   D3   D4
P1   2   6   3   11   7   6
P2   1   0   6   1   1
1
P3   5   8   5   15   3   9   2   10
Demand   7   5   3   2   17
Since number of occupied cells = 5 and m+n-1 = 6.
So, solution is degenerate.
CO-1,2;   c.   (i)   Maximin criterion   5
BL-   Summer   Flavor of the soft drink
Apply   Condition   Orange   Normal   Lime
Growth
Mild   16   13   11
Moderate   10   12   14
Severe   12   9   15
Very Severe   7   9   14
Column   7   9   11
Minimum
Maximin = Maximum (column Minimum) = 11.   (2 marks)
Best Strategy Chosen to launch is Lime.   (0.5 marks)
(ii)   Hurwicz Criterion
Given the coefficient of optimism, α equal to 0.7, the coefficient of
pessimism is 1- 0.7 = 0.3. then according to this criterion, select best
(Maximum) payoff and worst (Minimum) payoff. As we know that,
Hurwicz = α x maximum payoff + (1 – α) x Minimum payoff
Alternative   Maximum   Minimum   Hurwicz
Investment   Payoff   Payoff
Orange   16   7   13.3
Mango   13   9   11.8
Lime   15   11   13.8
(2 marks)
Best Strategy (Course of Action) Chosen to launch is Lime. (0.5 marks)
CO-1,2;   d.   5
BL-   Row   Minimum
Analyze   A1   -2
A2   -2
A3   -3
A4   -2
Maximin = max (-2, -2, -3, -2) = -2 [Marks: 1.5]
Column   Maximum
B1   3
B2   2
B3   2
B4   2
Minimax = min (3, 2, 2, 2) = 2 [Marks: 1.5]
A game is fair if value of the game is 0. [Marks=1]
********** 2 **********
--- page 3 ---
Q2   [20]
CO-1,2; a   (i) Pessimistic or Maximin criterion:   10
BL-   Strategy   State of Nature   Row
Analyze   N1   N2   N3   N4   minimum
S1   4,000   -100   6,000 18,000   -100
S2   20,000   5,000   400   0   0
S3   20,000 15,000 -2,000   1,000   -2000
Maximin = max (row minimum) = 0.
So, Best Strategy Chosen is S2.
(ii)   Optimistic or Maximax Criterion
Strategy   State of Nature   Row
N1   N2   N3   N4   maximum
S1   4,000   -100   6,000 18,000   18000
S2   20,000   5,000   400   0   20000
S3   20,000 15,000 -2,000   1,000   20000
Maximax = max (row maximum) = 20000.
So, Best Strategy Chosen is S2 or S3.
(iii)   Hurwicz criterion
Given the coefficient of optimism, α equal to 0.7, the coefficient of
pessimism is 1- 0.7 = 0.3. then according to this criterion, select best
(Maximum) payoff and worst (Minimum) payoff. As we know that,
Hurwicz = α x maximum payoff + (1 – α) x Minimum payoff
Strategy   Row maximum Row minimum   Hurwicz
S1   18000   -100   12570
S2   20000   0   14000
S3   20000   -2000   13400
Best of Hurwicz criterion = 14000
Therefore, best strategy chosen is S2.
(iv)   Minimax Regret criterion:
Regret table is given below:
Strategy   State of Nature   Row
N1   N2   N3   N4   maximum
S1   20000-4,000   15000-(-100)   6,000 -6000   18,000 –   16000
= 16000   = 15100   = 0   18000 = 0
S2   20,000-20000   15000-5,000   6000-400   18000   18000
= 0   = 10000   =5600
S3   20,000-20000 15000-15,000   6000-(-   18000-1,000   17000
= 0   = 0   2,000) =   = 17000
8000
Minimax = min (row maximum) = 16000
So, Best Strategy Chosen is S1.
CO-1,4; b   Decision Variables-----------------1M   10
BL-   Let: x = quantity of milk (in 1000 litres) ,   y = quantity of butter (in 100 kg)
Apply   Objective function:---------------------1M
Min Z =(15000+18000)x+(26000+28000)y=33000x+54000y
Constraints:--------------------3M
********** 3 **********
--- page 4 ---
Plant | time constraint

3c +y <16
Plant Il time constraint
22+ 1by < 16

Demand constraints

e>4

y>2
Non-negativity

zy20

Graphical solution

x1 x2 RHS
33000 54000

Constraint 1 3 1 = 16

Constraint 2 2 15 <= 16

Constraint 3 1 0 >= 4

Constraint 4 0 1 = 2

Solution-> 4 2 240000
Q3 [20]
CO-1,4; a Maximize 10
BL Z = 102, + 6x2 + 423 + 0s; +0

= 10x, + 6x2 + 4x3 + 08) + O82

Apply

Subject to:
ay +ao+23+ 81 = 100
22, + 2xy + 6x3 + So = 300

©1,€2,€3, 81,82 >0

FIC 7) IC HOH
--- page 5 ---
Writing std form---------------2M
Iteration 1(table, cj-zj, KC, KR etc)-----------------3M
Calculations for iteration2--------------3M
Iteration2 (table, cj-zj)----------------1M
Final ans----------------1M
CO-1,2; b   Given from question,   10
BL-   • Cost price (C) = Rs 2
Analyze   •   Selling price (SP) = Rs 4
So, Profit cases:
Sold vaccine dose profit = 4 - 2 = Rs 2
Unsold dose loss = Rs 2 loss
Q \ D   20   25   40   60
Prob.   0.1   0.3   0.5   0.1
20   40   40   40   40
25   30   50   50   50
40   0   20   80   80
60   -40   -20   40   120
So, EMV for each option is calculated as,
EMV (20)   40 x 0.1+ 40 x 0.3+40x0.5+40x 0.1 = 40
EMV (25)   30x0.1+50 x0.3 + 50x0.5+50x0.1 = 48
EMV (40)   0 x 0.1 + 20x0.3+80x0.5+80x0.1 = 54
EMV (60)   -40 x 0.1 + (-20) x 0.3 + 40 x 0.5+120 x 0.1 = 22
Best EMV = 54.
So, Best Strategy to stock doses is 40.
(ii) EOL
Max payoff for each demand:
Demand   Max payoff
20   40
25   50
40   80
60   120
********** 5 **********

[Text in pictures on this page, read by OCR]
io)

Iteration 1
it}
it}

Iteration 2
10
it}

Basic 10 6 2B 0 0

Variables Quantity Xt x2 slack 1 slack 2
slack 1 100
slack 2 300 2 2 6 0 1
z 0 0 0 0 0 0
cz)
100
slack 2 100 0 0 4 2 1
z 1,000 10 10 10 10 0

cj oO -4 6 10 0
--- page 6 ---
Regret or Opportunity Loss table is calculated as:
Q\D   20   25   40   60
Prob.   0.1   0.3   0.5   0.1
20   0   10   40   80
25   10   0   30   70
40   40   30   0   40
60   80   70   40   0
Expected Opportunity loss is calculated for each option:
EOL (20) = 0(0.1) +10(0.3) +40 (0.5) +80(0.1) = 31
EOL (25) = 10(0.1) +0(0.3) +30 (0.5) +70(0.1) = 23
EOL (40) = 40(0.1) +30(0.3) +0 (0.5) +40(0.1) = 17
EOL (60) = 80(0.1) +70(0.3) +40 (0.5) +0(0.1) = 49
Minimum Expected Opportunity Loss (EOL) = Rs 17
Best strategy chosen is stock of 40 doses.
Q4   [20]
CO-1,4; a   10
BL-
Apply
Iteration-1(for given table calculation of zj, cj-zj, KC, KR etc)----------------- 4M
Calculations for iteration-2--------------3M
Iteration-2 (table, zj, cj-zj)----------------2M
Final Ans----------------1M
CO-1,4; b   Solve LP Relaxation: [3 Marks]   10
BL-
Ignore the integer restriction first.
Analyze
Solving the problem, A graphically, we find that:
gives: X₁ =3, X₂ =2.5 which is an LP optimal solution
Solving Sub-Problem B: 2 Marks
Solving Sub-Problem C: 1 Marks
Solving Sub-Problem D: 2 Marks
Solving Sub-Problem E: 1 Marks
********** 6 **********

[Text in pictures on this page, read by OCR]
a. mene t

}-~——,~——3 | 0 ig I 0 1 ya
-_ 2 2 1 Y) = 0 0 jundefined|
0 e avi \cao 1 0 1 0 a

rF 10 =—M -M-10 0 -M

Prseegine 0 M+12 M+10 0 0

, : _|

2 % 3 0 1 1 0
. 2 | 2 0 al 0

| 0 S; 1 0 a iF i

| Zz 6 10 12 2 0
52% 0 0 2 0 =|

Since all entries in the C)-
solution is arrived at and is aken wy
*1 = 10, xp»

Problem 3.9& A» ac. rn.

row are either zero or negative, the optimum

-
--- page 7 ---
Branch and bound algorithm thus terminated and the optimal integer solution is:
ZD=26 and X₁ =3, X₂ =2 [1 Marks]
Q5   [20]
CO-   a   10
1,3;
BL-
Analyze
********** 7 **********
--- page 8 ---
CO-   b Step 1: Row Dominance (1 Marks)   10
1,2;   • Row2 dominates Row3 → remove Row3.
BL-   Step 2 Column Dominance (1 Marks)
Analyze   • Col1 dominates Col3 → remove Col3
Reduced Matrix (1 Marks)
I   II   IV
1   3   5   2
2   6   4   5
4   5   2   4
Step 3: Row Dominance (1 Marks)
Row2 dominates Row4 → remove Row4
I   II   IV
1   3   5   2
2   6   4   5
Column Dominance (1 Marks)
B4 dominates B1 → remove B1
II   IV
1   5   2
2   4   5
Check Saddle Point (1 Marks)
Maximin is not equal to Minimax
• Saddle Point does not exist
Finding the Probability for Y (1.5)
1 = 1/4
2 = 3/4
Finding the Probability for X (1.5)
II= ¾
IV= ¼
Value of the Game=4.25 (1 Marks)
Q6   [20]
CO-1,3; a   10
BL-   Step1. Row reduction Matrix:
Apply   Operators
1   2   3   4   5   Row
minimum
A   2   4   7   4   0   7
Jobs
B   0   9   7   7   4   6
C   6   7   0   2   2   6
D   2   0   1   3   0   9
E   0   5   7   3   7   7
Step 2: Column reduction matrix:
Operators
1   2   3   4   5
A   2   4   7   2   0
Jobs   B   0   9   7   5   4
C   6   7   0   0   2
D   2   0   1   1   0
E   0   5   7   1   7
Column   0   0   0   2   0
minimum
Step 3: Make assignment on modified matrix by applying row scanning and then column
scanning:
********** 8 **********
--- page 9 ---
Optimal   Operator   Operator   Operator   Operator   Operator
solution   1   2   3   4   5
value = 38
Job A   9   11   14   11   Assign 7
Job B   Assign 6   15   13   13   10
Job C   12   13   Assign 6   8   8
Job D   11   Assign 9   10   12   9
Job E   7   12   14   Assign 10   14
JOB   Assigned to   Cost
Job A   Operator 5   7
Job B   Operator 1   6
Job C   Operator 3   6
Job D   Operator 2   9
Job E   Operator 4   10
Total   38
•   Correct cost matrix formulation → 1 Mark
• Row reduction → 2 Marks
• Column reduction → 2 Marks
•   Optimality check (covering zeros) → 2 Marks
•   Final optimal assignment → 2 Mark
•   Total minimum cost (23) → 1 Mark
CO-1,4; b   10
BL-   Iteration 1: Adding Cj-Zj row (02 Marks]
Analyze   Cj   5   2   0   0
CB   Basis   x1   x2   S1   S2   RHS
5   x1   1   0   0.5   -0.5   1.5
2   x2   0   1   -0.5   1.5   2.5
Zj   Z=12.5   5   2   1.5   0.5
Cj-Zj   0   0   -1.5   -0.5
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=1.5,x2=2.5, Max Z=12.5
Add Gomory Cut [02 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut,
with the help of x1-row as follows:
1.5=1x1+0.5S1-0.5S2
The fractional cut will become
-0.5=Sg1-0.5S1-0.5S2→ (Cut-1)
Adding this additional constraint at the bottom of optimal simplex table. The new table
so obtained is [03 Marks]
Cj   5   2   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1 RHS
5   x1   1   0   0.5   -0.5   0   1.5
2   x2   0   1   -0.5   1.5   0   2.5
0   Sg1   0   0   -0.5   (-0.5)   1   -
0.5→
Z=12.5   Zj   5   2   1.5   0.5   0
********** 9 **********
--- page 10 ---
Cj-Zj   0   0   -1.5   -0.5   0
Ratio=Cj-Zj   --   --   3   1↑   --
/Sg1,j
and Sg1,j<0
Most negative RHS is -0.5 and its row index is 3. So, the leaving basis variable is Sg1.
Least positive ratio is 1 and its column index is 4. So, the entering variable is S2.
Iteration 2 [02 Marks]
Cj   5   2   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1   RHS
5   x1   1   0   1   0   -1   2
2   x2   0   1   -2   0   3   1
0   S2   0   0   1   1   -2   1
Z=12   Zj   5   2   1   0   1
Cj-Zj   0   0   -1   0   -1
Ratio
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as:
x1=2, x2=1, Max Z=12 [01 Marks]
Q7   [20]
CO-1,3; a   Since no. of rows is not equal to no. of column, so this unbalanced. So, add Dummy   8
BL-   column to make problem balanced.
Analyze   Optimal   A   B   C   D
solution
value = 35
1   (Assign) 9   26   15   0
2   13   27   (Assign) 6   0
3   35   (Assign) 20   15   0
4   18   30   20   (Assign) 0
Machine   Assigned to Jobs   Cost
1   A   9
2   C   6
3   B   20
4   D   0
Total   35
CO-1,4; b   6
BL-
Apply
-------------------4M
-------------------2M
********** 10 **********
--- page 11 ---
CO-1,4; c   6
BL-   1. Concept [01 Marks]
Apply   In some linear programming problems, the optimal solution obtained from LP relaxation
contains fractional values, whereas the problem requires integer solutions.
The Branch and Bound method are used to systematically find the best integer solution.
2. Short Example (can be any) [01 Marks]
Maximize
Z=3x+2y
Subject to
2x + y ≤ 7, x + 2y ≤7,
x, y ≥ 0
LP relaxation solution:
x=2.33, y=2.33(fractional)
3. Branching [01 Marks]
Choose a fractional variable (say x=2.33):
Create two branches:
• Branch 1: x≤2
• Branch 2: x≥3
4. Solving Subproblems [01 Marks]
Each branch is solved as a new LP:
• Branch 1 may give a feasible integer or fractional solution
• Branch 2 is solved similarly
If a solution is still fractional → further branching is done
5. Bounding [01 Marks]
• Keep track of the best integer solution found
•   If a branch gives a worse objective value than the current best → discard (fathom)
that branch
6. Termination [01 Marks]
The process continues until:
•   All branches are either explored or eliminated
• The best remaining solution is integer and optimal
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 47a1d70b893c

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AI_7012/Optimization Techniques/ANS_Optimization Techniques(702AI0C031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (11 pages), mean OCR confidence 78.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Optimization Techniques
Date: 08 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [10]
CO-1,4;   a.   5
BL-
Apply
********** 1 **********
--- page 2 ---
CO-1,3;   b. By applying NWCM, we have initial solution   5
BL-   Plant Distribution Center   Supply
Apply
D1   D2   D3   D4
P1   2   6   3   11   7   6
P2   1   0   6   1   1
1
P3   5   8   5   15   3   9   2   10
Demand   7   5   3   2   17
Since number of occupied cells = 5 and m+n-1 = 6.
So, solution is degenerate.
CO-1,2;   c.   (i)   Maximin criterion   5
BL-   Summer   Flavor of the soft drink
Apply   Condition   Orange   Normal   Lime
Growth
Mild   16   13   11
Moderate   10   12   14
Severe   12   9   15
Very Severe   7   9   14
Column   7   9   11
Minimum
Maximin = Maximum (column Minimum) = 11.   (2 marks)
Best Strategy Chosen to launch is Lime.   (0.5 marks)
(ii)   Hurwicz Criterion
Given the coefficient of optimism, α equal to 0.7, the coefficient of
pessimism is 1- 0.7 = 0.3. then according to this criterion, select best
(Maximum) payoff and worst (Minimum) payoff. As we know that,
Hurwicz = α x maximum payoff + (1 – α) x Minimum payoff
Alternative   Maximum   Minimum   Hurwicz
Investment   Payoff   Payoff
Orange   16   7   13.3
Mango   13   9   11.8
Lime   15   11   13.8
(2 marks)
Best Strategy (Course of Action) Chosen to launch is Lime. (0.5 marks)
CO-1,2;   d.   5
BL-   Row   Minimum
Analyze   A1   -2
A2   -2
A3   -3
A4   -2
Maximin = max (-2, -2, -3, -2) = -2 [Marks: 1.5]
Column   Maximum
B1   3
B2   2
B3   2
B4   2
Minimax = min (3, 2, 2, 2) = 2 [Marks: 1.5]
A game is fair if value of the game is 0. [Marks=1]
********** 2 **********
--- page 3 ---
Q2   [20]
CO-1,2; a   (i) Pessimistic or Maximin criterion:   10
BL-   Strategy   State of Nature   Row
Analyze   N1   N2   N3   N4   minimum
S1   4,000   -100   6,000 18,000   -100
S2   20,000   5,000   400   0   0
S3   20,000 15,000 -2,000   1,000   -2000
Maximin = max (row minimum) = 0.
So, Best Strategy Chosen is S2.
(ii)   Optimistic or Maximax Criterion
Strategy   State of Nature   Row
N1   N2   N3   N4   maximum
S1   4,000   -100   6,000 18,000   18000
S2   20,000   5,000   400   0   20000
S3   20,000 15,000 -2,000   1,000   20000
Maximax = max (row maximum) = 20000.
So, Best Strategy Chosen is S2 or S3.
(iii)   Hurwicz criterion
Given the coefficient of optimism, α equal to 0.7, the coefficient of
pessimism is 1- 0.7 = 0.3. then according to this criterion, select best
(Maximum) payoff and worst (Minimum) payoff. As we know that,
Hurwicz = α x maximum payoff + (1 – α) x Minimum payoff
Strategy   Row maximum Row minimum   Hurwicz
S1   18000   -100   12570
S2   20000   0   14000
S3   20000   -2000   13400
Best of Hurwicz criterion = 14000
Therefore, best strategy chosen is S2.
(iv)   Minimax Regret criterion:
Regret table is given below:
Strategy   State of Nature   Row
N1   N2   N3   N4   maximum
S1   20000-4,000   15000-(-100)   6,000 -6000   18,000 –   16000
= 16000   = 15100   = 0   18000 = 0
S2   20,000-20000   15000-5,000   6000-400   18000   18000
= 0   = 10000   =5600
S3   20,000-20000 15000-15,000   6000-(-   18000-1,000   17000
= 0   = 0   2,000) =   = 17000
8000
Minimax = min (row maximum) = 16000
So, Best Strategy Chosen is S1.
CO-1,4; b   Decision Variables-----------------1M   10
BL-   Let: x = quantity of milk (in 1000 litres) ,   y = quantity of butter (in 100 kg)
Apply   Objective function:---------------------1M
Min Z =(15000+18000)x+(26000+28000)y=33000x+54000y
Constraints:--------------------3M
********** 3 **********
--- page 4 ---
Plant | time constraint

3c +y <16
Plant Il time constraint
22+ 1by < 16

Demand constraints

e>4

y>2
Non-negativity

zy20

Graphical solution

x1 x2 RHS
33000 54000

Constraint 1 3 1 = 16

Constraint 2 2 15 <= 16

Constraint 3 1 0 >= 4

Constraint 4 0 1 = 2

Solution-> 4 2 240000
Q3 [20]
CO-1,4; a Maximize 10
BL Z = 102, + 6x2 + 423 + 0s; +0

= 10x, + 6x2 + 4x3 + 08) + O82

Apply

Subject to:
ay +ao+23+ 81 = 100
22, + 2xy + 6x3 + So = 300

©1,€2,€3, 81,82 >0

FIC 7) IC HOH
--- page 5 ---
Writing std form---------------2M
Iteration 1(table, cj-zj, KC, KR etc)-----------------3M
Calculations for iteration2--------------3M
Iteration2 (table, cj-zj)----------------1M
Final ans----------------1M
CO-1,2; b   Given from question,   10
BL-   • Cost price (C) = Rs 2
Analyze   •   Selling price (SP) = Rs 4
So, Profit cases:
Sold vaccine dose profit = 4 - 2 = Rs 2
Unsold dose loss = Rs 2 loss
Q \ D   20   25   40   60
Prob.   0.1   0.3   0.5   0.1
20   40   40   40   40
25   30   50   50   50
40   0   20   80   80
60   -40   -20   40   120
So, EMV for each option is calculated as,
EMV (20)   40 x 0.1+ 40 x 0.3+40x0.5+40x 0.1 = 40
EMV (25)   30x0.1+50 x0.3 + 50x0.5+50x0.1 = 48
EMV (40)   0 x 0.1 + 20x0.3+80x0.5+80x0.1 = 54
EMV (60)   -40 x 0.1 + (-20) x 0.3 + 40 x 0.5+120 x 0.1 = 22
Best EMV = 54.
So, Best Strategy to stock doses is 40.
(ii) EOL
Max payoff for each demand:
Demand   Max payoff
20   40
25   50
40   80
60   120
********** 5 **********

[Text in pictures on this page, read by OCR]
io)

Iteration 1
it}
it}

Iteration 2
10
it}

Basic 10 6 2B 0 0

Variables Quantity Xt x2 slack 1 slack 2
slack 1 100
slack 2 300 2 2 6 0 1
z 0 0 0 0 0 0
cz)
100
slack 2 100 0 0 4 2 1
z 1,000 10 10 10 10 0

cj oO -4 6 10 0
--- page 6 ---
Regret or Opportunity Loss table is calculated as:
Q\D   20   25   40   60
Prob.   0.1   0.3   0.5   0.1
20   0   10   40   80
25   10   0   30   70
40   40   30   0   40
60   80   70   40   0
Expected Opportunity loss is calculated for each option:
EOL (20) = 0(0.1) +10(0.3) +40 (0.5) +80(0.1) = 31
EOL (25) = 10(0.1) +0(0.3) +30 (0.5) +70(0.1) = 23
EOL (40) = 40(0.1) +30(0.3) +0 (0.5) +40(0.1) = 17
EOL (60) = 80(0.1) +70(0.3) +40 (0.5) +0(0.1) = 49
Minimum Expected Opportunity Loss (EOL) = Rs 17
Best strategy chosen is stock of 40 doses.
Q4   [20]
CO-1,4; a   10
BL-
Apply
Iteration-1(for given table calculation of zj, cj-zj, KC, KR etc)----------------- 4M
Calculations for iteration-2--------------3M
Iteration-2 (table, zj, cj-zj)----------------2M
Final Ans----------------1M
CO-1,4; b   Solve LP Relaxation: [3 Marks]   10
BL-
Ignore the integer restriction first.
Analyze
Solving the problem, A graphically, we find that:
gives: X₁ =3, X₂ =2.5 which is an LP optimal solution
Solving Sub-Problem B: 2 Marks
Solving Sub-Problem C: 1 Marks
Solving Sub-Problem D: 2 Marks
Solving Sub-Problem E: 1 Marks
********** 6 **********

[Text in pictures on this page, read by OCR]
a. mene t

}-~——,~——3 | 0 ig I 0 1 ya
-_ 2 2 1 Y) = 0 0 jundefined|
0 e avi \cao 1 0 1 0 a

rF 10 =—M -M-10 0 -M

Prseegine 0 M+12 M+10 0 0

, : _|

2 % 3 0 1 1 0
. 2 | 2 0 al 0

| 0 S; 1 0 a iF i

| Zz 6 10 12 2 0
52% 0 0 2 0 =|

Since all entries in the C)-
solution is arrived at and is aken wy
*1 = 10, xp»

Problem 3.9& A» ac. rn.

row are either zero or negative, the optimum

-
--- page 7 ---
Branch and bound algorithm thus terminated and the optimal integer solution is:
ZD=26 and X₁ =3, X₂ =2 [1 Marks]
Q5   [20]
CO-   a   10
1,3;
BL-
Analyze
********** 7 **********
--- page 8 ---
CO-   b Step 1: Row Dominance (1 Marks)   10
1,2;   • Row2 dominates Row3 → remove Row3.
BL-   Step 2 Column Dominance (1 Marks)
Analyze   • Col1 dominates Col3 → remove Col3
Reduced Matrix (1 Marks)
I   II   IV
1   3   5   2
2   6   4   5
4   5   2   4
Step 3: Row Dominance (1 Marks)
Row2 dominates Row4 → remove Row4
I   II   IV
1   3   5   2
2   6   4   5
Column Dominance (1 Marks)
B4 dominates B1 → remove B1
II   IV
1   5   2
2   4   5
Check Saddle Point (1 Marks)
Maximin is not equal to Minimax
• Saddle Point does not exist
Finding the Probability for Y (1.5)
1 = 1/4
2 = 3/4
Finding the Probability for X (1.5)
II= ¾
IV= ¼
Value of the Game=4.25 (1 Marks)
Q6   [20]
CO-1,3; a   10
BL-   Step1. Row reduction Matrix:
Apply   Operators
1   2   3   4   5   Row
minimum
A   2   4   7   4   0   7
Jobs
B   0   9   7   7   4   6
C   6   7   0   2   2   6
D   2   0   1   3   0   9
E   0   5   7   3   7   7
Step 2: Column reduction matrix:
Operators
1   2   3   4   5
A   2   4   7   2   0
Jobs   B   0   9   7   5   4
C   6   7   0   0   2
D   2   0   1   1   0
E   0   5   7   1   7
Column   0   0   0   2   0
minimum
Step 3: Make assignment on modified matrix by applying row scanning and then column
scanning:
********** 8 **********
--- page 9 ---
Optimal   Operator   Operator   Operator   Operator   Operator
solution   1   2   3   4   5
value = 38
Job A   9   11   14   11   Assign 7
Job B   Assign 6   15   13   13   10
Job C   12   13   Assign 6   8   8
Job D   11   Assign 9   10   12   9
Job E   7   12   14   Assign 10   14
JOB   Assigned to   Cost
Job A   Operator 5   7
Job B   Operator 1   6
Job C   Operator 3   6
Job D   Operator 2   9
Job E   Operator 4   10
Total   38
•   Correct cost matrix formulation → 1 Mark
• Row reduction → 2 Marks
• Column reduction → 2 Marks
•   Optimality check (covering zeros) → 2 Marks
•   Final optimal assignment → 2 Mark
•   Total minimum cost (23) → 1 Mark
CO-1,4; b   10
BL-   Iteration 1: Adding Cj-Zj row (02 Marks]
Analyze   Cj   5   2   0   0
CB   Basis   x1   x2   S1   S2   RHS
5   x1   1   0   0.5   -0.5   1.5
2   x2   0   1   -0.5   1.5   2.5
Zj   Z=12.5   5   2   1.5   0.5
Cj-Zj   0   0   -1.5   -0.5
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=1.5,x2=2.5, Max Z=12.5
Add Gomory Cut [02 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut,
with the help of x1-row as follows:
1.5=1x1+0.5S1-0.5S2
The fractional cut will become
-0.5=Sg1-0.5S1-0.5S2→ (Cut-1)
Adding this additional constraint at the bottom of optimal simplex table. The new table
so obtained is [03 Marks]
Cj   5   2   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1 RHS
5   x1   1   0   0.5   -0.5   0   1.5
2   x2   0   1   -0.5   1.5   0   2.5
0   Sg1   0   0   -0.5   (-0.5)   1   -
0.5→
Z=12.5   Zj   5   2   1.5   0.5   0
********** 9 **********
--- page 10 ---
Cj-Zj   0   0   -1.5   -0.5   0
Ratio=Cj-Zj   --   --   3   1↑   --
/Sg1,j
and Sg1,j<0
Most negative RHS is -0.5 and its row index is 3. So, the leaving basis variable is Sg1.
Least positive ratio is 1 and its column index is 4. So, the entering variable is S2.
Iteration 2 [02 Marks]
Cj   5   2   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1   RHS
5   x1   1   0   1   0   -1   2
2   x2   0   1   -2   0   3   1
0   S2   0   0   1   1   -2   1
Z=12   Zj   5   2   1   0   1
Cj-Zj   0   0   -1   0   -1
Ratio
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as:
x1=2, x2=1, Max Z=12 [01 Marks]
Q7   [20]
CO-1,3; a   Since no. of rows is not equal to no. of column, so this unbalanced. So, add Dummy   8
BL-   column to make problem balanced.
Analyze   Optimal   A   B   C   D
solution
value = 35
1   (Assign) 9   26   15   0
2   13   27   (Assign) 6   0
3   35   (Assign) 20   15   0
4   18   30   20   (Assign) 0
Machine   Assigned to Jobs   Cost
1   A   9
2   C   6
3   B   20
4   D   0
Total   35
CO-1,4; b   6
BL-
Apply
-------------------4M
-------------------2M
********** 10 **********
--- page 11 ---
CO-1,4; c   6
BL-   1. Concept [01 Marks]
Apply   In some linear programming problems, the optimal solution obtained from LP relaxation
contains fractional values, whereas the problem requires integer solutions.
The Branch and Bound method are used to systematically find the best integer solution.
2. Short Example (can be any) [01 Marks]
Maximize
Z=3x+2y
Subject to
2x + y ≤ 7, x + 2y ≤7,
x, y ≥ 0
LP relaxation solution:
x=2.33, y=2.33(fractional)
3. Branching [01 Marks]
Choose a fractional variable (say x=2.33):
Create two branches:
• Branch 1: x≤2
• Branch 2: x≥3
4. Solving Subproblems [01 Marks]
Each branch is solved as a new LP:
• Branch 1 may give a feasible integer or fractional solution
• Branch 2 is solved similarly
If a solution is still fractional → further branching is done
5. Bounding [01 Marks]
• Keep track of the best integer solution found
•   If a branch gives a worse objective value than the current best → discard (fathom)
that branch
6. Termination [01 Marks]
The process continues until:
•   All branches are either explored or eliminated
• The best remaining solution is integer and optimal
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 0e7568499a73

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_AI_7051/Optimization Techniques/ANS_Optimization Techniques(702AI0C031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (11 pages), mean OCR confidence 78.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Optimization Techniques
Date: 08 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [10]
CO-1,4;   a.   5
BL-
Apply
********** 1 **********
--- page 2 ---
CO-1,3;   b. By applying NWCM, we have initial solution   5
BL-   Plant Distribution Center   Supply
Apply
D1   D2   D3   D4
P1   2   6   3   11   7   6
P2   1   0   6   1   1
1
P3   5   8   5   15   3   9   2   10
Demand   7   5   3   2   17
Since number of occupied cells = 5 and m+n-1 = 6.
So, solution is degenerate.
CO-1,2;   c.   (i)   Maximin criterion   5
BL-   Summer   Flavor of the soft drink
Apply   Condition   Orange   Normal   Lime
Growth
Mild   16   13   11
Moderate   10   12   14
Severe   12   9   15
Very Severe   7   9   14
Column   7   9   11
Minimum
Maximin = Maximum (column Minimum) = 11.   (2 marks)
Best Strategy Chosen to launch is Lime.   (0.5 marks)
(ii)   Hurwicz Criterion
Given the coefficient of optimism, α equal to 0.7, the coefficient of
pessimism is 1- 0.7 = 0.3. then according to this criterion, select best
(Maximum) payoff and worst (Minimum) payoff. As we know that,
Hurwicz = α x maximum payoff + (1 – α) x Minimum payoff
Alternative   Maximum   Minimum   Hurwicz
Investment   Payoff   Payoff
Orange   16   7   13.3
Mango   13   9   11.8
Lime   15   11   13.8
(2 marks)
Best Strategy (Course of Action) Chosen to launch is Lime. (0.5 marks)
CO-1,2;   d.   5
BL-   Row   Minimum
Analyze   A1   -2
A2   -2
A3   -3
A4   -2
Maximin = max (-2, -2, -3, -2) = -2 [Marks: 1.5]
Column   Maximum
B1   3
B2   2
B3   2
B4   2
Minimax = min (3, 2, 2, 2) = 2 [Marks: 1.5]
A game is fair if value of the game is 0. [Marks=1]
********** 2 **********
--- page 3 ---
Q2   [20]
CO-1,2; a   (i) Pessimistic or Maximin criterion:   10
BL-   Strategy   State of Nature   Row
Analyze   N1   N2   N3   N4   minimum
S1   4,000   -100   6,000 18,000   -100
S2   20,000   5,000   400   0   0
S3   20,000 15,000 -2,000   1,000   -2000
Maximin = max (row minimum) = 0.
So, Best Strategy Chosen is S2.
(ii)   Optimistic or Maximax Criterion
Strategy   State of Nature   Row
N1   N2   N3   N4   maximum
S1   4,000   -100   6,000 18,000   18000
S2   20,000   5,000   400   0   20000
S3   20,000 15,000 -2,000   1,000   20000
Maximax = max (row maximum) = 20000.
So, Best Strategy Chosen is S2 or S3.
(iii)   Hurwicz criterion
Given the coefficient of optimism, α equal to 0.7, the coefficient of
pessimism is 1- 0.7 = 0.3. then according to this criterion, select best
(Maximum) payoff and worst (Minimum) payoff. As we know that,
Hurwicz = α x maximum payoff + (1 – α) x Minimum payoff
Strategy   Row maximum Row minimum   Hurwicz
S1   18000   -100   12570
S2   20000   0   14000
S3   20000   -2000   13400
Best of Hurwicz criterion = 14000
Therefore, best strategy chosen is S2.
(iv)   Minimax Regret criterion:
Regret table is given below:
Strategy   State of Nature   Row
N1   N2   N3   N4   maximum
S1   20000-4,000   15000-(-100)   6,000 -6000   18,000 –   16000
= 16000   = 15100   = 0   18000 = 0
S2   20,000-20000   15000-5,000   6000-400   18000   18000
= 0   = 10000   =5600
S3   20,000-20000 15000-15,000   6000-(-   18000-1,000   17000
= 0   = 0   2,000) =   = 17000
8000
Minimax = min (row maximum) = 16000
So, Best Strategy Chosen is S1.
CO-1,4; b   Decision Variables-----------------1M   10
BL-   Let: x = quantity of milk (in 1000 litres) ,   y = quantity of butter (in 100 kg)
Apply   Objective function:---------------------1M
Min Z =(15000+18000)x+(26000+28000)y=33000x+54000y
Constraints:--------------------3M
********** 3 **********
--- page 4 ---
Plant | time constraint

3c +y <16
Plant Il time constraint
22+ 1by < 16

Demand constraints

e>4

y>2
Non-negativity

zy20

Graphical solution

x1 x2 RHS
33000 54000

Constraint 1 3 1 = 16

Constraint 2 2 15 <= 16

Constraint 3 1 0 >= 4

Constraint 4 0 1 = 2

Solution-> 4 2 240000
Q3 [20]
CO-1,4; a Maximize 10
BL Z = 102, + 6x2 + 423 + 0s; +0

= 10x, + 6x2 + 4x3 + 08) + O82

Apply

Subject to:
ay +ao+23+ 81 = 100
22, + 2xy + 6x3 + So = 300

©1,€2,€3, 81,82 >0

FIC 7) IC HOH
--- page 5 ---
Writing std form---------------2M
Iteration 1(table, cj-zj, KC, KR etc)-----------------3M
Calculations for iteration2--------------3M
Iteration2 (table, cj-zj)----------------1M
Final ans----------------1M
CO-1,2; b   Given from question,   10
BL-   • Cost price (C) = Rs 2
Analyze   •   Selling price (SP) = Rs 4
So, Profit cases:
Sold vaccine dose profit = 4 - 2 = Rs 2
Unsold dose loss = Rs 2 loss
Q \ D   20   25   40   60
Prob.   0.1   0.3   0.5   0.1
20   40   40   40   40
25   30   50   50   50
40   0   20   80   80
60   -40   -20   40   120
So, EMV for each option is calculated as,
EMV (20)   40 x 0.1+ 40 x 0.3+40x0.5+40x 0.1 = 40
EMV (25)   30x0.1+50 x0.3 + 50x0.5+50x0.1 = 48
EMV (40)   0 x 0.1 + 20x0.3+80x0.5+80x0.1 = 54
EMV (60)   -40 x 0.1 + (-20) x 0.3 + 40 x 0.5+120 x 0.1 = 22
Best EMV = 54.
So, Best Strategy to stock doses is 40.
(ii) EOL
Max payoff for each demand:
Demand   Max payoff
20   40
25   50
40   80
60   120
********** 5 **********

[Text in pictures on this page, read by OCR]
io)

Iteration 1
it}
it}

Iteration 2
10
it}

Basic 10 6 2B 0 0

Variables Quantity Xt x2 slack 1 slack 2
slack 1 100
slack 2 300 2 2 6 0 1
z 0 0 0 0 0 0
cz)
100
slack 2 100 0 0 4 2 1
z 1,000 10 10 10 10 0

cj oO -4 6 10 0
--- page 6 ---
Regret or Opportunity Loss table is calculated as:
Q\D   20   25   40   60
Prob.   0.1   0.3   0.5   0.1
20   0   10   40   80
25   10   0   30   70
40   40   30   0   40
60   80   70   40   0
Expected Opportunity loss is calculated for each option:
EOL (20) = 0(0.1) +10(0.3) +40 (0.5) +80(0.1) = 31
EOL (25) = 10(0.1) +0(0.3) +30 (0.5) +70(0.1) = 23
EOL (40) = 40(0.1) +30(0.3) +0 (0.5) +40(0.1) = 17
EOL (60) = 80(0.1) +70(0.3) +40 (0.5) +0(0.1) = 49
Minimum Expected Opportunity Loss (EOL) = Rs 17
Best strategy chosen is stock of 40 doses.
Q4   [20]
CO-1,4; a   10
BL-
Apply
Iteration-1(for given table calculation of zj, cj-zj, KC, KR etc)----------------- 4M
Calculations for iteration-2--------------3M
Iteration-2 (table, zj, cj-zj)----------------2M
Final Ans----------------1M
CO-1,4; b   Solve LP Relaxation: [3 Marks]   10
BL-
Ignore the integer restriction first.
Analyze
Solving the problem, A graphically, we find that:
gives: X₁ =3, X₂ =2.5 which is an LP optimal solution
Solving Sub-Problem B: 2 Marks
Solving Sub-Problem C: 1 Marks
Solving Sub-Problem D: 2 Marks
Solving Sub-Problem E: 1 Marks
********** 6 **********

[Text in pictures on this page, read by OCR]
a. mene t

}-~——,~——3 | 0 ig I 0 1 ya
-_ 2 2 1 Y) = 0 0 jundefined|
0 e avi \cao 1 0 1 0 a

rF 10 =—M -M-10 0 -M

Prseegine 0 M+12 M+10 0 0

, : _|

2 % 3 0 1 1 0
. 2 | 2 0 al 0

| 0 S; 1 0 a iF i

| Zz 6 10 12 2 0
52% 0 0 2 0 =|

Since all entries in the C)-
solution is arrived at and is aken wy
*1 = 10, xp»

Problem 3.9& A» ac. rn.

row are either zero or negative, the optimum

-
--- page 7 ---
Branch and bound algorithm thus terminated and the optimal integer solution is:
ZD=26 and X₁ =3, X₂ =2 [1 Marks]
Q5   [20]
CO-   a   10
1,3;
BL-
Analyze
********** 7 **********
--- page 8 ---
CO-   b Step 1: Row Dominance (1 Marks)   10
1,2;   • Row2 dominates Row3 → remove Row3.
BL-   Step 2 Column Dominance (1 Marks)
Analyze   • Col1 dominates Col3 → remove Col3
Reduced Matrix (1 Marks)
I   II   IV
1   3   5   2
2   6   4   5
4   5   2   4
Step 3: Row Dominance (1 Marks)
Row2 dominates Row4 → remove Row4
I   II   IV
1   3   5   2
2   6   4   5
Column Dominance (1 Marks)
B4 dominates B1 → remove B1
II   IV
1   5   2
2   4   5
Check Saddle Point (1 Marks)
Maximin is not equal to Minimax
• Saddle Point does not exist
Finding the Probability for Y (1.5)
1 = 1/4
2 = 3/4
Finding the Probability for X (1.5)
II= ¾
IV= ¼
Value of the Game=4.25 (1 Marks)
Q6   [20]
CO-1,3; a   10
BL-   Step1. Row reduction Matrix:
Apply   Operators
1   2   3   4   5   Row
minimum
A   2   4   7   4   0   7
Jobs
B   0   9   7   7   4   6
C   6   7   0   2   2   6
D   2   0   1   3   0   9
E   0   5   7   3   7   7
Step 2: Column reduction matrix:
Operators
1   2   3   4   5
A   2   4   7   2   0
Jobs   B   0   9   7   5   4
C   6   7   0   0   2
D   2   0   1   1   0
E   0   5   7   1   7
Column   0   0   0   2   0
minimum
Step 3: Make assignment on modified matrix by applying row scanning and then column
scanning:
********** 8 **********
--- page 9 ---
Optimal   Operator   Operator   Operator   Operator   Operator
solution   1   2   3   4   5
value = 38
Job A   9   11   14   11   Assign 7
Job B   Assign 6   15   13   13   10
Job C   12   13   Assign 6   8   8
Job D   11   Assign 9   10   12   9
Job E   7   12   14   Assign 10   14
JOB   Assigned to   Cost
Job A   Operator 5   7
Job B   Operator 1   6
Job C   Operator 3   6
Job D   Operator 2   9
Job E   Operator 4   10
Total   38
•   Correct cost matrix formulation → 1 Mark
• Row reduction → 2 Marks
• Column reduction → 2 Marks
•   Optimality check (covering zeros) → 2 Marks
•   Final optimal assignment → 2 Mark
•   Total minimum cost (23) → 1 Mark
CO-1,4; b   10
BL-   Iteration 1: Adding Cj-Zj row (02 Marks]
Analyze   Cj   5   2   0   0
CB   Basis   x1   x2   S1   S2   RHS
5   x1   1   0   0.5   -0.5   1.5
2   x2   0   1   -0.5   1.5   2.5
Zj   Z=12.5   5   2   1.5   0.5
Cj-Zj   0   0   -1.5   -0.5
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=1.5,x2=2.5, Max Z=12.5
Add Gomory Cut [02 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut,
with the help of x1-row as follows:
1.5=1x1+0.5S1-0.5S2
The fractional cut will become
-0.5=Sg1-0.5S1-0.5S2→ (Cut-1)
Adding this additional constraint at the bottom of optimal simplex table. The new table
so obtained is [03 Marks]
Cj   5   2   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1 RHS
5   x1   1   0   0.5   -0.5   0   1.5
2   x2   0   1   -0.5   1.5   0   2.5
0   Sg1   0   0   -0.5   (-0.5)   1   -
0.5→
Z=12.5   Zj   5   2   1.5   0.5   0
********** 9 **********
--- page 10 ---
Cj-Zj   0   0   -1.5   -0.5   0
Ratio=Cj-Zj   --   --   3   1↑   --
/Sg1,j
and Sg1,j<0
Most negative RHS is -0.5 and its row index is 3. So, the leaving basis variable is Sg1.
Least positive ratio is 1 and its column index is 4. So, the entering variable is S2.
Iteration 2 [02 Marks]
Cj   5   2   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1   RHS
5   x1   1   0   1   0   -1   2
2   x2   0   1   -2   0   3   1
0   S2   0   0   1   1   -2   1
Z=12   Zj   5   2   1   0   1
Cj-Zj   0   0   -1   0   -1
Ratio
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as:
x1=2, x2=1, Max Z=12 [01 Marks]
Q7   [20]
CO-1,3; a   Since no. of rows is not equal to no. of column, so this unbalanced. So, add Dummy   8
BL-   column to make problem balanced.
Analyze   Optimal   A   B   C   D
solution
value = 35
1   (Assign) 9   26   15   0
2   13   27   (Assign) 6   0
3   35   (Assign) 20   15   0
4   18   30   20   (Assign) 0
Machine   Assigned to Jobs   Cost
1   A   9
2   C   6
3   B   20
4   D   0
Total   35
CO-1,4; b   6
BL-
Apply
-------------------4M
-------------------2M
********** 10 **********
--- page 11 ---
CO-1,4; c   6
BL-   1. Concept [01 Marks]
Apply   In some linear programming problems, the optimal solution obtained from LP relaxation
contains fractional values, whereas the problem requires integer solutions.
The Branch and Bound method are used to systematically find the best integer solution.
2. Short Example (can be any) [01 Marks]
Maximize
Z=3x+2y
Subject to
2x + y ≤ 7, x + 2y ≤7,
x, y ≥ 0
LP relaxation solution:
x=2.33, y=2.33(fractional)
3. Branching [01 Marks]
Choose a fractional variable (say x=2.33):
Create two branches:
• Branch 1: x≤2
• Branch 2: x≥3
4. Solving Subproblems [01 Marks]
Each branch is solved as a new LP:
• Branch 1 may give a feasible integer or fractional solution
• Branch 2 is solved similarly
If a solution is still fractional → further branching is done
5. Bounding [01 Marks]
• Keep track of the best integer solution found
•   If a branch gives a worse objective value than the current best → discard (fathom)
that branch
6. Termination [01 Marks]
The process continues until:
•   All branches are either explored or eliminated
• The best remaining solution is integer and optimal
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 4dd995d6541e

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIDS_7056/Optimization Techniques/ANS_Optimization Techniques(702AI0C031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: mixed (13 pages), mean OCR confidence 80.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Optimization Techniques
Date: 04 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [10]
********** 1 **********
--- page 2 ---
CO-1,4;   a.
BL-
Apply
5
CO-1,3;   b.   Step 1: Check Balance
BL-   Total Supply = 10 + 15 + 40 = 65
Apply   Total Demand = 20 + 15 + 30 = 65
Balanced problem
Step 2: NWCM Allocation
Start from top-left (S1–D1):
D1   D2   D3   Supply
S1   10   –   –   10
S2   10   5   –   15
S3   –   10   30   40   5
Demand   20   15   30
Step 3: Total Transportation Cost
=10×2+10×4+5×1+10×3+30×1
=20+40+5+30+30=125
Marking Scheme (5 Marks)
•   Balance check → 1 Mark
•   Correct NWCM allocations → 3 Marks
•   Total cost → 1 Mark
•
********** 2 **********
--- page 3 ---
CO-1,2;   c.
BL-   Given Payoff Table
Apply   Strategy   N1   N2   Minimum
S1   60   40   40
S2   20   30   20
S3   100   -10   -10
(a) Maximin Criterion
Maximin = 40
Best Strategy = S1
(b) Minimax Regret Criterion
Step 2: Regret Table
5
Strategy   N1   N2   Maximum Regret
S1   40   0   40
S2   80   10   80
S3   0   50   50
Minimum regret = 40
Best Strategy = S1
Marking Scheme (5 Marks)
• Maximin calculation → 2 Marks
•   Regret table → 2 Marks
•   Final decision → 1 Mark
CO-1,2;   d. Step 1: Row minima
BL-   • Row 1 → min = 1
Analyze   • Row 2 → min = 2
• Row 3 → min = 0
Maximin = 2 [1 Marks]
Step 2: Column maxima
• Column I → max = 3
• Column II → max = 2
• Column III → max = 4
Minimax = 2 [1 Marks]
5
Step 3: Conclusion
• Maximin = Minimax = 2 → Saddle point exists [1 Marks]
Step 4: Optimal Strategy [1 Marks]
•   Saddle point at (Row 2, Column II)
•   Optimal strategies:
o Player A: Row 2
o Player B: Column II
Step 5: Value of the Game [1 Marks]
Value = 2
Q2   [20]
CO-1,2; a   Given Payoff Table (₹)
BL-   Strategy High Medium Low   Maximum Minimum Laplace
Analyze   A   80000 40000   -20000 80000   -20000   33333.33
B   60000 35000   5000   60000   5000   33333.33
C   30000 25000   15000   30000   15000   23333.33
10
(i) Pessimistic Criterion (Maximin)
Maximin = 15000
Best Strategy = C
********** 3 **********
--- page 4 ---
(ii) Optimistic Criterion (Maximax)
Maximax = 80000
Best Strategy = A
(iii) Equally Likely (Laplace Criterion)
Best Strategy = A or B (tie)
(iv) Minimax Regret Criterion
Step 1: Column Maximums
High → 80000
Medium → 40000
Low → 15000
Step 2: Regret Table
Strategy   High   Medium   Low   Maximum
A   0   0   35000   35000
B   20000   5000   10000   20000
C   50000   15000   0   50000
Minimum regret = 20000
Best Strategy = B
Marking Scheme (10 Marks)
•   Pessimistic → 2 Marks
•   Optimistic → 2 Marks
•   Laplace → 3 Marks
•   Regret table + decision → 3 Marks
CO-1,4; b
BL-
Apply
10
Decision variables and obj function-------------------2M
********** 4 **********
--- page 5 ---
Step 3: Constraints

Weight requirement (exactly 150 kg)
Each unit contributes weight:

5a + 10y = 150

Simplify:
x+2y = 30
Minimum usage of B
y>14
Maximum usage of A
a < 20
Non-negativity
z,y>0
weneecneecenneeeee 3M
Graphical solution:
x2
15)
30
x1 20
aonnenneene nee 3M
x1 x2 z
15 120
2 14 116
(untitled) Solution
x1 X2 RHS
Minimize 2 8
Constraint 1 (5 10 |= | 150
Constraint 2 0 1 >= 14
Constraint 3 \1 0 [<= |20
Solution-> 2 14 116
Q3 [20]
CO-1,4; | a
BL- 10
Apply

FIC DI EH ar
--- page 6 ---
Writing std form---------------2M
Iteration 1(table, cj-zj, KC, KR etc)-----------------3M
Calculations for iteration2--------------3M
Iteration2 (table, cj-zj)----------------1M
Final ans----------------1M
CO-1,2; b   Step 1: Given Data
BL-   Cost price (C) = ₹10 per dozen
Analyze   Selling price (SP) = ₹30 per dozen
Profit per sold dozen = ₹20
Unsold roses → no salvage (loss = ₹10 per dozen)
Demand distribution:
Demand (dozens)   70   80   90   100
Probability   0.1   0.2   0.4   0.3
Step 2: Payoff Table (Profit ₹)
Order \ Demand   70   80   90   100
10
70   1400   1400   1400   1400
80   1300   1600   1600   1600
90   1200   1500   1800   1800
100   1100   1400   1700   2000
Step 3: EMV Calculation
EMV=∑ (Payoff × Probability)
• EMV(70) = 1400
• EMV(80) = 1300×0.1+1600×0.9=1570
• EMV(90) = 1200×0.1+1500×0.2+1800×0.7=1680
• EMV(100) = 1100×0.1+1400×0.2+1700×0.4+2000×0.3=1670
Maximum EMV = 1680 (Order 90 dozen)
********** 6 **********

[Text in pictures on this page, read by OCR]
Maximize
Z = 40002, + 200022 + 500023 + 0s; + Oso
Subject to:
122, + Tag + 9x3 + 8, = 1260
222; + 1822 + 16x3 + s2 = 19008

21,2, 23, $1, 82 >0

Cj Basic 4000 wee poe i) 0

Variables Quantity x1 slack 1 slack 2
a a ST ST
slack 1 1,260
i} slack 2 19,008 22 18 16 0 1
Zz 0 0 0 0

cj-zj 4,000 2,000 5,000
iteration 2 a
5000 140 1.3333 0.7778 1
i} slack 2 16,768 0.6667 5.5556 i)

q 7,00,000 6666.67 3888.89 5000
cj-zj -2,666.66. -1,888.88. 0. -555.5556 0
--- page 7 ---
Step 4: EOL (Regret Table)
Column maximums:
• 70 → 1400
• 80 → 1600
• 90 → 1800
• 100 → 2000
Regret Table
Order \ Demand   70   80   90   100
70   0   200   400   600
80   100   0   200   400
90   200   100   0   200
100   300   200   100   0
EOL Calculation
• EOL(70) = 0×0.1+200×0.2+400×0.4+600×0.3=380
• EOL(80) = 100×0.1+0×0.2+200×0.4+400×0.3=210
• EOL(90) = 200×0.1+100×0.2+0×0.4+200×0.3=100
• EOL(100) = 300×0.1+200×0.2+100×0.4+0×0.3=110
Minimum EOL = 100 (Order 90 dozen)
Marking Scheme (10 Marks)
•   Payoff table → 3 Marks
• EMV calculation → 3 Marks
•   Regret table → 2 Marks
• EOL calculation → 1 Mark
•   Final decision → 1 Mark
Q4   [20]
CO-1,4; a
BL-
Apply
10
********** 7 **********
--- page 8 ---
Iteration 1(for given table calculation of zj, cj-zj, KC, KR etc)----------------- 4M
Calculations for iteration2--------------3M
Iteration2 (table, zj, cj-zj)----------------2M
Final ans----------------1M
CO-1,4; b   Solve LP Relaxation: [4 Marks]
BL-   Ignore the integer restriction first.
Analyze   Solving the problem, A graphically, we find that:
LP optimum = (4.5, 0), Z = 31.5 which is an LP optimal solution
Solving Sub-Problem B: [3 Marks]
Solving Sub-Problem C: [2 Marks]
10
Branch and bound algorithm thus terminated and the optimal integer solution is :
ZB=31 and X1 =4, X2 =1
Q5   [20]
CO-   a   Step 1: Check Balance
1,3;   Total Supply = 40 + 20 + 40 = 100
BL-   Total Demand = 25 + 10 + 20 + 30 + 15 = 100
Analyze   Balanced
Step 2: Initial Basic Feasible Solution (VAM)
One optimal allocation:
A   B   C   D   E   Supply
Agra   –   10   20   –   10   40
Allahabad   20   –   –   –   –   20
10
Kolkata   5   –   –   30   5   40
Demand   25   10   20   30   15
Step 3: Total Transportation Cost
=10×30 + 20×40 + 10×40 + 20×35 + 5×40 + 30×35 + 5×30= 3600
Step 4: Optimality (MODI Test)
Using ui, vj method:
•   All opportunity costs dij≥0
Solution is optimal
Marking Scheme (10 Marks)
********** 8 **********
--- page 9 ---
•   Balance check → 1 Mark
•   Initial solution (VAM/NWCM) → 3 Marks
•   Cost calculation → 2 Marks
•   ui, vj calculation → 2 Marks
•   Optimality test → 1 Mark
•   Final answer → 1 Mark
CO-   b Row Dominance (1 Marks)
1,2;   Row 2 ≥ Row 4 for all entries: Eliminate Row 4
BL-
Analyze   Column Dominance (2 Marks)
Column II is smaller everywhere: Eliminate Column I
Column II dominates Column III: Eliminate Column III
Reduced Matrix (1 Marks)
II   IV
1   2   3
2   3   2
3   1   5
Reducing to 2x2 Matrix by Convex combinations: [2 Marks]
II   IV
1   2   3
2   3   2
10
Check Saddle Point (1 Marks)
Maximin is not equal to Minimax
• Saddle Point does not exist
Finding the Probability for A [ 1 Marks]
1 = 1/2
2 = 1/2
Finding the Probability for B [ 1 Marks]
II=1/2
IV=1/2
Value of the Game=2.5 (1 Marks)
Q6   [20]
********** 9 **********
--- page 10 ---
CO-1,3; a   Given Cost Matrix (‘000 Rs)
BL-   Bidder   I   II   III   IV   V
Apply   1   41   72   39   52   25
2   22   29   49   65   81
3   27   39   60   51   40
4   45   50   48   52   37
5   29   40   45   26   30
Optimal Assignment (Hungarian Method)
Bidder   Project   Cost (‘000 Rs)
1   V   25
2   I   22
3   II   39
4   III   48
5   IV   26   10
Minimum Total Cost =25+22+39+48+26 =160
Minimum Cost = ₹160,000
Marking Scheme (10 Marks)
•   Cost matrix formulation → 1 Mark
• Row reduction → 2 Marks
• Column reduction → 2 Marks
•   Zero allocation & optimality → 3 Marks
•   Final assignment → 1 Mark
•   Total cost → 1 Mark
********** 10 **********
--- page 11 ---
CO-1,4; b
BL-   Iteration 1 [02 Marks]
Analyze
Cj   4   3   0   0
CB   Basis   x1   x2   S1   S2   RHS
4   x1   1   0   0.67   -0.33   1.67
3   x2   0   1   -0.33   0.67   1.67
Zj   Z=11.67   4   3   1.67   0.67
Cj-Zj   0   0   -1.67   -0.67
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as:
x1=5.5, x2=0
Max Z=33
Add Gomory Cut [02 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut,
with the help of x2-row as follows:
1.67=1x2-0.33S1+0.67S2
(1+0.67) = (1+0) x2+(-1+0.67) S1+(0+0.67) S2
The fractional cut will become
-0.67=Sg1-0.67S1-0.67S2→ (Cut-1)
Adding Gomory Constraint in the Table and relevant calculations [03 Marks]
Cj   4   3   0   0   0   10
CB   Basis   x1   x2   S1   S2   Sg1   RHS
4   x1   1   0   0.67   -0.33   0   1.67
3   x2   0   1   -0.33   0.67   0   1.67
0   Sg1   0   0   -0.67   (-0.67)   1   -0.67→
Z=11.67   Zj   4   3   1.67   0.67   0
Cj-Zj   0   0   -1.67   -0.67   0
Ratio   Cj-   --   --   2.5   1↑   ---
Zj/Sg1,j
Most negative RHS is -0.67 and its row index is 3. So, the leaving basis variable is Sg1.
Least positive ratio is 1 and its column index is 4. So, the entering variable is S2.
∴ The pivot element is -0.67.
Entering =S2, Departing =Sg1, Key Element =-0.67
New Iteration [02 Marks]
Cj   4   3   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1 RHS
4   x1   1   0   1   0   -0.5   2
3   x2   0   1   -1   0   1   1
0   S2   0   0   1   1   -1.5   1
Z=11   Zj   4   3   1   0   1
Cj-Zj   0   0   -1   0   -1
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as [1 Marks]:
x1=2, x2=1, Max Z=11
********** 11 **********
--- page 12 ---
Q7   [20]
CO-   a
1,3;   Step 1: Cost Matrix (Hundreds of ₹)
BL-   (Replace prohibited entries with a very large number MMM)
Analyze   Machine   A   B   C   D   E
M1   9   11   15   10   11
M2   12   9   M   10   9
M3   M   11   14   11   7
M4   14   8   12   7   8
Step 2: Solve using Hungarian Method
(After row/column reductions and optimal zero assignment)
8
Optimal Assignment
Machine   Location   Cost
M1   A   9
M2   B   9
M3   E   7
M4   D   7
(Note: One location remains unused since 5 locations & 4 machines)
Minimum Total Cost = 9 + 9 + 7 + 7 = 32
In rupees: 32×100 = ₹ 3200
CO-   b
1,4;
BL-
Apply
-------------------4M
6
-------------------2M
********** 12 **********

[Text in pictures on this page, read by OCR]
(untitled) Solution

x1 x2 RHS
Minimize 200 400
Constraint 1 1 1 >= 200
Constraint 2 1 3 >= 400
Constraint 3 1 2 <= 350
Solution-> 100 100 60000
--- page 13 ---
CO-   c
1,4;
BL-   i. Recommended Method and Justification [3 Marks]
Apply   The recommended method is the Branch and Bound Method.
Justification
• The problem has only two variables, so the feasible region can be easily visualized
graphically.
• With only one fractional basic variable, branching can be done once, leading to
just two subproblems.
• The method is intuitive and easy to apply graphically, making it more suitable in
this case.
•   In contrast, the Gomory Cutting Plane Method involves additional tableau
computations, which are less convenient for graphical problems.
Procedure of the Chosen Method (Branch and Bound) [3 Marks]
1. Solve LP Relaxation
o Ignore integer restrictions and obtain the optimal fractional solution.
2. Branching
o   Select the variable with fractional value (say x1=2.6)   6
o Create two subproblems: x1≤2andx1≥3
3. Solve Subproblems
o Solve each subproblem graphically (or using LP)
o Obtain optimal values for each branch
4. Bounding
o Compare objective values
o Use LP values as upper bounds
5. Pruning
o Discard branches that are:
▪   Infeasible, or
▪   Inferior to an already obtained integer solution
6. Select Optimal Integer Solution
Choose the feasible integer solution with the best objective value
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper d2d96fe54d52

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIML_7053/Optimization Techniques/ANS_Optimization Techniques(702AI0C031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: mixed (13 pages), mean OCR confidence 80.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Optimization Techniques
Date: 04 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [10]
********** 1 **********
--- page 2 ---
CO-1,4;   a.
BL-
Apply
5
CO-1,3;   b.   Step 1: Check Balance
BL-   Total Supply = 10 + 15 + 40 = 65
Apply   Total Demand = 20 + 15 + 30 = 65
Balanced problem
Step 2: NWCM Allocation
Start from top-left (S1–D1):
D1   D2   D3   Supply
S1   10   –   –   10
S2   10   5   –   15
S3   –   10   30   40   5
Demand   20   15   30
Step 3: Total Transportation Cost
=10×2+10×4+5×1+10×3+30×1
=20+40+5+30+30=125
Marking Scheme (5 Marks)
•   Balance check → 1 Mark
•   Correct NWCM allocations → 3 Marks
•   Total cost → 1 Mark
•
********** 2 **********
--- page 3 ---
CO-1,2;   c.
BL-   Given Payoff Table
Apply   Strategy   N1   N2   Minimum
S1   60   40   40
S2   20   30   20
S3   100   -10   -10
(a) Maximin Criterion
Maximin = 40
Best Strategy = S1
(b) Minimax Regret Criterion
Step 2: Regret Table
5
Strategy   N1   N2   Maximum Regret
S1   40   0   40
S2   80   10   80
S3   0   50   50
Minimum regret = 40
Best Strategy = S1
Marking Scheme (5 Marks)
• Maximin calculation → 2 Marks
•   Regret table → 2 Marks
•   Final decision → 1 Mark
CO-1,2;   d. Step 1: Row minima
BL-   • Row 1 → min = 1
Analyze   • Row 2 → min = 2
• Row 3 → min = 0
Maximin = 2 [1 Marks]
Step 2: Column maxima
• Column I → max = 3
• Column II → max = 2
• Column III → max = 4
Minimax = 2 [1 Marks]
5
Step 3: Conclusion
• Maximin = Minimax = 2 → Saddle point exists [1 Marks]
Step 4: Optimal Strategy [1 Marks]
•   Saddle point at (Row 2, Column II)
•   Optimal strategies:
o Player A: Row 2
o Player B: Column II
Step 5: Value of the Game [1 Marks]
Value = 2
Q2   [20]
CO-1,2; a   Given Payoff Table (₹)
BL-   Strategy High Medium Low   Maximum Minimum Laplace
Analyze   A   80000 40000   -20000 80000   -20000   33333.33
B   60000 35000   5000   60000   5000   33333.33
C   30000 25000   15000   30000   15000   23333.33
10
(i) Pessimistic Criterion (Maximin)
Maximin = 15000
Best Strategy = C
********** 3 **********
--- page 4 ---
(ii) Optimistic Criterion (Maximax)
Maximax = 80000
Best Strategy = A
(iii) Equally Likely (Laplace Criterion)
Best Strategy = A or B (tie)
(iv) Minimax Regret Criterion
Step 1: Column Maximums
High → 80000
Medium → 40000
Low → 15000
Step 2: Regret Table
Strategy   High   Medium   Low   Maximum
A   0   0   35000   35000
B   20000   5000   10000   20000
C   50000   15000   0   50000
Minimum regret = 20000
Best Strategy = B
Marking Scheme (10 Marks)
•   Pessimistic → 2 Marks
•   Optimistic → 2 Marks
•   Laplace → 3 Marks
•   Regret table + decision → 3 Marks
CO-1,4; b
BL-
Apply
10
Decision variables and obj function-------------------2M
********** 4 **********
--- page 5 ---
Step 3: Constraints

Weight requirement (exactly 150 kg)
Each unit contributes weight:

5a + 10y = 150

Simplify:
x+2y = 30
Minimum usage of B
y>14
Maximum usage of A
a < 20
Non-negativity
z,y>0
weneecneecenneeeee 3M
Graphical solution:
x2
15)
30
x1 20
aonnenneene nee 3M
x1 x2 z
15 120
2 14 116
(untitled) Solution
x1 X2 RHS
Minimize 2 8
Constraint 1 (5 10 |= | 150
Constraint 2 0 1 >= 14
Constraint 3 \1 0 [<= |20
Solution-> 2 14 116
Q3 [20]
CO-1,4; | a
BL- 10
Apply

FIC DI EH ar
--- page 6 ---
Writing std form---------------2M
Iteration 1(table, cj-zj, KC, KR etc)-----------------3M
Calculations for iteration2--------------3M
Iteration2 (table, cj-zj)----------------1M
Final ans----------------1M
CO-1,2; b   Step 1: Given Data
BL-   Cost price (C) = ₹10 per dozen
Analyze   Selling price (SP) = ₹30 per dozen
Profit per sold dozen = ₹20
Unsold roses → no salvage (loss = ₹10 per dozen)
Demand distribution:
Demand (dozens)   70   80   90   100
Probability   0.1   0.2   0.4   0.3
Step 2: Payoff Table (Profit ₹)
Order \ Demand   70   80   90   100
10
70   1400   1400   1400   1400
80   1300   1600   1600   1600
90   1200   1500   1800   1800
100   1100   1400   1700   2000
Step 3: EMV Calculation
EMV=∑ (Payoff × Probability)
• EMV(70) = 1400
• EMV(80) = 1300×0.1+1600×0.9=1570
• EMV(90) = 1200×0.1+1500×0.2+1800×0.7=1680
• EMV(100) = 1100×0.1+1400×0.2+1700×0.4+2000×0.3=1670
Maximum EMV = 1680 (Order 90 dozen)
********** 6 **********

[Text in pictures on this page, read by OCR]
Maximize
Z = 40002, + 200022 + 500023 + 0s; + Oso
Subject to:
122, + Tag + 9x3 + 8, = 1260
222; + 1822 + 16x3 + s2 = 19008

21,2, 23, $1, 82 >0

Cj Basic 4000 wee poe i) 0

Variables Quantity x1 slack 1 slack 2
a a ST ST
slack 1 1,260
i} slack 2 19,008 22 18 16 0 1
Zz 0 0 0 0

cj-zj 4,000 2,000 5,000
iteration 2 a
5000 140 1.3333 0.7778 1
i} slack 2 16,768 0.6667 5.5556 i)

q 7,00,000 6666.67 3888.89 5000
cj-zj -2,666.66. -1,888.88. 0. -555.5556 0
--- page 7 ---
Step 4: EOL (Regret Table)
Column maximums:
• 70 → 1400
• 80 → 1600
• 90 → 1800
• 100 → 2000
Regret Table
Order \ Demand   70   80   90   100
70   0   200   400   600
80   100   0   200   400
90   200   100   0   200
100   300   200   100   0
EOL Calculation
• EOL(70) = 0×0.1+200×0.2+400×0.4+600×0.3=380
• EOL(80) = 100×0.1+0×0.2+200×0.4+400×0.3=210
• EOL(90) = 200×0.1+100×0.2+0×0.4+200×0.3=100
• EOL(100) = 300×0.1+200×0.2+100×0.4+0×0.3=110
Minimum EOL = 100 (Order 90 dozen)
Marking Scheme (10 Marks)
•   Payoff table → 3 Marks
• EMV calculation → 3 Marks
•   Regret table → 2 Marks
• EOL calculation → 1 Mark
•   Final decision → 1 Mark
Q4   [20]
CO-1,4; a
BL-
Apply
10
********** 7 **********
--- page 8 ---
Iteration 1(for given table calculation of zj, cj-zj, KC, KR etc)----------------- 4M
Calculations for iteration2--------------3M
Iteration2 (table, zj, cj-zj)----------------2M
Final ans----------------1M
CO-1,4; b   Solve LP Relaxation: [4 Marks]
BL-   Ignore the integer restriction first.
Analyze   Solving the problem, A graphically, we find that:
LP optimum = (4.5, 0), Z = 31.5 which is an LP optimal solution
Solving Sub-Problem B: [3 Marks]
Solving Sub-Problem C: [2 Marks]
10
Branch and bound algorithm thus terminated and the optimal integer solution is :
ZB=31 and X1 =4, X2 =1
Q5   [20]
CO-   a   Step 1: Check Balance
1,3;   Total Supply = 40 + 20 + 40 = 100
BL-   Total Demand = 25 + 10 + 20 + 30 + 15 = 100
Analyze   Balanced
Step 2: Initial Basic Feasible Solution (VAM)
One optimal allocation:
A   B   C   D   E   Supply
Agra   –   10   20   –   10   40
Allahabad   20   –   –   –   –   20
10
Kolkata   5   –   –   30   5   40
Demand   25   10   20   30   15
Step 3: Total Transportation Cost
=10×30 + 20×40 + 10×40 + 20×35 + 5×40 + 30×35 + 5×30= 3600
Step 4: Optimality (MODI Test)
Using ui, vj method:
•   All opportunity costs dij≥0
Solution is optimal
Marking Scheme (10 Marks)
********** 8 **********
--- page 9 ---
•   Balance check → 1 Mark
•   Initial solution (VAM/NWCM) → 3 Marks
•   Cost calculation → 2 Marks
•   ui, vj calculation → 2 Marks
•   Optimality test → 1 Mark
•   Final answer → 1 Mark
CO-   b Row Dominance (1 Marks)
1,2;   Row 2 ≥ Row 4 for all entries: Eliminate Row 4
BL-
Analyze   Column Dominance (2 Marks)
Column II is smaller everywhere: Eliminate Column I
Column II dominates Column III: Eliminate Column III
Reduced Matrix (1 Marks)
II   IV
1   2   3
2   3   2
3   1   5
Reducing to 2x2 Matrix by Convex combinations: [2 Marks]
II   IV
1   2   3
2   3   2
10
Check Saddle Point (1 Marks)
Maximin is not equal to Minimax
• Saddle Point does not exist
Finding the Probability for A [ 1 Marks]
1 = 1/2
2 = 1/2
Finding the Probability for B [ 1 Marks]
II=1/2
IV=1/2
Value of the Game=2.5 (1 Marks)
Q6   [20]
********** 9 **********
--- page 10 ---
CO-1,3; a   Given Cost Matrix (‘000 Rs)
BL-   Bidder   I   II   III   IV   V
Apply   1   41   72   39   52   25
2   22   29   49   65   81
3   27   39   60   51   40
4   45   50   48   52   37
5   29   40   45   26   30
Optimal Assignment (Hungarian Method)
Bidder   Project   Cost (‘000 Rs)
1   V   25
2   I   22
3   II   39
4   III   48
5   IV   26   10
Minimum Total Cost =25+22+39+48+26 =160
Minimum Cost = ₹160,000
Marking Scheme (10 Marks)
•   Cost matrix formulation → 1 Mark
• Row reduction → 2 Marks
• Column reduction → 2 Marks
•   Zero allocation & optimality → 3 Marks
•   Final assignment → 1 Mark
•   Total cost → 1 Mark
********** 10 **********
--- page 11 ---
CO-1,4; b
BL-   Iteration 1 [02 Marks]
Analyze
Cj   4   3   0   0
CB   Basis   x1   x2   S1   S2   RHS
4   x1   1   0   0.67   -0.33   1.67
3   x2   0   1   -0.33   0.67   1.67
Zj   Z=11.67   4   3   1.67   0.67
Cj-Zj   0   0   -1.67   -0.67
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as:
x1=5.5, x2=0
Max Z=33
Add Gomory Cut [02 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut,
with the help of x2-row as follows:
1.67=1x2-0.33S1+0.67S2
(1+0.67) = (1+0) x2+(-1+0.67) S1+(0+0.67) S2
The fractional cut will become
-0.67=Sg1-0.67S1-0.67S2→ (Cut-1)
Adding Gomory Constraint in the Table and relevant calculations [03 Marks]
Cj   4   3   0   0   0   10
CB   Basis   x1   x2   S1   S2   Sg1   RHS
4   x1   1   0   0.67   -0.33   0   1.67
3   x2   0   1   -0.33   0.67   0   1.67
0   Sg1   0   0   -0.67   (-0.67)   1   -0.67→
Z=11.67   Zj   4   3   1.67   0.67   0
Cj-Zj   0   0   -1.67   -0.67   0
Ratio   Cj-   --   --   2.5   1↑   ---
Zj/Sg1,j
Most negative RHS is -0.67 and its row index is 3. So, the leaving basis variable is Sg1.
Least positive ratio is 1 and its column index is 4. So, the entering variable is S2.
∴ The pivot element is -0.67.
Entering =S2, Departing =Sg1, Key Element =-0.67
New Iteration [02 Marks]
Cj   4   3   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1 RHS
4   x1   1   0   1   0   -0.5   2
3   x2   0   1   -1   0   1   1
0   S2   0   0   1   1   -1.5   1
Z=11   Zj   4   3   1   0   1
Cj-Zj   0   0   -1   0   -1
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as [1 Marks]:
x1=2, x2=1, Max Z=11
********** 11 **********
--- page 12 ---
Q7   [20]
CO-   a
1,3;   Step 1: Cost Matrix (Hundreds of ₹)
BL-   (Replace prohibited entries with a very large number MMM)
Analyze   Machine   A   B   C   D   E
M1   9   11   15   10   11
M2   12   9   M   10   9
M3   M   11   14   11   7
M4   14   8   12   7   8
Step 2: Solve using Hungarian Method
(After row/column reductions and optimal zero assignment)
8
Optimal Assignment
Machine   Location   Cost
M1   A   9
M2   B   9
M3   E   7
M4   D   7
(Note: One location remains unused since 5 locations & 4 machines)
Minimum Total Cost = 9 + 9 + 7 + 7 = 32
In rupees: 32×100 = ₹ 3200
CO-   b
1,4;
BL-
Apply
-------------------4M
6
-------------------2M
********** 12 **********

[Text in pictures on this page, read by OCR]
(untitled) Solution

x1 x2 RHS
Minimize 200 400
Constraint 1 1 1 >= 200
Constraint 2 1 3 >= 400
Constraint 3 1 2 <= 350
Solution-> 100 100 60000
--- page 13 ---
CO-   c
1,4;
BL-   i. Recommended Method and Justification [3 Marks]
Apply   The recommended method is the Branch and Bound Method.
Justification
• The problem has only two variables, so the feasible region can be easily visualized
graphically.
• With only one fractional basic variable, branching can be done once, leading to
just two subproblems.
• The method is intuitive and easy to apply graphically, making it more suitable in
this case.
•   In contrast, the Gomory Cutting Plane Method involves additional tableau
computations, which are less convenient for graphical problems.
Procedure of the Chosen Method (Branch and Bound) [3 Marks]
1. Solve LP Relaxation
o Ignore integer restrictions and obtain the optimal fractional solution.
2. Branching
o   Select the variable with fractional value (say x1=2.6)   6
o Create two subproblems: x1≤2andx1≥3
3. Solve Subproblems
o Solve each subproblem graphically (or using LP)
o Obtain optimal values for each branch
4. Bounding
o Compare objective values
o Use LP values as upper bounds
5. Pruning
o Discard branches that are:
▪   Infeasible, or
▪   Inferior to an already obtained integer solution
6. Select Optimal Integer Solution
Choose the feasible integer solution with the best objective value
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper fbc7a459a946

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AI_7012/Optimization Techniques/ANS_Optimization Techniques(702AI0C031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: mixed (13 pages), mean OCR confidence 80.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Optimization Techniques
Date: 04 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [10]
********** 1 **********
--- page 2 ---
CO-1,4;   a.
BL-
Apply
5
CO-1,3;   b.   Step 1: Check Balance
BL-   Total Supply = 10 + 15 + 40 = 65
Apply   Total Demand = 20 + 15 + 30 = 65
Balanced problem
Step 2: NWCM Allocation
Start from top-left (S1–D1):
D1   D2   D3   Supply
S1   10   –   –   10
S2   10   5   –   15
S3   –   10   30   40   5
Demand   20   15   30
Step 3: Total Transportation Cost
=10×2+10×4+5×1+10×3+30×1
=20+40+5+30+30=125
Marking Scheme (5 Marks)
•   Balance check → 1 Mark
•   Correct NWCM allocations → 3 Marks
•   Total cost → 1 Mark
•
********** 2 **********
--- page 3 ---
CO-1,2;   c.
BL-   Given Payoff Table
Apply   Strategy   N1   N2   Minimum
S1   60   40   40
S2   20   30   20
S3   100   -10   -10
(a) Maximin Criterion
Maximin = 40
Best Strategy = S1
(b) Minimax Regret Criterion
Step 2: Regret Table
5
Strategy   N1   N2   Maximum Regret
S1   40   0   40
S2   80   10   80
S3   0   50   50
Minimum regret = 40
Best Strategy = S1
Marking Scheme (5 Marks)
• Maximin calculation → 2 Marks
•   Regret table → 2 Marks
•   Final decision → 1 Mark
CO-1,2;   d. Step 1: Row minima
BL-   • Row 1 → min = 1
Analyze   • Row 2 → min = 2
• Row 3 → min = 0
Maximin = 2 [1 Marks]
Step 2: Column maxima
• Column I → max = 3
• Column II → max = 2
• Column III → max = 4
Minimax = 2 [1 Marks]
5
Step 3: Conclusion
• Maximin = Minimax = 2 → Saddle point exists [1 Marks]
Step 4: Optimal Strategy [1 Marks]
•   Saddle point at (Row 2, Column II)
•   Optimal strategies:
o Player A: Row 2
o Player B: Column II
Step 5: Value of the Game [1 Marks]
Value = 2
Q2   [20]
CO-1,2; a   Given Payoff Table (₹)
BL-   Strategy High Medium Low   Maximum Minimum Laplace
Analyze   A   80000 40000   -20000 80000   -20000   33333.33
B   60000 35000   5000   60000   5000   33333.33
C   30000 25000   15000   30000   15000   23333.33
10
(i) Pessimistic Criterion (Maximin)
Maximin = 15000
Best Strategy = C
********** 3 **********
--- page 4 ---
(ii) Optimistic Criterion (Maximax)
Maximax = 80000
Best Strategy = A
(iii) Equally Likely (Laplace Criterion)
Best Strategy = A or B (tie)
(iv) Minimax Regret Criterion
Step 1: Column Maximums
High → 80000
Medium → 40000
Low → 15000
Step 2: Regret Table
Strategy   High   Medium   Low   Maximum
A   0   0   35000   35000
B   20000   5000   10000   20000
C   50000   15000   0   50000
Minimum regret = 20000
Best Strategy = B
Marking Scheme (10 Marks)
•   Pessimistic → 2 Marks
•   Optimistic → 2 Marks
•   Laplace → 3 Marks
•   Regret table + decision → 3 Marks
CO-1,4; b
BL-
Apply
10
Decision variables and obj function-------------------2M
********** 4 **********
--- page 5 ---
Step 3: Constraints

Weight requirement (exactly 150 kg)
Each unit contributes weight:

5a + 10y = 150

Simplify:
x+2y = 30
Minimum usage of B
y>14
Maximum usage of A
a < 20
Non-negativity
z,y>0
weneecneecenneeeee 3M
Graphical solution:
x2
15)
30
x1 20
aonnenneene nee 3M
x1 x2 z
15 120
2 14 116
(untitled) Solution
x1 X2 RHS
Minimize 2 8
Constraint 1 (5 10 |= | 150
Constraint 2 0 1 >= 14
Constraint 3 \1 0 [<= |20
Solution-> 2 14 116
Q3 [20]
CO-1,4; | a
BL- 10
Apply

FIC DI EH ar
--- page 6 ---
Writing std form---------------2M
Iteration 1(table, cj-zj, KC, KR etc)-----------------3M
Calculations for iteration2--------------3M
Iteration2 (table, cj-zj)----------------1M
Final ans----------------1M
CO-1,2; b   Step 1: Given Data
BL-   Cost price (C) = ₹10 per dozen
Analyze   Selling price (SP) = ₹30 per dozen
Profit per sold dozen = ₹20
Unsold roses → no salvage (loss = ₹10 per dozen)
Demand distribution:
Demand (dozens)   70   80   90   100
Probability   0.1   0.2   0.4   0.3
Step 2: Payoff Table (Profit ₹)
Order \ Demand   70   80   90   100
10
70   1400   1400   1400   1400
80   1300   1600   1600   1600
90   1200   1500   1800   1800
100   1100   1400   1700   2000
Step 3: EMV Calculation
EMV=∑ (Payoff × Probability)
• EMV(70) = 1400
• EMV(80) = 1300×0.1+1600×0.9=1570
• EMV(90) = 1200×0.1+1500×0.2+1800×0.7=1680
• EMV(100) = 1100×0.1+1400×0.2+1700×0.4+2000×0.3=1670
Maximum EMV = 1680 (Order 90 dozen)
********** 6 **********

[Text in pictures on this page, read by OCR]
Maximize
Z = 40002, + 200022 + 500023 + 0s; + Oso
Subject to:
122, + Tag + 9x3 + 8, = 1260
222; + 1822 + 16x3 + s2 = 19008

21,2, 23, $1, 82 >0

Cj Basic 4000 wee poe i) 0

Variables Quantity x1 slack 1 slack 2
a a ST ST
slack 1 1,260
i} slack 2 19,008 22 18 16 0 1
Zz 0 0 0 0

cj-zj 4,000 2,000 5,000
iteration 2 a
5000 140 1.3333 0.7778 1
i} slack 2 16,768 0.6667 5.5556 i)

q 7,00,000 6666.67 3888.89 5000
cj-zj -2,666.66. -1,888.88. 0. -555.5556 0
--- page 7 ---
Step 4: EOL (Regret Table)
Column maximums:
• 70 → 1400
• 80 → 1600
• 90 → 1800
• 100 → 2000
Regret Table
Order \ Demand   70   80   90   100
70   0   200   400   600
80   100   0   200   400
90   200   100   0   200
100   300   200   100   0
EOL Calculation
• EOL(70) = 0×0.1+200×0.2+400×0.4+600×0.3=380
• EOL(80) = 100×0.1+0×0.2+200×0.4+400×0.3=210
• EOL(90) = 200×0.1+100×0.2+0×0.4+200×0.3=100
• EOL(100) = 300×0.1+200×0.2+100×0.4+0×0.3=110
Minimum EOL = 100 (Order 90 dozen)
Marking Scheme (10 Marks)
•   Payoff table → 3 Marks
• EMV calculation → 3 Marks
•   Regret table → 2 Marks
• EOL calculation → 1 Mark
•   Final decision → 1 Mark
Q4   [20]
CO-1,4; a
BL-
Apply
10
********** 7 **********
--- page 8 ---
Iteration 1(for given table calculation of zj, cj-zj, KC, KR etc)----------------- 4M
Calculations for iteration2--------------3M
Iteration2 (table, zj, cj-zj)----------------2M
Final ans----------------1M
CO-1,4; b   Solve LP Relaxation: [4 Marks]
BL-   Ignore the integer restriction first.
Analyze   Solving the problem, A graphically, we find that:
LP optimum = (4.5, 0), Z = 31.5 which is an LP optimal solution
Solving Sub-Problem B: [3 Marks]
Solving Sub-Problem C: [2 Marks]
10
Branch and bound algorithm thus terminated and the optimal integer solution is :
ZB=31 and X1 =4, X2 =1
Q5   [20]
CO-   a   Step 1: Check Balance
1,3;   Total Supply = 40 + 20 + 40 = 100
BL-   Total Demand = 25 + 10 + 20 + 30 + 15 = 100
Analyze   Balanced
Step 2: Initial Basic Feasible Solution (VAM)
One optimal allocation:
A   B   C   D   E   Supply
Agra   –   10   20   –   10   40
Allahabad   20   –   –   –   –   20
10
Kolkata   5   –   –   30   5   40
Demand   25   10   20   30   15
Step 3: Total Transportation Cost
=10×30 + 20×40 + 10×40 + 20×35 + 5×40 + 30×35 + 5×30= 3600
Step 4: Optimality (MODI Test)
Using ui, vj method:
•   All opportunity costs dij≥0
Solution is optimal
Marking Scheme (10 Marks)
********** 8 **********
--- page 9 ---
•   Balance check → 1 Mark
•   Initial solution (VAM/NWCM) → 3 Marks
•   Cost calculation → 2 Marks
•   ui, vj calculation → 2 Marks
•   Optimality test → 1 Mark
•   Final answer → 1 Mark
CO-   b Row Dominance (1 Marks)
1,2;   Row 2 ≥ Row 4 for all entries: Eliminate Row 4
BL-
Analyze   Column Dominance (2 Marks)
Column II is smaller everywhere: Eliminate Column I
Column II dominates Column III: Eliminate Column III
Reduced Matrix (1 Marks)
II   IV
1   2   3
2   3   2
3   1   5
Reducing to 2x2 Matrix by Convex combinations: [2 Marks]
II   IV
1   2   3
2   3   2
10
Check Saddle Point (1 Marks)
Maximin is not equal to Minimax
• Saddle Point does not exist
Finding the Probability for A [ 1 Marks]
1 = 1/2
2 = 1/2
Finding the Probability for B [ 1 Marks]
II=1/2
IV=1/2
Value of the Game=2.5 (1 Marks)
Q6   [20]
********** 9 **********
--- page 10 ---
CO-1,3; a   Given Cost Matrix (‘000 Rs)
BL-   Bidder   I   II   III   IV   V
Apply   1   41   72   39   52   25
2   22   29   49   65   81
3   27   39   60   51   40
4   45   50   48   52   37
5   29   40   45   26   30
Optimal Assignment (Hungarian Method)
Bidder   Project   Cost (‘000 Rs)
1   V   25
2   I   22
3   II   39
4   III   48
5   IV   26   10
Minimum Total Cost =25+22+39+48+26 =160
Minimum Cost = ₹160,000
Marking Scheme (10 Marks)
•   Cost matrix formulation → 1 Mark
• Row reduction → 2 Marks
• Column reduction → 2 Marks
•   Zero allocation & optimality → 3 Marks
•   Final assignment → 1 Mark
•   Total cost → 1 Mark
********** 10 **********
--- page 11 ---
CO-1,4; b
BL-   Iteration 1 [02 Marks]
Analyze
Cj   4   3   0   0
CB   Basis   x1   x2   S1   S2   RHS
4   x1   1   0   0.67   -0.33   1.67
3   x2   0   1   -0.33   0.67   1.67
Zj   Z=11.67   4   3   1.67   0.67
Cj-Zj   0   0   -1.67   -0.67
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as:
x1=5.5, x2=0
Max Z=33
Add Gomory Cut [02 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut,
with the help of x2-row as follows:
1.67=1x2-0.33S1+0.67S2
(1+0.67) = (1+0) x2+(-1+0.67) S1+(0+0.67) S2
The fractional cut will become
-0.67=Sg1-0.67S1-0.67S2→ (Cut-1)
Adding Gomory Constraint in the Table and relevant calculations [03 Marks]
Cj   4   3   0   0   0   10
CB   Basis   x1   x2   S1   S2   Sg1   RHS
4   x1   1   0   0.67   -0.33   0   1.67
3   x2   0   1   -0.33   0.67   0   1.67
0   Sg1   0   0   -0.67   (-0.67)   1   -0.67→
Z=11.67   Zj   4   3   1.67   0.67   0
Cj-Zj   0   0   -1.67   -0.67   0
Ratio   Cj-   --   --   2.5   1↑   ---
Zj/Sg1,j
Most negative RHS is -0.67 and its row index is 3. So, the leaving basis variable is Sg1.
Least positive ratio is 1 and its column index is 4. So, the entering variable is S2.
∴ The pivot element is -0.67.
Entering =S2, Departing =Sg1, Key Element =-0.67
New Iteration [02 Marks]
Cj   4   3   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1 RHS
4   x1   1   0   1   0   -0.5   2
3   x2   0   1   -1   0   1   1
0   S2   0   0   1   1   -1.5   1
Z=11   Zj   4   3   1   0   1
Cj-Zj   0   0   -1   0   -1
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as [1 Marks]:
x1=2, x2=1, Max Z=11
********** 11 **********
--- page 12 ---
Q7   [20]
CO-   a
1,3;   Step 1: Cost Matrix (Hundreds of ₹)
BL-   (Replace prohibited entries with a very large number MMM)
Analyze   Machine   A   B   C   D   E
M1   9   11   15   10   11
M2   12   9   M   10   9
M3   M   11   14   11   7
M4   14   8   12   7   8
Step 2: Solve using Hungarian Method
(After row/column reductions and optimal zero assignment)
8
Optimal Assignment
Machine   Location   Cost
M1   A   9
M2   B   9
M3   E   7
M4   D   7
(Note: One location remains unused since 5 locations & 4 machines)
Minimum Total Cost = 9 + 9 + 7 + 7 = 32
In rupees: 32×100 = ₹ 3200
CO-   b
1,4;
BL-
Apply
-------------------4M
6
-------------------2M
********** 12 **********

[Text in pictures on this page, read by OCR]
(untitled) Solution

x1 x2 RHS
Minimize 200 400
Constraint 1 1 1 >= 200
Constraint 2 1 3 >= 400
Constraint 3 1 2 <= 350
Solution-> 100 100 60000
--- page 13 ---
CO-   c
1,4;
BL-   i. Recommended Method and Justification [3 Marks]
Apply   The recommended method is the Branch and Bound Method.
Justification
• The problem has only two variables, so the feasible region can be easily visualized
graphically.
• With only one fractional basic variable, branching can be done once, leading to
just two subproblems.
• The method is intuitive and easy to apply graphically, making it more suitable in
this case.
•   In contrast, the Gomory Cutting Plane Method involves additional tableau
computations, which are less convenient for graphical problems.
Procedure of the Chosen Method (Branch and Bound) [3 Marks]
1. Solve LP Relaxation
o Ignore integer restrictions and obtain the optimal fractional solution.
2. Branching
o   Select the variable with fractional value (say x1=2.6)   6
o Create two subproblems: x1≤2andx1≥3
3. Solve Subproblems
o Solve each subproblem graphically (or using LP)
o Obtain optimal values for each branch
4. Bounding
o Compare objective values
o Use LP values as upper bounds
5. Pruning
o Discard branches that are:
▪   Infeasible, or
▪   Inferior to an already obtained integer solution
6. Select Optimal Integer Solution
Choose the feasible integer solution with the best objective value
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper dc65534e8fa7

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_AI_7051/Optimization Techniques/ANS_Optimization Techniques(702AI0C031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: mixed (13 pages), mean OCR confidence 80.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Optimization Techniques
Date: 04 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [10]
********** 1 **********
--- page 2 ---
CO-1,4;   a.
BL-
Apply
5
CO-1,3;   b.   Step 1: Check Balance
BL-   Total Supply = 10 + 15 + 40 = 65
Apply   Total Demand = 20 + 15 + 30 = 65
Balanced problem
Step 2: NWCM Allocation
Start from top-left (S1–D1):
D1   D2   D3   Supply
S1   10   –   –   10
S2   10   5   –   15
S3   –   10   30   40   5
Demand   20   15   30
Step 3: Total Transportation Cost
=10×2+10×4+5×1+10×3+30×1
=20+40+5+30+30=125
Marking Scheme (5 Marks)
•   Balance check → 1 Mark
•   Correct NWCM allocations → 3 Marks
•   Total cost → 1 Mark
•
********** 2 **********
--- page 3 ---
CO-1,2;   c.
BL-   Given Payoff Table
Apply   Strategy   N1   N2   Minimum
S1   60   40   40
S2   20   30   20
S3   100   -10   -10
(a) Maximin Criterion
Maximin = 40
Best Strategy = S1
(b) Minimax Regret Criterion
Step 2: Regret Table
5
Strategy   N1   N2   Maximum Regret
S1   40   0   40
S2   80   10   80
S3   0   50   50
Minimum regret = 40
Best Strategy = S1
Marking Scheme (5 Marks)
• Maximin calculation → 2 Marks
•   Regret table → 2 Marks
•   Final decision → 1 Mark
CO-1,2;   d. Step 1: Row minima
BL-   • Row 1 → min = 1
Analyze   • Row 2 → min = 2
• Row 3 → min = 0
Maximin = 2 [1 Marks]
Step 2: Column maxima
• Column I → max = 3
• Column II → max = 2
• Column III → max = 4
Minimax = 2 [1 Marks]
5
Step 3: Conclusion
• Maximin = Minimax = 2 → Saddle point exists [1 Marks]
Step 4: Optimal Strategy [1 Marks]
•   Saddle point at (Row 2, Column II)
•   Optimal strategies:
o Player A: Row 2
o Player B: Column II
Step 5: Value of the Game [1 Marks]
Value = 2
Q2   [20]
CO-1,2; a   Given Payoff Table (₹)
BL-   Strategy High Medium Low   Maximum Minimum Laplace
Analyze   A   80000 40000   -20000 80000   -20000   33333.33
B   60000 35000   5000   60000   5000   33333.33
C   30000 25000   15000   30000   15000   23333.33
10
(i) Pessimistic Criterion (Maximin)
Maximin = 15000
Best Strategy = C
********** 3 **********
--- page 4 ---
(ii) Optimistic Criterion (Maximax)
Maximax = 80000
Best Strategy = A
(iii) Equally Likely (Laplace Criterion)
Best Strategy = A or B (tie)
(iv) Minimax Regret Criterion
Step 1: Column Maximums
High → 80000
Medium → 40000
Low → 15000
Step 2: Regret Table
Strategy   High   Medium   Low   Maximum
A   0   0   35000   35000
B   20000   5000   10000   20000
C   50000   15000   0   50000
Minimum regret = 20000
Best Strategy = B
Marking Scheme (10 Marks)
•   Pessimistic → 2 Marks
•   Optimistic → 2 Marks
•   Laplace → 3 Marks
•   Regret table + decision → 3 Marks
CO-1,4; b
BL-
Apply
10
Decision variables and obj function-------------------2M
********** 4 **********
--- page 5 ---
Step 3: Constraints

Weight requirement (exactly 150 kg)
Each unit contributes weight:

5a + 10y = 150

Simplify:
x+2y = 30
Minimum usage of B
y>14
Maximum usage of A
a < 20
Non-negativity
z,y>0
weneecneecenneeeee 3M
Graphical solution:
x2
15)
30
x1 20
aonnenneene nee 3M
x1 x2 z
15 120
2 14 116
(untitled) Solution
x1 X2 RHS
Minimize 2 8
Constraint 1 (5 10 |= | 150
Constraint 2 0 1 >= 14
Constraint 3 \1 0 [<= |20
Solution-> 2 14 116
Q3 [20]
CO-1,4; | a
BL- 10
Apply

FIC DI EH ar
--- page 6 ---
Writing std form---------------2M
Iteration 1(table, cj-zj, KC, KR etc)-----------------3M
Calculations for iteration2--------------3M
Iteration2 (table, cj-zj)----------------1M
Final ans----------------1M
CO-1,2; b   Step 1: Given Data
BL-   Cost price (C) = ₹10 per dozen
Analyze   Selling price (SP) = ₹30 per dozen
Profit per sold dozen = ₹20
Unsold roses → no salvage (loss = ₹10 per dozen)
Demand distribution:
Demand (dozens)   70   80   90   100
Probability   0.1   0.2   0.4   0.3
Step 2: Payoff Table (Profit ₹)
Order \ Demand   70   80   90   100
10
70   1400   1400   1400   1400
80   1300   1600   1600   1600
90   1200   1500   1800   1800
100   1100   1400   1700   2000
Step 3: EMV Calculation
EMV=∑ (Payoff × Probability)
• EMV(70) = 1400
• EMV(80) = 1300×0.1+1600×0.9=1570
• EMV(90) = 1200×0.1+1500×0.2+1800×0.7=1680
• EMV(100) = 1100×0.1+1400×0.2+1700×0.4+2000×0.3=1670
Maximum EMV = 1680 (Order 90 dozen)
********** 6 **********

[Text in pictures on this page, read by OCR]
Maximize
Z = 40002, + 200022 + 500023 + 0s; + Oso
Subject to:
122, + Tag + 9x3 + 8, = 1260
222; + 1822 + 16x3 + s2 = 19008

21,2, 23, $1, 82 >0

Cj Basic 4000 wee poe i) 0

Variables Quantity x1 slack 1 slack 2
a a ST ST
slack 1 1,260
i} slack 2 19,008 22 18 16 0 1
Zz 0 0 0 0

cj-zj 4,000 2,000 5,000
iteration 2 a
5000 140 1.3333 0.7778 1
i} slack 2 16,768 0.6667 5.5556 i)

q 7,00,000 6666.67 3888.89 5000
cj-zj -2,666.66. -1,888.88. 0. -555.5556 0
--- page 7 ---
Step 4: EOL (Regret Table)
Column maximums:
• 70 → 1400
• 80 → 1600
• 90 → 1800
• 100 → 2000
Regret Table
Order \ Demand   70   80   90   100
70   0   200   400   600
80   100   0   200   400
90   200   100   0   200
100   300   200   100   0
EOL Calculation
• EOL(70) = 0×0.1+200×0.2+400×0.4+600×0.3=380
• EOL(80) = 100×0.1+0×0.2+200×0.4+400×0.3=210
• EOL(90) = 200×0.1+100×0.2+0×0.4+200×0.3=100
• EOL(100) = 300×0.1+200×0.2+100×0.4+0×0.3=110
Minimum EOL = 100 (Order 90 dozen)
Marking Scheme (10 Marks)
•   Payoff table → 3 Marks
• EMV calculation → 3 Marks
•   Regret table → 2 Marks
• EOL calculation → 1 Mark
•   Final decision → 1 Mark
Q4   [20]
CO-1,4; a
BL-
Apply
10
********** 7 **********
--- page 8 ---
Iteration 1(for given table calculation of zj, cj-zj, KC, KR etc)----------------- 4M
Calculations for iteration2--------------3M
Iteration2 (table, zj, cj-zj)----------------2M
Final ans----------------1M
CO-1,4; b   Solve LP Relaxation: [4 Marks]
BL-   Ignore the integer restriction first.
Analyze   Solving the problem, A graphically, we find that:
LP optimum = (4.5, 0), Z = 31.5 which is an LP optimal solution
Solving Sub-Problem B: [3 Marks]
Solving Sub-Problem C: [2 Marks]
10
Branch and bound algorithm thus terminated and the optimal integer solution is :
ZB=31 and X1 =4, X2 =1
Q5   [20]
CO-   a   Step 1: Check Balance
1,3;   Total Supply = 40 + 20 + 40 = 100
BL-   Total Demand = 25 + 10 + 20 + 30 + 15 = 100
Analyze   Balanced
Step 2: Initial Basic Feasible Solution (VAM)
One optimal allocation:
A   B   C   D   E   Supply
Agra   –   10   20   –   10   40
Allahabad   20   –   –   –   –   20
10
Kolkata   5   –   –   30   5   40
Demand   25   10   20   30   15
Step 3: Total Transportation Cost
=10×30 + 20×40 + 10×40 + 20×35 + 5×40 + 30×35 + 5×30= 3600
Step 4: Optimality (MODI Test)
Using ui, vj method:
•   All opportunity costs dij≥0
Solution is optimal
Marking Scheme (10 Marks)
********** 8 **********
--- page 9 ---
•   Balance check → 1 Mark
•   Initial solution (VAM/NWCM) → 3 Marks
•   Cost calculation → 2 Marks
•   ui, vj calculation → 2 Marks
•   Optimality test → 1 Mark
•   Final answer → 1 Mark
CO-   b Row Dominance (1 Marks)
1,2;   Row 2 ≥ Row 4 for all entries: Eliminate Row 4
BL-
Analyze   Column Dominance (2 Marks)
Column II is smaller everywhere: Eliminate Column I
Column II dominates Column III: Eliminate Column III
Reduced Matrix (1 Marks)
II   IV
1   2   3
2   3   2
3   1   5
Reducing to 2x2 Matrix by Convex combinations: [2 Marks]
II   IV
1   2   3
2   3   2
10
Check Saddle Point (1 Marks)
Maximin is not equal to Minimax
• Saddle Point does not exist
Finding the Probability for A [ 1 Marks]
1 = 1/2
2 = 1/2
Finding the Probability for B [ 1 Marks]
II=1/2
IV=1/2
Value of the Game=2.5 (1 Marks)
Q6   [20]
********** 9 **********
--- page 10 ---
CO-1,3; a   Given Cost Matrix (‘000 Rs)
BL-   Bidder   I   II   III   IV   V
Apply   1   41   72   39   52   25
2   22   29   49   65   81
3   27   39   60   51   40
4   45   50   48   52   37
5   29   40   45   26   30
Optimal Assignment (Hungarian Method)
Bidder   Project   Cost (‘000 Rs)
1   V   25
2   I   22
3   II   39
4   III   48
5   IV   26   10
Minimum Total Cost =25+22+39+48+26 =160
Minimum Cost = ₹160,000
Marking Scheme (10 Marks)
•   Cost matrix formulation → 1 Mark
• Row reduction → 2 Marks
• Column reduction → 2 Marks
•   Zero allocation & optimality → 3 Marks
•   Final assignment → 1 Mark
•   Total cost → 1 Mark
********** 10 **********
--- page 11 ---
CO-1,4; b
BL-   Iteration 1 [02 Marks]
Analyze
Cj   4   3   0   0
CB   Basis   x1   x2   S1   S2   RHS
4   x1   1   0   0.67   -0.33   1.67
3   x2   0   1   -0.33   0.67   1.67
Zj   Z=11.67   4   3   1.67   0.67
Cj-Zj   0   0   -1.67   -0.67
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as:
x1=5.5, x2=0
Max Z=33
Add Gomory Cut [02 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut,
with the help of x2-row as follows:
1.67=1x2-0.33S1+0.67S2
(1+0.67) = (1+0) x2+(-1+0.67) S1+(0+0.67) S2
The fractional cut will become
-0.67=Sg1-0.67S1-0.67S2→ (Cut-1)
Adding Gomory Constraint in the Table and relevant calculations [03 Marks]
Cj   4   3   0   0   0   10
CB   Basis   x1   x2   S1   S2   Sg1   RHS
4   x1   1   0   0.67   -0.33   0   1.67
3   x2   0   1   -0.33   0.67   0   1.67
0   Sg1   0   0   -0.67   (-0.67)   1   -0.67→
Z=11.67   Zj   4   3   1.67   0.67   0
Cj-Zj   0   0   -1.67   -0.67   0
Ratio   Cj-   --   --   2.5   1↑   ---
Zj/Sg1,j
Most negative RHS is -0.67 and its row index is 3. So, the leaving basis variable is Sg1.
Least positive ratio is 1 and its column index is 4. So, the entering variable is S2.
∴ The pivot element is -0.67.
Entering =S2, Departing =Sg1, Key Element =-0.67
New Iteration [02 Marks]
Cj   4   3   0   0   0
CB   Basis   x1   x2   S1   S2   Sg1 RHS
4   x1   1   0   1   0   -0.5   2
3   x2   0   1   -1   0   1   1
0   S2   0   0   1   1   -1.5   1
Z=11   Zj   4   3   1   0   1
Cj-Zj   0   0   -1   0   -1
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as [1 Marks]:
x1=2, x2=1, Max Z=11
********** 11 **********
--- page 12 ---
Q7   [20]
CO-   a
1,3;   Step 1: Cost Matrix (Hundreds of ₹)
BL-   (Replace prohibited entries with a very large number MMM)
Analyze   Machine   A   B   C   D   E
M1   9   11   15   10   11
M2   12   9   M   10   9
M3   M   11   14   11   7
M4   14   8   12   7   8
Step 2: Solve using Hungarian Method
(After row/column reductions and optimal zero assignment)
8
Optimal Assignment
Machine   Location   Cost
M1   A   9
M2   B   9
M3   E   7
M4   D   7
(Note: One location remains unused since 5 locations & 4 machines)
Minimum Total Cost = 9 + 9 + 7 + 7 = 32
In rupees: 32×100 = ₹ 3200
CO-   b
1,4;
BL-
Apply
-------------------4M
6
-------------------2M
********** 12 **********

[Text in pictures on this page, read by OCR]
(untitled) Solution

x1 x2 RHS
Minimize 200 400
Constraint 1 1 1 >= 200
Constraint 2 1 3 >= 400
Constraint 3 1 2 <= 350
Solution-> 100 100 60000
--- page 13 ---
CO-   c
1,4;
BL-   i. Recommended Method and Justification [3 Marks]
Apply   The recommended method is the Branch and Bound Method.
Justification
• The problem has only two variables, so the feasible region can be easily visualized
graphically.
• With only one fractional basic variable, branching can be done once, leading to
just two subproblems.
• The method is intuitive and easy to apply graphically, making it more suitable in
this case.
•   In contrast, the Gomory Cutting Plane Method involves additional tableau
computations, which are less convenient for graphical problems.
Procedure of the Chosen Method (Branch and Bound) [3 Marks]
1. Solve LP Relaxation
o Ignore integer restrictions and obtain the optimal fractional solution.
2. Branching
o   Select the variable with fractional value (say x1=2.6)   6
o Create two subproblems: x1≤2andx1≥3
3. Solve Subproblems
o Solve each subproblem graphically (or using LP)
o Obtain optimal values for each branch
4. Bounding
o Compare objective values
o Use LP values as upper bounds
5. Pruning
o Discard branches that are:
▪   Infeasible, or
▪   Inferior to an already obtained integer solution
6. Select Optimal Integer Solution
Choose the feasible integer solution with the best objective value
********** 13 **********
````
