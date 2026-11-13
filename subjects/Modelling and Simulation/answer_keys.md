# Modelling and Simulation: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper da42fba50764

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/MODELLING AND SIMULATION/ANS_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: mixed (9 pages), mean OCR confidence 66.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
CO- a Linearity (1 Mark): The relationship between the independent and dependent variables   (5 marks)
1 ;
SO-   follows a straight-line pattern.
2 ;   Independence (1 Mark): The individual data points are independent, meaning the error in
BL-1
one observation does not predict the error in another.
Constant Variance (1 Mark): Also known as homoscedasticity, the spread of the residuals
remains the same across all levels of the predictor variables.
Normal Distribution (1 Mark): The errors or residuals of the model should follow a bell-
shaped normal distribution curve.
No Multicollinearity (1 Mark): In models with multiple predictors, the independent
variables should not be too closely related to each other.
CO- bDefinition (2 Marks): The Allee effect occurs when there is a positive correlation between   (5 marks)
2 ;   population density and the individual fitness or growth rate. It suggests that very small
SO-   populations may struggle to survive because they cannot find mates or defend against
5 ;   predators effectively.
BL-1
Model Incorporation (3 Marks): In standard growth models, researchers add a critical
threshold value. If the population falls below this specific number, the growth rate becomes
negative, leading to a population crash or extinction. This creates a more realistic model for
********** 1 **********
--- page 2 ---
endangered species compared to standard models that assume growth always happens at
low densities.
CO- c Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and find   (5 marks)
3 ;   conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic or elliptic.
SO-
1;   A=1, B=4, C=-7, B2-4AC>0, Hyperbolic(2 marks)
BL-2 A=2, B=m, C=-2, B2-4AC=m2+16=0
This equation can never be parabolic, for any real value of m
Also for any value of m it is hyperbolic. (3 marks)
CO- dStep 1: Initialize: COUNTER = 0.   (5 marks)
3;
SO-   Step 2: For i = 1, 2, ..., n, do Steps 3 through 5.
2 ;   Step 3: Calculate random coordinates x sub i and y sub i, satisfying a is less than or equal to x
BL-3
sub i is less than or equal to b and 0 is less than or equal to y sub i is less than M.
Step 4: Calculate f(x sub i) for the random x sub i coordinate.
Step 5: If y sub i is less than or equal to f(x sub i), then increment the COUNTER by 1.
Otherwise, leave COUNTER as is.
Step 6: Calculate AREA = M times (b minus a) times COUNTER divided by n.
Step 7: OUTPUT (AREA).(1 mark for each step except 1 & 7)
Q2   a 1. Architecture of a Feedforward Neural Network (3 Marks)   (10marks)
CO-1; Layered Structure (1 Mark)
SO- Nodes and Weights (1 Mark)
2;   Activation Function (1 Mark)
BL-3
2. Optimization (2 Marks)
Loss Function (1 Mark): Optimization starts by measuring the "error" (loss) between the
network's prediction and the actual target.
Gradient Descent (1 Mark): An optimizer (like SGD or Adam) uses backpropagation to
calculate how much each weight contributed to the error. It then adjusts the weights in the
direction that reduces the error, repeating this until the network performs accurately.
3. Calculation of Trainable Parameters (5 Marks)
Between Input and Hidden Layer 1 (1.5 Marks):
Weights: 2 input neurons × 4 hidden neurons = 8 weights.
Biases: 4 (one for each neuron in the hidden layer).
Subtotal: 8 + 4 = 12 parameters.
Between Hidden Layer 1 and Hidden Layer 2 (1.5 Marks):
Weights: 4 neurons × 3 neurons = 12 weights.
Biases: 3 (one for each neuron in the second hidden layer).
Subtotal: 12 + 3 = 15 parameters.
Between Hidden Layer 2 and Output Layer (1.5 Marks):
Weights: 3 neurons × 1 output neuron = 3 weights.
Biases: 1 (for the output neuron).
Subtotal: 3 + 1 = 4 parameters.
Final Total (0.5 Marks):
********** 2 **********
--- page 3 ---
12 + 15 + 4 = 31 Trainable Parameters.
CO-2; b1. Identification of Equilibrium Points (5 Marks)   (10
SO-5; To find the equilibrium points, we look for the population levels where the rate of change for marks)
BL-4 both species is zero.
Point 1: Total Extinction (1 Mark)
(0, 0)
Point 2: Species X Monopoly (1 Mark)
(2, 0)
Point 3: Species Y Monopoly (1 Mark)
(0, 2)
Point 4: Coexistence Check (2 Marks)
2. Stability Analysis (5 Marks)
At the Origin (0, 0) (1.5 Marks)
Stability: Unstable Node.
At Species X Monopoly (2, 0) (1.5 Marks)
Stability: Saddle Point (Unstable).
At Species Y Monopoly (0, 2) (2 Marks)
Stability: Marginally Stable (Species Y persists).
Q3   a   (10marks)
i. State the regression equation
CO-1;
SO- The regression equation is formed using the coefficients (coef) for the Intercept and the
2;   independent variable (Brain_weight):
BL-2 Head_size = 520.6101 + 2.4269 × Brain_weight
ii. Interpret R²
The R-squared value is 0.639.
This means that approximately 63.9% of the variance in Head_size can be explained by the
variation in Brain_weight. The remaining 36.1% is due to other factors not included in this
model.
iii. Is the independent variable significant?
Yes. To determine significance, we look at the P>|t| value for Brain_weight.
The p-value is 0.000, which is much smaller than the standard significance level of 0.05.
Therefore, Brain_weight has a statistically significant impact on Head_size.
iv. Is the overall model significant?
Yes. To determine the overall significance, we look at the Prob (F-statistic).
The value is 5.96e-54 (an extremely small number close to zero).
Since this is significantly less than 0.05, the model as a whole is statistically significant and fits
the data better than a model with no predictors.
v. Predict Head_size if the Brain_weight is 5 units
Using the equation from part (i):
Head_size = 520.6101 + (2.4269 × 5)
Head_size = 520.6101 + 12.1345
********** 3 **********
--- page 4 ---
Predicted Head_size = 532.7446
(2 marks per sub question)
CO-2; b1. Inter-Arrival Time (Uniform 2 to 9 minutes)   (10
SO-
1;   There are 8 possible outcomes (2, 3, 4, 5, 6, 7, 8, 9). We divide the 1000 possible random   marks)
BL-3 numbers (000-999) into 8 equal ranges of 125.
000-124: 2 min | 125-249: 3 min | 250-374: 4 min | 375-499: 5 min
500-624: 6 min | 625-749: 7 min | 750-874: 8 min | 875-999: 9 min
2. Registration Time (Probability Distribution)
We create cumulative ranges for the 100 possible random numbers (00-99).
00-09: 2 min | 10-29: 3 min | 30-59: 4 min
60-79: 5 min | 80-89: 6 min | 90-99: 7 min
Step 2: Simulation Table for 10 Patients
Patient RN   Inter-   Arrival RN   Reg   Service   Service Wait   Idle
(Arr)   Arr   Time   (Reg) Time   Start   End   Time Time
1   -   -   0   18   3   0   3   0   0
2   284   4   4   73   5   4   9   0   1
3   715   7   11   41   4   11   15   0   2
4   039   2   13   96   7   15   22   2   0
5   862   8   21   05   2   22   24   1   0
6   451   5   26   67   5   26   31   0   2
7   607   6   32   29   3   32   35   0   1
8   198   3   35   84   6   35   41   0   0
9   943   9   44   52   4   44   48   0   3
10   326   4   48   11   3   48   51   0   0
Total   3   9
Step 3: Final Determinations
Average Waiting Time:
Total Wait Time / Number of Patients = 3 minutes / 10 = 0.3 minutes per patient.
Probability that the Clerk is Idle:
Total Idle Time / Total Simulation Time = 9 minutes / 51 minutes ≈ 0.176 (or 17.6%).
Q4   a   (10
Iteration Table ( 2 marks per iteration)
CO2-;   marks)
SO-   Iteration   A   B   C   D
1;
BL-4   0 (Initial)   0   0   0   0
1   575.00   300.00   425.00   150.00
********** 4 **********
--- page 5 ---
2   756.25   481.25   606.25   331.25
3   846.88   571.88   696.88   421.88
4   892.19   617.19   742.19   467.19
5 (Final)   914.84   639.84   764.84   489.84
CO-2; bGenetic   (10
SO-   Algorithm (GA) (5 Marks)
marks)
2;   GA is an evolutionary optimization technique inspired by Charles Darwin’s theory of natural
BL-3 selection. It maintains a population of potential solutions (chromosomes) and evolves them
over generations to find the optimal one.
Population: A set of candidate solutions represented as strings (usually binary or decimal).
Fitness Function: A metric that evaluates how "good" or successful a solution is relative to the
objective.
The Evolutionary Process:
Selection: The "fittest" individuals are chosen from the current population to act as parents for
the next generation.
Crossover (Recombination): Pairs of parents swap segments of their data to create offspring,
combining the best traits of both.
Mutation: Random changes are introduced into an individual’s data to maintain genetic
diversity and prevent the algorithm from getting stuck in local optima.
Particle Swarm Optimization (PSO) (5 Marks)
PSO is a social behavior-based optimization technique inspired by the movement of bird flocks
or fish schools. It does not use "evolution" but rather "social intelligence."
Key Components:
Particles: Each candidate solution is treated as a "particle" moving through a multi-dimensional
search space.
Velocity: Every particle has a speed and direction that determines its next position.
The Search Process:
Personal Best (pBest): Each particle remembers the best location it has personally reached so
far.
Global Best (gBest): The swarm communicates to find the best location reached by any particle
in the entire group.
Movement Logic: In every iteration, a particle adjusts its velocity based on its current direction,
its desire to return to its pBest, and its desire to move toward the swarm’s gBest.
********** 5 **********
--- page 6 ---
Feature   Genetic Algorithm (GA)   Particle Swarm
Optimization (PSO)
Inspiration   Biological Evolution   Social Behavior
(Flocking)
Logic   Selection, Crossover,   Velocity and Position
Mutation   updates
Memory   Population changes; past   Particles remember their
states are lost   best positions
Complexity Generally more complex to Simpler math; fewer
implement   parameters to tune
Q5   a Option Pricing Model – Answer Structure (10 Marks)   (10
CO-2;   marks)
SO-2;   1. Introduction to Option Pricing Models (1 mark)
BL-3   2. Assumptions of the Model (2 marks)
3. Concept of No-Arbitrage Principle (1 mark)
4. Derivation of the Model (Mathematical Formulation) (2 marks)
5. Key Parameters and Variables (1 mark)
6. The Pricing Formula (2 marks)
7. Applications and Limitations – (1 mark)
CO-3; b   (10
SO-   Class Interval   Observed   Expected
marks)
6;   O   E
BL-4   O-E   (O-E)2   (O-E)2/E
0.0 – 0.2   21   20   1   1   0.05
0.2 – 0.4   18   20   -2   4   0.20
0.4 – 0.6   22   20   2   4   0.20
0.6 – 0.8   19   20   -1   1   0.05
0.8 – 1.0   20   20   0   0   0.00
Total   100   100   0.50
(8 marks)
The calculated Chi-square value is 0.50. Since this is less than the critical value of 3.84, we
conclude that the difference between observed and expected frequencies is not statistically
significant.(2 marks)
********** 6 **********
--- page 7 ---
Q6   a   (10
CO-2;   marks)
SO-1;
BL-3
(5 marks)
Solution
(5 marks)
CO-3; bGradient Descent Method (4 marks)   (10marks)
SO-1;
BL-3   • An iterative optimization algorithm used to find the minimum of a multivariable
function.
• Based on moving in the direction of the negative gradient (steepest descent).
• Requires only first-order derivatives
• Simple and widely used in machine learning
Newton’s Method (4 marks)
• A second-order optimization method using both gradient and curvature.
• Uses the Hessian matrix to improve convergence speed.
•   Faster convergence near the optimum
• Requires computation and inversion of Hessian
Differences Between Gradient Descent and Newton’s Method (2 marks)
Aspect   Gradient Descent   Newton’s Method
Derivatives   First-order   First + second-order
used   (gradient)   (Hessian)
Convergence Slow (linear)   Fast (quadratic near
optimum)
Computation Low cost   High cost (matrix
inversion)
Step size   Needs tuning   Automatically determined
********** 7 **********

[Text in pictures on this page, read by OCR]
Using the internal points P1(1/3, 2/3), P2(2/3,2/3), P3(1/3, 1/3), and P4(2/3, 1/3), the
system is:

1. For P1:0+ P24+ 60+ P3—4- Pl = —0.89
2. For P2: Pl+60+60+ P}-4-P2= —1.78
3. For P3:0+ P+ PI+0-4- P38 = —044

4. For P4: P34+604+ 24+0-4-P4= —0.89
--- page 8 ---
Suitability   Large-scale   Small/medium problems
problems
Gradient Descent is simple and scalable, while Newton’s method is more accurate and
faster but computationally expensive.
Q7   a Simulation of SIR Model for 5 Days (6 marks)   (10marks)
CO-3;
SO-5;   Day   Susceptible   Infected   Recovered
BL-3   0   990.0000   10.0000 0.0000
1   987.0300   11.9700 1.0000
2   983.4856   14.3174 2.1970
3   979.2630   17.1087 3.6283
4   974.2365   20.4243 5.3392
5   968.2660   24.3519 7.3821
(ii) Basic Reproduction Number R0 (2 marks)
R0=β/γ=0.3/0.1=3
(iii) Interpretation of R0 (2 marks)
• R0=3 , Each infected individual infects 3 others on average
• The infection will spread in the population (epidemic growth)
• This is consistent with the table where the number of infected individuals increases
over time
The SIR simulation shows a rising infection trend, and since R0>1R_0>1R0>1, the disease
spreads rapidly through the population.
CO-3; b   (10
SO-2; 1. 0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
marks)
BL-4
0.02 (Level 1)   0   0.1680   0.2880   0.3120   0.1920   0
0.04 (Level 2)   0   0.1440   0.2400   0.2400   0.1560   0
2. Crank-Nicolson Method (Implicit) (5 marks)
0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
********** 8 **********
--- page 9 ---
(0.02 (Level 1) 0 0.1633 0.2598 0.2796 0.2066 0

(0.04 (Level 2) 0 0.1384 0.2110 (0.2223 (0.1601 0

FIC QF OH ar
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper d621260c2352

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/MODELLING AND SIMULATION/ANS_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: mixed (9 pages), mean OCR confidence 66.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
CO- a Linearity (1 Mark): The relationship between the independent and dependent variables   (5 marks)
1 ;
SO-   follows a straight-line pattern.
2 ;   Independence (1 Mark): The individual data points are independent, meaning the error in
BL-1
one observation does not predict the error in another.
Constant Variance (1 Mark): Also known as homoscedasticity, the spread of the residuals
remains the same across all levels of the predictor variables.
Normal Distribution (1 Mark): The errors or residuals of the model should follow a bell-
shaped normal distribution curve.
No Multicollinearity (1 Mark): In models with multiple predictors, the independent
variables should not be too closely related to each other.
CO- bDefinition (2 Marks): The Allee effect occurs when there is a positive correlation between   (5 marks)
2 ;   population density and the individual fitness or growth rate. It suggests that very small
SO-   populations may struggle to survive because they cannot find mates or defend against
5 ;   predators effectively.
BL-1
Model Incorporation (3 Marks): In standard growth models, researchers add a critical
threshold value. If the population falls below this specific number, the growth rate becomes
negative, leading to a population crash or extinction. This creates a more realistic model for
********** 1 **********
--- page 2 ---
endangered species compared to standard models that assume growth always happens at
low densities.
CO- c Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and find   (5 marks)
3 ;   conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic or elliptic.
SO-
1;   A=1, B=4, C=-7, B2-4AC>0, Hyperbolic(2 marks)
BL-2 A=2, B=m, C=-2, B2-4AC=m2+16=0
This equation can never be parabolic, for any real value of m
Also for any value of m it is hyperbolic. (3 marks)
CO- dStep 1: Initialize: COUNTER = 0.   (5 marks)
3;
SO-   Step 2: For i = 1, 2, ..., n, do Steps 3 through 5.
2 ;   Step 3: Calculate random coordinates x sub i and y sub i, satisfying a is less than or equal to x
BL-3
sub i is less than or equal to b and 0 is less than or equal to y sub i is less than M.
Step 4: Calculate f(x sub i) for the random x sub i coordinate.
Step 5: If y sub i is less than or equal to f(x sub i), then increment the COUNTER by 1.
Otherwise, leave COUNTER as is.
Step 6: Calculate AREA = M times (b minus a) times COUNTER divided by n.
Step 7: OUTPUT (AREA).(1 mark for each step except 1 & 7)
Q2   a 1. Architecture of a Feedforward Neural Network (3 Marks)   (10marks)
CO-1; Layered Structure (1 Mark)
SO- Nodes and Weights (1 Mark)
2;   Activation Function (1 Mark)
BL-3
2. Optimization (2 Marks)
Loss Function (1 Mark): Optimization starts by measuring the "error" (loss) between the
network's prediction and the actual target.
Gradient Descent (1 Mark): An optimizer (like SGD or Adam) uses backpropagation to
calculate how much each weight contributed to the error. It then adjusts the weights in the
direction that reduces the error, repeating this until the network performs accurately.
3. Calculation of Trainable Parameters (5 Marks)
Between Input and Hidden Layer 1 (1.5 Marks):
Weights: 2 input neurons × 4 hidden neurons = 8 weights.
Biases: 4 (one for each neuron in the hidden layer).
Subtotal: 8 + 4 = 12 parameters.
Between Hidden Layer 1 and Hidden Layer 2 (1.5 Marks):
Weights: 4 neurons × 3 neurons = 12 weights.
Biases: 3 (one for each neuron in the second hidden layer).
Subtotal: 12 + 3 = 15 parameters.
Between Hidden Layer 2 and Output Layer (1.5 Marks):
Weights: 3 neurons × 1 output neuron = 3 weights.
Biases: 1 (for the output neuron).
Subtotal: 3 + 1 = 4 parameters.
Final Total (0.5 Marks):
********** 2 **********
--- page 3 ---
12 + 15 + 4 = 31 Trainable Parameters.
CO-2; b1. Identification of Equilibrium Points (5 Marks)   (10
SO-5; To find the equilibrium points, we look for the population levels where the rate of change for marks)
BL-4 both species is zero.
Point 1: Total Extinction (1 Mark)
(0, 0)
Point 2: Species X Monopoly (1 Mark)
(2, 0)
Point 3: Species Y Monopoly (1 Mark)
(0, 2)
Point 4: Coexistence Check (2 Marks)
2. Stability Analysis (5 Marks)
At the Origin (0, 0) (1.5 Marks)
Stability: Unstable Node.
At Species X Monopoly (2, 0) (1.5 Marks)
Stability: Saddle Point (Unstable).
At Species Y Monopoly (0, 2) (2 Marks)
Stability: Marginally Stable (Species Y persists).
Q3   a   (10marks)
i. State the regression equation
CO-1;
SO- The regression equation is formed using the coefficients (coef) for the Intercept and the
2;   independent variable (Brain_weight):
BL-2 Head_size = 520.6101 + 2.4269 × Brain_weight
ii. Interpret R²
The R-squared value is 0.639.
This means that approximately 63.9% of the variance in Head_size can be explained by the
variation in Brain_weight. The remaining 36.1% is due to other factors not included in this
model.
iii. Is the independent variable significant?
Yes. To determine significance, we look at the P>|t| value for Brain_weight.
The p-value is 0.000, which is much smaller than the standard significance level of 0.05.
Therefore, Brain_weight has a statistically significant impact on Head_size.
iv. Is the overall model significant?
Yes. To determine the overall significance, we look at the Prob (F-statistic).
The value is 5.96e-54 (an extremely small number close to zero).
Since this is significantly less than 0.05, the model as a whole is statistically significant and fits
the data better than a model with no predictors.
v. Predict Head_size if the Brain_weight is 5 units
Using the equation from part (i):
Head_size = 520.6101 + (2.4269 × 5)
Head_size = 520.6101 + 12.1345
********** 3 **********
--- page 4 ---
Predicted Head_size = 532.7446
(2 marks per sub question)
CO-2; b1. Inter-Arrival Time (Uniform 2 to 9 minutes)   (10
SO-
1;   There are 8 possible outcomes (2, 3, 4, 5, 6, 7, 8, 9). We divide the 1000 possible random   marks)
BL-3 numbers (000-999) into 8 equal ranges of 125.
000-124: 2 min | 125-249: 3 min | 250-374: 4 min | 375-499: 5 min
500-624: 6 min | 625-749: 7 min | 750-874: 8 min | 875-999: 9 min
2. Registration Time (Probability Distribution)
We create cumulative ranges for the 100 possible random numbers (00-99).
00-09: 2 min | 10-29: 3 min | 30-59: 4 min
60-79: 5 min | 80-89: 6 min | 90-99: 7 min
Step 2: Simulation Table for 10 Patients
Patient RN   Inter-   Arrival RN   Reg   Service   Service Wait   Idle
(Arr)   Arr   Time   (Reg) Time   Start   End   Time Time
1   -   -   0   18   3   0   3   0   0
2   284   4   4   73   5   4   9   0   1
3   715   7   11   41   4   11   15   0   2
4   039   2   13   96   7   15   22   2   0
5   862   8   21   05   2   22   24   1   0
6   451   5   26   67   5   26   31   0   2
7   607   6   32   29   3   32   35   0   1
8   198   3   35   84   6   35   41   0   0
9   943   9   44   52   4   44   48   0   3
10   326   4   48   11   3   48   51   0   0
Total   3   9
Step 3: Final Determinations
Average Waiting Time:
Total Wait Time / Number of Patients = 3 minutes / 10 = 0.3 minutes per patient.
Probability that the Clerk is Idle:
Total Idle Time / Total Simulation Time = 9 minutes / 51 minutes ≈ 0.176 (or 17.6%).
Q4   a   (10
Iteration Table ( 2 marks per iteration)
CO2-;   marks)
SO-   Iteration   A   B   C   D
1;
BL-4   0 (Initial)   0   0   0   0
1   575.00   300.00   425.00   150.00
********** 4 **********
--- page 5 ---
2   756.25   481.25   606.25   331.25
3   846.88   571.88   696.88   421.88
4   892.19   617.19   742.19   467.19
5 (Final)   914.84   639.84   764.84   489.84
CO-2; bGenetic   (10
SO-   Algorithm (GA) (5 Marks)
marks)
2;   GA is an evolutionary optimization technique inspired by Charles Darwin’s theory of natural
BL-3 selection. It maintains a population of potential solutions (chromosomes) and evolves them
over generations to find the optimal one.
Population: A set of candidate solutions represented as strings (usually binary or decimal).
Fitness Function: A metric that evaluates how "good" or successful a solution is relative to the
objective.
The Evolutionary Process:
Selection: The "fittest" individuals are chosen from the current population to act as parents for
the next generation.
Crossover (Recombination): Pairs of parents swap segments of their data to create offspring,
combining the best traits of both.
Mutation: Random changes are introduced into an individual’s data to maintain genetic
diversity and prevent the algorithm from getting stuck in local optima.
Particle Swarm Optimization (PSO) (5 Marks)
PSO is a social behavior-based optimization technique inspired by the movement of bird flocks
or fish schools. It does not use "evolution" but rather "social intelligence."
Key Components:
Particles: Each candidate solution is treated as a "particle" moving through a multi-dimensional
search space.
Velocity: Every particle has a speed and direction that determines its next position.
The Search Process:
Personal Best (pBest): Each particle remembers the best location it has personally reached so
far.
Global Best (gBest): The swarm communicates to find the best location reached by any particle
in the entire group.
Movement Logic: In every iteration, a particle adjusts its velocity based on its current direction,
its desire to return to its pBest, and its desire to move toward the swarm’s gBest.
********** 5 **********
--- page 6 ---
Feature   Genetic Algorithm (GA)   Particle Swarm
Optimization (PSO)
Inspiration   Biological Evolution   Social Behavior
(Flocking)
Logic   Selection, Crossover,   Velocity and Position
Mutation   updates
Memory   Population changes; past   Particles remember their
states are lost   best positions
Complexity Generally more complex to Simpler math; fewer
implement   parameters to tune
Q5   a Option Pricing Model – Answer Structure (10 Marks)   (10
CO-2;   marks)
SO-2;   1. Introduction to Option Pricing Models (1 mark)
BL-3   2. Assumptions of the Model (2 marks)
3. Concept of No-Arbitrage Principle (1 mark)
4. Derivation of the Model (Mathematical Formulation) (2 marks)
5. Key Parameters and Variables (1 mark)
6. The Pricing Formula (2 marks)
7. Applications and Limitations – (1 mark)
CO-3; b   (10
SO-   Class Interval   Observed   Expected
marks)
6;   O   E
BL-4   O-E   (O-E)2   (O-E)2/E
0.0 – 0.2   21   20   1   1   0.05
0.2 – 0.4   18   20   -2   4   0.20
0.4 – 0.6   22   20   2   4   0.20
0.6 – 0.8   19   20   -1   1   0.05
0.8 – 1.0   20   20   0   0   0.00
Total   100   100   0.50
(8 marks)
The calculated Chi-square value is 0.50. Since this is less than the critical value of 3.84, we
conclude that the difference between observed and expected frequencies is not statistically
significant.(2 marks)
********** 6 **********
--- page 7 ---
Q6   a   (10
CO-2;   marks)
SO-1;
BL-3
(5 marks)
Solution
(5 marks)
CO-3; bGradient Descent Method (4 marks)   (10marks)
SO-1;
BL-3   • An iterative optimization algorithm used to find the minimum of a multivariable
function.
• Based on moving in the direction of the negative gradient (steepest descent).
• Requires only first-order derivatives
• Simple and widely used in machine learning
Newton’s Method (4 marks)
• A second-order optimization method using both gradient and curvature.
• Uses the Hessian matrix to improve convergence speed.
•   Faster convergence near the optimum
• Requires computation and inversion of Hessian
Differences Between Gradient Descent and Newton’s Method (2 marks)
Aspect   Gradient Descent   Newton’s Method
Derivatives   First-order   First + second-order
used   (gradient)   (Hessian)
Convergence Slow (linear)   Fast (quadratic near
optimum)
Computation Low cost   High cost (matrix
inversion)
Step size   Needs tuning   Automatically determined
********** 7 **********

[Text in pictures on this page, read by OCR]
Using the internal points P1(1/3, 2/3), P2(2/3,2/3), P3(1/3, 1/3), and P4(2/3, 1/3), the
system is:

1. For P1:0+ P24+ 60+ P3—4- Pl = —0.89
2. For P2: Pl+60+60+ P}-4-P2= —1.78
3. For P3:0+ P+ PI+0-4- P38 = —044

4. For P4: P34+604+ 24+0-4-P4= —0.89
--- page 8 ---
Suitability   Large-scale   Small/medium problems
problems
Gradient Descent is simple and scalable, while Newton’s method is more accurate and
faster but computationally expensive.
Q7   a Simulation of SIR Model for 5 Days (6 marks)   (10marks)
CO-3;
SO-5;   Day   Susceptible   Infected   Recovered
BL-3   0   990.0000   10.0000 0.0000
1   987.0300   11.9700 1.0000
2   983.4856   14.3174 2.1970
3   979.2630   17.1087 3.6283
4   974.2365   20.4243 5.3392
5   968.2660   24.3519 7.3821
(ii) Basic Reproduction Number R0 (2 marks)
R0=β/γ=0.3/0.1=3
(iii) Interpretation of R0 (2 marks)
• R0=3 , Each infected individual infects 3 others on average
• The infection will spread in the population (epidemic growth)
• This is consistent with the table where the number of infected individuals increases
over time
The SIR simulation shows a rising infection trend, and since R0>1R_0>1R0>1, the disease
spreads rapidly through the population.
CO-3; b   (10
SO-2; 1. 0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
marks)
BL-4
0.02 (Level 1)   0   0.1680   0.2880   0.3120   0.1920   0
0.04 (Level 2)   0   0.1440   0.2400   0.2400   0.1560   0
2. Crank-Nicolson Method (Implicit) (5 marks)
0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
********** 8 **********
--- page 9 ---
(0.02 (Level 1) 0 0.1633 0.2598 0.2796 0.2066 0

(0.04 (Level 2) 0 0.1384 0.2110 (0.2223 (0.1601 0

FIC QF OH ar
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper e9937a5640c2

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/MODELLING AND SIMULATION/ANS_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: mixed (9 pages), mean OCR confidence 66.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
CO- a Linearity (1 Mark): The relationship between the independent and dependent variables   (5 marks)
1 ;
SO-   follows a straight-line pattern.
2 ;   Independence (1 Mark): The individual data points are independent, meaning the error in
BL-1
one observation does not predict the error in another.
Constant Variance (1 Mark): Also known as homoscedasticity, the spread of the residuals
remains the same across all levels of the predictor variables.
Normal Distribution (1 Mark): The errors or residuals of the model should follow a bell-
shaped normal distribution curve.
No Multicollinearity (1 Mark): In models with multiple predictors, the independent
variables should not be too closely related to each other.
CO- bDefinition (2 Marks): The Allee effect occurs when there is a positive correlation between   (5 marks)
2 ;   population density and the individual fitness or growth rate. It suggests that very small
SO-   populations may struggle to survive because they cannot find mates or defend against
5 ;   predators effectively.
BL-1
Model Incorporation (3 Marks): In standard growth models, researchers add a critical
threshold value. If the population falls below this specific number, the growth rate becomes
negative, leading to a population crash or extinction. This creates a more realistic model for
********** 1 **********
--- page 2 ---
endangered species compared to standard models that assume growth always happens at
low densities.
CO- c Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and find   (5 marks)
3 ;   conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic or elliptic.
SO-
1;   A=1, B=4, C=-7, B2-4AC>0, Hyperbolic(2 marks)
BL-2 A=2, B=m, C=-2, B2-4AC=m2+16=0
This equation can never be parabolic, for any real value of m
Also for any value of m it is hyperbolic. (3 marks)
CO- dStep 1: Initialize: COUNTER = 0.   (5 marks)
3;
SO-   Step 2: For i = 1, 2, ..., n, do Steps 3 through 5.
2 ;   Step 3: Calculate random coordinates x sub i and y sub i, satisfying a is less than or equal to x
BL-3
sub i is less than or equal to b and 0 is less than or equal to y sub i is less than M.
Step 4: Calculate f(x sub i) for the random x sub i coordinate.
Step 5: If y sub i is less than or equal to f(x sub i), then increment the COUNTER by 1.
Otherwise, leave COUNTER as is.
Step 6: Calculate AREA = M times (b minus a) times COUNTER divided by n.
Step 7: OUTPUT (AREA).(1 mark for each step except 1 & 7)
Q2   a 1. Architecture of a Feedforward Neural Network (3 Marks)   (10marks)
CO-1; Layered Structure (1 Mark)
SO- Nodes and Weights (1 Mark)
2;   Activation Function (1 Mark)
BL-3
2. Optimization (2 Marks)
Loss Function (1 Mark): Optimization starts by measuring the "error" (loss) between the
network's prediction and the actual target.
Gradient Descent (1 Mark): An optimizer (like SGD or Adam) uses backpropagation to
calculate how much each weight contributed to the error. It then adjusts the weights in the
direction that reduces the error, repeating this until the network performs accurately.
3. Calculation of Trainable Parameters (5 Marks)
Between Input and Hidden Layer 1 (1.5 Marks):
Weights: 2 input neurons × 4 hidden neurons = 8 weights.
Biases: 4 (one for each neuron in the hidden layer).
Subtotal: 8 + 4 = 12 parameters.
Between Hidden Layer 1 and Hidden Layer 2 (1.5 Marks):
Weights: 4 neurons × 3 neurons = 12 weights.
Biases: 3 (one for each neuron in the second hidden layer).
Subtotal: 12 + 3 = 15 parameters.
Between Hidden Layer 2 and Output Layer (1.5 Marks):
Weights: 3 neurons × 1 output neuron = 3 weights.
Biases: 1 (for the output neuron).
Subtotal: 3 + 1 = 4 parameters.
Final Total (0.5 Marks):
********** 2 **********
--- page 3 ---
12 + 15 + 4 = 31 Trainable Parameters.
CO-2; b1. Identification of Equilibrium Points (5 Marks)   (10
SO-5; To find the equilibrium points, we look for the population levels where the rate of change for marks)
BL-4 both species is zero.
Point 1: Total Extinction (1 Mark)
(0, 0)
Point 2: Species X Monopoly (1 Mark)
(2, 0)
Point 3: Species Y Monopoly (1 Mark)
(0, 2)
Point 4: Coexistence Check (2 Marks)
2. Stability Analysis (5 Marks)
At the Origin (0, 0) (1.5 Marks)
Stability: Unstable Node.
At Species X Monopoly (2, 0) (1.5 Marks)
Stability: Saddle Point (Unstable).
At Species Y Monopoly (0, 2) (2 Marks)
Stability: Marginally Stable (Species Y persists).
Q3   a   (10marks)
i. State the regression equation
CO-1;
SO- The regression equation is formed using the coefficients (coef) for the Intercept and the
2;   independent variable (Brain_weight):
BL-2 Head_size = 520.6101 + 2.4269 × Brain_weight
ii. Interpret R²
The R-squared value is 0.639.
This means that approximately 63.9% of the variance in Head_size can be explained by the
variation in Brain_weight. The remaining 36.1% is due to other factors not included in this
model.
iii. Is the independent variable significant?
Yes. To determine significance, we look at the P>|t| value for Brain_weight.
The p-value is 0.000, which is much smaller than the standard significance level of 0.05.
Therefore, Brain_weight has a statistically significant impact on Head_size.
iv. Is the overall model significant?
Yes. To determine the overall significance, we look at the Prob (F-statistic).
The value is 5.96e-54 (an extremely small number close to zero).
Since this is significantly less than 0.05, the model as a whole is statistically significant and fits
the data better than a model with no predictors.
v. Predict Head_size if the Brain_weight is 5 units
Using the equation from part (i):
Head_size = 520.6101 + (2.4269 × 5)
Head_size = 520.6101 + 12.1345
********** 3 **********
--- page 4 ---
Predicted Head_size = 532.7446
(2 marks per sub question)
CO-2; b1. Inter-Arrival Time (Uniform 2 to 9 minutes)   (10
SO-
1;   There are 8 possible outcomes (2, 3, 4, 5, 6, 7, 8, 9). We divide the 1000 possible random   marks)
BL-3 numbers (000-999) into 8 equal ranges of 125.
000-124: 2 min | 125-249: 3 min | 250-374: 4 min | 375-499: 5 min
500-624: 6 min | 625-749: 7 min | 750-874: 8 min | 875-999: 9 min
2. Registration Time (Probability Distribution)
We create cumulative ranges for the 100 possible random numbers (00-99).
00-09: 2 min | 10-29: 3 min | 30-59: 4 min
60-79: 5 min | 80-89: 6 min | 90-99: 7 min
Step 2: Simulation Table for 10 Patients
Patient RN   Inter-   Arrival RN   Reg   Service   Service Wait   Idle
(Arr)   Arr   Time   (Reg) Time   Start   End   Time Time
1   -   -   0   18   3   0   3   0   0
2   284   4   4   73   5   4   9   0   1
3   715   7   11   41   4   11   15   0   2
4   039   2   13   96   7   15   22   2   0
5   862   8   21   05   2   22   24   1   0
6   451   5   26   67   5   26   31   0   2
7   607   6   32   29   3   32   35   0   1
8   198   3   35   84   6   35   41   0   0
9   943   9   44   52   4   44   48   0   3
10   326   4   48   11   3   48   51   0   0
Total   3   9
Step 3: Final Determinations
Average Waiting Time:
Total Wait Time / Number of Patients = 3 minutes / 10 = 0.3 minutes per patient.
Probability that the Clerk is Idle:
Total Idle Time / Total Simulation Time = 9 minutes / 51 minutes ≈ 0.176 (or 17.6%).
Q4   a   (10
Iteration Table ( 2 marks per iteration)
CO2-;   marks)
SO-   Iteration   A   B   C   D
1;
BL-4   0 (Initial)   0   0   0   0
1   575.00   300.00   425.00   150.00
********** 4 **********
--- page 5 ---
2   756.25   481.25   606.25   331.25
3   846.88   571.88   696.88   421.88
4   892.19   617.19   742.19   467.19
5 (Final)   914.84   639.84   764.84   489.84
CO-2; bGenetic   (10
SO-   Algorithm (GA) (5 Marks)
marks)
2;   GA is an evolutionary optimization technique inspired by Charles Darwin’s theory of natural
BL-3 selection. It maintains a population of potential solutions (chromosomes) and evolves them
over generations to find the optimal one.
Population: A set of candidate solutions represented as strings (usually binary or decimal).
Fitness Function: A metric that evaluates how "good" or successful a solution is relative to the
objective.
The Evolutionary Process:
Selection: The "fittest" individuals are chosen from the current population to act as parents for
the next generation.
Crossover (Recombination): Pairs of parents swap segments of their data to create offspring,
combining the best traits of both.
Mutation: Random changes are introduced into an individual’s data to maintain genetic
diversity and prevent the algorithm from getting stuck in local optima.
Particle Swarm Optimization (PSO) (5 Marks)
PSO is a social behavior-based optimization technique inspired by the movement of bird flocks
or fish schools. It does not use "evolution" but rather "social intelligence."
Key Components:
Particles: Each candidate solution is treated as a "particle" moving through a multi-dimensional
search space.
Velocity: Every particle has a speed and direction that determines its next position.
The Search Process:
Personal Best (pBest): Each particle remembers the best location it has personally reached so
far.
Global Best (gBest): The swarm communicates to find the best location reached by any particle
in the entire group.
Movement Logic: In every iteration, a particle adjusts its velocity based on its current direction,
its desire to return to its pBest, and its desire to move toward the swarm’s gBest.
********** 5 **********
--- page 6 ---
Feature   Genetic Algorithm (GA)   Particle Swarm
Optimization (PSO)
Inspiration   Biological Evolution   Social Behavior
(Flocking)
Logic   Selection, Crossover,   Velocity and Position
Mutation   updates
Memory   Population changes; past   Particles remember their
states are lost   best positions
Complexity Generally more complex to Simpler math; fewer
implement   parameters to tune
Q5   a Option Pricing Model – Answer Structure (10 Marks)   (10
CO-2;   marks)
SO-2;   1. Introduction to Option Pricing Models (1 mark)
BL-3   2. Assumptions of the Model (2 marks)
3. Concept of No-Arbitrage Principle (1 mark)
4. Derivation of the Model (Mathematical Formulation) (2 marks)
5. Key Parameters and Variables (1 mark)
6. The Pricing Formula (2 marks)
7. Applications and Limitations – (1 mark)
CO-3; b   (10
SO-   Class Interval   Observed   Expected
marks)
6;   O   E
BL-4   O-E   (O-E)2   (O-E)2/E
0.0 – 0.2   21   20   1   1   0.05
0.2 – 0.4   18   20   -2   4   0.20
0.4 – 0.6   22   20   2   4   0.20
0.6 – 0.8   19   20   -1   1   0.05
0.8 – 1.0   20   20   0   0   0.00
Total   100   100   0.50
(8 marks)
The calculated Chi-square value is 0.50. Since this is less than the critical value of 3.84, we
conclude that the difference between observed and expected frequencies is not statistically
significant.(2 marks)
********** 6 **********
--- page 7 ---
Q6   a   (10
CO-2;   marks)
SO-1;
BL-3
(5 marks)
Solution
(5 marks)
CO-3; bGradient Descent Method (4 marks)   (10marks)
SO-1;
BL-3   • An iterative optimization algorithm used to find the minimum of a multivariable
function.
• Based on moving in the direction of the negative gradient (steepest descent).
• Requires only first-order derivatives
• Simple and widely used in machine learning
Newton’s Method (4 marks)
• A second-order optimization method using both gradient and curvature.
• Uses the Hessian matrix to improve convergence speed.
•   Faster convergence near the optimum
• Requires computation and inversion of Hessian
Differences Between Gradient Descent and Newton’s Method (2 marks)
Aspect   Gradient Descent   Newton’s Method
Derivatives   First-order   First + second-order
used   (gradient)   (Hessian)
Convergence Slow (linear)   Fast (quadratic near
optimum)
Computation Low cost   High cost (matrix
inversion)
Step size   Needs tuning   Automatically determined
********** 7 **********

[Text in pictures on this page, read by OCR]
Using the internal points P1(1/3, 2/3), P2(2/3,2/3), P3(1/3, 1/3), and P4(2/3, 1/3), the
system is:

1. For P1:0+ P24+ 60+ P3—4- Pl = —0.89
2. For P2: Pl+60+60+ P}-4-P2= —1.78
3. For P3:0+ P+ PI+0-4- P38 = —044

4. For P4: P34+604+ 24+0-4-P4= —0.89
--- page 8 ---
Suitability   Large-scale   Small/medium problems
problems
Gradient Descent is simple and scalable, while Newton’s method is more accurate and
faster but computationally expensive.
Q7   a Simulation of SIR Model for 5 Days (6 marks)   (10marks)
CO-3;
SO-5;   Day   Susceptible   Infected   Recovered
BL-3   0   990.0000   10.0000 0.0000
1   987.0300   11.9700 1.0000
2   983.4856   14.3174 2.1970
3   979.2630   17.1087 3.6283
4   974.2365   20.4243 5.3392
5   968.2660   24.3519 7.3821
(ii) Basic Reproduction Number R0 (2 marks)
R0=β/γ=0.3/0.1=3
(iii) Interpretation of R0 (2 marks)
• R0=3 , Each infected individual infects 3 others on average
• The infection will spread in the population (epidemic growth)
• This is consistent with the table where the number of infected individuals increases
over time
The SIR simulation shows a rising infection trend, and since R0>1R_0>1R0>1, the disease
spreads rapidly through the population.
CO-3; b   (10
SO-2; 1. 0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
marks)
BL-4
0.02 (Level 1)   0   0.1680   0.2880   0.3120   0.1920   0
0.04 (Level 2)   0   0.1440   0.2400   0.2400   0.1560   0
2. Crank-Nicolson Method (Implicit) (5 marks)
0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
********** 8 **********
--- page 9 ---
(0.02 (Level 1) 0 0.1633 0.2598 0.2796 0.2066 0

(0.04 (Level 2) 0 0.1384 0.2110 (0.2223 (0.1601 0

FIC QF OH ar
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 5b6916c245b6

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/MODELLING AND SIMULATION/ANS_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: mixed (9 pages), mean OCR confidence 66.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
CO- a Linearity (1 Mark): The relationship between the independent and dependent variables   (5 marks)
1 ;
SO-   follows a straight-line pattern.
2 ;   Independence (1 Mark): The individual data points are independent, meaning the error in
BL-1
one observation does not predict the error in another.
Constant Variance (1 Mark): Also known as homoscedasticity, the spread of the residuals
remains the same across all levels of the predictor variables.
Normal Distribution (1 Mark): The errors or residuals of the model should follow a bell-
shaped normal distribution curve.
No Multicollinearity (1 Mark): In models with multiple predictors, the independent
variables should not be too closely related to each other.
CO- bDefinition (2 Marks): The Allee effect occurs when there is a positive correlation between   (5 marks)
2 ;   population density and the individual fitness or growth rate. It suggests that very small
SO-   populations may struggle to survive because they cannot find mates or defend against
5 ;   predators effectively.
BL-1
Model Incorporation (3 Marks): In standard growth models, researchers add a critical
threshold value. If the population falls below this specific number, the growth rate becomes
negative, leading to a population crash or extinction. This creates a more realistic model for
********** 1 **********
--- page 2 ---
endangered species compared to standard models that assume growth always happens at
low densities.
CO- c Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and find   (5 marks)
3 ;   conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic or elliptic.
SO-
1;   A=1, B=4, C=-7, B2-4AC>0, Hyperbolic(2 marks)
BL-2 A=2, B=m, C=-2, B2-4AC=m2+16=0
This equation can never be parabolic, for any real value of m
Also for any value of m it is hyperbolic. (3 marks)
CO- dStep 1: Initialize: COUNTER = 0.   (5 marks)
3;
SO-   Step 2: For i = 1, 2, ..., n, do Steps 3 through 5.
2 ;   Step 3: Calculate random coordinates x sub i and y sub i, satisfying a is less than or equal to x
BL-3
sub i is less than or equal to b and 0 is less than or equal to y sub i is less than M.
Step 4: Calculate f(x sub i) for the random x sub i coordinate.
Step 5: If y sub i is less than or equal to f(x sub i), then increment the COUNTER by 1.
Otherwise, leave COUNTER as is.
Step 6: Calculate AREA = M times (b minus a) times COUNTER divided by n.
Step 7: OUTPUT (AREA).(1 mark for each step except 1 & 7)
Q2   a 1. Architecture of a Feedforward Neural Network (3 Marks)   (10marks)
CO-1; Layered Structure (1 Mark)
SO- Nodes and Weights (1 Mark)
2;   Activation Function (1 Mark)
BL-3
2. Optimization (2 Marks)
Loss Function (1 Mark): Optimization starts by measuring the "error" (loss) between the
network's prediction and the actual target.
Gradient Descent (1 Mark): An optimizer (like SGD or Adam) uses backpropagation to
calculate how much each weight contributed to the error. It then adjusts the weights in the
direction that reduces the error, repeating this until the network performs accurately.
3. Calculation of Trainable Parameters (5 Marks)
Between Input and Hidden Layer 1 (1.5 Marks):
Weights: 2 input neurons × 4 hidden neurons = 8 weights.
Biases: 4 (one for each neuron in the hidden layer).
Subtotal: 8 + 4 = 12 parameters.
Between Hidden Layer 1 and Hidden Layer 2 (1.5 Marks):
Weights: 4 neurons × 3 neurons = 12 weights.
Biases: 3 (one for each neuron in the second hidden layer).
Subtotal: 12 + 3 = 15 parameters.
Between Hidden Layer 2 and Output Layer (1.5 Marks):
Weights: 3 neurons × 1 output neuron = 3 weights.
Biases: 1 (for the output neuron).
Subtotal: 3 + 1 = 4 parameters.
Final Total (0.5 Marks):
********** 2 **********
--- page 3 ---
12 + 15 + 4 = 31 Trainable Parameters.
CO-2; b1. Identification of Equilibrium Points (5 Marks)   (10
SO-5; To find the equilibrium points, we look for the population levels where the rate of change for marks)
BL-4 both species is zero.
Point 1: Total Extinction (1 Mark)
(0, 0)
Point 2: Species X Monopoly (1 Mark)
(2, 0)
Point 3: Species Y Monopoly (1 Mark)
(0, 2)
Point 4: Coexistence Check (2 Marks)
2. Stability Analysis (5 Marks)
At the Origin (0, 0) (1.5 Marks)
Stability: Unstable Node.
At Species X Monopoly (2, 0) (1.5 Marks)
Stability: Saddle Point (Unstable).
At Species Y Monopoly (0, 2) (2 Marks)
Stability: Marginally Stable (Species Y persists).
Q3   a   (10marks)
i. State the regression equation
CO-1;
SO- The regression equation is formed using the coefficients (coef) for the Intercept and the
2;   independent variable (Brain_weight):
BL-2 Head_size = 520.6101 + 2.4269 × Brain_weight
ii. Interpret R²
The R-squared value is 0.639.
This means that approximately 63.9% of the variance in Head_size can be explained by the
variation in Brain_weight. The remaining 36.1% is due to other factors not included in this
model.
iii. Is the independent variable significant?
Yes. To determine significance, we look at the P>|t| value for Brain_weight.
The p-value is 0.000, which is much smaller than the standard significance level of 0.05.
Therefore, Brain_weight has a statistically significant impact on Head_size.
iv. Is the overall model significant?
Yes. To determine the overall significance, we look at the Prob (F-statistic).
The value is 5.96e-54 (an extremely small number close to zero).
Since this is significantly less than 0.05, the model as a whole is statistically significant and fits
the data better than a model with no predictors.
v. Predict Head_size if the Brain_weight is 5 units
Using the equation from part (i):
Head_size = 520.6101 + (2.4269 × 5)
Head_size = 520.6101 + 12.1345
********** 3 **********
--- page 4 ---
Predicted Head_size = 532.7446
(2 marks per sub question)
CO-2; b1. Inter-Arrival Time (Uniform 2 to 9 minutes)   (10
SO-
1;   There are 8 possible outcomes (2, 3, 4, 5, 6, 7, 8, 9). We divide the 1000 possible random   marks)
BL-3 numbers (000-999) into 8 equal ranges of 125.
000-124: 2 min | 125-249: 3 min | 250-374: 4 min | 375-499: 5 min
500-624: 6 min | 625-749: 7 min | 750-874: 8 min | 875-999: 9 min
2. Registration Time (Probability Distribution)
We create cumulative ranges for the 100 possible random numbers (00-99).
00-09: 2 min | 10-29: 3 min | 30-59: 4 min
60-79: 5 min | 80-89: 6 min | 90-99: 7 min
Step 2: Simulation Table for 10 Patients
Patient RN   Inter-   Arrival RN   Reg   Service   Service Wait   Idle
(Arr)   Arr   Time   (Reg) Time   Start   End   Time Time
1   -   -   0   18   3   0   3   0   0
2   284   4   4   73   5   4   9   0   1
3   715   7   11   41   4   11   15   0   2
4   039   2   13   96   7   15   22   2   0
5   862   8   21   05   2   22   24   1   0
6   451   5   26   67   5   26   31   0   2
7   607   6   32   29   3   32   35   0   1
8   198   3   35   84   6   35   41   0   0
9   943   9   44   52   4   44   48   0   3
10   326   4   48   11   3   48   51   0   0
Total   3   9
Step 3: Final Determinations
Average Waiting Time:
Total Wait Time / Number of Patients = 3 minutes / 10 = 0.3 minutes per patient.
Probability that the Clerk is Idle:
Total Idle Time / Total Simulation Time = 9 minutes / 51 minutes ≈ 0.176 (or 17.6%).
Q4   a   (10
Iteration Table ( 2 marks per iteration)
CO2-;   marks)
SO-   Iteration   A   B   C   D
1;
BL-4   0 (Initial)   0   0   0   0
1   575.00   300.00   425.00   150.00
********** 4 **********
--- page 5 ---
2   756.25   481.25   606.25   331.25
3   846.88   571.88   696.88   421.88
4   892.19   617.19   742.19   467.19
5 (Final)   914.84   639.84   764.84   489.84
CO-2; bGenetic   (10
SO-   Algorithm (GA) (5 Marks)
marks)
2;   GA is an evolutionary optimization technique inspired by Charles Darwin’s theory of natural
BL-3 selection. It maintains a population of potential solutions (chromosomes) and evolves them
over generations to find the optimal one.
Population: A set of candidate solutions represented as strings (usually binary or decimal).
Fitness Function: A metric that evaluates how "good" or successful a solution is relative to the
objective.
The Evolutionary Process:
Selection: The "fittest" individuals are chosen from the current population to act as parents for
the next generation.
Crossover (Recombination): Pairs of parents swap segments of their data to create offspring,
combining the best traits of both.
Mutation: Random changes are introduced into an individual’s data to maintain genetic
diversity and prevent the algorithm from getting stuck in local optima.
Particle Swarm Optimization (PSO) (5 Marks)
PSO is a social behavior-based optimization technique inspired by the movement of bird flocks
or fish schools. It does not use "evolution" but rather "social intelligence."
Key Components:
Particles: Each candidate solution is treated as a "particle" moving through a multi-dimensional
search space.
Velocity: Every particle has a speed and direction that determines its next position.
The Search Process:
Personal Best (pBest): Each particle remembers the best location it has personally reached so
far.
Global Best (gBest): The swarm communicates to find the best location reached by any particle
in the entire group.
Movement Logic: In every iteration, a particle adjusts its velocity based on its current direction,
its desire to return to its pBest, and its desire to move toward the swarm’s gBest.
********** 5 **********
--- page 6 ---
Feature   Genetic Algorithm (GA)   Particle Swarm
Optimization (PSO)
Inspiration   Biological Evolution   Social Behavior
(Flocking)
Logic   Selection, Crossover,   Velocity and Position
Mutation   updates
Memory   Population changes; past   Particles remember their
states are lost   best positions
Complexity Generally more complex to Simpler math; fewer
implement   parameters to tune
Q5   a Option Pricing Model – Answer Structure (10 Marks)   (10
CO-2;   marks)
SO-2;   1. Introduction to Option Pricing Models (1 mark)
BL-3   2. Assumptions of the Model (2 marks)
3. Concept of No-Arbitrage Principle (1 mark)
4. Derivation of the Model (Mathematical Formulation) (2 marks)
5. Key Parameters and Variables (1 mark)
6. The Pricing Formula (2 marks)
7. Applications and Limitations – (1 mark)
CO-3; b   (10
SO-   Class Interval   Observed   Expected
marks)
6;   O   E
BL-4   O-E   (O-E)2   (O-E)2/E
0.0 – 0.2   21   20   1   1   0.05
0.2 – 0.4   18   20   -2   4   0.20
0.4 – 0.6   22   20   2   4   0.20
0.6 – 0.8   19   20   -1   1   0.05
0.8 – 1.0   20   20   0   0   0.00
Total   100   100   0.50
(8 marks)
The calculated Chi-square value is 0.50. Since this is less than the critical value of 3.84, we
conclude that the difference between observed and expected frequencies is not statistically
significant.(2 marks)
********** 6 **********
--- page 7 ---
Q6   a   (10
CO-2;   marks)
SO-1;
BL-3
(5 marks)
Solution
(5 marks)
CO-3; bGradient Descent Method (4 marks)   (10marks)
SO-1;
BL-3   • An iterative optimization algorithm used to find the minimum of a multivariable
function.
• Based on moving in the direction of the negative gradient (steepest descent).
• Requires only first-order derivatives
• Simple and widely used in machine learning
Newton’s Method (4 marks)
• A second-order optimization method using both gradient and curvature.
• Uses the Hessian matrix to improve convergence speed.
•   Faster convergence near the optimum
• Requires computation and inversion of Hessian
Differences Between Gradient Descent and Newton’s Method (2 marks)
Aspect   Gradient Descent   Newton’s Method
Derivatives   First-order   First + second-order
used   (gradient)   (Hessian)
Convergence Slow (linear)   Fast (quadratic near
optimum)
Computation Low cost   High cost (matrix
inversion)
Step size   Needs tuning   Automatically determined
********** 7 **********

[Text in pictures on this page, read by OCR]
Using the internal points P1(1/3, 2/3), P2(2/3,2/3), P3(1/3, 1/3), and P4(2/3, 1/3), the
system is:

1. For P1:0+ P24+ 60+ P3—4- Pl = —0.89
2. For P2: Pl+60+60+ P}-4-P2= —1.78
3. For P3:0+ P+ PI+0-4- P38 = —044

4. For P4: P34+604+ 24+0-4-P4= —0.89
--- page 8 ---
Suitability   Large-scale   Small/medium problems
problems
Gradient Descent is simple and scalable, while Newton’s method is more accurate and
faster but computationally expensive.
Q7   a Simulation of SIR Model for 5 Days (6 marks)   (10marks)
CO-3;
SO-5;   Day   Susceptible   Infected   Recovered
BL-3   0   990.0000   10.0000 0.0000
1   987.0300   11.9700 1.0000
2   983.4856   14.3174 2.1970
3   979.2630   17.1087 3.6283
4   974.2365   20.4243 5.3392
5   968.2660   24.3519 7.3821
(ii) Basic Reproduction Number R0 (2 marks)
R0=β/γ=0.3/0.1=3
(iii) Interpretation of R0 (2 marks)
• R0=3 , Each infected individual infects 3 others on average
• The infection will spread in the population (epidemic growth)
• This is consistent with the table where the number of infected individuals increases
over time
The SIR simulation shows a rising infection trend, and since R0>1R_0>1R0>1, the disease
spreads rapidly through the population.
CO-3; b   (10
SO-2; 1. 0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
marks)
BL-4
0.02 (Level 1)   0   0.1680   0.2880   0.3120   0.1920   0
0.04 (Level 2)   0   0.1440   0.2400   0.2400   0.1560   0
2. Crank-Nicolson Method (Implicit) (5 marks)
0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
********** 8 **********
--- page 9 ---
(0.02 (Level 1) 0 0.1633 0.2598 0.2796 0.2066 0

(0.04 (Level 2) 0 0.1384 0.2110 (0.2223 (0.1601 0

FIC QF OH ar
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 25023e1c29d1

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/MODELLING AND SIMULATION/ANS_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: mixed (9 pages), mean OCR confidence 66.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
CO- a Linearity (1 Mark): The relationship between the independent and dependent variables   (5 marks)
1 ;
SO-   follows a straight-line pattern.
2 ;   Independence (1 Mark): The individual data points are independent, meaning the error in
BL-1
one observation does not predict the error in another.
Constant Variance (1 Mark): Also known as homoscedasticity, the spread of the residuals
remains the same across all levels of the predictor variables.
Normal Distribution (1 Mark): The errors or residuals of the model should follow a bell-
shaped normal distribution curve.
No Multicollinearity (1 Mark): In models with multiple predictors, the independent
variables should not be too closely related to each other.
CO- bDefinition (2 Marks): The Allee effect occurs when there is a positive correlation between   (5 marks)
2 ;   population density and the individual fitness or growth rate. It suggests that very small
SO-   populations may struggle to survive because they cannot find mates or defend against
5 ;   predators effectively.
BL-1
Model Incorporation (3 Marks): In standard growth models, researchers add a critical
threshold value. If the population falls below this specific number, the growth rate becomes
negative, leading to a population crash or extinction. This creates a more realistic model for
********** 1 **********
--- page 2 ---
endangered species compared to standard models that assume growth always happens at
low densities.
CO- c Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and find   (5 marks)
3 ;   conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic or elliptic.
SO-
1;   A=1, B=4, C=-7, B2-4AC>0, Hyperbolic(2 marks)
BL-2 A=2, B=m, C=-2, B2-4AC=m2+16=0
This equation can never be parabolic, for any real value of m
Also for any value of m it is hyperbolic. (3 marks)
CO- dStep 1: Initialize: COUNTER = 0.   (5 marks)
3;
SO-   Step 2: For i = 1, 2, ..., n, do Steps 3 through 5.
2 ;   Step 3: Calculate random coordinates x sub i and y sub i, satisfying a is less than or equal to x
BL-3
sub i is less than or equal to b and 0 is less than or equal to y sub i is less than M.
Step 4: Calculate f(x sub i) for the random x sub i coordinate.
Step 5: If y sub i is less than or equal to f(x sub i), then increment the COUNTER by 1.
Otherwise, leave COUNTER as is.
Step 6: Calculate AREA = M times (b minus a) times COUNTER divided by n.
Step 7: OUTPUT (AREA).(1 mark for each step except 1 & 7)
Q2   a 1. Architecture of a Feedforward Neural Network (3 Marks)   (10marks)
CO-1; Layered Structure (1 Mark)
SO- Nodes and Weights (1 Mark)
2;   Activation Function (1 Mark)
BL-3
2. Optimization (2 Marks)
Loss Function (1 Mark): Optimization starts by measuring the "error" (loss) between the
network's prediction and the actual target.
Gradient Descent (1 Mark): An optimizer (like SGD or Adam) uses backpropagation to
calculate how much each weight contributed to the error. It then adjusts the weights in the
direction that reduces the error, repeating this until the network performs accurately.
3. Calculation of Trainable Parameters (5 Marks)
Between Input and Hidden Layer 1 (1.5 Marks):
Weights: 2 input neurons × 4 hidden neurons = 8 weights.
Biases: 4 (one for each neuron in the hidden layer).
Subtotal: 8 + 4 = 12 parameters.
Between Hidden Layer 1 and Hidden Layer 2 (1.5 Marks):
Weights: 4 neurons × 3 neurons = 12 weights.
Biases: 3 (one for each neuron in the second hidden layer).
Subtotal: 12 + 3 = 15 parameters.
Between Hidden Layer 2 and Output Layer (1.5 Marks):
Weights: 3 neurons × 1 output neuron = 3 weights.
Biases: 1 (for the output neuron).
Subtotal: 3 + 1 = 4 parameters.
Final Total (0.5 Marks):
********** 2 **********
--- page 3 ---
12 + 15 + 4 = 31 Trainable Parameters.
CO-2; b1. Identification of Equilibrium Points (5 Marks)   (10
SO-5; To find the equilibrium points, we look for the population levels where the rate of change for marks)
BL-4 both species is zero.
Point 1: Total Extinction (1 Mark)
(0, 0)
Point 2: Species X Monopoly (1 Mark)
(2, 0)
Point 3: Species Y Monopoly (1 Mark)
(0, 2)
Point 4: Coexistence Check (2 Marks)
2. Stability Analysis (5 Marks)
At the Origin (0, 0) (1.5 Marks)
Stability: Unstable Node.
At Species X Monopoly (2, 0) (1.5 Marks)
Stability: Saddle Point (Unstable).
At Species Y Monopoly (0, 2) (2 Marks)
Stability: Marginally Stable (Species Y persists).
Q3   a   (10marks)
i. State the regression equation
CO-1;
SO- The regression equation is formed using the coefficients (coef) for the Intercept and the
2;   independent variable (Brain_weight):
BL-2 Head_size = 520.6101 + 2.4269 × Brain_weight
ii. Interpret R²
The R-squared value is 0.639.
This means that approximately 63.9% of the variance in Head_size can be explained by the
variation in Brain_weight. The remaining 36.1% is due to other factors not included in this
model.
iii. Is the independent variable significant?
Yes. To determine significance, we look at the P>|t| value for Brain_weight.
The p-value is 0.000, which is much smaller than the standard significance level of 0.05.
Therefore, Brain_weight has a statistically significant impact on Head_size.
iv. Is the overall model significant?
Yes. To determine the overall significance, we look at the Prob (F-statistic).
The value is 5.96e-54 (an extremely small number close to zero).
Since this is significantly less than 0.05, the model as a whole is statistically significant and fits
the data better than a model with no predictors.
v. Predict Head_size if the Brain_weight is 5 units
Using the equation from part (i):
Head_size = 520.6101 + (2.4269 × 5)
Head_size = 520.6101 + 12.1345
********** 3 **********
--- page 4 ---
Predicted Head_size = 532.7446
(2 marks per sub question)
CO-2; b1. Inter-Arrival Time (Uniform 2 to 9 minutes)   (10
SO-
1;   There are 8 possible outcomes (2, 3, 4, 5, 6, 7, 8, 9). We divide the 1000 possible random   marks)
BL-3 numbers (000-999) into 8 equal ranges of 125.
000-124: 2 min | 125-249: 3 min | 250-374: 4 min | 375-499: 5 min
500-624: 6 min | 625-749: 7 min | 750-874: 8 min | 875-999: 9 min
2. Registration Time (Probability Distribution)
We create cumulative ranges for the 100 possible random numbers (00-99).
00-09: 2 min | 10-29: 3 min | 30-59: 4 min
60-79: 5 min | 80-89: 6 min | 90-99: 7 min
Step 2: Simulation Table for 10 Patients
Patient RN   Inter-   Arrival RN   Reg   Service   Service Wait   Idle
(Arr)   Arr   Time   (Reg) Time   Start   End   Time Time
1   -   -   0   18   3   0   3   0   0
2   284   4   4   73   5   4   9   0   1
3   715   7   11   41   4   11   15   0   2
4   039   2   13   96   7   15   22   2   0
5   862   8   21   05   2   22   24   1   0
6   451   5   26   67   5   26   31   0   2
7   607   6   32   29   3   32   35   0   1
8   198   3   35   84   6   35   41   0   0
9   943   9   44   52   4   44   48   0   3
10   326   4   48   11   3   48   51   0   0
Total   3   9
Step 3: Final Determinations
Average Waiting Time:
Total Wait Time / Number of Patients = 3 minutes / 10 = 0.3 minutes per patient.
Probability that the Clerk is Idle:
Total Idle Time / Total Simulation Time = 9 minutes / 51 minutes ≈ 0.176 (or 17.6%).
Q4   a   (10
Iteration Table ( 2 marks per iteration)
CO2-;   marks)
SO-   Iteration   A   B   C   D
1;
BL-4   0 (Initial)   0   0   0   0
1   575.00   300.00   425.00   150.00
********** 4 **********
--- page 5 ---
2   756.25   481.25   606.25   331.25
3   846.88   571.88   696.88   421.88
4   892.19   617.19   742.19   467.19
5 (Final)   914.84   639.84   764.84   489.84
CO-2; bGenetic   (10
SO-   Algorithm (GA) (5 Marks)
marks)
2;   GA is an evolutionary optimization technique inspired by Charles Darwin’s theory of natural
BL-3 selection. It maintains a population of potential solutions (chromosomes) and evolves them
over generations to find the optimal one.
Population: A set of candidate solutions represented as strings (usually binary or decimal).
Fitness Function: A metric that evaluates how "good" or successful a solution is relative to the
objective.
The Evolutionary Process:
Selection: The "fittest" individuals are chosen from the current population to act as parents for
the next generation.
Crossover (Recombination): Pairs of parents swap segments of their data to create offspring,
combining the best traits of both.
Mutation: Random changes are introduced into an individual’s data to maintain genetic
diversity and prevent the algorithm from getting stuck in local optima.
Particle Swarm Optimization (PSO) (5 Marks)
PSO is a social behavior-based optimization technique inspired by the movement of bird flocks
or fish schools. It does not use "evolution" but rather "social intelligence."
Key Components:
Particles: Each candidate solution is treated as a "particle" moving through a multi-dimensional
search space.
Velocity: Every particle has a speed and direction that determines its next position.
The Search Process:
Personal Best (pBest): Each particle remembers the best location it has personally reached so
far.
Global Best (gBest): The swarm communicates to find the best location reached by any particle
in the entire group.
Movement Logic: In every iteration, a particle adjusts its velocity based on its current direction,
its desire to return to its pBest, and its desire to move toward the swarm’s gBest.
********** 5 **********
--- page 6 ---
Feature   Genetic Algorithm (GA)   Particle Swarm
Optimization (PSO)
Inspiration   Biological Evolution   Social Behavior
(Flocking)
Logic   Selection, Crossover,   Velocity and Position
Mutation   updates
Memory   Population changes; past   Particles remember their
states are lost   best positions
Complexity Generally more complex to Simpler math; fewer
implement   parameters to tune
Q5   a Option Pricing Model – Answer Structure (10 Marks)   (10
CO-2;   marks)
SO-2;   1. Introduction to Option Pricing Models (1 mark)
BL-3   2. Assumptions of the Model (2 marks)
3. Concept of No-Arbitrage Principle (1 mark)
4. Derivation of the Model (Mathematical Formulation) (2 marks)
5. Key Parameters and Variables (1 mark)
6. The Pricing Formula (2 marks)
7. Applications and Limitations – (1 mark)
CO-3; b   (10
SO-   Class Interval   Observed   Expected
marks)
6;   O   E
BL-4   O-E   (O-E)2   (O-E)2/E
0.0 – 0.2   21   20   1   1   0.05
0.2 – 0.4   18   20   -2   4   0.20
0.4 – 0.6   22   20   2   4   0.20
0.6 – 0.8   19   20   -1   1   0.05
0.8 – 1.0   20   20   0   0   0.00
Total   100   100   0.50
(8 marks)
The calculated Chi-square value is 0.50. Since this is less than the critical value of 3.84, we
conclude that the difference between observed and expected frequencies is not statistically
significant.(2 marks)
********** 6 **********
--- page 7 ---
Q6   a   (10
CO-2;   marks)
SO-1;
BL-3
(5 marks)
Solution
(5 marks)
CO-3; bGradient Descent Method (4 marks)   (10marks)
SO-1;
BL-3   • An iterative optimization algorithm used to find the minimum of a multivariable
function.
• Based on moving in the direction of the negative gradient (steepest descent).
• Requires only first-order derivatives
• Simple and widely used in machine learning
Newton’s Method (4 marks)
• A second-order optimization method using both gradient and curvature.
• Uses the Hessian matrix to improve convergence speed.
•   Faster convergence near the optimum
• Requires computation and inversion of Hessian
Differences Between Gradient Descent and Newton’s Method (2 marks)
Aspect   Gradient Descent   Newton’s Method
Derivatives   First-order   First + second-order
used   (gradient)   (Hessian)
Convergence Slow (linear)   Fast (quadratic near
optimum)
Computation Low cost   High cost (matrix
inversion)
Step size   Needs tuning   Automatically determined
********** 7 **********

[Text in pictures on this page, read by OCR]
Using the internal points P1(1/3, 2/3), P2(2/3,2/3), P3(1/3, 1/3), and P4(2/3, 1/3), the
system is:

1. For P1:0+ P24+ 60+ P3—4- Pl = —0.89
2. For P2: Pl+60+60+ P}-4-P2= —1.78
3. For P3:0+ P+ PI+0-4- P38 = —044

4. For P4: P34+604+ 24+0-4-P4= —0.89
--- page 8 ---
Suitability   Large-scale   Small/medium problems
problems
Gradient Descent is simple and scalable, while Newton’s method is more accurate and
faster but computationally expensive.
Q7   a Simulation of SIR Model for 5 Days (6 marks)   (10marks)
CO-3;
SO-5;   Day   Susceptible   Infected   Recovered
BL-3   0   990.0000   10.0000 0.0000
1   987.0300   11.9700 1.0000
2   983.4856   14.3174 2.1970
3   979.2630   17.1087 3.6283
4   974.2365   20.4243 5.3392
5   968.2660   24.3519 7.3821
(ii) Basic Reproduction Number R0 (2 marks)
R0=β/γ=0.3/0.1=3
(iii) Interpretation of R0 (2 marks)
• R0=3 , Each infected individual infects 3 others on average
• The infection will spread in the population (epidemic growth)
• This is consistent with the table where the number of infected individuals increases
over time
The SIR simulation shows a rising infection trend, and since R0>1R_0>1R0>1, the disease
spreads rapidly through the population.
CO-3; b   (10
SO-2; 1. 0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
marks)
BL-4
0.02 (Level 1)   0   0.1680   0.2880   0.3120   0.1920   0
0.04 (Level 2)   0   0.1440   0.2400   0.2400   0.1560   0
2. Crank-Nicolson Method (Implicit) (5 marks)
0.00 (Initial)   0   0.1920   0.3360   0.3840   0.2880   0
********** 8 **********
--- page 9 ---
(0.02 (Level 1) 0 0.1633 0.2598 0.2796 0.2066 0

(0.04 (Level 2) 0 0.1384 0.2110 (0.2223 (0.1601 0

FIC QF OH ar
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 6f9cb2c6c755

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/MODELLING AND SIMULATION/ANS_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: mixed (6 pages), mean OCR confidence 71.3
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 11 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
a Do’s (2.5 marks)
•   Clearly define the objective and scope of the model (0.5)
•   State realistic and explicit assumptions (0.5)
• Keep the model as simple as possible but adequate (0.5)
•   Validate the model using data or known results (0.5)
CO-   •   Interpret results in real-world context (0.5)
;
O-   (5 marks)
;   Don’ts (2.5 marks)
BL-1
• Do not include unnecessary complexity or variables (0.5)
• Do not ignore limitations or assumptions (0.5)
• Do not overfit the model to limited data (0.5)
• Do not misinterpret results without validation (0.5)
• Do not neglect units, scaling, or consistency (0.5)
b Single species (exponential) growth model (2 marks)   (5 marks)
Model: dN/dt=rN, where N(t) = population, r = growth rate (1)
CO-
;   Solution: N(t)=N0ert , shows exponential increase/decay (1)
O-
;
BL-1   Assumptions: unlimited resources, no competition, constant growth rate, homogeneous
population (any two) (1)
********** 1 **********
--- page 2 ---
c   (5 marks)
CO-
;
O-
;
BL-2
d Define bounding region enclosing the object (2)
CO-   Generate large number of random points in region (1)
;
O-   Count points falling inside object using indicator function (1)   (5 marks)
;
BL-3   Estimate volume: V=(fraction inside)×(volume of region) (1)
a Architecture (5 marks)
Trainable parameters (5 marks)
Q2
• Between input (3) and hidden layer 1 (4): weights = 3×4 = 12, biases = 4 → total = 16
CO-1;   (1.5)   (10marks)
SO-   • Between hidden layer 1 (4) and hidden layer 2 (3): weights = 4×3 = 12, biases = 3 → total
;   = 15 (1.5)
BL-3   • Between hidden layer 2 (3) and output (1): weights = 3×1 = 3, bias = 1 → total = 4 (1.5)
•   Total trainable parameters = 16 + 15 + 4 = 35 (0.5)
b Model formulation (6 marks)
Assumptions (4 marks)
CO-2;   (10
O-5;   • Resources are limited and shared by both species (1)
BL-4   • Population is homogeneous with no age or spatial structure (1)   marks)
• Environment remains constant over time (1)
•   Interaction between species is proportional to their populations (1)
a   • Multiple linear regression models relationship between one dependent variable and
multiple independent variables (1)
Q3   •   It explains how changes in predictors affect the response variable (1)
CO-1;   • Assumes a linear relationship between dependent and independent variables (1)
SO-   • Used for prediction and interpretation of variable effects (1)   (10marks)
;
BL-2   Assumptions (3 marks)
• Linear relationship between variables (1)
********** 2 **********

[Text in pictures on this page, read by OCR]
¢ General form: Auzx + Buzy + Cuy +--+ = 0 (0.5)

* Discriminant: D = B? — 4AC (0.5)


+ A=5,B=3,C =—7(05)

« D=3? —4(5)(—7) = 9 + 140 = 149 > 0 = hyperbolic (1)
For Muze + 3Uxy — 2uyy + +++ = 0:

+ A=m,B=3,C =—2(05)

« D=9-—4(m)(—2) = 9 + 8m (05)
Conditions:

¢ Elliptic: D<0+>9+8m<0>m< —9/8 (0.5)
¢ Parabolic: D = 0 > m = —9/8 (0.5)
--- page 3 ---
• Independence of errors (0.5)
• Constant variance of errors (homoscedasticity) (0.5)
•   Errors are normally distributed (0.5)
• No strong multicollinearity among predictors (0.5)
Performance metrics (3 marks)
•   Coefficient of determination indicates goodness of fit (1)
• Adjusted measure accounts for number of predictors (0.5)
• Mean squared error measures average prediction error (0.5)
• Root mean squared error gives error in original scale (0.5)
• Mean absolute error measures average absolute deviation (0.5)
b
1. Distribution & RN Mapping (2 Marks)
To simulate the system, we first establish the cumulative probability ranges for both Inter-Arrival
Time (IAT) and Service Time (ST) based on the provided data.
IAT Distribution (Equal Prob 0.125)   ST Distribution (Given Probs)
1 min: 001–125   1 min: 01–15
2 min: 126–250   2 min: 16–35
3 min: 251–375   3 min: 36–60
4 min: 376–500   4 min: 61–80
5 min: 501–625   5 min: 81–90
6 min: 626–750   6 min: 91–00
7 min: 751–875
8 min: 876–000
2. Simulation Table (4 Marks)
We process 10 customers sequentially, determining their arrival times, service start/end times,
CO-2;   and any resulting delays or idle periods.
SO-   (10
;   Cust   IAT   AT   ST   Start   End   Wait   Idle
marks)
BL-3   1   0   4   0   4   0   0
2   2   2   1   4   5   2   0
3   6   8   6   8   14   0   3
4   4   12   2   14   16   2   0
5   1   13   1   16   17   3   0
6   8   21   4   21   25   0   4
7   4   25   3   25   28   0   0
8   2   27   2   28   30   1   0
9   7   34   5   34   39   0   4
10   3   37   3   39   42   2   0
Total   10   11
3. Final Calculations & Synthesis (4 Marks)
The primary metrics are derived from the total wait time and the cumulative idle time relative to
the total duration of the simulation.
Average Waiting Time (2M)
********** 3 **********
--- page 4 ---
Calculation: Total Wait Time / Total Customers
10 minutes / 10 customers = 1 minute per customer
Probability Teller is Idle (2M)
Calculation: Total Idle Time / Total Simulation Time 11 minutes / 42 minutes = 0.262
a Iteration 1- 5 marks
Iteration 2- 5 marks
Q4
Node   Initial Value   Final (2 Iter)   Current Residual
CO2-;   (10
A   1203   1206.25   0
SO-   marks)
;   B   786   789   3.25
BL-4   C   1036   1036   15.25
D   453   453   13
b
CO-2;
SO-
(10marks)
;
BL-3
Q5   a Fundamental Assumptions (3M)
CO-2;   Geometric Brownian Motion (GBM) Dynamics (3M)   (10marks)
O-2;   Role of Brownian Motion in Finance (3M)
BL-3   Model Convergence & Conclusion (1M)
b LCG Sequence Generation (3M)
Uniform Transformation (2M)
Chi-Square Hypothesis & Binning () (2M)
CO-3;   Statistic Calculation (2M)
SO-   Critical Comparison (1M)   (10
;   Numerical Results:   marks)
BL-4   Sequence: 6, 1, 8, 11, 10, 5, 12, 15, 14, 9
Calculated statistic: 1.6
Uniformly Distributed (1.6 < 3.84 )
Q6   a
(10
CO-2;
O-1;   marks)
BL-3
********** 4 **********

[Text in pictures on this page, read by OCR]
. PSO Algorithm IM New Position P1:

|. Concept & Inspiration 2M

OM (1,2)
’, Principles (Cognitive/Social) aM
3. Update Equations 1M

1. Numerical Solution (PT)

5. Final Result & Convergence
--- page 5 ---
b | 4. Gradient Descent Definition (2M)
1. Algorithm: X,4) = X, —aW f(X,,).

2. Step size a controls update magnitude; too large causes oscillation.

2. Gradient Derivation (2M)

af af
1. Vf. y= |S. ] =[2x,4yl.
Fy) E 2) [2x, dy]
0-3; 3. Iteration 1 Calculation (4M)
O-1; 1. x) =2-0.102%2)=2-04=16 (10marks:

3L-3
2. y = 1-O14x 1l=1-04=0.6
4. Convergence Analysis (2M)
1. f(xp yp) 1.67 + 2(0.67) = 2.56 + 0.72 = 3.28 (Reduced from 6.0).

Final Numerical Results (After 1 Iteration):
* New Point: (1.6, 0.4)

* Objective Value: 3.28
a 1. Model Assumptions (2M)

1. Fixed population (N = S+ 7+ R); No births/deaths.

2. Infection rate is proportional to contact between Sand I.

2. System of Differential Equations (4M)

dS _ _ BST
dt WN
dl pst
fa _yr
7 ai N
0-3: dR (10marks)
> 3. —=y7I y
0-5; a

3L-3 .
3. Reproduction Number Ry (3M)

1. Ro = ‘ (Ratio of infection rate to recovery rate).

4, Significance (1M)
1. If Ro > 1, epidemic spreads; if Ro < 1, disease dies out.

Final Result:
* Key Metric: Ro = fi'y.

FIC DI EH ar
--- page 6 ---
1. Implicit Scheme Setup (2M)
1. r= Kh? = 1/4,

2. Equation: —0.25u;_) j4) + 2.5u

+ 0.250; 4) j-
2. Initial Values (2M)
1. u( 1/3, 0) = sin(z/3) = 0.866

2. u(2/3, 0) = sin(2/3) = 0.866

ij) — 0.25u

it = 0.25,

i-1j + 15g; ;

il j4l

3. Matrix Reduction & Iteration (4M)

1. By symmetry uw) = up.

2. 2.25uy.., = 1.73(0.866) = 1.5155.

new

3. Upey = 1.5155/2.25 = 0.6735.

4. Step 5 Progression (2M)

1. Values decay by factor of (1.75/2.25) per step.

Final Numerical Results (Step 1):
« u(1/3, t)): 0.6735

» _u(2/3, ty): 0.6735

(10

marks)

FIC 6 I HF
````
