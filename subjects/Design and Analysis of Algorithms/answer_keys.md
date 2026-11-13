# Design and Analysis of Algorithms: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 34cf0d9e23de

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSE_DS_7011/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C068)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 07 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 question.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Define Algorithm.
“The choice of algorithmic design paradigm is an important aspect of
algorithm synthesis.” Justify the statement by giving suitable examples.
CO-1; SO-   1+4
1; BL-1
CO-1;   b.
SO-1;   Interpret the control abstraction of the Greedy paradigm.   5
BL-2
CO-4;   c.   Illustrate the optimality of the Dynamic Programming strategy.
SO-6;   5
BO-3
********** 1 **********

[Text in pictures on this page, read by OCR]
1. Definition of Algorithm

An algorithm is a finite sequence of well-defined, step-by-step instructions used to solve a problem or
perform a computation. It takes some input, processes it through a series of unambiguous steps, and
produces the desired output within a finite amount of time.

2. Justification of the Statement

“The choice of algorithmic design paradigm is an important aspect of algorithm synthesis.”

This statement is absolutely valid because the design paradigm (approach used to construct an algorithm)
directly affects:

¢ Efficiency (time and space complexity)
¢ Simplicity and clarity

¢ Scalability for large inputs

¢ Feasibility of solving complex problems
--- page 2 ---
CO-3; SO-   d.   1) Solve the recurrence relation of quicksort in the worst case?
2;   4+1
BL-2   2) How can we improve pivot selection to avoid the worst case?
a.   With reference to Asymptotic complexity,
1) Define Upper bound, Tight bound, Lower bound complexities.
2) State the Master’s theorem for decreasing functions.
3)
Q2
CO-1; SO-   With reference to Mergesort,   6+2+2
1; BL-2   b.   1) Explain the Mergesort algorithm using the Divide-and-Conquer
approach.
2) Discuss Mergesort with respect to stability and in-place sorting.
CO-4; SO-   8+2
6,7; BL-2,4
Q3   a.   Illustrate the operation of Quicksort on the array
CO-2;   A=<45,31,5,16,11,29,3,59,82,6>. Analyze the time complexity across   [10]
SO-1;   all scenarios. Identify the complexity of the data list given above. Show
BL-2   the complete data flow.
CO-3;   b.   Write and explain the algorithm for a Multistage graph using the
SO- 2;   backward approach in Dynamic Programming. Analyse its Time   [10]
BL-3   Complexity.
********** 2 **********

[Text in pictures on this page, read by OCR]
Key Idea of Optimality

The optimality of DP is based on the Principle of Optimality, which states:

‘An optimal solution to a problem contains optimal solutions to its subproblems.”

This means:
¢ Ifa problem can be broken into smaller parts,
e And each part is solved optimally,
¢ Then combining them yields a globally optimal solution.
--- page 3 ---
a.   1) What do you understand by a recurrence relation? Explain with an
example.
2) Solve the following recurrence relation using the recursion tree
method-
T(n) = T(n/3) + T(2n/3) + cn   3+7
b.
With reference to PRIM’s algorithm
1) Interpret the algorithm to solve the minimum spanning tree using
Q4   PRIM’s algorithm, adopting the greedy approach.
CO-2; SO-   7+2+1
6; BL-5   2) Analyse the time complexity.
3) Can Prim’s algorithm work for disconnected graphs?
CO-4; SO-
1; BL3
2+3+5
a.   With reference to the Sum of Subsets problem, X={3,4,5,6,7,}and
Q5   Y={15}
CO-3; SO-   1) State the problem statement of the Sum of Subsets problem
2;
BL3   2) Explain the Backtracking paradigm, in general.
3) Generate a state-space tree to find the possible subset from X
b.   that sum to Y using the backtracking approach.
CO-4; SO-
1; BL2   Apply Bellman-Ford algorithm using a dynamic approach to find all-
pairs shortest paths from source 1. Analyse its algorithm and
complexity.   5+5
********** 3 **********

[Text in pictures on this page, read by OCR]
Multistage Graph - Backward Approach (Dynamic Programming)

A multistage graph is a directed acyclic graph (DAG) divided into stages, where:

e There is a source node in stage 1
¢ Asink (destination) node in the last stage

¢ Edges exist only from one stage to the next

The goal is to find the minimum cost path from source to destination.

1) Idea of Backward Approach (Dynamic Programming)

Instead of solving from source — destination, we solve backwards:

© Start from the destination node
¢ Move stage by stage towards the source

¢ Compute the minimum cost from each node to destination

This ensures that when evaluating a node, all its future costs are already known.

1) Prim’s Algorithm using Greedy Approach

Prim’s Algorithm is used to find a Minimum Spanning Tree (MST) of a connected, weighted, undirected
graph.

Greedy Strategy
¢ Start from any vertex
¢ Ateach step, select the minimum weight edge that connects:
« A vvertex inside the MST to a vertex outside the MST
¢ Continue until all vertices are included

The algorithm always makes a locally optimal choice, which leads to a globally optimal solution.
--- page 4 ---
Q6   a.   Distinguish between Greedy, Divide & Conquer, Dynamic
CO-1;   Programming, and Backtracking in terms of:
SO-1;
BL-2   • Problem-solving approach
• Optimality   [10]
CO-4;   •   Efficiency
SO-1;   • Real-world applications
BL3
b.   Identify the efficient order for the chain of multiplication of three   [10]
matrices A(5x4), B(4x6), and C(6x2), using a dynamic programming
approach. Analyze its Time Complexity.
a.   1) State the condition that makes a decision problem belong to
a. Class P
[10]
b. Class NP
Q7   c. Class NP-Hard
CO-4;   d. NP-Complete
SO-1; BL3   Illustrate the relation between these classes using a Venn Diagram
2) Compare the growth of functions:
CO-1; SO-   𝑓(𝑛) = 𝑛2 log𝑛 and 𝑔(𝑛) = 𝑛(log𝑛)10
1; BL-1
Write and explain the algorithm for the “N queens problem” using the
[8+2]
b.   backtracking approach and taking a suitable example. Discuss its Time
complexity. Draw the state space tree for n=4.
********** 4 **********

[Text in pictures on this page, read by OCR]
Comparison of Algorithm Design Paradigms

Aspect Greedy Divide & Conquer Dynamic Programming Backtracking oe

Problem-Solving Makes the locally optimal Divides problem into Breaks problem into Explores all possible solutions,

Approach choice at each step without independent subproblems, overlapping subproblems abandoning paths that violate
reconsidering decisions solves recursively, and and stores results constraints

combines results (memoization/tabulation)

Optimality May or may not give global Gives optimal solution if Always gives optimal Guarantees optimal solution
optimum (depends on subproblems are solved solution (based on but by exhaustive search
greedy property) optimally Principle of Optimality)

Efficiency Very efficient ~ usually Efficient — typically O(n log Moderate — improves Least efficient often
O{n) or O(n log n) n) exponential problems to exponential time O(2")

polynomial time

Real-World - Network design (MST) - Sorting (Merge Sort, - Shortest path
Applications - Scheduling problems Quick Sort) - Resou
- Data compression ~ Binary search

- Parallel computing
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 9a8573c3d8f9

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CS_7055/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C071)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (13 pages)
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 16 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data, if necessary.
Q1
Answer briefly:   Marks
a.   Define an algorithm. Explain its key characteristics with suitable
examples.
Answer:
An algorithm is a finite sequence of well-defined, step-by-step
instructions used to solve a problem or perform a specific task.
Key Characteristics of an Algorithm (with examples)
1. Input
a. An algorithm takes zero or more inputs.
b. Example: Input numbers in a sorting algorithm.
2. Output
CO,   a. Produces at least one output.
b. Example: Sorted list as output of a sorting algorithm.   [5]
SO,BL
3. Definiteness (Unambiguity)
a. Each step must be clear and precisely defined.
b. Example: “Add two numbers” is clear, but “process
numbers” is vague.
4. Finiteness
a. Must terminate after a finite number of steps.
b. Example: Loop runs only until a condition is satisfied.
5. Effectiveness
a. Each step should be simple and executable in finite time.
b. Example:   Arithmetic   operations   like   addition,
comparison.
6. Correctness
a. Produces the correct output for all valid inputs.
b. Example: A searching algorithm returns the correct index.
********** 1 **********
--- page 2 ---
Marks: 1 mark for definition, any 4 key characteristics- 4 marks
CO,   b.   Explain the general process of divide-and-conquer method and give its [5]
SO,BL   control abstraction in pseudo-code.
Answer:
General divide and conquer method
•   Step 1. A problem is divided into several sub problems of the
same type, ideally of about equal size.
•   Step 2. The sub problems are solved (typically recursively,
though sometimes a different algorithm is employed, especially
when sub problems become small enough).
•   Step 3. If necessary, the solutions to the sub problems are
combined to get a solution to the original problem.
Algorithm:
Marks distribution:
General process- 2 marks;
control abstraction pseudocode- 3 marks
CO,   c.   Explain the concept of edge relaxation and its role in SSSP algorithms.   [5]
SO,BL
Solution: Edge relaxation is the core operation used in Single Source
Shortest Path (SSSP) algorithms to improve (or “relax”) the current
best-known distance to a vertex.
For an edge (u,v) with weight w:
If d[v]>d[u]+w(u,v),
then update: d[v]=d[u]+w(u,v)
•   d[u]: current shortest distance from source to u
•   d[v]: current shortest distance from source to v
Role in SSSP Algorithms
• Relaxes all edges repeatedly (|V| − 1 times)
• Can handle negative weights
Guarantees correct shortest paths even with negative edges
Marks: Explanation: 3 marks, role-2 marks
CO,   d.   Differentiate Backtracking from Brute Force. Explain the role of [5]
SO,BL   Bounding Function.
Solution:Any 4 differences-4Marks
Feature   Brute Force   Backtracking
Approach   Tries all combinations Prunes invalid
branches early
********** 2 **********

[Text in pictures on this page, read by OCR]
1 Algorithm DAndC(P)

2 {
3 if Small(P) then return S(P);

4 else

5

6 divide P into smaller instances P;, P2,...,P_, k > 1;

7 Apply DAndC to each of these subproblems;

8 return Combine(DAndC(P, ),DAndC(P2),...,DAndC(P,));
9
--- page 3 ---
Efficiency   Poor (exponential   Better (pruning
always)   reduces states)
State Space   Fully explored   Partially explored
Constraint   After full solution   At each step
Check
Role of Bounding Function (Bk): 1Mark
The bounding function determines whether a partial solution (x1, x2, ...,
xk) can possibly lead to a complete valid solution.
•   If Bk = true → continue expanding
•   If Bk = false → prune this branch, backtrack
A
i. Explain the set relationships between P, NP, NP-hard, and NP-
complete with a diagram.
ii. What do you mean by a non-deterministic machine?
iii. State any four meaningful differences between np-hard and np-
complete problems.
Solution:
i. Subset relation- 2marks
• P⊆NP
•   NP-complete ⊆ NP
•   NP-complete ⊆ NP-hard
•   NP-hard may include problems outside NP
Q2
CO,   [10]
SO,BL   Diagram- 2marks
ii. A non-deterministic machine is a theoretical model that:
• Can guess the correct solution instantly
• Then verifies it in polynomial time- (2marks)
iii. Differences- 1 mark for each difference
•   Definition: NP-Complete = NP + NP-Hard. NP-Hard does not require
being in NP.
•   Verification: NP-Complete problems are verifiable in polynomial
time. NP-Hard problems are not necessarily verifiable in polynomial
time.
• Problem Type: NP-Complete problems are usually decision problems
(yes/no). NP-Hard problems can be optimization, search, or decision
problems.
•   Relationship: Every NP problem can be reduced to an NP-Hard
problem in polynomial time.
CO,   B   For the given two sequences: X = "ABCBDAB" and Y = "GBDCAB":
SO,BL   i. Construct the LCS table using dynamic programming   [10]
ii. Find any one LCS
********** 3 **********
--- page 4 ---
iii. Give the pseudo-code for LCS
Sol:
LCS: BCAB/BDAB/BCBA
Pseudo-code for LCS:
Marks: Table construction-4 marks, LCS – 1-mark, Pseudo-code -5
marks
A   i. A relief organization want to supply food for disaster relief based on
their nutritional value. They have a truck that can carry maximum (M)
Q3   200 kg of the food items. Available food items such as Rice (100 kg),
CO,   Wheat Flour (70 kg), Beans (50 Kg) and Milk Powder (40 kg) with [10]
SO,BL   their nutritional values (450, 500, 300, 380) respectively. Identify how
can the truck be loaded with maximum nutritional value, considering
food can be split into smaller portions.
********** 4 **********

[Text in pictures on this page, read by OCR]
LCS-LENGTH(X, Y)

1 m= X. length

2 n= /Y.length

3 let b[1..m,1..n] and c[0..m,0..n] be new tables
4 fori = 1tom

5 c[i, 0] = 0

6 for 7 = Oton

7 c[0, 7] =0

8 fori = ltom

9 for j = lton

10 if x; == y;

11 cli, fj] =cfi-1,f-—1)+1
12 bli, J) = “N°

13 elseif c{i —1, 7] => cli, 7 —1]
14 cli, j] = cfi-1, J]

15 bli, j] = “t”

16 else c[i, j] = ci, j — 1]

17 bj, j] =“<”

18 return c and b
--- page 5 ---
ii. Identify the highest total nutritional value obtained, considering the
given constraint.
iii. Can this problem be classified as optimization problem? Why or why
not?
Sol: The problem can be solved as fractional knapsack problem.
Find the ratio and sort in descending order
1. Milk Powder → 9.5
2. Wheat Flour → 7.14
3. Beans → 6.0
4. Rice → 4.5
Fill the truck with each type of food in the order of ratio.
Final solution
• Milk Powder → Full
• Wheat Flour → Full
• Beans → Full
• Rice → 40% (partial)
(5 marks)
Total Nutritional value= 380 + 500 + 300 + 180 = 1360 (2 marks)
Yes, this problem be classified as optimization problem as it has
maximization problem with a given constraint. (3 marks)
B   Analyze the recurrence relation 𝑇(𝑛) = 𝑇( 𝑛 2) + 𝑛2 by constructing a [10]
recursion tree to determine the asymptotic upper bound. Further, verify
the obtained bound using the substitution method.
Answer:
𝑛2
𝑛 2
2
𝑛 2
4
CO,   𝑛 2
SO, BL   8
.......
1
2
𝑇(𝑛) = 𝑛2 + (𝑛 2) + (𝑛 4)2 + ⋯. .
1   1
𝑇(𝑛) = 𝑛2 (1 + + + ⋯. . )
4 16
********** 5 **********
--- page 6 ---
𝑇ℎ𝑒 𝐸𝑞𝑢𝑎𝑡𝑖𝑜𝑛 𝑖𝑠 𝑖𝑛 𝐺. 𝑃 𝑠𝑒𝑟𝑖𝑒𝑠
1   4
= 𝑛2.   = 𝑛2
1 −1 3
4
Therefore the complexity is 𝑂(𝑛2)
Substitution method:
𝑇(𝑛) <= 𝑐. 𝑔(𝑛)
𝑇(𝑛) <= 𝑐. 𝑛^2
Substitute into recurrence:
𝑇(𝑛) = 𝑇(𝑛 2) + 𝑛2
2
≤ 𝑐. (𝑛 2) + 𝑛2
≤ 𝑛2 (𝑐 + 1)
4
(𝑐 + 1) ≤𝐶= 1 ≤3𝑐
4   4
𝑇ℎ𝑒𝑟𝑒𝑓𝑜𝑟𝑒 𝐶≥ 4 𝑎𝑛𝑑 𝑇(𝑛) = 𝑂(𝑛2),
3
The asymptotic upper bound is quadratic.
Marks: 5 marks for recursion tree time complexity
5 marks for substitution verification.
A   For the following given graph:   [10]
Q4
CO,
SO,BL
i.   Compute the minimum cost from S to T using forward method
in dynamic programming.
ii.   Trace the optimal path.
iii.   Discuss the recurrence relation for solving a multistage graph
using the forward approach in dynamic programming.
Sol:
********** 6 **********
--- page 7 ---
recurrence relation:
Marks: computing cost stage-wise: 5 marks, optimal path tracing: 2
marks, recurrence relation: 3 marks
B   Given the following jobs:   [10]
Job   Deadline   Profit
J1   5   80
J2   3   60
J3   4   70
J4   2   65
J5   1   25
CO,SO,   J6   3   30
BL   i. Using the Greedy approach, determine the optimal job sequence
that maximizes total profit.
ii. Give the pseudo-code for the given problem
iii. Also discuss the algorithm's time complexity.
Solution:
Optimal job sequence: J5 → J4 → J2 → J3 → J1
Maximum Profit Calculation= 25 + 65 + 60 + 70 + 80= 300
********** 7 **********
--- page 8 ---
Pseudo-Code
Time Complexity
1. Sorting:
• Sorting jobs by profit → O(n log n)
2. Slot Allocation:
• For each job, checking slots → O(n × d)
(where d = maximum deadline)
• Worst case: O(n²)
Marks: Solution- 4 marks, Complexity- 2 marks, pseudo-code-4
marks
A   Discuss the N-Queens Problem conceptually. Explain how   [10]
Backtracking reduces the search space. Trace the state space tree
solution for N=4, step by step.
Solution:
N-Queens Concept- 2Marks
The N-Queens problem belongs to the class of Constraint Satisfaction
Problems (CSP). The goal is not to optimize a value but to find all
configurations satisfying a set of constraints.
The Problem is hard because
• For N=8: Brute force = 8⁸ = 16,777,216 possibilities
Q5   • Even with distinct columns (8!): 40,320 possibilities
CO,   • Backtracking reduces this to checking only ~2000 nodesBack
SO,BL
How Backtracking reduces the search space- 3marks
Backtracking Reduces the search space by
Step 1 — Early Detection: Constraints are checked at each placement,
not after all N queens are placed.
Step 2 — Pruning: If placing a queen at position (k, i) violates any
constraint, the entire subtree below that node is abandoned
immediately.
Step 3 — Systematic Exploration: The algorithm ensures every valid
solution is found without redundant checks.
Tracing of 4 Queen- 5marks
Should include Explicit and implicit conditions and stsep by step tracing
for the solution
********** 8 **********

[Text in pictures on this page, read by OCR]
1 Algorithm GreedyJob(d, J,n)
2 // Jisaset of jobs that can be completed by their deadlines.

3

4 J :={1}5

5 for i := 2 to n do

6

7 if (all jobs in J U {i} can be completed

8 by their deadlines) then J := J U {i};
9
--- page 9 ---
B   A delivery truck has a maximum capacity of 10 units. The items   [10]
available are:
Item   Weight   Profit
1   2   20
2   3   30
3   5   50
4   7   70
a) Build the DP table step-by-step. (6 marks)
c) Compute the maximum achievable profit. (2 marks)
d) Trace back and list the selected items. (2 marks)
Sol:
Let 𝑑𝑝[𝑖][𝑤] denote the maximum profit using first 𝑖 items with
CO,   capacity 𝑤.
SO,BL   i \ w   0   1   2   3   4   5   6   7   8   9   10
0   0   0   0   0   0   0   0   0   0   0   0
1   0   0   20   20   20   20   20   20   20   20   20
2   0   0   20   30   30   50   50   50   50   50   50
3   0   0   20   30   30   50   50   70   80   80   100
4   0   0   20   30   30   50   50   70   80   90   100
c) Maximum Profit (2 Marks)
Maximum Profit=𝟏𝟎𝟎Maximum Profit=𝟏𝟎𝟎
d) Selected Items (2 Marks)
Backtracking from
𝑑𝑝[4][10]=100:
********** 9 **********

[Text in pictures on this page, read by OCR]
A 3 / \ 8

2 a Q 4 2 & Q
a a = 8 it [o}
[\\ 7. .

23 44 3 4
a a
a a
71\ Fes
1
[ol
a
a
solution

FIGURE 12.2 State-space tree of solving the four-queens problem by backtracking.
x denotes an unsuccessful attempt to place a queen in the indicated
column. The numbers above the nodes indicate the order in which the
nodes are generated.
--- page 10 ---
• Compare 𝑑𝑝[4][10] with 𝑑𝑝[3][10]→ same ⇒ Item 4 not
selected
• Move to 𝑑𝑝[3][10]=100dp[3][10]=100:
 𝑑𝑝[3][10]≠𝑑𝑝[2][10]dp[3][10]≠dp[2][10]
⇒ Item 3 selected (weight = 5)
Remaining capacity = 10−5=510−5=5
At 𝑑𝑝[2][5]=50:
 𝑑𝑝[2][5]≠𝑑𝑝[1][5]
⇒ Item 2 selected (weight = 3)
Remaining capacity = 5−3=25−3=2
At 𝑑𝑝[1][2]=20: ⇒ Item 1 selected
A   Apply Quick Sort to the sequence of letters E, X, A, M, P, L, E by
selecting the first element as the pivot. Show the arrangement of
elements after each partition process. Further, derive the recurrence
relations for the best, average, and worst cases of the algorithm.
Answer:
E, X, A, M, P, L, E
Q6
[10]
CO,
SO,BL   Let T(n) be the time complexity.
1. Best Case: 𝑇(𝑛) = 2𝑇( 𝑛 2) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛𝑙𝑜𝑔𝑛)
2. Average Case:
𝑇(𝑛) = 𝑇(𝑘) + 𝑇(𝑛−𝑘−1) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛𝑙𝑜𝑔𝑛)
3. Worst Case: 𝑇(𝑛) = 𝑇(𝑛−1) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛2)
Marks: Quicksort application - 4 marks
Recurrence equations and complexity - 6 marks (2+2+2)
CO,   B   i. Compute the time complexity of the recurrence relation 𝑇(𝑛) =   [10]
SO,BL   4𝑇(√𝑛) + log2 𝑛
********** 10 **********
--- page 11 ---
(5 marks)
ii. Compute the time complexity of the code segment given below
𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛()
{
𝑖𝑛𝑡 𝑖= 1;
𝑤ℎ𝑖𝑙𝑒 (𝑖 < 𝑛)
{
𝑖𝑛𝑡 𝑗= 𝑛;
𝑤ℎ𝑖𝑙𝑒(𝑗 > 0)
𝑗 = 𝑗/2;
𝑖= 2 ∗𝑖;
} //𝑒𝑛𝑑 𝑜𝑓 𝑖
}
Answer:
T(n) = (log 𝑛∗log 𝑛) = log2 𝑛 (5 marks)
A   Design a recursive algorithm to find the minimum and maximum
Q7   element in the array-using divide and conquer. Find the its time
CO,   complexity and trace the algorithm for the given array a=[ 22, 13, -5, - [10]
SO,BL   8, 15, 60, 17, 31, 47].
********** 11 **********
--- page 12 ---
answer
𝑇(𝑛) = 2𝑇( 𝑛 2) + 𝐶 𝑂(𝑛)
Marks: 5 marks for algorithm, 3 marks for application and 2 marks
for time complexity.
B   Consider three algorithms X, Y and Z. and the run-time complexities are
𝑇𝑋= 5𝑛, 𝑇𝑌= 5 log10 𝑛, 𝑎𝑛𝑑 𝑇𝑍= 𝑛2. Compare the growth rates of
three algorithms when the input size increases from n=10 to n=1000.Plot
the graph and identify which algorithm performs better based on their
growth rates.
CO,   Answer:
[5]
SO,BL   Step 1: Given Time Complexities
• Algorithm X: 𝑇𝑋= 5𝑛
• Algorithm Y: 𝑇𝑌= 5 log10 𝑛
• Algorithm Z:𝑇𝑍= 𝑛2
Step 2: Values at Key Input Sizes
n   𝑇𝑋= 5𝑛 𝑇𝑌= 5 log10 𝑛 𝑇𝑍= 𝑛2
10   50   5   100
********** 12 **********

[Text in pictures on this page, read by OCR]
2 // all: nj is a global a Parameters é@ and j are integers,
1 i

3 = jain, The effect is to set yan and rrire to the
4 // largest and smallest values in ali ; j], respectively.

5

6 t if G — 7) then rnau rise :— alt}; // Small(?)

7 else if (i = j 1) then // Another case of Small(7?)
8

9 if (ali) []) then

10 {

1 max := ali]; nvin :—~ alz]s

12 7

13s else

da

iS max >— alt}; min :— aly];

16

17

18 else

19 { // ACP is not small, divide P into subprotlems.
20 // Find where to split the set.

21 mid i= ((@+ 7)/243

22 // Solve the subproblems.

Q3 MaxMin(é, mid, mea, mir);


25 // Combine the solutions.

26 if (maa << rnarl) then saw 2 reel;
27 if (min = min i) them min :— mini;

28 }

29 }
--- page 13 ---
100   500   10   10,000
1000 5000   15   1,000,000
Step 3: Growth Rate Observation
• Logarithmic growth increases very slowly.
• Linear growth increases proportionally with n.
• Quadratic growth increases very rapidly as n grows.
From the table and graph:
• 𝑇𝑌= 5 log10 𝑛 Grows slowest.
• 𝑇𝑋= 5𝑛 Grows moderately.
• 𝑇𝑍= 𝑛2 Grows fastest.
Step 4: Conclusion
Based on the rate of growth: 𝑇𝑌< 𝑇𝑋< 𝑇𝑍
• Best Algorithm: Y (logarithmic complexity)
• Moderate: X (linear complexity)
• Worst for large inputs: Z (quadratic complexity)
So, when the input size increases from 10 to 1000, Algorithm Y
performs the best because its running time increases very slowly
compared to the other two algorithms.
Marks: calculation 1 marks, plot the graph 1 marks better
algorithm growth rate 3 marks.
C   State the two important properties based on which we can decide that a
problem can be solved using greedy approach.
Solution: A problem can be solved using a greedy approach if it
CO,   satisfies:
1. Greedy Choice Property – A locally optimal choice leads to a   [5]
SO,BL
globally optimal solution.
2. Optimal Substructure – The optimal solution can be constructed
from optimal solutions of subproblems.
Marks: Each property correct explanation- 2.5 marks each
********** 13 **********

[Text in pictures on this page, read by OCR]
10

20

ee Growth Rate Comparison of Algorithms X, Y, and Z

— 1 x=5n
— TY =Slegiaim
— Tz=n72

fy 200 400 600 ‘200 1000
Input Size (n>
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper e04d8ab24cd2

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Computer_7002/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C071)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (13 pages)
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 16 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data, if necessary.
Q1
Answer briefly:   Marks
a.   Define an algorithm. Explain its key characteristics with suitable
examples.
Answer:
An algorithm is a finite sequence of well-defined, step-by-step
instructions used to solve a problem or perform a specific task.
Key Characteristics of an Algorithm (with examples)
1. Input
a. An algorithm takes zero or more inputs.
b. Example: Input numbers in a sorting algorithm.
2. Output
CO,   a. Produces at least one output.
b. Example: Sorted list as output of a sorting algorithm.   [5]
SO,BL
3. Definiteness (Unambiguity)
a. Each step must be clear and precisely defined.
b. Example: “Add two numbers” is clear, but “process
numbers” is vague.
4. Finiteness
a. Must terminate after a finite number of steps.
b. Example: Loop runs only until a condition is satisfied.
5. Effectiveness
a. Each step should be simple and executable in finite time.
b. Example:   Arithmetic   operations   like   addition,
comparison.
6. Correctness
a. Produces the correct output for all valid inputs.
b. Example: A searching algorithm returns the correct index.
********** 1 **********
--- page 2 ---
Marks: 1 mark for definition, any 4 key characteristics- 4 marks
CO,   b.   Explain the general process of divide-and-conquer method and give its [5]
SO,BL   control abstraction in pseudo-code.
Answer:
General divide and conquer method
•   Step 1. A problem is divided into several sub problems of the
same type, ideally of about equal size.
•   Step 2. The sub problems are solved (typically recursively,
though sometimes a different algorithm is employed, especially
when sub problems become small enough).
•   Step 3. If necessary, the solutions to the sub problems are
combined to get a solution to the original problem.
Algorithm:
Marks distribution:
General process- 2 marks;
control abstraction pseudocode- 3 marks
CO,   c.   Explain the concept of edge relaxation and its role in SSSP algorithms.   [5]
SO,BL
Solution: Edge relaxation is the core operation used in Single Source
Shortest Path (SSSP) algorithms to improve (or “relax”) the current
best-known distance to a vertex.
For an edge (u,v) with weight w:
If d[v]>d[u]+w(u,v),
then update: d[v]=d[u]+w(u,v)
•   d[u]: current shortest distance from source to u
•   d[v]: current shortest distance from source to v
Role in SSSP Algorithms
• Relaxes all edges repeatedly (|V| − 1 times)
• Can handle negative weights
Guarantees correct shortest paths even with negative edges
Marks: Explanation: 3 marks, role-2 marks
CO,   d.   Differentiate Backtracking from Brute Force. Explain the role of [5]
SO,BL   Bounding Function.
Solution:Any 4 differences-4Marks
Feature   Brute Force   Backtracking
Approach   Tries all combinations Prunes invalid
branches early
********** 2 **********

[Text in pictures on this page, read by OCR]
1 Algorithm DAndC(P)

2 {
3 if Small(P) then return S(P);

4 else

5

6 divide P into smaller instances P;, P2,...,P_, k > 1;

7 Apply DAndC to each of these subproblems;

8 return Combine(DAndC(P, ),DAndC(P2),...,DAndC(P,));
9
--- page 3 ---
Efficiency   Poor (exponential   Better (pruning
always)   reduces states)
State Space   Fully explored   Partially explored
Constraint   After full solution   At each step
Check
Role of Bounding Function (Bk): 1Mark
The bounding function determines whether a partial solution (x1, x2, ...,
xk) can possibly lead to a complete valid solution.
•   If Bk = true → continue expanding
•   If Bk = false → prune this branch, backtrack
A
i. Explain the set relationships between P, NP, NP-hard, and NP-
complete with a diagram.
ii. What do you mean by a non-deterministic machine?
iii. State any four meaningful differences between np-hard and np-
complete problems.
Solution:
i. Subset relation- 2marks
• P⊆NP
•   NP-complete ⊆ NP
•   NP-complete ⊆ NP-hard
•   NP-hard may include problems outside NP
Q2
CO,   [10]
SO,BL   Diagram- 2marks
ii. A non-deterministic machine is a theoretical model that:
• Can guess the correct solution instantly
• Then verifies it in polynomial time- (2marks)
iii. Differences- 1 mark for each difference
•   Definition: NP-Complete = NP + NP-Hard. NP-Hard does not require
being in NP.
•   Verification: NP-Complete problems are verifiable in polynomial
time. NP-Hard problems are not necessarily verifiable in polynomial
time.
• Problem Type: NP-Complete problems are usually decision problems
(yes/no). NP-Hard problems can be optimization, search, or decision
problems.
•   Relationship: Every NP problem can be reduced to an NP-Hard
problem in polynomial time.
CO,   B   For the given two sequences: X = "ABCBDAB" and Y = "GBDCAB":
SO,BL   i. Construct the LCS table using dynamic programming   [10]
ii. Find any one LCS
********** 3 **********
--- page 4 ---
iii. Give the pseudo-code for LCS
Sol:
LCS: BCAB/BDAB/BCBA
Pseudo-code for LCS:
Marks: Table construction-4 marks, LCS – 1-mark, Pseudo-code -5
marks
A   i. A relief organization want to supply food for disaster relief based on
their nutritional value. They have a truck that can carry maximum (M)
Q3   200 kg of the food items. Available food items such as Rice (100 kg),
CO,   Wheat Flour (70 kg), Beans (50 Kg) and Milk Powder (40 kg) with [10]
SO,BL   their nutritional values (450, 500, 300, 380) respectively. Identify how
can the truck be loaded with maximum nutritional value, considering
food can be split into smaller portions.
********** 4 **********

[Text in pictures on this page, read by OCR]
LCS-LENGTH(X, Y)

1 m= X. length

2 n= /Y.length

3 let b[1..m,1..n] and c[0..m,0..n] be new tables
4 fori = 1tom

5 c[i, 0] = 0

6 for 7 = Oton

7 c[0, 7] =0

8 fori = ltom

9 for j = lton

10 if x; == y;

11 cli, fj] =cfi-1,f-—1)+1
12 bli, J) = “N°

13 elseif c{i —1, 7] => cli, 7 —1]
14 cli, j] = cfi-1, J]

15 bli, j] = “t”

16 else c[i, j] = ci, j — 1]

17 bj, j] =“<”

18 return c and b
--- page 5 ---
ii. Identify the highest total nutritional value obtained, considering the
given constraint.
iii. Can this problem be classified as optimization problem? Why or why
not?
Sol: The problem can be solved as fractional knapsack problem.
Find the ratio and sort in descending order
1. Milk Powder → 9.5
2. Wheat Flour → 7.14
3. Beans → 6.0
4. Rice → 4.5
Fill the truck with each type of food in the order of ratio.
Final solution
• Milk Powder → Full
• Wheat Flour → Full
• Beans → Full
• Rice → 40% (partial)
(5 marks)
Total Nutritional value= 380 + 500 + 300 + 180 = 1360 (2 marks)
Yes, this problem be classified as optimization problem as it has
maximization problem with a given constraint. (3 marks)
B   Analyze the recurrence relation 𝑇(𝑛) = 𝑇( 𝑛 2) + 𝑛2 by constructing a [10]
recursion tree to determine the asymptotic upper bound. Further, verify
the obtained bound using the substitution method.
Answer:
𝑛2
𝑛 2
2
𝑛 2
4
CO,   𝑛 2
SO, BL   8
.......
1
2
𝑇(𝑛) = 𝑛2 + (𝑛 2) + (𝑛 4)2 + ⋯. .
1   1
𝑇(𝑛) = 𝑛2 (1 + + + ⋯. . )
4 16
********** 5 **********
--- page 6 ---
𝑇ℎ𝑒 𝐸𝑞𝑢𝑎𝑡𝑖𝑜𝑛 𝑖𝑠 𝑖𝑛 𝐺. 𝑃 𝑠𝑒𝑟𝑖𝑒𝑠
1   4
= 𝑛2.   = 𝑛2
1 −1 3
4
Therefore the complexity is 𝑂(𝑛2)
Substitution method:
𝑇(𝑛) <= 𝑐. 𝑔(𝑛)
𝑇(𝑛) <= 𝑐. 𝑛^2
Substitute into recurrence:
𝑇(𝑛) = 𝑇(𝑛 2) + 𝑛2
2
≤ 𝑐. (𝑛 2) + 𝑛2
≤ 𝑛2 (𝑐 + 1)
4
(𝑐 + 1) ≤𝐶= 1 ≤3𝑐
4   4
𝑇ℎ𝑒𝑟𝑒𝑓𝑜𝑟𝑒 𝐶≥ 4 𝑎𝑛𝑑 𝑇(𝑛) = 𝑂(𝑛2),
3
The asymptotic upper bound is quadratic.
Marks: 5 marks for recursion tree time complexity
5 marks for substitution verification.
A   For the following given graph:   [10]
Q4
CO,
SO,BL
i.   Compute the minimum cost from S to T using forward method
in dynamic programming.
ii.   Trace the optimal path.
iii.   Discuss the recurrence relation for solving a multistage graph
using the forward approach in dynamic programming.
Sol:
********** 6 **********
--- page 7 ---
recurrence relation:
Marks: computing cost stage-wise: 5 marks, optimal path tracing: 2
marks, recurrence relation: 3 marks
B   Given the following jobs:   [10]
Job   Deadline   Profit
J1   5   80
J2   3   60
J3   4   70
J4   2   65
J5   1   25
CO,SO,   J6   3   30
BL   i. Using the Greedy approach, determine the optimal job sequence
that maximizes total profit.
ii. Give the pseudo-code for the given problem
iii. Also discuss the algorithm's time complexity.
Solution:
Optimal job sequence: J5 → J4 → J2 → J3 → J1
Maximum Profit Calculation= 25 + 65 + 60 + 70 + 80= 300
********** 7 **********
--- page 8 ---
Pseudo-Code
Time Complexity
1. Sorting:
• Sorting jobs by profit → O(n log n)
2. Slot Allocation:
• For each job, checking slots → O(n × d)
(where d = maximum deadline)
• Worst case: O(n²)
Marks: Solution- 4 marks, Complexity- 2 marks, pseudo-code-4
marks
A   Discuss the N-Queens Problem conceptually. Explain how   [10]
Backtracking reduces the search space. Trace the state space tree
solution for N=4, step by step.
Solution:
N-Queens Concept- 2Marks
The N-Queens problem belongs to the class of Constraint Satisfaction
Problems (CSP). The goal is not to optimize a value but to find all
configurations satisfying a set of constraints.
The Problem is hard because
• For N=8: Brute force = 8⁸ = 16,777,216 possibilities
Q5   • Even with distinct columns (8!): 40,320 possibilities
CO,   • Backtracking reduces this to checking only ~2000 nodesBack
SO,BL
How Backtracking reduces the search space- 3marks
Backtracking Reduces the search space by
Step 1 — Early Detection: Constraints are checked at each placement,
not after all N queens are placed.
Step 2 — Pruning: If placing a queen at position (k, i) violates any
constraint, the entire subtree below that node is abandoned
immediately.
Step 3 — Systematic Exploration: The algorithm ensures every valid
solution is found without redundant checks.
Tracing of 4 Queen- 5marks
Should include Explicit and implicit conditions and stsep by step tracing
for the solution
********** 8 **********

[Text in pictures on this page, read by OCR]
1 Algorithm GreedyJob(d, J,n)
2 // Jisaset of jobs that can be completed by their deadlines.

3

4 J :={1}5

5 for i := 2 to n do

6

7 if (all jobs in J U {i} can be completed

8 by their deadlines) then J := J U {i};
9
--- page 9 ---
B   A delivery truck has a maximum capacity of 10 units. The items   [10]
available are:
Item   Weight   Profit
1   2   20
2   3   30
3   5   50
4   7   70
a) Build the DP table step-by-step. (6 marks)
c) Compute the maximum achievable profit. (2 marks)
d) Trace back and list the selected items. (2 marks)
Sol:
Let 𝑑𝑝[𝑖][𝑤] denote the maximum profit using first 𝑖 items with
CO,   capacity 𝑤.
SO,BL   i \ w   0   1   2   3   4   5   6   7   8   9   10
0   0   0   0   0   0   0   0   0   0   0   0
1   0   0   20   20   20   20   20   20   20   20   20
2   0   0   20   30   30   50   50   50   50   50   50
3   0   0   20   30   30   50   50   70   80   80   100
4   0   0   20   30   30   50   50   70   80   90   100
c) Maximum Profit (2 Marks)
Maximum Profit=𝟏𝟎𝟎Maximum Profit=𝟏𝟎𝟎
d) Selected Items (2 Marks)
Backtracking from
𝑑𝑝[4][10]=100:
********** 9 **********

[Text in pictures on this page, read by OCR]
A 3 / \ 8

2 a Q 4 2 & Q
a a = 8 it [o}
[\\ 7. .

23 44 3 4
a a
a a
71\ Fes
1
[ol
a
a
solution

FIGURE 12.2 State-space tree of solving the four-queens problem by backtracking.
x denotes an unsuccessful attempt to place a queen in the indicated
column. The numbers above the nodes indicate the order in which the
nodes are generated.
--- page 10 ---
• Compare 𝑑𝑝[4][10] with 𝑑𝑝[3][10]→ same ⇒ Item 4 not
selected
• Move to 𝑑𝑝[3][10]=100dp[3][10]=100:
 𝑑𝑝[3][10]≠𝑑𝑝[2][10]dp[3][10]≠dp[2][10]
⇒ Item 3 selected (weight = 5)
Remaining capacity = 10−5=510−5=5
At 𝑑𝑝[2][5]=50:
 𝑑𝑝[2][5]≠𝑑𝑝[1][5]
⇒ Item 2 selected (weight = 3)
Remaining capacity = 5−3=25−3=2
At 𝑑𝑝[1][2]=20: ⇒ Item 1 selected
A   Apply Quick Sort to the sequence of letters E, X, A, M, P, L, E by
selecting the first element as the pivot. Show the arrangement of
elements after each partition process. Further, derive the recurrence
relations for the best, average, and worst cases of the algorithm.
Answer:
E, X, A, M, P, L, E
Q6
[10]
CO,
SO,BL   Let T(n) be the time complexity.
1. Best Case: 𝑇(𝑛) = 2𝑇( 𝑛 2) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛𝑙𝑜𝑔𝑛)
2. Average Case:
𝑇(𝑛) = 𝑇(𝑘) + 𝑇(𝑛−𝑘−1) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛𝑙𝑜𝑔𝑛)
3. Worst Case: 𝑇(𝑛) = 𝑇(𝑛−1) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛2)
Marks: Quicksort application - 4 marks
Recurrence equations and complexity - 6 marks (2+2+2)
CO,   B   i. Compute the time complexity of the recurrence relation 𝑇(𝑛) =   [10]
SO,BL   4𝑇(√𝑛) + log2 𝑛
********** 10 **********
--- page 11 ---
(5 marks)
ii. Compute the time complexity of the code segment given below
𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛()
{
𝑖𝑛𝑡 𝑖= 1;
𝑤ℎ𝑖𝑙𝑒 (𝑖 < 𝑛)
{
𝑖𝑛𝑡 𝑗= 𝑛;
𝑤ℎ𝑖𝑙𝑒(𝑗 > 0)
𝑗 = 𝑗/2;
𝑖= 2 ∗𝑖;
} //𝑒𝑛𝑑 𝑜𝑓 𝑖
}
Answer:
T(n) = (log 𝑛∗log 𝑛) = log2 𝑛 (5 marks)
A   Design a recursive algorithm to find the minimum and maximum
Q7   element in the array-using divide and conquer. Find the its time
CO,   complexity and trace the algorithm for the given array a=[ 22, 13, -5, - [10]
SO,BL   8, 15, 60, 17, 31, 47].
********** 11 **********
--- page 12 ---
answer
𝑇(𝑛) = 2𝑇( 𝑛 2) + 𝐶 𝑂(𝑛)
Marks: 5 marks for algorithm, 3 marks for application and 2 marks
for time complexity.
B   Consider three algorithms X, Y and Z. and the run-time complexities are
𝑇𝑋= 5𝑛, 𝑇𝑌= 5 log10 𝑛, 𝑎𝑛𝑑 𝑇𝑍= 𝑛2. Compare the growth rates of
three algorithms when the input size increases from n=10 to n=1000.Plot
the graph and identify which algorithm performs better based on their
growth rates.
CO,   Answer:
[5]
SO,BL   Step 1: Given Time Complexities
• Algorithm X: 𝑇𝑋= 5𝑛
• Algorithm Y: 𝑇𝑌= 5 log10 𝑛
• Algorithm Z:𝑇𝑍= 𝑛2
Step 2: Values at Key Input Sizes
n   𝑇𝑋= 5𝑛 𝑇𝑌= 5 log10 𝑛 𝑇𝑍= 𝑛2
10   50   5   100
********** 12 **********

[Text in pictures on this page, read by OCR]
2 // all: nj is a global a Parameters é@ and j are integers,
1 i

3 = jain, The effect is to set yan and rrire to the
4 // largest and smallest values in ali ; j], respectively.

5

6 t if G — 7) then rnau rise :— alt}; // Small(?)

7 else if (i = j 1) then // Another case of Small(7?)
8

9 if (ali) []) then

10 {

1 max := ali]; nvin :—~ alz]s

12 7

13s else

da

iS max >— alt}; min :— aly];

16

17

18 else

19 { // ACP is not small, divide P into subprotlems.
20 // Find where to split the set.

21 mid i= ((@+ 7)/243

22 // Solve the subproblems.

Q3 MaxMin(é, mid, mea, mir);


25 // Combine the solutions.

26 if (maa << rnarl) then saw 2 reel;
27 if (min = min i) them min :— mini;

28 }

29 }
--- page 13 ---
100   500   10   10,000
1000 5000   15   1,000,000
Step 3: Growth Rate Observation
• Logarithmic growth increases very slowly.
• Linear growth increases proportionally with n.
• Quadratic growth increases very rapidly as n grows.
From the table and graph:
• 𝑇𝑌= 5 log10 𝑛 Grows slowest.
• 𝑇𝑋= 5𝑛 Grows moderately.
• 𝑇𝑍= 𝑛2 Grows fastest.
Step 4: Conclusion
Based on the rate of growth: 𝑇𝑌< 𝑇𝑋< 𝑇𝑍
• Best Algorithm: Y (logarithmic complexity)
• Moderate: X (linear complexity)
• Worst for large inputs: Z (quadratic complexity)
So, when the input size increases from 10 to 1000, Algorithm Y
performs the best because its running time increases very slowly
compared to the other two algorithms.
Marks: calculation 1 marks, plot the graph 1 marks better
algorithm growth rate 3 marks.
C   State the two important properties based on which we can decide that a
problem can be solved using greedy approach.
Solution: A problem can be solved using a greedy approach if it
CO,   satisfies:
1. Greedy Choice Property – A locally optimal choice leads to a   [5]
SO,BL
globally optimal solution.
2. Optimal Substructure – The optimal solution can be constructed
from optimal solutions of subproblems.
Marks: Each property correct explanation- 2.5 marks each
********** 13 **********

[Text in pictures on this page, read by OCR]
10

20

ee Growth Rate Comparison of Algorithms X, Y, and Z

— 1 x=5n
— TY =Slegiaim
— Tz=n72

fy 200 400 600 ‘200 1000
Input Size (n>
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 8fe5e7c57105

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_Computer_7047/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C071)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (13 pages)
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 16 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data, if necessary.
Q1
Answer briefly:   Marks
a.   Define an algorithm. Explain its key characteristics with suitable
examples.
Answer:
An algorithm is a finite sequence of well-defined, step-by-step
instructions used to solve a problem or perform a specific task.
Key Characteristics of an Algorithm (with examples)
1. Input
a. An algorithm takes zero or more inputs.
b. Example: Input numbers in a sorting algorithm.
2. Output
CO,   a. Produces at least one output.
b. Example: Sorted list as output of a sorting algorithm.   [5]
SO,BL
3. Definiteness (Unambiguity)
a. Each step must be clear and precisely defined.
b. Example: “Add two numbers” is clear, but “process
numbers” is vague.
4. Finiteness
a. Must terminate after a finite number of steps.
b. Example: Loop runs only until a condition is satisfied.
5. Effectiveness
a. Each step should be simple and executable in finite time.
b. Example:   Arithmetic   operations   like   addition,
comparison.
6. Correctness
a. Produces the correct output for all valid inputs.
b. Example: A searching algorithm returns the correct index.
********** 1 **********
--- page 2 ---
Marks: 1 mark for definition, any 4 key characteristics- 4 marks
CO,   b.   Explain the general process of divide-and-conquer method and give its [5]
SO,BL   control abstraction in pseudo-code.
Answer:
General divide and conquer method
•   Step 1. A problem is divided into several sub problems of the
same type, ideally of about equal size.
•   Step 2. The sub problems are solved (typically recursively,
though sometimes a different algorithm is employed, especially
when sub problems become small enough).
•   Step 3. If necessary, the solutions to the sub problems are
combined to get a solution to the original problem.
Algorithm:
Marks distribution:
General process- 2 marks;
control abstraction pseudocode- 3 marks
CO,   c.   Explain the concept of edge relaxation and its role in SSSP algorithms.   [5]
SO,BL
Solution: Edge relaxation is the core operation used in Single Source
Shortest Path (SSSP) algorithms to improve (or “relax”) the current
best-known distance to a vertex.
For an edge (u,v) with weight w:
If d[v]>d[u]+w(u,v),
then update: d[v]=d[u]+w(u,v)
•   d[u]: current shortest distance from source to u
•   d[v]: current shortest distance from source to v
Role in SSSP Algorithms
• Relaxes all edges repeatedly (|V| − 1 times)
• Can handle negative weights
Guarantees correct shortest paths even with negative edges
Marks: Explanation: 3 marks, role-2 marks
CO,   d.   Differentiate Backtracking from Brute Force. Explain the role of [5]
SO,BL   Bounding Function.
Solution:Any 4 differences-4Marks
Feature   Brute Force   Backtracking
Approach   Tries all combinations Prunes invalid
branches early
********** 2 **********

[Text in pictures on this page, read by OCR]
1 Algorithm DAndC(P)

2 {
3 if Small(P) then return S(P);

4 else

5

6 divide P into smaller instances P;, P2,...,P_, k > 1;

7 Apply DAndC to each of these subproblems;

8 return Combine(DAndC(P, ),DAndC(P2),...,DAndC(P,));
9
--- page 3 ---
Efficiency   Poor (exponential   Better (pruning
always)   reduces states)
State Space   Fully explored   Partially explored
Constraint   After full solution   At each step
Check
Role of Bounding Function (Bk): 1Mark
The bounding function determines whether a partial solution (x1, x2, ...,
xk) can possibly lead to a complete valid solution.
•   If Bk = true → continue expanding
•   If Bk = false → prune this branch, backtrack
A
i. Explain the set relationships between P, NP, NP-hard, and NP-
complete with a diagram.
ii. What do you mean by a non-deterministic machine?
iii. State any four meaningful differences between np-hard and np-
complete problems.
Solution:
i. Subset relation- 2marks
• P⊆NP
•   NP-complete ⊆ NP
•   NP-complete ⊆ NP-hard
•   NP-hard may include problems outside NP
Q2
CO,   [10]
SO,BL   Diagram- 2marks
ii. A non-deterministic machine is a theoretical model that:
• Can guess the correct solution instantly
• Then verifies it in polynomial time- (2marks)
iii. Differences- 1 mark for each difference
•   Definition: NP-Complete = NP + NP-Hard. NP-Hard does not require
being in NP.
•   Verification: NP-Complete problems are verifiable in polynomial
time. NP-Hard problems are not necessarily verifiable in polynomial
time.
• Problem Type: NP-Complete problems are usually decision problems
(yes/no). NP-Hard problems can be optimization, search, or decision
problems.
•   Relationship: Every NP problem can be reduced to an NP-Hard
problem in polynomial time.
CO,   B   For the given two sequences: X = "ABCBDAB" and Y = "GBDCAB":
SO,BL   i. Construct the LCS table using dynamic programming   [10]
ii. Find any one LCS
********** 3 **********
--- page 4 ---
iii. Give the pseudo-code for LCS
Sol:
LCS: BCAB/BDAB/BCBA
Pseudo-code for LCS:
Marks: Table construction-4 marks, LCS – 1-mark, Pseudo-code -5
marks
A   i. A relief organization want to supply food for disaster relief based on
their nutritional value. They have a truck that can carry maximum (M)
Q3   200 kg of the food items. Available food items such as Rice (100 kg),
CO,   Wheat Flour (70 kg), Beans (50 Kg) and Milk Powder (40 kg) with [10]
SO,BL   their nutritional values (450, 500, 300, 380) respectively. Identify how
can the truck be loaded with maximum nutritional value, considering
food can be split into smaller portions.
********** 4 **********

[Text in pictures on this page, read by OCR]
LCS-LENGTH(X, Y)

1 m= X. length

2 n= /Y.length

3 let b[1..m,1..n] and c[0..m,0..n] be new tables
4 fori = 1tom

5 c[i, 0] = 0

6 for 7 = Oton

7 c[0, 7] =0

8 fori = ltom

9 for j = lton

10 if x; == y;

11 cli, fj] =cfi-1,f-—1)+1
12 bli, J) = “N°

13 elseif c{i —1, 7] => cli, 7 —1]
14 cli, j] = cfi-1, J]

15 bli, j] = “t”

16 else c[i, j] = ci, j — 1]

17 bj, j] =“<”

18 return c and b
--- page 5 ---
ii. Identify the highest total nutritional value obtained, considering the
given constraint.
iii. Can this problem be classified as optimization problem? Why or why
not?
Sol: The problem can be solved as fractional knapsack problem.
Find the ratio and sort in descending order
1. Milk Powder → 9.5
2. Wheat Flour → 7.14
3. Beans → 6.0
4. Rice → 4.5
Fill the truck with each type of food in the order of ratio.
Final solution
• Milk Powder → Full
• Wheat Flour → Full
• Beans → Full
• Rice → 40% (partial)
(5 marks)
Total Nutritional value= 380 + 500 + 300 + 180 = 1360 (2 marks)
Yes, this problem be classified as optimization problem as it has
maximization problem with a given constraint. (3 marks)
B   Analyze the recurrence relation 𝑇(𝑛) = 𝑇( 𝑛 2) + 𝑛2 by constructing a [10]
recursion tree to determine the asymptotic upper bound. Further, verify
the obtained bound using the substitution method.
Answer:
𝑛2
𝑛 2
2
𝑛 2
4
CO,   𝑛 2
SO, BL   8
.......
1
2
𝑇(𝑛) = 𝑛2 + (𝑛 2) + (𝑛 4)2 + ⋯. .
1   1
𝑇(𝑛) = 𝑛2 (1 + + + ⋯. . )
4 16
********** 5 **********
--- page 6 ---
𝑇ℎ𝑒 𝐸𝑞𝑢𝑎𝑡𝑖𝑜𝑛 𝑖𝑠 𝑖𝑛 𝐺. 𝑃 𝑠𝑒𝑟𝑖𝑒𝑠
1   4
= 𝑛2.   = 𝑛2
1 −1 3
4
Therefore the complexity is 𝑂(𝑛2)
Substitution method:
𝑇(𝑛) <= 𝑐. 𝑔(𝑛)
𝑇(𝑛) <= 𝑐. 𝑛^2
Substitute into recurrence:
𝑇(𝑛) = 𝑇(𝑛 2) + 𝑛2
2
≤ 𝑐. (𝑛 2) + 𝑛2
≤ 𝑛2 (𝑐 + 1)
4
(𝑐 + 1) ≤𝐶= 1 ≤3𝑐
4   4
𝑇ℎ𝑒𝑟𝑒𝑓𝑜𝑟𝑒 𝐶≥ 4 𝑎𝑛𝑑 𝑇(𝑛) = 𝑂(𝑛2),
3
The asymptotic upper bound is quadratic.
Marks: 5 marks for recursion tree time complexity
5 marks for substitution verification.
A   For the following given graph:   [10]
Q4
CO,
SO,BL
i.   Compute the minimum cost from S to T using forward method
in dynamic programming.
ii.   Trace the optimal path.
iii.   Discuss the recurrence relation for solving a multistage graph
using the forward approach in dynamic programming.
Sol:
********** 6 **********
--- page 7 ---
recurrence relation:
Marks: computing cost stage-wise: 5 marks, optimal path tracing: 2
marks, recurrence relation: 3 marks
B   Given the following jobs:   [10]
Job   Deadline   Profit
J1   5   80
J2   3   60
J3   4   70
J4   2   65
J5   1   25
CO,SO,   J6   3   30
BL   i. Using the Greedy approach, determine the optimal job sequence
that maximizes total profit.
ii. Give the pseudo-code for the given problem
iii. Also discuss the algorithm's time complexity.
Solution:
Optimal job sequence: J5 → J4 → J2 → J3 → J1
Maximum Profit Calculation= 25 + 65 + 60 + 70 + 80= 300
********** 7 **********
--- page 8 ---
Pseudo-Code
Time Complexity
1. Sorting:
• Sorting jobs by profit → O(n log n)
2. Slot Allocation:
• For each job, checking slots → O(n × d)
(where d = maximum deadline)
• Worst case: O(n²)
Marks: Solution- 4 marks, Complexity- 2 marks, pseudo-code-4
marks
A   Discuss the N-Queens Problem conceptually. Explain how   [10]
Backtracking reduces the search space. Trace the state space tree
solution for N=4, step by step.
Solution:
N-Queens Concept- 2Marks
The N-Queens problem belongs to the class of Constraint Satisfaction
Problems (CSP). The goal is not to optimize a value but to find all
configurations satisfying a set of constraints.
The Problem is hard because
• For N=8: Brute force = 8⁸ = 16,777,216 possibilities
Q5   • Even with distinct columns (8!): 40,320 possibilities
CO,   • Backtracking reduces this to checking only ~2000 nodesBack
SO,BL
How Backtracking reduces the search space- 3marks
Backtracking Reduces the search space by
Step 1 — Early Detection: Constraints are checked at each placement,
not after all N queens are placed.
Step 2 — Pruning: If placing a queen at position (k, i) violates any
constraint, the entire subtree below that node is abandoned
immediately.
Step 3 — Systematic Exploration: The algorithm ensures every valid
solution is found without redundant checks.
Tracing of 4 Queen- 5marks
Should include Explicit and implicit conditions and stsep by step tracing
for the solution
********** 8 **********

[Text in pictures on this page, read by OCR]
1 Algorithm GreedyJob(d, J,n)
2 // Jisaset of jobs that can be completed by their deadlines.

3

4 J :={1}5

5 for i := 2 to n do

6

7 if (all jobs in J U {i} can be completed

8 by their deadlines) then J := J U {i};
9
--- page 9 ---
B   A delivery truck has a maximum capacity of 10 units. The items   [10]
available are:
Item   Weight   Profit
1   2   20
2   3   30
3   5   50
4   7   70
a) Build the DP table step-by-step. (6 marks)
c) Compute the maximum achievable profit. (2 marks)
d) Trace back and list the selected items. (2 marks)
Sol:
Let 𝑑𝑝[𝑖][𝑤] denote the maximum profit using first 𝑖 items with
CO,   capacity 𝑤.
SO,BL   i \ w   0   1   2   3   4   5   6   7   8   9   10
0   0   0   0   0   0   0   0   0   0   0   0
1   0   0   20   20   20   20   20   20   20   20   20
2   0   0   20   30   30   50   50   50   50   50   50
3   0   0   20   30   30   50   50   70   80   80   100
4   0   0   20   30   30   50   50   70   80   90   100
c) Maximum Profit (2 Marks)
Maximum Profit=𝟏𝟎𝟎Maximum Profit=𝟏𝟎𝟎
d) Selected Items (2 Marks)
Backtracking from
𝑑𝑝[4][10]=100:
********** 9 **********

[Text in pictures on this page, read by OCR]
A 3 / \ 8

2 a Q 4 2 & Q
a a = 8 it [o}
[\\ 7. .

23 44 3 4
a a
a a
71\ Fes
1
[ol
a
a
solution

FIGURE 12.2 State-space tree of solving the four-queens problem by backtracking.
x denotes an unsuccessful attempt to place a queen in the indicated
column. The numbers above the nodes indicate the order in which the
nodes are generated.
--- page 10 ---
• Compare 𝑑𝑝[4][10] with 𝑑𝑝[3][10]→ same ⇒ Item 4 not
selected
• Move to 𝑑𝑝[3][10]=100dp[3][10]=100:
 𝑑𝑝[3][10]≠𝑑𝑝[2][10]dp[3][10]≠dp[2][10]
⇒ Item 3 selected (weight = 5)
Remaining capacity = 10−5=510−5=5
At 𝑑𝑝[2][5]=50:
 𝑑𝑝[2][5]≠𝑑𝑝[1][5]
⇒ Item 2 selected (weight = 3)
Remaining capacity = 5−3=25−3=2
At 𝑑𝑝[1][2]=20: ⇒ Item 1 selected
A   Apply Quick Sort to the sequence of letters E, X, A, M, P, L, E by
selecting the first element as the pivot. Show the arrangement of
elements after each partition process. Further, derive the recurrence
relations for the best, average, and worst cases of the algorithm.
Answer:
E, X, A, M, P, L, E
Q6
[10]
CO,
SO,BL   Let T(n) be the time complexity.
1. Best Case: 𝑇(𝑛) = 2𝑇( 𝑛 2) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛𝑙𝑜𝑔𝑛)
2. Average Case:
𝑇(𝑛) = 𝑇(𝑘) + 𝑇(𝑛−𝑘−1) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛𝑙𝑜𝑔𝑛)
3. Worst Case: 𝑇(𝑛) = 𝑇(𝑛−1) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛2)
Marks: Quicksort application - 4 marks
Recurrence equations and complexity - 6 marks (2+2+2)
CO,   B   i. Compute the time complexity of the recurrence relation 𝑇(𝑛) =   [10]
SO,BL   4𝑇(√𝑛) + log2 𝑛
********** 10 **********
--- page 11 ---
(5 marks)
ii. Compute the time complexity of the code segment given below
𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛()
{
𝑖𝑛𝑡 𝑖= 1;
𝑤ℎ𝑖𝑙𝑒 (𝑖 < 𝑛)
{
𝑖𝑛𝑡 𝑗= 𝑛;
𝑤ℎ𝑖𝑙𝑒(𝑗 > 0)
𝑗 = 𝑗/2;
𝑖= 2 ∗𝑖;
} //𝑒𝑛𝑑 𝑜𝑓 𝑖
}
Answer:
T(n) = (log 𝑛∗log 𝑛) = log2 𝑛 (5 marks)
A   Design a recursive algorithm to find the minimum and maximum
Q7   element in the array-using divide and conquer. Find the its time
CO,   complexity and trace the algorithm for the given array a=[ 22, 13, -5, - [10]
SO,BL   8, 15, 60, 17, 31, 47].
********** 11 **********
--- page 12 ---
answer
𝑇(𝑛) = 2𝑇( 𝑛 2) + 𝐶 𝑂(𝑛)
Marks: 5 marks for algorithm, 3 marks for application and 2 marks
for time complexity.
B   Consider three algorithms X, Y and Z. and the run-time complexities are
𝑇𝑋= 5𝑛, 𝑇𝑌= 5 log10 𝑛, 𝑎𝑛𝑑 𝑇𝑍= 𝑛2. Compare the growth rates of
three algorithms when the input size increases from n=10 to n=1000.Plot
the graph and identify which algorithm performs better based on their
growth rates.
CO,   Answer:
[5]
SO,BL   Step 1: Given Time Complexities
• Algorithm X: 𝑇𝑋= 5𝑛
• Algorithm Y: 𝑇𝑌= 5 log10 𝑛
• Algorithm Z:𝑇𝑍= 𝑛2
Step 2: Values at Key Input Sizes
n   𝑇𝑋= 5𝑛 𝑇𝑌= 5 log10 𝑛 𝑇𝑍= 𝑛2
10   50   5   100
********** 12 **********

[Text in pictures on this page, read by OCR]
2 // all: nj is a global a Parameters é@ and j are integers,
1 i

3 = jain, The effect is to set yan and rrire to the
4 // largest and smallest values in ali ; j], respectively.

5

6 t if G — 7) then rnau rise :— alt}; // Small(?)

7 else if (i = j 1) then // Another case of Small(7?)
8

9 if (ali) []) then

10 {

1 max := ali]; nvin :—~ alz]s

12 7

13s else

da

iS max >— alt}; min :— aly];

16

17

18 else

19 { // ACP is not small, divide P into subprotlems.
20 // Find where to split the set.

21 mid i= ((@+ 7)/243

22 // Solve the subproblems.

Q3 MaxMin(é, mid, mea, mir);


25 // Combine the solutions.

26 if (maa << rnarl) then saw 2 reel;
27 if (min = min i) them min :— mini;

28 }

29 }
--- page 13 ---
100   500   10   10,000
1000 5000   15   1,000,000
Step 3: Growth Rate Observation
• Logarithmic growth increases very slowly.
• Linear growth increases proportionally with n.
• Quadratic growth increases very rapidly as n grows.
From the table and graph:
• 𝑇𝑌= 5 log10 𝑛 Grows slowest.
• 𝑇𝑋= 5𝑛 Grows moderately.
• 𝑇𝑍= 𝑛2 Grows fastest.
Step 4: Conclusion
Based on the rate of growth: 𝑇𝑌< 𝑇𝑋< 𝑇𝑍
• Best Algorithm: Y (logarithmic complexity)
• Moderate: X (linear complexity)
• Worst for large inputs: Z (quadratic complexity)
So, when the input size increases from 10 to 1000, Algorithm Y
performs the best because its running time increases very slowly
compared to the other two algorithms.
Marks: calculation 1 marks, plot the graph 1 marks better
algorithm growth rate 3 marks.
C   State the two important properties based on which we can decide that a
problem can be solved using greedy approach.
Solution: A problem can be solved using a greedy approach if it
CO,   satisfies:
1. Greedy Choice Property – A locally optimal choice leads to a   [5]
SO,BL
globally optimal solution.
2. Optimal Substructure – The optimal solution can be constructed
from optimal solutions of subproblems.
Marks: Each property correct explanation- 2.5 marks each
********** 13 **********

[Text in pictures on this page, read by OCR]
10

20

ee Growth Rate Comparison of Algorithms X, Y, and Z

— 1 x=5n
— TY =Slegiaim
— Tz=n72

fy 200 400 600 ‘200 1000
Input Size (n>
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 2dbe342e8fc1

- Departments: Artificial Intelligence, Computer Science and Business Systems
- Programmes: BTech AI 7012, BTech CSBS 7036, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_AI_7012/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C010)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 Nov 2025
- Text: mixed (14 pages), mean OCR confidence 86.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSBS)/MBA Tech (AI)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 26 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Attempt any 4 questions from the remaining questions.
6. Total 5 questions to be attempted.
Q.1 Attempt all questions   [20
:   ]
(a   Define an algorithm and write the characteristics of algorithm.   [5]
)
Definition:
An algorithm is a step-by-step procedure for solving a problem in a finite amount of
time.
It is not tied to any specific programming language — it's a logical plan, not code.
Characteristics of a Good Algorithm
A well-designed algorithm has the following key characteristics:
# Characteristic   Description
The algorithm must always terminate after a finite number of
1 Finiteness
steps.
Each step of the algorithm must be precisely and
2 Definiteness
unambiguously defined.
It should accept zero or more inputs, externally supplied before
3 Input
or during execution.
It should produce at least one output, which is the result of the
4 Output
computation.
All operations must be basic enough to be carried out by a
5 Effectiveness
person using paper and pencil in a reasonable time.
The algorithm should solve a general class of problems, not just
6 Generality
a single instance.
(b Given the set of symbols and corresponding frequency table as below, Draw the [5]
)   Huffman tree and generate the Huffman code.
********** 1 **********
--- page 2 ---
Symbol A B C D E F G H I
Frequency 7 6 4 6 5 1 10 7 8
Solution: Huffman tree 3 marks, code 2 marks
(c   Differentiate between Divide & Conquer techniques and Dynamic Programming in terms of   [5]
)   subproblem structure and overlapping subproblems. Show with example.
Solution:
********** 2 **********

[Text in pictures on this page, read by OCR]
[54]

/ \
[22]EFCBD   [32]AHIG
f / \
[1@]EFC [12]BD [14]AH [18]IG
fr rin i fr
[5]E [5]FC [6]B [6]D [7]A [7]H [8]I [1e]G
i

[1]F [4]c

Divide and Conquer vs Dynamic Programming

Feature Divide and Conquer Dynamic Programming
Subproblem Structure Divides a problem into independent Divides a problem into overlapping
subproblems that do not overlap. subproblems that are reused multiple
times.
Overlapping Subproblems No overlapping — each subproblem is Overlapping — same subproblems occur
solved once. repeatedly; results are stored

(memoization/tabulation).

Optimal Substructure May or may not use optimal Always relies on optimal substructure
substructure explicitly. property.

Storage of Results Does not store results of subproblems. Stores results to avoid recomputation.

Example Merge Sort / Quick Sort - each half is 0/1 Knapsack / Fibonacci / Matrix Chain
independent. Multiplication — subproblems overlap and

reuse results.
--- page 3 ---
(d The regional planning committee wants to prepare a digital representation of 5 states   [5]
)   for a map-based application. The regions must be marked in a digital map so that
neighboring areas have distinct identifiers, using the least possible numbers. Their
geographical borders are as follows:
• A shares borders with B, C, and D.
• B shares borders with A and C.
• C shares borders with A , B, and E.
• D shares borders with A and E.
• E shares borders with G and D.
(i)   Identify & explain the suitable algorithmic concept that fits in this
situation.
(ii)   Draw the graph representation and find the minimum number of
identifiers needed.
Solution: identification & explanation of algorithm ( 2marks), draw diagram ( 2
marks), minimum no. of identifier needed ( 1 mark)
Graph coloring problem, minimum 3 colors needed
Q 2   (a Compute the time complexity for the recurrence relation T(n)=3T(n/4)+ n2 using (i) [10
)   Master’s Theorem, (ii) Substitution Method.   ]
Solution: 5 marks each
Complexity is n2
(b   (i) Write the algorithm of Longest Common Subsequence and compute the time [10
)   complexity.   ]
(ii) Solve the two strings: A = “qpqrr” and B = “pqprqrp” using LCS method.
Solution: 5 marks algorithm, 5 marks solution
********** 3 **********
--- page 4 ---
Time complexity
In dynamic programming, only table of size m ´ n is filled up using two nested for
loops. So running time of the dynamic programming approach would take O(mn)
Q.3   (a   (i)   Simulate   Quick   sort   algorithm   for   the   following   example [10
)   25,36,12,4,5,16,58,54,24,16,9,65,78. Pivot element is 25.   ]
********** 4 **********

[Text in pictures on this page, read by OCR]
LCS-LENGTH(X, Y)

1 m= X.length

2 n=Y.length

3 let b[l..m,1..n] and c[0..m,0..n] be new tables
4 fori = ltom

5 cfi,0] = 0

6 for 7 = Oton

7 co, 7] =0

8 fori = ltom

9 for j = lton

10 ifx; == y;

i cli, j] = ck -—1,7 -1]+1
12 big] ="

13 elseif c[i — 1, j] = cfi,j —1]
14 cli, j] = ci —1.j]

15 bi. jJ="t"

16 else cli, j] = cli. j — 1]

17 bli, j] = “—”

18 return c andb
--- page 5 ---
(ii) Compute the best case time complexity of quick sort using Master’s theorem.
Solution : 6 marks solution, 4 marks time complexity
Step 1: Partitioning around pivot (25)
We separate elements into:
•   Left: elements less than pivot
•   Right: elements greater than or equal to pivot
• Elements less than 25: [12, 4, 5, 16, 24, 16, 9]
• Elements greater than or equal to 25: [36, 58, 54, 65, 78]
After first partition:
➡ [12, 4, 5, 16, 24, 16, 9, 25, 36, 58, 54, 65, 78]
Now apply quick sort recursively to left and right sub-arrays.
Final Sorted Array:
➡ [4, 5, 9, 12, 16, 16, 24, 25, 36, 54, 58, 65, 78]
(b   Explain the concept of Sum of subset in backtracking. Draw The state-space tree [10
)   and compute the solution for the instances S = (3, 5, 6, 7) and sum = 15.   ]
Solution: 3 marks for explanation, 5 marks for tree, 2 marks for solution
********** 5 **********

[Text in pictures on this page, read by OCR]
Recurrence (QuickSort — best case).

When every partition splits the array exactly in half:
T(n)=27(5)+0(n), TA) = @().

Match to Master Theorem form: T'(n) = aT (n/b) + f(n).

e a-2
e b=2
° f(n) = O(n)

Compute nl 4 — nes? — pn! = n,
We compare f(n) with n!°% 4;
f(n) = @(n) = (n°)
so this is Case 2 of the Master Theorem (polynomially equal, ie. f (n) — O(n! log* n) with k = 0
By Case 2:
T(n) = @(n'®*log**! n) = O(n log n).

Answer: QuickSort (best case) T(n) = O(n log n).
--- page 6 ---
The Sum of Subsets problem is a classic backtracking example where we find all subsets of
a given set whose elements add up to a specific target sum. The algorithm explores all
possible combinations by choosing whether to include or exclude each element, forming a
decision tree. If the current sum exceeds the target, that branch is abandoned (backtracked)
to reduce unnecessary computations. This approach efficiently generates valid subsets while
avoiding exhaustive search of all possibilities. It is commonly used in optimization and
combinatorial problems.
Solution is 3,5,7
Q.4   (a   Write the algorithm for job sequencing with deadlines? Solve the following instance [10
)   of Job sequencing with deadlines problem n=7, profits (p1,p2,p3,p4,p5,p6,p7) = (3, 5,   ]
20,18, 1, 6, 30)and deadlines (d1,d2, d3, d4, d5, d5, d7)= (1,3,4,3,2,1,2). Schedule the
jobs in such way so as to get maximum profit.
Solution: 5 marks for algorithm, 5 marks for solution
Schedule Jobs:
• J7 (30, deadline=2):
Try slot 2 → free → assign J7 → [-, J7, -, -]
• J3 (20, deadline=4):
Try slot 4 → free → assign J3 → [-, J7, -, J3]
********** 6 **********

[Text in pictures on this page, read by OCR]
| Algorithm GreedyJob(d, J, 1)
2 // J isa set of jobs that can be completed by their deadlines.

4 J = {1};

5 for i := 2 to n do

6

7 if (all jobs in J U {i} can be completed

8 by their deadlines) then J := J U {i};
9
--- page 7 ---
• J4 (18, deadline=3):
Try slot 3 → free → assign J4 → [-, J7, J4, J3]
• J6 (6, deadline=1):
Try slot 1 → free → assign J6 → [J6, J7, J4, J3]
• J2 (5, deadline=3):
Try slot 3 → already taken
Try slot 2 → taken
Try slot 1 → taken
❌ Cannot schedule
• J1 (3, deadline=1):
All earlier slots taken
❌ Cannot schedule
• J5 (1, deadline=2):
Slot 2 → taken
Slot 1 → taken
❌ Cannot schedule
Final Job Sequence (by slot):
Slot Job
1   J6
2   J7
3   J4
4   J3
Scheduled Jobs: J6, J7, J4, J3
Total Profit: 6 + 30 + 18 + 20 = 74
• Maximum Profit: 74
• Job Sequence (by slot): J6 → J7 → J4 → J3
(Or just: [J6, J7, J4, J3])
(b   (i) Differentiate between 0/1 Knapsack and Fractional Knapsack in terms of Item   [10
)   selection rules and approach used for the optimal solution.   ]
(ii) A knapsack has a capacity of 7 kg. There are 4 items with the following weights
{1, 3, 4, 5} and profits: {1, 4, 5, 7}, with knapsack capacity W = 7.
(a) Compute the max profit using table method of 0/1
knapsack.
(b) Using the recursive formula of 0/1 Knapsack, compute the values of
DP[4][6] and DP[4][7] (i.e., for the last item at capacities 6 and 7).
Show all steps clearly.Solution:
Solution: (i) 2 marks, (ii) 8 marks – (a) 5 marks) (b) 3 marks
********** 7 **********
--- page 8 ---
Solution:
Q.5   (a   Explain Asymptotic Notations with graph.   [10
)   ]
Solution:
Theta Notation: Let g and f be the function from the set of natural
numbers to itself. The function f is said to be Θ(g), if there are
constants c1, c2 > 0 and a natural number n0 such that c1* g(n) ≤ f(n)
≤ c2 * g(n) for all n ≥ n0
********** 8 **********

[Text in pictures on this page, read by OCR]
Compute DP[4][6] and DP[4][7]
© DP[4][6]: w = weight[4]=5 —

DP(4)(6] = max(profit(4] + DP(3]|6 — 5], DP(3)[6]) = max(7 + DP(3)[1],6) = max(7 + 1,6) = 8
© DP[4][7]: w = weight[4]=5 —

DP{4][7] = max(profit[4] + DP[3]|7 — 5], DP{3|[7]) — max(7 + DP[3][2],9) — max(7 + 1,9) — 9
--- page 9 ---
Big O Notation
If f(n) describes the running time of an algorithm, f(n) is O(g(n)) if
there exist a positive constant C and n0 such that, 0 ≤ f(n) ≤ cg(n) for
all n ≥ n0
Omega Notation
Let g and f be the function from the set of natural numbers to itself.
The function f is said to be Ω(g), if there is a constant c > 0 and a
natural number n0 such that c*g(n) ≤ f(n) for all n ≥ n0
********** 9 **********
--- page 10 ---
(b   (i)   Write the algorithm of fractional knapsack problem   [10
)   (ii)   Find the feasible solution of the Knapsack instance n= 7, M=15, (p1,p2,   ]
p3, p4, p5, p6, p7) = (10,5,15,7,6,18,3) and (w1,w2,w3, w4, w5,
w6,w7)=(2,3,5,7,1,4,1).
Solution: algorithm 5 marks, solution 5 marks
Capacity
Item Weight Profit   Take?   Total Profit
Left
5   1   6   Take whole   15 - 1 = 14 6
1   2   10   Take whole   14 - 2 = 12 6 + 10 = 16
6   4   18   Take whole   12 - 4 = 8 16 + 18 = 34
3   5   15   Take whole   8 - 5 = 3   34 + 15 = 49
7   1   3   Take whole   3 - 1 = 2   49 + 3 = 52
Only 2 weight left   52 + 5×23=3.335 \times } =
2   3   5   0
— take fraction 2/3   3.335×32=3.33 ≈ 55.33
********** 10 **********

[Text in pictures on this page, read by OCR]
* Greedy-fractional-knapsack (w, v, W)
1. forj=lton

2. doxf{i] =0

3. weight =0

4. while weight < W

5. do/=best remaining item
6. if weight + wi/]s W

7. then x{fJ=1

8. weight = weight + w{/]
9. else

10. x{i) = (w~- weight) / w{i]
11, weight=W

12. return x
--- page 11 ---
Final answer:
• Take full items: 5, 1, 6, 3, 7
• Take fraction 2/3 of item 2
•   Total profit ≈55.33\approx 55.33≈55.33
Q.6   (a Compute the time and space complexity of the given code snippets. Also, identify the [10
)   type of complexity function (such as linear, exponential etc.) and plot the respective   ]
graphs of time complexity:
(i)   int a =0, b=0, n ,m;   (ii)   int i, n, k, x;
{   {
for(i=0; i<n; i++)   for(i=1; i<=n; i++)
{   {
for(j=0; j<m; j++)   for(k=j;   k<=n;
a=a+j;   k=k*2)
}   x=x+1;
}   }
for(k=0; k<=n; k++)   }
{
b=b+k;
}
Solution: 5 marks each. Time complexity ( 2marks), space complexity ( 2 marks),
diagram ( 1 mark) for each question
(i) O(𝒏𝟐)   (ii) 𝑶(𝒏𝒍𝒐𝒈𝒏)
(b   (i)   Write down algorithm for finding shortest path from a multi stage   [10
)   graph using forward method.   ]
(ii)   Find out the shortest path to reach from source ‘1’ to destination ‘12’
using Forward Method of Multi Stage Graph.
Solution:
********** 11 **********
--- page 12 ---
(i)   4 marks
(ii)   6 marks: shortest path
Q.7   (a   Write the algorithm for min_max recursive function. Demonstrate the min_max   [10
)   function on the given array A=[23,45,12,67,34,89,54,31, 89] and compute the total   ]
number of comparisons required.
Solution: Algorithm 5 marks, comparisons 5 marks
MinMax(arr, low, high)
if low == high:   // Only one element
return (arr[low], arr[low]) // min = max = arr[low]
if high == low + 1:   // Two elements
if arr[low] < arr[high]:
return (arr[low], arr[high])
else:
return (arr[high], arr[low])
mid = (low + high) / 2
(min1, max1) = MinMax(arr, low, mid)
(min2, max2) = MinMax(arr, mid+1, high)
min_final = min(min1, min2)
max_final = max(max1, max2)
return (min_final, max_final)
********** 12 **********

[Text in pictures on this page, read by OCR]
Fgraph (G, K, n, P)
{
Cost[n]:= 0.0;
for j:=n-1 to 1 step -1do
{

Let r be a vertex such that <j, > is an edge of G and C[j, r] + cost{r]
isminimum; _//r is the vertex in v;,, and j be the vertex in v;

C{j, r] + Cost[r]; //taking the value of min. cost edge

Pi] = a[PEi-1N);
--- page 13 ---
No. of comparisons 12
(b   Write the algorithm of Bellmanford approach for single source shortest path and [5]
)   explain its time complexity.
(c   Define P, NP, NP-hard and NP-complete problems with diagram. Give examples for   [5]
)   each class.
********** 13 **********

[Text in pictures on this page, read by OCR]
[@-8]
fi
[e-3] [4-8]
/ \ i \
[@-1] [2-3] [4-5] [6-8]
i fN £N / oN
23 45 12 67 34 89 [6-7] 389
fx
54 31

BELLMAN: FORD(V, E, W, S)

INITIALIZE-SINGLE-SOURCE(V, s)

— ew)
2. fori<lto|V|-1 O ]

3. do for each edge (u,v) ¢ E ™) ‘O(VE)
4. do RELAX(u, v, w) Of) J

5. for each edge (u,v) «¢ E

6 do if d[v] > d[u] + w(u, v) —— O()

1 then return FALSE

8. return TRUE

Running time: O(V+VE+E)=O(VE)

Class Definition Example

P (Polynomial time) Problems that can be solved in polynomial time by a Sorting (Merge Sort, Quick Sort),
deterministic algorithm. Shortest Path (Dijkstra)

NP (Nondeterministic Problems for which a given solution can be verified in Subset Sum, Hamiltonian Path,

Polynomial time) polynomial time. Knapsack (0/1)

NP-hard Problems that are at least as hard as the hardest Halting Problem, General TSP

problems in NP. They may not be in NP (solution may
not be verifiable in polynomial time).

NP-complete Problems that are both in NP and NP-hard. 3-SAT, 0/1 Knapsack, Hamiltonian Cycle
--- page 14 ---
NP-Complete, NP-Hard

Class Example Problem

P Sorting, Minimum Spanning Tree, Shortest Path (Dijkstra)
NP Subset Sum, Graph Coloring, Hamiltonian Path

NP-hard Traveling Salesman Problem (general), Halting Problem
NP-complete 3-SAT, 0/1 Knapsack, Hamiltonian Cycle, Graph Coloring

FRR IC 7 I OH
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper df825b282dc2

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_Computer_7032/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (13 pages)
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 16 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data, if necessary.
Q1
Answer briefly:   Marks
a.   Define an algorithm. Explain its key characteristics with suitable
examples.
Answer:
An algorithm is a finite sequence of well-defined, step-by-step
instructions used to solve a problem or perform a specific task.
Key Characteristics of an Algorithm (with examples)
1. Input
a. An algorithm takes zero or more inputs.
b. Example: Input numbers in a sorting algorithm.
2. Output
CO,   a. Produces at least one output.
b. Example: Sorted list as output of a sorting algorithm.   [5]
SO,BL
3. Definiteness (Unambiguity)
a. Each step must be clear and precisely defined.
b. Example: “Add two numbers” is clear, but “process
numbers” is vague.
4. Finiteness
a. Must terminate after a finite number of steps.
b. Example: Loop runs only until a condition is satisfied.
5. Effectiveness
a. Each step should be simple and executable in finite time.
b. Example:   Arithmetic   operations   like   addition,
comparison.
6. Correctness
a. Produces the correct output for all valid inputs.
b. Example: A searching algorithm returns the correct index.
********** 1 **********
--- page 2 ---
Marks: 1 mark for definition, any 4 key characteristics- 4 marks
CO,   b.   Explain the general process of divide-and-conquer method and give its [5]
SO,BL   control abstraction in pseudo-code.
Answer:
General divide and conquer method
•   Step 1. A problem is divided into several sub problems of the
same type, ideally of about equal size.
•   Step 2. The sub problems are solved (typically recursively,
though sometimes a different algorithm is employed, especially
when sub problems become small enough).
•   Step 3. If necessary, the solutions to the sub problems are
combined to get a solution to the original problem.
Algorithm:
Marks distribution:
General process- 2 marks;
control abstraction pseudocode- 3 marks
CO,   c.   Explain the concept of edge relaxation and its role in SSSP algorithms.   [5]
SO,BL
Solution: Edge relaxation is the core operation used in Single Source
Shortest Path (SSSP) algorithms to improve (or “relax”) the current
best-known distance to a vertex.
For an edge (u,v) with weight w:
If d[v]>d[u]+w(u,v),
then update: d[v]=d[u]+w(u,v)
•   d[u]: current shortest distance from source to u
•   d[v]: current shortest distance from source to v
Role in SSSP Algorithms
• Relaxes all edges repeatedly (|V| − 1 times)
• Can handle negative weights
Guarantees correct shortest paths even with negative edges
Marks: Explanation: 3 marks, role-2 marks
CO,   d.   Differentiate Backtracking from Brute Force. Explain the role of [5]
SO,BL   Bounding Function.
Solution:Any 4 differences-4Marks
Feature   Brute Force   Backtracking
Approach   Tries all combinations Prunes invalid
branches early
********** 2 **********

[Text in pictures on this page, read by OCR]
1 Algorithm DAndC(P)

2 {
3 if Small(P) then return S(P);

4 else

5

6 divide P into smaller instances P;, P2,...,P_, k > 1;

7 Apply DAndC to each of these subproblems;

8 return Combine(DAndC(P, ),DAndC(P2),...,DAndC(P,));
9
--- page 3 ---
Efficiency   Poor (exponential   Better (pruning
always)   reduces states)
State Space   Fully explored   Partially explored
Constraint   After full solution   At each step
Check
Role of Bounding Function (Bk): 1Mark
The bounding function determines whether a partial solution (x1, x2, ...,
xk) can possibly lead to a complete valid solution.
•   If Bk = true → continue expanding
•   If Bk = false → prune this branch, backtrack
A
i. Explain the set relationships between P, NP, NP-hard, and NP-
complete with a diagram.
ii. What do you mean by a non-deterministic machine?
iii. State any four meaningful differences between np-hard and np-
complete problems.
Solution:
i. Subset relation- 2marks
• P⊆NP
•   NP-complete ⊆ NP
•   NP-complete ⊆ NP-hard
•   NP-hard may include problems outside NP
Q2
CO,   [10]
SO,BL   Diagram- 2marks
ii. A non-deterministic machine is a theoretical model that:
• Can guess the correct solution instantly
• Then verifies it in polynomial time- (2marks)
iii. Differences- 1 mark for each difference
•   Definition: NP-Complete = NP + NP-Hard. NP-Hard does not require
being in NP.
•   Verification: NP-Complete problems are verifiable in polynomial
time. NP-Hard problems are not necessarily verifiable in polynomial
time.
• Problem Type: NP-Complete problems are usually decision problems
(yes/no). NP-Hard problems can be optimization, search, or decision
problems.
•   Relationship: Every NP problem can be reduced to an NP-Hard
problem in polynomial time.
CO,   B   For the given two sequences: X = "ABCBDAB" and Y = "GBDCAB":
SO,BL   i. Construct the LCS table using dynamic programming   [10]
ii. Find any one LCS
********** 3 **********
--- page 4 ---
iii. Give the pseudo-code for LCS
Sol:
LCS: BCAB/BDAB/BCBA
Pseudo-code for LCS:
Marks: Table construction-4 marks, LCS – 1-mark, Pseudo-code -5
marks
A   i. A relief organization want to supply food for disaster relief based on
their nutritional value. They have a truck that can carry maximum (M)
Q3   200 kg of the food items. Available food items such as Rice (100 kg),
CO,   Wheat Flour (70 kg), Beans (50 Kg) and Milk Powder (40 kg) with [10]
SO,BL   their nutritional values (450, 500, 300, 380) respectively. Identify how
can the truck be loaded with maximum nutritional value, considering
food can be split into smaller portions.
********** 4 **********

[Text in pictures on this page, read by OCR]
LCS-LENGTH(X, Y)

1 m= X. length

2 n= /Y.length

3 let b[1..m,1..n] and c[0..m,0..n] be new tables
4 fori = 1tom

5 c[i, 0] = 0

6 for 7 = Oton

7 c[0, 7] =0

8 fori = ltom

9 for j = lton

10 if x; == y;

11 cli, fj] =cfi-1,f-—1)+1
12 bli, J) = “N°

13 elseif c{i —1, 7] => cli, 7 —1]
14 cli, j] = cfi-1, J]

15 bli, j] = “t”

16 else c[i, j] = ci, j — 1]

17 bj, j] =“<”

18 return c and b
--- page 5 ---
ii. Identify the highest total nutritional value obtained, considering the
given constraint.
iii. Can this problem be classified as optimization problem? Why or why
not?
Sol: The problem can be solved as fractional knapsack problem.
Find the ratio and sort in descending order
1. Milk Powder → 9.5
2. Wheat Flour → 7.14
3. Beans → 6.0
4. Rice → 4.5
Fill the truck with each type of food in the order of ratio.
Final solution
• Milk Powder → Full
• Wheat Flour → Full
• Beans → Full
• Rice → 40% (partial)
(5 marks)
Total Nutritional value= 380 + 500 + 300 + 180 = 1360 (2 marks)
Yes, this problem be classified as optimization problem as it has
maximization problem with a given constraint. (3 marks)
B   Analyze the recurrence relation 𝑇(𝑛) = 𝑇( 𝑛 2) + 𝑛2 by constructing a [10]
recursion tree to determine the asymptotic upper bound. Further, verify
the obtained bound using the substitution method.
Answer:
𝑛2
𝑛 2
2
𝑛 2
4
CO,   𝑛 2
SO, BL   8
.......
1
2
𝑇(𝑛) = 𝑛2 + (𝑛 2) + (𝑛 4)2 + ⋯. .
1   1
𝑇(𝑛) = 𝑛2 (1 + + + ⋯. . )
4 16
********** 5 **********
--- page 6 ---
𝑇ℎ𝑒 𝐸𝑞𝑢𝑎𝑡𝑖𝑜𝑛 𝑖𝑠 𝑖𝑛 𝐺. 𝑃 𝑠𝑒𝑟𝑖𝑒𝑠
1   4
= 𝑛2.   = 𝑛2
1 −1 3
4
Therefore the complexity is 𝑂(𝑛2)
Substitution method:
𝑇(𝑛) <= 𝑐. 𝑔(𝑛)
𝑇(𝑛) <= 𝑐. 𝑛^2
Substitute into recurrence:
𝑇(𝑛) = 𝑇(𝑛 2) + 𝑛2
2
≤ 𝑐. (𝑛 2) + 𝑛2
≤ 𝑛2 (𝑐 + 1)
4
(𝑐 + 1) ≤𝐶= 1 ≤3𝑐
4   4
𝑇ℎ𝑒𝑟𝑒𝑓𝑜𝑟𝑒 𝐶≥ 4 𝑎𝑛𝑑 𝑇(𝑛) = 𝑂(𝑛2),
3
The asymptotic upper bound is quadratic.
Marks: 5 marks for recursion tree time complexity
5 marks for substitution verification.
A   For the following given graph:   [10]
Q4
CO,
SO,BL
i.   Compute the minimum cost from S to T using forward method
in dynamic programming.
ii.   Trace the optimal path.
iii.   Discuss the recurrence relation for solving a multistage graph
using the forward approach in dynamic programming.
Sol:
********** 6 **********
--- page 7 ---
recurrence relation:
Marks: computing cost stage-wise: 5 marks, optimal path tracing: 2
marks, recurrence relation: 3 marks
B   Given the following jobs:   [10]
Job   Deadline   Profit
J1   5   80
J2   3   60
J3   4   70
J4   2   65
J5   1   25
CO,SO,   J6   3   30
BL   i. Using the Greedy approach, determine the optimal job sequence
that maximizes total profit.
ii. Give the pseudo-code for the given problem
iii. Also discuss the algorithm's time complexity.
Solution:
Optimal job sequence: J5 → J4 → J2 → J3 → J1
Maximum Profit Calculation= 25 + 65 + 60 + 70 + 80= 300
********** 7 **********
--- page 8 ---
Pseudo-Code
Time Complexity
1. Sorting:
• Sorting jobs by profit → O(n log n)
2. Slot Allocation:
• For each job, checking slots → O(n × d)
(where d = maximum deadline)
• Worst case: O(n²)
Marks: Solution- 4 marks, Complexity- 2 marks, pseudo-code-4
marks
A   Discuss the N-Queens Problem conceptually. Explain how   [10]
Backtracking reduces the search space. Trace the state space tree
solution for N=4, step by step.
Solution:
N-Queens Concept- 2Marks
The N-Queens problem belongs to the class of Constraint Satisfaction
Problems (CSP). The goal is not to optimize a value but to find all
configurations satisfying a set of constraints.
The Problem is hard because
• For N=8: Brute force = 8⁸ = 16,777,216 possibilities
Q5   • Even with distinct columns (8!): 40,320 possibilities
CO,   • Backtracking reduces this to checking only ~2000 nodesBack
SO,BL
How Backtracking reduces the search space- 3marks
Backtracking Reduces the search space by
Step 1 — Early Detection: Constraints are checked at each placement,
not after all N queens are placed.
Step 2 — Pruning: If placing a queen at position (k, i) violates any
constraint, the entire subtree below that node is abandoned
immediately.
Step 3 — Systematic Exploration: The algorithm ensures every valid
solution is found without redundant checks.
Tracing of 4 Queen- 5marks
Should include Explicit and implicit conditions and stsep by step tracing
for the solution
********** 8 **********

[Text in pictures on this page, read by OCR]
1 Algorithm GreedyJob(d, J,n)
2 // Jisaset of jobs that can be completed by their deadlines.

3

4 J :={1}5

5 for i := 2 to n do

6

7 if (all jobs in J U {i} can be completed

8 by their deadlines) then J := J U {i};
9
--- page 9 ---
B   A delivery truck has a maximum capacity of 10 units. The items   [10]
available are:
Item   Weight   Profit
1   2   20
2   3   30
3   5   50
4   7   70
a) Build the DP table step-by-step. (6 marks)
c) Compute the maximum achievable profit. (2 marks)
d) Trace back and list the selected items. (2 marks)
Sol:
Let 𝑑𝑝[𝑖][𝑤] denote the maximum profit using first 𝑖 items with
CO,   capacity 𝑤.
SO,BL   i \ w   0   1   2   3   4   5   6   7   8   9   10
0   0   0   0   0   0   0   0   0   0   0   0
1   0   0   20   20   20   20   20   20   20   20   20
2   0   0   20   30   30   50   50   50   50   50   50
3   0   0   20   30   30   50   50   70   80   80   100
4   0   0   20   30   30   50   50   70   80   90   100
c) Maximum Profit (2 Marks)
Maximum Profit=𝟏𝟎𝟎Maximum Profit=𝟏𝟎𝟎
d) Selected Items (2 Marks)
Backtracking from
𝑑𝑝[4][10]=100:
********** 9 **********

[Text in pictures on this page, read by OCR]
A 3 / \ 8

2 a Q 4 2 & Q
a a = 8 it [o}
[\\ 7. .

23 44 3 4
a a
a a
71\ Fes
1
[ol
a
a
solution

FIGURE 12.2 State-space tree of solving the four-queens problem by backtracking.
x denotes an unsuccessful attempt to place a queen in the indicated
column. The numbers above the nodes indicate the order in which the
nodes are generated.
--- page 10 ---
• Compare 𝑑𝑝[4][10] with 𝑑𝑝[3][10]→ same ⇒ Item 4 not
selected
• Move to 𝑑𝑝[3][10]=100dp[3][10]=100:
 𝑑𝑝[3][10]≠𝑑𝑝[2][10]dp[3][10]≠dp[2][10]
⇒ Item 3 selected (weight = 5)
Remaining capacity = 10−5=510−5=5
At 𝑑𝑝[2][5]=50:
 𝑑𝑝[2][5]≠𝑑𝑝[1][5]
⇒ Item 2 selected (weight = 3)
Remaining capacity = 5−3=25−3=2
At 𝑑𝑝[1][2]=20: ⇒ Item 1 selected
A   Apply Quick Sort to the sequence of letters E, X, A, M, P, L, E by
selecting the first element as the pivot. Show the arrangement of
elements after each partition process. Further, derive the recurrence
relations for the best, average, and worst cases of the algorithm.
Answer:
E, X, A, M, P, L, E
Q6
[10]
CO,
SO,BL   Let T(n) be the time complexity.
1. Best Case: 𝑇(𝑛) = 2𝑇( 𝑛 2) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛𝑙𝑜𝑔𝑛)
2. Average Case:
𝑇(𝑛) = 𝑇(𝑘) + 𝑇(𝑛−𝑘−1) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛𝑙𝑜𝑔𝑛)
3. Worst Case: 𝑇(𝑛) = 𝑇(𝑛−1) + 𝛩(𝑛)
𝑇(𝑛) = 𝛩(𝑛2)
Marks: Quicksort application - 4 marks
Recurrence equations and complexity - 6 marks (2+2+2)
CO,   B   i. Compute the time complexity of the recurrence relation 𝑇(𝑛) =   [10]
SO,BL   4𝑇(√𝑛) + log2 𝑛
********** 10 **********
--- page 11 ---
(5 marks)
ii. Compute the time complexity of the code segment given below
𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛()
{
𝑖𝑛𝑡 𝑖= 1;
𝑤ℎ𝑖𝑙𝑒 (𝑖 < 𝑛)
{
𝑖𝑛𝑡 𝑗= 𝑛;
𝑤ℎ𝑖𝑙𝑒(𝑗 > 0)
𝑗 = 𝑗/2;
𝑖= 2 ∗𝑖;
} //𝑒𝑛𝑑 𝑜𝑓 𝑖
}
Answer:
T(n) = (log 𝑛∗log 𝑛) = log2 𝑛 (5 marks)
A   Design a recursive algorithm to find the minimum and maximum
Q7   element in the array-using divide and conquer. Find the its time
CO,   complexity and trace the algorithm for the given array a=[ 22, 13, -5, - [10]
SO,BL   8, 15, 60, 17, 31, 47].
********** 11 **********
--- page 12 ---
answer
𝑇(𝑛) = 2𝑇( 𝑛 2) + 𝐶 𝑂(𝑛)
Marks: 5 marks for algorithm, 3 marks for application and 2 marks
for time complexity.
B   Consider three algorithms X, Y and Z. and the run-time complexities are
𝑇𝑋= 5𝑛, 𝑇𝑌= 5 log10 𝑛, 𝑎𝑛𝑑 𝑇𝑍= 𝑛2. Compare the growth rates of
three algorithms when the input size increases from n=10 to n=1000.Plot
the graph and identify which algorithm performs better based on their
growth rates.
CO,   Answer:
[5]
SO,BL   Step 1: Given Time Complexities
• Algorithm X: 𝑇𝑋= 5𝑛
• Algorithm Y: 𝑇𝑌= 5 log10 𝑛
• Algorithm Z:𝑇𝑍= 𝑛2
Step 2: Values at Key Input Sizes
n   𝑇𝑋= 5𝑛 𝑇𝑌= 5 log10 𝑛 𝑇𝑍= 𝑛2
10   50   5   100
********** 12 **********

[Text in pictures on this page, read by OCR]
2 // all: nj is a global a Parameters é@ and j are integers,
1 i

3 = jain, The effect is to set yan and rrire to the
4 // largest and smallest values in ali ; j], respectively.

5

6 t if G — 7) then rnau rise :— alt}; // Small(?)

7 else if (i = j 1) then // Another case of Small(7?)
8

9 if (ali) []) then

10 {

1 max := ali]; nvin :—~ alz]s

12 7

13s else

da

iS max >— alt}; min :— aly];

16

17

18 else

19 { // ACP is not small, divide P into subprotlems.
20 // Find where to split the set.

21 mid i= ((@+ 7)/243

22 // Solve the subproblems.

Q3 MaxMin(é, mid, mea, mir);


25 // Combine the solutions.

26 if (maa << rnarl) then saw 2 reel;
27 if (min = min i) them min :— mini;

28 }

29 }
--- page 13 ---
100   500   10   10,000
1000 5000   15   1,000,000
Step 3: Growth Rate Observation
• Logarithmic growth increases very slowly.
• Linear growth increases proportionally with n.
• Quadratic growth increases very rapidly as n grows.
From the table and graph:
• 𝑇𝑌= 5 log10 𝑛 Grows slowest.
• 𝑇𝑋= 5𝑛 Grows moderately.
• 𝑇𝑍= 𝑛2 Grows fastest.
Step 4: Conclusion
Based on the rate of growth: 𝑇𝑌< 𝑇𝑋< 𝑇𝑍
• Best Algorithm: Y (logarithmic complexity)
• Moderate: X (linear complexity)
• Worst for large inputs: Z (quadratic complexity)
So, when the input size increases from 10 to 1000, Algorithm Y
performs the best because its running time increases very slowly
compared to the other two algorithms.
Marks: calculation 1 marks, plot the graph 1 marks better
algorithm growth rate 3 marks.
C   State the two important properties based on which we can decide that a
problem can be solved using greedy approach.
Solution: A problem can be solved using a greedy approach if it
CO,   satisfies:
1. Greedy Choice Property – A locally optimal choice leads to a   [5]
SO,BL
globally optimal solution.
2. Optimal Substructure – The optimal solution can be constructed
from optimal solutions of subproblems.
Marks: Each property correct explanation- 2.5 marks each
********** 13 **********

[Text in pictures on this page, read by OCR]
10

20

ee Growth Rate Comparison of Algorithms X, Y, and Z

— 1 x=5n
— TY =Slegiaim
— Tz=n72

fy 200 400 600 ‘200 1000
Input Size (n>
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper d3261fc6e48d

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSE_DS_7011/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C068)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 03 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 question.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the fundamental characteristics of an algorithm with examples.
CO-1;
SO-1;   5
BL-2
CO-2;   b.   What is the greedy choice property? How is it satisfied in MST
SO-6;   problems?   1+4
BO-3
********** 1 **********

[Text in pictures on this page, read by OCR]
The fundamental characteristics of an algorithm describe the essential properties that any well-defined
algorithm must satisfy. These are often asked in theory exams, so it's good to present them clearly with
examples.

1. Input

An algorithm should accept zero or more inputs.

Example:
An algorithm to find the sum of two numbers takes inputs a and b.

2. Output

It must produce at least one output/result.
--- page 2 ---
c.   Write and explain the algorithm for the Longest Common Subsequence
using the Dynamic Programming approach. Analyse its time
complexity.
CO-2;
SO-6;   5
BO-3
CO-3;   d.
Solve the recurrence relation of the minmax problem using the
SO-2;   5
Substitution method.
BL-2
a.   With reference to Asymptotic complexity,
6+4
1) Define Upper bound, Tight bound, Lower bound complexities.
Q2
CO-1;
2) Explain Relaxation algorithm used in bellman ford and analyse
SO-1;
its time complexity
BL-2
CO-4;
SO-6,7;
With reference to Merge sort,
BL-2,4
b.   1) Explain the Merge Sort algorithm using the Divide-and-Conquer
8+2
approach.
2) Discuss Merge sort with respect to stability and in-place sorting.
********** 2 **********

[Text in pictures on this page, read by OCR]
Greedy Choice Property

It states that:

A globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step.

In other words, at every stage, we pick the best immediate option without reconsidering previous choices,

and this still leads to the overall optimal solution.

Example (Simple Idea)

In coin change (for certain coin systems), always picking the largest denomination first leads to the

minimum number of coins.

How it is satisfied in Minimum Spanning Tree (MST)

Los.

The Longest Common Subsequence (LCS) problem is a classic example of Dynamic Programming, where

we break the problem into smaller overlapping subproblems and store their results.

@ Problem Definition
Given two sequences:

© X=21,22,...,L2m

© Y= yi, yr, Yn

Find the longest subsequence common to both sequences (not necessarily contiguous).

Example:
X = “ABCBDAB"
Y = “BDCAB”

LCS = “BCAB" (length = 4)
--- page 3 ---
a.   1) Explain any two types of algorithmic approaches with examples.
2) Explain P, NP, NPH, and NPC decision problems with examples
b.   5+5
1+2
Q3   7
CO-1;
SO-1;
BL-2
CO-3;
SO- 2;
BL-3
With reference to the Multistage Graph,
1) State the Recurrence relation for the Multistage Graph problem
using the dynamic programming approach and analyse the time
complexity.
2) Solve for a minimum cost path from ‘s’ to ‘t’ in the multistage graph
of the figure given below. Adopt a backward approach.
********** 3 **********

[Text in pictures on this page, read by OCR]
1) Merge Sort using Divide-and-Conquer
Merge Sort follows the Divide-and-Conquer paradigm, which involves three steps:
®@ Steps:

1. Divide

© Split the array into two halves recursively until each subarray has only one element.

2. Conquer

© Recursively sort the subarrays.

3. Combine (Merge)

° Merge the sorted subarrays to produce a fully sorted array.
--- page 4 ---
a.   1) What happens to time complexity when:
a) The number of recursive calls increase?
2
b) The input size reduces faster (e.g., n/2 vs n-1)
2) Solve the following recurrence relation using the recursion tree
method-
8
T(n) = T(n/2) + T(n/4) + n2
Q4
CO-2;
b.   Assume that the numbers given below represent counts of letters in
SO-6;
hundreds from a file. For example, in the file, there will be exactly 20*
BL-5
100 occurrences of the letter ‘a ’, etc.,
a-20, c-11, d-2, e-10, 0-15, m-8, s-10, t-22, u-2
CO-4;
Based on the given data, perform the task mentioned below.
SO-1;   3+2
1) Draw a Huffman tree
BL3
2) Generate Huffman codes for each letter, and calculate the
total length of the encoded file
1+1+1
3) Generate fixed-length coding for each letter (ASCII-7bits)
4) Calculate the total length of fixed length for this file
2
5) Average bit length of the characters.
6) Percentage of reduction when using the Huffman code.
2+3+5
Q5   a.
CO-3;
SO- 2;
BL3   With reference to the n-Queen’s problem,
1) State the problem statement of the n-queen’s problem
2) Explain the Backtracking paradigm, in general.
CO-4;   3) Generate a state-space tree for the 4 queens’ problem using the
SO-1;   b.   backtracking approach.   2+1
BL2
7
********** 4 **********
--- page 5 ---
1) State the problem statement of Matrix Chain multiplication.
Write the recurrence relation to solve using the dynamic
programming approach.
2) Appling Dynamic programming to derive the efficient order of
multiplying four matrices.[A : 4x4, B : 4x5, C : 5x2, D : 2x4]
Q6   a.   Apply the following methods to find the time complexity for the
following recurrence function.
a) Master Theorem   b) Substitution Method
T(n) = 3T(n/3) + n/2   T(n) = 2T(n/2) + nlogn   {for n>1}
b.
5+5
8+2
Q7   Write the asymptotic relation among all three functions.   5+5
CO-4;   a.   1) f(n) = 2n ; g(n) = n! ; h(n) =nlogn
SO-1;
BL3   2) Evaluate Time and Space complexity for the following code snippet
int a =0, b=0; (2)
for( i=0; i<N; i++)
{
for(j=0; j<N; j++)
{
********** 5 **********

[Text in pictures on this page, read by OCR]
1) Problem Statement of the N-Queen’s Problem

The N-Queens Problem is defined as:

Place N queens on an N x N chessboard such that no two queens attack each other.

@ Constraints
A queen can attack:

¢ Horizontally (same row)
© Vertically (same column)
¢ Diagonally

Therefore, the placement must ensure:

© No two queens share the same row
¢ No two queens share the same column

¢ No two queens lie on the same diagonal LV

@ Longest Common Subsequence (LCS) — Interpretation

ZY Problem

Given two sequences:

e© X =21,%,...,L2m
© Y= yi, Yass Yn

Find the longest subsequence common to both (not necessarily contiguous).

v Key Idea (Dynamic Programming)
The problem satisfies:

* Optimal Substructure — LCS of larger strings depends on smaller substrings

© Overlapping Subproblems — Same subproblems are solved repeatedly

Hence, we store results in a table to avoid recomputation.
--- page 6 ---
CO-1;   a=a+j;
SO-1;   }
BL-1   }
for(k=0; k<N; k++)
b=b+k;
8+2
Illustrate the operation of Quicksort on the array A = < 55, 21, 4, 17,
b.   10, 30, 2, 61,72,3>. Analyse the time complexity of the entire operation
across all scenarios. Show the complete data flow.
********** 6 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 274ddb8cb6c8

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CS_7055/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C071)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 11 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data, if necessary.
Q1   Answer briefly:   Marks
A   State any five differences between a pseudo-code and a source-code.
Sol: Differentiate between source code and pseudo-code based on the following
characteristics:
CO1,
SO1,   •   Syntax rules   [5]
• Language dependency
BL2
•   Readability
•   Execution
•   Purpose
[1 Marks for each difference]
CO2, B   A Divide and Conquer algorithm splits a problem of size n into subproblems of   [5]
SO1,
BL2   sizes n/6 and n/6. The merging step takes linear time.
(i) Write the recurrence relation
(ii) Identify whether the division is balanced or unbalanced
[recurrence relation- 3 marks, balanced or unbalanced explanation-2 marks]
CO4, C   State what is an optimization problem and how can it be solved? Define feasible [5]
SO1,
BL2   and optimal solutions.
[optimization problem definition- 2 marks, feasible and optimal solutions
definitions- 1.5 marks each]
CO4, D   Give the general iterative backtracking pseudo-code?   [5]
SO1,
BL2
Sol: 5 marks for correct pseudo-code
********** 1 **********
--- page 2 ---
A   i.   Can you design a non-deterministic algorithm? Also specify which
particular step/s in this algorithm makes it non-deterministic.
Q2   ii.   Draw a well-labelled diagram that explains the relationship between P, NP,
CO1,   [10]
SO1,   NP-Hard, and NP-Complete Complexity Classes.
BL2
Sol: Designing any non-deterministic algorithm (4 marks), Identifying the non-
deterministic steps (3 marks), Diagram (3 marks)
B   Considering the graph below, calculate the shortest path from vertex A with the
help of Bellman-Ford algorithm:
CO4,
SO1,   [10]
BL3
Explain the concept of a negative weight cycle.
Sol: There are total 6 vertices in graph, so we have to relax 5 times all the edges.
The final shortest path from vertex A is [ 0, 1, 3, 5, 0, 3]
stepwise shortest path identification- 7 marks
Negative weight cycle: A negative weight cycle is a cycle in a graph, whose sum
of edge weights is negative. If you traverse the cycle, the total weight
accumulated would be less than zero.
A
Q3   Consider a source emits symbols with frequencies:
CO3,   (a:10), (b:15), (c:30), (d:16), (e:29)   [10]
SO1,
BL4   i.   Construct Huffman tree
ii.   Construct Huffman codes
********** 2 **********

[Text in pictures on this page, read by OCR]
Algorithm |Backtrack(n)

// This schema describes the backtracking process.
// All solutions are generated in x[{1 : n] and printed
// as soon as they are determined.

k:=1;
while (k 4 0) do

if (there remains an untried z[k] € T(a({1], 2[2],...,
z[k —1]) and B,(z{1],...,2[k]) is true) then

if (x{1],...,2[k] is a path to an answer node)
then write (x[{1 : k]);
k :=k+1; // Consider the next set.

else k := k — 1; // Backtrack to the previous set.
+
}
--- page 3 ---
iii.   Compute total weighted path length
iv.   Explain why most frequent symbol gets shortest code
Sol:
i.   Construct Huffman tree - 3marks
Merging steps:
• 10+15=25
• 16+25=41
• 29+30=59
• 41+59=100
ii.   Codes (one valid set): - 3 marks
•   c → 11
•   e → 10
• d → 011
• b → 0101
•   a → 0100
iii.   Weighted path length: 10×4+15×4+16×3+29×2+30×2=266 – 2 marks
iv.   Most frequent symbol gets shortest code Explanation: - 2 marks
• Huffman minimizes weighted cost
•   High-frequency symbols placed closer to root
→ shorter codes
B   Consider the following recursive algorithm:   [10]
void fun(int n){
if(n <= 1) return;
for(int i = 0; i < n; i++){
for(int j = 0; j < n; j++){
cout << i+j << " ";
}
CO1,
}
SO1,
fun(n/2);
BL4
fun(n/2);
}
i.   Form the recurrence relation equation
ii.   Analyze the algorithm by using applicable method
iii.   Identify and justify the applicable case
Sol:
********** 3 **********
--- page 4 ---
A   Consider the following matrix chain:   [10]
A1 (5 x 4), A2 (4 x 6), A3 (6 x 2), A4 (2 x 7)
i.   Using Dynamic Programming, compute the minimum number of scalar
multiplications needed to multiply
ii.   Determine the optimal parenthesization of the matrix chain.
Sol:
Solution:
Q4
CO4,
SO1,   Split Table
BL4
Start from m[1,5] = 160
Look at s[1,5] = 3, so split as:
(A1A2A3)  and  (A4A5)
********** 4 **********

[Text in pictures on this page, read by OCR]
. Form the recurrence relation equation [4 marks]
Work per call = O(n’) (nested loops) — [2 marks]
T(n)= 2r( ; )+ [2 marks]

. Analyze the algorithm by using applicable method [3

marks]

Apply Master Theorem:

© a=2,b=2, n°*2 =n

e f(n)=n? > n—Case3

. Identify and justify the applicable case [3 Marks]
Final Complexity=O(n" )

Justification: dominant term

Final m-table

i\j 1 2 3 4 5

1 oO 120 88 158 160
2 0 48 104 114
3 0 84 78
4 O 42

This table stores the value of k where optimal split occurs.

i\j 1 2 3
1 - 1 1
2 - 2
3 -
4
--- page 5 ---
Then recursively:
s[1,3]=1⇒(A1)(A2A3)
s[4,5]=4⇒(A4)(A5)
Minimum Cost : 160
Optimal Parenthesization: ((A1(A2A3))(A4A5))
Marking Scheme –
Correct Formula – 1 mark
m table– 6 marks (1 mark for each correct value)
Split table – 2 marks
Correct Parenthesization – 1 mark
B   Discuss the correlation of fractional knapsack problem with the Greedy method. [10]
Solve the following problem using the same approach and find the solution to fill
the knapsack. There are 4 items given in the table below along with its weights and
profits. The maximum size of the knapsack is 40.
Item   Weight   Profit
A   10   75
B   5   25
C   20   50
D   16   100
What will be the time and space complexity of the algorithm?
Sol: Discussion on correlation (3 Marks)
The Greedy Method is an algorithmic approach where:
• At each step, we make the locally optimal choice
CO3,   • With the hope that it leads to a globally optimal solution
SO1,   •   It does not reconsider previous choices
BL3
In the fractional knapsack problem:
• We select items based on maximum value per unit weight (profit/weight
ratio), that is the greedy approach.
• At every step, we pick the best available option
The greedy method works perfectly here because:
•   Items can be broken into fractions
• So we can always take the “best part” of any item
• The optimal solution can be built from optimal choices at each step
Solution- (5 Marks) Student need to write each step
Sort in Descending Order of Profit / Weight ratio
Order of selection:
1. A → 7.5
2. D → 6.25
3. B → 5.0
4. C → 2.5
Total Profit = 75 + 100 + 25 + 22.5 = 222.5
********** 5 **********
--- page 6 ---
Item Selected: Final Answer
• A → Full
• D → Full
• B → Full
• C → 45% (fractional)
Complexity: (2 Marks)
3. Ratio Calculation:
• Time = O(n)
2. Sorting:
• Time = O(n log n)
3. Selection Loop:
• Time = O(n)
Overall Time Complexity: O(n log n )
Space Complexity O(n)
A   Given a set A = {3, 5, 6, 7} and a target sum M=15,   [10]
i.   Find all subsets of A whose sum is equal to M using a backtracking
approach.
ii.   Draw the state space tree to illustrate the solution process.
iii.   Write the pseudo-code for the Sum of Subsets algorithm.
Sol: state-space tree – 4 marks
Q5
CO4,
SO1,
BL3
1 solutions- 2 marks
Pseudo-code – 4 marks
B   [10]
For the sequences:
X="ABCDGH", and Y="AEDFHR"
CO4,   i.   Build the LCS dynamic programming table
SO1,   ii.   Identify the length of LCS and LCS
BL3   iii.   Identify its time complexity
iv.
Sol: LCS Table (DP Matrix)
********** 6 **********
--- page 7 ---
LCS Length: 3
LCS: "ADH"
Time complexity In dynamic programming, only table of size m x n is filled up
using two nested for loops. So running time of the dynamic programming
approach would take O(m x n)
Marks: Table construction-4 marks, length of LCS and the LCS – 2 mark each,
Time complexity-2 marks
A   Analyze the following pseudocode and answer the given questions:   [10]
for i = 0 to n-1:
min = i
for j = i+1 to n-1:
if A[j] < A[min]:
min = j
swap(A[i], A[min])
Q6   i.   Identify algorithm
ii.   Count exact number of comparisons
CO2,
SO1,   iii.   What are the best-case and worst-case time complexities of this
BL4   algorithm? Justify.
Sol:
3. best-case and worst-case time complexities: O(n^2)
CO1, B   [10]
SO1,   Compare the following pairs and determine whether:
BL4
********** 7 **********
--- page 8 ---
Sol:
i.   f(n) =O (g(n))
ii. f(n) =O (g(n))
iii. f(n) = Ω(g(n))
iv. f(n) = Theta(g(n))
v. f(n) = Ω(g(n))
[each part carries 2 marks each, 5 x 2 = 10 marks]
A   Determine the time complexity of the Min–Max algorithm by formulating and
analyzing mathematical equations for both the iterative and recursive methods.
Answer: Description of both methods (2 Marks)
•   Correct identification of:
   Iterative (traditional) method → 1 Mark
 Recursive (divide-and-conquer) method → 1 Mark
Mathematical Formulation (Equations) (3 Marks)
Q7
CO2,   •   Iterative method equation: 𝑇(𝑛)=2(𝑛−1)→ 1.5 Marks   [10]
SO1,   •   Recursive method recurrence: 𝑇(𝑛)=2𝑇(𝑛/2)+2, with base case → 1.5
BL4   Marks
Derivation / Solution of Equations (3 Marks)
•   Iterative method simplification to 𝑂(𝑛) → 1 Mark
•   Solving recurrence using:
Expansion / substitution / Master theorem → 2 Marks
Final result: O(n), ((3𝑛)/2)−2
Comparison & Interpretation (2 Marks)
B   i. How do we compare the growth rate of two functions?
ii. What do you mean by “dominant term” in a function. Explain with an
example.
CO1,   Sol: i. Using asymptotic notations:
SO1,   [5]
BL2   •   If f(n)=O(g(n)) → f grows no faster than g
•   If f(n)=Ω(g(n)) → f grows at least as fast as g
•   If f(n)=Θ(g(n)) → both grow at the same rate
[2 marks]
********** 8 **********
--- page 9 ---
ii. The dominant term is the term that grows the fastest as ￼￼n→∞, and
therefore determines the overall growth rate of the function. [2 marks]
E.g. f(n) = 5n2 + 3n + 7; here dominant term is n2
[1 mark]
C   Define Greedy Algorithm. Explain the difference between local optimal and global
optimal solutions with an example.
Sol: A Greedy Algorithm is an approach that makes the best possible choice at each
step (locally optimal) with the hope that these choices will lead to a globally
optimal solution.
CO3,   Difference between Local Optimal and Global Optimal:
SO1,   [5]
BL2   Term   Meaning   Example
Choosing the largest value item that
Local   The best choice at the current
fits in the knapsack at that moment
Optimal   step or subproblem.
(Fractional Knapsack).
Global   The best solution overall for the Maximum total profit that can be
Optimal   entire problem.   achieved after considering all items.
[greedy definition- 2 marks, differences- 3 marks]
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper d148b8a27a4e

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Computer_7002/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C071)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 11 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data, if necessary.
Q1   Answer briefly:   Marks
A   State any five differences between a pseudo-code and a source-code.
Sol: Differentiate between source code and pseudo-code based on the following
characteristics:
CO1,
SO1,   •   Syntax rules   [5]
• Language dependency
BL2
•   Readability
•   Execution
•   Purpose
[1 Marks for each difference]
CO2, B   A Divide and Conquer algorithm splits a problem of size n into subproblems of   [5]
SO1,
BL2   sizes n/6 and n/6. The merging step takes linear time.
(i) Write the recurrence relation
(ii) Identify whether the division is balanced or unbalanced
[recurrence relation- 3 marks, balanced or unbalanced explanation-2 marks]
CO4, C   State what is an optimization problem and how can it be solved? Define feasible [5]
SO1,
BL2   and optimal solutions.
[optimization problem definition- 2 marks, feasible and optimal solutions
definitions- 1.5 marks each]
CO4, D   Give the general iterative backtracking pseudo-code?   [5]
SO1,
BL2
Sol: 5 marks for correct pseudo-code
********** 1 **********
--- page 2 ---
A   i.   Can you design a non-deterministic algorithm? Also specify which
particular step/s in this algorithm makes it non-deterministic.
Q2   ii.   Draw a well-labelled diagram that explains the relationship between P, NP,
CO1,   [10]
SO1,   NP-Hard, and NP-Complete Complexity Classes.
BL2
Sol: Designing any non-deterministic algorithm (4 marks), Identifying the non-
deterministic steps (3 marks), Diagram (3 marks)
B   Considering the graph below, calculate the shortest path from vertex A with the
help of Bellman-Ford algorithm:
CO4,
SO1,   [10]
BL3
Explain the concept of a negative weight cycle.
Sol: There are total 6 vertices in graph, so we have to relax 5 times all the edges.
The final shortest path from vertex A is [ 0, 1, 3, 5, 0, 3]
stepwise shortest path identification- 7 marks
Negative weight cycle: A negative weight cycle is a cycle in a graph, whose sum
of edge weights is negative. If you traverse the cycle, the total weight
accumulated would be less than zero.
A
Q3   Consider a source emits symbols with frequencies:
CO3,   (a:10), (b:15), (c:30), (d:16), (e:29)   [10]
SO1,
BL4   i.   Construct Huffman tree
ii.   Construct Huffman codes
********** 2 **********

[Text in pictures on this page, read by OCR]
Algorithm |Backtrack(n)

// This schema describes the backtracking process.
// All solutions are generated in x[{1 : n] and printed
// as soon as they are determined.

k:=1;
while (k 4 0) do

if (there remains an untried z[k] € T(a({1], 2[2],...,
z[k —1]) and B,(z{1],...,2[k]) is true) then

if (x{1],...,2[k] is a path to an answer node)
then write (x[{1 : k]);
k :=k+1; // Consider the next set.

else k := k — 1; // Backtrack to the previous set.
+
}
--- page 3 ---
iii.   Compute total weighted path length
iv.   Explain why most frequent symbol gets shortest code
Sol:
i.   Construct Huffman tree - 3marks
Merging steps:
• 10+15=25
• 16+25=41
• 29+30=59
• 41+59=100
ii.   Codes (one valid set): - 3 marks
•   c → 11
•   e → 10
• d → 011
• b → 0101
•   a → 0100
iii.   Weighted path length: 10×4+15×4+16×3+29×2+30×2=266 – 2 marks
iv.   Most frequent symbol gets shortest code Explanation: - 2 marks
• Huffman minimizes weighted cost
•   High-frequency symbols placed closer to root
→ shorter codes
B   Consider the following recursive algorithm:   [10]
void fun(int n){
if(n <= 1) return;
for(int i = 0; i < n; i++){
for(int j = 0; j < n; j++){
cout << i+j << " ";
}
CO1,
}
SO1,
fun(n/2);
BL4
fun(n/2);
}
i.   Form the recurrence relation equation
ii.   Analyze the algorithm by using applicable method
iii.   Identify and justify the applicable case
Sol:
********** 3 **********
--- page 4 ---
A   Consider the following matrix chain:   [10]
A1 (5 x 4), A2 (4 x 6), A3 (6 x 2), A4 (2 x 7)
i.   Using Dynamic Programming, compute the minimum number of scalar
multiplications needed to multiply
ii.   Determine the optimal parenthesization of the matrix chain.
Sol:
Solution:
Q4
CO4,
SO1,   Split Table
BL4
Start from m[1,5] = 160
Look at s[1,5] = 3, so split as:
(A1A2A3)  and  (A4A5)
********** 4 **********

[Text in pictures on this page, read by OCR]
. Form the recurrence relation equation [4 marks]
Work per call = O(n’) (nested loops) — [2 marks]
T(n)= 2r( ; )+ [2 marks]

. Analyze the algorithm by using applicable method [3

marks]

Apply Master Theorem:

© a=2,b=2, n°*2 =n

e f(n)=n? > n—Case3

. Identify and justify the applicable case [3 Marks]
Final Complexity=O(n" )

Justification: dominant term

Final m-table

i\j 1 2 3 4 5

1 oO 120 88 158 160
2 0 48 104 114
3 0 84 78
4 O 42

This table stores the value of k where optimal split occurs.

i\j 1 2 3
1 - 1 1
2 - 2
3 -
4
--- page 5 ---
Then recursively:
s[1,3]=1⇒(A1)(A2A3)
s[4,5]=4⇒(A4)(A5)
Minimum Cost : 160
Optimal Parenthesization: ((A1(A2A3))(A4A5))
Marking Scheme –
Correct Formula – 1 mark
m table– 6 marks (1 mark for each correct value)
Split table – 2 marks
Correct Parenthesization – 1 mark
B   Discuss the correlation of fractional knapsack problem with the Greedy method. [10]
Solve the following problem using the same approach and find the solution to fill
the knapsack. There are 4 items given in the table below along with its weights and
profits. The maximum size of the knapsack is 40.
Item   Weight   Profit
A   10   75
B   5   25
C   20   50
D   16   100
What will be the time and space complexity of the algorithm?
Sol: Discussion on correlation (3 Marks)
The Greedy Method is an algorithmic approach where:
• At each step, we make the locally optimal choice
CO3,   • With the hope that it leads to a globally optimal solution
SO1,   •   It does not reconsider previous choices
BL3
In the fractional knapsack problem:
• We select items based on maximum value per unit weight (profit/weight
ratio), that is the greedy approach.
• At every step, we pick the best available option
The greedy method works perfectly here because:
•   Items can be broken into fractions
• So we can always take the “best part” of any item
• The optimal solution can be built from optimal choices at each step
Solution- (5 Marks) Student need to write each step
Sort in Descending Order of Profit / Weight ratio
Order of selection:
1. A → 7.5
2. D → 6.25
3. B → 5.0
4. C → 2.5
Total Profit = 75 + 100 + 25 + 22.5 = 222.5
********** 5 **********
--- page 6 ---
Item Selected: Final Answer
• A → Full
• D → Full
• B → Full
• C → 45% (fractional)
Complexity: (2 Marks)
3. Ratio Calculation:
• Time = O(n)
2. Sorting:
• Time = O(n log n)
3. Selection Loop:
• Time = O(n)
Overall Time Complexity: O(n log n )
Space Complexity O(n)
A   Given a set A = {3, 5, 6, 7} and a target sum M=15,   [10]
i.   Find all subsets of A whose sum is equal to M using a backtracking
approach.
ii.   Draw the state space tree to illustrate the solution process.
iii.   Write the pseudo-code for the Sum of Subsets algorithm.
Sol: state-space tree – 4 marks
Q5
CO4,
SO1,
BL3
1 solutions- 2 marks
Pseudo-code – 4 marks
B   [10]
For the sequences:
X="ABCDGH", and Y="AEDFHR"
CO4,   i.   Build the LCS dynamic programming table
SO1,   ii.   Identify the length of LCS and LCS
BL3   iii.   Identify its time complexity
iv.
Sol: LCS Table (DP Matrix)
********** 6 **********
--- page 7 ---
LCS Length: 3
LCS: "ADH"
Time complexity In dynamic programming, only table of size m x n is filled up
using two nested for loops. So running time of the dynamic programming
approach would take O(m x n)
Marks: Table construction-4 marks, length of LCS and the LCS – 2 mark each,
Time complexity-2 marks
A   Analyze the following pseudocode and answer the given questions:   [10]
for i = 0 to n-1:
min = i
for j = i+1 to n-1:
if A[j] < A[min]:
min = j
swap(A[i], A[min])
Q6   i.   Identify algorithm
ii.   Count exact number of comparisons
CO2,
SO1,   iii.   What are the best-case and worst-case time complexities of this
BL4   algorithm? Justify.
Sol:
3. best-case and worst-case time complexities: O(n^2)
CO1, B   [10]
SO1,   Compare the following pairs and determine whether:
BL4
********** 7 **********
--- page 8 ---
Sol:
i.   f(n) =O (g(n))
ii. f(n) =O (g(n))
iii. f(n) = Ω(g(n))
iv. f(n) = Theta(g(n))
v. f(n) = Ω(g(n))
[each part carries 2 marks each, 5 x 2 = 10 marks]
A   Determine the time complexity of the Min–Max algorithm by formulating and
analyzing mathematical equations for both the iterative and recursive methods.
Answer: Description of both methods (2 Marks)
•   Correct identification of:
   Iterative (traditional) method → 1 Mark
 Recursive (divide-and-conquer) method → 1 Mark
Mathematical Formulation (Equations) (3 Marks)
Q7
CO2,   •   Iterative method equation: 𝑇(𝑛)=2(𝑛−1)→ 1.5 Marks   [10]
SO1,   •   Recursive method recurrence: 𝑇(𝑛)=2𝑇(𝑛/2)+2, with base case → 1.5
BL4   Marks
Derivation / Solution of Equations (3 Marks)
•   Iterative method simplification to 𝑂(𝑛) → 1 Mark
•   Solving recurrence using:
Expansion / substitution / Master theorem → 2 Marks
Final result: O(n), ((3𝑛)/2)−2
Comparison & Interpretation (2 Marks)
B   i. How do we compare the growth rate of two functions?
ii. What do you mean by “dominant term” in a function. Explain with an
example.
CO1,   Sol: i. Using asymptotic notations:
SO1,   [5]
BL2   •   If f(n)=O(g(n)) → f grows no faster than g
•   If f(n)=Ω(g(n)) → f grows at least as fast as g
•   If f(n)=Θ(g(n)) → both grow at the same rate
[2 marks]
********** 8 **********
--- page 9 ---
ii. The dominant term is the term that grows the fastest as ￼￼n→∞, and
therefore determines the overall growth rate of the function. [2 marks]
E.g. f(n) = 5n2 + 3n + 7; here dominant term is n2
[1 mark]
C   Define Greedy Algorithm. Explain the difference between local optimal and global
optimal solutions with an example.
Sol: A Greedy Algorithm is an approach that makes the best possible choice at each
step (locally optimal) with the hope that these choices will lead to a globally
optimal solution.
CO3,   Difference between Local Optimal and Global Optimal:
SO1,   [5]
BL2   Term   Meaning   Example
Choosing the largest value item that
Local   The best choice at the current
fits in the knapsack at that moment
Optimal   step or subproblem.
(Fractional Knapsack).
Global   The best solution overall for the Maximum total profit that can be
Optimal   entire problem.   achieved after considering all items.
[greedy definition- 2 marks, differences- 3 marks]
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 1885b1d47dc0

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_Computer_7047/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C071)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 11 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data, if necessary.
Q1   Answer briefly:   Marks
A   State any five differences between a pseudo-code and a source-code.
Sol: Differentiate between source code and pseudo-code based on the following
characteristics:
CO1,
SO1,   •   Syntax rules   [5]
• Language dependency
BL2
•   Readability
•   Execution
•   Purpose
[1 Marks for each difference]
CO2, B   A Divide and Conquer algorithm splits a problem of size n into subproblems of   [5]
SO1,
BL2   sizes n/6 and n/6. The merging step takes linear time.
(i) Write the recurrence relation
(ii) Identify whether the division is balanced or unbalanced
[recurrence relation- 3 marks, balanced or unbalanced explanation-2 marks]
CO4, C   State what is an optimization problem and how can it be solved? Define feasible [5]
SO1,
BL2   and optimal solutions.
[optimization problem definition- 2 marks, feasible and optimal solutions
definitions- 1.5 marks each]
CO4, D   Give the general iterative backtracking pseudo-code?   [5]
SO1,
BL2
Sol: 5 marks for correct pseudo-code
********** 1 **********
--- page 2 ---
A   i.   Can you design a non-deterministic algorithm? Also specify which
particular step/s in this algorithm makes it non-deterministic.
Q2   ii.   Draw a well-labelled diagram that explains the relationship between P, NP,
CO1,   [10]
SO1,   NP-Hard, and NP-Complete Complexity Classes.
BL2
Sol: Designing any non-deterministic algorithm (4 marks), Identifying the non-
deterministic steps (3 marks), Diagram (3 marks)
B   Considering the graph below, calculate the shortest path from vertex A with the
help of Bellman-Ford algorithm:
CO4,
SO1,   [10]
BL3
Explain the concept of a negative weight cycle.
Sol: There are total 6 vertices in graph, so we have to relax 5 times all the edges.
The final shortest path from vertex A is [ 0, 1, 3, 5, 0, 3]
stepwise shortest path identification- 7 marks
Negative weight cycle: A negative weight cycle is a cycle in a graph, whose sum
of edge weights is negative. If you traverse the cycle, the total weight
accumulated would be less than zero.
A
Q3   Consider a source emits symbols with frequencies:
CO3,   (a:10), (b:15), (c:30), (d:16), (e:29)   [10]
SO1,
BL4   i.   Construct Huffman tree
ii.   Construct Huffman codes
********** 2 **********

[Text in pictures on this page, read by OCR]
Algorithm |Backtrack(n)

// This schema describes the backtracking process.
// All solutions are generated in x[{1 : n] and printed
// as soon as they are determined.

k:=1;
while (k 4 0) do

if (there remains an untried z[k] € T(a({1], 2[2],...,
z[k —1]) and B,(z{1],...,2[k]) is true) then

if (x{1],...,2[k] is a path to an answer node)
then write (x[{1 : k]);
k :=k+1; // Consider the next set.

else k := k — 1; // Backtrack to the previous set.
+
}
--- page 3 ---
iii.   Compute total weighted path length
iv.   Explain why most frequent symbol gets shortest code
Sol:
i.   Construct Huffman tree - 3marks
Merging steps:
• 10+15=25
• 16+25=41
• 29+30=59
• 41+59=100
ii.   Codes (one valid set): - 3 marks
•   c → 11
•   e → 10
• d → 011
• b → 0101
•   a → 0100
iii.   Weighted path length: 10×4+15×4+16×3+29×2+30×2=266 – 2 marks
iv.   Most frequent symbol gets shortest code Explanation: - 2 marks
• Huffman minimizes weighted cost
•   High-frequency symbols placed closer to root
→ shorter codes
B   Consider the following recursive algorithm:   [10]
void fun(int n){
if(n <= 1) return;
for(int i = 0; i < n; i++){
for(int j = 0; j < n; j++){
cout << i+j << " ";
}
CO1,
}
SO1,
fun(n/2);
BL4
fun(n/2);
}
i.   Form the recurrence relation equation
ii.   Analyze the algorithm by using applicable method
iii.   Identify and justify the applicable case
Sol:
********** 3 **********
--- page 4 ---
A   Consider the following matrix chain:   [10]
A1 (5 x 4), A2 (4 x 6), A3 (6 x 2), A4 (2 x 7)
i.   Using Dynamic Programming, compute the minimum number of scalar
multiplications needed to multiply
ii.   Determine the optimal parenthesization of the matrix chain.
Sol:
Solution:
Q4
CO4,
SO1,   Split Table
BL4
Start from m[1,5] = 160
Look at s[1,5] = 3, so split as:
(A1A2A3)  and  (A4A5)
********** 4 **********

[Text in pictures on this page, read by OCR]
. Form the recurrence relation equation [4 marks]
Work per call = O(n’) (nested loops) — [2 marks]
T(n)= 2r( ; )+ [2 marks]

. Analyze the algorithm by using applicable method [3

marks]

Apply Master Theorem:

© a=2,b=2, n°*2 =n

e f(n)=n? > n—Case3

. Identify and justify the applicable case [3 Marks]
Final Complexity=O(n" )

Justification: dominant term

Final m-table

i\j 1 2 3 4 5

1 oO 120 88 158 160
2 0 48 104 114
3 0 84 78
4 O 42

This table stores the value of k where optimal split occurs.

i\j 1 2 3
1 - 1 1
2 - 2
3 -
4
--- page 5 ---
Then recursively:
s[1,3]=1⇒(A1)(A2A3)
s[4,5]=4⇒(A4)(A5)
Minimum Cost : 160
Optimal Parenthesization: ((A1(A2A3))(A4A5))
Marking Scheme –
Correct Formula – 1 mark
m table– 6 marks (1 mark for each correct value)
Split table – 2 marks
Correct Parenthesization – 1 mark
B   Discuss the correlation of fractional knapsack problem with the Greedy method. [10]
Solve the following problem using the same approach and find the solution to fill
the knapsack. There are 4 items given in the table below along with its weights and
profits. The maximum size of the knapsack is 40.
Item   Weight   Profit
A   10   75
B   5   25
C   20   50
D   16   100
What will be the time and space complexity of the algorithm?
Sol: Discussion on correlation (3 Marks)
The Greedy Method is an algorithmic approach where:
• At each step, we make the locally optimal choice
CO3,   • With the hope that it leads to a globally optimal solution
SO1,   •   It does not reconsider previous choices
BL3
In the fractional knapsack problem:
• We select items based on maximum value per unit weight (profit/weight
ratio), that is the greedy approach.
• At every step, we pick the best available option
The greedy method works perfectly here because:
•   Items can be broken into fractions
• So we can always take the “best part” of any item
• The optimal solution can be built from optimal choices at each step
Solution- (5 Marks) Student need to write each step
Sort in Descending Order of Profit / Weight ratio
Order of selection:
1. A → 7.5
2. D → 6.25
3. B → 5.0
4. C → 2.5
Total Profit = 75 + 100 + 25 + 22.5 = 222.5
********** 5 **********
--- page 6 ---
Item Selected: Final Answer
• A → Full
• D → Full
• B → Full
• C → 45% (fractional)
Complexity: (2 Marks)
3. Ratio Calculation:
• Time = O(n)
2. Sorting:
• Time = O(n log n)
3. Selection Loop:
• Time = O(n)
Overall Time Complexity: O(n log n )
Space Complexity O(n)
A   Given a set A = {3, 5, 6, 7} and a target sum M=15,   [10]
i.   Find all subsets of A whose sum is equal to M using a backtracking
approach.
ii.   Draw the state space tree to illustrate the solution process.
iii.   Write the pseudo-code for the Sum of Subsets algorithm.
Sol: state-space tree – 4 marks
Q5
CO4,
SO1,
BL3
1 solutions- 2 marks
Pseudo-code – 4 marks
B   [10]
For the sequences:
X="ABCDGH", and Y="AEDFHR"
CO4,   i.   Build the LCS dynamic programming table
SO1,   ii.   Identify the length of LCS and LCS
BL3   iii.   Identify its time complexity
iv.
Sol: LCS Table (DP Matrix)
********** 6 **********
--- page 7 ---
LCS Length: 3
LCS: "ADH"
Time complexity In dynamic programming, only table of size m x n is filled up
using two nested for loops. So running time of the dynamic programming
approach would take O(m x n)
Marks: Table construction-4 marks, length of LCS and the LCS – 2 mark each,
Time complexity-2 marks
A   Analyze the following pseudocode and answer the given questions:   [10]
for i = 0 to n-1:
min = i
for j = i+1 to n-1:
if A[j] < A[min]:
min = j
swap(A[i], A[min])
Q6   i.   Identify algorithm
ii.   Count exact number of comparisons
CO2,
SO1,   iii.   What are the best-case and worst-case time complexities of this
BL4   algorithm? Justify.
Sol:
3. best-case and worst-case time complexities: O(n^2)
CO1, B   [10]
SO1,   Compare the following pairs and determine whether:
BL4
********** 7 **********
--- page 8 ---
Sol:
i.   f(n) =O (g(n))
ii. f(n) =O (g(n))
iii. f(n) = Ω(g(n))
iv. f(n) = Theta(g(n))
v. f(n) = Ω(g(n))
[each part carries 2 marks each, 5 x 2 = 10 marks]
A   Determine the time complexity of the Min–Max algorithm by formulating and
analyzing mathematical equations for both the iterative and recursive methods.
Answer: Description of both methods (2 Marks)
•   Correct identification of:
   Iterative (traditional) method → 1 Mark
 Recursive (divide-and-conquer) method → 1 Mark
Mathematical Formulation (Equations) (3 Marks)
Q7
CO2,   •   Iterative method equation: 𝑇(𝑛)=2(𝑛−1)→ 1.5 Marks   [10]
SO1,   •   Recursive method recurrence: 𝑇(𝑛)=2𝑇(𝑛/2)+2, with base case → 1.5
BL4   Marks
Derivation / Solution of Equations (3 Marks)
•   Iterative method simplification to 𝑂(𝑛) → 1 Mark
•   Solving recurrence using:
Expansion / substitution / Master theorem → 2 Marks
Final result: O(n), ((3𝑛)/2)−2
Comparison & Interpretation (2 Marks)
B   i. How do we compare the growth rate of two functions?
ii. What do you mean by “dominant term” in a function. Explain with an
example.
CO1,   Sol: i. Using asymptotic notations:
SO1,   [5]
BL2   •   If f(n)=O(g(n)) → f grows no faster than g
•   If f(n)=Ω(g(n)) → f grows at least as fast as g
•   If f(n)=Θ(g(n)) → both grow at the same rate
[2 marks]
********** 8 **********
--- page 9 ---
ii. The dominant term is the term that grows the fastest as ￼￼n→∞, and
therefore determines the overall growth rate of the function. [2 marks]
E.g. f(n) = 5n2 + 3n + 7; here dominant term is n2
[1 mark]
C   Define Greedy Algorithm. Explain the difference between local optimal and global
optimal solutions with an example.
Sol: A Greedy Algorithm is an approach that makes the best possible choice at each
step (locally optimal) with the hope that these choices will lead to a globally
optimal solution.
CO3,   Difference between Local Optimal and Global Optimal:
SO1,   [5]
BL2   Term   Meaning   Example
Choosing the largest value item that
Local   The best choice at the current
fits in the knapsack at that moment
Optimal   step or subproblem.
(Fractional Knapsack).
Global   The best solution overall for the Maximum total profit that can be
Optimal   entire problem.   achieved after considering all items.
[greedy definition- 2 marks, differences- 3 marks]
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper bc955bdf40da

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CSBS_7036/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 72.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSBS)/MBA Tech (AI)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Attempt any 4 questions from the remaining questions.
6. Total 5 questions to be attempted.
Q.1 Attempt all questions   [20
:   ]
(a) Discuss time and space complexity. Compute the time and space complexity of the [5]
code segment given below:
main ( )
{
for(i=1; i<=n; i++)
{
for(j=1; j<=n; j=2*j)
{
x = y+z;
}
}
}
Solution: Time complexity measures the amount of time an
algorithm takes to complete as a function of the input size. It’s a
way to estimate the running time of an algorithm.
Space complexity measures the amount of memory an algorithm
uses as a function of the input size.
Time complexity O(nlogn), space complexity O(1)
********** 1 **********
--- page 2 ---
(b) Build the Huffman tree and generate the codeword for the given characters:   [5]
character : a b c d e   f
Frequency : 5 9 12 13 16 45
Solution: Steps to Build Huffman Tree (Greedy Algorithm)
Step 1: Initialize a Min-Heap with all characters sorted by frequency.
We use a priority queue (or min-heap) to always select the two lowest-frequency
nodes.
Step 2: Combine two lowest-frequency nodes into a new node.
The new node’s frequency is the sum of the two.
This new node becomes a parent, and the two nodes become its left and right children.
Repeat until only one node (root) remains.
[100]
/   \
[45]   [55]
/   \
[25]   [30]
/ \   /   \
[12] [13] [14] [16]
(c) (d) [5] [9] (e)
(a) (b)
Character Frequency Huffman Code
a   5   1100
b   9   1101
c   12   100
d   13   101
e   16   111
f   45   0
(c) Give the difference between dynamic programing and divide & conquer technique.   [5]
Solution:
Basis of Difference Divide and Conquer Dynamic Programming
Divides the problem into
Divides the problem into overlapping
independent subproblems, solves
Approach   subproblems, solves each subproblem
them recursively, and combines
once, and stores the result for reuse.
their results.
Overlapping   Subproblems are independent Subproblems are dependent
Subproblems   (no repetition).   and repeated.
Optimal   May or may not have optimal   Always has optimal
Substructure   substructure.   substructure property.
Uses table (array/matrix) or
Storage /   Does not use storage of
memoization to store intermediate
Memoization   intermediate results.
results.
(d) Generate the solution by drawing state space tree to place the queens on 4x4 [5]
chessboard using backtracking approach.
********** 2 **********
--- page 3 ---
Solution:
Q.2 (a)   i. Define Master’s theorem for computing time complexity.   [10
ii Consider the following recurrence   ]
T(𝑛)= T(n−1)+𝑛, 𝑛>0 ;
1   n=0
Compute the time complexity using substitution method
Solution: 5 marks each
Masters Theorem
Substitution method
********** 3 **********

[Text in pictures on this page, read by OCR]
The Master Method depends on the following Theorem:

Theorem: Let a => 1 and b > 1 be constants, let f(n) be a function, and let T(n) be
defined on the nonnegative integers by the recurrence:

T(n) =aT (7) +f(n)

Then T(n) can be bounded asymptotically as follows.

1. If f(n) = O(n!8 2) for some constant ¢ > 0, then T(n) = O(n!°8 2),
2. If f(n) = O(n!8 4), then T(n) = O(n! * ign).
3. if f(n) = Q(n!& *+) for some constant £ > 0, and if a- f (7) = cf(n) for some constant

¢ < 1 and all sufficiently large n, then T(n) = O(f(n)). F 4
--- page 4 ---
(b) Consider the problem of finding the Longest Common Subsequence (LCS) between   [10
two given strings S1 = TAGTCACG and S2 = AGACTGTC.   ]
(i)   Generate the longest common subsequence of the given strings. Show
each step.
(ii)   Write the algorithm for generating the longest common subsequence and
compute the time complexity.
Solution:
4 marks generation of LCS, 4 marks algorithm, 2 marks time complexity
i.
The LCS for the above example is AGACG of length 5.
ii.   Algorithm
********** 4 **********

[Text in pictures on this page, read by OCR]
T(n) =T(n—1)+n
Substitute for T(n — 1):
T(n) = [T(n— 2) + (n—1)] +n=T(n—2) + (n—1) +n
Substitute again:
T(n) = T(n—3)+(n—2)+(n—-1) +n

Continuing this pattern k times:

k-1

T(n) =T(n—k) + S\(n-i)

i=0
--- page 5 ---
Time Complexity: O(mxn)
Q.3 (a)   (i) Write the algorithm of merging step of merge sort.   [10
]
(ii) Use Merge sort to sort the array of numbers {15, 6, 5, 17, 22, 8, 12, 21}.
(iii)   Write the recurrence equation of Merge sort and find the time complexity of
Merge sort by substitution method.
Solution: Algorithm ( 4 marks), solution (3 marks), time complexity ( 3 marks)
MERGE(A, p, q, r)
1. n1 = q - p + 1
2. n2 = r - q
3. Create arrays L[1..n1+1] and R[1..n2+1]
4. for i = 1 to n1
L[i] = A[p + i - 1]
5. for j = 1 to n2
R[j] = A[q + j]
6. L[n1 + 1] = ∞   // Sentinel value
7. R[n2 + 1] = ∞
8. i = 1, j = 1
9. for k = p to r
if L[i] ≤ R[j]
A[k] = L[i]
i = i + 1
********** 5 **********

[Text in pictures on this page, read by OCR]
LCS-LENGTH(X, Y)

1 m= X.length

2 n=Y.length

3 let b[l..m,1..n] and c[0..m,0..n] be new tables
4 fori = ltom

5 cfi,0] = 0

6 for 7 = Oton

7 co, 7] =0

8 fori = ltom

9 for j = lton

10 ifx; == y;

i cli, j] = ck -—1,7 -1]+1
12 big] ="

13 elseif c[i — 1, j] = cfi,j —1]
14 cli, j] = ci —1.j]

15 bi. jJ="t"

16 else cli, j] = cli. j — 1]

17 bli, j] = “—”

18 return c andb
--- page 6 ---
else
A[k] = R[j]
j = j + 1
Recurse on both halves:
•   Left half: [15, 6, 5, 17] → split into [15, 6] and [5, 17]
o [15, 6] → merge → [6, 15]
o [5, 17] → merge → [5, 17]
o Merge [6, 15] and [5, 17] → [5, 6, 15, 17]
• Right half: [22, 8, 12, 21] → split into [22, 8] and [12, 21]
o [22, 8] → merge → [8, 22]
o [12, 21] → merge → [12, 21]
o Merge [8, 22] and [12, 21] → [8, 12, 21, 22]
Final Merge:
Merge [5, 6, 15, 17] and [8, 12, 21, 22]
********** 6 **********

[Text in pictures on this page, read by OCR]
Step 1: Expand once

Step 2: Expand again

Step 3: Observe the pattern
After k levels of expansion:

T(n) = 27 (5) +en

T(n)=2 [2r (=) + er +en

T(n) —4T (=) + 2cn

T(n) = 427 (=) + ct] +2cn

T(n) — 87 (5) + 8cn

T(n) = 2*T (sz) + ken
--- page 7 ---
(b) Explain the concept of graph coloring. Identify the minimum number of colors [10
required to color the nodes of the given graph using state space tree.   ]
Solution: concept ( 3 marks), solution ( 7 markS)
Graph coloring is the process of assigning colors to the vertices (or edges) of a graph such
that no two adjacent vertices (or edges) have the same color.
********** 7 **********

[Text in pictures on this page, read by OCR]
At the last level, 3; = 1
=> 2*-nsk=logyn
Substitute this in the above expression:
T(n) = nT(1) + enlogyn
Since T(1) = ¢,

T(n) = en + enlogyn

Step 5: Simplify

T(n) = O(nlogn)
--- page 8 ---
Q.4 (a) Write algorithm for greedy knapsack and obtain the solution to following [10
fractional   greedy knapsack problem where n=5, m=100, (p1, p2....p5) =   ]
(10,20,30,40,50) and (w1,w2,w3,w4,w5) = (20,30,66,40,60)
Solution: Algorithm 5 marks, solution 5 marks
Algorithm: Greedy-Fractional-Knapsack (w[1..n], p[1..n], M)
for i = 1 to n
do x[i] = 0
profit =0
for i = 1 to n
if w[i] ≤ M then
x[i] = 1
weight = M - w[i]
profit = profit+p* x[i]
else
x[i] = (weight- w[i]) / w[i]
profit = profit+p* x[i]
break
return x
return profit
Given:
• Number of items n=7n = 7n=7
• Knapsack capacity M=20M = 20M=20
•   Profits: p=(8,5,6,7,6,12,3)p = (8, 5, 6, 7, 6, 12, 3)p=(8,5,6,7,6,12,3)
• Weights: w=(2,10,8,7,6,4,11)w = (2, 10, 8, 7, 6, 4, 11)w=(2,10,8,7,6,4,11)
Item Profit (p_i) Weight (w_i) Ratio (p_i/w_i)
1   8   2   4.00
2   5   10   0.50
3   6   8   0.75
4   7   7   1.00
5   6   6   1.00
6   12   4   3.00
7   3   11   0.27
********** 8 **********
--- page 9 ---
Step 2: Sort by ratio (descending)
Sorted order (by index): 1, 6, 4, 5, 3, 2, 7
Order   Item   Profit   Weight   Ratio
1   1   8   2   4.00
2   6   12   4   3.00
3   4   7   7   1.00
4   5   6   6   1.00
5   3   6   8   0.75
6   2   5   10   0.50
7   7   3   11   0.27
Step 3: Fill the knapsack greedily
Capacity: 20 units
We now select items in order:
1. Item 1: Weight = 2 → remaining capacity = 18, profit = 8
2. Item 6: Weight = 4 → remaining capacity = 14, profit = 12 → total = 20
3. Item 4: Weight = 7 → remaining capacity = 7, profit = 7 → total = 27
4. Item 5: Weight = 6 → remaining capacity = 1, profit = 6 → total = 33
5. Item 3: Weight = 8 → only 1 unit left, so take fraction
Fraction = 18\frac{1}{8}81, profit = 18×6=0.75\frac{1}{8} \times 6 =
0.7581×6=0.75
Final Result (Fractional Knapsack):
• Items taken: 1, 6, 4, 5, part of 3
• Total weight: 2 + 4 + 7 + 6 + 1 = 20
• Total profit: 8 + 12 + 7 + 6 + 0.75 = 33.75
(b)   [10
Suppose that we have a graph consisting of 5 vertices having edges between them as shown   ]
in the picture below.
(i)   State the name of the method which can be used in this scenario and write
the algorithm.
(ii)   Find the shortest distance to each vertex vi, starting from the vertex 1.
********** 9 **********
--- page 10 ---
Solution: 5 marks each
Bellman ford algorithm
Q.5 (a) Consider the following graph and compute the shortest path   [10
]
********** 10 **********

[Text in pictures on this page, read by OCR]
BELLMAN-FORD(G, w,s)

| INITIALIZE-SINGLE-SOURCE(G,. 5)
2 fori = 1 to|G.V|-—1

3 for each edge (u,v) € G.E
4 RELAX (u,v. Ww)

5 for each edge (u,v) € G.E

6 ifv.d>u.d+w(u,v)

7 return FALSE

8 return TRUE
--- page 11 ---
Solution
Step 1: Cost (K-2, j)
In this step, three nodes (node 4, 5. 6) are selected as j. Hence, we
have three options to choose the minimum cost at this step.
Cost(3, 4) = min {c(4, 7) + Cost(7, 9),c(4, 8) + Cost(8, 9)} = 7
Cost(3, 5) = min {c(5, 7) + Cost(7, 9),c(5, 8) + Cost(8, 9)} = 5
Cost(3, 6) = min {c(6, 7) + Cost(7, 9),c(6, 8) + Cost(8, 9)} = 5
Step 2: Cost (K-3, j)
Two nodes are selected as j because at stage k - 3 = 2 there are
two nodes, 2 and 3. So, the value i = 2 and j = 2 and 3.
Cost(2, 2) = min {c(2, 4) + Cost(4, 8) + Cost(8, 9),c(2, 6) +
Cost(6, 8) + Cost(8, 9)} = 8
Cost(2, 3) = {c(3, 4) + Cost(4, 8) + Cost(8, 9), c(3, 5) + Cost(5,
8)+ Cost(8, 9), c(3, 6) + Cost(6, 8) + Cost(8, 9)} = 10
Step 3: Cost (K-4, j)
Cost (1, 1) = {c(1, 2) + Cost(2, 6) + Cost(6, 8) + Cost(8, 9), c(1,
3) + Cost(3, 5) + Cost(5, 8) + Cost(8, 9))} = 12
c(1, 3) + Cost(3, 6) + Cost(6, 8 + Cost(8, 9))} = 13
Hence, the path having the minimum cost is 1→ 3→ 5→ 8→ 9.
Q. A manufacturing company requires job scheduling with the following constraints:   [10
5   ]
(b)   • Job 1: Profit = 50, Deadline = 2
• Job 2: Profit = 40, Deadline = 1
• Job 3: Profit = 30, Deadline = 2
• Job 4: Profit = 10, Deadline = 1
(i) Write the algorithm for job scheduling with deadline.
(ii) Draw the Gannt chart to identify the optimal slots assigned to each job.
(iii) Calculate the total profit achieved through the scheduling approach.
Solution – algorithm 5 marks solution 5 marks
********** 11 **********
--- page 12 ---
Optimal Job Sequence and Time Slots: (3 marks with proper timeline)
Job 1 (Profit 50): Allocated to Slot 2
Job 2 (Profit 40): Allocated to Slot 1
Job 3 (Profit 30): Not scheduled (time slot conflict)
Job 4 (Profit 10): Not scheduled (time slot conflict)
Total Profit Calculation: ( 2marks )
Job 1: 50 profit
Job 2: 40 profit
Total Profit: 90
Q.6 (a) A thief plans to rob a store and has a knapsack that can carry a maximum weight of W.   [10
There are n available items, where the weight of the i-th item is wᵢ and the profit of   ]
selecting this item is pᵢ. The thief can either take an entire item or leave it (i.e., cannot
take a fraction of any item).
(i) Identify the algorithmic approach used to obtain the most optimal solution for
this problem.
(ii) Write the algorithm that can be applied to find the maximum profit for the
thief.
(iii) Compute the time and space complexity of the algorithm.
Solution:
(i) 0/1 knapsack (1 mark)
(ii)Algorithm: (5 marks)
for i = 1 to n
do c[i, 0] = 0
for w = 1 to W
do
if wi ≤ w then
********** 12 **********

[Text in pictures on this page, read by OCR]
Algorithm

| Algorithm GreedyJob(d, J, n)
2 // J isaset of jobs that can be completed by their deadlines.

4 J = {1};

5 for i := 2 to n do

6

7 if (all jobs in J U {i} can be completed

8 by their deadlines) then J := J U {i};
9
--- page 13 ---
if vi + c[i-1, w-wi]
then c[i, w] = vi + c[i-1, w-wi]
else c[i, w] = c[i-1, w]
else c[i, w] = c[i-1, w]
(iii)Time Complexity (2marks)
This algorithm takes Ɵ(n.w) times as algorithm has (n+1).(w+1) times loops, where
each entry requires Ɵ(1) time to compute.
Space Complexity(2 marks)
We store the results for all subproblems in a (n+1) × (W+1) matrix. Hence space
complexity will be O(nW).
(b) Solve the following recurrence relations using master theorem   [10
]
a)T(n)=2T(n/2)+1
b)T(n)=4T(n/2)+n²
c)T(n)=2T(n/2)+n²logn
d)T(n)=2T(n/2)+n/logn
Q.7 (a) A teacher wants to arrange the marks of her students in ascending order. Instead of   [10
sorting the entire list at once, she first selects one student’s mark as a reference point   ]
(pivot element). She then places all marks lower than the pivot on the left side and
marks higher than the pivot on the right side. After that, she repeats the same process
independently on both the left and right groups until all marks are in order.
(i) Identify the name of the sorting algorithm used in this scenario.
(ii) Write the algorithm for the same.
(iii) Compute the worst-case time complexity of the identified algorithm
(b) Explain P, NP, NP hard and NP complete problem with example.   [5]
********** 13 **********

[Text in pictures on this page, read by OCR]
Class Definition Example

P (Polynomial time) Problems that can be solved in polynomial time by 2 Sorting (Merge Sort, Quick Sort),
deterministic algorithm. Shortest Path (Dijkstra)

NP (Nondeterministic Problems for which a given solution can be verified in Subset Sum, Hamiltonian Path,

Polynomial time) polynomial time. Knapsack (0/1)

NP-hard Problems that are at least as hard as the hardest Halting Problem, General TSP

problems in NP. They may not be in NP (solution may
not be verifiable in polynomial time).

NP-complete Problems that are both in NP and NP-hard. 3-SAT, 0/1 Knapsack, Hamiltonian Cycle
--- page 14 ---
(c)   Give the definition & mathematical representation of Big Oh (O) notation and [5]
test if f(n) = O(g(n)) when f(n) = n+20 and g(n) = n. Compute the Omega (Ω)
notation of f(n) = 7n3 + 5n2 + 2n + 4.
1. Big Oh (O) Notation – Definition & Mathematical Representation
Definition:
Big O notation describes the upper bound of an algorithm's running time. It gives
the worst-case time complexity, indicating how the runtime scales with input size
nnn. It provides an upper limit such that the function doesn't grow faster than a
certain rate.
********** 14 **********

[Text in pictures on this page, read by OCR]
Class Example Problem

P Sorting, Minimum Spanning Tree, Shortest Path (Dijkstra)
NP Subset Sum, Graph Coloring, Hamiltonian Path
NP-hard Traveling Salesman Problem (general), Halting Problem

NP-complete 3-SAT, 0/1 Knapsack, Hamiltonian Cycle, Graph Coloring
--- page 15 ---
Let's try to find constants ¢ and no.

Divide both sides:

20
l+—<e
n

Asm — co, 20 —+ 0. So forn > 20, 20 <1, hence:

20
1+—<14+1=2
n

So, take ¢ = 2, mp = 20. Then:
f(n) =n+20 < 2n=c-g(n)

[) Conclusion: Yes, f(n) = O(g(n))

FRR IC 7 DA HOH
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 81f7394efb04

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_AI_7051/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 72.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSBS)/MBA Tech (AI)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Attempt any 4 questions from the remaining questions.
6. Total 5 questions to be attempted.
Q.1 Attempt all questions   [20
:   ]
(a) Discuss time and space complexity. Compute the time and space complexity of the [5]
code segment given below:
main ( )
{
for(i=1; i<=n; i++)
{
for(j=1; j<=n; j=2*j)
{
x = y+z;
}
}
}
Solution: Time complexity measures the amount of time an
algorithm takes to complete as a function of the input size. It’s a
way to estimate the running time of an algorithm.
Space complexity measures the amount of memory an algorithm
uses as a function of the input size.
Time complexity O(nlogn), space complexity O(1)
********** 1 **********
--- page 2 ---
(b) Build the Huffman tree and generate the codeword for the given characters:   [5]
character : a b c d e   f
Frequency : 5 9 12 13 16 45
Solution: Steps to Build Huffman Tree (Greedy Algorithm)
Step 1: Initialize a Min-Heap with all characters sorted by frequency.
We use a priority queue (or min-heap) to always select the two lowest-frequency
nodes.
Step 2: Combine two lowest-frequency nodes into a new node.
The new node’s frequency is the sum of the two.
This new node becomes a parent, and the two nodes become its left and right children.
Repeat until only one node (root) remains.
[100]
/   \
[45]   [55]
/   \
[25]   [30]
/ \   /   \
[12] [13] [14] [16]
(c) (d) [5] [9] (e)
(a) (b)
Character Frequency Huffman Code
a   5   1100
b   9   1101
c   12   100
d   13   101
e   16   111
f   45   0
(c) Give the difference between dynamic programing and divide & conquer technique.   [5]
Solution:
Basis of Difference Divide and Conquer Dynamic Programming
Divides the problem into
Divides the problem into overlapping
independent subproblems, solves
Approach   subproblems, solves each subproblem
them recursively, and combines
once, and stores the result for reuse.
their results.
Overlapping   Subproblems are independent Subproblems are dependent
Subproblems   (no repetition).   and repeated.
Optimal   May or may not have optimal   Always has optimal
Substructure   substructure.   substructure property.
Uses table (array/matrix) or
Storage /   Does not use storage of
memoization to store intermediate
Memoization   intermediate results.
results.
(d) Generate the solution by drawing state space tree to place the queens on 4x4 [5]
chessboard using backtracking approach.
********** 2 **********
--- page 3 ---
Solution:
Q.2 (a)   i. Define Master’s theorem for computing time complexity.   [10
ii Consider the following recurrence   ]
T(𝑛)= T(n−1)+𝑛, 𝑛>0 ;
1   n=0
Compute the time complexity using substitution method
Solution: 5 marks each
Masters Theorem
Substitution method
********** 3 **********

[Text in pictures on this page, read by OCR]
The Master Method depends on the following Theorem:

Theorem: Let a => 1 and b > 1 be constants, let f(n) be a function, and let T(n) be
defined on the nonnegative integers by the recurrence:

T(n) =aT (7) +f(n)

Then T(n) can be bounded asymptotically as follows.

1. If f(n) = O(n!8 2) for some constant ¢ > 0, then T(n) = O(n!°8 2),
2. If f(n) = O(n!8 4), then T(n) = O(n! * ign).
3. if f(n) = Q(n!& *+) for some constant £ > 0, and if a- f (7) = cf(n) for some constant

¢ < 1 and all sufficiently large n, then T(n) = O(f(n)). F 4
--- page 4 ---
(b) Consider the problem of finding the Longest Common Subsequence (LCS) between   [10
two given strings S1 = TAGTCACG and S2 = AGACTGTC.   ]
(i)   Generate the longest common subsequence of the given strings. Show
each step.
(ii)   Write the algorithm for generating the longest common subsequence and
compute the time complexity.
Solution:
4 marks generation of LCS, 4 marks algorithm, 2 marks time complexity
i.
The LCS for the above example is AGACG of length 5.
ii.   Algorithm
********** 4 **********

[Text in pictures on this page, read by OCR]
T(n) =T(n—1)+n
Substitute for T(n — 1):
T(n) = [T(n— 2) + (n—1)] +n=T(n—2) + (n—1) +n
Substitute again:
T(n) = T(n—3)+(n—2)+(n—-1) +n

Continuing this pattern k times:

k-1

T(n) =T(n—k) + S\(n-i)

i=0
--- page 5 ---
Time Complexity: O(mxn)
Q.3 (a)   (i) Write the algorithm of merging step of merge sort.   [10
]
(ii) Use Merge sort to sort the array of numbers {15, 6, 5, 17, 22, 8, 12, 21}.
(iii)   Write the recurrence equation of Merge sort and find the time complexity of
Merge sort by substitution method.
Solution: Algorithm ( 4 marks), solution (3 marks), time complexity ( 3 marks)
MERGE(A, p, q, r)
1. n1 = q - p + 1
2. n2 = r - q
3. Create arrays L[1..n1+1] and R[1..n2+1]
4. for i = 1 to n1
L[i] = A[p + i - 1]
5. for j = 1 to n2
R[j] = A[q + j]
6. L[n1 + 1] = ∞   // Sentinel value
7. R[n2 + 1] = ∞
8. i = 1, j = 1
9. for k = p to r
if L[i] ≤ R[j]
A[k] = L[i]
i = i + 1
********** 5 **********

[Text in pictures on this page, read by OCR]
LCS-LENGTH(X, Y)

1 m= X.length

2 n=Y.length

3 let b[l..m,1..n] and c[0..m,0..n] be new tables
4 fori = ltom

5 cfi,0] = 0

6 for 7 = Oton

7 co, 7] =0

8 fori = ltom

9 for j = lton

10 ifx; == y;

i cli, j] = ck -—1,7 -1]+1
12 big] ="

13 elseif c[i — 1, j] = cfi,j —1]
14 cli, j] = ci —1.j]

15 bi. jJ="t"

16 else cli, j] = cli. j — 1]

17 bli, j] = “—”

18 return c andb
--- page 6 ---
else
A[k] = R[j]
j = j + 1
Recurse on both halves:
•   Left half: [15, 6, 5, 17] → split into [15, 6] and [5, 17]
o [15, 6] → merge → [6, 15]
o [5, 17] → merge → [5, 17]
o Merge [6, 15] and [5, 17] → [5, 6, 15, 17]
• Right half: [22, 8, 12, 21] → split into [22, 8] and [12, 21]
o [22, 8] → merge → [8, 22]
o [12, 21] → merge → [12, 21]
o Merge [8, 22] and [12, 21] → [8, 12, 21, 22]
Final Merge:
Merge [5, 6, 15, 17] and [8, 12, 21, 22]
********** 6 **********

[Text in pictures on this page, read by OCR]
Step 1: Expand once

Step 2: Expand again

Step 3: Observe the pattern
After k levels of expansion:

T(n) = 27 (5) +en

T(n)=2 [2r (=) + er +en

T(n) —4T (=) + 2cn

T(n) = 427 (=) + ct] +2cn

T(n) — 87 (5) + 8cn

T(n) = 2*T (sz) + ken
--- page 7 ---
(b) Explain the concept of graph coloring. Identify the minimum number of colors [10
required to color the nodes of the given graph using state space tree.   ]
Solution: concept ( 3 marks), solution ( 7 markS)
Graph coloring is the process of assigning colors to the vertices (or edges) of a graph such
that no two adjacent vertices (or edges) have the same color.
********** 7 **********

[Text in pictures on this page, read by OCR]
At the last level, 3; = 1
=> 2*-nsk=logyn
Substitute this in the above expression:
T(n) = nT(1) + enlogyn
Since T(1) = ¢,

T(n) = en + enlogyn

Step 5: Simplify

T(n) = O(nlogn)
--- page 8 ---
Q.4 (a) Write algorithm for greedy knapsack and obtain the solution to following [10
fractional   greedy knapsack problem where n=5, m=100, (p1, p2....p5) =   ]
(10,20,30,40,50) and (w1,w2,w3,w4,w5) = (20,30,66,40,60)
Solution: Algorithm 5 marks, solution 5 marks
Algorithm: Greedy-Fractional-Knapsack (w[1..n], p[1..n], M)
for i = 1 to n
do x[i] = 0
profit =0
for i = 1 to n
if w[i] ≤ M then
x[i] = 1
weight = M - w[i]
profit = profit+p* x[i]
else
x[i] = (weight- w[i]) / w[i]
profit = profit+p* x[i]
break
return x
return profit
Given:
• Number of items n=7n = 7n=7
• Knapsack capacity M=20M = 20M=20
•   Profits: p=(8,5,6,7,6,12,3)p = (8, 5, 6, 7, 6, 12, 3)p=(8,5,6,7,6,12,3)
• Weights: w=(2,10,8,7,6,4,11)w = (2, 10, 8, 7, 6, 4, 11)w=(2,10,8,7,6,4,11)
Item Profit (p_i) Weight (w_i) Ratio (p_i/w_i)
1   8   2   4.00
2   5   10   0.50
3   6   8   0.75
4   7   7   1.00
5   6   6   1.00
6   12   4   3.00
7   3   11   0.27
********** 8 **********
--- page 9 ---
Step 2: Sort by ratio (descending)
Sorted order (by index): 1, 6, 4, 5, 3, 2, 7
Order   Item   Profit   Weight   Ratio
1   1   8   2   4.00
2   6   12   4   3.00
3   4   7   7   1.00
4   5   6   6   1.00
5   3   6   8   0.75
6   2   5   10   0.50
7   7   3   11   0.27
Step 3: Fill the knapsack greedily
Capacity: 20 units
We now select items in order:
1. Item 1: Weight = 2 → remaining capacity = 18, profit = 8
2. Item 6: Weight = 4 → remaining capacity = 14, profit = 12 → total = 20
3. Item 4: Weight = 7 → remaining capacity = 7, profit = 7 → total = 27
4. Item 5: Weight = 6 → remaining capacity = 1, profit = 6 → total = 33
5. Item 3: Weight = 8 → only 1 unit left, so take fraction
Fraction = 18\frac{1}{8}81, profit = 18×6=0.75\frac{1}{8} \times 6 =
0.7581×6=0.75
Final Result (Fractional Knapsack):
• Items taken: 1, 6, 4, 5, part of 3
• Total weight: 2 + 4 + 7 + 6 + 1 = 20
• Total profit: 8 + 12 + 7 + 6 + 0.75 = 33.75
(b)   [10
Suppose that we have a graph consisting of 5 vertices having edges between them as shown   ]
in the picture below.
(i)   State the name of the method which can be used in this scenario and write
the algorithm.
(ii)   Find the shortest distance to each vertex vi, starting from the vertex 1.
********** 9 **********
--- page 10 ---
Solution: 5 marks each
Bellman ford algorithm
Q.5 (a) Consider the following graph and compute the shortest path   [10
]
********** 10 **********

[Text in pictures on this page, read by OCR]
BELLMAN-FORD(G, w,s)

| INITIALIZE-SINGLE-SOURCE(G,. 5)
2 fori = 1 to|G.V|-—1

3 for each edge (u,v) € G.E
4 RELAX (u,v. Ww)

5 for each edge (u,v) € G.E

6 ifv.d>u.d+w(u,v)

7 return FALSE

8 return TRUE
--- page 11 ---
Solution
Step 1: Cost (K-2, j)
In this step, three nodes (node 4, 5. 6) are selected as j. Hence, we
have three options to choose the minimum cost at this step.
Cost(3, 4) = min {c(4, 7) + Cost(7, 9),c(4, 8) + Cost(8, 9)} = 7
Cost(3, 5) = min {c(5, 7) + Cost(7, 9),c(5, 8) + Cost(8, 9)} = 5
Cost(3, 6) = min {c(6, 7) + Cost(7, 9),c(6, 8) + Cost(8, 9)} = 5
Step 2: Cost (K-3, j)
Two nodes are selected as j because at stage k - 3 = 2 there are
two nodes, 2 and 3. So, the value i = 2 and j = 2 and 3.
Cost(2, 2) = min {c(2, 4) + Cost(4, 8) + Cost(8, 9),c(2, 6) +
Cost(6, 8) + Cost(8, 9)} = 8
Cost(2, 3) = {c(3, 4) + Cost(4, 8) + Cost(8, 9), c(3, 5) + Cost(5,
8)+ Cost(8, 9), c(3, 6) + Cost(6, 8) + Cost(8, 9)} = 10
Step 3: Cost (K-4, j)
Cost (1, 1) = {c(1, 2) + Cost(2, 6) + Cost(6, 8) + Cost(8, 9), c(1,
3) + Cost(3, 5) + Cost(5, 8) + Cost(8, 9))} = 12
c(1, 3) + Cost(3, 6) + Cost(6, 8 + Cost(8, 9))} = 13
Hence, the path having the minimum cost is 1→ 3→ 5→ 8→ 9.
Q. A manufacturing company requires job scheduling with the following constraints:   [10
5   ]
(b)   • Job 1: Profit = 50, Deadline = 2
• Job 2: Profit = 40, Deadline = 1
• Job 3: Profit = 30, Deadline = 2
• Job 4: Profit = 10, Deadline = 1
(i) Write the algorithm for job scheduling with deadline.
(ii) Draw the Gannt chart to identify the optimal slots assigned to each job.
(iii) Calculate the total profit achieved through the scheduling approach.
Solution – algorithm 5 marks solution 5 marks
********** 11 **********
--- page 12 ---
Optimal Job Sequence and Time Slots: (3 marks with proper timeline)
Job 1 (Profit 50): Allocated to Slot 2
Job 2 (Profit 40): Allocated to Slot 1
Job 3 (Profit 30): Not scheduled (time slot conflict)
Job 4 (Profit 10): Not scheduled (time slot conflict)
Total Profit Calculation: ( 2marks )
Job 1: 50 profit
Job 2: 40 profit
Total Profit: 90
Q.6 (a) A thief plans to rob a store and has a knapsack that can carry a maximum weight of W.   [10
There are n available items, where the weight of the i-th item is wᵢ and the profit of   ]
selecting this item is pᵢ. The thief can either take an entire item or leave it (i.e., cannot
take a fraction of any item).
(i) Identify the algorithmic approach used to obtain the most optimal solution for
this problem.
(ii) Write the algorithm that can be applied to find the maximum profit for the
thief.
(iii) Compute the time and space complexity of the algorithm.
Solution:
(i) 0/1 knapsack (1 mark)
(ii)Algorithm: (5 marks)
for i = 1 to n
do c[i, 0] = 0
for w = 1 to W
do
if wi ≤ w then
********** 12 **********

[Text in pictures on this page, read by OCR]
Algorithm

| Algorithm GreedyJob(d, J, n)
2 // J isaset of jobs that can be completed by their deadlines.

4 J = {1};

5 for i := 2 to n do

6

7 if (all jobs in J U {i} can be completed

8 by their deadlines) then J := J U {i};
9
--- page 13 ---
if vi + c[i-1, w-wi]
then c[i, w] = vi + c[i-1, w-wi]
else c[i, w] = c[i-1, w]
else c[i, w] = c[i-1, w]
(iii)Time Complexity (2marks)
This algorithm takes Ɵ(n.w) times as algorithm has (n+1).(w+1) times loops, where
each entry requires Ɵ(1) time to compute.
Space Complexity(2 marks)
We store the results for all subproblems in a (n+1) × (W+1) matrix. Hence space
complexity will be O(nW).
(b) Solve the following recurrence relations using master theorem   [10
]
a)T(n)=2T(n/2)+1
b)T(n)=4T(n/2)+n²
c)T(n)=2T(n/2)+n²logn
d)T(n)=2T(n/2)+n/logn
Q.7 (a) A teacher wants to arrange the marks of her students in ascending order. Instead of   [10
sorting the entire list at once, she first selects one student’s mark as a reference point   ]
(pivot element). She then places all marks lower than the pivot on the left side and
marks higher than the pivot on the right side. After that, she repeats the same process
independently on both the left and right groups until all marks are in order.
(i) Identify the name of the sorting algorithm used in this scenario.
(ii) Write the algorithm for the same.
(iii) Compute the worst-case time complexity of the identified algorithm
(b) Explain P, NP, NP hard and NP complete problem with example.   [5]
********** 13 **********

[Text in pictures on this page, read by OCR]
Class Definition Example

P (Polynomial time) Problems that can be solved in polynomial time by 2 Sorting (Merge Sort, Quick Sort),
deterministic algorithm. Shortest Path (Dijkstra)

NP (Nondeterministic Problems for which a given solution can be verified in Subset Sum, Hamiltonian Path,

Polynomial time) polynomial time. Knapsack (0/1)

NP-hard Problems that are at least as hard as the hardest Halting Problem, General TSP

problems in NP. They may not be in NP (solution may
not be verifiable in polynomial time).

NP-complete Problems that are both in NP and NP-hard. 3-SAT, 0/1 Knapsack, Hamiltonian Cycle
--- page 14 ---
(c)   Give the definition & mathematical representation of Big Oh (O) notation and [5]
test if f(n) = O(g(n)) when f(n) = n+20 and g(n) = n. Compute the Omega (Ω)
notation of f(n) = 7n3 + 5n2 + 2n + 4.
1. Big Oh (O) Notation – Definition & Mathematical Representation
Definition:
Big O notation describes the upper bound of an algorithm's running time. It gives
the worst-case time complexity, indicating how the runtime scales with input size
nnn. It provides an upper limit such that the function doesn't grow faster than a
certain rate.
********** 14 **********

[Text in pictures on this page, read by OCR]
Class Example Problem

P Sorting, Minimum Spanning Tree, Shortest Path (Dijkstra)
NP Subset Sum, Graph Coloring, Hamiltonian Path
NP-hard Traveling Salesman Problem (general), Halting Problem

NP-complete 3-SAT, 0/1 Knapsack, Hamiltonian Cycle, Graph Coloring
--- page 15 ---
Let's try to find constants ¢ and no.

Divide both sides:

20
l+—<e
n

Asm — co, 20 —+ 0. So forn > 20, 20 <1, hence:

20
1+—<14+1=2
n

So, take ¢ = 2, mp = 20. Then:
f(n) =n+20 < 2n=c-g(n)

[) Conclusion: Yes, f(n) = O(g(n))

FRR IC 7 DA HOH
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper cbb91ea54aff

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_Computer_7032/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Design and Analysis of Algorithms
Date: 11 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data, if necessary.
Q1   Answer briefly:   Marks
A   State any five differences between a pseudo-code and a source-code.
Sol: Differentiate between source code and pseudo-code based on the following
characteristics:
CO1,
SO1,   •   Syntax rules   [5]
• Language dependency
BL2
•   Readability
•   Execution
•   Purpose
[1 Marks for each difference]
CO2, B   A Divide and Conquer algorithm splits a problem of size n into subproblems of   [5]
SO1,
BL2   sizes n/6 and n/6. The merging step takes linear time.
(i) Write the recurrence relation
(ii) Identify whether the division is balanced or unbalanced
[recurrence relation- 3 marks, balanced or unbalanced explanation-2 marks]
CO4, C   State what is an optimization problem and how can it be solved? Define feasible [5]
SO1,
BL2   and optimal solutions.
[optimization problem definition- 2 marks, feasible and optimal solutions
definitions- 1.5 marks each]
CO4, D   Give the general iterative backtracking pseudo-code?   [5]
SO1,
BL2
Sol: 5 marks for correct pseudo-code
********** 1 **********
--- page 2 ---
A   i.   Can you design a non-deterministic algorithm? Also specify which
particular step/s in this algorithm makes it non-deterministic.
Q2   ii.   Draw a well-labelled diagram that explains the relationship between P, NP,
CO1,   [10]
SO1,   NP-Hard, and NP-Complete Complexity Classes.
BL2
Sol: Designing any non-deterministic algorithm (4 marks), Identifying the non-
deterministic steps (3 marks), Diagram (3 marks)
B   Considering the graph below, calculate the shortest path from vertex A with the
help of Bellman-Ford algorithm:
CO4,
SO1,   [10]
BL3
Explain the concept of a negative weight cycle.
Sol: There are total 6 vertices in graph, so we have to relax 5 times all the edges.
The final shortest path from vertex A is [ 0, 1, 3, 5, 0, 3]
stepwise shortest path identification- 7 marks
Negative weight cycle: A negative weight cycle is a cycle in a graph, whose sum
of edge weights is negative. If you traverse the cycle, the total weight
accumulated would be less than zero.
A
Q3   Consider a source emits symbols with frequencies:
CO3,   (a:10), (b:15), (c:30), (d:16), (e:29)   [10]
SO1,
BL4   i.   Construct Huffman tree
ii.   Construct Huffman codes
********** 2 **********

[Text in pictures on this page, read by OCR]
Algorithm |Backtrack(n)

// This schema describes the backtracking process.
// All solutions are generated in x[{1 : n] and printed
// as soon as they are determined.

k:=1;
while (k 4 0) do

if (there remains an untried z[k] € T(a({1], 2[2],...,
z[k —1]) and B,(z{1],...,2[k]) is true) then

if (x{1],...,2[k] is a path to an answer node)
then write (x[{1 : k]);
k :=k+1; // Consider the next set.

else k := k — 1; // Backtrack to the previous set.
+
}
--- page 3 ---
iii.   Compute total weighted path length
iv.   Explain why most frequent symbol gets shortest code
Sol:
i.   Construct Huffman tree - 3marks
Merging steps:
• 10+15=25
• 16+25=41
• 29+30=59
• 41+59=100
ii.   Codes (one valid set): - 3 marks
•   c → 11
•   e → 10
• d → 011
• b → 0101
•   a → 0100
iii.   Weighted path length: 10×4+15×4+16×3+29×2+30×2=266 – 2 marks
iv.   Most frequent symbol gets shortest code Explanation: - 2 marks
• Huffman minimizes weighted cost
•   High-frequency symbols placed closer to root
→ shorter codes
B   Consider the following recursive algorithm:   [10]
void fun(int n){
if(n <= 1) return;
for(int i = 0; i < n; i++){
for(int j = 0; j < n; j++){
cout << i+j << " ";
}
CO1,
}
SO1,
fun(n/2);
BL4
fun(n/2);
}
i.   Form the recurrence relation equation
ii.   Analyze the algorithm by using applicable method
iii.   Identify and justify the applicable case
Sol:
********** 3 **********
--- page 4 ---
A   Consider the following matrix chain:   [10]
A1 (5 x 4), A2 (4 x 6), A3 (6 x 2), A4 (2 x 7)
i.   Using Dynamic Programming, compute the minimum number of scalar
multiplications needed to multiply
ii.   Determine the optimal parenthesization of the matrix chain.
Sol:
Solution:
Q4
CO4,
SO1,   Split Table
BL4
Start from m[1,5] = 160
Look at s[1,5] = 3, so split as:
(A1A2A3)  and  (A4A5)
********** 4 **********

[Text in pictures on this page, read by OCR]
. Form the recurrence relation equation [4 marks]
Work per call = O(n’) (nested loops) — [2 marks]
T(n)= 2r( ; )+ [2 marks]

. Analyze the algorithm by using applicable method [3

marks]

Apply Master Theorem:

© a=2,b=2, n°*2 =n

e f(n)=n? > n—Case3

. Identify and justify the applicable case [3 Marks]
Final Complexity=O(n" )

Justification: dominant term

Final m-table

i\j 1 2 3 4 5

1 oO 120 88 158 160
2 0 48 104 114
3 0 84 78
4 O 42

This table stores the value of k where optimal split occurs.

i\j 1 2 3
1 - 1 1
2 - 2
3 -
4
--- page 5 ---
Then recursively:
s[1,3]=1⇒(A1)(A2A3)
s[4,5]=4⇒(A4)(A5)
Minimum Cost : 160
Optimal Parenthesization: ((A1(A2A3))(A4A5))
Marking Scheme –
Correct Formula – 1 mark
m table– 6 marks (1 mark for each correct value)
Split table – 2 marks
Correct Parenthesization – 1 mark
B   Discuss the correlation of fractional knapsack problem with the Greedy method. [10]
Solve the following problem using the same approach and find the solution to fill
the knapsack. There are 4 items given in the table below along with its weights and
profits. The maximum size of the knapsack is 40.
Item   Weight   Profit
A   10   75
B   5   25
C   20   50
D   16   100
What will be the time and space complexity of the algorithm?
Sol: Discussion on correlation (3 Marks)
The Greedy Method is an algorithmic approach where:
• At each step, we make the locally optimal choice
CO3,   • With the hope that it leads to a globally optimal solution
SO1,   •   It does not reconsider previous choices
BL3
In the fractional knapsack problem:
• We select items based on maximum value per unit weight (profit/weight
ratio), that is the greedy approach.
• At every step, we pick the best available option
The greedy method works perfectly here because:
•   Items can be broken into fractions
• So we can always take the “best part” of any item
• The optimal solution can be built from optimal choices at each step
Solution- (5 Marks) Student need to write each step
Sort in Descending Order of Profit / Weight ratio
Order of selection:
1. A → 7.5
2. D → 6.25
3. B → 5.0
4. C → 2.5
Total Profit = 75 + 100 + 25 + 22.5 = 222.5
********** 5 **********
--- page 6 ---
Item Selected: Final Answer
• A → Full
• D → Full
• B → Full
• C → 45% (fractional)
Complexity: (2 Marks)
3. Ratio Calculation:
• Time = O(n)
2. Sorting:
• Time = O(n log n)
3. Selection Loop:
• Time = O(n)
Overall Time Complexity: O(n log n )
Space Complexity O(n)
A   Given a set A = {3, 5, 6, 7} and a target sum M=15,   [10]
i.   Find all subsets of A whose sum is equal to M using a backtracking
approach.
ii.   Draw the state space tree to illustrate the solution process.
iii.   Write the pseudo-code for the Sum of Subsets algorithm.
Sol: state-space tree – 4 marks
Q5
CO4,
SO1,
BL3
1 solutions- 2 marks
Pseudo-code – 4 marks
B   [10]
For the sequences:
X="ABCDGH", and Y="AEDFHR"
CO4,   i.   Build the LCS dynamic programming table
SO1,   ii.   Identify the length of LCS and LCS
BL3   iii.   Identify its time complexity
iv.
Sol: LCS Table (DP Matrix)
********** 6 **********
--- page 7 ---
LCS Length: 3
LCS: "ADH"
Time complexity In dynamic programming, only table of size m x n is filled up
using two nested for loops. So running time of the dynamic programming
approach would take O(m x n)
Marks: Table construction-4 marks, length of LCS and the LCS – 2 mark each,
Time complexity-2 marks
A   Analyze the following pseudocode and answer the given questions:   [10]
for i = 0 to n-1:
min = i
for j = i+1 to n-1:
if A[j] < A[min]:
min = j
swap(A[i], A[min])
Q6   i.   Identify algorithm
ii.   Count exact number of comparisons
CO2,
SO1,   iii.   What are the best-case and worst-case time complexities of this
BL4   algorithm? Justify.
Sol:
3. best-case and worst-case time complexities: O(n^2)
CO1, B   [10]
SO1,   Compare the following pairs and determine whether:
BL4
********** 7 **********
--- page 8 ---
Sol:
i.   f(n) =O (g(n))
ii. f(n) =O (g(n))
iii. f(n) = Ω(g(n))
iv. f(n) = Theta(g(n))
v. f(n) = Ω(g(n))
[each part carries 2 marks each, 5 x 2 = 10 marks]
A   Determine the time complexity of the Min–Max algorithm by formulating and
analyzing mathematical equations for both the iterative and recursive methods.
Answer: Description of both methods (2 Marks)
•   Correct identification of:
   Iterative (traditional) method → 1 Mark
 Recursive (divide-and-conquer) method → 1 Mark
Mathematical Formulation (Equations) (3 Marks)
Q7
CO2,   •   Iterative method equation: 𝑇(𝑛)=2(𝑛−1)→ 1.5 Marks   [10]
SO1,   •   Recursive method recurrence: 𝑇(𝑛)=2𝑇(𝑛/2)+2, with base case → 1.5
BL4   Marks
Derivation / Solution of Equations (3 Marks)
•   Iterative method simplification to 𝑂(𝑛) → 1 Mark
•   Solving recurrence using:
Expansion / substitution / Master theorem → 2 Marks
Final result: O(n), ((3𝑛)/2)−2
Comparison & Interpretation (2 Marks)
B   i. How do we compare the growth rate of two functions?
ii. What do you mean by “dominant term” in a function. Explain with an
example.
CO1,   Sol: i. Using asymptotic notations:
SO1,   [5]
BL2   •   If f(n)=O(g(n)) → f grows no faster than g
•   If f(n)=Ω(g(n)) → f grows at least as fast as g
•   If f(n)=Θ(g(n)) → both grow at the same rate
[2 marks]
********** 8 **********
--- page 9 ---
ii. The dominant term is the term that grows the fastest as ￼￼n→∞, and
therefore determines the overall growth rate of the function. [2 marks]
E.g. f(n) = 5n2 + 3n + 7; here dominant term is n2
[1 mark]
C   Define Greedy Algorithm. Explain the difference between local optimal and global
optimal solutions with an example.
Sol: A Greedy Algorithm is an approach that makes the best possible choice at each
step (locally optimal) with the hope that these choices will lead to a globally
optimal solution.
CO3,   Difference between Local Optimal and Global Optimal:
SO1,   [5]
BL2   Term   Meaning   Example
Choosing the largest value item that
Local   The best choice at the current
fits in the knapsack at that moment
Optimal   step or subproblem.
(Fractional Knapsack).
Global   The best solution overall for the Maximum total profit that can be
Optimal   entire problem.   achieved after considering all items.
[greedy definition- 2 marks, differences- 3 marks]
********** 9 **********
````

## 2024-25 · Final-Exam · Sem 4 · Answer key · paper fc13de4bfbe2

- Departments: Data Science
- Programmes: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND ENGINEERING (DATA SCIENCE) - 7011
- Source: `00_Original_Downloads/2024/67804__Semester IV__context_fixed.zip :: Final-Exam/BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND ENGINEERING (DATA SCIENCE) - 7011/Design and Analysis of Algorithms/ANS_Final-Exam_Design and Analysis of Algorithms(702CO0C010)_Semester IV_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2025
- Text: mixed (15 pages), mean OCR confidence 29.9
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester IV(Exam Year: 2024-2025)
Subject: Design and Analysis of Algorithms
Date: 05 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Differentiate between the Greedy and divide-and-conquer algorithmic
approaches.
1. Definition
Appro   Divide-and-Conquer
CO- ;   Greedy Algorithm
ach   Algorithm   [5]
SO- ;
Makes locally optimal   Breaks a problem into smaller
BL-
Conce choices at each step, hoping subproblems, solves them
pt   to reach a globally optimal recursively, and then combines
solution.   the results.
Selects the best choice at
Solves problems by dividing,
Strate the moment without
solving independently, and
gy   considering future
combining the results.
consequences.
b.   Apply the Kruskal algorithm using the greedy approach to calculate the
CO- ;
SO- ;   minimum spanning tree from the graph below. Will the Kruskal work   [5]
BL-   efficiently for a directed Graph? State the reason
********** 1 **********
--- page 2 ---
c.   Determine the time complexity of quicksort in the worst-case scenario
using the Substitution method.
1. Quicksort Recurrence Relation
Quicksort follows the divide-and-conquer approach, where:
• The pivot divides the array into two parts.
• We recursively sort the two subarrays.
• We then combine the sorted parts.
In the worst case, Quicksort selects the smallest or largest element as the
pivot, causing one partition to have n−1n-1n−1 elements and the other to
have 0 elements. This leads to the recurrence relation:
T(n)=T(n−1)+O(n)T(n) = T(n-1) + O(n)T(n)=T(n−1)+O(n)
where:
•   T(n−1)T(n-1)T(n−1) is the time to sort the larger subarray.
CO- ;   •   O(n)O(n)O(n) is the time to partition the array.
SO- ;   [5]
BL-
2. Solving Using the Substitution Method
We expand the recurrence step by step:
T(n)=T(n−1)+cnT(n) = T(n-1) + cnT(n)=T(n−1)+cn
Expanding further,
T(n−1)=T(n−2)+c(n−1)T(n-1) = T(n-2) + c(n-1)T(n−1)=T(n−2)+c(n−1)
T(n−2)=T(n−3)+c(n−2)T(n-2) = T(n-3) + c(n-2)T(n−2)=T(n−3)+c(n−2)
Expanding until we reach the base case T(1)=O(1)T(1) = O(1)T(1)=O(1), we
get:
T(n)=T(n−1)+cnT(n) = T(n-1) + cnT(n)=T(n−1)+cn =(T(n−2)+c(n−1))+cn=
\left( T(n-2) + c(n-1) \right) + cn=(T(n−2)+c(n−1))+cn
=((T(n−3)+c(n−2))+c(n−1))+cn= \left( \left( T(n-3) + c(n-2) \right) + c(n-1)
\right) + cn=((T(n−3)+c(n−2))+c(n−1))+cn =T(1)+c(2+3+⋯+(n−1)+n)= T(1) + c(2
+ 3 + (n-1) + n)=T(1)+c(2+3+⋯+(n−1)+n)
T(n)=O(n2)T(n) = O(n^2)T(n)=O(n2)
********** 2 **********
--- page 3 ---
d.   Write the algorithm for Bellman-Ford's Single Source Shortest Path using
Dynamic Programming. Justify its Time complexity step by step.
CO- ;
SO- ;   [5]
BL-
a.   Consider the set S = {5, 10, 12, 13, 15, 18} and d = 30. Solve it to obtain
the sum of the subset using Backtracking
[10]
Let A1, A2, A3, and A4 be four matrices of dimensions 10 x 5 , 5 x 20,
Q2   b.   20 x 10, and 10 x 5, respectively. Calculate the minimum number of
CO-;   scalar multiplications required to find the product A1 × A2 × A3 × A4   [10]
SO-;
BL-   using matrix chain multiplication with dynamic programming. Show the
parenthesizing of the product to achieve the lowest multiplication.
Verify the answer with basic matrix multiplication. (Show complete
steps)
a.   [3]
Define the properties of the Algorithm. Write an algorithm for searching
an element in a sorted array of size ‘n.’
Properties of an Algorithm
Q3
An algorithm is a finite sequence of well-defined instructions used to solve a
CO-;   problem. A good algorithm should have the following properties:
SO-; BL-
1. Input
• The algorithm must take zero or more inputs.
********** 3 **********

[Text in pictures on this page, read by OCR]
3. Algorithm (Step-by-Step)

Step 1: Initialization
1. Let dist[] be an array of size V,, initialized as:
© dist[s] = @ (distance from source to itself is 0).

© dist[v] = © for all other vertices v.

Step 2: Relaxation of Edges (Repeat for V — 1 times)
2. Repeat for V — 1 times:
* For each edge (u, v, w), update distance if a shorter path is found:
if dist{u| + w < dist{v] then dist|v] = dist{u] + w
Step 3: Negative Cycle Detection
3. Check for Negative Weight Cycles:
* Ifafter V — 1 iterations, an edge (u, v, w) still satisfies:
dist(u] + w < dist{v]

then negative weight cycle exists.
--- page 4 ---
2. Output
• The algorithm must produce at least one output (result).
3. Definiteness
• Each step must be precise and unambiguous.
4. Finiteness
• The algorithm must terminate after a finite number of steps.
5. Effectiveness
• Each step should be simple enough to be executed in a finite time.
6. Correctness
• The algorithm must produce the correct output for all valid inputs.
7. Generality
• The algorithm should be applicable to various inputs, not just a single
case.
Implement quicksort on the following list of numbers, using the first
number as the pivot, and discuss its asymptotic analysis for all cases:
<20, 33, 10, 8, 27, 58, 6, 66, 11, 49>. Show complete data trace path.
[7]
b.
********** 4 **********

[Text in pictures on this page, read by OCR]
Algorithm (Binary Search - Iterative Approach)
1. Initialize low = @ and high =n - 1.

2. Repeat while low <= high:
a. Compute mid = (low + high) / 2.
b. If arr[mid] == key, return mid (element found).
c. If arr[mid] < key, Set low = mid + 1 (search in the right half).
d. Else, set high = mid - 1 (search in the left half).

3. If low > high, return -1 (element not found).
--- page 5 ---
Solve the two strings A = “abcbdab” and B = “bdcaba” for the longest
common subsequence using dynamic programming. Let x be the length
of the longest common subsequence between A and B, and let y be the
number of such subsequences. Then, compute x + 10y. Justify its Time
Complexity.
********** 5 **********

[Text in pictures on this page, read by OCR]
Step-by-Step Execution (Data Trace Path)
Step 1: First Partition (Pivot = 20)
* Pivot: 20
* Partitioning:

e Elements < 20 [10, 8, 6, 11]

e Elements > 20 — [33, 27, 58, 66, 49]
e = Rearranged list:

(10, 8, 6, 11, 20, 33, 27, 58, 66, 49]

Step 2: Recursively Sort Left Subarray [10, 8, 6, 11] (Pivot = 10)
* Pivot: 10
* Partitioning:

« Elements < 10 — [8, 6]

e Elements > 10 — [11]
« Rearranged:

(8,6, 10, 11]

Step 2.1: Recursively Sort [8, 6] (Pivot = 8)

« Partitioning:
e Elements < 10 > [8, 6]
e Elements > 10 > [11]

e Rearranged:

(8,6, 10, 11]
Step 2.1: Recursively Sort [8, 6] (Pivot = 8)

« Pivot: 8
« Partitioning:
« <8- [6]
« >8- []
e Rearranged:

(6,8)

Step 2.2: [11] is already sorted.

Sorted left subarray:

(6, 8, 10, 11]
--- page 6 ---
c.   [10]
a.   [5]
Find the solution to the recurrence T(n) = T(n/2) + T(n/4) + n2 using the
recursion tree method. Show complete steps.
Q4
CO-;
SO-;
BL-
********** 6 **********

[Text in pictures on this page, read by OCR]
Level 0 (Root Level)
* Work done: n?

«Recursive calls: T(n/2) and T(n/4)

Level 1
Expand T(n/2) and T(n/4):
T(n/2) = T(n/4) + T(n/8) + (n/2)?
T(n/4) = T(n/8) + T(n/16) + (n/4)?
Total work at this level:

© (n/2)? + (n/4)? = n?/4+ n?/16

Level 2

Expand each subproblem:
T(n/4) = T(n/8) + T(n/16) + (n/4)?
T(n/8) = T(n/16) + T(n/32) + (n/8)?

Total work:

2 2 2 2
4)? + (n/8)? + (n/8)? + (n/16)? = 4
(n/a)? + (n/8)* + (n/8)? + (n/16)* = + 4 4

Step 2: Pattern Formation

Observing the pattern, at level i:

¢ The subproblem sizes are n/2',n/4', contributing:

(5) +(@).

e The number of terms grows exponentially.

(1 2
"|G Te

The total work done at level i:

Step 3: Summation Over All Levels

The recursion continues until the subproblem size reaches 1, i.e, 2/2’ = 1, so:
--- page 7 ---
Apply the Master Theorem to determine the time complexity and identify
the case number and error.
T (n) = 4T (n/5) + 5n
Write an algorithm for a Multistage Graph (MSG) algorithm using
Dynamic programming with backward reasoning to calculate the
minimum shortest travelling distance from source to destination.
Discuss its time complexity.
def multistage_graph(cost, n, stages):
# Step 1: Initialize Distance and Path Arrays
INF = float('inf')
dist = [INF] * (n + 1)
path = [0] * (stages + 1)
# Step 2: Distance of Destination Node is 0
dist[n] = 0
b.   # Step 3: Compute Shortest Distance for each node (Backward)   [5]
for i in range(n - 1, 0, -1): # Traverse nodes in reverse
for j in range(i + 1, n + 1): # Check all possible outgoing edges
if cost[i][j] != INF: # If edge exists
dist[i] = min(dist[i], cost[i][j] + dist[j])
c.
# Step 4: Find the Shortest Path   [5]
path[1] = 1 # Start from the source
for i in range(2, stages + 1):
for j in range(path[i - 1] + 1, n + 1):
if cost[path[i - 1]][j] != INF and dist[path[i - 1]] == cost[path[i -
1]][j] + dist[j]:
path[i] = j
break # Move to the next stage
# Step 5: Return Result
return dist[1], path
********** 7 **********

[Text in pictures on this page, read by OCR]
Summing the contributions from all levels:

T(n) = =n (5 7 w)

This is a geometric series with a constant ratio less than 1, which converges to a constant.

Thus, the total complexity simplifies to:

T(n) = O(n?)

Final Answer
T(n) = O(n?)

* Conclusion: The dominant term n? dictates the complexity, making the recurrence asymptotically

quadratic O(n”). <
--- page 8 ---
# Example Usage
INF = float('inf')
n = 8 # Number of nodes
stages = 4 # Number of stages
cost = [[INF] * (n + 1) for _ in range(n + 1)] # Initialize cost matrix
# Define the graph with given costs
cost[1][2] = 2; cost[1][3] = 1
cost[2][4] = 3; cost[2][5] = 2
cost[3][5] = 3; cost[3][6] = 6
cost[4][7] = 2; cost[5][7] = 1
cost[6][7] = 4
cost[7][8] = 3
# Find minimum shortest distance and path
min_cost, shortest_path = multistage_graph(cost, n, stages)
print("Minimum Shortest Distance:", min_cost)
print("Shortest Path:", shortest_path)
a.   Discuss the Best, Worst, and Average cases in terms of asymptotic   [10]
notation for computing the time complexity of an algorithm, providing a
suitable example.
Best, Worst, and Average Cases in Asymptotic Notation
In algorithm analysis, we determine the efficiency of an algorithm using
asymptotic notation, which describes the time complexity in different
scenarios: best case, worst case, and average case. These cases help us
understand how an algorithm performs under various input conditions.
1. Best Case (Ω - Omega Notation)
Q5   The best-case scenario represents the situation where the algorithm
performs the minimum number of operations. It provides a lower bound on
CO-;   the time complexity.
SO-;
BL-   Example: Linear Search
Consider a linear search algorithm that searches for an element in an
unsorted array. The best case occurs when the target element is found at the
first position.
2. Worst Case (O - Big-O Notation)
The worst-case scenario represents the situation where the algorithm takes
the maximum number of operations to complete. It provides an upper bound
on the time complexity.
Example: Linear Search
If the target element is not in the array or is at the last position, the
algorithm will iterate through the entire list.
********** 8 **********
--- page 9 ---
• Worst case complexity: O(n)\mathbf{O(n)}O(n), where nnn is the
number of elements in the array.
3. Average Case (Θ - Theta Notation)
The average-case complexity considers all possible inputs and calculates the
expected time complexity.
Example: Linear Search
In an average scenario, the target element may be found anywhere in the
array. If we assume that the element is equally likely to appear at any
position:
• On average, the algorithm searches half of the elements before
finding the target.
• Average case complexity: Θ(n)\mathbf{\Theta(n)}Θ(n).
Write and apply the Dijkstra algorithm to find all-pair shortest paths
from source 1. Interpret its algorithm and complexity.
[10]
b.
a.   [2+5]
List various types of algorithms. Describe the characteristics of those
algorithms. Also, describe their use cases.
1. Brute Force Algorithm
Characteristics
Q6   •   Tries all possible solutions to find the best one.
•   Simple but inefficient for large problems.
CO-;   • Guarantees a correct solution (if an exhaustive search is possible).
SO-;
BL-   Use Cases
• Password Cracking: Trying all possible combinations.
•   Traveling Salesman Problem (TSP): Checking all possible routes.
•   Sorting (Bubble Sort, Selection Sort): Comparing all elements
iteratively.
********** 9 **********
--- page 10 ---
2. Divide and Conquer Algorithm
Characteristics
•   Breaks a problem into smaller subproblems.
•   Solves subproblems recursively and combines solutions.
•   Efficient for large-scale problems.
Use Cases
• Merge Sort & Quick Sort: Sorting algorithms using partitioning.
•   Binary Search: Splitting the search space in half each step.
•   Fast Fourier Transform (FFT): Used in signal processing.
3. Dynamic Programming (DP)
Characteristics
•   Breaks problems into overlapping subproblems.
•   Stores computed results to avoid redundant calculations
(memoization).
•   Efficient for optimization problems.
Use Cases
•   Fibonacci Sequence Calculation: Avoids redundant calculations.
• Knapsack Problem: Maximizing profit with limited weight capacity.
•   Shortest Path (Bellman-Ford Algorithm): Finding the shortest path in
graphs.
4. Greedy Algorithm
Characteristics
• Makes the best local choice at each step.
• Does not always guarantee an optimal solution but is efficient.
• Works well for optimization problems.
Use Cases
• Huffman Coding: Data compression technique.
•   Prim’s & Kruskal’s Algorithm: Minimum spanning tree (MST)
problems.
•   Dijkstra’s Algorithm: Shortest path finding in graphs.
5. Backtracking Algorithm
Characteristics
•   Explores all possible solutions but abandons those that fail
constraints (pruning).
• Uses recursion to explore paths.
•   Efficient for combinatorial problems.
********** 10 **********
--- page 11 ---
Use Cases
• N-Queens Problem: Placing queens on a chessboard without attack.
• Sudoku Solver: Filling in a grid with constraints.
• Graph Coloring Problem: Assigning colors without conflicts.
6. Recursive Algorithm
Characteristics
•   Solves a problem by calling itself with modified parameters.
• Uses a base case to terminate recursion.
•
Write and explain the algorithm for Kruskal using dynamic
programming. Justify its complexity.
class DisjointSet:
def __init__(self, n):
self.parent = [i for i in range(n)]
self.rank = [0] * n # Rank for union optimization
[8]
def find(self, x):
b.   if self.parent[x] != x:
self.parent[x] = self.find(self.parent[x]) # Path Compression
return self.parent[x]
def union(self, x, y):
root_x = self.find(x)
root_y = self.find(y)
if root_x != root_y:
if self.rank[root_x] > self.rank[root_y]:
self.parent[root_y] = root_x
elif self.rank[root_x] < self.rank[root_y]:
self.parent[root_x] = root_y
else:
self.parent[root_y] = root_x
self.rank[root_x] += 1 # Increment rank if ranks are equal
********** 11 **********
--- page 12 ---
def kruskal_mst(graph, V):
# Step 1: Sort edges by weight
Define Exhaustive search. Write control abstraction for the
Backtracking algorithm.
Exhaustive Search
Exhaustive search is a brute force algorithmic technique that systematically
explores all possible solutions to find the best one. It is used when no
efficient algorithm is available for solving a problem optimally.
Characteristics of Exhaustive Search
•   Tries all possible combinations of solutions.
• Guaranteed to find the optimal solution, if one exists.
•   Computationally expensive for large input sizes due to exponential
complexity.
•   Often used in combinatorial optimization problems.
[2+3]
Examples of Exhaustive Search
c.
1. Brute-force password cracking (trying all possible passwords).
2. Traveling Salesman Problem (TSP) (checking all possible paths).
3. Subset Sum Problem (checking all subsets to find a sum).
a.   [5]
Q7
CO-;   Explain with examples all three cases of the Master Theorem.
SO-;
BL-
********** 12 **********

[Text in pictures on this page, read by OCR]
Time Complexity Analysis

1. Sorting Edges: O( E log E)

* Sorting the edge list using a comparison-based sort (like Merge Sort or QuickSort).
2. Find & Union Operations: O( E log V)

e Find operation is nearly O(1) due to path compression.

* Union operation is amortized O(a(V)), where a(V) is the inverse Ackermann function, which
grows very slowly.

3. Overall Complexity:
O(E log E) + O(E log V) = O(E log V)
Since E log E = E log V (in connected graphs, BE ~ V2), we conclude:

O(EBlogV)
--- page 13 ---
b.
Define state space tree. Explain with an example.
State Space Tree
A State Space Tree is a tree representation of all possible states (or
configurations) of a problem as it progresses through different stages of
computation. It is primarily used in backtracking and branch-and-bound   [5]
algorithms to visualize how the solution space is explored.
Characteristics of a State Space Tree
1. Root Node: Represents the initial state of the problem.
c..   2. Internal Nodes: Represent partial solutions.
3. Leaf Nodes: Represent either a complete solution or a failure (dead-
end).
4. Branches: Represent choices made at each step.
Write and explain the algorithm for Merge Sort by providing a suitable
example. Discuss its time complexity for all cases.
[5]
********** 13 **********

[Text in pictures on this page, read by OCR]
Master Theorem Explanation with All Three Cases

The Master Theorem provides an easy way to analyze the time complexity of divide-and-conquer

algorithms of the form:
n
T(n) =aF (*) + F(n)
where:
© a= Number of subproblems

e 6 = Factor by which the problem size is reduced

« f(n) = Work done outside recursive calls (merging, partitioning, etc.)

Three Cases of Master Theorem

The complexity of T’(n) is determined by comparing f (n) with O(n!%*):

Case Condition Complexity
Case1 f(n) = O(n"),c < log,a O(n'°#2)
Case 2 f(n) = O(n*),c = log, a O(n° log n)

case3.——f (n) = (n°), ¢ > log, a and regularity condition holds O(F(n))
--- page 14 ---
d.
[5]
Explain the Graph coloring problem using the backtracking method.
Discuss its time complexity,
Graph Coloring Using Backtracking
Backtracking Approach
•   Start from the first vertex and try assigning a color.
• Move to the next vertex and assign a valid color (not used by its
adjacent vertices).
•   If all vertices are colored successfully, print the solution.
•   If no valid color is found, backtrack and change the previous vertex's
color.
********** 14 **********

[Text in pictures on this page, read by OCR]
Algorithm for Merge Sort
MergeSort(A, left, right)
1. Ifleft < right:
« Find the middle index: mid = (left + right) /2
e Recursively sort the left half: MergeSort(A, left, mid)
e Recursively sort the right half: MergeSort(A, mid+1, right)

© Merge both sorted halves using Merge(A, left, mid, right)

Merge(A, left, mid, right)
1. Create two temporary arrays:
© Left[] = A[left ... mid]
© =Right[] = A[mid+1 ... right]
2. Compare elements from both arrays and place them in the correct order in A.

3. Copy any remaining elements from Left[] and Right[] into a.

Time Complexity Analysis

The worst-case time complexity of the backtracking approach is:
O(m")

where:

« V is the number of vertices.

* mis the number of colors.

Breakdown of Complexity
1. Each vertex has m choices - O(m) per vertex.
2. There are V vertices — Recursive depth is O(V).

3. Total combinations - O(m" ).

Best, Average, and Worst Cases

Case Complexity Explanation
Best Case O(V) If an early valid coloring is found.
Average Case O(m") Recursion explores valid paths.

Worst Case O(m") Tries all color combinations before backtracking.
--- page 15 ---
FRR IC 7 DA HOH
````

## 2024-25 · Re-Exam · Sem 4 · Answer key · paper 50beb19a8501

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_04/Re-Exam/BTech_CSE_DS_7011/Design and Analysis of Algorithms/ANS_Design and Analysis of Algorithms(702CO0C010)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Jul 2025
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Sem 4 Re-exam(Exam Year: 2024-2025)
Subject: Design and Analysis of Algorithms
Date: 07 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   “The analysis of an algorithm is very important in any problem-solving
approach.” Justify the statement with its benefits.
Algorithm analysis is a crucial aspect of problem-solving in computer
science and engineering. It helps evaluate the efficiency, correctness,
and feasibility of an algorithm before implementation. Here’s why
analyzing an algorithm is essential:
1. Performance Optimization
Algorithm analysis helps determine the time and space complexity of an
algorithm, allowing developers to choose the most efficient approach.
CO-
An optimized algorithm improves execution speed and reduces memory   [5]
1;SO-
usage.
1;BL-5
2. Comparison of Algorithms
By analyzing different algorithms for the same problem, one can
compare their performance and select the best one based on constraints
like execution time, resource availability, and scalability.
3. Scalability and Feasibility
Algorithms should perform efficiently for large inputs. Analyzing an
algorithm helps assess its scalability, ensuring that it works well as the
input size increases.
********** 1 **********
--- page 2 ---
4. Cost and Resource Management
Efficient algorithms minimize hardware and computational resource
costs. A well-analyzed algorithm can reduce power consumption and
execution time in large-scale applications.
5. Avoiding Redundant Computations
Algorithm analysis helps in detecting inefficiencies like redundant
calculations or unnecessary loops, leading to better optimization.
6. Predicting Worst-Case Scenarios
Big-O notation and other analytical techniques help in determining the
worst-case complexity, aiding in designing robust systems that can
handle peak loads effectively.
7. Enhancing Software Reliability
A well-analyzed algorithm ensures correctness, reducing the likelihood
of errors, crashes, or unexpected behavior in software applications.
b.   Discuss the control abstraction of Dynamic Programming.
CO-
4;SO-   [5]
1;BL-2
c.   Write the recursive MAXMIN procedure. Also, state the time and space
complexity of the recursive MAXMIN procedure.
def MAXMIN(arr, low, high):
# If only one element, return it as both max and min
CO-   if low == high:
2;SO-   [5]
return arr[low], arr[low]
1;BL-2
# If two elements, return min and max directly
if high == low + 1:
if arr[low] < arr[high]:
********** 2 **********

[Text in pictures on this page, read by OCR]
Algorithm DYNAMIC PROGRAMMING (P)

if solved(P) then
return lookup (P)
else
Ans + SOLVE (P)
store (P, Ans)
end

Function SOLVE (P)
if sufficiently small(P) then

solution(P) // Find solution for sufficiently small problem
else

Divide P into smaller sub problems Pi, Pz, .., Py

Ans; «+ DYNAMIC PROGRAMMIN (P;)

Ans; « DYNAMIC _PROGRAMMIN (P2)

Ans, «+ DYNAMIC _PROGRAMMIN (P,)

return ( combine (Ans:, Ansz2, .. , ANS,))
end
--- page 3 ---
return arr[low], arr[high]
else:
return arr[high], arr[low]
# Find the middle index
mid = (low + high) // 2
# Recursively find max and min in left half
min1, max1 = MAXMIN(arr, low, mid)
# Recursively find max and min in right half
min2, max2 = MAXMIN(arr, mid + 1, high)
# Combine results
return min(min1, min2), max(max1, max2)
# Example usage
arr = [3, 5, 1, 9, 7, 2, 6]
minimum, maximum = MAXMIN(arr, 0, len(arr) - 1)
print("Minimum:", minimum, "Maximum:", maximum)
d.   What is a greedy algorithm? Explain its two characteristics.
Greedy Algorithm: Definition
A greedy algorithm is an approach for solving optimization problems
by making a sequence of choices, each of which locally appears to be
the best at that moment. The algorithm does not reconsider previous
decisions and aims to reach a global optimum by following a series of
locally optimal steps.
CO-
3;SO-   Greedy algorithms are commonly used in problems where a globally   [5]
1;BL-2   optimal solution can be found by choosing locally optimal solutions at
each step, such as Dijkstra’s algorithm, Kruskal’s algorithm, and
Huffman coding.
Characteristics of a Greedy Algorithm
1. Greedy Choice Property
********** 3 **********
--- page 4 ---
• A greedy algorithm makes the best possible choice at each step
without considering future consequences.
• Once a choice is made, it cannot be changed later.
• This property ensures that selecting a local optimum at each step
leads to a globally optimal solution.
Example:
•   Activity Selection Problem:
o The problem is to select the maximum number of non-
overlapping activities.
o The greedy approach picks the activity that finishes the
earliest, ensuring more activities can be accommodated
later.
2. Optimal Substructure
• A problem exhibits optimal substructure if an optimal solution
to the overall problem can be constructed from optimal solutions
to its subproblems.
• This means that if a solution to a subproblem is optimal,
combining it with other optimal subproblem solutions will yield
the best global solution.
Example:
• Kruskal’s Algorithm (Minimum Spanning Tree):
o The algorithm selects the smallest available edge that
doesn’t form a cycle.
o The local optimal decisions (choosing the smallest edge
at each step) lead to a globally optimal MST.
a.   Discuss the Best, Worst, and Average cases in terms of asymptotic   [10]
notation for computing the time complexity of an algorithm, providing a
suitable example.
Q2
CO-   Best, Worst, and Average Cases in Asymptotic Notation
1;SO-
2;BL-2   The time complexity of an algorithm is analyzed using asymptotic
notation to describe how its runtime grows with input size nnn. The
three main cases analyzed are:
1. Best Case (Ω\OmegaΩ - Omega Notation)
CO-   o The minimum time an algorithm takes for a given input
3;SO-   size.
1;BL-3   o Represents the most favorable scenario (e.g., sorted input
in some algorithms).
2. Worst Case (OOO - Big-O Notation)
o The maximum time an algorithm takes for a given input
size.
********** 4 **********
--- page 5 ---
o Represents the least favorable scenario (e.g., unsorted or
reverse-sorted input).
3. Average Case (Θ\ThetaΘ - Theta Notation)
o The expected time an algorithm takes for a randomly
distributed set of inputs.
o Represents the typical runtime behavior.
Example: Linear Search Algorithm
Algorithm (Linear Search)
python
CopyEdit
def linear_search(arr, key):
for i in range(len(arr)):
if arr[i] == key:
return i # Element found
return -1 # Element not found
1. Best Case (Ω(1)\Omega(1)Ω(1))
• The element is found in the first position.
• Only one comparison is needed.
• Time Complexity: Ω(1)\Omega(1)Ω(1) (constant time).
2. Worst Case (O(n)O(n)O(n))
• The element is found at the last position or not found at all.
• The algorithm performs nnn comparisons.
• Time Complexity: O(n)O(n)O(n) (linear time).
3. Average Case (Θ(n)\Theta(n)Θ(n))
• The element is equally likely to be in any position.
• On average, n/2n/2n/2 comparisons are needed.
• Time Complexity: Θ(n)\Theta(n)Θ(n) (linear time).
Comparison Table
Time Complexity (Linear Search
Case   Definition
Example)
Minimum time
Best Case   Ω(1)\Omega(1)Ω(1)
required
Worst   Maximum time
O(n)O(n)O(n)
Case   required
Average   Expected time
Θ(n)\Theta(n)Θ(n)
Case   required
********** 5 **********
--- page 6 ---
Write the Huffman code algorithm. Solve the sending of the message to
the destination.
“YOUR CLASS IS SPECIAL”
b.   With a smaller number of bits used by constructing the Huffman Tree [2+6+
(include Space) and Calculate
1+1]
1. Average bit length used
2. Percentage of reduction bits; instead, ASCII would have used 7 bits.
Huffman Coding Algorithm
Huffman coding is a greedy algorithm used for lossless data
compression. It assigns variable-length binary codes to characters
based on their frequencies, ensuring the most frequent characters get
shorter codes.
Huffman Coding Algorithm Steps
1. Calculate Frequency: Count the frequency of each character in
the message.
2. Build Min-Heap: Create a priority queue (min-heap) with nodes
representing characters and their frequencies.
3. Construct Huffman Tree:
o Remove the two lowest-frequency nodes.
o Merge them into a new node (sum of their frequencies).
o Repeat until a single root node remains.
4. Generate Huffman Codes:
o Assign 0 to the left child and 1 to the right child.
o Recursively traverse the tree to assign codes to each
character.
5. Encode the Message:
o Replace each character with its corresponding Huffman
code.
Step 1: Frequency Count for "YOUR CLASS IS SPECIAL"
(Space is included as a character.)
Characte Frequenc
r   y
Y   1
O   1
U   1
R   1
(space)   3
C   2
L   3
A   2
********** 6 **********
--- page 7 ---
S   4
I   2
P   1
E   1
Step 2-4: Constructing the Huffman Tree and Assigning
Codes
After building the Huffman tree, let’s assume the following Huffman
codes are generated:
Characte   Huffman
r   Code
S   00
(space)   01
L   100
C   1010
A   1011
I   1100
U   11010
R   11011
Y   11100
O   11101
P   11110
E   11111
Step 5: Encoding the Message
Using the generated Huffman codes, the message "YOUR CLASS IS
SPECIAL" is encoded as follows:
yaml
CopyEdit
11100 11101 11010 11011 01 1010 100 1011 00 00 01 1100 00
01 11110 00 1011 11111 1010 100 01
(Total bits used: 50)
Calculations
1. Average Bit Length Used
Average Bit Length=Total Huffman Bits UsedTotal Characters\text{Av
erage Bit Length} = \frac{\text{Total Huffman Bits Used}}{\text{Total
Characters}}Average Bit Length=Total CharactersTotal Huffman Bits
********** 7 **********
--- page 8 ---
Used =5021≈2.38 bits per character= \frac{50}{21} \approx 2.38 \text{
bits per character}=2150≈2.38 bits per character
2. Percentage of Bit Reduction
• ASCII Encoding: Each character takes 7 bits → Total bits used
= 21×7=14721 \times 7 = 14721×7=147.
• Huffman Encoding: Total bits used = 50.
Reduction=(147−50147)×100\text{Reduction} =   \left( \frac{147   -
50}{147}   \right)   \times   100Reduction=(147147−50)×100
=(97147)×100= \left( \frac{97}{147} \right) \times 100=(14797)×100
≈65.99% reduction in bits\approx   65.99\%   \text{   reduction   in
bits}≈65.99% reduction in bits
a.   List various types of algorithms. Describe the characteristics of those
[10]
algorithms. Also, describe their use cases.
Algorithms are step-by-step procedures for solving computational
problems. Different types of algorithms exist, each with unique
characteristics and applications. Below is a list of various types of
algorithms along with their characteristics and use cases.
1. Brute Force Algorithm
Characteristics:
Q3
CO-   •   Tries all possible solutions to find the best one.
1;SO-   • Simple but inefficient for large inputs.
1;BL-2   • Often used as a baseline for comparison.
Use Cases:
CO-   • Password Cracking: Tries all possible passwords.
4;SO-   • String Matching: Naïve pattern searching in text processing.
2;BL-3   • Traveling Salesman Problem (TSP): Tries all possible routes.
2. Divide and Conquer Algorithm
Characteristics:
• Breaks a problem into smaller subproblems.
• Solves subproblems recursively.
• Combines the solutions to get the final result.
•   Efficient for large datasets.
Use Cases:
********** 8 **********
--- page 9 ---
• Merge Sort & Quick Sort: Sorting large datasets.
• Binary Search: Searching in a sorted array.
• Fast Matrix Multiplication: Strassen’s algorithm.
3. Greedy Algorithm
Characteristics:
• Makes the best local choice at each step.
• Does not reconsider previous decisions.
• Works well for problems with greedy choice property and
optimal substructure.
Use Cases:
•   Dijkstra’s Algorithm: Shortest path in graphs.
• Kruskal’s Algorithm: Minimum Spanning Tree (MST).
• Huffman Coding: Data compression.
4. Dynamic Programming (DP) Algorithm
Characteristics:
• Solves problems by breaking them into overlapping
subproblems.
•   Stores results of subproblems to avoid redundant calculations.
• Uses memoization (top-down) or tabulation (bottom-up).
Use Cases:
• Fibonacci Sequence: Efficient computation using memoization.
•   0/1 Knapsack Problem: Optimizing selection of items in
limited space.
• Longest Common Subsequence (LCS): DNA sequence
alignment.
5. Backtracking Algorithm
Characteristics:
•   Tries different possibilities and undoes a choice if it leads to
failure.
• Uses recursion to explore potential solutions.
•   Efficient for constraint-satisfaction problems.
Use Cases:
********** 9 **********
--- page 10 ---
• N-Queens Problem: Placing queens on a chessboard without
attacks.
• Sudoku Solver: Filling a Sudoku grid.
• Subset Sum Problem: Finding subsets with a given sum.
6. Graph Algorithm
Characteristics:
• Operates on graphs (nodes and edges).
• Finds paths, connectivity, cycles, etc.
• Uses techniques like BFS, DFS, and shortest path calculations.
Use Cases:
•   Dijkstra’s Algorithm: Shortest path in road networks.
• Bellman-Ford Algorithm: Detecting negative-weight cycles.
•
Write and explain the algorithm for finding the Longest Common
Subsequences from two given substrings using the Dynamic
Programming method. Justify its time complexity.
b.   Algorithm for Longest Common Subsequence (LCS) using Dynamic   [10]
Programming
The Longest Common Subsequence (LCS) problem is a classic Dynamic
Programming (DP) problem. It finds the length of the longest sequence that
appears in the same relative order in both strings but may not be contiguous.
Algorithm Explanation
1. Define the Problem
o Given two strings XXX and YYY of lengths mmm and nnn, find
the longest sequence that appears in both strings in the same
order.
2. Define the DP Table
o Create a 2D table dp[m+1][n+1], where dp[i][j]
represents the LCS length of the substrings X[0:i] and
Y[0:j].
3.   Fill the DP Table
o   If characters match:
dp[i][j]=1+dp[i−1][j−1]dp[i][j] = 1 + dp[i-1][j-
1]dp[i][j]=1+dp[i−1][j−1]
o   If characters do not match:
********** 10 **********
--- page 11 ---
dp[i][j]=max⁡(dp[i−1][j],dp[i][j−1])dp[i][j] = \max(dp[i-1][j],
dp[i][j-1])dp[i][j]=max(dp[i−1][j],dp[i][j−1])
o Base Case: If either string is empty, dp[i][0] = dp[0][j]
= 0.
4. Trace Back to Get LCS
o   Start from dp[m][n] and trace back using the table to
reconstruct the LCS.
Algorithm: Longest Common Subsequence (LCS)
python
CopyEdit
def lcs(X, Y):
m, n = len(X), len(Y)
# Step 1: Create a DP table initialized to zero
dp = [[0] * (n + 1) for _ in range(m + 1)]
# Step 2: Fill the DP table
for i in range(1, m + 1):
for j in range(1, n + 1):
if X[i - 1] == Y[j - 1]: # Characters match
dp[i][j] = 1 + dp[i - 1][j - 1]
else: # Characters do not match
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# Step 3: Reconstruct the LCS string
lcs_str = []
i, j = m, n
while i > 0 and j > 0:
if X[i - 1] == Y[j - 1]: # Character part of LCS
lcs_str.append(X[i - 1])
i -= 1
j -= 1
elif dp[i - 1][j] > dp[i][j - 1]: # Move upwards
i -= 1
else: # Move left
j -= 1
return "".join(reversed(lcs_str)) # Reverse to get
correct order
# Example usage
X = "ACDBE"
Y = "ABCDE"
print("Longest Common Subsequence:", lcs(X, Y))
Q4   a.   Solve for the time complexity of the recurrence relation below using the
CO-   a) Substitution method.
3;SO-
T(n) = 2 T(n/2) + nlogn   for n>1 { T(n) = 1; if n==1 }   [5]
1;BL-4
b) Master Theorem {Also tell the CASE number it belongs}   [5]
T(n) = 49 T(n/25) + n3/2 log n
********** 11 **********
--- page 12 ---
CO-
2;SO-
b.   Illustrate the operation of merge sort on the array <5, 2, 4, 7, 1, 3, 2, 6>.   [10]
2;BL-4
Show the complete data flow path. Analyse the time complexity for the
entire operation. Is merge sort a stable sorting method? Explain.
Step 1: Understanding Merge Sort
Merge Sort follows the Divide and Conquer approach:
1. Divide the array into two halves recursively until each sub-array
contains a single element.
2. Conquer by merging the sorted sub-arrays to get the final sorted
array.
Step 2: Breaking Down Merge Sort on <5, 2, 4, 7, 1, 3, 2,
6>
1. Splitting the Array
We continuously split the array into halves:
less
CopyEdit
Original Array: [5, 2, 4, 7, 1, 3, 2, 6]
Split into:   [5, 2, 4, 7]   |   [1, 3, 2, 6]
Further Split:   [5, 2] [4, 7]   |   [1, 3] [2, 6]
Further Split:   [5] [2] [4] [7] |   [1] [3] [2] [6]
Now, all sub-arrays are of size 1, so we start merging.
2. Merging the Subarrays
Now, we merge the subarrays in sorted order.
First Level Merge
css
CopyEdit
[5] [2] → [2, 5]
[4] [7] → [4, 7]
[1] [3] → [1, 3]
[2] [6] → [2, 6]
Second Level Merge
css
CopyEdit
[2, 5] [4, 7] → [2, 4, 5, 7]
[1, 3] [2, 6] → [1, 2, 3, 6]
Final Merge
css
CopyEdit
[2, 4, 5, 7] [1, 2, 3, 6] → [1, 2, 2, 3, 4, 5, 6, 7]
********** 12 **********
--- page 13 ---
Step 3: Visualization of Merge Sort Flow
yaml
CopyEdit
Original:   [5, 2, 4, 7, 1, 3, 2, 6]
Split:   [5, 2, 4, 7]   [1, 3, 2, 6]
Split:   [5, 2]   [4, 7]   [1, 3]   [2, 6]
Split:   [5] [2] [4] [7] [1] [3] [2] [6]
Merge:   [2, 5] [4, 7] [1, 3] [2, 6]
Merge:   [2, 4, 5, 7]   [1, 2, 3, 6]
Final Merge:   [1, 2, 2, 3, 4, 5, 6, 7]
Step 4: Time Complexity Analysis
Merge Sort has a time complexity of O(n log n) in all cases.
Breakdown
•   Dividing the array: Each split operation divides the array into halves,
leading to a height of log₂(n) for the recursion tree.
• Merging the subarrays: At each level, merging takes O(n) operations.
•   Total time complexity:
O(nlog⁡n)O(n \log n)O(nlogn)
Case-wise Complexity
Case   Time Complexity
Best Case   O(nlog⁡n)O(n \log n)O(nlogn)
Average Case O(nlog⁡n)O(n \log n)O(nlogn)
Worst Case   O(nlog⁡n)O(n \log n)O(nlogn)
a.   Write an algorithm for solving the N-Queen problem using backtracking [10]
and explain it with an example using a state space tree.
Q5
CO-   b.   Apply the dynamic strategy to find the shortest path from A to L for the
following multistage graph (Use the forward method). Analyse its time
4;SO-   complexity. Find the total cost.
2;BL-4
[10]
CO-
4;SO-
2;BL-3
a.   Determine the Time and space complexities of the following code   [5]
Q6   snippet.
int i, j, k = 0;
for (i = n / 2; i <= n; i++) {
********** 13 **********
--- page 14 ---
CO-   for (j = 2; j <= n; j = j * 2) {
k = k + n / 2;
1;SO-
}
1;BL-3   }   [5]
b.
Write the asymptotic growth among all functions.
2n ; n1/3 ; en ; n7/4 ; 1.0000001n ; nlogn
[10]
CO-   c.   Write and explain the algorithm for Matrix chain Multiplication using
1;SO-   Dynamic Programming. Write the recursive function for minimum cost
1;BL-3   for parenthesizing the product Ai * Ai+1 * Ai+2 * .....Aj in Matrix
Chain Multiplication using Dynamic Programming. Discuss its Time
CO-   Complexity.
4;SO-   3. Algorithm for Matrix Chain Multiplication (Dynamic
Programming)
1;BL5
Iterative DP Approach (Bottom-Up)
python
CopyEdit
def matrix_chain_order(p):
n = len(p) - 1
dp = [[0] * n for _ in range(n)]
# l is the chain length
for l in range(2, n + 1):
for i in range(n - l + 1):
j = i + l - 1
dp[i][j] = float('inf')
for k in range(i, j):
cost = dp[i][k] + dp[k + 1][j] + p[i] *
p[k + 1] * p[j + 1]
if cost < dp[i][j]:
dp[i][j] = cost
return dp[0][n - 1] # Minimum cost for multiplying A1
to An
# Example Usage
p = [10, 20, 30, 40, 30] # Matrix dimensions
print("Minimum cost of multiplication:",
matrix_chain_order(p))
a.   State the condition which makes a decision problem belong to   [5]
Q7
a. Class P
CO-
1;SO-   b. Class NP
1;BL-2   c. Class NP Hard
d. Class NP Complete
b.   What is the difference between Backtracking and Recursion?
********** 14 **********
--- page 15 ---
CO-
4;SO-   Recursion
1;BL-1
Recursion is a general programming technique where a function calls
CO-   itself directly or indirectly to solve smaller subproblems of the original
2;SO-   problem.
1;BL-2
Key Characteristics of Recursion:
CO-
3;SO-   • Breaks a problem into smaller subproblems of the same type.
2; BL-3   • Has a base case to terminate recursion.
• May involve overlapping subproblems, but recursion alone
does not necessarily avoid redundant calculations.
• Examples: Factorial calculation, Fibonacci sequence, and Tree
Traversal.
Example: Recursion (Factorial Calculation)
python
CopyEdit
def factorial(n):
if n == 0 or n == 1: # Base case
return 1
return n * factorial(n - 1) # Recursive call
print(factorial(5)) # Output: 120
2. Backtracking
Backtracking is a special type of recursion where we systematically
explore all possible choices and undo (backtrack) when a choice
leads to an invalid solution.
Key Characteristics of Backtracking:
• Used for decision-making problems where we explore all
possible solutions.   [5]
• Uses recursion to explore solutions but "backs up" when a
dead end is reached.
•   Efficient pruning: If a partial solution is invalid, we stop
exploring further.
• Examples: N-Queens problem, Sudoku Solver, Maze solving,
Graph coloring.
Demonstrate the effect of various methods of Pivot selection with
c.   [5]
respect to the ordering of elements.
Write and explain Prim’s algorithm using the Greedy approach to find
d.
the Minimum shortest spanning tree. Will Prim’s algorithm fail for a
Directed Graph? State the reason.
********** 15 **********
--- page 16 ---
2. Algorithm (Step-by-Step)
Input:
• A weighted, connected, and undirected graph represented as an   [5]
adjacency matrix or adjacency list.
Steps:
1. Initialize:
o   Select any arbitrary vertex as the starting point.
o Create a visited array to keep track of vertices included in
MST.
o Create a key array to store the minimum edge weight to
connect each vertex.
o Create a parent array to store MST edges.
2. Iterate until all vertices are included in the MST:
o   Select the vertex with the minimum key value (not yet in
MST).
o Mark the vertex as included in MST.
o Update the key values of its adjacent vertices if they can be
connected with a lower weight edge.
3. Repeat until all vertices are included in the MST.
4. Return the MST (edges stored in the parent array).
********** 16 **********
````
