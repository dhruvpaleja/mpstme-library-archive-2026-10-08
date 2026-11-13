# Business Analytics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper f71cd7e3c87d

- Departments: Electronics and Telecommunication
- Programmes: MBATech (ELECTRONICS & TELECOMMUNICATIO
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech (ELECTRONICS & TELECOMMUNICATIO_ba3ceaa3/Business Analytics/ANS_Business Analytics(703TM0C003)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 08 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (EXTC)/MBA
Tech (IT)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 08 May 2026   Time: 02:00 pm to 04:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Template for TEE Exam Set 1
Q1
Answer briefly:
a   Explain the concept of Bias–Variance Tradeoff in predictive modeling. How does
it impact model performance? Illustrate your answer by explaining what happens
.   in cases of underfitting and overfitting.
Answer: The Bias–Variance Tradeoff refers to the balance between two types of errors
in a predictive model:
CO   • Bias is the error due to overly simplistic assumptions in the model. High bias leads
-1;   to underfitting, where the model fails to capture the underlying pattern in the data.
• Variance is the error due to excessive sensitivity to training data. High variance
BL-   leads to overfitting, where the model captures noise along with the pattern and
Un   performs poorly on new data.   [5]
de
rst   A good model aims to minimize both bias and variance, achieving optimal predictive
an   performance.
d
•   In underfitting, the model has high bias and low variance (too simple).
•   In overfitting, the model has low bias and high variance (too complex).
Thus, the tradeoff involves selecting a model that balances bias and variance to ensure good
generalization on unseen data.
CO b
(a) Discuss the role of data pre-processing in business analytics. Briefly explain any
-1;
.   two pre-processing techniques.
BL-   [5]
Answer: Data pre-processing is a crucial step in business analytics that involves preparing
Un   raw data for analysis by improving its quality and structure. It ensures that the data is
de   accurate, consistent, and suitable for decision-making.
rst
********** 1 **********
--- page 2 ---
an
d,   Two common pre-processing techniques are:
ap
ply   1. Handling Missing Data:
Missing values can be treated by methods such as deletion, mean/median
imputation, or predictive techniques. This prevents distortion in analysis.
2. Data Normalization:
It involves scaling data into a common range to ensure that variables with larger
values do not dominate the analysis, especially in models like regression or
clustering.
Synoptic Answer
a) State the multiple regression equation. (2 Marks)
The multiple regression equation is:
Y = 197.08 + (0.348 x TV Advertising Spend) + (0.742 x social media spend) + (0.293 x
Email Marketing Spend) + (1.494 x Discount Offered)
b) Interpret the meaning of each regression coefficient. (2 Marks)
• Intercept (197.084):
Monthly sales are expected to be 197.084 (in $1000) when all marketing
Q2   expenditures are zero (not practically meaningful).
CO   • TV Spend (0.348):
A 1 unit increase in TV advertising increases sales by 0.348 units, holding other
-
variables constant.
1,2
•   Social Spend (0.742):
,3;
A 1 unit increase in social media spend increases sales by 0.742 units (highest
BL-   impact).
Ap   • Email Spend (0.293):   [10
ply   A 1 unit increase in email marketing increases sales by 0.293 units.
,   • Discount (1.494):   ]
An   A 1% increase in discount increases sales by 1.494 units.
aly
se,   c) Can the regression equation be used for prediction? (2 Marks)
Ev   The regression model can be used for prediction based on the following:
alu
at   i. ANOVA Test:
e   o Significance value = 0.000 < 0.05
o Indicates the model is statistically significant
ii.   Coefficient of Determination (R²):
o R2=0.493
o The model explains 49.3% variation in sales
o Indicates moderate explanatory power
iii.   Significance of Coefficients (t-test):
o All predictors have p-values < 0.05
o Hence, all variables are statistically significant
iv.   Autocorrelation (Durbin-Watson):
o DW = 1.847 (close to 2)
o Indicates no autocorrelation
********** 2 **********
--- page 3 ---
v.   Multicollinearity (Correlation/VIF logic):
o Correlation among independent variables is low
o Hence, no multicollinearity issue
vi.   Normality of Residuals:
o Histogram is approximately bell-shaped
o P-P plot follows diagonal
o Indicates normality assumption satisfied
vii.   Homoscedasticity:
o Residual scatter plot shows random distribution
o No funnel pattern → variance is constant
d) Determine R² and interpret its meaning. (2 Marks)
• R2=0.493
Interpretation:
49.3% of the variation in monthly sales is explained by TV spend, social media
spend, email marketing, and discount.
This indicates a moderate model fit.
e) Predict monthly sales and interpret. (2 Marks)
Given:
• TV Spend = 120
•   Social Spend = 45
• Email Spend = 30
• Discount = 10
Y=197.084 + 0.348 (120) + 0.742 (45) + 0.293 (30) + 1.494 (10)
Y = 295.964 (in $1000)
Solution:
a) Yes, factor analysis is appropriate.
Q3   • KMO = 0.698 → Acceptable (≥ 0.6), indicating adequate sampling
CO   •   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
-
b) The MSA values (diagonal elements) are above 0.5, hence all the variables are suitable
1,2
for factor analysis.
,3;
BL-   c) Using Eigenvalue > 1 criterion:
Ap   [10
ply   •   Factor 1 = 2.820
]
Ev   •   Factor 2 = 2.029
alu   •   Factor 3 = 1.669
at
Total factors retained = 3
e,
These explain ~70.35% of total variance
cre   d) Factor 1: Service Efficiency
at
e   Service Quality (0.844)
Staff Responsiveness (0.819)
Digital Ease (0.856)
Represents quality of service delivery and responsiveness
Factor 2: Trust & Financial Fairness
********** 3 **********
--- page 4 ---
Trust & Security (0.817)
Pricing Fairness (0.828)
Complaint Resolution (0.868)
Represents customer trust, fairness, and issue handling
Factor 3: Accessibility & Satisfaction
Accessibility (0.882)
Overall Satisfaction (0.748)
Represents ease of access and overall customer satisfaction
e) Factor 1 → Digital Ease (0.856)
Factor 2 → Complaint Resolution (0.868)
Factor 3 → Accessibility (0.882)
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) From Rotation Sums of Squared Loadings:
•   Factor 1 = 26.829%
•   Factor 2 = 26.587%
•   Factor 3 = 16.936%
Most important factor: Factor 1 (Service Efficiency) that explains the highest
variance.
Q4 a
Synoptic Answer
CO
Device   Distance   Class   Rank
-
C   √1 = 1.00   High   1
1,2   G   √2 = 1.41   High   2
A   √2 = 1.41   Low   3
,3;   B   √2 = 1.41   Low   4
BL-   E   √4 = 2.00   Low   5
D   √4 = 2.00   Low   6
Ap   I   √5 = 2.24   High   7
ply   H   √8 = 2.83   Low   8
F   √10 = 3.16   Low   9   [4]
,   J   √16 = 4.00   Low   10
An   k = 3 → High (2 High vs 1 Low)
k = 5 → Low (2 High vs 3 Low)
aly
Step   Marks
se,
Distance calculation   1
Ev   Nearest neighbors’ identification   1
alu   Prediction using k=3   1
Prediction using k=5   1
at
e
b Answers
Q4   [6]
********** 4 **********
--- page 5 ---
CO   i)   Discriminant Function = 0.150 - -6.861 * Debt_to_Income + 0.178*
Credit_History_Yrs + .00001* Savings_Balance
-   ii)   Structure matrix gives explanatory power of variables. Highest absolute values
1,2   ( modulus since it is correlations) indicate highest explanatory power of variables.
And lowest absolute values ( modulus since it is correlations) indicate lowest
,3;   explanatory power of variables. In this case, Savings_Balancehas highest (.945) and
Debt_to_Income (-.876) has lowest explanatory power.
BL-
iii)   H0 : The covariance matrices of the groups are same across the two groups
Ap   H1 : The covariance matrices of the groups are different across the two groups
Here the Box’s M is not significant (p value =.000 < 0.05) this suggests covariance
ply   matrices are significantly different across two groups. So assumption of equal
covariance matrices does not holds good
,
i)   Cross-validated accuracy is 96.0%.
An   Chance accuracy Calculations
aly   Risk   0   49   3   52   0.52
se,   Type   1   1   47   48   0.48
Overall Percentage   100
Ev
Chance Accuracy 0.5008
alu   Minimum required Acc
at   0.626
this data has around equal number of successes and failures. The chance accuracy for the data is
e   p(S)2 + p(F)2 = 0.5008
We need atleast 25% improvement over chance accuracy i.e. 0.5008* 1.25 = 0. 0.626 the overall
cross validated accuracy much better than minimum required accuracy also Wilk’s Lamda is low
and significant, each variable is significant and canonical correlation is high (.901) hence the
model could be used for prediction.
Answers :
Q5   1. The logistic regression model is:
CO   𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
𝑝(𝑥) =
1 + 𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
-   2. Which Tests ?
•   Wald Test: p <0.05): significant model
1,2
•   Hosmer-Lemeshow Test (p > 0.05): significant model
,3;   3. Analyze the classification table and explain its implications?
BL-
FPR (Specificity ) is 98.9
Ap   [10
TPR (Sensitivity) is 72.7
ply   ]
,   Classification accuracy is 96.0
An   Chance Accuracy is 0.8042
aly
Minimum Required accuracy is: 1.25 * Chance Accuracy = 1.00525
se,
The data has class imbalance resulting in minimum required accuracy more than 100% since
Ev   Classification accuracy is less than the required accuracy, the model could not be trusted for
prediction. On the other side, TPR is decent, indicating good percentage of success
alu
********** 5 **********
--- page 6 ---
at   4. Explain the concepts of Sensitivity and Specificity in relation to this model.
Sensitivity (Recall) = TP / (TP + FN)
e   Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Specificity (98.9%): The model correctly identifies 98.9% of non premium Cars as non
premium cars
•   Sensitivity (72.7%): The model correctly identifies 72.7% of premium Cars as premium
cars.
5. Probability of premium Car = 0.14479
Price   1.646   12
Mileage   -0.916   18
Horsepo   0.05
wer   110
Age   -0.79   3
Constant   -8.17   1
Y   -1.776
exp(-y)   5.906184
P   0.144798
6. Since probability is less than 0.5, the car is catagorised as non premium.
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his/her choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO
-
2,3   d) Cluster Characteristics Interpretation
;   We interpret each cluster by comparing high vs low mean values across variables.
BL-   Cluster 1 (n = 10): “Credit-Dependent, High-Risk Customers”
[6]
Key Observations:
Un
de   •   Savings: Low (4.80)
•   Credit Usage: Very High (7.70)
rst   •   Online Banking: Low (4.10)
an   •   Investment: Very Low (3.00)
•   Risk Appetite: Very High (8.40)
d   • Loan Dependence: Very High (8.00)
Interpretation:
• Customers do not save much
•   Highly dependent on credit and loans
•   Willing to take high financial risks
********** 6 **********
--- page 7 ---
•   Limited use of digital banking
•   Very low inclination towards investment planning
“High-Risk Borrowers” / “Credit-Driven Segment”
Cluster 2 (n = 11): “Wealth Builders / Conservative Investors”
Key Observations:
•   Savings: Very High (8.64)
•   Credit Usage: Very Low (2.18)
•   Online Banking: Very High (9.00)
•   Investment: High (7.73)
•   Risk Appetite: Very Low (1.91)
• Loan Dependence: Low (2.82)
Interpretation:
•   Strong saving habits
•   Prefer low risk financial behavior
•   Active users of digital banking
•   Invest regularly (likely safe instruments)
•   Avoid loans and credit
“Conservative Wealth Builders” / “Digital Savers”
Cluster 3 (n = 9): “Balanced / Moderate Customers”
Key Observations:
•   Savings: Moderate (6.33)
•   Credit Usage: Moderate (5.44)
•   Online Banking: Moderate (6.44)
•   Investment: Moderate (5.56)
•   Risk Appetite: Moderate (5.78)
• Loan Dependence: Moderate (5.67)
Interpretation:
•   Balanced behavior across all dimensions
• Moderate use of:
o Savings
o   Credit
o Investment
•   Neither highly risk-averse nor risk-seeking
“Balanced Customers” / “Average Financial Users”
Cluste
Profile   Key Traits
r
High credit, high risk, low
1   High-Risk Borrowers
savings
Conservative Wealth   High savings, low risk, high
2
Builders   digital
********** 7 **********
--- page 8 ---
3   Balanced Customers   Moderate across all variables
b Solution: To identify outliers using Cook’s Distance, a common rule of thumb is:
Q6   Threshold=4/n = 4/30 ≈ 0.133
Any observation with Cook’s Distance greater than 0.133 is considered influential
CO
(potential outlier).
-;
SO   [4]
•   S.No. 17 → 0.18362 (> 0.133)
-;   •   All others are below 0.133
S.No. of Outliers: 17
BL-
Q7 a Answer
3
CO   Wee   Demand   Moving   Exponential
-   k   (Units)   Averag   Smoothing alpha
e   Error   =0.4   Error
1,2   1   42   42
,3;   2   48   42   6
3   45   44.4   0.6
BL-   4   50   45   5   44.64   5.36
Ap   47.666   7.3333
5   55
67   33   46.784   8.216
ply   6   52   50   2   50.0704   1.9296
[4]
,   52.333
Forecast   33   50.84224
An   14.333   22.105
Total Error   33 Total Error   6
aly
Mean Absolute   4.7777 Mean Absolute   4.4211
se,   Error   78 Error   2
1) 52.33333
Ev
2) 50.84224
alu   3) Mean absolute Error for 3 moving average is 4.777778, Exponential Smoothing is
4.42112. Since exponential smoothing error is less than 3 moving average, exponential
at
smoothing is better forecast and hence should be used
e
Q7 b
CO
-
1,2
,3;   Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the   [6]
BL-
lags and are above zero as well as below zero indicating stationarity. There is no need for
Ap   difference for this data.
ply
,
An
********** 8 **********
--- page 9 ---
aly
se,
Ev
alu
at
e
The model selection is done on the basis of following parameters
1. Requirement of stationarity (in this case d = 0)
2. BIC as low as possible
3. All lags (except intercept) need to be significant
4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
In above case
Sr   Model   BIC   Description   Result
No
1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, Model
without   lag sig   cannot be
removing   problem – Residual ACF &   used
outliers   PACF not within range
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,.   Model
without   Residual ACF & PACF within   cannot be
removing   range   used
outliers   problem – d=1, all lags not
sig,
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag   Model
without   sig, Residual ACF & PACF   cannot be
removing   within range   used
outliers   problem – d=1
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig, Model
without   problem – Residual ACF &   cannot be
removing   PACF not within range   used
outliers   all lags not sig.
5   ARIMA(1,0,0)   8.962   All correct + minimum BIC +   Model can
after   Simplest possible model   be used
removing
outliers
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Model   30   31   32   33   34   35
Demand EV - Forecas   2026   2015   2007   2001   1996   1992
Model_1   t
********** 9 **********
--- page 10 ---
UCL   2148   2150   2149   2147   2144   2142
LCL   1905   1881   1865   1855   1847   1842
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 92f1fb776f58

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_AI_7051/Business Analytics/ANS_Business Analytics(703TM0C003)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 08 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (EXTC)/MBA
Tech (IT)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 08 May 2026   Time: 02:00 pm to 04:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Template for TEE Exam Set 1
Q1
Answer briefly:
a   Explain the concept of Bias–Variance Tradeoff in predictive modeling. How does
it impact model performance? Illustrate your answer by explaining what happens
.   in cases of underfitting and overfitting.
Answer: The Bias–Variance Tradeoff refers to the balance between two types of errors
in a predictive model:
CO   • Bias is the error due to overly simplistic assumptions in the model. High bias leads
-1;   to underfitting, where the model fails to capture the underlying pattern in the data.
• Variance is the error due to excessive sensitivity to training data. High variance
BL-   leads to overfitting, where the model captures noise along with the pattern and
Un   performs poorly on new data.   [5]
de
rst   A good model aims to minimize both bias and variance, achieving optimal predictive
an   performance.
d
•   In underfitting, the model has high bias and low variance (too simple).
•   In overfitting, the model has low bias and high variance (too complex).
Thus, the tradeoff involves selecting a model that balances bias and variance to ensure good
generalization on unseen data.
CO b
(a) Discuss the role of data pre-processing in business analytics. Briefly explain any
-1;
.   two pre-processing techniques.
BL-   [5]
Answer: Data pre-processing is a crucial step in business analytics that involves preparing
Un   raw data for analysis by improving its quality and structure. It ensures that the data is
de   accurate, consistent, and suitable for decision-making.
rst
********** 1 **********
--- page 2 ---
an
d,   Two common pre-processing techniques are:
ap
ply   1. Handling Missing Data:
Missing values can be treated by methods such as deletion, mean/median
imputation, or predictive techniques. This prevents distortion in analysis.
2. Data Normalization:
It involves scaling data into a common range to ensure that variables with larger
values do not dominate the analysis, especially in models like regression or
clustering.
Synoptic Answer
a) State the multiple regression equation. (2 Marks)
The multiple regression equation is:
Y = 197.08 + (0.348 x TV Advertising Spend) + (0.742 x social media spend) + (0.293 x
Email Marketing Spend) + (1.494 x Discount Offered)
b) Interpret the meaning of each regression coefficient. (2 Marks)
• Intercept (197.084):
Monthly sales are expected to be 197.084 (in $1000) when all marketing
Q2   expenditures are zero (not practically meaningful).
CO   • TV Spend (0.348):
A 1 unit increase in TV advertising increases sales by 0.348 units, holding other
-
variables constant.
1,2
•   Social Spend (0.742):
,3;
A 1 unit increase in social media spend increases sales by 0.742 units (highest
BL-   impact).
Ap   • Email Spend (0.293):   [10
ply   A 1 unit increase in email marketing increases sales by 0.293 units.
,   • Discount (1.494):   ]
An   A 1% increase in discount increases sales by 1.494 units.
aly
se,   c) Can the regression equation be used for prediction? (2 Marks)
Ev   The regression model can be used for prediction based on the following:
alu
at   i. ANOVA Test:
e   o Significance value = 0.000 < 0.05
o Indicates the model is statistically significant
ii.   Coefficient of Determination (R²):
o R2=0.493
o The model explains 49.3% variation in sales
o Indicates moderate explanatory power
iii.   Significance of Coefficients (t-test):
o All predictors have p-values < 0.05
o Hence, all variables are statistically significant
iv.   Autocorrelation (Durbin-Watson):
o DW = 1.847 (close to 2)
o Indicates no autocorrelation
********** 2 **********
--- page 3 ---
v.   Multicollinearity (Correlation/VIF logic):
o Correlation among independent variables is low
o Hence, no multicollinearity issue
vi.   Normality of Residuals:
o Histogram is approximately bell-shaped
o P-P plot follows diagonal
o Indicates normality assumption satisfied
vii.   Homoscedasticity:
o Residual scatter plot shows random distribution
o No funnel pattern → variance is constant
d) Determine R² and interpret its meaning. (2 Marks)
• R2=0.493
Interpretation:
49.3% of the variation in monthly sales is explained by TV spend, social media
spend, email marketing, and discount.
This indicates a moderate model fit.
e) Predict monthly sales and interpret. (2 Marks)
Given:
• TV Spend = 120
•   Social Spend = 45
• Email Spend = 30
• Discount = 10
Y=197.084 + 0.348 (120) + 0.742 (45) + 0.293 (30) + 1.494 (10)
Y = 295.964 (in $1000)
Solution:
a) Yes, factor analysis is appropriate.
Q3   • KMO = 0.698 → Acceptable (≥ 0.6), indicating adequate sampling
CO   •   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
-
b) The MSA values (diagonal elements) are above 0.5, hence all the variables are suitable
1,2
for factor analysis.
,3;
BL-   c) Using Eigenvalue > 1 criterion:
Ap   [10
ply   •   Factor 1 = 2.820
]
Ev   •   Factor 2 = 2.029
alu   •   Factor 3 = 1.669
at
Total factors retained = 3
e,
These explain ~70.35% of total variance
cre   d) Factor 1: Service Efficiency
at
e   Service Quality (0.844)
Staff Responsiveness (0.819)
Digital Ease (0.856)
Represents quality of service delivery and responsiveness
Factor 2: Trust & Financial Fairness
********** 3 **********
--- page 4 ---
Trust & Security (0.817)
Pricing Fairness (0.828)
Complaint Resolution (0.868)
Represents customer trust, fairness, and issue handling
Factor 3: Accessibility & Satisfaction
Accessibility (0.882)
Overall Satisfaction (0.748)
Represents ease of access and overall customer satisfaction
e) Factor 1 → Digital Ease (0.856)
Factor 2 → Complaint Resolution (0.868)
Factor 3 → Accessibility (0.882)
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) From Rotation Sums of Squared Loadings:
•   Factor 1 = 26.829%
•   Factor 2 = 26.587%
•   Factor 3 = 16.936%
Most important factor: Factor 1 (Service Efficiency) that explains the highest
variance.
Q4 a
Synoptic Answer
CO
Device   Distance   Class   Rank
-
C   √1 = 1.00   High   1
1,2   G   √2 = 1.41   High   2
A   √2 = 1.41   Low   3
,3;   B   √2 = 1.41   Low   4
BL-   E   √4 = 2.00   Low   5
D   √4 = 2.00   Low   6
Ap   I   √5 = 2.24   High   7
ply   H   √8 = 2.83   Low   8
F   √10 = 3.16   Low   9   [4]
,   J   √16 = 4.00   Low   10
An   k = 3 → High (2 High vs 1 Low)
k = 5 → Low (2 High vs 3 Low)
aly
Step   Marks
se,
Distance calculation   1
Ev   Nearest neighbors’ identification   1
alu   Prediction using k=3   1
Prediction using k=5   1
at
e
b Answers
Q4   [6]
********** 4 **********
--- page 5 ---
CO   i)   Discriminant Function = 0.150 - -6.861 * Debt_to_Income + 0.178*
Credit_History_Yrs + .00001* Savings_Balance
-   ii)   Structure matrix gives explanatory power of variables. Highest absolute values
1,2   ( modulus since it is correlations) indicate highest explanatory power of variables.
And lowest absolute values ( modulus since it is correlations) indicate lowest
,3;   explanatory power of variables. In this case, Savings_Balancehas highest (.945) and
Debt_to_Income (-.876) has lowest explanatory power.
BL-
iii)   H0 : The covariance matrices of the groups are same across the two groups
Ap   H1 : The covariance matrices of the groups are different across the two groups
Here the Box’s M is not significant (p value =.000 < 0.05) this suggests covariance
ply   matrices are significantly different across two groups. So assumption of equal
covariance matrices does not holds good
,
i)   Cross-validated accuracy is 96.0%.
An   Chance accuracy Calculations
aly   Risk   0   49   3   52   0.52
se,   Type   1   1   47   48   0.48
Overall Percentage   100
Ev
Chance Accuracy 0.5008
alu   Minimum required Acc
at   0.626
this data has around equal number of successes and failures. The chance accuracy for the data is
e   p(S)2 + p(F)2 = 0.5008
We need atleast 25% improvement over chance accuracy i.e. 0.5008* 1.25 = 0. 0.626 the overall
cross validated accuracy much better than minimum required accuracy also Wilk’s Lamda is low
and significant, each variable is significant and canonical correlation is high (.901) hence the
model could be used for prediction.
Answers :
Q5   1. The logistic regression model is:
CO   𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
𝑝(𝑥) =
1 + 𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
-   2. Which Tests ?
•   Wald Test: p <0.05): significant model
1,2
•   Hosmer-Lemeshow Test (p > 0.05): significant model
,3;   3. Analyze the classification table and explain its implications?
BL-
FPR (Specificity ) is 98.9
Ap   [10
TPR (Sensitivity) is 72.7
ply   ]
,   Classification accuracy is 96.0
An   Chance Accuracy is 0.8042
aly
Minimum Required accuracy is: 1.25 * Chance Accuracy = 1.00525
se,
The data has class imbalance resulting in minimum required accuracy more than 100% since
Ev   Classification accuracy is less than the required accuracy, the model could not be trusted for
prediction. On the other side, TPR is decent, indicating good percentage of success
alu
********** 5 **********
--- page 6 ---
at   4. Explain the concepts of Sensitivity and Specificity in relation to this model.
Sensitivity (Recall) = TP / (TP + FN)
e   Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Specificity (98.9%): The model correctly identifies 98.9% of non premium Cars as non
premium cars
•   Sensitivity (72.7%): The model correctly identifies 72.7% of premium Cars as premium
cars.
5. Probability of premium Car = 0.14479
Price   1.646   12
Mileage   -0.916   18
Horsepo   0.05
wer   110
Age   -0.79   3
Constant   -8.17   1
Y   -1.776
exp(-y)   5.906184
P   0.144798
6. Since probability is less than 0.5, the car is catagorised as non premium.
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his/her choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO
-
2,3   d) Cluster Characteristics Interpretation
;   We interpret each cluster by comparing high vs low mean values across variables.
BL-   Cluster 1 (n = 10): “Credit-Dependent, High-Risk Customers”
[6]
Key Observations:
Un
de   •   Savings: Low (4.80)
•   Credit Usage: Very High (7.70)
rst   •   Online Banking: Low (4.10)
an   •   Investment: Very Low (3.00)
•   Risk Appetite: Very High (8.40)
d   • Loan Dependence: Very High (8.00)
Interpretation:
• Customers do not save much
•   Highly dependent on credit and loans
•   Willing to take high financial risks
********** 6 **********
--- page 7 ---
•   Limited use of digital banking
•   Very low inclination towards investment planning
“High-Risk Borrowers” / “Credit-Driven Segment”
Cluster 2 (n = 11): “Wealth Builders / Conservative Investors”
Key Observations:
•   Savings: Very High (8.64)
•   Credit Usage: Very Low (2.18)
•   Online Banking: Very High (9.00)
•   Investment: High (7.73)
•   Risk Appetite: Very Low (1.91)
• Loan Dependence: Low (2.82)
Interpretation:
•   Strong saving habits
•   Prefer low risk financial behavior
•   Active users of digital banking
•   Invest regularly (likely safe instruments)
•   Avoid loans and credit
“Conservative Wealth Builders” / “Digital Savers”
Cluster 3 (n = 9): “Balanced / Moderate Customers”
Key Observations:
•   Savings: Moderate (6.33)
•   Credit Usage: Moderate (5.44)
•   Online Banking: Moderate (6.44)
•   Investment: Moderate (5.56)
•   Risk Appetite: Moderate (5.78)
• Loan Dependence: Moderate (5.67)
Interpretation:
•   Balanced behavior across all dimensions
• Moderate use of:
o Savings
o   Credit
o Investment
•   Neither highly risk-averse nor risk-seeking
“Balanced Customers” / “Average Financial Users”
Cluste
Profile   Key Traits
r
High credit, high risk, low
1   High-Risk Borrowers
savings
Conservative Wealth   High savings, low risk, high
2
Builders   digital
********** 7 **********
--- page 8 ---
3   Balanced Customers   Moderate across all variables
b Solution: To identify outliers using Cook’s Distance, a common rule of thumb is:
Q6   Threshold=4/n = 4/30 ≈ 0.133
Any observation with Cook’s Distance greater than 0.133 is considered influential
CO
(potential outlier).
-;
SO   [4]
•   S.No. 17 → 0.18362 (> 0.133)
-;   •   All others are below 0.133
S.No. of Outliers: 17
BL-
Q7 a Answer
3
CO   Wee   Demand   Moving   Exponential
-   k   (Units)   Averag   Smoothing alpha
e   Error   =0.4   Error
1,2   1   42   42
,3;   2   48   42   6
3   45   44.4   0.6
BL-   4   50   45   5   44.64   5.36
Ap   47.666   7.3333
5   55
67   33   46.784   8.216
ply   6   52   50   2   50.0704   1.9296
[4]
,   52.333
Forecast   33   50.84224
An   14.333   22.105
Total Error   33 Total Error   6
aly
Mean Absolute   4.7777 Mean Absolute   4.4211
se,   Error   78 Error   2
1) 52.33333
Ev
2) 50.84224
alu   3) Mean absolute Error for 3 moving average is 4.777778, Exponential Smoothing is
4.42112. Since exponential smoothing error is less than 3 moving average, exponential
at
smoothing is better forecast and hence should be used
e
Q7 b
CO
-
1,2
,3;   Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the   [6]
BL-
lags and are above zero as well as below zero indicating stationarity. There is no need for
Ap   difference for this data.
ply
,
An
********** 8 **********
--- page 9 ---
aly
se,
Ev
alu
at
e
The model selection is done on the basis of following parameters
1. Requirement of stationarity (in this case d = 0)
2. BIC as low as possible
3. All lags (except intercept) need to be significant
4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
In above case
Sr   Model   BIC   Description   Result
No
1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, Model
without   lag sig   cannot be
removing   problem – Residual ACF &   used
outliers   PACF not within range
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,.   Model
without   Residual ACF & PACF within   cannot be
removing   range   used
outliers   problem – d=1, all lags not
sig,
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag   Model
without   sig, Residual ACF & PACF   cannot be
removing   within range   used
outliers   problem – d=1
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig, Model
without   problem – Residual ACF &   cannot be
removing   PACF not within range   used
outliers   all lags not sig.
5   ARIMA(1,0,0)   8.962   All correct + minimum BIC +   Model can
after   Simplest possible model   be used
removing
outliers
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Model   30   31   32   33   34   35
Demand EV - Forecas   2026   2015   2007   2001   1996   1992
Model_1   t
********** 9 **********
--- page 10 ---
UCL   2148   2150   2149   2147   2144   2142
LCL   1905   1881   1865   1855   1847   1842
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 8abd30d61f10

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_Computer_7047/Business Analytics/ANS_Business Analytics(703TM0C003)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 08 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (EXTC)/MBA
Tech (IT)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 08 May 2026   Time: 02:00 pm to 04:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Template for TEE Exam Set 1
Q1
Answer briefly:
a   Explain the concept of Bias–Variance Tradeoff in predictive modeling. How does
it impact model performance? Illustrate your answer by explaining what happens
.   in cases of underfitting and overfitting.
Answer: The Bias–Variance Tradeoff refers to the balance between two types of errors
in a predictive model:
CO   • Bias is the error due to overly simplistic assumptions in the model. High bias leads
-1;   to underfitting, where the model fails to capture the underlying pattern in the data.
• Variance is the error due to excessive sensitivity to training data. High variance
BL-   leads to overfitting, where the model captures noise along with the pattern and
Un   performs poorly on new data.   [5]
de
rst   A good model aims to minimize both bias and variance, achieving optimal predictive
an   performance.
d
•   In underfitting, the model has high bias and low variance (too simple).
•   In overfitting, the model has low bias and high variance (too complex).
Thus, the tradeoff involves selecting a model that balances bias and variance to ensure good
generalization on unseen data.
CO b
(a) Discuss the role of data pre-processing in business analytics. Briefly explain any
-1;
.   two pre-processing techniques.
BL-   [5]
Answer: Data pre-processing is a crucial step in business analytics that involves preparing
Un   raw data for analysis by improving its quality and structure. It ensures that the data is
de   accurate, consistent, and suitable for decision-making.
rst
********** 1 **********
--- page 2 ---
an
d,   Two common pre-processing techniques are:
ap
ply   1. Handling Missing Data:
Missing values can be treated by methods such as deletion, mean/median
imputation, or predictive techniques. This prevents distortion in analysis.
2. Data Normalization:
It involves scaling data into a common range to ensure that variables with larger
values do not dominate the analysis, especially in models like regression or
clustering.
Synoptic Answer
a) State the multiple regression equation. (2 Marks)
The multiple regression equation is:
Y = 197.08 + (0.348 x TV Advertising Spend) + (0.742 x social media spend) + (0.293 x
Email Marketing Spend) + (1.494 x Discount Offered)
b) Interpret the meaning of each regression coefficient. (2 Marks)
• Intercept (197.084):
Monthly sales are expected to be 197.084 (in $1000) when all marketing
Q2   expenditures are zero (not practically meaningful).
CO   • TV Spend (0.348):
A 1 unit increase in TV advertising increases sales by 0.348 units, holding other
-
variables constant.
1,2
•   Social Spend (0.742):
,3;
A 1 unit increase in social media spend increases sales by 0.742 units (highest
BL-   impact).
Ap   • Email Spend (0.293):   [10
ply   A 1 unit increase in email marketing increases sales by 0.293 units.
,   • Discount (1.494):   ]
An   A 1% increase in discount increases sales by 1.494 units.
aly
se,   c) Can the regression equation be used for prediction? (2 Marks)
Ev   The regression model can be used for prediction based on the following:
alu
at   i. ANOVA Test:
e   o Significance value = 0.000 < 0.05
o Indicates the model is statistically significant
ii.   Coefficient of Determination (R²):
o R2=0.493
o The model explains 49.3% variation in sales
o Indicates moderate explanatory power
iii.   Significance of Coefficients (t-test):
o All predictors have p-values < 0.05
o Hence, all variables are statistically significant
iv.   Autocorrelation (Durbin-Watson):
o DW = 1.847 (close to 2)
o Indicates no autocorrelation
********** 2 **********
--- page 3 ---
v.   Multicollinearity (Correlation/VIF logic):
o Correlation among independent variables is low
o Hence, no multicollinearity issue
vi.   Normality of Residuals:
o Histogram is approximately bell-shaped
o P-P plot follows diagonal
o Indicates normality assumption satisfied
vii.   Homoscedasticity:
o Residual scatter plot shows random distribution
o No funnel pattern → variance is constant
d) Determine R² and interpret its meaning. (2 Marks)
• R2=0.493
Interpretation:
49.3% of the variation in monthly sales is explained by TV spend, social media
spend, email marketing, and discount.
This indicates a moderate model fit.
e) Predict monthly sales and interpret. (2 Marks)
Given:
• TV Spend = 120
•   Social Spend = 45
• Email Spend = 30
• Discount = 10
Y=197.084 + 0.348 (120) + 0.742 (45) + 0.293 (30) + 1.494 (10)
Y = 295.964 (in $1000)
Solution:
a) Yes, factor analysis is appropriate.
Q3   • KMO = 0.698 → Acceptable (≥ 0.6), indicating adequate sampling
CO   •   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
-
b) The MSA values (diagonal elements) are above 0.5, hence all the variables are suitable
1,2
for factor analysis.
,3;
BL-   c) Using Eigenvalue > 1 criterion:
Ap   [10
ply   •   Factor 1 = 2.820
]
Ev   •   Factor 2 = 2.029
alu   •   Factor 3 = 1.669
at
Total factors retained = 3
e,
These explain ~70.35% of total variance
cre   d) Factor 1: Service Efficiency
at
e   Service Quality (0.844)
Staff Responsiveness (0.819)
Digital Ease (0.856)
Represents quality of service delivery and responsiveness
Factor 2: Trust & Financial Fairness
********** 3 **********
--- page 4 ---
Trust & Security (0.817)
Pricing Fairness (0.828)
Complaint Resolution (0.868)
Represents customer trust, fairness, and issue handling
Factor 3: Accessibility & Satisfaction
Accessibility (0.882)
Overall Satisfaction (0.748)
Represents ease of access and overall customer satisfaction
e) Factor 1 → Digital Ease (0.856)
Factor 2 → Complaint Resolution (0.868)
Factor 3 → Accessibility (0.882)
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) From Rotation Sums of Squared Loadings:
•   Factor 1 = 26.829%
•   Factor 2 = 26.587%
•   Factor 3 = 16.936%
Most important factor: Factor 1 (Service Efficiency) that explains the highest
variance.
Q4 a
Synoptic Answer
CO
Device   Distance   Class   Rank
-
C   √1 = 1.00   High   1
1,2   G   √2 = 1.41   High   2
A   √2 = 1.41   Low   3
,3;   B   √2 = 1.41   Low   4
BL-   E   √4 = 2.00   Low   5
D   √4 = 2.00   Low   6
Ap   I   √5 = 2.24   High   7
ply   H   √8 = 2.83   Low   8
F   √10 = 3.16   Low   9   [4]
,   J   √16 = 4.00   Low   10
An   k = 3 → High (2 High vs 1 Low)
k = 5 → Low (2 High vs 3 Low)
aly
Step   Marks
se,
Distance calculation   1
Ev   Nearest neighbors’ identification   1
alu   Prediction using k=3   1
Prediction using k=5   1
at
e
b Answers
Q4   [6]
********** 4 **********
--- page 5 ---
CO   i)   Discriminant Function = 0.150 - -6.861 * Debt_to_Income + 0.178*
Credit_History_Yrs + .00001* Savings_Balance
-   ii)   Structure matrix gives explanatory power of variables. Highest absolute values
1,2   ( modulus since it is correlations) indicate highest explanatory power of variables.
And lowest absolute values ( modulus since it is correlations) indicate lowest
,3;   explanatory power of variables. In this case, Savings_Balancehas highest (.945) and
Debt_to_Income (-.876) has lowest explanatory power.
BL-
iii)   H0 : The covariance matrices of the groups are same across the two groups
Ap   H1 : The covariance matrices of the groups are different across the two groups
Here the Box’s M is not significant (p value =.000 < 0.05) this suggests covariance
ply   matrices are significantly different across two groups. So assumption of equal
covariance matrices does not holds good
,
i)   Cross-validated accuracy is 96.0%.
An   Chance accuracy Calculations
aly   Risk   0   49   3   52   0.52
se,   Type   1   1   47   48   0.48
Overall Percentage   100
Ev
Chance Accuracy 0.5008
alu   Minimum required Acc
at   0.626
this data has around equal number of successes and failures. The chance accuracy for the data is
e   p(S)2 + p(F)2 = 0.5008
We need atleast 25% improvement over chance accuracy i.e. 0.5008* 1.25 = 0. 0.626 the overall
cross validated accuracy much better than minimum required accuracy also Wilk’s Lamda is low
and significant, each variable is significant and canonical correlation is high (.901) hence the
model could be used for prediction.
Answers :
Q5   1. The logistic regression model is:
CO   𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
𝑝(𝑥) =
1 + 𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
-   2. Which Tests ?
•   Wald Test: p <0.05): significant model
1,2
•   Hosmer-Lemeshow Test (p > 0.05): significant model
,3;   3. Analyze the classification table and explain its implications?
BL-
FPR (Specificity ) is 98.9
Ap   [10
TPR (Sensitivity) is 72.7
ply   ]
,   Classification accuracy is 96.0
An   Chance Accuracy is 0.8042
aly
Minimum Required accuracy is: 1.25 * Chance Accuracy = 1.00525
se,
The data has class imbalance resulting in minimum required accuracy more than 100% since
Ev   Classification accuracy is less than the required accuracy, the model could not be trusted for
prediction. On the other side, TPR is decent, indicating good percentage of success
alu
********** 5 **********
--- page 6 ---
at   4. Explain the concepts of Sensitivity and Specificity in relation to this model.
Sensitivity (Recall) = TP / (TP + FN)
e   Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Specificity (98.9%): The model correctly identifies 98.9% of non premium Cars as non
premium cars
•   Sensitivity (72.7%): The model correctly identifies 72.7% of premium Cars as premium
cars.
5. Probability of premium Car = 0.14479
Price   1.646   12
Mileage   -0.916   18
Horsepo   0.05
wer   110
Age   -0.79   3
Constant   -8.17   1
Y   -1.776
exp(-y)   5.906184
P   0.144798
6. Since probability is less than 0.5, the car is catagorised as non premium.
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his/her choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO
-
2,3   d) Cluster Characteristics Interpretation
;   We interpret each cluster by comparing high vs low mean values across variables.
BL-   Cluster 1 (n = 10): “Credit-Dependent, High-Risk Customers”
[6]
Key Observations:
Un
de   •   Savings: Low (4.80)
•   Credit Usage: Very High (7.70)
rst   •   Online Banking: Low (4.10)
an   •   Investment: Very Low (3.00)
•   Risk Appetite: Very High (8.40)
d   • Loan Dependence: Very High (8.00)
Interpretation:
• Customers do not save much
•   Highly dependent on credit and loans
•   Willing to take high financial risks
********** 6 **********
--- page 7 ---
•   Limited use of digital banking
•   Very low inclination towards investment planning
“High-Risk Borrowers” / “Credit-Driven Segment”
Cluster 2 (n = 11): “Wealth Builders / Conservative Investors”
Key Observations:
•   Savings: Very High (8.64)
•   Credit Usage: Very Low (2.18)
•   Online Banking: Very High (9.00)
•   Investment: High (7.73)
•   Risk Appetite: Very Low (1.91)
• Loan Dependence: Low (2.82)
Interpretation:
•   Strong saving habits
•   Prefer low risk financial behavior
•   Active users of digital banking
•   Invest regularly (likely safe instruments)
•   Avoid loans and credit
“Conservative Wealth Builders” / “Digital Savers”
Cluster 3 (n = 9): “Balanced / Moderate Customers”
Key Observations:
•   Savings: Moderate (6.33)
•   Credit Usage: Moderate (5.44)
•   Online Banking: Moderate (6.44)
•   Investment: Moderate (5.56)
•   Risk Appetite: Moderate (5.78)
• Loan Dependence: Moderate (5.67)
Interpretation:
•   Balanced behavior across all dimensions
• Moderate use of:
o Savings
o   Credit
o Investment
•   Neither highly risk-averse nor risk-seeking
“Balanced Customers” / “Average Financial Users”
Cluste
Profile   Key Traits
r
High credit, high risk, low
1   High-Risk Borrowers
savings
Conservative Wealth   High savings, low risk, high
2
Builders   digital
********** 7 **********
--- page 8 ---
3   Balanced Customers   Moderate across all variables
b Solution: To identify outliers using Cook’s Distance, a common rule of thumb is:
Q6   Threshold=4/n = 4/30 ≈ 0.133
Any observation with Cook’s Distance greater than 0.133 is considered influential
CO
(potential outlier).
-;
SO   [4]
•   S.No. 17 → 0.18362 (> 0.133)
-;   •   All others are below 0.133
S.No. of Outliers: 17
BL-
Q7 a Answer
3
CO   Wee   Demand   Moving   Exponential
-   k   (Units)   Averag   Smoothing alpha
e   Error   =0.4   Error
1,2   1   42   42
,3;   2   48   42   6
3   45   44.4   0.6
BL-   4   50   45   5   44.64   5.36
Ap   47.666   7.3333
5   55
67   33   46.784   8.216
ply   6   52   50   2   50.0704   1.9296
[4]
,   52.333
Forecast   33   50.84224
An   14.333   22.105
Total Error   33 Total Error   6
aly
Mean Absolute   4.7777 Mean Absolute   4.4211
se,   Error   78 Error   2
1) 52.33333
Ev
2) 50.84224
alu   3) Mean absolute Error for 3 moving average is 4.777778, Exponential Smoothing is
4.42112. Since exponential smoothing error is less than 3 moving average, exponential
at
smoothing is better forecast and hence should be used
e
Q7 b
CO
-
1,2
,3;   Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the   [6]
BL-
lags and are above zero as well as below zero indicating stationarity. There is no need for
Ap   difference for this data.
ply
,
An
********** 8 **********
--- page 9 ---
aly
se,
Ev
alu
at
e
The model selection is done on the basis of following parameters
1. Requirement of stationarity (in this case d = 0)
2. BIC as low as possible
3. All lags (except intercept) need to be significant
4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
In above case
Sr   Model   BIC   Description   Result
No
1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, Model
without   lag sig   cannot be
removing   problem – Residual ACF &   used
outliers   PACF not within range
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,.   Model
without   Residual ACF & PACF within   cannot be
removing   range   used
outliers   problem – d=1, all lags not
sig,
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag   Model
without   sig, Residual ACF & PACF   cannot be
removing   within range   used
outliers   problem – d=1
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig, Model
without   problem – Residual ACF &   cannot be
removing   PACF not within range   used
outliers   all lags not sig.
5   ARIMA(1,0,0)   8.962   All correct + minimum BIC +   Model can
after   Simplest possible model   be used
removing
outliers
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Model   30   31   32   33   34   35
Demand EV - Forecas   2026   2015   2007   2001   1996   1992
Model_1   t
********** 9 **********
--- page 10 ---
UCL   2148   2150   2149   2147   2144   2142
LCL   1905   1881   1865   1855   1847   1842
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper b73677824b63

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_DS_7052/Business Analytics/ANS_Business Analytics(703TM0C003)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 08 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (EXTC)/MBA
Tech (IT)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 08 May 2026   Time: 02:00 pm to 04:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Template for TEE Exam Set 1
Q1
Answer briefly:
a   Explain the concept of Bias–Variance Tradeoff in predictive modeling. How does
it impact model performance? Illustrate your answer by explaining what happens
.   in cases of underfitting and overfitting.
Answer: The Bias–Variance Tradeoff refers to the balance between two types of errors
in a predictive model:
CO   • Bias is the error due to overly simplistic assumptions in the model. High bias leads
-1;   to underfitting, where the model fails to capture the underlying pattern in the data.
• Variance is the error due to excessive sensitivity to training data. High variance
BL-   leads to overfitting, where the model captures noise along with the pattern and
Un   performs poorly on new data.   [5]
de
rst   A good model aims to minimize both bias and variance, achieving optimal predictive
an   performance.
d
•   In underfitting, the model has high bias and low variance (too simple).
•   In overfitting, the model has low bias and high variance (too complex).
Thus, the tradeoff involves selecting a model that balances bias and variance to ensure good
generalization on unseen data.
CO b
(a) Discuss the role of data pre-processing in business analytics. Briefly explain any
-1;
.   two pre-processing techniques.
BL-   [5]
Answer: Data pre-processing is a crucial step in business analytics that involves preparing
Un   raw data for analysis by improving its quality and structure. It ensures that the data is
de   accurate, consistent, and suitable for decision-making.
rst
********** 1 **********
--- page 2 ---
an
d,   Two common pre-processing techniques are:
ap
ply   1. Handling Missing Data:
Missing values can be treated by methods such as deletion, mean/median
imputation, or predictive techniques. This prevents distortion in analysis.
2. Data Normalization:
It involves scaling data into a common range to ensure that variables with larger
values do not dominate the analysis, especially in models like regression or
clustering.
Synoptic Answer
a) State the multiple regression equation. (2 Marks)
The multiple regression equation is:
Y = 197.08 + (0.348 x TV Advertising Spend) + (0.742 x social media spend) + (0.293 x
Email Marketing Spend) + (1.494 x Discount Offered)
b) Interpret the meaning of each regression coefficient. (2 Marks)
• Intercept (197.084):
Monthly sales are expected to be 197.084 (in $1000) when all marketing
Q2   expenditures are zero (not practically meaningful).
CO   • TV Spend (0.348):
A 1 unit increase in TV advertising increases sales by 0.348 units, holding other
-
variables constant.
1,2
•   Social Spend (0.742):
,3;
A 1 unit increase in social media spend increases sales by 0.742 units (highest
BL-   impact).
Ap   • Email Spend (0.293):   [10
ply   A 1 unit increase in email marketing increases sales by 0.293 units.
,   • Discount (1.494):   ]
An   A 1% increase in discount increases sales by 1.494 units.
aly
se,   c) Can the regression equation be used for prediction? (2 Marks)
Ev   The regression model can be used for prediction based on the following:
alu
at   i. ANOVA Test:
e   o Significance value = 0.000 < 0.05
o Indicates the model is statistically significant
ii.   Coefficient of Determination (R²):
o R2=0.493
o The model explains 49.3% variation in sales
o Indicates moderate explanatory power
iii.   Significance of Coefficients (t-test):
o All predictors have p-values < 0.05
o Hence, all variables are statistically significant
iv.   Autocorrelation (Durbin-Watson):
o DW = 1.847 (close to 2)
o Indicates no autocorrelation
********** 2 **********
--- page 3 ---
v.   Multicollinearity (Correlation/VIF logic):
o Correlation among independent variables is low
o Hence, no multicollinearity issue
vi.   Normality of Residuals:
o Histogram is approximately bell-shaped
o P-P plot follows diagonal
o Indicates normality assumption satisfied
vii.   Homoscedasticity:
o Residual scatter plot shows random distribution
o No funnel pattern → variance is constant
d) Determine R² and interpret its meaning. (2 Marks)
• R2=0.493
Interpretation:
49.3% of the variation in monthly sales is explained by TV spend, social media
spend, email marketing, and discount.
This indicates a moderate model fit.
e) Predict monthly sales and interpret. (2 Marks)
Given:
• TV Spend = 120
•   Social Spend = 45
• Email Spend = 30
• Discount = 10
Y=197.084 + 0.348 (120) + 0.742 (45) + 0.293 (30) + 1.494 (10)
Y = 295.964 (in $1000)
Solution:
a) Yes, factor analysis is appropriate.
Q3   • KMO = 0.698 → Acceptable (≥ 0.6), indicating adequate sampling
CO   •   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
-
b) The MSA values (diagonal elements) are above 0.5, hence all the variables are suitable
1,2
for factor analysis.
,3;
BL-   c) Using Eigenvalue > 1 criterion:
Ap   [10
ply   •   Factor 1 = 2.820
]
Ev   •   Factor 2 = 2.029
alu   •   Factor 3 = 1.669
at
Total factors retained = 3
e,
These explain ~70.35% of total variance
cre   d) Factor 1: Service Efficiency
at
e   Service Quality (0.844)
Staff Responsiveness (0.819)
Digital Ease (0.856)
Represents quality of service delivery and responsiveness
Factor 2: Trust & Financial Fairness
********** 3 **********
--- page 4 ---
Trust & Security (0.817)
Pricing Fairness (0.828)
Complaint Resolution (0.868)
Represents customer trust, fairness, and issue handling
Factor 3: Accessibility & Satisfaction
Accessibility (0.882)
Overall Satisfaction (0.748)
Represents ease of access and overall customer satisfaction
e) Factor 1 → Digital Ease (0.856)
Factor 2 → Complaint Resolution (0.868)
Factor 3 → Accessibility (0.882)
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) From Rotation Sums of Squared Loadings:
•   Factor 1 = 26.829%
•   Factor 2 = 26.587%
•   Factor 3 = 16.936%
Most important factor: Factor 1 (Service Efficiency) that explains the highest
variance.
Q4 a
Synoptic Answer
CO
Device   Distance   Class   Rank
-
C   √1 = 1.00   High   1
1,2   G   √2 = 1.41   High   2
A   √2 = 1.41   Low   3
,3;   B   √2 = 1.41   Low   4
BL-   E   √4 = 2.00   Low   5
D   √4 = 2.00   Low   6
Ap   I   √5 = 2.24   High   7
ply   H   √8 = 2.83   Low   8
F   √10 = 3.16   Low   9   [4]
,   J   √16 = 4.00   Low   10
An   k = 3 → High (2 High vs 1 Low)
k = 5 → Low (2 High vs 3 Low)
aly
Step   Marks
se,
Distance calculation   1
Ev   Nearest neighbors’ identification   1
alu   Prediction using k=3   1
Prediction using k=5   1
at
e
b Answers
Q4   [6]
********** 4 **********
--- page 5 ---
CO   i)   Discriminant Function = 0.150 - -6.861 * Debt_to_Income + 0.178*
Credit_History_Yrs + .00001* Savings_Balance
-   ii)   Structure matrix gives explanatory power of variables. Highest absolute values
1,2   ( modulus since it is correlations) indicate highest explanatory power of variables.
And lowest absolute values ( modulus since it is correlations) indicate lowest
,3;   explanatory power of variables. In this case, Savings_Balancehas highest (.945) and
Debt_to_Income (-.876) has lowest explanatory power.
BL-
iii)   H0 : The covariance matrices of the groups are same across the two groups
Ap   H1 : The covariance matrices of the groups are different across the two groups
Here the Box’s M is not significant (p value =.000 < 0.05) this suggests covariance
ply   matrices are significantly different across two groups. So assumption of equal
covariance matrices does not holds good
,
i)   Cross-validated accuracy is 96.0%.
An   Chance accuracy Calculations
aly   Risk   0   49   3   52   0.52
se,   Type   1   1   47   48   0.48
Overall Percentage   100
Ev
Chance Accuracy 0.5008
alu   Minimum required Acc
at   0.626
this data has around equal number of successes and failures. The chance accuracy for the data is
e   p(S)2 + p(F)2 = 0.5008
We need atleast 25% improvement over chance accuracy i.e. 0.5008* 1.25 = 0. 0.626 the overall
cross validated accuracy much better than minimum required accuracy also Wilk’s Lamda is low
and significant, each variable is significant and canonical correlation is high (.901) hence the
model could be used for prediction.
Answers :
Q5   1. The logistic regression model is:
CO   𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
𝑝(𝑥) =
1 + 𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
-   2. Which Tests ?
•   Wald Test: p <0.05): significant model
1,2
•   Hosmer-Lemeshow Test (p > 0.05): significant model
,3;   3. Analyze the classification table and explain its implications?
BL-
FPR (Specificity ) is 98.9
Ap   [10
TPR (Sensitivity) is 72.7
ply   ]
,   Classification accuracy is 96.0
An   Chance Accuracy is 0.8042
aly
Minimum Required accuracy is: 1.25 * Chance Accuracy = 1.00525
se,
The data has class imbalance resulting in minimum required accuracy more than 100% since
Ev   Classification accuracy is less than the required accuracy, the model could not be trusted for
prediction. On the other side, TPR is decent, indicating good percentage of success
alu
********** 5 **********
--- page 6 ---
at   4. Explain the concepts of Sensitivity and Specificity in relation to this model.
Sensitivity (Recall) = TP / (TP + FN)
e   Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Specificity (98.9%): The model correctly identifies 98.9% of non premium Cars as non
premium cars
•   Sensitivity (72.7%): The model correctly identifies 72.7% of premium Cars as premium
cars.
5. Probability of premium Car = 0.14479
Price   1.646   12
Mileage   -0.916   18
Horsepo   0.05
wer   110
Age   -0.79   3
Constant   -8.17   1
Y   -1.776
exp(-y)   5.906184
P   0.144798
6. Since probability is less than 0.5, the car is catagorised as non premium.
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his/her choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO
-
2,3   d) Cluster Characteristics Interpretation
;   We interpret each cluster by comparing high vs low mean values across variables.
BL-   Cluster 1 (n = 10): “Credit-Dependent, High-Risk Customers”
[6]
Key Observations:
Un
de   •   Savings: Low (4.80)
•   Credit Usage: Very High (7.70)
rst   •   Online Banking: Low (4.10)
an   •   Investment: Very Low (3.00)
•   Risk Appetite: Very High (8.40)
d   • Loan Dependence: Very High (8.00)
Interpretation:
• Customers do not save much
•   Highly dependent on credit and loans
•   Willing to take high financial risks
********** 6 **********
--- page 7 ---
•   Limited use of digital banking
•   Very low inclination towards investment planning
“High-Risk Borrowers” / “Credit-Driven Segment”
Cluster 2 (n = 11): “Wealth Builders / Conservative Investors”
Key Observations:
•   Savings: Very High (8.64)
•   Credit Usage: Very Low (2.18)
•   Online Banking: Very High (9.00)
•   Investment: High (7.73)
•   Risk Appetite: Very Low (1.91)
• Loan Dependence: Low (2.82)
Interpretation:
•   Strong saving habits
•   Prefer low risk financial behavior
•   Active users of digital banking
•   Invest regularly (likely safe instruments)
•   Avoid loans and credit
“Conservative Wealth Builders” / “Digital Savers”
Cluster 3 (n = 9): “Balanced / Moderate Customers”
Key Observations:
•   Savings: Moderate (6.33)
•   Credit Usage: Moderate (5.44)
•   Online Banking: Moderate (6.44)
•   Investment: Moderate (5.56)
•   Risk Appetite: Moderate (5.78)
• Loan Dependence: Moderate (5.67)
Interpretation:
•   Balanced behavior across all dimensions
• Moderate use of:
o Savings
o   Credit
o Investment
•   Neither highly risk-averse nor risk-seeking
“Balanced Customers” / “Average Financial Users”
Cluste
Profile   Key Traits
r
High credit, high risk, low
1   High-Risk Borrowers
savings
Conservative Wealth   High savings, low risk, high
2
Builders   digital
********** 7 **********
--- page 8 ---
3   Balanced Customers   Moderate across all variables
b Solution: To identify outliers using Cook’s Distance, a common rule of thumb is:
Q6   Threshold=4/n = 4/30 ≈ 0.133
Any observation with Cook’s Distance greater than 0.133 is considered influential
CO
(potential outlier).
-;
SO   [4]
•   S.No. 17 → 0.18362 (> 0.133)
-;   •   All others are below 0.133
S.No. of Outliers: 17
BL-
Q7 a Answer
3
CO   Wee   Demand   Moving   Exponential
-   k   (Units)   Averag   Smoothing alpha
e   Error   =0.4   Error
1,2   1   42   42
,3;   2   48   42   6
3   45   44.4   0.6
BL-   4   50   45   5   44.64   5.36
Ap   47.666   7.3333
5   55
67   33   46.784   8.216
ply   6   52   50   2   50.0704   1.9296
[4]
,   52.333
Forecast   33   50.84224
An   14.333   22.105
Total Error   33 Total Error   6
aly
Mean Absolute   4.7777 Mean Absolute   4.4211
se,   Error   78 Error   2
1) 52.33333
Ev
2) 50.84224
alu   3) Mean absolute Error for 3 moving average is 4.777778, Exponential Smoothing is
4.42112. Since exponential smoothing error is less than 3 moving average, exponential
at
smoothing is better forecast and hence should be used
e
Q7 b
CO
-
1,2
,3;   Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the   [6]
BL-
lags and are above zero as well as below zero indicating stationarity. There is no need for
Ap   difference for this data.
ply
,
An
********** 8 **********
--- page 9 ---
aly
se,
Ev
alu
at
e
The model selection is done on the basis of following parameters
1. Requirement of stationarity (in this case d = 0)
2. BIC as low as possible
3. All lags (except intercept) need to be significant
4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
In above case
Sr   Model   BIC   Description   Result
No
1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, Model
without   lag sig   cannot be
removing   problem – Residual ACF &   used
outliers   PACF not within range
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,.   Model
without   Residual ACF & PACF within   cannot be
removing   range   used
outliers   problem – d=1, all lags not
sig,
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag   Model
without   sig, Residual ACF & PACF   cannot be
removing   within range   used
outliers   problem – d=1
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig, Model
without   problem – Residual ACF &   cannot be
removing   PACF not within range   used
outliers   all lags not sig.
5   ARIMA(1,0,0)   8.962   All correct + minimum BIC +   Model can
after   Simplest possible model   be used
removing
outliers
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Model   30   31   32   33   34   35
Demand EV - Forecas   2026   2015   2007   2001   1996   1992
Model_1   t
********** 9 **********
--- page 10 ---
UCL   2148   2150   2149   2147   2144   2142
LCL   1905   1881   1865   1855   1847   1842
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 63a9b345dc0d

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_IT_7041/Business Analytics/ANS_Business Analytics(703TM0C003)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 08 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (EXTC)/MBA
Tech (IT)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 08 May 2026   Time: 02:00 pm to 04:00 pm (02:00 Hrs.)
Max. Marks: 50
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Template for TEE Exam Set 1
Q1
Answer briefly:
a   Explain the concept of Bias–Variance Tradeoff in predictive modeling. How does
it impact model performance? Illustrate your answer by explaining what happens
.   in cases of underfitting and overfitting.
Answer: The Bias–Variance Tradeoff refers to the balance between two types of errors
in a predictive model:
CO   • Bias is the error due to overly simplistic assumptions in the model. High bias leads
-1;   to underfitting, where the model fails to capture the underlying pattern in the data.
• Variance is the error due to excessive sensitivity to training data. High variance
BL-   leads to overfitting, where the model captures noise along with the pattern and
Un   performs poorly on new data.   [5]
de
rst   A good model aims to minimize both bias and variance, achieving optimal predictive
an   performance.
d
•   In underfitting, the model has high bias and low variance (too simple).
•   In overfitting, the model has low bias and high variance (too complex).
Thus, the tradeoff involves selecting a model that balances bias and variance to ensure good
generalization on unseen data.
CO b
(a) Discuss the role of data pre-processing in business analytics. Briefly explain any
-1;
.   two pre-processing techniques.
BL-   [5]
Answer: Data pre-processing is a crucial step in business analytics that involves preparing
Un   raw data for analysis by improving its quality and structure. It ensures that the data is
de   accurate, consistent, and suitable for decision-making.
rst
********** 1 **********
--- page 2 ---
an
d,   Two common pre-processing techniques are:
ap
ply   1. Handling Missing Data:
Missing values can be treated by methods such as deletion, mean/median
imputation, or predictive techniques. This prevents distortion in analysis.
2. Data Normalization:
It involves scaling data into a common range to ensure that variables with larger
values do not dominate the analysis, especially in models like regression or
clustering.
Synoptic Answer
a) State the multiple regression equation. (2 Marks)
The multiple regression equation is:
Y = 197.08 + (0.348 x TV Advertising Spend) + (0.742 x social media spend) + (0.293 x
Email Marketing Spend) + (1.494 x Discount Offered)
b) Interpret the meaning of each regression coefficient. (2 Marks)
• Intercept (197.084):
Monthly sales are expected to be 197.084 (in $1000) when all marketing
Q2   expenditures are zero (not practically meaningful).
CO   • TV Spend (0.348):
A 1 unit increase in TV advertising increases sales by 0.348 units, holding other
-
variables constant.
1,2
•   Social Spend (0.742):
,3;
A 1 unit increase in social media spend increases sales by 0.742 units (highest
BL-   impact).
Ap   • Email Spend (0.293):   [10
ply   A 1 unit increase in email marketing increases sales by 0.293 units.
,   • Discount (1.494):   ]
An   A 1% increase in discount increases sales by 1.494 units.
aly
se,   c) Can the regression equation be used for prediction? (2 Marks)
Ev   The regression model can be used for prediction based on the following:
alu
at   i. ANOVA Test:
e   o Significance value = 0.000 < 0.05
o Indicates the model is statistically significant
ii.   Coefficient of Determination (R²):
o R2=0.493
o The model explains 49.3% variation in sales
o Indicates moderate explanatory power
iii.   Significance of Coefficients (t-test):
o All predictors have p-values < 0.05
o Hence, all variables are statistically significant
iv.   Autocorrelation (Durbin-Watson):
o DW = 1.847 (close to 2)
o Indicates no autocorrelation
********** 2 **********
--- page 3 ---
v.   Multicollinearity (Correlation/VIF logic):
o Correlation among independent variables is low
o Hence, no multicollinearity issue
vi.   Normality of Residuals:
o Histogram is approximately bell-shaped
o P-P plot follows diagonal
o Indicates normality assumption satisfied
vii.   Homoscedasticity:
o Residual scatter plot shows random distribution
o No funnel pattern → variance is constant
d) Determine R² and interpret its meaning. (2 Marks)
• R2=0.493
Interpretation:
49.3% of the variation in monthly sales is explained by TV spend, social media
spend, email marketing, and discount.
This indicates a moderate model fit.
e) Predict monthly sales and interpret. (2 Marks)
Given:
• TV Spend = 120
•   Social Spend = 45
• Email Spend = 30
• Discount = 10
Y=197.084 + 0.348 (120) + 0.742 (45) + 0.293 (30) + 1.494 (10)
Y = 295.964 (in $1000)
Solution:
a) Yes, factor analysis is appropriate.
Q3   • KMO = 0.698 → Acceptable (≥ 0.6), indicating adequate sampling
CO   •   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
-
b) The MSA values (diagonal elements) are above 0.5, hence all the variables are suitable
1,2
for factor analysis.
,3;
BL-   c) Using Eigenvalue > 1 criterion:
Ap   [10
ply   •   Factor 1 = 2.820
]
Ev   •   Factor 2 = 2.029
alu   •   Factor 3 = 1.669
at
Total factors retained = 3
e,
These explain ~70.35% of total variance
cre   d) Factor 1: Service Efficiency
at
e   Service Quality (0.844)
Staff Responsiveness (0.819)
Digital Ease (0.856)
Represents quality of service delivery and responsiveness
Factor 2: Trust & Financial Fairness
********** 3 **********
--- page 4 ---
Trust & Security (0.817)
Pricing Fairness (0.828)
Complaint Resolution (0.868)
Represents customer trust, fairness, and issue handling
Factor 3: Accessibility & Satisfaction
Accessibility (0.882)
Overall Satisfaction (0.748)
Represents ease of access and overall customer satisfaction
e) Factor 1 → Digital Ease (0.856)
Factor 2 → Complaint Resolution (0.868)
Factor 3 → Accessibility (0.882)
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) From Rotation Sums of Squared Loadings:
•   Factor 1 = 26.829%
•   Factor 2 = 26.587%
•   Factor 3 = 16.936%
Most important factor: Factor 1 (Service Efficiency) that explains the highest
variance.
Q4 a
Synoptic Answer
CO
Device   Distance   Class   Rank
-
C   √1 = 1.00   High   1
1,2   G   √2 = 1.41   High   2
A   √2 = 1.41   Low   3
,3;   B   √2 = 1.41   Low   4
BL-   E   √4 = 2.00   Low   5
D   √4 = 2.00   Low   6
Ap   I   √5 = 2.24   High   7
ply   H   √8 = 2.83   Low   8
F   √10 = 3.16   Low   9   [4]
,   J   √16 = 4.00   Low   10
An   k = 3 → High (2 High vs 1 Low)
k = 5 → Low (2 High vs 3 Low)
aly
Step   Marks
se,
Distance calculation   1
Ev   Nearest neighbors’ identification   1
alu   Prediction using k=3   1
Prediction using k=5   1
at
e
b Answers
Q4   [6]
********** 4 **********
--- page 5 ---
CO   i)   Discriminant Function = 0.150 - -6.861 * Debt_to_Income + 0.178*
Credit_History_Yrs + .00001* Savings_Balance
-   ii)   Structure matrix gives explanatory power of variables. Highest absolute values
1,2   ( modulus since it is correlations) indicate highest explanatory power of variables.
And lowest absolute values ( modulus since it is correlations) indicate lowest
,3;   explanatory power of variables. In this case, Savings_Balancehas highest (.945) and
Debt_to_Income (-.876) has lowest explanatory power.
BL-
iii)   H0 : The covariance matrices of the groups are same across the two groups
Ap   H1 : The covariance matrices of the groups are different across the two groups
Here the Box’s M is not significant (p value =.000 < 0.05) this suggests covariance
ply   matrices are significantly different across two groups. So assumption of equal
covariance matrices does not holds good
,
i)   Cross-validated accuracy is 96.0%.
An   Chance accuracy Calculations
aly   Risk   0   49   3   52   0.52
se,   Type   1   1   47   48   0.48
Overall Percentage   100
Ev
Chance Accuracy 0.5008
alu   Minimum required Acc
at   0.626
this data has around equal number of successes and failures. The chance accuracy for the data is
e   p(S)2 + p(F)2 = 0.5008
We need atleast 25% improvement over chance accuracy i.e. 0.5008* 1.25 = 0. 0.626 the overall
cross validated accuracy much better than minimum required accuracy also Wilk’s Lamda is low
and significant, each variable is significant and canonical correlation is high (.901) hence the
model could be used for prediction.
Answers :
Q5   1. The logistic regression model is:
CO   𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
𝑝(𝑥) =
1 + 𝑒−8.170−.790(𝐴𝑔𝑒)+0.050(Horsepower)−0..916(𝑀𝑖𝑙𝑒𝑎𝑔𝑒)+1.646(Price)
-   2. Which Tests ?
•   Wald Test: p <0.05): significant model
1,2
•   Hosmer-Lemeshow Test (p > 0.05): significant model
,3;   3. Analyze the classification table and explain its implications?
BL-
FPR (Specificity ) is 98.9
Ap   [10
TPR (Sensitivity) is 72.7
ply   ]
,   Classification accuracy is 96.0
An   Chance Accuracy is 0.8042
aly
Minimum Required accuracy is: 1.25 * Chance Accuracy = 1.00525
se,
The data has class imbalance resulting in minimum required accuracy more than 100% since
Ev   Classification accuracy is less than the required accuracy, the model could not be trusted for
prediction. On the other side, TPR is decent, indicating good percentage of success
alu
********** 5 **********
--- page 6 ---
at   4. Explain the concepts of Sensitivity and Specificity in relation to this model.
Sensitivity (Recall) = TP / (TP + FN)
e   Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Specificity (98.9%): The model correctly identifies 98.9% of non premium Cars as non
premium cars
•   Sensitivity (72.7%): The model correctly identifies 72.7% of premium Cars as premium
cars.
5. Probability of premium Car = 0.14479
Price   1.646   12
Mileage   -0.916   18
Horsepo   0.05
wer   110
Age   -0.79   3
Constant   -8.17   1
Y   -1.776
exp(-y)   5.906184
P   0.144798
6. Since probability is less than 0.5, the car is catagorised as non premium.
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his/her choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO
-
2,3   d) Cluster Characteristics Interpretation
;   We interpret each cluster by comparing high vs low mean values across variables.
BL-   Cluster 1 (n = 10): “Credit-Dependent, High-Risk Customers”
[6]
Key Observations:
Un
de   •   Savings: Low (4.80)
•   Credit Usage: Very High (7.70)
rst   •   Online Banking: Low (4.10)
an   •   Investment: Very Low (3.00)
•   Risk Appetite: Very High (8.40)
d   • Loan Dependence: Very High (8.00)
Interpretation:
• Customers do not save much
•   Highly dependent on credit and loans
•   Willing to take high financial risks
********** 6 **********
--- page 7 ---
•   Limited use of digital banking
•   Very low inclination towards investment planning
“High-Risk Borrowers” / “Credit-Driven Segment”
Cluster 2 (n = 11): “Wealth Builders / Conservative Investors”
Key Observations:
•   Savings: Very High (8.64)
•   Credit Usage: Very Low (2.18)
•   Online Banking: Very High (9.00)
•   Investment: High (7.73)
•   Risk Appetite: Very Low (1.91)
• Loan Dependence: Low (2.82)
Interpretation:
•   Strong saving habits
•   Prefer low risk financial behavior
•   Active users of digital banking
•   Invest regularly (likely safe instruments)
•   Avoid loans and credit
“Conservative Wealth Builders” / “Digital Savers”
Cluster 3 (n = 9): “Balanced / Moderate Customers”
Key Observations:
•   Savings: Moderate (6.33)
•   Credit Usage: Moderate (5.44)
•   Online Banking: Moderate (6.44)
•   Investment: Moderate (5.56)
•   Risk Appetite: Moderate (5.78)
• Loan Dependence: Moderate (5.67)
Interpretation:
•   Balanced behavior across all dimensions
• Moderate use of:
o Savings
o   Credit
o Investment
•   Neither highly risk-averse nor risk-seeking
“Balanced Customers” / “Average Financial Users”
Cluste
Profile   Key Traits
r
High credit, high risk, low
1   High-Risk Borrowers
savings
Conservative Wealth   High savings, low risk, high
2
Builders   digital
********** 7 **********
--- page 8 ---
3   Balanced Customers   Moderate across all variables
b Solution: To identify outliers using Cook’s Distance, a common rule of thumb is:
Q6   Threshold=4/n = 4/30 ≈ 0.133
Any observation with Cook’s Distance greater than 0.133 is considered influential
CO
(potential outlier).
-;
SO   [4]
•   S.No. 17 → 0.18362 (> 0.133)
-;   •   All others are below 0.133
S.No. of Outliers: 17
BL-
Q7 a Answer
3
CO   Wee   Demand   Moving   Exponential
-   k   (Units)   Averag   Smoothing alpha
e   Error   =0.4   Error
1,2   1   42   42
,3;   2   48   42   6
3   45   44.4   0.6
BL-   4   50   45   5   44.64   5.36
Ap   47.666   7.3333
5   55
67   33   46.784   8.216
ply   6   52   50   2   50.0704   1.9296
[4]
,   52.333
Forecast   33   50.84224
An   14.333   22.105
Total Error   33 Total Error   6
aly
Mean Absolute   4.7777 Mean Absolute   4.4211
se,   Error   78 Error   2
1) 52.33333
Ev
2) 50.84224
alu   3) Mean absolute Error for 3 moving average is 4.777778, Exponential Smoothing is
4.42112. Since exponential smoothing error is less than 3 moving average, exponential
at
smoothing is better forecast and hence should be used
e
Q7 b
CO
-
1,2
,3;   Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the   [6]
BL-
lags and are above zero as well as below zero indicating stationarity. There is no need for
Ap   difference for this data.
ply
,
An
********** 8 **********
--- page 9 ---
aly
se,
Ev
alu
at
e
The model selection is done on the basis of following parameters
1. Requirement of stationarity (in this case d = 0)
2. BIC as low as possible
3. All lags (except intercept) need to be significant
4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
In above case
Sr   Model   BIC   Description   Result
No
1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, Model
without   lag sig   cannot be
removing   problem – Residual ACF &   used
outliers   PACF not within range
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,.   Model
without   Residual ACF & PACF within   cannot be
removing   range   used
outliers   problem – d=1, all lags not
sig,
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag   Model
without   sig, Residual ACF & PACF   cannot be
removing   within range   used
outliers   problem – d=1
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig, Model
without   problem – Residual ACF &   cannot be
removing   PACF not within range   used
outliers   all lags not sig.
5   ARIMA(1,0,0)   8.962   All correct + minimum BIC +   Model can
after   Simplest possible model   be used
removing
outliers
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Model   30   31   32   33   34   35
Demand EV - Forecas   2026   2015   2007   2001   1996   1992
Model_1   t
********** 9 **********
--- page 10 ---
UCL   2148   2150   2149   2147   2144   2142
LCL   1905   1881   1865   1855   1847   1842
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 10c105574e64

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/MBATech_Computer_7047/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025_10c105574e.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (15 pages), mean OCR confidence 36.2
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Chem)/MBA Tech (Comp)/MBA Tech (DS)/MBA
Tech (EXTC)/MBA Tech (IT)/MBA Tech (Mech)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 08 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 15 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1   [20
Answer briefly:
]
a Discuss the importance of data visualization in business analytics. What are the principles of
effective visualization? Explain how poor visualization can lead to misinterpretation of data.
.
Answer:
Data visualization converts complex data into graphical formats for better understanding.
Importance:
•   Simplifies complex information
•   Enables quick decision-making
CO-   •   Identifies trends and patterns
1;
BL-   Principles:
[5]
Und
•   Clarity and simplicity
erst
•   Appropriate chart selection
and   •   Avoid misleading scales
•   Consistent formatting
Risks of poor visualization:
•   Misinterpretation
•   Biased decisions
•   Loss of credibility
b Critically evaluate the trade-off between prediction accuracy and model interpretability. In
CO-
what business situations would you prioritize interpretability over accuracy and vice versa?   [5]
1;   .
********** 1 **********
--- page 2 ---
BL-   Answer:
Und   There is often a trade-off between model accuracy and interpretability.
erst
• High accuracy models: Neural networks, ensemble methods (less interpretable)
and,
•   Interpretable models: Linear regression, decision trees (less complex)
appl
y   When to prioritize interpretability:
•   Healthcare
•   Banking (loan approvals)
•   Regulatory environments
When to prioritize accuracy:
• Recommendation systems
•   Fraud detection
The choice depends on business context, risk, and regulatory requirements.
c Differentiate between regression and classification problems in detail. Discuss the types of
business problems suited for each and explain how model performance is evaluated in both
.
cases.
Answer:
Regression and classification are supervised learning techniques.
CO-
1,2;   •   Regression: Predicts continuous outcomes (e.g., sales forecasting)
BL-   •   Classification: Predicts categorical outcomes (e.g., churn: yes/no)
Und
[5]
Evaluation metrics:
erst
and,
•   Regression: R², RMSE, MAE
appl   •   Classification: Accuracy, Precision, Recall, F1-score
y
Applications:
•   Regression → Pricing, demand forecasting
•   Classification → Credit scoring, fraud detection
d Explain the bias-variance trade-off in the context of machine learning models. How does it
CO-   impact model performance? Discuss techniques to achieve an optimal balance.
.
2,3;
BL-
Answer:   [5]
Und
The bias-variance trade-off explains model performance in terms of underfitting and
erst   overfitting.
and,
• High Bias: Model is too simple → underfitting
********** 2 **********
--- page 3 ---
appl   • High Variance: Model is too complex → overfitting
y
Impact:
• Poor generalization to new data
Balancing techniques:
•   Cross-validation
•   Regularization (Lasso, Ridge)
•   Pruning decision trees
•   Increasing training data
An optimal model minimizes both bias and variance.
a) Which model was applied, and why? (2 Marks)
b) State the multiple regression equation. (3 Marks)
c) Interpret the meaning of each regression coefficient. (3 Marks)
d) Can the regression equation be used for prediction? Explain. (5 Marks)
e) Determine the coefficient of multiple determination and interpret its meaning. (3
Marks)
f) Predict exam marks for the following values of independent variables. (4 Marks)
X1   X2   X3   X4
20   85   7   3
Q2
CO-
Synoptic
1,2,
a) Which model was applied, and why? (2 Marks)
3;
Stepwise Multiple Linear Regression was applied.
BL-   [2
Appl   Reason:
0]
y,   • There is one dependent variable (Final Marks)
Anal   • Multiple independent variables are considered
yse,
Eval   • Stepwise method selects only statistically significant variables automatically
uate   b) State the multiple regression equation. (3 Marks)
From Final Model (Model 3):
Final Marks = 29.869 + 1.350(Study Hours) + 0.493(Attendance)
−1.881(Social Media Hours)
c) Interpret the meaning of each regression coefficient. (3 Marks)
•   Intercept (29.869):
Base marks when all predictors are zero (not practically meaningful)
********** 3 **********
--- page 4 ---
• Study Hours (1.350):
Each additional hour of study increases marks by 1.350 (strong positive
effect)
• Attendance (0.493):
A 1% increase in attendance increases marks by 0.493
•   Social Media Hours (-1.881):
Each additional hour spent on social media reduces marks by 1.881
(negative impact)
d) Can the regression equation be used for prediction? (5 Marks)
The model can be used for prediction based on:
1. ANOVA Test:
o p-value = 0.000 < 0.05 → model is statistically significant
2. R² Value:
o R2 = 0.490→ explains 49% variation (moderate fit)
3. Significance of Variables:
o All included variables have p < 0.05 → statistically significant
4. Durbin-Watson:
o DW = 2.305 (~2) → no serious autocorrelation
5. Multicollinearity:
o Tolerance values high → no multicollinearity
6. Normality:
o Histogram is approximately normal
o P-P plot follows diagonal
7. Homoscedasticity:
o Residual scatterplot shows random distribution
********** 4 **********
--- page 5 ---
The model is statistically significant, all predictors are significant, and assumptions
are satisfied. Hence, it can be reliably used for prediction.
e) Determine R² and interpret. (3 Marks)
• 𝑅2 = 0.490
Interpretation:
49% of variation in final marks is explained by study hours, attendance, and social
media usage.
f) Predict exam marks. (4 Marks)
Given:
• Study Hours = 20
• Attendance = 85
•   Social Media Hours = 7
(Note: Sleep Hours is excluded in final model)
𝑌= 29.869 + 1.350(20) + 0.493(85) −1.881(7)
𝑌= 85.607 ≈85.61
Predicted Final Marks = 85.61
a Answer following questions:
a) Is factor analysis appropriate for this dataset? Justify. (4)
b) What will you conclude from Anti-image correlation matrix? (2)
c) How many factors would you retain? What is the total variance explained by the
retained factors. (4)
Q3
d) Name the factors. (4)
CO-
1,2,   e) Which variable has the highest loading on each factor? (2)
3;   f)   Is there any variable that should be removed? Justify. (2)
BL-   g) Which factor appears to be the most important in influencing patient perception? (2)
[2
Appl
y   Solution:   0]
Eval   a) Yes, factor analysis is appropriate.
• KMO = 0.692 → Acceptable (≥ 0.6), indicating adequate sampling
uate
,   •   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
crea   •   Variables are sufficiently correlated
te
b) Diagonal values (MSA) are mostly above 0.5, therefore variables are suitable.
c) Using Eigenvalue > 1 criterion:
•   Factor 1 = 2.813
•   Factor 2 = 2.060
•   Factor 3 = 1.650
********** 5 **********
--- page 6 ---
Total factors retained = 3. These explain ~70.54% of total variance
d) Factor 1: Clinical Service Quality
•   Doctor Competence (DC)
•   Nursing Care (NC)
•   Medical Equipment (ME)
Factor 2: Service Experience Quality
•   Hospital Cleanliness (HC)
• Treatment Cost Fairness (TC)
•   Complaint Resolution (CR)
Factor 3: Patient Outcome & Efficiency
•   Waiting Time Management (WT)
•   Overall Satisfaction (OS)
e)   Factor 1 → Medical Equipment (ME)
Factor 2 → Complaint Resolution (CR)
Factor 3 → Waiting Time Management (WT)
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) Clinical Service Quality
a
Synoptic
Employee   Distance   Class   Rank
Q4
E1   √2 = 1.41   Stay   1
CO-   E2   √2 = 1.41   Stay   2
1,2,   E3   √1 = 1.00   Leave   3
3;   E7   √2 = 1.41   Leave   4
BL-   E5   √4 = 2.00   Leave   5
[1
Appl   E4   √4 = 2.00   Stay   6
0]
y,   E8   √5 = 2.24   Stay   7
E9   √8 = 2.83   Leave   8
Anal
E6   √10 = 3.16   Stay   9
yse,
E10   √8 = 2.83   Stay   10
Eval
k = 3
uate   Stay, Stay, Leave → Stay
k = 5
Leave, Stay, Leave, Leave, Leave → Leave
********** 6 **********
--- page 7 ---
Step   Marks
Distance calculation   4
Nearest neighbors’ identification   2
Prediction using k=3   2
Prediction using k=5   2
b
Ans
a) To predict the model, identify the multivariate technique used with the
justification of using the same.
Ans.: The multivariate technique used here is the linear discriminant analysis
as the dependent variable is having two categories and the list of independent
variables are all continuous. Also, the output is related to the model fitting in
terms of discriminant functional form.
b) Write out the functional form of the model.
Ans.: The functional form can be written as follows:
x4   -3.294
Q4   x6   .466
x7   3.677
CO-
D = -3.294* X4 + .466 * X6 + 3.677 * X7
1,2,   c) State the test statistic /s used to test the goodness of fit of the model?
The Wilk’s Lambda is used to assess the goodness of fit of the model. The
3;
discriminant function is highly significant as the p-value (.000) is < 0.01 and
BL-   displays a canonical correlation of 0.837. We interpret this correlation by
squaring it (.837)2 = 0.700569. Thus, 70 percent of the variance in the [1
Appl
dependent variable (X8) can be accounted for (explained) by this model.   0]
y,   d) How would you interpret the classification table?
Ans. Classification matrices for the observations were calculated, and the
Anal
results are shown in classification table. The sample shows prediction accuracy
yse,   of 94.8 percent.
e) Rank the discriminating variables and state the most and the least important
Eval
one which classifies the note as genuine and counterfeit. On what basis you
uate   will rank the discriminating variables?
Variables in the Analysis
Tolera   F to   Wilks'   Rank
Step   nce   Remove Lambda
3   x6   .904   32.937   .346   3
x7   .059 266.003   .684   1
x4   .059 169.073   .544   2
The most important discriminating variable is X7 and the least is X6 in discriminating the
product being classified as rejected and accepted.
The ranks are given based on the F-statistic (higher the value better the rank i.e. 1) or Wilk’s
Lambda (lower the value better the rank i.e. 1)
a Ans   [1
Q5   a) Write down the model in equation form.
Ans. the equation is written as   5]
********** 7 **********
--- page 8 ---
CO-   Ln(odds) = -1.77 + 1.011* Diffclty + 0.928 Season(1) - .418 * Season(2)
1,2,   b) What are the measures of coefficient of determination for this model, interpret them.
Ans. ; the measures of coefficient of determination for this model is Cox and Snell R2
3;   and Nagelkerke R2 is an adjustment over Cox and Snell R2 Cox and Snell's R 2 is based
BL-   on the log likelihood for the model compared to the log likelihood for a baseline model.
However, with categorical outcomes, it has a theoretical maximum value of less than 1,
Appl   even for a "perfect" model. Nagelkerke's R 2 is an adjusted version of the Cox &
Snell R-square that adjusts the scale of the statistic to cover the full range from 0 to 1. In
y,
our case the values are on lower side indicating a poor explained variation by this model.
Anal   c) Interpret the classification table.
yse,   Ans. The classification table shows that Sensitivity is 66.7% and specificity is 88.9 %.
Eval   Overall the model classifies the cases correctly 80% of times.
uate
b A study was conducted to understand SALES PERFORMANCE (Monthly sales in ₹ thousands)
based on the following parameters:
• TRAINING SESSIONS (Number of training sessions attended per month)
• SALES EXPERIENCE (Years of experience in sales)
• CUSTOMER INTERACTION (Average number of customer interactions per day)
• ADMINISTRATIVE TIME (Hours spent on non-selling activities daily)
Cook’s Distance was calculated for the data and is given in the following table. Identify
outliers, if present, in the data with proper justification. Only mention S.No. of the outliers.
S.No.   Cook’s Distance
1   0.00185
2   0.01247
3   0.00096
4   0.00278
5   0.00563
6   0.00112
Q5   7   0.00845
8   0.01123
CO-;   9   0.00214   [5]
SO-;   10   0.01678
11   0.02245
BL-   12   0.03890
13   0.00312
14   0.01967
15   0.06945
16   0.00088
17   0.15278
18   0.14034
19   0.01356
20   0.16523
21   0.07654
22   0.02467
23   0.00789
24   0.00934
25   0.00547
26   0.01012
27   0.00105
28   0.00476
29   0.00058
30   0.00201
********** 8 **********
--- page 9 ---
a) How many clusters are appropriate for this data? Explain (4 Marks)
b) Who are the members of the group (give case number)? (3 marks)
c) What would you conclude from ANOVA? (3 Marks)
d) What are characteristics of each group? (6 marks)
e) Based on the cluster analysis performed on customer responses, identify the
most profitable Automobile buyer segment. Justify your answer (4 Marks)
Solution: ( Any other cluster solution with appropriate explaination is
considered correct)
a. According to Dendrogram 5 cluster solution is appropriate for the data.
b. Student may write the case numbers as per 5 cluster solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
d. Cluster Characteristics Interpretation
Cluster 1 (n = 10): “Economy Value Seekers”
Q6   Key Observations:
CO-
•   Price Sensitivity: Very High (8.30)
1,2,   • Mileage Importance: Very High (9.30)
3;   • Brand: Moderate (6.30)
•   Safety: High (7.80)
BL-   • Luxury: Very Low (3.10)
•   Resale: High (6.90)   [2
Appl
0]
y,
Interpretation:
Anal
yse,   •   Strong focus on affordability and fuel efficiency
•   Value practical benefits (mileage + resale)
Eval   • Not interested in luxury features
uate   • Moderate concern for brand
Suggested Name:
“Economy Buyers” / “Value Seekers”
Cluster 2 (n = 5): “Luxury-Oriented Buyers”
Key Observations:
•   Price Sensitivity: Very Low (2.60)
•   Mileage: Low (4.00)
• Brand: High (7.00)
•   Safety: Moderate (5.80)
• Luxury: Very High (8.40)
•   Resale: Low (4.20)
********** 9 **********
--- page 10 ---
Interpretation:
•   Willing to pay premium prices
•   Strong preference for luxury and brand image
•   Less concerned about:
o Mileage
o Resale value
Suggested Name:
“Luxury Buyers” / “Premium Segment”
Cluster 3 (n = 5): “Practical Balanced Buyers”
Key Observations:
•   Price: Moderate (6.00)
•   Mileage: High (7.00)
• Brand: Moderate (6.00)
•   Safety: Moderate-High (6.80)
• Luxury: Moderate (5.00)
•   Resale: Moderate (6.40)
Interpretation:
•   Balanced preferences across all attributes
•   Consider both:
o Performance (mileage)
o   Practical value (resale)
•   Neither highly price-sensitive nor luxury-driven
Suggested Name:
“Balanced Buyers” / “Practical Consumers”
Cluster 4 (n = 5): “Brand-Conscious Luxury Seekers”
Key Observations:
•   Price Sensitivity: Low (3.20)
•   Mileage: Low (3.40)
• Brand: Very High (8.40)
•   Safety: Moderate (6.60)
• Luxury: Very High (9.00)
•   Resale: Low (4.00)
Interpretation:
•   Strong focus on brand prestige and luxury
********** 10 **********
--- page 11 ---
•   Willing to ignore:
o Mileage
o Resale value
•   Likely status-driven buyers
Suggested Name:
“Status Seekers” / “Brand-Luxury Buyers”
Cluster 5 (n = 5): “Value-Conscious Balanced Buyers”
Key Observations:
Price: Moderate (6.00)
•   Mileage: High (7.00)
• Brand: High (7.40)
•   Safety: High (7.20)
• Luxury: Moderate (5.20)
•   Resale: Moderate (6.00)
Interpretation:
•   Value both performance and brand
•   Balanced orientation toward:
o Safety
o Mileage
• Moderate interest in luxury
Suggested Name:
“Smart Value Buyers” / “Quality Seekers”
Comparison Summary
Factor   C1   C2   C3   C4   C5
Price   Moderat   Moderat
High   Low   Low
Sensitivity   e   e
Very
Mileage   Low High   Low   High
High
Hig Moderat Very   Moderat
Luxury   Low
h   e   High   e
Moderat Hig Moderat Very
Brand   High
e   h   e   High
Key Insight (High-Scoring Point)
The data reveals 5 distinct automobile buyer segments:
1. Economy-focused buyers
********** 11 **********
--- page 12 ---
2. Luxury-focused buyers
3. Balanced practical buyers
4. Status-driven premium buyers
5. Quality-conscious value buyers
Strong differentiation → very meaningful clustering
Most Profitable Segment
Cluster 4 (Brand-Luxury Buyers)
Reason:
•   Highest preference for:
o Luxury
o Brand
• Low price sensitivity → high margins
Alternative answer: Cluster 2 also acceptable (luxury buyers)
a   a) Calculate a three month moving average for months three to eight. What would be
your forecast for the demand in 9th month?   (3 marks)
b) Apply exponential smoothing with a smoothing constant of 0.4 to derive a
forecast for the demand in 9th month. (3 marks)
c) Which of the two forecasts for 9th month do you prefer and why? (4
marks)Solution:
Q7
CO-
1,2,   (a) The three month moving average for months 3 to 9 is given by:
3;
Month   Sale   Forecast   Error
BL-   1   160
[1
Appl   2   110
3   130   0]
y,
4   160   133.3333   711.1111
Anal   5   180   133.3333   2177.778
6   150   156.6667   44.44444
yse,
7   200   163.3333   1344.444
Eval   8   220   176.6667   1877.778
uate   9   180   190   100
10   150   200   2500
Forecas
t   183.3333
Error   1250.794
********** 12 **********
--- page 13 ---
The forecast for month 10 is just the moving average for the month before that i.e. the
moving average for month 9 = m9 = 20.33.
Hence (as we cannot have fractional demand) the forecast for month 9 is 183.3333
(b) Applying exponential smoothing with a smoothing constant of 0.4 we get:
0.4
Month   Sale   Forecast   Error
1   160   170
2   110   166   3136
3   130   143.6   184.96
4   160   138.16   476.9856
5   180   146.896   1095.875
6   150   160.1376   102.7709
7   200   156.0826   1928.742
8   220   173.6495   2148.366
9   180   192.1897   148.5893
10   150   187.3138   1392.322
Forecas
t   172.3883
Error   1179.401
Forecast : 172.3883
(c) To compare the two forecasts we calculate the mean squared deviation (MSD). If we do
this, we find that for the moving average
Overall then we see that the Exponential Smoothing method appears to give the best one
month ahead forecasts as it has a lower MSD. Hence we prefer the forecast of 172.3883
that has been produced by the Exponential Smoothing
b Answers
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below,
Q7   the lags and are above zero as well as below zero indicating stationarity. There is no need
for difference for this data.
CO-
1,2,
3;
BL-
[1
Appl
0]
y,
Anal
yse,
Eval
uate
The model selection is done on the basis of following parameters
1. Requirement of stationarity (in this case d = 0)
********** 13 **********
--- page 14 ---
2. BIC as low as possible
3. All lags (except intercept) need to be significant
4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
Any simplest model that satisfies above parameters is the best model and can be used
for forecasting.
In above case
Sr   Model   BIC   Description   Result
No
1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, Model
without   lag sig   cannot be
removing   problem – Residual ACF &   used
outliers   PACF not within range
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,.   Model
without   Residual ACF & PACF within   cannot be
removing   range   used
outliers   problem – d=1, all lags not
sig,
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag   Model
without   sig, Residual ACF & PACF   cannot be
removing   within range   used
outliers   problem – d=1
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig, Model
without   problem – Residual ACF &   cannot be
removing   PACF not within range   used
outliers   all lags not sig.
5   ARIMA(1,0,0)   8.962   All correct + minimum BIC +   Model can
after   Simplest possible model   be used
removing
outliers
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Model   30   31   32   33   34   35
Demand   Forecas   2026   2015   2007   2001   1996   1992
Solar-   t
Model_1   UCL   2148   2150   2149   2147   2144   2142
LCL   1905   1881   1865   1855   1847   1842
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is
not too wide for initial forecasts. As the forecasting period extends, width becomes
wider making forecasts untrusted.
********** 14 **********
--- page 15 ---
FAC OR CC 7] eae ek ak
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 6f5fdaa2125c

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_Computer_7047/Business Analytics/ANS_Business Analytics(703TM0C003)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 04 Jul 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (EXTC)/MBA
Tech (IT)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 04 Jul 2026   Time: 02:00 pm to 04:00 pm (02:00 Hrs.)
Max. Marks: 50
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the difference between parametric and non-parametric methods in statistical
modeling. How do their assumptions affect model flexibility and performance? Illustrate
. your answer with suitable examples.
Answer: Parametric methods assume a specific functional form for the model and a fixed
number of parameters. They rely on strong assumptions about the data distribution (e.g.,
normality). Examples include linear regression and logistic regression. These methods
CO   are generally simple, fast, and require less data, but may perform poorly if assumptions
-1;   are violated.
Non-parametric methods do not assume a fixed functional form and are more flexible in
BL-   capturing complex patterns in the data. Examples include decision trees and k-nearest
Un   neighbors (KNN). These methods make fewer assumptions but typically require more [5]
de   data and can be computationally intensive.
rst   In terms of performance:
an
d   • Parametric methods may underfit if the model is too simple.
• Non-parametric methods may overfit if not properly controlled.
Thus, the choice depends on the data structure, sample size, and the tradeoff between
simplicity and flexibility.
CO b Explain the importance of data cleaning in business analytics. Briefly describe any two data
cleaning techniques.
-1;   . Answer: Data cleaning is the process of identifying and correcting errors, inconsistencies,
and inaccuracies in the dataset. It is essential in business analytics because poor-quality   [5]
BL-   data can lead to incorrect conclusions and poor decision-making.
Un
de   Two common data cleaning techniques are:
rst
********** 1 **********
--- page 2 ---
an   1. Handling Missing Values:
d,   Missing data can be treated by deletion or imputation (mean, median, or predictive
ap   methods) to maintain dataset completeness.
ply   2. Outlier Detection and Treatment:
Extreme values are identified using statistical methods (e.g., Z-score, IQR) and
can be removed or adjusted to prevent distortion in results.
Synoptic Answer
a) State the regression equation (Final Model). (2 Marks)
From Model 2 (Final Stepwise Model):
House Price = 75457.677 + 94.444 (House Size) − 1524.106 (House Age)
b) Interpret regression coefficients. (2 Marks)
•   Intercept (75457.677):
Base price when all predictors are zero (not practically meaningful)
Q2
CO   • House Size (94.444):
-   A 1 sq. ft increase in house size increases price by $94.444
1,2   (Strong positive impact, highly significant p = 0.000)
,3;
BL-   • House Age (-1524.106):
Ap   Each additional year reduces house price by $1524.106
ply   (Negative relationship, significant p = 0.019)   [10
,   ]
c) Can the regression equation be used for prediction? (2 Marks)
An
The model can be used for prediction based on:
aly
se,   i. ANOVA Test:
Ev   o p-value = 0.000 < 0.05 → model is statistically significant
alu   ii.   R² Value:
at   o R2=0.478 → explains 47.8% variation (moderate fit)
e   iii.   Significance of Variables:
o Both variables in final model are statistically significant
iv.   Durbin-Watson:
o DW = 2.000 → no autocorrelation
v.   Multicollinearity:
o Tolerance values ≈ 1 → no multicollinearity
vi.   Normality:
o Histogram bell-shaped, P-P plot near diagonal
vii.   Homoscedasticity:
o Residual scatterplot shows random distribution
********** 2 **********
--- page 3 ---
Final Conclusion:
The model is statistically significant, all included variables are significant, and
assumptions are satisfied. Hence, the regression model can be reliably used for
prediction.
d) Determine R² and interpret. (2 Marks)
• R2=0.478
Interpretation:
47.8% of variation in house price is explained by house size and house age.
e) Predict house price. (2 Marks)
Given:
• House Size = 1800
• House Age = 12
Y = 75457.677 + 94.444 (1800) − 1524.106 (12)
Y = 227167.605
Predicted House Price = $227,168
Solution:
a) Yes, factor analysis is appropriate.
• KMO = 0.692 → Acceptable (≥ 0.6), indicating adequate sampling
•   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
•   Variables are sufficiently correlated
Q3   b) Diagonal values (MSA) are mostly above 0.5, therefore variables are suitable.
CO   c) Using Eigenvalue > 1 criterion:
-   •   Factor 1 = 2.813
1,2   •   Factor 2 = 2.060
,3;   •   Factor 3 = 1.650
Total factors retained = 3. These explain ~70.54% of total variance
BL-
d) Factor 1: Academic Experience   [10
Ap
• Teaching Quality (0.827)
ply   •   Faculty Support (0.813)   ]
Ev   •   Digital Learning (0.875)
alu   Represents quality of teaching and academic support
at   Factor 2: Administrative & Support Services
e,   • Campus Safety (0.802)
cre   • Fee Fairness (0.829)
at   • Grievance Handling (0.891)
e   Represents institutional fairness, safety, and grievance handling
Factor 3: Infrastructure & Satisfaction
•   Infrastructure (0.888)
•   Overall Satisfaction (0.743)
Represents physical facilities and overall student satisfaction
e)   Factor 1 → Digital Learning (0.875)
Factor 2 → Grievance Handling (0.891)
Factor 3 → Infrastructure (0.888)
********** 3 **********
--- page 4 ---
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) From Rotation Sums of Squared Loadings:
•   Factor 1 = 26.794%
•   Factor 2 = 26.772%
•   Factor 3 = 16.976%
Most important factor: Factor 1 (Academic Experience)
Q4 a   Synoptic Answer
Customer   Distance   Class   Rank
CO
C7   √2 = 1.41   No   1
-   C1   √2 = 1.41   Buy   2
1,2   C2   √1 = 1.00   No   3
C5   √4 = 2.00   Buy   4
,3;   C3   √4 = 2.00   Buy   5
BL-   C4   √5 = 2.24   No   6
C8   √5 = 2.24   No   7
Ap
C9   √8 = 2.83   Buy   8
ply   C6   √9 = 3.00   No   9
[4]
,   C10   √8 = 2.83   No   10
An   k = 3
aly   No, Buy, No → No
k = 5
se,   No, Buy, No, Buy, Buy → Buy
Ev
Step   Marks
alu   Distance calculation   1
at   Nearest neighbors’ identification   1
Prediction using k=3   1
e
Prediction using k=5   1
Q4 b
Answers:
CO   a) State the Discriminant function:
Canonical Discriminant Function Coefficients
-
Function
1,2   1
Response_Time   -.453
,3;   [6]
Customer_Satisfaction   .642
BL-   Task_Completion_Rate   .045
Ap   (Constant)   -4.980
Unstandardized coefficients
ply
,   D F = -4.980+-.453 x Response time +.642 x Customer_Satisfaction +.045 x
Task_Completion_Rate
********** 4 **********
--- page 5 ---
An   (since all independent variables are significant)
aly   b) How would you assess the model? Which test statistic /s used to test accuracy of
se,   the model?
1) High value of Canonical Correlation (.870)
Ev   2) Wilk’s Lamda significant
3) Classification table accuracy (since 97% > 62.5% required accuracy is attained )
alu
c. 97% of cross-validated grouped cases correctly classified.
at   Probability
e   S   50   .25
F   50   .25
Total   100
Random Accuracy   0.5
25% improvement
over RA   .625
Since all the requirements are satisfied, you can use model for prediction
c) How would you test the assumption of homogeneity of variance?
Ans: Using Box’s M test.
• Box’s M Sig = 0.039 < 0.05
• Therefore → Significant
The assumption of equal covariance matrices is violated. However, LDA can still be
used cautiously if group sizes are equal.
Answers :
Q5   It   is to be noted that the first Logistic regression out has insignificant variables hence should not
be used for answering the questions. Second output is Stepwise logistic regression Last model of
CO   the stepwise should be used for answering questions. 2 marks should be cut if student selects
incorrect model
-
1. The logistic regression model is:
1,2   P = 1/(1+e-y ) where Y = -6.256 + 0.230* Time_on_Site + 0.276 * Pages_Viewed + 0.118 *
Discount
,3;   2. Which Tests ?
•   Wald Test: p <0.05): significant Variable
BL-   •   Hosmer-Lemeshow Test (p > 0.05): significant model
Ap   3. Analyze the classification table and explain its implications?
FPR (Specificity ) is 66%
ply   TPR (Sensitivity) is 74%   [10
Classification accuracy is 70%
,   Chance Accuracy is 0.5   ]
Minimum Required accuracy is: 1.25 * Chance Accuracy = 0.625
An
33   17   50   0.5
aly   13   37   50   0.5
se,   100
0.5
Ev
0.625
alu   The model is ok, Has 25% Improvement over chance accuracy, overall accuracy 70%, True
positive rate 74%. NR2 is low but ok.
at   4. Explain the concepts of Sensitivity and Specificity in relation to this model.
e   Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
Specificity = TN / (TN + FP)
********** 5 **********
--- page 6 ---
Measures the model’s ability to correctly identify employees who stayed.
5. Probability of purchase = 0.737691
Time_on_Site   0.23
12
Pages_Viewe   0.276
d   10
Discount   0.118
15
Constant   -6.256   1
Y   1.034
0.35558
exp(-y)   2
0.73769
P   1
Since the probability is > 0.5 the user is catagorised as Purchaser
a
Solution:
a. According to Dendrogram 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per 3 cluster solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
d) Cluster Characteristics Interpretation
Cluster 1 (n = 7): “Highly Committed Fitness Enthusiasts”
Key Observations:
• Gym Visits: Very High (7.71)
Q6   •   Diet: Very High (9.29)
•   Cardio: Very High (8.43)
CO
•   Strength: High (6.71)
-   • Supplements: High (6.86)
2,3   •   Trainer Usage: Very High (7.71)
;
Interpretation:
BL-   •   Extremely dedicated and disciplined fitness users
•   Strong focus on:   [6]
Un   o Diet (highest among all clusters)
o Cardio + strength balance
de   •   Actively invest in:
rst   o Supplements
o Personal trainers
an   •   Likely goal-oriented (weight loss / muscle gain)
d   Suggested Name:
“Hardcore Fitness Enthusiasts” / “Premium Members”
Cluster 2 (n = 7): “Low Engagement / Casual Members”
Key Observations:
• Gym Visits: Very Low (2.57)
•   Diet: Low (4.00)
•   Cardio: Moderate-Low (5.00)
•   Strength: Low (3.14)
• Supplements: Very Low (2.14)
•   Trainer Usage: Very Low (2.00)
********** 6 **********
--- page 7 ---
Interpretation:
• Minimal participation in gym activities
• Weak commitment to:
o Diet
o Structured workouts
•   Avoid spending on:
o   Trainers
o Supplements
•   Likely:
o New members OR
o   Irregular / unmotivated users
“Casual Members” / “Low Involvement Users”
Cluster 3 (n = 6): “Moderately Active / Balanced Users”
Key Observations:
• Gym Visits: Moderate (5.83)
•   Diet: Moderate (5.83)
•   Cardio: High (7.00)
•   Strength: Moderate-High (6.00)
• Supplements: Moderate (4.83)
•   Trainer Usage: Moderate-High (6.17)
Interpretation:
•   Regular but not extreme fitness participants
•   Balanced focus on:
o Cardio (relatively high)
o Strength training
• Moderate investment in:
o   Trainers
o Supplements
•   Likely health-conscious but not highly intensive
“Moderate Fitness Users” / “Balanced Members”
Comparison Across Clusters (Very Important)
Variable   Cluster 1 Cluster 2 Cluster 3   Insight
Very   Moderat
Gym Visits   Very Low   Engagement split
High   e
Very   Moderat
Diet   Low   Lifestyle gap
High   e
Very   Moderat Spending
Trainer   Very Low
High   e   difference
Supplement   Moderat
High   Very Low   Serious vs casual
s   e
Very   Moderat
Cardio   High   Health focus
High   e
Key Insight (High Marks Point)
•   Clear 3-tier segmentation:
1. High engagement (premium users)
2. Low engagement (casual users)
********** 7 **********
--- page 8 ---
3. Moderate engagement (middle segment)
Indicates strong and meaningful clustering
Most Profitable Segment (Important Exam Add-on)
Cluster 1 (Hardcore Fitness Enthusiasts)
Reason:
•   High usage of:
o   Trainers
o Supplements
•   Likely to:
o Buy premium memberships
o Stay loyal
o Generate recurring revenue
Q6 b
CO   Solution: Using the Cook’s Distance rule of thumb:
-;   Threshold=4n=430≈0.133
• The highest value is S.No. 18 → 0.12401, which is less than 0.133
SO   [4]
•   All other values are also below the threshold
-;
So, no outliers.
BL-
a Answer
Wee   Demand   3   Exponential
Q7   k   (Units)   Moving   Smoothing alpha
Average   Error   =0.1   Error
CO
1   100   100
-   2   115   100   15
1,2   3   110   101.5   8.5
108.333   16.6666
,3;   4   125
3   7   102.35   22.65
BL-   116.666   13.3333
5   130
7   3   104.615   25.385
Ap   121.666   18.3333
6   140
7   3   107.1535   32.8465
ply
131.666   [4]
,   Forecast   7   110.43815
48.3333   104.381
An
Total Error   3 Total Error   5
aly   Mean Absolute   16.1111 Mean Absolute
Error   1 Error   20.8763
se,   1. the forecast for Week 7 using a 3-period Moving Average. : 131.6667
Ev   2. the forecast for Week 7 using Exponential Smoothing with alpha = 0.1 : 110.43815
alu
3. Calculate error for both forecasts and explain which is better. Mean Absolute error for 3
at   moving average is 16.11111 and for Exponential Smoothing with alpha = 0.1 is 20.8763
e   Since the error is less for moving average, it would be preferred over exponential
smoothing (alpha 0.1). The final forecast is 131.667
********** 8 **********
--- page 9 ---
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
The model selection is done on the basis of following parameters
,3;   1. Requirement of stationarity (in this case d = 0)
2. BIC as low as possible
BL-   3. All lags (except intercept) need to be significant
Ap   4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
ply
Any simplest model that satisfies above parameters is the best model and can be used for   [6]
,   forecasting.
All the models are with outlier analysis, if outliers not present, they are not removed.
An
In above case
aly   Sr   Model   BIC   Description   Result
No
se,   1   ARIMA(1,0,0)   6.927   problem – LB test sig   Model
Ev   Rest all fine   cannot be
used
alu   2   ARIMA(0,0,1)   7.186   problem – LB test sig ,   Model
Residual ACF & PACF not   cannot be
at
within range   used
e   Rest all fine
3   ARIMA(1,0,1)   6.240   problem – LB test sig, All Lags Model
not significant   cannot be
Rest all fine   used
4   ARIMA(2,0,0)   6.453   All requirements satisfied.   Model can
be used
5   ARIMA(1,1,1)   6.371   problem – d=1, All lags not   Model
significant, Residual ACF &   cannot be
PACF not within range   used
Final model chosen is ARIMA(2,0,0) after removing outliers hence company should use
following forecasts
Model   25   26   27   28   29
Sales-   235.59   223.57   224.06   234.2 249.82
Model_1   8
UCL   267.00   281.69   301.67   322.3 341.15
3
********** 9 **********

[Text in pictures on this page, read by OCR]
BB Coefficient
10 — Upper Confidence Limit
Lower Confidence Limit
os
oo
08
40

12 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Lag Number
--- page 10 ---
LCL   204.19   165.45   146.45   146.2 158.50
4
Comment on forecasts : the forecasts not good as the width of 95% interval is wide even for
forecasts. As the forecasting period extends, width becomes wider making forecasts
untrusted.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 97b422a363f4

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_DS_7052/Business Analytics/ANS_Business Analytics(703TM0C003)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 04 Jul 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (EXTC)/MBA
Tech (IT)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 04 Jul 2026   Time: 02:00 pm to 04:00 pm (02:00 Hrs.)
Max. Marks: 50
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the difference between parametric and non-parametric methods in statistical
modeling. How do their assumptions affect model flexibility and performance? Illustrate
. your answer with suitable examples.
Answer: Parametric methods assume a specific functional form for the model and a fixed
number of parameters. They rely on strong assumptions about the data distribution (e.g.,
normality). Examples include linear regression and logistic regression. These methods
CO   are generally simple, fast, and require less data, but may perform poorly if assumptions
-1;   are violated.
Non-parametric methods do not assume a fixed functional form and are more flexible in
BL-   capturing complex patterns in the data. Examples include decision trees and k-nearest
Un   neighbors (KNN). These methods make fewer assumptions but typically require more [5]
de   data and can be computationally intensive.
rst   In terms of performance:
an
d   • Parametric methods may underfit if the model is too simple.
• Non-parametric methods may overfit if not properly controlled.
Thus, the choice depends on the data structure, sample size, and the tradeoff between
simplicity and flexibility.
CO b Explain the importance of data cleaning in business analytics. Briefly describe any two data
cleaning techniques.
-1;   . Answer: Data cleaning is the process of identifying and correcting errors, inconsistencies,
and inaccuracies in the dataset. It is essential in business analytics because poor-quality   [5]
BL-   data can lead to incorrect conclusions and poor decision-making.
Un
de   Two common data cleaning techniques are:
rst
********** 1 **********
--- page 2 ---
an   1. Handling Missing Values:
d,   Missing data can be treated by deletion or imputation (mean, median, or predictive
ap   methods) to maintain dataset completeness.
ply   2. Outlier Detection and Treatment:
Extreme values are identified using statistical methods (e.g., Z-score, IQR) and
can be removed or adjusted to prevent distortion in results.
Synoptic Answer
a) State the regression equation (Final Model). (2 Marks)
From Model 2 (Final Stepwise Model):
House Price = 75457.677 + 94.444 (House Size) − 1524.106 (House Age)
b) Interpret regression coefficients. (2 Marks)
•   Intercept (75457.677):
Base price when all predictors are zero (not practically meaningful)
Q2
CO   • House Size (94.444):
-   A 1 sq. ft increase in house size increases price by $94.444
1,2   (Strong positive impact, highly significant p = 0.000)
,3;
BL-   • House Age (-1524.106):
Ap   Each additional year reduces house price by $1524.106
ply   (Negative relationship, significant p = 0.019)   [10
,   ]
c) Can the regression equation be used for prediction? (2 Marks)
An
The model can be used for prediction based on:
aly
se,   i. ANOVA Test:
Ev   o p-value = 0.000 < 0.05 → model is statistically significant
alu   ii.   R² Value:
at   o R2=0.478 → explains 47.8% variation (moderate fit)
e   iii.   Significance of Variables:
o Both variables in final model are statistically significant
iv.   Durbin-Watson:
o DW = 2.000 → no autocorrelation
v.   Multicollinearity:
o Tolerance values ≈ 1 → no multicollinearity
vi.   Normality:
o Histogram bell-shaped, P-P plot near diagonal
vii.   Homoscedasticity:
o Residual scatterplot shows random distribution
********** 2 **********
--- page 3 ---
Final Conclusion:
The model is statistically significant, all included variables are significant, and
assumptions are satisfied. Hence, the regression model can be reliably used for
prediction.
d) Determine R² and interpret. (2 Marks)
• R2=0.478
Interpretation:
47.8% of variation in house price is explained by house size and house age.
e) Predict house price. (2 Marks)
Given:
• House Size = 1800
• House Age = 12
Y = 75457.677 + 94.444 (1800) − 1524.106 (12)
Y = 227167.605
Predicted House Price = $227,168
Solution:
a) Yes, factor analysis is appropriate.
• KMO = 0.692 → Acceptable (≥ 0.6), indicating adequate sampling
•   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
•   Variables are sufficiently correlated
Q3   b) Diagonal values (MSA) are mostly above 0.5, therefore variables are suitable.
CO   c) Using Eigenvalue > 1 criterion:
-   •   Factor 1 = 2.813
1,2   •   Factor 2 = 2.060
,3;   •   Factor 3 = 1.650
Total factors retained = 3. These explain ~70.54% of total variance
BL-
d) Factor 1: Academic Experience   [10
Ap
• Teaching Quality (0.827)
ply   •   Faculty Support (0.813)   ]
Ev   •   Digital Learning (0.875)
alu   Represents quality of teaching and academic support
at   Factor 2: Administrative & Support Services
e,   • Campus Safety (0.802)
cre   • Fee Fairness (0.829)
at   • Grievance Handling (0.891)
e   Represents institutional fairness, safety, and grievance handling
Factor 3: Infrastructure & Satisfaction
•   Infrastructure (0.888)
•   Overall Satisfaction (0.743)
Represents physical facilities and overall student satisfaction
e)   Factor 1 → Digital Learning (0.875)
Factor 2 → Grievance Handling (0.891)
Factor 3 → Infrastructure (0.888)
********** 3 **********
--- page 4 ---
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) From Rotation Sums of Squared Loadings:
•   Factor 1 = 26.794%
•   Factor 2 = 26.772%
•   Factor 3 = 16.976%
Most important factor: Factor 1 (Academic Experience)
Q4 a   Synoptic Answer
Customer   Distance   Class   Rank
CO
C7   √2 = 1.41   No   1
-   C1   √2 = 1.41   Buy   2
1,2   C2   √1 = 1.00   No   3
C5   √4 = 2.00   Buy   4
,3;   C3   √4 = 2.00   Buy   5
BL-   C4   √5 = 2.24   No   6
C8   √5 = 2.24   No   7
Ap
C9   √8 = 2.83   Buy   8
ply   C6   √9 = 3.00   No   9
[4]
,   C10   √8 = 2.83   No   10
An   k = 3
aly   No, Buy, No → No
k = 5
se,   No, Buy, No, Buy, Buy → Buy
Ev
Step   Marks
alu   Distance calculation   1
at   Nearest neighbors’ identification   1
Prediction using k=3   1
e
Prediction using k=5   1
Q4 b
Answers:
CO   a) State the Discriminant function:
Canonical Discriminant Function Coefficients
-
Function
1,2   1
Response_Time   -.453
,3;   [6]
Customer_Satisfaction   .642
BL-   Task_Completion_Rate   .045
Ap   (Constant)   -4.980
Unstandardized coefficients
ply
,   D F = -4.980+-.453 x Response time +.642 x Customer_Satisfaction +.045 x
Task_Completion_Rate
********** 4 **********
--- page 5 ---
An   (since all independent variables are significant)
aly   b) How would you assess the model? Which test statistic /s used to test accuracy of
se,   the model?
1) High value of Canonical Correlation (.870)
Ev   2) Wilk’s Lamda significant
3) Classification table accuracy (since 97% > 62.5% required accuracy is attained )
alu
c. 97% of cross-validated grouped cases correctly classified.
at   Probability
e   S   50   .25
F   50   .25
Total   100
Random Accuracy   0.5
25% improvement
over RA   .625
Since all the requirements are satisfied, you can use model for prediction
c) How would you test the assumption of homogeneity of variance?
Ans: Using Box’s M test.
• Box’s M Sig = 0.039 < 0.05
• Therefore → Significant
The assumption of equal covariance matrices is violated. However, LDA can still be
used cautiously if group sizes are equal.
Answers :
Q5   It   is to be noted that the first Logistic regression out has insignificant variables hence should not
be used for answering the questions. Second output is Stepwise logistic regression Last model of
CO   the stepwise should be used for answering questions. 2 marks should be cut if student selects
incorrect model
-
1. The logistic regression model is:
1,2   P = 1/(1+e-y ) where Y = -6.256 + 0.230* Time_on_Site + 0.276 * Pages_Viewed + 0.118 *
Discount
,3;   2. Which Tests ?
•   Wald Test: p <0.05): significant Variable
BL-   •   Hosmer-Lemeshow Test (p > 0.05): significant model
Ap   3. Analyze the classification table and explain its implications?
FPR (Specificity ) is 66%
ply   TPR (Sensitivity) is 74%   [10
Classification accuracy is 70%
,   Chance Accuracy is 0.5   ]
Minimum Required accuracy is: 1.25 * Chance Accuracy = 0.625
An
33   17   50   0.5
aly   13   37   50   0.5
se,   100
0.5
Ev
0.625
alu   The model is ok, Has 25% Improvement over chance accuracy, overall accuracy 70%, True
positive rate 74%. NR2 is low but ok.
at   4. Explain the concepts of Sensitivity and Specificity in relation to this model.
e   Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
Specificity = TN / (TN + FP)
********** 5 **********
--- page 6 ---
Measures the model’s ability to correctly identify employees who stayed.
5. Probability of purchase = 0.737691
Time_on_Site   0.23
12
Pages_Viewe   0.276
d   10
Discount   0.118
15
Constant   -6.256   1
Y   1.034
0.35558
exp(-y)   2
0.73769
P   1
Since the probability is > 0.5 the user is catagorised as Purchaser
a
Solution:
a. According to Dendrogram 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per 3 cluster solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
d) Cluster Characteristics Interpretation
Cluster 1 (n = 7): “Highly Committed Fitness Enthusiasts”
Key Observations:
• Gym Visits: Very High (7.71)
Q6   •   Diet: Very High (9.29)
•   Cardio: Very High (8.43)
CO
•   Strength: High (6.71)
-   • Supplements: High (6.86)
2,3   •   Trainer Usage: Very High (7.71)
;
Interpretation:
BL-   •   Extremely dedicated and disciplined fitness users
•   Strong focus on:   [6]
Un   o Diet (highest among all clusters)
o Cardio + strength balance
de   •   Actively invest in:
rst   o Supplements
o Personal trainers
an   •   Likely goal-oriented (weight loss / muscle gain)
d   Suggested Name:
“Hardcore Fitness Enthusiasts” / “Premium Members”
Cluster 2 (n = 7): “Low Engagement / Casual Members”
Key Observations:
• Gym Visits: Very Low (2.57)
•   Diet: Low (4.00)
•   Cardio: Moderate-Low (5.00)
•   Strength: Low (3.14)
• Supplements: Very Low (2.14)
•   Trainer Usage: Very Low (2.00)
********** 6 **********
--- page 7 ---
Interpretation:
• Minimal participation in gym activities
• Weak commitment to:
o Diet
o Structured workouts
•   Avoid spending on:
o   Trainers
o Supplements
•   Likely:
o New members OR
o   Irregular / unmotivated users
“Casual Members” / “Low Involvement Users”
Cluster 3 (n = 6): “Moderately Active / Balanced Users”
Key Observations:
• Gym Visits: Moderate (5.83)
•   Diet: Moderate (5.83)
•   Cardio: High (7.00)
•   Strength: Moderate-High (6.00)
• Supplements: Moderate (4.83)
•   Trainer Usage: Moderate-High (6.17)
Interpretation:
•   Regular but not extreme fitness participants
•   Balanced focus on:
o Cardio (relatively high)
o Strength training
• Moderate investment in:
o   Trainers
o Supplements
•   Likely health-conscious but not highly intensive
“Moderate Fitness Users” / “Balanced Members”
Comparison Across Clusters (Very Important)
Variable   Cluster 1 Cluster 2 Cluster 3   Insight
Very   Moderat
Gym Visits   Very Low   Engagement split
High   e
Very   Moderat
Diet   Low   Lifestyle gap
High   e
Very   Moderat Spending
Trainer   Very Low
High   e   difference
Supplement   Moderat
High   Very Low   Serious vs casual
s   e
Very   Moderat
Cardio   High   Health focus
High   e
Key Insight (High Marks Point)
•   Clear 3-tier segmentation:
1. High engagement (premium users)
2. Low engagement (casual users)
********** 7 **********
--- page 8 ---
3. Moderate engagement (middle segment)
Indicates strong and meaningful clustering
Most Profitable Segment (Important Exam Add-on)
Cluster 1 (Hardcore Fitness Enthusiasts)
Reason:
•   High usage of:
o   Trainers
o Supplements
•   Likely to:
o Buy premium memberships
o Stay loyal
o Generate recurring revenue
Q6 b
CO   Solution: Using the Cook’s Distance rule of thumb:
-;   Threshold=4n=430≈0.133
• The highest value is S.No. 18 → 0.12401, which is less than 0.133
SO   [4]
•   All other values are also below the threshold
-;
So, no outliers.
BL-
a Answer
Wee   Demand   3   Exponential
Q7   k   (Units)   Moving   Smoothing alpha
Average   Error   =0.1   Error
CO
1   100   100
-   2   115   100   15
1,2   3   110   101.5   8.5
108.333   16.6666
,3;   4   125
3   7   102.35   22.65
BL-   116.666   13.3333
5   130
7   3   104.615   25.385
Ap   121.666   18.3333
6   140
7   3   107.1535   32.8465
ply
131.666   [4]
,   Forecast   7   110.43815
48.3333   104.381
An
Total Error   3 Total Error   5
aly   Mean Absolute   16.1111 Mean Absolute
Error   1 Error   20.8763
se,   1. the forecast for Week 7 using a 3-period Moving Average. : 131.6667
Ev   2. the forecast for Week 7 using Exponential Smoothing with alpha = 0.1 : 110.43815
alu
3. Calculate error for both forecasts and explain which is better. Mean Absolute error for 3
at   moving average is 16.11111 and for Exponential Smoothing with alpha = 0.1 is 20.8763
e   Since the error is less for moving average, it would be preferred over exponential
smoothing (alpha 0.1). The final forecast is 131.667
********** 8 **********
--- page 9 ---
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
The model selection is done on the basis of following parameters
,3;   1. Requirement of stationarity (in this case d = 0)
2. BIC as low as possible
BL-   3. All lags (except intercept) need to be significant
Ap   4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
ply
Any simplest model that satisfies above parameters is the best model and can be used for   [6]
,   forecasting.
All the models are with outlier analysis, if outliers not present, they are not removed.
An
In above case
aly   Sr   Model   BIC   Description   Result
No
se,   1   ARIMA(1,0,0)   6.927   problem – LB test sig   Model
Ev   Rest all fine   cannot be
used
alu   2   ARIMA(0,0,1)   7.186   problem – LB test sig ,   Model
Residual ACF & PACF not   cannot be
at
within range   used
e   Rest all fine
3   ARIMA(1,0,1)   6.240   problem – LB test sig, All Lags Model
not significant   cannot be
Rest all fine   used
4   ARIMA(2,0,0)   6.453   All requirements satisfied.   Model can
be used
5   ARIMA(1,1,1)   6.371   problem – d=1, All lags not   Model
significant, Residual ACF &   cannot be
PACF not within range   used
Final model chosen is ARIMA(2,0,0) after removing outliers hence company should use
following forecasts
Model   25   26   27   28   29
Sales-   235.59   223.57   224.06   234.2 249.82
Model_1   8
UCL   267.00   281.69   301.67   322.3 341.15
3
********** 9 **********

[Text in pictures on this page, read by OCR]
BB Coefficient
10 — Upper Confidence Limit
Lower Confidence Limit
os
oo
08
40

12 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Lag Number
--- page 10 ---
LCL   204.19   165.45   146.45   146.2 158.50
4
Comment on forecasts : the forecasts not good as the width of 95% interval is wide even for
forecasts. As the forecasting period extends, width becomes wider making forecasts
untrusted.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 1150bac34807

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_IT_7041/Business Analytics/ANS_Business Analytics(703TM0C003)_2025-2026.pdf`
- Printed on paper: max marks: 50; duration hours: 2; exam date: 04 Jul 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)/MBA Tech (EXTC)/MBA
Tech (IT)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Business Analytics
Date: 04 Jul 2026   Time: 02:00 pm to 04:00 pm (02:00 Hrs.)
Max. Marks: 50
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the difference between parametric and non-parametric methods in statistical
modeling. How do their assumptions affect model flexibility and performance? Illustrate
. your answer with suitable examples.
Answer: Parametric methods assume a specific functional form for the model and a fixed
number of parameters. They rely on strong assumptions about the data distribution (e.g.,
normality). Examples include linear regression and logistic regression. These methods
CO   are generally simple, fast, and require less data, but may perform poorly if assumptions
-1;   are violated.
Non-parametric methods do not assume a fixed functional form and are more flexible in
BL-   capturing complex patterns in the data. Examples include decision trees and k-nearest
Un   neighbors (KNN). These methods make fewer assumptions but typically require more [5]
de   data and can be computationally intensive.
rst   In terms of performance:
an
d   • Parametric methods may underfit if the model is too simple.
• Non-parametric methods may overfit if not properly controlled.
Thus, the choice depends on the data structure, sample size, and the tradeoff between
simplicity and flexibility.
CO b Explain the importance of data cleaning in business analytics. Briefly describe any two data
cleaning techniques.
-1;   . Answer: Data cleaning is the process of identifying and correcting errors, inconsistencies,
and inaccuracies in the dataset. It is essential in business analytics because poor-quality   [5]
BL-   data can lead to incorrect conclusions and poor decision-making.
Un
de   Two common data cleaning techniques are:
rst
********** 1 **********
--- page 2 ---
an   1. Handling Missing Values:
d,   Missing data can be treated by deletion or imputation (mean, median, or predictive
ap   methods) to maintain dataset completeness.
ply   2. Outlier Detection and Treatment:
Extreme values are identified using statistical methods (e.g., Z-score, IQR) and
can be removed or adjusted to prevent distortion in results.
Synoptic Answer
a) State the regression equation (Final Model). (2 Marks)
From Model 2 (Final Stepwise Model):
House Price = 75457.677 + 94.444 (House Size) − 1524.106 (House Age)
b) Interpret regression coefficients. (2 Marks)
•   Intercept (75457.677):
Base price when all predictors are zero (not practically meaningful)
Q2
CO   • House Size (94.444):
-   A 1 sq. ft increase in house size increases price by $94.444
1,2   (Strong positive impact, highly significant p = 0.000)
,3;
BL-   • House Age (-1524.106):
Ap   Each additional year reduces house price by $1524.106
ply   (Negative relationship, significant p = 0.019)   [10
,   ]
c) Can the regression equation be used for prediction? (2 Marks)
An
The model can be used for prediction based on:
aly
se,   i. ANOVA Test:
Ev   o p-value = 0.000 < 0.05 → model is statistically significant
alu   ii.   R² Value:
at   o R2=0.478 → explains 47.8% variation (moderate fit)
e   iii.   Significance of Variables:
o Both variables in final model are statistically significant
iv.   Durbin-Watson:
o DW = 2.000 → no autocorrelation
v.   Multicollinearity:
o Tolerance values ≈ 1 → no multicollinearity
vi.   Normality:
o Histogram bell-shaped, P-P plot near diagonal
vii.   Homoscedasticity:
o Residual scatterplot shows random distribution
********** 2 **********
--- page 3 ---
Final Conclusion:
The model is statistically significant, all included variables are significant, and
assumptions are satisfied. Hence, the regression model can be reliably used for
prediction.
d) Determine R² and interpret. (2 Marks)
• R2=0.478
Interpretation:
47.8% of variation in house price is explained by house size and house age.
e) Predict house price. (2 Marks)
Given:
• House Size = 1800
• House Age = 12
Y = 75457.677 + 94.444 (1800) − 1524.106 (12)
Y = 227167.605
Predicted House Price = $227,168
Solution:
a) Yes, factor analysis is appropriate.
• KMO = 0.692 → Acceptable (≥ 0.6), indicating adequate sampling
•   Bartlett’s Test: Sig. = 0.000 (< 0.05) → Significant
•   Variables are sufficiently correlated
Q3   b) Diagonal values (MSA) are mostly above 0.5, therefore variables are suitable.
CO   c) Using Eigenvalue > 1 criterion:
-   •   Factor 1 = 2.813
1,2   •   Factor 2 = 2.060
,3;   •   Factor 3 = 1.650
Total factors retained = 3. These explain ~70.54% of total variance
BL-
d) Factor 1: Academic Experience   [10
Ap
• Teaching Quality (0.827)
ply   •   Faculty Support (0.813)   ]
Ev   •   Digital Learning (0.875)
alu   Represents quality of teaching and academic support
at   Factor 2: Administrative & Support Services
e,   • Campus Safety (0.802)
cre   • Fee Fairness (0.829)
at   • Grievance Handling (0.891)
e   Represents institutional fairness, safety, and grievance handling
Factor 3: Infrastructure & Satisfaction
•   Infrastructure (0.888)
•   Overall Satisfaction (0.743)
Represents physical facilities and overall student satisfaction
e)   Factor 1 → Digital Learning (0.875)
Factor 2 → Grievance Handling (0.891)
Factor 3 → Infrastructure (0.888)
********** 3 **********
--- page 4 ---
f) All variables have high communalities (> 0.5) and all variables load clearly on one
factor. Therefore: No variable needs to be removed
g) From Rotation Sums of Squared Loadings:
•   Factor 1 = 26.794%
•   Factor 2 = 26.772%
•   Factor 3 = 16.976%
Most important factor: Factor 1 (Academic Experience)
Q4 a   Synoptic Answer
Customer   Distance   Class   Rank
CO
C7   √2 = 1.41   No   1
-   C1   √2 = 1.41   Buy   2
1,2   C2   √1 = 1.00   No   3
C5   √4 = 2.00   Buy   4
,3;   C3   √4 = 2.00   Buy   5
BL-   C4   √5 = 2.24   No   6
C8   √5 = 2.24   No   7
Ap
C9   √8 = 2.83   Buy   8
ply   C6   √9 = 3.00   No   9
[4]
,   C10   √8 = 2.83   No   10
An   k = 3
aly   No, Buy, No → No
k = 5
se,   No, Buy, No, Buy, Buy → Buy
Ev
Step   Marks
alu   Distance calculation   1
at   Nearest neighbors’ identification   1
Prediction using k=3   1
e
Prediction using k=5   1
Q4 b
Answers:
CO   a) State the Discriminant function:
Canonical Discriminant Function Coefficients
-
Function
1,2   1
Response_Time   -.453
,3;   [6]
Customer_Satisfaction   .642
BL-   Task_Completion_Rate   .045
Ap   (Constant)   -4.980
Unstandardized coefficients
ply
,   D F = -4.980+-.453 x Response time +.642 x Customer_Satisfaction +.045 x
Task_Completion_Rate
********** 4 **********
--- page 5 ---
An   (since all independent variables are significant)
aly   b) How would you assess the model? Which test statistic /s used to test accuracy of
se,   the model?
1) High value of Canonical Correlation (.870)
Ev   2) Wilk’s Lamda significant
3) Classification table accuracy (since 97% > 62.5% required accuracy is attained )
alu
c. 97% of cross-validated grouped cases correctly classified.
at   Probability
e   S   50   .25
F   50   .25
Total   100
Random Accuracy   0.5
25% improvement
over RA   .625
Since all the requirements are satisfied, you can use model for prediction
c) How would you test the assumption of homogeneity of variance?
Ans: Using Box’s M test.
• Box’s M Sig = 0.039 < 0.05
• Therefore → Significant
The assumption of equal covariance matrices is violated. However, LDA can still be
used cautiously if group sizes are equal.
Answers :
Q5   It   is to be noted that the first Logistic regression out has insignificant variables hence should not
be used for answering the questions. Second output is Stepwise logistic regression Last model of
CO   the stepwise should be used for answering questions. 2 marks should be cut if student selects
incorrect model
-
1. The logistic regression model is:
1,2   P = 1/(1+e-y ) where Y = -6.256 + 0.230* Time_on_Site + 0.276 * Pages_Viewed + 0.118 *
Discount
,3;   2. Which Tests ?
•   Wald Test: p <0.05): significant Variable
BL-   •   Hosmer-Lemeshow Test (p > 0.05): significant model
Ap   3. Analyze the classification table and explain its implications?
FPR (Specificity ) is 66%
ply   TPR (Sensitivity) is 74%   [10
Classification accuracy is 70%
,   Chance Accuracy is 0.5   ]
Minimum Required accuracy is: 1.25 * Chance Accuracy = 0.625
An
33   17   50   0.5
aly   13   37   50   0.5
se,   100
0.5
Ev
0.625
alu   The model is ok, Has 25% Improvement over chance accuracy, overall accuracy 70%, True
positive rate 74%. NR2 is low but ok.
at   4. Explain the concepts of Sensitivity and Specificity in relation to this model.
e   Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
Specificity = TN / (TN + FP)
********** 5 **********
--- page 6 ---
Measures the model’s ability to correctly identify employees who stayed.
5. Probability of purchase = 0.737691
Time_on_Site   0.23
12
Pages_Viewe   0.276
d   10
Discount   0.118
15
Constant   -6.256   1
Y   1.034
0.35558
exp(-y)   2
0.73769
P   1
Since the probability is > 0.5 the user is catagorised as Purchaser
a
Solution:
a. According to Dendrogram 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per 3 cluster solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
d) Cluster Characteristics Interpretation
Cluster 1 (n = 7): “Highly Committed Fitness Enthusiasts”
Key Observations:
• Gym Visits: Very High (7.71)
Q6   •   Diet: Very High (9.29)
•   Cardio: Very High (8.43)
CO
•   Strength: High (6.71)
-   • Supplements: High (6.86)
2,3   •   Trainer Usage: Very High (7.71)
;
Interpretation:
BL-   •   Extremely dedicated and disciplined fitness users
•   Strong focus on:   [6]
Un   o Diet (highest among all clusters)
o Cardio + strength balance
de   •   Actively invest in:
rst   o Supplements
o Personal trainers
an   •   Likely goal-oriented (weight loss / muscle gain)
d   Suggested Name:
“Hardcore Fitness Enthusiasts” / “Premium Members”
Cluster 2 (n = 7): “Low Engagement / Casual Members”
Key Observations:
• Gym Visits: Very Low (2.57)
•   Diet: Low (4.00)
•   Cardio: Moderate-Low (5.00)
•   Strength: Low (3.14)
• Supplements: Very Low (2.14)
•   Trainer Usage: Very Low (2.00)
********** 6 **********
--- page 7 ---
Interpretation:
• Minimal participation in gym activities
• Weak commitment to:
o Diet
o Structured workouts
•   Avoid spending on:
o   Trainers
o Supplements
•   Likely:
o New members OR
o   Irregular / unmotivated users
“Casual Members” / “Low Involvement Users”
Cluster 3 (n = 6): “Moderately Active / Balanced Users”
Key Observations:
• Gym Visits: Moderate (5.83)
•   Diet: Moderate (5.83)
•   Cardio: High (7.00)
•   Strength: Moderate-High (6.00)
• Supplements: Moderate (4.83)
•   Trainer Usage: Moderate-High (6.17)
Interpretation:
•   Regular but not extreme fitness participants
•   Balanced focus on:
o Cardio (relatively high)
o Strength training
• Moderate investment in:
o   Trainers
o Supplements
•   Likely health-conscious but not highly intensive
“Moderate Fitness Users” / “Balanced Members”
Comparison Across Clusters (Very Important)
Variable   Cluster 1 Cluster 2 Cluster 3   Insight
Very   Moderat
Gym Visits   Very Low   Engagement split
High   e
Very   Moderat
Diet   Low   Lifestyle gap
High   e
Very   Moderat Spending
Trainer   Very Low
High   e   difference
Supplement   Moderat
High   Very Low   Serious vs casual
s   e
Very   Moderat
Cardio   High   Health focus
High   e
Key Insight (High Marks Point)
•   Clear 3-tier segmentation:
1. High engagement (premium users)
2. Low engagement (casual users)
********** 7 **********
--- page 8 ---
3. Moderate engagement (middle segment)
Indicates strong and meaningful clustering
Most Profitable Segment (Important Exam Add-on)
Cluster 1 (Hardcore Fitness Enthusiasts)
Reason:
•   High usage of:
o   Trainers
o Supplements
•   Likely to:
o Buy premium memberships
o Stay loyal
o Generate recurring revenue
Q6 b
CO   Solution: Using the Cook’s Distance rule of thumb:
-;   Threshold=4n=430≈0.133
• The highest value is S.No. 18 → 0.12401, which is less than 0.133
SO   [4]
•   All other values are also below the threshold
-;
So, no outliers.
BL-
a Answer
Wee   Demand   3   Exponential
Q7   k   (Units)   Moving   Smoothing alpha
Average   Error   =0.1   Error
CO
1   100   100
-   2   115   100   15
1,2   3   110   101.5   8.5
108.333   16.6666
,3;   4   125
3   7   102.35   22.65
BL-   116.666   13.3333
5   130
7   3   104.615   25.385
Ap   121.666   18.3333
6   140
7   3   107.1535   32.8465
ply
131.666   [4]
,   Forecast   7   110.43815
48.3333   104.381
An
Total Error   3 Total Error   5
aly   Mean Absolute   16.1111 Mean Absolute
Error   1 Error   20.8763
se,   1. the forecast for Week 7 using a 3-period Moving Average. : 131.6667
Ev   2. the forecast for Week 7 using Exponential Smoothing with alpha = 0.1 : 110.43815
alu
3. Calculate error for both forecasts and explain which is better. Mean Absolute error for 3
at   moving average is 16.11111 and for Exponential Smoothing with alpha = 0.1 is 20.8763
e   Since the error is less for moving average, it would be preferred over exponential
smoothing (alpha 0.1). The final forecast is 131.667
********** 8 **********
--- page 9 ---
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
The model selection is done on the basis of following parameters
,3;   1. Requirement of stationarity (in this case d = 0)
2. BIC as low as possible
BL-   3. All lags (except intercept) need to be significant
Ap   4. Ljung-Box test should not be significant
5. Residual ACF & PACF should be within the lines
ply
Any simplest model that satisfies above parameters is the best model and can be used for   [6]
,   forecasting.
All the models are with outlier analysis, if outliers not present, they are not removed.
An
In above case
aly   Sr   Model   BIC   Description   Result
No
se,   1   ARIMA(1,0,0)   6.927   problem – LB test sig   Model
Ev   Rest all fine   cannot be
used
alu   2   ARIMA(0,0,1)   7.186   problem – LB test sig ,   Model
Residual ACF & PACF not   cannot be
at
within range   used
e   Rest all fine
3   ARIMA(1,0,1)   6.240   problem – LB test sig, All Lags Model
not significant   cannot be
Rest all fine   used
4   ARIMA(2,0,0)   6.453   All requirements satisfied.   Model can
be used
5   ARIMA(1,1,1)   6.371   problem – d=1, All lags not   Model
significant, Residual ACF &   cannot be
PACF not within range   used
Final model chosen is ARIMA(2,0,0) after removing outliers hence company should use
following forecasts
Model   25   26   27   28   29
Sales-   235.59   223.57   224.06   234.2 249.82
Model_1   8
UCL   267.00   281.69   301.67   322.3 341.15
3
********** 9 **********

[Text in pictures on this page, read by OCR]
BB Coefficient
10 — Upper Confidence Limit
Lower Confidence Limit
os
oo
08
40

12 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Lag Number
--- page 10 ---
LCL   204.19   165.45   146.45   146.2 158.50
4
Comment on forecasts : the forecasts not good as the width of 95% interval is wide even for
forecasts. As the forecasting period extends, width becomes wider making forecasts
untrusted.
********** 10 **********
````

## 2024-25 · Final-Exam · Sem 8 · Answer key · paper 203f7844e7b3

- Departments: Chemical
- Programmes: MBATech (CHEMICAL ENGINEERING) - 7045
- Source: `02_Question_Papers/2024/Sem_08/Final-Exam/MBATech (CHEMICAL ENGINEERING) - 7045/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Apr 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Semester VIII(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 29 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the significance of predictive analytics in gaining a competitive advantage in
. business.
Synoptic Answer:
Predictive analytics involves using historical data, statistical models, and machine learning
techniques to make predictions about future outcomes. It helps businesses make
proactive, data-driven decisions.
CO
-1;   Key Points:
Definition & Importance (1 mark) – Predictive analytics anticipates future trends based
BL-
Un   on historical patterns.   [5]
de   Key Techniques (1 mark) – Regression analysis, decision trees, neural networks, and time
rst
an   series forecasting.
d   Applications in Business (1 mark) – Demand forecasting, customer behavior analysis, risk
assessment.
Competitive Advantage (1 mark) – Helps in optimizing pricing, improving customer
retention, and enhancing operational efficiency.
Example (1 mark) – Retailers use predictive analytics to forecast inventory demand and
reduce stockouts.
********** 1 **********
--- page 2 ---
b What are the common methods to deal with missing data during data preprocessing?
.   Synoptic Answer:
Missing data can distort analysis, leading to biased results. Proper handling is crucial for
CO   reliable models.
-1;   Key Points:
BL-   1. Understanding Missing Data (1 mark) – Types: MCAR (Missing Completely at
Un   Random), MAR (Missing at Random), MNAR (Missing Not at Random).
de   2. Deletion Methods (1 mark) – Listwise deletion (removing entire rows), Pairwise   [5]
rst   deletion (removing only missing values).
an   3. Imputation Techniques (1 mark) – Mean, median, mode imputation; Regression-
d,   based imputation.
ap   4. Advanced Techniques (1 mark) – Multiple Imputation, KNN imputation,
ply   Predictive modeling.
5. Example (1 mark) – In customer survey data, missing age values can be imputed
using the median age of respondents.
c Discuss the assumptions of regression models, focusing on heteroscedasticity and
.   multicollinearity.
CO   Synoptic Answer:
-   Regression models are based on specific assumptions, and violations affect accuracy and
1,2   reliability.
;   Key Points:
BL-   1. Overview of Regression Assumptions (1 mark) – Linearity, Independence,
Un   Homoscedasticity, Normality, No multicollinearity.   [5]
de   2. Heteroscedasticity (1 mark) – Variance of residuals is unequal across
rst   observations, leading to inefficient estimates.
an   3. Detection (1 mark) – Breusch-Pagan test, White test, residual plots.
d,   4. Remedies (1 mark) – Log transformation, Weighted Least Squares (WLS), robust
ap   standard errors.
ply   5. Multicollinearity (1 mark) – High correlation among independent variables; detected
using VIF (>10 indicates concern).
d Compare K-Nearest Neighbors (KNN) classification with logistic regression.
CO
-   .   Synoptic Answer:
Both methods classify data points but differ in their approach and applicability.
2,3
Key Points:
;
1. Definition & Overview (1 mark) – KNN is a non-parametric, instance-based
BL-
learning algorithm; Logistic Regression is a statistical method for binary   [5]
Un
classification.
de
2. Mechanism (1 mark) – KNN classifies based on nearest neighbors; Logistic
rst
Regression estimates probability using the sigmoid function.
an
3. Advantages (1 mark) – KNN is simple and handles non-linearity; Logistic
d,
Regression is interpretable and computationally efficient.
ap
4. Limitations (1 mark) – KNN is computationally expensive for large datasets;
ply
Logistic Regression assumes linearity.
********** 2 **********
--- page 3 ---
5. Example (1 mark) – In customer churn prediction, Logistic Regression identifies
key drivers, while KNN finds patterns in similar customers.
Marking Scheme:
1.   Which model was applied, and why? .....01 mark
The Multiple Linear Regression (MLR) model was applied because the company wants to
predict Sales Revenue based on multiple independent variables:
•   Advertising Spend
•   Social Media Reach
•   Product Reviews
• Campaign Type (categorical variable)
MLR is appropriate as it examines the relationship between multiple predictors and a
continuous dependent variable.
2.   Identify the baseline for qualitative predictor. .....01 mark
• The qualitative predictor is Campaign Type (Online = 1, Others = 0).
• The baseline category is Others (TV and Print Ads, coded as 0).
Q2
3.   State the model equation. .....01 marks
CO   Sales Revenue=
-   -9.629+2.702(Advertising Spend)+0.809(Social Media Reach)+1.484(Product Reviews)-
2.718
1,2
,3;   4.   Interpret the coefficient of the independent variable Campaign_Online…..02marks
BL-
Ap   It can be interpreted that Sales revenue will be lowered by -2.718 units when the   [20
ply   campaign is Online than when it would be offline (others).
,   ]
An
aly   1. Explain why the constant coefficient (b₀) has no practical meaning in this context. .....01
se,   marks
Ev
alu   b0 is the predicted Sales Revenue when all predictors are zero (i.e., no advertising spend, no
social media reach, zero product reviews, and only traditional campaigns).
at
e   This scenario is unrealistic, making b0 meaningless in practical business decisions.
2. Can the equation be used for prediction? Explain. .....01 marks
Since, Campaign_Online is an insignificant predictor (p=.541) of Sales Revenue; the model
cannot be used for prediction purposes.
3. Determine the coefficient of multiple determination (R²) and interpret its significance. .....02
marks
R² = 0.963, meaning 96.3% of the variation in sales revenue is explained by the independent
variables.
This is a strong R² value, suggesting the model is effective in predicting sales revenue.
********** 3 **********
--- page 4 ---
4. Identify which variable has the highest impact on sales revenue and which has the least
impact. .....02 marks
The highest impact variable: Social Media Reach
The least impact variable: Campaign Type
9.   What does the VIF (Variance Inflation Factor) indicate? .....01 marks
The VIF values are:
•   Advertising Spend: 1.006
•   Social Media Reach: 1.038
•   Product Reviews: 1.071
• Campaign Type: 1.056
Since all VIF values are below 5, there is no significant multicollinearity, meaning the
predictors are independent and do not distort the model.
10.   Interpret the PP plot. .....01 marks
The PP plot follows a nearly straight line, indicating that residuals are normally
distributed.
Small deviations exist, but they are within acceptable limits, so the normality assumption
holds.
11.   Analyze the normality of residuals using a histogram. .....01 marks
• The histogram of residuals is approximately bell-shaped, supporting the assumption of
normality.
• No extreme skewness or outliers were detected, confirming that the model errors are well-
distributed.
12.   Interpret the residual plot and analyze the residuals: Do they show any patterns indicating
model bias or need for improvement? .....01 marks
• The residual plot shows random scatter, meaning there are no clear patterns or trends.
• No heteroscedasticity (funnel-shaped pattern) was detected, meaning variance is constant.
•   This suggests no major model bias and that the assumptions of regression hold.
13.   Examine the ANOVA table: What does the significance (p-value) tell us about the overall
model fit? .....01 marks
F-statistic p-value (which is < 0.05), meaning the model is statistically significant.
14.   Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals? .....01 marks
Durbin-Watson (DW) = 2.388, which is close to 2, meaning no significant autocorrelation
in residuals.
15.   Predict the sales revenue when:
•   Advertising Spend: $11,000
•   Social Media Reach: 130,000 users
•   Product Reviews: 9.1 (average rating)
•   Campaign Type: Online .....03 marks
Given:
•   Advertising Spend = $11,000
•   Social Media Reach = 130,000 users
•   Product Reviews = 9.1
• Campaign Type = Online (1)
Using the model equation:
Sales Revenue: 136.0494
********** 4 **********
--- page 5 ---
Answers
Synoptic
a) this is three factor solution.
Rotated Component Matrixa
Component
1   2   3
Rate Baskin Robbins on
0.298   0.199   0.804
taste
Rate Baskin Robbins on
0.025   0.186   0.919
number of flavours
Rate Baskin Robbins on
0.055   0.748   0.297
Indian flavours
Rate Baskin Robbins on
0.406   0.577   0.182
packaging
Rate Baskin Robbins on
0.15   0.853   0.102
availability
Rate Baskin Robbins on
0.667   0.478   0.044
promotional offers
Rate Baskin Robbins on
Q3   Service   0.646   0.212   0.479
Rate Baskin Robbins on
CO   Advertising   0.868   -0.001   0.06
-   Rate Baskin Robbins on
0.529   0.349   0.356
1,2   value for money
,3;   Extraction Method: Principal Component Analysis.
BL-   Rotation Method: Varimax with Kaiser Normalization.
Ap   [20
Note to evaluators : Factor names are subjective student may name them
ply   in multiple ways   ]
Ev   Factor 2 (Local
alu   Factor 1 (Service   flavours   Factor 3 (Taste
at   Advertising & Price)   Availability)   Choices)
e,   Rate Baskin Robbins on   Rate Baskin   Rate Baskin
Robbins on
cre   Service   Indian flavours   Robbins on taste
at   Rate Baskin   Rate Baskin
Rate Baskin Robbins on
e   Advertising   Robbins on   Robbins on
availability   number of flavours
Rate Baskin Robbins on
value for money
b) Variables “Rate Baskin Robbins on packaging” & “ Rate Baskin Robbins on promotional
offers” have cross loadings hence need to be removed.
c) Scree plot indicates 3 factor as good solution
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5, total
explained variance > 60% indicates a good solution, however above mentioned two
variables have cross loadings, hence the solution needs to be revised by removing these
two variables.
Factor 1 (Service Advertising & Price) is most important factor as it has highest eigen value.
e) Selecting the right number of factors is crucial in factor analysis. Here are the
commonly used methods:
1. Eigenvalues (Kaiser’s Criterion)
• Retain factors with eigenvalues > 1 (i.e., explaining more variance than a single
variable).
********** 5 **********
--- page 6 ---
• Helps in determining significant factors based on variance contribution.
• Works well when the number of variables is less than 30.
2. Scree Plot (Elbow Method)
• A graphical representation of eigenvalues.
• The plot shows a sharp decline (elbow point), after which the curve flattens.
•   Factors before the elbow are retained.
3. Variance Explained Criterion
• Choose the number of factors that together explain at least 60%-70% of the total
variance.
• The cumulative variance contribution is checked for interpretability.
5. Factor Loadings & Interpretability
• Examine factor loadings after extraction.
• The chosen number of factors should make theoretical sense and be interpretable.
a
Answer:
5NN
Standar Standar   Standar   Standar
Q4
dised   dised   dised   dised   Standardis
CO   Distanc   Distance Distance Distance ed Distance
e of 1st   of 2nd   of 3rd   of 4th   of 5th
-   Visit
Supermarke   observa observat observat observat   observation
1,2   t   tion   ion   ion   ion
N   4   6   5   6   7
,3;
N   2   2   3   7   4
BL-   N   7   3   7   4   3
N   5   7   1   3   6
Ap
N   6   5   4   2   5
ply   Y   1   4   2   5   1   [10
,   Y   3   1   6   1   2   ]
An   Rank
aly   1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
se,   3 Y   N   Y   N   N
Ev   4 N   Y   N   N   Y
5 N   N   N   Y   N
alu
Prediction Y   Y   N   N   Y
at   Actual Y   N   N   N   Y
e
Predicti
on   Actual
Y   Y
Y   N
********** 6 **********
--- page 7 ---
N   N
N   N
Y   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   2   2
Grand Total   2   3   5
Accuracy   80.00%
100.00
Recall / Sensitivity   %
Specificity   66.67%
Precision   66.67%
3NN
Rank
1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
3 Y   N   Y   N   N
Prediction Y   Y   Y   N   Y
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Row Labels   N   Y   Grand Total
Actual   N   1   2   3
Y   2   2
Grand Total   1   4   5
Accuracy   60.00%
100.00
Recall / Sensitivity   %
Specificity   33.33%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
Q4 b Answers
i)   Discriminant Function = -3.754 + .057 * Age (years) + .052 * Salary ($1000s) + 0.108 *
CO   Years at Company + .651 * Job Type -.025 * Months since Last Raise   [10
ii)   Wilks lambda signifies discriminating power for the model. Lower the value(close to
-   ]
0), better discrimination. Higher the value (close to 1 ) less discriminating power of
1,2   the model. In this case wilk’s lambda is .848 => close to 1 hence the model has poor
discriminating power.
********** 7 **********
--- page 8 ---
,3;   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of variables.
BL-   And lowest absolute values ( modulus since it is correlations) indicate lowest
Ap   explanatory power of variables. In this case, Age has highest (.539) and Job
Type(.238) has lowest explanatory power.
ply   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
,
Here the Box’s M is not significant (p value =.892 > 0.05) this suggests there is no
An   enough evidence to conclude that covariance matrices are significantly different
across two groups. So assumption of equal covariance matrices holds good
aly   v)   Cross-validated accuracy is 64.3%. this data has equal number of successes and
failures. The chance accuracy for the data is   p(S)2 + p(F)2 = 0.25+.25 = 0.5
se,   We need atleast 25% improvement over chance accuracy i.e. 0.5 * 1.25 = 62.5% the overall cross
Ev   validated accuracy is better than minimum required accuracy hence, Ideally the model could be
used for prediction, but since the power of model is too low and there are some non-significant
alu   variables in the model like Job type (sig value .084 > 0.05 indicating this variable does not add
value in the model) you can avoid using the model. You may use stepwise DA.
at
e
a
Marking Scheme:
1. Which multivariate technique is applied in this scenario, and why is it suitable? (1 Mark)
•   Multivariate Technique Applied: Logistic Regression Why?
Q5   • The dependent variable (Loan Approval: Approved=1, Rejected = 0) is binary
(categorical).
CO   •   Logistic regression models the probability of approval using predictor variables.
2. Write the function used in the model. (1 Mark)
-
The logistic regression model function is:
1,2   e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
p ( x ) = 1 + e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
,3;
3. Interpret the pseudo R-square values and their significance. (1 Mark)
BL-   • The model explains 4.7% to 26.2% of the variance in loan approval decisions.
4. Which test statistic(s) are used to evaluate the accuracy of the model? (2 Marks)
Ap   • Wald Test: p <0.05): significant model
ply   • Hosmer-Lemeshow Test (p > 0.05): significant model   [15
,   5. Analyze the classification table and explain its implications. (2 Marks)   ]
False Negatives (Type II Error):
An   • The model predicted all loans as "approved" (1) since no "0" (denials) were predicted.
aly   •   There were 2 cases where loans were actually denied (0), but the model misclassified
them as approved (1). This leads to a 0% accuracy for denied loans.
se,   True Positives:
• The model correctly classified 98 approved loans (1) as approved.
Ev
• Accuracy for approved loans is 100%.
alu   Overall Accuracy:
• 98 out of 100 cases were classified correctly, leading to an overall accuracy of 98%.
at
e   6. Define and interpret the Sensitivity and Specificity of this model. (2 Marks)
•   Sensitivity (Recall) = TP / (TP + FN)
Measures the model’s ability to correctly identify actual positives (approved loans).
•   Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify actual negatives (denied loans).
•   Sensitivity = 100%: The model perfectly identifies approved loans.
********** 8 **********
--- page 9 ---
•   Specificity = 0%: The model completely fails to identify denied loans, predicting
all as approved.
7. Interpret the coefficients of the model. (3 Marks)
Odds Ratio (Exp(B)):
• Age → A 1-year increase in Age increases odds of approval by 0.024.
• Income → A $1,000 increase in income raises odds by 0.098
•   Credit Score → A 10-point increase in Credit Score raises odds by 0.005
Loan Type (b4=1.5) → Home Loan applicants are 0.389 times more likely to be approved.
Q5 b
Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as an
CO
outlier.
-;
Here, 4/(n-k-1) = 4/ (30-3-1) = 0.154
SO   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.154)   [5]
-;
BL-
a Explain the research design for cluster analysis and differentiate between hierarchical
. and non-hierarchical clustering techniques.
Q6   Synoptic Answer:
Cluster analysis groups similar data points together based on predefined criteria.
CO   Key Points:
-
1. Definition of Cluster Analysis (1 mark) – A technique used for segmenting data
1,2   into meaningful groups.
2. Research Design (1 mark) – Identify objectives, select clustering method, choose   [5]
,3;
distance metric, validate results.
BL-   3. Hierarchical Clustering (1 mark) – Builds a nested hierarchy using agglomerative
or divisive approaches.
Ap
4. Non-Hierarchical Clustering (1 mark) – Assigns data into pre-specified clusters
ply   (e.g., K-means).
5. Comparison (1 mark) – Hierarchical is useful for small datasets; K-means is
efficient for large datasets.
Q6 b
Solution:
CO   a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
-   Students may answer the other parts as per their choice of solution, i.e. 2 or 3.
2,3   b. Student may write the case numbers as per his choice of 2 or 3 cluster solution.
;   c. ANOVA is significant for all variables (for 2 cluster solution) indicating that all
variables are contributing in the cluster analysis. This also validates the cluster
results.   [15
BL-
*Students may write for 3 cluster solution as well.
]
Un   d. What are characteristics of each group? (For 3 cluster solution)
de
Cluste   LuxaryIt   Tech   CustomerSer
rst   r   N   Online_Sho   Discount   BrandLo   ImpulseBu   EcoFrie   ems   Savv   vice
pping   s   yalty   ying   ndly   y
an   1   1   5.67   5.47   4.87   7.07   3.07   5.53   7.8   7.60
5   0
d
********** 9 **********
--- page 10 ---
2   1   7.20   7.80   8.10   5.60   6.20   3.50   4.9   4.20
0   0
Total   2   6.28   6.40   6.16   6.48   4.32   4.72   6.6   6.24
5   4
Cluster 1: Low on BrandLoyalty, EcoFriendly , Moderate on Online_Shopping, Discounts
and LuxaryItems and High on ImpulseBuying, TechSavvy and CustomerService
Cluster 2: Low/ Moderate on ImpulseBuying, LuxaryItems, TechSavvy and
CustomerService but High on Online_Shopping, Discounts, BrandLoyalty and
EcoFriendly.
*Students may write for 3 cluster solution as well.
e. Cluster 1 is likely to be more profitable because:
1. High Impulse Buying: Customers frequently make unplanned purchases, leading
to higher revenue.
2. Tech-Savvy: More likely to engage with digital promotions, e-commerce
platforms, and AI-driven recommendations, increasing sales.
3. Strong Preference for Customer Service: Willing to pay a premium for better
support and experiences, leading to higher margins.
While Cluster 2 values discounts and brand loyalty, they may focus more on price
sensitivity and long-term relationships rather than impulsive, high-margin purchases.
*Students may write for 3 cluster solution as well.
a
Q7
Answer
CO
0.6
-
Sales
1,2   Mont   Reve
nue
,3;   h   ($100
0s)   4 moving avg   Exp sm
BL-
Jan   120   125   25
Ap   Feb   135   122   169   [10
ply   Mar   140   129.8   104.04   ]
Apr   150   135.92 198.2464
,   564.0
May   160
136.25   625   144.368 244.3594
An
564.0   153.747
Jun   170
aly   146.25   625   2 264.1535
163.498
se,   Jul   180   155   625   9   272.287
Ev   173.399
165   6
alu
********** 10 **********
--- page 11 ---
at
e
Method   Forecast   MSE
4 moving   165   584.375
Expo sm alpha = 0.6   173.3996   182.4409
Exponential Smoothing with alpha = 0.6 is best as it has
minimum MSE
Final Forecast is 173.3996
b Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
,3;
BL-
The model selection is done on the basis of following parameters
Ap
1. Requirement of stationarity (in this case d = 0)
ply   2. BIC as low as possible   [10
3. All lags (except intercept) need to be significant
,   ]
4. Ljung-Box test should not be significant
An   5. Residual ACF & PACF should be within the lines
aly   Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
se,   In above case
Ev   Sr No Model   BIC   Description   Result
1   ARIMA(1,0,0   6.875   Correct : d=0, LB test not sig, lag1 sig   Model can
alu   )   & Residual ACF & PACF within range   be used
2   ARIMA(0,0,1   7.703   Correct : d=0, , lags sig. problem –   Model
at
)   Residual ACF & PACF not within range, cannot be
e   LB test sig   used
3   ARIMA(2,0,0   7.012   Correct : d=0, LB test not sig, problem Model
)   – ACF & PACF not within range, lag2   cannot be
not sig   used
4   ARIMA(1,1,0   7.012   Correct : LB test not sig, Residual ACF   Model
)   & PACF not within range   cannot be
problem – d=1, lag not sig ACF &   used
PACF not within range
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) as it satisfies all criteria, it is simplest and has lowest
BIC. hence company should use following forecasts
Model   21   22   23   24   25
Price-Model_1   Forecast   3041.33   3038.10 3035.01 3032.05 3029.23
UCL   3085.28   3098.91 3107.90 3114.46 3119.46
LCL   2997.38   2977.29 2962.12 2949.65 2939.00
Forecast
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 8 · Answer key · paper adcde1013d2c

- Departments: Electronics and Telecommunication
- Programmes: MBATech (ELECTRONICS & TELECOMMUNICATIO
- Source: `02_Question_Papers/2024/Sem_08/Final-Exam/MBATech (ELECTRONICS & TELECOMMUNICATIO_ba3ceaa3/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Apr 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Semester VIII(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 29 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the significance of predictive analytics in gaining a competitive advantage in
. business.
Synoptic Answer:
Predictive analytics involves using historical data, statistical models, and machine learning
techniques to make predictions about future outcomes. It helps businesses make
proactive, data-driven decisions.
CO
-1;   Key Points:
Definition & Importance (1 mark) – Predictive analytics anticipates future trends based
BL-
Un   on historical patterns.   [5]
de   Key Techniques (1 mark) – Regression analysis, decision trees, neural networks, and time
rst
an   series forecasting.
d   Applications in Business (1 mark) – Demand forecasting, customer behavior analysis, risk
assessment.
Competitive Advantage (1 mark) – Helps in optimizing pricing, improving customer
retention, and enhancing operational efficiency.
Example (1 mark) – Retailers use predictive analytics to forecast inventory demand and
reduce stockouts.
********** 1 **********
--- page 2 ---
b What are the common methods to deal with missing data during data preprocessing?
.   Synoptic Answer:
Missing data can distort analysis, leading to biased results. Proper handling is crucial for
CO   reliable models.
-1;   Key Points:
BL-   1. Understanding Missing Data (1 mark) – Types: MCAR (Missing Completely at
Un   Random), MAR (Missing at Random), MNAR (Missing Not at Random).
de   2. Deletion Methods (1 mark) – Listwise deletion (removing entire rows), Pairwise   [5]
rst   deletion (removing only missing values).
an   3. Imputation Techniques (1 mark) – Mean, median, mode imputation; Regression-
d,   based imputation.
ap   4. Advanced Techniques (1 mark) – Multiple Imputation, KNN imputation,
ply   Predictive modeling.
5. Example (1 mark) – In customer survey data, missing age values can be imputed
using the median age of respondents.
c Discuss the assumptions of regression models, focusing on heteroscedasticity and
.   multicollinearity.
CO   Synoptic Answer:
-   Regression models are based on specific assumptions, and violations affect accuracy and
1,2   reliability.
;   Key Points:
BL-   1. Overview of Regression Assumptions (1 mark) – Linearity, Independence,
Un   Homoscedasticity, Normality, No multicollinearity.   [5]
de   2. Heteroscedasticity (1 mark) – Variance of residuals is unequal across
rst   observations, leading to inefficient estimates.
an   3. Detection (1 mark) – Breusch-Pagan test, White test, residual plots.
d,   4. Remedies (1 mark) – Log transformation, Weighted Least Squares (WLS), robust
ap   standard errors.
ply   5. Multicollinearity (1 mark) – High correlation among independent variables; detected
using VIF (>10 indicates concern).
d Compare K-Nearest Neighbors (KNN) classification with logistic regression.
CO
-   .   Synoptic Answer:
Both methods classify data points but differ in their approach and applicability.
2,3
Key Points:
;
1. Definition & Overview (1 mark) – KNN is a non-parametric, instance-based
BL-
learning algorithm; Logistic Regression is a statistical method for binary   [5]
Un
classification.
de
2. Mechanism (1 mark) – KNN classifies based on nearest neighbors; Logistic
rst
Regression estimates probability using the sigmoid function.
an
3. Advantages (1 mark) – KNN is simple and handles non-linearity; Logistic
d,
Regression is interpretable and computationally efficient.
ap
4. Limitations (1 mark) – KNN is computationally expensive for large datasets;
ply
Logistic Regression assumes linearity.
********** 2 **********
--- page 3 ---
5. Example (1 mark) – In customer churn prediction, Logistic Regression identifies
key drivers, while KNN finds patterns in similar customers.
Marking Scheme:
1.   Which model was applied, and why? .....01 mark
The Multiple Linear Regression (MLR) model was applied because the company wants to
predict Sales Revenue based on multiple independent variables:
•   Advertising Spend
•   Social Media Reach
•   Product Reviews
• Campaign Type (categorical variable)
MLR is appropriate as it examines the relationship between multiple predictors and a
continuous dependent variable.
2.   Identify the baseline for qualitative predictor. .....01 mark
• The qualitative predictor is Campaign Type (Online = 1, Others = 0).
• The baseline category is Others (TV and Print Ads, coded as 0).
Q2
3.   State the model equation. .....01 marks
CO   Sales Revenue=
-   -9.629+2.702(Advertising Spend)+0.809(Social Media Reach)+1.484(Product Reviews)-
2.718
1,2
,3;   4.   Interpret the coefficient of the independent variable Campaign_Online…..02marks
BL-
Ap   It can be interpreted that Sales revenue will be lowered by -2.718 units when the   [20
ply   campaign is Online than when it would be offline (others).
,   ]
An
aly   1. Explain why the constant coefficient (b₀) has no practical meaning in this context. .....01
se,   marks
Ev
alu   b0 is the predicted Sales Revenue when all predictors are zero (i.e., no advertising spend, no
social media reach, zero product reviews, and only traditional campaigns).
at
e   This scenario is unrealistic, making b0 meaningless in practical business decisions.
2. Can the equation be used for prediction? Explain. .....01 marks
Since, Campaign_Online is an insignificant predictor (p=.541) of Sales Revenue; the model
cannot be used for prediction purposes.
3. Determine the coefficient of multiple determination (R²) and interpret its significance. .....02
marks
R² = 0.963, meaning 96.3% of the variation in sales revenue is explained by the independent
variables.
This is a strong R² value, suggesting the model is effective in predicting sales revenue.
********** 3 **********
--- page 4 ---
4. Identify which variable has the highest impact on sales revenue and which has the least
impact. .....02 marks
The highest impact variable: Social Media Reach
The least impact variable: Campaign Type
9.   What does the VIF (Variance Inflation Factor) indicate? .....01 marks
The VIF values are:
•   Advertising Spend: 1.006
•   Social Media Reach: 1.038
•   Product Reviews: 1.071
• Campaign Type: 1.056
Since all VIF values are below 5, there is no significant multicollinearity, meaning the
predictors are independent and do not distort the model.
10.   Interpret the PP plot. .....01 marks
The PP plot follows a nearly straight line, indicating that residuals are normally
distributed.
Small deviations exist, but they are within acceptable limits, so the normality assumption
holds.
11.   Analyze the normality of residuals using a histogram. .....01 marks
• The histogram of residuals is approximately bell-shaped, supporting the assumption of
normality.
• No extreme skewness or outliers were detected, confirming that the model errors are well-
distributed.
12.   Interpret the residual plot and analyze the residuals: Do they show any patterns indicating
model bias or need for improvement? .....01 marks
• The residual plot shows random scatter, meaning there are no clear patterns or trends.
• No heteroscedasticity (funnel-shaped pattern) was detected, meaning variance is constant.
•   This suggests no major model bias and that the assumptions of regression hold.
13.   Examine the ANOVA table: What does the significance (p-value) tell us about the overall
model fit? .....01 marks
F-statistic p-value (which is < 0.05), meaning the model is statistically significant.
14.   Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals? .....01 marks
Durbin-Watson (DW) = 2.388, which is close to 2, meaning no significant autocorrelation
in residuals.
15.   Predict the sales revenue when:
•   Advertising Spend: $11,000
•   Social Media Reach: 130,000 users
•   Product Reviews: 9.1 (average rating)
•   Campaign Type: Online .....03 marks
Given:
•   Advertising Spend = $11,000
•   Social Media Reach = 130,000 users
•   Product Reviews = 9.1
• Campaign Type = Online (1)
Using the model equation:
Sales Revenue: 136.0494
********** 4 **********
--- page 5 ---
Answers
Synoptic
a) this is three factor solution.
Rotated Component Matrixa
Component
1   2   3
Rate Baskin Robbins on
0.298   0.199   0.804
taste
Rate Baskin Robbins on
0.025   0.186   0.919
number of flavours
Rate Baskin Robbins on
0.055   0.748   0.297
Indian flavours
Rate Baskin Robbins on
0.406   0.577   0.182
packaging
Rate Baskin Robbins on
0.15   0.853   0.102
availability
Rate Baskin Robbins on
0.667   0.478   0.044
promotional offers
Rate Baskin Robbins on
Q3   Service   0.646   0.212   0.479
Rate Baskin Robbins on
CO   Advertising   0.868   -0.001   0.06
-   Rate Baskin Robbins on
0.529   0.349   0.356
1,2   value for money
,3;   Extraction Method: Principal Component Analysis.
BL-   Rotation Method: Varimax with Kaiser Normalization.
Ap   [20
Note to evaluators : Factor names are subjective student may name them
ply   in multiple ways   ]
Ev   Factor 2 (Local
alu   Factor 1 (Service   flavours   Factor 3 (Taste
at   Advertising & Price)   Availability)   Choices)
e,   Rate Baskin Robbins on   Rate Baskin   Rate Baskin
Robbins on
cre   Service   Indian flavours   Robbins on taste
at   Rate Baskin   Rate Baskin
Rate Baskin Robbins on
e   Advertising   Robbins on   Robbins on
availability   number of flavours
Rate Baskin Robbins on
value for money
b) Variables “Rate Baskin Robbins on packaging” & “ Rate Baskin Robbins on promotional
offers” have cross loadings hence need to be removed.
c) Scree plot indicates 3 factor as good solution
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5, total
explained variance > 60% indicates a good solution, however above mentioned two
variables have cross loadings, hence the solution needs to be revised by removing these
two variables.
Factor 1 (Service Advertising & Price) is most important factor as it has highest eigen value.
e) Selecting the right number of factors is crucial in factor analysis. Here are the
commonly used methods:
1. Eigenvalues (Kaiser’s Criterion)
• Retain factors with eigenvalues > 1 (i.e., explaining more variance than a single
variable).
********** 5 **********
--- page 6 ---
• Helps in determining significant factors based on variance contribution.
• Works well when the number of variables is less than 30.
2. Scree Plot (Elbow Method)
• A graphical representation of eigenvalues.
• The plot shows a sharp decline (elbow point), after which the curve flattens.
•   Factors before the elbow are retained.
3. Variance Explained Criterion
• Choose the number of factors that together explain at least 60%-70% of the total
variance.
• The cumulative variance contribution is checked for interpretability.
5. Factor Loadings & Interpretability
• Examine factor loadings after extraction.
• The chosen number of factors should make theoretical sense and be interpretable.
a
Answer:
5NN
Standar Standar   Standar   Standar
Q4
dised   dised   dised   dised   Standardis
CO   Distanc   Distance Distance Distance ed Distance
e of 1st   of 2nd   of 3rd   of 4th   of 5th
-   Visit
Supermarke   observa observat observat observat   observation
1,2   t   tion   ion   ion   ion
N   4   6   5   6   7
,3;
N   2   2   3   7   4
BL-   N   7   3   7   4   3
N   5   7   1   3   6
Ap
N   6   5   4   2   5
ply   Y   1   4   2   5   1   [10
,   Y   3   1   6   1   2   ]
An   Rank
aly   1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
se,   3 Y   N   Y   N   N
Ev   4 N   Y   N   N   Y
5 N   N   N   Y   N
alu
Prediction Y   Y   N   N   Y
at   Actual Y   N   N   N   Y
e
Predicti
on   Actual
Y   Y
Y   N
********** 6 **********
--- page 7 ---
N   N
N   N
Y   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   2   2
Grand Total   2   3   5
Accuracy   80.00%
100.00
Recall / Sensitivity   %
Specificity   66.67%
Precision   66.67%
3NN
Rank
1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
3 Y   N   Y   N   N
Prediction Y   Y   Y   N   Y
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Row Labels   N   Y   Grand Total
Actual   N   1   2   3
Y   2   2
Grand Total   1   4   5
Accuracy   60.00%
100.00
Recall / Sensitivity   %
Specificity   33.33%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
Q4 b Answers
i)   Discriminant Function = -3.754 + .057 * Age (years) + .052 * Salary ($1000s) + 0.108 *
CO   Years at Company + .651 * Job Type -.025 * Months since Last Raise   [10
ii)   Wilks lambda signifies discriminating power for the model. Lower the value(close to
-   ]
0), better discrimination. Higher the value (close to 1 ) less discriminating power of
1,2   the model. In this case wilk’s lambda is .848 => close to 1 hence the model has poor
discriminating power.
********** 7 **********
--- page 8 ---
,3;   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of variables.
BL-   And lowest absolute values ( modulus since it is correlations) indicate lowest
Ap   explanatory power of variables. In this case, Age has highest (.539) and Job
Type(.238) has lowest explanatory power.
ply   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
,
Here the Box’s M is not significant (p value =.892 > 0.05) this suggests there is no
An   enough evidence to conclude that covariance matrices are significantly different
across two groups. So assumption of equal covariance matrices holds good
aly   v)   Cross-validated accuracy is 64.3%. this data has equal number of successes and
failures. The chance accuracy for the data is   p(S)2 + p(F)2 = 0.25+.25 = 0.5
se,   We need atleast 25% improvement over chance accuracy i.e. 0.5 * 1.25 = 62.5% the overall cross
Ev   validated accuracy is better than minimum required accuracy hence, Ideally the model could be
used for prediction, but since the power of model is too low and there are some non-significant
alu   variables in the model like Job type (sig value .084 > 0.05 indicating this variable does not add
value in the model) you can avoid using the model. You may use stepwise DA.
at
e
a
Marking Scheme:
1. Which multivariate technique is applied in this scenario, and why is it suitable? (1 Mark)
•   Multivariate Technique Applied: Logistic Regression Why?
Q5   • The dependent variable (Loan Approval: Approved=1, Rejected = 0) is binary
(categorical).
CO   •   Logistic regression models the probability of approval using predictor variables.
2. Write the function used in the model. (1 Mark)
-
The logistic regression model function is:
1,2   e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
p ( x ) = 1 + e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
,3;
3. Interpret the pseudo R-square values and their significance. (1 Mark)
BL-   • The model explains 4.7% to 26.2% of the variance in loan approval decisions.
4. Which test statistic(s) are used to evaluate the accuracy of the model? (2 Marks)
Ap   • Wald Test: p <0.05): significant model
ply   • Hosmer-Lemeshow Test (p > 0.05): significant model   [15
,   5. Analyze the classification table and explain its implications. (2 Marks)   ]
False Negatives (Type II Error):
An   • The model predicted all loans as "approved" (1) since no "0" (denials) were predicted.
aly   •   There were 2 cases where loans were actually denied (0), but the model misclassified
them as approved (1). This leads to a 0% accuracy for denied loans.
se,   True Positives:
• The model correctly classified 98 approved loans (1) as approved.
Ev
• Accuracy for approved loans is 100%.
alu   Overall Accuracy:
• 98 out of 100 cases were classified correctly, leading to an overall accuracy of 98%.
at
e   6. Define and interpret the Sensitivity and Specificity of this model. (2 Marks)
•   Sensitivity (Recall) = TP / (TP + FN)
Measures the model’s ability to correctly identify actual positives (approved loans).
•   Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify actual negatives (denied loans).
•   Sensitivity = 100%: The model perfectly identifies approved loans.
********** 8 **********
--- page 9 ---
•   Specificity = 0%: The model completely fails to identify denied loans, predicting
all as approved.
7. Interpret the coefficients of the model. (3 Marks)
Odds Ratio (Exp(B)):
• Age → A 1-year increase in Age increases odds of approval by 0.024.
• Income → A $1,000 increase in income raises odds by 0.098
•   Credit Score → A 10-point increase in Credit Score raises odds by 0.005
Loan Type (b4=1.5) → Home Loan applicants are 0.389 times more likely to be approved.
Q5 b
Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as an
CO
outlier.
-;
Here, 4/(n-k-1) = 4/ (30-3-1) = 0.154
SO   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.154)   [5]
-;
BL-
a Explain the research design for cluster analysis and differentiate between hierarchical
. and non-hierarchical clustering techniques.
Q6   Synoptic Answer:
Cluster analysis groups similar data points together based on predefined criteria.
CO   Key Points:
-
1. Definition of Cluster Analysis (1 mark) – A technique used for segmenting data
1,2   into meaningful groups.
2. Research Design (1 mark) – Identify objectives, select clustering method, choose   [5]
,3;
distance metric, validate results.
BL-   3. Hierarchical Clustering (1 mark) – Builds a nested hierarchy using agglomerative
or divisive approaches.
Ap
4. Non-Hierarchical Clustering (1 mark) – Assigns data into pre-specified clusters
ply   (e.g., K-means).
5. Comparison (1 mark) – Hierarchical is useful for small datasets; K-means is
efficient for large datasets.
Q6 b
Solution:
CO   a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
-   Students may answer the other parts as per their choice of solution, i.e. 2 or 3.
2,3   b. Student may write the case numbers as per his choice of 2 or 3 cluster solution.
;   c. ANOVA is significant for all variables (for 2 cluster solution) indicating that all
variables are contributing in the cluster analysis. This also validates the cluster
results.   [15
BL-
*Students may write for 3 cluster solution as well.
]
Un   d. What are characteristics of each group? (For 3 cluster solution)
de
Cluste   LuxaryIt   Tech   CustomerSer
rst   r   N   Online_Sho   Discount   BrandLo   ImpulseBu   EcoFrie   ems   Savv   vice
pping   s   yalty   ying   ndly   y
an   1   1   5.67   5.47   4.87   7.07   3.07   5.53   7.8   7.60
5   0
d
********** 9 **********
--- page 10 ---
2   1   7.20   7.80   8.10   5.60   6.20   3.50   4.9   4.20
0   0
Total   2   6.28   6.40   6.16   6.48   4.32   4.72   6.6   6.24
5   4
Cluster 1: Low on BrandLoyalty, EcoFriendly , Moderate on Online_Shopping, Discounts
and LuxaryItems and High on ImpulseBuying, TechSavvy and CustomerService
Cluster 2: Low/ Moderate on ImpulseBuying, LuxaryItems, TechSavvy and
CustomerService but High on Online_Shopping, Discounts, BrandLoyalty and
EcoFriendly.
*Students may write for 3 cluster solution as well.
e. Cluster 1 is likely to be more profitable because:
1. High Impulse Buying: Customers frequently make unplanned purchases, leading
to higher revenue.
2. Tech-Savvy: More likely to engage with digital promotions, e-commerce
platforms, and AI-driven recommendations, increasing sales.
3. Strong Preference for Customer Service: Willing to pay a premium for better
support and experiences, leading to higher margins.
While Cluster 2 values discounts and brand loyalty, they may focus more on price
sensitivity and long-term relationships rather than impulsive, high-margin purchases.
*Students may write for 3 cluster solution as well.
a
Q7
Answer
CO
0.6
-
Sales
1,2   Mont   Reve
nue
,3;   h   ($100
0s)   4 moving avg   Exp sm
BL-
Jan   120   125   25
Ap   Feb   135   122   169   [10
ply   Mar   140   129.8   104.04   ]
Apr   150   135.92 198.2464
,   564.0
May   160
136.25   625   144.368 244.3594
An
564.0   153.747
Jun   170
aly   146.25   625   2 264.1535
163.498
se,   Jul   180   155   625   9   272.287
Ev   173.399
165   6
alu
********** 10 **********
--- page 11 ---
at
e
Method   Forecast   MSE
4 moving   165   584.375
Expo sm alpha = 0.6   173.3996   182.4409
Exponential Smoothing with alpha = 0.6 is best as it has
minimum MSE
Final Forecast is 173.3996
b Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
,3;
BL-
The model selection is done on the basis of following parameters
Ap
1. Requirement of stationarity (in this case d = 0)
ply   2. BIC as low as possible   [10
3. All lags (except intercept) need to be significant
,   ]
4. Ljung-Box test should not be significant
An   5. Residual ACF & PACF should be within the lines
aly   Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
se,   In above case
Ev   Sr No Model   BIC   Description   Result
1   ARIMA(1,0,0   6.875   Correct : d=0, LB test not sig, lag1 sig   Model can
alu   )   & Residual ACF & PACF within range   be used
2   ARIMA(0,0,1   7.703   Correct : d=0, , lags sig. problem –   Model
at
)   Residual ACF & PACF not within range, cannot be
e   LB test sig   used
3   ARIMA(2,0,0   7.012   Correct : d=0, LB test not sig, problem Model
)   – ACF & PACF not within range, lag2   cannot be
not sig   used
4   ARIMA(1,1,0   7.012   Correct : LB test not sig, Residual ACF   Model
)   & PACF not within range   cannot be
problem – d=1, lag not sig ACF &   used
PACF not within range
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) as it satisfies all criteria, it is simplest and has lowest
BIC. hence company should use following forecasts
Model   21   22   23   24   25
Price-Model_1   Forecast   3041.33   3038.10 3035.01 3032.05 3029.23
UCL   3085.28   3098.91 3107.90 3114.46 3119.46
LCL   2997.38   2977.29 2962.12 2949.65 2939.00
Forecast
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 8 · Answer key · paper 976facd18ffe

- Departments: Mechanical
- Programmes: MBATech (MECHANICAL ENGINEERING) - 7046
- Source: `02_Question_Papers/2024/Sem_08/Final-Exam/MBATech (MECHANICAL ENGINEERING) - 7046/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Apr 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Semester VIII(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 29 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the significance of predictive analytics in gaining a competitive advantage in
. business.
Synoptic Answer:
Predictive analytics involves using historical data, statistical models, and machine learning
techniques to make predictions about future outcomes. It helps businesses make
proactive, data-driven decisions.
CO
-1;   Key Points:
Definition & Importance (1 mark) – Predictive analytics anticipates future trends based
BL-
Un   on historical patterns.   [5]
de   Key Techniques (1 mark) – Regression analysis, decision trees, neural networks, and time
rst
an   series forecasting.
d   Applications in Business (1 mark) – Demand forecasting, customer behavior analysis, risk
assessment.
Competitive Advantage (1 mark) – Helps in optimizing pricing, improving customer
retention, and enhancing operational efficiency.
Example (1 mark) – Retailers use predictive analytics to forecast inventory demand and
reduce stockouts.
********** 1 **********
--- page 2 ---
b What are the common methods to deal with missing data during data preprocessing?
.   Synoptic Answer:
Missing data can distort analysis, leading to biased results. Proper handling is crucial for
CO   reliable models.
-1;   Key Points:
BL-   1. Understanding Missing Data (1 mark) – Types: MCAR (Missing Completely at
Un   Random), MAR (Missing at Random), MNAR (Missing Not at Random).
de   2. Deletion Methods (1 mark) – Listwise deletion (removing entire rows), Pairwise   [5]
rst   deletion (removing only missing values).
an   3. Imputation Techniques (1 mark) – Mean, median, mode imputation; Regression-
d,   based imputation.
ap   4. Advanced Techniques (1 mark) – Multiple Imputation, KNN imputation,
ply   Predictive modeling.
5. Example (1 mark) – In customer survey data, missing age values can be imputed
using the median age of respondents.
c Discuss the assumptions of regression models, focusing on heteroscedasticity and
.   multicollinearity.
CO   Synoptic Answer:
-   Regression models are based on specific assumptions, and violations affect accuracy and
1,2   reliability.
;   Key Points:
BL-   1. Overview of Regression Assumptions (1 mark) – Linearity, Independence,
Un   Homoscedasticity, Normality, No multicollinearity.   [5]
de   2. Heteroscedasticity (1 mark) – Variance of residuals is unequal across
rst   observations, leading to inefficient estimates.
an   3. Detection (1 mark) – Breusch-Pagan test, White test, residual plots.
d,   4. Remedies (1 mark) – Log transformation, Weighted Least Squares (WLS), robust
ap   standard errors.
ply   5. Multicollinearity (1 mark) – High correlation among independent variables; detected
using VIF (>10 indicates concern).
d Compare K-Nearest Neighbors (KNN) classification with logistic regression.
CO
-   .   Synoptic Answer:
Both methods classify data points but differ in their approach and applicability.
2,3
Key Points:
;
1. Definition & Overview (1 mark) – KNN is a non-parametric, instance-based
BL-
learning algorithm; Logistic Regression is a statistical method for binary   [5]
Un
classification.
de
2. Mechanism (1 mark) – KNN classifies based on nearest neighbors; Logistic
rst
Regression estimates probability using the sigmoid function.
an
3. Advantages (1 mark) – KNN is simple and handles non-linearity; Logistic
d,
Regression is interpretable and computationally efficient.
ap
4. Limitations (1 mark) – KNN is computationally expensive for large datasets;
ply
Logistic Regression assumes linearity.
********** 2 **********
--- page 3 ---
5. Example (1 mark) – In customer churn prediction, Logistic Regression identifies
key drivers, while KNN finds patterns in similar customers.
Marking Scheme:
1.   Which model was applied, and why? .....01 mark
The Multiple Linear Regression (MLR) model was applied because the company wants to
predict Sales Revenue based on multiple independent variables:
•   Advertising Spend
•   Social Media Reach
•   Product Reviews
• Campaign Type (categorical variable)
MLR is appropriate as it examines the relationship between multiple predictors and a
continuous dependent variable.
2.   Identify the baseline for qualitative predictor. .....01 mark
• The qualitative predictor is Campaign Type (Online = 1, Others = 0).
• The baseline category is Others (TV and Print Ads, coded as 0).
Q2
3.   State the model equation. .....01 marks
CO   Sales Revenue=
-   -9.629+2.702(Advertising Spend)+0.809(Social Media Reach)+1.484(Product Reviews)-
2.718
1,2
,3;   4.   Interpret the coefficient of the independent variable Campaign_Online…..02marks
BL-
Ap   It can be interpreted that Sales revenue will be lowered by -2.718 units when the   [20
ply   campaign is Online than when it would be offline (others).
,   ]
An
aly   1. Explain why the constant coefficient (b₀) has no practical meaning in this context. .....01
se,   marks
Ev
alu   b0 is the predicted Sales Revenue when all predictors are zero (i.e., no advertising spend, no
social media reach, zero product reviews, and only traditional campaigns).
at
e   This scenario is unrealistic, making b0 meaningless in practical business decisions.
2. Can the equation be used for prediction? Explain. .....01 marks
Since, Campaign_Online is an insignificant predictor (p=.541) of Sales Revenue; the model
cannot be used for prediction purposes.
3. Determine the coefficient of multiple determination (R²) and interpret its significance. .....02
marks
R² = 0.963, meaning 96.3% of the variation in sales revenue is explained by the independent
variables.
This is a strong R² value, suggesting the model is effective in predicting sales revenue.
********** 3 **********
--- page 4 ---
4. Identify which variable has the highest impact on sales revenue and which has the least
impact. .....02 marks
The highest impact variable: Social Media Reach
The least impact variable: Campaign Type
9.   What does the VIF (Variance Inflation Factor) indicate? .....01 marks
The VIF values are:
•   Advertising Spend: 1.006
•   Social Media Reach: 1.038
•   Product Reviews: 1.071
• Campaign Type: 1.056
Since all VIF values are below 5, there is no significant multicollinearity, meaning the
predictors are independent and do not distort the model.
10.   Interpret the PP plot. .....01 marks
The PP plot follows a nearly straight line, indicating that residuals are normally
distributed.
Small deviations exist, but they are within acceptable limits, so the normality assumption
holds.
11.   Analyze the normality of residuals using a histogram. .....01 marks
• The histogram of residuals is approximately bell-shaped, supporting the assumption of
normality.
• No extreme skewness or outliers were detected, confirming that the model errors are well-
distributed.
12.   Interpret the residual plot and analyze the residuals: Do they show any patterns indicating
model bias or need for improvement? .....01 marks
• The residual plot shows random scatter, meaning there are no clear patterns or trends.
• No heteroscedasticity (funnel-shaped pattern) was detected, meaning variance is constant.
•   This suggests no major model bias and that the assumptions of regression hold.
13.   Examine the ANOVA table: What does the significance (p-value) tell us about the overall
model fit? .....01 marks
F-statistic p-value (which is < 0.05), meaning the model is statistically significant.
14.   Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals? .....01 marks
Durbin-Watson (DW) = 2.388, which is close to 2, meaning no significant autocorrelation
in residuals.
15.   Predict the sales revenue when:
•   Advertising Spend: $11,000
•   Social Media Reach: 130,000 users
•   Product Reviews: 9.1 (average rating)
•   Campaign Type: Online .....03 marks
Given:
•   Advertising Spend = $11,000
•   Social Media Reach = 130,000 users
•   Product Reviews = 9.1
• Campaign Type = Online (1)
Using the model equation:
Sales Revenue: 136.0494
********** 4 **********
--- page 5 ---
Answers
Synoptic
a) this is three factor solution.
Rotated Component Matrixa
Component
1   2   3
Rate Baskin Robbins on
0.298   0.199   0.804
taste
Rate Baskin Robbins on
0.025   0.186   0.919
number of flavours
Rate Baskin Robbins on
0.055   0.748   0.297
Indian flavours
Rate Baskin Robbins on
0.406   0.577   0.182
packaging
Rate Baskin Robbins on
0.15   0.853   0.102
availability
Rate Baskin Robbins on
0.667   0.478   0.044
promotional offers
Rate Baskin Robbins on
Q3   Service   0.646   0.212   0.479
Rate Baskin Robbins on
CO   Advertising   0.868   -0.001   0.06
-   Rate Baskin Robbins on
0.529   0.349   0.356
1,2   value for money
,3;   Extraction Method: Principal Component Analysis.
BL-   Rotation Method: Varimax with Kaiser Normalization.
Ap   [20
Note to evaluators : Factor names are subjective student may name them
ply   in multiple ways   ]
Ev   Factor 2 (Local
alu   Factor 1 (Service   flavours   Factor 3 (Taste
at   Advertising & Price)   Availability)   Choices)
e,   Rate Baskin Robbins on   Rate Baskin   Rate Baskin
Robbins on
cre   Service   Indian flavours   Robbins on taste
at   Rate Baskin   Rate Baskin
Rate Baskin Robbins on
e   Advertising   Robbins on   Robbins on
availability   number of flavours
Rate Baskin Robbins on
value for money
b) Variables “Rate Baskin Robbins on packaging” & “ Rate Baskin Robbins on promotional
offers” have cross loadings hence need to be removed.
c) Scree plot indicates 3 factor as good solution
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5, total
explained variance > 60% indicates a good solution, however above mentioned two
variables have cross loadings, hence the solution needs to be revised by removing these
two variables.
Factor 1 (Service Advertising & Price) is most important factor as it has highest eigen value.
e) Selecting the right number of factors is crucial in factor analysis. Here are the
commonly used methods:
1. Eigenvalues (Kaiser’s Criterion)
• Retain factors with eigenvalues > 1 (i.e., explaining more variance than a single
variable).
********** 5 **********
--- page 6 ---
• Helps in determining significant factors based on variance contribution.
• Works well when the number of variables is less than 30.
2. Scree Plot (Elbow Method)
• A graphical representation of eigenvalues.
• The plot shows a sharp decline (elbow point), after which the curve flattens.
•   Factors before the elbow are retained.
3. Variance Explained Criterion
• Choose the number of factors that together explain at least 60%-70% of the total
variance.
• The cumulative variance contribution is checked for interpretability.
5. Factor Loadings & Interpretability
• Examine factor loadings after extraction.
• The chosen number of factors should make theoretical sense and be interpretable.
a
Answer:
5NN
Standar Standar   Standar   Standar
Q4
dised   dised   dised   dised   Standardis
CO   Distanc   Distance Distance Distance ed Distance
e of 1st   of 2nd   of 3rd   of 4th   of 5th
-   Visit
Supermarke   observa observat observat observat   observation
1,2   t   tion   ion   ion   ion
N   4   6   5   6   7
,3;
N   2   2   3   7   4
BL-   N   7   3   7   4   3
N   5   7   1   3   6
Ap
N   6   5   4   2   5
ply   Y   1   4   2   5   1   [10
,   Y   3   1   6   1   2   ]
An   Rank
aly   1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
se,   3 Y   N   Y   N   N
Ev   4 N   Y   N   N   Y
5 N   N   N   Y   N
alu
Prediction Y   Y   N   N   Y
at   Actual Y   N   N   N   Y
e
Predicti
on   Actual
Y   Y
Y   N
********** 6 **********
--- page 7 ---
N   N
N   N
Y   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   2   2
Grand Total   2   3   5
Accuracy   80.00%
100.00
Recall / Sensitivity   %
Specificity   66.67%
Precision   66.67%
3NN
Rank
1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
3 Y   N   Y   N   N
Prediction Y   Y   Y   N   Y
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Row Labels   N   Y   Grand Total
Actual   N   1   2   3
Y   2   2
Grand Total   1   4   5
Accuracy   60.00%
100.00
Recall / Sensitivity   %
Specificity   33.33%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
Q4 b Answers
i)   Discriminant Function = -3.754 + .057 * Age (years) + .052 * Salary ($1000s) + 0.108 *
CO   Years at Company + .651 * Job Type -.025 * Months since Last Raise   [10
ii)   Wilks lambda signifies discriminating power for the model. Lower the value(close to
-   ]
0), better discrimination. Higher the value (close to 1 ) less discriminating power of
1,2   the model. In this case wilk’s lambda is .848 => close to 1 hence the model has poor
discriminating power.
********** 7 **********
--- page 8 ---
,3;   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of variables.
BL-   And lowest absolute values ( modulus since it is correlations) indicate lowest
Ap   explanatory power of variables. In this case, Age has highest (.539) and Job
Type(.238) has lowest explanatory power.
ply   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
,
Here the Box’s M is not significant (p value =.892 > 0.05) this suggests there is no
An   enough evidence to conclude that covariance matrices are significantly different
across two groups. So assumption of equal covariance matrices holds good
aly   v)   Cross-validated accuracy is 64.3%. this data has equal number of successes and
failures. The chance accuracy for the data is   p(S)2 + p(F)2 = 0.25+.25 = 0.5
se,   We need atleast 25% improvement over chance accuracy i.e. 0.5 * 1.25 = 62.5% the overall cross
Ev   validated accuracy is better than minimum required accuracy hence, Ideally the model could be
used for prediction, but since the power of model is too low and there are some non-significant
alu   variables in the model like Job type (sig value .084 > 0.05 indicating this variable does not add
value in the model) you can avoid using the model. You may use stepwise DA.
at
e
a
Marking Scheme:
1. Which multivariate technique is applied in this scenario, and why is it suitable? (1 Mark)
•   Multivariate Technique Applied: Logistic Regression Why?
Q5   • The dependent variable (Loan Approval: Approved=1, Rejected = 0) is binary
(categorical).
CO   •   Logistic regression models the probability of approval using predictor variables.
2. Write the function used in the model. (1 Mark)
-
The logistic regression model function is:
1,2   e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
p ( x ) = 1 + e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
,3;
3. Interpret the pseudo R-square values and their significance. (1 Mark)
BL-   • The model explains 4.7% to 26.2% of the variance in loan approval decisions.
4. Which test statistic(s) are used to evaluate the accuracy of the model? (2 Marks)
Ap   • Wald Test: p <0.05): significant model
ply   • Hosmer-Lemeshow Test (p > 0.05): significant model   [15
,   5. Analyze the classification table and explain its implications. (2 Marks)   ]
False Negatives (Type II Error):
An   • The model predicted all loans as "approved" (1) since no "0" (denials) were predicted.
aly   •   There were 2 cases where loans were actually denied (0), but the model misclassified
them as approved (1). This leads to a 0% accuracy for denied loans.
se,   True Positives:
• The model correctly classified 98 approved loans (1) as approved.
Ev
• Accuracy for approved loans is 100%.
alu   Overall Accuracy:
• 98 out of 100 cases were classified correctly, leading to an overall accuracy of 98%.
at
e   6. Define and interpret the Sensitivity and Specificity of this model. (2 Marks)
•   Sensitivity (Recall) = TP / (TP + FN)
Measures the model’s ability to correctly identify actual positives (approved loans).
•   Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify actual negatives (denied loans).
•   Sensitivity = 100%: The model perfectly identifies approved loans.
********** 8 **********
--- page 9 ---
•   Specificity = 0%: The model completely fails to identify denied loans, predicting
all as approved.
7. Interpret the coefficients of the model. (3 Marks)
Odds Ratio (Exp(B)):
• Age → A 1-year increase in Age increases odds of approval by 0.024.
• Income → A $1,000 increase in income raises odds by 0.098
•   Credit Score → A 10-point increase in Credit Score raises odds by 0.005
Loan Type (b4=1.5) → Home Loan applicants are 0.389 times more likely to be approved.
Q5 b
Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as an
CO
outlier.
-;
Here, 4/(n-k-1) = 4/ (30-3-1) = 0.154
SO   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.154)   [5]
-;
BL-
a Explain the research design for cluster analysis and differentiate between hierarchical
. and non-hierarchical clustering techniques.
Q6   Synoptic Answer:
Cluster analysis groups similar data points together based on predefined criteria.
CO   Key Points:
-
1. Definition of Cluster Analysis (1 mark) – A technique used for segmenting data
1,2   into meaningful groups.
2. Research Design (1 mark) – Identify objectives, select clustering method, choose   [5]
,3;
distance metric, validate results.
BL-   3. Hierarchical Clustering (1 mark) – Builds a nested hierarchy using agglomerative
or divisive approaches.
Ap
4. Non-Hierarchical Clustering (1 mark) – Assigns data into pre-specified clusters
ply   (e.g., K-means).
5. Comparison (1 mark) – Hierarchical is useful for small datasets; K-means is
efficient for large datasets.
Q6 b
Solution:
CO   a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
-   Students may answer the other parts as per their choice of solution, i.e. 2 or 3.
2,3   b. Student may write the case numbers as per his choice of 2 or 3 cluster solution.
;   c. ANOVA is significant for all variables (for 2 cluster solution) indicating that all
variables are contributing in the cluster analysis. This also validates the cluster
results.   [15
BL-
*Students may write for 3 cluster solution as well.
]
Un   d. What are characteristics of each group? (For 3 cluster solution)
de
Cluste   LuxaryIt   Tech   CustomerSer
rst   r   N   Online_Sho   Discount   BrandLo   ImpulseBu   EcoFrie   ems   Savv   vice
pping   s   yalty   ying   ndly   y
an   1   1   5.67   5.47   4.87   7.07   3.07   5.53   7.8   7.60
5   0
d
********** 9 **********
--- page 10 ---
2   1   7.20   7.80   8.10   5.60   6.20   3.50   4.9   4.20
0   0
Total   2   6.28   6.40   6.16   6.48   4.32   4.72   6.6   6.24
5   4
Cluster 1: Low on BrandLoyalty, EcoFriendly , Moderate on Online_Shopping, Discounts
and LuxaryItems and High on ImpulseBuying, TechSavvy and CustomerService
Cluster 2: Low/ Moderate on ImpulseBuying, LuxaryItems, TechSavvy and
CustomerService but High on Online_Shopping, Discounts, BrandLoyalty and
EcoFriendly.
*Students may write for 3 cluster solution as well.
e. Cluster 1 is likely to be more profitable because:
1. High Impulse Buying: Customers frequently make unplanned purchases, leading
to higher revenue.
2. Tech-Savvy: More likely to engage with digital promotions, e-commerce
platforms, and AI-driven recommendations, increasing sales.
3. Strong Preference for Customer Service: Willing to pay a premium for better
support and experiences, leading to higher margins.
While Cluster 2 values discounts and brand loyalty, they may focus more on price
sensitivity and long-term relationships rather than impulsive, high-margin purchases.
*Students may write for 3 cluster solution as well.
a
Q7
Answer
CO
0.6
-
Sales
1,2   Mont   Reve
nue
,3;   h   ($100
0s)   4 moving avg   Exp sm
BL-
Jan   120   125   25
Ap   Feb   135   122   169   [10
ply   Mar   140   129.8   104.04   ]
Apr   150   135.92 198.2464
,   564.0
May   160
136.25   625   144.368 244.3594
An
564.0   153.747
Jun   170
aly   146.25   625   2 264.1535
163.498
se,   Jul   180   155   625   9   272.287
Ev   173.399
165   6
alu
********** 10 **********
--- page 11 ---
at
e
Method   Forecast   MSE
4 moving   165   584.375
Expo sm alpha = 0.6   173.3996   182.4409
Exponential Smoothing with alpha = 0.6 is best as it has
minimum MSE
Final Forecast is 173.3996
b Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
,3;
BL-
The model selection is done on the basis of following parameters
Ap
1. Requirement of stationarity (in this case d = 0)
ply   2. BIC as low as possible   [10
3. All lags (except intercept) need to be significant
,   ]
4. Ljung-Box test should not be significant
An   5. Residual ACF & PACF should be within the lines
aly   Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
se,   In above case
Ev   Sr No Model   BIC   Description   Result
1   ARIMA(1,0,0   6.875   Correct : d=0, LB test not sig, lag1 sig   Model can
alu   )   & Residual ACF & PACF within range   be used
2   ARIMA(0,0,1   7.703   Correct : d=0, , lags sig. problem –   Model
at
)   Residual ACF & PACF not within range, cannot be
e   LB test sig   used
3   ARIMA(2,0,0   7.012   Correct : d=0, LB test not sig, problem Model
)   – ACF & PACF not within range, lag2   cannot be
not sig   used
4   ARIMA(1,1,0   7.012   Correct : LB test not sig, Residual ACF   Model
)   & PACF not within range   cannot be
problem – d=1, lag not sig ACF &   used
PACF not within range
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) as it satisfies all criteria, it is simplest and has lowest
BIC. hence company should use following forecasts
Model   21   22   23   24   25
Price-Model_1   Forecast   3041.33   3038.10 3035.01 3032.05 3029.23
UCL   3085.28   3098.91 3107.90 3114.46 3119.46
LCL   2997.38   2977.29 2962.12 2949.65 2939.00
Forecast
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 8 · Answer key · paper 64843a372783

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2024/Sem_08/Final-Exam/MBATech_AI_7051/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Apr 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Semester VIII(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 29 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the significance of predictive analytics in gaining a competitive advantage in
. business.
Synoptic Answer:
Predictive analytics involves using historical data, statistical models, and machine learning
techniques to make predictions about future outcomes. It helps businesses make
proactive, data-driven decisions.
CO
-1;   Key Points:
Definition & Importance (1 mark) – Predictive analytics anticipates future trends based
BL-
Un   on historical patterns.   [5]
de   Key Techniques (1 mark) – Regression analysis, decision trees, neural networks, and time
rst
an   series forecasting.
d   Applications in Business (1 mark) – Demand forecasting, customer behavior analysis, risk
assessment.
Competitive Advantage (1 mark) – Helps in optimizing pricing, improving customer
retention, and enhancing operational efficiency.
Example (1 mark) – Retailers use predictive analytics to forecast inventory demand and
reduce stockouts.
********** 1 **********
--- page 2 ---
b What are the common methods to deal with missing data during data preprocessing?
.   Synoptic Answer:
Missing data can distort analysis, leading to biased results. Proper handling is crucial for
CO   reliable models.
-1;   Key Points:
BL-   1. Understanding Missing Data (1 mark) – Types: MCAR (Missing Completely at
Un   Random), MAR (Missing at Random), MNAR (Missing Not at Random).
de   2. Deletion Methods (1 mark) – Listwise deletion (removing entire rows), Pairwise   [5]
rst   deletion (removing only missing values).
an   3. Imputation Techniques (1 mark) – Mean, median, mode imputation; Regression-
d,   based imputation.
ap   4. Advanced Techniques (1 mark) – Multiple Imputation, KNN imputation,
ply   Predictive modeling.
5. Example (1 mark) – In customer survey data, missing age values can be imputed
using the median age of respondents.
c Discuss the assumptions of regression models, focusing on heteroscedasticity and
.   multicollinearity.
CO   Synoptic Answer:
-   Regression models are based on specific assumptions, and violations affect accuracy and
1,2   reliability.
;   Key Points:
BL-   1. Overview of Regression Assumptions (1 mark) – Linearity, Independence,
Un   Homoscedasticity, Normality, No multicollinearity.   [5]
de   2. Heteroscedasticity (1 mark) – Variance of residuals is unequal across
rst   observations, leading to inefficient estimates.
an   3. Detection (1 mark) – Breusch-Pagan test, White test, residual plots.
d,   4. Remedies (1 mark) – Log transformation, Weighted Least Squares (WLS), robust
ap   standard errors.
ply   5. Multicollinearity (1 mark) – High correlation among independent variables; detected
using VIF (>10 indicates concern).
d Compare K-Nearest Neighbors (KNN) classification with logistic regression.
CO
-   .   Synoptic Answer:
Both methods classify data points but differ in their approach and applicability.
2,3
Key Points:
;
1. Definition & Overview (1 mark) – KNN is a non-parametric, instance-based
BL-
learning algorithm; Logistic Regression is a statistical method for binary   [5]
Un
classification.
de
2. Mechanism (1 mark) – KNN classifies based on nearest neighbors; Logistic
rst
Regression estimates probability using the sigmoid function.
an
3. Advantages (1 mark) – KNN is simple and handles non-linearity; Logistic
d,
Regression is interpretable and computationally efficient.
ap
4. Limitations (1 mark) – KNN is computationally expensive for large datasets;
ply
Logistic Regression assumes linearity.
********** 2 **********
--- page 3 ---
5. Example (1 mark) – In customer churn prediction, Logistic Regression identifies
key drivers, while KNN finds patterns in similar customers.
Marking Scheme:
1.   Which model was applied, and why? .....01 mark
The Multiple Linear Regression (MLR) model was applied because the company wants to
predict Sales Revenue based on multiple independent variables:
•   Advertising Spend
•   Social Media Reach
•   Product Reviews
• Campaign Type (categorical variable)
MLR is appropriate as it examines the relationship between multiple predictors and a
continuous dependent variable.
2.   Identify the baseline for qualitative predictor. .....01 mark
• The qualitative predictor is Campaign Type (Online = 1, Others = 0).
• The baseline category is Others (TV and Print Ads, coded as 0).
Q2
3.   State the model equation. .....01 marks
CO   Sales Revenue=
-   -9.629+2.702(Advertising Spend)+0.809(Social Media Reach)+1.484(Product Reviews)-
2.718
1,2
,3;   4.   Interpret the coefficient of the independent variable Campaign_Online…..02marks
BL-
Ap   It can be interpreted that Sales revenue will be lowered by -2.718 units when the   [20
ply   campaign is Online than when it would be offline (others).
,   ]
An
aly   1. Explain why the constant coefficient (b₀) has no practical meaning in this context. .....01
se,   marks
Ev
alu   b0 is the predicted Sales Revenue when all predictors are zero (i.e., no advertising spend, no
social media reach, zero product reviews, and only traditional campaigns).
at
e   This scenario is unrealistic, making b0 meaningless in practical business decisions.
2. Can the equation be used for prediction? Explain. .....01 marks
Since, Campaign_Online is an insignificant predictor (p=.541) of Sales Revenue; the model
cannot be used for prediction purposes.
3. Determine the coefficient of multiple determination (R²) and interpret its significance. .....02
marks
R² = 0.963, meaning 96.3% of the variation in sales revenue is explained by the independent
variables.
This is a strong R² value, suggesting the model is effective in predicting sales revenue.
********** 3 **********
--- page 4 ---
4. Identify which variable has the highest impact on sales revenue and which has the least
impact. .....02 marks
The highest impact variable: Social Media Reach
The least impact variable: Campaign Type
9.   What does the VIF (Variance Inflation Factor) indicate? .....01 marks
The VIF values are:
•   Advertising Spend: 1.006
•   Social Media Reach: 1.038
•   Product Reviews: 1.071
• Campaign Type: 1.056
Since all VIF values are below 5, there is no significant multicollinearity, meaning the
predictors are independent and do not distort the model.
10.   Interpret the PP plot. .....01 marks
The PP plot follows a nearly straight line, indicating that residuals are normally
distributed.
Small deviations exist, but they are within acceptable limits, so the normality assumption
holds.
11.   Analyze the normality of residuals using a histogram. .....01 marks
• The histogram of residuals is approximately bell-shaped, supporting the assumption of
normality.
• No extreme skewness or outliers were detected, confirming that the model errors are well-
distributed.
12.   Interpret the residual plot and analyze the residuals: Do they show any patterns indicating
model bias or need for improvement? .....01 marks
• The residual plot shows random scatter, meaning there are no clear patterns or trends.
• No heteroscedasticity (funnel-shaped pattern) was detected, meaning variance is constant.
•   This suggests no major model bias and that the assumptions of regression hold.
13.   Examine the ANOVA table: What does the significance (p-value) tell us about the overall
model fit? .....01 marks
F-statistic p-value (which is < 0.05), meaning the model is statistically significant.
14.   Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals? .....01 marks
Durbin-Watson (DW) = 2.388, which is close to 2, meaning no significant autocorrelation
in residuals.
15.   Predict the sales revenue when:
•   Advertising Spend: $11,000
•   Social Media Reach: 130,000 users
•   Product Reviews: 9.1 (average rating)
•   Campaign Type: Online .....03 marks
Given:
•   Advertising Spend = $11,000
•   Social Media Reach = 130,000 users
•   Product Reviews = 9.1
• Campaign Type = Online (1)
Using the model equation:
Sales Revenue: 136.0494
********** 4 **********
--- page 5 ---
Answers
Synoptic
a) this is three factor solution.
Rotated Component Matrixa
Component
1   2   3
Rate Baskin Robbins on
0.298   0.199   0.804
taste
Rate Baskin Robbins on
0.025   0.186   0.919
number of flavours
Rate Baskin Robbins on
0.055   0.748   0.297
Indian flavours
Rate Baskin Robbins on
0.406   0.577   0.182
packaging
Rate Baskin Robbins on
0.15   0.853   0.102
availability
Rate Baskin Robbins on
0.667   0.478   0.044
promotional offers
Rate Baskin Robbins on
Q3   Service   0.646   0.212   0.479
Rate Baskin Robbins on
CO   Advertising   0.868   -0.001   0.06
-   Rate Baskin Robbins on
0.529   0.349   0.356
1,2   value for money
,3;   Extraction Method: Principal Component Analysis.
BL-   Rotation Method: Varimax with Kaiser Normalization.
Ap   [20
Note to evaluators : Factor names are subjective student may name them
ply   in multiple ways   ]
Ev   Factor 2 (Local
alu   Factor 1 (Service   flavours   Factor 3 (Taste
at   Advertising & Price)   Availability)   Choices)
e,   Rate Baskin Robbins on   Rate Baskin   Rate Baskin
Robbins on
cre   Service   Indian flavours   Robbins on taste
at   Rate Baskin   Rate Baskin
Rate Baskin Robbins on
e   Advertising   Robbins on   Robbins on
availability   number of flavours
Rate Baskin Robbins on
value for money
b) Variables “Rate Baskin Robbins on packaging” & “ Rate Baskin Robbins on promotional
offers” have cross loadings hence need to be removed.
c) Scree plot indicates 3 factor as good solution
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5, total
explained variance > 60% indicates a good solution, however above mentioned two
variables have cross loadings, hence the solution needs to be revised by removing these
two variables.
Factor 1 (Service Advertising & Price) is most important factor as it has highest eigen value.
e) Selecting the right number of factors is crucial in factor analysis. Here are the
commonly used methods:
1. Eigenvalues (Kaiser’s Criterion)
• Retain factors with eigenvalues > 1 (i.e., explaining more variance than a single
variable).
********** 5 **********
--- page 6 ---
• Helps in determining significant factors based on variance contribution.
• Works well when the number of variables is less than 30.
2. Scree Plot (Elbow Method)
• A graphical representation of eigenvalues.
• The plot shows a sharp decline (elbow point), after which the curve flattens.
•   Factors before the elbow are retained.
3. Variance Explained Criterion
• Choose the number of factors that together explain at least 60%-70% of the total
variance.
• The cumulative variance contribution is checked for interpretability.
5. Factor Loadings & Interpretability
• Examine factor loadings after extraction.
• The chosen number of factors should make theoretical sense and be interpretable.
a
Answer:
5NN
Standar Standar   Standar   Standar
Q4
dised   dised   dised   dised   Standardis
CO   Distanc   Distance Distance Distance ed Distance
e of 1st   of 2nd   of 3rd   of 4th   of 5th
-   Visit
Supermarke   observa observat observat observat   observation
1,2   t   tion   ion   ion   ion
N   4   6   5   6   7
,3;
N   2   2   3   7   4
BL-   N   7   3   7   4   3
N   5   7   1   3   6
Ap
N   6   5   4   2   5
ply   Y   1   4   2   5   1   [10
,   Y   3   1   6   1   2   ]
An   Rank
aly   1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
se,   3 Y   N   Y   N   N
Ev   4 N   Y   N   N   Y
5 N   N   N   Y   N
alu
Prediction Y   Y   N   N   Y
at   Actual Y   N   N   N   Y
e
Predicti
on   Actual
Y   Y
Y   N
********** 6 **********
--- page 7 ---
N   N
N   N
Y   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   2   2
Grand Total   2   3   5
Accuracy   80.00%
100.00
Recall / Sensitivity   %
Specificity   66.67%
Precision   66.67%
3NN
Rank
1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
3 Y   N   Y   N   N
Prediction Y   Y   Y   N   Y
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Row Labels   N   Y   Grand Total
Actual   N   1   2   3
Y   2   2
Grand Total   1   4   5
Accuracy   60.00%
100.00
Recall / Sensitivity   %
Specificity   33.33%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
Q4 b Answers
i)   Discriminant Function = -3.754 + .057 * Age (years) + .052 * Salary ($1000s) + 0.108 *
CO   Years at Company + .651 * Job Type -.025 * Months since Last Raise   [10
ii)   Wilks lambda signifies discriminating power for the model. Lower the value(close to
-   ]
0), better discrimination. Higher the value (close to 1 ) less discriminating power of
1,2   the model. In this case wilk’s lambda is .848 => close to 1 hence the model has poor
discriminating power.
********** 7 **********
--- page 8 ---
,3;   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of variables.
BL-   And lowest absolute values ( modulus since it is correlations) indicate lowest
Ap   explanatory power of variables. In this case, Age has highest (.539) and Job
Type(.238) has lowest explanatory power.
ply   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
,
Here the Box’s M is not significant (p value =.892 > 0.05) this suggests there is no
An   enough evidence to conclude that covariance matrices are significantly different
across two groups. So assumption of equal covariance matrices holds good
aly   v)   Cross-validated accuracy is 64.3%. this data has equal number of successes and
failures. The chance accuracy for the data is   p(S)2 + p(F)2 = 0.25+.25 = 0.5
se,   We need atleast 25% improvement over chance accuracy i.e. 0.5 * 1.25 = 62.5% the overall cross
Ev   validated accuracy is better than minimum required accuracy hence, Ideally the model could be
used for prediction, but since the power of model is too low and there are some non-significant
alu   variables in the model like Job type (sig value .084 > 0.05 indicating this variable does not add
value in the model) you can avoid using the model. You may use stepwise DA.
at
e
a
Marking Scheme:
1. Which multivariate technique is applied in this scenario, and why is it suitable? (1 Mark)
•   Multivariate Technique Applied: Logistic Regression Why?
Q5   • The dependent variable (Loan Approval: Approved=1, Rejected = 0) is binary
(categorical).
CO   •   Logistic regression models the probability of approval using predictor variables.
2. Write the function used in the model. (1 Mark)
-
The logistic regression model function is:
1,2   e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
p ( x ) = 1 + e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
,3;
3. Interpret the pseudo R-square values and their significance. (1 Mark)
BL-   • The model explains 4.7% to 26.2% of the variance in loan approval decisions.
4. Which test statistic(s) are used to evaluate the accuracy of the model? (2 Marks)
Ap   • Wald Test: p <0.05): significant model
ply   • Hosmer-Lemeshow Test (p > 0.05): significant model   [15
,   5. Analyze the classification table and explain its implications. (2 Marks)   ]
False Negatives (Type II Error):
An   • The model predicted all loans as "approved" (1) since no "0" (denials) were predicted.
aly   •   There were 2 cases where loans were actually denied (0), but the model misclassified
them as approved (1). This leads to a 0% accuracy for denied loans.
se,   True Positives:
• The model correctly classified 98 approved loans (1) as approved.
Ev
• Accuracy for approved loans is 100%.
alu   Overall Accuracy:
• 98 out of 100 cases were classified correctly, leading to an overall accuracy of 98%.
at
e   6. Define and interpret the Sensitivity and Specificity of this model. (2 Marks)
•   Sensitivity (Recall) = TP / (TP + FN)
Measures the model’s ability to correctly identify actual positives (approved loans).
•   Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify actual negatives (denied loans).
•   Sensitivity = 100%: The model perfectly identifies approved loans.
********** 8 **********
--- page 9 ---
•   Specificity = 0%: The model completely fails to identify denied loans, predicting
all as approved.
7. Interpret the coefficients of the model. (3 Marks)
Odds Ratio (Exp(B)):
• Age → A 1-year increase in Age increases odds of approval by 0.024.
• Income → A $1,000 increase in income raises odds by 0.098
•   Credit Score → A 10-point increase in Credit Score raises odds by 0.005
Loan Type (b4=1.5) → Home Loan applicants are 0.389 times more likely to be approved.
Q5 b
Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as an
CO
outlier.
-;
Here, 4/(n-k-1) = 4/ (30-3-1) = 0.154
SO   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.154)   [5]
-;
BL-
a Explain the research design for cluster analysis and differentiate between hierarchical
. and non-hierarchical clustering techniques.
Q6   Synoptic Answer:
Cluster analysis groups similar data points together based on predefined criteria.
CO   Key Points:
-
1. Definition of Cluster Analysis (1 mark) – A technique used for segmenting data
1,2   into meaningful groups.
2. Research Design (1 mark) – Identify objectives, select clustering method, choose   [5]
,3;
distance metric, validate results.
BL-   3. Hierarchical Clustering (1 mark) – Builds a nested hierarchy using agglomerative
or divisive approaches.
Ap
4. Non-Hierarchical Clustering (1 mark) – Assigns data into pre-specified clusters
ply   (e.g., K-means).
5. Comparison (1 mark) – Hierarchical is useful for small datasets; K-means is
efficient for large datasets.
Q6 b
Solution:
CO   a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
-   Students may answer the other parts as per their choice of solution, i.e. 2 or 3.
2,3   b. Student may write the case numbers as per his choice of 2 or 3 cluster solution.
;   c. ANOVA is significant for all variables (for 2 cluster solution) indicating that all
variables are contributing in the cluster analysis. This also validates the cluster
results.   [15
BL-
*Students may write for 3 cluster solution as well.
]
Un   d. What are characteristics of each group? (For 3 cluster solution)
de
Cluste   LuxaryIt   Tech   CustomerSer
rst   r   N   Online_Sho   Discount   BrandLo   ImpulseBu   EcoFrie   ems   Savv   vice
pping   s   yalty   ying   ndly   y
an   1   1   5.67   5.47   4.87   7.07   3.07   5.53   7.8   7.60
5   0
d
********** 9 **********
--- page 10 ---
2   1   7.20   7.80   8.10   5.60   6.20   3.50   4.9   4.20
0   0
Total   2   6.28   6.40   6.16   6.48   4.32   4.72   6.6   6.24
5   4
Cluster 1: Low on BrandLoyalty, EcoFriendly , Moderate on Online_Shopping, Discounts
and LuxaryItems and High on ImpulseBuying, TechSavvy and CustomerService
Cluster 2: Low/ Moderate on ImpulseBuying, LuxaryItems, TechSavvy and
CustomerService but High on Online_Shopping, Discounts, BrandLoyalty and
EcoFriendly.
*Students may write for 3 cluster solution as well.
e. Cluster 1 is likely to be more profitable because:
1. High Impulse Buying: Customers frequently make unplanned purchases, leading
to higher revenue.
2. Tech-Savvy: More likely to engage with digital promotions, e-commerce
platforms, and AI-driven recommendations, increasing sales.
3. Strong Preference for Customer Service: Willing to pay a premium for better
support and experiences, leading to higher margins.
While Cluster 2 values discounts and brand loyalty, they may focus more on price
sensitivity and long-term relationships rather than impulsive, high-margin purchases.
*Students may write for 3 cluster solution as well.
a
Q7
Answer
CO
0.6
-
Sales
1,2   Mont   Reve
nue
,3;   h   ($100
0s)   4 moving avg   Exp sm
BL-
Jan   120   125   25
Ap   Feb   135   122   169   [10
ply   Mar   140   129.8   104.04   ]
Apr   150   135.92 198.2464
,   564.0
May   160
136.25   625   144.368 244.3594
An
564.0   153.747
Jun   170
aly   146.25   625   2 264.1535
163.498
se,   Jul   180   155   625   9   272.287
Ev   173.399
165   6
alu
********** 10 **********
--- page 11 ---
at
e
Method   Forecast   MSE
4 moving   165   584.375
Expo sm alpha = 0.6   173.3996   182.4409
Exponential Smoothing with alpha = 0.6 is best as it has
minimum MSE
Final Forecast is 173.3996
b Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
,3;
BL-
The model selection is done on the basis of following parameters
Ap
1. Requirement of stationarity (in this case d = 0)
ply   2. BIC as low as possible   [10
3. All lags (except intercept) need to be significant
,   ]
4. Ljung-Box test should not be significant
An   5. Residual ACF & PACF should be within the lines
aly   Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
se,   In above case
Ev   Sr No Model   BIC   Description   Result
1   ARIMA(1,0,0   6.875   Correct : d=0, LB test not sig, lag1 sig   Model can
alu   )   & Residual ACF & PACF within range   be used
2   ARIMA(0,0,1   7.703   Correct : d=0, , lags sig. problem –   Model
at
)   Residual ACF & PACF not within range, cannot be
e   LB test sig   used
3   ARIMA(2,0,0   7.012   Correct : d=0, LB test not sig, problem Model
)   – ACF & PACF not within range, lag2   cannot be
not sig   used
4   ARIMA(1,1,0   7.012   Correct : LB test not sig, Residual ACF   Model
)   & PACF not within range   cannot be
problem – d=1, lag not sig ACF &   used
PACF not within range
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) as it satisfies all criteria, it is simplest and has lowest
BIC. hence company should use following forecasts
Model   21   22   23   24   25
Price-Model_1   Forecast   3041.33   3038.10 3035.01 3032.05 3029.23
UCL   3085.28   3098.91 3107.90 3114.46 3119.46
LCL   2997.38   2977.29 2962.12 2949.65 2939.00
Forecast
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 8 · Answer key · paper 447ff31e6ac3

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2024/Sem_08/Final-Exam/MBATech_Computer_7047/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Apr 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Semester VIII(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 29 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the significance of predictive analytics in gaining a competitive advantage in
. business.
Synoptic Answer:
Predictive analytics involves using historical data, statistical models, and machine learning
techniques to make predictions about future outcomes. It helps businesses make
proactive, data-driven decisions.
CO
-1;   Key Points:
Definition & Importance (1 mark) – Predictive analytics anticipates future trends based
BL-
Un   on historical patterns.   [5]
de   Key Techniques (1 mark) – Regression analysis, decision trees, neural networks, and time
rst
an   series forecasting.
d   Applications in Business (1 mark) – Demand forecasting, customer behavior analysis, risk
assessment.
Competitive Advantage (1 mark) – Helps in optimizing pricing, improving customer
retention, and enhancing operational efficiency.
Example (1 mark) – Retailers use predictive analytics to forecast inventory demand and
reduce stockouts.
********** 1 **********
--- page 2 ---
b What are the common methods to deal with missing data during data preprocessing?
.   Synoptic Answer:
Missing data can distort analysis, leading to biased results. Proper handling is crucial for
CO   reliable models.
-1;   Key Points:
BL-   1. Understanding Missing Data (1 mark) – Types: MCAR (Missing Completely at
Un   Random), MAR (Missing at Random), MNAR (Missing Not at Random).
de   2. Deletion Methods (1 mark) – Listwise deletion (removing entire rows), Pairwise   [5]
rst   deletion (removing only missing values).
an   3. Imputation Techniques (1 mark) – Mean, median, mode imputation; Regression-
d,   based imputation.
ap   4. Advanced Techniques (1 mark) – Multiple Imputation, KNN imputation,
ply   Predictive modeling.
5. Example (1 mark) – In customer survey data, missing age values can be imputed
using the median age of respondents.
c Discuss the assumptions of regression models, focusing on heteroscedasticity and
.   multicollinearity.
CO   Synoptic Answer:
-   Regression models are based on specific assumptions, and violations affect accuracy and
1,2   reliability.
;   Key Points:
BL-   1. Overview of Regression Assumptions (1 mark) – Linearity, Independence,
Un   Homoscedasticity, Normality, No multicollinearity.   [5]
de   2. Heteroscedasticity (1 mark) – Variance of residuals is unequal across
rst   observations, leading to inefficient estimates.
an   3. Detection (1 mark) – Breusch-Pagan test, White test, residual plots.
d,   4. Remedies (1 mark) – Log transformation, Weighted Least Squares (WLS), robust
ap   standard errors.
ply   5. Multicollinearity (1 mark) – High correlation among independent variables; detected
using VIF (>10 indicates concern).
d Compare K-Nearest Neighbors (KNN) classification with logistic regression.
CO
-   .   Synoptic Answer:
Both methods classify data points but differ in their approach and applicability.
2,3
Key Points:
;
1. Definition & Overview (1 mark) – KNN is a non-parametric, instance-based
BL-
learning algorithm; Logistic Regression is a statistical method for binary   [5]
Un
classification.
de
2. Mechanism (1 mark) – KNN classifies based on nearest neighbors; Logistic
rst
Regression estimates probability using the sigmoid function.
an
3. Advantages (1 mark) – KNN is simple and handles non-linearity; Logistic
d,
Regression is interpretable and computationally efficient.
ap
4. Limitations (1 mark) – KNN is computationally expensive for large datasets;
ply
Logistic Regression assumes linearity.
********** 2 **********
--- page 3 ---
5. Example (1 mark) – In customer churn prediction, Logistic Regression identifies
key drivers, while KNN finds patterns in similar customers.
Marking Scheme:
1.   Which model was applied, and why? .....01 mark
The Multiple Linear Regression (MLR) model was applied because the company wants to
predict Sales Revenue based on multiple independent variables:
•   Advertising Spend
•   Social Media Reach
•   Product Reviews
• Campaign Type (categorical variable)
MLR is appropriate as it examines the relationship between multiple predictors and a
continuous dependent variable.
2.   Identify the baseline for qualitative predictor. .....01 mark
• The qualitative predictor is Campaign Type (Online = 1, Others = 0).
• The baseline category is Others (TV and Print Ads, coded as 0).
Q2
3.   State the model equation. .....01 marks
CO   Sales Revenue=
-   -9.629+2.702(Advertising Spend)+0.809(Social Media Reach)+1.484(Product Reviews)-
2.718
1,2
,3;   4.   Interpret the coefficient of the independent variable Campaign_Online…..02marks
BL-
Ap   It can be interpreted that Sales revenue will be lowered by -2.718 units when the   [20
ply   campaign is Online than when it would be offline (others).
,   ]
An
aly   1. Explain why the constant coefficient (b₀) has no practical meaning in this context. .....01
se,   marks
Ev
alu   b0 is the predicted Sales Revenue when all predictors are zero (i.e., no advertising spend, no
social media reach, zero product reviews, and only traditional campaigns).
at
e   This scenario is unrealistic, making b0 meaningless in practical business decisions.
2. Can the equation be used for prediction? Explain. .....01 marks
Since, Campaign_Online is an insignificant predictor (p=.541) of Sales Revenue; the model
cannot be used for prediction purposes.
3. Determine the coefficient of multiple determination (R²) and interpret its significance. .....02
marks
R² = 0.963, meaning 96.3% of the variation in sales revenue is explained by the independent
variables.
This is a strong R² value, suggesting the model is effective in predicting sales revenue.
********** 3 **********
--- page 4 ---
4. Identify which variable has the highest impact on sales revenue and which has the least
impact. .....02 marks
The highest impact variable: Social Media Reach
The least impact variable: Campaign Type
9.   What does the VIF (Variance Inflation Factor) indicate? .....01 marks
The VIF values are:
•   Advertising Spend: 1.006
•   Social Media Reach: 1.038
•   Product Reviews: 1.071
• Campaign Type: 1.056
Since all VIF values are below 5, there is no significant multicollinearity, meaning the
predictors are independent and do not distort the model.
10.   Interpret the PP plot. .....01 marks
The PP plot follows a nearly straight line, indicating that residuals are normally
distributed.
Small deviations exist, but they are within acceptable limits, so the normality assumption
holds.
11.   Analyze the normality of residuals using a histogram. .....01 marks
• The histogram of residuals is approximately bell-shaped, supporting the assumption of
normality.
• No extreme skewness or outliers were detected, confirming that the model errors are well-
distributed.
12.   Interpret the residual plot and analyze the residuals: Do they show any patterns indicating
model bias or need for improvement? .....01 marks
• The residual plot shows random scatter, meaning there are no clear patterns or trends.
• No heteroscedasticity (funnel-shaped pattern) was detected, meaning variance is constant.
•   This suggests no major model bias and that the assumptions of regression hold.
13.   Examine the ANOVA table: What does the significance (p-value) tell us about the overall
model fit? .....01 marks
F-statistic p-value (which is < 0.05), meaning the model is statistically significant.
14.   Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals? .....01 marks
Durbin-Watson (DW) = 2.388, which is close to 2, meaning no significant autocorrelation
in residuals.
15.   Predict the sales revenue when:
•   Advertising Spend: $11,000
•   Social Media Reach: 130,000 users
•   Product Reviews: 9.1 (average rating)
•   Campaign Type: Online .....03 marks
Given:
•   Advertising Spend = $11,000
•   Social Media Reach = 130,000 users
•   Product Reviews = 9.1
• Campaign Type = Online (1)
Using the model equation:
Sales Revenue: 136.0494
********** 4 **********
--- page 5 ---
Answers
Synoptic
a) this is three factor solution.
Rotated Component Matrixa
Component
1   2   3
Rate Baskin Robbins on
0.298   0.199   0.804
taste
Rate Baskin Robbins on
0.025   0.186   0.919
number of flavours
Rate Baskin Robbins on
0.055   0.748   0.297
Indian flavours
Rate Baskin Robbins on
0.406   0.577   0.182
packaging
Rate Baskin Robbins on
0.15   0.853   0.102
availability
Rate Baskin Robbins on
0.667   0.478   0.044
promotional offers
Rate Baskin Robbins on
Q3   Service   0.646   0.212   0.479
Rate Baskin Robbins on
CO   Advertising   0.868   -0.001   0.06
-   Rate Baskin Robbins on
0.529   0.349   0.356
1,2   value for money
,3;   Extraction Method: Principal Component Analysis.
BL-   Rotation Method: Varimax with Kaiser Normalization.
Ap   [20
Note to evaluators : Factor names are subjective student may name them
ply   in multiple ways   ]
Ev   Factor 2 (Local
alu   Factor 1 (Service   flavours   Factor 3 (Taste
at   Advertising & Price)   Availability)   Choices)
e,   Rate Baskin Robbins on   Rate Baskin   Rate Baskin
Robbins on
cre   Service   Indian flavours   Robbins on taste
at   Rate Baskin   Rate Baskin
Rate Baskin Robbins on
e   Advertising   Robbins on   Robbins on
availability   number of flavours
Rate Baskin Robbins on
value for money
b) Variables “Rate Baskin Robbins on packaging” & “ Rate Baskin Robbins on promotional
offers” have cross loadings hence need to be removed.
c) Scree plot indicates 3 factor as good solution
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5, total
explained variance > 60% indicates a good solution, however above mentioned two
variables have cross loadings, hence the solution needs to be revised by removing these
two variables.
Factor 1 (Service Advertising & Price) is most important factor as it has highest eigen value.
e) Selecting the right number of factors is crucial in factor analysis. Here are the
commonly used methods:
1. Eigenvalues (Kaiser’s Criterion)
• Retain factors with eigenvalues > 1 (i.e., explaining more variance than a single
variable).
********** 5 **********
--- page 6 ---
• Helps in determining significant factors based on variance contribution.
• Works well when the number of variables is less than 30.
2. Scree Plot (Elbow Method)
• A graphical representation of eigenvalues.
• The plot shows a sharp decline (elbow point), after which the curve flattens.
•   Factors before the elbow are retained.
3. Variance Explained Criterion
• Choose the number of factors that together explain at least 60%-70% of the total
variance.
• The cumulative variance contribution is checked for interpretability.
5. Factor Loadings & Interpretability
• Examine factor loadings after extraction.
• The chosen number of factors should make theoretical sense and be interpretable.
a
Answer:
5NN
Standar Standar   Standar   Standar
Q4
dised   dised   dised   dised   Standardis
CO   Distanc   Distance Distance Distance ed Distance
e of 1st   of 2nd   of 3rd   of 4th   of 5th
-   Visit
Supermarke   observa observat observat observat   observation
1,2   t   tion   ion   ion   ion
N   4   6   5   6   7
,3;
N   2   2   3   7   4
BL-   N   7   3   7   4   3
N   5   7   1   3   6
Ap
N   6   5   4   2   5
ply   Y   1   4   2   5   1   [10
,   Y   3   1   6   1   2   ]
An   Rank
aly   1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
se,   3 Y   N   Y   N   N
Ev   4 N   Y   N   N   Y
5 N   N   N   Y   N
alu
Prediction Y   Y   N   N   Y
at   Actual Y   N   N   N   Y
e
Predicti
on   Actual
Y   Y
Y   N
********** 6 **********
--- page 7 ---
N   N
N   N
Y   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   2   2
Grand Total   2   3   5
Accuracy   80.00%
100.00
Recall / Sensitivity   %
Specificity   66.67%
Precision   66.67%
3NN
Rank
1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
3 Y   N   Y   N   N
Prediction Y   Y   Y   N   Y
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Row Labels   N   Y   Grand Total
Actual   N   1   2   3
Y   2   2
Grand Total   1   4   5
Accuracy   60.00%
100.00
Recall / Sensitivity   %
Specificity   33.33%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
Q4 b Answers
i)   Discriminant Function = -3.754 + .057 * Age (years) + .052 * Salary ($1000s) + 0.108 *
CO   Years at Company + .651 * Job Type -.025 * Months since Last Raise   [10
ii)   Wilks lambda signifies discriminating power for the model. Lower the value(close to
-   ]
0), better discrimination. Higher the value (close to 1 ) less discriminating power of
1,2   the model. In this case wilk’s lambda is .848 => close to 1 hence the model has poor
discriminating power.
********** 7 **********
--- page 8 ---
,3;   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of variables.
BL-   And lowest absolute values ( modulus since it is correlations) indicate lowest
Ap   explanatory power of variables. In this case, Age has highest (.539) and Job
Type(.238) has lowest explanatory power.
ply   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
,
Here the Box’s M is not significant (p value =.892 > 0.05) this suggests there is no
An   enough evidence to conclude that covariance matrices are significantly different
across two groups. So assumption of equal covariance matrices holds good
aly   v)   Cross-validated accuracy is 64.3%. this data has equal number of successes and
failures. The chance accuracy for the data is   p(S)2 + p(F)2 = 0.25+.25 = 0.5
se,   We need atleast 25% improvement over chance accuracy i.e. 0.5 * 1.25 = 62.5% the overall cross
Ev   validated accuracy is better than minimum required accuracy hence, Ideally the model could be
used for prediction, but since the power of model is too low and there are some non-significant
alu   variables in the model like Job type (sig value .084 > 0.05 indicating this variable does not add
value in the model) you can avoid using the model. You may use stepwise DA.
at
e
a
Marking Scheme:
1. Which multivariate technique is applied in this scenario, and why is it suitable? (1 Mark)
•   Multivariate Technique Applied: Logistic Regression Why?
Q5   • The dependent variable (Loan Approval: Approved=1, Rejected = 0) is binary
(categorical).
CO   •   Logistic regression models the probability of approval using predictor variables.
2. Write the function used in the model. (1 Mark)
-
The logistic regression model function is:
1,2   e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
p ( x ) = 1 + e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
,3;
3. Interpret the pseudo R-square values and their significance. (1 Mark)
BL-   • The model explains 4.7% to 26.2% of the variance in loan approval decisions.
4. Which test statistic(s) are used to evaluate the accuracy of the model? (2 Marks)
Ap   • Wald Test: p <0.05): significant model
ply   • Hosmer-Lemeshow Test (p > 0.05): significant model   [15
,   5. Analyze the classification table and explain its implications. (2 Marks)   ]
False Negatives (Type II Error):
An   • The model predicted all loans as "approved" (1) since no "0" (denials) were predicted.
aly   •   There were 2 cases where loans were actually denied (0), but the model misclassified
them as approved (1). This leads to a 0% accuracy for denied loans.
se,   True Positives:
• The model correctly classified 98 approved loans (1) as approved.
Ev
• Accuracy for approved loans is 100%.
alu   Overall Accuracy:
• 98 out of 100 cases were classified correctly, leading to an overall accuracy of 98%.
at
e   6. Define and interpret the Sensitivity and Specificity of this model. (2 Marks)
•   Sensitivity (Recall) = TP / (TP + FN)
Measures the model’s ability to correctly identify actual positives (approved loans).
•   Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify actual negatives (denied loans).
•   Sensitivity = 100%: The model perfectly identifies approved loans.
********** 8 **********
--- page 9 ---
•   Specificity = 0%: The model completely fails to identify denied loans, predicting
all as approved.
7. Interpret the coefficients of the model. (3 Marks)
Odds Ratio (Exp(B)):
• Age → A 1-year increase in Age increases odds of approval by 0.024.
• Income → A $1,000 increase in income raises odds by 0.098
•   Credit Score → A 10-point increase in Credit Score raises odds by 0.005
Loan Type (b4=1.5) → Home Loan applicants are 0.389 times more likely to be approved.
Q5 b
Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as an
CO
outlier.
-;
Here, 4/(n-k-1) = 4/ (30-3-1) = 0.154
SO   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.154)   [5]
-;
BL-
a Explain the research design for cluster analysis and differentiate between hierarchical
. and non-hierarchical clustering techniques.
Q6   Synoptic Answer:
Cluster analysis groups similar data points together based on predefined criteria.
CO   Key Points:
-
1. Definition of Cluster Analysis (1 mark) – A technique used for segmenting data
1,2   into meaningful groups.
2. Research Design (1 mark) – Identify objectives, select clustering method, choose   [5]
,3;
distance metric, validate results.
BL-   3. Hierarchical Clustering (1 mark) – Builds a nested hierarchy using agglomerative
or divisive approaches.
Ap
4. Non-Hierarchical Clustering (1 mark) – Assigns data into pre-specified clusters
ply   (e.g., K-means).
5. Comparison (1 mark) – Hierarchical is useful for small datasets; K-means is
efficient for large datasets.
Q6 b
Solution:
CO   a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
-   Students may answer the other parts as per their choice of solution, i.e. 2 or 3.
2,3   b. Student may write the case numbers as per his choice of 2 or 3 cluster solution.
;   c. ANOVA is significant for all variables (for 2 cluster solution) indicating that all
variables are contributing in the cluster analysis. This also validates the cluster
results.   [15
BL-
*Students may write for 3 cluster solution as well.
]
Un   d. What are characteristics of each group? (For 3 cluster solution)
de
Cluste   LuxaryIt   Tech   CustomerSer
rst   r   N   Online_Sho   Discount   BrandLo   ImpulseBu   EcoFrie   ems   Savv   vice
pping   s   yalty   ying   ndly   y
an   1   1   5.67   5.47   4.87   7.07   3.07   5.53   7.8   7.60
5   0
d
********** 9 **********
--- page 10 ---
2   1   7.20   7.80   8.10   5.60   6.20   3.50   4.9   4.20
0   0
Total   2   6.28   6.40   6.16   6.48   4.32   4.72   6.6   6.24
5   4
Cluster 1: Low on BrandLoyalty, EcoFriendly , Moderate on Online_Shopping, Discounts
and LuxaryItems and High on ImpulseBuying, TechSavvy and CustomerService
Cluster 2: Low/ Moderate on ImpulseBuying, LuxaryItems, TechSavvy and
CustomerService but High on Online_Shopping, Discounts, BrandLoyalty and
EcoFriendly.
*Students may write for 3 cluster solution as well.
e. Cluster 1 is likely to be more profitable because:
1. High Impulse Buying: Customers frequently make unplanned purchases, leading
to higher revenue.
2. Tech-Savvy: More likely to engage with digital promotions, e-commerce
platforms, and AI-driven recommendations, increasing sales.
3. Strong Preference for Customer Service: Willing to pay a premium for better
support and experiences, leading to higher margins.
While Cluster 2 values discounts and brand loyalty, they may focus more on price
sensitivity and long-term relationships rather than impulsive, high-margin purchases.
*Students may write for 3 cluster solution as well.
a
Q7
Answer
CO
0.6
-
Sales
1,2   Mont   Reve
nue
,3;   h   ($100
0s)   4 moving avg   Exp sm
BL-
Jan   120   125   25
Ap   Feb   135   122   169   [10
ply   Mar   140   129.8   104.04   ]
Apr   150   135.92 198.2464
,   564.0
May   160
136.25   625   144.368 244.3594
An
564.0   153.747
Jun   170
aly   146.25   625   2 264.1535
163.498
se,   Jul   180   155   625   9   272.287
Ev   173.399
165   6
alu
********** 10 **********
--- page 11 ---
at
e
Method   Forecast   MSE
4 moving   165   584.375
Expo sm alpha = 0.6   173.3996   182.4409
Exponential Smoothing with alpha = 0.6 is best as it has
minimum MSE
Final Forecast is 173.3996
b Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
,3;
BL-
The model selection is done on the basis of following parameters
Ap
1. Requirement of stationarity (in this case d = 0)
ply   2. BIC as low as possible   [10
3. All lags (except intercept) need to be significant
,   ]
4. Ljung-Box test should not be significant
An   5. Residual ACF & PACF should be within the lines
aly   Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
se,   In above case
Ev   Sr No Model   BIC   Description   Result
1   ARIMA(1,0,0   6.875   Correct : d=0, LB test not sig, lag1 sig   Model can
alu   )   & Residual ACF & PACF within range   be used
2   ARIMA(0,0,1   7.703   Correct : d=0, , lags sig. problem –   Model
at
)   Residual ACF & PACF not within range, cannot be
e   LB test sig   used
3   ARIMA(2,0,0   7.012   Correct : d=0, LB test not sig, problem Model
)   – ACF & PACF not within range, lag2   cannot be
not sig   used
4   ARIMA(1,1,0   7.012   Correct : LB test not sig, Residual ACF   Model
)   & PACF not within range   cannot be
problem – d=1, lag not sig ACF &   used
PACF not within range
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) as it satisfies all criteria, it is simplest and has lowest
BIC. hence company should use following forecasts
Model   21   22   23   24   25
Price-Model_1   Forecast   3041.33   3038.10 3035.01 3032.05 3029.23
UCL   3085.28   3098.91 3107.90 3114.46 3119.46
LCL   2997.38   2977.29 2962.12 2949.65 2939.00
Forecast
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 8 · Answer key · paper 9b1476d6d0ea

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2024/Sem_08/Final-Exam/MBATech_DS_7052/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Apr 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Semester VIII(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 29 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the significance of predictive analytics in gaining a competitive advantage in
. business.
Synoptic Answer:
Predictive analytics involves using historical data, statistical models, and machine learning
techniques to make predictions about future outcomes. It helps businesses make
proactive, data-driven decisions.
CO
-1;   Key Points:
Definition & Importance (1 mark) – Predictive analytics anticipates future trends based
BL-
Un   on historical patterns.   [5]
de   Key Techniques (1 mark) – Regression analysis, decision trees, neural networks, and time
rst
an   series forecasting.
d   Applications in Business (1 mark) – Demand forecasting, customer behavior analysis, risk
assessment.
Competitive Advantage (1 mark) – Helps in optimizing pricing, improving customer
retention, and enhancing operational efficiency.
Example (1 mark) – Retailers use predictive analytics to forecast inventory demand and
reduce stockouts.
********** 1 **********
--- page 2 ---
b What are the common methods to deal with missing data during data preprocessing?
.   Synoptic Answer:
Missing data can distort analysis, leading to biased results. Proper handling is crucial for
CO   reliable models.
-1;   Key Points:
BL-   1. Understanding Missing Data (1 mark) – Types: MCAR (Missing Completely at
Un   Random), MAR (Missing at Random), MNAR (Missing Not at Random).
de   2. Deletion Methods (1 mark) – Listwise deletion (removing entire rows), Pairwise   [5]
rst   deletion (removing only missing values).
an   3. Imputation Techniques (1 mark) – Mean, median, mode imputation; Regression-
d,   based imputation.
ap   4. Advanced Techniques (1 mark) – Multiple Imputation, KNN imputation,
ply   Predictive modeling.
5. Example (1 mark) – In customer survey data, missing age values can be imputed
using the median age of respondents.
c Discuss the assumptions of regression models, focusing on heteroscedasticity and
.   multicollinearity.
CO   Synoptic Answer:
-   Regression models are based on specific assumptions, and violations affect accuracy and
1,2   reliability.
;   Key Points:
BL-   1. Overview of Regression Assumptions (1 mark) – Linearity, Independence,
Un   Homoscedasticity, Normality, No multicollinearity.   [5]
de   2. Heteroscedasticity (1 mark) – Variance of residuals is unequal across
rst   observations, leading to inefficient estimates.
an   3. Detection (1 mark) – Breusch-Pagan test, White test, residual plots.
d,   4. Remedies (1 mark) – Log transformation, Weighted Least Squares (WLS), robust
ap   standard errors.
ply   5. Multicollinearity (1 mark) – High correlation among independent variables; detected
using VIF (>10 indicates concern).
d Compare K-Nearest Neighbors (KNN) classification with logistic regression.
CO
-   .   Synoptic Answer:
Both methods classify data points but differ in their approach and applicability.
2,3
Key Points:
;
1. Definition & Overview (1 mark) – KNN is a non-parametric, instance-based
BL-
learning algorithm; Logistic Regression is a statistical method for binary   [5]
Un
classification.
de
2. Mechanism (1 mark) – KNN classifies based on nearest neighbors; Logistic
rst
Regression estimates probability using the sigmoid function.
an
3. Advantages (1 mark) – KNN is simple and handles non-linearity; Logistic
d,
Regression is interpretable and computationally efficient.
ap
4. Limitations (1 mark) – KNN is computationally expensive for large datasets;
ply
Logistic Regression assumes linearity.
********** 2 **********
--- page 3 ---
5. Example (1 mark) – In customer churn prediction, Logistic Regression identifies
key drivers, while KNN finds patterns in similar customers.
Marking Scheme:
1.   Which model was applied, and why? .....01 mark
The Multiple Linear Regression (MLR) model was applied because the company wants to
predict Sales Revenue based on multiple independent variables:
•   Advertising Spend
•   Social Media Reach
•   Product Reviews
• Campaign Type (categorical variable)
MLR is appropriate as it examines the relationship between multiple predictors and a
continuous dependent variable.
2.   Identify the baseline for qualitative predictor. .....01 mark
• The qualitative predictor is Campaign Type (Online = 1, Others = 0).
• The baseline category is Others (TV and Print Ads, coded as 0).
Q2
3.   State the model equation. .....01 marks
CO   Sales Revenue=
-   -9.629+2.702(Advertising Spend)+0.809(Social Media Reach)+1.484(Product Reviews)-
2.718
1,2
,3;   4.   Interpret the coefficient of the independent variable Campaign_Online…..02marks
BL-
Ap   It can be interpreted that Sales revenue will be lowered by -2.718 units when the   [20
ply   campaign is Online than when it would be offline (others).
,   ]
An
aly   1. Explain why the constant coefficient (b₀) has no practical meaning in this context. .....01
se,   marks
Ev
alu   b0 is the predicted Sales Revenue when all predictors are zero (i.e., no advertising spend, no
social media reach, zero product reviews, and only traditional campaigns).
at
e   This scenario is unrealistic, making b0 meaningless in practical business decisions.
2. Can the equation be used for prediction? Explain. .....01 marks
Since, Campaign_Online is an insignificant predictor (p=.541) of Sales Revenue; the model
cannot be used for prediction purposes.
3. Determine the coefficient of multiple determination (R²) and interpret its significance. .....02
marks
R² = 0.963, meaning 96.3% of the variation in sales revenue is explained by the independent
variables.
This is a strong R² value, suggesting the model is effective in predicting sales revenue.
********** 3 **********
--- page 4 ---
4. Identify which variable has the highest impact on sales revenue and which has the least
impact. .....02 marks
The highest impact variable: Social Media Reach
The least impact variable: Campaign Type
9.   What does the VIF (Variance Inflation Factor) indicate? .....01 marks
The VIF values are:
•   Advertising Spend: 1.006
•   Social Media Reach: 1.038
•   Product Reviews: 1.071
• Campaign Type: 1.056
Since all VIF values are below 5, there is no significant multicollinearity, meaning the
predictors are independent and do not distort the model.
10.   Interpret the PP plot. .....01 marks
The PP plot follows a nearly straight line, indicating that residuals are normally
distributed.
Small deviations exist, but they are within acceptable limits, so the normality assumption
holds.
11.   Analyze the normality of residuals using a histogram. .....01 marks
• The histogram of residuals is approximately bell-shaped, supporting the assumption of
normality.
• No extreme skewness or outliers were detected, confirming that the model errors are well-
distributed.
12.   Interpret the residual plot and analyze the residuals: Do they show any patterns indicating
model bias or need for improvement? .....01 marks
• The residual plot shows random scatter, meaning there are no clear patterns or trends.
• No heteroscedasticity (funnel-shaped pattern) was detected, meaning variance is constant.
•   This suggests no major model bias and that the assumptions of regression hold.
13.   Examine the ANOVA table: What does the significance (p-value) tell us about the overall
model fit? .....01 marks
F-statistic p-value (which is < 0.05), meaning the model is statistically significant.
14.   Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals? .....01 marks
Durbin-Watson (DW) = 2.388, which is close to 2, meaning no significant autocorrelation
in residuals.
15.   Predict the sales revenue when:
•   Advertising Spend: $11,000
•   Social Media Reach: 130,000 users
•   Product Reviews: 9.1 (average rating)
•   Campaign Type: Online .....03 marks
Given:
•   Advertising Spend = $11,000
•   Social Media Reach = 130,000 users
•   Product Reviews = 9.1
• Campaign Type = Online (1)
Using the model equation:
Sales Revenue: 136.0494
********** 4 **********
--- page 5 ---
Answers
Synoptic
a) this is three factor solution.
Rotated Component Matrixa
Component
1   2   3
Rate Baskin Robbins on
0.298   0.199   0.804
taste
Rate Baskin Robbins on
0.025   0.186   0.919
number of flavours
Rate Baskin Robbins on
0.055   0.748   0.297
Indian flavours
Rate Baskin Robbins on
0.406   0.577   0.182
packaging
Rate Baskin Robbins on
0.15   0.853   0.102
availability
Rate Baskin Robbins on
0.667   0.478   0.044
promotional offers
Rate Baskin Robbins on
Q3   Service   0.646   0.212   0.479
Rate Baskin Robbins on
CO   Advertising   0.868   -0.001   0.06
-   Rate Baskin Robbins on
0.529   0.349   0.356
1,2   value for money
,3;   Extraction Method: Principal Component Analysis.
BL-   Rotation Method: Varimax with Kaiser Normalization.
Ap   [20
Note to evaluators : Factor names are subjective student may name them
ply   in multiple ways   ]
Ev   Factor 2 (Local
alu   Factor 1 (Service   flavours   Factor 3 (Taste
at   Advertising & Price)   Availability)   Choices)
e,   Rate Baskin Robbins on   Rate Baskin   Rate Baskin
Robbins on
cre   Service   Indian flavours   Robbins on taste
at   Rate Baskin   Rate Baskin
Rate Baskin Robbins on
e   Advertising   Robbins on   Robbins on
availability   number of flavours
Rate Baskin Robbins on
value for money
b) Variables “Rate Baskin Robbins on packaging” & “ Rate Baskin Robbins on promotional
offers” have cross loadings hence need to be removed.
c) Scree plot indicates 3 factor as good solution
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5, total
explained variance > 60% indicates a good solution, however above mentioned two
variables have cross loadings, hence the solution needs to be revised by removing these
two variables.
Factor 1 (Service Advertising & Price) is most important factor as it has highest eigen value.
e) Selecting the right number of factors is crucial in factor analysis. Here are the
commonly used methods:
1. Eigenvalues (Kaiser’s Criterion)
• Retain factors with eigenvalues > 1 (i.e., explaining more variance than a single
variable).
********** 5 **********
--- page 6 ---
• Helps in determining significant factors based on variance contribution.
• Works well when the number of variables is less than 30.
2. Scree Plot (Elbow Method)
• A graphical representation of eigenvalues.
• The plot shows a sharp decline (elbow point), after which the curve flattens.
•   Factors before the elbow are retained.
3. Variance Explained Criterion
• Choose the number of factors that together explain at least 60%-70% of the total
variance.
• The cumulative variance contribution is checked for interpretability.
5. Factor Loadings & Interpretability
• Examine factor loadings after extraction.
• The chosen number of factors should make theoretical sense and be interpretable.
a
Answer:
5NN
Standar Standar   Standar   Standar
Q4
dised   dised   dised   dised   Standardis
CO   Distanc   Distance Distance Distance ed Distance
e of 1st   of 2nd   of 3rd   of 4th   of 5th
-   Visit
Supermarke   observa observat observat observat   observation
1,2   t   tion   ion   ion   ion
N   4   6   5   6   7
,3;
N   2   2   3   7   4
BL-   N   7   3   7   4   3
N   5   7   1   3   6
Ap
N   6   5   4   2   5
ply   Y   1   4   2   5   1   [10
,   Y   3   1   6   1   2   ]
An   Rank
aly   1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
se,   3 Y   N   Y   N   N
Ev   4 N   Y   N   N   Y
5 N   N   N   Y   N
alu
Prediction Y   Y   N   N   Y
at   Actual Y   N   N   N   Y
e
Predicti
on   Actual
Y   Y
Y   N
********** 6 **********
--- page 7 ---
N   N
N   N
Y   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   2   2
Grand Total   2   3   5
Accuracy   80.00%
100.00
Recall / Sensitivity   %
Specificity   66.67%
Precision   66.67%
3NN
Rank
1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
3 Y   N   Y   N   N
Prediction Y   Y   Y   N   Y
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Row Labels   N   Y   Grand Total
Actual   N   1   2   3
Y   2   2
Grand Total   1   4   5
Accuracy   60.00%
100.00
Recall / Sensitivity   %
Specificity   33.33%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
Q4 b Answers
i)   Discriminant Function = -3.754 + .057 * Age (years) + .052 * Salary ($1000s) + 0.108 *
CO   Years at Company + .651 * Job Type -.025 * Months since Last Raise   [10
ii)   Wilks lambda signifies discriminating power for the model. Lower the value(close to
-   ]
0), better discrimination. Higher the value (close to 1 ) less discriminating power of
1,2   the model. In this case wilk’s lambda is .848 => close to 1 hence the model has poor
discriminating power.
********** 7 **********
--- page 8 ---
,3;   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of variables.
BL-   And lowest absolute values ( modulus since it is correlations) indicate lowest
Ap   explanatory power of variables. In this case, Age has highest (.539) and Job
Type(.238) has lowest explanatory power.
ply   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
,
Here the Box’s M is not significant (p value =.892 > 0.05) this suggests there is no
An   enough evidence to conclude that covariance matrices are significantly different
across two groups. So assumption of equal covariance matrices holds good
aly   v)   Cross-validated accuracy is 64.3%. this data has equal number of successes and
failures. The chance accuracy for the data is   p(S)2 + p(F)2 = 0.25+.25 = 0.5
se,   We need atleast 25% improvement over chance accuracy i.e. 0.5 * 1.25 = 62.5% the overall cross
Ev   validated accuracy is better than minimum required accuracy hence, Ideally the model could be
used for prediction, but since the power of model is too low and there are some non-significant
alu   variables in the model like Job type (sig value .084 > 0.05 indicating this variable does not add
value in the model) you can avoid using the model. You may use stepwise DA.
at
e
a
Marking Scheme:
1. Which multivariate technique is applied in this scenario, and why is it suitable? (1 Mark)
•   Multivariate Technique Applied: Logistic Regression Why?
Q5   • The dependent variable (Loan Approval: Approved=1, Rejected = 0) is binary
(categorical).
CO   •   Logistic regression models the probability of approval using predictor variables.
2. Write the function used in the model. (1 Mark)
-
The logistic regression model function is:
1,2   e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
p ( x ) = 1 + e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
,3;
3. Interpret the pseudo R-square values and their significance. (1 Mark)
BL-   • The model explains 4.7% to 26.2% of the variance in loan approval decisions.
4. Which test statistic(s) are used to evaluate the accuracy of the model? (2 Marks)
Ap   • Wald Test: p <0.05): significant model
ply   • Hosmer-Lemeshow Test (p > 0.05): significant model   [15
,   5. Analyze the classification table and explain its implications. (2 Marks)   ]
False Negatives (Type II Error):
An   • The model predicted all loans as "approved" (1) since no "0" (denials) were predicted.
aly   •   There were 2 cases where loans were actually denied (0), but the model misclassified
them as approved (1). This leads to a 0% accuracy for denied loans.
se,   True Positives:
• The model correctly classified 98 approved loans (1) as approved.
Ev
• Accuracy for approved loans is 100%.
alu   Overall Accuracy:
• 98 out of 100 cases were classified correctly, leading to an overall accuracy of 98%.
at
e   6. Define and interpret the Sensitivity and Specificity of this model. (2 Marks)
•   Sensitivity (Recall) = TP / (TP + FN)
Measures the model’s ability to correctly identify actual positives (approved loans).
•   Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify actual negatives (denied loans).
•   Sensitivity = 100%: The model perfectly identifies approved loans.
********** 8 **********
--- page 9 ---
•   Specificity = 0%: The model completely fails to identify denied loans, predicting
all as approved.
7. Interpret the coefficients of the model. (3 Marks)
Odds Ratio (Exp(B)):
• Age → A 1-year increase in Age increases odds of approval by 0.024.
• Income → A $1,000 increase in income raises odds by 0.098
•   Credit Score → A 10-point increase in Credit Score raises odds by 0.005
Loan Type (b4=1.5) → Home Loan applicants are 0.389 times more likely to be approved.
Q5 b
Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as an
CO
outlier.
-;
Here, 4/(n-k-1) = 4/ (30-3-1) = 0.154
SO   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.154)   [5]
-;
BL-
a Explain the research design for cluster analysis and differentiate between hierarchical
. and non-hierarchical clustering techniques.
Q6   Synoptic Answer:
Cluster analysis groups similar data points together based on predefined criteria.
CO   Key Points:
-
1. Definition of Cluster Analysis (1 mark) – A technique used for segmenting data
1,2   into meaningful groups.
2. Research Design (1 mark) – Identify objectives, select clustering method, choose   [5]
,3;
distance metric, validate results.
BL-   3. Hierarchical Clustering (1 mark) – Builds a nested hierarchy using agglomerative
or divisive approaches.
Ap
4. Non-Hierarchical Clustering (1 mark) – Assigns data into pre-specified clusters
ply   (e.g., K-means).
5. Comparison (1 mark) – Hierarchical is useful for small datasets; K-means is
efficient for large datasets.
Q6 b
Solution:
CO   a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
-   Students may answer the other parts as per their choice of solution, i.e. 2 or 3.
2,3   b. Student may write the case numbers as per his choice of 2 or 3 cluster solution.
;   c. ANOVA is significant for all variables (for 2 cluster solution) indicating that all
variables are contributing in the cluster analysis. This also validates the cluster
results.   [15
BL-
*Students may write for 3 cluster solution as well.
]
Un   d. What are characteristics of each group? (For 3 cluster solution)
de
Cluste   LuxaryIt   Tech   CustomerSer
rst   r   N   Online_Sho   Discount   BrandLo   ImpulseBu   EcoFrie   ems   Savv   vice
pping   s   yalty   ying   ndly   y
an   1   1   5.67   5.47   4.87   7.07   3.07   5.53   7.8   7.60
5   0
d
********** 9 **********
--- page 10 ---
2   1   7.20   7.80   8.10   5.60   6.20   3.50   4.9   4.20
0   0
Total   2   6.28   6.40   6.16   6.48   4.32   4.72   6.6   6.24
5   4
Cluster 1: Low on BrandLoyalty, EcoFriendly , Moderate on Online_Shopping, Discounts
and LuxaryItems and High on ImpulseBuying, TechSavvy and CustomerService
Cluster 2: Low/ Moderate on ImpulseBuying, LuxaryItems, TechSavvy and
CustomerService but High on Online_Shopping, Discounts, BrandLoyalty and
EcoFriendly.
*Students may write for 3 cluster solution as well.
e. Cluster 1 is likely to be more profitable because:
1. High Impulse Buying: Customers frequently make unplanned purchases, leading
to higher revenue.
2. Tech-Savvy: More likely to engage with digital promotions, e-commerce
platforms, and AI-driven recommendations, increasing sales.
3. Strong Preference for Customer Service: Willing to pay a premium for better
support and experiences, leading to higher margins.
While Cluster 2 values discounts and brand loyalty, they may focus more on price
sensitivity and long-term relationships rather than impulsive, high-margin purchases.
*Students may write for 3 cluster solution as well.
a
Q7
Answer
CO
0.6
-
Sales
1,2   Mont   Reve
nue
,3;   h   ($100
0s)   4 moving avg   Exp sm
BL-
Jan   120   125   25
Ap   Feb   135   122   169   [10
ply   Mar   140   129.8   104.04   ]
Apr   150   135.92 198.2464
,   564.0
May   160
136.25   625   144.368 244.3594
An
564.0   153.747
Jun   170
aly   146.25   625   2 264.1535
163.498
se,   Jul   180   155   625   9   272.287
Ev   173.399
165   6
alu
********** 10 **********
--- page 11 ---
at
e
Method   Forecast   MSE
4 moving   165   584.375
Expo sm alpha = 0.6   173.3996   182.4409
Exponential Smoothing with alpha = 0.6 is best as it has
minimum MSE
Final Forecast is 173.3996
b Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
,3;
BL-
The model selection is done on the basis of following parameters
Ap
1. Requirement of stationarity (in this case d = 0)
ply   2. BIC as low as possible   [10
3. All lags (except intercept) need to be significant
,   ]
4. Ljung-Box test should not be significant
An   5. Residual ACF & PACF should be within the lines
aly   Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
se,   In above case
Ev   Sr No Model   BIC   Description   Result
1   ARIMA(1,0,0   6.875   Correct : d=0, LB test not sig, lag1 sig   Model can
alu   )   & Residual ACF & PACF within range   be used
2   ARIMA(0,0,1   7.703   Correct : d=0, , lags sig. problem –   Model
at
)   Residual ACF & PACF not within range, cannot be
e   LB test sig   used
3   ARIMA(2,0,0   7.012   Correct : d=0, LB test not sig, problem Model
)   – ACF & PACF not within range, lag2   cannot be
not sig   used
4   ARIMA(1,1,0   7.012   Correct : LB test not sig, Residual ACF   Model
)   & PACF not within range   cannot be
problem – d=1, lag not sig ACF &   used
PACF not within range
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) as it satisfies all criteria, it is simplest and has lowest
BIC. hence company should use following forecasts
Model   21   22   23   24   25
Price-Model_1   Forecast   3041.33   3038.10 3035.01 3032.05 3029.23
UCL   3085.28   3098.91 3107.90 3114.46 3119.46
LCL   2997.38   2977.29 2962.12 2949.65 2939.00
Forecast
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 8 · Answer key · paper 4ff9e38b59ae

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2024/Sem_08/Final-Exam/MBATech_IT_7041/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Apr 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Semester VIII(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 29 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a Explain the significance of predictive analytics in gaining a competitive advantage in
. business.
Synoptic Answer:
Predictive analytics involves using historical data, statistical models, and machine learning
techniques to make predictions about future outcomes. It helps businesses make
proactive, data-driven decisions.
CO
-1;   Key Points:
Definition & Importance (1 mark) – Predictive analytics anticipates future trends based
BL-
Un   on historical patterns.   [5]
de   Key Techniques (1 mark) – Regression analysis, decision trees, neural networks, and time
rst
an   series forecasting.
d   Applications in Business (1 mark) – Demand forecasting, customer behavior analysis, risk
assessment.
Competitive Advantage (1 mark) – Helps in optimizing pricing, improving customer
retention, and enhancing operational efficiency.
Example (1 mark) – Retailers use predictive analytics to forecast inventory demand and
reduce stockouts.
********** 1 **********
--- page 2 ---
b What are the common methods to deal with missing data during data preprocessing?
.   Synoptic Answer:
Missing data can distort analysis, leading to biased results. Proper handling is crucial for
CO   reliable models.
-1;   Key Points:
BL-   1. Understanding Missing Data (1 mark) – Types: MCAR (Missing Completely at
Un   Random), MAR (Missing at Random), MNAR (Missing Not at Random).
de   2. Deletion Methods (1 mark) – Listwise deletion (removing entire rows), Pairwise   [5]
rst   deletion (removing only missing values).
an   3. Imputation Techniques (1 mark) – Mean, median, mode imputation; Regression-
d,   based imputation.
ap   4. Advanced Techniques (1 mark) – Multiple Imputation, KNN imputation,
ply   Predictive modeling.
5. Example (1 mark) – In customer survey data, missing age values can be imputed
using the median age of respondents.
c Discuss the assumptions of regression models, focusing on heteroscedasticity and
.   multicollinearity.
CO   Synoptic Answer:
-   Regression models are based on specific assumptions, and violations affect accuracy and
1,2   reliability.
;   Key Points:
BL-   1. Overview of Regression Assumptions (1 mark) – Linearity, Independence,
Un   Homoscedasticity, Normality, No multicollinearity.   [5]
de   2. Heteroscedasticity (1 mark) – Variance of residuals is unequal across
rst   observations, leading to inefficient estimates.
an   3. Detection (1 mark) – Breusch-Pagan test, White test, residual plots.
d,   4. Remedies (1 mark) – Log transformation, Weighted Least Squares (WLS), robust
ap   standard errors.
ply   5. Multicollinearity (1 mark) – High correlation among independent variables; detected
using VIF (>10 indicates concern).
d Compare K-Nearest Neighbors (KNN) classification with logistic regression.
CO
-   .   Synoptic Answer:
Both methods classify data points but differ in their approach and applicability.
2,3
Key Points:
;
1. Definition & Overview (1 mark) – KNN is a non-parametric, instance-based
BL-
learning algorithm; Logistic Regression is a statistical method for binary   [5]
Un
classification.
de
2. Mechanism (1 mark) – KNN classifies based on nearest neighbors; Logistic
rst
Regression estimates probability using the sigmoid function.
an
3. Advantages (1 mark) – KNN is simple and handles non-linearity; Logistic
d,
Regression is interpretable and computationally efficient.
ap
4. Limitations (1 mark) – KNN is computationally expensive for large datasets;
ply
Logistic Regression assumes linearity.
********** 2 **********
--- page 3 ---
5. Example (1 mark) – In customer churn prediction, Logistic Regression identifies
key drivers, while KNN finds patterns in similar customers.
Marking Scheme:
1.   Which model was applied, and why? .....01 mark
The Multiple Linear Regression (MLR) model was applied because the company wants to
predict Sales Revenue based on multiple independent variables:
•   Advertising Spend
•   Social Media Reach
•   Product Reviews
• Campaign Type (categorical variable)
MLR is appropriate as it examines the relationship between multiple predictors and a
continuous dependent variable.
2.   Identify the baseline for qualitative predictor. .....01 mark
• The qualitative predictor is Campaign Type (Online = 1, Others = 0).
• The baseline category is Others (TV and Print Ads, coded as 0).
Q2
3.   State the model equation. .....01 marks
CO   Sales Revenue=
-   -9.629+2.702(Advertising Spend)+0.809(Social Media Reach)+1.484(Product Reviews)-
2.718
1,2
,3;   4.   Interpret the coefficient of the independent variable Campaign_Online…..02marks
BL-
Ap   It can be interpreted that Sales revenue will be lowered by -2.718 units when the   [20
ply   campaign is Online than when it would be offline (others).
,   ]
An
aly   1. Explain why the constant coefficient (b₀) has no practical meaning in this context. .....01
se,   marks
Ev
alu   b0 is the predicted Sales Revenue when all predictors are zero (i.e., no advertising spend, no
social media reach, zero product reviews, and only traditional campaigns).
at
e   This scenario is unrealistic, making b0 meaningless in practical business decisions.
2. Can the equation be used for prediction? Explain. .....01 marks
Since, Campaign_Online is an insignificant predictor (p=.541) of Sales Revenue; the model
cannot be used for prediction purposes.
3. Determine the coefficient of multiple determination (R²) and interpret its significance. .....02
marks
R² = 0.963, meaning 96.3% of the variation in sales revenue is explained by the independent
variables.
This is a strong R² value, suggesting the model is effective in predicting sales revenue.
********** 3 **********
--- page 4 ---
4. Identify which variable has the highest impact on sales revenue and which has the least
impact. .....02 marks
The highest impact variable: Social Media Reach
The least impact variable: Campaign Type
9.   What does the VIF (Variance Inflation Factor) indicate? .....01 marks
The VIF values are:
•   Advertising Spend: 1.006
•   Social Media Reach: 1.038
•   Product Reviews: 1.071
• Campaign Type: 1.056
Since all VIF values are below 5, there is no significant multicollinearity, meaning the
predictors are independent and do not distort the model.
10.   Interpret the PP plot. .....01 marks
The PP plot follows a nearly straight line, indicating that residuals are normally
distributed.
Small deviations exist, but they are within acceptable limits, so the normality assumption
holds.
11.   Analyze the normality of residuals using a histogram. .....01 marks
• The histogram of residuals is approximately bell-shaped, supporting the assumption of
normality.
• No extreme skewness or outliers were detected, confirming that the model errors are well-
distributed.
12.   Interpret the residual plot and analyze the residuals: Do they show any patterns indicating
model bias or need for improvement? .....01 marks
• The residual plot shows random scatter, meaning there are no clear patterns or trends.
• No heteroscedasticity (funnel-shaped pattern) was detected, meaning variance is constant.
•   This suggests no major model bias and that the assumptions of regression hold.
13.   Examine the ANOVA table: What does the significance (p-value) tell us about the overall
model fit? .....01 marks
F-statistic p-value (which is < 0.05), meaning the model is statistically significant.
14.   Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals? .....01 marks
Durbin-Watson (DW) = 2.388, which is close to 2, meaning no significant autocorrelation
in residuals.
15.   Predict the sales revenue when:
•   Advertising Spend: $11,000
•   Social Media Reach: 130,000 users
•   Product Reviews: 9.1 (average rating)
•   Campaign Type: Online .....03 marks
Given:
•   Advertising Spend = $11,000
•   Social Media Reach = 130,000 users
•   Product Reviews = 9.1
• Campaign Type = Online (1)
Using the model equation:
Sales Revenue: 136.0494
********** 4 **********
--- page 5 ---
Answers
Synoptic
a) this is three factor solution.
Rotated Component Matrixa
Component
1   2   3
Rate Baskin Robbins on
0.298   0.199   0.804
taste
Rate Baskin Robbins on
0.025   0.186   0.919
number of flavours
Rate Baskin Robbins on
0.055   0.748   0.297
Indian flavours
Rate Baskin Robbins on
0.406   0.577   0.182
packaging
Rate Baskin Robbins on
0.15   0.853   0.102
availability
Rate Baskin Robbins on
0.667   0.478   0.044
promotional offers
Rate Baskin Robbins on
Q3   Service   0.646   0.212   0.479
Rate Baskin Robbins on
CO   Advertising   0.868   -0.001   0.06
-   Rate Baskin Robbins on
0.529   0.349   0.356
1,2   value for money
,3;   Extraction Method: Principal Component Analysis.
BL-   Rotation Method: Varimax with Kaiser Normalization.
Ap   [20
Note to evaluators : Factor names are subjective student may name them
ply   in multiple ways   ]
Ev   Factor 2 (Local
alu   Factor 1 (Service   flavours   Factor 3 (Taste
at   Advertising & Price)   Availability)   Choices)
e,   Rate Baskin Robbins on   Rate Baskin   Rate Baskin
Robbins on
cre   Service   Indian flavours   Robbins on taste
at   Rate Baskin   Rate Baskin
Rate Baskin Robbins on
e   Advertising   Robbins on   Robbins on
availability   number of flavours
Rate Baskin Robbins on
value for money
b) Variables “Rate Baskin Robbins on packaging” & “ Rate Baskin Robbins on promotional
offers” have cross loadings hence need to be removed.
c) Scree plot indicates 3 factor as good solution
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5, total
explained variance > 60% indicates a good solution, however above mentioned two
variables have cross loadings, hence the solution needs to be revised by removing these
two variables.
Factor 1 (Service Advertising & Price) is most important factor as it has highest eigen value.
e) Selecting the right number of factors is crucial in factor analysis. Here are the
commonly used methods:
1. Eigenvalues (Kaiser’s Criterion)
• Retain factors with eigenvalues > 1 (i.e., explaining more variance than a single
variable).
********** 5 **********
--- page 6 ---
• Helps in determining significant factors based on variance contribution.
• Works well when the number of variables is less than 30.
2. Scree Plot (Elbow Method)
• A graphical representation of eigenvalues.
• The plot shows a sharp decline (elbow point), after which the curve flattens.
•   Factors before the elbow are retained.
3. Variance Explained Criterion
• Choose the number of factors that together explain at least 60%-70% of the total
variance.
• The cumulative variance contribution is checked for interpretability.
5. Factor Loadings & Interpretability
• Examine factor loadings after extraction.
• The chosen number of factors should make theoretical sense and be interpretable.
a
Answer:
5NN
Standar Standar   Standar   Standar
Q4
dised   dised   dised   dised   Standardis
CO   Distanc   Distance Distance Distance ed Distance
e of 1st   of 2nd   of 3rd   of 4th   of 5th
-   Visit
Supermarke   observa observat observat observat   observation
1,2   t   tion   ion   ion   ion
N   4   6   5   6   7
,3;
N   2   2   3   7   4
BL-   N   7   3   7   4   3
N   5   7   1   3   6
Ap
N   6   5   4   2   5
ply   Y   1   4   2   5   1   [10
,   Y   3   1   6   1   2   ]
An   Rank
aly   1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
se,   3 Y   N   Y   N   N
Ev   4 N   Y   N   N   Y
5 N   N   N   Y   N
alu
Prediction Y   Y   N   N   Y
at   Actual Y   N   N   N   Y
e
Predicti
on   Actual
Y   Y
Y   N
********** 6 **********
--- page 7 ---
N   N
N   N
Y   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   2   2
Grand Total   2   3   5
Accuracy   80.00%
100.00
Recall / Sensitivity   %
Specificity   66.67%
Precision   66.67%
3NN
Rank
1 Y   Y   N   Y   Y
2 Y   Y   Y   N   Y
3 Y   N   Y   N   N
Prediction Y   Y   Y   N   Y
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Row Labels   N   Y   Grand Total
Actual   N   1   2   3
Y   2   2
Grand Total   1   4   5
Accuracy   60.00%
100.00
Recall / Sensitivity   %
Specificity   33.33%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
Q4 b Answers
i)   Discriminant Function = -3.754 + .057 * Age (years) + .052 * Salary ($1000s) + 0.108 *
CO   Years at Company + .651 * Job Type -.025 * Months since Last Raise   [10
ii)   Wilks lambda signifies discriminating power for the model. Lower the value(close to
-   ]
0), better discrimination. Higher the value (close to 1 ) less discriminating power of
1,2   the model. In this case wilk’s lambda is .848 => close to 1 hence the model has poor
discriminating power.
********** 7 **********
--- page 8 ---
,3;   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of variables.
BL-   And lowest absolute values ( modulus since it is correlations) indicate lowest
Ap   explanatory power of variables. In this case, Age has highest (.539) and Job
Type(.238) has lowest explanatory power.
ply   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
,
Here the Box’s M is not significant (p value =.892 > 0.05) this suggests there is no
An   enough evidence to conclude that covariance matrices are significantly different
across two groups. So assumption of equal covariance matrices holds good
aly   v)   Cross-validated accuracy is 64.3%. this data has equal number of successes and
failures. The chance accuracy for the data is   p(S)2 + p(F)2 = 0.25+.25 = 0.5
se,   We need atleast 25% improvement over chance accuracy i.e. 0.5 * 1.25 = 62.5% the overall cross
Ev   validated accuracy is better than minimum required accuracy hence, Ideally the model could be
used for prediction, but since the power of model is too low and there are some non-significant
alu   variables in the model like Job type (sig value .084 > 0.05 indicating this variable does not add
value in the model) you can avoid using the model. You may use stepwise DA.
at
e
a
Marking Scheme:
1. Which multivariate technique is applied in this scenario, and why is it suitable? (1 Mark)
•   Multivariate Technique Applied: Logistic Regression Why?
Q5   • The dependent variable (Loan Approval: Approved=1, Rejected = 0) is binary
(categorical).
CO   •   Logistic regression models the probability of approval using predictor variables.
2. Write the function used in the model. (1 Mark)
-
The logistic regression model function is:
1,2   e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
p ( x ) = 1 + e − 4.378 + 0.024( Age ) + 0.098( Income ) + 0.05( CredtScore ) + 0.398(Loantype)
,3;
3. Interpret the pseudo R-square values and their significance. (1 Mark)
BL-   • The model explains 4.7% to 26.2% of the variance in loan approval decisions.
4. Which test statistic(s) are used to evaluate the accuracy of the model? (2 Marks)
Ap   • Wald Test: p <0.05): significant model
ply   • Hosmer-Lemeshow Test (p > 0.05): significant model   [15
,   5. Analyze the classification table and explain its implications. (2 Marks)   ]
False Negatives (Type II Error):
An   • The model predicted all loans as "approved" (1) since no "0" (denials) were predicted.
aly   •   There were 2 cases where loans were actually denied (0), but the model misclassified
them as approved (1). This leads to a 0% accuracy for denied loans.
se,   True Positives:
• The model correctly classified 98 approved loans (1) as approved.
Ev
• Accuracy for approved loans is 100%.
alu   Overall Accuracy:
• 98 out of 100 cases were classified correctly, leading to an overall accuracy of 98%.
at
e   6. Define and interpret the Sensitivity and Specificity of this model. (2 Marks)
•   Sensitivity (Recall) = TP / (TP + FN)
Measures the model’s ability to correctly identify actual positives (approved loans).
•   Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify actual negatives (denied loans).
•   Sensitivity = 100%: The model perfectly identifies approved loans.
********** 8 **********
--- page 9 ---
•   Specificity = 0%: The model completely fails to identify denied loans, predicting
all as approved.
7. Interpret the coefficients of the model. (3 Marks)
Odds Ratio (Exp(B)):
• Age → A 1-year increase in Age increases odds of approval by 0.024.
• Income → A $1,000 increase in income raises odds by 0.098
•   Credit Score → A 10-point increase in Credit Score raises odds by 0.005
Loan Type (b4=1.5) → Home Loan applicants are 0.389 times more likely to be approved.
Q5 b
Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as an
CO
outlier.
-;
Here, 4/(n-k-1) = 4/ (30-3-1) = 0.154
SO   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.154)   [5]
-;
BL-
a Explain the research design for cluster analysis and differentiate between hierarchical
. and non-hierarchical clustering techniques.
Q6   Synoptic Answer:
Cluster analysis groups similar data points together based on predefined criteria.
CO   Key Points:
-
1. Definition of Cluster Analysis (1 mark) – A technique used for segmenting data
1,2   into meaningful groups.
2. Research Design (1 mark) – Identify objectives, select clustering method, choose   [5]
,3;
distance metric, validate results.
BL-   3. Hierarchical Clustering (1 mark) – Builds a nested hierarchy using agglomerative
or divisive approaches.
Ap
4. Non-Hierarchical Clustering (1 mark) – Assigns data into pre-specified clusters
ply   (e.g., K-means).
5. Comparison (1 mark) – Hierarchical is useful for small datasets; K-means is
efficient for large datasets.
Q6 b
Solution:
CO   a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
-   Students may answer the other parts as per their choice of solution, i.e. 2 or 3.
2,3   b. Student may write the case numbers as per his choice of 2 or 3 cluster solution.
;   c. ANOVA is significant for all variables (for 2 cluster solution) indicating that all
variables are contributing in the cluster analysis. This also validates the cluster
results.   [15
BL-
*Students may write for 3 cluster solution as well.
]
Un   d. What are characteristics of each group? (For 3 cluster solution)
de
Cluste   LuxaryIt   Tech   CustomerSer
rst   r   N   Online_Sho   Discount   BrandLo   ImpulseBu   EcoFrie   ems   Savv   vice
pping   s   yalty   ying   ndly   y
an   1   1   5.67   5.47   4.87   7.07   3.07   5.53   7.8   7.60
5   0
d
********** 9 **********
--- page 10 ---
2   1   7.20   7.80   8.10   5.60   6.20   3.50   4.9   4.20
0   0
Total   2   6.28   6.40   6.16   6.48   4.32   4.72   6.6   6.24
5   4
Cluster 1: Low on BrandLoyalty, EcoFriendly , Moderate on Online_Shopping, Discounts
and LuxaryItems and High on ImpulseBuying, TechSavvy and CustomerService
Cluster 2: Low/ Moderate on ImpulseBuying, LuxaryItems, TechSavvy and
CustomerService but High on Online_Shopping, Discounts, BrandLoyalty and
EcoFriendly.
*Students may write for 3 cluster solution as well.
e. Cluster 1 is likely to be more profitable because:
1. High Impulse Buying: Customers frequently make unplanned purchases, leading
to higher revenue.
2. Tech-Savvy: More likely to engage with digital promotions, e-commerce
platforms, and AI-driven recommendations, increasing sales.
3. Strong Preference for Customer Service: Willing to pay a premium for better
support and experiences, leading to higher margins.
While Cluster 2 values discounts and brand loyalty, they may focus more on price
sensitivity and long-term relationships rather than impulsive, high-margin purchases.
*Students may write for 3 cluster solution as well.
a
Q7
Answer
CO
0.6
-
Sales
1,2   Mont   Reve
nue
,3;   h   ($100
0s)   4 moving avg   Exp sm
BL-
Jan   120   125   25
Ap   Feb   135   122   169   [10
ply   Mar   140   129.8   104.04   ]
Apr   150   135.92 198.2464
,   564.0
May   160
136.25   625   144.368 244.3594
An
564.0   153.747
Jun   170
aly   146.25   625   2 264.1535
163.498
se,   Jul   180   155   625   9   272.287
Ev   173.399
165   6
alu
********** 10 **********
--- page 11 ---
at
e
Method   Forecast   MSE
4 moving   165   584.375
Expo sm alpha = 0.6   173.3996   182.4409
Exponential Smoothing with alpha = 0.6 is best as it has
minimum MSE
Final Forecast is 173.3996
b Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph below, the
lags and are above zero as well as below zero indicating stationarity. There is no need for
difference for this data.
Q7
CO
-
1,2
,3;
BL-
The model selection is done on the basis of following parameters
Ap
1. Requirement of stationarity (in this case d = 0)
ply   2. BIC as low as possible   [10
3. All lags (except intercept) need to be significant
,   ]
4. Ljung-Box test should not be significant
An   5. Residual ACF & PACF should be within the lines
aly   Any simplest model that satisfies above parameters is the best model and can be used for
forecasting.
se,   In above case
Ev   Sr No Model   BIC   Description   Result
1   ARIMA(1,0,0   6.875   Correct : d=0, LB test not sig, lag1 sig   Model can
alu   )   & Residual ACF & PACF within range   be used
2   ARIMA(0,0,1   7.703   Correct : d=0, , lags sig. problem –   Model
at
)   Residual ACF & PACF not within range, cannot be
e   LB test sig   used
3   ARIMA(2,0,0   7.012   Correct : d=0, LB test not sig, problem Model
)   – ACF & PACF not within range, lag2   cannot be
not sig   used
4   ARIMA(1,1,0   7.012   Correct : LB test not sig, Residual ACF   Model
)   & PACF not within range   cannot be
problem – d=1, lag not sig ACF &   used
PACF not within range
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) as it satisfies all criteria, it is simplest and has lowest
BIC. hence company should use following forecasts
Model   21   22   23   24   25
Price-Model_1   Forecast   3041.33   3038.10 3035.01 3032.05 3029.23
UCL   3085.28   3098.91 3107.90 3114.46 3119.46
LCL   2997.38   2977.29 2962.12 2949.65 2939.00
Forecast
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is not
too wide for initial forecasts. As the forecasting period extends, width becomes wider
making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Re-Exam · Sem 8 · Answer key · paper 22db61f16839

- Departments: Chemical
- Programmes: MBATech (CHEMICAL ENGINEERING) - 7045
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/MBATech (CHEMICAL ENGINEERING) - 7045/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Sem 8 Re-exam(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 02 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a How does data visualization enhance decision-making in business analytics?
.
Synoptic Answer:
Data visualization converts complex information into graphical formats for better
decision-making.
CO-   Key Points:
1;
BL-   1. Definition (1 mark) – Visual representation of data through graphs, charts,   [5]
Und   dashboards.
erst   2. Benefits (1 mark) – Identifies trends, outliers, and correlations.
and   3. Types (1 mark) – Bar charts, scatter plots, heat maps, dashboards.
4. Business Applications (1 mark) – Sales forecasting, customer segmentation,
fraud detection.
5. Example (1 mark) – A retail company uses dashboards to track regional sales
performance.
CO- b What are the essential steps in handling outliers in data pre-processing?
1;
.
BL-   Synoptic Answer:
Und   [5]
erst   Outliers can distort statistical models and must be handled carefully.
and,
appl   Key Points:
y
********** 1 **********
--- page 2 ---
1. Definition & Causes (1 mark) – Data errors, genuine variations, fraudulent
activities.
2. Detection Methods (1 mark) – Box plots, Z-score method, IQR rule.
3. Treatment Strategies (1 mark) – Winsorization, transformation (log/square
root), capping.
4. Removing Outliers (1 mark) – If justified, remove extreme values.
5. Example (1 mark) – In a salary dataset, a CEO’s salary may be an outlier
compared to employees.
c Explain the role of dummy variables in multiple regression analysis with an example.
.
Synoptic Answer:
Dummy variables convert categorical data into numerical format for regression
CO-
models.
1,2;
BL-
Key Points:
Und   [5]
erst
1. Definition (1 mark) – Used to include categorical data in regression models.
and,
2. Creation (1 mark) – Assign 0/1 to different categories.
appl
3. Example (1 mark) – Gender (Male = 1, Female = 0).
y
4. Regression Interpretation (1 mark) – Dummy variable coefficients show
category effects.
5. Business Application (1 mark) – Analyzing salary differences between
departments.
d Describe the concepts of sensitivity and specificity in the context of classification
models.
.
Synoptic Answer:
Sensitivity and specificity measure the performance of classification models.
CO-
2,3;
Key Points:
BL-
Und   1. Sensitivity (1 mark) – Measures true positive rate (correctly classified   [5]
erst
positive cases).
and,
2. Specificity (1 mark) – Measures true negative rate (correctly classified
appl
negative cases).
y
3. Trade-off (1 mark) – Higher sensitivity lowers specificity and vice versa.
4. Use Cases (1 mark) – Sensitivity in medical tests; specificity in fraud
detection.
5. Example (1 mark) – A cancer screening test prioritizes sensitivity to detect all
positive cases.
Q2
Answers   [2
CO-
1,2,   1. What type of model was applied, and why is it appropriate for this scenario?   0]
3;   The Multiple Linear Regression (MLR) model was applied because the resale price
BL-   (dependent variable) is continuous and influenced by multiple predictors:
********** 2 **********
--- page 3 ---
Appl   o Car Age
y,   o Mileage
Anal   o Engine Power
yse,   o Fuel Type (categorical)
Eval   • MLR is appropriate for predicting a continuous variable based on multiple factors.
uate
2. Which category serves as the reference for the qualitative variable (Fuel Type), and
why?
• The categorical variable is Fuel Type (Petrol = 1, Diesel = 0).
• The baseline/reference category is Diesel (coded as 0).
3. Write down the equation obtained from the analysis.
Resale Price=-
1.003−0.773(Car Age)−0.043(Mileage)+0.304(Engine Power)+1.380(Fuel Type)
4. Explain the significance of coefficient of Fuel Type in the model.
•   (Fuel Type - Petrol): Petrol cars are, on average, 1.380 more expensive than Diesel
cars.
5. Why does the intercept (b0) lack practical interpretation in this context?
• The intercept represents the resale price when all predictors are zero (0-year-old car,
0 mileage, 0 HP, Diesel).
•   This is not realistic as cars always have mileage, age, and power.
6. Can this equation be reliably used to estimate resale prices? Support your answer with
reasoning.
• The equation is reliable because:
o R² = 0.971, meaning the model explains 97.1% of the variation in resale
price.
o P-values for predictors are statistically significant (<0.05).
o Residuals are normally distributed, making the predictions valid.
7. Determine and interpret the coefficient of multiple determination (R²). How well does
the model explain variations in resale price?
• R² = 0.971, meaning 97.1% of the variance in resale price is explained by the model.
8. Which predictor has the most influence on resale price, and which has the least
impact? Explain your findings.
• Most influential predictor: Engine Power
•   Least influential predictor: Fuel Type – Petrol
9. What does the Variance Inflation Factor (VIF) reveal about multicollinearity among
the predictors?
• The VIF values are:
o Car Age: 1.063
o Mileage: 1.016
o Engine Power:1.025
o Fuel Type: 1.025
•   Since all VIF values are beow 5, multicollinearity is not a concern.
10. Analyze the P-P plot. Does it suggest that residuals follow a normal distribution?
•   Yes, the P-P plot follows a 45-degree straight line, meaning residuals are normally
distributed.
********** 3 **********
--- page 4 ---
11. Examine the residual histogram. Does the distribution appear normal, or are there
deviations?
• The histogram of residuals is bell-shaped, confirming normality.
•   There are no extreme outliers, meaning the model is well-behaved.
12. Evaluate the residual plot. Are there any noticeable patterns indicating problems with
the model?
• The residual plot shows no clear pattern, indicating homoscedasticity (constant
variance).
• The random scatter confirms that the model does not suffer from systematic bias.
13. Examine the ANOVA table: What does the significance (p-value) tell us about the
overall model fit?
• The F-statistic p-value (<0.05);ljm , meaning the model is statistically significant
14. Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals?
• Durbin-Watson (DW) = 2.041, which is close to 2, indicating no significant
autocorrelation in residuals.
15. Predict the resale price for a car with these features:
• Car Age = 5 years
• Mileage = 60,000 miles
• Engine Power = 150 HP
•   Fuel Type = Petrol (1)
Using the regression equation:
31.802
a
Synoptic
a) this is three factor solution.
Rotated Factor Matrixa
Q3
Factor
CO-
1   2   3
1,2,
3;   [Price]   0.043   0.992   0.026
BL-   [2
Appl   [Quantity]   0.062   0.921   0.019
y   0]
[Product Variety]   0.986   0.024   0.097
Eval
uate   [Advertisements]   0.131   0.028   0.966
,
crea   [Health Concern ( Sugar free, fat free etc)]   0.985   0.04   0.129
te
[Presentation of Ice Cream]   0.137   0.024   0.967
[Value for money]   -0.016   0.954   0.02
********** 4 **********
--- page 5 ---
[Product Ingredients]   0.959   0.029   0.121
Extraction Method: Principal Axis Factoring.
Rotation Method: Varimax with Kaiser Normalization.
Note to evaluators : Factor names are subjective student may name them in multiple ways
Factor 1 (Healthy   Factor 3 (in-
Choices)   Factor 2 (Tangible)   Tangible)
[Product Variety]   [Price]   [Advertisements]
[Health Concern ( Sugar   [Presentation of
[Quantity]
free, fat free etc)]   Ice Cream]
[Product Ingredients]   [Value for money]
b) there is no variable that should not be there in the factor analysis as all variables
have anti-aging correlations >0.5, extraction communality >0.5, and non of them
have any cross loading.
c) Scree plot indicates 3 factors as good solution however 3 factors have steep slopes
4th factor slope is not so steep
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5,
total explained variance > 60% all variables have communality >0.5, and there is no
cross loading indicates a good solution. Yes factor analysis is relevant in this case
and this solution can be used
e) Factor 1 (Healthy Choices) is the most important factor As it has highest
communality.
F. Difference Between PCA & Common Factor Analysis
Principal Component   Common Factor
Feature
Analysis (PCA)   Analysis (CFA)
Data reduction and   Identifying latent factors
Purpose   transformation to   that explain the observed
uncorrelated components.   variables.
Explanatory, used to
Descriptive, used to
Type of Analysis   uncover hidden
summarize variance in data.
constructs.
Focuses only on shared
Mathematical   Maximizes total variance in
(common) variance
Basis   the data.
among variables.
Components are extracted   Factors are extracted to
Factor
to explain the maximum   explain correlations
Extraction
variance.   between variables.
Correlation   Does not assume any   Assumes an underlying
Assumption   underlying factor structure. structure where observed
********** 5 **********
--- page 6 ---
variables load onto latent
factors.
Data compression,   Psychological, social, and
Use Cases   dimensionality reduction,   economic research to
visualization.   study latent traits.
Factors represent
Components are
underlying traits or
mathematical constructs
Interpretability   constructs that explain
and may not have direct
relationships among
interpretability.
variables.
a Answer:
5NN
Standa
Standar   Standar
rdised
dised   dised   Standardis
Distan   Standardised
Distance Distance ed Distance
ce of   of 2nd   of 3rd   of 4th   Distance of
1st   5th
observation
observat observat   observation
observ
ion   ion
Visit Supermarket   ation
N   4   1   5   4   1
Q4   Y   1   6   6   7   4
N   7   5   3   2   7
CO-
Y   2   2   4   1   3
1,2,   N   5   7   7   3   6
3;   Y   6   3   2   6   5
N   3   4   1   5   2
BL-
[1
Appl   Rank
1 Y   N   N   Y   N   0]
y,
2 Y   Y   Y   N   N
Anal   3 N   Y   N   N   Y
4 N   N   Y   N   Y
yse,
5 N   N   N   N   Y
Eval
uate   Prediction   N   N   N   N   Y
Actual   Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   3   3
Y   1   1   2
Grand Total   4   1   5
********** 6 **********
--- page 7 ---
Accuracy   80.00%
Recall / Sensitivity   50.00%
100.00
Specificity   %
100.00
Precision   %
3NN
Rank
1 Y   N   N   Y   N
2 Y   Y   Y   N   N
3 N   Y   N   N   Y
Prediction Y   Y   N   N   N
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   1   1   2
Grand Total   3   2   5
Accuracy   60.00%
Recall / Sensitivity   50.00%
Specificity   66.67%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
b
Answers
Q4
i)   Discriminant Function = -4.824 + .023* Age (years) + .101 * Salary ($1000s)
CO-   + .004* Credit Score + .643* loan Type
ii)   Wilks lambda signifies discriminating power for the model. Lower the
1,2,   value(close to 0), better discrimination. Higher the value (close to 1 ) less
discriminating power of the model. In this case wilk’s lambda is .922 => close to
3;
1 hence the model has poor discriminating power.
BL-   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of   [1
Appl   variables. And lowest absolute values ( modulus since it is correlations) indicate
0]
lowest explanatory power of variables. In this case, Credit Score has highest
y,
(.718) and Age (.393) has lowest explanatory power.
Anal   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
yse,   Here the Box’s M is not significant (p value =.783 > 0.05) this suggests there is
Eval   no enough evidence to conclude that covariance matrices are significantly
different across two groups. So assumption of equal covariance matrices holds
uate   good
v)   Cross-validated accuracy is 57.0%.
Chance accuracy Calculations
********** 7 **********
--- page 8 ---
P()
44   29   73   0.365
57   70   127   0.635
0.5364
Chance Accuracy   5
Min Required   0.6705
Accuracy   63
this data has equal number of successes and failures. The chance accuracy for
the data is   p(S)2 + p(F)2 = 0.53645
We need atleast 25% improvement over chance accuracy i.e. 0.53645* 1.25 = 0.670563the
overall cross validated accuracy is not better than minimum required accuracy hence, the
model could not be used for prediction. Also the power of model is too low and there are some
non-significant variables in the model like loan type, Age you should not use the model for
prediction. You may use stepwise DA to improve results.
a
Marking scheme:
1. Why is logistic regression the appropriate technique for this problem? (01 Mark)
Logistic regression is used because the dependent variable (Employee Attrition: 1 =
Leaves, 0 = Stays) is binary.
It models the probability of an event occurring based on predictor variables (Age,
Salary, Years at Company, and Job Type).
2. Formulate the logistic regression equation based on the given predictors. (01 Mark)
The logistic regression model is:
e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
Q5   p ( x ) =
1 + e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
CO-
3. What does the pseudo R-square value indicate about the model’s performance? (02
1,2,   Marks)
The model explains 26.4% to 35.8% of the variance
3;   4. Which statistical tests are commonly used to assess model accuracy, and why? (02
BL-   Marks)
• Wald Test: p <0.05): significant model   [1
Appl   • Hosmer-Lemeshow Test (p > 0.05): significant model
5]
y,   5. How can the classification table help in evaluating the model’s effectiveness? (03
Mark)
Anal
yse,   False Positives (FP) = 16, meaning 16 employees who actually stayed were misclassified
as leaving.
Eval
False Negatives (FN) = 26, meaning 26 employees who actually left were misclassified
uate   as staying.
True Positives (TP) = 32, meaning 32 employees who left were correctly identified.
True Negatives (TN) = 76, meaning 76 employees who stayed were correctly identified.
Overall Accuracy = 72%, showing the model performs well but has limitations in
identifying employees who left.
6. Explain the concepts of Sensitivity and Specificity in relation to this model. (03 Marks)
Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
********** 8 **********
--- page 9 ---
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Sensitivity (55.2%): The model correctly identifies 55.2% of employees who left.
•   Specificity (82.6%): The model correctly identifies 82.6% of employees who
stayed.
7. Interpret the p-values of the predictors. Which variables are statistically significant?
(03 Marks)
• Age → Significant (p < 0.05), meaning age influences attrition.
•   Salary → significant (p < 0.05 meaning salary is a strong predictor.
•   Years at Company → Significant, p < 0.05 tenure strongly reduces attrition.
•   Job Type → p < 0.05 significant.
b Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as
Q5   an outlier.
Here, 4/(n-k-1) = 4/ (30-5-1) = 0.167
CO-;   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.167)   [5]
SO-;
BL-
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO-   d. What are characteristics of each group? (For 3 cluster solution)
1,2,   Cluster N   LuxuryTra   Adventu   LastMin   StayLuxur   Loyalt   GroupTrave
vel   re   ute   Budget   Flights   y   y   l
3;   1   9   4.89   4.89   5.33   8.22   4.44   7.44   8.00   7.33
BL-   2   8   6.75   4.75   4.25   5.25   2.13   7.00   7.13   7.75
3   13   7.69   8.00   8.08   5.85   6.23   3.92   4.69   4.00   [1
Appl   Total   30   6.60   6.20   6.23   6.40   4.60   5.80   6.33   6.00
5]
y,
Cluster 1: Low on LuxuryTravel, Adventure and Flights but High on Budget,
Anal
StayLuxury, Loyalty and GroupTravel
yse,   Cluster 2: Low/ Moderate on LuxuryTravel and Budget but High on StayLuxury,
Loyalty and GroupTravel
Eval   Cluster 3: High on LuxuryTravel, Adventure, LastMinute and Flights but low on
uate   budget, StayLuxury, Loyalty and GroupTravel
*Students may write for 2 cluster solution as well.
e. Which group is most profitable for the bank?
Cluster 3 is most profitable. (For 3 cluster solution)
• These customers prefer luxury travel and high-end experiences, meaning they
are willing to spend more on luxury accommodations, premium flight tickets,
and exclusive experiences.
********** 9 **********
--- page 10 ---
• Frequent and Spontaneous Travelers – High scores on LastMinute suggest that
they often book trips impulsively. Last-minute bookings usually come with
higher pricing and fewer discounts, increasing revenue for travel companies.
• Preference for Flights – Since these customers prioritize air travel over other
modes, they tend to book more expensive flight tickets, especially for
premium seating, business class, or direct flights.
• Adventure Enthusiasts Pay for Experiences – Travelers who score high on
Adventure often seek adventure sports, guided tours, and activity-based
packages, which are high-margin offerings for companies.
*Students may write for 2 cluster solution as well.
b Discuss the objectives of cluster analysis and its applications in business.
.
Synoptic Answer:
Q6   Clustering groups similar data points, useful in multiple business domains.
CO-
2,3;   Key Points:
BL-
1. Objective (1 mark) – Identify patterns, segment markets, detect anomalies.   [5]
Und   2. Clustering Methods (1 mark) – K-means, Hierarchical, DBSCAN.
erst   3. Applications (1 mark) – Customer segmentation, fraud detection,
recommender systems.
and   4. Example (1 mark) – E-commerce uses clustering for personalized
recommendations.
5. Business Impact (1 mark) – Enhances marketing strategies and operational
efficiency.
a Answers
Q7   Sales Revenue   3 moving
Month
($1000s)   Avg   error&2   Exp sm
CO-   Jan   200   180   400
Feb   220   194   676
1,2,
Mar   250   212.2   1428.84
3;   Apr   270   223.3333 2177.778   238.66   982.1956
BL-   May   290   246.6667 1877.778   260.598   864.4776
Jun   310   270   1600 281.1794   830.627   [1
Appl   Jul   330   290   1600 301.3538   820.6036
0]
y,   310   321.4061
Anal
yse,   Forecast
Eval   error   1813.889   857.5348
uate
Summary
Method   Forecast   MSE
3 moving   310   1813.889
********** 10 **********
--- page 11 ---
Expo sm alpha =
0.7   321.4061   857.5348
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph
below, the lags and are above zero as well as below zero indicating stationarity. There is no
need for difference for this data.
Q7
CO-
The model selection is done on the basis of following parameters
1,2,
1. Requirement of stationarity (in this case d = 0)
3;   2. BIC as low as possible
3. All lags (except intercept) need to be significant
BL-   4. Ljung-Box test should not be significant
[1
Appl   5. Residual ACF & PACF should be within the lines
0]
y,   Any simplest model that satisfies above parameters is the best model and can be used
for forecasting.
Anal   In above case
Sr   Model   BIC   Description   Result
yse,
No
Eval   1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, lag sig   Model
without   problem – Residual ACF & PACF not   cannot be
uate   removing   within range   used
outliers
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,. Residual   Model
without   ACF & PACF within range problem –   cannot be
removing   d=1, all lags not sig,   used
outliers
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag sig,   Model
without   Residual ACF & PACF within range   cannot be
removing   problem – d=1   used
outliers
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig,   Model
without   Residual ACF & PACF not within   cannot be
removing   range   used
outliers   problem – all lags not sig.
5   ARIMA(1,0,0)   9.456   All correct + minimum BIC + Simplest Model can
after removing   possible model   be used
outliers
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Forecast
Model   30   31   32   33   34   35
Ethereum Forecast   2076.11 2083.18 2089.84 2096.09 2101.97 2107.51
Price in US UCL   2231.33 2298.01 2347.04 2386.30 2419.02 2446.89
$-Model_1 LCL   1925.19 1876.50 1844.19 1820.47 1802.23 1787.82
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is
not too wide for initial forecasts. As the forecasting period extends, width becomes
wider making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Re-Exam · Sem 8 · Answer key · paper 28470e89fcfb

- Departments: Electronics and Telecommunication
- Programmes: MBATech (ELECTRONICS & TELECOMMUNICATIO
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/MBATech (ELECTRONICS & TELECOMMUNICATIO_ba3ceaa3/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Sem 8 Re-exam(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 02 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a How does data visualization enhance decision-making in business analytics?
.
Synoptic Answer:
Data visualization converts complex information into graphical formats for better
decision-making.
CO-   Key Points:
1;
BL-   1. Definition (1 mark) – Visual representation of data through graphs, charts,   [5]
Und   dashboards.
erst   2. Benefits (1 mark) – Identifies trends, outliers, and correlations.
and   3. Types (1 mark) – Bar charts, scatter plots, heat maps, dashboards.
4. Business Applications (1 mark) – Sales forecasting, customer segmentation,
fraud detection.
5. Example (1 mark) – A retail company uses dashboards to track regional sales
performance.
CO- b What are the essential steps in handling outliers in data pre-processing?
1;
.
BL-   Synoptic Answer:
Und   [5]
erst   Outliers can distort statistical models and must be handled carefully.
and,
appl   Key Points:
y
********** 1 **********
--- page 2 ---
1. Definition & Causes (1 mark) – Data errors, genuine variations, fraudulent
activities.
2. Detection Methods (1 mark) – Box plots, Z-score method, IQR rule.
3. Treatment Strategies (1 mark) – Winsorization, transformation (log/square
root), capping.
4. Removing Outliers (1 mark) – If justified, remove extreme values.
5. Example (1 mark) – In a salary dataset, a CEO’s salary may be an outlier
compared to employees.
c Explain the role of dummy variables in multiple regression analysis with an example.
.
Synoptic Answer:
Dummy variables convert categorical data into numerical format for regression
CO-
models.
1,2;
BL-
Key Points:
Und   [5]
erst
1. Definition (1 mark) – Used to include categorical data in regression models.
and,
2. Creation (1 mark) – Assign 0/1 to different categories.
appl
3. Example (1 mark) – Gender (Male = 1, Female = 0).
y
4. Regression Interpretation (1 mark) – Dummy variable coefficients show
category effects.
5. Business Application (1 mark) – Analyzing salary differences between
departments.
d Describe the concepts of sensitivity and specificity in the context of classification
models.
.
Synoptic Answer:
Sensitivity and specificity measure the performance of classification models.
CO-
2,3;
Key Points:
BL-
Und   1. Sensitivity (1 mark) – Measures true positive rate (correctly classified   [5]
erst
positive cases).
and,
2. Specificity (1 mark) – Measures true negative rate (correctly classified
appl
negative cases).
y
3. Trade-off (1 mark) – Higher sensitivity lowers specificity and vice versa.
4. Use Cases (1 mark) – Sensitivity in medical tests; specificity in fraud
detection.
5. Example (1 mark) – A cancer screening test prioritizes sensitivity to detect all
positive cases.
Q2
Answers   [2
CO-
1,2,   1. What type of model was applied, and why is it appropriate for this scenario?   0]
3;   The Multiple Linear Regression (MLR) model was applied because the resale price
BL-   (dependent variable) is continuous and influenced by multiple predictors:
********** 2 **********
--- page 3 ---
Appl   o Car Age
y,   o Mileage
Anal   o Engine Power
yse,   o Fuel Type (categorical)
Eval   • MLR is appropriate for predicting a continuous variable based on multiple factors.
uate
2. Which category serves as the reference for the qualitative variable (Fuel Type), and
why?
• The categorical variable is Fuel Type (Petrol = 1, Diesel = 0).
• The baseline/reference category is Diesel (coded as 0).
3. Write down the equation obtained from the analysis.
Resale Price=-
1.003−0.773(Car Age)−0.043(Mileage)+0.304(Engine Power)+1.380(Fuel Type)
4. Explain the significance of coefficient of Fuel Type in the model.
•   (Fuel Type - Petrol): Petrol cars are, on average, 1.380 more expensive than Diesel
cars.
5. Why does the intercept (b0) lack practical interpretation in this context?
• The intercept represents the resale price when all predictors are zero (0-year-old car,
0 mileage, 0 HP, Diesel).
•   This is not realistic as cars always have mileage, age, and power.
6. Can this equation be reliably used to estimate resale prices? Support your answer with
reasoning.
• The equation is reliable because:
o R² = 0.971, meaning the model explains 97.1% of the variation in resale
price.
o P-values for predictors are statistically significant (<0.05).
o Residuals are normally distributed, making the predictions valid.
7. Determine and interpret the coefficient of multiple determination (R²). How well does
the model explain variations in resale price?
• R² = 0.971, meaning 97.1% of the variance in resale price is explained by the model.
8. Which predictor has the most influence on resale price, and which has the least
impact? Explain your findings.
• Most influential predictor: Engine Power
•   Least influential predictor: Fuel Type – Petrol
9. What does the Variance Inflation Factor (VIF) reveal about multicollinearity among
the predictors?
• The VIF values are:
o Car Age: 1.063
o Mileage: 1.016
o Engine Power:1.025
o Fuel Type: 1.025
•   Since all VIF values are beow 5, multicollinearity is not a concern.
10. Analyze the P-P plot. Does it suggest that residuals follow a normal distribution?
•   Yes, the P-P plot follows a 45-degree straight line, meaning residuals are normally
distributed.
********** 3 **********
--- page 4 ---
11. Examine the residual histogram. Does the distribution appear normal, or are there
deviations?
• The histogram of residuals is bell-shaped, confirming normality.
•   There are no extreme outliers, meaning the model is well-behaved.
12. Evaluate the residual plot. Are there any noticeable patterns indicating problems with
the model?
• The residual plot shows no clear pattern, indicating homoscedasticity (constant
variance).
• The random scatter confirms that the model does not suffer from systematic bias.
13. Examine the ANOVA table: What does the significance (p-value) tell us about the
overall model fit?
• The F-statistic p-value (<0.05);ljm , meaning the model is statistically significant
14. Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals?
• Durbin-Watson (DW) = 2.041, which is close to 2, indicating no significant
autocorrelation in residuals.
15. Predict the resale price for a car with these features:
• Car Age = 5 years
• Mileage = 60,000 miles
• Engine Power = 150 HP
•   Fuel Type = Petrol (1)
Using the regression equation:
31.802
a
Synoptic
a) this is three factor solution.
Rotated Factor Matrixa
Q3
Factor
CO-
1   2   3
1,2,
3;   [Price]   0.043   0.992   0.026
BL-   [2
Appl   [Quantity]   0.062   0.921   0.019
y   0]
[Product Variety]   0.986   0.024   0.097
Eval
uate   [Advertisements]   0.131   0.028   0.966
,
crea   [Health Concern ( Sugar free, fat free etc)]   0.985   0.04   0.129
te
[Presentation of Ice Cream]   0.137   0.024   0.967
[Value for money]   -0.016   0.954   0.02
********** 4 **********
--- page 5 ---
[Product Ingredients]   0.959   0.029   0.121
Extraction Method: Principal Axis Factoring.
Rotation Method: Varimax with Kaiser Normalization.
Note to evaluators : Factor names are subjective student may name them in multiple ways
Factor 1 (Healthy   Factor 3 (in-
Choices)   Factor 2 (Tangible)   Tangible)
[Product Variety]   [Price]   [Advertisements]
[Health Concern ( Sugar   [Presentation of
[Quantity]
free, fat free etc)]   Ice Cream]
[Product Ingredients]   [Value for money]
b) there is no variable that should not be there in the factor analysis as all variables
have anti-aging correlations >0.5, extraction communality >0.5, and non of them
have any cross loading.
c) Scree plot indicates 3 factors as good solution however 3 factors have steep slopes
4th factor slope is not so steep
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5,
total explained variance > 60% all variables have communality >0.5, and there is no
cross loading indicates a good solution. Yes factor analysis is relevant in this case
and this solution can be used
e) Factor 1 (Healthy Choices) is the most important factor As it has highest
communality.
F. Difference Between PCA & Common Factor Analysis
Principal Component   Common Factor
Feature
Analysis (PCA)   Analysis (CFA)
Data reduction and   Identifying latent factors
Purpose   transformation to   that explain the observed
uncorrelated components.   variables.
Explanatory, used to
Descriptive, used to
Type of Analysis   uncover hidden
summarize variance in data.
constructs.
Focuses only on shared
Mathematical   Maximizes total variance in
(common) variance
Basis   the data.
among variables.
Components are extracted   Factors are extracted to
Factor
to explain the maximum   explain correlations
Extraction
variance.   between variables.
Correlation   Does not assume any   Assumes an underlying
Assumption   underlying factor structure. structure where observed
********** 5 **********
--- page 6 ---
variables load onto latent
factors.
Data compression,   Psychological, social, and
Use Cases   dimensionality reduction,   economic research to
visualization.   study latent traits.
Factors represent
Components are
underlying traits or
mathematical constructs
Interpretability   constructs that explain
and may not have direct
relationships among
interpretability.
variables.
a Answer:
5NN
Standa
Standar   Standar
rdised
dised   dised   Standardis
Distan   Standardised
Distance Distance ed Distance
ce of   of 2nd   of 3rd   of 4th   Distance of
1st   5th
observation
observat observat   observation
observ
ion   ion
Visit Supermarket   ation
N   4   1   5   4   1
Q4   Y   1   6   6   7   4
N   7   5   3   2   7
CO-
Y   2   2   4   1   3
1,2,   N   5   7   7   3   6
3;   Y   6   3   2   6   5
N   3   4   1   5   2
BL-
[1
Appl   Rank
1 Y   N   N   Y   N   0]
y,
2 Y   Y   Y   N   N
Anal   3 N   Y   N   N   Y
4 N   N   Y   N   Y
yse,
5 N   N   N   N   Y
Eval
uate   Prediction   N   N   N   N   Y
Actual   Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   3   3
Y   1   1   2
Grand Total   4   1   5
********** 6 **********
--- page 7 ---
Accuracy   80.00%
Recall / Sensitivity   50.00%
100.00
Specificity   %
100.00
Precision   %
3NN
Rank
1 Y   N   N   Y   N
2 Y   Y   Y   N   N
3 N   Y   N   N   Y
Prediction Y   Y   N   N   N
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   1   1   2
Grand Total   3   2   5
Accuracy   60.00%
Recall / Sensitivity   50.00%
Specificity   66.67%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
b
Answers
Q4
i)   Discriminant Function = -4.824 + .023* Age (years) + .101 * Salary ($1000s)
CO-   + .004* Credit Score + .643* loan Type
ii)   Wilks lambda signifies discriminating power for the model. Lower the
1,2,   value(close to 0), better discrimination. Higher the value (close to 1 ) less
discriminating power of the model. In this case wilk’s lambda is .922 => close to
3;
1 hence the model has poor discriminating power.
BL-   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of   [1
Appl   variables. And lowest absolute values ( modulus since it is correlations) indicate
0]
lowest explanatory power of variables. In this case, Credit Score has highest
y,
(.718) and Age (.393) has lowest explanatory power.
Anal   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
yse,   Here the Box’s M is not significant (p value =.783 > 0.05) this suggests there is
Eval   no enough evidence to conclude that covariance matrices are significantly
different across two groups. So assumption of equal covariance matrices holds
uate   good
v)   Cross-validated accuracy is 57.0%.
Chance accuracy Calculations
********** 7 **********
--- page 8 ---
P()
44   29   73   0.365
57   70   127   0.635
0.5364
Chance Accuracy   5
Min Required   0.6705
Accuracy   63
this data has equal number of successes and failures. The chance accuracy for
the data is   p(S)2 + p(F)2 = 0.53645
We need atleast 25% improvement over chance accuracy i.e. 0.53645* 1.25 = 0.670563the
overall cross validated accuracy is not better than minimum required accuracy hence, the
model could not be used for prediction. Also the power of model is too low and there are some
non-significant variables in the model like loan type, Age you should not use the model for
prediction. You may use stepwise DA to improve results.
a
Marking scheme:
1. Why is logistic regression the appropriate technique for this problem? (01 Mark)
Logistic regression is used because the dependent variable (Employee Attrition: 1 =
Leaves, 0 = Stays) is binary.
It models the probability of an event occurring based on predictor variables (Age,
Salary, Years at Company, and Job Type).
2. Formulate the logistic regression equation based on the given predictors. (01 Mark)
The logistic regression model is:
e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
Q5   p ( x ) =
1 + e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
CO-
3. What does the pseudo R-square value indicate about the model’s performance? (02
1,2,   Marks)
The model explains 26.4% to 35.8% of the variance
3;   4. Which statistical tests are commonly used to assess model accuracy, and why? (02
BL-   Marks)
• Wald Test: p <0.05): significant model   [1
Appl   • Hosmer-Lemeshow Test (p > 0.05): significant model
5]
y,   5. How can the classification table help in evaluating the model’s effectiveness? (03
Mark)
Anal
yse,   False Positives (FP) = 16, meaning 16 employees who actually stayed were misclassified
as leaving.
Eval
False Negatives (FN) = 26, meaning 26 employees who actually left were misclassified
uate   as staying.
True Positives (TP) = 32, meaning 32 employees who left were correctly identified.
True Negatives (TN) = 76, meaning 76 employees who stayed were correctly identified.
Overall Accuracy = 72%, showing the model performs well but has limitations in
identifying employees who left.
6. Explain the concepts of Sensitivity and Specificity in relation to this model. (03 Marks)
Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
********** 8 **********
--- page 9 ---
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Sensitivity (55.2%): The model correctly identifies 55.2% of employees who left.
•   Specificity (82.6%): The model correctly identifies 82.6% of employees who
stayed.
7. Interpret the p-values of the predictors. Which variables are statistically significant?
(03 Marks)
• Age → Significant (p < 0.05), meaning age influences attrition.
•   Salary → significant (p < 0.05 meaning salary is a strong predictor.
•   Years at Company → Significant, p < 0.05 tenure strongly reduces attrition.
•   Job Type → p < 0.05 significant.
b Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as
Q5   an outlier.
Here, 4/(n-k-1) = 4/ (30-5-1) = 0.167
CO-;   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.167)   [5]
SO-;
BL-
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO-   d. What are characteristics of each group? (For 3 cluster solution)
1,2,   Cluster N   LuxuryTra   Adventu   LastMin   StayLuxur   Loyalt   GroupTrave
vel   re   ute   Budget   Flights   y   y   l
3;   1   9   4.89   4.89   5.33   8.22   4.44   7.44   8.00   7.33
BL-   2   8   6.75   4.75   4.25   5.25   2.13   7.00   7.13   7.75
3   13   7.69   8.00   8.08   5.85   6.23   3.92   4.69   4.00   [1
Appl   Total   30   6.60   6.20   6.23   6.40   4.60   5.80   6.33   6.00
5]
y,
Cluster 1: Low on LuxuryTravel, Adventure and Flights but High on Budget,
Anal
StayLuxury, Loyalty and GroupTravel
yse,   Cluster 2: Low/ Moderate on LuxuryTravel and Budget but High on StayLuxury,
Loyalty and GroupTravel
Eval   Cluster 3: High on LuxuryTravel, Adventure, LastMinute and Flights but low on
uate   budget, StayLuxury, Loyalty and GroupTravel
*Students may write for 2 cluster solution as well.
e. Which group is most profitable for the bank?
Cluster 3 is most profitable. (For 3 cluster solution)
• These customers prefer luxury travel and high-end experiences, meaning they
are willing to spend more on luxury accommodations, premium flight tickets,
and exclusive experiences.
********** 9 **********
--- page 10 ---
• Frequent and Spontaneous Travelers – High scores on LastMinute suggest that
they often book trips impulsively. Last-minute bookings usually come with
higher pricing and fewer discounts, increasing revenue for travel companies.
• Preference for Flights – Since these customers prioritize air travel over other
modes, they tend to book more expensive flight tickets, especially for
premium seating, business class, or direct flights.
• Adventure Enthusiasts Pay for Experiences – Travelers who score high on
Adventure often seek adventure sports, guided tours, and activity-based
packages, which are high-margin offerings for companies.
*Students may write for 2 cluster solution as well.
b Discuss the objectives of cluster analysis and its applications in business.
.
Synoptic Answer:
Q6   Clustering groups similar data points, useful in multiple business domains.
CO-
2,3;   Key Points:
BL-
1. Objective (1 mark) – Identify patterns, segment markets, detect anomalies.   [5]
Und   2. Clustering Methods (1 mark) – K-means, Hierarchical, DBSCAN.
erst   3. Applications (1 mark) – Customer segmentation, fraud detection,
recommender systems.
and   4. Example (1 mark) – E-commerce uses clustering for personalized
recommendations.
5. Business Impact (1 mark) – Enhances marketing strategies and operational
efficiency.
a Answers
Q7   Sales Revenue   3 moving
Month
($1000s)   Avg   error&2   Exp sm
CO-   Jan   200   180   400
Feb   220   194   676
1,2,
Mar   250   212.2   1428.84
3;   Apr   270   223.3333 2177.778   238.66   982.1956
BL-   May   290   246.6667 1877.778   260.598   864.4776
Jun   310   270   1600 281.1794   830.627   [1
Appl   Jul   330   290   1600 301.3538   820.6036
0]
y,   310   321.4061
Anal
yse,   Forecast
Eval   error   1813.889   857.5348
uate
Summary
Method   Forecast   MSE
3 moving   310   1813.889
********** 10 **********
--- page 11 ---
Expo sm alpha =
0.7   321.4061   857.5348
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph
below, the lags and are above zero as well as below zero indicating stationarity. There is no
need for difference for this data.
Q7
CO-
The model selection is done on the basis of following parameters
1,2,
1. Requirement of stationarity (in this case d = 0)
3;   2. BIC as low as possible
3. All lags (except intercept) need to be significant
BL-   4. Ljung-Box test should not be significant
[1
Appl   5. Residual ACF & PACF should be within the lines
0]
y,   Any simplest model that satisfies above parameters is the best model and can be used
for forecasting.
Anal   In above case
Sr   Model   BIC   Description   Result
yse,
No
Eval   1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, lag sig   Model
without   problem – Residual ACF & PACF not   cannot be
uate   removing   within range   used
outliers
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,. Residual   Model
without   ACF & PACF within range problem –   cannot be
removing   d=1, all lags not sig,   used
outliers
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag sig,   Model
without   Residual ACF & PACF within range   cannot be
removing   problem – d=1   used
outliers
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig,   Model
without   Residual ACF & PACF not within   cannot be
removing   range   used
outliers   problem – all lags not sig.
5   ARIMA(1,0,0)   9.456   All correct + minimum BIC + Simplest Model can
after removing   possible model   be used
outliers
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Forecast
Model   30   31   32   33   34   35
Ethereum Forecast   2076.11 2083.18 2089.84 2096.09 2101.97 2107.51
Price in US UCL   2231.33 2298.01 2347.04 2386.30 2419.02 2446.89
$-Model_1 LCL   1925.19 1876.50 1844.19 1820.47 1802.23 1787.82
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is
not too wide for initial forecasts. As the forecasting period extends, width becomes
wider making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Re-Exam · Sem 8 · Answer key · paper 07021b33b8f9

- Departments: Mechanical
- Programmes: MBATech (MECHANICAL ENGINEERING) - 7046
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/MBATech (MECHANICAL ENGINEERING) - 7046/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Sem 8 Re-exam(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 02 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a How does data visualization enhance decision-making in business analytics?
.
Synoptic Answer:
Data visualization converts complex information into graphical formats for better
decision-making.
CO-   Key Points:
1;
BL-   1. Definition (1 mark) – Visual representation of data through graphs, charts,   [5]
Und   dashboards.
erst   2. Benefits (1 mark) – Identifies trends, outliers, and correlations.
and   3. Types (1 mark) – Bar charts, scatter plots, heat maps, dashboards.
4. Business Applications (1 mark) – Sales forecasting, customer segmentation,
fraud detection.
5. Example (1 mark) – A retail company uses dashboards to track regional sales
performance.
CO- b What are the essential steps in handling outliers in data pre-processing?
1;
.
BL-   Synoptic Answer:
Und   [5]
erst   Outliers can distort statistical models and must be handled carefully.
and,
appl   Key Points:
y
********** 1 **********
--- page 2 ---
1. Definition & Causes (1 mark) – Data errors, genuine variations, fraudulent
activities.
2. Detection Methods (1 mark) – Box plots, Z-score method, IQR rule.
3. Treatment Strategies (1 mark) – Winsorization, transformation (log/square
root), capping.
4. Removing Outliers (1 mark) – If justified, remove extreme values.
5. Example (1 mark) – In a salary dataset, a CEO’s salary may be an outlier
compared to employees.
c Explain the role of dummy variables in multiple regression analysis with an example.
.
Synoptic Answer:
Dummy variables convert categorical data into numerical format for regression
CO-
models.
1,2;
BL-
Key Points:
Und   [5]
erst
1. Definition (1 mark) – Used to include categorical data in regression models.
and,
2. Creation (1 mark) – Assign 0/1 to different categories.
appl
3. Example (1 mark) – Gender (Male = 1, Female = 0).
y
4. Regression Interpretation (1 mark) – Dummy variable coefficients show
category effects.
5. Business Application (1 mark) – Analyzing salary differences between
departments.
d Describe the concepts of sensitivity and specificity in the context of classification
models.
.
Synoptic Answer:
Sensitivity and specificity measure the performance of classification models.
CO-
2,3;
Key Points:
BL-
Und   1. Sensitivity (1 mark) – Measures true positive rate (correctly classified   [5]
erst
positive cases).
and,
2. Specificity (1 mark) – Measures true negative rate (correctly classified
appl
negative cases).
y
3. Trade-off (1 mark) – Higher sensitivity lowers specificity and vice versa.
4. Use Cases (1 mark) – Sensitivity in medical tests; specificity in fraud
detection.
5. Example (1 mark) – A cancer screening test prioritizes sensitivity to detect all
positive cases.
Q2
Answers   [2
CO-
1,2,   1. What type of model was applied, and why is it appropriate for this scenario?   0]
3;   The Multiple Linear Regression (MLR) model was applied because the resale price
BL-   (dependent variable) is continuous and influenced by multiple predictors:
********** 2 **********
--- page 3 ---
Appl   o Car Age
y,   o Mileage
Anal   o Engine Power
yse,   o Fuel Type (categorical)
Eval   • MLR is appropriate for predicting a continuous variable based on multiple factors.
uate
2. Which category serves as the reference for the qualitative variable (Fuel Type), and
why?
• The categorical variable is Fuel Type (Petrol = 1, Diesel = 0).
• The baseline/reference category is Diesel (coded as 0).
3. Write down the equation obtained from the analysis.
Resale Price=-
1.003−0.773(Car Age)−0.043(Mileage)+0.304(Engine Power)+1.380(Fuel Type)
4. Explain the significance of coefficient of Fuel Type in the model.
•   (Fuel Type - Petrol): Petrol cars are, on average, 1.380 more expensive than Diesel
cars.
5. Why does the intercept (b0) lack practical interpretation in this context?
• The intercept represents the resale price when all predictors are zero (0-year-old car,
0 mileage, 0 HP, Diesel).
•   This is not realistic as cars always have mileage, age, and power.
6. Can this equation be reliably used to estimate resale prices? Support your answer with
reasoning.
• The equation is reliable because:
o R² = 0.971, meaning the model explains 97.1% of the variation in resale
price.
o P-values for predictors are statistically significant (<0.05).
o Residuals are normally distributed, making the predictions valid.
7. Determine and interpret the coefficient of multiple determination (R²). How well does
the model explain variations in resale price?
• R² = 0.971, meaning 97.1% of the variance in resale price is explained by the model.
8. Which predictor has the most influence on resale price, and which has the least
impact? Explain your findings.
• Most influential predictor: Engine Power
•   Least influential predictor: Fuel Type – Petrol
9. What does the Variance Inflation Factor (VIF) reveal about multicollinearity among
the predictors?
• The VIF values are:
o Car Age: 1.063
o Mileage: 1.016
o Engine Power:1.025
o Fuel Type: 1.025
•   Since all VIF values are beow 5, multicollinearity is not a concern.
10. Analyze the P-P plot. Does it suggest that residuals follow a normal distribution?
•   Yes, the P-P plot follows a 45-degree straight line, meaning residuals are normally
distributed.
********** 3 **********
--- page 4 ---
11. Examine the residual histogram. Does the distribution appear normal, or are there
deviations?
• The histogram of residuals is bell-shaped, confirming normality.
•   There are no extreme outliers, meaning the model is well-behaved.
12. Evaluate the residual plot. Are there any noticeable patterns indicating problems with
the model?
• The residual plot shows no clear pattern, indicating homoscedasticity (constant
variance).
• The random scatter confirms that the model does not suffer from systematic bias.
13. Examine the ANOVA table: What does the significance (p-value) tell us about the
overall model fit?
• The F-statistic p-value (<0.05);ljm , meaning the model is statistically significant
14. Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals?
• Durbin-Watson (DW) = 2.041, which is close to 2, indicating no significant
autocorrelation in residuals.
15. Predict the resale price for a car with these features:
• Car Age = 5 years
• Mileage = 60,000 miles
• Engine Power = 150 HP
•   Fuel Type = Petrol (1)
Using the regression equation:
31.802
a
Synoptic
a) this is three factor solution.
Rotated Factor Matrixa
Q3
Factor
CO-
1   2   3
1,2,
3;   [Price]   0.043   0.992   0.026
BL-   [2
Appl   [Quantity]   0.062   0.921   0.019
y   0]
[Product Variety]   0.986   0.024   0.097
Eval
uate   [Advertisements]   0.131   0.028   0.966
,
crea   [Health Concern ( Sugar free, fat free etc)]   0.985   0.04   0.129
te
[Presentation of Ice Cream]   0.137   0.024   0.967
[Value for money]   -0.016   0.954   0.02
********** 4 **********
--- page 5 ---
[Product Ingredients]   0.959   0.029   0.121
Extraction Method: Principal Axis Factoring.
Rotation Method: Varimax with Kaiser Normalization.
Note to evaluators : Factor names are subjective student may name them in multiple ways
Factor 1 (Healthy   Factor 3 (in-
Choices)   Factor 2 (Tangible)   Tangible)
[Product Variety]   [Price]   [Advertisements]
[Health Concern ( Sugar   [Presentation of
[Quantity]
free, fat free etc)]   Ice Cream]
[Product Ingredients]   [Value for money]
b) there is no variable that should not be there in the factor analysis as all variables
have anti-aging correlations >0.5, extraction communality >0.5, and non of them
have any cross loading.
c) Scree plot indicates 3 factors as good solution however 3 factors have steep slopes
4th factor slope is not so steep
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5,
total explained variance > 60% all variables have communality >0.5, and there is no
cross loading indicates a good solution. Yes factor analysis is relevant in this case
and this solution can be used
e) Factor 1 (Healthy Choices) is the most important factor As it has highest
communality.
F. Difference Between PCA & Common Factor Analysis
Principal Component   Common Factor
Feature
Analysis (PCA)   Analysis (CFA)
Data reduction and   Identifying latent factors
Purpose   transformation to   that explain the observed
uncorrelated components.   variables.
Explanatory, used to
Descriptive, used to
Type of Analysis   uncover hidden
summarize variance in data.
constructs.
Focuses only on shared
Mathematical   Maximizes total variance in
(common) variance
Basis   the data.
among variables.
Components are extracted   Factors are extracted to
Factor
to explain the maximum   explain correlations
Extraction
variance.   between variables.
Correlation   Does not assume any   Assumes an underlying
Assumption   underlying factor structure. structure where observed
********** 5 **********
--- page 6 ---
variables load onto latent
factors.
Data compression,   Psychological, social, and
Use Cases   dimensionality reduction,   economic research to
visualization.   study latent traits.
Factors represent
Components are
underlying traits or
mathematical constructs
Interpretability   constructs that explain
and may not have direct
relationships among
interpretability.
variables.
a Answer:
5NN
Standa
Standar   Standar
rdised
dised   dised   Standardis
Distan   Standardised
Distance Distance ed Distance
ce of   of 2nd   of 3rd   of 4th   Distance of
1st   5th
observation
observat observat   observation
observ
ion   ion
Visit Supermarket   ation
N   4   1   5   4   1
Q4   Y   1   6   6   7   4
N   7   5   3   2   7
CO-
Y   2   2   4   1   3
1,2,   N   5   7   7   3   6
3;   Y   6   3   2   6   5
N   3   4   1   5   2
BL-
[1
Appl   Rank
1 Y   N   N   Y   N   0]
y,
2 Y   Y   Y   N   N
Anal   3 N   Y   N   N   Y
4 N   N   Y   N   Y
yse,
5 N   N   N   N   Y
Eval
uate   Prediction   N   N   N   N   Y
Actual   Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   3   3
Y   1   1   2
Grand Total   4   1   5
********** 6 **********
--- page 7 ---
Accuracy   80.00%
Recall / Sensitivity   50.00%
100.00
Specificity   %
100.00
Precision   %
3NN
Rank
1 Y   N   N   Y   N
2 Y   Y   Y   N   N
3 N   Y   N   N   Y
Prediction Y   Y   N   N   N
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   1   1   2
Grand Total   3   2   5
Accuracy   60.00%
Recall / Sensitivity   50.00%
Specificity   66.67%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
b
Answers
Q4
i)   Discriminant Function = -4.824 + .023* Age (years) + .101 * Salary ($1000s)
CO-   + .004* Credit Score + .643* loan Type
ii)   Wilks lambda signifies discriminating power for the model. Lower the
1,2,   value(close to 0), better discrimination. Higher the value (close to 1 ) less
discriminating power of the model. In this case wilk’s lambda is .922 => close to
3;
1 hence the model has poor discriminating power.
BL-   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of   [1
Appl   variables. And lowest absolute values ( modulus since it is correlations) indicate
0]
lowest explanatory power of variables. In this case, Credit Score has highest
y,
(.718) and Age (.393) has lowest explanatory power.
Anal   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
yse,   Here the Box’s M is not significant (p value =.783 > 0.05) this suggests there is
Eval   no enough evidence to conclude that covariance matrices are significantly
different across two groups. So assumption of equal covariance matrices holds
uate   good
v)   Cross-validated accuracy is 57.0%.
Chance accuracy Calculations
********** 7 **********
--- page 8 ---
P()
44   29   73   0.365
57   70   127   0.635
0.5364
Chance Accuracy   5
Min Required   0.6705
Accuracy   63
this data has equal number of successes and failures. The chance accuracy for
the data is   p(S)2 + p(F)2 = 0.53645
We need atleast 25% improvement over chance accuracy i.e. 0.53645* 1.25 = 0.670563the
overall cross validated accuracy is not better than minimum required accuracy hence, the
model could not be used for prediction. Also the power of model is too low and there are some
non-significant variables in the model like loan type, Age you should not use the model for
prediction. You may use stepwise DA to improve results.
a
Marking scheme:
1. Why is logistic regression the appropriate technique for this problem? (01 Mark)
Logistic regression is used because the dependent variable (Employee Attrition: 1 =
Leaves, 0 = Stays) is binary.
It models the probability of an event occurring based on predictor variables (Age,
Salary, Years at Company, and Job Type).
2. Formulate the logistic regression equation based on the given predictors. (01 Mark)
The logistic regression model is:
e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
Q5   p ( x ) =
1 + e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
CO-
3. What does the pseudo R-square value indicate about the model’s performance? (02
1,2,   Marks)
The model explains 26.4% to 35.8% of the variance
3;   4. Which statistical tests are commonly used to assess model accuracy, and why? (02
BL-   Marks)
• Wald Test: p <0.05): significant model   [1
Appl   • Hosmer-Lemeshow Test (p > 0.05): significant model
5]
y,   5. How can the classification table help in evaluating the model’s effectiveness? (03
Mark)
Anal
yse,   False Positives (FP) = 16, meaning 16 employees who actually stayed were misclassified
as leaving.
Eval
False Negatives (FN) = 26, meaning 26 employees who actually left were misclassified
uate   as staying.
True Positives (TP) = 32, meaning 32 employees who left were correctly identified.
True Negatives (TN) = 76, meaning 76 employees who stayed were correctly identified.
Overall Accuracy = 72%, showing the model performs well but has limitations in
identifying employees who left.
6. Explain the concepts of Sensitivity and Specificity in relation to this model. (03 Marks)
Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
********** 8 **********
--- page 9 ---
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Sensitivity (55.2%): The model correctly identifies 55.2% of employees who left.
•   Specificity (82.6%): The model correctly identifies 82.6% of employees who
stayed.
7. Interpret the p-values of the predictors. Which variables are statistically significant?
(03 Marks)
• Age → Significant (p < 0.05), meaning age influences attrition.
•   Salary → significant (p < 0.05 meaning salary is a strong predictor.
•   Years at Company → Significant, p < 0.05 tenure strongly reduces attrition.
•   Job Type → p < 0.05 significant.
b Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as
Q5   an outlier.
Here, 4/(n-k-1) = 4/ (30-5-1) = 0.167
CO-;   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.167)   [5]
SO-;
BL-
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO-   d. What are characteristics of each group? (For 3 cluster solution)
1,2,   Cluster N   LuxuryTra   Adventu   LastMin   StayLuxur   Loyalt   GroupTrave
vel   re   ute   Budget   Flights   y   y   l
3;   1   9   4.89   4.89   5.33   8.22   4.44   7.44   8.00   7.33
BL-   2   8   6.75   4.75   4.25   5.25   2.13   7.00   7.13   7.75
3   13   7.69   8.00   8.08   5.85   6.23   3.92   4.69   4.00   [1
Appl   Total   30   6.60   6.20   6.23   6.40   4.60   5.80   6.33   6.00
5]
y,
Cluster 1: Low on LuxuryTravel, Adventure and Flights but High on Budget,
Anal
StayLuxury, Loyalty and GroupTravel
yse,   Cluster 2: Low/ Moderate on LuxuryTravel and Budget but High on StayLuxury,
Loyalty and GroupTravel
Eval   Cluster 3: High on LuxuryTravel, Adventure, LastMinute and Flights but low on
uate   budget, StayLuxury, Loyalty and GroupTravel
*Students may write for 2 cluster solution as well.
e. Which group is most profitable for the bank?
Cluster 3 is most profitable. (For 3 cluster solution)
• These customers prefer luxury travel and high-end experiences, meaning they
are willing to spend more on luxury accommodations, premium flight tickets,
and exclusive experiences.
********** 9 **********
--- page 10 ---
• Frequent and Spontaneous Travelers – High scores on LastMinute suggest that
they often book trips impulsively. Last-minute bookings usually come with
higher pricing and fewer discounts, increasing revenue for travel companies.
• Preference for Flights – Since these customers prioritize air travel over other
modes, they tend to book more expensive flight tickets, especially for
premium seating, business class, or direct flights.
• Adventure Enthusiasts Pay for Experiences – Travelers who score high on
Adventure often seek adventure sports, guided tours, and activity-based
packages, which are high-margin offerings for companies.
*Students may write for 2 cluster solution as well.
b Discuss the objectives of cluster analysis and its applications in business.
.
Synoptic Answer:
Q6   Clustering groups similar data points, useful in multiple business domains.
CO-
2,3;   Key Points:
BL-
1. Objective (1 mark) – Identify patterns, segment markets, detect anomalies.   [5]
Und   2. Clustering Methods (1 mark) – K-means, Hierarchical, DBSCAN.
erst   3. Applications (1 mark) – Customer segmentation, fraud detection,
recommender systems.
and   4. Example (1 mark) – E-commerce uses clustering for personalized
recommendations.
5. Business Impact (1 mark) – Enhances marketing strategies and operational
efficiency.
a Answers
Q7   Sales Revenue   3 moving
Month
($1000s)   Avg   error&2   Exp sm
CO-   Jan   200   180   400
Feb   220   194   676
1,2,
Mar   250   212.2   1428.84
3;   Apr   270   223.3333 2177.778   238.66   982.1956
BL-   May   290   246.6667 1877.778   260.598   864.4776
Jun   310   270   1600 281.1794   830.627   [1
Appl   Jul   330   290   1600 301.3538   820.6036
0]
y,   310   321.4061
Anal
yse,   Forecast
Eval   error   1813.889   857.5348
uate
Summary
Method   Forecast   MSE
3 moving   310   1813.889
********** 10 **********
--- page 11 ---
Expo sm alpha =
0.7   321.4061   857.5348
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph
below, the lags and are above zero as well as below zero indicating stationarity. There is no
need for difference for this data.
Q7
CO-
The model selection is done on the basis of following parameters
1,2,
1. Requirement of stationarity (in this case d = 0)
3;   2. BIC as low as possible
3. All lags (except intercept) need to be significant
BL-   4. Ljung-Box test should not be significant
[1
Appl   5. Residual ACF & PACF should be within the lines
0]
y,   Any simplest model that satisfies above parameters is the best model and can be used
for forecasting.
Anal   In above case
Sr   Model   BIC   Description   Result
yse,
No
Eval   1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, lag sig   Model
without   problem – Residual ACF & PACF not   cannot be
uate   removing   within range   used
outliers
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,. Residual   Model
without   ACF & PACF within range problem –   cannot be
removing   d=1, all lags not sig,   used
outliers
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag sig,   Model
without   Residual ACF & PACF within range   cannot be
removing   problem – d=1   used
outliers
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig,   Model
without   Residual ACF & PACF not within   cannot be
removing   range   used
outliers   problem – all lags not sig.
5   ARIMA(1,0,0)   9.456   All correct + minimum BIC + Simplest Model can
after removing   possible model   be used
outliers
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Forecast
Model   30   31   32   33   34   35
Ethereum Forecast   2076.11 2083.18 2089.84 2096.09 2101.97 2107.51
Price in US UCL   2231.33 2298.01 2347.04 2386.30 2419.02 2446.89
$-Model_1 LCL   1925.19 1876.50 1844.19 1820.47 1802.23 1787.82
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is
not too wide for initial forecasts. As the forecasting period extends, width becomes
wider making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Re-Exam · Sem 8 · Answer key · paper cd44c72500a2

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/MBATech_AI_7051/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Sem 8 Re-exam(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 02 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a How does data visualization enhance decision-making in business analytics?
.
Synoptic Answer:
Data visualization converts complex information into graphical formats for better
decision-making.
CO-   Key Points:
1;
BL-   1. Definition (1 mark) – Visual representation of data through graphs, charts,   [5]
Und   dashboards.
erst   2. Benefits (1 mark) – Identifies trends, outliers, and correlations.
and   3. Types (1 mark) – Bar charts, scatter plots, heat maps, dashboards.
4. Business Applications (1 mark) – Sales forecasting, customer segmentation,
fraud detection.
5. Example (1 mark) – A retail company uses dashboards to track regional sales
performance.
CO- b What are the essential steps in handling outliers in data pre-processing?
1;
.
BL-   Synoptic Answer:
Und   [5]
erst   Outliers can distort statistical models and must be handled carefully.
and,
appl   Key Points:
y
********** 1 **********
--- page 2 ---
1. Definition & Causes (1 mark) – Data errors, genuine variations, fraudulent
activities.
2. Detection Methods (1 mark) – Box plots, Z-score method, IQR rule.
3. Treatment Strategies (1 mark) – Winsorization, transformation (log/square
root), capping.
4. Removing Outliers (1 mark) – If justified, remove extreme values.
5. Example (1 mark) – In a salary dataset, a CEO’s salary may be an outlier
compared to employees.
c Explain the role of dummy variables in multiple regression analysis with an example.
.
Synoptic Answer:
Dummy variables convert categorical data into numerical format for regression
CO-
models.
1,2;
BL-
Key Points:
Und   [5]
erst
1. Definition (1 mark) – Used to include categorical data in regression models.
and,
2. Creation (1 mark) – Assign 0/1 to different categories.
appl
3. Example (1 mark) – Gender (Male = 1, Female = 0).
y
4. Regression Interpretation (1 mark) – Dummy variable coefficients show
category effects.
5. Business Application (1 mark) – Analyzing salary differences between
departments.
d Describe the concepts of sensitivity and specificity in the context of classification
models.
.
Synoptic Answer:
Sensitivity and specificity measure the performance of classification models.
CO-
2,3;
Key Points:
BL-
Und   1. Sensitivity (1 mark) – Measures true positive rate (correctly classified   [5]
erst
positive cases).
and,
2. Specificity (1 mark) – Measures true negative rate (correctly classified
appl
negative cases).
y
3. Trade-off (1 mark) – Higher sensitivity lowers specificity and vice versa.
4. Use Cases (1 mark) – Sensitivity in medical tests; specificity in fraud
detection.
5. Example (1 mark) – A cancer screening test prioritizes sensitivity to detect all
positive cases.
Q2
Answers   [2
CO-
1,2,   1. What type of model was applied, and why is it appropriate for this scenario?   0]
3;   The Multiple Linear Regression (MLR) model was applied because the resale price
BL-   (dependent variable) is continuous and influenced by multiple predictors:
********** 2 **********
--- page 3 ---
Appl   o Car Age
y,   o Mileage
Anal   o Engine Power
yse,   o Fuel Type (categorical)
Eval   • MLR is appropriate for predicting a continuous variable based on multiple factors.
uate
2. Which category serves as the reference for the qualitative variable (Fuel Type), and
why?
• The categorical variable is Fuel Type (Petrol = 1, Diesel = 0).
• The baseline/reference category is Diesel (coded as 0).
3. Write down the equation obtained from the analysis.
Resale Price=-
1.003−0.773(Car Age)−0.043(Mileage)+0.304(Engine Power)+1.380(Fuel Type)
4. Explain the significance of coefficient of Fuel Type in the model.
•   (Fuel Type - Petrol): Petrol cars are, on average, 1.380 more expensive than Diesel
cars.
5. Why does the intercept (b0) lack practical interpretation in this context?
• The intercept represents the resale price when all predictors are zero (0-year-old car,
0 mileage, 0 HP, Diesel).
•   This is not realistic as cars always have mileage, age, and power.
6. Can this equation be reliably used to estimate resale prices? Support your answer with
reasoning.
• The equation is reliable because:
o R² = 0.971, meaning the model explains 97.1% of the variation in resale
price.
o P-values for predictors are statistically significant (<0.05).
o Residuals are normally distributed, making the predictions valid.
7. Determine and interpret the coefficient of multiple determination (R²). How well does
the model explain variations in resale price?
• R² = 0.971, meaning 97.1% of the variance in resale price is explained by the model.
8. Which predictor has the most influence on resale price, and which has the least
impact? Explain your findings.
• Most influential predictor: Engine Power
•   Least influential predictor: Fuel Type – Petrol
9. What does the Variance Inflation Factor (VIF) reveal about multicollinearity among
the predictors?
• The VIF values are:
o Car Age: 1.063
o Mileage: 1.016
o Engine Power:1.025
o Fuel Type: 1.025
•   Since all VIF values are beow 5, multicollinearity is not a concern.
10. Analyze the P-P plot. Does it suggest that residuals follow a normal distribution?
•   Yes, the P-P plot follows a 45-degree straight line, meaning residuals are normally
distributed.
********** 3 **********
--- page 4 ---
11. Examine the residual histogram. Does the distribution appear normal, or are there
deviations?
• The histogram of residuals is bell-shaped, confirming normality.
•   There are no extreme outliers, meaning the model is well-behaved.
12. Evaluate the residual plot. Are there any noticeable patterns indicating problems with
the model?
• The residual plot shows no clear pattern, indicating homoscedasticity (constant
variance).
• The random scatter confirms that the model does not suffer from systematic bias.
13. Examine the ANOVA table: What does the significance (p-value) tell us about the
overall model fit?
• The F-statistic p-value (<0.05);ljm , meaning the model is statistically significant
14. Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals?
• Durbin-Watson (DW) = 2.041, which is close to 2, indicating no significant
autocorrelation in residuals.
15. Predict the resale price for a car with these features:
• Car Age = 5 years
• Mileage = 60,000 miles
• Engine Power = 150 HP
•   Fuel Type = Petrol (1)
Using the regression equation:
31.802
a
Synoptic
a) this is three factor solution.
Rotated Factor Matrixa
Q3
Factor
CO-
1   2   3
1,2,
3;   [Price]   0.043   0.992   0.026
BL-   [2
Appl   [Quantity]   0.062   0.921   0.019
y   0]
[Product Variety]   0.986   0.024   0.097
Eval
uate   [Advertisements]   0.131   0.028   0.966
,
crea   [Health Concern ( Sugar free, fat free etc)]   0.985   0.04   0.129
te
[Presentation of Ice Cream]   0.137   0.024   0.967
[Value for money]   -0.016   0.954   0.02
********** 4 **********
--- page 5 ---
[Product Ingredients]   0.959   0.029   0.121
Extraction Method: Principal Axis Factoring.
Rotation Method: Varimax with Kaiser Normalization.
Note to evaluators : Factor names are subjective student may name them in multiple ways
Factor 1 (Healthy   Factor 3 (in-
Choices)   Factor 2 (Tangible)   Tangible)
[Product Variety]   [Price]   [Advertisements]
[Health Concern ( Sugar   [Presentation of
[Quantity]
free, fat free etc)]   Ice Cream]
[Product Ingredients]   [Value for money]
b) there is no variable that should not be there in the factor analysis as all variables
have anti-aging correlations >0.5, extraction communality >0.5, and non of them
have any cross loading.
c) Scree plot indicates 3 factors as good solution however 3 factors have steep slopes
4th factor slope is not so steep
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5,
total explained variance > 60% all variables have communality >0.5, and there is no
cross loading indicates a good solution. Yes factor analysis is relevant in this case
and this solution can be used
e) Factor 1 (Healthy Choices) is the most important factor As it has highest
communality.
F. Difference Between PCA & Common Factor Analysis
Principal Component   Common Factor
Feature
Analysis (PCA)   Analysis (CFA)
Data reduction and   Identifying latent factors
Purpose   transformation to   that explain the observed
uncorrelated components.   variables.
Explanatory, used to
Descriptive, used to
Type of Analysis   uncover hidden
summarize variance in data.
constructs.
Focuses only on shared
Mathematical   Maximizes total variance in
(common) variance
Basis   the data.
among variables.
Components are extracted   Factors are extracted to
Factor
to explain the maximum   explain correlations
Extraction
variance.   between variables.
Correlation   Does not assume any   Assumes an underlying
Assumption   underlying factor structure. structure where observed
********** 5 **********
--- page 6 ---
variables load onto latent
factors.
Data compression,   Psychological, social, and
Use Cases   dimensionality reduction,   economic research to
visualization.   study latent traits.
Factors represent
Components are
underlying traits or
mathematical constructs
Interpretability   constructs that explain
and may not have direct
relationships among
interpretability.
variables.
a Answer:
5NN
Standa
Standar   Standar
rdised
dised   dised   Standardis
Distan   Standardised
Distance Distance ed Distance
ce of   of 2nd   of 3rd   of 4th   Distance of
1st   5th
observation
observat observat   observation
observ
ion   ion
Visit Supermarket   ation
N   4   1   5   4   1
Q4   Y   1   6   6   7   4
N   7   5   3   2   7
CO-
Y   2   2   4   1   3
1,2,   N   5   7   7   3   6
3;   Y   6   3   2   6   5
N   3   4   1   5   2
BL-
[1
Appl   Rank
1 Y   N   N   Y   N   0]
y,
2 Y   Y   Y   N   N
Anal   3 N   Y   N   N   Y
4 N   N   Y   N   Y
yse,
5 N   N   N   N   Y
Eval
uate   Prediction   N   N   N   N   Y
Actual   Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   3   3
Y   1   1   2
Grand Total   4   1   5
********** 6 **********
--- page 7 ---
Accuracy   80.00%
Recall / Sensitivity   50.00%
100.00
Specificity   %
100.00
Precision   %
3NN
Rank
1 Y   N   N   Y   N
2 Y   Y   Y   N   N
3 N   Y   N   N   Y
Prediction Y   Y   N   N   N
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   1   1   2
Grand Total   3   2   5
Accuracy   60.00%
Recall / Sensitivity   50.00%
Specificity   66.67%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
b
Answers
Q4
i)   Discriminant Function = -4.824 + .023* Age (years) + .101 * Salary ($1000s)
CO-   + .004* Credit Score + .643* loan Type
ii)   Wilks lambda signifies discriminating power for the model. Lower the
1,2,   value(close to 0), better discrimination. Higher the value (close to 1 ) less
discriminating power of the model. In this case wilk’s lambda is .922 => close to
3;
1 hence the model has poor discriminating power.
BL-   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of   [1
Appl   variables. And lowest absolute values ( modulus since it is correlations) indicate
0]
lowest explanatory power of variables. In this case, Credit Score has highest
y,
(.718) and Age (.393) has lowest explanatory power.
Anal   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
yse,   Here the Box’s M is not significant (p value =.783 > 0.05) this suggests there is
Eval   no enough evidence to conclude that covariance matrices are significantly
different across two groups. So assumption of equal covariance matrices holds
uate   good
v)   Cross-validated accuracy is 57.0%.
Chance accuracy Calculations
********** 7 **********
--- page 8 ---
P()
44   29   73   0.365
57   70   127   0.635
0.5364
Chance Accuracy   5
Min Required   0.6705
Accuracy   63
this data has equal number of successes and failures. The chance accuracy for
the data is   p(S)2 + p(F)2 = 0.53645
We need atleast 25% improvement over chance accuracy i.e. 0.53645* 1.25 = 0.670563the
overall cross validated accuracy is not better than minimum required accuracy hence, the
model could not be used for prediction. Also the power of model is too low and there are some
non-significant variables in the model like loan type, Age you should not use the model for
prediction. You may use stepwise DA to improve results.
a
Marking scheme:
1. Why is logistic regression the appropriate technique for this problem? (01 Mark)
Logistic regression is used because the dependent variable (Employee Attrition: 1 =
Leaves, 0 = Stays) is binary.
It models the probability of an event occurring based on predictor variables (Age,
Salary, Years at Company, and Job Type).
2. Formulate the logistic regression equation based on the given predictors. (01 Mark)
The logistic regression model is:
e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
Q5   p ( x ) =
1 + e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
CO-
3. What does the pseudo R-square value indicate about the model’s performance? (02
1,2,   Marks)
The model explains 26.4% to 35.8% of the variance
3;   4. Which statistical tests are commonly used to assess model accuracy, and why? (02
BL-   Marks)
• Wald Test: p <0.05): significant model   [1
Appl   • Hosmer-Lemeshow Test (p > 0.05): significant model
5]
y,   5. How can the classification table help in evaluating the model’s effectiveness? (03
Mark)
Anal
yse,   False Positives (FP) = 16, meaning 16 employees who actually stayed were misclassified
as leaving.
Eval
False Negatives (FN) = 26, meaning 26 employees who actually left were misclassified
uate   as staying.
True Positives (TP) = 32, meaning 32 employees who left were correctly identified.
True Negatives (TN) = 76, meaning 76 employees who stayed were correctly identified.
Overall Accuracy = 72%, showing the model performs well but has limitations in
identifying employees who left.
6. Explain the concepts of Sensitivity and Specificity in relation to this model. (03 Marks)
Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
********** 8 **********
--- page 9 ---
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Sensitivity (55.2%): The model correctly identifies 55.2% of employees who left.
•   Specificity (82.6%): The model correctly identifies 82.6% of employees who
stayed.
7. Interpret the p-values of the predictors. Which variables are statistically significant?
(03 Marks)
• Age → Significant (p < 0.05), meaning age influences attrition.
•   Salary → significant (p < 0.05 meaning salary is a strong predictor.
•   Years at Company → Significant, p < 0.05 tenure strongly reduces attrition.
•   Job Type → p < 0.05 significant.
b Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as
Q5   an outlier.
Here, 4/(n-k-1) = 4/ (30-5-1) = 0.167
CO-;   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.167)   [5]
SO-;
BL-
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO-   d. What are characteristics of each group? (For 3 cluster solution)
1,2,   Cluster N   LuxuryTra   Adventu   LastMin   StayLuxur   Loyalt   GroupTrave
vel   re   ute   Budget   Flights   y   y   l
3;   1   9   4.89   4.89   5.33   8.22   4.44   7.44   8.00   7.33
BL-   2   8   6.75   4.75   4.25   5.25   2.13   7.00   7.13   7.75
3   13   7.69   8.00   8.08   5.85   6.23   3.92   4.69   4.00   [1
Appl   Total   30   6.60   6.20   6.23   6.40   4.60   5.80   6.33   6.00
5]
y,
Cluster 1: Low on LuxuryTravel, Adventure and Flights but High on Budget,
Anal
StayLuxury, Loyalty and GroupTravel
yse,   Cluster 2: Low/ Moderate on LuxuryTravel and Budget but High on StayLuxury,
Loyalty and GroupTravel
Eval   Cluster 3: High on LuxuryTravel, Adventure, LastMinute and Flights but low on
uate   budget, StayLuxury, Loyalty and GroupTravel
*Students may write for 2 cluster solution as well.
e. Which group is most profitable for the bank?
Cluster 3 is most profitable. (For 3 cluster solution)
• These customers prefer luxury travel and high-end experiences, meaning they
are willing to spend more on luxury accommodations, premium flight tickets,
and exclusive experiences.
********** 9 **********
--- page 10 ---
• Frequent and Spontaneous Travelers – High scores on LastMinute suggest that
they often book trips impulsively. Last-minute bookings usually come with
higher pricing and fewer discounts, increasing revenue for travel companies.
• Preference for Flights – Since these customers prioritize air travel over other
modes, they tend to book more expensive flight tickets, especially for
premium seating, business class, or direct flights.
• Adventure Enthusiasts Pay for Experiences – Travelers who score high on
Adventure often seek adventure sports, guided tours, and activity-based
packages, which are high-margin offerings for companies.
*Students may write for 2 cluster solution as well.
b Discuss the objectives of cluster analysis and its applications in business.
.
Synoptic Answer:
Q6   Clustering groups similar data points, useful in multiple business domains.
CO-
2,3;   Key Points:
BL-
1. Objective (1 mark) – Identify patterns, segment markets, detect anomalies.   [5]
Und   2. Clustering Methods (1 mark) – K-means, Hierarchical, DBSCAN.
erst   3. Applications (1 mark) – Customer segmentation, fraud detection,
recommender systems.
and   4. Example (1 mark) – E-commerce uses clustering for personalized
recommendations.
5. Business Impact (1 mark) – Enhances marketing strategies and operational
efficiency.
a Answers
Q7   Sales Revenue   3 moving
Month
($1000s)   Avg   error&2   Exp sm
CO-   Jan   200   180   400
Feb   220   194   676
1,2,
Mar   250   212.2   1428.84
3;   Apr   270   223.3333 2177.778   238.66   982.1956
BL-   May   290   246.6667 1877.778   260.598   864.4776
Jun   310   270   1600 281.1794   830.627   [1
Appl   Jul   330   290   1600 301.3538   820.6036
0]
y,   310   321.4061
Anal
yse,   Forecast
Eval   error   1813.889   857.5348
uate
Summary
Method   Forecast   MSE
3 moving   310   1813.889
********** 10 **********
--- page 11 ---
Expo sm alpha =
0.7   321.4061   857.5348
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph
below, the lags and are above zero as well as below zero indicating stationarity. There is no
need for difference for this data.
Q7
CO-
The model selection is done on the basis of following parameters
1,2,
1. Requirement of stationarity (in this case d = 0)
3;   2. BIC as low as possible
3. All lags (except intercept) need to be significant
BL-   4. Ljung-Box test should not be significant
[1
Appl   5. Residual ACF & PACF should be within the lines
0]
y,   Any simplest model that satisfies above parameters is the best model and can be used
for forecasting.
Anal   In above case
Sr   Model   BIC   Description   Result
yse,
No
Eval   1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, lag sig   Model
without   problem – Residual ACF & PACF not   cannot be
uate   removing   within range   used
outliers
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,. Residual   Model
without   ACF & PACF within range problem –   cannot be
removing   d=1, all lags not sig,   used
outliers
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag sig,   Model
without   Residual ACF & PACF within range   cannot be
removing   problem – d=1   used
outliers
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig,   Model
without   Residual ACF & PACF not within   cannot be
removing   range   used
outliers   problem – all lags not sig.
5   ARIMA(1,0,0)   9.456   All correct + minimum BIC + Simplest Model can
after removing   possible model   be used
outliers
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Forecast
Model   30   31   32   33   34   35
Ethereum Forecast   2076.11 2083.18 2089.84 2096.09 2101.97 2107.51
Price in US UCL   2231.33 2298.01 2347.04 2386.30 2419.02 2446.89
$-Model_1 LCL   1925.19 1876.50 1844.19 1820.47 1802.23 1787.82
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is
not too wide for initial forecasts. As the forecasting period extends, width becomes
wider making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Re-Exam · Sem 8 · Answer key · paper 4ae5de27757a

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/MBATech_Computer_7047/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Sem 8 Re-exam(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 02 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a How does data visualization enhance decision-making in business analytics?
.
Synoptic Answer:
Data visualization converts complex information into graphical formats for better
decision-making.
CO-   Key Points:
1;
BL-   1. Definition (1 mark) – Visual representation of data through graphs, charts,   [5]
Und   dashboards.
erst   2. Benefits (1 mark) – Identifies trends, outliers, and correlations.
and   3. Types (1 mark) – Bar charts, scatter plots, heat maps, dashboards.
4. Business Applications (1 mark) – Sales forecasting, customer segmentation,
fraud detection.
5. Example (1 mark) – A retail company uses dashboards to track regional sales
performance.
CO- b What are the essential steps in handling outliers in data pre-processing?
1;
.
BL-   Synoptic Answer:
Und   [5]
erst   Outliers can distort statistical models and must be handled carefully.
and,
appl   Key Points:
y
********** 1 **********
--- page 2 ---
1. Definition & Causes (1 mark) – Data errors, genuine variations, fraudulent
activities.
2. Detection Methods (1 mark) – Box plots, Z-score method, IQR rule.
3. Treatment Strategies (1 mark) – Winsorization, transformation (log/square
root), capping.
4. Removing Outliers (1 mark) – If justified, remove extreme values.
5. Example (1 mark) – In a salary dataset, a CEO’s salary may be an outlier
compared to employees.
c Explain the role of dummy variables in multiple regression analysis with an example.
.
Synoptic Answer:
Dummy variables convert categorical data into numerical format for regression
CO-
models.
1,2;
BL-
Key Points:
Und   [5]
erst
1. Definition (1 mark) – Used to include categorical data in regression models.
and,
2. Creation (1 mark) – Assign 0/1 to different categories.
appl
3. Example (1 mark) – Gender (Male = 1, Female = 0).
y
4. Regression Interpretation (1 mark) – Dummy variable coefficients show
category effects.
5. Business Application (1 mark) – Analyzing salary differences between
departments.
d Describe the concepts of sensitivity and specificity in the context of classification
models.
.
Synoptic Answer:
Sensitivity and specificity measure the performance of classification models.
CO-
2,3;
Key Points:
BL-
Und   1. Sensitivity (1 mark) – Measures true positive rate (correctly classified   [5]
erst
positive cases).
and,
2. Specificity (1 mark) – Measures true negative rate (correctly classified
appl
negative cases).
y
3. Trade-off (1 mark) – Higher sensitivity lowers specificity and vice versa.
4. Use Cases (1 mark) – Sensitivity in medical tests; specificity in fraud
detection.
5. Example (1 mark) – A cancer screening test prioritizes sensitivity to detect all
positive cases.
Q2
Answers   [2
CO-
1,2,   1. What type of model was applied, and why is it appropriate for this scenario?   0]
3;   The Multiple Linear Regression (MLR) model was applied because the resale price
BL-   (dependent variable) is continuous and influenced by multiple predictors:
********** 2 **********
--- page 3 ---
Appl   o Car Age
y,   o Mileage
Anal   o Engine Power
yse,   o Fuel Type (categorical)
Eval   • MLR is appropriate for predicting a continuous variable based on multiple factors.
uate
2. Which category serves as the reference for the qualitative variable (Fuel Type), and
why?
• The categorical variable is Fuel Type (Petrol = 1, Diesel = 0).
• The baseline/reference category is Diesel (coded as 0).
3. Write down the equation obtained from the analysis.
Resale Price=-
1.003−0.773(Car Age)−0.043(Mileage)+0.304(Engine Power)+1.380(Fuel Type)
4. Explain the significance of coefficient of Fuel Type in the model.
•   (Fuel Type - Petrol): Petrol cars are, on average, 1.380 more expensive than Diesel
cars.
5. Why does the intercept (b0) lack practical interpretation in this context?
• The intercept represents the resale price when all predictors are zero (0-year-old car,
0 mileage, 0 HP, Diesel).
•   This is not realistic as cars always have mileage, age, and power.
6. Can this equation be reliably used to estimate resale prices? Support your answer with
reasoning.
• The equation is reliable because:
o R² = 0.971, meaning the model explains 97.1% of the variation in resale
price.
o P-values for predictors are statistically significant (<0.05).
o Residuals are normally distributed, making the predictions valid.
7. Determine and interpret the coefficient of multiple determination (R²). How well does
the model explain variations in resale price?
• R² = 0.971, meaning 97.1% of the variance in resale price is explained by the model.
8. Which predictor has the most influence on resale price, and which has the least
impact? Explain your findings.
• Most influential predictor: Engine Power
•   Least influential predictor: Fuel Type – Petrol
9. What does the Variance Inflation Factor (VIF) reveal about multicollinearity among
the predictors?
• The VIF values are:
o Car Age: 1.063
o Mileage: 1.016
o Engine Power:1.025
o Fuel Type: 1.025
•   Since all VIF values are beow 5, multicollinearity is not a concern.
10. Analyze the P-P plot. Does it suggest that residuals follow a normal distribution?
•   Yes, the P-P plot follows a 45-degree straight line, meaning residuals are normally
distributed.
********** 3 **********
--- page 4 ---
11. Examine the residual histogram. Does the distribution appear normal, or are there
deviations?
• The histogram of residuals is bell-shaped, confirming normality.
•   There are no extreme outliers, meaning the model is well-behaved.
12. Evaluate the residual plot. Are there any noticeable patterns indicating problems with
the model?
• The residual plot shows no clear pattern, indicating homoscedasticity (constant
variance).
• The random scatter confirms that the model does not suffer from systematic bias.
13. Examine the ANOVA table: What does the significance (p-value) tell us about the
overall model fit?
• The F-statistic p-value (<0.05);ljm , meaning the model is statistically significant
14. Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals?
• Durbin-Watson (DW) = 2.041, which is close to 2, indicating no significant
autocorrelation in residuals.
15. Predict the resale price for a car with these features:
• Car Age = 5 years
• Mileage = 60,000 miles
• Engine Power = 150 HP
•   Fuel Type = Petrol (1)
Using the regression equation:
31.802
a
Synoptic
a) this is three factor solution.
Rotated Factor Matrixa
Q3
Factor
CO-
1   2   3
1,2,
3;   [Price]   0.043   0.992   0.026
BL-   [2
Appl   [Quantity]   0.062   0.921   0.019
y   0]
[Product Variety]   0.986   0.024   0.097
Eval
uate   [Advertisements]   0.131   0.028   0.966
,
crea   [Health Concern ( Sugar free, fat free etc)]   0.985   0.04   0.129
te
[Presentation of Ice Cream]   0.137   0.024   0.967
[Value for money]   -0.016   0.954   0.02
********** 4 **********
--- page 5 ---
[Product Ingredients]   0.959   0.029   0.121
Extraction Method: Principal Axis Factoring.
Rotation Method: Varimax with Kaiser Normalization.
Note to evaluators : Factor names are subjective student may name them in multiple ways
Factor 1 (Healthy   Factor 3 (in-
Choices)   Factor 2 (Tangible)   Tangible)
[Product Variety]   [Price]   [Advertisements]
[Health Concern ( Sugar   [Presentation of
[Quantity]
free, fat free etc)]   Ice Cream]
[Product Ingredients]   [Value for money]
b) there is no variable that should not be there in the factor analysis as all variables
have anti-aging correlations >0.5, extraction communality >0.5, and non of them
have any cross loading.
c) Scree plot indicates 3 factors as good solution however 3 factors have steep slopes
4th factor slope is not so steep
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5,
total explained variance > 60% all variables have communality >0.5, and there is no
cross loading indicates a good solution. Yes factor analysis is relevant in this case
and this solution can be used
e) Factor 1 (Healthy Choices) is the most important factor As it has highest
communality.
F. Difference Between PCA & Common Factor Analysis
Principal Component   Common Factor
Feature
Analysis (PCA)   Analysis (CFA)
Data reduction and   Identifying latent factors
Purpose   transformation to   that explain the observed
uncorrelated components.   variables.
Explanatory, used to
Descriptive, used to
Type of Analysis   uncover hidden
summarize variance in data.
constructs.
Focuses only on shared
Mathematical   Maximizes total variance in
(common) variance
Basis   the data.
among variables.
Components are extracted   Factors are extracted to
Factor
to explain the maximum   explain correlations
Extraction
variance.   between variables.
Correlation   Does not assume any   Assumes an underlying
Assumption   underlying factor structure. structure where observed
********** 5 **********
--- page 6 ---
variables load onto latent
factors.
Data compression,   Psychological, social, and
Use Cases   dimensionality reduction,   economic research to
visualization.   study latent traits.
Factors represent
Components are
underlying traits or
mathematical constructs
Interpretability   constructs that explain
and may not have direct
relationships among
interpretability.
variables.
a Answer:
5NN
Standa
Standar   Standar
rdised
dised   dised   Standardis
Distan   Standardised
Distance Distance ed Distance
ce of   of 2nd   of 3rd   of 4th   Distance of
1st   5th
observation
observat observat   observation
observ
ion   ion
Visit Supermarket   ation
N   4   1   5   4   1
Q4   Y   1   6   6   7   4
N   7   5   3   2   7
CO-
Y   2   2   4   1   3
1,2,   N   5   7   7   3   6
3;   Y   6   3   2   6   5
N   3   4   1   5   2
BL-
[1
Appl   Rank
1 Y   N   N   Y   N   0]
y,
2 Y   Y   Y   N   N
Anal   3 N   Y   N   N   Y
4 N   N   Y   N   Y
yse,
5 N   N   N   N   Y
Eval
uate   Prediction   N   N   N   N   Y
Actual   Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   3   3
Y   1   1   2
Grand Total   4   1   5
********** 6 **********
--- page 7 ---
Accuracy   80.00%
Recall / Sensitivity   50.00%
100.00
Specificity   %
100.00
Precision   %
3NN
Rank
1 Y   N   N   Y   N
2 Y   Y   Y   N   N
3 N   Y   N   N   Y
Prediction Y   Y   N   N   N
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   1   1   2
Grand Total   3   2   5
Accuracy   60.00%
Recall / Sensitivity   50.00%
Specificity   66.67%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
b
Answers
Q4
i)   Discriminant Function = -4.824 + .023* Age (years) + .101 * Salary ($1000s)
CO-   + .004* Credit Score + .643* loan Type
ii)   Wilks lambda signifies discriminating power for the model. Lower the
1,2,   value(close to 0), better discrimination. Higher the value (close to 1 ) less
discriminating power of the model. In this case wilk’s lambda is .922 => close to
3;
1 hence the model has poor discriminating power.
BL-   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of   [1
Appl   variables. And lowest absolute values ( modulus since it is correlations) indicate
0]
lowest explanatory power of variables. In this case, Credit Score has highest
y,
(.718) and Age (.393) has lowest explanatory power.
Anal   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
yse,   Here the Box’s M is not significant (p value =.783 > 0.05) this suggests there is
Eval   no enough evidence to conclude that covariance matrices are significantly
different across two groups. So assumption of equal covariance matrices holds
uate   good
v)   Cross-validated accuracy is 57.0%.
Chance accuracy Calculations
********** 7 **********
--- page 8 ---
P()
44   29   73   0.365
57   70   127   0.635
0.5364
Chance Accuracy   5
Min Required   0.6705
Accuracy   63
this data has equal number of successes and failures. The chance accuracy for
the data is   p(S)2 + p(F)2 = 0.53645
We need atleast 25% improvement over chance accuracy i.e. 0.53645* 1.25 = 0.670563the
overall cross validated accuracy is not better than minimum required accuracy hence, the
model could not be used for prediction. Also the power of model is too low and there are some
non-significant variables in the model like loan type, Age you should not use the model for
prediction. You may use stepwise DA to improve results.
a
Marking scheme:
1. Why is logistic regression the appropriate technique for this problem? (01 Mark)
Logistic regression is used because the dependent variable (Employee Attrition: 1 =
Leaves, 0 = Stays) is binary.
It models the probability of an event occurring based on predictor variables (Age,
Salary, Years at Company, and Job Type).
2. Formulate the logistic regression equation based on the given predictors. (01 Mark)
The logistic regression model is:
e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
Q5   p ( x ) =
1 + e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
CO-
3. What does the pseudo R-square value indicate about the model’s performance? (02
1,2,   Marks)
The model explains 26.4% to 35.8% of the variance
3;   4. Which statistical tests are commonly used to assess model accuracy, and why? (02
BL-   Marks)
• Wald Test: p <0.05): significant model   [1
Appl   • Hosmer-Lemeshow Test (p > 0.05): significant model
5]
y,   5. How can the classification table help in evaluating the model’s effectiveness? (03
Mark)
Anal
yse,   False Positives (FP) = 16, meaning 16 employees who actually stayed were misclassified
as leaving.
Eval
False Negatives (FN) = 26, meaning 26 employees who actually left were misclassified
uate   as staying.
True Positives (TP) = 32, meaning 32 employees who left were correctly identified.
True Negatives (TN) = 76, meaning 76 employees who stayed were correctly identified.
Overall Accuracy = 72%, showing the model performs well but has limitations in
identifying employees who left.
6. Explain the concepts of Sensitivity and Specificity in relation to this model. (03 Marks)
Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
********** 8 **********
--- page 9 ---
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Sensitivity (55.2%): The model correctly identifies 55.2% of employees who left.
•   Specificity (82.6%): The model correctly identifies 82.6% of employees who
stayed.
7. Interpret the p-values of the predictors. Which variables are statistically significant?
(03 Marks)
• Age → Significant (p < 0.05), meaning age influences attrition.
•   Salary → significant (p < 0.05 meaning salary is a strong predictor.
•   Years at Company → Significant, p < 0.05 tenure strongly reduces attrition.
•   Job Type → p < 0.05 significant.
b Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as
Q5   an outlier.
Here, 4/(n-k-1) = 4/ (30-5-1) = 0.167
CO-;   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.167)   [5]
SO-;
BL-
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO-   d. What are characteristics of each group? (For 3 cluster solution)
1,2,   Cluster N   LuxuryTra   Adventu   LastMin   StayLuxur   Loyalt   GroupTrave
vel   re   ute   Budget   Flights   y   y   l
3;   1   9   4.89   4.89   5.33   8.22   4.44   7.44   8.00   7.33
BL-   2   8   6.75   4.75   4.25   5.25   2.13   7.00   7.13   7.75
3   13   7.69   8.00   8.08   5.85   6.23   3.92   4.69   4.00   [1
Appl   Total   30   6.60   6.20   6.23   6.40   4.60   5.80   6.33   6.00
5]
y,
Cluster 1: Low on LuxuryTravel, Adventure and Flights but High on Budget,
Anal
StayLuxury, Loyalty and GroupTravel
yse,   Cluster 2: Low/ Moderate on LuxuryTravel and Budget but High on StayLuxury,
Loyalty and GroupTravel
Eval   Cluster 3: High on LuxuryTravel, Adventure, LastMinute and Flights but low on
uate   budget, StayLuxury, Loyalty and GroupTravel
*Students may write for 2 cluster solution as well.
e. Which group is most profitable for the bank?
Cluster 3 is most profitable. (For 3 cluster solution)
• These customers prefer luxury travel and high-end experiences, meaning they
are willing to spend more on luxury accommodations, premium flight tickets,
and exclusive experiences.
********** 9 **********
--- page 10 ---
• Frequent and Spontaneous Travelers – High scores on LastMinute suggest that
they often book trips impulsively. Last-minute bookings usually come with
higher pricing and fewer discounts, increasing revenue for travel companies.
• Preference for Flights – Since these customers prioritize air travel over other
modes, they tend to book more expensive flight tickets, especially for
premium seating, business class, or direct flights.
• Adventure Enthusiasts Pay for Experiences – Travelers who score high on
Adventure often seek adventure sports, guided tours, and activity-based
packages, which are high-margin offerings for companies.
*Students may write for 2 cluster solution as well.
b Discuss the objectives of cluster analysis and its applications in business.
.
Synoptic Answer:
Q6   Clustering groups similar data points, useful in multiple business domains.
CO-
2,3;   Key Points:
BL-
1. Objective (1 mark) – Identify patterns, segment markets, detect anomalies.   [5]
Und   2. Clustering Methods (1 mark) – K-means, Hierarchical, DBSCAN.
erst   3. Applications (1 mark) – Customer segmentation, fraud detection,
recommender systems.
and   4. Example (1 mark) – E-commerce uses clustering for personalized
recommendations.
5. Business Impact (1 mark) – Enhances marketing strategies and operational
efficiency.
a Answers
Q7   Sales Revenue   3 moving
Month
($1000s)   Avg   error&2   Exp sm
CO-   Jan   200   180   400
Feb   220   194   676
1,2,
Mar   250   212.2   1428.84
3;   Apr   270   223.3333 2177.778   238.66   982.1956
BL-   May   290   246.6667 1877.778   260.598   864.4776
Jun   310   270   1600 281.1794   830.627   [1
Appl   Jul   330   290   1600 301.3538   820.6036
0]
y,   310   321.4061
Anal
yse,   Forecast
Eval   error   1813.889   857.5348
uate
Summary
Method   Forecast   MSE
3 moving   310   1813.889
********** 10 **********
--- page 11 ---
Expo sm alpha =
0.7   321.4061   857.5348
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph
below, the lags and are above zero as well as below zero indicating stationarity. There is no
need for difference for this data.
Q7
CO-
The model selection is done on the basis of following parameters
1,2,
1. Requirement of stationarity (in this case d = 0)
3;   2. BIC as low as possible
3. All lags (except intercept) need to be significant
BL-   4. Ljung-Box test should not be significant
[1
Appl   5. Residual ACF & PACF should be within the lines
0]
y,   Any simplest model that satisfies above parameters is the best model and can be used
for forecasting.
Anal   In above case
Sr   Model   BIC   Description   Result
yse,
No
Eval   1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, lag sig   Model
without   problem – Residual ACF & PACF not   cannot be
uate   removing   within range   used
outliers
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,. Residual   Model
without   ACF & PACF within range problem –   cannot be
removing   d=1, all lags not sig,   used
outliers
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag sig,   Model
without   Residual ACF & PACF within range   cannot be
removing   problem – d=1   used
outliers
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig,   Model
without   Residual ACF & PACF not within   cannot be
removing   range   used
outliers   problem – all lags not sig.
5   ARIMA(1,0,0)   9.456   All correct + minimum BIC + Simplest Model can
after removing   possible model   be used
outliers
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Forecast
Model   30   31   32   33   34   35
Ethereum Forecast   2076.11 2083.18 2089.84 2096.09 2101.97 2107.51
Price in US UCL   2231.33 2298.01 2347.04 2386.30 2419.02 2446.89
$-Model_1 LCL   1925.19 1876.50 1844.19 1820.47 1802.23 1787.82
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is
not too wide for initial forecasts. As the forecasting period extends, width becomes
wider making forecasts untrusted.
********** 12 **********
````

## 2024-25 · Re-Exam · Sem 8 · Answer key · paper 4f0286351d65

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/MBATech_DS_7052/Business Analytics/ANS_Business Analytics(703TM0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MBA. Tech (AI)/MBA. Tech (Chem)/MBA Tech (Comp)/MBA. Tech (DS)/MBA.
Tech (EXTC)/MBA. Tech (IT)/MBA. Tech (Mech)
Year: IV/Sem 8 Re-exam(Exam Year: 2024-2025)
Subject: Business Analytics
Date: 02 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory
3. A attempt any 4 questions out of remaining 6 questions
4. Answer to each new question to be started on a fresh page.
5. Figures in brackets on the right hand side indicate full marks.
6. Assume Suitable data if necessary.
Q1
Answer briefly:
a How does data visualization enhance decision-making in business analytics?
.
Synoptic Answer:
Data visualization converts complex information into graphical formats for better
decision-making.
CO-   Key Points:
1;
BL-   1. Definition (1 mark) – Visual representation of data through graphs, charts,   [5]
Und   dashboards.
erst   2. Benefits (1 mark) – Identifies trends, outliers, and correlations.
and   3. Types (1 mark) – Bar charts, scatter plots, heat maps, dashboards.
4. Business Applications (1 mark) – Sales forecasting, customer segmentation,
fraud detection.
5. Example (1 mark) – A retail company uses dashboards to track regional sales
performance.
CO- b What are the essential steps in handling outliers in data pre-processing?
1;
.
BL-   Synoptic Answer:
Und   [5]
erst   Outliers can distort statistical models and must be handled carefully.
and,
appl   Key Points:
y
********** 1 **********
--- page 2 ---
1. Definition & Causes (1 mark) – Data errors, genuine variations, fraudulent
activities.
2. Detection Methods (1 mark) – Box plots, Z-score method, IQR rule.
3. Treatment Strategies (1 mark) – Winsorization, transformation (log/square
root), capping.
4. Removing Outliers (1 mark) – If justified, remove extreme values.
5. Example (1 mark) – In a salary dataset, a CEO’s salary may be an outlier
compared to employees.
c Explain the role of dummy variables in multiple regression analysis with an example.
.
Synoptic Answer:
Dummy variables convert categorical data into numerical format for regression
CO-
models.
1,2;
BL-
Key Points:
Und   [5]
erst
1. Definition (1 mark) – Used to include categorical data in regression models.
and,
2. Creation (1 mark) – Assign 0/1 to different categories.
appl
3. Example (1 mark) – Gender (Male = 1, Female = 0).
y
4. Regression Interpretation (1 mark) – Dummy variable coefficients show
category effects.
5. Business Application (1 mark) – Analyzing salary differences between
departments.
d Describe the concepts of sensitivity and specificity in the context of classification
models.
.
Synoptic Answer:
Sensitivity and specificity measure the performance of classification models.
CO-
2,3;
Key Points:
BL-
Und   1. Sensitivity (1 mark) – Measures true positive rate (correctly classified   [5]
erst
positive cases).
and,
2. Specificity (1 mark) – Measures true negative rate (correctly classified
appl
negative cases).
y
3. Trade-off (1 mark) – Higher sensitivity lowers specificity and vice versa.
4. Use Cases (1 mark) – Sensitivity in medical tests; specificity in fraud
detection.
5. Example (1 mark) – A cancer screening test prioritizes sensitivity to detect all
positive cases.
Q2
Answers   [2
CO-
1,2,   1. What type of model was applied, and why is it appropriate for this scenario?   0]
3;   The Multiple Linear Regression (MLR) model was applied because the resale price
BL-   (dependent variable) is continuous and influenced by multiple predictors:
********** 2 **********
--- page 3 ---
Appl   o Car Age
y,   o Mileage
Anal   o Engine Power
yse,   o Fuel Type (categorical)
Eval   • MLR is appropriate for predicting a continuous variable based on multiple factors.
uate
2. Which category serves as the reference for the qualitative variable (Fuel Type), and
why?
• The categorical variable is Fuel Type (Petrol = 1, Diesel = 0).
• The baseline/reference category is Diesel (coded as 0).
3. Write down the equation obtained from the analysis.
Resale Price=-
1.003−0.773(Car Age)−0.043(Mileage)+0.304(Engine Power)+1.380(Fuel Type)
4. Explain the significance of coefficient of Fuel Type in the model.
•   (Fuel Type - Petrol): Petrol cars are, on average, 1.380 more expensive than Diesel
cars.
5. Why does the intercept (b0) lack practical interpretation in this context?
• The intercept represents the resale price when all predictors are zero (0-year-old car,
0 mileage, 0 HP, Diesel).
•   This is not realistic as cars always have mileage, age, and power.
6. Can this equation be reliably used to estimate resale prices? Support your answer with
reasoning.
• The equation is reliable because:
o R² = 0.971, meaning the model explains 97.1% of the variation in resale
price.
o P-values for predictors are statistically significant (<0.05).
o Residuals are normally distributed, making the predictions valid.
7. Determine and interpret the coefficient of multiple determination (R²). How well does
the model explain variations in resale price?
• R² = 0.971, meaning 97.1% of the variance in resale price is explained by the model.
8. Which predictor has the most influence on resale price, and which has the least
impact? Explain your findings.
• Most influential predictor: Engine Power
•   Least influential predictor: Fuel Type – Petrol
9. What does the Variance Inflation Factor (VIF) reveal about multicollinearity among
the predictors?
• The VIF values are:
o Car Age: 1.063
o Mileage: 1.016
o Engine Power:1.025
o Fuel Type: 1.025
•   Since all VIF values are beow 5, multicollinearity is not a concern.
10. Analyze the P-P plot. Does it suggest that residuals follow a normal distribution?
•   Yes, the P-P plot follows a 45-degree straight line, meaning residuals are normally
distributed.
********** 3 **********
--- page 4 ---
11. Examine the residual histogram. Does the distribution appear normal, or are there
deviations?
• The histogram of residuals is bell-shaped, confirming normality.
•   There are no extreme outliers, meaning the model is well-behaved.
12. Evaluate the residual plot. Are there any noticeable patterns indicating problems with
the model?
• The residual plot shows no clear pattern, indicating homoscedasticity (constant
variance).
• The random scatter confirms that the model does not suffer from systematic bias.
13. Examine the ANOVA table: What does the significance (p-value) tell us about the
overall model fit?
• The F-statistic p-value (<0.05);ljm , meaning the model is statistically significant
14. Analyze the Durbin-Watson statistic: Does it indicate any autocorrelation in the
residuals?
• Durbin-Watson (DW) = 2.041, which is close to 2, indicating no significant
autocorrelation in residuals.
15. Predict the resale price for a car with these features:
• Car Age = 5 years
• Mileage = 60,000 miles
• Engine Power = 150 HP
•   Fuel Type = Petrol (1)
Using the regression equation:
31.802
a
Synoptic
a) this is three factor solution.
Rotated Factor Matrixa
Q3
Factor
CO-
1   2   3
1,2,
3;   [Price]   0.043   0.992   0.026
BL-   [2
Appl   [Quantity]   0.062   0.921   0.019
y   0]
[Product Variety]   0.986   0.024   0.097
Eval
uate   [Advertisements]   0.131   0.028   0.966
,
crea   [Health Concern ( Sugar free, fat free etc)]   0.985   0.04   0.129
te
[Presentation of Ice Cream]   0.137   0.024   0.967
[Value for money]   -0.016   0.954   0.02
********** 4 **********
--- page 5 ---
[Product Ingredients]   0.959   0.029   0.121
Extraction Method: Principal Axis Factoring.
Rotation Method: Varimax with Kaiser Normalization.
Note to evaluators : Factor names are subjective student may name them in multiple ways
Factor 1 (Healthy   Factor 3 (in-
Choices)   Factor 2 (Tangible)   Tangible)
[Product Variety]   [Price]   [Advertisements]
[Health Concern ( Sugar   [Presentation of
[Quantity]
free, fat free etc)]   Ice Cream]
[Product Ingredients]   [Value for money]
b) there is no variable that should not be there in the factor analysis as all variables
have anti-aging correlations >0.5, extraction communality >0.5, and non of them
have any cross loading.
c) Scree plot indicates 3 factors as good solution however 3 factors have steep slopes
4th factor slope is not so steep
d) KMO >0.5, Bartlet’s test is significant, all variables have sampling adequacy >0.5,
total explained variance > 60% all variables have communality >0.5, and there is no
cross loading indicates a good solution. Yes factor analysis is relevant in this case
and this solution can be used
e) Factor 1 (Healthy Choices) is the most important factor As it has highest
communality.
F. Difference Between PCA & Common Factor Analysis
Principal Component   Common Factor
Feature
Analysis (PCA)   Analysis (CFA)
Data reduction and   Identifying latent factors
Purpose   transformation to   that explain the observed
uncorrelated components.   variables.
Explanatory, used to
Descriptive, used to
Type of Analysis   uncover hidden
summarize variance in data.
constructs.
Focuses only on shared
Mathematical   Maximizes total variance in
(common) variance
Basis   the data.
among variables.
Components are extracted   Factors are extracted to
Factor
to explain the maximum   explain correlations
Extraction
variance.   between variables.
Correlation   Does not assume any   Assumes an underlying
Assumption   underlying factor structure. structure where observed
********** 5 **********
--- page 6 ---
variables load onto latent
factors.
Data compression,   Psychological, social, and
Use Cases   dimensionality reduction,   economic research to
visualization.   study latent traits.
Factors represent
Components are
underlying traits or
mathematical constructs
Interpretability   constructs that explain
and may not have direct
relationships among
interpretability.
variables.
a Answer:
5NN
Standa
Standar   Standar
rdised
dised   dised   Standardis
Distan   Standardised
Distance Distance ed Distance
ce of   of 2nd   of 3rd   of 4th   Distance of
1st   5th
observation
observat observat   observation
observ
ion   ion
Visit Supermarket   ation
N   4   1   5   4   1
Q4   Y   1   6   6   7   4
N   7   5   3   2   7
CO-
Y   2   2   4   1   3
1,2,   N   5   7   7   3   6
3;   Y   6   3   2   6   5
N   3   4   1   5   2
BL-
[1
Appl   Rank
1 Y   N   N   Y   N   0]
y,
2 Y   Y   Y   N   N
Anal   3 N   Y   N   N   Y
4 N   N   Y   N   Y
yse,
5 N   N   N   N   Y
Eval
uate   Prediction   N   N   N   N   Y
Actual   Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   3   3
Y   1   1   2
Grand Total   4   1   5
********** 6 **********
--- page 7 ---
Accuracy   80.00%
Recall / Sensitivity   50.00%
100.00
Specificity   %
100.00
Precision   %
3NN
Rank
1 Y   N   N   Y   N
2 Y   Y   Y   N   N
3 N   Y   N   N   Y
Prediction Y   Y   N   N   N
Actual Y   N   N   N   Y
Predicted
Count of Prediction Column Labels
Grand
Row Labels   N   Y   Total
Actual   N   2   1   3
Y   1   1   2
Grand Total   3   2   5
Accuracy   60.00%
Recall / Sensitivity   50.00%
Specificity   66.67%
Precision   50.00%
5NN better than 3NN as has high accuracy as well as Specificity & Precision.
b
Answers
Q4
i)   Discriminant Function = -4.824 + .023* Age (years) + .101 * Salary ($1000s)
CO-   + .004* Credit Score + .643* loan Type
ii)   Wilks lambda signifies discriminating power for the model. Lower the
1,2,   value(close to 0), better discrimination. Higher the value (close to 1 ) less
discriminating power of the model. In this case wilk’s lambda is .922 => close to
3;
1 hence the model has poor discriminating power.
BL-   iii)   Structure matrix gives explanatory power of variables. Highest absolute values
( modulus since it is correlations) indicate highest explanatory power of   [1
Appl   variables. And lowest absolute values ( modulus since it is correlations) indicate
0]
lowest explanatory power of variables. In this case, Credit Score has highest
y,
(.718) and Age (.393) has lowest explanatory power.
Anal   iv)   H0 : The covariance matrices of the groups are same across the two groups
H1 : The covariance matrices of the groups are different across the two groups
yse,   Here the Box’s M is not significant (p value =.783 > 0.05) this suggests there is
Eval   no enough evidence to conclude that covariance matrices are significantly
different across two groups. So assumption of equal covariance matrices holds
uate   good
v)   Cross-validated accuracy is 57.0%.
Chance accuracy Calculations
********** 7 **********
--- page 8 ---
P()
44   29   73   0.365
57   70   127   0.635
0.5364
Chance Accuracy   5
Min Required   0.6705
Accuracy   63
this data has equal number of successes and failures. The chance accuracy for
the data is   p(S)2 + p(F)2 = 0.53645
We need atleast 25% improvement over chance accuracy i.e. 0.53645* 1.25 = 0.670563the
overall cross validated accuracy is not better than minimum required accuracy hence, the
model could not be used for prediction. Also the power of model is too low and there are some
non-significant variables in the model like loan type, Age you should not use the model for
prediction. You may use stepwise DA to improve results.
a
Marking scheme:
1. Why is logistic regression the appropriate technique for this problem? (01 Mark)
Logistic regression is used because the dependent variable (Employee Attrition: 1 =
Leaves, 0 = Stays) is binary.
It models the probability of an event occurring based on predictor variables (Age,
Salary, Years at Company, and Job Type).
2. Formulate the logistic regression equation based on the given predictors. (01 Mark)
The logistic regression model is:
e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
Q5   p ( x ) =
1 + e − 5.072 + 0.074( Age ) + 0.025(Salary) − 0.087(Yearsatcompany) + 0.796(Jobtype)
CO-
3. What does the pseudo R-square value indicate about the model’s performance? (02
1,2,   Marks)
The model explains 26.4% to 35.8% of the variance
3;   4. Which statistical tests are commonly used to assess model accuracy, and why? (02
BL-   Marks)
• Wald Test: p <0.05): significant model   [1
Appl   • Hosmer-Lemeshow Test (p > 0.05): significant model
5]
y,   5. How can the classification table help in evaluating the model’s effectiveness? (03
Mark)
Anal
yse,   False Positives (FP) = 16, meaning 16 employees who actually stayed were misclassified
as leaving.
Eval
False Negatives (FN) = 26, meaning 26 employees who actually left were misclassified
uate   as staying.
True Positives (TP) = 32, meaning 32 employees who left were correctly identified.
True Negatives (TN) = 76, meaning 76 employees who stayed were correctly identified.
Overall Accuracy = 72%, showing the model performs well but has limitations in
identifying employees who left.
6. Explain the concepts of Sensitivity and Specificity in relation to this model. (03 Marks)
Sensitivity (Recall) = TP / (TP + FN)
Sensitivity (Recall or True Positive Rate - TPR): Measures the model’s ability to correctly
identify employees who left.
********** 8 **********
--- page 9 ---
Specificity = TN / (TN + FP)
Measures the model’s ability to correctly identify employees who stayed.
•   Sensitivity (55.2%): The model correctly identifies 55.2% of employees who left.
•   Specificity (82.6%): The model correctly identifies 82.6% of employees who
stayed.
7. Interpret the p-values of the predictors. Which variables are statistically significant?
(03 Marks)
• Age → Significant (p < 0.05), meaning age influences attrition.
•   Salary → significant (p < 0.05 meaning salary is a strong predictor.
•   Years at Company → Significant, p < 0.05 tenure strongly reduces attrition.
•   Job Type → p < 0.05 significant.
b Solution: Any value of Cook’s distance greater than 4/(n-k-1) will be considered as
Q5   an outlier.
Here, 4/(n-k-1) = 4/ (30-5-1) = 0.167
CO-;   So, the outliers are S.No. 8, 15, 27 and 29 (as all of them are greater than 0.167)   [5]
SO-;
BL-
a Solution:
a. According to Dendrogram, 2 and 3 cluster solution is appropriate for the data.
b. Student may write the case numbers as per his choice of 2 or 3 cluster
solution.
c. ANOVA is significant for all variables indicating that all variables are
contributing in the cluster analysis. This also validates the cluster results.
Q6
CO-   d. What are characteristics of each group? (For 3 cluster solution)
1,2,   Cluster N   LuxuryTra   Adventu   LastMin   StayLuxur   Loyalt   GroupTrave
vel   re   ute   Budget   Flights   y   y   l
3;   1   9   4.89   4.89   5.33   8.22   4.44   7.44   8.00   7.33
BL-   2   8   6.75   4.75   4.25   5.25   2.13   7.00   7.13   7.75
3   13   7.69   8.00   8.08   5.85   6.23   3.92   4.69   4.00   [1
Appl   Total   30   6.60   6.20   6.23   6.40   4.60   5.80   6.33   6.00
5]
y,
Cluster 1: Low on LuxuryTravel, Adventure and Flights but High on Budget,
Anal
StayLuxury, Loyalty and GroupTravel
yse,   Cluster 2: Low/ Moderate on LuxuryTravel and Budget but High on StayLuxury,
Loyalty and GroupTravel
Eval   Cluster 3: High on LuxuryTravel, Adventure, LastMinute and Flights but low on
uate   budget, StayLuxury, Loyalty and GroupTravel
*Students may write for 2 cluster solution as well.
e. Which group is most profitable for the bank?
Cluster 3 is most profitable. (For 3 cluster solution)
• These customers prefer luxury travel and high-end experiences, meaning they
are willing to spend more on luxury accommodations, premium flight tickets,
and exclusive experiences.
********** 9 **********
--- page 10 ---
• Frequent and Spontaneous Travelers – High scores on LastMinute suggest that
they often book trips impulsively. Last-minute bookings usually come with
higher pricing and fewer discounts, increasing revenue for travel companies.
• Preference for Flights – Since these customers prioritize air travel over other
modes, they tend to book more expensive flight tickets, especially for
premium seating, business class, or direct flights.
• Adventure Enthusiasts Pay for Experiences – Travelers who score high on
Adventure often seek adventure sports, guided tours, and activity-based
packages, which are high-margin offerings for companies.
*Students may write for 2 cluster solution as well.
b Discuss the objectives of cluster analysis and its applications in business.
.
Synoptic Answer:
Q6   Clustering groups similar data points, useful in multiple business domains.
CO-
2,3;   Key Points:
BL-
1. Objective (1 mark) – Identify patterns, segment markets, detect anomalies.   [5]
Und   2. Clustering Methods (1 mark) – K-means, Hierarchical, DBSCAN.
erst   3. Applications (1 mark) – Customer segmentation, fraud detection,
recommender systems.
and   4. Example (1 mark) – E-commerce uses clustering for personalized
recommendations.
5. Business Impact (1 mark) – Enhances marketing strategies and operational
efficiency.
a Answers
Q7   Sales Revenue   3 moving
Month
($1000s)   Avg   error&2   Exp sm
CO-   Jan   200   180   400
Feb   220   194   676
1,2,
Mar   250   212.2   1428.84
3;   Apr   270   223.3333 2177.778   238.66   982.1956
BL-   May   290   246.6667 1877.778   260.598   864.4776
Jun   310   270   1600 281.1794   830.627   [1
Appl   Jul   330   290   1600 301.3538   820.6036
0]
y,   310   321.4061
Anal
yse,   Forecast
Eval   error   1813.889   857.5348
uate
Summary
Method   Forecast   MSE
3 moving   310   1813.889
********** 10 **********
--- page 11 ---
Expo sm alpha =
0.7   321.4061   857.5348
b
Answer :
Looking at ACF & PACF for raw data, it is clear that the series is stationary. See graph
below, the lags and are above zero as well as below zero indicating stationarity. There is no
need for difference for this data.
Q7
CO-
The model selection is done on the basis of following parameters
1,2,
1. Requirement of stationarity (in this case d = 0)
3;   2. BIC as low as possible
3. All lags (except intercept) need to be significant
BL-   4. Ljung-Box test should not be significant
[1
Appl   5. Residual ACF & PACF should be within the lines
0]
y,   Any simplest model that satisfies above parameters is the best model and can be used
for forecasting.
Anal   In above case
Sr   Model   BIC   Description   Result
yse,
No
Eval   1   ARIMA(1,0,0)   9.951   Correct : d=0, LB test not sig, lag sig   Model
without   problem – Residual ACF & PACF not   cannot be
uate   removing   within range   used
outliers
2   ARIMA(1,1,0)   9.648   Correct :, LB test not sig,. Residual   Model
without   ACF & PACF within range problem –   cannot be
removing   d=1, all lags not sig,   used
outliers
3   ARIMA(0,1,1)   9.591   Correct :, LB test not sig, lag sig,   Model
without   Residual ACF & PACF within range   cannot be
removing   problem – d=1   used
outliers
4   ARIMA(1,0,1)   9.997   Correct : d=1, LB test not sig,   Model
without   Residual ACF & PACF not within   cannot be
removing   range   used
outliers   problem – all lags not sig.
5   ARIMA(1,0,0)   9.456   All correct + minimum BIC + Simplest Model can
after removing   possible model   be used
outliers
********** 11 **********
--- page 12 ---
Final model chosen is ARIMA(1,0,0) after removing outliers hence company should use
following forecasts
Forecast
Model   30   31   32   33   34   35
Ethereum Forecast   2076.11 2083.18 2089.84 2096.09 2101.97 2107.51
Price in US UCL   2231.33 2298.01 2347.04 2386.30 2419.02 2446.89
$-Model_1 LCL   1925.19 1876.50 1844.19 1820.47 1802.23 1787.82
Comment on forecasts : the forecasts seems to be good as the width of 95% interval is
not too wide for initial forecasts. As the forecasting period extends, width becomes
wider making forecasts untrusted.
********** 12 **********
````
