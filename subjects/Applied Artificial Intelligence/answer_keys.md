# Applied Artificial Intelligence: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 0994ae72e3a5

- Departments: Data Science
- Programmes: BTech DS 7009, Integrated DS 7038, MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_DS_7009/Applied Artificial Intelligence/ANS_Applied Artificial Intelligence(702DB0C019)_2025-2026.docx` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: mixed (7 pages), mean OCR confidence 79.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF   TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
|
Program:   B.Tech /MBA Tech/B Tech INTG
Stream:   Data Science
| Year: III ,V   Semester: V/IX

|
Subject: Applied Artificial Intelligence
| Time: 3 hrs (2:00 pm to 5:00 pm)
|
Date:
| No. of Pages: 09
|
Marks: 100
|
|
Final Examination Synoptic Solution
|
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
8) Assume Suitable data if necessary.

Q1
|
| Answer briefly:
| [20]
|
CO- 1,2; SO-2 ; BL-1
| a.
| What is Alpha-Beta Pruning? Define the alpha (α) and beta (β) values and explain the condition under which pruning occurs.
Alpha–beta pruning is a technique used in the minimax algorithm to reduce the number of nodes the algorithm evaluates in a game tree. It removes branches that cannot affect the final decision, which saves time without changing the outcome.
Alpha (α):
The best value that the maximizing player has found so far. It represents the lower bound of possible outcomes for the maximizer.
Beta (β):
The best value that the minimizing player has found so far. It represents the upper bound of possible outcomes for the minimizer.
Pruning condition:
Pruning happens when α ≥ β.
| [5]
|
CO-1 ; SO- 3;   BL-2
| b.
| What is the significance of knowledge representation? Mention the desirable properties of knowledge representation.
Significance of Knowledge Representation:
Enables a machine to store and utilize knowledge for reasoning and decision-making.
Helps in understanding, learning, and problem-solving like humans.
Allows communication between humans and intelligent systems.
Provides a basis for inference and deriving new knowledge.
Desirable Properties:
Representational Adequacy – Ability to represent all kinds of knowledge.
Inferential Adequacy – Ability to derive new facts from existing knowledge.
Inferential Efficiency – Supports efficient reasoning.
Acquisitional Efficiency – Easy to acquire and update knowledge.
| [5]
|
CO-3 ; SO- 2; BL-3
| c.
| In a class of 30 students, 18 like chocolate ice cream, 15 like vanilla ice cream, and 10 like both. What is the probability that a randomly chosen student likes chocolate ice cream given that they like vanilla ice cream?

| [5]
|
CO-4 ; SO-2 ; BL-2
| d.
| Backpropagation is the process used to train deep neural networks by adjusting their weights. It works by calculating the error at the output layer, then moving backward through the network to find how much each weight contributed to that error. Using this information, the weights are updated to reduce future errors. This repeated update helps the network learn patterns from data.
| [5]
|

|
|
|
|
Q2
CO-1; SO-2; BL-2
| a
| Compare and contrast the four basic types of intelligent agent programs — Simple Reflex Agents, Model-Based Reflex Agents, Goal-Based Agents, and Utility-Based Agents , highlighting their working principles, memory usage, decision-making capability, and performance.
Simple Reflex Agents: Act only on current percepts using condition–action rules; no internal memory; limited in dynamic environments.
Model-Based Reflex Agents: Maintain an internal model of the world to handle partially observable environments; can infer hidden aspects of the current state.
Goal-Based Agents: Use goals to decide which actions to take; involve search and planning to achieve specific objectives.
Utility-Based Agents: Choose actions based on a utility function that measures desirability; handle trade-offs between conflicting goals and optimize performance.
Comparison Focus:
Memory usage and world model
Ability to handle uncertainty
Decision-making sophistication
Flexibility and adaptability
Computational complexity

| [10]
|
Q2
CO-1,2,3; SO-2; BL-5
| b
| Explain A* algorithm with an example problem.
Consider the following graph with the given edge costs and heuristic values (h):
Start (S) → A (cost 2), B (cost 5)
A → C (cost 4), D (cost 6)
B → D (cost 3), E (cost 7)
C → Goal (G) (cost 5)
D → Goal (G) (cost 2)
E → Goal (G) (cost 1)
Heuristic values:
h(S)=7, h(A)=6, h(B)=4, h(C)=3, h(D)=2, h(E)=1, h(G)=0
I.Perform Greedy Best-First Search on the given graph starting from Start (S) and trace all the steps until the Goal (G) is reached.
II.Apply the A* Search algorithm on the same graph.
III.Identify which of the two algorithms finds the optimal solution and provide a brief justification for your answer.

| 4
3
3

|

|
| S A C G 11
|
|
Q3
CO-2,3;
SO-2;
BL-3,6
| a
| During an investigation, the following statements are made about a suspect:
If the suspect was in the city on the night of the crime, then he could not have been at home.
If the suspect was not at home, then he met his friend John.
If the suspect met John, then John knows about the crime.
John does not know about the crime.
Tasks:
(i) Represent each statement in propositional logic form using suitable symbols.
(ii) Using logical inference or a truth table, determine whether the suspect was in the city on the night of the crime.
(iii) Explain your reasoning clearly.

| [10]
|
Q3
CO-2,3;
SO-2;
BL-3,6
| b
| Define state-space search and explain its role in problem-solving using AI.
For the 9-tile puzzle, consider the following initial state and goal state as given below. Represent the problem as a state-space search and draw the state-space tree expanding until the goal state is reached. Clearly label each move of the blank. Assume cost of each action = 1. Find the total cost of the path from initial to goal.
Initial State:   Final State:

Cost =2
| 10
|

|
|
|
|
Q4
CO-2;
SO-2;
BL-6
| a
| Three boys A, B and C are throwing a ball to each other. A always throw the ball to B and B always throw the ball to C but C is as likely to throw the ball to B as to A.If the initial probability distribution of three states A,B and C is 0.3 ,0.4 and 0.3 respectively. Find
(i) Transition Matrix
(ii) P(X2 = B)
(iii) ) P(X3 = B,X2= C,X1= B,X0=A)=.15

| [10]

2

4

4

|
Q4
CO-2;
SO-2;
BL-6
| b
| Explain the role of probabilistic reasoning in AI using the concept of Bayesian Networks. Illustrate how a Bayesian Network can be used to model uncertainty in a real world scenario
Probabilistic reasoning in AI deals with reasoning under uncertainty. It allows AI systems to make reliable conclusions even when information is incomplete or noisy.
A Bayesian Network (BN) is a graphical model that represents a set of variables and their conditional dependencies using a directed acyclic graph (DAG). Each node represents a random variable, and edges represent probabilistic dependencies. The strength of these dependencies is quantified using conditional probability tables (CPTs).
Bayesian Networks use Bayes’ theorem to update beliefs about unknown events when new evidence is observed, enabling inference and prediction in uncertain situations.
Example (Real-world scenario):
Consider a medical diagnosis problem:
Nodes: Disease (D), Fever (F), Cough (C).
The BN models how Disease causes Fever and Cough.
If a patient shows Fever and Cough, the network can compute the probability of having the Disease using Bayes’ theorem:

Thus, a Bayesian Network helps in predicting and reasoning under uncertainty, supporting better decision-making in real-world AI applications.

| [10]
|

|
|
|
|
Q 5
CO-4;
SO-2;
BL-2
| a.
| "What is clustering in unsupervised learning? Explain the K-Means Clustering algorithm with its mathematical formulation. Discuss how centroids are updated and how the Elbow Method helps in determining the optimal number of clusters
Clustering is an unsupervised learning method where data points are grouped based on similarity. The goal is to form clusters so that points in the same cluster are alike, while points in different clusters are different.
K-Means Clustering:
K-Means divides the dataset into a fixed number of clusters, K. It works in two main steps:
Each data point is assigned to the nearest cluster center.
Each cluster center (centroid) is then recalculated based on the points assigned to it.
Centroid Update:
After assigning points, the centroid of each cluster is updated by taking the average position of all points in that cluster. The algorithm repeats these steps until the centroids stop changing much.
Elbow Method:
The Elbow Method helps decide how many clusters to use. It works by checking how the total variation inside clusters decreases as K increases. At a certain point, the improvement becomes small, forming an “elbow” in the graph. That K value is usually considered the best choice.

| [10]
|
Q5
CO-1,3;
SO-2;
BL-3
| b.
| Compare Local Search with Linear Programming
A farmer has a 125 acre farm. He produces radish, mutter and potato. Whatever he raises is fully sold. He gets Rs.5 per kg for radish, Rs.4 per kg for mutter and Rs.5 per kg for potato. The average yield per acre is 1500 kg for radish, 1800 kg for mutter and 1200 kg for potato. Cost of manure per acre is Rs.187.50, Rs.225 and Rs.187.50 for radish, mutter and potato respectively. Labour required per acre is 6 man-days each for radish and potato and 5 man-days for mutter. A total of 500 man-days of labour is available at the rate of Rs.40 per man-day. Formulate this as an LPP model to maximize the profit.
Decision variables: acreage for each produce:
Acres for radish, say r
Acres for mutter, say m
Acres for potato, say p

| [10]

3

7
|

|
|
|
|
Q6
CO-1,2;
SO-2;
BL-4,5
| a
| Illustrate the Hill Climbing algorithm through a suitable example. Explain how it works and highlight its key limitations.
Hill Climbing is a heuristic search algorithm used to find the optimal solution by iteratively moving towards the neighbour state with a higher value (better solution).
Working:
Start with an initial solution (state).
Evaluate all neighboring states.
Move to the neighbour with the highest value (improvement).
Repeat until no better neighbour exists.
| [10]
|
Q6
CO-2;
SO-2;
BL-6
| b
| Describe the steps involved in training and optimizing a neural network using feedforward and backpropagation. Discuss how these steps impact the network’s learning and performance.
1. Initialize weights and biases
The network starts with small random weights and biases. These act as the starting point for learning.
2. Feedforward pass
Input data moves through the network layer by layer.
Each neuron applies its weights, bias and activation function to produce an output.
The final layer produces the predicted value.
3. Compute the loss
The prediction is compared with the actual target using a loss function.
This gives a measure of how wrong the network’s output is.
4. Backpropagation of error
The loss is sent backward through the network.
The algorithm calculates how much each weight and bias contributed to the error.
5. Update weights and biases
Using an optimizer (like gradient descent), each weight is adjusted in the direction that reduces the loss.
This step improves the network’s performance for the next iteration.
6. Repeat for many epochs
Steps 2–5 are repeated on the full training data multiple times.
With every cycle, the network learns better representations and reduces its error.

| [10]
|

|
|
|
|
Q 7
CO-1,2,3,4; SO-2;
BL-4
| a
| Draw and explain the architecture of a CNN, covering convolutional layers, pooling layers, and fully connected layers
Convolutional Neural Network (CNN) Architecture:
Input Layer:
Receives the raw image (e.g., height × width × channels).
Convolutional Layers:
Apply filters/kernels to extract features like edges, textures, patterns.
Each filter produces a feature map.
Activation functions (like ReLU) introduce non-linearity.
Pooling Layers:
Reduce the spatial dimensions of feature maps (e.g., Max Pooling).
Helps reduce computation and control overfitting.
Fully Connected (FC) Layers:
Flatten feature maps into a vector and connect to neurons.
Perform classification or regression based on extracted features.
Output Layer:
Produces the final prediction (e.g., class probabilities with Softmax).

|

[10]

|
Q 7
CO-1,2,3,4; SO-2;
BL-4
| b
| Compare and contrast Supervised and Unsupervised Learning in terms of data requirements, algorithms, and typical applications.
Supervised Learning
Data Requirements: Uses labeled data (input–output pairs).
Algorithms: Linear Regression, Logistic Regression, Decision Tree, Random Forest, SVM, Neural Networks.
Functionality: Learns a mapping from inputs to known outputs.
Applications: Email spam detection, disease diagnosis, stock price prediction, image classification.
Unsupervised Learning
Data Requirements: Uses unlabeled data (only inputs).
Algorithms: K-Means Clustering, Hierarchical Clustering, PCA, Apriori, Autoencoders.
Functionality: Finds hidden patterns or structure in data.
Applications: Customer segmentation, anomaly detection, market basket analysis, dimensionality reduction.

| [10]
|
--- page 2 ---
Solution:

P(Chocolate and Vanilla)

P(Chocolate|Vanilla) = P(Vanilla)
anilla

e P(Chocolate and Vanilla) = i
* P(Vanilla) = 2 = 3

So:

10/30 10 2

P(Chocolate|Vanilla) = 15/30 ~ 15-3

~ 0.6667
--- page 3 ---
|. Greedy Best-First Search

Rule: Expand the node with the lowest heuristic value h(n). Ignore g(n).
Step 1: Start at S — children:

© A(h=6), B (h=4)

* Choose B (lowest h)

Step 2: Expand B — children:

* D(h=2), E (h=1)

* Frontier: Afh=6), D(h=2), E(h=1) — choose E (lowest h=1)
Step 3: Expand E — child:

* G{h=0)

* Frontier: Afh=6), D(h=2), G(h=0) — choose G

Path chosen by Greedy:

S-B-E-G

Total cost (g):
--- page 4 ---
A® path found:
S-A-[-G

Total cost (g): SA =2, A-D=6, (-s-j- 2 ahah = 16 @ optimal

ill. Comparison and Optimality

Algorithm Path chosen Total cost Optimal?

Greedy S38-E-G6 13 No

AY S+A-[-6 tl Yes
--- page 5 ---
(i) The required TPM is

0 1 0
P -| 0 O 1] & gq =[0.3,0.4,0.3]
1/2 1/2 0
--- page 6 ---
(i) P(X, = By= ??

la

| Means we need to find q2(B) | Hence, go = qyP*
p? = P.P | 0 0 1
=(0.3 0.4 0.3)}/0.5 0.5 O
: 3 0 05 05
=| 0 O 1]}) 0 0 1
11/2 1/2 Ojl1/2 1/2 0 =[0.20 0.35 0.45]
ol Thus,
=30.5 0.5 0
| 0 O05 0.5 P(X, = B) = 0.35
--- page 7 ---
Max Z = (5*1500 -187.5 — 6*40) r + (4*1800 — 225 - 5*40)m
+ (5*1200 — 187.5 — 6*40)p

Sub to: r+m+p<=125 (Land constraint)
6r + 5m + 6p <= 500 (Man-days constraint)
r,m,p>=0 (non-negativity)
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 93524fa397f0

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7057/Applied Artificial Intelligence/ANS_Applied Artificial Intelligence(702DB0C019)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Applied Artificial Intelligence
Date: 06 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right-hand side indicate full marks.
9. Assume Suitable data if necessary.
10. All code is to be deployed on Google Colab for creation and testing.
11. All coding question should also be submitted on answer book itself.
12. Internet is allowed during code implementation in google Colab only.
Q1
Answer briefly:
CO-1;   1.   Using PEAS Framework, analyze the design of an autonomous taxi system. Briefly explain how
SO-2;   each element and components contribute to the system’s effectiveness and decision-making.
BL-   Ans: The PEAS (Performance measure, Environment, Actuators, Sensors) framework is used to
define the interaction between an agent (automated taxi) and its environment. It helps in
designing intelligent agents by specifying what the agent needs to sense, how it should act, and
what determines its success.
1. Performance Measure: The success of an automated taxi depends on several factors,
including such as Safety, Comfort, Efficiency, Fuel/Energy Consumption, Customer Satisfaction
etc.
2. Environment: The automated taxi operates in a dynamic and uncertain environment, including
Roads, Traffic Conditions, Pedestrians and Cyclists, Weather Conditions etc.
3. Actuators: Actuators are the mechanisms through which the taxi interacts with the
environment. These include Steering system, Accelerator and Brake, Gear System, Indicators
and Headlights etc.
4. Sensors: Sensors collect information about the environment to help the taxi make intelligent
decisions. Key sensors include Cameras, LiDAR (Light Detection and Ranging), Radar, GPS
etc.
CO-1;   2.   Convert the following FOPL:
SO-1;   I.   All birds are fly.
BL-2   II.   Every man respects his parent.
III.   Not all students like both Mathematics and Science.
IV.   Some boys play cricket.
V.   Only one student failed in Mathematics.
********** 1 **********
--- page 2 ---
Ans:
1. ∀x(Bird(x)→Fly(x))
2. ∀x(Man(x)→Respects(x,Parent(x)))
3. ¬∀x(Student(x)→(Likes(x,Math)∧Likes(x,Science)))
4. ∃x(Boy(x)∧Plays(x,Cricket))
5. ∃x(Student(x)∧Failed(x,Math)∧∀y((Student(y)∧Failed(y,Math))→x=y))
CO-2;   3.   Briefly explain the difference between Random-Restart Hill Climbing over the Simple Hill Climbing
SO-1;   algorithm. Also, discuss its advantages and limitations
BL-2   Ans: Hill Climbing is a local search algorithm that starts from an initial state and iteratively
moves to a neighboring state with a higher value (better solution). The process continues until
no further improvement is possible. Whereas Random-Restart Hill Climbing is a variation in
which multiple hill-climbing searches are performed from different random starting points. If one
search gets stuck in a local optimum, another search from a different starting point might find a
better solution.
Advantages of Random-Restart Hill Climbing:
•   Avoids Local Optima: Since the search is restarted from different points, it increases the
chances of finding a global optimum.
•   Efficient for Complex Search Spaces: Works well when the problem has multiple peaks
(local maxima).
•   Simple to Implement: Only requires modifying the starting point selection.
Limitations of Random-Restart Hill Climbing:
•   Computationally Expensive: Multiple restarts increase processing time.
• Does Not Guarantee Global Optimum: Although it improves the chances, it may still not
find the best solution.
********** 2 **********
--- page 3 ---
CO-2;   4.   Explain the differences between L1 Regularization and L2 Regularization, and discuss how each
SO-1;   technique affects model performance, including aspects such as overfitting, feature selection, and
BL-2   generalization ability.
Ans: Regularization is a technique used to prevent overfitting in machine learning models by
adding a penalty to the loss function.
1. L1 Regularization (Lasso Regression): L1 regularization adds the absolute value of
coefficients as a penalty term:
•   Encourages sparsity by setting some coefficients to zero (feature selection).
•   Helps in selecting the most important features and ignoring irrelevant ones.
•   Useful when the dataset has many irrelevant features.
2. L2 Regularization (Ridge Regression): L2 regularization adds the squared value of
coefficients as a penalty term:
• Does not set coefficients to zero but shrinks them closer to zero.
• Reduces the impact of less significant features rather than removing them.
•   Useful when all features contribute to the prediction.
Impact on Model Performance:
Feature   L1 Regularization   L2 Regularization
Feature   Yes (eliminates irrelevant
No (retains all features)
Selection   features)
Model   Prevents large weights but
Reduces complexity
Complexity   keeps all features
Overfitting   Helps by removing   Helps by penalizing large
Reduction   unimportant features   weights
When feature selection is When all features are
Suitability
needed   important
Q2   1)   Define a Rational Agent, and explain how an Intelligent Agent demonstrates intelligence
CO-1;   through its actions and decision-making processes?
SO-1;   Ans: A rational agent is an AI-based system that takes actions to maximize its performance
BL-1   based on available knowledge and the environment. It always chooses the best possible action
given what it knows. A rational agent should:
-   Act optimally to achieve its goal.
-   Choose actions that yield the maximum expected performance.
-   Adapt to different environments based on feedback.
Example of a Rational Agent: A self-driving car is an example of the rational agent. Its
component can be described as
-   Senses the road (using cameras, Lidar, GPS).
-   Follows traffic rules.
-   Avoids obstacles and optimizes fuel efficiency.
-   Adapts to weather conditions for safe driving.
An intelligent agent exhibits intelligence by perceiving its environment and acting in a way
that improves its goal-oriented behavior. It does this using five key capabilities:
1. Perception: The agent senses data from the environment using sensors (e.g., cameras,
Lidar, temperature sensors). Example: A smart home assistant listens to voice
commands and recognizes them.
2. Learning: An agent learns from past experiences and adapts its behavior using
Machine Learning (ML) and AI algorithms. Example: A spam filter learns which
emails to block over time.
********** 3 **********
--- page 4 ---
3. Decision-Making: The agent analyzes possible actions and selects the best one using
logic, heuristics, or probability models. Example: Chess AI calculates millions of
possible moves and picks the best one.
4. Problem Solving: The agent searches for solutions using techniques like Uninformed
Search (DFS, BFS) and *Informed Search (A, Greedy Search)**. Example: Google
Maps finds the shortest route using A* search.
5. Acting: Once a decision is made, the agent performs the required action using
actuators. Example: A robot vacuum cleaner moves and cleans based on dirt detection.
2)   Is it possible that adversarial search algorithm can applicable to solve the chess game?
Discuss steps of the algorithm for solving this problem and role of the alpha and beta
pruning.
Ans: Yes, Chess is a classic example of a two-player, zero-sum game, making it ideal
for adversarial search in Artificial Intelligence.
One player’s gain = other player’s loss
Players: MAX (AI) vs MIN (opponent)
Steps of Minimax in Chess
Represent the Game as a Tree
• Each node = board configuration
• Each edge = legal move
Generate Possible Moves
• From current position, generate all legal moves
• Expand to a certain depth (limited due to complexity)
Evaluate Leaf Nodes
• Use an evaluation function (heuristic), e.g.:
o Material value (queen = 9, rook = 5, etc.)
o Board control
o King safety
4️ Backpropagation
• Apply Minimax rule:
o MAX chooses highest value
o MIN chooses lowest value
Choose Optimal Move
•   Select move leading to best evaluated outcome
Problem with Plain Minimax
• Chess has huge search space (~10^120 possibilities)
•   Full tree search is impossible
•   Requires optimization
Alpha-Beta pruning is an optimization technique that eliminates branches that
cannot affect the final decision.
• Alpha (α) → Best value MAX can guarantee so far
********** 4 **********
--- page 5 ---
• Beta (β) → Best value MIN can guarantee so far
While exploring: If α ≥ β, stop exploring that branch
•   That branch cannot influence the final decision
Reduces number of nodes explored
Makes deeper search possible
Improves efficiency significantly
If MAX already has a move with value = 5:
• While exploring another branch, MIN finds option ≤ 5
•   That branch is useless → prune it
Benefits of Alpha-Beta Pruning
• Same result as Minimax (no loss in accuracy)
• Much faster
•   Enables real-time decision-making in chess
Q3   1)   1. John likes all kind of food.
CO-1,2;   2. Apple and vegetable are food
SO-1;   3. Anything anyone eats and not killed is food.
BL-3,2   4. Anil eats peanuts and still alive
5. Harry eats everything that Anil eats.
Prove by resolution that: John likes peanuts.
Ans: Step 1: Convert the Given Statements into First-Order Predicate Logic (FOPL)
Step 2: Convert Statements into Clause Form (Skolemization and CNF Conversion)
********** 5 **********
--- page 6 ---
Step 3: Perform Resolution to Derive Likes(John, Peanuts)
Step 3.1: Use Eats(Anil, Peanuts) and General Food Rule
Step 3.2: Use Food(Peanuts) and John’s Liking Rule
By using resolution refutation, we have successfully proven that John likes peanuts.
Or
Resolution Graph
********** 6 **********

[Text in pictures on this page, read by OCR]
Step 2.1: Eliminate Implications
¢ Convert A + Binto“AV B
1. John likes all kinds of food:
aFood(x) V Likes(John, x)
2. Apple and vegetable are food (already in CNF):
Food( Apple)
Food(V egetable)

3. Anything anyone eats and is not killed is food:

aEats(y, x) V Killed(y) V Food(z)

4. Anil eats peanuts and is still alive (already in CNF):
Eats( Anil, Peanuts)
=Killed( Anil)

5. Harry eats everything that Anil eats:

=Eats(Anil,x) V Eats(Harry, x)
--- page 7 ---
Explain the Markov assumption in probabilistic modeling and analyze its significance in
2)   simplifying dependency structures?
Ans: The Markov Assumption states that the probability of a future state only depends on the
present state and is independent of past states. In mathematical terms, if we have a sequence of
states S1, S2,..., Sn the Markov Assumption can be written as:
This means that the next state Sn depends only on the current state Sn−1 and not on the previous
history. The Markov Assumption is crucial because it simplifies complex probabilistic models by
reducing dependencies. Some of its key applications include:
1. Simplifies Computation in Sequential Processes
-   Instead of storing and processing the entire history, only the current state needs
to be considered, making calculations much more efficient.
2. Used in Markov Chains
-   Markov Chains model systems where transitions occur based on a fixed
probability distribution, such as weather prediction, stock market trends, and
speech recognition.
3. Foundation of Hidden Markov Models (HMMs)
- HMMs use the Markov Assumption to model sequences where states are not
directly observable but inferred through emitted observations (e.g., speech
processing, bioinformatics).
4. Applicable in Reinforcement Learning (RL)
- Many RL algorithms, such as Markov Decision Processes (MDPs), rely on the
Markov Assumption to model agent-environment interactions.
Markov Process for Simplifies Computation:
1. Reduces State Dependencies
-   Instead of considering entire past histories, we only need to store the current
state.
2. Transition Probabilities Become Manageable
-   Since the probability of moving to the next state only depends on the current
state, we can use a simple transition probability matrix P(i,j), where:
3. Enables Efficient Predictions
-   Given an initial state distribution and transition probabilities, predicting future
states becomes straightforward.
********** 7 **********
--- page 8 ---
A Hidden Markov Model (HMM) is an extension of Markov Chains where the actual state is
hidden and only an observed output (or emission) is available.
1. Decouples Past History from Future Predictions
-   The hidden state at time t depends only on the previous state t−1, making state
estimation computationally feasible.
2. Simplifies Probability Computations
-   The probability of an observation sequence O1, O2,...,On given the hidden states
S1, S2,..., Sn follows:
-
-   This factorization significantly reduces the number of probability terms to
compute.
3. Enables Efficient Inference using the Viterbi Algorithm
-   By assuming that each state depends only on the previous state, the Viterbi
algorithm efficiently finds the most probable sequence of hidden states.
Q4   1)   Explain how the Backtracking Search algorithm can be used to solve the 4-Queens problem.
CO-2,3;   Construct the corresponding state space tree and describe the step-by-step execution.
SO-6;   Ans: The 4-Queens Problem is a classic CSP where we need to place four queens on a 4×4
BL-3,2   chessboard such that No two queens attack each other and Queens should not be placed in the
same row, column, or diagonal. Other side, Backtracking is a recursive, depth-first search
approach used for CSPs. It attempts to place a queen in a column and checks for constraints. If
a conflict arises, it backtracks to the previous step and tries another position.
Steps of Backtracking Algorithm:
1. Start placing queens column-wise from the leftmost column.
2. Try placing a queen in a row that does not conflict with previous queens.
3.   If no row is valid, backtrack to the previous column and try a different row.
4.   If a queen is placed in the last column successfully, a solution is found.
5. Repeat until all possible solutions are explored.
State Space Tree Using Backtracking
2)   Explain the fundamental architecture of an Artificial Neural Network (ANN) with a suitable
diagram. Additionally, discuss the role and types of activation functions used in ANN and deep
learning.
Ans: An Artificial Neural Network (ANN) is a computational model inspired by the human brain. It
consists of interconnected processing units called neurons, which are arranged in layers. ANNs
are widely used in
********** 8 **********
--- page 9 ---
machine learning, pattern recognition, and deep learning applications. An ANN consists of three
main layers:
Input Layer: This layer receives raw data as input. Each neuron in the input layer represents a
feature from the dataset. No computation is performed here—data is simply passed to the next
layer.
Hidden Layer(s): This is where most computations take place. Each neuron in a hidden layer receives
weighted inputs, applies an activation function, and passes the result to the next layer. The number of
hidden layers and neurons can vary based on the complexity of the problem.
Output Layer: Produces the final output of the network.
Apart from above the weight and bias also having important role in ANN which are described below.
Weights and Biases: the weight and bias are the important parameter of the ANN. Weights determine
the importance of each input. Biases allow the model to shift the activation function to improve learning.
Weights and biases are updated using backpropagation during training.
In classification tasks, it often uses Softmax or Sigmoid activation to generate probabilities. In regression
tasks, it may use a linear activation function. Whereas, deep learning algorithm utilizes the Tanh
(Hyperbolic Tangent), ReLU (Rectified Linear Unit) and Leaky ReLU funtions.
Q5   1)   Using Data provided, Build Classification Models Binary Logistic Regression & MLP Classifier.
CO-3,2;   Also Explain the feature representation and model design.
SO-1;   Ans: Check the code.
BL-6   Suppose, given a dataset containing information about real estate properties, including various
2)   attributes that influence property prices. The dataset consists of the following features such as No,
X1 transaction date, X2 house age, X3 distance to the nearest MRT station, X4 number of
convenience stores, X5 latitude, X6 longitude, Y house price of unit area. Build a machine learning
model to predict the house price per unit area (Y) based on the given input features.
Ans: Check the code.
Q6   1)   Explain the importance of Bayesian Networks in probabilistic modeling and describe their
CO-2;   key components. Construct a Bayesian Network diagram to represent relationships
SO-2;   among variables in a real-world scenario.
BL-2   Ans: Bayesian Network (BN) is a graphical probabilistic model that represents a set of variables
and their conditional dependencies using a Directed Acyclic Graph (DAG). It is widely used in
uncertainty modelling, decision-making, and machine learning applications. BNs help model
real-world problems where uncertainty exists (e.g., medical diagnosis, weather prediction). It
uses probability distributions to handle incomplete or noisy data. BNs also enables reasoning
under uncertainty by calculating the posterior probability of events using Bayes’ Theorem.
Example: In medical diagnosis, given symptoms, BNs compute the probability of a disease.
Graphical Representation of Dependencies:
Components of a Bayesian Network
A Bayesian Network consists of the following three main components:
Nodes (Variables):
-   Represent random variables (e.g., Disease, Symptoms, Test Results).
- Each node has a probability distribution
Edges (Directed Arrows).
********** 9 **********
--- page 10 ---
-   It represents conditional dependencies between variables.
-   If there is an edge from A → B, then A influences B.
Conditional Probability Tables (CPTs):
-   Each node has a CPT defining the probability distribution given its parents
In the above diagram, A, B, C, and D nodes are random variables represented by the nodes
of the network graph. If we are considering node B, which is connected with node A by a
directed arrow, then node A is called the parent of Node B. Node C is independent of node
A.
Real life Example:
Consider a Medical Diagnosis System for detecting whether a patient has the flu based on
symptoms and external factors.
Variables:
Flu (F): Whether the patient has the flu.
Fever (Fe): Presence of fever (depends on Flu).
Cough (C): Presence of cough (depends on Flu).
Cold Weather (W): Whether it is cold outside (independent factor).
Sore Throat (S): Presence of sore throat (depends on Flu and Cough).
BN Diagram
2)   Describe k-means clustering in details and solve the below mentioned toy example using
the k-means algorithm. The dataset contains the following points P1(2, 10), P2(2, 5), P3(8,
4), P4(5, 8), P5(7, 5) and P6(6, 4), number of clusters (k = 2) and consider Euclidean
distance as the similarity measure. The initial centroids for the dataset are (2,10) and
(8,4).
Ans: K-Means is an unsupervised machine learning algorithm used for partitioning a dataset into K
clusters based on similarity. It minimizes the variance within clusters while maximizing the difference
between them. K-Means minimizes the Sum of Squared Errors (SSE), also known as within-cluster
variance and objective function of the algorithm. The task of this function is to minimize this function,
ensuring tight clusters. The steps of the K-Means Algorithm is mentioned below.
-   Initialize K Centroids: Randomly select K points as initial cluster centers.
-   Assign Data Points to the Nearest Centroid: Compute the Euclidean distance between each
point and all centroids, then assign the point to the closest centroid.
-   Recalculate Centroids: Compute the mean of all points in each cluster to update the
centroid.
********** 10 **********
--- page 11 ---
-   Repeat Steps 2 and 3 until centroids no longer change or the maximum number of iterations
is reached
Q7   1)   Explain the concept of arc consistency in Constraint Satisfaction Problems (CSPs). Describe the
CO-2,1;   AC-3 algorithm in detail and demonstrate its application using a simple example such as the 8-
SO-1;   puzzle problem.
BL-2   Ans: A Constraint Satisfaction Problem (CSP) consists of:
- A set of variables (X1, X2, ..., Xn)
- A set of domains (possible values for each variable)
- A set of constraints (rules that define valid variable assignments)
Arc Consistency is a property of binary CSPs where for every variable X and Y connected by a
constraint, every value of X has a corresponding value in Y that satisfies the constraint. If any value
of X does not have a valid corresponding value in Y, it is removed from the domain of X. A CSP is
arc consistent if all arcs in the constraint graph satisfy this property. The AC-3 (Arc Consistency 3)
algorithm is used to enforce arc consistency in a CSP. It systematically removes values from
variable domains that violate constraints.
Steps of AC-3 Algorithm:
-   Initialize a queue with all arcs (Xi, Xj) from the CSP.
-   While the queue is not empty:
o Remove an arc (Xi, Xj) from the queue.
o Check if any value in the domain of Xi has no corresponding value in Xj that
satisfies the constraint.
o   If such a value exists, remove it from the domain of Xi.
o   If the domain of Xi is modified, add all arcs (Xk, Xi) back to the queue.
-   Repeat until no more values are removed.
Maze Problem Using AC-3: Setup: Consider a simple 3x3 maze, where each cell is a variable (X1,
X2, ..., X9) with possible values {0, 1}, where, 0 represents an empty path and 1 represents a wall.
Constraints ensure that a valid path is formed from the start to the goal.
Constraint Graph: Each cell is connected to its adjacent (left, right, top, bottom) cells, forming
constraints that enforce: A valid path must be continuous. Walls (1) cannot be part of the solution.
Compare and contrast the informed search and uniformed search.
2)   Ans: The search algorithms in Artificial Intelligence (AI) can be classified into Informed Search and
Uninformed Search based on the information they use to navigate the search space.
Uninformed Search also known as Blind Search. It can search the solution without any additional
information beyond the problem definition (i.e., initial state, goal state, and possible actions). It does not
use heuristics to guide the search.
Informed Search (Heuristic Search): This search utilizes the problem-specific knowledge (heuristics) to
find solutions more efficiently. Heuristics help estimate how close a state is to the goal, reducing
unnecessary exploration.
Feature   Uninformed Search   Informed Search
Use of Heuristics   No heuristics used.   Uses heuristics to improve
efficiency.
Efficiency   Explores blindly, leading to high More efficient as it prioritizes
time and space complexity.   promising paths.
Optimality   Some algorithms (BFS, UCS)   A* search is optimal if heuristics
guarantee optimality.   are admissible.
Completeness   BFS and UCS are complete,   A* is complete if heuristics are
DFS is not always.   consistent.
Time Complexity   High because it explores the   Lower compared to uninformed
entire tree/graph.   search if heuristics are good.
Examples   BFS, DFS, UCS, IDDFS,   A*, Greedy Best-First Search,
Bidirectional Search.   Hill Climbing, Simulated
Annealing.
********** 11 **********
--- page 12 ---
Explain the conjunctive normal form and illustrate the various steps to convert the sentence into
3)   CNF.
Ans: Conjunctive Normal Form (CNF) is a standard form of a logical expression where a formula is
represented as a conjunction (AND operation) of disjunctions (OR operations) of literals. A literal is
either a variable or its negation. A formula in CNF follows the structure:
where each clause (expression within parentheses) is a disjunction of literals, and the entire formula
is a conjunction of such clauses.
Steps to Convert a Sentence into CNF
To convert a given logical sentence into CNF, follow these steps:
1. Express the statement in propositional logic.
2. Eliminate implications.
3. Move negations inward using De Morgan's laws.
4.   Distribute disjunctions over conjunctions using distributive laws.
5. Ensure the final form is a conjunction of disjunctions.
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper a3d08e68c96c

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7057/Applied Artificial Intelligence/ANS_Applied Artificial Intelligence(702DB0C019)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Applied Artificial Intelligence
Date: 02 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right-hand side indicate full marks.
9. Assume Suitable data if necessary.
10. All code is to be deployed on Google Colab for creation and testing.
11. All coding question should also be submitted on answer book itself.
12. Internet is allowed during code implementation in google Colab only.
1.
1. Explain the differences between informed search and uninformed search in Artificial Intelligence, including
their principles, advantages, limitations, and typical use cases with examples?
Answer:
1. Feature Uninformed Search Informed Search
Knowledge No extra knowledge Uses heuristic knowledge
Efficiency Less efficient   More efficient
Speed   Slower   Faster
Complexity High   Reduced (with good heuristic)
Examples BFS, DFS   A*, Greedy
1.2
Translate the following statement into Second Order Logic:
“There exists a property that is true for all elements in a domain.”
Also briefly explain how Second Order Logic differs from First Order Logic.
Answer:
1. Correct Second Order Logic translation – 2 marks
∃𝑃  ∀𝑥  𝑃(𝑥)
2. Explanation of the formula – 1 mark
(Explaining that a property holds for all elements)
********** 1 **********
--- page 2 ---
3. Definition of Second Order Logic – 1 mark
(Quantifies over properties/relations)
4. Difference from First Order Logic – 1 mark
(FOL quantifies only over individuals)
1.3
Explain the Arc Consistency concept in Constraint Satisfaction Problems and describe the AC-3 in detail with an
illustrative example?
Answer:
Arc Consistency (AC-3) Algorithm is used in Constraint Satisfaction Problems (CSPs) to reduce domains of
variables by enforcing consistency between pairs of variables (arcs). Marks 1
An arc (𝑋, 𝑌)is consistent if for every value in 𝑋, there exists a compatible value in 𝑌satisfying the constraint.
AC-3 Algorithm: Marks 3
•   Start with a queue of all arcs
•   Repeatedly remove an arc (𝑋, 𝑌)
• Remove values from domain of 𝑋that have no supporting value in 𝑌
•   If domain of 𝑋changes, add all neighboring arcs back to queue
•   Continue until queue is empty
Result: Reduces search space and helps detect inconsistency early. Marks 1
1.4
Explain the concept of Reinforcement Learning in Artificial Intelligence suitable with examples?
Answer:
Reinforcement Learning (RL) is a type of machine learning where an agent learns by interacting with an
environment and improves its behavior through rewards and penalties.
The agent takes actions in different states and receives feedback in the form of rewards. The objective is to
maximize cumulative reward over time.
Key elements include:
• Agent (learner/decision maker)
• Environment (where agent operates)
•   State, Action, Reward
•   Policy (strategy followed by agent)
Common methods include Q-Learning and Policy Learning.
Application: Robotics, game playing, recommendation systems.
Marks Mapping (5 Marks)
1. Definition of Reinforcement Learning – 1 mark
2. Concept (agent, environment, reward) – 1 mark
3. Working principle (interaction & learning process) – 2 marks
4. Applications / examples – 1 mark
********** 2 **********
--- page 3 ---
2.1 Explain the PEAS framework used in Artificial Intelligence for designing intelligent agents with suitable
examples and applications.
Answer:
PEAS Framework is used in Artificial Intelligence to define the task environment of an intelligent agent. It helps
in designing agents by specifying what they should do and how their performance is evaluated.
PEAS stands for:
• P – Performance Measure: Criteria to evaluate agent’s success
• E – Environment: The surroundings in which the agent operates
• A – Actuators: Actions the agent can perform
• S – Sensors: Inputs the agent receives from the environment
Example (Self-driving car):
•   Performance: Safety, speed, comfort
•   Environment: Roads, traffic, pedestrians
•   Actuators: Steering, brakes, accelerator
•   Sensors: Cameras, GPS, radar
Use: Helps in clearly defining problems and designing intelligent agents effectively.
Marks Mapping (10 Marks)
1. Definition of PEAS Framework – 2 marks
2. Expansion of PEAS (P, E, A, S) – 2 marks
3. Explanation of each component – 4 marks
o Performance (1)
o Environment (1)
o Actuators (1)
o Sensors (1)
4. Example (e.g., self-driving car) – 1 mark
5. Application/importance – 1 mark
2.2 Explain adversarial search in Artificial Intelligence, and describe the Minimax algorithm in detail with
suitable examples?
Answer:
Adversarial Search is used in environments where multiple agents compete, such as games. The Minimax
Algorithm is a decision-making strategy used in two-player zero-sum games (e.g., Tic-Tac-Toe, Chess), where
one player tries to maximize gain while the opponent tries to minimize it.
Working Principle:
• The game is represented as a game tree
•   Players alternate turns:
o MAX player: chooses the move with maximum value
o MIN player: chooses the move with minimum value
********** 3 **********
--- page 4 ---
• The algorithm explores all possible moves up to terminal states
•   Utility values are assigned to terminal nodes
•   Values are propagated upward:
o MAX selects highest value
o MIN selects lowest value
Result: The optimal move is chosen assuming the opponent also plays optimally.
Limitation: High time complexity (exponential), improved using Alpha-Beta Pruning.
Marks Mapping (10 Marks)
1. Definition of Adversarial Search – 2 marks
2. Definition of Minimax Algorithm – 2 marks
3. Working principle (game tree, MAX & MIN roles) – 3 marks
4. Utility values & backtracking concept – 1 mark
5. Applications (games like Chess, Tic-Tac-Toe) – 1 mark
6. Limitation / improvement (Alpha-Beta pruning) – 1 mark
3.1 Consider the following statements:
All employees who work hard get promoted.
Some employees are careless.
Careless employees do not work hard.
Tasks:
Translate the above statements into First Order Logic.
Using logical inference or resolution, prove that some employees do not get promoted
Answer:
Step 1: Predicate Definitions
Let:
• 𝐸𝑚𝑝𝑙𝑜𝑦𝑒𝑒(𝑥): x is an employee
• 𝑊𝑜𝑟𝑘𝐻𝑎𝑟𝑑(𝑥): x works hard
• 𝑃𝑟𝑜𝑚𝑜𝑡𝑒𝑑(𝑥): x is promoted
•   𝐶𝑎𝑟𝑒𝑙𝑒𝑠𝑠(𝑥): x is careless
Step 2: Translation into First Order Logic
1. All employees who work hard get promoted:
∀𝑥  [(𝐸𝑚𝑝𝑙𝑜𝑦𝑒𝑒(𝑥) ∧𝑊𝑜𝑟𝑘𝐻𝑎𝑟𝑑(𝑥)) →𝑃𝑟𝑜𝑚𝑜𝑡𝑒𝑑(𝑥)]
2. Some employees are careless:
∃𝑥  [𝐸𝑚𝑝𝑙𝑜𝑦𝑒𝑒(𝑥) ∧𝐶𝑎𝑟𝑒𝑙𝑒𝑠𝑠(𝑥)]
3. Careless employees do not work hard:
∀𝑥  [𝐶𝑎𝑟𝑒𝑙𝑒𝑠𝑠(𝑥) →¬𝑊𝑜𝑟𝑘𝐻𝑎𝑟𝑑(𝑥)]
Step 3: Logical Inference (Proof)
********** 4 **********
--- page 5 ---
From (2):
There exists an 𝑥such that 𝐸𝑚𝑝𝑙𝑜𝑦𝑒𝑒(𝑥) ∧𝐶𝑎𝑟𝑒𝑙𝑒𝑠𝑠(𝑥)
From (3):
If 𝐶𝑎𝑟𝑒𝑙𝑒𝑠𝑠(𝑥), then ¬𝑊𝑜𝑟𝑘𝐻𝑎𝑟𝑑(𝑥)
⇒ For that 𝑥:
𝐸𝑚𝑝𝑙𝑜𝑦𝑒𝑒(𝑥) ∧¬𝑊𝑜𝑟𝑘𝐻𝑎𝑟𝑑(𝑥)
From (1):
Only employees who work hard get promoted
(contrapositive idea: if not working hard → not promoted)
⇒ Therefore:
¬𝑃𝑟𝑜𝑚𝑜𝑡𝑒𝑑(𝑥)
Conclusion:
∃𝑥  [𝐸𝑚𝑝𝑙𝑜𝑦𝑒𝑒(𝑥) ∧¬𝑃𝑟𝑜𝑚𝑜𝑡𝑒𝑑(𝑥)]
Some employees do not get promoted.
Marks Mapping (10 Marks)
1. Predicate definitions – 2 marks
2. Correct FOL translations (3 statements) – 3 marks
3. Applying inference (linking statements) – 3 marks
4. Deriving final conclusion – 1 mark
5. Logical clarity/steps – 1 mark
3.2 Explain the Hidden Markov Model (HMM) in detail including its components, working mechanism,
mathematical representation, and real-world applications with suitable examples?
Answer:
A Hidden Markov Model (HMM) is a statistical model used to represent systems where the states are hidden (not
directly observable) but outputs (observations) are visible.
It is based on the Markov Process, where the next state depends only on the current state.
Components of HMM:
•   States (S): Hidden states of the system
•   Observations (O): Visible outputs
•   Transition Probabilities (A): Probability of moving from one state to another
•   Emission Probabilities (B): Probability of an observation given a state
•   Initial Probabilities (π): Starting state distribution
Working:
• System transitions between hidden states
• Each state generates observable outputs
• Goal is to infer hidden states from observations
Three Fundamental Problems:
********** 5 **********
--- page 6 ---
1. Evaluation Problem: Compute probability of observation sequence (Forward algorithm)
2. Decoding Problem: Find most likely state sequence (Viterbi algorithm)
3. Learning Problem: Estimate model parameters (Baum-Welch algorithm)
Applications:
• Speech recognition
•   Natural Language Processing (POS tagging)
•   Bioinformatics (gene prediction)
Marks Mapping (10 Marks)
1. Definition of HMM – 2 marks
2. Markov property explanation – 1 mark
3. Components (S, O, A, B, π) – 3 marks
4. Working principle – 2 marks
5. Three problems (Evaluation, Decoding, Learning) – 1 mark
6. Applications – 1 mark
4. 1 Describe the Backtracking Search algorithm used in problem-solving and Constraint Satisfaction Problems
(CSPs) and how solutions are systematically explored with a detailed example?
Answer:
Backtracking Search is a systematic method for solving Constraint Satisfaction Problems (CSPs) by exploring
possible solutions and backtracking (undoing choices) when a constraint is violated.
It builds a solution incrementally and abandons a path as soon as it determines that it cannot lead to a valid
solution.
Working:
•   Select an unassigned variable
•   Assign a value from its domain
• Check constraints:
o   If satisfied → continue
o   If violated → backtrack (remove assignment and try next value)
•   Repeat until solution is found or all possibilities are exhausted
Queens Problem
Place 4 queens on a chessboard such that no two queens attack each other.
• Try placing queens row by row
•   If a conflict occurs (same row, column, diagonal) → backtrack
•   Continue until a valid arrangement is found
Advantages:
•   Guarantees finding a solution (if exists)
********** 6 **********
--- page 7 ---
•   Efficient by pruning invalid paths early
Disadvantages:
• Time complexity can be high (exponential)
• Not suitable for very large problems without optimization
Marks Mapping (10 Marks)
1. Definition of Backtracking Search – 2 marks
2. Working/algorithm steps – 3 marks
3. Example explanation (e.g., 4-Queens) – 3 marks
4. Advantages – 1 mark
5. Disadvantages – 1 mark
4. 2 Discuss Neural Network Architecture in detail with suitable examples. Also explain the three activation
functions with proper formulas.
Answer:
A Neural Network Architecture is a computational model inspired by the human brain, consisting of
interconnected layers of neurons that process data.
Architecture:
•   Input Layer: Receives input features
• Hidden Layer(s): Performs computations using weights and activation functions
•   Output Layer: Produces final result
Each neuron computes:
𝑧= 𝑤⋅𝑥+ 𝑏
and passes it through an activation function.
Activation Functions (with Formulae)
1. Sigmoid Function
1
𝜎(𝑥) =
1 + 𝑒−𝑥
•   Output range: (0, 1)
• Used in binary classification
2. ReLU (Rectified Linear Unit)
𝑓(𝑥) = max⁡(0, 𝑥)
•   Output: 0 for negative, x for positive
• Widely used in hidden layers
3. Tanh Function
********** 7 **********
--- page 8 ---
𝑒𝑥−𝑒−𝑥
tanh⁡(𝑥) =
𝑒𝑥+ 𝑒−𝑥
•   Output range: (-1, 1)
•   Zero-centered
Working:
•   Inputs are weighted and summed
•   Activation functions introduce non-linearity
• Network learns by adjusting weights (training)
Advantages:
• Can model complex patterns
• Used in image, speech, NLP tasks
Marks Mapping (10 Marks)
1. Definition of Neural Network – 2 marks
2. Architecture (input, hidden, output layers) – 2 marks
3. Neuron computation (weighted sum) – 1 mark
4. Three activation functions with formulae – 3 marks
5. Working explanation – 1 mark
6. Applications/advantages – 1 mark
5.1 Consider, Grapevine Leaves Image Dataset consists of images of different grapevine leaf species. Build a
Multi-Layer Neural Network to classify these leaves based on their features.
Answer:
Check Code
5.2 You have been given a dataset containing images of different butterfly species. Each image belongs to one of
several butterfly classes. Consider a Convolutional Neural Network (CNN) model to classify butterfly images
into their respective species
Answer:
Check Code
6.1 In a college:
60% of students are boys and 40% are girls.
70% of boys play cricket.
50% of girls play cricket.
Tasks:
1. Find the probability that a randomly selected student plays cricket. (4 Marks)
2. If a student is known to play cricket, find the probability that the student is a boy.
********** 8 **********
--- page 9 ---
Answer:
Given Data
• 𝑃(𝐵𝑜𝑦) = 0.6, 𝑃(𝐺𝑖𝑟𝑙) = 0.4
• 𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡∣𝐵𝑜𝑦) = 0.7
• 𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡∣𝐺𝑖𝑟𝑙) = 0.5
1. Probability that a student plays cricket (4 Marks)
Using Total Probability Theorem:
𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡) = 𝑃(𝐵𝑜𝑦) ⋅𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡∣𝐵𝑜𝑦) + 𝑃(𝐺𝑖𝑟𝑙) ⋅𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡∣𝐺𝑖𝑟𝑙)
= (0.6 × 0.7) + (0.4 × 0.5)
= 0.42 + 0.20 = 0.62
𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡) = 0.62
2. Probability that a cricket player is a boy (6 Marks)
Using Bayes’ Theorem:
𝑃(𝐵𝑜𝑦) ⋅𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡∣𝐵𝑜𝑦)
𝑃(𝐵𝑜𝑦∣𝐶𝑟𝑖𝑐𝑘𝑒𝑡) =
𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡)
0.6 × 0.7
=
0.62
0.42
=   ≈0.677
0.62
𝑃(𝐵𝑜𝑦∣𝐶𝑟𝑖𝑐𝑘𝑒𝑡) ≈0.677  (67.7%)
Final Answers
1. 𝑃(𝐶𝑟𝑖𝑐𝑘𝑒𝑡) = 0.62
2. 𝑃(𝐵𝑜𝑦∣𝐶𝑟𝑖𝑐𝑘𝑒𝑡) ≈0.677
6. 2 Briefly explain the K Means Clustering Algorithm in detail with suitable example?
Answer:
K-Means Clustering is an unsupervised machine learning algorithm used to partition data into K clusters based
on similarity. Each cluster is represented by its centroid (mean point).
Working of Algorithm:
1. Choose number of clusters 𝐾
2. Initialize 𝐾centroids randomly
3. Assign each data point to the nearest centroid (using distance, usually Euclidean)
4. Recalculate centroids as mean of assigned points
5. Repeat steps 3–4 until centroids do not change (convergence)
Objective Function:
Minimize within-cluster variance:
********** 9 **********
--- page 10 ---
𝐾
𝐽= ∑∑∥𝑥− 𝜇𝑖∥2
𝑥∈𝐶𝑖
𝑖=1
Advantages:
• Simple and easy to implement
•   Efficient for large datasets
• Works well for spherical clusters
Disadvantages:
• Need to choose 𝐾in advance
•   Sensitive to initial centroids
• Not suitable for non-spherical clusters or outliers
Applications:
• Customer segmentation
• Image compression
•   Pattern recognition
Marks Mapping (10 Marks)
1. Definition of K-Means – 2 marks
2. Concept of clustering & centroid – 1 mark
3. Algorithm steps – 3 marks
4. Objective function (formula) – 1 mark
5. Advantages – 1 mark
6. Disadvantages – 1 mark
7. Applications – 1 mark
7.
1. Explain the concept of Random Restart Search in Artificial Intelligence and illustrate its effectiveness with a
suitable example?
2. Compare and contrast Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms in Artificial
Intelligence with suitable examples. Also explain their working principles, advantages, limitations, and suitable
use cases too.
3. Convert the following logical expression into Conjunctive Normal Form (CNF):
¬(P→Q)∨(R∧S)
********** 10 **********
--- page 11 ---
Answer:
Random Restart Search is an optimization technique used to overcome the problem of local maxima/minima in
search algorithms like hill climbing. It repeatedly runs the search algorithm from different random initial states
and selects the best solution found.
Working:
•   Start with a random initial state
• Apply a local search algorithm (e.g., Hill Climbing)
•   If a local optimum is reached, restart with a new random state
•   Repeat multiple times
• Choose the best solution among all runs
8 Queens Problem
•   Start with random placement of queens
•   Hill climbing may get stuck in local optimum
•   Restart with new random configuration
•   After several restarts, a valid solution is found
Advantages:
• Avoids getting stuck in local optima
•   Increases probability of finding global optimum
• Simple and effective
Disadvantages:
•   Computationally expensive (multiple runs)
• No guarantee of optimal solution
Applications:
•   Constraint Satisfaction Problems
•   Optimization problems
• AI search problems (e.g., N-Queens)
Marks Mapping (10 Marks)
1. Definition of Random Restart Search – 2 marks
2. Concept (local optima problem) – 1 mark
3. Working/algorithm steps – 3 marks
4. Example (e.g., 8-Queens) – 2 marks
5. Advantages – 1 mark
6. Disadvantages – 1 mark
********** 11 **********
--- page 12 ---
7. 2
Feature   BFS   DFS
Strategy   Level-wise   Depth-wise
Data Structure Queue   Stack/Recursion
Completeness Complete   May not be complete
Optimality   Yes (shortest path) No
Memory   High   Low
7.c
Given Expression
¬(𝑃→𝑄)     ∨  (𝑅∧𝑆)
Step-by-Step Conversion
Step 1: Eliminate Implication
𝑃→𝑄≡¬𝑃∨𝑄
⇒¬(¬𝑃∨𝑄) ∨(𝑅∧𝑆)
Step 2: Apply De Morgan’s Law
¬(¬𝑃∨𝑄) = 𝑃∧¬𝑄
⇒(𝑃∧¬𝑄) ∨(𝑅∧𝑆)
Step 3: Distribute OR over AND
(𝑃∧¬𝑄) ∨(𝑅∧𝑆)
= (𝑃∨𝑅) ∧(𝑃∨𝑆) ∧(¬𝑄∨𝑅) ∧(¬𝑄∨𝑆)
\ Final CNF
(𝑃∨𝑅) ∧(𝑃∨𝑆) ∧(¬𝑄∨𝑅) ∧(¬𝑄∨𝑆)
Marks Mapping (5 Marks)
1. Removing implication – 1 mark
2. Applying De Morgan’s law – 1 mark
3. Intermediate expression – 1 mark
4. Distribution to CNF form – 1 mark
5. Final correct CNF – 1 mark
********** 12 **********
````
