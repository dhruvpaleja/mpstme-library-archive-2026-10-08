# Intelligent Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper e511db77bc15

- Departments: Artificial Intelligence
- Programmes: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE) - 7012
- Source: `00_Original_Downloads/2025/Semester II/76514__Final-Exam.zip :: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE) - 7012/INTELLIGENT SYSTEMS/ANS_Final-Exam_INTELLIGENT SYSTEMS(702AI0C034)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (15 pages)
- 3 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: INTELLIGENT SYSTEMS
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Question No. _1___ is compulsory
3. Out of remaining questions attempt any 4 Questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Figures in brackets on right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly   [20]
CO- 1;   a.   Explain the major approaches to Artificial Intelligence: Acting Humanly,   [5]
SO- 1;   Thinking Humanly, Thinking Rationally, and Acting Rationally with
BL-1   suitable examples.
Explanation 4 marks
Examples 1 mark
The acting humanly approach : It defines intelligence based on observable
behavior. This approach was formalized by Alan Turing in 1950 through
the famous Turing Test.
• According to this test, a machine is considered intelligent if it can
imitate human behavior so well that a human interrogator cannot
distinguish between the machine and a real human based on written
conversation alone.
Think Humanly: This approach is closely related to cognitive
science, which combines insights from psychology, neuroscience,
and artificial intelligence.
• Example– If we want to model the thinking of Roger Federer and
make the model system to compete with someone or against him to
play in a tennis game, it may not be possible to replicate the exact
thinking as Roger Federer, however, a good build of Intelligence
systems (Robot) can play and win the game against him.
The thinking rationally approach is based on the idea that intelligence
involves correct reasoning This approach led to the development of
********** 1 **********
--- page 2 ---
logic, which became a central tool in early AI research for
representing knowledge and performing reasoning.
• These laws of thought were supposed to govern the operation of the
mind; their study initiated the field called logic.
Act Rationally: A rational agent chooses actions that maximize the
expected achievement of its goals, given the available information.
•   Unlike the laws of thought approach, acting rationally does not
require perfect reasoning. Some rational actions, such as reflexes,
do not involve explicit inference but are still effective.
•   Rationality is only concerned about the action taken and does
not what the thought process
Limitations: Achieving perfect rationality—always doing the right thing—
is not feasible in complicated environments
CO-2 ;   b.   Identify the Performance, Environment, Actuators and sensors for an AI-   [5]
SO- 1;   based fraud detection system in banking.
BL-2
Listing PEAS parameters 4 marks
Explanation for each 1 mark
1. Performance Measure (P)
This defines how well the system performs.
•   Accuracy of fraud detection
• Low false positives (legitimate transactions not flagged)
•   High true positive rate (actual frauds detected)
• Response time (real-time or near real-time detection)
• Customer satisfaction (minimal inconvenience)
•   Financial loss prevention
2. Environment (E)
This includes everything the system interacts with.
•   Banking systems (core banking, transaction processing systems)
•   Online transactions (credit/debit card, UPI, net banking)
• Customer profiles and historical transaction data
•   Fraudster activities and patterns
•   External data sources (geolocation, device info, IP address)
•   Regulatory and compliance requirements
2. Actuators (A)
These are the actions the system can take.
•   Flagging suspicious transactions
•   Blocking or declining transactions
•   Sending alerts/notifications to customers or banks
•   Triggering multi-factor authentication (OTP, verification)
•   Freezing accounts temporarily
********** 2 **********
--- page 3 ---
•   Reporting fraud cases to authorities
4. Sensors (S)
These are the inputs/data the system collects.
•   Transaction details (amount, time, location)
•   User behavior patterns (spending habits, frequency)
•   Device information (mobile, browser, IP address)
•   Login activity and authentication data
•   Historical transaction data
•   External signals (blacklists, fraud databases)
CO6;   c.   Define Constraint Satisfaction Problem in AI. Identify Variables,   [5]
SO-1;   Domain, and Constraints in Course Selection (5M) [Def-2M,
BL-1   Identification-3M]
❑ In artificial intelligence and operations research, constraint
satisfaction is the process of finding a solution to a set of
constraints that impose conditions that the variables must
satisfy.
❑ CSP is defined by a set of variables X1, X2…………Xn and set of
conditions C1, C2……….Cn such that each of the variables Xi
has a non-empty domain Di of possible values.
❖ Variables- A finite set of Variables V1,V2……….Vn
❖ Domain- Each Variable has a domain D1,D2…..Dn from which
it can take a value.
❖ Constraints- A finite set of satisfaction constraints C1,C2….Cn
Identify Variables, Domain, and Constraints in Course Selection
Variables:
Courses → C1, C2, C3
Domain:
Time slots → {Morning, Afternoon, Evening}
Constraints:
• No time clash
• Some courses only in morning
• Student must take all courses
CO - 4;   d.   Wumpus World is a classic Artificial Intelligence problem used to [5]
SO -1 ;   represent a knowledge-based environment. It is a grid-based world
BL- 1
where an intelligent agent uses logical reasoning to make decisions
under uncertainty.
…….. 1 mark
Structure and Layout :
The environment consists of a 4 × 4 grid (16 rooms).
Each room is connected to its adjacent rooms (up, down, left, right).
The agent usually starts from the bottom-left corner of the grid.
…….. 1 mark
Agent in Wumpus World :
********** 3 **********
--- page 4 ---
• The agent is the decision-maker that moves through the grid.
•   It can perform actions like move forward, turn, grab gold,
shoot arrow, and climb out.
• The agent has limited knowledge and depends on percepts
(clues).
It has only one arrow to kill the Wumpus.   …….. 2 mark
The main goal of the agent is to:
Find and grab the gold
Avoid Wumpus and pits
Return safely to the starting point
Q2   a)   Def-1M alpha (α) and beta (β) values-1M,   pruning improve [10]
efficiency-2M, Numerical-6M stepwise analysis]
CO-5;
Alpha–Beta Pruning is an optimization technique used with the
SO-1;
BL-3   Minimax algorithm in game playing. It reduces the number of nodes that
need to be evaluated by eliminating branches that cannot affect the
final decision. It gives the same result as Minimax, but in less time.
Alpha (α) and Beta (β) Values
Alpha (α):
The best (maximum) value found so far for the MAX player. It
represents the lower bound of the possible solution.
Beta (β):
The best (minimum) value found so far for the MIN player. It represents
the upper bound of the possible solution.
Pruning occur when:
How Pruning Improves Efficiency
•   In the Minimax algorithm, all nodes in the game tree are
evaluated.
•   In Alpha-Beta Pruning, unnecessary branches are skipped.
Example :
Initially, the maximizer node A sets alpha to negative infinity and beta
to positive infinity. Assuming that node A selects node B which inherits
these values. Node B which is also a maximizer picks node D. At D, the
maximizer chooses the max value (4) and then updates its alpha. Upon
returning to B (minimizer), it compares its current beta with D’s alpha
value. If D’s alpha is smaller, B’s beta value gets updated. In this
example, B’s beta gets updated since D’s alpha value is smaller.
Now, node B selects node E and passes down its current alpha and beta
values to node E. Node E inherits the alpha value of negative infinity and
beta value of 4. As a maximizer, E explores its left leaf node that holds a
value of 5. Since 5 is greater than negative infinity, E’s alpha gets
updated.
********** 4 **********
--- page 5 ---
Given that alpha is greater than beta, the other leaf node in E is
unnecessary to explore so it gets pruned.
At node B, it compares its beta value with node E’s alpha, if E’s alpha value
is lesser than B’s beta updates with E’s alpha. However, if E’s alpha is
greater than B’s beta, B’s beta remains unchanged. In our example, since
B’s beta is not greater than E’s alpha, so B’s beta value remains the same.
Returning to node A, its alpha value updates with B’s beta value because
B’s beta is greater than A’s alpha.
At node A, the maximizer’s alpha becomes 4 ensuring a value of 4 or higher.
A then explores its right child which is node R. At C, alpha is 4 and beta is
positive infinity. C then chooses its left child F. Node F inherits the alpha
value 4 and beta value positive infinity from the parent node. F’s left child
yields 0 updating the F’s alpha to 4 and also F’s right child yields 1.
Although F can achieve 1, alpha remains 4. C receives 1 from F which
makes the beta 1. As alpha is greater than beta, the entire subtree of node G
gets pruned. This pruning logic ensures that, as C is guaranteed 1 or less,
it’s irrational for A to choose C over B, where A is already guaranteed 4.
********** 5 **********
--- page 6 ---
CO-3;   b)   [10]
SO-1;   For the below figure If Source node is A and destination is Z.
BL-3   Using A star Algorithm derive the shortest path showing calculations step
by step.
********** 6 **********
--- page 7 ---
Q3   a)   Consider the crypt arithmetic problem shown below. Identify the   [10]
CO-6;   variables, domains and constraint for this problem. (10M)
SO-1;   Identifying the value of each letter (1 mark each) with proper
BL-3   mathematical justification.
S O M E
T   I M E
______________________
S P E N T
Initial state constraints:
• No two letters have the same value.
• The sums of the digits satisfy the predefined arithmetic rules.
Examine the domain for each variable at every step to evaluate
possible   solutions   for   {   S,O,M,E,N,T,P,I}
********** 7 **********

[Text in pictures on this page, read by OCR]
Cryptarithmetic Problem

Character Code

c3 c2 c1 § Al,
+ T | ME M
E
+
1 \
IF T=8 P
C3+S+T=P+10 N

1+1+8=P+10
--- page 8 ---
CO-1,3;   b)   i) Discuss various applications of Artificial Intelligence in the healthcare   [5]
sector with suitable examples.
SO-1;
BL-1,2   Any 5 applications of AI healthcare 1 mark each   [5]
ii) Describe the Hill Climbing Algorithm. Explain Local Minima and global
minima with proper diagram and explanation.
Explanation Hill Climbing (3 marks) diagram(2 marks)
• The Hill climbing algorithm is a local search algorithm that
continuously moves in the direction of increasing elevation/value
to find the peak of the mountain or the best solution to the
problem. It terminates when it reaches a peak value where no
neighbour has a higher value.
• The hill climbing algorithm is a technique that is used for
optimizing mathematical problems.
• One of the widely discussed examples of the Hill climbing
algorithm is the travel salesman problem in which we need to
minimize the distance traveled by the salesman.
•   It is also called greedy local search as it only looks to its good
immediate neighbor state and not beyond that.
• A node of a hill climbing algorithm has two components which are
state and value.
********** 8 **********

[Text in pictures on this page, read by OCR]
Cryptarithmetic Problem

Character Code

1 c3 c2 c1 s 1
BT). ff Ee
+ TI M oc Mi
PELE) pa =D
a 0| 4| j 5
~   C1+M+M=N P oO
2 N<9 N

Cryptarithmetic Problem

1 c3

BOO ie

c2

cl

3le/s]@| s-5

10468

ie) M E
1 M E
E N v

Character Code

Ss 1

o 69
M 3

E 4
Ts

| 5

P |0
--- page 9 ---
Q4   a)   Propositional Logic Representation (1 mark for each statement.. 5   [10]
marks)
CO – 4   Let:
SO – 1   •   P: Librarian is at the desk
BL- 3   • Q: Books are issued
• R: Fines are checked
•   S: Overdue books are returned
The statements can be written as:
********** 9 **********
--- page 10 ---
…4 marks for explanation
Conclusion: The librarian was at the desk.   …………… 1 mark
CO-6;   b)   i) In First-Order Logic (FOL), quantifiers are used to express statements [10]
SO-1;   about a collection of objects. They specify how many elements in the
BL-3   domain satisfy a given predicate.   ……….. 1
mark
Universal Quantifier (∀)   …………….2 marks
The universal quantifier is denoted by ∀, meaning “for all”.
It states that a predicate is true for every element in the domain.
Existential Quantifier (∃)   ……………2 marks
The existential quantifier is denoted by ∃, meaning “there exists at least
one”.
It states that a predicate is true for at least one element in the domain.
∀ (Universal) → applies to all elements
∃ (Existential) → applies to at least one element
ii) Inference rules are logical patterns used to derive valid conclusions
from given premises. They form the basis of reasoning in propositional
logic.
…..1 mark
********** 10 **********

[Text in pictures on this page, read by OCR]
From:
« Q- Rand R - S,weget
Q — S (by Hypothetical Syllogism)

But it is given:
© QA7S
This contradicts Q — S.

Now consider:

« =P — —=Q, whose contrapositive is Q + P

Since Q is true,

= P must be true
--- page 11 ---
…. 2 marks for rule and 2
marks for example
Q5   a)   [Explanation-3M, 7 setps-7M]   [10]
CO-6;
SO-1;
BL-2
Arc Consistency is a technique
used in CSP to reduce the domain of variables by removing values
that violate constraints.
CO-5,6;   b)   [5]
SO-1;
BL-2,3   Minimax Algorithm   Alpha–Beta Pruning
decision-making   An   optimization
algorithm used to find   technique applied to
the optimal move in   Minimax
games
Evaluates all nodes in   Evaluates   only
the game tree   necessary nodes
Slower due to full tree   Faster   due   to
exploration   pruning of branches
********** 11 **********
--- page 12 ---
No pruning is done   Unnecessary   i)
branches are pruned
Less efficient for large   More efficient for
trees   large trees
Gives optimal solution   Gives same optimal
solution as Minimax
Basic   game-playing   Used   to improve
algorithm   Minimax
performance
ii)   A proposition   is a declarative   statement which   is
either true or false.   It   is a technique of knowledge
representation in logical and mathematical form. Example:
•   “It is raining” → can be True or False
• “2 + 2 = 4” → True   ………….. 2 marks
Atomic Propositions: Atomic propositions are the simple
propositions. It consists of a single proposition symbol. These are the
sentences which must be either true or false.
1. 2+2 is 4, it is an atomic proposition as it is a true fact.
2. "The Sun is cold" is also a proposition as it is a false fact.
•   P: “It is raining”
• Q: “The sun is shining”
These are basic statements with no logical connectives. …….. 1.5
marks
Compound propositions: Compound propositions are constructed by
combining simpler or atomic propositions, using parenthesis and logical
connectives.
1. "It is raining today, and street is wet."
"Ankit is a doctor, and his clinic is in Mumbai."   ….1.5 marks
Q6   a) Explain the following types of AI agents in detail with diagram ,mentioning   [10]
their advantages and limitations
CO-2;
SO-1;
1) Simple Reflex Agent….Diagram and explanation(5 marks)
BL-1
2) Model-Based Reflex Agent…. Diagram and explanation(5 marks)
•   Solution:
The Simple reflex agents are the simplest agents. These agents take
decisions on the basis of the current precepts and ignore the rest of the
percept history.
These agents only succeed in the fully observable environment.
The Simple reflex agent does not consider any part of precepts history
during their decision and action process.
The Simple reflex agent works on the Condition-action rule, which means it
maps the current state to action. Such as a Room Cleaner agent, it works
only if there is dirt in the room.
********** 12 **********
--- page 13 ---
• The Model-based agent can work in a partially observable
environment, and track the situation.
• A model-based agent has two important factors:
• Model: It is knowledge about "how things happen in the
world," so it is called a
Model-based agent.
•   Internal State: It is a representation of the current state
based on percept history.
•   These agents have the model, "which is knowledge of the
world" and based on the model they perform actions.
• Updating the agent state requires information about:
• How the world evolves
• How the agent's action affects the world.
34
********** 13 **********

[Text in pictures on this page, read by OCR]
f OY

(— ae 7 Precepts
$ -

Sensors

State Sal as real

How the world evolves |» | What the world s.
is like now :

— i
What my actions do 5
should do now

| Action

Actuators’

\ Agent SD)
--- page 14 ---
CO-3;   b)   Given a 3x3 board with 8 tiles (every tile has one number from 1 to 8) and   [10]
SO-1;
one empty space. The objective is to place the numbers on tiles in order
BL-2
using the empty space. We can slide four adjacent (left, right, above and
below) tiles into the empty space. Using Greedy best first search. Show the
step by step method to reach the goal state for the following initial state.
1   2   3
4   6
7   5   8
Initial State
1   2   3
4   5   6
7   8
Goal State
Q7   a)   [10]
CO-4;
SO-1;
BL-3
Answer : Statement 1 is always true-Tautology ………… 1 mark
********** 14 **********
--- page 15 ---
Writing all correct values for:
column (P ∨ Q ) - 2 marks
column (P ∨ Q ) ∧ R - 2 marks
column (P ∧ R) - 2 marks
column (Q ∧ R) - 2 marks
column (P ∧ R) ∨ (Q ∧ R) – 1 mark
CO-4;   b) Predicate form:   …….. 1 mark   [10]
SO-1;
• Spot is a cat
BL-2
→ Cat(Spot)
• All cats are mammals
→ ∀x (Cat(x) → Mammal(x))
• All mammals are warm-blooded
→ ∀x (Mammal(x) → WarmBlooded(x))
1. Eliminate Implications   ……. 2 marks
Using rule: P→Q = ¬P ∨ Q
1. Cat(Spot)
2. ∀x (¬Cat(x) ∨ Mammal(x))
3. ∀x (¬Mammal(x) ∨ WarmBlooded(x))
2. Standardize Variables ……. 2 marks
Already unique (only one x)
3. Skolemization ……. 2 marks
No existential quantifiers
4. Drop Universal Quantifiers ……. 2 marks
Cat(Spot)
¬Cat(x) ∨ Mammal(x)
¬Mammal(x) ∨ WarmBlooded(x)
5. CNF……. 1 marks
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 7f4d139de744

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/BTech_AIML_7053/INTELLIGENT SYSTEMS/ANS_INTELLIGENT SYSTEMS(702AI0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (15 pages)
- 3 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: INTELLIGENT SYSTEMS
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Question No. _1___ is compulsory
3. Out of remaining questions attempt any 4 Questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Figures in brackets on right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly   [20]
CO- 1;   a.   Explain the major approaches to Artificial Intelligence: Acting Humanly,   [5]
SO- 1;   Thinking Humanly, Thinking Rationally, and Acting Rationally with
BL-1   suitable examples.
Explanation 4 marks
Examples 1 mark
The acting humanly approach : It defines intelligence based on observable
behavior. This approach was formalized by Alan Turing in 1950 through
the famous Turing Test.
• According to this test, a machine is considered intelligent if it can
imitate human behavior so well that a human interrogator cannot
distinguish between the machine and a real human based on written
conversation alone.
Think Humanly: This approach is closely related to cognitive
science, which combines insights from psychology, neuroscience,
and artificial intelligence.
• Example– If we want to model the thinking of Roger Federer and
make the model system to compete with someone or against him to
play in a tennis game, it may not be possible to replicate the exact
thinking as Roger Federer, however, a good build of Intelligence
systems (Robot) can play and win the game against him.
The thinking rationally approach is based on the idea that intelligence
involves correct reasoning This approach led to the development of
********** 1 **********
--- page 2 ---
logic, which became a central tool in early AI research for
representing knowledge and performing reasoning.
• These laws of thought were supposed to govern the operation of the
mind; their study initiated the field called logic.
Act Rationally: A rational agent chooses actions that maximize the
expected achievement of its goals, given the available information.
•   Unlike the laws of thought approach, acting rationally does not
require perfect reasoning. Some rational actions, such as reflexes,
do not involve explicit inference but are still effective.
•   Rationality is only concerned about the action taken and does
not what the thought process
Limitations: Achieving perfect rationality—always doing the right thing—
is not feasible in complicated environments
CO-2 ;   b.   Identify the Performance, Environment, Actuators and sensors for an AI-   [5]
SO- 1;   based fraud detection system in banking.
BL-2
Listing PEAS parameters 4 marks
Explanation for each 1 mark
1. Performance Measure (P)
This defines how well the system performs.
•   Accuracy of fraud detection
• Low false positives (legitimate transactions not flagged)
•   High true positive rate (actual frauds detected)
• Response time (real-time or near real-time detection)
• Customer satisfaction (minimal inconvenience)
•   Financial loss prevention
2. Environment (E)
This includes everything the system interacts with.
•   Banking systems (core banking, transaction processing systems)
•   Online transactions (credit/debit card, UPI, net banking)
• Customer profiles and historical transaction data
•   Fraudster activities and patterns
•   External data sources (geolocation, device info, IP address)
•   Regulatory and compliance requirements
2. Actuators (A)
These are the actions the system can take.
•   Flagging suspicious transactions
•   Blocking or declining transactions
•   Sending alerts/notifications to customers or banks
•   Triggering multi-factor authentication (OTP, verification)
•   Freezing accounts temporarily
********** 2 **********
--- page 3 ---
•   Reporting fraud cases to authorities
4. Sensors (S)
These are the inputs/data the system collects.
•   Transaction details (amount, time, location)
•   User behavior patterns (spending habits, frequency)
•   Device information (mobile, browser, IP address)
•   Login activity and authentication data
•   Historical transaction data
•   External signals (blacklists, fraud databases)
CO6;   c.   Define Constraint Satisfaction Problem in AI. Identify Variables,   [5]
SO-1;   Domain, and Constraints in Course Selection (5M) [Def-2M,
BL-1   Identification-3M]
❑ In artificial intelligence and operations research, constraint
satisfaction is the process of finding a solution to a set of
constraints that impose conditions that the variables must
satisfy.
❑ CSP is defined by a set of variables X1, X2…………Xn and set of
conditions C1, C2……….Cn such that each of the variables Xi
has a non-empty domain Di of possible values.
❖ Variables- A finite set of Variables V1,V2……….Vn
❖ Domain- Each Variable has a domain D1,D2…..Dn from which
it can take a value.
❖ Constraints- A finite set of satisfaction constraints C1,C2….Cn
Identify Variables, Domain, and Constraints in Course Selection
Variables:
Courses → C1, C2, C3
Domain:
Time slots → {Morning, Afternoon, Evening}
Constraints:
• No time clash
• Some courses only in morning
• Student must take all courses
CO - 4;   d.   Wumpus World is a classic Artificial Intelligence problem used to [5]
SO -1 ;   represent a knowledge-based environment. It is a grid-based world
BL- 1
where an intelligent agent uses logical reasoning to make decisions
under uncertainty.
…….. 1 mark
Structure and Layout :
The environment consists of a 4 × 4 grid (16 rooms).
Each room is connected to its adjacent rooms (up, down, left, right).
The agent usually starts from the bottom-left corner of the grid.
…….. 1 mark
Agent in Wumpus World :
********** 3 **********
--- page 4 ---
• The agent is the decision-maker that moves through the grid.
•   It can perform actions like move forward, turn, grab gold,
shoot arrow, and climb out.
• The agent has limited knowledge and depends on percepts
(clues).
It has only one arrow to kill the Wumpus.   …….. 2 mark
The main goal of the agent is to:
Find and grab the gold
Avoid Wumpus and pits
Return safely to the starting point
Q2   a)   Def-1M alpha (α) and beta (β) values-1M,   pruning improve [10]
efficiency-2M, Numerical-6M stepwise analysis]
CO-5;
Alpha–Beta Pruning is an optimization technique used with the
SO-1;
BL-3   Minimax algorithm in game playing. It reduces the number of nodes that
need to be evaluated by eliminating branches that cannot affect the
final decision. It gives the same result as Minimax, but in less time.
Alpha (α) and Beta (β) Values
Alpha (α):
The best (maximum) value found so far for the MAX player. It
represents the lower bound of the possible solution.
Beta (β):
The best (minimum) value found so far for the MIN player. It represents
the upper bound of the possible solution.
Pruning occur when:
How Pruning Improves Efficiency
•   In the Minimax algorithm, all nodes in the game tree are
evaluated.
•   In Alpha-Beta Pruning, unnecessary branches are skipped.
Example :
Initially, the maximizer node A sets alpha to negative infinity and beta
to positive infinity. Assuming that node A selects node B which inherits
these values. Node B which is also a maximizer picks node D. At D, the
maximizer chooses the max value (4) and then updates its alpha. Upon
returning to B (minimizer), it compares its current beta with D’s alpha
value. If D’s alpha is smaller, B’s beta value gets updated. In this
example, B’s beta gets updated since D’s alpha value is smaller.
Now, node B selects node E and passes down its current alpha and beta
values to node E. Node E inherits the alpha value of negative infinity and
beta value of 4. As a maximizer, E explores its left leaf node that holds a
value of 5. Since 5 is greater than negative infinity, E’s alpha gets
updated.
********** 4 **********
--- page 5 ---
Given that alpha is greater than beta, the other leaf node in E is
unnecessary to explore so it gets pruned.
At node B, it compares its beta value with node E’s alpha, if E’s alpha value
is lesser than B’s beta updates with E’s alpha. However, if E’s alpha is
greater than B’s beta, B’s beta remains unchanged. In our example, since
B’s beta is not greater than E’s alpha, so B’s beta value remains the same.
Returning to node A, its alpha value updates with B’s beta value because
B’s beta is greater than A’s alpha.
At node A, the maximizer’s alpha becomes 4 ensuring a value of 4 or higher.
A then explores its right child which is node R. At C, alpha is 4 and beta is
positive infinity. C then chooses its left child F. Node F inherits the alpha
value 4 and beta value positive infinity from the parent node. F’s left child
yields 0 updating the F’s alpha to 4 and also F’s right child yields 1.
Although F can achieve 1, alpha remains 4. C receives 1 from F which
makes the beta 1. As alpha is greater than beta, the entire subtree of node G
gets pruned. This pruning logic ensures that, as C is guaranteed 1 or less,
it’s irrational for A to choose C over B, where A is already guaranteed 4.
********** 5 **********
--- page 6 ---
CO-3;   b)   [10]
SO-1;   For the below figure If Source node is A and destination is Z.
BL-3   Using A star Algorithm derive the shortest path showing calculations step
by step.
********** 6 **********
--- page 7 ---
Q3   a)   Consider the crypt arithmetic problem shown below. Identify the   [10]
CO-6;   variables, domains and constraint for this problem. (10M)
SO-1;   Identifying the value of each letter (1 mark each) with proper
BL-3   mathematical justification.
S O M E
T   I M E
______________________
S P E N T
Initial state constraints:
• No two letters have the same value.
• The sums of the digits satisfy the predefined arithmetic rules.
Examine the domain for each variable at every step to evaluate
possible   solutions   for   {   S,O,M,E,N,T,P,I}
********** 7 **********

[Text in pictures on this page, read by OCR]
Cryptarithmetic Problem

Character Code

c3 c2 c1 § Al,
+ T | ME M
E
+
1 \
IF T=8 P
C3+S+T=P+10 N

1+1+8=P+10
--- page 8 ---
CO-1,3;   b)   i) Discuss various applications of Artificial Intelligence in the healthcare   [5]
sector with suitable examples.
SO-1;
BL-1,2   Any 5 applications of AI healthcare 1 mark each   [5]
ii) Describe the Hill Climbing Algorithm. Explain Local Minima and global
minima with proper diagram and explanation.
Explanation Hill Climbing (3 marks) diagram(2 marks)
• The Hill climbing algorithm is a local search algorithm that
continuously moves in the direction of increasing elevation/value
to find the peak of the mountain or the best solution to the
problem. It terminates when it reaches a peak value where no
neighbour has a higher value.
• The hill climbing algorithm is a technique that is used for
optimizing mathematical problems.
• One of the widely discussed examples of the Hill climbing
algorithm is the travel salesman problem in which we need to
minimize the distance traveled by the salesman.
•   It is also called greedy local search as it only looks to its good
immediate neighbor state and not beyond that.
• A node of a hill climbing algorithm has two components which are
state and value.
********** 8 **********

[Text in pictures on this page, read by OCR]
Cryptarithmetic Problem

Character Code

1 c3 c2 c1 s 1
BT). ff Ee
+ TI M oc Mi
PELE) pa =D
a 0| 4| j 5
~   C1+M+M=N P oO
2 N<9 N

Cryptarithmetic Problem

1 c3

BOO ie

c2

cl

3le/s]@| s-5

10468

ie) M E
1 M E
E N v

Character Code

Ss 1

o 69
M 3

E 4
Ts

| 5

P |0
--- page 9 ---
Q4   a)   Propositional Logic Representation (1 mark for each statement.. 5   [10]
marks)
CO – 4   Let:
SO – 1   •   P: Librarian is at the desk
BL- 3   • Q: Books are issued
• R: Fines are checked
•   S: Overdue books are returned
The statements can be written as:
********** 9 **********
--- page 10 ---
…4 marks for explanation
Conclusion: The librarian was at the desk.   …………… 1 mark
CO-6;   b)   i) In First-Order Logic (FOL), quantifiers are used to express statements [10]
SO-1;   about a collection of objects. They specify how many elements in the
BL-3   domain satisfy a given predicate.   ……….. 1
mark
Universal Quantifier (∀)   …………….2 marks
The universal quantifier is denoted by ∀, meaning “for all”.
It states that a predicate is true for every element in the domain.
Existential Quantifier (∃)   ……………2 marks
The existential quantifier is denoted by ∃, meaning “there exists at least
one”.
It states that a predicate is true for at least one element in the domain.
∀ (Universal) → applies to all elements
∃ (Existential) → applies to at least one element
ii) Inference rules are logical patterns used to derive valid conclusions
from given premises. They form the basis of reasoning in propositional
logic.
…..1 mark
********** 10 **********

[Text in pictures on this page, read by OCR]
From:
« Q- Rand R - S,weget
Q — S (by Hypothetical Syllogism)

But it is given:
© QA7S
This contradicts Q — S.

Now consider:

« =P — —=Q, whose contrapositive is Q + P

Since Q is true,

= P must be true
--- page 11 ---
…. 2 marks for rule and 2
marks for example
Q5   a)   [Explanation-3M, 7 setps-7M]   [10]
CO-6;
SO-1;
BL-2
Arc Consistency is a technique
used in CSP to reduce the domain of variables by removing values
that violate constraints.
CO-5,6;   b)   [5]
SO-1;
BL-2,3   Minimax Algorithm   Alpha–Beta Pruning
decision-making   An   optimization
algorithm used to find   technique applied to
the optimal move in   Minimax
games
Evaluates all nodes in   Evaluates   only
the game tree   necessary nodes
Slower due to full tree   Faster   due   to
exploration   pruning of branches
********** 11 **********
--- page 12 ---
No pruning is done   Unnecessary   i)
branches are pruned
Less efficient for large   More efficient for
trees   large trees
Gives optimal solution   Gives same optimal
solution as Minimax
Basic   game-playing   Used   to improve
algorithm   Minimax
performance
ii)   A proposition   is a declarative   statement which   is
either true or false.   It   is a technique of knowledge
representation in logical and mathematical form. Example:
•   “It is raining” → can be True or False
• “2 + 2 = 4” → True   ………….. 2 marks
Atomic Propositions: Atomic propositions are the simple
propositions. It consists of a single proposition symbol. These are the
sentences which must be either true or false.
1. 2+2 is 4, it is an atomic proposition as it is a true fact.
2. "The Sun is cold" is also a proposition as it is a false fact.
•   P: “It is raining”
• Q: “The sun is shining”
These are basic statements with no logical connectives. …….. 1.5
marks
Compound propositions: Compound propositions are constructed by
combining simpler or atomic propositions, using parenthesis and logical
connectives.
1. "It is raining today, and street is wet."
"Ankit is a doctor, and his clinic is in Mumbai."   ….1.5 marks
Q6   a) Explain the following types of AI agents in detail with diagram ,mentioning   [10]
their advantages and limitations
CO-2;
SO-1;
1) Simple Reflex Agent….Diagram and explanation(5 marks)
BL-1
2) Model-Based Reflex Agent…. Diagram and explanation(5 marks)
•   Solution:
The Simple reflex agents are the simplest agents. These agents take
decisions on the basis of the current precepts and ignore the rest of the
percept history.
These agents only succeed in the fully observable environment.
The Simple reflex agent does not consider any part of precepts history
during their decision and action process.
The Simple reflex agent works on the Condition-action rule, which means it
maps the current state to action. Such as a Room Cleaner agent, it works
only if there is dirt in the room.
********** 12 **********
--- page 13 ---
• The Model-based agent can work in a partially observable
environment, and track the situation.
• A model-based agent has two important factors:
• Model: It is knowledge about "how things happen in the
world," so it is called a
Model-based agent.
•   Internal State: It is a representation of the current state
based on percept history.
•   These agents have the model, "which is knowledge of the
world" and based on the model they perform actions.
• Updating the agent state requires information about:
• How the world evolves
• How the agent's action affects the world.
34
********** 13 **********

[Text in pictures on this page, read by OCR]
f OY

(— ae 7 Precepts
$ -

Sensors

State Sal as real

How the world evolves |» | What the world s.
is like now :

— i
What my actions do 5
should do now

| Action

Actuators’

\ Agent SD)
--- page 14 ---
CO-3;   b)   Given a 3x3 board with 8 tiles (every tile has one number from 1 to 8) and   [10]
SO-1;
one empty space. The objective is to place the numbers on tiles in order
BL-2
using the empty space. We can slide four adjacent (left, right, above and
below) tiles into the empty space. Using Greedy best first search. Show the
step by step method to reach the goal state for the following initial state.
1   2   3
4   6
7   5   8
Initial State
1   2   3
4   5   6
7   8
Goal State
Q7   a)   [10]
CO-4;
SO-1;
BL-3
Answer : Statement 1 is always true-Tautology ………… 1 mark
********** 14 **********
--- page 15 ---
Writing all correct values for:
column (P ∨ Q ) - 2 marks
column (P ∨ Q ) ∧ R - 2 marks
column (P ∧ R) - 2 marks
column (Q ∧ R) - 2 marks
column (P ∧ R) ∨ (Q ∧ R) – 1 mark
CO-4;   b) Predicate form:   …….. 1 mark   [10]
SO-1;
• Spot is a cat
BL-2
→ Cat(Spot)
• All cats are mammals
→ ∀x (Cat(x) → Mammal(x))
• All mammals are warm-blooded
→ ∀x (Mammal(x) → WarmBlooded(x))
1. Eliminate Implications   ……. 2 marks
Using rule: P→Q = ¬P ∨ Q
1. Cat(Spot)
2. ∀x (¬Cat(x) ∨ Mammal(x))
3. ∀x (¬Mammal(x) ∨ WarmBlooded(x))
2. Standardize Variables ……. 2 marks
Already unique (only one x)
3. Skolemization ……. 2 marks
No existential quantifiers
4. Drop Universal Quantifiers ……. 2 marks
Cat(Spot)
¬Cat(x) ∨ Mammal(x)
¬Mammal(x) ∨ WarmBlooded(x)
5. CNF……. 1 marks
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 0e6b00e0c1a5

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MBATech_AI_7051/INTELLIGENT SYSTEMS/ANS_INTELLIGENT SYSTEMS(702AI0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (15 pages)
- 3 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: INTELLIGENT SYSTEMS
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Question No. _1___ is compulsory
3. Out of remaining questions attempt any 4 Questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Figures in brackets on right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly   [20]
CO- 1;   a.   Explain the major approaches to Artificial Intelligence: Acting Humanly,   [5]
SO- 1;   Thinking Humanly, Thinking Rationally, and Acting Rationally with
BL-1   suitable examples.
Explanation 4 marks
Examples 1 mark
The acting humanly approach : It defines intelligence based on observable
behavior. This approach was formalized by Alan Turing in 1950 through
the famous Turing Test.
• According to this test, a machine is considered intelligent if it can
imitate human behavior so well that a human interrogator cannot
distinguish between the machine and a real human based on written
conversation alone.
Think Humanly: This approach is closely related to cognitive
science, which combines insights from psychology, neuroscience,
and artificial intelligence.
• Example– If we want to model the thinking of Roger Federer and
make the model system to compete with someone or against him to
play in a tennis game, it may not be possible to replicate the exact
thinking as Roger Federer, however, a good build of Intelligence
systems (Robot) can play and win the game against him.
The thinking rationally approach is based on the idea that intelligence
involves correct reasoning This approach led to the development of
********** 1 **********
--- page 2 ---
logic, which became a central tool in early AI research for
representing knowledge and performing reasoning.
• These laws of thought were supposed to govern the operation of the
mind; their study initiated the field called logic.
Act Rationally: A rational agent chooses actions that maximize the
expected achievement of its goals, given the available information.
•   Unlike the laws of thought approach, acting rationally does not
require perfect reasoning. Some rational actions, such as reflexes,
do not involve explicit inference but are still effective.
•   Rationality is only concerned about the action taken and does
not what the thought process
Limitations: Achieving perfect rationality—always doing the right thing—
is not feasible in complicated environments
CO-2 ;   b.   Identify the Performance, Environment, Actuators and sensors for an AI-   [5]
SO- 1;   based fraud detection system in banking.
BL-2
Listing PEAS parameters 4 marks
Explanation for each 1 mark
1. Performance Measure (P)
This defines how well the system performs.
•   Accuracy of fraud detection
• Low false positives (legitimate transactions not flagged)
•   High true positive rate (actual frauds detected)
• Response time (real-time or near real-time detection)
• Customer satisfaction (minimal inconvenience)
•   Financial loss prevention
2. Environment (E)
This includes everything the system interacts with.
•   Banking systems (core banking, transaction processing systems)
•   Online transactions (credit/debit card, UPI, net banking)
• Customer profiles and historical transaction data
•   Fraudster activities and patterns
•   External data sources (geolocation, device info, IP address)
•   Regulatory and compliance requirements
2. Actuators (A)
These are the actions the system can take.
•   Flagging suspicious transactions
•   Blocking or declining transactions
•   Sending alerts/notifications to customers or banks
•   Triggering multi-factor authentication (OTP, verification)
•   Freezing accounts temporarily
********** 2 **********
--- page 3 ---
•   Reporting fraud cases to authorities
4. Sensors (S)
These are the inputs/data the system collects.
•   Transaction details (amount, time, location)
•   User behavior patterns (spending habits, frequency)
•   Device information (mobile, browser, IP address)
•   Login activity and authentication data
•   Historical transaction data
•   External signals (blacklists, fraud databases)
CO6;   c.   Define Constraint Satisfaction Problem in AI. Identify Variables,   [5]
SO-1;   Domain, and Constraints in Course Selection (5M) [Def-2M,
BL-1   Identification-3M]
❑ In artificial intelligence and operations research, constraint
satisfaction is the process of finding a solution to a set of
constraints that impose conditions that the variables must
satisfy.
❑ CSP is defined by a set of variables X1, X2…………Xn and set of
conditions C1, C2……….Cn such that each of the variables Xi
has a non-empty domain Di of possible values.
❖ Variables- A finite set of Variables V1,V2……….Vn
❖ Domain- Each Variable has a domain D1,D2…..Dn from which
it can take a value.
❖ Constraints- A finite set of satisfaction constraints C1,C2….Cn
Identify Variables, Domain, and Constraints in Course Selection
Variables:
Courses → C1, C2, C3
Domain:
Time slots → {Morning, Afternoon, Evening}
Constraints:
• No time clash
• Some courses only in morning
• Student must take all courses
CO - 4;   d.   Wumpus World is a classic Artificial Intelligence problem used to [5]
SO -1 ;   represent a knowledge-based environment. It is a grid-based world
BL- 1
where an intelligent agent uses logical reasoning to make decisions
under uncertainty.
…….. 1 mark
Structure and Layout :
The environment consists of a 4 × 4 grid (16 rooms).
Each room is connected to its adjacent rooms (up, down, left, right).
The agent usually starts from the bottom-left corner of the grid.
…….. 1 mark
Agent in Wumpus World :
********** 3 **********
--- page 4 ---
• The agent is the decision-maker that moves through the grid.
•   It can perform actions like move forward, turn, grab gold,
shoot arrow, and climb out.
• The agent has limited knowledge and depends on percepts
(clues).
It has only one arrow to kill the Wumpus.   …….. 2 mark
The main goal of the agent is to:
Find and grab the gold
Avoid Wumpus and pits
Return safely to the starting point
Q2   a)   Def-1M alpha (α) and beta (β) values-1M,   pruning improve [10]
efficiency-2M, Numerical-6M stepwise analysis]
CO-5;
Alpha–Beta Pruning is an optimization technique used with the
SO-1;
BL-3   Minimax algorithm in game playing. It reduces the number of nodes that
need to be evaluated by eliminating branches that cannot affect the
final decision. It gives the same result as Minimax, but in less time.
Alpha (α) and Beta (β) Values
Alpha (α):
The best (maximum) value found so far for the MAX player. It
represents the lower bound of the possible solution.
Beta (β):
The best (minimum) value found so far for the MIN player. It represents
the upper bound of the possible solution.
Pruning occur when:
How Pruning Improves Efficiency
•   In the Minimax algorithm, all nodes in the game tree are
evaluated.
•   In Alpha-Beta Pruning, unnecessary branches are skipped.
Example :
Initially, the maximizer node A sets alpha to negative infinity and beta
to positive infinity. Assuming that node A selects node B which inherits
these values. Node B which is also a maximizer picks node D. At D, the
maximizer chooses the max value (4) and then updates its alpha. Upon
returning to B (minimizer), it compares its current beta with D’s alpha
value. If D’s alpha is smaller, B’s beta value gets updated. In this
example, B’s beta gets updated since D’s alpha value is smaller.
Now, node B selects node E and passes down its current alpha and beta
values to node E. Node E inherits the alpha value of negative infinity and
beta value of 4. As a maximizer, E explores its left leaf node that holds a
value of 5. Since 5 is greater than negative infinity, E’s alpha gets
updated.
********** 4 **********
--- page 5 ---
Given that alpha is greater than beta, the other leaf node in E is
unnecessary to explore so it gets pruned.
At node B, it compares its beta value with node E’s alpha, if E’s alpha value
is lesser than B’s beta updates with E’s alpha. However, if E’s alpha is
greater than B’s beta, B’s beta remains unchanged. In our example, since
B’s beta is not greater than E’s alpha, so B’s beta value remains the same.
Returning to node A, its alpha value updates with B’s beta value because
B’s beta is greater than A’s alpha.
At node A, the maximizer’s alpha becomes 4 ensuring a value of 4 or higher.
A then explores its right child which is node R. At C, alpha is 4 and beta is
positive infinity. C then chooses its left child F. Node F inherits the alpha
value 4 and beta value positive infinity from the parent node. F’s left child
yields 0 updating the F’s alpha to 4 and also F’s right child yields 1.
Although F can achieve 1, alpha remains 4. C receives 1 from F which
makes the beta 1. As alpha is greater than beta, the entire subtree of node G
gets pruned. This pruning logic ensures that, as C is guaranteed 1 or less,
it’s irrational for A to choose C over B, where A is already guaranteed 4.
********** 5 **********
--- page 6 ---
CO-3;   b)   [10]
SO-1;   For the below figure If Source node is A and destination is Z.
BL-3   Using A star Algorithm derive the shortest path showing calculations step
by step.
********** 6 **********
--- page 7 ---
Q3   a)   Consider the crypt arithmetic problem shown below. Identify the   [10]
CO-6;   variables, domains and constraint for this problem. (10M)
SO-1;   Identifying the value of each letter (1 mark each) with proper
BL-3   mathematical justification.
S O M E
T   I M E
______________________
S P E N T
Initial state constraints:
• No two letters have the same value.
• The sums of the digits satisfy the predefined arithmetic rules.
Examine the domain for each variable at every step to evaluate
possible   solutions   for   {   S,O,M,E,N,T,P,I}
********** 7 **********

[Text in pictures on this page, read by OCR]
Cryptarithmetic Problem

Character Code

c3 c2 c1 § Al,
+ T | ME M
E
+
1 \
IF T=8 P
C3+S+T=P+10 N

1+1+8=P+10
--- page 8 ---
CO-1,3;   b)   i) Discuss various applications of Artificial Intelligence in the healthcare   [5]
sector with suitable examples.
SO-1;
BL-1,2   Any 5 applications of AI healthcare 1 mark each   [5]
ii) Describe the Hill Climbing Algorithm. Explain Local Minima and global
minima with proper diagram and explanation.
Explanation Hill Climbing (3 marks) diagram(2 marks)
• The Hill climbing algorithm is a local search algorithm that
continuously moves in the direction of increasing elevation/value
to find the peak of the mountain or the best solution to the
problem. It terminates when it reaches a peak value where no
neighbour has a higher value.
• The hill climbing algorithm is a technique that is used for
optimizing mathematical problems.
• One of the widely discussed examples of the Hill climbing
algorithm is the travel salesman problem in which we need to
minimize the distance traveled by the salesman.
•   It is also called greedy local search as it only looks to its good
immediate neighbor state and not beyond that.
• A node of a hill climbing algorithm has two components which are
state and value.
********** 8 **********

[Text in pictures on this page, read by OCR]
Cryptarithmetic Problem

Character Code

1 c3 c2 c1 s 1
BT). ff Ee
+ TI M oc Mi
PELE) pa =D
a 0| 4| j 5
~   C1+M+M=N P oO
2 N<9 N

Cryptarithmetic Problem

1 c3

BOO ie

c2

cl

3le/s]@| s-5

10468

ie) M E
1 M E
E N v

Character Code

Ss 1

o 69
M 3

E 4
Ts

| 5

P |0
--- page 9 ---
Q4   a)   Propositional Logic Representation (1 mark for each statement.. 5   [10]
marks)
CO – 4   Let:
SO – 1   •   P: Librarian is at the desk
BL- 3   • Q: Books are issued
• R: Fines are checked
•   S: Overdue books are returned
The statements can be written as:
********** 9 **********
--- page 10 ---
…4 marks for explanation
Conclusion: The librarian was at the desk.   …………… 1 mark
CO-6;   b)   i) In First-Order Logic (FOL), quantifiers are used to express statements [10]
SO-1;   about a collection of objects. They specify how many elements in the
BL-3   domain satisfy a given predicate.   ……….. 1
mark
Universal Quantifier (∀)   …………….2 marks
The universal quantifier is denoted by ∀, meaning “for all”.
It states that a predicate is true for every element in the domain.
Existential Quantifier (∃)   ……………2 marks
The existential quantifier is denoted by ∃, meaning “there exists at least
one”.
It states that a predicate is true for at least one element in the domain.
∀ (Universal) → applies to all elements
∃ (Existential) → applies to at least one element
ii) Inference rules are logical patterns used to derive valid conclusions
from given premises. They form the basis of reasoning in propositional
logic.
…..1 mark
********** 10 **********

[Text in pictures on this page, read by OCR]
From:
« Q- Rand R - S,weget
Q — S (by Hypothetical Syllogism)

But it is given:
© QA7S
This contradicts Q — S.

Now consider:

« =P — —=Q, whose contrapositive is Q + P

Since Q is true,

= P must be true
--- page 11 ---
…. 2 marks for rule and 2
marks for example
Q5   a)   [Explanation-3M, 7 setps-7M]   [10]
CO-6;
SO-1;
BL-2
Arc Consistency is a technique
used in CSP to reduce the domain of variables by removing values
that violate constraints.
CO-5,6;   b)   [5]
SO-1;
BL-2,3   Minimax Algorithm   Alpha–Beta Pruning
decision-making   An   optimization
algorithm used to find   technique applied to
the optimal move in   Minimax
games
Evaluates all nodes in   Evaluates   only
the game tree   necessary nodes
Slower due to full tree   Faster   due   to
exploration   pruning of branches
********** 11 **********
--- page 12 ---
No pruning is done   Unnecessary   i)
branches are pruned
Less efficient for large   More efficient for
trees   large trees
Gives optimal solution   Gives same optimal
solution as Minimax
Basic   game-playing   Used   to improve
algorithm   Minimax
performance
ii)   A proposition   is a declarative   statement which   is
either true or false.   It   is a technique of knowledge
representation in logical and mathematical form. Example:
•   “It is raining” → can be True or False
• “2 + 2 = 4” → True   ………….. 2 marks
Atomic Propositions: Atomic propositions are the simple
propositions. It consists of a single proposition symbol. These are the
sentences which must be either true or false.
1. 2+2 is 4, it is an atomic proposition as it is a true fact.
2. "The Sun is cold" is also a proposition as it is a false fact.
•   P: “It is raining”
• Q: “The sun is shining”
These are basic statements with no logical connectives. …….. 1.5
marks
Compound propositions: Compound propositions are constructed by
combining simpler or atomic propositions, using parenthesis and logical
connectives.
1. "It is raining today, and street is wet."
"Ankit is a doctor, and his clinic is in Mumbai."   ….1.5 marks
Q6   a) Explain the following types of AI agents in detail with diagram ,mentioning   [10]
their advantages and limitations
CO-2;
SO-1;
1) Simple Reflex Agent….Diagram and explanation(5 marks)
BL-1
2) Model-Based Reflex Agent…. Diagram and explanation(5 marks)
•   Solution:
The Simple reflex agents are the simplest agents. These agents take
decisions on the basis of the current precepts and ignore the rest of the
percept history.
These agents only succeed in the fully observable environment.
The Simple reflex agent does not consider any part of precepts history
during their decision and action process.
The Simple reflex agent works on the Condition-action rule, which means it
maps the current state to action. Such as a Room Cleaner agent, it works
only if there is dirt in the room.
********** 12 **********
--- page 13 ---
• The Model-based agent can work in a partially observable
environment, and track the situation.
• A model-based agent has two important factors:
• Model: It is knowledge about "how things happen in the
world," so it is called a
Model-based agent.
•   Internal State: It is a representation of the current state
based on percept history.
•   These agents have the model, "which is knowledge of the
world" and based on the model they perform actions.
• Updating the agent state requires information about:
• How the world evolves
• How the agent's action affects the world.
34
********** 13 **********

[Text in pictures on this page, read by OCR]
f OY

(— ae 7 Precepts
$ -

Sensors

State Sal as real

How the world evolves |» | What the world s.
is like now :

— i
What my actions do 5
should do now

| Action

Actuators’

\ Agent SD)
--- page 14 ---
CO-3;   b)   Given a 3x3 board with 8 tiles (every tile has one number from 1 to 8) and   [10]
SO-1;
one empty space. The objective is to place the numbers on tiles in order
BL-2
using the empty space. We can slide four adjacent (left, right, above and
below) tiles into the empty space. Using Greedy best first search. Show the
step by step method to reach the goal state for the following initial state.
1   2   3
4   6
7   5   8
Initial State
1   2   3
4   5   6
7   8
Goal State
Q7   a)   [10]
CO-4;
SO-1;
BL-3
Answer : Statement 1 is always true-Tautology ………… 1 mark
********** 14 **********
--- page 15 ---
Writing all correct values for:
column (P ∨ Q ) - 2 marks
column (P ∨ Q ) ∧ R - 2 marks
column (P ∧ R) - 2 marks
column (Q ∧ R) - 2 marks
column (P ∧ R) ∨ (Q ∧ R) – 1 mark
CO-4;   b) Predicate form:   …….. 1 mark   [10]
SO-1;
• Spot is a cat
BL-2
→ Cat(Spot)
• All cats are mammals
→ ∀x (Cat(x) → Mammal(x))
• All mammals are warm-blooded
→ ∀x (Mammal(x) → WarmBlooded(x))
1. Eliminate Implications   ……. 2 marks
Using rule: P→Q = ¬P ∨ Q
1. Cat(Spot)
2. ∀x (¬Cat(x) ∨ Mammal(x))
3. ∀x (¬Mammal(x) ∨ WarmBlooded(x))
2. Standardize Variables ……. 2 marks
Already unique (only one x)
3. Skolemization ……. 2 marks
No existential quantifiers
4. Drop Universal Quantifiers ……. 2 marks
Cat(Spot)
¬Cat(x) ∨ Mammal(x)
¬Mammal(x) ∨ WarmBlooded(x)
5. CNF……. 1 marks
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 823dc1da9102

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/BTech_AI_7012/INTELLIGENT SYSTEMS/ANS_INTELLIGENT SYSTEMS(702AI0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Jul 2026
- Text: mixed (16 pages), mean OCR confidence 70.7

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: INTELLIGENT SYSTEMS
Date: 13 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. _1___ is compulsory
3. Out of remaining questions attempt any 4 Questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Figures in brackets on right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly   [20]
CO- 1;   a.   What is the Turing Test? Explain its significance and list the capabilities a   [5]
SO- 1;   machine must possess to pass the test.
BL-2
The Turing Test was proposed by Alan Turing in 1950 as a way to
determine whether a machine can exhibit intelligent behavior equivalent
to a human.
In this test:
• A human evaluator interacts with both a machine and a human
through text (no voice or visuals).
•   If the evaluator cannot reliably distinguish the machine from the
human, the machine is said to have passed the test.
Capabilities required to pass the test
• Natural Language Processing (NLP)
• To communicate successfully in English
• Knowledge Representation
• To store what it knows or hears
• Automated Reasoning
• To use stored information to answer questions and draw
conclusions
********** 1 **********
--- page 2 ---
• Machine Learning
• To adapt to new situations and detect patterns
CO-3 ;   b.   Identify the Performance, Environment, Actuators and Sensors for an AI-   [5]
SO- 1;   based recommendation system (eg: Netflix, Youtube).
BL-1,3
Performance Measure (P)
This defines how well the system is performing.
•   User satisfaction (likes, ratings, watch time)
•   Accuracy of recommendations
•   Click-through rate (CTR)
• Engagement (time spent on platform)
•   Retention rate (returning users)
Environment (E)
The environment in which the system operates.
•   Users with different preferences
•   Large database of movies/videos/content
•   User devices (mobile, TV, laptop)
• Network conditions
• Dynamic content (new uploads, trends)
Actuators (A)
How the system acts on the environment (outputs).
•   Displaying recommended movies/videos
•   Personalized home page feeds
•   Notifications (e.g., “Recommended for you”)
•   Auto-play suggestions
•   Ranking and ordering of content
Sensors (S)
How the system gathers information.
•   User watch history
•   Search queries
•   Likes, dislikes, ratings
•   Click behavior
• Time spent on content
•   Device/location data
CO-2 ;   c.   1. Define N queen problem. Consider the 4-Queen problem, where the [5]
SO- 1;   objective is to place 4 queens on a 4×4 chessboard such that no two
BL-3   queens attack each other. Using the backtracking algorithm, show step-
by-step how queens are placed on the board. Clearly indicate the
positions tried and rejected.
********** 2 **********
--- page 3 ---
CO - 4;   d.   Discuss the primary limitations of Propositional Logic in the context of   [5]
SO -1 ;   representing real-world knowledge.
BL- 2
Solution: Propositional Logic is useful for basic logical reasoning, but it
has several limitations when applied to real-world situations:
Limited Expressive Power (2 Mark)
Propositional logic cannot represent detailed relationships or internal
structure of statements.
• Example: It cannot express statements like “All girls are
intelligent” or “Some apples are sweet”.
•   It treats each statement as a whole without breaking it into
components.
Inability to Represent Quantifiers (1 Mark)
It cannot handle words like “all”, “some”, or “none”, which are
common in real-world knowledge.
• Example: Statements involving groups or quantities cannot be
properly expressed.
Limited Inference Capability (1 Mark)
It works only with binary truth values (True/False) and cannot perform
deeper logical reasoning involving relationships between objects.
Inability to Handle Uncertainty (1 Mark)
Propositional logic cannot represent uncertain or probabilistic
information.
********** 3 **********

[Text in pictures on this page, read by OCR]
4-Queen Problem using Backtracking (Step-by-Step)

Q Queen Placed (Safe) X_ Position Tried and Rejected (Not Safe) — Empty Position
1. Place Q in row 1 2. Try row 2 3. Try row 3

column I col 1 -+ Not safe (same column) col 1 + Not safe (column)
Try col 2 Not safe (diagonal) col 2 + Not safe (diagonal)
Try col 3+ Safe col 3 — Not safe (cotomn),
col 4 -+ Not safe (di )
1203 4 1203 4 ‘nie Yan on
ifa[-[-]- ifel-|[-]- ife]-|-|-

2{/-|-|-]- 2[x[x]e@|- 2[x]x]/aql- ce
3/-|-|-|- Se SBEE 3] x | x | x | x LE from (2,3) |
4/-|-|-[- af-[-[-]- af-|-|]-|- :
J
*

4. Backtrack to row 2 5. Try row 3

‘Try next column col 1 + Not safe

col 4 — Safe col 2 + Safe

1203 4 1203 4 A
ifel-]-|[- fej -[-|-
a[x]x][x]fe 2[|x|[x|[x]e
a{-|-]-|]- 3|x]Qq|-|-
«|-]-]-|- a{-|-[-|-

7. Backtrack to row 3 8. Try row 4

Try next column col 1 — Not safe

col 3 + Safe col 2 — Not safe

col 3 + Not safe
tity rae
1 -|-T-
= ife][-[-|[- oe
a[x|[x]xfe sitions of Queens:
— 71x1|x|x/a (1,1) (2,4) (3,3) (4,4)

Continue Search for Next Solution 1 | — | Q | — | — Solution Found — 2 Summary

—- 2/-|-|-Te 1 Total Solutions for 4-Queen = 2
——-— ee ‘+ Bockoracking mies positions,
ja (1,2) 24) (3,1) (4,3) pavers

bbocksracks to try alternatives.
--- page 4 ---
Example: It cannot express statements like “There is a 70% chance of
rain”.
Q2   a)   [10]
CO-2;
Consider the game tree shown in the figure, where the root node is a
SO-1;
BL-4   MAX node and the levels alternate between MIN and MAX nodes.
Assume that the nodes are evaluated from left to right using the
Alpha-Beta Pruning algorithm. Apply the Alpha-Beta Pruning
algorithm and determine the final optimal value at the root node.
Clearly show the intermediate α (alpha) and β (beta) values.
Evaluation of Left Subtree (2 Marks)
• Evaluates left MIN node → computes value from its children (4,
3, 6, 2).
•   Correctly determines MIN value = 4.
• Updates root: α = max(−∞, 4) = 4.
• Shows correct intermediate α, β updates.
•
Pruning in Left Subtree (1 Mark)
•   Identifies pruning condition: β ≤ α at MIN node.
•   Correctly prunes unnecessary branches (after value 4 is fixed).
•
Evaluation of Middle Subtree (2 Marks)
• Evaluates middle MIN node.
• Computes partial values and identifies β becomes ≤ α (4).
• Concludes MIN value = 2.
• Updates root: α = max(4, 2) = 4.
•
********** 4 **********
--- page 5 ---
Pruning in Middle Subtree (1 Mark)
•   Correctly identifies and marks pruned branches after cutoff
condition.
• Explains pruning using α ≥ β condition.
•
Evaluation of Right Subtree (2 Marks)
• Evaluates right MIN node with updated α = 4.
• Computes values (5, 4, 7, 5) and finds MIN value = 5.
• Updates root: α = max(4, 5) = 5.
•
Pruning in Right Subtree (1 Mark)
•   Identifies pruning when β ≤ α (last branch cut).
Optimal value at root (MAX) = 5 (1Marks)
CO-1;   b)   [10]
SO-1;
BL-1,2
Using A star Algorithm find the shortest path from source node A to G
Show step by step calculations for the same.
each step (3 marks)
final path (1 mark)
Q3   a)   Consider the crypt arithmetic problem shown below. Identify the [10]
CO-1;   variables, domains and constraints for this problem.
SO-1;   S O M E
BL-2   + T   I M E
********** 5 **********
--- page 6 ---
______________________
S P E N T
Initial state constraints:
• No two letters have the same value.
• The sums of the digits satisfy the predefined arithmetic rules.
Examine the domain for each variable at every step to evaluate possible
solutions for   { S,O,M,E,N,T,P,I}
Assigning Constraints (1 Mark)
• Each letter represents a unique digit (0–9).
• Leading digits (S, T) cannot be zero.
Column-wise Analysis – Units Place (1 Mark)
• From: E + E = T (mod 10)
• Determines value of T and carry C1.
Tens Place Analysis (1 Mark)
• From: M + M + C1 = N (mod 10)
• Finds N and carry C2.
Hundreds Place Analysis (1 Mark)
o   From: O + I + C2 = E (mod 10)
o   Determines relationship between O, I, E.
Thousands Place Analysis (2 Mark)
• From: S + T + C3 = P (mod 10)
• Computes P and carry.
Ten-Thousands Place (1 Mark)
• From: final carry gives S consistency
•   Validates that the result is a 5-digit number.
Correct Assignment of Digits (2 Marks)
•   Correct mapping obtained:
S = 1, O = 9, M = 3, E = 4, T = 8, I = 5, P = 0, N = 6
Verification of Solution (1 Mark)
•   Substitute values:
1934 + 8534 = 10468
• LHS = RHS verified.
********** 6 **********
--- page 7 ---
CO-2;   b)   i) Explain the major approaches to Artificial Intelligence: Thinking   [5]
Rationally, and Acting Rationally with suitable examples.
SO-1;
BL-2   Thinking Rationally:   [5]
This approach focuses on correct reasoning.
The idea is that an AI system should think logically and derive correct
conclusions using formal rules of logic.
• Based on principles from logic (e.g., syllogisms by Aristotle)
• Uses formal reasoning to reach conclusions
• Emphasis is on how the system thinks
Acting Rationally:
This approach focuses on doing the right action rather than how thinking
happens internally.
• An AI system is considered intelligent if it acts to achieve the best
outcome
• Based on the concept of a rational agent
ii) What is heuristic distance and explain Manhattan distance with
example.
Heuristic Distance
A heuristic distance is an estimate of the cost from a current node to
the goal node.
• Used in search algorithms like A*
•   Helps in making faster decisions
• Not always exact, but should be close to actual cost
(2.5 marks)
Manhattan Distance
The Manhattan distance is a heuristic used in grid-based problems
(like puzzles, pathfinding).
It calculates distance as:
Distance=∣x1−x2∣+∣y1−y2∣\text{Distance} = |x_1 - x_2| + |y_1 -
y_2|Distance=∣x1−x2∣+∣y1−y2∣…………….(2.5 marks)
********** 7 **********
--- page 8 ---
Q4   a)   Express the given statements using propositional logic with suitable   [10]
symbols. Also, using logical analysis, conclude whether the invigilator
CO – 4
was present or not. Observations:
SO – 1
BL- 3
•   If answer sheets are distributed, then students attempt the exam.
• The start of the exam ensures that answer sheets are distributed.
•   If the invigilator is not present, the exam cannot begin.
• When the invigilator is present, the exam begins.
•   It is observed that although the exam began, students did not
attempt the exam.
a) Propositional Logic Representation (5 Marks)
P: Invigilator is present
Q: Exam begins
R: Answer sheets are distributed
S: Students attempt the exam
The given statements can be written as:
Conclusion: The invigilator was present. …… 5 marks
CO- 4;   b)   i) Differentiate between proposition logic and predicate logic   [5]
SO-1 ;
BL- 2
[5]
I mark each point
********** 8 **********

[Text in pictures on this page, read by OCR]
From:
¢ Q- RandR > S,we get
Q = S (by transitivity / hypothetical syllogism)

But it is given that:
¢ QA 4S (exam began but students did not attempt)

This contradicts Q > S.
Now consider:

¢ AP + 7Q is logically equivalent to Q + P

Since Q is true, from Q — P, we get:

e Pistrue

Sr.No Propositional logic Predicate logic

1 Propositional logic is the logic that deals with a Predicate logic is an expression consisting of
collection of declarative statements which have variables with a specified domain. It consists of

a truth value, true or false. objects, relations and functions between the
objects.
2 It is the basic and most widely used logic. Also It is an extension of propositional logic covering
known as Boolean logic. predicates and quantification.

3 A proposition has a specific truth value, either A predicate’s truth value depends on the variables’
true or false. value.

4 Propositions are combined with Logical Predicate Logic adds by introducing quantifiers to
Operators or Logical Connectives like the existing proposition.
Negation(-), Disjunction(v), Conjunction(A),
Exclusive-OR(®),Implication(=),BiConditional
or Double Implication(=).

5 It cannot deal with sets of entities. It can deal with set of entities with the help of
quantifiers.
--- page 9 ---
ii) Explain any two inference rules used in propositional logic.
For each rule:
• Define the rule
• Write its symbolic representation
•   Illustrate with a suitable example
Solution:
Introduction to Inference Rules (1 mark)
Inference rules are logical patterns used to derive valid conclusions
from given premises in propositional logic. They ensure that the
reasoning process is correct.
Modus Ponens (2 marks)
Definition:
Modus Ponens is an inference rule where if a conditional statement and
its premise are true, then the conclusion is also true.
Symbolic Representation:
•   ( P →Q )
•   ( P )
• ∴ ( Q )
Example:
•   If a student studies, then they pass the exam. (P → Q)
• The student studies. (P)
• ∴ The student passes the exam. (Q)
Hypothetical Syllogism (2 marks)
Definition:
Hypothetical Syllogism states that if one statement implies a second,
and the second implies a third, then the first implies the third.
Symbolic Representation:
•   ( P → Q )
•   ( Q → R )
• ∴ ( P → R )
Example:
•   If it rains, the roads get wet. (P → Q)
•   If roads are wet, traffic slows down. (Q → R)
∴ If it rains, traffic slows down. (P → R)
********** 9 **********
--- page 10 ---
Q5   a)   Explain the Backtracking algorithm for solving Constraint Satisfaction [10]
Problems. Consider a map consisting of four regions: a, b, c, and d. Some
CO-3;
regions are adjacent to each other as shown in the given graph.
SO-1;
BL-3
The objective is to color each region such that:
• No two adjacent regions have the same color.
• Only the given three colors (R, G, B) are allowed.
• Each region must be assigned exactly one color.
Using the Backtracking algorithm. Construct the state space tree for the
coloring problem.
Solution:
Backtracking working [5M]
The Backtracking algorithm is a systematic search technique used to
solve Constraint Satisfaction Problems (CSPs) by building a solution
incrementally and abandoning (backtracking from) any   partial
assignment that violates constraints.
•   Variables: Elements that need to be assigned values (e.g., regions
in map coloring).
• Domains: Set of possible values for each variable (e.g., {R, G,
B}).
•   Constraints: Rules that restrict assignments (e.g., adjacent regions
cannot have the same color).
Working of Backtracking Algorithm:
1. Start with an empty assignment.
2. Select a variable that has not yet been assigned a value.
3. Assign a value from its domain.
4. Check constraints:
o   If the assignment is consistent, proceed to the next
variable.
o   If it violates constraints, reject the assignment.
5. Repeat the process until:
o All variables are assigned → Solution found, or
o No valid value is available → Backtrack to the previous
variable and try a different value.
When a conflict occurs, the algorithm goes back (backtracks) to the
previous step and tries another possible value.
Solution: 5 Marks
********** 10 **********
--- page 11 ---
CO - 4;   b)   i) Define Constraint Satisfaction Problem in AI. Identify Variables,   [5]
SO -1 ;   Domain, and Constraints
BL- 3
in Crossword Puzzle   [5]
Solution: [Def-1M, Identification-4M]
A Constraint Satisfaction Problem (CSP) in Artificial Intelligence is a
problem where a set of variables must be assigned values from their
respective domains such that all specified constraints are satisfied
simultaneously.
1. Variables:
• Each blank slot (across or down) in the crossword grid is a
variable.
• Example: X1, X2, X3 (represent different word positions in the
grid)
2. Domains:
• The domain of each variable is the set of words that can fit in
that slot.
• Words must match the length of the slot.
3. Constraints:
o Word length must match the slot length
o Intersecting words must have matching letters
o Example: If X1 and X2 intersect at a cell, then: Letter at that
position in X1 = Letter at that position in X2
********** 11 **********
--- page 12 ---
ii) Explain the Wumpus World as a problem-solving environment for
intelligent agents
Wumpus World is a classic AI problem-solving environment used to
test how an intelligent agent makes decisions using logic and reasoning
in an uncertain world. It is typically represented as a 4×4 grid.
……1
The environment consists of:
Agent – explores the world
Wumpus – dangerous monster
Pits – deadly holes
Gold – goal of the agent   ………….2
marks
The agent must find the gold and exit safely without falling into pits
or being killed by the Wumpus.
Percepts and Reasoning (…………………..1 Mark)
The agent cannot see the whole environment, so it depends on
percepts:
• Stench → Wumpus nearby
• Breeze → Pit nearby
•   Glitter → Gold present
Using these clues, the agent applies logical reasoning to make safe
decisions. The agent must: Build a knowledge base, Use inference rules
to deduce safe paths ,Plan actions to maximize reward and minimize
risk.
…… 1 marks
Q6   a) Explain the following types of AI agents in detail with diagram   [10]
mentioning their advantages and limitations.
CO-3;
SO-1;
1) Goal-Based Agent
BL-2
2) Utility-Based Agent
Goal Based Agent   (5 marks)
• The knowledge of the current state environment is not always
sufficient to decide for an agent to
********** 12 **********

[Text in pictures on this page, read by OCR]
(— >

Sensors +——}
‘
low the world evoh ‘What the world
eS a
[What my actions do

‘Whatit will be
like if I do action A
WhatactionI
Goals *|_ should do now

Actuators

\ Agent wy

Precepts

Action

LO)
--- page 13 ---
what to do.
• The agent needs to know its goal which describes desirable
situations.
•   Goal-based   agents expand the   capabilities   of
the   model-based agent by   having the   "goal"
information.
• They choose an action, so that they can achieve the goal.
•   These agents may have to consider a long sequence of
possible actions before deciding whether the goal is achieved or
not.
•   This agent is more flexible and the agent develops its
decision making skill by choosing the right from the various
options available
•   Such considerations of different scenarios are called
searching and planning, which makes an agent proactive.
✓ It focus only on reaching the goal set and hence the decision
took by the agent is based on how
Utility based Agent   (5 marks)
• These agents are similar to the goal-based agent but provide an
extra component of utility measurement which makes them
different by providing a measure of success at a given state.
•   Utility-based agent act based not only goals but also the best
way to achieve the
goal.
•   The Utility-based agent is useful when there are multiple
possible alternatives, and an agent has to choose in order to
perform the best action.
•   The utility function maps each state to a real number to
check how efficiently each action achieves the goals.
********** 13 **********
--- page 14 ---
CO-4;   b) Given a 3x3 board with 8 tiles (every tile has one number from 1 to 8) and   [10]
SO-1;
one empty space. The objective is to place the numbers on tiles in order
BL-2
using the empty space. We can slide four adjacent (left, right, above and
below) tiles into the empty space. Using Greedy best first search. Show the
step by step method to reach the goal state for the following initial state.
1   2   3
7   4   6
5   8
Initial State
1   2   3
4   5   6
7   8
Goal State
********** 14 **********
--- page 15 ---
Q7   a) Prove that the logical expression (P→Q) ∨ (Q→P) is always true for all   [10]
CO – 4   possible truth values of P and Q, i.e., show that it is a tautology.
SO – 1
Solution:
BL- 4
The last column contains only T's. Therefore, the formula is a
tautology. 3 marks
Writing all correct values for:
column (P→Q) - 2 marks
column (Q→P) - 2 marks
column (P→Q) ∨ (Q→P) - 3 marks
CO- 4;   b) Predicate Logic (FOL)   [10]
SO-1 ;
BL- 3
…….. 2 marks
1. Eliminate Implications
……….. 2 marks
2. Standardize Variables
Variables are already standardized and quantifiers are at the front — no
change needed   ….. 1mark
3. Skolemization
… 2
4. Drop Universal Quantifiers
********** 15 **********

[Text in pictures on this page, read by OCR]
. All people who are graduating are happy.
Va (Graduating(x) — Happy(z))

. All happy people smile.

Va (Happy(x) + Smile(x))

. Someone is graduating.

dz Graduating(xr)
--- page 16 ---
1. aGraduating(x) V Happy(x)
2. ~Happy(z) V Smile(z)

3. Graduating(a)
.... 2 marks

CNEF / Clause Form

{{-Graduating(z), Happy(z)}, {-Happy(z), Smile(z)}, {Graduating(a)} }

... | mark

FRR ICR 7 6 AC OH
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 8e94df546df8

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/MBATech_AI_7051/INTELLIGENT SYSTEMS/ANS_INTELLIGENT SYSTEMS(702AI0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Jul 2026
- Text: mixed (16 pages), mean OCR confidence 70.7

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: INTELLIGENT SYSTEMS
Date: 13 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. _1___ is compulsory
3. Out of remaining questions attempt any 4 Questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Figures in brackets on right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly   [20]
CO- 1;   a.   What is the Turing Test? Explain its significance and list the capabilities a   [5]
SO- 1;   machine must possess to pass the test.
BL-2
The Turing Test was proposed by Alan Turing in 1950 as a way to
determine whether a machine can exhibit intelligent behavior equivalent
to a human.
In this test:
• A human evaluator interacts with both a machine and a human
through text (no voice or visuals).
•   If the evaluator cannot reliably distinguish the machine from the
human, the machine is said to have passed the test.
Capabilities required to pass the test
• Natural Language Processing (NLP)
• To communicate successfully in English
• Knowledge Representation
• To store what it knows or hears
• Automated Reasoning
• To use stored information to answer questions and draw
conclusions
********** 1 **********
--- page 2 ---
• Machine Learning
• To adapt to new situations and detect patterns
CO-3 ;   b.   Identify the Performance, Environment, Actuators and Sensors for an AI-   [5]
SO- 1;   based recommendation system (eg: Netflix, Youtube).
BL-1,3
Performance Measure (P)
This defines how well the system is performing.
•   User satisfaction (likes, ratings, watch time)
•   Accuracy of recommendations
•   Click-through rate (CTR)
• Engagement (time spent on platform)
•   Retention rate (returning users)
Environment (E)
The environment in which the system operates.
•   Users with different preferences
•   Large database of movies/videos/content
•   User devices (mobile, TV, laptop)
• Network conditions
• Dynamic content (new uploads, trends)
Actuators (A)
How the system acts on the environment (outputs).
•   Displaying recommended movies/videos
•   Personalized home page feeds
•   Notifications (e.g., “Recommended for you”)
•   Auto-play suggestions
•   Ranking and ordering of content
Sensors (S)
How the system gathers information.
•   User watch history
•   Search queries
•   Likes, dislikes, ratings
•   Click behavior
• Time spent on content
•   Device/location data
CO-2 ;   c.   1. Define N queen problem. Consider the 4-Queen problem, where the [5]
SO- 1;   objective is to place 4 queens on a 4×4 chessboard such that no two
BL-3   queens attack each other. Using the backtracking algorithm, show step-
by-step how queens are placed on the board. Clearly indicate the
positions tried and rejected.
********** 2 **********
--- page 3 ---
CO - 4;   d.   Discuss the primary limitations of Propositional Logic in the context of   [5]
SO -1 ;   representing real-world knowledge.
BL- 2
Solution: Propositional Logic is useful for basic logical reasoning, but it
has several limitations when applied to real-world situations:
Limited Expressive Power (2 Mark)
Propositional logic cannot represent detailed relationships or internal
structure of statements.
• Example: It cannot express statements like “All girls are
intelligent” or “Some apples are sweet”.
•   It treats each statement as a whole without breaking it into
components.
Inability to Represent Quantifiers (1 Mark)
It cannot handle words like “all”, “some”, or “none”, which are
common in real-world knowledge.
• Example: Statements involving groups or quantities cannot be
properly expressed.
Limited Inference Capability (1 Mark)
It works only with binary truth values (True/False) and cannot perform
deeper logical reasoning involving relationships between objects.
Inability to Handle Uncertainty (1 Mark)
Propositional logic cannot represent uncertain or probabilistic
information.
********** 3 **********

[Text in pictures on this page, read by OCR]
4-Queen Problem using Backtracking (Step-by-Step)

Q Queen Placed (Safe) X_ Position Tried and Rejected (Not Safe) — Empty Position
1. Place Q in row 1 2. Try row 2 3. Try row 3

column I col 1 -+ Not safe (same column) col 1 + Not safe (column)
Try col 2 Not safe (diagonal) col 2 + Not safe (diagonal)
Try col 3+ Safe col 3 — Not safe (cotomn),
col 4 -+ Not safe (di )
1203 4 1203 4 ‘nie Yan on
ifa[-[-]- ifel-|[-]- ife]-|-|-

2{/-|-|-]- 2[x[x]e@|- 2[x]x]/aql- ce
3/-|-|-|- Se SBEE 3] x | x | x | x LE from (2,3) |
4/-|-|-[- af-[-[-]- af-|-|]-|- :
J
*

4. Backtrack to row 2 5. Try row 3

‘Try next column col 1 + Not safe

col 4 — Safe col 2 + Safe

1203 4 1203 4 A
ifel-]-|[- fej -[-|-
a[x]x][x]fe 2[|x|[x|[x]e
a{-|-]-|]- 3|x]Qq|-|-
«|-]-]-|- a{-|-[-|-

7. Backtrack to row 3 8. Try row 4

Try next column col 1 — Not safe

col 3 + Safe col 2 — Not safe

col 3 + Not safe
tity rae
1 -|-T-
= ife][-[-|[- oe
a[x|[x]xfe sitions of Queens:
— 71x1|x|x/a (1,1) (2,4) (3,3) (4,4)

Continue Search for Next Solution 1 | — | Q | — | — Solution Found — 2 Summary

—- 2/-|-|-Te 1 Total Solutions for 4-Queen = 2
——-— ee ‘+ Bockoracking mies positions,
ja (1,2) 24) (3,1) (4,3) pavers

bbocksracks to try alternatives.
--- page 4 ---
Example: It cannot express statements like “There is a 70% chance of
rain”.
Q2   a)   [10]
CO-2;
Consider the game tree shown in the figure, where the root node is a
SO-1;
BL-4   MAX node and the levels alternate between MIN and MAX nodes.
Assume that the nodes are evaluated from left to right using the
Alpha-Beta Pruning algorithm. Apply the Alpha-Beta Pruning
algorithm and determine the final optimal value at the root node.
Clearly show the intermediate α (alpha) and β (beta) values.
Evaluation of Left Subtree (2 Marks)
• Evaluates left MIN node → computes value from its children (4,
3, 6, 2).
•   Correctly determines MIN value = 4.
• Updates root: α = max(−∞, 4) = 4.
• Shows correct intermediate α, β updates.
•
Pruning in Left Subtree (1 Mark)
•   Identifies pruning condition: β ≤ α at MIN node.
•   Correctly prunes unnecessary branches (after value 4 is fixed).
•
Evaluation of Middle Subtree (2 Marks)
• Evaluates middle MIN node.
• Computes partial values and identifies β becomes ≤ α (4).
• Concludes MIN value = 2.
• Updates root: α = max(4, 2) = 4.
•
********** 4 **********
--- page 5 ---
Pruning in Middle Subtree (1 Mark)
•   Correctly identifies and marks pruned branches after cutoff
condition.
• Explains pruning using α ≥ β condition.
•
Evaluation of Right Subtree (2 Marks)
• Evaluates right MIN node with updated α = 4.
• Computes values (5, 4, 7, 5) and finds MIN value = 5.
• Updates root: α = max(4, 5) = 5.
•
Pruning in Right Subtree (1 Mark)
•   Identifies pruning when β ≤ α (last branch cut).
Optimal value at root (MAX) = 5 (1Marks)
CO-1;   b)   [10]
SO-1;
BL-1,2
Using A star Algorithm find the shortest path from source node A to G
Show step by step calculations for the same.
each step (3 marks)
final path (1 mark)
Q3   a)   Consider the crypt arithmetic problem shown below. Identify the [10]
CO-1;   variables, domains and constraints for this problem.
SO-1;   S O M E
BL-2   + T   I M E
********** 5 **********
--- page 6 ---
______________________
S P E N T
Initial state constraints:
• No two letters have the same value.
• The sums of the digits satisfy the predefined arithmetic rules.
Examine the domain for each variable at every step to evaluate possible
solutions for   { S,O,M,E,N,T,P,I}
Assigning Constraints (1 Mark)
• Each letter represents a unique digit (0–9).
• Leading digits (S, T) cannot be zero.
Column-wise Analysis – Units Place (1 Mark)
• From: E + E = T (mod 10)
• Determines value of T and carry C1.
Tens Place Analysis (1 Mark)
• From: M + M + C1 = N (mod 10)
• Finds N and carry C2.
Hundreds Place Analysis (1 Mark)
o   From: O + I + C2 = E (mod 10)
o   Determines relationship between O, I, E.
Thousands Place Analysis (2 Mark)
• From: S + T + C3 = P (mod 10)
• Computes P and carry.
Ten-Thousands Place (1 Mark)
• From: final carry gives S consistency
•   Validates that the result is a 5-digit number.
Correct Assignment of Digits (2 Marks)
•   Correct mapping obtained:
S = 1, O = 9, M = 3, E = 4, T = 8, I = 5, P = 0, N = 6
Verification of Solution (1 Mark)
•   Substitute values:
1934 + 8534 = 10468
• LHS = RHS verified.
********** 6 **********
--- page 7 ---
CO-2;   b)   i) Explain the major approaches to Artificial Intelligence: Thinking   [5]
Rationally, and Acting Rationally with suitable examples.
SO-1;
BL-2   Thinking Rationally:   [5]
This approach focuses on correct reasoning.
The idea is that an AI system should think logically and derive correct
conclusions using formal rules of logic.
• Based on principles from logic (e.g., syllogisms by Aristotle)
• Uses formal reasoning to reach conclusions
• Emphasis is on how the system thinks
Acting Rationally:
This approach focuses on doing the right action rather than how thinking
happens internally.
• An AI system is considered intelligent if it acts to achieve the best
outcome
• Based on the concept of a rational agent
ii) What is heuristic distance and explain Manhattan distance with
example.
Heuristic Distance
A heuristic distance is an estimate of the cost from a current node to
the goal node.
• Used in search algorithms like A*
•   Helps in making faster decisions
• Not always exact, but should be close to actual cost
(2.5 marks)
Manhattan Distance
The Manhattan distance is a heuristic used in grid-based problems
(like puzzles, pathfinding).
It calculates distance as:
Distance=∣x1−x2∣+∣y1−y2∣\text{Distance} = |x_1 - x_2| + |y_1 -
y_2|Distance=∣x1−x2∣+∣y1−y2∣…………….(2.5 marks)
********** 7 **********
--- page 8 ---
Q4   a)   Express the given statements using propositional logic with suitable   [10]
symbols. Also, using logical analysis, conclude whether the invigilator
CO – 4
was present or not. Observations:
SO – 1
BL- 3
•   If answer sheets are distributed, then students attempt the exam.
• The start of the exam ensures that answer sheets are distributed.
•   If the invigilator is not present, the exam cannot begin.
• When the invigilator is present, the exam begins.
•   It is observed that although the exam began, students did not
attempt the exam.
a) Propositional Logic Representation (5 Marks)
P: Invigilator is present
Q: Exam begins
R: Answer sheets are distributed
S: Students attempt the exam
The given statements can be written as:
Conclusion: The invigilator was present. …… 5 marks
CO- 4;   b)   i) Differentiate between proposition logic and predicate logic   [5]
SO-1 ;
BL- 2
[5]
I mark each point
********** 8 **********

[Text in pictures on this page, read by OCR]
From:
¢ Q- RandR > S,we get
Q = S (by transitivity / hypothetical syllogism)

But it is given that:
¢ QA 4S (exam began but students did not attempt)

This contradicts Q > S.
Now consider:

¢ AP + 7Q is logically equivalent to Q + P

Since Q is true, from Q — P, we get:

e Pistrue

Sr.No Propositional logic Predicate logic

1 Propositional logic is the logic that deals with a Predicate logic is an expression consisting of
collection of declarative statements which have variables with a specified domain. It consists of

a truth value, true or false. objects, relations and functions between the
objects.
2 It is the basic and most widely used logic. Also It is an extension of propositional logic covering
known as Boolean logic. predicates and quantification.

3 A proposition has a specific truth value, either A predicate’s truth value depends on the variables’
true or false. value.

4 Propositions are combined with Logical Predicate Logic adds by introducing quantifiers to
Operators or Logical Connectives like the existing proposition.
Negation(-), Disjunction(v), Conjunction(A),
Exclusive-OR(®),Implication(=),BiConditional
or Double Implication(=).

5 It cannot deal with sets of entities. It can deal with set of entities with the help of
quantifiers.
--- page 9 ---
ii) Explain any two inference rules used in propositional logic.
For each rule:
• Define the rule
• Write its symbolic representation
•   Illustrate with a suitable example
Solution:
Introduction to Inference Rules (1 mark)
Inference rules are logical patterns used to derive valid conclusions
from given premises in propositional logic. They ensure that the
reasoning process is correct.
Modus Ponens (2 marks)
Definition:
Modus Ponens is an inference rule where if a conditional statement and
its premise are true, then the conclusion is also true.
Symbolic Representation:
•   ( P →Q )
•   ( P )
• ∴ ( Q )
Example:
•   If a student studies, then they pass the exam. (P → Q)
• The student studies. (P)
• ∴ The student passes the exam. (Q)
Hypothetical Syllogism (2 marks)
Definition:
Hypothetical Syllogism states that if one statement implies a second,
and the second implies a third, then the first implies the third.
Symbolic Representation:
•   ( P → Q )
•   ( Q → R )
• ∴ ( P → R )
Example:
•   If it rains, the roads get wet. (P → Q)
•   If roads are wet, traffic slows down. (Q → R)
∴ If it rains, traffic slows down. (P → R)
********** 9 **********
--- page 10 ---
Q5   a)   Explain the Backtracking algorithm for solving Constraint Satisfaction [10]
Problems. Consider a map consisting of four regions: a, b, c, and d. Some
CO-3;
regions are adjacent to each other as shown in the given graph.
SO-1;
BL-3
The objective is to color each region such that:
• No two adjacent regions have the same color.
• Only the given three colors (R, G, B) are allowed.
• Each region must be assigned exactly one color.
Using the Backtracking algorithm. Construct the state space tree for the
coloring problem.
Solution:
Backtracking working [5M]
The Backtracking algorithm is a systematic search technique used to
solve Constraint Satisfaction Problems (CSPs) by building a solution
incrementally and abandoning (backtracking from) any   partial
assignment that violates constraints.
•   Variables: Elements that need to be assigned values (e.g., regions
in map coloring).
• Domains: Set of possible values for each variable (e.g., {R, G,
B}).
•   Constraints: Rules that restrict assignments (e.g., adjacent regions
cannot have the same color).
Working of Backtracking Algorithm:
1. Start with an empty assignment.
2. Select a variable that has not yet been assigned a value.
3. Assign a value from its domain.
4. Check constraints:
o   If the assignment is consistent, proceed to the next
variable.
o   If it violates constraints, reject the assignment.
5. Repeat the process until:
o All variables are assigned → Solution found, or
o No valid value is available → Backtrack to the previous
variable and try a different value.
When a conflict occurs, the algorithm goes back (backtracks) to the
previous step and tries another possible value.
Solution: 5 Marks
********** 10 **********
--- page 11 ---
CO - 4;   b)   i) Define Constraint Satisfaction Problem in AI. Identify Variables,   [5]
SO -1 ;   Domain, and Constraints
BL- 3
in Crossword Puzzle   [5]
Solution: [Def-1M, Identification-4M]
A Constraint Satisfaction Problem (CSP) in Artificial Intelligence is a
problem where a set of variables must be assigned values from their
respective domains such that all specified constraints are satisfied
simultaneously.
1. Variables:
• Each blank slot (across or down) in the crossword grid is a
variable.
• Example: X1, X2, X3 (represent different word positions in the
grid)
2. Domains:
• The domain of each variable is the set of words that can fit in
that slot.
• Words must match the length of the slot.
3. Constraints:
o Word length must match the slot length
o Intersecting words must have matching letters
o Example: If X1 and X2 intersect at a cell, then: Letter at that
position in X1 = Letter at that position in X2
********** 11 **********
--- page 12 ---
ii) Explain the Wumpus World as a problem-solving environment for
intelligent agents
Wumpus World is a classic AI problem-solving environment used to
test how an intelligent agent makes decisions using logic and reasoning
in an uncertain world. It is typically represented as a 4×4 grid.
……1
The environment consists of:
Agent – explores the world
Wumpus – dangerous monster
Pits – deadly holes
Gold – goal of the agent   ………….2
marks
The agent must find the gold and exit safely without falling into pits
or being killed by the Wumpus.
Percepts and Reasoning (…………………..1 Mark)
The agent cannot see the whole environment, so it depends on
percepts:
• Stench → Wumpus nearby
• Breeze → Pit nearby
•   Glitter → Gold present
Using these clues, the agent applies logical reasoning to make safe
decisions. The agent must: Build a knowledge base, Use inference rules
to deduce safe paths ,Plan actions to maximize reward and minimize
risk.
…… 1 marks
Q6   a) Explain the following types of AI agents in detail with diagram   [10]
mentioning their advantages and limitations.
CO-3;
SO-1;
1) Goal-Based Agent
BL-2
2) Utility-Based Agent
Goal Based Agent   (5 marks)
• The knowledge of the current state environment is not always
sufficient to decide for an agent to
********** 12 **********

[Text in pictures on this page, read by OCR]
(— >

Sensors +——}
‘
low the world evoh ‘What the world
eS a
[What my actions do

‘Whatit will be
like if I do action A
WhatactionI
Goals *|_ should do now

Actuators

\ Agent wy

Precepts

Action

LO)
--- page 13 ---
what to do.
• The agent needs to know its goal which describes desirable
situations.
•   Goal-based   agents expand the   capabilities   of
the   model-based agent by   having the   "goal"
information.
• They choose an action, so that they can achieve the goal.
•   These agents may have to consider a long sequence of
possible actions before deciding whether the goal is achieved or
not.
•   This agent is more flexible and the agent develops its
decision making skill by choosing the right from the various
options available
•   Such considerations of different scenarios are called
searching and planning, which makes an agent proactive.
✓ It focus only on reaching the goal set and hence the decision
took by the agent is based on how
Utility based Agent   (5 marks)
• These agents are similar to the goal-based agent but provide an
extra component of utility measurement which makes them
different by providing a measure of success at a given state.
•   Utility-based agent act based not only goals but also the best
way to achieve the
goal.
•   The Utility-based agent is useful when there are multiple
possible alternatives, and an agent has to choose in order to
perform the best action.
•   The utility function maps each state to a real number to
check how efficiently each action achieves the goals.
********** 13 **********
--- page 14 ---
CO-4;   b) Given a 3x3 board with 8 tiles (every tile has one number from 1 to 8) and   [10]
SO-1;
one empty space. The objective is to place the numbers on tiles in order
BL-2
using the empty space. We can slide four adjacent (left, right, above and
below) tiles into the empty space. Using Greedy best first search. Show the
step by step method to reach the goal state for the following initial state.
1   2   3
7   4   6
5   8
Initial State
1   2   3
4   5   6
7   8
Goal State
********** 14 **********
--- page 15 ---
Q7   a) Prove that the logical expression (P→Q) ∨ (Q→P) is always true for all   [10]
CO – 4   possible truth values of P and Q, i.e., show that it is a tautology.
SO – 1
Solution:
BL- 4
The last column contains only T's. Therefore, the formula is a
tautology. 3 marks
Writing all correct values for:
column (P→Q) - 2 marks
column (Q→P) - 2 marks
column (P→Q) ∨ (Q→P) - 3 marks
CO- 4;   b) Predicate Logic (FOL)   [10]
SO-1 ;
BL- 3
…….. 2 marks
1. Eliminate Implications
……….. 2 marks
2. Standardize Variables
Variables are already standardized and quantifiers are at the front — no
change needed   ….. 1mark
3. Skolemization
… 2
4. Drop Universal Quantifiers
********** 15 **********

[Text in pictures on this page, read by OCR]
. All people who are graduating are happy.
Va (Graduating(x) — Happy(z))

. All happy people smile.

Va (Happy(x) + Smile(x))

. Someone is graduating.

dz Graduating(xr)
--- page 16 ---
1. aGraduating(x) V Happy(x)
2. ~Happy(z) V Smile(z)

3. Graduating(a)
.... 2 marks

CNEF / Clause Form

{{-Graduating(z), Happy(z)}, {-Happy(z), Smile(z)}, {Graduating(a)} }

... | mark

FRR ICR 7 6 AC OH
````
