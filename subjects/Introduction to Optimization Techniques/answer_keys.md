# Introduction to Optimization Techniques: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 93103f0f8617

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/Introduction to Optimization Techniques/ANS_Introduction to Optimization Techniques(701BS0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (22 pages), mean OCR confidence 77.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: DIPLOMA IN COMPUTER SCIENCE AND ENGINEERING
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Optimization Techniques
Date: 15 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   20
a. ABC Foods Company is developing a low–calorie, high–protein diet supplement called
Hi–Pro. The specifications for Hi–Pro have been established by a panel of medical
experts. These specifications, along with the calorie, protein, and vitamin content of three
basic foods, are given in the following table.
Units of Nutritional Elements Basic Foods Hi
Nutritional
/100 gm serving of Basic Foods   –   Pro
Elements
1   2   3   Specifications
Calories   350   250   200   300(max.)
Proteins   250   300   150   200(max.)
CO-
1,4;   Vitamin A   100   150   75   100(min.)   5
K3   Vitamin C   75   125   150   100(min.)
Cost/serving (Rs.)   1.50   2.00   1.20
Formulate this problem as an LP model to minimize the cost of serving.
Sol:
---1M
********** 1 **********
--- page 2 ---
obj function ----1M, constraints-----3M
b. Apples are stored in warehouses at four different locations (New York, Philadelphia,
Atlanta, and Dallas), which supply three distribution centers (Boston, Detroit, and
Miami). The apples are transported in tons. The supply capacities, demands, and
transportation costs per ton are given below. Determine the initial transportation plan that
minimizes the total shipping cost. Use the Northwest Corner Method (NWCM) to find
the initial feasible solution and initial cost.
Cost to Distribution Center
CO-
1,3,4;   A: Boston   B: Detroit   C:   Supply (tons)   5
K3   Miami
Cost   from 1: New York   4   1   2   100
Warehouse   2: Philadelphia   6   4   3   120
3: Atlanta   5   2   6   120
4: Dallas   9   7   8   150
Demand (tons)   210   100   180
Sol:
********** 2 **********
--- page 3 ---
---4 M
Z=400+660+40+180+180+1200 Z=2660Z = 2660Z=2660   ------1M
c. A student, Sarah, is considering three career options after graduation: Software Engineer
(D1), Data Scientist (D2), and Product Manager (D3). Her future salary in each career
path depends on how the job market evolves. The possible states of the job market are
High Demand (S1), Moderate Demand (S2), and Low Demand (S3). Sarah's potential
annual earnings (in thousands of dollars) in each career under each market condition are
provided below:
career   Market demand
options   High   Moderate Low
D1   120   85   50
D2   110   90   70
D3   100   80   60
CO-
1,2,4;   Which career path should she choose based on the Maximin decision criteria?   5
K2
Sol:
---3M
Choose Maximum of the Minimum Values
Max(50,70,60)=70   ----------1M
********** 3 **********
--- page 4 ---
The Maximin value = 70 corresponds to D2 (Data Scientist).
Sarah should choose the career path of Data Scientist.   ----------1M
This decision ensures the best worst-case income, meaning that even in the worst
market conditions, she will earn $70,000, which is higher than the worst-case outcomes
of the other options.
d. Solve the following assignment problem to determine an assignment of workers to jobs
that minimizes the total completion time, and state the minimum total time.
Jobs
Worker   A   B   C   D
1   12   7   9   7
2   8   9   6   6
3   7   17   12   14
4   15   14   6   10
SOL:
Row-reduced matrix   ------------1M
Jobs
Worker   A   B   C   D
CO-
1   5   0   2   0
1,3,4   5
;   2   2   3   0   0
K3
3   0   10   5   7
4   9   8   0   4
Col reduced matrix   ----------1M
Jobs
Worker   A   B   C   D
1   5   0   2   0
2   2   3   0   0
3   0   10   5   7
4   9   8   0   4
Assignments------------2M
SOLUTION:------------1M
1-B 7
********** 4 **********
--- page 5 ---
2-D 6
3-A 7
4-C 6
TOTAL=26
Q2   20
a. A furniture manufacturer produces tables and chairs using wood and labor. The available
resources are 40 units of wood and 30 hours of labor. Each table requires 5 units of wood
and 3 hours of labor, while each chair requires 2 units of wood and 2 hours of labor. The
profit per table is $20, and the profit per chair is $10. The manufacturer wants to
determine how many tables and chairs to produce to maximize profit while staying within
the resource limits. Formulate this as an LPP, define the decision variables, constraints,
and objective function, and solve it graphically.
SOL:
Formulation:
x = number of tables produced, y= number of chairs produced   -----------1M
Z max= 20x+10y   -------------------1M
CO-   5x+2y<=40
1,4;
K3   3x+2y<=30   10
x,y>=0   -------------------2M
Graphical solution:
---------1M
********** 5 **********
--- page 6 ---
------------2M
------------2M
Optimal Production
•   Tables = 5
•   Chairs = 7.5
Maximum Profit Z=175 ------------1M
Solve the following LPP using the Simplex method.
b. Maximize Z = 8 x 1 + 12 x 2 + 4 x 3
subject to,
2 x 1 + 2 x 2 + 2 x 3  6
2 x 1 + 5 x 2 + 10 x 3  20
CO-   x 1 , x 2 , x 3  0
1,4
K2   Solution:   10
Std form----------------3M
Iteration 1----------------3M
Iteration 2----------------3M
Final ans---------------------1M
********** 6 **********
--- page 7 ---
Final ans
Q3   20
a. A firm manufacturing industrial chemicals has 3 plants, P1, P2 , and P3 , each having
capacities to produce 350 kg, 300 kg, and 500 kg, respectively, of a particular chemical
per day. Four bulk consumers have placed orders for the products on the following
basis:
Consumer   kg Required per Day
I   400
II   250
III   350
CO-
1,3,4   IV   150
10
K3   Shipping costs (paise per kg) from plants to consumers:
Plant   C1   C2   C3   C4
P1   3   5   4   6
P2   8   11   9   12
P3   4   6   2   8
1. Write the mathematical formulation of the above transportation problem.
2. Find the initial shipping cost using the Least Cost Method (LCM).
Solution:
********** 7 **********
--- page 8 ---
1. Mathematical Formulation of the Transportation Problem

Decision Variables

Let

© 2X4; = kg shipped from P1— C1
© X49 = kg shipped from P1 > C2
© 213 = kg shipped from P1 — C3
© 214 = kg shipped from P1 — C4
© 2&9; = kg shipped from P2 — C1
© X99 = kg shipped from P2 — C2
*® X93 = kg shipped from P2 — C3
© 224 = kg shipped from P2 — C4
© 231 = kg shipped from P3 — C1
© 2X39 = kg shipped from P3 — C2
*® 2X33 = kg shipped from P3 — C3
© 2X34 = kg shipped from P3 — C4

Objective Function (Minimize Transportation Cost)
Minimize Z = 321, + 5x12 + 4213 + 6214 + 8x01 + Llao2 + 9x23 + 12224 + 431 + Gago + 2233 + Bars

(All costs are in paise per kg.)

Supply Constraints

Plant P;

By + LQ + 23 + X14 = 350
Plant P2

©, + Loq + Lo3 + Loy = 300
Plant P3

231 + @gq + £33 + 34 = 500

Demand Constraints

Consumer C,

2) + %q) + eg, = 400
Consumer C2

212 + Log + 32 = 250
Consumer C3

213 + Lo93 + @33 = 350

Consumer C4

@14 + Lo4 + X34 = 150

Non-negativity Xij>0

Formulation

FIC QF EH 1
--- page 9 ---
LCM Allocation Table
Plant / Consumer   C1 C2 C3 C4 Supply
P1   350 0   0   0   350
P2   0   150 0   150 300
50 100 350 0   500
Demand   400 250 350 150
--------- 5M
Initial Transportation Cost
Z=6000 paise i.e. Z=60 rupees   ---------------1M
b. A small electronics retailer is deciding which type of new gadget to stock for the
upcoming holiday season. The store can choose to stock one of three types of gadgets:
Smartwatches (D1), Wireless Earbuds (D2), or Portable Speakers (D3). The success
of each choice depends on customer demand, which could be high, moderate, or low
(these are the states of nature). The profit in each state is estimated based on market
research. The estimated profit (in dollars) for each choice under each state of nature is as
CO-   follows:
1,2,4   10
K2   Market demand
New gadgets   High   Moderate   Low
Smartwatches (D1)   1200   1000   900
Wireless Earbuds (D2)   1300   1100   800
Portable Speakers (D3)   1400   950   850
Which stocking option should the retailer choose based on 1) Maximax decision criteria
and 2) Laplace decision criteria?
Solution:
********** 9 **********
--- page 10 ---
-------------5M
-------------5M
Maximax favors Portable Speakers (the highest possible profit).
Laplace results in a tie between Wireless Earbuds and Portable Speakers since both
have the same average profit.
Q4
a. A project manager needs to assign four technicians to perform four different maintenance
tasks. Each technician can perform only one task, and each task must be assigned to
CO-
1,3,4   exactly one technician. The manager wants to minimize the total time required to 10
K3   complete all the tasks. Based on records, the estimated time (in minutes) taken by each
technician to complete each task is given in the following table.
********** 10 **********
--- page 11 ---
maintenance tasks
technicians A   B   C   D
1   2   10   9   7
2   15   4   14   8
3   13   14   16   11
4   4   15   13   9
Determine the optimal assignment of technicians to tasks that minimizes the total
completion time using the Hungarian Method, and find the minimum total time.
Solution:
Row reduced   maintenance tasks
technicians A   B   C   D
1   0   8   7   5
2   11   0   10   4
3   2   3   5   0
4   0   11   9   5
-------------1M
Col reduced   maintenance tasks
technicians A   B   C   D
1   0   8   2   5
2   11   0   5   4
3   2   3   0   0
4   0   11   4   5
Col reduced---------------1M, allocations--------------2M,   lines-------1M
1st improved   maintenance tasks
technicians A   B   C   D
1   0   6   0   3
2   13   0   5   4
3   4   3   0   0
4   0   9   2   3
1st improved--------------2M,   allocations--------------2M
MIN TOTAL TIME=28--------------1M
CO-   b.   1) What is meant by strictly determinable and pure game? How is it identified?
1,2,4;
2) Determine whether the following game is strictly determinable and pure.
K2   10
Two consumer electronics companies, Nova Electronics Ltd. and Zenith Systems
Pvt. Ltd., are competing in the premium home appliance market. Each company
********** 11 **********
--- page 12 ---
has four alternative product strategy options. The following payoff matrix (in ₹
millions) gives the profit to Nova Electronics. Solve the game for the optimal
strategies of the two players and for the value of the game.
Zenith Systems Pvt. Ltd.
Z1   Z2   Z3   Z4
N1   -1   0   0   5
Nova
N2   3   2   2   2
Electronics
N3   -4   -3   0   2
Ltd.
N4   5   3   -4   2
Solution:
1)
Strictly Determinable Game:
A game is said to be strictly determinable if there exists a saddle point in the payoff
matrix. In such a case, the maximin value equals the minimax value, and both players
have optimal strategies without randomization.
Pure Strategy:
A pure strategy means that a player consistently chooses one specific strategy with
probability 1. No mixing of strategies is required.
Identification Method:
To identify whether a game is strictly determinable:
1. Find Row Minimums (because Player A/Nova wants to maximize profit but
must consider the worst-case outcome in each row).
2. Find Column Maximums (because Player B/Zenith wants to minimize Nova’s
profit but must consider the worst Nova could earn in each column).
3. Compute:
o Maximin = Maximum of Row Minimums
o Minimax = Minimum of Column Maximums
4. If Maximin = Minimax, a saddle point exists, and the game is strictly
determinable with pure strategies.
---------------------4M
********** 12 **********
--- page 13 ---
2)
Row minimum values (−1,  2,  −4,  −4)
Maximin: Max (−1,2,−4,−4)=2
Column maximum values (5,  3,  2,  5)
Minimax: min (5,3,2,5)=2
Maximin = Minimax = 2, a saddle point exists.
Optimal strategy for Nova Electronics: N2
Optimal strategy for Zenith Systems: Z3
The game is strictly determinable.
A pure strategy saddle point exists at (N2, Z3).
Value of the game = ₹2 million., The game is not pure.
---------------------6M
Q5   20
a. Solve the following LPP graphically.
Min Z = 5 x 1 + 10 x 2
Subject to the constraints
x 1 + 2 x 2  120 , x 1 + x 2  60 , x 1 − 2 x 2  0 , x 1 , x 2  0 .
CO-
1,4;   Solution:
K3   10
********** 13 **********
--- page 14 ---
Graph--------------6M
Points--------------3M
Final ans----------1M
b. Find the dual of the following primal problem
Z   = 5 x − x + 3 x
min   1   2   3
Subject to the constraints
2 x − 3 x + 4 x  5
1   2   3
x − 2 x + 6 x  3
1   2   3
x 1 , x 2 , x 3  0
Solution:
CO-
1,4   5
K2
---------------1M
********** 14 **********
--- page 15 ---
-------------4M
c Mr. Anand wants to invest in one of the three options A, B, and C. The pay-off for his
investment depends on the nature of the economy (inflation, recession, or no change).
The possible returns under each economic situation are given below
Strategy   Nature of Economy
Inflation E1   Recession E2 No Change E3
S1   2000   1200   1500
S2   3000   800   1000
S3   2500   1000   1800
What course of action does he take according to the Hurwicz ( = 0 6. ) criterion?
Solution:
CO-
1,2,4   5
K2
------------2M
----------3M
Q6   20
********** 15 **********
--- page 16 ---
CO-   a   Solve the following LPP graphically.
1,4,   Max Z = x + 2 x
1   2
K3   Subject to the constraints
x 1 + 2 x 2  100 , 2 x 1 − x 2  0 , 2 x 1 + x 2  200 , x 1 , x 2  0 .
Sol:
10
Graph--------------6M
Points--------------3M
Final ans----------1M
b. A technology firm manufactures and sells smartphones and smartwatches in India. The
company has recently expanded its production facility, which can operate for 48 hours
per week. To assemble one smartphone, the production line requires 2 hours, while
CO-   assembling one smartwatch requires 3 hours of manufacturing time. The company
1,4;   5
estimates that each smartphone yields a profit of approximately ₹4,000, and each
K3
smartwatch yields a profit of approximately ₹1,500. Market research indicates that due to
demand limits, the company can sell at most 15 smartphones and 10 smartwatches per
week. Formulate a linear programming model to determine the number of smartphones
********** 16 **********
--- page 17 ---
and smartwatches the firm should produce weekly to maximize total profit, considering
the constraints on production capacity and market demand.
Solution:
---------1M
------------4M
c. Following severe flooding in multiple regions, a disaster management authority must
distribute relief kits from warehouses located at Coimbatore, Visakhapatnam, and Kanpur
to affected districts, including Mysuru, Prayagraj, and Jabalpur. The warehouses at
Coimbatore, Visakhapatnam, and Kanpur can dispatch 600, 700, and 500 relief kits per
day, respectively. The daily requirement in Mysuru is 500 kits, in Prayagraj 600 kits, and
in Jabalpur 700 kits. The transportation cost per relief kit from each warehouse to each
district is given in the attached cost matrix.
CO-
Compute an initial feasible solution using the Least Cost Method (LCM) for the given 5
1,3,4;
K3   Transportation problem.
Transportation Cost Table (₹ per relief kit)
From / To   Mysuru   Prayagraj Jabalpur
Coimbatore   500   1100   950
Visakhapatnam   600   1000   700
Kanpur   850   400   600
Solution:
********** 17 **********
--- page 18 ---
----4M
Total Transportation Cost: Z=1,050,000   -------------1M
Q7   20
a. Check whether a saddle point exists for the following game. If a saddle point does not
exist, solve the game using the dominance rule and determine the optimal strategies and
the value of the game.
Firm B
B1   B2   B3
Firm A   A1   12   10   8
A2   14   14   10
A3   16   12   15
Solution:
CO-
1,2,4   10
K2
-------3M
--------------1M
********** 18 **********
--- page 19 ---
Step 2: Apply Dominance Rule
A2 ≥ A1, Since A2 dominates A1, eliminate A1.
B1 B2 B3
A2 14 14 10
A3 16 12 15
----------------------------1M
B2 ≤ B1 → B2 dominates B1
Eliminate B1
B2 B3
A2 14 10
A3 12 15
----------------------------1M
Let, A plays A2 with probability p, A plays A3 with probability (1 − p)
Make B indifferent
Payoff for B2: 14p+12(1−p)
Payoff for B3: 10p+15(1−p)
Equating
14p+12−12p=10p+15−
2p+12=−5p+15
7p=3
p=3/7
So, A3 probability = 4/7
Strategy of Player B
Let B play
• B2 = q
• B3 = 1 − q
Equating payoffs of rows
14q+10(1−q)=12q+15(1−q)
14q+10−10q=12q+15−15q
4q+10=−3q+15
7q=5
q=5/7
********** 19 **********
--- page 20 ---
So, B3 probability = 2/7
Value of Game
Substitute p=3/7
V=14p+12(1−p)
V=14(3/7)+12(4/7)
V=6+48/7
V=90/7
V≈12.86
Optimal Strategies
Player A
• A2 = 3/7
• A3 = 4/7
Player B
• B2 = 5/7
• B3 = 2/7
Value of game: V=90/7≈12.86
--------------------4M
b. A consumer electronics company is planning to launch a new product line for the
upcoming festive season. After several brainstorming sessions, the management has
shortlisted three design alternatives: Product A, Product B, and Product C.
However, the future market demand for the product is uncertain. Based on past sales
patterns and current market analysis, the marketing department has identified four
possible demand scenarios: Low (State 1), Moderate (State 2), High (State 3), and Very
High (State 4), with associated probabilities of 0.25, 0.35, 0.25, and 0.15, respectively.
The projected profits (in thousands of rupees) for each product under these market
CO-   conditions are summarized below:
1,2,4;   Market demand   5
K2   Product   Low   Moderate   High   Very High
A   30   50   80   100
B   40   60   70   90
C   20   55   85   95
Using the EOL, determine the best investment decision.
Solution:
********** 20 **********
--- page 21 ---
-----------------------3M
Minimum EOL = 5.25 -----------------1M
Best decision: Launch Product B   -----------------1M
c. A pharmaceutical company is planning to introduce a new over-the-counter medicine.
The management has three possible investment strategies: Strategy A, Strategy B, and
Strategy C. However, the future demand for the medicine is uncertain. Based on market
research, the company has identified four possible demand conditions: Poor, Fair, Good,
and Excellent, with probabilities 0.20, 0.30, 0.35, and 0.15, respectively. The expected
profits (in lakhs of rupees) under each market condition are given in the table below.
CO-
1,2,4;   Using the Expected Monetary Value (EMV) criterion, determine the best decision.   5
K2
Strategy Poor Fair Good Excellent
A   20 40 70   90
B   30 50 60   80
C   10 45 80   85
Solution:
********** 21 **********
--- page 22 ---
Payoff Table (Profit in = lakhs)

Good Excellent EMV
Strategy Poor (0.20) Fair (0.30) (0.35) (0.15) Calculation EMV

A 20 40 70 90 (20%0,20)+ 54
(40%0,30)+
(70x0,35)+
(900,15)

B 30 50 60 80 (30%0,20)+ 54
(50x0,30)+
(60*0,35)+
(800,15)

c 10 45 80 85 (10*0.20)+ 56.25
(45x0.30)+
(80x0.35)+
(850.15)

Highest EMV = 56.25
Best Decision: Strategy C

FIR ICR DAC HH
````
