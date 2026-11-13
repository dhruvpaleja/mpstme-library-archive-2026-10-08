# Machine Learning: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper f72690472fcb

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Machine Learning/ANS_Machine Learning(703CO0C025)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: mixed (19 pages), mean OCR confidence 54.1
- 5 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: NA)
Subject: Machine Learning
Date: NA   Time: NA to NA (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 1 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
a. How do we select the ML model? Discuss the necessary steps.
Ans:
Understanding the Problem and Data: Regression, classification or clustering
1. Understanding data
2. Define and understand the problem clearly   [05]
3. Start the process with a simple model
4. Evaluate multiple models
5. Consider computational resources and subsequently complexity.
Cross-Validation Based Selection [1 Marks for each step]
b. Discuss the steps of feature engineering used in ML
Ans: [1 Marks for each step]
1. Feature Creation
2. Feature Transformation   [05]
3. Feature Extraction
4. Feature Selection
5. Feature Scaling
c. Discuss the advantages and disadvantages of tree-based classification models with
a suitable example.
[05]
Advantages: [3 Marks]
1. Relatively Easy to Interpret,
********** 1 **********
--- page 2 ---
2. Robust to Outliers
3. Can Deal with Missing Values
4. Non-Linear
5. Combining Features to Make Predictions
Disadvantage: [2 Marks]
1. Prone to Overfitting
2. Unstable to Changes in the Data
3. Unstable to Noise
4. Unbalanced Classes
d. Explain the hierarchical clustering algorithm with the help of a suitable example.
Ans:
Explanation [3 Marks]
1   Hierarchical   clustering   is   an unsupervised   machine   learning
algorithm used to group similar data points into clusters by creating a
hierarchy (tree-like structure) of clusters.
2   It is particularly useful when the number of clusters is not known beforehand.
The algorithm operates in two main approaches:
 Agglomerative (Bottom-Up): Starts with each data point as its own
cluster and merges them iteratively based on similarity until all points
belong to a single cluster or a stopping criterion is met.
 Divisive (Top-Down): Starts with all data points in one cluster and splits
[05]
them iteratively into smaller clusters.
Advantages
 Does not require specifying the number of clusters in advance.
 Produces a dendrogram (tree structure) that provides insights into the data's
hierarchical relationships.
Disadvantages
 Computationally expensive for large datasets (time complexity)
   Sensitive to noise and outliers.
Hierarchical clustering is widely used in fields like bioinformatics, market
segmentation, and document clustering.
Example [2 Marks]
********** 2 **********
--- page 3 ---
a. Apply polynomial regression model up to degree 2? Consider following dataset
with three samples. Find out all the required coefficients of the model and predict
the value of Y for given value of X.
Study Time (X) in   Marks obtained (Y)
Hrs.   in multiple of 10
1   2
4   3
Q2   5   6   [10]
Predict the marks if the study time 2.5 hrs.
Ans:
Scatter plot [2 Marks]
Calculation table with X and X^2 and all other values [4 Marks]
Calculation of coefficients – [2 Marks]
********** 3 **********
--- page 4 ---

--- page 5 ---
b. Explain in detail the concept of Gradient Descent with suitable example.
Ans:
Explanation of concept [2 Marks]
Gradient curve need to form with example and explain [4 Marks]   [10]
Finalization of value of Y intercept and slope need to explain with example [4
Marks]
 Steps of GD, Gradient Curve and example:
********** 5 **********
--- page 6 ---

--- page 7 ---
FRAO 7) AACR Ck ok ok ok oak
--- page 8 ---
a. Design and train the single layer perceptron network for the following dataset.
Network should be able to satisfy all the input feature vectors. Also consider the
bias and display data using scatter plot.
X1 X2   Class
0   0   0
0   1   0
1   0   0
1   1   1
Ans:
Scatter Plot [2 Marks]
Solving complete example [8 Marks]
Q3
[10]
b. What is the significance of correlation coefficient? How do you use it in the linear
regression to derive the model? Explain with example.
Ans: Students can give any example of linear regression to find out the model with   [10]
correlation coefficient. For reference one example is given below to understand the steps.
Significance [2 Marks]
Use and finding model with example [8 Marks]
********** 8 **********
--- page 9 ---

--- page 10 ---

--- page 11 ---
a. A pharmaceutical company would like to test the efficiency of its drugs in terms of
the dosage amount, if tested on a person. Use the regression tree algorithm to
determine the effectiveness of the dosage amount. Consider the following training
dataset to develop the model and assess the effectiveness of a 19 mg dose.
Dosage of the   Effectiveness on person
Drug   (%)
1   0
5   5
8   14
Q4   12   20   [10]
18   98
21   95
23   97
28   35
30   25
35   20
Ans:
scatter plot [1 Marks]
finding regression tree [7 Marks]
Finding value of test sample [2 Marks]
********** 11 **********
--- page 12 ---

--- page 13 ---
b. Apply Logistic Regression on the following data set and devise the model for
classification using GD. Assume initially all the coefficients as 1 and update them
up to one iteration. Also show data distribution using scatter plot.
IQ of the student (x   Study time daily   Result
100) (X1)   (Hrs.) (X2)   (class)
1.3   0.5   Fail
1.1   1.5   Pass
0.9   1   Fail
0.9   2.5   Pass
[10]
Predict the result if IQ is 1.2 and Study time 0.6 hrs daily.
Ans:
Scatter Plot [2M]
Assuming coefficients and finding values [3M]
Use Gradient Descent in updating the coefficients [3M]
Testing [2M]
********** 13 **********
--- page 14 ---
a. Discuss the necessary steps of the “Complete Linkage” clustering (hierarchical)
algorithm with a suitable example. Show the dendrogram generated after the
Q5
clustering process.   [10]
Ans:
Steps of complete linkage algorithm [4 Marks]
********** 14 **********
--- page 15 ---
Example [4 marks]
Dendrogram [2 Marks]
Note: student can give another example also.
b. What is ensemble learning? Explain the bootstrap aggregation algorithm with its
advantages and a suitable example.
[10]
Ans:
Ensemble learning: [2 marks]
1. It helps improve machine learning results by combining several models.
2. This approach allows the production of better predictive performance
compared to a single model.
3. The basic idea is to learn a set of classifiers (experts) and to allow them to
vote.
4. Bagging and Boosting are two types of Ensemble Learning.
5. These two decrease the variance of a single estimate as they combine
several estimates from different models.   [10]
6. So the result may be a model with higher stability.
Bootstrap Aggregation (Bagging):
Bootstrap Aggregating, also known as bagging, is a machine learning ensemble
meta-algorithm designed to improve the stability and accuracy of machine learning
algorithms used in statistical classification and regression. It decreases
the variance and helps to avoid overfitting. It is usually applied to decision tree
methods.
Bagging is a special case of the model averaging approach.
Advantages – [2 Marks]
Algorithm and Example: [6 marks]
Suppose a set D of d tuples, at each iteration i, a training set Di of d tuples is
selected via row sampling with a replacement method (i.e., there can be repetitive
elements from different d tuples) from D (i.e., bootstrap). Then a classifier model
********** 15 **********
--- page 16 ---
Mi is learned for each training set D < i. Each classifier Mi returns its class
prediction. The bagged classifier M* counts the votes and assigns the class with
the most votes to X (unknown sample).
Implementation Steps of Bagging
 Step 1: Multiple subsets are created from the original data set with equal
tuples, selecting observations with replacement.
 Step 2: A base model is created on each of these subsets.
 Step 3: Each model is learned in parallel with each training set and
independent of each other.
 Step 4: The final predictions are determined by combining the predictions
from all the models.
a. Explain and apply the K-means clustering algorithm on the following dataset.
Perform at least one iteration and show the final clusters using a scatter plot,
where the value of K is 2.
Points X Y
P1   1   1
Q6   P2   1   2
P3   2   1   [10]
P4   4   3
P5   3   4
P6   5   5
Ans:
Scatter plot [1 Mark]
Explanation of K means algorithm with steps [3 Marks]
Solving the example and finding clusters [6 Marks]
********** 16 **********
--- page 17 ---
b. The result of the classification model is given below:
Total Test Sample: 10000, Correct positive classification: 4300, Correct negative
classification: 3800, Incorrect positive classification: 900 and Incorrect negative
classification: 1000, Evaluate the performance by calculate the following
performance parameters and also comment on result.
1. Confusion matrix   [10]
2. Accuracy, Precision, Recall
3. F1 – score
Ans:
1. Confusion matrix [2M]
2. Accuracy, Precision, Recall [4M]
********** 17 **********
--- page 18 ---
3. F1 – score [2M]
4. Comment on each result[2M]
Q7   Write a short note on the following
a   One-hot encoding on nominal features
Ans:
One Hot Encoding is a method for converting categorical variables into a binary
format. It creates new binary columns (0s and 1s) for each category in the original
variable. Each category in the original column is represented as a separate column, [10]
where a value of 1 indicates the presence of that category, and 0 indicates its
absence.
1. Eliminating Ordinality:
2. Improving Model Performance
********** 18 **********
--- page 19 ---
3. Compatibility with Algorithms
Explanation [5M]
Example [5M]: Student can give any relevant example, need to show complete
process in the example.
b ROC curve and AUC
Ans:
Explanation [7 Marks]
The ROC (Receiver Operating Characteristic) curve is a graphical
representation used to evaluate the performance of a binary classification model
across various thresholds. It plots the True Positive Rate (TPR) against the False
Positive Rate (FPR), providing insights into the trade-off between sensitivity and
specificity at different thresholds.
The AUC (Area Under the Curve) quantifies the overall ability of the model to
distinguish between positive and negative classes. A higher AUC indicates better
model performance, with values ranging from 0.5 (random guessing) to 1.0
(perfect classification).
Key Metrics for ROC and AUC
 True Positive Rate (TPR): Measures the proportion of actual positives
[10]
correctly identified (also called recall or sensitivity).
 False Positive Rate (FPR): Measures the proportion of actual negatives
incorrectly classified as positives.
 AUC: Represents the probability that a randomly chosen positive instance
is ranked higher than a randomly chosen negative instance.
Example [3 Marks]
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 46ff9d9c0b6e

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIDS_7056/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/MBA
Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q1
Answer briefly:   [20]
CO-1; a
Consider a real-world problem with limited labeled data. Examine how this
SO-1;   [5]
constraint affects supervised learning models and discuss five major limitations.
BL-2
Explanation of any 5 (each 1 mark)
Overfitting and Poor Generalization
High Cost of Data Annotation
Insufficient Representation of Data Variability
Class Imbalance and Bias
Inefficient Use of Unlabeled Data
High Variance and Model Instability
Poor Adaptability to Domain Shift
Difficulty in Model Evaluation
Noise Sensitivity
Inability to Discover Hidden Structures
b   Two datasets A and B each contain 5 values:
Dataset A: 48, 49, 50, 51, 52
CO-2;   Dataset B: 30, 40, 50, 60, 70
SO-1;   (i) Calculate the mean, median and variance for both datasets.   [5]
BL-2   (ii) Compare the dispersion of both datasets.
(iii) Based on the variance values, analyze which dataset is more likely to cause
overfitting in a machine learning model and justify your answer.
Dataset A (1 marks)
Mean = (48 + 49 + 50 + 51 + 52) / 5 = 250 / 5 = 50
Median = 50
Variance =2
Dataset B (1 mark)
********** 1 **********
--- page 2 ---
Mean = (30 + 40 + 50 + 60 + 70) / 5 = 250 / 5 = 50
Median = 50
Variance=200
Dispersion (1 mark)
Dataset A → Variance = 2 (Low dispersion)
Dataset B → Variance = 200 (High dispersion)
Dataset B is much more spread out
Overfit (2 marks)
Dataset A (Low Variance) - Data is closely clustered, model learns stable patterns
and more robust and reliable.
Dataset B (High Variance) - Data is widely spread, model may fit noise and learn
inconsistent patterns - higher risk of overfitting
c   A machine learning model is trained on a dataset and shows the following
behavior:
• Training error: very low
CO-3;
•   Test error: very high
SO-2;   [5]
(i). Identify whether the model is suffering from high bias or high variance.
BL-3
(ii). Suggest two methods to address this issue.
(iii). Explain how these methods help improve model performance in terms of the
bias–variance tradeoff.
i. The model is suffering from high variance (overfitting). (1 mark)
ii. Two methods to address this issue – (2 marks)
Apply Regularization (L1 or L2) and reduce model complexity
iii. Explanation using Bias–Variance Tradeoff – (2 marks)
• High variance means the model is too complex and fits noise in training
data.
• Regularization adds a penalty to large weights → simplifies the model →
reduces variance.
• Reducing model complexity prevents overfitting.
These methods: Decrease variance and slightly increase bias
Result in better generalization on test data
d   A classifier produces the following confusion matrix:
Predicted Positive   Predicted Negative
CO-4;
Actual Positive   80   20
SO-2;   [5]
Actual Negative   10   90
BL-3
(i) Calculate accuracy, precision, recall and F1-score.
(ii) Which metric is more important in medical diagnosis and why?
Performance (4 marks)
Accuracy= 𝑇𝑃+𝑇𝑁+𝐹𝑃+𝐹𝑁= 𝑇𝑃+𝑇𝑁   80+90 = 0.85
80+90+10+20
Precision= 𝑇𝑃+𝐹𝑃= 𝑇𝑃   80 = 0.89
80+10
Recall= 𝑇𝑃+𝐹𝑁= 𝑇𝑃   80 = 0.80
80+20
F1= 2𝑋(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑋𝑟𝑒𝑐𝑎𝑙𝑙) = 2𝑋0.712 = 0.84
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑟𝑒𝑐𝑎𝑙𝑙   1.69
Important metric in medical diagnosis (1 marks)
Recall measures how many actual positive cases are correctly identified
In medical diagnosis:
Positive = disease present
False Negative (FN) = Patient has disease but model says No. This is dangerous.
Q2   a
CO-2;   (i) Given dataset with 2 features, Category = A, B, C, A, C and Target = 10, 20,
[5]
SO-1;   30, 40, 50. Apply label encoding and one-hot encoding for category feature.
BL-2
********** 2 **********
--- page 3 ---
(ii) A dataset contains both ordinal and nominal categorical variables. Discuss how
you would choose between label encoding and one-hot encoding for each feature
and justify your decisions.
Label Encoding (1 mark)
A-0
B-1
C-2
One-hot encoding (1 mark)
A   B   C
A   1   0   0
B   0   1   0
C   0   0   1
Explanation (3 marks)
For ordinal variables (ordered data) - Low < Medium < High
Use: Label / ordinal encoding
Preserves   natural   order,   model   can   learn-   relative   ranking   and
increasing/decreasing trends
For nominal variables (Unordered Data) - Color: Red, Blue, Green and Category:
A, B, C
Use: One-Hot Encoding
No artificial order introduced, each category treated independently and avoids
misleading relationships
Q2   b
CO-5;   How do Bagging and Boosting differ in machine learning models? Discuss their
[5]
SO-2;   working mechanisms and identify appropriate use cases for each technique.
BL-3
Bagging (Bootstrap Aggregating) (2 marks):
Generates multiple training datasets using sampling with replacement (bootstrap).
Trains multiple models independently and in parallel.
Combines predictions using averaging (regression) and majority voting
(classification).
Reduces variance and prevents overfitting
Boosting (2 marks):
Models are trained sequentially.
Each new model focuses on errors made by previous models.
Misclassified data points are given higher importance (weights). Final prediction
is a weighted combination of all models.
Reduces bias and variance, improves overall accuracy
Use case (1 mark)
c   (i) A bank wants to classify loan applicants as Approved (A) or Rejected (R) based
on Income, Credit score and Employment status.
No.   Income Credit Employment   Class
1   High   Good   Employed   A
Q2   2   High   Good   Employed   A
CO-4;   3   High   Bad   Employed   A
[10]
SO-2;   4   Low   Good   Employed   A
BL-3   5   High   Good   Unemployed   A
6   Low   Bad   Unemployed   R
7   Low   Bad   Employed   R
8   Low   Good   Unemployed   R
9   High   Bad   Unemployed   R
********** 3 **********
--- page 4 ---
10   Low   Bad   Unemployed   R
11   High   Good   Employed   A
12   Low   Good   Employed   R
Classify a new applicant: X = (Income = High, Credit = Good, Employment =
Employed) using Naïve Bayes classifier.
(ii) Discuss the problem of zero probability in Naive Bayes classification. How
does it affect prediction? Explain Laplace smoothing with a suitable example.
P(A∣X) (3 marks)
P(A)=6/12=0.5, P(R)=6/12=0.5
P(High/A)=5/6
P(Good/A)=5/6
P(Employed/A)=5/6
P(A∣X) ∝ P(A)XP(High/A)X P(Good/A)X P(Employed/A)
∝ 0.289
P(R∣X) (3 marks)
P(High/R)=1/6
P(Good/A)=2/6=1/3
P(Employed/A)=2/6=1/3
P(R∣X) ∝ P(A)XP(High/R)X P(Good/R)X P(Employed/R)
∝ 0.0093
Final class (1 marks)
P(A∣X) > P(R∣X)
Class is Approved (A)
(ii)Explanation (2 marks)
If any one conditional probability becomes zero, then: P(Y∣X)=0. This is called
the zero-frequency problem. It occurs, when a particular feature value never
appears in the training data for a class.
Laplace smoothing: Add a small constant (usually +1) to all counts to avoid zero
probabilities.
Example (1 mark)
a   (i) Briefly explain the objective function used in simple linear regression with
gradient decent. Algorithm.
Q3   (ii) Using gradient decent for simple linear regression, determine loss function
CO-3;   after two iterations for the given a dataset. Consider Learning rate as 0.001 and [10]
SO-2;   initial weights/coefficients as zeros.
BL-3   x   1   2   3   4   5
y   3   5   7   8   10
In Simple Linear Regression (using gradient decent), the objective is to find the best-
fitting line: y = mx + b
The objective function used is the Mean Squared Error (MSE): (1 mark)
Explanation (1 mark)
•   It measures the average squared difference between actual values and predicted
values. m is total number of samples.
• The goal of gradient descent is to minimize this cost function.
• By iteratively updating slope and intercept, we find the line that gives the least
prediction error.
Equations (2 marks) and iteration – 1 (3 marks)
********** 4 **********
--- page 5 ---
Iteration – 2 (3 marks)
b   (i) Consider the following dataset with two class (+1) and (-1). Find the class for
sample (4,2) using Support Vector Machine. Consider A and D points are support
vectors.
Q3   ID   X1   X2   Y
CO-4;   A   2   3   +1
[10]
SO-2;   B   3   4   +1
BL-3   C   1   1   -1
D   2   2   -1
(ii) Describe the kernel trick in SVM and how it helps in solving non-linear
classification problems.
(i) Writing equations (2 marks)
2w1+2w2+b=−1
2w1+3w2+b=+1
Calculation of w1, w2 and b (4 marks)
Lagrangian formula
9a1+11a2=-1
11a1+14a2=+1
A1=-5, a2=4
w1=-2
w2=2
w=(−2,2),b=−1
class (2 marks)
y=−2x1+2x2−1
Substitute point (4,2) in y.
y=-5
********** 5 **********
--- page 6 ---
sign of y is -ve so the sample (4,2) belongs to -1 class
(ii) Explanation (2 marks)
A straight line (or hyperplane) cannot divide the data properly
Kernel Trick Works:
Data is implicitly mapped to a higher-dimensional space
In that space, data becomes linearly separable
SVM finds a linear hyperplane in this new space
The result corresponds to a non-linear boundary in original space
Q4   a   (i) How do histogram and box plot differ in representing data distribution
CO-2;   characteristics such as spread, skewness, and outliers?
[5]
SO-1;   (ii) Discuss the working of filter, wrapper, and embedded techniques in feature
BL-2   selection.
Histogram and box plot (2 marks)
Histograms provide detailed distribution patterns (visual detail) while box plots
summarize spread and outliers (statistical summary)
Aspect   Histogram   Box Plot
Data Representation   Detailed distribution   Summary statistics
Spread   Range across bins   IQR + whiskers
Skewness   Shape of distribution   Median   position   &
whiskers
Outliers   Harder to detect   Clearly identified
Feature selection method (3 marks)
Filter methods: Assess feature relevance independent of the model using statistical
measures.
Wrapper methods: Evaluate different feature subsets using performance of a
specific machine learning model
Embedded methods: Incorporate feature selection into the model training process.
b.   At a hostel pizza party, students are classified into two categories:
“Happy” and “Angry” based on pizza distribution. You collected the following
Q4   data:
CO-5;   Group   Happy   Angry
[5]
SO-2;   Group A (Got Extra Cheese)   8   2
BL-3   Group B (No Extra Cheese)   3   7
Calculate the Gini Index for Group A and Group B and compute the weighted Gini
Index after the split. Comment whether this split is good or not.
Step 1: Gini for Group A
Total = 8 + 2 = 10
8 2   2 2
𝐺𝑖𝑛𝑖(𝐴) = 1 −( 10) −( 10)
= 1 −(0.64 + 0.04) = 1 −0.68 = 0.32
Step 2: Gini for Group B
Total = 3 + 7 = 10
3 2   7 2
𝐺𝑖𝑛𝑖(𝐵) = 1 −( 10) −( 10)
= 1 −(0.09 + 0.49) = 1 −0.58 = 0.42
********** 6 **********
--- page 7 ---
Step 3: Weighted Gini
10   10
𝐺𝑖𝑛𝑖𝑠𝑝𝑙𝑖𝑡= 20(0.32) + 20(0.42)
= 0.5(0.32) + 0.5(0.42) = 0.16 + 0.21 = 0.37
Conclusion:
Lower Gini indicates better purity. Since 0.37 is relatively low, the split is
reasonably good.
c.   (i) A company wants to classify customers as either "High Spender (H/1)" or "Low
Spender (L/0)" based on their Age and Annual Income using K-NN. A new
customer (X) has Age = 32 and Income = 55. Classify this customer using K-NN
(K = 3).
Customer   Age   Income   Class
Q4
A   25   50   H
CO-4;
B   30   60   H   [10]
SO-2;
C   35   80   H
BL-3
D   40   40   L
E   45   50   L
(ii) You are given a binary classification setup with feature: 𝑥=2 and true label:
𝑦=1. Model parameters: weight 𝑤=0.5 and bias 𝑏=−0.5. Compute the predicted
probability and cross entropy loss (using logistic regression).
(i) 7 marks
Customer   Age   Income   Class   Distance2   Rank
A   25   50   H   74   2
B   30   60   H   29   1
C   35   80   H   634   5
D   40   40   L   289   4
E   45   50   L   194   3
Majority class – H
(ii) Predicted probability and loss (3 marks)
Predicted probability = 0.622
********** 7 **********
--- page 8 ---
a
(i) Justify the statement: “K-Means clustering is sensitive to outliers.”
(ii) Consider the following data with initial cluster centers are A(2,2),C(1,1)and
the number of clusters K=2,Use the k-means algorithm with Euclidean
distance ,what are the assignments until converge.
Q5
CO-4;   Object X1 X2   [10]
SO-2;
A   2   2
BL-3
B   3   2
C   1   1
D   3   1
E   1.5 0.5
(i) K-Means clustering is sensitive to outliers (2 marks)
because the algorithm uses the mean of data points to determine the cluster centers
(centroids). Since the mean is highly affected by extreme values, even a single
outlier can significantly shift the centroid, leading to incorrect clustering
(ii) First iteration-3 marks
Second iteration 3 marks
Final cluster (to stop iteration) -2 marks
Q5   b   Following table shows the number of item sale for a particular day. Find the
CO-3;   regression equation in the form Y = aX + b. Also predict a sale for day 8.
[10]
SO-2;   Day (X)   1   2   3   4   5   6   7
BL-3   Sales (Y)   9   8   10   12   11   13   14
********** 8 **********
--- page 9 ---
Table calculation – 2 marks
Calculation of coefficients – 4 marks
Equation of line – 2 marks
Prediction – 2 marks
X   Y   X²   Y²   XY
1   9   1   81   9
2   8   4   64   16
3   10   9   100   30
4   12   16   144   48
5   11   25   121   55
6   13   36   169   78
Sale for day 8 = 0.929*8+7.284 = 14.716 (15)
a   A group of students is deciding whether to order momos. The decision (Target:
Order = Yes/No) depends on:
• Weather (Sunny/Rainy)
• Mood (Happy/Grumpy)
Dataset:
Q6   Weather   Mood   Order
CO-5;
Sunny   Happy   Yes   [10]
SO-2;
Sunny   Grumpy   No
BL-3
Rainy   Happy   Yes
Rainy   Grumpy   Yes
Sunny   Happy   Yes
Calculate the Entropy of the dataset. Information Gain for Weather and Mood and
identify the root node using ID3. Explain briefly how ID3 builds the decision tree
********** 9 **********
--- page 10 ---
Entropy calculation – 2 marks
IG (Weather) – 2 marks
IG (Mood) – 2 marks
Correct root selection – 2 marks
ID3 explanation – 2 marks
Step 1: Entropy of Dataset
Total = 5
Yes = 4, No = 1
−(4   4 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) =   5 log⁡2 5 + 5 log⁡2 5)
= −(0.8 ⋅−0.32 + 0.2 ⋅−2.32) ≈0.72
Step 2: Information Gain
(A) Weather
• Sunny → (Yes=2, No=1)
−(2   2 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦=   3 log⁡2 3 + 3 log⁡2 3) ≈0.92
• Rainy → (Yes=2, No=0)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦= 0
Weighted Entropy:
3   2
= (0.92) + (0) = 0.552
5   5
𝐼𝐺(𝑊𝑒𝑎𝑡ℎ𝑒𝑟) = 0.72 −0.552 = 0.168
(B) Mood
• Happy → (Yes=3, No=0) → Entropy = 0
• Grumpy → (Yes=1, No=1) → Entropy = 1
Weighted Entropy:
3   2
= (0) + (1) = 0.4
5   5
𝐼𝐺(𝑀𝑜𝑜𝑑) = 0.72 −0.4 = 0.32
Step 3: Root Node
Since IG(Mood) > IG(Weather)
Root Node = Mood
Step 4: ID3 Explanation
• ID3 builds a decision tree top-down (greedy approach)
•   Selects attribute with highest Information Gain
•   Splits dataset recursively
• Stops when: All examples belong to one class
No attributes left
b   (i) Define Core Point, Border Point, and Noise Point in DBSCAN clustering.
(ii) Consider the following dataset Ɛ = 2, MinPts = 3 Using DBSCAN, determine:
Core Points, Border Points, Noise Points, Final clusters formed.
Q6   Point   X   Y
CO-4;   P1   1   1   [10]
SO-1;
P2   2   2
BL-3
P3   2   1
P4   8   8
P5   8   9
********** 10 **********
--- page 11 ---
P6   25   25
Definition – (2 marks)
Core Point: A core point is a point that has at least MinPts points (including
itself) within its ε-neighborhood.
Border Point: A border point is a point that has fewer than MinPts points in
its ε-neighborhood but lies within the ε-neighborhood of a core point.
Noise Point: A noise point is a point that is neither a core point nor
reachable from any core point, meaning it does not belong to any cluster.
Distance table (3 marks)
Distance is calculated using Euclidean distance:
P1   P2   P3   P4   P5   P6
P1   0   1.41   1   9.9   10.63   33.94
P2   1.41   0   1   8.49   9.22   32.53
P3   1   1   0   9.22   10   33.24
P4   9.9   8.49   9.22   0   1   24.76
P5   10.63   9.22   10   1   0   23.35
P6   33.94   32.53   33.24   24.76   23.35   0
ε–Neighborhoods (2 marks)
• P1: {P1, P2, P3} → 3 points
• P2: {P1, P2, P3} → 3 points
• P3: {P1, P2, P3} → 3 points
• P4: {P4, P5} → 2 points
• P5: {P4, P5} → 2 points
• P6: {P6} → 1 point
Core Points (1 mark)
Core point condition → points ≥ MinPts (3)
Core point P1, P2, P3
Border points: (1 mark)
have less than MinPts
but be within ε of a core point. P4 and P5 are not within ε of any core point.
Therefore they cannot be border points.
Noise Points (1 mark)
Points not reachable from any core point:
Noise Points: P4, P5, P6
Q7   a   A dataset shows highly non-linear patterns and large in size. Which model type
CO-1;   (parametric / non-parametric) is more suitable? Analyze (i) the trade-off between
[5]
SO-1;   bias and variance (ii) How does dataset size (from small to large) influence the
BL-2   choice between parametric and non-parametric models?
Model type (1 mark)
Non-parametric preferred for non-linear data.
Tradeoff (2 marks)
Parametric – Bias is high and variance is low
Non-parametric – Bias is low and variance is high
Dataset size (2 marks)
Small Dataset- Use parametric models (Require less data, less sensitive to noise
and lower variance), non-parametric models may overfits easily.
********** 11 **********
--- page 12 ---
Large Dataset – Use non-parametric models (Capture complex patterns, reduce
overfitting), Parametric models may underfit.
Q7   b   Describe the working of Random Forest as an ensemble technique. How does it
CO-5;   improve over a single Decision Tree?
[5]
SO-1;
BL-3
Random Forest is an ensemble learning method that constructs multiple decision
trees and combines their outputs to improve predictive performance. (3 Marks)
Working:
1. Draw multiple bootstrap samples from the dataset.
2. Train a decision tree on each sample.
3. At each split, consider a random subset of features instead of all features.
4. Aggregate predictions using:
o Majority voting (classification)
o Averaging (regression)
Improvement over Decision Tree: (2 Marks)
• A single decision tree is prone to overfitting.
• Random Forest:
o Reduces variance by averaging multiple trees
o Improves generalization
Handles noise better
c   (i) Differentiate between Agglomerative and Divisive hierarchical clustering.
(ii) Using the given dataset, perform Agglomerative Hierarchical Clustering with
Q7   Single Linkage. Compute Euclidean distances and draw the dendrogram.
CO-4;   Point   X   Y
SO-1;   A   1   1   [10]
BL-3   B   2   1
C   4   3
D   5   4
Difference - (2 marks)
Agglomerative Clustering   Divisive Clustering
Bottom-up approach   Top-down approach
Starts with each   Starts with all
observation as a separate   observations in one
cluster   single cluster
Clusters are merged step-   Clusters are split
by-step   step-by-step
n clusters (n = number of
1 cluster
data points)
Ends with one large   Ends with many
cluster   smaller clusters
We use Euclidean distance
The distance matrix after applying Euclidean distance (2 marks)
A   B   C   D
********** 12 **********
--- page 13 ---
A   0   1   3.61   5
B   1   0   2.83   4.24
C   3.61   2.83   0   1.41
D   5   4.24   1.41   0
First Merge (Smallest Distance)
Smallest distance = 1 (A,B)
Clusters now:
{AB}, {C}, {D} ---------(1 mark)
Update Distance (Single Link)------------(updating distance and table creation
-2 marks)
Single link = minimum distance between cluster members
Distance (AB , C)
min(d(A,C),d(B,C))
min(3.61,2.83)=2.83
Distance (AB , D) = min(5,4.24)=4.24
AB   C   D
AB   0   2.83   4.24
C   2.83   0   1.41
D   4.24   1.41   0
Second Merge
Smallest distance = 1.41 (C,D)
Cluster:
C2={C,D}
Clusters now:
{AB}, {CD}---------(1 mark)
Distance (AB , CD)=min(d(AB,C),d(AB,D))= min(2.83,4.24)=2.83---------
(update distance and table creation -1 mark)
AB   CD
AB   0   2.83
CD   2.83   0
Final cluster
{ABCD}
Final dendogram— (1 mark)
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper c6844ea54dc4

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIML_7053/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/MBA
Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q1
Answer briefly:   [20]
CO-1; a
Consider a real-world problem with limited labeled data. Examine how this
SO-1;   [5]
constraint affects supervised learning models and discuss five major limitations.
BL-2
Explanation of any 5 (each 1 mark)
Overfitting and Poor Generalization
High Cost of Data Annotation
Insufficient Representation of Data Variability
Class Imbalance and Bias
Inefficient Use of Unlabeled Data
High Variance and Model Instability
Poor Adaptability to Domain Shift
Difficulty in Model Evaluation
Noise Sensitivity
Inability to Discover Hidden Structures
b   Two datasets A and B each contain 5 values:
Dataset A: 48, 49, 50, 51, 52
CO-2;   Dataset B: 30, 40, 50, 60, 70
SO-1;   (i) Calculate the mean, median and variance for both datasets.   [5]
BL-2   (ii) Compare the dispersion of both datasets.
(iii) Based on the variance values, analyze which dataset is more likely to cause
overfitting in a machine learning model and justify your answer.
Dataset A (1 marks)
Mean = (48 + 49 + 50 + 51 + 52) / 5 = 250 / 5 = 50
Median = 50
Variance =2
Dataset B (1 mark)
********** 1 **********
--- page 2 ---
Mean = (30 + 40 + 50 + 60 + 70) / 5 = 250 / 5 = 50
Median = 50
Variance=200
Dispersion (1 mark)
Dataset A → Variance = 2 (Low dispersion)
Dataset B → Variance = 200 (High dispersion)
Dataset B is much more spread out
Overfit (2 marks)
Dataset A (Low Variance) - Data is closely clustered, model learns stable patterns
and more robust and reliable.
Dataset B (High Variance) - Data is widely spread, model may fit noise and learn
inconsistent patterns - higher risk of overfitting
c   A machine learning model is trained on a dataset and shows the following
behavior:
• Training error: very low
CO-3;
•   Test error: very high
SO-2;   [5]
(i). Identify whether the model is suffering from high bias or high variance.
BL-3
(ii). Suggest two methods to address this issue.
(iii). Explain how these methods help improve model performance in terms of the
bias–variance tradeoff.
i. The model is suffering from high variance (overfitting). (1 mark)
ii. Two methods to address this issue – (2 marks)
Apply Regularization (L1 or L2) and reduce model complexity
iii. Explanation using Bias–Variance Tradeoff – (2 marks)
• High variance means the model is too complex and fits noise in training
data.
• Regularization adds a penalty to large weights → simplifies the model →
reduces variance.
• Reducing model complexity prevents overfitting.
These methods: Decrease variance and slightly increase bias
Result in better generalization on test data
d   A classifier produces the following confusion matrix:
Predicted Positive   Predicted Negative
CO-4;
Actual Positive   80   20
SO-2;   [5]
Actual Negative   10   90
BL-3
(i) Calculate accuracy, precision, recall and F1-score.
(ii) Which metric is more important in medical diagnosis and why?
Performance (4 marks)
Accuracy= 𝑇𝑃+𝑇𝑁+𝐹𝑃+𝐹𝑁= 𝑇𝑃+𝑇𝑁   80+90 = 0.85
80+90+10+20
Precision= 𝑇𝑃+𝐹𝑃= 𝑇𝑃   80 = 0.89
80+10
Recall= 𝑇𝑃+𝐹𝑁= 𝑇𝑃   80 = 0.80
80+20
F1= 2𝑋(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑋𝑟𝑒𝑐𝑎𝑙𝑙) = 2𝑋0.712 = 0.84
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑟𝑒𝑐𝑎𝑙𝑙   1.69
Important metric in medical diagnosis (1 marks)
Recall measures how many actual positive cases are correctly identified
In medical diagnosis:
Positive = disease present
False Negative (FN) = Patient has disease but model says No. This is dangerous.
Q2   a
CO-2;   (i) Given dataset with 2 features, Category = A, B, C, A, C and Target = 10, 20,
[5]
SO-1;   30, 40, 50. Apply label encoding and one-hot encoding for category feature.
BL-2
********** 2 **********
--- page 3 ---
(ii) A dataset contains both ordinal and nominal categorical variables. Discuss how
you would choose between label encoding and one-hot encoding for each feature
and justify your decisions.
Label Encoding (1 mark)
A-0
B-1
C-2
One-hot encoding (1 mark)
A   B   C
A   1   0   0
B   0   1   0
C   0   0   1
Explanation (3 marks)
For ordinal variables (ordered data) - Low < Medium < High
Use: Label / ordinal encoding
Preserves   natural   order,   model   can   learn-   relative   ranking   and
increasing/decreasing trends
For nominal variables (Unordered Data) - Color: Red, Blue, Green and Category:
A, B, C
Use: One-Hot Encoding
No artificial order introduced, each category treated independently and avoids
misleading relationships
Q2   b
CO-5;   How do Bagging and Boosting differ in machine learning models? Discuss their
[5]
SO-2;   working mechanisms and identify appropriate use cases for each technique.
BL-3
Bagging (Bootstrap Aggregating) (2 marks):
Generates multiple training datasets using sampling with replacement (bootstrap).
Trains multiple models independently and in parallel.
Combines predictions using averaging (regression) and majority voting
(classification).
Reduces variance and prevents overfitting
Boosting (2 marks):
Models are trained sequentially.
Each new model focuses on errors made by previous models.
Misclassified data points are given higher importance (weights). Final prediction
is a weighted combination of all models.
Reduces bias and variance, improves overall accuracy
Use case (1 mark)
c   (i) A bank wants to classify loan applicants as Approved (A) or Rejected (R) based
on Income, Credit score and Employment status.
No.   Income Credit Employment   Class
1   High   Good   Employed   A
Q2   2   High   Good   Employed   A
CO-4;   3   High   Bad   Employed   A
[10]
SO-2;   4   Low   Good   Employed   A
BL-3   5   High   Good   Unemployed   A
6   Low   Bad   Unemployed   R
7   Low   Bad   Employed   R
8   Low   Good   Unemployed   R
9   High   Bad   Unemployed   R
********** 3 **********
--- page 4 ---
10   Low   Bad   Unemployed   R
11   High   Good   Employed   A
12   Low   Good   Employed   R
Classify a new applicant: X = (Income = High, Credit = Good, Employment =
Employed) using Naïve Bayes classifier.
(ii) Discuss the problem of zero probability in Naive Bayes classification. How
does it affect prediction? Explain Laplace smoothing with a suitable example.
P(A∣X) (3 marks)
P(A)=6/12=0.5, P(R)=6/12=0.5
P(High/A)=5/6
P(Good/A)=5/6
P(Employed/A)=5/6
P(A∣X) ∝ P(A)XP(High/A)X P(Good/A)X P(Employed/A)
∝ 0.289
P(R∣X) (3 marks)
P(High/R)=1/6
P(Good/A)=2/6=1/3
P(Employed/A)=2/6=1/3
P(R∣X) ∝ P(A)XP(High/R)X P(Good/R)X P(Employed/R)
∝ 0.0093
Final class (1 marks)
P(A∣X) > P(R∣X)
Class is Approved (A)
(ii)Explanation (2 marks)
If any one conditional probability becomes zero, then: P(Y∣X)=0. This is called
the zero-frequency problem. It occurs, when a particular feature value never
appears in the training data for a class.
Laplace smoothing: Add a small constant (usually +1) to all counts to avoid zero
probabilities.
Example (1 mark)
a   (i) Briefly explain the objective function used in simple linear regression with
gradient decent. Algorithm.
Q3   (ii) Using gradient decent for simple linear regression, determine loss function
CO-3;   after two iterations for the given a dataset. Consider Learning rate as 0.001 and [10]
SO-2;   initial weights/coefficients as zeros.
BL-3   x   1   2   3   4   5
y   3   5   7   8   10
In Simple Linear Regression (using gradient decent), the objective is to find the best-
fitting line: y = mx + b
The objective function used is the Mean Squared Error (MSE): (1 mark)
Explanation (1 mark)
•   It measures the average squared difference between actual values and predicted
values. m is total number of samples.
• The goal of gradient descent is to minimize this cost function.
• By iteratively updating slope and intercept, we find the line that gives the least
prediction error.
Equations (2 marks) and iteration – 1 (3 marks)
********** 4 **********
--- page 5 ---
Iteration – 2 (3 marks)
b   (i) Consider the following dataset with two class (+1) and (-1). Find the class for
sample (4,2) using Support Vector Machine. Consider A and D points are support
vectors.
Q3   ID   X1   X2   Y
CO-4;   A   2   3   +1
[10]
SO-2;   B   3   4   +1
BL-3   C   1   1   -1
D   2   2   -1
(ii) Describe the kernel trick in SVM and how it helps in solving non-linear
classification problems.
(i) Writing equations (2 marks)
2w1+2w2+b=−1
2w1+3w2+b=+1
Calculation of w1, w2 and b (4 marks)
Lagrangian formula
9a1+11a2=-1
11a1+14a2=+1
A1=-5, a2=4
w1=-2
w2=2
w=(−2,2),b=−1
class (2 marks)
y=−2x1+2x2−1
Substitute point (4,2) in y.
y=-5
********** 5 **********
--- page 6 ---
sign of y is -ve so the sample (4,2) belongs to -1 class
(ii) Explanation (2 marks)
A straight line (or hyperplane) cannot divide the data properly
Kernel Trick Works:
Data is implicitly mapped to a higher-dimensional space
In that space, data becomes linearly separable
SVM finds a linear hyperplane in this new space
The result corresponds to a non-linear boundary in original space
Q4   a   (i) How do histogram and box plot differ in representing data distribution
CO-2;   characteristics such as spread, skewness, and outliers?
[5]
SO-1;   (ii) Discuss the working of filter, wrapper, and embedded techniques in feature
BL-2   selection.
Histogram and box plot (2 marks)
Histograms provide detailed distribution patterns (visual detail) while box plots
summarize spread and outliers (statistical summary)
Aspect   Histogram   Box Plot
Data Representation   Detailed distribution   Summary statistics
Spread   Range across bins   IQR + whiskers
Skewness   Shape of distribution   Median   position   &
whiskers
Outliers   Harder to detect   Clearly identified
Feature selection method (3 marks)
Filter methods: Assess feature relevance independent of the model using statistical
measures.
Wrapper methods: Evaluate different feature subsets using performance of a
specific machine learning model
Embedded methods: Incorporate feature selection into the model training process.
b.   At a hostel pizza party, students are classified into two categories:
“Happy” and “Angry” based on pizza distribution. You collected the following
Q4   data:
CO-5;   Group   Happy   Angry
[5]
SO-2;   Group A (Got Extra Cheese)   8   2
BL-3   Group B (No Extra Cheese)   3   7
Calculate the Gini Index for Group A and Group B and compute the weighted Gini
Index after the split. Comment whether this split is good or not.
Step 1: Gini for Group A
Total = 8 + 2 = 10
8 2   2 2
𝐺𝑖𝑛𝑖(𝐴) = 1 −( 10) −( 10)
= 1 −(0.64 + 0.04) = 1 −0.68 = 0.32
Step 2: Gini for Group B
Total = 3 + 7 = 10
3 2   7 2
𝐺𝑖𝑛𝑖(𝐵) = 1 −( 10) −( 10)
= 1 −(0.09 + 0.49) = 1 −0.58 = 0.42
********** 6 **********
--- page 7 ---
Step 3: Weighted Gini
10   10
𝐺𝑖𝑛𝑖𝑠𝑝𝑙𝑖𝑡= 20(0.32) + 20(0.42)
= 0.5(0.32) + 0.5(0.42) = 0.16 + 0.21 = 0.37
Conclusion:
Lower Gini indicates better purity. Since 0.37 is relatively low, the split is
reasonably good.
c.   (i) A company wants to classify customers as either "High Spender (H/1)" or "Low
Spender (L/0)" based on their Age and Annual Income using K-NN. A new
customer (X) has Age = 32 and Income = 55. Classify this customer using K-NN
(K = 3).
Customer   Age   Income   Class
Q4
A   25   50   H
CO-4;
B   30   60   H   [10]
SO-2;
C   35   80   H
BL-3
D   40   40   L
E   45   50   L
(ii) You are given a binary classification setup with feature: 𝑥=2 and true label:
𝑦=1. Model parameters: weight 𝑤=0.5 and bias 𝑏=−0.5. Compute the predicted
probability and cross entropy loss (using logistic regression).
(i) 7 marks
Customer   Age   Income   Class   Distance2   Rank
A   25   50   H   74   2
B   30   60   H   29   1
C   35   80   H   634   5
D   40   40   L   289   4
E   45   50   L   194   3
Majority class – H
(ii) Predicted probability and loss (3 marks)
Predicted probability = 0.622
********** 7 **********
--- page 8 ---
a
(i) Justify the statement: “K-Means clustering is sensitive to outliers.”
(ii) Consider the following data with initial cluster centers are A(2,2),C(1,1)and
the number of clusters K=2,Use the k-means algorithm with Euclidean
distance ,what are the assignments until converge.
Q5
CO-4;   Object X1 X2   [10]
SO-2;
A   2   2
BL-3
B   3   2
C   1   1
D   3   1
E   1.5 0.5
(i) K-Means clustering is sensitive to outliers (2 marks)
because the algorithm uses the mean of data points to determine the cluster centers
(centroids). Since the mean is highly affected by extreme values, even a single
outlier can significantly shift the centroid, leading to incorrect clustering
(ii) First iteration-3 marks
Second iteration 3 marks
Final cluster (to stop iteration) -2 marks
Q5   b   Following table shows the number of item sale for a particular day. Find the
CO-3;   regression equation in the form Y = aX + b. Also predict a sale for day 8.
[10]
SO-2;   Day (X)   1   2   3   4   5   6   7
BL-3   Sales (Y)   9   8   10   12   11   13   14
********** 8 **********
--- page 9 ---
Table calculation – 2 marks
Calculation of coefficients – 4 marks
Equation of line – 2 marks
Prediction – 2 marks
X   Y   X²   Y²   XY
1   9   1   81   9
2   8   4   64   16
3   10   9   100   30
4   12   16   144   48
5   11   25   121   55
6   13   36   169   78
Sale for day 8 = 0.929*8+7.284 = 14.716 (15)
a   A group of students is deciding whether to order momos. The decision (Target:
Order = Yes/No) depends on:
• Weather (Sunny/Rainy)
• Mood (Happy/Grumpy)
Dataset:
Q6   Weather   Mood   Order
CO-5;
Sunny   Happy   Yes   [10]
SO-2;
Sunny   Grumpy   No
BL-3
Rainy   Happy   Yes
Rainy   Grumpy   Yes
Sunny   Happy   Yes
Calculate the Entropy of the dataset. Information Gain for Weather and Mood and
identify the root node using ID3. Explain briefly how ID3 builds the decision tree
********** 9 **********
--- page 10 ---
Entropy calculation – 2 marks
IG (Weather) – 2 marks
IG (Mood) – 2 marks
Correct root selection – 2 marks
ID3 explanation – 2 marks
Step 1: Entropy of Dataset
Total = 5
Yes = 4, No = 1
−(4   4 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) =   5 log⁡2 5 + 5 log⁡2 5)
= −(0.8 ⋅−0.32 + 0.2 ⋅−2.32) ≈0.72
Step 2: Information Gain
(A) Weather
• Sunny → (Yes=2, No=1)
−(2   2 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦=   3 log⁡2 3 + 3 log⁡2 3) ≈0.92
• Rainy → (Yes=2, No=0)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦= 0
Weighted Entropy:
3   2
= (0.92) + (0) = 0.552
5   5
𝐼𝐺(𝑊𝑒𝑎𝑡ℎ𝑒𝑟) = 0.72 −0.552 = 0.168
(B) Mood
• Happy → (Yes=3, No=0) → Entropy = 0
• Grumpy → (Yes=1, No=1) → Entropy = 1
Weighted Entropy:
3   2
= (0) + (1) = 0.4
5   5
𝐼𝐺(𝑀𝑜𝑜𝑑) = 0.72 −0.4 = 0.32
Step 3: Root Node
Since IG(Mood) > IG(Weather)
Root Node = Mood
Step 4: ID3 Explanation
• ID3 builds a decision tree top-down (greedy approach)
•   Selects attribute with highest Information Gain
•   Splits dataset recursively
• Stops when: All examples belong to one class
No attributes left
b   (i) Define Core Point, Border Point, and Noise Point in DBSCAN clustering.
(ii) Consider the following dataset Ɛ = 2, MinPts = 3 Using DBSCAN, determine:
Core Points, Border Points, Noise Points, Final clusters formed.
Q6   Point   X   Y
CO-4;   P1   1   1   [10]
SO-1;
P2   2   2
BL-3
P3   2   1
P4   8   8
P5   8   9
********** 10 **********
--- page 11 ---
P6   25   25
Definition – (2 marks)
Core Point: A core point is a point that has at least MinPts points (including
itself) within its ε-neighborhood.
Border Point: A border point is a point that has fewer than MinPts points in
its ε-neighborhood but lies within the ε-neighborhood of a core point.
Noise Point: A noise point is a point that is neither a core point nor
reachable from any core point, meaning it does not belong to any cluster.
Distance table (3 marks)
Distance is calculated using Euclidean distance:
P1   P2   P3   P4   P5   P6
P1   0   1.41   1   9.9   10.63   33.94
P2   1.41   0   1   8.49   9.22   32.53
P3   1   1   0   9.22   10   33.24
P4   9.9   8.49   9.22   0   1   24.76
P5   10.63   9.22   10   1   0   23.35
P6   33.94   32.53   33.24   24.76   23.35   0
ε–Neighborhoods (2 marks)
• P1: {P1, P2, P3} → 3 points
• P2: {P1, P2, P3} → 3 points
• P3: {P1, P2, P3} → 3 points
• P4: {P4, P5} → 2 points
• P5: {P4, P5} → 2 points
• P6: {P6} → 1 point
Core Points (1 mark)
Core point condition → points ≥ MinPts (3)
Core point P1, P2, P3
Border points: (1 mark)
have less than MinPts
but be within ε of a core point. P4 and P5 are not within ε of any core point.
Therefore they cannot be border points.
Noise Points (1 mark)
Points not reachable from any core point:
Noise Points: P4, P5, P6
Q7   a   A dataset shows highly non-linear patterns and large in size. Which model type
CO-1;   (parametric / non-parametric) is more suitable? Analyze (i) the trade-off between
[5]
SO-1;   bias and variance (ii) How does dataset size (from small to large) influence the
BL-2   choice between parametric and non-parametric models?
Model type (1 mark)
Non-parametric preferred for non-linear data.
Tradeoff (2 marks)
Parametric – Bias is high and variance is low
Non-parametric – Bias is low and variance is high
Dataset size (2 marks)
Small Dataset- Use parametric models (Require less data, less sensitive to noise
and lower variance), non-parametric models may overfits easily.
********** 11 **********
--- page 12 ---
Large Dataset – Use non-parametric models (Capture complex patterns, reduce
overfitting), Parametric models may underfit.
Q7   b   Describe the working of Random Forest as an ensemble technique. How does it
CO-5;   improve over a single Decision Tree?
[5]
SO-1;
BL-3
Random Forest is an ensemble learning method that constructs multiple decision
trees and combines their outputs to improve predictive performance. (3 Marks)
Working:
1. Draw multiple bootstrap samples from the dataset.
2. Train a decision tree on each sample.
3. At each split, consider a random subset of features instead of all features.
4. Aggregate predictions using:
o Majority voting (classification)
o Averaging (regression)
Improvement over Decision Tree: (2 Marks)
• A single decision tree is prone to overfitting.
• Random Forest:
o Reduces variance by averaging multiple trees
o Improves generalization
Handles noise better
c   (i) Differentiate between Agglomerative and Divisive hierarchical clustering.
(ii) Using the given dataset, perform Agglomerative Hierarchical Clustering with
Q7   Single Linkage. Compute Euclidean distances and draw the dendrogram.
CO-4;   Point   X   Y
SO-1;   A   1   1   [10]
BL-3   B   2   1
C   4   3
D   5   4
Difference - (2 marks)
Agglomerative Clustering   Divisive Clustering
Bottom-up approach   Top-down approach
Starts with each   Starts with all
observation as a separate   observations in one
cluster   single cluster
Clusters are merged step-   Clusters are split
by-step   step-by-step
n clusters (n = number of
1 cluster
data points)
Ends with one large   Ends with many
cluster   smaller clusters
We use Euclidean distance
The distance matrix after applying Euclidean distance (2 marks)
A   B   C   D
********** 12 **********
--- page 13 ---
A   0   1   3.61   5
B   1   0   2.83   4.24
C   3.61   2.83   0   1.41
D   5   4.24   1.41   0
First Merge (Smallest Distance)
Smallest distance = 1 (A,B)
Clusters now:
{AB}, {C}, {D} ---------(1 mark)
Update Distance (Single Link)------------(updating distance and table creation
-2 marks)
Single link = minimum distance between cluster members
Distance (AB , C)
min(d(A,C),d(B,C))
min(3.61,2.83)=2.83
Distance (AB , D) = min(5,4.24)=4.24
AB   C   D
AB   0   2.83   4.24
C   2.83   0   1.41
D   4.24   1.41   0
Second Merge
Smallest distance = 1.41 (C,D)
Cluster:
C2={C,D}
Clusters now:
{AB}, {CD}---------(1 mark)
Distance (AB , CD)=min(d(AB,C),d(AB,D))= min(2.83,4.24)=2.83---------
(update distance and table creation -1 mark)
AB   CD
AB   0   2.83
CD   2.83   0
Final cluster
{ABCD}
Final dendogram— (1 mark)
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 1c46bd79d0b4

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AI_7012/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/MBA
Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q1
Answer briefly:   [20]
CO-1; a
Consider a real-world problem with limited labeled data. Examine how this
SO-1;   [5]
constraint affects supervised learning models and discuss five major limitations.
BL-2
Explanation of any 5 (each 1 mark)
Overfitting and Poor Generalization
High Cost of Data Annotation
Insufficient Representation of Data Variability
Class Imbalance and Bias
Inefficient Use of Unlabeled Data
High Variance and Model Instability
Poor Adaptability to Domain Shift
Difficulty in Model Evaluation
Noise Sensitivity
Inability to Discover Hidden Structures
b   Two datasets A and B each contain 5 values:
Dataset A: 48, 49, 50, 51, 52
CO-2;   Dataset B: 30, 40, 50, 60, 70
SO-1;   (i) Calculate the mean, median and variance for both datasets.   [5]
BL-2   (ii) Compare the dispersion of both datasets.
(iii) Based on the variance values, analyze which dataset is more likely to cause
overfitting in a machine learning model and justify your answer.
Dataset A (1 marks)
Mean = (48 + 49 + 50 + 51 + 52) / 5 = 250 / 5 = 50
Median = 50
Variance =2
Dataset B (1 mark)
********** 1 **********
--- page 2 ---
Mean = (30 + 40 + 50 + 60 + 70) / 5 = 250 / 5 = 50
Median = 50
Variance=200
Dispersion (1 mark)
Dataset A → Variance = 2 (Low dispersion)
Dataset B → Variance = 200 (High dispersion)
Dataset B is much more spread out
Overfit (2 marks)
Dataset A (Low Variance) - Data is closely clustered, model learns stable patterns
and more robust and reliable.
Dataset B (High Variance) - Data is widely spread, model may fit noise and learn
inconsistent patterns - higher risk of overfitting
c   A machine learning model is trained on a dataset and shows the following
behavior:
• Training error: very low
CO-3;
•   Test error: very high
SO-2;   [5]
(i). Identify whether the model is suffering from high bias or high variance.
BL-3
(ii). Suggest two methods to address this issue.
(iii). Explain how these methods help improve model performance in terms of the
bias–variance tradeoff.
i. The model is suffering from high variance (overfitting). (1 mark)
ii. Two methods to address this issue – (2 marks)
Apply Regularization (L1 or L2) and reduce model complexity
iii. Explanation using Bias–Variance Tradeoff – (2 marks)
• High variance means the model is too complex and fits noise in training
data.
• Regularization adds a penalty to large weights → simplifies the model →
reduces variance.
• Reducing model complexity prevents overfitting.
These methods: Decrease variance and slightly increase bias
Result in better generalization on test data
d   A classifier produces the following confusion matrix:
Predicted Positive   Predicted Negative
CO-4;
Actual Positive   80   20
SO-2;   [5]
Actual Negative   10   90
BL-3
(i) Calculate accuracy, precision, recall and F1-score.
(ii) Which metric is more important in medical diagnosis and why?
Performance (4 marks)
Accuracy= 𝑇𝑃+𝑇𝑁+𝐹𝑃+𝐹𝑁= 𝑇𝑃+𝑇𝑁   80+90 = 0.85
80+90+10+20
Precision= 𝑇𝑃+𝐹𝑃= 𝑇𝑃   80 = 0.89
80+10
Recall= 𝑇𝑃+𝐹𝑁= 𝑇𝑃   80 = 0.80
80+20
F1= 2𝑋(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑋𝑟𝑒𝑐𝑎𝑙𝑙) = 2𝑋0.712 = 0.84
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑟𝑒𝑐𝑎𝑙𝑙   1.69
Important metric in medical diagnosis (1 marks)
Recall measures how many actual positive cases are correctly identified
In medical diagnosis:
Positive = disease present
False Negative (FN) = Patient has disease but model says No. This is dangerous.
Q2   a
CO-2;   (i) Given dataset with 2 features, Category = A, B, C, A, C and Target = 10, 20,
[5]
SO-1;   30, 40, 50. Apply label encoding and one-hot encoding for category feature.
BL-2
********** 2 **********
--- page 3 ---
(ii) A dataset contains both ordinal and nominal categorical variables. Discuss how
you would choose between label encoding and one-hot encoding for each feature
and justify your decisions.
Label Encoding (1 mark)
A-0
B-1
C-2
One-hot encoding (1 mark)
A   B   C
A   1   0   0
B   0   1   0
C   0   0   1
Explanation (3 marks)
For ordinal variables (ordered data) - Low < Medium < High
Use: Label / ordinal encoding
Preserves   natural   order,   model   can   learn-   relative   ranking   and
increasing/decreasing trends
For nominal variables (Unordered Data) - Color: Red, Blue, Green and Category:
A, B, C
Use: One-Hot Encoding
No artificial order introduced, each category treated independently and avoids
misleading relationships
Q2   b
CO-5;   How do Bagging and Boosting differ in machine learning models? Discuss their
[5]
SO-2;   working mechanisms and identify appropriate use cases for each technique.
BL-3
Bagging (Bootstrap Aggregating) (2 marks):
Generates multiple training datasets using sampling with replacement (bootstrap).
Trains multiple models independently and in parallel.
Combines predictions using averaging (regression) and majority voting
(classification).
Reduces variance and prevents overfitting
Boosting (2 marks):
Models are trained sequentially.
Each new model focuses on errors made by previous models.
Misclassified data points are given higher importance (weights). Final prediction
is a weighted combination of all models.
Reduces bias and variance, improves overall accuracy
Use case (1 mark)
c   (i) A bank wants to classify loan applicants as Approved (A) or Rejected (R) based
on Income, Credit score and Employment status.
No.   Income Credit Employment   Class
1   High   Good   Employed   A
Q2   2   High   Good   Employed   A
CO-4;   3   High   Bad   Employed   A
[10]
SO-2;   4   Low   Good   Employed   A
BL-3   5   High   Good   Unemployed   A
6   Low   Bad   Unemployed   R
7   Low   Bad   Employed   R
8   Low   Good   Unemployed   R
9   High   Bad   Unemployed   R
********** 3 **********
--- page 4 ---
10   Low   Bad   Unemployed   R
11   High   Good   Employed   A
12   Low   Good   Employed   R
Classify a new applicant: X = (Income = High, Credit = Good, Employment =
Employed) using Naïve Bayes classifier.
(ii) Discuss the problem of zero probability in Naive Bayes classification. How
does it affect prediction? Explain Laplace smoothing with a suitable example.
P(A∣X) (3 marks)
P(A)=6/12=0.5, P(R)=6/12=0.5
P(High/A)=5/6
P(Good/A)=5/6
P(Employed/A)=5/6
P(A∣X) ∝ P(A)XP(High/A)X P(Good/A)X P(Employed/A)
∝ 0.289
P(R∣X) (3 marks)
P(High/R)=1/6
P(Good/A)=2/6=1/3
P(Employed/A)=2/6=1/3
P(R∣X) ∝ P(A)XP(High/R)X P(Good/R)X P(Employed/R)
∝ 0.0093
Final class (1 marks)
P(A∣X) > P(R∣X)
Class is Approved (A)
(ii)Explanation (2 marks)
If any one conditional probability becomes zero, then: P(Y∣X)=0. This is called
the zero-frequency problem. It occurs, when a particular feature value never
appears in the training data for a class.
Laplace smoothing: Add a small constant (usually +1) to all counts to avoid zero
probabilities.
Example (1 mark)
a   (i) Briefly explain the objective function used in simple linear regression with
gradient decent. Algorithm.
Q3   (ii) Using gradient decent for simple linear regression, determine loss function
CO-3;   after two iterations for the given a dataset. Consider Learning rate as 0.001 and [10]
SO-2;   initial weights/coefficients as zeros.
BL-3   x   1   2   3   4   5
y   3   5   7   8   10
In Simple Linear Regression (using gradient decent), the objective is to find the best-
fitting line: y = mx + b
The objective function used is the Mean Squared Error (MSE): (1 mark)
Explanation (1 mark)
•   It measures the average squared difference between actual values and predicted
values. m is total number of samples.
• The goal of gradient descent is to minimize this cost function.
• By iteratively updating slope and intercept, we find the line that gives the least
prediction error.
Equations (2 marks) and iteration – 1 (3 marks)
********** 4 **********
--- page 5 ---
Iteration – 2 (3 marks)
b   (i) Consider the following dataset with two class (+1) and (-1). Find the class for
sample (4,2) using Support Vector Machine. Consider A and D points are support
vectors.
Q3   ID   X1   X2   Y
CO-4;   A   2   3   +1
[10]
SO-2;   B   3   4   +1
BL-3   C   1   1   -1
D   2   2   -1
(ii) Describe the kernel trick in SVM and how it helps in solving non-linear
classification problems.
(i) Writing equations (2 marks)
2w1+2w2+b=−1
2w1+3w2+b=+1
Calculation of w1, w2 and b (4 marks)
Lagrangian formula
9a1+11a2=-1
11a1+14a2=+1
A1=-5, a2=4
w1=-2
w2=2
w=(−2,2),b=−1
class (2 marks)
y=−2x1+2x2−1
Substitute point (4,2) in y.
y=-5
********** 5 **********
--- page 6 ---
sign of y is -ve so the sample (4,2) belongs to -1 class
(ii) Explanation (2 marks)
A straight line (or hyperplane) cannot divide the data properly
Kernel Trick Works:
Data is implicitly mapped to a higher-dimensional space
In that space, data becomes linearly separable
SVM finds a linear hyperplane in this new space
The result corresponds to a non-linear boundary in original space
Q4   a   (i) How do histogram and box plot differ in representing data distribution
CO-2;   characteristics such as spread, skewness, and outliers?
[5]
SO-1;   (ii) Discuss the working of filter, wrapper, and embedded techniques in feature
BL-2   selection.
Histogram and box plot (2 marks)
Histograms provide detailed distribution patterns (visual detail) while box plots
summarize spread and outliers (statistical summary)
Aspect   Histogram   Box Plot
Data Representation   Detailed distribution   Summary statistics
Spread   Range across bins   IQR + whiskers
Skewness   Shape of distribution   Median   position   &
whiskers
Outliers   Harder to detect   Clearly identified
Feature selection method (3 marks)
Filter methods: Assess feature relevance independent of the model using statistical
measures.
Wrapper methods: Evaluate different feature subsets using performance of a
specific machine learning model
Embedded methods: Incorporate feature selection into the model training process.
b.   At a hostel pizza party, students are classified into two categories:
“Happy” and “Angry” based on pizza distribution. You collected the following
Q4   data:
CO-5;   Group   Happy   Angry
[5]
SO-2;   Group A (Got Extra Cheese)   8   2
BL-3   Group B (No Extra Cheese)   3   7
Calculate the Gini Index for Group A and Group B and compute the weighted Gini
Index after the split. Comment whether this split is good or not.
Step 1: Gini for Group A
Total = 8 + 2 = 10
8 2   2 2
𝐺𝑖𝑛𝑖(𝐴) = 1 −( 10) −( 10)
= 1 −(0.64 + 0.04) = 1 −0.68 = 0.32
Step 2: Gini for Group B
Total = 3 + 7 = 10
3 2   7 2
𝐺𝑖𝑛𝑖(𝐵) = 1 −( 10) −( 10)
= 1 −(0.09 + 0.49) = 1 −0.58 = 0.42
********** 6 **********
--- page 7 ---
Step 3: Weighted Gini
10   10
𝐺𝑖𝑛𝑖𝑠𝑝𝑙𝑖𝑡= 20(0.32) + 20(0.42)
= 0.5(0.32) + 0.5(0.42) = 0.16 + 0.21 = 0.37
Conclusion:
Lower Gini indicates better purity. Since 0.37 is relatively low, the split is
reasonably good.
c.   (i) A company wants to classify customers as either "High Spender (H/1)" or "Low
Spender (L/0)" based on their Age and Annual Income using K-NN. A new
customer (X) has Age = 32 and Income = 55. Classify this customer using K-NN
(K = 3).
Customer   Age   Income   Class
Q4
A   25   50   H
CO-4;
B   30   60   H   [10]
SO-2;
C   35   80   H
BL-3
D   40   40   L
E   45   50   L
(ii) You are given a binary classification setup with feature: 𝑥=2 and true label:
𝑦=1. Model parameters: weight 𝑤=0.5 and bias 𝑏=−0.5. Compute the predicted
probability and cross entropy loss (using logistic regression).
(i) 7 marks
Customer   Age   Income   Class   Distance2   Rank
A   25   50   H   74   2
B   30   60   H   29   1
C   35   80   H   634   5
D   40   40   L   289   4
E   45   50   L   194   3
Majority class – H
(ii) Predicted probability and loss (3 marks)
Predicted probability = 0.622
********** 7 **********
--- page 8 ---
a
(i) Justify the statement: “K-Means clustering is sensitive to outliers.”
(ii) Consider the following data with initial cluster centers are A(2,2),C(1,1)and
the number of clusters K=2,Use the k-means algorithm with Euclidean
distance ,what are the assignments until converge.
Q5
CO-4;   Object X1 X2   [10]
SO-2;
A   2   2
BL-3
B   3   2
C   1   1
D   3   1
E   1.5 0.5
(i) K-Means clustering is sensitive to outliers (2 marks)
because the algorithm uses the mean of data points to determine the cluster centers
(centroids). Since the mean is highly affected by extreme values, even a single
outlier can significantly shift the centroid, leading to incorrect clustering
(ii) First iteration-3 marks
Second iteration 3 marks
Final cluster (to stop iteration) -2 marks
Q5   b   Following table shows the number of item sale for a particular day. Find the
CO-3;   regression equation in the form Y = aX + b. Also predict a sale for day 8.
[10]
SO-2;   Day (X)   1   2   3   4   5   6   7
BL-3   Sales (Y)   9   8   10   12   11   13   14
********** 8 **********
--- page 9 ---
Table calculation – 2 marks
Calculation of coefficients – 4 marks
Equation of line – 2 marks
Prediction – 2 marks
X   Y   X²   Y²   XY
1   9   1   81   9
2   8   4   64   16
3   10   9   100   30
4   12   16   144   48
5   11   25   121   55
6   13   36   169   78
Sale for day 8 = 0.929*8+7.284 = 14.716 (15)
a   A group of students is deciding whether to order momos. The decision (Target:
Order = Yes/No) depends on:
• Weather (Sunny/Rainy)
• Mood (Happy/Grumpy)
Dataset:
Q6   Weather   Mood   Order
CO-5;
Sunny   Happy   Yes   [10]
SO-2;
Sunny   Grumpy   No
BL-3
Rainy   Happy   Yes
Rainy   Grumpy   Yes
Sunny   Happy   Yes
Calculate the Entropy of the dataset. Information Gain for Weather and Mood and
identify the root node using ID3. Explain briefly how ID3 builds the decision tree
********** 9 **********
--- page 10 ---
Entropy calculation – 2 marks
IG (Weather) – 2 marks
IG (Mood) – 2 marks
Correct root selection – 2 marks
ID3 explanation – 2 marks
Step 1: Entropy of Dataset
Total = 5
Yes = 4, No = 1
−(4   4 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) =   5 log⁡2 5 + 5 log⁡2 5)
= −(0.8 ⋅−0.32 + 0.2 ⋅−2.32) ≈0.72
Step 2: Information Gain
(A) Weather
• Sunny → (Yes=2, No=1)
−(2   2 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦=   3 log⁡2 3 + 3 log⁡2 3) ≈0.92
• Rainy → (Yes=2, No=0)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦= 0
Weighted Entropy:
3   2
= (0.92) + (0) = 0.552
5   5
𝐼𝐺(𝑊𝑒𝑎𝑡ℎ𝑒𝑟) = 0.72 −0.552 = 0.168
(B) Mood
• Happy → (Yes=3, No=0) → Entropy = 0
• Grumpy → (Yes=1, No=1) → Entropy = 1
Weighted Entropy:
3   2
= (0) + (1) = 0.4
5   5
𝐼𝐺(𝑀𝑜𝑜𝑑) = 0.72 −0.4 = 0.32
Step 3: Root Node
Since IG(Mood) > IG(Weather)
Root Node = Mood
Step 4: ID3 Explanation
• ID3 builds a decision tree top-down (greedy approach)
•   Selects attribute with highest Information Gain
•   Splits dataset recursively
• Stops when: All examples belong to one class
No attributes left
b   (i) Define Core Point, Border Point, and Noise Point in DBSCAN clustering.
(ii) Consider the following dataset Ɛ = 2, MinPts = 3 Using DBSCAN, determine:
Core Points, Border Points, Noise Points, Final clusters formed.
Q6   Point   X   Y
CO-4;   P1   1   1   [10]
SO-1;
P2   2   2
BL-3
P3   2   1
P4   8   8
P5   8   9
********** 10 **********
--- page 11 ---
P6   25   25
Definition – (2 marks)
Core Point: A core point is a point that has at least MinPts points (including
itself) within its ε-neighborhood.
Border Point: A border point is a point that has fewer than MinPts points in
its ε-neighborhood but lies within the ε-neighborhood of a core point.
Noise Point: A noise point is a point that is neither a core point nor
reachable from any core point, meaning it does not belong to any cluster.
Distance table (3 marks)
Distance is calculated using Euclidean distance:
P1   P2   P3   P4   P5   P6
P1   0   1.41   1   9.9   10.63   33.94
P2   1.41   0   1   8.49   9.22   32.53
P3   1   1   0   9.22   10   33.24
P4   9.9   8.49   9.22   0   1   24.76
P5   10.63   9.22   10   1   0   23.35
P6   33.94   32.53   33.24   24.76   23.35   0
ε–Neighborhoods (2 marks)
• P1: {P1, P2, P3} → 3 points
• P2: {P1, P2, P3} → 3 points
• P3: {P1, P2, P3} → 3 points
• P4: {P4, P5} → 2 points
• P5: {P4, P5} → 2 points
• P6: {P6} → 1 point
Core Points (1 mark)
Core point condition → points ≥ MinPts (3)
Core point P1, P2, P3
Border points: (1 mark)
have less than MinPts
but be within ε of a core point. P4 and P5 are not within ε of any core point.
Therefore they cannot be border points.
Noise Points (1 mark)
Points not reachable from any core point:
Noise Points: P4, P5, P6
Q7   a   A dataset shows highly non-linear patterns and large in size. Which model type
CO-1;   (parametric / non-parametric) is more suitable? Analyze (i) the trade-off between
[5]
SO-1;   bias and variance (ii) How does dataset size (from small to large) influence the
BL-2   choice between parametric and non-parametric models?
Model type (1 mark)
Non-parametric preferred for non-linear data.
Tradeoff (2 marks)
Parametric – Bias is high and variance is low
Non-parametric – Bias is low and variance is high
Dataset size (2 marks)
Small Dataset- Use parametric models (Require less data, less sensitive to noise
and lower variance), non-parametric models may overfits easily.
********** 11 **********
--- page 12 ---
Large Dataset – Use non-parametric models (Capture complex patterns, reduce
overfitting), Parametric models may underfit.
Q7   b   Describe the working of Random Forest as an ensemble technique. How does it
CO-5;   improve over a single Decision Tree?
[5]
SO-1;
BL-3
Random Forest is an ensemble learning method that constructs multiple decision
trees and combines their outputs to improve predictive performance. (3 Marks)
Working:
1. Draw multiple bootstrap samples from the dataset.
2. Train a decision tree on each sample.
3. At each split, consider a random subset of features instead of all features.
4. Aggregate predictions using:
o Majority voting (classification)
o Averaging (regression)
Improvement over Decision Tree: (2 Marks)
• A single decision tree is prone to overfitting.
• Random Forest:
o Reduces variance by averaging multiple trees
o Improves generalization
Handles noise better
c   (i) Differentiate between Agglomerative and Divisive hierarchical clustering.
(ii) Using the given dataset, perform Agglomerative Hierarchical Clustering with
Q7   Single Linkage. Compute Euclidean distances and draw the dendrogram.
CO-4;   Point   X   Y
SO-1;   A   1   1   [10]
BL-3   B   2   1
C   4   3
D   5   4
Difference - (2 marks)
Agglomerative Clustering   Divisive Clustering
Bottom-up approach   Top-down approach
Starts with each   Starts with all
observation as a separate   observations in one
cluster   single cluster
Clusters are merged step-   Clusters are split
by-step   step-by-step
n clusters (n = number of
1 cluster
data points)
Ends with one large   Ends with many
cluster   smaller clusters
We use Euclidean distance
The distance matrix after applying Euclidean distance (2 marks)
A   B   C   D
********** 12 **********
--- page 13 ---
A   0   1   3.61   5
B   1   0   2.83   4.24
C   3.61   2.83   0   1.41
D   5   4.24   1.41   0
First Merge (Smallest Distance)
Smallest distance = 1 (A,B)
Clusters now:
{AB}, {C}, {D} ---------(1 mark)
Update Distance (Single Link)------------(updating distance and table creation
-2 marks)
Single link = minimum distance between cluster members
Distance (AB , C)
min(d(A,C),d(B,C))
min(3.61,2.83)=2.83
Distance (AB , D) = min(5,4.24)=4.24
AB   C   D
AB   0   2.83   4.24
C   2.83   0   1.41
D   4.24   1.41   0
Second Merge
Smallest distance = 1.41 (C,D)
Cluster:
C2={C,D}
Clusters now:
{AB}, {CD}---------(1 mark)
Distance (AB , CD)=min(d(AB,C),d(AB,D))= min(2.83,4.24)=2.83---------
(update distance and table creation -1 mark)
AB   CD
AB   0   2.83
CD   2.83   0
Final cluster
{ABCD}
Final dendogram— (1 mark)
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper fa56630fcb96

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSE_DS_7057/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/MBA
Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q1
Answer briefly:   [20]
CO-1; a
Consider a real-world problem with limited labeled data. Examine how this
SO-1;   [5]
constraint affects supervised learning models and discuss five major limitations.
BL-2
Explanation of any 5 (each 1 mark)
Overfitting and Poor Generalization
High Cost of Data Annotation
Insufficient Representation of Data Variability
Class Imbalance and Bias
Inefficient Use of Unlabeled Data
High Variance and Model Instability
Poor Adaptability to Domain Shift
Difficulty in Model Evaluation
Noise Sensitivity
Inability to Discover Hidden Structures
b   Two datasets A and B each contain 5 values:
Dataset A: 48, 49, 50, 51, 52
CO-2;   Dataset B: 30, 40, 50, 60, 70
SO-1;   (i) Calculate the mean, median and variance for both datasets.   [5]
BL-2   (ii) Compare the dispersion of both datasets.
(iii) Based on the variance values, analyze which dataset is more likely to cause
overfitting in a machine learning model and justify your answer.
Dataset A (1 marks)
Mean = (48 + 49 + 50 + 51 + 52) / 5 = 250 / 5 = 50
Median = 50
Variance =2
Dataset B (1 mark)
********** 1 **********
--- page 2 ---
Mean = (30 + 40 + 50 + 60 + 70) / 5 = 250 / 5 = 50
Median = 50
Variance=200
Dispersion (1 mark)
Dataset A → Variance = 2 (Low dispersion)
Dataset B → Variance = 200 (High dispersion)
Dataset B is much more spread out
Overfit (2 marks)
Dataset A (Low Variance) - Data is closely clustered, model learns stable patterns
and more robust and reliable.
Dataset B (High Variance) - Data is widely spread, model may fit noise and learn
inconsistent patterns - higher risk of overfitting
c   A machine learning model is trained on a dataset and shows the following
behavior:
• Training error: very low
CO-3;
•   Test error: very high
SO-2;   [5]
(i). Identify whether the model is suffering from high bias or high variance.
BL-3
(ii). Suggest two methods to address this issue.
(iii). Explain how these methods help improve model performance in terms of the
bias–variance tradeoff.
i. The model is suffering from high variance (overfitting). (1 mark)
ii. Two methods to address this issue – (2 marks)
Apply Regularization (L1 or L2) and reduce model complexity
iii. Explanation using Bias–Variance Tradeoff – (2 marks)
• High variance means the model is too complex and fits noise in training
data.
• Regularization adds a penalty to large weights → simplifies the model →
reduces variance.
• Reducing model complexity prevents overfitting.
These methods: Decrease variance and slightly increase bias
Result in better generalization on test data
d   A classifier produces the following confusion matrix:
Predicted Positive   Predicted Negative
CO-4;
Actual Positive   80   20
SO-2;   [5]
Actual Negative   10   90
BL-3
(i) Calculate accuracy, precision, recall and F1-score.
(ii) Which metric is more important in medical diagnosis and why?
Performance (4 marks)
Accuracy= 𝑇𝑃+𝑇𝑁+𝐹𝑃+𝐹𝑁= 𝑇𝑃+𝑇𝑁   80+90 = 0.85
80+90+10+20
Precision= 𝑇𝑃+𝐹𝑃= 𝑇𝑃   80 = 0.89
80+10
Recall= 𝑇𝑃+𝐹𝑁= 𝑇𝑃   80 = 0.80
80+20
F1= 2𝑋(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑋𝑟𝑒𝑐𝑎𝑙𝑙) = 2𝑋0.712 = 0.84
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑟𝑒𝑐𝑎𝑙𝑙   1.69
Important metric in medical diagnosis (1 marks)
Recall measures how many actual positive cases are correctly identified
In medical diagnosis:
Positive = disease present
False Negative (FN) = Patient has disease but model says No. This is dangerous.
Q2   a
CO-2;   (i) Given dataset with 2 features, Category = A, B, C, A, C and Target = 10, 20,
[5]
SO-1;   30, 40, 50. Apply label encoding and one-hot encoding for category feature.
BL-2
********** 2 **********
--- page 3 ---
(ii) A dataset contains both ordinal and nominal categorical variables. Discuss how
you would choose between label encoding and one-hot encoding for each feature
and justify your decisions.
Label Encoding (1 mark)
A-0
B-1
C-2
One-hot encoding (1 mark)
A   B   C
A   1   0   0
B   0   1   0
C   0   0   1
Explanation (3 marks)
For ordinal variables (ordered data) - Low < Medium < High
Use: Label / ordinal encoding
Preserves   natural   order,   model   can   learn-   relative   ranking   and
increasing/decreasing trends
For nominal variables (Unordered Data) - Color: Red, Blue, Green and Category:
A, B, C
Use: One-Hot Encoding
No artificial order introduced, each category treated independently and avoids
misleading relationships
Q2   b
CO-5;   How do Bagging and Boosting differ in machine learning models? Discuss their
[5]
SO-2;   working mechanisms and identify appropriate use cases for each technique.
BL-3
Bagging (Bootstrap Aggregating) (2 marks):
Generates multiple training datasets using sampling with replacement (bootstrap).
Trains multiple models independently and in parallel.
Combines predictions using averaging (regression) and majority voting
(classification).
Reduces variance and prevents overfitting
Boosting (2 marks):
Models are trained sequentially.
Each new model focuses on errors made by previous models.
Misclassified data points are given higher importance (weights). Final prediction
is a weighted combination of all models.
Reduces bias and variance, improves overall accuracy
Use case (1 mark)
c   (i) A bank wants to classify loan applicants as Approved (A) or Rejected (R) based
on Income, Credit score and Employment status.
No.   Income Credit Employment   Class
1   High   Good   Employed   A
Q2   2   High   Good   Employed   A
CO-4;   3   High   Bad   Employed   A
[10]
SO-2;   4   Low   Good   Employed   A
BL-3   5   High   Good   Unemployed   A
6   Low   Bad   Unemployed   R
7   Low   Bad   Employed   R
8   Low   Good   Unemployed   R
9   High   Bad   Unemployed   R
********** 3 **********
--- page 4 ---
10   Low   Bad   Unemployed   R
11   High   Good   Employed   A
12   Low   Good   Employed   R
Classify a new applicant: X = (Income = High, Credit = Good, Employment =
Employed) using Naïve Bayes classifier.
(ii) Discuss the problem of zero probability in Naive Bayes classification. How
does it affect prediction? Explain Laplace smoothing with a suitable example.
P(A∣X) (3 marks)
P(A)=6/12=0.5, P(R)=6/12=0.5
P(High/A)=5/6
P(Good/A)=5/6
P(Employed/A)=5/6
P(A∣X) ∝ P(A)XP(High/A)X P(Good/A)X P(Employed/A)
∝ 0.289
P(R∣X) (3 marks)
P(High/R)=1/6
P(Good/A)=2/6=1/3
P(Employed/A)=2/6=1/3
P(R∣X) ∝ P(A)XP(High/R)X P(Good/R)X P(Employed/R)
∝ 0.0093
Final class (1 marks)
P(A∣X) > P(R∣X)
Class is Approved (A)
(ii)Explanation (2 marks)
If any one conditional probability becomes zero, then: P(Y∣X)=0. This is called
the zero-frequency problem. It occurs, when a particular feature value never
appears in the training data for a class.
Laplace smoothing: Add a small constant (usually +1) to all counts to avoid zero
probabilities.
Example (1 mark)
a   (i) Briefly explain the objective function used in simple linear regression with
gradient decent. Algorithm.
Q3   (ii) Using gradient decent for simple linear regression, determine loss function
CO-3;   after two iterations for the given a dataset. Consider Learning rate as 0.001 and [10]
SO-2;   initial weights/coefficients as zeros.
BL-3   x   1   2   3   4   5
y   3   5   7   8   10
In Simple Linear Regression (using gradient decent), the objective is to find the best-
fitting line: y = mx + b
The objective function used is the Mean Squared Error (MSE): (1 mark)
Explanation (1 mark)
•   It measures the average squared difference between actual values and predicted
values. m is total number of samples.
• The goal of gradient descent is to minimize this cost function.
• By iteratively updating slope and intercept, we find the line that gives the least
prediction error.
Equations (2 marks) and iteration – 1 (3 marks)
********** 4 **********
--- page 5 ---
Iteration – 2 (3 marks)
b   (i) Consider the following dataset with two class (+1) and (-1). Find the class for
sample (4,2) using Support Vector Machine. Consider A and D points are support
vectors.
Q3   ID   X1   X2   Y
CO-4;   A   2   3   +1
[10]
SO-2;   B   3   4   +1
BL-3   C   1   1   -1
D   2   2   -1
(ii) Describe the kernel trick in SVM and how it helps in solving non-linear
classification problems.
(i) Writing equations (2 marks)
2w1+2w2+b=−1
2w1+3w2+b=+1
Calculation of w1, w2 and b (4 marks)
Lagrangian formula
9a1+11a2=-1
11a1+14a2=+1
A1=-5, a2=4
w1=-2
w2=2
w=(−2,2),b=−1
class (2 marks)
y=−2x1+2x2−1
Substitute point (4,2) in y.
y=-5
********** 5 **********
--- page 6 ---
sign of y is -ve so the sample (4,2) belongs to -1 class
(ii) Explanation (2 marks)
A straight line (or hyperplane) cannot divide the data properly
Kernel Trick Works:
Data is implicitly mapped to a higher-dimensional space
In that space, data becomes linearly separable
SVM finds a linear hyperplane in this new space
The result corresponds to a non-linear boundary in original space
Q4   a   (i) How do histogram and box plot differ in representing data distribution
CO-2;   characteristics such as spread, skewness, and outliers?
[5]
SO-1;   (ii) Discuss the working of filter, wrapper, and embedded techniques in feature
BL-2   selection.
Histogram and box plot (2 marks)
Histograms provide detailed distribution patterns (visual detail) while box plots
summarize spread and outliers (statistical summary)
Aspect   Histogram   Box Plot
Data Representation   Detailed distribution   Summary statistics
Spread   Range across bins   IQR + whiskers
Skewness   Shape of distribution   Median   position   &
whiskers
Outliers   Harder to detect   Clearly identified
Feature selection method (3 marks)
Filter methods: Assess feature relevance independent of the model using statistical
measures.
Wrapper methods: Evaluate different feature subsets using performance of a
specific machine learning model
Embedded methods: Incorporate feature selection into the model training process.
b.   At a hostel pizza party, students are classified into two categories:
“Happy” and “Angry” based on pizza distribution. You collected the following
Q4   data:
CO-5;   Group   Happy   Angry
[5]
SO-2;   Group A (Got Extra Cheese)   8   2
BL-3   Group B (No Extra Cheese)   3   7
Calculate the Gini Index for Group A and Group B and compute the weighted Gini
Index after the split. Comment whether this split is good or not.
Step 1: Gini for Group A
Total = 8 + 2 = 10
8 2   2 2
𝐺𝑖𝑛𝑖(𝐴) = 1 −( 10) −( 10)
= 1 −(0.64 + 0.04) = 1 −0.68 = 0.32
Step 2: Gini for Group B
Total = 3 + 7 = 10
3 2   7 2
𝐺𝑖𝑛𝑖(𝐵) = 1 −( 10) −( 10)
= 1 −(0.09 + 0.49) = 1 −0.58 = 0.42
********** 6 **********
--- page 7 ---
Step 3: Weighted Gini
10   10
𝐺𝑖𝑛𝑖𝑠𝑝𝑙𝑖𝑡= 20(0.32) + 20(0.42)
= 0.5(0.32) + 0.5(0.42) = 0.16 + 0.21 = 0.37
Conclusion:
Lower Gini indicates better purity. Since 0.37 is relatively low, the split is
reasonably good.
c.   (i) A company wants to classify customers as either "High Spender (H/1)" or "Low
Spender (L/0)" based on their Age and Annual Income using K-NN. A new
customer (X) has Age = 32 and Income = 55. Classify this customer using K-NN
(K = 3).
Customer   Age   Income   Class
Q4
A   25   50   H
CO-4;
B   30   60   H   [10]
SO-2;
C   35   80   H
BL-3
D   40   40   L
E   45   50   L
(ii) You are given a binary classification setup with feature: 𝑥=2 and true label:
𝑦=1. Model parameters: weight 𝑤=0.5 and bias 𝑏=−0.5. Compute the predicted
probability and cross entropy loss (using logistic regression).
(i) 7 marks
Customer   Age   Income   Class   Distance2   Rank
A   25   50   H   74   2
B   30   60   H   29   1
C   35   80   H   634   5
D   40   40   L   289   4
E   45   50   L   194   3
Majority class – H
(ii) Predicted probability and loss (3 marks)
Predicted probability = 0.622
********** 7 **********
--- page 8 ---
a
(i) Justify the statement: “K-Means clustering is sensitive to outliers.”
(ii) Consider the following data with initial cluster centers are A(2,2),C(1,1)and
the number of clusters K=2,Use the k-means algorithm with Euclidean
distance ,what are the assignments until converge.
Q5
CO-4;   Object X1 X2   [10]
SO-2;
A   2   2
BL-3
B   3   2
C   1   1
D   3   1
E   1.5 0.5
(i) K-Means clustering is sensitive to outliers (2 marks)
because the algorithm uses the mean of data points to determine the cluster centers
(centroids). Since the mean is highly affected by extreme values, even a single
outlier can significantly shift the centroid, leading to incorrect clustering
(ii) First iteration-3 marks
Second iteration 3 marks
Final cluster (to stop iteration) -2 marks
Q5   b   Following table shows the number of item sale for a particular day. Find the
CO-3;   regression equation in the form Y = aX + b. Also predict a sale for day 8.
[10]
SO-2;   Day (X)   1   2   3   4   5   6   7
BL-3   Sales (Y)   9   8   10   12   11   13   14
********** 8 **********
--- page 9 ---
Table calculation – 2 marks
Calculation of coefficients – 4 marks
Equation of line – 2 marks
Prediction – 2 marks
X   Y   X²   Y²   XY
1   9   1   81   9
2   8   4   64   16
3   10   9   100   30
4   12   16   144   48
5   11   25   121   55
6   13   36   169   78
Sale for day 8 = 0.929*8+7.284 = 14.716 (15)
a   A group of students is deciding whether to order momos. The decision (Target:
Order = Yes/No) depends on:
• Weather (Sunny/Rainy)
• Mood (Happy/Grumpy)
Dataset:
Q6   Weather   Mood   Order
CO-5;
Sunny   Happy   Yes   [10]
SO-2;
Sunny   Grumpy   No
BL-3
Rainy   Happy   Yes
Rainy   Grumpy   Yes
Sunny   Happy   Yes
Calculate the Entropy of the dataset. Information Gain for Weather and Mood and
identify the root node using ID3. Explain briefly how ID3 builds the decision tree
********** 9 **********
--- page 10 ---
Entropy calculation – 2 marks
IG (Weather) – 2 marks
IG (Mood) – 2 marks
Correct root selection – 2 marks
ID3 explanation – 2 marks
Step 1: Entropy of Dataset
Total = 5
Yes = 4, No = 1
−(4   4 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) =   5 log⁡2 5 + 5 log⁡2 5)
= −(0.8 ⋅−0.32 + 0.2 ⋅−2.32) ≈0.72
Step 2: Information Gain
(A) Weather
• Sunny → (Yes=2, No=1)
−(2   2 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦=   3 log⁡2 3 + 3 log⁡2 3) ≈0.92
• Rainy → (Yes=2, No=0)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦= 0
Weighted Entropy:
3   2
= (0.92) + (0) = 0.552
5   5
𝐼𝐺(𝑊𝑒𝑎𝑡ℎ𝑒𝑟) = 0.72 −0.552 = 0.168
(B) Mood
• Happy → (Yes=3, No=0) → Entropy = 0
• Grumpy → (Yes=1, No=1) → Entropy = 1
Weighted Entropy:
3   2
= (0) + (1) = 0.4
5   5
𝐼𝐺(𝑀𝑜𝑜𝑑) = 0.72 −0.4 = 0.32
Step 3: Root Node
Since IG(Mood) > IG(Weather)
Root Node = Mood
Step 4: ID3 Explanation
• ID3 builds a decision tree top-down (greedy approach)
•   Selects attribute with highest Information Gain
•   Splits dataset recursively
• Stops when: All examples belong to one class
No attributes left
b   (i) Define Core Point, Border Point, and Noise Point in DBSCAN clustering.
(ii) Consider the following dataset Ɛ = 2, MinPts = 3 Using DBSCAN, determine:
Core Points, Border Points, Noise Points, Final clusters formed.
Q6   Point   X   Y
CO-4;   P1   1   1   [10]
SO-1;
P2   2   2
BL-3
P3   2   1
P4   8   8
P5   8   9
********** 10 **********
--- page 11 ---
P6   25   25
Definition – (2 marks)
Core Point: A core point is a point that has at least MinPts points (including
itself) within its ε-neighborhood.
Border Point: A border point is a point that has fewer than MinPts points in
its ε-neighborhood but lies within the ε-neighborhood of a core point.
Noise Point: A noise point is a point that is neither a core point nor
reachable from any core point, meaning it does not belong to any cluster.
Distance table (3 marks)
Distance is calculated using Euclidean distance:
P1   P2   P3   P4   P5   P6
P1   0   1.41   1   9.9   10.63   33.94
P2   1.41   0   1   8.49   9.22   32.53
P3   1   1   0   9.22   10   33.24
P4   9.9   8.49   9.22   0   1   24.76
P5   10.63   9.22   10   1   0   23.35
P6   33.94   32.53   33.24   24.76   23.35   0
ε–Neighborhoods (2 marks)
• P1: {P1, P2, P3} → 3 points
• P2: {P1, P2, P3} → 3 points
• P3: {P1, P2, P3} → 3 points
• P4: {P4, P5} → 2 points
• P5: {P4, P5} → 2 points
• P6: {P6} → 1 point
Core Points (1 mark)
Core point condition → points ≥ MinPts (3)
Core point P1, P2, P3
Border points: (1 mark)
have less than MinPts
but be within ε of a core point. P4 and P5 are not within ε of any core point.
Therefore they cannot be border points.
Noise Points (1 mark)
Points not reachable from any core point:
Noise Points: P4, P5, P6
Q7   a   A dataset shows highly non-linear patterns and large in size. Which model type
CO-1;   (parametric / non-parametric) is more suitable? Analyze (i) the trade-off between
[5]
SO-1;   bias and variance (ii) How does dataset size (from small to large) influence the
BL-2   choice between parametric and non-parametric models?
Model type (1 mark)
Non-parametric preferred for non-linear data.
Tradeoff (2 marks)
Parametric – Bias is high and variance is low
Non-parametric – Bias is low and variance is high
Dataset size (2 marks)
Small Dataset- Use parametric models (Require less data, less sensitive to noise
and lower variance), non-parametric models may overfits easily.
********** 11 **********
--- page 12 ---
Large Dataset – Use non-parametric models (Capture complex patterns, reduce
overfitting), Parametric models may underfit.
Q7   b   Describe the working of Random Forest as an ensemble technique. How does it
CO-5;   improve over a single Decision Tree?
[5]
SO-1;
BL-3
Random Forest is an ensemble learning method that constructs multiple decision
trees and combines their outputs to improve predictive performance. (3 Marks)
Working:
1. Draw multiple bootstrap samples from the dataset.
2. Train a decision tree on each sample.
3. At each split, consider a random subset of features instead of all features.
4. Aggregate predictions using:
o Majority voting (classification)
o Averaging (regression)
Improvement over Decision Tree: (2 Marks)
• A single decision tree is prone to overfitting.
• Random Forest:
o Reduces variance by averaging multiple trees
o Improves generalization
Handles noise better
c   (i) Differentiate between Agglomerative and Divisive hierarchical clustering.
(ii) Using the given dataset, perform Agglomerative Hierarchical Clustering with
Q7   Single Linkage. Compute Euclidean distances and draw the dendrogram.
CO-4;   Point   X   Y
SO-1;   A   1   1   [10]
BL-3   B   2   1
C   4   3
D   5   4
Difference - (2 marks)
Agglomerative Clustering   Divisive Clustering
Bottom-up approach   Top-down approach
Starts with each   Starts with all
observation as a separate   observations in one
cluster   single cluster
Clusters are merged step-   Clusters are split
by-step   step-by-step
n clusters (n = number of
1 cluster
data points)
Ends with one large   Ends with many
cluster   smaller clusters
We use Euclidean distance
The distance matrix after applying Euclidean distance (2 marks)
A   B   C   D
********** 12 **********
--- page 13 ---
A   0   1   3.61   5
B   1   0   2.83   4.24
C   3.61   2.83   0   1.41
D   5   4.24   1.41   0
First Merge (Smallest Distance)
Smallest distance = 1 (A,B)
Clusters now:
{AB}, {C}, {D} ---------(1 mark)
Update Distance (Single Link)------------(updating distance and table creation
-2 marks)
Single link = minimum distance between cluster members
Distance (AB , C)
min(d(A,C),d(B,C))
min(3.61,2.83)=2.83
Distance (AB , D) = min(5,4.24)=4.24
AB   C   D
AB   0   2.83   4.24
C   2.83   0   1.41
D   4.24   1.41   0
Second Merge
Smallest distance = 1.41 (C,D)
Cluster:
C2={C,D}
Clusters now:
{AB}, {CD}---------(1 mark)
Distance (AB , CD)=min(d(AB,C),d(AB,D))= min(2.83,4.24)=2.83---------
(update distance and table creation -1 mark)
AB   CD
AB   0   2.83
CD   2.83   0
Final cluster
{ABCD}
Final dendogram— (1 mark)
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper de1a992cea83

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_AI_7051/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/MBA
Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q1
Answer briefly:   [20]
CO-1; a
Consider a real-world problem with limited labeled data. Examine how this
SO-1;   [5]
constraint affects supervised learning models and discuss five major limitations.
BL-2
Explanation of any 5 (each 1 mark)
Overfitting and Poor Generalization
High Cost of Data Annotation
Insufficient Representation of Data Variability
Class Imbalance and Bias
Inefficient Use of Unlabeled Data
High Variance and Model Instability
Poor Adaptability to Domain Shift
Difficulty in Model Evaluation
Noise Sensitivity
Inability to Discover Hidden Structures
b   Two datasets A and B each contain 5 values:
Dataset A: 48, 49, 50, 51, 52
CO-2;   Dataset B: 30, 40, 50, 60, 70
SO-1;   (i) Calculate the mean, median and variance for both datasets.   [5]
BL-2   (ii) Compare the dispersion of both datasets.
(iii) Based on the variance values, analyze which dataset is more likely to cause
overfitting in a machine learning model and justify your answer.
Dataset A (1 marks)
Mean = (48 + 49 + 50 + 51 + 52) / 5 = 250 / 5 = 50
Median = 50
Variance =2
Dataset B (1 mark)
********** 1 **********
--- page 2 ---
Mean = (30 + 40 + 50 + 60 + 70) / 5 = 250 / 5 = 50
Median = 50
Variance=200
Dispersion (1 mark)
Dataset A → Variance = 2 (Low dispersion)
Dataset B → Variance = 200 (High dispersion)
Dataset B is much more spread out
Overfit (2 marks)
Dataset A (Low Variance) - Data is closely clustered, model learns stable patterns
and more robust and reliable.
Dataset B (High Variance) - Data is widely spread, model may fit noise and learn
inconsistent patterns - higher risk of overfitting
c   A machine learning model is trained on a dataset and shows the following
behavior:
• Training error: very low
CO-3;
•   Test error: very high
SO-2;   [5]
(i). Identify whether the model is suffering from high bias or high variance.
BL-3
(ii). Suggest two methods to address this issue.
(iii). Explain how these methods help improve model performance in terms of the
bias–variance tradeoff.
i. The model is suffering from high variance (overfitting). (1 mark)
ii. Two methods to address this issue – (2 marks)
Apply Regularization (L1 or L2) and reduce model complexity
iii. Explanation using Bias–Variance Tradeoff – (2 marks)
• High variance means the model is too complex and fits noise in training
data.
• Regularization adds a penalty to large weights → simplifies the model →
reduces variance.
• Reducing model complexity prevents overfitting.
These methods: Decrease variance and slightly increase bias
Result in better generalization on test data
d   A classifier produces the following confusion matrix:
Predicted Positive   Predicted Negative
CO-4;
Actual Positive   80   20
SO-2;   [5]
Actual Negative   10   90
BL-3
(i) Calculate accuracy, precision, recall and F1-score.
(ii) Which metric is more important in medical diagnosis and why?
Performance (4 marks)
Accuracy= 𝑇𝑃+𝑇𝑁+𝐹𝑃+𝐹𝑁= 𝑇𝑃+𝑇𝑁   80+90 = 0.85
80+90+10+20
Precision= 𝑇𝑃+𝐹𝑃= 𝑇𝑃   80 = 0.89
80+10
Recall= 𝑇𝑃+𝐹𝑁= 𝑇𝑃   80 = 0.80
80+20
F1= 2𝑋(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑋𝑟𝑒𝑐𝑎𝑙𝑙) = 2𝑋0.712 = 0.84
𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑟𝑒𝑐𝑎𝑙𝑙   1.69
Important metric in medical diagnosis (1 marks)
Recall measures how many actual positive cases are correctly identified
In medical diagnosis:
Positive = disease present
False Negative (FN) = Patient has disease but model says No. This is dangerous.
Q2   a
CO-2;   (i) Given dataset with 2 features, Category = A, B, C, A, C and Target = 10, 20,
[5]
SO-1;   30, 40, 50. Apply label encoding and one-hot encoding for category feature.
BL-2
********** 2 **********
--- page 3 ---
(ii) A dataset contains both ordinal and nominal categorical variables. Discuss how
you would choose between label encoding and one-hot encoding for each feature
and justify your decisions.
Label Encoding (1 mark)
A-0
B-1
C-2
One-hot encoding (1 mark)
A   B   C
A   1   0   0
B   0   1   0
C   0   0   1
Explanation (3 marks)
For ordinal variables (ordered data) - Low < Medium < High
Use: Label / ordinal encoding
Preserves   natural   order,   model   can   learn-   relative   ranking   and
increasing/decreasing trends
For nominal variables (Unordered Data) - Color: Red, Blue, Green and Category:
A, B, C
Use: One-Hot Encoding
No artificial order introduced, each category treated independently and avoids
misleading relationships
Q2   b
CO-5;   How do Bagging and Boosting differ in machine learning models? Discuss their
[5]
SO-2;   working mechanisms and identify appropriate use cases for each technique.
BL-3
Bagging (Bootstrap Aggregating) (2 marks):
Generates multiple training datasets using sampling with replacement (bootstrap).
Trains multiple models independently and in parallel.
Combines predictions using averaging (regression) and majority voting
(classification).
Reduces variance and prevents overfitting
Boosting (2 marks):
Models are trained sequentially.
Each new model focuses on errors made by previous models.
Misclassified data points are given higher importance (weights). Final prediction
is a weighted combination of all models.
Reduces bias and variance, improves overall accuracy
Use case (1 mark)
c   (i) A bank wants to classify loan applicants as Approved (A) or Rejected (R) based
on Income, Credit score and Employment status.
No.   Income Credit Employment   Class
1   High   Good   Employed   A
Q2   2   High   Good   Employed   A
CO-4;   3   High   Bad   Employed   A
[10]
SO-2;   4   Low   Good   Employed   A
BL-3   5   High   Good   Unemployed   A
6   Low   Bad   Unemployed   R
7   Low   Bad   Employed   R
8   Low   Good   Unemployed   R
9   High   Bad   Unemployed   R
********** 3 **********
--- page 4 ---
10   Low   Bad   Unemployed   R
11   High   Good   Employed   A
12   Low   Good   Employed   R
Classify a new applicant: X = (Income = High, Credit = Good, Employment =
Employed) using Naïve Bayes classifier.
(ii) Discuss the problem of zero probability in Naive Bayes classification. How
does it affect prediction? Explain Laplace smoothing with a suitable example.
P(A∣X) (3 marks)
P(A)=6/12=0.5, P(R)=6/12=0.5
P(High/A)=5/6
P(Good/A)=5/6
P(Employed/A)=5/6
P(A∣X) ∝ P(A)XP(High/A)X P(Good/A)X P(Employed/A)
∝ 0.289
P(R∣X) (3 marks)
P(High/R)=1/6
P(Good/A)=2/6=1/3
P(Employed/A)=2/6=1/3
P(R∣X) ∝ P(A)XP(High/R)X P(Good/R)X P(Employed/R)
∝ 0.0093
Final class (1 marks)
P(A∣X) > P(R∣X)
Class is Approved (A)
(ii)Explanation (2 marks)
If any one conditional probability becomes zero, then: P(Y∣X)=0. This is called
the zero-frequency problem. It occurs, when a particular feature value never
appears in the training data for a class.
Laplace smoothing: Add a small constant (usually +1) to all counts to avoid zero
probabilities.
Example (1 mark)
a   (i) Briefly explain the objective function used in simple linear regression with
gradient decent. Algorithm.
Q3   (ii) Using gradient decent for simple linear regression, determine loss function
CO-3;   after two iterations for the given a dataset. Consider Learning rate as 0.001 and [10]
SO-2;   initial weights/coefficients as zeros.
BL-3   x   1   2   3   4   5
y   3   5   7   8   10
In Simple Linear Regression (using gradient decent), the objective is to find the best-
fitting line: y = mx + b
The objective function used is the Mean Squared Error (MSE): (1 mark)
Explanation (1 mark)
•   It measures the average squared difference between actual values and predicted
values. m is total number of samples.
• The goal of gradient descent is to minimize this cost function.
• By iteratively updating slope and intercept, we find the line that gives the least
prediction error.
Equations (2 marks) and iteration – 1 (3 marks)
********** 4 **********
--- page 5 ---
Iteration – 2 (3 marks)
b   (i) Consider the following dataset with two class (+1) and (-1). Find the class for
sample (4,2) using Support Vector Machine. Consider A and D points are support
vectors.
Q3   ID   X1   X2   Y
CO-4;   A   2   3   +1
[10]
SO-2;   B   3   4   +1
BL-3   C   1   1   -1
D   2   2   -1
(ii) Describe the kernel trick in SVM and how it helps in solving non-linear
classification problems.
(i) Writing equations (2 marks)
2w1+2w2+b=−1
2w1+3w2+b=+1
Calculation of w1, w2 and b (4 marks)
Lagrangian formula
9a1+11a2=-1
11a1+14a2=+1
A1=-5, a2=4
w1=-2
w2=2
w=(−2,2),b=−1
class (2 marks)
y=−2x1+2x2−1
Substitute point (4,2) in y.
y=-5
********** 5 **********
--- page 6 ---
sign of y is -ve so the sample (4,2) belongs to -1 class
(ii) Explanation (2 marks)
A straight line (or hyperplane) cannot divide the data properly
Kernel Trick Works:
Data is implicitly mapped to a higher-dimensional space
In that space, data becomes linearly separable
SVM finds a linear hyperplane in this new space
The result corresponds to a non-linear boundary in original space
Q4   a   (i) How do histogram and box plot differ in representing data distribution
CO-2;   characteristics such as spread, skewness, and outliers?
[5]
SO-1;   (ii) Discuss the working of filter, wrapper, and embedded techniques in feature
BL-2   selection.
Histogram and box plot (2 marks)
Histograms provide detailed distribution patterns (visual detail) while box plots
summarize spread and outliers (statistical summary)
Aspect   Histogram   Box Plot
Data Representation   Detailed distribution   Summary statistics
Spread   Range across bins   IQR + whiskers
Skewness   Shape of distribution   Median   position   &
whiskers
Outliers   Harder to detect   Clearly identified
Feature selection method (3 marks)
Filter methods: Assess feature relevance independent of the model using statistical
measures.
Wrapper methods: Evaluate different feature subsets using performance of a
specific machine learning model
Embedded methods: Incorporate feature selection into the model training process.
b.   At a hostel pizza party, students are classified into two categories:
“Happy” and “Angry” based on pizza distribution. You collected the following
Q4   data:
CO-5;   Group   Happy   Angry
[5]
SO-2;   Group A (Got Extra Cheese)   8   2
BL-3   Group B (No Extra Cheese)   3   7
Calculate the Gini Index for Group A and Group B and compute the weighted Gini
Index after the split. Comment whether this split is good or not.
Step 1: Gini for Group A
Total = 8 + 2 = 10
8 2   2 2
𝐺𝑖𝑛𝑖(𝐴) = 1 −( 10) −( 10)
= 1 −(0.64 + 0.04) = 1 −0.68 = 0.32
Step 2: Gini for Group B
Total = 3 + 7 = 10
3 2   7 2
𝐺𝑖𝑛𝑖(𝐵) = 1 −( 10) −( 10)
= 1 −(0.09 + 0.49) = 1 −0.58 = 0.42
********** 6 **********
--- page 7 ---
Step 3: Weighted Gini
10   10
𝐺𝑖𝑛𝑖𝑠𝑝𝑙𝑖𝑡= 20(0.32) + 20(0.42)
= 0.5(0.32) + 0.5(0.42) = 0.16 + 0.21 = 0.37
Conclusion:
Lower Gini indicates better purity. Since 0.37 is relatively low, the split is
reasonably good.
c.   (i) A company wants to classify customers as either "High Spender (H/1)" or "Low
Spender (L/0)" based on their Age and Annual Income using K-NN. A new
customer (X) has Age = 32 and Income = 55. Classify this customer using K-NN
(K = 3).
Customer   Age   Income   Class
Q4
A   25   50   H
CO-4;
B   30   60   H   [10]
SO-2;
C   35   80   H
BL-3
D   40   40   L
E   45   50   L
(ii) You are given a binary classification setup with feature: 𝑥=2 and true label:
𝑦=1. Model parameters: weight 𝑤=0.5 and bias 𝑏=−0.5. Compute the predicted
probability and cross entropy loss (using logistic regression).
(i) 7 marks
Customer   Age   Income   Class   Distance2   Rank
A   25   50   H   74   2
B   30   60   H   29   1
C   35   80   H   634   5
D   40   40   L   289   4
E   45   50   L   194   3
Majority class – H
(ii) Predicted probability and loss (3 marks)
Predicted probability = 0.622
********** 7 **********
--- page 8 ---
a
(i) Justify the statement: “K-Means clustering is sensitive to outliers.”
(ii) Consider the following data with initial cluster centers are A(2,2),C(1,1)and
the number of clusters K=2,Use the k-means algorithm with Euclidean
distance ,what are the assignments until converge.
Q5
CO-4;   Object X1 X2   [10]
SO-2;
A   2   2
BL-3
B   3   2
C   1   1
D   3   1
E   1.5 0.5
(i) K-Means clustering is sensitive to outliers (2 marks)
because the algorithm uses the mean of data points to determine the cluster centers
(centroids). Since the mean is highly affected by extreme values, even a single
outlier can significantly shift the centroid, leading to incorrect clustering
(ii) First iteration-3 marks
Second iteration 3 marks
Final cluster (to stop iteration) -2 marks
Q5   b   Following table shows the number of item sale for a particular day. Find the
CO-3;   regression equation in the form Y = aX + b. Also predict a sale for day 8.
[10]
SO-2;   Day (X)   1   2   3   4   5   6   7
BL-3   Sales (Y)   9   8   10   12   11   13   14
********** 8 **********
--- page 9 ---
Table calculation – 2 marks
Calculation of coefficients – 4 marks
Equation of line – 2 marks
Prediction – 2 marks
X   Y   X²   Y²   XY
1   9   1   81   9
2   8   4   64   16
3   10   9   100   30
4   12   16   144   48
5   11   25   121   55
6   13   36   169   78
Sale for day 8 = 0.929*8+7.284 = 14.716 (15)
a   A group of students is deciding whether to order momos. The decision (Target:
Order = Yes/No) depends on:
• Weather (Sunny/Rainy)
• Mood (Happy/Grumpy)
Dataset:
Q6   Weather   Mood   Order
CO-5;
Sunny   Happy   Yes   [10]
SO-2;
Sunny   Grumpy   No
BL-3
Rainy   Happy   Yes
Rainy   Grumpy   Yes
Sunny   Happy   Yes
Calculate the Entropy of the dataset. Information Gain for Weather and Mood and
identify the root node using ID3. Explain briefly how ID3 builds the decision tree
********** 9 **********
--- page 10 ---
Entropy calculation – 2 marks
IG (Weather) – 2 marks
IG (Mood) – 2 marks
Correct root selection – 2 marks
ID3 explanation – 2 marks
Step 1: Entropy of Dataset
Total = 5
Yes = 4, No = 1
−(4   4 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) =   5 log⁡2 5 + 5 log⁡2 5)
= −(0.8 ⋅−0.32 + 0.2 ⋅−2.32) ≈0.72
Step 2: Information Gain
(A) Weather
• Sunny → (Yes=2, No=1)
−(2   2 1   1
𝐸𝑛𝑡𝑟𝑜𝑝𝑦=   3 log⁡2 3 + 3 log⁡2 3) ≈0.92
• Rainy → (Yes=2, No=0)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦= 0
Weighted Entropy:
3   2
= (0.92) + (0) = 0.552
5   5
𝐼𝐺(𝑊𝑒𝑎𝑡ℎ𝑒𝑟) = 0.72 −0.552 = 0.168
(B) Mood
• Happy → (Yes=3, No=0) → Entropy = 0
• Grumpy → (Yes=1, No=1) → Entropy = 1
Weighted Entropy:
3   2
= (0) + (1) = 0.4
5   5
𝐼𝐺(𝑀𝑜𝑜𝑑) = 0.72 −0.4 = 0.32
Step 3: Root Node
Since IG(Mood) > IG(Weather)
Root Node = Mood
Step 4: ID3 Explanation
• ID3 builds a decision tree top-down (greedy approach)
•   Selects attribute with highest Information Gain
•   Splits dataset recursively
• Stops when: All examples belong to one class
No attributes left
b   (i) Define Core Point, Border Point, and Noise Point in DBSCAN clustering.
(ii) Consider the following dataset Ɛ = 2, MinPts = 3 Using DBSCAN, determine:
Core Points, Border Points, Noise Points, Final clusters formed.
Q6   Point   X   Y
CO-4;   P1   1   1   [10]
SO-1;
P2   2   2
BL-3
P3   2   1
P4   8   8
P5   8   9
********** 10 **********
--- page 11 ---
P6   25   25
Definition – (2 marks)
Core Point: A core point is a point that has at least MinPts points (including
itself) within its ε-neighborhood.
Border Point: A border point is a point that has fewer than MinPts points in
its ε-neighborhood but lies within the ε-neighborhood of a core point.
Noise Point: A noise point is a point that is neither a core point nor
reachable from any core point, meaning it does not belong to any cluster.
Distance table (3 marks)
Distance is calculated using Euclidean distance:
P1   P2   P3   P4   P5   P6
P1   0   1.41   1   9.9   10.63   33.94
P2   1.41   0   1   8.49   9.22   32.53
P3   1   1   0   9.22   10   33.24
P4   9.9   8.49   9.22   0   1   24.76
P5   10.63   9.22   10   1   0   23.35
P6   33.94   32.53   33.24   24.76   23.35   0
ε–Neighborhoods (2 marks)
• P1: {P1, P2, P3} → 3 points
• P2: {P1, P2, P3} → 3 points
• P3: {P1, P2, P3} → 3 points
• P4: {P4, P5} → 2 points
• P5: {P4, P5} → 2 points
• P6: {P6} → 1 point
Core Points (1 mark)
Core point condition → points ≥ MinPts (3)
Core point P1, P2, P3
Border points: (1 mark)
have less than MinPts
but be within ε of a core point. P4 and P5 are not within ε of any core point.
Therefore they cannot be border points.
Noise Points (1 mark)
Points not reachable from any core point:
Noise Points: P4, P5, P6
Q7   a   A dataset shows highly non-linear patterns and large in size. Which model type
CO-1;   (parametric / non-parametric) is more suitable? Analyze (i) the trade-off between
[5]
SO-1;   bias and variance (ii) How does dataset size (from small to large) influence the
BL-2   choice between parametric and non-parametric models?
Model type (1 mark)
Non-parametric preferred for non-linear data.
Tradeoff (2 marks)
Parametric – Bias is high and variance is low
Non-parametric – Bias is low and variance is high
Dataset size (2 marks)
Small Dataset- Use parametric models (Require less data, less sensitive to noise
and lower variance), non-parametric models may overfits easily.
********** 11 **********
--- page 12 ---
Large Dataset – Use non-parametric models (Capture complex patterns, reduce
overfitting), Parametric models may underfit.
Q7   b   Describe the working of Random Forest as an ensemble technique. How does it
CO-5;   improve over a single Decision Tree?
[5]
SO-1;
BL-3
Random Forest is an ensemble learning method that constructs multiple decision
trees and combines their outputs to improve predictive performance. (3 Marks)
Working:
1. Draw multiple bootstrap samples from the dataset.
2. Train a decision tree on each sample.
3. At each split, consider a random subset of features instead of all features.
4. Aggregate predictions using:
o Majority voting (classification)
o Averaging (regression)
Improvement over Decision Tree: (2 Marks)
• A single decision tree is prone to overfitting.
• Random Forest:
o Reduces variance by averaging multiple trees
o Improves generalization
Handles noise better
c   (i) Differentiate between Agglomerative and Divisive hierarchical clustering.
(ii) Using the given dataset, perform Agglomerative Hierarchical Clustering with
Q7   Single Linkage. Compute Euclidean distances and draw the dendrogram.
CO-4;   Point   X   Y
SO-1;   A   1   1   [10]
BL-3   B   2   1
C   4   3
D   5   4
Difference - (2 marks)
Agglomerative Clustering   Divisive Clustering
Bottom-up approach   Top-down approach
Starts with each   Starts with all
observation as a separate   observations in one
cluster   single cluster
Clusters are merged step-   Clusters are split
by-step   step-by-step
n clusters (n = number of
1 cluster
data points)
Ends with one large   Ends with many
cluster   smaller clusters
We use Euclidean distance
The distance matrix after applying Euclidean distance (2 marks)
A   B   C   D
********** 12 **********
--- page 13 ---
A   0   1   3.61   5
B   1   0   2.83   4.24
C   3.61   2.83   0   1.41
D   5   4.24   1.41   0
First Merge (Smallest Distance)
Smallest distance = 1 (A,B)
Clusters now:
{AB}, {C}, {D} ---------(1 mark)
Update Distance (Single Link)------------(updating distance and table creation
-2 marks)
Single link = minimum distance between cluster members
Distance (AB , C)
min(d(A,C),d(B,C))
min(3.61,2.83)=2.83
Distance (AB , D) = min(5,4.24)=4.24
AB   C   D
AB   0   2.83   4.24
C   2.83   0   1.41
D   4.24   1.41   0
Second Merge
Smallest distance = 1.41 (C,D)
Cluster:
C2={C,D}
Clusters now:
{AB}, {CD}---------(1 mark)
Distance (AB , CD)=min(d(AB,C),d(AB,D))= min(2.83,4.24)=2.83---------
(update distance and table creation -1 mark)
AB   CD
AB   0   2.83
CD   2.83   0
Final cluster
{ABCD}
Final dendogram— (1 mark)
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 8e154f836e01

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CSBS_7036/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.docx`
- Printed on paper: duration hours: 3
- Text: docx (1 page)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF   TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
|
Program/s: B. Tech(Computer)
Stream/s ; B. Tech(CSBS)/B.Tech(CS)
| Year: III, IV   Semester: V, VII
|
Subject: Machine Learning
| Time: 3 Hours hrs (______to_______)
|

| No. of Pages: 3
|
Marks: __100_______
|
|
Synoptic Answer
|

Q1
|
| Answer briefly:
|
|

| a)
| Given the following scenarios, identify the most suitable type of machine learning technique and justify your choice:
a) Predicting house prices based on features like size and location.
b) Grouping customers based on purchasing patterns.
c) Recognize handwritten digits from images

Technique carries 3 marks and justification carries 2 marks
a) Predicting house prices based on features like size and location
Suitable Technique: Supervised Learning – Regression
Justification: The model learns from labeled data (house features with known prices) to predict a continuous value — the price.
b) Grouping customers based on purchasing patterns
Suitable Technique: Unsupervised Learning – Clustering
Justification: There are no predefined labels; the model discovers hidden patterns and forms groups based on similarity among customer behaviors.
c) Neural Network, Supervised Learning
Suitable Technique: Artificial neural network
Justification: Handwritten digit recognition is fundamentally an image classification problem, which involves mapping an image (a grid of pixels) to one of 10 discrete categories (the digits 0 through 9).
Mapping: The neural network takes the pixel values of the image as its input (e.g., a 28×28 image is flattened into a 784-dimension input vector).
Output: The final layer has 10 neurons, one for each digit. The network uses the Softmax activation function on the output layer, which converts the scores into a probability distribution. The digit corresponding to the highest probability is the network's prediction.
|
|

| b)
| Explain backpropagation using gradient descent algorithm for an artificial neural network.

Ans: Explanation with diagram 2 marks
Backpropagation-3 marks
Backpropagation   o compute gradients of the loss function with respect to each weight in the network. These gradients tell us how to adjust the weights to reduce the error.
Backpropagation computes gradient descent, which uses the gradients to update the weights.

Wnew= Wold+ delta w

|
|

| c)
| You are developing a machine learning model for predicting customer churn. How can bootstrapping and bagging improve the performance of your model? Explain briefly.

Ans: 2.5 Marks each for bootstrapping and bagging

Bootstrap sampling is a technique of creating multiple datasets from the original dataset by random sampling with replacement. This means each sample in the original dataset can appear more than once or not at all in a new dataset.

Creating Training Datasets in Bagging:

Suppose the original dataset has 1000 samples.

To create a bootstrap sample, randomly select 1000 samples with replacement from the original dataset.

Repeat this process multiple times (e.g., 10–100 times) to create multiple training datasets.

Each of these datasets is slightly different from the others due to the random selection and replacement.

Purpose in Bagging:

Each bootstrap dataset is used to train a separate base learner (e.g., a decision tree).

Combining the predictions of all learners (e.g., by majority voting for classification or averaging for regression) helps to reduce variance and improve the model’s overall performance.

|
|

| d)
| A regression model performs poorly on both training and test data. Another model performs very well on training data but poorly on test data.
Identify which model suffers from high bias and which from high variance, and justify your answer.

Ans: 2.5 marks   each for the identification of bias and variance and proper justification

Model 1 suffers from high bias. High bias means the model is too simple to capture the underlying data complexity. It underfits the data. Underfitting causes large errors everywhere—both on training and test sets.
Model 2 suffers with variance. Performs very well on training data but poorly on test data.
Excellent performance on training data means:
The model learned the training patterns extremely well. Poor performance on test data means:   It fails to generalize the unseen data. High variance occurs when the model is too complex and fits the training data too closely (overfitting).
   It memorizes the training dataset instead of learning general patterns.
   This leads to low training error but high test error.
|
|
Q2
|
|
|
|

| a)
| What is exploratory data analysis? Explain different steps in exploratory data analysis for model building.
Ans:
Exploratory data analysis (EDA) is used by data scientists to analyze and investigate data sets and summarize their main characteristics, often employing data visualization methods.
Exploratory Data Analysis is a crucial step before you jump to machine learning or modeling of your data. By doing this you can get to know whether the selected features are good enough to model, are all the features required, are there any correlations based on which we can either go back to the Data Pre-processing step or move on to modeling.
Each Step along with example carries 2 marks
Steps
Description of data
Handling missing data
Handling outliers
Understanding relationships and new insights through plots

|
|

| b)
| Write the K-Means Clustering Algorithm. Apply it to the following one-dimensional dataset:{2,4,10,12,3,20,30,11,25}
Use K = 2 clusters and determine: (i)The final stable clusters. (ii)The centroids of each cluster after convergence. (iii)Show all steps of the algorithm clearly.
Ans:   K-means Algorithm carries 5 marks and Numerical Carries 5 marks

Numerical carries marks
Given: {2,4,10,12,3,20,30,11,25}, k=2
Randomly assign means: m1=3,m2=4
K1={2,3}, K2={4,10,12,20,30,11,25}, m1=2.5,m2=16
K1={2,3,4},K2={10,12,20,30,11,25}, m1=3,m2=18
K1={2,3,4,10},K2={12,20,30,11,25}, m1=4.75,m2=19.6
K1={2,3,4,10,11,12},K2={20,30,25}, m1=7,m2=25
Stop as the clusters with these means are the same.

|
|
Q3
|
|
|
|

| a)
| How does SVM find the optimal separating hyperplane for binary classification? Explain how SVM uses the kernel trick to handle non-linearly separable data.
Ans: SVM finding optimal separating hyperplane carries 5 marks and any two SVM kernel tricks carries 5 marks
A SVM which is used to classify data which are linearly separable is called linear SVM.
In other words, a linear SVM searches for a hyperplane with the maximum margin.
This is why a linear SVM is often termed as a maximal margin classifier (MMC).

Non Linear SVM 5 Marks
Kernel functions:
The kernel function is a technique used to transform data into a higher dimension to make it easier to classify when the data is not linearly separable in its original space.
Common kernel functions include:
Linear Kernel: No transformation; works directly in the input space.
Polynomial Kernel: Adds polynomial features.
Radial Basis Function (RBF) Kernel: Maps data into infinite dimensions using a Gaussian function.
Sigmoid Kernel: Similar to a neural network activation function.

If we cannot draw a straight line (or hyperplane) to separate the classes in the input space, SVM needs a non-linear boundary. Using the Kernel trick, z=x2+y2   is used to handle non-linear data.

|
|

| b)
| Logistic Regression models the probability of a binary outcome using the logistic (sigmoid) function carries 5 marks
Logistic Regression models the probability of a binary outcome (e.g., Yes/No, 1/0) by using the logistic function, also known as the sigmoid function, to map the output of a standard linear equation into the range of [0,1].
Here is a breakdown of the three key steps:
1. The Linear Model (The "Input")
Like Linear Regression, Logistic Regression begins by calculating a linear combination of the input features (x) and their corresponding weights (β), plus an intercept (β0​ or b). This intermediate result is often denoted as z and is called the log-odds or the logit.

2. The Sigmoid Transformation
This is where the logistic (sigmoid) function comes in. Its purpose is to transform the unbounded linear output (z) into a value that is strictly bounded between 0 and 1, which can then be interpreted as a probability.

3. Interpreting the Log-Odds (z) and Probability (P)
The sigmoid function ensures that:
Linear Output (z)
| Sigmoid Output (P)
| Interpretation
|
z→∞ (Very large positive)
| P→1
| The outcome is almost certain to be 1.
|
z=0
| P=0.5
| The outcome is equally likely to be 0 or 1.
|
z→−∞ (Very large negative)
| P→0
| The outcome is almost certain to be 0.
|

Numerical on Logistic Regression Carries-5 marks
A company wants to predict whether a candidate will get selected for a job based on the number of hours they spent preparing for the interview.
The log of odd value is given as: log⁡(odds)=z=-10.985+0.4395×Hours
i) Calculate the probability that a candidate who prepared for 28 hours will be selected. ii) Determine the minimum number of hours a candidate should prepare to have a probability of selection of at least 90%.

Ans:

P=11+e-1.318=11+0.268≈0.789

For 28 hours=0.789
X=13.1820.4394≈30 hours
So, a candidate should prepare at least 30 hours to have ≥ 90% chance of selection.
First part 5 marks,
Second part 5 marks
|
|
Q4
|
|
|
|

| a)
| A Python program to perform the following operations using pandas. (i)Read the CSV file into a Data Frame. (ii)Display the first 5 records. (iii)Display the number of rows and columns. (iv)Identify missing values and replace with mean values (v) Perform one-hot encoding on the Department column.
Each Operation Carries 2 marks
Employee.CSV file
Emp Id
| Name
| Age
| Department
| Salary
| Gender
|
101
| Raj
| 28
| HR
| 45000
| Male
|
102
| Meena
| 32
| IT
| 60000
| Female
|
103
| Karan
| NaN
| Finance
| 52000
| Male
|
104
| Priya
| 29
| IT
| NaN
| ,Female
|
105
| Amit
| 35
| HR
| 48000
| Male
|

|
|

|
| Reading the CSV into a DataFrame — Bloom: Remember / Understand
Uses pd.read_csv('employee.csv') correctly and assigns to a DataFrame.
Displaying the first 5 records   — Bloom: Remember
Full (1.0): Uses df.head() or df.head(5) and shows output.
Finding number of rows and columns   — Bloom: Understand
Uses df.shape (or len(df) & df.shape[1]) and reports correctly.
Identifying missing values   — Bloom: Analyze
Uses df.isnull().sum() (or equivalent) and identifies the missing entries in Age and Salary.
Replacing missing Age with mean — Bloom: Apply
Full (1.5): Computes mean from non-missing ages, uses e.g. df['Age'].fillna(df['Age'].mean(), inplace=True) and shows updated values (correct mean used).
Replacing missing Salary with median   — Bloom: Apply
Full (1.5): Computes median from non-missing salaries and fills NaN correctly (e.g., df['Salary'].fillna(df['Salary'].median(), inplace=True))..
One-hot encoding Department — Bloom: Apply / Create
Full (1.5): Uses pd.get_dummies(df['Department'], prefix='Department') or pd.get_dummies(df, columns=['Department']), correctly appends/replaces columns and drops original if required. All department categories handled.

|
|

| b)

| Design Dendrogram and form clusters by applying Agglomerative algorithm with the following data stored in adjacency distance matrix using single link approach and complete link technique.

Designed of Dendrogram with single link carries 5 marks by solving adjacency matrix at every level by single link distance.

Designed of dendrogram using complete link with steps carries 5 marks by solving adjancy matrix at every level.

|
|
Q5
|
|
|
|

| a)
| Explain the major 4 challenges faced in Unsupervised Learning and illustrate each challenge with suitable examples.
Four challenges with explanation carries 2 marks each and example carries 2 marks(4*2+2=10)
Point
| Explanation
| Marks
|
1. Lack of Ground Truth / Labels
| No predefined labels make it difficult to evaluate model performance or validate cluster quality.
| 1.5
|
2. Determining the Right Number of Clusters or Groups
| Algorithms like K-Means require k as input; choosing optimal k is challenging.
| 1.5
|
3. Interpretability of Results
| It’s often unclear what each cluster or pattern represents in real-world terms.
| 1
|
4. Sensitivity to Initialization / Parameters
| Many algorithms (e.g., K-Means) depend on initial centroid selection, leading to different outcomes.
| 1
|
5. Handling High-Dimensional Data
| In high dimensions, distances become less meaningful (curse of dimensionality).
| 1.5
|
6. Noisy or Overlapping Data
| Noise and outliers can distort clusters and reduce accuracy.
| 1
|
7. Scalability Issues
| Algorithms may become computationally expensive for large datasets.
| 1
|
8. Evaluation Metrics
| Choosing metrics like silhouette score, Davies–Bouldin index, etc., is non-trivial.
| 1.5
|

|
|

| b)
| Design a Decision Tree for the given dataset using the ID3 algorithm. Calculate the entropy and information gain for each attribute. Find the best root node. Mention the steps clearly. All the answers to be mentioned to the 4th decimal.

Best rootnode=Study hours

Entropy of the entire dataset 1 marks, 3 marks each for gain calculation of 3 independent variables.

Study
Hours
| Attendance
| Homework
| Result
|
High
| Regular
| Yes
| Pass
|
High
| Irregular
| No
| Pass
|
Medium
| Regular
| Yes
| Pass
|
Low
| Regular
| No
| Fail
|
Low
| Irregular
| No
| Fail
|
Medium
| Irregular
| No
| Fail
|
Medium
| Regular
| No
| Pass
|
High
| Regular
| No
| Pass
|
Low
| Regular
| Yes
| Fail
|
High
| Irregular
| Yes
| Pass
|

|
|

Q6
|
|
|
|

| a)
| Answer
Brain Tumor Type
| Predicted: Glioma (0)
| Predicted: Meningioma (1)
| Predicted: Pituitary (2)
|
Actual: Glioma (0)
| 5
| 2
| 1
|
Actual: Meningioma (1)
| 1
| 6
| 1
|
Actual: Pituitary(2)
| 0
| 2
| 2
|
From this matrix we can compute metrics:
For Class 0 (Glioma): 2.5 marks
TP = 5 (correctly predicted Apples)
FP = 1 + 0 = 1
FN = 2 + 1 = 3
TN = 20 - (TP+FP+FN) = 20 - 9 = 11
So,
Precision (Glioma) = TP / (TP+FP) = 5 / (5+1) = 0.833
Recall (Glioma) = TP / (TP+FN) = 5 / (5+3) = 0.625

For Class 1 (Meningioma): 2.5 marks
TP = 6
FP = 2 + 2 = 4
FN = 1 + 1 = 2
TN = 20 - (6+4+2) = 8
So,
Precision (Meningioma) = 6 / (6+4) = 0.6
Recall (Meningioma) = 6 / (6+2) = 0.75

For Class 2 (Pituitary): 2.5 marks
TP = 2
FN = 2
TN = 20 - (2+2+2) = 14
So,
Precision (Pituitary) = 2 / (2+2) = 0.5
Recall (Orange Pituitary = 2 / (2+2) = 0.5
Overall Accuracy 1 marks
Accuracy=Correct PredictionsTotal Predictions\t{Accuracy} = Predictions}}Accuracy=Total PredictionsCorrect Predictions​
Correct predictions = diagonal sum = 5 + 6 + 2 = 13
Total = 20
Accuracy=13/20=0.65=65

Justification carries 1.5 marks

|
|

| b)
| Apply Naïve Bayesian Algorithm to classify incoming tuple T
T={Age=Old, Competition=Yes, Industry=Hardware} as Low or High

Marks mentioned against the solved problem

|
|
Q7
|
|
|
|

| A
| The sale of company in million dollars for each year are shown in table:

X(Years)
| 2005
| 2006
| 2007
| 2008
| 2009
|
Y (Sales)
| 12
| 19
| 29
| 37
| 45
|
Find
Least Square Regression Line y=ax+b
Use Least Square Regression Line as a model to estimate sale of company in 2012
Compute the Mean Squared Error (MSE) for the given data using the obtained regression model. Analyze and comment on the performance and accuracy of the model based on the calculated MSE value.

Least square Regression line 5 marks, Estimate sale 2 marks, MSE calculation 2 Marks, Inference 1 Marks

Regression Line
| y=8.4x+3.2
|

Estimated Sale (2012)
| $70.4 million
|

Mean Squared Error (MSE)
| 0.32
|

|
|

|
|

|
|

| b
| Explain any   2 types of cross validation techniques to improve the performance of machine learning model,   to deal with problem of model overfitting and underfitting.

Ans:   Each Technique carries 5 marks along with figures
1. K fold cross validation
The dataset is split into K equal parts (folds).
The model is trained on 20-80, 30-70, 50-50, 70-30 etc
This process repeats K times, each time using a different fold for testing.
Final performance = average of all K test results.
The model is tested on multiple different subsets, preventing it from memorizing one particular train-test split.
Ensures good generalization.
Uses a large portion (K–1 folds) for training each time, giving the model more data to learn from.
2. Stratified K-Fold Cross Validation
(Useful especially in classification problems, e.g., heart disease dataset)
Similar to K-Fold, but ensures each fold has the same class proportion as the original dataset.
Example: If original dataset has 60% class 0 and 40% class 1, each fold maintains the same ratio.
Prevents training on folds with skewed class distribution.
Ensures the model does not learn patterns that are biased toward one class.
Balanced folds help the model learn representative patterns from minority classes.

|
|
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper e92cca887dca

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CSBS_7036/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: duration hours: 3
- Text: mixed (21 pages), mean OCR confidence 86.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
Program/s: B. Tech(Computer)   Year: III, IV Semester: V, VII
Stream/s ; B. Tech(CSBS)/B.Tech(CS)
Subject: Machine Learning   Time: 3 Hours hrs (______to_______)
No. of Pages: 3
Marks: __100_______
Synoptic Answer
Q1   Answer briefly:
a) Given the following scenarios, identify the most suitable type of machine learning technique and justify
your choice:
a) Predicting house prices based on features like size and location.
b) Grouping customers based on purchasing patterns.
c) Recognize handwritten digits from images
Technique carries 3 marks and justification carries 2 marks
a) Predicting house prices based on features like size and location
•   Suitable Technique: Supervised Learning – Regression
•   Justification: The model learns from labeled data (house features with known prices) to
predict a continuous value — the price.
b) Grouping customers based on purchasing patterns
•   Suitable Technique: Unsupervised Learning – Clustering
•   Justification: There are no predefined labels; the model discovers hidden patterns and forms
groups based on similarity among customer behaviors.
c) Neural Network, Supervised Learning
•   Suitable Technique: Artificial neural network
•   Justification: Handwritten digit recognition is fundamentally an image
classification problem, which involves mapping an image (a grid of pixels) to one
of 10 discrete categories (the digits 0 through 9).
1. Mapping: The neural network takes the pixel values of the image as its input (e.g.,
a 28×28 image is flattened into a 784-dimension input vector).
2. Output: The final layer has 10 neurons, one for each digit. The network uses the
Softmax activation function on the output layer, which converts the scores into a
1
--- page 2 ---
probability distribution. The digit corresponding to the highest probability is the
network's prediction.
b) Explain backpropagation using gradient descent algorithm for an artificial neural network.
Ans: Explanation with diagram 2 marks
Backpropagation-3 marks
Backpropagation o compute gradients of the loss function with respect to each weight in the
network. These gradients tell us how to adjust the weights to reduce the error.
Backpropagation computes gradient descent, which uses the gradients to update the weights.
Wnew= Wold+ delta w
c) You are developing a machine learning model for predicting customer churn. How can bootstrapping
and bagging improve the performance of your model? Explain briefly.
Ans: 2.5 Marks each for bootstrapping and bagging
Bootstrap sampling is a technique of creating multiple datasets from the original dataset by random
sampling with replacement. This means each sample in the original dataset can appear more than once
or not at all in a new dataset.
2
--- page 3 ---
Creating Training Datasets in Bagging:
Suppose the original dataset has 1000 samples.
To create a bootstrap sample, randomly select 1000 samples with replacement from the original dataset.
Repeat this process multiple times (e.g., 10–100 times) to create multiple training datasets.
Each of these datasets is slightly different from the others due to the random selection and replacement.
Purpose in Bagging:
Each bootstrap dataset is used to train a separate base learner (e.g., a decision tree).
Combining the predictions of all learners (e.g., by majority voting for classification or averaging for
regression) helps to reduce variance and improve the model’s overall performance.
d) A regression model performs poorly on both training and test data. Another model performs very well
on   training   data   but   poorly   on   test   data.
Identify which model suffers from high bias and which from high variance, and justify your answer.
Ans: 2.5 marks each for the identification of bias and variance and proper justification
Model 1 suffers from high bias. High bias means the model is too simple to capture the underlying data
complexity. It underfits the data. Underfitting causes large errors everywhere—both on training and test
sets.
Model 2 suffers with variance. Performs very well on training data but poorly on test data.
Excellent performance on training data means:
The model learned the training patterns extremely well. Poor performance on test data means:
It fails to generalize the unseen data. High variance occurs when the model is too complex
and fits the training data too closely (overfitting).
• It memorizes the training dataset instead of learning general patterns.
• This leads to low training error but high test error.
Q2
a) What is exploratory data analysis? Explain different steps in exploratory data analysis for model
building.
Ans:
•   Exploratory data analysis (EDA) is used by data scientists to analyze and investigate data sets
and summarize their main characteristics, often employing data visualization methods.
•   Exploratory Data Analysis is a crucial step before you jump to machine learning or modeling
of your data. By doing this you can get to know whether the selected features are good enough
to model, are all the features required, are there any correlations based on which we can either
go back to the Data Pre-processing step or move on to modeling.
Each Step along with example carries 2 marks
3
--- page 4 ---
Steps
•   Description of data
•   Handling missing data
•   Handling outliers
•   Understanding relationships and new insights through plots
b) Write the K-Means Clustering Algorithm. Apply it to the following one-dimensional
dataset:{2,4,10,12,3,20,30,11,25}
Use K = 2 clusters and determine: (i)The final stable clusters. (ii)The centroids of each cluster after
convergence. (iii)Show all steps of the algorithm clearly.
Ans: K-means Algorithm carries 5 marks and Numerical Carries 5 marks
Numerical carries marks
•   Given: {2,4,10,12,3,20,30,11,25}, k=2
• Randomly assign means: m1=3,m2=4
•   K1={2,3}, K2={4,10,12,20,30,11,25}, m1=2.5,m2=16
•   K1={2,3,4},K2={10,12,20,30,11,25}, m1=3,m2=18
•   K1={2,3,4,10},K2={12,20,30,11,25}, m1=4.75,m2=19.6
•   K1={2,3,4,10,11,12},K2={20,30,25}, m1=7,m2=25
•   Stop as the clusters with these means are the same.
4
--- page 5 ---
Q3
a) How does SVM find the optimal separating hyperplane for binary classification? Explain how SVM
uses the kernel trick to handle non-linearly separable data.
Ans: SVM finding optimal separating hyperplane carries 5 marks and any two SVM kernel tricks
carries 5 marks
• A SVM which is used to classify data which are linearly separable is called linear SVM.
•   In other words, a linear SVM searches for a hyperplane with the maximum margin.
•   This is why a linear SVM is often termed as a maximal margin classifier (MMC).
5
--- page 6 ---
@ In matrix form, a hyperplane thus can be represented as

W.X+b=0 (4)

where W =[Wy,W2
constant.

Xm] and bis a real

@ Here, W and b are parameters of the classifier model to be
evaluated given a training set D.

Figure 4: Computation of the MMH

A by +
* te toiy + +t
++ +

Ay

e@ Let us consider a two-dimensional training set consisting two
classes + and - as shown in Fig. 4.

e@ Suppose, 6; and bz are two decision boundaries above and below
a hyperplane, respectively.

e@ Consider any two points X, and X_ as shown in Fig. 4.

e@ For X. located above the decision boundary, the equation can be
written as

W.X,+b=K where K > 0 (5)

e@ Similarly, for any point X_ located below the decision boundary,
the equation is

W.X_+b=k’ where K’ <0 (6)

e Thus, if we label all +’s are as class label + and all -’s are class
label -, then we can predict the class label Y for any test data X as

_f + ifWxX+b>0
m={t ifwW.x+b<0
--- page 7 ---
Non Linear SVM 5 Marks
Kernel functions:
The kernel function is a technique used to transform data into a higher dimension to make it easier to
classify when the data is not linearly separable in its original space.
Common kernel functions include:
•   Linear Kernel: No transformation; works directly in the input space.
•   Polynomial Kernel: Adds polynomial features.
•   Radial Basis Function (RBF) Kernel: Maps data into infinite dimensions using a Gaussian
function.
•   Sigmoid Kernel: Similar to a neural network activation function.
7
--- page 8 ---
•
If we cannot draw a straight line (or hyperplane) to separate the classes in the input space, SVM
needs a non-linear boundary. Using the Kernel trick, z=x2+y2 is used to handle non-linear data.
b) Logistic Regression models the probability of a binary outcome using the logistic (sigmoid) function
carries 5 marks
Logistic Regression models the probability of a binary outcome (e.g., Yes/No, 1/0) by using
the logistic function, also known as the sigmoid function, to map the output of a standard
linear equation into the range of [0,1].
Here is a breakdown of the three key steps:
1. The Linear Model (The "Input")
8
--- page 9 ---
Like Linear Regression, Logistic Regression begins by calculating a linear combination of the
input features (x) and their corresponding weights (β), plus an intercept (β0 or b). This
intermediate result is often denoted as z and is called the log-odds or the logit.
2. The Sigmoid Transformation
This is where the logistic (sigmoid) function comes in. Its purpose is to transform the unbounded
linear output (z) into a value that is strictly bounded between 0 and 1, which can then be interpreted
as a probability.
3. Interpreting the Log-Odds (z) and Probability (P)
The sigmoid function ensures that:
Linear Output (z)   Sigmoid Output (P) Interpretation
z→∞ (Very large positive) P→1   The outcome is almost certain to be 1.
z=0   P=0.5   The outcome is equally likely to be 0 or 1.
z→−∞ (Very large negative) P→0   The outcome is almost certain to be 0.
Numerical on Logistic Regression Carries-5 marks
A company wants to predict whether a candidate will get selected for a job based on the number of
hours they spent preparing for the interview.
The log of odd value is given as: log⁡(odds) = 𝑧= −10.985 + 0.4395 × Hours
i) Calculate the probability that a candidate who prepared for 28 hours will be selected. ii) Determine
the minimum number of hours a candidate should prepare to have a probability of selection of at least
90%.
Ans:
1   1
𝑃=   =   ≈0.789
1 + 𝑒−1.318 1 + 0.268
9
--- page 10 ---
For 28 hours=0.789
13.182
𝑋=   ≈30 hours
0.4394
So, a candidate should prepare at least 30 hours to have ≥ 90% chance of selection.
First part 5 marks,
Second part 5 marks
Q4
a) A Python program to perform the following operations using pandas. (i)Read the CSV file into a Data
Frame. (ii)Display the first 5 records. (iii)Display the number of rows and columns. (iv)Identify
missing values and replace with mean values (v) Perform one-hot encoding on the Department
column.
Each Operation Carries 2 marks
Employee.CSV file
Emp Id Name Age Department Salary Gender
101   Raj   28   HR   45000 Male
102   Meena 32   IT   60000   Female
103   Karan NaN Finance   52000 Male
104   Priya   29   IT   NaN   ,Female
105   Amit   35   HR   48000 Male
1. Reading the CSV into a DataFrame — Bloom: Remember / Understand
o Uses pd.read_csv('employee.csv') correctly and assigns to a DataFrame.
2. Displaying the first 5 records — Bloom: Remember
o Full (1.0): Uses df.head() or df.head(5) and shows output.
3. Finding number of rows and columns — Bloom: Understand
Uses df.shape (or len(df) & df.shape[1]) and reports correctly.
4. Identifying missing values — Bloom: Analyze
o   Uses df.isnull().sum() (or equivalent) and identifies the missing entries in
Age and Salary.
5. Replacing missing Age with mean — Bloom: Apply
o Full (1.5): Computes mean from non-missing ages, uses e.g.
df['Age'].fillna(df['Age'].mean(), inplace=True) and shows updated
values (correct mean used).
6. Replacing missing Salary with median — Bloom: Apply
o Full (1.5): Computes median from non-missing salaries and fills NaN correctly
(e.g., df['Salary'].fillna(df['Salary'].median(), inplace=True))..
7. One-hot encoding Department — Bloom: Apply / Create
10
--- page 11 ---
o Full (1.5): Uses pd.get_dummies(df['Department'],
prefix='Department') or pd.get_dummies(df,
columns=['Department']), correctly appends/replaces columns and drops
original if required. All department categories handled.
b) Design Dendrogram and form clusters by applying Agglomerative algorithm with the following data
stored in adjacency distance matrix using single link approach and complete link technique.
Designed of Dendrogram with single link carries 5 marks by solving adjacency matrix at every level
by single link distance.
11
--- page 12 ---
Designed of dendrogram using complete link with steps carries 5 marks by solving adjancy matrix at
every level.
12
--- page 13 ---
Q5
a) Explain the major 4 challenges faced in Unsupervised Learning and illustrate each challenge with
suitable examples.
Four challenges with explanation carries 2 marks each and example carries 2 marks(4*2+2=10)
Point   Explanation   Marks
No predefined labels make it
1. Lack of Ground   difficult to evaluate model
1.5
Truth / Labels   performance or validate cluster
quality.
2. Determining the   Algorithms like K-Means require k
Right Number of   as input; choosing optimal k is   1.5
Clusters or Groups   challenging.
It’s often unclear what each cluster
3. Interpretability of
or pattern represents in real-world   1
Results
terms.
4. Sensitivity to   Many algorithms (e.g., K-Means)
Initialization /   depend on initial centroid selection, 1
Parameters   leading to different outcomes.
In high dimensions, distances
5. Handling High-
become less meaningful (curse of   1.5
Dimensional Data
dimensionality).
6. Noisy or   Noise and outliers can distort
1
Overlapping Data   clusters and reduce accuracy.
13
--- page 14 ---
Algorithms may become
7. Scalability Issues   computationally expensive for large 1
datasets.
Choosing metrics like silhouette
8. Evaluation Metrics   score, Davies–Bouldin index, etc., is 1.5
non-trivial.
b) Design a Decision Tree for the given dataset using the ID3 algorithm. Calculate the entropy and
information gain for each attribute. Find the best root node. Mention the steps clearly. All the answers
to be mentioned to the 4th decimal.
Best rootnode=Study hours
Entropy of the entire dataset 1 marks, 3 marks each for gain calculation of 3 independent variables.
14
--- page 15 ---
Study
Attendance Homework Result
Hours
High   Regular   Yes   Pass
High   Irregular   No   Pass
Medium Regular   Yes   Pass
Low   Regular   No   Fail
Low   Irregular   No   Fail
Medium   Irregular   No   Fail
Medium Regular   No   Pass
High   Regular   No   Pass
Low   Regular   Yes   Fail
High   Irregular   Yes   Pass
15
--- page 16 ---
Q6
a) Answer
Predicted:   Predicted:   Predicted:
Brain Tumor Type
Glioma (0)   Meningioma (1)   Pituitary (2)
Actual: Glioma (0)   5   2   1
Actual: Meningioma
1   6   1
(1)
Actual: Pituitary(2)   0   2   2
From this matrix we can compute metrics:
For Class 0 (Glioma): 2.5 marks
• TP = 5 (correctly predicted Apples)
• FP = 1 + 0 = 1
• FN = 2 + 1 = 3
• TN = 20 - (TP+FP+FN) = 20 - 9 = 11
So,
•   Precision (Glioma) = TP / (TP+FP) = 5 / (5+1) = 0.833
•   Recall (Glioma) = TP / (TP+FN) = 5 / (5+3) = 0.625
For Class 1 (Meningioma): 2.5 marks
• TP = 6
• FP = 2 + 2 = 4
• FN = 1 + 1 = 2
• TN = 20 - (6+4+2) = 8
So,
•   Precision (Meningioma) = 6 / (6+4) = 0.6
•   Recall (Meningioma) = 6 / (6+2) = 0.75
For Class 2 (Pituitary): 2.5 marks
• TP = 2
• FN = 2
• TN = 20 - (2+2+2) = 14
16
--- page 17 ---
So,
•   Precision (Pituitary) = 2 / (2+2) = 0.5
•   Recall (Orange Pituitary = 2 / (2+2) = 0.5
Overall Accuracy 1 marks
•   Accuracy=Correct PredictionsTotal Predictions\t{Accuracy} =
Predictions}}Accuracy=Total PredictionsCorrect Predictions
•   Correct predictions = diagonal sum = 5 + 6 + 2 = 13
Total = 20
•   Accuracy=13/20=0.65=65
Justification carries 1.5 marks
b)
Apply Naïve Bayesian Algorithm to classify incoming tuple T
T={Age=Old, Competition=Yes, Industry=Hardware} as Low or High
Marks mentioned against the solved problem
17
--- page 18 ---
Q7
A The sale of company in million dollars for each year are shown in table:
X(Years)   2005   2006   2007   2008   2009
Y (Sales)   12   19   29   37   45
Find
a. Least Square Regression Line y=ax+b
b. Use Least Square Regression Line as a model to estimate sale of company in 2012
Compute the Mean Squared Error (MSE) for the given data using the obtained regression model.
Analyze and comment on the performance and accuracy of the model based on the calculated MSE
value.
18
--- page 19 ---
Least square Regression line 5 marks, Estimate sale 2 marks, MSE calculation 2 Marks, Inference 1
Marks
Regression Line 𝑦= 8.4𝑥+ 3.2
Estimated Sale (2012) $70.4 million
Mean Squared Error (MSE)   0.32
19
--- page 20 ---
(b) Estimate sale in 2012—2marks

For 2012: x = 2012 — 2005 = 7.

Peo12 = 8-4(7) + 11.6 = 58.8 + 11.6 = [70.4 million $

(c) Find MSE and comment— 2 marks for MSE and 1 mark for
inerence

First compute predicted values and residuals for the data:

Year x Actual y Predicted # = 8.4x + 11.6 Residual e = y —# e7

2005 0 12.0 11.6 +0.4 0.16
2006 1 19.0 20.0 —1.0 1.00
2007 2 29.0 28.4 +0.6 0.36
2008 3 37.0 36.8 +0.2 0.04
2009 4 45.0 45.2 —0.2 0.04

Sum of squared errors (SSE):

SSE = Fe* = 0.16 + 1.00 + 0.36 + 0.044 0.04 = 1.60

MSE (mean squared error, using nfor average prediction error):

SSE 1.60 “aqe z
MSE = === 0.32 (million $)
nm

RMSE (for interpretability in dollars):

RMSE = VMSE = ¥V0.32 * [0.57 million $

(If instead estimating residual variance for inference, use n — 2 = 3in
denominator: s* = 1.60/3 © 0.533and s * 0.73.)

Comment on performance (based on MSE)

« MSE=0.32 means the average squared prediction error is 0.32 (:

« Compared to sales values (12-45 million), an average error of about
$0.57 million is very small.

« Therefore the linear model fits the data very well and 1s appropriate
for prediction in this range (subject to usual caveats about
extrapolation — e.g.. predictions far beyond observed years may be

less reliable).

20
--- page 21 ---
b   Explain any 2 types of cross validation techniques to improve the performance of machine learning
model, to deal with problem of model overfitting and underfitting.
Ans: Each Technique carries 5 marks along with figures
1. K fold cross validation
• The dataset is split into K equal parts (folds).
• The model is trained on 20-80, 30-70, 50-50, 70-30 etc
•   This process repeats K times, each time using a different fold for testing.
•   Final performance = average of all K test results.
• The model is tested on multiple different subsets, preventing it from memorizing one
particular train-test split.
• Ensures good generalization.
• Uses a large portion (K–1 folds) for training each time, giving the model more data to
learn from.
2. Stratified K-Fold Cross Validation
(Useful especially in classification problems, e.g., heart disease dataset)
•   Similar to K-Fold, but ensures each fold has the same class proportion as the
original dataset.
Example: If original dataset has 60% class 0 and 40% class 1, each fold maintains the
same ratio.
•   Prevents training on folds with skewed class distribution.
• Ensures the model does not learn patterns that are biased toward one class.
• Balanced folds help the model learn representative patterns from minority classes.
21
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper c8aa1fb20c72

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CSE_DS_7011/Machine Learning/ANS_Machine Learning(702DB0C015)_2025-2026.pdf`
- Text: ocr (12 pages), mean OCR confidence 34.0
- 6 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
l
--- page 2 ---
= \— 0 6051
= 073949

_

Back propagabe eps

A Bheaaeng demmig Rokk “1:
Ani = 4 S} Of -
tL banteg 2
iy oad HRM
Or = olf volt
g. 2 0;(1° 91 yoo) AP
g BD drdder

j (te 65) xh AN ate

gz °
Badeword fon :
Exar ot 3 tang ~ ©
ves, 2 Os L173) (eae ’
_ 6-605) (1-07 605! (\ — 076051)
_ 0° 0343
or on 0°59 38
Nvgg, = “1 $3 = TE”
~— 00554

N93 (new) = Wa3z(eld
~ oy + 010559 = O24 55F
--- page 3 ---

--- page 4 ---
F

gp
As)

arled lobo po ke.
ie, Qa, as, B® 40, 35, 4)

( 14) 1s)
Lie Tyee
C,=\5 C22 AaS- C32 8S.
12 AQ yo
30
{QAIBHIS 2.242820 TF otas
—a S se
cE Ly 2°
New.
mewkiol 4
a Ameer 4
G\ = 1S Co = 9420 aad 33S ,
nen) = new
Therion - L
(9, 1118 ad )25,*+8, 80 205uD .


ae charts macy $2) 1518

C2 $ 22, 2S, LS, 304 ,

CBD 35, 4of,
--- page 5 ---
rcbabikly = 18 Qu-

S) wher Probably = 0165

Pa 0°6S
!
Poe She Se:
\- a fh te Sex)

Pur dogcvic-
--- page 6 ---
JP > wMwxte

O64 = Hye OSH”
61% =
ee

oS

9. Q+D28
--- page 7 ---
-%C%)

Age 450°
Medron = @ariec) | a 2 = IQ
Q, = Qi
(Qs > 10S TOR + [oS-9Q 213
Ow kn gue :
Drhy
7) atk r
--- page 8 ---
4 {2)

Slobe (>)
be 2x8) ys) ee
Fox G = Mian fy,
a 550 22D. Ke is
900 4 = 66°
bo = ye
be = 33.
ganakon iv, Yo 29% i

bin be

64 b)

pow Me 1k, fog arb
Saly 2 ys gran Fem 2°

= $9 2600 60
--- page 9 ---
A (») 5
jf —- \ ? %o Py Ps
7 \ \ \
% pels \ © \ :
0. 02503 003 = oO
oe °
Py, 0 +430 xx 0
oo 118 01323 owe ©
5 Ot
ae -
a 0 aCe) ‘
Peo peUs\ ° Cee) oe
. O iM: ° 3) ote
( % £u) o:¥30 o 1 aaa
vo 0133 93)* (PsPa) Pr
S
P yea (Ps Pe) (Pash)
oo F138 1-614
(ee) be
P58 Ju, 05
= pebgr 03%
(Parent)
peust oll& -
(P, Pa) Pr
(3 @) Ps
6:7173 7 0° 338
(#1 0 os
pete

(09.0 tui g
Ooo tuck) oO O (Pr iPs) Fy Pos) &
--- page 10 ---

--- page 11 ---
Ha)
agin
Jo
_ _ \\
2) Robt ro _
%) stohi le hy ~
\
) wmtidura in prtol
“Uou .
--- page 12 ---
Q-4
(? -

Evrropy = ¥ (s)= - p,Aeda? — Peas? -

of, ees — & teoho

~ 04, —
lo Je lO

wR o19404

eo
—oo

Flan ky he furan , |
~ 03, + ~ ho 3

= or ela
3
(bare) 2 - AIG - bee
= 18
teeg OBNZ
" evita) (Premios) ae +4
H ( 5|tlen=— . gaus
ah (Plan) = w OS) - 4 (5\ tox)
= O 9304-08
2 of 0ybul
44( s\ea) ~ 97 36eF
toCcatts) = 9° 6034v wo
= 02 3709 sews
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper b64cde8cf857

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (22 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (EXTC)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Question No.1 is compulsory.
3. Out of remaining questionsa attempt any 4 questions.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figure in brackets on the right hand side indicates full marks.
7. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Define overfitting using an example. Explain its significance.   [05]
SO-   Solution:
1;   Overfitting :
BL   When a machine learning model provides correct predictions for training data but not for
-2   new data, this is known as overfitting, an undesirable machine learning tendency. Data
scientists first train machine learning models on a known data set before using them to
make predictions. The model then attempts to forecast results for fresh data sets using this
information. An overfit model cannot function properly for all kinds of incoming data and
may produce erroneous predictions.
02 Marks
Why?
Overfitting happens when a model sticks too closely to the training data and struggles to
handle new data. Basically, it memorizes the details and noise instead of learning the
actual patterns. This usually comes up for a few reasons. Sometimes, you just don’t have
enough training data, so the model can’t really get a sense of everything it needs to know.
Or maybe the training data has too much random or irrelevant information—what’s called
noisy data—which confuses the model. Training a model for too many rounds on the
same dataset also makes things worse, since it just keeps picking up more noise with each
pass. And if the model itself is too complicated, it tries to capture every tiny detail, even
the ones that don’t matter. That’s why overfitting is such a common headache in machine
learning.
Example: Consider a use case where a machine learning model has to analyze photos and
identify the ones that contain dogs in them. If the machine learning model was trained on
a data set that contained majority photos showing dogs outside in parks , it may may learn
to use grass as a feature for classification, and may not recognize a dog inside a room.
03Marks
CO-1; SO-   b. A dataset contains product categories: Car, Bike, Bus, Car, and Bike. Apply One-Hot   [05]
1;   Encoding to convert this categorical data into numerical format and explain why
BL   assigning simple numeric labels may lead to incorrect interpretations.
-4
********** 1 **********
--- page 2 ---
Solution:
Apply One-Hot Encoding to convert this categorical data into numerical format- 2 marks
explain why assigning simple numeric labels may lead to incorrect interpretations.3
marks
03Marks
One-Hot Encoding converts categorical values into binary vectors, where only one
position is marked as 1 and the rest are 0. This ensures that each category is treated as
independent and equally important.
If we instead assign simple numeric labels such as:
Car = 1, Bike = 2, Bus = 3,
it may lead to incorrect interpretations. Machine learning models may assume an
ordinal relationship (e.g., Bus > Bike > Car), which is not meaningful because these
categories do not have any inherent order.
2Marks
CO-2; SO-1;   c.   Under what circumstances are Precision, or Recall better performance metrics in   [05]
BL-2   comparison with accuracy? Give an example each for the situations where “Recall is a
more important evaluation metric than Precision”.” Precision is a more important
evaluation metric than Recall”.
Solution:
When are Precision or Recall better than Accuracy?
Accuracy works well only when classes are balanced and errors have equal cost.
But in many real-world problems (like **Cancer detection or spam filtering), data is
imbalanced and mistakes have different consequences.
Use Recall when:
• Missing a positive case is very dangerous
• You want to capture as many actual positives as possible
•   False negatives must be minimized
Example:
Disease Detection (e.g., Cancer Screening)
•   If a patient has cancer but the model predicts negative → very risky
•   It’s better to flag more people as positive (even if some are wrong)
•   So, Recall is more important
********** 2 **********
--- page 3 ---
Use Precision when:
•   False positives are costly or harmful
• You want predictions to be highly accurate when positive
• Avoid wrongly labeling negatives as positives
Example:
Email Spam Detection
•   If a normal email is marked as spam → important message may be lost
•   So, predictions labeled “spam” should be very accurate
• Hence, Precision is more important
Summary Table
Metric   Focus   Important When   Example
Minimize False   Missing positive is   Cancer
Recall
Negatives   dangerous   detection
Minimize False   Spam
Precision   False alarms are costly
Positives   filtering
1Mark for each explanation
CO-2; SO-2;   d. Discuss the computational complexity of K-Means and Hierarchical Clustering and its   [05]
BL-2   impact on scalability.
Solution:
K_Means and Hierarchical Clustering: 02 M
Comaparison: 03 M
K-Means is an iterative algorithm.
• Time Complexity:
O(n × k × t × d)
where:
o n = number of data points
o k = number of clusters
o   t = number of iterations
o d = number of features
• Each iteration assigns points to nearest centroid → O(n × k)
• Updating centroids → O(n)
• Repeated for t iterations
Hierarchical clustering builds a tree (dendrogram).
• Time Complexity:
O(n² log n) (optimized) or up to O(n³) (naive)
********** 3 **********
--- page 4 ---
• Space Complexity:
O(n²) (distance matrix)
• Computes pairwise distance matrix → O(n²)
• Repeated merging/splitting of clusters
• Updating distances after each merge
Clustering algorithms differ significantly in computational complexity, which directly
impacts their scalability to large datasets.
K-Means Clustering is relatively efficient and scalable. Its time complexity is
approximately O(n × k × i × d), where n is the number of data points, k is the number of
clusters, i is the number of iterations, and d is the number of features. Since k and i are
usually small, K-Means scales well to large datasets and is widely used in real-time and
big data applications.
In contrast, Hierarchical Clustering (especially agglomerative) has much higher
complexity. Its time complexity is typically O(n² log n) or even O(n³) depending on
implementation, and space complexity is O(n²) due to the need to store distance matrices.
This makes it computationally expensive and less suitable for large datasets.
Impact on scalability:
• K-Means is highly scalable and suitable for large-scale datasets (millions of
points).
•   Hierarchical clustering is limited to smaller datasets due to its high computational
and memory requirements.
Complexity: 02 M
•   Explanation with scalability: 03
1 Mark for each correct step
Q2   a.   The following table records the number of balls that Ayush took for scoring runs. In   [10]
CO-2;   how many balls is he likely to score a century?
SO-
2;   Runs   Number of
BL-   Scored   Balls
4   8   10
35   20
47   31
54   23
11   5
85   47
84   35
93   67
89   73
2   1
Solution:
********** 4 **********
--- page 5 ---
x = Runs scored
y = Number of balls
We need to predict the number of balls required when Ayush scores 100 runs.
We use the linear regression model:
y = mx + b,
where y and x are variables,
m is the slope, and
b is the y-intercept.
The equations for m and b are as below -
m = (n∑xy - ∑y∑x)/[n∑x2 - (∑x)2]
b = (∑y - m∑x)/n
∑xy = 23199
∑y = 312
∑x = 508
∑x2 = 37390
(∑x)2 = 508*508
m = (n∑xy - ∑y∑x)/[n∑x2 - (∑x)2]
= (10*23199-312*508) / [10*37390-(508*508)]
m = 0.634466
b = (∑y - m∑x)/n
b= (312-0.634466*508)/10
b = -1.03087
The equation will be –
Y = 0.634466*X + (-1.03087)   08 Marks
Predict balls for 100 runs i.e.x=100
Substitute x=100 in regression line equation.
Y = 0.634466*100 + (-1.03087) = 62.41573
Ayush requires 62 balls to score 100 runs.
2Marks
Q2   b. Explain how nonlinear data can be classify using SVM? Explain different kernel   [10]
CO-2; SO-2;   functions used classification.
BL-2   Solution:
If the dataset is not linearly separable, SVM uses a nonlinear decision boundary
to classify the data. This is called a nonlinear SVM.
1Mark
Key Idea-
Instead of drawing a straight line, nonlinear SVM:
• Transforms the data into a higher-dimensional space
• Uses a kernel function to make the data separable
• Then finds a linear boundary in that higher dimension, which appears
nonlinear in original space
•   1Mark for each explanation (04)
********** 5 **********
--- page 6 ---
Kernal functions are used to deal with nonlinear SVM
Explanation how nonlinear SVM is analyzed using kernel function:
Different types of kernel functions are:
i) Homogeneous polynomial kernel
ii) Non-homogeneous polynomial kernel
iii) Radial basis function
iv) Sigmoid kernel function
1Mark for each explanation of kernel function with equation
(05)
Q3   a. A company analyzes employee attrition using the following dataset:   [10]
CO-3;
SO-6;
BL-3   Experience   Satisfaction   Leave
High   Low   Yes
High   Medium   No
Medium   Low   Yes
Low   Medium   No
Low   High   No
Medium   High   No
Apply ID3 algorithm to:
•   Calculate Entropy of target variable
• Compute Information Gain of attributes
•   Identify the root node
Solution:
Step 1: Dataset Summary
Total samples = 6
Target (Leave):
• Yes = 2
• No = 4
Step 2: Entropy of Target Variable
[
Entropy(S) = - (2/6)\log_2(2/6) - (4/6)\log_2(4/6)
]
[
= - (0.333)(-1.585) - (0.667)(-0.585)
]
[
= 0.528 + 0.390 = 0.918
********** 6 **********
--- page 7 ---
]
Entropy(S) = 0.918
03Marks
Step 3: Information Gain Calculations
(A) Attribute: Experience
Ye N Tota
Experience   Entropy
s   o   l
High   1 1 2   1
Medium   1 1 2   1
Low   0 2 2   0
[
Weighted = (2/6)(1) + (2/6)(1) + (2/6)(0)
]
[
= 0.333 + 0.333 + 0 = 0.666
]
[
IG(Experience) = 0.918 - 0.666 = 0.252
]
IG(Experience) = 0.252
03Marks
(B) Attribute: Satisfaction
Ye N Tota
Satisfaction   Entropy
s   o   l
Low   2 0 2   0
********** 7 **********
--- page 8 ---
Medium   0 2 2   0
High   0 2 2   0
[
Weighted = (2/6)(0) + (2/6)(0) + (2/6)(0) = 0
]
[
IG(Satisfaction) = 0.918 - 0 = 0.918
]
IG(Satisfaction) = 0.918
03Marks
Step 4: Root Node Selection
•   IG(Experience) = 0.252
•   IG(Satisfaction) = 0.918
Root Node = Satisfaction (highest IG)
01Mark
Q3   b. A hedge fund analyzes 200+ financial indicators (prices, volatility, macroeconomic   [10]
CO-1;   factors). The dataset suffers from multicollinearity and noise, leading to unstable
SO-1; BL-2   predictive models.
Tasks:
1. Explain how PCA can address multicollinearity in this dataset.
2. How would you decide the number of principal components to retain?
3. Discuss potential risks of using PCA in financial decision-making.
Solution:
A hedge fund often works with a very large number of financial variables such as stock
prices, returns, volatility measures, interest rates, inflation, exchange rates, sector indices,
and macroeconomic indicators. In such datasets, many variables are highly correlated
with each other. This creates multicollinearity, which makes predictive models unstable.
Also, noisy and redundant features increase computational complexity and reduce model
reliability.
Principal Component Analysis (PCA) is a dimensionality reduction technique that can
help solve these issues by transforming the original correlated variables into a smaller set
********** 8 **********
--- page 9 ---
of new uncorrelated variables called principal components.
1. How PCA can address multicollinearity in this dataset
Meaning of multicollinearity
Multicollinearity occurs when two or more input variables are strongly correlated. In
finance, this is very common because many indicators move together.
For example:
•   stock price and moving average may be strongly related
•   inflation and interest rate may influence each other
•   sector indices may follow the same market trend
When multicollinearity exists:
• model coefficients become unstable
•   small changes in data can produce large changes in predictions
•   interpretation of variable importance becomes difficult
•   regression models may overfit or behave inconsistently
How PCA solves this
PCA transforms the original set of correlated features into a new set of variables called
principal components.
These principal components have two key properties:
1. They are linear combinations of original variables
2. They are uncorrelated with each other
So, instead of directly using 200 correlated financial indicators, the hedge fund can use a
smaller number of principal components that summarize the major patterns in the dataset.
Why this reduces multicollinearity
Since the principal components are orthogonal, there is no correlation among them. This
removes the multicollinearity problem.
Practical effect in hedge fund modeling
Using PCA:
•   correlated indicators are compressed into a few market factors
•   regression or prediction models become more stable
•   estimation becomes more reliable
•   redundant information is removed
•   noise can be reduced by discarding less important components
********** 9 **********
--- page 10 ---
Example intuition
Suppose many indicators reflect overall market movement. PCA may combine them into
one principal component representing market trend. Another component may capture
volatility behavior. A third may represent macroeconomic pressure. Thus, instead of
200 raw variables, a model may work with 10–20 meaningful components.
2. How to decide the number of principal components to retain
Choosing the correct number of principal components is very important. If too few are
kept, useful information may be lost. If too many are kept, noise and redundancy may
remain.
Several methods are used:
A. Explained Variance Criterion
Each principal component explains some portion of the total variance in the data.
• The first component explains the maximum variance
• The second explains the next highest variance
• and so on
A common rule is to retain enough components to explain 80% to 95% of the total
variance.
In finance
A hedge fund may choose enough components to explain around 90%–95% variance,
especially when trying to preserve important market structure.
Advantage
• Simple and widely used
• Gives a quantitative basis for selection
Limitation
• High explained variance does not always mean high predictive usefulness
B. Scree Plot Method
A scree plot shows eigenvalues versus component number.
• The curve usually drops sharply at first
• Then it begins to flatten
The point where the curve starts flattening is called the elbow point. Components before
this point are usually retained.
********** 10 **********
--- page 11 ---
Meaning
Beyond the elbow, extra components add only small amounts of information and may
mainly represent noise.
C. Kaiser Criterion
According to this rule, keep components with eigenvalue greater than 1.
Reason
An eigenvalue greater than 1 indicates that the component explains more variance than an
individual standardized original variable.
Limitation
This rule is more useful in moderate-sized datasets and may not always be ideal for large
financial datasets.
D. Cross-Validation / Model Performance
A more practical approach is to try different numbers of principal components and test the
predictive model performance.
For example:
•   train model with first 5 components
•   then with 10 components
•   then with 15 components
• compare prediction accuracy, stability, and risk metrics
3. Potential risks of using PCA in financial decision-making
Although PCA is useful, it also has important risks, especially in finance where decisions
involve high uncertainty and financial loss.
A. Loss of Interpretability
The original variables are easy to understand, such as inflation, interest rates, or stock
returns. But principal components are combinations of many variables.
This makes interpretation difficult.
Risk
A portfolio manager may not clearly understand what a principal component
economically represents. This can reduce trust in the model.
B. Important Low-Variance Features May Be Discarded
********** 11 **********
--- page 12 ---
PCA keeps components with the highest variance and removes low-variance components.
However, in finance, some low-variance variables may contain important predictive
signals.
Example
A small but consistent macroeconomic indicator may have low variance but still be very
useful for forecasting a crisis.
Risk
Discarding such components may harm prediction quality.
01Mark for each correct explanation (10 steps must be written)
Q4   a. A regression model gives a high R-squared value but poor predictive accuracy.   [10]
CO-2;
SO-   Analyse this situation and relate it to potential issues such as overfitting or data
2;   distribution.
BL-   Solution:
2   A regression model may show a high R-squared value but still have poor predictive
accuracy when it fits the training data well but fails to generalize to new or unseen
data. This means the model explains a large proportion of variance in the available
dataset, yet its practical prediction performance is weak.
Meaning of high R-squared
R-squared measures the proportion of variation in the dependent variable explained
by the independent variables. A high value suggests that the model fits the observed
data closely.
However, a good fit on test data does not always guarantee good prediction on test
data.
Overfitting as a major reason
One common reason is overfitting. Overfitting occurs when the regression model
learns not only the true pattern in the data but also the random noise. This usually
happens when:
•   too many predictors are included,
•   higher-order polynomial terms are used unnecessarily,
•   the model becomes too complex for the size of data.
********** 12 **********
--- page 13 ---
In such cases, the model performs very well on training data, giving a high R-squared,
but performs poorly on test or validation data.
Problems related to data distribution
Poor predictive accuracy may also arise because of data distribution issues.
Examples include:
a) Training and test data mismatch
If test data has a different distribution from training data, the model may not work
well even if training fit is excellent.
b) Presence of outliers
A few extreme values can distort regression coefficients and create misleadingly high
goodness-of-fit.
c) Non-linearity
If the true relationship is not linear but a linear regression model is applied, R-squared
may appear acceptable on one dataset but prediction may fail on others.
d) Heteroscedasticity
When error variance is not constant, predictions become unreliable across different
ranges of input values.
01Mark for each correct explanation
Q4   b. The 2×2 Image given bellow is applied to the fully connected neural network with   [10]
CO-3;
SO-6;   sigmoid activation function. calculate the following
BL-6
a. Predicted output after first epoch.
b. Mean square error after first epoch.
c.   If learning rate of 0.05 find the updated value of weight W14 using error
back propagation algorithm.
Assume bias at hidden layer neurons b1=0.30, and bias at output layer neuron
b2=0.50 and weights are given in following table.
W1   W2   W3   W4   W5   W6   W7   W8   W9   W10   W11   W12   W13   W14   W15
0.10   0.20   0.30   0.40   0.50   0.60   0.70   0.80   0.90   0.65   0.75   0.95   0.75   0.55   0.85
Inputs applied to the input layer is
X1   X2   X3   X4
0.40   0.55   0.65   0.85
********** 13 **********
--- page 14 ---
Solution:
Input to neural network are we convert 2D image in to 1D image by converting rows
in to columns so the inputs to neural network are x1=0.40,x2=0.55,x3=0.65,x4=0.85
Predicted output after first epoch
a. h11in=b1+w1x1+w4x2+w7x3+w10x4 =1.5575
h11out=1/(1+e- h11in)=0.4627
b. h12in= b1+w2x1+w5x2+w8x3+w11x4 =1.8125
h12out=1/(1+e- h12in)=0.3555
c. h13in=b1+w3x1+w6x2+w9x3+w12x4 =2.1425
h13out=1/(1+e- h11in)=0.3182
d. O1in=b2+w13 h11out +w14 h12out +w15 h13out =1.3129
O1out=1/(1+e- O1in)=0.4323
05Mark
Mean square error after first epoch
Mean Square error after first epoch =1/2[(O1-T1)2]= 1/2[(O11out -T1)2=]
= 1/2[(0.4323 -0.82)2]
Mean Square error after first epoch =0.0.0751
02Mark
If learning rate of 0.05 find the updated value of weight w14 using error back
propagation algorithm.
w14New=0.5481
Steps for updating weight
********** 14 **********
--- page 15 ---
03Mark
Q5   a. Explain Ensemble Learning. Discuss how ensemble methods improve the performance   [10]
CO-3;   of Decision Trees.
SO-
1;   Solution:
BL   Ensemble Learning
-3
Ensemble Learning is a technique where multiple models are combined to improve
overall performance.
Instead of relying on a single model, multiple weak learners are used to create a
strong learner.
Types of Ensemble Methods
********** 15 **********
--- page 16 ---
1. Bagging
2. Boosting
3. Random Forest
How Ensemble Improves Decision Trees
Decision Trees suffer from:
• High variance
•   Overfitting
Ensemble methods solve these issues:
1. Bagging (Bootstrap Aggregation)
•   Multiple datasets created using sampling with replacement
•   Train separate trees
•   Final output = majority voting / averaging
Reduces variance
2. Random Forest
• Extension of bagging
• Random feature selection + multiple trees
More robust and less correlated trees
3. Boosting
• Models trained sequentially
• Focus on correcting previous errors
Examples:
• AdaBoost
********** 16 **********
--- page 17 ---
• Gradient Boosting
Reduces bias + variance
1 Mark for each correct steps/explanation
Q5   b. Implement K-Means clustering with K = 3 on the following dataset. Use the first three [10]
CO-2;
SO-2;   points as the initial cluster centroids and apply Euclidean distance to assign points to
BL-2
clusters. Perform two iterations of the algorithm. Show:
1. Initial centroids
2. Distance calculations
3. Cluster assignment after each iteration
4. Updated centroids
5. Final grouping after two iterations.
The Dataset is: {(2,4),(3,5),(4,6),(8,8),(9,9),(10,10),(15,3),(16,4),(17,5)}
Solution:
Step 1: Initial Centroids
Since the first three points are taken as the initial centroids:
• C1=(2,4
•   C2=(3,5)
•   C3=(4,6)
Dataset: (2,4), (3,5), (4,6), (8,8), (9,9), (10,10), (15,3), (16,4), (17,5)
Initial Centroids: C1 = (2,4) C2 = (3,5) C3 = (4,6)
Iteration 1: Cluster 1: (2,4) Cluster 2: (3,5) Cluster 3: (4,6), (8,8), (9,9), (10,10), (15,3),
(16,4), (17,5)
Updated Centroids:
05Mark
********** 17 **********
--- page 18 ---
C1 = (2,4) C2 = (3,5) C3 = (11.29, 6.43)
Iteration 2: Cluster 1: (2,4) Cluster 2: (3,5), (4,6) Cluster 3: (8,8), (9,9), (10,10), (15,3),
(16,4), (17,5)
Final Centroids: C1 = (2,4) C2 = (3.5, 5.5) C3 = (12.5, 6.5)
05Mark
Q6   a. Describe the steps involved in preparing data for a regression model. Explain the   [10]
CO-2;   importance of selecting variables, handling missing values, and checking data
SO-2;
BL-5   consistency for regression model building.
Solution:
Preparing data for a regression model involves understanding the problem, collecting
and organizing data, selecting relevant variables, handling missing values, checking
consistency, and performing cleaning and transformation. Among these, variable
selection, missing value treatment, and consistency checking are especially
important because they directly affect the accuracy, reliability, and interpretability of
the regression model. Proper data preparation forms the foundation for building an
effective regression model.
02Mark
Importance of selecting variables
Handling missing values
04Mark
Checking data consistency.
Explain all in detail..
04Mark
********** 18 **********
--- page 19 ---
Q6   b. For the data set give bellow has 10 samples Create a confusion matrix and Calculate   [10]
CO-4;   Accuracy, Precision, Recall, F1-score. Assume Car as Positive Class.
SO-
6;
BL-   No Expected/Actu
4   Predicted
.   al
1   Car   Car
2   Bike   Bike
3   Car   Bike
4   Bike   Bike
5   Car   Car
6   Bike   Car
7   Car   Car
8   Bike   Bike
9   Car   Bike
10   Bike   Car
Solution:
• TP (True Positive) → Car predicted as Car = 3 (1, 5, 7)
• TN (True Negative) → Bike predicted as Bike = 3 (2, 4, 8)
• FP (False Positive) → Bike predicted as Car = 2 (6, 10)
• FN (False Negative) → Car predicted as Bike = 2 (3, 9)
03Mark
Confusion Matrix
Predicted Car   Predicted Bike
Actual Car   TP = 3   FN = 2
Actual Bike   FP = 2   TN = 3
02Mark
Accuracy= Tp+TN/Total= 6/10 = 0.6
PRECISION=TP/TP+FP=3/5= 0.6
RECALL=TP/TP+FN=3/5= 0.6
F1=0.6
05Mark
********** 19 **********
--- page 20 ---
Q7   a. Explain Bagging and Boosting techniques in detail. Compare their working mechanisms [10]
CO-2;   and their impact on bias and variance.
SO-
2;   Solution
BL-
2   Bagging (Bootstrap Aggregation)
• Random sampling with replacement
•   Parallel model training
• Equal weight to all models
Working:
1. Create multiple datasets
2. Train models independently
3. Aggregate results
Reduces variance
Boosting
•   Sequential learning
• Each model focuses on previous errors
Working:
1. Train first model
2. Increase weight of misclassified points
3. Train next model
4. Combine weighted results
Reduces bias and variance
Comparison
Aspect   Bagging   Boosting
Training   Parallel   Sequential
********** 20 **********
--- page 21 ---
Reduce
Focus   Reduce bias + variance
variance
Data
Random   Weighted
sampling
Can overfit if not
Overfitting   Less
controlled
Example   Random Forest AdaBoost
01 Mark for each correct explanation
Q7   b. What factors should be considered while selecting a machine learning model?   [05]
CO-1;   Solution:
SO-
2;   Things to Take Into Account When Choosing a Machine Learning Model
BL-
2   The nature of the issue
Tasks involving classification, regression, or grouping
The dataset's size
Complex models are supported by large datasets, while simpler models are needed
for small datasets.
Data Quality
Model selection is impacted by the existence of noise, missing variables, and outliers.
Dimensionality of Features
Models like SVM or dimensionality reduction methods may be necessary for high-
dimensional data.
Complexity of the Model
Strike a balance between overfitting and underfitting (bias–variance trade-off).
Interpretability
Compared to sophisticated outational Cos, simple models (such decision trees and
linear regression) are simpler to understand.
Certain models, like deep learning models, demand a lot of processing power.
Measures of Performance
Depending on the issue, accuracy, precision, recall, F1-score, and RMSE
Scalability
The model's capacity to manage expanding data
0.5 Mark for each correct explanation
Q7   c. A bank analyzes transaction amounts (in ₹):   [05]
CO-1;   200, 220, 250, 270, 300, 320, 350, 400, 2000
SO-
6;   Apply the IQR method to detect any abnormal amount. Based on your findings, decide
BL-   how you should treat the extreme value.
2
********** 21 **********
--- page 22 ---
Solution:
Apply IQR 3 mark
Outlier Treatment 2 marks
To detect abnormal transaction amounts using the IQR (Interquartile Range)
method, we first arrange the data in ascending order:
200, 220, 250, 270, 300, 320, 350, 400, 2000
The total number of observations is 9. The median (Q2) is the 5th value, which is
300.
Now, we divide the dataset into two halves (excluding the median):
• Lower half: 200, 220, 250, 270 → Q1 = (220 + 250) / 2 = 235
• Upper half: 320, 350, 400, 2000 → Q3 = (350 + 400) / 2 = 375
Next, calculate the IQR:
IQR = Q3 − Q1 = 375 − 235 = 140
Now, compute the bounds:
• Lower bound = Q1 − 1.5 × IQR = 235 − (1.5 × 140) = 235 − 210 = 25
• Upper bound = Q3 + 1.5 × IQR = 375 + 210 = 585
Any value outside the range 25 to 585 is considered an outlier.
Here, 2000 > 585, so ₹2000 is an outlier (abnormal transaction).
The transaction amount ₹2000 is significantly higher than the rest of the data. The
appropriate treatment depends on the context:
•   If the transaction is legitimate (e.g., a genuine high-value transfer), it should
be retained, as it may indicate important customer behavior.
•   If it is fraudulent or suspicious, it should be flagged for investigation rather
than removed.
•   If it is due to a data entry error, it should be corrected or removed.
• For analytical purposes, we may apply capping (winsorization) by replacing
₹2000 with the upper bound (₹585) to reduce its impact on statistical models.
03 Marks
********** 22 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper c35d2e06612c

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_EXTC_7006/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (22 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (EXTC)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Question No.1 is compulsory.
3. Out of remaining questionsa attempt any 4 questions.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figure in brackets on the right hand side indicates full marks.
7. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Define overfitting using an example. Explain its significance.   [05]
SO-   Solution:
1;   Overfitting :
BL   When a machine learning model provides correct predictions for training data but not for
-2   new data, this is known as overfitting, an undesirable machine learning tendency. Data
scientists first train machine learning models on a known data set before using them to
make predictions. The model then attempts to forecast results for fresh data sets using this
information. An overfit model cannot function properly for all kinds of incoming data and
may produce erroneous predictions.
02 Marks
Why?
Overfitting happens when a model sticks too closely to the training data and struggles to
handle new data. Basically, it memorizes the details and noise instead of learning the
actual patterns. This usually comes up for a few reasons. Sometimes, you just don’t have
enough training data, so the model can’t really get a sense of everything it needs to know.
Or maybe the training data has too much random or irrelevant information—what’s called
noisy data—which confuses the model. Training a model for too many rounds on the
same dataset also makes things worse, since it just keeps picking up more noise with each
pass. And if the model itself is too complicated, it tries to capture every tiny detail, even
the ones that don’t matter. That’s why overfitting is such a common headache in machine
learning.
Example: Consider a use case where a machine learning model has to analyze photos and
identify the ones that contain dogs in them. If the machine learning model was trained on
a data set that contained majority photos showing dogs outside in parks , it may may learn
to use grass as a feature for classification, and may not recognize a dog inside a room.
03Marks
CO-1; SO-   b. A dataset contains product categories: Car, Bike, Bus, Car, and Bike. Apply One-Hot   [05]
1;   Encoding to convert this categorical data into numerical format and explain why
BL   assigning simple numeric labels may lead to incorrect interpretations.
-4
********** 1 **********
--- page 2 ---
Solution:
Apply One-Hot Encoding to convert this categorical data into numerical format- 2 marks
explain why assigning simple numeric labels may lead to incorrect interpretations.3
marks
03Marks
One-Hot Encoding converts categorical values into binary vectors, where only one
position is marked as 1 and the rest are 0. This ensures that each category is treated as
independent and equally important.
If we instead assign simple numeric labels such as:
Car = 1, Bike = 2, Bus = 3,
it may lead to incorrect interpretations. Machine learning models may assume an
ordinal relationship (e.g., Bus > Bike > Car), which is not meaningful because these
categories do not have any inherent order.
2Marks
CO-2; SO-1;   c.   Under what circumstances are Precision, or Recall better performance metrics in   [05]
BL-2   comparison with accuracy? Give an example each for the situations where “Recall is a
more important evaluation metric than Precision”.” Precision is a more important
evaluation metric than Recall”.
Solution:
When are Precision or Recall better than Accuracy?
Accuracy works well only when classes are balanced and errors have equal cost.
But in many real-world problems (like **Cancer detection or spam filtering), data is
imbalanced and mistakes have different consequences.
Use Recall when:
• Missing a positive case is very dangerous
• You want to capture as many actual positives as possible
•   False negatives must be minimized
Example:
Disease Detection (e.g., Cancer Screening)
•   If a patient has cancer but the model predicts negative → very risky
•   It’s better to flag more people as positive (even if some are wrong)
•   So, Recall is more important
********** 2 **********
--- page 3 ---
Use Precision when:
•   False positives are costly or harmful
• You want predictions to be highly accurate when positive
• Avoid wrongly labeling negatives as positives
Example:
Email Spam Detection
•   If a normal email is marked as spam → important message may be lost
•   So, predictions labeled “spam” should be very accurate
• Hence, Precision is more important
Summary Table
Metric   Focus   Important When   Example
Minimize False   Missing positive is   Cancer
Recall
Negatives   dangerous   detection
Minimize False   Spam
Precision   False alarms are costly
Positives   filtering
1Mark for each explanation
CO-2; SO-2;   d. Discuss the computational complexity of K-Means and Hierarchical Clustering and its   [05]
BL-2   impact on scalability.
Solution:
K_Means and Hierarchical Clustering: 02 M
Comaparison: 03 M
K-Means is an iterative algorithm.
• Time Complexity:
O(n × k × t × d)
where:
o n = number of data points
o k = number of clusters
o   t = number of iterations
o d = number of features
• Each iteration assigns points to nearest centroid → O(n × k)
• Updating centroids → O(n)
• Repeated for t iterations
Hierarchical clustering builds a tree (dendrogram).
• Time Complexity:
O(n² log n) (optimized) or up to O(n³) (naive)
********** 3 **********
--- page 4 ---
• Space Complexity:
O(n²) (distance matrix)
• Computes pairwise distance matrix → O(n²)
• Repeated merging/splitting of clusters
• Updating distances after each merge
Clustering algorithms differ significantly in computational complexity, which directly
impacts their scalability to large datasets.
K-Means Clustering is relatively efficient and scalable. Its time complexity is
approximately O(n × k × i × d), where n is the number of data points, k is the number of
clusters, i is the number of iterations, and d is the number of features. Since k and i are
usually small, K-Means scales well to large datasets and is widely used in real-time and
big data applications.
In contrast, Hierarchical Clustering (especially agglomerative) has much higher
complexity. Its time complexity is typically O(n² log n) or even O(n³) depending on
implementation, and space complexity is O(n²) due to the need to store distance matrices.
This makes it computationally expensive and less suitable for large datasets.
Impact on scalability:
• K-Means is highly scalable and suitable for large-scale datasets (millions of
points).
•   Hierarchical clustering is limited to smaller datasets due to its high computational
and memory requirements.
Complexity: 02 M
•   Explanation with scalability: 03
1 Mark for each correct step
Q2   a.   The following table records the number of balls that Ayush took for scoring runs. In   [10]
CO-2;   how many balls is he likely to score a century?
SO-
2;   Runs   Number of
BL-   Scored   Balls
4   8   10
35   20
47   31
54   23
11   5
85   47
84   35
93   67
89   73
2   1
Solution:
********** 4 **********
--- page 5 ---
x = Runs scored
y = Number of balls
We need to predict the number of balls required when Ayush scores 100 runs.
We use the linear regression model:
y = mx + b,
where y and x are variables,
m is the slope, and
b is the y-intercept.
The equations for m and b are as below -
m = (n∑xy - ∑y∑x)/[n∑x2 - (∑x)2]
b = (∑y - m∑x)/n
∑xy = 23199
∑y = 312
∑x = 508
∑x2 = 37390
(∑x)2 = 508*508
m = (n∑xy - ∑y∑x)/[n∑x2 - (∑x)2]
= (10*23199-312*508) / [10*37390-(508*508)]
m = 0.634466
b = (∑y - m∑x)/n
b= (312-0.634466*508)/10
b = -1.03087
The equation will be –
Y = 0.634466*X + (-1.03087)   08 Marks
Predict balls for 100 runs i.e.x=100
Substitute x=100 in regression line equation.
Y = 0.634466*100 + (-1.03087) = 62.41573
Ayush requires 62 balls to score 100 runs.
2Marks
Q2   b. Explain how nonlinear data can be classify using SVM? Explain different kernel   [10]
CO-2; SO-2;   functions used classification.
BL-2   Solution:
If the dataset is not linearly separable, SVM uses a nonlinear decision boundary
to classify the data. This is called a nonlinear SVM.
1Mark
Key Idea-
Instead of drawing a straight line, nonlinear SVM:
• Transforms the data into a higher-dimensional space
• Uses a kernel function to make the data separable
• Then finds a linear boundary in that higher dimension, which appears
nonlinear in original space
•   1Mark for each explanation (04)
********** 5 **********
--- page 6 ---
Kernal functions are used to deal with nonlinear SVM
Explanation how nonlinear SVM is analyzed using kernel function:
Different types of kernel functions are:
i) Homogeneous polynomial kernel
ii) Non-homogeneous polynomial kernel
iii) Radial basis function
iv) Sigmoid kernel function
1Mark for each explanation of kernel function with equation
(05)
Q3   a. A company analyzes employee attrition using the following dataset:   [10]
CO-3;
SO-6;
BL-3   Experience   Satisfaction   Leave
High   Low   Yes
High   Medium   No
Medium   Low   Yes
Low   Medium   No
Low   High   No
Medium   High   No
Apply ID3 algorithm to:
•   Calculate Entropy of target variable
• Compute Information Gain of attributes
•   Identify the root node
Solution:
Step 1: Dataset Summary
Total samples = 6
Target (Leave):
• Yes = 2
• No = 4
Step 2: Entropy of Target Variable
[
Entropy(S) = - (2/6)\log_2(2/6) - (4/6)\log_2(4/6)
]
[
= - (0.333)(-1.585) - (0.667)(-0.585)
]
[
= 0.528 + 0.390 = 0.918
********** 6 **********
--- page 7 ---
]
Entropy(S) = 0.918
03Marks
Step 3: Information Gain Calculations
(A) Attribute: Experience
Ye N Tota
Experience   Entropy
s   o   l
High   1 1 2   1
Medium   1 1 2   1
Low   0 2 2   0
[
Weighted = (2/6)(1) + (2/6)(1) + (2/6)(0)
]
[
= 0.333 + 0.333 + 0 = 0.666
]
[
IG(Experience) = 0.918 - 0.666 = 0.252
]
IG(Experience) = 0.252
03Marks
(B) Attribute: Satisfaction
Ye N Tota
Satisfaction   Entropy
s   o   l
Low   2 0 2   0
********** 7 **********
--- page 8 ---
Medium   0 2 2   0
High   0 2 2   0
[
Weighted = (2/6)(0) + (2/6)(0) + (2/6)(0) = 0
]
[
IG(Satisfaction) = 0.918 - 0 = 0.918
]
IG(Satisfaction) = 0.918
03Marks
Step 4: Root Node Selection
•   IG(Experience) = 0.252
•   IG(Satisfaction) = 0.918
Root Node = Satisfaction (highest IG)
01Mark
Q3   b. A hedge fund analyzes 200+ financial indicators (prices, volatility, macroeconomic   [10]
CO-1;   factors). The dataset suffers from multicollinearity and noise, leading to unstable
SO-1; BL-2   predictive models.
Tasks:
1. Explain how PCA can address multicollinearity in this dataset.
2. How would you decide the number of principal components to retain?
3. Discuss potential risks of using PCA in financial decision-making.
Solution:
A hedge fund often works with a very large number of financial variables such as stock
prices, returns, volatility measures, interest rates, inflation, exchange rates, sector indices,
and macroeconomic indicators. In such datasets, many variables are highly correlated
with each other. This creates multicollinearity, which makes predictive models unstable.
Also, noisy and redundant features increase computational complexity and reduce model
reliability.
Principal Component Analysis (PCA) is a dimensionality reduction technique that can
help solve these issues by transforming the original correlated variables into a smaller set
********** 8 **********
--- page 9 ---
of new uncorrelated variables called principal components.
1. How PCA can address multicollinearity in this dataset
Meaning of multicollinearity
Multicollinearity occurs when two or more input variables are strongly correlated. In
finance, this is very common because many indicators move together.
For example:
•   stock price and moving average may be strongly related
•   inflation and interest rate may influence each other
•   sector indices may follow the same market trend
When multicollinearity exists:
• model coefficients become unstable
•   small changes in data can produce large changes in predictions
•   interpretation of variable importance becomes difficult
•   regression models may overfit or behave inconsistently
How PCA solves this
PCA transforms the original set of correlated features into a new set of variables called
principal components.
These principal components have two key properties:
1. They are linear combinations of original variables
2. They are uncorrelated with each other
So, instead of directly using 200 correlated financial indicators, the hedge fund can use a
smaller number of principal components that summarize the major patterns in the dataset.
Why this reduces multicollinearity
Since the principal components are orthogonal, there is no correlation among them. This
removes the multicollinearity problem.
Practical effect in hedge fund modeling
Using PCA:
•   correlated indicators are compressed into a few market factors
•   regression or prediction models become more stable
•   estimation becomes more reliable
•   redundant information is removed
•   noise can be reduced by discarding less important components
********** 9 **********
--- page 10 ---
Example intuition
Suppose many indicators reflect overall market movement. PCA may combine them into
one principal component representing market trend. Another component may capture
volatility behavior. A third may represent macroeconomic pressure. Thus, instead of
200 raw variables, a model may work with 10–20 meaningful components.
2. How to decide the number of principal components to retain
Choosing the correct number of principal components is very important. If too few are
kept, useful information may be lost. If too many are kept, noise and redundancy may
remain.
Several methods are used:
A. Explained Variance Criterion
Each principal component explains some portion of the total variance in the data.
• The first component explains the maximum variance
• The second explains the next highest variance
• and so on
A common rule is to retain enough components to explain 80% to 95% of the total
variance.
In finance
A hedge fund may choose enough components to explain around 90%–95% variance,
especially when trying to preserve important market structure.
Advantage
• Simple and widely used
• Gives a quantitative basis for selection
Limitation
• High explained variance does not always mean high predictive usefulness
B. Scree Plot Method
A scree plot shows eigenvalues versus component number.
• The curve usually drops sharply at first
• Then it begins to flatten
The point where the curve starts flattening is called the elbow point. Components before
this point are usually retained.
********** 10 **********
--- page 11 ---
Meaning
Beyond the elbow, extra components add only small amounts of information and may
mainly represent noise.
C. Kaiser Criterion
According to this rule, keep components with eigenvalue greater than 1.
Reason
An eigenvalue greater than 1 indicates that the component explains more variance than an
individual standardized original variable.
Limitation
This rule is more useful in moderate-sized datasets and may not always be ideal for large
financial datasets.
D. Cross-Validation / Model Performance
A more practical approach is to try different numbers of principal components and test the
predictive model performance.
For example:
•   train model with first 5 components
•   then with 10 components
•   then with 15 components
• compare prediction accuracy, stability, and risk metrics
3. Potential risks of using PCA in financial decision-making
Although PCA is useful, it also has important risks, especially in finance where decisions
involve high uncertainty and financial loss.
A. Loss of Interpretability
The original variables are easy to understand, such as inflation, interest rates, or stock
returns. But principal components are combinations of many variables.
This makes interpretation difficult.
Risk
A portfolio manager may not clearly understand what a principal component
economically represents. This can reduce trust in the model.
B. Important Low-Variance Features May Be Discarded
********** 11 **********
--- page 12 ---
PCA keeps components with the highest variance and removes low-variance components.
However, in finance, some low-variance variables may contain important predictive
signals.
Example
A small but consistent macroeconomic indicator may have low variance but still be very
useful for forecasting a crisis.
Risk
Discarding such components may harm prediction quality.
01Mark for each correct explanation (10 steps must be written)
Q4   a. A regression model gives a high R-squared value but poor predictive accuracy.   [10]
CO-2;
SO-   Analyse this situation and relate it to potential issues such as overfitting or data
2;   distribution.
BL-   Solution:
2   A regression model may show a high R-squared value but still have poor predictive
accuracy when it fits the training data well but fails to generalize to new or unseen
data. This means the model explains a large proportion of variance in the available
dataset, yet its practical prediction performance is weak.
Meaning of high R-squared
R-squared measures the proportion of variation in the dependent variable explained
by the independent variables. A high value suggests that the model fits the observed
data closely.
However, a good fit on test data does not always guarantee good prediction on test
data.
Overfitting as a major reason
One common reason is overfitting. Overfitting occurs when the regression model
learns not only the true pattern in the data but also the random noise. This usually
happens when:
•   too many predictors are included,
•   higher-order polynomial terms are used unnecessarily,
•   the model becomes too complex for the size of data.
********** 12 **********
--- page 13 ---
In such cases, the model performs very well on training data, giving a high R-squared,
but performs poorly on test or validation data.
Problems related to data distribution
Poor predictive accuracy may also arise because of data distribution issues.
Examples include:
a) Training and test data mismatch
If test data has a different distribution from training data, the model may not work
well even if training fit is excellent.
b) Presence of outliers
A few extreme values can distort regression coefficients and create misleadingly high
goodness-of-fit.
c) Non-linearity
If the true relationship is not linear but a linear regression model is applied, R-squared
may appear acceptable on one dataset but prediction may fail on others.
d) Heteroscedasticity
When error variance is not constant, predictions become unreliable across different
ranges of input values.
01Mark for each correct explanation
Q4   b. The 2×2 Image given bellow is applied to the fully connected neural network with   [10]
CO-3;
SO-6;   sigmoid activation function. calculate the following
BL-6
a. Predicted output after first epoch.
b. Mean square error after first epoch.
c.   If learning rate of 0.05 find the updated value of weight W14 using error
back propagation algorithm.
Assume bias at hidden layer neurons b1=0.30, and bias at output layer neuron
b2=0.50 and weights are given in following table.
W1   W2   W3   W4   W5   W6   W7   W8   W9   W10   W11   W12   W13   W14   W15
0.10   0.20   0.30   0.40   0.50   0.60   0.70   0.80   0.90   0.65   0.75   0.95   0.75   0.55   0.85
Inputs applied to the input layer is
X1   X2   X3   X4
0.40   0.55   0.65   0.85
********** 13 **********
--- page 14 ---
Solution:
Input to neural network are we convert 2D image in to 1D image by converting rows
in to columns so the inputs to neural network are x1=0.40,x2=0.55,x3=0.65,x4=0.85
Predicted output after first epoch
a. h11in=b1+w1x1+w4x2+w7x3+w10x4 =1.5575
h11out=1/(1+e- h11in)=0.4627
b. h12in= b1+w2x1+w5x2+w8x3+w11x4 =1.8125
h12out=1/(1+e- h12in)=0.3555
c. h13in=b1+w3x1+w6x2+w9x3+w12x4 =2.1425
h13out=1/(1+e- h11in)=0.3182
d. O1in=b2+w13 h11out +w14 h12out +w15 h13out =1.3129
O1out=1/(1+e- O1in)=0.4323
05Mark
Mean square error after first epoch
Mean Square error after first epoch =1/2[(O1-T1)2]= 1/2[(O11out -T1)2=]
= 1/2[(0.4323 -0.82)2]
Mean Square error after first epoch =0.0.0751
02Mark
If learning rate of 0.05 find the updated value of weight w14 using error back
propagation algorithm.
w14New=0.5481
Steps for updating weight
********** 14 **********
--- page 15 ---
03Mark
Q5   a. Explain Ensemble Learning. Discuss how ensemble methods improve the performance   [10]
CO-3;   of Decision Trees.
SO-
1;   Solution:
BL   Ensemble Learning
-3
Ensemble Learning is a technique where multiple models are combined to improve
overall performance.
Instead of relying on a single model, multiple weak learners are used to create a
strong learner.
Types of Ensemble Methods
********** 15 **********
--- page 16 ---
1. Bagging
2. Boosting
3. Random Forest
How Ensemble Improves Decision Trees
Decision Trees suffer from:
• High variance
•   Overfitting
Ensemble methods solve these issues:
1. Bagging (Bootstrap Aggregation)
•   Multiple datasets created using sampling with replacement
•   Train separate trees
•   Final output = majority voting / averaging
Reduces variance
2. Random Forest
• Extension of bagging
• Random feature selection + multiple trees
More robust and less correlated trees
3. Boosting
• Models trained sequentially
• Focus on correcting previous errors
Examples:
• AdaBoost
********** 16 **********
--- page 17 ---
• Gradient Boosting
Reduces bias + variance
1 Mark for each correct steps/explanation
Q5   b. Implement K-Means clustering with K = 3 on the following dataset. Use the first three [10]
CO-2;
SO-2;   points as the initial cluster centroids and apply Euclidean distance to assign points to
BL-2
clusters. Perform two iterations of the algorithm. Show:
1. Initial centroids
2. Distance calculations
3. Cluster assignment after each iteration
4. Updated centroids
5. Final grouping after two iterations.
The Dataset is: {(2,4),(3,5),(4,6),(8,8),(9,9),(10,10),(15,3),(16,4),(17,5)}
Solution:
Step 1: Initial Centroids
Since the first three points are taken as the initial centroids:
• C1=(2,4
•   C2=(3,5)
•   C3=(4,6)
Dataset: (2,4), (3,5), (4,6), (8,8), (9,9), (10,10), (15,3), (16,4), (17,5)
Initial Centroids: C1 = (2,4) C2 = (3,5) C3 = (4,6)
Iteration 1: Cluster 1: (2,4) Cluster 2: (3,5) Cluster 3: (4,6), (8,8), (9,9), (10,10), (15,3),
(16,4), (17,5)
Updated Centroids:
05Mark
********** 17 **********
--- page 18 ---
C1 = (2,4) C2 = (3,5) C3 = (11.29, 6.43)
Iteration 2: Cluster 1: (2,4) Cluster 2: (3,5), (4,6) Cluster 3: (8,8), (9,9), (10,10), (15,3),
(16,4), (17,5)
Final Centroids: C1 = (2,4) C2 = (3.5, 5.5) C3 = (12.5, 6.5)
05Mark
Q6   a. Describe the steps involved in preparing data for a regression model. Explain the   [10]
CO-2;   importance of selecting variables, handling missing values, and checking data
SO-2;
BL-5   consistency for regression model building.
Solution:
Preparing data for a regression model involves understanding the problem, collecting
and organizing data, selecting relevant variables, handling missing values, checking
consistency, and performing cleaning and transformation. Among these, variable
selection, missing value treatment, and consistency checking are especially
important because they directly affect the accuracy, reliability, and interpretability of
the regression model. Proper data preparation forms the foundation for building an
effective regression model.
02Mark
Importance of selecting variables
Handling missing values
04Mark
Checking data consistency.
Explain all in detail..
04Mark
********** 18 **********
--- page 19 ---
Q6   b. For the data set give bellow has 10 samples Create a confusion matrix and Calculate   [10]
CO-4;   Accuracy, Precision, Recall, F1-score. Assume Car as Positive Class.
SO-
6;
BL-   No Expected/Actu
4   Predicted
.   al
1   Car   Car
2   Bike   Bike
3   Car   Bike
4   Bike   Bike
5   Car   Car
6   Bike   Car
7   Car   Car
8   Bike   Bike
9   Car   Bike
10   Bike   Car
Solution:
• TP (True Positive) → Car predicted as Car = 3 (1, 5, 7)
• TN (True Negative) → Bike predicted as Bike = 3 (2, 4, 8)
• FP (False Positive) → Bike predicted as Car = 2 (6, 10)
• FN (False Negative) → Car predicted as Bike = 2 (3, 9)
03Mark
Confusion Matrix
Predicted Car   Predicted Bike
Actual Car   TP = 3   FN = 2
Actual Bike   FP = 2   TN = 3
02Mark
Accuracy= Tp+TN/Total= 6/10 = 0.6
PRECISION=TP/TP+FP=3/5= 0.6
RECALL=TP/TP+FN=3/5= 0.6
F1=0.6
05Mark
********** 19 **********
--- page 20 ---
Q7   a. Explain Bagging and Boosting techniques in detail. Compare their working mechanisms [10]
CO-2;   and their impact on bias and variance.
SO-
2;   Solution
BL-
2   Bagging (Bootstrap Aggregation)
• Random sampling with replacement
•   Parallel model training
• Equal weight to all models
Working:
1. Create multiple datasets
2. Train models independently
3. Aggregate results
Reduces variance
Boosting
•   Sequential learning
• Each model focuses on previous errors
Working:
1. Train first model
2. Increase weight of misclassified points
3. Train next model
4. Combine weighted results
Reduces bias and variance
Comparison
Aspect   Bagging   Boosting
Training   Parallel   Sequential
********** 20 **********
--- page 21 ---
Reduce
Focus   Reduce bias + variance
variance
Data
Random   Weighted
sampling
Can overfit if not
Overfitting   Less
controlled
Example   Random Forest AdaBoost
01 Mark for each correct explanation
Q7   b. What factors should be considered while selecting a machine learning model?   [05]
CO-1;   Solution:
SO-
2;   Things to Take Into Account When Choosing a Machine Learning Model
BL-
2   The nature of the issue
Tasks involving classification, regression, or grouping
The dataset's size
Complex models are supported by large datasets, while simpler models are needed
for small datasets.
Data Quality
Model selection is impacted by the existence of noise, missing variables, and outliers.
Dimensionality of Features
Models like SVM or dimensionality reduction methods may be necessary for high-
dimensional data.
Complexity of the Model
Strike a balance between overfitting and underfitting (bias–variance trade-off).
Interpretability
Compared to sophisticated outational Cos, simple models (such decision trees and
linear regression) are simpler to understand.
Certain models, like deep learning models, demand a lot of processing power.
Measures of Performance
Depending on the issue, accuracy, precision, recall, F1-score, and RMSE
Scalability
The model's capacity to manage expanding data
0.5 Mark for each correct explanation
Q7   c. A bank analyzes transaction amounts (in ₹):   [05]
CO-1;   200, 220, 250, 270, 300, 320, 350, 400, 2000
SO-
6;   Apply the IQR method to detect any abnormal amount. Based on your findings, decide
BL-   how you should treat the extreme value.
2
********** 21 **********
--- page 22 ---
Solution:
Apply IQR 3 mark
Outlier Treatment 2 marks
To detect abnormal transaction amounts using the IQR (Interquartile Range)
method, we first arrange the data in ascending order:
200, 220, 250, 270, 300, 320, 350, 400, 2000
The total number of observations is 9. The median (Q2) is the 5th value, which is
300.
Now, we divide the dataset into two halves (excluding the median):
• Lower half: 200, 220, 250, 270 → Q1 = (220 + 250) / 2 = 235
• Upper half: 320, 350, 400, 2000 → Q3 = (350 + 400) / 2 = 375
Next, calculate the IQR:
IQR = Q3 − Q1 = 375 − 235 = 140
Now, compute the bounds:
• Lower bound = Q1 − 1.5 × IQR = 235 − (1.5 × 140) = 235 − 210 = 25
• Upper bound = Q3 + 1.5 × IQR = 375 + 210 = 585
Any value outside the range 25 to 585 is considered an outlier.
Here, 2000 > 585, so ₹2000 is an outlier (abnormal transaction).
The transaction amount ₹2000 is significantly higher than the rest of the data. The
appropriate treatment depends on the context:
•   If the transaction is legitimate (e.g., a genuine high-value transfer), it should
be retained, as it may indicate important customer behavior.
•   If it is fraudulent or suspicious, it should be flagged for investigation rather
than removed.
•   If it is due to a data entry error, it should be corrected or removed.
• For analytical purposes, we may apply capping (winsorization) by replacing
₹2000 with the upper bound (₹585) to reduce its impact on statistical models.
03 Marks
********** 22 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper fa7454da710e

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (22 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (EXTC)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Question No.1 is compulsory.
3. Out of remaining questionsa attempt any 4 questions.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figure in brackets on the right hand side indicates full marks.
7. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Define overfitting using an example. Explain its significance.   [05]
SO-   Solution:
1;   Overfitting :
BL   When a machine learning model provides correct predictions for training data but not for
-2   new data, this is known as overfitting, an undesirable machine learning tendency. Data
scientists first train machine learning models on a known data set before using them to
make predictions. The model then attempts to forecast results for fresh data sets using this
information. An overfit model cannot function properly for all kinds of incoming data and
may produce erroneous predictions.
02 Marks
Why?
Overfitting happens when a model sticks too closely to the training data and struggles to
handle new data. Basically, it memorizes the details and noise instead of learning the
actual patterns. This usually comes up for a few reasons. Sometimes, you just don’t have
enough training data, so the model can’t really get a sense of everything it needs to know.
Or maybe the training data has too much random or irrelevant information—what’s called
noisy data—which confuses the model. Training a model for too many rounds on the
same dataset also makes things worse, since it just keeps picking up more noise with each
pass. And if the model itself is too complicated, it tries to capture every tiny detail, even
the ones that don’t matter. That’s why overfitting is such a common headache in machine
learning.
Example: Consider a use case where a machine learning model has to analyze photos and
identify the ones that contain dogs in them. If the machine learning model was trained on
a data set that contained majority photos showing dogs outside in parks , it may may learn
to use grass as a feature for classification, and may not recognize a dog inside a room.
03Marks
CO-1; SO-   b. A dataset contains product categories: Car, Bike, Bus, Car, and Bike. Apply One-Hot   [05]
1;   Encoding to convert this categorical data into numerical format and explain why
BL   assigning simple numeric labels may lead to incorrect interpretations.
-4
********** 1 **********
--- page 2 ---
Solution:
Apply One-Hot Encoding to convert this categorical data into numerical format- 2 marks
explain why assigning simple numeric labels may lead to incorrect interpretations.3
marks
03Marks
One-Hot Encoding converts categorical values into binary vectors, where only one
position is marked as 1 and the rest are 0. This ensures that each category is treated as
independent and equally important.
If we instead assign simple numeric labels such as:
Car = 1, Bike = 2, Bus = 3,
it may lead to incorrect interpretations. Machine learning models may assume an
ordinal relationship (e.g., Bus > Bike > Car), which is not meaningful because these
categories do not have any inherent order.
2Marks
CO-2; SO-1;   c.   Under what circumstances are Precision, or Recall better performance metrics in   [05]
BL-2   comparison with accuracy? Give an example each for the situations where “Recall is a
more important evaluation metric than Precision”.” Precision is a more important
evaluation metric than Recall”.
Solution:
When are Precision or Recall better than Accuracy?
Accuracy works well only when classes are balanced and errors have equal cost.
But in many real-world problems (like **Cancer detection or spam filtering), data is
imbalanced and mistakes have different consequences.
Use Recall when:
• Missing a positive case is very dangerous
• You want to capture as many actual positives as possible
•   False negatives must be minimized
Example:
Disease Detection (e.g., Cancer Screening)
•   If a patient has cancer but the model predicts negative → very risky
•   It’s better to flag more people as positive (even if some are wrong)
•   So, Recall is more important
********** 2 **********
--- page 3 ---
Use Precision when:
•   False positives are costly or harmful
• You want predictions to be highly accurate when positive
• Avoid wrongly labeling negatives as positives
Example:
Email Spam Detection
•   If a normal email is marked as spam → important message may be lost
•   So, predictions labeled “spam” should be very accurate
• Hence, Precision is more important
Summary Table
Metric   Focus   Important When   Example
Minimize False   Missing positive is   Cancer
Recall
Negatives   dangerous   detection
Minimize False   Spam
Precision   False alarms are costly
Positives   filtering
1Mark for each explanation
CO-2; SO-2;   d. Discuss the computational complexity of K-Means and Hierarchical Clustering and its   [05]
BL-2   impact on scalability.
Solution:
K_Means and Hierarchical Clustering: 02 M
Comaparison: 03 M
K-Means is an iterative algorithm.
• Time Complexity:
O(n × k × t × d)
where:
o n = number of data points
o k = number of clusters
o   t = number of iterations
o d = number of features
• Each iteration assigns points to nearest centroid → O(n × k)
• Updating centroids → O(n)
• Repeated for t iterations
Hierarchical clustering builds a tree (dendrogram).
• Time Complexity:
O(n² log n) (optimized) or up to O(n³) (naive)
********** 3 **********
--- page 4 ---
• Space Complexity:
O(n²) (distance matrix)
• Computes pairwise distance matrix → O(n²)
• Repeated merging/splitting of clusters
• Updating distances after each merge
Clustering algorithms differ significantly in computational complexity, which directly
impacts their scalability to large datasets.
K-Means Clustering is relatively efficient and scalable. Its time complexity is
approximately O(n × k × i × d), where n is the number of data points, k is the number of
clusters, i is the number of iterations, and d is the number of features. Since k and i are
usually small, K-Means scales well to large datasets and is widely used in real-time and
big data applications.
In contrast, Hierarchical Clustering (especially agglomerative) has much higher
complexity. Its time complexity is typically O(n² log n) or even O(n³) depending on
implementation, and space complexity is O(n²) due to the need to store distance matrices.
This makes it computationally expensive and less suitable for large datasets.
Impact on scalability:
• K-Means is highly scalable and suitable for large-scale datasets (millions of
points).
•   Hierarchical clustering is limited to smaller datasets due to its high computational
and memory requirements.
Complexity: 02 M
•   Explanation with scalability: 03
1 Mark for each correct step
Q2   a.   The following table records the number of balls that Ayush took for scoring runs. In   [10]
CO-2;   how many balls is he likely to score a century?
SO-
2;   Runs   Number of
BL-   Scored   Balls
4   8   10
35   20
47   31
54   23
11   5
85   47
84   35
93   67
89   73
2   1
Solution:
********** 4 **********
--- page 5 ---
x = Runs scored
y = Number of balls
We need to predict the number of balls required when Ayush scores 100 runs.
We use the linear regression model:
y = mx + b,
where y and x are variables,
m is the slope, and
b is the y-intercept.
The equations for m and b are as below -
m = (n∑xy - ∑y∑x)/[n∑x2 - (∑x)2]
b = (∑y - m∑x)/n
∑xy = 23199
∑y = 312
∑x = 508
∑x2 = 37390
(∑x)2 = 508*508
m = (n∑xy - ∑y∑x)/[n∑x2 - (∑x)2]
= (10*23199-312*508) / [10*37390-(508*508)]
m = 0.634466
b = (∑y - m∑x)/n
b= (312-0.634466*508)/10
b = -1.03087
The equation will be –
Y = 0.634466*X + (-1.03087)   08 Marks
Predict balls for 100 runs i.e.x=100
Substitute x=100 in regression line equation.
Y = 0.634466*100 + (-1.03087) = 62.41573
Ayush requires 62 balls to score 100 runs.
2Marks
Q2   b. Explain how nonlinear data can be classify using SVM? Explain different kernel   [10]
CO-2; SO-2;   functions used classification.
BL-2   Solution:
If the dataset is not linearly separable, SVM uses a nonlinear decision boundary
to classify the data. This is called a nonlinear SVM.
1Mark
Key Idea-
Instead of drawing a straight line, nonlinear SVM:
• Transforms the data into a higher-dimensional space
• Uses a kernel function to make the data separable
• Then finds a linear boundary in that higher dimension, which appears
nonlinear in original space
•   1Mark for each explanation (04)
********** 5 **********
--- page 6 ---
Kernal functions are used to deal with nonlinear SVM
Explanation how nonlinear SVM is analyzed using kernel function:
Different types of kernel functions are:
i) Homogeneous polynomial kernel
ii) Non-homogeneous polynomial kernel
iii) Radial basis function
iv) Sigmoid kernel function
1Mark for each explanation of kernel function with equation
(05)
Q3   a. A company analyzes employee attrition using the following dataset:   [10]
CO-3;
SO-6;
BL-3   Experience   Satisfaction   Leave
High   Low   Yes
High   Medium   No
Medium   Low   Yes
Low   Medium   No
Low   High   No
Medium   High   No
Apply ID3 algorithm to:
•   Calculate Entropy of target variable
• Compute Information Gain of attributes
•   Identify the root node
Solution:
Step 1: Dataset Summary
Total samples = 6
Target (Leave):
• Yes = 2
• No = 4
Step 2: Entropy of Target Variable
[
Entropy(S) = - (2/6)\log_2(2/6) - (4/6)\log_2(4/6)
]
[
= - (0.333)(-1.585) - (0.667)(-0.585)
]
[
= 0.528 + 0.390 = 0.918
********** 6 **********
--- page 7 ---
]
Entropy(S) = 0.918
03Marks
Step 3: Information Gain Calculations
(A) Attribute: Experience
Ye N Tota
Experience   Entropy
s   o   l
High   1 1 2   1
Medium   1 1 2   1
Low   0 2 2   0
[
Weighted = (2/6)(1) + (2/6)(1) + (2/6)(0)
]
[
= 0.333 + 0.333 + 0 = 0.666
]
[
IG(Experience) = 0.918 - 0.666 = 0.252
]
IG(Experience) = 0.252
03Marks
(B) Attribute: Satisfaction
Ye N Tota
Satisfaction   Entropy
s   o   l
Low   2 0 2   0
********** 7 **********
--- page 8 ---
Medium   0 2 2   0
High   0 2 2   0
[
Weighted = (2/6)(0) + (2/6)(0) + (2/6)(0) = 0
]
[
IG(Satisfaction) = 0.918 - 0 = 0.918
]
IG(Satisfaction) = 0.918
03Marks
Step 4: Root Node Selection
•   IG(Experience) = 0.252
•   IG(Satisfaction) = 0.918
Root Node = Satisfaction (highest IG)
01Mark
Q3   b. A hedge fund analyzes 200+ financial indicators (prices, volatility, macroeconomic   [10]
CO-1;   factors). The dataset suffers from multicollinearity and noise, leading to unstable
SO-1; BL-2   predictive models.
Tasks:
1. Explain how PCA can address multicollinearity in this dataset.
2. How would you decide the number of principal components to retain?
3. Discuss potential risks of using PCA in financial decision-making.
Solution:
A hedge fund often works with a very large number of financial variables such as stock
prices, returns, volatility measures, interest rates, inflation, exchange rates, sector indices,
and macroeconomic indicators. In such datasets, many variables are highly correlated
with each other. This creates multicollinearity, which makes predictive models unstable.
Also, noisy and redundant features increase computational complexity and reduce model
reliability.
Principal Component Analysis (PCA) is a dimensionality reduction technique that can
help solve these issues by transforming the original correlated variables into a smaller set
********** 8 **********
--- page 9 ---
of new uncorrelated variables called principal components.
1. How PCA can address multicollinearity in this dataset
Meaning of multicollinearity
Multicollinearity occurs when two or more input variables are strongly correlated. In
finance, this is very common because many indicators move together.
For example:
•   stock price and moving average may be strongly related
•   inflation and interest rate may influence each other
•   sector indices may follow the same market trend
When multicollinearity exists:
• model coefficients become unstable
•   small changes in data can produce large changes in predictions
•   interpretation of variable importance becomes difficult
•   regression models may overfit or behave inconsistently
How PCA solves this
PCA transforms the original set of correlated features into a new set of variables called
principal components.
These principal components have two key properties:
1. They are linear combinations of original variables
2. They are uncorrelated with each other
So, instead of directly using 200 correlated financial indicators, the hedge fund can use a
smaller number of principal components that summarize the major patterns in the dataset.
Why this reduces multicollinearity
Since the principal components are orthogonal, there is no correlation among them. This
removes the multicollinearity problem.
Practical effect in hedge fund modeling
Using PCA:
•   correlated indicators are compressed into a few market factors
•   regression or prediction models become more stable
•   estimation becomes more reliable
•   redundant information is removed
•   noise can be reduced by discarding less important components
********** 9 **********
--- page 10 ---
Example intuition
Suppose many indicators reflect overall market movement. PCA may combine them into
one principal component representing market trend. Another component may capture
volatility behavior. A third may represent macroeconomic pressure. Thus, instead of
200 raw variables, a model may work with 10–20 meaningful components.
2. How to decide the number of principal components to retain
Choosing the correct number of principal components is very important. If too few are
kept, useful information may be lost. If too many are kept, noise and redundancy may
remain.
Several methods are used:
A. Explained Variance Criterion
Each principal component explains some portion of the total variance in the data.
• The first component explains the maximum variance
• The second explains the next highest variance
• and so on
A common rule is to retain enough components to explain 80% to 95% of the total
variance.
In finance
A hedge fund may choose enough components to explain around 90%–95% variance,
especially when trying to preserve important market structure.
Advantage
• Simple and widely used
• Gives a quantitative basis for selection
Limitation
• High explained variance does not always mean high predictive usefulness
B. Scree Plot Method
A scree plot shows eigenvalues versus component number.
• The curve usually drops sharply at first
• Then it begins to flatten
The point where the curve starts flattening is called the elbow point. Components before
this point are usually retained.
********** 10 **********
--- page 11 ---
Meaning
Beyond the elbow, extra components add only small amounts of information and may
mainly represent noise.
C. Kaiser Criterion
According to this rule, keep components with eigenvalue greater than 1.
Reason
An eigenvalue greater than 1 indicates that the component explains more variance than an
individual standardized original variable.
Limitation
This rule is more useful in moderate-sized datasets and may not always be ideal for large
financial datasets.
D. Cross-Validation / Model Performance
A more practical approach is to try different numbers of principal components and test the
predictive model performance.
For example:
•   train model with first 5 components
•   then with 10 components
•   then with 15 components
• compare prediction accuracy, stability, and risk metrics
3. Potential risks of using PCA in financial decision-making
Although PCA is useful, it also has important risks, especially in finance where decisions
involve high uncertainty and financial loss.
A. Loss of Interpretability
The original variables are easy to understand, such as inflation, interest rates, or stock
returns. But principal components are combinations of many variables.
This makes interpretation difficult.
Risk
A portfolio manager may not clearly understand what a principal component
economically represents. This can reduce trust in the model.
B. Important Low-Variance Features May Be Discarded
********** 11 **********
--- page 12 ---
PCA keeps components with the highest variance and removes low-variance components.
However, in finance, some low-variance variables may contain important predictive
signals.
Example
A small but consistent macroeconomic indicator may have low variance but still be very
useful for forecasting a crisis.
Risk
Discarding such components may harm prediction quality.
01Mark for each correct explanation (10 steps must be written)
Q4   a. A regression model gives a high R-squared value but poor predictive accuracy.   [10]
CO-2;
SO-   Analyse this situation and relate it to potential issues such as overfitting or data
2;   distribution.
BL-   Solution:
2   A regression model may show a high R-squared value but still have poor predictive
accuracy when it fits the training data well but fails to generalize to new or unseen
data. This means the model explains a large proportion of variance in the available
dataset, yet its practical prediction performance is weak.
Meaning of high R-squared
R-squared measures the proportion of variation in the dependent variable explained
by the independent variables. A high value suggests that the model fits the observed
data closely.
However, a good fit on test data does not always guarantee good prediction on test
data.
Overfitting as a major reason
One common reason is overfitting. Overfitting occurs when the regression model
learns not only the true pattern in the data but also the random noise. This usually
happens when:
•   too many predictors are included,
•   higher-order polynomial terms are used unnecessarily,
•   the model becomes too complex for the size of data.
********** 12 **********
--- page 13 ---
In such cases, the model performs very well on training data, giving a high R-squared,
but performs poorly on test or validation data.
Problems related to data distribution
Poor predictive accuracy may also arise because of data distribution issues.
Examples include:
a) Training and test data mismatch
If test data has a different distribution from training data, the model may not work
well even if training fit is excellent.
b) Presence of outliers
A few extreme values can distort regression coefficients and create misleadingly high
goodness-of-fit.
c) Non-linearity
If the true relationship is not linear but a linear regression model is applied, R-squared
may appear acceptable on one dataset but prediction may fail on others.
d) Heteroscedasticity
When error variance is not constant, predictions become unreliable across different
ranges of input values.
01Mark for each correct explanation
Q4   b. The 2×2 Image given bellow is applied to the fully connected neural network with   [10]
CO-3;
SO-6;   sigmoid activation function. calculate the following
BL-6
a. Predicted output after first epoch.
b. Mean square error after first epoch.
c.   If learning rate of 0.05 find the updated value of weight W14 using error
back propagation algorithm.
Assume bias at hidden layer neurons b1=0.30, and bias at output layer neuron
b2=0.50 and weights are given in following table.
W1   W2   W3   W4   W5   W6   W7   W8   W9   W10   W11   W12   W13   W14   W15
0.10   0.20   0.30   0.40   0.50   0.60   0.70   0.80   0.90   0.65   0.75   0.95   0.75   0.55   0.85
Inputs applied to the input layer is
X1   X2   X3   X4
0.40   0.55   0.65   0.85
********** 13 **********
--- page 14 ---
Solution:
Input to neural network are we convert 2D image in to 1D image by converting rows
in to columns so the inputs to neural network are x1=0.40,x2=0.55,x3=0.65,x4=0.85
Predicted output after first epoch
a. h11in=b1+w1x1+w4x2+w7x3+w10x4 =1.5575
h11out=1/(1+e- h11in)=0.4627
b. h12in= b1+w2x1+w5x2+w8x3+w11x4 =1.8125
h12out=1/(1+e- h12in)=0.3555
c. h13in=b1+w3x1+w6x2+w9x3+w12x4 =2.1425
h13out=1/(1+e- h11in)=0.3182
d. O1in=b2+w13 h11out +w14 h12out +w15 h13out =1.3129
O1out=1/(1+e- O1in)=0.4323
05Mark
Mean square error after first epoch
Mean Square error after first epoch =1/2[(O1-T1)2]= 1/2[(O11out -T1)2=]
= 1/2[(0.4323 -0.82)2]
Mean Square error after first epoch =0.0.0751
02Mark
If learning rate of 0.05 find the updated value of weight w14 using error back
propagation algorithm.
w14New=0.5481
Steps for updating weight
********** 14 **********
--- page 15 ---
03Mark
Q5   a. Explain Ensemble Learning. Discuss how ensemble methods improve the performance   [10]
CO-3;   of Decision Trees.
SO-
1;   Solution:
BL   Ensemble Learning
-3
Ensemble Learning is a technique where multiple models are combined to improve
overall performance.
Instead of relying on a single model, multiple weak learners are used to create a
strong learner.
Types of Ensemble Methods
********** 15 **********
--- page 16 ---
1. Bagging
2. Boosting
3. Random Forest
How Ensemble Improves Decision Trees
Decision Trees suffer from:
• High variance
•   Overfitting
Ensemble methods solve these issues:
1. Bagging (Bootstrap Aggregation)
•   Multiple datasets created using sampling with replacement
•   Train separate trees
•   Final output = majority voting / averaging
Reduces variance
2. Random Forest
• Extension of bagging
• Random feature selection + multiple trees
More robust and less correlated trees
3. Boosting
• Models trained sequentially
• Focus on correcting previous errors
Examples:
• AdaBoost
********** 16 **********
--- page 17 ---
• Gradient Boosting
Reduces bias + variance
1 Mark for each correct steps/explanation
Q5   b. Implement K-Means clustering with K = 3 on the following dataset. Use the first three [10]
CO-2;
SO-2;   points as the initial cluster centroids and apply Euclidean distance to assign points to
BL-2
clusters. Perform two iterations of the algorithm. Show:
1. Initial centroids
2. Distance calculations
3. Cluster assignment after each iteration
4. Updated centroids
5. Final grouping after two iterations.
The Dataset is: {(2,4),(3,5),(4,6),(8,8),(9,9),(10,10),(15,3),(16,4),(17,5)}
Solution:
Step 1: Initial Centroids
Since the first three points are taken as the initial centroids:
• C1=(2,4
•   C2=(3,5)
•   C3=(4,6)
Dataset: (2,4), (3,5), (4,6), (8,8), (9,9), (10,10), (15,3), (16,4), (17,5)
Initial Centroids: C1 = (2,4) C2 = (3,5) C3 = (4,6)
Iteration 1: Cluster 1: (2,4) Cluster 2: (3,5) Cluster 3: (4,6), (8,8), (9,9), (10,10), (15,3),
(16,4), (17,5)
Updated Centroids:
05Mark
********** 17 **********
--- page 18 ---
C1 = (2,4) C2 = (3,5) C3 = (11.29, 6.43)
Iteration 2: Cluster 1: (2,4) Cluster 2: (3,5), (4,6) Cluster 3: (8,8), (9,9), (10,10), (15,3),
(16,4), (17,5)
Final Centroids: C1 = (2,4) C2 = (3.5, 5.5) C3 = (12.5, 6.5)
05Mark
Q6   a. Describe the steps involved in preparing data for a regression model. Explain the   [10]
CO-2;   importance of selecting variables, handling missing values, and checking data
SO-2;
BL-5   consistency for regression model building.
Solution:
Preparing data for a regression model involves understanding the problem, collecting
and organizing data, selecting relevant variables, handling missing values, checking
consistency, and performing cleaning and transformation. Among these, variable
selection, missing value treatment, and consistency checking are especially
important because they directly affect the accuracy, reliability, and interpretability of
the regression model. Proper data preparation forms the foundation for building an
effective regression model.
02Mark
Importance of selecting variables
Handling missing values
04Mark
Checking data consistency.
Explain all in detail..
04Mark
********** 18 **********
--- page 19 ---
Q6   b. For the data set give bellow has 10 samples Create a confusion matrix and Calculate   [10]
CO-4;   Accuracy, Precision, Recall, F1-score. Assume Car as Positive Class.
SO-
6;
BL-   No Expected/Actu
4   Predicted
.   al
1   Car   Car
2   Bike   Bike
3   Car   Bike
4   Bike   Bike
5   Car   Car
6   Bike   Car
7   Car   Car
8   Bike   Bike
9   Car   Bike
10   Bike   Car
Solution:
• TP (True Positive) → Car predicted as Car = 3 (1, 5, 7)
• TN (True Negative) → Bike predicted as Bike = 3 (2, 4, 8)
• FP (False Positive) → Bike predicted as Car = 2 (6, 10)
• FN (False Negative) → Car predicted as Bike = 2 (3, 9)
03Mark
Confusion Matrix
Predicted Car   Predicted Bike
Actual Car   TP = 3   FN = 2
Actual Bike   FP = 2   TN = 3
02Mark
Accuracy= Tp+TN/Total= 6/10 = 0.6
PRECISION=TP/TP+FP=3/5= 0.6
RECALL=TP/TP+FN=3/5= 0.6
F1=0.6
05Mark
********** 19 **********
--- page 20 ---
Q7   a. Explain Bagging and Boosting techniques in detail. Compare their working mechanisms [10]
CO-2;   and their impact on bias and variance.
SO-
2;   Solution
BL-
2   Bagging (Bootstrap Aggregation)
• Random sampling with replacement
•   Parallel model training
• Equal weight to all models
Working:
1. Create multiple datasets
2. Train models independently
3. Aggregate results
Reduces variance
Boosting
•   Sequential learning
• Each model focuses on previous errors
Working:
1. Train first model
2. Increase weight of misclassified points
3. Train next model
4. Combine weighted results
Reduces bias and variance
Comparison
Aspect   Bagging   Boosting
Training   Parallel   Sequential
********** 20 **********
--- page 21 ---
Reduce
Focus   Reduce bias + variance
variance
Data
Random   Weighted
sampling
Can overfit if not
Overfitting   Less
controlled
Example   Random Forest AdaBoost
01 Mark for each correct explanation
Q7   b. What factors should be considered while selecting a machine learning model?   [05]
CO-1;   Solution:
SO-
2;   Things to Take Into Account When Choosing a Machine Learning Model
BL-
2   The nature of the issue
Tasks involving classification, regression, or grouping
The dataset's size
Complex models are supported by large datasets, while simpler models are needed
for small datasets.
Data Quality
Model selection is impacted by the existence of noise, missing variables, and outliers.
Dimensionality of Features
Models like SVM or dimensionality reduction methods may be necessary for high-
dimensional data.
Complexity of the Model
Strike a balance between overfitting and underfitting (bias–variance trade-off).
Interpretability
Compared to sophisticated outational Cos, simple models (such decision trees and
linear regression) are simpler to understand.
Certain models, like deep learning models, demand a lot of processing power.
Measures of Performance
Depending on the issue, accuracy, precision, recall, F1-score, and RMSE
Scalability
The model's capacity to manage expanding data
0.5 Mark for each correct explanation
Q7   c. A bank analyzes transaction amounts (in ₹):   [05]
CO-1;   200, 220, 250, 270, 300, 320, 350, 400, 2000
SO-
6;   Apply the IQR method to detect any abnormal amount. Based on your findings, decide
BL-   how you should treat the extreme value.
2
********** 21 **********
--- page 22 ---
Solution:
Apply IQR 3 mark
Outlier Treatment 2 marks
To detect abnormal transaction amounts using the IQR (Interquartile Range)
method, we first arrange the data in ascending order:
200, 220, 250, 270, 300, 320, 350, 400, 2000
The total number of observations is 9. The median (Q2) is the 5th value, which is
300.
Now, we divide the dataset into two halves (excluding the median):
• Lower half: 200, 220, 250, 270 → Q1 = (220 + 250) / 2 = 235
• Upper half: 320, 350, 400, 2000 → Q3 = (350 + 400) / 2 = 375
Next, calculate the IQR:
IQR = Q3 − Q1 = 375 − 235 = 140
Now, compute the bounds:
• Lower bound = Q1 − 1.5 × IQR = 235 − (1.5 × 140) = 235 − 210 = 25
• Upper bound = Q3 + 1.5 × IQR = 375 + 210 = 585
Any value outside the range 25 to 585 is considered an outlier.
Here, 2000 > 585, so ₹2000 is an outlier (abnormal transaction).
The transaction amount ₹2000 is significantly higher than the rest of the data. The
appropriate treatment depends on the context:
•   If the transaction is legitimate (e.g., a genuine high-value transfer), it should
be retained, as it may indicate important customer behavior.
•   If it is fraudulent or suspicious, it should be flagged for investigation rather
than removed.
•   If it is due to a data entry error, it should be corrected or removed.
• For analytical purposes, we may apply capping (winsorization) by replacing
₹2000 with the upper bound (₹585) to reduce its impact on statistical models.
03 Marks
********** 22 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper ae6f55dd0fe9

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CS_7055/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: duration hours: 3
- Text: mixed (22 pages), mean OCR confidence 68.9
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
Program/s: B. Tech(Computer)   Year: III, IV Semester: V, VII
Stream/s ; B. Tech(CSBS)/B.Tech(CS)
Subject: Machine Learning   Time: 3 Hours hrs (______to_______)
No. of Pages: 3
Marks: __100_______
Synoptic Answer
Q1   Answer briefly:
a) Given the following scenarios, identify the most suitable type of machine learning technique and justify
your choice:
a) Predicting house prices based on features like size and location.
b) Grouping customers based on purchasing patterns.
c) Recognize handwritten digits from images
Technique carries 3 marks and justification carries 2 marks
a) Predicting house prices based on features like size and location
   Suitable Technique: Supervised Learning – Regression
   Justification: The model learns from labeled data (house features with known prices) to
predict a continuous value — the price.
b) Grouping customers based on purchasing patterns
   Suitable Technique: Unsupervised Learning – Clustering
   Justification: There are no predefined labels; the model discovers hidden patterns and forms
groups based on similarity among customer behaviors.
c) Neural Network, Supervised Learning
   Suitable Technique: Artificial neural network
   Justification: Handwritten digit recognition is fundamentally an image
classification problem, which involves mapping an image (a grid of pixels) to one
of 10 discrete categories (the digits 0 through 9).
1. Mapping: The neural network takes the pixel values of the image as its input (e.g.,
a 28×28 image is flattened into a 784-dimension input vector).
2. Output: The final layer has 10 neurons, one for each digit. The network uses the
Softmax activation function on the output layer, which converts the scores into a
1
--- page 2 ---
probability distribution. The digit corresponding to the highest probability is the
network's prediction.
b) Explain backpropagation using gradient descent algorithm for an artificial neural network.
Ans: Explanation with diagram 2 marks
Backpropagation-3 marks
Backpropagation o compute gradients of the loss function with respect to each weight in the
network. These gradients tell us how to adjust the weights to reduce the error.
Backpropagation computes gradient descent, which uses the gradients to update the weights.
Wnew= Wold+ delta w
c) You are developing a machine learning model for predicting customer churn. How can bootstrapping
and bagging improve the performance of your model? Explain briefly.
Ans: 2.5 Marks each for bootstrapping and bagging
Bootstrap sampling is a technique of creating multiple datasets from the original dataset by random
sampling with replacement. This means each sample in the original dataset can appear more than once
or not at all in a new dataset.
2
--- page 3 ---
Creating Training Datasets in Bagging:
Suppose the original dataset has 1000 samples.
To create a bootstrap sample, randomly select 1000 samples with replacement from the original dataset.
Repeat this process multiple times (e.g., 10–100 times) to create multiple training datasets.
Each of these datasets is slightly different from the others due to the random selection and replacement.
Purpose in Bagging:
Each bootstrap dataset is used to train a separate base learner (e.g., a decision tree).
Combining the predictions of all learners (e.g., by majority voting for classification or averaging for
regression) helps to reduce variance and improve the model’s overall performance.
d) A regression model performs poorly on both training and test data. Another model performs very well
on   training   data   but   poorly   on   test   data.
Identify which model suffers from high bias and which from high variance, and justify your answer.
Ans: 2.5 marks each for the identification of bias and variance and proper justification
Model 1 suffers from high bias. High bias means the model is too simple to capture the underlying data
complexity. It underfits the data. Underfitting causes large errors everywhere—both on training and test
sets.
Model 2 suffers with variance. Performs very well on training data but poorly on test data.
Excellent performance on training data means:
The model learned the training patterns extremely well. Poor performance on test data means:
It fails to generalize the unseen data. High variance occurs when the model is too complex
and fits the training data too closely (overfitting).
 It memorizes the training dataset instead of learning general patterns.
 This leads to low training error but high test error.
Q2
a) What is exploratory data analysis? Explain different steps in exploratory data analysis for model
building.
Ans:
•   Exploratory data analysis (EDA) is used by data scientists to analyze and investigate data sets
and summarize their main characteristics, often employing data visualization methods.
•   Exploratory Data Analysis is a crucial step before you jump to machine learning or modeling
of your data. By doing this you can get to know whether the selected features are good enough
to model, are all the features required, are there any correlations based on which we can either
go back to the Data Pre-processing step or move on to modeling.
Each Step along with example carries 2 marks
3
--- page 4 ---
Steps
•   Description of data
•   Handling missing data
•   Handling outliers
•   Understanding relationships and new insights through plots
b) Write the K-Means Clustering Algorithm. Apply it to the following one-dimensional
dataset:{2,4,10,12,3,20,30,11,25}
Use K = 2 clusters and determine: (i)The final stable clusters. (ii)The centroids of each cluster after
convergence. (iii)Show all steps of the algorithm clearly.
Ans: K-means Algorithm carries 5 marks and Numerical Carries 5 marks
Numerical carries marks
•   Given: {2,4,10,12,3,20,30,11,25}, k=2
• Randomly assign means: m1=3,m2=4
•   K1={2,3}, K2={4,10,12,20,30,11,25}, m1=2.5,m2=16
•   K1={2,3,4},K2={10,12,20,30,11,25}, m1=3,m2=18
•   K1={2,3,4,10},K2={12,20,30,11,25}, m1=4.75,m2=19.6
•   K1={2,3,4,10,11,12},K2={20,30,25}, m1=7,m2=25
•   Stop as the clusters with these means are the same.
4
--- page 5 ---
Q3
a) How does SVM find the optimal separating hyperplane for binary classification? Explain how SVM
uses the kernel trick to handle non-linearly separable data.
Ans: SVM finding optimal separating hyperplane carries 5 marks and any two SVM kernel tricks
carries 5 marks
• A SVM which is used to classify data which are linearly separable is called linear SVM.
•   In other words, a linear SVM searches for a hyperplane with the maximum margin.
•   This is why a linear SVM is often termed as a maximal margin classifier (MMC).
5
--- page 6 ---
@ In matrix form, a hyperplane thus can be represented as

W.X+b=0 (4)

where W =[Wy,W2
constant.

Xm] and bis a real

@ Here, W and b are parameters of the classifier model to be
evaluated given a training set D.

Figure 4: Computation of the MMH

A by +
* te toiy + +t
++ +

Ay

e@ Let us consider a two-dimensional training set consisting two
classes + and - as shown in Fig. 4.

e@ Suppose, 6; and bz are two decision boundaries above and below
a hyperplane, respectively.

e@ Consider any two points X, and X_ as shown in Fig. 4.

e@ For X. located above the decision boundary, the equation can be
written as

W.X,+b=K where K > 0 (5)

e@ Similarly, for any point X_ located below the decision boundary,
the equation is

W.X_+b=k’ where K’ <0 (6)

e Thus, if we label all +’s are as class label + and all -’s are class
label -, then we can predict the class label Y for any test data X as

_f + ifWxX+b>0
m={t ifwW.x+b<0
--- page 7 ---
Non Linear SVM 5 Marks
Kernel functions:
The kernel function is a technique used to transform data into a higher dimension to make it easier to
classify when the data is not linearly separable in its original space.
Common kernel functions include:
•   Linear Kernel: No transformation; works directly in the input space.
•   Polynomial Kernel: Adds polynomial features.
•   Radial Basis Function (RBF) Kernel: Maps data into infinite dimensions using a Gaussian
function.
•   Sigmoid Kernel: Similar to a neural network activation function.
7
--- page 8 ---
•
If we cannot draw a straight line (or hyperplane) to separate the classes in the input space, SVM
needs a non-linear boundary. Using the Kernel trick, z=x2+y2 is used to handle non-linear data.
b) Logistic Regression models the probability of a binary outcome using the logistic (sigmoid) function
carries 5 marks
Logistic Regression models the probability of a binary outcome (e.g., Yes/No, 1/0) by using
the logistic function, also known as the sigmoid function, to map the output of a standard
linear equation into the range of [0,1].
Here is a breakdown of the three key steps:
1. The Linear Model (The "Input")
8
--- page 9 ---
Like Linear Regression, Logistic Regression begins by calculating a linear combination of the
input features (x) and their corresponding weights (β), plus an intercept (β0 or b). This
intermediate result is often denoted as z and is called the log-odds or the logit.
2. The Sigmoid Transformation
This is where the logistic (sigmoid) function comes in. Its purpose is to transform the unbounded
linear output (z) into a value that is strictly bounded between 0 and 1, which can then be interpreted
as a probability.
3. Interpreting the Log-Odds (z) and Probability (P)
The sigmoid function ensures that:
Linear Output (z)   Sigmoid Output (P) Interpretation
z→∞ (Very large positive) P→1   The outcome is almost certain to be 1.
z=0   P=0.5   The outcome is equally likely to be 0 or 1.
z→−∞ (Very large negative) P→0   The outcome is almost certain to be 0.
Numerical on Logistic Regression Carries-5 marks
A company wants to predict whether a candidate will get selected for a job based on the number of
hours they spent preparing for the interview.
The log of odd value is given as: log⁡(odds) = 𝑧= −10.985 + 0.4395 × Hours
i) Calculate the probability that a candidate who prepared for 28 hours will be selected. ii) Determine
the minimum number of hours a candidate should prepare to have a probability of selection of at least
90%.
Ans:
1   1
𝑃=   =   ≈0.789
1 + 𝑒−1.318 1 + 0.268
9
--- page 10 ---
For 28 hours=0.789
13.182
𝑋=   ≈30 hours
0.4394
So, a candidate should prepare at least 30 hours to have ≥ 90% chance of selection.
First part 5 marks,
Second part 5 marks
Q4
a) A Python program to perform the following operations using pandas. (i)Read the CSV file into a Data
Frame. (ii)Display the first 5 records. (iii)Display the number of rows and columns. (iv)Identify
missing values and replace with mean values (v) Perform one-hot encoding on the Department
column.
Each Operation Carries 2 marks
Employee.CSV file
Emp Id Name Age Department Salary Gender
101   Raj   28   HR   45000 Male
102   Meena 32   IT   60000   Female
103   Karan NaN Finance   52000 Male
104   Priya   29   IT   NaN   ,Female
105   Amit   35   HR   48000 Male
1. Reading the CSV into a DataFrame — Bloom: Remember / Understand
o Uses pd.read_csv('employee.csv') correctly and assigns to a DataFrame.
2. Displaying the first 5 records — Bloom: Remember
o Full (1.0): Uses df.head() or df.head(5) and shows output.
3. Finding number of rows and columns — Bloom: Understand
Uses df.shape (or len(df) & df.shape[1]) and reports correctly.
4. Identifying missing values — Bloom: Analyze
o   Uses df.isnull().sum() (or equivalent) and identifies the missing entries in
Age and Salary.
5. Replacing missing Age with mean — Bloom: Apply
o Full (1.5): Computes mean from non-missing ages, uses e.g.
df['Age'].fillna(df['Age'].mean(), inplace=True) and shows updated
values (correct mean used).
6. Replacing missing Salary with median — Bloom: Apply
o Full (1.5): Computes median from non-missing salaries and fills NaN correctly
(e.g., df['Salary'].fillna(df['Salary'].median(), inplace=True))..
7. One-hot encoding Department — Bloom: Apply / Create
10
--- page 11 ---
o Full (1.5): Uses pd.get_dummies(df['Department'],
prefix='Department') or pd.get_dummies(df,
columns=['Department']), correctly appends/replaces columns and drops
original if required. All department categories handled.
b) Design Dendrogram and form clusters by applying Agglomerative algorithm with the following data
stored in adjacency distance matrix using single link approach and complete link technique.
Designed of Dendrogram with single link carries 5 marks by solving adjacency matrix at every level
by single link distance.
11
--- page 12 ---
Designed of dendrogram using complete link with steps carries 5 marks by solving adjancy matrix at
every level.
12
--- page 13 ---
Q5
a) Explain the major 4 challenges faced in Unsupervised Learning and illustrate each challenge with
suitable examples.
Four challenges with explanation carries 2 marks each and example carries 2 marks(4*2+2=10)
Point   Explanation   Marks
No predefined labels make it
1. Lack of Ground   difficult to evaluate model
1.5
Truth / Labels   performance or validate cluster
quality.
2. Determining the   Algorithms like K-Means require k
Right Number of   as input; choosing optimal k is   1.5
Clusters or Groups   challenging.
It’s often unclear what each cluster
3. Interpretability of
or pattern represents in real-world   1
Results
terms.
4. Sensitivity to   Many algorithms (e.g., K-Means)
Initialization /   depend on initial centroid selection, 1
Parameters   leading to different outcomes.
In high dimensions, distances
5. Handling High-
become less meaningful (curse of   1.5
Dimensional Data
dimensionality).
6. Noisy or   Noise and outliers can distort
1
Overlapping Data   clusters and reduce accuracy.
13
--- page 14 ---
Algorithms may become
7. Scalability Issues   computationally expensive for large 1
datasets.
Choosing metrics like silhouette
8. Evaluation Metrics   score, Davies–Bouldin index, etc., is 1.5
non-trivial.
b) Design a Decision Tree for the given dataset using the ID3 algorithm. Calculate the entropy and
information gain for each attribute. Find the best root node. Mention the steps clearly. All the answers
to be mentioned to the 4th decimal.
Study Hours 0.6951
Homework 0.0461
Attendance 0.0020
Best root node=Study hours
Entropy of the entire dataset 1 marks, 3 marks each for gain calculation of 3 independent variables.
14
--- page 15 ---
CO) “Belg Car 5
ia |

lo 2 rea Oa

= O4401 + 0. sogy, = SS ASL Qe
entreP gy pa ASrodstoons-
nCS dH9D) os = S'9g,.05 = oo

“Creag rns, = St -Vegcr) —e"

milous

FS BQnosegqy PAK VST
= 038411 + OS2=3
a o-A1e2.

~~. eperghted Sum op opy =,

\o 1D ae
=, Gales re
Fngoe Gy ot = HW) —H CBredyHoo )
= o-ANos —o-24S54C
= o-¢4S\

Le eens Artendon® as Spit
ACA Do a ee SregsCa) + 2199, C «12D
= O-C¢c6 KO*SE44 HY 0'3395 aw Vsegy

—r+ 3 mers

= 0-3¢18 + O'S282
= -O-91e

15
--- page 16 ---
Study
Attendance Homework Result
Hours
High   Regular   Yes   Pass
High   Irregular   No   Pass
Medium Regular   Yes   Pass
Low   Regular   No   Fail
Low   Irregular   No   Fail
Medium   Irregular   No   Fail
Medium Regular   No   Pass
High   Regular   No   Pass
Low   Regular   Yes   Fail
High   Irregular   Yes   Pass
16
--- page 17 ---
Q6
a) Answer
Predicted:   Predicted:   Predicted:
Brain Tumor Type
Glioma (0)   Meningioma (1)   Pituitary (2)
Actual: Glioma (0)   5   2   1
Actual: Meningioma
1   6   1
(1)
Actual: Pituitary(2)   0   2   2
From this matrix we can compute metrics:
For Class 0 (Glioma): 2.5 marks
 TP = 5 (correctly predicted Apples)
 FP = 1 + 0 = 1
 FN = 2 + 1 = 3
 TN = 20 - (TP+FP+FN) = 20 - 9 = 11
So,
   Precision (Glioma) = TP / (TP+FP) = 5 / (5+1) = 0.833
   Recall (Glioma) = TP / (TP+FN) = 5 / (5+3) = 0.625
For Class 1 (Meningioma): 2.5 marks
 TP = 6
 FP = 2 + 2 = 4
 FN = 1 + 1 = 2
 TN = 20 - (6+4+2) = 8
So,
   Precision (Meningioma) = 6 / (6+4) = 0.6
   Recall (Meningioma) = 6 / (6+2) = 0.75
For Class 2 (Pituitary): 2.5 marks
 TP = 2
 FN = 2
 TN = 20 - (2+2+2) = 14
17
--- page 18 ---
So,
   Precision (Pituitary) = 2 / (2+2) = 0.5
   Recall (Orange Pituitary = 2 / (2+2) = 0.5
Overall Accuracy 1 marks
   Accuracy=Correct PredictionsTotal Predictions\t{Accuracy} =
Predictions}}Accuracy=Total PredictionsCorrect Predictions
   Correct predictions = diagonal sum = 5 + 6 + 2 = 13
Total = 20
   Accuracy=13/20=0.65=65
Justification carries 1.5 marks
b)
Apply Naïve Bayesian Algorithm to classify incoming tuple T
T={Age=Old, Competition=Yes, Industry=Hardware} as Low or High
Marks mentioned against the solved problem
18
--- page 19 ---
Q7
A The sale of company in million dollars for each year are shown in table:
X(Years)   2005   2006   2007   2008   2009
Y (Sales)   12   19   29   37   45
Find
a. Least Square Regression Line y=ax+b
b. Use Least Square Regression Line as a model to estimate sale of company in 2012
Compute the Mean Squared Error (MSE) for the given data using the obtained regression model.
Analyze and comment on the performance and accuracy of the model based on the calculated MSE
value.
19
--- page 20 ---
Least square Regression line 5 marks, Estimate sale 2 marks, MSE calculation 2 Marks, Inference 1
Marks
Regression Line 𝑦= 8.4𝑥+ 3.2
Estimated Sale (2012) $70.4 million
Mean Squared Error (MSE)   0.32
20
--- page 21 ---
(b) Estimate sale in 2012—2marks

For 2012: x = 2012 — 2005 = 7.

Peo12 = 8-4(7) + 11.6 = 58.8 + 11.6 = [70.4 million $

(c) Find MSE and comment— 2 marks for MSE and 1 mark for
inerence

First compute predicted values and residuals for the data:

Year x Actual y Predicted # = 8.4x + 11.6 Residual e = y —# e7

2005 0 12.0 11.6 +0.4 0.16
2006 1 19.0 20.0 —1.0 1.00
2007 2 29.0 28.4 +0.6 0.36
2008 3 37.0 36.8 +0.2 0.04
2009 4 45.0 45.2 —0.2 0.04

Sum of squared errors (SSE):

SSE = Fe* = 0.16 + 1.00 + 0.36 + 0.044 0.04 = 1.60

MSE (mean squared error, using nfor average prediction error):

SSE 1.60 “aqe z
MSE = === 0.32 (million $)
nm

RMSE (for interpretability in dollars):

RMSE = VMSE = ¥V0.32 * [0.57 million $

(If instead estimating residual variance for inference, use n — 2 = 3in
denominator: s* = 1.60/3 © 0.533and s * 0.73.)

Comment on performance (based on MSE)

« MSE=0.32 means the average squared prediction error is 0.32 (:

« Compared to sales values (12-45 million), an average error of about
$0.57 million is very small.

« Therefore the linear model fits the data very well and 1s appropriate
for prediction in this range (subject to usual caveats about
extrapolation — e.g.. predictions far beyond observed years may be

less reliable).

21
--- page 22 ---
b   Explain any 2 types of cross validation techniques to improve the performance of machine learning
model, to deal with problem of model overfitting and underfitting.
Ans: Each Technique carries 5 marks along with figures
1. K fold cross validation
 The dataset is split into K equal parts (folds).
 The model is trained on 20-80, 30-70, 50-50, 70-30 etc
   This process repeats K times, each time using a different fold for testing.
   Final performance = average of all K test results.
 The model is tested on multiple different subsets, preventing it from memorizing one
particular train-test split.
 Ensures good generalization.
 Uses a large portion (K–1 folds) for training each time, giving the model more data to
learn from.
2. Stratified K-Fold Cross Validation
(Useful especially in classification problems, e.g., heart disease dataset)
   Similar to K-Fold, but ensures each fold has the same class proportion as the
original dataset.
Example: If original dataset has 60% class 0 and 40% class 1, each fold maintains the
same ratio.
   Prevents training on folds with skewed class distribution.
 Ensures the model does not learn patterns that are biased toward one class.
 Balanced folds help the model learn representative patterns from minority classes.
22
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper bcc4d33de319

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (22 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (EXTC)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Question No.1 is compulsory.
3. Out of remaining questionsa attempt any 4 questions.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figure in brackets on the right hand side indicates full marks.
7. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Define overfitting using an example. Explain its significance.   [05]
SO-   Solution:
1;   Overfitting :
BL   When a machine learning model provides correct predictions for training data but not for
-2   new data, this is known as overfitting, an undesirable machine learning tendency. Data
scientists first train machine learning models on a known data set before using them to
make predictions. The model then attempts to forecast results for fresh data sets using this
information. An overfit model cannot function properly for all kinds of incoming data and
may produce erroneous predictions.
02 Marks
Why?
Overfitting happens when a model sticks too closely to the training data and struggles to
handle new data. Basically, it memorizes the details and noise instead of learning the
actual patterns. This usually comes up for a few reasons. Sometimes, you just don’t have
enough training data, so the model can’t really get a sense of everything it needs to know.
Or maybe the training data has too much random or irrelevant information—what’s called
noisy data—which confuses the model. Training a model for too many rounds on the
same dataset also makes things worse, since it just keeps picking up more noise with each
pass. And if the model itself is too complicated, it tries to capture every tiny detail, even
the ones that don’t matter. That’s why overfitting is such a common headache in machine
learning.
Example: Consider a use case where a machine learning model has to analyze photos and
identify the ones that contain dogs in them. If the machine learning model was trained on
a data set that contained majority photos showing dogs outside in parks , it may may learn
to use grass as a feature for classification, and may not recognize a dog inside a room.
03Marks
CO-1; SO-   b. A dataset contains product categories: Car, Bike, Bus, Car, and Bike. Apply One-Hot   [05]
1;   Encoding to convert this categorical data into numerical format and explain why
BL   assigning simple numeric labels may lead to incorrect interpretations.
-4
********** 1 **********
--- page 2 ---
Solution:
Apply One-Hot Encoding to convert this categorical data into numerical format- 2 marks
explain why assigning simple numeric labels may lead to incorrect interpretations.3
marks
03Marks
One-Hot Encoding converts categorical values into binary vectors, where only one
position is marked as 1 and the rest are 0. This ensures that each category is treated as
independent and equally important.
If we instead assign simple numeric labels such as:
Car = 1, Bike = 2, Bus = 3,
it may lead to incorrect interpretations. Machine learning models may assume an
ordinal relationship (e.g., Bus > Bike > Car), which is not meaningful because these
categories do not have any inherent order.
2Marks
CO-2; SO-1;   c.   Under what circumstances are Precision, or Recall better performance metrics in   [05]
BL-2   comparison with accuracy? Give an example each for the situations where “Recall is a
more important evaluation metric than Precision”.” Precision is a more important
evaluation metric than Recall”.
Solution:
When are Precision or Recall better than Accuracy?
Accuracy works well only when classes are balanced and errors have equal cost.
But in many real-world problems (like **Cancer detection or spam filtering), data is
imbalanced and mistakes have different consequences.
Use Recall when:
• Missing a positive case is very dangerous
• You want to capture as many actual positives as possible
•   False negatives must be minimized
Example:
Disease Detection (e.g., Cancer Screening)
•   If a patient has cancer but the model predicts negative → very risky
•   It’s better to flag more people as positive (even if some are wrong)
•   So, Recall is more important
********** 2 **********
--- page 3 ---
Use Precision when:
•   False positives are costly or harmful
• You want predictions to be highly accurate when positive
• Avoid wrongly labeling negatives as positives
Example:
Email Spam Detection
•   If a normal email is marked as spam → important message may be lost
•   So, predictions labeled “spam” should be very accurate
• Hence, Precision is more important
Summary Table
Metric   Focus   Important When   Example
Minimize False   Missing positive is   Cancer
Recall
Negatives   dangerous   detection
Minimize False   Spam
Precision   False alarms are costly
Positives   filtering
1Mark for each explanation
CO-2; SO-2;   d. Discuss the computational complexity of K-Means and Hierarchical Clustering and its   [05]
BL-2   impact on scalability.
Solution:
K_Means and Hierarchical Clustering: 02 M
Comaparison: 03 M
K-Means is an iterative algorithm.
• Time Complexity:
O(n × k × t × d)
where:
o n = number of data points
o k = number of clusters
o   t = number of iterations
o d = number of features
• Each iteration assigns points to nearest centroid → O(n × k)
• Updating centroids → O(n)
• Repeated for t iterations
Hierarchical clustering builds a tree (dendrogram).
• Time Complexity:
O(n² log n) (optimized) or up to O(n³) (naive)
********** 3 **********
--- page 4 ---
• Space Complexity:
O(n²) (distance matrix)
• Computes pairwise distance matrix → O(n²)
• Repeated merging/splitting of clusters
• Updating distances after each merge
Clustering algorithms differ significantly in computational complexity, which directly
impacts their scalability to large datasets.
K-Means Clustering is relatively efficient and scalable. Its time complexity is
approximately O(n × k × i × d), where n is the number of data points, k is the number of
clusters, i is the number of iterations, and d is the number of features. Since k and i are
usually small, K-Means scales well to large datasets and is widely used in real-time and
big data applications.
In contrast, Hierarchical Clustering (especially agglomerative) has much higher
complexity. Its time complexity is typically O(n² log n) or even O(n³) depending on
implementation, and space complexity is O(n²) due to the need to store distance matrices.
This makes it computationally expensive and less suitable for large datasets.
Impact on scalability:
• K-Means is highly scalable and suitable for large-scale datasets (millions of
points).
•   Hierarchical clustering is limited to smaller datasets due to its high computational
and memory requirements.
Complexity: 02 M
•   Explanation with scalability: 03
1 Mark for each correct step
Q2   a.   The following table records the number of balls that Ayush took for scoring runs. In   [10]
CO-2;   how many balls is he likely to score a century?
SO-
2;   Runs   Number of
BL-   Scored   Balls
4   8   10
35   20
47   31
54   23
11   5
85   47
84   35
93   67
89   73
2   1
Solution:
********** 4 **********
--- page 5 ---
x = Runs scored
y = Number of balls
We need to predict the number of balls required when Ayush scores 100 runs.
We use the linear regression model:
y = mx + b,
where y and x are variables,
m is the slope, and
b is the y-intercept.
The equations for m and b are as below -
m = (n∑xy - ∑y∑x)/[n∑x2 - (∑x)2]
b = (∑y - m∑x)/n
∑xy = 23199
∑y = 312
∑x = 508
∑x2 = 37390
(∑x)2 = 508*508
m = (n∑xy - ∑y∑x)/[n∑x2 - (∑x)2]
= (10*23199-312*508) / [10*37390-(508*508)]
m = 0.634466
b = (∑y - m∑x)/n
b= (312-0.634466*508)/10
b = -1.03087
The equation will be –
Y = 0.634466*X + (-1.03087)   08 Marks
Predict balls for 100 runs i.e.x=100
Substitute x=100 in regression line equation.
Y = 0.634466*100 + (-1.03087) = 62.41573
Ayush requires 62 balls to score 100 runs.
2Marks
Q2   b. Explain how nonlinear data can be classify using SVM? Explain different kernel   [10]
CO-2; SO-2;   functions used classification.
BL-2   Solution:
If the dataset is not linearly separable, SVM uses a nonlinear decision boundary
to classify the data. This is called a nonlinear SVM.
1Mark
Key Idea-
Instead of drawing a straight line, nonlinear SVM:
• Transforms the data into a higher-dimensional space
• Uses a kernel function to make the data separable
• Then finds a linear boundary in that higher dimension, which appears
nonlinear in original space
•   1Mark for each explanation (04)
********** 5 **********
--- page 6 ---
Kernal functions are used to deal with nonlinear SVM
Explanation how nonlinear SVM is analyzed using kernel function:
Different types of kernel functions are:
i) Homogeneous polynomial kernel
ii) Non-homogeneous polynomial kernel
iii) Radial basis function
iv) Sigmoid kernel function
1Mark for each explanation of kernel function with equation
(05)
Q3   a. A company analyzes employee attrition using the following dataset:   [10]
CO-3;
SO-6;
BL-3   Experience   Satisfaction   Leave
High   Low   Yes
High   Medium   No
Medium   Low   Yes
Low   Medium   No
Low   High   No
Medium   High   No
Apply ID3 algorithm to:
•   Calculate Entropy of target variable
• Compute Information Gain of attributes
•   Identify the root node
Solution:
Step 1: Dataset Summary
Total samples = 6
Target (Leave):
• Yes = 2
• No = 4
Step 2: Entropy of Target Variable
[
Entropy(S) = - (2/6)\log_2(2/6) - (4/6)\log_2(4/6)
]
[
= - (0.333)(-1.585) - (0.667)(-0.585)
]
[
= 0.528 + 0.390 = 0.918
********** 6 **********
--- page 7 ---
]
Entropy(S) = 0.918
03Marks
Step 3: Information Gain Calculations
(A) Attribute: Experience
Ye N Tota
Experience   Entropy
s   o   l
High   1 1 2   1
Medium   1 1 2   1
Low   0 2 2   0
[
Weighted = (2/6)(1) + (2/6)(1) + (2/6)(0)
]
[
= 0.333 + 0.333 + 0 = 0.666
]
[
IG(Experience) = 0.918 - 0.666 = 0.252
]
IG(Experience) = 0.252
03Marks
(B) Attribute: Satisfaction
Ye N Tota
Satisfaction   Entropy
s   o   l
Low   2 0 2   0
********** 7 **********
--- page 8 ---
Medium   0 2 2   0
High   0 2 2   0
[
Weighted = (2/6)(0) + (2/6)(0) + (2/6)(0) = 0
]
[
IG(Satisfaction) = 0.918 - 0 = 0.918
]
IG(Satisfaction) = 0.918
03Marks
Step 4: Root Node Selection
•   IG(Experience) = 0.252
•   IG(Satisfaction) = 0.918
Root Node = Satisfaction (highest IG)
01Mark
Q3   b. A hedge fund analyzes 200+ financial indicators (prices, volatility, macroeconomic   [10]
CO-1;   factors). The dataset suffers from multicollinearity and noise, leading to unstable
SO-1; BL-2   predictive models.
Tasks:
1. Explain how PCA can address multicollinearity in this dataset.
2. How would you decide the number of principal components to retain?
3. Discuss potential risks of using PCA in financial decision-making.
Solution:
A hedge fund often works with a very large number of financial variables such as stock
prices, returns, volatility measures, interest rates, inflation, exchange rates, sector indices,
and macroeconomic indicators. In such datasets, many variables are highly correlated
with each other. This creates multicollinearity, which makes predictive models unstable.
Also, noisy and redundant features increase computational complexity and reduce model
reliability.
Principal Component Analysis (PCA) is a dimensionality reduction technique that can
help solve these issues by transforming the original correlated variables into a smaller set
********** 8 **********
--- page 9 ---
of new uncorrelated variables called principal components.
1. How PCA can address multicollinearity in this dataset
Meaning of multicollinearity
Multicollinearity occurs when two or more input variables are strongly correlated. In
finance, this is very common because many indicators move together.
For example:
•   stock price and moving average may be strongly related
•   inflation and interest rate may influence each other
•   sector indices may follow the same market trend
When multicollinearity exists:
• model coefficients become unstable
•   small changes in data can produce large changes in predictions
•   interpretation of variable importance becomes difficult
•   regression models may overfit or behave inconsistently
How PCA solves this
PCA transforms the original set of correlated features into a new set of variables called
principal components.
These principal components have two key properties:
1. They are linear combinations of original variables
2. They are uncorrelated with each other
So, instead of directly using 200 correlated financial indicators, the hedge fund can use a
smaller number of principal components that summarize the major patterns in the dataset.
Why this reduces multicollinearity
Since the principal components are orthogonal, there is no correlation among them. This
removes the multicollinearity problem.
Practical effect in hedge fund modeling
Using PCA:
•   correlated indicators are compressed into a few market factors
•   regression or prediction models become more stable
•   estimation becomes more reliable
•   redundant information is removed
•   noise can be reduced by discarding less important components
********** 9 **********
--- page 10 ---
Example intuition
Suppose many indicators reflect overall market movement. PCA may combine them into
one principal component representing market trend. Another component may capture
volatility behavior. A third may represent macroeconomic pressure. Thus, instead of
200 raw variables, a model may work with 10–20 meaningful components.
2. How to decide the number of principal components to retain
Choosing the correct number of principal components is very important. If too few are
kept, useful information may be lost. If too many are kept, noise and redundancy may
remain.
Several methods are used:
A. Explained Variance Criterion
Each principal component explains some portion of the total variance in the data.
• The first component explains the maximum variance
• The second explains the next highest variance
• and so on
A common rule is to retain enough components to explain 80% to 95% of the total
variance.
In finance
A hedge fund may choose enough components to explain around 90%–95% variance,
especially when trying to preserve important market structure.
Advantage
• Simple and widely used
• Gives a quantitative basis for selection
Limitation
• High explained variance does not always mean high predictive usefulness
B. Scree Plot Method
A scree plot shows eigenvalues versus component number.
• The curve usually drops sharply at first
• Then it begins to flatten
The point where the curve starts flattening is called the elbow point. Components before
this point are usually retained.
********** 10 **********
--- page 11 ---
Meaning
Beyond the elbow, extra components add only small amounts of information and may
mainly represent noise.
C. Kaiser Criterion
According to this rule, keep components with eigenvalue greater than 1.
Reason
An eigenvalue greater than 1 indicates that the component explains more variance than an
individual standardized original variable.
Limitation
This rule is more useful in moderate-sized datasets and may not always be ideal for large
financial datasets.
D. Cross-Validation / Model Performance
A more practical approach is to try different numbers of principal components and test the
predictive model performance.
For example:
•   train model with first 5 components
•   then with 10 components
•   then with 15 components
• compare prediction accuracy, stability, and risk metrics
3. Potential risks of using PCA in financial decision-making
Although PCA is useful, it also has important risks, especially in finance where decisions
involve high uncertainty and financial loss.
A. Loss of Interpretability
The original variables are easy to understand, such as inflation, interest rates, or stock
returns. But principal components are combinations of many variables.
This makes interpretation difficult.
Risk
A portfolio manager may not clearly understand what a principal component
economically represents. This can reduce trust in the model.
B. Important Low-Variance Features May Be Discarded
********** 11 **********
--- page 12 ---
PCA keeps components with the highest variance and removes low-variance components.
However, in finance, some low-variance variables may contain important predictive
signals.
Example
A small but consistent macroeconomic indicator may have low variance but still be very
useful for forecasting a crisis.
Risk
Discarding such components may harm prediction quality.
01Mark for each correct explanation (10 steps must be written)
Q4   a. A regression model gives a high R-squared value but poor predictive accuracy.   [10]
CO-2;
SO-   Analyse this situation and relate it to potential issues such as overfitting or data
2;   distribution.
BL-   Solution:
2   A regression model may show a high R-squared value but still have poor predictive
accuracy when it fits the training data well but fails to generalize to new or unseen
data. This means the model explains a large proportion of variance in the available
dataset, yet its practical prediction performance is weak.
Meaning of high R-squared
R-squared measures the proportion of variation in the dependent variable explained
by the independent variables. A high value suggests that the model fits the observed
data closely.
However, a good fit on test data does not always guarantee good prediction on test
data.
Overfitting as a major reason
One common reason is overfitting. Overfitting occurs when the regression model
learns not only the true pattern in the data but also the random noise. This usually
happens when:
•   too many predictors are included,
•   higher-order polynomial terms are used unnecessarily,
•   the model becomes too complex for the size of data.
********** 12 **********
--- page 13 ---
In such cases, the model performs very well on training data, giving a high R-squared,
but performs poorly on test or validation data.
Problems related to data distribution
Poor predictive accuracy may also arise because of data distribution issues.
Examples include:
a) Training and test data mismatch
If test data has a different distribution from training data, the model may not work
well even if training fit is excellent.
b) Presence of outliers
A few extreme values can distort regression coefficients and create misleadingly high
goodness-of-fit.
c) Non-linearity
If the true relationship is not linear but a linear regression model is applied, R-squared
may appear acceptable on one dataset but prediction may fail on others.
d) Heteroscedasticity
When error variance is not constant, predictions become unreliable across different
ranges of input values.
01Mark for each correct explanation
Q4   b. The 2×2 Image given bellow is applied to the fully connected neural network with   [10]
CO-3;
SO-6;   sigmoid activation function. calculate the following
BL-6
a. Predicted output after first epoch.
b. Mean square error after first epoch.
c.   If learning rate of 0.05 find the updated value of weight W14 using error
back propagation algorithm.
Assume bias at hidden layer neurons b1=0.30, and bias at output layer neuron
b2=0.50 and weights are given in following table.
W1   W2   W3   W4   W5   W6   W7   W8   W9   W10   W11   W12   W13   W14   W15
0.10   0.20   0.30   0.40   0.50   0.60   0.70   0.80   0.90   0.65   0.75   0.95   0.75   0.55   0.85
Inputs applied to the input layer is
X1   X2   X3   X4
0.40   0.55   0.65   0.85
********** 13 **********
--- page 14 ---
Solution:
Input to neural network are we convert 2D image in to 1D image by converting rows
in to columns so the inputs to neural network are x1=0.40,x2=0.55,x3=0.65,x4=0.85
Predicted output after first epoch
a. h11in=b1+w1x1+w4x2+w7x3+w10x4 =1.5575
h11out=1/(1+e- h11in)=0.4627
b. h12in= b1+w2x1+w5x2+w8x3+w11x4 =1.8125
h12out=1/(1+e- h12in)=0.3555
c. h13in=b1+w3x1+w6x2+w9x3+w12x4 =2.1425
h13out=1/(1+e- h11in)=0.3182
d. O1in=b2+w13 h11out +w14 h12out +w15 h13out =1.3129
O1out=1/(1+e- O1in)=0.4323
05Mark
Mean square error after first epoch
Mean Square error after first epoch =1/2[(O1-T1)2]= 1/2[(O11out -T1)2=]
= 1/2[(0.4323 -0.82)2]
Mean Square error after first epoch =0.0.0751
02Mark
If learning rate of 0.05 find the updated value of weight w14 using error back
propagation algorithm.
w14New=0.5481
Steps for updating weight
********** 14 **********
--- page 15 ---
03Mark
Q5   a. Explain Ensemble Learning. Discuss how ensemble methods improve the performance   [10]
CO-3;   of Decision Trees.
SO-
1;   Solution:
BL   Ensemble Learning
-3
Ensemble Learning is a technique where multiple models are combined to improve
overall performance.
Instead of relying on a single model, multiple weak learners are used to create a
strong learner.
Types of Ensemble Methods
********** 15 **********
--- page 16 ---
1. Bagging
2. Boosting
3. Random Forest
How Ensemble Improves Decision Trees
Decision Trees suffer from:
• High variance
•   Overfitting
Ensemble methods solve these issues:
1. Bagging (Bootstrap Aggregation)
•   Multiple datasets created using sampling with replacement
•   Train separate trees
•   Final output = majority voting / averaging
Reduces variance
2. Random Forest
• Extension of bagging
• Random feature selection + multiple trees
More robust and less correlated trees
3. Boosting
• Models trained sequentially
• Focus on correcting previous errors
Examples:
• AdaBoost
********** 16 **********
--- page 17 ---
• Gradient Boosting
Reduces bias + variance
1 Mark for each correct steps/explanation
Q5   b. Implement K-Means clustering with K = 3 on the following dataset. Use the first three [10]
CO-2;
SO-2;   points as the initial cluster centroids and apply Euclidean distance to assign points to
BL-2
clusters. Perform two iterations of the algorithm. Show:
1. Initial centroids
2. Distance calculations
3. Cluster assignment after each iteration
4. Updated centroids
5. Final grouping after two iterations.
The Dataset is: {(2,4),(3,5),(4,6),(8,8),(9,9),(10,10),(15,3),(16,4),(17,5)}
Solution:
Step 1: Initial Centroids
Since the first three points are taken as the initial centroids:
• C1=(2,4
•   C2=(3,5)
•   C3=(4,6)
Dataset: (2,4), (3,5), (4,6), (8,8), (9,9), (10,10), (15,3), (16,4), (17,5)
Initial Centroids: C1 = (2,4) C2 = (3,5) C3 = (4,6)
Iteration 1: Cluster 1: (2,4) Cluster 2: (3,5) Cluster 3: (4,6), (8,8), (9,9), (10,10), (15,3),
(16,4), (17,5)
Updated Centroids:
05Mark
********** 17 **********
--- page 18 ---
C1 = (2,4) C2 = (3,5) C3 = (11.29, 6.43)
Iteration 2: Cluster 1: (2,4) Cluster 2: (3,5), (4,6) Cluster 3: (8,8), (9,9), (10,10), (15,3),
(16,4), (17,5)
Final Centroids: C1 = (2,4) C2 = (3.5, 5.5) C3 = (12.5, 6.5)
05Mark
Q6   a. Describe the steps involved in preparing data for a regression model. Explain the   [10]
CO-2;   importance of selecting variables, handling missing values, and checking data
SO-2;
BL-5   consistency for regression model building.
Solution:
Preparing data for a regression model involves understanding the problem, collecting
and organizing data, selecting relevant variables, handling missing values, checking
consistency, and performing cleaning and transformation. Among these, variable
selection, missing value treatment, and consistency checking are especially
important because they directly affect the accuracy, reliability, and interpretability of
the regression model. Proper data preparation forms the foundation for building an
effective regression model.
02Mark
Importance of selecting variables
Handling missing values
04Mark
Checking data consistency.
Explain all in detail..
04Mark
********** 18 **********
--- page 19 ---
Q6   b. For the data set give bellow has 10 samples Create a confusion matrix and Calculate   [10]
CO-4;   Accuracy, Precision, Recall, F1-score. Assume Car as Positive Class.
SO-
6;
BL-   No Expected/Actu
4   Predicted
.   al
1   Car   Car
2   Bike   Bike
3   Car   Bike
4   Bike   Bike
5   Car   Car
6   Bike   Car
7   Car   Car
8   Bike   Bike
9   Car   Bike
10   Bike   Car
Solution:
• TP (True Positive) → Car predicted as Car = 3 (1, 5, 7)
• TN (True Negative) → Bike predicted as Bike = 3 (2, 4, 8)
• FP (False Positive) → Bike predicted as Car = 2 (6, 10)
• FN (False Negative) → Car predicted as Bike = 2 (3, 9)
03Mark
Confusion Matrix
Predicted Car   Predicted Bike
Actual Car   TP = 3   FN = 2
Actual Bike   FP = 2   TN = 3
02Mark
Accuracy= Tp+TN/Total= 6/10 = 0.6
PRECISION=TP/TP+FP=3/5= 0.6
RECALL=TP/TP+FN=3/5= 0.6
F1=0.6
05Mark
********** 19 **********
--- page 20 ---
Q7   a. Explain Bagging and Boosting techniques in detail. Compare their working mechanisms [10]
CO-2;   and their impact on bias and variance.
SO-
2;   Solution
BL-
2   Bagging (Bootstrap Aggregation)
• Random sampling with replacement
•   Parallel model training
• Equal weight to all models
Working:
1. Create multiple datasets
2. Train models independently
3. Aggregate results
Reduces variance
Boosting
•   Sequential learning
• Each model focuses on previous errors
Working:
1. Train first model
2. Increase weight of misclassified points
3. Train next model
4. Combine weighted results
Reduces bias and variance
Comparison
Aspect   Bagging   Boosting
Training   Parallel   Sequential
********** 20 **********
--- page 21 ---
Reduce
Focus   Reduce bias + variance
variance
Data
Random   Weighted
sampling
Can overfit if not
Overfitting   Less
controlled
Example   Random Forest AdaBoost
01 Mark for each correct explanation
Q7   b. What factors should be considered while selecting a machine learning model?   [05]
CO-1;   Solution:
SO-
2;   Things to Take Into Account When Choosing a Machine Learning Model
BL-
2   The nature of the issue
Tasks involving classification, regression, or grouping
The dataset's size
Complex models are supported by large datasets, while simpler models are needed
for small datasets.
Data Quality
Model selection is impacted by the existence of noise, missing variables, and outliers.
Dimensionality of Features
Models like SVM or dimensionality reduction methods may be necessary for high-
dimensional data.
Complexity of the Model
Strike a balance between overfitting and underfitting (bias–variance trade-off).
Interpretability
Compared to sophisticated outational Cos, simple models (such decision trees and
linear regression) are simpler to understand.
Certain models, like deep learning models, demand a lot of processing power.
Measures of Performance
Depending on the issue, accuracy, precision, recall, F1-score, and RMSE
Scalability
The model's capacity to manage expanding data
0.5 Mark for each correct explanation
Q7   c. A bank analyzes transaction amounts (in ₹):   [05]
CO-1;   200, 220, 250, 270, 300, 320, 350, 400, 2000
SO-
6;   Apply the IQR method to detect any abnormal amount. Based on your findings, decide
BL-   how you should treat the extreme value.
2
********** 21 **********
--- page 22 ---
Solution:
Apply IQR 3 mark
Outlier Treatment 2 marks
To detect abnormal transaction amounts using the IQR (Interquartile Range)
method, we first arrange the data in ascending order:
200, 220, 250, 270, 300, 320, 350, 400, 2000
The total number of observations is 9. The median (Q2) is the 5th value, which is
300.
Now, we divide the dataset into two halves (excluding the median):
• Lower half: 200, 220, 250, 270 → Q1 = (220 + 250) / 2 = 235
• Upper half: 320, 350, 400, 2000 → Q3 = (350 + 400) / 2 = 375
Next, calculate the IQR:
IQR = Q3 − Q1 = 375 − 235 = 140
Now, compute the bounds:
• Lower bound = Q1 − 1.5 × IQR = 235 − (1.5 × 140) = 235 − 210 = 25
• Upper bound = Q3 + 1.5 × IQR = 375 + 210 = 585
Any value outside the range 25 to 585 is considered an outlier.
Here, 2000 > 585, so ₹2000 is an outlier (abnormal transaction).
The transaction amount ₹2000 is significantly higher than the rest of the data. The
appropriate treatment depends on the context:
•   If the transaction is legitimate (e.g., a genuine high-value transfer), it should
be retained, as it may indicate important customer behavior.
•   If it is fraudulent or suspicious, it should be flagged for investigation rather
than removed.
•   If it is due to a data entry error, it should be corrected or removed.
• For analytical purposes, we may apply capping (winsorization) by replacing
₹2000 with the upper bound (₹585) to reduce its impact on statistical models.
03 Marks
********** 22 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper fe24c6471025

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIDS_7056/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/MBA
Tech (AI)
Year: II/Sem 4 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 30 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q
1   Answer briefly:   [20]
C   a
O-
1;
S
Analyze a traffic management system that needs to forecast congestion and group similar
O-
traffic behaviors. Identify suitable ML tasks, describe data collection methods, and explain [5]
1;
how these tasks can complement each other.
B
L-
2
Suitable Machine Learning Tasks (4 marks)
Traffic congestion prediction - Supervised learning -Regression (predict traffic speed,
travel time) and Classification (e.g., low / medium / high congestion)
Traffic pattern grouping - Unsupervised learning- Clustering (group similar traffic
behaviors across time/locations)
Clustering finds patterns, prediction uses those patterns to forecast the future.
Data Sources (1 marks) - Sensors & IoT devices, mobile or GPS, Historical traffic records
etc.
C   b
O-
2;
A dataset contains features such as “City,” “Satisfaction Level (Low, Medium, High),” and
S
“Temperature.” Explain how each feature should be treated based on whether it is nominal, [5]
O-
ordinal, or interval data, and justify your preprocessing choices.
1;
B
********** 1 **********
--- page 2 ---
L-
2
Type (1 mark)
Preprocessing (2 marks)
Justification (2 marks)
Feature   Type   Preprocessing   Why It Matters
City   Nominal   One-hot   Avoids false order
encoding
Satisfaction Level   Ordinal   Ordinal encoding   Preserves ranking
Temperature   Interval   Scaling   Ensures numerical stability
C   c
O-
3;
S   You are given a small dataset with class imbalance (e.g., 90% negative, 10% positive).
O-   Which validation technique would you choose among holdout, k-fold, LOOCV, and
[5]
2;   stratified cross-validation? Justify your choice and explain how it improves model
evaluation.
B
L-
3
stratified cross-validation (1 mark)
Justification (3 marks)
1. Holdout Method - random split may produce uneven class distribution
2. Standard k-Fold Cross-Validation - data is split into k folds randomly. Some folds may
have very few minority class samples
3. Leave-One-Out Cross-Validation (LOOCV)- each test set has only one sample. With
imbalance, most test cases will be negative
4. Stratified cross-validation - each fold preserves the original class distribution i.e., ~90%
negative and ~10% positive in every fold.
How it improves model evaluation (1 mark)
1. Balanced Representation
2. Reliable Performance Metrics
3. Reduced Variance- results across folds are more stable, avoids random fluctuations due
to class imbalance
4. Better Generalization Estimate- mimics real-world distribution in every split.
C   d
O-   A classifier outputs probabilities for 10 samples:
4;   Sample   1   2   3   4   5   6   7   8   9   10
S
O-   Probability 0.9   0.8   0.7   0.6   0.55   0.45   0.4   0.3   0.3   0.1
[5]
2;   Actual   1   1   0   1   0   1   0   0   1   0
class
B   (i) Construct confusion matrices at thresholds 0.5 and 0.7
L-   (ii) Compute TPR and FPR for both thresholds
3
Predictions (1 marks)
Sample   1   2   3   4   5   6   7   8   9   10
Probability 0.9   0.8   0.7   0.6   0.55   0.45   0.4   0.3   0.3   0.1
Actual   1   1   0   1   0   1   0   0   1   0
class
T>=0.5   1   1   1   1   1   0   0   0   0   0
********** 2 **********
--- page 3 ---
T>=0.7   1   1   1   0   0   0   0   0   0   0
Confusion matrix (2 marks)   +   -
+   -   +   2   3
+   3   2   -   1   4
-   2   3
TPR & FPR (2 marks)
FPR= FP / (FP + TN)
TPR= TP / (TP + FN)
Q   a
2
C
O-
2;
(i) What is feature binarization? and why is it used in machine learning?
S
(ii) what is the importance of data visualization. Briefly explain Name and briefly explain   [5]
O-
histogram, scatter plot, box plot with example.
1;
B
L-
2
Feature binarization (1 mark)
It is a preprocessing technique where numerical or continuous data is converted into binary
values (0 or 1) using a threshold.
Value > threshold → 1
Value ≤ threshold → 0
Why it is used (1 mark)
• Simplifies data → Converts complex values into simple binary form
• Improves model efficiency → Faster computation and less memory
• Works well with some algorithms → e.g., Naive Bayes
• Reduces noise → Minor variations are ignored
• Helps decision-making → Clear yes/no classification
Data visualization (1 mark)
It is the graphical representation of data using charts, graphs, or plots to make information
easy to understand.
• Helps in understanding patterns and trends
• Makes complex data easy to interpret
• Aids in decision-making
• Helps detect outliers and anomalies
• Improves communication of insights
Three plots (2 marks)
Q   b A dataset contains two classes with the following distribution: 9 instances of Class A and
2   7 instances of Class B. Calculate the entropy of the dataset and interpret the level of
C   impurity.
O-
5;
[5]
S
O-
2;
B
********** 3 **********
--- page 4 ---
L-
3
Step 1: Entropy Formula (1 Mark)
𝐻= −𝑝1log⁡2 𝑝1 −𝑝2log⁡2 𝑝2
Step 2: Calculate Probabilities (1 Mark)
Total instances = 16
𝑝𝐴= 9/16 = 0.5625,𝑝𝐵= 7/16 = 0.4375
Step 3: Entropy Calculation (2 Marks)
𝐻= −(0.5625log⁡2 0.5625 + 0.4375log⁡2 0.4375)
≈−(0.5625 × −0.83 + 0.4375 × −1.19)
≈0.467 + 0.521 = 0.988
Step 4: Interpretation (1 Mark)
• Entropy ≈ 0.99 (close to 1)
•   Indicates high impurity
Classes are almost evenly mixed
c A dataset contains information about a customer buys a product (Buy = Yes / No) based
Q   on age, income and he is student or not. Using Naive Bayes, classify the following instance:
2   X= (Young, Medium, Yes)
C   No.   Age   Income   Student   Buy
O-   1   Young   High   No   No
4;   2   Young   High   No   No
S   3   Middle   High   No   Yes   [10]
O-   4   Old   Medium   No   Yes
2;   5   Old   Low   Yes   Yes
6   Old   Low   Yes   No
B   7   Middle   Low   Yes   Yes
L-   8   Young   Medium   No   No
3   9   Young   Low   Yes   Yes
10   Old   Medium   Yes   Yes
Priori probabilities (1 marks)
Likelihood probabilities (4 marks)
Posterior probability (4 marks)
********** 4 **********
--- page 5 ---
Class is yes (1 mark)
Q   a
3
C   Using the given dataset, apply gradient descent to a simple linear regression model and carry out
O-   two iterations. Assume initial parameter values as zero and use a learning rate of α = 0.01.
3;
S   Study Hours   1 2   3   4   5   [10]
O-   Exam Scores   5 9 13 17 15
2;
B
L-
3
Iteration – 1 (5 marks)
alpha=   0.01
h(x) =   0 +   0 X
x   y   h(x) = h(x) -y (h(x) -y)^2 (h(x) -y )*x
1   5   0   -5   25   -5
2   9   0   -9   81   -18
3   13   0   -13   169   -39
4   17   0   -17   289   -68
5   15   0   -15   225   -75
-59   789   -205
m=   5
Cost J   78.9
theta 0   0.118
theta 1   0.41
Iteration – 2 (5 marks)
********** 5 **********
--- page 6 ---
alpha=   0.01
h(x) =   0.118 +   0.41 X
x   x   y   h(x) =   h(x) -y (h(x) -y)^2 (h(x) -y )*x
1   5   0.528   -4.472 19.99878   -4.472
2   9   0.938   -8.062 64.99584   -16.124
3   13   1.348   -11.652 135.7691   -34.956
4   17   1.758   -15.242 232.3186   -60.968
5   15   2.168   -12.832 164.6602   -64.16
-52.26 617.7425   -180.68
m=   5
Cost J   61.77425
theta 0   0.22252
theta 1   0.77136
b Consider the following dataset with two class (+1) and (-1).
Point   (x₁, x₂)   Class
Q
A   (1,3)   +1
3
B   (2,4)   +1
C
C   (5,2)   −1
O-
D   (6,3)   −1
4;
S   [10]
Two candidate hyperplanes are given:
O-
H1: −3x1 + 2x2 + 2.5 = 0
2;
H2: 2x1 + x2 −10 = 0
B
For   each   hyperplane,   compute   the   decision   function:   f(x) = w ⋅x + b
L-
for all data points and determine their predicted class labels. For each hyperplane, compute
3
the margin. Among the given hyperplanes, determine the optimal SVM hyperplane. Justify
your choice based on both classification correctness and margin.
W and b values (1 mark)
For H1 (3 marks)
Point   Calculation   f(x)   Predicted   Actual
A(1,3)   -3 + 6 + 2.5   5.5   +1   +1
B(2,4)   -6 + 8 + 2.5   4.5   +1   +1
C(5,2)   -15 + 4 + 2.5 -8.5   −1   −1
D(6,3)   -18 + 6 + 2.5 -9.5   −1   −1
All points correctly classified
Margin=2/sqrt(13)
For H2 (3 marks)
Point   Calculation   f(x)   Predicted   Actual
A(1,3)   2 + 3 - 10   -5   −1   +1
B(2,4)   4 + 4 - 10   -2   −1   +1
C(5,2)   10 + 2 - 10   2   +1   −1
D(6,3)   12 + 3 - 10   5   +1   −1
All points are misclassified
Margin=2/sqrt(5)
Optimal hyperplane is H1(3 marks)
A hyperplane with larger margin is useless if it misclassifies data.
Validity > Margin in SVM selection.
********** 6 **********
--- page 7 ---
Q   a
4
C
O-
2;   Explain how transforming input features can simplify a learning problem. Support your
S   answer with the given data: (1,10,100,1000) by applying log transformation.
[5]
O-
1;
B
L-
2
Explanation (2 marks)
Transforming input features simplifies a learning problem by reshaping the data into a form
where patterns become easier for a model to capture. Instead of forcing a model to learn
complex relationships, we modify the input, so the relationship appears simpler.
Example (3 marks)
Raw → highly skewed
After log transform → (0,1,2,3)
Relationship becomes linear and stable
b A bank dataset uses Employment Status and Credit Score to decide loan approval:
.
Instance   1   2   3   4   5   6   7   8
Q   Employ Emplo Emplo Emplo Emplo Unempl Unempl Unempl Unempl
4   ment   yed   yed   yed   yed   oyed   oyed   oyed   oyed
C   Status
O-   Credit   High   High   Low   Low   High   High   Low   Low
5;
Score
S
Loan   Yes   Yes   No   No   Yes   No   No   No   [5]
O-
Approv
2;
ed
B
Using the above dataset:
L-
•   Split the dataset based on Employment Status and compute the Gini Index.
3
•   Split the dataset based on Credit Score and compute the Gini Index.
• Determine which feature provides a better split with justification.
Step 1: Gini Formula (1 Mark)
𝐺𝑖𝑛𝑖= 1 −∑𝑝𝑖 2
Step 2: Split on Employment Status (2 Marks)
Groups:
• Employed → (Yes,Yes,No,No) = (2,2)
𝐺𝑖𝑛𝑖𝐸𝑚𝑝= 1 −(0.52 + 0.52) = 0.5
• Unemployed → (Yes,No,No,No) = (1,3)
𝐺𝑖𝑛𝑖𝑈𝑛𝑒𝑚𝑝= 1 −(0.252 + 0.752) = 0.375
Weighted Gini:
4   4
𝐺𝑖𝑛𝑖𝐸𝑚𝑝𝑙𝑜𝑦𝑚𝑒𝑛𝑡= (0.5) + (0.375) = 0.25 + 0.1875 = 0.4375
8   8
Step 3: Split on Credit Score (2 Marks)
********** 7 **********
--- page 8 ---
Groups:
• High → (Yes,Yes,Yes,No) = (3,1)
𝐺𝑖𝑛𝑖𝐻𝑖𝑔ℎ= 1 −(0.752 + 0.252) = 0.375
• Low → (No,No,No,No) = (0,4)
𝐺𝑖𝑛𝑖𝐿𝑜𝑤= 1 −(02 + 12) = 0
Weighted Gini:
4   4
𝐺𝑖𝑛𝑖𝐶𝑟𝑒𝑑𝑖𝑡= (0.375) + (0) = 0.1875
8   8
Step 4: Final Decision
• Gini (Employment) = 0.4375
• Gini (Credit Score) = 0.1875
Better Split: Credit Score
• Lower Gini Index → higher purity
• One node is completely pure (all “No”)
c   (i) A dataset is used to classify instances into two classes: Class 1 (1) and Class 0 (0) based
. on Feature 1 (x₁), feature 2 (x₂), feature 3 (x₃). A new data point is X=(3,2,4). Compute
Q   Euclidean distance from X to all points and identify the 3 nearest neighbors. Predict the
4   class of X.
C
O-   Point   x₁   x₂   x₃   Class
4;   A   1   2   3   0
S   B   2   3   4   0
[10]
O-   C   3   3   5   1
2;   D   6   5   4   1
E   7   6   5   1
B
L-   (ii) Given: x=(1,3,2), y=0, w=(0.4,−0.1,0.2), b=−0.2. Compute z=w⋅x+b. Compute
3   predicted probability using logistic regression and cross-entropy loss.
Point   x₁   x₂   x₃   Class   Distance
A   1   2   3   0   2.24
B   2   3   4   0   1.41
C   3   3   5   1   1.41
D   6   5   4   1   4.24
E   7   6   5   1   5.74
Class is 0 (1 mark)
Calculate Euclidean distance (4 marks)
Calculation of z (2 mark)
Calculation of probability (1 marks)
********** 8 **********
--- page 9 ---
Loss (2 marks)
Q   a
5
C
O-
Apply K-Means clustering (K = 2) on the following 1D dataset:
4;
Data points:2, 4, 10, 12, 3, 20, 30, 11, 25
S
Initial centroids:C1 = 2, C2 = 20   [10]
O-
Use Euclidean distance and perform 2 iterations.
2;
B
L-
3
Step 1: Assign points to nearest centroid (2 marks)
Point   Distance to   Distance to   Cluster
C1=2   C2=20
2   0   18   C1
4   2   16   C1
10   8   10   C1
12   10   8   C2
3   1   17   C1
20   18   0   C2
30   28   10   C2
11   9   9   C1 (tie → choose C1)
25   23   5   C2
Step 2: Form clusters (2 marks)
• Cluster C1 → {2, 4, 10, 3, 11}
• Cluster C2 → {12, 20, 30, 25}
Step 3: Compute new centroids (2 marks)
C1=2+4+10+3+11 / 5=30/5=6
C2=12+20+30+25/4=87/4=21.75
Step 4: Reassign points (Iteration 2) (2 marks)
Point   Dist to   Dist to   Cluster
C1=6   C2=21.75
2   4   19.75   C1
4   2   17.75   C1
10   4   11.75   C1
12   6   9.75   C1
********** 9 **********
--- page 10 ---
3   3   18.75   C1
20   14   1.75   C2
30   24   8.25   C2
11   5   10.75   C1
25   19   3.25   C2
Step 5: Final clusters
• C1 → {2, 4, 10, 12, 3, 11}
• C2 → {20, 30, 25}
Step 6: Final centroids
C1=2+4+10+12+3+11/6=7
C2 =20+30+25/3=25
Final Answer (2 marks)
•   Cluster 1 → {2, 4, 10, 12, 3, 11}, Centroid = 7
•   Cluster 2 → {20, 30, 25}, Centroid = 25
Q   b Following table shows the experience in years (X) and monthly salary (Y) of employees.
5   X   1   2   3   4   5   6
C   Y   30   35   50   55   65   80
O-   (i) Compute the regression equation of Y on X using the least squares method.
3;   (ii) Estimate the salary of an employee with 3.5 years of experience. Calculate the
S   residual for the employee with 4 years of experience   [10]
O-
2;
B
L-
3
Table calculation – 2 marks
Calculation of coefficients – 3 marks
Equation of line – 1 marks
Prediction – 2 marks
Residual – 2 marks
********** 10 **********
--- page 11 ---
Q   a When predicting student performance, selecting an attribute that maximizes information
6   gain is crucial.
[10]
C   • Briefly explain how entropy is used to measure uncertainty in classification.
O-
********** 11 **********
--- page 12 ---
5;   • Using the dataset below, determine which feature should be selected as the root
S   node.
O-   Study   High   High   High   High   Low   Low   Low   Low
2;   Hours
Attendance Good Good   Poor   Poor   Good   Good   Poor   Poor
B
L-   Result   Pass   Pass   Fail   Fail   Pass   Fail   Fail   Fail
3
1. Entropy Concept (3 Marks)
• Entropy (H) measures the uncertainty/impurity in a dataset.
• Formula:
𝐻= −𝑝1log⁡2 𝑝1 −𝑝2log⁡2 𝑝2
• 𝐻= 0→ pure (all same class)
• Higher 𝐻→ more mixed classes
Used to evaluate how good a split is.
2. Entropy of Dataset (2 Marks)
Class distribution: Pass = 3, Fail = 5 (Total = 8)
𝑝𝑃𝑎𝑠𝑠= 3/8 = 0.375,𝑝𝐹𝑎𝑖𝑙= 5/8 = 0.625
𝐸𝑛𝑡𝑟𝑜𝑝𝑦≈−(0.375log⁡2 0.375 + 0.625log⁡2 0.625) ≈0.954
3. Information Gain Calculation (4 Marks)
Split on Study Hours
High → (Pass,Pass,Fail,Fail) = (2,2)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐻𝑖𝑔ℎ= 1
Low → (Pass,Fail,Fail,Fail) = (1,3)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐿𝑜𝑤= 0.811
Weighted Entropy
4   4
= (1) + (0.811) = 0.5 + 0.405 = 0.905
8   8
Information Gain
𝐼𝐺𝑆𝑡𝑢𝑑𝑦= 0.954 −0.905 = 0.049
Split on Attendance
Good → (Pass,Pass,Pass,Fail) = (3,1)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐺𝑜𝑜𝑑= 0.811
Poor → (Fail,Fail,Fail,Fail) = (0,4)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝑃𝑜𝑜𝑟= 0
Weighted Entropy
4   4
= (0.811) + (0) = 0.405
8   8
Information Gain
𝐼𝐺𝐴𝑡𝑡𝑒𝑛𝑑𝑎𝑛𝑐𝑒= 0.954 −0.405 = 0.549
4. Final Decision (1 Mark)
• IG (Study Hours) = 0.049
• IG (Attendance) = 0.549
Best Attribute: Attendance
Justification:
• Higher information gain
• Produces a pure node (Poor → all Fail)
•   Better class separation
b Given the following 2D dataset:
Q
Points: A(1,1), B(1.2,1.1), C(0.8,1.2), D(8,8), E(8.2,8.1), F(25,25)   [10]
6
Apply DBSCAN with Eps = 0.5, MinPts = 3. Use Euclidean distance.
********** 12 **********
--- page 13 ---
C
O-
4;
S
O-
1;
B
L-
3
Step 1: Find ε-neighborhood (Eps = 0.5) (4 marks)
We compute distances (only nearby points matter):
Distance(A,B) ≈ √[(1.2−1)² + (1.1−1)²] ≈ 0.22
Distance(A,C) ≈ √[(0.8−1)² + (1.2−1)²] ≈ 0.28
Both < 0.5
So:
A → neighbors: {A, B, C} → count = 3
For B: neighbors = {A, B, C} → count = 3
For C: neighbors = {A, B, C} → count = 3
Distance(D,E) ≈ 0.22 → neighbors = {D, E} → count = 2
F is far from all → neighbors = {F} → count = 1
Step 2: Identify core, border, noise (4 marks)
Core points (≥ MinPts = 3)
→ A, B, C
Border points (<3 but near core)
→ None
Noise points
→ D, E, F
Step 3: Form clusters
Cluster 1 → {A, B, C}
Noise → {D, E, F}
Final Answer: (2 marks)
Cluster formed: {A, B, C}
Noise points: D, E, F
Q   a
7
C
O-
1;
S   Why is machine learning preferred over traditional programming for complex real-world
[5]
O-   problems? Explain with examples.
1;
B
L-
2
Why Traditional Programming Fails for Complex Problems (2 marks)
Real-world problems are too complex and variable.
Rules are hard to define explicitly.
Systems don’t adapt unless reprogrammed.
Why Machine Learning Works Better (2 marks)
********** 13 **********
--- page 14 ---
Machine learning can learn, adapt, and scale, making it suitable for complex, real-world
problems where fixed rules are not enough.
Example (1 mark)
Q   b A classifier fails to correctly predict certain training samples. Explain how AdaBoost
7   modifies the learning process to improve performance on such samples.
C
O-
5;
S
[5]
O-
1;
B
L-
3
Concept of AdaBoost (1 Mark)
• AdaBoost is a boosting ensemble method that builds a strong classifier by
combining multiple weak learners (e.g., decision stumps).
Modification of Learning Process (4 Marks)
1. Initialize Weights
•   All training samples are assigned equal weights initially.
2. Identify Errors
•   After training a weak learner, misclassified samples are identified.
3. Update Weights
•   Misclassified samples → weights increased
•   Correctly classified samples → weights decreased
This forces the next model to focus more on difficult samples.
4. Sequential Learning
• Each new learner is trained on the updated weighted dataset.
• Hard samples receive more importance over iterations.
5. Weighted Combination
• Each learner is assigned a weight based on accuracy.
•   Final prediction is a weighted vote of all learners.
Q   c
7
C
O-
4;
Apply Agglomerative Clustering (Complete Linkage) on the dataset: Points (2D): A(1,1),
S
B(2,2), C(5,5), D(6,6). Use Euclidean distance and perform clustering until 1 cluster [10]
O-
remains
1;
B
L-
3
********** 14 **********
--- page 15 ---
Step 1: Compute distance matrix (3 marks)
A   B   C   D
A 0   √2≈1.41   √32≈5.66   √50≈7.07
B   1.41   0   √18≈4.24   √32≈5.66
C   5.66   4.24   0   √2≈1.41
D   7.07   5.66   1.41   0
Step 2: Find closest pair (1 mark)
Minimum distance = 1.41 → (A,B)
Merge → C1 = {A,B}
Step 3: Update distances (Complete linkage = maximum distance) (2 marks)
d(C1,C) = max(5.66, 4.24) = 5.66
d(C1,D) = max(7.07, 5.66) = 7.07
Step 4: Next closest pair (2 marks)
Minimum distance = 1.41 → (C,D)
Merge → C2 = {C,D}
Step 5: Final merge (2 marks)
Distance between clusters:
d(C1,C2) = max(5.66, 7.07, 4.24, 5.66) = 7.07
Merge → Final cluster = {A,B,C,D}
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper e5fa5630186e

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIML_7053/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/MBA
Tech (AI)
Year: II/Sem 4 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 30 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q
1   Answer briefly:   [20]
C   a
O-
1;
S
Analyze a traffic management system that needs to forecast congestion and group similar
O-
traffic behaviors. Identify suitable ML tasks, describe data collection methods, and explain [5]
1;
how these tasks can complement each other.
B
L-
2
Suitable Machine Learning Tasks (4 marks)
Traffic congestion prediction - Supervised learning -Regression (predict traffic speed,
travel time) and Classification (e.g., low / medium / high congestion)
Traffic pattern grouping - Unsupervised learning- Clustering (group similar traffic
behaviors across time/locations)
Clustering finds patterns, prediction uses those patterns to forecast the future.
Data Sources (1 marks) - Sensors & IoT devices, mobile or GPS, Historical traffic records
etc.
C   b
O-
2;
A dataset contains features such as “City,” “Satisfaction Level (Low, Medium, High),” and
S
“Temperature.” Explain how each feature should be treated based on whether it is nominal, [5]
O-
ordinal, or interval data, and justify your preprocessing choices.
1;
B
********** 1 **********
--- page 2 ---
L-
2
Type (1 mark)
Preprocessing (2 marks)
Justification (2 marks)
Feature   Type   Preprocessing   Why It Matters
City   Nominal   One-hot   Avoids false order
encoding
Satisfaction Level   Ordinal   Ordinal encoding   Preserves ranking
Temperature   Interval   Scaling   Ensures numerical stability
C   c
O-
3;
S   You are given a small dataset with class imbalance (e.g., 90% negative, 10% positive).
O-   Which validation technique would you choose among holdout, k-fold, LOOCV, and
[5]
2;   stratified cross-validation? Justify your choice and explain how it improves model
evaluation.
B
L-
3
stratified cross-validation (1 mark)
Justification (3 marks)
1. Holdout Method - random split may produce uneven class distribution
2. Standard k-Fold Cross-Validation - data is split into k folds randomly. Some folds may
have very few minority class samples
3. Leave-One-Out Cross-Validation (LOOCV)- each test set has only one sample. With
imbalance, most test cases will be negative
4. Stratified cross-validation - each fold preserves the original class distribution i.e., ~90%
negative and ~10% positive in every fold.
How it improves model evaluation (1 mark)
1. Balanced Representation
2. Reliable Performance Metrics
3. Reduced Variance- results across folds are more stable, avoids random fluctuations due
to class imbalance
4. Better Generalization Estimate- mimics real-world distribution in every split.
C   d
O-   A classifier outputs probabilities for 10 samples:
4;   Sample   1   2   3   4   5   6   7   8   9   10
S
O-   Probability 0.9   0.8   0.7   0.6   0.55   0.45   0.4   0.3   0.3   0.1
[5]
2;   Actual   1   1   0   1   0   1   0   0   1   0
class
B   (i) Construct confusion matrices at thresholds 0.5 and 0.7
L-   (ii) Compute TPR and FPR for both thresholds
3
Predictions (1 marks)
Sample   1   2   3   4   5   6   7   8   9   10
Probability 0.9   0.8   0.7   0.6   0.55   0.45   0.4   0.3   0.3   0.1
Actual   1   1   0   1   0   1   0   0   1   0
class
T>=0.5   1   1   1   1   1   0   0   0   0   0
********** 2 **********
--- page 3 ---
T>=0.7   1   1   1   0   0   0   0   0   0   0
Confusion matrix (2 marks)   +   -
+   -   +   2   3
+   3   2   -   1   4
-   2   3
TPR & FPR (2 marks)
FPR= FP / (FP + TN)
TPR= TP / (TP + FN)
Q   a
2
C
O-
2;
(i) What is feature binarization? and why is it used in machine learning?
S
(ii) what is the importance of data visualization. Briefly explain Name and briefly explain   [5]
O-
histogram, scatter plot, box plot with example.
1;
B
L-
2
Feature binarization (1 mark)
It is a preprocessing technique where numerical or continuous data is converted into binary
values (0 or 1) using a threshold.
Value > threshold → 1
Value ≤ threshold → 0
Why it is used (1 mark)
• Simplifies data → Converts complex values into simple binary form
• Improves model efficiency → Faster computation and less memory
• Works well with some algorithms → e.g., Naive Bayes
• Reduces noise → Minor variations are ignored
• Helps decision-making → Clear yes/no classification
Data visualization (1 mark)
It is the graphical representation of data using charts, graphs, or plots to make information
easy to understand.
• Helps in understanding patterns and trends
• Makes complex data easy to interpret
• Aids in decision-making
• Helps detect outliers and anomalies
• Improves communication of insights
Three plots (2 marks)
Q   b A dataset contains two classes with the following distribution: 9 instances of Class A and
2   7 instances of Class B. Calculate the entropy of the dataset and interpret the level of
C   impurity.
O-
5;
[5]
S
O-
2;
B
********** 3 **********
--- page 4 ---
L-
3
Step 1: Entropy Formula (1 Mark)
𝐻= −𝑝1log⁡2 𝑝1 −𝑝2log⁡2 𝑝2
Step 2: Calculate Probabilities (1 Mark)
Total instances = 16
𝑝𝐴= 9/16 = 0.5625,𝑝𝐵= 7/16 = 0.4375
Step 3: Entropy Calculation (2 Marks)
𝐻= −(0.5625log⁡2 0.5625 + 0.4375log⁡2 0.4375)
≈−(0.5625 × −0.83 + 0.4375 × −1.19)
≈0.467 + 0.521 = 0.988
Step 4: Interpretation (1 Mark)
• Entropy ≈ 0.99 (close to 1)
•   Indicates high impurity
Classes are almost evenly mixed
c A dataset contains information about a customer buys a product (Buy = Yes / No) based
Q   on age, income and he is student or not. Using Naive Bayes, classify the following instance:
2   X= (Young, Medium, Yes)
C   No.   Age   Income   Student   Buy
O-   1   Young   High   No   No
4;   2   Young   High   No   No
S   3   Middle   High   No   Yes   [10]
O-   4   Old   Medium   No   Yes
2;   5   Old   Low   Yes   Yes
6   Old   Low   Yes   No
B   7   Middle   Low   Yes   Yes
L-   8   Young   Medium   No   No
3   9   Young   Low   Yes   Yes
10   Old   Medium   Yes   Yes
Priori probabilities (1 marks)
Likelihood probabilities (4 marks)
Posterior probability (4 marks)
********** 4 **********
--- page 5 ---
Class is yes (1 mark)
Q   a
3
C   Using the given dataset, apply gradient descent to a simple linear regression model and carry out
O-   two iterations. Assume initial parameter values as zero and use a learning rate of α = 0.01.
3;
S   Study Hours   1 2   3   4   5   [10]
O-   Exam Scores   5 9 13 17 15
2;
B
L-
3
Iteration – 1 (5 marks)
alpha=   0.01
h(x) =   0 +   0 X
x   y   h(x) = h(x) -y (h(x) -y)^2 (h(x) -y )*x
1   5   0   -5   25   -5
2   9   0   -9   81   -18
3   13   0   -13   169   -39
4   17   0   -17   289   -68
5   15   0   -15   225   -75
-59   789   -205
m=   5
Cost J   78.9
theta 0   0.118
theta 1   0.41
Iteration – 2 (5 marks)
********** 5 **********
--- page 6 ---
alpha=   0.01
h(x) =   0.118 +   0.41 X
x   x   y   h(x) =   h(x) -y (h(x) -y)^2 (h(x) -y )*x
1   5   0.528   -4.472 19.99878   -4.472
2   9   0.938   -8.062 64.99584   -16.124
3   13   1.348   -11.652 135.7691   -34.956
4   17   1.758   -15.242 232.3186   -60.968
5   15   2.168   -12.832 164.6602   -64.16
-52.26 617.7425   -180.68
m=   5
Cost J   61.77425
theta 0   0.22252
theta 1   0.77136
b Consider the following dataset with two class (+1) and (-1).
Point   (x₁, x₂)   Class
Q
A   (1,3)   +1
3
B   (2,4)   +1
C
C   (5,2)   −1
O-
D   (6,3)   −1
4;
S   [10]
Two candidate hyperplanes are given:
O-
H1: −3x1 + 2x2 + 2.5 = 0
2;
H2: 2x1 + x2 −10 = 0
B
For   each   hyperplane,   compute   the   decision   function:   f(x) = w ⋅x + b
L-
for all data points and determine their predicted class labels. For each hyperplane, compute
3
the margin. Among the given hyperplanes, determine the optimal SVM hyperplane. Justify
your choice based on both classification correctness and margin.
W and b values (1 mark)
For H1 (3 marks)
Point   Calculation   f(x)   Predicted   Actual
A(1,3)   -3 + 6 + 2.5   5.5   +1   +1
B(2,4)   -6 + 8 + 2.5   4.5   +1   +1
C(5,2)   -15 + 4 + 2.5 -8.5   −1   −1
D(6,3)   -18 + 6 + 2.5 -9.5   −1   −1
All points correctly classified
Margin=2/sqrt(13)
For H2 (3 marks)
Point   Calculation   f(x)   Predicted   Actual
A(1,3)   2 + 3 - 10   -5   −1   +1
B(2,4)   4 + 4 - 10   -2   −1   +1
C(5,2)   10 + 2 - 10   2   +1   −1
D(6,3)   12 + 3 - 10   5   +1   −1
All points are misclassified
Margin=2/sqrt(5)
Optimal hyperplane is H1(3 marks)
A hyperplane with larger margin is useless if it misclassifies data.
Validity > Margin in SVM selection.
********** 6 **********
--- page 7 ---
Q   a
4
C
O-
2;   Explain how transforming input features can simplify a learning problem. Support your
S   answer with the given data: (1,10,100,1000) by applying log transformation.
[5]
O-
1;
B
L-
2
Explanation (2 marks)
Transforming input features simplifies a learning problem by reshaping the data into a form
where patterns become easier for a model to capture. Instead of forcing a model to learn
complex relationships, we modify the input, so the relationship appears simpler.
Example (3 marks)
Raw → highly skewed
After log transform → (0,1,2,3)
Relationship becomes linear and stable
b A bank dataset uses Employment Status and Credit Score to decide loan approval:
.
Instance   1   2   3   4   5   6   7   8
Q   Employ Emplo Emplo Emplo Emplo Unempl Unempl Unempl Unempl
4   ment   yed   yed   yed   yed   oyed   oyed   oyed   oyed
C   Status
O-   Credit   High   High   Low   Low   High   High   Low   Low
5;
Score
S
Loan   Yes   Yes   No   No   Yes   No   No   No   [5]
O-
Approv
2;
ed
B
Using the above dataset:
L-
•   Split the dataset based on Employment Status and compute the Gini Index.
3
•   Split the dataset based on Credit Score and compute the Gini Index.
• Determine which feature provides a better split with justification.
Step 1: Gini Formula (1 Mark)
𝐺𝑖𝑛𝑖= 1 −∑𝑝𝑖 2
Step 2: Split on Employment Status (2 Marks)
Groups:
• Employed → (Yes,Yes,No,No) = (2,2)
𝐺𝑖𝑛𝑖𝐸𝑚𝑝= 1 −(0.52 + 0.52) = 0.5
• Unemployed → (Yes,No,No,No) = (1,3)
𝐺𝑖𝑛𝑖𝑈𝑛𝑒𝑚𝑝= 1 −(0.252 + 0.752) = 0.375
Weighted Gini:
4   4
𝐺𝑖𝑛𝑖𝐸𝑚𝑝𝑙𝑜𝑦𝑚𝑒𝑛𝑡= (0.5) + (0.375) = 0.25 + 0.1875 = 0.4375
8   8
Step 3: Split on Credit Score (2 Marks)
********** 7 **********
--- page 8 ---
Groups:
• High → (Yes,Yes,Yes,No) = (3,1)
𝐺𝑖𝑛𝑖𝐻𝑖𝑔ℎ= 1 −(0.752 + 0.252) = 0.375
• Low → (No,No,No,No) = (0,4)
𝐺𝑖𝑛𝑖𝐿𝑜𝑤= 1 −(02 + 12) = 0
Weighted Gini:
4   4
𝐺𝑖𝑛𝑖𝐶𝑟𝑒𝑑𝑖𝑡= (0.375) + (0) = 0.1875
8   8
Step 4: Final Decision
• Gini (Employment) = 0.4375
• Gini (Credit Score) = 0.1875
Better Split: Credit Score
• Lower Gini Index → higher purity
• One node is completely pure (all “No”)
c   (i) A dataset is used to classify instances into two classes: Class 1 (1) and Class 0 (0) based
. on Feature 1 (x₁), feature 2 (x₂), feature 3 (x₃). A new data point is X=(3,2,4). Compute
Q   Euclidean distance from X to all points and identify the 3 nearest neighbors. Predict the
4   class of X.
C
O-   Point   x₁   x₂   x₃   Class
4;   A   1   2   3   0
S   B   2   3   4   0
[10]
O-   C   3   3   5   1
2;   D   6   5   4   1
E   7   6   5   1
B
L-   (ii) Given: x=(1,3,2), y=0, w=(0.4,−0.1,0.2), b=−0.2. Compute z=w⋅x+b. Compute
3   predicted probability using logistic regression and cross-entropy loss.
Point   x₁   x₂   x₃   Class   Distance
A   1   2   3   0   2.24
B   2   3   4   0   1.41
C   3   3   5   1   1.41
D   6   5   4   1   4.24
E   7   6   5   1   5.74
Class is 0 (1 mark)
Calculate Euclidean distance (4 marks)
Calculation of z (2 mark)
Calculation of probability (1 marks)
********** 8 **********
--- page 9 ---
Loss (2 marks)
Q   a
5
C
O-
Apply K-Means clustering (K = 2) on the following 1D dataset:
4;
Data points:2, 4, 10, 12, 3, 20, 30, 11, 25
S
Initial centroids:C1 = 2, C2 = 20   [10]
O-
Use Euclidean distance and perform 2 iterations.
2;
B
L-
3
Step 1: Assign points to nearest centroid (2 marks)
Point   Distance to   Distance to   Cluster
C1=2   C2=20
2   0   18   C1
4   2   16   C1
10   8   10   C1
12   10   8   C2
3   1   17   C1
20   18   0   C2
30   28   10   C2
11   9   9   C1 (tie → choose C1)
25   23   5   C2
Step 2: Form clusters (2 marks)
• Cluster C1 → {2, 4, 10, 3, 11}
• Cluster C2 → {12, 20, 30, 25}
Step 3: Compute new centroids (2 marks)
C1=2+4+10+3+11 / 5=30/5=6
C2=12+20+30+25/4=87/4=21.75
Step 4: Reassign points (Iteration 2) (2 marks)
Point   Dist to   Dist to   Cluster
C1=6   C2=21.75
2   4   19.75   C1
4   2   17.75   C1
10   4   11.75   C1
12   6   9.75   C1
********** 9 **********
--- page 10 ---
3   3   18.75   C1
20   14   1.75   C2
30   24   8.25   C2
11   5   10.75   C1
25   19   3.25   C2
Step 5: Final clusters
• C1 → {2, 4, 10, 12, 3, 11}
• C2 → {20, 30, 25}
Step 6: Final centroids
C1=2+4+10+12+3+11/6=7
C2 =20+30+25/3=25
Final Answer (2 marks)
•   Cluster 1 → {2, 4, 10, 12, 3, 11}, Centroid = 7
•   Cluster 2 → {20, 30, 25}, Centroid = 25
Q   b Following table shows the experience in years (X) and monthly salary (Y) of employees.
5   X   1   2   3   4   5   6
C   Y   30   35   50   55   65   80
O-   (i) Compute the regression equation of Y on X using the least squares method.
3;   (ii) Estimate the salary of an employee with 3.5 years of experience. Calculate the
S   residual for the employee with 4 years of experience   [10]
O-
2;
B
L-
3
Table calculation – 2 marks
Calculation of coefficients – 3 marks
Equation of line – 1 marks
Prediction – 2 marks
Residual – 2 marks
********** 10 **********
--- page 11 ---
Q   a When predicting student performance, selecting an attribute that maximizes information
6   gain is crucial.
[10]
C   • Briefly explain how entropy is used to measure uncertainty in classification.
O-
********** 11 **********
--- page 12 ---
5;   • Using the dataset below, determine which feature should be selected as the root
S   node.
O-   Study   High   High   High   High   Low   Low   Low   Low
2;   Hours
Attendance Good Good   Poor   Poor   Good   Good   Poor   Poor
B
L-   Result   Pass   Pass   Fail   Fail   Pass   Fail   Fail   Fail
3
1. Entropy Concept (3 Marks)
• Entropy (H) measures the uncertainty/impurity in a dataset.
• Formula:
𝐻= −𝑝1log⁡2 𝑝1 −𝑝2log⁡2 𝑝2
• 𝐻= 0→ pure (all same class)
• Higher 𝐻→ more mixed classes
Used to evaluate how good a split is.
2. Entropy of Dataset (2 Marks)
Class distribution: Pass = 3, Fail = 5 (Total = 8)
𝑝𝑃𝑎𝑠𝑠= 3/8 = 0.375,𝑝𝐹𝑎𝑖𝑙= 5/8 = 0.625
𝐸𝑛𝑡𝑟𝑜𝑝𝑦≈−(0.375log⁡2 0.375 + 0.625log⁡2 0.625) ≈0.954
3. Information Gain Calculation (4 Marks)
Split on Study Hours
High → (Pass,Pass,Fail,Fail) = (2,2)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐻𝑖𝑔ℎ= 1
Low → (Pass,Fail,Fail,Fail) = (1,3)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐿𝑜𝑤= 0.811
Weighted Entropy
4   4
= (1) + (0.811) = 0.5 + 0.405 = 0.905
8   8
Information Gain
𝐼𝐺𝑆𝑡𝑢𝑑𝑦= 0.954 −0.905 = 0.049
Split on Attendance
Good → (Pass,Pass,Pass,Fail) = (3,1)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐺𝑜𝑜𝑑= 0.811
Poor → (Fail,Fail,Fail,Fail) = (0,4)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝑃𝑜𝑜𝑟= 0
Weighted Entropy
4   4
= (0.811) + (0) = 0.405
8   8
Information Gain
𝐼𝐺𝐴𝑡𝑡𝑒𝑛𝑑𝑎𝑛𝑐𝑒= 0.954 −0.405 = 0.549
4. Final Decision (1 Mark)
• IG (Study Hours) = 0.049
• IG (Attendance) = 0.549
Best Attribute: Attendance
Justification:
• Higher information gain
• Produces a pure node (Poor → all Fail)
•   Better class separation
b Given the following 2D dataset:
Q
Points: A(1,1), B(1.2,1.1), C(0.8,1.2), D(8,8), E(8.2,8.1), F(25,25)   [10]
6
Apply DBSCAN with Eps = 0.5, MinPts = 3. Use Euclidean distance.
********** 12 **********
--- page 13 ---
C
O-
4;
S
O-
1;
B
L-
3
Step 1: Find ε-neighborhood (Eps = 0.5) (4 marks)
We compute distances (only nearby points matter):
Distance(A,B) ≈ √[(1.2−1)² + (1.1−1)²] ≈ 0.22
Distance(A,C) ≈ √[(0.8−1)² + (1.2−1)²] ≈ 0.28
Both < 0.5
So:
A → neighbors: {A, B, C} → count = 3
For B: neighbors = {A, B, C} → count = 3
For C: neighbors = {A, B, C} → count = 3
Distance(D,E) ≈ 0.22 → neighbors = {D, E} → count = 2
F is far from all → neighbors = {F} → count = 1
Step 2: Identify core, border, noise (4 marks)
Core points (≥ MinPts = 3)
→ A, B, C
Border points (<3 but near core)
→ None
Noise points
→ D, E, F
Step 3: Form clusters
Cluster 1 → {A, B, C}
Noise → {D, E, F}
Final Answer: (2 marks)
Cluster formed: {A, B, C}
Noise points: D, E, F
Q   a
7
C
O-
1;
S   Why is machine learning preferred over traditional programming for complex real-world
[5]
O-   problems? Explain with examples.
1;
B
L-
2
Why Traditional Programming Fails for Complex Problems (2 marks)
Real-world problems are too complex and variable.
Rules are hard to define explicitly.
Systems don’t adapt unless reprogrammed.
Why Machine Learning Works Better (2 marks)
********** 13 **********
--- page 14 ---
Machine learning can learn, adapt, and scale, making it suitable for complex, real-world
problems where fixed rules are not enough.
Example (1 mark)
Q   b A classifier fails to correctly predict certain training samples. Explain how AdaBoost
7   modifies the learning process to improve performance on such samples.
C
O-
5;
S
[5]
O-
1;
B
L-
3
Concept of AdaBoost (1 Mark)
• AdaBoost is a boosting ensemble method that builds a strong classifier by
combining multiple weak learners (e.g., decision stumps).
Modification of Learning Process (4 Marks)
1. Initialize Weights
•   All training samples are assigned equal weights initially.
2. Identify Errors
•   After training a weak learner, misclassified samples are identified.
3. Update Weights
•   Misclassified samples → weights increased
•   Correctly classified samples → weights decreased
This forces the next model to focus more on difficult samples.
4. Sequential Learning
• Each new learner is trained on the updated weighted dataset.
• Hard samples receive more importance over iterations.
5. Weighted Combination
• Each learner is assigned a weight based on accuracy.
•   Final prediction is a weighted vote of all learners.
Q   c
7
C
O-
4;
Apply Agglomerative Clustering (Complete Linkage) on the dataset: Points (2D): A(1,1),
S
B(2,2), C(5,5), D(6,6). Use Euclidean distance and perform clustering until 1 cluster [10]
O-
remains
1;
B
L-
3
********** 14 **********
--- page 15 ---
Step 1: Compute distance matrix (3 marks)
A   B   C   D
A 0   √2≈1.41   √32≈5.66   √50≈7.07
B   1.41   0   √18≈4.24   √32≈5.66
C   5.66   4.24   0   √2≈1.41
D   7.07   5.66   1.41   0
Step 2: Find closest pair (1 mark)
Minimum distance = 1.41 → (A,B)
Merge → C1 = {A,B}
Step 3: Update distances (Complete linkage = maximum distance) (2 marks)
d(C1,C) = max(5.66, 4.24) = 5.66
d(C1,D) = max(7.07, 5.66) = 7.07
Step 4: Next closest pair (2 marks)
Minimum distance = 1.41 → (C,D)
Merge → C2 = {C,D}
Step 5: Final merge (2 marks)
Distance between clusters:
d(C1,C2) = max(5.66, 7.07, 4.24, 5.66) = 7.07
Merge → Final cluster = {A,B,C,D}
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper ef539c10e09e

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AI_7012/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. TECH (CSE - DS)/MBA
Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 30 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q
1   Answer briefly:   [20]
C   a
O-
1;
S
Analyze a traffic management system that needs to forecast congestion and group similar
O-
traffic behaviors. Identify suitable ML tasks, describe data collection methods, and explain [5]
1;
how these tasks can complement each other.
B
L-
2
Suitable Machine Learning Tasks (4 marks)
Traffic congestion prediction - Supervised learning -Regression (predict traffic speed,
travel time) and Classification (e.g., low / medium / high congestion)
Traffic pattern grouping - Unsupervised learning- Clustering (group similar traffic
behaviors across time/locations)
Clustering finds patterns, prediction uses those patterns to forecast the future.
Data Sources (1 marks) - Sensors & IoT devices, mobile or GPS, Historical traffic records
etc.
C   b
O-
2;
A dataset contains features such as “City,” “Satisfaction Level (Low, Medium, High),” and
S
“Temperature.” Explain how each feature should be treated based on whether it is nominal, [5]
O-
ordinal, or interval data, and justify your preprocessing choices.
1;
B
********** 1 **********
--- page 2 ---
L-
2
Type (1 mark)
Preprocessing (2 marks)
Justification (2 marks)
Feature   Type   Preprocessing   Why It Matters
City   Nominal   One-hot   Avoids false order
encoding
Satisfaction Level   Ordinal   Ordinal encoding   Preserves ranking
Temperature   Interval   Scaling   Ensures numerical stability
C   c
O-
3;
S   You are given a small dataset with class imbalance (e.g., 90% negative, 10% positive).
O-   Which validation technique would you choose among holdout, k-fold, LOOCV, and
[5]
2;   stratified cross-validation? Justify your choice and explain how it improves model
evaluation.
B
L-
3
stratified cross-validation (1 mark)
Justification (3 marks)
1. Holdout Method - random split may produce uneven class distribution
2. Standard k-Fold Cross-Validation - data is split into k folds randomly. Some folds may
have very few minority class samples
3. Leave-One-Out Cross-Validation (LOOCV)- each test set has only one sample. With
imbalance, most test cases will be negative
4. Stratified cross-validation - each fold preserves the original class distribution i.e., ~90%
negative and ~10% positive in every fold.
How it improves model evaluation (1 mark)
1. Balanced Representation
2. Reliable Performance Metrics
3. Reduced Variance- results across folds are more stable, avoids random fluctuations due
to class imbalance
4. Better Generalization Estimate- mimics real-world distribution in every split.
C   d
O-   A classifier outputs probabilities for 10 samples:
4;   Sample   1   2   3   4   5   6   7   8   9   10
S
O-   Probability 0.9   0.8   0.7   0.6   0.55   0.45   0.4   0.3   0.3   0.1
[5]
2;   Actual   1   1   0   1   0   1   0   0   1   0
class
B   (i) Construct confusion matrices at thresholds 0.5 and 0.7
L-   (ii) Compute TPR and FPR for both thresholds
3
Predictions (1 marks)
Sample   1   2   3   4   5   6   7   8   9   10
Probability 0.9   0.8   0.7   0.6   0.55   0.45   0.4   0.3   0.3   0.1
Actual   1   1   0   1   0   1   0   0   1   0
class
T>=0.5   1   1   1   1   1   0   0   0   0   0
********** 2 **********
--- page 3 ---
T>=0.7   1   1   1   0   0   0   0   0   0   0
Confusion matrix (2 marks)   +   -
+   -   +   2   3
+   3   2   -   1   4
-   2   3
TPR & FPR (2 marks)
FPR= FP / (FP + TN)
TPR= TP / (TP + FN)
Q   a
2
C
O-
2;
(i) What is feature binarization? and why is it used in machine learning?
S
(ii) what is the importance of data visualization. Briefly explain Name and briefly explain   [5]
O-
histogram, scatter plot, box plot with example.
1;
B
L-
2
Feature binarization (1 mark)
It is a preprocessing technique where numerical or continuous data is converted into binary
values (0 or 1) using a threshold.
Value > threshold → 1
Value ≤ threshold → 0
Why it is used (1 mark)
• Simplifies data → Converts complex values into simple binary form
• Improves model efficiency → Faster computation and less memory
• Works well with some algorithms → e.g., Naive Bayes
• Reduces noise → Minor variations are ignored
• Helps decision-making → Clear yes/no classification
Data visualization (1 mark)
It is the graphical representation of data using charts, graphs, or plots to make information
easy to understand.
• Helps in understanding patterns and trends
• Makes complex data easy to interpret
• Aids in decision-making
• Helps detect outliers and anomalies
• Improves communication of insights
Three plots (2 marks)
Q   b A dataset contains two classes with the following distribution: 9 instances of Class A and
2   7 instances of Class B. Calculate the entropy of the dataset and interpret the level of
C   impurity.
O-
5;
[5]
S
O-
2;
B
********** 3 **********
--- page 4 ---
L-
3
Step 1: Entropy Formula (1 Mark)
𝐻= −𝑝1log⁡2 𝑝1 −𝑝2log⁡2 𝑝2
Step 2: Calculate Probabilities (1 Mark)
Total instances = 16
𝑝𝐴= 9/16 = 0.5625,𝑝𝐵= 7/16 = 0.4375
Step 3: Entropy Calculation (2 Marks)
𝐻= −(0.5625log⁡2 0.5625 + 0.4375log⁡2 0.4375)
≈−(0.5625 × −0.83 + 0.4375 × −1.19)
≈0.467 + 0.521 = 0.988
Step 4: Interpretation (1 Mark)
• Entropy ≈ 0.99 (close to 1)
•   Indicates high impurity
Classes are almost evenly mixed
c A dataset contains information about a customer buys a product (Buy = Yes / No) based
Q   on age, income and he is student or not. Using Naive Bayes, classify the following instance:
2   X= (Young, Medium, Yes)
C   No.   Age   Income   Student   Buy
O-   1   Young   High   No   No
4;   2   Young   High   No   No
S   3   Middle   High   No   Yes   [10]
O-   4   Old   Medium   No   Yes
2;   5   Old   Low   Yes   Yes
6   Old   Low   Yes   No
B   7   Middle   Low   Yes   Yes
L-   8   Young   Medium   No   No
3   9   Young   Low   Yes   Yes
10   Old   Medium   Yes   Yes
Priori probabilities (1 marks)
Likelihood probabilities (4 marks)
Posterior probability (4 marks)
********** 4 **********
--- page 5 ---
Class is yes (1 mark)
Q   a
3
C   Using the given dataset, apply gradient descent to a simple linear regression model and carry out
O-   two iterations. Assume initial parameter values as zero and use a learning rate of α = 0.01.
3;
S   Study Hours   1 2   3   4   5   [10]
O-   Exam Scores   5 9 13 17 15
2;
B
L-
3
Iteration – 1 (5 marks)
alpha=   0.01
h(x) =   0 +   0 X
x   y   h(x) = h(x) -y (h(x) -y)^2 (h(x) -y )*x
1   5   0   -5   25   -5
2   9   0   -9   81   -18
3   13   0   -13   169   -39
4   17   0   -17   289   -68
5   15   0   -15   225   -75
-59   789   -205
m=   5
Cost J   78.9
theta 0   0.118
theta 1   0.41
Iteration – 2 (5 marks)
********** 5 **********
--- page 6 ---
alpha=   0.01
h(x) =   0.118 +   0.41 X
x   x   y   h(x) =   h(x) -y (h(x) -y)^2 (h(x) -y )*x
1   5   0.528   -4.472 19.99878   -4.472
2   9   0.938   -8.062 64.99584   -16.124
3   13   1.348   -11.652 135.7691   -34.956
4   17   1.758   -15.242 232.3186   -60.968
5   15   2.168   -12.832 164.6602   -64.16
-52.26 617.7425   -180.68
m=   5
Cost J   61.77425
theta 0   0.22252
theta 1   0.77136
b Consider the following dataset with two class (+1) and (-1).
Point   (x₁, x₂)   Class
Q
A   (1,3)   +1
3
B   (2,4)   +1
C
C   (5,2)   −1
O-
D   (6,3)   −1
4;
S   [10]
Two candidate hyperplanes are given:
O-
H1: −3x1 + 2x2 + 2.5 = 0
2;
H2: 2x1 + x2 −10 = 0
B
For   each   hyperplane,   compute   the   decision   function:   f(x) = w ⋅x + b
L-
for all data points and determine their predicted class labels. For each hyperplane, compute
3
the margin. Among the given hyperplanes, determine the optimal SVM hyperplane. Justify
your choice based on both classification correctness and margin.
W and b values (1 mark)
For H1 (3 marks)
Point   Calculation   f(x)   Predicted   Actual
A(1,3)   -3 + 6 + 2.5   5.5   +1   +1
B(2,4)   -6 + 8 + 2.5   4.5   +1   +1
C(5,2)   -15 + 4 + 2.5 -8.5   −1   −1
D(6,3)   -18 + 6 + 2.5 -9.5   −1   −1
All points correctly classified
Margin=2/sqrt(13)
For H2 (3 marks)
Point   Calculation   f(x)   Predicted   Actual
A(1,3)   2 + 3 - 10   -5   −1   +1
B(2,4)   4 + 4 - 10   -2   −1   +1
C(5,2)   10 + 2 - 10   2   +1   −1
D(6,3)   12 + 3 - 10   5   +1   −1
All points are misclassified
Margin=2/sqrt(5)
Optimal hyperplane is H1(3 marks)
A hyperplane with larger margin is useless if it misclassifies data.
Validity > Margin in SVM selection.
********** 6 **********
--- page 7 ---
Q   a
4
C
O-
2;   Explain how transforming input features can simplify a learning problem. Support your
S   answer with the given data: (1,10,100,1000) by applying log transformation.
[5]
O-
1;
B
L-
2
Explanation (2 marks)
Transforming input features simplifies a learning problem by reshaping the data into a form
where patterns become easier for a model to capture. Instead of forcing a model to learn
complex relationships, we modify the input, so the relationship appears simpler.
Example (3 marks)
Raw → highly skewed
After log transform → (0,1,2,3)
Relationship becomes linear and stable
b A bank dataset uses Employment Status and Credit Score to decide loan approval:
.
Instance   1   2   3   4   5   6   7   8
Q   Employ Emplo Emplo Emplo Emplo Unempl Unempl Unempl Unempl
4   ment   yed   yed   yed   yed   oyed   oyed   oyed   oyed
C   Status
O-   Credit   High   High   Low   Low   High   High   Low   Low
5;
Score
S
Loan   Yes   Yes   No   No   Yes   No   No   No   [5]
O-
Approv
2;
ed
B
Using the above dataset:
L-
•   Split the dataset based on Employment Status and compute the Gini Index.
3
•   Split the dataset based on Credit Score and compute the Gini Index.
• Determine which feature provides a better split with justification.
Step 1: Gini Formula (1 Mark)
𝐺𝑖𝑛𝑖= 1 −∑𝑝𝑖 2
Step 2: Split on Employment Status (2 Marks)
Groups:
• Employed → (Yes,Yes,No,No) = (2,2)
𝐺𝑖𝑛𝑖𝐸𝑚𝑝= 1 −(0.52 + 0.52) = 0.5
• Unemployed → (Yes,No,No,No) = (1,3)
𝐺𝑖𝑛𝑖𝑈𝑛𝑒𝑚𝑝= 1 −(0.252 + 0.752) = 0.375
Weighted Gini:
4   4
𝐺𝑖𝑛𝑖𝐸𝑚𝑝𝑙𝑜𝑦𝑚𝑒𝑛𝑡= (0.5) + (0.375) = 0.25 + 0.1875 = 0.4375
8   8
Step 3: Split on Credit Score (2 Marks)
********** 7 **********
--- page 8 ---
Groups:
• High → (Yes,Yes,Yes,No) = (3,1)
𝐺𝑖𝑛𝑖𝐻𝑖𝑔ℎ= 1 −(0.752 + 0.252) = 0.375
• Low → (No,No,No,No) = (0,4)
𝐺𝑖𝑛𝑖𝐿𝑜𝑤= 1 −(02 + 12) = 0
Weighted Gini:
4   4
𝐺𝑖𝑛𝑖𝐶𝑟𝑒𝑑𝑖𝑡= (0.375) + (0) = 0.1875
8   8
Step 4: Final Decision
• Gini (Employment) = 0.4375
• Gini (Credit Score) = 0.1875
Better Split: Credit Score
• Lower Gini Index → higher purity
• One node is completely pure (all “No”)
c   (i) A dataset is used to classify instances into two classes: Class 1 (1) and Class 0 (0) based
. on Feature 1 (x₁), feature 2 (x₂), feature 3 (x₃). A new data point is X=(3,2,4). Compute
Q   Euclidean distance from X to all points and identify the 3 nearest neighbors. Predict the
4   class of X.
C
O-   Point   x₁   x₂   x₃   Class
4;   A   1   2   3   0
S   B   2   3   4   0
[10]
O-   C   3   3   5   1
2;   D   6   5   4   1
E   7   6   5   1
B
L-   (ii) Given: x=(1,3,2), y=0, w=(0.4,−0.1,0.2), b=−0.2. Compute z=w⋅x+b. Compute
3   predicted probability using logistic regression and cross-entropy loss.
Point   x₁   x₂   x₃   Class   Distance
A   1   2   3   0   2.24
B   2   3   4   0   1.41
C   3   3   5   1   1.41
D   6   5   4   1   4.24
E   7   6   5   1   5.74
Class is 0 (1 mark)
Calculate Euclidean distance (4 marks)
Calculation of z (2 mark)
Calculation of probability (1 marks)
********** 8 **********
--- page 9 ---
Loss (2 marks)
Q   a
5
C
O-
Apply K-Means clustering (K = 2) on the following 1D dataset:
4;
Data points:2, 4, 10, 12, 3, 20, 30, 11, 25
S
Initial centroids:C1 = 2, C2 = 20   [10]
O-
Use Euclidean distance and perform 2 iterations.
2;
B
L-
3
Step 1: Assign points to nearest centroid (2 marks)
Point   Distance to   Distance to   Cluster
C1=2   C2=20
2   0   18   C1
4   2   16   C1
10   8   10   C1
12   10   8   C2
3   1   17   C1
20   18   0   C2
30   28   10   C2
11   9   9   C1 (tie → choose C1)
25   23   5   C2
Step 2: Form clusters (2 marks)
• Cluster C1 → {2, 4, 10, 3, 11}
• Cluster C2 → {12, 20, 30, 25}
Step 3: Compute new centroids (2 marks)
C1=2+4+10+3+11 / 5=30/5=6
C2=12+20+30+25/4=87/4=21.75
Step 4: Reassign points (Iteration 2) (2 marks)
Point   Dist to   Dist to   Cluster
C1=6   C2=21.75
2   4   19.75   C1
4   2   17.75   C1
10   4   11.75   C1
12   6   9.75   C1
********** 9 **********
--- page 10 ---
3   3   18.75   C1
20   14   1.75   C2
30   24   8.25   C2
11   5   10.75   C1
25   19   3.25   C2
Step 5: Final clusters
• C1 → {2, 4, 10, 12, 3, 11}
• C2 → {20, 30, 25}
Step 6: Final centroids
C1=2+4+10+12+3+11/6=7
C2 =20+30+25/3=25
Final Answer (2 marks)
•   Cluster 1 → {2, 4, 10, 12, 3, 11}, Centroid = 7
•   Cluster 2 → {20, 30, 25}, Centroid = 25
Q   b Following table shows the experience in years (X) and monthly salary (Y) of employees.
5   X   1   2   3   4   5   6
C   Y   30   35   50   55   65   80
O-   (i) Compute the regression equation of Y on X using the least squares method.
3;   (ii) Estimate the salary of an employee with 3.5 years of experience. Calculate the
S   residual for the employee with 4 years of experience   [10]
O-
2;
B
L-
3
Table calculation – 2 marks
Calculation of coefficients – 3 marks
Equation of line – 1 marks
Prediction – 2 marks
Residual – 2 marks
********** 10 **********
--- page 11 ---
Q   a When predicting student performance, selecting an attribute that maximizes information
6   gain is crucial.
[10]
C   • Briefly explain how entropy is used to measure uncertainty in classification.
O-
********** 11 **********
--- page 12 ---
5;   • Using the dataset below, determine which feature should be selected as the root
S   node.
O-   Study   High   High   High   High   Low   Low   Low   Low
2;   Hours
Attendance Good Good   Poor   Poor   Good   Good   Poor   Poor
B
L-   Result   Pass   Pass   Fail   Fail   Pass   Fail   Fail   Fail
3
1. Entropy Concept (3 Marks)
• Entropy (H) measures the uncertainty/impurity in a dataset.
• Formula:
𝐻= −𝑝1log⁡2 𝑝1 −𝑝2log⁡2 𝑝2
• 𝐻= 0→ pure (all same class)
• Higher 𝐻→ more mixed classes
Used to evaluate how good a split is.
2. Entropy of Dataset (2 Marks)
Class distribution: Pass = 3, Fail = 5 (Total = 8)
𝑝𝑃𝑎𝑠𝑠= 3/8 = 0.375,𝑝𝐹𝑎𝑖𝑙= 5/8 = 0.625
𝐸𝑛𝑡𝑟𝑜𝑝𝑦≈−(0.375log⁡2 0.375 + 0.625log⁡2 0.625) ≈0.954
3. Information Gain Calculation (4 Marks)
Split on Study Hours
High → (Pass,Pass,Fail,Fail) = (2,2)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐻𝑖𝑔ℎ= 1
Low → (Pass,Fail,Fail,Fail) = (1,3)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐿𝑜𝑤= 0.811
Weighted Entropy
4   4
= (1) + (0.811) = 0.5 + 0.405 = 0.905
8   8
Information Gain
𝐼𝐺𝑆𝑡𝑢𝑑𝑦= 0.954 −0.905 = 0.049
Split on Attendance
Good → (Pass,Pass,Pass,Fail) = (3,1)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝐺𝑜𝑜𝑑= 0.811
Poor → (Fail,Fail,Fail,Fail) = (0,4)
𝐸𝑛𝑡𝑟𝑜𝑝𝑦𝑃𝑜𝑜𝑟= 0
Weighted Entropy
4   4
= (0.811) + (0) = 0.405
8   8
Information Gain
𝐼𝐺𝐴𝑡𝑡𝑒𝑛𝑑𝑎𝑛𝑐𝑒= 0.954 −0.405 = 0.549
4. Final Decision (1 Mark)
• IG (Study Hours) = 0.049
• IG (Attendance) = 0.549
Best Attribute: Attendance
Justification:
• Higher information gain
• Produces a pure node (Poor → all Fail)
•   Better class separation
b Given the following 2D dataset:
Q
Points: A(1,1), B(1.2,1.1), C(0.8,1.2), D(8,8), E(8.2,8.1), F(25,25)   [10]
6
Apply DBSCAN with Eps = 0.5, MinPts = 3. Use Euclidean distance.
********** 12 **********
--- page 13 ---
C
O-
4;
S
O-
1;
B
L-
3
Step 1: Find ε-neighborhood (Eps = 0.5) (4 marks)
We compute distances (only nearby points matter):
Distance(A,B) ≈ √[(1.2−1)² + (1.1−1)²] ≈ 0.22
Distance(A,C) ≈ √[(0.8−1)² + (1.2−1)²] ≈ 0.28
Both < 0.5
So:
A → neighbors: {A, B, C} → count = 3
For B: neighbors = {A, B, C} → count = 3
For C: neighbors = {A, B, C} → count = 3
Distance(D,E) ≈ 0.22 → neighbors = {D, E} → count = 2
F is far from all → neighbors = {F} → count = 1
Step 2: Identify core, border, noise (4 marks)
Core points (≥ MinPts = 3)
→ A, B, C
Border points (<3 but near core)
→ None
Noise points
→ D, E, F
Step 3: Form clusters
Cluster 1 → {A, B, C}
Noise → {D, E, F}
Final Answer: (2 marks)
Cluster formed: {A, B, C}
Noise points: D, E, F
Q   a
7
C
O-
1;
S   Why is machine learning preferred over traditional programming for complex real-world
[5]
O-   problems? Explain with examples.
1;
B
L-
2
Why Traditional Programming Fails for Complex Problems (2 marks)
Real-world problems are too complex and variable.
Rules are hard to define explicitly.
Systems don’t adapt unless reprogrammed.
Why Machine Learning Works Better (2 marks)
********** 13 **********
--- page 14 ---
Machine learning can learn, adapt, and scale, making it suitable for complex, real-world
problems where fixed rules are not enough.
Example (1 mark)
Q   b A classifier fails to correctly predict certain training samples. Explain how AdaBoost
7   modifies the learning process to improve performance on such samples.
C
O-
5;
S
[5]
O-
1;
B
L-
3
Concept of AdaBoost (1 Mark)
• AdaBoost is a boosting ensemble method that builds a strong classifier by
combining multiple weak learners (e.g., decision stumps).
Modification of Learning Process (4 Marks)
1. Initialize Weights
•   All training samples are assigned equal weights initially.
2. Identify Errors
•   After training a weak learner, misclassified samples are identified.
3. Update Weights
•   Misclassified samples → weights increased
•   Correctly classified samples → weights decreased
This forces the next model to focus more on difficult samples.
4. Sequential Learning
• Each new learner is trained on the updated weighted dataset.
• Hard samples receive more importance over iterations.
5. Weighted Combination
• Each learner is assigned a weight based on accuracy.
•   Final prediction is a weighted vote of all learners.
Q   c
7
C
O-
4;
Apply Agglomerative Clustering (Complete Linkage) on the dataset: Points (2D): A(1,1),
S
B(2,2), C(5,5), D(6,6). Use Euclidean distance and perform clustering until 1 cluster [10]
O-
remains
1;
B
L-
3
********** 14 **********
--- page 15 ---
Step 1: Compute distance matrix (3 marks)
A   B   C   D
A 0   √2≈1.41   √32≈5.66   √50≈7.07
B   1.41   0   √18≈4.24   √32≈5.66
C   5.66   4.24   0   √2≈1.41
D   7.07   5.66   1.41   0
Step 2: Find closest pair (1 mark)
Minimum distance = 1.41 → (A,B)
Merge → C1 = {A,B}
Step 3: Update distances (Complete linkage = maximum distance) (2 marks)
d(C1,C) = max(5.66, 4.24) = 5.66
d(C1,D) = max(7.07, 5.66) = 7.07
Step 4: Next closest pair (2 marks)
Minimum distance = 1.41 → (C,D)
Merge → C2 = {C,D}
Step 5: Final merge (2 marks)
Distance between clusters:
d(C1,C2) = max(5.66, 7.07, 4.24, 5.66) = 7.07
Merge → Final cluster = {A,B,C,D}
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper bfa70617a624

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSE_DS_7057/Machine Learning/ANS_Machine Learning(702AI0C032)_2025-2026.pdf`
- Text: ocr (1 page)

````text

````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 90dffa7c7171

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CSBS_7036/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: mixed (10 pages), mean OCR confidence 85.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (CSBS)
Year: III / IV/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No.1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. Answer to each question to be started on a fresh page
6. Assume suitable data if necessary
7. Figures in bracket on the right hand side indicate full marks
Q1   Answer briefly:   [20]
a) P1 = (1,1) , P2 = (1.5,2) , P3 = (3,4) , P4 = (5,7) and P5 = (3.5,5). Using K Means
clustering find 2 clusters. Assume initial clusters as P1 and P2.
Ans:
2+2 Marks for distance calculation and 1 mark for final clusters.
Step 1: Initialization
initial centroids as:
C₁ = P₁ = (1, 1)
C₂ = P₂ = (1.5, 2)
Step 2: Compute Euclidean Distances
We’ll calculate the distance of each point from both centroids.
Formula:
𝑑= √(𝑥2 −𝑥1)2 + (𝑦2 −𝑦1)2
Point Coordinates   d(P, C₁)   [5]
P₁   (1, 1)   0
P₂   (1.5, 2)   √((1.5−1)² + (2−1)²) = √(0.25 + 1) = 1.118
P₃   (3, 4)   √((3−1)² + (4−1)²) = √(4 + 9) = 3.606
P₄   (5, 7)   √((5−1)² + (7−1)²) = √(16 + 36) = 7.211
P₅   (3.5, 5)   √((3.5−1)² + (5−1)²) = √(6.25 + 16) = 4.719
Distance from P2:
Point Coordinates   d(P, C₂)
P₁   (1, 1)   1.118
P₂   (1.5, 2)   0
P₃   (3, 4)   √((3−1.5)² + (4−2)²) = √(2.25 + 4) = 2.5
********** 1 **********
--- page 2 ---
P₄   (5, 7)   √((5−1.5)² + (7−2)²) = √(12.25 + 25) = 6.103
P₅   (3.5, 5)   √((3.5−1.5)² + (5−2)²) = √(4 + 9) = 3.606
Assigning points to the nearest cluster.
Point d(P, C₁) d(P, C₂) Assigned Cluster
P₁   0   1.118   C₁
P₂   1.118   0   C₂
P₃   3.606   2.5   C₂
P₄   7.211   6.103   C₂
P₅   4.719   3.606   C₂
Cluster Assignment (Iteration 1):
•   Cluster 1 (C₁): { P₁ }
•   Cluster 2 (C₂): { P₂, P₃, P₄, P₅ }
How is variance reduction achieved in Random Forest? What is OOB concept in Random
forest?
3 marks for part a and 2 marks for OOB concept.
Ans: Random Forest is an ensemble of decision trees built using two key ideas:
1. Bootstrap Sampling (Bagging)
2. Feature Randomness (Random Subspace Method)
(a) Bootstrap Aggregation (Bagging)
• Each tree is trained on a different random subset of the data (sampled with
replacement).
•   Since each tree sees a slightly different dataset, their errors are uncorrelated.
•   Final prediction is made by averaging (for regression) or voting (for [5]
classification)   over   all   trees.
Averaging multiple uncorrelated models reduces variance without increasing bias.
(b) Random Feature Selection
• At each split in a tree, Random Forest randomly selects a subset of features
instead of using all features.
•   This decorrelates the trees further, because different trees may choose different
predictors.
Variance reduction is achieved through:
1. Bagging (Bootstrap sampling) — different data subsets
2. Random feature selection — different predictors per split
3. Averaging/Voting — combining results to smooth out fluctuations
c) Why do we use Polynomial Regression instead of Linear Regression in some cases?
Explain with an example.
3 marks for first part, 2 marks for example and explanation.
Limitation of Linear Regression
Linear Regression assumes a linear relationship between the independent variable 𝑋and
the dependent variable 𝑌.   [5]
That is:
𝑌= 𝛽0 + 𝛽1𝑋+ 𝜀
However, in many real-world problems, the data shows a non-linear pattern — the
change in 𝑌is not proportional to the change in 𝑋.
In such cases, a straight line cannot capture the underlying trend accurately.
********** 2 **********
--- page 3 ---
Polynomial Regression – The Solution
Polynomial Regression is an extension of Linear Regression that allows modeling
curved relationships between 𝑋and 𝑌.
It adds higher-degree polynomial terms of the predictor variable.
The general form is:
𝑌= 𝛽0 + 𝛽1𝑋+ 𝛽2𝑋2 + 𝛽3𝑋3 + ⋯+ 𝛽𝑛𝑋𝑛+ 𝜀
This still uses linear coefficients 𝛽0, 𝛽1, … , 𝛽𝑛, so it’s called polynomial regression, but
it is still a type of linear model in parameters.
When to Use Polynomial Regression
Use Polynomial Regression when:
• The relationship between 𝑋and 𝑌is non-linear but smooth (e.g., curved,
parabolic).
• The residuals from a linear regression show a pattern, suggesting underfitting.
• You want a better fit without switching to complex models like neural networks.
d)
What is absolute scaling method and Min-Max scaling method? Explain the disadvantage
of using absolute scaling method with an example.
Ans:
3 marks for first part, 2 Marks for second part
Absolute Scaling divides by the maximum but ignores the minimum → can produce
negative or biased results.   [5]
Min–Max Scaling adjusts based on both min and max, preferred and robust for most
ML preprocessing tasks.
Disadvantage: The main disadvantage is that the technique is sensitive to outliers. Like
consider the feature ‘square feet’, if 99% of the houses have square feet area of less than
1000, and even if just 1 house has a square feet area of 20,000, then all those other house
values will be scaled down to less than 0.05.
Q2   [20]
a)   Explain the concept of One-Hot Encoding used for handling categorical variables in
machine learning. How can One-Hot Encoding lead to multicollinearity in models such
as Linear or Logistic Regression? Illustrate your answer with a suitable example and
describe how this issue can be resolved.
Ans:
3 marks first part, 2 marks second part and 5 marks third part.
One-Hot Encoding is a technique used to convert categorical variables (non-numeric
data such as gender, color, type, etc.) into a numerical format that can be used by   [10]
algorithms.
Many ML algorithms (like Linear Regression, Logistic Regression, SVM, etc.) require
numerical inputs. One-Hot Encoding converts a categorical feature with n unique
categories into n binary (0/1) variables, each representing the presence (1) or absence
(0) of one category.
Multicollinearity occurs when one or more independent variables in a regression model
are highly correlated, meaning one can be predicted linearly from others.
b)   Explain the activation functions in neural networks Sigmoid, ReLU, and Tanh.
For each function, write its mathematical expression, specify its output range, and   [10]
describe when and why it is used in neural network models.
********** 3 **********
--- page 4 ---
Ans: Mathematical expression=4 Marks+ 6 marks for range and when and why used
Activation functions introduce non-linearity into neural networks, enabling them to
learn complex relationships between inputs and outputs.
They determine how the weighted sum of inputs is transformed into the output of a
neuron.
Q3   [20]
a). A teacher records marks of two sections of a class in the final exam:
Section A:
40,50,52,55,58,60,62,65,70,80
Section B:
35,38,40,45,50,52,55,60,65,90
1. Draw box plots for both sections.
2. Identify which section performed better overall. Compare their median and IQR
3. Determine which dataset is more skewed, and explain which type of skewness it
is.
4. State your Analysis
Ans:
2.5 each Answer.
Section A   [10]
Ordered Data: 40, 50, 52, 55, 58, 60, 62, 65, 70, 80
n = 10
• Minimum (Min): 40
• Maximum (Max): 80
• Median (Q2): Average of 5th & 6th = (58 + 60) / 2 = 59
• Q1 (25th percentile): Median of lower half (40, 50, 52, 55, 58) → 52
• Q3 (75th percentile): Median of upper half (60, 62, 65, 70, 80) → 65
IQR = 𝑄3 −𝑄1 = 65 −52 = 13
Section B
Ordered Data: 35, 38, 40, 45, 50, 52, 55, 60, 65, 90
n = 10
• Min: 35
• Max: 90
• Median (Q2): (50 + 52) / 2 = 51
********** 4 **********
--- page 5 ---
• Q1: Median of (35, 38, 40, 45, 50) → 40
• Q3: Median of (52, 55, 60, 65, 90) → 60
IQR = 𝑄3 −𝑄1 = 60 −40 = 20
b)
The professor wishes to build a predictive model using Linear Regression to understand
and quantify the relationship between hours of study and exam performance.
Hours of Study   Exam Score
1   52
2   56
3   61
4   66
5   70
6   74
7   78
8   85
[10]
1. Plot a scatter diagram to visualize the relationship between hours studied and
exam scores.
2. Calculate the R-squared (R²) value to measure how well the model fits the data.
3. Use the model to predict the expected exam score if a student studies for 10
hours.
Intercept=47.28   2 Marks
Slope=4.548   2 marks
R square=0.799   3 marks
10 hours of study=92.78 3 marks
Q4   [20]
a)   Neural network small problem. Three inputs 0.7,0.4 and 0.3 is given as inputs, with the
weights 0.2,0.3 and -0.2 respectively. And bias value is =0.25. Find the output using
sigmoid activation function. Draw the neat neural network with all the parameters.
[10]
Ans:5 Marks each
b)   Agglomerative algorithm with the following data and plot a Dendogram using single
link approach.   [10]
********** 5 **********
--- page 6 ---
1. Compute the Euclidean Distance Matrix between all customers. 2 marks
2. Apply the Agglomerative Hierarchical Clustering (Single Linkage) method
manually, draw the dendogram 7 marks
3. Identify which customers form clusters first. 1 marks
Customer Income Spending Score
C1   25   30
C2   28   35
C3   70   65
C4   72   72
C5   75   80
Q5   [20]
a)   Explain the concept of Dimensionality Reduction in Machine Learning. Why is it
necessary? Discuss the Principal Component Analysis (PCA) technique for
dimensionality reduction. Describe the mathematical steps involved in PCA and explain
how it helps in feature extraction.
Ans:
2 marks, 3+ 3 marks discuss and describe, 2 marks for feature extraction part
Dimensionality Reduction is the process of reducing the number of input variables or
features in a dataset while retaining the most important information.
In simple terms, it transforms a high-dimensional dataset (with many variables) into a
lower-dimensional one (with fewer variables) without losing significant patterns or
relationships in the data.
Why Dimensionality Reduction is Necessary
1. Removes Redundant Features:   [10]
Many features may be correlated or carry overlapping information. Reduction
eliminates redundancy.
2. Reduces Overfitting:
Fewer features lead to simpler models that generalize better.
3. Improves Computational Efficiency:
Reducing dimensions decreases storage, training time, and computational cost.
4. Better Visualization:
Data with 2 or 3 dimensions can be plotted for easier interpretation.
5. Noise Reduction:
It filters out irrelevant or less important features, enhancing model performance.
Steps of Principal Component Analysis (PCA):
1. Standardize the data
2. Compute the covariance matrix
********** 6 **********
--- page 7 ---
3. Calculate eigenvalues and eigenvectors
4. Sort eigenvalues in descending order
5. Select the top k eigenvectors (principal components)
6. Form the projection matrix using selected eigenvectors
7. Transform the original data onto the new subspace
b) A hospital has developed a machine learning model to classify patients into three
categories based on their medical test results: Class A: Healthy, Class B: At Risk, Class
C: Diseased. Find Precision, Recall and Accuracy for all 3 classes from the following
Confusion Matrix.
Actual/Predicated Healthy At Risk   Diseased
Healthy   25   3   2
At Risk   4   20   6
Diseased   1   5   24
Formula- 4 marks+ 6 marks
[10]
Q6   [20]
a)   Explain the working of a Support Vector Machine (SVM) classifier for linearly
separable data with the following points wrt SVM algorithm. i)The objective function of
SVM ii)The concept of margin maximization iii) The role of support vectors iv) A neat
diagram showing separating hyperplane and margins.
Ans:
2.5 each Marks.   [10]
A Support Vector Machine (SVM) is a supervised learning algorithm used for
classification and regression tasks.
For linearly separable data, SVM aims to find the best possible decision boundary
(hyperplane) that separates data points of different classes with the maximum margin.
B
A company wants to predict whether a new email (X) is Spam or Not Spam using a
Naïve Bayes Classifier based on the presence of certain keywords.
A new email (X) has the following features:
Offer = Yes, Free = Yes, Click = No
Email
Offer Free Click Label
ID
1   Yes   Yes   Yes   Spam
********** 7 **********
--- page 8 ---
2   Yes   No   Yes   Spam
Not
3   No   Yes No
Spam
Not
4   Yes   No   No
Spam
5   No   Yes   Yes   Spam
Not
6   No   No   No
Spam
Marks: 4 marks + 4 marks+ 2 Marks
For spam
For Not spam:
It is spam.
Q7   [20]
a)   Differentiate between Bagging and Boosting in terms of sampling method, model
training, and error handling. What is the intuition behind Boosting? How does it convert
weak learners into a strong learner?
[10]
Ans: 6 marks+ 2 Marks+ 2Marks
********** 8 **********
--- page 9 ---
A telecom company wants to predict whether a customer will churn (leave the service)
b)   or stay, based on certain attributes.
The dataset is shown below: For the given dataset, find which is the suitable root node
using ID3 decision Tree algorithm.
[10]
Customer
Payment
Customer Contract Type   Support   Churn
Method
Calls
Month-to-
1   Online   High   Yes
Month
Month-to-
2   Online   Low   No
Month
3   One Year   Offline   Low   No
4   Two Year   Offline   Low   No
Month-to-
5   Offline   High   Yes
Month
6   One Year   Online   Medium   No
7   Two Year   Online   Low   No
Month-to-
8   Online   Medium   Yes
Month
9   One Year   Offline   High   No
10   Two Year   Online   Medium   No
Ans: Entropy 2 marks+ 4 Marks+ 4 marks
Entropy= 0.881
********** 9 **********
--- page 10 ---
6 4
E(Payment) = 79 (0-918) + i (2-814) = 0.875

Information Gain:

IG(Payment) = 0.881 — 0.875 = 0.006

Weighted Entropy:

3 3 4
E(SupportCalls) = —(0.918) + —(0.918) + rly = 0.551

10 10

Information Gain:

IG(SupportCalls) = 0.881 — 0.551 = 0.330

The attribute with the highest Information Gain is Contract Type.

FRR ICR 7 OI HOH
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper cc28d41983d9

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CSE_DS_7011/Machine Learning/ANS_Machine Learning(702DB0C015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No 1 is compulsory.
3. Out of remaining questions, attempt any 4questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
a)   Using get_dummies method in Python, find One hot encoding for the given dataset. (Using
Python Code). Show the step by step approach while using one hot encoding. List the
appropriate Libraries used in the implementation.
Ans:
[5]
appropriate library and commands required.
Food Name   Calories
Cookies   70
Chocolates   60
Cakes   80
b)   Explain the concept of bagging and boosting with neat diagram.
Ans:
Bagging builds multiple independent models (usually of the same type, e.g.,
decision trees).Each model is trained on a randomly sampled subset of the   [5]
training data (using replacement → bootstrap sampling).
• Final output is obtained by: Averaging predictions (for regression)
Majority voting (for classification)
c)   What is regularization in machine learning, and why is it needed? What is the difference
between L1 and L2 regularization?
Ans:
[5]
Regularization is a technique used to prevent overfitting in machine learning
models by adding a penalty term to the model’s cost (or loss) function.
********** 1 **********
--- page 2 ---
It discourages the model from fitting too closely to the training data, especially
by penalizing large coefficient (weight) values.
d)   Identify the Most Suitable machine learning algorithm
a) Predicting tomorrow’s temperature
b) Grouping students based on learning habits.
c) Classifying handwritten digits (0–9).
d) You have multiple dependent variables and continuous outputs.   [5]
e) Predicting the likelihood that a loan applicant will default.
Ans: Linear Regression, Clustering (unsupervised grouping), Multiclass Classification,
Multivariate Regression
Q2   [20]
a) A neural network has inputs: x1=0.6, x2=0.9. Assume necessary data.
[10]
Ans:
a)Compute the net input and output of each neuron using the sigmoid activation
function
b)Perform one step of backpropagation, updating the weights connected to h₂ →
output, assuming a learning rate (η) = 0.1, Expected output is 1.
b)   Apply the K-Means algorithm with K=2, with the following centroids: The
dataset is:{12,25,30,15,19,22,28,38,20}. Centroids are C1=15,C2=25
Cluster Data Points Final Centroid   [10]
C₁ {12, 15, 19, 20, 22} 17.6
C₂ {25, 28, 30, 38} 30.25
Q3   [20]
a).   What is the decision boundary, and how is it derived in logistic regression?
A healthcare startup wants to predict whether a patient is at risk of diabetes (Yes = 1,
No = 0) based on their Body Mass Index (BMI).
The company uses a logistic regression model trained on patient data. where c=−6,   [10]
m=0.25. Use Logistic regression to solve the problem.
a) Compute the probability that a patient with a BMI of 28 will have
diabetes.
********** 2 **********
--- page 3 ---
b) Find the BMI value at which the probability of having diabetes
becomes 0.7.
b)   A healthcare analyst is studying whether smoking habits are associated with higher
systolic blood pressure (SBP) readings.
Group SBP Readings (mmHg)
Smokers [120, 125, 130, 135, 140, 145, 150, 155, 160, 170]
Non-Smokers [110, 115, 118, 120, 122, 125, 128, 130, 135, 140]   [10]
a) Draw box plots for both groups Smokers and Non-Smokers on the same
graph. (b) From the data, calculate for each group find Minimum, First Quartile
(Q1), Median (Q2), Third Quartile (Q3), Maximum, Interquartile (c) Identify
any potential outliers using the 1.5 × IQR rule.
Q4   [20]
a)
Explain the meaning of the slope (m) and intercept (c) in a regression line. Draw using
neat diagram. Solve the model to predict the salary of an employee after 12 years of
work experience using Linear Regression.
[10]
Years of   Salary in
Experience   $1000
3   30
8   57
9   64
13   72
4   36
b)   Discuss the Agglomerative algorithm with the following data and plot a Dendogram
using complete linkage approach. The table below comprises sample data items
indicating the distance between elements.
A B C D E
[10]
A 0
B 0.6 0
C 0.8 0.7 0
D 0.5 1.2 0.4 0
E 0.9 0.3 0.5 0.6 0
Q5   [20]
a)   You are given a binary classification model that predicts whether patients have a
certain disease. The model outputs probabilities for the positive class. Plot the ROC
curve for this model. Explain what the ROC curve and AUC tell you about the
performance of the model.
True Positive False Positive
Threshold Rate (TPR)   Rate (FPR)   [10]
0.9   0.2   0.01
0.7   0.5   0.05
0.5   0.7   0.10
0.3   0.85   0.20
0.1   0.95   0.50
********** 3 **********
--- page 4 ---
b)   In a zoo keeper want to classify the animals into different species, such as Monkey,
Lion, and Tiger, using an automated image recognition system. The goal is to assist
zookeepers in monitoring bird populations, tracking their health, and ensuring proper
care for each species.
Find Precision and Accuracy for Monkey and Lion class from the following Confusion
Matrix.   [10]
Predicted animal class
Monkey   Lion   Tiger
Actual   Monkey   50   8   2
animal   Lion   5   40   10
Class   Tiger   3   7   45
Q6   [20]
a)   Compare SVM with Logistic Regression. Under what circumstances might one be   [10]
preferred over the other? Define the kernel trick. Why is it useful in SVMs?
b)   Use the gradient descent principles for cost function. Given the slope as 0.5, find the
MSE with random intercept values 0, 2, 4, 6. Plot these values and find the lowest cost
function. Explore how the intercept affects MSE. The data table is as below.   [10]
X   1   2   3   4
Y   3   5   7   9
Q7   [20]
a)   Define anomaly detection and explain its importance in machine learning
applications. Describe at least two approaches for anomaly detection.
[10]
Ans: Z score, clustering
Use the Id3 classifier to predict whether an incoming email is Spam or Not Spam. Find
b)   the best root node, also construct DT for the given dataset.
Ans: Best root node = Contains Attachment
Contains Contains
Spam
Link   Attachment
[10]
Yes   No   Yes
Yes   Yes   Yes
No   No   No
Yes   No   Yes
No   No   No
No   Yes   Yes
Yes   No   No
No   No   No
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 81c53fc33e01

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (EXTC)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No.1 is compulsory.
3. Out of remaining questionsa attempt any 4 questions.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figure in brackets on the right hand side indicates full marks.
7. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Define Bias and Variance in a machine learning model. How do they contribute to the total   [05]
SO-   error of the model?
1;
Solution:
BL
Bias and Variance are two fundamental sources of error that determine the performance and
-2
generalization ability of a machine learning model.
Bias:
Bias refers to the error introduced due to simplifying assumptions made by the model while
learning the data. It measures how far the model’s predicted values are from the actual values
on average.
• High bias implies the model is too simple and fails to capture the underlying patterns.
•   It often leads to underfitting.
Variance:
Variance refers to the model’s sensitivity to small fluctuations in the training dataset. It
measures how much the model’s predictions change when trained on different subsets of data.
• High variance implies the model is too complex and captures noise along with
patterns.
•   It often leads to overfitting.
Contribution to Total Error:
The overall prediction error of a model can be decomposed as:
Total Error = Bias² + Variance + Irreducible Error
•   Bias²: Error due to incorrect assumptions
•   Variance: Error due to model instability
•   Irreducible Error: Noise inherent in the data that cannot be eliminated
Intuition:
• A model with high bias and low variance is consistent but inaccurate.
• A model with low bias and high variance is accurate on training data but unstable on
new data.
So we can conclude that
An optimal model minimizes total error by balancing bias and variance, ensuring good
generalization to unseen data.
********** 1 **********
--- page 2 ---
CO-1; SO-   b. Find outlier in following data set using IQR method.   [05]
1; BL   (0.1,1,10,20,25,30,35,40,45,230,500, 50,55,60,65,70,75,80,100,150,175,200)
-4   Solution:
Q1=30
Q3=100
IQR=Q1-Q3=75
Lower Fence=Q1-1.5(IQR)=-75
Upper Fence=Q1+1.5(IQR)= 205
So 230,500 are outlier
CO-2; SO-1;   c. Explain about maximum margin hyper plane in Linear support vector machine.   [05]
BL-2   Solution:
It is a supervised machine learning problem where we try to find a
hyperplane that best separates the two classes. Both the algorithms try to
find the best hyperplane, but the main difference is logistic regression is a
probabilistic approach whereas support vector machine is based on statistical
approaches.
There can be an infinite number of hyperplanes passing through a point
and classifying the two classes perfectly.
SVM does this by finding the maximum margin between the hyperplanes that
means maximum distances between the two classes.
The maximum margin will be
CO-2; SO-2;   d. Discuss the computational complexity of K-Means and Hierarchical Clustering and   [05]
BL-2   its impact on scalability.
Solution:
K_Means and Hierarchical Clustering: 02 M
Comaparison: 03 M
********** 2 **********
--- page 3 ---
K-Means is an iterative algorithm.
• Time Complexity:
O(n × k × t × d)
where:
o n = number of data points
o k = number of clusters
o   t = number of iterations
o d = number of features
• Each iteration assigns points to nearest centroid → O(n × k)
• Updating centroids → O(n)
• Repeated for t iterations
Hierarchical clustering builds a tree (dendrogram).
• Time Complexity:
O(n² log n) (optimized) or up to O(n³) (naive)
• Space Complexity:
O(n²) (distance matrix)
• Computes pairwise distance matrix → O(n²)
• Repeated merging/splitting of clusters
• Updating distances after each merge
K-Means and Hierarchical Clustering are widely used unsupervised learning
algorithms, but they differ significantly in terms of computational complexity and
scalability.
K-Means is an iterative, partition-based clustering algorithm. Its time complexity is
generally O(n × k × t × d), where n is the number of data points, k is the number of
clusters, t is the number of iterations, and d is the number of features. In practice,
since k and t are usually small and fixed, the complexity grows approximately
linearly with the number of data points (n). This makes K-Means computationally
efficient and suitable for large datasets. Additionally, it requires relatively low
memory, as it does not need to store pairwise distances between all data points.
In contrast, Hierarchical Clustering is a tree-based approach that builds a hierarchy of
clusters using either a bottom-up (agglomerative) or top-down (divisive) strategy. Its
time complexity is significantly higher, typically O(n² log n) in optimized
implementations and up to O(n³) in naïve implementations. This is because it requires
computing and updating a full pairwise distance matrix between data points, which
itself requires O(n²) space. As the number of data points increases, both the
computational time and memory requirements grow rapidly.
The difference in computational complexity has a direct impact on scalability. K-
Means is highly scalable and can efficiently handle large datasets with thousands or
even millions of data points. It is commonly used in real-world applications such as
customer segmentation and image processing. On the other hand, Hierarchical
Clustering does not scale well to large datasets due to its high time and space
********** 3 **********
--- page 4 ---
complexity. It is more suitable for smaller datasets where understanding the
hierarchical relationships between clusters is important.
Q2   a.   [10]
CO-2;   In the organization in Mumbai the chief medical officer of the in house dispensary is
SO-   distributed because of the alarming rise in the cases of high blood pressure among
2;   young male employees. A study of high BP men employees revealed that two main
BL-
factors causes high BP. Work related stress and family related stress. The chief
4
medical officer collected the data for a period of five weeks which is given bellow.
From the data set calculate multiple regression equation for employee suffering from
high blood pressure
No of employee suffering from high Blood Pressure   60   52 56 64   68
No of employee suffering from work related stress   47   41 50 42   40
No of employee suffering from family relates stress   22   26 18 13   21
Solution:
Final MLR equation is X1=19.52+0.51X2+0.902X3
Q2   b. Explain how the total error can be minimize by using error back propagation   [10]
CO-2; SO-2;   algorithm in feedforward neural network. Explain with steps.
BL-2   Solution:
Error Backpropagation, short for Backward Propagation of Errors, is a key
algorithm used to train neural networks by minimizing the difference between
predicted and actual outputs. It works by propagating errors backward through the
network, using the chain rule of calculus to compute gradients and then iteratively
updating the weights and biases.   01 Marks
********** 4 **********
--- page 5 ---
Back Propagation plays a critical role in how neural networks improve over time. Here's
why:
1. Efficient Weight Update: It computes the gradient of the loss function with respect
to each weight using the chain rule making it possible to update weights efficiently.
2. Scalability: The Back Propagation algorithm scales well to networks with multiple
layers and complex architectures making deep learning feasible.
3. Automated Learning: With Back Propagation the learning process becomes
automated and the model can adjust itself to optimize its performance.
Steps of error back propagation.
The process involves two main phases: a forward pass, where the input data is passed
through the network to compute the output, and a backward pass, where the gradients are
computed by propagating the error backward through the network.
Forward Pass
In the forward pass, the input data is fed into the network, and operations defined by the
network architecture are performed layer by layer to compute the output. This output is
then used to calculate the loss, which measures the difference between the network's
prediction and the true target values.
Backward Pass
The backward pass starts with the computation of the gradient of the loss function with
respect to the output of the network. Then, by applying the chain rule, the algorithm
calculates the gradient of the loss with respect to each weight by propagating the error
information back from the output layer to the input layer. This process involves the
following steps:
1. Compute the derivative of the loss function with respect to the activations of the
output layer.
2. For each layer, starting from the last hidden layer and moving to the first, compute
the gradients of the loss with respect to the layer's inputs, which are the activations
of the previous layer.
3. Compute the gradients of the loss with respect to the weights by considering the
gradients with respect to the layer's inputs and the derivatives of the layer's
activations with respect to its weights.
These gradients tell us how much a change in each weight would affect the loss, allowing
the optimization algorithm to adjust the weights in a direction that minimizes the loss.
Updating Weights
Once the gradients are computed, the weights are updated typically using a gradient
descent optimization algorithm. The weight update rule is generally of the form:
new_weight = old_weight - learning_rate * gradient
where the learning rate is a hyperparameter that controls the size of the weight updates.
These steps repeated multiple time to minimize the total error generated at the
********** 5 **********
--- page 6 ---
output
Q3   a. Consider the dataset:   [10]
CO-3;
SO-6;
BL-3   Credit Score   Income   Loan Approved
High   High   Yes
High   Medium   Yes
Medium   High   Yes
Low   Medium   No
Low   Low   No
Medium   Low   No
Using ID3 algorithm:
•   Calculate Entropy of target variable
• Compute Information Gain for attributes
Determine the root node
Solution:
1. Entropy of Target Variable
Total = 6
Yes = 3, No = 3
[
H(S) = -0.5\log_2(0.5) - 0.5\log_2(0.5)
]
H(S) = 1
Entropy = 1
🔹 2. Information Gain
➤ Attribute: Credit Score
• High → (2 Yes, 0 No) → Entropy = 0
• Medium → (1 Yes, 1 No) → Entropy = 1
• Low → (0 Yes, 2 No) → Entropy = 0
Weighted entropy:
[
= \frac{2}{6}(0) + \frac{2}{6}(1) + \frac{2}{6}(0) = 0.333
]
********** 6 **********
--- page 7 ---
IG:
[
IG = 1 - 0.333 = 0.667
]
➤ Attribute: Income
• High → (2 Yes, 0 No) → Entropy = 0
• Medium → (1 Yes, 1 No) → Entropy = 1
• Low → (0 Yes, 2 No) → Entropy = 0
Weighted entropy = 0.333
[
IG = 1 - 0.333 = 0.667
]
🔹 3. Root Node
• IG(Credit Score) = 0.667
• IG(Income) = 0.667
Root Node: Either attribute (tie condition)
Q3   b. Explain the concept of Unsupervised Learning and discuss the major challenges faced [10]
CO-1;
SO-1;   while implementing it. Explain tree based unsupervised learning algorithm
BL-2
Solution:
Unsupervised Learning is a type of machine learning in which the model is trained
on data without labeled outputs. The system tries to identify hidden patterns,
structures, or relationships in the data on its own.
Examples
• Customer segmentation in marketing
• Grouping similar documents
•   Clustering users on platforms like Amazon based on behavior
Common Techniques
•   Clustering (e.g., K-Means)
********** 7 **********
--- page 8 ---
•   Association Rule Mining
• Dimensionality Reduction (e.g., PCA)
Challenges of Unsupervised Learning
1. No Labeled Data
• There is no ground truth to guide learning
•   Difficult to verify correctness of results
2. Evaluation Difficulty
• No clear metrics to measure performance
•   Results may vary and be subjective
3. Interpretation of Results
•   Clusters or patterns may be hard to understand
• Requires domain knowledge
4. Choosing Parameters
•   Selecting number of clusters (K in K-Means) is difficult
•   Results depend heavily on parameter choices
5. Sensitivity to Noise
•   Outliers and noisy data can affect results
• May lead to incorrect grouping
6. Scalability Issues
• Large datasets increase computational complexity
Some algorithms become slow
Explain Hierarchical clustering algorithm
Q4   a. In a war situation, military logistics planners need to forecast the daily ammunition   [10]
CO-2;
consumption of artillery units to ensure supply lines can meet demand. The model has
SO-
2;   the relationship between daily number of fire missions and the total shells consumed.
BL-   How this problem can be solved using simple linear regression and gradient descent
2   techniques?
Solution:
Assume a linear relationship between:
•   x: number of fire missions per day
•   y: total shells consumed per day
Simple Linear regression -
y = mx + b,
where y and x are variables,
********** 8 **********
--- page 9 ---
m is the slope, and
b is the y-intercept.
Gradient Descent –
We want to minimize prediction error using Mean Squared Error (MSE).
The steps followed are -
i.   Initialize parameters
ii.   Compute gradients
iii.   Update parameters
Repeat gradient computation and updates until the Cost function converges (minimal change)
or Maximum iterations reached.
Q4   b. For the training example, X=[1,0,1] and Target label t=1, and learning rate is 0.9. The [10]
CO-3;
SO-6;   sigmoid activation function is applied to both the hidden and output layers. The
BL-6   weights are given by,
X1 X2 X3 W14 W15   W24   W25 W34   W35 W46   W56   W04   W05 W06
1   0   1   0.2   -0.3   0.4   0.1   -0.5   0.2   -0.3   -0.2   -0.4   0.2   0.1
Solution:
Solution {each answer is 2 mark)(2*5=10)
4in = 0.2+0-0.5-0.4=-0.7 4out=0.332
5in= -0.3+0+0.2+0.2=0.1 5out=0.525
6in = -0.3*0.332- 0.2*0.525+0.1 =-0.105 6out = 0.474
actual output= 6out = 0.474
********** 9 **********
--- page 10 ---
Q5   a. Explain Random Forest algorithm in detail. Discuss how randomness in data   [10]
CO-3;   sampling and feature selection improves generalization.
SO-
1;   Solution:
BL   Definition
-3
Random Forest is an ensemble learning algorithm that builds multiple decision trees
and combines their outputs to improve accuracy and reduce overfitting.
🔹 Working Steps
1. Bootstrap Sampling (Bagging)
o Random samples are drawn with replacement from dataset.
2. Decision Tree Construction
o Each tree is trained on a different subset.
3. Random Feature Selection
o At each split, only a random subset of features is considered.
4. Aggregation
o Classification → Majority Voting
o Regression → Average
🔹 Role of Randomness
1. Data Sampling (Bagging)
• Each tree sees different data → reduces variance
• Prevents overfitting
2. Feature Selection
• Forces trees to be diverse
• Avoids dominance of strong features
🔹 Advantages
• High accuracy
• Reduces overfitting
********** 10 **********
--- page 11 ---
• Handles large datasets
• Works well with missing values
🔹 Limitations
• Computationally expensive
• Less interpretable
• Slower prediction time
🔹 Applications
• Fraud detection
• Medical diagnosis
• Recommendation systems
• Stock prediction.
Q5   b. Apply K-Means clustering on the following dataset representing Height (cm) and   [10]
CO-2;
SO-2;   Weight (kg): {(150,50),(155,55),(160,60),(170,70),(175,75),(180,80)}
BL-2
Perform clustering for K = 2 and K = 3. Show the steps, update centroids, and
compare the final clusters.
Solution:
Case 1: K = 2
Step 1: Initialize Centroids
Take first two points:
C1 = (150,50), C2 = (155,55)
Step 2: Assign Points (Iteration 1)
• Cluster 1 → (150,50)
• Cluster 2 → (155,55), (160,60), (170,70), (175,75), (180,80)
Step 3: Update Centroids
• C1 = (150,50)
• C2 = average = (168,68)
Iteration 2: Reassign Points
• Cluster 1 → (150,50), (155,55), (160,60)
• Cluster 2 → (170,70), (175,75), (180,80)
Update Centroids
• C1 = (155,55)
• C2 = (175,75)
********** 11 **********
--- page 12 ---
Final Clusters (K=2)
• Cluster 1: {(150,50), (155,55), (160,60)}
• Cluster 2: {(170,70), (175,75), (180,80)}
Case 2: K = 3
Step 1: Initialize Centroids
C1 = (150,50), C2 = (155,55), C3 = (160,60)
Step 2: Assign Points
• Cluster 1 → (150,50)
• Cluster 2 → (155,55)
• Cluster 3 → (160,60), (170,70), (175,75), (180,80)
Step 3: Update Centroids
• C1 = (150,50)
• C2 = (155,55)
• C3 = (171.25, 71.25)
Iteration 2: Reassign Points
• Cluster 1 → (150,50), (155,55)
• Cluster 2 → (160,60)
• Cluster 3 → (170,70), (175,75), (180,80)
Update Centroids
• C1 = (152.5, 52.5)
• C2 = (160,60)
• C3 = (175,75)
Final Clusters (K=3)
• Cluster 1: {(150,50), (155,55)}
• Cluster 2: {(160,60)}
• Cluster 3: {(170,70), (175,75), (180,80)}
Comparison
Aspect   K = 2   K = 3
Clusters   2 groups   3 groups
Grouping   Broad (short vs tall)   More detailed
Interpretation   Simple   More precise
Q6   a. Discuss the situation where polynomial regression is applicable. What is the impact of higher [10]
CO-2; SO-2;   degree polynomial on the final result?
BL-5   Solution:
Polynomial regression is needed when the relationship between the independent
variable and dependent variable is not linear, but follows a curved pattern. In such
cases, a simple linear regression model cannot fit the data accurately. Polynomial
regression extends linear regression by adding higher-order terms such as X2, X3 etc.,
to capture the non-linear trend.
The general form of a polynomial regression model is:
y=b0+b1x1+b2x12+b2x13+…bnx1n
********** 12 **********
--- page 13 ---
Where -
y is the dependent variable,
x1 is the independent variable, and
b0 - bn are the parameters you can optimize
Need for Polymer Regression
•   It helps model curvilinear relationships between variables.
•   It improves the fit when data points do not lie along a straight line.
•   It provides better prediction accuracy than simple linear regression for non-
linear data patterns.
Impact of higher degree polynomial –
1. Better fit to training data
2. Risk of overfitting
Increased variance
One can explain with example
********** 13 **********
--- page 14 ---
Q6   b. Explain K- fold- cross validation for the dataset with 10,000 samples and number   [10]
CO-4; SO-   of fold are 100. Comment if number of folds are 1000 for the same samples.
6;   Solution:
BL- 4   K-Fold Cross Validation
K-Fold Cross Validation is a model evaluation technique used to assess the
performance and generalization ability of a machine learning model.
Working of K-Fold Cross Validation
• The dataset is divided into K equal subsets (folds).
•   In each iteration:
o One fold is used as the testing/validation set.
o Remaining K−1 folds are used for training.
• This process repeats K times, so every sample is used:
o once for testing
o K−1 times for training
The final model performance is the average of all K results.
Case 1: Dataset = 10,000 Samples, K = 100
Given:
•   Total samples = 10,000
• Number of folds = 100
Fold Size
Each fold contains:
10000100=100\frac{10000}{100}=10010010000=100
So each fold has 100 samples.
In Each Iteration
•   Training samples:
10000−100=990010000-100 = 990010000−100=9900
•   Testing samples:
100100100
Thus, for each of the 100 iterations:
•   Train model on 9,900 samples
•   Test model on 100 samples
After 100 runs, average all performance scores.
Comment on 100 Folds
Advantages
• More training data in each run (99% data used for training)
• Lower bias in performance estimate
•   Better model evaluation than small K (like 5 or 10)
Disadvantages
• Computationally expensive (train model 100 times)
• Very small test sets may give slightly unstable validation scores
This is close to high-fold cross validation.
Case 2: Same Dataset, K = 1000
Fold Size
100001000=10\frac{10000}{1000}=10100010000=10
Each fold has only 10 samples.
In Each Iteration
•   Training samples = 9,990
•   Testing samples = 10
Repeated 1000 times.
Comment on 1000 Folds
********** 14 **********
--- page 15 ---
Advantages
• Very low bias
• Almost entire dataset used for training
Q7   a. Compare Bagging, Boosting, and Random Forest techniques. Discuss their   [10]
CO-2;
SO-   advantages, limitations, and applications.
2;
BL-
2   Solution:
********** 15 **********
--- page 16 ---
1. Bagging (Bootstrap Aggregating)
Concept
•   Multiple models trained independently on different samples
Key Idea
• Reduce variance
Advantages
• Simple and effective
• Reduces overfitting
Limitations
•   Doesn’t reduce bias
•   All models treated equally
🔹 2. Boosting
Concept
• Models trained sequentially
• Each model focuses on previous errors
Key Idea
• Reduce bias and variance
Advantages
• High accuracy
• Handles complex patterns
Limitations
•   Sensitive to noise
• Can overfit
• Slower training
********** 16 **********
--- page 17 ---
🔹 3. Random Forest
Concept
• Combination of Bagging + Random feature selection
Key Idea
• Reduce variance + improve generalization
🔹 Comparison Table
Feature   Bagging   Boosting   Random Forest
Training   Parallel   Sequential   Parallel
Focus   Variance   Bias + Variance Variance
Overfitting Reduced   Can overfit   Strongly reduced
Noise   Robust   Sensitive   Robust
Example Bagged Trees AdaBoost, GBM Random Forest
Q7   b. What is the meaning of optimal capacity in a machine learning model? How is it   [05]
CO-1;   related to Overfitting and Underfitting?
SO-   Solution:
2;
BL-   The term "optimal capacity" describes a model's ideal complexity, or the point at which it is
2   strong enough to identify underlying patterns in the data without being so complex that it
begins to memorize noise. It basically involves striking a balance between the flexibility of
the model and its capacity for generalization.
Connection to Underfitting and Overfitting:
When the model's capacity is too little, underfitting occurs. It performs poorly on both
training and test sets since it is unable to identify the real patterns in the data.
Overfitting: Occurs when the capacity of the model is very high. It performs worse on unseen
test data because it matches the training data—including noise—too well.
********** 17 **********
--- page 18 ---
Between these extremes is the optimal capacity. The model achieves excellent accuracy on
both training and test sets, demonstrating good generalization.
Q7   c. What is outlier in the dataset? How one can minimize outlier explain with example   [05]
CO-1;
SO-   Solution:
6;   Explanation of outlier-02 marks
BL-
2   How to minimize explain with example-03
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 0ecd4b795853

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_EXTC_7006/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (EXTC)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No.1 is compulsory.
3. Out of remaining questionsa attempt any 4 questions.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figure in brackets on the right hand side indicates full marks.
7. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Define Bias and Variance in a machine learning model. How do they contribute to the total   [05]
SO-   error of the model?
1;
Solution:
BL
Bias and Variance are two fundamental sources of error that determine the performance and
-2
generalization ability of a machine learning model.
Bias:
Bias refers to the error introduced due to simplifying assumptions made by the model while
learning the data. It measures how far the model’s predicted values are from the actual values
on average.
• High bias implies the model is too simple and fails to capture the underlying patterns.
•   It often leads to underfitting.
Variance:
Variance refers to the model’s sensitivity to small fluctuations in the training dataset. It
measures how much the model’s predictions change when trained on different subsets of data.
• High variance implies the model is too complex and captures noise along with
patterns.
•   It often leads to overfitting.
Contribution to Total Error:
The overall prediction error of a model can be decomposed as:
Total Error = Bias² + Variance + Irreducible Error
•   Bias²: Error due to incorrect assumptions
•   Variance: Error due to model instability
•   Irreducible Error: Noise inherent in the data that cannot be eliminated
Intuition:
• A model with high bias and low variance is consistent but inaccurate.
• A model with low bias and high variance is accurate on training data but unstable on
new data.
So we can conclude that
An optimal model minimizes total error by balancing bias and variance, ensuring good
generalization to unseen data.
********** 1 **********
--- page 2 ---
CO-1; SO-   b. Find outlier in following data set using IQR method.   [05]
1; BL   (0.1,1,10,20,25,30,35,40,45,230,500, 50,55,60,65,70,75,80,100,150,175,200)
-4   Solution:
Q1=30
Q3=100
IQR=Q1-Q3=75
Lower Fence=Q1-1.5(IQR)=-75
Upper Fence=Q1+1.5(IQR)= 205
So 230,500 are outlier
CO-2; SO-1;   c. Explain about maximum margin hyper plane in Linear support vector machine.   [05]
BL-2   Solution:
It is a supervised machine learning problem where we try to find a
hyperplane that best separates the two classes. Both the algorithms try to
find the best hyperplane, but the main difference is logistic regression is a
probabilistic approach whereas support vector machine is based on statistical
approaches.
There can be an infinite number of hyperplanes passing through a point
and classifying the two classes perfectly.
SVM does this by finding the maximum margin between the hyperplanes that
means maximum distances between the two classes.
The maximum margin will be
CO-2; SO-2;   d. Discuss the computational complexity of K-Means and Hierarchical Clustering and   [05]
BL-2   its impact on scalability.
Solution:
K_Means and Hierarchical Clustering: 02 M
Comaparison: 03 M
********** 2 **********
--- page 3 ---
K-Means is an iterative algorithm.
• Time Complexity:
O(n × k × t × d)
where:
o n = number of data points
o k = number of clusters
o   t = number of iterations
o d = number of features
• Each iteration assigns points to nearest centroid → O(n × k)
• Updating centroids → O(n)
• Repeated for t iterations
Hierarchical clustering builds a tree (dendrogram).
• Time Complexity:
O(n² log n) (optimized) or up to O(n³) (naive)
• Space Complexity:
O(n²) (distance matrix)
• Computes pairwise distance matrix → O(n²)
• Repeated merging/splitting of clusters
• Updating distances after each merge
K-Means and Hierarchical Clustering are widely used unsupervised learning
algorithms, but they differ significantly in terms of computational complexity and
scalability.
K-Means is an iterative, partition-based clustering algorithm. Its time complexity is
generally O(n × k × t × d), where n is the number of data points, k is the number of
clusters, t is the number of iterations, and d is the number of features. In practice,
since k and t are usually small and fixed, the complexity grows approximately
linearly with the number of data points (n). This makes K-Means computationally
efficient and suitable for large datasets. Additionally, it requires relatively low
memory, as it does not need to store pairwise distances between all data points.
In contrast, Hierarchical Clustering is a tree-based approach that builds a hierarchy of
clusters using either a bottom-up (agglomerative) or top-down (divisive) strategy. Its
time complexity is significantly higher, typically O(n² log n) in optimized
implementations and up to O(n³) in naïve implementations. This is because it requires
computing and updating a full pairwise distance matrix between data points, which
itself requires O(n²) space. As the number of data points increases, both the
computational time and memory requirements grow rapidly.
The difference in computational complexity has a direct impact on scalability. K-
Means is highly scalable and can efficiently handle large datasets with thousands or
even millions of data points. It is commonly used in real-world applications such as
customer segmentation and image processing. On the other hand, Hierarchical
Clustering does not scale well to large datasets due to its high time and space
********** 3 **********
--- page 4 ---
complexity. It is more suitable for smaller datasets where understanding the
hierarchical relationships between clusters is important.
Q2   a.   [10]
CO-2;   In the organization in Mumbai the chief medical officer of the in house dispensary is
SO-   distributed because of the alarming rise in the cases of high blood pressure among
2;   young male employees. A study of high BP men employees revealed that two main
BL-
factors causes high BP. Work related stress and family related stress. The chief
4
medical officer collected the data for a period of five weeks which is given bellow.
From the data set calculate multiple regression equation for employee suffering from
high blood pressure
No of employee suffering from high Blood Pressure   60   52 56 64   68
No of employee suffering from work related stress   47   41 50 42   40
No of employee suffering from family relates stress   22   26 18 13   21
Solution:
Final MLR equation is X1=19.52+0.51X2+0.902X3
Q2   b. Explain how the total error can be minimize by using error back propagation   [10]
CO-2; SO-2;   algorithm in feedforward neural network. Explain with steps.
BL-2   Solution:
Error Backpropagation, short for Backward Propagation of Errors, is a key
algorithm used to train neural networks by minimizing the difference between
predicted and actual outputs. It works by propagating errors backward through the
network, using the chain rule of calculus to compute gradients and then iteratively
updating the weights and biases.   01 Marks
********** 4 **********
--- page 5 ---
Back Propagation plays a critical role in how neural networks improve over time. Here's
why:
1. Efficient Weight Update: It computes the gradient of the loss function with respect
to each weight using the chain rule making it possible to update weights efficiently.
2. Scalability: The Back Propagation algorithm scales well to networks with multiple
layers and complex architectures making deep learning feasible.
3. Automated Learning: With Back Propagation the learning process becomes
automated and the model can adjust itself to optimize its performance.
Steps of error back propagation.
The process involves two main phases: a forward pass, where the input data is passed
through the network to compute the output, and a backward pass, where the gradients are
computed by propagating the error backward through the network.
Forward Pass
In the forward pass, the input data is fed into the network, and operations defined by the
network architecture are performed layer by layer to compute the output. This output is
then used to calculate the loss, which measures the difference between the network's
prediction and the true target values.
Backward Pass
The backward pass starts with the computation of the gradient of the loss function with
respect to the output of the network. Then, by applying the chain rule, the algorithm
calculates the gradient of the loss with respect to each weight by propagating the error
information back from the output layer to the input layer. This process involves the
following steps:
1. Compute the derivative of the loss function with respect to the activations of the
output layer.
2. For each layer, starting from the last hidden layer and moving to the first, compute
the gradients of the loss with respect to the layer's inputs, which are the activations
of the previous layer.
3. Compute the gradients of the loss with respect to the weights by considering the
gradients with respect to the layer's inputs and the derivatives of the layer's
activations with respect to its weights.
These gradients tell us how much a change in each weight would affect the loss, allowing
the optimization algorithm to adjust the weights in a direction that minimizes the loss.
Updating Weights
Once the gradients are computed, the weights are updated typically using a gradient
descent optimization algorithm. The weight update rule is generally of the form:
new_weight = old_weight - learning_rate * gradient
where the learning rate is a hyperparameter that controls the size of the weight updates.
These steps repeated multiple time to minimize the total error generated at the
********** 5 **********
--- page 6 ---
output
Q3   a. Consider the dataset:   [10]
CO-3;
SO-6;
BL-3   Credit Score   Income   Loan Approved
High   High   Yes
High   Medium   Yes
Medium   High   Yes
Low   Medium   No
Low   Low   No
Medium   Low   No
Using ID3 algorithm:
•   Calculate Entropy of target variable
• Compute Information Gain for attributes
Determine the root node
Solution:
1. Entropy of Target Variable
Total = 6
Yes = 3, No = 3
[
H(S) = -0.5\log_2(0.5) - 0.5\log_2(0.5)
]
H(S) = 1
Entropy = 1
🔹 2. Information Gain
➤ Attribute: Credit Score
• High → (2 Yes, 0 No) → Entropy = 0
• Medium → (1 Yes, 1 No) → Entropy = 1
• Low → (0 Yes, 2 No) → Entropy = 0
Weighted entropy:
[
= \frac{2}{6}(0) + \frac{2}{6}(1) + \frac{2}{6}(0) = 0.333
]
********** 6 **********
--- page 7 ---
IG:
[
IG = 1 - 0.333 = 0.667
]
➤ Attribute: Income
• High → (2 Yes, 0 No) → Entropy = 0
• Medium → (1 Yes, 1 No) → Entropy = 1
• Low → (0 Yes, 2 No) → Entropy = 0
Weighted entropy = 0.333
[
IG = 1 - 0.333 = 0.667
]
🔹 3. Root Node
• IG(Credit Score) = 0.667
• IG(Income) = 0.667
Root Node: Either attribute (tie condition)
Q3   b. Explain the concept of Unsupervised Learning and discuss the major challenges faced [10]
CO-1;
SO-1;   while implementing it. Explain tree based unsupervised learning algorithm
BL-2
Solution:
Unsupervised Learning is a type of machine learning in which the model is trained
on data without labeled outputs. The system tries to identify hidden patterns,
structures, or relationships in the data on its own.
Examples
• Customer segmentation in marketing
• Grouping similar documents
•   Clustering users on platforms like Amazon based on behavior
Common Techniques
•   Clustering (e.g., K-Means)
********** 7 **********
--- page 8 ---
•   Association Rule Mining
• Dimensionality Reduction (e.g., PCA)
Challenges of Unsupervised Learning
1. No Labeled Data
• There is no ground truth to guide learning
•   Difficult to verify correctness of results
2. Evaluation Difficulty
• No clear metrics to measure performance
•   Results may vary and be subjective
3. Interpretation of Results
•   Clusters or patterns may be hard to understand
• Requires domain knowledge
4. Choosing Parameters
•   Selecting number of clusters (K in K-Means) is difficult
•   Results depend heavily on parameter choices
5. Sensitivity to Noise
•   Outliers and noisy data can affect results
• May lead to incorrect grouping
6. Scalability Issues
• Large datasets increase computational complexity
Some algorithms become slow
Explain Hierarchical clustering algorithm
Q4   a. In a war situation, military logistics planners need to forecast the daily ammunition   [10]
CO-2;
consumption of artillery units to ensure supply lines can meet demand. The model has
SO-
2;   the relationship between daily number of fire missions and the total shells consumed.
BL-   How this problem can be solved using simple linear regression and gradient descent
2   techniques?
Solution:
Assume a linear relationship between:
•   x: number of fire missions per day
•   y: total shells consumed per day
Simple Linear regression -
y = mx + b,
where y and x are variables,
********** 8 **********
--- page 9 ---
m is the slope, and
b is the y-intercept.
Gradient Descent –
We want to minimize prediction error using Mean Squared Error (MSE).
The steps followed are -
i.   Initialize parameters
ii.   Compute gradients
iii.   Update parameters
Repeat gradient computation and updates until the Cost function converges (minimal change)
or Maximum iterations reached.
Q4   b. For the training example, X=[1,0,1] and Target label t=1, and learning rate is 0.9. The [10]
CO-3;
SO-6;   sigmoid activation function is applied to both the hidden and output layers. The
BL-6   weights are given by,
X1 X2 X3 W14 W15   W24   W25 W34   W35 W46   W56   W04   W05 W06
1   0   1   0.2   -0.3   0.4   0.1   -0.5   0.2   -0.3   -0.2   -0.4   0.2   0.1
Solution:
Solution {each answer is 2 mark)(2*5=10)
4in = 0.2+0-0.5-0.4=-0.7 4out=0.332
5in= -0.3+0+0.2+0.2=0.1 5out=0.525
6in = -0.3*0.332- 0.2*0.525+0.1 =-0.105 6out = 0.474
actual output= 6out = 0.474
********** 9 **********
--- page 10 ---
Q5   a. Explain Random Forest algorithm in detail. Discuss how randomness in data   [10]
CO-3;   sampling and feature selection improves generalization.
SO-
1;   Solution:
BL   Definition
-3
Random Forest is an ensemble learning algorithm that builds multiple decision trees
and combines their outputs to improve accuracy and reduce overfitting.
🔹 Working Steps
1. Bootstrap Sampling (Bagging)
o Random samples are drawn with replacement from dataset.
2. Decision Tree Construction
o Each tree is trained on a different subset.
3. Random Feature Selection
o At each split, only a random subset of features is considered.
4. Aggregation
o Classification → Majority Voting
o Regression → Average
🔹 Role of Randomness
1. Data Sampling (Bagging)
• Each tree sees different data → reduces variance
• Prevents overfitting
2. Feature Selection
• Forces trees to be diverse
• Avoids dominance of strong features
🔹 Advantages
• High accuracy
• Reduces overfitting
********** 10 **********
--- page 11 ---
• Handles large datasets
• Works well with missing values
🔹 Limitations
• Computationally expensive
• Less interpretable
• Slower prediction time
🔹 Applications
• Fraud detection
• Medical diagnosis
• Recommendation systems
• Stock prediction.
Q5   b. Apply K-Means clustering on the following dataset representing Height (cm) and   [10]
CO-2;
SO-2;   Weight (kg): {(150,50),(155,55),(160,60),(170,70),(175,75),(180,80)}
BL-2
Perform clustering for K = 2 and K = 3. Show the steps, update centroids, and
compare the final clusters.
Solution:
Case 1: K = 2
Step 1: Initialize Centroids
Take first two points:
C1 = (150,50), C2 = (155,55)
Step 2: Assign Points (Iteration 1)
• Cluster 1 → (150,50)
• Cluster 2 → (155,55), (160,60), (170,70), (175,75), (180,80)
Step 3: Update Centroids
• C1 = (150,50)
• C2 = average = (168,68)
Iteration 2: Reassign Points
• Cluster 1 → (150,50), (155,55), (160,60)
• Cluster 2 → (170,70), (175,75), (180,80)
Update Centroids
• C1 = (155,55)
• C2 = (175,75)
********** 11 **********
--- page 12 ---
Final Clusters (K=2)
• Cluster 1: {(150,50), (155,55), (160,60)}
• Cluster 2: {(170,70), (175,75), (180,80)}
Case 2: K = 3
Step 1: Initialize Centroids
C1 = (150,50), C2 = (155,55), C3 = (160,60)
Step 2: Assign Points
• Cluster 1 → (150,50)
• Cluster 2 → (155,55)
• Cluster 3 → (160,60), (170,70), (175,75), (180,80)
Step 3: Update Centroids
• C1 = (150,50)
• C2 = (155,55)
• C3 = (171.25, 71.25)
Iteration 2: Reassign Points
• Cluster 1 → (150,50), (155,55)
• Cluster 2 → (160,60)
• Cluster 3 → (170,70), (175,75), (180,80)
Update Centroids
• C1 = (152.5, 52.5)
• C2 = (160,60)
• C3 = (175,75)
Final Clusters (K=3)
• Cluster 1: {(150,50), (155,55)}
• Cluster 2: {(160,60)}
• Cluster 3: {(170,70), (175,75), (180,80)}
Comparison
Aspect   K = 2   K = 3
Clusters   2 groups   3 groups
Grouping   Broad (short vs tall)   More detailed
Interpretation   Simple   More precise
Q6   a. Discuss the situation where polynomial regression is applicable. What is the impact of higher [10]
CO-2; SO-2;   degree polynomial on the final result?
BL-5   Solution:
Polynomial regression is needed when the relationship between the independent
variable and dependent variable is not linear, but follows a curved pattern. In such
cases, a simple linear regression model cannot fit the data accurately. Polynomial
regression extends linear regression by adding higher-order terms such as X2, X3 etc.,
to capture the non-linear trend.
The general form of a polynomial regression model is:
y=b0+b1x1+b2x12+b2x13+…bnx1n
********** 12 **********
--- page 13 ---
Where -
y is the dependent variable,
x1 is the independent variable, and
b0 - bn are the parameters you can optimize
Need for Polymer Regression
•   It helps model curvilinear relationships between variables.
•   It improves the fit when data points do not lie along a straight line.
•   It provides better prediction accuracy than simple linear regression for non-
linear data patterns.
Impact of higher degree polynomial –
1. Better fit to training data
2. Risk of overfitting
Increased variance
One can explain with example
********** 13 **********
--- page 14 ---
Q6   b. Explain K- fold- cross validation for the dataset with 10,000 samples and number   [10]
CO-4; SO-   of fold are 100. Comment if number of folds are 1000 for the same samples.
6;   Solution:
BL- 4   K-Fold Cross Validation
K-Fold Cross Validation is a model evaluation technique used to assess the
performance and generalization ability of a machine learning model.
Working of K-Fold Cross Validation
• The dataset is divided into K equal subsets (folds).
•   In each iteration:
o One fold is used as the testing/validation set.
o Remaining K−1 folds are used for training.
• This process repeats K times, so every sample is used:
o once for testing
o K−1 times for training
The final model performance is the average of all K results.
Case 1: Dataset = 10,000 Samples, K = 100
Given:
•   Total samples = 10,000
• Number of folds = 100
Fold Size
Each fold contains:
10000100=100\frac{10000}{100}=10010010000=100
So each fold has 100 samples.
In Each Iteration
•   Training samples:
10000−100=990010000-100 = 990010000−100=9900
•   Testing samples:
100100100
Thus, for each of the 100 iterations:
•   Train model on 9,900 samples
•   Test model on 100 samples
After 100 runs, average all performance scores.
Comment on 100 Folds
Advantages
• More training data in each run (99% data used for training)
• Lower bias in performance estimate
•   Better model evaluation than small K (like 5 or 10)
Disadvantages
• Computationally expensive (train model 100 times)
• Very small test sets may give slightly unstable validation scores
This is close to high-fold cross validation.
Case 2: Same Dataset, K = 1000
Fold Size
100001000=10\frac{10000}{1000}=10100010000=10
Each fold has only 10 samples.
In Each Iteration
•   Training samples = 9,990
•   Testing samples = 10
Repeated 1000 times.
Comment on 1000 Folds
********** 14 **********
--- page 15 ---
Advantages
• Very low bias
• Almost entire dataset used for training
Q7   a. Compare Bagging, Boosting, and Random Forest techniques. Discuss their   [10]
CO-2;
SO-   advantages, limitations, and applications.
2;
BL-
2   Solution:
********** 15 **********
--- page 16 ---
1. Bagging (Bootstrap Aggregating)
Concept
•   Multiple models trained independently on different samples
Key Idea
• Reduce variance
Advantages
• Simple and effective
• Reduces overfitting
Limitations
•   Doesn’t reduce bias
•   All models treated equally
🔹 2. Boosting
Concept
• Models trained sequentially
• Each model focuses on previous errors
Key Idea
• Reduce bias and variance
Advantages
• High accuracy
• Handles complex patterns
Limitations
•   Sensitive to noise
• Can overfit
• Slower training
********** 16 **********
--- page 17 ---
🔹 3. Random Forest
Concept
• Combination of Bagging + Random feature selection
Key Idea
• Reduce variance + improve generalization
🔹 Comparison Table
Feature   Bagging   Boosting   Random Forest
Training   Parallel   Sequential   Parallel
Focus   Variance   Bias + Variance Variance
Overfitting Reduced   Can overfit   Strongly reduced
Noise   Robust   Sensitive   Robust
Example Bagged Trees AdaBoost, GBM Random Forest
Q7   b. What is the meaning of optimal capacity in a machine learning model? How is it   [05]
CO-1;   related to Overfitting and Underfitting?
SO-   Solution:
2;
BL-   The term "optimal capacity" describes a model's ideal complexity, or the point at which it is
2   strong enough to identify underlying patterns in the data without being so complex that it
begins to memorize noise. It basically involves striking a balance between the flexibility of
the model and its capacity for generalization.
Connection to Underfitting and Overfitting:
When the model's capacity is too little, underfitting occurs. It performs poorly on both
training and test sets since it is unable to identify the real patterns in the data.
Overfitting: Occurs when the capacity of the model is very high. It performs worse on unseen
test data because it matches the training data—including noise—too well.
********** 17 **********
--- page 18 ---
Between these extremes is the optimal capacity. The model achieves excellent accuracy on
both training and test sets, demonstrating good generalization.
Q7   c. What is outlier in the dataset? How one can minimize outlier explain with example   [05]
CO-1;
SO-   Solution:
6;   Explanation of outlier-02 marks
BL-
2   How to minimize explain with example-03
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 99ba4cbafcae

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_Computer_7047/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (EXTC)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No.1 is compulsory.
3. Out of remaining questionsa attempt any 4 questions.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figure in brackets on the right hand side indicates full marks.
7. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Define Bias and Variance in a machine learning model. How do they contribute to the total   [05]
SO-   error of the model?
1;
Solution:
BL
Bias and Variance are two fundamental sources of error that determine the performance and
-2
generalization ability of a machine learning model.
Bias:
Bias refers to the error introduced due to simplifying assumptions made by the model while
learning the data. It measures how far the model’s predicted values are from the actual values
on average.
• High bias implies the model is too simple and fails to capture the underlying patterns.
•   It often leads to underfitting.
Variance:
Variance refers to the model’s sensitivity to small fluctuations in the training dataset. It
measures how much the model’s predictions change when trained on different subsets of data.
• High variance implies the model is too complex and captures noise along with
patterns.
•   It often leads to overfitting.
Contribution to Total Error:
The overall prediction error of a model can be decomposed as:
Total Error = Bias² + Variance + Irreducible Error
•   Bias²: Error due to incorrect assumptions
•   Variance: Error due to model instability
•   Irreducible Error: Noise inherent in the data that cannot be eliminated
Intuition:
• A model with high bias and low variance is consistent but inaccurate.
• A model with low bias and high variance is accurate on training data but unstable on
new data.
So we can conclude that
An optimal model minimizes total error by balancing bias and variance, ensuring good
generalization to unseen data.
********** 1 **********
--- page 2 ---
CO-1; SO-   b. Find outlier in following data set using IQR method.   [05]
1; BL   (0.1,1,10,20,25,30,35,40,45,230,500, 50,55,60,65,70,75,80,100,150,175,200)
-4   Solution:
Q1=30
Q3=100
IQR=Q1-Q3=75
Lower Fence=Q1-1.5(IQR)=-75
Upper Fence=Q1+1.5(IQR)= 205
So 230,500 are outlier
CO-2; SO-1;   c. Explain about maximum margin hyper plane in Linear support vector machine.   [05]
BL-2   Solution:
It is a supervised machine learning problem where we try to find a
hyperplane that best separates the two classes. Both the algorithms try to
find the best hyperplane, but the main difference is logistic regression is a
probabilistic approach whereas support vector machine is based on statistical
approaches.
There can be an infinite number of hyperplanes passing through a point
and classifying the two classes perfectly.
SVM does this by finding the maximum margin between the hyperplanes that
means maximum distances between the two classes.
The maximum margin will be
CO-2; SO-2;   d. Discuss the computational complexity of K-Means and Hierarchical Clustering and   [05]
BL-2   its impact on scalability.
Solution:
K_Means and Hierarchical Clustering: 02 M
Comaparison: 03 M
********** 2 **********
--- page 3 ---
K-Means is an iterative algorithm.
• Time Complexity:
O(n × k × t × d)
where:
o n = number of data points
o k = number of clusters
o   t = number of iterations
o d = number of features
• Each iteration assigns points to nearest centroid → O(n × k)
• Updating centroids → O(n)
• Repeated for t iterations
Hierarchical clustering builds a tree (dendrogram).
• Time Complexity:
O(n² log n) (optimized) or up to O(n³) (naive)
• Space Complexity:
O(n²) (distance matrix)
• Computes pairwise distance matrix → O(n²)
• Repeated merging/splitting of clusters
• Updating distances after each merge
K-Means and Hierarchical Clustering are widely used unsupervised learning
algorithms, but they differ significantly in terms of computational complexity and
scalability.
K-Means is an iterative, partition-based clustering algorithm. Its time complexity is
generally O(n × k × t × d), where n is the number of data points, k is the number of
clusters, t is the number of iterations, and d is the number of features. In practice,
since k and t are usually small and fixed, the complexity grows approximately
linearly with the number of data points (n). This makes K-Means computationally
efficient and suitable for large datasets. Additionally, it requires relatively low
memory, as it does not need to store pairwise distances between all data points.
In contrast, Hierarchical Clustering is a tree-based approach that builds a hierarchy of
clusters using either a bottom-up (agglomerative) or top-down (divisive) strategy. Its
time complexity is significantly higher, typically O(n² log n) in optimized
implementations and up to O(n³) in naïve implementations. This is because it requires
computing and updating a full pairwise distance matrix between data points, which
itself requires O(n²) space. As the number of data points increases, both the
computational time and memory requirements grow rapidly.
The difference in computational complexity has a direct impact on scalability. K-
Means is highly scalable and can efficiently handle large datasets with thousands or
even millions of data points. It is commonly used in real-world applications such as
customer segmentation and image processing. On the other hand, Hierarchical
Clustering does not scale well to large datasets due to its high time and space
********** 3 **********
--- page 4 ---
complexity. It is more suitable for smaller datasets where understanding the
hierarchical relationships between clusters is important.
Q2   a.   [10]
CO-2;   In the organization in Mumbai the chief medical officer of the in house dispensary is
SO-   distributed because of the alarming rise in the cases of high blood pressure among
2;   young male employees. A study of high BP men employees revealed that two main
BL-
factors causes high BP. Work related stress and family related stress. The chief
4
medical officer collected the data for a period of five weeks which is given bellow.
From the data set calculate multiple regression equation for employee suffering from
high blood pressure
No of employee suffering from high Blood Pressure   60   52 56 64   68
No of employee suffering from work related stress   47   41 50 42   40
No of employee suffering from family relates stress   22   26 18 13   21
Solution:
Final MLR equation is X1=19.52+0.51X2+0.902X3
Q2   b. Explain how the total error can be minimize by using error back propagation   [10]
CO-2; SO-2;   algorithm in feedforward neural network. Explain with steps.
BL-2   Solution:
Error Backpropagation, short for Backward Propagation of Errors, is a key
algorithm used to train neural networks by minimizing the difference between
predicted and actual outputs. It works by propagating errors backward through the
network, using the chain rule of calculus to compute gradients and then iteratively
updating the weights and biases.   01 Marks
********** 4 **********
--- page 5 ---
Back Propagation plays a critical role in how neural networks improve over time. Here's
why:
1. Efficient Weight Update: It computes the gradient of the loss function with respect
to each weight using the chain rule making it possible to update weights efficiently.
2. Scalability: The Back Propagation algorithm scales well to networks with multiple
layers and complex architectures making deep learning feasible.
3. Automated Learning: With Back Propagation the learning process becomes
automated and the model can adjust itself to optimize its performance.
Steps of error back propagation.
The process involves two main phases: a forward pass, where the input data is passed
through the network to compute the output, and a backward pass, where the gradients are
computed by propagating the error backward through the network.
Forward Pass
In the forward pass, the input data is fed into the network, and operations defined by the
network architecture are performed layer by layer to compute the output. This output is
then used to calculate the loss, which measures the difference between the network's
prediction and the true target values.
Backward Pass
The backward pass starts with the computation of the gradient of the loss function with
respect to the output of the network. Then, by applying the chain rule, the algorithm
calculates the gradient of the loss with respect to each weight by propagating the error
information back from the output layer to the input layer. This process involves the
following steps:
1. Compute the derivative of the loss function with respect to the activations of the
output layer.
2. For each layer, starting from the last hidden layer and moving to the first, compute
the gradients of the loss with respect to the layer's inputs, which are the activations
of the previous layer.
3. Compute the gradients of the loss with respect to the weights by considering the
gradients with respect to the layer's inputs and the derivatives of the layer's
activations with respect to its weights.
These gradients tell us how much a change in each weight would affect the loss, allowing
the optimization algorithm to adjust the weights in a direction that minimizes the loss.
Updating Weights
Once the gradients are computed, the weights are updated typically using a gradient
descent optimization algorithm. The weight update rule is generally of the form:
new_weight = old_weight - learning_rate * gradient
where the learning rate is a hyperparameter that controls the size of the weight updates.
These steps repeated multiple time to minimize the total error generated at the
********** 5 **********
--- page 6 ---
output
Q3   a. Consider the dataset:   [10]
CO-3;
SO-6;
BL-3   Credit Score   Income   Loan Approved
High   High   Yes
High   Medium   Yes
Medium   High   Yes
Low   Medium   No
Low   Low   No
Medium   Low   No
Using ID3 algorithm:
•   Calculate Entropy of target variable
• Compute Information Gain for attributes
Determine the root node
Solution:
1. Entropy of Target Variable
Total = 6
Yes = 3, No = 3
[
H(S) = -0.5\log_2(0.5) - 0.5\log_2(0.5)
]
H(S) = 1
Entropy = 1
🔹 2. Information Gain
➤ Attribute: Credit Score
• High → (2 Yes, 0 No) → Entropy = 0
• Medium → (1 Yes, 1 No) → Entropy = 1
• Low → (0 Yes, 2 No) → Entropy = 0
Weighted entropy:
[
= \frac{2}{6}(0) + \frac{2}{6}(1) + \frac{2}{6}(0) = 0.333
]
********** 6 **********
--- page 7 ---
IG:
[
IG = 1 - 0.333 = 0.667
]
➤ Attribute: Income
• High → (2 Yes, 0 No) → Entropy = 0
• Medium → (1 Yes, 1 No) → Entropy = 1
• Low → (0 Yes, 2 No) → Entropy = 0
Weighted entropy = 0.333
[
IG = 1 - 0.333 = 0.667
]
🔹 3. Root Node
• IG(Credit Score) = 0.667
• IG(Income) = 0.667
Root Node: Either attribute (tie condition)
Q3   b. Explain the concept of Unsupervised Learning and discuss the major challenges faced [10]
CO-1;
SO-1;   while implementing it. Explain tree based unsupervised learning algorithm
BL-2
Solution:
Unsupervised Learning is a type of machine learning in which the model is trained
on data without labeled outputs. The system tries to identify hidden patterns,
structures, or relationships in the data on its own.
Examples
• Customer segmentation in marketing
• Grouping similar documents
•   Clustering users on platforms like Amazon based on behavior
Common Techniques
•   Clustering (e.g., K-Means)
********** 7 **********
--- page 8 ---
•   Association Rule Mining
• Dimensionality Reduction (e.g., PCA)
Challenges of Unsupervised Learning
1. No Labeled Data
• There is no ground truth to guide learning
•   Difficult to verify correctness of results
2. Evaluation Difficulty
• No clear metrics to measure performance
•   Results may vary and be subjective
3. Interpretation of Results
•   Clusters or patterns may be hard to understand
• Requires domain knowledge
4. Choosing Parameters
•   Selecting number of clusters (K in K-Means) is difficult
•   Results depend heavily on parameter choices
5. Sensitivity to Noise
•   Outliers and noisy data can affect results
• May lead to incorrect grouping
6. Scalability Issues
• Large datasets increase computational complexity
Some algorithms become slow
Explain Hierarchical clustering algorithm
Q4   a. In a war situation, military logistics planners need to forecast the daily ammunition   [10]
CO-2;
consumption of artillery units to ensure supply lines can meet demand. The model has
SO-
2;   the relationship between daily number of fire missions and the total shells consumed.
BL-   How this problem can be solved using simple linear regression and gradient descent
2   techniques?
Solution:
Assume a linear relationship between:
•   x: number of fire missions per day
•   y: total shells consumed per day
Simple Linear regression -
y = mx + b,
where y and x are variables,
********** 8 **********
--- page 9 ---
m is the slope, and
b is the y-intercept.
Gradient Descent –
We want to minimize prediction error using Mean Squared Error (MSE).
The steps followed are -
i.   Initialize parameters
ii.   Compute gradients
iii.   Update parameters
Repeat gradient computation and updates until the Cost function converges (minimal change)
or Maximum iterations reached.
Q4   b. For the training example, X=[1,0,1] and Target label t=1, and learning rate is 0.9. The [10]
CO-3;
SO-6;   sigmoid activation function is applied to both the hidden and output layers. The
BL-6   weights are given by,
X1 X2 X3 W14 W15   W24   W25 W34   W35 W46   W56   W04   W05 W06
1   0   1   0.2   -0.3   0.4   0.1   -0.5   0.2   -0.3   -0.2   -0.4   0.2   0.1
Solution:
Solution {each answer is 2 mark)(2*5=10)
4in = 0.2+0-0.5-0.4=-0.7 4out=0.332
5in= -0.3+0+0.2+0.2=0.1 5out=0.525
6in = -0.3*0.332- 0.2*0.525+0.1 =-0.105 6out = 0.474
actual output= 6out = 0.474
********** 9 **********
--- page 10 ---
Q5   a. Explain Random Forest algorithm in detail. Discuss how randomness in data   [10]
CO-3;   sampling and feature selection improves generalization.
SO-
1;   Solution:
BL   Definition
-3
Random Forest is an ensemble learning algorithm that builds multiple decision trees
and combines their outputs to improve accuracy and reduce overfitting.
🔹 Working Steps
1. Bootstrap Sampling (Bagging)
o Random samples are drawn with replacement from dataset.
2. Decision Tree Construction
o Each tree is trained on a different subset.
3. Random Feature Selection
o At each split, only a random subset of features is considered.
4. Aggregation
o Classification → Majority Voting
o Regression → Average
🔹 Role of Randomness
1. Data Sampling (Bagging)
• Each tree sees different data → reduces variance
• Prevents overfitting
2. Feature Selection
• Forces trees to be diverse
• Avoids dominance of strong features
🔹 Advantages
• High accuracy
• Reduces overfitting
********** 10 **********
--- page 11 ---
• Handles large datasets
• Works well with missing values
🔹 Limitations
• Computationally expensive
• Less interpretable
• Slower prediction time
🔹 Applications
• Fraud detection
• Medical diagnosis
• Recommendation systems
• Stock prediction.
Q5   b. Apply K-Means clustering on the following dataset representing Height (cm) and   [10]
CO-2;
SO-2;   Weight (kg): {(150,50),(155,55),(160,60),(170,70),(175,75),(180,80)}
BL-2
Perform clustering for K = 2 and K = 3. Show the steps, update centroids, and
compare the final clusters.
Solution:
Case 1: K = 2
Step 1: Initialize Centroids
Take first two points:
C1 = (150,50), C2 = (155,55)
Step 2: Assign Points (Iteration 1)
• Cluster 1 → (150,50)
• Cluster 2 → (155,55), (160,60), (170,70), (175,75), (180,80)
Step 3: Update Centroids
• C1 = (150,50)
• C2 = average = (168,68)
Iteration 2: Reassign Points
• Cluster 1 → (150,50), (155,55), (160,60)
• Cluster 2 → (170,70), (175,75), (180,80)
Update Centroids
• C1 = (155,55)
• C2 = (175,75)
********** 11 **********
--- page 12 ---
Final Clusters (K=2)
• Cluster 1: {(150,50), (155,55), (160,60)}
• Cluster 2: {(170,70), (175,75), (180,80)}
Case 2: K = 3
Step 1: Initialize Centroids
C1 = (150,50), C2 = (155,55), C3 = (160,60)
Step 2: Assign Points
• Cluster 1 → (150,50)
• Cluster 2 → (155,55)
• Cluster 3 → (160,60), (170,70), (175,75), (180,80)
Step 3: Update Centroids
• C1 = (150,50)
• C2 = (155,55)
• C3 = (171.25, 71.25)
Iteration 2: Reassign Points
• Cluster 1 → (150,50), (155,55)
• Cluster 2 → (160,60)
• Cluster 3 → (170,70), (175,75), (180,80)
Update Centroids
• C1 = (152.5, 52.5)
• C2 = (160,60)
• C3 = (175,75)
Final Clusters (K=3)
• Cluster 1: {(150,50), (155,55)}
• Cluster 2: {(160,60)}
• Cluster 3: {(170,70), (175,75), (180,80)}
Comparison
Aspect   K = 2   K = 3
Clusters   2 groups   3 groups
Grouping   Broad (short vs tall)   More detailed
Interpretation   Simple   More precise
Q6   a. Discuss the situation where polynomial regression is applicable. What is the impact of higher [10]
CO-2; SO-2;   degree polynomial on the final result?
BL-5   Solution:
Polynomial regression is needed when the relationship between the independent
variable and dependent variable is not linear, but follows a curved pattern. In such
cases, a simple linear regression model cannot fit the data accurately. Polynomial
regression extends linear regression by adding higher-order terms such as X2, X3 etc.,
to capture the non-linear trend.
The general form of a polynomial regression model is:
y=b0+b1x1+b2x12+b2x13+…bnx1n
********** 12 **********
--- page 13 ---
Where -
y is the dependent variable,
x1 is the independent variable, and
b0 - bn are the parameters you can optimize
Need for Polymer Regression
•   It helps model curvilinear relationships between variables.
•   It improves the fit when data points do not lie along a straight line.
•   It provides better prediction accuracy than simple linear regression for non-
linear data patterns.
Impact of higher degree polynomial –
1. Better fit to training data
2. Risk of overfitting
Increased variance
One can explain with example
********** 13 **********
--- page 14 ---
Q6   b. Explain K- fold- cross validation for the dataset with 10,000 samples and number   [10]
CO-4; SO-   of fold are 100. Comment if number of folds are 1000 for the same samples.
6;   Solution:
BL- 4   K-Fold Cross Validation
K-Fold Cross Validation is a model evaluation technique used to assess the
performance and generalization ability of a machine learning model.
Working of K-Fold Cross Validation
• The dataset is divided into K equal subsets (folds).
•   In each iteration:
o One fold is used as the testing/validation set.
o Remaining K−1 folds are used for training.
• This process repeats K times, so every sample is used:
o once for testing
o K−1 times for training
The final model performance is the average of all K results.
Case 1: Dataset = 10,000 Samples, K = 100
Given:
•   Total samples = 10,000
• Number of folds = 100
Fold Size
Each fold contains:
10000100=100\frac{10000}{100}=10010010000=100
So each fold has 100 samples.
In Each Iteration
•   Training samples:
10000−100=990010000-100 = 990010000−100=9900
•   Testing samples:
100100100
Thus, for each of the 100 iterations:
•   Train model on 9,900 samples
•   Test model on 100 samples
After 100 runs, average all performance scores.
Comment on 100 Folds
Advantages
• More training data in each run (99% data used for training)
• Lower bias in performance estimate
•   Better model evaluation than small K (like 5 or 10)
Disadvantages
• Computationally expensive (train model 100 times)
• Very small test sets may give slightly unstable validation scores
This is close to high-fold cross validation.
Case 2: Same Dataset, K = 1000
Fold Size
100001000=10\frac{10000}{1000}=10100010000=10
Each fold has only 10 samples.
In Each Iteration
•   Training samples = 9,990
•   Testing samples = 10
Repeated 1000 times.
Comment on 1000 Folds
********** 14 **********
--- page 15 ---
Advantages
• Very low bias
• Almost entire dataset used for training
Q7   a. Compare Bagging, Boosting, and Random Forest techniques. Discuss their   [10]
CO-2;
SO-   advantages, limitations, and applications.
2;
BL-
2   Solution:
********** 15 **********
--- page 16 ---
1. Bagging (Bootstrap Aggregating)
Concept
•   Multiple models trained independently on different samples
Key Idea
• Reduce variance
Advantages
• Simple and effective
• Reduces overfitting
Limitations
•   Doesn’t reduce bias
•   All models treated equally
🔹 2. Boosting
Concept
• Models trained sequentially
• Each model focuses on previous errors
Key Idea
• Reduce bias and variance
Advantages
• High accuracy
• Handles complex patterns
Limitations
•   Sensitive to noise
• Can overfit
• Slower training
********** 16 **********
--- page 17 ---
🔹 3. Random Forest
Concept
• Combination of Bagging + Random feature selection
Key Idea
• Reduce variance + improve generalization
🔹 Comparison Table
Feature   Bagging   Boosting   Random Forest
Training   Parallel   Sequential   Parallel
Focus   Variance   Bias + Variance Variance
Overfitting Reduced   Can overfit   Strongly reduced
Noise   Robust   Sensitive   Robust
Example Bagged Trees AdaBoost, GBM Random Forest
Q7   b. What is the meaning of optimal capacity in a machine learning model? How is it   [05]
CO-1;   related to Overfitting and Underfitting?
SO-   Solution:
2;
BL-   The term "optimal capacity" describes a model's ideal complexity, or the point at which it is
2   strong enough to identify underlying patterns in the data without being so complex that it
begins to memorize noise. It basically involves striking a balance between the flexibility of
the model and its capacity for generalization.
Connection to Underfitting and Overfitting:
When the model's capacity is too little, underfitting occurs. It performs poorly on both
training and test sets since it is unable to identify the real patterns in the data.
Overfitting: Occurs when the capacity of the model is very high. It performs worse on unseen
test data because it matches the training data—including noise—too well.
********** 17 **********
--- page 18 ---
Between these extremes is the optimal capacity. The model achieves excellent accuracy on
both training and test sets, demonstrating good generalization.
Q7   c. What is outlier in the dataset? How one can minimize outlier explain with example   [05]
CO-1;
SO-   Solution:
6;   Explanation of outlier-02 marks
BL-
2   How to minimize explain with example-03
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 371ed8550bc4

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CS_7055/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: mixed (10 pages), mean OCR confidence 85.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CS)/B. Tech (CSBS)
Year: III / IV/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No.1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. Answer to each question to be started on a fresh page
6. Assume suitable data if necessary
7. Figures in bracket on the right hand side indicate full marks
Q1   Answer briefly:   [20]
a) P1 = (1,1) , P2 = (1.5,2) , P3 = (3,4) , P4 = (5,7) and P5 = (3.5,5). Using K Means
clustering find 2 clusters. Assume initial clusters as P1 and P2.
Ans:
2+2 Marks for distance calculation and 1 mark for final clusters.
Step 1: Initialization
initial centroids as:
C₁ = P₁ = (1, 1)
C₂ = P₂ = (1.5, 2)
Step 2: Compute Euclidean Distances
We’ll calculate the distance of each point from both centroids.
Formula:
𝑑= √(𝑥2 −𝑥1)2 + (𝑦2 −𝑦1)2
Point Coordinates   d(P, C₁)   [5]
P₁   (1, 1)   0
P₂   (1.5, 2)   √((1.5−1)² + (2−1)²) = √(0.25 + 1) = 1.118
P₃   (3, 4)   √((3−1)² + (4−1)²) = √(4 + 9) = 3.606
P₄   (5, 7)   √((5−1)² + (7−1)²) = √(16 + 36) = 7.211
P₅   (3.5, 5)   √((3.5−1)² + (5−1)²) = √(6.25 + 16) = 4.719
Distance from P2:
Point Coordinates   d(P, C₂)
P₁   (1, 1)   1.118
P₂   (1.5, 2)   0
P₃   (3, 4)   √((3−1.5)² + (4−2)²) = √(2.25 + 4) = 2.5
********** 1 **********
--- page 2 ---
P₄   (5, 7)   √((5−1.5)² + (7−2)²) = √(12.25 + 25) = 6.103
P₅   (3.5, 5)   √((3.5−1.5)² + (5−2)²) = √(4 + 9) = 3.606
Assigning points to the nearest cluster.
Point d(P, C₁) d(P, C₂) Assigned Cluster
P₁   0   1.118   C₁
P₂   1.118   0   C₂
P₃   3.606   2.5   C₂
P₄   7.211   6.103   C₂
P₅   4.719   3.606   C₂
Cluster Assignment (Iteration 1):
•   Cluster 1 (C₁): { P₁ }
•   Cluster 2 (C₂): { P₂, P₃, P₄, P₅ }
How is variance reduction achieved in Random Forest? What is OOB concept in Random
forest?
3 marks for part a and 2 marks for OOB concept.
Ans: Random Forest is an ensemble of decision trees built using two key ideas:
1. Bootstrap Sampling (Bagging)
2. Feature Randomness (Random Subspace Method)
(a) Bootstrap Aggregation (Bagging)
• Each tree is trained on a different random subset of the data (sampled with
replacement).
•   Since each tree sees a slightly different dataset, their errors are uncorrelated.
•   Final prediction is made by averaging (for regression) or voting (for [5]
classification)   over   all   trees.
Averaging multiple uncorrelated models reduces variance without increasing bias.
(b) Random Feature Selection
• At each split in a tree, Random Forest randomly selects a subset of features
instead of using all features.
•   This decorrelates the trees further, because different trees may choose different
predictors.
Variance reduction is achieved through:
1. Bagging (Bootstrap sampling) — different data subsets
2. Random feature selection — different predictors per split
3. Averaging/Voting — combining results to smooth out fluctuations
c) Why do we use Polynomial Regression instead of Linear Regression in some cases?
Explain with an example.
3 marks for first part, 2 marks for example and explanation.
Limitation of Linear Regression
Linear Regression assumes a linear relationship between the independent variable 𝑋and
the dependent variable 𝑌.   [5]
That is:
𝑌= 𝛽0 + 𝛽1𝑋+ 𝜀
However, in many real-world problems, the data shows a non-linear pattern — the
change in 𝑌is not proportional to the change in 𝑋.
In such cases, a straight line cannot capture the underlying trend accurately.
********** 2 **********
--- page 3 ---
Polynomial Regression – The Solution
Polynomial Regression is an extension of Linear Regression that allows modeling
curved relationships between 𝑋and 𝑌.
It adds higher-degree polynomial terms of the predictor variable.
The general form is:
𝑌= 𝛽0 + 𝛽1𝑋+ 𝛽2𝑋2 + 𝛽3𝑋3 + ⋯+ 𝛽𝑛𝑋𝑛+ 𝜀
This still uses linear coefficients 𝛽0, 𝛽1, … , 𝛽𝑛, so it’s called polynomial regression, but
it is still a type of linear model in parameters.
When to Use Polynomial Regression
Use Polynomial Regression when:
• The relationship between 𝑋and 𝑌is non-linear but smooth (e.g., curved,
parabolic).
• The residuals from a linear regression show a pattern, suggesting underfitting.
• You want a better fit without switching to complex models like neural networks.
d)
What is absolute scaling method and Min-Max scaling method? Explain the disadvantage
of using absolute scaling method with an example.
Ans:
3 marks for first part, 2 Marks for second part
Absolute Scaling divides by the maximum but ignores the minimum → can produce
negative or biased results.   [5]
Min–Max Scaling adjusts based on both min and max, preferred and robust for most
ML preprocessing tasks.
Disadvantage: The main disadvantage is that the technique is sensitive to outliers. Like
consider the feature ‘square feet’, if 99% of the houses have square feet area of less than
1000, and even if just 1 house has a square feet area of 20,000, then all those other house
values will be scaled down to less than 0.05.
Q2   [20]
a)   Explain the concept of One-Hot Encoding used for handling categorical variables in
machine learning. How can One-Hot Encoding lead to multicollinearity in models such
as Linear or Logistic Regression? Illustrate your answer with a suitable example and
describe how this issue can be resolved.
Ans:
3 marks first part, 2 marks second part and 5 marks third part.
One-Hot Encoding is a technique used to convert categorical variables (non-numeric
data such as gender, color, type, etc.) into a numerical format that can be used by   [10]
algorithms.
Many ML algorithms (like Linear Regression, Logistic Regression, SVM, etc.) require
numerical inputs. One-Hot Encoding converts a categorical feature with n unique
categories into n binary (0/1) variables, each representing the presence (1) or absence
(0) of one category.
Multicollinearity occurs when one or more independent variables in a regression model
are highly correlated, meaning one can be predicted linearly from others.
b)   Explain the activation functions in neural networks Sigmoid, ReLU, and Tanh.
For each function, write its mathematical expression, specify its output range, and   [10]
describe when and why it is used in neural network models.
********** 3 **********
--- page 4 ---
Ans: Mathematical expression=4 Marks+ 6 marks for range and when and why used
Activation functions introduce non-linearity into neural networks, enabling them to
learn complex relationships between inputs and outputs.
They determine how the weighted sum of inputs is transformed into the output of a
neuron.
Q3   [20]
a). A teacher records marks of two sections of a class in the final exam:
Section A:
40,50,52,55,58,60,62,65,70,80
Section B:
35,38,40,45,50,52,55,60,65,90
1. Draw box plots for both sections.
2. Identify which section performed better overall. Compare their median and IQR
3. Determine which dataset is more skewed, and explain which type of skewness it
is.
4. State your Analysis
Ans:
2.5 each Answer.
Section A   [10]
Ordered Data: 40, 50, 52, 55, 58, 60, 62, 65, 70, 80
n = 10
• Minimum (Min): 40
• Maximum (Max): 80
• Median (Q2): Average of 5th & 6th = (58 + 60) / 2 = 59
• Q1 (25th percentile): Median of lower half (40, 50, 52, 55, 58) → 52
• Q3 (75th percentile): Median of upper half (60, 62, 65, 70, 80) → 65
IQR = 𝑄3 −𝑄1 = 65 −52 = 13
Section B
Ordered Data: 35, 38, 40, 45, 50, 52, 55, 60, 65, 90
n = 10
• Min: 35
• Max: 90
• Median (Q2): (50 + 52) / 2 = 51
********** 4 **********
--- page 5 ---
• Q1: Median of (35, 38, 40, 45, 50) → 40
• Q3: Median of (52, 55, 60, 65, 90) → 60
IQR = 𝑄3 −𝑄1 = 60 −40 = 20
b)
The professor wishes to build a predictive model using Linear Regression to understand
and quantify the relationship between hours of study and exam performance.
Hours of Study   Exam Score
1   52
2   56
3   61
4   66
5   70
6   74
7   78
8   85
[10]
1. Plot a scatter diagram to visualize the relationship between hours studied and
exam scores.
2. Calculate the R-squared (R²) value to measure how well the model fits the data.
3. Use the model to predict the expected exam score if a student studies for 10
hours.
Intercept=47.28   2 Marks
Slope=4.548   2 marks
R square=0.799   3 marks
10 hours of study=92.78 3 marks
Q4   [20]
a)   Neural network small problem. Three inputs 0.7,0.4 and 0.3 is given as inputs, with the
weights 0.2,0.3 and -0.2 respectively. And bias value is =0.25. Find the output using
sigmoid activation function. Draw the neat neural network with all the parameters.
[10]
Ans:5 Marks each
b)   Agglomerative algorithm with the following data and plot a Dendogram using single
link approach.   [10]
********** 5 **********
--- page 6 ---
1. Compute the Euclidean Distance Matrix between all customers. 2 marks
2. Apply the Agglomerative Hierarchical Clustering (Single Linkage) method
manually, draw the dendogram 7 marks
3. Identify which customers form clusters first. 1 marks
Customer Income Spending Score
C1   25   30
C2   28   35
C3   70   65
C4   72   72
C5   75   80
Q5   [20]
a)   Explain the concept of Dimensionality Reduction in Machine Learning. Why is it
necessary? Discuss the Principal Component Analysis (PCA) technique for
dimensionality reduction. Describe the mathematical steps involved in PCA and explain
how it helps in feature extraction.
Ans:
2 marks, 3+ 3 marks discuss and describe, 2 marks for feature extraction part
Dimensionality Reduction is the process of reducing the number of input variables or
features in a dataset while retaining the most important information.
In simple terms, it transforms a high-dimensional dataset (with many variables) into a
lower-dimensional one (with fewer variables) without losing significant patterns or
relationships in the data.
Why Dimensionality Reduction is Necessary
1. Removes Redundant Features:   [10]
Many features may be correlated or carry overlapping information. Reduction
eliminates redundancy.
2. Reduces Overfitting:
Fewer features lead to simpler models that generalize better.
3. Improves Computational Efficiency:
Reducing dimensions decreases storage, training time, and computational cost.
4. Better Visualization:
Data with 2 or 3 dimensions can be plotted for easier interpretation.
5. Noise Reduction:
It filters out irrelevant or less important features, enhancing model performance.
Steps of Principal Component Analysis (PCA):
1. Standardize the data
2. Compute the covariance matrix
********** 6 **********
--- page 7 ---
3. Calculate eigenvalues and eigenvectors
4. Sort eigenvalues in descending order
5. Select the top k eigenvectors (principal components)
6. Form the projection matrix using selected eigenvectors
7. Transform the original data onto the new subspace
b) A hospital has developed a machine learning model to classify patients into three
categories based on their medical test results: Class A: Healthy, Class B: At Risk, Class
C: Diseased. Find Precision, Recall and Accuracy for all 3 classes from the following
Confusion Matrix.
Actual/Predicated Healthy At Risk   Diseased
Healthy   25   3   2
At Risk   4   20   6
Diseased   1   5   24
Formula- 4 marks+ 6 marks
[10]
Q6   [20]
a)   Explain the working of a Support Vector Machine (SVM) classifier for linearly
separable data with the following points wrt SVM algorithm. i)The objective function of
SVM ii)The concept of margin maximization iii) The role of support vectors iv) A neat
diagram showing separating hyperplane and margins.
Ans:
2.5 each Marks.   [10]
A Support Vector Machine (SVM) is a supervised learning algorithm used for
classification and regression tasks.
For linearly separable data, SVM aims to find the best possible decision boundary
(hyperplane) that separates data points of different classes with the maximum margin.
B
A company wants to predict whether a new email (X) is Spam or Not Spam using a
Naïve Bayes Classifier based on the presence of certain keywords.
A new email (X) has the following features:
Offer = Yes, Free = Yes, Click = No
Email
Offer Free Click Label
ID
1   Yes   Yes   Yes   Spam
********** 7 **********
--- page 8 ---
2   Yes   No   Yes   Spam
Not
3   No   Yes No
Spam
Not
4   Yes   No   No
Spam
5   No   Yes   Yes   Spam
Not
6   No   No   No
Spam
Marks: 4 marks + 4 marks+ 2 Marks
For spam
For Not spam:
It is spam.
Q7   [20]
a)   Differentiate between Bagging and Boosting in terms of sampling method, model
training, and error handling. What is the intuition behind Boosting? How does it convert
weak learners into a strong learner?
[10]
Ans: 6 marks+ 2 Marks+ 2Marks
********** 8 **********
--- page 9 ---
A telecom company wants to predict whether a customer will churn (leave the service)
b)   or stay, based on certain attributes.
The dataset is shown below: For the given dataset, find which is the suitable root node
using ID3 decision Tree algorithm.
[10]
Customer
Payment
Customer Contract Type   Support   Churn
Method
Calls
Month-to-
1   Online   High   Yes
Month
Month-to-
2   Online   Low   No
Month
3   One Year   Offline   Low   No
4   Two Year   Offline   Low   No
Month-to-
5   Offline   High   Yes
Month
6   One Year   Online   Medium   No
7   Two Year   Online   Low   No
Month-to-
8   Online   Medium   Yes
Month
9   One Year   Offline   High   No
10   Two Year   Online   Medium   No
Ans: Entropy 2 marks+ 4 Marks+ 4 marks
Entropy= 0.881
********** 9 **********
--- page 10 ---
6 4
E(Payment) = 79 (0-918) + i (2-814) = 0.875

Information Gain:

IG(Payment) = 0.881 — 0.875 = 0.006

Weighted Entropy:

3 3 4
E(SupportCalls) = —(0.918) + —(0.918) + rly = 0.551

10 10

Information Gain:

IG(SupportCalls) = 0.881 — 0.551 = 0.330

The attribute with the highest Information Gain is Contract Type.

FRR ICR 7 OI HOH
````

## 2025-26 · Re-Exam · Sem 10 · Answer key · paper 418a584be62c

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Re-Exam/Integrated_Computer_7032/Machine Learning/ANS_Machine Learning(702CO1E001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (EXTC)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Machine Learning
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No.1 is compulsory.
3. Out of remaining questionsa attempt any 4 questions.
4. All questions carry equal marks.
5. Answer to each new question to be started on a fresh page.
6. Figure in brackets on the right hand side indicates full marks.
7. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Define Bias and Variance in a machine learning model. How do they contribute to the total   [05]
SO-   error of the model?
1;
Solution:
BL
Bias and Variance are two fundamental sources of error that determine the performance and
-2
generalization ability of a machine learning model.
Bias:
Bias refers to the error introduced due to simplifying assumptions made by the model while
learning the data. It measures how far the model’s predicted values are from the actual values
on average.
• High bias implies the model is too simple and fails to capture the underlying patterns.
•   It often leads to underfitting.
Variance:
Variance refers to the model’s sensitivity to small fluctuations in the training dataset. It
measures how much the model’s predictions change when trained on different subsets of data.
• High variance implies the model is too complex and captures noise along with
patterns.
•   It often leads to overfitting.
Contribution to Total Error:
The overall prediction error of a model can be decomposed as:
Total Error = Bias² + Variance + Irreducible Error
•   Bias²: Error due to incorrect assumptions
•   Variance: Error due to model instability
•   Irreducible Error: Noise inherent in the data that cannot be eliminated
Intuition:
• A model with high bias and low variance is consistent but inaccurate.
• A model with low bias and high variance is accurate on training data but unstable on
new data.
So we can conclude that
An optimal model minimizes total error by balancing bias and variance, ensuring good
generalization to unseen data.
********** 1 **********
--- page 2 ---
CO-1; SO-   b. Find outlier in following data set using IQR method.   [05]
1; BL   (0.1,1,10,20,25,30,35,40,45,230,500, 50,55,60,65,70,75,80,100,150,175,200)
-4   Solution:
Q1=30
Q3=100
IQR=Q1-Q3=75
Lower Fence=Q1-1.5(IQR)=-75
Upper Fence=Q1+1.5(IQR)= 205
So 230,500 are outlier
CO-2; SO-1;   c. Explain about maximum margin hyper plane in Linear support vector machine.   [05]
BL-2   Solution:
It is a supervised machine learning problem where we try to find a
hyperplane that best separates the two classes. Both the algorithms try to
find the best hyperplane, but the main difference is logistic regression is a
probabilistic approach whereas support vector machine is based on statistical
approaches.
There can be an infinite number of hyperplanes passing through a point
and classifying the two classes perfectly.
SVM does this by finding the maximum margin between the hyperplanes that
means maximum distances between the two classes.
The maximum margin will be
CO-2; SO-2;   d. Discuss the computational complexity of K-Means and Hierarchical Clustering and   [05]
BL-2   its impact on scalability.
Solution:
K_Means and Hierarchical Clustering: 02 M
Comaparison: 03 M
********** 2 **********
--- page 3 ---
K-Means is an iterative algorithm.
• Time Complexity:
O(n × k × t × d)
where:
o n = number of data points
o k = number of clusters
o   t = number of iterations
o d = number of features
• Each iteration assigns points to nearest centroid → O(n × k)
• Updating centroids → O(n)
• Repeated for t iterations
Hierarchical clustering builds a tree (dendrogram).
• Time Complexity:
O(n² log n) (optimized) or up to O(n³) (naive)
• Space Complexity:
O(n²) (distance matrix)
• Computes pairwise distance matrix → O(n²)
• Repeated merging/splitting of clusters
• Updating distances after each merge
K-Means and Hierarchical Clustering are widely used unsupervised learning
algorithms, but they differ significantly in terms of computational complexity and
scalability.
K-Means is an iterative, partition-based clustering algorithm. Its time complexity is
generally O(n × k × t × d), where n is the number of data points, k is the number of
clusters, t is the number of iterations, and d is the number of features. In practice,
since k and t are usually small and fixed, the complexity grows approximately
linearly with the number of data points (n). This makes K-Means computationally
efficient and suitable for large datasets. Additionally, it requires relatively low
memory, as it does not need to store pairwise distances between all data points.
In contrast, Hierarchical Clustering is a tree-based approach that builds a hierarchy of
clusters using either a bottom-up (agglomerative) or top-down (divisive) strategy. Its
time complexity is significantly higher, typically O(n² log n) in optimized
implementations and up to O(n³) in naïve implementations. This is because it requires
computing and updating a full pairwise distance matrix between data points, which
itself requires O(n²) space. As the number of data points increases, both the
computational time and memory requirements grow rapidly.
The difference in computational complexity has a direct impact on scalability. K-
Means is highly scalable and can efficiently handle large datasets with thousands or
even millions of data points. It is commonly used in real-world applications such as
customer segmentation and image processing. On the other hand, Hierarchical
Clustering does not scale well to large datasets due to its high time and space
********** 3 **********
--- page 4 ---
complexity. It is more suitable for smaller datasets where understanding the
hierarchical relationships between clusters is important.
Q2   a.   [10]
CO-2;   In the organization in Mumbai the chief medical officer of the in house dispensary is
SO-   distributed because of the alarming rise in the cases of high blood pressure among
2;   young male employees. A study of high BP men employees revealed that two main
BL-
factors causes high BP. Work related stress and family related stress. The chief
4
medical officer collected the data for a period of five weeks which is given bellow.
From the data set calculate multiple regression equation for employee suffering from
high blood pressure
No of employee suffering from high Blood Pressure   60   52 56 64   68
No of employee suffering from work related stress   47   41 50 42   40
No of employee suffering from family relates stress   22   26 18 13   21
Solution:
Final MLR equation is X1=19.52+0.51X2+0.902X3
Q2   b. Explain how the total error can be minimize by using error back propagation   [10]
CO-2; SO-2;   algorithm in feedforward neural network. Explain with steps.
BL-2   Solution:
Error Backpropagation, short for Backward Propagation of Errors, is a key
algorithm used to train neural networks by minimizing the difference between
predicted and actual outputs. It works by propagating errors backward through the
network, using the chain rule of calculus to compute gradients and then iteratively
updating the weights and biases.   01 Marks
********** 4 **********
--- page 5 ---
Back Propagation plays a critical role in how neural networks improve over time. Here's
why:
1. Efficient Weight Update: It computes the gradient of the loss function with respect
to each weight using the chain rule making it possible to update weights efficiently.
2. Scalability: The Back Propagation algorithm scales well to networks with multiple
layers and complex architectures making deep learning feasible.
3. Automated Learning: With Back Propagation the learning process becomes
automated and the model can adjust itself to optimize its performance.
Steps of error back propagation.
The process involves two main phases: a forward pass, where the input data is passed
through the network to compute the output, and a backward pass, where the gradients are
computed by propagating the error backward through the network.
Forward Pass
In the forward pass, the input data is fed into the network, and operations defined by the
network architecture are performed layer by layer to compute the output. This output is
then used to calculate the loss, which measures the difference between the network's
prediction and the true target values.
Backward Pass
The backward pass starts with the computation of the gradient of the loss function with
respect to the output of the network. Then, by applying the chain rule, the algorithm
calculates the gradient of the loss with respect to each weight by propagating the error
information back from the output layer to the input layer. This process involves the
following steps:
1. Compute the derivative of the loss function with respect to the activations of the
output layer.
2. For each layer, starting from the last hidden layer and moving to the first, compute
the gradients of the loss with respect to the layer's inputs, which are the activations
of the previous layer.
3. Compute the gradients of the loss with respect to the weights by considering the
gradients with respect to the layer's inputs and the derivatives of the layer's
activations with respect to its weights.
These gradients tell us how much a change in each weight would affect the loss, allowing
the optimization algorithm to adjust the weights in a direction that minimizes the loss.
Updating Weights
Once the gradients are computed, the weights are updated typically using a gradient
descent optimization algorithm. The weight update rule is generally of the form:
new_weight = old_weight - learning_rate * gradient
where the learning rate is a hyperparameter that controls the size of the weight updates.
These steps repeated multiple time to minimize the total error generated at the
********** 5 **********
--- page 6 ---
output
Q3   a. Consider the dataset:   [10]
CO-3;
SO-6;
BL-3   Credit Score   Income   Loan Approved
High   High   Yes
High   Medium   Yes
Medium   High   Yes
Low   Medium   No
Low   Low   No
Medium   Low   No
Using ID3 algorithm:
•   Calculate Entropy of target variable
• Compute Information Gain for attributes
Determine the root node
Solution:
1. Entropy of Target Variable
Total = 6
Yes = 3, No = 3
[
H(S) = -0.5\log_2(0.5) - 0.5\log_2(0.5)
]
H(S) = 1
Entropy = 1
🔹 2. Information Gain
➤ Attribute: Credit Score
• High → (2 Yes, 0 No) → Entropy = 0
• Medium → (1 Yes, 1 No) → Entropy = 1
• Low → (0 Yes, 2 No) → Entropy = 0
Weighted entropy:
[
= \frac{2}{6}(0) + \frac{2}{6}(1) + \frac{2}{6}(0) = 0.333
]
********** 6 **********
--- page 7 ---
IG:
[
IG = 1 - 0.333 = 0.667
]
➤ Attribute: Income
• High → (2 Yes, 0 No) → Entropy = 0
• Medium → (1 Yes, 1 No) → Entropy = 1
• Low → (0 Yes, 2 No) → Entropy = 0
Weighted entropy = 0.333
[
IG = 1 - 0.333 = 0.667
]
🔹 3. Root Node
• IG(Credit Score) = 0.667
• IG(Income) = 0.667
Root Node: Either attribute (tie condition)
Q3   b. Explain the concept of Unsupervised Learning and discuss the major challenges faced [10]
CO-1;
SO-1;   while implementing it. Explain tree based unsupervised learning algorithm
BL-2
Solution:
Unsupervised Learning is a type of machine learning in which the model is trained
on data without labeled outputs. The system tries to identify hidden patterns,
structures, or relationships in the data on its own.
Examples
• Customer segmentation in marketing
• Grouping similar documents
•   Clustering users on platforms like Amazon based on behavior
Common Techniques
•   Clustering (e.g., K-Means)
********** 7 **********
--- page 8 ---
•   Association Rule Mining
• Dimensionality Reduction (e.g., PCA)
Challenges of Unsupervised Learning
1. No Labeled Data
• There is no ground truth to guide learning
•   Difficult to verify correctness of results
2. Evaluation Difficulty
• No clear metrics to measure performance
•   Results may vary and be subjective
3. Interpretation of Results
•   Clusters or patterns may be hard to understand
• Requires domain knowledge
4. Choosing Parameters
•   Selecting number of clusters (K in K-Means) is difficult
•   Results depend heavily on parameter choices
5. Sensitivity to Noise
•   Outliers and noisy data can affect results
• May lead to incorrect grouping
6. Scalability Issues
• Large datasets increase computational complexity
Some algorithms become slow
Explain Hierarchical clustering algorithm
Q4   a. In a war situation, military logistics planners need to forecast the daily ammunition   [10]
CO-2;
consumption of artillery units to ensure supply lines can meet demand. The model has
SO-
2;   the relationship between daily number of fire missions and the total shells consumed.
BL-   How this problem can be solved using simple linear regression and gradient descent
2   techniques?
Solution:
Assume a linear relationship between:
•   x: number of fire missions per day
•   y: total shells consumed per day
Simple Linear regression -
y = mx + b,
where y and x are variables,
********** 8 **********
--- page 9 ---
m is the slope, and
b is the y-intercept.
Gradient Descent –
We want to minimize prediction error using Mean Squared Error (MSE).
The steps followed are -
i.   Initialize parameters
ii.   Compute gradients
iii.   Update parameters
Repeat gradient computation and updates until the Cost function converges (minimal change)
or Maximum iterations reached.
Q4   b. For the training example, X=[1,0,1] and Target label t=1, and learning rate is 0.9. The [10]
CO-3;
SO-6;   sigmoid activation function is applied to both the hidden and output layers. The
BL-6   weights are given by,
X1 X2 X3 W14 W15   W24   W25 W34   W35 W46   W56   W04   W05 W06
1   0   1   0.2   -0.3   0.4   0.1   -0.5   0.2   -0.3   -0.2   -0.4   0.2   0.1
Solution:
Solution {each answer is 2 mark)(2*5=10)
4in = 0.2+0-0.5-0.4=-0.7 4out=0.332
5in= -0.3+0+0.2+0.2=0.1 5out=0.525
6in = -0.3*0.332- 0.2*0.525+0.1 =-0.105 6out = 0.474
actual output= 6out = 0.474
********** 9 **********
--- page 10 ---
Q5   a. Explain Random Forest algorithm in detail. Discuss how randomness in data   [10]
CO-3;   sampling and feature selection improves generalization.
SO-
1;   Solution:
BL   Definition
-3
Random Forest is an ensemble learning algorithm that builds multiple decision trees
and combines their outputs to improve accuracy and reduce overfitting.
🔹 Working Steps
1. Bootstrap Sampling (Bagging)
o Random samples are drawn with replacement from dataset.
2. Decision Tree Construction
o Each tree is trained on a different subset.
3. Random Feature Selection
o At each split, only a random subset of features is considered.
4. Aggregation
o Classification → Majority Voting
o Regression → Average
🔹 Role of Randomness
1. Data Sampling (Bagging)
• Each tree sees different data → reduces variance
• Prevents overfitting
2. Feature Selection
• Forces trees to be diverse
• Avoids dominance of strong features
🔹 Advantages
• High accuracy
• Reduces overfitting
********** 10 **********
--- page 11 ---
• Handles large datasets
• Works well with missing values
🔹 Limitations
• Computationally expensive
• Less interpretable
• Slower prediction time
🔹 Applications
• Fraud detection
• Medical diagnosis
• Recommendation systems
• Stock prediction.
Q5   b. Apply K-Means clustering on the following dataset representing Height (cm) and   [10]
CO-2;
SO-2;   Weight (kg): {(150,50),(155,55),(160,60),(170,70),(175,75),(180,80)}
BL-2
Perform clustering for K = 2 and K = 3. Show the steps, update centroids, and
compare the final clusters.
Solution:
Case 1: K = 2
Step 1: Initialize Centroids
Take first two points:
C1 = (150,50), C2 = (155,55)
Step 2: Assign Points (Iteration 1)
• Cluster 1 → (150,50)
• Cluster 2 → (155,55), (160,60), (170,70), (175,75), (180,80)
Step 3: Update Centroids
• C1 = (150,50)
• C2 = average = (168,68)
Iteration 2: Reassign Points
• Cluster 1 → (150,50), (155,55), (160,60)
• Cluster 2 → (170,70), (175,75), (180,80)
Update Centroids
• C1 = (155,55)
• C2 = (175,75)
********** 11 **********
--- page 12 ---
Final Clusters (K=2)
• Cluster 1: {(150,50), (155,55), (160,60)}
• Cluster 2: {(170,70), (175,75), (180,80)}
Case 2: K = 3
Step 1: Initialize Centroids
C1 = (150,50), C2 = (155,55), C3 = (160,60)
Step 2: Assign Points
• Cluster 1 → (150,50)
• Cluster 2 → (155,55)
• Cluster 3 → (160,60), (170,70), (175,75), (180,80)
Step 3: Update Centroids
• C1 = (150,50)
• C2 = (155,55)
• C3 = (171.25, 71.25)
Iteration 2: Reassign Points
• Cluster 1 → (150,50), (155,55)
• Cluster 2 → (160,60)
• Cluster 3 → (170,70), (175,75), (180,80)
Update Centroids
• C1 = (152.5, 52.5)
• C2 = (160,60)
• C3 = (175,75)
Final Clusters (K=3)
• Cluster 1: {(150,50), (155,55)}
• Cluster 2: {(160,60)}
• Cluster 3: {(170,70), (175,75), (180,80)}
Comparison
Aspect   K = 2   K = 3
Clusters   2 groups   3 groups
Grouping   Broad (short vs tall)   More detailed
Interpretation   Simple   More precise
Q6   a. Discuss the situation where polynomial regression is applicable. What is the impact of higher [10]
CO-2; SO-2;   degree polynomial on the final result?
BL-5   Solution:
Polynomial regression is needed when the relationship between the independent
variable and dependent variable is not linear, but follows a curved pattern. In such
cases, a simple linear regression model cannot fit the data accurately. Polynomial
regression extends linear regression by adding higher-order terms such as X2, X3 etc.,
to capture the non-linear trend.
The general form of a polynomial regression model is:
y=b0+b1x1+b2x12+b2x13+…bnx1n
********** 12 **********
--- page 13 ---
Where -
y is the dependent variable,
x1 is the independent variable, and
b0 - bn are the parameters you can optimize
Need for Polymer Regression
•   It helps model curvilinear relationships between variables.
•   It improves the fit when data points do not lie along a straight line.
•   It provides better prediction accuracy than simple linear regression for non-
linear data patterns.
Impact of higher degree polynomial –
1. Better fit to training data
2. Risk of overfitting
Increased variance
One can explain with example
********** 13 **********
--- page 14 ---
Q6   b. Explain K- fold- cross validation for the dataset with 10,000 samples and number   [10]
CO-4; SO-   of fold are 100. Comment if number of folds are 1000 for the same samples.
6;   Solution:
BL- 4   K-Fold Cross Validation
K-Fold Cross Validation is a model evaluation technique used to assess the
performance and generalization ability of a machine learning model.
Working of K-Fold Cross Validation
• The dataset is divided into K equal subsets (folds).
•   In each iteration:
o One fold is used as the testing/validation set.
o Remaining K−1 folds are used for training.
• This process repeats K times, so every sample is used:
o once for testing
o K−1 times for training
The final model performance is the average of all K results.
Case 1: Dataset = 10,000 Samples, K = 100
Given:
•   Total samples = 10,000
• Number of folds = 100
Fold Size
Each fold contains:
10000100=100\frac{10000}{100}=10010010000=100
So each fold has 100 samples.
In Each Iteration
•   Training samples:
10000−100=990010000-100 = 990010000−100=9900
•   Testing samples:
100100100
Thus, for each of the 100 iterations:
•   Train model on 9,900 samples
•   Test model on 100 samples
After 100 runs, average all performance scores.
Comment on 100 Folds
Advantages
• More training data in each run (99% data used for training)
• Lower bias in performance estimate
•   Better model evaluation than small K (like 5 or 10)
Disadvantages
• Computationally expensive (train model 100 times)
• Very small test sets may give slightly unstable validation scores
This is close to high-fold cross validation.
Case 2: Same Dataset, K = 1000
Fold Size
100001000=10\frac{10000}{1000}=10100010000=10
Each fold has only 10 samples.
In Each Iteration
•   Training samples = 9,990
•   Testing samples = 10
Repeated 1000 times.
Comment on 1000 Folds
********** 14 **********
--- page 15 ---
Advantages
• Very low bias
• Almost entire dataset used for training
Q7   a. Compare Bagging, Boosting, and Random Forest techniques. Discuss their   [10]
CO-2;
SO-   advantages, limitations, and applications.
2;
BL-
2   Solution:
********** 15 **********
--- page 16 ---
1. Bagging (Bootstrap Aggregating)
Concept
•   Multiple models trained independently on different samples
Key Idea
• Reduce variance
Advantages
• Simple and effective
• Reduces overfitting
Limitations
•   Doesn’t reduce bias
•   All models treated equally
🔹 2. Boosting
Concept
• Models trained sequentially
• Each model focuses on previous errors
Key Idea
• Reduce bias and variance
Advantages
• High accuracy
• Handles complex patterns
Limitations
•   Sensitive to noise
• Can overfit
• Slower training
********** 16 **********
--- page 17 ---
🔹 3. Random Forest
Concept
• Combination of Bagging + Random feature selection
Key Idea
• Reduce variance + improve generalization
🔹 Comparison Table
Feature   Bagging   Boosting   Random Forest
Training   Parallel   Sequential   Parallel
Focus   Variance   Bias + Variance Variance
Overfitting Reduced   Can overfit   Strongly reduced
Noise   Robust   Sensitive   Robust
Example Bagged Trees AdaBoost, GBM Random Forest
Q7   b. What is the meaning of optimal capacity in a machine learning model? How is it   [05]
CO-1;   related to Overfitting and Underfitting?
SO-   Solution:
2;
BL-   The term "optimal capacity" describes a model's ideal complexity, or the point at which it is
2   strong enough to identify underlying patterns in the data without being so complex that it
begins to memorize noise. It basically involves striking a balance between the flexibility of
the model and its capacity for generalization.
Connection to Underfitting and Overfitting:
When the model's capacity is too little, underfitting occurs. It performs poorly on both
training and test sets since it is unable to identify the real patterns in the data.
Overfitting: Occurs when the capacity of the model is very high. It performs worse on unseen
test data because it matches the training data—including noise—too well.
********** 17 **********
--- page 18 ---
Between these extremes is the optimal capacity. The model achieves excellent accuracy on
both training and test sets, demonstrating good generalization.
Q7   c. What is outlier in the dataset? How one can minimize outlier explain with example   [05]
CO-1;
SO-   Solution:
6;   Explanation of outlier-02 marks
BL-
2   How to minimize explain with example-03
********** 18 **********
````
