# Programming Logic and Techniques: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 8ba6148b7537

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Final-Exam/Bachelor of Science (Information Technology) - 45618/Programming Logic And Techniques/ANS_Final-Exam_Programming Logic And Techniques(NHPLT101)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 13 Oct 2025
- Text: text (11 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Science (Information Technology)
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Programming Logic and Techniques/Programming Logic
And Techniques
Time: 11:30 am - 01:30 pm
Date: 13 Oct 2025
(02:00 Hrs.)
Max Marks: 60
FINAL EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 11 pages
2. Each question carries equal marks
3. Answer to each new question to be started on a fresh page
4. Draw neat and clear diagrams wherever required
5. Students may add pseudocode or code snippet to the answer where relevant
6. For any psuedocode-based question, ensure to describe clearly
7. Figure on the right-hand side indicates full marks
Q1. Answer the following questions(Attempt Any 4 Questions)   20
a. Definition – 1 Mark, Example – 1 Mark, Reason – 3 Marks   5
A programming language is a formal notation consisting of a set of symbols, rules (syntax) and
meanings (semantics) used to write instructions that a computer can execute.
These are required for the following reasons:
-   Computers only understand binary (0s and 1s). Programming languages provide a
human-readable way of giving instructions that can be translated into machine code.
-   It provides human-readable constructs (variables, control structures, functions, data
types) that are translated into machine code by a compiler or interpreter
-   A language lets programmers’ express algorithms clearly and efficiently without writing
raw binary
-   Instead of worrying about how memory or CPU registers work, programmers can focus
on solving problems
-   Programmers can read, write, and understand instructions in a structured way.
Page 1 of 11
--- page 2 ---
-   Programming languages provide error messages, debugging tools, and structured error
handling. This ensures programs are more reliable than manually writing machine instructions
Example:
In Python, the statement print(5 + 3) tells the interpreter to evaluate 5 + 3 and display 8. The
interpreter parses the statement, computes the sum and sends the result to output. Without a
programming language, humans would have to write long, unreadable machine code for such
operations.
b. Explanation – 3 Marks   5
Programming languages are essential for automating repetitive or complex tasks, which
significantly reduces manual effort and increases efficiency. By writing programs, humans can
instruct computers to perform tasks automatically, saving time and minimizing errors.
-   Tasks that would take hours manually can be completed in seconds or minutes by a
program
-   Automation ensures tasks are performed consistently and without human errors
-   Computers can execute complicated sequences of steps without fatigue, which is difficult
for humans to perform manually
-   Developers can focus on higher-level problem-solving while repetitive tasks are handled
by programs
-   Automated programs can handle increasing amounts of work without extra manual effort
Example – 2 Marks
Before Automation: Companies used to calculate salaries, taxes, and deductions manually for
each employee. This was time-consuming and prone to errors.
After Automation: Now, payroll software written in programming languages like C, Python,
Java automatically calculates salaries, deducts taxes, generates payslips, and even deposits
money into bank accounts.
c. Defintiion - 1 Mark   5
Object-Oriented Programming (OOP) and Modularity:
Modularity in OOP refers to dividing a program into separate, independent, and reusable
components called classes and objects. Each class represents a specific entity or module with
its own data (attributes) and behavior (methods). Modularity makes programs organized, easier
to understand, maintain, and debug.
Components - 2 Marks
Components of Modularity in OOP:
1.   Class: A blueprint that defines attributes (data) and methods (functions) for an object.
2.   Object: An instance of a class that can perform the tasks defined in the class.
3.   Attributes: Features of the class that store the a certain value to the variable
Page 2 of 11
--- page 3 ---
4.   MEthods: Actions to be preformed by that class
Example – 2 Marks
Library Management System
We can divide the system into modular classes:
1.   Class Book:
o Attributes: title, author, isbn
o Methods: display_info(), check_availability()
2.   Class Member:
o Attributes: name, member_id
o Methods: borrow_book(), return_book()
3.   Class Library:
o Attributes: name, books_list, members_list
o Methods: add_book(), register_member(), lend_book()
Modularity in OOP allows developers to break complex systems into smaller, reusable, and
independent modules. By using classes and objects, programs become easier to manage, debug,
and expand. The Library Management System example clearly demonstrates how modular
components interact while maintaining independence
d. Scenario Examination – 1 Mark   5
The teacher has 200 answer sheets to grade.
Two possible approaches:
1.   Strict step-by-step marking scheme: Grade each answer according to predefined rules.
2.   Quick estimation based on patterns: Grade based on observed patterns without checking
every answer.
Identification of the Approach and Justification – 4 Marks
For this scenario, the algorithmic approach is more effective because:
·   Accuracy and fairness are critical in grading
·   Even a small error can affect student results
·   Heuristic shortcuts may be faster but can produce unreliable results
Algorithmic approach is preferred for grading answer sheets because it follows systematic,
step-by-step procedures, ensuring accuracy, fairness, and reliability. Heuristic methods may be
useful for quick estimations in less critical tasks but are not suitable for high-stakes evaluations
like grading
e. 4 Marks - Decomposition Tree   5
1 Mark - Identification of he root node, 3 child node, and leaf node, and specify the level of
the tree
Page 3 of 11
--- page 4 ---
f. Given terms are: 2, 3, 8, 27, 124   5
Step 1 - Comparing the terms - 1 Mark
2 = 2 - 1! = 2 - 1 = 1
3 = 3 - 2! = 3 - 2 = 1
8 = 8 - 3! = 8 - 6 = 2
27 = 27 - 4! = 27 - 24 = 3
124 = 124 - 5! = 124 - 120 = 4
The differences in term follow the pattern 1, 1, 2, 3, 4
Step 2 - Rule or pattern for the series - 2 Marks
From the differences above we see the additive increments after the first two terms increase by
1 each step: 1, 1, 2, 3, 4,....
For n = 1, the rule is n! + 1
For positions n = 2, 3, 4, 5,........ those increments equal n -1, So the rule is Tn = n! + (n - 1)
Step 3 - Checking the rule with the series - 1 Mark
n = 1 → T1 = 1! + 1 = 1
n = 2 → T2 = 2! + (2 - 1) = 2 + 1 = 3
Page 4 of 11
--- page 5 ---
n = 3 → T3 = 3! + (3 - 1) = 6 + 2 = 8
n = 4 → T4 = 4! + (4 - 1) = 24 + 3 = 27
n = 5 → T5 = 5! + (5 - 1) = 120 + 4 = 124
Step 4 - Using rule to predict the next three days count - 1 Mark
n = 6 → T6= 6! + (6 - 1) = 720 + 5= 725
n = 7 → T7 = 7! + (7 - 1) = 5040 + 6 = 5046
n = 8 → T8 = 8! + (8 - 1) = 40320 + 7 = 40327
So the next 3 predicted numbers in the series are: 725, 5046, 40327
Q2. Answer the following questions(Attempt Any 4 Questions)   20
a. Reasoning for why it is independent – 5 Marks   5
An algorithm is a step-by-step procedure to solve a problem. It is independent of any
programming language because:
1.   Logic vs Syntax
a. An algorithm focuses on the logic or steps required to solve a problem, not on the syntax
of a programming language.
b.   Example: Calculating the sum of two numbers can be written as a set of steps without
using Python, Java, or C++.
2.   Universal Understanding
a.   Algorithms can be expressed in natural language, pseudocode, or flowcharts, which can
be understood by anyone familiar with problem-solving concepts.
b.   Example:
1.   Take two numbers as input.
2. Add the numbers.
3.   Display the result.
This same algorithm can be implemented in any language.
3.   Reusability
a.   Because an algorithm is language-independent, it can be implemented in multiple
programming languages without changing its logic.
Example: Any algorithm like sorting a list of numbers can be implemented using Python or C
or C++, what matters is the logic must be correct and te steps should remain same
b. Explanation for 5 Marks - Each operator for 1.5 Marks + 0.5 Marks example   5
In logic programming, AND, OR, and NOT are logical operators used to combine conditions
and make decisions based on facts and rules
Page 5 of 11
--- page 6 ---
1. AND Operator (∧)
o Meaning: All conditions connected by AND must be true for the rule to be true.
o Example:
§ Rule: “I will go for a walk if it is sunny AND I have free time.”
§ Decision: Only if both conditions are true, the action occurs.
2. OR Operator (∨)
o Meaning: At least one of the conditions connected by OR must be true for the rule to be
true.
o Example:
§ Rule: “I will carry an umbrella if it is raining OR the weather forecast predicts rain.”
§ Decision: If either condition is true, the action occurs.
3. NOT Operator (¬)
o Meaning: Reverses the truth value of a condition. If a condition is true, NOT makes it false,
and vice versa.
o Example:
§ Rule: “I will not go outside if it is raining.”
§ Decision: If it is raining, the condition evaluates to false → I stay inside.
These operators can be combined to handle complex decision-making.
Example: Rule: “I will go outside if it is NOT raining OR I have an umbrella AND I am
wearing raincoat.” Decision: The combination of conditions is evaluated logically to decide the
action.
c. Issues – 2 Marks   5
a.   Step 3 uses OR which may turn AC ON even if the room is unoccupied and temperature
is below desired. Example: current = 18°C, desired = 22°C, room unoccupied → AC turns ON
instead of heater or staying off.
b.   Step 4 “maintain current state” may not correctly handle cases where temperature equals
desired
Rewriting the Algorithm – 3 Marks
Step 1: Input current temperature (T_current), desired temperature (T_desired), room
occupancy (Occupied)
Step 2: If Occupied = Yes:
If T_current < T_desired - 1:   // small buffer to avoid frequent switching
Turn Heater ON
Else if T_current > T_desired + 1:
Turn AC ON
Else:
Maintain current state
Page 6 of 11
--- page 7 ---
Else: // Room unoccupied
Maintain current state
Step 3: Print device status (Heater, AC, or None)
The correct algorithm may vary among students
d. Identification of problem – 2 Marks   5
a.   This algorithm solves the problem of aggregating daily travel durations into a total
b.   It automates calculation to ensure accuracy and saves time compared to manual addition
of daily hours
Explanation – 3 Marks
c.   The algorithm is designed to calculate the total travel time over multiple days
d.   It ensures that daily travel durations are summed to give a cumulative travel time, which
can be used for planning, reporting, or payroll purposes (e.g., for drivers or employees on
travel)
e.   Provides a single value representing total travel hours, giving an overview of the total
time invested in travel over the given period
e. Diagram with correct symbols, flow, and logic – 5 Marks   5
Start and Stop may be drawn either as a lozenge or oval
Page 7 of 11
--- page 8 ---
f. Algorithm with correct logic and written stepwise with clear conventions and instructions = 5   5
Marks
1.   Start
2. Read steps and exercise_time for the user
3. Check if steps are greater than or equal to 10000
d.   If Yes then proceed to Step 4
e.   If No then go to Step 6
4. Check if exercise_time is greater than or equal to 30
d.   If Yes, proceed to Step 5
e.   If No, go to Step 6
5.   Trigger alert: “Congratulations! You have achieved your daily activity goal.”
6.   If any condition is not met, do not trigger alert
7. End
Q3. Answer the following questions(Attempt Any 4 Questions)   20
a. Each point 1 mark   5
• A variable is a storage location in memory that can hold a value, which may change during
program execution.
• An assignment statement sets a variable to a specific value.
• The format in pseudocode:
Set <variable> = <value>
• Example:
Set age = 18
Set name = "Swati"
• Once assigned, the variable holds the value until it is updated with another assignment.
b. Each error 1 mark, rewriting 1   5
Errors in pseudocode: Mistakes in the given pseudocode
1. Formula for Simple Interest is wrong → should divide by 100, not 1000.
2. Output statement prints P (Principal) instead of SI.
3. Total Amount is wrongly calculated as P – SI; it should be P + SI.
4. Inputs should ideally be prompted separately for clarity.
DISPLAY "Enter Principal:"
INPUT P
Page 8 of 11
--- page 9 ---
DISPLAY "Enter Rate of Interest:"
INPUT R
DISPLAY "Enter Time (in years):"
INPUT T
// Calculate Simple Interest
SET SI = (P * R * T) / 100
DISPLAY "The Simple Interest is:" + SI
// Calculate Total Amount
SET TotalAmount = P + SI
DISPLAY "The Total Amount (Principal + Interest) is:" + TotalAmount
c. Variant A – Check inside loop   5
Logic: Loops through all numbers from 1 to N, adding only if the number is even (i % 2 =
0).
Advantages:
Simple and easy to understand.
Works for all numbers without worrying about starting point.
Disadvantages:
Checks every number, including odd ones, which is less efficient for large N.
Variant B – Increment by 2
Logic: Starts from 2 and increments by 2, summing only even numbers.
Advantages:
Only iterates over even numbers, reducing the number of loop iterations by half.
More efficient, especially for large N.
Disadvantages:
Page 9 of 11
--- page 10 ---
Slightly less intuitive for beginners.
Comparison / Which is more efficient?
Variant B (Increment by 2) is more efficient because it:
Avoids unnecessary checks for odd numbers.
Reduces loop iterations by roughly 50%, saving time and computational effort.
d.   5
Iteration   i   Condition (i > 0   Action (sum =   sum   Output
AND odd?)   sum + i)   after
update
1   -2   False (not > 0)   No   0   i = -2 Sum = 0
2   -1   False (not > 0)   No   0   i = -1 Sum = 0
3   0   False (not > 0)   No   0   i = 0 Sum = 0
4   1   True ( > 0 & odd)   sum = 0 + 1 = 1   1   i = 1 Sum = 1
5   2   False (even)   No   1   i = 2 Sum = 1
6   3   True ( > 0 & odd)   sum = 1 + 3 = 4   4   i = 3 Sum = 4
7   4   False (even)   No   4   i = 4 Sum = 4
8   5   True ( > 0 & odd)   sum = 4 + 5 = 9   9   i = 5 Sum = 9
e. MODULE FindMin(Integer a, Integer b, Integer c)   5
SET min = a
IF b < min THEN
SET min = b
END IF
IF c < min THEN
SET min = c
END IF
RETURN min
END MODULE
Page 10 of 11
--- page 11 ---
// Main Program
MODULE main( )
DECLARE Integer a, b, c, minimum
DISPLAY "Enter three numbers:"
INPUT a, b, c
SET minimum = FindMin(a, b, c)
DISPLAY "The smallest number is: " + minimum
END MODULE
f. FOR num = 1 TO 15   5
IF (num MOD 3 == 0) OR (num > 12 AND num MOD 2 == 0) THEN
DISPLAY num
END IF
END FOR
Page 11 of 11
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 0c1455499933

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Re-Exam/Bachelor of Science (Information Technology) - 45618/Programming Logic And Techniques/ANS_Final-Exam_Deep Learning(UADLE551)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 25 Mar 2026
- Text: text (10 pages)

````text
Synoptic
SVKM
SVKM's UPG College of Arts, Sci. & Com.
Programme: Master of Science (Artificial Intelligence and Data Science)
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Deep Learning
Date: 25 Mar 2026   Time: 08:00 am - 10:00 am (02:00 Hrs.)
Max Marks: 60
FINAL EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 10 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
1.   Attempt any three questions(Attempt Any 3 Questions)   15
a.   5
Page 1 of 10
--- page 2 ---
A perceptron is a supervised learning algorithm used for binary classification tasks. It consists
of input nodes, corresponding weights, a bias term, a summation unit, and an activation
function. Each input is multiplied by its respective weight, and all weighted inputs are summed
together. A bias term is added to shift the decision boundary if necessary.
Mathematically, the perceptron computes:
z=∑wixi+b
The result is passed through an activation function, typically a step function, which produces
the final output:
y=f(z)
If the weighted sum exceeds a threshold, the output is 1; otherwise, it is 0. This
mechanism creates a linear decision boundary separating two classes. The perceptron is
effective for linearly separable data but cannot model nonlinear relationships.
5
b. Forward Propagation Backpropagation
Page 2 of 10
--- page 3 ---
Forward Propagation Backpropagation
Computes output   Updates weights
Input → Output   Output → Input
Uses current weights   Adjusts weights
Forward propagation is the process of passing input data through the network layer by layer to
compute the final output. Each layer applies weights, adds bias, and uses an activation function
to produce output. This continues until the final prediction is obtained.
Backpropagation is the reverse process where the error between predicted and actual output is
propagated backward through the network. It computes gradients of the loss function with
respect to each weight using the chain rule of calculus.
Forward propagation generates predictions, while backpropagation adjusts weights to minimize
error. Together, they enable the neural network to learn from data efficiently.
c. The vanishing gradient problem occurs during backpropagation when gradients become   5
extremely small as they are propagated backward through multiple layers of a deep neural
network. This typically happens when activation functions like sigmoid or tanh are used, as
their derivatives are small for large positive or negative inputs.
When gradients become very small, weight updates in earlier layers become negligible. As a
result, those layers learn very slowly or may stop learning entirely. This significantly affects
the performance of deep networks, especially when many hidden layers are involved.
The impact includes slow convergence, poor feature learning in early layers, and difficulty
training very deep architectures. This problem historically limited the depth of neural
networks. Modern solutions such as ReLU activation, better weight initialization techniques
(He/Xavier), batch normalization, and residual connections help mitigate this issue.
d. Activation functions play a critical role in neural networks by introducing non-linearity into the   5
model. Without activation functions, a neural network composed of multiple layers would
behave like a simple linear regression model.
Nonlinearity allows the network to learn complex patterns and relationships in data. Activation
functions determine whether a neuron should be activated based on the weighted sum of inputs.
They also control the output range and influence gradient behavior during backpropagation.
Common activation functions include sigmoid, tanh, ReLU, and softmax.
By enabling hierarchical feature learning, activation functions make deep learning models
powerful and capable of solving complex real-world problems.
2.   Attempt any three questions(Attempt Any 3 Questions)   15
Page 3 of 10
--- page 4 ---
a. Mini-batch gradient descent divides the dataset into smaller subsets called batches. Instead of   5
computing gradients using the entire dataset (batch gradient descent) or using a single sample
(SGD), it computes gradients using a small group of samples.
This method reduces computational burden compared to full-batch training because smaller
batches require less memory. At the same time, it reduces the high variance seen in SGD
because gradients are averaged over multiple samples.
Mini-batch training also enables parallel processing, making it efficient when using GPUs or
TPUs. It often results in faster convergence and better generalization.
Because of its balance between stability and efficiency, mini-batch gradient descent has
become the standard optimization method in modern deep learning frameworks.
b. One common sign is a significant gap between training and validation accuracy. High training   5
accuracy combined with low validation accuracy indicates overfitting.
Another indicator is when validation loss increases while training loss decreases. This
divergence suggests that the model is learning noise from the training set.
Plotting training and validation curves helps identify these patterns. Early detection allows
corrective measures such as regularization or dropout to be applied.
c. Building and training a neural network in TensorFlow follows a structured workflow. The first   5
step involves importing required libraries such as TensorFlow and Keras. Next, the dataset is
loaded and preprocessed. Preprocessing may include normalization, encoding categorical
variables, and splitting the data into training, validation, and test sets.
After preparing the data, the model architecture is defined. This includes specifying the number
of layers, type of layers (Dense, Conv2D, etc.), number of neurons, and activation functions.
The model is then compiled by selecting an optimizer (e.g., Adam), a suitable loss function
(e.g., categorical cross-entropy), and performance metrics (e.g., accuracy).
Training is performed using the .fit() method, where the model learns by adjusting weights
through backpropagation. After training, the model is evaluated on test data using .evaluate()
and used for predictions with .predict().
This pipeline ensures systematic model development from data preparation to evaluation.
d. Adagrad adapts learning rates by accumulating squared gradients for each parameter.   5
Parameters that receive frequent updates get smaller learning rates, while infrequent
parameters get larger updates.
However, Adagrad’s accumulated gradients can grow large, causing learning rates to shrink
excessively over time.
Page 4 of 10
--- page 5 ---
RMSprop improves upon Adagrad by using an exponentially decaying average of squared
gradients rather than accumulating them indefinitely. This prevents learning rates from
becoming too small.
Adam further enhances this by combining momentum (first moment) and RMSprop (second
moment). It corrects bias in early training stages and provides stable and efficient optimization.
These adaptive algorithms significantly improve training performance in deep learning
applications.
3.   Attempt any three questions(Attempt Any 3 Questions)   15
a. While CNNs have revolutionized deep learning, they still have limitations in certain   5
applications.
Limitations:
Overfitting: If CNNs are trained on a small dataset, they memorize instead of generalizing.
This is a challenge in medical imaging, where datasets are limited.
Data Dependency: CNNs need massive labeled datasets for training, which is difficult in
some domains (e.g., Indian language OCR systems for ancient scripts).
Computational Cost: CNNs require powerful hardware like GPUs/TPUs, which may not be
affordable for small-scale Indian companies.
Solutions:
Data Augmentation: Creating synthetic images using rotation, cropping, and flipping can
help CNNs generalize better. This is used in handwriting recognition systems for Indian
regional languages.
Transfer Learning: Pre-trained models like VGG16, ResNet, and MobileNet can be fine-
tuned on a small dataset, reducing the need for large labeled datasets. This is commonly
used in AI-powered medical diagnostics in India.
Efficient Architectures: New models like MobileNet and EfficientNet are optimized for
mobile devices, making them practical for low-resource applications such as AI in rural
healthcare.
By addressing these limitations, CNNs can be effectively optimized for Indian scenarios such
as smart city projects, agricultural monitoring, and AI-based security surveillance.
b. A CNN follows a structured architecture, consisting of:   5
Input Layer: Accepts the input image, typically represented as a matrix of pixel values.
Page 5 of 10
--- page 6 ---
Convolutional Layers: Apply multiple filters to detect local patterns such as edges, corners,
and textures.
Activation Layers: Use non-linear functions (like Rectified Linear Unit) to introduce non-
linearity into the model.
Pooling Layers: Reduce dimensionality and computation while preserving key features.
Fully Connected Layers: Aggregate information from previous layers to perform
classification or regression tasks.
Output Layer: Uses activation functions like Softmax (for classification) or Sigmoid (for
binary tasks) to generate predictions.
Each component plays a crucial role in processing image data, from feature extraction to
decision-making.
c.   5
ResNet (Residual Network) introduced a revolutionary concept called Residual Learning,
allowing CNNs to train much deeper networks without degradation in performance.
Problem: Vanishing Gradient
In very deep networks, gradients become too small, preventing proper weight updates.
As a result, deeper networks often perform worse than shallower networks.
ResNet Solution: Residual Connections (Skip Connections)
Instead of directly learning a mapping H(x), ResNet learns the residual function F(x) = H(x)
- x, where x is the input.
These skip connections allow gradients to flow directly through the network, preventing
them from becoming too small.
Enables networks with 100+ layers, outperforming shallower architectures.
ResNet Architecture:
Uses 3×3 convolutional layers like VGG.
Introduces Residual Blocks, where input is added to the output of convolutional layers.
Available in multiple versions: ResNet-18, ResNet-34, ResNet-50, ResNet-101, and
ResNet-152, where the number indicates layers.
Page 6 of 10
--- page 7 ---
Key Benefits:
1. Enables Very Deep Networks: Unlike VGG, which struggles beyond 19 layers, ResNet
scales up to 152 layers efficiently.
2. Improves Training Efficiency: Reduces gradient-related issues, leading to faster and more
stable training.
3. Better Accuracy: Achieves higher classification accuracy in benchmark datasets like
ImageNet.
ResNet’s success has led to its adoption in modern AI applications, including object detection,
facial recognition, and medical imaging.
d. Understanding how CNNs learn features is crucial for model interpretability and debugging.   5
Visualization techniques help analyze the behavior of different layers:
Key Visualization Methods:
1. Filter Visualization: Shows what kind of features (edges, textures) a CNN detects at
different layers.
2. Activation Maps: Displays which parts of an image are most important for predictions.
3. Saliency Maps: Highlights pixels that contribute most to a decision, useful in medical
imaging and self-driving cars.
4. Grad-CAM (Gradient-weighted Class Activation Mapping): Identifies image regions
responsible for a CNN’s predictions.
5. t-SNE (t-Distributed Stochastic Neighbor Embedding): Reduces high-dimensional feature
representations to 2D or 3D for visualization.
Importance of Visualization:
Helps detect biases and errors in the model.
Improves model explainability in sensitive applications like healthcare and finance.
Aids in hyperparameter tuning by analyzing layer-wise activations.
4.   Attempt any three questions(Attempt Any 3 Questions)   15
Page 7 of 10
--- page 8 ---
5
a. Feature   Autoencoders   PCA
Nature   Non-linear transformation   Linear transformation
Learning Type   Neural network-based   Matrix factorization-based
Captures only variance-based
Feature Learning   Learns hierarchical features
features
Dimensionality   Fixed number of principal
Latent space can be customized
Reduction   components
Reconstruction   Uses loss functions (MSE,
Uses eigenvectors and variance
Loss   Cross-Entropy)
Performance drops with high-
Scalability   Works well with large datasets
dimensional data
Key Differences:
Autoencoders capture complex, non-linear relationships, making them better for deep
learning applications.
PCA is computationally faster and works well for small datasets with simple structures.
Autoencoders can be fine-tuned and adapted for different tasks, while PCA is static.
Autoencoders are preferred for deep learning tasks, whereas PCA is commonly used in
traditional machine learning applications.
b. Types of Autoencoders and Their Characteristics   5
Autoencoders have several variations, each designed to handle different tasks. The main types
are:
1.   Vanilla Autoencoder:
o Standard autoencoder with a simple encoder-decoder architecture.
o Learns compressed representations but lacks control over encoding.
2.   Denoising Autoencoder:
o Trained with noisy input but learns to reconstruct the clean version.
o Improves feature extraction and robustness.
3.   Sparse Autoencoder:
o Uses a sparsity constraint (L1 regularization) to ensure only a few neurons activate at a
time.
Page 8 of 10
--- page 9 ---
o Helps in learning disentangled features.
4.   Variational Autoencoder (VAE):
o Learns a probabilistic distribution rather than deterministic encoding.
o Used for generative modeling.
5.   Contractive Autoencoder:
o Uses Jacobian regularization to make representations invariant to small changes in input.
o Enhances robustness in data compression.
Each type has specific advantages, depending on the application, such as feature learning,
denoising, anomaly detection, and generative modeling.
5
c. Feature   RNN   LSTM   GRU
Handles Long-Term   No (vanishing   Yes (better than
Yes
Dependencies?   gradient issue)   RNN)
Complex   Less complex than
Architecture Complexity   Simple
(gates)   LSTM
Training Time   Fast   Slower   Faster than LSTM
Memory Requirement   Low   High   Moderate
Long   Faster alternatives to
Application   Basic sequence tasks
sequences   LSTM
Key Differences:
RNNs struggle with long-term dependencies due to the vanishing gradient problem.
LSTMs solve this using gates that selectively store and forget information.
GRUs are a simplified version of LSTMs, performing similarly with fewer computations.
When to Use:
RNN: Short sequences with no long-term dependency (e.g., simple time-series prediction).
LSTM: Tasks requiring long memory, such as speech recognition and chatbot training.
GRU: Faster alternative when LSTM is too computationally expensive.
LSTMs and GRUs have largely replaced RNNs in modern deep learning applications, making
sequence-based tasks more efficient.
Page 9 of 10
--- page 10 ---
d. The exploding gradient problem occurs when gradients become excessively large during   5
backpropagation through time (BPTT), leading to unstable training and divergence in weight
updates.
Why Does It Happen?
If the recurrent weights are greater than 1, repeated multiplications during backpropagation
cause exponential growth in gradients.
This results in extremely large weight updates, making the model unstable.
Effects of Exploding Gradient:
The model fails to converge and may generate random or meaningless outputs.
Training loss fluctuates wildly and does not decrease.
The network becomes highly sensitive to small variations in input, reducing generalization
ability.
Page 10 of 10
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 61fba7a1bf22

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Re-Exam/Bachelor of Science (Information Technology) - 45618/Programming Logic And Techniques/ANS_Re-Exam_Programming Logic And Techniques(NHPLT101)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 19 Jan 2026
- Text: text (12 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: B.Sc. (IT)
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Programming Logic and Techniques/Programming Logic
And Techniques
Time: 11:00 am - 01:00 pm
Date: 19 Jan 2026
(02:00 Hrs.)
Max Marks: 60
RE EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 12 pages
2. Each question carries equal marks
3. Answer to each new question to be started on a fresh page
4. Draw neat and clear diagrams wherever required
5. Students may add pseudocode or code snippet to the answer where relevant
6. For any psuedocode-based question, ensure to describe clearly
7. Figure on the right-hand side indicates full marks
Q1. Answer the following questions(Attempt Any 4 Questions)   20
a. Any 5 points, 1 Mark for each   5
Aspect   High-Level Language (HLL)   Low-Level Language (LLL)
Language close to human   Language close to machine
Definition   language with high abstraction   code with little or no
from hardware.   abstraction.
Difficult to read; uses binary or
Easy to read, write, and
Readability   mnemonics (e.g., Machine,
understand (e.g., Python, Java).
Assembly).
Programs can run on different
Programs are
Portability   machines with minimal
hardware/processor dependent.
changes.
Page 1 of 12
--- page 2 ---
Aspect   High-Level Language (HLL)   Low-Level Language (LLL)
Execution   Slower compared to low-level   Very fast execution (closer to
Speed   (needs translation).   hardware).
Control over   Limited control over hardware   Direct control of memory, CPU
Hardware   details.   registers, and hardware.
b. Explanation of Role – 4 Marks   5
Programming languages play a central role in software development as they provide the tools
to design, implement, and maintain software applications. They allow developers to translate
ideas and requirements into instructions that computers can execute. They transform ideas into
functional applications, support efficient data handling, provide reusable components, and
ensure reliable software execution.
Following is the role of programming language in software development
-   Languages help developers express the step-by-step logic needed to solve a problem
-   Languages allow creation of interactive software interfaces for users
-   Languages provide mechanisms to store, access, and manipulate data efficiently
-   Functions, libraries, and modules in programming languages allow reusable code,
reducing development time
-   Programming languages include tools to detect and handle errors, ensuring software
reliability
Example: (Any two examples – 1 Mark)
a.   Python – Data Science
b.   Java – Game Development
c. C – Operating System
d.   JavaScript – Web Development
e. SQL – Database Management
c. Explanation – 3 Marks   5
Functional programming is a programming paradigm where computation is treated as the
evaluation of mathematical functions. In this approach:
·   Programs are built using pure functions that do not have side effects (i.e., they do not alter
external states).
·   Data is immutable, meaning once created, it cannot be changed.
·   Functions are first-class citizens, which means they can be passed as arguments, returned
from other functions, or assigned to variables.
Page 2 of 12
--- page 3 ---
·   Emphasizes declarative programming, focusing on what to compute rather than how to
compute it
·   This programming paradigm promotes popularity
Example – 2 Marks
A company wants to automatically filter incoming emails into two categories: important and
others, based on whether they contain certain keywords like “urgent” or “meeting”. Functional
programming would create a function that will classify the emails based on the mapping of
certain keywords and this function shall then be called. This helps atomate email categorization
in a more predictable way, reducing manual effort.
d. Explanation – 2 Mark   5
An algorithm is a step-by-step procedure or set of instructions designed to solve a specific
problem or perform a task. It is precise, finite, and should lead to a correct solution when
followed. It helps break the complex problem into manageable steps thereby improving
efficiency and performance. Algorithms are foundations of problem-solving.
Structured Problem Solving – 3 Marks
Problem-solving can be effectively approached using the Scientific Method and George Pólya's
method as complementary frameworks
Problem Solving Using the Scientific Method
a.   Understand the Problem - Clearly define the problem you want to solve
b. Form a Hypothesis - Develop a testable hypothesis based on your understanding
c.   Plan Experiment - Design an experiment that outlines the variables, controls, and
measurement methods
d.   Execute Experiment - Conduct the experiment according to the established plan.
Problem Solving Using George Pólya's Method
a.   Understand the Problem - Understand the requirements, constraints, and objectives of the
problem
b.   Devise a Plan - Create a strategy for how to test the hypothesis and outline the steps
needed
c.   Execute the Plan - Follow the devised plan while carefully recording observations and
data
d. Review and Extend - Reflect on the results and consider how the solution can be applied
or improved
e. 4 Makrs - Decomposition Tree   5
Page 3 of 12
--- page 4 ---
1 Mark - Identification of the root node, 3 child nodes, and leaf nodes, and specify the
level of the tree
f. Given terms are : 3, 8 ,15, 24, 35, 48   5
Step 1 - Look at the first order difference - 1 Mark
8 - 3 = 5
15 - 8 = 7
24 - 15 = 9
35 - 24 = 11
48 - 3 = 13
So the differences of each term increases by the next odd term
Step 2 - Rule - 2 Marks
Since the differences of each term increase by the next odd term, the general rule of the series
is Tn = n(n + 2)
Step 3 - Checking the previous terms with the rule - 1 Mark
T1 = 1 * (1 + 2) = 1 * 3 = 3
T2 = 2 * (2 + 2) = 2 * 4 = 8
T3 = 3 * (3 + 2) = 3 * 5 = 15
Page 4 of 12
--- page 5 ---
T4 = 4 * (4 + 2) = 4 * 6 = 24
T5 = 5 * (5 + 2) = 5 * 7 = 35
T6 = 6 * (6 + 2) = 6 * 8 = 48
Step 4 - The next three predicted terms in the meter reading series will be - 1 Mark
T7 = 7 * (7 + 2) = 7 * 9 = 63
T8 = 8 * (8 + 2) = 8 * 10 = 80
T9 = 9 * (9 + 2) = 9 * 11 = 99
So the next three predicted readings are 63, 80, 99
Q2. Answer the following questions(Attempt Any 4 Questions)   20
a. Any 5 reasons, each for 1 Mark   5
Algorithms are designed to solve specific problems efficiently. However, they need to be
adaptable for the following reasons:
a.   Real-world problems often have similar structures but different input values
b.   Adaptable algorithms can be reused for multiple related problems without rewriting from
scratch
c.   By adapting an existing algorithm, developers save time instead of designing a new
solution for each similar problem
d.   Adaptable algorithms can scale to handle larger values or additional constraints without
major changes
e.   Algorithms that are adaptable allow programmers to apply them creatively to new
problems with minimal modification
f.   Adaptable algorithms are easier to maintain and update when requirements change
g.   Adaptable algorithms encourage innovation by allowing developers to experiment with
variations and extensions
b. Explanation of CTs applicability – 4 Marks   5
Example – 1 Mark
Computational thinking (CT) is a problem-solving approach that uses concepts like
decomposition, pattern recognition, abstraction, and algorithm design. It is not limited to
computers, it can be applied in everyday life:
a.   Breaking a complex task into smaller, manageable parts. For example, planning a
birthday party can be broken into tasks such as invitations, decorations, catering, and games
b.   Identifying similarities or patterns in problems to make solutions more efficient. For
example, Noticing that sending reminders three days before each event always improves
attendance
Page 5 of 12
--- page 6 ---
c.   Focusing on important information and ignoring unnecessary details. For example, While
preparing a to-do list, only prioritize tasks that must be done today, ignoring less urgent tasks
d.   Creating a step-by-step plan to solve a problem. For example, Making a shopping list in
order of store layout to minimize walking time
e.   Checking the plan’s effectiveness and improving it if needed. For example, After
organizing the party, evaluating what went well (timing, catering) to improve next time
c. Reasononing – 5 Marks   5
a.   When interest = amount - principal executes before amount is calculated, the variable
amount is undefined (or may have a previous value if reused). This results in incorrect interest
b. By definition, interest = amount – principal
c.   If amount is not yet calculated, there is no current value of amount based on the input
principal, rate, and time
d.   Calculating interest before computing amount means the formula is using a value of
amount that does not correspond to the current inputs. Therefore, interest cannot correctly
represent the actual gain
e.   For every account, interest will be wrong because it is computed using an out-of-date or
uninitialized value of amount. Only after amount is calculated will the correct interest be
obtainable, so the order of operations is critical.
d. Identification of problem – 2 Marks   5
This algorithm solves the problem of calculating income tax efficiently for multiple taxpayers
according to a tiered tax slab system, ensuring accuracy and consistency in taxation.
Explanation – 3 Marks
a.   The algorithm is designed to calculate income tax for multiple taxpayers based on a
progressive tax slab system
b.   It ensures that:
1. Low-income taxpayers (≤ 5 lakh) are not taxed.
2.   Middle-income taxpayers (5–10 lakh) pay 10% tax on the portion exceeding 5 lakh.
3.   High-income taxpayers (> 10 lakh) pay 10% on 5–10 lakh and 20% on income above 10
lakh
c.   For each taxpayer, it provides the tax amount, helping authorities or individuals in
compliance and reporting
e. Diagram with correct symbols, flow, and logic – 5 Marks   5
Start and Stop may be drawn either as a lozenge or oval
Page 6 of 12
--- page 7 ---
f. Algorithm with correct logic and written stepwise with clear conventions and instructions = 5   5
Marks
1.   Start
2.   Input n (number of students) and days (number of class days)
3.   Initialize total_present_students = 0
4.   For each student i = 1 to n:
a. Initialize present_count[i] = 0
b. For each day j = 1 to days:
o Input attendance[i][j]
o If attendance[i][j] == "Present", increment present_count[i] by 1
o If attendance[i][j] == "Present", increment total_present_students by 1
5.   For each student i = 1 to n:
o Calculate student_percentage[i] as (present_count[i] / days) * 100
o If student_percentage[i] is less than 75%, mark student i as “Low Attendance”
6.   Calculate the class_percentage as (total_present_students / (n * days)) * 100
7.   Display the student_percentage[i] for each student individually
8.   Display the class_percentage
9.   Display the list of students with attendance below 75%
10. End
Q3. Answer the following questions(Attempt Any 4 Questions)   20
a. Each generation of language 1 mark   5
Page 7 of 12
--- page 8 ---
Programming languages have evolved over time, and they are classified into five main
generations based on their level of abstraction and ease of use:
1. First Generation (1GL) – Machine Language:
This is the lowest-level language consisting of binary code (0s and 1s) directly
understood by the computer’s hardware.
Programs are difficult to write, read, and debug, but they execute very fast.
2. Second Generation (2GL) – Assembly Language:
Uses symbolic codes or mnemonics instead of binary, which makes programming
slightly easier. o Requires an assembler to translate it into machine code.
Still hardware-dependent and low-level.
3. Third Generation (3GL) – High-Level Languages:
Examples include C, Java, Python, and Fortran.
These languages are closer to human language and easier to read and write.
They are machine-independent and require a compiler or interpreter to convert into
machine code.
4. Fourth Generation (4GL):
Designed for specific tasks like database management, report generation, and data
analysis.
Examples: SQL, MATLAB, Oracle Reports.
These languages allow programmers to write less code to perform complex tasks,
improving productivity.
5. Fifth Generation (5GL):
Focuses on solving problems using constraints, logic, or AI techniques rather than
explicit algorithms.
Examples: Prolog, LISP.
These are mainly used in artificial intelligence, expert systems, and natural
language processing.
Page 8 of 12
--- page 9 ---
b. Each error 1 mark, rewriting 1 mark   5
Errors:
1. The sum is calculated as sum = sum - mark; it should be sum = sum + mark.
2. For calculating the average, Set must be used to assign a value to a average variable, makes
it more readable
3. Output prints mark instead of average.
4. PRINT is used instead of DISPLAY/OUTPUT
SET sum = 0
FOR i = 1 TO 5
DISPLAY "Enter mark:"
INPUT mark
SET sum = sum +mark
END FOR
SET average = sum / 5
DISPLAY "The average mark is: " + average
c. Variant A – CASE   5
Logic: Uses a CASE (or SELECT CASE) structure to evaluate the marks and select the
corresponding grade.
Advantages:
Clear and readable for multiple discrete conditions.
Easier to maintain if new grade ranges are added.
Reduces deep nesting, making the code less error-prone.
Disadvantages:
Some languages may not support CASE with range-based conditions, requiring explicit
handling.
Variant B – Nested IF
Logic: Uses multiple IF-ELSE statements nested to check each grade range.
Page 9 of 12
--- page 10 ---
Advantages:
Flexible for complex or overlapping conditions.
Supported in all programming languages.
Disadvantages:
Can become hard to read with many nested conditions.
More prone to logical errors due to deep nesting.
Comparison / Which is better?
CASE (Variant A) is generally better for grading because:
It is more readable and maintainable.
Reduces the risk of mistakes compared to deeply nested IFs.
Nested IF (Variant B) is useful if the language does not support CASE or if conditions are
complex and not easily expressed as discrete cases.
d.   5
For each iteration 1 mark
i   Input x Condition (x > 0) Action on sum sum after update
1   -5   False   sum unchanged   0
2 7   True   sum = sum + 7   0 + 7 = 7
3   -3   False   sum unchanged   7
4 10   True   sum = sum + 10 7 + 10 = 17
5 1   True   sum = sum + 1   17 + 1 = 18
e. MODULE ConvertToFahrenheit (REAL Celsius)   5
DECLARE REAL Fahrenheit
SET Fahrenheit = (Celsius * 9 / 5) + 32
RETURN Fahrenheit
END MODULE
Page 10 of 12
--- page 11 ---
// Main Program
MODULE main( )
DECLARE REAL Celsius, Fahrenheit
DISPLAY "Enter temperature in Celsius:"
INPUT Celsius
SET Fahrenheit = ConvertToFahrenheit(Celsius)
DISPLAY "Temperature in Fahrenheit is: " + Fahrenheit
END MODULE
If function is used then the pseudocode would be
FUNCTION REAL ConvertToFahrenheit(REAL Celsius)
SET Fahrenheit = (Celsius * 9 / 5) + 32
RETURN Fahrenheit
END MODULE
// Main Program
MODULE main( )
DECLARE REAL Celsius, Fahrenheit
DISPLAY "Enter temperature in Celsius:"
INPUT Celsius
SET Fahrenheit = ConvertToFahrenheit(Celsius)
DISPLAY "Temperature in Fahrenheit is: " + Fahrenheit
END MODULE
f. DECLARE Integer num, largestEven   5
SET largestEven = -9999   // Initialize to very small number
FOR i = 1 TO 8
DISPLAY "Enter number "+ i + ":"
INPUT num
IF num MOD 2 == 0 THEN   // Check if the number is even
IF num > largestEven THEN
Page 11 of 12
--- page 12 ---
SET largestEven = num
END IF
END IF
END FOR
IF largestEven == -9999 THEN
DISPLAY "No even numbers were entered."
ELSE
DISPLAY "The largest even number is: "+ largestEven
END IF
Page 12 of 12
````
