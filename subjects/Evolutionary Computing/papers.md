# Evolutionary Computing: question papers in full

10 unique papers · 2023-24 to 2025-26 · Artificial Intelligence

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 6 · paper 6d8ea9fe8319

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Evolutionary Computing/QP_Evolutionary Computing(702AI0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Evolutionary Computing
Date: 02 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
CO-2 ;   a   Discuss one recombination technique and one mutation technique in floating
SO-1 ;   point representation. Give example of one domain where this representation
BL-2   can be employed.
CO-2 ;   b
With reference to survivor selection mechanism, discuss fitness based &
SO-1 ;
age-based replacement techniques with the help of suitable examples.
BL-2
CO-4 ;   c
SO- 1;   Explain Bloat and Over Selection concept in Genetic Programming.
BL-3
CO-3 ;   d   Write the algorithm for Elitist Ant System Algorithm. Identify the key
SO-1 ;   features that differentiate the Elitist Ant System from Ant System
BL- 2   Algorithm.
a   Discuss drawbacks of partially mapped crossover technique for
permutation representation.
Consider the following two parents with permutation representation.
Parent 1: [9 5 6 1 3 7 8 4 2]
Parent 2: [5 6 4 1 8 3 2 9 7]
Q2
CO-2;   i.   Apply cycle crossover on the two-parent chromosome to obtain two
[10]
SO-1;   offsprings.
BL-2,3   ii. On the offsprings obtained after cycle crossover, apply swap
mutation on both the offsprings. Swap allele of positions 3 and 6.
iii.   Apply order crossover on the two chromosomes to obtain two
offsprings. Take the cross over points as 2 and 6.
iv.   For the offspring 1 obtained after order crossover, apply inversion
mutation on offspring 1 between points 2 and 5.
CO-2   b   Explain genitor survivor selection technique and elitism survivor selection
[05]
SO-1;   technique with suitable example.
********** 1 **********
--- page 2 ---
BL-2
CO-4   c
With the help of suitable block diagram, explain the steps in Genetic
SO-1;   [05]
Programming Algorithm.
BL-2
a   Consider the problem to Maximize 𝑓(𝑥) = 2𝑥1 2 −2𝑥1𝑥2 + 𝑥2 2 where
−4 ≤𝑥1, 𝑥2 ≤4 . Apply Particle Swarm Optimization to-
i.   Determine fitness of the initial population
ii.   Identify local best of each particle of the first generation and
identify the global best of the swarm
iii.   Update velocity, position only for the first particle of the second
generation
iv.   Evaluate fitness of the updated first particle and identify the local
Q3   best for the same.
CO-3;   The initial position and velocity are as given in the table below-
[10]
SO-1
BL-4,5   Index(i)   Xi(1)   Vi(1)
1   (2,3)   (0.0,0.0)
2   (-2,1)   (0.0,0.0)
3   (0,-3)   (0.0,0.0)
4   (4,-1)   (0.0,0.0)
5   (-1,2)   (0.0,0.0)
Take inertia weight 𝑤𝑡= 0.65, correction factors 𝑐1 = 2 𝑎𝑛𝑑 𝑐2 = 2.
Random numbers for the first particle are given below-
Particle   r1   r2
1   0.6   0.3
b   Consider the following Finite State Machine
CO-4
SO-1
[05]
BL-2
i.   For the input stream [0 1 1 1 0 1] evaluate the corresponding
output.
ii.   Evaluate fitness for the above input if the fitness function is
% of 𝐼𝑛𝑝𝑢𝑡𝑛+1 = 𝑂𝑢𝑡𝑝𝑢𝑡𝑛
iii.   Perform the mutation on the above state diagram by changing
the initial state to 𝐵 and obtain the output corresponding to the
same input given above
iv.   Evaluate the fitness using the function given above
CO-2   c   Consider a chromosome 𝑋= [1.2, 3.0, 4.5, −1]. The allowed range for
[05]
SO-1   each gene is [−1.0, 5.0]. Let the mutation probability 𝑝𝑚= 0.3. For each
********** 2 **********
--- page 3 ---
BL-3,4   gene the random number generated is [0.25, 0.4, 0.15, 0.5]. Apply creep
mutation to obtain the offspring. Let creep value ∆= 0.7.
Q4   a
CO-3   Discuss general principles of swarm intelligence. State main reasons for
[05]
SO-1   success of a swarm.
BL-2
CO-1   b
Sketch a suitable flow diagram for evolutionary algorithm and explain the
SO-1   [05]
following components in brief- Population, Fitness, Parent Selection.
BL-2
c   Consider a problem where we must minimize the function where
𝑓(𝑥) = 𝑥3 −4
Single parent in the population 𝑥= 3
Initial variation 𝜎= 1
CO-4   Let the random numbers taken from the normal distribution for mutation
SO-1   are
[10]
BL-4,5   𝑧𝑖= [0.8, −0.2, 0.2, 0.5, −0.4]
i.   Using two membered evolutionary strategy algorithm, generate five
off springs from parent given above.
ii.   Compute fitness of parent and off springs
iii.   Evaluate new 𝜎 based on 1/5 success rule
iv.   State your inference about 𝜎 obtained in (iii) above
a   Consider a problem statement to minimize 𝑓(𝑥) = 𝑥1 −2𝑥2 + 𝑥3 where
𝑥𝑗∈[−8,8].
Individual 1   Individual 2   Individual 3   Individual 4
𝑥1   -1   2   -5   -4
𝑥2.   5   -3   1   -2
𝑥3.   3   1   3   1
Here population size 𝑁= 4, number of parameters 𝐷= 3, Crossover rate
Q5   𝐶𝑅= 0.5, Mutation factor 𝐹= 0.7, Random integer for recombination step
CO-4   𝐼𝑟𝑎𝑛𝑑= 2,
SO-1   Random number for selection of each element during recombination step = [10]
BL-2,3   [0.6, 0.8, 0.95]
Apply Differential Evolution Algorithm to-
i.   Generate weighted difference vector using Individual 3 and
Individual 4.
ii.   Generate the noisy vector using Individual 1 and the weighted
difference vector.
iii.   Construct trial vector using Individual 2 as parent and the noisy
vector
iv.   Evaluate fitness of parent vector and offspring vector. State your
inference.
b   Consider 4 Cities A, B, C, D to be travelled by the ant, starting at City A.
CO-3   The ant should return back to City A after covering all the cities.
SO-1   The distance matrix is given as:
[10]
BL-4
A   B   C   D
A   0   5   2   7
********** 3 **********
--- page 4 ---
B   4   0   1   8
C   2   2   0   7
D   7   9   2   0
The Pheromone Matrix is:
A   B   C   D
A   0   1   1   1
B   1   0   1   1
C   1   1   0   1
D   1   1   1   0
i. Taking city A as the starting point, evaluate probabilities of taking
path AB, AC and AD. (Assume 𝛼= 1 𝑎𝑛𝑑 𝛽= 1)
ii. Explain the importance 𝛼 𝑎𝑛𝑑 𝛽 while evaluating probabilities
iii. Let the path traversed by one ant be A-C-B-D-A. Using Ant system
algorithm, update the pheromone matrix. (Assume evaporation rate
as 𝜌= 0.7)
iv. Discuss the effect of evaporation rate on pheromone level.
a   With the help of suitable pseudocode, demonstrate the steps in Tournament
Selection Algorithm.
Consider the following objective function which has to be minimized.
𝑓(𝑥) = 𝑥1 2 −𝑥2 + 2𝑥3
The solutions in the initial population are given below.
Individual   A   B   C   D
Q6
Genotype   [2,3,5]   [1,2,3]   [3,1,2]   [2,5,6]
CO-2
SO-1   [10]
BL-3,5   Using genetic algorithm approach, answer the following-
i.   Implement tournament selection rounds to select two parents as
follows
1st Tournament between individuals A and D
2nd Tournament between individuals B and C
ii.   Use one point crossover between the winner parents from step (i).
Take crossover point as 2.
iii.   Evaluate fitness of the two offspring
b   Consider the following problem. You have a knapsack of capacity 13kg, and
you must choose from the following six items, maximizing total value while
keeping the total weight ≤ 13 kg. Each item can be either included (1) or not
included (0) in the knapsack.
Item   Weight (kg)   Value
P   2   3
CO-1   Q   3   4
SO-1   R   4   5
[10]
BL-2, 4   S   5   8
T   6   9
U   7   10
i   Create two parent chromosomes of length 6 each by selecting items
[P,Q,T] in chromosome 1 and items [Q, R, S] in chromosome 2
ii Compute two off springs using Uniform cross over with p=0.5
where the random number for each gene is [0.3, 0.2, 0.4, 0.6, 0.1,
0.8]
********** 4 **********
--- page 5 ---
iii Perform mutation by flipping bits 1,3,5 in offspring 1 and 2,4,6 in
offspring 2
iv   Calculate fitness of each offspring and comment on the same
a   With reference to Rank Based Ant System Algorithm, answer the
following question
Q7
i.   Discuss the concept of pheromone trails update in Rank Based Ant
CO-3
System Algorithm
SO-1   [10]
ii.   Write the expression for pheromone update rule
BL-2,3
iii.   Explain each component of the expression in (ii)
iv.   Elaborate on the key differences between Ant System Algorithm
and Rank Based Ant System Algorithm
b   State the factors on which flow of information depends upon through a
CO-3   Social Structure. Discuss with the help of suitable diagram Star Social
SO-1   Structure, Ring Social Structure, Wheel Social Structure and Von
[10]
BL-2   Neumann Social Structure with reference to network topologies in Particle
Swarm Optimization
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 3bef70d18021

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/Evolutionary Computing/QP_Evolutionary Computing(702AI0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Evolutionary Computing
Date: 02 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
CO-2 ;   a   Discuss one recombination technique and one mutation technique in floating
SO-1 ;   point representation. Give example of one domain where this representation
BL-2   can be employed.
CO-2 ;   b
With reference to survivor selection mechanism, discuss fitness based &
SO-1 ;
age-based replacement techniques with the help of suitable examples.
BL-2
CO-4 ;   c
SO- 1;   Explain Bloat and Over Selection concept in Genetic Programming.
BL-3
CO-3 ;   d   Write the algorithm for Elitist Ant System Algorithm. Identify the key
SO-1 ;   features that differentiate the Elitist Ant System from Ant System
BL- 2   Algorithm.
a   Discuss drawbacks of partially mapped crossover technique for
permutation representation.
Consider the following two parents with permutation representation.
Parent 1: [9 5 6 1 3 7 8 4 2]
Parent 2: [5 6 4 1 8 3 2 9 7]
Q2
CO-2;   i.   Apply cycle crossover on the two-parent chromosome to obtain two
[10]
SO-1;   offsprings.
BL-2,3   ii. On the offsprings obtained after cycle crossover, apply swap
mutation on both the offsprings. Swap allele of positions 3 and 6.
iii.   Apply order crossover on the two chromosomes to obtain two
offsprings. Take the cross over points as 2 and 6.
iv.   For the offspring 1 obtained after order crossover, apply inversion
mutation on offspring 1 between points 2 and 5.
CO-2   b   Explain genitor survivor selection technique and elitism survivor selection
[05]
SO-1;   technique with suitable example.
********** 1 **********
--- page 2 ---
BL-2
CO-4   c
With the help of suitable block diagram, explain the steps in Genetic
SO-1;   [05]
Programming Algorithm.
BL-2
a   Consider the problem to Maximize 𝑓(𝑥) = 2𝑥1 2 −2𝑥1𝑥2 + 𝑥2 2 where
−4 ≤𝑥1, 𝑥2 ≤4 . Apply Particle Swarm Optimization to-
i.   Determine fitness of the initial population
ii.   Identify local best of each particle of the first generation and
identify the global best of the swarm
iii.   Update velocity, position only for the first particle of the second
generation
iv.   Evaluate fitness of the updated first particle and identify the local
Q3   best for the same.
CO-3;   The initial position and velocity are as given in the table below-
[10]
SO-1
BL-4,5   Index(i)   Xi(1)   Vi(1)
1   (2,3)   (0.0,0.0)
2   (-2,1)   (0.0,0.0)
3   (0,-3)   (0.0,0.0)
4   (4,-1)   (0.0,0.0)
5   (-1,2)   (0.0,0.0)
Take inertia weight 𝑤𝑡= 0.65, correction factors 𝑐1 = 2 𝑎𝑛𝑑 𝑐2 = 2.
Random numbers for the first particle are given below-
Particle   r1   r2
1   0.6   0.3
b   Consider the following Finite State Machine
CO-4
SO-1
[05]
BL-2
i.   For the input stream [0 1 1 1 0 1] evaluate the corresponding
output.
ii.   Evaluate fitness for the above input if the fitness function is
% of 𝐼𝑛𝑝𝑢𝑡𝑛+1 = 𝑂𝑢𝑡𝑝𝑢𝑡𝑛
iii.   Perform the mutation on the above state diagram by changing
the initial state to 𝐵 and obtain the output corresponding to the
same input given above
iv.   Evaluate the fitness using the function given above
CO-2   c   Consider a chromosome 𝑋= [1.2, 3.0, 4.5, −1]. The allowed range for
[05]
SO-1   each gene is [−1.0, 5.0]. Let the mutation probability 𝑝𝑚= 0.3. For each
********** 2 **********
--- page 3 ---
BL-3,4   gene the random number generated is [0.25, 0.4, 0.15, 0.5]. Apply creep
mutation to obtain the offspring. Let creep value ∆= 0.7.
Q4   a
CO-3   Discuss general principles of swarm intelligence. State main reasons for
[05]
SO-1   success of a swarm.
BL-2
CO-1   b
Sketch a suitable flow diagram for evolutionary algorithm and explain the
SO-1   [05]
following components in brief- Population, Fitness, Parent Selection.
BL-2
c   Consider a problem where we must minimize the function where
𝑓(𝑥) = 𝑥3 −4
Single parent in the population 𝑥= 3
Initial variation 𝜎= 1
CO-4   Let the random numbers taken from the normal distribution for mutation
SO-1   are
[10]
BL-4,5   𝑧𝑖= [0.8, −0.2, 0.2, 0.5, −0.4]
i.   Using two membered evolutionary strategy algorithm, generate five
off springs from parent given above.
ii.   Compute fitness of parent and off springs
iii.   Evaluate new 𝜎 based on 1/5 success rule
iv.   State your inference about 𝜎 obtained in (iii) above
a   Consider a problem statement to minimize 𝑓(𝑥) = 𝑥1 −2𝑥2 + 𝑥3 where
𝑥𝑗∈[−8,8].
Individual 1   Individual 2   Individual 3   Individual 4
𝑥1   -1   2   -5   -4
𝑥2.   5   -3   1   -2
𝑥3.   3   1   3   1
Here population size 𝑁= 4, number of parameters 𝐷= 3, Crossover rate
Q5   𝐶𝑅= 0.5, Mutation factor 𝐹= 0.7, Random integer for recombination step
CO-4   𝐼𝑟𝑎𝑛𝑑= 2,
SO-1   Random number for selection of each element during recombination step = [10]
BL-2,3   [0.6, 0.8, 0.95]
Apply Differential Evolution Algorithm to-
i.   Generate weighted difference vector using Individual 3 and
Individual 4.
ii.   Generate the noisy vector using Individual 1 and the weighted
difference vector.
iii.   Construct trial vector using Individual 2 as parent and the noisy
vector
iv.   Evaluate fitness of parent vector and offspring vector. State your
inference.
b   Consider 4 Cities A, B, C, D to be travelled by the ant, starting at City A.
CO-3   The ant should return back to City A after covering all the cities.
SO-1   The distance matrix is given as:
[10]
BL-4
A   B   C   D
A   0   5   2   7
********** 3 **********
--- page 4 ---
B   4   0   1   8
C   2   2   0   7
D   7   9   2   0
The Pheromone Matrix is:
A   B   C   D
A   0   1   1   1
B   1   0   1   1
C   1   1   0   1
D   1   1   1   0
i. Taking city A as the starting point, evaluate probabilities of taking
path AB, AC and AD. (Assume 𝛼= 1 𝑎𝑛𝑑 𝛽= 1)
ii. Explain the importance 𝛼 𝑎𝑛𝑑 𝛽 while evaluating probabilities
iii. Let the path traversed by one ant be A-C-B-D-A. Using Ant system
algorithm, update the pheromone matrix. (Assume evaporation rate
as 𝜌= 0.7)
iv. Discuss the effect of evaporation rate on pheromone level.
a   With the help of suitable pseudocode, demonstrate the steps in Tournament
Selection Algorithm.
Consider the following objective function which has to be minimized.
𝑓(𝑥) = 𝑥1 2 −𝑥2 + 2𝑥3
The solutions in the initial population are given below.
Individual   A   B   C   D
Q6
Genotype   [2,3,5]   [1,2,3]   [3,1,2]   [2,5,6]
CO-2
SO-1   [10]
BL-3,5   Using genetic algorithm approach, answer the following-
i.   Implement tournament selection rounds to select two parents as
follows
1st Tournament between individuals A and D
2nd Tournament between individuals B and C
ii.   Use one point crossover between the winner parents from step (i).
Take crossover point as 2.
iii.   Evaluate fitness of the two offspring
b   Consider the following problem. You have a knapsack of capacity 13kg, and
you must choose from the following six items, maximizing total value while
keeping the total weight ≤ 13 kg. Each item can be either included (1) or not
included (0) in the knapsack.
Item   Weight (kg)   Value
P   2   3
CO-1   Q   3   4
SO-1   R   4   5
[10]
BL-2, 4   S   5   8
T   6   9
U   7   10
i   Create two parent chromosomes of length 6 each by selecting items
[P,Q,T] in chromosome 1 and items [Q, R, S] in chromosome 2
ii Compute two off springs using Uniform cross over with p=0.5
where the random number for each gene is [0.3, 0.2, 0.4, 0.6, 0.1,
0.8]
********** 4 **********
--- page 5 ---
iii Perform mutation by flipping bits 1,3,5 in offspring 1 and 2,4,6 in
offspring 2
iv   Calculate fitness of each offspring and comment on the same
a   With reference to Rank Based Ant System Algorithm, answer the
following question
Q7
i.   Discuss the concept of pheromone trails update in Rank Based Ant
CO-3
System Algorithm
SO-1   [10]
ii.   Write the expression for pheromone update rule
BL-2,3
iii.   Explain each component of the expression in (ii)
iv.   Elaborate on the key differences between Ant System Algorithm
and Rank Based Ant System Algorithm
b   State the factors on which flow of information depends upon through a
CO-3   Social Structure. Discuss with the help of suitable diagram Star Social
SO-1   Structure, Ring Social Structure, Wheel Social Structure and Von
[10]
BL-2   Neumann Social Structure with reference to network topologies in Particle
Swarm Optimization
********** 5 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 96aa9ef4677c

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AI_7012/Evolutionary Computing/QP_Evolutionary Computing(702AI0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Evolutionary Computing
Date: 29 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
CO-2 ;   a   With reference to permutation representation, discuss the following two
SO-1 ;   mutation techniques- scramble mutation, swap mutation using suitable
BL-2   examples.
CO-2 ;   b   Discuss Linear and Exponential Rank-based parent selection mechanism
SO-1 ;   with suitable expression.
BL-2
c   Compare Genetic Algorithm and Genetic Programming with reference to
CO-4 ;
the following points-
SO- 1;
Representation, Recombination, Mutation, Parent Selection, Survivor
BL-3
Selection
CO-3 ;   d   For Ant System algorithm state and explain equations to update the
SO-1 ;   pheromone level with and without evaporation. State the significance of
BL- 2   evaporation rate in terms of exploration and exploitation.
a   i.   Apply Order Crossover to generate two off springs. Assume the
Crossover points as 3 and 5.
Parent 1: 8 6 5 7 3 2 1 4
Parent 2: 1 2 7 3 4 5 6 8
ii.   Apply uniform crossover on the following parents to generate
two offsprings using the crossover mask as given-
Q2
Parent 1: 1 1 0 1 0 0 1 0
CO-2;
Parent 2: 0 1 1 0 1 1 1 1   [10]
SO-1;
Uniform crossover mask: 1 1 1 0 0 0 1 1
BL-2,3
iii.   Consider the chromosome 𝑌= [4,6,2,9,3,7]. The allowed gene
range is   [0-9]. Mutation probability for each gene is 𝑝𝑚= 0.4.
The random numbers   generated   for each gene   are
[0.35,0.45, 0.1,0.67, 0.25, 0.75] . Apply creep mutation with
creep value ∆= −1.
iv.   State the expression for random setting in integer representation.
CO-2   b
Explain fitness sharing diversity maintenance approach with suitable
SO-1;   [05]
expressions.
BL-2
********** 1 **********
--- page 2 ---
CO-4   c
With reference to Genetic Programming, explain Grow and Full methods for
SO-1;   [05]
population initialization.
BL-2
a   Consider the problem to Maximize 𝑓(𝑥) = 50(𝑥1 2 −𝑥2 2) where
−3 ≤𝑥1, 𝑥2 ≤3 . Apply GBest Particle Swarm Optimization Algorithm
to-
i.   Determine fitness of the initial population.
ii.   Identify personal best of each particle of the first generation and
identify the global best of the swarm.
iii.   Update velocity, position only for the second particle of the second
generation
iv.   Evaluate fitness of the updated second particle and identify the
personal best for the same.
Q3   The initial position and velocity are as given in the table below-
CO-3;
[10]
SO-1   Index(i)   Xi(1)   Vi(1)
BL-4,5   1   (3,2)   (0.0,0.0)
2   (-1,3)   (0.0,0.0)
3   (0,-3)   (0.0,0.0)
4   (1,-2)   (0.0,0.0)
5   (-1,-2)   (0.0,0.0)
Take inertia weight 𝑤𝑡= 0.75, correction factors 𝑐1 = 2 𝑎𝑛𝑑 𝑐2 = 2.
Random numbers for the second particle are given below-
Particle   r1   r2
2   0.3   0.5
b   Consider the following Finite State Machine (FSM)
CO-4
SO-1
[05]
BL-2
i.   For the input stream [0 1 1 1 0 1] evaluate the corresponding
output.
ii.   Evaluate fitness for the above input if the fitness function is-
% 𝑜𝑓 𝐼𝑛𝑝𝑢𝑡𝑛+1 = 𝑂𝑢𝑡𝑝𝑢𝑡𝑛
iii.   Perform the mutation on the above state diagram by changing
the initial state to 2 and obtain the output corresponding to the
same input given above.
iv.   Evaluate fitness using the function given above.
c   i.   State two common applications where permutation representation
can be used.
CO-2
ii.   Apply cycle crossover on the following two parents to obtain two
SO-1   [05]
offsprings.
BL-3,4
Parent 1: 9 8 7 6 5 4 3 2 1
Parent 2: 4 1 5 6 2 8 7 3 9
********** 2 **********
--- page 3 ---
Q4   a
With reference to Particle Swarm Optimization, explain the following
CO-3
social network structure with appropriate diagrams- Star social structure   [05]
SO-1
and Ring social structure.
BL-2
CO-1   b   Write the pseudocode of Evolutionary Algorithm. Discuss the following
SO-1   components of Evolutionary Algorithm in not more than 2 lines each-   [05]
BL-2   Representation, Evaluation Function, Termination Condition.
c   Consider a problem statement to minimize 𝑓(𝑦) = 𝑦1 + 4𝑦2 + 2𝑦3 where
𝑦𝑗∈[−9,9].
Individual 1   Individual 2   Individual 3 Individual 4
𝑦1   -2   2   -4   -5
𝑦2   4   -3   1   -2
𝑦3   2   1   2   3
CO-4   Here population size 𝑁= 4, number of parameters 𝐷= 3, Crossover rate
SO-1   𝐶𝑅= 0.7, Mutation factor 𝐹= 0.6, Random integer for recombination step
BL-4,5   𝐼𝑟𝑎𝑛𝑑= 3 , Random number for selection of each element during [10]
recombination step = [0.5, 0.85, 0.9]
Apply Differential Evolution Algorithm to-
i.   Generate weighted difference vector using Individual 1 and
Individual 4.
ii.   Generate the noisy vector using Individual 3 and the weighted
difference vector.
iii.   Construct trial vector using Individual 2 as parent and the noisy
vector.
iv.   Evaluate fitness of parent vector and offspring vector. State your
inference.
a   For a minimization problem the given function is as follows:
𝑓(𝑥) = 2𝑥2 −3
Single parent in the population 𝑥= 4
Initial variation 𝜎= 1
Let the random numbers taken from the normal distribution for mutation
Q5   are-
CO-4   𝑧𝑖= [0.7, −0.2, 0.3, 0.5, −0.6]
SO-1   [10]
BL-2,3   i.   Using two membered evolutionary strategy algorithm, generate five
off springs from parent given above.
ii.   Compute fitness of parent and off springs.
iii.   Evaluate new 𝜎 based on 1/5 success rule. Take the value of 𝑐=
0.8.
iv.   State your inference about 𝜎 obtained in (iii) above.
b   Discuss the improvement of Elitist Ant System Algorithm over Ant System
CO-3   Algorithm with reference to pheromone update expression.
SO-1
[10]
BL-4   Consider the following distance graph and pheromone level graph for the
Travelling Salesman Problem where nodes A, B, C and D represent four
cities.
********** 3 **********
--- page 4 ---
Distance graph   Initial Pheromone level graph
The two ants in this problem have traversed the following loop-
Ant 1: A-B-C-D-A and Ant 2: A-C-B-D-A
i.   Compute the pheromone level 𝜏𝐴𝐷 𝑎𝑛𝑑 𝜏𝐵𝐷 with evaporation rate
𝜌= 0.8 using expression of Elitist Ant System Algorithm. Take
parameter that defines weight given to the best-so-far tour 𝑒= 2.
ii.   Compute the pheromone level 𝜏𝐴𝐷 𝑎𝑛𝑑 𝜏𝐵𝐷 with evaporation rate
𝜌= 0.8 using expression of Ant System Algorithm
iii.   State your inference about pheromone level based on the results
obtained in (i) and (ii)
a   i.   Explain Fitness Proportionate Selection mechanism for parent
selection with the help of suitable expression.
ii.   Explain how Fitness Proportional Selection Mechanism suffers
from – premature convergence and high susceptibility to
function transposition.
iii.   Consider the following five chromosomes in the initial
population, 𝑥𝑖= {8, 21, 10, 12, and 5} . Complete the table
below and determine the two parents selected for recombination
using Roulette Wheel selection algorithm if the fitness function
is 𝑓(𝑥𝑖) = 3𝑥𝑖+ 2 and the random numbers generated are
{0.76, 0.23}.
Q6
CO-2   Chromosome Chromosome   Fitness   Probability   CDF
SO-1   value   [10]
BL-3,5   𝑥𝑖
A   8
B   21
C   10
D   12
E   5
********** 4 **********
--- page 5 ---
b   Consider a 4-Queens problem where the initial population has the
following four chromosomes.
A   2 3 2 4
B   3 1 2 4
C   4 2 3 1
D   1 3 4 2
i.   Compute fitness for each chromosome if the fitness function is
CO-1   number of non-attacking queens.
SO-1   ii.   Implement tournament selection rounds to select two parents as   [10]
BL-2, 4   follows-
1st Tournament between chromosomes A and D.
2nd Tournament between chromosomes B and C.
iii.   Apply one point crossover between the parents obtained in (ii)
to obtain the two offsprings. Take cross over point as 1.
iv.   Apply swap mutation only on offspring 1. Swap allele in
position 2 and 4.
v.   Evaluate the fitness of both the offsprings.
a   With reference to Max-Min Ant System Algorithm, answer the following
question
Q7
i.   Discuss the concept of pheromone trails update in Max-Min Ant
CO-3
System Algorithm.
SO-1   [10]
ii.   Write the expression for pheromone update rule.
BL-2,3
iii.   Explain each component of the expression in (ii).
iv.   Elaborate on the key differences between Ant System Algorithm
and Max-Min Ant System Algorithm.
CO-3   b   i.   Discuss the significance of velocity clamping and inertia weights
SO-1   with the help of suitable expressions.
[10]
BL-2   ii.   Explain the following rules with respect to the flocking behavior in
particle swarm optimization- Separation, Alignment, Cohesion.
********** 5 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 2f58d0202d6e

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/EVOLUTIONARY COMPUTING/Evolutionary Computing, Sem-VI, Batch 2024-25 & 2025-2026, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 June 2026
- Text: ocr (5 pages), mean OCR confidence 88.3

````text
SVKM’S NMIMS
/ MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING
Academic Year: 2025-26

Program: B Tech/ MBA Tech (AT)

Year: HI Semester :
Subject: Evolutionary Computing e
Time: 10.00 am to 1.00 pm (3 hrs)
Date : 29 June 2026 :
No. of Pages: OS
Marks: 100

Re-Exam (2024-25/2025-26)

Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No._1___ is compulsory.
5. Out of remaining questions, attempt any 4 _ questions
6. Inall__5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.

rt
Ql Answer briefly: [20]
CO-2 ; a With reference to permutation representation, discuss the following two
SO-1 ; mutation techniques- scramble mutation, swap mutation using suitable
BL-2 examples. ‘
CO-2 ; b Discuss Linear and Exponential Rank-based parent selection mechanism
SO-1 ; with suitable expression.
BL-2
CO-4: c Compare Genetic Algorithm and Genetic Programming with reference to
SO- I the following points- a ;
BL-3 > Representation, Recombination, Mutation, Parent Selection, Survivor
Selection
CO-3 ; d For Ant System algorithm state and explain equations to update the
SO-1 ; pheromone level with and without evaporation. State the significance of
BL- 2 evaporation rate in terms of exploration and exploitation.
§ a i. Apply Order Crossover to generate two off springs. Assume the
Crossover points as 3 and 5.
Parent 1:86573214
Parent 2:12734568
_ i Apply uniform crossover on the following parents to generate
Q2 , two offsprings using the crossover mask as given-
CO-2: Parent 1:11010010
SO-1: Parent 2: 01101111 [10]
BL-2.3 Uniform crossover mask: 1 1100011
° f iii. Consider the chromosome Y = [4,6,2,9,3,7]. The allowed gene
range is [0-9]. Mutation probability for each gene is p,, = 0.4.
The random numbers generated for each gene are
[0.35, 0.45, 0.1,0.6.7,0.25,0.75] . Apply creep mutation with
creep value A= —1.
iv. State the expression for random setting in integer representation,
sory. fyb Explain fitness sharing diversity maintenance approach with suitable [05]
BL-2 expressions. ;

FRR RK RRR Ke
--- page 2 ---
CO-4 ec

SO-1: With reference to Genetic Programming, explain Grow and Full methods for [05]
> population initialization. :
BL-2 5
a Consider the problem to Maximize f(x) = 50(x? — x2) where

—3 S X4,Xz <3. Apply GBest Particle Swarm Optimization Algorithm
to- :
i. Determine fitness of the initial population.
ii. _ Identify personal best of each particle of the first generation and
identify the global best of the swarm.
ili. Update velocity, position only for the second particle of the second
generation
iv. Evaluate fitness of the updated second particle and identify the
personal best for the same.

o ” The initial position and velocity are as given in the table below-
SO-1 , F [10]
Index(i) XM) vi
Bll 1 G2) (0.0,0.0) a
2 (-1,3) (0.0,0.0)
3 (0,-3) . (0.0,0.0)
4 - | (,-2) (0.0,0.0)
5 (-1,-2) (0.0,0.0)
Take inertia weight w, = 0.75, correction factors c, = 2 and cy = 2.
Random numbers for the second particle are given below-
Particle | rl 12
2 0.3 0.5
b Consider the following Finite State Machine (FSM)
on ) : @
co-4 C) “
SO-1
BL-2 é [05]
2 1 For the input stream [0 1 1 1 0 1] evaluate the corresponding
output.
il. Evaluate fitness for the above input if the fitness function is-
% of Inputn,, = Output,
ii. Perform the mutation on the above state diagram by changing
the initial state to 2 and obtain the output corresponding to the
same input given above.
iv. Evaluate fitness using the function given above. __
c i. State two common applications where permutation representation
can be used.
CO-2 .. : .
SO-1 ; il. Apply cycle crossover on the following two parents to obtain two [05]
BL-3,4 offsprings.

Parent 1:987654321
Parent 2:415628739

FRR Rk
--- page 3 ---
Q4

With reference to Particle Swarm Optimization, explain the following

Son social network structure with appropriate diagrams- Star social st®acture [05]
BL-2 and Ring social structure. a
CO-1 Write the pseudocode of Evolutionary Algorithm. Pima the following
SO-1 components of Evolutionary Algorithm in not more than 2 lines each- [05]
BL-2 Representation, Evaluation Function, Termination Condition.
Consider a problem statement to minimize f(y) = y, + 4y2 + 2y3 where
y; € [-9,9].
Individual 1_| Individual 2 Individual 3 | Individual 4
V4 -2 2 4 -5
2 4 3 1 -2
V3 py) 1 2 3
CO-4 Here population size N = 4, number of parameters D = 3, Crossover rate
| so-1 CR = 0.7, Mutation factor F = 0.6, Random integer for recombination step
BL-4,5 T-and = 3, Random number for selection of each element during [10]
recombination step = [0.5, 0.85, 0.9]
Apply Differential Evolution Algorithm to-
i. Generate weighted difference vector using Individual 1 and
Individual 4.
il. Generate the noisy vector using individant 3 and the weighted
difference vector.
ili. Construct trial vector using Individual 2 as parent and the noisy
vector.
iv. Evaluate fitness of parent vector and offspring vector. State your
inference.
For a minimization problem the given function is as follows:
f(x) = 2x? -3
Single parent in the population x = 4
e@ Initial variation 0 = 1
Let the random numbers taken from the normal distribution for mutation
Q5 are-
CO-4 2; = [0.7, —0.2, 0.3, 0.5, —0.6]
SO-1 [10]
BL-2,3 “i, Using two membered evolutionary strategy algorithm, generate five
off springs from parent given above.
ii. | Compute fitness of parent and off springs.
ili. | Evaluate new o based on 1/5 success rule. Take the value of c =
0.8.
iv. State your inference about o obtained in (iii) above.
Discuss the improvement of Eljtist Ant System Algorithm over Ant System
CO-3 Algorithm with reference to pheromone update expression.
SO-1 [10]
BL-4 Consider the following distance graph and pheromone level graph for the

Travelling Salesman Problem where nodes A, B, C and D represent four
cities.

FIG a ik
--- page 4 ---
Distance graph Initial Pheromone level graph

OY)
7

The two ants in this problem have traversed the following loop-
Ant 1: A-B-C-D-A and Ant 2: A-C-B-D-A
i. Compute the pheromone level t4p and Tgp with evaporation rate
p = 0.8 using expression of Elitist Ant System Algorithm. Take
parameter that defines weight given to the best-so-far tour e = 2. QR
ii. Compute the pheromone level t4p and Tgp with evaporation rate
p = 0.8 using expression of Ant System Algorithm
iii. State your inference about pheromone level based on the results
obtained in (i) and (ii)

a i. Explain Fitness Proportionate Selection mechanism for parent
selection with the help of suitable expression.
il. Explain how Fitness Proportional Selection Mechanism suffers

from — premature convergence and high susceptibility to
function transposition.

ili. Consider the following five chromosomes in the initial
population, x; = {8,21,10,12,and5}. Complete the table
below and determine the two parents selected for recombination
using Roulette Wheel selection algorithm if the fitness function
is f(x;) =3x;+.2 and the random numbers generated are

{0.76, 0.23}. ‘ ie

Q6 : =
CcO-2 Chromosome | Chromosome _ | Fitness Probability | CDF
SO-1 . value [10]
BL-3,5 : Xj

A 8

B 21

Cc 10

D 12

E 5

FOI GRA x
--- page 5 ---
Consider a 4-Queens problem where the initial population has the
following four chromosomes.

A 2324

Lad
B 3124
Cc 4231]
D 1342
i. Compute fitness for each chromosome if the fitness function i is
CO-1 number of non-attacking queens.
SO-1 ii. Implement tournament selection rounds to select two parents as 10]
BL-2, 4 follows-
1* Tournament between chromosomes A and D.
24 Tournament between chromosomes B and C.
iii. Apply one point crossover between the parents obtained in (ii)
to obtain the two offsprings. Take cross over point as 1.
iv. Apply swap mutation only on offspring 1. Swap allele in
position 2 and 4.
Vv. Evaluate the fitness of both the offsprings.
With reference to Max-Min Ant System Algorithm, answer the following
Q7 question ,
C03 i. Discuss the concept of pheromone trails update in Max-Min Ant
SO-1 . System Algorithm. : [10]
BL-2.3 il. Write the expression for pheromone update rule.
> ii. Explain each component of the expression in (ii).
iv. Elaborate on the key: differences between Ant System Algorithm
and Max-Min Ant System Algorithm,
CO-3 i. Discuss the significance of velocity clamping and inertia weights
SO-1 with the help of suitable expressions. [10]
BL-2 ii.

Explain the following rules with respect to the flocking behavior in
particle swarm optimization- Separation, Alignment, Cohesion.

SRK Dd
````

## 2024-25 · Final + Re-Exam · Sem 6 · paper 5b0212d3404a

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/EVOLUTIONARY COMPUTING/Evolutionary Computing, Sem VI, Final Exam 2024-25 & Re Exam 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 76.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
"Academic Year: 2024-2025

Program/s: _ BTECH/MBA TECH Year: I] Semester: VI
Stream/s;_AI/AIDS

Subject: __ Evolutionary Computing_ Time: _3 hrs (250pmto_ 5% ODpus)
Date:_7_/ 5/2025 No. of Pages:_5

Marks: 100" §

Final Examination 2024-25/Re-Examination (2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.
3)Inall__5_ questions to be attempted.

4) All questions carry equal marks. :

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

2S ‘Answer briefly [20]
CO.2 . a With reference to mutation for permutation representation, explain insert
S0-1 : mutation, swap mutation and scramble mutation with the help of a suitable
BL2 example. Identify one use-case where permutation representation is used.
b Compare
CO- 2 i. Fitness based replacement and Age based replacement
SO- 1 ii, | Generational population management model with steady state
BL-3 population management model
c Compare Genetic Programming with Genetic Algorithm with reference to
CcO- 4 the following points-
SO- 1 . | Representation, Recombination, Mutation, Parent selection, Survivor
BL-3 selection
co-3; | d ; ; . . — =
SO- 1 Explain the concept of ant foraging, stigmergic communication and

BL-2 autocatalysis in ant colony optimization
--- page 2 ---
a With reference to edge crossover algorithm for permutation representation-

i. Discuss the steps for edge crossover algorithm
ii. Construct the edge table for the parents given below
Parent 1: [3 1642785]

Q2 - Parent 2: [75183264]
CcO-2 ; iii. Demonstrate the process of generating new offspring using the.
So-1 : tabular layout given below. Choose the initial random element in the [103
BL-4,5 offspring as [2]
Choices Element Reason Partial Result
Selected
All male Random [2]
b. Answer the following-
CO-2.4 i. Explain fitness sharing and crowding mechanism to preserve
SO-1. population diversity [10}
BL2 ii. Discuss Michigan Style Classifier System based in the following
; points- Representation, Recombination, Mutation, Parent Selection,

Survivor Selection, Fitness

a i. Apply uniform crossover on the following parents to generate one
offspring using the crossover mask as given-

Parent 1:11010010
Parent 2: 01101111

Q3 Uniform crossover mask: 11100011

CO-2 : [05]
SO-1 ii. Consider the following parent genotype with Permutation
BL-3 Representation

Parent 1:46573218

Parent 2:14732568

Apply Order Crossover to generate one off spring. Assume the
Crossover points as 4 and 7.

co 4d With the help of a suitable pseudocode, explain Two Membered [05]

SO-1 ; ‘
BL-2 Evolutionary Strategy Algorithm
--- page 3 ---
c Consider the problem to Minimize f(x) = (« — 5)*where
—7 <x <7. Apply Particle Swarm Optimization to
i. Determine fitness of the initial population
ii. Identify local best of each particle of the first generation and
identify the global best of swarm
iii, | Update velocity, position only for the first particle of the second

generation |

iv. Evaluate fitness of the updated first particle and identify the local
co-3 best for the same.
SO-1 The initial position and velocity are as given in the table below- [10]
BL-4,5 Index(i) XO VO

1 : 2 1.5

Zu 3.5 -0.5

3 4 1.0

4 1.5 2.0

Take inertia weight w, = 0.70, correction factors c, = 1.5.and cy = 1.5,
Random numbers for the first particle are given below-

Particle | ri - | 12
1 0.6 0.8
Q4 a
CcO-3 With reference to Particle Swarm Optimization, discuss the concept of [05]
SO-1 velocity clamping and justify its significance.
BL-2 f
CO-1 b Explain the significance of the following two main forces that form the basis
SO-I of any Evolutionary System. Give suitable examples for cach. [05]
i. Variation Operator
BL-2 FE ;
ii. _ Selection :
¢ Consider a problem statement to minimize f(x,y) = (¢ — 3)? + Gy +2)"
Individual P1 | Individual P2 | Individual P3 | Individual P4
x 2 4 1 5
y cl -3 0 2
Here population size N = 4, number of parameters D = 2, Crossover rate
CR = 0.7, Mutation factor F = 0.5, Random integer for recombination step
rand = 2, Random number for selection of each element during
co-4 recombination step = rand; = [0.65, 0.3]
SO-1 Apply Differential Evolution Algorithm to- [10]
BL-4,5 i. Generate weighted difference vector using Individual P2 and
Individual P3.
ii. Generate the noisy vector (donor vector) using Individual P1 and

the weighted difference vector. -

iii. Construct trial vector (offspring) using the noisy vector and
Individual P4 as parent.

iv. Evaluate the fitness of the offspring and the parent. State your
inference

— ~A-
--- page 4 ---
Consider: a problem of symbolic regression where the goal is to
automatically create a computer program whose output is equal to the values

Q5 of the quadratic equation x? — 3x +5 in the range of [-1,1]. Explain the
Cco-4 following preparatory steps of genetic programming for the given quadratic [10]
SO-1 equation —
BL-2 Terminal set, function sét, fitness measure, control parameters, termination
condition
Discuss the improvement of Max-Min Ant System Algorithm over Ant
System Algorithm with reference to pheromone update expression.
Consider the following distance graph and pheromone level graph for the
Travelling Salesman Problem where nodes A, B, C and D represent four
cities.
CO-4
SO-1 [10]
BL-4,5

Distance graph Initial Pheromone level graph

The two ants in this problem have traversed the following loop-
Ant 1: A-B-C-D-A and Ant 2: A-C-B-D-A

i. Compute the pheromone level t4p and tgp with evaporation rate
p = 0.5 using expression of Ant system Algorithm
ii. | Compute the pheromone level t4p and Tgp with evaporation rate
p = 0.5 using expression of Max Min Ant System Algorithm
iii. | State your inference about pheromone level based on the results
obtained in (i) and (ii)

Assume Q = 1, Tmax = 0.9 and Trin = 0.4
--- page 5 ---
i. Discuss two drawbacks of Fitness Proportionate Selection
Algorithm

ii. Explain Rank Based Selection with the help of appropriate
expression.

iii. Consider a population of size » =4 with its corresponding fitness
value as given in table below. Complete the table by evaluating
selection probabilities P,.;-for all the individuals using fitness
proportionate selection and rank based selection for various values

Q6 of s
CO-2
50-1 Individual | Fitness | Rank | P,., Prot Pret [10]
BL-2,45 Fitness | Rank Rank
Proport | based based
ionate (s=2) | (s=1.5)
A 1
B 2
Cc 3
D 4
iv. State your inference based on the results obtained in (iii)
With reference to Evolutionary Algorithm, define the following terms-.
Population, Chromosome, Gene, and Allele.
Apply Evolutionary Algorithm approach on the given 8-queens problem to,
complete the table below.
Cco-1 Parent Generate two off | Swap the] Off spring
So-1 Genotype springs by | first and | fitness [10]
BL-2,3 applying _two | last digits | (number of
point Crossover | in the off) non-attacking
at point 3 and 6 __| spring queens) |
43652141
24145.163
Q7 Explain with the help of a pseudocode Ant System Algorithm. Elaborate on
COo-1 the variations that are implemented in Elitist Ant System Algorithm. | [10]
S0-1 Discuss the key differences between Ant System Algorithm and Elitist Ant
BL-2,3 System Algorithm.
With reference to Particle Swarm Optimization(PSO) answer the following-
i. Fora minimization problem state and explain expression of personal
CO-1 best position of i*” particle in t*” generation.
ii. For a minimization problem state and explain expression of global
SO-1 b ~~ GP) Seay spe an ; [10]
BL2 est position of i“ particle in t™ generation.

iii. State velocity update expression and explain significance of each
term in the expression.

iv. _ Explain Global Best PSO algorithm with the help of a pseudocode.
--- page 6 ---
ak me a siemens “| “ey
— if ar 7
“(Ee

a ae oe

it rds aa a
````

## 2024-25 · Final + Re-Exam · paper aa49f7cb16d6

- Departments: Artificial Intelligence
- Programmes: MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/MBA TECH/3RD YEAR/ARTIFICIAL INTELLIGENCE/Evolutionary Computing/Evolutionary Computing , Final 2024-25, Re-exam 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 76.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
"Academic Year: 2024-2025

Program/s: _ BTECH/MBA TECH Year: I] Semester: VI
Stream/s;_AI/AIDS

Subject: __ Evolutionary Computing_ Time: _3 hrs (250pmto_ 5% ODpus)
Date:_7_/ 5/2025 No. of Pages:_5

Marks: 100" §

Final Examination 2024-25/Re-Examination (2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.
3)Inall__5_ questions to be attempted.

4) All questions carry equal marks. :

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

2S ‘Answer briefly [20]
CO.2 . a With reference to mutation for permutation representation, explain insert
S0-1 : mutation, swap mutation and scramble mutation with the help of a suitable
BL2 example. Identify one use-case where permutation representation is used.
b Compare
CO- 2 i. Fitness based replacement and Age based replacement
SO- 1 ii, | Generational population management model with steady state
BL-3 population management model
c Compare Genetic Programming with Genetic Algorithm with reference to
CcO- 4 the following points-
SO- 1 . | Representation, Recombination, Mutation, Parent selection, Survivor
BL-3 selection
co-3; | d ; ; . . — =
SO- 1 Explain the concept of ant foraging, stigmergic communication and

BL-2 autocatalysis in ant colony optimization
--- page 2 ---
a With reference to edge crossover algorithm for permutation representation-

i. Discuss the steps for edge crossover algorithm
ii. Construct the edge table for the parents given below
Parent 1: [3 1642785]

Q2 - Parent 2: [75183264]
CcO-2 ; iii. Demonstrate the process of generating new offspring using the.
So-1 : tabular layout given below. Choose the initial random element in the [103
BL-4,5 offspring as [2]
Choices Element Reason Partial Result
Selected
All male Random [2]
b. Answer the following-
CO-2.4 i. Explain fitness sharing and crowding mechanism to preserve
SO-1. population diversity [10}
BL2 ii. Discuss Michigan Style Classifier System based in the following
; points- Representation, Recombination, Mutation, Parent Selection,

Survivor Selection, Fitness

a i. Apply uniform crossover on the following parents to generate one
offspring using the crossover mask as given-

Parent 1:11010010
Parent 2: 01101111

Q3 Uniform crossover mask: 11100011

CO-2 : [05]
SO-1 ii. Consider the following parent genotype with Permutation
BL-3 Representation

Parent 1:46573218

Parent 2:14732568

Apply Order Crossover to generate one off spring. Assume the
Crossover points as 4 and 7.

co 4d With the help of a suitable pseudocode, explain Two Membered [05]

SO-1 ; ‘
BL-2 Evolutionary Strategy Algorithm
--- page 3 ---
c Consider the problem to Minimize f(x) = (« — 5)*where
—7 <x <7. Apply Particle Swarm Optimization to
i. Determine fitness of the initial population
ii. Identify local best of each particle of the first generation and
identify the global best of swarm
iii, | Update velocity, position only for the first particle of the second

generation |

iv. Evaluate fitness of the updated first particle and identify the local
co-3 best for the same.
SO-1 The initial position and velocity are as given in the table below- [10]
BL-4,5 Index(i) XO VO

1 : 2 1.5

Zu 3.5 -0.5

3 4 1.0

4 1.5 2.0

Take inertia weight w, = 0.70, correction factors c, = 1.5.and cy = 1.5,
Random numbers for the first particle are given below-

Particle | ri - | 12
1 0.6 0.8
Q4 a
CcO-3 With reference to Particle Swarm Optimization, discuss the concept of [05]
SO-1 velocity clamping and justify its significance.
BL-2 f
CO-1 b Explain the significance of the following two main forces that form the basis
SO-I of any Evolutionary System. Give suitable examples for cach. [05]
i. Variation Operator
BL-2 FE ;
ii. _ Selection :
¢ Consider a problem statement to minimize f(x,y) = (¢ — 3)? + Gy +2)"
Individual P1 | Individual P2 | Individual P3 | Individual P4
x 2 4 1 5
y cl -3 0 2
Here population size N = 4, number of parameters D = 2, Crossover rate
CR = 0.7, Mutation factor F = 0.5, Random integer for recombination step
rand = 2, Random number for selection of each element during
co-4 recombination step = rand; = [0.65, 0.3]
SO-1 Apply Differential Evolution Algorithm to- [10]
BL-4,5 i. Generate weighted difference vector using Individual P2 and
Individual P3.
ii. Generate the noisy vector (donor vector) using Individual P1 and

the weighted difference vector. -

iii. Construct trial vector (offspring) using the noisy vector and
Individual P4 as parent.

iv. Evaluate the fitness of the offspring and the parent. State your
inference

— ~A-
--- page 4 ---
Consider: a problem of symbolic regression where the goal is to
automatically create a computer program whose output is equal to the values

Q5 of the quadratic equation x? — 3x +5 in the range of [-1,1]. Explain the
Cco-4 following preparatory steps of genetic programming for the given quadratic [10]
SO-1 equation —
BL-2 Terminal set, function sét, fitness measure, control parameters, termination
condition
Discuss the improvement of Max-Min Ant System Algorithm over Ant
System Algorithm with reference to pheromone update expression.
Consider the following distance graph and pheromone level graph for the
Travelling Salesman Problem where nodes A, B, C and D represent four
cities.
CO-4
SO-1 [10]
BL-4,5

Distance graph Initial Pheromone level graph

The two ants in this problem have traversed the following loop-
Ant 1: A-B-C-D-A and Ant 2: A-C-B-D-A

i. Compute the pheromone level t4p and tgp with evaporation rate
p = 0.5 using expression of Ant system Algorithm
ii. | Compute the pheromone level t4p and Tgp with evaporation rate
p = 0.5 using expression of Max Min Ant System Algorithm
iii. | State your inference about pheromone level based on the results
obtained in (i) and (ii)

Assume Q = 1, Tmax = 0.9 and Trin = 0.4
--- page 5 ---
i. Discuss two drawbacks of Fitness Proportionate Selection
Algorithm

ii. Explain Rank Based Selection with the help of appropriate
expression.

iii. Consider a population of size » =4 with its corresponding fitness
value as given in table below. Complete the table by evaluating
selection probabilities P,.;-for all the individuals using fitness
proportionate selection and rank based selection for various values

Q6 of s
CO-2
50-1 Individual | Fitness | Rank | P,., Prot Pret [10]
BL-2,45 Fitness | Rank Rank
Proport | based based
ionate (s=2) | (s=1.5)
A 1
B 2
Cc 3
D 4
iv. State your inference based on the results obtained in (iii)
With reference to Evolutionary Algorithm, define the following terms-.
Population, Chromosome, Gene, and Allele.
Apply Evolutionary Algorithm approach on the given 8-queens problem to,
complete the table below.
Cco-1 Parent Generate two off | Swap the] Off spring
So-1 Genotype springs by | first and | fitness [10]
BL-2,3 applying _two | last digits | (number of
point Crossover | in the off) non-attacking
at point 3 and 6 __| spring queens) |
43652141
24145.163
Q7 Explain with the help of a pseudocode Ant System Algorithm. Elaborate on
COo-1 the variations that are implemented in Elitist Ant System Algorithm. | [10]
S0-1 Discuss the key differences between Ant System Algorithm and Elitist Ant
BL-2,3 System Algorithm.
With reference to Particle Swarm Optimization(PSO) answer the following-
i. Fora minimization problem state and explain expression of personal
CO-1 best position of i*” particle in t*” generation.
ii. For a minimization problem state and explain expression of global
SO-1 b ~~ GP) Seay spe an ; [10]
BL2 est position of i“ particle in t™ generation.

iii. State velocity update expression and explain significance of each
term in the expression.

iv. _ Explain Global Best PSO algorithm with the help of a pseudocode.
--- page 6 ---
ak me a siemens “| “ey
— if ar 7
“(Ee

a ae oe

it rds aa a
````

## 2023-24 · Final-Exam · Sem 6 · paper 2cf351ed9ac5

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/EVOLUTIONARY COMPUTING/Evolutionary Computing, Sem-VI, Final Exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 83.2

````text
ef AL

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS E
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024.

Program/s: B.Tech/MBA Tech "Year: IIT Semester: VI

Stream/s; AV/AIDS

Subject: Evolutionary Computing ; i Time: 3hrs * \(2200pato 5:00pm) -
Date:_%5 /Aps/ 2024 : . No. of Pages: 5

Marks: 100.
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

lai

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.
Ql. . ,

Answer briefly: ; [20]
ae Classify problems on the basis of modeling, simulation and optimization with .
So- iy ; the help of suitable block diagram ; [05]
BL-2
" b. “Tt is important to select appropriate form of representation while solving a

CO-2 ; problem through evolutionary approach”. Justify this statement by taking an [05]
es: example of binary representation and integer representation.
Ged With reference to population management models, compare generational
SO- 1 , model with steady state model. ‘ 2 [05]
BL-2
CO-3 ; la Extend the influence of ant colony concept on Ant Colony Optimization [05]
SO-1 ; : :
BL2 algorithms
--- page 2 ---
a Consider the fitness function f(x) = x* — 2x, where x is the decimal pe :
' [10]

representation of the initial population. Develop the following table.
String Initial “x value | Fitness
number Population - ; f(x)
: ; : =x? -2x
1 | 11010
= 00111
Q2 3" 10110
4 00001
CO-2,4;
SO-1; — : oe ,
BL-2,3,4 Using Genetic Algorithm concept, apply the following steps-
i. Implement one round of tournament selection as follows to
generate select two parents
a. 15* Tournament :(1;3), 2"! Tournament :(2,4)
ii. Use one point crossover on the two parents selected in step (i) to
generate two off springs. Take cross over point as 3.
iii. Evaluate fitness of the two offspring.

b Compare fitness based replacement strategy with age based fitness strategy.
we With reference to fitness based survivor strategy for survivor selecti on,
BL-2 explain the following methods- ,

Replace worst (Genitor), Elitism, (u + A) and (u, A) :
a Consider the following two parent chromosomes with permutation
representation. ;
3)1)2)4)5);6)/8)7)9
Q .
CO-1; 3]9])4)8]6]7|5|2)1 , [10] °
SO-1;
BL-3 ie
State the steps and apply the following crossover techniques
i. Partially Mapped Crossover with crossover points as 4 and 7
ii. Order crossover with crossover points as 4 and 7
--- page 3 ---
i

[b | With reference to Ant System Algorithm, explain the expressions to update
the pheromone level with and without evaporation rate. Discuss the effect of
evaporation rate on pheromone level. ;
For a travelling salesman problem distance matrix and pheromone level
matrix are as shown. With reference to Ant System Algorithm, perform the
following-

i. Ifan ant has to start the journey from city A, appraise the probability
‘of taking path AB, AC and AD. ,
ii. If the random number generated for this iteration is 0.63, which city

would be visited next according to the Roulette Wheel Selection

_ algorithm?
CO-3; :
SO-1,6; Assume control parametersa@=1landB=1. — | [10]
‘| BL-2,3,5 ; ,
Distance matrix 7 Initial Pheromone level matrix
A |B |]C|]D A/B/C |D
AlO |3 [9 | 7 AJO }]1l Ji] 1
B]| 3 0,115 “T7B 1,0 Jt Jd
cj}9 Ji jo f2 c}i }1 jo }i
D|-7 5 {2 10 Dil {14140
a Compare Genetic Algorithm with Genetic Programming Algorithm with the
04 help of suitable flow chart.
cO-4: State and explain the five preparatory steps of Genetic Programming to 110]
SO-1; automatically create a computer program whose output is equal to the
BL-2,4 ;

quadratic equation x? + 2x + 1 in the range of {-1,1}.
--- page 4 ---
b Consider the fitness function f(x) = x? +10 and a population of three.
individuals {a, b,c}. When decoded their genes give the values are
x = {1,2,3} respectively. If Fitness Proportionate Selection algorithm is to
be applied, determine the selection probability all the individuals? If the
cO-4; fitness function is changed to f(x) = x? +100 and f(x) = x? + 1000,

SO-1; ;
BL-3,4,5 what will be the change in selection probability? With reference to the

[10]

above example, explain how fitness proportionate algorithm suffers from
“High susceptibility to function transposition”. Discuss how Rank based
selection algorithm can overcome drawbacks of fitness proportionate .

selection algorithm. ,

a Consider the problem to minimizef (x1, X2) = 100(x — X)* where
<5 <x4,x2 <5. Apply Particle Swarm Optimization to
i. Determine fitness of the given first. generation
ji. Identify local best of each particle of the first generation and
identify the global best of swarm
iii. | Update velocity, position only for the first particle of the second
generation ; .
iv. Evaluate fitness of the updated first particle of the second
Q5 generation and deduce the local best for the same.
CO-3; The initial position and velocity of the first generation are as given in the [10]
S0-1,6; table below-

BL-4,5
be .| Index(i) XO VQ
1 (2.212, 3.009) (0.0,0.0)
2 (-2.289, -2.396) (0.0,0.0)
3 (-2.393, -4.790) (0.0,0.0)
4 (-0.639,1.692) (0.0,0.0)
5 (-3.168,0.706) (0.0,0.0)

Take inertia weight w, = 0.75, correction factors cy = 1.5 and cz = 2.

Random numbers.for the first particle are given below-

Particle | ‘rl 12
1 0.661 0.312
--- page 5 ---
i

b State the significance of using Differential Evolution approach for problem

solving. With the help of suitable diagram and expressions, explain the

Co- 43 following steps in Differential Evolution Algorithm
SO-1; i Initialization te [10]
BL-2 ‘

ii Mutation
iii Recombination.

iv Selection

06 _|a-~ Explain withthe help of a pseudocode Ant System Algorithm. Elaborate on
CO-3: the variations that are implemented in Max-Min Ant System Algorithm and [10]
-| SO-1; the key differences between Ant System Algorithm and Max Min
Ble ; Algorithm.
CO-1.4: b List the popular variants of Evolutionary Algorithm.
SO-1; - | Demonstrate the steps in “Two membered “Evolutionary Strategy [10]
BL-2 Bae. ; ;
algorithm.
Q7 a Write a short note on — :
_ / i. Michigan and Pittsburgh approaches for Learning Classifier ;
CO-4,2; aa [10]
.| SO-1; . Systems . ;
BL-2 om Serer .
ii. | Recombination in Real-Valued Representation —
b Discuss generalized framework of Particle Swarm Optimization algorithm.
In particular, explain the following terms with the help of suitable
CO-3; equation/s ;
SO-1; : [10]
BL-2 i. Local best position of each particle

ii. Global best position of swarm.

iii, Velocity update and particle position update
````
