# Foundations of Machine Learning: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 972e60e63a5b

- Departments: Data Science
- Programmes: BTech DS 7009, Integrated DS 7038, MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_DS_7009/Foundations of Machine Learning/ANS_Foundations of Machine Learning(702DB0C020)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (8 pages), mean OCR confidence 81.2
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026

Program: B.Tech/MBATech/BTI Year: IW/U/V Semester: V/V/IX
Stream: Data Science

Subject: Foundations of Machine Learning Time:

Date: No. of Pages: 08

Marks: 100

Synoptic answer

. Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

Ql Answer briefly: [20]

a. + Features: Supervised uses labeled data (X,y); unsupervised uses unlabeled data
(x).
* Objective: Supervised predicts labels/values; unsupervised finds patterns or
clusters. ; (5]

¢ Training: Supervised minimizes a loss function (e.g., MSE, cross-entropy);
unsupervised optimizes similarity or variance measures.

* Output: Supervised — predictions; unsupervised — clusters or reduced
features

b. Influence: Determines step size during weight updates; affects convergence speed
and stability.
Too high: Can cause overshooting or divergence.
Too low: Leads to slow convergence and may get stuck in local minima. [5]
Strategies:
Use learning rate scheduling (decay over time).
Apply adaptive optimizers like Adam, RMSProp.
Experiment with moderate initial values and adjust based on training behavior.

c. e Initialize the model parameters (weight and bias) with small random values or

zeros.

© Compute predictions using current parameters for all training examples.

¢ Calculate the error by comparing predictions with actual target values.

e Compute gradients of the error with respect to each parameter to understand
the direction to adjust. [5]

¢ Update parameters by moving them slightly in the direction that reduces the
error (controlled by learning rate).

¢ Repeat steps 2—5 iteratively until the error stops decreasing significantly
(convergence).

e Resuit: Parameters converge to values that minimize predic
--- page 2 ---
Formulae 1 marks

d. © Concept:

e A hierarchical clustering method that starts with each data point as a separate
cluster and merges clusters step by step based on similarity until all points
form a single cluster or a stopping criterion is met.

e Linkage Types:

¢ Single Linkage: Distance between the closest points of clusters; can form
elongated clusters.

¢ Complete Linkage: Distance between the farthest points of clusters; produces
compact clusters. [5]

e Average Linkage: Average distance between all points of clusters; balances
single and complete linkage.

¢ Ward Linkage: Merges clusters to minimize increase in total within-cluster
variance; produces clusters of similar size.

e Applications:

¢ Market segmentation, gene expression analysis, image segmentation, and
identifying hierarchical relationships in data.

Q2 : [20]

a. Formula: tanh(x) = (e*- e™) / (e* + e™)

Gradient: tanh'(x) = 1 - tanh’

Description: The tanh function maps inputs to the range (-1, 1) and is zero-centered,

making it often preferable to sigmoid. However, it also suffers from vanishing gradients

for large input magnitudes.

import numpy as np

import matplotlib.pyplot as plt

# Define tanh and its gradient

x = np.linspace(-5, 5, 200)

tanh_x = np.tanh(x)

grad_tanh = | - tanh_x**2

# Plot tanh and its gradient

plt.figure(figsize=(10,5))
pee plt.subplot(1,2,1) [10]
, plt.plot(x, tanh_x, label='tanh(x)', color="blue’)

plt.title(‘tanh Activation Function’)

plt.xlabel('x’)

pit.ylabel(‘tanh(x)’)

plt.grid(True)

pit.legendQ)

pit.subplot(1,2,2)

plt.plot(x, grad_tanh, label='Gradient of tanh’, color='red')

plt.title(‘Gradient of tanh(x)’)

pit.xlabel(‘x')

pit.ylabel('l - tanh?(x)')

plt.grid(True)

plt.legendQ
--- page 3 ---
\npr x ¢ Rp
We em wt Ww ER

Ze wl es

y (zd >

[xenk >:
co-3 [10]
Ar . is ?) ql
‘BL-3 oy) = Pr caueap yc’ as o tz. © Cult} +b)
Trvrbys -tog | ( \o4 \b ss)
Carlie Y '
Wor = -~y) %!
heel is _ _
we & hen og- I) fs
¢ Support Vectors: Critical data points closest to the decision boundary that
define the margin.
¢ Maximizing the Margin: Ensures better generalization and reduces
classification error on unseen data.
¢ Coefficients and Intercept: Coefficients define the slope/direction of the
hyperplane, and the intercept determines its position relative to the origin.
¢ Application in Dataset: Using student math and science scores, a linear SVM
can classify pass (1) vs fail (0), with support vectors, coefficients, and
intercept determining the decision boundary.
e Prediction and Accuracy: The model predicts class labels and computes
accuracy to assess performance.
Q3 import numpy as np
CO-3; | ° from sklearn.svm import SVC [20]
BL-3 from sklearn.metrics import accuracy_score
# Dataset
X = np.array([

[55, 65], [48, 52], [60, 58], [50, 49], [62, 61],
[70, 72], [68, 65}, [75, 78], [80, 82], [85, 88],
[45, 50], [52, 48}, [55, 54], [57, 59], [60, 63],
[65, 68], [72, 70], [77, 75], [82, 80], [88, 85]
)
y = np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1))

# Linear SVM model
svm_model = SVC(kernel="'linear’)
--- page 4 ---
svm_model.fit(X, y)

# Outputs P
print("Support Vectors:\n", sym_model.support_vectors_)
print("Coefficients:", svm_model.coef_)
print("Intercept:", svm_model.intercept_)

# Predictions

y_pred = svm_model.predict(X)

print("Predicted labels:", y_pred)

# Accuracy

accuracy = accuracy_score(y, y_pred) ©
print("Accuracy:", accuracy)

Q4

‘e Curse of Dimensionality: As the number of features increases, data becomes
sparse in high-dimensional space, making distance measures less meaningful

and models prone to overfitting.
e . :

¢ How.PCA Helps: Reduces dimensionality by projecting data onto principal
components that capture the most variance, improving computational
efficiency, visualization, and mitigating overfitting.

import pandas as pd

import numpy as np

import matplotlib.pyplot as pit

from sklearn.datasets import load_wine

# Load dataset

data = load_wine()

X = pd.DataFrame(data.data, columns=data.feature_names)
CO-2 ; # Step 1: Standardize features
ue X_std = (X - X.mean()) / X.std0) [20]

# Step 2: Compute covariance matrix

cov_matrix = np.cov(X_std.T)

# Step 3: Eigen decomposition

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 4: Sort eigenvalues & eigenvectors

idx = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[idx]

eigenvectors = eigenvectors[:, idx]

# Step 5: Project data onto first 2 principal components

PCs = X_std.dot(eigenvectors[:, :2])

# Step 6: Explained variance ratio

explained_variance_ratio = eigenvalues / eigenvalues.sum()

print("Explained variance ratio:", explained_variance_ratio[:5])

print("Total variance retained (first 2 PCs):", explained_variance_ratio[:2].sum())

# Step 7: Visualize first 2 PCs

plt.figure(figsize=(8,6))
--- page 5 ---
plt.scatter(PCs.iloc[:,0], PCs.iloc[:,1], c=data.target, cmap='viridis',
edgecolor="'k')

plt.xlabel('PC1')

plt.ylabel('PC2')

plt.title((Wine Dataset: First Two Principal Components’)
plt.colorbar(label='Wine Class’)

pit.show()

a. import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy score, precision_score, recall_score,
fl_score, confusion_matrix, ConfusionMatrixDisplay
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42, stratify=y)
# Standardize features

Q5 scaler = StandardScaler() [20]
CO-2 ; X_train_std = scaler. fit_transform(X_train).
BL-2 X_test_std = scaler.transform(X_test)

# --- KNN Classifier ---

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train_std, y_train)

y_pred_knn = knn.predict(X_test_std)

# Metrics KNN

acc_knn = accuracy_score(y_test, y_pred_knn)

prec_knn = precision_score(y_test, y_pred_knn, average='macro’)
recall_knn = recall_score(y_test, y_pred_knn, average='macro')
fl_knn = fl_score(y_test, y_pred_knn, average='macro')
print("KNN - Accuracy:", acc_knn, "Precision:", prec_knn, "Recall:", recall_knn,
"F1-score:", f1_knn)

# Confusion matrix KNN

cm_knn = confusion_matrix(y_test, y_pred_krin)
ConfusionMatrixDisplay(cm_knn).plot()

plt.title("KNN Confusion Matrix")

plit.showQ

# --- ANN Classifier ---
--- page 6 ---
ann = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000,
random_state=42)

ann.fit(X_train_std, y_train)

y_pred_ann = ann.predict(X_test_std)

# Metrics ANN

acc_ann = accuracy_score(y_test, y_pred_ann)

prec_ann = precision_score(y_test, y_pred_ann, average='macro')

recall_ann = recall_score(y_test, y_pred_ann, average='macro')

fl_ann = fl_score(y_test, y_pred_ann, average='macro')

print("ANN - Accuracy:", acc_ann, "Precision:”, prec_ann, "Recall:", recall_ ann,
"Fl-score:", f1_ ann)

# Confusion matrix ANN

cm_ann = confusion_matrix(y_test, y_pred_ann)
ConfusionMatrixDisplay(cm_ann).plot()

pit.title("ANN Confusion Matrix")

plt.show() ;

Accuracy & Metrics: Compare metrics to see which model performs better.

Visualization: Confusion matrices help identify which classes are misclassified by
each model.

import numpy as np

import matplotlib.pyplot as plt

# Dataset

X= np.array([1, 2,3, 4,5])   # House sizes (1000 sq.ft.)
| y = np.array([150, 200, 250, 300, 350]) # Prices ($1000)

# Initialize parameters

w, b= 0,0

alpha = 0.01

iterations = 1000

m = len(X)

# Gradient Descent

for i in range(iterations):

CO-3 ; y_pred=w*X+b # Predictions
BL-3 error = y_pred - y [20]
Q6 # Compute gradients

dw = (1/m) * np.sum(error * X)
db = (1/m) * np.sum(error)

# Update parameters
w -= alpha * dw
b = alpha * db

# Output final parameters

print(f" Weight (w): {w:.2f}, Bias (b): {b:.2f}")

# Predictions :

y_pred_final = w * X+b

print("Predicted prices:", y_pred_final)

# Plot

plt.scatter(X, y, color="blue’, label='Actual Prices’)
--- page 7 ---
pit.plot(X, y_pred_final, color="red’, label='Fitted Line’)
pit.xlabel(‘House Size (1000 sq. ft.)')

plt.ylabel('Price ($1000)')

plt.title(Linear Regression using Gradient Descent’)
plt.legendQ

plt.showO

Q7 [20]

MER
\ Ue 2. t

AAA
yf? te ree
Brio wre et y-

cox word! Bie yh tase { Leno
ce

aos Zz
Rode ors
CO-2 ; e
BL-2 Guecoovierd cheno 10]
BL 2 OK’
ye?
--- page 8 ---
b. import numpy as np
from sklearn.cluster import KMeans
# Data points
X = np.array([[2,41, [2,8], (2.01, [8.4], [8,8], [8,0]))
# K-Means model

kmeans = KMeans(n_clusters=2, init='random', n_init=1, max_iter=10,
random_state=42)
kmeans. fit(X)

CO-3 ; # Outputs

BL3 print("Cluster centroids:\n", kmeans.cluster_centers_) [10]

print("Cluster assignments:", kmeans.labels_)

Manual methods will add to EXCEL

O Centroids: Compare final positions from manual iterations vs sklearn.

O Cluster assignments: Check if the points grouped similarly in both methods.

O Observation: ;

Both manual and sklearn K-Means generally converge to two vertical clusters:
points with x=2 in one cluster, points with x=8 in the other.

Minor differences may occur due to initialization choice.
````
