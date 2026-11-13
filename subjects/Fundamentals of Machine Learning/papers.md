# Fundamentals of Machine Learning: question papers in full

10 unique papers · 2022-23 to 2025-26 · Data Science, Electronics and Telecommunication

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final + Re-Exam · Sem 5 · paper b958bd9a7d59

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/FUNDAMENTALS OF MACHINE LEARNING/Foundations of Machine Learning 2025-26 Final Batch 2023-24 ,2024-25 Re Exam.pdf`
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 90.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
SCHOOL OF TECHNOLOGY MANAGEMENT :
Academic Year: 2025-2026

Program: B.Tech/MBATech/BTI Year:. _ .III/V Semester: -V/IX
Stream: Data Science i

Subject: Foundations of Machine Learning Time: 2:00pu to Ss 00pm. (3hus)
Date: 28 (u/2x _ No. of Pages: 04

Marks: 100

Final Examination (as-26 Re Exarnwation (23-24 /: 24-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.
2) Out of remaining questions, attempt any __4 _ questions: ”
3) In all___5_ questions to be attempted.
4) All questions carry equal marks.
. 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly: [20]

a. | Explain the key components of a supervised and unsupervised learning
CO- 1; BL-2 [5]
model, including features, objectives, and the model training process.

b. | Analyze how the learning rate influences ANN model training and
CO-5 ; BL-4 convergence, and propose strategies to address issues caused by rates [5]

that are too high or too low.

; c. | How gradient descent is help to find out the parameter in linear
CO-1; BL-2 : {5]
regression?

Explain the concept of Agglomerative Clustering in machine learning
CO-2 ;BL-2 [5]
and describe its different linkage types along with their applications.

Q2 [20]

.a. | Derive the mathematical expression for the derivative of the tanh

CO-5 ;BL-4 activation function and plot both'the function and its gradient over the [10]

range [-5, 5] using Python. Analyse how the gradient behaves for large
--- page 2 ---
«

input values and briefly explain its role in the vanishing gradient

£5)

problem.
Explain and derive a cost function, weights, and biases for logistic [10]
CO-2 ;BL-3 regression using the gradient descent method.
Describe the role of support vectors for SVM, the importance of
maximizing the margin, and the significance of the coefficients and
intercept.
Using the dataset of 20 students with their math and science scores, ao
where y = | indicates passed and y = 0 indicates failed, perform a linear
SVM classification using Python. Fit,the model on the dataset, print the
support vectors, coefficients, and intercept, predict the class labels, and
Q3 compute the accuracy.
CO-6 ; BL-5 import numpy as np i”
X = np.array([
(55, 65], [48, 52], [60, 58], [50, 49], [62, 61],
[70, 72], [68, 65], [75, 78], [80, 82], [85, 88],
[45, 50], [52, 48], [55,54], [57, 59], [60, 63],
[65, 68], [72, 70], [77, 75], [82, 80], [88, 85]
)
y = np.array({0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1))
Q4
Explain. the’ Curse of Dimensionality and how PCA helps address
challenges in high-dimensional data.
Using the Wine dataset from sklearn.datasets, perform’ Principal
Component Analysis (PCA) to reduce the dimensionality of the 13
CO-6 ; BL-6 [20]

chemical features. Write Python code to compute the covariance matrix,

extract its eigenvalues and eigenvectors, and project the data onto the
‘al

first few principal components. Visually represent the data in the space

of the first two principal components and interpret how the principal
--- page 3 ---
¥

components capture the variance: in the features. Compute and analyze
the explained variance ratio to determine how much information is
retained, and discuss how PCA helps in feature reduction and data
visualization.

# Load dataset

data = load_wine()

X = pd.DataFrame(data.data, columns=data.feature_names)

Using the Iris dataset from sklearn.datasets, compare the performance
of. Artificial Neural Network (ANN) and K-nearest Neighbor (KNN)
classifiers. Standardize the features and split the dataset into training and
testing sets. Train a KNN classifier and an ANN classifier on the training
data, then predict the class labels on the testing set. Compute and
compare the accuracy, precision, recall, and Fl-score for both models,
visualize their confusion matrices, and discuss the differences in |:

performance, strengths, and limitations of KNN versus ANN on this

Q5 [20]
dataset.

CO-4 ; BL-5 :

from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris(Q)

# Features (inputs)
X = iris.data

# Target (labels)

y = iris.target

Using a synthetic dataset of house sizes and prices, where X = [1, 2, 3,
; 4, 5] (in 1000 sq.. ft.) and y = [150, 200, 250, 300, 350] (in $1000),
6 v |. : . . . .
Q . implement linear regression using gradient descent to fit a line y= w*X
CO-3 ; BE-5 [20]
+ b. Initialize w and b to zero, choose a learning rate (0.01), and
iteratively(1000) update the parameters using the mean squared error

loss.
--- page 4 ---
Q7 - [20]

a. | Derive the forward prorogation equations and backpropagation update
tules for a three-layer neural network with two input neurons, four
CO-5 : BL-4 neurons .in the firstshidden layer, Two neurons in the second hidden _ [0]

layer and one output neuron, using gradient descent. Assume Linear

function as an activation function in each layer.

b. | Consider the following 6 data points in 2D space: (2,4), (2,8), (2,0),
(8,4), (8,8), and (8,0). Perform K-Means clustering with k = 2 clusters.

Perform manual K-Means clustering for 3 iterations, updating cluster
CO-3 ; BL-3 . . . [10]
assignments and centroids at each step. Next, perform K-Means using

sklearn.cluster. K-Means, compare the cluster assignments and centroid

positions with your manual results.
````

## 2025-26 · Final-Exam · Sem 5 · paper 4ddcad063ef5

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/FUNDAMENTALS OF MACHINE LEARNING/B Tech MBA Tech BTI (DS), Foundation of Machine Learning, Sem-V, Final Exam 2024-_7604c8e1.pdf`
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 93.0

````text
SVKM’S NMIMS ;
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026

Program: B.Tech/MBATech/BTI Year:. . .JII/V Semester: V/IX
Stream: Data Science

Subject: Foundations of Machine Learning Time: 2:00pm to Ss 00pm (3hus)
Date; 26 (uf/2ax No. of Pages: 04

Marks: 100

Final Examination (2s-26 Re Examination. (273-24 / 24-2 5)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.
2) Out of remaining questions, attempt any__4 _ questions.
3)Inall__5_ questions to be attempted.
4) All questions carry equal marks.

. 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: [20]

a. | Explain the key components of a supervised and unsupervised learning
CO- 1; BL-2 ; [5]
model, including features, objectives, and the model training process.

b. | Analyze how the learning rate influences ANN model training and
CO-5 ; BL-4 convergence, and propose strategies to address issues caused by rates [5]

that are too high or too low.

c. | How gradient descent is help to find out the parameter in linear
CO-1; BL-2 ; [5]
regression?

Explain the concept of Agglomerative Clustering in machine learning [5]
CO-2 ;BL-2
and describe its different linkage types along with their applications.

Q2 [20]

a. | Derive the mathematical expression for the derivative of the tanh

CO-5 ;BL-4 activation function and plot both the function and its gradient over the [10]

range [-5, 5] using Python. Analyse how the gradient behaves for large
--- page 2 ---
input values and briefly explain its role in the vanishing gradient

problem.
b. | Explain and derive a cost function, weights, and biases for logistic (10)
CO-2 ;BL-3 regression using the gradient descent method.
Describe the role of support vectors for SVM, the importance of
maximizing the margin, and the significance of the coefficients and
intercept.
Using the dataset of 20 students with their math and science scores,
where y = 1 indicates passed and y = 0 indicates failed, perform a linear
SVM classification using Python. Fit the model on the dataset, print the
support vectors, coefficients, and intercept, predict the class labels, and
Q3 compute the accuracy.
CO-6 ; BL-5 import numpy as np pa
X = np.array([
(S5, 65], [48, 52], (60, 58], [50, 49], [62, 61],
(70, 72], [68, 65], [75, 78], [80, 82], [85, 88],
[45, 50], [52, 48], [55, 54], [57, 59], [60, 63],
[65, 68], [72, 70], [77, 75], [82, 80], [88, 85]
)
y= np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1])
Q4
Explain the’ Curse of Dimensionality and how PCA helps address
challenges in high-dimensional data.
Using the Wine dataset from sklearn.datasets, perform Principal
Component Analysis (PCA) to reduce the dimensionality of the 13
CO-6 ; BL-6 [20]

chernical features. Write Python code to compute the covariance matrix,
extract its eigenvalues and eigenvectors, and project the data onto the
first few principal components. Visually represent the data in the space

of the first two principal components and interpret how the principal
--- page 3 ---
components capture the variance-in the features. Compute and analyze
the explained variance ratio to determine how much information is
retained, and discuss how PCA helps in feature reduction and data
visualization.

# Load dataset

data = load_wine()

X = pd.DataFrame(data.data, columns=data.feature_names)

Using the Iris dataset from sklearn.datasets, compare the performance
of Artificial Neural Network (ANN) and K-nearest Neighbor (KNN)
classifiers. Standardize the features and split the dataset into training and
testing sets. Train a KNN classifier and an ANN classifier on the training
data, then predict the class labels on the testing set. Compute and
compare the accuracy, precision, recall, and Fl-score for both models,
visualize. their confusion matrices, and discuss the differences in

performance, strengths, and limitations of KNN versus ANN on this

Q5 [20]
dataset.

CO-4 ; BL-5
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()

# Features (inputs)
X= iris.data

# Target (labels)

y = iris.target

Using a synthetic dataset of house sizes and prices, where X = [1, 2, 3,
. 4, 5] (in 1000 sq. ft.) and y = [150, 200, 250, 300, 350] (in $1000),
6
Q implement linear regression using gradient descent to fit a line y= w*X
CO-3 ; BL-5 ; [20}
+ b. Initialize w and b to zero, choose a learning rate (0.01), and
iteratively(1000) update the parameters using the mean squared error

loss.
--- page 4 ---
Q7 [20]

a. | Derive the forward prorogation equations and backpropagation update
rules for a three-layer neural network with two input neurons, four
CO-5 : BL-4 neurons.in the first hidden layer, Two neurons in the second hidden [10]
layer and one output neuron, using gradient descent. Assume Linear

function as an activation function in each layer.

b. | Consider the following 6 data points in 2D space: (2,4), (2,8), (2,0),
(8,4), (8,8), and (8,0). Perform K-Means clustering with k = 2 clusters.

Perform manual K-Means clustering for 3 iterations, updating cluster

CO-3 ; BL-3 [10]

assignments and centroids at each step. Next, perform K-Means using
sklearn.cluster. K-Means, compare the cluster assignments and centroid

positions with your manual results.
````

## 2024-25 · Final + Re-Exam · Sem 5 · paper 439f6f51686b

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/FUNDAMENTALS OF MACHINE LEARNING/Foudations of Machine Learning, Sem-V, Final Exam 2024-25 & Re Exam 2022-23, 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 88.5
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS SP
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
Academic Year: 2024-2025

¥

Program/s: B Tech/MBA Tech Year: _IIL~ Semester: Vv
Stream/s ;_ Data Science

Subject: __ Foundations of Machine Learning - Time: 3 hrs (_2:00 pm to 5:00 pm )
Date:__29 / 11 /2024 . No. of Pages:_ 6

Marks: 100.

Final Examination/Re-Exam 2022-23,2023-24
(2024-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

'€ 2) Out of remaining questions, attempt any__4 _ questions.
3) In all___5_ questions to be attempted. ra
4) All questions carry equal marks. “ey
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Ql .
Answer briefly: [20/20]
A import numpy as np .
X = np.array([ [-1.0, 2.0, -3.0, 4.0, 1.0], [1.5, -2.5, 3.5, -1.0, 0.5], [2.0, -1.0,
CO-1; 2.0, 3.0, -1.5] ]) :
SO- 2; . . . [5]
BL-1 How can you implement the Relu and Tanh function from scratch in Python
“= - on the data set given above?
Write down the python code in your answer book.
CO-2 ; B . 3 : .
SO-2; Differentiate between Supervised Versus Unsupervised Learning. [5]
BL-3
CO-1 ; Cc . .
SO-3; Explain what Vector and Scalar Projection with an example. [5]
BL-1
a CO-2 ; D .
SO-2; Write down the python code for linear regression cost function [5]
a BL-1
Q A import numpy as np [10]
CO-2; X = np.array([[0.5, -1.2, 3.3
50-3: p.array([[0.5, ]
--- page 2 ---
BL-4

[-0.8, 1.0, -0.5], 7
(2.2, -0.1, 0.0], -
[1.5, 1.2, -1.2]])

y = np.array({1, 0, 1, 0))..

Implement logistic regression using gradient descent on the above data set
to find the best-fitting line for the given above dataset. Write down Python
code in your answer book with following specifications:

¢ Initialize the parameters to zero.

e Set the learning rate to 0.01.

e Run the gradient descent for 1000 iterations.
Hint:
def LRGOQ):
m=
ne =
w=
f= *
cost_hist =[]
for i in range(epoch):
h=
a=
error=
cost =
dw=
db =
w
b=
cost_hist.append(cost)

return w,b
--- page 3 ---
CO-3;
SO-3;
BL-4

What is Linear Discriminant Analysis (LDA) and how mathematically we [10]
derive Fisher’s Z scores? ~

Q3
CO-3;
SO-4;
BL-5

Given the following four two-dimensional data points:
(2,3),(3,3),(6,7),(8,8),(3,4) manually apply the K-Means clustering | [10]

algorithm to group these points into 2 clusters.

How can you implement forward propagation ANN structure (2 Layers, Ist
layer (Relu) with 4 node, 2nd Layer out put layer with sigmoid activation
function using Python, with random weight initialization?.
Write down the python code in your answer book.
Hint:
def forward_propagation(X, patameters):
WI =
bl =
W2=
—_ [10]
ai=
Al= . q
Z2=
A2 =

cache =

return A2, cache

Q4

CO3-;
SO-3;
BL-4

How can you mathematically implement Principal component Analysis
(PCA) using NumPy arrays in the below data set

[10]
import numpy as np

# Sample dataset
--- page 4 ---
X = np.array(([2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0], [2.3,
2.7], (2.0, 1.6], [1.0, 1.1], [1.5, 1.6], [1.1, 0.9]]) ~
Write down the python code in your answer book.

Hint: 7

# calculate the mean of each column

M=

# center columns by subtracting column means

ee f

# calculate covariance matrix of centered matrix

_ :

##Calculate eigvector(V) for projection

import numpy as np :

ey


foal

CO3-;
SO-3;
BL-4

How can you implement a simple Artificial Neural Network (ANN) model

using Keras in Python to classify the wine dataset which contains three
layers?

Note:The Wine dataset is another popular dataset ‘for classification tasks. It
contains chemical analysis results for 178 wine samples, with 13 features

(e.g., alcohol content, malic acid, ash, etc.) and 3 target classes,
corresponding to three different wine cultivars [10]
from sklearn.datasets import load_wine

iris = load_wine()

X = wine.data

y = wine.target

Write down the python code in your answer book.

Q5

CO-3;
SO-3;

How does Agglomerative Hierarchical Clustering work? Using a dataset of
four points with coordinates do Agglomerative Hierarchical Clustering | [10]

using the method of complete linkages.
--- page 5 ---
BL-4

Name | X1 X2
A 1 2
B 3 4
Cc 5 6
D 8 8
CO-3;
SO-4; Explain the algorithm of gradient descent for linear regression [10]
BL-5
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()
X, y = digits.data, digits.target ©
X.shape
Q6
CO-3: Note: Digits dataset of grayscale images, each of size 8x8 pixels. The [10]
SO-4; images are flattened into 64-dimensional vectors for processing.
BL-5
What is the concept of Eigenface. Apply PCA‘to reduce the dimensionality
of the digits from 64 dimensions to 4 dimensions. Reconstruct a few digits
from the reduced dataset using the 4 principal components in Python.
Write down the python code in your answer book.
How does the K-Nearest Neighbors (KNN) algorithm work? Using a dataset
with 10 points characterized by two features and two classes, can you
explain the step-by-step process of classifying a new point P(3,2) using
K=3?
CO-3;
SO-4; Point__| X1 X2 class [10]
BL-5 A 1 2 0
B 2 2 0
Cc 3 1 1
D 4 K 1
5 ‘s 4 1
F 1 ] 0
5
--- page 6 ---
G 2 4 0 ;
H 3 3 1 wo
| 6 5 1

J 5 2 0

Q7

CO-2;
SO-4;
BL-3

How can you implement and compare Linear Discriminant Analysis (LDA),
Artificial Neural Networks (ANN), Support Vector Machine (SVM), and K-
Nearest Neighbors (KNN) classifiers using the iris dataset in Python?

Note: The Iris dataset is a popular dataset used for classification tasks. It
consists of 150 samples of iris flowers with four features (sepal length, sepal
width, petal length, and petal width) and three target classes (setosa,
versicolor, virginica). The goal is to classify the type of iris flower based on
these features. . °

# Load the data set

from sklearn.datasets import load_iris

iris = load_iris() X, y = iris.data, iris.target

Write down the python code in your answer book.

[20]
````

## 2024-25 · Re-Exam · Sem 5 · paper 8ae069b6d7f7

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/FUNDAMENTALS OF MACHINE LEARNING/Foundations of Machine Learning, Sem-V, 2024-25, Re Exam.pdf`
- Printed on paper: max marks: 100
- Text: ocr (8 pages), mean OCR confidence 89.5
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025

Program/s: B Tech/MBA Tech Year: II] Semester: Vo
Stream/s ; Data Science

Subject: __ Foundations of Machine Learning Time: __3_hrs (2:00 pm to 5:00 pm)
Date:_ (8/2/25 No. of Pages: 7 __

Marks: 100

Re-Exam 2022-23 , 2023-24, 2024-25

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql :

Answer briefly: [20/20]
CO-1 ; A How does the choice of learning rate impact the performance and
SO- 2; ; [5]
BL-1 convergence of gradient descent?

B import numpy as np

X = np.array([ [1.0, 2.0, 3.0, 4.0, 1.0], [1.5, 2.5, 3.5, 1.0, 0.5], [2.0, 1.0, 2.0,
CO-2 ; 3.0, 1.5] ])
SO-2 ; ; ee Soe amie el
BL3 How can you implement the sigmoid and softmax function from scratch in

Python on the data set given above?

Write down the python code in your answer book.
CO-1 ; C
S0-3; Explain what Vector and Scalar Projection with an Example. [5]
BL-1
CO-2 ; D What is the primary goal of K-Means clustering? And what is the "elbow 15]
oe method" in the context of K-Means?
--- page 2 ---
Q2 A Given the following four two-dimensional data _— points:

CO-2; (2,3),(3,3),(6,7),(8,8),(3,4) manually apply the K-Means clustering algorithm | [10]
~ to group these points into 2 clusters.

B import numpy as np
xX =np.array([1, 2, 3, 4]) # Features
y = np.array([2, 3,5, 7]) #Target
Implement linear regression using gradient descent on the above data set to
find the best-fitting line for the given dataset. Write down python code in
your answer book with following specifications:
e Initialize the parameters to zero.
e Set the learning rate to 0.01.
e Run the gradient descent for 1000 iterations.
Hint:
def gradient_descent():

we
CO-3; theta =

SO-3; [10]
BL-4 cost_history = []

for iteration in range(n_iterations):
predictions =
errors =
gradients =
theta =
cost =

cost_history.append()

return theta, cost_history

theta, cost_history = gradient_descent()

Q3 A What are the principal components, and how mathematically do we derive r10)
components?
--- page 3 ---
CO-3;
SO-4;
BL-5

B How can you implement backpropagation in an ANN structure (2 Layers, Ist
layer (Relu) with 4 node, 2nd Layer out put layer with sigmoid activation
function using Python, with random weight initialization?.

Write down the python-code in your answer book.
Hint:
def BWP (parameters, cache,X, Y):

W1l=

b1l=

W2=

b2=

Al=
SO-4; [10]

A2=
BL-5

CO-3;

>

m=
daZ2=
dW2=
db2=
dAl=
dZ]=
dW1=
dbl=
grades=

return grades

A How can you mathematically implement Linear Discriminant Analysis

(LDA) using NumPy arrays in the below data set, including the computation
Q4

CO3-;
SO-3;
BL-4 X= np.array([[4.0, 2.0], [2.0, 4.0], [2.0, 3.0], [3.0, 6.0], [4.0, 4.0], [9.0, 10.0],

[6.0, 8.0], [9.0, 5.0], [8.0, 7.0], [10.0, 8.0]])
y =np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1))

of mean vectors, within-class scatter matrix, between-class scatter matrix?

import numpy as np [10]
--- page 4 ---
import pandas as pd

df= pd.DataFrame(data=np.column_stack((X,y)),columns=['X1','X2','Y'])
Write down the python code in your answer book.
Flint:

df1=

df2 =

##Calculate Between Variability
mul] =

mu21=

mul2=

mu22=

mu=

mu=np.array(mu).reshape(1,2)

SB=

afl [xt] =

afl ['x2'] =

df2[x1'] =

df2['x2'] =

##Calculate within Variability

xL2=

x22 =

Swl=np.dot(x12.T,x12)/5

Sw2=

Sw = Swl+Sw2

A=np.dot()

B How can you implement a simple Artificial Neural Network (ANN) model

CO-3;

Pe using Keras in Python to classify the Iris dataset given below which contains
; four layers?

BL-5
--- page 5 ---
Note: The Iris dataset is a popular dataset used for classification tasks. It
consists of 150 samples of iris flowers with four features (sepal length, sepal
width, petal length, and petal width) and three target classes (setosa,

versicolor, virginica). The goal is to classify the type of iris flower based on

these features.

from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data

y = iris.target

Write down the python code in your answer book.
Q5 A
Explain the algorithm of gradient descent for logistic regression [10]
BL-4

B How does Agglomerative Hierarchical Clustering work? Using a dataset of

four points with coordiriates manually do Agglomerative Hierarchical

CO-3; Clustering using the method of single linkages.
80-4, Name_| X1 X2 [10]
BL-5 A 1 2

B 2 Ss)

Cc 5 4

D 6 5

A How does the K-Nearest Neighbors (KNN) algorithm work? Using a dataset
with 10 points characterized by two features and two classes, manually

calculate and explain the step-by-step process of classifying a new point
Q6 P(3,2) using K=3?

CO-3; [10]
a Point x1 X2 class

A 1 2 0

B 2 2 0

C 2 il 1

D 4 3 1

E 5 4 i
--- page 6 ---
G 2 4 0
H 3 fis 2 1
I 6 5 i
J 5 2 0

B What is the concept of Eigenfaces in the context of face recognition, and how

can it be implemented using the Olivetti faces dataset given below in Python?

Note: The Olivetti Faces dataset is a collection of grayscale images of human

faces, commonly used for facial recognition tasks and image processing

research. The dataset consists of 400 images, with each image being a 64x64
ai pixel grayscale image of a face. Each individual has 10 different images

0-4; [10]
are captured in various poses and expressions

from sklearn.datasets import fetch_olivetti_faces
faces = fetch _olivetti_faces()

X = faces.data # Images in 2D flattened format
y = faces.target

Write down the python code in your answer book.

How can you implement and compare Linear Discriminant Analysis (LDA),
Artificial Neural Networks (ANN), Support Vector Machine (SVM), and K-
Nearest Neighbors (KNN) classifiers using the Breast Cancer Wisconsin

dataset given below in Python?

Q7 Note: The Breast Cancer Wisconsin (Diagnostic) dataset is a well-known
COs dataset in machine learning and statistics, commonly used for classification | [20]
a tasks. It contains features computed from a digitized image of a fine needle
aspirate (FNA) of a breast mass. The dataset consists of 569 instances
(samples) and 30 features (attributes), which describe various characteristics
of the cell nuclei present in the images. The target variable is classify whether

a tumor is malignant (1) or benign (0).
--- page 7 ---
# Load the Breast Cancer Wisconsin dataset
from sklearn.datasets import load_breast_cancer
breast_cancer = datasets.load_breast_cancer()

X = breast_cancer.data # Features

y = breast_cancer.target # Target classes

Write down the python code in your answer book.
--- page 8 ---

````

## 2023-24 · Final + Re-Exam · Sem 5 · paper 615dc6fa6f4c

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/FUNDAMENTALS OF MACHINE LEARNING/Foundation of Machine Learning, Sem-V, Final Exam 2023-24 & Re Exam 2022-23.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 88.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS E
Academic Year: 2023-2024

rt

Program/s: B Tech and MBA Tech Year: _Il_ “Semester: v
Stream/s ; Data Science

Subject: Foundations of Machine Learning Time: 3 hrs (2:00 pm to 5:00pm)
Date:_23   / 11/2023 —— No. of Pages: 3

Marks: 100.

Final Examination(2023-24)/Re-Exam(2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20/20]
CO-1; a. Explain the significance of hyper parameter “learning rate” in gradient [5]
SO- 2;
BL-l descent.
CO-2 ; b. Write down the equation, value range, and python code for sigmoid function
SO-2 ; ee [5]
BL3 and tanh function.
CO-1; co ; °
SO-3; Explain what is Vector and Scalar Projection with an Example [5]
BL-1
CO-2; d. . ies : :
$02; ° Write down the python code for logistic regression cost function 6]
BL-1
a Develop “Linear Regression Gradient Descent” function using python
Q2
code for the dataset given below.
CO-2; ~ [10]
S0-3; X = [43,50,48,52,55,68,72] # study hours :
BL4 -- | y= [45,52,43,57,60,63,70] # Exam Score
--- page 2 ---
Paws
b Write down the python gode to compute the Linear Discriminant Analysis

(LDA) for the following two-dimensional dataset and find out the accuracy

CO-3; of the LDA model
SO-3; : [10]
BL-4 X1 4 242 13 14 9 6 9 8 10

x2 1 413 |6 |4 10 8 5 7 8

Class 1 1 j1 1 }1 2 2 2 2, 2

a Using the California Housing dataset provided in a CSV file, apply
Principal Component Analysis (PCA) to explore the dataset's
dimensionality. ,

Perform the following steps:

03 (i) Load the California Housing dataset from the CSV file into a pandas

CO-3;
So-4 . (ii) Standardize the feature matrix to have zero mean and unit variance.

DataFrame(california_housing.csv). 110]
BL-5 (iii) Implement PCA to reduce the dimensionality while retaining most of

the dataset's information.

(iv) Determine the number of principal components required to capture

90% of the variability.

Write down the Python code in the answer book.

b Explain the math behind SVD and Write the python code for Singular Value
Decomposition of above mentioned matrix A. Also write the resulting

rotation and stretch matrices along with their numerical values.

from numpy import array
A= np.array([ Hl
[1,2,3,4,],
(5,6.7,8],

[9,10,11,12]])

Q4 np.random.seed(5) ## same for weights

CO3-; X = np.random.randn(5, 25)
SO-3;

[20]
--- page 3 ---
[ BL-4

et

[¥ = (np.random.randn(1, 25)>0)

Define a function to create an ANN for the dataset given above. Write the
python code for ANN model in your answer sheet.

Q5
CO-3;
SO-3;
BL-4

Explain the algorithm of gradient descent for linear regression

[20]

CO-3;
SO-4;
BL-5

Write down the Python code do neural network with and without PCA on
the mnist data set(mnist.csv).

Q7

CO-2;
SO-4;
BL-3

[20]

Write down the python code do LDA, Neural network and SVM on iris
data set(iris.csv),

[20]
--- page 4 ---
import pandas as pd H

import numpy as np
from sklearn.discriminant_analysis Simp

from sklearn.preprocessing import Stan
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras. layers import Dense
from numpy import loadtxt

import*tensorflow as tf
from tensorflow.keras.utils import to_categorical
from sklearn.decomposition import PCA

from sklearn import datasets

import os
import cv2
from tensorflo
from tensorflow.keras.models impor
from numpy import array

from numpy import mean

from numpy import cov

from numpy.linalg import eig
import matplotlib.pyplot as pit
from scipy import ndimage

from scipy.linalg import svd

ort LinearDiscriminantAnalysis*'as LDA
dardScaler, LabelEncoder al

w.keras. preprocessing. image import load_img, img_to_array

+ load_model .
````

## 2023-24 · Final-Exam · Sem 10 · paper e8b90b1320b4

- Departments: Electronics and Telecommunication
- Programmes: B.TECH INTEGRATED / EXTC
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/EXTC/SEM X/FUNDAMENTALS OF MACHINE LEARNING/Fundamentals of Machine Learning Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 83.9

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT ‘
Academic Year: 2023-2024
Program/s: BTE.CH Integrated ; Year: 5° Semester: X

¥

Stream/s: EXTC

Subject: Fundamentals of Machine Learning . Time: 3 hrs @-00 proto 5:00 pm)
Date:_23 / 04 / 2024
Marks: 100

Final-Examination

Instructions: Candidates should read carefully the instructions printed on the question p:
of the Answer Book, which is provided for their use. ;

O 1) Question No. _1____ is compulsory.
2) Out of remaining questions, attempt any__4 questions.
3) In all__5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20M]

CO-1;
SO-1 ; a.
BL-4

CO-3 ;
SO-1; b. _| How does Support Vector Machine Work? [05M]

BL-1

CO-1;
SO-1 : c, | Why Feature scaling is required? [05M]

BL-1
CO-3 ; . '
SO-1; d. | Compare Regression and Classification algorithm.

BL-2

Q2
a.
Sout List and explain the outlier detection treatment methods [OM
BL-2
Q2 b. | For the given dataset classify:

Give the classification of Machine Learning algorithm [05M]

[0SM]

CO-3; Whether a special paper tissue is good or not by using K-NN for K=3 [10M]

SO-1;
BL-4

1|Page
--- page 2 ---
X1=Acid Durability X2= Strength Y= Classification

(seconds) (Kg/Kilometer)
7 7 Bad
7 ae 4 Bad
3 4 Good
1 4 Good
Q3
Discuss techniques of feature scaling and the importance of feature
CO-1; a. q 8 P [10M]
SO-1; selection.
BL-1
Q3
CO-;SO- | b. List the types of Logistic Regression and explain logistic regression (0M
1; equation.
BL-2
Q4
So a. a. | Discuss parametric and non-parametric machine learning algorithm. [10M]
BL-6
Q4 What is regularization? How does regularization works?
rete b. Explain regularization techniques. [10M]
BL-1,2
Q5
es a. | Explain steps involved in machine leaning process. [10M]
BL-2
Write note on:
Q5
CO2-: i. Batch Gradient Descent
SO-1: b. ii. Stochastic Gradient Descent [10M]
BL-1 ili. Mini Batch Gradient Descent
iv. Learning Rate:
Q6
What is Principle Component Analysis?
CO-3; a. P P y [10M]
SO-1; List the steps involved in Principle Component Analysis.
BL-1,2

2|Page-
--- page 3 ---
Q6 .
tH b. | With an example explain how does Random forest work? [10M]
BL-2

Q7
. List the advantages, disadvantages and applications of k-means clustering
CO-3; a. g g pp [10M]

SO-1; algorithm.
BL-2

Determine the root node of classification tree for the following dataset by

calculating information gain and entropy.

Day outlook temperature humidity wind _ playtennis

DI sunny hot high weak no
Q7 D2 sunny hot high strong no
b. D3 overcast hot high weak yes
CO-3; D4 ss rain mild high weak yes [10M]
SO-2; DS rain cool Rormal weak yes
BL-5 D6 rain cool normal strong no
D7 overcast cool normal strong yes
D8 sunny mild high weak no
D9 sunny cool normal weak yes
D10 rain mild normal weak yes
Dil sunny mild normal strong ycs
D112 overcast mild high strong yes
DI3_ overcast hot normal weak yes
DIi4 rain mild high strong no

3|Page
````

## 2023-24 · Re-Exam · Sem 5 · paper 4d4a40df9d5d

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/FUNDAMENTALS OF MACHINE LEARNING/Foundations of Machine Learning , Re-exam 2022-23.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 88.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024

*

Program/s: B Tech and MBA Tech Year: Ul _ Seinester: VO
Stream/s ; Data Science

Subject: Foundations of Machine Learning Time: 3 hrs (2:00 pm to 5:00pm)
Date:__07 / 62 /2024 _ No. of Pages:_ 3

Marks: 100 :

Re-Exam(2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql .

Answer briefly: (20/20]
CO-1; a. Write down the equation, value range, and python code for ReLu function 15]
pe and softmax function.
CO-2 ; b. . .
SO-2 ; Differentiate between Supervised Versus Unsupervised Learning. [5]
BL-3 ‘

_ CO-1; a. . . . .
S03; Explain algorithm behind Support vector machine [5]
BL-1
co2;   |d. ; ;
SO-2; Write down the python code for linear regression cost function [5]
BL-1
a Develop “Logistic Regression Gradient Descent” function using python

Q2 code for the dataset given below.
CO-2; X = [1.2, 3.4, 2.0, 4.5, 1.8, 5.2, 2.3, 3.9, 2.7, 4.1] # Tumour Size (cm3) [10]
snl Y =[0, 1, 0, 1, 0, 1, 0, 1, 0, 1] # Tumour Type (0 for benign, 1 for

malignant)
--- page 2 ---
CO-3;

Explain the algorithm of Principal Component Analysis and how it is help

SO-3; [10]
BL-4 to reduce the dimension with an examples.
Explain the Algorithm of Linear Discriminant Analysis (LDA). Linear
Discriminant Analysis (LDA) to reduce the dimensionality of the below
03 give dataset and find highest eigenvalues.
c0-3; X = np.array(([1, 2, 3], [10]
SO-4; [4, 5, 6],
Bie [7, 8, 91)
y = np.array([0, 1, 0])
Explain the forward and backward propagation in Neural Network [10]
np.random.seed(2) ## same for weights
Q4 X = np.random.randn(6, 30)
oe Y = (np.random.randn(1, 30)>8) [20]
BL-4 Define a function to create an ANN for the dataset given above. Write the
python code in your answer sheet.
Q5
oe Explain the algorithm of gradient descent for logistic regression [20]
BL-4
Write down the Python code do 3 layers ANN model with (Node(10, 8,15)
with Forest fire data set.
forest=pd.read_csv(‘forestfires.csv')
forest.head()
Q6 forest.pop(‘month')
oan forest.pop(‘day’) [20]
BL-5 forest.isna().sum()

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
forest['size_category']=label_encoder.fit_transform(forest['size_category'])

x=forest.iloc[:,0:28]

~
--- page 3 ---
y=forest.iloc[:,28]

Using the Pizza dataset provided in a CSV file, apply Principal Component |-
Analysis (PCA) to explore the dataset's dimensionality(pizza.csv).

Perform the following steps:
(i) Load the Pizza dataset from the CSV file into a pandas DataFrame.

Q7 .
CO-2: (ii) Standardize the feature matrix to have zero mean and unit variance. 120)
SO-4; (iii) Implement PCA to reduce the dimensionality while retaining most of

BL-3

the dataset's information.
(iv) Determine the number of principal components required to capture
90% of the variability. a

Write down the Python code in the answer book.
--- page 4 ---
import pandas as pd
import numpy as np 7
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis™as LDA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix

from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential

from tensorflow.keras. layers import Dense

from numpy import loadtxt

import tensorflow as tf

from tensorflow.keras.utils import to_categorical

from sklearn.decomposition import PCA

from sklearn import datasets

import os

import cv2 .

from tensorflow.keras.preprocessing. image import load_img, img_to_array
from tensorflow.keras.models import load_model

from numpy import array

from numpy import mean

from numpy import cov

from numpy.linalg import eig
import matplotlib.pyplot as plt
from scipy import ndimage

from scipy.linalg import svd

HT
````

## 2022-23 · Final-Exam · Sem 5 · paper 4b790875b4da

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/FUNDAMENTALS OF MACHINE LEARNING/Fundamentals of Machine Learning, 3rd Year, Sem-V, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 19 November 2022
- Text: ocr (3 pages), mean OCR confidence 82.1

````text
SVEN ‘s NMIMS
MUKESH 1 PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2022-23

Programme: B. Tech (Data Science) , Year: II | Semester: V ;
Subject: Foundations of Machine Learning . .
. Marks: 100

Date: 19 November 2022: . Time: 10.00 am - 1.00 pm ~
: Durations: 3 (Hrs)
No. of Pages: O34

Final Examination

Instructions: Candidates should read carefully the instructions Printed on the queation paper and on ithe cover
of the Answer Book, which is provided for their use.

. 1) Question No.1 is compulsory.
2) Out of remaining questions, attempt any __4 _ questions.
3)Inall___5_ questions to be attempted.
4) All questions carry equal marks. :
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

or Answer briefly: : + [20
Fill the “2” in the below Python code to complete cost function of ANN
CO-2; a def compute_cost (A2,Y): ,

SO-1; . . 5
BL-1 oe : , :
return cost

CO-2 ; .| Write down the python code for Relu and LeakyRelu activation function

$02; |B - 5
BL-2 and it’s gradient.

| CO-3 ; Explain how the concepts Eigen Values and Eigen Vectors use in Machine

80-1; me learnin , , .
BL2 e
CO- 1; ; ss ws : segs . 45
0-2. D What is vector projection? How it is helpful in classification algorithms

'/s
--- page 2 ---
-BL-1

Q2 Answer briefly: ; ~ 120
Q2 Let x = [8, 12, 20, 55, 67, 70] # Age
CO-3: y =[0, 0, 0, 1, 1, 1] # Disease- .
SO 1 2 A write down the Python code to creat=: 4 Logistic Regression gradient 10
_ .| descent function
BL-1
Q2 . : D Loo.
CO-1: How gradient descent is help to find out the parameter in Linear
SO-1; B | regression? « : a
BL-2 :
Q3 Answer briefly: 20
Let X train and Y train data is given below
np.random. seed (1)
X = np.random.randn(200,2)
A y = np.repeat([1,-1]., 100)
Q3 X[y == -1] = Xly 45 -1]41_
CO-3; _ 10
SO-2; BL- Do SVM and test the accuracy on testing data set given below
2: np.random. seed (1)
X_test = np.random.randn(20,2) °
y_test = np.random.choice([-1,1], 20)
X_test[y_test == 1] = X_test[y_test == 1]-1
Q3 ;
CO-1; B   -| Explain the algorithm of principal component analysis.
S0-1: BL- Pp 8 prineip: ponen y
1
Q4 Answer briefly: ; ; ; Rida pe 8 : 20
The data(mnist) contains 10000 continuous variables which correspond to
digits and a categorical variable describing the types of digits.
a Q4 A Do aprincipal component analysis using python code on the above data sets
: CO-;3 and find out how many components capture 90% of the variability. And| 10
nee a after that Do LDA with and without PCA and check the accuracy

Write down the Python code in the answer book.

*/3
--- page 3 ---
Q4 B
na SO- Explain the algorithmic of SVM 10
BL-1
Q5 Answer briefly: 20
Q5 _| Write down the tenser flow code answer book to create a simple 2 layers
aie SO- ANN model to predicts the digits with an image size of (64*64). (Hint : 10
BL2 any number of nodes and activation function you can use)
The data(iris) contains four continuous variables which correspond to .
- physical measures of flowers and a categorical vari iable describing the
Q5 ; flowers’ species.
ila SO- Do aLDA and ANN analysis using python.code on the above data-sets 10
BL2 and find out the accuracy of LDA and ANN model. Write down the whole
python code in your_answer book
Q6 Answer briefly: 20
Q6
CO-1; SO- . ; Log
2: Explain the concept of forward propagation in Neural Network 10
BL-l
from numpy import array
A=array([ ;
Q6 [10,20,30,40,50,60,70,80,90,1],
ail [1,2,3,4,5,6,7,8,9,21, ‘“
BL2 . [21,22,23,24,25,26,27,28,29,30]])
Write down the SVD python code in your answer book and find out
rotation and stretch matrix :
Q7 Answer briefly: 20
Write down the python code in your answer book to create an ANN model
CO-3; SO- with two-layer Neural network
2; np.random.seed(2) ## same for weights 20
BL-2 X=np.random. randn (4,200) :

Y= (fp. random. randn (1,200) >0)

V3
````

## 2022-23 · Final-Exam · Sem 10 · paper d1e3952e1c4c

- Departments: Electronics and Telecommunication
- Programmes: B.TECH INTEGRATED / EXTC
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/EXTC/SEM X/FUNDAMENTALS OF MACHINE LEARNING/Fundamentals of Machine Learning Batch 2022-23 Final0001.pdf`
- Printed on paper: max marks: 100
- Text: ocr (3 pages), mean OCR confidence 91.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023

ke

Program/s: B Tech Integrated (Sear: V Semester: X

fru!

Stream/s : Electronics & Telecommunication

Subject: Fundamentals of Machine Learning

‘Lime: S__ hrs @:0apmto S:00pn)
\ }

Date:_26 /Aps/ 2023 Noaf Pages: 3
a
Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.
(> 2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: [20]

Raa, Ody Bled a. Discuss on the curse of dimensionality and illustrate the ways in

which it can be tackled.

[5]

CO-1; SO-6; BL-3 b.
Demonstrate any two line of treatment for the outliers in the [5]
data

) | CO-2; SO-1; BL-5 c.
Evaluate the following statement. Lasso regression addresses the | [5]
over-fitting problem and also aids in feature selection.

CO-3; SO- 1: BL-2 d. Sumimanize the motivation for reducing the dataset’s [5]
dimensionality
Q2 [20]
a. Evaluate. If your AdaBoost ensemble underfits the training data,
CO-3; SO-1; BL-5 the hyperparameters needs to tweaked. Also mention the ways [10]
to do it.
. b. Explain how the algorithm uses the gradient to iteratively update

SOE SOE; Ele the parameters, and what is the role of the learning rate is inthe | [10]

algorithm
--- page 2 ---
Q3 pot

a. With a illustration, highlight the limitation of accuracy as an [10]
performance metric. Hence find out the accuracy, precision &
recall for the following confusion matrix
Predicted | Predicted
CO-2; SO-6; BL-4 Positive Negative
Actual 30 30
True
Actual 10 930
False

b. With an example, explain what is linear regression and state all [10]

CO-2; SO-1; BL-2 : ; : :
the assumptions to be met before starting the linear regression

Q4 [20]

CO-3; SO-1; a.
BL-1

What is the basic idea behind using PCA for feature selection? [as

b. Determine whether to use a regression or classification [10]
CO-3, SO-1, BL -3 algorithm for a given real-world scenario and dataset, and
explain how the chosen algorithm's output aligns with the
problem's objectives and limitations, when interpreting results.

Qs [20]

a. Explain how each of the techniques for handling missing values [10]
works, and what assumptions they make about the nature of the
missing data

CO-1; SO-1; BL-2

b. Describe how the bias-variance tradeoff can impact the [10]

CO-2 ; SO-1; BL-2 .
performance of different models

Qé [20]

a. A gynecologist records blood pressure of patient and collected
following data
Age Lower limit of BP
23 65
24 60
25 62
CO-2; SO-6; BL-3 26 70
28 70
29 73
31 75:
35 83
40 90

[10]

Calculate the value of BP if the age is 38 , 42
--- page 3 ---
b. Identify the factors in which the decision tree performance

C0-2, SO-1, BL-2 depends on? [10]
Q7 [20]
CO3-; SO-1; a. Explain how ROC curve and AUC are used to evaluate the [10]
BL-2 performance of a classifier

CO1-; SO-1; b. What is feature engineering and why is it important in machine [10]

BL-1 learning?
````

## 2022-23 · Re-Exam · Sem 5 · paper 03ce010e1437

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/FUNDAMENTALS OF MACHINE LEARNING/Foundation of Machine Learning, 3rd Year, Sem-V, Year 2022-23, Re-Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 January 2023
- Text: ocr (4 pages), mean OCR confidence 87.5

````text
SVIKM’S NMIMS

, MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
/ SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING

Program: B, Tech (Data Science) Year: III Semester : V

AcademicY ear: 2022-2023

Subject: Foundations of Machine Learning
Marks: 100

Date : 28 January 2023 Time: 10.00 am - 1.00 pm
Durations: 3 (Hrs)

_ , No. of Pages:_ OY

Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4__ questions.

3) In all___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

QI Answer briefly: , 20

Fill the “2” in the below Python code to complete the forward propagation
with 2 layers (1 input layer with activation function tanh and output layer
with activation function sigmoid)

def int_parameters(n_x, n_h, n_y):

A Wl = ?
CO- 2; bl = ?
SO-1 ; W2 = ? 5
BL-1 b2 = ?
parameters = {?}

return parameters

def FP(X, parameters) :
W1l= ?

‘ty
--- page 2 ---
bl = ?

W2 = ?
b2 = ?
Zl = ?
Al = ?
Z22 = ?
A2 =?
cache = {?}.

return cache

CO-1;
SO-2; B Write down the python code for tanh and sigmoid function and its Gradient | 5
BL-2 ‘
CO-1 ; .
SO-1; Cc Explain the concepts SVD 5
BL-2
CO- 1;
SO-2 ; D What is vector projection? How it is helpful in classification algorithms 5
BL-1
Q2 Answer briefly: 20
Q2 Let x = [58, 62, 60, 64, 67, 70] # mother's height and
CO-3: A y = [60, 60, 58, 60, 70, 72] # daughter's height
S O-l- write down the python code to create a linear Regression gradient descent | 10
BL- 1 function
Q2 . : F we
CO-3: How gradient descent is help to find out the parameter in logistic
SO-1; B regression? "
BL-2
Q3 Answer briefly: 20
Do a Support Vector Machine(SVM) two dimensional dataset?

A
Q3
CO-1;
SO-2; BL- ”
2 e

2/4

\
--- page 3 ---
Good Accounts Bad Accounts

Return Return

Curre | On Curre | On

nt investme | Accou | nt investme | Accou

Ratio | nt ntNo_ | Ratio | nt nt No
1.1 13 1 0.7 {| ou
1.5 15 2 0.9 -4 12
L2 17 3 0.8 6 13
0.9 21 4 13) 2, 14
1.6 7 | 1.1 6 15
2.2 8 6 0.5 8 16

0.9 16 7 0.3 8 17

; | ; Write down the Python code for Support Vector Machines (SVM) on the
| above data sets and find out the support vectors.

Q3

CO-ts B Explain how principal component analysis is helpful to recognize face

| sot ; BL-
Q4 Answer briefly: : 20

| | The data(iris) contains four continuous variables which correspond to

' physical measures of flowers and a categorical variable describing the

Q4 flowers’ species.

Co-;3 Do a principal component analysis using python code on the above data sets
SO-2; A and find out how many components capture 90% of the variability.

di BL-1 Write down the Python code in the answer book. 10

Q4
CO-;1 . . - . .
S0-2; B Explain how LDA algorithm works in a supervised learning data set. 10
BL-1
Q5 Answer briefly: , 20
Qs Write down the tenser flow code answer book to, create a simple 5 layers
con A ANN model to predicts the digits with an image size of (28*28). (Hint: | 9
BL-2 any number of nodes and activation function you can use)

3/4
--- page 4 ---
The data(mnist) contains 10000 continuous variables which correspond to

203: digits and a categorical variable describing the types of digits.
50-2: Do a LDA and ANN analysis using python code on the above data sets 10
BL2 and find out the accuracy of LDA and ANN model. Write down the whole
code in your_answer book
Q6 Answer briefly: 20
Q6 .
CO-1; What happened if Weights Initialized with zero in an ANN?
SO-2; a .
BL-2
from numpy import array
A = array([
Q6 [1,2,3,4,5,6,7,8,9,10],
CO-3; [11,12,13,14,15,16,17,18,19,20],
SO-2; 10
BL2 (21,22,23,24,25,26,27,28,29,30]])
Write down the SVD python code in your answer book and find out
rotation and stretch matrix
Q7 Answer briefly: 20
Write down the python code in your answer book to create an ANN for the
data set given below
CO-3; .
SO-2: np.random.seed(1) ## same for weights 20
BL-2 X=np.random. randn (4,10)

Y=(np.random.randn (1,10) >0)

Xx

‘ly
````
