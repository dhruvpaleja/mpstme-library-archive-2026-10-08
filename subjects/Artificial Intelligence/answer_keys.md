# Artificial Intelligence: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper f1333bf38937

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Artificial Intelligence/ANS_Artificial Intelligence(703CO0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
a.   Explain any two suitable applications of artificial intelligence.
Ans
[05]
Any to applications: specifying all the components
2.5 marks each
b.   Discuss the uniform cost search algorithm with a suitable example.
Ans: (2 Marks)
step-by-step process of how UCS works:
1. Initialization: UCS starts with the root node. It is added to the priority queue with
a cumulative cost of zero since no steps have been taken yet.
2. Node Expansion: The node with the lowest path cost is removed from the priority
queue. This node is then expanded, and its neighbors are explored.
3. Exploring Neighbors: For each neighbor of the expanded node, the algorithm
calculates the total cost from the start node to the neighbor through the current [05]
node. If a neighbor node is not in the priority queue, it is added to the queue with
the calculated cost. If the neighbor is already in the queue but a lower cost path to
this neighbor is found, the cost is updated in the queue.
4. Goal Check: After expanding a node, the algorithm checks if it has reached the
goal node. If the goal is reached, the algorithm returns the total cost to reach this
node and the path taken.
5. Repetition: This process repeats until the priority queue is empty or the goal is
reached.
********** 1 **********
--- page 2 ---
Example: (3 Marks)
c.   Convert the following FOPL statement into Conjunctive Normal Form (CNF). Give all
the necessary steps.
“There is a barber who shaves all men in town who do not shave themselves.”
∃x [Barber(x) ∧ ∀y ((Man(y) ∧ ¬Shaves(y, y))→Shaves(x, y))]
Ans:
CNF: (1 mark for each step)
Step 1: Remove implication
(Man(y)∧¬Shaves(y, y))→Shaves(x, y) becomes
¬ Man(y) ∨ Shaves(y, y) ∨ Shaves(x, y)
Step 2: ∃x(Barber(x)∧∀y(¬Man(y)∨Shaves(y,y)∨Shaves(x,y)))   [05]
Step 3: Take out the quantifier outside
∃x ∀y (Barber(x) ∧ (¬Man(y) ∨ Shaves(y, y) ∨ Shaves(x, y)))
Step 4: Skolemization – remove existential by skolemization, x to b.
∀y (Barber(b) ∧ (¬Man(y) ∨ Shaves(y, y) ∨ Shaves(b, y)))
Step 5: remove universal quantifier
Final CNF
1. Barber(b)
2. ¬Man(y)∨Shaves(y,y)∨Shaves(b,y)
d.   Explain the important characteristics of an expert system.
Ans:
1. Operates as an interactive system
2. Tools can store and select (filter) knowledge
[05]
3. The capability to make logical inferences based on the knowledge stored
4. Ability to explain reasoning
5. Systems are very domain-specific
6. Capability to assign of confidence values
a.   Discuss different types of task environments applicable to AI agents with suitable
Q2
examples.   [10]
Ans: Discussion on each task environment with example (2 Marks)
********** 2 **********
--- page 3 ---
1. Fully observable
2. Deterministic
3. Episodic
4. Static
5. Discrete
6. Single agent
b.   Apply and explain the greedy best-first search algorithm on the following map to reach
the goal node from start node A. Consider the heuristic given at each node.
Ans: Explanation on algorithm (4 Marks)
•   Evaluation function f(n) = h(n) (heuristic)
[10]
= estimate of cost from n to goal
e.g., hSLD(n) = straight-line distance from n to Bucharest
•   Greedy best-first search expands the node that appears to be closest to the goal
Solving example: (6 Marks)
A – D (35), C(25), B(32)
C – F(17), E(19)
F – G(0), H(10)
G – Goal
Path = A – C- F - G
a.   Assume the following fact:
1. Steve likes all the easy courses.
2. Science courses are hard.
3. All basket-weaving courses are easy.
4. BK301 is a basket-weaving course.
Q3   Prove using Resolution, Steve likes BK301.
[10]
Ans:
Step 1: Convert to FOPL (3 Marks)
1. ∀y (Easy(y) → Likes(Steve, y))
2. ∀y (Science(y) → Hard(y))
3. ∀y (Basket(y) → Easy(y))
********** 3 **********
--- page 4 ---
4. Basket(BK301)
Goal:
Likes(Steve, BK301)
Step 2: Convert to CNF (4 Marks)
Remove implications:
1. ¬Easy(y) ∨ Likes(Steve,y)
2. ¬Science(y) ∨ Hard(y)
3. ¬Basket(y) ∨ Easy(y)
4. Basket(BK301)
Negated Goal:
5. ¬Likes(Steve,BK301)
Step 3: Resolution Proof. (3 Marks)
1. Resolve (3) and (4)
• C3: ¬Basket(y) ∨ Easy(y)
C4: Basket(BK301)
Substitute y = BK301
C6: Easy(BK301)
2. Resolve (1) and C6
C1: ¬Easy(y) ∨ Likes(Steve,y)
Substitute y = BK301
C7: ¬Easy(BK301) ∨ Likes(Steve,BK301)
3. Resolve with C6:
C8: Likes(Steve,BK301)
4. Resolve with Negated Goal
C5: ¬Likes(Steve,BK301)
C8: Likes(Steve,BK301)
Result: NIL (Empty Clause)
Contradicting with fact so inferred that Steve likes BK301.
********** 4 **********
--- page 5 ---
b.   What is the map coloring problem in CSP? Apply the backtracking search method to
solve the map coloring problem.
Ans: Map coloring problem [3 Marks]
Students can give other map example also.
Define following parameters for the map.
◼ Variables WA, NT, Q, NSW, V, SA, T
◼ Domains Di = {red,green,blue}
◼ Constraints: adjacent regions must have different colors
e.g., WA ≠ NT, or (WA,NT) in {(red,green),(red,blue),(green,red),
(green,blue),(blue,red),(blue,green)}
◼ Variable assignments are
commutative}, i.e.,
[ WA = red then NT = green ] same as
[ NT = green then WA = red ]
◼ Only need to consider
assignments to a single variable
at each node   [10]
→ b = d and there are
$d^n$ leaves
◼ Depth-first search for CSPs with
single-variable assignments is
called backtracking search
◼ Backtracking search is the basic
uninformed algorithm for CSPs
Solving by applying backtracking (7 Marks)
Example of map coloring decision where backtracking is applied by satisfying all the
constraints.
a. What is unsupervised learning? Apply one iteration of k-means clustering with
the following dataset and show the clusters.
X1 X2
1   1
Q4   1.5   1.5
1   2   [10]
3   2
3   3
4   2.5
Ans:
Unsupervised Learning: (3 Marks)
********** 5 **********
--- page 6 ---
Unsupervised Learning is a type of machine learning where the algorithm
learns patterns from unlabeled data.
•   In labeled data, you know the output (e.g., “spam” or “not spam”) →
supervised learning.
•   In unlabeled data, you only have inputs, and the algorithm finds structure
→ unsupervised learning.
Goal: Discover hidden patterns, groupings, or features in the data without
explicit guidance.
Plotting of data (1 Mark)
Solving the given example by K-means (5 Marks)
b.   Discuss the architecture of an expert system with a suitable example.
Ans:
Explanation of each component (5 Marks)
Diagram (5 Marks)
[10]
a.   Describe the significance of the PEAS for AI agents. How do you apply it for a utility-
based agent? Give a suitable example.
Q5
[10]
Ans:
Significance (3 Marks)
Utility-based agent (4 Marks)
********** 6 **********
--- page 7 ---
Example applying PEAS (3 Marks)
b.   What is the simulated annealing algorithm? Discuss its significance in the scenario of
the N-queen problem.
Ans:
Discussion on simulated annealing searching algorithm (5 Marks)
[10]
Application in the n-queen scenario – 5 Marks
a.   Explain how variable ordering and value ordering heuristics are used to find a solution
in the timetable preparation. Assume a suitable variable and values.
Ans:
In a CSP-based timetable problem, we assign variables (e.g., classes, subjects, or
Q6   exams) to values (e.g., time slots, rooms) while satisfying constraints such as no
clashes, teacher availability, and room capacity.   [10]
1. Variable Ordering Heuristics
Variable ordering determines which variable to assign next.
Common Strategies:
• Minimum Remaining Values (MRV):
********** 7 **********
--- page 8 ---
o Choose the variable with the fewest legal values left.
o Example: If Math class can only be scheduled in 2 slots while English
has 5 options, schedule Math first.
o   Benefit: Detects failure early.
• Degree Heuristic:
o Choose the variable involved in the largest number of constraints.
o Example: A teacher teaching multiple classes should be scheduled first.
o   Benefit: Reduces future conflicts.
2. Value Ordering Heuristics
Value ordering determines which value to try first for a chosen variable.
Common Strategy:
•   Least Constraining Value (LCV):
o Choose the value that eliminates the fewest options for other variables.
o Example: Assign a time slot to a class that leaves maximum flexibility for
other classes.
o   Benefit: Keeps more options open for remaining assignments.
Example (Timetable Context)
•   Variables: {Math, English, Physics}
•   Values: {Slot1, Slot2, Slot3}
Constraints:
• Math and Physics cannot be taught at the same time (same teacher).
•   English requires a specific room available only in Slot 1 or Slot 2.
Applying heuristics:
•   Variable ordering (MRV):
o   English has only 2 slots → assign it first.
• Value ordering (LCV):
o Choose the slot for English that least restricts Math and Physics.
Conclusion
•   Variable ordering reduces the branching factor by selecting the most
constrained variables first.
• Value ordering increases the chance of success by choosing flexible
assignments.
********** 8 **********
--- page 9 ---
•   Together, they significantly improve the efficiency of solving timetable CSPs.
b.   Explain the learning agent and its necessary components, with a suitable example.
Ans:
Learning Agent Diagram (5 Marks)
[10]
Explanation of each component with example (5 Marks)
Q7
a   Consider the following knowledge base
1.   If food is oily, it is good in taste and not good for health.
2.   If anyone eats unhealthy food, they fall sick.
3. Christina loves oily food, and she eats only what she loves.
4. “Potato wedges” is an oily food item.
Apply and explain the forward chaining method to find whether Christina is healthy or
sick.
Ans: Explanation on Forward Chaining (2 Marks)
[10]
Convert the statements in to FOPL   Forward Chaining Proof (4 Marks)
(4 Marks)
b   Discuss the adversarial search algorithm with the help of the tic-tac-toe game problem.
[10]
How do you prune the unnecessary branches of the game tree?
********** 9 **********
--- page 10 ---
Ans:
Discussion on adversarial search (4 Marks)
Discussion on Pruning by considering complete steps(6 Marks)
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper ad86d6c8bf36

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIDS_7056/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (14 pages), mean OCR confidence 79.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
8. Use of Scientific calculator is allowed.
Q1   Answer briefly:   [20]
CO- 1   a. An intelligent agent   is designed for an autonomous vacuum cleaner.   [05]
SO- 1   Identify the PEAS description for this agent and explain how each component
BL- 2   contributes to its functioning.
Sol   Each description – 1.25 marks (P,E,A,S)
1. Performance Measure (P)
Maximum dirt cleaned
Minimum time taken
Minimum energy consumption
Avoid collisions/damage
Complete coverage of area
2. Environment (E)
Rooms, floors, walls
Furniture and obstacles
Dirt/dust distribution
Humans/pets (dynamic elements)
3. Actuators (A)
Wheels (movement: forward, backward, turn)
Vacuum/suction motor
Brushes
Docking mechanism (charging)
4. Sensors (S)
Dirt sensors
Proximity sensors
Camera/LiDAR
Bump sensors
Cliff sensors (to avoid falling)
CO- 3   b. Explain with examples, various problems due to which hill climbing may get   [05]
SO- 1   stuck.
********** 1 **********
--- page 2 ---
BL-3
Sol   3 problems (Local Maximum, Plateau, Ridge)- 3 marks
Examples – 2 marks
CO- 3   c. Write the sentences “Every object has some color” in to first order predicate   [05]
SO- 1   logic and then convert into skolem normal form. After this convert it into CNF.
BL-3
Sol   Predicate representation – 1 mark
Skolem – 3 marks
CNF- 1 Mark
Skolemization
y depends on xxx → replace with Skolem function f(x)
CNF
CO- 3   d. Solve the following Cryptarithmetic problem: EAT+THAT=APPLE   [05]
SO- 1,6
BL- 4
Sol   Letter   Digit
E   8
A   1
T   9
H   2
P   0
L   7
Q2   a   Analyze the different types of intelligent agents used in Artificial Intelligence.
CO- 1   Compare simple reflex, model-based, goal-based, utility-based, and learning   [10]
SO- 1   agents, and evaluate their suitability for real-world applications.
BL-3
Sol   Analysis different types- 3 marks
Compare – 4 marks
Suitability for real world – 3 marks
Types of Agents
a) Simple Reflex Agents
• Operate using condition–action rules
• Action depends only on current percept
• No memory of past states
********** 2 **********
--- page 3 ---
• Example: Thermostat
•   Fast and simple
b) Model-Based Agents
• Maintain an internal state (model) of the environment
• Use past information + current percept
• Example: Robot navigation system
• Works in partially observable environments
c) Goal-Based Agents
• Use goals to guide actions
• Evaluate possible actions to achieve goal
• Example: Path-finding (A* search)
•   Flexible and goal-oriented
d) Utility-Based Agents
• Use a utility function to measure satisfaction
• Choose action that maximizes utility
• Example: Self-driving car (comfort vs speed vs safety)
• Handles trade-offs and uncertainty
e) Learning Agents
• Improve performance through experience
• Components:
• Learning element
•   Critic
• Performance element
• Example: Reinforcement learning systems
Comparison of Agents
Evaluation for Real-World Applications
• Simple Reflex: Suitable for simple, fully observable environments
• Model-Based: Useful in dynamic systems (robotics, automation)
• Goal-Based: Applied in search and planning problems
•   Utility-Based: Best for decision-making under uncertainty
• Learning Agents:
Most suitable for complex real-world systems like:
o autonomous vehicles
o recommendation systems
********** 3 **********
--- page 4 ---
o healthcare AI
Q2   b   Apply Graph version of Breadth first search on Three water jug problem [A   [10]
CO- 2   standard problem with capacity (8, 5, 3) and start & goal state as (8, 0, 0) & (4,
SO- 7   4, 0) respectively]. Clearly show the frontier and explored set in each iteration.
BL- 4
Sol   Marks as per the below details
BFS Initialization
• Frontier = [(8,0,0)]
• Explored = ∅
Iteration 1
Expand: (8,0,0)
Possible moves:
• A → B → (3,5,0)
• A → C → (5,0,3)
Frontier = [(3,5,0), (5,0,3)]
Explored = {(8,0,0)
Iteration 2
Expand: (3,5,0)
Moves:
• B → C → (3,2,3)
Frontier = [(5,0,3), (3,2,3)]
Explored = {(8,0,0), (3,5,0)}
Iteration 3
Expand: (5,0,3)
Moves:
• C → B → (5,3,0)
Frontier = [(3,2,3), (5,3,0)]
Explored = {(8,0,0), (3,5,0), (5,0,3)}
Iteration 4
Expand: (3,2,3)
Moves:
********** 4 **********
--- page 5 ---
• C → A → (6,2,0)
Frontier = [(5,3,0), (6,2,0)]
Explored = {(8,0,0), (3,5,0), (5,0,3), (3,2,3)}
Iteration 5
Expand: (5,3,0)
Moves:
• B → C → (5,0,3) (already explored)
• A → B → (3,5,0) (already explored)
No new state
Frontier = [(6,2,0)]
Explored updated
Iteration 6
Expand: (6,2,0)
Moves:
• A → B → (1,5,2)
Frontier = [(1,5,2)]
Explored updated
Iteration 7
Expand: (1,5,2)
Moves:
• B → C → (1,4,3)
Frontier = [(1,4,3)]
Explored updated
Iteration 8
Expand: (1,4,3)
Moves:
• C → A → (4,4,0) --- GOAL
Q3   a   Best First Search and A* Search are important informed search strategies used in   [10]
CO- 2   Artificial Intelligence.
SO- 1,6   i.   Explain the working principle of Greedy Best First Search and A* search
algorithms.
********** 5 **********
--- page 6 ---
BL- 4   ii.   Analyze the role of heuristic functions in both algorithms and how they
influence the search process.
iii.   Compare and evaluate Greedy Best First Search and A* in terms of
Completeness, Optimality, Time and space complexity
iv.   Justify why A* is generally preferred over Greedy Best First Search for
optimal pathfinding problems, with a suitable example.
Sol   Working – 3 marks
Role of heuristic – 2 marks
Comparision – 3 marks
Justification – 2 marks
Q3   b   Apply minimax algorithm and Alpha Beta pruning on the following figure to find   [10]
CO- 2   out value of root node. How many evaluations are saved after applying Alpha
SO- 1   Beta pruning.
BL-3
Sol   Find value of a (i.e. 4) by minmax algo – 4 marks
Alpha beta pruning – 6 marks
TWO evaluations are saved
Q4   a   Consider the following axioms:   [10]
CO- 3
1. All hounds howl at night.
SO- 7
2. Anyone who has any cats will not have any mice.
BL- 4
3. Light sleepers do not have anything which howls at night.
********** 6 **********
--- page 7 ---
4. John has either a cat or a hound.
And prove by resolution that If John is a light sleeper, then John does not have
any mice.
Sol   Conversion into clause form – 4 marks
Proof – 6 marks
********** 7 **********
--- page 8 ---
Q4   b   "All people who are not poor and are smart are happy. Those people who can   [10]
CO- 3   read are not stupid. John can read and is wealthy. Happy people have exciting
SO- 7   lives. Can anyone be found with an exciting life?"
Prove by resolution.
BL-4
Sol   Conversion into clause form – 4 marks
Proof – 6 marks
********** 8 **********
--- page 9 ---
Q5   a   Consider a map consisting of six regions: P, Q, R, S, T, and U. The map must be   [10]
CO- 3   colored using the colors Red, Green, Blue, and Yellow such that no two adjacent
SO- 1,6   regions have the same color.
The adjacency relationships between the regions are as follows:
BL- 4
• Region P is adjacent to Q, R, and S
• Region Q is adjacent to P, R, and T
• Region R is adjacent to P, Q, S, and T
• Region S is adjacent to P, R, and U
• Region T is adjacent to Q, R, and U
• Region U is adjacent to S and T
i. Represent this problem as a Constraint Satisfaction Problem (CSP) by
specifying the variables, domains, and constraints with the help of the
diagram.
ii. Assign appropriate colors to all regions such that no two adjacent regions share
the same color.
********** 9 **********
--- page 10 ---
Sol   i.   Representation – 5 marks
ii.   Solving – 5 marks
Region   Color
P   Red
Q   Green
R   Blue
S   Green
T   Red
U   Blue
Each region is a variable: X={P,Q,R,S,T,U}
Domain: Each region can take one of the colors: D={Red,Green,Blue,Yellow}
Constraint: No two adjacent regions can have the same color:
• P≠Q,P≠R,P≠S
• Q≠R,Q≠T
• R≠S,R≠T
• S≠U
• T≠U
Q5   b   Explain the N-Queen Problem in Artificial Intelligence. Illustrate how the 4-   [10]
CO- 3   Queen problem can be solved.
SO- 6
BL-3
Sol   Definition → 2
Constraints → 2
Representation → 2
4-Queen solution (diagram/array) → 3
Explanation of method → 1
The N-Queen Problem is a classical problem in Artificial Intelligence and
combinatorial search. The objective is to place N queens on an N × N chessboard
such that no two queens attack each other.
In chess, a queen can attack another queen if they are in the same:
• Row
• Column
• Diagonal
Therefore, the solution must ensure that no two queens share the same row,
column, or diagonal.
Q6   a   Apply the concept of decision tree to identify Gini Index for each of the attribute   [10]
CO- 4   where final outcome is “Pass Exam”
SO- 2   Day   Study Hours   Attendance   Assignment   Pass Exam
BL-4   1   High   Good   Yes   Yes
2   High   Good   No   Yes
3   Medium   Good   Yes   Yes
4   Low   Poor   No   No
5   Low   Good   No   No
6   Medium   Poor   Yes   No
7   High   Good   Yes   Yes
8   Medium   Good   No   Yes
********** 10 **********
--- page 11 ---
Gini Index of Dataset
Gini = 1 — (PP. + Px)
Pyes = 5/8 = 0.625
Pyo = 3/8 = 0.375
Gini = 1 — (0.625 + 0.3757)

Gini = 0.4688

Gini for Attribute Study Hours

High
Records = 3
Yes = 3

No =0

Ginipyign = 1— (1? + 0”)

=0

Records = 3
Yes = 2
No=1

Gini Medium = 1 — ((2/3)? + (1/3))
=1-(0.444 + 0.111)
= 0.445

Low

Records = 2
Yes = 0
No=2

Ginitow = 1— (0? +1°)

=0

Weighted Gini

Gini studyHours

= (3/8)(0) + (3/8)(0.445) + (2/8)(0)

=0+0.167+0
= 0.167
Attribute Gini Index
Study Hours 0.166
Attendance 0.208
Assignment 0.437

FRI ICR 7 FI OH
--- page 12 ---
Q6   b A dataset contains 8 two-dimensional points representing customer purchasing   [10]
CO- 4   patterns:
SO- 6   Point   X   Y
BL-4   P1   2   10
P2   2   5
P3   8   4
P4   5   8
P5   7   5
P6   6   4
P7   1   2
P8   4   9
Use the K-Means clustering algorithm with K = 3 till two iteratios.
Initial cluster centroids are selected as: C1 = P1 (2,10), C2 = P4 (5,8), C3 = P7
(1,2)
Sol
Iteration 1
Point   C1 C2   C3   Cluster
P1   0   5   9   C1
P2   5   6   4   C3
P3   12   7   9   C2
P4   5   0   10   C2
P5   10   5   9   C2
P6   10   5   7   C2
P7   9   10   0   C3
P8   3   2   10   C2
Point   C1   C2   C3   Cluster
P1   0   8   7   C1
P2   5   5   2   C3
P3   12   4   7   C2
P4   5   3   8   C2
P5   10   2   7   C2
P6   10   2   5   C2
P7   9   9   2   C3
P8   3   5   8   C1
C1 = (3 , 9.5)   C2 = (6.5 , 5.25) C3 = (1.5 , 3.5)
Q7   a   Analyze the limitations of Propositional Logic and explain how Predicate Logic   [05]
CO- 3   overcomes these limitations. Illustrate your answer with suitable examples.
SO- 1
BL- 2,3
Sol   Limitation – 3 marks
Advantages – 2 marks
Limitations of Propositional Logic
i.   Cannot represent objects or relationships
ii.   Cannot express general statements
iii.   No use of variables
iv.   Example limitation: “All humans are mortal” cannot be represented properly
********** 12 **********
--- page 13 ---
Predicate Logic Advantages
Uses: Variables, Predicates, Quantifiers
Example:
∀x(Human(x)→Mortal(x))
b What is Unsupervised Learning? Discuss how clustering are used to discover   [05]
hidden patterns in data.
Sol   i.
ii.   Unsupervised Learning is a type of machine learning where the
algorithm learns patterns from unlabeled data. The system tries to
identify hidden structures or relationships within the dataset without
predefined outputs.
Key Objectives
• Discover hidden patterns in data
• Group similar data points
•   Identify relationships among variables
Common Techniques
1. Clustering
o Groups similar data points together.
Example: Customer segmentation using K-Means clustering.
Q7   b   Explain the development process, limitations, and real-world examples of expert   [10]
CO- 4   systems.
SO- 1
BL-2
Sol   1. Development Process of Expert System
The development of an expert system involves several systematic steps.
1. Problem Identification
•   Identify a domain where expert knowledge is required.
• Define the scope of the system.
2. Knowledge Acquisition
•   Collect knowledge from domain experts, books, and databases.
3. Knowledge Representation
• Convert the collected knowledge into machine-readable form.
• Common techniques include:
o Rule-based representation
o Frames
o Semantic networks
4. System Design
• Design the architecture of the expert system.
•   Select inference techniques.
5. Implementation
• Develop the system using AI tools such as:
o Prolog
o Lisp
o Expert system shells
********** 13 **********
--- page 14 ---
6. Testing and Validation
•   Test the system using real problems.
• Ensure accuracy and reliability.
7. Maintenance and Updating
• Update the knowledge base when new knowledge becomes available.
2. Limitations of Expert Systems
Despite their usefulness, expert systems have several limitations.
1. Lack of Common Sense
• Cannot apply general human reasoning.
2. Knowledge Acquisition Difficulty
•   Extracting expert knowledge is time-consuming and difficult.
3. High Development Cost
• Building and maintaining expert systems requires significant resources.
4. Limited Domain
• Works only in a specific field.
5. No Learning Ability
Traditional expert systems do not learn automatically.
3. Examples of Expert Systems
1. MYCIN
• Developed for diagnosing bacterial infections.
• Used in medical decision support.
2. DENDRAL
• Used in chemistry to analyze molecular structures.
3. XCON (R1)
• Developed by Digital Equipment Corporation.
• Used for configuring computer systems.
4. PROSPECTOR
• Used in geology to identify mineral deposits.
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper db26eaf00eed

- Departments: Computer Engineering
- Programmes: BTech Computer 7002, Integrated Computer 7032, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_Computer_7002/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C032)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: mixed (22 pages), mean OCR confidence 77.2
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   State the differences between Uninformed and Informed Search strategies
with examples.
Solution –
Uninformed Search   Informed Search
Uses no domain-specific   Uses extra knowledge
knowledge beyond the   (heuristics) about the problem
problem definition (start and   to guide the search.
goal states).
Does not know where the goal   Guided by heuristic
CO-2 ;   lies; explores blindly.   information estimating the
SO-   closeness to the goal.   [5]
1,2,6,7 ;   Generally less efficient—   More efficient, as it focuses on
BL-2   explores more nodes before   promising paths first.
reaching the goal.
Time and space complexity   Time and space complexity
usually higher due to   usually lower, as fewer nodes
exhaustive search.   are expanded.
- Breadth-First Search (BFS)   - Greedy Best-First Search
- Depth-First Search (DFS)   - A* Search
- Uniform Cost Search   - Hill Climbing
Marking Scheme –
Each point 1 mark
CO-3 ;   b.   Differentiate between forward and backward chaining with suitable
SO-   examples.   [5]
1,6,7 ;
BL-2   Solution –
********** 1 **********
--- page 2 ---
Forward Chaining   Backward Chaining
Data-driven reasoning — starts   Goal-driven reasoning — starts
from known facts and applies   from a goal (hypothesis) and
inference rules to derive new   works backward to determine
facts until a goal is reached.   which facts must be true to
support the goal.
Goes from facts to conclusion   Goes from goal to facts
Used when all facts are known   Used when the goal is known and
and the objective is to find out   we need to determine whether it
what can be concluded.   can be supported by the facts.
More suitable for data-driven   More suitable for goal-driven
systems, such as expert systems   systems, such as query answering
for monitoring or diagnosis.   or theorem proving.
May generate many irrelevant   More efficient when the number
facts before reaching the goal.   of possible goals is small.
If the facts are: 1. “It is raining.”   Goal: “Is the ground wet?” →
2. “If it is raining, the ground   The system checks: “If it is
will be wet.” → Using forward   raining, the ground will be wet.”
chaining, the system concludes: → Checks whether “It is
“The ground is wet.”   raining.” is true. → If true,
concludes: “The ground is wet.”
Marking Scheme –
Each point 1 mark
c.   Solve the following Cryptarithmatic –
F A I R
+ G A M E
___________
CO-3 ;   P L A Y
SO-
1,6,7 ;   Solution –
BL-3   F = 5, A = 6, I = 7, R = 8, G = 1, M = 9, E = 4, P = 6, L = 2, Y = 0
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
d.   Cluster these points into K = 2 clusters –
Data = [2, 4, 5, 8, 10, 12]
Solution –
CO-4 ;
SO-   Step 1: Initialization
[5]
1,5,6,7 ;   We need to choose two initial cluster centers (means).
BL-3   Let’s pick:
• C1=2C_1 = 2C1=2
• C2=10C_2 = 10C2=10
Step 2: Assignment Step
Assign each data point to the cluster whose mean is closest.
********** 2 **********
--- page 3 ---
Data   Distance from   Distance from   Nearest
Point   C₁=2   C₂=10   Cluster
2   0   8   C₁
4   2   6   C₁
5   3   5   C₁
8   6   2   C₂
10   8   0   C₂
12   10   2   C₂
Clusters after assignment:
• C1={2,4,5}C_1 = \{2, 4, 5\}C1={2,4,5}
• C2={8,10,12}C_2 = \{8, 10, 12\}C2={8,10,12}
Step 3: Update Step
Compute new means for each cluster.
C1′=2+4+53=113=3.67C_1' = \frac{2 + 4 + 5}{3} = \frac{11}{3} =
3.67C1′=32+4+5=311=3.67 C2′=8+10+123=303=10C_2' = \frac{8 + 10
+ 12}{3} = \frac{30}{3} = 10C2′=38+10+12=330=10
So new centers:
• C1=3.67C_1 = 3.67C1=3.67
• C2=10C_2 = 10C2=10
Step 4: Reassign Points
Recalculate cluster memberships.
| Data | |C₁ - x| | |C₂ - x| | Cluster |
|------|---------|---------|----------|
| 2   | 1.67   | 8   |   C₁   |
| 4   | 0.33   | 6   |   C₁   |
| 5   | 1.33   | 5   |   C₁   |
| 8   | 4.33   | 2   |   C₂   |
| 10   | 6.33   | 0   |   C₂   |
| 12   | 8.33   | 2   |   C₂   |
No change in cluster assignment. Thus, algorithm converges.
Final Clusters
• Cluster 1: {2, 4, 5}, mean = 3.67
• Cluster 2: {8, 10, 12}, mean = 10
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
a. Explain the architecture of a Learning-based Agent with neat
Q2   diagram. Clearly describe the roles of its components and showing
how the interaction between these components improves decision-
CO-1, 1,   making over time.
2; SO-   Solution –   [10+5+5]
1,2,   Learning allows an agent to operate in initially unknown environments.
5,6,7;   The learning element modifies the performance element. Learning is
BL-2, 3,   required for true autonomy, Learn by itself and improved.
2   Components of learning agents are: Critic, learning element,
performance element and problem generator.
********** 3 **********
--- page 4 ---
1.Critic Learning Element
Role: Responsible for making improvements to the agent’s
behavior.Uses feedback from the Critic to update strategies, rules, or
models.Adapts to new or previously unseen situations by modifying its
internal knowledge base.
2. Performance Element
Role: Chooses the external actions the agent will perform. Directly
interacts with the environment and executes decisions. Uses the current
knowledge and strategies (which are continuously refined by the
Learning Element).
3. Critic
Role:Provides feedback on the agent’s performance by comparing the
outcome of actions with a fixed performance standard or goal.
Evaluates whether the chosen actions brought the agent closer to
achieving its objective.Supplies this evaluation to the Learning
Element for further improvement.
4. Problem Generator
Role: Suggests exploratory actions that may lead the agent to
discover better strategies.Encourages exploration beyond the already
known knowledge (avoiding getting stuck in local optima).Balances
exploration (trying new things) and exploitation (using known
successful strategies).
Interaction Between the Components
1. The Performance Element interacts with the environment by
taking actions.
2. The Critic observes the results and evaluates them against
desired goals.
3. The Learning Element receives feedback from the Critic and
updates the agent’s knowledge, policies, or strategies.
4. The Problem Generator ensures the agent does not become
static, by suggesting new exploratory actions to discover
potentially better solutions.
Over time, this feedback loop enables the agent to continuously
improve, adapt to dynamic environments, and make better
decisions.
Marking Scheme –
Diagram – 5 marks
Explanation – 5 marks
********** 4 **********
--- page 5 ---
b. Define the PEAS properties and construct a complete PEAS
description for an ‘AI powered drone for environment
monitoring’, clearly explaining each component.
Solution –
1. Performance Measure (P)
These are the criteria to evaluate how well the drone is performing.
Examples:
• Accuracy in detecting environmental parameters (air quality,
temperature, humidity).
• Coverage of assigned area (no area left unmonitored).
• Energy efficiency (battery usage).
• Timeliness (real-time or near real-time data collection).
•   Safety (avoid collisions with obstacles, animals, or humans).
2. Environment (E)
The environment is where the drone operates. Examples:
• Urban areas (parks, streets, industrial zones).
• Rural areas (forests, rivers, lakes, farmlands).
• Weather conditions (sunny, rainy, windy).
• Presence of obstacles (trees, buildings, birds, power lines).
3. Actuators (A)
Actuators are the components the AI agent uses to interact with the
environment. Examples:
•   Propellers (for movement in all directions).
• Camera gimbal (to adjust camera angle).
• Sprayers or samplers (if collecting physical samples).
•   Signal transmitters (send data to base station).
•   Lights or alarms (for navigation or warning).
4. Sensors (S)
Sensors are the components that perceive the environment. Examples:
• Cameras (RGB, infrared) for visual monitoring.
• LIDAR or ultrasonic sensors (for obstacle detection).
• Temperature and humidity sensors.
• Air quality sensors (CO₂, PM2.5, PM10).
• GPS module (for location tracking).
• Accelerometer and gyroscope (for flight stability).
Component   Description
Performance Accuracy of environmental readings, area coverage,
Measure (P) battery efficiency, timely data collection, safety.
Environmen Urban and rural areas, varying weather, obstacles
t (E)   like trees, buildings, animals, humans.
Actuators   Propellers, camera gimbal, sprayers/samplers, signal
(A)   transmitters, lights/alarms.
Cameras (RGB/IR), LIDAR/ultrasonic,
temperature/humidity sensors, air quality sensors,
Sensors (S)
GPS, accelerometer, gyroscope.
Marking Scheme –
Each Property – 1 mark
Discussion – 1 mark
c. Why is Hill Climbing called a local search algorithm? List two
advantages and two disadvantages of Hill Climbing.
********** 5 **********
--- page 6 ---
Solution –
Hill Climbing is called a local search algorithm because:
•   It starts from a current state and iteratively moves to a
neighboring state that improves the evaluation (or fitness)
function.
•   It only considers local information (the current state and its
immediate neighbors) rather than exploring the entire search
space.
•   It does not maintain a complete path or explore previously
visited states extensively.
Advantages of Hill Climbing
1. Simple and easy to implement – It does not require complex
data structures or algorithms.
2. Efficient for small search spaces – Quickly finds a solution if
the landscape is smooth and has a clear peak.
Limitations –
• Can get stuck in local maxima – It may find a suboptimal solution
instead of the global optimum.
• Cannot handle plateaus or ridges well – If multiple neighboring
states have the same value, it may fail to progress.
Marking Scheme –
Explanation of Local Search – 2 Marks
Advantages – 1 mark
Limitation – 2 marks
a. Solve the graph below using A* Search.
Q3
CO-2, 2,
1; SO-   [5+10+5]
1,2,5,6,7;
BL-3, 3,
2
Solution –
********** 6 **********
--- page 7 ---
Marking Scheme –
Approach – 3 marks
Correct Answer – 2 marks
b. Apply Alpha-Beta pruning algorithm to prune the game tree
shown below.
Solution –
Red edges are pruned.
********** 7 **********
--- page 8 ---
Marking Scheme –
Each Correct Prune – 2 marks
c. What are the different types of Environments? Give one example
for each.
Solution –
1. Fully Observable vs Partially Observable
• Fully Observable: The agent can access complete and accurate
information about the environment at any time.
o Example: Chess – the agent knows the exact position of
all pieces on the board.
•   Partially Observable: The agent has limited or noisy
information about the environment.
o Example: Self-driving car – it cannot always see around
corners or through fog.
2. Deterministic vs Stochastic
• Deterministic: The next state is completely determined by the
current state and the agent’s action.
o Example: Tic-Tac-Toe – the outcome of each move is
predictable.
•   Stochastic: The next state involves uncertainty; the same action
may produce different results.
o Example: Rolling a dice – outcome is random even if
you roll the same way.
3. Episodic vs Sequential
• Episodic: The agent’s experience is divided into independent
episodes; the current action does not affect future states.
o Example: Image classification – each image is classified
independently.
• Sequential: The current action affects future states; decisions
have long-term consequences.
o Example: Robot navigation – one wrong move may
block future paths.
4. Static vs Dynamic
********** 8 **********
--- page 9 ---
•   Static: The environment does not change while the agent is
thinking.
o Example: Crossword puzzle – the clues don’t change
while solving.
• Dynamic: The environment changes over time, even if the
agent does nothing.
o Example: Stock market trading – prices change
constantly.
5. Discrete vs Continuous
•   Discrete: A finite number of distinct states and actions.
o Example: Board games like Checkers – a limited number
of moves.
• Continuous: Infinite or continuous range of states or actions.
o Example: Self-driving car speed control – speed can vary
continuously.
Marking Scheme –
Each type with Example – 1 mark
a. Consider the following facts and prove that Tom will receive a
bonus using Resolution Graph.
i. Every employee works on at least one project.
ii. Any project leader is a manager.
iii. Any manager who completes a critical project successfully will
receive a bonus.
iv. Every manager supervises at least one employee.
v. Jerry is an employee.
vi. Tom is a manager.
Q4   vii. Jerry works on the project led by Tom.
viii. Tom completed a critical project successfully.
CO-3, 3;   Solution –   [15+5]
SO-1,6,7;
BL-3, 3
********** 9 **********
--- page 10 ---
Marking Scheme –
Conversion to FOL – 5 marks
Conversion to CNF – 5 marks
Resolution Graph – 5 marks
b. Let X,Y,Z∈{1,2,3,4,5} subject to the constraints: X+Y=Z, X<Y
i. Express this problem in CSP form.
ii. Enumerate all valid solutions.
Solution –
Step 1: Identify variables and domains
We have:
• Variables: X,Y,Z
********** 10 **********
--- page 11 ---
• Domains: {1,2,3,4,5}
Step 2: List the constraints
1. X+Y=Z
2. X<Y
Step 3: Generate candidate pairs for X and Y
Since X<Y, we can list all possible ordered pairs (X,Y) from the
domain:
•   (1,2), (1,3), (1,4), (1,5)
•   (2,3), (2,4), (2,5)
•   (3,4), (3,5)
•   (4,5)
These satisfy the constraint X<Y.
Step 4: Check the sum constraint
For each (X,Y) pair, compute Z=X+Y. Check if Z∈{1,2,3,4,5}
X Y   X+Y = Z   Z in domain?
1   2   3   yes
1   3   4   yes
1   4   5   yes
1   5   6   no
2   3   5   yes
2   4   6   no
2   5   7   no
3   4   7   no
3   5   8   no
4   5   9   no
Step 5: Collect valid solutions
The valid solutions are the pairs where both constraints are satisfied:
(X,Y,Z)=(1,2,3), (1,3,4), (1,4,5), (2,3,5)
Marking Scheme –
Approach – 3 marks
Correct Solution – 2 marks
Q5   a. Convert the following facts into FOL:
CO-3, 3,   i. Every child loves every candy.
4; SO-   ii. Anyone who loves some candy is not a nutrition fanatic.
1,5,6,7;   iii. Anyone who eats any pumpkin is a nutrition fanatic.   [5+5+10]
BL-3, 2,   iv. Anyone who buys any pumpkin either carves it or eats it.
v. John buys a pumpkin.
3   Solution -
********** 11 **********
--- page 12 ---
1. Every child loves every candy.
Px Ky (CHILD (x) A CANDY(y) = LOVES (x,y)

2. Anyone who loves some candy is not a nutrition fanatic.

Wx ( (Fy (CANDY(y) ALOVES(x,y))) + — FANATIC(x))

3. Anyone who eats any pumpkin is a nutrition fanatic.
Wx ((Fy (PUMPKIN(y) A EAT(x,y))) + FANATIC (x))

4. Anyone who buys any pumpkin either carves it or eats it.
bx by (PUMPKIN) A BUY (x,y) + CARVE(x,y) VEAT(x,y))

5. John buys a pumpkin.
3x (PUMPKIN(x) A BUY(John,x))

Marking Scheme —
Each FOL — 1 mark

b. Write down the rules to convert FOL into CNF.
Solution —

FRR ICR] DA KH
--- page 13 ---
Step 1: Eliminate Implications and Biconditionals
© Replace implications P > Q with -P Vv Q.
© Replace biconditionals P <> Q with (P > Q) A (Q => P).

Example:
P=+=Q — -APVvQ

Step 2: Move Negations Inward (Use De Morgan’s Laws)
e Push negations (—) directly onto predicates.
° Apply:
« A(PAQ)=-Pv-Q
« A(PVQ)=-PA-Q
e -~VaeP(x) = 3r-P(zx)
e 732P(x) = Ve7P(x)
Step 3: Standardize Variables
* Rename variables so that each quantifier has a unique variable name.
* Example:


Step 4: Move Quantifiers to the Front (Prenex Form)
¢ All quantifiers should be placed at the beginning of the sentence.
« Example:

Va(P(x) Vv 3yQ(y)) > VeastP(=) V O(y))

Step 5: Skolemization (Remove Existential Quantifiers)
* Replace existential quantifiers (3) with Skolem constants or functions.
* Rules:
* if 3a P(z) has no universal quantifiers before it + replace x with a constant.
«If there are universal quantifiers before it - replace x with a Skolem function of those universal
variables.

Example:

VasyP(z,y) - VaxP(zx, f(x))

Step 6: Drop Universal Quantifiers
* After Skolemization, all remaining variables are universally quantified and can be assumed implicitly.

Step 7: Distribute V over /\

* Convert the formula into conjunctions of disjunctions.
© Apply distributive law:

PV (QAR) =(PVQ)A(PVR)

Step 8: Resulting CNF
* The final formula is @ conjunction of clauses, where each clause is a disjunction of literals (predicate or
negated predicate).

Marking Scheme —
Each rule — 0.5 marks
Concept — 1 mark

FIR ICR 7] QI HO
--- page 14 ---
c. Write k-means clustering algorithm. For the given data, compute two
clusters using K-means algorithm for clustering where initial cluster
centers are (1.0, 1.0) and (5.0, 7.0). Execute for three iterations.
Solution –
Perform same in Iteration 3, and in iteration3 it will be no change, so
conclude the final clusters are –
Marking Scheme –
Algorithm – 3 marks
Correct approach – 2 marks
Iteration 1 – 2 marks
Iteration 2 – 2 marks
Iteration 3 – 1 mark
********** 14 **********
--- page 15 ---
a. Using the dataset, build a decision tree to predict Return. You may use
any decision tree algorithm (ID3 or CART). Determine the root node and
subsequent splits based on your chosen method. Define Inductive
Learning and explain how it can be applied to this dataset. Generate IF–
THEN rules from your decision tree for predicting Return.
Solution –
Q6
CO-4, 4;
SO-   [15+5]
1,5,6,7;
BL-3, 2
********** 15 **********
--- page 16 ---
IF–THEN Rules
1. IF Past Trend = Up THEN Return = Profit
2. IF Past Trend = Down THEN Return = Loss
Inductive Learning
Inductive Learning is the process of learning general rules or patterns
from specific examples or data.
It involves using training data to infer a general model that can predict
outcomes for unseen data.
********** 16 **********
--- page 17 ---
Application to this dataset:
Here, the learning algorithm (ID3) observes the examples of “Past
Trend,” “Open Interest,” and “Trading Volume” along with their
“Return.”
It induces the general rule that “If the Past Trend is Up, then Return is
Profit; if Down, then Return is Loss.”
This learned pattern can now be used to predict the return for new
market data.
Marking Scheme –
Decision Tree – 12 marks
Inductive Learning – 3 marks
b. Describe the architecture of an expert system with a neat diagram.
Solution –
1. Knowledge Base:
The knowledge base is the heart of an expert system. It contains all the
facts, rules, and expert knowledge related to a specific domain. Think of it
as a library filled with textbooks, research papers, and expert opinions.
The accuracy and completeness of the knowledge base directly impact
the system’s performance. If the knowledge is outdated or incomplete,
the system’s recommendations may be flawed.
2. Inference Engine:
The inference engine is the brain of the expert system. It processes the
information stored in the knowledge base to draw conclusions or make
recommendations. The inference engine uses reasoning strategies (like
forward chaining or backward chaining) to analyze data and apply
rules.
• Forward Chaining: Starts with available data and works toward a
conclusion.
• Backward Chaining: Starts with a goal and works backward to find
supporting evidence. For example,
3. User Interface:
The user interface is the bridge that allows users to interact with the
expert system. It’s designed to be intuitive and user-friendly, ensuring that
even non-experts can use the system effectively. Users provide
a query (problem or question), and the system processes the request. The
system then delivers advice or recommendations back to the user.
4. Explanation Module:
The explanation module is a critical feature that explains how the system
arrived at a particular conclusion. It’s like a teacher showing their work
when solving a math problem. This module provides users with a clear,
step-by-step explanation of the system’s reasoning.
********** 17 **********
--- page 18 ---
• This transparency is especially important in fields like healthcare and
finance, where decisions can have significant consequences.
5. Knowledge Acquisition Module:
The knowledge acquisition module is responsible for updating and
expanding the knowledge base. It ensures that the system stays current with
the latest information and trends. Without regular updates, the system’s
knowledge base can become outdated, reducing its effectiveness.
Marking Scheme –
Diagram – 3 marks
Explanation – 2 marks
a. A dataset contains information about 100 customers of a retail store.
The attributes are:
• Age (numeric)
• Income (Low, Medium, High)
• Spending Score (1–100)
• Membership Type (Regular, Premium)
i) Explain how you would use a classification algorithm to predict
whether a new customer will be a Premium member, given the other
attributes. Mention the steps and a suitable algorithm.
ii) Explain how you would use a clustering algorithm to segment the
customers into groups based on their purchasing behaviour (Income and
Spending Score). Describe the steps and a suitable algorithm.
Solution –
Q7
CO-4, 3,   i. To predict whether a new customer will be a Premium or Regular
[5+5+5+5
4, 4; SO-   member, a Decision Tree classification algorithm can be used. The
1,5,6,7;   dataset contains attributes such as Age, Income, and Spending Score,   ]
BL-4, 3,   which act as input features, while Membership Type is the target class.
2, 4   First, the data is preprocessed by converting the categorical attribute
“Income” into numeric form and normalizing the numerical attributes
like Age and Spending Score. The dataset is then divided into training
and testing sets. The Decision Tree algorithm (such as ID3 or C4.5) is
trained on the data, where it learns decision rules based on attribute
values that best separate the classes using measures like Information
Gain or Gini Index. For example, the tree may learn that customers with
a high income and spending score above a certain threshold are more
likely to be Premium members. Once trained, the model can classify new
customers by following the decision paths in the tree to predict their
membership type. This approach is effective because the Decision Tree
handles both numerical and categorical data and produces easily
interpretable rules.
ii. To segment the customers into groups based on their purchasing
behaviour, a clustering algorithm such as K-Means can be used. In this
case, the attributes Income and Spending Score are selected as they
directly represent a customer’s financial capacity and spending pattern.
********** 18 **********
--- page 19 ---
First, the data is preprocessed by converting the categorical attribute
“Income” (Low, Medium, High) into numerical values and scaling the
data to ensure both attributes contribute equally to distance calculations.
Next, the number of clusters (K) is chosen — for example, by using the
Elbow Method, which helps determine the optimal number of customer
segments. The K-Means algorithm is then applied, where it randomly
initializes K cluster centroids and iteratively assigns each customer to the
nearest centroid based on the Euclidean distance, then recalculates
centroids until the clusters stabilize. After clustering, each group
represents a distinct customer segment, such as “Low Income–Low
Spending,” “High Income–High Spending,” or “Medium Income–
Moderate Spending.” These segments help the retail store design targeted
marketing strategies and improve customer satisfaction by tailoring
offers and services to different groups.
Marking Scheme –
Classification – 2.5 marks
Clustering – 2.5 marks
b. Solve the 8-Queens problem using backtracking. Show the stepwise
assignments of the first 4 queens. Identify where backtracking occurs.
Solution –
Below is a clear backtracking trace for the 8-Queens problem. I’ll show
the stepwise assignments of the first 4 queens (Q1–Q4), continue a bit
further to show the conflict that forces backtracking, and explicitly mark
where backtracking happens. I use 1-based coordinates (row, column).
The algorithm places one queen per row, trying columns left→right; a
placement is invalid if it is in the same column or same diagonal as any
already placed queen.
Stepwise placements (rows 1 → 4)
Row 1 (place Q1)
• Try col = 1: no queens yet → place Q1 at (1,1).
Current partial solution: [(1,1)].
Row 2 (place Q2)
• Try col = 1: same column as Q1 → invalid.
• Try col = 2: diagonal with Q1 (|1-2|=1 and |1-2|=1) →
invalid.
• Try col = 3: not same column, not diagonal with Q1 → place
Q2 at (2,3).
Current partial solution: [(1,1), (2,3)].
Row 3 (place Q3)
• Try col = 1: same column as Q1 → invalid.
• Try col = 2: diagonal with Q2 ((2,3) vs (3,2)) → invalid.
• Try col = 3: same column as Q2 → invalid.
• Try col = 4: diagonal with Q2 ((2,3) vs (3,4)) → invalid.
• Try col = 5: safe with respect to Q1 and Q2 → place Q3 at
(3,5).
Current partial solution: [(1,1), (2,3), (3,5)].
Row 4 (place Q4)
********** 19 **********
--- page 20 ---
• Try col = 1: same column as Q1 → invalid.
• Try col = 2: safe wrt Q1,Q2,Q3 → place Q4 at (4,2).
Current partial solution after 4 queens: [(1,1), (2,3),
(3,5), (4,2)].
At this point we have placed the first four queens successfully without
backtracking.
Continue: row 5 → row 6 and the first backtracking point
Row 5 (place Q5) — try columns left→right:
• col = 1: conflict with Q1 (column).
• col = 2: conflict with Q4 (column).
• col = 3: conflict with Q2 (column).
• col = 4: safe → place Q5 at (5,4).
Partial: [(1,1),(2,3),(3,5),(4,2),(5,4)].
Row 6 (place Q6) — try columns:
• col = 1: conflict with Q1.
• col = 2: conflict with Q4.
• col = 3: conflict with Q2.
• col = 4: conflict with Q5.
• col = 5: conflict with Q3.
• col = 6: diagonal conflict with Q1 ( (1,1) vs (6,6) ).
• col = 7: diagonal conflict with Q2 ( (2,3) vs (6,7) ).
• col = 8: diagonal conflict with Q3 ( (3,5) vs (6,8) ).
Result: No valid column found for Q6 when Q5 is at (5,4).
This is the first backtracking event — the algorithm must backtrack
because row 6 has no safe placement.
Backtracking action:
• Backtrack to Row 5, move Q5 to its next candidate column after
4. (i.e., try col = 5,6,7,8 in row 5). If those all fail, we
would backtrack further to Row 4, and so on.
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
c. Explain what an expert system is and   its advantages and
disadvantages.
Solution –
An expert system is a computer program that is designed to solve
complex problems and to provide decision-making ability like a human
expert. It performs this by extracting knowledge from its knowledge base
using the reasoning and inference rules according to the user queries.
Advantages of Expert System
o These systems are highly reproducible.
o They can be used for risky places where the human presence is
not safe.
o Error possibilities are less if the KB contains correct knowledge.
o The performance of these systems remains steady as it is not
affected by emotions, tension, or fatigue.
o They provide a very high speed to respond to a particular query.
********** 20 **********
--- page 21 ---
Limitations of Expert System
o The response of the expert system may get wrong if the knowledge
base contains the wrong information.
o Like a human being, it cannot produce a creative output for
different scenarios.
o   Its maintenance and development costs are very high.
o Knowledge acquisition for designing is much difficult.
o For each domain, we require a specific ES, which is one of the big
limitations.
o   It cannot learn from itself and hence requires manual updates.
Marking Scheme –
Definition – 1 mark
Advantages – 2 marks
Disadvantages – 2 marks
d. A hospital wants to develop an expert system to help diagnose patients
based on their symptoms. The system should be able to suggest a possible
disease and recommend treatment.
Design a simple rule-based expert system for diagnosing three diseases
(e.g., Flu, Cold, and Malaria) based on the following symptoms:
• Fever (High, Low)
• Headache (Yes, No)
• Body Pain (Yes, No)
• Vomiting (Yes, No)
• Write at least 5 IF–THEN rules for this system.
Explain how the expert system would infer a diagnosis when a new
patient provides their symptoms.
Solution –
Rule-Based Expert System for Disease Diagnosis
A rule-based expert system can be designed to help a hospital
diagnose diseases such as Flu, Cold, and Malaria based on patient
symptoms. The system uses IF–THEN rules to represent medical
knowledge and a reasoning engine to infer a possible diagnosis from the
patient’s input symptoms.
Knowledge Base (Rules)
1. IF Fever = High AND Headache = Yes AND Body Pain = Yes
AND Vomiting = Yes
THEN Disease = Malaria AND Treatment = “Take antimalarial
drugs and consult a doctor immediately.”
2. IF Fever = High AND Headache = Yes AND Body Pain = Yes
AND Vomiting = No
THEN Disease = Flu AND Treatment = “Take rest, drink fluids,
and use prescribed antiviral medication.”
3. IF Fever = Low AND Headache = Yes AND Body Pain = No
AND Vomiting = No
THEN Disease = Cold AND Treatment = “Take steam
inhalation, drink warm fluids, and use decongestant if needed.”
********** 21 **********
--- page 22 ---
4. IF Fever = Low AND Headache = No AND Body Pain = Yes
AND Vomiting = No
THEN Disease = Flu (Mild) AND Treatment = “Take adequate
rest and mild fever reducers.”
5. IF Fever = High AND Headache = No AND Body Pain = Yes
AND Vomiting = Yes
THEN Disease = Malaria (Suspected) AND Treatment =
“Recommend blood test and start preventive medication.”
Inference Process (How Diagnosis is Made)
When a new patient enters their symptoms (for example: Fever = High,
Headache = Yes, Body Pain = Yes, Vomiting = No), the inference
engine of the expert system compares these inputs with the conditions
of each rule in the knowledge base. It checks which rule’s IF-part
matches all the given symptoms. In this case, Rule 2’s conditions match
exactly, so the system concludes the diagnosis as Flu and provides the
recommended treatment.
The system follows a forward chaining approach, starting from
known facts (symptoms) and applying rules to reach a conclusion
(disease and treatment). If multiple rules partially match, it can apply a
certainty factor or ask for additional symptoms to refine the diagnosis.
Marking Scheme –
Rules – 3 marks
Inference Process – 2 marks
********** 22 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 0ff2349aa548

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSBS_7036/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: mixed (26 pages), mean OCR confidence 74.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (CSBS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Additional Instructions:
1. Question No. _1___ is compulsory.
2. Out of remaining questions, attempt any __4___ questions.
3. In all ___5_ questions to be attempted.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Draw the flowchart of Genetic Algorithm. Explain the operators of
Genetic Algorithm with diagram.
Solution:
CO-2 ;
SO-   [5]
1,2,6,7 ;
BL-2
********** 1 **********
--- page 2 ---
Marking Scheme –
Flowchart – 2 Marks
Operators – 1 Mark
Explanation – 2 Marks
b.   Convert the following statements into FOL:
1. Every child loves Santa.
2. Everyone who loves Santa loves any reindeer.
3. Rudolph is a reindeer, and Rudolph has a red nose.
4. Anything which has a red nose is weird or is a clown.
5. No reindeer is a clown.
Solution –
CO-3 ;
SO-   [5]
1,6,7 ;
BL-3
Marking Scheme –
Each FOL – 1 Mark
c.   Explain intelligent backtracking with a suitable example.
Solution –
CO-3 ;
SO-   Intelligent backtracking is a smarter version of plain backtracking used [5]
1,6,7 ;   in Constraint Satisfaction Problems (CSPs). Instead of blindly going
BL-3   back to the immediately previous variable when a dead-end occurs, it
analyzes why the failure happened and jumps back directly to the
variable responsible for the conflict.
********** 2 **********
--- page 3 ---
Step 0: Initialize a 4x4 board.
Step 1:
• Put our first Queen (Q1) in the (0,0) cell .
•   'x' represents the cells which is not safe i.e. they are under
attack by the Queen (Q1).
•   After this move to the next row [ 0 -> 1 ].
Step 2:
• Put our next Queen (Q2) in the (1,2) cell .
•   After this move to the next row [ 1 -> 2 ].
Step 3:
• At row 2 there is no cell which are safe to place Queen (Q3) .
• So, backtrack and remove queen Q2 queen from cell ( 1, 2 ) .
Step 4:
• There is still a safe cell in the row 1 i.e. cell ( 1, 3 ).
• Put Queen ( Q2 ) at cell ( 1, 3).
********** 3 **********
--- page 4 ---
Step 5:
• Put queen ( Q3 ) at cell ( 2, 1 ).
Step 6:
• There is no any cell to place Queen ( Q4 ) at row 3.
• Backtrack and remove Queen ( Q3 ) from row 2.
• Again there is no other safe cell in row 2, So backtrack again
and remove queen ( Q2 ) from row 1.
• Queen ( Q1 ) will be remove from cell (0,0) and move to
next safe cell i.e. (0 , 1).
Step 7:
• Place Queen Q1 at cell (0 , 1), and move to next row.
Step 8:
********** 4 **********
--- page 5 ---
• Place Queen Q2 at cell (1 , 3), and move to next row.
Step 9:
• Place Queen Q3 at cell (2 , 0), and move to next row.
Step 10:
• Place Queen Q4 at cell (3 , 2), and move to next row.
• This is one possible configuration of solution
Marking Scheme –
Correct place – 2 Marks
Explanation – 3 Marks
********** 5 **********
--- page 6 ---
d.   Cluster these points into K = 2 clusters –
Data = [2, 3, 6, 8, 10, 12]
Assume the initial centroids are C₁ = 4 and C₂ = 9.
Solution –
CO-4 ;
SO-   [5]
1,5,6,7 ;
BL-2
Marking Scheme –
Approach – 3 Marks
Correct Clusters – 2 Marks
********** 6 **********
--- page 7 ---
a. What are the different types of Agents? Explain with example.
Solution –
Simple reflex agents
•   Simple-reflex agents are simple, but they turn out to be of very
limited intelligence
• The agent will work only if the correct decision can be made on
the basis of the current percept – that is only if the environment
is fully observable
•   Infinite loops are often unavoidable – escape could be possible
by randomizing
Model-based reflex agents
The agent should keep track of the part of the world it can't see now
The agent should maintain some sort of internal state that depends on
the percept history and reflects at least some of the unobserved aspects
Q2
of the current state
CO-1, 1,
2; SO-   Updating the internal state information as time goes by requires two   [10+5
1,2,   kinds of knowledge to be encoded in the agent program   +5]
5,6,7;
BL-2, 3,   •   Information about how the world evolves independently of the
2   agent
•   Information about how the agent's own actions affects the world
Goal-based agents
• Knowing about the current state of the environment is not
always enough to decide what to do (e.g. decision at a road
junction)
• The agent needs some sort of goal information that describes
situations that are desirable
• The agent program can combine this with information about the
results of possible actions in order to choose actions that
achieve the goal
•   Usually requires search and planning
Utility-based agents
********** 7 **********
--- page 8 ---
• Goals alone are not really enough to generate high quality
behavior in most environments – they just provide a binary
distinction between happy and unhappy states
• A more general performance measure should allow a
comparison of different world states according to exactly how
happy they would make the agent if they could be achieved
• Happy – Utility (the quality of being useful)
• A utility function maps a state onto a real number which
describes the associated degree of happiness
• Learning element – responsible for making improvements
• Performance element – responsible for selecting external actions
(it is what we had defined as the entire agent before)
• Learning element uses feedback from the critic on how the
agent is doing and determines how the performance element
should be modified to do better in the future
• Problem generator is responsible for suggesting actions that will
lead to a new and informative experiences
Learning Agents
• Define the PEAS properties. PEAS of Intelligent Exam
Proctoring System.
• What are the differences between Uninformed Search and
Informed Search strategies? Explain with graphical examples.
Marking Scheme –
Each type of Agents – 2 Marks
b. Define the PEAS properties. PEAS of Intelligent Exam Proctoring
System.
Solution –
PEAS for Intelligent Exam Proctoring System
1. Performance Measure (P)
• Detect cheating accurately
• Minimize false positives (wrong accusations)
• Ensure fairness to all students
• Maintain exam integrity
• Real-time alert generation
• High system reliability and uptime
********** 8 **********
--- page 9 ---
2. Environment (E)
• Online exam platform
• Students appearing remotely
• Webcam video/audio feed
•   Different lighting/background conditions
• Network variability
• Devices (laptop, mobile, etc.)
3. Actuators (A)
• Raise alerts/flags for suspicious activity
• Pause or terminate exam session
• Send notifications to invigilator
• Log events (screen switch, multiple faces, etc.)
• Capture screenshots or video clips
4. Sensors (S)
• Webcam (face detection, eye movement)
• Microphone (background noise detection)
• Screen monitoring (tab switching, copy-paste)
• Keyboard/mouse activity
• Network activity logs
Marking Scheme –
Each Property – 1 mark
Discussion – 1 mark
c. What are the differences between Uninformed Search and Informed
Search strategies? Explain with graphical examples.
Solution –
Uninformed Search   Informed Search
It   is   Uninformed   Search   It   is   Heuristic   Search
techniques   techniques.
Uses no domain-specific   Uses extra knowledge
knowledge beyond the   (heuristics) about the problem
problem definition (start and   to guide the search.
goal states).
Does not know where the goal   Guided by heuristic
lies; explores blindly.   information estimating the
closeness to the goal.
Generally less efficient—   More efficient, as it focuses on
explores more nodes before   promising paths first.
reaching the goal.
********** 9 **********
--- page 10 ---
Time and space complexity   Time and space complexity
usually higher due to   usually lower, as fewer nodes
exhaustive search.   are expanded.
- Breadth-First Search (BFS)   - Greedy Best-First Search
- Depth-First Search (DFS)   - A* Search
- Uniform Cost Search   - Hill Climbing
Marking Scheme -
Each point 1 mark
a. Apply A* Search and Greedy Best First Search on the following
Graph and justify the results.
Solution –
Q3   • A = 13
• B = 12   [10+1
CO-2, 2;   • C = 4
SO-   • D = 7   0]
1,2,5,6,7;   • E = 3
BL-3, 3   • F = 8
• G = 2
• H = 0 (Goal)
Step 1: Start at A
Neighbors:
• B (h = 12)
• C (h = 4)
Choose C (lowest heuristic)
Step 2: From C
Neighbors:
• F (h = 8)
• G (h = 2)
Choose G (lowest heuristic)
Step 3: From G
********** 10 **********
--- page 11 ---
Neighbor:
• H (h = 0)
Choose H (goal reached)
Final Path (GBFS Solution)
A→C→G→H
Marking Scheme –
GBFS – 4 Marks
A* Search – 4 Marks
Justification – 2 Marks
b. Apply the Alpha–Beta Pruning algorithm assuming left-to-right
traversal of the tree shown below.
Show the values of α (alpha) and β (beta) at each step of the algorithm.
Identify and mark the branches that are pruned during the search.
Determine the final optimal value at the root node.
********** 11 **********
--- page 12 ---
Solution –
Marking Scheme –
Approach – 2 Marks
Each Correct Pruning – 1 Mark (Total 3 Marks)
Correct Values of Nodes – 0.5 Marks Each (Total 5 Marks)
Convert the following statements into FOL
a. All hounds howl at night.
b. Anyone who has any cats will not have any mice.
Q4
c. Light sleepers do not have anything which howls at night.
[10+5
CO-3, 3;   d. John has either a cat or a hound.
SO-1,6,7;   +5]
BL-3, 3   Prove ‘If John is a light sleeper, then John does not have any mice.’
using Resolution Graph.
Solution –
********** 12 **********
--- page 13 ---
1. ¥x (HOUND(x) + HOWL (x)
— HOUND() VHOWL (x)
2. ¥x Wy (HAVE (xy) ACAT (vy) = — Fz (HAVE(x,z) A MOUSE (2)))
Vx Vy (HAVE (x,y) ACAT (vy) — Wz — (HAVE(x,z) A MOUSE (z)))
Vx Vy Wz (— (HAVE (x,y) ACAT (y)) V— (HAVE(x,z) AMOUSE (2)))
— HAVE(x,y) V— CAT(y) V- HAVE(x,z) V~ MOUSE(2)
3. x (LS(x) + — Fy (HAVE (xy) AHOWL()))
Vx (LS(x) — Vy — (HAVE (xy) AHOWL()))
Vx Vy (LS(x) = — HAVE(x,y) v- HOWL())
Vx Vy (— LS) V— HAVE(%,y) V- HOWL)
— LS(x<) v- HAVE(x,y) v- HOWL(y)
4. 3x (HAVE (John,x) A (CAT(x) VHOUND(x)))
HAVE(John,a) A(CAT(a) VHOUND(a))
5. — [LS(John) — — 3z (HAVE(John,z) A MOUSE(2))] (negated conclusion)
= [= LS (John) v- 3z (HAVE (John, z) A MOUSE(z))]
LS(John) A 3z (HAVE(John, z) A MOUSE(2)))

LS(John) A HAVE(John,b) A MOUSE(b)

The set of CNF clauses for this problem is thus as follows:
1. -— HOUND (x) VHOWL (x)
2. — HAVE(x,y) V- CAT(y) V- HAVE(,2) V- MOUSE()
3. — LS(x) V- HAVE(xy) ¥- HOWL)

4.
1. HAVE(John,a)

2. CAT(a) VHOUND(a)

1. LS(Joim)
2. HAVE(John,b)
3. MOUSE)

FIR ICR 7] QI HO
--- page 14 ---
Marking Scheme –
Correct FOL statements – 0.5 Marks Each (Total 4 Marks)
Conversion into CNF – 3 Marks
Resolution Graph – 3 Marks
b. Write down the rules converting FOL in CNF.
Solution –
********** 14 **********
--- page 15 ---
Marking Scheme –
Each rule – 0.5 marks
Concept – 1 mark
c. Differentiate between backtracking search and local search in CSP.
Solution –
Marking Scheme –
Each difference – 0.5 marks
a. Prove using Cryptarithmatic:
B A S E + B A L L = G A M E S
Solution –
Q5
[5+10
CO-3, 3;
SO-1,6,7;   +5]
BL-3, 3
********** 15 **********
--- page 16 ---
Marking Scheme:
Each Correct Assignment – 0.5 Marks (Total 5 Marks)
b. Solve the constraint satisfaction problem that no two adjacent
vertices have the same colour. Given three colours (Red, Green, Blue).
Solution –
Variables (Possible
Step Action
Values → Assigned)
1   Start   All nodes = {R, G, B}
2   Assign A   A = {R,G,B} → R
Update neighbors (B,
3   B, C ≠ R → {G, B}
C)
4   Assign B   B = {G,B} → G
Update neighbors (C,   C ≠ {R,G} → {B}, D ≠ G
5
D)   → {R,B}
6   Assign C   C = {B} → B
Update neighbors (D, D ≠ {G,B} → {R}, E ≠ B
7
E, F)   → {R,G}, F ≠ B → {R,G}
8   Assign D   D = {R} → R
9   Update neighbor (E)   E ≠ {B,R} → {G}
10   Assign E   E = {G} → G
11   Update neighbor (F)   F ≠ {B,G} → {R}
12   Assign F   F = {R} → R
13   Assign G (isolated)   G = {R,G,B} → B
Variables (Nodes):
A, B, C, D, E, F, G
Constraint:
Adjacent nodes must have different colors
********** 16 **********
--- page 17 ---
Marking Scheme –
Each Step – 0.5 Marks
c. Proof ‘Colonel is criminal’ using Forward chaining and Backward
chaining.
i. It is crime for Americans to sell the weapon to the enemy of America
ii. Country Nono is an enemy of America
iii. Nono has some Missiles
iv. All missiles were sold to Nono by Colonel
v. Colonel is American
vi. Missile is a weapon
Solution –
********** 17 **********
--- page 18 ---
Marking Scheme –
Forward Chaining – 2.5 Marks
Backward Chaining – 2.5 Marks
a. Consider a decision tree for the following set of samples. Write any
two decision rules obtained from the tree. Classify a new sample with
(gender = ‘’Female’’; height = ‘’1.92m’’)
Person ID   Gender   Height   Class
1   Female   1.6m   Short
2   Male   2m   Tall
Q6
CO-4;   3   Female   1.9m   Medium   [10+1
SO-
1,5,6,7;   4   Female   2.1m   Tall   0]
BL-3, 3
5   Female   1.7m   Short
6   Male   1.85m   Medium
7   Female   1.6m   Short
8   Male   1.7m   Short
9   Male   2.2m   Tall
Solution –
********** 18 **********
--- page 19 ---
Step 1: Dataset Summary

Total samples = 9
Class distribution:

* Short = 4
* Medium = 2
* Tall =3

Step 2: Entropy of Dataset

Using entropy formula:

H(S) = —¥) pi logs pi

4. 4 2, 2 3 8
H(S) = — ( —logs ~ + = logy = + = logs =
(S) (Flos § + Flom § + 51085)

H(S) © 1.53

Step 3: Information Gain Calculation
Attribute 1: Gender

Split:
e Female — (Short=3, Medium=1, Tall=1)
e Male — (Short=1, Medium=1, Tall=2)

Entropy(Female) = 1.37
Entropy(Male) ~ 1.50

Weighted entropy:

5 a
= =(1.37) + —(1.50) = 1.43
5 (1.87) + 5 (1-50)

IG(Gender) = 1.53 — 1.43 = 0.10

FRR ICR 7 QI OR
--- page 20 ---
Attribute 2: Height

We split height into ranges:

e < 1.7 = Short (pure)
¢ 1.7-1.95 + Medium (mostly)
e 22.0 = Tall (pure)

Entropy:
e <17-0
e 220-0
e Middle group — small entropy

Weighted entropy = 0.30

IG(Height) = 1.53 — 0.30 = 1.23

Step 4: Choose Root Node

« 1G(Height) = 1.23 (HIGH)
e 1!G(Gender) = 0.10 (LOW)
Root Node = Height

Height
/ | \
£1.7 1.7-1.95 22.8
Short Medium Tall

Step 6: Decision Rules

Rule 1

IF Height = 1.7 m
— Class = Short

Rule 2

IF Height = 2.0 m
— Class = Tall

(Optional Rule 3)

IF 1.7 < Height < 2.0 > Class = Medium

FRI ICR DO) A RH
--- page 21 ---
Predicted Class = Medium
Marking Scheme –
Algorithmic Approach and Correct Calculation – 4 Marks
Correct Tree Construction – 2 Marks
Decision Rules – 2 Marks
Prediction of class – 2 Marks
b. A travel clinic wants to develop an expert system to advise travellers
about possible illnesses based on their symptoms. The system should
suggest a likely disease and recommend precautions.
Diseases: Dengue, Typhoid, and Food Poisoning
Symptoms:
• Fever (High, Low)
• Nausea (Yes, No)
• Stomach Pain (Yes, No)
• Headache (Yes, No)
Solution –
1. Knowledge Representation (Facts)
Symptoms (inputs):
• Fever ∈ {High, Low}
• Nausea ∈ {Yes, No}
• StomachPain ∈ {Yes, No}
• Headache ∈ {Yes, No}
Diseases (outputs):
• Dengue
• Typhoid
• Food Poisoning
2. Rule Base (IF–THEN Rules)
********** 21 **********
--- page 22 ---
Rules for Dengue
• R1: IF Fever = High AND Headache = Yes AND Nausea = Yes
THEN Disease = Dengue
• R2: IF Fever = High AND Headache = Yes AND StomachPain
= No
THEN Disease = Dengue
Rules for Typhoid
• R3: IF Fever = High AND StomachPain = Yes AND Headache
= Yes
THEN Disease = Typhoid
• R4: IF Fever = High AND StomachPain = Yes AND Nausea =
No
THEN Disease = Typhoid
Rules for Food Poisoning
• R5: IF Fever = Low AND Nausea = Yes AND StomachPain =
Yes
THEN Disease = Food Poisoning
• R6: IF Fever = Low AND Nausea = Yes AND Headache = No
THEN Disease = Food Poisoning
3. Inference Mechanism
• Use forward chaining:
o   Start from given symptoms
o Match rules
o Fire the rule whose conditions are satisfied
o Output disease
4. Precautions (Knowledge Base Extension)
Dengue
• Drink plenty of fluids
• Avoid mosquito exposure
• Seek medical care immediately
Typhoid
• Take antibiotics (doctor prescribed)
• Maintain hygiene
• Drink boiled/clean water
Food Poisoning
• Stay hydrated
• Avoid contaminated food
• Take rest
********** 22 **********
--- page 23 ---
5. Example Inference
Input:
• Fever = High
• Headache = Yes
• Nausea = Yes
• StomachPain = No
Triggered Rule: R1
Output: Dengue + precautions
Marking Scheme –
Implementation – 5 Marks
Example – 5 Marks
a. Apply K-means clustering (K = 2) on the following dataset:
(150,50), (155,52), (160,58), (165,62), (170,66), (175,70)
• Use Euclidean distance.
• Perform 2 iterations only.
Take the first two points (150, 50) and (155, 52) as the initial centroids.
Solution –
Given Data Points
(150,50), (155,52), (160,58), (165,62), (170,66), (175,70)
Q7   Initial Centroids
CO-4;   [10+1
SO-   C1 = (150,50)
0]
1,5,6,7;
BL-3, 3   C2 = (155,52)
Iteration 1
Distance to   Cluste
Point   Distance to C1
C2   r
(150,50)   0.00   5.39   C1
(155,52)   5.39   0.00   C2
(160,58)   11.66   6.71   C2
(165,62)   18.03   11.40   C2
(170,66)   24.49   16.40   C2
(175,70)   30.81   21.40   C2
Recalculate Centroids
********** 23 **********
--- page 24 ---
C1 = Mean of points in C1 = (150,50)
C2 = Mean of points in C2 = ((155+160+165+170+175)/5 ,
(52+58+62+66+70)/5) = (165,61.6)
Iteration 2
Point   Distance to C1 Distance to C2 Cluster
(150,50) 0.00   20.80   C1
(155,52) 5.39   11.04   C1
(160,58) 11.66   3.62   C2
(165,62) 18.03   0.45   C2
(170,66) 24.49   5.15   C2
(175,70) 30.81   11.28   C2
Update Centroids Again
C1 = Mean of points in C1 = ((150+155)/2 , (50+52)/2) = (152.5,51)
C2 = Mean of points in C2 = ((160+165+170+175)/4 ,
(58+62+66+70)/4) = (167.5,64)
Cluster   Points   Centroid
C1   (150,50), (155,52)   (152.5,51)
C2   (160,58), (165,62), (170,66), (175,70)   (167.5,64)
Marking Scheme –
Iteration 1 – 4 Marks
Iteration 2 – 4 Marks
Correct Clustering – 2 Marks
b. Evaluate expert systems in modern applications by discussing their
advantages and limitations, also explain the development process of an
expert system along with the challenges involved.
Solution –
1. Development Process
1. Identification
o Define problem, scope, and required expertise.
2. Conceptualization
o Identify key concepts, variables, and relationships.
3. Formalization
o Represent knowledge using rules, frames, or logic.
********** 24 **********
--- page 25 ---
4. Implementation
o Encode rules into the system using a suitable
tool/language.
5. Testing (Validation)
o Test with real cases, refine rules, and improve accuracy.
2. Evaluation of the Process
• Strengths:
o Systematic and structured approach
o Ensures domain knowledge is well-organized
o   Iterative refinement improves accuracy
• Limitations:
o Time-consuming and complex
o Requires close interaction with domain experts
o Difficult to model real-world uncertainty
3. Challenges
1. Knowledge Acquisition Bottleneck
o Extracting expert knowledge is difficult and slow
2. Knowledge Representation Issues
o Choosing the right format (rules, frames, etc.)
3. Scalability (Rule Explosion)
o Large systems require many rules → complex
maintenance
4. Lack of Learning Ability
o Cannot adapt automatically without updates
5. Validation & Reliability
o Ensuring correctness of rules is challenging
6. High Development Cost & Time
o Requires skilled experts and resources
Advantages and Limitations of Expert Systems   5M
Advantages
1. Consistency in Decision Making
o Produces consistent results without human bias or fatigue.
2. Availability (24/7)
o Can operate continuously without breaks, unlike human
experts.
3. Knowledge Preservation
o Stores expert knowledge permanently, even if human experts
leave.
4. Faster Problem Solving
o Provides quick solutions using predefined rules and inference.
********** 25 **********
--- page 26 ---
5. Cost-Effective (Long-term)
o Reduces dependency on highly paid human experts.
6. Explanation Facility
o Can justify decisions with reasoning (IF–THEN rules).
7. Useful in Risky Environments
o Applied in domains like medical diagnosis, fault detection, etc.
Limitations
1. Lack of Learning Ability
o   Traditional expert systems cannot learn or adapt automatically
(unlike modern AI/ML).
2. Knowledge Acquisition Bottleneck
o   Difficult and time-consuming to extract knowledge from
experts.
3. Limited to Specific Domain
o Cannot generalize beyond the programmed domain.
4. High Development Cost
o   Initial development and maintenance can be expensive.
5. No Common Sense Reasoning
o Cannot handle ambiguous or unexpected situations well.
6. Rule Explosion Problem
o Large systems require many rules, making them complex to
manage.
7. Dependence on Quality of Knowledge Base
o   Incorrect or incomplete knowledge leads to wrong decisions.
Marking Scheme –
Development – 4 Marks
Advantages – 3 Marks
Limitation – 3 Marks
********** 26 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 74941ea02b7b

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7011/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C042)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (19 pages), mean OCR confidence 77.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
a.   What are crossover and mutation in Genetic Algorithm? How do they
differ?
Ans:1.a.
Genetic Algorithm (GA) is a search and optimization technique
inspired by the process of natural evolution. Crossover and mutation
are the two key genetic operators used to create new solutions and
improve the quality of the population over successive generations.
Crossover is a process in which two parent chromosomes exchange
parts of their genetic material to produce one or more offspring. The
CO- ;   main objective of crossover is to combine good features from both
SO- ;   parents so that better solutions can be generated. For example, consider   [5]
BL-   two parent chromosomes:
Parent 1 = 110010
Parent 2 = 101111
If single-point crossover is applied after the third bit, the offspring
produced will be:
Offspring = 110111.
Crossover usually occurs with a high probability and helps in exploiting
existing good solutions.
Mutation is an operator that randomly changes one or more genes in a
chromosome. Its purpose is to maintain diversity in the population and
prevent the algorithm from getting stuck in local optimum solutions. For
example, if mutation is applied to the chromosome 110111 by flipping
********** 1 **********
--- page 2 ---
the last bit, the mutated chromosome becomes 110110. Mutation is
applied with a very low probability.
Difference:
Crossover combines information from two parents, whereas mutation
modifies a single chromosome. Crossover focuses on exploiting existing
solutions, while mutation introduces new variations and supports
exploration of the search space.
b.   In First Order Logic, a model provides a precise meaning to the
symbols used in logical expressions by mapping them to objects and
relations in the real or abstract world. A first-order model w consists of
a domain of objects and an interpretation function that assigns
meanings to symbols.
A model w maps:
• Constant symbols to objects in the domain
Example:
w(alice) = o1
w(bob) = o2
w(arithmetic) = o3
• Predicate symbols to tuples of objects
For a binary predicate, the mapping is to pairs of objects:
w(Knows) = {(o1, o3), (o2, o3), ...}
CO- ;
SO- ;   This means Alice knows Arithmetic and Bob knows Arithmetic.   [5]
BL-
Example: Students John and Bob
Given the statement:
“John and Bob are students”
Logical representation:
Student(john) ∧ Student(bob)
Different possible interpretations (models) are:
• w₁ (Valid model)
w₁(john) = o1
w₁(bob) = o2
w₁(Student) = {o1, o2}
********** 2 **********
--- page 3 ---
• w₂ (Invalid model)
Both john and bob map to the same object o1.
This violates the Unique Names Assumption.
• w₃ (Invalid model)
An object exists in the domain (e.g., o3) with no constant symbol
referring to it.
This violates the Domain Closure Assumption.
Restrictions in First Order Logic Models
1. Unique Names Assumption
Each object has at most one constant symbol.
This restriction eliminates models like w₂, where different
constants refer to the same object.
2. Domain Closure Assumption
Every object in the domain must be named by at least one
constant symbol.
This restriction eliminates models like w₃, where unnamed
objects exist.
c.   Solve using Cryptarithmetic
EAT
+ THAT
CO- ;
SO- ;   ------   [5]
BL-   APPLE
EAT=819 THAT=9219 APPLE=10038
d.   How to evaluate K-mean Model? How to select the optimal value of K.
Ans 1.d.
K-Means is an unsupervised clustering algorithm, so it is evaluated using
internal clustering metrics rather than accuracy. The goal is to measure how
well data points are grouped within clusters and separated across clusters.,
CO- ;
SO- ;   Silhouette Score measures how similar a point is to its own cluster   [5]
compared to other clusters.
BL-
s= (b−a)/ max(a,b)
where
•   a = average distance to points in the same cluster
• b = average distance to points in the nearest other cluster
• Range: −1 to +1
********** 3 **********
--- page 4 ---
• Higher value → better clustering
Elbow Method
•   Plot WCSS vs K
• Choose K at the “elbow point” where WCSS reduction slows
down
A smart city uses an AI-based traffic management system that collects
data from cameras, sensors, and GPS devices to control traffic lights
a.
and reduce congestion.
1. Model this system as an intelligent agent, Identify sensors,
actuators, and the agent function.
2. Classify the environment:
[15]
•   Is it fully/partially observable?
• Deterministic or stochastic?
• Episodic or sequential?
•   Static or dynamic?
• Discrete or continuous?
3. Justify your design choices
• Explain why the selected agent type is appropriate
Q2
for handling real-time traffic conditions.
CO-; SO-;
BL-
Ans 2.a.
a.   1. Modeling the Smart Traffic Management System as an
Intelligent Agent
The AI-based traffic management system can be modelled as an
intelligent agent that continuously perceives traffic conditions and
takes actions to optimize traffic flow. The sensors of the agent include
traffic cameras at intersections, road-embedded sensors, and GPS data
from vehicles, which provide real-time information about vehicle
density, speed, congestion, and incidents. The actuators of the agent   [5]
are the traffic signals, variable message signboards, and lane control
mechanisms that allow the system to change signal timings and traffic
directions.
The agent function maps percepts (traffic density, queue length,
waiting time, and congestion levels) to actions (changing signal
durations, prioritizing emergency vehicles, and rerouting traffic).
Formally, the agent function can be represented as:
********** 4 **********
--- page 5 ---
f:Percept History→Action
The goal of the agent is to minimize congestion, reduce waiting time,
and ensure smooth traffic flow across the city.
2. Classification of the Environment
• Observability:
The environment is partially observable because although
cameras and sensors provide extensive data, the agent cannot
observe all factors such as driver intentions, sudden breakdowns,
or unexpected pedestrian behavior.
• Deterministic or Stochastic:
The environment is stochastic, as traffic conditions change
unpredictably due to human behavior, weather conditions,
accidents, and random events.
• Episodic or Sequential:
The environment is sequential because current decisions (signal
timings) affect future traffic conditions and congestion levels.
•   Static or Dynamic:
The environment is dynamic since traffic conditions change
continuously even while the agent is making decisions.
• Discrete or Continuous:
The environment is continuous, as traffic flow, speed, and time
are measured on continuous scales.
3. Justification of Design Choices
The intelligent agent must operate in real time and continuously adapt
to changing traffic conditions. Since traffic data is noisy and
incomplete, a simple reflex agent is insufficient. The system requires a
learning-based, model-based agent that can predict traffic patterns,
adapt signal timings dynamically, and improve performance over time
using historical data. The use of AI techniques such as reinforcement
learning allows the agent to optimize long-term traffic flow rather than
making short-sighted decisions.
b. Write a short note on Hill climbing, Provide at least three limitations.
Ans.2.b. Hill climbing is a local search algorithm used in Artificial
Intelligence for solving optimization problems. It starts with an initial
state and iteratively moves to a neighboring state that has a better value
according to a given evaluation (heuristic) function. The algorithm
continues this process until no neighboring state offers an improvement,
at which point it terminates. Hill climbing is often described as a
greedy approach because it always selects the locally best option
without considering the global picture. It is commonly used in problems
********** 5 **********
--- page 6 ---
such as scheduling, path optimization, and constraint satisfaction
where the search space is large.
Limitations of Hill Climbing
1. Local Maxima:
Hill climbing can get stuck at a local maximum where no
neighboring state is better, even though a better global solution
exists elsewhere in the search space.
2. Plateaus:
The algorithm may encounter flat regions in the search space
where neighboring states have the same evaluation value,
causing it to stop without reaching an optimal solution.
3. Ridges:
In some problems, the optimal path requires a series of sideways
or diagonal moves, but hill climbing may fail because it only
considers direct improvements.
Differentiate between Blind search and Informed search. Given an
a.   initial state of a 8-puzzle problem and final state to be reached. Find the
most cost-effective path to reach the final state from the initial state
using A* Algorithm. Consider g(n)=Depth of node and h(n)=Number of
misplaced tiles.
2   8   3   1   2   3   [10]
8   4
1   6   4
7   6   5
7   5
Initial State   Final State
Q3
CO-; SO-;   Differentiate between Blind Search and Informed Search
BL-   Ans
Aspect   Blind Search   Informed Search
wer   Knowledge used Uses no additional knowledge about goal   Uses heuristic information
Guidance   Explores nodes blindly   Guided toward the goal
Efficiency   Less efficient, explores many nodes   More efficient, fewer node expansions
Optimality   Not always optimal   Can be optimal (e.g., A*)
b.   Examples   BFS, DFS, Uniform Cost Search   A*, Greedy Best-First Search
Time & Space   Usually high   Comparatively lower
[10]
2. A Algorithm for 8-Puzzle Problem*
Given
•   g(n) = Depth of node
•   h(n) = Number of misplaced tiles
•   f(n) = g(n) + h(n)
********** 6 **********
--- page 7 ---
Step 1: Heuristic Calculation for Initial State
Compare initial and goal states (ignore blank):
Misplaced tiles: 2, 8, 1, 6
h(n)=4h(n) = 4h(n)=4
Depth:
g(n)=0g(n) = 0g(n)=0 f(n)=g(n)+h(n)=0+4=4f(n) = g(n) + h(n) = 0 + 4 =
4f(n)=g(n)+h(n)=0+4=4
Step 2: Generate Successor States
Blank can move Up, Left, Right
Move 1: Blank moves UP
2 8 3
1 _ 4
7 6 5
Misplaced tiles: 2, 8, 1
h(n)=3,  g(n)=1h(n) = 3,\; g(n) = 1h(n)=3,g(n)=1 f(n)=4f(n) = 4f(n)=4
Move 2: Blank moves LEFT
2 8 3
1 6 4
_ 7 5
Misplaced tiles: 2, 8, 1, 6, 7
h(n)=5,  g(n)=1h(n) = 5,\; g(n) = 1h(n)=5,g(n)=1 f(n)=6f(n) = 6f(n)=6
Move 3: Blank moves RIGHT
2 8 3
1 6 4
7 5 _
Misplaced tiles: 2, 8, 1, 6, 5
h(n)=5,  g(n)=1
f(n)=6
Step 3: Choose Node with Lowest f(n)
✔ Best node: Blank moves UP (f = 4)
Step 4: Continue Expansion
From:
2 8 3
1 _ 4
7 6 5
Blank moves LEFT
2 8 3
_ 1 4
7 6 5
Misplaced tiles: 2, 8
h(n)=2,  g(n)=2h(n) = 2,\; g(n) = 2h(n)=2,g(n)=2 f(n)=4f(n) = 4f(n)=4
Next Move: Blank moves UP
_ 8 3
2 1 4
7 6 5
Not optimal → discard
Optimal Expansion Leads to Goal
Continuing A* expansions with minimum f(n) leads to:
********** 7 **********
--- page 8 ---
1 2 3
8 _ 4
7 6 5
Final Result
• A finds the most cost-effective path.
• Uses heuristic to minimize expansions.
• Guarantees optimal solution since heuristic is admissible
b. Given a complete binary tree of depth 3:
• Leaf values:
3, 5, 6, 9, 1, 2, 0, -1
1. Apply Alpha-Beta pruning and find actually evaluated nodes and
2. Pruned nodes and Calculate percentage of pruning.
Ans:
Category   Result
3, 5, 6, 1,
Evaluated nodes
2
Pruned nodes   9, 0, −1
Total leaves   8
Nodes pruned   3
Pruning
37.5%
percentage
Using a predicate logic, convert following sentences to predicate and
a.   prove:   [15]
1. Every teacher who teaches a subject is knowledgeable in that
subject. 2. Anyone who is knowledgeable in a subject can answer all
Q4   questions about that subject.
CO-; SO-;   3. Every student who takes a subject from a teacher becomes
BL-   knowledgeable in that subject.
4. Ron is a student who takes AI from ProfRaima.
5. ProfRaima is a teacher who teaches AI.
Prove CanAnswer(Ron, AI).
Ans.4.a
********** 8 **********
--- page 9 ---
Step 1: Predicate Definitions   [5]
b.
•   Teacher(x), Student(x)
•   Teaches(x, s)
•   Takes(x, s, y)
•   Knowledgeable(x, s)
•   CanAnswer(x, s)
Constants:
Ron, ProfRaima, AI
Step 2: Convert All Statements to CNF
********** 9 **********
--- page 10 ---
(3)
VaVsVy|(Student(x) \ Teacher(y) \ Takes(z, s,y)) + Knowledgeable(z, s)|
Remove implication:
—>Student(x) V ~Teacher(y) V ~Takes(zx, s,y) V Knowledgeable(z, s)
Clause (C3):

—Student(x) V ~Teacher(y) V ~Takes(a, s,y) V Knowledgeable(z, s)

(4) Facts:
Student(Ron)
Takes(Ron, AI, Prof Raima)

Clauses:

* (C4): Student(Ron)
* (C5): Takes(Ron, Al, ProfRaima)

(5) Facts:
Teacher(Prof Raima)

Teaches(Prof Raima, AI)

Clauses:

© (C6): Teacher(ProfRaima)
© (C7): Teaches(ProfRaima, Al)

Step 3: Negate Goal

Goal:
CanAnswer(Ron, Al)
Negation:
=CanAnswer(Ron, AI)
Clause (C8):
=CanAnswer(Ron, AI)

FRR ICR 7 OI HOH
--- page 11 ---
Q. Why do we use backward chaining? Write an algorithm.
Ans. Backward chaining is a goal-driven inference technique used in Artificial
Intelligence, especially in expert systems and rule-based systems. It starts
with a goal (query) and works backward to determine whether the known
facts and rules can satisfy that goal.
BACKWARD-CHAINING (KnowledgeBase KB, Goal G)
1. If G is present in KB as a fact
return TRUE
2. For each rule R in KB of the form:
IF P1 ∧ P2 ∧ ... ∧ Pn → G
********** 11 **********
--- page 12 ---
do
For each premise Pi in R
result = BACKWARD-CHAINING(KB, Pi)
If result is FALSE
break and try next rule
If all Pi return TRUE
return TRUE
3. If no rule can infer G
return FALSE
Sudoku is a popular puzzle where each number from 1 to 9 must appear
exactly once in every row, column, and 3×3 sub-grid.
a.   1. Model the Sudoku puzzle as a CSP.
2. Identify the types of constraints involved.
3. Explain how constraint propagation and backtracking are
used to solve Sudoku efficiently.
Ans.a.: Sudoku is a classic example of a Constraint Satisfaction
Problem (CSP) in Artificial Intelligence, where the objective is to
assign values to variables while satisfying a set of constraints. Each cell
in the Sudoku grid must be filled in such a way that the puzzle rules are   [10]
followed strictly.
1. Modeling Sudoku as a CSP
b.   Sudoku can be modeled as a CSP by defining the following
Q5   components:
CO-; SO-;
• Variables:
BL-   Each cell in the 9×9 Sudoku grid is a variable. Thus, there are 81
variables, commonly denoted as XijX_{ij}Xij, where iii and jjj
represent the row and column positions.
• Domains:
The domain of each variable is the set {1,2,3,4,5,6,7,8,9}\{1, 2,
3, 4, 5, 6, 7, 8, 9\}{1,2,3,4,5,6,7,8,9}.
[10]
For cells that are pre-filled in the puzzle, the domain is restricted
to the given value.
• Constraints:
Constraints ensure that Sudoku rules are satisfied, i.e., numbers
1 to 9 appear exactly once in each row, column, and 3×3 sub-
grid.
Thus, Sudoku is effectively represented as a CSP with variables,
domains, and constraints.
2. Types of Constraints Involved
********** 12 **********
--- page 13 ---
The constraints in Sudoku are mainly binary and global constraints:
• Row Constraints: All variables in the same row must have
different values (All-Different constraint).
• Column Constraints: All variables in the same column must
have different values.
• Sub-grid Constraints: Each 3×3 sub-grid must contain all digits
from 1 to 9 without repetition.
• Unary Constraints: Pre-filled cells impose unary constraints by
fixing the value of a variable.
3. Use of Constraint Propagation and Backtracking
Constraint propagation is used to reduce the domain of variables by
enforcing constraints. Techniques such as forward checking and arc
consistency (AC-3) eliminate values from a cell’s domain that violate
Sudoku rules. This significantly reduces the search space before actual
guessing begins.
When constraint propagation alone is insufficient, backtracking search
is applied. The algorithm selects an unassigned cell, assigns a value
from its domain, and recursively attempts to solve the remaining puzzle.
If a constraint violation occurs, the algorithm backtracks and tries a
different value. Heuristics such as Minimum Remaining Values
(MRV) and Least Constraining Value (LCV) further improve
efficiency.
Qb. An AI system solving a configuration problem faces repeated
failures deep in the search tree.
1. Why is normal backtracking inefficient here?
2. How does intelligent backtracking help?
3. Mention any limitation of intelligent backtracking.
Ans b:
1. Why is Normal Backtracking Inefficient?
Normal (chronological) backtracking becomes inefficient in
configuration problems when failures occur deep in the search tree. In
such cases, the algorithm backtracks only to the most recent variable
assignment, even if the cause of failure is an earlier decision. This
leads to repeated exploration of similar invalid paths and redundant
computations. As a result, the search process wastes time revisiting the
same conflicting assignments, especially in large and complex
configuration spaces.
2. How Does Intelligent Backtracking Help?
Intelligent backtracking, also known as conflict-directed
backtracking, improves efficiency by analyzing the actual cause of
********** 13 **********
--- page 14 ---
failure. Instead of backtracking step by step, it jumps directly to the
variable responsible for the conflict. It records conflict sets that identify
which variable assignments led to the failure and avoids repeating them.
By pruning large irrelevant parts of the search tree, intelligent
backtracking significantly reduces unnecessary recomputation and
speeds up problem-solving.
3. Limitation of Intelligent Backtracking
One major limitation of intelligent backtracking is the additional
memory and computation overhead required to store and analyze
conflict sets. Maintaining these conflict explanations can be costly for
very large problems. Additionally, if conflicts are weakly informative or
highly dynamic, the benefits of intelligent backtracking may be limited.
a.   Qa.A logistics company wants to divide a city into 2 delivery zones to
minimize travel distance for drivers. Each delivery location   is
represented by coordinates (x, y).
Given Locations:
[10]
(2,3), (3,4), (5,8), (6,9), (8,2), (9,3)
Initial Centroids:
•   C₁ = (2,3) → Zone 1
• C₂ = (8,2) → Zone 2
Perform two Iteration of K-Means and form clusters.
Ans a. Delivery locations (x, y):
Q6   P1 (2,3), P2 (3,4), P3 (5,8), P4 (6,9), P5 (8,2), P6 (9,3)
CO-; SO-;   Number of clusters: K = 2
Initial Centroids:
BL-
•   C₁ = (2,3) → Zone 1
•   C₂ = (8,2) → Zone 2   [10]
Distance measure: Euclidean distance
Iteration 1
Step 1: Assign points to nearest centroid
Point Distance to C₁ (2,3) Distance to C₂ (8,2) Assigned Cluster
(2,3) 0   √37 ≈ 6.08   Zone 1
(3,4) √2 ≈ 1.41   √29 ≈ 5.38   Zone 1
(5,8) √34 ≈ 5.83   √45 ≈ 6.70   Zone 1
(6,9) √52 ≈ 7.21   √53 ≈ 7.28   Zone 1
(8,2) √37 ≈ 6.08   0   Zone 2
(9,3) √49 = 7   √2 ≈ 1.41   Zone 2
********** 14 **********
--- page 15 ---
Clusters after Iteration 1
• Zone 1: (2,3), (3,4), (5,8), (6,9)
• Zone 2: (8,2), (9,3)
Step 2: Recalculate Centroids
New C₁:
(2+3+5+64,3+4+8+94)=(4,6)\left(\frac{2+3+5+6}{4}, \frac{3+4+8+9}{4}\right) =
(4,6)(42+3+5+6,43+4+8+9)=(4,6)
New C₂:
(8+92,2+32)=(8.5,2.5)\left(\frac{8+9}{2}, \frac{2+3}{2}\right) = (8.5,2.5)(28+9
,22+3)=(8.5,2.5)
Iteration 2
Step 1: Reassign points using updated centroids
Point Distance to C₁ (4,6) Distance to C₂ (8.5,2.5) Assigned Cluster
(2,3) √13 ≈ 3.61   √42.5 ≈ 6.52   Zone 1
(3,4) √5 ≈ 2.24   √32.5 ≈ 5.70   Zone 1
(5,8) √5 ≈ 2.24   √46.5 ≈ 6.82   Zone 1
(6,9) √13 ≈ 3.61   √52.5 ≈ 7.24   Zone 1
(8,2) √32 ≈ 5.66   √0.5 ≈ 0.71   Zone 2
(9,3) √34 ≈ 5.83   √0.5 ≈ 0.71   Zone 2
Clusters after Iteration 2
• Zone 1: (2,3), (3,4), (5,8), (6,9)
• Zone 2: (8,2), (9,3)
Clusters remain unchanged, so the algorithm has converged.
Final Centroids
•   C₁ = (4,6)
•   C₂ = (8.5,2.5)
Q .b. Calculate the Entropy and Information Gain for the dataset below
and identify the best attribute to split while constructing a decision tree.
Predicting whether a customer will subscribe to a service
Usage
Support Calls Contract Type Subscribe
Level
High   Low   Annual   Yes
Medium   Low   Monthly   Yes
Low   High   Monthly   No
High   Low   Annual   Yes
Medium   High   Monthly   No
Low   High   Annual   No
High   Low   Monthly   Yes
********** 15 **********
--- page 16 ---
Medium   High   Annual   No
• Compute the entropy of the target variable (Subscribe).
•   Calculate information gain for each attribute:
o Usage Level
o Support Calls
o Contract Type
•   Identify the best attribute to split.
Ans b. 1. Entropy of Target Variable (Subscribe)
Class Distribution
•   Yes = 4
• No = 4
Entropy(S)=−(4/8 log 2 4/8+ 4/8 log 2 4/8) <- base 2
Entropy(S)=−(0.5×−1+0.5×−1)
Entropy(S)=1.0
2. Information Gain Calculation
A) Attribute: Usage Level
Usage Level Yes No Total
High   3   0 3
Medium   1   2 3
Low   0   2 2
Entropy for each subset
• High Entropy=0(pure)
• Medium Entropy=−(1/3 log 2 1/3+ 2/3 log 2 2/3)=0.918
• Low Entropy=0(pure)
Weighted Entropy: E(Usage)=3/8(0)+3/8(0.918)+2/8(0)
E(Usage)=0.344
Information Gain: IG(Usage)=1.0−0.344=0.656
B) Attribute: Support Calls
Support Calls Yes No Total
Low   4   0 4
High   0   4 4
Entropy
• Low → 0
•   High → 0
Weighted Entropy
E(Support)=4/8(0)+ 4/8(0) =0
Information Gain
IG(Support)=1.0−0=1.0
C) Attribute: Contract Type
********** 16 **********
--- page 17 ---
Contract Type Yes No Total
Annual   2   2 4
Monthly   2   2 4
Entropy for each subset
Entropy=−(2/4 log 2 2/4+ 2/4 log 2 2/4)=1
Weighted Entropy
E(Contract)=4/8(1)+4/8(1)=1
Information Gain
IG(Contract)=1.0−1.0=0
3. Best Attribute to Split
Attribute   Information Gain
Usage Level   0.656
Support Calls 1.0 (Highest)
Contract Type 0
Best Attribute to Split: Support Calls
•   Entropy of Subscribe = 1.0
•   Information Gain:
o Usage Level = 0.656
o Support Calls = 1.0
o Contract Type = 0
•   Best split attribute = Support Calls
Qa. Design a medical expert system:
a.   • Define knowledge base, inference engine
•   Explain rule representation
Ans.a.
b.   1. Knowledge Base   [15]
The knowledge base stores medical domain knowledge required for
Q7   diagnosis and treatment. It contains:
CO-; SO-;
•   Facts: Patient information such as symptoms, age, test results, and
BL-
medical history
•   Rules: Logical relationships between symptoms and diseases
[5]
• Medical knowledge: Disease descriptions, severity levels, and
treatment protocols
Example facts:
•   Patient has fever
•   Patient has cough
•   Patient has high white blood cell count
********** 17 **********
--- page 18 ---
The accuracy of the medical expert system depends heavily on the
quality and completeness of this knowledge base.
2. Inference Engine
The inference engine is responsible for reasoning and decision-making.
It applies rules to known facts to infer new information or conclusions.
In a medical expert system, the inference engine may use:
• Forward chaining: Starts from patient symptoms and derives possible
diseases
• Backward chaining: Starts with a suspected disease and checks if
supporting symptoms exist
The inference engine also resolves conflicts when multiple rules are
applicable and provides explanations for its conclusions, which is
crucial in healthcare systems.
3. Rule Representation (With Examples)
Medical expert systems commonly use IF–THEN production rules for
knowledge representation because they closely resemble human
reasoning and are easy to understand and modify.
Sample Medical Rules
Rule 1:
IF fever AND cough AND chest_pain
THEN disease = Pneumonia
Rule 2:
IF fever AND body_ache AND sore_throat
THEN disease = Viral_Fever
Rule 3:
IF high_blood_sugar AND frequent_urination AND
excessive_thirst
THEN disease = Diabetes
Rule 4:
IF disease = Pneumonia
THEN treatment = Antibiotics
Rule 5:
IF disease = Diabetes
THEN recommendation = Lifestyle_Modification AND
Insulin_Therapy
These rules allow the system to logically map symptoms to diagnoses
and recommend treatments in a structured manner.
Q.b. Explain quantifiers in First-Order Logic. Illustrate with suitable example.
Ans.b. 1. Universal Quantifier ( ∀ )
The universal quantifier states that a predicate is true for all elements
in the domain of discourse.
Syntax:
∀xP(x)
Meaning:
“For every x, P(x) is true.”
Example:
Statement: All students are registered.
Logical representation:
∀x(Student(x)→Registered(x))
********** 18 **********
--- page 19 ---
This means that every object x in the domain, if it is a student, then it
must be registered.
2. Existential Quantifier ( ∃ )
The existential quantifier states that there exists at least one element
in the domain for which the predicate is true.
Syntax:
∃xP(x)
Meaning:
“There exists at least one x such that P(x) is true.”
Example:
Statement: Some student has topped the exam.
Logical representation:
∃x(Student(x)∧Topper(x))
This asserts that at least one student in the domain is a topper.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 4c18fc266cf4

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CS_7055/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: mixed (26 pages), mean OCR confidence 74.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (CSBS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Additional Instructions:
1. Question No. _1___ is compulsory.
2. Out of remaining questions, attempt any __4___ questions.
3. In all ___5_ questions to be attempted.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Draw the flowchart of Genetic Algorithm. Explain the operators of
Genetic Algorithm with diagram.
Solution:
CO-2 ;
SO-   [5]
1,2,6,7 ;
BL-2
********** 1 **********
--- page 2 ---
Marking Scheme –
Flowchart – 2 Marks
Operators – 1 Mark
Explanation – 2 Marks
b.   Convert the following statements into FOL:
1. Every child loves Santa.
2. Everyone who loves Santa loves any reindeer.
3. Rudolph is a reindeer, and Rudolph has a red nose.
4. Anything which has a red nose is weird or is a clown.
5. No reindeer is a clown.
Solution –
CO-3 ;
SO-   [5]
1,6,7 ;
BL-3
Marking Scheme –
Each FOL – 1 Mark
c.   Explain intelligent backtracking with a suitable example.
Solution –
CO-3 ;
SO-   Intelligent backtracking is a smarter version of plain backtracking used [5]
1,6,7 ;   in Constraint Satisfaction Problems (CSPs). Instead of blindly going
BL-3   back to the immediately previous variable when a dead-end occurs, it
analyzes why the failure happened and jumps back directly to the
variable responsible for the conflict.
********** 2 **********
--- page 3 ---
Step 0: Initialize a 4x4 board.
Step 1:
• Put our first Queen (Q1) in the (0,0) cell .
•   'x' represents the cells which is not safe i.e. they are under
attack by the Queen (Q1).
•   After this move to the next row [ 0 -> 1 ].
Step 2:
• Put our next Queen (Q2) in the (1,2) cell .
•   After this move to the next row [ 1 -> 2 ].
Step 3:
• At row 2 there is no cell which are safe to place Queen (Q3) .
• So, backtrack and remove queen Q2 queen from cell ( 1, 2 ) .
Step 4:
• There is still a safe cell in the row 1 i.e. cell ( 1, 3 ).
• Put Queen ( Q2 ) at cell ( 1, 3).
********** 3 **********
--- page 4 ---
Step 5:
• Put queen ( Q3 ) at cell ( 2, 1 ).
Step 6:
• There is no any cell to place Queen ( Q4 ) at row 3.
• Backtrack and remove Queen ( Q3 ) from row 2.
• Again there is no other safe cell in row 2, So backtrack again
and remove queen ( Q2 ) from row 1.
• Queen ( Q1 ) will be remove from cell (0,0) and move to
next safe cell i.e. (0 , 1).
Step 7:
• Place Queen Q1 at cell (0 , 1), and move to next row.
Step 8:
********** 4 **********
--- page 5 ---
• Place Queen Q2 at cell (1 , 3), and move to next row.
Step 9:
• Place Queen Q3 at cell (2 , 0), and move to next row.
Step 10:
• Place Queen Q4 at cell (3 , 2), and move to next row.
• This is one possible configuration of solution
Marking Scheme –
Correct place – 2 Marks
Explanation – 3 Marks
********** 5 **********
--- page 6 ---
d.   Cluster these points into K = 2 clusters –
Data = [2, 3, 6, 8, 10, 12]
Assume the initial centroids are C₁ = 4 and C₂ = 9.
Solution –
CO-4 ;
SO-   [5]
1,5,6,7 ;
BL-2
Marking Scheme –
Approach – 3 Marks
Correct Clusters – 2 Marks
********** 6 **********
--- page 7 ---
a. What are the different types of Agents? Explain with example.
Solution –
Simple reflex agents
•   Simple-reflex agents are simple, but they turn out to be of very
limited intelligence
• The agent will work only if the correct decision can be made on
the basis of the current percept – that is only if the environment
is fully observable
•   Infinite loops are often unavoidable – escape could be possible
by randomizing
Model-based reflex agents
The agent should keep track of the part of the world it can't see now
The agent should maintain some sort of internal state that depends on
the percept history and reflects at least some of the unobserved aspects
Q2
of the current state
CO-1, 1,
2; SO-   Updating the internal state information as time goes by requires two   [10+5
1,2,   kinds of knowledge to be encoded in the agent program   +5]
5,6,7;
BL-2, 3,   •   Information about how the world evolves independently of the
2   agent
•   Information about how the agent's own actions affects the world
Goal-based agents
• Knowing about the current state of the environment is not
always enough to decide what to do (e.g. decision at a road
junction)
• The agent needs some sort of goal information that describes
situations that are desirable
• The agent program can combine this with information about the
results of possible actions in order to choose actions that
achieve the goal
•   Usually requires search and planning
Utility-based agents
********** 7 **********
--- page 8 ---
• Goals alone are not really enough to generate high quality
behavior in most environments – they just provide a binary
distinction between happy and unhappy states
• A more general performance measure should allow a
comparison of different world states according to exactly how
happy they would make the agent if they could be achieved
• Happy – Utility (the quality of being useful)
• A utility function maps a state onto a real number which
describes the associated degree of happiness
• Learning element – responsible for making improvements
• Performance element – responsible for selecting external actions
(it is what we had defined as the entire agent before)
• Learning element uses feedback from the critic on how the
agent is doing and determines how the performance element
should be modified to do better in the future
• Problem generator is responsible for suggesting actions that will
lead to a new and informative experiences
Learning Agents
• Define the PEAS properties. PEAS of Intelligent Exam
Proctoring System.
• What are the differences between Uninformed Search and
Informed Search strategies? Explain with graphical examples.
Marking Scheme –
Each type of Agents – 2 Marks
b. Define the PEAS properties. PEAS of Intelligent Exam Proctoring
System.
Solution –
PEAS for Intelligent Exam Proctoring System
1. Performance Measure (P)
• Detect cheating accurately
• Minimize false positives (wrong accusations)
• Ensure fairness to all students
• Maintain exam integrity
• Real-time alert generation
• High system reliability and uptime
********** 8 **********
--- page 9 ---
2. Environment (E)
• Online exam platform
• Students appearing remotely
• Webcam video/audio feed
•   Different lighting/background conditions
• Network variability
• Devices (laptop, mobile, etc.)
3. Actuators (A)
• Raise alerts/flags for suspicious activity
• Pause or terminate exam session
• Send notifications to invigilator
• Log events (screen switch, multiple faces, etc.)
• Capture screenshots or video clips
4. Sensors (S)
• Webcam (face detection, eye movement)
• Microphone (background noise detection)
• Screen monitoring (tab switching, copy-paste)
• Keyboard/mouse activity
• Network activity logs
Marking Scheme –
Each Property – 1 mark
Discussion – 1 mark
c. What are the differences between Uninformed Search and Informed
Search strategies? Explain with graphical examples.
Solution –
Uninformed Search   Informed Search
It   is   Uninformed   Search   It   is   Heuristic   Search
techniques   techniques.
Uses no domain-specific   Uses extra knowledge
knowledge beyond the   (heuristics) about the problem
problem definition (start and   to guide the search.
goal states).
Does not know where the goal   Guided by heuristic
lies; explores blindly.   information estimating the
closeness to the goal.
Generally less efficient—   More efficient, as it focuses on
explores more nodes before   promising paths first.
reaching the goal.
********** 9 **********
--- page 10 ---
Time and space complexity   Time and space complexity
usually higher due to   usually lower, as fewer nodes
exhaustive search.   are expanded.
- Breadth-First Search (BFS)   - Greedy Best-First Search
- Depth-First Search (DFS)   - A* Search
- Uniform Cost Search   - Hill Climbing
Marking Scheme -
Each point 1 mark
a. Apply A* Search and Greedy Best First Search on the following
Graph and justify the results.
Solution –
Q3   • A = 13
• B = 12   [10+1
CO-2, 2;   • C = 4
SO-   • D = 7   0]
1,2,5,6,7;   • E = 3
BL-3, 3   • F = 8
• G = 2
• H = 0 (Goal)
Step 1: Start at A
Neighbors:
• B (h = 12)
• C (h = 4)
Choose C (lowest heuristic)
Step 2: From C
Neighbors:
• F (h = 8)
• G (h = 2)
Choose G (lowest heuristic)
Step 3: From G
********** 10 **********
--- page 11 ---
Neighbor:
• H (h = 0)
Choose H (goal reached)
Final Path (GBFS Solution)
A→C→G→H
Marking Scheme –
GBFS – 4 Marks
A* Search – 4 Marks
Justification – 2 Marks
b. Apply the Alpha–Beta Pruning algorithm assuming left-to-right
traversal of the tree shown below.
Show the values of α (alpha) and β (beta) at each step of the algorithm.
Identify and mark the branches that are pruned during the search.
Determine the final optimal value at the root node.
********** 11 **********
--- page 12 ---
Solution –
Marking Scheme –
Approach – 2 Marks
Each Correct Pruning – 1 Mark (Total 3 Marks)
Correct Values of Nodes – 0.5 Marks Each (Total 5 Marks)
Convert the following statements into FOL
a. All hounds howl at night.
b. Anyone who has any cats will not have any mice.
Q4
c. Light sleepers do not have anything which howls at night.
[10+5
CO-3, 3;   d. John has either a cat or a hound.
SO-1,6,7;   +5]
BL-3, 3   Prove ‘If John is a light sleeper, then John does not have any mice.’
using Resolution Graph.
Solution –
********** 12 **********
--- page 13 ---
1. ¥x (HOUND(x) + HOWL (x)
— HOUND() VHOWL (x)
2. ¥x Wy (HAVE (xy) ACAT (vy) = — Fz (HAVE(x,z) A MOUSE (2)))
Vx Vy (HAVE (x,y) ACAT (vy) — Wz — (HAVE(x,z) A MOUSE (z)))
Vx Vy Wz (— (HAVE (x,y) ACAT (y)) V— (HAVE(x,z) AMOUSE (2)))
— HAVE(x,y) V— CAT(y) V- HAVE(x,z) V~ MOUSE(2)
3. x (LS(x) + — Fy (HAVE (xy) AHOWL()))
Vx (LS(x) — Vy — (HAVE (xy) AHOWL()))
Vx Vy (LS(x) = — HAVE(x,y) v- HOWL())
Vx Vy (— LS) V— HAVE(%,y) V- HOWL)
— LS(x<) v- HAVE(x,y) v- HOWL(y)
4. 3x (HAVE (John,x) A (CAT(x) VHOUND(x)))
HAVE(John,a) A(CAT(a) VHOUND(a))
5. — [LS(John) — — 3z (HAVE(John,z) A MOUSE(2))] (negated conclusion)
= [= LS (John) v- 3z (HAVE (John, z) A MOUSE(z))]
LS(John) A 3z (HAVE(John, z) A MOUSE(2)))

LS(John) A HAVE(John,b) A MOUSE(b)

The set of CNF clauses for this problem is thus as follows:
1. -— HOUND (x) VHOWL (x)
2. — HAVE(x,y) V- CAT(y) V- HAVE(,2) V- MOUSE()
3. — LS(x) V- HAVE(xy) ¥- HOWL)

4.
1. HAVE(John,a)

2. CAT(a) VHOUND(a)

1. LS(Joim)
2. HAVE(John,b)
3. MOUSE)

FIR ICR 7] QI HO
--- page 14 ---
Marking Scheme –
Correct FOL statements – 0.5 Marks Each (Total 4 Marks)
Conversion into CNF – 3 Marks
Resolution Graph – 3 Marks
b. Write down the rules converting FOL in CNF.
Solution –
********** 14 **********
--- page 15 ---
Marking Scheme –
Each rule – 0.5 marks
Concept – 1 mark
c. Differentiate between backtracking search and local search in CSP.
Solution –
Marking Scheme –
Each difference – 0.5 marks
a. Prove using Cryptarithmatic:
B A S E + B A L L = G A M E S
Solution –
Q5
[5+10
CO-3, 3;
SO-1,6,7;   +5]
BL-3, 3
********** 15 **********
--- page 16 ---
Marking Scheme:
Each Correct Assignment – 0.5 Marks (Total 5 Marks)
b. Solve the constraint satisfaction problem that no two adjacent
vertices have the same colour. Given three colours (Red, Green, Blue).
Solution –
Variables (Possible
Step Action
Values → Assigned)
1   Start   All nodes = {R, G, B}
2   Assign A   A = {R,G,B} → R
Update neighbors (B,
3   B, C ≠ R → {G, B}
C)
4   Assign B   B = {G,B} → G
Update neighbors (C,   C ≠ {R,G} → {B}, D ≠ G
5
D)   → {R,B}
6   Assign C   C = {B} → B
Update neighbors (D, D ≠ {G,B} → {R}, E ≠ B
7
E, F)   → {R,G}, F ≠ B → {R,G}
8   Assign D   D = {R} → R
9   Update neighbor (E)   E ≠ {B,R} → {G}
10   Assign E   E = {G} → G
11   Update neighbor (F)   F ≠ {B,G} → {R}
12   Assign F   F = {R} → R
13   Assign G (isolated)   G = {R,G,B} → B
Variables (Nodes):
A, B, C, D, E, F, G
Constraint:
Adjacent nodes must have different colors
********** 16 **********
--- page 17 ---
Marking Scheme –
Each Step – 0.5 Marks
c. Proof ‘Colonel is criminal’ using Forward chaining and Backward
chaining.
i. It is crime for Americans to sell the weapon to the enemy of America
ii. Country Nono is an enemy of America
iii. Nono has some Missiles
iv. All missiles were sold to Nono by Colonel
v. Colonel is American
vi. Missile is a weapon
Solution –
********** 17 **********
--- page 18 ---
Marking Scheme –
Forward Chaining – 2.5 Marks
Backward Chaining – 2.5 Marks
a. Consider a decision tree for the following set of samples. Write any
two decision rules obtained from the tree. Classify a new sample with
(gender = ‘’Female’’; height = ‘’1.92m’’)
Person ID   Gender   Height   Class
1   Female   1.6m   Short
2   Male   2m   Tall
Q6
CO-4;   3   Female   1.9m   Medium   [10+1
SO-
1,5,6,7;   4   Female   2.1m   Tall   0]
BL-3, 3
5   Female   1.7m   Short
6   Male   1.85m   Medium
7   Female   1.6m   Short
8   Male   1.7m   Short
9   Male   2.2m   Tall
Solution –
********** 18 **********
--- page 19 ---
Step 1: Dataset Summary

Total samples = 9
Class distribution:

* Short = 4
* Medium = 2
* Tall =3

Step 2: Entropy of Dataset

Using entropy formula:

H(S) = —¥) pi logs pi

4. 4 2, 2 3 8
H(S) = — ( —logs ~ + = logy = + = logs =
(S) (Flos § + Flom § + 51085)

H(S) © 1.53

Step 3: Information Gain Calculation
Attribute 1: Gender

Split:
e Female — (Short=3, Medium=1, Tall=1)
e Male — (Short=1, Medium=1, Tall=2)

Entropy(Female) = 1.37
Entropy(Male) ~ 1.50

Weighted entropy:

5 a
= =(1.37) + —(1.50) = 1.43
5 (1.87) + 5 (1-50)

IG(Gender) = 1.53 — 1.43 = 0.10

FRR ICR 7 QI OR
--- page 20 ---
Attribute 2: Height

We split height into ranges:

e < 1.7 = Short (pure)
¢ 1.7-1.95 + Medium (mostly)
e 22.0 = Tall (pure)

Entropy:
e <17-0
e 220-0
e Middle group — small entropy

Weighted entropy = 0.30

IG(Height) = 1.53 — 0.30 = 1.23

Step 4: Choose Root Node

« 1G(Height) = 1.23 (HIGH)
e 1!G(Gender) = 0.10 (LOW)
Root Node = Height

Height
/ | \
£1.7 1.7-1.95 22.8
Short Medium Tall

Step 6: Decision Rules

Rule 1

IF Height = 1.7 m
— Class = Short

Rule 2

IF Height = 2.0 m
— Class = Tall

(Optional Rule 3)

IF 1.7 < Height < 2.0 > Class = Medium

FRI ICR DO) A RH
--- page 21 ---
Predicted Class = Medium
Marking Scheme –
Algorithmic Approach and Correct Calculation – 4 Marks
Correct Tree Construction – 2 Marks
Decision Rules – 2 Marks
Prediction of class – 2 Marks
b. A travel clinic wants to develop an expert system to advise travellers
about possible illnesses based on their symptoms. The system should
suggest a likely disease and recommend precautions.
Diseases: Dengue, Typhoid, and Food Poisoning
Symptoms:
• Fever (High, Low)
• Nausea (Yes, No)
• Stomach Pain (Yes, No)
• Headache (Yes, No)
Solution –
1. Knowledge Representation (Facts)
Symptoms (inputs):
• Fever ∈ {High, Low}
• Nausea ∈ {Yes, No}
• StomachPain ∈ {Yes, No}
• Headache ∈ {Yes, No}
Diseases (outputs):
• Dengue
• Typhoid
• Food Poisoning
2. Rule Base (IF–THEN Rules)
********** 21 **********
--- page 22 ---
Rules for Dengue
• R1: IF Fever = High AND Headache = Yes AND Nausea = Yes
THEN Disease = Dengue
• R2: IF Fever = High AND Headache = Yes AND StomachPain
= No
THEN Disease = Dengue
Rules for Typhoid
• R3: IF Fever = High AND StomachPain = Yes AND Headache
= Yes
THEN Disease = Typhoid
• R4: IF Fever = High AND StomachPain = Yes AND Nausea =
No
THEN Disease = Typhoid
Rules for Food Poisoning
• R5: IF Fever = Low AND Nausea = Yes AND StomachPain =
Yes
THEN Disease = Food Poisoning
• R6: IF Fever = Low AND Nausea = Yes AND Headache = No
THEN Disease = Food Poisoning
3. Inference Mechanism
• Use forward chaining:
o   Start from given symptoms
o Match rules
o Fire the rule whose conditions are satisfied
o Output disease
4. Precautions (Knowledge Base Extension)
Dengue
• Drink plenty of fluids
• Avoid mosquito exposure
• Seek medical care immediately
Typhoid
• Take antibiotics (doctor prescribed)
• Maintain hygiene
• Drink boiled/clean water
Food Poisoning
• Stay hydrated
• Avoid contaminated food
• Take rest
********** 22 **********
--- page 23 ---
5. Example Inference
Input:
• Fever = High
• Headache = Yes
• Nausea = Yes
• StomachPain = No
Triggered Rule: R1
Output: Dengue + precautions
Marking Scheme –
Implementation – 5 Marks
Example – 5 Marks
a. Apply K-means clustering (K = 2) on the following dataset:
(150,50), (155,52), (160,58), (165,62), (170,66), (175,70)
• Use Euclidean distance.
• Perform 2 iterations only.
Take the first two points (150, 50) and (155, 52) as the initial centroids.
Solution –
Given Data Points
(150,50), (155,52), (160,58), (165,62), (170,66), (175,70)
Q7   Initial Centroids
CO-4;   [10+1
SO-   C1 = (150,50)
0]
1,5,6,7;
BL-3, 3   C2 = (155,52)
Iteration 1
Distance to   Cluste
Point   Distance to C1
C2   r
(150,50)   0.00   5.39   C1
(155,52)   5.39   0.00   C2
(160,58)   11.66   6.71   C2
(165,62)   18.03   11.40   C2
(170,66)   24.49   16.40   C2
(175,70)   30.81   21.40   C2
Recalculate Centroids
********** 23 **********
--- page 24 ---
C1 = Mean of points in C1 = (150,50)
C2 = Mean of points in C2 = ((155+160+165+170+175)/5 ,
(52+58+62+66+70)/5) = (165,61.6)
Iteration 2
Point   Distance to C1 Distance to C2 Cluster
(150,50) 0.00   20.80   C1
(155,52) 5.39   11.04   C1
(160,58) 11.66   3.62   C2
(165,62) 18.03   0.45   C2
(170,66) 24.49   5.15   C2
(175,70) 30.81   11.28   C2
Update Centroids Again
C1 = Mean of points in C1 = ((150+155)/2 , (50+52)/2) = (152.5,51)
C2 = Mean of points in C2 = ((160+165+170+175)/4 ,
(58+62+66+70)/4) = (167.5,64)
Cluster   Points   Centroid
C1   (150,50), (155,52)   (152.5,51)
C2   (160,58), (165,62), (170,66), (175,70)   (167.5,64)
Marking Scheme –
Iteration 1 – 4 Marks
Iteration 2 – 4 Marks
Correct Clustering – 2 Marks
b. Evaluate expert systems in modern applications by discussing their
advantages and limitations, also explain the development process of an
expert system along with the challenges involved.
Solution –
1. Development Process
1. Identification
o Define problem, scope, and required expertise.
2. Conceptualization
o Identify key concepts, variables, and relationships.
3. Formalization
o Represent knowledge using rules, frames, or logic.
********** 24 **********
--- page 25 ---
4. Implementation
o Encode rules into the system using a suitable
tool/language.
5. Testing (Validation)
o Test with real cases, refine rules, and improve accuracy.
2. Evaluation of the Process
• Strengths:
o Systematic and structured approach
o Ensures domain knowledge is well-organized
o   Iterative refinement improves accuracy
• Limitations:
o Time-consuming and complex
o Requires close interaction with domain experts
o Difficult to model real-world uncertainty
3. Challenges
1. Knowledge Acquisition Bottleneck
o Extracting expert knowledge is difficult and slow
2. Knowledge Representation Issues
o Choosing the right format (rules, frames, etc.)
3. Scalability (Rule Explosion)
o Large systems require many rules → complex
maintenance
4. Lack of Learning Ability
o Cannot adapt automatically without updates
5. Validation & Reliability
o Ensuring correctness of rules is challenging
6. High Development Cost & Time
o Requires skilled experts and resources
Advantages and Limitations of Expert Systems   5M
Advantages
1. Consistency in Decision Making
o Produces consistent results without human bias or fatigue.
2. Availability (24/7)
o Can operate continuously without breaks, unlike human
experts.
3. Knowledge Preservation
o Stores expert knowledge permanently, even if human experts
leave.
4. Faster Problem Solving
o Provides quick solutions using predefined rules and inference.
********** 25 **********
--- page 26 ---
5. Cost-Effective (Long-term)
o Reduces dependency on highly paid human experts.
6. Explanation Facility
o Can justify decisions with reasoning (IF–THEN rules).
7. Useful in Risky Environments
o Applied in domains like medical diagnosis, fault detection, etc.
Limitations
1. Lack of Learning Ability
o   Traditional expert systems cannot learn or adapt automatically
(unlike modern AI/ML).
2. Knowledge Acquisition Bottleneck
o   Difficult and time-consuming to extract knowledge from
experts.
3. Limited to Specific Domain
o Cannot generalize beyond the programmed domain.
4. High Development Cost
o   Initial development and maintenance can be expensive.
5. No Common Sense Reasoning
o Cannot handle ambiguous or unexpected situations well.
6. Rule Explosion Problem
o Large systems require many rules, making them complex to
manage.
7. Dependence on Quality of Knowledge Base
o   Incorrect or incomplete knowledge leads to wrong decisions.
Marking Scheme –
Development – 4 Marks
Advantages – 3 Marks
Limitation – 3 Marks
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper fe9007c569e4

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIDS_7056/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
8. Use of Scientific calculator is allowed.
Q1   Answer briefly:   [20]
CO- 1   a. A movie recommendation system suggests movies based on user ratings and   [05]
SO- 1   preferences. Explain how a utility-based agent can be used to choose the best
BL- 2   recommendation among multiple options.
sol   Explanation – 5 marks
A utility-based agent selects actions based on a utility function, which measures
how desirable an outcome is. It does not just achieve a goal, but chooses the best
possible option among many by maximizing utility.
Application in Movie Recommendation System
In a movie recommendation system:
• The agent considers multiple movie options
• Each movie is assigned a utility value based on user preferences
Factors Used to Compute Utility
Utility can be calculated using:
• User ratings (past preferences)
• Genre preference
•   Popularity or reviews
•   Similarity to previously liked movies
• Context (time, mood, etc.)
Example
Suppose three movies are available:
********** 1 **********
--- page 2 ---
Movi
Genre Match Rating Utility Score
e
A   High   4.5   0.9
B   Medium   4.8   0.8
C   High   4.0   0.85
The agent computes utility for each movie and selects:
Movie A (highest utility = 0.9)
CO- 2   b. Explain the working of Genetic algorithm with reference to 8-puzzle problem.   [05]
SO- 1
BL-3
Sol   Explanation – 5 marks
CO- 3   c. Write the following sentences in to first order predicate logic.   [05]
SO- 1
BL-3   i.   Deepak is either a surgeon or a lawyer.
ii.   All surgeons are doctors.
iii.   Deepak has a boss who is a lawyer.
iv.   There exists a lawyer, all of whose customers are doctors.
v.   Harish is not a customer of any lawyer.
Sol   1 mark for each
i.   Surgeon(Deepak)∨Lawyer(Deepak)
ii.   ∀x(Surgeon(x)→Doctor(x))
iii.   ∃x(Boss(x,Deepak)∧Lawyer(x))
iv.   ∃x(Lawyer(x)∧∀y(Customer(y,x)→Doctor(y)))
v.   ¬∃x(Lawyer(x)∧Customer(Harish,x))
CO- 3   d. Solve the following cryptarithmetic puzzle: CROSS+ROADS=DANGER   [05]
SO- 1,6
BL- 4
Sol
Letter   Digit
C   9
R   6
O   2
S   3
A   5
D   1
N   8
G   7
E   4
********** 2 **********
--- page 3 ---
Q2   a   Write   the PEAS   description   for “Vacuum   Cleaner” AI   system.
CO- 1   Analyze the task environment properties of it.   [10]
SO- 1
BL-3
Sol   PEAS – 5 marks
Characteristics – 5 marks
Performance Measure (P): Cleanliness of environment , Minimum energy
consumption, Minimum time taken, Avoid collisions
Environment (E): Rooms (grid/world) , Dirt locations, Obstacles/walls, May be
single or multiple rooms
Actuators (A): Move (Left, Right, Up, Down) , Suck dirt, Stop
Sensors (S): Dirt sensor (clean/dirty), Location sensor, Obstacle sensor
Properties:
a) Observability
•   Partially observable (if agent cannot see entire room)
•   Fully observable (if full map available)
b) Deterministic vs Stochastic
•   Deterministic: actions predictable
•   Stochastic: dirt may reappear randomly
c) Episodic vs Sequential
•   Sequential: current action affects future states
d) Static vs Dynamic
•   Static: environment does not change
• Dynamic: new dirt appears
e) Discrete vs Continuous
• Usually discrete (grid world)
f) Single-agent vs Multi-agent
•   Typically single-agent
Q2   b What is the maximum number of nodes generated in the following searching   [10]
CO- 2   algorithms with branching factor of b and depth d?
SO- 7   i.   Depth limited DFS with depth d
BL- 4   ii.   Iterative Deepening Search (IDS)
iii.   Breadth first search
What are the total numbers of nodes generated for b = 6 and d =8. Why these
algorithms are called uninformed search algorithms?
Sol   Number of nodes calculation – 3 marks each
Why? – 1 mark
********** 3 **********
--- page 4 ---
ii.
iii. Similar to Depth first search
These algorithms are called uninformed (blind) search because:
• They do not use any domain knowledge or heuristics
• They explore the search space without guidance
• Only use:
o   Initial state
o Successor function
o Goal test
Q3a   How many heuristics can be described for 8-puzzle problem? Explain it with an   [10]
CO- 2   example. Comment whether these are admissible and consistent heuristics. If yes,
SO- 6   how?
BL- 4
Sol   2 heuristic with example – 3 marks each
2 marks consistent heuristic
2 marks admissible heuristic
Q3   b   Apply minimax algorithm and Alpha Beta pruning on the following figure to find   [10]
CO- 2   out value of root node. How many evaluations are saved while applying Alpha
SO- 7   Beta pruning.
BL-3
********** 4 **********
--- page 5 ---
Sol   Find value of a (i.e. 4) by minmax algo – 4 marks
Alpha beta pruning – 6 marks
Q4   a   Consider the following axioms:   [10]
CO- 3
SO- 7   1. Every student is enrolled in at least one course.
BL- 4   2. If a person is enrolled in a course and the course exists, then the person
studies that course.
3. If a person studies a course, then the person passes that course.
4. John is a student.
Prove that: John passes at least one course by resolution.
Sol   Conversion into clause form – 4 marks
Proof – 6 marks
********** 5 **********
--- page 6 ---
Q4   b   Consider the following axioms:   [10]
CO- 3
SO- 7   1. Every teacher teaches at least one subject.
BL-4   2. Anyone who teaches a subject knows that subject.
3. Anyone who knows a subject can guide students.
4. Ravi is a teacher.
Prove that: Ravi guide students using resolution in predicate logic.
Sol   Conversion into clause form – 4 marks
Proof – 6 marks
********** 6 **********
--- page 7 ---
Convert to CNF
Q5   a   Consider a map divided into five regions: A, B, C, D, and E. The goal is to color   [10]
CO- 3   each region using the colors Red, Green, Blue, and Yellow such that no two
SO- 1   adjacent regions have the same color.
BL- 4   The adjacency relationships between the regions are as follows:
• Region A is adjacent to B, C, and D
• Region B is adjacent to A, C, and E
• Region C is adjacent to A, B, D, and E
• Region D is adjacent to A and C
********** 7 **********
--- page 8 ---
• Region E is adjacent to B and C
i.   Represent the problem as a Constraint Satisfaction Problem (CSP) by
specifying the variables, domains, and constraints with the help of the
diagram.
ii.   Determine a valid coloring of the map such that no two neighboring
regions share the same colour. Start Region A color with RED.
Sol   Representation – 6 marks
Solution – 4 marks
Domain
Constraint
Region   Color
A   Red
B   Green
C   Blue
D   Green
E   Red
Q5   b   Explain the Wumpus World Problem in Artificial Intelligence. Formulate this   [10]
CO- 3   problem as Constraint satisfaction problem.
SO- 1
BL-3
Sol   The Wumpus World is a well-known knowledge-based environment used in
Artificial Intelligence to demonstrate logical reasoning and intelligent agents.
It consists of a grid-based cave where an agent must find gold while avoiding
dangers.
Environment Components
1. Agent – The explorer searching for gold.
2. Wumpus – A dangerous creature that kills the agent if encountered.
3. Pits – Holes in the ground that trap the agent.
Gold – The goal that the agent must find.
********** 8 **********
--- page 9 ---
Q6   a   Apply the concept of decision tree to identify Gini Index for each of the attribute   [10]
CO- 4   where final outcome is “Play Football”
SO- 6   Day   Weather   Temperature Wind   Play Football
BL-4   1   Sunny   Hot   Weak   No
2   Sunny   Hot   Strong   No
3   Cloudy   Hot   Weak   Yes
4   Rainy   Mild   Weak   Yes
5   Rainy   Cool   Weak   Yes
6   Rainy   Cool   Strong   No
7   Cloudy   Mild   Strong   Yes
8   Sunny   Cool   Weak   Yes
Sol   Solution
Calculate Gini for Attribute Weather
********** 9 **********
--- page 10 ---
Attribute   Weighted Gini
Weather   0.334
Temperature   0.334
Wind   0.367
Q6   b   Eight geographical locations are represented by coordinates:   [10]
CO- 4   Point   X Y
SO- 6   A   1   4
BL-4   B   1   3
C   2   2
D   6   8
E   7   7
F   8   6
G   3   4
H   4   5
Apply K-Means clustering with K = 3 till 2 iteration. Use Manhattan distance as
distance metric, where Initial centroids are C1 = A (1,4), C2 = D (6,8), C3 = H
(4,5)
Sol   Iteration 1
Distance Table
Point C1   C2   C3   Cluster
A   0   9   4   C1
B   1   10   5   C1
C   3   10   5   C1
D   9   0   5   C2
E   9   2   5   C2
F   9   4   5   C2
G   2   7   2   C3
H   4   5   0   C3
Clusters
Cluster   Points
C1   A, B, C
C2   D, E, F
C3   G, H
New Centroids C1 = (1.33 , 3) C2 = (7 , 7) C3 = (3.5 , 4.5)
Iteration 2
Distance Table
Point   C1 (1.33,3)   C2 (7,7)   C3 (3.5,4.5)   Cluster
A   1.67   9   3   C1
B   0.33   10   4   C1
C   1.67   10   4   C1
D   9.67   2   6   C2
E   9.67   0   6   C2
********** 10 **********
--- page 11 ---
F   9.67   2   6   C2
G   2.67   7   1   C3
H   4.67   5   1   C3
New Centroids C1 = (1.33 , 3) C2 = (7 , 7) C3 = (3.5 , 4.5)
Q7   a What is Skolemization. Explain it with an examples.   [05]
CO- 3
SO- 1
BL- 2
Sol   What is Skolemization – 1 mark
Example – 2 marks for each variant
Q7   b   Define Supervised Learning. Differentiate between classification and regression   [05]
CO- 4   problems with examples.
SO- 1
BL- 3
Sol   Supervised Learning is a type of machine learning in which a model is trained
using labeled data, meaning that the input data is paired with the correct output.
The algorithm learns the relationship between inputs and outputs so that it can
predict the output for new unseen data.
Key Characteristics
• Uses labeled training data.
• Requires input–output pairs.
• The model learns a mapping function from input to output.
• Used for prediction and classification tasks.
Types of Supervised Learning
1. Classification
o Used when the output variable is categorical.
o Example: Email Spam or Not Spam.
2. Regression
o Used when the output variable is continuous.
o Example: Predicting house prices.
Q7   c   Define an Expert System. Explain its model, characteristics, and architecture in   [10]
CO- 3   detail.
SO- 1
BL-2
Sol   1. Definition of Expert System
An Expert System is a computer program that uses artificial intelligence
techniques to simulate the decision-making ability of a human expert in a
specific domain. It uses a knowledge base and inference engine to solve
complex problems that normally require human expertise.
Expert systems are widely used in areas such as medicine, finance, engineering,
and troubleshooting systems.
2. Model of an Expert System
The model of an expert system consists of the following components:
1. Knowledge Base
•   Stores domain-specific knowledge.
• Contains facts and rules.
• Knowledge is usually represented in the form of IF–THEN rules.
********** 11 **********
--- page 12 ---
Example:
IF fever AND cough
THEN possible disease = Flu
2. Inference Engine
• The reasoning mechanism of the system.
• Applies logical rules to the knowledge base to derive conclusions.
• Uses techniques such as:
o Forward Chaining
o Backward Chaining
3. User Interface
• Allows interaction between the user and the expert system.
• Users can input queries and receive advice or solutions.
4. Explanation System
• Explains the reasoning process of the system.
• Helps users understand why a particular decision was made.
3. Characteristics of Expert Systems
Expert systems possess several important characteristics:
1. High Performance
• Provides solutions comparable to those of human experts.
2. Reliability
• Produces consistent and dependable results.
3. Explanation Capability
• Can explain reasoning steps and conclusions.
4. Domain Specificity
• Designed to solve problems in a specific domain.
5. Knowledge-Driven
• Performance depends on the quality of the knowledge base.
6. Symbolic Reasoning
• Uses logical reasoning instead of numerical computation.
4. Architecture of Expert System
The architecture of an expert system typically includes the following
components:
1. Knowledge Base
2. Inference Engine
3. Working Memory
4. User Interface
5. Explanation Facility
6. Knowledge Acquisition System
Working Memory
•   Stores temporary facts and data during the reasoning process.
Knowledge Acquisition System
• Helps experts and developers input knowledge into the system.
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 8a661a01bd6f

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_Computer_7002/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: mixed (20 pages), mean OCR confidence 80.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   State the differences between Greedy Best First Search and A* Search
strategies with examples.
Solution –
CO-2 ;
SO-   [5]
1,2,6,7 ;
BL-2
Marking Scheme –
Each point – 1 mark
b.   Consider the following knowledge base:
1. If a person studies hard, then the person passes the exam.
CO-3 ;
2. If a person passes the exam, then the person gets a job.
SO-   3. Ram studies hard.   [5]
1,6,7 ;
BL-2
Using forward chaining inference, determine whether Ram gets a job.
Show the sequence of inferences made.
********** 1 **********
--- page 2 ---
Solution –
Step 1: Known fact
• From (3): studies_hard(Ram) is true.
Step 2: Apply Rule 1
• Rule 1: If a person studies hard, then the person passes the
exam.
• Antecedent: studies_hard(Ram) → satisfied.
•   Therefore, passes_exam(Ram) can be inferred.
Step 3: Apply Rule 2
• Rule 2: If a person passes the exam, then the person gets a job.
• Antecedent: passes_exam(Ram) → satisfied.
•   Therefore, gets_job(Ram) can be inferred.
By forward chaining, we infer that Ram gets a job.
c.   Solve the following Cryptarithmatic –
SEND + MORE = MONEY
Solution –
S = 9
E = 5
CO-3 ;   N = 6
SO-   D = 7   [5]
1,6,7 ;   M = 1
BL-3   O = 0
R = 8
Y = 2
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
d.   Cluster these points into K = 2 clusters –
CO-4 ;
SO-   Data = [2, 3, 6, 8, 10, 12]
[5]
1,5,6,7 ;   Assume the initial centroids are C₁ = 4 and C₂ = 9.
BL-3
Solution –
********** 2 **********
--- page 3 ---
Cluster assignment after Iteration 1:
•   Cluster 1 (C₁): [2, 3, 6]
•   Cluster 2 (C₂): [8, 10, 12]
Update centroids
Compute the mean of each cluster:
• C₁_new = (2 + 3 + 6)/3 = 11/3 ≈ 3.67
• C₂_new = (8 + 10 + 12)/3 = 30/3 = 10
Cluster assignment unchanged:
•   Cluster 1 (C₁): [2, 3, 6]
•   Cluster 2 (C₂): [8, 10, 12]
Centroids update again:
• C₁_new = (2+3+6)/3 ≈ 3.67 (same as previous)
• C₂_new = (8+10+12)/3 = 10 (same as previous)
Since centroids did not change, the algorithm converges.
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
a. Explain the architecture of a Goal-based Agent with neat diagram.
Clearly describe the roles of its components.
Q2   Solution –
CO-1, 1,   • Knowing about the current state of the environment is not always
2; SO-   enough to decide what to do (e.g. decision at a road junction)
1,2,   • The agent needs some sort of goal information that describes [10+5+5]
5,6,7;   situations that are desirable
BL-2, 3,   • The agent program can combine this with information about the
2   results of possible actions in order to choose actions that achieve
the goal
•   Usually requires search and planning
********** 3 **********
--- page 4 ---
Sensors
• Role: Detect and perceive the current state of the environment.
• Example: Cameras, temperature sensors, RFID scanners, motion
detectors.
Percept Sequence
• Role: Keeps a history of all percepts the agent has received. This
helps the agent understand how the environment is changing over
time.
• Example: A smart thermostat recording temperature changes over
hours.
Model of the World / State Representation
• Role: Represents the current state of the environment and predicts
the effects of possible actions.
• Example: A self-driving car maintaining a map of the road and
positions of other vehicles.
Goal Generator
• Role: Specifies the desired outcomes or objectives that the agent
wants to achieve.
• Example: “Reach destination safely” for a self-driving car or
“minimize food wastage” for a smart refrigerator.
Decision / Reasoning Module
• Role: Evaluates possible actions and selects the one that best
achieves the goal, often by planning or searching future states.
• Example: Choosing whether to slow down, overtake, or stop in
traffic.
Actuators
• Role: Execute the chosen actions in the environment.
• Example: Steering wheel, brakes, accelerator for a car; controlling
fridge temperature or sending notifications for a smart
refrigerator.
Marking Scheme –
Diagram – 5 marks
Explanation – 5 marks
b. Define the PEAS properties and construct a complete PEAS
description for an ‘AI-based Smart Refrigerator’, clearly
explaining each component.
Solution –
********** 4 **********
--- page 5 ---
Marking Scheme –
Each Property – 1 mark
Discussion – 1 mark
c. Explain the roles of main steps of Genetic Algorithm (GA) and
discuss advantages and disadvantages of GA.
Solution –
Main steps of GA:
1. Initialization: Generate a random population of chromosomes.
2. Evaluation: Compute fitness of each chromosome.
3. Selection: Choose chromosomes for reproduction based on
fitness.
4. Crossover: Combine selected parents to create offspring.
5. Mutation: Introduce random changes in offspring to maintain
diversity.
6. Replacement: Form a new generation and repeat until
termination criteria.
Advantages:
• Works for complex, non-linear, and multi-modal problems.
• Does not require derivative information.
Limitations:
• May converge slowly.
• Needs careful tuning of parameters (mutation rate, population
size).
Marking Scheme –
Steps of GA – 3 marks
********** 5 **********
--- page 6 ---
Advantages – 1 mark
Disadvantages – 1 mark
a. Solve 8 tiles problem using Greedy Best First Search. Consider
the no. of misplaced tiles as the heuristic.
Solution –
Q3
CO-2, 2,
1; SO-   [5+10+5]
1,2,5,6,7;
BL-3, 3,
2
Marking Scheme –
Approach – 3 marks
Correct solution – 2 marks
b. Apply Alpha-Beta pruning algorithm to prune the game tree
shown below.
********** 6 **********
--- page 7 ---
Solution –
Marking Scheme –
Each Correct Prune – 2 marks
c. What are the different types of agents? Give one example for
each.
Solution –
Marking Scheme –
Each agent – 1 mark
********** 7 **********
--- page 8 ---
a. Consider the following facts and prove that Bob will receive a
bonus using Resolution Graph.
i. Any employee who completes a project successfully is
eligible for a bonus.
ii. Any employee who is eligible for a bonus and has
excellent performance receives a bonus.
iii. Bob completed a project successfully.
iv. Bob has excellent performance.
v. Any employee who receives a bonus is appreciated by
HR.
vi. Any employee who is appreciated by HR and meets
criteria gets promoted.
vii. Every employee who exceeds targets is eligible for a
bonus.
Solution –
Q4
CO-3, 3;   [15+5]
SO-1,6,7;
BL-3, 3
********** 8 **********
--- page 9 ---
Marking Scheme –
Conversion to FOL – 5 marks
Conversion to CNF – 5 marks
Resolution Graph – 5 marks
b. Color the countries with any one of 2 colors: {Red, Green, B}
such that no two neighboring countries share the same color,
also explain when backtracking is required in Map Coloring
problem.
Countries: [India, Pakistan, Nepal, Bangladesh, Bhutan, Myanmar]
Borders:
• India borders Pakistan, Nepal, Bangladesh, Bhutan, Myanmar
• Pakistan borders India
• Nepal borders India, Bhutan
• Bangladesh borders India, Myanmar
• Bhutan borders India, Nepal
• Myanmar borders India, Bangladesh
Solution –
Pakistan: neighbor of India → cannot be Red → choose Green
Nepal: neighbor of India → cannot be Red → choose Green
Bangladesh: neighbor of India → cannot be Red → choose Green
Bhutan: neighbor of India and Nepal → cannot be Red (India) or
Green (Nepal) → choose Blue
Myanmar: neighbor of India and Bangladesh → cannot be Red
(India) or Green (Bangladesh) → choose Blue
Backtracking is needed if a conflict occurs during assignment, i.e., no
available color left for a country:
• Example scenario:
********** 9 **********
--- page 10 ---
Suppose we initially colored Nepal → Green and Bangladesh →
Green (as above), and then we tried Bhutan → Green instead of
Blue:
o Bhutan neighbors: India (Red) → ok, Nepal (Green) →
conflict!
o No other color available? If we had only 2 colors, yes →
no valid choice → must backtrack.
•   Similarly, if Myanmar cannot pick a valid color because all
neighbors already have colors conflicting with its available
options → backtracking occurs.
Backtracking is required whenever a country cannot be assigned a
color without violating constraints, especially in densely connected
graphs with triangles.
In this problem, because neighbors of India also border each other
(Nepal–Bhutan, Bangladesh–Myanmar), bad early choices may force
backtracking.
Marking Scheme –
Colouring map – 3 marks
Explanation when backtracking required – 2 marks
a. Convert the following facts into FOL:
i. Anyone who rides any Harley is a rough character.
ii. Anyone who rides any BMW is a yuppie.
iii. Every yuppie is a lawyer.
iv. Any nice girl does not date anyone who is a rough character.
v. Mary is a nice girl, and John is a biker.
Solution –
Anyone who rides any Harley is a rough character.
∀ x ((∃ y (HARLEY(y) ∧ RIDES(x,y))) → ROUGH(x))
Q5
Anyone who rides any BMW is a yuppie.
CO-3, 3,   ∀ x ∀ y (RIDES(x,y) ∧ BMW(y) → YUPPIE(x))
4; SO-
[5+5+10]
1,5,6,7;   Every yuppie is a lawyer.
BL-3, 2,   ∀ x (YUPPIE(x) → LAWYER(x))
3
Any nice girl does not date anyone who is a rough character.
∀ x ∀ y (NICE(x) ∧ ROUGH(y) → ¬ DATE(x,y))
Mary is a nice girl, and John is a biker.
NICE(Mary) ∧ BIKER(John)
Marking Scheme –
Each FOL – 1 mark
c. Write down the rules to convert FOL into CNF.
Solution –
********** 10 **********
--- page 11 ---
Marking Scheme –
Each rule – 0.5 marks
Concept – 1 mark
c. Write down K-means Clustering Algorithm. A coffee shop wants to
segment customers based on amount spent per visit (in $) and number
of visits per week to design targeted offers. Group customers into 2
clusters, where initial cluster centres are (5, 1) and (15, 5).
********** 11 **********
--- page 12 ---
Customer Amount Spent ($) Visits per Week

a 5 1
c2 7 2
3 8 1
cA 15 5
cs 16 4
6 14 5
c7 3 1

Solution —

Step 1: Assign Customers to Nearest Cluster

Euclidean distance formula:
( — x)? + (y ~ Ye)?

Compute distances and assignments:

Customer To C1 (5,1) To C2 (15,5) Cluster Assigned
C1 (5,1) O v((5-15)*2 + (1-5)42) = ¥116 = a
10.77
C2 (7,2) V((7-5)42 + (2-1)42) = V5 = V((7-15)42 + (2-5)*2) = V73 = a
2.24 8.54
C3 (8,1) V((8-5)42 + (1-1)42) = V9 =3 V((8-15)*2 + (1-5)*2) = V65 = a
8.06
C4 (15,5) V((15-5)42 + (5-1)42) = V116 = t) c2
10.77
C5 (16,4) V((16-5)42 + (4-1)42) = V122 = V((16-15)42 + (4-5)*2) = V2 = c2
11.05 1.41
C6 (14,5) V((14-5)42 + (5-1)*2) = V97 = V((14-15)42 + (5-5)42) = V1 = c2
9.85 1
C7 (3,1) V((3-5)42 + (1-1)42) = V4 =2 ¥((3-15)*2 + (1-5)42) = ¥160 = a
12.65

Cluster assignment after first iteration:

e Cluster 1: Cl, C2, C3, C7
e Cluster 2: C4, C5, C6

Step 2: Compute New Cluster Centers

Cluster 1: Mean of (Amount Spent, Visits):

5+74+843 1424141
4 , 4

Clnew = ( ) = (5.75, 1.25)

Cluster 2: Mean of (Amount Spent, Visits):

15+16+14 54+4+5
3 , 3

C2nene — ( ) = (15, 4.67)

FRR ICR] DA KH
--- page 13 ---
Cluster assignments remain the same → Converged.
Step 4: Final Clusters
• Cluster 1 (C1): C1, C2, C3, C7 → Center (5.75, 1.25)
• Cluster 2 (C2): C4, C5, C6 → Center (15, 4.67)
Marking Scheme –
Algorithm – 3 marks
Correct approach – 2 marks
Iteration 1 – 2 marks
Iteration 2 – 2 marks
Iteration 3 – 1 mark
Q6
CO-4, 4;
SO-   [15+5]
1,5,6,7;
BL-3, 2
Using the dataset, build a decision tree to predict Return. You may use
any decision tree algorithm (ID3 or CART). Determine the root node and
subsequent splits based on your chosen method. Define Inductive
Learning and explain how it can be applied to this dataset. Generate IF–
THEN rules from your decision tree for predicting Return.
Solution –
********** 13 **********
--- page 14 ---
Entropy formula:

Entropy(S) = — S~ pi logo(pi)

e Total Yes = 5 (Applicants 1,2,3,6,8)
© Total No = 3 (Applicants 4,5,7)

5 5 3 3
Entropy(S) = -3 logs 378 logs 3

Step by step:

5 3
= = 0.625, = =0.375
8 8

Entropy(S) — —0.625 - log, (0.625) — 0.375 - log,(0.375)
log,(0.625) ~ —0.678, log,(0.375) = —1.415
Entropy(S) = —(0.625 - —0.678 + 0.375 - —1.415)

Entropy(S) = 0.423 + 0.531 = 0.954

A) CreditHistory
© Good: Applicants 1,2,8 - ApproveLoan = Yes, Yes, Yes — All Yes
=> Entropy — 0
e Fair: Applicants 3,6,7 + ApproveLoan = Yes, Yes, No — 2 Yes, 1 No

2 2 1 1
Entropy(Fair) = -3 logs 373 log 3

2 1
-3° (—0.585) — 37 (—1.585) = 0.389 + 0.528 = 0.918

¢ Poor: Applicants 4,5 — ApproveLoan = No, No = All No = Entropy = 0
Weighted Entropy:

E(CreditHistory) = : -O+ ; - 0.918 + ; -0 = 0.344

Gain(CreditHistory) = 0.954 — 0.344 = 0.610

B) Income
¢ High: Applicants 1,2,3 - ApproveLoan = Yes, Yes, Yes ~ Entropy = 0
¢ Medium: Applicants 4,6,8 —- ApproveLoan = No, Yes, Yes > 2 Yes, 1 No — Entropy = 0.918
© Low: Applicants 5,7 — ApproveLoan = No, No — Entropy = 0

Weighted Entropy:

2
E(Income) = ; 04 : 0.918 + 5-0 = 0.344

Gain(Income) = 0.954 — 0.344 = 0.610

FRR IC 7 I OH
--- page 15 ---
Highest gain = CreditHistory (0.610) or Income (0.610) → choose
CreditHistory as root.
Good: Applicants 1,2,8 → All Yes → Leaf Node: ApproveLoan =
Yes
Poor: Applicants 4,5 → All No → Leaf Node: ApproveLoan = No
Fair: Applicants 3,6,7 → Mix (Yes, Yes, No) → Need further
splitting
Entropy of this subset ≈ 0.918 (as calculated earlier)
Check Information Gain for remaining attributes:
• Income: High → Yes (Entropy=0)
Medium → Yes (Entropy=0)
Low → No (Entropy=0)
Weighted Entropy: E(Income)=0E(Income) = 0E(Income)=0 → Gain =
0.918 → best split = Income
High: Applicant 3 → Yes → Leaf: Yes
Medium: Applicant 6 → Yes → Leaf: Yes
Low: Applicant 7 → No → Leaf: No
********** 15 **********
--- page 16 ---
Marking Scheme –
Approach – 10 marks
Correct Tree – 5 marks
b. Explain the components of a Rule-Based Expert System and illustrate
its working with a neat diagram.
Solution –
A typical RBES has five main components:
A) Knowledge Base
•   Stores domain-specific knowledge as facts and rules.
•   Facts: Statements about the problem (e.g., “Patient has fever”)
• Rules: IF–THEN statements (e.g., “IF fever AND headache
THEN disease = Flu”)
B) Inference Engine
• The “brain” of the system.
• Applies reasoning techniques to deduce new facts or make
decisions.
• Two main reasoning methods:
o Forward chaining: Starts with facts → applies rules →
deduces conclusions.
o Backward chaining: Starts with goal → searches for
rules → verifies facts.
C) Working Memory (Fact Base)
• Temporary storage for current facts of the problem.
• Updated as the inference engine applies rules.
• Example: “Patient has high fever” is stored here.
D) User Interface
• Enables interaction between user and system.
• Users can input facts and get solutions.
• Example: A doctor enters symptoms, system outputs possible
disease.
E) Explanation Facility
• Explains why a conclusion was reached or which rules were
applied.
• Helps build trust in the system.
• Example: “Patient has fever and headache → Flu diagnosed.”
Working of Rule-Based Expert System
Step-by-step process:
1. User inputs facts → Stored in working memory
2. Inference engine checks rules in the knowledge base.
3. Matches rules whose conditions satisfy the facts.
4. Applies the rule → Deduces new facts or decision.
5. Updates working memory.
6. Provides conclusion to user via the interface.
7. Explanation facility can explain reasoning steps.
********** 16 **********
--- page 17 ---
Marking Scheme –
Diagram – 3 marks
Explanation – 2 marks
a. A dataset contains information about 120 students of a university.
The attributes are:
• Age (numeric)
• GPA (numeric, 0–10)
• Study Hours per Week (numeric)
• Scholarship Status (Yes, No)
i) Explain how you would use a classification algorithm to predict
whether a new student will receive a scholarship, given the other
attributes. Mention the steps and a suitable algorithm.
Q7   ii) Explain how you would use a clustering algorithm to segment the
students into groups based on their academic performance (GPA and
CO-4, 3,   Study Hours). Describe the steps and a suitable algorithm.
4, 4; SO-   [5+5+5+5
1,5,6,7;   Solution –   ]
BL-4, 3,
2, 4   To predict whether a new student will receive a scholarship based on
attributes like Age, GPA, and Study Hours per Week, a classification
algorithm such as a decision tree can be used. First, the dataset of 120
students is preprocessed to handle any missing values, and numeric
attributes may be scaled if necessary. The dataset is then divided into
training and testing sets, typically in an 80:20 ratio. Using the training
data, a decision tree is built by selecting at each node the attribute that
best splits the data, using criteria like Information Gain or Gini Index.
For numeric attributes like GPA or Study Hours, appropriate threshold
values are determined to create splits. The resulting tree produces IF–
THEN rules, for example, “IF GPA > 8 AND Study Hours > 20 THEN
Scholarship = Yes,” which makes the model interpretable. After
evaluating the model on the test set to check its accuracy, it can be used
to predict the scholarship status of a new student by following the tree
********** 17 **********
--- page 18 ---
from the root to the appropriate leaf node based on the student’s attribute
values. This approach is advantageous because it handles numeric data
effectively and provides a clear reasoning path for decisions, which is
useful for university administration.
To segment the students into groups based on their academic performance
using clustering, we can apply an unsupervised learning algorithm
such as K-Means clustering. In this approach, the attributes GPA and
Study Hours per Week are used as input features, while Age and
Scholarship Status are ignored since clustering is based solely on
performance. First, the dataset should be preprocessed by handling any
missing values and scaling the numeric attributes if they have different
ranges, to ensure fair distance calculations. Next, a suitable number of
clusters, say k = 3 (e.g., low, medium, and high performers), is chosen,
and k initial cluster centroids are selected randomly. Each student is
then assigned to the nearest cluster centroid based on a distance measure
such as Euclidean distance. After all students are assigned, the centroids
are recalculated as the mean GPA and Study Hours of the students in each
cluster. This process of assignment and centroid recalculation is repeated
iteratively until the clusters stabilize and no further changes occur. The
final clusters represent groups of students with similar academic
performance, which can help the university identify high achievers,
average performers, and students who may need additional support.
Marking Scheme –
Classification – 2.5 marks
Clustering – 2.5 marks
b. Solve the N-Queens problem for N = 4 using backtracking. Show the
stepwise placement of queens and indicate where backtracking occurs.
Solution –
Goal: Place 4 queens on a 4×4 board so that no two queens attack each
other.
Steps:
1. Row 1: Place Q1 at column 1 → Safe
2. Row 2:
o Column 1 → Unsafe (same column)
o Column 2 → Unsafe (diagonal conflict)
o Column 3 → Safe → Place Q2 at (2,3)
3. Row 3:
o All columns unsafe → Backtrack: Remove Q2 from
(2,3)
4. Row 2 (Retry):
o Column 4 → Safe → Place Q2 at (2,4)
5. Row 3:
o Column 1 → Safe → Place Q3 at (3,1)
6. Row 4:
o Column 3 → Safe → Place Q4 at (4,3) → Solution 1
found
7. Second Solution: Explore alternative placements for Q1 and Q2
to find another arrangement.
********** 18 **********
--- page 19 ---
Backtracking occurs whenever no safe column is found in a row (Row
3 after first Q2 placement).
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
c. What is an expert system? Write its advantages and disadvantages.
Solution –
An expert system is a computer program that is designed to solve
complex problems and to provide decision-making ability like a human
expert. It performs this by extracting knowledge from its knowledge base
using the reasoning and inference rules according to the user queries.
Advantages of Expert System
o These systems are highly reproducible.
o They can be used for risky places where the human presence is
not safe.
o Error possibilities are less if the KB contains correct knowledge.
o The performance of these systems remains steady as it is not
affected by emotions, tension, or fatigue.
o They provide a very high speed to respond to a particular query.
Limitations of Expert System
o The response of the expert system may get wrong if the knowledge
base contains the wrong information.
o Like a human being, it cannot produce a creative output for
different scenarios.
o   Its maintenance and development costs are very high.
o Knowledge acquisition for designing is much difficult.
o For each domain, we require a specific ES, which is one of the big
limitations.
o   It cannot learn from itself and hence requires manual updates.
Marking Scheme –
Definition – 1 mark
Advantages – 2 marks
d. A travel clinic wants to develop an expert system to advise travellers
about possible illnesses based on their symptoms. The system should
suggest a likely disease and recommend precautions.
Diseases: Dengue, Typhoid, and Food Poisoning
Symptoms:
• Fever (High, Low)
• Nausea (Yes, No)
• Stomach Pain (Yes, No)
• Headache (Yes, No)
i) Design a simple rule-based expert system with at least 5 IF–THEN
rules to diagnose the above diseases.
********** 19 **********
--- page 20 ---
ii) Explain how the expert system would infer a diagnosis when a
new traveller provides their symptoms.
Solution –
i) Rule-Based Expert System Design
Diseases: Dengue, Typhoid, Food Poisoning
Symptoms: Fever, Nausea, Stomach Pain, Headache
Knowledge Base (IF–THEN Rules)
1. Rule 1: IF Fever = High AND Headache = Yes AND Nausea =
Yes THEN Disease = Dengue AND Precaution = “Rest,
Hydration, Visit doctor”
2. Rule 2: IF Fever = High AND Stomach Pain = Yes AND Nausea
= Yes THEN Disease = Typhoid AND Precaution = “Avoid
contaminated food/water, Visit doctor”
3. Rule 3: IF Fever = Low AND Stomach Pain = Yes AND Nausea
= Yes THEN Disease = Food Poisoning AND Precaution =
“Drink fluids, Eat light diet”
4. Rule 4: IF Fever = High AND Headache = Yes AND Stomach
Pain = No THEN Disease = Dengue AND Precaution = “Rest,
Hydration, Monitor symptoms”
5. Rule 5: IF Fever = Low AND Nausea = Yes AND Stomach Pain
= No THEN Disease = Food Poisoning AND Precaution =
“Hydration, Avoid oily food”
ii) Inference Process (How the Expert System Works)
1. Input Symptoms: A traveller enters their symptoms, e.g., Fever
= High, Nausea = Yes, Stomach Pain = No, Headache = Yes.
2. Working Memory: The system stores these symptoms as facts.
3. Rule Matching: The inference engine checks each IF–THEN
rule to see which rule conditions match the traveller’s symptoms.
o In this example, Rule 4 matches.
4. Apply Rule: The system infers that the likely disease is Dengue.
5. Provide Recommendation: The system outputs the
precaution/advice associated with the rule: “Rest, Hydration,
Monitor symptoms.”
6. Explanation (Optional): The system can explain the reasoning:
“Since Fever is High, Headache is present, and Stomach Pain is
absent, Dengue is suggested.”
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 09bbabf2a2ec

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_Computer_7047/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: mixed (20 pages), mean OCR confidence 80.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   State the differences between Greedy Best First Search and A* Search
strategies with examples.
Solution –
CO-2 ;
SO-   [5]
1,2,6,7 ;
BL-2
Marking Scheme –
Each point – 1 mark
b.   Consider the following knowledge base:
1. If a person studies hard, then the person passes the exam.
CO-3 ;
2. If a person passes the exam, then the person gets a job.
SO-   3. Ram studies hard.   [5]
1,6,7 ;
BL-2
Using forward chaining inference, determine whether Ram gets a job.
Show the sequence of inferences made.
********** 1 **********
--- page 2 ---
Solution –
Step 1: Known fact
• From (3): studies_hard(Ram) is true.
Step 2: Apply Rule 1
• Rule 1: If a person studies hard, then the person passes the
exam.
• Antecedent: studies_hard(Ram) → satisfied.
•   Therefore, passes_exam(Ram) can be inferred.
Step 3: Apply Rule 2
• Rule 2: If a person passes the exam, then the person gets a job.
• Antecedent: passes_exam(Ram) → satisfied.
•   Therefore, gets_job(Ram) can be inferred.
By forward chaining, we infer that Ram gets a job.
c.   Solve the following Cryptarithmatic –
SEND + MORE = MONEY
Solution –
S = 9
E = 5
CO-3 ;   N = 6
SO-   D = 7   [5]
1,6,7 ;   M = 1
BL-3   O = 0
R = 8
Y = 2
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
d.   Cluster these points into K = 2 clusters –
CO-4 ;
SO-   Data = [2, 3, 6, 8, 10, 12]
[5]
1,5,6,7 ;   Assume the initial centroids are C₁ = 4 and C₂ = 9.
BL-3
Solution –
********** 2 **********
--- page 3 ---
Cluster assignment after Iteration 1:
•   Cluster 1 (C₁): [2, 3, 6]
•   Cluster 2 (C₂): [8, 10, 12]
Update centroids
Compute the mean of each cluster:
• C₁_new = (2 + 3 + 6)/3 = 11/3 ≈ 3.67
• C₂_new = (8 + 10 + 12)/3 = 30/3 = 10
Cluster assignment unchanged:
•   Cluster 1 (C₁): [2, 3, 6]
•   Cluster 2 (C₂): [8, 10, 12]
Centroids update again:
• C₁_new = (2+3+6)/3 ≈ 3.67 (same as previous)
• C₂_new = (8+10+12)/3 = 10 (same as previous)
Since centroids did not change, the algorithm converges.
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
a. Explain the architecture of a Goal-based Agent with neat diagram.
Clearly describe the roles of its components.
Q2   Solution –
CO-1, 1,   • Knowing about the current state of the environment is not always
2; SO-   enough to decide what to do (e.g. decision at a road junction)
1,2,   • The agent needs some sort of goal information that describes [10+5+5]
5,6,7;   situations that are desirable
BL-2, 3,   • The agent program can combine this with information about the
2   results of possible actions in order to choose actions that achieve
the goal
•   Usually requires search and planning
********** 3 **********
--- page 4 ---
Sensors
• Role: Detect and perceive the current state of the environment.
• Example: Cameras, temperature sensors, RFID scanners, motion
detectors.
Percept Sequence
• Role: Keeps a history of all percepts the agent has received. This
helps the agent understand how the environment is changing over
time.
• Example: A smart thermostat recording temperature changes over
hours.
Model of the World / State Representation
• Role: Represents the current state of the environment and predicts
the effects of possible actions.
• Example: A self-driving car maintaining a map of the road and
positions of other vehicles.
Goal Generator
• Role: Specifies the desired outcomes or objectives that the agent
wants to achieve.
• Example: “Reach destination safely” for a self-driving car or
“minimize food wastage” for a smart refrigerator.
Decision / Reasoning Module
• Role: Evaluates possible actions and selects the one that best
achieves the goal, often by planning or searching future states.
• Example: Choosing whether to slow down, overtake, or stop in
traffic.
Actuators
• Role: Execute the chosen actions in the environment.
• Example: Steering wheel, brakes, accelerator for a car; controlling
fridge temperature or sending notifications for a smart
refrigerator.
Marking Scheme –
Diagram – 5 marks
Explanation – 5 marks
b. Define the PEAS properties and construct a complete PEAS
description for an ‘AI-based Smart Refrigerator’, clearly
explaining each component.
Solution –
********** 4 **********
--- page 5 ---
Marking Scheme –
Each Property – 1 mark
Discussion – 1 mark
c. Explain the roles of main steps of Genetic Algorithm (GA) and
discuss advantages and disadvantages of GA.
Solution –
Main steps of GA:
1. Initialization: Generate a random population of chromosomes.
2. Evaluation: Compute fitness of each chromosome.
3. Selection: Choose chromosomes for reproduction based on
fitness.
4. Crossover: Combine selected parents to create offspring.
5. Mutation: Introduce random changes in offspring to maintain
diversity.
6. Replacement: Form a new generation and repeat until
termination criteria.
Advantages:
• Works for complex, non-linear, and multi-modal problems.
• Does not require derivative information.
Limitations:
• May converge slowly.
• Needs careful tuning of parameters (mutation rate, population
size).
Marking Scheme –
Steps of GA – 3 marks
********** 5 **********
--- page 6 ---
Advantages – 1 mark
Disadvantages – 1 mark
a. Solve 8 tiles problem using Greedy Best First Search. Consider
the no. of misplaced tiles as the heuristic.
Solution –
Q3
CO-2, 2,
1; SO-   [5+10+5]
1,2,5,6,7;
BL-3, 3,
2
Marking Scheme –
Approach – 3 marks
Correct solution – 2 marks
b. Apply Alpha-Beta pruning algorithm to prune the game tree
shown below.
********** 6 **********
--- page 7 ---
Solution –
Marking Scheme –
Each Correct Prune – 2 marks
c. What are the different types of agents? Give one example for
each.
Solution –
Marking Scheme –
Each agent – 1 mark
********** 7 **********
--- page 8 ---
a. Consider the following facts and prove that Bob will receive a
bonus using Resolution Graph.
i. Any employee who completes a project successfully is
eligible for a bonus.
ii. Any employee who is eligible for a bonus and has
excellent performance receives a bonus.
iii. Bob completed a project successfully.
iv. Bob has excellent performance.
v. Any employee who receives a bonus is appreciated by
HR.
vi. Any employee who is appreciated by HR and meets
criteria gets promoted.
vii. Every employee who exceeds targets is eligible for a
bonus.
Solution –
Q4
CO-3, 3;   [15+5]
SO-1,6,7;
BL-3, 3
********** 8 **********
--- page 9 ---
Marking Scheme –
Conversion to FOL – 5 marks
Conversion to CNF – 5 marks
Resolution Graph – 5 marks
b. Color the countries with any one of 2 colors: {Red, Green, B}
such that no two neighboring countries share the same color,
also explain when backtracking is required in Map Coloring
problem.
Countries: [India, Pakistan, Nepal, Bangladesh, Bhutan, Myanmar]
Borders:
• India borders Pakistan, Nepal, Bangladesh, Bhutan, Myanmar
• Pakistan borders India
• Nepal borders India, Bhutan
• Bangladesh borders India, Myanmar
• Bhutan borders India, Nepal
• Myanmar borders India, Bangladesh
Solution –
Pakistan: neighbor of India → cannot be Red → choose Green
Nepal: neighbor of India → cannot be Red → choose Green
Bangladesh: neighbor of India → cannot be Red → choose Green
Bhutan: neighbor of India and Nepal → cannot be Red (India) or
Green (Nepal) → choose Blue
Myanmar: neighbor of India and Bangladesh → cannot be Red
(India) or Green (Bangladesh) → choose Blue
Backtracking is needed if a conflict occurs during assignment, i.e., no
available color left for a country:
• Example scenario:
********** 9 **********
--- page 10 ---
Suppose we initially colored Nepal → Green and Bangladesh →
Green (as above), and then we tried Bhutan → Green instead of
Blue:
o Bhutan neighbors: India (Red) → ok, Nepal (Green) →
conflict!
o No other color available? If we had only 2 colors, yes →
no valid choice → must backtrack.
•   Similarly, if Myanmar cannot pick a valid color because all
neighbors already have colors conflicting with its available
options → backtracking occurs.
Backtracking is required whenever a country cannot be assigned a
color without violating constraints, especially in densely connected
graphs with triangles.
In this problem, because neighbors of India also border each other
(Nepal–Bhutan, Bangladesh–Myanmar), bad early choices may force
backtracking.
Marking Scheme –
Colouring map – 3 marks
Explanation when backtracking required – 2 marks
a. Convert the following facts into FOL:
i. Anyone who rides any Harley is a rough character.
ii. Anyone who rides any BMW is a yuppie.
iii. Every yuppie is a lawyer.
iv. Any nice girl does not date anyone who is a rough character.
v. Mary is a nice girl, and John is a biker.
Solution –
Anyone who rides any Harley is a rough character.
∀ x ((∃ y (HARLEY(y) ∧ RIDES(x,y))) → ROUGH(x))
Q5
Anyone who rides any BMW is a yuppie.
CO-3, 3,   ∀ x ∀ y (RIDES(x,y) ∧ BMW(y) → YUPPIE(x))
4; SO-
[5+5+10]
1,5,6,7;   Every yuppie is a lawyer.
BL-3, 2,   ∀ x (YUPPIE(x) → LAWYER(x))
3
Any nice girl does not date anyone who is a rough character.
∀ x ∀ y (NICE(x) ∧ ROUGH(y) → ¬ DATE(x,y))
Mary is a nice girl, and John is a biker.
NICE(Mary) ∧ BIKER(John)
Marking Scheme –
Each FOL – 1 mark
c. Write down the rules to convert FOL into CNF.
Solution –
********** 10 **********
--- page 11 ---
Marking Scheme –
Each rule – 0.5 marks
Concept – 1 mark
c. Write down K-means Clustering Algorithm. A coffee shop wants to
segment customers based on amount spent per visit (in $) and number
of visits per week to design targeted offers. Group customers into 2
clusters, where initial cluster centres are (5, 1) and (15, 5).
********** 11 **********
--- page 12 ---
Customer Amount Spent ($) Visits per Week

a 5 1
c2 7 2
3 8 1
cA 15 5
cs 16 4
6 14 5
c7 3 1

Solution —

Step 1: Assign Customers to Nearest Cluster

Euclidean distance formula:
( — x)? + (y ~ Ye)?

Compute distances and assignments:

Customer To C1 (5,1) To C2 (15,5) Cluster Assigned
C1 (5,1) O v((5-15)*2 + (1-5)42) = ¥116 = a
10.77
C2 (7,2) V((7-5)42 + (2-1)42) = V5 = V((7-15)42 + (2-5)*2) = V73 = a
2.24 8.54
C3 (8,1) V((8-5)42 + (1-1)42) = V9 =3 V((8-15)*2 + (1-5)*2) = V65 = a
8.06
C4 (15,5) V((15-5)42 + (5-1)42) = V116 = t) c2
10.77
C5 (16,4) V((16-5)42 + (4-1)42) = V122 = V((16-15)42 + (4-5)*2) = V2 = c2
11.05 1.41
C6 (14,5) V((14-5)42 + (5-1)*2) = V97 = V((14-15)42 + (5-5)42) = V1 = c2
9.85 1
C7 (3,1) V((3-5)42 + (1-1)42) = V4 =2 ¥((3-15)*2 + (1-5)42) = ¥160 = a
12.65

Cluster assignment after first iteration:

e Cluster 1: Cl, C2, C3, C7
e Cluster 2: C4, C5, C6

Step 2: Compute New Cluster Centers

Cluster 1: Mean of (Amount Spent, Visits):

5+74+843 1424141
4 , 4

Clnew = ( ) = (5.75, 1.25)

Cluster 2: Mean of (Amount Spent, Visits):

15+16+14 54+4+5
3 , 3

C2nene — ( ) = (15, 4.67)

FRR ICR] DA KH
--- page 13 ---
Cluster assignments remain the same → Converged.
Step 4: Final Clusters
• Cluster 1 (C1): C1, C2, C3, C7 → Center (5.75, 1.25)
• Cluster 2 (C2): C4, C5, C6 → Center (15, 4.67)
Marking Scheme –
Algorithm – 3 marks
Correct approach – 2 marks
Iteration 1 – 2 marks
Iteration 2 – 2 marks
Iteration 3 – 1 mark
Q6
CO-4, 4;
SO-   [15+5]
1,5,6,7;
BL-3, 2
Using the dataset, build a decision tree to predict Return. You may use
any decision tree algorithm (ID3 or CART). Determine the root node and
subsequent splits based on your chosen method. Define Inductive
Learning and explain how it can be applied to this dataset. Generate IF–
THEN rules from your decision tree for predicting Return.
Solution –
********** 13 **********
--- page 14 ---
Entropy formula:

Entropy(S) = — S~ pi logo(pi)

e Total Yes = 5 (Applicants 1,2,3,6,8)
© Total No = 3 (Applicants 4,5,7)

5 5 3 3
Entropy(S) = -3 logs 378 logs 3

Step by step:

5 3
= = 0.625, = =0.375
8 8

Entropy(S) — —0.625 - log, (0.625) — 0.375 - log,(0.375)
log,(0.625) ~ —0.678, log,(0.375) = —1.415
Entropy(S) = —(0.625 - —0.678 + 0.375 - —1.415)

Entropy(S) = 0.423 + 0.531 = 0.954

A) CreditHistory
© Good: Applicants 1,2,8 - ApproveLoan = Yes, Yes, Yes — All Yes
=> Entropy — 0
e Fair: Applicants 3,6,7 + ApproveLoan = Yes, Yes, No — 2 Yes, 1 No

2 2 1 1
Entropy(Fair) = -3 logs 373 log 3

2 1
-3° (—0.585) — 37 (—1.585) = 0.389 + 0.528 = 0.918

¢ Poor: Applicants 4,5 — ApproveLoan = No, No = All No = Entropy = 0
Weighted Entropy:

E(CreditHistory) = : -O+ ; - 0.918 + ; -0 = 0.344

Gain(CreditHistory) = 0.954 — 0.344 = 0.610

B) Income
¢ High: Applicants 1,2,3 - ApproveLoan = Yes, Yes, Yes ~ Entropy = 0
¢ Medium: Applicants 4,6,8 —- ApproveLoan = No, Yes, Yes > 2 Yes, 1 No — Entropy = 0.918
© Low: Applicants 5,7 — ApproveLoan = No, No — Entropy = 0

Weighted Entropy:

2
E(Income) = ; 04 : 0.918 + 5-0 = 0.344

Gain(Income) = 0.954 — 0.344 = 0.610

FRR IC 7 I OH
--- page 15 ---
Highest gain = CreditHistory (0.610) or Income (0.610) → choose
CreditHistory as root.
Good: Applicants 1,2,8 → All Yes → Leaf Node: ApproveLoan =
Yes
Poor: Applicants 4,5 → All No → Leaf Node: ApproveLoan = No
Fair: Applicants 3,6,7 → Mix (Yes, Yes, No) → Need further
splitting
Entropy of this subset ≈ 0.918 (as calculated earlier)
Check Information Gain for remaining attributes:
• Income: High → Yes (Entropy=0)
Medium → Yes (Entropy=0)
Low → No (Entropy=0)
Weighted Entropy: E(Income)=0E(Income) = 0E(Income)=0 → Gain =
0.918 → best split = Income
High: Applicant 3 → Yes → Leaf: Yes
Medium: Applicant 6 → Yes → Leaf: Yes
Low: Applicant 7 → No → Leaf: No
********** 15 **********
--- page 16 ---
Marking Scheme –
Approach – 10 marks
Correct Tree – 5 marks
b. Explain the components of a Rule-Based Expert System and illustrate
its working with a neat diagram.
Solution –
A typical RBES has five main components:
A) Knowledge Base
•   Stores domain-specific knowledge as facts and rules.
•   Facts: Statements about the problem (e.g., “Patient has fever”)
• Rules: IF–THEN statements (e.g., “IF fever AND headache
THEN disease = Flu”)
B) Inference Engine
• The “brain” of the system.
• Applies reasoning techniques to deduce new facts or make
decisions.
• Two main reasoning methods:
o Forward chaining: Starts with facts → applies rules →
deduces conclusions.
o Backward chaining: Starts with goal → searches for
rules → verifies facts.
C) Working Memory (Fact Base)
• Temporary storage for current facts of the problem.
• Updated as the inference engine applies rules.
• Example: “Patient has high fever” is stored here.
D) User Interface
• Enables interaction between user and system.
• Users can input facts and get solutions.
• Example: A doctor enters symptoms, system outputs possible
disease.
E) Explanation Facility
• Explains why a conclusion was reached or which rules were
applied.
• Helps build trust in the system.
• Example: “Patient has fever and headache → Flu diagnosed.”
Working of Rule-Based Expert System
Step-by-step process:
1. User inputs facts → Stored in working memory
2. Inference engine checks rules in the knowledge base.
3. Matches rules whose conditions satisfy the facts.
4. Applies the rule → Deduces new facts or decision.
5. Updates working memory.
6. Provides conclusion to user via the interface.
7. Explanation facility can explain reasoning steps.
********** 16 **********
--- page 17 ---
Marking Scheme –
Diagram – 3 marks
Explanation – 2 marks
a. A dataset contains information about 120 students of a university.
The attributes are:
• Age (numeric)
• GPA (numeric, 0–10)
• Study Hours per Week (numeric)
• Scholarship Status (Yes, No)
i) Explain how you would use a classification algorithm to predict
whether a new student will receive a scholarship, given the other
attributes. Mention the steps and a suitable algorithm.
Q7   ii) Explain how you would use a clustering algorithm to segment the
students into groups based on their academic performance (GPA and
CO-4, 3,   Study Hours). Describe the steps and a suitable algorithm.
4, 4; SO-   [5+5+5+5
1,5,6,7;   Solution –   ]
BL-4, 3,
2, 4   To predict whether a new student will receive a scholarship based on
attributes like Age, GPA, and Study Hours per Week, a classification
algorithm such as a decision tree can be used. First, the dataset of 120
students is preprocessed to handle any missing values, and numeric
attributes may be scaled if necessary. The dataset is then divided into
training and testing sets, typically in an 80:20 ratio. Using the training
data, a decision tree is built by selecting at each node the attribute that
best splits the data, using criteria like Information Gain or Gini Index.
For numeric attributes like GPA or Study Hours, appropriate threshold
values are determined to create splits. The resulting tree produces IF–
THEN rules, for example, “IF GPA > 8 AND Study Hours > 20 THEN
Scholarship = Yes,” which makes the model interpretable. After
evaluating the model on the test set to check its accuracy, it can be used
to predict the scholarship status of a new student by following the tree
********** 17 **********
--- page 18 ---
from the root to the appropriate leaf node based on the student’s attribute
values. This approach is advantageous because it handles numeric data
effectively and provides a clear reasoning path for decisions, which is
useful for university administration.
To segment the students into groups based on their academic performance
using clustering, we can apply an unsupervised learning algorithm
such as K-Means clustering. In this approach, the attributes GPA and
Study Hours per Week are used as input features, while Age and
Scholarship Status are ignored since clustering is based solely on
performance. First, the dataset should be preprocessed by handling any
missing values and scaling the numeric attributes if they have different
ranges, to ensure fair distance calculations. Next, a suitable number of
clusters, say k = 3 (e.g., low, medium, and high performers), is chosen,
and k initial cluster centroids are selected randomly. Each student is
then assigned to the nearest cluster centroid based on a distance measure
such as Euclidean distance. After all students are assigned, the centroids
are recalculated as the mean GPA and Study Hours of the students in each
cluster. This process of assignment and centroid recalculation is repeated
iteratively until the clusters stabilize and no further changes occur. The
final clusters represent groups of students with similar academic
performance, which can help the university identify high achievers,
average performers, and students who may need additional support.
Marking Scheme –
Classification – 2.5 marks
Clustering – 2.5 marks
b. Solve the N-Queens problem for N = 4 using backtracking. Show the
stepwise placement of queens and indicate where backtracking occurs.
Solution –
Goal: Place 4 queens on a 4×4 board so that no two queens attack each
other.
Steps:
1. Row 1: Place Q1 at column 1 → Safe
2. Row 2:
o Column 1 → Unsafe (same column)
o Column 2 → Unsafe (diagonal conflict)
o Column 3 → Safe → Place Q2 at (2,3)
3. Row 3:
o All columns unsafe → Backtrack: Remove Q2 from
(2,3)
4. Row 2 (Retry):
o Column 4 → Safe → Place Q2 at (2,4)
5. Row 3:
o Column 1 → Safe → Place Q3 at (3,1)
6. Row 4:
o Column 3 → Safe → Place Q4 at (4,3) → Solution 1
found
7. Second Solution: Explore alternative placements for Q1 and Q2
to find another arrangement.
********** 18 **********
--- page 19 ---
Backtracking occurs whenever no safe column is found in a row (Row
3 after first Q2 placement).
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
c. What is an expert system? Write its advantages and disadvantages.
Solution –
An expert system is a computer program that is designed to solve
complex problems and to provide decision-making ability like a human
expert. It performs this by extracting knowledge from its knowledge base
using the reasoning and inference rules according to the user queries.
Advantages of Expert System
o These systems are highly reproducible.
o They can be used for risky places where the human presence is
not safe.
o Error possibilities are less if the KB contains correct knowledge.
o The performance of these systems remains steady as it is not
affected by emotions, tension, or fatigue.
o They provide a very high speed to respond to a particular query.
Limitations of Expert System
o The response of the expert system may get wrong if the knowledge
base contains the wrong information.
o Like a human being, it cannot produce a creative output for
different scenarios.
o   Its maintenance and development costs are very high.
o Knowledge acquisition for designing is much difficult.
o For each domain, we require a specific ES, which is one of the big
limitations.
o   It cannot learn from itself and hence requires manual updates.
Marking Scheme –
Definition – 1 mark
Advantages – 2 marks
d. A travel clinic wants to develop an expert system to advise travellers
about possible illnesses based on their symptoms. The system should
suggest a likely disease and recommend precautions.
Diseases: Dengue, Typhoid, and Food Poisoning
Symptoms:
• Fever (High, Low)
• Nausea (Yes, No)
• Stomach Pain (Yes, No)
• Headache (Yes, No)
i) Design a simple rule-based expert system with at least 5 IF–THEN
rules to diagnose the above diseases.
********** 19 **********
--- page 20 ---
ii) Explain how the expert system would infer a diagnosis when a
new traveller provides their symptoms.
Solution –
i) Rule-Based Expert System Design
Diseases: Dengue, Typhoid, Food Poisoning
Symptoms: Fever, Nausea, Stomach Pain, Headache
Knowledge Base (IF–THEN Rules)
1. Rule 1: IF Fever = High AND Headache = Yes AND Nausea =
Yes THEN Disease = Dengue AND Precaution = “Rest,
Hydration, Visit doctor”
2. Rule 2: IF Fever = High AND Stomach Pain = Yes AND Nausea
= Yes THEN Disease = Typhoid AND Precaution = “Avoid
contaminated food/water, Visit doctor”
3. Rule 3: IF Fever = Low AND Stomach Pain = Yes AND Nausea
= Yes THEN Disease = Food Poisoning AND Precaution =
“Drink fluids, Eat light diet”
4. Rule 4: IF Fever = High AND Headache = Yes AND Stomach
Pain = No THEN Disease = Dengue AND Precaution = “Rest,
Hydration, Monitor symptoms”
5. Rule 5: IF Fever = Low AND Nausea = Yes AND Stomach Pain
= No THEN Disease = Food Poisoning AND Precaution =
“Hydration, Avoid oily food”
ii) Inference Process (How the Expert System Works)
1. Input Symptoms: A traveller enters their symptoms, e.g., Fever
= High, Nausea = Yes, Stomach Pain = No, Headache = Yes.
2. Working Memory: The system stores these symptoms as facts.
3. Rule Matching: The inference engine checks each IF–THEN
rule to see which rule conditions match the traveller’s symptoms.
o In this example, Rule 4 matches.
4. Apply Rule: The system infers that the likely disease is Dengue.
5. Provide Recommendation: The system outputs the
precaution/advice associated with the rule: “Rest, Hydration,
Monitor symptoms.”
6. Explanation (Optional): The system can explain the reasoning:
“Since Fever is High, Headache is present, and Stomach Pain is
absent, Dengue is suggested.”
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 585e2f4ae6e8

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSBS_7036/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: mixed (21 pages), mean OCR confidence 61.2
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (CSBS)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 01 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Additional Instructions:
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   What are the differences between Blind Search and Heuristic Search
strategies? Explain with graphical examples.
Solution:
Blind Search   Heuristic Search
It   is   Uninformed   Search   It   is   Heuristic   Search
techniques   techniques.
Uses no domain-specific   Uses extra knowledge
knowledge beyond the   (heuristics) about the problem
CO-2 ;   problem definition (start and   to guide the search.
SO-   goal states).
[5]
1,2,6,7 ;   Does not know where the goal   Guided by heuristic
BL-2   lies; explores blindly.   information estimating the
closeness to the goal.
Generally less efficient—   More efficient, as it focuses on
explores more nodes before   promising paths first.
reaching the goal.
Time and space complexity   Time and space complexity
usually higher due to   usually lower, as fewer nodes
exhaustive search.   are expanded.
- Breadth-First Search (BFS)   - Greedy Best-First Search
- Depth-First Search (DFS)   - A* Search
- Uniform Cost Search   - Hill Climbing
********** 1 **********
--- page 2 ---
Marking Scheme -
Each point 1 mark
b.   Convert the following statements into FOL:
i. Every child loves every candy.
ii. Anyone who loves some candy is not a nutrition fanatic.
iii. Anyone who eats any pumpkin is a nutrition fanatic.
iv. Anyone who buys any pumpkin either carves it or eats it.
v. John buys a pumpkin.
Solution:
CO-3 ;
SO-   [5]
1,6,7 ;
BL-3
Marking Scheme –
Each statement – 1 Mark (Total 5 Marks)
c.   What are the main components of a CSP? Also Discuss real-world
applications of CSP.
Solution:
Component Description
Variables   The set of unknowns that need to be assigned values
(e.g., A, B, C).
CO-3 ;
SO-   Domains   The set of possible values that each variable can take   [5]
1,6,7 ;   (e.g., {1, 2, 3}).
BL-3   Constraints   Rules that restrict the values the variables can take (e.g.,
A ≠ B, A < C).
1. Scheduling Problems
• Example: University course timetabling, employee shift
scheduling, airline crew schedules.
o Variables → Courses or employees
o Domains → Time slots or shifts
********** 2 **********
--- page 3 ---
o Constraints → No overlapping, availability, resource
limits
2. Resource Allocation
• Example: Assigning machines to jobs in a factory, cloud
computing resource assignment.
o Variables → Jobs/tasks
o Domains → Available machines or servers
o Constraints → Machine capacity, deadlines,
dependencies
3. Planning and Robotics
• Example: Path planning for autonomous vehicles or robot
motion planning.
o Variables → Positions or actions
o Domains → Possible moves or time steps
o Constraints → Obstacles, maximum speed, collision
avoidance
4. Puzzles and Games
• Example: Sudoku, N-Queens, crosswords, crypt-arithmetic
puzzles.
o Variables → Cells, board positions, letters
o Domains → Numbers, colors, letters
o Constraints → Game rules or puzzle restrictions
5. Configuration Problems
• Example: Product configuration in e-commerce (like
configuring a PC or car).
o Variables → Components (CPU, RAM, wheels, color)
o Domains → Available options
o Constraints → Compatibility between components
6. Artificial Intelligence and Expert Systems
• Example: Natural language processing, diagnostic systems,
reasoning tasks.
o Variables → Possible interpretations, symptoms, or
hypotheses
o Domains → Allowed values or diagnoses
o Constraints → Logical consistency, medical rules, or
grammar rules
Marking Scheme –
Components – 2 Marks
Applications – 3 Marks
d.   What is the difference between an induction learning algorithm and an
analogy learning algorithm?
Solution:
Learning by Analogy   Learning by Induction
CO-4 ;   Algorithm   Algorithm
SO-   It is a process of learning a   [5]
1,5,6,7 ;   new concept or solution   Inductive learning is the
BL-2   system that tries to induce a
through the use of similar
general rule based on
known concepts or
observed instances.
solutions.
This system finds a common This system tries to infer an
substructure between the   association between specific
problem domain and one of   inputs and outputs.
********** 3 **********
--- page 4 ---
the analogous domains
stored in the learner’s
existing knowledge base.
This strategy requires more   This strategy requires less
inferencing by the learning   inferencing by the learning
system.   system.
Analogy method involves
Induction method involves
learning by inductive
learning by examples,
inference, deductive
experimentation,
inference, and systems
observation, and discovery.
existing knowledge.
Learning by analogy is also   Generally inductive learning
used by humans more   is frequently used by
frequently.   humans.
It is one of the types of   It is one of the types of
single-agent learning.   single-agent learning.
This form of learning is
This form of learning is less
more powerful than the
powerful.
others.
Example: The driving
technique of vehicles. If
anyone knows the driving   Example: Humans can say
procedure of a bike, then   the taste of sugar is sweet
that person will drive a car   because they have the
by using some sort of   knowledge about sweetness.
previous learning
procedures.
Marking Scheme –
Each differences – 1 Mark (Total 5 Marks)
a. What are the different types of Environments? Explain with
examples.
Solution:
Fully observable vs. partially observable
An environment is fully observable if an agent's sensors give it access
Q2   to the complete state of the environment at each point in time.
CO-1, 1,   Fully observable environments are convenient, because the agent need
2; SO-   not maintain any internal state to keep track of the world   [10+5
1,2,   An environment might be partially observable because of noisy and
5,6,7;   inaccurate sensors or because parts of the state are simply missing from +5]
BL-2, 3,   the sensor data
2   Examples: vacuum cleaner with local dirt sensor, taxi driver
Deterministic vs. stochastic
The environment is deterministic if the next state of the environment is
completely determined by the current state and the action executed by
the agent.
In principle, an agent need not worry about uncertainty in a fully
observable, deterministic environment
********** 4 **********
--- page 5 ---
If the environment is partially observable then it could appear to be
stochastic
Examples: Vacuum world is deterministic while taxi driver is not
If the environment is deterministic except for the actions of other
agents, then the environment is strategic
Episodic vs. sequential
In episodic environments, the agent's experience is divided into atomic
"episodes" (each episode consists of the agent perceiving and then
performing a single action), and the choice of action in each episode
depends only on the episode itself.
Examples: classification tasks
In sequential environments, the current decision could affect all future
decisions
Examples: chess and taxi driver
Static vs. dynamic
The environment is unchanged while an agent is deliberating.
Static environments are easy to deal with because the agent need not
keep looking at the world while it is deciding on the action or need it
worry about the passage of time
Dynamic environments continuously ask the agent what it wants to do
The environment is semi-dynamic if the environment itself does not
change with the passage of time but the agent's performance score does
Examples: taxi driving is dynamic, chess when played with a clock is
semi-dynamic, crossword puzzles are static
Discrete vs. continuous
A limited number of distinct, clearly defined states, percepts and
actions.
Examples: Chess has finite number of discrete states, and has discrete
set of percepts and actions. Taxi driving has continuous states, and
actions
Single agent vs. multiagent
An agent operating by itself in an environment is single agent
Examples: Crossword is a single agent while chess is two-agents
Question: Does an agent A have to treat an object B as an agent or can
it be treated as a stochastically behaving object
Whether B's behaviour is best described by as maximizing a
performance measure whose value depends on agent's A behaviour
Examples: chess is a competitive multiagent environment while taxi
driving is a partially cooperative multiagent environment
Marking Scheme –
Each Type with Example – 2 Marks (Total 10 Marks for any 5)
********** 5 **********
--- page 6 ---
b. Define the PEAS properties. PEAS of automated Traffic
Signaling system on roads.
Solution:
PEAS stands for:
• P – Performance Measure
• E – Environment
• A – Actuators
• S – Sensors
Performance Measure
•   Criteria to evaluate how well the agent performs
• Defines the goal or success
Example: accuracy, safety, efficiency
Environment
• The surroundings in which the agent operates
•   Includes all external conditions
Example: roads, vehicles, weather
Actuators
• Actions the agent can perform
• Means by which the agent affects the environment
Example: signals, alarms, controls
Sensors
• Used to perceive the environment
•   Collects input data
Example: cameras, detectors
Marking Scheme –
Each Property – 1 mark
Discussion – 1 mark
c. Explain how Genetic Algorithm can be used to solve Travelling
Salesman Problem with example.
Solution:
Travelling Salesman Problem (TSP)
The Travelling Salesman Problem is to:
• Find the shortest possible route
•   Visit each city exactly once
• Return to the starting city
********** 6 **********
--- page 7 ---
TSP is a combinatorial optimization problem.
For large cities, exact methods are slow.
Genetic Algorithm provides a near-optimal solution using:
• Evolution
•   Selection
• Crossover
• Mutation
Each solution (tour) is represented as a chromosome:
Example with 5 cities (A, B, C, D, E):
Chromosome: A → C → B → E → D → A
This represents one possible route.
Initial Population
Generate random routes:
P1: A B C D E
P2: A C E B D
P3: A D B C E
Fitness Function
Fitness = inverse of total distance
Fitness=1/Total Distance
Shorter route = Higher fitness
Selection
Select best routes (parents) based on fitness.
Example:
• Choose P2 and P3
Parent 1: A B C D E
Parent 2: A C E B D
Cut points → [ B C D ]
Child → _ B C D _
Fill from Parent 2 → A E
Final Child: A B C D E
Mutation
Swap two cities to maintain diversity:
Before: A B C D E
After : A D C B E
Replacement
• Replace worst solutions with new offspring
• Repeat process for multiple generations
********** 7 **********
--- page 8 ---
Stop when:
• Maximum generations reached OR
• No improvement in solution
Example path:
A → B → C → D → E → A Advantages of GA in TSP
• Handles large search space efficiently
• Avoids getting stuck in local minima
• Provides near-optimal solutions
•   Flexible and adaptable
Marking Scheme –
Discussion – 3 Marks
Example – 2 Marks
a. Apply A* Search and Greedy Best First Search on the following
Graph and justify the results.
Solution:
Q3
A* Final Path
CO-2, 2,   0 → 1 → 2 → 5   [10+1
1; SO-   Total Cost = 2 + 5 + 9 = 16
1,2,5,6,7;   Greedy Final Path   0]
BL-3, 3,   0 → 3 → 4 → 5
2   Total Cost = 6 + 10 + 6 = 22
A* finds the optimal path (cost = 16) because it considers both:
•   actual cost g(n)
•   heuristic h(n)
Greedy Best-First Search selects nodes only based on heuristic:
•   It reaches goal faster
• But gives a suboptimal path (cost = 22)
Marking Scheme –
A* Search – 4 Marks
GBFS – 4 Marks
********** 8 **********
--- page 9 ---
Justification – 2 Marks
b. Apply the steps of Alpha-Beta pruning to the following Tree and find
out the pruned nodes.
Show the values of α (alpha) and β (beta) at each step of the algorithm.
Identify and mark the branches that are pruned during the search.
Determine the final optimal value at the root node.
Solution:
Marking Scheme –
Each subtree pruned - Each 1 Marks (Total 3 Marks)
Correct node Values – Each 0.5 Marks (Total 7 Marks)
b. Convert the following statements into FOL
c. Any employee who completes a project successfully is eligible
for a bonus.
d. Any employee who is eligible for a bonus and has excellent
Q4   performance receives a bonus.
e. Bob completed a project successfully.   [10+5
CO-3, 3;
f. Bob has excellent performance.
SO-1,6,7;   +5]
g. Any employee who receives a bonus is appreciated by HR.
BL-3, 3
h. Any employee who is appreciated by HR and meets criteria gets
promoted.
i. Every employee who exceeds targets is eligible for a bonus.
j. Bob exceeds targets.
********** 9 **********
--- page 10 ---
Prove ‘Bob receives Bonus’ using Resolution Graph.

Solution:

| Ww) Nk Combo Led Project (x) —> EXigibtals
| Rece v2 Bowral)
(3) Comblired Foohects ( Bob) 5 s

4) £ ne eile nk (Bed)

| \b ) Sa Rewivesbient,( Appreciated By
(6) ta (¢ HPpre cy ad 34 WROU) A Me ts Crvirie

Paomote4

—»>
eal eAyTangeky mathe



\3) Combo eA Frogec nt (Gob)

4) Excellent (Bob) :
by iRecewesBewalOV Mbbrectabed Ball

re ci AB WR (AD N | Meek? Cruel
a 7A Aypre ‘ou V Pripe ded (24)
(p iF

8) E ceeds Tryarr (Gob)

FIGS 7 (FI I IOK
--- page 11 ---
Marking Scheme –
Correct FOL statements – 0.5 Marks Each (Total 4 Marks)
Conversion into CNF – 3 Marks
Resolution Graph – 3 Marks
b. Write down the rules converting FOL in CNF.
********** 11 **********
--- page 12 ---
Marking Scheme –
Each rule – 0.5 marks
Concept – 1 mark
c. Solve following CSP using backtracking:
Variables: X, Y, Z
Domains: {1, 2, 3, 4}
Constraints: X < Y, Y ≠ Z, X + Z = 5
Find a valid assignment. Show using Tree.
Solution:
All valid solutions:
k. (X=1, Y=2, Z=4)
********** 12 **********
--- page 13 ---
l. (X=1, Y=3, Z=4)
m. (X=2, Y=4, Z=3)
n. (X=3, Y=4, Z=2)
Marking Scheme –
Valid Assignment – 2 Marks
Tree – 3 Marks
a. Explain the constraint satisfaction procedure to solve given crypt-
arithmetic problem.
C R O S S + R O A D S = D A N G E R
Solution:
Now let S = 3
S(3) + S(3) = R(6)
↓
Let D = 1
S(3) + D(1) = E(4)
↓
Let O = 2
A + O(2) = G
Q5   ↓
Let A = 5   [5+10
CO-3, 3;
A(5) + O(2) = G(7)
SO-1,6,7;   +5]
↓
BL-3, 3
R(6) + O(2) = N(8)
↓
Let C = 9
C(9) + R(6) = A(5)
∴ Solution is,
C = 9, R = 6, O = 2, S = 3, D = 1, A = 5, N = 8, G = 7, E = 4
Marking Scheme:
Each Correct Assignment – 0.5 Marks (Total 5 Marks)
b. Solve the constraint satisfaction problem to colour the regions of a
given map such that no 2 adjacent regions have the same colour. Given
three colours-(Red, Green, and Blue).
********** 13 **********
--- page 14 ---
Solution:
Variables and Constraints
• Variables (Regions): N, NW, NE, M, MW, ME, S, SE.
• Domain (Colours): {Red (R), Green (G), Blue (B), Yellow
(Y)}.
• Constraint: No two adjacent regions (sharing a border line) can
have the same color.
Adjacency List:
• N: NW, M, NE
• NW: N, M, MW
• NE: N, M, ME
• M: N, NW, NE, MW, ME
• MW: NW, M, S
• ME: NE, M, S
• S: MW, ME
• SE: (Island) No constraints/No neighbors.
Region   Color
Middle (M)   Red
North (N)   Green
North West (NW)   Blue
********** 14 **********
--- page 15 ---
North East (NE)   Blue
Middle West (MW) Green
Middle East (ME)   Yellow
South (S)   Red
South East (SE)   Red
Marking Scheme -
Constraints – 1 Marks
Approach – 1 Marks
Each Correct Assignment – 0.5 Marks (Total 8 Marks)
c. What is a goal-driven approach? What is a data-driven approach?
Explain with proper examples.
Solution:
Forward Chaining
Forward chaining is a data-driven approach.
It starts from known facts and applies rules to derive new facts until a
goal is reached.
Forward chaining is best when:
•   All or most data is available initially
• You want to discover all possible conclusions
• There may be multiple goals
• Used in monitoring or real-time systems
Example 1: Medical Diagnosis System
Facts:
• Fever
• Cough
Rules:
• IF Fever AND Cough → Flu
• IF Flu → Rest
Process:
•   Start with facts → Fever, Cough
• Apply rule → Flu
• Apply next rule → Rest
Here, we derive conclusions automatically from available data.
Backward Chaining
********** 15 **********
--- page 16 ---
Backward chaining is a goal-driven approach.
It starts with a goal and works backward to check if the facts support it.
Backward chaining is best when:
• There is a specific goal or query
• You want to verify a hypothesis
• The dataset is large but only some facts are relevant
• Used in diagnosis, query systems, theorem proving
Example 1: Disease Diagnosis
Goal: Check if patient has Flu
Rules:
• IF Fever AND Cough → Flu
Process:
• Goal: Flu
• Check rule → need Fever and Cough
• Ask: Does patient have Fever? TRUE
• Ask: Does patient have Cough? TRUE
Goal satisfied → Flu confirmed
Marking Scheme –
Data Driven Approach (Forward Chaining) – 2.5 Marks
Goal Driven Approach (Backward Chaining) – 2.5 Marks
a. Using the dataset, build a decision tree to predict Return. You may use
any decision tree algorithm (ID3 or CART). Determine the root node and
subsequent splits based on your chosen method. Define Inductive
Learning and explain how it can be applied to this dataset. Generate IF–
THEN rules from your decision tree for predicting Return.
Q6
CO-4;   [10+1
SO-
0]
1,5,6,7;
BL-3, 3
Solution:
********** 16 **********
--- page 17 ---
The target variable (Risk Category) has two classes: Low Risk and High Risk.
From the dataset:

e Low Risk = 3 occurrences

¢ High Risk = 3 occurrences

¢ Total samples = 6

The entropy formula:

H(S) = —py logs(p1) — p2loga(p2)
where p and po are the probabilities of Low Risk and High Risk, respectively.
3 3.3 3
A(S) = — | —log, — + - log, —
(S) ( g 082 § + G lees 7)
1 1 1 1
H(S) =- (5 logs 3 + 3 182 5)
A(S) = —(0.5 x -14+0.5 x -1)=1
So, Entropy before splitting = 1.
(a) Splitting by “Surgery Type”
© Minor (1) — (3 samples: Low Risk = 2, High Risk = 1)

e Major (2) — (3 samples: Low Risk = 1, High Risk = 2)

H (Minor) = — (5 logs 5 + je 5)

H(Minor) = — (0.667 x —0.585 + 0.333 x —1.585) = 0.918

H(Major) = — (5108. ; + ; logy ;)
H(Major) = 0.918
Weighted Entropy:
Hsurgery = - x 0.918 + = x 0.918 = 0.918

IG surgery = 1 — 0.918 = 0.082

FRR ICR] AC OH
--- page 18 ---
Since Information Gain (IG) is highest for "Pre-existing Conditions"
(IG = 1), we split first on "Pre-existing Conditions".
1. If Pre-existing Condition = No (0) → Low Risk
2. If Pre-existing Condition = Yes (1) → High Risk
This means "Pre-existing Conditions" is the best first split, and we
do not need further splits.
Marking Scheme –
Correct Calculation of Information Gain – 8 Marks
Drawing correct decision tree – 2 Marks
b. Explain the steps involved in developing an expert system.
Solution –
1. Identification
Determine the characteristics of the problem.
2. Conceptualization
Find the concept to produce the solution.
3. Formalization
********** 18 **********
--- page 19 ---
Design structures to organize the knowledge.
4. Implementation
Marking Scheme –
Diagram - 3 Marks
Explanation – 2 Marks
a. Apply K-means clustering (K = 2) on the following dataset:
(150,50), (155,52), (160,58), (165,62), (170,66), (175,70)
• Use Euclidean distance.
• Perform 2 iterations only.
Take the first two points (150, 50) and (155, 52) as the initial centroids.
Solution:
Given Data Points
(150,50), (155,52), (160,58), (165,62), (170,66), (175,70)
Initial Centroids
Q7
C1 = (150,50)
CO-4;   [10+1
SO-
C2 = (155,52)   0]
1,5,6,7;
BL-3, 3
Iteration 1
Distance to   Cluste
Point   Distance to C1
C2   r
(150,50)   0.00   5.39   C1
(155,52)   5.39   0.00   C2
(160,58)   11.66   6.71   C2
(165,62)   18.03   11.40   C2
(170,66)   24.49   16.40   C2
(175,70)   30.81   21.40   C2
Recalculate Centroids
C1 = Mean of points in C1 = (150,50)
C2 = Mean of points in C2 = ((155+160+165+170+175)/5 ,
(52+58+62+66+70)/5) = (165,61.6)
********** 19 **********
--- page 20 ---
Iteration 2
Point   Distance to C1 Distance to C2 Cluster
(150,50) 0.00   20.80   C1
(155,52) 5.39   11.04   C1
(160,58) 11.66   3.62   C2
(165,62) 18.03   0.45   C2
(170,66) 24.49   5.15   C2
(175,70) 30.81   11.28   C2
Update Centroids Again
C1 = Mean of points in C1 = ((150+155)/2 , (50+52)/2) = (152.5,51)
C2 = Mean of points in C2 = ((160+165+170+175)/4 ,
(58+62+66+70)/4) = (167.5,64)
Cluster   Points   Centroid
C1   (150,50), (155,52)   (152.5,51)
C2   (160,58), (165,62), (170,66), (175,70)   (167.5,64)
Marking Scheme –
Iteration 1 – 4 Marks
Iteration 2 – 4 Marks
Correct Clustering – 2 Marks
b. Design a rule-based expert system for diagnosing common cold vs flu
(include rules and inference process).
Solution:
A rule-based expert system uses:
• Facts (symptoms)
• IF–THEN rules
• Inference engine (forward/backward chaining)
to diagnose whether a patient has Common Cold or Flu.
Knowledge Base
Facts (Input Symptoms)
• Fever (High / Mild / None)
• Cough (Yes / No)
• Body ache (Yes / No)
•   Fatigue (Yes / No)
• Sneezing (Yes / No)
********** 20 **********
--- page 21 ---
• Headache (Yes / No)
Rules
Rules for Flu
• R1: IF Fever = High AND Body Ache = Yes → Flu
• R2: IF Fever = High AND Fatigue = Yes → Flu
• R3: IF Headache = Yes AND Body Ache = Yes → Flu
Rules for Common Cold
• R4: IF Sneezing = Yes AND Fever = Mild → Cold
• R5: IF Cough = Yes AND Sneezing = Yes → Cold
• R6: IF Fever = None AND Sneezing = Yes → Cold
Inference Process
Using Forward Chaining (Data-driven)
Step 1: Input Facts
Example:
• Fever = High
• Body Ache = Yes
•   Fatigue = Yes
Match Rules
• R1 matches → Flu
• R2 matches → Flu
Fire Rule
Conclusion: Patient has Flu
Marking Scheme –
Each Section – 2.5 Marks (Total 10 Marks)
********** 21 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 46e3b876428b

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7011/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C042)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: mixed (19 pages), mean OCR confidence 73.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
a.   A Genetic Algorithm is used to maximize the function
f(x) = x^2
where x is represented using 4-bit binary encoding.
Initial population is:
Chromosome Binary   Decimal x
C1   0101   5
C2   0011   3
C3   0110   6
C4   1001   9
a) Calculate the fitness of each chromosome.
CO- ;   b) Apply rank selection to choose two parents.
SO- ;   [5]
BL-
Ans 1(a) Fitness Calculation
f(x)=x2f(x) = x^2f(x)=x2
Chromosome x Fitness
C1   5 25
C2   3 9
C3   6 36
C4   9 81
(b) Rank Selection
Step 1: Rank chromosomes by fitness
********** 1 **********
--- page 2 ---
Rank Chromosome Fitness
1 (Best) C4   81
2   C3   36
3   C1   25
4   C2   9
Step 2: Assign selection probabilities
Higher rank → higher chance.
Selected Parents:
•   Parent 1: C4 (1001)
•   Parent 2: C3 (0110)
b.   Question from Unit 3
Compare Propositional Logic and First Order Logic with examples.
Propositional Logic
•   Basic unit is a proposition, which is a complete statement
•   Structure consists of atomic propositions combined using logical
connectives (AND, OR, NOT, IMPLIES)
• Does not support variables
• Does not support quantifiers
• Has limited expressiveness
• Domain of discourse is not required
• Cannot represent internal structure or relationships between objects
• Has limited inference power
• Used for simple logical reasoning
CO- ;
First Order Logic (FOL)   [5]
SO- ;
BL-
•   Basic unit is a predicate with variables
•   Structure consists of predicates applied to objects
•   Supports variables
•   Supports quantifiers such as:
o Universal quantifier (∀)
o   Existential quantifier (∃)
•   Is highly expressive
•   Requires a domain of discourse
• Can represent relationships between objects
• Has strong and flexible inference power
• Used for knowledge representation in Artificial Intelligence
Example 1: Propositional Logic
Statement:
“If it is raining, then the ground is wet.”
Let:
•   P: It is raining
********** 2 **********
--- page 3 ---
•   q: The ground is wet
Representation:
p→q
Works well for simple facts, but cannot specify who or what is
involved.
Example 2: Limitation of Propositional Logic
Statement:
“All humans are mortal.”
Cannot be expressed properly in propositional logic because it involves
all individuals.
Example 3: First Order Logic
Statement:
“All humans are mortal.”
Let:
Human(x): x is a human
M ortal(x): x is mortal
Representation:
∀x(Human(x)→Mortal(x))
FOL can represent general rules using quantifiers.
c.   Question from Unit 4
Solve using Cryptarithmetic:
CROSS
+ ROADS
-------
CO- ;
SO- ;   DANGER
BL-   Ans.c.
96233
+ 62513
-------
158746
d.   Question from Unit 5
• Provide at least two Real-world supervised learning use case.
• Provide three Real-world unsupervised learning use case
CO- ;
SO- ;   Ans.d. 5 (3+2) points from below should be fine
BL-
Assumptions of the K-means Clustering Algorithm
K-means works well only when certain assumptions hold:
• Number of clusters (K) is known in advance
The user must specify the value of K before running the algorithm.
********** 3 **********
--- page 4 ---
•   Clusters are spherical (globular) in shape
K-means assumes clusters are roughly circular and evenly spread
around their centroids.
•   Clusters are of similar size and density
It performs best when each cluster has approximately the same
number of data points and similar variance.
•   Distance metric is meaningful (usually Euclidean)
K-means relies on distance calculations, assuming Euclidean distance
accurately reflects similarity.
•   Features are numeric and continuous
Categorical or non-numeric data is not directly supported.
• Each data point belongs to exactly one cluster
No overlap between clusters is assumed.
Situations Where K-means May Fail
K-means may produce incorrect or misleading clusters in the
following cases:
•   Non-spherical or irregularly shaped clusters
For example, crescent-shaped or concentric clusters cannot be
correctly separated.
•   Clusters with different sizes or densities
Large or dense clusters dominate centroid movement, causing
smaller clusters to be misclassified.
• Presence of outliers or noise
Outliers significantly affect centroid positions, leading to poor
clustering.
•   Incorrect choice of K
Too small or too large K results in under-clustering or over-clustering.
•   Categorical or mixed-type data
K-means cannot handle non-numeric features without
transformation.
•   Different feature scales
Features with larger ranges dominate distance computation unless
normalization is applied.
• Poor initialization of centroids
Random initialization can lead to local minima and inconsistent
results.
A smart agriculture system uses sensors (soil, weather, crop health):
[15]
a.   • Model this as an agent system
•   Classify environment (observable, dynamic, stochastic, etc.)
• Propose suitable agent type (reactive/model-based/goal-based)
Q2
•   Justify design decisions
CO-; SO-;
BL-
Ans.a.
b.   A smart healthcare monitoring system can be modeled as an
[5]
intelligent agent that continuously perceives patient health conditions
and takes appropriate actions to ensure timely medical intervention.
********** 4 **********
--- page 5 ---
1. Modeling the System as an Intelligent Agent
•   Agent: Smart Healthcare Monitoring Agent
•   Sensors:
o Heart rate sensor
o Blood pressure sensor
o Oxygen saturation (SpO₂) sensor
o Body temperature sensor
•   Actuators:
o   Alert system (doctor/nurse notifications)
o Emergency response trigger (ambulance call)
o Medication reminder system
o   Hospital dashboard updates
Agent Function:
The agent maps sensor inputs to actions. For example, if oxygen level
drops below a threshold, the agent sends an alert to the doctor and
triggers emergency protocols. If vitals are stable, it continues
monitoring and logs data.
2. Classification of the Environment
•   Observability: Partially observable
Not all internal patient conditions (e.g., sudden internal
complications) are directly measurable through sensors.
•   Deterministic / Stochastic: Stochastic
Patient health conditions can change unpredictably due to biological
variations or external factors.
•   Episodic / Sequential: Sequential
Current health trends depend on past vitals and treatments, and
current actions influence future patient conditions.
•   Static / Dynamic: Dynamic
Patient vitals can change rapidly over time, even without agent
intervention.
•   Discrete / Continuous: Continuous
Vital signs such as heart rate and temperature vary continuously.
3. Suitable Agent Type
A model-based, goal-oriented agent is most suitable for this system.
• Model-based:
Maintains an internal model of patient health history and trends.
•   Goal-based:
Aims to maintain patient vitals within safe limits and prevent medical
emergencies.
4. Justification of Design Decisions
A reactive agent would only respond to immediate sensor readings,
which may lead to delayed or incorrect decisions. A model-based agent
allows the system to analyze historical health data to detect gradual
********** 5 **********
--- page 6 ---
deterioration or improvement. The goal-based approach ensures that
decisions focus on patient safety, early diagnosis, and timely
intervention. This design is essential in healthcare environments where
accuracy, prediction, and reliability are critical.
b. List out atleast three differences between informed and uninformed
search.
Ans.b.
Uninformed
Feature   Informed Search
Search
Uses heuristic
Knowledge   No extra knowledge
knowledge
Approach   Blind exploration   Goal-directed search
Efficiency   Low   High
Node
More   Less
Expansion
Complexity   Higher   Lower (usually)
Example   BFS, DFS   A*, Greedy
What is meant by a production rule in Artificial Intelligence? Explain how
a.   the Water Jug problem can be solved using production rules.
Given:
• 2 jugs, a 4-liter one and a 3-liter one. Neither has any
measuring markers on it.
[10]
• There is a pump that can be used to fill the jugs with water.
How can you get exactly 2 litres of water into 4-liter jug?
Q3
b.
CO-; SO-;   •   Ans.a.
BL-
• A Production Rule is a rule in the form:
IF (condition) THEN (action)
[10]
•   It is used in AI to represent knowledge and problem-solving
steps
•   Consists of:
o Condition (LHS) → when rule is applicable
o Action (RHS) → operation performed
********** 6 **********
--- page 7 ---
• Used in:
o Problem solving
o Expert systems
o State-space search
Water Jug Problem (Using Production Rules)
Given:
• Jug A = 4 litres
• Jug B = 3 litres
• Goal: Get exactly 2 litres in 4L jug
State Representation:
• Represent as: (A, B)
o A = water in 4L jug
o B = water in 3L jug
•   Initial state: (0, 0)
• Goal state: (2, x)
Production Rules
•   Fill 4L jug → (4, B)
•   Fill 3L jug → (A, 3)
• Empty 4L jug → (0, B)
• Empty 3L jug → (A, 0)
• Pour 4L → 3L
• Pour 3L → 4L
Ste   State (A,
Action
p   B)
1   Fill 3L jug   (0, 3)
2   Pour 3L → 4L   (3, 0)
3   Fill 3L jug   (3, 3)
Pour 3L → 4L (till
4   (4, 2)
full)
5   Empty 4L jug   (0, 2)
6   Pour 3L → 4L   (2, 0)
Q.b. Apply Alpha-Beta pruning to a given game tree and Mark pruned
nodes.
********** 7 **********
--- page 8 ---
Ans.b.
The entire second child of right MIN is pruned:
• MAX node with leaves:
o 8
o 1
These nodes are NOT evaluated
Final Result
• Root (MAX) value = 7
Final Answer
Evaluated Nodes:
•   5, 9 → 9
•   2, 3 → 3
• 7
•   4, 6 → 6
Pruned Nodes:
•   8, 1
• Pruning happens when:
o α ≥ β
• Saved computation by skipping unnecessary subtree
Q4   [15]
Question from Unit 3
CO-; SO-;   a.
********** 8 **********
--- page 9 ---
BL-   Using a predicate logic, convert following sentences to predicate and
prove:
Question
2. Every engineer who works on a system understands that system.
3. Anyone who understands a system can maintain it.
4. Every trainee who works under an engineer learns that system.
5. Ananya is a trainee working under EngineerRavi on SystemX.
6. EngineerRavi works on SystemX.
Prove → Maintain(Ananya, SystemX)
Answer.4.a.
Step 1: Define Predicates
7. Engineer(x) : x is an engineer
8. Trainee(x) : x is a trainee
9. WorksOn(x, s) : x works on system s
10. Under(x, y) : x works under y
11. Understands(x, s) : x understands system s
12. Learns(x, s) : x learns system s
13. Maintain(x, s) : x can maintain system s
Step 3: Proof
From (5) and (1):
EngineerRavi is an engineer and works on SystemX
Understands(EngineerRavi,SystemX)Understands(EngineerRavi,
SystemX)Understands(EngineerRavi,SystemX)
********** 9 **********
--- page 10 ---
From (3), (4), and (5):
Ananya is a trainee working under EngineerRavi who works on
SystemX
Learns(Ananya,SystemX)Learns(Ananya, SystemX)Learns(Ananya,SystemX)
Learning implies understanding:
Learns(Ananya,SystemX)→Understands(Ananya,SystemX)Learns(Ananya,
SystemX) \rightarrow Understands(Ananya,
SystemX)Learns(Ananya,SystemX)→Understands(Ananya,SystemX)
From (2):
Understands(Ananya,SystemX)→Maintain(Ananya,SystemX)Understands(Ana
nya, SystemX) \rightarrow Maintain(Ananya,
SystemX)Understands(Ananya,SystemX)→Maintain(Ananya,SystemX)
Conclusion
Maintain(Ananya,SystemX)
Q.4.b.
Write an algorithm of forward chaining? Provide an application where it can
be used.
Ans.4.b
Forward Chaining Algorithm
Forward chaining is a data-driven inference technique used in
Artificial Intelligence. It starts with known facts and repeatedly applies
inference rules to derive new facts until a goal is reached or no more
rules can be applied.
Algorithm: Forward Chaining
Input:
- Knowledge Base KB containing:
• A set of facts
• A set of inference rules (IF–THEN rules)
- Goal (optional)
Output:
- Whether the goal can be derived
Steps:
1. Initialize Working Memory (WM) with all known facts
from KB.
2. Repeat:
a. Select a rule R whose IF part (premise) is
satisfied by facts in WM.
b. If the THEN part (conclusion) of R is not already
in WM:
i. Add the conclusion to WM.
c. Mark rule R as fired.
3. Continue until:
a. The goal is found in WM, OR
b. No new facts can be derived.   [5]
4. If the goal is in WM:
Return SUCCESS.
Else:
Return FAILURE.
********** 10 **********
--- page 11 ---
Explanation
Forward chaining begins with the available data and moves forward
logically by applying rules. It is suitable when all or most facts are
known in advance and the system needs to discover what conclusions
follow from them.
Application of Forward Chaining
Expert Systems (Medical Diagnosis System)
Forward chaining is widely used in medical expert systems.
Example:
Facts:
•   Patient has fever
•   Patient has cough
Rules:
•   If fever and cough → suspect flu
•   If flu → prescribe antiviral medicine
Using forward chaining:
• From fever and cough, the system infers flu
• From flu, it infers treatment recommendation
Thus, forward chaining helps the system automatically derive diagnoses
and treatment suggestions from observed symptoms.
Conclusion
Forward chaining is a powerful inference method for real-time decision
making and monitoring systems, where conclusions must be derived
continuously as new facts arrive.
Tyku is a popular puzzle where each number from 1 to 9 must appear   [10]
exactly once in every row, column, and 3×3 sub-grid.
a.
1. Model the Tyku puzzle as a CSP.
2. Identify the types of constraints involved.
3. Explain how constraint propagation and backtracking are
used to solve Tyku efficiently.
Q5
Ans.a.: Tyku is a classic example of a Constraint Satisfaction
CO-; SO-;   Problem (CSP) in Artificial Intelligence, where the objective is to
BL-   assign values to variables while satisfying a set of constraints. Each cell
in the Sudoku grid must be filled in such a way that the puzzle rules are
followed strictly.
1. Modeling Tyku as a CSP
Sudoku can be modeled as a CSP by defining the following
components:
********** 11 **********
--- page 12 ---
• Variables:
Each cell in the 9×9 Tyku grid is a variable. Thus, there are 81
variables, commonly denoted as XijX_{ij}Xij, where iii and jjj
represent the row and column positions.
• Domains:
The domain of each variable is the set {1,2,3,4,5,6,7,8,9}\{1, 2,
3, 4, 5, 6, 7, 8, 9\}{1,2,3,4,5,6,7,8,9}.
For cells that are pre-filled in the puzzle, the domain is restricted
to the given value.
• Constraints:
Constraints ensure that Sudoku rules are satisfied, i.e., numbers
1 to 9 appear exactly once in each row, column, and 3×3 sub-
grid.
Thus, Tyku is effectively represented as a CSP with variables, domains,
and constraints.
2. Types of Constraints Involved
The constraints in Sudoku are mainly binary and global constraints:
• Row Constraints: All variables in the same row must have
different values (All-Different constraint).
• Column Constraints: All variables in the same column must
have different values.
• Sub-grid Constraints: Each 3×3 sub-grid must contain all digits
from 1 to 9 without repetition.
• Unary Constraints: Pre-filled cells impose unary constraints by
fixing the value of a variable.
3. Use of Constraint Propagation and Backtracking
Constraint propagation is used to reduce the domain of variables by
enforcing constraints. Techniques such as forward checking and arc
consistency (AC-3) eliminate values from a cell’s domain that violate
Sudoku rules. This significantly reduces the search space before actual
guessing begins.
When constraint propagation alone is insufficient, backtracking search
is applied. The algorithm selects an unassigned cell, assigns a value
from its domain, and recursively attempts to solve the remaining puzzle.
If a constraint violation occurs, the algorithm backtracks and tries a
different value. Heuristics such as Minimum Remaining Values
(MRV) and Least Constraining Value (LCV) further improve
efficiency.
Qb. An AI system solving a configuration problem faces repeated
failures deep in the search tree.
********** 12 **********
--- page 13 ---
1. Why is normal backtracking inefficient here?
2. How does intelligent backtracking help?
3. Mention any limitation of intelligent backtracking.
Ans b:
[10]
1. Why is Normal Backtracking Inefficient?
Normal (chronological) backtracking becomes inefficient in
configuration problems when failures occur deep in the search tree. In
such cases, the algorithm backtracks only to the most recent variable
assignment, even if the cause of failure is an earlier decision. This
leads to repeated exploration of similar invalid paths and redundant
computations. As a result, the search process wastes time revisiting the
same conflicting assignments, especially in large and complex
configuration spaces.
2. How Does Intelligent Backtracking Help?
Intelligent backtracking, also known as conflict-directed
backtracking, improves efficiency by analyzing the actual cause of
failure. Instead of backtracking step by step, it jumps directly to the
variable responsible for the conflict. It records conflict sets that identify
which variable assignments led to the failure and avoids repeating them.
By pruning large irrelevant parts of the search tree, intelligent
backtracking significantly reduces unnecessary recomputation and
speeds up problem-solving.
3. Limitation of Intelligent Backtracking
One major limitation of intelligent backtracking is the additional
memory and computation overhead required to store and analyze
conflict sets. Maintaining these conflict explanations can be costly for
very large problems. Additionally, if conflicts are weakly informative or
highly dynamic, the benefits of intelligent backtracking may be limited.
Qa.A logistics company wants to divide a city into 2 delivery zones to
a.   [10]
minimize travel distance for drivers. Each delivery location   is
represented by coordinates (x, y).
Given Locations:
Q6   (2,3), (3,4), (5,8), (6,9), (8,2), (9,3)
CO-; SO-;   Initial Centroids:
BL-   •   C₁ = (2,3) → Zone 1
• C₂ = (8,2) → Zone 2
Perform two Iteration of K-Means and form clusters.
[10]
Ans a. Delivery locations (x, y):
P1 (2,3), P2 (3,4), P3 (5,8), P4 (6,9), P5 (8,2), P6 (9,3)
Number of clusters: K = 2
********** 13 **********
--- page 14 ---
Initial Centroids:
b.
•   C₁ = (2,3) → Zone 1
•   C₂ = (8,2) → Zone 2
Distance measure: Euclidean distance
Iteration 1
Step 1: Assign points to nearest centroid
Point Distance to C₁ (2,3) Distance to C₂ (8,2) Assigned Cluster
(2,3) 0   √37 ≈ 6.08   Zone 1
(3,4) √2 ≈ 1.41   √29 ≈ 5.38   Zone 1
(5,8) √34 ≈ 5.83   √45 ≈ 6.70   Zone 1
(6,9) √52 ≈ 7.21   √53 ≈ 7.28   Zone 1
(8,2) √37 ≈ 6.08   0   Zone 2
(9,3) √49 = 7   √2 ≈ 1.41   Zone 2
Clusters after Iteration 1
• Zone 1: (2,3), (3,4), (5,8), (6,9)
• Zone 2: (8,2), (9,3)
Step 2: Recalculate Centroids
New C₁:
C1=((2+3+5+6)/4,(3+4+8+9)/4)=(4,6)
New C₂:
C2=((8+9)/2,(2+3)/2)=(8.5,2.5)
Iteration 2
Step 1: Reassign points using updated centroids
Point Distance to C₁ (4,6) Distance to C₂ (8.5,2.5) Assigned Cluster
(2,3) √13 ≈ 3.61   √42.5 ≈ 6.52   Zone 1
(3,4) √5 ≈ 2.24   √32.5 ≈ 5.70   Zone 1
(5,8) √5 ≈ 2.24   √46.5 ≈ 6.82   Zone 1
(6,9) √13 ≈ 3.61   √52.5 ≈ 7.24   Zone 1
(8,2) √32 ≈ 5.66   √0.5 ≈ 0.71   Zone 2
(9,3) √34 ≈ 5.83   √0.5 ≈ 0.71   Zone 2
Clusters after Iteration 2
• Zone 1: (2,3), (3,4), (5,8), (6,9)
• Zone 2: (8,2), (9,3)
Clusters remain unchanged, so the algorithm has converged.
Final Centroids
•   C₁ = (4,6)
•   C₂ = (8.5,2.5)
********** 14 **********
--- page 15 ---
Q .b. Calculate the Entropy and Information Gain for the dataset below
and identify the best attribute to split while constructing a decision tree.
Predicting whether a customer will subscribe to a service
Usage
Support Calls Contract Type Subscribe
Level
High   Low   Annual   Yes
Medium   Low   Monthly   Yes
Low   High   Monthly   No
High   Low   Annual   Yes
Medium   High   Monthly   No
Low   High   Annual   No
High   Low   Monthly   Yes
Medium   High   Annual   No
• Compute the entropy of the target variable (Subscribe).
•   Calculate information gain for each attribute:
o Usage Level
o Support Calls
o Contract Type
•   Identify the best attribute to split.
Ans b. 1. Entropy of Target Variable (Subscribe)
Class Distribution
• Yes = 4
• No = 4
Entropy(S)=−(4/8 log 2 4/8+ 4/8 log 2 4/8) <- base 2
Entropy(S)=−(0.5×−1+0.5×−1)
Entropy(S)=1.0
2. Information Gain Calculation
A) Attribute: Usage Level
Usage Level Yes No Total
High   3   0 3
Medium   1   2 3
Low   0   2 2
Entropy for each subset
• High Entropy=0(pure)
• Medium Entropy=−(1/3 log 2 1/3+ 2/3 log 2 2/3)=0.918
• Low Entropy=0(pure)
Weighted Entropy: E(Usage)=3/8(0)+3/8(0.918)+2/8(0)
E(Usage)=0.344
Information Gain: IG(Usage)=1.0−0.344=0.656
********** 15 **********
--- page 16 ---
B) Attribute: Support Calls
Support Calls Yes No Total
Low   4   0 4
High   0   4 4
Entropy
• Low → 0
•   High → 0
Weighted Entropy
E(Support)=4/8(0)+ 4/8(0) =0
Information Gain
IG(Support)=1.0−0=1.0
C) Attribute: Contract Type
Contract Type Yes No Total
Annual   2   2 4
Monthly   2   2 4
Entropy for each subset
Entropy=−(2/4 log 2 2/4+ 2/4 log 2 2/4)=1
Weighted Entropy
E(Contract)=4/8(1)+4/8(1)=1
Information Gain
IG(Contract)=1.0−1.0=0
3. Best Attribute to Split
Attribute   Information Gain
Usage Level   0.656
Support Calls 1.0 (Highest)
Contract Type 0
Best Attribute to Split: Support Calls
•   Entropy of Subscribe = 1.0
•   Information Gain:
o Usage Level = 0.656
o Support Calls = 1.0
o Contract Type = 0
•   Best split attribute = Support Calls
Q 7.a. Define modus ponens and its application.   [5]
a.   Ans.7.a
Q7
Modus Ponens
CO-; SO-;
Definition
BL-
• Modus Ponens is a fundamental rule of inference in logic
•   It states:
********** 16 **********
--- page 17 ---
o   If P → Q (If P implies Q)
o And P is true Then Q is true
Example
If it rains, the ground is wet (P → Q)
It is raining (P)
∴ The ground is wet (Q)
Applications of Modus Ponens
•   Logical reasoning: Used to derive valid conclusions from known
facts
• Expert systems: Applies rules of the form IF–THEN to infer
results
•   Artificial Intelligence: Used in forward chaining and backward
chaining
• Mathematics and proofs: Helps in step-by-step logical proofs
• Programming / Rule-based systems: Used in decision-making
systems
What is an expert system? Explain each component with neat diagram.
b   Provide at least two examples of popular expert systems.   [15]
Ans 7.a.
********** 17 **********
--- page 18 ---
An Expert System is an AI program that mimics the decision-making
ability of a human expert. It uses knowledge + reasoning to solve
complex problems in a specific domain. Commonly used in: Medical
diagnosis Troubleshooting, Financial decision-making.
Components of an Expert System
1. Knowledge Base
•   Stores domain knowledge
• Contains Facts and Rules (IF–THEN)
• Example: Medical symptoms and disease rules
2. Inference Engine
• Acts as the brain of the system
•   Applies rules to known facts
• Performs reasoning using:
o Forward chaining
o Backward chaining
3. Working Memory
•   Stores current facts and intermediate results
• Updated during problem solving
4. User Interface (UI)
• Allows interaction between user and system
• Takes input and displays output
5. Explanation Facility
•   Explains: How a conclusion was reached? Why a particular
question was asked?
6. Knowledge Acquisition Module
• Helps in adding/updating knowledge
•   Collects knowledge from experts
Examples of Expert Systems
o MYCIN :Used for diagnosing bacterial infections
o DENDRAL : Used in chemistry for molecular structure
analysis
********** 18 **********
--- page 19 ---
o XCON (R1): Used by DEC for computer system

configuration

FRR ICR 7 QI OR
````

## 2025-26 · Re-Exam · Sem 9 · Answer key · paper 60db32e7d4c9

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_09/Re-Exam/Integrated_Computer_7032/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: mixed (20 pages), mean OCR confidence 80.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Artificial Intelligence
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   State the differences between Greedy Best First Search and A* Search
strategies with examples.
Solution –
CO-2 ;
SO-   [5]
1,2,6,7 ;
BL-2
Marking Scheme –
Each point – 1 mark
b.   Consider the following knowledge base:
1. If a person studies hard, then the person passes the exam.
CO-3 ;
2. If a person passes the exam, then the person gets a job.
SO-   3. Ram studies hard.   [5]
1,6,7 ;
BL-2
Using forward chaining inference, determine whether Ram gets a job.
Show the sequence of inferences made.
********** 1 **********
--- page 2 ---
Solution –
Step 1: Known fact
• From (3): studies_hard(Ram) is true.
Step 2: Apply Rule 1
• Rule 1: If a person studies hard, then the person passes the
exam.
• Antecedent: studies_hard(Ram) → satisfied.
•   Therefore, passes_exam(Ram) can be inferred.
Step 3: Apply Rule 2
• Rule 2: If a person passes the exam, then the person gets a job.
• Antecedent: passes_exam(Ram) → satisfied.
•   Therefore, gets_job(Ram) can be inferred.
By forward chaining, we infer that Ram gets a job.
c.   Solve the following Cryptarithmatic –
SEND + MORE = MONEY
Solution –
S = 9
E = 5
CO-3 ;   N = 6
SO-   D = 7   [5]
1,6,7 ;   M = 1
BL-3   O = 0
R = 8
Y = 2
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
d.   Cluster these points into K = 2 clusters –
CO-4 ;
SO-   Data = [2, 3, 6, 8, 10, 12]
[5]
1,5,6,7 ;   Assume the initial centroids are C₁ = 4 and C₂ = 9.
BL-3
Solution –
********** 2 **********
--- page 3 ---
Cluster assignment after Iteration 1:
•   Cluster 1 (C₁): [2, 3, 6]
•   Cluster 2 (C₂): [8, 10, 12]
Update centroids
Compute the mean of each cluster:
• C₁_new = (2 + 3 + 6)/3 = 11/3 ≈ 3.67
• C₂_new = (8 + 10 + 12)/3 = 30/3 = 10
Cluster assignment unchanged:
•   Cluster 1 (C₁): [2, 3, 6]
•   Cluster 2 (C₂): [8, 10, 12]
Centroids update again:
• C₁_new = (2+3+6)/3 ≈ 3.67 (same as previous)
• C₂_new = (8+10+12)/3 = 10 (same as previous)
Since centroids did not change, the algorithm converges.
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
a. Explain the architecture of a Goal-based Agent with neat diagram.
Clearly describe the roles of its components.
Q2   Solution –
CO-1, 1,   • Knowing about the current state of the environment is not always
2; SO-   enough to decide what to do (e.g. decision at a road junction)
1,2,   • The agent needs some sort of goal information that describes [10+5+5]
5,6,7;   situations that are desirable
BL-2, 3,   • The agent program can combine this with information about the
2   results of possible actions in order to choose actions that achieve
the goal
•   Usually requires search and planning
********** 3 **********
--- page 4 ---
Sensors
• Role: Detect and perceive the current state of the environment.
• Example: Cameras, temperature sensors, RFID scanners, motion
detectors.
Percept Sequence
• Role: Keeps a history of all percepts the agent has received. This
helps the agent understand how the environment is changing over
time.
• Example: A smart thermostat recording temperature changes over
hours.
Model of the World / State Representation
• Role: Represents the current state of the environment and predicts
the effects of possible actions.
• Example: A self-driving car maintaining a map of the road and
positions of other vehicles.
Goal Generator
• Role: Specifies the desired outcomes or objectives that the agent
wants to achieve.
• Example: “Reach destination safely” for a self-driving car or
“minimize food wastage” for a smart refrigerator.
Decision / Reasoning Module
• Role: Evaluates possible actions and selects the one that best
achieves the goal, often by planning or searching future states.
• Example: Choosing whether to slow down, overtake, or stop in
traffic.
Actuators
• Role: Execute the chosen actions in the environment.
• Example: Steering wheel, brakes, accelerator for a car; controlling
fridge temperature or sending notifications for a smart
refrigerator.
Marking Scheme –
Diagram – 5 marks
Explanation – 5 marks
b. Define the PEAS properties and construct a complete PEAS
description for an ‘AI-based Smart Refrigerator’, clearly
explaining each component.
Solution –
********** 4 **********
--- page 5 ---
Marking Scheme –
Each Property – 1 mark
Discussion – 1 mark
c. Explain the roles of main steps of Genetic Algorithm (GA) and
discuss advantages and disadvantages of GA.
Solution –
Main steps of GA:
1. Initialization: Generate a random population of chromosomes.
2. Evaluation: Compute fitness of each chromosome.
3. Selection: Choose chromosomes for reproduction based on
fitness.
4. Crossover: Combine selected parents to create offspring.
5. Mutation: Introduce random changes in offspring to maintain
diversity.
6. Replacement: Form a new generation and repeat until
termination criteria.
Advantages:
• Works for complex, non-linear, and multi-modal problems.
• Does not require derivative information.
Limitations:
• May converge slowly.
• Needs careful tuning of parameters (mutation rate, population
size).
Marking Scheme –
Steps of GA – 3 marks
********** 5 **********
--- page 6 ---
Advantages – 1 mark
Disadvantages – 1 mark
a. Solve 8 tiles problem using Greedy Best First Search. Consider
the no. of misplaced tiles as the heuristic.
Solution –
Q3
CO-2, 2,
1; SO-   [5+10+5]
1,2,5,6,7;
BL-3, 3,
2
Marking Scheme –
Approach – 3 marks
Correct solution – 2 marks
b. Apply Alpha-Beta pruning algorithm to prune the game tree
shown below.
********** 6 **********
--- page 7 ---
Solution –
Marking Scheme –
Each Correct Prune – 2 marks
c. What are the different types of agents? Give one example for
each.
Solution –
Marking Scheme –
Each agent – 1 mark
********** 7 **********
--- page 8 ---
a. Consider the following facts and prove that Bob will receive a
bonus using Resolution Graph.
i. Any employee who completes a project successfully is
eligible for a bonus.
ii. Any employee who is eligible for a bonus and has
excellent performance receives a bonus.
iii. Bob completed a project successfully.
iv. Bob has excellent performance.
v. Any employee who receives a bonus is appreciated by
HR.
vi. Any employee who is appreciated by HR and meets
criteria gets promoted.
vii. Every employee who exceeds targets is eligible for a
bonus.
Solution –
Q4
CO-3, 3;   [15+5]
SO-1,6,7;
BL-3, 3
********** 8 **********
--- page 9 ---
Marking Scheme –
Conversion to FOL – 5 marks
Conversion to CNF – 5 marks
Resolution Graph – 5 marks
b. Color the countries with any one of 2 colors: {Red, Green, B}
such that no two neighboring countries share the same color,
also explain when backtracking is required in Map Coloring
problem.
Countries: [India, Pakistan, Nepal, Bangladesh, Bhutan, Myanmar]
Borders:
• India borders Pakistan, Nepal, Bangladesh, Bhutan, Myanmar
• Pakistan borders India
• Nepal borders India, Bhutan
• Bangladesh borders India, Myanmar
• Bhutan borders India, Nepal
• Myanmar borders India, Bangladesh
Solution –
Pakistan: neighbor of India → cannot be Red → choose Green
Nepal: neighbor of India → cannot be Red → choose Green
Bangladesh: neighbor of India → cannot be Red → choose Green
Bhutan: neighbor of India and Nepal → cannot be Red (India) or
Green (Nepal) → choose Blue
Myanmar: neighbor of India and Bangladesh → cannot be Red
(India) or Green (Bangladesh) → choose Blue
Backtracking is needed if a conflict occurs during assignment, i.e., no
available color left for a country:
• Example scenario:
********** 9 **********
--- page 10 ---
Suppose we initially colored Nepal → Green and Bangladesh →
Green (as above), and then we tried Bhutan → Green instead of
Blue:
o Bhutan neighbors: India (Red) → ok, Nepal (Green) →
conflict!
o No other color available? If we had only 2 colors, yes →
no valid choice → must backtrack.
•   Similarly, if Myanmar cannot pick a valid color because all
neighbors already have colors conflicting with its available
options → backtracking occurs.
Backtracking is required whenever a country cannot be assigned a
color without violating constraints, especially in densely connected
graphs with triangles.
In this problem, because neighbors of India also border each other
(Nepal–Bhutan, Bangladesh–Myanmar), bad early choices may force
backtracking.
Marking Scheme –
Colouring map – 3 marks
Explanation when backtracking required – 2 marks
a. Convert the following facts into FOL:
i. Anyone who rides any Harley is a rough character.
ii. Anyone who rides any BMW is a yuppie.
iii. Every yuppie is a lawyer.
iv. Any nice girl does not date anyone who is a rough character.
v. Mary is a nice girl, and John is a biker.
Solution –
Anyone who rides any Harley is a rough character.
∀ x ((∃ y (HARLEY(y) ∧ RIDES(x,y))) → ROUGH(x))
Q5
Anyone who rides any BMW is a yuppie.
CO-3, 3,   ∀ x ∀ y (RIDES(x,y) ∧ BMW(y) → YUPPIE(x))
4; SO-
[5+5+10]
1,5,6,7;   Every yuppie is a lawyer.
BL-3, 2,   ∀ x (YUPPIE(x) → LAWYER(x))
3
Any nice girl does not date anyone who is a rough character.
∀ x ∀ y (NICE(x) ∧ ROUGH(y) → ¬ DATE(x,y))
Mary is a nice girl, and John is a biker.
NICE(Mary) ∧ BIKER(John)
Marking Scheme –
Each FOL – 1 mark
c. Write down the rules to convert FOL into CNF.
Solution –
********** 10 **********
--- page 11 ---
Marking Scheme –
Each rule – 0.5 marks
Concept – 1 mark
c. Write down K-means Clustering Algorithm. A coffee shop wants to
segment customers based on amount spent per visit (in $) and number
of visits per week to design targeted offers. Group customers into 2
clusters, where initial cluster centres are (5, 1) and (15, 5).
********** 11 **********
--- page 12 ---
Customer Amount Spent ($) Visits per Week

a 5 1
c2 7 2
3 8 1
cA 15 5
cs 16 4
6 14 5
c7 3 1

Solution —

Step 1: Assign Customers to Nearest Cluster

Euclidean distance formula:
( — x)? + (y ~ Ye)?

Compute distances and assignments:

Customer To C1 (5,1) To C2 (15,5) Cluster Assigned
C1 (5,1) O v((5-15)*2 + (1-5)42) = ¥116 = a
10.77
C2 (7,2) V((7-5)42 + (2-1)42) = V5 = V((7-15)42 + (2-5)*2) = V73 = a
2.24 8.54
C3 (8,1) V((8-5)42 + (1-1)42) = V9 =3 V((8-15)*2 + (1-5)*2) = V65 = a
8.06
C4 (15,5) V((15-5)42 + (5-1)42) = V116 = t) c2
10.77
C5 (16,4) V((16-5)42 + (4-1)42) = V122 = V((16-15)42 + (4-5)*2) = V2 = c2
11.05 1.41
C6 (14,5) V((14-5)42 + (5-1)*2) = V97 = V((14-15)42 + (5-5)42) = V1 = c2
9.85 1
C7 (3,1) V((3-5)42 + (1-1)42) = V4 =2 ¥((3-15)*2 + (1-5)42) = ¥160 = a
12.65

Cluster assignment after first iteration:

e Cluster 1: Cl, C2, C3, C7
e Cluster 2: C4, C5, C6

Step 2: Compute New Cluster Centers

Cluster 1: Mean of (Amount Spent, Visits):

5+74+843 1424141
4 , 4

Clnew = ( ) = (5.75, 1.25)

Cluster 2: Mean of (Amount Spent, Visits):

15+16+14 54+4+5
3 , 3

C2nene — ( ) = (15, 4.67)

FRR ICR] DA KH
--- page 13 ---
Cluster assignments remain the same → Converged.
Step 4: Final Clusters
• Cluster 1 (C1): C1, C2, C3, C7 → Center (5.75, 1.25)
• Cluster 2 (C2): C4, C5, C6 → Center (15, 4.67)
Marking Scheme –
Algorithm – 3 marks
Correct approach – 2 marks
Iteration 1 – 2 marks
Iteration 2 – 2 marks
Iteration 3 – 1 mark
Q6
CO-4, 4;
SO-   [15+5]
1,5,6,7;
BL-3, 2
Using the dataset, build a decision tree to predict Return. You may use
any decision tree algorithm (ID3 or CART). Determine the root node and
subsequent splits based on your chosen method. Define Inductive
Learning and explain how it can be applied to this dataset. Generate IF–
THEN rules from your decision tree for predicting Return.
Solution –
********** 13 **********
--- page 14 ---
Entropy formula:

Entropy(S) = — S~ pi logo(pi)

e Total Yes = 5 (Applicants 1,2,3,6,8)
© Total No = 3 (Applicants 4,5,7)

5 5 3 3
Entropy(S) = -3 logs 378 logs 3

Step by step:

5 3
= = 0.625, = =0.375
8 8

Entropy(S) — —0.625 - log, (0.625) — 0.375 - log,(0.375)
log,(0.625) ~ —0.678, log,(0.375) = —1.415
Entropy(S) = —(0.625 - —0.678 + 0.375 - —1.415)

Entropy(S) = 0.423 + 0.531 = 0.954

A) CreditHistory
© Good: Applicants 1,2,8 - ApproveLoan = Yes, Yes, Yes — All Yes
=> Entropy — 0
e Fair: Applicants 3,6,7 + ApproveLoan = Yes, Yes, No — 2 Yes, 1 No

2 2 1 1
Entropy(Fair) = -3 logs 373 log 3

2 1
-3° (—0.585) — 37 (—1.585) = 0.389 + 0.528 = 0.918

¢ Poor: Applicants 4,5 — ApproveLoan = No, No = All No = Entropy = 0
Weighted Entropy:

E(CreditHistory) = : -O+ ; - 0.918 + ; -0 = 0.344

Gain(CreditHistory) = 0.954 — 0.344 = 0.610

B) Income
¢ High: Applicants 1,2,3 - ApproveLoan = Yes, Yes, Yes ~ Entropy = 0
¢ Medium: Applicants 4,6,8 —- ApproveLoan = No, Yes, Yes > 2 Yes, 1 No — Entropy = 0.918
© Low: Applicants 5,7 — ApproveLoan = No, No — Entropy = 0

Weighted Entropy:

2
E(Income) = ; 04 : 0.918 + 5-0 = 0.344

Gain(Income) = 0.954 — 0.344 = 0.610

FRR IC 7 I OH
--- page 15 ---
Highest gain = CreditHistory (0.610) or Income (0.610) → choose
CreditHistory as root.
Good: Applicants 1,2,8 → All Yes → Leaf Node: ApproveLoan =
Yes
Poor: Applicants 4,5 → All No → Leaf Node: ApproveLoan = No
Fair: Applicants 3,6,7 → Mix (Yes, Yes, No) → Need further
splitting
Entropy of this subset ≈ 0.918 (as calculated earlier)
Check Information Gain for remaining attributes:
• Income: High → Yes (Entropy=0)
Medium → Yes (Entropy=0)
Low → No (Entropy=0)
Weighted Entropy: E(Income)=0E(Income) = 0E(Income)=0 → Gain =
0.918 → best split = Income
High: Applicant 3 → Yes → Leaf: Yes
Medium: Applicant 6 → Yes → Leaf: Yes
Low: Applicant 7 → No → Leaf: No
********** 15 **********
--- page 16 ---
Marking Scheme –
Approach – 10 marks
Correct Tree – 5 marks
b. Explain the components of a Rule-Based Expert System and illustrate
its working with a neat diagram.
Solution –
A typical RBES has five main components:
A) Knowledge Base
•   Stores domain-specific knowledge as facts and rules.
•   Facts: Statements about the problem (e.g., “Patient has fever”)
• Rules: IF–THEN statements (e.g., “IF fever AND headache
THEN disease = Flu”)
B) Inference Engine
• The “brain” of the system.
• Applies reasoning techniques to deduce new facts or make
decisions.
• Two main reasoning methods:
o Forward chaining: Starts with facts → applies rules →
deduces conclusions.
o Backward chaining: Starts with goal → searches for
rules → verifies facts.
C) Working Memory (Fact Base)
• Temporary storage for current facts of the problem.
• Updated as the inference engine applies rules.
• Example: “Patient has high fever” is stored here.
D) User Interface
• Enables interaction between user and system.
• Users can input facts and get solutions.
• Example: A doctor enters symptoms, system outputs possible
disease.
E) Explanation Facility
• Explains why a conclusion was reached or which rules were
applied.
• Helps build trust in the system.
• Example: “Patient has fever and headache → Flu diagnosed.”
Working of Rule-Based Expert System
Step-by-step process:
1. User inputs facts → Stored in working memory
2. Inference engine checks rules in the knowledge base.
3. Matches rules whose conditions satisfy the facts.
4. Applies the rule → Deduces new facts or decision.
5. Updates working memory.
6. Provides conclusion to user via the interface.
7. Explanation facility can explain reasoning steps.
********** 16 **********
--- page 17 ---
Marking Scheme –
Diagram – 3 marks
Explanation – 2 marks
a. A dataset contains information about 120 students of a university.
The attributes are:
• Age (numeric)
• GPA (numeric, 0–10)
• Study Hours per Week (numeric)
• Scholarship Status (Yes, No)
i) Explain how you would use a classification algorithm to predict
whether a new student will receive a scholarship, given the other
attributes. Mention the steps and a suitable algorithm.
Q7   ii) Explain how you would use a clustering algorithm to segment the
students into groups based on their academic performance (GPA and
CO-4, 3,   Study Hours). Describe the steps and a suitable algorithm.
4, 4; SO-   [5+5+5+5
1,5,6,7;   Solution –   ]
BL-4, 3,
2, 4   To predict whether a new student will receive a scholarship based on
attributes like Age, GPA, and Study Hours per Week, a classification
algorithm such as a decision tree can be used. First, the dataset of 120
students is preprocessed to handle any missing values, and numeric
attributes may be scaled if necessary. The dataset is then divided into
training and testing sets, typically in an 80:20 ratio. Using the training
data, a decision tree is built by selecting at each node the attribute that
best splits the data, using criteria like Information Gain or Gini Index.
For numeric attributes like GPA or Study Hours, appropriate threshold
values are determined to create splits. The resulting tree produces IF–
THEN rules, for example, “IF GPA > 8 AND Study Hours > 20 THEN
Scholarship = Yes,” which makes the model interpretable. After
evaluating the model on the test set to check its accuracy, it can be used
to predict the scholarship status of a new student by following the tree
********** 17 **********
--- page 18 ---
from the root to the appropriate leaf node based on the student’s attribute
values. This approach is advantageous because it handles numeric data
effectively and provides a clear reasoning path for decisions, which is
useful for university administration.
To segment the students into groups based on their academic performance
using clustering, we can apply an unsupervised learning algorithm
such as K-Means clustering. In this approach, the attributes GPA and
Study Hours per Week are used as input features, while Age and
Scholarship Status are ignored since clustering is based solely on
performance. First, the dataset should be preprocessed by handling any
missing values and scaling the numeric attributes if they have different
ranges, to ensure fair distance calculations. Next, a suitable number of
clusters, say k = 3 (e.g., low, medium, and high performers), is chosen,
and k initial cluster centroids are selected randomly. Each student is
then assigned to the nearest cluster centroid based on a distance measure
such as Euclidean distance. After all students are assigned, the centroids
are recalculated as the mean GPA and Study Hours of the students in each
cluster. This process of assignment and centroid recalculation is repeated
iteratively until the clusters stabilize and no further changes occur. The
final clusters represent groups of students with similar academic
performance, which can help the university identify high achievers,
average performers, and students who may need additional support.
Marking Scheme –
Classification – 2.5 marks
Clustering – 2.5 marks
b. Solve the N-Queens problem for N = 4 using backtracking. Show the
stepwise placement of queens and indicate where backtracking occurs.
Solution –
Goal: Place 4 queens on a 4×4 board so that no two queens attack each
other.
Steps:
1. Row 1: Place Q1 at column 1 → Safe
2. Row 2:
o Column 1 → Unsafe (same column)
o Column 2 → Unsafe (diagonal conflict)
o Column 3 → Safe → Place Q2 at (2,3)
3. Row 3:
o All columns unsafe → Backtrack: Remove Q2 from
(2,3)
4. Row 2 (Retry):
o Column 4 → Safe → Place Q2 at (2,4)
5. Row 3:
o Column 1 → Safe → Place Q3 at (3,1)
6. Row 4:
o Column 3 → Safe → Place Q4 at (4,3) → Solution 1
found
7. Second Solution: Explore alternative placements for Q1 and Q2
to find another arrangement.
********** 18 **********
--- page 19 ---
Backtracking occurs whenever no safe column is found in a row (Row
3 after first Q2 placement).
Marking Scheme –
Approach – 3 marks
Correct answer – 2 marks
c. What is an expert system? Write its advantages and disadvantages.
Solution –
An expert system is a computer program that is designed to solve
complex problems and to provide decision-making ability like a human
expert. It performs this by extracting knowledge from its knowledge base
using the reasoning and inference rules according to the user queries.
Advantages of Expert System
o These systems are highly reproducible.
o They can be used for risky places where the human presence is
not safe.
o Error possibilities are less if the KB contains correct knowledge.
o The performance of these systems remains steady as it is not
affected by emotions, tension, or fatigue.
o They provide a very high speed to respond to a particular query.
Limitations of Expert System
o The response of the expert system may get wrong if the knowledge
base contains the wrong information.
o Like a human being, it cannot produce a creative output for
different scenarios.
o   Its maintenance and development costs are very high.
o Knowledge acquisition for designing is much difficult.
o For each domain, we require a specific ES, which is one of the big
limitations.
o   It cannot learn from itself and hence requires manual updates.
Marking Scheme –
Definition – 1 mark
Advantages – 2 marks
d. A travel clinic wants to develop an expert system to advise travellers
about possible illnesses based on their symptoms. The system should
suggest a likely disease and recommend precautions.
Diseases: Dengue, Typhoid, and Food Poisoning
Symptoms:
• Fever (High, Low)
• Nausea (Yes, No)
• Stomach Pain (Yes, No)
• Headache (Yes, No)
i) Design a simple rule-based expert system with at least 5 IF–THEN
rules to diagnose the above diseases.
********** 19 **********
--- page 20 ---
ii) Explain how the expert system would infer a diagnosis when a
new traveller provides their symptoms.
Solution –
i) Rule-Based Expert System Design
Diseases: Dengue, Typhoid, Food Poisoning
Symptoms: Fever, Nausea, Stomach Pain, Headache
Knowledge Base (IF–THEN Rules)
1. Rule 1: IF Fever = High AND Headache = Yes AND Nausea =
Yes THEN Disease = Dengue AND Precaution = “Rest,
Hydration, Visit doctor”
2. Rule 2: IF Fever = High AND Stomach Pain = Yes AND Nausea
= Yes THEN Disease = Typhoid AND Precaution = “Avoid
contaminated food/water, Visit doctor”
3. Rule 3: IF Fever = Low AND Stomach Pain = Yes AND Nausea
= Yes THEN Disease = Food Poisoning AND Precaution =
“Drink fluids, Eat light diet”
4. Rule 4: IF Fever = High AND Headache = Yes AND Stomach
Pain = No THEN Disease = Dengue AND Precaution = “Rest,
Hydration, Monitor symptoms”
5. Rule 5: IF Fever = Low AND Nausea = Yes AND Stomach Pain
= No THEN Disease = Food Poisoning AND Precaution =
“Hydration, Avoid oily food”
ii) Inference Process (How the Expert System Works)
1. Input Symptoms: A traveller enters their symptoms, e.g., Fever
= High, Nausea = Yes, Stomach Pain = No, Headache = Yes.
2. Working Memory: The system stores these symptoms as facts.
3. Rule Matching: The inference engine checks each IF–THEN
rule to see which rule conditions match the traveller’s symptoms.
o In this example, Rule 4 matches.
4. Apply Rule: The system infers that the likely disease is Dengue.
5. Provide Recommendation: The system outputs the
precaution/advice associated with the rule: “Rest, Hydration,
Monitor symptoms.”
6. Explanation (Optional): The system can explain the reasoning:
“Since Fever is High, Headache is present, and Stomach Pain is
absent, Dengue is suggested.”
********** 20 **********
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 20ec7c427690

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Artificial Intelligence/ANS_Artificial Intelligence(703CO0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2025
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Artificial Intelligence
Date: 02 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 9 pages.
2. Question No. _1_ is compulsory.
3. Out of remaining questions, attempt any _4_ questions.
4. In all _5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-2 ;   a.   Explain the uniform cost searching with an example   [05]
BL-
Ans.   Explanation [2M]
Finding the least cost path in a graph. It is a variant of Dijkstra's algorithm and is
particularly useful when all edges of the graph have different weights, and the
goal is to find the path with the minimum total cost from a start node to a goal
node.
Uniform Cost Search is a pathfinding algorithm that expands the least cost
node first, ensuring that the path to the goal node has the minimum cost.
Example [3M]
CO- 3;   b.   Discuss any five issue of knowledge acquisition process used in expert systems. [05]
BL-
Ans.   The important issues in knowledge acquisition are:
■ knowledge is in the head of experts
■ Experts have vast amounts of knowledge
■ Experts have a lot of unspoken (tacit) knowledge
–   They do not know all that they know and use
– Unspoken knowledge is hard (impossible) to describe
■ Experts are very busy and valuable people
■ One expert does not know everything
■ Knowledge has a "shelf life“
CO- 2;   c.   Discuss the significance of alpha-beta pruning with an example.   [05]
BL-
********** 1 **********
--- page 2 ---
Ans.   • α is the value of the best (i.e., highest-value) choice found so far at any
choice point along the path for max
•   If v is worse than α, max will avoid it: prune that branch
CO- 1;   d.   Discuss the goal based agent with suitable example   [05]
BL-
Ans.   Discussion on agent [4M]
Example: [1M]
 Prepare a shopping list – because our goal is to purchase things we
required.
   It helps us to decide between options
   If milk is the goal on our list then we will not pick up orange juice
Q2   a.   Apply and discuss the steps of genetic algorithm to find the solutions for 8-
[10]
CO-2;   queen problem.
BL-
Ans.   • A successor state is generated by combining two parent states
•   Start with k randomly generated states (population)
• A state is represented as a string over a finite alphabet (often a string
of 0s and 1s)
•   Evaluation function (fitness function). Higher values for better states.
•   Produce the next generation of states by selection, crossover, and
mutation
• To represents the single state of the chess board 24 bits are required
•   Each state is rated by evaluation function (fitness function)
•   Fitness function should return higher value for better state
• Number of non-attacking pair is used as fitness function (28 is the
solution)
********** 2 **********
--- page 3 ---
• The values for the four state are 24, 23, 20 and11
CO-1;   b.   Discuss various types of task environments for agents. How environment
[10]
BL-   affects the performance of intelligent agents? Give example
Ans.   Task Environment [6M]
   Fully observable (vs. partially observable):
 Deterministic (vs. stochastic):
 Episodic (vs. sequential):
   Static (vs. dynamic):
 Discrete (vs. continuous):
   Single agent (vs. Multi-agent):
Effect on design and example [4M]
Q3   a.   Explain the application of MINMAX search algorithm with suitable example.
[10]
CO-2;   Discuss two refinements.
BL-
Ans.   •   Perfect play for deterministic games
•   Idea: choose move to position with highest minimax value
= best achievable payoff against best play
•   E.g., 2-ply game:
********** 3 **********
--- page 4 ---
CO-1;   b.
Explain the Learning Agent with suitable diagram and example.   [10]
BL-
Ans.   Diagram and description [7M]
1. Sensors: Sensors collect information from the environment and send it
to the agent, allowing for decision-making and acquisition of
knowledge.
2. Critic: The critic assesses and offers feedback on the agent's
performance based on pre-established goals or a predetermined reward
system. The critic supports the learner by providing feedback on the
quality of their decisions, allowing them to enhance their skills
through various activities.
3. Learning Element: This part acts as the central cognitive hub of the
agent, responsible for analyzing the experiences acquired from
interactions with the surroundings.
4. Performance Element: The performance element requires the
learning element and critic feedback so as to manage the agent's
activities in an environment.
5. Actuators: Actuators, also called effectors, carry out tasks selected by
the performance element
6. Problem Generator: The problem generator is in charge of creating
challenges or activities for the agent to complete. It consists of
situations that require the agent to apply the knowledge and skills it
has gained, hence improving ongoing learning and talent development.
Example[3M]
Q4   a.   How does informed search improve the performance over uninformed
[05]
CO-2;   search? Give example.
BL-
Ans.   Discussion on DFS or BFS – [2M]
Heuristics can improve the performance [2M]
********** 4 **********
--- page 5 ---
Finding shortest path with heuristics can be an example [1M]
b.   Consider the following statements and convert to WFF.
1.   It is a crime for an American to sell weapons to hostile nations
2. Country nono has some missiles
3. All of its missiles were sold to it by Colonel West
CO-3;
4. Missiles are weapons   [15]
BL-   5. An enemy of America counts as "hostile”
6. West, who is American
7. The country Nono, an enemy of America
Prove that “Col. West is a criminal” using Resolution method.
Ans.   WFF [5M]
CNF [5M]
Proof[5M]
********** 5 **********
--- page 6 ---
a.   Apply the backward chaining method to find if Christena is healthy or sick.
Following is the given information:
Q5
If food is oily it is good in taste and not good for health. If anyone eats   [10]
CO-3;
BL-   unhealthy food they fall sick. Christena loves oily food and she eats only what
she loves. “Potato wedges” is an oily food item.
Ans.   Convert to FOPL [5M]
Proof by backward chaining with each step :[5M]
CO-3;   b.   What is constraint satisfaction problem? Explain with the example of
[10]
BL-   cryptarithmetic problem.
********** 6 **********
--- page 7 ---
Ans.   Explanation on CSP [4M]
example of cryptarithmetic problem [6M]
1. Variables: F T U W
R O X1 X2 X3
2. Domains: {0,1,2,3,4,5,6,7,8,9}
3. Constraints: Alldiff (F,T,U,W,R,O)
a. O + O = R + 10 · X1
b. X1 + W + W = U + 10 · X2
c. X2 + T + T = O + 10 · X3
d. X3 = F, T ≠ 0, F ≠ 0
Q6   a.   What is unsupervised learning? Discuss step-by-step process of learning by k-
[10]
CO-4;   means clustering algorithm.
BL-
Ans.   Explanation on unsupervised learning [2M]
Student can give different algorithm – step-by-step [8M]
CO-2;   b.   Explain the significance of backtracking search in constraint satisfaction
[10]
BL-   problem with Graph Coloring Problem.
Ans.
Explanation on backtracking method [4M]
********** 7 **********
--- page 8 ---
Graph coloring problem [6M]
Q7   a.
Explain the method of inductive learning. Give suitable example.   [10]
CO-4;
BL-
Ans.   • The inductive learning is a process of learning by example. The
system tries to induce a general rules from a set of observed instances.
The learning methods extract rules and patterns out of massive data
sets.
• The learning processes belong to supervised learning, does
classification and constructs class definitions, called induction or
concept learning
•   Simplest form: learn a function from examples
f is the target function
An example is a pair (x, f(x))
Problem: find a hypothesis h
such that h ≈ f
given a training set of examples
(This is a highly simplified model of real learning:
–   Ignores prior knowledge
– Assumes examples are given
Explanation on learning example with different models [5M]
********** 8 **********
--- page 9 ---
CO-3;   b.
Discuss significant characteristics of an expert system.   [10]
BL-
Ans.   1. Operates as an interactive system
2. Tools have ability to store and select (filter) knowledge
3. Ability to explain reasoning
4. Systems are very domain-specific
5. Capability to assign of confidence values
6. Cost-effective alternative to human expert
********** 9 **********
````

## 2024-25 · Final-Exam · Sem 3 · Answer key · paper 21b346d199fe

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_03/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Artificial Intelligence/ANS_Artificial Intelligence(703CO0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2024
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: 2024-2025)
Subject: Artificial Intelligence
Date: 04 Dec 2024   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 10 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Define admissibility and consistency in the context of heuristic functions
b.   Write out the truth table for (A→B)∧(B∧C→A).
A B C A→B B∧C B∧C→A (A→B)∧(B∧C→A)
T T T T   T   T   T
T T F T   F   T   T
T F T F   F   T   F
T F F F   F   T   F
F T T T   T   F   F
F T F T   F   T   T
F F T T   F   T   T
********** 1 **********
--- page 2 ---
F F F T   F   T   T
c.   Solve : TWO + TWO = FOUR
938+938=1876
d.   Define supervised learning and explain its key characteristics.
Supervised learning is a category of machine learning that uses labeled
datasets to train algorithms to predict outcomes and recognize patterns.
Unlike unsupervised learning, supervised learning algorithms are given
labeled training to learn the relationship between the input and the
outputs.
a. Explain the properties of Fully Observable vs. Partially
Observable environments in AI. Provide real-world examples of
AI systems operating in both types of environments and discuss
how the environment impacts the agent’s behavior.
Fully Observable Environments:
•   Properties:
1. The agent has access to all relevant information about
the environment at any point in time.
2. The agent does not need to infer or guess any missing
information.
3. Decision-making is easier as the agent has complete
Q2
knowledge.   [20]
• Examples:
1. Chess playing AI (e.g., Deep Blue)
2. Autonomous car in a controlled simulation
• Impact on Agent Behavior:
1. Enables optimal decision-making.
2. Reduces the need for memory or complex inference.
Partially Observable Environments:
•   Properties:
1. The agent only has incomplete or noisy information
about the environment.
********** 2 **********
--- page 3 ---
2. The agent must infer missing information or make
decisions based on uncertainty.
3. Often requires memory or sensors to compensate for the
lack of visibility.
• Examples:
1. Autonomous cars in real-world traffic
2. Poker-playing AI (where opponents' cards are hidden)
• Impact on Agent Behavior:
1. Agents must handle uncertainty and plan with
incomplete information.
2. Use of probabilistic models, inference, or sensors
becomes crucial.
b. Describe Hill Climbing search as a local search technique.
Discuss its limitations, such as local maxima, plateaus, and
ridges.
Hill climbing algorithm is a local search algorithm which continuously
moves in the direction of increasing elevation/value to find the peak of
the mountain or best solution to the problem. It terminates when it
reaches a peak value where no neighbor has a higher value.
Hill climbing algorithm is a technique which is used for optimizing the
mathematical problems. One of the widely discussed examples of Hill
climbing algorithm is Traveling-salesman Problem in which we need to
minimize the distance traveled by the salesman. It is also called greedy
local search as it only looks to its good immediate neighbor state and
not beyond that. A node of hill climbing algorithm has two components
which are state and value. Hill Climbing is mostly used when a good
heuristic is available.
Problems in Hill Climbing Algorithm:
1. Local Maximum: A local maximum is a peak state in the landscape
which is better than each of its neighboring states, but there is another
state also present which is higher than the local
maximum.Solution: Backtracking technique can be a solution of the
********** 3 **********
--- page 4 ---
local maximum in state space landscape. Create a list of the promising
path so that the algorithm can backtrack the search space and explore
other paths as well.
2. Plateau: A plateau is the flat area of the search space in which all
the neighbor states of the current state contains the same value,
because of this algorithm does not find any best direction to move. A
hill-climbing search might be lost in the plateau area.
Solution: The solution for the plateau is to take big steps or very little
steps while searching, to solve the problem. Randomly select a state
which is far away from the current state so it is possible that the
algorithm could find non-plateau region.
3. Ridges: A ridge is a special form of the local maximum. It has an area
which is higher than its surrounding areas, but itself has a slope, and
cannot be reached in a single move.
Solution: With the use of bidirectional search, or by moving in
different directions, we can improve this problem.
a. Given the following graph, use the A* search algorithm to find
the shortest path from the start node S to the goal node G. The
numbers on the edges represent the actual cost (g), and the
numbers next to each node represent the heuristic (h) values
for the estimated cost to the goal.
3
S ----------- A (h=5)
|   |
Q3
2 |   2   |   [20]
|   |
B (h=4) C (h=2)
|   |
6 |   3   |
|   |
D (h=3) G (h=0)
********** 4 **********
--- page 5 ---
Heuristics (h):
•   S: 6, A: 5, B: 4, C: 2, D: 3, G: 0
1. Calculate the f(n) = g(n) + h(n) values for each node.
2. Use A* search to find the path from S to G with the
minimum total cost.
The path from S → B → A → C → G has a total cost of 8.
b. Using the same graph from the A* example above, perform a
Greedy Best-First Search (GBFS) from node S to node G. The
numbers next to the nodes represent the heuristic (h) values.\
The path from S → B → D → G is chosen based only on the heuristic
values, without considering the actual cost. However, this path may not
be optimal in terms of cost, as the total cost for this path is 11, whereas
the optimal cost from the A* search is 8.
a. Compare Forward Chaining and Backward Chaining as inference
techniques in First-Order Logic.
Aspect   Forward Chaining   Backward Chaining
Starts from known facts   Starts from the query (goal)
Inference
and applies rules to derive and works backward to find
Direction
new facts.   supporting facts.
Data-driven (bottom-up): Goal-driven (top-down): It
It looks at all known facts focuses on proving a
Approach   and iteratively applies   specific query by searching
Q4
rules to infer new   for supporting facts or   [20]
conclusions.   rules.
Begins with available facts Begins with a goal (query)
and uses inference rules   and works backward to find
Triggering
to discover all possible   facts or rules that support
consequences.   the goal.
Can be inefficient because More efficient for specific
it explores all possible   queries as it only searches
Efficiency
rules and facts, even those for information relevant to
not related to the query.   proving the goal.
********** 5 **********
--- page 6 ---
Best suited for scenarios
Best suited for goal-
where all possible
directed reasoning where a
conclusions need to be
Use Case   specific fact or conclusion
drawn from the available
needs to be verified (e.g.,
data (e.g., expert
diagnostic systems).
systems).
In a troubleshooting
In medical diagnosis,
system, starting with the
starting from symptoms
Example   problem and working
and facts to infer possible
backward to determine
diseases.
possible causes.
Stops once the goal is
Continues until no more   proven or all possible ways
Termination
new facts can be derived. to prove the goal have been
exhausted.
Smaller, more focused
Larger search space, as it
search space, as it only
Search Space may derive facts that are
searches paths that can
irrelevant to the query.
potentially satisfy the goal.
More efficient for single
High complexity for large   queries, but can face
Complexity   datasets, as every possible difficulties with large,
conclusion is explored.   complex rules or deep
recursion.
Production systems,   Prolog-based systems,
expert systems (e.g.,   diagnostic systems, and
Common
systems that need to   planning systems (e.g.,
Applications
derive all consequences of goal-oriented problem
known facts).   solving).
b. Consider the following facts:
1. If the project deadline is extended, more features will be added.
********** 6 **********
--- page 7 ---
2. If more features are added, the release date will be delayed.
3. The project deadline is extended.
Can you prove that the release date will be delayed? Construct a
resolution tree to determine if the query can be proven.
Delayed
/   \
FeaturesAdded   ¬FeaturesAdded ∨ Delayed
/
Extended
\
¬Extended ∨ FeaturesAdded
a. Define the key components of a Constraint Satisfaction Problem
(CSP). Give an example of a CSP.
Variables:
These are the unknowns that need to be assigned values in the
Q5
problem.   [20]
Example: In a Sudoku puzzle, each cell in the grid is a variable.
Domains:
Each variable has a set of possible values it can take, known as its
domain.
********** 7 **********
--- page 8 ---
Example: In Sudoku, the domain of each cell is the set {1, 2, 3, ..., 9},
representing the numbers that can be placed in the cell.
Constraints:
These define the relationships between variables and restrict the
combinations of values that the variables can take.
Example: In Sudoku, the constraint is that no two cells in the same row,
column, or 3x3 subgrid can have the same number.
b. Solve the following cryptarithmetic puzzle
C R O S S
+ R O A D S
-----------
D A N G E R
96755 + 60715 -------- 103470
a. Describe the K-means clustering algorithm. Explain how it
assigns data points to clusters and the importance of centroids
in this process.
Initialize K centroids randomly.
Assign each data point to the nearest centroid.
Update centroids by calculating the mean of assigned points.
Repeat steps 2 and 3 until centroids stabilize.
Centroids are crucial as they define the clusters and influence point
assignment.
Q6
b. Differentiate between forward & backward chaining rule system [20]
Difference Between Forward Chaining and Backward Chaining Rule
Systems
Aspect   Forward Chaining   Backward Chaining
Starts from known facts   Starts with the goal and
Inference
and applies rules to infer works backward to find
Direction
new facts.   supporting facts.
Approach   Data-driven (bottom-up). Goal-driven (top-down).
********** 8 **********
--- page 9 ---
Explores all possible   Focuses only on rules and
Focus   consequences of the   facts needed to prove the
known facts.   goal.
Stops when the goal is
Stops when no more new
Termination   proven or no more rules
facts can be inferred.
can apply.
May explore unnecessary More efficient for specific
Efficiency   facts not related to the   queries as it focuses only
goal.   on relevant facts.
Useful when all   Useful when a specific
Use Case   conclusions must be   query or goal needs to be
derived.   answered.
Expert systems (e.g.,   Diagnostic systems (e.g.,
Example
production systems).   Prolog-based systems).
a. Using PEAS as metrics explain the following environments:
1. Automated taxi driver
2. English tutor
1. Automated Taxi Driver
• Performance Measure:
o Safety (avoid accidents)
o   Efficiency (minimize time and fuel consumption)
o Comfort (smooth driving experience)
o Compliance (obey traffic rules)
• Environment:
o Roads, traffic, pedestrians, weather conditions, traffic signals,
Q7   passengers.
•   Actuators:   [20]
o   Steering, accelerator, brakes, indicators, wipers, lights.
•   Sensors:
o Cameras, LIDAR, GPS, speedometer, proximity sensors,
accelerometer, gyroscope.
2. English Tutor
• Performance Measure:
o Accuracy (correct explanations)
o Student engagement
o Improvement in student’s language skills
o Timeliness of feedback
• Environment:
o Students, curriculum, learning material, assessment tasks.
•   Actuators:
********** 9 **********
--- page 10 ---
o Screen display, voice responses, quizzes, hints, written
explanations.
•   Sensors:
o Keyboard inputs, microphone (for speech recognition),
student interaction tracking (e.g., mouse clicks, response
time), camera (for facial expressions).
b. List and explain in detail steps involved in NLP
Steps Involved in Natural Language Processing (NLP)
1. Tokenization:
o   Splitting the text into individual words or sentences.
2. Stop Word Removal:
o Removing common, irrelevant words (e.g., "and," "the").
3. Stemming/Lemmatization:
o Reducing words to their root form (e.g., "running" to "run").
4. POS Tagging (Part-of-Speech Tagging):
o   Identifying the grammatical role of each word (e.g., noun,
verb).
5. Named Entity Recognition (NER):
o   Identifying entities like names, dates, locations.
6. Parsing:
o Analyzing the grammatical structure of a sentence.
********** 10 **********
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 74496e465775

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/BTech_CSE_DS_7011/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C042)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 May 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Artificial Intelligence
Date: 03 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Question 1 is compulsory
4. Out of remaining questions, attempt any 4 questions
5. In all 5 questions to be attempted
6. All questions carry equal marks
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Artificial Intelligence - Answer Key(1)
Q1a) Define approaches/components of AI
The four approaches to Artificial Intelligence (AI) that you mentioned—thinking humanly, acting
humanly, thinking rationally, and acting rationally—were popularized by philosopher and AI
researcher John McCarthy. These approaches offer different perspectives on how AI systems can be
designed to emulate or simulate human behavior and intelligence. Here's a breakdown of each:
1. Thinking Humanly
•   Definition: This approach involves designing AI systems that mimic human cognitive processes,
i.e., they try to simulate the way humans think, reason, and understand the world.
• Goal: The goal is to create machines that reason and solve problems in ways similar to human
minds. This involves modeling the processes of human thought, such as perception, learning,
memory, and decision-making.
• Example: Cognitive modeling, which attempts to replicate how the brain processes information,
including symbolic AI and neural networks that try to mimic human brain structures.
• Challenges: Since human cognition is highly complex and not fully understood, creating a
model that closely mirrors human thinking is a difficult task.
2. Acting Humanly
•   Definition: In this approach, AI systems are designed to perform tasks in a way that appears
human-like, regardless of whether their internal processes are similar to human thought.
• Goal: The goal is for AI to exhibit behaviors that humans can recognize as intelligent, such as
understanding natural language, interpreting visual data, and making decisions.
• Example: Turing Test, where an AI system interacts with a human and must convince the
human that it is also human. Chatbots and virtual assistants (like Siri or Alexa) aim to act
humanly by conversing in natural language.
********** 1 **********
--- page 2 ---
• Challenges: Achieving "human-like" behavior can be very challenging because it involves
replicating subtle, complex social cues and behaviors, such as empathy, humor, and non-verbal
communication.
3. Thinking Rationally
•   Definition: This approach is about creating AI systems that reason in a logically correct way,
based on principles of rationality. Rational thinking involves making decisions that maximize the
chance of achieving desired goals, given the information available.
• Goal: The objective here is to model reasoning in a way that is purely logical and optimal. The
system should always choose the most rational decision based on the information it has, much
like a human or machine would use logic and deductive reasoning to solve problems.
• Example: Logic-based systems, such as those used in automated theorem proving, where AI
attempts to prove mathematical theorems using formal logic.
• Challenges: Rational thinking can sometimes ignore the nuances of real-world situations, such
as emotions or irrational human behavior, which could make purely rational agents seem out of
place in certain social contexts.
4. Acting Rationally
•   Definition: This approach focuses on AI systems that take the most appropriate actions to
achieve a given goal, based on available information and the current situation. It's more about
"doing the right thing" rather than simulating human-like thinking.
• Goal: The goal here is not to mimic human behavior, but to act in a way that is most likely to
lead to success in achieving the desired outcomes.
• Example: A self-driving car that must make decisions in real-time to navigate traffic safely and
efficiently. Robots that perform tasks like assembly or surgery based on their programmed goals
are also examples of acting rationally.
• Challenges: Defining the "right" actions can sometimes be subjective and highly dependent on
the context, as it may involve trade-offs, ethical considerations, or unpredictable variables.
Summary of the Four Approaches:
1. Thinking Humanly: Focuses on simulating human cognitive processes.
2. Acting Humanly: Focuses on mimicking human-like behavior.
3. Thinking Rationally: Focuses on logical, optimal reasoning.
4. Acting Rationally: Focuses on choosing the best actions to achieve goals, regardless of how
they resemble human thinking or behavior.
Each approach has its unique strengths and applications. The distinction between them highlights
different ways AI can be designed to understand, interact with, and operate in the world.
********** 2 **********
--- page 3 ---
Q1b Define PEAS components of Automatic Water Dispensor
The PEAS (Performance measure, Environment, Actuators, and Sensors) framework is used to define
the components of an intelligent agent. It helps to clearly outline the key elements involved in the
design and functionality of the agent for a given task. For an automatic water dispenser, the PEAS
components can be defined as follows:
1. Performance Measure
• The performance measure defines how the success of the automatic water dispenser will be
evaluated. For an automatic water dispenser, key performance metrics might include:
o Water dispensing accuracy: The ability to dispense the correct amount of water as
requested.
o Response time: How quickly the dispenser responds to a user's request.
o Reliability: Consistency in the dispenser's performance over time.
o User satisfaction: Whether the user receives the expected amount of water and the
experience is pleasant (e.g., no spills or overflows).
o Energy efficiency: The system’s ability to minimize energy consumption while
dispensing water.
2. Environment
• The environment refers to everything that the automatic water dispenser interacts with or
operates within. For this system, the environment includes:
o The user: The person requesting water.
o The water container: The source of water, which can be a tank or a bottle.
o The dispensing area: The location where the water is dispensed (e.g., a cup, bottle, or
other containers).
o External conditions: Any factors that affect the dispensing process, such as the
temperature of the water, water pressure, or possible blockages.
3. Actuators
• Actuators are the components of the automatic water dispenser that carry out actions based on
the agent's decisions. For an automatic water dispenser, the actuators may include:
o Water pump or valve: Controls the flow of water from the source to the dispensing
outlet.
o Motors: To move the mechanism that positions the water container (e.g., for refilling or
aligning the container).
o Heating/cooling system: If the dispenser includes temperature control (e.g., to heat or
cool the water).
o Display or indicator: A light or screen that shows the status of the dispenser, such as
"Ready" or "Low Water Level."
********** 3 **********
--- page 4 ---
4. Sensors
• Sensors provide feedback from the environment to the agent. They detect various conditions and
send data to the system, enabling it to make informed decisions. For the automatic water
dispenser, common sensors might include:
o Water level sensor: Detects the amount of water left in the container to ensure proper
dispensing and prevent overflow.
o Proximity or motion sensor: Detects when a user is near the dispenser, triggering the
water dispensing action.
o Flow sensor: Monitors the rate and amount of water dispensed, ensuring that the correct
quantity is delivered.
o Temperature sensor: Measures the temperature of the water to control the heating or
cooling system.
o Overflow sensor: Ensures the dispenser does not overflow by detecting the level of water
in the container being filled.
Summary of PEAS for Automatic Water Dispenser:
1. Performance Measure:
o Water dispensing accuracy
o Response time
o   Reliability
o User satisfaction
o Energy efficiency
2. Environment:
o The user
o Water container
o Dispensing area
o External conditions (temperature, pressure)
3. Actuators:
o Water pump or valve
o Motors for positioning
o Heating/cooling system
o Display or indicator lights
4. Sensors:
o Water level sensor
o Proximity or motion sensor
o Flow sensor
o Temperature sensor
o Overflow sensor
This PEAS framework helps to understand the functionality of the automatic water dispenser and the
components involved in its operation.
Q1c: Explain Agent structure. Give example of at least two types of agents
Agent Structure
An agent in artificial intelligence (AI) is an entity that perceives its environment through sensors and
acts upon it using actuators. The agent structure consists of the following components:
1. Perception (Sensors): Gathers information from the environment (e.g., cameras, microphones,
or software logs).
********** 4 **********
--- page 5 ---
2. Agent Function: Maps perceptions to actions based on a predefined function.
3. Agent Program: The implementation of the agent function that determines how the agent
behaves.
4. Actuators: Execute actions based on the agent’s decisions (e.g., robotic arms, displays, or
software commands).
5. Environment: The world or system in which the agent operates.
Types of Agents with Examples
1. Simple Reflex Agent
o These agents make decisions solely based on the current percepts, without considering
past actions.
o They follow condition-action rules (if-then rules) to respond to specific inputs.
o Example: A thermostat that turns on a heater if the temperature drops below a set
threshold.
2. Learning Agent
o These agents improve their performance over time by learning from past experiences.
o They have a learning element that updates their decision-making based on feedback.
o Example: A recommendation system (e.g., Netflix or Spotify) that suggests movies or
songs based on a user’s past preferences and feedback.
Would you like more details on other agent types, such as goal-based or utility-based agents? 😊
Q1d Define Heuristic function and Heuristic Value
Heuristic Function
A heuristic function is a method used in artificial intelligence (AI) and search algorithms to estimate
the cost or distance from the current state to the goal state. It helps guide the search process efficiently
by providing an educated guess rather than an exact solution.
•   It is denoted as h(n), where n is a node (state) in the search space.
• A good heuristic function reduces the number of nodes explored, improving search efficiency.
•   It is commonly used in informed search algorithms like A* and Greedy Best-First Search.
Example:
In the 8-puzzle problem, a heuristic function could be:
1. h₁(n) = Number of misplaced tiles
2. h₂(n) = Sum of Manhattan distances (total horizontal and vertical distance of tiles from
their goal positions)
Heuristic Value
The heuristic value is the numerical estimate returned by the heuristic function for a specific state. It
represents how far a given state is from the goal.
• Lower heuristic values usually indicate states that are closer to the goal.
•   In A search*, the evaluation function is f(n) = g(n) + h(n), where:
********** 5 **********
--- page 6 ---
o g(n) = Cost from the start state to node n
o h(n) = Heuristic value (estimated cost to goal)
Example:
If a heuristic function h(n) in a navigation problem estimates that a city is 200 km away from the
destination, then the heuristic value for that state is 200.
Would you like an example of how heuristic values are used in a real-world search algorithm? 😊
Q2: Differentiate between Informed and Uninformed search
Difference Between Informed and Uninformed Search
Feature   Informed Search   Uninformed Search
Uses heuristics (extra knowledge) to   Explores the search space blindly, without
Definition
find the goal efficiently.   additional domain knowledge.
Heuristic   Uses a heuristic function h(n) to
No heuristic function is used.
Function   estimate the cost to the goal.
More efficient as it explores fewer   Less efficient as it may explore many
Efficiency
nodes.   unnecessary nodes.
Breadth-First Search (BFS), Depth-First
Examples   A* Search, Greedy Best-First Search
Search (DFS)
Finds the goal faster by prioritizing   May take longer as it searches systematically
Goal Discovery
promising paths.   without prioritization.
Space   Can be lower due to heuristic
Can be high, depending on the search strategy.
Complexity   guidance.
Example for Each
1. Informed Search (A Algorithm)*
o Used in Google Maps to find the shortest route based on real-time traffic data.
2. Uninformed Search (BFS)
o Used in solving a maze by exploring all paths level by level until the exit is found.
Would you like a practical coding example of either search type? 😊
Q3: Explain any 2 supervised learning method used in AI
Two Supervised Learning Methods in AI
Supervised learning is a type of machine learning where an algorithm learns from labeled training data,
meaning each input has a corresponding correct output.
1. Linear Regression
Purpose: Used for predicting continuous numerical values.
How It Works:
********** 6 **********
--- page 7 ---
•   Establishes a linear relationship between input (features) and output (target variable).
• Uses the equation:
Y=mX+bY = mX + b
where:
o YY = predicted output
o XX = input feature
o mm = slope (weight)
o bb = intercept
• The model minimizes the Mean Squared Error (MSE) to find the best-fit line.
Example:
• Predicting house prices based on features like size, location, and number of bedrooms.
2. Support Vector Machine (SVM)
Purpose: Used for classification and regression tasks.
How It Works:
• Finds the optimal decision boundary (hyperplane) that maximizes the margin between different
classes.
• Works well in high-dimensional spaces and with small datasets.
• Uses kernel tricks to handle non-linearly separable data.
Example:
• Spam detection: Classifies emails as "Spam" or "Not Spam" based on email content and
metadata.
Would you like a real-world coding example for any of these? 😊
Q4: Write a Pseudo-code to design an application which counts number of people entering in Mall
Pseudo-code for Mall Entry Counter Application
BEGIN
INITIALIZE person_count = 0
DISPLAY "Mall Entry Counter Started"
WHILE mall_is_open DO
IF sensor_detects_entry THEN
INCREMENT person_count
DISPLAY "Person Entered: Total Count = ", person_count
ENDIF
IF sensor_detects_exit THEN
DECREMENT person_count
DISPLAY "Person Exited: Total Count = ", person_count
********** 7 **********
--- page 8 ---
ENDIF
WAIT for next sensor input
ENDWHILE
DISPLAY "Mall is Closed. Final Count: ", person_count
END
Explanation:
1. Initialize the person counter to zero.
2. Continuously monitor the entry and exit sensors while the mall is open.
3. Increase the count when a person enters.
4. Decrease the count when a person exits.
5. Display real-time updates on the screen.
6. Stop counting when the mall closes and display the final count.
Would you like a real Python implementation of this logic? 😊
Q5: Explain the use cases of segmentation in AI
Use Cases of Segmentation in AI
Segmentation in AI refers to dividing data (images, text, or customer groups) into meaningful parts for
better analysis and decision-making. It is widely used in various domains:
1. Image Segmentation (Computer Vision)
•   Definition: Divides an image into regions to identify objects or patterns.
• Use Cases:
o Medical Imaging: Helps in tumor detection by segmenting CT scans and MRIs.
o Autonomous Vehicles: Identifies roads, pedestrians, and obstacles.
o Facial Recognition: Segments different facial features for authentication.
2. Customer Segmentation (Marketing & Business Analytics)
•   Definition: Groups customers based on behavior, demographics, or preferences.
• Use Cases:
o Targeted Advertising: Companies like Amazon and Netflix recommend products based
on user segments.
o Churn Prediction: Identifies customers likely to leave a service.
o Pricing Strategy: Adjusts pricing based on customer segments.
3. Text Segmentation (Natural Language Processing - NLP)
•   Definition: Breaks text into meaningful chunks for better processing.
• Use Cases:
o Chatbots & Virtual Assistants: Segments user queries to understand intent.
o Document Summarization: Separates key sections for quick insights.
********** 8 **********
--- page 9 ---
o Sentiment Analysis: Segments reviews to analyze opinions in different parts of a
document.
4. Instance Segmentation (AI & Robotics)
•   Definition: Identifies individual objects in an image separately, even if they overlap.
• Use Cases:
o Retail Automation: AI-powered checkout systems (e.g., Amazon Go) recognize
individual items.
o Agriculture: Detects and counts crops or diseased plants.
o Manufacturing: Segments defective products in a quality control process.
Would you like a detailed explanation of any specific use case? 😊
Q6: Define Local Maxima and Simulated Annealing. Explain, in which algorithm, we face these
challenges
Local Maxima and Simulated Annealing
1. Local Maxima
•   Definition: A local maximum is a state in an optimization problem where the function value is
higher than its neighboring states but not the highest overall (global maximum).
• Problem: When an algorithm reaches a local maximum, it may get stuck and fail to find the
optimal solution.
Example:
•   In hill climbing search, if an algorithm reaches a peak that is lower than the global maximum, it
stops improving, leading to suboptimal results.
2. Simulated Annealing
•   Definition: Simulated Annealing is an optimization technique that helps overcome local
maxima by allowing occasional downhill moves (temporary bad decisions) to escape local
optima and explore better solutions.
• How It Works:
o   Starts with a high "temperature" (probability of accepting worse solutions).
o Gradually cools down, reducing the chance of accepting worse solutions over time.
o This prevents the algorithm from getting stuck in local maxima.
Example:
•   In traveling salesman problem (TSP), simulated annealing helps avoid being stuck in a non-
optimal route by allowing random jumps in early stages.
Algorithms Facing These Challenges
1. Local Maxima Problem Occurs In:
********** 9 **********
--- page 10 ---
o Hill Climbing Algorithm (Gradient Descent in some cases)
o Greedy Best-First Search
2. Simulated Annealing is Used In:
o Optimization Algorithms (e.g., TSP, scheduling problems)
o Machine Learning Hyperparameter Tuning
Would you like a simple Python example of simulated annealing? 😊
Q7: Solve the following problem using Uniform cost search method and calculate total cost
Solving the Uniform Cost Search (UCS) for the Given Graph
Graph Representation (from Image)
Each node represents a state, and edges have associated costs:
(S)
/   \
1/   \12
/   \
(A)------(G)
|
3|
|
(B)
|
3|
|
(D)
|
3|
|
(G)
Another path:
(S) → (C) (Cost = 1)
(C) → (D) (Cost = 1)
(C) → (G) (Cost = 2)
(D) → (G) (Cost = 3)
********** 10 **********
--- page 11 ---
Step-by-Step UCS Execution
1. Initialize Priority Queue:
Start at S with cost 0.
Node Path Cost
S   S   0
2. Expand Node S:
• S → A (Cost = 1)
• S → G (Cost = 12)
• S → C (Cost = 1)
Queue:
Node Path Cost
A   S → A 1
C   S → C 1
G   S → G 12
3. Expand Node A (lowest cost = 1):
• A → B (Cost = 1 + 3 = 4)
• A → C (Cost = 1 + 1 = 2)
Queue:
Node   Path   Cost
C   S → C   1
C   S → A → C 2
B   S → A → B 4
G   S → G   12
4. Expand Node C (lowest cost = 1):
• C → D (Cost = 1 + 1 = 2)
• C → G (Cost = 1 + 2 = 3)
Queue:
Node   Path   Cost
C   S → A → C 2
D   S → C → D 2
G   S → C → G 3
B   S → A → B 4
G   S → G   12
5. Expand Node C (lowest cost = 2, second occurrence ignored since we already expanded C
earlier):
Queue remains:
Node   Path   Cost
D   S → C → D 2
********** 11 **********
--- page 12 ---
Node   Path   Cost
G   S → C → G 3
B   S → A → B 4
G   S → G   12
6. Expand Node D (lowest cost = 2):
• D → G (Cost = 2 + 3 = 5)
Queue:
Node   Path   Cost
G   S → C → G   3
B   S → A → B   4
G   S → C → D → G 5
G   S → G   12
7. Expand Node G (lowest cost = 3, found goal state!)
• Optimal Path: S → C → G
• Total Cost: 3
Final Answer:
🔹 Optimal Path: S → C → G
🔹 Total Cost: 3
Would you like a Python implementation of UCS for this? 😊
********** 12 **********
````

## 2024-25 · Re-Exam · Sem 2 · Answer key · paper a3502c5c3b0a

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Artificial Intelligence/ANS_Artificial Intelligence(703CO0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2025
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 2 Re-exam(Exam Year: 2024-2025)
Subject: Artificial Intelligence
Date: 04 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 9 pages.
2. Question No. _1_ is compulsory.
3. Out of remaining questions, attempt any _4_ questions.
4. In all _5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly:
a.   Differentiate between informed and uninformed searching with example   [05]
Ans.
It uses knowledge for the searching   It doesn’t use knowledge for the
process. (Heuristics)   searching process. (Blind)
It finds solution slow as compared
It finds a solution more quickly.
to an informed search.
It may or may not be complete.   It is always complete.
Cost is low.   Cost is high.
CO-
2;
BL-   There is a direction given about the   No suggestion is given regarding
solution.   the solution in it.
Having a wide scope in terms of   Solving a massive search task is
handling large search problems.   challenging.
• Greedy Search
• Depth First Search (DFS)
•   A* Search
•   Breadth First Search (BFS)
• AO* Search
• Branch and Bound
•   Hill Climbing Algorithm
CO-   b.
3 ;   Discuss the significance of expert system shell in building expert systems.
BL-
********** 1 **********
--- page 2 ---
Ans.   • Need not to build the expert system from the start, it provide the framework.
• An Expert system shell is a software development environment. It contains the
basic components of expert systems.
• A shell is associated with a prescribed method for building applications by
configuring and instantiating these components.
CO-   c.   Discuss the problem solving by searching with necessary steps followed in problem
2 ;   [05]
BL-   formulation.
Ans.
Discussion on problem solving by searching [2M]
Problem formulation with example [3M]
CO-   d.
1;   Discuss the model based agent with suitable example   [05]
BL-
Ans. Discussion on agent [4M]
********** 2 **********
--- page 3 ---
Mars Lander: Example [1M]
1. Can pick up the stone sample from the surface around it, then it is normal
2. Or remove supporting rock under ledge then what? Fact : if removed them rock
will fall on the agent (Model)
a.   Apply and discuss that A* is optimal tree search algorithm for the following problem
and obtain optimum cost path from node C to G. Use given table as heuristics (straight
line distances).
Q2
[10]
CO-2;   Nodes   SLD
BL-
A   25
B   15
C   35
D   16
E   28
F   14
G   0
Ans. Optimality test [3M]
• A heuristic h(n) is admissible if for every node n,
h(n) ≤ h*(n), where h*(n) is the true cost to reach the goal state from n.
• An admissible heuristic never overestimates the cost to reach the goal, i.e., it
is optimistic
•   Example: hSLD(n) (never overestimates the actual road distance)
•   Theorem: If h(n) is admissible, then A* using TREE-SEARCH is optimal
Generating the solution tree with discussion on each step [7M]
b.   Explain the significance of PEAS for intelligent agent. Give the PEAS description for the
CO-1;   following agents
10
BL-   1   Medical diagnosis system
2   Wompus world problem
Ans. Significance of PEAS [3M]
Suggested: PEAS for Medical diagnosis system [3M]
•   Performance measure: Accurate diagnosis.
•   Environment: GUI.
•   Sensors: keyboard, mic.
•   Actuators: speaker, printer.
PEAS for Wompus world problem [4M]
********** 3 **********
--- page 4 ---
•   Performance measure
– gold +1000, death -1000
–   -1 per step, -10 for using the arrow
•   Environment
– Squares adjacent to wumpus are smelly
– Squares adjacent to pit are breezy
–   Glitter iff gold is in the same square
– Shooting kills wumpus if you are facing it
– Shooting uses up the only arrow
– Grabbing picks up gold if in same square
–   Releasing drops the gold in same square
•   Sensors: Stench, Breeze, Glitter, Bump, Scream
•   Actuators: Left turn, Right turn, Forward, Grab, Release, Shoot
Q3   a.   Explain the application of Hill climbing searching method to solve 8-queen problem.
[10]
CO-2;   Discuss types of problem occurs during implementation of search.
BL-
Ans. Application of Hill climbing as landscape for 8 queen problem
Probable tree structure of 8 queen problem: [6M]
Problems : Local maxima, Ridge, Plateau [4M]
CO-1;   b.
Explain the functioning of Learning Agent with suitable example.
BL-
Ans. Diagram and description [7M]
1. Sensors: Sensors collect information from the environment and send it to the
agent, allowing for decision-making and acquisition of knowledge.
2. Critic: The critic assesses and offers feedback on the agent's performance based
on pre-established goals or a predetermined reward system. The critic supports
the learner by providing feedback on the quality of their decisions, allowing
them to enhance their skills through various activities.
********** 4 **********
--- page 5 ---
3. Learning Element: This part acts as the central cognitive hub of the agent,
responsible for analyzing the experiences acquired from interactions with the
surroundings.
4. Performance Element: The performance element requires the learning element
and critic feedback so as to manage the agent's activities in an environment.
5. Actuators: Actuators, also called effectors, carry out tasks selected by the
performance element
6. Problem Generator: The problem generator is in charge of creating challenges
or activities for the agent to complete. It consists of situations that require the
agent to apply the knowledge and skills it has gained, hence improving ongoing
learning and talent development.
Example[3M]
Q4   a.   Discuss any suitable AI problem, with respect to search space and searching strategies
[05]
CO-2;   to obtain solution
BL-
Ans. Water jug problem or finding shortest path problem can be discussed. [2 M]
Discussion on search space and searching strategies [3M}
b.   Create a knowledgebase for the following sentences using first order predicate logic.
1   Marcus was a man
2   Marcus was a Pompeian
3   All Pompeian were Romans
CO-3;
4   Caesar was a ruler   [15]
BL-   5   All Romans were either loyal to Caesar or hated him
6   Everyone is loyal to someone
7   People only try to assassinate ruler they are not loyal to
8   Marcus tried to assassinate Caesar
Using resolution method answer the query: “Was Marcus loyal to Caesar?
Ans. Converting sentences to WFF [5M]
Converting WFF to CNF [5M]
********** 5 **********
--- page 6 ---
Proof [5M]
a.   Apply the forward chaining method to find if Christena is healthy or sick. Following is
the given information:
Q5
If food is oily it is good in taste and not good for health. If anyone eats unhealthy food   [10]
CO-3;
BL-   they fall sick. Christena loves oily food and she eats only what she loves. “Potato
wedges” is an oily food item.
Ans. Convert to FOPL [5M]
********** 6 **********
--- page 7 ---
Proof by forward chaining with each step [5M]
CO-3;   b.   What is constraint satisfaction problem? Explain with the help of Graph Coloring
[10]
BL-   problem.
Ans. Explanation on SCP [4M]
Explanation with graph colouring problem [6M]
a.   What do you mean by supervised learning? Apply a decision tree based classification
Q6   algorithm on following data.
[20]
CO-4;   X1 X2 Class
BL-
2   1.5 1
********** 7 **********
--- page 8 ---
2   3   1
4   4   1
3   2   -1
3   3   -1
4   2.5 -1
Ans. Explanation on supervised learning [2M}
Representation using scatter plot [2M]
Accurate decision tree [6M]
CO-2;   b.   Explain the local searching method used in Constraint Satisfaction problem with an
BL-   example.
Ans.   1. To apply to CSPs: [4M]
a. allow states with unsatisfied constraints
b. operators reassign variable values
2. Variable selection: randomly select any conflicted variable
3. Value selection by min-conflicts heuristic:
a. choose value that violates the fewest constraints
b.   i.e., hill-climb with h(n) = total number of violated constraints
N-Queen problem can be an example : [6M]
Q7   a.
Explain the method of inductive learning. Give suitable example.   [20]
CO-4;
BL-
Ans.   • The inductive learning is a process of learning by example. The system tries to
induce a general rules from a set of observed instances. The learning methods
extract rules and patterns out of massive data sets.
• The learning processes belong to supervised learning, does classification and
constructs class definitions, called induction or concept learning.
•   Simplest form: learn a function from examples
f is the target function
An example is a pair (x, f(x))
Problem: find a hypothesis h
such that h ≈ f
given a training set of examples
(This is a highly simplified model of real learning:
–   Ignores prior knowledge
– Assumes examples are given
********** 8 **********
--- page 9 ---
Explanation on learning example with different models [5M]
b.   What is Expert system? Draw and explain the generalize architecture of an Expert
CO-3;
System with example.
BL-
Ans. Architecture and explanation [10M]
********** 9 **********
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper 813c6a01f2e6

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/BTech_CSE_DS_7011/Artificial Intelligence/ANS_Artificial Intelligence(702CO0C042)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Jul 2025
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Artificial Intelligence
Date: 05 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Question 1 is compulsory
4. Out of remaining questions, attempt any 4 questions
5. In all 5 questions to be attempted
6. All questions carry equal marks
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Artificial Intelligence - Answer Key (2)
Q1a Define role of Mathematics and Economics in Artificial Intelligence.
Role of Mathematics and Economics in Artificial Intelligence (AI)
Artificial Intelligence (AI) is deeply rooted in Mathematics and Economics, as both fields provide
essential theories and models that drive AI decision-making, optimization, and learning processes.
1. Role of Mathematics in AI
Mathematics provides the foundation for AI algorithms, enabling machines to learn, make predictions,
and solve problems efficiently.
Key Mathematical Concepts in AI:
Mathematical
Role in AI   Example
Area
Used for vector operations, matrices, and   Image processing in
Linear Algebra   tensors, which are crucial for neural networks   Convolutional Neural Networks
and deep learning.   (CNNs).
Probability &   Helps in making predictions, handling   Bayesian Networks, Hidden
Statistics   uncertainty, and probabilistic reasoning.   Markov Models (HMM).
Used in optimization techniques like Gradient   Backpropagation in Deep
Calculus
Descent for training machine learning models.   Learning.
Helps in minimizing error functions and   Support Vector Machines
Optimization
improving AI efficiency.   (SVMs), Reinforcement Learning.
Essential for network analysis, decision trees,   Google PageRank Algorithm,
Graph Theory
and search algorithms.   Social Network Analysis.
********** 1 **********
--- page 2 ---
2. Role of Economics in AI
Economics plays a crucial role in AI, particularly in decision-making, game theory, and resource
allocation. Many AI applications use economic principles to model rational behavior, incentives, and
utility maximization.
Key Economic Concepts in AI:
Economic
Role in AI   Example
Theory
Models competitive and cooperative   Multi-Agent AI Systems, Self-Driving
Game Theory
decision-making among agents.   Cars Negotiating Traffic.
AI agents use utility functions to make   Recommendation Systems (Netflix,
Utility Theory
optimal decisions.   Amazon).
AI optimizes pricing and bidding strategies Online Ad Auctions (Google Ads),
Market Design
in e-commerce and stock trading.   Stock Market Predictions.
Mechanism   Helps in designing rules for AI-driven   Ride Pricing in Uber, Task Allocation in
Design   auctions, contracts, and social choices.   AI.
Decision   Guides AI in making rational choices under
Autonomous Robots, AI in Healthcare.
Theory   uncertainty.
Conclusion:
Mathematics powers AI algorithms, while Economics guides AI decision-making and strategy.
Together, they enable AI to learn, predict, optimize, and make rational decisions in various real-
world applications.
Would you like a deeper dive into any specific topic? 😊
Q1b What are the components of Rational Agents? Define with example
Components of a Rational Agent in AI
A rational agent is an intelligent entity that perceives its environment and takes actions to achieve the
best possible outcome based on available knowledge and goals.
Key Components of a Rational Agent:
Component   Definition   Example
The agent collects data from its   A self-driving car uses cameras,
Perception (Sensors)
environment.   LiDAR, and GPS to sense traffic.
Stores information about the
A chess-playing AI stores past game
Knowledge Base   environment, rules, and learned
moves and strategies.
experiences.
Decision-Making   Uses algorithms to analyze data and A chatbot processes user queries and
(Reasoning & Logic)   determine the best action.   selects the best response.
Learning (Machine   Improves decision-making based on A recommendation system learns
Learning Component)   past experiences and feedback.   user preferences over time.
Action (Actuators or   Executes the chosen action in response A robotic arm picks up an object
Output Mechanism)   to environmental input.   after processing visual input.
********** 2 **********
--- page 3 ---
Example: Rational Agent in a Self-Driving Car
1. Perception: Uses cameras, LiDAR, GPS, and sensors to detect roads, traffic signals, and
obstacles.
2. Knowledge Base: Knows speed limits, traffic rules, and past driving experiences.
3. Decision-Making: Uses AI algorithms to determine whether to stop, accelerate, or turn based
on real-time data.
4. Learning: Improves driving based on past experiences, adjusting to different driving conditions.
5. Action: Controls steering, braking, and acceleration to ensure safe driving.
A rational agent always chooses the best action to maximize success in achieving its goal.
Would you like a Python example of a simple rational agent? 😊
Q1c Explain With the help of diagram – Goal Based Agents
Goal-Based Agents in AI
Definition:
A goal-based agent is an intelligent system that takes actions to achieve a specific goal rather than just
reacting to inputs. It evaluates different possible actions and chooses the one that brings it closer to
the goal.
Key Components of a Goal-Based Agent:
1. Perception (Sensors): Collects information from the environment.
2. Knowledge Base: Stores information about the environment and past experiences.
3. Goal Information: Defines the desired outcome or target state.
4. Reasoning & Decision-Making: Evaluates different actions and selects the best one.
5. Action (Actuators): Performs actions that move the agent towards achieving the goal.
Example: Goal-Based Agent in a Self-Driving Car
• Perception: Detects road, traffic lights, obstacles, and other vehicles.
********** 3 **********
--- page 4 ---
• Knowledge Base: Stores past driving experience, road maps, and traffic rules.
• Goal Information: The destination set by the user (e.g., reaching "City B").
• Decision-Making: Chooses the best route, avoids obstacles, follows speed limits.
• Action Execution: Controls the car’s acceleration, braking, and steering.
👉 Unlike simple reflex agents, goal-based agents think ahead and make decisions based on future
consequences!
Would you like a real-world AI implementation example? 😊
Q1d What are the uses of Classification algorithms in application in AI
Uses of Classification Algorithms in AI Applications
Classification algorithms are a type of Supervised Learning used in AI to categorize data into
predefined classes or labels. They play a crucial role in various real-world applications across different
industries.
🔹 Applications of Classification Algorithms
1. Healthcare & Medical Diagnosis 🏥
📌 Use: Predict diseases based on symptoms and medical records.
📌 Example:
• Disease Prediction: Classify if a patient has diabetes (Yes/No) using logistic regression.
• Tumor Detection: Identify whether a tumor is malignant or benign using SVM.
2. Spam Detection in Emails 📧
📌 Use: Classify emails as Spam or Not Spam using text-based features.
📌 Example Algorithms:
• Naïve Bayes (commonly used in spam filters).
• Random Forest & Decision Trees for improving accuracy.
3. Fraud Detection in Finance 💰🔍
📌 Use: Identify fraudulent transactions in banking and credit card usage.
📌 Example:
• Credit Card Fraud Detection: Classify transactions as legitimate or fraudulent using Random
Forest.
• Loan Default Prediction: Determine whether a person is likely to default on a loan using
Logistic Regression.
********** 4 **********
--- page 5 ---
4. Image Recognition & Computer Vision 🖼️👀
📌 Use: Classify objects, faces, or handwritten digits in images.
📌 Example:
• Facial Recognition: Identify people in photos using Deep Learning (CNNs).
• Handwritten Digit Recognition: Classify numbers (0-9) using Neural Networks (used in postal
services).
5. Sentiment Analysis in Social Media & Customer Feedback 💬😊😡
📌 Use: Analyze customer reviews and classify them as positive, negative, or neutral.
📌 Example:
• Twitter Sentiment Analysis: Classify tweets as happy, angry, or sad using Support Vector
Machines (SVM).
• Product Reviews: Determine if customer feedback is positive or negative using Naïve Bayes.
6. Autonomous Vehicles & Self-Driving Cars 🚗🤖
📌 Use: Classify road objects (cars, pedestrians, traffic lights) to make driving decisions.
📌 Example:
• Object Detection: Detects if an object is a pedestrian, traffic sign, or vehicle using CNNs.
• Lane Detection: Classifies road lanes using Decision Trees.
7. Speech Recognition & Virtual Assistants
📌 Use: Convert spoken words into text and classify commands.
📌 Example:
• Voice Assistants (Alexa, Siri, Google Assistant): Classify voice inputs into different categories
(e.g., "Set Alarm," "Play Music").
• Speech-to-Text Systems: Classify spoken words into textual representation using Deep
Learning models.
8. Industrial Applications & Quality Control 🏭🔧
📌 Use: Detect manufacturing defects in production lines.
📌 Example:
• Defect Detection in Factories: Classify products as "defective" or "non-defective" using
Machine Learning.
• Predictive Maintenance: Detect whether a machine is likely to fail soon or not using SVM.
********** 5 **********
--- page 6 ---
9. Customer Segmentation in Marketing & E-commerce 🛒📊
📌 Use: Classify customers into different categories for personalized recommendations.
📌 Example:
• Product Recommendation Systems: Suggests products based on user preferences using
Decision Trees.
• Customer Churn Prediction: Classifies if a user is likely to leave a service or stay using
Random Forest.
🔹 Common Classification Algorithms Used in AI
Algorithm   Common Use Case
Logistic Regression   Disease Prediction, Loan Approval
Decision Tree   Fraud Detection, Customer Segmentation
Random Forest   Spam Detection, Image Classification
Naïve Bayes   Sentiment Analysis, Email Spam Filtering
Support Vector Machine (SVM) Text Classification, Face Recognition
k-Nearest Neighbors (KNN)   Handwritten Digit Recognition, Anomaly Detection
Neural Networks (CNN, RNN) Image Recognition, Speech Recognition
🔹 Conclusion:
Classification algorithms power AI applications in Healthcare, Finance, Marketing, Security, and
more. They enable machines to analyze data, recognize patterns, and make intelligent decisions
based on past experiences.
Would you like a Python example for a classification algorithm? 😊
Q2 Explain the traversing path of following problem using Depth First Search-
Ans -
A → B → F → K → C → G → H → L → M → N → D → E → I → J → O → P
Q3 Explain any 2 classification methods used in AI?
Two Classification Methods Used in AI
Classification is a type of Supervised Learning where an AI model learns from labeled data to
categorize new inputs into predefined classes. Here are two widely used classification methods in AI:
********** 6 **********
--- page 7 ---
1. Decision Tree Classification 🌳
Definition:
A Decision Tree is a tree-like model that splits data based on features and makes decisions at each node
until it reaches a final classification.
How it Works:
• The dataset is split into subsets based on the most significant feature at each step.
• The tree continues splitting until a decision node (leaf node) is reached.
• Uses metrics like Gini Index or Entropy (Information Gain) to determine the best splits.
Example Use Case:
👉 Medical Diagnosis:
• A decision tree can classify if a patient has Diabetes (Yes/No) based on symptoms like blood
sugar level, age, and weight.
Pros:
✅ Easy to interpret and visualize.
✅ Works well with both numerical and categorical data.
Cons:
❌ Prone to overfitting if the tree is too deep.
❌ Less effective on complex datasets compared to ensemble models.
2. Support Vector Machine (SVM) Classification 📊
Definition:
A Support Vector Machine (SVM) is a powerful classification algorithm that finds the optimal
hyperplane to separate data points into different categories.
How it Works:
• Maps input data into a high-dimensional space.
• Finds a decision boundary (hyperplane) that best separates different classes.
• Uses Support Vectors (critical data points) to maximize the margin between classes.
Example Use Case:
👉 Spam Detection in Emails:
• SVM can classify whether an email is Spam or Not Spam based on words in the message.
Pros:
✅ Works well with high-dimensional data.
✅ Effective in text and image classification tasks.
Cons:
❌ Computationally expensive for large datasets.
❌ Difficult to choose the correct kernel function for non-linear data.
********** 7 **********
--- page 8 ---
🔹 Comparison Table
Method   Best For   Advantages   Disadvantages
Decision   Simple, easy-to-
Fast and interpretable results Overfitting if not pruned properly
Tree   interpret cases
High-dimensional and Handles non-linearly   Computationally expensive for
SVM
text data   separable data well   large datasets
Both methods are widely used in AI applications like healthcare, finance, fraud detection, and
recommendation systems.
Would you like a Python example of these classification methods? 😊
Q4: Find best path and total cost for the following graph using A* algorithm:
Solving A Algorithm for the Given Tree*
The A (A-Star) Algorithm* is a search algorithm that finds the most cost-effective path from a start node
to a goal node. It uses the formula:
f(n)=g(n)+h(n)f(n) = g(n) + h(n)
Where:
•   f(n) = Total estimated cost of the node
•   g(n) = Cost from the start node to the current node
• h(n) = Heuristic estimate of the cost from the current node to the goal
Step 1: Identify the Given Data
• Start Node: S (Value = 7)
• Goal Nodes: Nodes with heuristic value = 0 (shaded nodes: F, L, M).
• Path Costs (g(n)): Given edge weights.
• Heuristic Costs (h(n)): Values inside each node.
********** 8 **********
--- page 9 ---
Step 2: Apply A Algorithm*
1. Start at Node S
f(S)=g(S)+h(S)=0+7=7f(S) = g(S) + h(S) = 0 + 7 = 7
Possible paths from S:
• S→AS \to A (Cost 5, h=0)
• S→BS \to B (Cost 3, h=1)
• S→CS \to C (Cost 4, h=4)
Calculate f(n) for each child:
• f(A)=5+0=5f(A) = 5 + 0 = 5
• f(B)=3+1=4f(B) = 3 + 1 = 4
• f(C)=4+4=8f(C) = 4 + 4 = 8
Choose the lowest f(n): B (f=4)
2. Expand Node B
Possible paths:
• B→FB \to F (Cost 8, h=0)
• B→GB \to G (Cost 5, h=?)
Calculate f(n):
• f(F)=(3+8)+0=11f(F) = (3+8) + 0 = 11
• f(G)=(3+5)+h(G)f(G) = (3+5) + h(G) → Unknown heuristic
Since F has the lowest f(n), choose F as the best path.
Step 3: Find the Best Path and Total Cost
The path followed based on A* evaluation:
S→B→FS \to B \to F
• Total cost (g(n)): 3+8=113 + 8 = 11
• Optimal path: S → B → F
Final Answer
✅ Best Path: S → B → F
✅ Total Cost: 11
Would you like me to verify another path or explain further? 😊
Q5: Differentiate between Supervised and Unsupervised learning in AI
Difference Between Supervised and Unsupervised Learning in AI
Supervised and Unsupervised Learning are two main types of Machine Learning used in AI. They differ
based on data availability, learning approach, and application areas.
********** 9 **********
--- page 10 ---
🔹 1. Supervised Learning
📌 Definition:
•   In Supervised Learning, the algorithm learns from a labeled dataset, where each input has a
corresponding output (label).
• The model maps input to output based on provided examples.
📌 How it Works:
• The algorithm trains on historical data (input → output) and predicts labels for new data.
📌 Examples:
✅ Email Spam Detection: Classifies emails as Spam (1) or Not Spam (0).
✅ Disease Prediction: Predicts if a patient has Diabetes (Yes/No) based on health parameters.
📌 Types:
1. Classification: Predicts discrete categories (e.g., Spam/Not Spam).
2. Regression: Predicts continuous values (e.g., House Price Prediction).
📌 Algorithms Used:
✔️ Decision Tree
✔️ Random Forest
✔️ Support Vector Machine (SVM)
✔️ Neural Networks
📌 Advantages:
✅ High accuracy due to labeled data.
✅ Helps in real-time predictions.
📌 Disadvantages:
❌ Requires large labeled datasets, which are costly to obtain.
❌ Less adaptable to changing environments.
🔹 2. Unsupervised Learning
📌 Definition:
•   In Unsupervised Learning, the algorithm learns from unlabeled data.
• The model identifies patterns, relationships, and structures in data without predefined labels.
📌 How it Works:
• The algorithm groups similar data points without prior knowledge.
📌 Examples:
✅ Customer Segmentation in Marketing: Groups customers based on shopping behavior.
✅ Anomaly Detection in Cybersecurity: Detects unusual login activity or fraud.
📌 Types:
********** 10 **********
--- page 11 ---
1. Clustering: Groups similar data points (e.g., K-Means Clustering).
2. Association: Finds relationships between items (e.g., Market Basket Analysis).
📌 Algorithms Used:
✔️ K-Means Clustering
✔️ Hierarchical Clustering
✔️ Principal Component Analysis (PCA)
✔️ Autoencoders (for dimensionality reduction)
📌 Advantages:
✅ Works well with unstructured data.
✅ Helps in discovering hidden patterns.
📌 Disadvantages:
❌ Results are harder to interpret due to no predefined labels.
❌ Less accurate compared to supervised models.
🔹 Key Differences:
Feature   Supervised Learning   Unsupervised Learning
Data Type   Labeled Data   Unlabeled Data
Purpose   Predict outcome   Find hidden patterns
Main Tasks   Classification & Regression   Clustering & Association
Example   Spam Detection, Disease Prediction Customer Segmentation, Fraud Detection
Accuracy   Higher due to labeled data   Lower due to no labels
Human Intervention Requires labeled data   Learns patterns without labels
🔹 Conclusion:
• Use Supervised Learning when labels are available (e.g., predicting diseases).
• Use Unsupervised Learning when labels are missing and you want to find patterns (e.g.,
market segmentation).
Would you like an example in Python for these? 😊
Q6: Differentiate between Depth First Search and Breadth First Search algorithm? Explain the
advantage for each
Difference Between Depth First Search (DFS) and Breadth First Search (BFS)
Depth First Search (DFS) and Breadth First Search (BFS) are two fundamental graph traversal
algorithms. They differ in how they explore nodes and their applications.
🔹 1. Depth First Search (DFS)
📌 Definition:
• DFS explores a graph/tree by moving deep into one branch before backtracking.
• Uses a stack (LIFO) to remember visited nodes.
********** 11 **********
--- page 12 ---
📌 How it Works:
1. Start at the root node.
2. Move to the deepest unvisited node.
3. Backtrack when no unvisited nodes remain.
📌 Example:
Traversal order for the below tree using DFS (Pre-order):
A
/ \
B C
/ \   \
D E F
DFS Traversal: A → B → D → E → C → F
📌 Applications:
✅ Maze Solving (Explores all paths until it finds an exit).
✅ Topological Sorting in dependency resolution.
✅ Game AI (Backtracking, Sudoku, Chess moves).
📌 Advantages:
✔️ Memory Efficient: Requires storing only the current path (O(depth)).
✔️ Works well for deep trees/graphs with fewer branches.
📌 Disadvantages:
❌ Might Get Stuck in Loops (if cycles exist without a visited check).
❌ Not Always Optimal (may not find the shortest path).
🔹 2. Breadth First Search (BFS)
📌 Definition:
• BFS explores a graph/tree level by level before moving deeper.
• Uses a queue (FIFO) to track nodes to visit next.
📌 How it Works:
1. Start at the root node.
2. Visit all neighbors first before moving to the next level.
📌 Example:
Traversal order for the same tree using BFS:
A
/ \
B C
/ \   \
D E F
BFS Traversal: A → B → C → D → E → F
📌 Applications:
✅ Shortest Path Finding (like Google Maps).
********** 12 **********
--- page 13 ---
✅ Social Network Analysis (finding people with mutual connections).
✅ AI in Web Crawling (traversing websites efficiently).
📌 Advantages:
✔️ Guaranteed Shortest Path (if all edges have equal weight).
✔️ Ideal for Shallow Graphs (expands level-wise).
📌 Disadvantages:
❌ More Memory Usage (stores all nodes at each level).
❌ Slow for Deep Graphs (must explore many nodes before reaching deep ones).
🔹 Key Differences:
Feature   Depth First Search (DFS)   Breadth First Search (BFS)
Data Structure Used   Stack (LIFO)   Queue (FIFO)
Exploration Order   Deep before wide   Level by level
Higher (O(b^d), where b =
Memory Usage   Lower (O(d), where d = depth)
branching factor)
Solving mazes, puzzles, backtracking   Finding the shortest path, social
Best for
problems   networks
Guaranteed Shortest   ✅ Yes (if all edges have equal
❌ No (depends on order)
Path?   weight)
Works Well When   Graph is deep with fewer branches   Graph is wide and shallow
🔹 When to Use DFS vs BFS?
• Use DFS when searching for a solution, not necessarily the shortest path (e.g., puzzle
solving).
• Use BFS when searching for the shortest path or all possible solutions at the same depth
(e.g., route finding).
Would you like a Python implementation of both? 😊
Q7: What are the differences between Informed and Uninformed searches
Difference Between Informed and Uninformed Search Algorithms
In Artificial Intelligence (AI), search algorithms help find a path from the initial state to the goal state
in problem-solving. They are classified into:
1. Uninformed Search (Blind Search)
2. Informed Search (Heuristic Search)
🔹 1. Uninformed Search (Blind Search)
📌 Definition:
• Uninformed search does not have additional information about the goal except for the problem
definition.
********** 13 **********
--- page 14 ---
•   It explores paths blindly until a solution is found.
📌 How it Works:
• Expands nodes without considering the goal distance.
• Uses only the problem constraints to traverse the search space.
📌 Common Algorithms:
✅ Breadth-First Search (BFS): Explores level by level.
✅ Depth-First Search (DFS): Explores deep first, then backtracks.
✅ Uniform Cost Search (UCS): Expands the least-cost node first.
📌 Advantages:
✔️ Simple to implement (no extra data required).
✔️ Guaranteed solution if a goal state exists.
📌 Disadvantages:
❌ Inefficient (may explore unnecessary paths).
❌ High time complexity in large search spaces.
🔹 2. Informed Search (Heuristic Search)
📌 Definition:
• Informed search uses additional knowledge (heuristics) to estimate the best path toward the
goal.
• The heuristic function h(n) helps prioritize the most promising paths.
📌 How it Works:
•   Instead of searching blindly, it uses a heuristic function to rank nodes based on estimated cost.
📌 Common Algorithms:
✅ Greedy Best-First Search: Chooses the node closest to the goal (h(n)).
✅ A Algorithm:* Uses both actual cost (g(n)) and heuristic cost (h(n)):
f(n)=g(n)+h(n)f(n) = g(n) + h(n)
📌 Advantages:
✔️ Faster than Uninformed Search (reduces unnecessary exploration).
✔️ More optimal solutions in many cases.
📌 Disadvantages:
❌ May require complex heuristics (choosing a good heuristic is challenging).
❌ Not always optimal (depends on heuristic function).
🔹 Key Differences Between Informed and Uninformed Search
Feature   Uninformed Search (Blind) Informed Search (Heuristic)
Knowledge Used   No additional information   Uses heuristic knowledge
Guidance Towards Goal   No   Yes
********** 14 **********
--- page 15 ---
Feature   Uninformed Search (Blind) Informed Search (Heuristic)
Efficiency   Less efficient (explores blindly) More efficient (guided search)
Time Complexity   Higher   Lower
Guarantees Optimal Solution? Sometimes (e.g., UCS)   Usually (e.g., A*)
Example Algorithms   BFS, DFS, UCS   Greedy Best-First Search, A*
🔹 When to Use Which?
• Use Uninformed Search when no heuristic information is available.
• Use Informed Search when you can estimate goal distance using a heuristic function.
Would you like a real-world example for each? 😊
********** 15 **********
````

## 2023-24 · Final-Exam · Sem 2 · Answer key · paper b899f8eb6f2e

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Artificial Intelligence/ANS_Final-Exam_Artificial Intelligence(703CO0C008)_Semester II_2023-2024.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 22 Apr 2024
- Text: mixed (17 pages), mean OCR confidence 84.6

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II (Exam Year: 2023-2024)
Subject: Artificial Intelligence
Date: 22 Apr 2024   Time: 10:00 am - 01:00 pm (03:00 Hrs.)
Max Marks:   100
FINAL EXAMINATION(2023-2024)
Instructions:
1. This Synoptic paper contains 17 pages
2. Question No. _1_ is compulsory.
3. Out of remaining questions, attempt any _4_ questions.
4. In all _5_ questions to be attempted.
5. All main questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
1. 1 Solve the following   20
A. Artificial Intelligence (AI) finds applications across various domains, revolutionizing processes   5
and tasks. Here are some of the key application areas:
Healthcare: AI is used for diagnosis assistance, personalized treatment plans, drug discovery,
and medical imaging analysis. It helps in predicting diseases, managing patient data, and
optimizing healthcare operations.
Finance: AI is applied in fraud detection, risk assessment, algorithmic trading, customer service
(chatbots), and personalized financial advice. It analyzes vast amounts of financial data to make
predictions and recommendations.
Retail: AI is used for personalized recommendations, demand forecasting, inventory
management, customer service (chatbots), and supply chain optimization. It enhances customer
experience and improves operational efficiency.
Automotive: AI powers self-driving cars, advanced driver-assistance systems (ADAS),
predictive maintenance, and vehicle diagnostics. It improves safety, efficiency, and convenience
in transportation.
Page 1 of 17
--- page 2 ---
Manufacturing: AI is applied in predictive maintenance, quality control, supply chain
optimization, autonomous robots, and process automation. It helps in reducing downtime,
improving productivity, and ensuring product quality.
Marketing: AI enables targeted advertising, customer segmentation, sentiment analysis, and
predictive analytics. It optimizes marketing campaigns, enhances customer engagement, and
improves ROI.
Education: AI assists in personalized learning, adaptive tutoring systems, student assessment,
and administrative tasks automation. It provides customized learning experiences and helps
educators in better decision-making.
Cybersecurity: AI is used for threat detection, anomaly detection, behavior analysis, and real-
time response in cybersecurity systems. It helps in identifying and mitigating security risks more
effectively.
Natural Language Processing (NLP): AI is applied in language translation, sentiment analysis,
text summarization, chatbots, and virtual assistants. It enables computers to understand,
interpret, and generate human language.
Robotics: AI powers autonomous robots in various industries, including manufacturing,
healthcare, agriculture, and logistics. It enables robots to perform complex tasks in dynamic
environments.
Entertainment: AI is used in content recommendation systems, personalized streaming services,
video game development, and virtual reality experiences. It enhances user engagement and
entertainment offerings.
Agriculture: AI assists in precision farming, crop monitoring, yield prediction, and pest
detection. It optimizes resource utilization, improves crop yields, and supports sustainable
agriculture practices.
B. In the context of Constraint Satisfaction Problems (CSPs), variable ordering refers to the   5
strategy of deciding which variable to assign a value to first, second, third, and so on. The order
in which you tackle the variables can significantly impact the efficiency of solving a CSP,
especially when using backtracking search algorithms.
Here's why variable ordering matters:
Reduced Backtracks: A good variable ordering can minimize the number of backtracks
needed during the search process. Imagine you're coloring a map. Choosing a variable
(country) that constrains many other countries' colors (e.g., a country in the center) early on
can help you avoid dead ends later when assigning colors to neighboring countries.
Pruning the Search Space: By strategically selecting variables, you can effectively prune
out parts of the search space that will inevitably lead to constraint violations. This reduces the
number of assignments you need to try before finding a solution.
Common Heuristics for Variable Ordering:
Page 2 of 17
--- page 3 ---
Minimum Remaining Values (MRV): This heuristic prioritizes assigning values to
variables with the fewest remaining possible values in their domain. The idea is that such
variables are more likely to cause conflicts early on, so making a decision about them can
help constrain the search space more effectively.
Most Constraining Variable (MCV): This approach focuses on variables that participate in
the most constraints with other unassigned variables. Assigning a value to such a variable can
quickly affect the feasibility of many other assignments, potentially pruning out invalid
branches early.
Degree Heuristic: This simple heuristic prioritizes variables with the highest number of
constraints they are involved in. Similar to MCV, it targets variables that have a wider impact
on the overall solution.
Choosing the Right Heuristic:
The best variable ordering heuristic depends on the specific CSP you're dealing with.
Sometimes, a combination of these heuristics can be even more effective. Experimenting with
different approaches can help you find the most efficient strategy for a particular problem.
Additional Considerations:
Variable ordering can be static, meaning the order is fixed before the search starts.
Dynamic ordering, on the other hand, can adapt the order based on the current state of the
search (e.g., after a backtrack).
While variable ordering is crucial, it's often used in conjunction with value ordering
heuristics, which determine the order in which to try the possible values for a chosen
variable.
By carefully considering variable ordering, you can significantly improve the efficiency of
solving Constraint Satisfaction Problems and find solutions faster.
C. Resolution is a theorem proving technique that proceeds by building refutation proofs, i.e.,   5
proofs by contradictions.
It was invented by a Mathematician John Alan Robinson in the year 1965.
Resolution is used, if there are various statements are given, and we need to prove a conclusion
of those statements.
Unification is a key concept in proofs by resolutions.
Resolution is a single inference rule which can efficiently operate on the conjunctive normal
form or clausal form.
Clause: Disjunction of literals (an atomic sentence) is called a clause. It is also known as a unit
clause.
Page 3 of 17
--- page 4 ---
Conjunctive Normal Form: A sentence represented as a conjunction of clauses is said to be
conjunctive normal form or CNF.
D. Here are a couple of examples of expert systems you might encounter in everyday life:   5
Medical Diagnosis Assistant: Imagine you're visiting a website to research your symptoms.
The website might use an expert system to ask you a series of questions about your
experiences. Based on your answers, the system can narrow down potential causes and
suggest you see a doctor if necessary. This wouldn't be a definitive diagnosis, but it can be a
helpful tool.
Technical Support Chatbot: When you contact a company's customer service for a
technical issue, you might interact with an expert system first. This chatbot can ask you
questions about the problem you're facing and try to diagnose the issue based on a set of
rules. It might even suggest solutions or troubleshoot common problems.
2. 2 Solve the following (Attempt Any 4 Questions)   80
1.   20
A.
10
10
Page 4 of 17
--- page 5 ---
B. Draw the state space search tree for the above knowledge.
2.   20
A. Heuristic search-   10
Blind search techniques used an arbitrary ordering (priority) of operations.
•Heuristic search techniques make use of domain specific information - a heuristic.
•What heurisitic(s) can we use to decide which 8-puzzle move is “best” (worth considering
first).
Page 5 of 17
--- page 6 ---
For now - we just want to establish some ordering to the possible moves (the values of our
heuristic does not matter as long as it ranks the moves).
Later - we will worry about the actual values returned by the heuristic function.
A Simple 8-puzzle heuristic-
Number of tiles in the correct position.
–The higher the number the better.
–Easy to compute (fast and takes little memory).
–Probably the simplest possible heuristic.
Number of tiles in the incorrect position.
–This can also be considered a lower bound on the number of moves from a solution!
–The “best” move is the one with the lowest number returned by the heuristic.
–Is this heuristic more than a heuristic (is it always correct?).
Given any 2 states, does it always order them properly with respect to the minimum number of
moves away from a solution?
There are a variety of search techniques that rely on the estimate provided by a heuristic
function.
•In all cases - the quality (accuracy) of the heuristic is important in real-life application of the
technique!
Example-
8 Puzzle Heuristics -
B. Following are the steps to apply.   10
Page 6 of 17
--- page 7 ---
Standardize variables:

1. Wx: graduati Dh
: graduating(x) appy(x) 1. Wx:- graduating(x) vhappy(x)

2. Wx: happy(x) > smile(x) 2 Vy:- happy(y) vsmilety)

3. dx: graduating(x) 3. 3z: graduating(z)
4. -(Ax: smile(x)) 4. -(3w:smile(w))
Remove implications: Move negation inverds and remove

1. Wx: - graduating(x) v happy(x) quantifiers:

- graduatin vha
2 Wx: -happy(x) v smile(x) : graduating(x) v happy(x)
2. - happy(y) vsmile(y)

3. 3x: graduating(x) 5. graduating(z)

4. -—(4x: smile(x)) 4. ~smile(w)

Prove by resolution that someone is smiling.

Local beam search

+ Keeping just one node in the memory is not
always a good solution

* Keeptrack ofk states rather than just one
* Start with k randomly generated states

« At each iteration, all the successors ofall k
states are generated

+ Ifany one is a goal state, stop; else selectthe k
best successors from the complete list and
repeat.

* Stochastic beam search (variant)

Page 7 of 17

20

10
--- page 8 ---
Local beam search

* It look similar to the random-restart search
that it runs in parallel rather in sequence

* In RR each process runs independently of
each other

* In LBS useful information is passed
among the K parallel search threads

* Ex: one state generate several good state,
while other generating all bad moves, first
state say to the other — “come over here,
the grass is greener”

Local beam search

* The algorithm quickly abandons unfruitful
searches

* Move its resources to where more
progress is being made

* LBS can suffer from the lack of diversity
among the k state

* They can quickly become concentrated in
a small region of the state space- making
the expensive version of HC

A.

B. Significance - 2 Marks
Algorithm with example (graph coloring) - 8 marks

Page 8 of 17

10
--- page 9 ---
function BACKTRACKING-SEARCH( csp) returns a solution, or failure
return RECURSIVE-BACKTRACKING({}, csp)

function RECURSIVE-BACKTRACKING( assignment, csp) returns a solution, or
failure
if assignment is complete then return assignment
var SELECT- UNASSIGNED- VARIABLE( Variables/csp/, assignment, csp)
for each value in ORDER-DOMAIN-VALUES(var, assignment, csp) do
if value is consistent with assignment according to Constraints[csp] then
add { var = value } to assignment
result — RECURSIVE-BACKTRACKING( assignment, csp)
if result # failue then return result
remove { var = value } from assignment
return failure

{ot
_—tT~.
O35 Cb ES
_——_
es &
_———_

es ¢

Page 9 of 17

20

10
--- page 10 ---
Minimax

+ Perfect play for deterministic games

* Idea: choose move to position with highest minimax
value
= best achievable payoff against best play
* Eg., 2-ply game:
MAX

MIN

Minimax algorithm

function Mintmax-Deersion(stafe) returns an action

tt MAX- VALUE(state)
return the action in SuCCESSORS( state) with value v

function MAX-VALUE(state) returns a ulility value
if Team Inat-Test(stete) then return UTILITy( state)
te —oO
for a,sin SUCCESSORS( state) do
wt Max(v, Mrn- VALUE(s))
return ©

function Mix-VaLUe(state) returns a utility value
if TERM INAt- Test (state) then return UrtLiry(state)
te oo
for o,sin SucCEssons( state) do
ve Min(e, Max-VaLve(s))
return w

Page 10 of 17
--- page 11 ---
A.
B. Significance in AI - 2 Marks   10
Explanation on inductive learning with example - 8 marks
The inductive learning is a process of learning by example. The system tries to induce a
general rules from a set of observed instances. The learning methods extract rules and patterns
out of massive data sets.
The learning processes belong to supervised learning, does classification and constructs class
definitions, called induction or concept learning.
Simplest form: learn a function from examples.
Page 11 of 17
--- page 12 ---
f is the target function
An example is a pair (x, f(x))
Problem: find a hypothesis h
such that h ≈ f
given a training set of examples.
Page 12 of 17
--- page 13 ---
Page 13 of 17
--- page 14 ---
Students should discuss at least three models from this example.
5.   20
A. Backward chaining - 5 Marks   10
●The backward reasoning is inverse of forward reasoning
●It starts by finding all the rules whose right side matches with the goal node
●Goal is analyzed in order to deduce the rules, initial facts and data.
●We can understand the concept by the similar example,
●In forward reasoning the doctor is trying to diagnose the patient with the help of the inceptive
data such as symptoms.
●However, in this case, the patient comes up with the name of disease, on the basis of which
the doctor is going to prove and verify the symptoms.
●This kind of reasoning comes under backward reasoning.
properties
●It is known as a top-down approach.
●Backward-chaining is based on modus ponens inference rule.
●In backward chaining, the goal is broken into sub-goal or sub-goals to prove the facts true.
Page 14 of 17
--- page 15 ---
●It is called a goal-driven approach, as a list of goals decides which rules are selected and
used.
●Backward chaining algorithm is used in game theory, automated theorem proving tools,
inference engines, proof assistants, and various AI applications.
●The backward-chaining method mostly uses a depth-first search strategy for proof.
Example: - 5 marks
B. Designing the tree and solving complete example [10 Marks]   10
6.   20
Page 15 of 17
--- page 16 ---
A. Local search for Constraint Satisfaction Problems (CSPs) is an alternative approach to   10
backtracking search. Unlike backtracking's systematic exploration, local search focuses on
iteratively improving an assignment until a solution is found. Here's a breakdown of the key
ideas:
Core Concept:
Local search doesn't explore the entire search space systematically. Instead, it starts with an
initial assignment of values to variables and then iteratively makes small modifications to
improve the solution.
The focus is on finding a solution that satisfies all constraints, but it doesn't guarantee
finding the optimal solution (one with the fewest constraint violations).
The Process:
1. Initial Assignment: Local search starts with an initial assignment of values to all variables.
This can be random or based on some heuristic.
2. Evaluation Function: A function evaluates the quality of the current assignment. This
typically involves counting the number of violated constraints. Lower values indicate a
better solution.
3. Neighborhood Exploration: Local search examines neighboring assignments. A neighbor
is typically created by modifying the value of a single variable in the current assignment.
4. Improvement Step: The algorithm moves to a neighboring assignment only if it improves
the evaluation function (reduces constraint violations).
5. Iteration: Steps 3 and 4 are repeated until a solution is found (no constraint violations) or a
stopping criterion is met (e.g., no improvement for a certain number of iterations).
Key Points about Local Search for CSPs:
Iterative Improvement: Local search improves solutions incrementally, focusing on
finding a good enough solution rather than the absolute best.
Heuristics for Exploration: How to choose neighboring assignments and which ones to
prioritize can be guided by heuristics. For example, picking the neighbor that reduces the
most constraint violations.
Incompleteness: Unlike backtracking, local search might get stuck in local optima - a
solution that seems good but isn't the best and no better neighbors exist based on the chosen
exploration strategy. Techniques like random restarts can help escape local optima and
explore different areas of the search space.
Page 16 of 17
--- page 17 ---
Efficiency: Local search can be faster than backtracking for large problems, especially
when a good solution is sufficient. However, it might miss the optimal solution entirely.
In essence, local search offers a trade-off between optimality and efficiency. It's a good
choice when finding a decent solution quickly is more important than finding the
absolute best one.
10
B.
Page 17 of 17
````
