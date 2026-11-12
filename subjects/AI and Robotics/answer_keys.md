# AI and Robotics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 2786b021be04

- Departments: Information Technology
- Programmes: BTech IT 7001, Integrated IT 7037, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_IT_7001/AI and Robotics/ANS_AI and Robotics(702IT0E013)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: AI and Robotics
Date: 01 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1   Synoptic:   [20]
CO-1, A.   Define Artificial Intelligence. List any four key application areas of AI.   5
BL-1
Answer:
Artificial Intelligence (AI) is the branch of computer science focused on
creating systems capable of performing tasks that usually require human
intelligence, such as learning, reasoning, problem-solving, and perception.
Four key AI application areas:
1. Natural Language Processing (NLP)
2. Robotics
3. Computer Vision
4. Expert Systems
Evaluation Rubric:
•   Clear, correct AI definition: 2 marks
•   Listing four relevant AI applications: 3 marks
CO-2, B.   Explain the key differences between supervised and unsupervised learning?   5
BL-2
Answer:
• Supervised learning: The model learns from labeled data where
each input has a corresponding output. It maps inputs to outputs to
make predictions.
• Unsupervised learning: The model learns from unlabeled data by
identifying patterns or groupings without predefined outputs.
Key differences:
1. Data type: labeled vs unlabeled
********** 1 **********
--- page 2 ---
2. Goal: prediction vs pattern discovery
3. Examples: classification/regression vs clustering/dimensionality
reduction
Evaluation Rubric:
• Explanation of supervised learning: 2 marks
• Explanation of unsupervised learning: 2 marks
• Clear key differences: 1 mark
CO-2, C.   What is predicate logic? Give an example to apply predicate and its   5
BL-3   arguments.
Answer:
Predicate logic is a formal system in logic where predicates represent
properties or relations that take arguments. It extends propositional logic by
expressing statements involving variables and quantifiers.
Example:
Predicate: Likes(x, y) means "x likes y".
Applying: Likes(John, IceCream) means "John likes ice cream."
Evaluation Rubric:
•   Correct definition: 2 marks
•   Suitable example with predicate and arguments: 3 marks
CO-3, D.   Analyse the role of the four Denavit-Hartenberg (D-H) parameters in   5
BL-4   defining the relationship between two consecutive robot links
Answer:
The four D-H parameters standardize the description of spatial
relationships between adjacent robot links:
1. θ (theta): Joint angle — rotation about the z-axis
2. d: Link offset — translation along the z-axis
3. a: Link length — translation along the x-axis
4. α (alpha): Link twist — rotation about the x-axis
They allow for systematic frame assignment and calculation of
transformation matrices that relate consecutive links.
Evaluation Rubric:
•   Identification and definition of all four parameters: 3 marks
•
Q2   [20]
CO-1, A.   Explain the fundamental concepts of Propositional Logic, including a   10
BL-2   definition of a proposition, a description of the five main logical
********** 2 **********
--- page 3 ---
connectives with their symbols and truth tables, and translate the following
sentence into a symbolic expression, defining your propositions:
"If the system is not offline and the connection is stable, then I can either
download the files or I will read the manual."
Answer:
• Proposition: A declarative statement that is either true or false.
• Logical connectives:
o Negation (¬)
o Conjunction (∧)
o Disjunction (∨)
o Implication (→)
o Biconditional (↔)
(Truth tables for each)
Translation:
Let:
P = System is offline
Q = Connection is stable
R = I can download files
S = I will read the manual
Symbolic expression:
(¬P ∧ Q) → (R ∨ S)
Evaluation Rubric:
•   Definition of proposition: 1 mark
•   List and explanation of connectives with truth tables: 4 marks
• Accurate symbolic translation and proposition definitions: 5 marks
CO-1, B.   List the four components of the PEAS framework used for defining a task   10
BL-1   environment. Apply this framework by providing a detailed PEAS
description for TWO of the following agents:
1. An automated medical diagnosis system
2. Part-picking robot in a warehouse
Answer:
PEAS Components:
• Performance measure
• Environment
• Actuators
• Sensors
Automated medical diagnosis system:
• Performance: Accuracy, speed of diagnosis
• Environment: Patient data, medical knowledge base
•   Actuators: Diagnostic report generation
•   Sensors: Medical tests, patient inputs
Part-picking robot:
********** 3 **********
--- page 4 ---
• Performance: Accuracy, speed, safety
• Environment: Warehouse
•   Actuators: Robot arm, gripper
•   Sensors: Cameras, proximity sensors
Evaluation Rubric:
•   Correct components listed: 2 marks
•   Detailed PEAS description for both agents: 8 marks
Q3   [20]
CO-3, A.   Given a specific robotic manipulator’s joint parameters, apply the concepts   10
BL-3   of forward and inverse kinematics to determine the end-effector position
and the required joint angles to reach a target point.
Answer:
• Forward kinematics: Calculate the position and orientation of the
end-effector given joint angles and link lengths, using
transformation matrices. For example, a 2-link planar arm:
x=l1cos⁡θ1+l2cos⁡(θ1+θ2)x = l_1 \cos \theta_1 + l_2
\cos(\theta_1 + \theta_2)x=l1cosθ1+l2cos(θ1+θ2)
y=l1sin⁡θ1+l2sin⁡(θ1+θ2)y = l_1 \sin \theta_1 + l_2 \sin(\theta_1
+ \theta_2)y=l1sinθ1+l2sin(θ1+θ2)
• Inverse kinematics: Given a target position (x,y), compute joint
angles (θ1,θ2\theta_1, \theta_2θ1,θ2) that achieve it by solving
equations.
Evaluation Rubric:
•   Correct forward kinematics application: 4 marks
• Proper inverse kinematics approach: 4 marks
• Clear presentation of calculations/results: 2 marks
CO-3, B.   Analyze the different classifications of robots. For each category, explain   10
BL-4   its characteristics and provide a real-life example that illustrates the
category.
Answer:
Classifications:
1. Structure-based:
o Articulated (e.g., KUKA robot arm): Multiple rotary joints,
flexible movement
o SCARA (Selective Compliance Assembly Robot Arm):
Horizontal assembly tasks
********** 4 **********
--- page 5 ---
o Cartesian: Linear movements along X, Y, Z (e.g., 3D
printers)
o Cylindrical: Rotation plus linear movement along axis
o Spherical: Rotation and two linear motions
2. Control-based:
o Autonomous
o Teleoperated
3. Application-based:
o Industrial robots
o Service robots
Examples:
•   Articulated: Industrial welding robot
• SCARA: Electronics assembly
•   Cartesian: CNC milling machine
Evaluation Rubric:
•   Correct classification and categories: 4 marks
• Clear characteristics analysis: 3 marks
• Relevant real-life examples: 3 marks
Q4   [20]
CO-2, A.   Discuss the architecture of an Artificial Neural Network and its learning   10
BL-2   process.
Answer:
• Architecture:
o Input layer: Receives input data
o Hidden layers: Perform weighted computations and feature
extraction
o Output layer: Outputs result or prediction
• Learning process:
o   Initialize weights randomly
o Forward propagation through layers
o Calculate error between predicted and actual output
o Backpropagation to update weights using gradient descent
o   Iterate until error minimized
Evaluation Rubric:
• Clear description of architecture: 4 marks
• Explanation of learning steps: 6 marks
CO-1, B.   Define the Universal Quantifier (∀) and the Existential Quantifier (∃).   10
BL-3   Translate the following sentences into well-formed formulas:
i.   "Every student has a backpack."
ii.   "There is a student who is sleeping."
********** 5 **********
--- page 6 ---
iii.   "All lions are fierce creatures."
Answer:
• Universal quantifier (∀): "For all"
•   Existential quantifier (∃): "There exists"
Translations:
i. "Every student has a backpack."
∀x (Student(x)→HasBackpack(x))\forall x \, (Student(x) \rightarrow
HasBackpack(x))∀x(Student(x)→HasBackpack(x))
ii. "There is a student who is sleeping."
∃x (Student(x)∧Sleeping(x))\exists x \, (Student(x) \wedge
Sleeping(x))∃x(Student(x)∧Sleeping(x))
iii. "All lions are fierce creatures."
∀x (Lion(x)→Fierce(x))\forall x \, (Lion(x) \rightarrow
Fierce(x))∀x(Lion(x)→Fierce(x))
Evaluation Rubric:
•   Correct quantifier definitions: 3 marks
• Accurate translations of all sentences: 7 marks
Q5   [20]
CO-2, A.   Illustrate how you would structure a simple Deep Neural Network for a   10
BL-3   basic image classification task. Specify the number of layers and the
purpose of each.
Answer:
•   Input layer: Accepts image pixels
• Convolutional layer(s): Extract spatial features
• Pooling layer(s): Downsample to reduce dimensionality
•   Fully connected layers: Combine features for classification
• Output layer: Softmax layer for class probabilities
Evaluation Rubric:
•   Correct layer identification and purposes: 6 marks
• Logical structure explanation: 4 marks
CO-3, B.   Discuss the types of robots based on geometry i.e. Cartesian, Cylindrical,   10
BL-2   Spherical, Articulated, and SCARA along with neat sketches.
********** 6 **********
--- page 7 ---
Answer:
•   Cartesian: Moves in X, Y, Z axes linearly
•   Cylindrical: Rotation plus linear movement along the axis
•   Spherical: Rotation and two linear movements forming spherical
workspace
•   Articulated: Rotary joints giving high flexibility
• SCARA: Selective compliance in horizontal plane
(Include neat sketches)
Evaluation Rubric:
•   Correct types and explanations: 5 marks
• Neat and accurate sketches: 5 marks
Q6   [20]
CO-2, A.   Compare and contrast Decision Tree Learning with Neural Network   10
BL-3   Learning.
Answer:
• Decision Tree: Rule-based, easy to interpret, splits data by features
• Neural Network: Uses layers and weights, learns complex patterns
via gradient descent
• Decision trees are interpretable but limited in complex tasks; neural
nets handle complex data but are black boxes
Evaluation Rubric:
• Clear comparison of learning methods: 5 marks
•   Contrast in advantages and disadvantages: 5 marks
CO-1, B.   Explain the difference in meaning between ∀x ∃y Loves(x, y) and ∃y ∀x   10
BL-2   Loves(x, y), assuming the domain is all people and the predicate Loves(x,
y) means "x loves y". Provide a clear English translation for each statement
that illustrates this difference and give an example where the first statement
is true but the second is false
Answer:
• ∀x ∃y Loves(x, y): Everyone loves someone (not necessarily the
same person)
• ∃y ∀x Loves(x, y): There is a particular someone loved by everyone
Example:
•   First true: Every person loves at least one celebrity (may be
different for each)
• Second false: No single person is loved by everyone
********** 7 **********
--- page 8 ---
Evaluation Rubric:
•   Correct explanation: 5 marks
• Accurate English translations: 3 marks
• Valid example illustrating difference: 2 marks
Q7   [20]
CO-3, A.   Describe in detail the different types of robot drives i.e. hydraulic,   10
BL-2   pneumatic, and electric. Mention their advantages and applications.
Answer:
• Hydraulic: Uses fluid pressure; high force output; used in heavy-
duty robots; bulky and noisy
• Pneumatic: Uses compressed air; fast actuation; less precise; used
in pick-and-place robots; low cost
•   Electric: Uses electric motors; precise control; widely used; limited
force compared to hydraulic
Advantages and applications:
•   Hydraulic: powerful but heavy
• Pneumatic: fast and cheap but less accurate
•   Electric: precise and clean but less powerful
Evaluation Rubric:
•   Description of all drives: 6 marks
• Advantages and applications: 4 marks
CO-3, B.   For a mobile robot designed to navigate an unknown indoor environment,   10
BL-5   evaluate the suitability of using ultrasonic sensors versus LiDAR sensors.
Justify your recommendation by weighing the pros and cons of each.
Answer:
• Ultrasonic: Low cost, affected by soft materials and environmental
noise, short range
• LiDAR: Expensive, highly accurate, provides detailed environment
mapping
• Recommendation: LiDAR preferred for precise indoor navigation
despite higher cost due to accuracy and resolution advantages
Evaluation Rubric:
•   Detailed comparison: 5 marks
•   Justified recommendation: 5 marks
********** 8 **********
````
