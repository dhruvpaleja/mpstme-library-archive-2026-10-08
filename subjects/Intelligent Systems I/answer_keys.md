# Intelligent Systems I: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 12e04955d5bd

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AIML_7053/Intelligent Systems - I/ANS_Intelligent Systems - I(702AI0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: mixed (18 pages), mean OCR confidence 67.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Intelligent Systems - I
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q:1
Artificial Intelligence (AI):Intelligence exhibited by machines. It is artificial, meaning it
is not real or human. AI mimics cognitive functions such as perceiving, learning, and
reasoning which are exhibited by humans.
[1 Marks]
Applications of AI (any four):   [4 Marks]
1. Search engines
AI is everywhere, including search engines, which use intelligent algorithms to
provide relevant results.
Q: 1   2. Medicine and diagnosis
a.   AI assists in diagnosis and image-guided surgery, image analysis, and
enhancement in the medical field.
3. Autonomous vehicles (self-driving cars)
AI is applied in transportation for autonomous vehicle control and pedestrian
detection.
4. Virtual assistants like Siri or Alexa
These are examples of Weak AI that provide human-like experience through
programmed responses.
Describe the characteristics of intelligent agents.   [5 Marks for 5 points]
1. 1. Autonomy:
Intelligent agents operate with a degree of independence. They can perform tasks
on their own   without constant human intervention.
Q: 1   2. Learning Ability:
b.   These agents can learn from their experiences and improve their performance over
time, even while executing tasks.
3. Interaction:
Intelligent agents are capable of interacting with other entities such as humans,
other agents, or systems to achieve their objectives.
********** 1 **********
--- page 2 ---
4. Adaptability:
They can accommodate new rules and information incrementally, allowing them
to adapt to changing environments or requirements.
5. Goal-Oriented Behavior:
Intelligent agents exhibit behavior that is directed toward achieving specific goals
or objectives.
6. Knowledge-Based:
They utilize knowledge about communication, processes, and entities to make
informed decisions and take appropriate actions.
Q: 1
c.
Minimum 5 points – 1 mark for each point
Predicate Logic (First-Order Logic):.   2 marks
Predicate Logic, also called First-Order Logic (FOL), is an extension of
Propositional Logic that allows reasoning about objects, their properties, and
relationships.
• Unlike propositional logic, which deals with simple true/false statements,
FOL can represent statements like “All humans are mortal” or “Some
students like mathematics.”
Types of Quantifiers in FOL:   3 marks
1. Universal Quantifier (∀):
Q: 1
o Symbol: ∀
d.
o Meaning: “For all” or “Every”
o Example:
▪ ∀x (Human(x) → Mortal(x))
▪   Translation: “For every x, if x is a human, then x is mortal.”
2. Existential Quantifier (∃):
o Symbol: ∃
o Meaning: “There exists” or “Some”
o Example:
▪ ∃x (Student(x) ∧ LikesMath(x))
▪   Translation: “There exists at least one x such that x is a
student and x likes mathematics.”
********** 2 **********
--- page 3 ---
Q:2   Answer briefly:
Weak AI or Narrow AI or Artificial   Strong AI or Artificial General
Narrow Intelligence (ANI)   Intelligence (AGI)
Intelligent at completing a specific task   Exhibits human intelligence
It can understand, perceive, think, act, plan,
AI applied to a specific domain
solve problems etc like a human being does
They give human like experience, but it is
They have self awareness
just a simulation
Q: 2   They can interact and operate a wide variety
They often have programmed response
a.   of independent and unrelated tasks
Examples: language translators, virtual
assistants, self driving cars, AI powered web
Can learn new tasks to solve new problems
searches, recommendation engines,
intelligent spam filters
Example Siri or Alexa, advanced chess   Machines that are indistinguishable from
programs   human mind
Minimum 5 points – 1 mark for each point
Structure of Agent (2 marks):
• AI designs an agent program to implement the agent function.
• Agent = Architecture + Program
o Architecture: Physical computing device with sensors and actuators.
o Program: Implements the agent function.
Agent Program vs Agent Function (3 marks):
Q: 2
• Agent Program:
b.   o Takes current percept as input from sensors.
o Returns action as output to actuators.
• Agent Function:
o Maps entire percept history to actions.
o More abstract and theoretical than the agent program.
Q: 2
c.   Aspect   A* Search Algorithm   AO* Search Algorithm
Graph Type OR-graph   AND-OR graph
Finds a single optimal   Finds solutions that may involve multiple
Goal
solution path   sub-goals (AND conditions)
Optimality   Provides optimal solution May not always provide optimal solution
Memory   Requires more memory as
Requires less memory compared to A*
Usage   it stores all generated nodes
Loop   Can go into infinite loops if Avoids infinite loops due to structured
Handling   not handled properly   decomposition
********** 3 **********
--- page 4 ---
Suitable for problems with Suitable for problems that can be
Use Case   a single goal and linear   decomposed into sub-problems with
path   AND/OR dependencies
Uses: 𝑓(𝑛) = 𝑔(𝑛) +
ℎ(𝑛)where:
Evaluation   - 𝑔(𝑛): cost from start to   Also uses: 𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)but applies
Function   current node   it over AND/OR branches collectively
- ℎ(𝑛): estimated cost to
goal
Pathfinding in maps, puzzle Planning tasks with multiple dependencies,
Example
solving   decision trees
4 marks for difference (minimum 4 points)
6 marks for solving (1 mark for each step and 1 mark for diagram)
Q:3   Answer briefly:
Simple Reflex Agent   [2 Marks]
Q: 3 A Simple Reflex Agent selects actions based on the current percept, ignoring the rest of
a.   the percept history. It operates using condition-action rules (also known as "if-then"
rules).
********** 4 **********
--- page 5 ---
Working:
• The agent perceives the environment through sensors.
•   It applies a rule to the current percept.
•   Executes an action using actuators based on the rule.
Characteristics:
• Works well in fully observable environments.
• Does not maintain any internal state.
•   Limited intelligence and adaptability.
2. Model-Based Reflex Agent   [2
Marks]
A Model-Based Reflex Agent improves upon the simple reflex agent by maintaining
some internal state to keep track of the partially observable environment.
Working:
•   Maintains an internal model of the world.
•   Updates the internal state based on percepts and the model of how the world
works.
•   Chooses actions based on the current percept and internal state.
Characteristics:
• Can handle partially observable environments.
•   Uses a model of the world and internal state to make decisions.
• More flexible and intelligent than simple reflex agents.
[1 Mark for diagram]
********** 5 **********
--- page 6 ---
Hill Climbing Algorithm:   [2 Marks]
Hill Climbing is a local search algorithm that continuously moves in the direction of
increasing value (or decreasing cost) to find the peak (or optimal solution). It evaluates the
neighboring states and selects the one with the best value.
•   It is also known as greedy local search.
•   It terminates when it reaches a state where no neighbor has a better value.
Q: 3
b.
Problems in Hill Climbing and Their Solutions:   [3 Marks]
1. Local Maximum:
o Problem: A peak that is higher than neighboring states but lower than the
global maximum.
o   Solution: Use backtracking to explore alternative paths or maintain a list
of promising paths.
2. Plateau:
o Problem: A flat area where neighboring states have the same value,
making it hard to determine the direction.
o   Solution: Take larger or random steps to escape the plateau and reach a
region with gradient.
3. Ridges:
o Problem: A slope that is higher than surrounding areas but cannot be
climbed directly due to its orientation.
o   Solution: Use bidirectional search or allow movement in multiple
directions to navigate the ridge.
Backtracking can be improved by using heuristics, such as choosing the most
constrained variable or the least constraining value to guide the search and reduce
the number of backtracks.
The efficiency of the backtracking algorithm can be improved using the Most
Constrained Variable (MCV) and Least Constraining Value (LCV) methods. In
Q: 3 MCV, we select the variable that has the fewest possible values left to assign.
c.
This helps detect conflicts early and reduces unnecessary search, as we try to assign
the hardest variable first. In LCV, when assigning a value to a variable, we choose
the one that leaves the most options open for other variables.
This helps keep future choices flexible and reduces the chances of backtracking later.
Together, these methods make the search process faster and more efficient.
********** 6 **********
--- page 7 ---
3 marks –explanation
Most Constrained Variable: SA (South Australia) should be colored first.
1 mark
6 marks for backtracking solving
1 mark for each assignment
********** 7 **********
--- page 8 ---
Q:4   Answer briefly:
Crypt arithmetic problems are mathematical puzzles in which the digits
are replaced by letters of the alphabets. Crypt arithmetic Problem is a type
of constraint satisfaction problem where the game is about digits and its
unique replacement either with alphabets or other symbols. In crypt
arithmetic problem, the digits 0 9 get substituted by some possible
alphabets or symbols. The task in crypt arithmetic problem is to substitute
each digit with an alphabet to get the result arithmetically correct.
…………… 2 marks
The rules or constraints on a crypt arithmetic problem are as follows:
• There should be a unique digit to be replaced with a unique
alphabet
• The result should satisfy the predefined arithmetic rules i e 2 2 4
• Digits should be from 0 9 only
• There should be only one carry forward, while performing the
addition
• operation on a problem
• The problem can be solved from both sides, i e left hand side (L H
S), or right hand side (R H S)
…………… 2 marks
Step 1   1 mark
Q: 4
a.   • Here obviously J = 1 as max carry allowed it
• (nothing) + M = O, i.e. 0 + M = O this should have had been M
only
•   It means that there is 1 carry coming from previous step
• Also this M + 1 (carry) = O, is generating 1 carry to next step
• This means M + 1 > 10, this is only possible when M = 9
• => O = M + 1 = 9 + 0 = 0 (1 carry)
M A C
+ M A A R
-----------
J O C K O
Step 2   2 marks
C + R = 0
Since, this is at units place there can be no carry from previous step
Possible values of (C, R) can be (2, 8), (3,7), (4, 6), (6,4), (7,3), (2,8)
Lets assume, first case C = 2 and R = 8 in that case C + R, will generate 1
carry to next step A + A = K. The new problem looks like this –
********** 8 **********
--- page 9 ---
1 1
9 A C
+ 9 A A R
-----------
1 0 C K 0
Step 3   2 mark
• Thus, A + A + 1 (Carry) = K
• Also, 9 + A = 2, this is possible in two ways
•   If, A = 3 (no carry from previous step) 9 + 3 = 2 (1 carry to next
step)
•   If, A = 2 (1 carry from previous step) but C value is already
assumed to be 2, so this is not possible thus, A has to be 3
• Thus K = 3 + 3 + 1 = 7
All values are fetched and there is no conflict.
1 1   1
9 A 2
+ 9 A A 8
-----------
1 0 2 K 0
Step 4   1 mark
• Thus, 3 A + 2 M + 2 C = 3(3) + 2(9) + 2(2) = 9 + 18 + 4 = 31
1 1   1
9 3 2
+ 9 3 3 8
-----------
1 0 2 7 0
********** 9 **********
--- page 10 ---
Q: 4
b.
• 5 mark → Correctly finding alpha beta values at each level .
• 1 mark → Correctly calculating the value at the root node.
• 2 mark → Correctly identifying pruned nodes.
• 2 mark → Clear step-by-step presentation.
Q5   Answer briefly:
A normal search problem and a game (adversarial search) differ mainly in the type
of environment and the presence of opponents.
Q: 5
1. Definition (1 mark)
a.
• Normal Search:
A process where a single agent searches for a sequence of actions to reach a
********** 10 **********
--- page 11 ---
goal.
Example: Pathfinding, planning, or scheduling.
• Game (Adversarial Search):
A situation where two or more agents compete with conflicting goals in the
same search space.
2. Presence of Adversary (1 mark)
•   In a normal search, there is no opponent; the agent acts alone.
•   In a game, an adversary (opponent) exists who tries to minimize your
success (e.g., MAX vs. MIN player).
3. Evaluation Function (1 mark)
• Normal Search: Evaluation is based on cost or distance to the goal.
• Game Search: Evaluation is based on the goodness of a game position (e.g.,
win/loss/draw).
4. Optimality of Solution (1 mark)
•   In normal search, heuristic methods can find an optimal solution.
•   In games, the optimal move depends on the opponent’s response.
5. Examples (1 mark)
• Normal Search: Planning, route finding, or scheduling tasks.
• Game Search: Chess, Tic-Tac-Toe, or Checkers.
Constraint Satisfaction Problem is a fundamental topic in artificial intelligence that
deals with solving problems by identifying constraints and finding solutions that
satisfy those constraints. ……………. 2 marks
In artificial intelligence and operations research, constraint satisfaction is the
process of finding a solution to a set of constraints that impose conditions that the
variables must satisfy.
CSP is defined by a set of variables X1 X2 …… Xn and set of conditions
Q:5
C1, C2,…. Cn such that each of the variables Xi has a non empty domain Di of
b.
possible values
Variables: A finite set of Variables V1 ,V2 ……… Vn
Domain: Each Variable has a domain D1 ,D2 …… Dn from which it can take a
value
Constraints: A finite set of satisfaction constraints C1 ,C2….. Cn
For example, We need to color each country as Red, Green, Blue in such a way
that no neighboring country has the same colors.
********** 11 **********
--- page 12 ---
… ……….. 3 marks to explain Variable, domain and constrain with example
1. symbol   Meaning   2 marks
T   Teacher is present
L   Lecture is conducted
A   Attendance is taken
B   Students bunk the next class
C   Lecture is cancelled
Step (b): Convert each statement into propositional logic….5 marks (1 for each)
If the teacher is present, the lecture will be conducted: T → L
If the lecture is conducted, attendance will be taken: L → A
If attendance is taken, students will not bunk the next class: A → ¬B
If the teacher is absent, the lecture will be cancelled: ¬T → C
The lecture was conducted, but attendance was not taken: L ∧ ¬A
Step (c): Logical Analysis …………. 2 marks
Q: 5
From statement (2): L → A (If lecture is conducted, attendance will be taken)
c.
But we are told that: L ∧ ¬A (Lecture conducted, attendance not taken)
This contradicts statement (2).
For L → A to be true, if L is true then A must also be true — but A is false here.
Therefore, L → A must not hold true in this situation, meaning the lecture being
conducted might not be due to the normal condition (T → L).
It could be a special case, for example, a guest lecture or class conducted without
attendance.
Now, check statement (1):
T → L
We have L true, but this doesn’t confirm T (since the converse of implication isn’t
necessarily true).
So, we cannot directly say T is true.
However, from (5) we know attendance not taken, which violates L → A —
implying something abnormal in the usual teaching pattern.
********** 12 **********
--- page 13 ---
Hence, it’s likely that the regular teacher (T) was absent, and someone else
conducted the class (hence no attendance).
• Teacher was absent (¬T)
•   Lecture was conducted (L), but attendance not taken (¬A), which breaks
the usual implication chain.
……………. 1 mark for final conclusion
Q: 6
(a) Translation into Predicate Logic (3 Marks)
Q:6
b.
********** 13 **********
--- page 14 ---
• 1 mark for elimination of implication
• 1 marks for standardize variable
• 1 mark for move negation inwards
• 2 marks for skolemization
• 2 marks for droping quantifier
********** 14 **********
--- page 15 ---
(a) Greedy Best-First Search Algorithm: ………… 4 marks
Greedy Best-First Search is an informed search algorithm that expands the node
that appears to be closest to the goal, using a heuristic function h(n).
Working:
It evaluates nodes by using the heuristic function:
f(n)=h(n)
where:
h(n)is the estimated cost from node nto the goal.
The algorithm always selects the node with the lowest heuristic value.
It uses OPEN and CLOSED lists:
OPEN: Nodes to be explored.
CLOSED: Nodes already explored.
Steps:
Initialize the OPEN list with the start node.
Repeat until the goal is found or OPEN is empty:
Remove the node with the lowest h(n)from OPEN.
Add it to CLOSED.
Expand the node and add its children to OPEN.
If a child is the goal, return the path.
Advantages:
Simple and easy to implement.
Fast and efficient in many cases.
Q:6
Requires less memory than other algorithms.
a.
Disadvantages:
Not guaranteed to find the optimal solution.
Can get stuck in local optima.
Depends heavily on the quality of the heuristic function.
6 marks for solving
********** 15 **********
--- page 16 ---
For Wumpus World:   ……….. 4 marks (1 mark for each )
1. Performance Measure (P):
o Quantifies how well the agent is performing.
o Example: +100 for grabbing the gold, -100 for dying (falling into a
pit or being eaten by Wumpus), -1 for each move.
2. Environment (E):
o The world in which the agent operates.
Q7   o For Wumpus World: a 4×4 grid of rooms containing pits, Wumpus,
gold, and empty spaces.
a.
3. Actuators (A):
o Tools or actions the agent can perform in the environment.
o For Wumpus World: move forward, turn left/right, grab gold, shoot
arrow, climb out of cave.
4. Sensors (S):
o Percepts through which the agent senses the environment.
o For Wumpus World: stench (Wumpus nearby), breeze (pit nearby),
glitter (gold in room), bump (hits wall), scream (Wumpus killed).
********** 16 **********
--- page 17 ---
RI: A S11 > AW11AN AW 112A 5 We
R2: 74 S21 > AW IIA AW 2Z1A A W220
R3: 7 S12» AW 11 AAW12AR W220
R4: SIZ2>W11IVW12V W13vV W22

Apply modus pones witha S11 & R1

W31
WIZ

3.391 > AW11A 4W12A 7 W221 a AI

_

AW 211A 3W12A 7 We1

Apply And eliminate to this
AW 11, =AW 12,7 W21

Apply modus pones witha S21 & R2

5 SZ1_, aW11AW21A5 W22A W313 921

W11ANA AW 21A7 W220 W31
Apply And eliminate to this

W11,,AW 21, 3 W22, W31

Apply modus pones with $12 & R4
M2 5W11VWi2v WI3V W22 Std

W11VW12V W13Vv W22

2 marks

Apply unit resolution on W11V W12V W13v W22 &AW 11

Apply unit resolution on W12V W13 V W22 &-= W22

Apply unit resolution on wyx6 v W13 &7 Wi?

Hence it is proved that Wumpus is in the room [1, 3]

2 marks

FRR ICR] AC OH
--- page 18 ---
1. The humidity is high *PVQ
or the sky is cloudy.

2. If the sky is cloudy, * QR
then it will rain.

3. If the humidity is high, |, Ps
then it is hot.

4. Itis not hot.

e =§

* Goal: It will rain. (R)

*-PVQ *-PVQ
* QDR * -QVR
- POs * =PVS
Q:7
* =S - 35
b.

Negation of Goal ([=R): It will not rain.

4 marks. statements to FOL, 3 marks for converting to CNF, 3 marks for resolution graph

*PVQ PvQ a

* 5QVR PVR “PVS

* =PVS RVS =S

ie Bing, oe <<

* -R (Goal) (@) Null
After applying Proof by

It will rain proved sha geal: ine ay ia

solved, and it has terminated
with a Null clause

(@). Hence, the goal is
achieved.

FOI 7 QF Cr
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper bfe6f25d9447

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AI_7012/Intelligent Systems - I/ANS_Intelligent Systems - I(702AI0C026)_2025-2026.docx` (+1 identical copies)
- Text: docx (1 page)

````text
Q:1
|
|
Q: 1 a.
| Artificial Intelligence (AI):Intelligence exhibited by machines. It is artificial, meaning it is not real or human. AI   mimics cognitive functions such as perceiving, learning, and reasoning which are   exhibited by humans.
[1 Marks]
Applications of AI (any four):   [4 Marks]
Search engines
AI is everywhere, including search engines, which use intelligent algorithms to provide relevant results.
Medicine and diagnosis
AI assists in diagnosis and image-guided surgery, image analysis, and enhancement in the medical field.
Autonomous vehicles (self-driving cars)
AI is applied in transportation for autonomous vehicle control and pedestrian detection.
Virtual assistants like Siri or Alexa
These are examples of Weak AI that provide human-like experience through programmed   responses.

|
Q: 1 b.
| Describe the characteristics of intelligent agents.   [5 Marks for 5 points]
1. Autonomy:
Intelligent agents operate with a degree of independence. They can perform tasks on their own   without constant human intervention.
Learning Ability:
These agents can learn from their experiences and improve their performance over time, even while executing tasks.
Interaction:
Intelligent agents are capable of interacting with other entities such as humans, other agents, or systems to achieve their objectives.
Adaptability:
They can accommodate new rules and information incrementally, allowing them to adapt to changing environments or requirements.
Goal-Oriented Behavior:
Intelligent agents exhibit behavior that is directed toward achieving specific goals or objectives.
Knowledge-Based:
They utilize knowledge about communication, processes, and entities to make informed decisions and take appropriate actions.

|
Q: 1 c.
|
Minimum 5 points – 1 mark for each point

|
Q: 1 d.
| Predicate Logic (First-Order Logic):.   2 marks   Predicate Logic, also called First-Order Logic (FOL), is an extension of Propositional Logic that allows reasoning about objects, their properties, and relationships.
Unlike propositional logic, which deals with simple true/false statements, FOL can represent statements like “All humans are mortal” or “Some students like mathematics.”
Types of Quantifiers in FOL:   3 marks
Universal Quantifier (∀):
Symbol: ∀
Meaning: “For all” or “Every”
Example:
∀x (Human(x) → Mortal(x))
Translation: “For every x, if x is a human, then x is mortal.”
Existential Quantifier (∃):
Symbol: ∃
Meaning: “There exists” or “Some”
Example:
∃x (Student(x) ∧ LikesMath(x))
Translation: “There exists at least one x such that x is a student and x likes mathematics.”
|
Q:2
| Answer briefly:
|
Q: 2 a.
| Weak AI or Narrow AI or Artificial Narrow Intelligence (ANI)
| Strong AI or Artificial General Intelligence (AGI)
|
Intelligent at completing a specific task
| Exhibits human intelligence
|
AI applied to a specific domain
| It can understand, perceive, think, act, plan, solve problems etc like a human being does
|
They give human like experience, but it is just a simulation
| They have self awareness
|
They often have programmed response
| They can interact and operate a wide variety of independent and unrelated tasks
|
Examples: language translators, virtual assistants, self driving cars, AI powered web searches, recommendation engines, intelligent spam filters
| Can learn new tasks to solve new problems
|
Example Siri or Alexa, advanced chess programs
| Machines that are indistinguishable from human mind
|

Minimum 5 points – 1 mark for each point
|
Q: 2 b.
|   Structure of Agent (2 marks):
AI designs an agent program to implement the agent function.
Agent = Architecture + Program
Architecture: Physical computing device with sensors and actuators.
Program: Implements the agent function.
Agent Program vs Agent Function (3 marks):
Agent Program:
Takes current percept as input from sensors.
Returns action as output to actuators.
Agent Function:
Maps entire percept history to actions.
More abstract and theoretical than the agent program.

|
Q: 2 c.

| Aspect
| A* Search Algorithm
| AO* Search Algorithm
|
Graph Type
| OR-graph
| AND-OR graph
|
Goal
| Finds a single optimal solution path
| Finds solutions that may involve multiple sub-goals (AND conditions)
|
Optimality
| Provides optimal solution
| May not always provide optimal solution
|
Memory Usage
| Requires more memory as it stores all generated nodes
| Requires less memory compared to A*
|
Loop Handling
| Can go into infinite loops if not handled properly
| Avoids infinite loops due to structured decomposition
|
Use Case
| Suitable for problems with a single goal and linear path
| Suitable for problems that can be decomposed into sub-problems with AND/OR dependencies
|
Evaluation Function
| Uses: f(n)=g(n)+h(n)where:
- g(n): cost from start to current node
- h(n): estimated cost to goal
| Also uses: f(n)=g(n)+h(n)but applies it over AND/OR branches collectively
|
Example
| Pathfinding in maps, puzzle solving
| Planning tasks with multiple dependencies,
decision trees
|
4 marks for difference (minimum 4 points)

6 marks for solving   (1 mark for each step and 1 mark for diagram)
|
Q:3
| Answer briefly:
|
Q: 3 a.
| Simple Reflex Agent   [2 Marks]
A Simple Reflex Agent selects actions based on the current percept, ignoring the rest of the percept history. It operates using condition-action rules (also known as "if-then" rules).
Working:
The agent perceives the environment through sensors.
It applies a rule to the current percept.
Executes an action using actuators based on the rule.
Characteristics:
Works well in fully observable environments.
Does not maintain any internal state.
Limited intelligence and adaptability.

2. Model-Based Reflex Agent   [2 Marks]
A Model-Based Reflex Agent improves upon the simple reflex agent by maintaining some internal state to keep track of the partially observable environment.
Working:
Maintains an internal model of the world.
Updates the internal state based on percepts and the model of how the world works.
Chooses actions based on the current percept and internal state.
Characteristics:
Can handle partially observable environments.
Uses a model of the world and internal state to make decisions.
More flexible and intelligent than simple reflex agents.
[1 Mark for diagram]

|
Q: 3 b.
| Hill Climbing Algorithm:   [2 Marks]
Hill Climbing is a local search algorithm that continuously moves in the direction of increasing value (or decreasing cost) to find the peak (or optimal solution). It evaluates the neighboring states and selects the one with the best value.
It is also known as greedy local search.
It terminates when it reaches a state where no neighbor has a better value.

Problems in Hill Climbing and Their Solutions:   [3 Marks]
Local Maximum:
Problem: A peak that is higher than neighboring states but lower than the global maximum.
Solution: Use backtracking to explore alternative paths or maintain a list of promising paths.
Plateau:
Problem: A flat area where neighboring states have the same value, making it hard to determine the direction.
Solution: Take larger or random steps to escape the plateau and reach a region with gradient.
Ridges:
Problem: A slope that is higher than surrounding areas but cannot be climbed directly due to its orientation.
Solution: Use bidirectional search or allow movement in multiple directions to navigate the ridge.

|
Q: 3 c.
| Backtracking can be improved by using heuristics, such as choosing the most constrained variable or the least constraining value to guide the search and reduce the number of backtracks.
The efficiency of the backtracking algorithm can be improved using the Most Constrained Variable (MCV) and Least Constraining Value (LCV) methods. In MCV, we select the variable that has the fewest possible values left to assign.
This helps detect conflicts early and reduces unnecessary search, as we try to assign the hardest variable first. In LCV, when assigning a value to a variable, we choose the one that leaves the most options open for other variables.
This helps keep future choices flexible and reduces the chances of backtracking later. Together, these methods make the search process faster and more efficient.
3 marks –explanation
Most Constrained Variable: SA (South Australia) should be colored first.
1 mark

6 marks for backtracking solving
1 mark for each assignment

|
Q:4
| Answer briefly:
|
Q: 4 a.
| Crypt arithmetic problems are mathematical puzzles in which the digits are replaced by letters of the alphabets. Crypt arithmetic Problem is a type of constraint satisfaction problem where the game is about digits and its unique replacement either with alphabets or other symbols. In crypt arithmetic problem, the digits 0 9 get substituted by some possible alphabets or symbols. The task in crypt arithmetic problem is to substitute each digit with an alphabet to get the result arithmetically correct.   …………… 2 marks
The rules or constraints on a crypt arithmetic problem are as follows:
There should be a unique digit to be replaced with a unique alphabet
The result should satisfy the predefined arithmetic rules i e 2 2 4
Digits should be from 0 9 only
There should be only one carry forward, while performing the addition
operation on a problem
The problem can be solved from both sides, i e left hand side (L H S), or right hand side (R H S)
…………… 2 marks
Step 1   1 mark
Here obviously J = 1 as max carry allowed it
(nothing) + M = O, i.e. 0 + M = O this should have had been M only
It means that there is 1 carry coming from previous step
Also this M + 1 (carry) = O, is generating 1 carry to next step
This means M + 1 > 10, this is only possible when M = 9
=> O = M + 1 = 9 + 0 = 0 (1 carry)
M A C
+ M A A R
-----------
J O C K O
Step 2   2 marks
C + R = 0
Since, this is at units place there can be no carry from previous step
Possible values of (C, R) can be (2, 8), (3,7), (4, 6), (6,4), (7,3), (2,8)
Lets assume, first case C = 2 and R = 8 in that case C + R, will generate 1 carry to next step A + A = K. The new problem looks like this –
1 1
9 A C
+ 9 A A R
-----------
1 0 C K 0
Step 3   2 mark
Thus, A + A + 1 (Carry) = K
Also, 9 + A = 2, this is possible in two ways
If, A = 3 (no carry from previous step) 9 + 3 = 2 (1 carry to next step)
If, A = 2 (1 carry from previous step) but C value is already assumed to be 2, so this is not possible thus, A has to be 3
Thus K = 3 + 3 + 1 = 7
All values are fetched and there is no conflict.
1 1   1
9 A 2
+ 9 A A 8
-----------
1 0 2 K 0
Step 4   1 mark
Thus, 3 A + 2 M + 2 C = 3(3) + 2(9) + 2(2) = 9 + 18 + 4 = 31
1 1   1
9 3 2
+ 9 3 3 8
-----------
1 0 2 7 0

|
Q: 4 b.
|
   5 mark → Correctly finding alpha beta values at each level .
   1 mark → Correctly calculating the value at the root node.
   2 mark → Correctly identifying pruned nodes.
   2 mark → Clear step-by-step presentation.
|

|
|
Q5
| Answer briefly:
|
Q: 5 a.
| A normal search problem and a game (adversarial search) differ mainly in the type of environment and the presence of opponents.
1. Definition (1 mark)
Normal Search:
A process where a single agent searches for a sequence of actions to reach a goal.
Example: Pathfinding, planning, or scheduling.
Game (Adversarial Search):
A situation where two or more agents compete with conflicting goals in the same search space.
2. Presence of Adversary (1 mark)
In a normal search, there is no opponent; the agent acts alone.
In a game, an adversary (opponent) exists who tries to minimize your success (e.g., MAX vs. MIN player).
3. Evaluation Function (1 mark)
Normal Search: Evaluation is based on cost or distance to the goal.
Game Search: Evaluation is based on the goodness of a game position (e.g., win/loss/draw).
4. Optimality of Solution (1 mark)
In normal search, heuristic methods can find an optimal solution.
In games, the optimal move depends on the opponent’s response.
5. Examples (1 mark)
Normal Search: Planning, route finding, or scheduling tasks.
Game Search: Chess, Tic-Tac-Toe, or Checkers.
|
Q:5 b.
| Constraint Satisfaction Problem is a fundamental topic in artificial intelligence that deals with solving problems by identifying constraints and finding solutions that satisfy those constraints. ……………. 2 marks
In artificial intelligence and operations research, constraint satisfaction is the process of finding a solution to a set of constraints that impose conditions that the variables must satisfy.
CSP is defined by a set of variables X1 X2 …… Xn and set of conditions
C1, C2,…. Cn such that each of the variables Xi has a non empty domain Di of possible values
Variables: A finite set of Variables V1 ,V2 ……… Vn
Domain: Each Variable has a domain D1 ,D2 …… Dn from which it can take a value
Constraints:   A finite set of satisfaction constraints C1 ,C2….. Cn
For example, We need to color each country as Red, Green, Blue in such a way that no neighboring country has the same colors.

…   ……….. 3 marks to explain Variable, domain and constrain with example
|
Q: 5 c.
| 1. symbolMeaning   2 marks
TTeacher is present
LLecture is conducted
AAttendance is taken
BStudents bunk the next class
CLecture is cancelled
Step (b): Convert each statement into propositional logic….5 marks (1 for each)
If the teacher is present, the lecture will be conducted: T → L
If the lecture is conducted, attendance will be taken: L → A
If attendance is taken, students will not bunk the next class: A → ¬B
If the teacher is absent, the lecture will be cancelled: ¬T → C
The lecture was conducted, but attendance was not taken: L ∧ ¬A
Step (c): Logical Analysis   …………. 2 marks
From statement (2): L → A (If lecture is conducted, attendance will be taken)
But we are told that: L ∧ ¬A (Lecture conducted, attendance not taken)
This contradicts statement (2).
For L → A to be true, if L is true then A must also be true — but A is false here.
Therefore, L → A must not hold true in this situation, meaning the lecture being conducted might not be due to the normal condition (T → L).
It could be a special case, for example, a guest lecture or class conducted without attendance.
Now, check statement (1):
T → L
We have L true, but this doesn’t confirm T (since the converse of implication isn’t necessarily true).
So, we cannot directly say T is true.
However, from (5) we know attendance not taken, which violates L → A — implying something abnormal in the usual teaching pattern.
Hence, it’s likely that the regular teacher (T) was absent, and someone else conducted the class (hence no attendance).
Teacher was absent (¬T)
Lecture was conducted (L), but attendance not taken (¬A), which breaks the usual implication chain.
……………. 1 mark for final conclusion
|
Q: 6
|
|
Q:6 b.
| (a) Translation into Predicate Logic (3 Marks)

1 mark for elimination of implication
1 marks for standardize variable
1 mark for move negation inwards
2 marks for skolemization
2 marks for droping quantifier

|
Q:6 a.
| (a) Greedy Best-First Search Algorithm:   ………… 4 marks
Greedy Best-First Search is an informed search algorithm that expands the node that appears to be closest to the goal, using a heuristic function h(n).
Working:
It evaluates nodes by using the heuristic function:
f(n)=h(n)

where:
h(n)is the estimated cost from node nto the goal.
The algorithm always selects the node with the lowest heuristic value.
It uses OPEN and CLOSED lists:
OPEN: Nodes to be explored.
CLOSED: Nodes already explored.
Steps:
Initialize the OPEN list with the start node.
Repeat until the goal is found or OPEN is empty:
Remove the node with the lowest h(n)from OPEN.
Add it to CLOSED.
Expand the node and add its children to OPEN.
If a child is the goal, return the path.

Advantages:
Simple and easy to implement.
Fast and efficient in many cases.
Requires less memory than other algorithms.

Disadvantages:
Not guaranteed to find the optimal solution.
Can get stuck in local optima.
Depends heavily on the quality of the heuristic function.

6 marks for solving

|

|
|
Q7 a.
| For Wumpus World:   ……….. 4 marks (1 mark for each )
Performance Measure (P):
Quantifies how well the agent is performing.
Example: +100 for grabbing the gold, -100 for dying (falling into a pit or being eaten by Wumpus), -1 for each move.
Environment (E):
The world in which the agent operates.
For Wumpus World: a 4×4 grid of rooms containing pits, Wumpus, gold, and empty spaces.
Actuators (A):
Tools or actions the agent can perform in the environment.
For Wumpus World: move forward, turn left/right, grab gold, shoot arrow, climb out of cave.
Sensors (S):
Percepts through which the agent senses the environment.
For Wumpus World: stench (Wumpus nearby), breeze (pit nearby), glitter (gold in room), bump (hits wall), scream (Wumpus killed).
………………………………………………………………………2 marks
…………………………………………………………………… 2 marks
…………………………………………………………………… 2 marks
|
Q:7 b.
|
4 marks. statements to FOL, 3 marks for converting to CNF, 3 marks for resolution graph

|
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 013e176a5c38

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AI_7012/Intelligent Systems - I/ANS_Intelligent Systems - I(702AI0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: mixed (18 pages), mean OCR confidence 67.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Intelligent Systems - I
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q:1
Artificial Intelligence (AI):Intelligence exhibited by machines. It is artificial, meaning it
is not real or human. AI mimics cognitive functions such as perceiving, learning, and
reasoning which are exhibited by humans.
[1 Marks]
Applications of AI (any four):   [4 Marks]
1. Search engines
AI is everywhere, including search engines, which use intelligent algorithms to
provide relevant results.
Q: 1   2. Medicine and diagnosis
a.   AI assists in diagnosis and image-guided surgery, image analysis, and
enhancement in the medical field.
3. Autonomous vehicles (self-driving cars)
AI is applied in transportation for autonomous vehicle control and pedestrian
detection.
4. Virtual assistants like Siri or Alexa
These are examples of Weak AI that provide human-like experience through
programmed responses.
Describe the characteristics of intelligent agents.   [5 Marks for 5 points]
1. 1. Autonomy:
Intelligent agents operate with a degree of independence. They can perform tasks
on their own   without constant human intervention.
Q: 1   2. Learning Ability:
b.   These agents can learn from their experiences and improve their performance over
time, even while executing tasks.
3. Interaction:
Intelligent agents are capable of interacting with other entities such as humans,
other agents, or systems to achieve their objectives.
********** 1 **********
--- page 2 ---
4. Adaptability:
They can accommodate new rules and information incrementally, allowing them
to adapt to changing environments or requirements.
5. Goal-Oriented Behavior:
Intelligent agents exhibit behavior that is directed toward achieving specific goals
or objectives.
6. Knowledge-Based:
They utilize knowledge about communication, processes, and entities to make
informed decisions and take appropriate actions.
Q: 1
c.
Minimum 5 points – 1 mark for each point
Predicate Logic (First-Order Logic):.   2 marks
Predicate Logic, also called First-Order Logic (FOL), is an extension of
Propositional Logic that allows reasoning about objects, their properties, and
relationships.
• Unlike propositional logic, which deals with simple true/false statements,
FOL can represent statements like “All humans are mortal” or “Some
students like mathematics.”
Types of Quantifiers in FOL:   3 marks
1. Universal Quantifier (∀):
Q: 1
o Symbol: ∀
d.
o Meaning: “For all” or “Every”
o Example:
▪ ∀x (Human(x) → Mortal(x))
▪   Translation: “For every x, if x is a human, then x is mortal.”
2. Existential Quantifier (∃):
o Symbol: ∃
o Meaning: “There exists” or “Some”
o Example:
▪ ∃x (Student(x) ∧ LikesMath(x))
▪   Translation: “There exists at least one x such that x is a
student and x likes mathematics.”
********** 2 **********
--- page 3 ---
Q:2   Answer briefly:
Weak AI or Narrow AI or Artificial   Strong AI or Artificial General
Narrow Intelligence (ANI)   Intelligence (AGI)
Intelligent at completing a specific task   Exhibits human intelligence
It can understand, perceive, think, act, plan,
AI applied to a specific domain
solve problems etc like a human being does
They give human like experience, but it is
They have self awareness
just a simulation
Q: 2   They can interact and operate a wide variety
They often have programmed response
a.   of independent and unrelated tasks
Examples: language translators, virtual
assistants, self driving cars, AI powered web
Can learn new tasks to solve new problems
searches, recommendation engines,
intelligent spam filters
Example Siri or Alexa, advanced chess   Machines that are indistinguishable from
programs   human mind
Minimum 5 points – 1 mark for each point
Structure of Agent (2 marks):
• AI designs an agent program to implement the agent function.
• Agent = Architecture + Program
o Architecture: Physical computing device with sensors and actuators.
o Program: Implements the agent function.
Agent Program vs Agent Function (3 marks):
Q: 2
• Agent Program:
b.   o Takes current percept as input from sensors.
o Returns action as output to actuators.
• Agent Function:
o Maps entire percept history to actions.
o More abstract and theoretical than the agent program.
Q: 2
c.   Aspect   A* Search Algorithm   AO* Search Algorithm
Graph Type OR-graph   AND-OR graph
Finds a single optimal   Finds solutions that may involve multiple
Goal
solution path   sub-goals (AND conditions)
Optimality   Provides optimal solution May not always provide optimal solution
Memory   Requires more memory as
Requires less memory compared to A*
Usage   it stores all generated nodes
Loop   Can go into infinite loops if Avoids infinite loops due to structured
Handling   not handled properly   decomposition
********** 3 **********
--- page 4 ---
Suitable for problems with Suitable for problems that can be
Use Case   a single goal and linear   decomposed into sub-problems with
path   AND/OR dependencies
Uses: 𝑓(𝑛) = 𝑔(𝑛) +
ℎ(𝑛)where:
Evaluation   - 𝑔(𝑛): cost from start to   Also uses: 𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)but applies
Function   current node   it over AND/OR branches collectively
- ℎ(𝑛): estimated cost to
goal
Pathfinding in maps, puzzle Planning tasks with multiple dependencies,
Example
solving   decision trees
4 marks for difference (minimum 4 points)
6 marks for solving (1 mark for each step and 1 mark for diagram)
Q:3   Answer briefly:
Simple Reflex Agent   [2 Marks]
Q: 3 A Simple Reflex Agent selects actions based on the current percept, ignoring the rest of
a.   the percept history. It operates using condition-action rules (also known as "if-then"
rules).
********** 4 **********
--- page 5 ---
Working:
• The agent perceives the environment through sensors.
•   It applies a rule to the current percept.
•   Executes an action using actuators based on the rule.
Characteristics:
• Works well in fully observable environments.
• Does not maintain any internal state.
•   Limited intelligence and adaptability.
2. Model-Based Reflex Agent   [2
Marks]
A Model-Based Reflex Agent improves upon the simple reflex agent by maintaining
some internal state to keep track of the partially observable environment.
Working:
•   Maintains an internal model of the world.
•   Updates the internal state based on percepts and the model of how the world
works.
•   Chooses actions based on the current percept and internal state.
Characteristics:
• Can handle partially observable environments.
•   Uses a model of the world and internal state to make decisions.
• More flexible and intelligent than simple reflex agents.
[1 Mark for diagram]
********** 5 **********
--- page 6 ---
Hill Climbing Algorithm:   [2 Marks]
Hill Climbing is a local search algorithm that continuously moves in the direction of
increasing value (or decreasing cost) to find the peak (or optimal solution). It evaluates the
neighboring states and selects the one with the best value.
•   It is also known as greedy local search.
•   It terminates when it reaches a state where no neighbor has a better value.
Q: 3
b.
Problems in Hill Climbing and Their Solutions:   [3 Marks]
1. Local Maximum:
o Problem: A peak that is higher than neighboring states but lower than the
global maximum.
o   Solution: Use backtracking to explore alternative paths or maintain a list
of promising paths.
2. Plateau:
o Problem: A flat area where neighboring states have the same value,
making it hard to determine the direction.
o   Solution: Take larger or random steps to escape the plateau and reach a
region with gradient.
3. Ridges:
o Problem: A slope that is higher than surrounding areas but cannot be
climbed directly due to its orientation.
o   Solution: Use bidirectional search or allow movement in multiple
directions to navigate the ridge.
Backtracking can be improved by using heuristics, such as choosing the most
constrained variable or the least constraining value to guide the search and reduce
the number of backtracks.
The efficiency of the backtracking algorithm can be improved using the Most
Constrained Variable (MCV) and Least Constraining Value (LCV) methods. In
Q: 3 MCV, we select the variable that has the fewest possible values left to assign.
c.
This helps detect conflicts early and reduces unnecessary search, as we try to assign
the hardest variable first. In LCV, when assigning a value to a variable, we choose
the one that leaves the most options open for other variables.
This helps keep future choices flexible and reduces the chances of backtracking later.
Together, these methods make the search process faster and more efficient.
********** 6 **********
--- page 7 ---
3 marks –explanation
Most Constrained Variable: SA (South Australia) should be colored first.
1 mark
6 marks for backtracking solving
1 mark for each assignment
********** 7 **********
--- page 8 ---
Q:4   Answer briefly:
Crypt arithmetic problems are mathematical puzzles in which the digits
are replaced by letters of the alphabets. Crypt arithmetic Problem is a type
of constraint satisfaction problem where the game is about digits and its
unique replacement either with alphabets or other symbols. In crypt
arithmetic problem, the digits 0 9 get substituted by some possible
alphabets or symbols. The task in crypt arithmetic problem is to substitute
each digit with an alphabet to get the result arithmetically correct.
…………… 2 marks
The rules or constraints on a crypt arithmetic problem are as follows:
• There should be a unique digit to be replaced with a unique
alphabet
• The result should satisfy the predefined arithmetic rules i e 2 2 4
• Digits should be from 0 9 only
• There should be only one carry forward, while performing the
addition
• operation on a problem
• The problem can be solved from both sides, i e left hand side (L H
S), or right hand side (R H S)
…………… 2 marks
Step 1   1 mark
Q: 4
a.   • Here obviously J = 1 as max carry allowed it
• (nothing) + M = O, i.e. 0 + M = O this should have had been M
only
•   It means that there is 1 carry coming from previous step
• Also this M + 1 (carry) = O, is generating 1 carry to next step
• This means M + 1 > 10, this is only possible when M = 9
• => O = M + 1 = 9 + 0 = 0 (1 carry)
M A C
+ M A A R
-----------
J O C K O
Step 2   2 marks
C + R = 0
Since, this is at units place there can be no carry from previous step
Possible values of (C, R) can be (2, 8), (3,7), (4, 6), (6,4), (7,3), (2,8)
Lets assume, first case C = 2 and R = 8 in that case C + R, will generate 1
carry to next step A + A = K. The new problem looks like this –
********** 8 **********
--- page 9 ---
1 1
9 A C
+ 9 A A R
-----------
1 0 C K 0
Step 3   2 mark
• Thus, A + A + 1 (Carry) = K
• Also, 9 + A = 2, this is possible in two ways
•   If, A = 3 (no carry from previous step) 9 + 3 = 2 (1 carry to next
step)
•   If, A = 2 (1 carry from previous step) but C value is already
assumed to be 2, so this is not possible thus, A has to be 3
• Thus K = 3 + 3 + 1 = 7
All values are fetched and there is no conflict.
1 1   1
9 A 2
+ 9 A A 8
-----------
1 0 2 K 0
Step 4   1 mark
• Thus, 3 A + 2 M + 2 C = 3(3) + 2(9) + 2(2) = 9 + 18 + 4 = 31
1 1   1
9 3 2
+ 9 3 3 8
-----------
1 0 2 7 0
********** 9 **********
--- page 10 ---
Q: 4
b.
• 5 mark → Correctly finding alpha beta values at each level .
• 1 mark → Correctly calculating the value at the root node.
• 2 mark → Correctly identifying pruned nodes.
• 2 mark → Clear step-by-step presentation.
Q5   Answer briefly:
A normal search problem and a game (adversarial search) differ mainly in the type
of environment and the presence of opponents.
Q: 5
1. Definition (1 mark)
a.
• Normal Search:
A process where a single agent searches for a sequence of actions to reach a
********** 10 **********
--- page 11 ---
goal.
Example: Pathfinding, planning, or scheduling.
• Game (Adversarial Search):
A situation where two or more agents compete with conflicting goals in the
same search space.
2. Presence of Adversary (1 mark)
•   In a normal search, there is no opponent; the agent acts alone.
•   In a game, an adversary (opponent) exists who tries to minimize your
success (e.g., MAX vs. MIN player).
3. Evaluation Function (1 mark)
• Normal Search: Evaluation is based on cost or distance to the goal.
• Game Search: Evaluation is based on the goodness of a game position (e.g.,
win/loss/draw).
4. Optimality of Solution (1 mark)
•   In normal search, heuristic methods can find an optimal solution.
•   In games, the optimal move depends on the opponent’s response.
5. Examples (1 mark)
• Normal Search: Planning, route finding, or scheduling tasks.
• Game Search: Chess, Tic-Tac-Toe, or Checkers.
Constraint Satisfaction Problem is a fundamental topic in artificial intelligence that
deals with solving problems by identifying constraints and finding solutions that
satisfy those constraints. ……………. 2 marks
In artificial intelligence and operations research, constraint satisfaction is the
process of finding a solution to a set of constraints that impose conditions that the
variables must satisfy.
CSP is defined by a set of variables X1 X2 …… Xn and set of conditions
Q:5
C1, C2,…. Cn such that each of the variables Xi has a non empty domain Di of
b.
possible values
Variables: A finite set of Variables V1 ,V2 ……… Vn
Domain: Each Variable has a domain D1 ,D2 …… Dn from which it can take a
value
Constraints: A finite set of satisfaction constraints C1 ,C2….. Cn
For example, We need to color each country as Red, Green, Blue in such a way
that no neighboring country has the same colors.
********** 11 **********
--- page 12 ---
… ……….. 3 marks to explain Variable, domain and constrain with example
1. symbol   Meaning   2 marks
T   Teacher is present
L   Lecture is conducted
A   Attendance is taken
B   Students bunk the next class
C   Lecture is cancelled
Step (b): Convert each statement into propositional logic….5 marks (1 for each)
If the teacher is present, the lecture will be conducted: T → L
If the lecture is conducted, attendance will be taken: L → A
If attendance is taken, students will not bunk the next class: A → ¬B
If the teacher is absent, the lecture will be cancelled: ¬T → C
The lecture was conducted, but attendance was not taken: L ∧ ¬A
Step (c): Logical Analysis …………. 2 marks
Q: 5
From statement (2): L → A (If lecture is conducted, attendance will be taken)
c.
But we are told that: L ∧ ¬A (Lecture conducted, attendance not taken)
This contradicts statement (2).
For L → A to be true, if L is true then A must also be true — but A is false here.
Therefore, L → A must not hold true in this situation, meaning the lecture being
conducted might not be due to the normal condition (T → L).
It could be a special case, for example, a guest lecture or class conducted without
attendance.
Now, check statement (1):
T → L
We have L true, but this doesn’t confirm T (since the converse of implication isn’t
necessarily true).
So, we cannot directly say T is true.
However, from (5) we know attendance not taken, which violates L → A —
implying something abnormal in the usual teaching pattern.
********** 12 **********
--- page 13 ---
Hence, it’s likely that the regular teacher (T) was absent, and someone else
conducted the class (hence no attendance).
• Teacher was absent (¬T)
•   Lecture was conducted (L), but attendance not taken (¬A), which breaks
the usual implication chain.
……………. 1 mark for final conclusion
Q: 6
(a) Translation into Predicate Logic (3 Marks)
Q:6
b.
********** 13 **********
--- page 14 ---
• 1 mark for elimination of implication
• 1 marks for standardize variable
• 1 mark for move negation inwards
• 2 marks for skolemization
• 2 marks for droping quantifier
********** 14 **********
--- page 15 ---
(a) Greedy Best-First Search Algorithm: ………… 4 marks
Greedy Best-First Search is an informed search algorithm that expands the node
that appears to be closest to the goal, using a heuristic function h(n).
Working:
It evaluates nodes by using the heuristic function:
f(n)=h(n)
where:
h(n)is the estimated cost from node nto the goal.
The algorithm always selects the node with the lowest heuristic value.
It uses OPEN and CLOSED lists:
OPEN: Nodes to be explored.
CLOSED: Nodes already explored.
Steps:
Initialize the OPEN list with the start node.
Repeat until the goal is found or OPEN is empty:
Remove the node with the lowest h(n)from OPEN.
Add it to CLOSED.
Expand the node and add its children to OPEN.
If a child is the goal, return the path.
Advantages:
Simple and easy to implement.
Fast and efficient in many cases.
Q:6
Requires less memory than other algorithms.
a.
Disadvantages:
Not guaranteed to find the optimal solution.
Can get stuck in local optima.
Depends heavily on the quality of the heuristic function.
6 marks for solving
********** 15 **********
--- page 16 ---
For Wumpus World:   ……….. 4 marks (1 mark for each )
1. Performance Measure (P):
o Quantifies how well the agent is performing.
o Example: +100 for grabbing the gold, -100 for dying (falling into a
pit or being eaten by Wumpus), -1 for each move.
2. Environment (E):
o The world in which the agent operates.
Q7   o For Wumpus World: a 4×4 grid of rooms containing pits, Wumpus,
gold, and empty spaces.
a.
3. Actuators (A):
o Tools or actions the agent can perform in the environment.
o For Wumpus World: move forward, turn left/right, grab gold, shoot
arrow, climb out of cave.
4. Sensors (S):
o Percepts through which the agent senses the environment.
o For Wumpus World: stench (Wumpus nearby), breeze (pit nearby),
glitter (gold in room), bump (hits wall), scream (Wumpus killed).
********** 16 **********
--- page 17 ---
RI: A S11 > AW11AN AW 112A 5 We
R2: 74 S21 > AW IIA AW 2Z1A A W220
R3: 7 S12» AW 11 AAW12AR W220
R4: SIZ2>W11IVW12V W13vV W22

Apply modus pones witha S11 & R1

W31
WIZ

3.391 > AW11A 4W12A 7 W221 a AI

_

AW 211A 3W12A 7 We1

Apply And eliminate to this
AW 11, =AW 12,7 W21

Apply modus pones witha S21 & R2

5 SZ1_, aW11AW21A5 W22A W313 921

W11ANA AW 21A7 W220 W31
Apply And eliminate to this

W11,,AW 21, 3 W22, W31

Apply modus pones with $12 & R4
M2 5W11VWi2v WI3V W22 Std

W11VW12V W13Vv W22

2 marks

Apply unit resolution on W11V W12V W13v W22 &AW 11

Apply unit resolution on W12V W13 V W22 &-= W22

Apply unit resolution on wyx6 v W13 &7 Wi?

Hence it is proved that Wumpus is in the room [1, 3]

2 marks

FRR ICR] AC OH
--- page 18 ---
1. The humidity is high *PVQ
or the sky is cloudy.

2. If the sky is cloudy, * QR
then it will rain.

3. If the humidity is high, |, Ps
then it is hot.

4. Itis not hot.

e =§

* Goal: It will rain. (R)

*-PVQ *-PVQ
* QDR * -QVR
- POs * =PVS
Q:7
* =S - 35
b.

Negation of Goal ([=R): It will not rain.

4 marks. statements to FOL, 3 marks for converting to CNF, 3 marks for resolution graph

*PVQ PvQ a

* 5QVR PVR “PVS

* =PVS RVS =S

ie Bing, oe <<

* -R (Goal) (@) Null
After applying Proof by

It will rain proved sha geal: ine ay ia

solved, and it has terminated
with a Null clause

(@). Hence, the goal is
achieved.

FOI 7 QF Cr
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper c87df288e363

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MBATech_AI_7051/Intelligent Systems - I/ANS_Intelligent Systems - I(702AI0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: mixed (18 pages), mean OCR confidence 67.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Intelligent Systems - I
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q:1
Artificial Intelligence (AI):Intelligence exhibited by machines. It is artificial, meaning it
is not real or human. AI mimics cognitive functions such as perceiving, learning, and
reasoning which are exhibited by humans.
[1 Marks]
Applications of AI (any four):   [4 Marks]
1. Search engines
AI is everywhere, including search engines, which use intelligent algorithms to
provide relevant results.
Q: 1   2. Medicine and diagnosis
a.   AI assists in diagnosis and image-guided surgery, image analysis, and
enhancement in the medical field.
3. Autonomous vehicles (self-driving cars)
AI is applied in transportation for autonomous vehicle control and pedestrian
detection.
4. Virtual assistants like Siri or Alexa
These are examples of Weak AI that provide human-like experience through
programmed responses.
Describe the characteristics of intelligent agents.   [5 Marks for 5 points]
1. 1. Autonomy:
Intelligent agents operate with a degree of independence. They can perform tasks
on their own   without constant human intervention.
Q: 1   2. Learning Ability:
b.   These agents can learn from their experiences and improve their performance over
time, even while executing tasks.
3. Interaction:
Intelligent agents are capable of interacting with other entities such as humans,
other agents, or systems to achieve their objectives.
********** 1 **********
--- page 2 ---
4. Adaptability:
They can accommodate new rules and information incrementally, allowing them
to adapt to changing environments or requirements.
5. Goal-Oriented Behavior:
Intelligent agents exhibit behavior that is directed toward achieving specific goals
or objectives.
6. Knowledge-Based:
They utilize knowledge about communication, processes, and entities to make
informed decisions and take appropriate actions.
Q: 1
c.
Minimum 5 points – 1 mark for each point
Predicate Logic (First-Order Logic):.   2 marks
Predicate Logic, also called First-Order Logic (FOL), is an extension of
Propositional Logic that allows reasoning about objects, their properties, and
relationships.
• Unlike propositional logic, which deals with simple true/false statements,
FOL can represent statements like “All humans are mortal” or “Some
students like mathematics.”
Types of Quantifiers in FOL:   3 marks
1. Universal Quantifier (∀):
Q: 1
o Symbol: ∀
d.
o Meaning: “For all” or “Every”
o Example:
▪ ∀x (Human(x) → Mortal(x))
▪   Translation: “For every x, if x is a human, then x is mortal.”
2. Existential Quantifier (∃):
o Symbol: ∃
o Meaning: “There exists” or “Some”
o Example:
▪ ∃x (Student(x) ∧ LikesMath(x))
▪   Translation: “There exists at least one x such that x is a
student and x likes mathematics.”
********** 2 **********
--- page 3 ---
Q:2   Answer briefly:
Weak AI or Narrow AI or Artificial   Strong AI or Artificial General
Narrow Intelligence (ANI)   Intelligence (AGI)
Intelligent at completing a specific task   Exhibits human intelligence
It can understand, perceive, think, act, plan,
AI applied to a specific domain
solve problems etc like a human being does
They give human like experience, but it is
They have self awareness
just a simulation
Q: 2   They can interact and operate a wide variety
They often have programmed response
a.   of independent and unrelated tasks
Examples: language translators, virtual
assistants, self driving cars, AI powered web
Can learn new tasks to solve new problems
searches, recommendation engines,
intelligent spam filters
Example Siri or Alexa, advanced chess   Machines that are indistinguishable from
programs   human mind
Minimum 5 points – 1 mark for each point
Structure of Agent (2 marks):
• AI designs an agent program to implement the agent function.
• Agent = Architecture + Program
o Architecture: Physical computing device with sensors and actuators.
o Program: Implements the agent function.
Agent Program vs Agent Function (3 marks):
Q: 2
• Agent Program:
b.   o Takes current percept as input from sensors.
o Returns action as output to actuators.
• Agent Function:
o Maps entire percept history to actions.
o More abstract and theoretical than the agent program.
Q: 2
c.   Aspect   A* Search Algorithm   AO* Search Algorithm
Graph Type OR-graph   AND-OR graph
Finds a single optimal   Finds solutions that may involve multiple
Goal
solution path   sub-goals (AND conditions)
Optimality   Provides optimal solution May not always provide optimal solution
Memory   Requires more memory as
Requires less memory compared to A*
Usage   it stores all generated nodes
Loop   Can go into infinite loops if Avoids infinite loops due to structured
Handling   not handled properly   decomposition
********** 3 **********
--- page 4 ---
Suitable for problems with Suitable for problems that can be
Use Case   a single goal and linear   decomposed into sub-problems with
path   AND/OR dependencies
Uses: 𝑓(𝑛) = 𝑔(𝑛) +
ℎ(𝑛)where:
Evaluation   - 𝑔(𝑛): cost from start to   Also uses: 𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)but applies
Function   current node   it over AND/OR branches collectively
- ℎ(𝑛): estimated cost to
goal
Pathfinding in maps, puzzle Planning tasks with multiple dependencies,
Example
solving   decision trees
4 marks for difference (minimum 4 points)
6 marks for solving (1 mark for each step and 1 mark for diagram)
Q:3   Answer briefly:
Simple Reflex Agent   [2 Marks]
Q: 3 A Simple Reflex Agent selects actions based on the current percept, ignoring the rest of
a.   the percept history. It operates using condition-action rules (also known as "if-then"
rules).
********** 4 **********
--- page 5 ---
Working:
• The agent perceives the environment through sensors.
•   It applies a rule to the current percept.
•   Executes an action using actuators based on the rule.
Characteristics:
• Works well in fully observable environments.
• Does not maintain any internal state.
•   Limited intelligence and adaptability.
2. Model-Based Reflex Agent   [2
Marks]
A Model-Based Reflex Agent improves upon the simple reflex agent by maintaining
some internal state to keep track of the partially observable environment.
Working:
•   Maintains an internal model of the world.
•   Updates the internal state based on percepts and the model of how the world
works.
•   Chooses actions based on the current percept and internal state.
Characteristics:
• Can handle partially observable environments.
•   Uses a model of the world and internal state to make decisions.
• More flexible and intelligent than simple reflex agents.
[1 Mark for diagram]
********** 5 **********
--- page 6 ---
Hill Climbing Algorithm:   [2 Marks]
Hill Climbing is a local search algorithm that continuously moves in the direction of
increasing value (or decreasing cost) to find the peak (or optimal solution). It evaluates the
neighboring states and selects the one with the best value.
•   It is also known as greedy local search.
•   It terminates when it reaches a state where no neighbor has a better value.
Q: 3
b.
Problems in Hill Climbing and Their Solutions:   [3 Marks]
1. Local Maximum:
o Problem: A peak that is higher than neighboring states but lower than the
global maximum.
o   Solution: Use backtracking to explore alternative paths or maintain a list
of promising paths.
2. Plateau:
o Problem: A flat area where neighboring states have the same value,
making it hard to determine the direction.
o   Solution: Take larger or random steps to escape the plateau and reach a
region with gradient.
3. Ridges:
o Problem: A slope that is higher than surrounding areas but cannot be
climbed directly due to its orientation.
o   Solution: Use bidirectional search or allow movement in multiple
directions to navigate the ridge.
Backtracking can be improved by using heuristics, such as choosing the most
constrained variable or the least constraining value to guide the search and reduce
the number of backtracks.
The efficiency of the backtracking algorithm can be improved using the Most
Constrained Variable (MCV) and Least Constraining Value (LCV) methods. In
Q: 3 MCV, we select the variable that has the fewest possible values left to assign.
c.
This helps detect conflicts early and reduces unnecessary search, as we try to assign
the hardest variable first. In LCV, when assigning a value to a variable, we choose
the one that leaves the most options open for other variables.
This helps keep future choices flexible and reduces the chances of backtracking later.
Together, these methods make the search process faster and more efficient.
********** 6 **********
--- page 7 ---
3 marks –explanation
Most Constrained Variable: SA (South Australia) should be colored first.
1 mark
6 marks for backtracking solving
1 mark for each assignment
********** 7 **********
--- page 8 ---
Q:4   Answer briefly:
Crypt arithmetic problems are mathematical puzzles in which the digits
are replaced by letters of the alphabets. Crypt arithmetic Problem is a type
of constraint satisfaction problem where the game is about digits and its
unique replacement either with alphabets or other symbols. In crypt
arithmetic problem, the digits 0 9 get substituted by some possible
alphabets or symbols. The task in crypt arithmetic problem is to substitute
each digit with an alphabet to get the result arithmetically correct.
…………… 2 marks
The rules or constraints on a crypt arithmetic problem are as follows:
• There should be a unique digit to be replaced with a unique
alphabet
• The result should satisfy the predefined arithmetic rules i e 2 2 4
• Digits should be from 0 9 only
• There should be only one carry forward, while performing the
addition
• operation on a problem
• The problem can be solved from both sides, i e left hand side (L H
S), or right hand side (R H S)
…………… 2 marks
Step 1   1 mark
Q: 4
a.   • Here obviously J = 1 as max carry allowed it
• (nothing) + M = O, i.e. 0 + M = O this should have had been M
only
•   It means that there is 1 carry coming from previous step
• Also this M + 1 (carry) = O, is generating 1 carry to next step
• This means M + 1 > 10, this is only possible when M = 9
• => O = M + 1 = 9 + 0 = 0 (1 carry)
M A C
+ M A A R
-----------
J O C K O
Step 2   2 marks
C + R = 0
Since, this is at units place there can be no carry from previous step
Possible values of (C, R) can be (2, 8), (3,7), (4, 6), (6,4), (7,3), (2,8)
Lets assume, first case C = 2 and R = 8 in that case C + R, will generate 1
carry to next step A + A = K. The new problem looks like this –
********** 8 **********
--- page 9 ---
1 1
9 A C
+ 9 A A R
-----------
1 0 C K 0
Step 3   2 mark
• Thus, A + A + 1 (Carry) = K
• Also, 9 + A = 2, this is possible in two ways
•   If, A = 3 (no carry from previous step) 9 + 3 = 2 (1 carry to next
step)
•   If, A = 2 (1 carry from previous step) but C value is already
assumed to be 2, so this is not possible thus, A has to be 3
• Thus K = 3 + 3 + 1 = 7
All values are fetched and there is no conflict.
1 1   1
9 A 2
+ 9 A A 8
-----------
1 0 2 K 0
Step 4   1 mark
• Thus, 3 A + 2 M + 2 C = 3(3) + 2(9) + 2(2) = 9 + 18 + 4 = 31
1 1   1
9 3 2
+ 9 3 3 8
-----------
1 0 2 7 0
********** 9 **********
--- page 10 ---
Q: 4
b.
• 5 mark → Correctly finding alpha beta values at each level .
• 1 mark → Correctly calculating the value at the root node.
• 2 mark → Correctly identifying pruned nodes.
• 2 mark → Clear step-by-step presentation.
Q5   Answer briefly:
A normal search problem and a game (adversarial search) differ mainly in the type
of environment and the presence of opponents.
Q: 5
1. Definition (1 mark)
a.
• Normal Search:
A process where a single agent searches for a sequence of actions to reach a
********** 10 **********
--- page 11 ---
goal.
Example: Pathfinding, planning, or scheduling.
• Game (Adversarial Search):
A situation where two or more agents compete with conflicting goals in the
same search space.
2. Presence of Adversary (1 mark)
•   In a normal search, there is no opponent; the agent acts alone.
•   In a game, an adversary (opponent) exists who tries to minimize your
success (e.g., MAX vs. MIN player).
3. Evaluation Function (1 mark)
• Normal Search: Evaluation is based on cost or distance to the goal.
• Game Search: Evaluation is based on the goodness of a game position (e.g.,
win/loss/draw).
4. Optimality of Solution (1 mark)
•   In normal search, heuristic methods can find an optimal solution.
•   In games, the optimal move depends on the opponent’s response.
5. Examples (1 mark)
• Normal Search: Planning, route finding, or scheduling tasks.
• Game Search: Chess, Tic-Tac-Toe, or Checkers.
Constraint Satisfaction Problem is a fundamental topic in artificial intelligence that
deals with solving problems by identifying constraints and finding solutions that
satisfy those constraints. ……………. 2 marks
In artificial intelligence and operations research, constraint satisfaction is the
process of finding a solution to a set of constraints that impose conditions that the
variables must satisfy.
CSP is defined by a set of variables X1 X2 …… Xn and set of conditions
Q:5
C1, C2,…. Cn such that each of the variables Xi has a non empty domain Di of
b.
possible values
Variables: A finite set of Variables V1 ,V2 ……… Vn
Domain: Each Variable has a domain D1 ,D2 …… Dn from which it can take a
value
Constraints: A finite set of satisfaction constraints C1 ,C2….. Cn
For example, We need to color each country as Red, Green, Blue in such a way
that no neighboring country has the same colors.
********** 11 **********
--- page 12 ---
… ……….. 3 marks to explain Variable, domain and constrain with example
1. symbol   Meaning   2 marks
T   Teacher is present
L   Lecture is conducted
A   Attendance is taken
B   Students bunk the next class
C   Lecture is cancelled
Step (b): Convert each statement into propositional logic….5 marks (1 for each)
If the teacher is present, the lecture will be conducted: T → L
If the lecture is conducted, attendance will be taken: L → A
If attendance is taken, students will not bunk the next class: A → ¬B
If the teacher is absent, the lecture will be cancelled: ¬T → C
The lecture was conducted, but attendance was not taken: L ∧ ¬A
Step (c): Logical Analysis …………. 2 marks
Q: 5
From statement (2): L → A (If lecture is conducted, attendance will be taken)
c.
But we are told that: L ∧ ¬A (Lecture conducted, attendance not taken)
This contradicts statement (2).
For L → A to be true, if L is true then A must also be true — but A is false here.
Therefore, L → A must not hold true in this situation, meaning the lecture being
conducted might not be due to the normal condition (T → L).
It could be a special case, for example, a guest lecture or class conducted without
attendance.
Now, check statement (1):
T → L
We have L true, but this doesn’t confirm T (since the converse of implication isn’t
necessarily true).
So, we cannot directly say T is true.
However, from (5) we know attendance not taken, which violates L → A —
implying something abnormal in the usual teaching pattern.
********** 12 **********
--- page 13 ---
Hence, it’s likely that the regular teacher (T) was absent, and someone else
conducted the class (hence no attendance).
• Teacher was absent (¬T)
•   Lecture was conducted (L), but attendance not taken (¬A), which breaks
the usual implication chain.
……………. 1 mark for final conclusion
Q: 6
(a) Translation into Predicate Logic (3 Marks)
Q:6
b.
********** 13 **********
--- page 14 ---
• 1 mark for elimination of implication
• 1 marks for standardize variable
• 1 mark for move negation inwards
• 2 marks for skolemization
• 2 marks for droping quantifier
********** 14 **********
--- page 15 ---
(a) Greedy Best-First Search Algorithm: ………… 4 marks
Greedy Best-First Search is an informed search algorithm that expands the node
that appears to be closest to the goal, using a heuristic function h(n).
Working:
It evaluates nodes by using the heuristic function:
f(n)=h(n)
where:
h(n)is the estimated cost from node nto the goal.
The algorithm always selects the node with the lowest heuristic value.
It uses OPEN and CLOSED lists:
OPEN: Nodes to be explored.
CLOSED: Nodes already explored.
Steps:
Initialize the OPEN list with the start node.
Repeat until the goal is found or OPEN is empty:
Remove the node with the lowest h(n)from OPEN.
Add it to CLOSED.
Expand the node and add its children to OPEN.
If a child is the goal, return the path.
Advantages:
Simple and easy to implement.
Fast and efficient in many cases.
Q:6
Requires less memory than other algorithms.
a.
Disadvantages:
Not guaranteed to find the optimal solution.
Can get stuck in local optima.
Depends heavily on the quality of the heuristic function.
6 marks for solving
********** 15 **********
--- page 16 ---
For Wumpus World:   ……….. 4 marks (1 mark for each )
1. Performance Measure (P):
o Quantifies how well the agent is performing.
o Example: +100 for grabbing the gold, -100 for dying (falling into a
pit or being eaten by Wumpus), -1 for each move.
2. Environment (E):
o The world in which the agent operates.
Q7   o For Wumpus World: a 4×4 grid of rooms containing pits, Wumpus,
gold, and empty spaces.
a.
3. Actuators (A):
o Tools or actions the agent can perform in the environment.
o For Wumpus World: move forward, turn left/right, grab gold, shoot
arrow, climb out of cave.
4. Sensors (S):
o Percepts through which the agent senses the environment.
o For Wumpus World: stench (Wumpus nearby), breeze (pit nearby),
glitter (gold in room), bump (hits wall), scream (Wumpus killed).
********** 16 **********
--- page 17 ---
RI: A S11 > AW11AN AW 112A 5 We
R2: 74 S21 > AW IIA AW 2Z1A A W220
R3: 7 S12» AW 11 AAW12AR W220
R4: SIZ2>W11IVW12V W13vV W22

Apply modus pones witha S11 & R1

W31
WIZ

3.391 > AW11A 4W12A 7 W221 a AI

_

AW 211A 3W12A 7 We1

Apply And eliminate to this
AW 11, =AW 12,7 W21

Apply modus pones witha S21 & R2

5 SZ1_, aW11AW21A5 W22A W313 921

W11ANA AW 21A7 W220 W31
Apply And eliminate to this

W11,,AW 21, 3 W22, W31

Apply modus pones with $12 & R4
M2 5W11VWi2v WI3V W22 Std

W11VW12V W13Vv W22

2 marks

Apply unit resolution on W11V W12V W13v W22 &AW 11

Apply unit resolution on W12V W13 V W22 &-= W22

Apply unit resolution on wyx6 v W13 &7 Wi?

Hence it is proved that Wumpus is in the room [1, 3]

2 marks

FRR ICR] AC OH
--- page 18 ---
1. The humidity is high *PVQ
or the sky is cloudy.

2. If the sky is cloudy, * QR
then it will rain.

3. If the humidity is high, |, Ps
then it is hot.

4. Itis not hot.

e =§

* Goal: It will rain. (R)

*-PVQ *-PVQ
* QDR * -QVR
- POs * =PVS
Q:7
* =S - 35
b.

Negation of Goal ([=R): It will not rain.

4 marks. statements to FOL, 3 marks for converting to CNF, 3 marks for resolution graph

*PVQ PvQ a

* 5QVR PVR “PVS

* =PVS RVS =S

ie Bing, oe <<

* -R (Goal) (@) Null
After applying Proof by

It will rain proved sha geal: ine ay ia

solved, and it has terminated
with a Null clause

(@). Hence, the goal is
achieved.

FOI 7 QF Cr
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper ca452c19a6db

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AIML_7053/Intelligent Systems - I/ANS_Intelligent Systems - I(702AI0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: mixed (18 pages), mean OCR confidence 88.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Intelligent Systems - I
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q:1   Answer briefly:   [20]
Ans : Four Approaches to Building AI Systems
Artificial Intelligence systems can be categorized based on how they think and
act, either humanly or rationally. The four approaches are:
1. Systems that think like humans   [1 Mark]
•   These systems model the human mind.
• They are designed as machines with minds.
• They perform activities associated with human thinking such as decision
making, problem solving, and learning.
2. Systems that act like humans   [1 Mark]
•   These systems are built to show human behaviour.
• They aim to replicate how humans act in various situations.
3. Systems that think rationally   [1 Mark]
•   These systems are capable of drawing logical inferences while making   [05]
Q:1 a.   decisions.
• They focus on reasoning and logic to arrive at conclusions.
4. Systems that act rationally   [1 Mark]
•   These systems are designed to perform actions that are rational.
• They aim to achieve the best possible outcome based on available information.
[1 Mark]
********** 1 **********
--- page 2 ---
•   Utility-Based Agents:   [2.5]
o These agents are similar to the goal-based agent but provide an
extra component of utility measurement.
o   Utility-based agent act based not only goals but also the best way to
achieve the goal.
The utility function maps each state to a real number to check how efficiently each
action achieves the goals.
Q:1 b.   • Goal-Based Agents:   [2.5]   [05]
o They choose an action, so that they can achieve the goal.
o These agents may have to consider a long sequence of possible
actions before deciding whether the goal is achieved or not.
o   It focuses only on reaching the goal set and hence the decision took
by the agent is based on how far it is currently from their goal.
In a game-playing scenario, the most effective search strategy is typically the A* (A-
Star) Search Algorithm.
Why A* is Effective in Game-Playing
1. Optimal Path Finding   [1 Mark]
A* combines the strengths of Uniform Cost Search and Greedy Best-   [05]
Q:1 c.
First Search.It uses:
o g(n): the cost to reach the current node.
o h(n): the estimated cost to reach the goal from the current node.
o The total cost is f(n) = g(n) + h(n).
This ensures that the algorithm finds the shortest and most efficient path, which
is crucial in games where optimal moves matter.
********** 2 **********
--- page 3 ---
2. Heuristic Guidance   [1 Mark]
A* uses heuristics to guide the search, making it faster and more
intelligent. In games like chess or puzzle-solving, heuristics help prioritize
promising moves.
3. Completeness and Optimality   [1 Mark]
A* is both complete (it will find a solution if one exists) and optimal (it
finds the best solution), provided the heuristic is admissible (never
overestimates the cost).
4. Reduced Search Space   [1 Mark]
Compared to uninformed searches like BFS or DFS, A* explores fewer
nodes, making it more efficient in complex game environments.
Example Use Cases in Games   [1 Mark]
• Pathfinding in strategy games (e.g., moving units on a map).
• Solving puzzles like the 8-puzzle or Sudoku.
• AI decision-making in turn-based games.
Limitations
• High memory usage: A* stores all generated nodes, which can be a
problem in large game maps.
•   Heuristic design: The effectiveness depends on how well the heuristic is
crafted.
Q:1 d.   [05]
1 mark for each point
Q:2   Answer briefly:   [20]
Turing Test
Definition and Criteria   (2 Marks)
• Turing Test: A human communicates with a computer via a teletype.
•   If the human can’t tell whether they are talking to a computer or another human,
the computer passes the test.
Q:2 a.   • To pass the test, the machine must produce responses that are indistinguishable   [05]
from those of a human.
Required Capabilities :   (2 Mark)
To succeed in the Turing Test, a computer must possess:
•   Natural language processing – to communicate successfully in English
• Knowledge representation – to store what it knows or hears
********** 3 **********
--- page 4 ---
• Automated reasoning – to answer questions and draw conclusions
• Machine learning – to adapt and detect patterns
Implications for AI Systems :   (1 Mark)
• The Turing Test signifies that a machine can simulate human intelligence to a
degree that it becomes indistinguishable from human behavior in conversation.
•   It raises philosophical questions like:
o Can the computer think?
o Does the computer have a mind in exactly the same sense that humans
do?
Task environments in AI can be classified along several dimensions. Below are four key
classifications:
1. Observability   [ 2 Marks]
•   Fully Observable: The agent’s sensors provide access to the complete state of
the environment.
Example: A chess game where all pieces and positions are visible.
•   Partially Observable: Sensors provide incomplete or noisy data.
Example: An automated taxi cannot perceive other drivers' intentions.
•   Unobservable: The agent has no sensors to perceive the environment.
Example: A blind robot with no input devices.
2. Agents   [1 Marks]
•   Single-Agent: Only one agent operates in the environment.
Example: Solving a crossword puzzle.
Q:2 b.   •   Multi-Agent: Multiple agents interact, either competitively or cooperatively.   [05]
Example: Playing a football match or chess.
3. Determinism   [1 Mark]
•   Deterministic: The next state is completely determined by the current state and
the agent’s action.
Example: A board game like tic-tac-toe.
•   Stochastic: The next state is uncertain due to randomness or unknown factors.
Example: Taxi driving, where traffic behavior is unpredictable.
4. Dynamics   [1 Mark]
•   Static: The environment does not change while the agent is deliberating.
Example: Crossword puzzles.
• Dynamic: The environment changes continuously.
Example: Taxi driving, where other vehicles keep moving.
a. Compute Heuristics   [5 Marks]
Manhattan Distance Formula
ℎ𝑀𝑎𝑛ℎ𝑎𝑡𝑡𝑎𝑛= ∑∣𝑥𝑖−𝑥𝑖 ∗∣+∣𝑦𝑖−𝑦𝑖 ∗∣
Where:
•   (𝑥𝑖, 𝑦𝑖)= current position of tile 𝑖
•   (𝑥𝑖 ∗, 𝑦𝑖 ∗)= goal position of tile 𝑖
Q:2 c.   Calculation:   [10]
•   Tile 2: (0,0) → Goal (0,1) → Distance = 1
•   Tile 8: (0,1) → Goal (1,0) → Distance = 2
•   Tile 3: (0,2) → Goal (0,2) → Distance = 0
•   Tile 1: (1,0) → Goal (0,0) → Distance = 1
•   Tile 6: (1,1) → Goal (2,1) → Distance = 1
•   Tile 4: (1,2) → Goal (1,2) → Distance = 0
•   Tile 7: (2,0) → Goal (2,0) → Distance = 0
•   Tile 5: (2,2) → Goal (2,2) → Distance = 0
********** 4 **********
--- page 5 ---
Total Manhattan Distance:
ℎ𝑀𝑎𝑛ℎ𝑎𝑡𝑡𝑎𝑛= 1 + 2 + 0 + 1 + 1 + 0 + 0 + 0 = 5
Misplaced Tiles Formula
ℎ𝑀𝑖𝑠𝑝𝑙𝑎𝑐𝑒𝑑= Number of tiles not in their goal position
Tiles misplaced: 2, 8, 1, 6 → 4 tiles
ℎ𝑀𝑖𝑠𝑝𝑙𝑎𝑐𝑒𝑑= 4
b. A* Algorithm Solution   [5 Marks]
Formula:
𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
Where:
• 𝑔(𝑛)= depth of node (moves so far)
• ℎ(𝑛)= number of misplaced tiles
Step-by-Step Path
Step 0   Step 3
2 8 3   2 3
1 6 4   1 8 4
7 5   7 6 5
g(n)=0, h(n)=4, f(n)=4   g(n)=3, h(n)=2, f(n)=5
Step 1   Step 4
2 8 3   1 2 3
1 4   8 4
7 6 5   7 6 5
g(n)=1, h(n)=3, f(n)=4   g(n)=4, h(n)=1, f(n)=5
Step 2   Step 5 (Goal State)
2 3   1 2 3
1 8 4   8 4
7 6 5   7 6 5
g(n)=2, h(n)=3, f(n)=5   g(n)=5, h(n)=0, f(n)=5
Q:3   Answer briefly:   [20]
PEAS Framework   [2.5 Marks]
PEAS stands for:
• Performance Measure (P): Criteria to evaluate the success of an agent.
• Environment (E): The surroundings in which the agent operates.
•   Actuators (A): Components that perform actions to affect the environment.
•   Sensors (S): Components that perceive the environment and provide input to the
agent.
Q:3 a
Example: Automated Taxi Driver   [2.5 Marks]
• Performance Measure: Safe, fast, legal, comfortable trip; maximize profits.
• Environment: Roads, traffic, pedestrians, weather conditions.
•   Actuators: Steering wheel, accelerator, brake, signal indicators, horn.
•   Sensors: Cameras, GPS, speedometer, sonar, engine sensors.
Role of Heuristic Functions   [2 Marks]
• A heuristic function (h(n)) provides an estimate of the cost from the current
node to the goal state.
Q:3 b   •   It is used in informed search algorithms to guide the search process toward the
goal more efficiently.
•   Unlike uninformed search, which explores blindly, informed search uses
heuristics to prioritize nodes that appear closer to the goal.
********** 5 **********
--- page 6 ---
Why Heuristics Are Important   [1 Marks]
• Reduce Search Space: By selecting promising nodes, fewer states are explored.
• Improve Efficiency: Faster convergence to the goal compared to blind search.
• Enable Optimal Solutions: When heuristics are admissible (never
overestimate), algorithms like A* guarantee optimality.
Examples :   [2 Marks]
1. Greedy Best-First Search
o Uses heuristic function h(n) to choose the node that appears closest to
the goal.
o Example: In a map navigation problem, h(n) could be the straight-line
distance to the destination.
2. A Search Algorithm*
o Combines path cost and heuristic:
𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
Where:
▪ 𝑔(𝑛)= cost from start to current node
▪ ℎ(𝑛)= estimated cost to goal
o Example: In an 8-puzzle problem, h(n) can be:
▪ Misplaced Tiles: Number of tiles not in place.
▪ Manhattan Distance: Sum of distances of tiles from their goal
positions.
Backtracking algorithms can be made more efficient using the following
techniques:
Most Constrained Variable (MCV) Heuristic: Also known as the Minimum
Remaining Values (MRV) heuristic. Choose the variable with the fewest legal
(available) values first. This reduces branching and makes failure detection faster.
Q:3 c.   Least Constraining Value (LCV) Heuristic: When selecting a value for a variable,   [10]
choose the one that leaves the most options open for remaining variables.
……………3 marks
By applying backtracking with the MCV heuristic, we efficiently select the next
variable (row) with the fewest valid moves, reducing the number of trials.
……………1 marks
********** 6 **********
--- page 7 ---
…………..6 marks for final solution showing all steps and domain
Q:4   Answer briefly:   [20]
Crypt arithmetic problems are mathematical puzzles in which the digits
are replaced by letters of the alphabets. Crypt arithmetic Problem is a
type of constraint satisfaction problem where the game is about digits
and its unique replacement either with alphabets or other symbols. In
Q:4 a. crypt arithmetic problem, the digits 0 9 get substituted by some possible   [10]
alphabets or symbols. The task in crypt arithmetic problem is to
substitute each digit with an alphabet to get the result arithmetically
correct.   …………… 2 marks
The rules or constraints on a crypt arithmetic problem are as follows:
********** 7 **********
--- page 8 ---
• There should be a unique digit to be replaced with a unique
alphabet
• The result should satisfy the predefined arithmetic rules i e 2 2 4
• Digits should be from 0 9 only
• There should be only one carry forward, while performing the
addition
• operation on a problem
• The problem can be solved from both sides, i e left hand side (L
H S), or right hand side (R H S)
…………… 2 marks
Step 1   ………….. 1 mark
• Clearly, P = 1, U = 9, E = 0
• Let’s replace the values here
U S A
+ U S S R
-----------
P E A C E
Step 2………….. 2 mark
• A + R = 0
• This is possible if, A = 5, R = 5, but, both can’t take same values
• So its possible with (8,2), (7,3), (6,4), (4,6), (3,7), (2,8)
• Let’s do hit and trial and take (2,8) and replace the new values.
0 S A
+ 9 S S R
-----------
1 0 A C 0
Step 3   ………….. 2 mark
• Now, assuming S value to be 3
• We have S + S + 1 (carry) = C
• 3 + 3 + 1 => C = 7 (unoccupied)
• All the values are found out we just need to verify
1
0 S 2
+ 9 S S 8
-----------
1 0 2 C 0
Step 3………….. 1 mark
• Values, are replaced and all the operations work just fine
********** 8 **********
--- page 9 ---
Value of P + E + A + C + E = 1 + 0 + 2 + 7 + 0 = 10
1
0 3 2
+ 9 3 3 8
-----------
1 0 2 7 0
Q:4 b.   [10]
• 5 mark → Correctly finding alpha beta values at each level .
• 1 mark → Correctly calculating the value at the root node.
• 2 mark → Correctly identifying pruned nodes.
• 2 mark → Clear step-by-step presentation.
Q5   Answer briefly:   [20]
********** 9 **********
--- page 10 ---
A
B
C
D   F   G
E
…………….. 1 marks
Step 1:
Q:5 a. Take A as the initial state of the tree.
The Maximizer starts with a worst-case value of –∞, and the Minimizer starts
with +∞.
Step 2:
The Maximizer compares all terminal node values with its initial value (–∞) and
chooses the maximum value for each branch.
For node D max(10, -∞) => max(10,6)= 10
For Node E max(100, -∞) => max(100, 8)= 100
For Node F max (1, -∞) => max(1, 2)= 2
For Node G max (20, -∞) => max(20, 4)= 20
…………….. 2 marks
Step 3: In the next step, it's a turn for the minimizer so it will compare all nodes
value with and will find the 3 rd layer node values
For node B : min(10,100) = 10
For node C= min ( 2, 20) = 2
…………….. 1 marks
Step 4: Now it's a turn for Maximizer, and it will again choose the maximum of
all nodes value and find the maximum value for the root node I.
Final root node value is max(2, 10) = 10
…………..1 mark
Variables:   ……. 1 mark
Q:5 b. Each event is a variable that needs a teacher assigned.
********** 10 **********
--- page 11 ---
• V = {100m Race, Long Jump, Shot Put, Relay}
Domains:   ……………….. 2 marks
Possible teachers available for each event:
• 100m Race → {A}
• Long Jump → {B}
• Shot Put → {B, C}
• Relay → {A, C}
Constraints:   …………. 2 marks
1. No teacher can supervise two events at the same time.
→ All assigned teachers must be different.
2. Teachers can only supervise events they are available for (as given in
domains).
(a) Concept of Knowledge Representation (2 Marks)
Knowledge Representation (KR) in Artificial Intelligence refers to the method of
storing and organizing knowledge in such a way that machines can
understand, reason, and make decisions like humans.
Humans use their knowledge to interpret situations and act accordingly.
Similarly, KR provides AI systems with a structured way to represent real-
world information so they can perform reasoning, problem-solving, and
learning.
In short, KR answers the question — “How can we make machines think and
reason using knowledge like humans?”
(b) Four Key Properties of Knowledge Representation (4 Marks)
1. Representation Adequacy (1 Mark)
Q:5 c.   o   It is the ability of a system to represent all types of knowledge
needed in a specific domain.
o Example: A medical diagnosis system must represent symptoms,
diseases, and their relationships.
2. Inferential Adequacy (1 Mark)
o   It is the ability to derive new knowledge from existing knowledge
using reasoning or inference.
o Example: If “All humans are mortal” and “Socrates is a human,”
then the system can infer “Socrates is mortal.”
3. Inferential Efficiency (1 Mark)
o   It refers to the ability of the knowledge system to derive
conclusions quickly and efficiently by focusing on the most
relevant information.
o Example: Using heuristics or shortcuts to reach conclusions faster
in expert systems.
4. Acquisition Efficiency (1 Mark)
o   It is the ability to easily acquire and update new knowledge in
the knowledge base.
********** 11 **********
--- page 12 ---
o Example: Adding new medical conditions to a diagnostic
knowledge base without redesigning the entire system.
3. Propositional Logic (2 Marks)
Propositional Logic represents knowledge as true or false statements using
symbols (P, Q, R) and logical connectives (∧, ∨, ¬, →, ↔).
It is also known as Boolean logic, as it operates on values 0 (false) and 1 (true).
4. Examples (2 Marks)
• Atomic Propositions:
P: 2 + 2 = 4 (True)
Q: The Sun is cold (False)
• Compound Propositions:
“It is raining and the ground is wet” → R ∧ S
“If it rains, then the ground is wet” → R → S
Q – 6
AO* Algorithm (AND-OR Graph Search)   [5 Marks]
The AO* algorithm is used for problems that can be decomposed into sub-problems
represented by AND-OR graphs. It finds the most cost-effective solution by considering
both AND (all sub-tasks must be solved) and OR (choose one alternative) relationships.
Working Formula
𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
Where:
•   g(n): Actual cost from the start node to the current node.
•   h(n): Estimated cost from the current node to the goal.
Q:6 a.   •   f(n): Total estimated cost from start to goal.
Steps of AO* Algorithm
1. Start at the root node and calculate:
𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
2. Expand the most promising node based on minimum cost.
3. For AND nodes, sum the costs of all connected sub-nodes.
4. For OR nodes, choose the branch with the minimum cost.
5. Update heuristic values of parent nodes whenever child nodes are expanded.
6. Repeat until the goal node is reached and all AND conditions are satisfied.
2nd part   [5 Marks]
********** 12 **********
--- page 13 ---
Step 1: Initial Evaluation Using f(n) = g(n) + h(n)
Starting from node A, we use the evaluation function:
f(A -> B) = g(B) + h(B)
=1+5 (g(n) = 1 is the default path cost)
=6
For the path involving AND nodes (C and D):
F(A -> C + D) = g(C) + h(C) + g(D) + h(D)
=1+2+1+4 (C&D are AND nodes)

=8

Since f(A -> B) = 6 is smaller than f(A -> C + D) = 8, we select the path A ->
B.

Start

7 9 3 0 0 0

AO* Algorithm (Step-1)

Step 2: Explore Node B
Next, we explore node B, and calculate the values for nodes E and F:

f(B -> E) = g(E) + h(E)
=1+7
=

£(B -> F) = g(F) + h(F)
=1+9
= 10

So, by above calculation B-»E path is chosen which is minimum path, i.e f(B->E)
because B's heuristic value is different from its actual value The heuristic is
updated and the minimum cost path is selected. The minimum value in our
situation is 8. Therefore, the heuristic for A must be updated due to the change

in B's heuristic.

FIR ICR 7] QI HO
--- page 14 ---
So we need to calculate it again.

Thus, f(B -> E) = 8 is chosen as the optimal path. Since B’s heuristic value

differs from its actual cost, we update the heuristic for A.

f(A -> B) = g(B) + updated h(B)
=1+8
=9

Start

AO* Algorithm (Step-2)

Step 3: Compare and Explore Paths

Now, we compare f(A -> B) = 9 with f(A -> C + D) = 8. Since f(A -> C+]

smaller, we explore this path and move to node C.

For node C:

#(C -> G) = g(G) + h(G)
=1+3
=4

#(C -> H + I) = g(H) + h(H) + g(I) + h(I)
=1+0+1+0 (H&TI are AND nodes)
=2

f(C-»H+l) is selected as the path with the lowest cost and the heuristic is
also left unchanged because it matches the actual cost. Paths H & | are sd
because the heuristic for those paths is 0, but Path A-»D needs to be calc
because it has an AND.

FRR IC 7 I OH
--- page 15 ---
(a) Translation into Predicate Logic (3 Marks)
Let us define the predicates:
•   Smiling(x): x is smiling
• Graduating(x): x is graduating
• Happy(x): x is happy
Q6 b.   1. Someone is smiling:
∃x (Smiling(x))   [10]
2. Someone is graduating:
∃x (Graduating(x) )
3. Everyone is happy:
∀x (Happy(x))
(b) Conversion into Conjunctive Normal Form (CNF) (7 Marks)
Step 1: Eliminate implications   ………… 1 mark
• No implications in the given sentences, so we move to next step.
********** 15 **********
--- page 16 ---
Step 2: Move quantifiers to the front ………… 2 mark
Already in standard form:
∃x Smiling(x),
∃x Graduating(x),
∀x Happy(x)
Step 3: Standardize variables ………… 2 mark
Rename variables to avoid confusion:
•   Smiling(a),
•   Graduating(b),
• ∀x Happy(x)
Step 4: Skolemization (eliminate existential quantifiers) ………… 1 mark
• There are only universal quantifiers, so no Skolemization needed.
• Drop universal quantifier (implicit universal scope remains).
Final CNF clause(s): { Happy(x) } (this is read as a universally
quantified clause Happy(x))
Final CNF (clauses) — summary ………… 1 mark
1. Smiling(a) — clause: { Smiling(a) }
2. Graduating(b) — clause: { Graduating(b) }
3. Happy(x) — clause: { Happy(x) } (implicitly ∀x)
Wumpus World is a grid-based environment used in Artificial Intelligence to
demonstrate knowledge-based agents and logical reasoning. It helps in
understanding how an intelligent agent perceives, reasons, and acts in an
uncertain environment.
…………… 1 mark
Layout:   …………… 2 mark
• The world is represented as a 4 × 4 grid of rooms (cells).
• Each cell can contain:
Q7   o Wumpus – a monster that kills the agent if it enters that cell.   [10]
a.   o Pit – a bottomless hole that causes death if entered.
o Gold – treasure that the agent must find and grab.
o Empty rooms – safe cells.
Percepts (Sensory Inputs): …………… 2 mark
• Stench: Smell perceived in rooms adjacent to the Wumpus.
• Breeze: Felt in rooms adjacent to a pit.
•   Glitter: Seen in the room with gold.
• Bump: Felt when the agent hits a wall.
• Scream: Heard when the Wumpus is killed.
********** 16 **********
--- page 17 ---
Agents and Actions: …………… 1 mark
• The agent can move forward, turn left/right, grab, shoot an arrow, or
climb out of the cave.
• The agent uses logical reasoning to identify safe paths and locate gold
while avoiding the Wumpus and pits.
Purpose of the Game: …………… 1 mark
• The main goal is to collect the gold and exit safely without falling into a
pit or being killed by the Wumpus, demonstrating intelligent decision-
making using logic.
…………… 3 mark
Q:7
b.
********** 17 **********
--- page 18 ---
* Sunny A Warm > enjoy
Eliminate implication:
-(Sunny A warm) V enjoy
Moving negation inside

Sunny V -warm V enjoy

* raining > wet
Eliminate implication:
-raining V wet

* warm

* raining

* Sunny

* Negate the statement to be proved: -enjoy

* Now take the statements one by one and create resolution
graph.
enjoy ~Sunny V -warm V enjoy

=Sunny V -warm warm

Sunny Sunny After applying Proof by

Refutation (Contradiction) on
i the goal, the problem is
solved, and it has terminated
Empty clause with a Null clause

(Contradiction) (@). Hence, the goal is
achieved.

Hence you will enjoy proved

4 marks ... statements to FOL
3 marks for converting to CNF

3 marks for resolution graph

FR ICR 7] QA HH
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 4cea82e44249

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_AI_7051/Intelligent Systems - I/ANS_Intelligent Systems - I(702AI0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: mixed (18 pages), mean OCR confidence 88.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Intelligent Systems - I
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q:1   Answer briefly:   [20]
Ans : Four Approaches to Building AI Systems
Artificial Intelligence systems can be categorized based on how they think and
act, either humanly or rationally. The four approaches are:
1. Systems that think like humans   [1 Mark]
•   These systems model the human mind.
• They are designed as machines with minds.
• They perform activities associated with human thinking such as decision
making, problem solving, and learning.
2. Systems that act like humans   [1 Mark]
•   These systems are built to show human behaviour.
• They aim to replicate how humans act in various situations.
3. Systems that think rationally   [1 Mark]
•   These systems are capable of drawing logical inferences while making   [05]
Q:1 a.   decisions.
• They focus on reasoning and logic to arrive at conclusions.
4. Systems that act rationally   [1 Mark]
•   These systems are designed to perform actions that are rational.
• They aim to achieve the best possible outcome based on available information.
[1 Mark]
********** 1 **********
--- page 2 ---
•   Utility-Based Agents:   [2.5]
o These agents are similar to the goal-based agent but provide an
extra component of utility measurement.
o   Utility-based agent act based not only goals but also the best way to
achieve the goal.
The utility function maps each state to a real number to check how efficiently each
action achieves the goals.
Q:1 b.   • Goal-Based Agents:   [2.5]   [05]
o They choose an action, so that they can achieve the goal.
o These agents may have to consider a long sequence of possible
actions before deciding whether the goal is achieved or not.
o   It focuses only on reaching the goal set and hence the decision took
by the agent is based on how far it is currently from their goal.
In a game-playing scenario, the most effective search strategy is typically the A* (A-
Star) Search Algorithm.
Why A* is Effective in Game-Playing
1. Optimal Path Finding   [1 Mark]
A* combines the strengths of Uniform Cost Search and Greedy Best-   [05]
Q:1 c.
First Search.It uses:
o g(n): the cost to reach the current node.
o h(n): the estimated cost to reach the goal from the current node.
o The total cost is f(n) = g(n) + h(n).
This ensures that the algorithm finds the shortest and most efficient path, which
is crucial in games where optimal moves matter.
********** 2 **********
--- page 3 ---
2. Heuristic Guidance   [1 Mark]
A* uses heuristics to guide the search, making it faster and more
intelligent. In games like chess or puzzle-solving, heuristics help prioritize
promising moves.
3. Completeness and Optimality   [1 Mark]
A* is both complete (it will find a solution if one exists) and optimal (it
finds the best solution), provided the heuristic is admissible (never
overestimates the cost).
4. Reduced Search Space   [1 Mark]
Compared to uninformed searches like BFS or DFS, A* explores fewer
nodes, making it more efficient in complex game environments.
Example Use Cases in Games   [1 Mark]
• Pathfinding in strategy games (e.g., moving units on a map).
• Solving puzzles like the 8-puzzle or Sudoku.
• AI decision-making in turn-based games.
Limitations
• High memory usage: A* stores all generated nodes, which can be a
problem in large game maps.
•   Heuristic design: The effectiveness depends on how well the heuristic is
crafted.
Q:1 d.   [05]
1 mark for each point
Q:2   Answer briefly:   [20]
Turing Test
Definition and Criteria   (2 Marks)
• Turing Test: A human communicates with a computer via a teletype.
•   If the human can’t tell whether they are talking to a computer or another human,
the computer passes the test.
Q:2 a.   • To pass the test, the machine must produce responses that are indistinguishable   [05]
from those of a human.
Required Capabilities :   (2 Mark)
To succeed in the Turing Test, a computer must possess:
•   Natural language processing – to communicate successfully in English
• Knowledge representation – to store what it knows or hears
********** 3 **********
--- page 4 ---
• Automated reasoning – to answer questions and draw conclusions
• Machine learning – to adapt and detect patterns
Implications for AI Systems :   (1 Mark)
• The Turing Test signifies that a machine can simulate human intelligence to a
degree that it becomes indistinguishable from human behavior in conversation.
•   It raises philosophical questions like:
o Can the computer think?
o Does the computer have a mind in exactly the same sense that humans
do?
Task environments in AI can be classified along several dimensions. Below are four key
classifications:
1. Observability   [ 2 Marks]
•   Fully Observable: The agent’s sensors provide access to the complete state of
the environment.
Example: A chess game where all pieces and positions are visible.
•   Partially Observable: Sensors provide incomplete or noisy data.
Example: An automated taxi cannot perceive other drivers' intentions.
•   Unobservable: The agent has no sensors to perceive the environment.
Example: A blind robot with no input devices.
2. Agents   [1 Marks]
•   Single-Agent: Only one agent operates in the environment.
Example: Solving a crossword puzzle.
Q:2 b.   •   Multi-Agent: Multiple agents interact, either competitively or cooperatively.   [05]
Example: Playing a football match or chess.
3. Determinism   [1 Mark]
•   Deterministic: The next state is completely determined by the current state and
the agent’s action.
Example: A board game like tic-tac-toe.
•   Stochastic: The next state is uncertain due to randomness or unknown factors.
Example: Taxi driving, where traffic behavior is unpredictable.
4. Dynamics   [1 Mark]
•   Static: The environment does not change while the agent is deliberating.
Example: Crossword puzzles.
• Dynamic: The environment changes continuously.
Example: Taxi driving, where other vehicles keep moving.
a. Compute Heuristics   [5 Marks]
Manhattan Distance Formula
ℎ𝑀𝑎𝑛ℎ𝑎𝑡𝑡𝑎𝑛= ∑∣𝑥𝑖−𝑥𝑖 ∗∣+∣𝑦𝑖−𝑦𝑖 ∗∣
Where:
•   (𝑥𝑖, 𝑦𝑖)= current position of tile 𝑖
•   (𝑥𝑖 ∗, 𝑦𝑖 ∗)= goal position of tile 𝑖
Q:2 c.   Calculation:   [10]
•   Tile 2: (0,0) → Goal (0,1) → Distance = 1
•   Tile 8: (0,1) → Goal (1,0) → Distance = 2
•   Tile 3: (0,2) → Goal (0,2) → Distance = 0
•   Tile 1: (1,0) → Goal (0,0) → Distance = 1
•   Tile 6: (1,1) → Goal (2,1) → Distance = 1
•   Tile 4: (1,2) → Goal (1,2) → Distance = 0
•   Tile 7: (2,0) → Goal (2,0) → Distance = 0
•   Tile 5: (2,2) → Goal (2,2) → Distance = 0
********** 4 **********
--- page 5 ---
Total Manhattan Distance:
ℎ𝑀𝑎𝑛ℎ𝑎𝑡𝑡𝑎𝑛= 1 + 2 + 0 + 1 + 1 + 0 + 0 + 0 = 5
Misplaced Tiles Formula
ℎ𝑀𝑖𝑠𝑝𝑙𝑎𝑐𝑒𝑑= Number of tiles not in their goal position
Tiles misplaced: 2, 8, 1, 6 → 4 tiles
ℎ𝑀𝑖𝑠𝑝𝑙𝑎𝑐𝑒𝑑= 4
b. A* Algorithm Solution   [5 Marks]
Formula:
𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
Where:
• 𝑔(𝑛)= depth of node (moves so far)
• ℎ(𝑛)= number of misplaced tiles
Step-by-Step Path
Step 0   Step 3
2 8 3   2 3
1 6 4   1 8 4
7 5   7 6 5
g(n)=0, h(n)=4, f(n)=4   g(n)=3, h(n)=2, f(n)=5
Step 1   Step 4
2 8 3   1 2 3
1 4   8 4
7 6 5   7 6 5
g(n)=1, h(n)=3, f(n)=4   g(n)=4, h(n)=1, f(n)=5
Step 2   Step 5 (Goal State)
2 3   1 2 3
1 8 4   8 4
7 6 5   7 6 5
g(n)=2, h(n)=3, f(n)=5   g(n)=5, h(n)=0, f(n)=5
Q:3   Answer briefly:   [20]
PEAS Framework   [2.5 Marks]
PEAS stands for:
• Performance Measure (P): Criteria to evaluate the success of an agent.
• Environment (E): The surroundings in which the agent operates.
•   Actuators (A): Components that perform actions to affect the environment.
•   Sensors (S): Components that perceive the environment and provide input to the
agent.
Q:3 a
Example: Automated Taxi Driver   [2.5 Marks]
• Performance Measure: Safe, fast, legal, comfortable trip; maximize profits.
• Environment: Roads, traffic, pedestrians, weather conditions.
•   Actuators: Steering wheel, accelerator, brake, signal indicators, horn.
•   Sensors: Cameras, GPS, speedometer, sonar, engine sensors.
Role of Heuristic Functions   [2 Marks]
• A heuristic function (h(n)) provides an estimate of the cost from the current
node to the goal state.
Q:3 b   •   It is used in informed search algorithms to guide the search process toward the
goal more efficiently.
•   Unlike uninformed search, which explores blindly, informed search uses
heuristics to prioritize nodes that appear closer to the goal.
********** 5 **********
--- page 6 ---
Why Heuristics Are Important   [1 Marks]
• Reduce Search Space: By selecting promising nodes, fewer states are explored.
• Improve Efficiency: Faster convergence to the goal compared to blind search.
• Enable Optimal Solutions: When heuristics are admissible (never
overestimate), algorithms like A* guarantee optimality.
Examples :   [2 Marks]
1. Greedy Best-First Search
o Uses heuristic function h(n) to choose the node that appears closest to
the goal.
o Example: In a map navigation problem, h(n) could be the straight-line
distance to the destination.
2. A Search Algorithm*
o Combines path cost and heuristic:
𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
Where:
▪ 𝑔(𝑛)= cost from start to current node
▪ ℎ(𝑛)= estimated cost to goal
o Example: In an 8-puzzle problem, h(n) can be:
▪ Misplaced Tiles: Number of tiles not in place.
▪ Manhattan Distance: Sum of distances of tiles from their goal
positions.
Backtracking algorithms can be made more efficient using the following
techniques:
Most Constrained Variable (MCV) Heuristic: Also known as the Minimum
Remaining Values (MRV) heuristic. Choose the variable with the fewest legal
(available) values first. This reduces branching and makes failure detection faster.
Q:3 c.   Least Constraining Value (LCV) Heuristic: When selecting a value for a variable,   [10]
choose the one that leaves the most options open for remaining variables.
……………3 marks
By applying backtracking with the MCV heuristic, we efficiently select the next
variable (row) with the fewest valid moves, reducing the number of trials.
……………1 marks
********** 6 **********
--- page 7 ---
…………..6 marks for final solution showing all steps and domain
Q:4   Answer briefly:   [20]
Crypt arithmetic problems are mathematical puzzles in which the digits
are replaced by letters of the alphabets. Crypt arithmetic Problem is a
type of constraint satisfaction problem where the game is about digits
and its unique replacement either with alphabets or other symbols. In
Q:4 a. crypt arithmetic problem, the digits 0 9 get substituted by some possible   [10]
alphabets or symbols. The task in crypt arithmetic problem is to
substitute each digit with an alphabet to get the result arithmetically
correct.   …………… 2 marks
The rules or constraints on a crypt arithmetic problem are as follows:
********** 7 **********
--- page 8 ---
• There should be a unique digit to be replaced with a unique
alphabet
• The result should satisfy the predefined arithmetic rules i e 2 2 4
• Digits should be from 0 9 only
• There should be only one carry forward, while performing the
addition
• operation on a problem
• The problem can be solved from both sides, i e left hand side (L
H S), or right hand side (R H S)
…………… 2 marks
Step 1   ………….. 1 mark
• Clearly, P = 1, U = 9, E = 0
• Let’s replace the values here
U S A
+ U S S R
-----------
P E A C E
Step 2………….. 2 mark
• A + R = 0
• This is possible if, A = 5, R = 5, but, both can’t take same values
• So its possible with (8,2), (7,3), (6,4), (4,6), (3,7), (2,8)
• Let’s do hit and trial and take (2,8) and replace the new values.
0 S A
+ 9 S S R
-----------
1 0 A C 0
Step 3   ………….. 2 mark
• Now, assuming S value to be 3
• We have S + S + 1 (carry) = C
• 3 + 3 + 1 => C = 7 (unoccupied)
• All the values are found out we just need to verify
1
0 S 2
+ 9 S S 8
-----------
1 0 2 C 0
Step 3………….. 1 mark
• Values, are replaced and all the operations work just fine
********** 8 **********
--- page 9 ---
Value of P + E + A + C + E = 1 + 0 + 2 + 7 + 0 = 10
1
0 3 2
+ 9 3 3 8
-----------
1 0 2 7 0
Q:4 b.   [10]
• 5 mark → Correctly finding alpha beta values at each level .
• 1 mark → Correctly calculating the value at the root node.
• 2 mark → Correctly identifying pruned nodes.
• 2 mark → Clear step-by-step presentation.
Q5   Answer briefly:   [20]
********** 9 **********
--- page 10 ---
A
B
C
D   F   G
E
…………….. 1 marks
Step 1:
Q:5 a. Take A as the initial state of the tree.
The Maximizer starts with a worst-case value of –∞, and the Minimizer starts
with +∞.
Step 2:
The Maximizer compares all terminal node values with its initial value (–∞) and
chooses the maximum value for each branch.
For node D max(10, -∞) => max(10,6)= 10
For Node E max(100, -∞) => max(100, 8)= 100
For Node F max (1, -∞) => max(1, 2)= 2
For Node G max (20, -∞) => max(20, 4)= 20
…………….. 2 marks
Step 3: In the next step, it's a turn for the minimizer so it will compare all nodes
value with and will find the 3 rd layer node values
For node B : min(10,100) = 10
For node C= min ( 2, 20) = 2
…………….. 1 marks
Step 4: Now it's a turn for Maximizer, and it will again choose the maximum of
all nodes value and find the maximum value for the root node I.
Final root node value is max(2, 10) = 10
…………..1 mark
Variables:   ……. 1 mark
Q:5 b. Each event is a variable that needs a teacher assigned.
********** 10 **********
--- page 11 ---
• V = {100m Race, Long Jump, Shot Put, Relay}
Domains:   ……………….. 2 marks
Possible teachers available for each event:
• 100m Race → {A}
• Long Jump → {B}
• Shot Put → {B, C}
• Relay → {A, C}
Constraints:   …………. 2 marks
1. No teacher can supervise two events at the same time.
→ All assigned teachers must be different.
2. Teachers can only supervise events they are available for (as given in
domains).
(a) Concept of Knowledge Representation (2 Marks)
Knowledge Representation (KR) in Artificial Intelligence refers to the method of
storing and organizing knowledge in such a way that machines can
understand, reason, and make decisions like humans.
Humans use their knowledge to interpret situations and act accordingly.
Similarly, KR provides AI systems with a structured way to represent real-
world information so they can perform reasoning, problem-solving, and
learning.
In short, KR answers the question — “How can we make machines think and
reason using knowledge like humans?”
(b) Four Key Properties of Knowledge Representation (4 Marks)
1. Representation Adequacy (1 Mark)
Q:5 c.   o   It is the ability of a system to represent all types of knowledge
needed in a specific domain.
o Example: A medical diagnosis system must represent symptoms,
diseases, and their relationships.
2. Inferential Adequacy (1 Mark)
o   It is the ability to derive new knowledge from existing knowledge
using reasoning or inference.
o Example: If “All humans are mortal” and “Socrates is a human,”
then the system can infer “Socrates is mortal.”
3. Inferential Efficiency (1 Mark)
o   It refers to the ability of the knowledge system to derive
conclusions quickly and efficiently by focusing on the most
relevant information.
o Example: Using heuristics or shortcuts to reach conclusions faster
in expert systems.
4. Acquisition Efficiency (1 Mark)
o   It is the ability to easily acquire and update new knowledge in
the knowledge base.
********** 11 **********
--- page 12 ---
o Example: Adding new medical conditions to a diagnostic
knowledge base without redesigning the entire system.
3. Propositional Logic (2 Marks)
Propositional Logic represents knowledge as true or false statements using
symbols (P, Q, R) and logical connectives (∧, ∨, ¬, →, ↔).
It is also known as Boolean logic, as it operates on values 0 (false) and 1 (true).
4. Examples (2 Marks)
• Atomic Propositions:
P: 2 + 2 = 4 (True)
Q: The Sun is cold (False)
• Compound Propositions:
“It is raining and the ground is wet” → R ∧ S
“If it rains, then the ground is wet” → R → S
Q – 6
AO* Algorithm (AND-OR Graph Search)   [5 Marks]
The AO* algorithm is used for problems that can be decomposed into sub-problems
represented by AND-OR graphs. It finds the most cost-effective solution by considering
both AND (all sub-tasks must be solved) and OR (choose one alternative) relationships.
Working Formula
𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
Where:
•   g(n): Actual cost from the start node to the current node.
•   h(n): Estimated cost from the current node to the goal.
Q:6 a.   •   f(n): Total estimated cost from start to goal.
Steps of AO* Algorithm
1. Start at the root node and calculate:
𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
2. Expand the most promising node based on minimum cost.
3. For AND nodes, sum the costs of all connected sub-nodes.
4. For OR nodes, choose the branch with the minimum cost.
5. Update heuristic values of parent nodes whenever child nodes are expanded.
6. Repeat until the goal node is reached and all AND conditions are satisfied.
2nd part   [5 Marks]
********** 12 **********
--- page 13 ---
Step 1: Initial Evaluation Using f(n) = g(n) + h(n)
Starting from node A, we use the evaluation function:
f(A -> B) = g(B) + h(B)
=1+5 (g(n) = 1 is the default path cost)
=6
For the path involving AND nodes (C and D):
F(A -> C + D) = g(C) + h(C) + g(D) + h(D)
=1+2+1+4 (C&D are AND nodes)

=8

Since f(A -> B) = 6 is smaller than f(A -> C + D) = 8, we select the path A ->
B.

Start

7 9 3 0 0 0

AO* Algorithm (Step-1)

Step 2: Explore Node B
Next, we explore node B, and calculate the values for nodes E and F:

f(B -> E) = g(E) + h(E)
=1+7
=

£(B -> F) = g(F) + h(F)
=1+9
= 10

So, by above calculation B-»E path is chosen which is minimum path, i.e f(B->E)
because B's heuristic value is different from its actual value The heuristic is
updated and the minimum cost path is selected. The minimum value in our
situation is 8. Therefore, the heuristic for A must be updated due to the change

in B's heuristic.

FIR ICR 7] QI HO
--- page 14 ---
So we need to calculate it again.

Thus, f(B -> E) = 8 is chosen as the optimal path. Since B’s heuristic value

differs from its actual cost, we update the heuristic for A.

f(A -> B) = g(B) + updated h(B)
=1+8
=9

Start

AO* Algorithm (Step-2)

Step 3: Compare and Explore Paths

Now, we compare f(A -> B) = 9 with f(A -> C + D) = 8. Since f(A -> C+]

smaller, we explore this path and move to node C.

For node C:

#(C -> G) = g(G) + h(G)
=1+3
=4

#(C -> H + I) = g(H) + h(H) + g(I) + h(I)
=1+0+1+0 (H&TI are AND nodes)
=2

f(C-»H+l) is selected as the path with the lowest cost and the heuristic is
also left unchanged because it matches the actual cost. Paths H & | are sd
because the heuristic for those paths is 0, but Path A-»D needs to be calc
because it has an AND.

FRR IC 7 I OH
--- page 15 ---
(a) Translation into Predicate Logic (3 Marks)
Let us define the predicates:
•   Smiling(x): x is smiling
• Graduating(x): x is graduating
• Happy(x): x is happy
Q6 b.   1. Someone is smiling:
∃x (Smiling(x))   [10]
2. Someone is graduating:
∃x (Graduating(x) )
3. Everyone is happy:
∀x (Happy(x))
(b) Conversion into Conjunctive Normal Form (CNF) (7 Marks)
Step 1: Eliminate implications   ………… 1 mark
• No implications in the given sentences, so we move to next step.
********** 15 **********
--- page 16 ---
Step 2: Move quantifiers to the front ………… 2 mark
Already in standard form:
∃x Smiling(x),
∃x Graduating(x),
∀x Happy(x)
Step 3: Standardize variables ………… 2 mark
Rename variables to avoid confusion:
•   Smiling(a),
•   Graduating(b),
• ∀x Happy(x)
Step 4: Skolemization (eliminate existential quantifiers) ………… 1 mark
• There are only universal quantifiers, so no Skolemization needed.
• Drop universal quantifier (implicit universal scope remains).
Final CNF clause(s): { Happy(x) } (this is read as a universally
quantified clause Happy(x))
Final CNF (clauses) — summary ………… 1 mark
1. Smiling(a) — clause: { Smiling(a) }
2. Graduating(b) — clause: { Graduating(b) }
3. Happy(x) — clause: { Happy(x) } (implicitly ∀x)
Wumpus World is a grid-based environment used in Artificial Intelligence to
demonstrate knowledge-based agents and logical reasoning. It helps in
understanding how an intelligent agent perceives, reasons, and acts in an
uncertain environment.
…………… 1 mark
Layout:   …………… 2 mark
• The world is represented as a 4 × 4 grid of rooms (cells).
• Each cell can contain:
Q7   o Wumpus – a monster that kills the agent if it enters that cell.   [10]
a.   o Pit – a bottomless hole that causes death if entered.
o Gold – treasure that the agent must find and grab.
o Empty rooms – safe cells.
Percepts (Sensory Inputs): …………… 2 mark
• Stench: Smell perceived in rooms adjacent to the Wumpus.
• Breeze: Felt in rooms adjacent to a pit.
•   Glitter: Seen in the room with gold.
• Bump: Felt when the agent hits a wall.
• Scream: Heard when the Wumpus is killed.
********** 16 **********
--- page 17 ---
Agents and Actions: …………… 1 mark
• The agent can move forward, turn left/right, grab, shoot an arrow, or
climb out of the cave.
• The agent uses logical reasoning to identify safe paths and locate gold
while avoiding the Wumpus and pits.
Purpose of the Game: …………… 1 mark
• The main goal is to collect the gold and exit safely without falling into a
pit or being killed by the Wumpus, demonstrating intelligent decision-
making using logic.
…………… 3 mark
Q:7
b.
********** 17 **********
--- page 18 ---
* Sunny A Warm > enjoy
Eliminate implication:
-(Sunny A warm) V enjoy
Moving negation inside

Sunny V -warm V enjoy

* raining > wet
Eliminate implication:
-raining V wet

* warm

* raining

* Sunny

* Negate the statement to be proved: -enjoy

* Now take the statements one by one and create resolution
graph.
enjoy ~Sunny V -warm V enjoy

=Sunny V -warm warm

Sunny Sunny After applying Proof by

Refutation (Contradiction) on
i the goal, the problem is
solved, and it has terminated
Empty clause with a Null clause

(Contradiction) (@). Hence, the goal is
achieved.

Hence you will enjoy proved

4 marks ... statements to FOL
3 marks for converting to CNF

3 marks for resolution graph

FR ICR 7] QA HH
````
