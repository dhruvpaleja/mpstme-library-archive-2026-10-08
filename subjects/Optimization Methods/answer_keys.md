# Optimization Methods: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 7a42bd192f7f

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSE_DS_7057/Optimization Methods/ANS_Optimization Methods(702BS0C079)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Optimization Methods
Date: 08 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figure on right hand side indicates full marks
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1. a
Aggie Power Generation has four generating stations S₁, S₂, S₃ and S₄ with annual available capacities (in
MW) 5, 8, 7 and 14 respectively. They supply three markets (destinations) D₁, D₂, D₃ whose annual demands
are 7, 9 and 18 MW respectively. The unit shipping costs ($/MW) from each station to each destination are
given below
D₁   D₂   D₃   Supply
S₁   2   7   4   5
S₂   3   3   1   8
S₃   5   4   7   7
S₄   1   6   2   14
Demand   7   9   18   34
Using the North-West Corner Method, determine an initial basic feasible solution for the Aggie Power
distribution problem and compute the total distribution cost.
Solution:
4 Marks
********** 1 **********
--- page 2 ---
1 Marks
Q1. b
Formulate the dual of the given primal problem.
Maximize Z = 6 x 1 + 4 x 2
subject to,
2 x 1 + 3 x 2  12
x 1 + x 2  6
x 1 + 4 x 2 = 8
x 1 , x 2  0
Solution:
Since objective function is maximizing, all ≥ constraints (2) can be converted to ≤ type by multiplying both
sides by -1
---------------------------------------------------(1 mark)
MAX zx = 6 x1 + 4 x2
subject to
2 x1 + 3 x2 ≤ 12
- x1 - x2 ≤ -6
x1 + 4 x2 = 8
and x1,x2≥0;
In primal, There are 2 variables and 3 constraints, so in dual there must be 2 constraints and 3 variables
In primal, The coefficient of objective function c1=6,c2=4 becomes right hand side constants in dual
In primal, The right hand side constants b1=12,b2=-6,b3=8 becomes coefficient of objective function in
dual
In primal, objective function is maximizing, so in dual objective function must be minimizing
Let y1,y2,y3 be the dual variables
Since 3rd constraint in the primal is equality, the corresponding dual variable y3 will be unrestricted in sign.
---------------------------------------------------(1 mark)
Dual is
MIN Zy = 12 y1 - 6 y2 + 8 y3
subject to
2 y1 - y2 + y3 ≥ 6
3 y1 - y2 + 4 y3 ≥ 4
and y1,y2≥0;y3 unrestricted in sign
------------------------------------(3 marks)
********** 2 **********
--- page 3 ---
Q1. c
State whether the game whose payoff matrix is given below is strictly determinable and fair. Also, determine
the value of the game.
Player B
B1   B2   B3   B4
A1   −5   −2   0   7
Player A   A2   5   −6   −4   8
A3   4   0   2   3
Solution:
Player B
B1   B2   B3   B4
A1   −5   −2   0   7   -5
Player A   A2   5   −6   −4   8   -6   3 Marks
A3   4   0   2   3   0
4   0   2   8
Maximin
Minimax
• As minimax=maximin, saddle point exits, it is strictly determinable
• A uses A3 strategy and B uses B2 strategy.   2 Marks
• Value of the gate is zero, it’s a fair game.
Q1. d
A sales representative has to travel to four major cities to meet clients and promote new products. He will
begin his journey from one city, visit each of the remaining cities exactly once, and finally return to the starting
city. The estimated travel cost (in thousand rupees) between every pair of cities is given in the table below.
A   B   C   D
A   -   15   20   10
B   25   -   35   15
C   5   25   -   20
D   10   20   12   -
He wants to plan his trip in the most economical way possible so that his total travel expense is minimized.
What should be the order in which the salesman visits the cities so that the total travel cost is minimized?
Solution:
Row operation   Column Operation
………………………(1 mark)   ………………………….(1 mark)
********** 3 **********
--- page 4 ---
Allocation
…………….(2 marks)
Optimal solution is A → B → D → C → A   ……………(1 Mark)
Q2. a
Solve the following two player game.
Player B
B₁   B₂   B₃   B₄
A₁   5   -10   9   0
Player A   A₂   6   7   8   1
A₃   8   7   15   1
A₄   3   4   -1   4
Solution:
Show that saddle point does not exists (maximin, minimax). ………………………(3 marks)
….1 marks   ……1 marks   ……1 marks
……1 marks
…….3 marks
Q2. b
A manufacturing company produces three types of portable LED lamps Model A, Model B, and Model C.
The profit obtained from the sale of each unit of Model A, Model B, and Model C is ₹30, ₹40, and ₹20
respectively. Each unit of the product requires processing time on a common machining line. The machining
********** 4 **********
--- page 5 ---
time required per unit is 10 minutes for Model A, 12 minutes for Model B, and 7 minutes for Model C. The
total available machining time per week is limited to 10,000 minutes. In addition, due to packaging and market
constraints, the total number of lamps (of all models together) that can be produced in a week cannot exceed
1,000 units.
Formulate and solve a Linear Programming Problem (LPP) to determine the number of units of each model
to be produced per week so that the total profit is maximized
Solution:
LPP formulation to maximize the profit:
Maximize Z = 30 x 1 + 40 x 2 + 20 x 3
subject to,
10 x 1 + 12 x 2 + 7 x 3  10000   ………………….(3 marks)
x 1 + x 2 + x 3  1000
x 1 , x 2 , x 3  0
Setting up the initial solution
And solving till iteration1 …………………………………………………………………….(3 marks)
Iteration 2 ………………………………….………………….(3 marks)
Final answer ………………….(1 marks)
Q3. a
Fresh Blend Beverages Pvt. Ltd. produces bottled juices at three factories in Dallas, Chicago, and Atlanta with
weekly capacities of 200, 160, and 90 crates respectively. They supply juices to three warehouses in New
York, Los Angeles, and Houston which require 180, 120, and 150 crates weekly. The unit shipping costs (in
dollars) are given in the table below.
Warehouse
Factory   New York Los Angeles Houston   Supply
Dallas   16   20   12   200
Chicago   14   8   18   160
Atlanta   26   24   16   90
********** 5 **********
--- page 6 ---
Demand   180   120   150   450
Determine the initial distribution for this company using the VAM method and check whether the obtained
solution is optimal using MODI method so that the total shipping cost is the minimum.
Solution:
1 mark   1 mark
1 mark   1 mark
IBFS VAM Solution : 120(8)+90(16)+12(60)+14(40)+16(140) = 5920   → 1 Mark
→ 1 Mark
→ 2 Marks
********** 6 **********
--- page 7 ---
→ 2 marks
Optimal value is 5920.. same as VAM
Q3. b
Mr Girish wants to invest Rs 10,000 in one of the three options A, B and C. The pay-off for his investment
depends on the nature of the economy (inflation, recession, or no change). The possible returns under each
economic situation are given below
Strategy   Nature of Economy
Inflation E1   Recession E2 No Change E3
S1   2000   1200   1500
S2   3000   800   1000
S3   2500   1000   1800
What course of action has he to take according to
(i) The pessimistic criterion (Maximin)
(ii) The equally likely criterion (Laplace)
(iii) The regret criterion.
(iv) Hurwicz criterion, the degree of optimism being 0.6.
Solution:
(i) Pessimistic criterion — Maximin
For each strategy find the minimum payoff across the states.
Strategy   Minimum
payoff (Rs)
A   1200
B   800
C   1000
Maximum among these minima = Rs 1200 for A.   --------------------(2 Marks)
(ii) Equally likely criterion — Laplace
Assume each state is equally likely (probability 1/3).
Strategy   Average payoff (Rs)
A   1566.67
B   1600.00
C   1766.67
The strategy with the largest average payoff is C.   --------------------(2 Marks)
********** 7 **********
--- page 8 ---
(iii) Regret criterion — Minimax regret
For each state (column) find the best payoff. Then compute regret = (best in state) − (actual payoff).
Strategy   Regret in   Regret in   Regret in No
Inflation (E1)   Recession (E2) change (E3) (Rs)
(Rs)   (Rs)
A   1000   0   300
B   0   400   800
C   500   200   0
For each strategy, the maximum regret (worst-case regret).
Strategy   Maximum
regret (Rs)
A   1000
B   800
C   500
The strategy with smallest maximum regret: C (max regret = Rs 500). ----------(3 Marks)
(iv) Hurwicz criterion — Degree of optimism α = 0.6
Hurwicz value = α*(maximum payoff) + (1−α)*(minimum payoff), where α = 0.6.
Strategy   Max payoff   Min payoff   Hurwicz value
(Rs)   (Rs)   (α=0.6)
A   2000   1200   1680.00
B   3000   800   2120.00
C   2500   1000   1900.00
Option B (highest Hurwicz value = Rs 2120.00).   ----------(3 Marks)
Q4. a
Solve the following LPP using the Big-M method to find the optimal cost.
Minimize Z = 500 x 1 + 200 x 2
subject to,
3 x 1 + 2 x 2  90
x 1  10
− 2 x 1 + x 2 = 0
x 1 , x 2  0
Solution:
Setting up the initial solution
And solving till iteration1 …………………………………..(4 marks)
Iteration 2 ………………………………….………………….(3 marks)
Iteration 3 ………………………………….………………….(2 marks)
********** 8 **********
--- page 9 ---
Iteration 1
Iteration 2
Iteration 3
Sol: x1=10, x2=20 and Z min=9000 ………………….(1 marks)
Q4. b
A company operates in five major territories and has five salesmen available for assignment. Each territory
differs in its sales potential, and each salesman has a different level of selling effectiveness. The estimated
annual sales that each salesman would generate in each territory are given in the table below:
Territories
A   B   C   D   E
1   32   38   40   28   40
2   40   24   28   21   36
Salesmen
3   41   27   33   30   37
4   22   38   41   36   36
5   29   33   40   35   39
Identify the best allocation of salesmen to territories so that the sales revenues are maximized.
Solution:
********** 9 **********
--- page 10 ---
As the given problem is of maximization type, it has to be converted to minimization type.
Minimization form
A B C D E
1 9   3   1 13 1
2 1 17 13 20 5
3 0 14 8 11 4
4 19 3   0   5 5
5 12 8   1   6 2
2 Marks
Row operation
A B C D E
1 8   2   0 12 0
2 0 16 12 19 4
3 0 14 8 11 4
4 19 3   0   5 5
5 11 7   0   5 1
1 mark
Column operation
A B C D E
1 8   0   0   7 0
2 0 14 12 14 4
3 0 12 8   6 4
4 19 1   0   0 5
5 11 5   0   0 1
1 mark
Allocation
A   B   C   D   E
1   8   0   0   7   0
2   0   14   12   14   4   ✓
3   0   12   8   6   4   ✓
4   19   1   0   0   5
5   11   5   0   0   1   ➔ 2 Marks
✓
Revised allocation (optimal)
A   B   C   D   E
1   12   0   0   7   0
2   0   10   8   10   0
3   0   8   4   2   0
4   23   1   0   0   5
5   15   5   0   0   1   ➔ 2 Marks
1→B, 2→A, 3→E, 4→C, 5→D   → 1 Mark
The associated maximum sales revenue is 38+40+37+41+35 = 191,000/-
********** 10 **********
--- page 11 ---
Q5. a
A bakery keeps stock of a popular brand of cake. Previous experience shows the daily demand pattern for the
item with associated probabilities, as given below
Daily Demand   0   10   20   30   40   50
Probability   0.01   0.20   0.15   0.50   0.12   0.02
Use the following sequence of random numbers to simulate the demand for next 10 days. Random numbers:
25, 39, 65, 76, 12, 05, 73, 89, 19, 49. Also estimate the daily average demand for the cakes on the basis of
the simulated data.
Solution:
The daily demand values and corresponding probabilities are:
Demand   Probability   Cumulative   Random number
probability   interval (00-99)
0   0.01   0.01   00 - 00
10   0.20   0.21   01 - 20
20   0.15   0.36   21 - 35
30   0.50   0.86   36 - 85
40   0.12   0.98   86 - 97
50   0.02   1.00   98 - 99
----------------(3 Marks)
Random numbers used (two-digit): 25, 39, 65, 76, 12, 05, 73, 89, 19, 49.
Simulation Table (10 days)
Day   Random number   Simulated demand (cakes)
1   25   20
2   39   30
3   65   30
4   76   30
5   12   10
6   05   10
7   73   30
8   89   40
9   19   10
10   49   30
-------------------(5 Marks)
Total demand over 10 days = 240 cakes.   -----------------(1 Mark)
Average daily demand = 240 / 10 = 24.00 cakes per day.   ------------------(1 Mark)
Q5. b
Solve the following Integer Linear Programming (ILP) problem using the Branch and Bound (Graphical)
method and determine the optimal integer solution.
Max z = 7 x 1 + 9 x 2
Subject to
− x 1 + 3 x 2  6
7 x 1 + x 2  35
x 2  7
x 1 , x 2 are non negative integers
********** 11 **********
--- page 12 ---
Solution:
……………(5 marks)
Branch at x1: x1<=4, x1>=5   …………………..(1mark)
Branch B solution …………………..(1mark)
Branch C solution …………………..(1mark)
Branch D solution …………………..(1mark)
Branch E solution …………………..(1mark)
********** 12 **********
--- page 13 ---
Q6. a
A fruit merchant purchases oranges at Rs 50 per basket and sells them at Rs 80. Unsold oranges are disposed
off at Rs 20 per basket the next day. Past record of sales for 120 days is as given below
Baskets Sold   15 16 17 18
No. of Days Sold 12 24 48 36
Using EMV, find how many baskets the merchant should purchase every day to maximize his profit.
Solution:
Here unsold baskets have a salvage value of Rs 20 each. Therefore, the loss per basket is 50-20 = 30.
Daily sales (D)   No. of days (out of 120)   Empirical probability
15   12   0.10
16   24   0.20
17   48   0.40
18   36   0.30
----------------(1 Mark)
********** 13 **********
--- page 14 ---
Thus the Profit = 30 (no. of baskets sold) - 30 (no. of baskets unsold)
Stock Q \ Demand D   15   16   17   18
Probability   0.1   0.2   0.4   0.3
15   Rs 450.00   Rs 450.00   Rs 450.00   Rs450.00
16   Rs 420.00   Rs 480.00   Rs 480.00   Rs 480.00
17   Rs 390.00   Rs 450.00   Rs 510.00   Rs 510.00
18   Rs 360.00   Rs 420.00   Rs 480.00   Rs 540.00
-------------------(2 Marks)
Stock Q EMV = Σ [Profit(Q,D) × P(D)]   EMV (Rs)
15   450*0.1 +450*0.2 +450*0.4+450*0.3 = 450   450
16   420*0.1 +480*0.2 +480*0.4+480*0.3 = 474   474
17   390*0.1 +450*0.2 +510*0.4+510*0.3 = 486   486
18   360*0.1 +420*0.2 +480*0.4+540*0.3 = 474   474
-------------------(1 Mark)
Since the highest EMV is 486, the course of action to be chosen is A3. Thus the merchant should
purchase 17 baskets every day.   -------------------(1 Mark)
Q6. b
A company produces motorcycle seats. The company has two production lines. The production rate for line 1
is 50 seats per hour and for line 2 it is 60 seats per hour. The company has entered into a contract to daily
supply 1,200 seats daily to another company. Currently, the normal operation period for each line is 8 hours.
The production manager of the company is trying to determine the best daily operation hours for the two lines.
He has set the priorities to achieve his goals, as given below:
P1: Produce and deliver 1,200 seats daily
P2: Limit the daily overtime operation hours of line 2 to 3 hours
P3: Minimize the underutilization of the regular daily operation hours of each line. Assign differential weights
based on the relative productivity rate.
P4: Minimize the daily overtime operation hours of each line as much as possible. Assign differential weights
based on the relative cost of overtime. It is assumed that the cost of operation is identical for the two production
lines.
Formulate this problem as a Goal Programming model.
Solution:
Let 𝑥1 𝑎𝑛𝑑 𝑥2 = daily operation hours for the lines 1 and 2, respectively.
It may be noted in this problem that the first criterion for determining the differential weights in the
third priority goal is the relative cost of overtime. The production rates ratio for the lines is 50 to 60.
Therefore, the relative cost resulting from an hour of overtime is greater for line 1 than for line 2. The
relative cost of overtime ratio for line 1 to line 2 will be line 6 to line 5. Second, the criterion for
determining the differential weights in the fourth priority goal is relative productivity rate. Since the
productivity of line 1 is 50 seats/ hour and of line 2 is 60 seats/hour, the productivity goals are weighted
for line 1 to line 2 as line 5 to line 6. The goal programming model for this problem can now be
formulated as follows ------(1 Mark)
Then the GP model is stated as follows:
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑4 + + 𝑃3(5𝑑2 −+ 6𝑑3 −) + 𝑃4(6𝑑2 + + 5𝑑3 +) ---------------(1 Mark)
********** 14 **********
--- page 15 ---
subject to the constraints
50𝑥1 + 60𝑥2 + 𝑑1 −−𝑑1 + = 1200
𝑥1 + 𝑑2 −−𝑑2 + = 8   ----------------(1 Mark)
𝑥2 + 𝑑3 −−𝑑3 + = 8
𝑥2 + 𝑑4 −−𝑑4 + = 11   ----------------(1 Mark)
and   𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑2 +, 𝑑3 −, 𝑑3 +, 𝑑4 −, 𝑑4 + ≥0. ----------------(1 Mark)
Q6. c
Given an Integer Linear Programming (ILP) problem with a relaxed optimal solution from the Simplex
method is shown below:
Max z = 2 x 1 + 5 x 2
Subject to
2 x 1 + 3 x 2  1, x 2  2,
x 1 , x 2 are non negative integers
CJ   2   5   0   0
B   CB XB   X1   X2   S1   S2
X2   5   0.3333   0.6667 1   0.3333 0
S2   0   1.6667   -0.6667 0   -0.3333 1
Z=1.6665   ZJ   3.3333 5   1.6667 0
CJ-ZJ   -1.3333 0   -1.6667 0
a) Construct first Gomory's fractional cut for the given non-integer optimal solution.
b) Illustrate the first iteration of Gomory’s cutting-plane method.
Determine the non-integer optimal solution after first Gomory’s cut.
Solution:
1. From Simplex solution:
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=0,x2=0.3333
Max Z=1.6667…………………….[02 Marks]
2. First iteration of Gomory’s cutting-plane method.
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut, with the help
of x2-row as follows:
0.3333=0.6667x1+1x2+0.3333S1
(0+0.3333)=(0+0.6667)x1+(1+0)x2+(0+0.3333)S1
The fractional cut will become
-0.3333=Sg1-0.6667x1-0.3333S1→ (Cut-1)
Adding this additional constraint at the bottom of optimal simplex table. The new table so obtained is
…………………….[02 Marks]
********** 15 **********
--- page 16 ---
…………………….[02 Marks]
Minimum negative XB is -0.3333 and its row index is 3. So, the leaving basis variable is Sg1.
Minimum positive ratio is 2 and its column index is 1. So, the entering variable is x1.
∴ The pivot element is -0.6667.
Entering =x1, Departing =Sg1, Key Element =-0.6667
R3(new)=R1(old) ÷(-0.6667)
R1(new)=R3(old) -(0.6667) R3(new)
R2(new)=R2(old) +(0.6667) R3(new)
…………………….[02 Marks]
3. Non-integer optimal solution after first Gomory’s cut
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=0.5,x2=0
Max Z=1…………………….[02 Marks]
********** 16 **********
--- page 17 ---
Q7. a
Distinguish between (i) Pure strategy and mixed strategy (ii) Zero-sum and non-zero-sum games.
Solution:
Pure Strategy   Mixed Strategy
A strategy in which a player consistently   A strategy in which a player randomly selects among two or
follows one specific course of action.   more pure strategies according to certain probabilities.
Deterministic (definite choice).   Probabilistic (involves randomization).
Opponent can predict the player’s move.   Opponent cannot easily predict the player’s move.
Used when one strategy always provides   Used when no pure strategy dominates; helps in achieving
the best payoff.   equilibrium.
3 Marks
Zero-Sum Game   Non-Zero-Sum Game
The gain of one player is exactly equal to   The gain or loss of one player does not necessarily equal
the loss of another.   the loss or gain of another.
Constant (sum of payoffs = 0).   Variable (sum of payoffs ≠ 0).
Purely competitive — one’s success means May involve both competition and cooperation.
another’s failure.
2 Marks
Q7. b
What is Monte Carlo simulation? Describe the idea of experimentation (Random sampling) in simulation.
Solution:
The monte Carlo simulation approach is used to incorporate the random behaviour of variable(s) of
interest in a model. A formal definition of Monte Carlo Simulation is as follows:
• The Monte Carlo simulation technique involves conducting repetitive experiments on the model of the
system under study, with some known probability distribution to draw random samples (observations)
using random numbers.
The Monte Carlo simulation approach consists of following steps:
1. Setting up a probability distribution for variables to be analysed.
2. Building a cumulative probability distribution for each random variable.
3. Generating random numbers and then assigning an appropriate set of random numbers to represent
value or range (interval) of values for each random variable.
4. Conducting the simulation experiment using random sampling.
5. Repeating Step 4 until the required number of simulation runs has been generated.
6. Designing and implementing a course of action and maintaining control. -------(4 Marks)
Random Number Generation: Monte Carlo simulation requires the generation of a sequence of random
numbers where
(i)   all numbers are equally likely, and
(ii)   no patterns appear in sequence of numbers. This sequence of random numbers helps in
choosing random observations (samples) from the probability distribution
-----------(1 Mark)
Q7. c
Use the Graphical Method to solve the following Goal Programming Problem.
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑4 + + 5𝑃3𝑑2 −+ 3𝑃3𝑑3 −+ 𝑃4𝑑1 +
subject to the constraints
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 80
********** 17 **********
--- page 18 ---
𝑥1 + 𝑑2 −= 70
𝑥2 + 𝑑3 −= 45
𝑥1 + 𝑥2 + 𝑑4 −−𝑑4 + = 90
𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑3 −, 𝑑4 −, 𝑑4 + ≥0.
Solution:
We assume the priority ordering (lexicographic): P1 (highest), then P2, then P3, then P4. If you have a
different priority ordering please tell me and I will recompute accordingly.
Step 1: Express deviational variables in x1,x2
d1^- = max(80 - (x1 + x2), 0)
d1^+ = max((x1 + x2) - 80, 0)
d2^- = max(70 - x1, 0)
d3^- = max(45 - x2, 0)
d4^- = max(90 - (x1 + x2), 0)
d4^+ = max((x1 + x2) - 90, 0)   ---------------(2 Marks)
Step 2: Priority 1 & 2 -> feasible strip
Minimizing d1^- requires x1 + x2 ≥ 80. Minimizing d4^+ requires x1 + x2 ≤ 90. Combined: 80 ≤ x1 + x2 ≤
90. We restrict attention to this strip for subsequent priorities.
Step 3: Minimize P3-term (5 d2^- + 3 d3^-) on the strip
We minimize f3(x1,x2) = 5·max(70-x1,0) + 3·max(45-x2,0) subject to 80 ≤ x1 + x2 ≤ 90. A numerical
search on a fine grid yields the minimum f3 value and the corresponding point shown in the contour plot
below.   ---------------(2 Marks)
---------------(4 Marks)
********** 18 **********
--- page 19 ---
Numerical minimization yields the minimizing point (approx): x1 = 70.0, x2 = 20.0.
At this point:
d1^- = 0.0, d1^+ = 10.0
d2^- = 0.0, d3^- = 25.0
d4^- = 0.0, d4^+ = 0.0
Step 4: Priority 4 — minimize d1^+ without worsening higher priorities
Among points that achieve the minimal f3 value we selected one that minimizes d1^+. The final chosen
point above satisfies all priorities lexicographically.
Final decision variables: x1 = 70.0, x2 = 20.0.   ---------------(2 Marks)
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper da8898c1a82b

- Departments: Data Science
- Programmes: BTech DS 7009, Integrated DS 7038, MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_DS_7009/Optimization Methods/ANS_Optimization Methods(702BS0C079)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Optimization Methods
Date: 08 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figure on right hand side indicates full marks
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1. a
Aggie Power Generation has four generating stations S₁, S₂, S₃ and S₄ with annual available capacities (in
MW) 5, 8, 7 and 14 respectively. They supply three markets (destinations) D₁, D₂, D₃ whose annual demands
are 7, 9 and 18 MW respectively. The unit shipping costs ($/MW) from each station to each destination are
given below
D₁   D₂   D₃   Supply
S₁   2   7   4   5
S₂   3   3   1   8
S₃   5   4   7   7
S₄   1   6   2   14
Demand   7   9   18   34
Using the North-West Corner Method, determine an initial basic feasible solution for the Aggie Power
distribution problem and compute the total distribution cost.
Solution:
4 Marks
********** 1 **********
--- page 2 ---
1 Marks
Q1. b
Formulate the dual of the given primal problem.
Maximize Z = 6 x 1 + 4 x 2
subject to,
2 x 1 + 3 x 2  12
x 1 + x 2  6
x 1 + 4 x 2 = 8
x 1 , x 2  0
Solution:
Since objective function is maximizing, all ≥ constraints (2) can be converted to ≤ type by multiplying both
sides by -1
---------------------------------------------------(1 mark)
MAX zx = 6 x1 + 4 x2
subject to
2 x1 + 3 x2 ≤ 12
- x1 - x2 ≤ -6
x1 + 4 x2 = 8
and x1,x2≥0;
In primal, There are 2 variables and 3 constraints, so in dual there must be 2 constraints and 3 variables
In primal, The coefficient of objective function c1=6,c2=4 becomes right hand side constants in dual
In primal, The right hand side constants b1=12,b2=-6,b3=8 becomes coefficient of objective function in
dual
In primal, objective function is maximizing, so in dual objective function must be minimizing
Let y1,y2,y3 be the dual variables
Since 3rd constraint in the primal is equality, the corresponding dual variable y3 will be unrestricted in sign.
---------------------------------------------------(1 mark)
Dual is
MIN Zy = 12 y1 - 6 y2 + 8 y3
subject to
2 y1 - y2 + y3 ≥ 6
3 y1 - y2 + 4 y3 ≥ 4
and y1,y2≥0;y3 unrestricted in sign
------------------------------------(3 marks)
********** 2 **********
--- page 3 ---
Q1. c
State whether the game whose payoff matrix is given below is strictly determinable and fair. Also, determine
the value of the game.
Player B
B1   B2   B3   B4
A1   −5   −2   0   7
Player A   A2   5   −6   −4   8
A3   4   0   2   3
Solution:
Player B
B1   B2   B3   B4
A1   −5   −2   0   7   -5
Player A   A2   5   −6   −4   8   -6   3 Marks
A3   4   0   2   3   0
4   0   2   8
Maximin
Minimax
• As minimax=maximin, saddle point exits, it is strictly determinable
• A uses A3 strategy and B uses B2 strategy.   2 Marks
• Value of the gate is zero, it’s a fair game.
Q1. d
A sales representative has to travel to four major cities to meet clients and promote new products. He will
begin his journey from one city, visit each of the remaining cities exactly once, and finally return to the starting
city. The estimated travel cost (in thousand rupees) between every pair of cities is given in the table below.
A   B   C   D
A   -   15   20   10
B   25   -   35   15
C   5   25   -   20
D   10   20   12   -
He wants to plan his trip in the most economical way possible so that his total travel expense is minimized.
What should be the order in which the salesman visits the cities so that the total travel cost is minimized?
Solution:
Row operation   Column Operation
………………………(1 mark)   ………………………….(1 mark)
********** 3 **********
--- page 4 ---
Allocation
…………….(2 marks)
Optimal solution is A → B → D → C → A   ……………(1 Mark)
Q2. a
Solve the following two player game.
Player B
B₁   B₂   B₃   B₄
A₁   5   -10   9   0
Player A   A₂   6   7   8   1
A₃   8   7   15   1
A₄   3   4   -1   4
Solution:
Show that saddle point does not exists (maximin, minimax). ………………………(3 marks)
….1 marks   ……1 marks   ……1 marks
……1 marks
…….3 marks
Q2. b
A manufacturing company produces three types of portable LED lamps Model A, Model B, and Model C.
The profit obtained from the sale of each unit of Model A, Model B, and Model C is ₹30, ₹40, and ₹20
respectively. Each unit of the product requires processing time on a common machining line. The machining
********** 4 **********
--- page 5 ---
time required per unit is 10 minutes for Model A, 12 minutes for Model B, and 7 minutes for Model C. The
total available machining time per week is limited to 10,000 minutes. In addition, due to packaging and market
constraints, the total number of lamps (of all models together) that can be produced in a week cannot exceed
1,000 units.
Formulate and solve a Linear Programming Problem (LPP) to determine the number of units of each model
to be produced per week so that the total profit is maximized
Solution:
LPP formulation to maximize the profit:
Maximize Z = 30 x 1 + 40 x 2 + 20 x 3
subject to,
10 x 1 + 12 x 2 + 7 x 3  10000   ………………….(3 marks)
x 1 + x 2 + x 3  1000
x 1 , x 2 , x 3  0
Setting up the initial solution
And solving till iteration1 …………………………………………………………………….(3 marks)
Iteration 2 ………………………………….………………….(3 marks)
Final answer ………………….(1 marks)
Q3. a
Fresh Blend Beverages Pvt. Ltd. produces bottled juices at three factories in Dallas, Chicago, and Atlanta with
weekly capacities of 200, 160, and 90 crates respectively. They supply juices to three warehouses in New
York, Los Angeles, and Houston which require 180, 120, and 150 crates weekly. The unit shipping costs (in
dollars) are given in the table below.
Warehouse
Factory   New York Los Angeles Houston   Supply
Dallas   16   20   12   200
Chicago   14   8   18   160
Atlanta   26   24   16   90
********** 5 **********
--- page 6 ---
Demand   180   120   150   450
Determine the initial distribution for this company using the VAM method and check whether the obtained
solution is optimal using MODI method so that the total shipping cost is the minimum.
Solution:
1 mark   1 mark
1 mark   1 mark
IBFS VAM Solution : 120(8)+90(16)+12(60)+14(40)+16(140) = 5920   → 1 Mark
→ 1 Mark
→ 2 Marks
********** 6 **********
--- page 7 ---
→ 2 marks
Optimal value is 5920.. same as VAM
Q3. b
Mr Girish wants to invest Rs 10,000 in one of the three options A, B and C. The pay-off for his investment
depends on the nature of the economy (inflation, recession, or no change). The possible returns under each
economic situation are given below
Strategy   Nature of Economy
Inflation E1   Recession E2 No Change E3
S1   2000   1200   1500
S2   3000   800   1000
S3   2500   1000   1800
What course of action has he to take according to
(i) The pessimistic criterion (Maximin)
(ii) The equally likely criterion (Laplace)
(iii) The regret criterion.
(iv) Hurwicz criterion, the degree of optimism being 0.6.
Solution:
(i) Pessimistic criterion — Maximin
For each strategy find the minimum payoff across the states.
Strategy   Minimum
payoff (Rs)
A   1200
B   800
C   1000
Maximum among these minima = Rs 1200 for A.   --------------------(2 Marks)
(ii) Equally likely criterion — Laplace
Assume each state is equally likely (probability 1/3).
Strategy   Average payoff (Rs)
A   1566.67
B   1600.00
C   1766.67
The strategy with the largest average payoff is C.   --------------------(2 Marks)
********** 7 **********
--- page 8 ---
(iii) Regret criterion — Minimax regret
For each state (column) find the best payoff. Then compute regret = (best in state) − (actual payoff).
Strategy   Regret in   Regret in   Regret in No
Inflation (E1)   Recession (E2) change (E3) (Rs)
(Rs)   (Rs)
A   1000   0   300
B   0   400   800
C   500   200   0
For each strategy, the maximum regret (worst-case regret).
Strategy   Maximum
regret (Rs)
A   1000
B   800
C   500
The strategy with smallest maximum regret: C (max regret = Rs 500). ----------(3 Marks)
(iv) Hurwicz criterion — Degree of optimism α = 0.6
Hurwicz value = α*(maximum payoff) + (1−α)*(minimum payoff), where α = 0.6.
Strategy   Max payoff   Min payoff   Hurwicz value
(Rs)   (Rs)   (α=0.6)
A   2000   1200   1680.00
B   3000   800   2120.00
C   2500   1000   1900.00
Option B (highest Hurwicz value = Rs 2120.00).   ----------(3 Marks)
Q4. a
Solve the following LPP using the Big-M method to find the optimal cost.
Minimize Z = 500 x 1 + 200 x 2
subject to,
3 x 1 + 2 x 2  90
x 1  10
− 2 x 1 + x 2 = 0
x 1 , x 2  0
Solution:
Setting up the initial solution
And solving till iteration1 …………………………………..(4 marks)
Iteration 2 ………………………………….………………….(3 marks)
Iteration 3 ………………………………….………………….(2 marks)
********** 8 **********
--- page 9 ---
Iteration 1
Iteration 2
Iteration 3
Sol: x1=10, x2=20 and Z min=9000 ………………….(1 marks)
Q4. b
A company operates in five major territories and has five salesmen available for assignment. Each territory
differs in its sales potential, and each salesman has a different level of selling effectiveness. The estimated
annual sales that each salesman would generate in each territory are given in the table below:
Territories
A   B   C   D   E
1   32   38   40   28   40
2   40   24   28   21   36
Salesmen
3   41   27   33   30   37
4   22   38   41   36   36
5   29   33   40   35   39
Identify the best allocation of salesmen to territories so that the sales revenues are maximized.
Solution:
********** 9 **********
--- page 10 ---
As the given problem is of maximization type, it has to be converted to minimization type.
Minimization form
A B C D E
1 9   3   1 13 1
2 1 17 13 20 5
3 0 14 8 11 4
4 19 3   0   5 5
5 12 8   1   6 2
2 Marks
Row operation
A B C D E
1 8   2   0 12 0
2 0 16 12 19 4
3 0 14 8 11 4
4 19 3   0   5 5
5 11 7   0   5 1
1 mark
Column operation
A B C D E
1 8   0   0   7 0
2 0 14 12 14 4
3 0 12 8   6 4
4 19 1   0   0 5
5 11 5   0   0 1
1 mark
Allocation
A   B   C   D   E
1   8   0   0   7   0
2   0   14   12   14   4   ✓
3   0   12   8   6   4   ✓
4   19   1   0   0   5
5   11   5   0   0   1   ➔ 2 Marks
✓
Revised allocation (optimal)
A   B   C   D   E
1   12   0   0   7   0
2   0   10   8   10   0
3   0   8   4   2   0
4   23   1   0   0   5
5   15   5   0   0   1   ➔ 2 Marks
1→B, 2→A, 3→E, 4→C, 5→D   → 1 Mark
The associated maximum sales revenue is 38+40+37+41+35 = 191,000/-
********** 10 **********
--- page 11 ---
Q5. a
A bakery keeps stock of a popular brand of cake. Previous experience shows the daily demand pattern for the
item with associated probabilities, as given below
Daily Demand   0   10   20   30   40   50
Probability   0.01   0.20   0.15   0.50   0.12   0.02
Use the following sequence of random numbers to simulate the demand for next 10 days. Random numbers:
25, 39, 65, 76, 12, 05, 73, 89, 19, 49. Also estimate the daily average demand for the cakes on the basis of
the simulated data.
Solution:
The daily demand values and corresponding probabilities are:
Demand   Probability   Cumulative   Random number
probability   interval (00-99)
0   0.01   0.01   00 - 00
10   0.20   0.21   01 - 20
20   0.15   0.36   21 - 35
30   0.50   0.86   36 - 85
40   0.12   0.98   86 - 97
50   0.02   1.00   98 - 99
----------------(3 Marks)
Random numbers used (two-digit): 25, 39, 65, 76, 12, 05, 73, 89, 19, 49.
Simulation Table (10 days)
Day   Random number   Simulated demand (cakes)
1   25   20
2   39   30
3   65   30
4   76   30
5   12   10
6   05   10
7   73   30
8   89   40
9   19   10
10   49   30
-------------------(5 Marks)
Total demand over 10 days = 240 cakes.   -----------------(1 Mark)
Average daily demand = 240 / 10 = 24.00 cakes per day.   ------------------(1 Mark)
Q5. b
Solve the following Integer Linear Programming (ILP) problem using the Branch and Bound (Graphical)
method and determine the optimal integer solution.
Max z = 7 x 1 + 9 x 2
Subject to
− x 1 + 3 x 2  6
7 x 1 + x 2  35
x 2  7
x 1 , x 2 are non negative integers
********** 11 **********
--- page 12 ---
Solution:
……………(5 marks)
Branch at x1: x1<=4, x1>=5   …………………..(1mark)
Branch B solution …………………..(1mark)
Branch C solution …………………..(1mark)
Branch D solution …………………..(1mark)
Branch E solution …………………..(1mark)
********** 12 **********
--- page 13 ---
Q6. a
A fruit merchant purchases oranges at Rs 50 per basket and sells them at Rs 80. Unsold oranges are disposed
off at Rs 20 per basket the next day. Past record of sales for 120 days is as given below
Baskets Sold   15 16 17 18
No. of Days Sold 12 24 48 36
Using EMV, find how many baskets the merchant should purchase every day to maximize his profit.
Solution:
Here unsold baskets have a salvage value of Rs 20 each. Therefore, the loss per basket is 50-20 = 30.
Daily sales (D)   No. of days (out of 120)   Empirical probability
15   12   0.10
16   24   0.20
17   48   0.40
18   36   0.30
----------------(1 Mark)
********** 13 **********
--- page 14 ---
Thus the Profit = 30 (no. of baskets sold) - 30 (no. of baskets unsold)
Stock Q \ Demand D   15   16   17   18
Probability   0.1   0.2   0.4   0.3
15   Rs 450.00   Rs 450.00   Rs 450.00   Rs450.00
16   Rs 420.00   Rs 480.00   Rs 480.00   Rs 480.00
17   Rs 390.00   Rs 450.00   Rs 510.00   Rs 510.00
18   Rs 360.00   Rs 420.00   Rs 480.00   Rs 540.00
-------------------(2 Marks)
Stock Q EMV = Σ [Profit(Q,D) × P(D)]   EMV (Rs)
15   450*0.1 +450*0.2 +450*0.4+450*0.3 = 450   450
16   420*0.1 +480*0.2 +480*0.4+480*0.3 = 474   474
17   390*0.1 +450*0.2 +510*0.4+510*0.3 = 486   486
18   360*0.1 +420*0.2 +480*0.4+540*0.3 = 474   474
-------------------(1 Mark)
Since the highest EMV is 486, the course of action to be chosen is A3. Thus the merchant should
purchase 17 baskets every day.   -------------------(1 Mark)
Q6. b
A company produces motorcycle seats. The company has two production lines. The production rate for line 1
is 50 seats per hour and for line 2 it is 60 seats per hour. The company has entered into a contract to daily
supply 1,200 seats daily to another company. Currently, the normal operation period for each line is 8 hours.
The production manager of the company is trying to determine the best daily operation hours for the two lines.
He has set the priorities to achieve his goals, as given below:
P1: Produce and deliver 1,200 seats daily
P2: Limit the daily overtime operation hours of line 2 to 3 hours
P3: Minimize the underutilization of the regular daily operation hours of each line. Assign differential weights
based on the relative productivity rate.
P4: Minimize the daily overtime operation hours of each line as much as possible. Assign differential weights
based on the relative cost of overtime. It is assumed that the cost of operation is identical for the two production
lines.
Formulate this problem as a Goal Programming model.
Solution:
Let 𝑥1 𝑎𝑛𝑑 𝑥2 = daily operation hours for the lines 1 and 2, respectively.
It may be noted in this problem that the first criterion for determining the differential weights in the
third priority goal is the relative cost of overtime. The production rates ratio for the lines is 50 to 60.
Therefore, the relative cost resulting from an hour of overtime is greater for line 1 than for line 2. The
relative cost of overtime ratio for line 1 to line 2 will be line 6 to line 5. Second, the criterion for
determining the differential weights in the fourth priority goal is relative productivity rate. Since the
productivity of line 1 is 50 seats/ hour and of line 2 is 60 seats/hour, the productivity goals are weighted
for line 1 to line 2 as line 5 to line 6. The goal programming model for this problem can now be
formulated as follows ------(1 Mark)
Then the GP model is stated as follows:
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑4 + + 𝑃3(5𝑑2 −+ 6𝑑3 −) + 𝑃4(6𝑑2 + + 5𝑑3 +) ---------------(1 Mark)
********** 14 **********
--- page 15 ---
subject to the constraints
50𝑥1 + 60𝑥2 + 𝑑1 −−𝑑1 + = 1200
𝑥1 + 𝑑2 −−𝑑2 + = 8   ----------------(1 Mark)
𝑥2 + 𝑑3 −−𝑑3 + = 8
𝑥2 + 𝑑4 −−𝑑4 + = 11   ----------------(1 Mark)
and   𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑2 +, 𝑑3 −, 𝑑3 +, 𝑑4 −, 𝑑4 + ≥0. ----------------(1 Mark)
Q6. c
Given an Integer Linear Programming (ILP) problem with a relaxed optimal solution from the Simplex
method is shown below:
Max z = 2 x 1 + 5 x 2
Subject to
2 x 1 + 3 x 2  1, x 2  2,
x 1 , x 2 are non negative integers
CJ   2   5   0   0
B   CB XB   X1   X2   S1   S2
X2   5   0.3333   0.6667 1   0.3333 0
S2   0   1.6667   -0.6667 0   -0.3333 1
Z=1.6665   ZJ   3.3333 5   1.6667 0
CJ-ZJ   -1.3333 0   -1.6667 0
a) Construct first Gomory's fractional cut for the given non-integer optimal solution.
b) Illustrate the first iteration of Gomory’s cutting-plane method.
Determine the non-integer optimal solution after first Gomory’s cut.
Solution:
1. From Simplex solution:
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=0,x2=0.3333
Max Z=1.6667…………………….[02 Marks]
2. First iteration of Gomory’s cutting-plane method.
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut, with the help
of x2-row as follows:
0.3333=0.6667x1+1x2+0.3333S1
(0+0.3333)=(0+0.6667)x1+(1+0)x2+(0+0.3333)S1
The fractional cut will become
-0.3333=Sg1-0.6667x1-0.3333S1→ (Cut-1)
Adding this additional constraint at the bottom of optimal simplex table. The new table so obtained is
…………………….[02 Marks]
********** 15 **********
--- page 16 ---
…………………….[02 Marks]
Minimum negative XB is -0.3333 and its row index is 3. So, the leaving basis variable is Sg1.
Minimum positive ratio is 2 and its column index is 1. So, the entering variable is x1.
∴ The pivot element is -0.6667.
Entering =x1, Departing =Sg1, Key Element =-0.6667
R3(new)=R1(old) ÷(-0.6667)
R1(new)=R3(old) -(0.6667) R3(new)
R2(new)=R2(old) +(0.6667) R3(new)
…………………….[02 Marks]
3. Non-integer optimal solution after first Gomory’s cut
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=0.5,x2=0
Max Z=1…………………….[02 Marks]
********** 16 **********
--- page 17 ---
Q7. a
Distinguish between (i) Pure strategy and mixed strategy (ii) Zero-sum and non-zero-sum games.
Solution:
Pure Strategy   Mixed Strategy
A strategy in which a player consistently   A strategy in which a player randomly selects among two or
follows one specific course of action.   more pure strategies according to certain probabilities.
Deterministic (definite choice).   Probabilistic (involves randomization).
Opponent can predict the player’s move.   Opponent cannot easily predict the player’s move.
Used when one strategy always provides   Used when no pure strategy dominates; helps in achieving
the best payoff.   equilibrium.
3 Marks
Zero-Sum Game   Non-Zero-Sum Game
The gain of one player is exactly equal to   The gain or loss of one player does not necessarily equal
the loss of another.   the loss or gain of another.
Constant (sum of payoffs = 0).   Variable (sum of payoffs ≠ 0).
Purely competitive — one’s success means May involve both competition and cooperation.
another’s failure.
2 Marks
Q7. b
What is Monte Carlo simulation? Describe the idea of experimentation (Random sampling) in simulation.
Solution:
The monte Carlo simulation approach is used to incorporate the random behaviour of variable(s) of
interest in a model. A formal definition of Monte Carlo Simulation is as follows:
• The Monte Carlo simulation technique involves conducting repetitive experiments on the model of the
system under study, with some known probability distribution to draw random samples (observations)
using random numbers.
The Monte Carlo simulation approach consists of following steps:
1. Setting up a probability distribution for variables to be analysed.
2. Building a cumulative probability distribution for each random variable.
3. Generating random numbers and then assigning an appropriate set of random numbers to represent
value or range (interval) of values for each random variable.
4. Conducting the simulation experiment using random sampling.
5. Repeating Step 4 until the required number of simulation runs has been generated.
6. Designing and implementing a course of action and maintaining control. -------(4 Marks)
Random Number Generation: Monte Carlo simulation requires the generation of a sequence of random
numbers where
(i)   all numbers are equally likely, and
(ii)   no patterns appear in sequence of numbers. This sequence of random numbers helps in
choosing random observations (samples) from the probability distribution
-----------(1 Mark)
Q7. c
Use the Graphical Method to solve the following Goal Programming Problem.
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑4 + + 5𝑃3𝑑2 −+ 3𝑃3𝑑3 −+ 𝑃4𝑑1 +
subject to the constraints
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 80
********** 17 **********
--- page 18 ---
𝑥1 + 𝑑2 −= 70
𝑥2 + 𝑑3 −= 45
𝑥1 + 𝑥2 + 𝑑4 −−𝑑4 + = 90
𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑3 −, 𝑑4 −, 𝑑4 + ≥0.
Solution:
We assume the priority ordering (lexicographic): P1 (highest), then P2, then P3, then P4. If you have a
different priority ordering please tell me and I will recompute accordingly.
Step 1: Express deviational variables in x1,x2
d1^- = max(80 - (x1 + x2), 0)
d1^+ = max((x1 + x2) - 80, 0)
d2^- = max(70 - x1, 0)
d3^- = max(45 - x2, 0)
d4^- = max(90 - (x1 + x2), 0)
d4^+ = max((x1 + x2) - 90, 0)   ---------------(2 Marks)
Step 2: Priority 1 & 2 -> feasible strip
Minimizing d1^- requires x1 + x2 ≥ 80. Minimizing d4^+ requires x1 + x2 ≤ 90. Combined: 80 ≤ x1 + x2 ≤
90. We restrict attention to this strip for subsequent priorities.
Step 3: Minimize P3-term (5 d2^- + 3 d3^-) on the strip
We minimize f3(x1,x2) = 5·max(70-x1,0) + 3·max(45-x2,0) subject to 80 ≤ x1 + x2 ≤ 90. A numerical
search on a fine grid yields the minimum f3 value and the corresponding point shown in the contour plot
below.   ---------------(2 Marks)
---------------(4 Marks)
********** 18 **********
--- page 19 ---
Numerical minimization yields the minimizing point (approx): x1 = 70.0, x2 = 20.0.
At this point:
d1^- = 0.0, d1^+ = 10.0
d2^- = 0.0, d3^- = 25.0
d4^- = 0.0, d4^+ = 0.0
Step 4: Priority 4 — minimize d1^+ without worsening higher priorities
Among points that achieve the minimal f3 value we selected one that minimizes d1^+. The final chosen
point above satisfies all priorities lexicographically.
Final decision variables: x1 = 70.0, x2 = 20.0.   ---------------(2 Marks)
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 7ea36ff7c4d6

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CSE_DS_7057/Optimization Methods/ANS_Optimization Methods(702BS0C079)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 75.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Optimization Methods
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figure on right hand side indicates full marks
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1.a
A company operates three warehouses, S₁, S₂, and S₃, from which it distributes goods to four regional markets
located in D₁, D₂, D₃, and D₄. The transportation cost per unit (in ₹) from each warehouse to each market,
along with the supply available at each warehouse and the demand at each market, is given in the table below:
D₁   D₂   D₃   D₄   Supply
S₁   6   8   8   5   30
S₂   5   11   9   7   40
S₃   8   9   7   13   50
Demand   35   28   32   25   120
Apply the North-West Corner rule to find the basic feasible solution. Also, compute the total cost of this
transportation.
Solution:
4 Marks
1 Marks
********** 1 **********
--- page 2 ---
Q1.b
Formulate the dual of the given primal problem.
Minimize Z = 5 x 1 + 7 x 2
subject to,
3 x 1 + 2 x 2  10
x 1 + 4 x 2  12
2 x 1 + x 2 = 8
x 1 , x 2  0
Solution:
Since objective function is minimizing,
≤ constraints (2) can be converted to ≥ type by multipling both sides by -1
---------------------------------------------------(1 mark)
In primal, There are 2 variables and 3 constraints, so in dual there must be 2 constraints and 3 variables
In primal, The coefficient of objective function c1=5,c2=7 becomes right hand side constants in dual
In primal, The right hand side constants b1=10,b2=-12,b3=8 becomes coefficient of objective function in
dual
In primal, objective function is minimizing, so in dual objective function must be maximizing
Let y1,y2,y3 be the dual variables
Since 3rd constraint in the primal is equality, the corresponding dual variable y3 will be unrestricted in sign.
---------------------------------------------------(1 mark)
Dual is
MAX Zy = 10 y1 - 12 y2 + 8 y3
subject to
3 y1 - y2 + 2 y3 ≤ 5
2 y1 - 4 y2 + y3 ≤ 7
and y1,y2≥0;y3 unrestricted in sign
------------------------------------(3 marks)
Q1. c
State whether the game whose payoff matrix is given below is strictly determinable and fair. Also, find the
best course of action for player A and player B, and the value of the game.
Player B
B1   B2   B3   B4   B5
A1   -2   0   0   5   3
Player A   A2   3   2   1   2   2
A3   -4   -3   0   -2   6
A4   5   3   -4   2   -6
Solution:
********** 2 **********
--- page 3 ---
3 Marks
2 Marks
The game is strictly determinable and unfair.
Q1. d
The principal of a college has four peons, and four tasks have to be assigned to them. The peons differ in
efficiency and the tasks differ in their intrinsic difficulty. The time each peon would take to perform each task
is given in the following effectiveness matrix
Task   T1   T2   T3   T4
Peon
P1   18   26   17   11
P2   13   28   14   26
P3   38   19   18   15
P4   19   26   24   10
How should the tasks be allocated, one to each peon, to minimize the total peon hours?
Solution:
1 Mark
1 Mark
********** 3 **********
--- page 4 ---
1 Mark
2 Marks
P1→ T3, P2→T1, P3→T2, P4→T4
The optimal value equals 59.
Q2. a
Solve the following two-player game.
Player B
B₁   B₂   B₃   B₄
A₁   3   2   4   0
Player A   A₂   3   4   2   4
A₃   4   2   4   0
A₄   0   4   0   8
Solution:
Show that saddle point does not exists (maximin, minimax). ………………………(3 marks)
A1<A3, A3 dominate A1, delete A1   ………………..(1 mark)
B1> B3, B3 dominates B1, delete B1   …………………….(1 mark)
Avg(B3,B4)=B2, delete B2
………………..(1 Marks)
********** 4 **********
--- page 5 ---
…………………………(1 Marks)
…………………………..(3 Marks)
Q2. b
A furniture manufacturing company produces three types of products chairs (x₁), tables (x₂), and cupboards
(x₃). Each product requires time on two key resources: the carpentry section and the polishing section. The
time available per week in each section and the time required per unit of each product are given below
Resource   Chairs   Tables Cupboards   Available maximum
(x₁)   (x₂)   (x₃)   time
Carpentry (hours) 2   1   1   150
Polishing (hours)   3   1   2   70
The company earns profits of ₹10 per chair, ₹15 per table, and ₹8 per cupboard.
Formulate and solve a Linear Programming Problem (LPP) to determine how many units of each product
should be manufactured weekly to maximize total profit, without exceeding the available time in each
department.
Solution:
LPP formulation to maximize the profit:
Maximize Z = 10 x 1 + 15 x 2 + 8 x 3
subject to,
2 x 1 + x 2 + x 3  150   ………………….(3 marks)
3 x 1 + x 2 + 2 x 3  70
x 1 , x 2 , x 3  0
********** 5 **********
--- page 6 ---
Setting up the initial solution
And solving till iteration1 …………………………………………………………………….(3 marks)
Iteration 2 ………………………………….………………….(3 marks)
Final answer ………………….(1 marks)
Q3. a
A product is manufactured at four factories A, B, C and D. Their production capacities are 50, 70, 30 and 50
units, respectively. These factories supply the product to four stores, demands of which are 25, 35, 105 and
20 units respectively. Unit transportation cost in rupees from each factory to each store is given in the table
below:
Stores
Factories   I   II   III   IV
A   4   6   8   13
B   13   11   10   8
C   14   4   10   13
D   9   11   13   8
Determine the initial distribution using the VAM method and check whether the obtained solution is optimal
using MODI method so that the transportation cost is the minimum.
Solution:
It’s an unbalanced TP. Add dummy column
Stores
Factories   I   II   III IV V Supply
A   4   6   8   13 0   50
B   13 11 10   8   0   70   1 Marks
C   14 4   10 13 0   30
D   9 11 13   8   0   50
Demand 25 35 105 20 15   200
IBFS by VAM
3 Marks
100+30+160+700+120+195+160=1465
********** 6 **********
--- page 7 ---
Non degeneracy test
• Number of occupied cells = 7
1 Mark
• Compare with m+n−1=7
• Occupied cells = 7 → exactly equal to m+n−1
• Therefore, No degeneracy
Shadow prices
2 Marks
2 Marks
As all the values are positive, optimal solution is achieved
Total minimum cost is 1465/-
1 Mark
Q3. b
The following matrix gives the payoff (in Rs) of different strategies (alternatives) S1, S2 and S3 against
conditions (events) N1, N2, N3 and N4.
States of Nature
Strategy N1   N2   N3   N4
S1   4,000   -100   6,000   18,000
********** 7 **********
--- page 8 ---
S2   20,000   5,000   400   0
S3   20,000   15,000   -2000   1,000
Indicate the decision taken under the following approaches:
(i) The optimistic criterion (Maximax)
(ii) The equally likely criterion (Laplace)
(iii) The regret criterion.
(iv) Hurwicz criterion, the degree of optimism being 0.7.
Solution:
(i) Maximax (Optimistic criterion):
For each strategy compute the largest of the maxima (max of maxima).
Strategy   Calculation   Maximum payoff (Rs)
S1   max(4000, -100, 6000,   Rs 18,000
18000)
S2   max(20000, 5000, 400, 0)   Rs 20,000
S3   max(20000, 15000, -2000,   Rs 20,000
1000)
The highest payoff among these is Rs 20,000 achieved by S2, S3. -----------------(2 Marks)
(ii) Laplace (Equally likely criterion):
Compute the average payoff for each strategy (sum of payoffs divided by number of states). Choose the
strategy with the highest average (expected) payoff under equal probabilities.
Strategy   Sum of payoffs   Average payoff   Calculation
(Rs)   (Rs)
S1   Rs 27,900   Rs 6,975.00   (4000 -100 + 6000 + 18000) / 4 = 27900 / 4
= 6975.00
S2   Rs 25,400   Rs 6,350.00   (20000 + 5000 + 400 + 0) / 4 = 25400 / 4 =
6350.00
S3   Rs 34,000   Rs 8,500.00   (20000 + 15000 -2000 + 1000) / 4 = 34000
/ 4 = 8500.00
By Laplace choose strategy S3 (highest average Rs 8,500.00). ------------------(2 Marks)
(iii) Regret criterion — Minimax regret
For each strategy compute regret = (best payoff in that state) − (strategy payoff). Choose the strategy with
the smallest maximum regret (minimax regret).
Strategy   Regret in   Regret in   Regret in   Regret in   Max regret
N1 (Rs)   N2 (Rs)   N3 (Rs)   N4 (Rs)   (Rs)
S1   Rs 16,000 Rs 15,100 Rs 0   Rs 0   Rs 16,000
S2   Rs 0   Rs 10,000 Rs 5,600   Rs 18,000 Rs 18,000
S3   Rs 0   Rs 0   Rs 8,000   Rs 17,000 Rs 17,000
By Minimax regret, the strategy with smallest maximum regret: S1 (max regret = Rs 16,000).
--------------------(3 Marks)
********** 8 **********
--- page 9 ---
(iv) Hurwicz criterion (Degree of optimism α = 0.7)
Hurwicz value = α*(maximum payoff) + (1−α)*(minimum payoff).
Strategy Max payoff (Rs)   Min payoff (Rs) Hurwicz formula (α = 0.7)   Hurwicz value (Rs)
S1   Rs 18,000   Rs -100   0.7*(18,000) + 0.3*(-100)   Rs 12,570.00
S2   Rs 20,000   Rs 0   0.7*(20,000) + 0.3*(0)   Rs 14,000.00
S3   Rs 20,000   Rs -2,000   0.7*(20,000) + 0.3*(-2,000) Rs 13,400.00
By Hurwicz (α = 0.7), the strategy S2 (highest Hurwicz value = Rs 14,000.00).
--------------------(3 Marks)
Q4. a
Solve the following LPP to maximize the profit using Big-M method.
Maximize Z = 10 x 1 + 12 x 2
subject to,
x 1 + x 2 = 5
x 1  2
x 2  4
x 1 , x 2  0
Solution:
Setting up the initial solution
And solving till iteration1 …………………………………..(4 marks)
Iteration 2 ………………………………….………………….(3 marks)
Iteration 3 ………………………………….………………….(2 marks)
********** 9 **********
--- page 10 ---
Iteration 1
Iteration 2
Iteration 3
Final Sol: x1=2, x2=3 and Z max=56 ………………….(1 marks)
Q4. b
A company has 5 salesmen and 5 sales districts. Considering the capabilities of the salesmen and the nature
of the districts, the company manager estimates that sales per month (in hundred) for each salesman in each
district would be as follows.
Districts
A   B   C   D   E
1   40   40   35   25   50
2   42   30   16   25   27
Salesmen
3   50   48   40   60   50
4   20   19   20   18   25
5   58   60   59   55   53
Find the assignment of salesmen to districts that will result in the maximization of sales.
********** 10 **********
--- page 11 ---
Solution:
Maximization problem converted to minimization
2 Mark
Row operation
1 Marks
Column operatoin
1 Mark
Allocation and Marking
3 Marks
Revised final Matrix and allocation
2 Mark
1→E, 2→A, 3→D, 4→C, 5→B
1 Mark
The optimal assignment cost is 232
********** 11 **********
--- page 12 ---
Q5. a
A company manufactures 200 motor cycles per day. Depending upon the availability of raw materials and
other conditions, the daily production has been varying from 196 motor cycles to 204 motor cycles, whose
probability distribution is as given below:
Production 196   197   198   199   200   201   202   203   204
/Day
Probability 0.05   0.09   0.12   0.14   0.20   0.15   0.11   0.08   0.06
The motorcycles are transported in a specially designed three-storied lorry that can accommodate only 200
motorcycles. Using the following random numbers: 82, 89, 78, 24, 52, 53, 61, 18, 45, 04, 23, 50, 77, 27, 54,
10, simulate the process to find out:
(a) The average number of motorcycles waiting in the factory?
(b) The average number of empty spaces on the lorry?
Solution:
Depending on availability of raw materials, daily production varies from 196 to 204 motor cycles. The
probability distribution is:
Production/day   Probability   Cumulative   Random number
probability   interval (00-99)
196   0.05   0.05   00 - 04
197   0.09   0.14   05 - 13
198   0.12   0.26   14 - 25
199   0.14   0.40   26 - 39
200   0.20   0.60   40 - 59
201   0.15   0.75   60 - 74
202   0.11   0.86   75 - 85
203   0.08   0.94   86 - 93
204   0.06   1.00   94 - 99
------------------(3 Marks)
Given random numbers (two-digit): 82, 89, 78, 24, 53, 61, 18, 45, 04, 23, 50, 77, 27, 54, 10.
Simulation Table (15 days)
Day   Random   Production per   Motor cycles   Empty spaces
number   day   waiting in   in lorry (200
factory   capacity)
1   82   202   2   0
2   89   203   3   0
3   78   202   2   0
4   24   198   0   2
5   53   200   0   0
6   61   201   1   0
7   18   198   0   2
8   45   200   0   0
9   04   196   0   4
10   23   198   0   2
11   50   200   0   0
12   77   202   2   0
13   27   199   0   1
14   54   200   0   0
15   10   197   0   3
********** 12 **********
--- page 13 ---
-------------------(5 Marks)
Total motor cycles waiting (sum over 15 days) = 10.
Average number of motor cycles waiting in the factory = Total waiting / 15 = 10 / 15 = 0.6667 motor cycles
(≈ 0.667).   ----------------(1 Mark)
Total empty spaces in lorry (sum over 15 days) = 14.
Average number of empty spaces in the lorry = Total empty / 15 = 14 / 15 = 0.9333 spaces (≈ 0.933).
-----------------(1 Mark)
Q5. b
Solve the following Integer Linear Programming (ILP) problem using the Branch and Bound (Graphical)
method and determine the optimal integer solution.
Max z = 3 x 1 + 5 x 2
Subject to
2 x 1 + 4 x 2  25
x 1  8
x 2  5
x 1 , x 2 are non negative integers
Solution:
********** 13 **********
--- page 14 ---
2. To draw constraint x, <8 > Q)
Treat it as x, = 8

Here line is parallel to Y-axis
*1/8/8

%9/0)14

Put x; = 0.x) = 0 (origin) inx,; = 8, then 0 = 8, which is true,

The half plane containing the origin is the region of the solution set of the inequation x, = 8
3. To draw constraint x) < 5 + 3)

Treat it asx. =5

Here line is parallel to X-axis
x4/0)1

9/55

Put xy = 0, x9 = 0 (origin) in x = 5, then 0 = 5, which is true,

The half plane containing the origin is the region of the solution set of the inequation x = 5

TT + ox
1 6 7 8 8 0 1 12

FRR IC 7 I OH
--- page 15 ---
The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates || ines through Extreme Point

Objective function value
z= 3x, + 5x7

(%4.%)
4- xy 20
O(0, 0) 5+ x,20 3(0) + 5(0) = 0
27x,<8
A(8, 0) 5x, 20 3(8) + 5(0) = 24
1 = 2x; + 4x9 25
B(8, 2.25) 2x, <8 3(8) + 5(2.25) = 35.25
a 1 = 2x; + 4x, = 25 .
(2.5, 5) 3 xy<5 3(2.5) + 5(5) = 32.5
_ 34x<5
D(0, 5) 4+ x,20 3(0) + 5(5) = 25

The maximum value of the objective function z = 35.25 occurs at the extreme point (8, 2.25).

Hence, the optimal solution to the given LP problem is : x; = 8, xz = 2.25 and max z = 35.25.
..(5 Marks)

se eeeeeeeeeees (1 Marks)

Two branches: X2<=2 and X2>=3

Sub-problem B : Solution is found by adding x» < 2.
Solution steps by Big method, Graphical method
Max Z = 3X; + 5X2
subject to
2X4 + 4X2<25
x; <8
2X7<10
X7<2

and x1,x7 2 0;

Solution is
Max Zg = 34 (x; = 8,x2 = 2)

and Z, = 34 (x = 8,x = 2) obtainted by the rounded off solution values.
This Problem has integer solution, so no further branching is required.

FRR IC 7 DA HOH
--- page 16 ---
~T 2 x1
1 6 7 8 $$ © 1 12

xz

The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates || ines through Extreme Point

Objective function value

(4.29) z= 3x, + 5x2

0(0, 0) ; _ x ; ; 3(0) + 5(0) = 0
A(8, 0) ; _ x . ; 3(8) + 5(0) = 24
B(8, 2) : _ ' : : 3(8) + 5(2) = 34
(0, 2) : _ e : ; 3(0) + 5(2) = 10

The maximum value of the objective function z = 34 occurs at the extreme point (8, 2).

Hence, the optimal solution to the given LP problem is : x; = 8, x) = 2 and max z = 34.

Sub-problem C : Solution is found by adding x 2 3.
Solution steps by Big method, Graphical method
Max Z = 3x1 + 5X)
Subject to
ty + 4yye}5
My <8
2y<10
Xy33
and x1,%) 2 0;

Solution i
Max Zo = 345 (: = 65, 73)

and Z; = 33 (x, = 6.x) =3) obtained bythe rounded of soon values.

FRR ICR 7 6 AC OH

seeeeee(1.5 Marks)
--- page 17 ---
| N
NI

xit oxi
* 1 6 7 8 9 0 1 12
xz

The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates |Lines through Extreme Point

Objective function value

(4.9) Z = 3x1 + 5x2
4-4 x7,23
A(0, 3) 5x20 3(0) + 5(3) = 15
34 x2<5
B(O, 5) 5 x,20 3(0) + 5(5) = 25
1 — 2x, + 4x = 25
C(2.5, 5) 3x <5 3(2.5) + 5(5) = 32.5
1 2x, + 4x 525
D(6.5, 3) 3(6.5) + 5(3) = 34.5

4x23

The maximum value of the objective function Z = 34.5 occurs at the extreme point (6.5, 3).

Hence, the optimal solution to the given LP problem is : x; = 6.5, x = 3 and max Z = 34.5.
++ee(1.5 Marks)

The branch and bound diagram

ak 2

Xy = 8,x2=2
Zn=34
Zp=34

|Solution steps by|

BigM method,
Graphical method

FRR ICR] AC OH
--- page 18 ---
As x2>=3 (branch B) will not yield IP solution more than 34
……..(1 Marks)
Q6. a
A shopkeeper buys a vegetable puff at Rs 2 and sells it at Rs 5. Unsold puffs are given to poor people free of
cost. The following are the sales details during the past 100 days.
Daily Sales of Puffs 10   11   12   13
No. of Days Sold   15   20   40   25
Apply EMV criterion to determine how many puffs the shopkeeper has to stock every day to maximize his
profit.
Solution:
From the past 100 days the sales distribution is:
Daily sales (D)   No. of days (out of 100)   Empirical probability
10   15   0.15
11   20   0.20
12   40   0.40
13   25   0.25
----------------(1 Mark)
Revenue = selling price × min(Q, D).
Cost = cost price × Q (all stocked items are purchased).
Profit = Revenue − Cost = 5×min(Q,D) − 2×Q (in Rs).
Stock Q \ Demand D 10   11   12   13
10   Rs 30.00   Rs 30.00   Rs 30.00   Rs 30.00
11   Rs 28.00   Rs 33.00   Rs 33.00   Rs 33.00
12   Rs 26.00   Rs 31.00   Rs 36.00   Rs 36.00
13   Rs 24.00   Rs 29.00   Rs 34.00   Rs 39.00
-------------------(2 Marks)
Stock Q EMV = Σ [Profit(Q,D) × P(D)]   EMV (Rs)
10   (30.00×0.15) + (30.00×0.20) + (30.00×0.40) +   Rs 30.00
(30.00×0.25)
11   (28.00×0.15) + (33.00×0.20) + (33.00×0.40) +   Rs 32.25
(33.00×0.25)
12   (26.00×0.15) + (31.00×0.20) + (36.00×0.40) +   Rs 33.50
(36.00×0.25)
13   (24.00×0.15) + (29.00×0.20) + (34.00×0.40) +   Rs 32.75
(39.00×0.25)
-------------------(1 Mark)
The EMVs show that stocking Q = 12 puffs yields the highest expected daily profit of Rs 33.50.
-------------------(1 Mark)
********** 18 **********
--- page 19 ---
Q6. b
A firm produces two products A and B. Each product must be processed through two departments namely 1
and 2. Department 1 has 30 hours of production capacity per day, and department 2 has 60 hours. Each unit
of product A requires 2 hours in department 1 and 6 hours in department 2. Each unit of product B requires 3
hours in department 1 and 4 hours in department 2. Management has rank ordered the following goals it would
like to achieve in determining the daily product mix:
P1: Minimize the underachievement of joint total production of 10 units.
P2: Minimize the underachievement of producing 7 units of product B.
P3: Minimize the underachievement of producing 8 units of product A.
Formulate this problem as a Goal Programming model.
Solution:
Let 𝑥1 𝑎𝑛𝑑 𝑥2 = number of units of products A and B produced, respectively
𝑑𝑖 −, 𝑑𝑖 += underachievement and overachievement associated with goal i, respectively.
----------------(1 Mark)
Then the GP model is stated as follows:
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑3 − + 𝑃3𝑑2 −   ----------------(1 Mark)
subject to the constraints
2𝑥1 + 3𝑥2 ≤30
6𝑥1 + 4𝑥2 ≤60   ----------------(1 Mark)
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 10
𝑥1 + 𝑑2 −−𝑑2 + = 8   ----------------(1 Mark)
𝑥1 + 𝑑3 −−𝑑3 + = 7
and   𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑2 +, 𝑑3 −, 𝑑3 + ≥0.   ----------------(1 Mark)
Q6. c
Given an Integer Linear Programming (ILP) problem with a relaxed optimal solution from the Simplex method
is shown below:
Max z = x 1 + 3 x 2
Subject to
x 1 + 2 x 2  1; x 2  2; x 1 & x 2 are non negative integers
CJ   1   3   0   0
B   CB XB   X1   X2   S1   S2
X2   3   0.5   0.5   1   0.5   0
S2   0   1.5   -0.5   0   -0.5   1
Z=1.5   ZJ   1.5   3   1.5   0
CJ-ZJ   -0.5   0   -1.5   0
a) Construct first Gomory's fractional cut for the given non-integer optimal solution.
b) Demonstrate the first iteration of Gomory’s cutting-plane method.
Identify the integer optimal solution
Solution:
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
********** 19 **********
--- page 20 ---
x1=0,x2=0.5
Max Z=1.5   …………………….[01 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut, with the help
of x2-row as follows:
0.5=0.5x1+1x2+0.5S1
(0+0.5)=(0+0.5)x1+(1+0)x2+(0+0.5)S1
The factional cut will become
-0.5=Sg1-0.5x1-0.5S1→ (Cut-1)   …………………….[03 Marks]
………[02 Marks]
Minimum negative XB is -0.5 and its row index is 3. So, the leaving basis variable is Sg1.
Minimum positive ratio is 1 and its column index is 1. So, the entering variable is x1.
∴ The pivot element is -0.5.
Entering =x1, Departing =Sg1, Key Element =-0.5
R3(new)=R3(old) ÷(-0.5)
R1(new)=R1(old) -(-0.5) R3(new)
R2(new)=R2(old) +(-0.5) R3(new
…………………….[02 Marks]
Identify the integer optimal solution
********** 20 **********
--- page 21 ---
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as:
x1=1,x2=0
Max Z=1
The integer optimal solution found after 1st cut.   …………………….[02 Marks]
Q7. a
Distinguish between deterministic and probabilistic games. What approaches do you apply to solve each of
them?
Solution:
Deterministic Games   Probabilistic games
If the game yields a solution with one certain,   If a player adopts more than one strategy with
single strategy (pure strategy) for each some probabilities or prepares a blend of two
player, the game is deterministic.   or more strategies, these games are said to be
probabilistic.
In this game the strategies are pure and Here, mixed strategies are used as no saddle
saddle points exist.   points exist.
………………………………………….3 marks
Approaches for Deterministic Games:
• Solved using the minimax approach, where players choose strategies to minimize maximum loss
and maximize minimum gain.
• The dominance principle is also used to eliminate inferior strategies and identify the optimal one.
Approaches for Probabilistic Games:
• Solved using the arithmetic (expected value) approach, where payoffs are multiplied by their
probabilities to find the best average outcome.
•   Probability and decision theory help evaluate uncertain outcomes and guide rational choices under
risk.
………………………………………….2 marks
Q7. b
What are the advantages and limitations of Simulation models?
Solution:
Advantages
1. This approach is suitable to analyse large and complex real-life problems that cannot be solved by the
analytical methods.
2. It facilitates to study the interactive system variables, and the effect of changes that take place in
these variables, on the system performance in order to determine the desired result.
3. Simulation experiments are done on the model, not on the system itself. Experimentation takes into
consideration additional information during analysis that most quantitative models do not permit. In
other words, simulation can be used to ‘experiment’ on a model of a real situation, without incurring the
costs of operating on the system.
4. Simulation can be used as a pre-service test to try out new policies and decision rules for operating a
system before running the risk of experimentation in the real system.
------------------(3 Marks)
********** 21 **********
--- page 22 ---
Disadvantages
1. Simulation models are expensive and take a long time to develop. For example, a corporate planning
model may take a long time to develop and may also prove to be expensive.
2. It is the trial and error approach that produces different solutions in repeated runs. This means it does
not generate optimal solutions to problems.
3. The simulation model does not produce answers by itself. The user has to provide all the constraints
for the solutions that he wants to examine.   ---------------(2 Marks)
Q7. c
Use Graphical Method to solve the following Goal Programming Problem.
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2(2𝑑2 −+ 𝑑3 −) + 𝑃3𝑑1 +
subject to the constraints
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 400
𝑥1 + 𝑑2 −= 240
𝑥1 + 𝑑3 −= 300
𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑3 −≥0.
Solution:
Goal 1: Make 𝑥1 + 𝑥2 as close to 400 as possible (𝑑1 − is shortfall, 𝑑1 + is excess).
Goal 2: Make 𝑥1 close to 240 (𝑑2 −captures shortfall).
Goal 3: Make 𝑥1 close to 300 (𝑑3 −captures shortfall).
We solve by following the priorities in order (P1 highest priority, then P2, then P3).
Priority 1: Minimize 𝑑1 − (avoid shortfall on goal 1)
To minimize 𝑑1 −, choose 𝑑1 −= 0 if possible. With 𝑑1 −= 0 the first constraint becomes:
𝑥1 + 𝑥2 −𝑑1 + = 400 → 𝑥1 + 𝑥2 −400 = 𝑑1 +. (So for 𝑑1 −= 0 we must have 𝑥1 + 𝑥2 ≥400)
---------------(2 Marks)
Priority 2: Minimize 2𝑑2 −+ 𝑑3 −
From constraints 2 and 3 we have: 𝑑2 −= 240 −𝑥1 and 𝑑3 −= 300 −𝑥1 (both ≥ 0).
Hence 2𝑑2 −+ 𝑑3 − = 2(240 −𝑥1) + (300 −𝑥1) = 780 − 3 𝑥1.
But 𝑑2 − ≥ 0 requires 𝑥1 ≤ 240. Therefore, the maximum feasible 𝑥1 is 𝑥1 = 240.
Set 𝑥1 = 240 to optimally reduce the P2-term, that gives 𝑑2 − = 0 and 𝑑3 − = 60.
At this stage the first constraint (with 𝑑1 − = 0) becomes 𝑥1 + 𝑥2 −𝑑1 + = 400→ 240 + 𝑥2 −𝑑1 + = 400 →
𝑑1 + = 𝑥2 −160.
So to keep 𝑑1 + small we should choose 𝑥2 as small as possible that gives 𝑥2 ≥160
-----------(2 Marks)
Priority 3: Minimize 𝑑1 +
With 𝑥1 = 240, we choose the smallest feasible 𝑥2, i.e. 𝑥2 = 160, to minimize 𝑑1 + = 𝑥2 −160 = 0.
Thus,   𝑥1 = 240, 𝑥2 = 160
𝑑1 − = 0, 𝑑1 + = 0
𝑑2 −= 0, 𝑑3 − = 60   ---------------(2 Marks)
Objective value (in terms of deviational variables): 𝑍= 𝑃1𝑑1 −+ 𝑃2(2𝑑2 −+ 𝑑3 −) + 𝑃3𝑑1 + = 60·𝑃2.
The line 𝑥1 + 𝑥2 = 400 and the vertical line 𝑥1 = 240 Their intersection at (240,160) is the corner point
found by the priority procedure.
********** 22 **********
--- page 23 ---
Graphical sketch: lines x1 + x2 = 400 and x1 = 240
Feasible corner for lexicographic solution: (240,160)

2507

200+ (240, 160)

\

150F
100;

50F

0 50 100 150 200 250 300
xl

(4 Marks)
Graph for reference

X2
400

240 0

oS to }240 | 160
iJ an 100 © 300

FIR ICR 2 I OH
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 7258464ed0e9

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_DS_7009/Optimization Methods/ANS_Optimization Methods(702BS0C079)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 75.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Optimization Methods
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figure on right hand side indicates full marks
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1.a
A company operates three warehouses, S₁, S₂, and S₃, from which it distributes goods to four regional markets
located in D₁, D₂, D₃, and D₄. The transportation cost per unit (in ₹) from each warehouse to each market,
along with the supply available at each warehouse and the demand at each market, is given in the table below:
D₁   D₂   D₃   D₄   Supply
S₁   6   8   8   5   30
S₂   5   11   9   7   40
S₃   8   9   7   13   50
Demand   35   28   32   25   120
Apply the North-West Corner rule to find the basic feasible solution. Also, compute the total cost of this
transportation.
Solution:
4 Marks
1 Marks
********** 1 **********
--- page 2 ---
Q1.b
Formulate the dual of the given primal problem.
Minimize Z = 5 x 1 + 7 x 2
subject to,
3 x 1 + 2 x 2  10
x 1 + 4 x 2  12
2 x 1 + x 2 = 8
x 1 , x 2  0
Solution:
Since objective function is minimizing,
≤ constraints (2) can be converted to ≥ type by multipling both sides by -1
---------------------------------------------------(1 mark)
In primal, There are 2 variables and 3 constraints, so in dual there must be 2 constraints and 3 variables
In primal, The coefficient of objective function c1=5,c2=7 becomes right hand side constants in dual
In primal, The right hand side constants b1=10,b2=-12,b3=8 becomes coefficient of objective function in
dual
In primal, objective function is minimizing, so in dual objective function must be maximizing
Let y1,y2,y3 be the dual variables
Since 3rd constraint in the primal is equality, the corresponding dual variable y3 will be unrestricted in sign.
---------------------------------------------------(1 mark)
Dual is
MAX Zy = 10 y1 - 12 y2 + 8 y3
subject to
3 y1 - y2 + 2 y3 ≤ 5
2 y1 - 4 y2 + y3 ≤ 7
and y1,y2≥0;y3 unrestricted in sign
------------------------------------(3 marks)
Q1. c
State whether the game whose payoff matrix is given below is strictly determinable and fair. Also, find the
best course of action for player A and player B, and the value of the game.
Player B
B1   B2   B3   B4   B5
A1   -2   0   0   5   3
Player A   A2   3   2   1   2   2
A3   -4   -3   0   -2   6
A4   5   3   -4   2   -6
Solution:
********** 2 **********
--- page 3 ---
3 Marks
2 Marks
The game is strictly determinable and unfair.
Q1. d
The principal of a college has four peons, and four tasks have to be assigned to them. The peons differ in
efficiency and the tasks differ in their intrinsic difficulty. The time each peon would take to perform each task
is given in the following effectiveness matrix
Task   T1   T2   T3   T4
Peon
P1   18   26   17   11
P2   13   28   14   26
P3   38   19   18   15
P4   19   26   24   10
How should the tasks be allocated, one to each peon, to minimize the total peon hours?
Solution:
1 Mark
1 Mark
********** 3 **********
--- page 4 ---
1 Mark
2 Marks
P1→ T3, P2→T1, P3→T2, P4→T4
The optimal value equals 59.
Q2. a
Solve the following two-player game.
Player B
B₁   B₂   B₃   B₄
A₁   3   2   4   0
Player A   A₂   3   4   2   4
A₃   4   2   4   0
A₄   0   4   0   8
Solution:
Show that saddle point does not exists (maximin, minimax). ………………………(3 marks)
A1<A3, A3 dominate A1, delete A1   ………………..(1 mark)
B1> B3, B3 dominates B1, delete B1   …………………….(1 mark)
Avg(B3,B4)=B2, delete B2
………………..(1 Marks)
********** 4 **********
--- page 5 ---
…………………………(1 Marks)
…………………………..(3 Marks)
Q2. b
A furniture manufacturing company produces three types of products chairs (x₁), tables (x₂), and cupboards
(x₃). Each product requires time on two key resources: the carpentry section and the polishing section. The
time available per week in each section and the time required per unit of each product are given below
Resource   Chairs   Tables Cupboards   Available maximum
(x₁)   (x₂)   (x₃)   time
Carpentry (hours) 2   1   1   150
Polishing (hours)   3   1   2   70
The company earns profits of ₹10 per chair, ₹15 per table, and ₹8 per cupboard.
Formulate and solve a Linear Programming Problem (LPP) to determine how many units of each product
should be manufactured weekly to maximize total profit, without exceeding the available time in each
department.
Solution:
LPP formulation to maximize the profit:
Maximize Z = 10 x 1 + 15 x 2 + 8 x 3
subject to,
2 x 1 + x 2 + x 3  150   ………………….(3 marks)
3 x 1 + x 2 + 2 x 3  70
x 1 , x 2 , x 3  0
********** 5 **********
--- page 6 ---
Setting up the initial solution
And solving till iteration1 …………………………………………………………………….(3 marks)
Iteration 2 ………………………………….………………….(3 marks)
Final answer ………………….(1 marks)
Q3. a
A product is manufactured at four factories A, B, C and D. Their production capacities are 50, 70, 30 and 50
units, respectively. These factories supply the product to four stores, demands of which are 25, 35, 105 and
20 units respectively. Unit transportation cost in rupees from each factory to each store is given in the table
below:
Stores
Factories   I   II   III   IV
A   4   6   8   13
B   13   11   10   8
C   14   4   10   13
D   9   11   13   8
Determine the initial distribution using the VAM method and check whether the obtained solution is optimal
using MODI method so that the transportation cost is the minimum.
Solution:
It’s an unbalanced TP. Add dummy column
Stores
Factories   I   II   III IV V Supply
A   4   6   8   13 0   50
B   13 11 10   8   0   70   1 Marks
C   14 4   10 13 0   30
D   9 11 13   8   0   50
Demand 25 35 105 20 15   200
IBFS by VAM
3 Marks
100+30+160+700+120+195+160=1465
********** 6 **********
--- page 7 ---
Non degeneracy test
• Number of occupied cells = 7
1 Mark
• Compare with m+n−1=7
• Occupied cells = 7 → exactly equal to m+n−1
• Therefore, No degeneracy
Shadow prices
2 Marks
2 Marks
As all the values are positive, optimal solution is achieved
Total minimum cost is 1465/-
1 Mark
Q3. b
The following matrix gives the payoff (in Rs) of different strategies (alternatives) S1, S2 and S3 against
conditions (events) N1, N2, N3 and N4.
States of Nature
Strategy N1   N2   N3   N4
S1   4,000   -100   6,000   18,000
********** 7 **********
--- page 8 ---
S2   20,000   5,000   400   0
S3   20,000   15,000   -2000   1,000
Indicate the decision taken under the following approaches:
(i) The optimistic criterion (Maximax)
(ii) The equally likely criterion (Laplace)
(iii) The regret criterion.
(iv) Hurwicz criterion, the degree of optimism being 0.7.
Solution:
(i) Maximax (Optimistic criterion):
For each strategy compute the largest of the maxima (max of maxima).
Strategy   Calculation   Maximum payoff (Rs)
S1   max(4000, -100, 6000,   Rs 18,000
18000)
S2   max(20000, 5000, 400, 0)   Rs 20,000
S3   max(20000, 15000, -2000,   Rs 20,000
1000)
The highest payoff among these is Rs 20,000 achieved by S2, S3. -----------------(2 Marks)
(ii) Laplace (Equally likely criterion):
Compute the average payoff for each strategy (sum of payoffs divided by number of states). Choose the
strategy with the highest average (expected) payoff under equal probabilities.
Strategy   Sum of payoffs   Average payoff   Calculation
(Rs)   (Rs)
S1   Rs 27,900   Rs 6,975.00   (4000 -100 + 6000 + 18000) / 4 = 27900 / 4
= 6975.00
S2   Rs 25,400   Rs 6,350.00   (20000 + 5000 + 400 + 0) / 4 = 25400 / 4 =
6350.00
S3   Rs 34,000   Rs 8,500.00   (20000 + 15000 -2000 + 1000) / 4 = 34000
/ 4 = 8500.00
By Laplace choose strategy S3 (highest average Rs 8,500.00). ------------------(2 Marks)
(iii) Regret criterion — Minimax regret
For each strategy compute regret = (best payoff in that state) − (strategy payoff). Choose the strategy with
the smallest maximum regret (minimax regret).
Strategy   Regret in   Regret in   Regret in   Regret in   Max regret
N1 (Rs)   N2 (Rs)   N3 (Rs)   N4 (Rs)   (Rs)
S1   Rs 16,000 Rs 15,100 Rs 0   Rs 0   Rs 16,000
S2   Rs 0   Rs 10,000 Rs 5,600   Rs 18,000 Rs 18,000
S3   Rs 0   Rs 0   Rs 8,000   Rs 17,000 Rs 17,000
By Minimax regret, the strategy with smallest maximum regret: S1 (max regret = Rs 16,000).
--------------------(3 Marks)
********** 8 **********
--- page 9 ---
(iv) Hurwicz criterion (Degree of optimism α = 0.7)
Hurwicz value = α*(maximum payoff) + (1−α)*(minimum payoff).
Strategy Max payoff (Rs)   Min payoff (Rs) Hurwicz formula (α = 0.7)   Hurwicz value (Rs)
S1   Rs 18,000   Rs -100   0.7*(18,000) + 0.3*(-100)   Rs 12,570.00
S2   Rs 20,000   Rs 0   0.7*(20,000) + 0.3*(0)   Rs 14,000.00
S3   Rs 20,000   Rs -2,000   0.7*(20,000) + 0.3*(-2,000) Rs 13,400.00
By Hurwicz (α = 0.7), the strategy S2 (highest Hurwicz value = Rs 14,000.00).
--------------------(3 Marks)
Q4. a
Solve the following LPP to maximize the profit using Big-M method.
Maximize Z = 10 x 1 + 12 x 2
subject to,
x 1 + x 2 = 5
x 1  2
x 2  4
x 1 , x 2  0
Solution:
Setting up the initial solution
And solving till iteration1 …………………………………..(4 marks)
Iteration 2 ………………………………….………………….(3 marks)
Iteration 3 ………………………………….………………….(2 marks)
********** 9 **********
--- page 10 ---
Iteration 1
Iteration 2
Iteration 3
Final Sol: x1=2, x2=3 and Z max=56 ………………….(1 marks)
Q4. b
A company has 5 salesmen and 5 sales districts. Considering the capabilities of the salesmen and the nature
of the districts, the company manager estimates that sales per month (in hundred) for each salesman in each
district would be as follows.
Districts
A   B   C   D   E
1   40   40   35   25   50
2   42   30   16   25   27
Salesmen
3   50   48   40   60   50
4   20   19   20   18   25
5   58   60   59   55   53
Find the assignment of salesmen to districts that will result in the maximization of sales.
********** 10 **********
--- page 11 ---
Solution:
Maximization problem converted to minimization
2 Mark
Row operation
1 Marks
Column operatoin
1 Mark
Allocation and Marking
3 Marks
Revised final Matrix and allocation
2 Mark
1→E, 2→A, 3→D, 4→C, 5→B
1 Mark
The optimal assignment cost is 232
********** 11 **********
--- page 12 ---
Q5. a
A company manufactures 200 motor cycles per day. Depending upon the availability of raw materials and
other conditions, the daily production has been varying from 196 motor cycles to 204 motor cycles, whose
probability distribution is as given below:
Production 196   197   198   199   200   201   202   203   204
/Day
Probability 0.05   0.09   0.12   0.14   0.20   0.15   0.11   0.08   0.06
The motorcycles are transported in a specially designed three-storied lorry that can accommodate only 200
motorcycles. Using the following random numbers: 82, 89, 78, 24, 52, 53, 61, 18, 45, 04, 23, 50, 77, 27, 54,
10, simulate the process to find out:
(a) The average number of motorcycles waiting in the factory?
(b) The average number of empty spaces on the lorry?
Solution:
Depending on availability of raw materials, daily production varies from 196 to 204 motor cycles. The
probability distribution is:
Production/day   Probability   Cumulative   Random number
probability   interval (00-99)
196   0.05   0.05   00 - 04
197   0.09   0.14   05 - 13
198   0.12   0.26   14 - 25
199   0.14   0.40   26 - 39
200   0.20   0.60   40 - 59
201   0.15   0.75   60 - 74
202   0.11   0.86   75 - 85
203   0.08   0.94   86 - 93
204   0.06   1.00   94 - 99
------------------(3 Marks)
Given random numbers (two-digit): 82, 89, 78, 24, 53, 61, 18, 45, 04, 23, 50, 77, 27, 54, 10.
Simulation Table (15 days)
Day   Random   Production per   Motor cycles   Empty spaces
number   day   waiting in   in lorry (200
factory   capacity)
1   82   202   2   0
2   89   203   3   0
3   78   202   2   0
4   24   198   0   2
5   53   200   0   0
6   61   201   1   0
7   18   198   0   2
8   45   200   0   0
9   04   196   0   4
10   23   198   0   2
11   50   200   0   0
12   77   202   2   0
13   27   199   0   1
14   54   200   0   0
15   10   197   0   3
********** 12 **********
--- page 13 ---
-------------------(5 Marks)
Total motor cycles waiting (sum over 15 days) = 10.
Average number of motor cycles waiting in the factory = Total waiting / 15 = 10 / 15 = 0.6667 motor cycles
(≈ 0.667).   ----------------(1 Mark)
Total empty spaces in lorry (sum over 15 days) = 14.
Average number of empty spaces in the lorry = Total empty / 15 = 14 / 15 = 0.9333 spaces (≈ 0.933).
-----------------(1 Mark)
Q5. b
Solve the following Integer Linear Programming (ILP) problem using the Branch and Bound (Graphical)
method and determine the optimal integer solution.
Max z = 3 x 1 + 5 x 2
Subject to
2 x 1 + 4 x 2  25
x 1  8
x 2  5
x 1 , x 2 are non negative integers
Solution:
********** 13 **********
--- page 14 ---
2. To draw constraint x, <8 > Q)
Treat it as x, = 8

Here line is parallel to Y-axis
*1/8/8

%9/0)14

Put x; = 0.x) = 0 (origin) inx,; = 8, then 0 = 8, which is true,

The half plane containing the origin is the region of the solution set of the inequation x, = 8
3. To draw constraint x) < 5 + 3)

Treat it asx. =5

Here line is parallel to X-axis
x4/0)1

9/55

Put xy = 0, x9 = 0 (origin) in x = 5, then 0 = 5, which is true,

The half plane containing the origin is the region of the solution set of the inequation x = 5

TT + ox
1 6 7 8 8 0 1 12

FRR IC 7 I OH
--- page 15 ---
The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates || ines through Extreme Point

Objective function value
z= 3x, + 5x7

(%4.%)
4- xy 20
O(0, 0) 5+ x,20 3(0) + 5(0) = 0
27x,<8
A(8, 0) 5x, 20 3(8) + 5(0) = 24
1 = 2x; + 4x9 25
B(8, 2.25) 2x, <8 3(8) + 5(2.25) = 35.25
a 1 = 2x; + 4x, = 25 .
(2.5, 5) 3 xy<5 3(2.5) + 5(5) = 32.5
_ 34x<5
D(0, 5) 4+ x,20 3(0) + 5(5) = 25

The maximum value of the objective function z = 35.25 occurs at the extreme point (8, 2.25).

Hence, the optimal solution to the given LP problem is : x; = 8, xz = 2.25 and max z = 35.25.
..(5 Marks)

se eeeeeeeeeees (1 Marks)

Two branches: X2<=2 and X2>=3

Sub-problem B : Solution is found by adding x» < 2.
Solution steps by Big method, Graphical method
Max Z = 3X; + 5X2
subject to
2X4 + 4X2<25
x; <8
2X7<10
X7<2

and x1,x7 2 0;

Solution is
Max Zg = 34 (x; = 8,x2 = 2)

and Z, = 34 (x = 8,x = 2) obtainted by the rounded off solution values.
This Problem has integer solution, so no further branching is required.

FRR IC 7 DA HOH
--- page 16 ---
~T 2 x1
1 6 7 8 $$ © 1 12

xz

The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates || ines through Extreme Point

Objective function value

(4.29) z= 3x, + 5x2

0(0, 0) ; _ x ; ; 3(0) + 5(0) = 0
A(8, 0) ; _ x . ; 3(8) + 5(0) = 24
B(8, 2) : _ ' : : 3(8) + 5(2) = 34
(0, 2) : _ e : ; 3(0) + 5(2) = 10

The maximum value of the objective function z = 34 occurs at the extreme point (8, 2).

Hence, the optimal solution to the given LP problem is : x; = 8, x) = 2 and max z = 34.

Sub-problem C : Solution is found by adding x 2 3.
Solution steps by Big method, Graphical method
Max Z = 3x1 + 5X)
Subject to
ty + 4yye}5
My <8
2y<10
Xy33
and x1,%) 2 0;

Solution i
Max Zo = 345 (: = 65, 73)

and Z; = 33 (x, = 6.x) =3) obtained bythe rounded of soon values.

FRR ICR 7 6 AC OH

seeeeee(1.5 Marks)
--- page 17 ---
| N
NI

xit oxi
* 1 6 7 8 9 0 1 12
xz

The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates |Lines through Extreme Point

Objective function value

(4.9) Z = 3x1 + 5x2
4-4 x7,23
A(0, 3) 5x20 3(0) + 5(3) = 15
34 x2<5
B(O, 5) 5 x,20 3(0) + 5(5) = 25
1 — 2x, + 4x = 25
C(2.5, 5) 3x <5 3(2.5) + 5(5) = 32.5
1 2x, + 4x 525
D(6.5, 3) 3(6.5) + 5(3) = 34.5

4x23

The maximum value of the objective function Z = 34.5 occurs at the extreme point (6.5, 3).

Hence, the optimal solution to the given LP problem is : x; = 6.5, x = 3 and max Z = 34.5.
++ee(1.5 Marks)

The branch and bound diagram

ak 2

Xy = 8,x2=2
Zn=34
Zp=34

|Solution steps by|

BigM method,
Graphical method

FRR ICR] AC OH
--- page 18 ---
As x2>=3 (branch B) will not yield IP solution more than 34
……..(1 Marks)
Q6. a
A shopkeeper buys a vegetable puff at Rs 2 and sells it at Rs 5. Unsold puffs are given to poor people free of
cost. The following are the sales details during the past 100 days.
Daily Sales of Puffs 10   11   12   13
No. of Days Sold   15   20   40   25
Apply EMV criterion to determine how many puffs the shopkeeper has to stock every day to maximize his
profit.
Solution:
From the past 100 days the sales distribution is:
Daily sales (D)   No. of days (out of 100)   Empirical probability
10   15   0.15
11   20   0.20
12   40   0.40
13   25   0.25
----------------(1 Mark)
Revenue = selling price × min(Q, D).
Cost = cost price × Q (all stocked items are purchased).
Profit = Revenue − Cost = 5×min(Q,D) − 2×Q (in Rs).
Stock Q \ Demand D 10   11   12   13
10   Rs 30.00   Rs 30.00   Rs 30.00   Rs 30.00
11   Rs 28.00   Rs 33.00   Rs 33.00   Rs 33.00
12   Rs 26.00   Rs 31.00   Rs 36.00   Rs 36.00
13   Rs 24.00   Rs 29.00   Rs 34.00   Rs 39.00
-------------------(2 Marks)
Stock Q EMV = Σ [Profit(Q,D) × P(D)]   EMV (Rs)
10   (30.00×0.15) + (30.00×0.20) + (30.00×0.40) +   Rs 30.00
(30.00×0.25)
11   (28.00×0.15) + (33.00×0.20) + (33.00×0.40) +   Rs 32.25
(33.00×0.25)
12   (26.00×0.15) + (31.00×0.20) + (36.00×0.40) +   Rs 33.50
(36.00×0.25)
13   (24.00×0.15) + (29.00×0.20) + (34.00×0.40) +   Rs 32.75
(39.00×0.25)
-------------------(1 Mark)
The EMVs show that stocking Q = 12 puffs yields the highest expected daily profit of Rs 33.50.
-------------------(1 Mark)
********** 18 **********
--- page 19 ---
Q6. b
A firm produces two products A and B. Each product must be processed through two departments namely 1
and 2. Department 1 has 30 hours of production capacity per day, and department 2 has 60 hours. Each unit
of product A requires 2 hours in department 1 and 6 hours in department 2. Each unit of product B requires 3
hours in department 1 and 4 hours in department 2. Management has rank ordered the following goals it would
like to achieve in determining the daily product mix:
P1: Minimize the underachievement of joint total production of 10 units.
P2: Minimize the underachievement of producing 7 units of product B.
P3: Minimize the underachievement of producing 8 units of product A.
Formulate this problem as a Goal Programming model.
Solution:
Let 𝑥1 𝑎𝑛𝑑 𝑥2 = number of units of products A and B produced, respectively
𝑑𝑖 −, 𝑑𝑖 += underachievement and overachievement associated with goal i, respectively.
----------------(1 Mark)
Then the GP model is stated as follows:
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑3 − + 𝑃3𝑑2 −   ----------------(1 Mark)
subject to the constraints
2𝑥1 + 3𝑥2 ≤30
6𝑥1 + 4𝑥2 ≤60   ----------------(1 Mark)
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 10
𝑥1 + 𝑑2 −−𝑑2 + = 8   ----------------(1 Mark)
𝑥1 + 𝑑3 −−𝑑3 + = 7
and   𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑2 +, 𝑑3 −, 𝑑3 + ≥0.   ----------------(1 Mark)
Q6. c
Given an Integer Linear Programming (ILP) problem with a relaxed optimal solution from the Simplex method
is shown below:
Max z = x 1 + 3 x 2
Subject to
x 1 + 2 x 2  1; x 2  2; x 1 & x 2 are non negative integers
CJ   1   3   0   0
B   CB XB   X1   X2   S1   S2
X2   3   0.5   0.5   1   0.5   0
S2   0   1.5   -0.5   0   -0.5   1
Z=1.5   ZJ   1.5   3   1.5   0
CJ-ZJ   -0.5   0   -1.5   0
a) Construct first Gomory's fractional cut for the given non-integer optimal solution.
b) Demonstrate the first iteration of Gomory’s cutting-plane method.
Identify the integer optimal solution
Solution:
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
********** 19 **********
--- page 20 ---
x1=0,x2=0.5
Max Z=1.5   …………………….[01 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut, with the help
of x2-row as follows:
0.5=0.5x1+1x2+0.5S1
(0+0.5)=(0+0.5)x1+(1+0)x2+(0+0.5)S1
The factional cut will become
-0.5=Sg1-0.5x1-0.5S1→ (Cut-1)   …………………….[03 Marks]
………[02 Marks]
Minimum negative XB is -0.5 and its row index is 3. So, the leaving basis variable is Sg1.
Minimum positive ratio is 1 and its column index is 1. So, the entering variable is x1.
∴ The pivot element is -0.5.
Entering =x1, Departing =Sg1, Key Element =-0.5
R3(new)=R3(old) ÷(-0.5)
R1(new)=R1(old) -(-0.5) R3(new)
R2(new)=R2(old) +(-0.5) R3(new
…………………….[02 Marks]
Identify the integer optimal solution
********** 20 **********
--- page 21 ---
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as:
x1=1,x2=0
Max Z=1
The integer optimal solution found after 1st cut.   …………………….[02 Marks]
Q7. a
Distinguish between deterministic and probabilistic games. What approaches do you apply to solve each of
them?
Solution:
Deterministic Games   Probabilistic games
If the game yields a solution with one certain,   If a player adopts more than one strategy with
single strategy (pure strategy) for each some probabilities or prepares a blend of two
player, the game is deterministic.   or more strategies, these games are said to be
probabilistic.
In this game the strategies are pure and Here, mixed strategies are used as no saddle
saddle points exist.   points exist.
………………………………………….3 marks
Approaches for Deterministic Games:
• Solved using the minimax approach, where players choose strategies to minimize maximum loss
and maximize minimum gain.
• The dominance principle is also used to eliminate inferior strategies and identify the optimal one.
Approaches for Probabilistic Games:
• Solved using the arithmetic (expected value) approach, where payoffs are multiplied by their
probabilities to find the best average outcome.
•   Probability and decision theory help evaluate uncertain outcomes and guide rational choices under
risk.
………………………………………….2 marks
Q7. b
What are the advantages and limitations of Simulation models?
Solution:
Advantages
1. This approach is suitable to analyse large and complex real-life problems that cannot be solved by the
analytical methods.
2. It facilitates to study the interactive system variables, and the effect of changes that take place in
these variables, on the system performance in order to determine the desired result.
3. Simulation experiments are done on the model, not on the system itself. Experimentation takes into
consideration additional information during analysis that most quantitative models do not permit. In
other words, simulation can be used to ‘experiment’ on a model of a real situation, without incurring the
costs of operating on the system.
4. Simulation can be used as a pre-service test to try out new policies and decision rules for operating a
system before running the risk of experimentation in the real system.
------------------(3 Marks)
********** 21 **********
--- page 22 ---
Disadvantages
1. Simulation models are expensive and take a long time to develop. For example, a corporate planning
model may take a long time to develop and may also prove to be expensive.
2. It is the trial and error approach that produces different solutions in repeated runs. This means it does
not generate optimal solutions to problems.
3. The simulation model does not produce answers by itself. The user has to provide all the constraints
for the solutions that he wants to examine.   ---------------(2 Marks)
Q7. c
Use Graphical Method to solve the following Goal Programming Problem.
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2(2𝑑2 −+ 𝑑3 −) + 𝑃3𝑑1 +
subject to the constraints
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 400
𝑥1 + 𝑑2 −= 240
𝑥1 + 𝑑3 −= 300
𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑3 −≥0.
Solution:
Goal 1: Make 𝑥1 + 𝑥2 as close to 400 as possible (𝑑1 − is shortfall, 𝑑1 + is excess).
Goal 2: Make 𝑥1 close to 240 (𝑑2 −captures shortfall).
Goal 3: Make 𝑥1 close to 300 (𝑑3 −captures shortfall).
We solve by following the priorities in order (P1 highest priority, then P2, then P3).
Priority 1: Minimize 𝑑1 − (avoid shortfall on goal 1)
To minimize 𝑑1 −, choose 𝑑1 −= 0 if possible. With 𝑑1 −= 0 the first constraint becomes:
𝑥1 + 𝑥2 −𝑑1 + = 400 → 𝑥1 + 𝑥2 −400 = 𝑑1 +. (So for 𝑑1 −= 0 we must have 𝑥1 + 𝑥2 ≥400)
---------------(2 Marks)
Priority 2: Minimize 2𝑑2 −+ 𝑑3 −
From constraints 2 and 3 we have: 𝑑2 −= 240 −𝑥1 and 𝑑3 −= 300 −𝑥1 (both ≥ 0).
Hence 2𝑑2 −+ 𝑑3 − = 2(240 −𝑥1) + (300 −𝑥1) = 780 − 3 𝑥1.
But 𝑑2 − ≥ 0 requires 𝑥1 ≤ 240. Therefore, the maximum feasible 𝑥1 is 𝑥1 = 240.
Set 𝑥1 = 240 to optimally reduce the P2-term, that gives 𝑑2 − = 0 and 𝑑3 − = 60.
At this stage the first constraint (with 𝑑1 − = 0) becomes 𝑥1 + 𝑥2 −𝑑1 + = 400→ 240 + 𝑥2 −𝑑1 + = 400 →
𝑑1 + = 𝑥2 −160.
So to keep 𝑑1 + small we should choose 𝑥2 as small as possible that gives 𝑥2 ≥160
-----------(2 Marks)
Priority 3: Minimize 𝑑1 +
With 𝑥1 = 240, we choose the smallest feasible 𝑥2, i.e. 𝑥2 = 160, to minimize 𝑑1 + = 𝑥2 −160 = 0.
Thus,   𝑥1 = 240, 𝑥2 = 160
𝑑1 − = 0, 𝑑1 + = 0
𝑑2 −= 0, 𝑑3 − = 60   ---------------(2 Marks)
Objective value (in terms of deviational variables): 𝑍= 𝑃1𝑑1 −+ 𝑃2(2𝑑2 −+ 𝑑3 −) + 𝑃3𝑑1 + = 60·𝑃2.
The line 𝑥1 + 𝑥2 = 400 and the vertical line 𝑥1 = 240 Their intersection at (240,160) is the corner point
found by the priority procedure.
********** 22 **********
--- page 23 ---
Graphical sketch: lines x1 + x2 = 400 and x1 = 240
Feasible corner for lexicographic solution: (240,160)

2507

200+ (240, 160)

\

150F
100;

50F

0 50 100 150 200 250 300
xl

(4 Marks)
Graph for reference

X2
400

240 0

oS to }240 | 160
iJ an 100 © 300

FIR ICR 2 I OH
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 407e0503ce59

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_DS_7052/Optimization Methods/ANS_Optimization Methods(702BS0C079)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 75.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Optimization Methods
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figure on right hand side indicates full marks
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1.a
A company operates three warehouses, S₁, S₂, and S₃, from which it distributes goods to four regional markets
located in D₁, D₂, D₃, and D₄. The transportation cost per unit (in ₹) from each warehouse to each market,
along with the supply available at each warehouse and the demand at each market, is given in the table below:
D₁   D₂   D₃   D₄   Supply
S₁   6   8   8   5   30
S₂   5   11   9   7   40
S₃   8   9   7   13   50
Demand   35   28   32   25   120
Apply the North-West Corner rule to find the basic feasible solution. Also, compute the total cost of this
transportation.
Solution:
4 Marks
1 Marks
********** 1 **********
--- page 2 ---
Q1.b
Formulate the dual of the given primal problem.
Minimize Z = 5 x 1 + 7 x 2
subject to,
3 x 1 + 2 x 2  10
x 1 + 4 x 2  12
2 x 1 + x 2 = 8
x 1 , x 2  0
Solution:
Since objective function is minimizing,
≤ constraints (2) can be converted to ≥ type by multipling both sides by -1
---------------------------------------------------(1 mark)
In primal, There are 2 variables and 3 constraints, so in dual there must be 2 constraints and 3 variables
In primal, The coefficient of objective function c1=5,c2=7 becomes right hand side constants in dual
In primal, The right hand side constants b1=10,b2=-12,b3=8 becomes coefficient of objective function in
dual
In primal, objective function is minimizing, so in dual objective function must be maximizing
Let y1,y2,y3 be the dual variables
Since 3rd constraint in the primal is equality, the corresponding dual variable y3 will be unrestricted in sign.
---------------------------------------------------(1 mark)
Dual is
MAX Zy = 10 y1 - 12 y2 + 8 y3
subject to
3 y1 - y2 + 2 y3 ≤ 5
2 y1 - 4 y2 + y3 ≤ 7
and y1,y2≥0;y3 unrestricted in sign
------------------------------------(3 marks)
Q1. c
State whether the game whose payoff matrix is given below is strictly determinable and fair. Also, find the
best course of action for player A and player B, and the value of the game.
Player B
B1   B2   B3   B4   B5
A1   -2   0   0   5   3
Player A   A2   3   2   1   2   2
A3   -4   -3   0   -2   6
A4   5   3   -4   2   -6
Solution:
********** 2 **********
--- page 3 ---
3 Marks
2 Marks
The game is strictly determinable and unfair.
Q1. d
The principal of a college has four peons, and four tasks have to be assigned to them. The peons differ in
efficiency and the tasks differ in their intrinsic difficulty. The time each peon would take to perform each task
is given in the following effectiveness matrix
Task   T1   T2   T3   T4
Peon
P1   18   26   17   11
P2   13   28   14   26
P3   38   19   18   15
P4   19   26   24   10
How should the tasks be allocated, one to each peon, to minimize the total peon hours?
Solution:
1 Mark
1 Mark
********** 3 **********
--- page 4 ---
1 Mark
2 Marks
P1→ T3, P2→T1, P3→T2, P4→T4
The optimal value equals 59.
Q2. a
Solve the following two-player game.
Player B
B₁   B₂   B₃   B₄
A₁   3   2   4   0
Player A   A₂   3   4   2   4
A₃   4   2   4   0
A₄   0   4   0   8
Solution:
Show that saddle point does not exists (maximin, minimax). ………………………(3 marks)
A1<A3, A3 dominate A1, delete A1   ………………..(1 mark)
B1> B3, B3 dominates B1, delete B1   …………………….(1 mark)
Avg(B3,B4)=B2, delete B2
………………..(1 Marks)
********** 4 **********
--- page 5 ---
…………………………(1 Marks)
…………………………..(3 Marks)
Q2. b
A furniture manufacturing company produces three types of products chairs (x₁), tables (x₂), and cupboards
(x₃). Each product requires time on two key resources: the carpentry section and the polishing section. The
time available per week in each section and the time required per unit of each product are given below
Resource   Chairs   Tables Cupboards   Available maximum
(x₁)   (x₂)   (x₃)   time
Carpentry (hours) 2   1   1   150
Polishing (hours)   3   1   2   70
The company earns profits of ₹10 per chair, ₹15 per table, and ₹8 per cupboard.
Formulate and solve a Linear Programming Problem (LPP) to determine how many units of each product
should be manufactured weekly to maximize total profit, without exceeding the available time in each
department.
Solution:
LPP formulation to maximize the profit:
Maximize Z = 10 x 1 + 15 x 2 + 8 x 3
subject to,
2 x 1 + x 2 + x 3  150   ………………….(3 marks)
3 x 1 + x 2 + 2 x 3  70
x 1 , x 2 , x 3  0
********** 5 **********
--- page 6 ---
Setting up the initial solution
And solving till iteration1 …………………………………………………………………….(3 marks)
Iteration 2 ………………………………….………………….(3 marks)
Final answer ………………….(1 marks)
Q3. a
A product is manufactured at four factories A, B, C and D. Their production capacities are 50, 70, 30 and 50
units, respectively. These factories supply the product to four stores, demands of which are 25, 35, 105 and
20 units respectively. Unit transportation cost in rupees from each factory to each store is given in the table
below:
Stores
Factories   I   II   III   IV
A   4   6   8   13
B   13   11   10   8
C   14   4   10   13
D   9   11   13   8
Determine the initial distribution using the VAM method and check whether the obtained solution is optimal
using MODI method so that the transportation cost is the minimum.
Solution:
It’s an unbalanced TP. Add dummy column
Stores
Factories   I   II   III IV V Supply
A   4   6   8   13 0   50
B   13 11 10   8   0   70   1 Marks
C   14 4   10 13 0   30
D   9 11 13   8   0   50
Demand 25 35 105 20 15   200
IBFS by VAM
3 Marks
100+30+160+700+120+195+160=1465
********** 6 **********
--- page 7 ---
Non degeneracy test
• Number of occupied cells = 7
1 Mark
• Compare with m+n−1=7
• Occupied cells = 7 → exactly equal to m+n−1
• Therefore, No degeneracy
Shadow prices
2 Marks
2 Marks
As all the values are positive, optimal solution is achieved
Total minimum cost is 1465/-
1 Mark
Q3. b
The following matrix gives the payoff (in Rs) of different strategies (alternatives) S1, S2 and S3 against
conditions (events) N1, N2, N3 and N4.
States of Nature
Strategy N1   N2   N3   N4
S1   4,000   -100   6,000   18,000
********** 7 **********
--- page 8 ---
S2   20,000   5,000   400   0
S3   20,000   15,000   -2000   1,000
Indicate the decision taken under the following approaches:
(i) The optimistic criterion (Maximax)
(ii) The equally likely criterion (Laplace)
(iii) The regret criterion.
(iv) Hurwicz criterion, the degree of optimism being 0.7.
Solution:
(i) Maximax (Optimistic criterion):
For each strategy compute the largest of the maxima (max of maxima).
Strategy   Calculation   Maximum payoff (Rs)
S1   max(4000, -100, 6000,   Rs 18,000
18000)
S2   max(20000, 5000, 400, 0)   Rs 20,000
S3   max(20000, 15000, -2000,   Rs 20,000
1000)
The highest payoff among these is Rs 20,000 achieved by S2, S3. -----------------(2 Marks)
(ii) Laplace (Equally likely criterion):
Compute the average payoff for each strategy (sum of payoffs divided by number of states). Choose the
strategy with the highest average (expected) payoff under equal probabilities.
Strategy   Sum of payoffs   Average payoff   Calculation
(Rs)   (Rs)
S1   Rs 27,900   Rs 6,975.00   (4000 -100 + 6000 + 18000) / 4 = 27900 / 4
= 6975.00
S2   Rs 25,400   Rs 6,350.00   (20000 + 5000 + 400 + 0) / 4 = 25400 / 4 =
6350.00
S3   Rs 34,000   Rs 8,500.00   (20000 + 15000 -2000 + 1000) / 4 = 34000
/ 4 = 8500.00
By Laplace choose strategy S3 (highest average Rs 8,500.00). ------------------(2 Marks)
(iii) Regret criterion — Minimax regret
For each strategy compute regret = (best payoff in that state) − (strategy payoff). Choose the strategy with
the smallest maximum regret (minimax regret).
Strategy   Regret in   Regret in   Regret in   Regret in   Max regret
N1 (Rs)   N2 (Rs)   N3 (Rs)   N4 (Rs)   (Rs)
S1   Rs 16,000 Rs 15,100 Rs 0   Rs 0   Rs 16,000
S2   Rs 0   Rs 10,000 Rs 5,600   Rs 18,000 Rs 18,000
S3   Rs 0   Rs 0   Rs 8,000   Rs 17,000 Rs 17,000
By Minimax regret, the strategy with smallest maximum regret: S1 (max regret = Rs 16,000).
--------------------(3 Marks)
********** 8 **********
--- page 9 ---
(iv) Hurwicz criterion (Degree of optimism α = 0.7)
Hurwicz value = α*(maximum payoff) + (1−α)*(minimum payoff).
Strategy Max payoff (Rs)   Min payoff (Rs) Hurwicz formula (α = 0.7)   Hurwicz value (Rs)
S1   Rs 18,000   Rs -100   0.7*(18,000) + 0.3*(-100)   Rs 12,570.00
S2   Rs 20,000   Rs 0   0.7*(20,000) + 0.3*(0)   Rs 14,000.00
S3   Rs 20,000   Rs -2,000   0.7*(20,000) + 0.3*(-2,000) Rs 13,400.00
By Hurwicz (α = 0.7), the strategy S2 (highest Hurwicz value = Rs 14,000.00).
--------------------(3 Marks)
Q4. a
Solve the following LPP to maximize the profit using Big-M method.
Maximize Z = 10 x 1 + 12 x 2
subject to,
x 1 + x 2 = 5
x 1  2
x 2  4
x 1 , x 2  0
Solution:
Setting up the initial solution
And solving till iteration1 …………………………………..(4 marks)
Iteration 2 ………………………………….………………….(3 marks)
Iteration 3 ………………………………….………………….(2 marks)
********** 9 **********
--- page 10 ---
Iteration 1
Iteration 2
Iteration 3
Final Sol: x1=2, x2=3 and Z max=56 ………………….(1 marks)
Q4. b
A company has 5 salesmen and 5 sales districts. Considering the capabilities of the salesmen and the nature
of the districts, the company manager estimates that sales per month (in hundred) for each salesman in each
district would be as follows.
Districts
A   B   C   D   E
1   40   40   35   25   50
2   42   30   16   25   27
Salesmen
3   50   48   40   60   50
4   20   19   20   18   25
5   58   60   59   55   53
Find the assignment of salesmen to districts that will result in the maximization of sales.
********** 10 **********
--- page 11 ---
Solution:
Maximization problem converted to minimization
2 Mark
Row operation
1 Marks
Column operatoin
1 Mark
Allocation and Marking
3 Marks
Revised final Matrix and allocation
2 Mark
1→E, 2→A, 3→D, 4→C, 5→B
1 Mark
The optimal assignment cost is 232
********** 11 **********
--- page 12 ---
Q5. a
A company manufactures 200 motor cycles per day. Depending upon the availability of raw materials and
other conditions, the daily production has been varying from 196 motor cycles to 204 motor cycles, whose
probability distribution is as given below:
Production 196   197   198   199   200   201   202   203   204
/Day
Probability 0.05   0.09   0.12   0.14   0.20   0.15   0.11   0.08   0.06
The motorcycles are transported in a specially designed three-storied lorry that can accommodate only 200
motorcycles. Using the following random numbers: 82, 89, 78, 24, 52, 53, 61, 18, 45, 04, 23, 50, 77, 27, 54,
10, simulate the process to find out:
(a) The average number of motorcycles waiting in the factory?
(b) The average number of empty spaces on the lorry?
Solution:
Depending on availability of raw materials, daily production varies from 196 to 204 motor cycles. The
probability distribution is:
Production/day   Probability   Cumulative   Random number
probability   interval (00-99)
196   0.05   0.05   00 - 04
197   0.09   0.14   05 - 13
198   0.12   0.26   14 - 25
199   0.14   0.40   26 - 39
200   0.20   0.60   40 - 59
201   0.15   0.75   60 - 74
202   0.11   0.86   75 - 85
203   0.08   0.94   86 - 93
204   0.06   1.00   94 - 99
------------------(3 Marks)
Given random numbers (two-digit): 82, 89, 78, 24, 53, 61, 18, 45, 04, 23, 50, 77, 27, 54, 10.
Simulation Table (15 days)
Day   Random   Production per   Motor cycles   Empty spaces
number   day   waiting in   in lorry (200
factory   capacity)
1   82   202   2   0
2   89   203   3   0
3   78   202   2   0
4   24   198   0   2
5   53   200   0   0
6   61   201   1   0
7   18   198   0   2
8   45   200   0   0
9   04   196   0   4
10   23   198   0   2
11   50   200   0   0
12   77   202   2   0
13   27   199   0   1
14   54   200   0   0
15   10   197   0   3
********** 12 **********
--- page 13 ---
-------------------(5 Marks)
Total motor cycles waiting (sum over 15 days) = 10.
Average number of motor cycles waiting in the factory = Total waiting / 15 = 10 / 15 = 0.6667 motor cycles
(≈ 0.667).   ----------------(1 Mark)
Total empty spaces in lorry (sum over 15 days) = 14.
Average number of empty spaces in the lorry = Total empty / 15 = 14 / 15 = 0.9333 spaces (≈ 0.933).
-----------------(1 Mark)
Q5. b
Solve the following Integer Linear Programming (ILP) problem using the Branch and Bound (Graphical)
method and determine the optimal integer solution.
Max z = 3 x 1 + 5 x 2
Subject to
2 x 1 + 4 x 2  25
x 1  8
x 2  5
x 1 , x 2 are non negative integers
Solution:
********** 13 **********
--- page 14 ---
2. To draw constraint x, <8 > Q)
Treat it as x, = 8

Here line is parallel to Y-axis
*1/8/8

%9/0)14

Put x; = 0.x) = 0 (origin) inx,; = 8, then 0 = 8, which is true,

The half plane containing the origin is the region of the solution set of the inequation x, = 8
3. To draw constraint x) < 5 + 3)

Treat it asx. =5

Here line is parallel to X-axis
x4/0)1

9/55

Put xy = 0, x9 = 0 (origin) in x = 5, then 0 = 5, which is true,

The half plane containing the origin is the region of the solution set of the inequation x = 5

TT + ox
1 6 7 8 8 0 1 12

FRR IC 7 I OH
--- page 15 ---
The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates || ines through Extreme Point

Objective function value
z= 3x, + 5x7

(%4.%)
4- xy 20
O(0, 0) 5+ x,20 3(0) + 5(0) = 0
27x,<8
A(8, 0) 5x, 20 3(8) + 5(0) = 24
1 = 2x; + 4x9 25
B(8, 2.25) 2x, <8 3(8) + 5(2.25) = 35.25
a 1 = 2x; + 4x, = 25 .
(2.5, 5) 3 xy<5 3(2.5) + 5(5) = 32.5
_ 34x<5
D(0, 5) 4+ x,20 3(0) + 5(5) = 25

The maximum value of the objective function z = 35.25 occurs at the extreme point (8, 2.25).

Hence, the optimal solution to the given LP problem is : x; = 8, xz = 2.25 and max z = 35.25.
..(5 Marks)

se eeeeeeeeeees (1 Marks)

Two branches: X2<=2 and X2>=3

Sub-problem B : Solution is found by adding x» < 2.
Solution steps by Big method, Graphical method
Max Z = 3X; + 5X2
subject to
2X4 + 4X2<25
x; <8
2X7<10
X7<2

and x1,x7 2 0;

Solution is
Max Zg = 34 (x; = 8,x2 = 2)

and Z, = 34 (x = 8,x = 2) obtainted by the rounded off solution values.
This Problem has integer solution, so no further branching is required.

FRR IC 7 DA HOH
--- page 16 ---
~T 2 x1
1 6 7 8 $$ © 1 12

xz

The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates || ines through Extreme Point

Objective function value

(4.29) z= 3x, + 5x2

0(0, 0) ; _ x ; ; 3(0) + 5(0) = 0
A(8, 0) ; _ x . ; 3(8) + 5(0) = 24
B(8, 2) : _ ' : : 3(8) + 5(2) = 34
(0, 2) : _ e : ; 3(0) + 5(2) = 10

The maximum value of the objective function z = 34 occurs at the extreme point (8, 2).

Hence, the optimal solution to the given LP problem is : x; = 8, x) = 2 and max z = 34.

Sub-problem C : Solution is found by adding x 2 3.
Solution steps by Big method, Graphical method
Max Z = 3x1 + 5X)
Subject to
ty + 4yye}5
My <8
2y<10
Xy33
and x1,%) 2 0;

Solution i
Max Zo = 345 (: = 65, 73)

and Z; = 33 (x, = 6.x) =3) obtained bythe rounded of soon values.

FRR ICR 7 6 AC OH

seeeeee(1.5 Marks)
--- page 17 ---
| N
NI

xit oxi
* 1 6 7 8 9 0 1 12
xz

The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates |Lines through Extreme Point

Objective function value

(4.9) Z = 3x1 + 5x2
4-4 x7,23
A(0, 3) 5x20 3(0) + 5(3) = 15
34 x2<5
B(O, 5) 5 x,20 3(0) + 5(5) = 25
1 — 2x, + 4x = 25
C(2.5, 5) 3x <5 3(2.5) + 5(5) = 32.5
1 2x, + 4x 525
D(6.5, 3) 3(6.5) + 5(3) = 34.5

4x23

The maximum value of the objective function Z = 34.5 occurs at the extreme point (6.5, 3).

Hence, the optimal solution to the given LP problem is : x; = 6.5, x = 3 and max Z = 34.5.
++ee(1.5 Marks)

The branch and bound diagram

ak 2

Xy = 8,x2=2
Zn=34
Zp=34

|Solution steps by|

BigM method,
Graphical method

FRR ICR] AC OH
--- page 18 ---
As x2>=3 (branch B) will not yield IP solution more than 34
……..(1 Marks)
Q6. a
A shopkeeper buys a vegetable puff at Rs 2 and sells it at Rs 5. Unsold puffs are given to poor people free of
cost. The following are the sales details during the past 100 days.
Daily Sales of Puffs 10   11   12   13
No. of Days Sold   15   20   40   25
Apply EMV criterion to determine how many puffs the shopkeeper has to stock every day to maximize his
profit.
Solution:
From the past 100 days the sales distribution is:
Daily sales (D)   No. of days (out of 100)   Empirical probability
10   15   0.15
11   20   0.20
12   40   0.40
13   25   0.25
----------------(1 Mark)
Revenue = selling price × min(Q, D).
Cost = cost price × Q (all stocked items are purchased).
Profit = Revenue − Cost = 5×min(Q,D) − 2×Q (in Rs).
Stock Q \ Demand D 10   11   12   13
10   Rs 30.00   Rs 30.00   Rs 30.00   Rs 30.00
11   Rs 28.00   Rs 33.00   Rs 33.00   Rs 33.00
12   Rs 26.00   Rs 31.00   Rs 36.00   Rs 36.00
13   Rs 24.00   Rs 29.00   Rs 34.00   Rs 39.00
-------------------(2 Marks)
Stock Q EMV = Σ [Profit(Q,D) × P(D)]   EMV (Rs)
10   (30.00×0.15) + (30.00×0.20) + (30.00×0.40) +   Rs 30.00
(30.00×0.25)
11   (28.00×0.15) + (33.00×0.20) + (33.00×0.40) +   Rs 32.25
(33.00×0.25)
12   (26.00×0.15) + (31.00×0.20) + (36.00×0.40) +   Rs 33.50
(36.00×0.25)
13   (24.00×0.15) + (29.00×0.20) + (34.00×0.40) +   Rs 32.75
(39.00×0.25)
-------------------(1 Mark)
The EMVs show that stocking Q = 12 puffs yields the highest expected daily profit of Rs 33.50.
-------------------(1 Mark)
********** 18 **********
--- page 19 ---
Q6. b
A firm produces two products A and B. Each product must be processed through two departments namely 1
and 2. Department 1 has 30 hours of production capacity per day, and department 2 has 60 hours. Each unit
of product A requires 2 hours in department 1 and 6 hours in department 2. Each unit of product B requires 3
hours in department 1 and 4 hours in department 2. Management has rank ordered the following goals it would
like to achieve in determining the daily product mix:
P1: Minimize the underachievement of joint total production of 10 units.
P2: Minimize the underachievement of producing 7 units of product B.
P3: Minimize the underachievement of producing 8 units of product A.
Formulate this problem as a Goal Programming model.
Solution:
Let 𝑥1 𝑎𝑛𝑑 𝑥2 = number of units of products A and B produced, respectively
𝑑𝑖 −, 𝑑𝑖 += underachievement and overachievement associated with goal i, respectively.
----------------(1 Mark)
Then the GP model is stated as follows:
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑3 − + 𝑃3𝑑2 −   ----------------(1 Mark)
subject to the constraints
2𝑥1 + 3𝑥2 ≤30
6𝑥1 + 4𝑥2 ≤60   ----------------(1 Mark)
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 10
𝑥1 + 𝑑2 −−𝑑2 + = 8   ----------------(1 Mark)
𝑥1 + 𝑑3 −−𝑑3 + = 7
and   𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑2 +, 𝑑3 −, 𝑑3 + ≥0.   ----------------(1 Mark)
Q6. c
Given an Integer Linear Programming (ILP) problem with a relaxed optimal solution from the Simplex method
is shown below:
Max z = x 1 + 3 x 2
Subject to
x 1 + 2 x 2  1; x 2  2; x 1 & x 2 are non negative integers
CJ   1   3   0   0
B   CB XB   X1   X2   S1   S2
X2   3   0.5   0.5   1   0.5   0
S2   0   1.5   -0.5   0   -0.5   1
Z=1.5   ZJ   1.5   3   1.5   0
CJ-ZJ   -0.5   0   -1.5   0
a) Construct first Gomory's fractional cut for the given non-integer optimal solution.
b) Demonstrate the first iteration of Gomory’s cutting-plane method.
Identify the integer optimal solution
Solution:
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
********** 19 **********
--- page 20 ---
x1=0,x2=0.5
Max Z=1.5   …………………….[01 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut, with the help
of x2-row as follows:
0.5=0.5x1+1x2+0.5S1
(0+0.5)=(0+0.5)x1+(1+0)x2+(0+0.5)S1
The factional cut will become
-0.5=Sg1-0.5x1-0.5S1→ (Cut-1)   …………………….[03 Marks]
………[02 Marks]
Minimum negative XB is -0.5 and its row index is 3. So, the leaving basis variable is Sg1.
Minimum positive ratio is 1 and its column index is 1. So, the entering variable is x1.
∴ The pivot element is -0.5.
Entering =x1, Departing =Sg1, Key Element =-0.5
R3(new)=R3(old) ÷(-0.5)
R1(new)=R1(old) -(-0.5) R3(new)
R2(new)=R2(old) +(-0.5) R3(new
…………………….[02 Marks]
Identify the integer optimal solution
********** 20 **********
--- page 21 ---
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as:
x1=1,x2=0
Max Z=1
The integer optimal solution found after 1st cut.   …………………….[02 Marks]
Q7. a
Distinguish between deterministic and probabilistic games. What approaches do you apply to solve each of
them?
Solution:
Deterministic Games   Probabilistic games
If the game yields a solution with one certain,   If a player adopts more than one strategy with
single strategy (pure strategy) for each some probabilities or prepares a blend of two
player, the game is deterministic.   or more strategies, these games are said to be
probabilistic.
In this game the strategies are pure and Here, mixed strategies are used as no saddle
saddle points exist.   points exist.
………………………………………….3 marks
Approaches for Deterministic Games:
• Solved using the minimax approach, where players choose strategies to minimize maximum loss
and maximize minimum gain.
• The dominance principle is also used to eliminate inferior strategies and identify the optimal one.
Approaches for Probabilistic Games:
• Solved using the arithmetic (expected value) approach, where payoffs are multiplied by their
probabilities to find the best average outcome.
•   Probability and decision theory help evaluate uncertain outcomes and guide rational choices under
risk.
………………………………………….2 marks
Q7. b
What are the advantages and limitations of Simulation models?
Solution:
Advantages
1. This approach is suitable to analyse large and complex real-life problems that cannot be solved by the
analytical methods.
2. It facilitates to study the interactive system variables, and the effect of changes that take place in
these variables, on the system performance in order to determine the desired result.
3. Simulation experiments are done on the model, not on the system itself. Experimentation takes into
consideration additional information during analysis that most quantitative models do not permit. In
other words, simulation can be used to ‘experiment’ on a model of a real situation, without incurring the
costs of operating on the system.
4. Simulation can be used as a pre-service test to try out new policies and decision rules for operating a
system before running the risk of experimentation in the real system.
------------------(3 Marks)
********** 21 **********
--- page 22 ---
Disadvantages
1. Simulation models are expensive and take a long time to develop. For example, a corporate planning
model may take a long time to develop and may also prove to be expensive.
2. It is the trial and error approach that produces different solutions in repeated runs. This means it does
not generate optimal solutions to problems.
3. The simulation model does not produce answers by itself. The user has to provide all the constraints
for the solutions that he wants to examine.   ---------------(2 Marks)
Q7. c
Use Graphical Method to solve the following Goal Programming Problem.
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2(2𝑑2 −+ 𝑑3 −) + 𝑃3𝑑1 +
subject to the constraints
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 400
𝑥1 + 𝑑2 −= 240
𝑥1 + 𝑑3 −= 300
𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑3 −≥0.
Solution:
Goal 1: Make 𝑥1 + 𝑥2 as close to 400 as possible (𝑑1 − is shortfall, 𝑑1 + is excess).
Goal 2: Make 𝑥1 close to 240 (𝑑2 −captures shortfall).
Goal 3: Make 𝑥1 close to 300 (𝑑3 −captures shortfall).
We solve by following the priorities in order (P1 highest priority, then P2, then P3).
Priority 1: Minimize 𝑑1 − (avoid shortfall on goal 1)
To minimize 𝑑1 −, choose 𝑑1 −= 0 if possible. With 𝑑1 −= 0 the first constraint becomes:
𝑥1 + 𝑥2 −𝑑1 + = 400 → 𝑥1 + 𝑥2 −400 = 𝑑1 +. (So for 𝑑1 −= 0 we must have 𝑥1 + 𝑥2 ≥400)
---------------(2 Marks)
Priority 2: Minimize 2𝑑2 −+ 𝑑3 −
From constraints 2 and 3 we have: 𝑑2 −= 240 −𝑥1 and 𝑑3 −= 300 −𝑥1 (both ≥ 0).
Hence 2𝑑2 −+ 𝑑3 − = 2(240 −𝑥1) + (300 −𝑥1) = 780 − 3 𝑥1.
But 𝑑2 − ≥ 0 requires 𝑥1 ≤ 240. Therefore, the maximum feasible 𝑥1 is 𝑥1 = 240.
Set 𝑥1 = 240 to optimally reduce the P2-term, that gives 𝑑2 − = 0 and 𝑑3 − = 60.
At this stage the first constraint (with 𝑑1 − = 0) becomes 𝑥1 + 𝑥2 −𝑑1 + = 400→ 240 + 𝑥2 −𝑑1 + = 400 →
𝑑1 + = 𝑥2 −160.
So to keep 𝑑1 + small we should choose 𝑥2 as small as possible that gives 𝑥2 ≥160
-----------(2 Marks)
Priority 3: Minimize 𝑑1 +
With 𝑥1 = 240, we choose the smallest feasible 𝑥2, i.e. 𝑥2 = 160, to minimize 𝑑1 + = 𝑥2 −160 = 0.
Thus,   𝑥1 = 240, 𝑥2 = 160
𝑑1 − = 0, 𝑑1 + = 0
𝑑2 −= 0, 𝑑3 − = 60   ---------------(2 Marks)
Objective value (in terms of deviational variables): 𝑍= 𝑃1𝑑1 −+ 𝑃2(2𝑑2 −+ 𝑑3 −) + 𝑃3𝑑1 + = 60·𝑃2.
The line 𝑥1 + 𝑥2 = 400 and the vertical line 𝑥1 = 240 Their intersection at (240,160) is the corner point
found by the priority procedure.
********** 22 **********
--- page 23 ---
Graphical sketch: lines x1 + x2 = 400 and x1 = 240
Feasible corner for lexicographic solution: (240,160)

2507

200+ (240, 160)

\

150F
100;

50F

0 50 100 150 200 250 300
xl

(4 Marks)
Graph for reference

X2
400

240 0

oS to }240 | 160
iJ an 100 © 300

FIR ICR 2 I OH
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper e53de350ee7b

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/Integrated_DS_7038/Optimization Methods/ANS_Optimization Methods(702BS0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 75.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Optimization Methods
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figure on right hand side indicates full marks
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1.a
A company operates three warehouses, S₁, S₂, and S₃, from which it distributes goods to four regional markets
located in D₁, D₂, D₃, and D₄. The transportation cost per unit (in ₹) from each warehouse to each market,
along with the supply available at each warehouse and the demand at each market, is given in the table below:
D₁   D₂   D₃   D₄   Supply
S₁   6   8   8   5   30
S₂   5   11   9   7   40
S₃   8   9   7   13   50
Demand   35   28   32   25   120
Apply the North-West Corner rule to find the basic feasible solution. Also, compute the total cost of this
transportation.
Solution:
4 Marks
1 Marks
********** 1 **********
--- page 2 ---
Q1.b
Formulate the dual of the given primal problem.
Minimize Z = 5 x 1 + 7 x 2
subject to,
3 x 1 + 2 x 2  10
x 1 + 4 x 2  12
2 x 1 + x 2 = 8
x 1 , x 2  0
Solution:
Since objective function is minimizing,
≤ constraints (2) can be converted to ≥ type by multipling both sides by -1
---------------------------------------------------(1 mark)
In primal, There are 2 variables and 3 constraints, so in dual there must be 2 constraints and 3 variables
In primal, The coefficient of objective function c1=5,c2=7 becomes right hand side constants in dual
In primal, The right hand side constants b1=10,b2=-12,b3=8 becomes coefficient of objective function in
dual
In primal, objective function is minimizing, so in dual objective function must be maximizing
Let y1,y2,y3 be the dual variables
Since 3rd constraint in the primal is equality, the corresponding dual variable y3 will be unrestricted in sign.
---------------------------------------------------(1 mark)
Dual is
MAX Zy = 10 y1 - 12 y2 + 8 y3
subject to
3 y1 - y2 + 2 y3 ≤ 5
2 y1 - 4 y2 + y3 ≤ 7
and y1,y2≥0;y3 unrestricted in sign
------------------------------------(3 marks)
Q1. c
State whether the game whose payoff matrix is given below is strictly determinable and fair. Also, find the
best course of action for player A and player B, and the value of the game.
Player B
B1   B2   B3   B4   B5
A1   -2   0   0   5   3
Player A   A2   3   2   1   2   2
A3   -4   -3   0   -2   6
A4   5   3   -4   2   -6
Solution:
********** 2 **********
--- page 3 ---
3 Marks
2 Marks
The game is strictly determinable and unfair.
Q1. d
The principal of a college has four peons, and four tasks have to be assigned to them. The peons differ in
efficiency and the tasks differ in their intrinsic difficulty. The time each peon would take to perform each task
is given in the following effectiveness matrix
Task   T1   T2   T3   T4
Peon
P1   18   26   17   11
P2   13   28   14   26
P3   38   19   18   15
P4   19   26   24   10
How should the tasks be allocated, one to each peon, to minimize the total peon hours?
Solution:
1 Mark
1 Mark
********** 3 **********
--- page 4 ---
1 Mark
2 Marks
P1→ T3, P2→T1, P3→T2, P4→T4
The optimal value equals 59.
Q2. a
Solve the following two-player game.
Player B
B₁   B₂   B₃   B₄
A₁   3   2   4   0
Player A   A₂   3   4   2   4
A₃   4   2   4   0
A₄   0   4   0   8
Solution:
Show that saddle point does not exists (maximin, minimax). ………………………(3 marks)
A1<A3, A3 dominate A1, delete A1   ………………..(1 mark)
B1> B3, B3 dominates B1, delete B1   …………………….(1 mark)
Avg(B3,B4)=B2, delete B2
………………..(1 Marks)
********** 4 **********
--- page 5 ---
…………………………(1 Marks)
…………………………..(3 Marks)
Q2. b
A furniture manufacturing company produces three types of products chairs (x₁), tables (x₂), and cupboards
(x₃). Each product requires time on two key resources: the carpentry section and the polishing section. The
time available per week in each section and the time required per unit of each product are given below
Resource   Chairs   Tables Cupboards   Available maximum
(x₁)   (x₂)   (x₃)   time
Carpentry (hours) 2   1   1   150
Polishing (hours)   3   1   2   70
The company earns profits of ₹10 per chair, ₹15 per table, and ₹8 per cupboard.
Formulate and solve a Linear Programming Problem (LPP) to determine how many units of each product
should be manufactured weekly to maximize total profit, without exceeding the available time in each
department.
Solution:
LPP formulation to maximize the profit:
Maximize Z = 10 x 1 + 15 x 2 + 8 x 3
subject to,
2 x 1 + x 2 + x 3  150   ………………….(3 marks)
3 x 1 + x 2 + 2 x 3  70
x 1 , x 2 , x 3  0
********** 5 **********
--- page 6 ---
Setting up the initial solution
And solving till iteration1 …………………………………………………………………….(3 marks)
Iteration 2 ………………………………….………………….(3 marks)
Final answer ………………….(1 marks)
Q3. a
A product is manufactured at four factories A, B, C and D. Their production capacities are 50, 70, 30 and 50
units, respectively. These factories supply the product to four stores, demands of which are 25, 35, 105 and
20 units respectively. Unit transportation cost in rupees from each factory to each store is given in the table
below:
Stores
Factories   I   II   III   IV
A   4   6   8   13
B   13   11   10   8
C   14   4   10   13
D   9   11   13   8
Determine the initial distribution using the VAM method and check whether the obtained solution is optimal
using MODI method so that the transportation cost is the minimum.
Solution:
It’s an unbalanced TP. Add dummy column
Stores
Factories   I   II   III IV V Supply
A   4   6   8   13 0   50
B   13 11 10   8   0   70   1 Marks
C   14 4   10 13 0   30
D   9 11 13   8   0   50
Demand 25 35 105 20 15   200
IBFS by VAM
3 Marks
100+30+160+700+120+195+160=1465
********** 6 **********
--- page 7 ---
Non degeneracy test
• Number of occupied cells = 7
1 Mark
• Compare with m+n−1=7
• Occupied cells = 7 → exactly equal to m+n−1
• Therefore, No degeneracy
Shadow prices
2 Marks
2 Marks
As all the values are positive, optimal solution is achieved
Total minimum cost is 1465/-
1 Mark
Q3. b
The following matrix gives the payoff (in Rs) of different strategies (alternatives) S1, S2 and S3 against
conditions (events) N1, N2, N3 and N4.
States of Nature
Strategy N1   N2   N3   N4
S1   4,000   -100   6,000   18,000
********** 7 **********
--- page 8 ---
S2   20,000   5,000   400   0
S3   20,000   15,000   -2000   1,000
Indicate the decision taken under the following approaches:
(i) The optimistic criterion (Maximax)
(ii) The equally likely criterion (Laplace)
(iii) The regret criterion.
(iv) Hurwicz criterion, the degree of optimism being 0.7.
Solution:
(i) Maximax (Optimistic criterion):
For each strategy compute the largest of the maxima (max of maxima).
Strategy   Calculation   Maximum payoff (Rs)
S1   max(4000, -100, 6000,   Rs 18,000
18000)
S2   max(20000, 5000, 400, 0)   Rs 20,000
S3   max(20000, 15000, -2000,   Rs 20,000
1000)
The highest payoff among these is Rs 20,000 achieved by S2, S3. -----------------(2 Marks)
(ii) Laplace (Equally likely criterion):
Compute the average payoff for each strategy (sum of payoffs divided by number of states). Choose the
strategy with the highest average (expected) payoff under equal probabilities.
Strategy   Sum of payoffs   Average payoff   Calculation
(Rs)   (Rs)
S1   Rs 27,900   Rs 6,975.00   (4000 -100 + 6000 + 18000) / 4 = 27900 / 4
= 6975.00
S2   Rs 25,400   Rs 6,350.00   (20000 + 5000 + 400 + 0) / 4 = 25400 / 4 =
6350.00
S3   Rs 34,000   Rs 8,500.00   (20000 + 15000 -2000 + 1000) / 4 = 34000
/ 4 = 8500.00
By Laplace choose strategy S3 (highest average Rs 8,500.00). ------------------(2 Marks)
(iii) Regret criterion — Minimax regret
For each strategy compute regret = (best payoff in that state) − (strategy payoff). Choose the strategy with
the smallest maximum regret (minimax regret).
Strategy   Regret in   Regret in   Regret in   Regret in   Max regret
N1 (Rs)   N2 (Rs)   N3 (Rs)   N4 (Rs)   (Rs)
S1   Rs 16,000 Rs 15,100 Rs 0   Rs 0   Rs 16,000
S2   Rs 0   Rs 10,000 Rs 5,600   Rs 18,000 Rs 18,000
S3   Rs 0   Rs 0   Rs 8,000   Rs 17,000 Rs 17,000
By Minimax regret, the strategy with smallest maximum regret: S1 (max regret = Rs 16,000).
--------------------(3 Marks)
********** 8 **********
--- page 9 ---
(iv) Hurwicz criterion (Degree of optimism α = 0.7)
Hurwicz value = α*(maximum payoff) + (1−α)*(minimum payoff).
Strategy Max payoff (Rs)   Min payoff (Rs) Hurwicz formula (α = 0.7)   Hurwicz value (Rs)
S1   Rs 18,000   Rs -100   0.7*(18,000) + 0.3*(-100)   Rs 12,570.00
S2   Rs 20,000   Rs 0   0.7*(20,000) + 0.3*(0)   Rs 14,000.00
S3   Rs 20,000   Rs -2,000   0.7*(20,000) + 0.3*(-2,000) Rs 13,400.00
By Hurwicz (α = 0.7), the strategy S2 (highest Hurwicz value = Rs 14,000.00).
--------------------(3 Marks)
Q4. a
Solve the following LPP to maximize the profit using Big-M method.
Maximize Z = 10 x 1 + 12 x 2
subject to,
x 1 + x 2 = 5
x 1  2
x 2  4
x 1 , x 2  0
Solution:
Setting up the initial solution
And solving till iteration1 …………………………………..(4 marks)
Iteration 2 ………………………………….………………….(3 marks)
Iteration 3 ………………………………….………………….(2 marks)
********** 9 **********
--- page 10 ---
Iteration 1
Iteration 2
Iteration 3
Final Sol: x1=2, x2=3 and Z max=56 ………………….(1 marks)
Q4. b
A company has 5 salesmen and 5 sales districts. Considering the capabilities of the salesmen and the nature
of the districts, the company manager estimates that sales per month (in hundred) for each salesman in each
district would be as follows.
Districts
A   B   C   D   E
1   40   40   35   25   50
2   42   30   16   25   27
Salesmen
3   50   48   40   60   50
4   20   19   20   18   25
5   58   60   59   55   53
Find the assignment of salesmen to districts that will result in the maximization of sales.
********** 10 **********
--- page 11 ---
Solution:
Maximization problem converted to minimization
2 Mark
Row operation
1 Marks
Column operatoin
1 Mark
Allocation and Marking
3 Marks
Revised final Matrix and allocation
2 Mark
1→E, 2→A, 3→D, 4→C, 5→B
1 Mark
The optimal assignment cost is 232
********** 11 **********
--- page 12 ---
Q5. a
A company manufactures 200 motor cycles per day. Depending upon the availability of raw materials and
other conditions, the daily production has been varying from 196 motor cycles to 204 motor cycles, whose
probability distribution is as given below:
Production 196   197   198   199   200   201   202   203   204
/Day
Probability 0.05   0.09   0.12   0.14   0.20   0.15   0.11   0.08   0.06
The motorcycles are transported in a specially designed three-storied lorry that can accommodate only 200
motorcycles. Using the following random numbers: 82, 89, 78, 24, 52, 53, 61, 18, 45, 04, 23, 50, 77, 27, 54,
10, simulate the process to find out:
(a) The average number of motorcycles waiting in the factory?
(b) The average number of empty spaces on the lorry?
Solution:
Depending on availability of raw materials, daily production varies from 196 to 204 motor cycles. The
probability distribution is:
Production/day   Probability   Cumulative   Random number
probability   interval (00-99)
196   0.05   0.05   00 - 04
197   0.09   0.14   05 - 13
198   0.12   0.26   14 - 25
199   0.14   0.40   26 - 39
200   0.20   0.60   40 - 59
201   0.15   0.75   60 - 74
202   0.11   0.86   75 - 85
203   0.08   0.94   86 - 93
204   0.06   1.00   94 - 99
------------------(3 Marks)
Given random numbers (two-digit): 82, 89, 78, 24, 53, 61, 18, 45, 04, 23, 50, 77, 27, 54, 10.
Simulation Table (15 days)
Day   Random   Production per   Motor cycles   Empty spaces
number   day   waiting in   in lorry (200
factory   capacity)
1   82   202   2   0
2   89   203   3   0
3   78   202   2   0
4   24   198   0   2
5   53   200   0   0
6   61   201   1   0
7   18   198   0   2
8   45   200   0   0
9   04   196   0   4
10   23   198   0   2
11   50   200   0   0
12   77   202   2   0
13   27   199   0   1
14   54   200   0   0
15   10   197   0   3
********** 12 **********
--- page 13 ---
-------------------(5 Marks)
Total motor cycles waiting (sum over 15 days) = 10.
Average number of motor cycles waiting in the factory = Total waiting / 15 = 10 / 15 = 0.6667 motor cycles
(≈ 0.667).   ----------------(1 Mark)
Total empty spaces in lorry (sum over 15 days) = 14.
Average number of empty spaces in the lorry = Total empty / 15 = 14 / 15 = 0.9333 spaces (≈ 0.933).
-----------------(1 Mark)
Q5. b
Solve the following Integer Linear Programming (ILP) problem using the Branch and Bound (Graphical)
method and determine the optimal integer solution.
Max z = 3 x 1 + 5 x 2
Subject to
2 x 1 + 4 x 2  25
x 1  8
x 2  5
x 1 , x 2 are non negative integers
Solution:
********** 13 **********
--- page 14 ---
2. To draw constraint x, <8 > Q)
Treat it as x, = 8

Here line is parallel to Y-axis
*1/8/8

%9/0)14

Put x; = 0.x) = 0 (origin) inx,; = 8, then 0 = 8, which is true,

The half plane containing the origin is the region of the solution set of the inequation x, = 8
3. To draw constraint x) < 5 + 3)

Treat it asx. =5

Here line is parallel to X-axis
x4/0)1

9/55

Put xy = 0, x9 = 0 (origin) in x = 5, then 0 = 5, which is true,

The half plane containing the origin is the region of the solution set of the inequation x = 5

TT + ox
1 6 7 8 8 0 1 12

FRR IC 7 I OH
--- page 15 ---
The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates || ines through Extreme Point

Objective function value
z= 3x, + 5x7

(%4.%)
4- xy 20
O(0, 0) 5+ x,20 3(0) + 5(0) = 0
27x,<8
A(8, 0) 5x, 20 3(8) + 5(0) = 24
1 = 2x; + 4x9 25
B(8, 2.25) 2x, <8 3(8) + 5(2.25) = 35.25
a 1 = 2x; + 4x, = 25 .
(2.5, 5) 3 xy<5 3(2.5) + 5(5) = 32.5
_ 34x<5
D(0, 5) 4+ x,20 3(0) + 5(5) = 25

The maximum value of the objective function z = 35.25 occurs at the extreme point (8, 2.25).

Hence, the optimal solution to the given LP problem is : x; = 8, xz = 2.25 and max z = 35.25.
..(5 Marks)

se eeeeeeeeeees (1 Marks)

Two branches: X2<=2 and X2>=3

Sub-problem B : Solution is found by adding x» < 2.
Solution steps by Big method, Graphical method
Max Z = 3X; + 5X2
subject to
2X4 + 4X2<25
x; <8
2X7<10
X7<2

and x1,x7 2 0;

Solution is
Max Zg = 34 (x; = 8,x2 = 2)

and Z, = 34 (x = 8,x = 2) obtainted by the rounded off solution values.
This Problem has integer solution, so no further branching is required.

FRR IC 7 DA HOH
--- page 16 ---
~T 2 x1
1 6 7 8 $$ © 1 12

xz

The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates || ines through Extreme Point

Objective function value

(4.29) z= 3x, + 5x2

0(0, 0) ; _ x ; ; 3(0) + 5(0) = 0
A(8, 0) ; _ x . ; 3(8) + 5(0) = 24
B(8, 2) : _ ' : : 3(8) + 5(2) = 34
(0, 2) : _ e : ; 3(0) + 5(2) = 10

The maximum value of the objective function z = 34 occurs at the extreme point (8, 2).

Hence, the optimal solution to the given LP problem is : x; = 8, x) = 2 and max z = 34.

Sub-problem C : Solution is found by adding x 2 3.
Solution steps by Big method, Graphical method
Max Z = 3x1 + 5X)
Subject to
ty + 4yye}5
My <8
2y<10
Xy33
and x1,%) 2 0;

Solution i
Max Zo = 345 (: = 65, 73)

and Z; = 33 (x, = 6.x) =3) obtained bythe rounded of soon values.

FRR ICR 7 6 AC OH

seeeeee(1.5 Marks)
--- page 17 ---
| N
NI

xit oxi
* 1 6 7 8 9 0 1 12
xz

The value of the objective function at each of these extreme points is as follows:
Extreme Point
Coordinates |Lines through Extreme Point

Objective function value

(4.9) Z = 3x1 + 5x2
4-4 x7,23
A(0, 3) 5x20 3(0) + 5(3) = 15
34 x2<5
B(O, 5) 5 x,20 3(0) + 5(5) = 25
1 — 2x, + 4x = 25
C(2.5, 5) 3x <5 3(2.5) + 5(5) = 32.5
1 2x, + 4x 525
D(6.5, 3) 3(6.5) + 5(3) = 34.5

4x23

The maximum value of the objective function Z = 34.5 occurs at the extreme point (6.5, 3).

Hence, the optimal solution to the given LP problem is : x; = 6.5, x = 3 and max Z = 34.5.
++ee(1.5 Marks)

The branch and bound diagram

ak 2

Xy = 8,x2=2
Zn=34
Zp=34

|Solution steps by|

BigM method,
Graphical method

FRR ICR] AC OH
--- page 18 ---
As x2>=3 (branch B) will not yield IP solution more than 34
……..(1 Marks)
Q6. a
A shopkeeper buys a vegetable puff at Rs 2 and sells it at Rs 5. Unsold puffs are given to poor people free of
cost. The following are the sales details during the past 100 days.
Daily Sales of Puffs 10   11   12   13
No. of Days Sold   15   20   40   25
Apply EMV criterion to determine how many puffs the shopkeeper has to stock every day to maximize his
profit.
Solution:
From the past 100 days the sales distribution is:
Daily sales (D)   No. of days (out of 100)   Empirical probability
10   15   0.15
11   20   0.20
12   40   0.40
13   25   0.25
----------------(1 Mark)
Revenue = selling price × min(Q, D).
Cost = cost price × Q (all stocked items are purchased).
Profit = Revenue − Cost = 5×min(Q,D) − 2×Q (in Rs).
Stock Q \ Demand D 10   11   12   13
10   Rs 30.00   Rs 30.00   Rs 30.00   Rs 30.00
11   Rs 28.00   Rs 33.00   Rs 33.00   Rs 33.00
12   Rs 26.00   Rs 31.00   Rs 36.00   Rs 36.00
13   Rs 24.00   Rs 29.00   Rs 34.00   Rs 39.00
-------------------(2 Marks)
Stock Q EMV = Σ [Profit(Q,D) × P(D)]   EMV (Rs)
10   (30.00×0.15) + (30.00×0.20) + (30.00×0.40) +   Rs 30.00
(30.00×0.25)
11   (28.00×0.15) + (33.00×0.20) + (33.00×0.40) +   Rs 32.25
(33.00×0.25)
12   (26.00×0.15) + (31.00×0.20) + (36.00×0.40) +   Rs 33.50
(36.00×0.25)
13   (24.00×0.15) + (29.00×0.20) + (34.00×0.40) +   Rs 32.75
(39.00×0.25)
-------------------(1 Mark)
The EMVs show that stocking Q = 12 puffs yields the highest expected daily profit of Rs 33.50.
-------------------(1 Mark)
********** 18 **********
--- page 19 ---
Q6. b
A firm produces two products A and B. Each product must be processed through two departments namely 1
and 2. Department 1 has 30 hours of production capacity per day, and department 2 has 60 hours. Each unit
of product A requires 2 hours in department 1 and 6 hours in department 2. Each unit of product B requires 3
hours in department 1 and 4 hours in department 2. Management has rank ordered the following goals it would
like to achieve in determining the daily product mix:
P1: Minimize the underachievement of joint total production of 10 units.
P2: Minimize the underachievement of producing 7 units of product B.
P3: Minimize the underachievement of producing 8 units of product A.
Formulate this problem as a Goal Programming model.
Solution:
Let 𝑥1 𝑎𝑛𝑑 𝑥2 = number of units of products A and B produced, respectively
𝑑𝑖 −, 𝑑𝑖 += underachievement and overachievement associated with goal i, respectively.
----------------(1 Mark)
Then the GP model is stated as follows:
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑3 − + 𝑃3𝑑2 −   ----------------(1 Mark)
subject to the constraints
2𝑥1 + 3𝑥2 ≤30
6𝑥1 + 4𝑥2 ≤60   ----------------(1 Mark)
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 10
𝑥1 + 𝑑2 −−𝑑2 + = 8   ----------------(1 Mark)
𝑥1 + 𝑑3 −−𝑑3 + = 7
and   𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑2 +, 𝑑3 −, 𝑑3 + ≥0.   ----------------(1 Mark)
Q6. c
Given an Integer Linear Programming (ILP) problem with a relaxed optimal solution from the Simplex method
is shown below:
Max z = x 1 + 3 x 2
Subject to
x 1 + 2 x 2  1; x 2  2; x 1 & x 2 are non negative integers
CJ   1   3   0   0
B   CB XB   X1   X2   S1   S2
X2   3   0.5   0.5   1   0.5   0
S2   0   1.5   -0.5   0   -0.5   1
Z=1.5   ZJ   1.5   3   1.5   0
CJ-ZJ   -0.5   0   -1.5   0
a) Construct first Gomory's fractional cut for the given non-integer optimal solution.
b) Demonstrate the first iteration of Gomory’s cutting-plane method.
Identify the integer optimal solution
Solution:
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
********** 19 **********
--- page 20 ---
x1=0,x2=0.5
Max Z=1.5   …………………….[01 Marks]
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut, with the help
of x2-row as follows:
0.5=0.5x1+1x2+0.5S1
(0+0.5)=(0+0.5)x1+(1+0)x2+(0+0.5)S1
The factional cut will become
-0.5=Sg1-0.5x1-0.5S1→ (Cut-1)   …………………….[03 Marks]
………[02 Marks]
Minimum negative XB is -0.5 and its row index is 3. So, the leaving basis variable is Sg1.
Minimum positive ratio is 1 and its column index is 1. So, the entering variable is x1.
∴ The pivot element is -0.5.
Entering =x1, Departing =Sg1, Key Element =-0.5
R3(new)=R3(old) ÷(-0.5)
R1(new)=R1(old) -(-0.5) R3(new)
R2(new)=R2(old) +(-0.5) R3(new
…………………….[02 Marks]
Identify the integer optimal solution
********** 20 **********
--- page 21 ---
Since all Cj-Zj≤0
Hence, integer optimal solution is arrived with value of variables as:
x1=1,x2=0
Max Z=1
The integer optimal solution found after 1st cut.   …………………….[02 Marks]
Q7. a
Distinguish between deterministic and probabilistic games. What approaches do you apply to solve each of
them?
Solution:
Deterministic Games   Probabilistic games
If the game yields a solution with one certain,   If a player adopts more than one strategy with
single strategy (pure strategy) for each some probabilities or prepares a blend of two
player, the game is deterministic.   or more strategies, these games are said to be
probabilistic.
In this game the strategies are pure and Here, mixed strategies are used as no saddle
saddle points exist.   points exist.
………………………………………….3 marks
Approaches for Deterministic Games:
• Solved using the minimax approach, where players choose strategies to minimize maximum loss
and maximize minimum gain.
• The dominance principle is also used to eliminate inferior strategies and identify the optimal one.
Approaches for Probabilistic Games:
• Solved using the arithmetic (expected value) approach, where payoffs are multiplied by their
probabilities to find the best average outcome.
•   Probability and decision theory help evaluate uncertain outcomes and guide rational choices under
risk.
………………………………………….2 marks
Q7. b
What are the advantages and limitations of Simulation models?
Solution:
Advantages
1. This approach is suitable to analyse large and complex real-life problems that cannot be solved by the
analytical methods.
2. It facilitates to study the interactive system variables, and the effect of changes that take place in
these variables, on the system performance in order to determine the desired result.
3. Simulation experiments are done on the model, not on the system itself. Experimentation takes into
consideration additional information during analysis that most quantitative models do not permit. In
other words, simulation can be used to ‘experiment’ on a model of a real situation, without incurring the
costs of operating on the system.
4. Simulation can be used as a pre-service test to try out new policies and decision rules for operating a
system before running the risk of experimentation in the real system.
------------------(3 Marks)
********** 21 **********
--- page 22 ---
Disadvantages
1. Simulation models are expensive and take a long time to develop. For example, a corporate planning
model may take a long time to develop and may also prove to be expensive.
2. It is the trial and error approach that produces different solutions in repeated runs. This means it does
not generate optimal solutions to problems.
3. The simulation model does not produce answers by itself. The user has to provide all the constraints
for the solutions that he wants to examine.   ---------------(2 Marks)
Q7. c
Use Graphical Method to solve the following Goal Programming Problem.
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2(2𝑑2 −+ 𝑑3 −) + 𝑃3𝑑1 +
subject to the constraints
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 400
𝑥1 + 𝑑2 −= 240
𝑥1 + 𝑑3 −= 300
𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑3 −≥0.
Solution:
Goal 1: Make 𝑥1 + 𝑥2 as close to 400 as possible (𝑑1 − is shortfall, 𝑑1 + is excess).
Goal 2: Make 𝑥1 close to 240 (𝑑2 −captures shortfall).
Goal 3: Make 𝑥1 close to 300 (𝑑3 −captures shortfall).
We solve by following the priorities in order (P1 highest priority, then P2, then P3).
Priority 1: Minimize 𝑑1 − (avoid shortfall on goal 1)
To minimize 𝑑1 −, choose 𝑑1 −= 0 if possible. With 𝑑1 −= 0 the first constraint becomes:
𝑥1 + 𝑥2 −𝑑1 + = 400 → 𝑥1 + 𝑥2 −400 = 𝑑1 +. (So for 𝑑1 −= 0 we must have 𝑥1 + 𝑥2 ≥400)
---------------(2 Marks)
Priority 2: Minimize 2𝑑2 −+ 𝑑3 −
From constraints 2 and 3 we have: 𝑑2 −= 240 −𝑥1 and 𝑑3 −= 300 −𝑥1 (both ≥ 0).
Hence 2𝑑2 −+ 𝑑3 − = 2(240 −𝑥1) + (300 −𝑥1) = 780 − 3 𝑥1.
But 𝑑2 − ≥ 0 requires 𝑥1 ≤ 240. Therefore, the maximum feasible 𝑥1 is 𝑥1 = 240.
Set 𝑥1 = 240 to optimally reduce the P2-term, that gives 𝑑2 − = 0 and 𝑑3 − = 60.
At this stage the first constraint (with 𝑑1 − = 0) becomes 𝑥1 + 𝑥2 −𝑑1 + = 400→ 240 + 𝑥2 −𝑑1 + = 400 →
𝑑1 + = 𝑥2 −160.
So to keep 𝑑1 + small we should choose 𝑥2 as small as possible that gives 𝑥2 ≥160
-----------(2 Marks)
Priority 3: Minimize 𝑑1 +
With 𝑥1 = 240, we choose the smallest feasible 𝑥2, i.e. 𝑥2 = 160, to minimize 𝑑1 + = 𝑥2 −160 = 0.
Thus,   𝑥1 = 240, 𝑥2 = 160
𝑑1 − = 0, 𝑑1 + = 0
𝑑2 −= 0, 𝑑3 − = 60   ---------------(2 Marks)
Objective value (in terms of deviational variables): 𝑍= 𝑃1𝑑1 −+ 𝑃2(2𝑑2 −+ 𝑑3 −) + 𝑃3𝑑1 + = 60·𝑃2.
The line 𝑥1 + 𝑥2 = 400 and the vertical line 𝑥1 = 240 Their intersection at (240,160) is the corner point
found by the priority procedure.
********** 22 **********
--- page 23 ---
Graphical sketch: lines x1 + x2 = 400 and x1 = 240
Feasible corner for lexicographic solution: (240,160)

2507

200+ (240, 160)

\

150F
100;

50F

0 50 100 150 200 250 300
xl

(4 Marks)
Graph for reference

X2
400

240 0

oS to }240 | 160
iJ an 100 © 300

FIR ICR 2 I OH
````

## 2024-25 · Re-Exam · Sem 3 · Answer key · paper a2a75f53ee53

- Departments: Data Science
- Programmes: BTech DS 7009, Integrated DS 7038, MBATech DS 7052
- Source: `02_Question_Papers/2024/Sem_03/Re-Exam/BTech_DS_7009/Optimization Methods/ANS_Optimization Methods(702BS0C032)_2024-2025.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Optimization Methods
Date: 08 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figure on right hand side indicates full marks
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1. a
Aggie Power Generation has four generating stations S₁, S₂, S₃ and S₄ with annual available capacities (in
MW) 5, 8, 7 and 14 respectively. They supply three markets (destinations) D₁, D₂, D₃ whose annual demands
are 7, 9 and 18 MW respectively. The unit shipping costs ($/MW) from each station to each destination are
given below
D₁   D₂   D₃   Supply
S₁   2   7   4   5
S₂   3   3   1   8
S₃   5   4   7   7
S₄   1   6   2   14
Demand   7   9   18   34
Using the North-West Corner Method, determine an initial basic feasible solution for the Aggie Power
distribution problem and compute the total distribution cost.
Solution:
4 Marks
********** 1 **********
--- page 2 ---
1 Marks
Q1. b
Formulate the dual of the given primal problem.
Maximize Z = 6 x 1 + 4 x 2
subject to,
2 x 1 + 3 x 2  12
x 1 + x 2  6
x 1 + 4 x 2 = 8
x 1 , x 2  0
Solution:
Since objective function is maximizing, all ≥ constraints (2) can be converted to ≤ type by multiplying both
sides by -1
---------------------------------------------------(1 mark)
MAX zx = 6 x1 + 4 x2
subject to
2 x1 + 3 x2 ≤ 12
- x1 - x2 ≤ -6
x1 + 4 x2 = 8
and x1,x2≥0;
In primal, There are 2 variables and 3 constraints, so in dual there must be 2 constraints and 3 variables
In primal, The coefficient of objective function c1=6,c2=4 becomes right hand side constants in dual
In primal, The right hand side constants b1=12,b2=-6,b3=8 becomes coefficient of objective function in
dual
In primal, objective function is maximizing, so in dual objective function must be minimizing
Let y1,y2,y3 be the dual variables
Since 3rd constraint in the primal is equality, the corresponding dual variable y3 will be unrestricted in sign.
---------------------------------------------------(1 mark)
Dual is
MIN Zy = 12 y1 - 6 y2 + 8 y3
subject to
2 y1 - y2 + y3 ≥ 6
3 y1 - y2 + 4 y3 ≥ 4
and y1,y2≥0;y3 unrestricted in sign
------------------------------------(3 marks)
********** 2 **********
--- page 3 ---
Q1. c
State whether the game whose payoff matrix is given below is strictly determinable and fair. Also, determine
the value of the game.
Player B
B1   B2   B3   B4
A1   −5   −2   0   7
Player A   A2   5   −6   −4   8
A3   4   0   2   3
Solution:
Player B
B1   B2   B3   B4
A1   −5   −2   0   7   -5
Player A   A2   5   −6   −4   8   -6   3 Marks
A3   4   0   2   3   0
4   0   2   8
Maximin
Minimax
• As minimax=maximin, saddle point exits, it is strictly determinable
• A uses A3 strategy and B uses B2 strategy.   2 Marks
• Value of the gate is zero, it’s a fair game.
Q1. d
A sales representative has to travel to four major cities to meet clients and promote new products. He will
begin his journey from one city, visit each of the remaining cities exactly once, and finally return to the starting
city. The estimated travel cost (in thousand rupees) between every pair of cities is given in the table below.
A   B   C   D
A   -   15   20   10
B   25   -   35   15
C   5   25   -   20
D   10   20   12   -
He wants to plan his trip in the most economical way possible so that his total travel expense is minimized.
What should be the order in which the salesman visits the cities so that the total travel cost is minimized?
Solution:
Row operation   Column Operation
………………………(1 mark)   ………………………….(1 mark)
********** 3 **********
--- page 4 ---
Allocation
…………….(2 marks)
Optimal solution is A → B → D → C → A   ……………(1 Mark)
Q2. a
Solve the following two player game.
Player B
B₁   B₂   B₃   B₄
A₁   5   -10   9   0
Player A   A₂   6   7   8   1
A₃   8   7   15   1
A₄   3   4   -1   4
Solution:
Show that saddle point does not exists (maximin, minimax). ………………………(3 marks)
….1 marks   ……1 marks   ……1 marks
……1 marks
…….3 marks
Q2. b
A manufacturing company produces three types of portable LED lamps Model A, Model B, and Model C.
The profit obtained from the sale of each unit of Model A, Model B, and Model C is ₹30, ₹40, and ₹20
respectively. Each unit of the product requires processing time on a common machining line. The machining
********** 4 **********
--- page 5 ---
time required per unit is 10 minutes for Model A, 12 minutes for Model B, and 7 minutes for Model C. The
total available machining time per week is limited to 10,000 minutes. In addition, due to packaging and market
constraints, the total number of lamps (of all models together) that can be produced in a week cannot exceed
1,000 units.
Formulate and solve a Linear Programming Problem (LPP) to determine the number of units of each model
to be produced per week so that the total profit is maximized
Solution:
LPP formulation to maximize the profit:
Maximize Z = 30 x 1 + 40 x 2 + 20 x 3
subject to,
10 x 1 + 12 x 2 + 7 x 3  10000   ………………….(3 marks)
x 1 + x 2 + x 3  1000
x 1 , x 2 , x 3  0
Setting up the initial solution
And solving till iteration1 …………………………………………………………………….(3 marks)
Iteration 2 ………………………………….………………….(3 marks)
Final answer ………………….(1 marks)
Q3. a
Fresh Blend Beverages Pvt. Ltd. produces bottled juices at three factories in Dallas, Chicago, and Atlanta with
weekly capacities of 200, 160, and 90 crates respectively. They supply juices to three warehouses in New
York, Los Angeles, and Houston which require 180, 120, and 150 crates weekly. The unit shipping costs (in
dollars) are given in the table below.
Warehouse
Factory   New York Los Angeles Houston   Supply
Dallas   16   20   12   200
Chicago   14   8   18   160
Atlanta   26   24   16   90
********** 5 **********
--- page 6 ---
Demand   180   120   150   450
Determine the initial distribution for this company using the VAM method and check whether the obtained
solution is optimal using MODI method so that the total shipping cost is the minimum.
Solution:
1 mark   1 mark
1 mark   1 mark
IBFS VAM Solution : 120(8)+90(16)+12(60)+14(40)+16(140) = 5920   → 1 Mark
→ 1 Mark
→ 2 Marks
********** 6 **********
--- page 7 ---
→ 2 marks
Optimal value is 5920.. same as VAM
Q3. b
Mr Girish wants to invest Rs 10,000 in one of the three options A, B and C. The pay-off for his investment
depends on the nature of the economy (inflation, recession, or no change). The possible returns under each
economic situation are given below
Strategy   Nature of Economy
Inflation E1   Recession E2 No Change E3
S1   2000   1200   1500
S2   3000   800   1000
S3   2500   1000   1800
What course of action has he to take according to
(i) The pessimistic criterion (Maximin)
(ii) The equally likely criterion (Laplace)
(iii) The regret criterion.
(iv) Hurwicz criterion, the degree of optimism being 0.6.
Solution:
(i) Pessimistic criterion — Maximin
For each strategy find the minimum payoff across the states.
Strategy   Minimum
payoff (Rs)
A   1200
B   800
C   1000
Maximum among these minima = Rs 1200 for A.   --------------------(2 Marks)
(ii) Equally likely criterion — Laplace
Assume each state is equally likely (probability 1/3).
Strategy   Average payoff (Rs)
A   1566.67
B   1600.00
C   1766.67
The strategy with the largest average payoff is C.   --------------------(2 Marks)
********** 7 **********
--- page 8 ---
(iii) Regret criterion — Minimax regret
For each state (column) find the best payoff. Then compute regret = (best in state) − (actual payoff).
Strategy   Regret in   Regret in   Regret in No
Inflation (E1)   Recession (E2) change (E3) (Rs)
(Rs)   (Rs)
A   1000   0   300
B   0   400   800
C   500   200   0
For each strategy, the maximum regret (worst-case regret).
Strategy   Maximum
regret (Rs)
A   1000
B   800
C   500
The strategy with smallest maximum regret: C (max regret = Rs 500). ----------(3 Marks)
(iv) Hurwicz criterion — Degree of optimism α = 0.6
Hurwicz value = α*(maximum payoff) + (1−α)*(minimum payoff), where α = 0.6.
Strategy   Max payoff   Min payoff   Hurwicz value
(Rs)   (Rs)   (α=0.6)
A   2000   1200   1680.00
B   3000   800   2120.00
C   2500   1000   1900.00
Option B (highest Hurwicz value = Rs 2120.00).   ----------(3 Marks)
Q4. a
Solve the following LPP using the Big-M method to find the optimal cost.
Minimize Z = 500 x 1 + 200 x 2
subject to,
3 x 1 + 2 x 2  90
x 1  10
− 2 x 1 + x 2 = 0
x 1 , x 2  0
Solution:
Setting up the initial solution
And solving till iteration1 …………………………………..(4 marks)
Iteration 2 ………………………………….………………….(3 marks)
Iteration 3 ………………………………….………………….(2 marks)
********** 8 **********
--- page 9 ---
Iteration 1
Iteration 2
Iteration 3
Sol: x1=10, x2=20 and Z min=9000 ………………….(1 marks)
Q4. b
A company operates in five major territories and has five salesmen available for assignment. Each territory
differs in its sales potential, and each salesman has a different level of selling effectiveness. The estimated
annual sales that each salesman would generate in each territory are given in the table below:
Territories
A   B   C   D   E
1   32   38   40   28   40
2   40   24   28   21   36
Salesmen
3   41   27   33   30   37
4   22   38   41   36   36
5   29   33   40   35   39
Identify the best allocation of salesmen to territories so that the sales revenues are maximized.
Solution:
********** 9 **********
--- page 10 ---
As the given problem is of maximization type, it has to be converted to minimization type.
Minimization form
A B C D E
1 9   3   1 13 1
2 1 17 13 20 5
3 0 14 8 11 4
4 19 3   0   5 5
5 12 8   1   6 2
2 Marks
Row operation
A B C D E
1 8   2   0 12 0
2 0 16 12 19 4
3 0 14 8 11 4
4 19 3   0   5 5
5 11 7   0   5 1
1 mark
Column operation
A B C D E
1 8   0   0   7 0
2 0 14 12 14 4
3 0 12 8   6 4
4 19 1   0   0 5
5 11 5   0   0 1
1 mark
Allocation
A   B   C   D   E
1   8   0   0   7   0
2   0   14   12   14   4   ✓
3   0   12   8   6   4   ✓
4   19   1   0   0   5
5   11   5   0   0   1   ➔ 2 Marks
✓
Revised allocation (optimal)
A   B   C   D   E
1   12   0   0   7   0
2   0   10   8   10   0
3   0   8   4   2   0
4   23   1   0   0   5
5   15   5   0   0   1   ➔ 2 Marks
1→B, 2→A, 3→E, 4→C, 5→D   → 1 Mark
The associated maximum sales revenue is 38+40+37+41+35 = 191,000/-
********** 10 **********
--- page 11 ---
Q5. a
A bakery keeps stock of a popular brand of cake. Previous experience shows the daily demand pattern for the
item with associated probabilities, as given below
Daily Demand   0   10   20   30   40   50
Probability   0.01   0.20   0.15   0.50   0.12   0.02
Use the following sequence of random numbers to simulate the demand for next 10 days. Random numbers:
25, 39, 65, 76, 12, 05, 73, 89, 19, 49. Also estimate the daily average demand for the cakes on the basis of
the simulated data.
Solution:
The daily demand values and corresponding probabilities are:
Demand   Probability   Cumulative   Random number
probability   interval (00-99)
0   0.01   0.01   00 - 00
10   0.20   0.21   01 - 20
20   0.15   0.36   21 - 35
30   0.50   0.86   36 - 85
40   0.12   0.98   86 - 97
50   0.02   1.00   98 - 99
----------------(3 Marks)
Random numbers used (two-digit): 25, 39, 65, 76, 12, 05, 73, 89, 19, 49.
Simulation Table (10 days)
Day   Random number   Simulated demand (cakes)
1   25   20
2   39   30
3   65   30
4   76   30
5   12   10
6   05   10
7   73   30
8   89   40
9   19   10
10   49   30
-------------------(5 Marks)
Total demand over 10 days = 240 cakes.   -----------------(1 Mark)
Average daily demand = 240 / 10 = 24.00 cakes per day.   ------------------(1 Mark)
Q5. b
Solve the following Integer Linear Programming (ILP) problem using the Branch and Bound (Graphical)
method and determine the optimal integer solution.
Max z = 7 x 1 + 9 x 2
Subject to
− x 1 + 3 x 2  6
7 x 1 + x 2  35
x 2  7
x 1 , x 2 are non negative integers
********** 11 **********
--- page 12 ---
Solution:
……………(5 marks)
Branch at x1: x1<=4, x1>=5   …………………..(1mark)
Branch B solution …………………..(1mark)
Branch C solution …………………..(1mark)
Branch D solution …………………..(1mark)
Branch E solution …………………..(1mark)
********** 12 **********
--- page 13 ---
Q6. a
A fruit merchant purchases oranges at Rs 50 per basket and sells them at Rs 80. Unsold oranges are disposed
off at Rs 20 per basket the next day. Past record of sales for 120 days is as given below
Baskets Sold   15 16 17 18
No. of Days Sold 12 24 48 36
Using EMV, find how many baskets the merchant should purchase every day to maximize his profit.
Solution:
Here unsold baskets have a salvage value of Rs 20 each. Therefore, the loss per basket is 50-20 = 30.
Daily sales (D)   No. of days (out of 120)   Empirical probability
15   12   0.10
16   24   0.20
17   48   0.40
18   36   0.30
----------------(1 Mark)
********** 13 **********
--- page 14 ---
Thus the Profit = 30 (no. of baskets sold) - 30 (no. of baskets unsold)
Stock Q \ Demand D   15   16   17   18
Probability   0.1   0.2   0.4   0.3
15   Rs 450.00   Rs 450.00   Rs 450.00   Rs450.00
16   Rs 420.00   Rs 480.00   Rs 480.00   Rs 480.00
17   Rs 390.00   Rs 450.00   Rs 510.00   Rs 510.00
18   Rs 360.00   Rs 420.00   Rs 480.00   Rs 540.00
-------------------(2 Marks)
Stock Q EMV = Σ [Profit(Q,D) × P(D)]   EMV (Rs)
15   450*0.1 +450*0.2 +450*0.4+450*0.3 = 450   450
16   420*0.1 +480*0.2 +480*0.4+480*0.3 = 474   474
17   390*0.1 +450*0.2 +510*0.4+510*0.3 = 486   486
18   360*0.1 +420*0.2 +480*0.4+540*0.3 = 474   474
-------------------(1 Mark)
Since the highest EMV is 486, the course of action to be chosen is A3. Thus the merchant should
purchase 17 baskets every day.   -------------------(1 Mark)
Q6. b
A company produces motorcycle seats. The company has two production lines. The production rate for line 1
is 50 seats per hour and for line 2 it is 60 seats per hour. The company has entered into a contract to daily
supply 1,200 seats daily to another company. Currently, the normal operation period for each line is 8 hours.
The production manager of the company is trying to determine the best daily operation hours for the two lines.
He has set the priorities to achieve his goals, as given below:
P1: Produce and deliver 1,200 seats daily
P2: Limit the daily overtime operation hours of line 2 to 3 hours
P3: Minimize the underutilization of the regular daily operation hours of each line. Assign differential weights
based on the relative productivity rate.
P4: Minimize the daily overtime operation hours of each line as much as possible. Assign differential weights
based on the relative cost of overtime. It is assumed that the cost of operation is identical for the two production
lines.
Formulate this problem as a Goal Programming model.
Solution:
Let 𝑥1 𝑎𝑛𝑑 𝑥2 = daily operation hours for the lines 1 and 2, respectively.
It may be noted in this problem that the first criterion for determining the differential weights in the
third priority goal is the relative cost of overtime. The production rates ratio for the lines is 50 to 60.
Therefore, the relative cost resulting from an hour of overtime is greater for line 1 than for line 2. The
relative cost of overtime ratio for line 1 to line 2 will be line 6 to line 5. Second, the criterion for
determining the differential weights in the fourth priority goal is relative productivity rate. Since the
productivity of line 1 is 50 seats/ hour and of line 2 is 60 seats/hour, the productivity goals are weighted
for line 1 to line 2 as line 5 to line 6. The goal programming model for this problem can now be
formulated as follows ------(1 Mark)
Then the GP model is stated as follows:
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑4 + + 𝑃3(5𝑑2 −+ 6𝑑3 −) + 𝑃4(6𝑑2 + + 5𝑑3 +) ---------------(1 Mark)
********** 14 **********
--- page 15 ---
subject to the constraints
50𝑥1 + 60𝑥2 + 𝑑1 −−𝑑1 + = 1200
𝑥1 + 𝑑2 −−𝑑2 + = 8   ----------------(1 Mark)
𝑥2 + 𝑑3 −−𝑑3 + = 8
𝑥2 + 𝑑4 −−𝑑4 + = 11   ----------------(1 Mark)
and   𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑2 +, 𝑑3 −, 𝑑3 +, 𝑑4 −, 𝑑4 + ≥0. ----------------(1 Mark)
Q6. c
Given an Integer Linear Programming (ILP) problem with a relaxed optimal solution from the Simplex
method is shown below:
Max z = 2 x 1 + 5 x 2
Subject to
2 x 1 + 3 x 2  1, x 2  2,
x 1 , x 2 are non negative integers
CJ   2   5   0   0
B   CB XB   X1   X2   S1   S2
X2   5   0.3333   0.6667 1   0.3333 0
S2   0   1.6667   -0.6667 0   -0.3333 1
Z=1.6665   ZJ   3.3333 5   1.6667 0
CJ-ZJ   -1.3333 0   -1.6667 0
a) Construct first Gomory's fractional cut for the given non-integer optimal solution.
b) Illustrate the first iteration of Gomory’s cutting-plane method.
Determine the non-integer optimal solution after first Gomory’s cut.
Solution:
1. From Simplex solution:
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=0,x2=0.3333
Max Z=1.6667…………………….[02 Marks]
2. First iteration of Gomory’s cutting-plane method.
To obtain the integer valued solution, we proceed to construct Gomory's fractional cut, with the help
of x2-row as follows:
0.3333=0.6667x1+1x2+0.3333S1
(0+0.3333)=(0+0.6667)x1+(1+0)x2+(0+0.3333)S1
The fractional cut will become
-0.3333=Sg1-0.6667x1-0.3333S1→ (Cut-1)
Adding this additional constraint at the bottom of optimal simplex table. The new table so obtained is
…………………….[02 Marks]
********** 15 **********
--- page 16 ---
…………………….[02 Marks]
Minimum negative XB is -0.3333 and its row index is 3. So, the leaving basis variable is Sg1.
Minimum positive ratio is 2 and its column index is 1. So, the entering variable is x1.
∴ The pivot element is -0.6667.
Entering =x1, Departing =Sg1, Key Element =-0.6667
R3(new)=R1(old) ÷(-0.6667)
R1(new)=R3(old) -(0.6667) R3(new)
R2(new)=R2(old) +(0.6667) R3(new)
…………………….[02 Marks]
3. Non-integer optimal solution after first Gomory’s cut
Since all Cj-Zj≤0
Hence, non-integer optimal solution is arrived with value of variables as :
x1=0.5,x2=0
Max Z=1…………………….[02 Marks]
********** 16 **********
--- page 17 ---
Q7. a
Distinguish between (i) Pure strategy and mixed strategy (ii) Zero-sum and non-zero-sum games.
Solution:
Pure Strategy   Mixed Strategy
A strategy in which a player consistently   A strategy in which a player randomly selects among two or
follows one specific course of action.   more pure strategies according to certain probabilities.
Deterministic (definite choice).   Probabilistic (involves randomization).
Opponent can predict the player’s move.   Opponent cannot easily predict the player’s move.
Used when one strategy always provides   Used when no pure strategy dominates; helps in achieving
the best payoff.   equilibrium.
3 Marks
Zero-Sum Game   Non-Zero-Sum Game
The gain of one player is exactly equal to   The gain or loss of one player does not necessarily equal
the loss of another.   the loss or gain of another.
Constant (sum of payoffs = 0).   Variable (sum of payoffs ≠ 0).
Purely competitive — one’s success means May involve both competition and cooperation.
another’s failure.
2 Marks
Q7. b
What is Monte Carlo simulation? Describe the idea of experimentation (Random sampling) in simulation.
Solution:
The monte Carlo simulation approach is used to incorporate the random behaviour of variable(s) of
interest in a model. A formal definition of Monte Carlo Simulation is as follows:
• The Monte Carlo simulation technique involves conducting repetitive experiments on the model of the
system under study, with some known probability distribution to draw random samples (observations)
using random numbers.
The Monte Carlo simulation approach consists of following steps:
1. Setting up a probability distribution for variables to be analysed.
2. Building a cumulative probability distribution for each random variable.
3. Generating random numbers and then assigning an appropriate set of random numbers to represent
value or range (interval) of values for each random variable.
4. Conducting the simulation experiment using random sampling.
5. Repeating Step 4 until the required number of simulation runs has been generated.
6. Designing and implementing a course of action and maintaining control. -------(4 Marks)
Random Number Generation: Monte Carlo simulation requires the generation of a sequence of random
numbers where
(i)   all numbers are equally likely, and
(ii)   no patterns appear in sequence of numbers. This sequence of random numbers helps in
choosing random observations (samples) from the probability distribution
-----------(1 Mark)
Q7. c
Use the Graphical Method to solve the following Goal Programming Problem.
𝑀𝑖𝑛𝑖𝑚𝑖𝑧𝑒 𝑍= 𝑃1𝑑1 −+ 𝑃2𝑑4 + + 5𝑃3𝑑2 −+ 3𝑃3𝑑3 −+ 𝑃4𝑑1 +
subject to the constraints
𝑥1 + 𝑥2 + 𝑑1 −−𝑑1 + = 80
********** 17 **********
--- page 18 ---
𝑥1 + 𝑑2 −= 70
𝑥2 + 𝑑3 −= 45
𝑥1 + 𝑥2 + 𝑑4 −−𝑑4 + = 90
𝑥1, 𝑥2, 𝑑1 −, 𝑑1 +, 𝑑2 −, 𝑑3 −, 𝑑4 −, 𝑑4 + ≥0.
Solution:
We assume the priority ordering (lexicographic): P1 (highest), then P2, then P3, then P4. If you have a
different priority ordering please tell me and I will recompute accordingly.
Step 1: Express deviational variables in x1,x2
d1^- = max(80 - (x1 + x2), 0)
d1^+ = max((x1 + x2) - 80, 0)
d2^- = max(70 - x1, 0)
d3^- = max(45 - x2, 0)
d4^- = max(90 - (x1 + x2), 0)
d4^+ = max((x1 + x2) - 90, 0)   ---------------(2 Marks)
Step 2: Priority 1 & 2 -> feasible strip
Minimizing d1^- requires x1 + x2 ≥ 80. Minimizing d4^+ requires x1 + x2 ≤ 90. Combined: 80 ≤ x1 + x2 ≤
90. We restrict attention to this strip for subsequent priorities.
Step 3: Minimize P3-term (5 d2^- + 3 d3^-) on the strip
We minimize f3(x1,x2) = 5·max(70-x1,0) + 3·max(45-x2,0) subject to 80 ≤ x1 + x2 ≤ 90. A numerical
search on a fine grid yields the minimum f3 value and the corresponding point shown in the contour plot
below.   ---------------(2 Marks)
---------------(4 Marks)
********** 18 **********
--- page 19 ---
Numerical minimization yields the minimizing point (approx): x1 = 70.0, x2 = 20.0.
At this point:
d1^- = 0.0, d1^+ = 10.0
d2^- = 0.0, d3^- = 25.0
d4^- = 0.0, d4^+ = 0.0
Step 4: Priority 4 — minimize d1^+ without worsening higher priorities
Among points that achieve the minimal f3 value we selected one that minimizes d1^+. The final chosen
point above satisfies all priorities lexicographically.
Final decision variables: x1 = 70.0, x2 = 20.0.   ---------------(2 Marks)
********** 19 **********
````
