# Applied Machine Learning: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 042543859612

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Applied Machine Learning/ANS_Applied Machine Learning(703DB0C049)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Applied Machine Learning
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary.
8. Figures in brackets on the right hand side indicate full marks.
Q1   Answer briefly:   [20]
CO- 1; SO-   a.   •   Supervised Learning   [5]
1 ; BL-2
•   Unsupervised Learning
•   Reinforcement Learning
•   Batch vs Online (Continuous) Learning
•   Instance-based vs Model-based Learning
CO-2 ; SO-   b. Z-Score / IQR to detect extreme values   [5]
3; BL-3
Remove outlier rows
Winsorization (capping at percentiles)
Replace extremes with boundary values, capping
CO-3 ; SO-   c. Bias: 1 marks, Varinec: 1, Trade off:2 marks, 1 marks requriment   [5]
2; BL-2
CO-2 ; SO-   d. An activation function is a mathematical function in a neural network   [5]
2 ; BL-2   that decides whether a neuron should be “activated” or not, allowing the
network to learn complex, non-linear patterns.
• Sigmoid: outputs 0–1, used in binary classification.
• ReLU: outputs 0 for negatives, linear for positives, used in deep
networks.
• Tanh: outputs –1 to 1, often used in hidden layers.
Maeks neural networks more powerful than simple linear models.
Q2   Forward Propogation: 5 marks   [20]
Backward first layer 5 amrks
********** 1 **********
--- page 2 ---
CO-2; SO-   Backward second layer 5 marks
2; BL-5
Final equation 5 marks
Q3   • Impute missing values (median/mean for numerical, mode for   [20]
categorical).
CO-1; SO-
2;   • Transform skewed features (log transformation for Area & Rent).
BL-6   • Encode categorical variables (one-hot or binary encoding).
• Scale numerical features if required.
• Handle outliers if extreme deviations remain.
• Code will have 10 marks and all above 2 marks each
Q4   Evalutaion Matrix   [20]
CO-3; SO-
Metric   Description   Use Case / Insight
2;
Mean Absolute   Average absolute   Less sensitive to outliers;
BL-6
Error (MAE)   difference between   interpretable in ₹ directly
predicted and actual values
Mean Squared   Average squared   Penalizes large errors
Error (MSE)   difference between   heavily; useful if large
predicted and actual values deviations are costly
Root Mean   Square root of MSE   Same units as target;
Squared Error   interpretable
(RMSE)
R² Score   Proportion of variance   Measures goodness of fit; 1
explained by the model   = perfect, 0 = no fit
• Use MAE if you want robust performance ignoring extreme
outliers.
• Use RMSE to penalize models that make large errors.
• R² helps compare how well different models explain variance.
Codes will have 5 marks for 2 models each and evaluation matrix
definition and codes for the models will have 10 Marks.
Random Forest
•   Strengths: Handles non-linear relationships, robust to outliers,
minimal hyperparameter tuning.
• Weaknesses: Can be less precise for skewed targets, slower for
very large datasets.
➢ Gradient Boosting
➢ Strengths: Handles skewed data well, often better predictive
performance.
➢ Weaknesses: Sensitive to overfitting if not tuned, longer training
time.
➢ Model Selection:
• Compare RMSE and R² for both models.
•   If RMSE is lower and R² higher in one model → choose that.
********** 2 **********
--- page 3 ---
•   Optionally, perform hyperparameter tuning (GridSearchCV) to
optimize performance.
Q5   1. Reinforcement Learning (RL) 10 marks   [20]
RL is a type of ML where an agent learns by interacting with an
CO-3; SO-
environment to maximize cumulative reward. Unlike supervised learning, it
2;
learns from trial and error, not labeled data.
BL-5
Key difference from other ML:
•   Supervised: Learns from labeled data.
• Unsupervised: Finds patterns without labels.
• RL: Learns optimal actions from rewards.
2.Deep Q-Network (DQN) 10 marks
DQN uses a neural network to approximate Q-values for actions in given
states, enabling RL in high-dimensional spaces.
Key Components:
• Q-Network: Predicts Q-values.
• Experience Replay: Stores past transitions for stable training.
• Target Network: Provides stable targets, updated periodically.
Algorithm (simplified):
1. Initialize Q-network, target network, and replay buffer.
2. For each step: take action (ε-greedy), store (s,a,r,s').
3. Sample mini-batch, compute target y = r + γ max Q_target(s',a').
4. Update Q-network, periodically update target network.
Applications:   Games,   robotics,   autonomous   driving,   trading.
Advantages:   Handles   high-dimensional   inputs,   stable   learning.
Limitations: Computationally heavy, sensitive to hyperparameters,
struggles with continuous actions.
Q 6   Reason   Explanation   [20]
CO-2; SO-   Reduced   Combining multiple models reduces the effect of
2;   Variance   outliers or noise.
BL-3   Reduced Bias   Boosting models sequentially correct mistakes of
prior models.
Better   More robust predictions on unseen data.
Generalization
Handles   Can model non-linear relationships better than
Complexity   single models.
1. Random Forest (RF)
Features:
• Bagging-based ensemble of decision trees.
• Reduces variance by averaging predictions.
• Handles non-linear data well.
• Robust to outliers and overfitting compared to a single tree.
********** 3 **********
--- page 4 ---
Algorithm (Simplified):
1. Take n bootstrap samples from the dataset.
2. Train a decision tree on each sample.
3. At each node, choose the best split from a random subset of
features.
4. For prediction:
o Regression: Average outputs of all trees.
o Classification: Majority vote of all trees.
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
# Initialize and train model
rf   =   RandomForestRegressor(n_estimators=100,   max_depth=10,
random_state=42)
rf.fit(X_train, y_train)
# Predict and evaluate
y_pred = rf.predict(X_test)
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
2. Gradient Boosting (GBM / XGBoost)
Features:
•   Sequential ensemble where each tree corrects errors of previous
trees.
• Reduces bias while controlling variance.
• Handles skewed and complex datasets effectively.
• Requires careful tuning of learning rate and tree depth.
Algorithm (Simplified):
1. Initialize model with a constant prediction.
2. For n iterations:
o Compute residuals (errors) of current model.
o   Fit a new tree to residuals.
o Update   predictions:   prediction +=   learning_rate *
new_tree_prediction.
3. Final prediction is the sum of all tree predictions.
import xgboost as xgb
from sklearn.metrics import mean_squared_error
xg_reg = xgb.XGBRegressor(n_estimators=200, learning_rate=0.05,
max_depth=5, random_state=42)
xg_reg.fit(X_train, y_train)
y_pred = xg_reg.predict(X_test)
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
Unsupervised Approach for Fraud Detection   [20]
Q 7
CO-3; SO-   Goal: Cluster similar transactions and detect anomalies.
2;
********** 4 **********
--- page 5 ---
BL-6   Algorithm Choice:
•   Clustering: K-Means or DBSCAN (group similar transactions).
• Anomaly Detection: Isolation Forest or Local Outlier Factor (flag
unusual transactions).
Preprocessing:
• Scale numerical features (Purchase_Amount, Purchase_Time).
• Encode   categorical   features   (Product_Category,
Payment_Method).
•   Optional: cyclic transform for Purchase_Time using sin/cos.
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest
preprocessor = ColumnTransformer([
('num', StandardScaler(), ['Purchase_Amount', 'Purchase_Time']),
('cat',OneHotEncoder(drop='first'),['Product_Category',
'Payment_Method']
])
X = preprocessor.fit_transform(df)
# Clustering
clusters = DBSCAN(eps=0.5, min_samples=5).fit_predict(X)
df['Cluster'] = clusters
# Anomaly Detection
df['Anomaly']   =   IsolationForest(contamination=0.01,
random_state=42).fit_predict(X)
********** 5 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 6c5bbaf08bea

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Applied Machine Learning/ANS_Applied Machine Learning(703DB0C049)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: Applied Machine Learning
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary.
8. Figures in brackets on the right hand side indicate full marks.
Q1   Answer briefly:   [20]
CO- 1; SO-2 ;   a. A learning curve plots model performance (e.g., accuracy or error) on training and   [5]
BL-2   validation sets against the size of the training dataset.It shows how the model
learns as more data is provided.
Scenario   Training   Validation   Interpretation
Error   Error
High Bias   High   High   Model is too simple; adding
(Underfitting)   more data won’t help much.
Need a more complex model.
High Variance   Low   High   Model memorizes training data;
(Overfitting)   adding more data or
regularization can help reduce
variance.
Good Fit   Low   Low   Model generalizes well; balanced
bias and variance.
CO-2 ; SO- 3;   b. Importance of Feature Scaling:   [5]
BL-3   Ensures all features contribute equally in distance-based models (KNN, SVM, K-
Means).
Helps gradient-based models converge faster.
Prevents bias in regularized models (Ridge, Lasso).
Common Scaling Techniques:
Min-Max Scaling: Scales to [0,1].
Standardization (Z-score): Mean=0, Std=1.
Robust Scaling: Uses median/IQR, handles outliers.
Max Abs Scaling: Scales to [-1,1] based on max absolute value.
CO-3 ; SO- 2;   c.   Supervised, unsupervised, semi-supervised, reinforcement learning, model based,   [5]
BL-2   instance based, continuous and batch
CO-2 ; SO-2 ;   d. Combines Momentum and RMSProp, adapting learning rates for each parameter   [5]
BL-2   using first and second moment estimates.
Advantages: Faster convergence, handles sparse gradients, and requires less
tuning than standard gradient descent.
********** 1 **********
--- page 2 ---
Q2   Forward Propogation: 5 marks   [20]
CO-2; SO-2;   Backward first layer 5 amrks
BL-5   Backward second layer 5 marks
Final equation 5 marks
Q3   Step   Feature / Type   Method / Action   [20]
CO-1; SO-2;   Missing Values   Blood Pressure,   Impute with median
BL-6   Cholesterol (Numerical)
Smoking_Status   Impute with mode
(Categorical)
Skewness &   Blood Pressure,   Apply log transformation
Outliers   Cholesterol
Categorical   Smoking_Status,   One-hot encoding
Encoding   Exercise_Level
Target Encoding   Disease_Risk   Label encoding (High=1,
Low=0)
Feature Scaling   Age, BMI, Blood Pressure,   StandardScaler
Cholesterol
Class Imbalance   Disease_Risk (target)   SMOTE or class weights
Q4   1. Evaluation Metrics for Classification   [20]
CO-3; SO-2;   Metric   Description   Use Case
BL-6   Accuracy   Correct predictions /   Works for balanced datasets
total predictions
Precision   True Positives /   Minimizes false positives
Predicted Positives   (important in disease prediction)
Recall   True Positives / Actual   Minimizes false negatives (critical
(Sensitivity)   Positives   for detecting high-risk patients)
F1-Score   Harmonic mean of   Balances precision and recall,
precision & recall   useful for imbalanced datasets
ROC-AUC   Area under ROC curve   Measures model’s discrimination
ability
Inference:Since the target is imbalanced (High=20%), Recall, F1-Score, and ROC-
AUC are more important than raw accuracy.
Choice of Advanced ML Models
Random Forest Classifier
Ensemble of decision trees, robust to overfitting, handles non-linear relationships.
XGBoost Classifier
Gradient boosting model, handles imbalanced data well, often high predictive
performance.
Prioritize Recall and F1-Score for detecting high-risk patients.
Use cross-validation to tune hyperparameters.
XGBoost often performs slightly better for imbalanced, structured data, but
Random Forest is easier to implement and interpret.
********** 2 **********
--- page 3 ---
Q5   i. Reinforcement Learning (RL):   [10]
CO-2; SO-2;   RL involves an agent interacting with an environment to maximize cumulative
BL-3   rewards.
Algorithm (Q-Learning, simple version):
Initialize Q(s, a) table arbitrarily.
For each episode:
Observe current state sss
Choose action aaa using policy (e.g., ε-greedy)
Take action, observe reward rrr and next state s′s's′
Update Q-value:
[10]
Q 6   [20]
CO-3; SO-   i. Ridge vs Lasso Regularization:   [10]
2;BL-4   Comparison & Overfitting Control:
Ridge (L2): Adds squared magnitude of coefficients as penalty. Shrinks
coefficients, reduces overfitting, but none are set to zero.
Lasso (L1): Adds absolute value of coefficients as penalty. Can shrink some
coefficients to zero, performing feature selection.
Scenario & Justification:
Use Ridge when all features are relevant but may cause overfitting.
Use Lasso when some features are irrelevant or sparse.
Use Elastic Net (L1 + L2) when features are correlated, combining benefits of both.
Enhancements:
Cross-validation to tune regularization parameter λ\lambdaλ.
Feature scaling for stability.
Initialize w, b
for i in range(max_iter):
y_pred = X.dot(w) + b
********** 3 **********
--- page 4 ---
error = y_pred - y
if regularization == "ridge":
w_grad = (X.T.dot(error) + lambda * w)/n
elif regularization == "lasso":
w_grad = (X.T.dot(error) + lambda * sign(w))/n
w = w - learning_rate * w_grad
b = b - learning_rate * mean(error)
ii. Random Forest Algorithm:
Explanation & Key Components:
Ensemble method using bagging (bootstrap aggregating) to build multiple decision
trees.
Key components:   [10]
Random sampling of data for each tree
Random subset of features at each split
Aggregation of predictions (majority vote for classification, average for regression)
Typical Uses:
Classification and regression tasks
High-dimensional datasets
Handles missing values and unbalanced data
Algorithm (High-level):
For each tree:
Sample data with replacement (bootstrap)
Select random subset of features at each split
Train decision tree on the sampled data
Aggregate predictions from all trees for final output
for i in range(num_trees):
sample = bootstrap(data)
tree = train_decision_tree(sample, random_features)
forest.append(tree)
def predict(forest, X):
predictions = [tree.predict(X) for tree in forest]
return aggregate(predictions) # majority vote or mean
Q 7   [20]
CO-3; SO-2;   i. Customer Segmentation using K-Means Clustering   [10]
BL-3   Design & Steps:
Data Collection: Gather customer data (e.g., demographics, purchase history,
website activity).
Preprocessing: Handle missing values, scale/normalize features, encode
categorical variables.
K-Means Clustering:
Choose number of clusters kkk (using Elbow or Silhouette method).
Initialize centroids randomly.
Assign each customer to the nearest centroid.
Recalculate centroids and repeat until convergence.
Interpretation: Analyze cluster characteristics (e.g., high spenders, occasional
buyers).
Application in Marketing:
Targeted campaigns for each cluster.
Personalized promotions and product recommendations.
Customer retention strategies for high-value segments.
# X = preprocessed customer data
********** 4 **********
--- page 5 ---
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)
labels = kmeans.labels_ # cluster assignments
centroids = kmeans.cluster_centers_
i. Anomaly Detection Workflow
Workflow Steps:
Data Collection & Preprocessing: Handle missing values, normalize data, encode
categorical features.
Model Selection: Choose unsupervised anomaly detection methods (e.g., Isolation
Forest, One-Class SVM, Autoencoders).   [10]
Training: Fit model to normal data to learn patterns.
Detection: Flag data points significantly deviating from learned patterns as
anomalies.
Comparison with Supervised Learning:
Supervised learning requires labeled anomaly data.
Anomaly detection works when labels are scarce or unknown.
Integration:
Feed anomalies into broader analytics pipeline (fraud detection, predictive
maintenance, or monitoring).
Combine with reporting, alerts, and business decision support.
from sklearn.ensemble import IsolationForest
model = IsolationForest(contamination=0.05)
model.fit(X) # X = preprocessed dataset
anomalies = model.predict(X) # -1 = anomaly, 1 = normal
********** 5 **********
````
