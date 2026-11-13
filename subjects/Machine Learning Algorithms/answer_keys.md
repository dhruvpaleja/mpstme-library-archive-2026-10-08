# Machine Learning Algorithms: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 22cd717b00da

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Machine Learning Algorithms/ANS_Machine Learning Algorithms(702IT0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: mixed (11 pages), mean OCR confidence 86.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Machine Learning Algorithms
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Justify the statement: “Supervised learning requires labeled data, whereas
unsupervised learning does not.”
1. Supervised learning is a type of machine learning in which the model
is trained using labeled data, where each input has a corresponding
known output (target).
2. The objective of supervised learning is to learn a mapping between
input variables and output labels to make predictions on new data.
CO-1 ;
3. Examples of supervised learning algorithms include Linear Regression,
SO- 2;   5
Logistic Regression, Decision Trees, and Support Vector Machines.
BL-5
4. Unsupervised learning is a type of machine learning in which the model
is trained using unlabeled data, where no target output is provided.
5. The objective of unsupervised learning is to discover hidden patterns,
structures, or groupings within the data.
6. Examples of unsupervised learning algorithms include K-means
clustering, Hierarchical clustering, and Principal Component Analysis
(PCA).
********** 1 **********
--- page 2 ---
7. Therefore, supervised learning requires labeled data to guide the
learning process, whereas unsupervised learning operates without
labeled data and relies on the inherent structure of the data.
b.   Explain the concept of maximum margin in Support Vector Machines. Why is
maximizing the margin important?
CO3- ;   1. Definition of margin in SVM — 3 marks
SO-2;   2. Concept of maximum margin / optimal hyperplane — 3 marks   5
BL-2   3. Importance of maximizing margin (generalization / robustness) — 2
marks
4. Overall justification / conclusion — 2 marks
c. Why are Regression Trees considered non-linear models? Explain your answer
briefly.
CO-3 ;
1. Definition of Regression Trees — 3 marks
SO-2 ;   5
2. Explanation of piecewise prediction / splitting mechanism — 3 marks
BL-2
3. Reason why they model nonlinear relationships — 2 marks
4. Brief conclusion / justification — 2 marks
d. When is validation necessary in a machine learning model? Explain the concept
CO-2 ;   of cross-validation with one technique.
SO-2 ;   Requirement of validating a machine learning model: 1 mark   5
Method of validation: 1 mark
BL-2
Cross-validation: 1 mark
Technique of cross-validation: 2 marks
********** 2 **********
--- page 3 ---
Q2   a.   Consider the following dataset for predicting whether a person will Play
CO-3;   Tennis based on Outlook, Temperature, and Humidity. Using the Naive
SO-2;   Bayes classifier, classify the instance:   [10]
BL-3   (Outlook=Sunny, Temperature=Cool, Humidity=High)
Temperatur
No.   Outlook   Humidity   Play
e
1   Sunny   Hot   High   No
2   Sunny   Hot   High   No
3   Overcast   Hot   High   Yes
4   Rain   Mild   High   Yes
5   Rain   Cool   Normal   Yes
6   Rain   Cool   Normal   No
7   Overcast   Cool   Normal   Yes
8   Sunny   Mild   High   No
9   Sunny   Cool   Normal   Yes
10   Rain   Mild   Normal   Yes
********** 3 **********

[Text in pictures on this page, read by OCR]
Step 1: Prior Probabilities

Total observations:
n=10

Yes:

No:

6
P(Yes) = 107 0.6

4
P(No) = 7, =0.4
--- page 4 ---
Step 2: Conditional Probabilities

For Play = Yes
Total Yes = 6

Outlook = Sunny

1
1
P(Sunny| Yes) = 6

Temperature = Cool

3
3
P(Cool|Yes) = 67 0.5

Humidity = High

2

. 2
P(High|Yes) = $7 0.333

For Play = No
Total No = 4

Outlook = Sunny

3
3
P(Sunny|No) = i= 0.75
Temperature = Cool
1
1
P(Cool|No) = i” 0.25
Humidity = High
3

P(High|No) = : = 0.75

FIC 7) IC HOH
--- page 5 ---
CO-3;   b.   Discuss Bagging, Random Forest, and Boosting as ensemble techniques,   [10]
SO-2;   highlighting their working principles and key differences.
BL-2   1. Working principle of Bagging – 2 Marks
2. Working of Random Forest – 3 Marks
3. Working of Boosting – 3 Marks
4. Key differences among Bagging, Random Forest, and Boosting – 2
Marks
Q3   a.   The following dataset contains two variables X and Y. Apply Principal   [10]
CO-2;   Component Analysis (PCA) to compute the mean of each variable, form the
SO-2;   covariance matrix, determine the eigenvalues and eigenvectors, and identify
BL-3   the first principal component.
X   1   3   5   7
Y   2   4   6   8
********** 5 **********

[Text in pictures on this page, read by OCR]
Step 3: Posterior Probabilities

For Yes
P(Yes|X) x P(Yes) x P(Sunny|Yes) x P(Cool/Yes) x P(High|Yes)
= 0.6 x ; x 0.5 x 0.333
= 0.0167
For No

P(No|X) x 0.4 x 0.75 x 0.25 x 0.75

= 0.0563

Step 4: Final Classification

Compare:
P(Yes|X) = 0.0167
P(No|X) = 0.0563
Since:

0.0563 > 0.0167

Final Answer

Predicted class = No
--- page 6 ---
Solution
Step 1: Mean of each variable (1 marks)
Mean of X = (1 + 3 + 5 + 7) / 4 = 4.00
Mean of Y = (2 + 4 + 6 + 8) / 4 = 5.00
Mean vector = (4.00, 5.00)
Step 2: Center the data (2 marks)
on   X - mean   Y - mean
-3.00   -3.00
-1.00   -1.00
1.00   1.00
3.00   3.00
Step 3: Covariance matrix (2 marks)
Cov(X,X) = 6.6667
Cov(Y,Y) = 6.6667
Cov(X,Y) = 6.6667
Covariance matrix = [[6.6667, 6.6667], [6.6667, 6.6667]]
Step 4: Eigenvalues and eigenvectors (4 marks)
Eigenvalue λ1 = 13.3333
Eigenvalue λ2 = 0.0000
Eigenvector for λ1 = (0.7071, 0.7071)
Eigenvector for λ2 = (-0.7071, 0.7071)
Step 5: First principal component (1 marks)
The first principal component is the eigenvector corresponding to the largest
eigenvalue, so PC1 = (0.7071, 0.7071).
Final Answer
Mean vector   (4.00, 5.00)
[[6.6667, 6.6667], [6.6667,
Covariance matrix
6.6667]]
Eigenvalues   13.3333, 0.0000
PC1 direction   (0.7071, 0.7071)
********** 6 **********
--- page 7 ---
PC1 captures the maximum
Interpretation
variance (100.00%).
b.   Discuss the formulation of Multiple Linear Regression, including model   [10]
representation, assumptions, and interpretation of coefficients.
CO-2;
1. Model representation and formulation of Multiple Linear Regression –
SO-2;
3 Marks
BL-2
2. Assumptions of Multiple Linear Regression – 4 Marks
3. Interpretation of regression coefficients – 3 Marks
Q4   a.   Explain the fundamental concept of Logistic Regression. How does it   [10]
CO-3;   approach the task of classification? What is the importance of the sigmoid
SO-2;   function and loss function?
BL-2   1. Fundamental concept of Logistic Regression – 3 Marks
2. Approach to classification – 3 Marks
3. Role of sigmoid function – 2 Marks
4. Importance of loss function – 2 Marks
CO-3;   b.   Consider the multi-layer perceptron network consisting of two input neurons,
SO-2;   [10]
1   1
BL-3
0.25   0.3
X1   0.15   Z1   0.4   Y1
0.2   0.3   0.6   0.5
X2   0.4   Z2   0.45   Y2
0.1
0.35
1   1
two hidden neurons, and two output neurons as given in the figure. Consider
the input as (X1, X2) = (0, 1). Compute the outputs Y1 and Y2 for the forward
pass, considering the sigmoid activation function. Also, compute the error for
the output vector (1, 0).
To calculate the output of the network, we need to calculate the activation of
hidden neurons: (4 Marks)
********** 7 **********
--- page 8 ---
𝑧𝑖𝑛1 = 𝑥1 ∗𝑣11 + 𝑥2 ∗𝑣21 + 𝑣01 = 0 ∗0.15 + 1 ∗0.3 + 0.25 = 0.55
𝑧𝑖𝑛2 = 𝑥1 ∗𝑣12 + 𝑥2 ∗𝑣22 + 𝑣02 = 0 ∗0.2 + 1 ∗0.4 + 0.35 = 0.75
1   1   1
𝑧1 =   =   =   = 0.6342
1 + 𝑒−𝑧𝑖𝑛1 1 + 𝑒−0.55 1 + 0.5769
1   1   1
𝑧2 =   =   =   = 0.6792
1 + 𝑒−𝑧𝑖𝑛2 1 + 𝑒−0.75 1 + 0.4724
Calculate the activations of the output neuron: (4 marks)
𝑦𝑖𝑛1 = 𝑧1 ∗𝑤11 + 𝑧2 ∗𝑤21 + 𝑤01 = 0.6342 ∗0.4 + 0.6792 ∗0.6 + 0.3
= 0.9612
𝑦𝑖𝑛2 = 𝑧1 ∗𝑤12 + 𝑧2 ∗𝑤22 + 𝑤02 = 0.6342 ∗0.5 + 0.6792 ∗0.45 + 0.1
= 0.7227
1   1   1
𝑦1 =   =   =   = 0.7234
1 + 𝑒−𝑦𝑖𝑛1 1 + 𝑒−0.9612 1 + 0.3824
1   1   1
𝑦2 =   =   =   = 0.6732
1 + 𝑒−𝑦𝑖𝑛2 1 + 𝑒−0.7227 1 + 0.4854
Error calculation: (2 marks)
Expected output (1,0)
Output from network (0.7234, 0.6732)
Error at y1=(t1-y1)=(1-0.7234)=0.2766
Error at y2=(t2-y2)=(0-0.6732)=-0.6732
Q5   a.   Consider the following dataset. Construct a full decision tree using the Gini
CO-3;   Index as the attribute selection measure. Show all calculations.   [10]
SO-2;   Study Hours   Attendance   Result
BL-3
High   Good   Pass
High   Good   Pass
High   Good   Pass
High   Poor   Fail
High   Poor   Fail
Low   Good   Fail
Low   Good   Fail
Low   Good   Fail
Low   Poor   Pass
Low   Poor   Pass
Solution
Step 1: Count the class values (2 marks)
Pass = 5, Fail = 5
Gini(D) = 1 - (5/10)^2 - (5/10)^2 = 1 - 0.25 - 0.25 = 0.50
********** 8 **********
--- page 9 ---
Step 2: Gini for attribute Study Hours (3 marks)
High: 3 Pass, 2 Fail
Gini(High) = 1 - (3/5)^2 - (2/5)^2 = 1 - 9/25 - 4/25 = 12/25 = 0.48
Low: 2 Pass, 3 Fail
Gini(Low) = 1 - (2/5)^2 - (3/5)^2 = 1 - 4/25 - 9/25 = 12/25 = 0.48
Weighted Gini(Study Hours) = (5/10)(0.48) + (5/10)(0.48) = 0.48
Step 3: Gini for attribute Attendance (3 marks)
Good: 3 Pass, 3 Fail
Gini(Good) = 1 - (3/6)^2 - (3/6)^2 = 1 - 0.25 - 0.25 = 0.50
Poor: 2 Pass, 2 Fail
Gini(Poor) = 1 - (2/4)^2 - (2/4)^2 = 1 - 0.25 - 0.25 = 0.50
Weighted Gini(Attendance) = (6/10)(0.50) + (4/10)(0.50) = 0.50
Root node decision: Choose Study Hours because it has the lower Gini value
(0.48) compared with Attendance (0.50).
Step 4: Split each branch further using Attendance (2 marks)
For Study Hours = High: using Attendance gives
- Good -> Pass, Pass, Pass -> pure leaf: Pass
- Poor -> Fail, Fail -> pure leaf: Fail
For Study Hours = Low: using Attendance gives
- Good -> Fail, Fail, Fail -> pure leaf: Fail
- Poor -> Pass, Pass -> pure leaf: Pass
Final Decision Tree
Study Hours
├── High -> Attendance
│ ├── Good -> Pass
│ └── Poor -> Fail
└── Low -> Attendance
├── Good -> Fail
└── Poor -> Pass
Final answer: The complete decision tree is created with Study Hours as the
root node and Attendance as the second splitting attribute. All terminal nodes
are pure.
b.   Discuss how Lasso regression can be used for feature selection. Why is Ridge
regression less suitable for this purpose?   [10]
CO-2;
1. Concept of Lasso regression and feature selection mechanism – 5
SO-2;
Marks
BL-2
2. Limitations of Ridge regression for feature selection – 3 Marks
3. Reasoning based on penalty functions (L1 vs L2) – 2 Marks
Q6   a.   Describe the concept of soft margin SVM. How does the regularization
parameter (C) affect the decision boundary?   [10]
********** 9 **********
--- page 10 ---
CO-3;   1. Concept of soft margin SVM – 4 Marks
SO-2;   2. Role of slack variables and margin flexibility – 2 Marks
BL-2   3. Effect of regularization parameter (C) on decision boundary – 4
Marks
CO-2;   b.   Explain the concept of a confusion matrix? How is it used to evaluate
SO-2;   classification algorithms? Define the terms Accuracy, Precision, Recall, and [10]
BL-2   F1-score from the confusion matrix.
From the confusion matrix given below, calculate accuracy, precision, recall,
and f1-score.
Actual
Positive   Negative
Positive   560   60
Prediction
Negative   70   330
Confusion Matrix=2 marks
Actual
Positive   Negativ
e
Positive   560   60
Prediction   Negativ   70   330
e
TP=560, TN=330, FP=60, FN=70
Each parameter definition and calculation (2 Marks)
𝑇𝑃+ 𝑇𝑁
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=
𝑇𝑃+ 𝑇𝑁+ 𝐹𝑃+ 𝐹𝑁
560 + 330   890
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=   =   = 0.87
560 + 330 + 60 + 70 1020
𝑇𝑃
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=
𝑇𝑃+ 𝐹𝑃
560
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=   = 0.90
560 + 60
𝑇𝑃
𝑅𝑒𝑐𝑎𝑙𝑙=
𝑇𝑃+ 𝐹𝑁
560
𝑅𝑒𝑐𝑎𝑙𝑙=   = 0.88
560 + 70
2 ∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑟𝑒𝑐𝑎𝑙𝑙
𝑓1 −𝑠𝑐𝑜𝑟𝑒=
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+ 𝑟𝑒𝑐𝑎𝑙𝑙
2 ∗0.90 ∗0.88
𝑓1 −𝑠𝑐𝑜𝑟𝑒=   = 0.89
0.90 + 0.88
Q7   a.   Explain the working of a convolutional neural network. What are the different
CO-3;   layers present in CNN? Also, explain the role of padding and stride with a [10]
SO-2;   suitable example.
BL-2   Basic Structure of CNN: 3 Marks
Layers of CNN: 3 marks
********** 10 **********
--- page 11 ---
1. Convolutional layer
2. Pooling Layer
3. Fully Connected Layer
4. Classification Layer
Concept of padding and stride with example (4 Marks)
b. Apply the DBSCAN algorithm to the given data points and create the clusters
with minPts=3 and epsilon (Ɛ=2.1).   [10]
Data Points: P1: (3, 7), P2: (4,6), P3: (5,5), P4: (6, 4), P5: (7,3), P6: (6,2)
Use Euclidean distance and calculate the distance between each point
𝐷𝑒(𝑝(𝑥1,𝑦1), 𝑞(𝑥2,𝑦2)) = √(𝑥2 −𝑥1)2 + (𝑦2 −𝑦1)2
P1 (3, 7)   P2 (4, 6)   P3 (5, 5)   P4 (6,4)   P5 (7,3)   P6
P1 (3, 7)   0   1.41   2.83   4.24   5.65
P2 (4, 6)   1.41   0   1.41   2.83   4.24
CO-3;   P3 (5, 5)   2.83   1.41   0   1.41   2.83
P4 (6,4)   4.24   2.83   1.41   0   1.41
SO-2;   P5 (7,3)   5.65   4.24   2.83   1.41   0
BL-2   P6 (6,2)   5.83   4.47   3.16   2   1.41
MinPts=3, epsilon (Ɛ)=2.1
P1: P2
P2: P1, P3
P3: P2, P4
P4: P3, P5, P6
P5: P4, P6
P6: P4, P5
Points   Status
P1 (3, 7)   Noise   Border
P2 (4, 6)   Core
P3 (5, 5)   Core
P4 (6,4)   Core
P5 (7,3)   Core
P6 (6,2)   Core
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper cfb859e04a12

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Machine Learning Algorithms/ANS_Machine Learning Algorithms(702IT0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: mixed (11 pages), mean OCR confidence 86.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Machine Learning Algorithms
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Justify the statement: “Supervised learning requires labeled data, whereas
unsupervised learning does not.”
1. Supervised learning is a type of machine learning in which the model
is trained using labeled data, where each input has a corresponding
known output (target).
2. The objective of supervised learning is to learn a mapping between
input variables and output labels to make predictions on new data.
CO-1 ;
3. Examples of supervised learning algorithms include Linear Regression,
SO- 2;   5
Logistic Regression, Decision Trees, and Support Vector Machines.
BL-5
4. Unsupervised learning is a type of machine learning in which the model
is trained using unlabeled data, where no target output is provided.
5. The objective of unsupervised learning is to discover hidden patterns,
structures, or groupings within the data.
6. Examples of unsupervised learning algorithms include K-means
clustering, Hierarchical clustering, and Principal Component Analysis
(PCA).
********** 1 **********
--- page 2 ---
7. Therefore, supervised learning requires labeled data to guide the
learning process, whereas unsupervised learning operates without
labeled data and relies on the inherent structure of the data.
b.   Explain the concept of maximum margin in Support Vector Machines. Why is
maximizing the margin important?
CO3- ;   1. Definition of margin in SVM — 3 marks
SO-2;   2. Concept of maximum margin / optimal hyperplane — 3 marks   5
BL-2   3. Importance of maximizing margin (generalization / robustness) — 2
marks
4. Overall justification / conclusion — 2 marks
c. Why are Regression Trees considered non-linear models? Explain your answer
briefly.
CO-3 ;
1. Definition of Regression Trees — 3 marks
SO-2 ;   5
2. Explanation of piecewise prediction / splitting mechanism — 3 marks
BL-2
3. Reason why they model nonlinear relationships — 2 marks
4. Brief conclusion / justification — 2 marks
d. When is validation necessary in a machine learning model? Explain the concept
CO-2 ;   of cross-validation with one technique.
SO-2 ;   Requirement of validating a machine learning model: 1 mark   5
Method of validation: 1 mark
BL-2
Cross-validation: 1 mark
Technique of cross-validation: 2 marks
********** 2 **********
--- page 3 ---
Q2   a.   Consider the following dataset for predicting whether a person will Play
CO-3;   Tennis based on Outlook, Temperature, and Humidity. Using the Naive
SO-2;   Bayes classifier, classify the instance:   [10]
BL-3   (Outlook=Sunny, Temperature=Cool, Humidity=High)
Temperatur
No.   Outlook   Humidity   Play
e
1   Sunny   Hot   High   No
2   Sunny   Hot   High   No
3   Overcast   Hot   High   Yes
4   Rain   Mild   High   Yes
5   Rain   Cool   Normal   Yes
6   Rain   Cool   Normal   No
7   Overcast   Cool   Normal   Yes
8   Sunny   Mild   High   No
9   Sunny   Cool   Normal   Yes
10   Rain   Mild   Normal   Yes
********** 3 **********

[Text in pictures on this page, read by OCR]
Step 1: Prior Probabilities

Total observations:
n=10

Yes:

No:

6
P(Yes) = 107 0.6

4
P(No) = 7, =0.4
--- page 4 ---
Step 2: Conditional Probabilities

For Play = Yes
Total Yes = 6

Outlook = Sunny

1
1
P(Sunny| Yes) = 6

Temperature = Cool

3
3
P(Cool|Yes) = 67 0.5

Humidity = High

2

. 2
P(High|Yes) = $7 0.333

For Play = No
Total No = 4

Outlook = Sunny

3
3
P(Sunny|No) = i= 0.75
Temperature = Cool
1
1
P(Cool|No) = i” 0.25
Humidity = High
3

P(High|No) = : = 0.75

FIC 7) IC HOH
--- page 5 ---
CO-3;   b.   Discuss Bagging, Random Forest, and Boosting as ensemble techniques,   [10]
SO-2;   highlighting their working principles and key differences.
BL-2   1. Working principle of Bagging – 2 Marks
2. Working of Random Forest – 3 Marks
3. Working of Boosting – 3 Marks
4. Key differences among Bagging, Random Forest, and Boosting – 2
Marks
Q3   a.   The following dataset contains two variables X and Y. Apply Principal   [10]
CO-2;   Component Analysis (PCA) to compute the mean of each variable, form the
SO-2;   covariance matrix, determine the eigenvalues and eigenvectors, and identify
BL-3   the first principal component.
X   1   3   5   7
Y   2   4   6   8
********** 5 **********

[Text in pictures on this page, read by OCR]
Step 3: Posterior Probabilities

For Yes
P(Yes|X) x P(Yes) x P(Sunny|Yes) x P(Cool/Yes) x P(High|Yes)
= 0.6 x ; x 0.5 x 0.333
= 0.0167
For No

P(No|X) x 0.4 x 0.75 x 0.25 x 0.75

= 0.0563

Step 4: Final Classification

Compare:
P(Yes|X) = 0.0167
P(No|X) = 0.0563
Since:

0.0563 > 0.0167

Final Answer

Predicted class = No
--- page 6 ---
Solution
Step 1: Mean of each variable (1 marks)
Mean of X = (1 + 3 + 5 + 7) / 4 = 4.00
Mean of Y = (2 + 4 + 6 + 8) / 4 = 5.00
Mean vector = (4.00, 5.00)
Step 2: Center the data (2 marks)
on   X - mean   Y - mean
-3.00   -3.00
-1.00   -1.00
1.00   1.00
3.00   3.00
Step 3: Covariance matrix (2 marks)
Cov(X,X) = 6.6667
Cov(Y,Y) = 6.6667
Cov(X,Y) = 6.6667
Covariance matrix = [[6.6667, 6.6667], [6.6667, 6.6667]]
Step 4: Eigenvalues and eigenvectors (4 marks)
Eigenvalue λ1 = 13.3333
Eigenvalue λ2 = 0.0000
Eigenvector for λ1 = (0.7071, 0.7071)
Eigenvector for λ2 = (-0.7071, 0.7071)
Step 5: First principal component (1 marks)
The first principal component is the eigenvector corresponding to the largest
eigenvalue, so PC1 = (0.7071, 0.7071).
Final Answer
Mean vector   (4.00, 5.00)
[[6.6667, 6.6667], [6.6667,
Covariance matrix
6.6667]]
Eigenvalues   13.3333, 0.0000
PC1 direction   (0.7071, 0.7071)
********** 6 **********
--- page 7 ---
PC1 captures the maximum
Interpretation
variance (100.00%).
b.   Discuss the formulation of Multiple Linear Regression, including model   [10]
representation, assumptions, and interpretation of coefficients.
CO-2;
1. Model representation and formulation of Multiple Linear Regression –
SO-2;
3 Marks
BL-2
2. Assumptions of Multiple Linear Regression – 4 Marks
3. Interpretation of regression coefficients – 3 Marks
Q4   a.   Explain the fundamental concept of Logistic Regression. How does it   [10]
CO-3;   approach the task of classification? What is the importance of the sigmoid
SO-2;   function and loss function?
BL-2   1. Fundamental concept of Logistic Regression – 3 Marks
2. Approach to classification – 3 Marks
3. Role of sigmoid function – 2 Marks
4. Importance of loss function – 2 Marks
CO-3;   b.   Consider the multi-layer perceptron network consisting of two input neurons,
SO-2;   [10]
1   1
BL-3
0.25   0.3
X1   0.15   Z1   0.4   Y1
0.2   0.3   0.6   0.5
X2   0.4   Z2   0.45   Y2
0.1
0.35
1   1
two hidden neurons, and two output neurons as given in the figure. Consider
the input as (X1, X2) = (0, 1). Compute the outputs Y1 and Y2 for the forward
pass, considering the sigmoid activation function. Also, compute the error for
the output vector (1, 0).
To calculate the output of the network, we need to calculate the activation of
hidden neurons: (4 Marks)
********** 7 **********
--- page 8 ---
𝑧𝑖𝑛1 = 𝑥1 ∗𝑣11 + 𝑥2 ∗𝑣21 + 𝑣01 = 0 ∗0.15 + 1 ∗0.3 + 0.25 = 0.55
𝑧𝑖𝑛2 = 𝑥1 ∗𝑣12 + 𝑥2 ∗𝑣22 + 𝑣02 = 0 ∗0.2 + 1 ∗0.4 + 0.35 = 0.75
1   1   1
𝑧1 =   =   =   = 0.6342
1 + 𝑒−𝑧𝑖𝑛1 1 + 𝑒−0.55 1 + 0.5769
1   1   1
𝑧2 =   =   =   = 0.6792
1 + 𝑒−𝑧𝑖𝑛2 1 + 𝑒−0.75 1 + 0.4724
Calculate the activations of the output neuron: (4 marks)
𝑦𝑖𝑛1 = 𝑧1 ∗𝑤11 + 𝑧2 ∗𝑤21 + 𝑤01 = 0.6342 ∗0.4 + 0.6792 ∗0.6 + 0.3
= 0.9612
𝑦𝑖𝑛2 = 𝑧1 ∗𝑤12 + 𝑧2 ∗𝑤22 + 𝑤02 = 0.6342 ∗0.5 + 0.6792 ∗0.45 + 0.1
= 0.7227
1   1   1
𝑦1 =   =   =   = 0.7234
1 + 𝑒−𝑦𝑖𝑛1 1 + 𝑒−0.9612 1 + 0.3824
1   1   1
𝑦2 =   =   =   = 0.6732
1 + 𝑒−𝑦𝑖𝑛2 1 + 𝑒−0.7227 1 + 0.4854
Error calculation: (2 marks)
Expected output (1,0)
Output from network (0.7234, 0.6732)
Error at y1=(t1-y1)=(1-0.7234)=0.2766
Error at y2=(t2-y2)=(0-0.6732)=-0.6732
Q5   a.   Consider the following dataset. Construct a full decision tree using the Gini
CO-3;   Index as the attribute selection measure. Show all calculations.   [10]
SO-2;   Study Hours   Attendance   Result
BL-3
High   Good   Pass
High   Good   Pass
High   Good   Pass
High   Poor   Fail
High   Poor   Fail
Low   Good   Fail
Low   Good   Fail
Low   Good   Fail
Low   Poor   Pass
Low   Poor   Pass
Solution
Step 1: Count the class values (2 marks)
Pass = 5, Fail = 5
Gini(D) = 1 - (5/10)^2 - (5/10)^2 = 1 - 0.25 - 0.25 = 0.50
********** 8 **********
--- page 9 ---
Step 2: Gini for attribute Study Hours (3 marks)
High: 3 Pass, 2 Fail
Gini(High) = 1 - (3/5)^2 - (2/5)^2 = 1 - 9/25 - 4/25 = 12/25 = 0.48
Low: 2 Pass, 3 Fail
Gini(Low) = 1 - (2/5)^2 - (3/5)^2 = 1 - 4/25 - 9/25 = 12/25 = 0.48
Weighted Gini(Study Hours) = (5/10)(0.48) + (5/10)(0.48) = 0.48
Step 3: Gini for attribute Attendance (3 marks)
Good: 3 Pass, 3 Fail
Gini(Good) = 1 - (3/6)^2 - (3/6)^2 = 1 - 0.25 - 0.25 = 0.50
Poor: 2 Pass, 2 Fail
Gini(Poor) = 1 - (2/4)^2 - (2/4)^2 = 1 - 0.25 - 0.25 = 0.50
Weighted Gini(Attendance) = (6/10)(0.50) + (4/10)(0.50) = 0.50
Root node decision: Choose Study Hours because it has the lower Gini value
(0.48) compared with Attendance (0.50).
Step 4: Split each branch further using Attendance (2 marks)
For Study Hours = High: using Attendance gives
- Good -> Pass, Pass, Pass -> pure leaf: Pass
- Poor -> Fail, Fail -> pure leaf: Fail
For Study Hours = Low: using Attendance gives
- Good -> Fail, Fail, Fail -> pure leaf: Fail
- Poor -> Pass, Pass -> pure leaf: Pass
Final Decision Tree
Study Hours
├── High -> Attendance
│ ├── Good -> Pass
│ └── Poor -> Fail
└── Low -> Attendance
├── Good -> Fail
└── Poor -> Pass
Final answer: The complete decision tree is created with Study Hours as the
root node and Attendance as the second splitting attribute. All terminal nodes
are pure.
b.   Discuss how Lasso regression can be used for feature selection. Why is Ridge
regression less suitable for this purpose?   [10]
CO-2;
1. Concept of Lasso regression and feature selection mechanism – 5
SO-2;
Marks
BL-2
2. Limitations of Ridge regression for feature selection – 3 Marks
3. Reasoning based on penalty functions (L1 vs L2) – 2 Marks
Q6   a.   Describe the concept of soft margin SVM. How does the regularization
parameter (C) affect the decision boundary?   [10]
********** 9 **********
--- page 10 ---
CO-3;   1. Concept of soft margin SVM – 4 Marks
SO-2;   2. Role of slack variables and margin flexibility – 2 Marks
BL-2   3. Effect of regularization parameter (C) on decision boundary – 4
Marks
CO-2;   b.   Explain the concept of a confusion matrix? How is it used to evaluate
SO-2;   classification algorithms? Define the terms Accuracy, Precision, Recall, and [10]
BL-2   F1-score from the confusion matrix.
From the confusion matrix given below, calculate accuracy, precision, recall,
and f1-score.
Actual
Positive   Negative
Positive   560   60
Prediction
Negative   70   330
Confusion Matrix=2 marks
Actual
Positive   Negativ
e
Positive   560   60
Prediction   Negativ   70   330
e
TP=560, TN=330, FP=60, FN=70
Each parameter definition and calculation (2 Marks)
𝑇𝑃+ 𝑇𝑁
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=
𝑇𝑃+ 𝑇𝑁+ 𝐹𝑃+ 𝐹𝑁
560 + 330   890
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=   =   = 0.87
560 + 330 + 60 + 70 1020
𝑇𝑃
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=
𝑇𝑃+ 𝐹𝑃
560
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=   = 0.90
560 + 60
𝑇𝑃
𝑅𝑒𝑐𝑎𝑙𝑙=
𝑇𝑃+ 𝐹𝑁
560
𝑅𝑒𝑐𝑎𝑙𝑙=   = 0.88
560 + 70
2 ∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑟𝑒𝑐𝑎𝑙𝑙
𝑓1 −𝑠𝑐𝑜𝑟𝑒=
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+ 𝑟𝑒𝑐𝑎𝑙𝑙
2 ∗0.90 ∗0.88
𝑓1 −𝑠𝑐𝑜𝑟𝑒=   = 0.89
0.90 + 0.88
Q7   a.   Explain the working of a convolutional neural network. What are the different
CO-3;   layers present in CNN? Also, explain the role of padding and stride with a [10]
SO-2;   suitable example.
BL-2   Basic Structure of CNN: 3 Marks
Layers of CNN: 3 marks
********** 10 **********
--- page 11 ---
1. Convolutional layer
2. Pooling Layer
3. Fully Connected Layer
4. Classification Layer
Concept of padding and stride with example (4 Marks)
b. Apply the DBSCAN algorithm to the given data points and create the clusters
with minPts=3 and epsilon (Ɛ=2.1).   [10]
Data Points: P1: (3, 7), P2: (4,6), P3: (5,5), P4: (6, 4), P5: (7,3), P6: (6,2)
Use Euclidean distance and calculate the distance between each point
𝐷𝑒(𝑝(𝑥1,𝑦1), 𝑞(𝑥2,𝑦2)) = √(𝑥2 −𝑥1)2 + (𝑦2 −𝑦1)2
P1 (3, 7)   P2 (4, 6)   P3 (5, 5)   P4 (6,4)   P5 (7,3)   P6
P1 (3, 7)   0   1.41   2.83   4.24   5.65
P2 (4, 6)   1.41   0   1.41   2.83   4.24
CO-3;   P3 (5, 5)   2.83   1.41   0   1.41   2.83
P4 (6,4)   4.24   2.83   1.41   0   1.41
SO-2;   P5 (7,3)   5.65   4.24   2.83   1.41   0
BL-2   P6 (6,2)   5.83   4.47   3.16   2   1.41
MinPts=3, epsilon (Ɛ)=2.1
P1: P2
P2: P1, P3
P3: P2, P4
P4: P3, P5, P6
P5: P4, P6
P6: P4, P5
Points   Status
P1 (3, 7)   Noise   Border
P2 (4, 6)   Core
P3 (5, 5)   Core
P4 (6,4)   Core
P5 (7,3)   Core
P6 (6,2)   Core
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 8dbd1b96149d

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Machine Learning Algorithms/ANS_Machine Learning Algorithms(702IT0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: mixed (11 pages), mean OCR confidence 86.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Machine Learning Algorithms
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Justify the statement: “Supervised learning requires labeled data, whereas
unsupervised learning does not.”
1. Supervised learning is a type of machine learning in which the model
is trained using labeled data, where each input has a corresponding
known output (target).
2. The objective of supervised learning is to learn a mapping between
input variables and output labels to make predictions on new data.
CO-1 ;
3. Examples of supervised learning algorithms include Linear Regression,
SO- 2;   5
Logistic Regression, Decision Trees, and Support Vector Machines.
BL-5
4. Unsupervised learning is a type of machine learning in which the model
is trained using unlabeled data, where no target output is provided.
5. The objective of unsupervised learning is to discover hidden patterns,
structures, or groupings within the data.
6. Examples of unsupervised learning algorithms include K-means
clustering, Hierarchical clustering, and Principal Component Analysis
(PCA).
********** 1 **********
--- page 2 ---
7. Therefore, supervised learning requires labeled data to guide the
learning process, whereas unsupervised learning operates without
labeled data and relies on the inherent structure of the data.
b.   Explain the concept of maximum margin in Support Vector Machines. Why is
maximizing the margin important?
CO3- ;   1. Definition of margin in SVM — 3 marks
SO-2;   2. Concept of maximum margin / optimal hyperplane — 3 marks   5
BL-2   3. Importance of maximizing margin (generalization / robustness) — 2
marks
4. Overall justification / conclusion — 2 marks
c. Why are Regression Trees considered non-linear models? Explain your answer
briefly.
CO-3 ;
1. Definition of Regression Trees — 3 marks
SO-2 ;   5
2. Explanation of piecewise prediction / splitting mechanism — 3 marks
BL-2
3. Reason why they model nonlinear relationships — 2 marks
4. Brief conclusion / justification — 2 marks
d. When is validation necessary in a machine learning model? Explain the concept
CO-2 ;   of cross-validation with one technique.
SO-2 ;   Requirement of validating a machine learning model: 1 mark   5
Method of validation: 1 mark
BL-2
Cross-validation: 1 mark
Technique of cross-validation: 2 marks
********** 2 **********
--- page 3 ---
Q2   a.   Consider the following dataset for predicting whether a person will Play
CO-3;   Tennis based on Outlook, Temperature, and Humidity. Using the Naive
SO-2;   Bayes classifier, classify the instance:   [10]
BL-3   (Outlook=Sunny, Temperature=Cool, Humidity=High)
Temperatur
No.   Outlook   Humidity   Play
e
1   Sunny   Hot   High   No
2   Sunny   Hot   High   No
3   Overcast   Hot   High   Yes
4   Rain   Mild   High   Yes
5   Rain   Cool   Normal   Yes
6   Rain   Cool   Normal   No
7   Overcast   Cool   Normal   Yes
8   Sunny   Mild   High   No
9   Sunny   Cool   Normal   Yes
10   Rain   Mild   Normal   Yes
********** 3 **********

[Text in pictures on this page, read by OCR]
Step 1: Prior Probabilities

Total observations:
n=10

Yes:

No:

6
P(Yes) = 107 0.6

4
P(No) = 7, =0.4
--- page 4 ---
Step 2: Conditional Probabilities

For Play = Yes
Total Yes = 6

Outlook = Sunny

1
1
P(Sunny| Yes) = 6

Temperature = Cool

3
3
P(Cool|Yes) = 67 0.5

Humidity = High

2

. 2
P(High|Yes) = $7 0.333

For Play = No
Total No = 4

Outlook = Sunny

3
3
P(Sunny|No) = i= 0.75
Temperature = Cool
1
1
P(Cool|No) = i” 0.25
Humidity = High
3

P(High|No) = : = 0.75

FIC 7) IC HOH
--- page 5 ---
CO-3;   b.   Discuss Bagging, Random Forest, and Boosting as ensemble techniques,   [10]
SO-2;   highlighting their working principles and key differences.
BL-2   1. Working principle of Bagging – 2 Marks
2. Working of Random Forest – 3 Marks
3. Working of Boosting – 3 Marks
4. Key differences among Bagging, Random Forest, and Boosting – 2
Marks
Q3   a.   The following dataset contains two variables X and Y. Apply Principal   [10]
CO-2;   Component Analysis (PCA) to compute the mean of each variable, form the
SO-2;   covariance matrix, determine the eigenvalues and eigenvectors, and identify
BL-3   the first principal component.
X   1   3   5   7
Y   2   4   6   8
********** 5 **********

[Text in pictures on this page, read by OCR]
Step 3: Posterior Probabilities

For Yes
P(Yes|X) x P(Yes) x P(Sunny|Yes) x P(Cool/Yes) x P(High|Yes)
= 0.6 x ; x 0.5 x 0.333
= 0.0167
For No

P(No|X) x 0.4 x 0.75 x 0.25 x 0.75

= 0.0563

Step 4: Final Classification

Compare:
P(Yes|X) = 0.0167
P(No|X) = 0.0563
Since:

0.0563 > 0.0167

Final Answer

Predicted class = No
--- page 6 ---
Solution
Step 1: Mean of each variable (1 marks)
Mean of X = (1 + 3 + 5 + 7) / 4 = 4.00
Mean of Y = (2 + 4 + 6 + 8) / 4 = 5.00
Mean vector = (4.00, 5.00)
Step 2: Center the data (2 marks)
on   X - mean   Y - mean
-3.00   -3.00
-1.00   -1.00
1.00   1.00
3.00   3.00
Step 3: Covariance matrix (2 marks)
Cov(X,X) = 6.6667
Cov(Y,Y) = 6.6667
Cov(X,Y) = 6.6667
Covariance matrix = [[6.6667, 6.6667], [6.6667, 6.6667]]
Step 4: Eigenvalues and eigenvectors (4 marks)
Eigenvalue λ1 = 13.3333
Eigenvalue λ2 = 0.0000
Eigenvector for λ1 = (0.7071, 0.7071)
Eigenvector for λ2 = (-0.7071, 0.7071)
Step 5: First principal component (1 marks)
The first principal component is the eigenvector corresponding to the largest
eigenvalue, so PC1 = (0.7071, 0.7071).
Final Answer
Mean vector   (4.00, 5.00)
[[6.6667, 6.6667], [6.6667,
Covariance matrix
6.6667]]
Eigenvalues   13.3333, 0.0000
PC1 direction   (0.7071, 0.7071)
********** 6 **********
--- page 7 ---
PC1 captures the maximum
Interpretation
variance (100.00%).
b.   Discuss the formulation of Multiple Linear Regression, including model   [10]
representation, assumptions, and interpretation of coefficients.
CO-2;
1. Model representation and formulation of Multiple Linear Regression –
SO-2;
3 Marks
BL-2
2. Assumptions of Multiple Linear Regression – 4 Marks
3. Interpretation of regression coefficients – 3 Marks
Q4   a.   Explain the fundamental concept of Logistic Regression. How does it   [10]
CO-3;   approach the task of classification? What is the importance of the sigmoid
SO-2;   function and loss function?
BL-2   1. Fundamental concept of Logistic Regression – 3 Marks
2. Approach to classification – 3 Marks
3. Role of sigmoid function – 2 Marks
4. Importance of loss function – 2 Marks
CO-3;   b.   Consider the multi-layer perceptron network consisting of two input neurons,
SO-2;   [10]
1   1
BL-3
0.25   0.3
X1   0.15   Z1   0.4   Y1
0.2   0.3   0.6   0.5
X2   0.4   Z2   0.45   Y2
0.1
0.35
1   1
two hidden neurons, and two output neurons as given in the figure. Consider
the input as (X1, X2) = (0, 1). Compute the outputs Y1 and Y2 for the forward
pass, considering the sigmoid activation function. Also, compute the error for
the output vector (1, 0).
To calculate the output of the network, we need to calculate the activation of
hidden neurons: (4 Marks)
********** 7 **********
--- page 8 ---
𝑧𝑖𝑛1 = 𝑥1 ∗𝑣11 + 𝑥2 ∗𝑣21 + 𝑣01 = 0 ∗0.15 + 1 ∗0.3 + 0.25 = 0.55
𝑧𝑖𝑛2 = 𝑥1 ∗𝑣12 + 𝑥2 ∗𝑣22 + 𝑣02 = 0 ∗0.2 + 1 ∗0.4 + 0.35 = 0.75
1   1   1
𝑧1 =   =   =   = 0.6342
1 + 𝑒−𝑧𝑖𝑛1 1 + 𝑒−0.55 1 + 0.5769
1   1   1
𝑧2 =   =   =   = 0.6792
1 + 𝑒−𝑧𝑖𝑛2 1 + 𝑒−0.75 1 + 0.4724
Calculate the activations of the output neuron: (4 marks)
𝑦𝑖𝑛1 = 𝑧1 ∗𝑤11 + 𝑧2 ∗𝑤21 + 𝑤01 = 0.6342 ∗0.4 + 0.6792 ∗0.6 + 0.3
= 0.9612
𝑦𝑖𝑛2 = 𝑧1 ∗𝑤12 + 𝑧2 ∗𝑤22 + 𝑤02 = 0.6342 ∗0.5 + 0.6792 ∗0.45 + 0.1
= 0.7227
1   1   1
𝑦1 =   =   =   = 0.7234
1 + 𝑒−𝑦𝑖𝑛1 1 + 𝑒−0.9612 1 + 0.3824
1   1   1
𝑦2 =   =   =   = 0.6732
1 + 𝑒−𝑦𝑖𝑛2 1 + 𝑒−0.7227 1 + 0.4854
Error calculation: (2 marks)
Expected output (1,0)
Output from network (0.7234, 0.6732)
Error at y1=(t1-y1)=(1-0.7234)=0.2766
Error at y2=(t2-y2)=(0-0.6732)=-0.6732
Q5   a.   Consider the following dataset. Construct a full decision tree using the Gini
CO-3;   Index as the attribute selection measure. Show all calculations.   [10]
SO-2;   Study Hours   Attendance   Result
BL-3
High   Good   Pass
High   Good   Pass
High   Good   Pass
High   Poor   Fail
High   Poor   Fail
Low   Good   Fail
Low   Good   Fail
Low   Good   Fail
Low   Poor   Pass
Low   Poor   Pass
Solution
Step 1: Count the class values (2 marks)
Pass = 5, Fail = 5
Gini(D) = 1 - (5/10)^2 - (5/10)^2 = 1 - 0.25 - 0.25 = 0.50
********** 8 **********
--- page 9 ---
Step 2: Gini for attribute Study Hours (3 marks)
High: 3 Pass, 2 Fail
Gini(High) = 1 - (3/5)^2 - (2/5)^2 = 1 - 9/25 - 4/25 = 12/25 = 0.48
Low: 2 Pass, 3 Fail
Gini(Low) = 1 - (2/5)^2 - (3/5)^2 = 1 - 4/25 - 9/25 = 12/25 = 0.48
Weighted Gini(Study Hours) = (5/10)(0.48) + (5/10)(0.48) = 0.48
Step 3: Gini for attribute Attendance (3 marks)
Good: 3 Pass, 3 Fail
Gini(Good) = 1 - (3/6)^2 - (3/6)^2 = 1 - 0.25 - 0.25 = 0.50
Poor: 2 Pass, 2 Fail
Gini(Poor) = 1 - (2/4)^2 - (2/4)^2 = 1 - 0.25 - 0.25 = 0.50
Weighted Gini(Attendance) = (6/10)(0.50) + (4/10)(0.50) = 0.50
Root node decision: Choose Study Hours because it has the lower Gini value
(0.48) compared with Attendance (0.50).
Step 4: Split each branch further using Attendance (2 marks)
For Study Hours = High: using Attendance gives
- Good -> Pass, Pass, Pass -> pure leaf: Pass
- Poor -> Fail, Fail -> pure leaf: Fail
For Study Hours = Low: using Attendance gives
- Good -> Fail, Fail, Fail -> pure leaf: Fail
- Poor -> Pass, Pass -> pure leaf: Pass
Final Decision Tree
Study Hours
├── High -> Attendance
│ ├── Good -> Pass
│ └── Poor -> Fail
└── Low -> Attendance
├── Good -> Fail
└── Poor -> Pass
Final answer: The complete decision tree is created with Study Hours as the
root node and Attendance as the second splitting attribute. All terminal nodes
are pure.
b.   Discuss how Lasso regression can be used for feature selection. Why is Ridge
regression less suitable for this purpose?   [10]
CO-2;
1. Concept of Lasso regression and feature selection mechanism – 5
SO-2;
Marks
BL-2
2. Limitations of Ridge regression for feature selection – 3 Marks
3. Reasoning based on penalty functions (L1 vs L2) – 2 Marks
Q6   a.   Describe the concept of soft margin SVM. How does the regularization
parameter (C) affect the decision boundary?   [10]
********** 9 **********
--- page 10 ---
CO-3;   1. Concept of soft margin SVM – 4 Marks
SO-2;   2. Role of slack variables and margin flexibility – 2 Marks
BL-2   3. Effect of regularization parameter (C) on decision boundary – 4
Marks
CO-2;   b.   Explain the concept of a confusion matrix? How is it used to evaluate
SO-2;   classification algorithms? Define the terms Accuracy, Precision, Recall, and [10]
BL-2   F1-score from the confusion matrix.
From the confusion matrix given below, calculate accuracy, precision, recall,
and f1-score.
Actual
Positive   Negative
Positive   560   60
Prediction
Negative   70   330
Confusion Matrix=2 marks
Actual
Positive   Negativ
e
Positive   560   60
Prediction   Negativ   70   330
e
TP=560, TN=330, FP=60, FN=70
Each parameter definition and calculation (2 Marks)
𝑇𝑃+ 𝑇𝑁
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=
𝑇𝑃+ 𝑇𝑁+ 𝐹𝑃+ 𝐹𝑁
560 + 330   890
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=   =   = 0.87
560 + 330 + 60 + 70 1020
𝑇𝑃
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=
𝑇𝑃+ 𝐹𝑃
560
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=   = 0.90
560 + 60
𝑇𝑃
𝑅𝑒𝑐𝑎𝑙𝑙=
𝑇𝑃+ 𝐹𝑁
560
𝑅𝑒𝑐𝑎𝑙𝑙=   = 0.88
560 + 70
2 ∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑟𝑒𝑐𝑎𝑙𝑙
𝑓1 −𝑠𝑐𝑜𝑟𝑒=
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+ 𝑟𝑒𝑐𝑎𝑙𝑙
2 ∗0.90 ∗0.88
𝑓1 −𝑠𝑐𝑜𝑟𝑒=   = 0.89
0.90 + 0.88
Q7   a.   Explain the working of a convolutional neural network. What are the different
CO-3;   layers present in CNN? Also, explain the role of padding and stride with a [10]
SO-2;   suitable example.
BL-2   Basic Structure of CNN: 3 Marks
Layers of CNN: 3 marks
********** 10 **********
--- page 11 ---
1. Convolutional layer
2. Pooling Layer
3. Fully Connected Layer
4. Classification Layer
Concept of padding and stride with example (4 Marks)
b. Apply the DBSCAN algorithm to the given data points and create the clusters
with minPts=3 and epsilon (Ɛ=2.1).   [10]
Data Points: P1: (3, 7), P2: (4,6), P3: (5,5), P4: (6, 4), P5: (7,3), P6: (6,2)
Use Euclidean distance and calculate the distance between each point
𝐷𝑒(𝑝(𝑥1,𝑦1), 𝑞(𝑥2,𝑦2)) = √(𝑥2 −𝑥1)2 + (𝑦2 −𝑦1)2
P1 (3, 7)   P2 (4, 6)   P3 (5, 5)   P4 (6,4)   P5 (7,3)   P6
P1 (3, 7)   0   1.41   2.83   4.24   5.65
P2 (4, 6)   1.41   0   1.41   2.83   4.24
CO-3;   P3 (5, 5)   2.83   1.41   0   1.41   2.83
P4 (6,4)   4.24   2.83   1.41   0   1.41
SO-2;   P5 (7,3)   5.65   4.24   2.83   1.41   0
BL-2   P6 (6,2)   5.83   4.47   3.16   2   1.41
MinPts=3, epsilon (Ɛ)=2.1
P1: P2
P2: P1, P3
P3: P2, P4
P4: P3, P5, P6
P5: P4, P6
P6: P4, P5
Points   Status
P1 (3, 7)   Noise   Border
P2 (4, 6)   Core
P3 (5, 5)   Core
P4 (6,4)   Core
P5 (7,3)   Core
P6 (6,2)   Core
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper b252b1d1e112

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_IT_7001/Machine Learning Algorithms/ANS_Machine Learning Algorithms(702IT0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Jul 2026
- Text: mixed (13 pages), mean OCR confidence 78.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning Algorithms
Date: 13 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-   a. Explain the concepts of underfitting and overfitting in machine learning with suitable
1 ;   examples.
SO-   1. Concept of underfitting – 2 Marks   5
2;   2. Concept of overfitting – 2 Marks
BL-2   3. Examples / comparison illustrating both – 1 Mark
CO3 b
How do Logistic Regression and SVM differ in handling classification problems?
- ;
.   1. Approach to classification (probability vs margin-based) – 2 Marks   5
SO-
2. Difference in decision boundary and model behavior – 2 Marks
2;
3. Key distinguishing point (loss function / application insight) – 1 Mark
BL-2
CO-   c.
Distinguish between regression trees and classification trees.
3 ;
1. Difference based on type of target variable – 2 Marks   5
SO-2
2. Difference in splitting criteria – 2 Marks
;
3. Difference in prediction/output – 1 Mark
BL-4
CO-   d
2 ;   Explain the k-fold cross-validation technique.
SO-2   .   Algorithm to perform k-fold cross-validation: 3 marks   5
; BL-   Representation: 2 marks
2
Q2   a. The following data shows the relationship between advertising expenditure (X) and
sales revenue (Y):
CO-
3;   X   2   3   5   7   9   [10
SO-
Y   4   5   7   10   15
]
Using Simple Linear Regression:
********** 1 **********
--- page 2 ---
2;   1. Find the regression equation 𝑌= 𝑎+ 𝑏𝑋
BL-3   2. Predict the value of Y when X = 6
3. Calculate the error (residual) for each observation
4. Compute the Sum of Squared Errors (SSE)
********** 2 **********

[Text in pictures on this page, read by OCR]
Step 1: Required Sums

x Y x xy
2 4 4 8

3 5 9 15

5 7 25 35

7 10 49 70

9 15 81 135

Yo x = 26
Soy =41
Yo x? = 168
SO XY = 263

n=5

Step 2: Calculate Slope b

nVUxy -(S XV Y)
ny X?- (Sx)?
__ 5(263) — (26)(41)
5(168) — 262
1315 — 1066
~ “340 — 676
249

p-—
164

b= 1.52

b=

b

Step 3: Calculate Intercept a
_vY-byx

n
g — b= 1.52(26)
5
41 — 39.52
a-
5
_ 1.48

5
a= 0.296

a
--- page 3 ---
CO-   b   Explain Random Forest algorithm, highlighting how bootstrap sampling and random   [10
3;   feature selection contribute to reducing overfitting and improving generalization.
.   ]
SO-   1. Explanation of Random Forest algorithm / basic concept — 3 marks
2;   2. Role of bootstrap sampling in Random Forest — 3 marks
BL-2   3. Role of random feature selection — 2 marks
4. How these reduce overfitting and improve generalization — 2 marks
Q3   a. Consider the dataset below representing measurements of two features X and Y.   [10
Using Principal Component Analysis (PCA), center the data, compute the covariance
CO-   ]
matrix, determine the eigenvalues and eigenvectors, and calculate the first principal
2;
component (PC1) for the
SO-
dataset.
2;
BL-3   X   2   4   6   8
Y   4   2   6   8
********** 3 **********

[Text in pictures on this page, read by OCR]
Step 4: Regression Equation

Y = 0.296 + 1.52X

Step 5: Predict Value when X = 6
Y = 0.296 + 1.52(6)

Y = 0.296 + 9.12

Step 6: Calculate Errors (Residuals)

Error = Y —Y
x Y Predicted Y Error
2 4 3.336 0.664
3 5 4856 0.144
5 7 7.896 -0.896
7 10 10.936 0.936

9 15 13.976 1.024

Step 7: Compute Sum of Squared Errors (SSE)
SSE=)-(y-Y)?
= 0.441 + 0.021 + 0.803 + 0.876 + 1.049

Final Answer (Exam-Ready)

Regression equation:

Y = 0.296 + 1.52X

Predicted value at X = 6:

Sum of Squared Errors:
--- page 4 ---
Solution

Step 1: Mean of each variable

So, the mean vector is:

Step 2: Mean-centered data

Subtract the mean from each observation:

Observation

1

4

Step 3: Covariance matrix

Cou(X, X) =

a
4
yust2t648
4
(5,5)

X-5
3

1

1

3

(=3)? + (-1)? +17 +3? _9+1+1+9 20

—=66
4-1 3 3 7

(-1)? + (-3)? +17 +3? = 1494149

Cov(Y,Y) = = = 6.67

Cov(X,Y) =

(=3)(=1) + (-1)(-3) + ()@) + (3)(3) _ 3+34+149_ 16

3 3

So the covariance matrix is:

3 3

Step 4: Eigenvalues and eigenvectors

Solve:

On solving:

|C-AI|=0

6.67-A 5.33 |_
5.33 6.67—A|

(6.67 — )? — (5.33)? = 0

M=12, 9 Ap = 1.34

Since the largest eigenvalue is 12, this gives PCI.

Corresponding eigenvector:

| _ [0.707
"10,707

= 5.33

Y-5

FIC 7) IC HOH
--- page 5 ---
b A fitness researcher studies the effect of exercise duration (X₁) and diet type (X₂) on   [10
CO-   weight loss. It is observed that the impact of exercise differs across diet types.
.   ]
2;   Explain how an interaction term can be incorporated into the regression model and
SO-   interpret its significance.
2;
BL-2   Partition of Marks (Out of 10)
1. Concept of interaction term in regression — 3 marks
********** 5 **********

[Text in pictures on this page, read by OCR]
Step 5: Equation of PC1

The first principal component is:
PC1 = 0.707(X — 5) + 0.707(Y — 5)

This is the required PC1 equation.

Step 6: Compute PC1 scores

Now substitute each centered observation into:
PC1 = 0.707(X — 5) + 0.707(Y — 5)
Observation 1: (—3, —1)
PC1 = 0.707(—3) + 0.707(—1)
= —2.121 — 0.707 = —2.828
Observation 2: (—1, —3)
PC1 = 0.707(—1) + 0.707(—3)
= —0.707 — 2.121 = —2.828
Observation 3: (1, 1)
PC1 = 0.707(1) + 0.707(1) = 1.414
Observation 4: (3, 3)

PC1 = 0.707(3) + 0.707(3) = 4.242

Final PC1 Scores

Observation PC! Score
1 -2.828
2 -2.828
3 1414
4 4.242

Final Answer

The first principal component is:

[PC1 = 0.707(x — 5) + 0.707(¥ — 5)

The PC1 scores are:

[—2.828, —2.828, 1.414, 4.242]
--- page 6 ---
2. How to incorporate interaction term in model — 3 marks
3. Interpretation of interaction term significance — 2 marks
4. Application to given scenario (exercise and diet) — 2 marks
Answer (For Reference)
When the effect of one independent variable depends on another variable, an
interaction term is included in the regression model. In this case, the effect of exercise
duration (X1) on weight loss changes depending on the diet type (X2), indicating an
interaction between the two variables.
The interaction term is created by multiplying the two variables:
𝑋1X2
The regression model with an interaction term becomes:
The coefficient 𝛽3 indicates whether the impact of exercise on weight loss varies
across different diet types. If 𝛽3 is significant, it means the relationship between
exercise and weight loss depends on the diet type. Therefore, including an interaction
term allows the regression model to capture combined effects of variables and
represent more realistic relationships.
Q4   a.   [10
CO-   ]
3;   Describe Logistic Regression as a linear classifier, explaining odds, log-odds, and its
SO-   limitations in real-world applications.
2;
BL-2
********** 6 **********
--- page 7 ---
Partition of Marks (Out of 10)

1. Logistic Regression as a linear classifier — 3 marks

2. Explanation of odds and log-odds concepts — 3 marks

3. Working / probability modeling using sigmoid function — 2 marks
4. Limitations in real-world applications — 2 marks

Total = 10 marks

Answer (For Examiner's Reference)

Logistic Regression is a supervised learning algorithm used for binary classification. It is considered a linear
classifier because it creates a linear decision boundary between classes based on a linear combination of
input features.

The model first computes a linear function:
2 = By + BX, + BoXy +--+ + BrXn
This value is then transformed into a probability using the sigmoid (logistic) function:

P(Y =1|X)=

1l+e*

Odds
Odds represent the ratio of the probability of an event occurring to the probability of it not occurring.
P
1-P

Odds =

For example, if the probability of success is 0.8:

0.8
Odds = —— = 4
S02

This means success is four times more likely than failure.

Log-Odds (Logit)
Log-odds, also called the logit, is the natural logarithm of the odds.

P
Log-odds = log TP

Logistic Regression models this log-odds as a linear function of the input variables:

P
we ("5 *;) = Bot MiX1+--++ BnXn
Thus, the classifier is linear in terms of log-odds, which is why Logistic Regression is considered a linear
classifier.

Limitations in Real-World Applications
1. Logistic Regression assumes a linear relationship between predictors and log-odds.
2. It performs poorly when the relationship between variables is highly nonlinear.
3. It is sensitive to outliers and multicollinearity.
4. It may struggle with high-dimensional or complex datasets without feature engineering.
5. It requires sufficient and relevant features to achieve good performance.

FIC 7 IC OHH
--- page 8 ---
CO-   b   Consider the multi-layer perceptron network consisting of two input neurons, two
3;   hidden neurons, and two output neurons as given in the figure. Consider the input as
.   [10
SO-   (X1, X2) = (0, 1). Compute the outputs Y1 and Y2 for the forward pass, considering the
2;   sigmoid activation function. Also, compute the error for the output vector (1, 0).   ]
BL-3
1   1
0.15   0.35
X1   0.4   Z1   0.3   Y1
0.3   0.2   0.2   0.25
X2   0.1   Z2   0.4   Y2
0.15
0.25
1   1
To calculate the output of the network, we need to calculate the activation of hidden neurons:
(4 Marks)
𝑧𝑖𝑛1 = 𝑥1 ∗𝑣11 + 𝑥2 ∗𝑣21 + 𝑣01 = 0 ∗0.4 + 1 ∗0.2 + 0.15 = 0.35
𝑧𝑖𝑛2 = 𝑥1 ∗𝑣12 + 𝑥2 ∗𝑣22 + 𝑣02 = 0 ∗0.3 + 1 ∗0.1 + 0.25 = 0.35
1   1   1
𝑧1 =   =   =   = 0.5866
1 + 𝑒−𝑧𝑖𝑛1 1 + 𝑒−0.35 1 + 0.7047
1   1   1
𝑧2 =   =   =   = 0.5866
1 + 𝑒−𝑧𝑖𝑛2 1 + 𝑒−0.35 1 + 0.7047
Calculate the activations of the output neuron: (4 marks)
𝑦𝑖𝑛1 = 𝑧1 ∗𝑤11 + 𝑧2 ∗𝑤21 + 𝑤01 = 0.5866 ∗0.3 + 0.5866 ∗0.25 + 0.35 = 0.6726
𝑦𝑖𝑛2 = 𝑧1 ∗𝑤12 + 𝑧2 ∗𝑤22 + 𝑤02 = 0.5866 ∗0.2 + 0.5866 ∗0.4 + 0.15 = 0.5020
1   1   1
𝑦1 =   =   =   = 0.6621
1 + 𝑒−𝑦𝑖𝑛1 1 + 𝑒−0.6726 1 + 0.5104
1   1   1
𝑦2 =   =   =   = 0.6229
1 + 𝑒−𝑦𝑖𝑛2 1 + 𝑒−0.5020 1 + 0.6053
Error calculation: (2 marks)
Expected output (1,0)
Output from network (0.6621, 0.6229)
Error at y1=(t1-y1)=(1-0.6621)=0.3379
Error at y2=(t2-y2)=(0-0.6229)=-0.6229
********** 8 **********
--- page 9 ---
Q5   a. Using the dataset given below, compute the Gini Index for each attribute (Weather,
CO-   Parents, and Decision) considering Money as the class label.   [10
3;
Determine the best attribute for the root node of the Decision Tree using the Gini   ]
SO-
2;   Index as the attribute selection measure.
BL-3
Weather Parents Decision Money
Sunny   Yes   Cinema   Rich
Sunny   No   Tennis   Rich
Windy   Yes   Cinema   Rich
Rainy   Yes   Cinema   Poor
Rainy   No   Stay-In   Rich
Rainy   Yes   Cinema   Poor
Windy   No   Cinema   Poor
Windy   No   Shopping   Rich
Windy   Yes   Cinema   Rich
Sunny   No   Tennis   Rich
********** 9 **********

[Text in pictures on this page, read by OCR]
Step 1: Count Class Values

Total records = 10
Class (Money):

© Rich =7
© Poor =3

Step 2: Gini Index of Dataset

‘We use the formula:

Gini(D) = 1- Sop?

(3) - (a)

Gini(D) = 1 — 0.49 — 0.09

Gini(D) =

Gini(D)

2

Step 3: Gini Index for Attribute Weather

Sunny
Records: 1, 2, 10
© Rich =3

© Poor =0

Gini(Sunny) = 0
--- page 10 ---
Windy

Records: 3, 7, 8,9

© Rich=3

© Poor=1
2

3)? (1)?
Gini(Windy) =1—{-—}) —[-
ini(Windy) (2) (3)

= 0.375

Rainy
Records: 4, 5,6
© Rich =1

© Poor =2

Gini(Rainy) = 0.444

Weighted Gini for Weather

3 4 3
Gini(Weather) = —(0 — (0.375) + —(0.444
ini(W eather) 10! )+ 10! 5) 10! )

Gini(W eather) = 0.283

Step 4: Gini Index for Attribute Parents

Parents = Yes
Records: 1, 3, 4, 6,9

© Rich=
© Poor=2

Gini(Yes) = 0.48

Parents = No
Records: 2, 5, 7,8, 10

© Rich=
© Poor=1

Gini(No) = 0.32

Weighted Gini for Parents

Gini(Parents) = (0-48) + Fp (0-82)

Gini(Parent .40

FRR ICR 7 OI HOH
--- page 11 ---
b   Explain the concept of Ridge Regression. Discuss its mathematical formulation and
CO-
2;   . how it helps in controlling model complexity.   [10
SO-   1. Concept of Ridge Regression   3 marks   ]
2;
2. Mathematical formulation   4 marks
BL-2
3. Control of model complexity   3 marks
Q6   a. Define following terminologies with reference to Support vector machine:
CO-   Hyper plane, Support Vectors, Hard Margin, Soft Margin, Kernel   [10
3;
Hyperplane 2 marks   ]
SO-
2;   Support Vectors 2 marks
BL-2   Hard Margin 2 marks
********** 11 **********

[Text in pictures on this page, read by OCR]
Step 5: Gini Index for Attribute Decision

Cinema

© Rich=3
© Poor=3

Gini(Cinema) = 0.50

Tennis
Records: 2, 10

Gini(Tennis) = 0

Stay-In
Record: 5

Gini(Stay-In) = 0

Shopping
Record: 8

Gini( Shopping) = 0

Weighted Gini for Decision

6 2 1 1
Gini (Decision) = 55 (0-50) + 75(0) + 75(0) + 5)

Step 6: Compare All Gini Values

Attribute Gini
Weather 0.283
Parents 0.40
Decision 0,30

Final Answer (Root Node Only)

The attribute with the minimum Gini Index is:

Therefore,

Root Node of the Decision Tree = Weather
--- page 12 ---
Soft Margin 2 marks
Kernel 2 marks
CO-   b A classification model is applied to the cancer dataset to identify whether the person
2;   has cancer or not. Class 1 denotes a person has cancer, and class 0 denotes a person
.   [10
SO-   does not have cancer. The table below denotes the actual class and the predicted class
2;   for each sample of the test data.   ]
BL-3   Construct a confusion matrix, calculate the accuracy of the model, and fill the
classification report.
Sample   Y   Y   Sample   Y   Y
ID   Actual   Predicted   ID   Actual   Predicted
1   1   0   11   1   0
2   1   1   12   1   1
3   1   1   13   1   1
4   0   0   14   0   0
5   1   1   15   1   1
6   0   1   16   0   1
7   1   1   17   1   1
8   0   1   18   0   1
9   1   1   19   1   0
10   0   0   20   0   1
Classification Report
Precision   Recall   F1-Score
Class   1   (has
cancer)
Actual
Positive   Negative
[10
Positive   09   05
Prediction   (Class 1)   ]
Negative   03   03
From the confusion matrix
TP=09, FP=05, TN=03, FN=03
𝑇𝑃+ 𝑇𝑁
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=
𝑇𝑃+ 𝑇𝑁+ 𝐹𝑃+ 𝐹𝑁
9 + 3   12
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=   = = 0.6
9 + 3 + 5 + 3 20
𝑇𝑃
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=
𝑇𝑃+ 𝐹𝑃
9
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=   = 0.64
9 + 5
𝑇𝑃
𝑅𝑒𝑐𝑎𝑙𝑙=
𝑇𝑃+ 𝐹𝑁
9
𝑅𝑒𝑐𝑎𝑙𝑙=   = 0.75
9 + 3
2 ∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑟𝑒𝑐𝑎𝑙𝑙
𝑓1 −𝑠𝑐𝑜𝑟𝑒=
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+ 𝑟𝑒𝑐𝑎𝑙𝑙
2 ∗0.64 ∗0.75
𝑓1 −𝑠𝑐𝑜𝑟𝑒=   = 0.69
0.64 + 0.75
********** 12 **********
--- page 13 ---
Precision   Recall   F1-Score
Class   1   (has 0.64   0.75   0.69
cancer)
b What is the DBSCAN Clustering algorithm? Explain the role of Epsilon (Ɛ) and the MinPts
CO-
Parameter in DBSCAN. Explain the steps used to identify core points, border points, and
3;   .   [10
noise points.
SO-   DBSCAN Algorithm: 2 marks   ]
2;   Importance of parameters Epsilon (Ɛ) and the MinPts: 4 marks
BL-2   steps used to identify core points, border points, and noise points: 4 marks
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 10 · Answer key · paper 3f7bed5e1c03

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Re-Exam/Integrated_IT_7037/Machine Learning Algorithms/ANS_Machine Learning Algorithms(702IT0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Jul 2026
- Text: mixed (13 pages), mean OCR confidence 78.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning Algorithms
Date: 13 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-   a. Explain the concepts of underfitting and overfitting in machine learning with suitable
1 ;   examples.
SO-   1. Concept of underfitting – 2 Marks   5
2;   2. Concept of overfitting – 2 Marks
BL-2   3. Examples / comparison illustrating both – 1 Mark
CO3 b
How do Logistic Regression and SVM differ in handling classification problems?
- ;
.   1. Approach to classification (probability vs margin-based) – 2 Marks   5
SO-
2. Difference in decision boundary and model behavior – 2 Marks
2;
3. Key distinguishing point (loss function / application insight) – 1 Mark
BL-2
CO-   c.
Distinguish between regression trees and classification trees.
3 ;
1. Difference based on type of target variable – 2 Marks   5
SO-2
2. Difference in splitting criteria – 2 Marks
;
3. Difference in prediction/output – 1 Mark
BL-4
CO-   d
2 ;   Explain the k-fold cross-validation technique.
SO-2   .   Algorithm to perform k-fold cross-validation: 3 marks   5
; BL-   Representation: 2 marks
2
Q2   a. The following data shows the relationship between advertising expenditure (X) and
sales revenue (Y):
CO-
3;   X   2   3   5   7   9   [10
SO-
Y   4   5   7   10   15
]
Using Simple Linear Regression:
********** 1 **********
--- page 2 ---
2;   1. Find the regression equation 𝑌= 𝑎+ 𝑏𝑋
BL-3   2. Predict the value of Y when X = 6
3. Calculate the error (residual) for each observation
4. Compute the Sum of Squared Errors (SSE)
********** 2 **********

[Text in pictures on this page, read by OCR]
Step 1: Required Sums

x Y x xy
2 4 4 8

3 5 9 15

5 7 25 35

7 10 49 70

9 15 81 135

Yo x = 26
Soy =41
Yo x? = 168
SO XY = 263

n=5

Step 2: Calculate Slope b

nVUxy -(S XV Y)
ny X?- (Sx)?
__ 5(263) — (26)(41)
5(168) — 262
1315 — 1066
~ “340 — 676
249

p-—
164

b= 1.52

b=

b

Step 3: Calculate Intercept a
_vY-byx

n
g — b= 1.52(26)
5
41 — 39.52
a-
5
_ 1.48

5
a= 0.296

a
--- page 3 ---
CO-   b   Explain Random Forest algorithm, highlighting how bootstrap sampling and random   [10
3;   feature selection contribute to reducing overfitting and improving generalization.
.   ]
SO-   1. Explanation of Random Forest algorithm / basic concept — 3 marks
2;   2. Role of bootstrap sampling in Random Forest — 3 marks
BL-2   3. Role of random feature selection — 2 marks
4. How these reduce overfitting and improve generalization — 2 marks
Q3   a. Consider the dataset below representing measurements of two features X and Y.   [10
Using Principal Component Analysis (PCA), center the data, compute the covariance
CO-   ]
matrix, determine the eigenvalues and eigenvectors, and calculate the first principal
2;
component (PC1) for the
SO-
dataset.
2;
BL-3   X   2   4   6   8
Y   4   2   6   8
********** 3 **********

[Text in pictures on this page, read by OCR]
Step 4: Regression Equation

Y = 0.296 + 1.52X

Step 5: Predict Value when X = 6
Y = 0.296 + 1.52(6)

Y = 0.296 + 9.12

Step 6: Calculate Errors (Residuals)

Error = Y —Y
x Y Predicted Y Error
2 4 3.336 0.664
3 5 4856 0.144
5 7 7.896 -0.896
7 10 10.936 0.936

9 15 13.976 1.024

Step 7: Compute Sum of Squared Errors (SSE)
SSE=)-(y-Y)?
= 0.441 + 0.021 + 0.803 + 0.876 + 1.049

Final Answer (Exam-Ready)

Regression equation:

Y = 0.296 + 1.52X

Predicted value at X = 6:

Sum of Squared Errors:
--- page 4 ---
Solution

Step 1: Mean of each variable

So, the mean vector is:

Step 2: Mean-centered data

Subtract the mean from each observation:

Observation

1

4

Step 3: Covariance matrix

Cou(X, X) =

a
4
yust2t648
4
(5,5)

X-5
3

1

1

3

(=3)? + (-1)? +17 +3? _9+1+1+9 20

—=66
4-1 3 3 7

(-1)? + (-3)? +17 +3? = 1494149

Cov(Y,Y) = = = 6.67

Cov(X,Y) =

(=3)(=1) + (-1)(-3) + ()@) + (3)(3) _ 3+34+149_ 16

3 3

So the covariance matrix is:

3 3

Step 4: Eigenvalues and eigenvectors

Solve:

On solving:

|C-AI|=0

6.67-A 5.33 |_
5.33 6.67—A|

(6.67 — )? — (5.33)? = 0

M=12, 9 Ap = 1.34

Since the largest eigenvalue is 12, this gives PCI.

Corresponding eigenvector:

| _ [0.707
"10,707

= 5.33

Y-5

FIC 7) IC HOH
--- page 5 ---
b A fitness researcher studies the effect of exercise duration (X₁) and diet type (X₂) on   [10
CO-   weight loss. It is observed that the impact of exercise differs across diet types.
.   ]
2;   Explain how an interaction term can be incorporated into the regression model and
SO-   interpret its significance.
2;
BL-2   Partition of Marks (Out of 10)
1. Concept of interaction term in regression — 3 marks
********** 5 **********

[Text in pictures on this page, read by OCR]
Step 5: Equation of PC1

The first principal component is:
PC1 = 0.707(X — 5) + 0.707(Y — 5)

This is the required PC1 equation.

Step 6: Compute PC1 scores

Now substitute each centered observation into:
PC1 = 0.707(X — 5) + 0.707(Y — 5)
Observation 1: (—3, —1)
PC1 = 0.707(—3) + 0.707(—1)
= —2.121 — 0.707 = —2.828
Observation 2: (—1, —3)
PC1 = 0.707(—1) + 0.707(—3)
= —0.707 — 2.121 = —2.828
Observation 3: (1, 1)
PC1 = 0.707(1) + 0.707(1) = 1.414
Observation 4: (3, 3)

PC1 = 0.707(3) + 0.707(3) = 4.242

Final PC1 Scores

Observation PC! Score
1 -2.828
2 -2.828
3 1414
4 4.242

Final Answer

The first principal component is:

[PC1 = 0.707(x — 5) + 0.707(¥ — 5)

The PC1 scores are:

[—2.828, —2.828, 1.414, 4.242]
--- page 6 ---
2. How to incorporate interaction term in model — 3 marks
3. Interpretation of interaction term significance — 2 marks
4. Application to given scenario (exercise and diet) — 2 marks
Answer (For Reference)
When the effect of one independent variable depends on another variable, an
interaction term is included in the regression model. In this case, the effect of exercise
duration (X1) on weight loss changes depending on the diet type (X2), indicating an
interaction between the two variables.
The interaction term is created by multiplying the two variables:
𝑋1X2
The regression model with an interaction term becomes:
The coefficient 𝛽3 indicates whether the impact of exercise on weight loss varies
across different diet types. If 𝛽3 is significant, it means the relationship between
exercise and weight loss depends on the diet type. Therefore, including an interaction
term allows the regression model to capture combined effects of variables and
represent more realistic relationships.
Q4   a.   [10
CO-   ]
3;   Describe Logistic Regression as a linear classifier, explaining odds, log-odds, and its
SO-   limitations in real-world applications.
2;
BL-2
********** 6 **********
--- page 7 ---
Partition of Marks (Out of 10)

1. Logistic Regression as a linear classifier — 3 marks

2. Explanation of odds and log-odds concepts — 3 marks

3. Working / probability modeling using sigmoid function — 2 marks
4. Limitations in real-world applications — 2 marks

Total = 10 marks

Answer (For Examiner's Reference)

Logistic Regression is a supervised learning algorithm used for binary classification. It is considered a linear
classifier because it creates a linear decision boundary between classes based on a linear combination of
input features.

The model first computes a linear function:
2 = By + BX, + BoXy +--+ + BrXn
This value is then transformed into a probability using the sigmoid (logistic) function:

P(Y =1|X)=

1l+e*

Odds
Odds represent the ratio of the probability of an event occurring to the probability of it not occurring.
P
1-P

Odds =

For example, if the probability of success is 0.8:

0.8
Odds = —— = 4
S02

This means success is four times more likely than failure.

Log-Odds (Logit)
Log-odds, also called the logit, is the natural logarithm of the odds.

P
Log-odds = log TP

Logistic Regression models this log-odds as a linear function of the input variables:

P
we ("5 *;) = Bot MiX1+--++ BnXn
Thus, the classifier is linear in terms of log-odds, which is why Logistic Regression is considered a linear
classifier.

Limitations in Real-World Applications
1. Logistic Regression assumes a linear relationship between predictors and log-odds.
2. It performs poorly when the relationship between variables is highly nonlinear.
3. It is sensitive to outliers and multicollinearity.
4. It may struggle with high-dimensional or complex datasets without feature engineering.
5. It requires sufficient and relevant features to achieve good performance.

FIC 7 IC OHH
--- page 8 ---
CO-   b   Consider the multi-layer perceptron network consisting of two input neurons, two
3;   hidden neurons, and two output neurons as given in the figure. Consider the input as
.   [10
SO-   (X1, X2) = (0, 1). Compute the outputs Y1 and Y2 for the forward pass, considering the
2;   sigmoid activation function. Also, compute the error for the output vector (1, 0).   ]
BL-3
1   1
0.15   0.35
X1   0.4   Z1   0.3   Y1
0.3   0.2   0.2   0.25
X2   0.1   Z2   0.4   Y2
0.15
0.25
1   1
To calculate the output of the network, we need to calculate the activation of hidden neurons:
(4 Marks)
𝑧𝑖𝑛1 = 𝑥1 ∗𝑣11 + 𝑥2 ∗𝑣21 + 𝑣01 = 0 ∗0.4 + 1 ∗0.2 + 0.15 = 0.35
𝑧𝑖𝑛2 = 𝑥1 ∗𝑣12 + 𝑥2 ∗𝑣22 + 𝑣02 = 0 ∗0.3 + 1 ∗0.1 + 0.25 = 0.35
1   1   1
𝑧1 =   =   =   = 0.5866
1 + 𝑒−𝑧𝑖𝑛1 1 + 𝑒−0.35 1 + 0.7047
1   1   1
𝑧2 =   =   =   = 0.5866
1 + 𝑒−𝑧𝑖𝑛2 1 + 𝑒−0.35 1 + 0.7047
Calculate the activations of the output neuron: (4 marks)
𝑦𝑖𝑛1 = 𝑧1 ∗𝑤11 + 𝑧2 ∗𝑤21 + 𝑤01 = 0.5866 ∗0.3 + 0.5866 ∗0.25 + 0.35 = 0.6726
𝑦𝑖𝑛2 = 𝑧1 ∗𝑤12 + 𝑧2 ∗𝑤22 + 𝑤02 = 0.5866 ∗0.2 + 0.5866 ∗0.4 + 0.15 = 0.5020
1   1   1
𝑦1 =   =   =   = 0.6621
1 + 𝑒−𝑦𝑖𝑛1 1 + 𝑒−0.6726 1 + 0.5104
1   1   1
𝑦2 =   =   =   = 0.6229
1 + 𝑒−𝑦𝑖𝑛2 1 + 𝑒−0.5020 1 + 0.6053
Error calculation: (2 marks)
Expected output (1,0)
Output from network (0.6621, 0.6229)
Error at y1=(t1-y1)=(1-0.6621)=0.3379
Error at y2=(t2-y2)=(0-0.6229)=-0.6229
********** 8 **********
--- page 9 ---
Q5   a. Using the dataset given below, compute the Gini Index for each attribute (Weather,
CO-   Parents, and Decision) considering Money as the class label.   [10
3;
Determine the best attribute for the root node of the Decision Tree using the Gini   ]
SO-
2;   Index as the attribute selection measure.
BL-3
Weather Parents Decision Money
Sunny   Yes   Cinema   Rich
Sunny   No   Tennis   Rich
Windy   Yes   Cinema   Rich
Rainy   Yes   Cinema   Poor
Rainy   No   Stay-In   Rich
Rainy   Yes   Cinema   Poor
Windy   No   Cinema   Poor
Windy   No   Shopping   Rich
Windy   Yes   Cinema   Rich
Sunny   No   Tennis   Rich
********** 9 **********

[Text in pictures on this page, read by OCR]
Step 1: Count Class Values

Total records = 10
Class (Money):

© Rich =7
© Poor =3

Step 2: Gini Index of Dataset

‘We use the formula:

Gini(D) = 1- Sop?

(3) - (a)

Gini(D) = 1 — 0.49 — 0.09

Gini(D) =

Gini(D)

2

Step 3: Gini Index for Attribute Weather

Sunny
Records: 1, 2, 10
© Rich =3

© Poor =0

Gini(Sunny) = 0
--- page 10 ---
Windy

Records: 3, 7, 8,9

© Rich=3

© Poor=1
2

3)? (1)?
Gini(Windy) =1—{-—}) —[-
ini(Windy) (2) (3)

= 0.375

Rainy
Records: 4, 5,6
© Rich =1

© Poor =2

Gini(Rainy) = 0.444

Weighted Gini for Weather

3 4 3
Gini(Weather) = —(0 — (0.375) + —(0.444
ini(W eather) 10! )+ 10! 5) 10! )

Gini(W eather) = 0.283

Step 4: Gini Index for Attribute Parents

Parents = Yes
Records: 1, 3, 4, 6,9

© Rich=
© Poor=2

Gini(Yes) = 0.48

Parents = No
Records: 2, 5, 7,8, 10

© Rich=
© Poor=1

Gini(No) = 0.32

Weighted Gini for Parents

Gini(Parents) = (0-48) + Fp (0-82)

Gini(Parent .40

FRR ICR 7 OI HOH
--- page 11 ---
b   Explain the concept of Ridge Regression. Discuss its mathematical formulation and
CO-
2;   . how it helps in controlling model complexity.   [10
SO-   1. Concept of Ridge Regression   3 marks   ]
2;
2. Mathematical formulation   4 marks
BL-2
3. Control of model complexity   3 marks
Q6   a. Define following terminologies with reference to Support vector machine:
CO-   Hyper plane, Support Vectors, Hard Margin, Soft Margin, Kernel   [10
3;
Hyperplane 2 marks   ]
SO-
2;   Support Vectors 2 marks
BL-2   Hard Margin 2 marks
********** 11 **********

[Text in pictures on this page, read by OCR]
Step 5: Gini Index for Attribute Decision

Cinema

© Rich=3
© Poor=3

Gini(Cinema) = 0.50

Tennis
Records: 2, 10

Gini(Tennis) = 0

Stay-In
Record: 5

Gini(Stay-In) = 0

Shopping
Record: 8

Gini( Shopping) = 0

Weighted Gini for Decision

6 2 1 1
Gini (Decision) = 55 (0-50) + 75(0) + 75(0) + 5)

Step 6: Compare All Gini Values

Attribute Gini
Weather 0.283
Parents 0.40
Decision 0,30

Final Answer (Root Node Only)

The attribute with the minimum Gini Index is:

Therefore,

Root Node of the Decision Tree = Weather
--- page 12 ---
Soft Margin 2 marks
Kernel 2 marks
CO-   b A classification model is applied to the cancer dataset to identify whether the person
2;   has cancer or not. Class 1 denotes a person has cancer, and class 0 denotes a person
.   [10
SO-   does not have cancer. The table below denotes the actual class and the predicted class
2;   for each sample of the test data.   ]
BL-3   Construct a confusion matrix, calculate the accuracy of the model, and fill the
classification report.
Sample   Y   Y   Sample   Y   Y
ID   Actual   Predicted   ID   Actual   Predicted
1   1   0   11   1   0
2   1   1   12   1   1
3   1   1   13   1   1
4   0   0   14   0   0
5   1   1   15   1   1
6   0   1   16   0   1
7   1   1   17   1   1
8   0   1   18   0   1
9   1   1   19   1   0
10   0   0   20   0   1
Classification Report
Precision   Recall   F1-Score
Class   1   (has
cancer)
Actual
Positive   Negative
[10
Positive   09   05
Prediction   (Class 1)   ]
Negative   03   03
From the confusion matrix
TP=09, FP=05, TN=03, FN=03
𝑇𝑃+ 𝑇𝑁
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=
𝑇𝑃+ 𝑇𝑁+ 𝐹𝑃+ 𝐹𝑁
9 + 3   12
𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑦=   = = 0.6
9 + 3 + 5 + 3 20
𝑇𝑃
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=
𝑇𝑃+ 𝐹𝑃
9
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=   = 0.64
9 + 5
𝑇𝑃
𝑅𝑒𝑐𝑎𝑙𝑙=
𝑇𝑃+ 𝐹𝑁
9
𝑅𝑒𝑐𝑎𝑙𝑙=   = 0.75
9 + 3
2 ∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑟𝑒𝑐𝑎𝑙𝑙
𝑓1 −𝑠𝑐𝑜𝑟𝑒=
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+ 𝑟𝑒𝑐𝑎𝑙𝑙
2 ∗0.64 ∗0.75
𝑓1 −𝑠𝑐𝑜𝑟𝑒=   = 0.69
0.64 + 0.75
********** 12 **********
--- page 13 ---
Precision   Recall   F1-Score
Class   1   (has 0.64   0.75   0.69
cancer)
b What is the DBSCAN Clustering algorithm? Explain the role of Epsilon (Ɛ) and the MinPts
CO-
Parameter in DBSCAN. Explain the steps used to identify core points, border points, and
3;   .   [10
noise points.
SO-   DBSCAN Algorithm: 2 marks   ]
2;   Importance of parameters Epsilon (Ɛ) and the MinPts: 4 marks
BL-2   steps used to identify core points, border points, and noise points: 4 marks
********** 13 **********
````
