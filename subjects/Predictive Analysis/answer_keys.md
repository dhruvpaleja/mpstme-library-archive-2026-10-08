# Predictive Analysis: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 1a8d2a4bc1f2

- Departments: AI and Data Science, Data Science
- Programmes: BTech AIDS 7056, Integrated DS 7038, MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_AIDS_7056/Predictive Analysis/ANS_Predictive Analysis(702DB0E003)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (22 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III/ V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Predictive Analysis
Date: 08 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
9. The marks distribution is given for reference, may be changed as per the pattern of the given ans.
Q1   Answer briefly:   [20]
CO-1; SO-1;   a. Explain the SEMMA methodology used in SAS Enterprise Miner. Briefly   [05]
BL-2   describe each of its five stages. How this process helps in building
reliable and accurate predictive models.
ANS:
SEMMA is a data mining methodology developed by SAS and widely used
in SAS Enterprise Miner. The term SEMMA stands for Sample, Explore,
Modify, Model, and Assess. It provides a systematic and structured approach
for building reliable and accurate predictive models by guiding the user   01x5
through all essential stages of data mining.
Five Stages of SEMMA
1. Sample
•   In this stage, a representative subset of the data is selected from a
large dataset.
• Sampling reduces computational cost while preserving important
patterns.
• Data is often divided into training, validation, and testing sets.
Purpose:
Ensures efficient processing and prevents overfitting by working on
manageable and representative data.
2. Explore
********** 1 **********
--- page 2 ---
• The data is explored using descriptive statistics and visualization
techniques.
•   Identifies outliers, missing values, trends, and relationships among
variables.
Purpose:
Helps in understanding data behavior and detecting issues that may affect
model performance.
3. Modify
• Data is transformed to improve model quality.
•   Operations include handling missing values, normalization, feature
selection, binning, and variable creation.
Purpose:
Prepares clean and meaningful input data, improving the predictive power of
models.
4. Model
•   Different data mining algorithms such as regression, decision trees,
neural networks, and clustering are applied.
•   Multiple models are created and tuned using training and validation
data.
Purpose:
Identifies patterns and relationships to predict outcomes effectively.
5. Assess
• Model performance is evaluated using metrics like accuracy, ROC
curves, lift charts, and error rates.
• Models are compared to select the best-performing one.
Purpose:
Ensures the selected model is reliable, accurate, and generalizable to new
data.
SEMMA Helps in Building Reliable and Accurate Predictive Models
•   Provides a step-by-step framework that reduces errors and bias.
• Encourages data understanding before modelling, improving decision
quality.
•   Supports model comparison and validation, ensuring robustness.
• Helps prevent overfitting and underfitting through proper assessment.
• Ensures models are interpretable, scalable, and deployment-ready.
Apply the pruning process in SAS Enterprise Miner to a fully grown Decision
CO-2; SO-1;   b. Tree. Describe the key steps involved in selecting and deriving the optimal tree   [05]
BL-3   model.
ANS:
********** 2 **********
--- page 3 ---
Steps to Prune a Fully Grown Decision Tree in SAS Enterprise Miner
1. Build the Maximal Tree: Create a fully grown decision tree using all   03
possible splits; this tree may overfit the data.
2. Select a Pruning Method: Choose a method such as Cost-Complexity
Pruning or Minimum Error Pruning.
3. Evaluate Node Statistics: Examine metrics like misclassification rate
or Gini index to identify less important branches.
4. Apply Pruning Criteria: Remove branches that do not significantly
improve predictive accuracy, often using validation data.
5. Validate and Select Optimal Tree: Compare performance metrics
before and after pruning; choose the tree that balances simplicity and
accuracy.
Outcome:
A smaller, more generalizable tree that performs well on unseen data
and avoids overfitting.
02
Explanation of the Fig related to Pruning.
CO-1; SO-1;   c. Describe how the graph of the “Age” variable was created in SAS Enterprise   [05]
BL-2   Miner. What does the graph represent, and how does it help you understand
the distribution of the “Age” variable? Identify the number of bins used and
explain what the shape of the distribution suggests about the dataset.
********** 3 **********
--- page 4 ---
ANS: (Process of Graph Creation)
01x5
1. The figure is a histogram created by grouping the “Age” variable
into intervals called bins and plotting the frequency of values in each
bin.
2. The x-axis shows age intervals, and the y-axis shows the count of
individuals in each interval.
3. The histogram represents the distribution of Age, showing which
age groups are most common, whether the distribution is skewed, and
if there are any outliers.
4. This graph uses around 50 bins to divide the age range.
5. Insights: Most ages fall within certain intervals, indicating dominant
age groups; the spread of bars shows variability, and isolated bars
may indicate outliers.
CO-4; SO-1;   d. Analyze   [05]
BL-3,4   the limitation of input selection in neural network models and explain how
using a regression node before the neural network can address this problem.
ANS:
Limitation of Input Selection in Neural Networks and Role of Regression
Node
02
1. Limitation – Input Selection:
• Neural networks are sensitive to the choice of input
features.
•   Irrelevant, redundant, or poorly scaled inputs can reduce
accuracy, increase training time, and lead to overfitting.
• This limitation is often called input selection incapability
because the network cannot automatically identify the most
important predictors.
2. Solution – Using a Regression Node:
• A regression node can be applied before the neural network
to preprocess input features.   1.5
•   It helps by:
▪   Identifying the most relevant variables for
predicting the target.
********** 4 **********
--- page 5 ---
▪ Transforming or scaling inputs to improve neural
network performance.
• This ensures that the neural network receives clean,
important, and appropriately scaled inputs, improving
predictive accuracy and convergence.
3. Impact on Model Performance:
1.5
• Reduces overfitting and training time.
• Improves generalization to unseen data.
• Helps the neural network focus on meaningful patterns
rather than noise.
Input selection is a key limitation of neural networks. Using a
regression node prior to the network mitigates this problem by
filtering and preprocessing inputs, leading to more accurate and
efficient models.
Q2   Demonstrate the Model essential’s part with reference to the given figure
CO-2; SO-1;   a. of Predict New Cases for the Predictive Model in detail with the help of   [10]
BL-3,4   sketches.
ANS:
Demonstration of the Model Essentials in “Predict New Cases” for a   03x3
Predictive Model
The “Predict New Cases” node in a predictive model allows users to
generate predictions for new or unseen data using a trained model. The
Model Essentials part of this process typically includes three main
prediction types:
1. Rankings: (Figure Require)
• Assigns a rank or priority to predicted outcomes.
• Useful when you want to order cases based on predicted
probability or likelihood.
********** 5 **********
--- page 6 ---
• Example Sketch: A table with cases ranked from highest to
lowest predicted probability.
2. Estimates: (Figure Require)
• Provides the numerical prediction for each case.
• For continuous targets, it gives predicted values (e.g., sales,
age).
• For categorical targets, it provides predicted class
probabilities.
• Example Sketch: A chart showing predicted values vs.
actual values for selected cases.
3. Inputs, Prediction, Decisions: (Figure Require)
•   Inputs: Shows the original values of the input variables
used for prediction.
•   Prediction: Displays the predicted outcome for each case.
• Decisions: Includes actions or recommendations based on
predicted outcomes (e.g., approve/reject, yes/no).
• Example Sketch: A table with columns for input variables,
predicted value, and suggested decision.
Process Demonstration:   01
• The trained model takes new cases as input.
•   Predictions are generated according to the model type (e.g.,
regression, classification).
• Model Essentials summarizes the key outputs for each case in
terms of ranking, estimates, and decision-making.
•   Visualizations or sketches help interpret and communicate results
clearly.
Q2   How can you import a dataset from your PC/Laptop for analysis? Explain
CO-1; SO-1;   b. the process step by step with reference to the given figure as one step out of   [10]
BL-3   many. Also explain how to create the New Project. Mention the procedure in
detail.
ANS: (The real Process of creation is required.)
2.5x
Importing a Dataset and Creating a New Project in SAS Viya
4
1. Creating a New Project:
********** 6 **********
--- page 7 ---
• Open SAS Viya and navigate to the Projects tab.
•   Click on New Project.
•   Provide a project name and optional description.
•   Select the location to save the project.
•   Click Create to initialize the project workspace.
2. Importing a Dataset from PC/Laptop:
•   In the project workspace, click Import Data.
• Browse and select the dataset file from your PC or Laptop (e.g.,
CSV, Excel).
• Follow the import wizard to specify:
• Data source (local file).
•   File format (CSV, XLSX, etc.).
• Delimiter or sheet selection if required.
•   Click Next to preview the data.
3. Setting Role Properties (Step 2):
• The right pane in SAS Viya allows you to set the role of each
variable:
•   Input: Predictor variables for modeling.
•   Target: Dependent variable to predict (e.g., churn).
• ID: Unique identifier for each record.
• Other roles (e.g., reject, partition) as needed.
•   Scroll through the variable list to locate the churn variable and assign
it as the Target.
•   Adjust other variables’ roles according to your analysis plan.
4. Finalizing Import:
•   After setting roles, click Finish or Import.
• The dataset is now available in the project for analysis and modeling.
Q3   Explain the Forward Selection process used for input (variable) selection
CO-2; SO-1;   a.   in a Regression Model. Describe step-by-step how variables are added to   [10]
BL-3   the model, including the criteria used for selection (such as R², AIC, or p-
values). Illustrate your answer with an example showing how the model
evolves as new predictors are included.
Forward Selection Process in Regression Model (Figure)
Forward Selection is a stepwise variable selection technique used in
regression modeling to identify the most significant predictors for the
target variable. The process starts with no input variables in the model
and adds them one by one based on statistical significance or
improvement in model performance.
********** 7 **********
--- page 8 ---
Step-by-Step Procedure:   07
1. Start with No Variables:
• Begin with an empty model containing only the intercept
(no predictors).
2. Evaluate Each Predictor:
• Test each independent variable individually by fitting a
simple regression model.
• Measure performance using criteria such as R², Adjusted
R², Akaike Information Criterion (AIC), or p-values.
3. Select the Best Variable:
• Choose the variable that provides the most significant
improvement in the model (highest R² or lowest AIC/p-
value).
4. Add Variable to the Model:
• Include this variable in the model and fix it as part of the
regression equation.
5. Repeat the Process:
• Test the remaining variables one by one in combination
with the selected variables.
• Continue adding variables that significantly improve the
model.
6. Stopping Criteria:
• The process stops when no additional variable improves the
model significantly, or when the improvement in R² or
reduction in AIC becomes negligible.
Example:
Suppose we have a dataset with a target variable Y (Sales) and three   03
predictors — X₁ (Advertising Spend), X₂ (Price), and X₃ (Store Size).
Final Model:
Y = β₀ + β₁X₁ + β₂X₂ + ε
Q3   Explain the Model Essential Optimize Complexity of a Neural Network model
CO-4; SO-1;   b. and describe, in simple terms, how the Stopped Training method helps in
BL-2   optimizing model complexity using the fit statistic.
ANS: (Explanation is required)   [10]
Fit Statistic: Expiation
********** 8 **********
--- page 9 ---
02x5
Explain the above given diagrams.
Q4   Explain in brief about any two problem solving methods from the given
CO2; SO-1;   a.   figure:   [10]
BL-2,3
ANS:
Problem-Solving Methods from Regressions: Beyond the Prediction
Formula
********** 9 **********
--- page 10 ---
From the given figure, three key problem-solving methods are:
Regression analysis is not limited to generating predictions. Effective
problem-solving using regression requires addressing data quality issues and
correctly understanding model behaviour. Two important problem-solving
methods are explained below.
05x2
1. Managing Missing Values
Managing missing values is a critical problem-solving step in regression
analysis. Real-world datasets often contain incomplete or missing data due to
errors in data collection, non-responses, or system failures. If missing values
are not handled properly, they can lead to biased models and inaccurate
predictions.
Techniques
• Removing rows or columns with missing values
• Imputing missing values using mean, median, or mode
• Using advanced techniques such as regression imputation or k-NN
imputation
Importance
• Ensures data completeness and consistency
• Improves model accuracy and reliability
•   Prevents loss of important information
Thus, managing missing values helps build a stable and trustworthy
regression model.
2. Interpreting the Model
Interpreting the regression model is another key problem-solving method. It
involves understanding the relationship between independent variables and
the dependent variable, rather than focusing only on predictions.
Aspects
•   Interpreting regression coefficients to understand variable influence
• Analyzing statistical significance (p-values)
• Understanding goodness-of-fit measures such as R²
Importance
• Helps explain why predictions occur
•   Supports decision-making and business insights
• Ensures the model aligns with domain knowledge
Proper model interpretation transforms regression from a black-box predictor
into a meaningful analytical tool.
********** 10 **********
--- page 11 ---
3. Handling Extreme or Unusual Values
Extreme or unusual values, also known as outliers, are data points that differ
significantly from other observations in the dataset. These values may occur
due to data entry errors, measurement faults, or genuine rare events. In
regression analysis, outliers can strongly influence the regression line and
distort model accuracy.
Techniques
•   Identifying outliers using box plots, z-scores, or IQR method
• Removing incorrect or irrelevant extreme values
• Transforming variables (log, square root) to reduce the impact of
extreme values
• Using robust regression techniques that reduce sensitivity to outliers
Importance
•   Prevents biased or misleading regression results
• Improves model stability and predictive accuracy
• Ensures the regression model reflects true data patterns
Handling extreme or unusual values is essential to ensure that regression
models are reliable and not dominated by a few abnormal observations.
Method   Purpose
Managing missing   Ensures complete and reliable data
values
Interpreting the model   Provides insights beyond prediction
Handling extreme   Prevents distortion and improves
values   accuracy
Q4   Discuss the importance of statistical graphics in the assessment of models
CO-3; SO-1;   b. citing two examples of statistical graphics and their use. Also, give an   [10]
BL-2, 3   example of profit matrix and its significance in decision making.
ANS: (Give Examples with all three)
********** 11 **********
--- page 12 ---
1. Importance of Statistical Graphics in Model Assessment
Statistical graphics help visualize and interpret data and model performance,   06
making complex patterns easier to understand. They allow analysts to identify
trends, anomalies, relationships, and model accuracy clearly and intuitively.
Examples and Uses:
1. ROC Curve (Receiver Operating Characteristic Curve):
•   Plots True Positive Rate vs. False Positive Rate for classification
models.
• Example: Suppose a model predicts whether customers will
respond to a marketing campaign. By varying the prediction
threshold (e.g., 0.5, 0.7, 0.9), TPR and FPR are calculated and
plotted.
• Use: Assesses the model’s discrimination ability and helps select
an optimal threshold.
2. Cumulative Lift Chart:
• Measures how much better the model is at predicting positive
outcomes compared to random selection.
• Example: In a campaign with 1000 customers, the top 10% of
predicted responders might contain 50 actual responders. Lift =
(Response rate in top 10%) / (Average response rate).
• Use: Helps prioritize top customers for targeted campaigns,
quantifying improvement over random targeting.
2. Profit Matrix and Its Significance
A Profit Matrix (or cost-benefit matrix) assigns monetary values to correct and
incorrect predictions, linking model performance to business outcomes.
Example of Profit Matrix for a Binary Classification Problem:
04
Significance:
•   Helps determine decision thresholds that maximize expected profit.
•   Guides resource allocation by prioritizing actions with higher returns.
•   Translates model performance into financial impact, not just accuracy
metrics.
Q5   Evaluate the use of K-Means clustering for customer segmentation. Discuss
CO-5; SO-1;   a.   its benefits, drawbacks, and how it can influence business decisions. Explain   [10]
BL-5   with an example.
ANS:
********** 12 **********
--- page 13 ---
Evaluation of K-Means Clustering for Customer Segmentation
02
K-Means clustering is an unsupervised machine learning algorithm widely
used for customer segmentation. It groups customers into K distinct clusters
based on similarity in their attributes such as age, income, purchase
behavior, and frequency of visits. Each customer belongs to the cluster with
the nearest mean (centroid).
Benefits of K-Means for Customer Segmentation
1. Simplicity and Efficiency   02
K-Means is easy to understand and implement. It works efficiently
even with large customer datasets.
2. Scalability
The algorithm performs well for large-scale data, making it suitable
for organizations with millions of customers.
3. Clear Segment Formation
Produces well-defined, non-overlapping customer groups, which are
easy to interpret and act upon.
4. Supports Targeted Marketing
Helps businesses design personalized offers and marketing
campaigns for each customer segment.
Drawbacks of K-Means Clustering
02
1. Need to Predefine K
The number of clusters must be chosen in advance, which may not
always be obvious.
2. Sensitivity to Outliers
Extreme values can distort cluster centroids and affect segmentation
quality.
3. Assumes Spherical Clusters
K-Means works best when clusters are of similar size and shape,
which may not reflect real customer behavior.
4. Initial Centroid Dependency
Different initial centroids can lead to different clustering results.
Influence on Business Decisions
K-Means clustering helps organizations:
•   Identify high-value customers   01
• Design personalized marketing strategies
• Improve customer retention
• Optimize pricing and promotions
•   Allocate resources efficiently to profitable segments
These insights lead to data-driven and customer-centric business decisions.
Example
Retail Store Customer Segmentation
********** 13 **********
--- page 14 ---
A retail company applies K-Means clustering on customer data using
features such as:
• Annual income   03
• Spending score
• Purchase frequency
After analysis, the customers are grouped into four clusters:
1. High-income, high-spending customers
2. Low-income, low-spending customers
3. Price-sensitive frequent shoppers
4. Occasional buyers
Business Impact
• Premium products are promoted to high-income clusters.
• Discount offers target price-sensitive customers.
•   Loyalty programs are introduced for frequent shoppers.
This segmentation improves sales, customer satisfaction, and marketing
efficiency.
OR
Example:
A retail store segments customers based on annual spending and purchase
frequency:
•   Cluster 1: High spenders, frequent buyers → premium offers
•   Cluster 2: Moderate spenders, occasional buyers → loyalty discounts
•   Cluster 3: Low spenders, rare buyers → introductory promotions
This segmentation helps the company design strategies to maximize
engagement and revenue.
K-Means clustering is a powerful and practical technique for customer
segmentation. While it has limitations such as sensitivity to outliers and
dependency on the number of clusters, its simplicity, scalability, and ability
to support strategic decision-making make it highly valuable in business
analytics.
Q5   Explain how model features are explored during the scoring of a Champion
CO-3; SO-1;   b. Model and describe the sequential steps involved in the Model Scoring   [10]
BL-4   process using the SAS platform.
ANS: (SAS Viya Process)
In SAS, the process of exploring model features for scoring and performing
model scoring for the Champion Model is an essential part of model
deployment and operationalization. SAS provides a unified analytical   05x2
********** 14 **********
--- page 15 ---
environment that simplifies the transition from model training to production
scoring through its visual and automated tools.
1. Exploring Model Features for Scoring in SAS
Before scoring, it is important to explore and validate the input features of
the Champion Model to ensure consistent and accurate predictions. This
process involves:
•   Feature Validation:
Confirm that all required input variables used during model training
are present in the scoring dataset.
• Data Type Consistency:
Check that variable types (numeric, categorical, date, etc.) in the
scoring data match those expected by the Champion Model.
•   Transformation Synchronization:
Ensure that all transformations (like standardization, encoding, or
binning) performed in the training phase are also applied to the
scoring dataset.
• Handling Missing Values:
Apply the same missing value imputation rules used during model
building to avoid scoring errors.
•   Feature Importance Analysis:
In SAS tools such as Model Studio and SAS Visual Data Mining and
Machine Learning (VDMML), feature importance plots can be
viewed to understand how each input affects model predictions.
• Champion Model Verification:
The selected Champion Model is verified in the Model Repository to
ensure it represents the best-performing model based on validation
metrics like AUC, RMSE, or Misclassification Rate.
2. Steps of the Model Scoring Procedure in SAS
• Access the Model Repository:
Open Model Studio or Model Manager in SAS. Identify and select
the Champion Model from the model comparison results.
• Prepare the Scoring Data:
Load the new dataset (for prediction) into the SAS environment.
Ensure that the data structure aligns with the model’s input schema.
• Generate Score Code:
SAS automatically creates the scoring code (in SAS language, DS2,
or other supported formats). This code can be reviewed or
customized before deployment.
• Use the Scoring Node or Pipeline:
In Model Studio, connect the Score Node to the Champion Model
pipeline and configure scoring settings — such as output variables
(predicted probabilities, class labels, or residuals).
• Execute Scoring:
Run the scoring process in the SAS environment. The model’s
scoring logic is executed efficiently, allowing for high-performance
predictions even on large datasets.
• Review Scored Output:
Access the scored output dataset. Examine predictions, probabilities,
and decision outcomes using SAS visualization tools.
********** 15 **********
--- page 16 ---
• Model Monitoring and Deployment:
The scored model can be deployed through SAS Model Manager for
real-time or batch scoring. The model’s performance is monitored
continuously to detect drift or performance degradation.
Example:
Suppose a Champion Logistic Regression Model predicts customer churn.
• A new customer dataset is loaded into SAS.
• The Score Node is used to apply the model and generate churn
probabilities.
•   Results show customers with a churn probability >0.7 as high-risk.
• The scoring code is then deployed to production using SAS Model
Manager for live prediction.
Conclusion:
In SAS, the Champion Model Scoring process ensures automation, accuracy,
and transparency. By maintaining proper feature validation, transformation
consistency, and seamless deployment, SAS enables efficient and scalable
model operationalization for predictive analytics across industries.
Q6   Explain the working of the DMNeural Model by discussing its key model
CO-4; SO-1;   a.   essentials - Predict New Cases, Select Useful Inputs, and Optimize   [10]
BL-4,   Complexity. Additionally, outline the major steps involved in the DM Neural
algorithm.
ANS:
The DM Neural Model in SAS Enterprise Miner is a powerful predictive
modeling tool that combines neural network principles with regression-based
learning to deliver accurate and flexible predictions. It is designed to
automatically select useful inputs, optimize model complexity, and generate
reliable predictions through a multi-stage prediction formula.
Model Essentials of DM Neural
1. Predict New Cases   02x3
The DM Neural model creates a multi-stage prediction formula that is used
to score new or unseen data.
• At each stage, the model fits a regression equation based on
transformed principal components (PCs) of the input data.
• The residuals (errors from the previous stage) are used to refine
predictions in subsequent stages, improving accuracy progressively.
********** 16 **********
--- page 17 ---
•   This stagewise prediction process helps in capturing complex,
nonlinear relationships between input variables and the target
variable.
2. Select Useful Inputs
Instead of directly using all input variables, DMNeural employs Principal
Component Analysis (PCA) to identify the most relevant features.
• The model transforms the original inputs into principal components
(uncorrelated linear combinations of the original features).
• Out of all PCs, up to three principal components with the highest
target R² (correlation with the target) are selected.
•   This approach reduces multicollinearity, removes redundant
variables, and simplifies the model without losing predictive power.
3. Optimize Complexity
Model complexity in DMNeural is controlled by the number of stages in the
multi-stage prediction formula.
• Each stage improves the prediction by modeling the residuals left by
the previous stage.
•   Typically, three stages are used, balancing model accuracy and
generalization.
•   This prevents overfitting while maintaining flexibility in modeling
complex relationships.
Steps of the DMNeural Algorithm
1. Principal Component Transformation:
Transform all input variables into principal components (orthogonal
transformations of inputs).   04
2. Component Selection:
Select up to three PCs with the highest correlation (R²) with the target
variable.
3. Transformation Selection:
Apply one of eight nonlinear transformations (Square, Tanh,
Arctangent, Logistic, Gaussian, Sine, Cosine, or Exponential) to the
selected PCs.
The transformation that produces the best fit statistic (minimum
squared error) is chosen.
4. Regression Modeling:
Fit a regression model using the selected principal components and
their transformations to predict the target variable.
5. Residual Computation:
Compute residuals — the difference between actual and predicted
target values.
6. Stagewise Repetition:
Repeat the process (usually up to three stages) using residuals as new
targets, improving accuracy at each stage.
********** 17 **********
--- page 18 ---
7. Final Model Formation:
Combine the results from all stages to create the final multi-stage
prediction formula, which can be used to score new cases.
Q6   Explain the concept of ensemble models in SAS Enterprise Miner. Compare
CO-3; SO-1;   b. bagging, boosting, and model averaging techniques, highlighting how Start   [10]
BL-5   Groups and End Groups nodes are used to implement them. Additionally,
describe the role of the Ensemble node, explaining how it combines model
predictions using methods such as Average, Maximum, and Voting. Explain
with examples of scenarios where each ensemble approach is most effective.
ANS:
Ensemble models in SAS Enterprise Miner combine the results of multiple
models to improve prediction accuracy and robustness. Instead of relying on
a single model, ensembles reduce variance and bias by aggregating diverse
model outcomes.
1. Techniques of Ensemble Modeling:
05
• Bagging (Bootstrap Aggregating):
Multiple models are trained on random subsets of the data, and their
results are averaged. It helps reduce variance and is effective for
unstable models like decision trees.
Example: Customer churn prediction using multiple decision trees to
get stable outcomes.
•   Boosting:
Models are built sequentially, where each new model focuses on
correcting the errors of the previous one. It reduces bias and
improves predictive power but may risk overfitting.
Example: Credit risk classification or fraud detection.
• Model Averaging:
Combines predictions from different models (e.g., logistic regression,
neural networks, decision trees) by averaging or weighting their
outputs. It balances model strengths and weaknesses.
Example: Combining regression and neural networks for sales
forecasting.
2. Start Groups and End Groups Nodes:
In SAS Enterprise Miner, Start Groups and End Groups nodes define the
ensemble flow. The Start Groups node initiates parallel model training, while   02
the End Groups node aggregates model results for ensemble evaluation.
3. The Ensemble Node:
The Ensemble node is not a model itself; it combines predictions from
several models using one of the following methods:
• Average: Takes the mean of prediction estimates (default method).
• Maximum: Selects the highest prediction estimate across models.
•   Voting:
• Average Method: Averages estimates from models predicting   02
the primary outcome.
********** 18 **********
--- page 19 ---
• Proportion Method: Uses the proportion of models predicting
the primary outcome.
4. Summary of Effectiveness:   01
• Bagging → Reduces variance, useful for unstable learners.
• Boosting → Reduces bias, suitable for complex decision tasks.
• Model Averaging → Balances multiple model types, ideal when
models differ in structure.
Thus, ensemble modeling in SAS Enterprise Miner enhances accuracy,
generalization, and reliability of predictive analytics.
Q7   A retail store has recorded the following transactions from 10 customers:
CO-5; SO-1;   a.   [10]
BL-5   Transaction ID   Items Purchased
1   Milk, Bread
2   Milk, Diaper, Beer
3   Bread, Butter
4   Milk, Bread, Butter
5   Bread, Diaper
6   Milk, Bread, Diaper
7   Beer, Diaper
8   Milk, Bread, Butter
9   Milk, Bread, Diaper
10   Bread, Butter
Using this dataset, identify how support, confidence, and lift can be
calculated to find associations such as {Milk} ⇒ {Bread}. Evaluate that
how these measures contribute to understanding patterns in Market Basket
Analysis and suggest actionable insights for the store.
ANS:
********** 19 **********

[Text in pictures on this page, read by OCR]
We are analyzing the association rule {milk} > {Bread} using support, confidence, and lift to
understand purchase patterns.

Step 1: Calculate Support
Support measures how frequently the item set appears in the transactions.

Transactions containing both Milk and Bread
Total Transactions

Support(Milk > Bread) =

From the dataset: Transactions with both Milk and Bread = 1, 4, 6, 8, 9 — 5 transactions.
Total transactions = 10

Support = — = 0.5 (50%)

7
--- page 20 ---
02x3
Step 4: Interpretation   02
• Support (50%): Half of all transactions include both Milk and Bread.
• Confidence (83.3%): If a customer buys Milk, there is an 83.3%
chance they also buy Bread.
•   Lift (1.04): Slight positive correlation; Milk slightly increases the
likelihood of Bread purchase, but the effect is modest.
Actionable Insights for the Store:
• Milk and Bread could be promoted together as a combo product or   02
placement strategy.
•   Since lift is just above 1, further analysis with other items could
reveal stronger associations for cross-selling.
Q7   Briefly explain the concepts of Accuracy and Misclassification in the
CO-2; SO1;   b. Decision Tree’s Decision Optimization process.   [05]
BL-2
ANS:
In the Decision Tree’s Decision Optimization process, Accuracy and
Misclassification are key measures used to evaluate the performance of the
model:
02
• Accuracy: It represents the proportion of correctly classified cases
(both true positives and true negatives) out of the total number of
cases. Higher accuracy indicates that the decision tree is correctly
predicting outcomes for most observations.
********** 20 **********

[Text in pictures on this page, read by OCR]
Step 2: Calculate Confidence

Confidence measures how often Bread is purchased when Milk is purchased.

Transactions containing both Milk and Bread
Transactions containing Milk

Confidence(Milk > Bread) =

Transactions with Milk = 1, 2, 4, 6, 8, 9 - 6 transactions

5

Confidence = 5 = 0.833 (83.3%)

Step 3: Calculate Lift

Lift measures how much more likely Bread is purchased with Milk compared to its baseline frequency.

Confidence(Milk > Bread)

Lift(Milk + Bread) = Support (Bread)

Transactions with Bread = 1, 3, 4, 5, 6, 8, 9, 10 — 8 transactions

Support(Bread) = = =0.8

, _ 0.833 _
Lift = > ~ 1.04
--- page 21 ---
•   Misclassification: This is the proportion of cases that are incorrectly
classified by the decision tree. It measures the error rate and is
complementary to accuracy.
02
Usage:
These metrics help in evaluating how well the decision tree model predicts
outcomes and in optimizing splits or pruning to improve predictive   01
performance.
Example:
If a decision tree predicts 90 correct outcomes and 10 incorrect outcomes out
of 100 cases:
• Accuracy = 90/100 = 90%
•   Misclassification = 10/100 = 10%
Higher accuracy and lower misclassification indicate a better-optimized
decision tree model.
Q7
CO-2; SO1;   c. Explain in brief about the logistic Regeression Model Prediction Formula.   [05]
BL-2   Also identify the type of Targate variable.
ANS:
Explanation of the following figure:
Introduction
Logistic Regression is a supervised machine learning algorithm used for
classification problems, especially when the outcome is categorical. Unlike
linear regression, logistic regression predicts the probability that an instance
belongs to a particular class.
Logistic Regression Prediction Formula
The logistic regression model uses the logistic (sigmoid) function to convert
a linear combination of input features into a probability value between 0 and
1.
Prediction Formula
********** 21 **********
--- page 22 ---
Type of Target Variable
The target variable in logistic regression is:
Categorical (Discrete)
• Most commonly Binary
Examples: Yes/No, 0/1, Pass/Fail, Fraud/Not Fraud
• Can be extended to multiclass classification using multinomial
logistic regression
Example
Predicting whether a customer will purchase a product:
•   Target Variable:
• 1 → Purchase
• 0 → Not Purchase
Logistic regression predicts the probability of purchase based on features
such as age, income, and browsing time.
********** 22 **********

[Text in pictures on this page, read by OCR]
1

P(Y=1|X)= 1p ee MX Ma)

Where:

+ P(Y =1) X) = probability that the target variable belongs to class 1
» B=
* Bi, Bo,-..,
e X,,Xo,...,X, = independent variables
« e= base of the natural logarithm

intercept (bias term)

8, = model coefficients

Explanation of the Formula
1. The expression

Bo + BX +++++ BaXn

represents a linear combination of inputs.
2. The sigmoid function transforms this linear value into a probability between 0 and 1.
3. Adecision threshold (usually 0.5) is applied:
e If probability = 0.5 — Class 1
e If probability < 0.5 — Class 0
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 240a653df3e9

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/Predictive Analysis/ANS_Predictive Analysis(702DB0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. TECH (CSE - DS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Predictive Analysis
Date: 02 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A bank wants to classify loan approval (Yes/No) based on an attribute
“Income Level”:
Income Level   Yes No
High   4   1
Medium   3   2
Low   2   3
Compute the Gini Index for this split and interpret whether it is a good split.
CO- 2;
SO- 1;   [5]
BL-2
********** 1 **********

[Text in pictures on this page, read by OCR]
High:
Gini = 1 — (0.8? + 0.27) = 0.32

Medium:

Gini = 1 — (0.6? + 0.47) = 0.48
Low:

Gini = 1 — (0.4 + 0.67) = 0.48
Weighted:

x0. 32) + 75 °-(0. 48) + 2. (0.48) — 0.426
--- page 2 ---
b.   Given the following dataset representing the number of hours studied (X)
and the final exam score (Y) for 5 students:
Student   Hours Studied (X)   Exam Score (Y)
1   2   50
2   3   60
3   5   80
4   7   85
5   8   95
Calculate the slope (m) and intercept (c) for the linear regression line   Y
= mX + c using the least squares method.
CO-2;
SO-1;   [5]
BL-2
c.   Explain the Perceptron model. Describe its structure, working, and
CO- 4;
SO- 1   activation function.   [5]
BL- 2
MODEL – 5 MARKS
d.   Define Model Fit Statistics and explain their importance.
Model Fit Statistics are quantitative measures used to evaluate how well a
statistical model fits the observed data. They compare actual and predicted
CO- 3;   values to assess accuracy.   [5]
SO- 2
BL- 5
Importance:
• Help in selecting the best model
• Measure prediction accuracy
********** 2 **********

[Text in pictures on this page, read by OCR]
Compute sums

Sox =25, SOY =370
Sox? = 151, SO XY = 2035
n=5
Calculate slope m
__ 5(2035) — (25)(370)
5(151) — (25)?

1 —
_ 10175~9250 925
755-625 130

Calculate intercept c

370 — (7.115 x 25)
7
5
370 — 177.875 192.125
_ _

= 38.425
5 5
--- page 3 ---
•   Detect overfitting or underfitting
• Ensure model reliability
A A company wants to decide whether to approve a loan based on the
following dataset:
ID   Income   Credit   Student   Loan
Score   Approved
1   High   Good   No   No
2   High   Good   Yes   No
3   Medium   Good   No   Yes
4   Low   Fair   No   Yes
Q2
CO-2;   5   Low   Poor   Yes   Yes   [10]
SO-2;
6   Low   Poor   No   No
BL-3
7   Medium   Poor   Yes   Yes
8   High   Fair   No   No
9   High   Poor   Yes   Yes
10   Low   Fair   Yes   Yes
Construct a decision tree for the above dataset.
B   You are given summary statistics (not raw data) for a dataset with 10
observations:
𝑛= 10
∑𝑋= 50
∑𝑌= 60
∑𝑋𝑌= 350
∑𝑋2 = 300
Using the standard least squares formulas, calculate the slope 𝛽1and intercept
CO-2;   𝛽0of the simple linear regression line. Then write the final regression equation.
SO-2;   Step 1: Use the formula for the slope   [10]
BL-3   𝑛∑𝑋𝑌−(∑𝑋)(∑𝑌)
𝛽1 =
𝑛∑𝑋2 −(∑𝑋)2
Substitute values:
Numerator:
𝑛∑𝑋𝑌−(∑𝑋)(∑𝑌) = 10 ⋅350 −50 ⋅60
= 3500 −3000 = 500
********** 3 **********
--- page 4 ---
Denominator:
𝑛∑𝑋2 −(∑𝑋)2 = 10 ⋅300 −502
= 3000 −2500 = 500
So,
500
𝛽1 =   = 1
500
Step 2: Compute the intercept
Formula:
𝛽0 = 𝑌ˉ −𝛽1𝑋ˉ
Compute means:
50
𝑋ˉ = = 5
10
60
𝑌ˉ = = 6
10
Now:
𝛽0 = 6 −(1)(5) = 1
✅ Final Regression Equation
𝑌̂ = 1 + 1𝑋
Q3   A   Explain the concept of pruning in decision trees. Why is pruning necessary?
CO-2;   Compare pre-pruning and post-pruning techniques with suitable   [10]
SO-2;
BL-3   examples.
B   Design and implement a Perceptron model to realize the logic function of
CO-4;   an AND gate.
SO-2;   [10]
BL-4   Activation function: step function
Bias weight = 0.4, w1 = 0.3 , w2 = -0.2 , Bias = 1 and learning rate = =0.2
Q4   A   Explain the difference between Batch GD, Stochastic GD, and Mini-Batch
CO-2;   GD.   [10]
SO-2;
Each comparison – 2 marks
BL-3
B A teacher trains a model using polynomial regression of degree 12 to
predict student exam scores from hours studied.
The training accuracy is extremely high (98%), but test accuracy is very
CO-4;   poor (62%).
SO-2;   The model gives unrealistic wavy curves. Identify the issue and explain   [10]
BL-4   why it happens.
Solution:
The model is experiencing overfitting.
• Polynomial of degree 12 is too complex for a simple relationship.
********** 4 **********
--- page 5 ---
•   It memorizes noise, random fluctuations, and outliers in the training
set.
• Training accuracy is high → low bias.
•   Test accuracy is low → high variance.
A   Explain the geometric interpretation of Lasso and Ridge regularization.
Why does Lasso frequently result in exact zero weights, acting as an
implicit feature selector, while Ridge does not?
Q5   Lasso (L1) uses a diamond-shaped constraint region. Ridge (L2) uses a
CO-2;   circular constraint region. The corners of the L1 diamond often intersect the
[10]
SO-2;   loss contours, producing exact zero coefficients, making Lasso a feature
BL-3   selector. Ridge shrinks weights smoothly but never forces them to zero
because the circular constraint has no sharp corners. Lasso → sparse
solution; Ridge → smooth shrinking.
B A real estate company wants to predict house prices based on:
•   Size (in sq. ft.)
• Number of bedrooms
They build simple and multiple regression models and want to evaluate which
model fits better using model fit statistics.
House   Size (X₁)   Bedrooms (X₂)   Actual Price (Y) (₹
lakhs)
CO-3;
SO-2;   1   1000   2   50   [10]
BL-5
2   1200   2   55
3   1500   3   65
4   1800   3   80
5   2000   4   90
Q6   A
Discuss Cross Validation and K Fold Cross Validation.
CO-5;   [10]
SO-2;
BL- 4
CO-1; B   Discuss Missing Values, Imputation methods(Manual & Algorithm based) and
SO-1   advantages & Limitations.   [10]
BL- 2
********** 5 **********
--- page 6 ---
Missing values refer to the absence of data in one or more fields of a dataset.
These are commonly represented as NULL, NaN, blank cells, or special symbols.
Causes:
• Data entry mistakes
•   Sensor/device failure
•   Non-response in surveys
• Data corruption during transfer
Missing values can reduce model accuracy and may introduce bias if not handled
properly.
2. Imputation Methods (6 Marks)
A) Manual Methods (3 Marks)
These methods are simple and directly applied by the analyst.
i) Mean / Median / Mode Imputation
• Mean: used for numerical continuous data
• Median: preferred when data contains outliers
• Mode: used for categorical data
Example:
If ages = 20, 25, NaN, 30
Mean = 25 → replace NaN with 25
ii) Constant Value Imputation
Replace missing values with fixed values like:
• 0
• “Unknown”
• “Not Available”
iii) Row/Column Deletion
Remove rows or columns having too many missing values.
B) Algorithm-Based Methods (3 Marks)
These use machine learning/statistical algorithms.
i) KNN Imputation
Uses nearest similar records to estimate missing values.
ii) Regression Imputation
Predicts missing values using regression models based on other features.
********** 6 **********
--- page 7 ---
iii) Multiple Imputation / Iterative Imputation
Generates multiple estimates and selects the most reliable value.
3. Advantages & Limitations (2 Marks)
Advantages:
• Improves data completeness
•   Better model training
• Reduces data loss
Limitations:
• Can introduce bias
• Mean imputation reduces variance
• Wrong method may distort relationships in data
A   What is Market Basket Analysis? Explain its importance in data mining.
Describe the concept of association rules, including support, confidence, and
lift. Illustrate the process with a suitable example and explain how it helps in
decision-making in retail businesses.
Answer:
Definition
Market Basket Analysis (MBA) is a data mining technique used to identify
relationships between items purchased together by customers.
It is based on association rule learning.
Importance
• Helps retailers understand customer buying behavior
• Improves product placement and cross-selling strategies
• Used in recommendation systems (e.g., Amazon, Flipkart)
•   Increases sales and customer satisfaction
Q7
CO-3;   [10]
SO-1;
BL-4   Association Rules Concept
An association rule is of the form:
X⇒Y
Where:
• X: Antecedent (if part)
• Y: Consequent (then part)
Key Measures
1. Support
• Frequency of occurrence of itemset
Transactions containing (X ∪Y)
Support(X ⇒Y) =
Total Transactions
********** 7 **********
--- page 8 ---
2. Confidence
• Likelihood that Y is purchased when X is purchased
Support (X ⇒Y)
Confidence(X ⇒Y) =
Support(X)
3. Lift
• Measures strength of rule
•   Lift > 1 → Strong association
Confidence (X ⇒Y)
Lift(X ⇒Y) =
Support(Y)
B   Explain the complete model implementation methodology in a data science
project.
CO-5;   • Data preparation
SO-1;   • Model building   [10]
BL-4
• Validation techniques
• Deployment
• Monitoring and maintenance
********** 8 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 6e8cebafb118

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7057/Predictive Analysis/ANS_Predictive Analysis(702DB0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. TECH (CSE - DS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Predictive Analysis
Date: 02 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A bank wants to classify loan approval (Yes/No) based on an attribute
“Income Level”:
Income Level   Yes No
High   4   1
Medium   3   2
Low   2   3
Compute the Gini Index for this split and interpret whether it is a good split.
CO- 2;
SO- 1;   [5]
BL-2
********** 1 **********

[Text in pictures on this page, read by OCR]
High:
Gini = 1 — (0.8? + 0.27) = 0.32

Medium:

Gini = 1 — (0.6? + 0.47) = 0.48
Low:

Gini = 1 — (0.4 + 0.67) = 0.48
Weighted:

x0. 32) + 75 °-(0. 48) + 2. (0.48) — 0.426
--- page 2 ---
b.   Given the following dataset representing the number of hours studied (X)
and the final exam score (Y) for 5 students:
Student   Hours Studied (X)   Exam Score (Y)
1   2   50
2   3   60
3   5   80
4   7   85
5   8   95
Calculate the slope (m) and intercept (c) for the linear regression line   Y
= mX + c using the least squares method.
CO-2;
SO-1;   [5]
BL-2
c.   Explain the Perceptron model. Describe its structure, working, and
CO- 4;
SO- 1   activation function.   [5]
BL- 2
MODEL – 5 MARKS
d.   Define Model Fit Statistics and explain their importance.
Model Fit Statistics are quantitative measures used to evaluate how well a
statistical model fits the observed data. They compare actual and predicted
CO- 3;   values to assess accuracy.   [5]
SO- 2
BL- 5
Importance:
• Help in selecting the best model
• Measure prediction accuracy
********** 2 **********

[Text in pictures on this page, read by OCR]
Compute sums

Sox =25, SOY =370
Sox? = 151, SO XY = 2035
n=5
Calculate slope m
__ 5(2035) — (25)(370)
5(151) — (25)?

1 —
_ 10175~9250 925
755-625 130

Calculate intercept c

370 — (7.115 x 25)
7
5
370 — 177.875 192.125
_ _

= 38.425
5 5
--- page 3 ---
•   Detect overfitting or underfitting
• Ensure model reliability
A A company wants to decide whether to approve a loan based on the
following dataset:
ID   Income   Credit   Student   Loan
Score   Approved
1   High   Good   No   No
2   High   Good   Yes   No
3   Medium   Good   No   Yes
4   Low   Fair   No   Yes
Q2
CO-2;   5   Low   Poor   Yes   Yes   [10]
SO-2;
6   Low   Poor   No   No
BL-3
7   Medium   Poor   Yes   Yes
8   High   Fair   No   No
9   High   Poor   Yes   Yes
10   Low   Fair   Yes   Yes
Construct a decision tree for the above dataset.
B   You are given summary statistics (not raw data) for a dataset with 10
observations:
𝑛= 10
∑𝑋= 50
∑𝑌= 60
∑𝑋𝑌= 350
∑𝑋2 = 300
Using the standard least squares formulas, calculate the slope 𝛽1and intercept
CO-2;   𝛽0of the simple linear regression line. Then write the final regression equation.
SO-2;   Step 1: Use the formula for the slope   [10]
BL-3   𝑛∑𝑋𝑌−(∑𝑋)(∑𝑌)
𝛽1 =
𝑛∑𝑋2 −(∑𝑋)2
Substitute values:
Numerator:
𝑛∑𝑋𝑌−(∑𝑋)(∑𝑌) = 10 ⋅350 −50 ⋅60
= 3500 −3000 = 500
********** 3 **********
--- page 4 ---
Denominator:
𝑛∑𝑋2 −(∑𝑋)2 = 10 ⋅300 −502
= 3000 −2500 = 500
So,
500
𝛽1 =   = 1
500
Step 2: Compute the intercept
Formula:
𝛽0 = 𝑌ˉ −𝛽1𝑋ˉ
Compute means:
50
𝑋ˉ = = 5
10
60
𝑌ˉ = = 6
10
Now:
𝛽0 = 6 −(1)(5) = 1
✅ Final Regression Equation
𝑌̂ = 1 + 1𝑋
Q3   A   Explain the concept of pruning in decision trees. Why is pruning necessary?
CO-2;   Compare pre-pruning and post-pruning techniques with suitable   [10]
SO-2;
BL-3   examples.
B   Design and implement a Perceptron model to realize the logic function of
CO-4;   an AND gate.
SO-2;   [10]
BL-4   Activation function: step function
Bias weight = 0.4, w1 = 0.3 , w2 = -0.2 , Bias = 1 and learning rate = =0.2
Q4   A   Explain the difference between Batch GD, Stochastic GD, and Mini-Batch
CO-2;   GD.   [10]
SO-2;
Each comparison – 2 marks
BL-3
B A teacher trains a model using polynomial regression of degree 12 to
predict student exam scores from hours studied.
The training accuracy is extremely high (98%), but test accuracy is very
CO-4;   poor (62%).
SO-2;   The model gives unrealistic wavy curves. Identify the issue and explain   [10]
BL-4   why it happens.
Solution:
The model is experiencing overfitting.
• Polynomial of degree 12 is too complex for a simple relationship.
********** 4 **********
--- page 5 ---
•   It memorizes noise, random fluctuations, and outliers in the training
set.
• Training accuracy is high → low bias.
•   Test accuracy is low → high variance.
A   Explain the geometric interpretation of Lasso and Ridge regularization.
Why does Lasso frequently result in exact zero weights, acting as an
implicit feature selector, while Ridge does not?
Q5   Lasso (L1) uses a diamond-shaped constraint region. Ridge (L2) uses a
CO-2;   circular constraint region. The corners of the L1 diamond often intersect the
[10]
SO-2;   loss contours, producing exact zero coefficients, making Lasso a feature
BL-3   selector. Ridge shrinks weights smoothly but never forces them to zero
because the circular constraint has no sharp corners. Lasso → sparse
solution; Ridge → smooth shrinking.
B A real estate company wants to predict house prices based on:
•   Size (in sq. ft.)
• Number of bedrooms
They build simple and multiple regression models and want to evaluate which
model fits better using model fit statistics.
House   Size (X₁)   Bedrooms (X₂)   Actual Price (Y) (₹
lakhs)
CO-3;
SO-2;   1   1000   2   50   [10]
BL-5
2   1200   2   55
3   1500   3   65
4   1800   3   80
5   2000   4   90
Q6   A
Discuss Cross Validation and K Fold Cross Validation.
CO-5;   [10]
SO-2;
BL- 4
CO-1; B   Discuss Missing Values, Imputation methods(Manual & Algorithm based) and
SO-1   advantages & Limitations.   [10]
BL- 2
********** 5 **********
--- page 6 ---
Missing values refer to the absence of data in one or more fields of a dataset.
These are commonly represented as NULL, NaN, blank cells, or special symbols.
Causes:
• Data entry mistakes
•   Sensor/device failure
•   Non-response in surveys
• Data corruption during transfer
Missing values can reduce model accuracy and may introduce bias if not handled
properly.
2. Imputation Methods (6 Marks)
A) Manual Methods (3 Marks)
These methods are simple and directly applied by the analyst.
i) Mean / Median / Mode Imputation
• Mean: used for numerical continuous data
• Median: preferred when data contains outliers
• Mode: used for categorical data
Example:
If ages = 20, 25, NaN, 30
Mean = 25 → replace NaN with 25
ii) Constant Value Imputation
Replace missing values with fixed values like:
• 0
• “Unknown”
• “Not Available”
iii) Row/Column Deletion
Remove rows or columns having too many missing values.
B) Algorithm-Based Methods (3 Marks)
These use machine learning/statistical algorithms.
i) KNN Imputation
Uses nearest similar records to estimate missing values.
ii) Regression Imputation
Predicts missing values using regression models based on other features.
********** 6 **********
--- page 7 ---
iii) Multiple Imputation / Iterative Imputation
Generates multiple estimates and selects the most reliable value.
3. Advantages & Limitations (2 Marks)
Advantages:
• Improves data completeness
•   Better model training
• Reduces data loss
Limitations:
• Can introduce bias
• Mean imputation reduces variance
• Wrong method may distort relationships in data
A   What is Market Basket Analysis? Explain its importance in data mining.
Describe the concept of association rules, including support, confidence, and
lift. Illustrate the process with a suitable example and explain how it helps in
decision-making in retail businesses.
Answer:
Definition
Market Basket Analysis (MBA) is a data mining technique used to identify
relationships between items purchased together by customers.
It is based on association rule learning.
Importance
• Helps retailers understand customer buying behavior
• Improves product placement and cross-selling strategies
• Used in recommendation systems (e.g., Amazon, Flipkart)
•   Increases sales and customer satisfaction
Q7
CO-3;   [10]
SO-1;
BL-4   Association Rules Concept
An association rule is of the form:
X⇒Y
Where:
• X: Antecedent (if part)
• Y: Consequent (then part)
Key Measures
1. Support
• Frequency of occurrence of itemset
Transactions containing (X ∪Y)
Support(X ⇒Y) =
Total Transactions
********** 7 **********
--- page 8 ---
2. Confidence
• Likelihood that Y is purchased when X is purchased
Support (X ⇒Y)
Confidence(X ⇒Y) =
Support(X)
3. Lift
• Measures strength of rule
•   Lift > 1 → Strong association
Confidence (X ⇒Y)
Lift(X ⇒Y) =
Support(Y)
B   Explain the complete model implementation methodology in a data science
project.
CO-5;   • Data preparation
SO-1;   • Model building   [10]
BL-4
• Validation techniques
• Deployment
• Monitoring and maintenance
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper b527cbe1e291

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AIDS_7056/Predictive Analysis/ANS_Predictive Analysis(702DB0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Predictive Analysis
Date: 11 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. This question paper contains 4 pages.
3. Answer to each new question to be started on a fresh page.
4. Figure in right hand side indicates full marks
5. Question No. 1 is compulsory.
6. Out of remaining questions, attempt any 4 questions.
7. In all 5 questions to be attempted.
8. All questions carry equal marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1; SO-1;   a. Explain the SEMMA methodology used in SAS Enterprise Miner.   [05]
BL-2   Describe the main purpose of each of its five stages and explain how this
process supports the development of accurate predictive models.
ANS:
SEMMA is a methodology used in SAS Enterprise Miner for structured
data mining and predictive modeling. It consists of five stages:
01x5
1. Sample:
Select a representative portion of data that is large enough to
capture significant patterns but manageable for processing.
2. Explore:
Examine the data to identify trends, relationships, and anomalies,
helping to gain insights and guide modeling decisions.
3. Modify:
Prepare and transform the data by creating new variables, handling
missing values, and improving data quality to focus the modeling
process.
4. Model:
Apply statistical and machine learning techniques to generate
predictive models that capture patterns in the data.
5. Assess:
Evaluate and compare models using performance metrics to select
the most reliable and effective model.
How SEMMA Supports Accurate Predictive Models:
By following a systematic process, SEMMA ensures data quality,
********** 1 **********
--- page 2 ---
thorough exploration, proper preparation, and rigorous model evaluation,
which together enhance the accuracy, reliability, and robustness of
predictive models.
Discuss the procedure used by SAS E-Miner for building a decision tree
CO-2; SO-1;   b. model by considering two input variables in the dataset.   [05]
BL-3,
ANS:
Procedure for Building a Decision Tree with Two Input Variables in
SAS Enterprise Miner:
01x5
1. Prepare the Data: Import the dataset, identify the target and two
input variables, and ensure the data is clean.
2. Create Decision Tree Node: Drag the Decision Tree node into
the workspace and connect it to the Input Data node.
3. Configure Tree Settings: Specify the target, select the two input
variables, and choose a splitting criterion (e.g., Gini index or
entropy).
4. Grow the Tree: The algorithm evaluates splits for the two inputs
and recursively builds the tree until stopping criteria are met.
5. Prune the Tree (Optional): Remove branches that do not improve
predictive accuracy using validation data.
6. Evaluate and Select Optimal Tree: Examine performance metrics
and choose the tree that balances complexity and accuracy.
Outcome:
• A small, interpretable decision tree that predicts the target based
on the two input variables and shows their influence.
Explain how this figure was created and describe what the graph
CO-1; SO-1;   c.   represents. What does it show about the distribution of the “Median Home   [05]
BL-2   Value Region” variable in the dataset? How many bins are used in this
graph, and what insights can you draw from their distribution?
ANS:
********** 2 **********

[Text in pictures on this page, read by OCR]
Frequency of Median Home Value Region
Frequency

2,500
2,000
1,500
1,000

500

$100,000 $200,000 $300,000 $400,000 $500,000 $600,000
Median Home Value Region
--- page 3 ---
1. The figure is a histogram created by dividing the “Median Home
01x5
Value Region” variable into intervals called bins and plotting the
frequency of values in each bin.
2. The x-axis represents the ranges of median home values, and the y-
axis represents the count of regions falling into each range.
3. The histogram shows the distribution of median home values,
highlighting which value ranges are most common and whether the
distribution is skewed or uniform.
4. The graph uses 20+ bins to segment the data.
5. Insights:
Peaks indicate the most common median home value ranges. The spread of
bars shows variability among regions.
CO-4; SO-1;   d. Explain any two limitations of neural network models and propose a method   [05]
BL-3,4   or approach to address at least one of these limitations.
ANS:
Limitations of Neural Network Models and Possible Solutions
1. Limitation 1 – Input Selection Incapability:   02
• Neural networks may struggle if irrelevant or poorly
scaled input features are provided. This can lead to
overfitting or reduced predictive accuracy.
• Solution: Use a regression node or feature selection step
before the neural network to identify and preprocess   02
relevant inputs.
2. Limitation 2 – Lack of Interpretability:
• Neural networks are often “black boxes,” making it
difficult to understand how input variables influence
predictions.   01
• Solution: Apply explainable AI techniques (e.g., SHAP,
LIME) or consider simpler interpretable models for
critical applications.
Addressing input selection and interpretability improves the
effectiveness and usability of neural network models.
Q2   Demonstrate the Model essential’s part with reference to the given
CO-2; SO-1;   a. figure of optimize Complexity: Tune Models with Validate Data for the   [10]
BL-3,4   Predictive Model in detail with the help of sketches.
********** 3 **********
--- page 4 ---
ANS: (sketches)
02x5
Demonstration of the Model Essentials in “Optimize Complexity: Tune
Models with Validation Data”
The “Optimize Complexity” process in predictive modeling involves selecting
the model that balances complexity and predictive accuracy using training and
validation data. The Model Essentials part can be demonstrated as follows:
1. Model Selection:
•   Multiple models are trained on the training dataset with
varying levels of complexity (e.g., number of nodes in a
decision tree, number of neurons in a neural network).
• Complexity levels are labeled (e.g., 1, 2, 3, 4, 5) from simplest
to most complex.
2. Validation Assessment:
• Each model is evaluated on the validation dataset to measure
predictive performance (e.g., misclassification rate, RMSE).
•   This ensures that the selected model generalizes well to
unseen data and avoids overfitting.
3. Select Optimal Model:
• The goal is to choose the simplest model that achieves the
highest validation assessment.
• Simpler models are preferred for interpretability and
efficiency, provided their predictive performance is adequate.
4. Process Flow (Illustrative Sketch/Table):
• The sketch shows that as complexity increases; training performance
improves but validation performance may decline due to overfitting.
********** 4 **********

[Text in pictures on this page, read by OCR]
Model Selection

Training Data Validation Data

Select the simplest model with the Model
highest validation assessment. Complexity

Model Training Data Validation Decision

Complexity Performance Assessment

1 (Simplest) Moderate High Selected

2 High High Consider

3 Very High Moderate Reject
(Overfit)

4 Very High Low Reject
(Overfit)

5 (Most Complex) | Very High Low Reject

(Overfit)
--- page 5 ---
• The optimal model is the one with good validation performance and
minimal complexity.
Q2   How can you import a dataset from your PC/Laptop for analysis? Explain
CO-1; SO-1;   b. the process step by step with reference to the given figure as one step out   [10]
BL-3   of many. Also explain how to create the New Project. Mention the
procedure in detail.
2.5x4
ANS:
Importing a Dataset and Creating a New Project in SAS Viya / Model
Studio
1. Creating a New Project:
• Open SAS Model Studio.
•   Click on “New Project”.
•   Enter a Project Name and Description (optional).
• Choose the project type (e.g., predictive modeling, machine
learning).
•   Click Create to initialize the project workspace.
• The new project workspace will display steps, data sources, and
modeling nodes.
2. Importing a Dataset from PC/Laptop:
•   In the Data Source section, select Import Data.
• Browse your PC/Laptop to locate the dataset (CSV, Excel, or
supported file types).
•   Click Open to upload the dataset.
• The dataset is imported into CAS (Cloud Analytic Services),
making it available for analysis in SAS Visual Analytics and
Model Studio.
3. Specifying Role Properties (Step 2):
• Once the dataset is loaded, open the Variable Properties pane (right
side).
• Assign roles to variables:
********** 5 **********
--- page 6 ---
•   Input: Independent variables used for modeling.
•   Target: Dependent variable for prediction (e.g., churn).
• ID / By: Unique identifier variables for each row.
• You may need to scroll down in the variable list to find specific
variables like “churn.”
•   Adjust data types, measurement levels, and modeling options as
needed.
4. Completion:
•   After the import and role assignment, the dataset is ready for
further modeling steps (data exploration, feature selection,
modeling).
• You are returned to the Model Studio interface, where the dataset
appears as a node ready for analysis.
Notes:
• SAS Viya supports various data types; ensure compatibility with
CAS.
• Imported datasets in CAS are shared across SAS Visual Analytics
for downstream analysis.
Q3   Describe the Backward Selection process in Regression Modeling.
CO-2; SO-1;   a. Explain how variables are systematically removed from a full model, the   [10]
BL-3   statistical criteria applied for elimination, and how this process leads to an
optimal subset of predictors.
Support your explanation with a diagram or flow showing each stage of
backward selection.
Ans:
Backward Elimination in Regression Modeling
Backward Elimination is a stepwise variable selection technique that starts
with all available predictors in the model and then removes the least
significant variables one by one based on a chosen statistical criterion -
typically the p-value. The goal is to retain only those predictors that
contribute meaningfully to predicting the target variable.
Step-by-Step Procedure (using p-value as criterion)
06
1. Start with the Full Model:
•   Include all independent variables in the regression model.
•   This is the most complex model possible.
2. Compute Statistical Significance:
• For each predictor, calculate its p-value from the regression
output (based on t-statistics or F-tests).
• The p-value indicates whether a variable’s contribution to
explaining the target is statistically significant.
********** 6 **********
--- page 7 ---
3. Identify the Least Significant Variable:
• Find the variable with the highest p-value (least significant).
•   If the p-value is greater than the removal cutoff (e.g., 0.05 or
0.10), mark it for removal.
4. Remove the Variable:
• Exclude this variable from the model.
•   Refit the model with the remaining variables.
5. Repeat the Process:
•   Recalculate p-values for the updated model.
• Continue removing variables one by one until all remaining
variables have p-values below the cutoff threshold.
6. Stop and Finalize the Model:
• The final model is reached when no predictor exceeds the p-
value threshold, meaning all retained predictors are
statistically significant.
•   This subset of predictors is considered optimal for balancing
simplicity and accuracy.
Flow Diagram of Backward Elimination
Start → Full Regression Model (all variables)
↓   02
Calculate p-values for all predictors
↓
Is the largest p-value > cutoff (e.g., 0.05)?
↙   ↘
Yes   No
↓   ↓
Remove variable with   Stop process.
highest p-value.   Final model obtained.
↓
Refit model and repeat.
Example
Suppose we start with predictors X1, X2, X3, X4 for predicting Y.
Cutoff = 0.05.   02
Final Model:
Y=β0+β1X1+β3X3+ε
Q3   Explain in brief about the model essentials, Predict New Cases: Neural Network
CO-4; SO-1;   b.   Prediction Formula for Interval and binary targets.
BL-2
Ans:
[10]
Neural networks predict cases using a mathematical equation involving the values
of the input variables.
********** 7 **********
--- page 8 ---
05
A neural network can be thought of as a regression model on a set of derived inputs,
called hidden units. In turn, the hidden units can be thought of as regressions on the
original inputs. The hidden unit “regressions” include a default link function (in
neural network language, an activation function), the hyperbolic tangent. The
hyperbolic tangent is a shift and rescaling of the logistic function. Because of a neural
network’s biological roots, its components receive different names from
corresponding components of a regression model. Instead of an intercept term, a
neural network has a bias term. Instead of parameter estimates, a neural network has
weight estimates. What makes neural networks interesting is their ability to
approximate virtually any continuous association between the inputs and the target.
Simply specify the correct number of hidden units and find reasonable values for the
weights. Specifying the correct number of hidden units involves some trial and error.
Finding reasonable values for the weights is done by least squares estimation (for
interval-valued targets).
05
When the target variable is binary, as in the demonstration data, the main neural
network regression equation receives the same logit link function featured in logistic
regression. As with logistic regression, the weight estimation process changes from
least squares to maximum likelihood.
Q4   Explain in brief about any two problem solving methods from the given
CO-2; SO-1;   a.   figure:   [10]
BL-2,3
********** 8 **********

[Text in pictures on this page, read by OCR]
Neural Network Binary Prediction Formula
F

logit

link function A A A

j H, = tanh(Wyo + W441 X1 + Waz Xp)
A A A

t) 1 Hy = tanh(Wa + W241 X14 + Wp Xz)

A A A
Hg = tanh(Wap + Waq X4 + Wa X2)
--- page 9 ---
ANS:   05x2
Problem-Solving Methods in Regression Modeling
From the given figure, three important problem-solving methods are:
1. Account for Nonlinearities
Definition: Adjusting the regression model to handle relationships
between predictors and target that are not strictly linear.
Approach:
• Transform predictors (e.g., log, square, square root).
• Use polynomial regression or interaction terms.
• Apply nonlinear regression techniques if required.
Importance:
• Improves model fit when linear assumptions are violated.
• Captures complex patterns in the data for better predictions.
2. Handle Extreme or Unusual Values
Definition: Managing outliers or influential points that may distort
model estimates.
Approach:
• Detect outliers using statistical measures (e.g., z-scores, Cook’s
distance).
• Remove or transform extreme values.
• Use robust regression techniques that reduce the influence of
outliers.
Importance:
• Prevents bias in coefficient estimates.
• Ensures more stable and reliable model predictions.
********** 9 **********
--- page 10 ---
3. Use Nonnumeric Inputs
Definition: Incorporating categorical or text-based variables into
regression models.
Approach:
• Convert categorical variables into dummy/indicator variables.
• Encode ordinal variables appropriately.
• Use specialized regression techniques for categorical or mixed-
type data.
Importance:
• Allows the model to utilize all available information, not just
numeric predictors.
• Enhances predictive performance by including qualitative
factors.
Q4   Explain the different model fit statistics used for Decision, Ranking, and
CO-3; SO-1;   b. Estimate predictions in SAS Enterprise Miner.   [10]
BL-2, 3
ANS:
1. Model Fit Statistics in SAS Enterprise Miner   04
SAS Enterprise Miner provides different fit statistics depending on the type of
prediction:
A. Decision Predictions (Binary/Multiclass Classification)
• Used when the model predicts a discrete class or decision.
•   Fit Statistics:
•   Misclassification Rate: Proportion of cases incorrectly
classified.
• Accuracy / Error Rate: Percentage of correct predictions.
• Confusion Matrix: Shows TP, TN, FP, FN counts.
•   Purpose: Evaluate how well the model assigns cases to the correct
category.
********** 10 **********

[Text in pictures on this page, read by OCR]
Assessment Measures

Prediction Type Fit Statistic
a Accuracy/Misclassification
D> Decisions KS Youden
7 ROC Index
D> Rankings Gini Coefficient
> Estimates Average Squared Error

RMSE/SBC/AIC/Likelihood
--- page 11 ---
B. Ranking Predictions (Scores or Probabilities)
• Used when the model outputs a ranking or probability score for each
case.
03
•   Fit Statistics:
•   Lift: Measures improvement in targeting top-ranked cases
compared to random selection.
• Cumulative Lift Chart: Visualizes how well the model
concentrates positives at the top deciles.
•   Gini Coefficient / ROC AUC: Measures discriminatory power.
•   Purpose: Assess how well the model separates high-value or high-risk
cases from low-value ones.
C. Estimate Predictions (Continuous/Interval Variables)
• Used when the model predicts numeric values (e.g., sales, price).
•   Fit Statistics:   03
• R² (Coefficient of Determination): Proportion of variance
explained.
• Mean Squared Error (MSE) / Root MSE (RMSE): Measures
average prediction error.
• Mean Absolute Error (MAE): Average absolute deviation
from actual values.
•   Purpose: Evaluate accuracy of predicted numeric values.
Q5   Evaluate the use of K-Means clustering for segmenting customers. Discuss
CO-5; SO-1;   a.   its advantages and limitations, and explain with an example that how the   [10]
BL-5   results can help in making business decisions.
ANS:
Evaluation of K-Means Clustering for Customer Segmentation
K-Means clustering is an unsupervised learning algorithm used to group
customers into clusters based on similarities in their features, such as
purchase behavior, demographics, or preferences. The main goal is to
identify distinct customer segments that can be targeted differently for
marketing, product design, or customer support.
02
Advantages of K-Means Clustering:
1. Simplicity and Speed: K-Means is easy to implement and works
efficiently on large datasets.
2. Clear Segmentation: It provides distinct clusters that help in
understanding customer groups.
3. Scalability: Can handle a large number of customers and variables.
Limitations of K-Means Clustering:
02
********** 11 **********
--- page 12 ---
1. Requires Number of Clusters: The number of clusters (K) must be
defined in advance.
2. Sensitive to Outliers: Extreme values can distort cluster centers.
3. Assumes Spherical Clusters: Works best when clusters are well-
separated and roughly equal in size.
Impact on Business Decisions:
• Helps design targeted marketing campaigns by understanding   02
customer needs.
• Supports personalized offers or loyalty programs for different
segments.
• Guides product recommendations and improves customer
satisfaction.
Example:
A retail company uses K-Means to segment customers based on annual   04
spending and purchase frequency.
•   Cluster 1: High spenders with frequent purchases
•   Cluster 2: Moderate spenders with occasional purchases
•   Cluster 3: Low spenders with rare purchases
The marketing team can target Cluster 1 with premium offers, Cluster 2
with loyalty discounts, and Cluster 3 with introductory promotions,
improving overall sales and customer engagement.
Conclusion:
K-Means clustering is an effective method for customer segmentation.
While it has limitations like sensitivity to outliers and the need to predefine
clusters, it provides valuable insights that help businesses make informed
marketing and product decisions.
Q5   Describe the process of exploring model features for scoring in a
CO-3; SO-1;   b. Champion Model. Also, outline the step-by-step procedure for model   [10]
BL-4   scoring in the SAS platform.
ANS:
In SAS, the Champion Model Scoring process involves exploring,
validating, and applying model features to new datasets for prediction. The
goal is to ensure that the deployed model (Champion Model) performs
consistently in real-world scenarios. SAS provides an integrated
environment through Model Studio, Model Manager, and Cloud Analytic
Services (CAS) to simplify and automate this workflow.
05x2
1. Exploring Model Features for Scoring in SAS
********** 12 **********
--- page 13 ---
Before scoring a model, it is essential to validate and explore the input
features to ensure compatibility with the model trained earlier.
(a) Feature Validation
Confirm that all required predictor variables (features) used during model
training are available in the scoring dataset.
SAS automatically highlights any missing or mismatched columns.
(b) Data Type Consistency
Verify that the variable formats (numeric, categorical, date) are identical to
those used in training.
Inconsistent data types can cause errors during scoring.
(c) Transformation Alignment
During model training, SAS applies transformations such as binning,
scaling, or encoding.
The same transformations must be applied to the scoring data.
SAS embeds these transformation rules directly in the model’s score code.
(d) Handling Missing or New Values
Missing values are treated using the same imputation rules applied during
training.
For categorical variables, SAS automatically handles unseen (new)
categories using default settings or rules.
(e) Reviewing Feature Importance
The Champion Model can be analysed through SAS Model Studio to
visualize variable importance and understand which features most
influence the prediction.
2. Model Scoring Procedure in SAS
Once the model features are validated, the Champion Model is used to
score new data and generate predictions. The following steps outline this
process:
Step 1: Access the Champion Model
Open SAS Model Manager.
Locate the Champion Model, which is the best-performing model from
model comparison.
Step 2: Prepare the Scoring Data
Load the new dataset into the CAS environment.
Ensure variable names and structures align with the training data schema.
********** 13 **********
--- page 14 ---
Step 3: Generate and Review Score Code
SAS automatically produces score code in formats such as DS2, Python, or
C.
This code includes all transformations, model parameters, and prediction
logic.
Step 4: Set Up the Scoring Pipeline
In Model Studio, add a Score Node to the pipeline.
Configure it to produce outputs such as predicted values, probabilities, or
decision rules.
Step 5: Execute Scoring in CAS
Run the scoring pipeline.
The CAS engine executes the scoring in-memory for fast performance,
even on large datasets.
Step 6: Review and Export Results
View the scored dataset containing predicted outcomes, class probabilities,
or residuals.
Export the results to a table, CSV file, or dashboard for business
interpretation.
Step 7: Deploy and Monitor
Deploy the scoring model using SAS Model Manager for:
• Batch scoring – scheduled predictions on bulk data.
•   Real-time scoring – instant scoring via REST APIs.
SAS also provides Model Performance Monitoring (MPM) to track
accuracy, drift, and stability over time.
Example:
A Champion Gradient Boosting Model predicting loan default is deployed
in SAS.
The analyst loads new applicant data to CAS.
Using the Score Node, SAS predicts the probability of default.
Predictions are exported to the organization’s data store and monitored
through Model Manager for performance tracking.
Conclusion:
In SAS, the process of exploring model features and performing model
scoring is automated, scalable, and transparent.
It ensures model consistency across environments, enables fast in-memory
********** 14 **********
--- page 15 ---
predictions, and supports continuous monitoring - making SAS a complete
solution for enterprise-level model deployment.
Q6   Explain the working of the Least Angle Regression Model by
CO-4; SO-1;   a. discussing its key model essentials - Predict New Cases, Select Useful   [10]
BL-4,   Inputs, and Optimize Complexity. Additionally, outline the major steps
involved in the Least Angle Regression algorithm.
ANS:
The Least Angle Regression (LARS) Model in SAS is an advanced
regression method that combines the logic of forward selection with
regularization techniques. It efficiently identifies the most relevant
input variables, optimizes model complexity, and provides accurate
predictions without overfitting. LARS is particularly effective for
datasets with many correlated predictors.
02x3
Model Essentials of LARS
1. Predict New Cases
The LARS model predicts new outcomes by gradually building the
regression equation in a stagewise manner.
It starts with all coefficients set to zero and adds input variables one at a
time.
At each stage:
• The algorithm finds the variable most correlated with the
residuals.
•   It increases its coefficient until another variable shows an equal
correlation.
• Both coefficients then grow together, ensuring balanced
contribution.
This process continues until an optimal fit is achieved, allowing LARS
to generate accurate predictions for new data.
2. Select Useful Inputs
LARS automatically selects the most informative variables using a
generalized forward selection process.
•   It begins with no variables and adds the one most correlated with
the residuals.
• When multiple inputs show similar correlations, they are added
together.
********** 15 **********
--- page 16 ---
•   Coefficients are updated in small, balanced steps rather than all
at once.
SAS also allows using the LASSO (Least Absolute Shrinkage and
Selection Operator) method within LARS to shrink less important
coefficients toward zero, improving interpretability and model
simplicity.
3. Optimize Complexity
Model complexity in LARS is managed using penalized best-fit criteria,
such as Schwarz’s Bayesian Criterion (SBC), AIC, or AICC.
These criteria penalize adding unnecessary variables, ensuring that only
those improving the model’s performance remain.
This prevents overfitting and ensures a balance between accuracy and
simplicity.
Steps of the LARS Algorithm
1. Initialization:
All regression coefficients start at zero; residuals equal the target
variable.
2. Select First Predictor:   04
Identify the variable most correlated with residuals and begin
increasing its coefficient.
3. Add More Predictors:
As the model evolves, when another predictor becomes equally
correlated with the residuals, it is added, and both coefficients
are adjusted together.
4. Sequential Updates:
Continue updating coefficients in equal angular directions until
the least squares solution or optimal penalized fit is reached.
5. Optimization & Stopping:
Stop adding variables when improvement no longer outweighs
the penalty (based on SBC or validation metrics).
6. Prediction:
The final model is used to score and predict outcomes on new
datasets.
Example
A retail company uses LARS to predict monthly sales based on
variables like advertising spend, customer visits, discounts, and
competitor pricing.
LARS first selects the most correlated input (advertising spend) and
gradually includes others (like discounts) as their correlation with the
residuals increases.
The model stops when adding more variables no longer improves
accuracy significantly.
********** 16 **********
--- page 17 ---
This results in a concise yet highly predictive model for strategic
business decisions.
Q6   Evaluate the Ensemble Model using the provided figure of ROC curve and
CO-3; SO-1;   b. Cumulative Lift chart. Compare its performance with other individual   [10]
BL-5   models, highlighting strengths and weaknesses. Support your analysis with
a suitable example.
ANS:
The Ensemble Model in SAS Enterprise Miner combines predictions from
03
multiple individual models to improve overall accuracy, stability, and
generalization. Unlike a single model, the Ensemble node does not
generate predictions itself; it merges outputs from component models
using methods like average, maximum, or voting for categorical targets.
Analysis Using ROC Curve:
• The ROC (Receiver Operating Characteristic) curve plots the true
positive rate against the false positive rate.
• A higher area under the ROC curve (AUC) indicates better
discrimination between classes.
•   In the Ensemble Model, the ROC curve typically lies above the
curves of individual models, showing improved predictive
performance.
Analysis Using Cumulative Lift Chart:
• The cumulative lift chart shows the effectiveness of the model in
identifying high-risk or high-value cases.   03
• A steeper lift curve for the Ensemble Model compared to
individual models indicates better ranking of cases and higher
business impact.
Comparison with Other Models:   02
• Bagging/Boosting Models: Ensemble often outperforms single
models by reducing variance (bagging) or bias (boosting).
********** 17 **********
--- page 18 ---
• Model Averaging: Ensemble smooths out prediction errors, making
it more stable than relying on a single algorithm.
Example:   02
In a customer churn prediction scenario:
•   Individual models like logistic regression or decision trees may
have AUCs of 0.78 and 0.80, respectively.
• An ensemble of these models can achieve an AUC of 0.85,
improving the identification of customers likely to churn.
• The cumulative lift chart shows that the top 20% of predicted
churners identified by the ensemble captures a higher proportion of
actual churners than any single model.
Conclusion:
The Ensemble Model leverages the strengths of multiple models, offering
better discrimination, stability, and business utility. It is particularly
effective in scenarios where individual models have complementary
strengths, as demonstrated by ROC and lift charts.
Q7   A grocery store has the following transaction data for 8 customers:
CO-5; SO-1;   a.   [10]
BL-5   Transaction ID   Items Purchased
1   Apples, Bananas, Milk
2   Milk, Bread, Butter
3   Apples, Bread
4   Milk, Apples, Bananas
5   Bread, Butter
6   Milk, Bread, Apples
7   Bananas, Butter
8   Milk, Bread, Bananas
Problem:
1. Using this data, consider the association rule {Bread} ⇒ {Butter}.
2. Calculate support, confidence, and lift for this rule.
3. Evaluate whether this rule is strong enough to suggest a cross-
selling strategy for Bread and Butter.
ANS:
Given Rule: {Bread} ⇒ {Butter}
********** 18 **********
--- page 19 ---
02x4
Step 5: Interpretation
02
• Support (25%): The rule applies to 25% of all transactions —
moderate frequency.
• Confidence (40%): 40% of customers who buy Bread also buy
Butter — reasonable association.
•   Lift (1.07): Slightly greater than 1, indicating a weak positive
correlation; buying Bread slightly increases the likelihood of
buying Butter.
Conclusion / Business Recommendation:
The association is weak but positive. The store could consider pairing
Bread and Butter in promotions or display them together to encourage
cross-selling, but it may not be a very strong predictive rule.
Q7
CO-2; SO-1;   b. Briefly explain the concepts of Concordance and Discordance in the   [05]
BL-2   Decision Tree Ranking Optimization process.
ANS:
In the Decision Tree Ranking Optimization process, Concordance and
Discordance are measures used to evaluate how well the model ranks   02
predicted outcomes compared to actual outcomes.
• Concordance: A pair of observations is concordant if the
observation with the higher predicted probability also has a higher
actual outcome (e.g., if the model predicts a higher probability of
success for a case that indeed succeeds). High concordance
indicates good predictive ranking.
•   Discordance: A pair of observations is discordant if the observation
with the higher predicted probability has a lower actual outcome.
High discordance indicates misranking by the model.
********** 19 **********

[Text in pictures on this page, read by OCR]
Step 1: Identify the Transactions

« Transactions containing Bread: 2, 3, 5,6, 8 —- Total=5

« Transactions containing Butter: 2, 5, 7 — Total = 3

« Transactions containing both Bread and Butter: 2, 5 — Total = 2
« Total transactions = 8

Step 2: Calculate Support

Transactions with Bread and Butter 2

Support(Bread > Butter) = Total T tions = 37 0.25 (25%)

Step 3: Calculate Confidence

T ti ith Bread and Butt: 2
Confidence(Bread > Butter) = a ~— — ~ ad = = = 0.4(40%)
ansas vo

Step 4: Calculate Lift

Confidence(Bread > Butter) 04 0.4

Lift(Bread > Butter) = ===
ift(Bread > Butter) Support (Butter) 3/8 0.375

= 1.07
--- page 20 ---
Usage:
These metrics help assess the ranking ability of decision tree models,
especially for binary or ordinal targets. The goal is to maximize
concordance and minimize discordance to ensure the model correctly   02
prioritizes or ranks cases.
Example:
If a model predicts the probability of customer churn for two customers:
• Customer A: predicted 0.8, actually churned (1)
• Customer B: predicted 0.6, actually did not churn (0)   01
This pair is concordant.
If Customer A had actually not churned and Customer B had churned, the
pair would be discordant.
Maximizing concordance and minimizing discordance improves the
reliability of the decision tree’s ranking predictions.
Q7
CO-2; SO-1;   c. Explain in brief about the Linear Regeression Model Prediction   [05]
BL-2   Formula. Also predict the type of Targate Variable.
ANS:
Explanation of the following figure:
.
********** 20 **********

[Text in pictures on this page, read by OCR]
Linear Regression Prediction Formula

input

measurement

A A A A prediction
Y = Wot WX, + WX)“;

Choose intercept and parameter estimates to minimize:
squared error function
A
D(vi- Vi)?

training
data
````
