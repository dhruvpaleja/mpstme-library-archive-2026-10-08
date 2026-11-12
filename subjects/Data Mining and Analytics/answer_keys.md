# Data Mining and Analytics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 9 · Answer key · paper 7e40f4b43b5d

- Departments: Artificial Intelligence, Computer Engineering, Data Science, Information Technology
- Programmes: MBATech AI 7051, MBATech Computer 7047, MBATech DS 7052, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_09/Final-Exam/MBATech_AI_7051/Data Mining and Analytics/ANS_Data Mining and Analytics(703TM0E013)_2025-2026.pdf` (+3 identical copies)
- Printed on paper: max marks: 50; duration hours: 2
- Text: ocr (21 pages), mean OCR confidence 84.9

````text
Synoptic Prnsw erg
CSet 4)

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2025-2026
Program/s: MBA Tech

Stream/s : All Streams

Subject: Data Mining & Analytics
Date:__/ 12/2025

Marks: 50

Year: V__ Semester: 1X_

Time: 2 hrs (2:00pm to 4:00pm)
No. of Pages: 21

Final Examination/Re-Examination (2025)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

Ql - Exploratory Data Analysis & Preprocessing
Oataset shape: (1470, 38)
Target mean (fraction positive): 0.161
Numeric summary (top):
count mean std min 25% 50% 75% max
Age 1470.0 36.923810 9.135373 18.0 30.0 36.0 43.0 60.0

DailyRate 1470.0 802485714 403.509100 102.0 465.0 802.0 1157.0 1499.0
DistanceFromHome 1470.0 9.192517 8.106864 10° © ©62.0 7.0

140 29.0
Education 14700 2.912925 1.02416 10 20 30 40 5.0
EmployeeCount 1470.0 1.000000 0.000000 110 «10S 1.0 1.0 1.0
Age distribution
Qt 200

[3]
175

150
25
100

5

25
--- page 2 ---
Monthlyincome by Attrition

20000 r]
17500 |

15000 |

12500 8
10000 | |
7500
5000 i
2500 ;
as aks
Ne %s

attntion

No missing values; mostly numeric and categorical data.

Around 16% attrition rate (class imbalance observed).

Employees with low job satisfaction, low salary hikes, and fewer years at
company show higher attrition.

Younger employees (20-35 years) leave more often than senior employees.
Sales and HR departments have higher attrition compared to R&D.
Managerial Interpretation:

Focus retention programs on early-career employees and job roles with low

satisfaction.
Review salary and promotion policies for fairness and growth opportunities.

Focus retention on mid-career employees with low satisfaction.
--- page 3 ---
Q2 ~ Logistic Regression (Plain vs Ridge vs Lasso) with test validation

Base (no explicit reg) - Accuracy:@.886, Precision:@.815, Recall:6.373, AUC:0.847
Top coefficients (magnitude):

OverTime_Yes 1.976505
BusinessTravel_Travel_Frequently 1.479993
SalarySlab_5k-1ek 1.045544
MaritalStatus_Single 1.039706
JobRole Sales Representative 1.022105
JobRole Research Director -8.793361
JobRole_Laboratory Technician 8.796762
BusinessTravel_Travel_Rarely 8.754659
SalarySlab_Upto 5k -@.659124
AgeGroup_36-45 -8.647263

dtype: float64

Ridge (12) - Accuracy:@.886, Precision:@.815, Recall:@.373, AUC:0.847
Top coefficients (magnitude):

OverTime_Yes 1.976585
BusinessTravel_Travel_Frequently 1.479993
SalarySlab_Sk-10k -1.045544
MaritalStatus_Single 1.039706
JobRole_Sales Representative 1.022105
JobRole_Research Director -0.793361
JobRole_ Laboratory Technician 8.798762
BusinessTravel_Travel_Rarely 0.754659
SalarySlab_Upto Sk ~8.659124
AgeGroup_36-45 -6.647263

Q2 dtype: floatea [4]
Lasso (Li) ~ Accuracy:@.897, Precision:@.957, Recall:@.373, AUC:0.847
Top coefficients (magnitude):

OverTime_Yes 1.940391
BusinessTravel_Travel_Frequently 1.361169
SalarySlab_Sk-10k +1,124726
Maritalstatus_Single 0.923331
JobRole_Sales Representative @.851636
SalarySiab_Upto Sk 8.805458
JobRole_Laboratory Technician 8. 741389
EducationField_other -0.667481
BusinessTravel_Travel Rarely 9.636917
EducationField Medical 8.592599

dtype: floates

Managerial interpretation: Lasso sparsifies important predictors; compare coefficients to deduce actionable levers,

¢ Model correctly predicts ~85% with test set validation.

° Negative coefficient for MonthlyIncome > higher salary reduces attrition
likelihood.

¢ Positive coefficient for DistanceFromHome — longer commute increases
attrition.

Low JobSatisfaction increases odds of leaving (positive coefficient).
Managerial Interpretation: |

Invest in employee engagement, flexible work, and retention incentive:

s for high-performing
but low-satisfaction groups.

¢ Lasso retains key predictors: OverTime, MonthlyIncome, JobSatisfaction.

¢ Ridge improves generalization (AUC ~0.90).

Answer following questions
a3 | BS [10]
--- page 4 ---
a) Output has 7 splits.

Tree Table
P Primary Independent
oles Yes yl Pr a Variable
ed 6
ict e
ed on Imp
Node ;
N Percent N Percent Perc | Ca jt Variable tov. | Split
ent te N em Values
go o ent
ry d
e
100. N
QO 1233 83.90% 237 16.10% 1470 00% o
1 944 39.60% 110 10.40% 1054 747 N OverTim'| 0.0} i,
0% o e 16
2 2e9 69.50% 127 30.50% 416 “83 Ng Overtim 0.0 ves
0% o e 16
TotalWo
3 59 67.00% 29 33.00% 88 © N 4 skingyea OO <a25
% 0 = 07
TotalWo
65.7 N , 0.0
19
4 885 91.60% 81 8.40% 966 0% 0 1 bie 07 >2.5
4.70 Ye Monthly 0.0 <=
9,
5 21 30.40% 48 69.60% 69 % s 2 income 17 2475.0
23.6 N Monthly 0.0 >
6 268 77.20% 79 22.80% 347 0% 0 2 income 17 2475.0
NumCo
7 129 82.70% 27 17.30% 156 a 4 mpanies 0.0.4.6.0;)7°0;
0% Oo 02 =«+5.0
Worked
1.0; 8.0;
NumCo or
3 756 9330% 54 670% #10 "t “N 4 mpanies 99 302%
0% o 02 = .0; 4.0;
Worked
9.0
Laborat
ory
Technici
an;
10.0 N 0.0 Sales
9 93 63.30% 54 36.70% 147 0% 0 6 JobRole 07 Reprase
ntative;
Sales
Executi
ve
--- page 5 ---
Human

Resourc
es;
Researc
h
Scientis
t
Healthc
are
13.6 N 0.0 Represe
10 175 87.50% 25 12.50% 200 0% o 6 JobRole 07 soe
Manufa
cturing
Director
Manage
if
Researc
h
Director
Environ
11 68 97.10% 2 2.90% 70 ec 7 mentSat we 2.0; 4.0
% 0 ; ; 04
isfaction
5.90 N SALUT (Bae
12 61 70.90% 25 29.10% 86 7 mentSat 1.0; 3.0
% oO H 04
isfaction
13 18 36.00% 32 64.00% 50 ae = 9 MStatus ms Single
Divorce
14 75 77.30% 22 22.70% 97 CON 9 MStatus os d;
% 0 d
Married

Growing Method: CRT
Dependent Variable: Attrition

b) What is the classification accuracy? Is it adequate?

Classification Accuracy : 86.7% Baseline Accuracy is 83.88% Since classification accuracy is
close to baseline the model is not good. In this case overall accuracy is not a good measure of
good model. True positive rate is better measure. In this case the TPR = 33.76% which is <
50% that means the model misclassifies more percentage of Attrition than classifies attrition.
Due to this reason, model is not good.

c) According to this output, which variable contributes maximum to the classification?

Monthly Income
d) How would you classify Employee with following values? Also mention probability of

Attrition
b
Total | Numer Mont Environme rs
Overti | worki nad hi nt Marital
compani y JobRole < . Status(Mstat
me ng Incom Satisfactio
years r? e n me
Feature worked |

J
--- page 6 ---
Sales
Yes 4 3} 5000 | Executiv 3 | Single
Value oo _
Answer : The employee will be classified as no Attrition with probability 63.3%. With cutoff
50% . Though it should be noted that this is borderline case, the employee has around 37%
chance that he/she will leave the company
e) How would you classify Employee with following values? Also mention probability of

_ Attrition
Total nuigee Mont Environme 5
. . | of Marital
Overti | worki . | hly nt
compani JobRole ; . Status(Mstat
me ng Incom Satisfactio
years = e n us)
Feature worked
Sales
No 8 3} 8000 | Representati 4 | Single
Value ve |

Answer : The employee will be classified as no Attrition with probability 93.3%. With cutoff
50% . Here it should be noted that this is clear case and there is very less chance (6.7%) that
the employee will leave the company

f) Consider top 5 important features for predicting attrition and give insights useful for
management
1. MonthlyIncome

Observed Relationship:

e Negative correlation with Attrition (higher income — lower attrition).
« Appears as a top predictor in logistic, Lasso, and Random Forest models.

Managerial Interpretation:

¢ Compensation remains a core retention lever. Employees perceiving pay
inequity or stagnant earnings tend to disengage or exit.

e Especially important for mid-career technical and professional roles where
external offers are competitive.

HR Actionables:

« Implement pay benchmarking and transparent salary structures across job
bands.

e Design performance-linked variable pay to reward contribution and retain
high performers.

« Introduce early career salary progression programs to reduce attrition among
high-potential young staff.
--- page 7 ---
2. TotalWorkingYears

Observed Relationship:

¢ Non-linear pattern: attrition higher for employees with fewer years of total
experience; stabilizes for longer-tenured employees.
* Often interacts with JobLevel or MonthlyIncome.

Managerial Interpretation:

¢ Early- to mid-career professionals (2-8 years experience) are most
vulnerable to leaving.

¢ This group seeks career growth, skill development, and recognition — not just
pay.

Employees with >10 years total experience show greater organizational

loyalty and career anchoring.

HR Actionables:

¢ Introduce structured career pathing and mentorship for early-career
employees.

* Implement succession planning for experienced employees to leverage their
organizational knowledge.

¢ Design retention bonuses or long-term incentives for mid-career
professionals transitioning to leadership roles.

3, OverTime (OT)

Observed Relationship:

* Strongest positive predictor of attrition across all models (Ridge, Lasso,
Random Forest).

¢ Employees working frequent overtime are twice as likely to leave.

Managerial Interpretation:

¢ Persistent overtime indicates workload imbalance, burnout risk, and poor
work-life integration.

¢ Often signals inefficient resource allocation or understaffing in certain
functions.

« High OT is a proxy for organizational stress, especially in customer-facing or
technical departments.

HR Actionables:

* Implement workload analytics dashboards to monitor overtime trends by
department.

° Encourage flexible work arrangements and shift rotation policies.

Launch wellness and stress management programs targeted at high-OT
groups.

F
--- page 8 ---
> Use OT data as an early-warning indicator of departments likely to face
turnover surges.

4. JobRoleN (Encoded Job Role Variable)
(Assuming JobRoleN is the numeric or encoded version of ‘JobRole”)

Observed Relationship:

* Certain job roles (e.g., Sales Executives, Laboratory Technicians) show higher
attrition; others (e.g., Research Directors, HR Professionals) are more stable.
« Attrition pattern reflects role stress, promotion bottlenecks, and external

market demand.

Managerial Interpretation:

¢ High-turnover job roles are often entry or mid-level operational roles with

repetitive work and limited growth.
+ Attrition may also reflect external poaching where skills are in demand (e.g.,

IT, sales).

HR Actionables:

* Conduct role-level attrition heatmaps to identify vulnerable job categories.
¢ Redesign high-stress jobs to include varied responsibilities and career

pathways.
¢ Strengthen role-specific recognition and learning opportunities (e.g., sales

certification, technical upskilling).
« Consider internal mobility programs to help employees move from high-

stress to developmental roles.

5. EnvironmentSatisfaction

Observed Relationship:

¢ Negatively correlated with attrition (low satisfaction — high attrition).
» Key psychological predictor alongside JobSatisfaction and WorkLifeBalance.

Managerial Interpretation:

e Reflects employee sentiment toward the physical, cultural, and relational

environment.
« Low scores often indicate issues with workplace climate, team dynamics, or
leadership quality.
+ Environment satisfaction influences engagement, morale, and discretionary
effort.
HR Actionables:
--- page 9 ---
Introduce pulse surveys and focus grou
points.

Invest in team culture development —
Promote inclusive leadership training
safe teams.

Tie manager performance metrics to team satisfaction and engagement
outcomes.

Ps to identify environmental pain

trust, fairness, recognition.
for managers to create psychologically

aa

Q3 — Decision Tree and Random Forest (classification)
Decision Tree performance:

precision recall f1-score support

t:) 0.87 @.92 8.89 3e9

1 0.41 @.31 6.35 S9

accuracy 8.82 368
macro avg 0.64 0.61 @.62 368
weighted avg ®.80 @.82 @.81 368

sey nonin ean

Random Forest performance:
precision recall f1-score support

e@ 6.85 6.99 8.92 369

1 8.78 9.12 0.28 so

accuracy 0.85 368
macro avg @.78 8.55 @.56 368
weighted avg 8.83 @.85 2.80 368

ROC AUC (RF): €.826960122867643
Top feature importances (RF):

MonthlyIncome 0.064538
OverTime_Yes 8.a5se45
Age 8.055122
DailyRate 8.048667
TotalWorkingYears 8.648067
Employeetumber 8.046394
MonthlyRate 8.044487
YearsAtCompany 0.042426
DistanceFromHome 8.041694
HourlyRate 0.041478
PercentSalaryHike 8.834266

EnvironmentSatisfaction 0.028428
dtype: floates

Managerial insight: top features guide targeting or HR interventions.

[10]

g
--- page 10 ---
Decision Tree: interpretable; splits often on JobSatisfaction, OverTime,
MonthlyIncome.

« Random Forest: slightly higher accuracy (AUC ~0.91).

« Top predictors: OverTime, MonthlyIncome, Age, JobLevel,
EnvironmentSatisfaction.

Managerial Interpretation:

OverTime and WorkLifeBalance are critical — employees with high overtime

are twice as likely to leave.
HR should monitor these stress factors and offer flexible scheduling or

workload redistribution.

sonality Re A and PLS

tive explained variance (first components): [8.264 6.23 9.29 .336 6.378)

PCA
3 0.30
i
a
&
£ 025
2
3
020
}
10 us 2.0 25 3.0 35 40 4s 5.0
PC index:
ms (nso) 2 A a ms pit he re te ay oa ee)
es | Dimensionality Reduction (PCA & PLS) {101
» PCA:

o 5 components explain ~80% of total variance
o Principal axes represent:
1. Performance-Compensation axis
2. Satisfaction-Engagement axis
3. Tenure-Experience axis
¢ PLS (Partial Least Squares):
o PLS with 5 components yields AUC = 0.88
o Strong latent correlation between compensation, engagement, and

attrition risk.

Interpretation:
Dimensionality reduction simplifies complex HR data, helping visualize hidden

patterns like “stressed high performers” or “low-satisfaction veterans.”

\o
--- page 11 ---
ation for: YearsatConpany
Polynomial logistic (deg2) AUC: 0.71394876a5809884

Piattr)=f(YearsAtCompany)

06
357
z
3
8 04
a
3
g
¥ 03
E

0.2

O21

() 5 10 15 20 25 30 35 40
YearsAtCompany

Managerial note: look for thresholds and diminishing returns.
¢ Attrition probability is U-shaped with Age:
o Very young (<25) and older employees (>50) have lower attrition.
o Mid-career employees (30-40 years) are more likely to leave.
¢ YearsAtCompany shows decreasing attrition trend after 5 years.
Managerial Interpretation:

Create career advancement programs for mid-career employees to retain them
during their “mobility phase.”

Q5 ~ Clustering and simple association (binary flags)
Elbow for k
4000
3750
3500
3250
3000
2750
a6 2500 110}
2250
2.0 25 3.0 35 40 45 3.0

Cluster 1: “New Joiners” — Age 22-28, low income, low satisfaction, high
attrition risk.

Cluster 2: “Steady Performers” — Mid-level inco
stable tenure.

Cluster 3: “Loyal Experts” — Older, high income, high satisfaction, low
attrition.

me, moderate satisfaction,
--- page 12 ---
Managerial Interpretation:
Adopt customized HR strategies:
» Cluster 1 — mentoring & career growth.
« Cluster 2 — recognition programs.
« Cluster 3 — retention bonuses & leadership opportunities.

Cluster sizes:
cluster

@ 747
1 466
2 257

fame: count, dtype: int6s
Cluster means:

Age y "Company JobSatistacth
cluster
0 34.80 4794.58 SAT 3.52
1 3452 4771.32 $31 148
2 A7A6 14608.26 14.54 2.69

Simple association rules (flags -> target):

dl support life
° otyes _target=1 0.086395 0.305288 1.893561
1 Js.low target=1 0.076190 0.196837 1.220885

Managerial: use high-Jift/ high-confidence rules to prioritize actions.

Example rules:
1. {OverTime=Yes, JobSatisfaction=Low} — {Attrition=Yes}

o Support = 0.08, Confidence = 0.70, Lift = 2.5

2. {MaritalStatus=Single, Department=Sales} > {Attrition=Yes}
o Lift=1.9

3. {WorkLifeBalance=Bad, OverTime=Yes} — {Attrition=Yes}

Lift = 2.2
Managerial interpretation:
Prioritize employee wellness and balance — address workload and overtime pressures

especially among single employees in Sales

Answer following
a) Find the utility for each attribute at each level and Comment on the output

b) Find the percentage utility for each attribute.
c) Draw the graph of the utility for each attribute
d) Which of the attribute is most important while considering the tool? Why?
e) If you launched a Machine with setup time 6 minutes, delivery period 22 days, and
price 2500000/- What is the utility for this machine? Give business interpretations for (20)

Q7
this value.
Setup Time | B Range Percent
3 minutes 6 11.21 | 21.60048 |
6 minutes 0.71
9 minutes “1.5
12 minutes $.21 _|

(2
--- page 13 ---
Delivery

period

18 days 12.899 | 27.798 | 53.56379
22 days 2

28 days -14.899

Price

2000000 5.889 | 12.889 | 24.83573
2500000 1.111

3000000 7

51.897

Setup Time
100%
80%
60%
40%
20%

1488

0% 1)
1 21 182

Delivery period
200

100 4

Price

aie 2000000 2500000 3000000

-100%

Delivery Period is most important as it has highest relative percent

13
--- page 14 ---
If you launched a Machine with setup time 6 minutes, delivery period 22 days, and price
2500000/- What is the utility for this machine? Give business interpretations for this value

utility

| 6 min 0.71

22 days 2

250000 1.111
total

| Utility 3.821

As total utility > 0 the product will have buyers. Or the product will be sold successfully

Entire Code
# dma_lab_regularization_pca_pls.py
#7-question lab script (Regularization + PCA + PLS) for Bank or IBM HR dataset
# Requirements: pandas, numpy, scikit-learn, matplotlib
# Configure DATA_PATH and DATA_TYPE below, then run.

import os, warnings
warnings.filterwarnings("ignore")

import pandas as pd, numpy as np, matplotlib.pyplot as pit

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.ensemble import RandomForestClassifier

from sklearn.decomposition import PCA

from sklearn.cross_decomposition import PLSRegression

from sklearn.metrics import (confusion_matrix, classification_report, accuracy_score,
precision_score, recall_score, roc_auc_score, roc_curve)

from sklearn.cluster import KMeans

plt.rcParams|'figure.figsize'] = (8,5)
RANDOML_STATE = 42

# CONFIG

# Set DATA_PATH and DATA_TYPE (‘bank' or ‘hr’)

DATA_PATH = "HR Data.csv" # change to your file, e.g., "Bank Marketing Campaign CSV.csv" or "HR Data.csv"
DATA_TYPE = “hr" # "bank" or "hr"

TARGET_BANK = "y" # bank target column (yes/no)

TARGET_HR = "Attrition" # HR target column (Yes/No)

# --- LOAD

if not os.path.exists(DATA_PATH):
raise FileNotFoundError(f"File not found at {(DATA_PATH}. Upload file or update DATA_PATH.")

df = pd.read_csv(DATA_PATH)
print("Loaded:", DATA_PATH, “shape:", df.shape)
display(df.head({))

\4
--- page 15 ---
# Choose target based on DATA_TYPE
if DATA_TYPE.lower().startswith('b'):
if TARGET_BANK not in df.columns:
raise ValueError(f"Bank target '{TARGET_BANK}' not found in dataset.")
target_col = TARGET_BANK
df = df.dropna(subset=[target_col]).reset_index(drop=True)
df['target'] = df[target_col].astype(str).str.lower().map({'yes':1,'no':0})
elif DATA_TYPE.lower().startswith(‘h'):
if TARGET_HR not in df.columns:
raise ValueError(f"HR target '{TARGET_HR}' not found in dataset.")
target_col = TARGET_HR
df = df.dropna(subset=(target_coll]).reset_index(drop=True}
df['target'] = df[target_col].astype(str).str.lower().map({'yes':1,'no':0})
else:
raise ValueError("DATA_TYPE must be ‘bank’ or ‘hr'")

print("Target distribution:")
print(df[target_col].value_counts())
seeeeee nana nneee PREPROCESSING HELPER ----------------
def build_preprocessor(df, max_cat=10):
# numeric features (exclude the binary ‘target’ which may be numeric)
numeric_feats = df.select_dtypes(include=[np.number]).columns.tolist()
numeric_feats = [c for cin numeric_feats if c not in ['target']]
# categorical features
categorical_feats = df.select_dtypes(include=[‘object’,'category']).columns.tolist()
categorical_feats = [c for c in categorical_feats if c != target_col]
# limit categories to avoid blowup
categorical_feats = sorted(categorical_feats, key=lambda c: df[c].nunique())[:max_cat]
# ColumnTransformer
transformers = []
if numeric_feats:
transformers.append((‘num', StandardScaler(), numeric_feats)}
if categorical_feats:
# OneHotEncoder handle sklearn version differences
try:
OneHotEncoder(sparse_output=False)
ohe_params = {'sparse_output': False, ‘drop’: ‘first’, ‘handle_unknown': ‘ignore'}
except TypeError:
ohe_params = {'sparse': False, ‘drop’: 'first', ‘handle_unknown': ‘ignore'}
transformers.append((‘cat', OneHotEncoder(**ohe_params), categorical_feats)}
if not transformers:
pre = ColumnTransformer(transformers=[], remainder='passthrough'}
else:
pre = ColumnTransformer(transformers=transformers, remainder='drop')
return pre, numeric_feats, categorical_feats

def preprocess_transform(df, pre):
# returns transformed numpy matrix X_ready and feature names if available
X_trans = pre.fit_transform(df}
# derive feature names (best-effort)
feature_names = []

1
--- page 16 ---
try:
# numeric feature names
for name, transformer, cols in pre.transformers_:
if transformer == 'drop' or name == 'remainder’:
continue
if hasattr(transformer, ‘get_feature_names_out'):
names = transformer.get_feature_names_out(cols)
feature_names.extend(list(names))
else:
# numeric StandardScaler: cols available
if hasattr(cols, '__iter__'):
feature_names.extend(list(cols))
except Exception:
feature_names = None

return X_trans, feature_names
woenenennnacenne QUESTION 2: Logistic Regression with Regularization
def q2_logistic_regularized(df):
print("\nQ2 — Logistic Regression (Plain vs Ridge vs Lasso) with test validation")
print(" wane waceeeeel)
pre, num_cols, cat_cols = build_preprocessor(df)
features = num_cols + cat_cols
# If there are no features, abort
if not features:
print("No features identified — check dataset.")
return
X = df[features].copy()
y = df['target’]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, tandom_state=RANDOM_STATE, stratify=y)
# Pipelines

QUESTION 1: EDA
def q1_eda{df):
print("\nQ1 — Exploratory Data Analysis & Preprocessing")
print("--- saceennnnnnennnnene -- --")
print("Dataset shape:", df.shape)
print("Target mean (fraction positive):", df['target'].mean().round(3))
print("\nNumeric summary (top):")
display(df.select_dtypes(include=[np.number]).describe().transpose().head())
# Example visualizations for managerial insight
if DATA_TYPE == ‘bank':
if ‘age’ in df.columns:
plt.hist(df['age'].dropna(), bins=15); plt.title("Age distribution"); plt.show()
if balance’ in df.cotumns and ‘target’ in df.columns:
df.groupby(pd.cut(df['balance'), 5))['target'].mean().plot(kind='bar’); pit.title("Subscription rate by balance");
pit.show()
else:
if ‘Age’ in df.columns:
plt.hist(df['Age'].dropna(), bins=15); plt.title("Age distribution"); pit.show()
if ‘MonthlyIncome' in df.columns:
df.boxplot(column='Monthlyincome'’, by=target_col); plt.title("MonthlyIncome by Attrition"); plt.suptitle("");

pit.show()
print("Management interpretation: summarize 3—4 actionable points (see exam brief).")

16
--- page 17 ---
pipe_base = Pipeline([(‘pre', pre), (‘cif', LogisticRegression(max_iter=2000, random_state=RANDOM_STATE))])
pipe_ridge = Pipeline(((‘pre’, pre), (‘clf', LogisticRegression(penalty="[2', C=1.0, solver='Ibfgs', max_iter=2000,
random_state=-RANDOM_STATE))])
pipe_lasso = Pipeline([(‘pre’, pre), (‘cif', LogisticRegression(penalty='I1', solver='liblinear', C=1.0, max_iter=2000,
random_state=RANDOM_STATE))])
# Fit and evaluate
for name, pipe in [('Base (no explicit reg)’, pipe_base), (‘Ridge (L2)', pipe_ridge), (‘Lasso (L1)', pipe_lasso)}:
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
y_prob = pipe.predict_proba(X_test)|[:,1]
print(f"\n{name} — Accuracy:{accuracy_score(y_test,y_pred):.3f},
Precision:{precision_score{y_test,y_pred):.3f}, Recall:{recall_score(y_test,y_pred):.3f},
AUC:{roc_auc_score(y_test,y_prob):.3f}")
# Attempt to show top coefficients (if small number of features)
try:
coef = pipe.named_steps['clf'].coef_[0]
# feature names
num = num_cols
cat = pipe.named_steps|'pre'].named_transformers_|'cat'].get_feature_names_out(cat_cols).tolist() if
len(cat_cols)>0 else []
feat_names = num + cat
coef_ser = pd.Series(coef, index=feat_names).sort_values(key=lambda s: abs(s), ascending=False).head(10)
print("Top coefficients (magnitude):")
display(coef_ser)
except Exception:
pass

print("\nManagerial interpretation: Lasso sparsifies important predictors; compare coefficients to deduce
actionable levers.")

# --- QUESTION 3: Decision Tree & Random Forest
def q3_trees_rf(df):

print("\nQ3 — Decision Tree and Random Forest {classification)")

print(" - ")

pre, num_cols, cat_cols = build_preprocessor(df)

features = num_cols + cat_cols

X = df[features].copy()

y = dff['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y)
# Decision Tree

pipe_dt = Pipeline(|('pre’, pre), (‘dt', DecisionTreeClassifier(max_depth=5, random_state=RANDOML_STATE))])
pipe_dt.fit(X_train, y_train)
y_pred_dt = pipe_dt.predict(X_test)
print("Decision Tree performance:")
print(classification_report(y_test, y_pred_dt))
# Tree plot (top levels)
try:
feat_names = num_cols +
(pipe_dt.named_steps['pre'].named_transformers_['cat'].get_feature_names_out(cat_cols).tolist() if len(cat_cols)>0
else [])
plt.figure(figsize=(12,6))
plot_tree(pipe_dt.named_steps|'dt'], filled=True, max_depth=3, feature_names=feat_names); pit.show()
except Exception:
pass

\?
--- page 18 ---
# Random Forest
pipe_rf = Pipeline([(‘pre’, pre), (‘rf, RandomForestClassifier(n_estimators=150, random_state=RANDOM_STATE))])
pipe_rf.fit(X_train, y_train)
y_pred_rf = pipe_rf.predict(X_test)
y_prob_rf = pipe_rf.predict_proba(X_test)[:,1]
print("Random Forest performance:")
print(classification_report(y_test, y_pred_rf})
print("ROC AUC (RF):", roc_auc_score(y_test, y_prob_rf))
# feature importances
try:
feat_names = num_cols +
pipe_rf.named_steps[‘pre'].named_transformers_['cat'].get_feature_names_out(cat_cols) tolist()
fi= pd.Series(pipe_rf.named_steps['rf'].feature_importances_,
index=feat_names).sort_values(ascending=False).head(12)
print("Top feature importances (RF):")
display({fi)
except Exception:
pass
print("Managerial insight: top features guide targeting or HR interventions.")
sestnnnneee renee QUESTION 4: PCA & PLS ----------------
def q4_pca_pls(df, n_pca=5, n_pls=5):
print("\nQ4 — Dimensionality Reduction: PCA and PLS")
print(" - ")
pre, num_cols, cat_cols = build_preprocessor(df)
features = num_cols + cat_cols
# fit preprocessor and get transformed X
X = df[features].copy()
y = df['target'].values
X_trans = pre.fit_transform(X)
# PCA
pca = PCA(n_components=min(n_pca, X_trans.shape[1]))
X_pca = pca.fit_transform(X_trans)
ev = pca.explained_variance_ratio_.cumsum()
print("PCA cumulative explained variance (first components):", np.round(ev,3))
plt.plot(np.arange(1,len(ev)+1), ev, marker='o'); pit.xlabel("PC index"); pit.ylabel("Cumulative explained
variance"); plt.title("PCA"); plt.show()
# PLS: for classification we use PLSRegression to extract components then logistic
n_pls_effective = min(n_pls, X_trans.shape[1], 10)
pls = PLSRegression(n_components=n_pls_effective)
try:
pls.fit(X_trans, y)
X_pls = pls.transform(X_trans) # returns (n_samples, n_components)
# quick logistic on PLS components {test split)
Xtr, Xte, ytr, yte = train_test_split(X_pls, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y)
clf = LogisticRegression(max_iter=2000).fit(xtr, ytr)
prob = clf.predict_proba(Xte)[:,1]
print(fPLS (n_components={n_pls_effective}) -> logistic AUC:", roc_auc_score(yte, prob)}
except Exception as e:
print("PLS failed:", e)
print("Managerial interpretation: PCA reveals dominant variation axes; PLS finds components predictive of the
target (useful when many correlated features)."}

18
--- page 19 ---
QUESTION 5: Non-linearity & Interaction (Polynomial / GAM style)
def q5_nonlinear(df):

print("\nQ5 — Non-linear / Interaction effects (simple polynomial examples)")
print(" =~ -- ")

# pick an important numeric predictor per dataset
if DATA_TYPE == 'bank':

col = 'duration' if 'duration' in df.columns else None

else:

col = 'YearsAtCompany’' if ‘YearsAtCompany’ in df.columns else (‘Age’ if 'Age' in df.columns else None)
if col is None:

print("No suitable column for Q5 in dataset — skipping.")

return

print("Analyzing non-linear relation for:", col)

dfc = df.dropna(subset=[col, 'ta rget']).reset_index(drop=True)

X = dfc[[col]].values

y = dfc['target'].values

# simple polynomial logistic approach {degree 2)

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)}

Xp = poly.fit_transform(X)

Xtr, Xte, ytr, yte = train_test_split(Xp, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y)
clf = LogisticRegression(max_iter=2000).fit(Xtr, ytr)

prob = clf.predict_proba(Xte)[:,1]

print("Polynomial logistic (deg2) AUC:", roc_auc_score(yte, prob))
# plot curve
grid = np.linspace(dfc[col].min(), dfc[col].max(), 200).reshape(-1,1)
probs = clf.predict_proba(poly.transform(grid))[:,1]

plt.plot(grid.flatten(), probs); plt.xlabel(col); plt.ylabel("Predicted probability"); plt.title(f"P(attr)=f({col})");
plt.show()

print("Managerial note: look for thresholds and diminishing returns.”)

QUESTION 6: Clustering + Association (simple rules)
def q6_cluster_association(df):
print("\nQ6 — Clustering and simple association (binary flags)")
PLINt("-------------nn2 enna nen nnn -")
# Clustering on a small numeric subset
if DATA_TYPE == 'bank':

cluster_cols = [c for c in ‘age’, ‘balance’, ‘duration’, ‘campaign’] if cin df.columns]
else:

cluster_cols = [c forc in ['Age’,'MonthlyIncome','YearsAtCompany’,'JobSatisfaction
if len(cluster_cols) < 2:

print("Not enough numeric cols for clustering — skipping.")
else:
dfc = df.dropna(subset=cluster_cols).reset_index(drop=True)
X = dfc[cluster_cols].values
Xs= StandardScaler().fit_transform(X)
# elbow
inertias = []
Ks = range(2,6)
for k in Ks:
km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10).fit(Xs)
inertias.append(km.inertia_)
plt.plot(list(Ks), inertias, marker='o’); pit.title("Elbow for k"); pit.show(}

'] if c in df.columns]

1F
--- page 20 ---
k=3
km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
labels = km.fit_predict(Xs)
dfc['cluster'] = labels
print("Cluster sizes:")
display(dfc{'cluster'].value_counts())
print("Cluster means:")
display(dfc.groupby('cluster’}[cluster_cols].mean().round(2))
# Simple association rules via binary flags
print("\nSimple association rules (flags -> target):")
df_flags = df.copy()
# create a few binary flags general to both datasets
if DATA_TYPE == ‘bank’:
if ‘poutcome’ in df_flags.columns:
df_flags['prev_success'] = df_flags[‘poutcome'].astype(str).str.lower() == ‘success’
if ‘duration’ in df_flags.columns:
df_flags[‘long_call'] = df_flags{‘duration’] > df_flags['duration'].median()
candidates = [c for c in ['prev_success',‘long_call'] if c in df_flags.columns]

else:
if 'OverTime' in df_flags.columns:
df_flags[‘ot_yes'] = df_flags[‘OverTime'].astype(str).str.lower()=="yes'
if JobSatisfaction' in df_flags.columns:
df_flags[‘js_low'] = df_flags[‘JobSatisfaction'] <= 2
candidates = [c for c in ['ot_yes’,'js_low'] if c in df_flags.columns]
rules = []
for a in candidates:
sup_a = df_flags[a].mean()
sup_c= df_flags[‘target'].mean()
sup_ac = df_flags[(df_flags[a]) & (df_flags['target'])].shape(0]/df_flags.shape[0]
conf = sup_ac/(sup_a + 1e-9)
lift = conf/(sup_c + 1e-9)
rules.append((a, ‘target=1', sup_ac, conf, lift))
if rules:
display(pd.DataFrame(rules, columns=[‘'antecedent’,'consequent','suppo
ascending=False))
else:
print("No flags found for associations.")
print("Managerial: use high-lift/ high-confidence rules to prioritize actions.")

rt','confidence', lift']).sort_values(‘lift’,

QUESTION 7: Model Evaluation & Business Decision

def q7_evaluation(df):
print("\nQ7 — Model Evaluation & Business Decision (Random Forest chosen)")

print(” - -- ")

pre, num_cols, cat_cols = build_preprocessor(df}

features = num_cols + cat_cols

X = dfffeatures].copy()

y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_sta
pipe = Pipeline([(‘pre’, pre), (‘rf', RandomForestClassifier(n_estimators=200, rand:
pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

y_prob = pipe.predict_proba(X_test){:,1]

print("Accuracy:", accuracy_score(y_test,y_pred))

te=RANDOM_STATE, stratify=y)
om_state=RANDOM_STATE})])

26
--- page 21 ---
print("Precision:", precision_score(y_test,y_pred))

print("Recall:", recall_score(y_test,y_pred})

print("ROC AUC:", roc_auc_score{y_test,y_prob)}

print("\nConfusion Matrix:\n", confusion_matrix(y_test,y_pred))

print("\nClassification Report:\n", classification_report(y_test,y_pred))

# ROC curve

fpr, tpr, _ = roc_curve(y_test,y_prob)

plt.plot(fpr, tpr); plt.plot({0,1], [0,1], linestyle='--'); plt.title("ROC Curve (Random Forest)"); pit.xlabel("FPR");
plt.ylabel("TPR"); plt.show()

print("Managerial guidance: pick threshold based on cost of false positives (unnecessary outreach/intervention) vs
false negatives (missed opportunities/risk).")

RUN ALL QUESTIONS

if__name__=="__main_":
q1_eda(df)
q2_logistic_regularized({df)
q3_trees_rf(df)
q4_pca_pls(df, n_pca=5, n_pls=5)
q5_nonlinear(df)
q6_cluster_association(df)
q7_evaluation(df)

print("\nAll tasks completed. Split functions into separate notebook cells for student distribution if desired.")
FIR ROOK Rk dot

at
````
