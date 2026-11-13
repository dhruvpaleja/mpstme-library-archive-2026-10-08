# Machine Learning and Data Mining: question papers in full

6 unique papers · 2015-16 to 2023-24 · Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2023-24 · Final-Exam · paper 268d9e435729

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/MACHINE LEARNING AND DATA MINING/Machine Learning and Data Mining Batch-2023-24 Final.pdf`
- Printed on paper: max marks: 100
- Text: ocr (2 pages), mean OCR confidence 83.5

````text
SVKM’S NMIMS j
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/

SCHOOL OF TECHNOLOGY MANAGEMENT at
Academic Year: 2023-2024
Program/s: _M. Tech Year: ool Semester: JI
Stream/s: Data Science (Business Analytics)
Subject: _Machine Learning and Data Mining Time: _3_ hrs (2se0puto Sz vopm )
Date:_2 /5   / 2024 No. of Pages:_2

Marks: 100

Final Examination; i — aN
Instructions: Candidates should read carefully the instructions printed on the question paper and of the cover 4
of the Answer Book, which is provided for their use. X

1) All the Questions are compulsory. cee raat
2)Inall__5_ questions to be attempted.

3) All questions carry equal marks are indicated in the right side of each question.

4) Answer to each new question to be started on a fresh page.

5) Figures in brackets on the right hand side indicate full marks.

6) Assume Suitable data if necessary.

Dataset:

Please consider attached dataset xnor.csv provided to you. Visualization of the data (for your reference
only) is as below:

1.50 | oe ‘ ° .
° e °
1.25 4
o% *% : * %0 “@
°
10] © @ “ase % e 6 °
ee 2 ® Mee eee 0 @ e
0754 @® ®% s e e® » ®
eee ® e
0.504 e e @e 3° oe
e = °°
0.254 e @ e g e é
eo Se em ee 48%,
0.00} @ @ e oe ° @e
3 e @ 5 % e @@, % °°
-0.25 4 ° a". eo % @ @ °
eee @ e e® ®
~0.504 ee
--- page 2 ---
Note: Obviously the above data looks very non-linear. Hence looks like a logistic regression will not work
on this data and hence we must try various neural network models to fit the data and in this exam the aim
will be to find the best model.

Question 1: : [mark: 5]

The input file has 200 training sets (m = 200) and X has 2 features (n = 2), namely x1 and x2 along with the
response variable y.

Write Python code to read the data and make sure X.shape = (2, 200) as per your wish and y.shape = (1,
200).

Question 2: [mark: 5]
Please try plotting the data to see the pattern yourself (it should come similar to figure given above).
Question 3: [mark: 20]

Build a Logistic Regression model (and you may want to use any package/library like keras) and calculate
the parameters and accuracy.

Also plot a decision boundary with parameters output from Logistic Regression.
Question 4: [mark: 35]

Build a neural network model with 2 input layer followed by one (1) hidden layer with 4 units or neurons in
the hidden layer. Followed by output layer with a single neuron (as output should be either zero or one).
Allow the neural network to learn with some good amount of iterations to find out weights matrices and
bias vectors. For this question implement the following steps:

a) Separately implement sigmoid/tanh function [mark: 4]
b) Implement activation function [mark: 4]
c) Implement cost function separately [mark: 4]
d) Implement forward propagation function separately [mark: 4]
e) Implement backward propagation function separately [mark: 4]
f) Finally, a fit function with iteration [mark: rest]

Also plot a decision boundary with parameters output from Logistic Regression.
Question 5: [mark: 35]

Now submit a generic code to tryout different neural network models with again one (1) hidden layer but
it should try [1, 2, 3, 4, 5, 20, 50] units / neurons in the given one hidden layer and analyze results in terms
of accuracy (and also how the boundary looks like for different models) and find the model which you will
choose as your final model. Also try to show some visualization in terms of cost function output and
boundaries for models.
````

## 2023-24 · Re-Exam · paper a790b9e6a15b

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/MACHINE LEARNING AND DATA MINING/Machine Learning and Data Mining Batch 2023-24 Re Exam0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 86.4
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS

SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

rr
Program/s: M. Tech ° Year: 2024 Semester: II

Stream/s: Data Science (Business Analytics)

Subject: _Machine Learning and Data Mining Time: 3 hrs (2:00pm to S00 pm.)
Date:_24 /_ 6 /2024 No. of Pages:_2_
Marks: 100 _

‘Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) All the Questions are compulsory.

2)Inall___5_ questions to be attempted.

3) All questions carry equal marks are indicated in the right side of each question.
4) Answer to each new question to be started on a fresh page.

5) Figures in brackets on the right hand side indicate full marks.

6) Assume Suitable data if necessary.

Dataset:

Please consider attached dataset noisy_moons.csv provided to you. Visualization of the data (for your
reference only) is as below:

15 4
e °
e ®
104 e °° “2° ee’
‘gee 8 8 Oe oe
" “eit ° e e
oes “eo , O& ae °
054 ; eo °,.6 Or) Se
° 3 & “of &,
ww “ Ff. % °
ee eo gts *, 2% 8
© Fo BoB? 2 «
“057 hee os Pe) °e

-15   -1.0 -0.5 0.0 0.5 10 15 2.0 2.5

Note: Obviously the above data looks very non-linear. Hence looks like a logistic regression will not work

on this data and hence we must try various neural network models to fit the data and in this exam the aim
will be to find the best model.
--- page 2 ---
Question 1: [mark: 5]

The input file has 200 training sets (m = 200) and X has 2 features (n = 2), namely x: and x3 along with the
response variable y.

Write Python code to read the data and make sure X.shape = (2, 200) as per your wish and y.shape = (1,
200).

Question 2: [mark:.5]
Please try plotting the data to see the pattern yourself (it should come similar to figure given above).
Question 3: [mark: 20]

Build a Logistic Regression model (and you may want to use any package/library like keras) and calculate
the parameters and accuracy.

Also plot a decision boundary with parameters output from Logistic Regression.
Question 4: [mark: 35]

Build a neural network model with 2 input layer followed by one (1) hidden layer with 4 units or neurons in
the hidden layer. Followed by output layer with a single neuron (as output should be either zero or one).
Allow the neural network to learn with some good amount of iterations to find out weights matrices and
bias vectors. For this question implement the following steps:

a) Separately implement sigmoid/tanh function [mark: 4]
b) Implement activation function [mark: 4]
c) Implement cost function separately [mark: 4]
d) Implement forward propagation function separately [mark: 4]
e) Implement backward propagation function separately [mark: 4]
f) Finally, a fit function with iteration [mark: rest]

Also plot a decision boundary with parameters output from Logistic Regression.
Question 5: [mark: 35]

Now submit a generic code to tryout different neural network models with again one (1) hidden layer but
it should try [1, 2, 3, 4, 5, 20, 50] units / neurons in the given one hidden layer and analyze results in terms
of accuracy (and also how the boundary looks like for different models) and find the model which you will
choose as your final model. Also try to show some visualization in terms of cost function output and
boundaries for models.
````

## 2022-23 · Final-Exam · paper 00915a3781d2

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/MACHINE LEARNING AND DATA MINING/Machine Learning and Data Mining 2022-23 Final0001.pdf`
- Text: ocr (2 pages), mean OCR confidence 86.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2022-2023

Program: M.Tech Stream: Data Science

MPSTME

Subject: _ Machine Learning ard Data Mining. Time;

Date:_06/05/ 2023.
Marks: _100

Fovah Examination.

Instructions: Candidates should read carefully the instructions printed on the question

paper and on the cover of the Answer Book, which is provided for their use.

1) Inall_5 questions to be attempted and all are compulsory. And marks are indicated in
the square brackets against each of the question.

2) You may want to submit your python notebook as your answer.

3) Answer to each new question to be started on a fresh page in MS word or something
similar.

4) Assume Suitable data if necessary.

Dataset:

Please consider attached dataset tee1.csv. Visualization of the data (for your reference only)

2.5 Class
* [one]
2.0 *4
%
AS * Bd *
* . a
. * *
1.0 vee * ke OK *
°
- * «# *% © got * :
05 x ok KF OMe ° sor * *
°
° a GPS go” _—
SZ 00 * xO Loe 8 “On
° 68,02 0 * *
- a Bk tex 0 @°o
-0.5 * Pe Pe SOR ye x
” * or eK
1.0 EE ee * *
* * x *
*
$5 * * *
x *
-2.0
*
-2.5

20 -15 -1.0 -0.5 0.0 0.5 1.0 1.5
X1

Xi vs. XO. Snape shows cetails about Class.
--- page 2 ---
Note: Obviously the above data looks very non-linear. Hence looks like a logistic regression
will not work on this data and hence we must try various neural network models to fit the
data and in this exam the aim will be to find the best model.

Question 1: [mark: 5]

The input file has 200 training sets (m = 200) and X has 2 features (n = 2), namely xo and x1
along with the response variable y.

Read the data and make sure X.shape = (200, 2) or (2, 200) as per your wish and y.shape =
(200, 1) or (1, 200).

Question 2: [mark: 5]

Please try plotting the data to see the pattern yourself (it should come similar to figure given
above).

Question 3: : [mark: 20]

Run a Logistic Regression (and you may want to use any package/library) and calculate the
parameters and accuracy.

Question 4: [mark: 35]

Build a neural network model with one (1) hidden layer (apart from one input layer (2 units)
and one output layer (1 unit)) with 4 units or neurons in the hidden layer. Allow the neural
network to learn with some good amount of iterations to find out weights matrices and bias
vectors.

a) Separately implement sigmoid function [mark: 4]
b) Implement activation function [mark: 4]
c) Implement cost function separately [mark: 4]
d) Implement forward propagation function separately [mark: 4]
e) Implement backward propagation function separately [mark: 4]
f) Finally, a covering function with iteration [mark: rest]
Question 5: [mark: 35]

Now submit a generic code to tryout different neural network models with again one (1)
hidden layer but it should try [1, 2, 3, 4, 5, 20, 50] units / neurons in the given one hidden
layer and analyze results in terms of accuracy (and also how the boundary looks like for
different models) and find the model which you will choose as your final model. Also try to
show some visualization in terms of cost function output and boundaries for models.
````

## 2021-22 · Final-Exam · paper e87844d03e09

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/MACHINE LEARNING AND DATA MINING/Machine Learning and Data Mining 2021-22 Final0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (1 page), mean OCR confidence 94.1

````text
. SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & E:
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEE

Academic Year: 2021-22

Programme: M.Tech Data Science (Business Analytics) Year: I Semester: II
Subject: Machine Learning and Data Mining

Marks: 100
Date: 11 April2022 ~~ Time: 2.00 pm to 5.00 pm

Durations: 3 (hrs)
No. of Pages: 1 _
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question
paper and on the cover of the Answer Book, which is provided for their use.
1) All questions to be attempted and all are compulsory.

2) All questions carry marks indicated in bracket beside each of the question.

3) Answer to each new question to be started on a fresh page.

4) Assume Suitable data if necessary.

~ QUESTION: [mark: 100]
Answer all sections below.

Dataset:
This dataset consists of 12500 cats and 12500 dogs.

You need to create 2 different classification models and compare the accuracy of these
model to select the best model you want to deploy.

Section A: [max mark: 10]

Define steps of preprocessing of data if there are any including splitting dataset into training
and test sets.

Section B: [max mark: 50]

Design three models (two in details) and show the architecture of your design with
explanations.

Section C: [max mark: 20]

Interpretation of your model outputs and discuss accuracy matrix that you are considering
to select the best model

Section D: [max mark: 10]
Discuss about your hyper parameters if there are any.
Section E: [max mark: 10]

Concluding remarks about your models

(2)
````

## 2018-19 · Final-Exam · paper e87e0abff043

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/MACHINE LEARNING AND DATA MINING/Machine Learning and Data Mining 2018-19 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 22 April 2019
- Text: ocr (6 pages), mean OCR confidence 92.7

````text
SVKM’s NMIMS — “
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENES EERING

Programme: M. Tech (Data Science) Year: IT Semester: Fall Semester2

Academic Year: 2018-2019

Subject: Machine Learning and Data Mining

. Marks: 100
Date: 22 April 2019 Time: 2.00 pm to 5.00 pm
Durations: 3 Hrs
No. of Pages:

Final-Examination (2018-19)

Instructions: Candidates should read carefully the instructions printed on the question
paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _11__ is compulsory.

2) Out of remaining 10 questions, attempt any__5___ questions.
3)Inall__6_ questions to be attempted.

4) Quarion 11 carries 50 marks

5) All others carry 10 each

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Question 1: A feature F1 can take certain value: A, B, C, D, E, & F and represents grade
of students from a college.

1) Which of the following statement is true in following case? 10 Marks

A) Feature F1 is an example of nominal variable.
B) Feature F1 is an example of ordinal variable.
C) It doesn’t belong to any of the above category.
D) Both of these

I\¢
--- page 2 ---
Question 2: Which of the following hyper parameter(s), when increased may cause
random forest to over fit the data? 10 Marks

1. Number of Trees
2. Depth of Tree
3. Learning Rate

A) Only 4

B) Only 2

C) Only 3

D) 1 and 2

E) 2 and 3

F) 4,2 and 3

Question 3: you want to develop a machine learning algorithm which predicts the
number of views on the articles. 10 Marks
Your analysis is based on features like author name, number of articles written by the
same author on in past and a few other features. Which of the following evaluation

metric would you choose in that case?

4, Mean Square Error
2. Accuracy
3. F1 Score

A) Only 4
B) Only 2
C) Only 3
D) 1 and 3
E) 2 and 3

F) 1 and 2
--- page 3 ---
Question 4: Below are the 8 actual values of target variable in the train file.
[0,0,0,1,1,1,1,1]

What is the entropy of the target variable? 10 Marks
A) -(6/8 log(5/8) + 3/8 log(3/8))

B) 5/8 log(5/8) + 3/8 log(3/8)

C) 3/8 log(5/8) + 5/8 log(3/8)

D) 5/8 log(3/8) ~ 3/8 log(5/8)

Question 5: Let’s say, you are working with categorical feature(s) and you have not
looked at the distribution of the categorical variable in the test data. 10 Marks

You want to apply one hot encoding (OHE) on the categorical feature(s). What
challenges you may face if you have applied OHE on a categorical variable of train
dataset?

A) All categories of categorical variable are not present in the test dataset.

B) Frequency distribution of categories is different in train as compared to the test-dataset.
C) Train and Test always have same distribution.

D) Both A and B

E) None of these

3c
--- page 4 ---
Question 6: Adding a non-important feature to a linear regression model may result
in. 10 Marks

1. Increase in R-square
2. Decrease in R-square

A) Only 1 is correct
B) Only 2 is correct
C) Either 1 or 2

D) None of these

Question 7: Imagine, you are solving a classification problems with highly imbalanced
class. The majority class is observed 99% of times in the training data.

Your model has 99% accuracy after taking the predictions on test data. Which of the
following is true in such a case? 10 Marks

1. Accuracy metric is not a good idea for imbalanced class problems.

2. Accuracy metric is a good idea for imbalanced class problems.

3. Precision and recall metrics are good for imbalanced class problems.
4. Precision and recall metrics aren’t good for imbalanced class problems.

A) 1 and 3
B) 1 and 4
C)2and3

D) 2 and 4

4 lk
--- page 5 ---
Question 8: In ensemble learning, you aggregate the predictions for weak learners, so
that an ensemble of these models will give a better prediction than prediction of
individual models. 10 Marks

Which of the following statements is / are true for weak learners used in ensemble
model?

4. They don’t usually overfit.
2.. They have high bias, so they cannot solve complex learning problems
3. They usually overfit.

A) i and 2
B) 1 and 3
C)2 and3
D) Only 1
E) Only 2

F) None of the above

Question 9: Which of the following is/are true about boosting trees? 10 Marks

1. In boosting trees, individual weak learners are independent of each other
2. Itis the method for improving the performance by aggregating the results of weak
learners

A) 1
B) 2

C) tand 2

D) None of these

s/s
--- page 6 ---
Question 10: Which of the following is/are true about Random Forest and Gradient
Boosting ensemble methods? 10 Marks

4. Both methods can be used for classification task

2. Random Forest is use for classification whereas Gradient Boosting is use for
regression task

3. Random Forest is use for regression whereas Gradient Boosting is use for
Classification task

4, Both methods can be used for regression task

A) 4
B) 2
C)3
D)4
E) 1 and 4

Question 11 50 Marks
- From 1934 to 1963, San Francisco was infamous for housing some of the world's most notorious
criminals on the inescapable island of Alcatraz.

Today, the city is known more for its tech scene than its criminal past. But, with rising wealth
inequality, housing shortages, and a proliferation of expensive digital toys riding BART to work, there
is no scarcity of crime in the city by the bay.

From Sunset to SOMA, and Marina to Excelsior, this competition's dataset provides nearly 12 years
of crime reports from across all of San Francisco's neighborhoods. Given time and location, you
must predict the category of crime that occurred.

Data is here: https://drive.google.com/open?id=1QAaFP_fRTPmge7APpFV66FBedA QsJt8y

é/6
````

## 2015-16 · Final-Exam · paper f38705571aae

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/MACHINE LEARNING AND DATA MINING/Machine Learning and Data Mining 2015-16 Final.pdf`
- Printed on paper: max marks: 70; duration hours: 3; exam date: 10/05/2016
- Text: ocr (3 pages), mean OCR confidence 92.2

````text
SVKM’s NMIMS |/ ‘1! i

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & EX ING
ae

Programme: M. Tech - Data Science (Business Analytics) Year! #8 uw

1 Semester - II

Academic Year: 2015-2016

Subject : Machine Learning and Data Mining
Marks: 70
Date : 10/05/2016 Time : 2.00 pm to 5.00 pm
Durations: 3 (hrs)
Final-Examination

Instruction: Candidates should read carefully the instructions printed on the question paper.
NB:

1) Question No. _1, 2, 3, 4, and 8_ are compulsory.

2) Out of remaining questions, attempt any one (from 5. 6. 7) questions.

3) In all_6 _ questions to be attempted.

4) Submit answer document on blackboard.

6) Figures in brackets on the right hand side indicate full marks.

7) Use data given on blackboard

CASE STUDY:
A super market plans to offer a new line of organic products. The supermarket’s management wants to

determine which customers are likely to purchase these products.

1. The supermarket has a customer loyalty program. As an initial buyer incentive plan, the
supermarket provided coupons for the organic products to all of the loyalty program
participants and collected data that includes whether these customers purchased any of the

organic products.

2. The ORGANIC dataset contains 13 variables and over 22000 observations. (data set attached)

The variables in the data set are shown below with the appropriate roles and levels:

Name Model Role | Measurement Level Description

ID ID Nominal Customer loyalty identification number
DemAffl Input Interval Affluent grade on a scale from 1 to 30 |
DemAge Input Interval Age, in years

DemCluster Rejected Nominal Type of residential neighborhood
DemClusterGroup | Input Nominal Neighborhood group

DemGender Input Nominal M = Male, F = Female, U = Unknown
DemRegion Input Nominal Geographical region

DemTVReg Input Nominal Television region

PromClass Input Nominal Loyalty status: tin, silver, gold, or platinum |
PromSpend * Input Interval Total Amount spent

PromTime Input Interval Time as Loyalty card member

TargetBuy Target Binary Organics purchased? 1 = Yes, 0 =No
TargetAmt Target Interval Number of organic products purchased
--- page 2 ---
Though there are two target variables existing in this data set, let us consider only one target variable
called TargetBuy (Binary).

The variable DemClusterGroup contains collapsed levels of the variable DemCluster. Presume that,
based on previous experience; you believe that DemClusterGroup is sufficient for this type of modeling
effort. You may not want to consider DemCluster as a variable while building the model.

Examine the data and answer following questions:

1. What is the proportion of individuals who purchased organic products? {Mark: 2]
2. As noted above, only TargetBuy will be used for this analysis and should have a role of Target or
response variable. Explain if TargetAmt can be an input for a model used to predict TargetBuy?
(Mark: 1]
3. If needed, partition the data as appropriate and explain your partition strategy. [Mark: 2]

Answer question 4 and select any one from 5 or 6 or 7 (any one) to answer:

Explain model assessment that you are using and explain accuracy of your models for question no 4, 5,
6, or 7.

4. Build Neural network models, explain model assessment that you are using and explain accuracy
of your model (Mark: 30]

Select any one from 5, 6 or 7

5. Build different tree based models and explain |
6. Build appropriate logistic models | {Mark: 25]
7. Build some Support Vector Machine models (linear, kernel) |

Question 8 is compulsory.
8. Compare above model and suggest which model is better and why? (Mark: 10]

Submit your output in a doc with required graphs, chards and diagnostic output noting assumptions that
you are making and explain each step of your execution.
--- page 3 ---
_ S

INSTRUCTION:

4. Please find an excel file in the name of “ORGANICS” contains the data for this examination.
2. This data file (set) needs to be given to all the students writing this examination.

3. Examination will be in lab
4. Students can use tools to solve this paper and submit PDF on their findings and insight and

submit on blackboard / email
5. All exploratory statistics and graphs and charts needs to be submitted

3/3

Ps 4
````
