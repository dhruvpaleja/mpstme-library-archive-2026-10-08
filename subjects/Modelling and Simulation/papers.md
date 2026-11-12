# Modelling and Simulation: question papers in full

35 unique papers · 2015-16 to 2025-26 · Common (all branches), Mechatronics, Artificial Intelligence, Computer Engineering, Cyber Security, Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 6 · paper 6e6bc30c7275

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/MODELLING AND SIMULATION/QP_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO-1 ;   a
SO-2 ;   State the assumptions of Linear Regression Model.   (5 marks)
BL-1
CO-2 ;   b   Explain Allee effect and how it is incorporated in population growth model.   (5 marks)
SO-5 ;
BL-1
CO-3 ;   c   Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and   (5 marks)
SO- 1;   find conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic
BL-2   or elliptic.
CO- 3;   d   Discuss the steps of the Monte Carlo Algorithm to calculate Area.   (5 marks)
SO-2 ;
BL-3
a   Explain the architecture of a feedforward neural network and its
optimization. For a Neural Network with following structure calculate no. of
Q2
trainable parameters,
CO-1;   • Input layer: 2 neurons   (10marks)
SO-2;   • Hidden layer 1: 4 neurons
BL-3   • Hidden layer 2: 3 neurons
• Output layer: 1 neuron
b Two competing species, are modelled by the following system of autonomous
differential equations:
𝑑𝑥
CO-2;   𝑑𝑡= 𝑥(2 −𝑥−𝑦)
SO-5;   (10 marks)
BL-4   𝑑𝑦
𝑑𝑡= 𝑦(4 −𝑥−2𝑦)
Identify all equilibrium points and examine stability against them.
********** 1 **********
--- page 2 ---
a
Q3
CO-1;   (10marks)
SO-2;
BL-2
Based on the regression result above answer the following,
i.   State the regression equation
ii.   Interpret R2.
iii.   Is the independent variable significant?
iv.   Is the overall model significant?
v.   Predict Head_size if the Brain_weight is 5 units.
b A small clinic has only one registration clerk. Patients arrive at the counter at
random intervals ranging from 2 to 9 minutes, each equally likely. The
registration time varies according to the probability distribution given below.
Registration Time Distribution
Time   Probability
(minutes)
2   0.10
3   0.20
4   0.30
5   0.20
6   0.10
7   0.10
CO-2;
SO-1;   Random Numbers for Time Between Arrivals   (10 marks)
BL-3   Patient 1   2   3   4   5   6   7   8   9   10
RN   - 284 715 039 862 451 607 198 943 326
Random Numbers for Registration Time
Patient 1   2   3   4   5   6   7   8   9 10
RN   18 73 41 96 05 67 29 84 52 11
i.   Simulate the system for 10 patients.
ii.   Determine:
1. Average waiting time of patients
2. Probability that the clerk is idle
Q4   a   Solve the Laplace equation using Jacobi’s method with the following initial
values (perform 5 iterations).   (10 marks)
CO2-;
********** 2 **********
--- page 3 ---
SO-1;
BL-4
CO-2;   b
SO-2;   Write a note on Particle swarm optimization & Genetic algorithm.   (10 marks)
BL-3
Q5   a
CO-2;   Describe the model for pricing options in detail.   (10 marks)
SO-2;
BL-3
b A sequence of 100 random numbers uniformly distributed between 0 and 1 is
generated. To test whether the numbers are uniformly distributed, the data is
grouped into the following 5 class intervals:
Class Interval Observed Frequency
CO-3;   0.0 – 0.2   21
SO-6;   0.2 – 0.4   18   (10 marks)
BL-4   0.4 – 0.6   22
0.6 – 0.8   19
0.8 – 1.0   20
Test whether the generated numbers are uniformly distributed using the Chi-
square test. (Critical value of Chi square at 5% LOS 3.84).
Q6   a   Solve the Poisson’s Equation uxx+ uyy=-36xy under the conditions
u(0,y)=0, u(1,y)=60, u(x,0)=0, u(x,1)=60, 0<x<1, 0<y<1
CO-2;   (Take h=1/3)   (10 marks)
SO-1;
BL-3
CO-3;   b   Explain the Gradient Descent & Newton’s algorithm for multivariable
SO-1;   optimization. Discuss the difference between the two methods.   (10marks)
BL-3
Q7   a A closed population of 1000 individuals is exposed to an infectious disease.   (10marks)
CO-3;   The population is divided into three compartments: Susceptible S(t), Infected
********** 3 **********
--- page 4 ---
SO-5;   I(t) & Recovered R(t) with initial values S(0)=990, I(0)=10, R(0)=0 & rates
BL-3   Infection rate: β=0.3 , Recovery rate: γ=0.1 & Time step: Δt=1 day
i. Simulate the SIR model for 5 days.
ii. Compute the basic reproduction number:
iii. Interpret the value of R0
b   Solve the boundary value problem ut=uxx under the conditions u(0,t)=0,
CO-3;   u(1,t)=0, u(x,0)=x(1−x2), 0<x<1, using the Schmidt method
SO-2;   (Take h=0.2 and k=0.02)   (10 marks)
BL-4   Carry out the computations for the first two time levels using Schmidt
Method & one next level using Crank-Nicolson Method.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 88a7b88bddd2

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/MODELLING AND SIMULATION/QP_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO-1 ;   a
SO-2 ;   State the assumptions of Linear Regression Model.   (5 marks)
BL-1
CO-2 ;   b   Explain Allee effect and how it is incorporated in population growth model.   (5 marks)
SO-5 ;
BL-1
CO-3 ;   c   Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and   (5 marks)
SO- 1;   find conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic
BL-2   or elliptic.
CO- 3;   d   Discuss the steps of the Monte Carlo Algorithm to calculate Area.   (5 marks)
SO-2 ;
BL-3
a   Explain the architecture of a feedforward neural network and its
optimization. For a Neural Network with following structure calculate no. of
Q2
trainable parameters,
CO-1;   • Input layer: 2 neurons   (10marks)
SO-2;   • Hidden layer 1: 4 neurons
BL-3   • Hidden layer 2: 3 neurons
• Output layer: 1 neuron
b Two competing species, are modelled by the following system of autonomous
differential equations:
𝑑𝑥
CO-2;   𝑑𝑡= 𝑥(2 −𝑥−𝑦)
SO-5;   (10 marks)
BL-4   𝑑𝑦
𝑑𝑡= 𝑦(4 −𝑥−2𝑦)
Identify all equilibrium points and examine stability against them.
********** 1 **********
--- page 2 ---
a
Q3
CO-1;   (10marks)
SO-2;
BL-2
Based on the regression result above answer the following,
i.   State the regression equation
ii.   Interpret R2.
iii.   Is the independent variable significant?
iv.   Is the overall model significant?
v.   Predict Head_size if the Brain_weight is 5 units.
b A small clinic has only one registration clerk. Patients arrive at the counter at
random intervals ranging from 2 to 9 minutes, each equally likely. The
registration time varies according to the probability distribution given below.
Registration Time Distribution
Time   Probability
(minutes)
2   0.10
3   0.20
4   0.30
5   0.20
6   0.10
7   0.10
CO-2;
SO-1;   Random Numbers for Time Between Arrivals   (10 marks)
BL-3   Patient 1   2   3   4   5   6   7   8   9   10
RN   - 284 715 039 862 451 607 198 943 326
Random Numbers for Registration Time
Patient 1   2   3   4   5   6   7   8   9 10
RN   18 73 41 96 05 67 29 84 52 11
i.   Simulate the system for 10 patients.
ii.   Determine:
1. Average waiting time of patients
2. Probability that the clerk is idle
Q4   a   Solve the Laplace equation using Jacobi’s method with the following initial
values (perform 5 iterations).   (10 marks)
CO2-;
********** 2 **********
--- page 3 ---
SO-1;
BL-4
CO-2;   b
SO-2;   Write a note on Particle swarm optimization & Genetic algorithm.   (10 marks)
BL-3
Q5   a
CO-2;   Describe the model for pricing options in detail.   (10 marks)
SO-2;
BL-3
b A sequence of 100 random numbers uniformly distributed between 0 and 1 is
generated. To test whether the numbers are uniformly distributed, the data is
grouped into the following 5 class intervals:
Class Interval Observed Frequency
CO-3;   0.0 – 0.2   21
SO-6;   0.2 – 0.4   18   (10 marks)
BL-4   0.4 – 0.6   22
0.6 – 0.8   19
0.8 – 1.0   20
Test whether the generated numbers are uniformly distributed using the Chi-
square test. (Critical value of Chi square at 5% LOS 3.84).
Q6   a   Solve the Poisson’s Equation uxx+ uyy=-36xy under the conditions
u(0,y)=0, u(1,y)=60, u(x,0)=0, u(x,1)=60, 0<x<1, 0<y<1
CO-2;   (Take h=1/3)   (10 marks)
SO-1;
BL-3
CO-3;   b   Explain the Gradient Descent & Newton’s algorithm for multivariable
SO-1;   optimization. Discuss the difference between the two methods.   (10marks)
BL-3
Q7   a A closed population of 1000 individuals is exposed to an infectious disease.   (10marks)
CO-3;   The population is divided into three compartments: Susceptible S(t), Infected
********** 3 **********
--- page 4 ---
SO-5;   I(t) & Recovered R(t) with initial values S(0)=990, I(0)=10, R(0)=0 & rates
BL-3   Infection rate: β=0.3 , Recovery rate: γ=0.1 & Time step: Δt=1 day
i. Simulate the SIR model for 5 days.
ii. Compute the basic reproduction number:
iii. Interpret the value of R0
b   Solve the boundary value problem ut=uxx under the conditions u(0,t)=0,
CO-3;   u(1,t)=0, u(x,0)=x(1−x2), 0<x<1, using the Schmidt method
SO-2;   (Take h=0.2 and k=0.02)   (10 marks)
BL-4   Carry out the computations for the first two time levels using Schmidt
Method & one next level using Crank-Nicolson Method.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 1e43ec4147e3

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/MODELLING AND SIMULATION/QP_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO-1 ;   a
SO-2 ;   State the assumptions of Linear Regression Model.   (5 marks)
BL-1
CO-2 ;   b   Explain Allee effect and how it is incorporated in population growth model.   (5 marks)
SO-5 ;
BL-1
CO-3 ;   c   Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and   (5 marks)
SO- 1;   find conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic
BL-2   or elliptic.
CO- 3;   d   Discuss the steps of the Monte Carlo Algorithm to calculate Area.   (5 marks)
SO-2 ;
BL-3
a   Explain the architecture of a feedforward neural network and its
optimization. For a Neural Network with following structure calculate no. of
Q2
trainable parameters,
CO-1;   • Input layer: 2 neurons   (10marks)
SO-2;   • Hidden layer 1: 4 neurons
BL-3   • Hidden layer 2: 3 neurons
• Output layer: 1 neuron
b Two competing species, are modelled by the following system of autonomous
differential equations:
𝑑𝑥
CO-2;   𝑑𝑡= 𝑥(2 −𝑥−𝑦)
SO-5;   (10 marks)
BL-4   𝑑𝑦
𝑑𝑡= 𝑦(4 −𝑥−2𝑦)
Identify all equilibrium points and examine stability against them.
********** 1 **********
--- page 2 ---
a
Q3
CO-1;   (10marks)
SO-2;
BL-2
Based on the regression result above answer the following,
i.   State the regression equation
ii.   Interpret R2.
iii.   Is the independent variable significant?
iv.   Is the overall model significant?
v.   Predict Head_size if the Brain_weight is 5 units.
b A small clinic has only one registration clerk. Patients arrive at the counter at
random intervals ranging from 2 to 9 minutes, each equally likely. The
registration time varies according to the probability distribution given below.
Registration Time Distribution
Time   Probability
(minutes)
2   0.10
3   0.20
4   0.30
5   0.20
6   0.10
7   0.10
CO-2;
SO-1;   Random Numbers for Time Between Arrivals   (10 marks)
BL-3   Patient 1   2   3   4   5   6   7   8   9   10
RN   - 284 715 039 862 451 607 198 943 326
Random Numbers for Registration Time
Patient 1   2   3   4   5   6   7   8   9 10
RN   18 73 41 96 05 67 29 84 52 11
i.   Simulate the system for 10 patients.
ii.   Determine:
1. Average waiting time of patients
2. Probability that the clerk is idle
Q4   a   Solve the Laplace equation using Jacobi’s method with the following initial
values (perform 5 iterations).   (10 marks)
CO2-;
********** 2 **********
--- page 3 ---
SO-1;
BL-4
CO-2;   b
SO-2;   Write a note on Particle swarm optimization & Genetic algorithm.   (10 marks)
BL-3
Q5   a
CO-2;   Describe the model for pricing options in detail.   (10 marks)
SO-2;
BL-3
b A sequence of 100 random numbers uniformly distributed between 0 and 1 is
generated. To test whether the numbers are uniformly distributed, the data is
grouped into the following 5 class intervals:
Class Interval Observed Frequency
CO-3;   0.0 – 0.2   21
SO-6;   0.2 – 0.4   18   (10 marks)
BL-4   0.4 – 0.6   22
0.6 – 0.8   19
0.8 – 1.0   20
Test whether the generated numbers are uniformly distributed using the Chi-
square test. (Critical value of Chi square at 5% LOS 3.84).
Q6   a   Solve the Poisson’s Equation uxx+ uyy=-36xy under the conditions
u(0,y)=0, u(1,y)=60, u(x,0)=0, u(x,1)=60, 0<x<1, 0<y<1
CO-2;   (Take h=1/3)   (10 marks)
SO-1;
BL-3
CO-3;   b   Explain the Gradient Descent & Newton’s algorithm for multivariable
SO-1;   optimization. Discuss the difference between the two methods.   (10marks)
BL-3
Q7   a A closed population of 1000 individuals is exposed to an infectious disease.   (10marks)
CO-3;   The population is divided into three compartments: Susceptible S(t), Infected
********** 3 **********
--- page 4 ---
SO-5;   I(t) & Recovered R(t) with initial values S(0)=990, I(0)=10, R(0)=0 & rates
BL-3   Infection rate: β=0.3 , Recovery rate: γ=0.1 & Time step: Δt=1 day
i. Simulate the SIR model for 5 days.
ii. Compute the basic reproduction number:
iii. Interpret the value of R0
b   Solve the boundary value problem ut=uxx under the conditions u(0,t)=0,
CO-3;   u(1,t)=0, u(x,0)=x(1−x2), 0<x<1, using the Schmidt method
SO-2;   (Take h=0.2 and k=0.02)   (10 marks)
BL-4   Carry out the computations for the first two time levels using Schmidt
Method & one next level using Crank-Nicolson Method.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 61199ca5e3db

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/MODELLING AND SIMULATION/QP_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO-1 ;   a
SO-2 ;   State the assumptions of Linear Regression Model.   (5 marks)
BL-1
CO-2 ;   b   Explain Allee effect and how it is incorporated in population growth model.   (5 marks)
SO-5 ;
BL-1
CO-3 ;   c   Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and   (5 marks)
SO- 1;   find conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic
BL-2   or elliptic.
CO- 3;   d   Discuss the steps of the Monte Carlo Algorithm to calculate Area.   (5 marks)
SO-2 ;
BL-3
a   Explain the architecture of a feedforward neural network and its
optimization. For a Neural Network with following structure calculate no. of
Q2
trainable parameters,
CO-1;   • Input layer: 2 neurons   (10marks)
SO-2;   • Hidden layer 1: 4 neurons
BL-3   • Hidden layer 2: 3 neurons
• Output layer: 1 neuron
b Two competing species, are modelled by the following system of autonomous
differential equations:
𝑑𝑥
CO-2;   𝑑𝑡= 𝑥(2 −𝑥−𝑦)
SO-5;   (10 marks)
BL-4   𝑑𝑦
𝑑𝑡= 𝑦(4 −𝑥−2𝑦)
Identify all equilibrium points and examine stability against them.
********** 1 **********
--- page 2 ---
a
Q3
CO-1;   (10marks)
SO-2;
BL-2
Based on the regression result above answer the following,
i.   State the regression equation
ii.   Interpret R2.
iii.   Is the independent variable significant?
iv.   Is the overall model significant?
v.   Predict Head_size if the Brain_weight is 5 units.
b A small clinic has only one registration clerk. Patients arrive at the counter at
random intervals ranging from 2 to 9 minutes, each equally likely. The
registration time varies according to the probability distribution given below.
Registration Time Distribution
Time   Probability
(minutes)
2   0.10
3   0.20
4   0.30
5   0.20
6   0.10
7   0.10
CO-2;
SO-1;   Random Numbers for Time Between Arrivals   (10 marks)
BL-3   Patient 1   2   3   4   5   6   7   8   9   10
RN   - 284 715 039 862 451 607 198 943 326
Random Numbers for Registration Time
Patient 1   2   3   4   5   6   7   8   9 10
RN   18 73 41 96 05 67 29 84 52 11
i.   Simulate the system for 10 patients.
ii.   Determine:
1. Average waiting time of patients
2. Probability that the clerk is idle
Q4   a   Solve the Laplace equation using Jacobi’s method with the following initial
values (perform 5 iterations).   (10 marks)
CO2-;
********** 2 **********
--- page 3 ---
SO-1;
BL-4
CO-2;   b
SO-2;   Write a note on Particle swarm optimization & Genetic algorithm.   (10 marks)
BL-3
Q5   a
CO-2;   Describe the model for pricing options in detail.   (10 marks)
SO-2;
BL-3
b A sequence of 100 random numbers uniformly distributed between 0 and 1 is
generated. To test whether the numbers are uniformly distributed, the data is
grouped into the following 5 class intervals:
Class Interval Observed Frequency
CO-3;   0.0 – 0.2   21
SO-6;   0.2 – 0.4   18   (10 marks)
BL-4   0.4 – 0.6   22
0.6 – 0.8   19
0.8 – 1.0   20
Test whether the generated numbers are uniformly distributed using the Chi-
square test. (Critical value of Chi square at 5% LOS 3.84).
Q6   a   Solve the Poisson’s Equation uxx+ uyy=-36xy under the conditions
u(0,y)=0, u(1,y)=60, u(x,0)=0, u(x,1)=60, 0<x<1, 0<y<1
CO-2;   (Take h=1/3)   (10 marks)
SO-1;
BL-3
CO-3;   b   Explain the Gradient Descent & Newton’s algorithm for multivariable
SO-1;   optimization. Discuss the difference between the two methods.   (10marks)
BL-3
Q7   a A closed population of 1000 individuals is exposed to an infectious disease.   (10marks)
CO-3;   The population is divided into three compartments: Susceptible S(t), Infected
********** 3 **********
--- page 4 ---
SO-5;   I(t) & Recovered R(t) with initial values S(0)=990, I(0)=10, R(0)=0 & rates
BL-3   Infection rate: β=0.3 , Recovery rate: γ=0.1 & Time step: Δt=1 day
i. Simulate the SIR model for 5 days.
ii. Compute the basic reproduction number:
iii. Interpret the value of R0
b   Solve the boundary value problem ut=uxx under the conditions u(0,t)=0,
CO-3;   u(1,t)=0, u(x,0)=x(1−x2), 0<x<1, using the Schmidt method
SO-2;   (Take h=0.2 and k=0.02)   (10 marks)
BL-4   Carry out the computations for the first two time levels using Schmidt
Method & one next level using Crank-Nicolson Method.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 6d0a988b8480

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/MODELLING AND SIMULATION/QP_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO-1 ;   a
SO-2 ;   State the assumptions of Linear Regression Model.   (5 marks)
BL-1
CO-2 ;   b   Explain Allee effect and how it is incorporated in population growth model.   (5 marks)
SO-5 ;
BL-1
CO-3 ;   c   Classify partial differential equation Uxx + 4Uxy - 7Uyy + Ux + Uy = 0 and   (5 marks)
SO- 1;   find conditions on ‘m’ for 2Uxx + mUxy - 2Uyy + Ux + Uy = 0 to be parabolic
BL-2   or elliptic.
CO- 3;   d   Discuss the steps of the Monte Carlo Algorithm to calculate Area.   (5 marks)
SO-2 ;
BL-3
a   Explain the architecture of a feedforward neural network and its
optimization. For a Neural Network with following structure calculate no. of
Q2
trainable parameters,
CO-1;   • Input layer: 2 neurons   (10marks)
SO-2;   • Hidden layer 1: 4 neurons
BL-3   • Hidden layer 2: 3 neurons
• Output layer: 1 neuron
b Two competing species, are modelled by the following system of autonomous
differential equations:
𝑑𝑥
CO-2;   𝑑𝑡= 𝑥(2 −𝑥−𝑦)
SO-5;   (10 marks)
BL-4   𝑑𝑦
𝑑𝑡= 𝑦(4 −𝑥−2𝑦)
Identify all equilibrium points and examine stability against them.
********** 1 **********
--- page 2 ---
a
Q3
CO-1;   (10marks)
SO-2;
BL-2
Based on the regression result above answer the following,
i.   State the regression equation
ii.   Interpret R2.
iii.   Is the independent variable significant?
iv.   Is the overall model significant?
v.   Predict Head_size if the Brain_weight is 5 units.
b A small clinic has only one registration clerk. Patients arrive at the counter at
random intervals ranging from 2 to 9 minutes, each equally likely. The
registration time varies according to the probability distribution given below.
Registration Time Distribution
Time   Probability
(minutes)
2   0.10
3   0.20
4   0.30
5   0.20
6   0.10
7   0.10
CO-2;
SO-1;   Random Numbers for Time Between Arrivals   (10 marks)
BL-3   Patient 1   2   3   4   5   6   7   8   9   10
RN   - 284 715 039 862 451 607 198 943 326
Random Numbers for Registration Time
Patient 1   2   3   4   5   6   7   8   9 10
RN   18 73 41 96 05 67 29 84 52 11
i.   Simulate the system for 10 patients.
ii.   Determine:
1. Average waiting time of patients
2. Probability that the clerk is idle
Q4   a   Solve the Laplace equation using Jacobi’s method with the following initial
values (perform 5 iterations).   (10 marks)
CO2-;
********** 2 **********
--- page 3 ---
SO-1;
BL-4
CO-2;   b
SO-2;   Write a note on Particle swarm optimization & Genetic algorithm.   (10 marks)
BL-3
Q5   a
CO-2;   Describe the model for pricing options in detail.   (10 marks)
SO-2;
BL-3
b A sequence of 100 random numbers uniformly distributed between 0 and 1 is
generated. To test whether the numbers are uniformly distributed, the data is
grouped into the following 5 class intervals:
Class Interval Observed Frequency
CO-3;   0.0 – 0.2   21
SO-6;   0.2 – 0.4   18   (10 marks)
BL-4   0.4 – 0.6   22
0.6 – 0.8   19
0.8 – 1.0   20
Test whether the generated numbers are uniformly distributed using the Chi-
square test. (Critical value of Chi square at 5% LOS 3.84).
Q6   a   Solve the Poisson’s Equation uxx+ uyy=-36xy under the conditions
u(0,y)=0, u(1,y)=60, u(x,0)=0, u(x,1)=60, 0<x<1, 0<y<1
CO-2;   (Take h=1/3)   (10 marks)
SO-1;
BL-3
CO-3;   b   Explain the Gradient Descent & Newton’s algorithm for multivariable
SO-1;   optimization. Discuss the difference between the two methods.   (10marks)
BL-3
Q7   a A closed population of 1000 individuals is exposed to an infectious disease.   (10marks)
CO-3;   The population is divided into three compartments: Susceptible S(t), Infected
********** 3 **********
--- page 4 ---
SO-5;   I(t) & Recovered R(t) with initial values S(0)=990, I(0)=10, R(0)=0 & rates
BL-3   Infection rate: β=0.3 , Recovery rate: γ=0.1 & Time step: Δt=1 day
i. Simulate the SIR model for 5 days.
ii. Compute the basic reproduction number:
iii. Interpret the value of R0
b   Solve the boundary value problem ut=uxx under the conditions u(0,t)=0,
CO-3;   u(1,t)=0, u(x,0)=x(1−x2), 0<x<1, using the Schmidt method
SO-2;   (Take h=0.2 and k=0.02)   (10 marks)
BL-4   Carry out the computations for the first two time levels using Schmidt
Method & one next level using Crank-Nicolson Method.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 5 · paper 31435eb13f7c

- Departments: Common (all branches)
- Programmes: B TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/MODELLING & SIMULATION/Modeling and Simulation, Sem-V, Year 2025-26, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Dec 2025
- Text: ocr (3 pages), mean OCR confidence 88.0

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (EXTC)/B. Tech (IT)/B.
Tech (MECH) “ oy
Year: III/Semester V(Exam Year: 2025-2026) ie
Subject: MODELLING AND SIMULATION
Date: 11 Dec 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.
Max. Marks: 100 ;

FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Figure in right hand side indicates full marks
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
> 8. Assume Suitable data if necessary.

Ql
CO-1; SO- 1; | a. | Discuss the need for modeling real-world systems. Mention at least three benefits of 5
BL-1 building models.
CO- 1; SO- 1; |b. . . . : ae .
BL-2 Explain the working principle of the Particle Swarm Optimization (PSO) algorithm. 5
CO-1; SO-2; | c. | State and classify the 2" order PDE for the following: Laplace, Poisson, wave & 5
BL-3 heat equation. . .
CO-1; SO-1; | d. | List the steps involved in the Monte Carlo algorithm for estimating the price of an 5
BL-2 option.
Q2
_ a. 10
( %- 1; SO-2; . . . .. .
BL-3 Explain the concept and mathematical formulation of logistic regression.
b. | Derive population growth model and discuss its limitations in realistic environments.
CO- 2; SO-6; Also, Extend the model to include environmental carrying capacity (K). 10
BL-4
Q3
a. | Draw the architecture of a simple feedforward neural network with the following
structure:
SSAA. e 3 input neurons
, One 1} ¢ 1 hidden layer with 4 neurons 18

e 2 output neurons

Write the mathematical expressions for the weighted sum and activation at each
layer. Also, Calculate the total number of trainable parameters in the network.

FG 7 ao ok kk
.
--- page 2 ---
OO b Explain Monte Carlo Simulation and state the algorithm to calculate area. 10,

Q4

a. | A two-species interaction model is described by the following, syétem of differential

equations:
dxdt=x(3-x—y)
CO- 2; SO-6; dydt=y(2x—4) 10
BL-4

where x represents the prey population and y represents the predator population.
Find all equilibrium points of the system. Determine the nature and stability of each
equilibrium point using eigenvalue analysis.

b.
Given the values of u(x, y) on the boundary of the square in the Figure evaluate the
function u(x, y) satisfying the Laplace equation Vu = 0 at the pivotal points of this
figure using Gauss seidel perform 5 iterations.
1 1 ce |
CO-2; SO-2; 10
BL-3 »
0 z, —|a, 0
0 a, ui, 0
0 0
Q5
CO-2: 80-6: | * Solve the boundary value problem u=u,x under the conditions u(0,t)=u(1,t)=0 and
BL-3 > u(x,0)=sin(zx), OSx<1 using the Crank Nicholson . Take h=0.2 and a=1/2 10
(perform for 4 time steps)
b. | At a car wash centre, cars arrive randomly, and service times vary as per the given iy
probability distributions. The centre can wash only one car at a time.
Simulate the operation for 10 cars using the random numbers below and evaluate:
1. Average waiting time for cars
2. Probability that a car waits before service
3. Average service time
CO-3; SO-1; Arrival Time Distribution ib
BL-2 Interarrival Probability
Time
(minutes)
3 0.10
* 4 0.25 +
. 5 0.30
6 0.20
7 P 0:15

FROCK 2 Rk x
--- page 3 ---
Service Time Distribution

Service Time Probability
(minutes)
3 0.15 oe
4 0.30
5 0.25
6 0.20
7 0.10

Random Numbers‘ for Simulation

° Arrival Time: 214, 650, 372, 945, 581, 103, 497, 766, 322
° Service Time: 25, 48, 73, 12, 95, 61, 30, 88, 57, 42

26
*- | Solve the one-dimensional heat equation, u=uxx using the Schmidt method for am
a=0.5 2
| j\i | 0 1 2 3 4 5 6 7 8
CO-2; SO- 1; 0 0 4 7 9 | 10} 9 7 4 0
BL-2

1 0 0

2 0 0

3 0 0

CO-3: §O- |: b. | Consider the cost function: J(x,y)=4x*+y?+3xy which represents the error surface

BL-4 of a predictive model. Using the Gradient Descent method, perform three iterations | 10 ;
starting from the initial guess (xo,yo)=(3,1) and a learning rate of 0.05.
Q7

CO-2; SO- 1; | a. | Derive the SIR model and explain its components. Demonstrate a short simulation of | 10
_ BL3 the SIR model for 4 days by assuming suitable rates.

CO-3; SO- 1; | b. | Generate 10 random numbers using the Linear Congruential Generator (LCG) with | 10
BL-4 the following parameters: a=5, c=3, m=16, X0=7.Then, test whether these numbers
are uniformly distributed in the interval [0, 1) using the Chi-Square test at a 5%
significance level. (critical value for chi square test is 9.488)

FI OR Ak
````

## 2025-26 · Re-Exam · Sem 6 · paper f3523b58be3e

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/MODELLING AND SIMULATION/QP_MODELLING AND SIMULATION(702BS0I018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (IT)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: MODELLING AND SIMULATION
Date: 11 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO-1 ;   a
SO-2 ;   State the do’s and don'ts of mathematical modelling.   (5 marks)
BL-1
CO-2 ;   b   Explain the single species (exponential) growth model and state its   (5 marks)
SO-5 ;   assumptions.
BL-1
CO-3 ;   c   Classify partial differential equation 5Uxx + 3Uxy - 7Uyy + Ux + Uy =   (5 marks)
SO- 1;   0 and find conditions on ‘m’ for mUxx + 3Uxy - 2Uyy + Ux + Uy = 0
BL-2   to be parabolic or elliptic.
CO- 3;   d   Discuss the steps of the Monte Carlo Algorithm to calculate volume.   (5 marks)
SO-2 ;
BL-3
a   Explain the architecture of a feedforward neural network, including
layers, neurons, and activation functions. Also, calculate the total
Q2
number of trainable parameters for a network with:
CO-1;   • Input layer: 3 neurons   (10marks)
SO-2;   • Hidden layer 1: 4 neurons
BL-3   • Hidden layer 2: 3 neurons
• Output layer: 1 neuron
b   Develop a system of differential equations to model the competitive
CO-2;   interaction between two species competing for the same resources,
SO-5;   incorporating intrinsic growth rates, self-limiting effects, and   (10 marks)
BL-4   interspecific competition. State at least four assumptions and write
the model.
Q3   a
Explain Multiple Linear Regression. State its key assumptions and
CO-1;   discuss appropriate metrics used to evaluate the performance of the   (10marks)
SO-2;   model.
BL-2
********** 1 **********
--- page 2 ---
b A small bank has only one teller. Customers arrive at the counter at
random times ranging from 1 to 8 minutes apart, with equal probability.
The service time varies from 1 to 6 minutes with the probabilities given
below. Simulate the system for 10 customers and hence find Average
waiting time & Probability that the teller is idle.
Service Time Distribution
Time (minutes) Probability
1   0.15
2   0.20
CO-2;   3   0.25
SO-1;   4   0.20   (10 marks)
BL-3   5   0.10
6   0.10
Random Numbers for Time Between Arrivals
Customer 1   2   3   4   5   6   7   8   9   10
RN   - 145 672 389 058 921 476 230 804 317
Random Numbers for Service Time
Customer 1   2   3   4   5   6   7   8   9 10
RN   72 14 95 33 08 61 47 22 89 55
a   Solve the Laplace equation using relaxation method with the following
initial values at A,B,C & D (perform 2 iterations)
Q4
CO2-;   (10 marks)
SO-1;
BL-4
********** 2 **********
--- page 3 ---
b   Explain the Particle Swarm Optimization (PSO) algorithm.
Using PSO Minimize: f(x,y)=x2+y2
CO-2;   Given:
SO-2;   (10marks)
BL-3   •   Particle 1: (2,3), velocity = (0,0)
•   Particle 2: (−1,2), velocity = (0,0)
Assume Particle 2 as the Global best. Perform one iteration for Particle
1 and find its new position.
Q5   a
Describe the assumptions of the Black–Scholes model, the stock price
CO-2;   dynamics using geometric Brownian motion, and the role of Brownian   (10marks)
SO-2;   motion in financial modelling.
BL-3
b   Generate random numbers using the Linear Congruential Generator:
CO-3;   Xn+1=(5Xn+3)  mod  16 with seed X0=7
SO-6;   (10 marks)
BL-4   Generate 10 random numbers and convert them into uniform random
numbers: Test whether the generated numbers are uniformly distributed
using the Chi-square test. (Take critical Chi square value at 0.05 is 3.84)
Q6   a   Solve the boundary value problem ut=uxx under the conditions u(0,t)=0,
u(1,t)=0, u(x,0)=x(1−x), 0<x<1, using the Schmidt method
CO-2;   (Take h=0.25 and α=1/4, Perform 5 iterations)   (10 marks)
SO-1;
BL-3
b   Explain the Gradient Descent algorithm for multivariable optimization.
CO-3;   Discuss the role of step size and explain its convergence behaviour.
SO-1;   Using gradient descent algorithm Minimize the function: f(x,y)=x2+2y2   (10marks)
BL-3   Initial point: (x0,y0)=(2,1) with Step size: α=0.1(Perform 2 iterations).
Q7   a   Formulate the SIR (Susceptible–Infected–Recovered) model for the
CO-3;   spread of an infectious disease. Clearly state the assumptions, derive the   (10marks)
SO-5;   system of differential equations, and define the basic reproduction
BL-3   number R0 along with its significance in disease dynamics.
CO-3;   b   Solve the one-dimensional heat equation Ut=Uxx subject to u(0,t)=0,
SO-2;   u(1,t)=0, u(x,0)=sin(πx), 0<x<1 Use step sizes h=1/3,  k=1/36 for x &   (10 marks)
BL-4   t respectively. Perform 5 time step iterations Using Crank Nicholson
Method.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper f599a2e6ef3d

- Departments: Artificial Intelligence, Computer Engineering, Cyber Security, Information Technology
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, B TECH / CSE CYBER SECURITY, B TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/MODELLING AND SIMULATION/Modelling and Simulation, Sem-VI, Batch 2025-26, Re Exam.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: ocr (3 pages), mean OCR confidence 85.4

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech (AI)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (ITPMBA Tech (AID)
Year: HI/Sem 6 Re-exam(Exam Year: 2025-2026) © ks
Subject: MODELLING AND SIMULATION

Date: 11 Jul 2026 Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100

RE EXAMINATION (Acad. Year:2025-2026)
Instructions:

1. This question paper contains 3 pages.
2. Question No. | is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted. MPSTME
5. All questions carry equal marks. LIBRARY
6. Answer to each new question to be started on a fresh page.

7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.

a .

Ql
Answer briefly:
CO-1; a :
SO-2 ; State the do’s and don'ts of mathematical modelling. (5 marks)
BL-1 :
CO-2 ; b Explain the single species (exponential) growth model and state its (5 marks)
SO-5 ; assumptions.
BL-1
CO-3 ; c Classify partial differential equation 5SUxx + 3Uxy - 7Uyy + Ux + Uy= (S marks)
SO- 1; 0 and find conditions on ‘m’ for mUxx + 3Uxy - 2Uyy + Ux + Uy=0
BL-2 to be parabolic or elliptic.
eae 4 | Discuss the steps of the Monte Carlo Algorithm to calculate volume. . (5 marks)
BL-3
a Explain the architecture of a feedforward neural network, including

Gy > layers; neurons, and activation functions. Also, calculate the total
Ss number of trainable parameters for a network with:
CO-1; “e Input layer: 3 neurons (10marks)
SO-2, e Hidden layer 1: 4 neurons
BL-3

e Hidden layer 2: 3 neurons
¢ Output layer: | neuron
b Develop a system of differential equations to model the competitive
a CO-2; interaction between two species competing for the same resources,
SO-5; incorporating intrinsic growth rates, self-limiting effects, and | (!0 marks)

BL-4 interspecific competition. State at least four assumptions and write
the model.
Q3 a . F P . , :
Explain Multiple Linear Regression. State its key assumptions and
CO-1; f discuss appropriate metrics used to evaluate the performance of the (10marks)
SO-2;
model.
BL-2

FOO 7 AO RR Ok
--- page 2 ---
FOCI ACHR ka

[ } ob A small bank has only one teller. Customers arrive at the counter at
random times ranging from 1 to 8 minutes apart, with equal probability.
The service time varies from 1 to 6 minutes with the probabilitigs given
below. Simulate the system for 10 customers and hence find Average
waiting time & Probability that the teller is idle. “
Service Time Distribution
Time (minutes) Probability
1 0.15
[2 L020]
CO-2; 3 0.25
SO-1; [ 4 [0.20 | (10 marks)
BL-3 5 0.10
[ 6 | 0.10 |
Random Numbers for Time Between Arrivals
Customer 1 2 3 4 5 6 7 8 9 10
RN -_145 672 389 058 921 476 230 804 317
Random Numbers for Service Time
Customer 1 2 3 4 5 6 7 8 9 40
[ RN 72_14 95 33 08°61 47 22 89 55 a )
a Solve the Laplace equation using relaxation method with the following
initial values at A,B,C & D (perform 2 iterations)
1000 1000 1000 1000
2000 a B 500
1203 786
2000 = BD 0
1036 453
“ 1000 L — _
CO2-; 500 9 Q (10 marks)
SO-1; :
BL-4 1000 1000 1000 1000, om
. | |
2000 : 5 500
2000 c xz 0
— 1000 LL :
500 0 0
--- page 3 ---
b Explain the Particle Swarm Optimization (PSO) algorithm.
i Using PSO Minimize: f(x,y)=x?+y? #
| CO-2: Given:
“| SO-2; (10marks)
BL-3 e Particle 1: (2,3), velocity = (0,0)

e Particle 2: (-1,2), velocity = (0,0)

Assume Particle 2 as the Global best. Perform one iteration for Particle
| and find its new position.

Q5 a . . .
Describe the assumptions of the Black-Scholes model, the stock price
CO-2; dynamics using geometric Brownian motion, and the role of Brownian — (19marks)

$0-2; motion in financial modelling.
BL-3
b Generate random numbers using the Linear Congruential Generator:

CO-3; Xn+1=(5Xnt+3) mod 16 with seed Xo=7
SO-6; (10 marks)
BL Generate 10 random numbers and cénvert them into uniform random

numbers: Test whether the generated numbers are uniformly distributed

using the Chi-square test. (Take critical Chi square value at 0.05 is 3.84)
Q6 a Solve the boundary value problem u=uxx under the conditions u(0,t)=0,

u(1,t)}=0, u(x,0)=x(1—x), 0<x<1, using the Schmidt method
iy (Take h=0.25 and a=1/4, Perform 5 iterations) (10 marks)
BL-3

b Explain the Gradient Descent algorithm for multivariable optimization.
CO-3: Discuss the role of step size and explain its convergence behaviour.
SO-1: Using gradient descent algorithm Minimize the function: f(x,y)=x?+2y” (10marks)
BL-3 Initial point: (xo0,yo)=(2,1) with Step size: a=0.1(Perform 2 iterations).
Q7 a Formulate the SIR (Susceptible—Infected—Recovered) model for the
CO-3: spread of an infectious disease. Clearly state the assumptions, derive the (| Qmarks)
SO-5: system of differential equations, and define the basic reproduction
>BL-3 number RO along with its significance in disease dynamics.
CO-3: b Solve the one-dimensional heat equation UU xx subject to u(0,t)=0,
SO-2: u(tt)=0, u(x,0)=sin(ax), 0<x<1 Use step sizes h=1/3, k=1/36 for x & (10 marks)
BL-4 t respectively. Perform 5 time step iterations Using Crank Nicholson
“7 Method.

Fo GR dak ii rok kd ak
````

## 2024-25 · Final-Exam · Sem 5 · paper 4b0d456e2e11

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/MODELLING & SIMULATION/Modelling and Simulation, Sem-V, Final Exam 2024-25.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11/12/2024
- Text: ocr (4 pages), mean OCR confidence 88.9

````text
SVKM’S NMIMS a
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEE
Academic Year: 2024-2025

Program: B TECH / MBA TECH Stream; All applicable streams Year: III Sentester: V
Subject: MODELLING AND SIMULATION Time: 3 hrs (Qs00pmto 5: oop)
Date:11/12/2024. f No. of Pages: 4

Marks:100

Final Examination(2024 -25)
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
(~7) Assume Suitable data if necessary.

Ql :
CO-1; SO- | a.
1; Explain linear regression and the metrics used to analyze a linear regression model. 5
BL-5
b. | A mathematician is tasked with optimizing the area of a rectangular plot under specific
CO- 1; constraints. The goal is to maximize the area of the rectangle, where the sum of the
SO- 1; lengths of two adjacent sides is 10 units. Using the method of Lagrange multipliers, | 5
BL-2 find the dimensions of the rectangle that will maximize the area.
c. | Classify the following partial differential equations:
CO-1; $0- Fug Fu Fu aw du
2: ax” dxdy ay? dx dy 5
oBL3

2
ve 4 (1-y*) ot a0,-wcxcn,—<yel
ox” ye

CO-1: SO- d. | Using the Linear Congruential Method, compute 5 random numbers with the following
I parameters: a multiplicative constant of 4, an additive constant of 7, a starting seed

3 3

BL-s value of 2, and a modulus of 9.
Q2
Co- 1; = Classify and compare the mathematical models on S & Q axes, where S denotes the 10
SO-2; system and Q denotes the question axis.
BL-3
CO-2; |b. | Discuss a mathematical model to describe the logistic growth of a population in an
SO-6; environment with limited resources. 10
BL-6
1/4
--- page 2 ---
—
Q3
Explain the concept of neural networks, including their architecture and the
mathematical principles that govern their functioning. Additionally, for a given neural
CO-2; SO- network with one hidden layer, where the input layer has 3 neurons; the hidden layer 10
1; has 4 neurons, and the output layer has 2 neurons, calculate the total number of trainable
BL-2 parameters in the network.
CO- 2; Develop a mathematical model to describe the spread of rumors in a population. Clearly
SO-6; state the assumptions in your model about the dynamics of rumor transmission. 10
BL-6
Q4
Consider the following system of differential equations that models population
dynamics:
dx
—=x(3-x- oo
CO- 2; at ¢ ») a
SO-6; dy ° 10
BL-6 ae YA-x-y) es
Find the equilibrium points of the system and also check its stability.

b. | Given the values of u(x, y) on the boundary of the square in the Figure evaluate the
function u(x, y) satisfying the Laplace equation Vu = 0 at the pivotal points of this
figure by Using Gauss-Seidal method (perform 5 iterations). :

ion 1000 1000 1000
CO-1; SO-
2; 2000 ai Ms 500 10
BL-3 +
2000 uy u, 0
1000 500 0 °
Q5
a. | Solve the partial differential equation:
CO- 2;
SO-6; Ou Pu ‘ 10
BL-6 Ot Ox?
2/4
--- page 3 ---
in 0<x<4, t20 given the boundary conditions: u(0,t)=0, u(4,t)=80
and the initial condition: u(x,0)=40 for 0<x<4.

Using a time-step of h=1, a=1 and employing the Crank-Nicolson method, compute

u for the first two time-steps.

,

A small bank has a single teller counter. Customers arrive at the counter randomly, with
the time between arrivals ranging from 1 to 7 minutes, each with equal probability. The
service times also vary, ranging from | to 5 minutes, with probabilities as shown in the
table below. Simulate the system for 8 customers using the provided random numbers
and calculate the following:

i. The average waiting time for a customer.

ii. The probability that a customer has to wait in the queue.
iii. The average service time.

iv. The average time between arrivals.

aos v. The average time a customer spends in the system.
CO-1; SO- [Service Time (minutes)|| Probability |
1; [ il [010] 10
anal 7) [025 |
| 3 [030 |
| 4 [0.20 |
| 5 [015]
Random numbers for simulation: “
e Arrival Time: 543, 812, 163, 473, 934, 265, 781, 650
e Service Time: 28, 45, 96, 13, 68, 87, 53, 24
Simulate the system using these random numbers and analyze the system’s
L performance based on the given metrics.
Q6
Solve the equation:
Au Ou
CO-2; SO- — = »___.
1; Ot = Ox? 10
BL-3
subject to the conditions: u(x,0)=cos(rx), 0<x<1; u(0,t)=u(1,t)=0.
Use the Schmidt method to carry out computations for two levels, taking h=1/4 and
k=1/64.
3/4
--- page 4 ---
¥

Consider the function f(x,y)=x*+y’+4xy, which represents the error in a machine

co a learning model. Starting from an initial guess (xo,yo)=(1,1), apply the gradient descent 10
BL- 4 method with a learning rate of 0.1 to reduce the error. Perform three iterations and find
the updated values of x and y.
Q7
CO-2; SO- Discuss Lotka Voltera model in detail. 10
1;
BL-3
CO-3; SO- Explain the concept of the Monte Carlo simulation and list the steps of an algorithm | 10
1; using the Monte Carlo method to estimate the area of a circle.
BL-4
4/4

>
````

## 2024-25 · Final-Exam · Sem 6 · paper 850cc8add094

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-VI/MODELLING AND SIMULATION/Modelling and Simulation, Sem VI, Final Exam 2024-25.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 86.2

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMEN T& ENGINEERING/

SCHOOL OF TECHNOLOGY MANAGEMENT. |

Academic Year: 2024-2025 .
Program/s: B Tech / MBA Tech / BTI Year: IIL/V Semester: VI/X
Stream/s ; All applicable streams

Subject: Modelling and Simulation _ — ; Time: 3 hrs (Aivopmto 5:00pm yor
Date:_13/ 05/2025 - .

No. of Pages:4
Marks: 100 ,

Final Examination (24- 25)
Instructions: Candidates should

U read carefully the instructions
the cover of the Auswer Book, w

printed on the question paper and on
hich is provided for their use. ae ; :
1) Question No. 1 is compulsory. ; ;
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.:
5) Answer to each new question to be started ona fresh page.

6) Figures in brackets on the right-hand side indicate full marks. : “
7) Assume Suitable data if necessary. fe

[ a —— oe
: |

O-1; SO- 1; | a. | Differentiate between deterministic and stochastic models with suitable examples. alle 5
BL-5 -
te Consider a highway system where vehicles are divided into two lanes with densities x |" °
and y (vehicles per km). The total traffic speed V(x, y) is modelled as:

CO- 1; SO- V(x,y)=50-2x-3y 7
1; The total number of vehicles must. remain constant: x+y=40. Find the optimal | 5
BL-2 distribution of vehicles (x, y) that maximizes the total traffic speed using the Lagrange | *~
; multiplier method. : ; -
c. | Classify the following partial differential equations as elliptic, parabolic, or hyperbolic,
and identify whether they represent a heat equation, wave equation, or other types of
CO-1; $O:2; sue Ms
BL-3 ; E,
a) Up = AUze :
b) ty, = CO Uss : ;
d. | List the steps involved in the Monte Carlo algorithm for estimating the area ofa given
CO-1; SO-1; SUES 7
BL-5

1/4
--- page 2 ---
SS a
Consider a neural network with an input layer of 4 neurons, @ hidden layer of 5 ;
neurons, and an output layer of 3 neurons: a ~
a) Draw the architecture.
b) Compute the total number of trainable parameters.
c) Derive the mathematical formulation of the model

Describe the Rumor Model and derive its governing equation:
the spread of rumors in a population?

CO- 1; SO-2;

BL-3
and express it in matrix form.

s. What factors influence |’

rive its

Describe logistic regression, its differences from linear regression, and de

mathematical formulation, including the sigmoid function.

Formulate the Lotka-Volterra Model and interpret the significance of its equilibrium |

-prey system is described by the following system of differential equations:

A predator

dx/dt=x(4—2x-y)
dy/dt=y(—x-2y

where x represents the prey population and y represents the predator population. .

1. Find the equilibrium points of the system.
2. Determine the stability of each equilibrium point using the Jacobian matrix and .

eigenvalues. .

the square in the Figure evaluate the
u = 0 at the pivotal points of this figure

Given the values of u(x, y) on the boundary of
function u(x, y) satisfying the Laplace equation Vv?
by Using Jacobi ‘method (perform 5 iterations).

60 60 60 60

.

2/4
--- page 3 ---
Q5

CO- 2; $0-6;
BL-6

Solve the partial differential equation:

a

ou ou
Ot Ax?

for0 < @ < 5,¢ > 0, given-the boundary conditions u(0, t) = 0, u(5,¢) = 100, and the initial
condition u(x, 0) = 50 forO<2 <5.

Using a time-step of h = 0.5, a = 1.5, and employing the Crank-Nicolson method, compute u for the

first two time steps, : ,

10

CO-1; SO-1;
BL-2

A coffee shop has a single counter where customers arrive at random intervals. The time
between arrivals ranges from 1 to 5 minutes (each with equal probability). The time

required to prepare-an ‘order varies from 2 to 6 minutes, based on the probability |,
distribution given below. Simulate the system for 12 customers using the provided Bis

random numbers and compute:

1. Average waiting time per customer
2. Probability that a customer has to: wait
3. Average service time -
4. Average time between arrivals
5. Average time spent in the system per customer

Service Time Distribution:

Service Time | Probability

minutes) :
2 0.20
3 0.25 a
4 — 0.30
6) . 0.15
6 0.10

Random Numbers for Simulation:

Arrival Time: 412, 801, 249, 578, 935, 361, 702, 127, 489, 654, 213, 871

Service Time: 21, 49/77, 39, 95, 66, 30, 85, 52, 17, 88, 43

10

3/4
--- page 4 ---
7

Q6
a. Z
Complete the following table using the Du Fort-Frankel method for a=0.8
C0-2: 80-1: ji 0 6 7 8
BL3 0 0 5 2.5 0
1 0 4.8 22 0
2 0 - - 0
3 0 - - 0
b. Given the cost function: C(x,y)=3x2+2y+5xy swhich represents a loss function in an 5
CO-3; SO- 1; |. optimization problem. Starting from the initial guess (Xo, yo) = (2,2), apply the gradient |. 10
BL-4 descent algorithm with a learning rate of 0.05 for three iterations and find the updated = [
values of x and y. :
Q7
CO-2; SO- 1; | a. | Derive the SIR Model and describe how it models the spread of infectious diseases. 10
BL3_| -
CO-3; SO- 1; | b. | Generate 10 random numbers using the Middle Square method with a 4-digit seed | 10
BL-4 1734”, Check whether these numbers are uniformly distributed using the Chi-Square | *
quare value for df= 4 at 5% is 9.488) .

test at a 5% significance level.(Critical Chi-S

ac ca

aa
````

## 2024-25 · Final-Exam · paper 90fadaf0b4ef

- Departments: Common (all branches)
- Programmes: B.TECH INTEGRATED
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/All Stream/Modelling and Simulation/Modelling and Simulation Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 87.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025

Program/s: B Tech / MBA Tech / BTI Year: IIl/V Semester: VI/X
Stream/s ; All applicable streams ; ,

Subject: Modelling and Simulation ; Time: 3 hrs (2i00pmto Stoopm )-
Date:__13/ 05 / 2025 ; No: of Pages:4

Marks: 100

Final Examination (24- 25°)

Instructions: Candidates should read carefully the instructions printed on the question paper and on
>, the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions. . ,

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks. -
7) Assume Suitable data if necessary. :

Ql

CO-1; SO- 1; | a. | Differentiate between deterministic and stochastic models with suitable exarnples.
BL-5 ”
‘b. | Consider a highway system where vehicles are divided into two lanes with densities x |.”
and y (vehicles per km). The total traffic speed V(x, y) is modelled as:

CO- 1; SO- V(x,y)=50-2x-3y :
@ 13 The total number of vehicles must. remain constant: x+y=40. Find the optimal | 5
BL-2 distribution of vehicles (x, y) that maximizes the total traffic speed using the Lagrange | ©
multiplier method. , -

c. | Classify the following partial differential equations as elliptic, parabolic, or hyperbolic,
and identify whether they represent a heat cquation, wave equation, or other types of

CO-1:; $O:2; PDEs: . : ;
BL-3 ”
a) Up = QUge :
b) Ure = C Uae
d. | List the steps involved in the Monte Carlo algorithm for estimating the area of a given
CO-1; SO-1; shape. -s

BL-5 : a

4a
--- page 2 ---
Q2

a. | Consider a neural network with an input layer of 4 neurons, a hidden layet af 5

10
. . neurons, and an output layer of 3 neurons: ~
CO- 1; SO-2;
BL3 a) Draw the architecture.
b) Compute the total number of trainable parameters.
c) Derive the mathematical formulation of the model and express it in matrix form.
CO-.2; SO-6; | b. | Describe the Rumor Model and derive its governing equations. What factors influence
. : 10
BL-6 -_| the spread of rumors in a population?
Q3
CO-2; SO-1; | a. | Describe logistic regression, its differences from linear regression, and derive its | 10,
BL-2 mathematical formulation, including the sigmoid function. .
. ; Formulate the Lotka-Volterra Model and interpret the significance of its equilibrium |:
CO- 2; SO-6; b int 10
BL-6 . | points.
~_ al
Q4
a. | A predator-prey system is described by the following system of differential equations:
dx/dt=x(4—2x-y) jo:
dy/dt=y(3-x-2y “
oo eee where x represents the prey population and y represents the predator population. ‘10,
1. Find the equilibrium points of the system.
2. Determine the stability of each equilibrium point using the Jacobian matrix and
eigenvalues. . *
b. | Given the values of u(x, y) on the boundary of the square in the Figure evaluate the
function u(x, y) satisfying the Laplace equation V7u = 0 at the pivotal points of this figure | -
by Using Jacobi method (perform 5 iterations). ;
60 60 60 60 ¥
CO-1; SO-2; “0 in ie
BL-3 s
20 40
8 10 20 30 |

2/4:
--- page 3 ---
Q5

CO- 2; SO-6;
BL-6

Solve the partial differential equation:
“ Ou aot
ot «Ox?
for 0 < x < 5,t > 0, given-the boundary. conditions u(0, ¢) = 0, u(5, £) = 100, and the initial
condition u(x, 0) = 50 for0 < @ <5.

Using a time-step of h = 0.5, a = 1.5, and employing the Crank-Nicolson method, compute u for the
first two time steps.

10 |

CO-1; SO-1;
BL-2

A coffee shop has a single counter whére customers arrive at random intervals. The time
between arrivals ranges from 1 to 5 minutes (each with equal probability). The time
required to prepare-an order varies from 2 to 6 minutes, based on the probability

distribution given below. Simulate the system for 12 customers using the provided |: .

random numbers and compute:

re

1. Average waiting time per customer

2. Probability that a customer has to wait

3. Average service time

4. Average time between arrivals

5. Average time spent in the system per customer

Service Time Distribution:

Service Time | Probability
(minutes)

2 0.20 =

3 0.25

4 {0.30

5 0.15

6 0.10

Random Numbers for Simulation:
Arrival Time: 412, 801, 249, 578, 935, 361, 702, 127, 489, 654, 213, 871

Service Time: 21, 49,77, 39, 95, 66, 30, 85, 52, 17, 88, 43

-10

a
--- page 4 ---
Q6

- 10°
Complete the following table using the Du Fort-Frankel method for o=0:8
ji 0 1 2 |. 3 4 5 6 7 8
CO-2; SO- 1; :
BL-3 0 0 2.5 5 6.5 7 6.5 5 2.5 0
1 0 3 52, =|) 6.8 6.9 6.1 4.8 2:2, 0
2 0 - - - - - - - 0
3 0 - - - - - - - 0
Given the cost function: C(x,y)=3x"+2y’+5xy ,which represents a loss function in an
CO-3; SO- 1; optimization problem. Starting from the initial guess (xo, yo) = (2,2), apply the gradient
BL-4 descent algorithm with a learning rate of 0.05 for three iterations and find the updated
values of x and y.
Q7
| a!
CO-2; SO- 1; Derive the SIR Model and describe how it models the spread of infectious diseases. 1
BL-3 7
CO-3; SO- 1; Generate 10 random numbers using the Middle Square method with a 4-digit seed | 10
BL-4 “1234”, Check whether these numbers are uniformly distributed using the Chi-Square .

test at a 5% significance level.(Critical Chi-Square value for df= 4 at 5% is 9.488)

°
````

## 2024-25 · Re-Exam · Sem 5 · paper cb3cf5b4331e

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/MODELLING & SIMULATION/Mopdelling & Simulation, Sem-V, Batch 2024-25 Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 87.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025

Program: B TECH / MBA TECH Stream: All applicable streams Year: IIT Semester: V
Subject: MODELLING AND SIMULATION Time: 3 hrs Qso0puto 5 oop m)
Date:_25/2/25 . ° No. of Pages: 4

Marks:100

Re Examination(2024- 25)
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi
CO-1; SO- | a. F 3 ‘ —
L: Explain and compare the following models Stochastic & Deterministic models. 5
BL-5
b. | An architect is optimizing the area of a rectangular garden under specific constraints.
CO- 1; The goal is to maximize the area of the garden, where the perimeter of the rectangle is
SO- 1; 40 units. Using the method of Lagrange multipliers, find the dimensions of the | 5
BL-2 rectangle that will maximize the area.
(es Classify the following partial differential equation:
ie al aru au ou
2: (142°) + (5420?) "4 (44°) =0. 5
BL-3 Ge at ot”
ware ea Using the Middle Square Method, generate 5 random numbers starting with a seed 5
BL-5 value of 1234.
Q2
co-1: |* 10
S 0-2. Classify and compare the mathematical models on S & M axes, where S denotes the
‘ system and M denotes the Math axis.
BL-3
CO-2; |b.
SO-6; Discuss predator prey model in detail. 10
BL-6
Q3
CO-2; SO- | a. Describe the concept of neural networks; include details about the role of layers,
1; neurons, and activation functions in the learning process. Additionally, consider a
BL-2 neural network with two hidden layers, where the input layer has 3 neurons, the first

1/4
--- page 2 ---
hidden layer has 4 neurons, the second hidden layer has 5 neurons, and the output layer
has 2 neurons. Calculate the total number of trainable parameters in this network.

rd A ; Construct a mathematical model to analyze the dynamics of an arms race between two 10
BL 6 competing countries. Clearly state the assumptions in your model.
Q4
Given the system of differential equations:
dx/dt = x(1-x)-xy
CO- 2; dy/dt =-y+xy
SO-6; 10
BL-6 Find all the equilibrium points of this system. For each equilibrium point, determine
the stability of the system.
Solve the Poisson equation tax + my = — 81xy, 0 < x < 1,0 <y< 1 given the details in the
following figure (take h, the interval width along both the axis.as 1/3)
» = 100 780
a: SO- _ 0 uP uy 100 . A
BL-3 ; 7
0 i 2 100
0 Og 2 Ox
Q5
CO-2: Solve the boundary value problem w= 1x under the conditions u(0, t)=u(1, A) = 0 and u(x, 0)
SO-6: = sin mx, 0<x<1_ using the Schmidt method (Take h = 0.2 and a = 1/2). Compute u for the 10
BL-6 first 5 time-steps.
A tech support center receives calls from customers seeking assistance with their
devices. Customers arrive at the support center randomly, with the time between
CO-1; SO- arrivals ranging from 2 to 12 minutes, each with equal probability. The service times
1; for handling calls vary from 3 to 8 minutes, with the probabilities indicated in the table | 10
BL-2

below. Simulate the system for 7 customers using the provided random numbers and
calculate the following:

2/4
--- page 3 ---
i. The average waiting time for a customer.

ii. The probability that a customer has to wait in the queue.
iii. The average service time.

iv. The average time between arrivals,
v. The average time a customer spends in the system.

[Service Time (minutes)|Probability _|
B —jo20_]
f “oa5——]
5 “oso
(6 _[o.1s |
i Joos
is jos]

Random numbers for simulation:

e Arrival Time: 325, 842, 659, 110, 907, 251, 474
e Service Time: 41, 12, 54, 28, 65, 37, 80

Simulate the system using these random

numbers and analyze the system’s
performance based on the specified metrics,

Q6
Solve the equation:
Pu Ou
CO-2; $0- dt dx?
1; 10
BL-3 subject to the conditions:
u(x,0)=cos(mx), O<x<1; u(0,t)=u(1,t)=0.
Use the Du Fort-Frankel method to carry out computations for two levels, taking
h=1/4 and k=1/64,
C0-3: SO- Consider the function f(x, y)=3x?+2y*+6xy, which represents the cost in a machine
I: learning model. Starting from an initial guess (xo,yo)=(2,2), apply the gradient descent 10
BI. 4 method with a learning rate of 0.05 to minimize the cost. Perform three iterations and

find the updated values of x and y after each iteration.

3/4
--- page 4 ---
Q7

CO-2; SO-| a. | Discuss SIR model for infectious disease modelling. 10
8
BL-3
CO-3; SO- |b. | Explain the concept of Monte Carlo simulation and its applications’ in estimating | 10
lg volumes. Outline the steps of an algorithm using the Monte Carlo method to estimate
BL-4 the volume of a sphere.

4/4
````

## 2023-24 · Final-Exam · Sem 5 · paper 4df23be233f3

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/MODELLING & SIMULATION/Modelling and Simulation , Final 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05/12/2023
- Text: ocr (3 pages), mean OCR confidence 85.9

````text
SVKM’S NMIMS

Academic Year: 2023-2024

Program: B TECH/ MBA TECH Stream : All applicable streams Year: [I/IV Sethester: V/VII
Subject: Modelling and simulation Time: 3 hrs (2.00 to 5.00 pm)
Date: 05/12/2023. . No. of Pages: 3

Marks: 100

Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

as . . . . . .
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Ql
a. | The summary of results for a multiple linear regression model between sales, unit price
and promotion is as follows, Interpret the results.
SUMMARY OUTPUT
Regression Statistics
Multiple R 0.97012
IR Square 0.941133
Adjusted R Squa 0.926416
Standard Error 515.7254
Observations 11
CO-1; SO- 1; 5
BL-S JANOVA
df SS MS FE Significance F *
Regression 2 34017672.79 17008836 63.94955 1.20086E-05
| iio Residual 8 2127781.758 265972.7
[Fotal 10 36145454,55

Coefficients Standard Error _t Stat P-value _ Lower 95% Upper 95% Lower 95.0% Upper 95.0%

intercept -1642.04 1151.801633   -1.42563 0.191804 -4298.10333 1014.015 -4298.1033 1014.01533
Unit Price 9.909374 0.876228512 11.30912 3.36£-06 7.888787251 11.92996 7.88878725 11.9299604
Promotion 8.133162 2.624163278 3.099335 0.014681 _2.081830676 14.18449 2.08183068 14.1844934

CO- 1; SO- 1; | b. | Discuss Allee effect on populations.

BL-2 >
c. | i. Classify the following partial differential equation:
CO-1; SO-2; 3Uxxt4Uxyt+6Uyy-2Ux+Uy-u=0 5
BL-3 ii, State the one dimensional heat equation; specify meaning of each notation used.
co SOn a. List the steps of the Monte Carlo’s algorithm to find volume of a cube. 5
Q2
CO- 1: $0-2: & Classify the models on the S(system), Q(question) & M(mathematical statement ) ™

BL-3 axes.
--- page 2 ---
CO- 2; SO-6;

Develop a Lotka Volterra model for the interactions between predators and prey.

BL-6 a
Q3 7 oe
Draw the architecture, compute the trainable parameters & state all the mathematical
expressions for a neural network with the following structure:
CO-2; SO-1; Input layer 2 neurons 10
BL-2 First hidden layer : 3 neurons
Second hidden layer 3 neurons
Output layer 2 neurons
CO- 2; SO-6; 10
BL-6 State the assumptions and develop a Mathematical model for infectious disease.
Q4
i. Find the equilibrium points of the logistic model for population growth.
ii. Find the equilibrium points and check the stability of the system defined by
CO- 2; SO-6; cad =2x—- 3y :
dx 10
BL-6 dy
—=4x+
dt
Solve the elliptic equation Uxx + Uyy = 0 for the following square mesh with boundary
values as shown in figure, Using Gauss Seidel Method perform 5 iterations
CO-1; SO-2; woo “i aD von
BL-3 uM
anu ES : z eB yy .
Tho = ~ ~ 060
Q5
Solve the boundary value problem U=U,x under the conditions u(0,t)=u(1,t)=0 and
CO- 2; SO-6; u(x,0)=0 and u(x,0)=sinax , 0<x<1, 0<t<0.02 using Schimdt method. 10
BL-6 (Take h=0.2 and a=1/2)
A small grocery store has only one chekout counter . Customers arrive at this checkout
counter at random from | to 8 minutes apart with the same probability of occurence.
The service times vary from | to 6 minutes apart with the probabilities as shown
below.Simulate the system for 6 customers and find the following,
CO-1: SO-I: i. The average waiting time for a customer
BL2 > ii. The probability that the customer has to wait in the queue 10

iii. The average service time
iv. The average time between arrival
v. The average time a customer spends in the system
--- page 3 ---
Service time | probability | Arrival time — | probability ]
(in minutes) (in minutes) ‘
I 0.10 1 0.425
2 0.20 2 0.125
3 0.30 , 3 0.125
4 0.25 4 0.125
5 0.10 . 5 0.125
L 6 0.05 6 0.125
7 0.125
8 0.125
Random numbers for simulation are as follows:
[ Random digits for arrival ~_ | 913 | 727 | 15 | 948 | 309
Loa Random digits for service time | 84] 10 |74 153/17 | 79
Q6
CO-2; SO- 1; Solve using relaxation method, the Laplace equation Uxx+Uyy=0 inside the square 10
BL-3 bounded by the lines x=0, x=4, y=0, y=4 given that U=x’y? on the boundary.
. : Minimize f(x1,x2)=x1-x2+2x1?+2x)x2+x2? taking the starting point as x={?} using
CO-3; SO- 1; 10
BL-4 steepest gradient descent method.(perform 4 iterations).
CO-2; SO- 1; Solve Us=16U;x with boundary conditions u(0,t)=0, u(5,t)=0, u:(x,0)=0 and 10
BL-3 u(x,0)=x?(5-x), take h=1,k=0.25.Perform for x= 0 to 5, t=0 to 1.25.
eg
CO-3; SO- 1; i. Discuss Monte Carlo Simulation. 10
BL-4

L

ii. Explain the middle square method of random number generation and hence
obtain 10 random numbers using the seed xo=1009.
````

## 2023-24 · Final-Exam · Sem 5 · paper ce2017bb2a6f

- Departments: Common (all branches)
- Programmes: B TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/MODELLING & SIMULATION/Modelling and Simulation, Sem-V, A Y 2023-24, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05/12/2023
- Text: ocr (3 pages), mean OCR confidence 84.7

````text
SVKM’S NMIMS a
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS ENGINEERING
Academic Year: 2023-2024

Program: B TECH/ MBA TECH Stream : All applicable streams Year: I/IV Semester: V/VII
Subject: Modelling and simulation Time: 3 hrs (2.00 to 5.00 pm)
Date: 05/12/2023. . No. of Pages: 3

Marks:100

Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted. ; :
4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page. :

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary. .

Qi
a. | The summary of results for a multiple linear regression model between sales, unit price
and promotion is as follows, Interpret the results.
SUMMARY OUTPUT
Regression Statistics
ultiple R 0.97012
IR Square 0.941133
Adjusted RSque 0.926416
Standard Error 515,7254
Observations 11 .
CO-1; SO- 1; 5
BL-5 ANOVA : re
dj SS Ms FE Significance F
Regression 2 34017672.79 17008836 63.94955 1.20086E-05
Residual . & 2127781.758 265972.7
[Total 40 36145454.55

Coefficients Standord Error t Stat P-volue Lower 95% Upper 95% Lower 95.0% Upper 95.0%

intercept 1642.04 1151.801633 -1.42563 0.191804 -4298.10333 1014.015 -4298.1033 1014.01533
Unit Price 9.909374 0,876228512 11,30912 3.36E-06 7.888787251 11.92996 7.88878725 11.9299604
Promotion 8.133162 2.624163278 3.099335 0.014681 _2.081830676 14.18449 2.08183068 14.1844934

CO- 1; SO-1; | b. | Discuss Allee effect on populations.

BL-2 5
c. | i. Classify the following partial differential equation:

CO-1; SO-2; 3 Unoct 4Uxy+ 6Uyy-2UyHUy-U=0 5

BL-3 ii, State the one dimensional heat equation; specify meaning of each notation used.
aa aie . List the steps of the Monte Carlo’s algorithm to find volume ofa cube. 5

Q2
j . . 1

CO- 1: $0-2: * Classify the models on the S(system), Q(question) & M(mathematical statement )

BL3 axes,
--- page 2 ---
CO- 2; SO-6;

Develop a Lotka Volterra model for the interactions between predators and prey.

BL-6 10
Q3 | 5 ua
Draw the architecture, compute the trainable parameters & state all thé mathematical
expressions for a neural network with the following structure: .
CO-2; SO-1; Input layer 2 neurons 10
BL-2 First hidden layer 3 neurons
Second hidden layer 3 neurons
. Output layer 2 neurons
CO- 2; SO-6; * : 10
BL-6 State the assumptions and develop a Mathematical model for infectious disease.
Q4 ;
i. Find the equilibrium points of the logistic model for population growth.
ii. Find the equilibrium points and check the stability of the system defined by
CO- 2; SO-6; o = 2x —3y
dx 10
BL-6 7d
a= 4x +
dt *
Solve the elliptic equation Uxx + Uyy = 0 for the following square mesh with boundary
values as shown in figure, Using Gauss Seidel Method perform 5 iterations
0 o_o _wo ,
CO-1; SO-2; 100 “ ms wo 1004) 10
BL-3
2000, a) mal a 7 z 2000
tt, my My a
fen * 1060
0 f oO
500 1000 500
Q5
Solve the boundary value problem UU,« under the conditions u(0,t)=u(1,t)=0 and
CO- 2; SO-6; u(x,0)=0 and u(x,0)}=sinnx , 0<x<1, 0<t<0.02 using Schimdt method. 10
BL-6 (Take h=0.2 and a=1/2)
A small grocery store has only one chekout counter . Customers arrive at this checkout
counter at random from 1 to 8 minutes apart with the same probability of occurence.
The service times vary from 1 to 6 minutes apart with the probabilities as shown
below.Simulate the system for 6 customers and find the following,
CO-1: SO-I: ' i, The average waiting time foracustomer ~ :
BL-2 > ii. | The probability that the customer has to wait in the queue 10

iii. The average service time
iv. The average time between arrival
v. The average time a customer spends in the system
--- page 3 ---
Service time | probability Arrival time | probability

ii. Explain the middle square method of random number generation and hence
obtain 10 random numbers using the seed xo=1009.

(in minutes) (in minutes)
1 0.10 1 0.125
2 0.20 2 0.125
3 0.30 3 0.125
4 0.25. 4 0.125
5 0.10 5 0.125
6 0.05 [6 0.125
7 0.125
8 0.125
Random numbers for simulation are as follows:
Random digits for arrival ~_| 913 [727] 15 | 948 | 309
Random digits for service time | 84|10 .| 74 |53}17 | 79
Q6
CO-2; SO- 1; Solve using relaxation method, the Laplace equation Usx+Uyy=0 inside the square 10
BL-3 bounded by the lines x=0, x=4, y=0, y=4 given that U=x’y? on the boundary.
. . Minimize f(x1,x2)=x1-x2+2x12+2x)xotx,? taking the starting point as x={?} using
CO-3; SO- 1; 0 ia
BL-4 steepest gradient descent method.(perform 4 iterations).
Q7
CO-2; SO- 1; Solve Us=16U;x with boundary conditions u(0,t)=0, u(5,t)=0, ur(x,0)=0 and 10
BL-3 u(x,0)=x?(5-x), take h=1,k=0.25.Perform for x= 0 to 5, t=0 to 1.25.
* .
CO-3; SO- 1; i. Discuss Monte Carlo Simulation. 10
BL-4
````

## 2023-24 · Re-Exam · Sem 5 · paper f65dcc748096

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/MODELLING & SIMULATION/Modelling & Simulation , Re-exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 85.0

````text
SVKM’S NMIMS j
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024 ‘

Program: B TECH/ MBA TECH Stream : All applicable streams Year: HI/IV Semester: V/VII
Subject: Modelling and Simulation Time: 3 hrs (2.00’to 5.00 pm)
Date: I2/o2/ ZOQy No. of Pages:3
Marks: 100

_ ReExamination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page. .

6) Figures in brackets on the right hand side indicate full marks.
(>_7) Assume Suitable data if necessary.

Qi
a. | The summary of results for a multiple linear regression model between car price and
max speed, peak power, range is as follows, Interpret the results.
SUMMARY OUTPUT ~ ~
Re Statistics —
ie R 0.93
R Square 0.86
A juare 0.79
‘or 2317.80
CO-1; SO- 1; s 10.06 5
BL-5
ANOVA ,
df $s MS F__ Significance F
Regression 3.00 196666739.35 65555579.78 12.20 0.01
Residual 6.00 32233260.65 5372210.11
Total 9.00 228500000.00 ‘
— Coefficients Standard Error tStot P-value Lower95% Upper 95% Lower 95.0% Upper 95,026
Intercept -50885.73 13250.66 3.84 0.01 -83308,92 -18462.54 ~83308.92 -18462.54
M Speed(mph) 245.43 181.30 1.35 0.22 -198.19 689.05 * -198.19 639.05
Paak Power(hp) 38.19 31.94 1.20 v.28 +39.96 116.34 -39.96 116.34
Range(miles} 94.38 146,94 0.64 0.54 -265.15 453.92 265.15 453.92
CO- 1; SO- 1; | b. . . ; .
BL 2 , Discuss population growth model for single species. 5

CO-1:so-2: | & i. Classify the following partial differential equation:
BL-3 > 3Uxxt4Uxy+6Uyy-2Uxt+uy-u=0 5
° ii, State the one-dimensional wave equation; specify meaning of each notation used.

ial a Summarize the steps of Monte Carlo’s algorithm to find area below the curve. 5

Q2

cot of a. Classify the mathematical models from black box to white box models. 10

10
Oe p80: Develop a predator prey model for interaction between two species.
--- page 2 ---
Q3

Draw the architecture, compute the trainable parameters & state all the mathematical
expressions for_a neural network with the following structure:

a

CO-2; SO-1; Input layer 2 neurons 10
BL-2 First hidden layer 3 neurons
Second hidden layer 3 neurons
Output layer 1 neurons
CO- 2; SO-6; Develop a compartmental model for the infectious disease, also explain the
: 10
BL-6 reproduction number Ro.
Q4
i. Identify the points of equilibrium in the population growth logistic model.
ii. Find the equilibrium points and check the stability of the system defined by
CO- 2; 80-6; 2 pale 0
BL-6 i
Pe +
de“ ">
Solve the elliptic equation Uxx + Uyy = 0 for the following square mesh with boundary
values as shown in Figure , Using Gauss Seidel Method perform 5 iterations,
1000 1800 1000 1000
aa ane 2000 =! = 500 10
2000 = a 0
1000. 500 0 0 ¢
Q5
Solve the boundary value problem U=Usx under the conditions u(5,t)=100, u(0,t)=0
CO- 2; SO-6; and U(x,0)=20 , 0<x<5, t=0 Compute Using Crank Nicholson Method take time step 10
BL-6 h=1.Peform for 2 steps for time.
At a doctors clinic the inter arrival time of patients and service time of the doctor is
randomly distributed as follows
Simulate the clinic for 6 patients and find the following,
i. The average waiting time for a patient
ii. | The probability that the patient has to wait in the queue
iii. | The average service time
CO-1; SO-1; iv. The average time between arrival 10
BL-2 v. The average time a patient spends in the system
--- page 3 ---
Arrival time probability Service time | probability ,

(in minutes) (in minutes)
5 0.50 4 0.50 :
10 0.30 8 0.20:
15 0.20 12 0.30

Random numbers for simulation are as follows:

Random digits for arrival - | 25 | 35 | 58 | 10 | 15
Random digits for service time | 84 | 10 | 74 | 53 | 17 | 79
Q6
C0-2: $0- |: Solve using relaxation method, the Laplace equation UsxtUyy=0 on the boundary
BL-3 ; conditions u(0,y)=0, u(4,y)=8+2y, u(x,0)=x?/2, u(x,4)=x? find u(i,j) =1,2,3,j=1,2,3 10
Os. S0-1: Minimize f(x1,x2)= 2x1?-+2x1x2t+x2? +4x1-2x2+taking the starting point as x=(p}
BL-4 , using Newton’s method. ‘ 10
Q7
CO-2; SO- 1; Solve Ur=Uxx With boundary conditions u(0,t)=uC1 ,t)=0 ur(x,0)=0 and 10
BL-3 u(x,0)=10+x(1-x), take h=0.1,k=0.1° Perform for x= 0 to 1, t=0 to 1
CO-3; SO- |; i. Discuss Monte Carlo Simulation 10
BL-4 ii. Explain Linear Congruential method of random number generation and
hence obtain 5 random numbers using the seed x0=7, multiplier=5,
additive=1 constant and modulus=8.
ff
````

## 2022-23 · Final-Exam · Sem 5 · paper b23de450788d

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/MODELLING & SIMULATION/Modelling & Simulation, 3rd Year, Sem V, Year 2022-23, Final Exam.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 December 2022
- Text: ocr (3 pages), mean OCR confidence 87.7

````text
4

SVKM’s NMIMS iy
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2022-23 Ee

c

Programme: B.Tech / MBA Tech (All Stream) Year: III/IV Semester: V/VII

Subject: Modelling and Simulation
Marks: 100
Date: 02 December 2022 Time: 2.00 pm - 5.00 pm

Durations: 3 (Hrs)

No. of Pages: 03
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.
2) Out of remaining questions, attempt any 4 questions.

. 3) In all 5 questions to be attempted.
- 4) Al! questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi
Answer briefly:
cO-1 a. Compute 5 random numbers using Linear Congruential Method with the
SO-2 ‘ multiplicative constant a=1, the additive constant b=3, the starting point or (5 marks)
BL-3 seed value 0, and the modulus M=10. :
b. i. Classify the following Partial Differential equations (5 marks)
CO-1 ; SU xt3 Uxy-7Uyyt+ U+U=0
a4 ii. Find ‘m’ if the following partial differential equation is parabolic,
- 9Ux+MUxyt+Uyy=0
c. Discuss the population related effect as visible in the following graph: (5 marks)
2
Zz
CO-3 ; 2
SO-5 ; 5°
BL-2 @ K \
2
2
a
proliferation rate vs time -
d. Explain the meaning and significance of following statistical parameters: (5 marks)
1. mean
CO-1; 2. median
SO-2; 3. range
BL-4 4. standard deviation

5. coefficient of variation

>
--- page 2 ---
Q2 a The Partial differential equation, U=U,x for 0<x<5, t=0 such that U(x,0) =20, U

CO-2; (0, t) =0, U (5, t) =100. (10marks)
oy Determine U for the time step , with h=1 Using Crank Nicholson Method.
CO-2; b :
an Explain the Lotka-Volterra Model in detail. (10 marks)
Q3 a
CO-1; Classify the mathematical model on the triplet (S, Q, M) consisting of a system S, (10marks)
SO-2; a question Q, and a set of mathematical statements M.
BL-2
CO-2; b Develop the logistic growth model, state the assumptions , mathematical
SO-1; . (10 marks)
BL-6 equations and explanatory graphs.
a Solve the Laplace equation U,.+Uyy=0 for the following Grid, perform 2
iterations using Gauss
Seidel Method.
0 11.1 17 19.7 18.6
Oty 0 uy Uy uy 219
CO3-; (10 marks)
SO-1;
BL-6 0 uy uy Ue a4
u. le Ng
0 ie
¥ 87 121 125 .
co-1; b Explain Monte Carlo Simulation.Also List the steps of Monte Carlo Algorithm to
SO-2; (10marks)
BL-2 calculate volume.
Q5 a . . . .
Discuss SIR Model for an epidemic. State the assumptions , mathematical
CO-2; (10marks)
SO-2; expressions, graphs and expression for reproduction number.
BL-2 -
CO-2; b Consider a small dedicated cargo airport with unloading facilities for cargo
SO-6; . (10 marks)
BL-6 airplanes. Only one airplane can be unloaded at a time. Airplanes arrive at the

2/3
--- page 3 ---
airport for unloading, the arrival time of the airplanes varies between 20 and 100
minutes, whereas the service time varies between 10 to 80 minutes.
Simulate the activity at the airport for 5 airplanes with the following inter arrival
time, unloading time, and obtain the following:

1. Average waiting time per airplane.

2. Average time at the airport per airplane

3. % for which unloading facilities are idle.

4. Longest queue length.

airplane 1 2 a 4 S
Inter arrival 20 30 45 50 40
time
Unloading 40 55 30 60 50
time
Q6 a _ .
Solve U,x+Uyy=0 inside the square bounded by x=0,x=4,y=0,y=4 given that
CO-1; (10 marks)
SO-1; u=x’y’ on the boundary using relaxation method.
BL-6
CO-3; b
SO-1; Evaluate the extreme values of f(x,y)=2x-5y subject to the constraint x’+y’=144. (10marks)
BL-5
Q7 a
CO-2; Discuss the working of Neural Network models (10marks)
SO-5; .
BL-2
b Explain the working of gradient descent method and hence Evaluate minimum
CO-3; . .
SO-2: value of the function f(x1,x2)= x1’+2x2” using Gradient descent method (perform (10 marks)
BL-6

3 iterations) starting at (3)

X
````

## 2022-23 · Re-Exam · Sem 5 · paper c915a91876bb

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/MODELLING & SIMULATION/Modelling & Simulation, All Streams, 3rd Year, Sem-V, Year 2022-23, Re-Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 February 2023
- Text: ocr (3 pages), mean OCR confidence 84.7

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING

/ Program: B.Tech / MBA Tech (All Stream) Year: III/IV Semester : V/VII

AcademicY ear: 2022-2023

ject: Modelli d Simulation
Subject: Modelling and Simulatio Marks: 100

Date : 08 February 2023 Time: 2.00 pm - 5.00 pm
Durations: 3 (Hrs)

No. of Pages:_O,5
Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
(> 3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly:
a. | Compute 7 random numbers usin, middle square method using x0=3043, Does the
CO- 1; $O-2; P . a ™ (5 marks)
BL-3 generated sequence show cycling?
b. | i. Classify the following Partial Differential equations (5 marks)
CO-1; 80-1; 3U oct 4Uyy-TUyyt 8Ux+ TU=0
BL-2 ii Find ‘m’ if the following partial differential equation is elliptic,
; UsctmUsytUyy=0
ps SO-5; | ¢. | Discuss Allee effect observed in population dynamics. (5 marks)
ir 80-2; | 4. Explain the working of Neural Network models fanatics)
Q a | Solve the boundary value problem U,=U,x such that U(0,t) =0, U (1, t) =0, U (x,0)
Bs a: (10marks)
ce SO-2; =sin(x), 0<x<i using Schimdt Method.(Assume h=0.2 and a=0.5) .
CO-2; SO-5; b . 10 k
j BL-4 Explain the Predator -Prey Model in detail. (10 marks)
Q3 a
‘ CO-1; SO-2; Classify the mathematical models between Black box and White box models. (10marks)
BL-2
CO-2: SO-1; | 6 | Develop the Single species growth model, state the assumptions , mathematical (10 ks)
; > . marks
BL-6 equations and explanatory graphs.
Qh a o mark
CO3-; SO-1; (10 marks)
- BL-6
--- page 2 ---
Solve the Laplace equation U,,+Uyy=0 for the following Grid, perform 5 iterations

using Gauss Seidel Method.

oO 500 1000 BOD 0
c
a u, uy a,
L000 - 1000
2000 [4 = = i B I sc00
7
u, u, ty
1000 : : : 1000 :
D
° 500 1000 500 ®
CO-1; SO-2; | 6 | Discuss Monte Carlo Simulation. Also List the steps of Monte Carlo Algorithm to (lomarks)
marks
BL-2 calculate area.
Qs a | Develop the compartmental SIR Model for an infectious disease. Clearly State the
CO-2: SO-2: assumptions , mathematical expressions, graphs and also the expression for ‘| (10 marks)
BL-2 reproduction number.
b | Consider a harbor with unloading facilities for cargo ships. Only one ship can be (10 marks)
unloaded at a time. Ships arrive at the airport for unloading, the arrival time of the
ships varies between 10 and 100 minutes, whereas the service time varies between ~|
20 to 80 minutes.
Simulate the activity at the airport for 5 ships with the following inter arrival time,
unloading time,
and obtain the following:
CO-2; SO-6; io A
BL-6 1. Average waiting time per ship.

2. Average time at the airport per ship
3. % for which unloading facilities are idle.

4. Longest queue length. -

ae
--- page 3 ---
ship 1 2 3 4 5

Inter arrival 30 20 50 40 40
time
Unloading 30 50 40 70 ao
time
a
Solve Uxx+Uyy=0, for the following square using Relaxation method.
1000 1000 1000
1000 5
- 1 1 u 3
Q6 2000 500
CO-1; SO-1; (10 marks)
BL-6
u u
3 4
2000 0
1000 0
500 0
oe BO-]) | 2 | pesmate the egrede-~valuator f(x,y)=x’+y" subject to the constraint x?+2y"=1. (10 marks)
a
Q7
Review the Linear regression model, also state any 2 statistical parameters to (10 marks)
ple SO-5; analyze the performance of Linear Regression Model.
b_ | Explain the working of gradient descent method and hence evaluate minimum value
CO-3; SO-2; of the function f(x1,x2)= x1?+2x2? -2x1x2+2x, using Gradient descent method (10 marks)
BL-6

(perform 3 iterations) starting at (ol

2/3
````

## 2021-22 · Final-Exam · Sem 8 · paper a04235c5e2f6

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/COMMON FOR ALL BRANCH VIII/SEM VIII/Modelling and Simulation/Modelling & Simulation,Sem8,Final,2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 22 April 2022
- Text: ocr (2 pages), mean OCR confidence 82.7

````text
SVKM’s NMIMS
en PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

4 SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2021-22

; all
Programme: B.Tech/MBA Tech (All Stream) Year: IV Semester: VII
Subject: Modelling and Simulation _.
Marks: 100
Date: 22 April 2022 Time: 2.00 pm to 5.00 pm

Durations: 3 (hrs)
No. of Pages: _2
7 _ Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
a. | The summary of results for a linear regression model between heart disease
and biking, smoking is as follows, Interpret the results.
VW:
TaCRormaT’ = heart.disease ~ biking + smoking, data = heart.data)
Residuals: ;
Min 1q Hedian 3Q Max
CO-1; -2.1789 -0.4463 0.0362 0.4422 1.9331
SO- 1; Coat eens inate std. Error t value pr(>|tl) 4
BL-5 (intercept) 14.984658 0.080137 186.99 <2e-16 ***
biking ~~ -0. 200133 0.001366 -146.53   <2e-16 ***
smoking 0.178334 0.003539 50.39 <2e-16 ***
signif. codes: 0 '***' 0,001 ‘**? 0.01 ‘*' 0.05 '.' O.1 6 ' 1
Residual standard error: 0.654 on 495 degrees of freedom
Multiple R-squared: 0.9796, Adjusted R-squared: 0.9795
F-statistic: 1.19e+04 on 2 and 495 DF, p-value: < 2.2e-16
CO- 1; b. ;
SO- 1; Write a note on setting up ODE models. 4
BL-2
CO-1; © | Classi . 2-7 45 ; .
assify the following partial differential equation:
7 +4uUxyt4uyy - Uxt2uy=0 ‘
BL-3 Uno Uy Tt Uyy~ Ux Uy
CO-1; d. :
SO-1; Summarize the steps of Monte Carlo’s area algorithm. 4
BL-5
CO-3; e. ; . _ :
Find the maximum value of f(x,y)=2x-Sy, subject to the
SO-2; i ae . ; Be : 4
BL-2 constraint x?+-y?=144 using Lagrange’s multiplier method.
Q2
CO- 1; a . a .
Classify the models on the Q(question) axis.
SO-2; 10
BL-3
CO- 2; b. c ‘ og gi 8
50-6: Develop a model for population growth with limited resources. 10
“Us
BL-6

i}o-
--- page 2 ---
Q3

CO-2;

SO-1; Explain feed forward Neural networks. 10
BL-2
CO- 2;
SO-6; Develop a model for the interactions between predators and their prey. 10
BL-6 :
Q4
CO- 2;
SO-6; Develop a model for HIV-1 virus. 10
BL-6
0 500 1000 500 0
c
1000 “ “s Ke 1000
A uy us Us B .
CO-1: 2000 2000
SO-2; 10
BL-3 us ul u,
1000 : = 1000
| D
8 500 1000 500 q
Solve the elliptic equation with boundary values as given in the figure
using Gauss Seidal method.
Q5
Determine the displacement y(x,t) of a string for x=0(2)10 and upto one half
2 2.
CO- 2; period of vibration .If y(x,t) satisfies the equation 2 =4 a2 and
pot boundary condition y(0,t)}=0 , y(10,t)}=0 .y=0 and y(x,0)=x(10-x)/100 using 10
BLA numerical technique to solve the one dimensional wave equation.
CO-1; : . .
: Explain the Linear congruence method of random number generation and
SO-1; A we _ 10
BL-2 hence obtain 10 random numbers using a=5, b=1, and c=8.
Q6
CO-2;
SO- 1; Develop the Model for one dimensional heat flow equation. 10
BL-3
CO-3: Minimize £(X1,X2)=X1-X2t2K12+2x1x2t x2? taking the starting point as
SO- 1; xi={P} using Newton’s method for optimization. 10
BL-4 a

2/2
````

## 2019-20 · Final + Re-Exam · paper 22f847dd0adf

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION FINAL EXAM 19-20 RE EXAM 17-18 18-19.pdf`
- Printed on paper: max marks: 70; exam date: 09 November 2019
- Text: ocr (2 pages), mean OCR confidence 91.5

````text
od

SVKM’s NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (Mechatronics) Year: III

Academic Year: 2019-20
Subject: Modelling and Simulation

MPSTME ~

Marks: 70 !
. BRARY ®
Date: 09 November 2019 Time: 10.00 We 1.6 pm LS
Durations: 3 (RXS)> 5S
No. of Pages: AUIS UNVERSSS

Final Examination (2019-20)/ Re-Examination (2017-18/ 2018-19

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.

(QA Attempt any four

a. Explain steps in hypothesis testing. (4)

b. Differentiate between Flow shop scheduling and Job shop scheduling. (3)

c. Describe SIMAN software features suitable for simulation and modeling. (4)

d. Define i. Validation ii. Verification iii. Accreditation. . (3)
Q.2a. | Explain in detail i. Advantages of Simulation ii. Disadvantages of Simulation. (7)
b. | Enumerate and explain various techniques for verification of simulation models. (7)
Q.3 a. Explain Batch Means Method. (7)
b. | With the help of a suitable flowchart explain the steps in modelling and simulation. (7)

'Q.4 qa. | Explain statistical methods for comparing Real-World observations with simulation output | (7)

data.

b. | A component of a system whose time to failure is exponentially distributed with failure rate 4 | (7)
=1/6. If 6 such components are installed in different systems, what is the probability that at
least 2 are still working at the end of 9 years?

Q5 a. | Derive the expressions of length of the system and queue,L, and L, in terms of arrival rate 4 | (7)
and service rate u for a single server infinite capacity queue system

(1/2)
--- page 2 ---
hoe

= om

b. | Enumerate various methods of generating random variates. Explain any two methods in detail. | (7) |

Q6 a. | Define EOQ. A company makes bicycles. It produces 450 bicycles a month. It buys the tires | (7)
for bicycles from a supplier at a cost of $20 per tire. The company’s inventory carrying cost

is estimated to be 15% of cost and the ordering-is $50 per order. |

|

i. Calculate EOQ. |

ii. What is the number of orders per year? '

iii. Compute the average annual ordering cost. :
iv.Compute the average inventory. |

v.What is the average annual carrying cost? |

vi. Compute the total cost. 1

b. | Explain estimation, estimator and all of its properties with suitable diagrams. (7) |

Q7 a. | Describe Quantile-Quantile plots and its use. (3.5) |
b. | Compare Simulation languages with Simulators: (3.5) |

|

c. | Describe the main issues addressed by output analysis. (3.5) |

d. | “Bad Data Equals Bad Models”. Do you Agree? Justify. (3.5) |

(2/2)
````

## 2018-19 · Final + Re-Exam · paper c5aede8da9a9

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION FINAL EXAM 18-19 RE EXAM 17-18.pdf`
- Printed on paper: duration hours: 3; exam date: 17 November 2018
- Text: ocr (2 pages), mean OCR confidence 90.0

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & EN

Programme: B. Tech (MECHATRONICS) - Year: III ‘

Academic Year: 2018-2019

/ Subject: Modelling and Simulation « ,

Date: 17 November 2018° Time: 10.00 am to
‘ Durations: 3 (hrs)

No. of Pages:

. Ce #
Final Examination (2018-19) / Re-examination (2017-18)

Instructions: Candidates should read carefully the instructions printed on the question paper and
on the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is.compulsory.
2) Out of remaining questions, attempt any | questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume -suitable data if necessary.
&

Ql. a. What are the advantages and disadvantages of simulation modelling? [4]
b. What are the steps involved in input modelling? [3]
c. What is output analysis and why we need it? [4]
d. When can we model the data with Poisson random variable and Gaussian [3]
random variable?
Q2. Explain the following

a. Parameter estimation, desirable qualities of an estimator and different ways [5]

-t) to estimate a parameter.
see b. With the help of a neat diagram, explain different ways to study a system. [5]
c. Define System, Attribute, Activity and State of a system. [4]
Q3. Discuss the following

fo
--- page 2 ---
a. Joint probability distribution and its application in modelling. [2]

b. Estimation of parameters for different distributions. [4]
c. Histogram and quantile plots. [4]
d. Terminating and non-terminating simulation models. [4]

Q4. a. Discuss in detail about various types of distributions and how to select an [7]

appropriate distribution for input modelling?

‘b. How to verify a simulation model, discuss in detail? [7]
QS. a. Discuss in detail about different techniques for generating a random [8]
variable.

b. Explain the working of a Linear congruential generator with the help of an —[6]
example >.
Q6. Discuss the following applications of modelling and simulation with an

example of each

a. Job shop system [7]
b. Inventory system : [7]
Q7 a. What are the steps involved in model building? ‘ [4]

b. Discuss different types of time advance mechanisms used in simulating a [4]
discrete event simulation model.

c. What is M/M/1 queuing system and how to model it? [6]

2fo.
````

## 2018-19 · Re-Exam · paper a50a64fdad49

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION BATCH 2017-18 18-19 RE EXAM.pdf`
- Printed on paper: exam date: 15 January 2019
- Text: ocr (2 pages), mean OCR confidence 91.0

````text
: SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Program: B. Tech (Mechatronics) < Year: III Semester: V7
Academic Year: 2018-2019 — ‘
| Subject: Modelling and Simulation © Marly
Ti

Date: 15 January 2019 ©

Re-examination (2017-18/ 2018-19)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new, question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Symbols and abbreviations imply their intended meaning.

8) Assume Suitable data if necessary.

1. Attempt for 14 marks Answer any 2 out of (a,b,c) and any 2 out of (d,e,f).
a. What is a model? Differentiate between static and dynamic models. [4]
b. What is an M/M/1 queue? Explain with an appropriate illustration. [4]
c. Explain new paper-boy problem. [4]
d. Define Simulation. How simulation is helpful in design process? 13]
e. Describe the steps involved in hypothesis testing. i3]
if Define type 1, and type 2 errors, of hypothesis testing. [3]
2 :
a. Classify the different model types. Explain building of a simulation model, from concept to
adaptation, using a flow chart of activities. (7)
b.. What do you mean by validation and verification (V&V) of a model? Describe various means to
attain V&V for a model. “A valid model may not be a credible one.” justify. (7)
i
a. What is interval estimation? Describe interval estimation using sampling distribution. (5)
b.

The system shown in the figure-1 is hanging wheei of a
stationary truck. Analyze its motion under various forces,
and suggest an electrical equivalent circuit, for modelling
of the same.

seat t= time

| x = vertical displacement

M = mass of the wheel

K = stiffness of the spring

D = damping coefficient of the shock absorber

Figure 1

(9)

1of2
--- page 2 ---
a.

Explain acceptance-rejection met
Let ‘X’, have an exponential distribution, with

(7)

hod of generation of random variates.
“B’ as mean, distribution is defined as:

fx) = exp(-x/P) for x>0

Derive the inverse transform

Compare simulation languages with general purpose languages.
Write flow chart for algorithm for simulation of automated packaging of a boo

blocks. The task of packing one book consumes 90 seconds followed b

consuming 30 + 10 seconds.

constructed, and write code of GPSS code for the same.

Explain Welch algorithm of out
period, and how is it handled in simulation studies?

b. Explain flow shop scheduling.

Discuss in brief:

a.
b.
c.
d.

Strange law of large numbers

Credibility of modeling
GPSS
Computer models

=0 otherwise
for “X’ to generate random population following fc(x) (7)

(7)
k, using standard GPSS
y inspection of packaging, ‘
The rejection of packaging is seen as 6%. Explain the flow chart so

(7)

put data analysis, with appropriate illustrations. What is warm-up

7)

oD)

(3)
(4)
G)
(4)

2 of 2
````

## 2017-18 · Re-Exam · paper 3ba69654e19b

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION BATCH 17-18 RE EXAM 2017-18.pdf`
- Printed on paper: max marks: 70; duration hours: 3; exam date: 30 May 2018
- Text: ocr (2 pages), mean OCR confidence 92.5

````text
aa?

SVKM’s NMIMS .
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (Mechatronics) “ Year: Il . Semester: V |

Batch: 2017-18 ~
Academic Year: 2017-2018

“ bject: Modelling and Simulation «
supses ° Marks: 70

Time: 10.00 amto1.00pm+ /
Durations: 3 (hrs) 4 a
No. of Pages: _©-2— ©
Re-Examination ” H

Date: 30 May 2018 ¢

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.

1) Question No. | is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Attempt any four (Each sub-question carries 3.5 marks) (14)
1. Describe the situations when simulation is not appropriate.

2. Differentiate between Type-1 and Type-2 errors with appropriate examples.

3. Explain timing & relationship diagram for validation, verification & credibility.

4. Compare simulation languages with general purpose languages.

5. Differentiate between terminating and non terminating simulation.

6. With the help of an example, explain balking in queueing system.

Q.2 1. With the help of a suitable flowchart explain the steps in modelling and simulation. (7)
2. What are the techniques for developing valid and credible models ? (7)

Q.3 1. Explain strong law of large numbers. We observed 28 successes in 70 independent (7)

Bernoulli trials. Compute a 90% confidence interval for the population proportion p.
gst 2. Explain Statistical Methods for Comparing Real-World Observation with Simulation
Output Data. (7)
ifee
--- page 2 ---
eon

=o

Q4 1. Enumerate various methods for generation of random variates. (7)

- Explain any two methods in detail.

2. Define EOQ. A company makes bicycles. It produces 450 bicycles a month. (7)
It buys the tires for bicycles from a supplier at a cost of $20 per tire. The company’s
inventory carrying cost is estimated to be 15% of cost and the ordering is $50 per order.
Calculate EOQ. What is the number of orders per year. Compute the average
annual ordering cost.

Q5 1. Axis Bank is considering opening a drive in window for customer service. (7)
Management estimates that customers will arrive at the rate of 15 per hour.
The teller whom it is considering to staff the window can service customers at
the rate of one every three minutes.
Assuming Poisson arrivals and exponential service find
1. Average number in the waiting line.
2. Average number in the system.
3. Average waiting time in line.
4. Average waiting time in the system.

2. Explain Batch Means Method. (7)
Q61 The time till failure of a part, T years, has probability density function (7)
f(t) =kt~* (t>1)
and is zero’elsewhere, where k is a constant.
1. Find the value of k

2. Find the mean time till failure
3. Find the failure rate

2. Explain flow shop scheduling. (7)
Q7 1 What are the advantages of simulation ? (7)
2. State and describe different types of simulation with regard to output data analysis. (7)
````

## 2016-17 · Final-Exam · paper 892fa518643b

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION B TECH (MECHATRONICS), 2016-17 FINAL EXAM.pdf`
- Printed on paper: exam date: 29 November 2016
- Text: ocr (1 page), mean OCR confidence 83.2

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (MECHATRONICS) Year: III Semester: V

Academic Year: 2016-2017 .-- Chea age 5 done y

ao ste? Ae “ane
Subject : Modelling and Simulation ’ eel & 2 (> }
“Marks: &o a Bi y <a - 2, ay:
Date : 29 November 2016 Tima 432,09 pra t 90 pm es
aa 3 (

Final-Examination. rs oasis iit le 4 Pa \\
’ SS —Tckee BY “ps \
Instructions: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which is provided for their use.
1) Question No.1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary
1) ANSWER ANY 4. [4X3=12]
a) Differentiate between hypothesis testing errors type-I, and type-ll .
b) Describe different confidence interval estimation methods.
c) Describe GPSS software features.
d) Describe physical modelling, and its applications.
e) “All models are wrong, but some models are useful.” Do you agree? Justify.

2)

a) Classify simulation models based on their objectives. Describe the process of model
verification and validation. (6]

b) A production manager at a tire manufacturing plant has inspected the number of defective
tires in twenty sandom samples with twenty observations each. Following are the number
of defective tires found in each sample: _- fel

Sample | 1/}2}3]4/5/6)7)8/9/]10/11/12]13]14145
Defectives|}3}2/1)2/1)/3/3/2/1]}/2/]3]2]/2t1T 174
Setermin day
" whe ther & lew 9)
Ne€ key mine” The pe cess \s An enh | Os nor ¢
3) val td alan

a) Explain the terms Verification, verification, and credibility in context of simulation and
modelling. Describe process of building valid credible models. [6]

b) What do you mean by “modeling the inputs”? How modeling of inputs impact process of
validation? (6)

4/0.
````

## 2016-17 · Re-Exam · paper 71ea59ddf2e0

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION (MECHATRONICS), BATCH 16-17 RE EXAM.pdf`
- Printed on paper: max marks: 60; exam date: 27 November 2017
- Text: ocr (1 page), mean OCR confidence 87.3

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (MECHATRONICS) Year: III Semester: V

Batch: 2016-17 e #
- Academic Year: 2017-2018

/ Subject: Modelling and Simulation er cnet’
/ L Marks: 60 ai an)
. OF a <«
Date: 27 November 2017 Time: 2.00 pm? to 5,00.pm»i A
Durations: 3 {hrs}. 3; 2 A AW a
2.
No. of Pages: #2! KJ
i \ ~ pF
Re-Examination YY! Menage "A
=
Instruction: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which is provided for their use.
NB:
1) Question No.1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all, S questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume guitable data if necessary.
Q.1 Attempt any three. 12
1. What are the types of simulation in output data analysis? Explain.
2. Explain steps in Hypothesis testing.
3. What is simulation? When it is used?
4. What is system? Explain its components with example.
Q.2 1. A production manager at a tire manufacturing plant has inspected the number of 6
defective tires in twenty random samples with twenty observations each. Following are
the number of defective tires found in each sample: Fotimpate C-1 & 3-p.
Sample   [|1/2/3/4|5/6|7/]8{9j| 10; 11] 12] 13] 14/15] 16/17/18] 19 | 20
Defectives | 3|/2]/1/2/1/3/3;2/1/2 |3 |2 |2 |1 {1 |2 |4 |3 [1 [1
2. Estimate Confidence Interval & draw normal distribution curve for viscosity 6
distribution of oil measured for water using digital viscometer for following data:
B# (poise) | 1.45 | 1.36 | 1.35 | 1.37 | 1.42 | 1.39 | 1.40 | 1.41 | 1.38] 1.44
f 4 7 6 2 12 10 9 6 7 10
Q.3 1. ABC Corporation has got’a demand for particular part at 10000 units/yr. The 6
cost/unit is Rs. 2 & it costs Rs. 36 to place an order & to process the delivery. The
inventory carrying cost is estimated at 9% of average inventory investment. Determine
EOQ, Optimum no. of orders to be placed/annum & minimum total cost of
inventory /annum.
2. State Simulation advantages & disadvantages 6
— Q.4 1. Explain steps in simulation & model building in detail. 6
2. State the applications of discrete event simulation. 6
ges Q.5 1. Explain monte-carlo simulation approach. 6
4 2. Explain general approach for generating random variables. 6
Q.6 1. Confidence Interval in brief, also explain CI for 68%, 95% & 99%. 6
2. Explain generating discrete random variables. 6
Q.7 1. Explain the types of errors in hypothesis testing. 6
2, Explain control charts for variables. 6

/;
````

## 2016-17 · Re-Exam · paper 14e3cd30e25b

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION BATCH 16-17 RE EXAM.pdf`
- Printed on paper: max marks: 60; duration hours: 3; exam date: 29 May 2017
- Text: ocr (2 pages), mean OCR confidence 90.0

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (MECHATRONICS) : Year: III Semester: V
Batch: 2016-17 (at
. : tore oF
Academic Year: 2016-2017 yet :
ye .
Subject: Modelling and Simulation ef pst ,
F ren a: |
? Marks: 60 eh LIBRARBR® ¥
Date: 29 May 2017 Time: 10.00 am ‘togh0 pm re
Durations: 3 (hrs) hea

No. of Pages: _ Zn 88 Oo
Re-Examination '

Instruction: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

NB:

1) Question No.1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all, 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary. :

Q.1 Attempt any three. 12
1. Explain timing & relationship diagram for validation, verification & credibility.
2. Define validation, verification, credibility & accreditation.
3. Explain classification of simulation model.
4. Explain types of Hypothesis testing.
Q.2 1. Determine the mean defect, S.D & variance of density distribution measured for 6
water for following data:
p (kg/m) | 992.5 | 1000.5 | 995.6 | 997.2 | 999.1 | 1000 993.48 | 997.67
f 3 2 1 4 3 5 6 1

2. The number of weekly customer complaints are monitored at a large hotel using a c- 6
chart. Complaints have been recorded over the past twenty weeks. Develop three-
sigma control limits using the following data:

Week T)2131415161/718]9]|10| 11 [12/13 [14] 15 | 16 | 17 | 18} 19 | 20
Complaints |3 [2/3 [1/3 /3]/2/1/3]1 3 4 2 1 1 1 3 2 2 3

Q.3 1. State advantages & toolkits of discrete event simulation method. 6
2. Determine optimal sequence for 8-job, 3-machine using Palmer’s Heuristic algorithm. 6

Also determine elapsed time & idle time for M2 & M3.

Jobi| 1|2|3|4/5|6|7/8
t:2 |si2{iif7]é¢[3 [715
Gis tz 2 6 2 5 6 7 2 1

ts |314{i6[2[1[5 [41/7

Q.4 1. A manufacture has to supply his customers 3600 units of his product/year. Inventory 6
carrying cost/run is Rs. 80. Find EOQ, Optimal number of orders/annum, minimum

annual inventory cost & optimum period of supply.

Ya
--- page 2 ---
2. Explain simulation tools in detail.

Q.5 1. Explain job shop analysis.

2. RV X taking values 0, 1, 2, 3, 4 w.r.t probability 0.25, 0.35, 0.45, 0.5. Find its
distribution also draw distribution function.

Q.6 1. ExplainControl Charts for attributes.
2. Explain flow shop scheduling.

Q.7 1. Explain random variable, pdf, cdf & poisson’s law.
2. A continuous RV X f(x) = Hx3; 0 < x 2 1. Find H, probability between 0.1 & 0.6 and
c.d.f.
````

## 2015-16 · Final-Exam · paper aae834db6a6b

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION B TECH (MECHATRONICS), YEAR 15-16 FINAL EXAM.pdf`
- Printed on paper: exam date: 30/11/2015
- Text: ocr (2 pages), mean OCR confidence 90.7

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (Mechatronics) Year: III Semester: V

Academic Year: 2015-2016 2 eg htNE 8 Bap,
ON

| Subject: Modelling and Simulation

Date: 30/11/2015

Final-Examination

Instruction: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which is provided for their use.

NB:
1) Question No.1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all, S questions to be attempted.
4) All questions carry equal marks.
_ 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary

Q.1 “Attempt any three. 12

1. What is system? Explain its components with example.
2. What are the types of simulation in output data analysis? Explain.
3. Explain generating discrete random variables.

4. State the applications of discrete event simulation.

Q.2 |} 1. Determine the mean defect, S.D & variance of density distribution measured for 6
water for following data:
p (kg/m) | 992.5 | 1000.5 | 995.6 | 997.2 | 999.1 | 1000 | 993.48 | 997.67
4 f 3 2 1 4 3 5 6 1

2. Istimate Confidence Interval & draw normal distribution curve for viscosity 6
distribution of oil measured using digital viscometer for following data:

H (poise) | 1.45 | 1.36 | 1.35 | 1.37 | 1.42 | 1.39] 1.40 | 1.41 | 1.38] 1.44

f 4 7 6 2 12 10 9 6 7 10
Q.3 | 1. What is estimation, estimator & its properties? Also state types of estimation in brief? | 6
" | 2 Explain Confidence Interval in brief. Also explain CI for 68%, 95% & 99%. 6
Q.4 1. Explain steps in simulation & model building in detail. 6
P 2. Explain validation, verification, credibility & accreditation in brief. 6

b-
--- page 2 ---
Q.5 |1. Explain Batch means method. 6
2. Explain general approach for generating random variables. 6

Q.6 | 1. Ifrandom variable has uniform distribution such that X ~ U (-1, 1), Y = X?. Find f(y). 6
2. What is simulation? When it is used? State its advantages & disadvantages. 6

Q.7| 1. State advantages & toolkits of discrete event simulation method. 6
2. Explain the techniques for increasing model validity & credibility. 6

he
````

## Year not stated · Exam not stated · Sem 8 · paper 9579b7fc9d6e

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/COMMON FOR ALL BRANCH VIII/SEM VIII/Modelling and Simulation/Modelling & Simulation.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05/Suly/2023
- Text: ocr (3 pages), mean OCR confidence 86.7

````text
MPSTME
LIBRARY

SVKM'S. NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS ENGIN GINE.
Academic Year: 2022-2023

Program: Btech /MBA tech Stream ;All streams Year: IV Semester: VII

Subject: Modelling & Simulation Time: 3 hrs (10:00. am to 1.00 pm)
Date: 05/Suly/2023 No. of Pages:0

Marks: 100

Re-| Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly:
CO-1 ; a State the don’ts of mathematical modelling.
SO-2 ; (5 marks)
BL-4
CO-3 ; b . (5 marks)
SO-5 ; Discuss Allee effect in short.
BL-2
CO-1 ; c . . (5 marks)
SO- 1; Explain Classification of Partial Differential equations.
BL-2
a d Compute 5 random numbers using Linear Congruential Method. Given the
“al SO-2 ; multiplicative constant a=5, the additive constant b=1, consider the starting point (5 marks)
BL-3 . or seed value as 2, and the modulus M=8.
a Solve the Laplace equation using Gauss Seidel method (Perform 4 iterations)
given that:
0 1d Ww 19.7 8.6
° ty uy uy a1
Q2
CO-2; 0 e ts ve 2 (10marks)
SO-2;
BL3 7 in is
0 7
0 9

8.7 12.1 125

\A
--- page 2 ---
b

Identify & Explain the model represented by the graph of population for the given
years.

Hare
mama Lynx
CO-2; a
SO-5; 120 (10 marks)
BL-4 ~ 100
thousands 8
60
40
20
1845 1855 1865 1875 1885 1895 1905 1915 1925 1935
Q3 a
CO-1; Classify and compare the mathematical models on S & Q axes, where S denotes (10marks)
SO-2; the system and Q denotes the question axis.
BL-2
CO-2; b Develop the logistic growth model, state the assumptions , mathematical -
SO-1; (10 marks)
BL-6 equations along with the explanatory graphs.
Q4 a
. Solve the Poisson equation Uxx+ Uyy=— 81xy, 0<x<1,0<y<1 given
ried that u(0, y) = 0, u(x, 0) = 0, u(1, y) = 100, u(x, 1) = 100 andh = 1/3. (10 marks)
BL-6
CO-1; b Explain Monte Carlo Simulation. List the steps of Monte Carlo Algorithm to
SO-2; (10marks)
BL-2 calculate area under the curve.
Q5 a . . .
Discuss SIR (compartmental) Model. State the assumptions , mathematical
CO-2; (10marks)
SO-2; expressions, graphs and expression for reproduction number.
BL-2
b A small grocery store has only one checkout counter. Customers arrive at the
checkout counter at random times from 1 to 8 minutes apart. The probability of
~ occurrence is as given in the table below. The service time vary from 1 to 6 minutes
with the probabilities given in the table below. Simulate the system for
10 customers & hence find average waiting time & probability of idle server
Arrival Time | Probability Service Time Probability
CO-2; (in Minutes) (in Minutes)
SO-6; (10 marks)
BL-6 1 0.125 1 0.10
2 0.125 2 0.20
3 0.125 3 0.30
4 0.125 4 0.25
5 0.125 5 0.15
6 0.125
I 0.125
8 0.125

2/2
--- page 3 ---
Random numbers for Time between arrival:
Customer 1 2 3 4 5 6 7 8 9 10
Random no.|- | 064 | 112 | 678 | 289 | 871 | 583 | 139 | 423 | 039

Random numbers for Service time:
Customer [1 ]2 [3 [4 [5 |6 {7 {8 |9 | 10 |
Random no. | 84 | 18 | 87 | 81 | 06 | 91 | 79 | 09 | 64 | 38 |

a Solve by relaxation method, the equation Vu = 0 inside the square bounded by
the lines x = 0, x = 4, y = 0, y =4, given that u=x’y’ on the boundary.
. 16 64 144 256
a
6 rn A B c 142
CO-1; (10 marks)
SO-1; D E FE
BL-6 ° “
0 & H i 16
0 0 0 0 0 xX
CO-3; b
SO-1; Evaluate the extreme values of f(x,y)=xy subject to the constraint 4x’+y’=8. (10marks)
BL-5S
Q7 a
CO-2; Discuss the architecture of Neural Network models. (10marks)
SO-5;
|-RL-2
vo-3; b Explain the working of gradient descent method and hence Evaluate minimum
SO-2; 3 (10 marks)
BL-6 value of the function f(x,y)= x°+2y? (perform 3 iterations) starting at [ “il!

3A
````

## Year not stated · Exam not stated · Sem 8 · paper 415fa8f618c5

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/COMMON FOR ALL BRANCH VIII/SEM VIII/Modelling and Simulation/Modelling & Simulation_415fa8f618.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jos 2023
- Text: ocr (3 pages), mean OCR confidence 87.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&
Academic Year: 2022-2023

Program:Btech /MBA tech Stream ;All streams Year: IV Semester: VIII

Subject: Modelling & Simulation Time: 3 hrs ( 40:00 am ty 1:00 pm)
Date: 04 Jos 2023 No. of Pages: 3 _

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
-~ 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql

Answer briefly:

a Ni SO-2; | a. | Explain the significance of p value and R?. (5 marks)
b. | i. Classify the following Partial Differential equation (5 marks)
CO-1; 80-1; Meat] OU y-TU yt 8Ux+7Uy=0
BL-2 ii Find ‘m’ if the following partial differential equation is parabolic,
UxxtmUsy+Uyy=0
ae 380-5; | c. | Write a short note on Lotka-Volterra Model. (5 marks)
CO-1;SO-2; | d. | Explain any one technique of random number generation? Also state the desirable (5 marks)
| BL-4 properties of random numbers.
a | Solve the elliptic equation Uxx + Uyy = 0, perform S iterations using Gauss Seidel
method. Given that
60 60 60 60
Q
CO-2; SO-2; 40 50 (10marks)
BL-3
20 40
9 7) 20 30
CO-2; SO-5; b
BL-4 Explain the modelling of HIV-1. (10 marks)
2 ‘ 10mark
C01: 0.2 Classify the mathematical models as Black box and White box models. (10marks)
--- page 2 ---
BL-2

CO-2: SO-1: Develop the Single species growth model, state the assumptions , mathematical
BL-6 equations and explanatory graphs. Omang)
Solve the Poisson’s equation V7u =8x’y" for the square mesh given in the figure with
u(x, y) = 0 on the boundary and mesh length = 1.
0 0 0 0
Q4
C03-; SO-1; 0 u, uy 0 (10 marks)
BL-6
0 u, a 1°
0 0 0 0
CO-1; SO-2; Discuss Monte Carlo Simulation. Also List the steps of Monte Carlo Algorithm to "
BL-2 calculate volume. silane
Identify and explain the model represented by the following graph, where Si)
represents the susceptible population at time t, I(t) represents infected population and
R(t) represents recovered population.
R(t)
Q5
CO-2; 80-2; st) (00 ana)
BL-2
He)
>
A garment store has only one checkout counter. Customers arrive at the checkout | (10 marks) 1+
counter at random times from 1 to 5 minutes apart. The probability of occurrence is
as given in the table below. The service time vary from 1 to 6 minutes with the
probabilities given in the table below. Simulate the system for 10 customers and hence
find average waiting time and probability of idle server.
Arrival Time | Probability Service Time | Probability
CO-2; SO-6; (in Minutes) (in Minutes)
BL-6
1 0.300 1 0.20
2 0.125 2 0.10
3 0.125 3 0.30
4 0.325 4 0.15
5 0.125 5 0.20
6 0.05

2/3
--- page 3 ---
Random numbers for Time between arrival:

Customer 1 2 3 4 5 6 7 8 9 10

Random no. | - | 264 | 152 | 678 | 289 | 871 | 583 | 139 | 423 | 039

Random numbers for Service time:

Customer 1 2 3 4 5 6 7 8 9 10

Random no. 84 | 18 | 87 | 81 | 06 | 91 | 79 | 09 | 64 | 38

a_ | Solve Ux.+Uyy=0, for the following square using Relaxation method.
_ 1000 1000 1000
| Q6 2000 = ue 500
0-1; SO-1; (10 marks)
BL-6 ue U.
2000 2 - 0
000 500 0 °
oni Bos | 8 Estimate the extreme values of f(x,y)=x’+y” subject to the constraint x + 2y—1=0. | (10 marks)
Q7 a Review the Multiple Linear regression model, also state and explain any 2 statistical
CO-2: $0-5: parameters to analyze the performance of the Multiple Linear Regression Model. (10 marks)
BL-2 ;
CO-3: $0-2: b_ | Evaluate minimum value of the function f(x1,x2)= x1°+x2” using Newton’s method
BL6é. (10 marks)

(perform 3 iterations) starting at [3].

34
````

## Year not stated · Final-Exam · paper 63f56e5483ad

- Departments: Mechatronics
- Programmes: B TECH / MECHATRONICS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/MECHATRONICS/MODELLING AND SIMULATION/MODELLING AND SIMULATION (MECHATRONICS), FINAL EXAM.pdf`
- Printed on paper: max marks: 70; exam date: 27 November 2017
- Text: ocr (2 pages), mean OCR confidence 91.8

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (MECHATRONICS) P ; Year: III Semester: V _
Academic Year: 2017-2018
/ Subject: Modelling and Simulation _
‘ Marks: 70 ~~ att oF

Date: 27 November 2017 Time: 2.00 3 hg te gyi: die So o nite 5 Y.
- Durations: 3 ( gy q

No. of Pages: a)
A
(BULL IEE "46,

Final-Examination

Instructions: Candidates should read carefully the instructions printed on the.question paper and on the cover of the
Answer Book, which is provided for their use.

1) Question No.1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Attempt any four(Each sub-question carries 3.5 marks) (14)
1. Explain all the classifications of simulation model.
2. Explain any 4 different types of hypotheses.
3. Describe SIMSCRIPT software features suitable for simulation and modeling.
4. Briefly explain the steps of input model development.
5. How can you avoid initial transients in output analysis for simulation models?

6. With the help of any suitable example, explain reneging in queueing system.

Q.2 1. Explain estimation, estimator and all of it’s properties with suitable diagrams. (7)

2. Enumerate and explain various techniques for verification of simulation models. (7)

Q.3.1. Briefly explain validation, verification, credibility and accreditation. What do
you meant by 95% confidence interval? (7)

pea 2. i) How do you select models without proper input data? (7)

v/a
--- page 2 ---
ii) Input of sales volume of various product is required. Salesperson of product XYZ

says that : No fewer than 1000 units and no more than 5000 units will be sold. Given

her experience she believes there is a 90% chance of selling more than 2000 units, a 25%
of selling more than 2500 units, and only a 1% chance of selling more than 4500 units.
Translate the above information into a cumulative probability of being less than or equal to
those goals for simulation input. Also plot the cumulative frequency for the above goals.

Q 4.1 Compare Simulation languages with simulator with definitions, advantages
and disadvantages. (7)

2 ABC Ltd. is engaged in sale of footballs. Its cost per order is $400 and its carrying (7)
cost unit is $10 per unit per annum. The company has a demand for 20,000 units
per year. Calculate the order size, total orders required during a year, total carrying
cost and total ordering cost for the year.

Q 5.1 Kalyan Jwellers has a single cashier. During the rush hours, customers arrive at the rate of 10
per hour. The average number of customers that can be processed by the cashier is 12 per hour.
On the basis of this information, find the following: (7)

a) Probability that the cashier is idle

b) Average number of customers in the queuing system
c) Average time a customer spends in the system

d) Average number of customers in the queue

e) Average time a customer spends in the queue

2 State and describe different types of simulations with regard to output data analysis. (7)

Q6. 1 “Exponential distributions are memoryless.” Justify the statement with proper

Mathematical proof. (7)
2. Explain Welch Algorithm with required mathematical expressions. (7)
Q7 1. State the applications of Simulations in various fields. (Any 7) (7)

2. Consider a Poisson probability distribution with an average number of occurrences of two per

period. (7)
— a. Write the appropriate Poisson distribution.
-   b. What is the average number of occurrences in three time periods?
pees c. Write the appropriate Poisson function to determine the probability of x occurrences in

three time periods.
d. Compute the probability of two occurrences in one time period.
e. Compute the probability of six occurrences in three time periods.

2/2
````
