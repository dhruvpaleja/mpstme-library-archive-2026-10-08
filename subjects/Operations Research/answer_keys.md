# Operations Research: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 7e96ddcacee7

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSBS_7036/Operations Research/ANS_Operations Research(702BS0C089)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Operations Research
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question no 1 is compulsory
5. Out of remaining question, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1   [20M]
CO-1; a   [5M]
SO-1;   Discuss types of Operation Research models in practice
BL-1   Answer
Deterministic Models (1 mark)
Probabilistic (Stochastic) Models (1 mark)
Static Models (1 mark)
Dynamic Models (1 mark)
Simulation Models (1 mark)
CO-1; b   [5M]
SO-1;   Maximize Z=10x+20y
BL-2
Subject to the constraints
4x+y ≤ 9
x+6y ≤ 12
x,y ≥ 0
Answer:
Maximize
Z = 10x + 20y
Subject to:
4 x + y  9, x + 6 y  12, x , y  0
********** 1 **********
--- page 2 ---
4 x + y = 9   (1)
x + 6 y = 12 (2)   [1]
x = 0  y = 9 (0,9)
9    9   
y = 0  x =    ,0 
4    4   
x = 0  y = 2 (0,2)
y = 0  x = 12 (12,0)   [1]
4 x + y = 9
x + 6 y = 12
 42 39 
   ,    [1]
 23 23 
Z = 10 x + 20 y
Z (0,0) = 0
 9 =
Z  ,0  22.5
 4   
Z (0,2) = 40   [1]
 42 39 = 1200
Z    ,       52.17
 23 23    23
1200
Z max =    52.17 [1]
23
CO-3; c   [5M]
SO-7;   Draw a network for the following project and number the events
BL-2
Activity   A   B   C   D   E   F   G
Immediate   -   -   B   B   B   E   A,D,C
predecessor
********** 2 **********
--- page 3 ---
Answer
[5]
CO-4; d   [5M]
SO-1;   An oil engine manufacturer purchases lubricants at the rate of `42 per piece from a
BL-1   vendor. The requirement of these lubricants is 1,800 per year. What should be the
order quantity per order, if the cost per placement of an order is `16 and inventory
carrying charge per rupee per year is only 20 paise?
Answer
Annual demand, D = 1800 units
Ordering cost, S = 16 (per order)
Cost per unit, C = 42
Carrying cost per rupee per year = 20 paise = 0.20
H = 0.20  42 = 8.4   [2]
2DS
EOQ =   [1]
H
2  1800  16
EOQ =
8.4
57600
=   = 6857.14
8.4
EOQ  82.8  83 units [2]
********** 3 **********
--- page 4 ---
Q2   [20M]
CO-1; a   [10M]
SO-1;   Solve the following LPP graphically
BL-2
Maximize Z=8x+12y
Subject to constraints   2x+y ≥ 9
x ≤𝟒 , y ≤𝟐
20x+50y ≤ 360
x,y ≥ 0
Answer
Maximize
Z = 8 x + 12 y
Subject to:
2 x + y  9, x  4, y  2, 20 x + 50 y  360, x , y  0
[3]
Z = 8 x + 12 y
Z (4,2) = 32 + 24 = 56
Z (4,1) = 32 + 12 = 44
Z (3.5,2) = 28 + 24 = 52
Z max = 56 at ( x , y ) = (4,2) [2]
CO-3; b   [10M]
SO-1;   Listed in the Table are the activities and sequencing requirements necessary for the
BL-3   completion of a research project.
Activity A B C D E   F G   H   I   J
Predecessor   -   - A A A C D   B,D,E   H   I,G,F
********** 4 **********
--- page 5 ---
activity
Duration   6   3   5   4   3   3   5   5   2   3
1. Draw a network diagram for this project.
2. Find the critical path and duration of the project.
3. Find the total, free and independent floats of various activities
Answer
[2]
TF = LS − ES
FF = ES successor − EF
IF = FF − TF successor
Activity   ES   EF   LS   LF   Total   Free
Float   Float
A   0   6   0   6   0   0
B   0   3   7   10   7   7
C   6   11   9   14   3   0
D   6   10   6   10   0   0
E   6   9   7   10   1   1
F   11   14   14   17   3   3
G   10   15   12   17   2   2
H   10   15   10   15   0   0
I   15   17   15   17   0   0
J   17   20   17   20   0   0
Table [6 M]
Activities with zero total float:
A → D → H → I → J [1 M]
Project Duration = 20 units [1 M]
Q3   [20M]
CO-2; a   [10M]
SO-1;   Goods have to be transported from factories F1,F2,F3,F4 to warehouses
BL-2   W1,W2,W3,W4 The transportation cost per unit, capacities and requirement of the
warehouses are given in the table
W1   W2   W3   W4   Capacity
F1   2   4   6   11   20
F2   10   8   7   5   25
F3   13   3   9   12   20
********** 5 **********
--- page 6 ---
F4   4   6   8   3   40
Requirement   25   35   15   30
Find the distribution with minimum cost. Obtain an initial basic feasible solution to
the following transportation problem using Vogel’ s Approximation Method
Answer:
Total Supply = 20 + 25 + 20 + 40 = 105
Total Demand = 25 + 35 + 15 + 30 = 105
Hence, the problem is balanced[1]
Iteration 1:
Row penalties: F 1 = 2, F 2 = 2, F 3 = 6, F 4 = 1
Column penalties:
W 1 = 2, W 2 = 1, W 3 = 1, W 4 = 2
Maximum penalty = 6 (Row F3)
Minimum cost in F3 is at W2 (cost = 3
x 32 = min(20,35) = 20
Update:
F 3 = 0, W 2 = 15 [1]
Iteration 2:
Select column W1 (penalty = 2)
Minimum cost = 2 at F1
x 11 = min(20,25) = 20
F 1 = 0, W 1 = 5 [1]
Iteration 3:
Column W1 has highest penalty
Minimum cost = 4 at F4
x 41 = min(40,5) = 5
Update:
F 4 = 35, W 1 = 0 [2]
Iteration 4:
Row F4 has highest penalty
Minimum cost = 3 at W4
x 44 = min(35,30) = 30
Update:
********** 6 **********
--- page 7 ---
F 4 = 5, W 4 = 0 [1]
Iteration 5:
Row F4 selected
x 42 = min(5,15) = 5
Update:
F 4 = 0, W 2 = 10
Final Allocation:
x 22 = 10, x 23 = 15   [2]
W1   W2   W3   W4
F1   20   0   0   0
F2   0   10   15   0
F3   0   20   0   0
F4   5   5   0   30
[1]
Z = 425 [1]
CO-3; b   [10M]
SO-7;   Consider a two channel waiting line with Poisson arrivals and exponential
BL-4   service times. The mean arrival rate is 14 units per hour, and the mean
service rate is 10 units per hour for each channel.
a. What is the probability that no units are in the system ?
b. What is the average number of units in the system?
c. What is the average time a unit waits for service?
d. What is the average time a unit is in the system?
e. What is the probability of having to wait for service?
[data required is at the end of paper]
the probability that no units are in the system 0.176 [2]
the average number of units in the system 2.74   [2]
the average time a unit waits for service 5.76   [2]
the average time a unit is in the system 11.76   [2]
the probability of having to wait for service 0.575   [2]
Q4   [20M]
CO-1; a   [10M]
SO-1;   Use simplex method to solve the LPP.
BL-3   Maximise Z=6x+4y
Subject to constraints
x+2y≤𝟕𝟐𝟎
2x+y≤𝟕𝟖𝟎
x≤𝟑𝟐𝟎
********** 7 **********
--- page 8 ---
x,y ≥𝟎
Answer
x + 2 y + s 1 = 720
2 x + y + s 2 = 780
x + s 3 = 320   [1]
x   y   s 1   s 2 RHS
s 1   1   2   1 0   720
s 2   2   1   0 1   780 [2]
s 3   1   0   0 0   320
Z − 6 − 4 0 0   0
Entering variable: x (most negative in Z-row)
Leaving variable: 3s (minimum ratio = 320)
Pivot element = 1[1]
x   y   s 1   s 2 RHS
s 1 0 2   1 0   400
s 2 0 1   0 1   140 [2]
x 1 0   0 0   320
Z 0 − 4 0 0 1920
Entering variable: y
Leaving variable: 2s Pivot element = 1
x y   s 1   s 2 RHS
s 1 0 0 1 − 2 120
y 0 1 0   1   140 [2]
x 1 0 0   0   320
Z 0 0 0   4 2480
Since no negative coefficients remain in Z-row:
x = 320, y = 140
Z max = 6(320) + 4(140) = 1920 + 560 = 2480
x = 320, y = 140, Z max = 2480 [2]
CO-2; b The marketing manager of a company needs to assign five regional managers A, B,   [10M]
SO-4;   C, D, and E to four sales zones I, II, III, and IV. Since there are more managers than
BL-2   zones, one manager will remain unassigned, and the corresponding zone will be
handled by a junior manager.Based on past experience, the efficiency (in percentage)
of each manager in each zone—judged by sales, market share, operating cost, etc.—
is given in the table below:
Location
********** 8 **********
--- page 9 ---
Machine   A   B   C   D   E
M1   9   11   15   10   11
M2   12   9   -   10   9
M3   -   11   14   11   7
M4   14   8   12   7   8
1. Determine the optimal assignment of managers to zones so as to maximize
total efficiency.
2. Identify which manager will remain unassigned.
3. Hence, state which zone should be managed by a junior manager
Answer
Zone A B C D E
I   9 11 15 10 11
II   12 9 0 10 9
III   0 11 14 11 7
IV   14 8 12 7 8
V (Dummy) 0 0 0 0 0
[1]
Maximum value = 15
Subtract each entry from 15:
Zone A B C D E
I   6 4 0 5 4
II   3 6 15 5 6
III   15 4 1 4 8
IV   1 7 3 8 7
V   15 15 15 15 15
[2]
Subtract row minimum from each row:
Zone A B C D E
I   6 4 0 5 4
II   0 3 12 2 3
III   14 3 0 3 7
IV   0 6 2 7 6
V   0 0 0 0 0
Column minima are already 0 → no change [2]
Select independent zeros:
• Row I → C
• Row II → A
• Row III → D
********** 9 **********
--- page 10 ---
• Row IV → A already used → choose next feasible: B not zero, so try
alternate set
• Zone I → C Zone II → D Zone III → B Zone IV → A
Zone V (Dummy) → E [2]
From original matrix:
I → C = 15 II → D = 10 III → B = 11 IV → A = 14 [1]
Total Efficiency=50   [1]
Manager E remains unassigned[1]
Q5   [20M]
CO-3; a   [10M]
SO-1;   A small project is composed of activities whose time estimates are listed in the Table
BL-5   below.
Activity   Predecessor Estimated duration (in weeks)
activity
Optimistic   Pessimistic   Most likely
A   -   2   4   3
B   -   8   8   8
C   A   7   11   9
D   B   6   6   6
E   C   9   11   10
F   C   10   18   14
G   C,D   11   11   11
H   F,G   6   14   10
I   E   4   6   5
J   I   3   5   4
K   H   1   1   1
1. Draw the project network.
2. Find the expected duration and variance for each activity.
3. What is the expected project length?
Answer
********** 10 **********
--- page 11 ---
[2]
Activity a m b (t_e) Variance (\sigma^2)
A   2 3 4 3   0.11
B   8 8 8 8   0
C   7 9 11 9   0.44
D   6 6 6 6   0
E   9 10 11 10   0.11
F   10 14 18 14   1.78
G   11 11 11 11 0
H   6 10 14 10   1.78
I   4 5 6 5   0.11
J   3 4 5 4   0.11
K   1 1 1 1   0
Table [[4]]
• Path 1: A → C → E → I → J   31
• Path 2: A → C → F → H → K   37
• Path 3: B → D → G → H → K 36   [2]
• Critical Path = A → C → F → H → K [1]
• Expected Project Duration = 37 weeks [1]
[10M]
b A confectioner sells confectionary items. Past data of demand per week (100 kgs)
CO-4;
SO-1;   Demand/week   0   5   10   15   20   25
BL-3   Frequency   2   11   8   21   5   3
Using the following sequence of random numbers, generate the demand for next 10
weeks. Also, find the average demand per week.
35,52,90,13,23,73,34,57,35,83,94,56,67,66,60
Answer:
Total frequency=50
Frequency Probability
Demand (100 kg)
0   2   2/50 = 0.04
5   11   11/50 = 0.22
10   8   8/50 = 0.16
15   21   21/50 = 0.42
20   5   5/50 = 0.10
25   3   3/50 = 0.06
********** 11 **********
--- page 12 ---
[2]
Demand Probability Cumulative Random Number Interval
0   0.04   0.04   00–03
5   0.22   0.26   04–25
10   0.16   0.42   26–41
15   0.42   0.84   42–83
20   0.10   0.94   84–93
94–99
25   0.06   1.00
[2]
Take first 10 random numbers:
35, 52, 90, 13, 23, 73, 34, 57, 35, 83
Random No. Demand
35 → (26–41) 10
52 → (42–83) 15
90 → (84–93) 20
13 → (04–25) 5
23 → (04–25) 5
73 → (42–83) 15
34 → (26–41) 10
57 → (42–83) 15
35 → (26–41) 10
83 → (42–83) 15
Table [4]
Total demand=120 [1], Average=120/10=12 [1]
Q6   [20M]
CO-1; a   Use Big-M method to   [10M]
SO-1;   Minimize Z=4x+3y
BL-4
subject to
2000x+100y ≥4000
x+2y≥50
40x+40y≥ 1400
x,y ≥0
Answer:
Minimize
Z = 4 x + 3 y
********** 12 **********
--- page 13 ---
Subject to:
20 x + y  40
x + 2 y  50
x + y  35
x , y  0
Introduce surplus and artificial variables:
20 x + y − s 1 + A 1 = 40, x + 2 y − s 2 + A 2 = 50, x + y − s 3 + A 3 = 35 [2]
.
Z = 4 x + 3 y + M ( A 1 + A 2 + A 3 ) [1]
A 1 = 40, A 2 = 50, A 3 = 35 [2]
y = 15, x = 20 [1]
• (0,40) → Z=120
• (50,0) → Z=200[1]
x = 20, y = 15 [1]
Z min = 125 [2]
CO-2; b Solve the following transportation problem using Least Cost Method and   [10M]
SO-1;   obtain initial basic feasible solution
BL-3
A   B   C   D   Supply
1   11   13   17   14   250
2   16   18   14   10   300
3   21   24   13   10   400
Demand 200   225   275   250
Answer:
Total Supply = 250 + 300 + 400 = 950
Total Demand = 200 + 225 + 275 + 250 = 950
Hence, the problem is balanced.[1]
Iteration 1: Minimum cost = 10 at (2,D) and (3,D)
Allocate to (2,D):   min(300,250) = 250
Update: Row 2 supply = 50, Column D demand = 0 [1]
Iteration 2:
Next minimum cost = 10 at (3,D) (column exhausted, skip)
Next minimum = 11 at (1,A)
Allocate: min(250,200) = 200
Update: Row 1 supply = 50, Column A demand = 0 [1]
Iteration 3:
********** 13 **********
--- page 14 ---
Next minimum = 13 at (1,B) and (3,C)
Choose (1,B):min(50,225) = 50
Update: Row 1 supply = 0, Column B demand = 175 [1]
Iteration 4: Next minimum = 13 at (3,C)
Allocate:   min(400,275) = 275
Update:   Row 3 supply = 125, Column C demand = 0 [1]
Iteration 5: Next minimum = 18 at (2,B)
Allocate:   min(50,175) = 50
Update:   Row 2 supply = 0, Column B demand = 125 [1]
Iteration 6: Remaining allocation at (3,B)   min(125,125) = 125 [1]
Initial Basic Feasible Solution
A   B   C D
1 200 50   0   0
[2]
2   0   50   0   250
3   0   125 275   0
Z = 200(11) + 50(13) + 50(18) + 250(10) + 125(24) + 275(13) = 12825 [1]
Q7   [20M]
CO-3; a   [10M]
SO-1;   Marty’ s Barber Shop has one barber. Customers arrive at the rate of 2.2
BL-3   customers per hour and haircuts are given at the average rate of 5 per hour.
Use the Poisson arrivals and exponential service timesw model to answer the
following questions?
a. What is probability that there are no units in the system?
b. What is the probability that 1 customer is receiving haircut and no one is
waiting?
c. What is the probability that 1 customer is receiving haircut and one is
waiting?
d. What is the probability that 1 customer is receiving haircut and two are
waiting?
e. What is the probability that more than two customers are waiting?
Answer:
The probability that there are no units in the system- 0.56 [1]
the probability that 1 customer is receiving haircut and no one is waiting 0.2464 [2]
the probability that 1 customer is receiving haircut and one is waiting 0.1084 [2]
the probability that 1 customer is receiving haircut and two are waiting 0.0477 [2]
the probability that more than two customers are waiting 0.0375 [3]
CO-4; b   [10M]
SO-1;
BL-2
********** 14 **********
--- page 15 ---
A manufacturer has to supply his customers 600 units per year. The setup cost per
production run is ₹80. The holding cost is ₹0.60 per unit per year, and the shortage
cost is ₹1.20 per unit per year. Shortages are allowed.
1. Determine the optimum production quantity.
2. Find the maximum shortage level.
3. Compute the minimum average yearly cost.
Answer:
Formula : [1]
the optimum production quantity= 490 units [2]
Formula : [1]
the maximum shortage level=163 units [2]
Ordering Cost=98, Holding Cost=65.4, Shortage Cost=32.6 [3]
the minimum average yearly cost=196 [1]
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper d60c963dddca

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_Mechatronics_7004/Operations Research/ANS_Operations Research(702MH0E002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (15 pages), mean OCR confidence 80.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Operations Research
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume Suitable data if necessary.
Q1. a infeasibility and unboundedness in linear programming – 2.5 marks each
b. Jockeying and reneging are two distinct customer behaviors in queuing theory, where jockeying is the act
of switching between parallel queues to find the one that appears faster, while reneging is when a customer
leaves a queue entirely after joining it due to a long wait
Jockeying-2.5 marks
Reneging-2.5 marks
c. Flow shop scheduling is a production process where a set of jobs must be processed on a series of machines
in the same order. The goal is to find an optimal sequence for the jobs to minimize the total time it takes for
all jobs to be completed (makespan). 5 marks
d. Models in operations research by purpose and nature of environment – 5 marks
Q2.
a.
********** 1 **********
--- page 2 ---
Stage 4 to Stage 5 (End: Z)

From Node (j) ToNode(k) Timed;,; MinTimetoZ, f,(j) | Shortest Path

s Z 8 8 Seay 4
T Z 7 7 TZ 2 marks
U Z 6 6 UZ
(8 Export to Sheets
Stage 3 (M, N, O) to Stage 4 (S, T, U)
From Node( _— Possible Time dj. + f4(k) Min Time to Z, Optimal Next Node (
j Paths fs() k)
M M>Ss 6+ fa(S) =64+8= 14 s
14
M>T 8+ f(T) =8+7= 2 marks
15
N NOT 44+ f(T) =44+7= n T
11
NU 7+ fa(U) =7+6=
13
fo) O>uU 5+ f,(U) =5+6= n U
11
Stage 2 (P, Q, R) to Stage 3 (M, N, O)
From Node( _ Possible Time dj,x + f3(k) Min Time to Z, Optimal Next Node (
‘) Paths f2(3) k)
P PM 6+ f,(M)=6+144= 18 N
20
PN 7+ f3(N) =7+11=
18
Q Q>N 8+ f3(N) =8+11= 16 °
19
Q-0o 5+ f;(0) =5+11= 2 marks
16
R RN 6+ f3(N) =6+11= 7 N
17
RO 8+ f;(0) =8+11=
19

FIC 2 I HH ar
--- page 3 ---
Stage 1 (Start: X) to Stage 2 (P, Q, R)

From Node( _— Possible Time dj, + fo(k) Min Time to Z, Optimal Next Node (
j) Paths fi(X) k)
Xx XP 4+f.(P)=4+18= 22 P,Q,R
22
X30 6+ fo(Q) =64+ 16=
22
2 marks
XR 5+ fo(R) =5+17=
22
Result

The minimum travel time required is 22.

There are multiple equally short paths:

1.XSGOPGON GT > Z(Time:44+74+4+47 = 22)

2. X3Q@30-+U>Z(Time:6+54+5+6=22) | 2marks
3. XGRGNGT—Z(Time:5 +6+4+7 = 22)
1. Problem Formulation
The objective is to maximize profit Z:
1 mark

Maximize Z = 200rp + 1502¢ + 6025

Subject to the constraints (with slack variables s), 82, $3):

1. 10r%p + 4ae¢ 4+ 2a + s; = 600 (Oak)

2. 5@p + 3xc¢ + 2g + 89 = 250 (Skilled Labor) 3 marks

3. dap + 2%¢ + wg + sz = 150 (Finishing Time)

FC QI a iar
--- page 4 ---
Final Optimal Tableau (Iteration 3)

This tableau shows the optimal solution where all Cj values (coefficients in the Z-row) are non-

negative.
Basis 9 Z zp tc ots $1 82 83 RHS
Z 10 250 00 15.0 00 0.0 75.0 11250.0
sl 0.0 40 00 00 10 00 -20 300.0 4 marks

s2 0.0 O05 00 -05 00 10 -1.5 25.0

Xo 0.0 «15 1.0 0.5 0.0 600 O45 75.0

(8 Export to Sheets

Optimal Solution:
* Max Profit: $11,250.00

¢ Production Mix: zc — 75 units (Cabinets); zp — 0,25 — 0. 2 marks

* Slack: s; — 300 (Oak), s2 = 25 (Labor), s3 — 0 (Finishing Time).

Q3.

FIC 7) IC HOH
--- page 5 ---
3 marks
Now subtract the minimum element of each column from all its elements in turn, and draw minimum number of lines
horizontal or vertical so as to cover all zeros. All zeros can be covered by four lines as given below-
2 marks
2 marks
2 marks
********** 5 **********
--- page 6 ---
Since the minimum no. of lines required to cover all the zeros is only 4 (< 5), optimal assignment cannot be
made at this stage also.
2 marks
1 mark
B
Expected number of people (𝐿𝑞) in the queue of an M/M/1 infinite queue length whose arrival rate (poisson
distribution) is λ/hour, service rate (exponential distribution) is μ/hour. – 8 marks
Q4
A
********** 6 **********
--- page 7 ---
Let x units of product A and y units of product B are purchased.

Required mathematical formulation of L.P. problem is as given below:

Minimize
Z= 20x+40y
Subject to the Constraints:
36x+ 6y = 108 3 marks
3x+12y = 36
20x+10y = 100 and
x,y 2 0

The problem is solved graphically below:

4 marks

(3.0) (5.0) (12,0)
4 g 12

Product’ (Linits)

For solving the above problem graphically, consider a set of rectangular axis x,y in the plane.
As each point has the coordinates of type (x, y), any point satisfying the conditions x = 0 and y
= 0 lies in the first quadrant only.

The constraints of the given problem as described earlier are plotted by treating them as
equations:

Jéx+6y = 108
3x4 12y = 36
20x+ 10y = 100

FIC 7 IC OHH
--- page 8 ---
The area beyond these lines represents the feasible region in respect of these constraints;
any point on the straight lines or in the region above these lines would satisfy the constraints.

Intersection Points:

The point of intersection for the lines
36x+6y = 108 and
20x + 10y = 100s given by Intersection Point R (2, 6)
The point of intersection for the lines
20x+ 10y = 100 and
3x+12y = 36s given by Intersection Point Q (4, 2)

The coordinates of the extreme points of the feasible region are given by

S = (0, 18)
R = (2,6)
Q = (4,2) and
P = (12,0)

The value of the objective function at each of these points can be evaluated as follows:
Extreme Co-Ordinates of the corer points of the | Value of the objective function

Point feasible region (value of x and y) Z=20x+ 40y
s (0, 18) %720 3 marks
R (2, 6) = 280
Q (4,2) 2 160
P (12, 0) 2 240

The value of the objective function is minimum at the point Q (4, 2). Hence, the optimum
solution in to purchase 4 units of product A and 2 units of product B in order to have minimum
cost of 2160.

4 marks

FIC QF EH 1
--- page 9 ---
Brief explanation of all the following steps
1. Problem formulation
2. Setting of objectives and overall project plan
3. Model conceptualization
4. Data collection
5. Model translation
6. Verification
7. Validation   4 marks
8. Experimental Design
9. Production runs and analysis
10. More runs
11. Documentation and reporting
12. Implementation
Q5
a.
7 marks
********** 9 **********
--- page 10 ---
Day Random Number (RN) RNRMatch Simulated Daily Demand

1 68 60 — 74 20
2 1 85 — 94 30
3 33 15 — 34 10
4 05 05 — 14 5

5 80 75 — 84 25
6 24 15 — 34 10
7 75 75 — 84 25
8 42 35 — 59 15
9 98 95 — 99 35
10 59 35 — 59 15 6 marks
TOTAL 190

The daily average service calls based on the simulation are calculated as:

Total Simulated Demand
Number of Days

Average Demand =

190 calls 2 k
Average Demand = ec marks

T0 days = 19 calls per day

FRR ICR 7 OI HOH
--- page 11 ---
1 mark
2 marks
2 marks
Q6.
a
4 marks
Electra's Optimal Strategy: A2 (TV Focus)
Maximin Value: 9 percentage points
********** 11 **********
--- page 12 ---
4 marks
Zenith's Optimal Strategy: B2
Minimax Value: 9 percentage points
3. Saddle Point and Value of the Game
A saddle point exists if the Maximin value equals the Minimax value.
Maximin Value (9)=Minimax Value (9)
Saddle Point: Yes, a saddle point exists at the intersection of the optimal strategies: cell (A2, B2), where the payoff is
9.
Value of the Game (V): 9 percentage points   2 marks
The game is stable in pure strategies. Electra should choose A2, and Zenith should choose B2. Electra's guaranteed
market share gain is 9 percentage points.
b.
********** 12 **********
--- page 13 ---
Vogel's Approximation Method (VAM)-

A B c Supply | Diff.
x 15 9 0 6 10/0 33
Y 21 12 6 iL 10/0 66
Zz 6 a0 18 9 10/0 3-
Demand 10/0 10/0 10/0 30
- 9 3 0
S - 3 0

The number of allocations are 3 which is less than m+n -1 i.e. 5, so it becomes a degeneracy
case. This degenerate situation will be made good by introducing two infinitesimally small
allocations ‘e:’ and ‘ez’ in independent lowest cost cells RiC3 and RsCs respectively. The initial
basic solution will be as follows-

A B c Supply
X 15 g Le 6 I 100 5 marks
Y 2 12 6 Ll t00
z 5 Le 18 9 L&I 100

Demand 10/0 10/0 10/0 30

Now we test the above initial solution for optimality.
(ui + vj) Matrix for Allocated / Unallocated Cells

ui

9 9 6 6

9 9 6 6

6 12 9 9
yj 3 3 0

Now we calculate Ajj = Cjj - (uj + vj) for non basic cells which are given in the table below-

FIR ICR 7] QI HO
--- page 14 ---
5 marks
b.
i.   Average Waiting Time in the system
3 marks
ii.   Average Number of Customers in the Queue
3 marks
iii.   Probability that the server is busy
3 marks
iv.   Probability of More Than Two Customers in the System
********** 14 **********
--- page 15 ---
Prsg = 1 — Paeg = 1— (Po + Pi + Po)
We use P,, = (1 — p)p", where 1 — p= 1 — 2/3 = 1/3.
* Po=(l-p)=3
* Pr=(1—p)e'= 3 (3) = 3

2
+ Po=(1—p)p?=3(3) —3%5-%

1 2 4
Pheo = Po+Pi+Pe==-+=-4+=—
<2 0+ Pi + Po 3+ 97

3 marks

p,-2,8,4_1
m2 907 «27 «TO

19 8
Pyasg =1-— Praeg =1- = = = = 0.296
me ne 27 (27
The probability of having more than two customers in the express lane system is approximately
29.6%.

FRR IC 7 DA HOH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper e04f5581738d

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSBS_7036/Operations Research/ANS_Operations Research(702BS0C089)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: mixed (14 pages), mean OCR confidence 78.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Operations Research
Date: 01 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question no 1 is compulsory
5. Out of remaining question, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
********** 1 **********
--- page 2 ---
(c) (5 Marks)
Activity Predecessor
A -
B A
Cc A
D B.C
E Cc
F D
G E
H F.G

1. Start 4 A (1 Mark)
2. A+ Band C (1 Mark)
3. B.C + D and C+ E (1 Mark)
4.D+FandE+G (1 Mark)
5. F,G — H (Finish) (1 Mark)

(d) (5 Marks)

Given:
D = 3600, S=36, C=10

Holding cost:
H = 0.25 x 10=2.5

(1 Mark)
EOQ formula:
. 2DSs
OV
(1 Mark)
Q'= ae) = 103680
Q* = 322 kg
(2 Marks)
Orders / year:
_ 3600
N= 3 11
(1 Mark)

FIC 2 I HH ar
--- page 3 ---
Q2

(a) (10 Marks)

Minimize:
Z = 200r + 300y
Constraints:
2e+15y>6, r+ye4, wv,y>0
(2 Marks)
Convert:
Qn+15y=6, r+y=4
Intercepts:
Constraint = x-int — y-int
2e+1.5y=6 (3,0) (0,4) (2 Marks)
a+y=4 (4.0) (0,4)
Intersection:
2x + 1.5y=6
r+y=4
Solve:
r=2, y=2

(2 Marks)
Feasible region corner points: (0,4), (2,2), (4,0) (2 Marks)

Evaluate Z:
Point Z Value

(0,4) 1200
(2.2) 1000 Min (2 Marks)
(4,0) 800

Optimal:

Zmin = 1000 at (2,2)

FOGG 2 FC IC Ir
--- page 4 ---
(b) (10 Marks)

Activity | Predecessor | Duration

A - 2
B A 3
Cc A 4
D B.C 6
E - 2
F E 8
(2 Marks)
Forward Pass (Earliest Times)
Activity | ES EF
A 0 2
B 2 5
Cc 2 6 (3 Marks)
D 6 12
E 0 2
F 2 10
Backward Pass (Latest Times)
Activity | LS LF
D 6 12
Cc 2 6
B 3. C6 (3 Marks)
A Oo 2
F 4 12
EB 2 4
Float Calculation
Activity | Float
é ; (1 Mark)
D 0
Critical Path:
A+sC+D
(1 Mark)

Project Duration:
=24+4+6 = 12 days

FIC 7) IC HOH
--- page 5 ---
Q3 (20 Marks)

(a) (10 Marks)

Step 1: Check balance
Supply = 50 + 40 + 70 = 160
Demand = 30+ 45+ 35 + 50 = 160
Balanced problem. (1 Mark)
Step 2: Initial Table
A B CD /| Supply
1 ll 20 7 8 50
2 21 16 20 12 40
3 8 12 8 9 70
Demand | 30 45 35 50

(1 Mark)
Step 3: Compute penalties
Row penalties: Rl = 8-7 =1, R2 = 16-12=4,R3=8-8=0
Column penalties: A = 11-8 = 3, B= 16-12=4,C =8-7=1,D=9-8=1

(2 Marks)
Step 4: Highest penalty = 4 (Row 2 or Column B)
Choose Row 2 + minimum cost = 12 (cell 2D)
Allocate = min(40,50) = 40
(2 Marks)
Updated table:
Demand D = 10 left
Step 5: Recompute penalties
Continue similarly...
Final Allocation:
: D
1/0 0 35 15
2};0 40 0 0
3/30 5 0 35
(3 Marks)
Step 6: Total Cost
= 35(7) + 15(8) + 40(16) + 30(8) + 5(12) + 35(9)
= 245 + 120 + 640 + 240 + 60 + 315 = 1620
(1 Mark)

Initial Basic Feasible Solution Cost = 1620

FIC DI EH ar
--- page 6 ---
(b) (10 Marks)

Given:
d= 8/hr, « = 12/hr (1 Mark)
Step 1: Current system
X 8 1
W, = ——~ = = = hh
7 iw) 124) 6
= 10 minutes (2 Marks)

L, = AW, =8 x i = 1.33

(1 Mark)
Step 2: New system
Service time = 3 min + yc = 20/hr
8 8
W, = =e = = = 0.033 hr
@~ 30712) 240 "
= 2 minutes (2 Marks)
L, =8 x 0.033 = 0.266
(1 Mark)
Step 3: Cost Analysis
Waiting cost /min/customer = 0.12 Rs
Old waiting cost /day:
= 1.33 x 10 x 60 x 0.12 = 95.76
New waiting cost:
= 0.266 x 2 x 60 x 0.12 = 3.83
(2 Marks)
Total cost comparison
Old = 95.76
New = 3.83 + 50 = 53.83
(1 Mark)

Conclusion: Install system (cost reduces)

FEC 6 FC IG Ir
--- page 7 ---
Q4 (20 Marks)
(a) (10 Marks)

Maximize:
Z =3a+2y

Constraints:

a+ dy +s; = 420
3x + 2y + sy = 460
3a + 2y + sy = 430

(2 Marks)
Initial Tableau
BV|x y sl s2 s3)RHS
sl/l 4 1 0 0} 420
s2/3 2 0 1 0} 460
33/3 2 0 0 1) 430
Z|3 2 0 0 0] 0

(2 Marks)
Iteration 1
Entering variable = x (most negative) (1 Mark)
Ratios:

420/1 = 420, 460/3 = 153, 430/3 = 143
Leaving variable = s3 (1 Mark)
Pivot - row operations (2 Marks)
Final Solution (after iterations)
a = 143.33, y = 69.17
(1 Mark)
Z = 3(143.33) + 2(69.17) = 568.33
(1 Mark)

Optimal Solution:
Zinaz = 568.33

FIC 7 IC OHH
--- page 8 ---
Q4 (b) (10 Marks)

Step 1: Check balance
Supply = 70 + 60 + 70 = 200
Demand = 80 + 30+ 50+ 40 = 200
Balanced problem. (1 Mark)
Step 2: Initial Table
D1 D2 D3 D4 | Supply
Ol 6 1 9 3 70
02 ll 5 2 8 60 (1 Mark)
03 10 12 ll 7 70
Demand | 80 30 50) 40
Step 3: NW Corner Allocation

e (O1,D1): min(70,80) = 70 (1 Mark)
e¢ Remaining D1 = 10
e (02,D1): min(60,10) = 10 (1 Mark)
e Remaining 02 = 50
e (02,D2): min(50,30) = 30 (1 Mark)
e Remaining O2 = 20
@ (02,D3): min(20,50) = 20 (1 Mark)
e Remaining D3 = 30
e (03,D3): min(70,30) = 30 (1 Mark)
e¢ Remaining O3 = 40
e (03,D4): min(40,40) = 40 (1 Mark)

Final Allocation Table
D1 D2 D3 D4

O01); 70 0 0 0

02/10 30 20 0 (1 Mark)
03/0 0 30 40
Step 4: Total Cost
= 70(6) + 10(11) + 30(5) + 20(2) + 30(11) + 40(7)
= 420 + 110 + 150 + 40 + 330 + 280 = 1330
(2 Marks)

Initial Basic Feasible Solution Cost = 1330

°

FOCI 9 FCI IC Ir
--- page 9 ---
Q5 (a) (10 Marks)

Formula:

a+4m+b 4 (“*)
t.=--, v=
6
(1 Mark)

Step 1: Compute values
Activity | a m b | t. Variance

1-2 O08 10° 1.2 | 10 0.0044

2-3 3.7 5.6 9.9 | 5.93 1.07

2-4 6.2 6.6 15.4] 8.0 2.33 (4 Marks)

3-4 21° 2.7 61 | 3.17 0.45

45 O8 34 3.6 | 3.0 0.22

5-6 09 34 27 | 25 0.09
Step 2: Paths

e 1-2-3-4-5-6 = 14 5.93 + 3.17 +34 2.5 = 15.6
@ 1-2-4-5-6 =14+8+342.5 = 14.5

(2 Marks)
Critical Path:
1-2-3-4-5-6

(1 Mark)
Expected duration:
= 15.6
(1 Mark)
Variance (CP):
o* = 0.0044 + 1.07 + 0.45 + 0.22 + 0.09 = 1.83
o = 1.35
(1 Mark)
Step 3: Probability (2 months earlier)
Target = 15.6 —2 = 13.6
Z- 13.6 — 15.6 = -148
1.35
From table:
P = 0.069
(1 Mark)

Probability = 6.9%

FEI QF IG Ir
--- page 10 ---
Q5 (b) (10 Marks)

Step 1: Cumulative distribution

Time | Probability | Cumulative
10 0.45 0.45
25 0.35 | 0.80 (2 Marks)
40 0.20 1.00
Mapping
00-44 +10
45-79 425
80-99 40 (2 Marks)

Step 2: Simulation Table
Patient | RN | Time | Start | Wait

1 35 10 0 0
2 60 | 25 25 0
3 81 40 50 10
4 90 | 40 75 15 (4 Marks)
5 72 25 100 15
6 55 25 125 15
7 45 25 150 15
8 58 25 175 15

Step 3: Results

Total waiting = 85

Average waiting:

8&5 .
=->7 10.6 minutes

(1 Mark)
Idle time occurs only initially (1 Mark)

FRR ICR 7 OI HOH
--- page 11 ---
6(a) (10 Marks)

Minimize:
Z=-2e-y
Subject to:
xrty>2
et+ys4
x.y>0

Step 1: Convert to standard form

aty-—s;+aq=
r+yt+s=

(2 Marks)
Phase I Objective:
A=a,
(1 Mark)
Initial Tableau
BV|x ysl al|RHS
al} 1 1 -1 1 2
s2}/1 1 0 0 4
Zi-l -1 1 Of] -2
Pivot operation
Entering variable = x (or y) Leaving variable = a,
After pivot, artificial variable removed.

(2 Marks)

(2 Marks)
Phase II
Solve remaining system:
Feasible region:
2<a+y<4
(1 Mark)
Optimal solution
Since Z is negative, minimize occurs at maximum (x+y)

a+y=4
Take:
x=4,y=0

(1 Mark)
Minimum value

Z = —-2(4)-0=-8
(1 Mark)

FRI ICR 7 FI OH
--- page 12 ---
(b) (10 Marks)

Since 4 tasks and 3 men — add dummy column. (2 Mark)
Step 1: Modified matrix
1 2 3 Dummy
I} 9 26 15 0
II} 13 27 6 0
| 35 20 15 0
IV} 18 30 20 0

(2 Mark)
Step 2: Row Reduction

Subtract row minimum:
I} 9 2 15 0-+ 9,26,15,0

II }13 27 6 0 -+13,27,6,0
11} 35 20 15 0 -+35,20,15,0
IV} 18 30 20 0 -+18,30,20,0
Step 3: Optimal Assignment
Assign minimum cost:
I- 1 (9)
Il + 3 (6)
III —+ 2 (20)
IV — Dummy (0)

(2 Marks)

(4 Marks)
Total Time

=9+6+20+0=35

FRR ICR] DA KH
--- page 13 ---
7(a) (10 Marks)

Given: Arrival rate: 99
A= 7 2.75 per hour

Service rate: .
60

H=55= 3 per hour
(2 Marks)
Utilization factor » 295
pan =22 =00917
Le 3
(2 Marks)
Average queue length
Dt
L. =—*_
" u(u— A)
(2.75)? 7.56
= = — = 10.08
3(3 — 2.75) 0.75
(2 Marks)
Waiting time
_ L, 1008 2.
W,= x = 375 = 3.66 hrs
(2 Marks)
Waiting cost
= 10.08 x 0.80 x 8 = 64.5
(2 Marks)

Total daily cost
= 64.5 + 40 = 104.5

FIR ICR 7] QI HO
--- page 14 ---
(b)(10 Marks)

Given:
p=50, d=25, S=100, H=0.01

(2 Marks)
EPQ formula
._ {2DS_p
a= H p-d
Take annual demand:
D = 25 x 365 = 9125
(2 Marks)
Q'= 2(9125) (100) 50
7 0.01 25
= ¥ 182500000 x 2
= V365000000 = 19105
(2 Marks)
Cycle time
—Q_ 19105 _, 7
T=7= 5 = 764 days
(1 Mark)
Production time Q 19105
: sd ARE avs
= > = 7 382 days
(1 Mark)
Maximum inventory
=Q (: - “) = 19105(0.5) = 9552
P
(1 Mark)
Minimum cost
_DS HQ (,_d
~ Q 2 p
(1 Mark)

Final Answer:
Q* =19105, Imax = 9552

FRR IC 7 I OH
````

## 2025-26 · Re-Exam · Sem 9 · Answer key · paper a940e12c440c

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_09/Re-Exam/Integrated_Computer_7032/Operations Research/ANS_Operations Research(702CO0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 64.7

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)
Year: V/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operations Research
Date: 09 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Part A is compulsory.
5. In Part B, Attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Part A. Answer the following Questions   20
Introduction & Definition (1 Mark)
• Meaning of Operations Research (scientific and quantitative
approach to decision-making).
•   Objective: optimize limited resources and improve decision quality.
2. Importance in Managerial Decision-Making- Min. 2 points (2
Marks)
•   Provides a rational, data-based framework.
• Helps in resource optimization and cost reduction.
a.
• Reduces risk and uncertainty.
• Enhances efficiency, productivity, and strategic planning.
3. Applications in Real-Life Problem-Solving- Min. 2 points (2 Marks)
•   Production management – product mix, scheduling, inventory
control.
•   Logistics – transportation and assignment problems.
• Finance – portfolio optimization
********** 1 **********
--- page 2 ---
b. Method & first step (1 mark) — Use Least-Cost Method: pick the cell
with smallest cost and allocate as much as possible.
• Smallest cost cell = W3–D2 (cost 10). Allocate min(W3 supply 20,
D2 demand 20) = 20. → W3 supply → 0, D2 → 0.
Next allocations (2 marks) — Continue with next least-cost available
cells:
• Next cheapest available = W1–D1 (cost 19). Allocate min(W1
supply 14, D1 demand 15) = 14. → W1 → 0, D1 → 1.
• Next cheapest with remaining demand = W2–D3 (cost 45) (D2 is 0,
W1 is exhausted). Allocate min(W2 supply 26, D3 demand 25) =
25. → W2 → 1, D3 → 0.
• Remaining demand D1 = 1 and remaining supply W2 = 1 → allocate
1 at W2–D1 (cost 65).
Final allocation table (display) (0.5 mark)
• W1: D1 = 14, D2 = 0, D3 = 0 (supply 14)
• W2: D1 = 1, D2 = 0, D3 = 25 (supply 26)
• W3: D1 = 0, D2 = 20, D3 = 0 (supply 20)
• Demands met: D1 = 15, D2 = 20, D3 = 25
Transportation cost calculation & result (1.5 marks) — compute cell
costs carefully:
• W1–D1: 14 × 19 = 266
• W2–D1: 1 × 65 = 65
• W2–D3: 25 × 45 = 1,125
• W3–D2: 20 × 10 = 200
• Total transportation cost = 266 + 65 + 1,125 + 200 = 1,656
c. Let A play 𝐴1with probability 𝑝(so 𝐴2with 1 −𝑝). Let B play 𝐵1with
probability 𝑞(so 𝐵3with 1 −𝑞). The payoff is to player A (zero-sum).
Make B indifferent (find 𝑝) — equate A's payoff when B chooses 𝐵1and
𝐵3:
𝑝(1) + (1 −𝑝)(−0.5) = 1.5𝑝−0.5
𝑝(−0.5) + (1 −𝑝)(0) = −0.5𝑝
• Solve 1.5𝑝−0.5 = −0.5𝑝⇒2𝑝= 0.5 ⇒𝑝= 0.25.
• So A plays 𝐴1with 0.25, 𝐴2with 0.75. (1.5 marks)
Make A indifferent (find 𝑞) — equate the expected payoff of 𝐴1and
𝐴2against B's mix:
𝑞(1) + (1 −𝑞)(−0.5) = 1.5𝑞−0.5
• 𝑞(−0.5) + (1 −𝑞)(0) = −0.5𝑞
• Solve 1.5𝑞−0.5 = −0.5𝑞⇒2𝑞= 0.5 ⇒𝑞= 0.25.
• So B plays 𝐵1with 0.25, 𝐵3with 0.75. (1.5 marks)
Value of the game 𝑉— plug either indifferent expression (they are equal):
********** 2 **********
--- page 3 ---
• 𝑉= 1.5𝑝−0.5 = 1.5(0.25) −0.5 = 0.375 −0.5 = −0.125.
• So value 𝑉= −0.125(i.e. − 1 8), meaning A's expected payoff is
−0.125(B's expected gain = +0.125). (1 mark)
Is the game fair?
• No. A fair zero-sum game has value 0. Here, V equals -0.125, not
equal to 0, so the game is not fair (advantage to B). (1 mark)
d. 1. Introduction (1 mark)
•   Simulation is a technique for imitating real-life systems to analyze
performance under varying conditions without real-world risk or
cost.
•   Useful where analytical solutions are complex or impractical.
2. In Inventory Management- Any two points (2 marks)
• Helps determine optimal inventory levels under uncertain demand
and lead time.
•   Simulates stock-outs, reorder points, and safety stock policies.
•   Evaluates the impact of demand variability, supplier delays, and
holding costs.
• Aids in policy comparison (e.g., EOQ vs. periodic review).
• Example: Simulating seasonal demand to decide reorder points for
a retail chain.
3. In Job Sequencing- Any two points (2 marks)
•   Simulates production scheduling and machine utilization under
different job order sequences.
•   Evaluates waiting times, idle time, and throughput for different
sequencing rules (e.g., FCFS, SPT, LPT).
•   Identifies the sequence minimizing total processing time or delay.
•   Useful in flexible manufacturing systems with random job arrivals.
Part B. (Attempt Any 4)   80
1   20
a.   Convert to standard form (add slack variables 𝒔𝟏, 𝒔𝟐, 𝒔𝟑) –(02 marks)
3𝑥1 + 3𝑥2 + 0𝑥3 + 𝑠1 = 22
𝑥1 + 2𝑥2 + 3𝑥3 + 𝑠2 = 14
3𝑥1 + 2𝑥2 + 0𝑥3 + 𝑠3 = 14
Objective: maximize 𝑍= 𝑥1 + 4𝑥2 + 5𝑥3.
Initial basic variables: 𝑠1 = 22,  𝑠2 = 14,  𝑠3 = 14. Initial 𝑍= 0.
Iteration 1 (3 marks)
(Columns order: 𝑥1  𝑥2  𝑥3  𝑠1  𝑠2  𝑠3     ∣RHS)
********** 3 **********
--- page 4 ---
Iteration-1 c; |1)4) 5 |o}ojo

MinRatio
B Cg] Xp |x /x2| x3 | $1| 82/83 AR

X3
8; |o}] 2 }3]/3] 0 J/ifoja —

14
Sy 0 14 1);2/ @ |0)1/0|=— =4 6667 —

3
83 0 14 3.) 2 0 o;oj}1 ---
zZ=0 Zj 0|;0 0 0;0);0
Z)-C;|-1|-4|-57 | 0] 0] 0
Iteration 2 (3 marks)
Iteration-2 G 1 4 5/0 0 |o
MinRatio
B Cg Xp | om xy |xy/Sy| Sy |S3) XB
x2
22
Sy o| 22 3 3 O}1} 0 | 0|> =7.3333
4.6667
x3 5 | 4.6667 |0.3333| 0.6667 | 1 | 0 |0.3333| 0 | —— =7
0.6667
14
S3 o| 14 3 @ jojo} o j1| 5-75
Z = 23.3333 Z; | 1.6667) 3.3333 | 5 | 0 | 1.6667 0

J
Z;~ C; | 0.6667 | -0.6667 t | 0 | 0 | 1.6667] 0

Iteration 3 (3 marks)

Iteration-3 Cc 1 |4/5/0] 0 0

B Cal Xg Xp | X2/x3/S]) Sy S3 | MinRatio

Sy 0 1 -15 |/0/0)/1 0 -15

x3 5 0 | -0.6667| 0 | 1 | 0 | 0.3333 | -0.3333

x2 4 7 1.5 1/0) 0 0 05

Z=28 Zj | 2.6667 | 4 | 5 | 0 | 1.6667) 0.3333

Z;- Cj) 1.6667 | 0 | 0 | 0 | 1.6667 | 0.3333

Final answer (1 mark)
Optimal solution: x, = 0, x2 = 7, x3 = 0.
Maximum value: Zax = 28.

FIC 7) IC HOH
--- page 5 ---
b.   Step-by-Step Network Diagram (04 marks)
Strategies to reduce project duration- Any two points (04 marks)
• Invest Additional Resources: Allocate extra funding to hire more
staff, authorize overtime, or use high-speed equipment to shorten the
duration of critical path tasks.
•   Prioritize Least Cost Crashing: Select the critical activity that
provides the largest reduction in time for the lowest additional cost,
then analyze the cost/time trade-off iteratively.
• Monitor for New Critical Paths: After crashing one path, recalculate
the project schedule immediately, as another path may become the
longest, requiring subsequent crashing efforts to focus on all current
critical paths.
2   20
a.   The initial feasible solution is: (4 marks)
Supp
D1   D2   D3   D4   Row Penalty
ly
S1   8   6(40) 19(10) 9   50   2 | 3 | 13 | 19 | -- | -- |
S2   9   7   4(20)   2(40) 60   2 | 2 | 3 | 4 | 4 | -- |
S3   3(30) 4   2(20)   5   50   1 | 2 | 2 | 2 | 2 | 2 |
Dem
30   40   50   40
and
Colu 5   2   2   3
mn   --   2   2   3
Pena --   2   2   --
lty   --   --   2   --
********** 5 **********
--- page 6 ---
--   --   2   --
--   --   2   --
The transportation cost =6×40+19×10+4×20+2×40+3×30+2×20=720
(01 mark)
Here, the number of allocated cells = 6 is equal to m + n - 1 = 3 + 4 - 1 = 6
∴ This solution is non-degenerate. (01 mark)
MODI method finding u and v: (02 marks)
D2   D3   D4   Supply   ui
D1
S1   8   6 (40)   19 (10) 9   50 u1=19
S2   9   7   4 (20)   2 (40)   60 u2=4
S3   3 (30) 4   2 (20)   5   50 u3=2
Demand   30   40   50   40
vj   v1=1   v2=-13 v3=0   v4=-2
Finding dij (03 marks)
D2   D3   D4   Supply   ui
D1
S1   8 [-12] 6 (40) 19 (10) 9 [-8] 50   u1=19
S2   9 [4]   7 [16] 4 (20)   2 (40) 60   u2=4
S3   3 (30)   4 [15] 2 (20)   5 [5]   50   u3=2
Demand   30   40   50   40
vj   v1=1   v2=-13 v3=0   v4=-2
The current solution is not optimal. (01 mark)
********** 6 **********
--- page 7 ---
b.   Network Diagram (2 marks) - Students can draw a diagram using the   mar
AOA method.
Table showing the timings (4 marks)
Activit ES EF LS LF   Float   Critical?
y   (LF -
EF)
A   0   2   0   2   0   Yes
B   2   6   2   6   0   Yes
C   2   5   3   6   1   No
D   6   11   6   11   0   Yes
E   5   7   9   11   4   No
F   11   12   11   12   0   Yes
Critical Path- A-B-D-F, Project Duration: 12 days (02 marks)
3   20
a.   Check for saddle point: (03 marks)
Maximin Value=max(1,2,0,2)=2
Minimax Value=min(5,3,4,3)=3
No pure-strategy, as a saddle point does not exist in this game. The
optimal solution will involve a combination of mixed strategies.
After applying the dominance principle, the reduced matrix is:
(05 marks for applying dominance) Step marks to be given for
demonstrating row/column dominance.
Step 1: Let probabilities (01 mark)
•   Let x = probability that Player A plays A2 → A4 = 1−x
•   Let y = probability that Player B plays B2 → B4 = 1−y
•   Let V = value of the game (expected payoff to Player A)
3x+2(1−x) = 2x+3(1−x)=V
Player A plays A2 with 0.5 and A4 with 0.5. (1 mark)
Similarly, Player B plays B2 with a probability of 0.5 and B4 with a
probability of 0.5. (1 mark)
Value of the game is: ₹250 per game in favor of Player A. (1 mark)
********** 7 **********
--- page 8 ---
b.   The step-by-step sequence construction: (04 marks for steps)
• Step 1: Shortest is (J5 on WS1). Sequence: [J5,
• Step 2: Shortest is (J2 on WS2). Sequence: [J5, , J2]
• Step 3: Shortest is (J3 on WS1). Sequence: [J5, J3, , J2]
• Step 4: Shortest is (J1 on WS1 or J4 on WS2 or J6 on WS1/WS2).
Let's pick J1 (WS1). Sequence: [J5, J3, J1, , J2]
• Step 5: Shortest is (J4 on WS2). Sequence: [J5, J3, J1, , J4, J2]
• Step 6: The Remaining is J6. Sequence: [J5, J3, J1, J6, J4, J2]
The Optimal Job Sequence is:
J5→J3→J1→J6→J4→J2
Following Table (03 marks)
Job WS1   WS2   WS1 In WS1 Out WS2 In   WS2 Out
Time   Time (t2)   (hrs)   (hrs)   (hrs)   (hrs)
(t1)
J5   2   3   0   2   max(2,0)   2+3=5
=2
J3   3   6   2   5   max(5,5)   5+6=11
=5
J1   4   5   5   9   max(9,11 11+5=16
)=11
J6   4   5   9   13   max(13,1 16+5=21
6)=16
J4   5   4   13   18   max(18,2 21+4=25
1)=21
J2   6   2   18   24   max(24,2 25+2=27
5)=25
The total minimum completion time for the sequence is 27 hours. (01 mark)
4   20
********** 8 **********
--- page 9 ---
a.   Problem formulation: (02 marks)
Step 1: Define decision variables
𝑥1 = kg of raw material R1
𝑥2 = kg of raw material R2
Objective: Minimize cost
Minimize 𝑍= 5𝑥1 + 4𝑥2
Step 2: Formulate constraints
Nutritional requirements:
Protein ≥ 18 units
3𝑥1 + 2𝑥2 ≥18
Fiber ≥ 10 units
1𝑥1 + 2𝑥2 ≥10
Non-negativity:
𝑥1, 𝑥2 ≥0
Convert to standard form: (01 mark)
3𝑥1 + 2𝑥2 −𝑠1 + 𝑎1 = 18
𝑥1 + 2𝑥2 −𝑠2 + 𝑎2 = 10
Maximize Z=-5x1-4x2-Ma1-Ma2 (converted to max. problem)
Iteration 1 (02 marks)
Cj   -5   -4   0   0 -M -M
B   CB XB   x1   x2   S1 S2 A1 A2 MinRatio
A1   -M 18   3   2   -1 0   1   0   18/2=9
A2   -M 10   1   (2)   0   -1 0   1   10/2=5→
Z=-28M   Zj   -4M -4M M M -M -M
Cj-Zj 4M-5 4M-4↑ -M -M 0   0
Iteration-2 (3 marks)
Iteration-2   Cj   -5   -4 0   0   -M
B   CB XB   x1   x2 S1 S2   A1 MinRatio
A1   -M 8   (2)   0   -1 1   1   8/2=4→
x2   -4 5   1/2   1 0   -1/2   0   5/1/2=10
Z=-8M-20   Zj   -2M-2   -4 M -M+2 -M
Cj-Zj 2M-3↑ 0 -M M-2   0
Iteration-3 (3 marks)
Cj   -5   -4 0   0
B   CB XB   x1 x2 S1   S2   MinRatio
x1   -5   4   1   0   -1/2   1/2
x2   -4   3   0   1   1/4   -3/4
Z=-32   Zj   -5   -4   3/2   /12
Cj-Zj   0   0   -3/2   -1/2
The optimal solution is arrived with the value of variables as:
x1=4, x2=3, Max Z=-32 (01 mark)
********** 9 **********
--- page 10 ---
b.   Convert to Minimization Problem (Maximization): (02 marks)
The Hungarian Algorithm minimizes cost. To maximize profit, we convert
the profit matrix into a regret matrix by subtracting every element from
the largest element in the entire matrix. The largest element in the given
profit matrix is 9.
R1   R2   R3   R4
S1   1   3   4   0
S2   2   1   3   2
S3   3   2   1   4
S4   0   4   2   1
Row reduction: (01 mark)
R1   R2   R3   R4
S1   1   3   4   0
S2   1   0   2   1
S3   2   1   0   3
S4   0   4   2   1
Column reduction: (01 mark)
R1   R2   R3   R4
S1   1   3   4   0
S2   1   0   2   1
S3   2   1   0   3
S4   0   4   2   1
Assignment (Zero covering) (02 marks)
Assign zeros such that one per row and column.
Look at zeros:
• S1: R4=0
• S2: R2=0
• S3: R3=0
• S4: R1=0
• Optimal assignment (01 mark)
Salesperson   Region
S1   R4
S2   R2
S3   R3
S4   R1
• Maximum total profit: ₹3,40,000 (01 mark)
5   20
a.   Iteration 1 (02 marks)
********** 10 **********
--- page 11 ---
Cj   3   2   0   0
CB   B   X1   X2   S1   S2   RHS
2   X2   0   1   0.6667   -0.3333   0.6667
3   X1   1   0   -0.3333   0.6667   5.6667
Zj   3   2   0.3333   1.3333   Z=18.3333
Cj-Zj   0   0   -0.3333   -1.3333
Since all Cj-Zj≤0
Hence, a non-integer optimal solution is arrived at with the value of
variables as:
x1=5.6667, x2=0.6667
Max Z=18.3333
To obtain the integer-valued solution, we proceed to construct Gomory's
fractional cut, with the help of the x1-row, as follows: (02 marks)
5.6667=1x1-0.3333S1+0.6667S2
(5+0.6667)=(1+0)x1+(-1+0.6667)S1+(0+0.6667)S2
The fractional cut will become
-0.6667=Sg1-0.6667S1-0.6667S2→ (Cut-1) (01 mark)
Adding this additional constraint at the bottom of the optimal simplex
table.
The new table so obtained is: (03 marks)
Cj   3   2   0   0   0
C
B   x1   x2   S1   S2   Sg1   RHS
B
2   x2   0   1   0.6667 -0.333   0   0.6667
3   x1   1   0   -0.333   0.667   0   5.6667
0   Sg1   0   0   (-0.67) -0.667   1   -0.6667
Zj   3   2   0.33   1.333   0   Z=18.33
-   -
Cj-Zj   0   0   0
0.3333 1.3333
Ratio=Cj-
Zj/ Sg1,j   ---   ---   0.5↑   2   ---
and Sg1,j<0
Minimum negative XB is -0.6667, and its row index is 3. So, the leaving
basis variable is Sg1.
The minimum positive ratio is 0.5, and its column index is 3. So, the
entering variable is S1.
∴ The pivot element is -0.6667.
Entering =S1, Departing =Sg1, Key Element =-0.6667
Iteration 3 : (03 marks)
********** 11 **********
--- page 12 ---
Cj   3   2   0   0   0
CB   B   x1   x2   S1   S2   Sg1   RHS
2   x2   0   1   0   -1   1   0
3   x1   1   0   0   1   -0.5   6
0   S1   0   0   1   1   -1.5   1
Zj   3   2   0   1   0.5   Z=18
Cj-Zj   0   0   0   -1   -0.5
Ratio   ---   ---   ---   ---   ---
Since all Cj-Zj≤0
Hence, an integer optimal solution is arrived with the value of variables
as: x1=6, x2=0, Max Z=18 (01 mark)
b.   Table as follows: (04 marks)
Earliest and Latest time (04 marks)
********** 12 **********
--- page 13 ---
6   20
a.   A sensitivity report provides insights about how changes in the parameters
of a linear programming (LP) problem affect the optimal solution. Key
information includes: (Any two points- 02 marks)
• Optimal values of decision variables – indicate which variables are
active in the optimal solution.
• Optimal value of the objective function – the maximum profit or
minimum cost.
• Shadow prices (dual values) – show how much the objective
function would improve per unit increase in a resource (constraint
RHS).
• Allowable increase/decrease in objective function coefficients –
range within which the current optimal solution remains optimal if
the profit or cost per unit changes.
********** 13 **********
--- page 14 ---
• Allowable increase/decrease in resource availability – indicates
the range of RHS changes where shadow prices remain valid.
Managerial Significance of Allowable Increase/Decrease-Any two
points (02 marks)
• Helps managers understand how much profit/cost per unit can
change before the current production plan becomes suboptimal.
• Enables pricing, sourcing, or cost reduction decisions.
• Shadow prices and allowable changes guide resource allocation
decisions.
• Managers can see how much adding or removing resources impacts
profit or cost.
• Helps in capacity planning and investment decisions.
Dual formulation (04 marks)
Max W=10Y1+35Y2+10Y3
• Dual constraints: Coefficients of X1 and X2 in primal become
constraints in dual:
1. For X1: 2𝑌1 + 1𝑌2 + 1𝑌3 ≤1
2. For X2: 4𝑌1 −1𝑌2 ≤2
• Dual variable signs:
o 𝑌1 ≥0
o 𝑌2 is unrestricted
o 𝑌3 ≥0(for X1 ≥10 bound, optional)
********** 14 **********
--- page 15 ---
b.   Find LP relaxation optimum using graphical method (03 marks): 𝑋1 =
8, 𝑋2 = 2.25, 𝑍= 35.25(fractional, need integer)
Step 2: Branching (01 mark)
•   Since 𝑋2 = 2.25 fractional → branch:
1. Branch 1: 𝑋2 ≤2
2. Branch 2: 𝑋2 ≥3
Step 3: Solve Branch 1 (𝑿𝟐≤𝟐) (01 mark)
• Maximize 𝑍= 3𝑋1 + 5𝑋2with constraints:
1. 2𝑋1 + 4𝑋2 ≤25→ 𝑋1 ≤(25 −4𝑋2)/2
2. 𝑋1 ≤8
3. 𝑋2 ≤2
• Try largest X2 = 2 → 𝑋1 ≤(25 −8)/2 = 17/2 = 8.5→ integer
max 𝑋1 = 8
•   Solution: 𝑋1 = 8, 𝑋2 = 2
• Z = 38 +52 = 24 +10 = 34
Step 4: Solve Branch 2 (𝑿𝟐≥𝟑) (01 mark)
• Max X2 = 5, X1 ≤ 8, and 2𝑋1 + 4𝑋2 ≤25→ 2X1 + 12 ≤25 → X1
≤ 6.5 → integer max X1=6
•   Possible integer pairs: (X1,X2) = (6,3), (5,3), (4,3), (0,3),
(0,4),(0,5), etc
• Compute Z: Best Z = 33 → less than branch 1
Step 5: Determine Optimal Integer Solution (02 marks)
• Compare feasible integer solutions from both branches:
• Branch 1: Z = 34 at (X1, X2) = (8,2)
• Branch 2: Z = 33 at (6,3)
Optimal integer solution: (01 mark)
𝑋1 = 8, 𝑋2 = 2, 𝑍max = 34
c.   Concept (02 marks)
• Degeneracy occurs when the number of occupied cells in a basic
feasible solution (BFS) is less than 𝑚+ 𝑛−1, where 𝑚= number
of rows (sources) and 𝑛= number of columns (destinations).
•   In other words, there are fewer allocations than required for a non-
degenerate BFS.
Impact on Optimal Solution: (01 mark for any one point)
• May lead to incorrect calculation of stepping-stone or MODI method
potentials.
• Can cause cycling or multiple iterations without improvement.
• Makes it difficult to identify the next entering variable, delaying
convergence.
Handling Degeneracy: (02 marks)
•   Introduce a very small quantity (ε) in an empty cell to temporarily
occupy it.
• Ensures the BFS has exactly 𝑚+ 𝑛−1allocations.
********** 15 **********
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper 464490a48c8b

- Departments: Computer Engineering
- Programmes: BTech Computer 7002, Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/BTech_Computer_7002/Operations Research/ANS_Operations Research(702CO0E003)_2024-2025.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Operations Research
Date: 02 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Part A is compulsory.
5. In Part B, Attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Part A. Answer the following Questions   20
a. Steps in Operations Research Approach: (3 marks)
1. Problem Definition: Clearly identify the objective, constraints, and
scope of the problem. (1 mark)
2. Model Formulation: Develop a mathematical or logical model
representing the real-world problem. (0.5 mark)
3. Model Solution: Apply suitable OR techniques (e.g., Linear
Programming, Queuing Theory) to obtain optimal solutions. (0.5
mark)
4. Validation and Testing: Check the model’s accuracy and relevance
through real-life data comparison. (0.5 mark)
5. Implementation and Monitoring: Apply the solution practically and
monitor performance for continuous improvement. (0.5 mark)
Importance of Model Formulation: (2 marks): Any other relevant point(s).
   It translates a real-world situation into a structured, analyzable form,
ensuring the problem is well-defined. (1 mark)
   Errors in this stage lead to misleading or impractical solutions,
making it the most crucial phase in the OR process. (1 mark)
b. The number of rows = 3 and columns = 3
A   B   C
J1   12   6   9
J2   10   17   5
J3   11   14   16
********** 1 **********
--- page 2 ---
Step-1: Find out row's minimum element and subtract it from that row (2
marks)
A   B   C
J1   6   0   3
J2   5   12   0
J3   0   3   5
Step-2: Find out the column's minimum element and subtract it from that
column. (1 mark)
1   2   3
A   6   0   3
B   5   12   0
C   0   3   5
Step-3: Make an assignment in the opportunity cost table (1 mark)
Optimal solution with correct cost (1 mark)
1   2   3
Work   Job   Cost
A   6   [0] 3
A   2   6
B   5   12   [0]
C   [0] 3   5   B   3   5
C   1   11
Total   22
c. 1. Compute row minima (worst payoff for Union for each row)
(1 mark):
   UI: min(7,12,5,8)=5
   UII: min(6,4,3,2)=2
   UIII: min(9,9,9,9)=9
 UIV: min(0,1,−1,2)=−1
Maximin=max {5, 2, 9,−1}=9. (0.5 mark):
Compute column maxima (worst payoff to Company, i.e., best for
Union in each column) (1 mark):
   CI: max(7,6,9,0)=9
   CII: max(12,4,9,1)=12
   CIII: max(5,3,9,−1)=9
 CIV: max(8,2,9,2)=9
********** 2 **********
--- page 3 ---
Minimax =min {9, 12, 9, 9}=9. (0.5 mark)
Maximin = Minimax = 9, so a saddle point exists and the value of the game
is 9. (1 mark):
Therefore, at equilibrium: Union → UIII; Company → any of CI, CIII
,CIV. Value = 9 (payoff to Union). (1 mark)
d.    Collect/assume demand distribution: Determine possible daily
demand values and their probabilities (from historical data or
assumptions). (0.5 marks)
 Build cumulative distribution (CDF): Compute cumulative
probabilities for the discrete demand values. (0.5 marks)
 Generate random numbers: Each simulated day, draw a uniform
random number u∈[0,1). (0.5 marks)
 Map to demand (inverse transform): Find the smallest demand
value whose CDF ≥ u; assign that demand for the day. (0.5 marks)
 Repeat & analyze: Repeat for the required number of days, then
compute average demand, variance, etc.(1 mark)
Brief worked example / intermediate steps (demonstrates the method) (2
marks)
Marks can be allotted if the answer aligns with the above steps.
Part B. (Attempt Any 4)   80
1   20
a. After introducing slack variables
Converting to canonical form: (01 mark)
Max Z =6X1+2X2+0S1+0S2+0S3
subject to
2X1+X2+S1= 1000
X1+S2 =400
X2+S3 =700
and X1, X2,S1, S2,S3≥0
Iteration-1 (03 marks)
Cj   6   2   0   0   0
B   CB   XB   X1   X2   S1   S2   S   MinRatio
3
S1   0   1000   2   1   1   0   0   1000/2=500
S2   0   400   (1)   0   0   1   0   400/1=400
→
S3   0   700   0   1   0   0   1   ---
Z=0   Zj   0   0   0   0   0
Cj-Zj   6↑   2   0   0   0
********** 3 **********
--- page 4 ---
Positive maximum Cj-Zj is 6 and its column index is 1. So, the entering
variable is X1.
Minimum ratio is 400 and its row index is 2. So, the leaving basis variable
is S2.∴ The pivot element is 1. Entering =X1, Departing =S2
Iteration-2 (03 marks)
Cj   6   2   0   0   0
B CB XB   X1   X2   S1   S2   S3   MinRatio
200/1=200
S1   0   200   0   (1)   1   -2   0
→
X1   6   400   1   0   0   1   0   ---
S3   0   700   0   1   0   0   1   700/1=700
Z=2
Zj   6   0   0   6   0
400
Cj-Zj   0   2↑   0   -6   0
Positive maximum Cj-Zj is 2 and its column index is 2. So, the entering
variable is X2. Minimum ratio is 200 and its row index is 1. So, the leaving
basis variable is S1. ∴ The pivot element is 1.
Iteration-3 (04 marks)
Cj   6   2   0   0   0
B   CB   XB   X1   X2   S1   S2   S3   Min
Ratio
X2   2   200   0   1   1   -2   0
X1   6   400   1   0   0   1   0
S3   0   500   0   0   -1   2   1
Z=28   Zj   6   2   2   2   0
00
Cj-Zj   0   0   -2   -2   0
Since all Cj-Zj≤0, Hence, optimal solution is arrived with value of
variables as : X1=400,X2=200, Max Z=2800: Final solution (01 mark)
********** 4 **********
--- page 5 ---
b.
The network diagram is as follows:
Correct Diagram (05 marks). Partial marks can be given based on the
completion.
   Identifying the primary factor: Cost vs. Benefit. (1 Mark)
 Explaining Critical Path impact (must be on the critical path and
check for new critical paths. (1 Mark)
 Mentioning   Resource   Availability   and/or   Technical
Feasibility/Quality limits. (1 Mark)
2   20
a. The total supply is 30+40+30=100. The total demand is 20+50+30=100.
Since total supply equals total demand, the problem is balanced.
Initial Basic feasible solution including cost calculation: (04 marks)
D1   D2   D3   Supply
S1   4   6   8 (30)   30
S2   2 (20)   5 (20)   7   40
S3   3   4 (30)   6   30
Demand   20   50   30
The minimum total transportation cost =8×30+2×20+5×20+4×30=500
Here, the number of allocated cells = 4, which is one less than to m + n - 1
= 3 + 3 - 1 = 5. ∴ This solution is degenerate (01 mark)
To resolve degeneracy, the quantity d is assigned to S1D1, which has the
minimum transportation cost = 4. (02 marks)
D1   D2   D3   Supply
S1   4 (d)   6   8 (30)   30
S2   2 (20)   5 (20)   7   40
S3   3   4 (30)   6   30
Demand   20   50   30
********** 5 **********
--- page 6 ---
Iteration-1 of optimality test (02 marks)
D2   D3   Supply   ui
D1
S1   4 (d)   6   8 (30)   30 u1=0
S2   2 (20)   5 (20)   7   40 u2=-2
S3   3   4 (30)   6   30 u3=-3
Demand   20   50   30
vj   v1=4   v2=7   v3=8
Find dij for all unoccupied cells(i,j), where dij=cij-(ui+vj) (02 marks)
D2   D3   Supply   ui
D1
S1   4 (d)   6 [-1]   8 (30)   30 u1=0
S2   2 (20)   5 (20)   7 [1]   40 u2=-2
S3   3 [2]   4 (30)   6 [1]   30 u3=-3
Demand   20   50   30
vj   v1=4   v2=7   v3=8
Since there is a negative dij, the current solution is not optimal.(01 marks)
b. Network diagram (02 marks)
Critical Path and Minimum Project Duration (04 marks)
 The critical path is the longest path from the start (Event 1) to the
finish (Event 6).
Path   Activities   Duration Calculation   Path Duration
P1   1→2→3→5→6   2(A)+3(B)+4(D)+1(F)   10 days
P2   1→2→4→5→6   2(A)+2(C)+1(E)+1(F)   6 days
   Critical Path: 1→2→3→5→6
 Minimum Project Duration: 10 days
Slack calculation (02 marks)
Event (j)   Earliest Start   Latest Finish   Slack (Lj−Ej)
(Ej)   (Lj)
1   0   0   0
2   2   2   0
3   5   5   0
4   4   8   4
5   9   9   0
6   10   10   0
3   20
********** 6 **********
--- page 7 ---
a. The solution should demonstrate calculation of Maximin and Minimax
value. Since Maximin Value (2) ≠ Minimax Value (3), no pure strategy
saddle point exists. The game must be solved using mixed strategies.
(03 marks).
Performing row dominance and column dominance and finding reduced
matrix as follows: (04 marks)
T2   T3
S2   2   3
S4   4   2
Let probabilities (1 mark)
   Let Player A play:
o S2 with probability x
o S4 with probability 1−x
   Let Player B play:
o T2 with probability y
o T3 with probability 1−y
If T2 strategy is chosen by Player B: 2x+4(1−x)=2x+4−4x=4−2x= Value
of the game.
If T3 strategy is chosen: 3x+2(1−x)=3x+2−2x=2+x = Value of the game.
Equating both we get, x= 2/3 and 1-x= 1/3. (02 marks)
Similarly we can get:
y=1/3
1-y =2/3, V = 8 / 3 (02 marks)
b. Applying the rules and showing the steps: (03 marks)
 Jobs whose minimum is on X are scheduled as early as possible in
increasing X: D(2), A(3), C(5) → D, A, C
 Jobs whose minimum is on Y are scheduled as late as possible in
decreasing Y (i.e. reverse order by Y): B (4), E(3) → placed as B,
E at the end but reversed ordering gives B before E.
Finding correct optimal sequence: (1 mark)
 D — A — C — B — E
Table (03 marks)
********** 7 **********
--- page 8 ---
Job   start on   finish on X   start on Y finish on Y
X
D   0   2   2   7
A   2   5   7   14
C   5   10   14   20
B   10   18   20   24
E   18   24   24   27
Makespan (total duration to finish all jobs) = 27 hours. (01 mark)
4   20
a. Convert to equalities (01 mark)
Maximize Z=40X1+50X2+0S1+0S2+0S3−MA1
Constraints (Equality Form):
1. 2X1+X2+s1=100
2. X1+2X2+s2=80
3. X1−s3+A1=10
4. X1, X2,S1,S2,S3,A1≥0
Iteration-1-( 02 marks)
Cj   40   50   0   0   0   -M
B CB XB   x1   x2   S1   S2   S3   A1   MinRatio
S1   0   100   2   1   1   0   0   0   100/2=50
S2   0   80   1   2   0   1   0   0   80/1=80
A1   -M   10   (1)   0   0   0   -1   1   10/1=10
→
Z=-10M Zj   -M   0   0   0 M   -M
Cj- M+   50   0   0   -M   0
Zj   40↑
Iteration-2-(03 marks)
Cj   40   50   0   0   0
B   CB   XB   x1   x2   S1   S2   S3   MinRatio
S1   0   80   0   1   1   0   2   80/1=80
S2   0   70   0   (2)   0   1   1   70/2=35→
x1   40   10   1   0   0   0   -1   ---
Z=40   Zj   40   0   0   0   -40
0
Cj-Zj   0   50↑   0   0   40
********** 8 **********
--- page 9 ---
Iteration-3-(03 marks)
Cj   40   50   0   0   0
B C XB   x1   x2   S1   S2   S3   MinRatio
B
S1   0   45   0   0   1   -0.5   (1.5)   45/1.5=30→
x2   5   35   0   1   0   0.5   0.5   35/0.5=70
0
x1   4   10   1   0   0   0   -1   ---
0
Z=2150   Zj   40   50   0   25   -15
Cj-Zj   0   0   0   -25   15↑
Iteration-4-(02 marks)
Cj   40   50   0   0   0
MinR
B   CB   XB   x1   x2   S1   S2   S3
atio
S3   0   30   0   0   0.6667   -0.333   1
x2   50   20   0   1   -0.3333 0.6667   0
-
x1   40   40   1   0   0.6667   0
0.3333
Z=2600   Zj   40   50   10   20   0
Cj-Zj   0   0   -10   -20   0
Since all Cj-Zj≤0
Hence, optimal solution is arrived with value of variables as   :
x1=40, x2=20 Max Z=2600 (01 mark)
********** 9 **********
--- page 10 ---
b. Row reduction (2 mark)
Row   J1   J2   J3   J4   J5
M1   9−6=3 ∞   7−6=1   6−6=0   8−6=2
M2   ∞   8−5=3   5−5=0 ∞   7−5=2
M3   6−6=0   7−6=1 ∞   8−6=2 ∞
M4   5−5=0   6−5=1   8−5=3 ∞   9−5=4
M5   7−5=2 ∞   6−5=1   9−5=4   5−5=0
Column reduction (1 mark)
J1   J2   J3   J4   J5
M1   3   ∞   1   0   2
M2   ∞   2   0   ∞   2
M3   0   0   ∞   2   ∞
M4   0   0   3   ∞   4
M5   2   ∞   1   4   0
Row-wise & column-wise assignment shown in table (2 mark)
J1   J2   J3   J4   J5
M1   3   ∞   1   [0]   2
M2   ∞   2   [0]   ∞   2
M3   [0]   0   ∞   2   ∞
M4   0   [0]   3   ∞   4
M5   2   ∞   1   4   [0]
Optimal solution (1 mark)
Work   Job   Cost
M1   J4   6
M2   J3   5
M3   J1   6
M4   J2   6
M5   J5   5
Total   28
Alternate Optimal assignments (1 mark)
J1   J2   J3   J4   J5
M1   3   ∞   1   [0]   2
M2   ∞   2   [0]   ∞   2
M3   0   [0]   ∞   2   ∞
M4   [0]   0   3   ∞   4
M5   2   ∞   1   4   [0]
Optimal solution ( 1 mark)
Work   Job   Cost
M1   J4   6
M2   J3   5
M3   J2   7
M4   J1   5
M5   J5   5
Total   28
********** 10 **********
--- page 11 ---
5   20
a.   The simplex method solution given is
Iteration 1 (01 mark):
2   1   0   0
CB   B   x1   x2   S1   S2   XB
2   x1   1   0.6667   0.3333   0   1.6667
0   S2   0   0.3333   -0.3333   1   0.3333
2   1.3333   0.6667   0   Z=3.33
0   -0.3333   -0.6667   0
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables
as:
x1=1.67,x2=0
Max Z=3.33
To obtain the integer valued solution, we proceed to construct Gomory's
fractional cut, with the help of x1-row as follows: (01 mark):
1.6667=1x1+0.6667x2+0.3333S1
(1+0.6667)=(1+0)x1+(0+0.6667)x2+(0+0.3333)S1
The fractional cut will become
Sg1-0.6667x2-0.3333S1=-0.6667 → (Cut-1) (02 marks):
Adding this additional constraint at the bottom of optimal simplex table.
The new table so obtained is:
Iteration 2 (03 marks)
2   1   0   0   0
CB B   x1   x2   S1   S2   Sg1 RHS
2   x1   1   0.6667   0.3333   0   0   1.6667
0   S2   0   0.3333   -0.3333   1   0   0.3333
0   Sg1 0   (-0.6667)   -0.3333   0   1   -0.6667
2   1.3333   0.6667   0   0   Z=3.3333
0   -0.3333   -0.6667   0   0
---   0.5↑   2   ---   ---
Minimum negative XB is -0.6667 and its row index is 3. So, the leaving
basis variable is Sg1.
Minimum positive ratio is 0.5 and its column index is 2. So, the
entering variable is x2, ∴ The pivot element is -0.6667.
Entering =x2, Departing =Sg1, Key Element =-0.6667 (01 mark):
Iteration 3 (03 marks)
2   1   0   0   0
********** 11 **********
--- page 12 ---
CB   B   x1   x2   S1   S2   Sg1   RHS
2   x1   1   0   0   0   1   1
0   S2   0   0   -0.5   1   0.5   0
1   x2   0   1   0.5   0   -1.5   1
2   1   0.5   0   0.5   Z=3
0   0   -0.5   0   -0.5
Since all Cj-Zj≤0,
Hence, integer optimal solution is arrived with value of variables as :
x1=1, x2=1, Max Z=3 (01 mark)
b.   Calculation of following table: (03 marks)   08
Activity   to   tm   tp   te=6to+4tm+tp   te
A   6   7   8 (6+4×7+8)/6=42/6   7
B   3   5   7 (3+4×5+7)/6=30/6   5
C   4   7   10 (4+4×7+10)/6=42/6   7
D   2   3   4 (2+4×3+4)/6=18/6   3
E   3   4   11 (3+4×4+11)/6=30/6   5
F   4   8   12 (4+4×8+12)/6=48/6   8
G   3   3   9 (3+4×3+9)/6=24/6   4
H   6   6   12 (6+4×6+12)/6=42/6   7
I   5   8   11 (5+4×8+11)/6=48/6   8
J   3   3   9 (3+4×3+9)/6=24/6   4
Finding Critical Path as follows: (03 marks)
From the diagram, we can see that nodes that satisfy the requirements are:
1 - 4 - 6 - 7 - 8 or C - F - H – J, the estimated time is: 7 + 8 + 7 + 4 = 26
days. (02 marks)
6   20
********** 12 **********
--- page 13 ---
a.   Explanation based on the following points: (04 marks)
 A positive shadow price means the resource is binding and extra
units would raise profit.
   If the firm can obtain an extra unit at a cost lower than the
shadow price, it should increase availability; expected profit gain
≈ (Shadow Price × Extra Units) within the allowable range.
   If the cost exceeds the shadow price, it is not worthwhile.
Dual: (04 marks)
Min W = 10y₁ + 2y₂ + 6y₃
s.t.
y₁ + 2y₂ + 2y₃ ≥ 1
y₁ – y₂ – 2y₃ ≥ –1
– y₂ – 3y₃ ≥ 1
y₁,y₂,y₃ ≥ 0
b.   Finding initial solution (03 marks)
x1=1.92,x2=2.69
ZA=-11.92
Sub-problem A, x1(=1.92) must be an integer value, so two new constraints
are created, x1≤1 and x1≥2 (1 mark)
Sub-problem B: Solution is found by adding x1≤1.
Solution is
Min ZB=-11 (x1=1,x2=3) ((1 mark)
Sub-problem C: Solution is found by adding x1≥2.
Solution is
Min ZC=-11.8 (x1=2,x2=2.6) (1 mark)
In Sub-problem C, x2(=2.6) must be an integer value, so two new
constraints are created, x2≤2 and x2≥3
Sub-problem D: Solution is found by adding x2≤2.
Solution is
Min ZD=-11 (x1=2.5,x2=2) (01 mark)
Sub-problem E: Solution is found by adding x2≥3.
Solution is
This Problem has an infeasible solution, so this branch is terminated.
(1 mark)
Every step should be backed by correct graphical solution.
c.   Description on the basis of following points: (03 marks)
********** 13 **********
--- page 14 ---
   In an assignment problem, each task (job) is assigned to one agent
(machine/person) to optimize total cost or profit.
 A minimization problem aims to minimize total cost or time (e.g.,
assigning workers to jobs to reduce total time).
 A maximization problem seeks to maximize total profit or
efficiency.
 The approach is the same (Hungarian method or similar), but for a
maximization case we convert it to a minimization by subtracting
all values from the largest entry (so higher profits become smaller
“costs”).
Relevant example of an assignment problem (02 marks)
********** 14 **********
````
