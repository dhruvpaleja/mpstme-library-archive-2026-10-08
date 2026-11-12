# Statistical Structures in Data and Inference: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper c77fe46d2ad1

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_DS_7009/Statistical Structures in Data and Inference/ANS_Statistical Structures in Data and Inference(702DB0C039)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Statistical Structures in Data and Inference
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary.
8. All questions carry equal marks.
Q1   Answer briefly:   [20]
a. We are given P(M) = .01, so P(B) = 1 − P(M) = .99. We are also given the conditional
probabilities P(+ | M) = .80 and P(− | B) = .90, where the event − is the complement of +, thus
CO-1 ;   P(+ | B) = .10   [5]
SO- 1;   P(M/+ve)=(0.8*0.01)/(0.8*0.01)+(0.10*0.99)=0.075
BL-3
So the chance would be 7.5%. A far cry from a common estimate of 75
b.
CO- 3;
SO- 3;   [5]
BL-2
********** 1 **********
--- page 2 ---
c.
CO- 2;
SO-1;   [5]
BL-3
Reject Null hypothesis
d.   1. Linearity
Relationship between predictors (area, distance) and price should be linear
2. Independence of Errors
Residuals should be independent (no autocorrelation)
3. Homoscedasticity
Constant variance of residuals (no funnel shape in residual plot)
CO- 6;   4. Normality of Residuals   [5]
SO- 4;
BL-3   Residuals should be approximately normally distributed
5. No Multicollinearity
Independent variables should not be highly correlated (check VIF)
6. No Significant Outliers/Influential Points
Check using Cook’s distance / leverage
Even with high R² (0.85), results are valid only if these assumptions hold.
Q2   [20]
a. # Define the negative log-likelihood function
def neg_log_likelihood(params, data):
mu, sigma = params # Parameters to estimate
if sigma <= 0: # Ensure sigma is positive
return np.inf
n = len(data)
return 0.5 * n * np.log(2 * np.pi * sigma**2) + np.sum((data - mu)**2) / (2 * sigma**2)
# Initial guesses for mu and sigma
initial_guess = [np.mean(data), np.std(data)]
CO-2;   # Perform optimization
SO-2;   result = opt.minimize(neg_log_likelihood, initial_guess, args=(data,), method='L-BFGS-B',   [10]
BL-4   bounds=[(None, None), (1e-5, None)])
# Extract MLE estimates
mu_mle, sigma_mle = result.x
sigma2_mle = sigma_mle**2 # Convert sigma to variance
# Print results
print(f"MLE Estimate of Mean (μ): {mu_mle:.4f}")
print(f"MLE Estimate of Variance (σ²): {sigma2_mle:.4f}")
# Verify with Scipy's built-in function
mu_fit, sigma_fit = stats.norm.fit(data)
********** 2 **********
--- page 3 ---
print(f"Scipy Fit Mean: {mu_fit:.4f}")
print(f"Scipy Fit Variance: {sigma_fit**2:.4f}") # Convert std to variance
b. import numpy as np
from scipy import stats
before_workshop = np.array([22, 25, 18, 30, 20, 24, 28, 21])
after_workshop = np.array([25, 29, 21, 31, 26, 23, 33, 22])
differences = after_workshop - before_workshop
mean_diff = np.mean(differences)
CO-4;   std_err = stats.sem(differences) # Standard Error of the mean difference
SO-2;   # stats.ttest_rel stands for "related" samples   [10]
BL-4   t_stat, p_val = stats.ttest_rel(after_workshop, before_workshop)
print(f"Mean Improvement: {mean_diff:.2f} lines/hr")
print(f"T-Statistic:   {t_stat:.4f}")
print(f"P-Value:   {p_val:.4f}")
Mean Improvement: 2.75 lines/hr
T-Statistic:   3.3606
P-Value:   0.0121
Q3
a. # DATA LOADING & CLEANING
# Load the dataset (Ensure HR_PR.csv is in your directory)
df = pd.read_csv('HR_PR.csv')
# Handling missing values for statistical integrity
df['previous_year_rating']   =
df['previous_year_rating'].fillna(df['previous_year_rating'].median())
# ASSUMPTION TESTING (LEVENE'S TEST)
# ANOVA assumes 'Homogeneity of Variance' (equal spread across groups)
depts = df['department'].unique()
dept_groups = [df[df['department'] == d]['avg_training_score'] for d in depts]
levene_stat, p_levene = stats.levene(*dept_groups)
print("ASSUMPTION CHECK: LEVENE'S TEST ---")
print(f"Levene’s Test P-value: {p_levene:.4f}")
if p_levene < 0.05:
print("Warning: Variances are unequal (p < 0.05). Use Welch's ANOVA if needed.\n")
else:
CO-3;   print("Success: Homogeneity of variance confirmed.\n")
SO-2;   # OMNIBUS TESTING (ONE-WAY ANOVA)   [10]
BL-4   # ---------------------------------------------------------
# Question: Does 'avg_training_score' differ across ANY departments?
model = ols('avg_training_score ~ C(department)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(" ONE-WAY ANOVA RESULTS ---")
print(anova_table)
p_anova = anova_table['PR(>F)'][0]
# POST-HOC ANALYSIS (TUKEY HSD)
# If ANOVA is significant, identify which specific pairs differ.
if p_anova < 0.05:
print("\n--- 3. TUKEY HSD PAIRWISE COMPARISONS ---")
tukey = pairwise_tukeyhsd(endog=df['avg_training_score'],
groups=df['department'],
alpha=0.05)
print(tukey.summary())
# INDEPENDENT SAMPLES T-TEST (POST-TUKEY DEEP DIVE)
# Example: Comparing 'Sales' specifically against 'Technology'
# to get a direct t-statistic and p-value.
********** 3 **********
--- page 4 ---
print("\n--- 4. INDEPENDENT SAMPLES T-TEST (Sales vs. Technology) ---")
sales_scores = df[df['department'] == 'Sales']['avg_training_score']
tech_scores = df[df['department'] == 'Technology']['avg_training_score']
# Using Welch's t-test (equal_var=False) is best practice for HR data
t_stat, p_ttest = stats.ttest_ind(sales_scores, tech_scores, equal_var=False)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_ttest:.4e}")
--- 1. ASSUMPTION CHECK: LEVENE'S TEST ---
Levene’s Test P-value: 0.0000
Warning: Variances are unequal (p < 0.05). Use Welch's ANOVA if needed.
--- 2. ONE-WAY ANOVA RESULTS ---
sum_sq   df   F PR(>F)
C(department) 8.620253e+06   8.0 50075.93456   0.0
Residual   1.179162e+06 54799.0   NaN NaN
--- 3. TUKEY HSD PAIRWISE COMPARISONS ---
C:\Users\91808\AppData\Local\Temp\ipykernel_17096\2005390533.py:38: FutureWarning:
Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys
will always be treated as labels (consistent with DataFrame behavior). To access a value by
position, use `ser.iloc[pos]`
p_anova = anova_table['PR(>F)'][0]
Multiple Comparison of Means - Tukey HSD, FWER=0.05
==================================================================
==========
group1   group2   meandiff p-adj lower upper reject
----------------------------------------------------------------------------
Analytics   Finance -24.3809   0.0 -24.7278 -24.0341 True
Analytics   HR -34.5848 0.0 -34.9373 -34.2322 True
Analytics   Legal -24.7348   0.0 -25.2226 -24.247 True
Analytics   Operations -24.3763   0.0 -24.6149 -24.1377 True
Analytics   Procurement -14.4805   0.0 -14.7407 -14.2203 True
Analytics   R&D -0.0064   1.0 -0.5023 0.4896 False
Analytics Sales & Marketing -34.3413   0.0 -34.567 -34.1155 True
Analytics   Technology -4.6743   0.0 -4.9344 -4.4141 True
Finance   HR -10.2038   0.0 -10.6128 -9.7948 True
Finance   Legal -0.3539 0.4934 -0.8839 0.1761 False
Finance   Operations 0.0046   1.0 -0.3114 0.3207 False
Finance   Procurement 9.9004   0.0 9.5678 10.2331 True
Finance   R&D 24.3746   0.0 23.8371 24.9121 True
Finance Sales & Marketing -9.9603   0.0 -10.2668 -9.6538 True
Finance   Technology 19.7067   0.0 19.3741 20.0393 True
HR   Legal 9.8499   0.0 9.3162 10.3837 True
HR   Operations 10.2085   0.0 9.8862 10.5307 True
HR   Procurement 20.1042   0.0 19.7657 20.4428 True
HR   R&D 34.5784   0.0 34.0372 35.1196 True
HR Sales & Marketing 0.2435 0.2762 -0.0694 0.5564 False
HR   Technology 29.9105 0.0 29.5719 30.2491 True
Legal   Operations 0.3585 0.2924 -0.1079 0.8249 False
Legal   Procurement 10.2543   0.0 9.7765 10.7321 True
Legal   R&D 24.7285 0.0 24.0909 25.366 True
Legal Sales & Marketing -9.6064   0.0 -10.0664 -9.1465 True
Legal   Technology 20.0605   0.0 19.5828 20.5383 True
Operations   Procurement 9.8958   0.0 9.6784 10.1132 True
Operations   R&D 24.3699   0.0 23.8951 24.8448 True
Operations Sales & Marketing -9.9649   0.0 -10.1397 -9.7902 True
Operations   Technology 19.702   0.0 19.4847 19.9194 True
Procurement   R&D 14.4742 0.0 13.9881 14.9602 True
Procurement Sales & Marketing -19.8607   0.0 -20.064 -19.6575 True
********** 4 **********
--- page 5 ---
Procurement   Technology 9.8062   0.0 9.5654 10.0471 True
R&D Sales & Marketing -34.3349   0.0 -34.8034 -33.8664 True
R&D   Technology -4.6679   0.0 -5.154 -4.1819 True
Sales & Marketing   Technology 29.667   0.0 29.4638 29.8702 True
----------------------------------------------------------------------------
b. def negative_log_likelihood(params, data):
mu, sigma = params
if sigma <= 0:
return np.inf
return -np.sum(stats.norm.logpdf(data, loc=mu, scale=sigma))
results = {}
for grp in df['group'].unique():
data_grp = df[df['group'] == grp]['values'].values
# Initial guess
init = [np.mean(data_grp), np.std(data_grp)]
CO-1;
SO-1;   # Optimization   [10]
BL-3   result = opt.minimize(negative_log_likelihood, init, args=(data_grp,))
mu_mle, sigma_mle = result.x
# Analytical
mu_analytical = np.mean(data_grp)
sigma_analytical = np.sqrt(np.mean((data_grp - mu_analytical)**2))
df = pd.DataFrame({
'outcome': np.concatenate([group_A, group_B]),
'group': ['A']*120 + ['B']*120
})
Q4   [20]
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from statsmodels.stats.outliers_influence import variance_inflation_factor
CO-4;   # 1. LOAD DATA
SO-6;   # Dataset: R&D Spend, Administration, Marketing Spend, State, Profit
BL-3   df = pd.read_csv('50_Startups.csv')
# 2. HANDLE CATEGORICAL DATA (The State Column)
# We use drop_first=True to avoid the Dummy Variable Trap.
# If we have 3 states, we only need 2 columns to represent them.
df_final = pd.get_dummies(df, columns=['State'], drop_first=True)
# 3. DEFINE FEATURES AND TARGET
********** 5 **********
--- page 6 ---
X = df_final.drop('Profit', axis=1)
y = df_final['Profit']
# FIX 1: Ensure all data is numeric (converts True/False to 1/0 and strings to numbers)
X = X.astype(float)
# FIX 2: Check for any stray NAs that might have been created
X = X.fillna(0)
# 4. MULTICOLLINEARITY CHECK (VIF)
# VIF measures how much a variable is predicted by other variables.
# VIF > 5-10 suggests high multicollinearity.
def calculate_vif(X_data):
vif_df = pd.DataFrame()
vif_df["Feature"] = X_data.columns
# Adding a constant is required for statsmodels VIF calculation
X_with_const = sm.add_constant(X_data)
vif_df["VIF"] = [variance_inflation_factor(X_with_const.values, i+1)
for i in range(len(X_data.columns))]
return vif_df
print("--- Variance Inflation Factors ---")
print(calculate_vif(X))
# 5. BUILDING THE MODEL (Using statsmodels for detailed p-values)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_const = sm.add_constant(X_train) # Adding the intercept (B0)
model = sm.OLS(y_train, X_train_const).fit()
# 6. OUTPUT RESULTS
print("\n--- Model Summary ---")
print(model.summary())
--- Variance Inflation Factors ---
Feature   VIF
0   R&D Spend 2.495511
1 Administration 1.177766
2 Marketing Spend 2.416797
3   State_Florida 1.387641
4 State_New York 1.335061
--- Model Summary ---
OLS Regression Results
==================================================================
============
Dep. Variable:   Profit R-squared:   0.954
Model:   OLS Adj. R-squared:   0.947
Method:   Least Squares F-statistic:   140.1
Date:   Sun, 22 Mar 2026 Prob (F-statistic):   1.13e-21
Time:   12:09:40 Log-Likelihood:   -420.63
No. Observations:   40 AIC:   853.3
Df Residuals:   34 BIC:   863.4
Df Model:   5
Covariance Type:   nonrobust
==================================================================
=================
coef   std err   t   P>|t|   [0.025   0.975]
-----------------------------------------------------------------------------------
********** 6 **********
--- page 7 ---
const   5.403e+04 8457.293   6.388   0.000 3.68e+04 7.12e+04
R&D Spend   0.8056   0.052   15.383   0.000   0.699   0.912
Administration   -0.0688   0.061   -1.133   0.265   -0.192   0.055
Marketing Spend   0.0299   0.022   1.346   0.187   -0.015   0.075
State_Florida   938.7930 3893.511   0.241   0.811 -6973.773 8851.359
State_New York   6.9878 3882.765   0.002   0.999 -7883.740 7897.715
==================================================================
============
Omnibus:   15.391 Durbin-Watson:   1.751
Prob(Omnibus):   0.000 Jarque-Bera (JB):   20.231
Skew:   -1.142 Prob(JB):   4.05e-05
Kurtosis:   5.631 Cond. No.   1.64e+06
==================================================================
============
Q5   [20]
a.
CO-1;
SO-2;   10
BL-4
********** 7 **********
--- page 8 ---
b.
CO-7;
SO-1;   10
BL-3
Q 6   [20]
a. import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# 1. Prepare Data
df = pd.read_csv('Fuel_Efficiency.csv')
X = df[['Engine_Speed']] # FIX: Double brackets for 2D shape
y = df['Efficiency']
# Simple Linear Regression (The Baseline)
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_lin_pred = lin_reg.predict(X)
CO-4;   # 2. Polynomial Transformation (Degree 2)   [10]
SO-1;   poly_features = PolynomialFeatures(degree=2, include_bias=False)
BL-3   X_poly = poly_features.fit_transform(X)
# 3. Fit Polynomial Regression
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
y_poly_pred = poly_reg.predict(X_poly)
# 4. Diagnostics & Comparison
print(f"Linear Model MSE: {mean_squared_error(y, y_lin_pred):.2f}")
print(f"Polynomial Model MSE: {mean_squared_error(y, y_poly_pred):.2f}")
print(f"Linear Model R2: {r2_score(y, y_lin_pred):.4f}")
print(f"Polynomial Model R2: {r2_score(y, y_poly_pred):.4f}")
# 5. Visual Check
# We use values.min() and values.max() to ensure we get the underlying numbers
X_grid = np.arange(X.values.min(), X.values.max(), 0.1).reshape(-1, 1)
********** 8 **********
--- page 9 ---
plt.scatter(X, y, color='blue', alpha=0.5, label='Actual Data')
plt.plot(X_grid, lin_reg.predict(X_grid), color='red', label='Linear Fit')
plt.plot(X_grid,   poly_reg.predict(poly_features.transform(X_grid)),   color='green',
label='Polynomial Fit')
plt.title('Fuel Efficiency: Linear vs. Polynomial Regression')
plt.xlabel('Engine Speed')
plt.ylabel('Efficiency')
plt.legend()
plt.show()
Linear Model MSE: 19.36
Polynomial Model MSE: 3.11
Linear Model R2: 0.5878
Polynomial Model R2: 0.9338
b. L1vs.L2: Because the L1 penalty is the absolute value, its derivative is a constant (+/-1) rather
than a term that depends on the size of the coefficient (beta). This means Lasso applies a
constant pressure to pull coefficients to zero. In a two-dimensional space, the constraint region
for Ridge is a circle, while for Lasso, it is a diamond (rhombus). The "corners" of the diamond
sit on the axes. When the RSS ellipses expand, they are highly likely to hit a corner first,
setting the other variable's coefficient to exactly 0.
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
# 1. SPLIT & SCALE (Lasso is extremely sensitive to scale)
CO-5;   X_clean=pd.read_csv('House_price.csv')
SO-2;   X_train, X_test, y_train, y_test = train_test_split(X_clean, y, test_size=0.2, random_state=42)   [10]
BL-4
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# 2. RUN LASSOCV
# We provide a range of alphas. LassoCV uses 5-fold CV by default.
lasso_mod = LassoCV(alphas=np.logspace(-4, -1, 50), cv=5, max_iter=10000)
lasso_mod.fit(X_train_scaled, y_train)
# 3. EVALUATE
y_pred = lasso_mod.predict(X_test_scaled)
********** 9 **********
--- page 10 ---
print(f"Optimal Alpha (Lambda): {lasso_mod.alpha_:.6f}")
print(f"R-squared: {r2_score(y_test, y_pred):.4f}")
# 4. DEMONSTRATE FEATURE SELECTION
total_features = X_clean.shape[1]
active_features = np.sum(lasso_mod.coef_ != 0)
removed_features = total_features - active_features
print(f"\nTotal Features: {total_features}")
print(f"Features Retained by Lasso: {active_features}")
print(f"Features Dropped (set to 0): {removed_features}")
Optimal Alpha (Lambda): 0.010481
R-squared: 0.8783
Total Features: 260
Features Retained by Lasso: 54
Features Dropped (set to 0): 206
Q 7   [20]
a. import numpy as np
from scipy import stats
group1 = np.array([18, 15, 14, 19, 16])
group2 = np.array([12, 14, 11, 15, 13])
mean1, mean2 = np.mean(group1), np.mean(group2)
std1, std2 = np.std(group1, ddof=1), np.array(group2).std(ddof=1)
n1, n2 = len(group1), len(group2)
# 3. Calculate Pooled Standard Deviation (for equal variance)
CO-2;   df = n1 + n2 - 2
SO-1;   pooled_var = ((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / df   [10]
BL-3   t_stat_manual = (mean1 - mean2) / np.sqrt(pooled_var * (1/n1 + 1/n2))
t_stat, p_val = stats.ttest_ind(group1, group2)
print(f"Group 1 Mean: {mean1} | Group 2 Mean: {mean2}")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val:.4f}")
Group 1 Mean: 16.4 | Group 2 Mean: 13.0
T-Statistic: 2.9155
P-Value: 0.0194
b. import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Source: HR Analytics Promotion Dataset (train.csv)
df = pd.read_csv('train.csv')
df['previous_year_rating']   =
df['previous_year_rating'].fillna(df['previous_year_rating'].median())
CO-6;   # Target is 'is_promoted' (1 for Yes, 0 for No)
SO-2;   features = ['age', 'avg_training_score', 'length_of_service', 'KPIs_met >80%', 'awards_won?']   [10]
BL-4   X = df[features]
y = df['is_promoted']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))
# Profile: Age 28, Score 85, Service 3, KPI Yes (1), Awards Yes (1)
candidate = pd.DataFrame([[28, 85, 3, 1, 1]], columns=features)
promotion_prob = model.predict_proba(candidate)[0][1]
********** 10 **********
--- page 11 ---
print(f"Train Accuracy: {train_acc:.2%}")
print(f"Test Accuracy: {test_acc:.2%}")
print(f"Candidate Promotion Probability: {promotion_prob:.2%}")
Train Accuracy: 95.14%
Test Accuracy: 90.90%
Candidate Promotion Probability: 25.00%
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper aaca742bb718

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_DS_7052/Statistical Structures in Data and Inference/ANS_Statistical Structures in Data and Inference(702DB0C039)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Statistical Structures in Data and Inference
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary.
8. All questions carry equal marks.
Q1   Answer briefly:   [20]
a. We are given P(M) = .01, so P(B) = 1 − P(M) = .99. We are also given the conditional
probabilities P(+ | M) = .80 and P(− | B) = .90, where the event − is the complement of +, thus
CO-1 ;   P(+ | B) = .10   [5]
SO- 1;   P(M/+ve)=(0.8*0.01)/(0.8*0.01)+(0.10*0.99)=0.075
BL-3
So the chance would be 7.5%. A far cry from a common estimate of 75
b.
CO- 3;
SO- 3;   [5]
BL-2
********** 1 **********
--- page 2 ---
c.
CO- 2;
SO-1;   [5]
BL-3
Reject Null hypothesis
d.   1. Linearity
Relationship between predictors (area, distance) and price should be linear
2. Independence of Errors
Residuals should be independent (no autocorrelation)
3. Homoscedasticity
Constant variance of residuals (no funnel shape in residual plot)
CO- 6;   4. Normality of Residuals   [5]
SO- 4;
BL-3   Residuals should be approximately normally distributed
5. No Multicollinearity
Independent variables should not be highly correlated (check VIF)
6. No Significant Outliers/Influential Points
Check using Cook’s distance / leverage
Even with high R² (0.85), results are valid only if these assumptions hold.
Q2   [20]
a. # Define the negative log-likelihood function
def neg_log_likelihood(params, data):
mu, sigma = params # Parameters to estimate
if sigma <= 0: # Ensure sigma is positive
return np.inf
n = len(data)
return 0.5 * n * np.log(2 * np.pi * sigma**2) + np.sum((data - mu)**2) / (2 * sigma**2)
# Initial guesses for mu and sigma
initial_guess = [np.mean(data), np.std(data)]
CO-2;   # Perform optimization
SO-2;   result = opt.minimize(neg_log_likelihood, initial_guess, args=(data,), method='L-BFGS-B',   [10]
BL-4   bounds=[(None, None), (1e-5, None)])
# Extract MLE estimates
mu_mle, sigma_mle = result.x
sigma2_mle = sigma_mle**2 # Convert sigma to variance
# Print results
print(f"MLE Estimate of Mean (μ): {mu_mle:.4f}")
print(f"MLE Estimate of Variance (σ²): {sigma2_mle:.4f}")
# Verify with Scipy's built-in function
mu_fit, sigma_fit = stats.norm.fit(data)
********** 2 **********
--- page 3 ---
print(f"Scipy Fit Mean: {mu_fit:.4f}")
print(f"Scipy Fit Variance: {sigma_fit**2:.4f}") # Convert std to variance
b. import numpy as np
from scipy import stats
before_workshop = np.array([22, 25, 18, 30, 20, 24, 28, 21])
after_workshop = np.array([25, 29, 21, 31, 26, 23, 33, 22])
differences = after_workshop - before_workshop
mean_diff = np.mean(differences)
CO-4;   std_err = stats.sem(differences) # Standard Error of the mean difference
SO-2;   # stats.ttest_rel stands for "related" samples   [10]
BL-4   t_stat, p_val = stats.ttest_rel(after_workshop, before_workshop)
print(f"Mean Improvement: {mean_diff:.2f} lines/hr")
print(f"T-Statistic:   {t_stat:.4f}")
print(f"P-Value:   {p_val:.4f}")
Mean Improvement: 2.75 lines/hr
T-Statistic:   3.3606
P-Value:   0.0121
Q3
a. # DATA LOADING & CLEANING
# Load the dataset (Ensure HR_PR.csv is in your directory)
df = pd.read_csv('HR_PR.csv')
# Handling missing values for statistical integrity
df['previous_year_rating']   =
df['previous_year_rating'].fillna(df['previous_year_rating'].median())
# ASSUMPTION TESTING (LEVENE'S TEST)
# ANOVA assumes 'Homogeneity of Variance' (equal spread across groups)
depts = df['department'].unique()
dept_groups = [df[df['department'] == d]['avg_training_score'] for d in depts]
levene_stat, p_levene = stats.levene(*dept_groups)
print("ASSUMPTION CHECK: LEVENE'S TEST ---")
print(f"Levene’s Test P-value: {p_levene:.4f}")
if p_levene < 0.05:
print("Warning: Variances are unequal (p < 0.05). Use Welch's ANOVA if needed.\n")
else:
CO-3;   print("Success: Homogeneity of variance confirmed.\n")
SO-2;   # OMNIBUS TESTING (ONE-WAY ANOVA)   [10]
BL-4   # ---------------------------------------------------------
# Question: Does 'avg_training_score' differ across ANY departments?
model = ols('avg_training_score ~ C(department)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(" ONE-WAY ANOVA RESULTS ---")
print(anova_table)
p_anova = anova_table['PR(>F)'][0]
# POST-HOC ANALYSIS (TUKEY HSD)
# If ANOVA is significant, identify which specific pairs differ.
if p_anova < 0.05:
print("\n--- 3. TUKEY HSD PAIRWISE COMPARISONS ---")
tukey = pairwise_tukeyhsd(endog=df['avg_training_score'],
groups=df['department'],
alpha=0.05)
print(tukey.summary())
# INDEPENDENT SAMPLES T-TEST (POST-TUKEY DEEP DIVE)
# Example: Comparing 'Sales' specifically against 'Technology'
# to get a direct t-statistic and p-value.
********** 3 **********
--- page 4 ---
print("\n--- 4. INDEPENDENT SAMPLES T-TEST (Sales vs. Technology) ---")
sales_scores = df[df['department'] == 'Sales']['avg_training_score']
tech_scores = df[df['department'] == 'Technology']['avg_training_score']
# Using Welch's t-test (equal_var=False) is best practice for HR data
t_stat, p_ttest = stats.ttest_ind(sales_scores, tech_scores, equal_var=False)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_ttest:.4e}")
--- 1. ASSUMPTION CHECK: LEVENE'S TEST ---
Levene’s Test P-value: 0.0000
Warning: Variances are unequal (p < 0.05). Use Welch's ANOVA if needed.
--- 2. ONE-WAY ANOVA RESULTS ---
sum_sq   df   F PR(>F)
C(department) 8.620253e+06   8.0 50075.93456   0.0
Residual   1.179162e+06 54799.0   NaN NaN
--- 3. TUKEY HSD PAIRWISE COMPARISONS ---
C:\Users\91808\AppData\Local\Temp\ipykernel_17096\2005390533.py:38: FutureWarning:
Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys
will always be treated as labels (consistent with DataFrame behavior). To access a value by
position, use `ser.iloc[pos]`
p_anova = anova_table['PR(>F)'][0]
Multiple Comparison of Means - Tukey HSD, FWER=0.05
==================================================================
==========
group1   group2   meandiff p-adj lower upper reject
----------------------------------------------------------------------------
Analytics   Finance -24.3809   0.0 -24.7278 -24.0341 True
Analytics   HR -34.5848 0.0 -34.9373 -34.2322 True
Analytics   Legal -24.7348   0.0 -25.2226 -24.247 True
Analytics   Operations -24.3763   0.0 -24.6149 -24.1377 True
Analytics   Procurement -14.4805   0.0 -14.7407 -14.2203 True
Analytics   R&D -0.0064   1.0 -0.5023 0.4896 False
Analytics Sales & Marketing -34.3413   0.0 -34.567 -34.1155 True
Analytics   Technology -4.6743   0.0 -4.9344 -4.4141 True
Finance   HR -10.2038   0.0 -10.6128 -9.7948 True
Finance   Legal -0.3539 0.4934 -0.8839 0.1761 False
Finance   Operations 0.0046   1.0 -0.3114 0.3207 False
Finance   Procurement 9.9004   0.0 9.5678 10.2331 True
Finance   R&D 24.3746   0.0 23.8371 24.9121 True
Finance Sales & Marketing -9.9603   0.0 -10.2668 -9.6538 True
Finance   Technology 19.7067   0.0 19.3741 20.0393 True
HR   Legal 9.8499   0.0 9.3162 10.3837 True
HR   Operations 10.2085   0.0 9.8862 10.5307 True
HR   Procurement 20.1042   0.0 19.7657 20.4428 True
HR   R&D 34.5784   0.0 34.0372 35.1196 True
HR Sales & Marketing 0.2435 0.2762 -0.0694 0.5564 False
HR   Technology 29.9105 0.0 29.5719 30.2491 True
Legal   Operations 0.3585 0.2924 -0.1079 0.8249 False
Legal   Procurement 10.2543   0.0 9.7765 10.7321 True
Legal   R&D 24.7285 0.0 24.0909 25.366 True
Legal Sales & Marketing -9.6064   0.0 -10.0664 -9.1465 True
Legal   Technology 20.0605   0.0 19.5828 20.5383 True
Operations   Procurement 9.8958   0.0 9.6784 10.1132 True
Operations   R&D 24.3699   0.0 23.8951 24.8448 True
Operations Sales & Marketing -9.9649   0.0 -10.1397 -9.7902 True
Operations   Technology 19.702   0.0 19.4847 19.9194 True
Procurement   R&D 14.4742 0.0 13.9881 14.9602 True
Procurement Sales & Marketing -19.8607   0.0 -20.064 -19.6575 True
********** 4 **********
--- page 5 ---
Procurement   Technology 9.8062   0.0 9.5654 10.0471 True
R&D Sales & Marketing -34.3349   0.0 -34.8034 -33.8664 True
R&D   Technology -4.6679   0.0 -5.154 -4.1819 True
Sales & Marketing   Technology 29.667   0.0 29.4638 29.8702 True
----------------------------------------------------------------------------
b. def negative_log_likelihood(params, data):
mu, sigma = params
if sigma <= 0:
return np.inf
return -np.sum(stats.norm.logpdf(data, loc=mu, scale=sigma))
results = {}
for grp in df['group'].unique():
data_grp = df[df['group'] == grp]['values'].values
# Initial guess
init = [np.mean(data_grp), np.std(data_grp)]
CO-1;
SO-1;   # Optimization   [10]
BL-3   result = opt.minimize(negative_log_likelihood, init, args=(data_grp,))
mu_mle, sigma_mle = result.x
# Analytical
mu_analytical = np.mean(data_grp)
sigma_analytical = np.sqrt(np.mean((data_grp - mu_analytical)**2))
df = pd.DataFrame({
'outcome': np.concatenate([group_A, group_B]),
'group': ['A']*120 + ['B']*120
})
Q4   [20]
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from statsmodels.stats.outliers_influence import variance_inflation_factor
CO-4;   # 1. LOAD DATA
SO-6;   # Dataset: R&D Spend, Administration, Marketing Spend, State, Profit
BL-3   df = pd.read_csv('50_Startups.csv')
# 2. HANDLE CATEGORICAL DATA (The State Column)
# We use drop_first=True to avoid the Dummy Variable Trap.
# If we have 3 states, we only need 2 columns to represent them.
df_final = pd.get_dummies(df, columns=['State'], drop_first=True)
# 3. DEFINE FEATURES AND TARGET
********** 5 **********
--- page 6 ---
X = df_final.drop('Profit', axis=1)
y = df_final['Profit']
# FIX 1: Ensure all data is numeric (converts True/False to 1/0 and strings to numbers)
X = X.astype(float)
# FIX 2: Check for any stray NAs that might have been created
X = X.fillna(0)
# 4. MULTICOLLINEARITY CHECK (VIF)
# VIF measures how much a variable is predicted by other variables.
# VIF > 5-10 suggests high multicollinearity.
def calculate_vif(X_data):
vif_df = pd.DataFrame()
vif_df["Feature"] = X_data.columns
# Adding a constant is required for statsmodels VIF calculation
X_with_const = sm.add_constant(X_data)
vif_df["VIF"] = [variance_inflation_factor(X_with_const.values, i+1)
for i in range(len(X_data.columns))]
return vif_df
print("--- Variance Inflation Factors ---")
print(calculate_vif(X))
# 5. BUILDING THE MODEL (Using statsmodels for detailed p-values)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_const = sm.add_constant(X_train) # Adding the intercept (B0)
model = sm.OLS(y_train, X_train_const).fit()
# 6. OUTPUT RESULTS
print("\n--- Model Summary ---")
print(model.summary())
--- Variance Inflation Factors ---
Feature   VIF
0   R&D Spend 2.495511
1 Administration 1.177766
2 Marketing Spend 2.416797
3   State_Florida 1.387641
4 State_New York 1.335061
--- Model Summary ---
OLS Regression Results
==================================================================
============
Dep. Variable:   Profit R-squared:   0.954
Model:   OLS Adj. R-squared:   0.947
Method:   Least Squares F-statistic:   140.1
Date:   Sun, 22 Mar 2026 Prob (F-statistic):   1.13e-21
Time:   12:09:40 Log-Likelihood:   -420.63
No. Observations:   40 AIC:   853.3
Df Residuals:   34 BIC:   863.4
Df Model:   5
Covariance Type:   nonrobust
==================================================================
=================
coef   std err   t   P>|t|   [0.025   0.975]
-----------------------------------------------------------------------------------
********** 6 **********
--- page 7 ---
const   5.403e+04 8457.293   6.388   0.000 3.68e+04 7.12e+04
R&D Spend   0.8056   0.052   15.383   0.000   0.699   0.912
Administration   -0.0688   0.061   -1.133   0.265   -0.192   0.055
Marketing Spend   0.0299   0.022   1.346   0.187   -0.015   0.075
State_Florida   938.7930 3893.511   0.241   0.811 -6973.773 8851.359
State_New York   6.9878 3882.765   0.002   0.999 -7883.740 7897.715
==================================================================
============
Omnibus:   15.391 Durbin-Watson:   1.751
Prob(Omnibus):   0.000 Jarque-Bera (JB):   20.231
Skew:   -1.142 Prob(JB):   4.05e-05
Kurtosis:   5.631 Cond. No.   1.64e+06
==================================================================
============
Q5   [20]
a.
CO-1;
SO-2;   10
BL-4
********** 7 **********
--- page 8 ---
b.
CO-7;
SO-1;   10
BL-3
Q 6   [20]
a. import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# 1. Prepare Data
df = pd.read_csv('Fuel_Efficiency.csv')
X = df[['Engine_Speed']] # FIX: Double brackets for 2D shape
y = df['Efficiency']
# Simple Linear Regression (The Baseline)
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_lin_pred = lin_reg.predict(X)
CO-4;   # 2. Polynomial Transformation (Degree 2)   [10]
SO-1;   poly_features = PolynomialFeatures(degree=2, include_bias=False)
BL-3   X_poly = poly_features.fit_transform(X)
# 3. Fit Polynomial Regression
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
y_poly_pred = poly_reg.predict(X_poly)
# 4. Diagnostics & Comparison
print(f"Linear Model MSE: {mean_squared_error(y, y_lin_pred):.2f}")
print(f"Polynomial Model MSE: {mean_squared_error(y, y_poly_pred):.2f}")
print(f"Linear Model R2: {r2_score(y, y_lin_pred):.4f}")
print(f"Polynomial Model R2: {r2_score(y, y_poly_pred):.4f}")
# 5. Visual Check
# We use values.min() and values.max() to ensure we get the underlying numbers
X_grid = np.arange(X.values.min(), X.values.max(), 0.1).reshape(-1, 1)
********** 8 **********
--- page 9 ---
plt.scatter(X, y, color='blue', alpha=0.5, label='Actual Data')
plt.plot(X_grid, lin_reg.predict(X_grid), color='red', label='Linear Fit')
plt.plot(X_grid,   poly_reg.predict(poly_features.transform(X_grid)),   color='green',
label='Polynomial Fit')
plt.title('Fuel Efficiency: Linear vs. Polynomial Regression')
plt.xlabel('Engine Speed')
plt.ylabel('Efficiency')
plt.legend()
plt.show()
Linear Model MSE: 19.36
Polynomial Model MSE: 3.11
Linear Model R2: 0.5878
Polynomial Model R2: 0.9338
b. L1vs.L2: Because the L1 penalty is the absolute value, its derivative is a constant (+/-1) rather
than a term that depends on the size of the coefficient (beta). This means Lasso applies a
constant pressure to pull coefficients to zero. In a two-dimensional space, the constraint region
for Ridge is a circle, while for Lasso, it is a diamond (rhombus). The "corners" of the diamond
sit on the axes. When the RSS ellipses expand, they are highly likely to hit a corner first,
setting the other variable's coefficient to exactly 0.
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
# 1. SPLIT & SCALE (Lasso is extremely sensitive to scale)
CO-5;   X_clean=pd.read_csv('House_price.csv')
SO-2;   X_train, X_test, y_train, y_test = train_test_split(X_clean, y, test_size=0.2, random_state=42)   [10]
BL-4
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# 2. RUN LASSOCV
# We provide a range of alphas. LassoCV uses 5-fold CV by default.
lasso_mod = LassoCV(alphas=np.logspace(-4, -1, 50), cv=5, max_iter=10000)
lasso_mod.fit(X_train_scaled, y_train)
# 3. EVALUATE
y_pred = lasso_mod.predict(X_test_scaled)
********** 9 **********
--- page 10 ---
print(f"Optimal Alpha (Lambda): {lasso_mod.alpha_:.6f}")
print(f"R-squared: {r2_score(y_test, y_pred):.4f}")
# 4. DEMONSTRATE FEATURE SELECTION
total_features = X_clean.shape[1]
active_features = np.sum(lasso_mod.coef_ != 0)
removed_features = total_features - active_features
print(f"\nTotal Features: {total_features}")
print(f"Features Retained by Lasso: {active_features}")
print(f"Features Dropped (set to 0): {removed_features}")
Optimal Alpha (Lambda): 0.010481
R-squared: 0.8783
Total Features: 260
Features Retained by Lasso: 54
Features Dropped (set to 0): 206
Q 7   [20]
a. import numpy as np
from scipy import stats
group1 = np.array([18, 15, 14, 19, 16])
group2 = np.array([12, 14, 11, 15, 13])
mean1, mean2 = np.mean(group1), np.mean(group2)
std1, std2 = np.std(group1, ddof=1), np.array(group2).std(ddof=1)
n1, n2 = len(group1), len(group2)
# 3. Calculate Pooled Standard Deviation (for equal variance)
CO-2;   df = n1 + n2 - 2
SO-1;   pooled_var = ((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / df   [10]
BL-3   t_stat_manual = (mean1 - mean2) / np.sqrt(pooled_var * (1/n1 + 1/n2))
t_stat, p_val = stats.ttest_ind(group1, group2)
print(f"Group 1 Mean: {mean1} | Group 2 Mean: {mean2}")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val:.4f}")
Group 1 Mean: 16.4 | Group 2 Mean: 13.0
T-Statistic: 2.9155
P-Value: 0.0194
b. import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Source: HR Analytics Promotion Dataset (train.csv)
df = pd.read_csv('train.csv')
df['previous_year_rating']   =
df['previous_year_rating'].fillna(df['previous_year_rating'].median())
CO-6;   # Target is 'is_promoted' (1 for Yes, 0 for No)
SO-2;   features = ['age', 'avg_training_score', 'length_of_service', 'KPIs_met >80%', 'awards_won?']   [10]
BL-4   X = df[features]
y = df['is_promoted']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))
# Profile: Age 28, Score 85, Service 3, KPI Yes (1), Awards Yes (1)
candidate = pd.DataFrame([[28, 85, 3, 1, 1]], columns=features)
promotion_prob = model.predict_proba(candidate)[0][1]
********** 10 **********
--- page 11 ---
print(f"Train Accuracy: {train_acc:.2%}")
print(f"Test Accuracy: {test_acc:.2%}")
print(f"Candidate Promotion Probability: {promotion_prob:.2%}")
Train Accuracy: 95.14%
Test Accuracy: 90.90%
Candidate Promotion Probability: 25.00%
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 20e067027a9f

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_DS_7038/Statistical Structures in Data and Inference/ANS_Statistical Structures in Data and Inference(702DB0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Statistical Structures in Data and Inference
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. Assume Suitable data if necessary.
8. All questions carry equal marks.
Q1   Answer briefly:   [20]
a. We are given P(M) = .01, so P(B) = 1 − P(M) = .99. We are also given the conditional
probabilities P(+ | M) = .80 and P(− | B) = .90, where the event − is the complement of +, thus
CO-1 ;   P(+ | B) = .10   [5]
SO- 1;   P(M/+ve)=(0.8*0.01)/(0.8*0.01)+(0.10*0.99)=0.075
BL-3
So the chance would be 7.5%. A far cry from a common estimate of 75
b.
CO- 3;
SO- 3;   [5]
BL-2
********** 1 **********
--- page 2 ---
c.
CO- 2;
SO-1;   [5]
BL-3
Reject Null hypothesis
d.   1. Linearity
Relationship between predictors (area, distance) and price should be linear
2. Independence of Errors
Residuals should be independent (no autocorrelation)
3. Homoscedasticity
Constant variance of residuals (no funnel shape in residual plot)
CO- 6;   4. Normality of Residuals   [5]
SO- 4;
BL-3   Residuals should be approximately normally distributed
5. No Multicollinearity
Independent variables should not be highly correlated (check VIF)
6. No Significant Outliers/Influential Points
Check using Cook’s distance / leverage
Even with high R² (0.85), results are valid only if these assumptions hold.
Q2   [20]
a. # Define the negative log-likelihood function
def neg_log_likelihood(params, data):
mu, sigma = params # Parameters to estimate
if sigma <= 0: # Ensure sigma is positive
return np.inf
n = len(data)
return 0.5 * n * np.log(2 * np.pi * sigma**2) + np.sum((data - mu)**2) / (2 * sigma**2)
# Initial guesses for mu and sigma
initial_guess = [np.mean(data), np.std(data)]
CO-2;   # Perform optimization
SO-2;   result = opt.minimize(neg_log_likelihood, initial_guess, args=(data,), method='L-BFGS-B',   [10]
BL-4   bounds=[(None, None), (1e-5, None)])
# Extract MLE estimates
mu_mle, sigma_mle = result.x
sigma2_mle = sigma_mle**2 # Convert sigma to variance
# Print results
print(f"MLE Estimate of Mean (μ): {mu_mle:.4f}")
print(f"MLE Estimate of Variance (σ²): {sigma2_mle:.4f}")
# Verify with Scipy's built-in function
mu_fit, sigma_fit = stats.norm.fit(data)
********** 2 **********
--- page 3 ---
print(f"Scipy Fit Mean: {mu_fit:.4f}")
print(f"Scipy Fit Variance: {sigma_fit**2:.4f}") # Convert std to variance
b. import numpy as np
from scipy import stats
before_workshop = np.array([22, 25, 18, 30, 20, 24, 28, 21])
after_workshop = np.array([25, 29, 21, 31, 26, 23, 33, 22])
differences = after_workshop - before_workshop
mean_diff = np.mean(differences)
CO-4;   std_err = stats.sem(differences) # Standard Error of the mean difference
SO-2;   # stats.ttest_rel stands for "related" samples   [10]
BL-4   t_stat, p_val = stats.ttest_rel(after_workshop, before_workshop)
print(f"Mean Improvement: {mean_diff:.2f} lines/hr")
print(f"T-Statistic:   {t_stat:.4f}")
print(f"P-Value:   {p_val:.4f}")
Mean Improvement: 2.75 lines/hr
T-Statistic:   3.3606
P-Value:   0.0121
Q3
a. # DATA LOADING & CLEANING
# Load the dataset (Ensure HR_PR.csv is in your directory)
df = pd.read_csv('HR_PR.csv')
# Handling missing values for statistical integrity
df['previous_year_rating']   =
df['previous_year_rating'].fillna(df['previous_year_rating'].median())
# ASSUMPTION TESTING (LEVENE'S TEST)
# ANOVA assumes 'Homogeneity of Variance' (equal spread across groups)
depts = df['department'].unique()
dept_groups = [df[df['department'] == d]['avg_training_score'] for d in depts]
levene_stat, p_levene = stats.levene(*dept_groups)
print("ASSUMPTION CHECK: LEVENE'S TEST ---")
print(f"Levene’s Test P-value: {p_levene:.4f}")
if p_levene < 0.05:
print("Warning: Variances are unequal (p < 0.05). Use Welch's ANOVA if needed.\n")
else:
CO-3;   print("Success: Homogeneity of variance confirmed.\n")
SO-2;   # OMNIBUS TESTING (ONE-WAY ANOVA)   [10]
BL-4   # ---------------------------------------------------------
# Question: Does 'avg_training_score' differ across ANY departments?
model = ols('avg_training_score ~ C(department)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(" ONE-WAY ANOVA RESULTS ---")
print(anova_table)
p_anova = anova_table['PR(>F)'][0]
# POST-HOC ANALYSIS (TUKEY HSD)
# If ANOVA is significant, identify which specific pairs differ.
if p_anova < 0.05:
print("\n--- 3. TUKEY HSD PAIRWISE COMPARISONS ---")
tukey = pairwise_tukeyhsd(endog=df['avg_training_score'],
groups=df['department'],
alpha=0.05)
print(tukey.summary())
# INDEPENDENT SAMPLES T-TEST (POST-TUKEY DEEP DIVE)
# Example: Comparing 'Sales' specifically against 'Technology'
# to get a direct t-statistic and p-value.
********** 3 **********
--- page 4 ---
print("\n--- 4. INDEPENDENT SAMPLES T-TEST (Sales vs. Technology) ---")
sales_scores = df[df['department'] == 'Sales']['avg_training_score']
tech_scores = df[df['department'] == 'Technology']['avg_training_score']
# Using Welch's t-test (equal_var=False) is best practice for HR data
t_stat, p_ttest = stats.ttest_ind(sales_scores, tech_scores, equal_var=False)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_ttest:.4e}")
--- 1. ASSUMPTION CHECK: LEVENE'S TEST ---
Levene’s Test P-value: 0.0000
Warning: Variances are unequal (p < 0.05). Use Welch's ANOVA if needed.
--- 2. ONE-WAY ANOVA RESULTS ---
sum_sq   df   F PR(>F)
C(department) 8.620253e+06   8.0 50075.93456   0.0
Residual   1.179162e+06 54799.0   NaN NaN
--- 3. TUKEY HSD PAIRWISE COMPARISONS ---
C:\Users\91808\AppData\Local\Temp\ipykernel_17096\2005390533.py:38: FutureWarning:
Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys
will always be treated as labels (consistent with DataFrame behavior). To access a value by
position, use `ser.iloc[pos]`
p_anova = anova_table['PR(>F)'][0]
Multiple Comparison of Means - Tukey HSD, FWER=0.05
==================================================================
==========
group1   group2   meandiff p-adj lower upper reject
----------------------------------------------------------------------------
Analytics   Finance -24.3809   0.0 -24.7278 -24.0341 True
Analytics   HR -34.5848 0.0 -34.9373 -34.2322 True
Analytics   Legal -24.7348   0.0 -25.2226 -24.247 True
Analytics   Operations -24.3763   0.0 -24.6149 -24.1377 True
Analytics   Procurement -14.4805   0.0 -14.7407 -14.2203 True
Analytics   R&D -0.0064   1.0 -0.5023 0.4896 False
Analytics Sales & Marketing -34.3413   0.0 -34.567 -34.1155 True
Analytics   Technology -4.6743   0.0 -4.9344 -4.4141 True
Finance   HR -10.2038   0.0 -10.6128 -9.7948 True
Finance   Legal -0.3539 0.4934 -0.8839 0.1761 False
Finance   Operations 0.0046   1.0 -0.3114 0.3207 False
Finance   Procurement 9.9004   0.0 9.5678 10.2331 True
Finance   R&D 24.3746   0.0 23.8371 24.9121 True
Finance Sales & Marketing -9.9603   0.0 -10.2668 -9.6538 True
Finance   Technology 19.7067   0.0 19.3741 20.0393 True
HR   Legal 9.8499   0.0 9.3162 10.3837 True
HR   Operations 10.2085   0.0 9.8862 10.5307 True
HR   Procurement 20.1042   0.0 19.7657 20.4428 True
HR   R&D 34.5784   0.0 34.0372 35.1196 True
HR Sales & Marketing 0.2435 0.2762 -0.0694 0.5564 False
HR   Technology 29.9105 0.0 29.5719 30.2491 True
Legal   Operations 0.3585 0.2924 -0.1079 0.8249 False
Legal   Procurement 10.2543   0.0 9.7765 10.7321 True
Legal   R&D 24.7285 0.0 24.0909 25.366 True
Legal Sales & Marketing -9.6064   0.0 -10.0664 -9.1465 True
Legal   Technology 20.0605   0.0 19.5828 20.5383 True
Operations   Procurement 9.8958   0.0 9.6784 10.1132 True
Operations   R&D 24.3699   0.0 23.8951 24.8448 True
Operations Sales & Marketing -9.9649   0.0 -10.1397 -9.7902 True
Operations   Technology 19.702   0.0 19.4847 19.9194 True
Procurement   R&D 14.4742 0.0 13.9881 14.9602 True
Procurement Sales & Marketing -19.8607   0.0 -20.064 -19.6575 True
********** 4 **********
--- page 5 ---
Procurement   Technology 9.8062   0.0 9.5654 10.0471 True
R&D Sales & Marketing -34.3349   0.0 -34.8034 -33.8664 True
R&D   Technology -4.6679   0.0 -5.154 -4.1819 True
Sales & Marketing   Technology 29.667   0.0 29.4638 29.8702 True
----------------------------------------------------------------------------
b. def negative_log_likelihood(params, data):
mu, sigma = params
if sigma <= 0:
return np.inf
return -np.sum(stats.norm.logpdf(data, loc=mu, scale=sigma))
results = {}
for grp in df['group'].unique():
data_grp = df[df['group'] == grp]['values'].values
# Initial guess
init = [np.mean(data_grp), np.std(data_grp)]
CO-1;
SO-1;   # Optimization   [10]
BL-3   result = opt.minimize(negative_log_likelihood, init, args=(data_grp,))
mu_mle, sigma_mle = result.x
# Analytical
mu_analytical = np.mean(data_grp)
sigma_analytical = np.sqrt(np.mean((data_grp - mu_analytical)**2))
df = pd.DataFrame({
'outcome': np.concatenate([group_A, group_B]),
'group': ['A']*120 + ['B']*120
})
Q4   [20]
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from statsmodels.stats.outliers_influence import variance_inflation_factor
CO-4;   # 1. LOAD DATA
SO-6;   # Dataset: R&D Spend, Administration, Marketing Spend, State, Profit
BL-3   df = pd.read_csv('50_Startups.csv')
# 2. HANDLE CATEGORICAL DATA (The State Column)
# We use drop_first=True to avoid the Dummy Variable Trap.
# If we have 3 states, we only need 2 columns to represent them.
df_final = pd.get_dummies(df, columns=['State'], drop_first=True)
# 3. DEFINE FEATURES AND TARGET
********** 5 **********
--- page 6 ---
X = df_final.drop('Profit', axis=1)
y = df_final['Profit']
# FIX 1: Ensure all data is numeric (converts True/False to 1/0 and strings to numbers)
X = X.astype(float)
# FIX 2: Check for any stray NAs that might have been created
X = X.fillna(0)
# 4. MULTICOLLINEARITY CHECK (VIF)
# VIF measures how much a variable is predicted by other variables.
# VIF > 5-10 suggests high multicollinearity.
def calculate_vif(X_data):
vif_df = pd.DataFrame()
vif_df["Feature"] = X_data.columns
# Adding a constant is required for statsmodels VIF calculation
X_with_const = sm.add_constant(X_data)
vif_df["VIF"] = [variance_inflation_factor(X_with_const.values, i+1)
for i in range(len(X_data.columns))]
return vif_df
print("--- Variance Inflation Factors ---")
print(calculate_vif(X))
# 5. BUILDING THE MODEL (Using statsmodels for detailed p-values)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_const = sm.add_constant(X_train) # Adding the intercept (B0)
model = sm.OLS(y_train, X_train_const).fit()
# 6. OUTPUT RESULTS
print("\n--- Model Summary ---")
print(model.summary())
--- Variance Inflation Factors ---
Feature   VIF
0   R&D Spend 2.495511
1 Administration 1.177766
2 Marketing Spend 2.416797
3   State_Florida 1.387641
4 State_New York 1.335061
--- Model Summary ---
OLS Regression Results
==================================================================
============
Dep. Variable:   Profit R-squared:   0.954
Model:   OLS Adj. R-squared:   0.947
Method:   Least Squares F-statistic:   140.1
Date:   Sun, 22 Mar 2026 Prob (F-statistic):   1.13e-21
Time:   12:09:40 Log-Likelihood:   -420.63
No. Observations:   40 AIC:   853.3
Df Residuals:   34 BIC:   863.4
Df Model:   5
Covariance Type:   nonrobust
==================================================================
=================
coef   std err   t   P>|t|   [0.025   0.975]
-----------------------------------------------------------------------------------
********** 6 **********
--- page 7 ---
const   5.403e+04 8457.293   6.388   0.000 3.68e+04 7.12e+04
R&D Spend   0.8056   0.052   15.383   0.000   0.699   0.912
Administration   -0.0688   0.061   -1.133   0.265   -0.192   0.055
Marketing Spend   0.0299   0.022   1.346   0.187   -0.015   0.075
State_Florida   938.7930 3893.511   0.241   0.811 -6973.773 8851.359
State_New York   6.9878 3882.765   0.002   0.999 -7883.740 7897.715
==================================================================
============
Omnibus:   15.391 Durbin-Watson:   1.751
Prob(Omnibus):   0.000 Jarque-Bera (JB):   20.231
Skew:   -1.142 Prob(JB):   4.05e-05
Kurtosis:   5.631 Cond. No.   1.64e+06
==================================================================
============
Q5   [20]
a.
CO-1;
SO-2;   10
BL-4
********** 7 **********
--- page 8 ---
b.
CO-7;
SO-1;   10
BL-3
Q 6   [20]
a. import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# 1. Prepare Data
df = pd.read_csv('Fuel_Efficiency.csv')
X = df[['Engine_Speed']] # FIX: Double brackets for 2D shape
y = df['Efficiency']
# Simple Linear Regression (The Baseline)
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_lin_pred = lin_reg.predict(X)
CO-4;   # 2. Polynomial Transformation (Degree 2)   [10]
SO-1;   poly_features = PolynomialFeatures(degree=2, include_bias=False)
BL-3   X_poly = poly_features.fit_transform(X)
# 3. Fit Polynomial Regression
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
y_poly_pred = poly_reg.predict(X_poly)
# 4. Diagnostics & Comparison
print(f"Linear Model MSE: {mean_squared_error(y, y_lin_pred):.2f}")
print(f"Polynomial Model MSE: {mean_squared_error(y, y_poly_pred):.2f}")
print(f"Linear Model R2: {r2_score(y, y_lin_pred):.4f}")
print(f"Polynomial Model R2: {r2_score(y, y_poly_pred):.4f}")
# 5. Visual Check
# We use values.min() and values.max() to ensure we get the underlying numbers
X_grid = np.arange(X.values.min(), X.values.max(), 0.1).reshape(-1, 1)
********** 8 **********
--- page 9 ---
plt.scatter(X, y, color='blue', alpha=0.5, label='Actual Data')
plt.plot(X_grid, lin_reg.predict(X_grid), color='red', label='Linear Fit')
plt.plot(X_grid,   poly_reg.predict(poly_features.transform(X_grid)),   color='green',
label='Polynomial Fit')
plt.title('Fuel Efficiency: Linear vs. Polynomial Regression')
plt.xlabel('Engine Speed')
plt.ylabel('Efficiency')
plt.legend()
plt.show()
Linear Model MSE: 19.36
Polynomial Model MSE: 3.11
Linear Model R2: 0.5878
Polynomial Model R2: 0.9338
b. L1vs.L2: Because the L1 penalty is the absolute value, its derivative is a constant (+/-1) rather
than a term that depends on the size of the coefficient (beta). This means Lasso applies a
constant pressure to pull coefficients to zero. In a two-dimensional space, the constraint region
for Ridge is a circle, while for Lasso, it is a diamond (rhombus). The "corners" of the diamond
sit on the axes. When the RSS ellipses expand, they are highly likely to hit a corner first,
setting the other variable's coefficient to exactly 0.
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
# 1. SPLIT & SCALE (Lasso is extremely sensitive to scale)
CO-5;   X_clean=pd.read_csv('House_price.csv')
SO-2;   X_train, X_test, y_train, y_test = train_test_split(X_clean, y, test_size=0.2, random_state=42)   [10]
BL-4
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# 2. RUN LASSOCV
# We provide a range of alphas. LassoCV uses 5-fold CV by default.
lasso_mod = LassoCV(alphas=np.logspace(-4, -1, 50), cv=5, max_iter=10000)
lasso_mod.fit(X_train_scaled, y_train)
# 3. EVALUATE
y_pred = lasso_mod.predict(X_test_scaled)
********** 9 **********
--- page 10 ---
print(f"Optimal Alpha (Lambda): {lasso_mod.alpha_:.6f}")
print(f"R-squared: {r2_score(y_test, y_pred):.4f}")
# 4. DEMONSTRATE FEATURE SELECTION
total_features = X_clean.shape[1]
active_features = np.sum(lasso_mod.coef_ != 0)
removed_features = total_features - active_features
print(f"\nTotal Features: {total_features}")
print(f"Features Retained by Lasso: {active_features}")
print(f"Features Dropped (set to 0): {removed_features}")
Optimal Alpha (Lambda): 0.010481
R-squared: 0.8783
Total Features: 260
Features Retained by Lasso: 54
Features Dropped (set to 0): 206
Q 7   [20]
a. import numpy as np
from scipy import stats
group1 = np.array([18, 15, 14, 19, 16])
group2 = np.array([12, 14, 11, 15, 13])
mean1, mean2 = np.mean(group1), np.mean(group2)
std1, std2 = np.std(group1, ddof=1), np.array(group2).std(ddof=1)
n1, n2 = len(group1), len(group2)
# 3. Calculate Pooled Standard Deviation (for equal variance)
CO-2;   df = n1 + n2 - 2
SO-1;   pooled_var = ((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / df   [10]
BL-3   t_stat_manual = (mean1 - mean2) / np.sqrt(pooled_var * (1/n1 + 1/n2))
t_stat, p_val = stats.ttest_ind(group1, group2)
print(f"Group 1 Mean: {mean1} | Group 2 Mean: {mean2}")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val:.4f}")
Group 1 Mean: 16.4 | Group 2 Mean: 13.0
T-Statistic: 2.9155
P-Value: 0.0194
b. import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Source: HR Analytics Promotion Dataset (train.csv)
df = pd.read_csv('train.csv')
df['previous_year_rating']   =
df['previous_year_rating'].fillna(df['previous_year_rating'].median())
CO-6;   # Target is 'is_promoted' (1 for Yes, 0 for No)
SO-2;   features = ['age', 'avg_training_score', 'length_of_service', 'KPIs_met >80%', 'awards_won?']   [10]
BL-4   X = df[features]
y = df['is_promoted']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))
# Profile: Age 28, Score 85, Service 3, KPI Yes (1), Awards Yes (1)
candidate = pd.DataFrame([[28, 85, 3, 1, 1]], columns=features)
promotion_prob = model.predict_proba(candidate)[0][1]
********** 10 **********
--- page 11 ---
print(f"Train Accuracy: {train_acc:.2%}")
print(f"Test Accuracy: {test_acc:.2%}")
print(f"Candidate Promotion Probability: {promotion_prob:.2%}")
Train Accuracy: 95.14%
Test Accuracy: 90.90%
Candidate Promotion Probability: 25.00%
********** 11 **********
````
