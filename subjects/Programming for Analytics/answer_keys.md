# Programming for Analytics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 843bd496bd47

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Programming for Analytics/ANS_Programming for Analytics(703DB0C048)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Programming for Analytics
Date: 28 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a.   Purpose: Converts between Python objects and JSON (JavaScript Object Notation) —
useful for data exchange with APIs.
Example:
import json
CO-1;
data = {"name": "Alice", "age": 25}   [5]
SO-2;
json_str = json.dumps(data)   # dict → JSON string
BL-1   print(json_str)
py_dict = json.loads(json_str) # JSON string → dict
print(py_dict)
b   Feature   Bar Plot   Box Plot   [5]
CO-3;   Purpose Compare categorical values Show distribution summary
SO-2;
Displays Heights = mean/count   Median, quartiles, outliers
BL-2
Use Case Sales per region   Salary spread per department
c   Concept: Allows a child class to inherit attributes and methods from a parent class.   [5]
Single-level Example:
class Animal:
CO-1;   def speak(self):
SO-2;
print("Animal sound")
BL-1
class Dog(Animal):
def bark(self):
********** 1 **********
--- page 2 ---
print("Woof!")
d = Dog()
d.speak() # inherited
d.bark()
CO-   d   Task   Type   Output   Example   [5]
4,5;   Regression   Supervised   Continuous Predict house price
SO-2;   Classification Supervised   Categorical Spam or Not
BL-1   Clustering   Unsupervised Groups   Customer segmentation
a.   def mae(y_true, y_pred):
Q2   return sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)
CO-
[10]
1,4;   y_true = [4, 2.5, 3.5, 6]
SO-2;
y_pred = [3.5, 2, 4, 5.5]
BL-6
print(mae(y_true, y_pred)) # Output: 0.375
b.   Idea: Choose optimal k (number of clusters) where adding more clusters gives   [10]
Q2   minimal improvement.
Steps:
CO-5;
1. Run K-Means for different k (e.g., 1–10).
SO-2;
2. Compute SSE (Sum of Squared Errors) for each k.
BL-1   3. Plot k vs SSE.
4. The “elbow” point (sharp bend) indicates optimal k.
a.   import pandas as pd   [10]
Q3
CO-2;   df = pd.read_csv('sales.csv')
SO-2;   df['date'] = pd.to_datetime(df['date'])
BL-3   total_rev = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
print(total_rev)
Q3   b.   [10]
Type Penalty Term   Effect
CO-4;
SO-2;   Ridge L2 = λΣw²   Shrinks weights, keeps all features
BL-2   Lasso L1 = λΣ   w
a.   import matplotlib.pyplot as plt   [10]
import numpy as np
x = np.linspace(0, 2*np.pi, 100)
fig, axes = plt.subplots(2,1, figsize=(6,6))
Q4
CO-3;   axes[0].plot(x, np.sin(x))
SO-2;   axes[0].set_title("Sine Wave")
BL-3   axes[0].set_xlabel("x"); axes[0].set_ylabel("sin(x)")
axes[1].plot(x, np.cos(x))
axes[1].set_title("Cosine Wave")
axes[1].set_xlabel("x"); axes[1].set_ylabel("cos(x)")
plt.tight_layout(); plt.show()
********** 2 **********
--- page 3 ---
b.   class BankAccount:   [10]
def __init__(self, holder_name, balance=0):
self.holder_name = holder_name
self.balance = balance
def deposit(self, amount):
Q4   self.balance += amount
CO1;   def withdraw(self, amount):
SO-2;   if amount <= self.balance:
BL-2   self.balance -= amount
else:
print("Insufficient funds!")
acc = BankAccount("Ravi", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.balance) # 1200
a.   import seaborn as sns   [10]
Q5   import matplotlib.pyplot as plt
CO-
iris = sns.load_dataset('iris')
3,4;
sns.lmplot(x='sepal_length', y='petal_length', hue='species', data=iris)
SO-2;   plt.show()
BL-6   Interpretation: Petal length increases with sepal length; slope differs by species,
showing clear separation.
b.   Purpose: Visualize correlations among numeric features.   [10]
Q5   corr = iris.corr()
CO-3;   sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
SO-2;
Interpretation: Strong positive correlation between petal_length and petal_width →
BL-2   these increase together.
a.   Principal Component Analysis (PCA)   [10]
•   Purpose: Reduce dimensionality while preserving maximum variance.
•   Benefits:
Q6   o   Faster training due to fewer features.
o   Easier visualization (2D/3D).
CO-5;
•   Steps:
SO-2;
o   Standardize data.
BL-1   o Compute covariance matrix.
o Find eigenvectors/eigenvalues.
o   Select top-k eigenvectors (principal components).
o   Project data onto them.
b.   from sklearn.datasets import load_iris   [10]
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
Q6
CO-5;   X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
SO-2;
BL-3   clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)
print("Tree depth:", clf.get_depth())
print("Accuracy:", accuracy_score(y_test, clf.predict(X_test)))
********** 3 **********
--- page 4 ---
a.   Feature   API   Web Scraping   [10]
Q7
Data   Structured (JSON/XML) Unstructured (HTML)
CO-1;
Ease   Easy & legal   Complex, may violate TOS
SO-2;
BL-2   Example Lib requests, httpx   BeautifulSoup, Scrapy
Use Case   Twitter API for tweets   Extracting product prices from websites
b.   import requests   [10]
Q7
url = "https://jsonplaceholder.typicode.com/users"
CO1-;   data = requests.get(url).json()
SO-2;
BL-6   for user in data:
if user['company']['name'] == "Romaguera-Crona":
print(user['name'], "-", user['email'])
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper f3d36b230aed

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Programming for Analytics/ANS_Programming for Analytics(703DB0C048)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (3 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: Programming for Analytics
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a.   •   Purpose: Simplifies sending HTTP/HTTPS requests in Python (GET, POST,
PUT, DELETE) and handling responses.
•   Difference from urllib: requests is higher-level, more user-friendly, handles
sessions, cookies, and JSON easily. urllib is lower-level, more verbose,
CO-1;   requires manual encoding/decoding.
SO-2;   import requests   [5]
BL-1
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()
print(data)
b   Histogram: Discrete bins, shows frequency/count.   [5]
CO-3;   KDE (Kernel Density Estimate): Smooth probability density function, shows
SO-2;
distribution trend.
BL-2
Use case: Histogram for counts/frequency; KDE for visualizing distribution shape.
c   __init__ method in Python   [5]
•   Role: Initializes object attributes when a class instance is created.
class Person:
CO-1;   def __init__(self, name, age):
SO-2;   self.name = name
BL-1   self.age = age
p = Person('Alice', 25)
print(p.name, p.age)
CO-4,5; d   Classification: Supervised, labels known. Example: Predict spam email.   [5]
SO-2;
********** 1 **********
--- page 2 ---
BL-1   Clustering: Unsupervised, groups without labels. Example: Customer segmentation.
a.   import math
Q2   def rmse(y_true, y_pred):
CO-1,4;   return math.sqrt(sum((yt - yp)**2 for yt, yp in zip(y_true, y_pred)) / len(y_true))   [10]
SO-2;
BL-6   y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
print(rmse(y_true, y_pred)) # Output: 0.612372
b.   K-Means++ Initialization   [10]
•   Definition: Smart initialization to choose initial centroids far apart to improve
convergence.
Q2
• Why preferred: Reduces likelihood of poor local minima compared to
CO-5;   random.
SO-2;   •   Steps:
BL-1   1. Choose first centroid randomly.
2. Compute distance of each point to nearest centroid.
3. Choose next centroid with probability ∝ distance².
4. Repeat until k centroids are chosen.
a.   import pandas as pd   [10]
Q3
df = pd.read_csv('transactions.csv')
CO-2;
SO-2;   df['date'] = pd.to_datetime(df['date'])
BL-3   total_per_user = df.groupby('user_id')['amount'].sum().sort_values(ascending=False)
print(total_per_user.head(3))
Q3   b.   Low complexity: High bias, low variance → underfitting.   [10]
CO-4;   High complexity: Low bias, high variance → overfitting.
SO-2;
BL-2   Goal: Balance complexity for best generalization.
a.   import matplotlib.pyplot as plt   [10]
import numpy as np
x = np.random.randn(100)
Q4   y = np.random.randn(100)
CO-3;
SO-2;   fig, axes = plt.subplots(1,2, figsize=(10,4))
BL-3   axes[0].scatter(x, y)
axes[0].set_title('Scatter plot')
axes[1].hist(x, bins=10)
axes[1].set_title('Histogram')
plt.show()
b.   class Inventory:   [10]
def __init__(self, name, qty):
self.name = name
Q4   self.qty = qty
CO1;
def restock(self, amount):
SO-2;
self.qty += amount
BL-2
item = Inventory('Pen', 10)
item.restock(5)
print(item.qty) # Output: 15
********** 2 **********
--- page 3 ---
a.   import seaborn as sns   [10]
Q5
import matplotlib.pyplot as plt
CO-3,4;
SO-2;   tips = sns.load_dataset('tips')
BL-6   sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips)
plt.show()
Q5   b.   [10]
• Conveys: Median, quartiles, min/max, outliers.
CO-3;   •   Outliers: Points beyond Q1-1.5*IQR or Q3+1.5*IQR.
SO-2;   sns.boxplot(x=tips['total_bill'])
BL-2   plt.show()
a.   PCA   [10]
•   Definition: Dimensionality reduction method to find orthogonal components
Q6
capturing maximum variance.
CO-5;   •   Steps (2-D example):
SO-2;   1. Center data by subtracting mean.
BL-1   2. Compute covariance matrix.
3. Compute eigenvectors/eigenvalues.
4. First principal component = eigenvector with largest eigenvalue.
b.   from sklearn.neighbors import KNeighborsClassifier   [10]
Q6
features = [[1,2],[2,1],[3,4],[4,3]]
CO-5;   labels = [0,0,1,1]
SO-2;
BL-3   knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(features, labels)
print(knn.predict([[2.5,2.5]])) # Output: [1]
Q7   a.   API: Structured data, reliable, officially provided. Example: Weather API.   [10]
CO-1;   Web scraping: Extracts unstructured HTML when API unavailable. Example:
SO-2;
BL-2   Scraping product prices.
b.   import requests   [10]
Q7
CO1-;   url = 'https://jsonplaceholder.typicode.com/todos'
SO-2;   data = requests.get(url).json()
BL-6   titles = [item['title'] for item in data if item['userId'] == 2]
print(titles)
********** 3 **********
````
