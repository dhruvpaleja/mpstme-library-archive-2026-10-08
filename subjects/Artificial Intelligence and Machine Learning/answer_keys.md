# Artificial Intelligence and Machine Learning: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper f28cb6037375

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING/ANS_ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING(703DB0C072)_2025-2026.docx`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Dec 2025
- Text: docx (1 page)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester I(Exam Year: 2025-2026) Subject: ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING
Date: 09 Dec 2025Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
This question paper contains 8 pages.
Question No. 1 is compulsory
Out of remaining questions, attempt any 4 questions.
In all 5 questions to be attempted.
All questions carry equal marks
Assume Suitable data if necessary
Answer to each new question to be started on a fresh page.
Figure in right hand side indicates full marks

Q1
|
| Answer briefly:
| [20]
|

| a.
| Explain the different types of Machine Learning systems based on the
|
|
CO- 1; SO-
2 ; BL-1
|
| nature of supervision. Give one example for each.
| [5]
|

| sol
| SupervisedLearning–labeleddata,input-outputmapping, regression/classification, example: spam detection.
UnsupervisedLearning–unlabeleddata,patterndiscovery, clustering/dimensionality reduction, example: customer segmentation.

Semi-supervised Learning – few labeled + many unlabeled samples, example: web content classification.
Reinforcement Learning – agent-environment interaction, rewards & penalties, example: game playing, robotics.
|
|

| b.
| A robot is learning to navigate a maze. It receives a reward of +10 for
|
|
CO-2 ; SO- 3; BL-2
|
| reaching the goal and a penalty of -1 for hitting walls. Explain how the
robot uses Reinforcement Learning to improve its navigation. Identify
| [5]
|

|
| the agent, environment, actions, reward, and policy in this scenario.
|
|

| sol
| Agent: Robot (the learner).

Environment: Maze (where the robot moves).

Actions: Move left, right, up, down.
|
|

|
| Reward: +10 for reaching goal, -1 for hitting walls.

Policy: Strategy used by robot to choose actions that maximize cumulative reward.
Key Idea: The robot learns optimal paths by trial-and-error, improving its policy over time.
|
|
CO-3 ; SO- 2; BL-3
| c.
| A binary classifier predicts whether a customer will churn. Explain how
you would use the ROC curve and AUC to evaluate its performance.
| [5]
|

| sol
| ROC Curve – Plots True Positive Rate vs False Positive Rate at different thresholds.
AUC – Area Under the ROC Curve; measures model’s ability to distinguish classes.

Interpretation – AUC = 1 (perfect), AUC = 0.5 (random guess). Usage – Compare models’ performance regardless of class imbalance.
Threshold Selection – Choose threshold to balance sensitivity and specificity.
|
|

CO-2 ; SO- 2 ; BL-2
| d.
| What is the curse of dimensionality in machine learning? Explain its
impact on unsupervised learning and mention one approach to mitigate it.
|
[5]
|

| SOL
| The curse of dimensionality means that as the number of features increases, data becomes sparse and distances lose meaning.
Impact on unsupervised learning: Clustering and similarity based methods perform poorly because points appear equally far apart.
One mitigation approach: Dimensionality reduction, for example using PCA.

|
|

|
|
|
|

Q2
CO-1,2,3;
SO-2; BL-5
|
| The Employee_Analytics dataset contains employee information such as experience, job title, department, education, location, and salary.
It is used to analyze salary trends, performance patterns, and factors influencing employee compensation.
Features and their types:
Employee_ID → unique identifier (categorical/ID)
Experience → numerical (years of experience)
Job_Title → categorical (Analyst, Manager, Developer)
Department → categorical (HR, IT, Sales)
Education → categorical (Bachelor, Master, PhD)
Location → categorical (City1, City2, City3)
|

[20]
|

|
| Salary → numerical (target variable)
Performance_Score → numerical (1–10)
Age → numerical

Write pseudocode to preprocess this dataset for predicting employee salaries. Include steps to handle missing values, encode categorical variables, scale numerical features, and perform basic exploratory data analysis (EDA).
Write pseudocode to create new features and prepare the dataset for modeling and discuss the importance of feature selection in improving model performance and describe two methods to identify the most
influential features for salary prediction.
|
|

| Sol
| i) Preprocessing pseudocode (short format):

Load dataset

Handle missing values

Numerical → mean/median

Categorical → mode

Encode categorical variables

Label / One-Hot Encoding

Scale numerical features

Standardization / Min-Max scaling

Basic EDA

Summary statistics

Correlation check

Salary distribution

(ii) Feature engineering + modeling prep (short format):

Create new features

Experience per age

Performance × Experience

Seniority level from experience

Split data

Train / Test

Feature selection (importance):

Reduces overfitting

Improves accuracy and interpretability

Two feature selection methods (just name + line):

Correlation / Mutual Information

Model-based importance (Linear regression coefficients, Random Forest importance)
|
|

|
|
|
|
Q3
CO-2,3; SO-2;
BL-3,6
|
| Using the same dataset, write pseudocode to implement two machine learning models for predicting salaries using the selected features. Also explain suitable evaluation metrics for regression tasks. Discuss key
insights and conclusions that could be derived from the models’ results.
|

[20]
|

| sol
| As per student perspective
|
|

|
|
|
|

Q4
CO-3; SO- 2;
BL-6
|
| Evaluate the concept of overfitting in Decision Trees and how pre- pruning and post-pruning techniques help control tree complexity. Mention one or two key pruning parameters and their impact on model performance.
Justify how Random Forest improves a single Decision Tree in terms of model stability. Describe two evaluation metrics used to assess classification models and explain their significance in model selection
| [2*10]
|

| sol
| Overfitting: Happens when a Decision Tree learns noise and fits training data too perfectly, reducing test accuracy.
Pre-pruning: Stops tree growth early using parameters like
max_depth or min_samples_split — prevents overly specific splits.
|
|

|
|
| Post-pruning: Grows full tree, then removes weak branches based on validation performance (e.g., using cost-complexity pruning α).
Impact: Balances bias–variance tradeoff and improves generalization.
|
|
|

|
|
| (ii)
Random Forest: Combines multiple Decision Trees trained on random data subsets and features, reducing overfitting and increasing stability.
Evaluation Metrics:
Accuracy: Measures overall correctness.
F1-score / ROC-AUC: Balances precision and recall, useful for imbalanced data.
Significance: Helps choose models that generalize well, not just perform on training data.
|
|
|
Q5
CO-4;
SO-2; BL-2
| a
| Explain how Principal Component Analysis (PCA) is used for dimensionality reduction in machine learning. Discuss its steps, advantages, and how reducing dimensionality affects the bias-variance
tradeoff in models.
|

[10]
|
|

| sol
| PCA Steps (brief):
Standardize data.
Compute covariance matrix. Calculate eigenvectors & eigenvalues. Select top k principal components.
Transform data to k-dimensional space. Advantages:
Reduces computational complexity. Removes redundant/correlated features. Helps with visualization and noise reduction. Bias-Variance Connection:
Reducing dimensions can reduce variance because the model becomes
simpler and less sensitive to noise.
|
|
|

|
| However, if too many components are removed, bias increases as important information is lost.
PCA thus helps find a balance, improving generalization by trading a small increase in bias for a large reduction in variance.
|
|
Q5
CO-1,3; SO-2; BL-3
| b
| Explain how regularization helps in controlling overfitting in machine learning models. Discuss the key ideas behind Ridge Regression and Lasso Regression, and explain how each method penalizes model
complexity.
|

[10]
|

| sol
| Regularization:
Technique to reduce overfitting by adding a penalty for large model coefficients.
Helps the model generalize better to unseen data. Ridge Regression (L2 Regularization):
Adds penalty term: λ * Σ (coefficients²) to the loss function.
Shrinks coefficients toward zero but does not set them exactly to zero. Useful when features are correlated.
Lasso Regression (L1 Regularization):
Adds penalty term: λ * Σ |coefficients| to the loss function.
Can shrink some coefficients exactly to zero, performing feature selection. Effect:
Reduces model variance while slightly increasing bias → better generalization.
λ (regularization parameter) controls the strength of penalty.
|
|

|
|
|
|

Q 6
CO-1,2; SO-2;
BL-4,5
|
| A market-basket dataset produced the following item supports after
running Apriori:
|

[5*4]
|

|
|
| ITEMSET
| SUPPORT
|
|

|
|
| {Milk}
| 0.60
|
|

|
|
| {Bread}
| 0.50
|
|

|
|
| {Butter}
| 0.40
|
|

|
|
| {Milk, Bread}
| 0.40
|
|

|
|
| {Milk, Butter}
| 0.30
|
|

|
|
| {Bread, Butter}
| 0.30
|
|

|
|
| {Milk, Bread, Butter}
| 0.20
|
|

|
| (i) Generate all possible association rules from these itemsets.
|
|

|
| (ii) For each rule compute support, confidence, and lift. (iii)Interpret which rules are strong/useful.
(iv)Discuss the effect of changing minimum confidence from 50% to
70% on the set of accepted rules.
|
|

| sol
|
Given

s(M)=0.60, s(B)=0.50, s(U)=0.40s(M)=0.60,\; s(B)=0.50,\; s(U)=0.40s(M)=0.60,s(B)=0.50,s(U)=0.40 where UUU = Butter.
s(M,B)=0.40, s(M,U)=0.30, s(B,U)=0.30, s(M,B,U)=0.20.s(M,B)=0.40,\; s(M,U)=0.30,\; s(B,U)=0.30,\;
s(M,B,U)=0.20.s(M,B)=0.40,s(M,U)=0.30,s(B,U)=0.30,s(M,B,U)
=0.20.
All possible rules

From pairs (both directions):
Milk→BreadMilk \rightarrow BreadMilk→Bread
Bread→MilkBread \rightarrow MilkBread→Milk
Milk→ButterMilk \rightarrow ButterMilk→Butter
Butter→MilkButter \rightarrow MilkButter→Milk
Bread→ButterBread \rightarrow ButterBread→Butter
Butter→BreadButter \rightarrow BreadButter→Bread From the triple {M,B,U}\{M,B,U\}{M,B,U} (all non-empty proper subsets → remainder):
{Milk,Bread}→Butter \{Milk,Bread\} \rightarrow Butter{Milk,Bread}→Butter
{Milk,Butter}→Bread \{Milk,Butter\} \rightarrow Bread{Milk,Butter}→Bread
{Bread,Butter}→Milk \{Bread,Butter\} \rightarrow Milk{Bread,Butter}→Milk
Milk→{Bread,Butter} Milk \rightarrow
\{Bread,Butter\}Milk→{Bread,Butter}
Bread→{Milk,Butter} Bread \rightarrow
\{Milk,Butter\}Bread→{Milk,Butter}
Butter→{Milk,Bread} Butter \rightarrow
\{Milk,Bread\}Butter→{Milk,Bread} (Total 12 rules.)
Calculations (support, confidence, lift) — formulas

support(X→Y)=s(X∪Y)\text{support}(X\rightarrow Y) = s(X\cup Y)support(X→Y)=s(X∪Y).
confidence(X→Y)=s(X∪Y)s(X)\text{confidence}(X\rightarrow Y)
= \dfrac{s(X\cup Y)}{s(X)}confidence(X→Y)=s(X)s(X∪Y) .
lift(X→Y)=confidence(X→Y)s(Y)=s(X∪Y)s(X) s(Y)\text{lift}(X\ri ghtarrow Y) = \dfrac{\text{confidence}(X\rightarrow Y)}{s(Y)} =
\dfrac{s(X\cup Y)}{s(X)\,s(Y)}lift(X→Y)=s(Y)confidence(X→Y)
=s(X)s(Y)s(X∪Y) .
|
|

All values rounded to 3 decimals.
Support

Rule
s(X∪Y)s(X\cup Y)s(X∪Y)
ConfidenceLift

1875663104428Milk → Bread
| 0.400
|
Bread → Milk
| 0.400
|
Milk → Butter
| 0.300
|
Butter → Milk
| 0.300
|
Bread → Butter
| 0.300
|
Butter → Bread
| 0.300
|
{Milk,Bread} → Butter
| 0.200
|
{Milk,Butter} →
Bread
| 0.200
|
{Bread,Butter}
→ Milk
| 0.200
|
Milk →
{Bread,Butter}
| 0.200
|
Bread →
{Milk,Butter}
| 0.200
|
Butter →
{Milk,Bread}
| 0.200
|

Milk → Bread
| 0.400
|
Bread → Milk
| 0.400
|
Milk → Butter
| 0.300
|
Butter → Milk
| 0.300
|
Bread → Butter
| 0.300
|
Butter → Bread
| 0.300
|
{Milk,Bread} → Butter
| 0.200
|
{Milk,Butter} →
Bread
| 0.200
|
{Bread,Butter}
→ Milk
| 0.200
|
Milk →
{Bread,Butter}
| 0.200
|
Bread →
{Milk,Butter}
| 0.200
|
Butter →
{Milk,Bread}
| 0.200
|

0.400 / 0.600 =
0.667
0.400 / 0.500 =
0.800
0.300 / 0.600 =
0.500
0.300 / 0.400 =
0.750
0.300 / 0.500 =
0.600
0.300 / 0.400 =
0.750
0.200 / 0.400 =
0.500
0.200 / 0.300 =
0.667
0.200 / 0.300 =
0.667
0.200 / 0.600 =
0.333
0.200 / 0.500 =
0.400
0.200 / 0.400 =
0.500
0.667 / 0.500 =
1.333
0.800 / 0.600 =
1.333
0.500 / 0.400 =
1.250
0.750 / 0.600 =
1.250
0.600 / 0.400 =
1.500
0.750 / 0.500 =
1.500
0.500 / 0.400 =
1.250
0.667 / 0.500 =
1.333
0.667 / 0.600 =
1.111
0.333 / 0.300 =
1.111
0.400 / 0.300 =
1.333
0.500 / 0.400 =
1.250

A fitness and wellness company wants to cluster its gym members to design personalized workout and nutrition plans. The dataset contains the following features:

457504628141
Q 7
CO-1,2,3,4; SO-2;
BL-3,4
Feature Member ID Age Gender
Weight Height BMI
WeeklyWorkout Hours
Description
Unique identifier for each member Member’s age in years
Male / Female / Other
Weight in kilograms Height in centimeters Body Mass Index
Average hours of exercise per week
Type categorica l (ID)
numeric categorica l
numeric numeric numeric
numeric

[2*10]

|
|
| DietCompliance
Score
| Score (1–100) based on adherence to
nutrition plan
| numeric
|
|
|

|
|
| Resting Heart Rate
| Average resting heart rate in bpm
| numeric
|
|
|

|
|
| Membership
Duration
| Years since joining the gym
| numeric
|
|
|

|
| Choose a suitable clustering algorithm and justify your choice. Write the pseudocode, showing main steps such as cluster initialization, point assignment, updates, and termination.
Explain how PCA can be used before clustering and its benefits. Discuss key hyperparameters, tuning strategies (e.g., Elbow Method, Silhouette Score), and how you would evaluate and interpret the clusters to provide actionable recommendations for personalized fitness plans.
|
|

| sol
| As per student perspective
|
|
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 7d7325d26e42

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING/ANS_ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING(703DB0C072)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Dec 2025
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING
Date: 09 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Assume Suitable data if necessary
7. Answer to each new question to be started on a fresh page.
8. Figure in right hand side indicates full marks
Q1   Answer briefly:   [20]
a.   Explain the different types of Machine Learning systems based on the
CO- 1; SO-   nature of supervision. Give one example for each.   [5]
2 ; BL-1
sol   Supervised   Learning   –   labeled   data,   input-output   mapping,
regression/classification, example: spam detection.
Unsupervised   Learning –   unlabeled   data,   pattern   discovery,
clustering/dimensionality reduction, example: customer segmentation.
Semi-supervised Learning – few labeled + many unlabeled samples,
example: web content classification.
Reinforcement Learning – agent-environment interaction, rewards &
penalties, example: game playing, robotics.
b.   A robot is learning to navigate a maze. It receives a reward of +10 for
reaching the goal and a penalty of -1 for hitting walls. Explain how the
CO-2 ; SO-   [5]
3; BL-2   robot uses Reinforcement Learning to improve its navigation. Identify
the agent, environment, actions, reward, and policy in this scenario.
sol   Agent: Robot (the learner).
Environment: Maze (where the robot moves).
Actions: Move left, right, up, down.
********** 1 **********
--- page 2 ---
Reward: +10 for reaching goal, -1 for hitting walls.
Policy: Strategy used by robot to choose actions that maximize
cumulative reward.
Key Idea: The robot learns optimal paths by trial-and-error, improving
its policy over time.
c.   A binary classifier predicts whether a customer will churn. Explain how
CO-3 ; SO-   [5]
2; BL-3   you would use the ROC curve and AUC to evaluate its performance.
sol   OC Curve – Plots True Positive Rate vs False Positive Rate at different
thresholds.
AUC – Area Under the ROC Curve; measures model’s ability to
distinguish classes.
Interpretation – AUC = 1 (perfect), AUC = 0.5 (random guess).
Usage – Compare models’ performance regardless of class imbalance.
Threshold Selection – Choose threshold to balance sensitivity and
specificity.
d.   What is the curse of dimensionality in machine learning? Explain its
CO-2 ; SO-   impact on unsupervised learning and mention one approach to mitigate   [5]
2 ; BL-2
it.
SOL The bias-variance trade-off is a fundamental concept in machine learning
and statistics that describes the balance between two sources of error that
affect the performance of predictive models: bias and variance.
Understanding this trade-off is crucial for building models that generalize
well to unseen data.
The Employee_Analytics dataset contains employee information such as
experience, job title, department, education, location, and salary.
It is used to analyze salary trends, performance patterns, and factors
influencing employee compensation.
Features and their types:
Q2
• Employee_ID → unique identifier (categorical/ID)   [20]
CO-1,2,3;
SO-2; BL-5   • Experience → numerical (years of experience)
•   Job_Title → categorical (Analyst, Manager, Developer)
• Department → categorical (HR, IT, Sales)
• Education → categorical (Bachelor, Master, PhD)
•   Location → categorical (City1, City2, City3)
********** 2 **********
--- page 3 ---
•   Salary → numerical (target variable)
• Performance_Score → numerical (1–10)
• Age → numerical
(i) Write pseudocode to preprocess this dataset for predicting employee
salaries. Include steps to handle missing values, encode categorical
variables, scale numerical features, and perform basic exploratory data
analysis (EDA).
(ii) Write pseudocode to create new features and prepare the dataset for
modeling and discuss the importance of feature selection in improving
model performance and describe two methods to identify the most
influential features for salary prediction.
Sol   As per student perspective
Using the same dataset, write pseudocode to implement two machine
Q3
learning models for predicting salaries using the selected features. Also
CO-2,3;   [20]
SO-2;   explain suitable evaluation metrics for regression tasks. Discuss key
BL-3,6   insights and conclusions that could be derived from the models’ results.
sol   As per student perspective
(i) Evaluate the concept of overfitting in Decision Trees and how pre- [2*10]
pruning and post-pruning techniques help control tree complexity.
Mention one or two key pruning parameters and their impact on model
Q4
performance.
CO-3; SO-
2;   (ii) Justify how Random Forest improves a single Decision Tree in terms
BL-6
of model stability. Describe two evaluation metrics used to assess
classification models and explain their significance in model selection
sol   •   Overfitting: Happens when a Decision Tree learns noise and fits
training data too perfectly, reducing test accuracy.
• Pre-pruning: Stops tree growth early using parameters like
max_depth or min_samples_split — prevents overly specific
splits.
********** 3 **********
--- page 4 ---
• Post-pruning: Grows full tree, then removes weak branches based
on validation performance (e.g., using cost-complexity pruning
α).
• Impact:   Balances   bias–variance   tradeoff and improves
generalization.
(ii)
• Random Forest: Combines multiple Decision Trees trained on
random data subsets and features, reducing overfitting and
increasing stability.
• Evaluation Metrics:
o Accuracy: Measures overall correctness.
o F1-score / ROC-AUC: Balances precision and recall,
useful for imbalanced data.
•   Significance: Helps choose models that generalize well, not just
perform on training data.
a   Explain how Principal Component Analysis (PCA) is used for
Q5
dimensionality reduction in machine learning. Discuss   its steps,
CO-4;   [10]
SO-2;   advantages, and how reducing dimensionality affects the bias-variance
BL-2
tradeoff in models.
sol   PCA Steps (brief):
Standardize data.
Compute covariance matrix.
Calculate eigenvectors & eigenvalues.
Select top k principal components.
Transform data to k-dimensional space.
Advantages:
Reduces computational complexity.
Removes redundant/correlated features.
Helps with visualization and noise reduction.
Bias-Variance Connection:
Reducing dimensions can reduce variance because the model becomes
simpler and less sensitive to noise.
********** 4 **********
--- page 5 ---
However, if too many components are removed, bias increases as
important information is lost.
PCA thus helps find a balance, improving generalization by trading a small
increase in bias for a large reduction in variance.
b   Explain how regularization helps in controlling overfitting in machine
Q5
CO-1,3;   learning models. Discuss the key ideas behind Ridge Regression and
[10]
SO-2;   Lasso Regression, and explain how each method penalizes model
BL-3
complexity.
sol   Regularization:
Technique to reduce overfitting by adding a penalty for large model
coefficients.
Helps the model generalize better to unseen data.
Ridge Regression (L2 Regularization):
Adds penalty term: λ * Σ (coefficients²) to the loss function.
Shrinks coefficients toward zero but does not set them exactly to zero.
Useful when features are correlated.
Lasso Regression (L1 Regularization):
Adds penalty term: λ * Σ |coefficients| to the loss function.
Can shrink some coefficients exactly to zero, performing feature selection.
Effect:
Reduces model variance while slightly increasing bias → better
generalization.
λ (regularization parameter) controls the strength of penalty.
A market-basket dataset produced the following item supports after
running Apriori:
ITEMSET   SUPPORT
Q 6   {Milk}   0.60
CO-1,2;   {Bread}   0.50
SO-2;   {Butter}   0.40   [5*4]
BL-4,5   {Milk, Bread}   0.40
{Milk, Butter}   0.30
{Bread, Butter}   0.30
{Milk, Bread, Butter}   0.20
(i) Generate all possible association rules from these itemsets.
********** 5 **********
--- page 6 ---
(ii) For each rule compute support, confidence, and lift.
(iii)Interpret which rules are strong/useful.
(iv) Discuss the effect of changing minimum confidence from 50% to
70% on the set of accepted rules.
sol
Given
• s(M)=0.60,  s(B)=0.50,  s(U)=0.40s(M)=0.60,\; s(B)=0.50,\;
s(U)=0.40s(M)=0.60,s(B)=0.50,s(U)=0.40 where UUU = Butter.
• s(M,B)=0.40,  s(M,U)=0.30,  s(B,U)=0.30,
s(M,B,U)=0.20.s(M,B)=0.40,\; s(M,U)=0.30,\; s(B,U)=0.30,\;
s(M,B,U)=0.20.s(M,B)=0.40,s(M,U)=0.30,s(B,U)=0.30,s(M,B,U)
=0.20.
1. All possible rules
From pairs (both directions):
1. Milk→BreadMilk \rightarrow BreadMilk→Bread
2. Bread→MilkBread \rightarrow MilkBread→Milk
3. Milk→ButterMilk \rightarrow ButterMilk→Butter
4. Butter→MilkButter \rightarrow MilkButter→Milk
5. Bread→ButterBread \rightarrow ButterBread→Butter
6. Butter→BreadButter \rightarrow BreadButter→Bread
From the triple {M,B,U}\{M,B,U\}{M,B,U} (all non-empty proper
subsets → remainder):
7. {Milk,Bread}→Butter \{Milk,Bread\} \rightarrow
Butter{Milk,Bread}→Butter
8. {Milk,Butter}→Bread \{Milk,Butter\} \rightarrow
Bread{Milk,Butter}→Bread
9. {Bread,Butter}→Milk \{Bread,Butter\} \rightarrow
Milk{Bread,Butter}→Milk
10. Milk→{Bread,Butter} Milk \rightarrow
\{Bread,Butter\}Milk→{Bread,Butter}
11. Bread→{Milk,Butter} Bread \rightarrow
\{Milk,Butter\}Bread→{Milk,Butter}
12. Butter→{Milk,Bread} Butter \rightarrow
\{Milk,Bread\}Butter→{Milk,Bread}
(Total 12 rules.)
2. Calculations (support, confidence, lift) — formulas
• support(X→Y)=s(X∪Y)\text{support}(X\rightarrow Y) = s(X\cup
Y)support(X→Y)=s(X∪Y).
• confidence(X→Y)=s(X∪Y)s(X)\text{confidence}(X\rightarrow Y)
= \dfrac{s(X\cup Y)}{s(X)}confidence(X→Y)=s(X)s(X∪Y) .
• lift(X→Y)=confidence(X→Y)s(Y)=s(X∪Y)s(X) s(Y)\text{lift}(X\ri
ghtarrow Y) = \dfrac{\text{confidence}(X\rightarrow Y)}{s(Y)} =
\dfrac{s(X\cup Y)}{s(X)\,s(Y)}lift(X→Y)=s(Y)confidence(X→Y)
=s(X)s(Y)s(X∪Y) .
********** 6 **********
--- page 7 ---
All values rounded to 3 decimals.
Support
Rule   s(X∪Y)s(X\cup   Confidence   Lift
Y)s(X∪Y)
0.400 / 0.600 = 0.667 / 0.500 =
Milk → Bread   0.400
0.667   1.333
0.400 / 0.500 = 0.800 / 0.600 =
Bread → Milk   0.400
0.800   1.333
0.300 / 0.600 = 0.500 / 0.400 =
Milk → Butter   0.300
0.500   1.250
0.300 / 0.400 = 0.750 / 0.600 =
Butter → Milk   0.300
0.750   1.250
0.300 / 0.500 = 0.600 / 0.400 =
Bread → Butter   0.300
0.600   1.500
0.300 / 0.400 = 0.750 / 0.500 =
Butter → Bread   0.300
0.750   1.500
{Milk,Bread} →   0.200 / 0.400 = 0.500 / 0.400 =
0.200
Butter   0.500   1.250
{Milk,Butter} →   0.200 / 0.300 = 0.667 / 0.500 =
0.200
Bread   0.667   1.333
{Bread,Butter}   0.200 / 0.300 = 0.667 / 0.600 =
0.200
→ Milk   0.667   1.111
Milk →   0.200 / 0.600 = 0.333 / 0.300 =
0.200
{Bread,Butter}   0.333   1.111
Bread →   0.200 / 0.500 = 0.400 / 0.300 =
0.200
{Milk,Butter}   0.400   1.333
Butter →   0.200 / 0.400 = 0.500 / 0.400 =
0.200
{Milk,Bread}   0.500   1.250
A fitness and wellness company wants to cluster its gym members to
design personalized workout and nutrition plans. The dataset contains the
following features:
Feature   Description   Type
Q 7   categorica
Member ID   Unique identifier for each member
CO-1,2,3,4;   l (ID)
SO-2;   Age   Member’s age in years   numeric
BL-3,4
categorica
Gender   Male / Female / Other
l
Weight   Weight in kilograms   numeric
Height   Height in centimeters   numeric
BMI   Body Mass Index   numeric
Weekly Workout   [2*10]
Average hours of exercise per week   numeric
Hours
********** 7 **********
--- page 8 ---
Diet Compliance Score (1–100) based on adherence to
numeric
Score   nutrition plan
Resting Heart Rate Average resting heart rate in bpm   numeric
Membership
Years since joining the gym   numeric
Duration
(i) Choose a suitable clustering algorithm and justify your choice.
Write the pseudocode, showing main steps such as cluster
initialization, point assignment, updates, and termination.
(ii) Explain how PCA can be used before clustering and its benefits.
Discuss key hyperparameters, tuning strategies (e.g., Elbow
Method, Silhouette Score), and how you would evaluate and
interpret the clusters to provide actionable recommendations for
personalized fitness plans.
sol   As per student perspective
********** 8 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 013fd58c5472

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Mechatronics_7004/Artificial Intelligence and Machine Learning/ANS_Artificial Intelligence and Machine Learning(702MH0C018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Artificial Intelligence and Machine Learning
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1.
a. Explanation of K-means algorithm – 5 marks
b. Ideal Rational Agent- 5 marks
c. Hidden Markovian model with suitable example-5 marks
d. Explain any 2 activation functions used in artificial neural networks-5 marks
Q2.
a. Comparison of Informed search and uninformed search – 2 marks
Atomic Agent Representation– 4 marks\
Any 1 drawback of atomic agent representation relevant to the problem-2 marks
b.
********** 1 **********
--- page 2 ---
9 marks
The relationship between used car age and price is strongly negative and nearly linear in this
dataset.
Strength
Correlation coefficient r = -0.988 indicates a very strong inverse link; R²=0.976 shows the linear
model explains 97.6% of price variance. 2 marks
Pattern
Price drops ~$1,150 per year, accelerating in early years 1 mark
Q3. a. Markovian model with suitable example – 5 marks
b. Implementation of Python Code-15 marks
Q4. a Basic definition of SVM with explanation of support vectors & hyperplane with suitable
illustration – 4 marks
Role of hard margin and soft margin in SVM-4 marks
b.
********** 2 **********
--- page 3 ---
8
Tree Complete: Perfect split! If "Some" patrons → Go; if "Full" → Don't Go.
2
Result: Single-level tree with 100% accuracy. Patrons perfectly separates decisions.
2
Q5. a
architecture of single layer perceptron – 3 marks
algorithm of perceptron learning rule – 5 marks
b.
. 𝑨̃ 𝑼 𝑩̃ = {(x1 ,0.5), (x2 ,0.75), (x3 ,0.7)}
𝑨̃ Ո 𝑩̃ = {(x1 ,0.25), (x2 ,0.4), (x3 ,0.2)}   4 marks
Inference in Predicate Logic - 4 marks
Prove De Mogan’s Laws under propositional logic
4 marks
********** 3 **********
--- page 4 ---
Q6. a
Python code to develop Mc-Culloch Pitts Neuron for AND function using binary inputs. – 15 marks
b.
explanation of Fuzzy propositions and Fuzzy connectives.
Q7. i. Logistic Regression – 7 marks
ii. Applications of evolutionary robotics – 6 marks
iii. Best First Search – 7 marks
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 146f9e64f9ab

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING/ANS_ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING(703DB0C072)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: ARTIFICIAL INTELLIGENCE WITH MACHINE LEARNING
Date: 04 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 7 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Assume Suitable data if necessary
7. Answer to each new question to be started on a fresh page.
8. Figure in right hand side indicates full marks
Q1   Answer briefly:   [20]
CO-   a.
1,2;   Describe the step-by-step process followed in developing a Machine Learning
SO-2   [5]
model from data collection to deployment
; BL-
2
sol
1. Problem Definition – Define the objective and success criteria of the
ML project.
2. Data Collection – Gather relevant data from databases, sensors, or
external sources.
3. Data Preprocessing – Clean data, handle missing values,
normalize/standardize features.
4. Model Building – Select algorithm, train the model on the prepared
data.
5. Model Evaluation – Test the model using metrics like accuracy,
precision, recall.
6. Deployment – Integrate the model into real-world applications or
systems.
7. Monitoring & Maintenance – Continuously monitor model
performance and retrain if needed.
CO-1   b.
Explain the two main types of Reinforcement Learning: Model-Based and Model-
; SO-   [5]
3;   Free. Highlight their differences and give one example of each.
BL-2
Model-Based RL:
********** 1 **********
--- page 2 ---
• Learns or uses a model of the environment (transition dynamics and
reward function).
• Agent predicts outcomes of actions before taking them.
• Example: Planning robot paths using a known map.
Model-Free RL:
• Learns directly from rewards without modeling the environment.
• Agent learns optimal policy through trial-and-error.
• Example: Q-Learning or SARSA in game playing.
c.   A regression model predicts housing prices. You notice that:
CO-3
• Model A performs poorly on both training and test data.
; SO-   • Model B performs very well on training data but poorly on test data.   [5]
2;
BL-3
Explain what these observations indicate about the model’s learning behaviour
and suggest ways to improve each model.
sol   Model A: High error on both training and test → Underfitting / High Bias.
• Model too simple to capture patterns.
•   Solution: Increase model complexity, add features, reduce
regularization.
Model B: Low training error, high test error → Overfitting / High Variance.
• Model memorizes training data but fails to generalize.
•   Solution: Use more training data, simplify model, apply regularization.
Key Idea: Balance between bias and variance is crucial for good
generalization.
CO-   d.
3,4 ;
A dataset is clustered using an unsupervised learning algorithm. Explain how you   [5]
SO-2
would evaluate the quality of the clusters.
; BL-
2
Sol
The Employee_Analytics dataset contains employee-related information such as
experience, job title, department, education, location, and salary.
Q2
It is used to analyze salary trends, performance patterns, and factors influencing
CO-
employee compensation.   [20]
1,2,3;
SO-2;   Features and their types:
BL-5
• Employee_ID → Unique identifier (Categorical / ID)
• Experience → Numerical (Years of experience)
********** 2 **********
--- page 3 ---
• Job_Title → Categorical (e.g., Analyst, Manager, Developer)
• Department → Categorical (e.g., HR, IT, Sales)
• Education → Categorical (e.g., Bachelor, Master, PhD)
• Location → Categorical (e.g., City1, City2, City3)
• Salary → Numerical (Target variable)
• Performance_Score → Numerical (Range: 1–10)
• Age → Numerical (Employee age in years)
(i) Write pseudocode to preprocess the dataset for a churn-prediction model. Include
steps to handle missing values, encode categorical variables, scale numerical features,
and perform basic EDA.
(ii) Write pseudocode to create new features and prepare the dataset for modeling. Also,
discuss the importance of feature selection in improving model performance and describe
two methods to identify the most influential features for salary prediction.
Sol   As per student perspective
Q3
CO-   Write pseudocode to implement any two machine learning models .Explain
2,3;
suitable evaluation metrics for binary classification problems.   [20]
SO-2;
BL-   Discuss inferences that would guide you in selecting the best model.
3,6
sol
As per student perspective
The following dataset shows information about a company’s product
performance based on Age, Competition, and Type of product. The target variable
is Profit.
No.   Age   Competition   Type   Profit
Q4   1.   Old   Yes   software   Down
2.   Old   No   software   Down
CO-
1,2,3;   3.   Old   No   hardware   Down   [20]
SO-2;   4.   mid   yes   software   Down
BL-6   5.   mid   yes   hardware   Down
6.   mid   No   hardware   Up
7.   mid   No   software   Up
8.   new   yes   software   Up
9.   new   No   hardware   Up
10.   new   No   software   Up
********** 3 **********
--- page 4 ---
Using Information Gain and Entropy, construct a Decision Tree to predict Profit
based on the given attributes. Clearly show the step-by-step calculation of entropy
and information gain for each attribute and justify the selection of the root node.
Sol   Calculate Entropy (5 marks)
Calculate Information Gain for each feature (10 marks)
Build Decision Tree (5 marks)
Create tree structure based on maximum information gain.
https://www.mltut.com/decision-tree-in-machine-learning-a-complete-guide-
with-example/
Q5   a   Explain the concept of dimensionality reduction in machine learning. Discuss its   [20]
CO-4;   importance, the difference between feature selection and feature extraction, and
SO-2;
describe two popular dimensionality reduction techniques with examples.
BL-2
sol   Dimensionality reduction is the process of reducing the number of input features
(variables) while retaining important information for ML models.
Importance / Benefits:
Reduces computational complexity.
Helps avoid overfitting.
Improves model interpretability.
Reduces noise and redundant features.
Feature Selection vs Feature Extraction:
Feature Selection: Choose a subset of original features without changing them.
Example: Select top k features using variance threshold or mutual information.
Feature Extraction: Transform original features into a new set of features.
Example: PCA, LDA (new features are combinations of original ones).
Popular Techniques:
Principal Component Analysis (PCA):
Projects data to a lower-dimensional space along directions of maximum
variance.
Example: Reducing 100-dimensional image data to 20 principal components.
Linear Discriminant Analysis (LDA):
Finds a feature subspace that maximizes class separability.
Example: Reducing features for a classification problem with 3 classes.
(Optional) t-SNE / UMAP:
Non-linear dimensionality reduction for visualization.
Example: 2D projection of high-dimensional embeddings.
********** 4 **********
--- page 5 ---
Q5   b
Illustrate the difference between policy-based and value-based (model-free)
CO-
1,3;   reinforcement learning methods. Discuss their key characteristics, advantages,
SO-2;   and typical algorithms.
BL-3
sol   Policy-Based Methods:
Learn the policy directly: π(a|s) → probability of taking action a in state s.
Do not maintain a value function for each state.
Can handle high-dimensional or continuous action spaces.
Example algorithms: REINFORCE, Actor-Critic.
Advantages:
Can learn stochastic policies.
Better for continuous action spaces.
Disadvantages:
Can have high variance in learning.
2. Value-Based (Policy-Free / Model-Free) Methods:
Learn a value function (V(s) or Q(s,a)) first.
Derive policy indirectly: π*(s) = argmax_a Q(s,a).
Typically works in discrete action spaces.
Example algorithms: Q-Learning, SARSA, Deep Q-Networks (DQN).
Advantages:
Easy to implement for discrete problems.
Converges to optimal policy with proper exploration.
Disadvantages:
Hard to apply to continuous action spaces.
Cannot directly learn stochastic policies.
[
With respect to FP-Growth Algorithm for Association Rule Mining explain
(i) The working of the FP-Growth algorithm used for mining frequent itemsets in
Q 6
CO-   association rule learning. Discuss its main steps and advantages over the Apriori
1,2;   algorithm.   [20]
SO-2;
BL-   (ii) Write the pseudocode for the FP-Growth algorithm and explain how frequent
4,5   itemsets are extracted from the FP-Tree using conditional pattern bases and
conditional FP-Trees.
********** 5 **********
--- page 6 ---
sol
(a) Working of FP-Growth (10 marks)
•   Definition: Efficient algorithm to mine frequent itemsets without
candidate generation.
• Approach: Divide-and-conquer; compresses the database using an FP-
Tree.
•   Steps:
o Scan database: Find frequent items (support ≥ min_sup).
o Sort items: Descending order of frequency.
o Build FP-Tree:
▪ Root = null.
▪   Insert transactions in sorted order.
▪ Shared prefixes share paths; header table links nodes.
o Mine tree recursively:
▪   Start from least frequent item.
▪   Extract conditional pattern base.
▪ Build conditional FP-Tree and mine recursively.
▪ Combine results to get all frequent itemsets.
• Advantages over Apriori:
o No candidate generation.
o Fewer database scans (2 vs multiple).
o Efficient for large/dense datasets.
o Uses compact FP-Tree structure.
(b) Pseudocode & Explanation (10 marks)
• Pseudocode:
FP-Growth(D, min_sup):
1. Scan D → find frequent items
2. Sort items in decreasing frequency
3. Build FP-Tree T from transactions
4. For each item i in T (least → most frequent):
a. Extract conditional pattern base for i
b. Build conditional FP-Tree Ti
c. If Ti ≠ empty:
FP-Growth(Ti)
Append i to patterns from Ti
d. Add patterns to result set
• Key Points / Explanation:
o Conditional pattern base = prefix paths leading to an item.
o Conditional FP-Tree = tree built from pattern base.
o Recursive mining continues until no frequent items remain.
o Efficient: avoids multiple database scans, compresses repeated
prefixes.
• Summary:
o FP-Growth is faster and more memory-efficient than Apriori.
o Produces all frequent itemsets without candidate generation.
********** 6 **********
--- page 7 ---
A real estate company aims to segment its housing data to identify market groups
such   as   affordable,   mid-range,   and   luxury   properties.
The dataset includes the following features:
Dataset Features
Location Type: Type of neighborhood (Urban / Suburban / Rural) (categorical)
Size: Total square footage of the house (numeric)
Number of Bedrooms: Total number of bedrooms in the property (numeric)
Age of Property: Number of years since construction (numeric)
Lot Size: Area of land occupied by the property in square feet (numeric)
Distance to Nearest School: Distance from the property to the nearest school, in
miles (numeric)
Crime Rate Index: Local safety index value ranging from 1 to 10 (numeric)
Average Neighborhood Income: Average annual household income in the
neighborhood (numeric)
Q7
CO-
1,2,3,   Observations:   [20]
4;
SO-2;
BL-4   • Missing values are present in Lot Size and Average Neighborhood Income.
• The scales of numerical features vary widely.
• Location Type is categorical and requires proper encoding.
• A few samples contain extremely large Lot Sizes, indicating possible
outliers.
(i) Discuss the data preprocessing strategy you would apply before
performing clustering. Then, choose a suitable clustering algorithm and
justify your choice based on the dataset’s nature and desired
interpretability.
(ii) Write the pseudocode for the selected clustering algorithm, describing
each   major   computational   step   clearly.
Identify the key hyperparameters and explain how you would tune them
and discuss how you would evaluate and interpret the resulting clusters to
provide useful insights for the real estate company
Sol   As per student perspective
********** 7 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 03cb91b33b6c

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Mechatronics_7004/Artificial Intelligence and Machine Learning/ANS_Artificial Intelligence and Machine Learning(702MH0C018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: text (3 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Artificial Intelligence and Machine Learning
Date: 01 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1.
a. Explanation of Fuzzy C-means algorithm – 5 marks
b. AI definition with respect to all 4 quadrants - 5 marks
c. Hidden Markovian model with suitable example-5 marks
d. Any 1 activation function used in Back Propagation Algorithm -5 marks
Q2. a. Comparison of Informed Search and Uninformed Search.- 4 marks
Atomic Agent Representation– 4 marks
b.
Y = Β0 + Β1X
Y = 7836 – 502.4*X 10 marks
With an estimated slope of – 502.4, we can conclude that the average car
price decreases $502.2 for each year a car increases in age. 2 marks
Q3.
a. Markovian model with suitable illustration- 5 marks
b. Python code to develop a perceptron for OR function with bipolar inputs and targets-15 marks
Q4.
a. Basic definition of SVM with explanation of support vectors & hyperplane with suitable
illustration - 4 marks
The trade-off of hard margin and soft margin in SVM while determining the optimal hyperplane-4
marks
b.
********** 1 **********
--- page 2 ---
4 marks
4 marks
4 marks
Person will not play tennis
Q5. A
Steps of the Back Propagation Algorithm. – 8 marks
b. i.
. 𝑨̃ 𝑼 𝑩̃ = {(x1 ,0.8), (x2 ,0.75), (x3 ,0.8)}
𝑨̃ Ո 𝑩̃ = {(x1 ,0.35), (x2 ,0.4), (x3 ,0.1)}   4 marks
ii.
4 marks
********** 2 **********
--- page 3 ---
iii.
4 marks
Q6.a
Python code to develop Mc-Culloch Pitts Neuron for OR function using bipolar inputs. – 15
marks
b. Defuzzification is the process of converting a fuzzy set into a crisp (numeric) value in fuzzy
logic systems. Common methods include Centroid (Area), Mean of Maxima (MOM), Weighted Average
etc. The Centroid method is the most widely used. Brief explanation of 3 methods are required-5 marks
Q7. a. Logistic Regression as a binary classifier – 7 marks
b. Applications of evolutionary robotics-6 marks
c. Explanation of any 1 type of informed search technique.-7 marks
********** 3 **********
````
