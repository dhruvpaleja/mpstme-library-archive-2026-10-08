# Evolutionary Computing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper db7b0ccbfc15

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Evolutionary Computing/ANS_Evolutionary Computing(702AI0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (25 pages), mean OCR confidence 78.1
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Evolutionary Computing
Date: 02 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 25 pages.
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
This representation can be used in the domains where gene comes from
continuous rather than discrete domain. Example- Financial model tuning,
optimizing neural network weights, engineering design parameters-weight,
length, speed, pressure.
********** 1 **********

[Text in pictures on this page, read by OCR]
Uniform mutation
a

Oo Uniform mutation

0 For this operator the values of x;’ are drawn uniformly
randomly from [L;, U;]

O This is the most straightforward option, analogous to bit-
flipping for binary encodings and the random resetting for
integer encodings

Olt is normally used with a positionwise mutation probability
--- page 2 ---
b
CO-2 ;   With reference to survivor selection mechanism, discuss fitness based, age-
SO-1 ;   based replacement techniques with the help of suitable examples.
BL-2
c
CO-4 ;
Explain Bloat and Over Selection concept in Genetic Programming
SO- 1;
BL-3
********** 2 **********

[Text in pictures on this page, read by OCR]
Recombination of real valued

representation
a

Oo We have three options for recombining two floating-point strings

oO First Method- using an analogous operator to those used for bit-strings, but
now split between floats
oO In other words, an allele is one floating-point value instead of one bit

O This has the disadvantage (shared with all.of the recombination operators
described above) that only mutation can insert new values into the population,
since recombination only gives us new combinations of existing values

© Recombination operators of this type for floating-point representations are
known as discrete recombination and have the property that if we are creating
an offspring z from parents x and y, then the allele value for gene i is given by

= Z = X; Or y; with equal likelihood.

Fitness Based Selection
ee

ao Children replace the least
fit individuals P1 and P10
of the population

a Since P1 and P9 have the
same fitness value, ‘ste ‘one

3) | _a

Oo the decision to remove 2 ‘anes Cvomesome fe] i
which individual from the a a = es
population is arbitrary fay | Ee —

| 78 oFFsPRINGS I] 8

—-
[eo] cy [s] a
--- page 3 ---
d
Write the algorithm for Elitist Ant System Algorithm. Identify the key
CO-3 ;
features that differentiate the Elitist Ant System from Ant System
SO-1 ;
Algorithm
BL- 2
********** 3 **********

[Text in pictures on this page, read by OCR]
Bloat in Genetic Programming
|
0 A special effect of varying chromosome sizes in GP is that these tend to grow during a GP run

© That is, without appropriate countermeasures the average tree size is growing during the search
process

© This phenomenon is known as bloat (sometimes called the "survival of the fattest")

The simplest way to prevent bloat is to introduce a maximum tree size and forbid a variation
operator if the child(ren) resulting from its application would exceed this maximum size

a In this case, this threshold can be seen as an additional parameter of mutation and recombination in
GP.

© One technique that is widely acknowledged is that of parsimony pressure

Such a pressure towards parsimony (i.e., being "stingy" or ungenerous) is achieved through

© introducing a penalty term in the fitness formula that reduces the fitness of large chromosomes or using multi-
objective techniques.

Over selection
a

a Over-selection is often used to deal with the typically large population sizes
0 (population sizes of several thousands are not unusual in GP)
a The method first ranks the population, then divides it into two groups,
© one containing the top x% and
oO the other containing the other (100 — x)%
a When parents are selected,
5 80% of the selection operations come from the first group, and
othe other 20% from the second group

a The values of x used are found empirically by rule of thumb and depend
on the population size with the aim that the number of individuals from
which the.majority.of parents are chosen stays constant in the low hundreds,
i.e., the selection pressure increases dramatically for larger populations

Elitist Ant System

Ty (t-+ 1) = pry (+ Ory + Ary @)

m = if ant k travels on edge (i,j)
where Any => Arf and Ari =

© otherwise

as before,

of if edge (i, j) is part of the best solution found so far

and Ary, =
o otherwise

where

Ary, increase of trail level on edge (i, j) caused by the elitist ants
o number of elitist ants
L* tour length of best solution found so far

Concerning the number of elitist ants we found that the results of the
ant system are very good for o = n = m, i.e. when there are as many elitist
ants used as there are cities in the problem.

Summary of Key Differences

Feature Ant System (AS) Elitist Ant System (EAS)

Pheromone Update All ants contribute equally Extra reinforcement to the best solution
Convergence Speed Slower Faster

Risk of Premature Convergence Lower Higher

Solution Diversity More exploration More exploitation
--- page 4 ---
a   Discuss drawbacks of partially mapped crossover technique for
permutation representation. [2 Marks]
Consider the following two parents with permutation representation.
Parent 1: [9 5 6 1 3 7 8 4 2]
Parent 2: [5 6 4 1 8 3 2 9 7]
Q2
i.   Apply cycle crossover on the two-parent chromosome to obtain two
CO-2;
offsprings [3 Marks]   [10]
SO-1;
ii. On the offsprings obtained after cycle crossover, apply swap
BL-2,3
mutation on both the offsprings. Swap allele of position 3 and 6.
[1 Marks]
iii.   Apply order crossover on the two chromosomes to obtain two
offsprings. Take the cross over points as 2 and 6. [3 Marks]
iv.   For the offspring 1 obtained after order crossover, apply inversion
mutation on offspring 1 between points 2 and 5 [1 Marks]
********** 4 **********

[Text in pictures on this page, read by OCR]
Drawbacks of PMX

oO Limited Exploration (Low Diversity)
PMX preserves many positional relationships from the parents. While this helps keep
good structures, it can reduce population diversity and increase the risk of
premature convergence

oO Disrupts Useful Order Information
PMX focuses on position-based mapping, not relative order. For problems where the
order of elements matters more than exact positions, PMX may destroy good
building blocks.

co Computational Overhead
Compared to simpler crossovers, PMX requires:
© Mapping creation

© Conflict resolution
This makes it slower and more complex to implement, especially for large permutations
--- page 5 ---
CO-2   b
Explain genitor survivor selection technique and elitism survivor selection
SO-1;   [05]
technique with suitable example. [2.5 Marks each]
BL-2
********** 5 **********

[Text in pictures on this page, read by OCR]
Replace worst (Genitor)

c In this scheme the worst \ members of the population are
selected for replacement

0 This can lead to very rapid improvements in the mean
population fitness

co However it can also lead to premature convergence as the
population tends to rapidly focus on the fittest member
currently present

O For this reason it is commonly used in conjunction with large
populations and/or a “no duplicates” policy
--- page 6 ---
CO-4   c   With the help of suitable block diagram, explain the steps in Genetic
SO-1;   Programming Algorithm. [2.5Marks +2.5 Marks]   [05]
BL-2
One-two lines on each step
Q3   a   [10]
********** 6 **********

[Text in pictures on this page, read by OCR]
Elitism
ee
O This scheme is commonly used in conjunction with age-based

and stochastic fitness-based replacement schemes

O This is done to prevent the loss of the current fittest member
of the population

Oo In essence a trace is kept of the current fittest member, and
it is always kept in the population

O Thus if it is chosen in the group to be replaced, and none of
the offspring being inserted into the population has equal or
better fitness than the current fittest member, then it is kept
and one of the offspring is discarded

eS
next < i = population size ?
generation <-—_————_

Vino

select variation op.
probabilistically

with p_ ge with p

select one select two
individual individuals
perform mutation perform crossover
en Ae v
add offspring to add offspring to
intermediate poo! intermediate pool
i=i-+] i=i+2
--- page 7 ---
CO-3;
SO-1
BL-4,5
Consider the problem to Maximize 𝑓(𝑥) = 2𝑥1 2 −2𝑥1𝑥2 + 𝑥2 2 where
−4 ≤𝑥1, 𝑥2 ≤4 . Apply Particle Swarm Optimization to-
i.   Determine fitness of the initial population [2.5Marks]
ii.   Identify local best of each particle of the first generation and
identify the global best of the swarm [[2.5Marks]
iii.   Update velocity, position only for the first particle of the second
generation [3 Marks]
iv.   Evaluate fitness of the updated first particle and identify the local
best for the same. [2Marks]
The initial position and velocity are as given in the table below-
Index(i)   Xi(1)   Vi(1)
1   (2,3)   (0.0,0.0)
2   (-2,1)   (0.0,0.0)
3   (0,-3)   (0.0,0.0)
4   (4,-1)   (0.0,0.0)
5   (-1,2)   (0.0,0.0)
Take inertia weight 𝑤𝑡= 0.65, correction factors 𝑐1 = 2 𝑎𝑛𝑑 𝑐2 = 2.
Random numbers for the first particle are given below-
Particle   r1   r2
1   0.6   0.3
********** 7 **********
--- page 8 ---
Uv
\ ;
pporiignk oe PON
i co vw!
] » bus \w 4 =
GH) eae ie (a =
Apww
C 2 9b) A= ta Be O\= 0°6 O2=903
a ghut = (%» Soe * (4)-\) 4 ;
: 2 ogo XO4F 2% g6 [2-2] + 2034 -2]
Shr

i q_
Oi = Be 49 Wyre +c) (ti, - Hin. | + Orn (> an)

= yocxot 2x04 (3-3) + 2x03 (-\ -3)

2£-2-U>

a

[v= (Vey? '4 )

| pontter wel
ms aut UN

= 24025 3°>
= ~-ouzo'é
mr = Mle vir = 3 4

vw pmb = ( 32, 06 )

Siren wh rw pmkoe pit”

FIC QF EH 1
--- page 9 ---
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
********** 9 **********
--- page 10 ---
c   Consider a chromosome 𝑋= [1.2,3.0,4.5, −1]. The allowed range for each
CO-2
gene is [−1.0, 5.0]. Let the mutation probability 𝑝𝑚= 0.3. For each gene
SO-1   [05]
the random number generated is [0.25, 0.4, 0.15, 0.5]. Apply creep
BL-3,4
mutation to obtain the offspring. Let creep value ∆= 0.7.
Q4   a
CO-3   Discuss general principles of swarm intelligence [2.5Marks]. State main
[05]
SO-1   reasons for success of a swarm. [2.5Marks]
BL-2
********** 10 **********
--- page 11 ---
CO-1   b   Sketch a suitable flow diagram for evolutionary algorithm [2Marks] and
SO-1   explain the following components in brief- Population, Fitness, Parent   [05]
BL-2   Selection. [3Marks]
********** 11 **********

[Text in pictures on this page, read by OCR]
General Principles of Swarm Intelligence
ee
a Proximity principle
© Basic units of a swarm should be capable of simple computation
related to its surrounding environment

© Here computation is regarded as a direct behavioral response to
environmental variance, such as those triggered by interactions
among agents

o Depending on the complexity of agents involved, responses may
vary greatly

& However, some fundamental behaviors are shared, such as living-
resource searching and nest building

Oo Principle of diverse response
in narrow region
The distribution should be designed so that each agent will
be maximally protected facing environmental fluctuations
oO Principle of stability and adaptability
Swarms are expected to
without rapidly changing modes since mode changing costs
energy
--- page 12 ---
) ) Parent selection Parents |

Recombination

Mutation

4

I ' ti : __ offs =

urvivor selection

Fig. 3.2. The general scheme of an evolutionary algorithm as a flowchart

Evaluation Function or Fitness Function

a Role of the evaluation function is

© to represent the requirements the population should adapt to meet
a It forms the basis for selection, and so it facilitates improvements
a It defines what improvement means

oO From the problem-solving perspective, it represents the fask to be
solved in the evolutionary context

a Technically, it is a function or procedure that assigns a quality
measure to genotypes

°
Population

SSCS
a The role of the population is to hold (the representation of) possible solutions

oO A population is a multiset of genotypes

a The population forms the unit of evolution

Oo Individuals are static objects that do not change or adapt; it is the population that
does

o Given a representation, defining a population may be as simple as specifying how
many individuals are in it, that is, setting the population size

oO Best individual of a given population is chosen to seed the next generation
oO Worst individual of a given population is chosen to be replaced by a new one
oO Diversity of a population is a measure of the number of different solutions present

© No single measure for diversity exists

oO Diversity measure might be different fitness values, number of phenotypes, number of
genotypes, entropy

FRR ICR] DA KH
--- page 13 ---
c   Consider a problem where we must minimize the function where
𝑓(𝑥) = 𝑥3 −4
Single parent in the population 𝑥= 3
Initial variation 𝜎= 1
Let the random numbers taken from the normal distribution for mutation
are
CO-4
SO-1   𝑧𝑖= [0.8, −0.2, 0.2, 0.5, −0.4]
[10]
BL-4,5   [2.5Marks each]
i.   Using two membered evolutionary strategy algorithm, generate five
off springs from parent given above.
ii.   Compute fitness of parent and off springs
iii.   Evaluate new 𝜎 based on 1/5 success rule
iv.   State your inference about 𝜎 obtained in (iii) above
********** 13 **********

[Text in pictures on this page, read by OCR]
Parent Selection Mechanism

QO The role of parent selection or mate selection is to distinguish among individuals based on their
quality

2 To allow the better individuals to become parents of the next generation

OQ An individual is a parent if it has been selected to undergo variation in order. to create
offspring

O Together with the survivor selection mechanism, parent selection is responsible for pushing
quality improvements

og In EC, parent selection is typically probabilistic
0 Means high-quality individuals have more chance of becoming parents than those with low quality

O Nevertheless, low-quality individuals are often given a small, but positive chance

0 otherwise the whole search could become too greedy and the population could get stuck in a local
optimum

Since £) = 3anda = 1:

Zi Offspring z; = 3+ 2;
0.8 3.8
-0.2 2.8
0.2 3.2
0.5 3.5

-0.4 2.6
--- page 14 ---
Parent

f(3) =3? —4=27-4=23

Offspring

Offspring f(z)=2-4 Success? (Minimize)
3.8 54.872 — 4 = 50.872 No

28 21.952 — 4 = 17.952 Yes

3.2 32.768 — 4 = 28.768 No

3.5 42.875 — 4 = 38.875 No

2.6 17.576 — 4 = 13.576 Yes

(iii) Evaluate new o using 1/5 success rule

Success rate

2
P,=2=04
5
1/5 rule:
e If P, > 1/5 - Increase o
e If. P, < 1/5 - Decrease o
e If P, = 1/5 — Keep o same
Since
0.4 > 0.2

(iv) Inference

Since the success rate is higher than 1/5:
e Step size (0) is too small
¢ Algorithm is progressing well
e Increase o to explore faster and improve convergence

Qs a Consider a problem statement to minimize f(x) = x, — 2x2 + x3 where

CO-4 x; € [-8,8].

B23 Individual 1 | Individual 2 Individual 3 | Individual 4 [10]
xy -1 2 -5 -4

FRR IC 7 I OH
--- page 15 ---
𝑥2.   5   -3   1   -2
𝑥3.   3   1   3   1
Here population size 𝑁= 4, number of parameters 𝐷= 3, Crossover rate
𝐶𝑅= 0.5, Mutation factor 𝐹= 0.7, Random integer for recombination step
𝐼𝑟𝑎𝑛𝑑= 2,
Random number for selection of each element during recombination step =
[0.6, 0.8, 0.95]
[2.5 Marks each]
Apply Differential Evolution Algorithm to-
i.   Generate weighted difference vector using Individual 3 and
Individual 4.
ii.   Generate the noisy vector using Individual 1 and the weighted
difference vector.
iii.   Construct trial vector using Individual 2 as parent and the noisy
vector
iv.   Evaluate fitness of parent vector and offspring vector. State your
inference.
********** 15 **********
--- page 16 ---
b   Consider 4 Cities A, B, C, D to be travelled by the ant, starting at City A.
The ant should return back to City A after covering all the cities.
The distance matrix is given as:
CO-3   A   B   C   D
SO-1   A   0   5   2   7
[10]
BL-4   B   4   0   1   8
C   2   2   0   7
D   7   9   2   0
The Pheromone Matrix is:
********** 16 **********
--- page 17 ---
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
[2.5 Marks each]
********** 17 **********

[Text in pictures on this page, read by OCR]
Py = ( Cu)” )
ij = a B
Z(t) (nis)
Where 1j,; = = ,L, jis the length of edge Gj)

aand B control the relative importance of
pheromone versus the heuristic information nj ;
k
Ty = (1 = ptay + Lhe AT;
Atijis the quantity of pheromone laid on edge (i, j) by ant k

Qa. eye
b ack, = Tel ant k used edge (i,j)in its tour
0, otherwise

1 Where @ is a constant, generally Q=1 and Ly is length of tour constructed by ant k

Sum
0.2 + 0.5 + 0.1429 = 0.8429
Probabilities
Pap = 0.2/0.8429 = 0.237
Pac = 0.5/0.8429 = 0.593

Pap = 0.1429/0.8429 = 0.169
--- page 18 ---
(iii) Pheromone Update
Path taken:

A~C+-B-D-A

Distances:
e A-C=2
e C-B=2
e B-D=8
e D-A=7
Total length:

D=2+2+8+7=19

Pheromone addition:

Evaporation rate:

p=0.7
Update rule:

Trew = (1 — p) Toa + At
(1— p) =0.3
Visited edges:
0.3(1) + 0.0526 = 0.3526

Non-visited edges:

0.3(1) = 0.3
Updated Pheromone Matrix
A B c D
A 0 03 0.3526 0.3526
B 03 0 0.3526 0.3526
c 0.3526 0.3526 0 03
D 0.3526 0.3526 03 0

FR ICR 7] QA HH
--- page 19 ---
a   With the help of suitable pseudocode, demonstrate the steps in Tournament
Selection Algorithm.
Consider the following objective function which has to be minimized.
𝑓(𝑥) = 𝑥1 2 −𝑥2 + 2𝑥3
The solutions in the initial population are given below.
Individual   A   B   C   D
Q6   Genotype   [2,3,5]   [1,2,3]   [3,1,2]   [2,5,6]
CO-2   [2.5 Marks each]
SO-1   [10]
BL-3,5   Using genetic algorithm approach, answer the following-
i.   Implement tournament selection rounds to select two parents as
follows
1st Tournament between individuals A and D
2nd Tournament between individuals B and C
ii.   Use one point crossover between the winner parents from step (i).
Take crossover point as 2.
iii.   Evaluate fitness of the two offspring
********** 19 **********

[Text in pictures on this page, read by OCR]
(iv) Effect of Evaporation Rate (p)

e High p = Fast evaporation — More exploration
e Low p - Slow evaporation — Strong exploitation

e Proper p balances exploration vs exploitation

Inference:

p = 0.7 gives high exploration and avoids premature convergence.

BEGIN
/* Assume we wish to select \ members of a pool of y individuals
set current_member = 1;
WHILE ( current-member <X ) DO
Pick k individuals randomly, with or without replacement;
Compare these k individuals and select the best of them;
Denote this individual as i;
set mating_pool[current_-member] = i;
set current_member = current_-member + 1;
oD
END

*/

Fig. 5.3. Pseudocode for the tournament selection algorithm
--- page 20 ---
Step 1: Evaluate Fitness of Initial Population
Individual A [2,3,5]

f(A) = 2? -342(5) =4-34+10=11
Individual B [1,2,3]

f(B) = —24+2(3)=1-2+6=5
Individual C [3,1,2]

f(C) =3? -14+2(2)=9-14+4=12
Individual D [2,5,6]

f(D) =2?-54+2(6) =4-5412=11
(i) Tournament Selection

1st Tournament: A vs D

A=11
D=11

Tie — choose any (choose A)

Winner1=A

2nd Tournament: B vs C

B=5
C=12
Winner 2 = B

Selected Parents

Parent 1 = A = [2,3,5]
Parent 2 = B = [1,2,3]

FRI ICR DO) A RH
--- page 21 ---
b   Consider the following problem. You have a knapsack of capacity 13kg, and
you must choose from the following six items, maximizing total value while
keeping the total weight ≤ 13 kg. Each item can be either included (1) or not
included (0) in the knapsack.
Item   Weight (kg)   Value
P   2   3
Q   3   4
R   4   5
S   5   8
CO-1   T   6   9
SO-1   U   7   10   [10]
BL-2, 4
i   Create two parent chromosomes of length 6 each by selecting items
[P,Q,T] in chromosome 1 and items [Q, R, S] in chromosome 2
[2Marks]
ii Compute two off springs using Uniform cross over with p=0.5
where the random number for each gene is [0.3, 0.2, 0.4, 0.6, 0.1,
0.8] [2.5Marks]
iii Perform mutation by flipping bits 1,3,5 in offspring 1 and 2,4,6 in
offspring 2 [2.5Marks]
iv   Calculate fitness of each offspring and comment on the same
[3Marks]
********** 21 **********

[Text in pictures on this page, read by OCR]
(ii) One-Point Crossover

Crossover point = 2

Parent 1: [2 3 | 5]
Parent 2: [1 2 | 3]
Offspring

Offspring 1 = [2,3,3]
Offspring 2 = [1,2,5]

(iii) Fitness of Offspring
Offspring 1 [2,3,3]

f =2?-342(3)=4-3+6=7
Offspring 2 [1,2,5]

f=V-—242(5)=1-24+10=9
--- page 22 ---
Mutated Offspring 1 represents a successful, feasible solution that respects
the constraints of the knapsack problem, yielding a good fitness score of 17.
Mutated Offspring 2 is an infeasible solution because it violates the 13 kg
weight limit constraint, meaning it cannot be used and effectively has a
fitness of 0 in standard genetic algorithm constraint handling.
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
********** 22 **********

[Text in pictures on this page, read by OCR]
Mutated Offspring 1: [@, 1, 1, 1, @, @] (Contains items Q, R, S)
¢ Total Weight = 3kg + 4kg + 5kg = 12 kg
e Total Value=4+5+8=17

e Evaluation: Since 12 kg < 13 kg, this is a valid solution. Fitness = 17.

Mutated Offspring 2: [@, @, 1, 1, , 1] (Contains items R, S, U)
¢ Total Weight = 4kg + 5kg + 7kg = 16 kg
¢ Total Value = 5 +8+10=23

¢ Evaluation: Since 16 kg > 13 kg, the weight exceeds the maximum capacity constraint.
Fitness = 0 (infeasible).
--- page 23 ---
b   State the factors on which flow of information depends upon through a
CO-3   Social Structure. Discuss with the help of suitable diagram Star Social
SO-1   Structure, Ring Social Structure, Wheel Social Structure and Von
[10]
BL-2   Neumann Social Structure with reference to network topologies in Particle
Swarm Optimization
********** 23 **********

[Text in pictures on this page, read by OCR]
Rank based Ant System Algorithm
AS+ank

3 Update of Pheromone Trails

5 Before updating the pheromone trails, the ants are sorted by increasing tour length and the quantity of pheromone an ant deposits is weighted
according to the rank r of the ant

5 Ties can be solved randomly (in our implementation they are solved by lexicographic ordering on the ant name k)

5 In each iteration only the (W — 1) bestranked ants and the ant that produced the best-so-far tour (this ant does not necessarily belong to the set
of ants of the current algorithm iteration) are allowed to deposit pheromone

© The best-so-far tour gives the strongest feedback, with weight w
= (Le, its contribution 1/Cps is multiplied by w),
o iy Tth best ant of the current iteration contributes to pheromone updating with the value 1/Cr multiplied by a weight given by max{0, w —
r}.

© Thus, the AS;ank pheromone update rule is, 1
we

y+ —r)At;, + wr},

o In AS+ank

each ant deposits an amount of pheromone that decreases
with its rank

the best-so-far ant always deposits the largest amount of
pheromone in each iteration

Feature Ant System (AS) Rank-Based Ant System (RBAS)

Pheromone Update All ants update pheromone Only top-ranked ants update
pheromone

Solution Contribution Every ant contributes equally Better ants contribute more

Convergence Speed Slower convergence Faster convergence

Solution Quality May converge to suboptimal Usually better solution quality
solution

Computational Efficiency Less efficient More efficient

Selection Strategy No ranking mechanism Uses ranking of ants

Exploitation vs Exploration More exploration More exploitation of best

solutions
--- page 24 ---
Social Network Structures

|
Oo Within the PSO, particles in the same neighborhood communicate with one
another by exchanging information about the success of each particle in
that neighborhood

oO AIl particles then move towards some quantification of what is believed to
be a better position

oO The performance of the PSO depends strongly on the structure of the social
network

0 The flow of information through a social network, depends on
© (1) the degree of connectivity among nodes (members) of the network,

© (2) the amount of clustering (clustering occurs when a node’s neighbors are also
neighbors to one another), and

a (3) the average shortest distance from one node to another

Various kinds of social network structures
es

O Star social structure
© All particles are interconnected

5 Each particle can therefore communicate with every
other particle

o In this case each particle is attracted towards the best
solution found by the entire swarm

5 Each particle therefore imitates the overall best
solution

othe first implementation of the PSO used a star
network structure, with the resulting algorithm
generally being referred to as the gbest PSO

© The gbest PSO has been shown to converge faster
than other network structures, but with a susceptibility
to be trapped in local minima

The gbest PSO performs best for unimodal problems (a) Star

Various kinds of social network structures
2 eee

0 Ring social structure
5 Each particle communicates with its nV immediate neighbors

5 Inthe case of nN = 2,4 particle communicates with its
immediately adjacent neighbors

5 Each particle attempts to imitate its best neighbor by moving
closer to the best solution found within the neighborhood

5 Its Important to note that neighborhoods overlap

5 This facilitates the exchange of information between
neighborhoods and, in the end, convergence to a single solution

5 Since information flows at a slower rate through the social network,
convergence is slower, but larger parts of the search space are
covered compared to the star structure

3 This behavior allows the ring structure to provide better
performance in terms of the quality of solutions found for multi-
modal problems than the star structure

3 Resulting PSO algorithm is generally referred to as the Ibest PSO
(b) Ring

Various kinds of social network structures
ee

a Wheel social structure

© Individuals in a neighborhood are isolated from
one another

© One particle serves as the focal point, and all
information is communicated through the focal
particle

O Focal particle compares the performances of all
particles in the neighborhood, and adjusts its
position towards the best neighbor

© If the new position of the focal particle results in
better performance, then the improvement is
communicated to all the members of the
neighborhood

Gc Wheel social network slows down the propagation (c) Wheel
of good solutions through the swarm

FRR IRD AC HOH
--- page 25 ---
Various kinds of social network structures

O The Von Neumann social
structure

© Particles are connected
in a grid structure

© The Von Neumann social
network has been shown >
in a.number.of empirical
studies to outperform
other social networks in
a.large number. of
problems

(8) Von Neumann,

FI ICR AC KH
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 119a064209b1

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/Evolutionary Computing/ANS_Evolutionary Computing(702AI0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (25 pages), mean OCR confidence 78.1
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Evolutionary Computing
Date: 02 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 25 pages.
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
This representation can be used in the domains where gene comes from
continuous rather than discrete domain. Example- Financial model tuning,
optimizing neural network weights, engineering design parameters-weight,
length, speed, pressure.
********** 1 **********

[Text in pictures on this page, read by OCR]
Uniform mutation
a

Oo Uniform mutation

0 For this operator the values of x;’ are drawn uniformly
randomly from [L;, U;]

O This is the most straightforward option, analogous to bit-
flipping for binary encodings and the random resetting for
integer encodings

Olt is normally used with a positionwise mutation probability
--- page 2 ---
b
CO-2 ;   With reference to survivor selection mechanism, discuss fitness based, age-
SO-1 ;   based replacement techniques with the help of suitable examples.
BL-2
c
CO-4 ;
Explain Bloat and Over Selection concept in Genetic Programming
SO- 1;
BL-3
********** 2 **********

[Text in pictures on this page, read by OCR]
Recombination of real valued

representation
a

Oo We have three options for recombining two floating-point strings

oO First Method- using an analogous operator to those used for bit-strings, but
now split between floats
oO In other words, an allele is one floating-point value instead of one bit

O This has the disadvantage (shared with all.of the recombination operators
described above) that only mutation can insert new values into the population,
since recombination only gives us new combinations of existing values

© Recombination operators of this type for floating-point representations are
known as discrete recombination and have the property that if we are creating
an offspring z from parents x and y, then the allele value for gene i is given by

= Z = X; Or y; with equal likelihood.

Fitness Based Selection
ee

ao Children replace the least
fit individuals P1 and P10
of the population

a Since P1 and P9 have the
same fitness value, ‘ste ‘one

3) | _a

Oo the decision to remove 2 ‘anes Cvomesome fe] i
which individual from the a a = es
population is arbitrary fay | Ee —

| 78 oFFsPRINGS I] 8

—-
[eo] cy [s] a
--- page 3 ---
d
Write the algorithm for Elitist Ant System Algorithm. Identify the key
CO-3 ;
features that differentiate the Elitist Ant System from Ant System
SO-1 ;
Algorithm
BL- 2
********** 3 **********

[Text in pictures on this page, read by OCR]
Bloat in Genetic Programming
|
0 A special effect of varying chromosome sizes in GP is that these tend to grow during a GP run

© That is, without appropriate countermeasures the average tree size is growing during the search
process

© This phenomenon is known as bloat (sometimes called the "survival of the fattest")

The simplest way to prevent bloat is to introduce a maximum tree size and forbid a variation
operator if the child(ren) resulting from its application would exceed this maximum size

a In this case, this threshold can be seen as an additional parameter of mutation and recombination in
GP.

© One technique that is widely acknowledged is that of parsimony pressure

Such a pressure towards parsimony (i.e., being "stingy" or ungenerous) is achieved through

© introducing a penalty term in the fitness formula that reduces the fitness of large chromosomes or using multi-
objective techniques.

Over selection
a

a Over-selection is often used to deal with the typically large population sizes
0 (population sizes of several thousands are not unusual in GP)
a The method first ranks the population, then divides it into two groups,
© one containing the top x% and
oO the other containing the other (100 — x)%
a When parents are selected,
5 80% of the selection operations come from the first group, and
othe other 20% from the second group

a The values of x used are found empirically by rule of thumb and depend
on the population size with the aim that the number of individuals from
which the.majority.of parents are chosen stays constant in the low hundreds,
i.e., the selection pressure increases dramatically for larger populations

Elitist Ant System

Ty (t-+ 1) = pry (+ Ory + Ary @)

m = if ant k travels on edge (i,j)
where Any => Arf and Ari =

© otherwise

as before,

of if edge (i, j) is part of the best solution found so far

and Ary, =
o otherwise

where

Ary, increase of trail level on edge (i, j) caused by the elitist ants
o number of elitist ants
L* tour length of best solution found so far

Concerning the number of elitist ants we found that the results of the
ant system are very good for o = n = m, i.e. when there are as many elitist
ants used as there are cities in the problem.

Summary of Key Differences

Feature Ant System (AS) Elitist Ant System (EAS)

Pheromone Update All ants contribute equally Extra reinforcement to the best solution
Convergence Speed Slower Faster

Risk of Premature Convergence Lower Higher

Solution Diversity More exploration More exploitation
--- page 4 ---
a   Discuss drawbacks of partially mapped crossover technique for
permutation representation. [2 Marks]
Consider the following two parents with permutation representation.
Parent 1: [9 5 6 1 3 7 8 4 2]
Parent 2: [5 6 4 1 8 3 2 9 7]
Q2
i.   Apply cycle crossover on the two-parent chromosome to obtain two
CO-2;
offsprings [3 Marks]   [10]
SO-1;
ii. On the offsprings obtained after cycle crossover, apply swap
BL-2,3
mutation on both the offsprings. Swap allele of position 3 and 6.
[1 Marks]
iii.   Apply order crossover on the two chromosomes to obtain two
offsprings. Take the cross over points as 2 and 6. [3 Marks]
iv.   For the offspring 1 obtained after order crossover, apply inversion
mutation on offspring 1 between points 2 and 5 [1 Marks]
********** 4 **********

[Text in pictures on this page, read by OCR]
Drawbacks of PMX

oO Limited Exploration (Low Diversity)
PMX preserves many positional relationships from the parents. While this helps keep
good structures, it can reduce population diversity and increase the risk of
premature convergence

oO Disrupts Useful Order Information
PMX focuses on position-based mapping, not relative order. For problems where the
order of elements matters more than exact positions, PMX may destroy good
building blocks.

co Computational Overhead
Compared to simpler crossovers, PMX requires:
© Mapping creation

© Conflict resolution
This makes it slower and more complex to implement, especially for large permutations
--- page 5 ---
CO-2   b
Explain genitor survivor selection technique and elitism survivor selection
SO-1;   [05]
technique with suitable example. [2.5 Marks each]
BL-2
********** 5 **********

[Text in pictures on this page, read by OCR]
Replace worst (Genitor)

c In this scheme the worst \ members of the population are
selected for replacement

0 This can lead to very rapid improvements in the mean
population fitness

co However it can also lead to premature convergence as the
population tends to rapidly focus on the fittest member
currently present

O For this reason it is commonly used in conjunction with large
populations and/or a “no duplicates” policy
--- page 6 ---
CO-4   c   With the help of suitable block diagram, explain the steps in Genetic
SO-1;   Programming Algorithm. [2.5Marks +2.5 Marks]   [05]
BL-2
One-two lines on each step
Q3   a   [10]
********** 6 **********

[Text in pictures on this page, read by OCR]
Elitism
ee
O This scheme is commonly used in conjunction with age-based

and stochastic fitness-based replacement schemes

O This is done to prevent the loss of the current fittest member
of the population

Oo In essence a trace is kept of the current fittest member, and
it is always kept in the population

O Thus if it is chosen in the group to be replaced, and none of
the offspring being inserted into the population has equal or
better fitness than the current fittest member, then it is kept
and one of the offspring is discarded

eS
next < i = population size ?
generation <-—_————_

Vino

select variation op.
probabilistically

with p_ ge with p

select one select two
individual individuals
perform mutation perform crossover
en Ae v
add offspring to add offspring to
intermediate poo! intermediate pool
i=i-+] i=i+2
--- page 7 ---
CO-3;
SO-1
BL-4,5
Consider the problem to Maximize 𝑓(𝑥) = 2𝑥1 2 −2𝑥1𝑥2 + 𝑥2 2 where
−4 ≤𝑥1, 𝑥2 ≤4 . Apply Particle Swarm Optimization to-
i.   Determine fitness of the initial population [2.5Marks]
ii.   Identify local best of each particle of the first generation and
identify the global best of the swarm [[2.5Marks]
iii.   Update velocity, position only for the first particle of the second
generation [3 Marks]
iv.   Evaluate fitness of the updated first particle and identify the local
best for the same. [2Marks]
The initial position and velocity are as given in the table below-
Index(i)   Xi(1)   Vi(1)
1   (2,3)   (0.0,0.0)
2   (-2,1)   (0.0,0.0)
3   (0,-3)   (0.0,0.0)
4   (4,-1)   (0.0,0.0)
5   (-1,2)   (0.0,0.0)
Take inertia weight 𝑤𝑡= 0.65, correction factors 𝑐1 = 2 𝑎𝑛𝑑 𝑐2 = 2.
Random numbers for the first particle are given below-
Particle   r1   r2
1   0.6   0.3
********** 7 **********
--- page 8 ---
Uv
\ ;
pporiignk oe PON
i co vw!
] » bus \w 4 =
GH) eae ie (a =
Apww
C 2 9b) A= ta Be O\= 0°6 O2=903
a ghut = (%» Soe * (4)-\) 4 ;
: 2 ogo XO4F 2% g6 [2-2] + 2034 -2]
Shr

i q_
Oi = Be 49 Wyre +c) (ti, - Hin. | + Orn (> an)

= yocxot 2x04 (3-3) + 2x03 (-\ -3)

2£-2-U>

a

[v= (Vey? '4 )

| pontter wel
ms aut UN

= 24025 3°>
= ~-ouzo'é
mr = Mle vir = 3 4

vw pmb = ( 32, 06 )

Siren wh rw pmkoe pit”

FIC QF EH 1
--- page 9 ---
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
********** 9 **********
--- page 10 ---
c   Consider a chromosome 𝑋= [1.2,3.0,4.5, −1]. The allowed range for each
CO-2
gene is [−1.0, 5.0]. Let the mutation probability 𝑝𝑚= 0.3. For each gene
SO-1   [05]
the random number generated is [0.25, 0.4, 0.15, 0.5]. Apply creep
BL-3,4
mutation to obtain the offspring. Let creep value ∆= 0.7.
Q4   a
CO-3   Discuss general principles of swarm intelligence [2.5Marks]. State main
[05]
SO-1   reasons for success of a swarm. [2.5Marks]
BL-2
********** 10 **********
--- page 11 ---
CO-1   b   Sketch a suitable flow diagram for evolutionary algorithm [2Marks] and
SO-1   explain the following components in brief- Population, Fitness, Parent   [05]
BL-2   Selection. [3Marks]
********** 11 **********

[Text in pictures on this page, read by OCR]
General Principles of Swarm Intelligence
ee
a Proximity principle
© Basic units of a swarm should be capable of simple computation
related to its surrounding environment

© Here computation is regarded as a direct behavioral response to
environmental variance, such as those triggered by interactions
among agents

o Depending on the complexity of agents involved, responses may
vary greatly

& However, some fundamental behaviors are shared, such as living-
resource searching and nest building

Oo Principle of diverse response
in narrow region
The distribution should be designed so that each agent will
be maximally protected facing environmental fluctuations
oO Principle of stability and adaptability
Swarms are expected to
without rapidly changing modes since mode changing costs
energy
--- page 12 ---
) ) Parent selection Parents |

Recombination

Mutation

4

I ' ti : __ offs =

urvivor selection

Fig. 3.2. The general scheme of an evolutionary algorithm as a flowchart

Evaluation Function or Fitness Function

a Role of the evaluation function is

© to represent the requirements the population should adapt to meet
a It forms the basis for selection, and so it facilitates improvements
a It defines what improvement means

oO From the problem-solving perspective, it represents the fask to be
solved in the evolutionary context

a Technically, it is a function or procedure that assigns a quality
measure to genotypes

°
Population

SSCS
a The role of the population is to hold (the representation of) possible solutions

oO A population is a multiset of genotypes

a The population forms the unit of evolution

Oo Individuals are static objects that do not change or adapt; it is the population that
does

o Given a representation, defining a population may be as simple as specifying how
many individuals are in it, that is, setting the population size

oO Best individual of a given population is chosen to seed the next generation
oO Worst individual of a given population is chosen to be replaced by a new one
oO Diversity of a population is a measure of the number of different solutions present

© No single measure for diversity exists

oO Diversity measure might be different fitness values, number of phenotypes, number of
genotypes, entropy

FRR ICR] DA KH
--- page 13 ---
c   Consider a problem where we must minimize the function where
𝑓(𝑥) = 𝑥3 −4
Single parent in the population 𝑥= 3
Initial variation 𝜎= 1
Let the random numbers taken from the normal distribution for mutation
are
CO-4
SO-1   𝑧𝑖= [0.8, −0.2, 0.2, 0.5, −0.4]
[10]
BL-4,5   [2.5Marks each]
i.   Using two membered evolutionary strategy algorithm, generate five
off springs from parent given above.
ii.   Compute fitness of parent and off springs
iii.   Evaluate new 𝜎 based on 1/5 success rule
iv.   State your inference about 𝜎 obtained in (iii) above
********** 13 **********

[Text in pictures on this page, read by OCR]
Parent Selection Mechanism

QO The role of parent selection or mate selection is to distinguish among individuals based on their
quality

2 To allow the better individuals to become parents of the next generation

OQ An individual is a parent if it has been selected to undergo variation in order. to create
offspring

O Together with the survivor selection mechanism, parent selection is responsible for pushing
quality improvements

og In EC, parent selection is typically probabilistic
0 Means high-quality individuals have more chance of becoming parents than those with low quality

O Nevertheless, low-quality individuals are often given a small, but positive chance

0 otherwise the whole search could become too greedy and the population could get stuck in a local
optimum

Since £) = 3anda = 1:

Zi Offspring z; = 3+ 2;
0.8 3.8
-0.2 2.8
0.2 3.2
0.5 3.5

-0.4 2.6
--- page 14 ---
Parent

f(3) =3? —4=27-4=23

Offspring

Offspring f(z)=2-4 Success? (Minimize)
3.8 54.872 — 4 = 50.872 No

28 21.952 — 4 = 17.952 Yes

3.2 32.768 — 4 = 28.768 No

3.5 42.875 — 4 = 38.875 No

2.6 17.576 — 4 = 13.576 Yes

(iii) Evaluate new o using 1/5 success rule

Success rate

2
P,=2=04
5
1/5 rule:
e If P, > 1/5 - Increase o
e If. P, < 1/5 - Decrease o
e If P, = 1/5 — Keep o same
Since
0.4 > 0.2

(iv) Inference

Since the success rate is higher than 1/5:
e Step size (0) is too small
¢ Algorithm is progressing well
e Increase o to explore faster and improve convergence

Qs a Consider a problem statement to minimize f(x) = x, — 2x2 + x3 where

CO-4 x; € [-8,8].

B23 Individual 1 | Individual 2 Individual 3 | Individual 4 [10]
xy -1 2 -5 -4

FRR IC 7 I OH
--- page 15 ---
𝑥2.   5   -3   1   -2
𝑥3.   3   1   3   1
Here population size 𝑁= 4, number of parameters 𝐷= 3, Crossover rate
𝐶𝑅= 0.5, Mutation factor 𝐹= 0.7, Random integer for recombination step
𝐼𝑟𝑎𝑛𝑑= 2,
Random number for selection of each element during recombination step =
[0.6, 0.8, 0.95]
[2.5 Marks each]
Apply Differential Evolution Algorithm to-
i.   Generate weighted difference vector using Individual 3 and
Individual 4.
ii.   Generate the noisy vector using Individual 1 and the weighted
difference vector.
iii.   Construct trial vector using Individual 2 as parent and the noisy
vector
iv.   Evaluate fitness of parent vector and offspring vector. State your
inference.
********** 15 **********
--- page 16 ---
b   Consider 4 Cities A, B, C, D to be travelled by the ant, starting at City A.
The ant should return back to City A after covering all the cities.
The distance matrix is given as:
CO-3   A   B   C   D
SO-1   A   0   5   2   7
[10]
BL-4   B   4   0   1   8
C   2   2   0   7
D   7   9   2   0
The Pheromone Matrix is:
********** 16 **********
--- page 17 ---
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
[2.5 Marks each]
********** 17 **********

[Text in pictures on this page, read by OCR]
Py = ( Cu)” )
ij = a B
Z(t) (nis)
Where 1j,; = = ,L, jis the length of edge Gj)

aand B control the relative importance of
pheromone versus the heuristic information nj ;
k
Ty = (1 = ptay + Lhe AT;
Atijis the quantity of pheromone laid on edge (i, j) by ant k

Qa. eye
b ack, = Tel ant k used edge (i,j)in its tour
0, otherwise

1 Where @ is a constant, generally Q=1 and Ly is length of tour constructed by ant k

Sum
0.2 + 0.5 + 0.1429 = 0.8429
Probabilities
Pap = 0.2/0.8429 = 0.237
Pac = 0.5/0.8429 = 0.593

Pap = 0.1429/0.8429 = 0.169
--- page 18 ---
(iii) Pheromone Update
Path taken:

A~C+-B-D-A

Distances:
e A-C=2
e C-B=2
e B-D=8
e D-A=7
Total length:

D=2+2+8+7=19

Pheromone addition:

Evaporation rate:

p=0.7
Update rule:

Trew = (1 — p) Toa + At
(1— p) =0.3
Visited edges:
0.3(1) + 0.0526 = 0.3526

Non-visited edges:

0.3(1) = 0.3
Updated Pheromone Matrix
A B c D
A 0 03 0.3526 0.3526
B 03 0 0.3526 0.3526
c 0.3526 0.3526 0 03
D 0.3526 0.3526 03 0

FR ICR 7] QA HH
--- page 19 ---
a   With the help of suitable pseudocode, demonstrate the steps in Tournament
Selection Algorithm.
Consider the following objective function which has to be minimized.
𝑓(𝑥) = 𝑥1 2 −𝑥2 + 2𝑥3
The solutions in the initial population are given below.
Individual   A   B   C   D
Q6   Genotype   [2,3,5]   [1,2,3]   [3,1,2]   [2,5,6]
CO-2   [2.5 Marks each]
SO-1   [10]
BL-3,5   Using genetic algorithm approach, answer the following-
i.   Implement tournament selection rounds to select two parents as
follows
1st Tournament between individuals A and D
2nd Tournament between individuals B and C
ii.   Use one point crossover between the winner parents from step (i).
Take crossover point as 2.
iii.   Evaluate fitness of the two offspring
********** 19 **********

[Text in pictures on this page, read by OCR]
(iv) Effect of Evaporation Rate (p)

e High p = Fast evaporation — More exploration
e Low p - Slow evaporation — Strong exploitation

e Proper p balances exploration vs exploitation

Inference:

p = 0.7 gives high exploration and avoids premature convergence.

BEGIN
/* Assume we wish to select \ members of a pool of y individuals
set current_member = 1;
WHILE ( current-member <X ) DO
Pick k individuals randomly, with or without replacement;
Compare these k individuals and select the best of them;
Denote this individual as i;
set mating_pool[current_-member] = i;
set current_member = current_-member + 1;
oD
END

*/

Fig. 5.3. Pseudocode for the tournament selection algorithm
--- page 20 ---
Step 1: Evaluate Fitness of Initial Population
Individual A [2,3,5]

f(A) = 2? -342(5) =4-34+10=11
Individual B [1,2,3]

f(B) = —24+2(3)=1-2+6=5
Individual C [3,1,2]

f(C) =3? -14+2(2)=9-14+4=12
Individual D [2,5,6]

f(D) =2?-54+2(6) =4-5412=11
(i) Tournament Selection

1st Tournament: A vs D

A=11
D=11

Tie — choose any (choose A)

Winner1=A

2nd Tournament: B vs C

B=5
C=12
Winner 2 = B

Selected Parents

Parent 1 = A = [2,3,5]
Parent 2 = B = [1,2,3]

FRI ICR DO) A RH
--- page 21 ---
b   Consider the following problem. You have a knapsack of capacity 13kg, and
you must choose from the following six items, maximizing total value while
keeping the total weight ≤ 13 kg. Each item can be either included (1) or not
included (0) in the knapsack.
Item   Weight (kg)   Value
P   2   3
Q   3   4
R   4   5
S   5   8
CO-1   T   6   9
SO-1   U   7   10   [10]
BL-2, 4
i   Create two parent chromosomes of length 6 each by selecting items
[P,Q,T] in chromosome 1 and items [Q, R, S] in chromosome 2
[2Marks]
ii Compute two off springs using Uniform cross over with p=0.5
where the random number for each gene is [0.3, 0.2, 0.4, 0.6, 0.1,
0.8] [2.5Marks]
iii Perform mutation by flipping bits 1,3,5 in offspring 1 and 2,4,6 in
offspring 2 [2.5Marks]
iv   Calculate fitness of each offspring and comment on the same
[3Marks]
********** 21 **********

[Text in pictures on this page, read by OCR]
(ii) One-Point Crossover

Crossover point = 2

Parent 1: [2 3 | 5]
Parent 2: [1 2 | 3]
Offspring

Offspring 1 = [2,3,3]
Offspring 2 = [1,2,5]

(iii) Fitness of Offspring
Offspring 1 [2,3,3]

f =2?-342(3)=4-3+6=7
Offspring 2 [1,2,5]

f=V-—242(5)=1-24+10=9
--- page 22 ---
Mutated Offspring 1 represents a successful, feasible solution that respects
the constraints of the knapsack problem, yielding a good fitness score of 17.
Mutated Offspring 2 is an infeasible solution because it violates the 13 kg
weight limit constraint, meaning it cannot be used and effectively has a
fitness of 0 in standard genetic algorithm constraint handling.
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
********** 22 **********

[Text in pictures on this page, read by OCR]
Mutated Offspring 1: [@, 1, 1, 1, @, @] (Contains items Q, R, S)
¢ Total Weight = 3kg + 4kg + 5kg = 12 kg
e Total Value=4+5+8=17

e Evaluation: Since 12 kg < 13 kg, this is a valid solution. Fitness = 17.

Mutated Offspring 2: [@, @, 1, 1, , 1] (Contains items R, S, U)
¢ Total Weight = 4kg + 5kg + 7kg = 16 kg
¢ Total Value = 5 +8+10=23

¢ Evaluation: Since 16 kg > 13 kg, the weight exceeds the maximum capacity constraint.
Fitness = 0 (infeasible).
--- page 23 ---
b   State the factors on which flow of information depends upon through a
CO-3   Social Structure. Discuss with the help of suitable diagram Star Social
SO-1   Structure, Ring Social Structure, Wheel Social Structure and Von
[10]
BL-2   Neumann Social Structure with reference to network topologies in Particle
Swarm Optimization
********** 23 **********

[Text in pictures on this page, read by OCR]
Rank based Ant System Algorithm
AS+ank

3 Update of Pheromone Trails

5 Before updating the pheromone trails, the ants are sorted by increasing tour length and the quantity of pheromone an ant deposits is weighted
according to the rank r of the ant

5 Ties can be solved randomly (in our implementation they are solved by lexicographic ordering on the ant name k)

5 In each iteration only the (W — 1) bestranked ants and the ant that produced the best-so-far tour (this ant does not necessarily belong to the set
of ants of the current algorithm iteration) are allowed to deposit pheromone

© The best-so-far tour gives the strongest feedback, with weight w
= (Le, its contribution 1/Cps is multiplied by w),
o iy Tth best ant of the current iteration contributes to pheromone updating with the value 1/Cr multiplied by a weight given by max{0, w —
r}.

© Thus, the AS;ank pheromone update rule is, 1
we

y+ —r)At;, + wr},

o In AS+ank

each ant deposits an amount of pheromone that decreases
with its rank

the best-so-far ant always deposits the largest amount of
pheromone in each iteration

Feature Ant System (AS) Rank-Based Ant System (RBAS)

Pheromone Update All ants update pheromone Only top-ranked ants update
pheromone

Solution Contribution Every ant contributes equally Better ants contribute more

Convergence Speed Slower convergence Faster convergence

Solution Quality May converge to suboptimal Usually better solution quality
solution

Computational Efficiency Less efficient More efficient

Selection Strategy No ranking mechanism Uses ranking of ants

Exploitation vs Exploration More exploration More exploitation of best

solutions
--- page 24 ---
Social Network Structures

|
Oo Within the PSO, particles in the same neighborhood communicate with one
another by exchanging information about the success of each particle in
that neighborhood

oO AIl particles then move towards some quantification of what is believed to
be a better position

oO The performance of the PSO depends strongly on the structure of the social
network

0 The flow of information through a social network, depends on
© (1) the degree of connectivity among nodes (members) of the network,

© (2) the amount of clustering (clustering occurs when a node’s neighbors are also
neighbors to one another), and

a (3) the average shortest distance from one node to another

Various kinds of social network structures
es

O Star social structure
© All particles are interconnected

5 Each particle can therefore communicate with every
other particle

o In this case each particle is attracted towards the best
solution found by the entire swarm

5 Each particle therefore imitates the overall best
solution

othe first implementation of the PSO used a star
network structure, with the resulting algorithm
generally being referred to as the gbest PSO

© The gbest PSO has been shown to converge faster
than other network structures, but with a susceptibility
to be trapped in local minima

The gbest PSO performs best for unimodal problems (a) Star

Various kinds of social network structures
2 eee

0 Ring social structure
5 Each particle communicates with its nV immediate neighbors

5 Inthe case of nN = 2,4 particle communicates with its
immediately adjacent neighbors

5 Each particle attempts to imitate its best neighbor by moving
closer to the best solution found within the neighborhood

5 Its Important to note that neighborhoods overlap

5 This facilitates the exchange of information between
neighborhoods and, in the end, convergence to a single solution

5 Since information flows at a slower rate through the social network,
convergence is slower, but larger parts of the search space are
covered compared to the star structure

3 This behavior allows the ring structure to provide better
performance in terms of the quality of solutions found for multi-
modal problems than the star structure

3 Resulting PSO algorithm is generally referred to as the Ibest PSO
(b) Ring

Various kinds of social network structures
ee

a Wheel social structure

© Individuals in a neighborhood are isolated from
one another

© One particle serves as the focal point, and all
information is communicated through the focal
particle

O Focal particle compares the performances of all
particles in the neighborhood, and adjusts its
position towards the best neighbor

© If the new position of the focal particle results in
better performance, then the improvement is
communicated to all the members of the
neighborhood

Gc Wheel social network slows down the propagation (c) Wheel
of good solutions through the swarm

FRR IRD AC HOH
--- page 25 ---
Various kinds of social network structures

O The Von Neumann social
structure

© Particles are connected
in a grid structure

© The Von Neumann social
network has been shown >
in a.number.of empirical
studies to outperform
other social networks in
a.large number. of
problems

(8) Von Neumann,

FI ICR AC KH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper d742a6ccff65

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AI_7012/Evolutionary Computing/ANS_Evolutionary Computing(702AI0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (22 pages), mean OCR confidence 67.5
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Evolutionary Computing
Date: 29 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a   With reference to permutation representation, discuss the following two
mutation techniques- scramble mutation, swap mutation using suitable
examples. [2.5 marks each]
CO-2 ;
SO-1 ;
BL-2
b   Discuss Linear and Exponential Rank-based parent selection mechanism
with suitable expression. [2.5 marks each]
CO-2 ;
SO-1 ;
BL-2
********** 1 **********

[Text in pictures on this page, read by OCR]
Ranking Selection
——
0 The usual formula for calculating the selection
probability for linear ranking schemes is
parameterised by a value s (1 <s < 2)
0 Since the best individual has rank . — 1, and the
worst has rank 0, then the selection probability for
an individual of rank i is
(2-8)   2i(s—1)
n+ wud)”

Phin—rank(i) =
--- page 2 ---
c   Compare Genetic Algorithm and Genetic Programming with reference to
the following points-
Representation, Recombination, Mutation, Parent Selection, Survivor
Selection [1 Mark each]
CO-4 ;
SO- 1;
BL-3
d   For Ant System algorithm state and explain equations to update the
pheromone level with and without evaporation. [3Marks] State the
significance of evaporation rate in terms of exploration and exploitation. [2
Marks]
CO-3 ;
SO-1 ;
BL- 2
a   i.   Apply Order Crossover to generate two off springs. Assume the
Q2   Crossover points as 3 and 5.   [10]
Parent 1: 8 6 5 7 3 2 1 4
********** 2 **********

[Text in pictures on this page, read by OCR]
ca When the mapping from rank to selection probabilities is linear, only limited selection
pressure can be applied

© This arises from the assumption that, on average, an individual of median fitness should
have one chance to be reproduced,
© which in turn imposes a maximum valve of s = 2.

1 (Since the scaling is linear, letting s > 2 would require the worst to have a negative selection
probability if the probabilities are to sum to unity)

2 If ahigher selection pressure is required, i.e., more emphasis on individuals of above-
average fitness, an exponential ranking scheme is often used, of the form

1—e*

Pezp-rank(i) = —=

The normalisation factor c is chosen so that the sum of the probabilities is unity, ie., it is a
function of the population size

Representation | Bit-strings

Recombination — |1-Point crossover

Mutation Bit flip

Parent selection |Fitness proportional - implemented by Roulette Wheel

Survival selection|Generational

Table 6.1. Sketch of the simple GA

Representation _|Tree structures

Recombination |Exchange of subtrees

Mutation Random change in trees

Parent selection |Fitness proportional

Survivor selection|Generational replacement

Table 6.4. Sketch of GP

Its main characteristic is that, at each iteration, the pheromone values are updated
by all the m ants that have built a solution in the iteration itself

The pheromone 7;,;, associated with the edge joining cities i and j, is updated as
follows-

5 tj = Lee Ath;
k
8 uy=(-p)tiy + De Ati;
= where p is the evaporation rate, mM is the number of ants, and Tj,

Atk jis the quantity of pheromone laid on edge (i, j) by ant k
Qa. © ion 7,
—,if ant k used edge (i, j)in its tour

o Ark, = mel ge (ij)

0, otherwise

cm Where Q is a constant, generally Q=1 and L, is length of tour constructed by ant k
--- page 3 ---
CO-2;   Parent 2: 1 2 7 3 4 5 6 8
SO-1;   ii.   Apply uniform crossover on the following parents to generate
BL-2,3   two offspring using the crossover mask as given-
Parent 1: 1 1 0 1 0 0 1 0
Parent 2: 0 1 1 0 1 1 1 1
Uniform crossover mask: 1 1 1 0 0 0 1 1
iii.   Consider the chromosome 𝑌= [4,6,2,9,3,7]. The allowed gene
range is   [0-9]. Mutation probability for each gene is 𝑝𝑚= 0.4.
The random numbers   generated   for each gene   are
[0.35,0.45, 0.1,0.67, 0.25, 0.75] . Apply creep mutation with
creep value ∆= −1.
iv.   State the expression for random setting in integer representation
********** 3 **********
--- page 4 ---
b
Explain fitness sharing diversity maintenance approach with suitable
expressions.
CO-2
SO-1;   [05]
BL-2
CO-4   c
With reference to Genetic Programming, explain Grow and Full methods for
SO-1;   [05]
population initialization. [2.5 Marks +2.5 Marks]
BL-2
********** 4 **********

[Text in pictures on this page, read by OCR]
Fitness Sharing

0 Fitness sharing distributes the population among multiple solutions so that only a few
individuals are maintained in the vicinity of each solution in the search space

0 The fitness of each individual in the current population is reduced based on the number of
similar individuals in the population
= Amodified fitness value is calculated for each population individual by
11 dividing the fitness, F, by the niche count of the individual, m;, which is defined by
= mj = Ljepop Sh(dij)
= Where djj is the Euclidean distance between individuals i and j and
= sh(djj) is the sharing function which is given by

a
# sn(ay)=43~ (4) Fay < es
0 otherwise
= Here a determines the shape of the sharing function. Example if @=1 then the sharing function is linear
= zs is the share radius which decides both
= How many niches can be maintained
= G ‘ity with which dit niches can be dis

Fitness Sharing
aaa V7—| oe)
a Hence modified fitness value is given by

o Fp) =2

a Where 1 m= Ljepop Sh(dij)
= Where dij; is the Euclidean distance between individuals i and j and
= sh(dj;) is the sharing function which is given by
1-(%)" if a,
w sa(ay)=}2~ (G1) Pau <a:
0 otherwise

= Here a determines the shape of the sharing function. Example if @=1 then the sharing
function is linear
= Gy is the share radius which decides both
= How many niches can be maintained
= Granularity with which different niches can be discriminated
--- page 5 ---
a   Consider the problem to Maximize 𝑓(𝑥) = 50(𝑥1 2 −𝑥2 2) where
−3 ≤𝑥1, 𝑥2 ≤3 . Apply GBest Particle Swarm Optimization Algorithm
to-[2.5 Marks each]
i.   Determine fitness of the initial population
ii.   Identify personal best of each particle of the first generation and
Q3
identify the global best of the swarm
CO-3;
iii.   Update velocity, position only for the second particle of the second [10]
SO-1
generation
BL-4,5
iv.   Evaluate fitness of the updated second particle and identify the
personal best for the same.
The initial position and velocity are as given in the table below-
Index(i)   Xi(1)   Vi(1)
1   (3,2)   (0.0,0.0)
********** 5 **********

[Text in pictures on this page, read by OCR]
Initializing the population
———K—z—r—aRL—L——
c In both the Full and Grow methods, the initial individuals
are generated subject to a pre-established maximum
depth
c In the Full method (so named because it generates full
trees)

© nodes are taken at random from the function set until this
maximum tree depth is reached

G and beyond that depth only terminals can be chosen

Initializing the population

|
a Full initialization method

Figure shows snapshots of this

Ht 2 133 tes
Taw process in the construction of a
full tree of depth 2
* * y © The children of the * node, for
ss ee wv example must be leaves, or the
resulting tree would be too deep
Thus at time t = 3 and time t = 4
x y x yd x ya ° terminals must be chosen (x and y

Fig. 4. Creation of a full tree having maximum depth 2 (and therefore a total of in this case)
seven nodes) using the Full initialization method (t=time)

© Full method generates trees of a
specific size and shape
Function set= {*,+,/,-}
Terminal set= {x,y,1,0}

Initializing the population
|

9 ~~ Grow initialization method

tt te ts 5 Grow method allows for the creation of trees
Dn Taw of varying size and shape
x x 5 Here nodes are selected from the whole
primitive set (functions and terminals) until the
to 5 depth limit is reached, below which only

terminals may be chosen
‘ x 15 Figure illustrates this process for the
construction of a tree with depth limit 2

2 2 y 2 Here the first child of the root + node
Fig. 5. Creation of a ation method with a happens to be a terminal, thus closing off
maximum depth of 2 ‘causing the left branch that branch before actually. reaching the
of the root to be closed at tha n depth had not been depth limit

reached 5 The other child, however, is « function (-), but
its children are forced to be terminals to
. — x ensure that the resulting tree does not exceed
Function set= {*,+,/,-} the depth limit

Terminal set= {x,y,2}
--- page 6 ---
2   (3,3)   (0.0,0.0)
3   (0,-3)   (0.0,0.0)
4   (1,-2)   (0.0,0.0)
5   (-1,-2)   (0.0,0.0)
Take inertia weight 𝑤𝑡= 0.75, correction factors 𝑐1 = 2 𝑎𝑛𝑑 𝑐2 = 2.
Random numbers for the second particle are given below-
Particle   r1   r2
2   0.3   0.5
CO-4   b
SO-1
Consider the following Finite State Machine (FSM)   [05]
BL-2
********** 6 **********
--- page 7 ---
i.   For the input stream [0 1 1 1 0 1] evaluate the corresponding
output. [1.5 Marks]
ii.   Evaluate fitness for the above input if the fitness function is
% 𝑜𝑓 𝐼𝑛𝑝𝑢𝑡𝑛+1 = 𝑂𝑢𝑡𝑝𝑢𝑡𝑛 [1 Marks]
iii.   Perform the mutation on the above state diagram by changing
the initial state to 2 and obtain the output corresponding to the
same input given above [1.5 Marks]
iv.   Evaluate fitness using the function given above [1 Marks]
********** 7 **********
--- page 8 ---
c   i.   State two common applications where permutation representation
can be used.[1 Marks]
ii.   Apply cycle crossover on the following two parents to obtain two
offsprings. [4 Marks]
Parent 1: 9 8 7 6 5 4 3 2 1
Parent 2: 4 1 5 6 2 8 7 3 9
Task Scheduling, Sequencing problem
CO-2
SO-1   [05]
BL-3,4
Q4   a
With reference to Particle Swarm Optimization, explain the following
CO-3
social network structure with appropriate diagrams- Star social structure
SO-1   [05]
and Ring social structure [2.5 Marks +2.5 Marks]
BL-2
********** 8 **********
--- page 9 ---
b   Write the pseudocode of Evolutionary Algorithm. [2Marks]
Discuss the following components of Evolutionary Algorithm in not more
than 2 lines each- Representation, Evaluation Function, Termination
Condition [1 Mark each]
CO-1
SO-1   [05]
BL-2
********** 9 **********

[Text in pictures on this page, read by OCR]
Star social structure
© All particles are interconnected

o Each particle can therefore communicate with every
other particle

© In this case each particle is attracted towards the best
solution found by the entire swarm

a Each particle therefore imitates the overall best

solution

1 The first implementation of the PSO used a star
network structure, with the resulting algorithm

generally being referred to as the gbest PSO

11 The gbest PSO has been shown to converge faster
than other network structures, but with a susceptibility
to be trapped in local minima

5 The gbest PSO performs best for unimodal problems (a) Star

2
a — Ring social structure

5 Each particle communicates with its nV immediate neighbors

© Inthe case of nN = 2,4 particle communicates with its
immediately adjacent neighbors

5 Each particle attempts to imitate its best neighbor by moving
closer to the best solution found within the neighborhood

5 Iris imp to note that nei P

This facilitates the exchange of information between
neighborhoods and, in the end, convergence to a single solution

1 Since information flows at a slower rate through the social network,
convergence is slower, but larger parts of the search space are
covered compared to the star structure

5 This behavior allows the ring structure to provide better

erformance in terms of the quality of solutions found for multi-

modal problems than the star structure

| Resulting PSO algorithm is generally referred to as the Ibest PSO

BEGIN
INITIALISE population with random candidate solutions;
EVALUATE each candidate;
REPEAT UNTIL ( TERMINATION CONDITION is satisfied ) DO
1 SELECT parents;
2 RECOMBINE pairs of parents;
3 MUTATE the resulting offspring;
4 EVALUATE new candidates;
5 SELECT individuals for the next generation;
oD

Fig. 3.1. The general scheme of an evolutionary algorithm in pseudocode
--- page 10 ---
Representation
eC

oO Mapping real world problem to (Evolutionary
Algorithm) EA world

Oo Simplifying or abstracting some aspects of the real
world

O to create a well-defined and tangible problem context
© within which possible solutions can exist and

oO can be evaluated, and this work is often undertaken by
domain experts

Evaluation Function or Fitness Function
ee
a Role of the evaluation function is
5 to represent the requirements the population should adapt to meet
c It forms the basis for selection, and so it facilitates improvements
a It defines what improvement means

oO From the problem-solving perspective, it represents the task to be
solved in the evolutionary context

a Technically, it is a function or procedure that assigns a quality
measure to genotypes

Termination Condition
HE eee

a If the problem has a known optimal fitness level, probably coming from a known optimum of
the given objective function, then in an ideal world our stopping condition would be the
discovery of a solution with this fitness

c_ If we know that our model of the real-world problem contains necessary simplifications, or
may contain noise, we may accept a solution that reaches the optimal fitness to within a given
precision €> 0

ca However, EAs are stochastic and mostly there are no guarantees of reaching such an optimum,
so this condition might never get satisfied, and the algorithm may never stop

c Therefore we must extend this condition with one that certainly stops the algorithm

5 The following options are commonly used for this purpose:
5 The maximally allowed CPU time elapses.
© The total number of fitness evaluations reaches a given limit

5 The fitness improvement remains under a threshold value for a given period.of time (i-e., for a.number.
of generations or fitness evaluations)

The population diversity drops under a given threshold

c Consider a problem statement to minimize f(y) = y1 + 4y2 + 2y3 where
y; € [-9,9].
co-4 Individual 1 | Individual 2 Individual 3 | Individual 4
si, | [oR a
V2 4 -3 1 -2
V3 2 1 2 3

FRR ICR 7 OI HOH
--- page 11 ---
Here population size 𝑁= 4, number of parameters 𝐷= 3, Crossover rate
𝐶𝑅= 0.7, Mutation factor 𝐹= 0.6, Random integer for recombination step
𝐼𝑟𝑎𝑛𝑑= 3,
Random number for selection of each element during recombination step =
[0.5, 0.85, 0.9]
Apply Differential Evolution Algorithm to- [2.5 Marks each]
i.   Generate weighted difference vector using Individual 1 and
Individual 4.
ii.   Generate the noisy vector using Individual 3 and the weighted
difference vector.
iii.   Construct trial vector using Individual 2 as parent and the noisy
vector
iv.   Evaluate fitness of parent vector and offspring vector. State your
inference.
********** 11 **********
--- page 12 ---
wernt Ay

oe) ath n dv > + veyev

(Wy Noicy igor wi

paves


= Wy,
Trin yor
32
4b
v4
7 = Ting
Vy y ambi SONS
it =
Atha
| My   mnagiae BS] Po
nthe >)
AW rene calor (AORN
By) fee 2 oe Naye=
eo ear etO
@
Rts y Tin r

yous UY > Ys
te = G+ ycu's> + 2 uu)

= \
S , } (sovent > ra
trou wh minimize =~

i binkvuhr ),

FRR ICR] DA KH
--- page 13 ---
a   For a minimization problem the given function is as follows:
𝑓(𝑥) = 2𝑥2 −3
Single parent in the population 𝑥= 4
Initial variation 𝜎= 1
Let the random numbers taken from the normal distribution for mutation
are
𝑧𝑖= [0.7, −0.2, 0.3, 0.5, −0.6]
i.   Using two membered evolutionary strategy algorithm, generate five
off springs from parent given above. [3 Marks]
ii.   Compute fitness of parent and off springs [3 Marks]
iii.   Evaluate new 𝜎 based on 1/5 success rule. Take the value of 𝑐=
0.8 [3 Marks]
iv.   State your inference about 𝜎 obtained in (iii) above [1Mark]
Q5
CO-4
SO-1   [10]
BL-2,3
b   Discuss the improvement of Elitist Ant System Algorithm over Ant System
Algorithm with reference to pheromone update expression. [2 Marks]
CO-3   Consider the following distance graph and pheromone level graph for the
SO-1   Travelling Salesman Problem where nodes A, B, C and D represent four
[10]
BL-4   cities.
********** 13 **********
--- page 14 ---
Distance graph   Initial Pheromone level graph
The two ants in this problem have traversed the following loop-
Ant 1: A-B-C-D-A and Ant 2: A-C-B-D-A
[2 Marks each]
i.   Compute the pheromone level 𝜏𝐴𝐷 𝑎𝑛𝑑 𝜏𝐵𝐷 with evaporation rate
𝜌= 0.8 using expression of Elitist Ant System Algorithm. Take
parameter that defines weight given to the best-so-far tour 𝑒= 2.
ii.   Compute the pheromone level 𝜏𝐴𝐷 𝑎𝑛𝑑 𝜏𝐵𝐷 with evaporation rate
𝜌= 0.8 using expression of Ant System Algorithm
iii.   State your inference about pheromone level based on the results
obtained in (i) and (ii)
********** 14 **********

[Text in pictures on this page, read by OCR]
0 Update of Pheromone Trails
0 Additional reinforcement of tour Tis achieved by adding a quantity e/C”® to its arcs

= where e is a parameter that defines the weight given to the best-so-far tour T?S,
CSis its length

@
5 Thus, equation for the pheromone deposit becomes

2.3

k bs m~™
9 Ty gt) At; +eArF, ¢ -   A_eZ, *
: > i ij Gij- G ey ona
Oo where o ° © =
bs
+ ebay
Atk = {Vv if are (i,j) belongs to T*; cio {! Co, if are (i,j) belongs to TP
1 No, otherwise; a otherwise.

where G;,, the length of the tour 7;,built by the keh ant
--- page 15 ---
K-B-CD-#& => Litzlé

ee far | Me
p-c B-dD-A DAF oF

fone 2 yen *
for Cuno ane (gz08, e=2l
Oe oet 2 Ati .t at
iy 2 be
‘yu bugs 38 306m Mh Ore

ATi 259 'lu
(6) onmni fe

(

2
1 2 9s, St * 4a
7

= 0 ATay= s,

Zay = (1-0-#) x04 +[43 uy oul

\6
= 0°304
————;
= 031%
= \ axes, 2 03'
Zone (1-08 1 + 25
ga0-e

Tap = C

FRR IC 7 DA HOH
--- page 16 ---
a   i.   Explain Fitness Proportionate Selection mechanism for parent
selection with the help of suitable expression.[2 Marks]
ii.   Explain how Fitness Proportional Selection Mechanism suffers
from – (A) Premature Convergence (B) High susceptibility to
Function transposition .[2 Marks]
iii.   Consider the following five chromosomes in the initial
population, 𝑥𝑖= {8, 21, 10, 12, and 5} . Complete the table
below and determine the two parents selected for recombination
using Roulette Wheel selection algorithm if the fitness function
Q6   is 𝑓(𝑥𝑖) = 3𝑥𝑖+ 2 and the random numbers generated are
CO-2
{0.76, 0.23}.[6Marks]
SO-1   [10]
BL-3,5   Chromosome Chromosom   Fitness   Probability   CDF
e value
𝑥𝑖
A   8
B   21
C   10
D   12
E   5
********** 16 **********
--- page 17 ---
b   Consider a 4-Queens problem where the initial population has the
following four chromosomes.[2 Marks each]
CO-1   A   2 3 2 4
SO-1   B   3 1 2 4
[10]
BL-2, 4   C   4 2 3 1
D   1 3 4 2
i.   Compute fitness for each chromosome if the fitness function is
number of non-attacking queens
********** 17 **********

[Text in pictures on this page, read by OCR]
Fitness Proportionate Selection
eee

oO Probability that an individual i is selected for crossover
depends on its absolute fitness value compared to the
absolute fitness values of the rest of the population

oO. Observing that the sum of the probabilities over the wh
population must equal 1 the selection probability of
individual i using FPS is

Prps(i = fil fj.
--- page 18 ---
ii.   Implement tournament selection rounds to select two parents as
follows
1st Tournament between chromosomes A and D
2nd Tournament between chromosomes B and C
iii.   Apply one point crossover between the parents obtained in (ii)
to obtain the two offsprings. Take cross over point as 1.
iv.   Apply swap mutation only on offspring 1. Swap allele in
position 2 and 4.
v.   Evaluate the fitness of both the offsprings.
********** 18 **********
--- page 19 ---
a   With reference to Max-Min Ant System Algorithm, answer the following
question [2.5 Marks each]
Q7
i.   Discuss the concept of pheromone trails update in Max-Min Ant
CO-3
System Algorithm
SO-1   [10]
ii.   Write the expression for pheromone update rule
BL-2,3
iii.   Explain each component of the expression in (ii)
iv.   Elaborate on the key differences between Ant System Algorithm
and Max-Min Ant System Algorithm
********** 19 **********
--- page 20 ---
b   i.   Discuss the significance of velocity clamping and inertia weights
with the help of suitable expressions [2.5 Marks +2.5 Marks]
ii.   Explain the following rules with respect to the flocking behavior in
particle swarm optimization- Separation, Alignment, Cohesion
[5Marks]
CO-3
SO-1
[10]
BL-2
********** 20 **********

[Text in pictures on this page, read by OCR]
Max Min Ant System Algorithm

O Key to achieve best performance of ACO algorithms is
5 to combine an improved exploitation of the best solutions found during the search with an
effective mechanism for avoiding early search stagnation
c MAX -MIN Ant System, which has been specifically developed to meet these
requirements, differs in three key aspects from AS
O To exploit the best solutions found during an iteration or during the run of the algorithm,
after each iteration only one single ant adds pheromone
= This ant may be the one which found the best solution in the current iteration (iteration-best ant) or
the one which found the best solution from the beginning of the trial (global-best ant)
© To avoid stagnation of the search the range of possible pheromone trails on each solution
component is limited to an interval [Tmax and Tmin]
o Additionally, we deliberately initialize the pheromone trails to Tmax, achieving in this way
a higher exploration of solutions at the start of the algorithm

Max Min Ant System Algorithm

© This algorithm is an improvement over the original Ant System

co Its characterizing elements are that
1 only the best ant updates the pheromone trails and

1 that the valve of the pheromone is bound

Pheromone update is implemented as follows-

ty [a = p)-ti + ads]! ~
Tin
Oo where where Tax and Tin are respectively i the upper and lower bounds imposed
on the pheromone; the operator x]%, and At;; Dest is defined as

b ifx <b, 0 otherwise,

ifx > a,

| a ifx>a Art = | 1/Lics if (i, j) belongs to the best tour,

yo
x otherwise;

Velocity Clamping
a

O To control the global exploration of particles, velocities are clamped
to stay within boundary constraints

a If a particle’s velocity exceeds a specified maximum velocity, the
particle’s velocity is set to the maximum velocity

a Let Vingx,j denote the maximum allowed velocity in dimension j
c Particle velocity is then adjusted before the position update using

vj(t+1) if uj(t+1) <Vinaxj :
»(t+1) = ij iy 16.1
alt+ 0) { Vinazy hey (t+1) 2 Vnaey un
--- page 21 ---
Velocity Clamping

a
2 The value of Vinax,j is very important, since it controls the granularity of the search by
clamping escalating velocities

2 Large values of Vinax,jfacilitate global exploration, while smaller values encourage local
exploitation

2 If Vinax,jis too small, the swarm may not explore sufficiently beyond locally good regions
5 Also, too small values for Vinax,j increase the number of time steps to reach an optimum

co Furthermore, the swarm may become trapped in a local optimum, with no means of escape
2 On the other hand, too large values of Vinax,j risk the possibility of missing a good region

co The particles may jump over good solutions, and continue to search in fruitless regions of the
search space

5 While large values do have the disadvantage that particles may jump over optima, particles
are moving faster

Velocity Clamping

a This leaves the problem of finding a good value for each
Vinax,j in.order.to balance between
© (1) moving too fast or too slow, and
5 (2) exploration and exploitation
a Usually, the Vingx,j values are selected to be a fraction of
the domain of each dimension of the search space
a That is,
Vinaz,j = 5(£maz,j — Tmin,j)

where Xmax,j ANd Xmin,j are respectively the maximum and minimum values of the
domain of x in dimension j, and 6 € (0, 1]

Inertia Weight

Oo Inertia weight was introduced by Shi and Eberhart as a mechanism
© to control the exploration and exploitation abilities of the swarm, and
© to eliminate the need for velocity clamping

oO The inertia weight was successful in addressing the first objective, but could
not completely. eliminate the need for velocity clamping

O The inertia weight, w, controls the momentum of the particle by weighing the
contribution of the previous velocity — basically controlling how much
memory of the previous flight direction will influence the new velocity

a For the gbest PSO, the velocity equation changes from equation (16.2) to

A similar change is made for the best PSO

Inertia Weight

a The value of w is extremely important to ensure convergent behavior, and
to optimally tradeoff exploration and exploitation

a For w 2 1, velocities increase over time, accelerating towards the maximum
velocity (assuming velocity clamping is used), and the swarm diverges

a Particles fail to change direction in.order.to move back towards promising
areas

a For w <1, particles decelerate until their velocities reach zero (depending
on the values of the acceleration coefficients)

a Large values for w facilitate exploration, with increased diversity
a Asmall w promotes local exploitation

FI ICR D7 FAC HOH
--- page 22 ---
Oo Essentially the basic models of flocking behaviour

are controlled by three simple rules:

5 Separation - avoid crowding neighbours (short range
repulsion)

o Alignment - steer towards average heading of
neighbours

o Cohesion - steer towards average position of
neighbours (long range attraction)

FIR ICR DAC HH
````
