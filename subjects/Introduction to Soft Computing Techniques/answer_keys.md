# Introduction to Soft Computing Techniques: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 0c6b601c91be

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/Integrated_IT_7037/Introduction to Soft Computing Techniques/ANS_Introduction to Soft Computing Techniques(701IT0C011)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Introduction to Soft Computing Techniques
Date: 13 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
Q1   Compulsory Questions:
CO-1 ; SO-2 ;   a.   What is problem space in Artificial Intelligence? Explain its   [5]
BL-1   components.
Answer:
▪ A problem space is the environment in which an AI
agent searches for a solution.
▪   It defines all possible states, actions, and paths from
the initial state to the goal state.
▪   “It is a conceptual map of all the states, decisions, and
transitions that an agent may encounter while trying
to solve a problem.
Think of it as the entire search area the AI explores to
find a solution.”
▪   Initial State – The starting point of the problem.
▪ Actions (Operators) – Moves or decisions the agent
can take.
▪   States – All possible configurations resulting from
actions.
▪ Goal State – The desired solution or target.
▪ Path / Sequence of Actions – A series of moves from
initial to goal state.
********** 1 **********
--- page 2 ---
CO-1 ; SO-2 ;   b.   Explain the working of Evolutionary cycle.   [5]
BL-2
Answer: Initialization – Create an initial random population
•   Evaluation (Fitness) – Measure quality of each
individual
•   Selection – Choose the fittest individuals as parents
• Recombination (Crossover) – Combine parent traits
to produce offspring
•   Mutation – Introduce small random changes to
maintain diversity
• Replacement –next generation from offspring (and
sometimes parents)
•   Termination – Stop when solution is satisfactory or
max generations reached
CO-2 ; SO-2 ;   c.   Explain permutation and tree representations in genetic   [5]
BL-2   algorithms with suitable examples.
Answer: permuttion
• Used when the solution depends on the order of
elements.
• Each chromosome shows a sequence or arrangement
of items.
Example:
•   In the Traveling Salesman Problem (TSP), a salesman
must visit each city once and return to the starting
city.
• The goal is to minimize the total travel distance.
• Example chromosome:
A → C → B → D → E
Tree: Solutions are represented as tree structures.
•   Often used in programming or symbolic expressions.
• Example expression:
• Each node represents an operator (+, -, *)
• Each leaf represents a value or variable
(x, y, 3, 2).
CO-3 ; SO-2 ;   d.   Discuss the working process of the K-Means algorithm.   [5]
BL-2
Answer: Choose the number of clusters (K)
1. Initialize K centroids (randomly selected points)
2. Assign each data point to the nearest centroid
********** 2 **********
--- page 3 ---
3. Recalculate the centroids as the mean of assigned
points
4. Repeat steps 3 and 4 until centroids do not change
significantly
Attempt any 4
Q2   a.   Explain the applications of Genetic Algorithms in financial [10]
modeling and in image and signal processing with suitable
CO-2 ; SO-2 ;
examples.
BL-2
Answer: Image and signal processing: Genetic Algorithms
are used in image and signal processing.
• They help improve image quality and remove noise.
• GAs can find the best settings for image or signal
processing methods.
• They can also detect important features or patterns
in images and signals.
Examples:
• Removing noise from images.
• Improving blurry images.
•   Recognizing patterns in images.
•   Financial modellimg: Genetic Algorithms are used in
finance to make better decisions.
• They help choose the best investment portfolio.
• GAs can also improve trading strategies.
• They help increase profit and reduce risk.
Examples:
•   Portfolio optimization -choosing the best
investments.
•   Trading strategies.
•   Risk management in financial markets.
Q2   b.   What is Fuzzy Logic? Describe its architecture and explain   [10]
its real-world applications.
CO-2 ; SO-2 ;
BL-2
Answer: Fuzzy Logic helps in situations where information is
not clear or not exact.
Instead of giving only 0 or 1, it allows values between
0 and 1, which means something can be partly true.
▪ This makes it useful for real-life decision-making.
▪ Handles uncertain and unclear information
▪ Uses values between 0 and 1 (partial truth)
********** 3 **********
--- page 4 ---
▪ Used in control systems, medical diagnosis, AI, and
image processing
▪ Helps systems make flexible and human-like
decisions
A fuzzy logic system has 4 simple steps:
1. Fuzzification
•   Converts exact input into fuzzy values
• Uses terms like low, medium, high instead of exact
numbers
Example:
Temperature = 30°C → 0.6 warm, 0.4 hot
2. Rule Base
• A set of IF–THEN rules made by experts
• These rules guide the system’s decisions
Example:
•   IF temperature is hot THEN fan is fast
•   IF temperature is warm THEN fan is medium
3. Inference Engine
• Checks all rules and finds which ones apply
• Combines the results to make a decision
Example:
•   If both “warm” and “hot” are true → combines both
outputs
4. Defuzzification
•   Converts fuzzy result into a single exact value
•   This helps the system take final action
Example:
Fan speed = 70%
1. Applications: Aerospace
1. Used to control satellites and spacecraft
height
2. Automotive
1. Helps in speed control and traffic systems
3. Industrial
1. Used in industries for process control like pH
control, drying, etc.
4. Artificial Intelligence
1. Used in language processing and decision
making
5. Control Systems
********** 4 **********
--- page 5 ---
1. Used in robots and smart systems to control
actions
6. Consumer Electronics
• Washing machines
•   Air conditioners (temperature control)
7. Healthcare
•   Medical diagnosis systems
Q3   a.   Explain the step-by-step process of Genetic Programming   [10]
with suitable examples.
CO-1 ; SO-2 ;
BL-2
Answer: Step 1: Define the Problem
•   Decide what task the program must perform
(e.g., prediction, classification, symbolic regression)
Step 2: Define Function Set & Terminal Set
Function set: Operators like + , − , × , ÷ , sin , cos
Terminal set: Variables and constants
Step 3: Initial Population Creation
•   Generate random programs
• Each program is represented as a tree structure
Step 4: Fitness Evaluation
• Each program is executed
•   Fitness is calculated based on how well it solves the
problem
(e.g., minimum error, maximum accuracy)
Step 5: Selection
•   Better programs (higher fitness) are selected as
parents
• Methods: Tournament selection, roulette wheel
• Tournament selection: A few individuals are
randomly picked, and the best among them is
selected as a parent.
•   Roulette wheel: The better the solution, the higher its
chance of getting selected.
Step 6: Genetic Operators
a) Crossover
• Exchange subtrees between two parent programs
•   Produces new offspring programs
b) Mutation
• Randomly change a node or subtree
•   Maintains diversity
Step 7: Create New Generation
• New programs replace weaker ones
********** 5 **********
--- page 6 ---
•   Best programs may be preserved.
Step 8: Termination Condition
• GP stops when:
•   Maximum generations reached OR
Desired fitness level achieved.
Q3   b.   Explain the Machine Learning Lifecycle in detail.   [10]
CO-3 ; SO-2 ;
BL-2   Answer: 1. Problem Definition
• Problem Definition is the first step in the Machine
Learning lifecycle where the objective of the project
is clearly defined. It involves understanding the
problem, identifying inputs and expected outputs,
and setting success criteria.
2. Data Collection
•   Data Collection is the process of gathering relevant
data from various sources such as databases,
websites, sensors, or APIs. The quality and quantity
of data directly affect the performance of the model.
3. Data Cleaning & Preprocessing
•   Data Cleaning and Preprocessing involve removing
errors, handling missing values, and converting raw
data into a structured format suitable for analysis.
This step ensures the data is accurate and consistent.
4. Exploratory Data Analysis (EDA)
•   Exploratory Data Analysis is used to understand the
data by summarizing its main characteristics using
statistical methods and visualizations. It helps in
identifying patterns, trends, and outliers.
5. Feature Engineering & Selection
•   Feature Engineering involves creating new features
from existing data, while Feature Selection involves
choosing the most important features. This step
improves model performance and reduces
complexity.
6. Model Selection
• Model Selection is the process of choosing the most
appropriate Machine Learning algorithm based on
the type of problem and data. Different models are
suitable for different tasks.
7. Model Training
• Model Training is the process where the selected
algorithm learns patterns from the training data. The
model adjusts its parameters to minimize errors and
improve accuracy.
8. Model Evaluation & Tuning
• Model Evaluation involves testing the model using
performance metrics such as accuracy, precision, and
********** 6 **********
--- page 7 ---
recall. Tuning is done to improve the model by
adjusting parameters.
9. Model Deployment
• Model Deployment is the process of making the
trained model available for real-world use, such as
integrating it into applications, websites, or systems.
10. Model Monitoring & Maintenance
• Model Monitoring and Maintenance involve
continuously tracking the model’s performance after
deployment and updating it when necessary to
maintain accuracy over time.
Q4   a.   What is a hypothesis? Discuss its characteristics, sources,   [10]
CO-1 ; SO-2 ;   functions, and examples.
BL-1,2
Answer: A hypothesis is an assumption that is made based
on some evidence.
This is the initial point of any investigation that translates
the research questions into predictions.
•   It includes components like variables, population and
the relation between the variables.
• A research hypothesis is a hypothesis that is used to
test the relationship between two or more variables.
• The hypothesis should be clear and precise to
consider it to be reliable.
•   If the hypothesis is a relational hypothesis, then it
should be stating the relationship between variables.
• The hypothesis must be specific and should have
scope for conducting more tests.
• The way of explanation of the hypothesis must be
very simple and it should also be understood that the
simplicity of the hypothesis is not related to its
significance.
A hypothesis is a tentative, testable statement. It can
be derived from several sources, especially in
research and academic studies. The main sources are:
1. Theory: Existing theories provide a strong basis for
forming hypotheses.
2. Previous Research Studies:Past research findings
help identify gaps or inconsistencies.
3. Observation:Daily life or field observations often
trigger hypotheses.
4. Personal Experience:Experiences of teachers,
professionals, or researchers can guide hypothesis
********** 7 **********
--- page 8 ---
5. Intuition or Insight:Sudden ideas based on
intellectual insight.
6. Problem Statement / Research Questions:Research
problems naturally lead to hypotheses.
Function: Hypothesis helps in making an observation and
experiments possible.
7. It becomes the start point for the investigation.
8. Hypothesis helps in verifying the observations.
9. It helps in directing the inquiries in the right
direction.
Q4   b.   Define job scheduling and explain its concept. Discuss its   [10]
CO-2 ; SO-2 ;   real-world applications with a suitable example.
BL-3
Answer: Job Scheduling is a problem of arranging jobs or
tasks in the best order so that work is completed efficiently.
Concept
• There are multiple jobs that need to be done.
• Each job may take different time or have a deadline.
Goal: to schedule jobs in an order that saves time and
resources.
Example
Suppose there are 3 jobs:
Possible   order:
J2 → J1 → J3
Total time calculation:
1 + 2 + 3 = 6 hours
Real-World Examples:
•   Factory production scheduling
• Exam timetable scheduling
Project task planning
Q5.a
•   Answer: It basically involves five phases to solve the
complex optimization problems, which are given as
below:
1. Initialization
2. Fitness Assignment
3. Selection
4. Reproduction
5. Termination
Q5   a.   Explain the procedure of a Genetic Algorithm in detail.   [10]
CO-1 ; SO-2 ;
BL-2   Answer: It basically involves five phases to solve the
complex optimization problems, which are given as below:
6. Initialization
7. Fitness Assignment
8. Selection
9. Reproduction
10. Termination
********** 8 **********
--- page 9 ---
Explain each in detail.
Q5   b.   Differentiate between supervised and unsupervised machine [10]
CO-2 ; SO-2 ;   learning with suitable examples.
BL-3
Answer:
Supervised   Unsupervised
Feature
Learning   Learning
Learns from   Learns from
Learning Type
labelled data   unlabelled data
Model compares
output with   Model finds
Training Process   actual answer   patterns on its
and corrects   own
errors
Feedback is   No feedback is
Feedback
given   given
Accuracy   Difficult to
Easy to measure
Measurement   evaluate
More controlled
Control   Less controlled
learning
Linear
K-Means,
Regression,
Algorithms   DBSCAN,
Decision Tree,
Hierarchical
SVM
Generally
More complex to
Complexity   simpler to
interpret results
understand
Predictive
Output Nature   (predicts   Descriptive
results)
Fraud detection,   Market
email filtering,   segmentation,
Real-world Use
medical   anomaly
diagnosis   detection
Depends on
Depends on
Dependency   quality of
structure of data
labeled data
Q6   a.   What are AI agents? Explain their types and give suitable   [10]
CO-1 ; SO-2 ;   examples.
BL-1,2
********** 9 **********
--- page 10 ---
Answer: Search problems – finding a solution path
1. Knowledge representation & reasoning – using facts
and rules
2. Planning problems – deciding a sequence of actions
3. Learning problems – improving performance from
experience
4. Perception problems – interpreting sensory data
(vision, speech)
Explain ALL in detail
Q6   b.   What is Soft Computing? Explain the reasons for its need and [10]
CO-3 ; SO-2 ;   discuss its advantages and disadvantages.
BL-3
Answer: Soft computing is a set of computational techniques
that deal with uncertainty, imprecision, and approximation
to provide efficient and near-optimal solutions to complex
real-world problems, often by mimicking human reasoning
and decision-making.
The following are some of the reasons why soft
computing is needed:
1. Complexity of real-world problems: Many real-world
problems are complex and involve uncertainty and
Inaccuracy. Traditional computing methods are not
well-suited to handle these complexities.
2. Incomplete information: In many cases, there is a
lack of complete and accurate information available
to solve a problem. Soft computing techniques can
provide approximate solutions even in the absence of
complete information.
3. 3.Noise and uncertainty: Real-world data is often
noisy and uncertain, and classical methods can
produce incorrect results when dealing with such
data. Soft computing techniques are designed to
handle uncertainty and imprecision.
4. 4.Non-linear problems: Many real-world problems
are non-linear, and classical methods are not well-
suited to solve them. Soft computing techniques such
as fuzzy logic and neural networks can handle non-
linear problems effectively.
5. 5.Human-like reasoning: Soft computing techniques
are designed to mimic human-like reasoning, which
is often more effective in solving complex problems.
•   Advantages: Can handle uncertain and incomplete
data
•   Provides flexible and approximate solutions
• Works well for complex real-world problems
********** 10 **********
--- page 11 ---
• Has learning ability (improves over time)
• More cost-effective and faster than hard computing
• Mimics human thinking and decision-making
•   Disadvatages: Does not give exact or precise results
• May require large data for training
• System design can be complex
•   Results may vary (not always consistent)
Sometimes difficult to interpret results
Q7   a.   A salesman must visit cities A, B, C, D, starting and ending at [10]
CO-2 ; SO-2 ;   A. The travel cost (in km) is:
BL-2
A   B   C   D
A   0   12   10   19
B   12   0   8   20
C   10   8   0   15
D   19   20   15   0
Find the optimal route and minimum cost using TSP.
Answer: Step 1: Possible routes (starting from A)
1. A → B → C → D → A
2. A → B → D → C → A
3. A → C → B → D → A
4. A → C → D → B → A
5. A → D → B → C → A
6. A → D → C → B → A
Step 2: Calculate cost
1. A → B → C → D → A
= 12 + 8 + 15 + 19 = 54
2. A → B → D → C → A
= 12 + 20 + 15 + 10 = 57
3. A → C → B → D → A
= 10 + 8 + 20 + 19 = 57
4. A → C → D → B → A
= 10 + 15 + 20 + 12 = 57
5. A → D → B → C → A
= 19 + 20 + 8 + 10 = 57
6. A → D → C → B → A
= 19 + 15 + 8 + 12 = 54
Step 3: Minimum cost
Minimum cost = 54
********** 11 **********
--- page 12 ---
Final Answer:
Optimal routes:
• A → B → C → D → A
• A → D → C → B → A
Minimum cost = 54 km
Q7   b.   Explain the concept of regression and describe its different   [10]
CO-3 ; SO-2 ;   types with examples.
BL-1,2
Answer: Regression is a type of supervised machine learning
technique used to predict continuous numerical values.
Unlike classification, which predicts categories, regression
predicts quantities such as price, marks, temperature, etc.
• The main objective of regression is to find the
relationship between input variables (features) and a
continuous output variable.
•   Linear Regression – relationship is linear
•   Multiple Regression – multiple input variables
•   Polynomial Regression – curved relationship
Explain each type in detail.
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 2ad055c0cce3

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/Integrated_IT_7037/Introduction to Soft Computing Techniques/ANS_Introduction to Soft Computing Techniques(701IT0C011)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to Soft Computing Techniques
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
Q1   Compulsory Questions:
CO-1 ; SO-2 ;   a.   What is an Intelligent Agent? Explain its components in detail. [5]
BL-1
Answer:
• An Intelligent Agent is an entity that perceives its
environment through sensors and acts upon that
environment through actuators in order to achieve
goals or maximize performance.
•   It represent a subset of AI systems demonstrating
intelligent behaviour, including adaptive learning,
planning, and problem-solving.
•   It operate in dynamic environments, where it makes
decisions based on the information available to them.
• These agents dynamically adjust their behaviour,
learning from past experiences to improve their
approach and aiming for accurate solutions.
Components of an Intelligent Agent:
1. Sensors – collect information from the environment
(camera, microphone, keyboard, sensors, etc.)
2. Actuators – perform actions in the environment
(motors, speakers, display, etc.)
3. Environment – the external world the agent interacts
with
4. Agent Program – decision-making logic
5. Performance Measure – criteria for success
CO-1 ; SO-2 ;   b.   Define Evolutionary Strategies. Explain their working.   [5]
BL-2
********** 1 **********
--- page 2 ---
Answer: Evolutionary Strategies (ES) are evolutionary
algorithms mainly used for numerical optimization that rely
on mutation and selection, with little or no crossover.
Working of Evolutionary Strategies:
Step 1: Initialize population
Start with real-valued solutions
Step 2: Mutation
Add small random changes to variables
Step 3: Fitness evaluation
Check how good each solution is.
Step 4: Selection
Choose best solutions for next generation
Step 5: Repeat
Continue until stopping condition is met.
CO-2 ; SO-2 ;   c.   Explain the applications of Genetic Programming in detail.   [5]
BL-2
Answer:
•   Symbolic Regression – Finding mathematical formulas
that fit data.
• Machine Learning – Creating models or programs
automatically from data.
• Image Processing – Detecting objects and patterns in
images.
•   Robotics – Developing control programs for robots.
•   Financial Modeling – Creating trading strategies and
prediction models.
• Game AI – Evolving strategies for computer games.
•   Circuit Design – Automatically designing electronic
circuits.
•   Data Mining – Discovering patterns and rules in large
datasets.
CO-3 ; SO-2 ;   d.   Write the advantages and disadvantages of Machine Learning.   [5]
BL-2
Answer:
Advantages:
1. Automation of Tasks: ML can automatically perform
tasks without human intervention (e.g., spam
detection).
2. Improves with Experience: Models learn from data
and get better over time.
********** 2 **********
--- page 3 ---
3. Handles Large Data: Can process and analyze huge
amounts of data efficiently.
4. High Accuracy: Provides accurate predictions and
decisions when trained properly.
5. Wide Applications: Used in healthcare, finance, e-
commerce, recommendation systems, etc.
6. Identifies Patterns: Finds hidden patterns and
relationships in data.
Disadvantages:
•   Requires Large Data: Needs a lot of data for good
performance.
• Time-Consuming Training: Training models can take a
lot of time and resources.
•   Complexity: Algorithms can be difficult to understand
and implement.
•   Overfitting Problem: Model may perform well on
training data but poorly on new data.
• High Cost: Requires powerful hardware and
infrastructure.
• No Human Understanding: ML lacks common sense
and cannot think like humans.
Attempt any 4
Q2   a.   What is genetic representation in genetic algorithms? Discuss [10]
its different types with suitable examples.
CO-2 ; SO-2 ;
BL-2
Answer:
Genetic representation means how a solution is encoded as a
chromosome in a Genetic Algorithm.
➢ Binary Representation
➢ Real Valued Representation
➢ Integer Representation
➢ Permutation Representation
➢ Tree Representation
Explain each type with suitable example.
Q2   b.   Explain the differences between Hard Computing and Soft   [10]
Computing with suitable examples.
CO-2 ; SO-2 ;
BL-2
Answer:
Feature   Hard Computing   Soft Computing
Uses
Uses exact   approximate
Definition   models to give   methods to give
precise results   near-optimal
results
Deterministic   Flexible and
Nature
(fixed rules)   adaptive
********** 3 **********
--- page 4 ---
Needs complete   Can handle
Data
and accurate   incomplete or
Requirement
data   uncertain data
Approximate
Output   Exact solution   (“good enough”)
solution
Error Tolerance   Very low   High tolerance
Mathematical   Human-like
Approach
and logical   reasoning
Can learn and
Learning Ability   No learning
adapt
Fuzzy logic,
Algorithms,   Neural networks,
Techniques Used
Boolean logic   Genetic
algorithms
Q3   a.   What are Genetic Algorithms in Artificial Intelligence?   [10]
Explain their advantages and disadvantages with an example.
CO-1 ; SO-2 ;
BL-2
Answer: A Genetic Algorithm (GA) is an optimization
technique inspired by natural evolution.
•   It works on a group of possible solutions (population)
and improves them step by step using selection,
crossover, and mutation to find the best or near-best
solution.
• GA is especially useful for complex problems where
normal optimization methods do not work well.
•   It works well for non-linear and complex problems.
•   It uses random (probabilistic) searching, not fixed
rules.
•   It does not need mathematical derivatives or gradient
information.
1. Advantages of Genetic Algorithm: Works for complex
problems: Genetic Algorithms can solve non-linear
and complex problems where traditional methods fail.
2. No mathematical derivatives needed: It does not
require gradient or derivative information, making it
suitable for real-world problems.
3. Parallel search capability: Multiple solutions are
processed at the same time, which increases the
chance of finding a good solution.
4. Flexible and adaptable: It can be applied to different
types of problems by changing the fitness function.
5. Robust method: It works well even when data is noisy
or incomplete.
1. Disadvantages of Genetic Algorithm: High
computational cost: Genetic Algorithms require more
********** 4 **********
--- page 5 ---
time and processing power, especially for large
populations.
2. No guarantee of exact optimal solution: GA usually
finds a near-optimal solution, not always the best
possible one.
3. Parameter tuning is difficult: Choosing proper values
for population size, crossover rate, and mutation rate
is challenging.
4. Slow convergence: GA may take many generations to
reach a good solution.
5. Problem-specific fitness design: Designing an effective
fitness function can be complex and time-consuming.
Example: Finding the Best Route to Reach College/Home
Q3   b.   What is Supervised Machine Learning? Explain its working in   [10]
CO-3 ; SO-2 ;   detail along with its advantages and disadvantages.
BL-2
Answer:
Supervised Machine Learning is a type of machine learning in
which the model is trained using labeled data.This means that
each input data is associated with a correct output, and the
model learns to map inputs to outputs based on this training
data.The main objective of supervised learning is to predict
the output for new, unseen data by learning patterns from the
given dataset.
Working of Supervised Machine Learning:
1. Collect Labeled Data
•   Gather a dataset where each input has a known
correct output (label).
•   Example: Images of handwritten digits with their
actual numbers as labels.
2. Split the Dataset
•   Divide the data into training data (about 80%) and
testing data (about 20%).
• The model will learn from the training data and be
evaluated on the testing data.
3. Train the Model
• Feed the training data (inputs and their labels) to a
suitable supervised learning algorithm (like Decision
Trees, SVM or Linear Regression).
• The model tries to find patterns that map inputs to
correct outputs.
4. Validate and Test the Model
•   Evaluate the model using testing data it has never
seen before.
********** 5 **********
--- page 6 ---
• The model predicts outputs and these predictions are
compared with the actual labels to calculate accuracy
or error.
5. Deploy and Predict on New Data
• Once the model performs well, it can be used to
predict outputs for completely new, unseen data.
Advantages of Supervised learning:
•   Simplicity & clarity: Easy to understand and
implement since it learns from labeled examples.
• High accuracy: When sufficient labeled data is
available, models achieve strong predictive
performance.
•   Versatility: Works for both classification like spam
detection, disease prediction and regression like price
forecasting.
•   Generalization: With enough diverse data and proper
training, models can generalize well to unseen inputs.
• Wide application: Used in speech recognition, medical
diagnosis, sentiment analysis, fraud detection and
more.
Disadvantages of Supervised learning:
•   Requires labeled data: Large amounts of labeled
datasets are expensive and time-consuming to
prepare.
•   Bias from data: If training data is biased or
unbalanced, the model may learn and amplify those
biases.
•   Overfitting risk: Model may memorize training data
instead of learning general patterns, especially with
small datasets.
•   Limited adaptability: Performance drops significantly
when applied to data distributions very different from
training data.
• Not scalable for some problems: In tasks with millions
of possible labels like natural language, supervised
labeling becomes impractical.
Q4   a.   Explain the concept of a Hypothesis. Discuss the different   [10]
CO-1 ; SO-2 ;   types of Hypothesis with suitable examples.
BL-1,2
• Answer: A hypothesis is an assumption that is made
based on some evidence.
This is the initial point of any investigation that
translates the research questions into predictions.
•   It includes components like variables, population and
the relation between the variables.
• A research hypothesis is a hypothesis that is used to
test the relationship between two or more variables.
********** 6 **********
--- page 7 ---
•   Simple Hypothesis: It shows a relationship between
one dependent variable and a single independent
variable.
•   For example – If you eat more vegetables, you will lose
weight faster.
•   Here, eating more vegetables is an independent
variable, while losing weight is the dependent
variable.
• Complex Hypothesis: It shows the relationship
between two or more dependent variables and two or
more independent variables.
•   Eating more vegetables and fruits leads to weight loss,
glowing skin, and reduces the risk of many diseases
such as heart disease.
•   Null Hypothesis: It provides a statement which is
contrary to the hypothesis.
•   It’s a negative statement, and there is no relationship
between independent and dependent variables.
• The symbol is denoted by “HO”.
•   Eg: There is no difference in marks between boys and
girls.
•   There is no difference screen time between
teenagers and adults.
•   There is no relationship between sugar intake and
obesity.
•   Alternate Hypothesis: It states there is a relationship
between two variables under research.
• Change in the independent variable effect the
dependant variable.
• The symbol is denoted by “Ha /H1”.
•   Eg: There is a strong relationship between sugar
intake and obesity.
•   Directional Hypothesis: It shows how a researcher is
intellectual and committed to a particular outcome.
The relationship between the variables can also
predict its nature.
•   For example- children aged four years eating proper
food over a five-year period are having higher IQ
levels than children not having a proper meal.
•   Students who study daily will score higher marks than
students who study occasionally.
•   This shows the effect and direction of the effect.
•   Non-directional Hypothesis: It is used when there is
no theory involved.
•   It is a statement that a relationship exists between
two variables, without predicting the exact nature
(direction) of the relationship.
•   Eg: There is a significant difference in exam
performance between student who attend online
classes and those who attend offline classes.
•   (It does not say which group performs better)
********** 7 **********
--- page 8 ---
•   Sugar intake effects human health.
Q4   b.   Explain the steps involved in the generational cycle of a   [10]
CO-2 ; SO-2 ;   genetic algorithm in detail.
BL-3
Answer:
• The generational cycle is the process of repeating GA
steps to improve solutions.
•   In each generation, the algorithm performs:
•   Selection – choose the best chromosomes.
•   Crossover – combine parents to create
offspring.
•   Mutation – make small random changes.
• Replacement – form a new generation.
•   This cycle repeats until the best or optimal
solution is found.
Explain each in detail
Q5   a.   Explain the principles and applications of evolutionary   [10]
CO-1 ; SO-2 ;   processes in detail.
BL-2
Answer: 1. Population-Based Approach
• Works with a set of solutions (population) instead of a
single solution.
• Each solution is called an individual.
•   2. Survival of the Fittest
•   Better solutions have higher chances of survival and
reproduction.
• Poor solutions are gradually eliminated.
3.Fitness Evaluation
• Each individual is evaluated using a fitness function.
•   Fitness measures how good a solution is for the
problem.
4. Selection
•   Fittest individuals are selected as parents for the next
generation.
•   Ensures good traits are passed forward.
5. Variation (Crossover & Mutation)
•   Crossover combines traits of parents to produce new
solutions.
•   Mutation introduces small random changes to
maintain diversity.
6.Adaptation Over Generations
•   Population improves gradually with each generation.
• Mimics biological evolution.
********** 8 **********
--- page 9 ---
7. Diversity Maintenance
•   Maintains variation in the population.
•   Prevents premature convergence to poor solutions.
8. Randomness with Guidance
• Uses randomness, but guided by fitness values.
•   Balances exploration and exploitation.
9. Termination Condition
•   Process stops when:
•   Desired fitness is achieved, or
• Maximum generations are completed.
Applicatios: Optimization problems
▪ Machine learning
▪ Scheduling and planning
▪ Robotics and control systems
Q5   b.   Explain Fuzzy Neural Networks (FNN). Discuss their   [10]
CO-2 ; SO-2 ;   advantages and disadvantages in detail.
BL-3
Answer: Fuzzy Neural Networks (FNN) are hybrid intelligent
systems that combine the structural learning capabilities of
artificial neural networks (ANNs) with the linguistic
reasoning and uncertainty-handling of fuzzy logic.
By embedding fuzzy sets into neural architectures, FNNs
optimize rule-based systems through training, enhancing
precision while maintaining high transparency.
They are heavily used in control systems, pattern recognition,
and data modeling, with key applications including pattern
classification and function approximation.
Advantages of FNN: 1. High Accuracy
• FNN gives more accurate results compared to using
fuzzy logic or neural networks alone
•   This is because it learns from data and also uses rules
Example: Better prediction in medical diagnosis
•   2. Can Learn and Adapt
• FNN can learn from past data (training)
•   It can improve its performance over time
Example: A system that becomes better at predicting
results after more usage.
•   3. Handles Uncertainty
•   It can work with unclear, incomplete, or noisy data
• Uses fuzzy logic to handle vague information
Example: Understanding “slightly hot” or “very cold”
•   4. Combines Strengths of FL and NN
• Fuzzy Logic → Good at reasoning and handling
uncertainty
********** 9 **********
--- page 10 ---
•   Neural Networks → Good at learning from data
FNN combines both to give better and smarter results
Disadvantages of FNN: Complex Structure: Has many layers
and components, making it complicated to understand and
build.
•   Requires More Computation
• Needs more processing power and time to work
compared to simple systems.
• Needs Training Data
•   Requires sufficient data to learn and perform well.
Difficult to Design
•   Designing rules and network structure is challenging
and needs expertise.
Q6   a.   Explain the different types of AI problems with suitable   [10]
CO-1 ; SO-2 ;   examples in detail.
BL-1,2
Answer:
1. Search problems – finding a solution path
2. Knowledge representation & reasoning – using facts
and rules
3. Planning problems – deciding a sequence of actions
4. Learning problems – improving performance from
experience
5. Perception problems – interpreting sensory data
(vision, speech)
Explain ALL in detail
Q6   b.   What is Random Forest? Explain its working in detail. Also   [10]
CO-3 ; SO-2 ;   discuss its advantages and disadvantages.
BL-3
Answer: Random Forest is a supervised machine learning
algorithm used for both classification and regression tasks. It
is an ensemble learning method, which means it combines
multiple models (Decision Trees) to improve overall
performance.Instead of using a single decision tree, Random
Forest builds many decision trees and combines their outputs
to make a final prediction.This process reduces errors and
improves accuracy.
❑ How Random Forest Works
1. It creates multiple subsets of the original dataset
using random sampling (bootstrap sampling).
2. For each subset, a Decision Tree is built.
3. Each tree makes its own prediction.
4. The final output is decided by:
1. Majority voting (for classification)
2. Average (for regression)
❑ Advantages
• High accuracy
********** 10 **********
--- page 11 ---
•   Handles missing values and large data efficiently
• Reduces overfitting
• Works for both classification and regression
❑ Disadvantages
• More complex than a single decision tree
•   Requires more computation and memory
•   Less interpretable (harder to understand decisions)
Q7   a. A salesman has to visit 4 cities (A, B, C, D). The distances   [10]
CO-2 ; SO-2 ;   between the cities are given below:
BL-2   A   B   C   D
A   0   10   15   20
B   10   0   35   25
C   15   35   0   30
D   20   25   30   0
Find the optimal route for the salesman starting from city A
using the Travelling Salesman Problem approach. Also
calculate the minimum cost.
Answer:
We evaluate all possible routes starting and ending at A.
Step 1: List possible routes
1. A → B → C → D → A
2. A → B → D → C → A
3. A → C → B → D → A
4. A → C → D → B → A
5. A → D → B → C → A
6. A → D → C → B → A
Step 2: Calculate total cost
1. A-B-C-D-A = 10 + 35 + 30 + 20 = 95
2. A-B-D-C-A = 10 + 25 + 30 + 15 = 80
3. A-C-B-D-A = 15 + 35 + 25 + 20 = 95
4. A-C-D-B-A = 15 + 30 + 25 + 10 = 80
5. A-D-B-C-A = 20 + 25 + 35 + 15 = 95
6. A-D-C-B-A = 20 + 30 + 35 + 10 = 95
Step 3: Find minimum cost
Minimum cost = 80
********** 11 **********
--- page 12 ---
Step 4: Optimal route
• A → B → D → C → A
• A → C → D → B → A
Final Answer
The optimal route is A → B → D → C → A (or A → C → D → B →
A) with a minimum cost of 80.
Q7   b.   Explain Hierarchical Clustering in detail.   [10]
CO-3 ; SO-2 ;
BL-1,2   Answer: Hierarchical Clustering is an unsupervised machine
learning algorithm used to group data points into clusters in a
hierarchical (tree-like) structure.
•   It does not require specifying the number of clusters
in advance.
• The result of hierarchical clustering is usually
represented using a dendrogram, which shows how
clusters are formed step by step.
How Hierarchical Clustering Works
•   Calculate the distance between all data points
• Merge or split clusters based on similarity
•   Repeat the process until a stopping condition is
reached.
•   Benefits
• Works well with small datasets
•   Provides clear hierarchy of clusters
• No need to specify K initially
Limitations
•   Computationally expensive for large datasets
•   Difficult to decide where to cut the dendrogram
•   Sensitive to noise and outliers
Examples:
• Customer segmentation
• Document clustering
•   Biological classification (taxonomy)
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 281e94e40c2c

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/Integrated_IT_7037/Introduction to Soft Computing Techniques/ANS_Introduction to Soft Computing Techniques(701IT0C011)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2025
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Introduction to Soft Computing Techniques
Date: 09 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 Questions.
6. In all 5 Questions to be attempted.
7. All Questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
a.   Define following terms in Genetic algorithm
• Mutation
• Gene
• Mutation: Mutation is a genetic algorithm operation that
introduces small random changes in an individual’s genetic
CO-1; BL-L   representation (chromosome) to maintain diversity and avoid   [5 M]
premature convergence. It helps explore new potential solutions
by altering one or more genes in a chromosome.
• Gene: A gene is the basic unit of a chromosome in a genetic
algorithm, representing a single parameter or trait in the solution
space. It holds a specific value (allele) that contributes to
defining an individual solution.
b.   Discuss working of an Intelligent agent in AI.
An intelligent agent in AI is an autonomous entity that perceives its
environment through sensors and acts upon it using actuators to achieve   [5 M]
CO-3,BL-L
specific goals. It follows a perception-action cycle and can be classified
as simple reflex agents, model-based agents, goal-based agents, utility-
based agents, and learning agents. Intelligent agents are used in
robotics, recommendation systems, and autonomous vehicles.
********** 1 **********
--- page 2 ---
c.   Identify and explain the advantages of the Fuzzy Logic
Fuzzy logic is a mathematical approach used for reasoning under
uncertainty. Its advantages include:
• Handling Uncertainty: Deals with imprecise and vague data
effectively.
• Robustness: Provides flexibility and fault tolerance in decision-
CO-2; BL-M   making.   [5 M]
• Better Representation of Human Reasoning: Mimics human
decision-making by handling degrees of truth.
•   Applicability in Various Domains: Used in control systems,
medical diagnosis, and AI applications.
• Improves Efficiency: Reduces computational complexity in
decision processes.
d.   Examine the features of Machine Learning and evaluate its significance.
Features of Machine Learning:
• Pattern Recognition: Identifies hidden patterns in data.
• Adaptability: Learns from past data and improves over time.
• Automation: Reduces manual intervention in decision-making.
CO-1; BL-M   •   Scalability: Can process large datasets efficiently.   [5 M]
• Predictive Capability: Forecasts future outcomes based on
learned patterns.
Significance: Machine learning is crucial in modern technology,
impacting industries like healthcare (disease prediction), finance (fraud
detection), and e-commerce (recommendation systems). It enhances
efficiency, accuracy, and automation across various domains.
Q2   [20]
a.   "Imagine you are working with a dataset of customer information for an
e-commerce platform. You are tasked with creating a model to predict
customer churn based on past behaviours.
a) Which type of Machine Learning (Supervised or Unsupervised)
would you choose for this task and why?
CO-1; BL-L   b) If you were given the same dataset but without labels or target   [10 M]
outcomes, how would your approach change?"
********** 2 **********
--- page 3 ---
• Supervised Learning: Since the problem involves predicting
churn based on labeled past behaviors, supervised learning is the
best choice. It enables classification models like decision trees,
logistic regression, and neural networks to learn from historical
data and make accurate predictions.
• Unsupervised Learning Approach: If the dataset lacks labels,
an unsupervised learning method like clustering (e.g., K-Means,
DBSCAN) can be used to segment customers based on similar
behaviors, which can later be analyzed for churn patterns.
b.   Analyze and contrast Genetic Algorithms with Traditional Algorithms,
providing examples to support your comparison
• Traditional Algorithms: Follow a predefined sequence of
operations and are deterministic (e.g., sorting, searching
CO-1; BL-M   algorithms).   [10 M]
• Genetic Algorithms (GA): Inspired by natural selection, they
use evolution-based techniques like selection, crossover, and
mutation to find optimal solutions.
• Example: In optimization problems like the Traveling Salesman
Problem (TSP), GA provides near-optimal solutions where
traditional brute-force approaches become inefficient.
Q3   [20]
a.   Explain the fundamental principles of Machine Learning, including the types
of learning paradigms, and how they are applied in real-world scenarios.
Provide examples to illustrate each principle.
CO-2; BL-M   • Supervised Learning: Learns from labeled data (e.g., spam   [10 M]
detection, credit scoring).
• Unsupervised Learning: Identifies patterns in unlabeled data
(e.g., customer segmentation).
• Reinforcement Learning: Learns through trial and error by
maximizing rewards (e.g., game-playing AI, robotics).
b.   Illustrate an example where K-Means Clustering can be applied in real-world
scenarios, such as segmenting customers in an online store based on their
purchase behavior.
CO-3; BL-H   [10 M]
K-Means clustering can segment customers based on purchasing
behavior in an online store. Customers with similar buying habits are
********** 3 **********
--- page 4 ---
grouped, allowing businesses to personalize marketing strategies for
each segment.
Q4   [20]
a.   Describe and classify the concept of Crossover and its various types in the
context of genetic algorithms, providing an appropriate diagram to illustrate
the concepts.
Crossover is a genetic operation that combines two parent solutions to
CO-1; BL-M   produce offspring. Types:   [10 M]
• Single-Point Crossover
• Two-Point Crossover
• Uniform Crossover
b.   Illustrate and describe the functioning of a Goal-Based Agent, providing an
appropriate diagram to support your explanation.
CO-3; BL-L   [10 M]
A goal-based agent takes actions based on achieving specific goals
rather than just reacting to the environment. Example: Pathfinding AI in
navigation systems.
Q5   [20]
a.   Describe the working process of a Genetic Algorithm and explain the role of
Mutation within the algorithm.
Genetic Algorithm follows:
•   Initialization
CO-1; BL-M   •   Selection   [10 M]
• Crossover
• Mutation
• Termination
Mutation Role: Helps maintain diversity and prevents premature
convergence.
CO-1; BL-H   b.   Explain following Terminologies Related to the Regression Analysis   [10 M]
I.   Dependent Variable
********** 4 **********
--- page 5 ---
II.   Independent Variable
III.   Outliers
IV.   Multi collinearity
V.   Under fitting and Overfitting
Regression Analysis Terminologies:
• Dependent Variable: Outcome being predicted.
• Independent Variable: Input feature influencing the dependent
variable.
•   Outliers: Data points significantly different from others.
•   Multicollinearity: High correlation between independent
variables.
• Underfitting & Overfitting: Poor generalization due to either
oversimplification or excessive complexity.
Q6   [20]
a.   Compare and contrast Machine Learning and Artificial Intelligence,
highlighting their key differences and applications
CO-3; BL-M   • AI is a broader concept; ML is a subset of AI that learns from   [10 M]
data.
• AI includes rule-based systems; ML focuses on data-driven
learning.
• AI applications: Expert Systems, NLP; ML applications: Fraud
Detection, Image Recognition.
b.   Define Unsupervised Machine Learning and illustrate the concept with a
suitable diagram
Unsupervised Machine Learning is a type of machine learning where
algorithms analyze and categorize data without labeled outputs. It
identifies hidden patterns, relationships, and structures within the data
without explicit supervision.
CO-1; BL-L   [10 M]
Key Features:
• Works with unlabeled data.
• Finds patterns and clusters without predefined categories.
• Common algorithms: K-Means clustering, Hierarchical
Clustering, Principal Component Analysis (PCA).
• Used in customer segmentation, anomaly detection, and
recommendation systems.
********** 5 **********
--- page 6 ---
Q7   Write a note on :   [20]
a.   Advantages and Disadvantages of Fuzzy Logic
Advantages & Disadvantages of Fuzzy Logic:
• Advantages: Handles uncertainty, mimics human reasoning,
CO-2; BL-H   flexible decision-making.   [10 M]
• Disadvantages: Lacks clear boundaries, computational
complexity.
b.   Directional Hypothesis and Non-Directional Hypothesis
•   Directional: Predicts a specific relationship (e.g., "Increased
CO-3; BL-M   study time improves scores").   [10 M]
• Non-Directional: Indicates a relationship exists without
specifying direction (e.g., "Study time affects scores").
********** 6 **********
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper ba7e37310ce0

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/Integrated_IT_7037/Introduction to Soft Computing Techniques/ANS_Introduction to Soft Computing Techniques(701IT0C011)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2025
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Introduction to Soft Computing Techniques
Date: 11 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 Questions.
6. In all 5 Questions to be attempted.
7. All Questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
a.   Explain the role of the Inference Engine in a Fuzzy Logic System.
The inference engine in a fuzzy logic system is responsible for applying
logical rules to the given input data to derive meaningful outputs. It
performs the following tasks:
•   Fuzzification: Converts crisp inputs into fuzzy values using
CO-1; BL-L   membership functions.   [5 M]
• Rule Evaluation: Applies fuzzy rules defined in the rule base to
determine relationships between inputs and outputs.
• Aggregation: Combines the results of multiple rules.
•   Defuzzification: Converts fuzzy outputs back into crisp values
for decision-making
b.   Discuss the Characteristics of the Hypothesis.
A hypothesis is a tentative assumption or statement used for testing and
research. Characteristics include:
CO-3,BL-L   [5 M]
•   Testability: It must be possible to test the hypothesis through
experiments or observations.
•   Specificity: Clearly defines the variables and relationships.
•   Simplicity: Should be as simple as possible while explaining the
phenomenon.
********** 1 **********
--- page 2 ---
• Consistency: Should align with existing knowledge and
theories.
•   Predictability: Allows for predictions about future observations.
c.   Define following terms in genetic algorithm
a. Fitness Function
b. Genetic Operators
CO-2; BL-M   •   Fitness Function: Measures how good a potential solution is   [5 M]
compared to others. It helps guide the selection of the best
individuals in a population.
• Genetic Operators: These are mechanisms that evolve the
population, including selection, crossover, and mutation to
create new generations of solutions.
d.   Discuss applications of Machine Learning.
Machine Learning is widely used in various domains, including:
• Healthcare: Disease diagnosis, personalized treatment, and drug
discovery.
• Finance: Fraud detection, credit scoring, and algorithmic
CO-1; BL-M   trading.   [5 M]
•   Retail: Customer segmentation, recommendation systems, and
inventory management.
• Autonomous Systems: Self-driving cars and robotics.
• Natural Language Processing: Chatbots, speech recognition,
and machine translation.
Q2   [20]
a.   Analyze the working of the K-Means Clustering algorithm, describing the
process of assigning data points to centroids and updating them until the
clusters are formed.
CO-1; BL-L   [10 M]
K-Means Clustering is an unsupervised learning algorithm used for data
segmentation:
1. Choose the number of clusters (K).
2. Initialize K centroids randomly.
3. Assign each data point to the nearest centroid.
********** 2 **********
--- page 3 ---
4. Update centroids by computing the mean of the assigned points.
5. Repeat steps 3 and 4 until convergence.
6. Final clusters are formed when centroids stabilize.
b.   Compare and contrast Classical Set Theory and Fuzzy Set Theory
Feature   Classical Set Theory   Fuzzy Set Theory
Elements either belong or Elements have degrees of
Membership
CO-1; BL-M   don’t (0 or 1)   membership (0 to 1)   [10 M]
Clearly defined   Handles imprecise or vague
Precision
boundaries   information
A person is either tall or A person can be tall to some
Example
not   degree
Q3   [20]
a.   Analyze the relationship between Machine Learning and Artificial
Intelligence, highlighting their similarities and differences.
• Machine Learning (ML) is a subset of Artificial Intelligence
(AI).
• AI aims to create machines that simulate human intelligence.
CO-2; BL-M   • ML enables systems to learn from data and improve without   [10 M]
explicit programming.
• AI applications include expert systems, robotics, and decision-
making.
• ML applications include speech recognition, fraud detection,
and recommendation systems.
b.   Given a problem with a large search space, how would you design a Genetic
Algorithm to find an optimal solution?
Designing a Genetic Algorithm for a large search space.
1. Initialization: Generate a random population of potential
CO-3; BL-H   solutions.   [10 M]
2. Fitness Evaluation: Assess solutions using a fitness function.
3. Selection: Choose the best individuals based on fitness scores.
4. Crossover: Combine pairs of solutions to create offspring.
5. Mutation: Introduce random changes to maintain diversity.
6. Iteration: Repeat the process until the best solution is found.
********** 3 **********
--- page 4 ---
Q4   [20]
a.   Discuss characteristics and types of hypotheses with suitable example.
haracteristics and types of hypotheses.
•   Characteristics: Testable, specific, simple, consistent, and
predictive.
• Types:
CO-1; BL-M   [10 M]
o Null Hypothesis (H0): No relationship exists.
o Alternative Hypothesis (H1): A relationship exists.
o Directional Hypothesis: Specifies direction (increase or
decrease).
o Non-Directional Hypothesis: Only states existence of a
relationship.
b.   Compare and contrast Soft Computing and Hard Computing.
Feature Soft Computing Hard Computing
Computational approach that   Traditional computing
Definition deals with approximation,   based on precise logic and
uncertainty, and learning.   deterministic algorithms.
Flexible, adaptive, and capable of   Rigid, rule-based, and
Nature
handling imprecise data.   requires exact inputs.
Fuzzy Logic, Neural   Binary Logic,
Techniques Networks, Genetic   Deterministic Algorithms,
Used   Algorithms, Evolutionary   Conventional
Computing.   Programming.
Handling   Can deal with vague, noisy, Requires exact and well-
Uncertainty   or incomplete data.   defined input data.
Capable of learning and
CO-3; BL-L   Learning   adapting (e.g., Neural   Cannot learn; follows pre- [10 M]
Ability   programmed rules.
Networks).
Processing May require more computational Generally faster due
Speed   time due to iterative learning.   to predefined logic.
Arithmetic Operations,
AI, Robotics, Pattern
Example   Database Management,
Recognition, Natural
Applications   Traditional Software
Language Processing.
Systems.
•   Soft Computing: Deals with approximation and uncertainty
(e.g., fuzzy logic, neural networks).
• Hard Computing: Uses precise rules and logic (e.g., traditional
algorithms).
********** 4 **********
--- page 5 ---
Q5   [20]
a.   Discuss Key components of a problem space.
Key components of a problem space.
1. Initial State - The starting point.
CO-1; BL-M   2. Operators - Actions that can be performed.   [10 M]
3. Goal State - The desired solution.
4. Path Cost - The cost to move from one state to another.
b.   Compare and contrast Neural Network and Fuzzy Logic.
Feature   Neural Network (NN)   Fuzzy Logic (FL)
Mimics the human brain Uses human-like
Concept   using interconnected   reasoning with degrees of
nodes (neurons)   truth (fuzziness)
Data   Requires large datasets Works well with expert-
Dependency   for training   defined rules
Learns from data using
Learning   Rule-based system, does
backpropagation and
Method   not require learning
CO-1; BL-H   optimization   [10 M]
Transparent and
Acts as a "black box"
Interpretability   explainable decision-
(difficult to interpret)
making
Learns from patterns but Handles imprecise and
Handling
struggles with   vague information
Uncertainty
uncertainty   effectively
Control systems (e.g., air
Image recognition,
Example   conditioners, washing
speech processing,
Applications   machines), decision
autonomous systems
support systems
Q6   [20]
a.   How do mutation and crossover contribute to the efficiency of Genetic
Algorithms?
Role of Mutation and Crossover in Genetic Algorithms.
CO-3; BL-M   • Crossover: Combines genes of parents to create offspring,   [10 M]
promoting diversity.
• Mutation: Introduces random changes to prevent premature
convergence.
b.   Compare and contrast supervised and unsupervised machine learning.
CO-1; BL-L   [10 M]
********** 5 **********
--- page 6 ---
feature   Supervised Learning   Unsupervised Learning
Data
Requires labelled data Uses unlabelled data
Labels
Classification,   Clustering, Dimensionality
Task
Regression   Reduction
Example Spam Detection   Customer Segmentation
Q7   Write a note on :   [20]
a.   Reinforcement Learning (RL)
• Learning method based on rewards and penalties.
• Used in robotics, self-driving cars, and game AI.
Reinforcement Learning (RL) is a type of machine learning where an
agent learns to make decisions by interacting with an environment to
maximize cumulative rewards. It is inspired by behavioral psychology
and is widely used in fields like robotics, gaming, and finance.
Key Components of RL:
1. Agent: The decision-maker (e.g., a robot, AI model).
2. Environment: The external system the agent interacts with.
3. State (S): The current situation or condition of the environment.
4. Action (A): The set of choices available to the agent.
5. Reward (R): Feedback received after taking an action (positive
or negative).
6. Policy (π): A strategy the agent follows to decide actions.
7. Value Function (V): Estimates the expected reward for being in
a certain state.
CO-2; BL-H   [10 M]
Types of Reinforcement Learning:
• Model-Based RL: The agent builds a model of the environment.
• Model-Free RL: The agent learns purely through trial and error.
Popular RL Algorithms:
• Q-Learning: A value-based algorithm that learns an optimal
action-selection policy.
• Deep Q-Network (DQN): Uses neural networks to approximate
Q-values.
• Policy Gradient Methods: Learn a policy directly instead of
estimating Q-values.
Applications of RL:
• Autonomous Vehicles: Learning to drive in different
environments.
• Game AI: Training AI to play games like Chess and Go.
• Robotics: Teaching robots to perform complex tasks.
• Finance: Optimizing stock trading strategies.
********** 6 **********
--- page 7 ---
b.   key aspects of the problem space in soft computing
• Uncertainty Handling: Works with vague data.
CO-3; BL-M   • Adaptability: Learns from changes in the environment.   [10 M]
•   Parallel Processing: Uses multiple approaches for better results.
********** 7 **********
````
