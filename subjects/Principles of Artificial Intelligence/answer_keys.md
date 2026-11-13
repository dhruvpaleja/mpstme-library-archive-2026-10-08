# Principles of Artificial Intelligence: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 89e796a65956

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_IT_7001/Principles of Artificial Intelligence/ANS_Principles of Artificial Intelligence(702IT0C035)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Principles of Artificial Intelligence
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
CO1 ; A Briefly elaborate PEAS parameters for AI agent for Personalized Music   5
BL2   Recommendation.
Ans: *[ PEAS full form-1M, Parameters covered-1M each]
1. Performance Measure (P)
Evaluates how well the system performs:
• Accuracy of recommendations
• User satisfaction (likes, skips, ratings)
•   Listening time / engagement
•   Diversity and novelty of songs
2. Environment (E)
The context in which the agent operates:
• Music streaming platform
•   Users with different preferences
• Music database (songs, artists, genres)
•   Context like time, mood, activity
3. Actuators (A)
Actions the system can perform:
• Recommend songs/playlists
•   Auto-play next track
•   Suggest artists or albums
•   Notify users with personalized suggestions
4. Sensors (S)
Data collected from the environment:
• User listening history
•   Likes, dislikes, skips
•   Search queries
Time of listening, device, location
********** 1 **********
--- page 2 ---
CO1 ; B Compare A* and AO* search based algorithm (Any 5 pts-5M)   5
BL4   Feature   A* Algorithm   AO* Algorithm
Graph Type   OR graph   AND-OR graph
Solution Type   Finds a single optimal   Finds an optimal solution graph
path
Node Types   Only OR nodes   Both AND and OR nodes
Evaluation   ( f(n) = g(n) + h(n) )   OR: min, AND: sum of child
Function   costs
Search Strategy   Expands lowest-cost   Expands most promising partial
node   solution graph
Backtracking   Not required   Required for cost updates
Complexity   Simpler   More complex
Application   Pathfinding (e.g., maps, Problem decomposition, planning
routing)
CO2 ; C   5
BL3   What is Overfitting in Decision Trees? How can it be avoided?
Overfitting in decision trees occurs when the model becomes excessively complex
and captures not only the underlying patterns in the training data but also noise and
outliers, leading to poor generalization on unseen data. This results in very high
accuracy on training data but low accuracy on test data. Overfitting typically
happens when the tree grows too deep with many branches. To avoid overfitting,
techniques such as pruning are used, including pre-pruning (limiting maximum
depth, minimum samples for split, etc.) and post-pruning (removing unnecessary
branches after full growth). Additionally, controlling tree depth, setting minimum
samples per node, using cross-validation, and applying ensemble methods like
Random Forest help improve model generalization.
Definition (1) + Causes/complexity & noise (1) + Effect/generalization & accuracy
gap (1) + Prevention methods/pruning & limits (1.5) + Advanced method (Random
Forest) (0.5)
CO3 ; D Differentiate between Information Retrieval and Information Extraction.   5
BL4
In Natural Language Processing, Information Retrieval (IR) and Information
Extraction (IE) are two different tasks. Information Retrieval refers to the process
of searching and retrieving relevant documents or data from a large collection
based on a user query, without modifying the content (e.g., search engines). In
contrast, Information Extraction involves automatically extracting structured
information such as entities, relationships, or facts from unstructured text. While
IR focuses on finding relevant documents, IE focuses on understanding and pulling
specific information from within those documents. Thus, IR deals with document-
level retrieval, whereas IE works at the content level to convert unstructured data
into structured form.
Definition of IR (1) + Definition of IE (1) + Key difference (retrieval vs
extraction) (1) + Level difference (document vs content) (1) + Example/clarity (1)
Q2   [20]
CO1 ; A Describe Depth-first search algorithm. Consider the graph shown below, start from 10
BL3   node A. identify the traversal path using depth First search algorithm
********** 2 **********
--- page 3 ---
Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by
going as deep as possible along each branch before backtracking. It starts from a
source node, visits an unvisited adjacent node, and continues this process
recursively until no unvisited nodes remain along the current path. Then it
backtracks to explore other branches. DFS can be implemented using a stack or
recursion.
🔍 DFS Traversal (Starting from A)
Assuming we visit adjacent nodes in a consistent order (e.g., left-to-right or
alphabetical), the traversal is:
A → C → F → G → D → E → B
🧠 Explanation of Traversal
•   Start at A
• Go deep: A → C
• From C → F
• From F → G
• From G → D
• From D → E
• From E → B
• No more unvisited nodes → stop
📊 Evaluation Rubric (5 Marks)
Definition of DFS (2) + Key idea (deep traversal & backtracking) (2) + Algorithm
approach (stack/recursion) (2) + Correct traversal path (3) + Clarity/step
explanation (1)
CO2 ; B Consider the following statement represent the given scenario involving a monkey, 10
BL3   a room, a hanging banana, a window, and a box.
• All monkeys are hungry.
• There exists a monkey at the door
• There exists a hungry monkey that cannot reach a hanging banana from the
ceiling.
• There exists a box at the window.
• All bananas are hanging from the ceiling.
Translate these sentences in predicate form.
[ All conversion-2M Each]
********** 3 **********
--- page 4 ---
Q3   [20]
CO1 ; A Explain the AO* search algorithm   10
BL4
*[Explanation-3M, Numerical solving stepwise 7M]
The AO* search algorithm is an informed search technique used for solving problems
represented as AND-OR graphs. In such graphs, some nodes represent OR choices (only
one path needs to be selected), while others represent AND conditions (all child nodes
must be solved together). AO* aims to find the optimal solution graph rather than just a
single path.
The algorithm starts from the initial node and expands the most promising node based on
heuristic values. Each node is assigned a cost estimate, and the algorithm continuously
updates these costs using a bottom-up approach. For OR nodes, the algorithm selects the
child with the minimum cost, whereas for AND nodes, it sums the costs of all child nodes.
As the search progresses, the best partial solution graph is maintained and updated until
an optimal solution is found. The algorithm also marks nodes as solved when all required
conditions are satisfied.
Feature   AO* Algorithm   A* Algorithm
Graph Type AND-OR Graph   OR Graph
Solution   Finds a solution graph   Finds a single path
Node Types AND nodes and OR nodes   Only OR nodes
Evaluation   Min (OR) and Sum (AND)   ( f(n) = g(n) + h(n) )
Expansion   Expands most promising partial   Expands lowest-cost
solution graph   node
Backtracking Required for cost updates   Not typically required
Step 1:
********** 4 **********
--- page 5 ---
Start from node A,
f(A⇢B) = g(B) + h(B)
= 1 + 5   ……here g(n)=1 is taken by default for path cost
= 6
f(A⇢C+D) = g(c) + h(c) + g(d) + h(d)
= 1 + 2 + 1 + 4   here we have added C & D because they are in AND
= 8
So, by calculation A⇢B path is chosen which is the minimum path, i.e f(A⇢B)
Here the value of E & F are calculated as follows,
f(B⇢E) = g(e) + h(e)
f(B⇢E) = 1 + 7
= 8
f(B⇢f) = g(f) + h(f)
f(B⇢f) = 1 + 9
= 10
So, by above calculation B⇢E path is chosen which is minimum path, i.e f(B⇢E) because
B's heuristic value is different from its actual value The heuristic is updated and the minimum
cost path is selected. The minimum value in our situation is 8. Therefore, the heuristic for A
must be updated due to the change in B's heuristic.
So we need to calculate it again.
f(A⇢B) = g(B) + updated h(B)
= 1 + 8
= 9
We have Updated all values in the above tree.
By comparing f(A⇢B) & f(A⇢C+D)
f(A⇢C+D) is shown to be smaller. i.e 8 < 9
Now explore f(A⇢C+D)
So, the current node is C
f(C⇢G) = g(g) + h(g)
f(C⇢G) = 1 + 3
= 4
f(C⇢H+I) = g(h) + h(h) + g(i) + h(i)
f(C⇢H+I) = 1 + 0 + 1 + 0
= 2
f(C⇢H+I) is selected as the path with the lowest cost and the heuristic is also left
unchanged because it matches the actual cost. Paths H & I are solved because the
heuristic for those paths is 0 but Path A⇢D needs to be calculated because it has an
AND.
f(D⇢J) = g(j) + h(j)
f(D⇢J) = 1 + 0
= 1
f(A⇢C+D) = g(c) + h(c) + g(d) + h(d)
= 1 + 2 + 1 + 1
= 5
********** 5 **********
--- page 6 ---
CO2 ; B Explain the concept of margin in SVM. Differentiate between hard margin and   10
BL4   soft margin SVM.
In Support Vector Machine (SVM), the margin refers to the distance between
the decision boundary (hyperplane) and the nearest data points from each class,
called support vectors. The main objective of SVM is to find a hyperplane that
maximizes this margin, as a larger margin leads to better generalization and
robustness of the model.
In a hard margin SVM, the model assumes that the data is perfectly linearly
separable and finds a hyperplane that separates all data points without any
misclassification. It strictly maximizes the margin with no tolerance for errors,
making it sensitive to noise and outliers. In contrast, a soft margin SVM allows
some misclassification by introducing slack variables, enabling the model to
handle non-linearly separable or noisy data. It balances between maximizing the
margin and minimizing classification errors using a regularization parameter (C).
📊 Evaluation Rubric (5 Marks)
Margin definition (2) + Role of margin/maximization (2) + Hard margin concept
(2) + Soft margin concept (2) + Key difference (strict vs tolerant) (2)
Q4   [20]
CO2 ; A Define the terms root node, attribute selection, and information gain in the context 10
BL5   of decision tree construction.
A small bank wants to decide whether to approve personal loans. They collected the
following small dataset of applicants:
Income   Credit Score   Loan Approved
Applicant
(High/Low)   (Good/Bad)   (Yes/No)
Ainal   High   Good   Yes
Badri   High   Bad   Yes
kartik   Low   Good   No
Sanjay   Low   Bad   No
1. Compute the information gain for the attributes Income and Credit Score.
Determine the best attribute for the root node.
2. Build a simple decision tree to classify whether a loan is approved.
*[ Each Def-2M each, IG calculation of each attributes-2M each, Identify best
attributes-2M, Tree-3M]
Root Node:
********** 6 **********
--- page 7 ---
The topmost node in a decision tree that represents the best attribute chosen to split the
dataset first. It divides the data into subsets based on the most informative feature.
Attribute Selection:
The process of choosing the best attribute at each step of tree construction. This is done
using measures like Information Gain, Gini Index, etc., to decide which attribute best
separates the data.
Information Gain:
Information Gain measures the reduction in entropy (uncertainty) after splitting a dataset
on an attribute. It is calculated as:
Entropy of Dataset:
Information Gain for Income
Split by Income:
High:
•   Yes = 2, No = 0 → Entropy = 0
Low:
•   Yes = 0, No = 2 → Entropy = 0
Information Gain for Credit Score
Split by Credit Score:
Good:
•   Yes = 1, No = 1 → Entropy = 1
Bad:
•   Yes = 1, No = 1 → Entropy = 1
Best Attribute for Root Node
• Income (IG = 1) is the best attribute
•   Credit Score (IG = 0) is not useful
Root Node = Income
Income
/   \
High   Low
CO2 ; B Explain the Minimax algorithm used in two-player games. How does Alpha-Beta   10
BL4   Pruning improve its efficiency?
The Minimax algorithm is used in two-player zero-sum games (like tic-tac-toe or
chess) to determine the optimal move by assuming both players play optimally. It
builds a game tree where one player (MAX) tries to maximize the score, while the
opponent (MIN) tries to minimize it. The algorithm recursively explores all
possible moves, evaluates terminal states using a utility function, and chooses the
move that gives the best worst-case outcome.
Alpha-Beta Pruning is an optimization technique for Minimax that reduces the
number of nodes evaluated in the game tree. It introduces two values: alpha (the
********** 7 **********
--- page 8 ---
best value MAX can achieve so far) and beta (the best value MIN can achieve so
far). If at any point alpha ≥ beta, further exploration of that branch is stopped
(pruned), as it will not affect the final decision. This significantly improves
efficiency without changing the final result of the algorithm.
Minimax definition (2) + MAX/MIN roles & game tree (2) + Recursive
evaluation/utility (2) + Alpha-Beta concept (2) + Efficiency improvement/pruning
condition (2)
Q5   [20]
CO2 ; A Define machine learning and its types.   10
BL3   Identify from the following is/are examples of supervised, unsupervised learning.
1.   Predicting rainfall based on historical data
2.   Predicting credit approval based on historical data
3.   Predicting the time (in days) a PhD student will take to complete his/her
thesis to earn a degree based on the historical data such as qualifications,
department, institute, research area, and time taken by other scholars to earn
the degree.
4.   Predicting if a customer is going to return or keep a particular product he/she
purchased from e-commerce website based on the historical data about the
customer purchases and the particular product.
*[Def-2M, Identification-2M each]
Machine learning is the science of getting computers to act by feeding them data
and letting them learn few tricks on their own without being explicitly
programmed.
1. Predicting rainfall based on historical data -------supervised
2. Predicting credit approval based on historical data---- supervised
3. Predicting the time (in days) a PhD student will take to complete his/her
thesis to earn a degree based on the historical data such as qualifications,
department, institute, research area, and time taken by other scholars to
earn the degree. ---- unsupervised
Predicting if a customer is going to return or keep a particular product he/she
purchased from e-commerce website based on the historical data about the
customer purchases and the particular product. ----supervised
CO3 ; B Describe the complete NLP pipeline. Explain each stage such as tokenization,   10
BL2   stemming, lemmatization, stop-word removal, and POS tagging
✍️ Answer (10 Marks)
The Natural Language Processing (NLP) pipeline is a sequence of steps used to
process raw text into a structured format so that machines can understand and
analyze human language. It involves several preprocessing stages that clean and
transform text before applying machine learning models.
Tokenization is the first step, where the input text is divided into smaller units
called tokens, such as words or sentences. This helps in breaking down
unstructured text into manageable pieces for further processing.
Stop-word removal is the process of eliminating common words like is, the, and,
in, which do not contribute significant meaning to the text. Removing these words
reduces data size and improves processing efficiency.
********** 8 **********
--- page 9 ---
Stemming is a technique used to reduce words to their root form by removing
suffixes. It is a rule-based process and may produce words that are not
grammatically correct. For example, words like running, runs, runner may be
reduced to run.
Lemmatization improves upon stemming by converting words into their correct
base or dictionary form (lemma) using vocabulary and grammatical analysis. For
example, better becomes good and running becomes run. It produces more
meaningful results compared to stemming.
Part-of-Speech (POS) tagging assigns grammatical categories to each word in a
sentence, such as noun, verb, adjective, etc. This helps in understanding the
syntactic structure and meaning of the sentence.
Overall, the NLP pipeline transforms raw text into a structured and meaningful
representation, enabling machines to perform tasks like text classification,
sentiment analysis, and information extraction effectively.
📊 Evaluation Rubric (10 Marks)
Definition of NLP pipeline (2) + Tokenization (2) + Stop-word removal (1.5) +
Stemming (1.5) + Lemmatization (1.5) + POS tagging (1.5)
Q6   [20]
CO1 ; A Differentiate propositional logic with First order logic. List the Inference rules   10
BL4   along with suitable examples for first order logic.
✍️ Answer (10 Marks)
In Artificial Intelligence, both Propositional Logic and First-Order Logic
(FOL) are used for knowledge representation, but they differ in expressiveness and
capability.
Propositional Logic deals with simple statements that are either true or false,
without considering internal structure. It uses propositional variables (P, Q, R) and
logical connectives like AND, OR, NOT. For example, P: It is raining. It cannot
represent relationships or quantify objects.
First-Order Logic (FOL) is more expressive and allows representation of objects,
properties, relations, and quantifiers. It uses predicates, variables, constants, and
quantifiers like ∀ (for all) and ∃ (there exists). For example, ∀x Human(x) →
Mortal(x) represents that all humans are mortal.
Difference: Propositional logic is simple but limited, while FOL is more powerful
and can represent complex relationships and general rules about objects in a
domain.
📌 Inference Rules in First-Order Logic (with Examples)
1. Universal Instantiation (UI)
From a universal statement, we can infer for a specific instance.
Example: ∀x Human(x) → Mortal(x)
⇒ Human(Socrates) → Mortal(Socrates)
2. Existential Instantiation (EI)
From an existential statement, we assume a specific instance.
Example: ∃x Student(x)
⇒ Student(A) (A is some specific student)
3. Universal Generalization (UG)
If something is true for an arbitrary element, it is true for all.
********** 9 **********
--- page 10 ---
Example: Human(x) → Mortal(x)
⇒ ∀x Human(x) → Mortal(x)
4. Existential Generalization (EG)
From a specific instance, we can generalize existence.
Example: Student(Ram)
⇒ ∃x Student(x)
5. Modus Ponens
If P → Q and P is true, then Q is true.
Example: Human(Socrates) → Mortal(Socrates), Human(Socrates)
⇒ Mortal(Socrates)
🧠 Conclusion
Propositional logic is limited to simple true/false statements, whereas First-Order
Logic provides a richer framework to represent real-world knowledge using objects
and relationships. Inference rules in FOL help derive new facts logically from
existing knowledge.
📊 Evaluation Rubric (10 Marks)
Definition of Propositional Logic (2) + Definition of FOL (2) + Key differences
(2) + Inference rules explanation (3) + Examples (1)
CO3 ; B Explain N-gram Language Models. Discuss unigram, bigram, and trigram models   10
BL2   along with their advantages and limitations.
✍️ Answer (10 Marks)
N-gram language models are probabilistic models used in Natural Language
Processing (NLP) to predict the likelihood of a sequence of words. They assume
that the probability of a word depends only on the previous N−1 words (Markov
assumption). Thus, instead of considering the entire sentence, the model simplifies
computation by using limited context.
🔤 Types of N-gram Models
1. Unigram Model (N = 1)
In a unigram model, each word is considered independent of others. The
probability of a sentence is the product of individual word probabilities.
Example:
P(“I love NLP”) = P(I) × P(love) × P(NLP)
Advantage: Simple and requires less data
Limitation: Ignores context, leading to poor accuracy
2. Bigram Model (N = 2)
In a bigram model, the probability of a word depends on the previous one word.
Example:
P(“I love NLP”) = P(I) × P(love|I) × P(NLP|love)
Advantage: Captures some context, better than unigram
Limitation: Still limited context, data sparsity problem
3. Trigram Model (N = 3)
In a trigram model, the probability of a word depends on the previous two words.
Example:
P(“I love NLP”) = P(I) × P(love|I) × P(NLP|I, love)
********** 10 **********
--- page 11 ---
Advantage: Captures more context, more accurate
Limitation: Requires large data, higher computational cost, sparsity increases
⚖️ Advantages of N-gram Models
• Simple and easy to implement
• Computationally efficient for small N
• Useful baseline for language modeling tasks
⚠️ Limitations of N-gram Models
• Data sparsity: Many word combinations may not appear in training data
• Limited context: Cannot capture long-range dependencies
• Storage issues: Large memory required for higher N
• Poor handling of unseen words (out-of-vocabulary problem)
🧠 Conclusion
N-gram models are foundational techniques in NLP that estimate word sequence
probabilities using limited context. While unigram, bigram, and trigram models
progressively improve context understanding, they suffer from sparsity and
scalability issues, which led to the development of more advanced models like
neural language models.
📊 Evaluation Rubric (10 Marks)
Definition of N-gram model (2) + Unigram explanation (2) + Bigram explanation
(2) + Trigram explanation (2) + Advantages & limitations (2)
Q7   [20]
CO2 ; A Explain the architecture of an Artificial Neural Network. Discuss different types   10
BL2   of layers (input, hidden, output) and their roles.
✍️ Answer (10 Marks)
An Artificial Neural Network (ANN) is a computational model inspired by the
human brain, consisting of interconnected nodes (neurons) organized in layers. It is
widely used in machine learning to recognize patterns, classify data, and make
predictions. The architecture of an ANN defines how neurons are arranged and
how information flows between layers.
🧠 Architecture of ANN
An ANN typically consists of three main types of layers: input layer, hidden
layer(s), and output layer. Each neuron receives inputs, applies weights, sums
them, and passes the result through an activation function to produce an output.
🔹 1. Input Layer
The input layer is the first layer of the network that receives raw data from the
external environment. Each neuron in this layer represents a feature of the input
dataset. It does not perform computations but simply passes the input values to the
next layer.
Role:
• Accepts input data
********** 11 **********
--- page 12 ---
•   Distributes data to hidden layers
🔹 2. Hidden Layer(s)
The hidden layers are intermediate layers between input and output layers. These
layers perform most of the computations in the network. Each neuron calculates a
weighted sum of inputs, applies an activation function (such as ReLU or sigmoid),
and passes the result forward.
Role:
•   Extract features and patterns
• Perform nonlinear transformations
• Enable learning of complex relationships
🔹 3. Output Layer
The output layer is the final layer that produces the result of the network. The
number of neurons depends on the type of problem (e.g., one neuron for
regression, multiple for classification). It uses appropriate activation functions like
sigmoid or softmax.
Role:
• Produces final prediction/output
• Maps processed data to desired format
⚙️ Additional Components
• Weights and Biases: Control the strength of connections
• Activation Functions: Introduce non-linearity
• Loss Function: Measures error
• Backpropagation: Updates weights to minimize error
🧠 Conclusion
The ANN architecture consists of layered neurons where the input layer receives
data, hidden layers process and learn patterns, and the output layer produces the
final result. This layered structure enables neural networks to model complex real-
world problems effectively.
📊 Evaluation Rubric (10 Marks)
Definition of ANN (2) + Architecture explanation (2) + Input layer role (2) +
Hidden layer role (2) + Output layer role (2)
CO2 ; B Explain the role of AI techniques such as Machine Learning, Natural Language   10
BL5   Processing, and Knowledge representation in modern applications. Illustrate with
examples how these techniques are used in intelligent systems.
✍️ Answer (10 Marks)
Artificial Intelligence (AI) uses various techniques such as Machine Learning
(ML), Natural Language Processing (NLP), and Knowledge Representation
(KR) to build intelligent systems that can learn, reason, and interact with humans.
These techniques play a crucial role in modern applications across multiple
domains.
********** 12 **********
--- page 13 ---
🤖 Machine Learning (ML)
Machine Learning enables systems to learn patterns from data and make
predictions or decisions without explicit programming. It is widely used in
applications such as recommendation systems, fraud detection, and image
recognition.
Example: Platforms like Netflix use ML algorithms to recommend movies based
on user preferences and viewing history. Similarly, email services use ML for
spam detection.
💬 Natural Language Processing (NLP)
NLP allows machines to understand, interpret, and generate human language. It is
essential for communication between humans and computers.
Example: Virtual assistants like Amazon Alexa and Google Assistant use NLP to
understand voice commands and respond appropriately. NLP is also used in
chatbots, language translation, and sentiment analysis.
🧠 Knowledge Representation (KR)
Knowledge Representation involves storing information in a structured form so
that machines can reason and make decisions. It uses techniques like logic, rules,
and ontologies to represent real-world knowledge.
Example: Expert systems in healthcare use KR to represent medical knowledge
and assist doctors in diagnosis. For instance, a system can infer diseases based on
symptoms using logical rules.
🌐 Role in Intelligent Systems
These techniques often work together in intelligent systems:
• ML provides learning from data
• NLP enables human-computer interaction
• KR supports reasoning and decision-making
Combined Example: A smart healthcare assistant can use NLP to understand
patient queries, ML to predict possible diseases, and KR to provide logical
explanations and recommendations.
🧠 Conclusion
Machine Learning, NLP, and Knowledge Representation are fundamental AI
techniques that power modern intelligent systems. Their integration enables
systems to learn, understand language, and reason effectively, making AI
applications more accurate and human-like.
📊 Evaluation Rubric (10 Marks)
Explanation of ML (2) + Explanation of NLP (2) + Explanation of KR (2) +
Examples for each (3) + Integration in intelligent systems (1)
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 723f30b2a312

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_IT_7041/Principles of Artificial Intelligence/ANS_Principles of Artificial Intelligence(702IT0C035)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Principles of Artificial Intelligence
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
CO1 ; A Briefly elaborate PEAS parameters for AI agent for Personalized Music   5
BL2   Recommendation.
Ans: *[ PEAS full form-1M, Parameters covered-1M each]
1. Performance Measure (P)
Evaluates how well the system performs:
• Accuracy of recommendations
• User satisfaction (likes, skips, ratings)
•   Listening time / engagement
•   Diversity and novelty of songs
2. Environment (E)
The context in which the agent operates:
• Music streaming platform
•   Users with different preferences
• Music database (songs, artists, genres)
•   Context like time, mood, activity
3. Actuators (A)
Actions the system can perform:
• Recommend songs/playlists
•   Auto-play next track
•   Suggest artists or albums
•   Notify users with personalized suggestions
4. Sensors (S)
Data collected from the environment:
• User listening history
•   Likes, dislikes, skips
•   Search queries
Time of listening, device, location
********** 1 **********
--- page 2 ---
CO1 ; B Compare A* and AO* search based algorithm (Any 5 pts-5M)   5
BL4   Feature   A* Algorithm   AO* Algorithm
Graph Type   OR graph   AND-OR graph
Solution Type   Finds a single optimal   Finds an optimal solution graph
path
Node Types   Only OR nodes   Both AND and OR nodes
Evaluation   ( f(n) = g(n) + h(n) )   OR: min, AND: sum of child
Function   costs
Search Strategy   Expands lowest-cost   Expands most promising partial
node   solution graph
Backtracking   Not required   Required for cost updates
Complexity   Simpler   More complex
Application   Pathfinding (e.g., maps, Problem decomposition, planning
routing)
CO2 ; C   5
BL3   What is Overfitting in Decision Trees? How can it be avoided?
Overfitting in decision trees occurs when the model becomes excessively complex
and captures not only the underlying patterns in the training data but also noise and
outliers, leading to poor generalization on unseen data. This results in very high
accuracy on training data but low accuracy on test data. Overfitting typically
happens when the tree grows too deep with many branches. To avoid overfitting,
techniques such as pruning are used, including pre-pruning (limiting maximum
depth, minimum samples for split, etc.) and post-pruning (removing unnecessary
branches after full growth). Additionally, controlling tree depth, setting minimum
samples per node, using cross-validation, and applying ensemble methods like
Random Forest help improve model generalization.
Definition (1) + Causes/complexity & noise (1) + Effect/generalization & accuracy
gap (1) + Prevention methods/pruning & limits (1.5) + Advanced method (Random
Forest) (0.5)
CO3 ; D Differentiate between Information Retrieval and Information Extraction.   5
BL4
In Natural Language Processing, Information Retrieval (IR) and Information
Extraction (IE) are two different tasks. Information Retrieval refers to the process
of searching and retrieving relevant documents or data from a large collection
based on a user query, without modifying the content (e.g., search engines). In
contrast, Information Extraction involves automatically extracting structured
information such as entities, relationships, or facts from unstructured text. While
IR focuses on finding relevant documents, IE focuses on understanding and pulling
specific information from within those documents. Thus, IR deals with document-
level retrieval, whereas IE works at the content level to convert unstructured data
into structured form.
Definition of IR (1) + Definition of IE (1) + Key difference (retrieval vs
extraction) (1) + Level difference (document vs content) (1) + Example/clarity (1)
Q2   [20]
CO1 ; A Describe Depth-first search algorithm. Consider the graph shown below, start from 10
BL3   node A. identify the traversal path using depth First search algorithm
********** 2 **********
--- page 3 ---
Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by
going as deep as possible along each branch before backtracking. It starts from a
source node, visits an unvisited adjacent node, and continues this process
recursively until no unvisited nodes remain along the current path. Then it
backtracks to explore other branches. DFS can be implemented using a stack or
recursion.
🔍 DFS Traversal (Starting from A)
Assuming we visit adjacent nodes in a consistent order (e.g., left-to-right or
alphabetical), the traversal is:
A → C → F → G → D → E → B
🧠 Explanation of Traversal
•   Start at A
• Go deep: A → C
• From C → F
• From F → G
• From G → D
• From D → E
• From E → B
• No more unvisited nodes → stop
📊 Evaluation Rubric (5 Marks)
Definition of DFS (2) + Key idea (deep traversal & backtracking) (2) + Algorithm
approach (stack/recursion) (2) + Correct traversal path (3) + Clarity/step
explanation (1)
CO2 ; B Consider the following statement represent the given scenario involving a monkey, 10
BL3   a room, a hanging banana, a window, and a box.
• All monkeys are hungry.
• There exists a monkey at the door
• There exists a hungry monkey that cannot reach a hanging banana from the
ceiling.
• There exists a box at the window.
• All bananas are hanging from the ceiling.
Translate these sentences in predicate form.
[ All conversion-2M Each]
********** 3 **********
--- page 4 ---
Q3   [20]
CO1 ; A Explain the AO* search algorithm   10
BL4
*[Explanation-3M, Numerical solving stepwise 7M]
The AO* search algorithm is an informed search technique used for solving problems
represented as AND-OR graphs. In such graphs, some nodes represent OR choices (only
one path needs to be selected), while others represent AND conditions (all child nodes
must be solved together). AO* aims to find the optimal solution graph rather than just a
single path.
The algorithm starts from the initial node and expands the most promising node based on
heuristic values. Each node is assigned a cost estimate, and the algorithm continuously
updates these costs using a bottom-up approach. For OR nodes, the algorithm selects the
child with the minimum cost, whereas for AND nodes, it sums the costs of all child nodes.
As the search progresses, the best partial solution graph is maintained and updated until
an optimal solution is found. The algorithm also marks nodes as solved when all required
conditions are satisfied.
Feature   AO* Algorithm   A* Algorithm
Graph Type AND-OR Graph   OR Graph
Solution   Finds a solution graph   Finds a single path
Node Types AND nodes and OR nodes   Only OR nodes
Evaluation   Min (OR) and Sum (AND)   ( f(n) = g(n) + h(n) )
Expansion   Expands most promising partial   Expands lowest-cost
solution graph   node
Backtracking Required for cost updates   Not typically required
Step 1:
********** 4 **********
--- page 5 ---
Start from node A,
f(A⇢B) = g(B) + h(B)
= 1 + 5   ……here g(n)=1 is taken by default for path cost
= 6
f(A⇢C+D) = g(c) + h(c) + g(d) + h(d)
= 1 + 2 + 1 + 4   here we have added C & D because they are in AND
= 8
So, by calculation A⇢B path is chosen which is the minimum path, i.e f(A⇢B)
Here the value of E & F are calculated as follows,
f(B⇢E) = g(e) + h(e)
f(B⇢E) = 1 + 7
= 8
f(B⇢f) = g(f) + h(f)
f(B⇢f) = 1 + 9
= 10
So, by above calculation B⇢E path is chosen which is minimum path, i.e f(B⇢E) because
B's heuristic value is different from its actual value The heuristic is updated and the minimum
cost path is selected. The minimum value in our situation is 8. Therefore, the heuristic for A
must be updated due to the change in B's heuristic.
So we need to calculate it again.
f(A⇢B) = g(B) + updated h(B)
= 1 + 8
= 9
We have Updated all values in the above tree.
By comparing f(A⇢B) & f(A⇢C+D)
f(A⇢C+D) is shown to be smaller. i.e 8 < 9
Now explore f(A⇢C+D)
So, the current node is C
f(C⇢G) = g(g) + h(g)
f(C⇢G) = 1 + 3
= 4
f(C⇢H+I) = g(h) + h(h) + g(i) + h(i)
f(C⇢H+I) = 1 + 0 + 1 + 0
= 2
f(C⇢H+I) is selected as the path with the lowest cost and the heuristic is also left
unchanged because it matches the actual cost. Paths H & I are solved because the
heuristic for those paths is 0 but Path A⇢D needs to be calculated because it has an
AND.
f(D⇢J) = g(j) + h(j)
f(D⇢J) = 1 + 0
= 1
f(A⇢C+D) = g(c) + h(c) + g(d) + h(d)
= 1 + 2 + 1 + 1
= 5
********** 5 **********
--- page 6 ---
CO2 ; B Explain the concept of margin in SVM. Differentiate between hard margin and   10
BL4   soft margin SVM.
In Support Vector Machine (SVM), the margin refers to the distance between
the decision boundary (hyperplane) and the nearest data points from each class,
called support vectors. The main objective of SVM is to find a hyperplane that
maximizes this margin, as a larger margin leads to better generalization and
robustness of the model.
In a hard margin SVM, the model assumes that the data is perfectly linearly
separable and finds a hyperplane that separates all data points without any
misclassification. It strictly maximizes the margin with no tolerance for errors,
making it sensitive to noise and outliers. In contrast, a soft margin SVM allows
some misclassification by introducing slack variables, enabling the model to
handle non-linearly separable or noisy data. It balances between maximizing the
margin and minimizing classification errors using a regularization parameter (C).
📊 Evaluation Rubric (5 Marks)
Margin definition (2) + Role of margin/maximization (2) + Hard margin concept
(2) + Soft margin concept (2) + Key difference (strict vs tolerant) (2)
Q4   [20]
CO2 ; A Define the terms root node, attribute selection, and information gain in the context 10
BL5   of decision tree construction.
A small bank wants to decide whether to approve personal loans. They collected the
following small dataset of applicants:
Income   Credit Score   Loan Approved
Applicant
(High/Low)   (Good/Bad)   (Yes/No)
Ainal   High   Good   Yes
Badri   High   Bad   Yes
kartik   Low   Good   No
Sanjay   Low   Bad   No
1. Compute the information gain for the attributes Income and Credit Score.
Determine the best attribute for the root node.
2. Build a simple decision tree to classify whether a loan is approved.
*[ Each Def-2M each, IG calculation of each attributes-2M each, Identify best
attributes-2M, Tree-3M]
Root Node:
********** 6 **********
--- page 7 ---
The topmost node in a decision tree that represents the best attribute chosen to split the
dataset first. It divides the data into subsets based on the most informative feature.
Attribute Selection:
The process of choosing the best attribute at each step of tree construction. This is done
using measures like Information Gain, Gini Index, etc., to decide which attribute best
separates the data.
Information Gain:
Information Gain measures the reduction in entropy (uncertainty) after splitting a dataset
on an attribute. It is calculated as:
Entropy of Dataset:
Information Gain for Income
Split by Income:
High:
•   Yes = 2, No = 0 → Entropy = 0
Low:
•   Yes = 0, No = 2 → Entropy = 0
Information Gain for Credit Score
Split by Credit Score:
Good:
•   Yes = 1, No = 1 → Entropy = 1
Bad:
•   Yes = 1, No = 1 → Entropy = 1
Best Attribute for Root Node
• Income (IG = 1) is the best attribute
•   Credit Score (IG = 0) is not useful
Root Node = Income
Income
/   \
High   Low
CO2 ; B Explain the Minimax algorithm used in two-player games. How does Alpha-Beta   10
BL4   Pruning improve its efficiency?
The Minimax algorithm is used in two-player zero-sum games (like tic-tac-toe or
chess) to determine the optimal move by assuming both players play optimally. It
builds a game tree where one player (MAX) tries to maximize the score, while the
opponent (MIN) tries to minimize it. The algorithm recursively explores all
possible moves, evaluates terminal states using a utility function, and chooses the
move that gives the best worst-case outcome.
Alpha-Beta Pruning is an optimization technique for Minimax that reduces the
number of nodes evaluated in the game tree. It introduces two values: alpha (the
********** 7 **********
--- page 8 ---
best value MAX can achieve so far) and beta (the best value MIN can achieve so
far). If at any point alpha ≥ beta, further exploration of that branch is stopped
(pruned), as it will not affect the final decision. This significantly improves
efficiency without changing the final result of the algorithm.
Minimax definition (2) + MAX/MIN roles & game tree (2) + Recursive
evaluation/utility (2) + Alpha-Beta concept (2) + Efficiency improvement/pruning
condition (2)
Q5   [20]
CO2 ; A Define machine learning and its types.   10
BL3   Identify from the following is/are examples of supervised, unsupervised learning.
1.   Predicting rainfall based on historical data
2.   Predicting credit approval based on historical data
3.   Predicting the time (in days) a PhD student will take to complete his/her
thesis to earn a degree based on the historical data such as qualifications,
department, institute, research area, and time taken by other scholars to earn
the degree.
4.   Predicting if a customer is going to return or keep a particular product he/she
purchased from e-commerce website based on the historical data about the
customer purchases and the particular product.
*[Def-2M, Identification-2M each]
Machine learning is the science of getting computers to act by feeding them data
and letting them learn few tricks on their own without being explicitly
programmed.
1. Predicting rainfall based on historical data -------supervised
2. Predicting credit approval based on historical data---- supervised
3. Predicting the time (in days) a PhD student will take to complete his/her
thesis to earn a degree based on the historical data such as qualifications,
department, institute, research area, and time taken by other scholars to
earn the degree. ---- unsupervised
Predicting if a customer is going to return or keep a particular product he/she
purchased from e-commerce website based on the historical data about the
customer purchases and the particular product. ----supervised
CO3 ; B Describe the complete NLP pipeline. Explain each stage such as tokenization,   10
BL2   stemming, lemmatization, stop-word removal, and POS tagging
✍️ Answer (10 Marks)
The Natural Language Processing (NLP) pipeline is a sequence of steps used to
process raw text into a structured format so that machines can understand and
analyze human language. It involves several preprocessing stages that clean and
transform text before applying machine learning models.
Tokenization is the first step, where the input text is divided into smaller units
called tokens, such as words or sentences. This helps in breaking down
unstructured text into manageable pieces for further processing.
Stop-word removal is the process of eliminating common words like is, the, and,
in, which do not contribute significant meaning to the text. Removing these words
reduces data size and improves processing efficiency.
********** 8 **********
--- page 9 ---
Stemming is a technique used to reduce words to their root form by removing
suffixes. It is a rule-based process and may produce words that are not
grammatically correct. For example, words like running, runs, runner may be
reduced to run.
Lemmatization improves upon stemming by converting words into their correct
base or dictionary form (lemma) using vocabulary and grammatical analysis. For
example, better becomes good and running becomes run. It produces more
meaningful results compared to stemming.
Part-of-Speech (POS) tagging assigns grammatical categories to each word in a
sentence, such as noun, verb, adjective, etc. This helps in understanding the
syntactic structure and meaning of the sentence.
Overall, the NLP pipeline transforms raw text into a structured and meaningful
representation, enabling machines to perform tasks like text classification,
sentiment analysis, and information extraction effectively.
📊 Evaluation Rubric (10 Marks)
Definition of NLP pipeline (2) + Tokenization (2) + Stop-word removal (1.5) +
Stemming (1.5) + Lemmatization (1.5) + POS tagging (1.5)
Q6   [20]
CO1 ; A Differentiate propositional logic with First order logic. List the Inference rules   10
BL4   along with suitable examples for first order logic.
✍️ Answer (10 Marks)
In Artificial Intelligence, both Propositional Logic and First-Order Logic
(FOL) are used for knowledge representation, but they differ in expressiveness and
capability.
Propositional Logic deals with simple statements that are either true or false,
without considering internal structure. It uses propositional variables (P, Q, R) and
logical connectives like AND, OR, NOT. For example, P: It is raining. It cannot
represent relationships or quantify objects.
First-Order Logic (FOL) is more expressive and allows representation of objects,
properties, relations, and quantifiers. It uses predicates, variables, constants, and
quantifiers like ∀ (for all) and ∃ (there exists). For example, ∀x Human(x) →
Mortal(x) represents that all humans are mortal.
Difference: Propositional logic is simple but limited, while FOL is more powerful
and can represent complex relationships and general rules about objects in a
domain.
📌 Inference Rules in First-Order Logic (with Examples)
1. Universal Instantiation (UI)
From a universal statement, we can infer for a specific instance.
Example: ∀x Human(x) → Mortal(x)
⇒ Human(Socrates) → Mortal(Socrates)
2. Existential Instantiation (EI)
From an existential statement, we assume a specific instance.
Example: ∃x Student(x)
⇒ Student(A) (A is some specific student)
3. Universal Generalization (UG)
If something is true for an arbitrary element, it is true for all.
********** 9 **********
--- page 10 ---
Example: Human(x) → Mortal(x)
⇒ ∀x Human(x) → Mortal(x)
4. Existential Generalization (EG)
From a specific instance, we can generalize existence.
Example: Student(Ram)
⇒ ∃x Student(x)
5. Modus Ponens
If P → Q and P is true, then Q is true.
Example: Human(Socrates) → Mortal(Socrates), Human(Socrates)
⇒ Mortal(Socrates)
🧠 Conclusion
Propositional logic is limited to simple true/false statements, whereas First-Order
Logic provides a richer framework to represent real-world knowledge using objects
and relationships. Inference rules in FOL help derive new facts logically from
existing knowledge.
📊 Evaluation Rubric (10 Marks)
Definition of Propositional Logic (2) + Definition of FOL (2) + Key differences
(2) + Inference rules explanation (3) + Examples (1)
CO3 ; B Explain N-gram Language Models. Discuss unigram, bigram, and trigram models   10
BL2   along with their advantages and limitations.
✍️ Answer (10 Marks)
N-gram language models are probabilistic models used in Natural Language
Processing (NLP) to predict the likelihood of a sequence of words. They assume
that the probability of a word depends only on the previous N−1 words (Markov
assumption). Thus, instead of considering the entire sentence, the model simplifies
computation by using limited context.
🔤 Types of N-gram Models
1. Unigram Model (N = 1)
In a unigram model, each word is considered independent of others. The
probability of a sentence is the product of individual word probabilities.
Example:
P(“I love NLP”) = P(I) × P(love) × P(NLP)
Advantage: Simple and requires less data
Limitation: Ignores context, leading to poor accuracy
2. Bigram Model (N = 2)
In a bigram model, the probability of a word depends on the previous one word.
Example:
P(“I love NLP”) = P(I) × P(love|I) × P(NLP|love)
Advantage: Captures some context, better than unigram
Limitation: Still limited context, data sparsity problem
3. Trigram Model (N = 3)
In a trigram model, the probability of a word depends on the previous two words.
Example:
P(“I love NLP”) = P(I) × P(love|I) × P(NLP|I, love)
********** 10 **********
--- page 11 ---
Advantage: Captures more context, more accurate
Limitation: Requires large data, higher computational cost, sparsity increases
⚖️ Advantages of N-gram Models
• Simple and easy to implement
• Computationally efficient for small N
• Useful baseline for language modeling tasks
⚠️ Limitations of N-gram Models
• Data sparsity: Many word combinations may not appear in training data
• Limited context: Cannot capture long-range dependencies
• Storage issues: Large memory required for higher N
• Poor handling of unseen words (out-of-vocabulary problem)
🧠 Conclusion
N-gram models are foundational techniques in NLP that estimate word sequence
probabilities using limited context. While unigram, bigram, and trigram models
progressively improve context understanding, they suffer from sparsity and
scalability issues, which led to the development of more advanced models like
neural language models.
📊 Evaluation Rubric (10 Marks)
Definition of N-gram model (2) + Unigram explanation (2) + Bigram explanation
(2) + Trigram explanation (2) + Advantages & limitations (2)
Q7   [20]
CO2 ; A Explain the architecture of an Artificial Neural Network. Discuss different types   10
BL2   of layers (input, hidden, output) and their roles.
✍️ Answer (10 Marks)
An Artificial Neural Network (ANN) is a computational model inspired by the
human brain, consisting of interconnected nodes (neurons) organized in layers. It is
widely used in machine learning to recognize patterns, classify data, and make
predictions. The architecture of an ANN defines how neurons are arranged and
how information flows between layers.
🧠 Architecture of ANN
An ANN typically consists of three main types of layers: input layer, hidden
layer(s), and output layer. Each neuron receives inputs, applies weights, sums
them, and passes the result through an activation function to produce an output.
🔹 1. Input Layer
The input layer is the first layer of the network that receives raw data from the
external environment. Each neuron in this layer represents a feature of the input
dataset. It does not perform computations but simply passes the input values to the
next layer.
Role:
• Accepts input data
********** 11 **********
--- page 12 ---
•   Distributes data to hidden layers
🔹 2. Hidden Layer(s)
The hidden layers are intermediate layers between input and output layers. These
layers perform most of the computations in the network. Each neuron calculates a
weighted sum of inputs, applies an activation function (such as ReLU or sigmoid),
and passes the result forward.
Role:
•   Extract features and patterns
• Perform nonlinear transformations
• Enable learning of complex relationships
🔹 3. Output Layer
The output layer is the final layer that produces the result of the network. The
number of neurons depends on the type of problem (e.g., one neuron for
regression, multiple for classification). It uses appropriate activation functions like
sigmoid or softmax.
Role:
• Produces final prediction/output
• Maps processed data to desired format
⚙️ Additional Components
• Weights and Biases: Control the strength of connections
• Activation Functions: Introduce non-linearity
• Loss Function: Measures error
• Backpropagation: Updates weights to minimize error
🧠 Conclusion
The ANN architecture consists of layered neurons where the input layer receives
data, hidden layers process and learn patterns, and the output layer produces the
final result. This layered structure enables neural networks to model complex real-
world problems effectively.
📊 Evaluation Rubric (10 Marks)
Definition of ANN (2) + Architecture explanation (2) + Input layer role (2) +
Hidden layer role (2) + Output layer role (2)
CO2 ; B Explain the role of AI techniques such as Machine Learning, Natural Language   10
BL5   Processing, and Knowledge representation in modern applications. Illustrate with
examples how these techniques are used in intelligent systems.
✍️ Answer (10 Marks)
Artificial Intelligence (AI) uses various techniques such as Machine Learning
(ML), Natural Language Processing (NLP), and Knowledge Representation
(KR) to build intelligent systems that can learn, reason, and interact with humans.
These techniques play a crucial role in modern applications across multiple
domains.
********** 12 **********
--- page 13 ---
🤖 Machine Learning (ML)
Machine Learning enables systems to learn patterns from data and make
predictions or decisions without explicit programming. It is widely used in
applications such as recommendation systems, fraud detection, and image
recognition.
Example: Platforms like Netflix use ML algorithms to recommend movies based
on user preferences and viewing history. Similarly, email services use ML for
spam detection.
💬 Natural Language Processing (NLP)
NLP allows machines to understand, interpret, and generate human language. It is
essential for communication between humans and computers.
Example: Virtual assistants like Amazon Alexa and Google Assistant use NLP to
understand voice commands and respond appropriately. NLP is also used in
chatbots, language translation, and sentiment analysis.
🧠 Knowledge Representation (KR)
Knowledge Representation involves storing information in a structured form so
that machines can reason and make decisions. It uses techniques like logic, rules,
and ontologies to represent real-world knowledge.
Example: Expert systems in healthcare use KR to represent medical knowledge
and assist doctors in diagnosis. For instance, a system can infer diseases based on
symptoms using logical rules.
🌐 Role in Intelligent Systems
These techniques often work together in intelligent systems:
• ML provides learning from data
• NLP enables human-computer interaction
• KR supports reasoning and decision-making
Combined Example: A smart healthcare assistant can use NLP to understand
patient queries, ML to predict possible diseases, and KR to provide logical
explanations and recommendations.
🧠 Conclusion
Machine Learning, NLP, and Knowledge Representation are fundamental AI
techniques that power modern intelligent systems. Their integration enables
systems to learn, understand language, and reason effectively, making AI
applications more accurate and human-like.
📊 Evaluation Rubric (10 Marks)
Explanation of ML (2) + Explanation of NLP (2) + Explanation of KR (2) +
Examples for each (3) + Integration in intelligent systems (1)
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 1942475cb5c9

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_IT_7037/Principles of Artificial Intelligence/ANS_Principles of Artificial Intelligence(702IT0C004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Principles of Artificial Intelligence
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
CO1 ; A Briefly elaborate PEAS parameters for AI agent for Personalized Music   5
BL2   Recommendation.
Ans: *[ PEAS full form-1M, Parameters covered-1M each]
1. Performance Measure (P)
Evaluates how well the system performs:
• Accuracy of recommendations
• User satisfaction (likes, skips, ratings)
•   Listening time / engagement
•   Diversity and novelty of songs
2. Environment (E)
The context in which the agent operates:
• Music streaming platform
•   Users with different preferences
• Music database (songs, artists, genres)
•   Context like time, mood, activity
3. Actuators (A)
Actions the system can perform:
• Recommend songs/playlists
•   Auto-play next track
•   Suggest artists or albums
•   Notify users with personalized suggestions
4. Sensors (S)
Data collected from the environment:
• User listening history
•   Likes, dislikes, skips
•   Search queries
Time of listening, device, location
********** 1 **********
--- page 2 ---
CO1 ; B Compare A* and AO* search based algorithm (Any 5 pts-5M)   5
BL4   Feature   A* Algorithm   AO* Algorithm
Graph Type   OR graph   AND-OR graph
Solution Type   Finds a single optimal   Finds an optimal solution graph
path
Node Types   Only OR nodes   Both AND and OR nodes
Evaluation   ( f(n) = g(n) + h(n) )   OR: min, AND: sum of child
Function   costs
Search Strategy   Expands lowest-cost   Expands most promising partial
node   solution graph
Backtracking   Not required   Required for cost updates
Complexity   Simpler   More complex
Application   Pathfinding (e.g., maps, Problem decomposition, planning
routing)
CO2 ; C   5
BL3   What is Overfitting in Decision Trees? How can it be avoided?
Overfitting in decision trees occurs when the model becomes excessively complex
and captures not only the underlying patterns in the training data but also noise and
outliers, leading to poor generalization on unseen data. This results in very high
accuracy on training data but low accuracy on test data. Overfitting typically
happens when the tree grows too deep with many branches. To avoid overfitting,
techniques such as pruning are used, including pre-pruning (limiting maximum
depth, minimum samples for split, etc.) and post-pruning (removing unnecessary
branches after full growth). Additionally, controlling tree depth, setting minimum
samples per node, using cross-validation, and applying ensemble methods like
Random Forest help improve model generalization.
Definition (1) + Causes/complexity & noise (1) + Effect/generalization & accuracy
gap (1) + Prevention methods/pruning & limits (1.5) + Advanced method (Random
Forest) (0.5)
CO3 ; D Differentiate between Information Retrieval and Information Extraction.   5
BL4
In Natural Language Processing, Information Retrieval (IR) and Information
Extraction (IE) are two different tasks. Information Retrieval refers to the process
of searching and retrieving relevant documents or data from a large collection
based on a user query, without modifying the content (e.g., search engines). In
contrast, Information Extraction involves automatically extracting structured
information such as entities, relationships, or facts from unstructured text. While
IR focuses on finding relevant documents, IE focuses on understanding and pulling
specific information from within those documents. Thus, IR deals with document-
level retrieval, whereas IE works at the content level to convert unstructured data
into structured form.
Definition of IR (1) + Definition of IE (1) + Key difference (retrieval vs
extraction) (1) + Level difference (document vs content) (1) + Example/clarity (1)
Q2   [20]
CO1 ; A Describe Depth-first search algorithm. Consider the graph shown below, start from 10
BL3   node A. identify the traversal path using depth First search algorithm
********** 2 **********
--- page 3 ---
Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by
going as deep as possible along each branch before backtracking. It starts from a
source node, visits an unvisited adjacent node, and continues this process
recursively until no unvisited nodes remain along the current path. Then it
backtracks to explore other branches. DFS can be implemented using a stack or
recursion.
🔍 DFS Traversal (Starting from A)
Assuming we visit adjacent nodes in a consistent order (e.g., left-to-right or
alphabetical), the traversal is:
A → C → F → G → D → E → B
🧠 Explanation of Traversal
•   Start at A
• Go deep: A → C
• From C → F
• From F → G
• From G → D
• From D → E
• From E → B
• No more unvisited nodes → stop
📊 Evaluation Rubric (5 Marks)
Definition of DFS (2) + Key idea (deep traversal & backtracking) (2) + Algorithm
approach (stack/recursion) (2) + Correct traversal path (3) + Clarity/step
explanation (1)
CO2 ; B Consider the following statement represent the given scenario involving a monkey, 10
BL3   a room, a hanging banana, a window, and a box.
• All monkeys are hungry.
• There exists a monkey at the door
• There exists a hungry monkey that cannot reach a hanging banana from the
ceiling.
• There exists a box at the window.
• All bananas are hanging from the ceiling.
Translate these sentences in predicate form.
[ All conversion-2M Each]
********** 3 **********
--- page 4 ---
Q3   [20]
CO1 ; A Explain the AO* search algorithm   10
BL4
*[Explanation-3M, Numerical solving stepwise 7M]
The AO* search algorithm is an informed search technique used for solving problems
represented as AND-OR graphs. In such graphs, some nodes represent OR choices (only
one path needs to be selected), while others represent AND conditions (all child nodes
must be solved together). AO* aims to find the optimal solution graph rather than just a
single path.
The algorithm starts from the initial node and expands the most promising node based on
heuristic values. Each node is assigned a cost estimate, and the algorithm continuously
updates these costs using a bottom-up approach. For OR nodes, the algorithm selects the
child with the minimum cost, whereas for AND nodes, it sums the costs of all child nodes.
As the search progresses, the best partial solution graph is maintained and updated until
an optimal solution is found. The algorithm also marks nodes as solved when all required
conditions are satisfied.
Feature   AO* Algorithm   A* Algorithm
Graph Type AND-OR Graph   OR Graph
Solution   Finds a solution graph   Finds a single path
Node Types AND nodes and OR nodes   Only OR nodes
Evaluation   Min (OR) and Sum (AND)   ( f(n) = g(n) + h(n) )
Expansion   Expands most promising partial   Expands lowest-cost
solution graph   node
Backtracking Required for cost updates   Not typically required
Step 1:
********** 4 **********
--- page 5 ---
Start from node A,
f(A⇢B) = g(B) + h(B)
= 1 + 5   ……here g(n)=1 is taken by default for path cost
= 6
f(A⇢C+D) = g(c) + h(c) + g(d) + h(d)
= 1 + 2 + 1 + 4   here we have added C & D because they are in AND
= 8
So, by calculation A⇢B path is chosen which is the minimum path, i.e f(A⇢B)
Here the value of E & F are calculated as follows,
f(B⇢E) = g(e) + h(e)
f(B⇢E) = 1 + 7
= 8
f(B⇢f) = g(f) + h(f)
f(B⇢f) = 1 + 9
= 10
So, by above calculation B⇢E path is chosen which is minimum path, i.e f(B⇢E) because
B's heuristic value is different from its actual value The heuristic is updated and the minimum
cost path is selected. The minimum value in our situation is 8. Therefore, the heuristic for A
must be updated due to the change in B's heuristic.
So we need to calculate it again.
f(A⇢B) = g(B) + updated h(B)
= 1 + 8
= 9
We have Updated all values in the above tree.
By comparing f(A⇢B) & f(A⇢C+D)
f(A⇢C+D) is shown to be smaller. i.e 8 < 9
Now explore f(A⇢C+D)
So, the current node is C
f(C⇢G) = g(g) + h(g)
f(C⇢G) = 1 + 3
= 4
f(C⇢H+I) = g(h) + h(h) + g(i) + h(i)
f(C⇢H+I) = 1 + 0 + 1 + 0
= 2
f(C⇢H+I) is selected as the path with the lowest cost and the heuristic is also left
unchanged because it matches the actual cost. Paths H & I are solved because the
heuristic for those paths is 0 but Path A⇢D needs to be calculated because it has an
AND.
f(D⇢J) = g(j) + h(j)
f(D⇢J) = 1 + 0
= 1
f(A⇢C+D) = g(c) + h(c) + g(d) + h(d)
= 1 + 2 + 1 + 1
= 5
********** 5 **********
--- page 6 ---
CO2 ; B Explain the concept of margin in SVM. Differentiate between hard margin and   10
BL4   soft margin SVM.
In Support Vector Machine (SVM), the margin refers to the distance between
the decision boundary (hyperplane) and the nearest data points from each class,
called support vectors. The main objective of SVM is to find a hyperplane that
maximizes this margin, as a larger margin leads to better generalization and
robustness of the model.
In a hard margin SVM, the model assumes that the data is perfectly linearly
separable and finds a hyperplane that separates all data points without any
misclassification. It strictly maximizes the margin with no tolerance for errors,
making it sensitive to noise and outliers. In contrast, a soft margin SVM allows
some misclassification by introducing slack variables, enabling the model to
handle non-linearly separable or noisy data. It balances between maximizing the
margin and minimizing classification errors using a regularization parameter (C).
📊 Evaluation Rubric (5 Marks)
Margin definition (2) + Role of margin/maximization (2) + Hard margin concept
(2) + Soft margin concept (2) + Key difference (strict vs tolerant) (2)
Q4   [20]
CO2 ; A Define the terms root node, attribute selection, and information gain in the context 10
BL5   of decision tree construction.
A small bank wants to decide whether to approve personal loans. They collected the
following small dataset of applicants:
Income   Credit Score   Loan Approved
Applicant
(High/Low)   (Good/Bad)   (Yes/No)
Ainal   High   Good   Yes
Badri   High   Bad   Yes
kartik   Low   Good   No
Sanjay   Low   Bad   No
1. Compute the information gain for the attributes Income and Credit Score.
Determine the best attribute for the root node.
2. Build a simple decision tree to classify whether a loan is approved.
*[ Each Def-2M each, IG calculation of each attributes-2M each, Identify best
attributes-2M, Tree-3M]
Root Node:
********** 6 **********
--- page 7 ---
The topmost node in a decision tree that represents the best attribute chosen to split the
dataset first. It divides the data into subsets based on the most informative feature.
Attribute Selection:
The process of choosing the best attribute at each step of tree construction. This is done
using measures like Information Gain, Gini Index, etc., to decide which attribute best
separates the data.
Information Gain:
Information Gain measures the reduction in entropy (uncertainty) after splitting a dataset
on an attribute. It is calculated as:
Entropy of Dataset:
Information Gain for Income
Split by Income:
High:
•   Yes = 2, No = 0 → Entropy = 0
Low:
•   Yes = 0, No = 2 → Entropy = 0
Information Gain for Credit Score
Split by Credit Score:
Good:
•   Yes = 1, No = 1 → Entropy = 1
Bad:
•   Yes = 1, No = 1 → Entropy = 1
Best Attribute for Root Node
• Income (IG = 1) is the best attribute
•   Credit Score (IG = 0) is not useful
Root Node = Income
Income
/   \
High   Low
CO2 ; B Explain the Minimax algorithm used in two-player games. How does Alpha-Beta   10
BL4   Pruning improve its efficiency?
The Minimax algorithm is used in two-player zero-sum games (like tic-tac-toe or
chess) to determine the optimal move by assuming both players play optimally. It
builds a game tree where one player (MAX) tries to maximize the score, while the
opponent (MIN) tries to minimize it. The algorithm recursively explores all
possible moves, evaluates terminal states using a utility function, and chooses the
move that gives the best worst-case outcome.
Alpha-Beta Pruning is an optimization technique for Minimax that reduces the
number of nodes evaluated in the game tree. It introduces two values: alpha (the
********** 7 **********
--- page 8 ---
best value MAX can achieve so far) and beta (the best value MIN can achieve so
far). If at any point alpha ≥ beta, further exploration of that branch is stopped
(pruned), as it will not affect the final decision. This significantly improves
efficiency without changing the final result of the algorithm.
Minimax definition (2) + MAX/MIN roles & game tree (2) + Recursive
evaluation/utility (2) + Alpha-Beta concept (2) + Efficiency improvement/pruning
condition (2)
Q5   [20]
CO2 ; A Define machine learning and its types.   10
BL3   Identify from the following is/are examples of supervised, unsupervised learning.
1.   Predicting rainfall based on historical data
2.   Predicting credit approval based on historical data
3.   Predicting the time (in days) a PhD student will take to complete his/her
thesis to earn a degree based on the historical data such as qualifications,
department, institute, research area, and time taken by other scholars to earn
the degree.
4.   Predicting if a customer is going to return or keep a particular product he/she
purchased from e-commerce website based on the historical data about the
customer purchases and the particular product.
*[Def-2M, Identification-2M each]
Machine learning is the science of getting computers to act by feeding them data
and letting them learn few tricks on their own without being explicitly
programmed.
1. Predicting rainfall based on historical data -------supervised
2. Predicting credit approval based on historical data---- supervised
3. Predicting the time (in days) a PhD student will take to complete his/her
thesis to earn a degree based on the historical data such as qualifications,
department, institute, research area, and time taken by other scholars to
earn the degree. ---- unsupervised
Predicting if a customer is going to return or keep a particular product he/she
purchased from e-commerce website based on the historical data about the
customer purchases and the particular product. ----supervised
CO3 ; B Describe the complete NLP pipeline. Explain each stage such as tokenization,   10
BL2   stemming, lemmatization, stop-word removal, and POS tagging
✍️ Answer (10 Marks)
The Natural Language Processing (NLP) pipeline is a sequence of steps used to
process raw text into a structured format so that machines can understand and
analyze human language. It involves several preprocessing stages that clean and
transform text before applying machine learning models.
Tokenization is the first step, where the input text is divided into smaller units
called tokens, such as words or sentences. This helps in breaking down
unstructured text into manageable pieces for further processing.
Stop-word removal is the process of eliminating common words like is, the, and,
in, which do not contribute significant meaning to the text. Removing these words
reduces data size and improves processing efficiency.
********** 8 **********
--- page 9 ---
Stemming is a technique used to reduce words to their root form by removing
suffixes. It is a rule-based process and may produce words that are not
grammatically correct. For example, words like running, runs, runner may be
reduced to run.
Lemmatization improves upon stemming by converting words into their correct
base or dictionary form (lemma) using vocabulary and grammatical analysis. For
example, better becomes good and running becomes run. It produces more
meaningful results compared to stemming.
Part-of-Speech (POS) tagging assigns grammatical categories to each word in a
sentence, such as noun, verb, adjective, etc. This helps in understanding the
syntactic structure and meaning of the sentence.
Overall, the NLP pipeline transforms raw text into a structured and meaningful
representation, enabling machines to perform tasks like text classification,
sentiment analysis, and information extraction effectively.
📊 Evaluation Rubric (10 Marks)
Definition of NLP pipeline (2) + Tokenization (2) + Stop-word removal (1.5) +
Stemming (1.5) + Lemmatization (1.5) + POS tagging (1.5)
Q6   [20]
CO1 ; A Differentiate propositional logic with First order logic. List the Inference rules   10
BL4   along with suitable examples for first order logic.
✍️ Answer (10 Marks)
In Artificial Intelligence, both Propositional Logic and First-Order Logic
(FOL) are used for knowledge representation, but they differ in expressiveness and
capability.
Propositional Logic deals with simple statements that are either true or false,
without considering internal structure. It uses propositional variables (P, Q, R) and
logical connectives like AND, OR, NOT. For example, P: It is raining. It cannot
represent relationships or quantify objects.
First-Order Logic (FOL) is more expressive and allows representation of objects,
properties, relations, and quantifiers. It uses predicates, variables, constants, and
quantifiers like ∀ (for all) and ∃ (there exists). For example, ∀x Human(x) →
Mortal(x) represents that all humans are mortal.
Difference: Propositional logic is simple but limited, while FOL is more powerful
and can represent complex relationships and general rules about objects in a
domain.
📌 Inference Rules in First-Order Logic (with Examples)
1. Universal Instantiation (UI)
From a universal statement, we can infer for a specific instance.
Example: ∀x Human(x) → Mortal(x)
⇒ Human(Socrates) → Mortal(Socrates)
2. Existential Instantiation (EI)
From an existential statement, we assume a specific instance.
Example: ∃x Student(x)
⇒ Student(A) (A is some specific student)
3. Universal Generalization (UG)
If something is true for an arbitrary element, it is true for all.
********** 9 **********
--- page 10 ---
Example: Human(x) → Mortal(x)
⇒ ∀x Human(x) → Mortal(x)
4. Existential Generalization (EG)
From a specific instance, we can generalize existence.
Example: Student(Ram)
⇒ ∃x Student(x)
5. Modus Ponens
If P → Q and P is true, then Q is true.
Example: Human(Socrates) → Mortal(Socrates), Human(Socrates)
⇒ Mortal(Socrates)
🧠 Conclusion
Propositional logic is limited to simple true/false statements, whereas First-Order
Logic provides a richer framework to represent real-world knowledge using objects
and relationships. Inference rules in FOL help derive new facts logically from
existing knowledge.
📊 Evaluation Rubric (10 Marks)
Definition of Propositional Logic (2) + Definition of FOL (2) + Key differences
(2) + Inference rules explanation (3) + Examples (1)
CO3 ; B Explain N-gram Language Models. Discuss unigram, bigram, and trigram models   10
BL2   along with their advantages and limitations.
✍️ Answer (10 Marks)
N-gram language models are probabilistic models used in Natural Language
Processing (NLP) to predict the likelihood of a sequence of words. They assume
that the probability of a word depends only on the previous N−1 words (Markov
assumption). Thus, instead of considering the entire sentence, the model simplifies
computation by using limited context.
🔤 Types of N-gram Models
1. Unigram Model (N = 1)
In a unigram model, each word is considered independent of others. The
probability of a sentence is the product of individual word probabilities.
Example:
P(“I love NLP”) = P(I) × P(love) × P(NLP)
Advantage: Simple and requires less data
Limitation: Ignores context, leading to poor accuracy
2. Bigram Model (N = 2)
In a bigram model, the probability of a word depends on the previous one word.
Example:
P(“I love NLP”) = P(I) × P(love|I) × P(NLP|love)
Advantage: Captures some context, better than unigram
Limitation: Still limited context, data sparsity problem
3. Trigram Model (N = 3)
In a trigram model, the probability of a word depends on the previous two words.
Example:
P(“I love NLP”) = P(I) × P(love|I) × P(NLP|I, love)
********** 10 **********
--- page 11 ---
Advantage: Captures more context, more accurate
Limitation: Requires large data, higher computational cost, sparsity increases
⚖️ Advantages of N-gram Models
• Simple and easy to implement
• Computationally efficient for small N
• Useful baseline for language modeling tasks
⚠️ Limitations of N-gram Models
• Data sparsity: Many word combinations may not appear in training data
• Limited context: Cannot capture long-range dependencies
• Storage issues: Large memory required for higher N
• Poor handling of unseen words (out-of-vocabulary problem)
🧠 Conclusion
N-gram models are foundational techniques in NLP that estimate word sequence
probabilities using limited context. While unigram, bigram, and trigram models
progressively improve context understanding, they suffer from sparsity and
scalability issues, which led to the development of more advanced models like
neural language models.
📊 Evaluation Rubric (10 Marks)
Definition of N-gram model (2) + Unigram explanation (2) + Bigram explanation
(2) + Trigram explanation (2) + Advantages & limitations (2)
Q7   [20]
CO2 ; A Explain the architecture of an Artificial Neural Network. Discuss different types   10
BL2   of layers (input, hidden, output) and their roles.
✍️ Answer (10 Marks)
An Artificial Neural Network (ANN) is a computational model inspired by the
human brain, consisting of interconnected nodes (neurons) organized in layers. It is
widely used in machine learning to recognize patterns, classify data, and make
predictions. The architecture of an ANN defines how neurons are arranged and
how information flows between layers.
🧠 Architecture of ANN
An ANN typically consists of three main types of layers: input layer, hidden
layer(s), and output layer. Each neuron receives inputs, applies weights, sums
them, and passes the result through an activation function to produce an output.
🔹 1. Input Layer
The input layer is the first layer of the network that receives raw data from the
external environment. Each neuron in this layer represents a feature of the input
dataset. It does not perform computations but simply passes the input values to the
next layer.
Role:
• Accepts input data
********** 11 **********
--- page 12 ---
•   Distributes data to hidden layers
🔹 2. Hidden Layer(s)
The hidden layers are intermediate layers between input and output layers. These
layers perform most of the computations in the network. Each neuron calculates a
weighted sum of inputs, applies an activation function (such as ReLU or sigmoid),
and passes the result forward.
Role:
•   Extract features and patterns
• Perform nonlinear transformations
• Enable learning of complex relationships
🔹 3. Output Layer
The output layer is the final layer that produces the result of the network. The
number of neurons depends on the type of problem (e.g., one neuron for
regression, multiple for classification). It uses appropriate activation functions like
sigmoid or softmax.
Role:
• Produces final prediction/output
• Maps processed data to desired format
⚙️ Additional Components
• Weights and Biases: Control the strength of connections
• Activation Functions: Introduce non-linearity
• Loss Function: Measures error
• Backpropagation: Updates weights to minimize error
🧠 Conclusion
The ANN architecture consists of layered neurons where the input layer receives
data, hidden layers process and learn patterns, and the output layer produces the
final result. This layered structure enables neural networks to model complex real-
world problems effectively.
📊 Evaluation Rubric (10 Marks)
Definition of ANN (2) + Architecture explanation (2) + Input layer role (2) +
Hidden layer role (2) + Output layer role (2)
CO2 ; B Explain the role of AI techniques such as Machine Learning, Natural Language   10
BL5   Processing, and Knowledge representation in modern applications. Illustrate with
examples how these techniques are used in intelligent systems.
✍️ Answer (10 Marks)
Artificial Intelligence (AI) uses various techniques such as Machine Learning
(ML), Natural Language Processing (NLP), and Knowledge Representation
(KR) to build intelligent systems that can learn, reason, and interact with humans.
These techniques play a crucial role in modern applications across multiple
domains.
********** 12 **********
--- page 13 ---
🤖 Machine Learning (ML)
Machine Learning enables systems to learn patterns from data and make
predictions or decisions without explicit programming. It is widely used in
applications such as recommendation systems, fraud detection, and image
recognition.
Example: Platforms like Netflix use ML algorithms to recommend movies based
on user preferences and viewing history. Similarly, email services use ML for
spam detection.
💬 Natural Language Processing (NLP)
NLP allows machines to understand, interpret, and generate human language. It is
essential for communication between humans and computers.
Example: Virtual assistants like Amazon Alexa and Google Assistant use NLP to
understand voice commands and respond appropriately. NLP is also used in
chatbots, language translation, and sentiment analysis.
🧠 Knowledge Representation (KR)
Knowledge Representation involves storing information in a structured form so
that machines can reason and make decisions. It uses techniques like logic, rules,
and ontologies to represent real-world knowledge.
Example: Expert systems in healthcare use KR to represent medical knowledge
and assist doctors in diagnosis. For instance, a system can infer diseases based on
symptoms using logical rules.
🌐 Role in Intelligent Systems
These techniques often work together in intelligent systems:
• ML provides learning from data
• NLP enables human-computer interaction
• KR supports reasoning and decision-making
Combined Example: A smart healthcare assistant can use NLP to understand
patient queries, ML to predict possible diseases, and KR to provide logical
explanations and recommendations.
🧠 Conclusion
Machine Learning, NLP, and Knowledge Representation are fundamental AI
techniques that power modern intelligent systems. Their integration enables
systems to learn, understand language, and reason effectively, making AI
applications more accurate and human-like.
📊 Evaluation Rubric (10 Marks)
Explanation of ML (2) + Explanation of NLP (2) + Explanation of KR (2) +
Examples for each (3) + Integration in intelligent systems (1)
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 9f327c94971f

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_IT_7001/Principles of Artificial Intelligence/ANS_Principles of Artificial Intelligence(702IT0C035)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Jul 2026
- Text: mixed (15 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Principles of Artificial Intelligence
Date: 13 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
CO1;   A   Identify PEAS parameters for the following AI agent types   5
BL2   a) Virtual Personal Assistant.
b) chess playing
*[ Part a -5M , Part b -5M]
Virtual Personal Assistant
• Performance Measure (P):
Task accuracy, response time, user satisfaction, successful task completion
• Environment (E):
User devices, internet, apps (email, calendar), real-world user context
• Actuators (A):
Voice responses, notifications, scheduling actions, sending messages
• Sensors (S):
Voice input, text commands, user data, calendar, emails
Chess Playing Agent
• Performance Measure (P):
Winning the game, minimizing moves, strategic advantage
• Environment (E):
Chessboard, opponent, game rules
• Actuators (A):
Moving pieces on the board
Sensors (S):
Board configuration, opponent moves
CO1 ;   B Compare Informed & Uninformed search with example   5
BL4
✍️ Answer (5 Marks)
In Artificial Intelligence, search algorithms are broadly classified into Uninformed
search and Informed search based on the knowledge they use.
Uninformed search (Blind search) does not use any additional information about the
problem domain. It explores the search space using only the initial state, goal state,
********** 1 **********
--- page 2 ---
and possible actions. Examples include Breadth-First Search (BFS) and Depth-First
Search (DFS). These methods may explore many unnecessary nodes, making them less
efficient.
Example: In a maze, BFS explores all possible paths level by level without knowing
which direction leads closer to the goal.
Informed search (Heuristic search) uses additional knowledge in the form of a
heuristic function to guide the search towards the goal more efficiently. It selects paths
that appear more promising, reducing the number of explored nodes. Examples include
A* search and Greedy Best-First Search.
Example: In the same maze, A* uses the estimated distance to the goal to choose the
best path, reaching the solution faster.
Difference: Uninformed search is simple but inefficient, while informed search is
more efficient due to the use of heuristics.
📊 Evaluation Rubric (5 Marks)
Definition of Uninformed search (1) + Definition of Informed search (1) + Key
difference (1) + Examples (1) + Clarity (1)
CO2 ;   C   Explain the structure and working of a Bayesian Network.   5
BL2
✍️ Answer (5 Marks)
A Bayesian Network (also called a Belief Network) is a probabilistic graphical model
that represents a set of variables and their conditional dependencies using a directed
acyclic graph (DAG). Each node in the graph represents a random variable, and the
directed edges represent probabilistic dependencies between variables. Associated
with each node is a conditional probability table (CPT) that quantifies the effect of
parent nodes on that variable.
Structure:
• Nodes → random variables
•   Directed edges → dependencies/causal relationships
• CPT → probability of a node given its parents
Working:
A Bayesian Network works based on Bayes’ theorem, where the joint probability of
all variables is computed as the product of conditional probabilities of each node given
its parents. When evidence is provided (e.g., some variables are known), the network
updates the probabilities of other variables using probabilistic inference.
Example:
In a medical diagnosis system, variables like Disease, Symptoms, and Test Results are
connected. If symptoms are observed, the network updates the probability of a disease
using conditional probabilities.
📊 Evaluation Rubric (5 Marks)
Definition of Bayesian Network (1) + Structure (nodes, edges, CPT) (1.5) + Working
(probability & inference) (1.5) + Example (1)
CO3 ;   D What are Language Models? Explain n-gram models with example.   5
BL2
✍️ Answer (5 Marks)
Language Models are used in Natural Language Processing (NLP) to estimate the
probability of a sequence of words and to predict the next word in a sentence. They
help machines understand and generate human language by learning patterns from text
data.
One common type is the N-gram model, which assumes that the probability of a word
depends only on the previous (N−1) words (Markov assumption).
********** 2 **********
--- page 3 ---
• Unigram (N=1): Each word is independent.
Example: P(“I love AI”) = P(I) × P(love) × P(AI)
• Bigram (N=2): Depends on one previous word.
Example: P(“I love AI”) = P(I) × P(love|I) × P(AI|love)
• Trigram (N=3): Depends on two previous words.
Example: P(“I love AI”) = P(I) × P(love|I) × P(AI|I, love)
Conclusion: N-gram models are simple and effective for basic language prediction
tasks, but they have limitations such as limited context and data sparsity.
📊 Evaluation Rubric (5 Marks)
Definition of Language Model (1.5) + N-gram concept (1.5) + Examples (1.5) +
Conclusion/limitation (0.5)
Q2   [20]
CO1 ;   A   Define alpha (α) and beta (β) values in the Alpha–Beta Pruning algorithm. Explain when 10
BL4   pruning occurs in the Alpha–Beta algorithm. Apply the Alpha–Beta Pruning algorithm
to the given game tree. Clearly indicate which branches are pruned, assuming left-to-
right traversal.
*[ Defination-2M, Condition-1M, Stepwise updation of α and β value -7M]
Alpha (α) represents the best (maximum) value that the maximizing player can
guarantee so far along the current path. In other words, it is the highest value found at
any point for the maximizer, and the algorithm tries to increase this value as it explores
more nodes.
Beta (β) represents the best (minimum) value that the minimizing player can
guarantee so far. It is the lowest value found so far for the minimizer, and the algorithm
attempts to decrease this value during exploration.
Pruning occurs when it is determined that further exploration of a node will not affect
the final decision. Specifically, pruning happens when:
********** 3 **********
--- page 4 ---
CO2 ;   B   Consider the following statement   10
BL5   1. Sunil likes all kind of food.
2. Apple and vegetable are food.
3. Anything anyone eats and not killed is food.
4. Anil eats peanuts and still alive.
5. Sohan eats everyting that Anil eats.
6. Sunil like peanuts.
a) Convert to FOL
b) Convert FOL to CNF
c) Prove that “ Sunil likes Peanuts” using the resolution
Draw Resolution Tree.
Answer:
FOL ( 2M)
********** 4 **********
--- page 5 ---
1. Wx: food(x)>likes(Sunil, x)
2. food(apple) A
food(vegetable)
3. Wx Vy: eats(x,y)A
- killed(x)>food(y)

4. eats(Anil , Peanut)A
alive(Anil)

5. Wx: eats(Anil, x) >
eats(Sohan, x)

6.   Likes(Sunil, Peanut)

° Wx : - killed(x)>alive(x)

° Vx : alive (x) >-killed (x)

(added predicates)

CNF: (4M)

1. - food(x) V likes(Sunil, x)
2. food(Apple)
3. food(vegetables)

4. -eats(y, z) V killed(y) V
food(z)

5. eats (Anil, Peanuts)

6. alive(Anil)

7. - eats(Anil, w) V
eats(Sohan, w)

8. killed(g) V alive(g)

9. - alive(k) V - killed(k)

10. likes(Sunil, Peanuts)

Resolution Tree (4M)

~likes(Sunil, Peanuts) = food(x) V likes(Sunil, x)
{Peanuts/x}

+ food(Peanuts) > eats(y, z) V killed(y) V food(z)

{Peanuts/z}
> eats(y, Peanuts) V killed(y) eats (Anil, Peanuts)
{Anil/y}
Killed(Anil) = alive(k) V ~ killed(k)
{Anil/k}
> alive(Anil) alive(Anil)
(6) Null

Q3

[20]

FIC DI EH ar
--- page 6 ---
CO1 ;   A   Describe Breadth-first search algorithm. Consider the graph shown below, start from 10
BL3   node 0. identify the traversal path using Breadth First search algorithm.
*[ Explanation-4M, Numerical stepwise explanation-6M]
Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by going
as deep as possible along each branch before backtracking. It uses either a stack data
structure or recursion. The algorithm starts from a given source node, marks it as visited,
and then recursively visits one of its unvisited adjacent nodes. This process continues
until it reaches a node that has no unvisited neighbors. At that point, it backtracks to the
previous node and explores other unvisited neighbors. This continues until all nodes in
the graph have been visited.
For the given graph, starting from node 0, DFS begins at node 0 and moves to node 1
(one of its adjacent nodes). From node 1, it proceeds deeper to node 2, then to node 4,
and then to node 6, following one path as far as possible. Since node 6 has no unvisited
adjacent nodes left, the algorithm backtracks to node 4, then to node 2, and continues
exploring the next unvisited neighbor, which is node 5. After visiting node 5, it
backtracks again to node 2, then to node 1, and finally visits node 3, which was not yet
explored.
Thus, the Depth-First Search traversal starting from node 0 is:
DFS traversal can vary depending on the order in which adjacent nodes are chosen
CO1;   B   Explain the concept of Support Vector Machines (SVM). How does it perform   10
BL4   classification using a hyperplane?
✍️ Answer (10 Marks)
Support Vector Machine (SVM) is a supervised machine learning algorithm used for
classification and regression tasks. It works by finding an optimal boundary, called a
hyperplane, that separates data points of different classes with the maximum possible
margin. SVM is particularly effective in high-dimensional spaces and is widely used
for classification problems.
📐 Concept of Hyperplane in SVM
A hyperplane is a decision boundary that divides the dataset into different classes.
•   In 2D → it is a line
•   In 3D → it is a plane
•   In higher dimensions → it is called a hyperplane
SVM selects the hyperplane that maximizes the margin, i.e., the distance between the
hyperplane and the nearest data points from each class.
📏 Role of Support Vectors
The data points that lie closest to the hyperplane are called support vectors. These
points are critical because they determine the position and orientation of the
hyperplane. Removing them would change the decision boundary.
********** 6 **********
--- page 7 ---
⚙️ Working of SVM for Classification
1. The algorithm identifies all possible hyperplanes that can separate the classes.
2.   It selects the hyperplane with the maximum margin (best separation).
3. The decision function classifies new data points based on which side of the
hyperplane they fall.
Mathematically, the hyperplane can be represented as:
w·x + b = 0
where w is the weight vector, x is the input, and b is the bias.
🔄 Handling Non-Linearly Separable Data
When data is not linearly separable, SVM uses the kernel trick to map data into a
higher-dimensional space where a linear hyperplane can separate the classes. Common
kernels include linear, polynomial, and radial basis function (RBF).
🧠 Conclusion
SVM is a powerful classification technique that finds the optimal hyperplane with
maximum margin using support vectors. Its ability to handle both linear and non-linear
data makes it widely applicable in real-world problems like image classification and
text categorization.
📊 Evaluation Rubric (10 Marks)
Definition of SVM (2) + Hyperplane concept (2) + Margin & support vectors (2) +
Working steps (2) + Kernel/non-linear handling (2)
Q4   [20]
CO2;   A   Distinguish between supervised and unsupervised learning algorithm. Illustrate with   10
BL4   an example
✍️ Answer (10 Marks)
Supervised learning and unsupervised learning are two main types of machine
learning algorithms, differing in how they learn from data.
Supervised learning involves training a model on labeled data, where both input and
corresponding output are known. The algorithm learns a mapping from input to output
and is used for tasks like classification and regression.
Example: Predicting whether an email is spam or not using labeled examples of spam
and non-spam emails.
Unsupervised learning, on the other hand, works with unlabeled data, where the
model tries to find hidden patterns or structures in the data without predefined outputs.
It is mainly used for clustering and association tasks.
Example: Grouping customers into different segments based on purchasing behavior
without prior labels.
🔍 Key Differences
•   Supervised learning uses labeled data, while unsupervised uses unlabeled
data
•   Supervised learning predicts outputs; unsupervised discovers patterns
•   Supervised tasks: classification, regression
•   Unsupervised tasks: clustering, association
********** 7 **********
--- page 8 ---
🧠 Conclusion
Supervised learning is useful when labeled data is available and prediction is required,
whereas unsupervised learning is useful for discovering hidden structures in data. Both
techniques are essential in building intelligent systems.
📊 Evaluation Rubric (10 Marks)
Definition of supervised learning (2) + Definition of unsupervised learning (2) + Key
differences (3) + Examples (2) + Conclusion/clarity (1)
CO1 ;   B   Illustrate the working of Hill Climbing using a suitable problem. Why does it fail in   10
BL4   certain situations? Discuss methods to overcome these failures
✍️ Answer (10 Marks)
Hill Climbing is a heuristic search algorithm used in Artificial Intelligence for
optimization problems. It starts with an initial solution and iteratively moves to a
neighboring solution that has a better value (higher for maximization or lower for
minimization). The process continues until no better neighboring state is found, at
which point the algorithm stops.
🔍 Working of Hill Climbing (Example)
Consider the problem of finding the maximum value of a function (e.g., maximizing
f(x)).
•   Start with an initial value of x
•   Evaluate neighboring values (e.g., x+1, x−1)
• Move to the neighbor with a higher value
•   Repeat until no improvement is possible
Illustration:
If we want to reach the highest peak of a hill:
•   Start at a random point
• Move uphill step by step
•   Stop when reaching a peak (no higher neighbor exists)
⚠️ Limitations / Failures
Hill Climbing may fail in the following situations:
1. Local Maximum – The algorithm may stop at a peak that is not the global
maximum
2. Plateau – A flat region where neighboring states have the same value, causing
no progress
3. Ridge Problem – Narrow paths where the algorithm struggles to find the
correct direction
🛠️ Methods to Overcome Failures
1. Random Restart Hill Climbing
o Run the algorithm multiple times with different initial states
o   Increases chance of finding global optimum
2. Simulated Annealing
o Allows occasional downhill moves to escape local maxima
3. Stochastic Hill Climbing
********** 8 **********
--- page 9 ---
o Chooses random neighbors instead of the best one
4. Sideways Moves
o Allows movement across plateaus for a limited number of steps
🧠 Conclusion
Hill Climbing is a simple and efficient optimization technique, but it may get stuck in
local optima or flat regions. Advanced strategies like random restart and simulated
annealing help improve its performance and reliability.
📊 Evaluation Rubric (10 Marks)
Definition of Hill Climbing (2) + Working with example (3) + Limitations (3) +
Methods to overcome (2)
Q5   [20]
CO2 ;   A   Define the following term in context to decision tree w.r.t suitable example:   10
BL2   a) Information Gain
b) Entropy
✍️ Answer
a) Information Gain (5 Marks)
Information Gain is a measure used in decision trees to determine which attribute
should be selected for splitting the data at each step. It calculates the reduction in
entropy after splitting a dataset based on a particular attribute. The attribute with the
highest information gain is chosen as the best split.
Mathematically:
Information Gain = Entropy (parent) − Weighted Entropy (children)
Example:
Consider a dataset of weather conditions to decide whether to play tennis. If splitting
on the attribute Outlook (Sunny, Rainy, Overcast) reduces uncertainty significantly
compared to other attributes, then Outlook will have the highest information gain and
will be selected as the root node.
b) Entropy (5 Marks)
Entropy is a measure of uncertainty or impurity in a dataset. It indicates how mixed
the data is. If all examples belong to the same class, entropy is 0 (pure). If the data is
evenly distributed among classes, entropy is maximum.
Mathematically:
Entropy = − Σ p(x) log₂ p(x)
Example:
In a dataset of 10 samples:
• 5 are “Yes” and 5 are “No” → High entropy (maximum uncertainty)
• 10 are “Yes” and 0 are “No” → Entropy = 0 (no uncertainty)
🧠 Conclusion
Entropy measures impurity in the dataset, while Information Gain measures how much
that impurity is reduced after a split. Decision trees use these concepts to build
efficient and accurate models.
📊 Evaluation Rubric
Information Gain: Definition (2) + Formula (1) + Example (2)
Entropy: Definition (2) + Formula (1) + Example (2)
********** 9 **********
--- page 10 ---
CO3 ;   B   Discuss various techniques used in Information Extraction. Explain their roles in   10
BL4   extracting meaningful information from text.
✍️ Answer (10 Marks)
Information Extraction (IE) is a task in Natural Language Processing (NLP) that
involves automatically extracting structured information such as entities, relationships,
and facts from unstructured text. Various techniques are used to identify and organize
meaningful information.
🔍 Techniques in Information Extraction
1. Named Entity Recognition (NER)
NER identifies and classifies entities like names of people, organizations, locations,
dates, etc.
Role: Converts raw text into structured entities.
Example: “Elon Musk founded SpaceX” → Elon Musk (Person), SpaceX
(Organization)
2. Part-of-Speech (POS) Tagging
POS tagging assigns grammatical labels (noun, verb, adjective, etc.) to words.
Role: Helps in understanding sentence structure and identifying important components
for extraction.
3. Chunking (Shallow Parsing)
Chunking groups words into meaningful phrases such as noun phrases or verb phrases.
Role: Helps identify relationships between words and extract relevant phrases.
4. Dependency Parsing
This technique analyzes grammatical relationships between words in a sentence.
Role: Helps in identifying subject-object relationships and extracting relations.
Example: “Ram eats apple” → Ram (subject), apple (object)
5. Rule-Based Techniques
These use predefined linguistic rules and patterns to extract information.
Role: Useful for domain-specific extraction where patterns are known.
6. Machine Learning-Based Techniques
Models are trained on annotated data to automatically learn extraction patterns.
Role: Improves accuracy and adaptability across different domains.
7. Template Filling
Extracted information is organized into predefined templates.
Role: Converts extracted data into structured formats (e.g., forms or databases).
🧠 Conclusion
Information Extraction combines linguistic and machine learning techniques to
transform unstructured text into structured knowledge. Techniques like NER, POS
tagging, and parsing play a key role in identifying entities and relationships, enabling
applications such as chatbots, search engines, and knowledge bases.
📊 Evaluation Rubric (10 Marks)
Definition of IE (2) + Explanation of techniques (6) + Roles of techniques (1) +
Example/clarity (1)
Q6   [20]
CO2 ;   A   Explain quantifiers in First-Order Logic. Discuss universal and existential quantifiers   10
BL2   with suitable examples.
********** 10 **********
--- page 11 ---
✍️ Answer (10 Marks)
In First-Order Logic (FOL), quantifiers are used to express statements about a
group of objects in a domain. They specify how many elements satisfy a given
predicate, making FOL more expressive than propositional logic. The two main types
of quantifiers are universal quantifier (∀) and existential quantifier (∃).
🔹 Universal Quantifier (∀)
The universal quantifier (∀) means “for all” and is used to state that a property holds
for every element in the domain.
Form: ∀x P(x)
This means P(x) is true for all values of x.
Example:
∀x Human(x) → Mortal(x)
This means “All humans are mortal.”
Role:
•   Represents general rules or universal truths
• Widely used in knowledge representation
🔹 Existential Quantifier (∃)
The existential quantifier (∃) means “there exists” and is used to indicate that at least
one element in the domain satisfies a given condition.
Form: ∃x P(x)
This means there exists at least one x for which P(x) is true.
Example:
∃x Student(x) ∧ Intelligent(x)
This means “There exists a student who is intelligent.”
Role:
•   Represents existence of at least one object
•   Useful for expressing partial or specific knowledge
🔍 Key Difference
• ∀ applies to all elements in the domain
• ∃ applies to at least one element
• ∀ expresses generalization, while ∃ expresses existence
🧠 Conclusion
Quantifiers enhance the power of First-Order Logic by allowing statements about
groups of objects. Universal quantifiers express general rules, while existential
quantifiers indicate the existence of specific instances, making FOL suitable for
representing real-world knowledge.
📊 Evaluation Rubric (10 Marks)
Definition of quantifiers (2) + Universal quantifier explanation (3) + Existential
quantifier explanation (3) + Examples (1) + Difference/conclusion (1)
CO3 ;   B   Explain the Bag-of-Words model. How are documents converted into vectors? Discuss 10
BL4   its limitations and improvements ?
********** 11 **********
--- page 12 ---
✍️ Answer (10 Marks)
The Bag-of-Words (BoW) model is a simple technique used in Natural Language
Processing (NLP) to represent text data as numerical vectors. In this model, a
document is treated as a “bag” of words, ignoring grammar and word order, and only
the frequency of words is considered.
🔤 How Documents are Converted into Vectors
1. Text Preprocessing
o Convert text to lowercase, remove punctuation, stop-words, etc.
2. Vocabulary Creation
o Create a list of all unique words from the dataset (called vocabulary)
3. Vector Representation
o Each document is represented as a vector of word counts based on the
vocabulary
Example:
Documents:
D1: “I love AI”
D2: “AI is powerful”
Vocabulary: [I, love, AI, is, powerful]
Vectors:
• D1 → [1, 1, 1, 0, 0]
• D2 → [0, 0, 1, 1, 1]
⚠️ Limitations of Bag-of-Words
•   Ignores word order → “AI is good” and “good is AI” are treated the same
• No semantic meaning → cannot understand synonyms or context
• High dimensionality → large vocabulary leads to large vectors
•   Sparsity → most values in vectors are zero
🚀 Improvement: TF-IDF
TF-IDF (Term Frequency–Inverse Document Frequency) improves BoW by
assigning weights to words based on importance.
• TF (Term Frequency): Frequency of a word in a document
• IDF (Inverse Document Frequency): Measures how rare a word is across
documents
Words that appear frequently in one document but rarely across others get higher
weight.
Advantage over BoW:
• Reduces importance of common words
•   Highlights meaningful and distinctive terms
🧠 Conclusion
The Bag-of-Words model is a basic and efficient method for text representation, but it
has limitations in capturing meaning and context. Techniques like TF-IDF improve its
********** 12 **********
--- page 13 ---
effectiveness by weighting important words, making it more suitable for tasks like text
classification and information retrieval.
📊 Evaluation Rubric (10 Marks)
Definition of BoW (2) + Vector conversion process (3) + Example (1) + Limitations
(2) + TF-IDF explanation (2)
Q7   [20]
CO2 ;   A   Design a Perceptron model for implementing the AND gate. Derive suitable weights   10
BL3   and bias, and verify the output using all input combinations.
✍️ Answer
A Perceptron is a simple neural network model used for binary classification. It
computes a weighted sum of inputs and applies an activation function (step function)
to produce an output.
🔢 Step 1: AND Gate Truth Table
x₁   x₂   Output (y)
0   0   0
0   1   0
1   0   0
1   1   1
⚙️ Step 2: Perceptron Model
Output is given by:
y = 1 if (w₁x₁ + w₂x₂ + b ≥ 0), else 0
🎯 Step 3: Choose Weights and Bias
For AND gate, suitable values are:
• w₁ = 1
• w₂ = 1
• b = −1.5
✅ Step 4: Verification
Now compute output for all inputs:
1. x₁=0, x₂=0
Net = (1×0 + 1×0 − 1.5) = −1.5 → y = 0
2. x₁=0, x₂=1
Net = (1×0 + 1×1 − 1.5) = −0.5 → y = 0
3. x₁=1, x₂=0
Net = (1×1 + 1×0 − 1.5) = −0.5 → y = 0
4. x₁=1, x₂=1
Net = (1×1 + 1×1 − 1.5) = 0.5 → y = 1
🧠 Conclusion
The perceptron with weights w₁ = 1, w₂ = 1 and bias b = −1.5 correctly implements the
AND gate, producing the desired output for all input combinations.
********** 13 **********
--- page 14 ---
📊 Evaluation Rubric (Typical 5–10 Marks)
Truth table (2) + Model/formula (2) + Weights & bias selection (2) + Verification (3)
+ Conclusion (1)
CO2 ;   B   Explain how AI techniques such as Machine Learning, Natural Language Processing   10
BL5   (NLP), and Knowledge Representation are applied in a smart virtual assistant
(Siri/Google Assistant).
Illustrate how each technique contributes to understanding user queries, processing
information, and generating intelligent responses.
✍️ Answer (10 Marks)
Smart virtual assistants like Siri and Google Assistant use multiple Artificial
Intelligence (AI) techniques such as Machine Learning (ML), Natural Language
Processing (NLP), and Knowledge Representation (KR) to understand user queries,
process information, and generate intelligent responses.
🤖 Machine Learning (ML)
Machine Learning enables the assistant to learn from user data and improve
performance over time. It is used for speech recognition, intent prediction, and
personalization.
Role:
•   Converts voice input into text (speech-to-text models)
•   Learns user preferences and behavior
• Improves accuracy of responses with experience
Example: Suggesting reminders based on user habits or predicting frequently used
commands.
💬 Natural Language Processing (NLP)
NLP helps the assistant understand and interpret human language. It processes the text
obtained from speech and extracts meaning.
Role:
•   Tokenization & parsing to break sentences
•   Intent recognition to understand what the user wants
•   Entity extraction to identify key details (e.g., time, place)
Example:
User says: “Set an alarm for 7 AM tomorrow”
NLP identifies intent = set alarm, time = 7 AM, date = tomorrow.
🧠 Knowledge Representation (KR)
Knowledge Representation stores structured information and rules that the system uses
to reason and respond.
Role:
•   Maintains knowledge base (facts, rules, relationships)
•   Enables logical reasoning and decision-making
•   Retrieves relevant information to answer queries
Example:
Answering “What is the capital of France?” using stored knowledge.
********** 14 **********
--- page 15 ---
🔄 Combined Working in Virtual Assistant
1. User Input: Voice command given
2. ML: Converts speech to text
3. NLP: Understands intent and extracts entities
4. KR: Retrieves or reasons using stored knowledge
5. Response Generation: System provides appropriate output (voice/text)
🧠 Conclusion
Machine Learning, NLP, and Knowledge Representation work together in virtual
assistants to enable intelligent interaction. ML handles learning and prediction, NLP
enables language understanding, and KR supports reasoning, making assistants
capable of providing accurate and context-aware responses.
📊 Evaluation Rubric (10 Marks)
Explanation of ML role (2) + NLP role (3) + KR role (2) + Integrated working (2) +
Example/clarity (1)
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 3090341950ab

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_IT_7041/Principles of Artificial Intelligence/ANS_Principles of Artificial Intelligence(702IT0C035)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Jul 2026
- Text: mixed (15 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Principles of Artificial Intelligence
Date: 13 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
CO1;   A   Identify PEAS parameters for the following AI agent types   5
BL2   a) Virtual Personal Assistant.
b) chess playing
*[ Part a -5M , Part b -5M]
Virtual Personal Assistant
• Performance Measure (P):
Task accuracy, response time, user satisfaction, successful task completion
• Environment (E):
User devices, internet, apps (email, calendar), real-world user context
• Actuators (A):
Voice responses, notifications, scheduling actions, sending messages
• Sensors (S):
Voice input, text commands, user data, calendar, emails
Chess Playing Agent
• Performance Measure (P):
Winning the game, minimizing moves, strategic advantage
• Environment (E):
Chessboard, opponent, game rules
• Actuators (A):
Moving pieces on the board
Sensors (S):
Board configuration, opponent moves
CO1 ;   B Compare Informed & Uninformed search with example   5
BL4
✍️ Answer (5 Marks)
In Artificial Intelligence, search algorithms are broadly classified into Uninformed
search and Informed search based on the knowledge they use.
Uninformed search (Blind search) does not use any additional information about the
problem domain. It explores the search space using only the initial state, goal state,
********** 1 **********
--- page 2 ---
and possible actions. Examples include Breadth-First Search (BFS) and Depth-First
Search (DFS). These methods may explore many unnecessary nodes, making them less
efficient.
Example: In a maze, BFS explores all possible paths level by level without knowing
which direction leads closer to the goal.
Informed search (Heuristic search) uses additional knowledge in the form of a
heuristic function to guide the search towards the goal more efficiently. It selects paths
that appear more promising, reducing the number of explored nodes. Examples include
A* search and Greedy Best-First Search.
Example: In the same maze, A* uses the estimated distance to the goal to choose the
best path, reaching the solution faster.
Difference: Uninformed search is simple but inefficient, while informed search is
more efficient due to the use of heuristics.
📊 Evaluation Rubric (5 Marks)
Definition of Uninformed search (1) + Definition of Informed search (1) + Key
difference (1) + Examples (1) + Clarity (1)
CO2 ;   C   Explain the structure and working of a Bayesian Network.   5
BL2
✍️ Answer (5 Marks)
A Bayesian Network (also called a Belief Network) is a probabilistic graphical model
that represents a set of variables and their conditional dependencies using a directed
acyclic graph (DAG). Each node in the graph represents a random variable, and the
directed edges represent probabilistic dependencies between variables. Associated
with each node is a conditional probability table (CPT) that quantifies the effect of
parent nodes on that variable.
Structure:
• Nodes → random variables
•   Directed edges → dependencies/causal relationships
• CPT → probability of a node given its parents
Working:
A Bayesian Network works based on Bayes’ theorem, where the joint probability of
all variables is computed as the product of conditional probabilities of each node given
its parents. When evidence is provided (e.g., some variables are known), the network
updates the probabilities of other variables using probabilistic inference.
Example:
In a medical diagnosis system, variables like Disease, Symptoms, and Test Results are
connected. If symptoms are observed, the network updates the probability of a disease
using conditional probabilities.
📊 Evaluation Rubric (5 Marks)
Definition of Bayesian Network (1) + Structure (nodes, edges, CPT) (1.5) + Working
(probability & inference) (1.5) + Example (1)
CO3 ;   D What are Language Models? Explain n-gram models with example.   5
BL2
✍️ Answer (5 Marks)
Language Models are used in Natural Language Processing (NLP) to estimate the
probability of a sequence of words and to predict the next word in a sentence. They
help machines understand and generate human language by learning patterns from text
data.
One common type is the N-gram model, which assumes that the probability of a word
depends only on the previous (N−1) words (Markov assumption).
********** 2 **********
--- page 3 ---
• Unigram (N=1): Each word is independent.
Example: P(“I love AI”) = P(I) × P(love) × P(AI)
• Bigram (N=2): Depends on one previous word.
Example: P(“I love AI”) = P(I) × P(love|I) × P(AI|love)
• Trigram (N=3): Depends on two previous words.
Example: P(“I love AI”) = P(I) × P(love|I) × P(AI|I, love)
Conclusion: N-gram models are simple and effective for basic language prediction
tasks, but they have limitations such as limited context and data sparsity.
📊 Evaluation Rubric (5 Marks)
Definition of Language Model (1.5) + N-gram concept (1.5) + Examples (1.5) +
Conclusion/limitation (0.5)
Q2   [20]
CO1 ;   A   Define alpha (α) and beta (β) values in the Alpha–Beta Pruning algorithm. Explain when 10
BL4   pruning occurs in the Alpha–Beta algorithm. Apply the Alpha–Beta Pruning algorithm
to the given game tree. Clearly indicate which branches are pruned, assuming left-to-
right traversal.
*[ Defination-2M, Condition-1M, Stepwise updation of α and β value -7M]
Alpha (α) represents the best (maximum) value that the maximizing player can
guarantee so far along the current path. In other words, it is the highest value found at
any point for the maximizer, and the algorithm tries to increase this value as it explores
more nodes.
Beta (β) represents the best (minimum) value that the minimizing player can
guarantee so far. It is the lowest value found so far for the minimizer, and the algorithm
attempts to decrease this value during exploration.
Pruning occurs when it is determined that further exploration of a node will not affect
the final decision. Specifically, pruning happens when:
********** 3 **********
--- page 4 ---
CO2 ;   B   Consider the following statement   10
BL5   1. Sunil likes all kind of food.
2. Apple and vegetable are food.
3. Anything anyone eats and not killed is food.
4. Anil eats peanuts and still alive.
5. Sohan eats everyting that Anil eats.
6. Sunil like peanuts.
a) Convert to FOL
b) Convert FOL to CNF
c) Prove that “ Sunil likes Peanuts” using the resolution
Draw Resolution Tree.
Answer:
FOL ( 2M)
********** 4 **********
--- page 5 ---
1. Wx: food(x)>likes(Sunil, x)
2. food(apple) A
food(vegetable)
3. Wx Vy: eats(x,y)A
- killed(x)>food(y)

4. eats(Anil , Peanut)A
alive(Anil)

5. Wx: eats(Anil, x) >
eats(Sohan, x)

6.   Likes(Sunil, Peanut)

° Wx : - killed(x)>alive(x)

° Vx : alive (x) >-killed (x)

(added predicates)

CNF: (4M)

1. - food(x) V likes(Sunil, x)
2. food(Apple)
3. food(vegetables)

4. -eats(y, z) V killed(y) V
food(z)

5. eats (Anil, Peanuts)

6. alive(Anil)

7. - eats(Anil, w) V
eats(Sohan, w)

8. killed(g) V alive(g)

9. - alive(k) V - killed(k)

10. likes(Sunil, Peanuts)

Resolution Tree (4M)

~likes(Sunil, Peanuts) = food(x) V likes(Sunil, x)
{Peanuts/x}

+ food(Peanuts) > eats(y, z) V killed(y) V food(z)

{Peanuts/z}
> eats(y, Peanuts) V killed(y) eats (Anil, Peanuts)
{Anil/y}
Killed(Anil) = alive(k) V ~ killed(k)
{Anil/k}
> alive(Anil) alive(Anil)
(6) Null

Q3

[20]

FIC DI EH ar
--- page 6 ---
CO1 ;   A   Describe Breadth-first search algorithm. Consider the graph shown below, start from 10
BL3   node 0. identify the traversal path using Breadth First search algorithm.
*[ Explanation-4M, Numerical stepwise explanation-6M]
Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by going
as deep as possible along each branch before backtracking. It uses either a stack data
structure or recursion. The algorithm starts from a given source node, marks it as visited,
and then recursively visits one of its unvisited adjacent nodes. This process continues
until it reaches a node that has no unvisited neighbors. At that point, it backtracks to the
previous node and explores other unvisited neighbors. This continues until all nodes in
the graph have been visited.
For the given graph, starting from node 0, DFS begins at node 0 and moves to node 1
(one of its adjacent nodes). From node 1, it proceeds deeper to node 2, then to node 4,
and then to node 6, following one path as far as possible. Since node 6 has no unvisited
adjacent nodes left, the algorithm backtracks to node 4, then to node 2, and continues
exploring the next unvisited neighbor, which is node 5. After visiting node 5, it
backtracks again to node 2, then to node 1, and finally visits node 3, which was not yet
explored.
Thus, the Depth-First Search traversal starting from node 0 is:
DFS traversal can vary depending on the order in which adjacent nodes are chosen
CO1;   B   Explain the concept of Support Vector Machines (SVM). How does it perform   10
BL4   classification using a hyperplane?
✍️ Answer (10 Marks)
Support Vector Machine (SVM) is a supervised machine learning algorithm used for
classification and regression tasks. It works by finding an optimal boundary, called a
hyperplane, that separates data points of different classes with the maximum possible
margin. SVM is particularly effective in high-dimensional spaces and is widely used
for classification problems.
📐 Concept of Hyperplane in SVM
A hyperplane is a decision boundary that divides the dataset into different classes.
•   In 2D → it is a line
•   In 3D → it is a plane
•   In higher dimensions → it is called a hyperplane
SVM selects the hyperplane that maximizes the margin, i.e., the distance between the
hyperplane and the nearest data points from each class.
📏 Role of Support Vectors
The data points that lie closest to the hyperplane are called support vectors. These
points are critical because they determine the position and orientation of the
hyperplane. Removing them would change the decision boundary.
********** 6 **********
--- page 7 ---
⚙️ Working of SVM for Classification
1. The algorithm identifies all possible hyperplanes that can separate the classes.
2.   It selects the hyperplane with the maximum margin (best separation).
3. The decision function classifies new data points based on which side of the
hyperplane they fall.
Mathematically, the hyperplane can be represented as:
w·x + b = 0
where w is the weight vector, x is the input, and b is the bias.
🔄 Handling Non-Linearly Separable Data
When data is not linearly separable, SVM uses the kernel trick to map data into a
higher-dimensional space where a linear hyperplane can separate the classes. Common
kernels include linear, polynomial, and radial basis function (RBF).
🧠 Conclusion
SVM is a powerful classification technique that finds the optimal hyperplane with
maximum margin using support vectors. Its ability to handle both linear and non-linear
data makes it widely applicable in real-world problems like image classification and
text categorization.
📊 Evaluation Rubric (10 Marks)
Definition of SVM (2) + Hyperplane concept (2) + Margin & support vectors (2) +
Working steps (2) + Kernel/non-linear handling (2)
Q4   [20]
CO2;   A   Distinguish between supervised and unsupervised learning algorithm. Illustrate with   10
BL4   an example
✍️ Answer (10 Marks)
Supervised learning and unsupervised learning are two main types of machine
learning algorithms, differing in how they learn from data.
Supervised learning involves training a model on labeled data, where both input and
corresponding output are known. The algorithm learns a mapping from input to output
and is used for tasks like classification and regression.
Example: Predicting whether an email is spam or not using labeled examples of spam
and non-spam emails.
Unsupervised learning, on the other hand, works with unlabeled data, where the
model tries to find hidden patterns or structures in the data without predefined outputs.
It is mainly used for clustering and association tasks.
Example: Grouping customers into different segments based on purchasing behavior
without prior labels.
🔍 Key Differences
•   Supervised learning uses labeled data, while unsupervised uses unlabeled
data
•   Supervised learning predicts outputs; unsupervised discovers patterns
•   Supervised tasks: classification, regression
•   Unsupervised tasks: clustering, association
********** 7 **********
--- page 8 ---
🧠 Conclusion
Supervised learning is useful when labeled data is available and prediction is required,
whereas unsupervised learning is useful for discovering hidden structures in data. Both
techniques are essential in building intelligent systems.
📊 Evaluation Rubric (10 Marks)
Definition of supervised learning (2) + Definition of unsupervised learning (2) + Key
differences (3) + Examples (2) + Conclusion/clarity (1)
CO1 ;   B   Illustrate the working of Hill Climbing using a suitable problem. Why does it fail in   10
BL4   certain situations? Discuss methods to overcome these failures
✍️ Answer (10 Marks)
Hill Climbing is a heuristic search algorithm used in Artificial Intelligence for
optimization problems. It starts with an initial solution and iteratively moves to a
neighboring solution that has a better value (higher for maximization or lower for
minimization). The process continues until no better neighboring state is found, at
which point the algorithm stops.
🔍 Working of Hill Climbing (Example)
Consider the problem of finding the maximum value of a function (e.g., maximizing
f(x)).
•   Start with an initial value of x
•   Evaluate neighboring values (e.g., x+1, x−1)
• Move to the neighbor with a higher value
•   Repeat until no improvement is possible
Illustration:
If we want to reach the highest peak of a hill:
•   Start at a random point
• Move uphill step by step
•   Stop when reaching a peak (no higher neighbor exists)
⚠️ Limitations / Failures
Hill Climbing may fail in the following situations:
1. Local Maximum – The algorithm may stop at a peak that is not the global
maximum
2. Plateau – A flat region where neighboring states have the same value, causing
no progress
3. Ridge Problem – Narrow paths where the algorithm struggles to find the
correct direction
🛠️ Methods to Overcome Failures
1. Random Restart Hill Climbing
o Run the algorithm multiple times with different initial states
o   Increases chance of finding global optimum
2. Simulated Annealing
o Allows occasional downhill moves to escape local maxima
3. Stochastic Hill Climbing
********** 8 **********
--- page 9 ---
o Chooses random neighbors instead of the best one
4. Sideways Moves
o Allows movement across plateaus for a limited number of steps
🧠 Conclusion
Hill Climbing is a simple and efficient optimization technique, but it may get stuck in
local optima or flat regions. Advanced strategies like random restart and simulated
annealing help improve its performance and reliability.
📊 Evaluation Rubric (10 Marks)
Definition of Hill Climbing (2) + Working with example (3) + Limitations (3) +
Methods to overcome (2)
Q5   [20]
CO2 ;   A   Define the following term in context to decision tree w.r.t suitable example:   10
BL2   a) Information Gain
b) Entropy
✍️ Answer
a) Information Gain (5 Marks)
Information Gain is a measure used in decision trees to determine which attribute
should be selected for splitting the data at each step. It calculates the reduction in
entropy after splitting a dataset based on a particular attribute. The attribute with the
highest information gain is chosen as the best split.
Mathematically:
Information Gain = Entropy (parent) − Weighted Entropy (children)
Example:
Consider a dataset of weather conditions to decide whether to play tennis. If splitting
on the attribute Outlook (Sunny, Rainy, Overcast) reduces uncertainty significantly
compared to other attributes, then Outlook will have the highest information gain and
will be selected as the root node.
b) Entropy (5 Marks)
Entropy is a measure of uncertainty or impurity in a dataset. It indicates how mixed
the data is. If all examples belong to the same class, entropy is 0 (pure). If the data is
evenly distributed among classes, entropy is maximum.
Mathematically:
Entropy = − Σ p(x) log₂ p(x)
Example:
In a dataset of 10 samples:
• 5 are “Yes” and 5 are “No” → High entropy (maximum uncertainty)
• 10 are “Yes” and 0 are “No” → Entropy = 0 (no uncertainty)
🧠 Conclusion
Entropy measures impurity in the dataset, while Information Gain measures how much
that impurity is reduced after a split. Decision trees use these concepts to build
efficient and accurate models.
📊 Evaluation Rubric
Information Gain: Definition (2) + Formula (1) + Example (2)
Entropy: Definition (2) + Formula (1) + Example (2)
********** 9 **********
--- page 10 ---
CO3 ;   B   Discuss various techniques used in Information Extraction. Explain their roles in   10
BL4   extracting meaningful information from text.
✍️ Answer (10 Marks)
Information Extraction (IE) is a task in Natural Language Processing (NLP) that
involves automatically extracting structured information such as entities, relationships,
and facts from unstructured text. Various techniques are used to identify and organize
meaningful information.
🔍 Techniques in Information Extraction
1. Named Entity Recognition (NER)
NER identifies and classifies entities like names of people, organizations, locations,
dates, etc.
Role: Converts raw text into structured entities.
Example: “Elon Musk founded SpaceX” → Elon Musk (Person), SpaceX
(Organization)
2. Part-of-Speech (POS) Tagging
POS tagging assigns grammatical labels (noun, verb, adjective, etc.) to words.
Role: Helps in understanding sentence structure and identifying important components
for extraction.
3. Chunking (Shallow Parsing)
Chunking groups words into meaningful phrases such as noun phrases or verb phrases.
Role: Helps identify relationships between words and extract relevant phrases.
4. Dependency Parsing
This technique analyzes grammatical relationships between words in a sentence.
Role: Helps in identifying subject-object relationships and extracting relations.
Example: “Ram eats apple” → Ram (subject), apple (object)
5. Rule-Based Techniques
These use predefined linguistic rules and patterns to extract information.
Role: Useful for domain-specific extraction where patterns are known.
6. Machine Learning-Based Techniques
Models are trained on annotated data to automatically learn extraction patterns.
Role: Improves accuracy and adaptability across different domains.
7. Template Filling
Extracted information is organized into predefined templates.
Role: Converts extracted data into structured formats (e.g., forms or databases).
🧠 Conclusion
Information Extraction combines linguistic and machine learning techniques to
transform unstructured text into structured knowledge. Techniques like NER, POS
tagging, and parsing play a key role in identifying entities and relationships, enabling
applications such as chatbots, search engines, and knowledge bases.
📊 Evaluation Rubric (10 Marks)
Definition of IE (2) + Explanation of techniques (6) + Roles of techniques (1) +
Example/clarity (1)
Q6   [20]
CO2 ;   A   Explain quantifiers in First-Order Logic. Discuss universal and existential quantifiers   10
BL2   with suitable examples.
********** 10 **********
--- page 11 ---
✍️ Answer (10 Marks)
In First-Order Logic (FOL), quantifiers are used to express statements about a
group of objects in a domain. They specify how many elements satisfy a given
predicate, making FOL more expressive than propositional logic. The two main types
of quantifiers are universal quantifier (∀) and existential quantifier (∃).
🔹 Universal Quantifier (∀)
The universal quantifier (∀) means “for all” and is used to state that a property holds
for every element in the domain.
Form: ∀x P(x)
This means P(x) is true for all values of x.
Example:
∀x Human(x) → Mortal(x)
This means “All humans are mortal.”
Role:
•   Represents general rules or universal truths
• Widely used in knowledge representation
🔹 Existential Quantifier (∃)
The existential quantifier (∃) means “there exists” and is used to indicate that at least
one element in the domain satisfies a given condition.
Form: ∃x P(x)
This means there exists at least one x for which P(x) is true.
Example:
∃x Student(x) ∧ Intelligent(x)
This means “There exists a student who is intelligent.”
Role:
•   Represents existence of at least one object
•   Useful for expressing partial or specific knowledge
🔍 Key Difference
• ∀ applies to all elements in the domain
• ∃ applies to at least one element
• ∀ expresses generalization, while ∃ expresses existence
🧠 Conclusion
Quantifiers enhance the power of First-Order Logic by allowing statements about
groups of objects. Universal quantifiers express general rules, while existential
quantifiers indicate the existence of specific instances, making FOL suitable for
representing real-world knowledge.
📊 Evaluation Rubric (10 Marks)
Definition of quantifiers (2) + Universal quantifier explanation (3) + Existential
quantifier explanation (3) + Examples (1) + Difference/conclusion (1)
CO3 ;   B   Explain the Bag-of-Words model. How are documents converted into vectors? Discuss 10
BL4   its limitations and improvements ?
********** 11 **********
--- page 12 ---
✍️ Answer (10 Marks)
The Bag-of-Words (BoW) model is a simple technique used in Natural Language
Processing (NLP) to represent text data as numerical vectors. In this model, a
document is treated as a “bag” of words, ignoring grammar and word order, and only
the frequency of words is considered.
🔤 How Documents are Converted into Vectors
1. Text Preprocessing
o Convert text to lowercase, remove punctuation, stop-words, etc.
2. Vocabulary Creation
o Create a list of all unique words from the dataset (called vocabulary)
3. Vector Representation
o Each document is represented as a vector of word counts based on the
vocabulary
Example:
Documents:
D1: “I love AI”
D2: “AI is powerful”
Vocabulary: [I, love, AI, is, powerful]
Vectors:
• D1 → [1, 1, 1, 0, 0]
• D2 → [0, 0, 1, 1, 1]
⚠️ Limitations of Bag-of-Words
•   Ignores word order → “AI is good” and “good is AI” are treated the same
• No semantic meaning → cannot understand synonyms or context
• High dimensionality → large vocabulary leads to large vectors
•   Sparsity → most values in vectors are zero
🚀 Improvement: TF-IDF
TF-IDF (Term Frequency–Inverse Document Frequency) improves BoW by
assigning weights to words based on importance.
• TF (Term Frequency): Frequency of a word in a document
• IDF (Inverse Document Frequency): Measures how rare a word is across
documents
Words that appear frequently in one document but rarely across others get higher
weight.
Advantage over BoW:
• Reduces importance of common words
•   Highlights meaningful and distinctive terms
🧠 Conclusion
The Bag-of-Words model is a basic and efficient method for text representation, but it
has limitations in capturing meaning and context. Techniques like TF-IDF improve its
********** 12 **********
--- page 13 ---
effectiveness by weighting important words, making it more suitable for tasks like text
classification and information retrieval.
📊 Evaluation Rubric (10 Marks)
Definition of BoW (2) + Vector conversion process (3) + Example (1) + Limitations
(2) + TF-IDF explanation (2)
Q7   [20]
CO2 ;   A   Design a Perceptron model for implementing the AND gate. Derive suitable weights   10
BL3   and bias, and verify the output using all input combinations.
✍️ Answer
A Perceptron is a simple neural network model used for binary classification. It
computes a weighted sum of inputs and applies an activation function (step function)
to produce an output.
🔢 Step 1: AND Gate Truth Table
x₁   x₂   Output (y)
0   0   0
0   1   0
1   0   0
1   1   1
⚙️ Step 2: Perceptron Model
Output is given by:
y = 1 if (w₁x₁ + w₂x₂ + b ≥ 0), else 0
🎯 Step 3: Choose Weights and Bias
For AND gate, suitable values are:
• w₁ = 1
• w₂ = 1
• b = −1.5
✅ Step 4: Verification
Now compute output for all inputs:
1. x₁=0, x₂=0
Net = (1×0 + 1×0 − 1.5) = −1.5 → y = 0
2. x₁=0, x₂=1
Net = (1×0 + 1×1 − 1.5) = −0.5 → y = 0
3. x₁=1, x₂=0
Net = (1×1 + 1×0 − 1.5) = −0.5 → y = 0
4. x₁=1, x₂=1
Net = (1×1 + 1×1 − 1.5) = 0.5 → y = 1
🧠 Conclusion
The perceptron with weights w₁ = 1, w₂ = 1 and bias b = −1.5 correctly implements the
AND gate, producing the desired output for all input combinations.
********** 13 **********
--- page 14 ---
📊 Evaluation Rubric (Typical 5–10 Marks)
Truth table (2) + Model/formula (2) + Weights & bias selection (2) + Verification (3)
+ Conclusion (1)
CO2 ;   B   Explain how AI techniques such as Machine Learning, Natural Language Processing   10
BL5   (NLP), and Knowledge Representation are applied in a smart virtual assistant
(Siri/Google Assistant).
Illustrate how each technique contributes to understanding user queries, processing
information, and generating intelligent responses.
✍️ Answer (10 Marks)
Smart virtual assistants like Siri and Google Assistant use multiple Artificial
Intelligence (AI) techniques such as Machine Learning (ML), Natural Language
Processing (NLP), and Knowledge Representation (KR) to understand user queries,
process information, and generate intelligent responses.
🤖 Machine Learning (ML)
Machine Learning enables the assistant to learn from user data and improve
performance over time. It is used for speech recognition, intent prediction, and
personalization.
Role:
•   Converts voice input into text (speech-to-text models)
•   Learns user preferences and behavior
• Improves accuracy of responses with experience
Example: Suggesting reminders based on user habits or predicting frequently used
commands.
💬 Natural Language Processing (NLP)
NLP helps the assistant understand and interpret human language. It processes the text
obtained from speech and extracts meaning.
Role:
•   Tokenization & parsing to break sentences
•   Intent recognition to understand what the user wants
•   Entity extraction to identify key details (e.g., time, place)
Example:
User says: “Set an alarm for 7 AM tomorrow”
NLP identifies intent = set alarm, time = 7 AM, date = tomorrow.
🧠 Knowledge Representation (KR)
Knowledge Representation stores structured information and rules that the system uses
to reason and respond.
Role:
•   Maintains knowledge base (facts, rules, relationships)
•   Enables logical reasoning and decision-making
•   Retrieves relevant information to answer queries
Example:
Answering “What is the capital of France?” using stored knowledge.
********** 14 **********
--- page 15 ---
🔄 Combined Working in Virtual Assistant
1. User Input: Voice command given
2. ML: Converts speech to text
3. NLP: Understands intent and extracts entities
4. KR: Retrieves or reasons using stored knowledge
5. Response Generation: System provides appropriate output (voice/text)
🧠 Conclusion
Machine Learning, NLP, and Knowledge Representation work together in virtual
assistants to enable intelligent interaction. ML handles learning and prediction, NLP
enables language understanding, and KR supports reasoning, making assistants
capable of providing accurate and context-aware responses.
📊 Evaluation Rubric (10 Marks)
Explanation of ML role (2) + NLP role (3) + KR role (2) + Integrated working (2) +
Example/clarity (1)
********** 15 **********
````
