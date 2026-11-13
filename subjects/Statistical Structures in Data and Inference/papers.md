# Statistical Structures in Data and Inference: question papers in full

16 unique papers · 2021-22 to 2025-26 · Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 4 · paper e5f42764b88c

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_DS_7009/Statistical Structures in Data and Inference/QP_Statistical Structures in Data and Inference(702DB0C039)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Statistical Structures in Data and Inference
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
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
8. All questions carry equal marks.
Q1   Answer briefly:   [20]
CO-1 ;   a. In a study, physicians were asked what the odds of breast cancer would be in a woman   [5]
SO- 1;
BL-3   who was initially thought to have a 1% risk of cancer but who ended up with a positive
mammogram result (a mammogram accurately classifies about 80% of cancerous
tumors and 90% of benign tumors.) 95 out of a hundred physicians estimated the
probability of cancer to be about 75%. Do you agree?
CO- 3;   b. In the context of Inferential Statistics, the One-Way Analysis of Variance (ANOVA)   [5]
SO- 3;
BL-2   relies on the fundamental principle of partitioning   total variation. Prove
mathematically that the Total Sum of Squares (SST) can be decomposed into the Sum
of Squares Between Groups (SSB) and the Sum of Squares Within Groups (SSW).
CO- 2;   c. Maxwell’s Hot Chocolate is concerned about the effect of the recent year-long coffee   [5]
SO-1;
BL-3   adver-tising campaign on hot chocolate sales. The average weekly hot chocolate
sales two years ago was 984.7 pounds and the standard deviation was 72.6 pounds.
Maxwell’s has randomly selected 30 weeks from the past year and found average
sales of 912.1 pounds.
i.   State appropriate hypotheses for testing whether hot chocolate sales have
decreased.
ii.   At the 2 percent significance level, test these hypotheses.
CO- 6;   d. You have built a Multiple Linear Regression model to predict House Prices based on   [5]
SO- 4;
BL-3   Square Footage area and Distance to Hospital. Your model returns an R2 of 0.85, which
are the major assumptions you have check before concluding the results.
Q2   [20]
********** 1 **********
--- page 2 ---
CO-2;   a. Suppose you are given a sample vector X containing n=100 independent and   [10]
SO-2;
BL-4   identically distributed (i.i.d.) observations. Your goal is to find the parameter vector
theta=(µ,σ) that maximizes the likelihood of the observed data. Construct a function
in python negative_log_likelihood(params, data) that computes the negative sum of
the log-probability density values using scipy.stats.norm.logpdf.
import numpy as np
import scipy.optimize as opt
import scipy.stats as stats
np.random.seed(42)
data = np.random.normal(loc=15, scale=5, size=100)
CO-4;   b. A tech lead claims that a new training program increases coding efficiency. Eight   [10]
SO-2;
BL-4   developers were tested before and after the program.
import numpy as np
from scipy import stats
before_workshop = np.array([22, 25, 18, 30, 20, 24, 28, 21])
after_workshop = np.array([25, 29, 21, 31, 26, 23, 33, 22])
At a 5% significance level (alpha = 0.05), is there sufficient evidence to conclude that
the training improved performance? Write the Python code in your answer book and
provide an interpretation of the results.
Q3
CO-3;   a. Utilizing the HR Promotion Dataset (HR_PR sheet), develop a comprehensive   [10]
SO-2;
BL-4   statistical pipeline to move a global technology firm from a standardized "one-size-
fits-all" promotion model to a data-validated, department-specific advancement
strategy. Do a One-Way ANOVA to determine if the avg_training_score differs
significantly across the various department groups. Furthermore, you must execute a
Tukey HSD post-hoc test o identify specific pairwise differences. Write the Python
code in your answer book and provide an interpretation of the results.
********** 2 **********
--- page 3 ---
CO-1;   b. Suppose you are given a dataset stored in a pandas DataFrame df containing a column   [10]
SO-1;
BL-3   outcome representing binary observations (0 = failure, 1 = success) from a Bernoulli
experiment, along with a grouping variable group with categories ‘A’ and ‘B’. Assume
that observations within each group are independent and identically distributed with
unknown probabilities of success pA_ and pB. Using Maximum Likelihood Estimation
(MLE), construct a Python function negative_log_likelihood(p, data) that computes
the negative log-likelihood using the Bernoulli probability mass function. Then, using
a for loop, estimate the parameters pA_ and pB via numerical optimization. Finally,
compare these estimates with the sample proportions of successes in each group and
interpret the difference in success probabilities between the two groups.
import numpy as np
import pandas as pd
np.random.seed(303)
group_A = np.random.binomial(1, 0.4, size=120)
group_B = np.random.binomial(1, 0.7, size=120)
df = pd.DataFrame({
'outcome': np.concatenate([group_A, group_B]),
'group': ['A']*120 + ['B']*120
})
Q4   [20]
CO-4;   A venture capital firm is evaluating 50 startups across three different states. They want
SO-6;
BL-3   to understand which types of operational expenditures are the strongest predictors of a
startup's Profit. You are provided with the dataset (50_Startups sheet) to build a
predictive model. Write the Python code in your answer book and provide an
interpretation of the results.(note: use dummies and VIF)
Q5   [20]
CO-1;   a. What is likelihood and derive the mathematical expressions for estimating the   [10]
SO-2;
BL-4   parameters for a Binomial distribution using MLE.
********** 3 **********
--- page 4 ---
CO-   b.   [10]
Melisa’s Boutique has three mall locations. Melisa keeps a daily record for each
7;
SO-1;   location of the number of customers who actually make a purchase. A sample of
BL-3
those data follows. Using the Kruskal-Wallis test, can you say at the 0.05 level of
significance that her stores have the same number of customers who buy?
Eastowne Mail   99   64 101   85   79   88   97   95   90 100
Craborchard Mall   83 102 125   61   91   96   94   89   93   75
Fairforest Mall   89   98   56 105   87   90   87 101   76   89
Q 6   [20]
a. An automotive engineer is studying the relationship between Engine Speed (RPM) and   [10]
CO-4;   Fuel Efficiency(Fuel_Efficiency sheet). After collecting 100 data points, an initial
SO-1;
BL-3   Simple Linear Regression model yields an R2 of 0.65. However, the engineer suspects
the relationship is actually quadratic. Check the hypothesis of the engineer. Write the
Python code in your answer book and provide an interpretation of the results
CO-5;   b. Using the Ames House Prices dataset (House_price sheet), demonstrate how to apply   [10]
SO-2;
BL-4   Lasso regularization to manage a high-dimensional feature set of 79 variables.
Specifically, explain the mathematical nature of the L1 penalty term compared to L2
how Lasso’s geometry enables automatic feature selection, and how you would utilize
cross-validation to identify the optimal sparsity level that balances the bias-variance
tradeoff. Write the Python code in your answer book and provide an interpretation of
the results.
Q 7   [20]
CO-2;   a. A researcher wants to determine if Visualization techniques improve memory recall   [10]
SO-1;
BL-3   more effectively than Rote Repetition. Two small groups of students were randomly
assigned to different study methods and asked to memorize a list of 20 words. The
number of words correctly recalled by each student is recorded below:
import numpy as np from scipy
import stats
group1 = np.array([18, 15, 14, 19, 16])
group2 = np.array([12, 14, 11, 15, 13])
At a 5% significance level (alpha = 0.05), does the data provide sufficient evidence to
conclude that Visualization leads to a higher mean recall than Rote Repetition? Note:
Assume the populations are normally distributed with equal variances. Write the
Python code in your answer book and provide an interpretation of the results.
********** 4 **********
--- page 5 ---
CO-6;   b. A global technology firm is facing a stagnating internal promotion rate, leading to a   [10]
SO-2;
BL-4   16% annual turnover rate as high-potential employees leave for better opportunities.
The People Operations department has provided you with the HR Promotion
Dataset(HR_PR sheet). You are tasked with developing a binary classification model
that moves the company from reactive exit interviews to proactive retention and
promotion strategies. Using Python and the Scikit-Learn library, develop a predictive
pipeline to determine the likelihood of an employee being promoted based on five key
drivers:   age,   avg_training_score,   length_of_service, KPIs_met >80%, and
awards_won?. Write the Python code in your answer book and provide an
interpretation of the results.
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 4 · paper 3f509d06e1ab

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_DS_7052/Statistical Structures in Data and Inference/QP_Statistical Structures in Data and Inference(702DB0C039)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Statistical Structures in Data and Inference
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
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
8. All questions carry equal marks.
Q1   Answer briefly:   [20]
CO-1 ;   a. In a study, physicians were asked what the odds of breast cancer would be in a woman   [5]
SO- 1;
BL-3   who was initially thought to have a 1% risk of cancer but who ended up with a positive
mammogram result (a mammogram accurately classifies about 80% of cancerous
tumors and 90% of benign tumors.) 95 out of a hundred physicians estimated the
probability of cancer to be about 75%. Do you agree?
CO- 3;   b. In the context of Inferential Statistics, the One-Way Analysis of Variance (ANOVA)   [5]
SO- 3;
BL-2   relies on the fundamental principle of partitioning   total variation. Prove
mathematically that the Total Sum of Squares (SST) can be decomposed into the Sum
of Squares Between Groups (SSB) and the Sum of Squares Within Groups (SSW).
CO- 2;   c. Maxwell’s Hot Chocolate is concerned about the effect of the recent year-long coffee   [5]
SO-1;
BL-3   adver-tising campaign on hot chocolate sales. The average weekly hot chocolate
sales two years ago was 984.7 pounds and the standard deviation was 72.6 pounds.
Maxwell’s has randomly selected 30 weeks from the past year and found average
sales of 912.1 pounds.
i.   State appropriate hypotheses for testing whether hot chocolate sales have
decreased.
ii.   At the 2 percent significance level, test these hypotheses.
CO- 6;   d. You have built a Multiple Linear Regression model to predict House Prices based on   [5]
SO- 4;
BL-3   Square Footage area and Distance to Hospital. Your model returns an R2 of 0.85, which
are the major assumptions you have check before concluding the results.
Q2   [20]
********** 1 **********
--- page 2 ---
CO-2;   a. Suppose you are given a sample vector X containing n=100 independent and   [10]
SO-2;
BL-4   identically distributed (i.i.d.) observations. Your goal is to find the parameter vector
theta=(µ,σ) that maximizes the likelihood of the observed data. Construct a function
in python negative_log_likelihood(params, data) that computes the negative sum of
the log-probability density values using scipy.stats.norm.logpdf.
import numpy as np
import scipy.optimize as opt
import scipy.stats as stats
np.random.seed(42)
data = np.random.normal(loc=15, scale=5, size=100)
CO-4;   b. A tech lead claims that a new training program increases coding efficiency. Eight   [10]
SO-2;
BL-4   developers were tested before and after the program.
import numpy as np
from scipy import stats
before_workshop = np.array([22, 25, 18, 30, 20, 24, 28, 21])
after_workshop = np.array([25, 29, 21, 31, 26, 23, 33, 22])
At a 5% significance level (alpha = 0.05), is there sufficient evidence to conclude that
the training improved performance? Write the Python code in your answer book and
provide an interpretation of the results.
Q3
CO-3;   a. Utilizing the HR Promotion Dataset (HR_PR sheet), develop a comprehensive   [10]
SO-2;
BL-4   statistical pipeline to move a global technology firm from a standardized "one-size-
fits-all" promotion model to a data-validated, department-specific advancement
strategy. Do a One-Way ANOVA to determine if the avg_training_score differs
significantly across the various department groups. Furthermore, you must execute a
Tukey HSD post-hoc test o identify specific pairwise differences. Write the Python
code in your answer book and provide an interpretation of the results.
********** 2 **********
--- page 3 ---
CO-1;   b. Suppose you are given a dataset stored in a pandas DataFrame df containing a column   [10]
SO-1;
BL-3   outcome representing binary observations (0 = failure, 1 = success) from a Bernoulli
experiment, along with a grouping variable group with categories ‘A’ and ‘B’. Assume
that observations within each group are independent and identically distributed with
unknown probabilities of success pA_ and pB. Using Maximum Likelihood Estimation
(MLE), construct a Python function negative_log_likelihood(p, data) that computes
the negative log-likelihood using the Bernoulli probability mass function. Then, using
a for loop, estimate the parameters pA_ and pB via numerical optimization. Finally,
compare these estimates with the sample proportions of successes in each group and
interpret the difference in success probabilities between the two groups.
import numpy as np
import pandas as pd
np.random.seed(303)
group_A = np.random.binomial(1, 0.4, size=120)
group_B = np.random.binomial(1, 0.7, size=120)
df = pd.DataFrame({
'outcome': np.concatenate([group_A, group_B]),
'group': ['A']*120 + ['B']*120
})
Q4   [20]
CO-4;   A venture capital firm is evaluating 50 startups across three different states. They want
SO-6;
BL-3   to understand which types of operational expenditures are the strongest predictors of a
startup's Profit. You are provided with the dataset (50_Startups sheet) to build a
predictive model. Write the Python code in your answer book and provide an
interpretation of the results.(note: use dummies and VIF)
Q5   [20]
CO-1;   a. What is likelihood and derive the mathematical expressions for estimating the   [10]
SO-2;
BL-4   parameters for a Binomial distribution using MLE.
********** 3 **********
--- page 4 ---
CO-   b.   [10]
Melisa’s Boutique has three mall locations. Melisa keeps a daily record for each
7;
SO-1;   location of the number of customers who actually make a purchase. A sample of
BL-3
those data follows. Using the Kruskal-Wallis test, can you say at the 0.05 level of
significance that her stores have the same number of customers who buy?
Eastowne Mail   99   64 101   85   79   88   97   95   90 100
Craborchard Mall   83 102 125   61   91   96   94   89   93   75
Fairforest Mall   89   98   56 105   87   90   87 101   76   89
Q 6   [20]
a. An automotive engineer is studying the relationship between Engine Speed (RPM) and   [10]
CO-4;   Fuel Efficiency(Fuel_Efficiency sheet). After collecting 100 data points, an initial
SO-1;
BL-3   Simple Linear Regression model yields an R2 of 0.65. However, the engineer suspects
the relationship is actually quadratic. Check the hypothesis of the engineer. Write the
Python code in your answer book and provide an interpretation of the results
CO-5;   b. Using the Ames House Prices dataset (House_price sheet), demonstrate how to apply   [10]
SO-2;
BL-4   Lasso regularization to manage a high-dimensional feature set of 79 variables.
Specifically, explain the mathematical nature of the L1 penalty term compared to L2
how Lasso’s geometry enables automatic feature selection, and how you would utilize
cross-validation to identify the optimal sparsity level that balances the bias-variance
tradeoff. Write the Python code in your answer book and provide an interpretation of
the results.
Q 7   [20]
CO-2;   a. A researcher wants to determine if Visualization techniques improve memory recall   [10]
SO-1;
BL-3   more effectively than Rote Repetition. Two small groups of students were randomly
assigned to different study methods and asked to memorize a list of 20 words. The
number of words correctly recalled by each student is recorded below:
import numpy as np from scipy
import stats
group1 = np.array([18, 15, 14, 19, 16])
group2 = np.array([12, 14, 11, 15, 13])
At a 5% significance level (alpha = 0.05), does the data provide sufficient evidence to
conclude that Visualization leads to a higher mean recall than Rote Repetition? Note:
Assume the populations are normally distributed with equal variances. Write the
Python code in your answer book and provide an interpretation of the results.
********** 4 **********
--- page 5 ---
CO-6;   b. A global technology firm is facing a stagnating internal promotion rate, leading to a   [10]
SO-2;
BL-4   16% annual turnover rate as high-potential employees leave for better opportunities.
The People Operations department has provided you with the HR Promotion
Dataset(HR_PR sheet). You are tasked with developing a binary classification model
that moves the company from reactive exit interviews to proactive retention and
promotion strategies. Using Python and the Scikit-Learn library, develop a predictive
pipeline to determine the likelihood of an employee being promoted based on five key
drivers:   age,   avg_training_score,   length_of_service, KPIs_met >80%, and
awards_won?. Write the Python code in your answer book and provide an
interpretation of the results.
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 8 · paper faaf91d0c490

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_DS_7038/Statistical Structures in Data and Inference/QP_Statistical Structures in Data and Inference(702DB0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Statistical Structures in Data and Inference
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
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
8. All questions carry equal marks.
Q1   Answer briefly:   [20]
CO-1 ;   a. In a study, physicians were asked what the odds of breast cancer would be in a woman   [5]
SO- 1;
BL-3   who was initially thought to have a 1% risk of cancer but who ended up with a positive
mammogram result (a mammogram accurately classifies about 80% of cancerous
tumors and 90% of benign tumors.) 95 out of a hundred physicians estimated the
probability of cancer to be about 75%. Do you agree?
CO- 3;   b. In the context of Inferential Statistics, the One-Way Analysis of Variance (ANOVA)   [5]
SO- 3;
BL-2   relies on the fundamental principle of partitioning   total variation. Prove
mathematically that the Total Sum of Squares (SST) can be decomposed into the Sum
of Squares Between Groups (SSB) and the Sum of Squares Within Groups (SSW).
CO- 2;   c. Maxwell’s Hot Chocolate is concerned about the effect of the recent year-long coffee   [5]
SO-1;
BL-3   adver-tising campaign on hot chocolate sales. The average weekly hot chocolate
sales two years ago was 984.7 pounds and the standard deviation was 72.6 pounds.
Maxwell’s has randomly selected 30 weeks from the past year and found average
sales of 912.1 pounds.
i.   State appropriate hypotheses for testing whether hot chocolate sales have
decreased.
ii.   At the 2 percent significance level, test these hypotheses.
CO- 6;   d. You have built a Multiple Linear Regression model to predict House Prices based on   [5]
SO- 4;
BL-3   Square Footage area and Distance to Hospital. Your model returns an R2 of 0.85, which
are the major assumptions you have check before concluding the results.
Q2   [20]
********** 1 **********
--- page 2 ---
CO-2;   a. Suppose you are given a sample vector X containing n=100 independent and   [10]
SO-2;
BL-4   identically distributed (i.i.d.) observations. Your goal is to find the parameter vector
theta=(µ,σ) that maximizes the likelihood of the observed data. Construct a function
in python negative_log_likelihood(params, data) that computes the negative sum of
the log-probability density values using scipy.stats.norm.logpdf.
import numpy as np
import scipy.optimize as opt
import scipy.stats as stats
np.random.seed(42)
data = np.random.normal(loc=15, scale=5, size=100)
CO-4;   b. A tech lead claims that a new training program increases coding efficiency. Eight   [10]
SO-2;
BL-4   developers were tested before and after the program.
import numpy as np
from scipy import stats
before_workshop = np.array([22, 25, 18, 30, 20, 24, 28, 21])
after_workshop = np.array([25, 29, 21, 31, 26, 23, 33, 22])
At a 5% significance level (alpha = 0.05), is there sufficient evidence to conclude that
the training improved performance? Write the Python code in your answer book and
provide an interpretation of the results.
Q3
CO-3;   a. Utilizing the HR Promotion Dataset (HR_PR sheet), develop a comprehensive   [10]
SO-2;
BL-4   statistical pipeline to move a global technology firm from a standardized "one-size-
fits-all" promotion model to a data-validated, department-specific advancement
strategy. Do a One-Way ANOVA to determine if the avg_training_score differs
significantly across the various department groups. Furthermore, you must execute a
Tukey HSD post-hoc test o identify specific pairwise differences. Write the Python
code in your answer book and provide an interpretation of the results.
********** 2 **********
--- page 3 ---
CO-1;   b. Suppose you are given a dataset stored in a pandas DataFrame df containing a column   [10]
SO-1;
BL-3   outcome representing binary observations (0 = failure, 1 = success) from a Bernoulli
experiment, along with a grouping variable group with categories ‘A’ and ‘B’. Assume
that observations within each group are independent and identically distributed with
unknown probabilities of success pA_ and pB. Using Maximum Likelihood Estimation
(MLE), construct a Python function negative_log_likelihood(p, data) that computes
the negative log-likelihood using the Bernoulli probability mass function. Then, using
a for loop, estimate the parameters pA_ and pB via numerical optimization. Finally,
compare these estimates with the sample proportions of successes in each group and
interpret the difference in success probabilities between the two groups.
import numpy as np
import pandas as pd
np.random.seed(303)
group_A = np.random.binomial(1, 0.4, size=120)
group_B = np.random.binomial(1, 0.7, size=120)
df = pd.DataFrame({
'outcome': np.concatenate([group_A, group_B]),
'group': ['A']*120 + ['B']*120
})
Q4   [20]
CO-4;   A venture capital firm is evaluating 50 startups across three different states. They want
SO-6;
BL-3   to understand which types of operational expenditures are the strongest predictors of a
startup's Profit. You are provided with the dataset (50_Startups sheet) to build a
predictive model. Write the Python code in your answer book and provide an
interpretation of the results.(note: use dummies and VIF)
Q5   [20]
CO-1;   a. What is likelihood and derive the mathematical expressions for estimating the   [10]
SO-2;
BL-4   parameters for a Binomial distribution using MLE.
********** 3 **********
--- page 4 ---
CO-   b.   [10]
Melisa’s Boutique has three mall locations. Melisa keeps a daily record for each
7;
SO-1;   location of the number of customers who actually make a purchase. A sample of
BL-3
those data follows. Using the Kruskal-Wallis test, can you say at the 0.05 level of
significance that her stores have the same number of customers who buy?
Eastowne Mail   99   64 101   85   79   88   97   95   90 100
Craborchard Mall   83 102 125   61   91   96   94   89   93   75
Fairforest Mall   89   98   56 105   87   90   87 101   76   89
Q 6   [20]
a. An automotive engineer is studying the relationship between Engine Speed (RPM) and   [10]
CO-4;   Fuel Efficiency(Fuel_Efficiency sheet). After collecting 100 data points, an initial
SO-1;
BL-3   Simple Linear Regression model yields an R2 of 0.65. However, the engineer suspects
the relationship is actually quadratic. Check the hypothesis of the engineer. Write the
Python code in your answer book and provide an interpretation of the results
CO-5;   b. Using the Ames House Prices dataset (House_price sheet), demonstrate how to apply   [10]
SO-2;
BL-4   Lasso regularization to manage a high-dimensional feature set of 79 variables.
Specifically, explain the mathematical nature of the L1 penalty term compared to L2
how Lasso’s geometry enables automatic feature selection, and how you would utilize
cross-validation to identify the optimal sparsity level that balances the bias-variance
tradeoff. Write the Python code in your answer book and provide an interpretation of
the results.
Q 7   [20]
CO-2;   a. A researcher wants to determine if Visualization techniques improve memory recall   [10]
SO-1;
BL-3   more effectively than Rote Repetition. Two small groups of students were randomly
assigned to different study methods and asked to memorize a list of 20 words. The
number of words correctly recalled by each student is recorded below:
import numpy as np from scipy
import stats
group1 = np.array([18, 15, 14, 19, 16])
group2 = np.array([12, 14, 11, 15, 13])
At a 5% significance level (alpha = 0.05), does the data provide sufficient evidence to
conclude that Visualization leads to a higher mean recall than Rote Repetition? Note:
Assume the populations are normally distributed with equal variances. Write the
Python code in your answer book and provide an interpretation of the results.
********** 4 **********
--- page 5 ---
CO-6;   b. A global technology firm is facing a stagnating internal promotion rate, leading to a   [10]
SO-2;
BL-4   16% annual turnover rate as high-potential employees leave for better opportunities.
The People Operations department has provided you with the HR Promotion
Dataset(HR_PR sheet). You are tasked with developing a binary classification model
that moves the company from reactive exit interviews to proactive retention and
promotion strategies. Using Python and the Scikit-Learn library, develop a predictive
pipeline to determine the likelihood of an employee being promoted based on five key
drivers:   age,   avg_training_score,   length_of_service, KPIs_met >80%, and
awards_won?. Write the Python code in your answer book and provide an
interpretation of the results.
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 4 · Dataset · paper 1239cfc80b5c

- Departments: Data Science
- Programmes: BTech DS 7009, Integrated DS 7038, MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_DS_7009/Statistical Structures in Data and Inference/data_set_Statistical Structures in Data and Inference(702DB0C039)_2025-2026.xlsx` (+2 identical copies)
- Text: xlsx (4 sheets)

````text
Sheet "50_startups": 51 rows, 5 columns

R&D Spend | Administration | Marketing Spend | State | Profit
165349.2 | 136897.8 | 471784.1 | New York | 192261.83
162597.7 | 151377.59 | 443898.53 | California | 191792.06
153441.51 | 101145.55 | 407934.54 | Florida | 191050.39
144372.41 | 118671.85 | 383199.62 | New York | 182901.99
142107.34 | 91391.77 | 366168.42 | Florida | 166187.94
131876.9 | 99814.71 | 362861.36 | New York | 156991.12
134615.46 | 147198.87 | 127716.82 | California | 156122.51
130298.13 | 145530.06 | 323876.68 | Florida | 155752.6
120542.52 | 148718.95 | 311613.29 | New York | 152211.77
123334.88 | 108679.17 | 304981.62 | California | 149759.96
101913.08 | 110594.11 | 229160.95 | Florida | 146121.95
100671.96 | 91790.61 | 249744.55 | California | 144259.4
93863.75 | 127320.38 | 249839.44 | Florida | 141585.52
91992.39 | 135495.07 | 252664.93 | California | 134307.35
119943.24 | 156547.42 | 256512.92 | Florida | 132602.65
114523.61 | 122616.84 | 261776.23 | New York | 129917.04
78013.11 | 121597.55 | 264346.06 | California | 126992.93
94657.16 | 145077.58 | 282574.31 | New York | 125370.37
91749.16 | 114175.79 | 294919.57 | Florida | 124266.9
86419.7 | 153514.11 | 0 | New York | 122776.86
76253.86 | 113867.3 | 298664.47 | California | 118474.03
78389.47 | 153773.43 | 299737.29 | New York | 111313.02
73994.56 | 122782.75 | 303319.26 | Florida | 110352.25
67532.53 | 105751.03 | 304768.73 | Florida | 108733.99
77044.01 | 99281.34 | 140574.81 | New York | 108552.04
64664.71 | 139553.16 | 137962.62 | California | 107404.34
75328.87 | 144135.98 | 134050.07 | Florida | 105733.54
72107.6 | 127864.55 | 353183.81 | New York | 105008.31
66051.52 | 182645.56 | 118148.2 | Florida | 103282.38
65605.48 | 153032.06 | 107138.38 | New York | 101004.64
61994.48 | 115641.28 | 91131.24 | Florida | 99937.59
61136.38 | 152701.92 | 88218.23 | New York | 97483.56
63408.86 | 129219.61 | 46085.25 | California | 97427.84
55493.95 | 103057.49 | 214634.81 | Florida | 96778.92
46426.07 | 157693.92 | 210797.67 | California | 96712.8
46014.02 | 85047.44 | 205517.64 | New York | 96479.51
28663.76 | 127056.21 | 201126.82 | Florida | 90708.19
44069.95 | 51283.14 | 197029.42 | California | 89949.14
20229.59 | 65947.93 | 185265.1 | New York | 81229.06
38558.51 | 82982.09 | 174999.3 | California | 81005.76
28754.33 | 118546.05 | 172795.67 | California | 78239.91
27892.92 | 84710.77 | 164470.71 | Florida | 77798.83
23640.93 | 96189.63 | 148001.11 | California | 71498.49
15505.73 | 127382.3 | 35534.17 | New York | 69758.98
22177.74 | 154806.14 | 28334.72 | California | 65200.33
1000.23 | 124153.04 | 1903.93 | New York | 64926.08
1315.46 | 115816.21 | 297114.46 | Florida | 49490.75
0 | 135426.92 | 0 | California | 42559.73
542.05 | 51743.15 | 0 | New York | 35673.41
0 | 116983.8 | 45173.06 | California | 14681.4
--- page 2 ---
Sheet "Fuel _Efficiency": 101 rows, 2 columns

Engine_Speed | Efficiency
3.745401188 | 5.951905602
9.507143064 | 26.07344073
7.319939418 | 15.01445984
5.986584842 | 5.98470668
1.560186404 | 6.097187819
1.559945203 | 7.251104052
0.580836122 | 11.38196502
8.661761458 | 20.49123097
6.011150117 | 8.416525309
7.080725778 | 12.82264735
0.205844943 | 11.23445548
9.699098522 | 28.59646272
8.324426408 | 18.61523788
2.1233911069999998 | 6.910756442
1.818249672 | 6.392422017
1.834045099 | 8.117015397
3.04242243 | 4.096793644
5.247564316 | 7.370448385
4.319450186 | 5.586258091
2.912291402 | 2.576816503
6.118528947 | 10.95485195
1.394938607 | 7.310221583
2.921446485 | 5.513312241
3.663618433 | 5.251020446
4.560699842 | 3.887150515
7.851759614 | 16.42849503
1.996737822 | 5.317838466
5.142344384 | 6.190265192
5.924145689 | 9.452742581
0.464504127 | 9.522471374
6.075448519 | 14.0015636
1.705241237 | 6.687355753
0.65051593 | 8.775138479
9.488855373 | 26.40373019
9.656320331 | 23.81575774
8.083973481 | 18.37036543
3.046137692 | 5.621524763
0.97672114 | 12.4733129
6.842330265 | 12.497029
4.401524937 | 7.08523076
1.220382348 | 7.014095953
4.951769101 | 5.067345237
0.343885211 | 11.31311851
9.093204021 | 25.56743368
2.587799816 | 7.16701839
6.625222844 | 10.25234542
3.117110761 | 8.312446087
5.200680212 | 5.117794572
5.467102793 | 9.717012284
1.848544555 | 10.54383607
9.695846278 | 25.93610604
7.751328234 | 15.65496453
9.394989416 | 26.14724754
8.948273504 | 22.18402753
5.978999788 | 6.835893007
9.21874235 | 24.97350416
0.884925021 | 5.612163657
1.959828624 | 6.988163107
0.452272889 | 6.906608247
3.253303308 | 8.631950093
3.886772897 | 4.326676501
2.713490318 | 4.896920867
8.287375092 | 21.10520211
3.567533267 | 3.199318372
2.809345097 | 5.973094515
5.426960832 | 11.05935495
1.40924225 | 3.550288641
8.021969808 | 18.47935809
0.745506437 | 8.561136202
9.868869366 | 30.65432893
7.722447693 | 14.17685468
1.987156815 | 3.372012432
0.055221171 | 10.87974431
8.154614285 | 19.37899356
7.068573438 | 14.27763061
7.29007168 | 15.39525393
7.712703467 | 15.24473754
0.740446517 | 8.517298365
3.584657285 | 6.257057017
1.158690595 | 5.766507326
8.631034259 | 25.08582243
6.232981268 | 11.67374978
3.308980249 | 3.165127403
0.635583503 | 9.608339903
3.109823217 | 3.556667229
3.25183322 | 7.105879193
7.296061783 | 17.04526458
6.375574714 | 9.555887687
8.872127426 | 24.66769251
4.722149252 | 7.808460876
1.195942459 | 8.771432125
7.132447872 | 17.83214867
7.607850486 | 15.62536682
5.612771976 | 7.40581637
7.7096718 | 14.81147537
4.937955964 | 5.746216089
5.227328294 | 7.826292245
4.275410184 | 6.995639518
0.254191267 | 9.823114397
1.07891427 | 8.999651689
--- page 3 ---
Sheet "House_price": 1461 rows, 260 columns; the first 8 rows are shown, the full data set is in the original file

MSSubClass | LotFrontage | LotArea | OverallQual | OverallCond | YearBuilt | YearRemodAdd | MasVnrArea | BsmtFinSF1 | BsmtFinSF2 | BsmtUnfSF | TotalBsmtSF | 1stFlrSF | 2ndFlrSF | LowQualFinSF | GrLivArea | BsmtFullBath | BsmtHalfBath | FullBath | HalfBath | BedroomAbvGr | KitchenAbvGr | TotRmsAbvGrd | Fireplaces | GarageYrBlt | GarageCars | GarageArea | WoodDeckSF | OpenPorchSF | EnclosedPorch | 3SsnPorch | ScreenPorch | PoolArea | MiscVal | MoSold | YrSold | TotalSF | MSZoning_FV | MSZoning_RH | MSZoning_RL | MSZoning_RM | Street_Pave | Alley_None | Alley_Pave | LotShape_IR2 | LotShape_IR3 | LotShape_Reg | LandContour_HLS | LandContour_Low | LandContour_Lvl | Utilities_NoSeWa | LotConfig_CulDSac | LotConfig_FR2 | LotConfig_FR3 | LotConfig_Inside | LandSlope_Mod | LandSlope_Sev | Neighborhood_Blueste | Neighborhood_BrDale | Neighborhood_BrkSide | Neighborhood_ClearCr | Neighborhood_CollgCr | Neighborhood_Crawfor | Neighborhood_Edwards | Neighborhood_Gilbert | Neighborhood_IDOTRR | Neighborhood_MeadowV | Neighborhood_Mitchel | Neighborhood_NAmes | Neighborhood_NPkVill | Neighborhood_NWAmes | Neighborhood_NoRidge | Neighborhood_NridgHt | Neighborhood_OldTown | Neighborhood_SWISU | Neighborhood_Sawyer | Neighborhood_SawyerW | Neighborhood_Somerst | Neighborhood_StoneBr | Neighborhood_Timber | Neighborhood_Veenker | Condition1_Feedr | Condition1_Norm | Condition1_PosA | Condition1_PosN | Condition1_RRAe | Condition1_RRAn | Condition1_RRNe | Condition1_RRNn | Condition2_Feedr | Condition2_Norm | Condition2_PosA | Condition2_PosN | Condition2_RRAe | Condition2_RRAn | Condition2_RRNn | BldgType_2fmCon | BldgType_Duplex | BldgType_Twnhs | BldgType_TwnhsE | HouseStyle_1.5Unf | HouseStyle_1Story | HouseStyle_2.5Fin | HouseStyle_2.5Unf | HouseStyle_2Story | HouseStyle_SFoyer | HouseStyle_SLvl | RoofStyle_Gable | RoofStyle_Gambrel | RoofStyle_Hip | RoofStyle_Mansard | RoofStyle_Shed | RoofMatl_CompShg | RoofMatl_Membran | RoofMatl_Metal | RoofMatl_Roll | RoofMatl_Tar&Grv | RoofMatl_WdShake | RoofMatl_WdShngl | Exterior1st_AsphShn | Exterior1st_BrkComm | Exterior1st_BrkFace | Exterior1st_CBlock | Exterior1st_CemntBd | Exterior1st_HdBoard | Exterior1st_ImStucc | Exterior1st_MetalSd | Exterior1st_Plywood | Exterior1st_Stone | Exterior1st_Stucco | Exterior1st_VinylSd | Exterior1st_Wd Sdng | Exterior1st_WdShing | Exterior2nd_AsphShn | Exterior2nd_Brk Cmn | Exterior2nd_BrkFace | Exterior2nd_CBlock | Exterior2nd_CmentBd | Exterior2nd_HdBoard | Exterior2nd_ImStucc | Exterior2nd_MetalSd | Exterior2nd_Other | Exterior2nd_Plywood | Exterior2nd_Stone | Exterior2nd_Stucco | Exterior2nd_VinylSd | Exterior2nd_Wd Sdng | Exterior2nd_Wd Shng | MasVnrType_BrkFace | MasVnrType_None | MasVnrType_Stone | ExterQual_Fa | ExterQual_Gd | ExterQual_TA | ExterCond_Fa | ExterCond_Gd | ExterCond_Po | ExterCond_TA | Foundation_CBlock | Foundation_PConc | Foundation_Slab | Foundation_Stone | Foundation_Wood | BsmtQual_Fa | BsmtQual_Gd | BsmtQual_None | BsmtQual_TA | BsmtCond_Gd | BsmtCond_None | BsmtCond_Po | BsmtCond_TA | BsmtExposure_Gd | BsmtExposure_Mn | BsmtExposure_No | BsmtExposure_None | BsmtFinType1_BLQ | BsmtFinType1_GLQ | BsmtFinType1_LwQ | BsmtFinType1_None | BsmtFinType1_Rec | BsmtFinType1_Unf | BsmtFinType2_BLQ | BsmtFinType2_GLQ | BsmtFinType2_LwQ | BsmtFinType2_None | BsmtFinType2_Rec | BsmtFinType2_Unf | Heating_GasA | Heating_GasW | Heating_Grav | Heating_OthW | Heating_Wall | HeatingQC_Fa | HeatingQC_Gd | HeatingQC_Po | HeatingQC_TA | CentralAir_Y | Electrical_FuseF | Electrical_FuseP | Electrical_Mix | Electrical_SBrkr | KitchenQual_Fa | KitchenQual_Gd | KitchenQual_TA | Functional_Maj2 | Functional_Min1 | Functional_Min2 | Functional_Mod | Functional_Sev | Functional_Typ | FireplaceQu_Fa | FireplaceQu_Gd | FireplaceQu_None | FireplaceQu_Po | FireplaceQu_TA | GarageType_Attchd | GarageType_Basment | GarageType_BuiltIn | GarageType_CarPort | GarageType_Detchd | GarageType_None | GarageFinish_None | GarageFinish_RFn | GarageFinish_Unf | GarageQual_Fa | GarageQual_Gd | GarageQual_None | GarageQual_Po | GarageQual_TA | GarageCond_Fa | GarageCond_Gd | GarageCond_None | GarageCond_Po | GarageCond_TA | PavedDrive_P | PavedDrive_Y | PoolQC_Fa | PoolQC_Gd | PoolQC_None | Fence_GdWo | Fence_MnPrv | Fence_MnWw | Fence_None | MiscFeature_None | MiscFeature_Othr | MiscFeature_Shed | MiscFeature_TenC | SaleType_CWD | SaleType_Con | SaleType_ConLD | SaleType_ConLI | SaleType_ConLw | SaleType_New | SaleType_Oth | SaleType_WD | SaleCondition_AdjLand | SaleCondition_Alloca | SaleCondition_Family | SaleCondition_Normal | SaleCondition_Partial
60 | 65 | 8450 | 7 | 5 | 2003 | 2003 | 196 | 706 | 0 | 150 | 856 | 856 | 854 | 0 | 1710 | 1 | 0 | 2 | 1 | 3 | 1 | 8 | 0 | 2003 | 2 | 548 | 0 | 61 | 0 | 0 | 0 | 0 | 0 | 2 | 2008 | 2566 | FALSE | FALSE | TRUE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE
20 | 80 | 9600 | 6 | 8 | 1976 | 1976 | 0 | 978 | 0 | 284 | 1262 | 1262 | 0 | 0 | 1262 | 0 | 1 | 2 | 0 | 3 | 1 | 6 | 1 | 1976 | 2 | 460 | 298 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 2007 | 2524 | FALSE | FALSE | TRUE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE
60 | 68 | 11250 | 7 | 5 | 2001 | 2002 | 162 | 486 | 0 | 434 | 920 | 920 | 866 | 0 | 1786 | 1 | 0 | 2 | 1 | 3 | 1 | 6 | 1 | 2001 | 2 | 608 | 0 | 42 | 0 | 0 | 0 | 0 | 0 | 9 | 2008 | 2706 | FALSE | FALSE | TRUE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE
70 | 60 | 9550 | 7 | 5 | 1915 | 1970 | 0 | 216 | 0 | 540 | 756 | 961 | 756 | 0 | 1717 | 1 | 0 | 1 | 0 | 3 | 1 | 7 | 1 | 1998 | 3 | 642 | 0 | 35 | 272 | 0 | 0 | 0 | 0 | 2 | 2006 | 2473 | FALSE | FALSE | TRUE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE
60 | 84 | 14260 | 8 | 5 | 2000 | 2000 | 350 | 655 | 0 | 490 | 1145 | 1145 | 1053 | 0 | 2198 | 1 | 0 | 2 | 1 | 4 | 1 | 9 | 1 | 2000 | 3 | 836 | 192 | 84 | 0 | 0 | 0 | 0 | 0 | 12 | 2008 | 3343 | FALSE | FALSE | TRUE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE
50 | 85 | 14115 | 5 | 5 | 1993 | 1995 | 0 | 732 | 0 | 64 | 796 | 796 | 566 | 0 | 1362 | 1 | 0 | 1 | 1 | 1 | 1 | 5 | 0 | 1993 | 2 | 480 | 40 | 30 | 0 | 320 | 0 | 0 | 700 | 10 | 2009 | 2158 | FALSE | FALSE | TRUE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE
20 | 75 | 10084 | 8 | 5 | 2004 | 2005 | 186 | 1369 | 0 | 317 | 1686 | 1694 | 0 | 0 | 1694 | 1 | 0 | 2 | 0 | 3 | 1 | 7 | 1 | 2004 | 2 | 636 | 255 | 57 | 0 | 0 | 0 | 0 | 0 | 8 | 2007 | 3380 | FALSE | FALSE | TRUE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | TRUE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | TRUE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE | FALSE | FALSE | FALSE | TRUE | FALSE
--- page 4 ---
Sheet "HR-PR": 54809 rows, 14 columns; the first 25 rows are shown, the full data set is in the original file

employee_id | department | region | education | gender | recruitment_channel | no_of_trainings | age | previous_year_rating | length_of_service | KPIs_met >80% | awards_won? | avg_training_score | is_promoted
65438 | Sales & Marketing | region_7 | Master's & above | f | sourcing | 1 | 35 | 5 | 8 | 1 | 0 | 49 | 0
65141 | Operations | region_22 | Bachelor's | m | other | 1 | 30 | 5 | 4 | 0 | 0 | 60 | 0
7513 | Sales & Marketing | region_19 | Bachelor's | m | sourcing | 1 | 34 | 3 | 7 | 0 | 0 | 50 | 0
2542 | Sales & Marketing | region_23 | Bachelor's | m | other | 2 | 39 | 1 | 10 | 0 | 0 | 50 | 0
48945 | Technology | region_26 | Bachelor's | m | other | 1 | 45 | 3 | 2 | 0 | 0 | 73 | 0
58896 | Analytics | region_2 | Bachelor's | m | sourcing | 2 | 31 | 3 | 7 | 0 | 0 | 85 | 0
20379 | Operations | region_20 | Bachelor's | f | other | 1 | 31 | 3 | 5 | 0 | 0 | 59 | 0
16290 | Operations | region_34 | Master's & above | m | sourcing | 1 | 33 | 3 | 6 | 0 | 0 | 63 | 0
73202 | Analytics | region_20 | Bachelor's | m | other | 1 | 28 | 4 | 5 | 0 | 0 | 83 | 0
28911 | Sales & Marketing | region_1 | Master's & above | m | sourcing | 1 | 32 | 5 | 5 | 1 | 0 | 54 | 0
29934 | Technology | region_23 |   | m | sourcing | 1 | 30 |   | 1 | 0 | 0 | 77 | 0
49017 | Sales & Marketing | region_7 | Bachelor's | f | sourcing | 1 | 35 | 5 | 3 | 1 | 0 | 50 | 1
60051 | Sales & Marketing | region_4 | Bachelor's | m | sourcing | 1 | 49 | 5 | 5 | 1 | 0 | 49 | 0
38401 | Technology | region_29 | Master's & above | m | other | 2 | 39 | 3 | 16 | 0 | 0 | 80 | 0
77040 | R&D | region_2 | Master's & above | m | sourcing | 1 | 37 | 3 | 7 | 0 | 0 | 84 | 0
43931 | Operations | region_7 | Bachelor's | m | other | 1 | 37 | 1 | 10 | 0 | 0 | 60 | 0
7152 | Technology | region_2 | Bachelor's | m | other | 1 | 38 | 3 | 5 | 1 | 0 | 77 | 0
9403 | Sales & Marketing | region_31 | Bachelor's | m | other | 1 | 34 | 1 | 4 | 0 | 0 | 51 | 0
17436 | Sales & Marketing | region_31 | Bachelor's | m | other | 1 | 34 | 5 | 8 | 1 | 0 | 46 | 0
54461 | Operations | region_15 | Bachelor's | m | other | 1 | 37 | 3 | 9 | 0 | 0 | 59 | 0
12067 | Procurement | region_14 | Bachelor's | m | other | 1 | 35 | 3 | 7 | 0 | 0 | 75 | 0
33332 | Operations | region_15 |   | m | sourcing | 1 | 41 | 4 | 11 | 0 | 0 | 57 | 0
58789 | Finance | region_11 | Bachelor's | f | other | 1 | 28 | 3 | 4 | 0 | 0 | 63 | 0
71177 | Procurement | region_5 | Bachelor's | m | other | 1 | 27 |   | 1 | 0 | 0 | 70 | 0
````

## 2025-26 · Re-Exam · Sem 4 · paper 87e493db6836

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, B.TECH INTEGRATED / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/STATISTICAL STRUCTURES IN DATA AND INFERENCE/Statistical Structures in Data and Inference Batch 2023-24,2024-25,2025-26 Re Exam.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; exam date: 06 July 2026
- Text: ocr (4 pages), mean OCR confidence 86.1
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
Program: B Tech/ MBA Tech/ B Tech Intg (DS)

Subject: Statistical Structures in Data and Inference

Date : 06 July 2026

Marks: 100

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING
Academic Year: 2025-26

Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any 4 _ questions.
6. Inall__5_ questions to be attempted.
7. Assume Suitable data if necessary.
8. All questions carry equal marks.

Ql Answer briefly: [20]
(co- a. | It is estimated that 50% of emails are spam emails. Some software has been applied to [5]
| so. 1; filter these spam emails before they reach your inbox. A certain brand of software
BLS claims that it can detect 99% of spam emails, and the probability for a false positive (a
non-spam email detected as spam) is 5%.-Now if an email is detected as spam, then
what is the probability that it is in fact a non-spam email?
SOs b. Prove mathematically that the Total Sum of Squares can be decomposed into the Sum [5]
35 of Squares Between Groups and the Sum of Squares Within Groups.
BL-2
| co- c. Atlas Sporting Goods has implemented a special trade promotion for its propane [5]
7 Bie stove and feels that the promotion should result in a price change for the
° consumer. Atlas knows that before the promotion began, the average retail price
of the stove was $44.95, and the standard deviation was $5.75. Atlas samples 25
{> of its retailers after the promotion begins and finds the mean price for the stoves
| is now $42.95. At a 0.02 significance level, does Atlas have reason to believe that
| the average retail price to the consumer has decreased?
| co i d. | Explain R? (R-squared) and its importance in regression analysis [5]
4; BL-
[a2 | [20]
| . a. | Suppose you are given a dataset stored in a pandas DataFrame df containing two groups [10]
BL-4 _ of observations labeled ‘A’ and ‘B’, each consisting of independent and identically

_distyibuted samples drawn from normal distributions with unknown parameters. Your

objective is to estimate the parameter vectors 0A= (uA,oA) and 0B=(1B,oB) using

% FOR 7] or
--- page 2 ---
Maximum Likelihood Estimation (MLE). Construct a Python — function
_ negative log likelihood (params, data) that computes the negative sum of the log-
_ probability density values using scipy.stats.norm.logpdf separately for each group.
| Then, apply a numerical optimization technique to estimate the optimal values of the
| means and standard deviations for both groups. Finally, compare the estimated
» parameters with the sample mean and standard deviation of each group and interpret
“the differences between the two distributions
| | import numpy as np
import pandas as pd

np.random.seed(42)
group_A = np.random.normal(loc=5, scale=1.5, size=100)
_ group_B = np.random.normal(loc=10, scale=2.0, size=100)
| df = pd.DataFrame({
| ‘values’: np.concatenate([group_A, group_B]),

‘group’: ['A']*100 + ['B']*100 : 4%
»)

b. | Acar manufacturer knows the industry standard defect rate is 3% (p = 0.03). They [10]
_test Line A and find 18 defects in 200 cars. At a 5% significance level (alpha =
0.05), is the defect rate of Line A significantly higher than the industry standard?

Write the Python code in your answer book and provide an interpretation of the

| results.

| import numpy as np

from scipy import stats

| n= 200 defects = 18

line_a = np.concatenate([np.ones(defects), np.zeros(n - defects)])

p_hat = np.mean(line_a)

___ ie ne fee
Q3 | ; [20]
| oe a. | Utilizing the IBM HR Analytics Dataset(IBM_HR sheet), develop a Python-based [10]
| BL-4 _ analytical pipeline to move a global technology firm from reactive exit interviews to
| proactive retention strategies by first conducting a One-Way ANOVA to determine if i
| Monthly Income differs significantly across Department groups, followed by a Tukey
HSD post-hoc test to identify specific pairwise differences between divisions. Write
_ the Python code in your answer book ‘and provide an interpretation of the results.
CO; b. ; A binary dataset representing outcomes of a Bernoulli experiment (taking values 0 for [10]

| #
| BL-3 ,

failure and | for success) is generated using Python. Using this data, formulate the

FRR DOR EE

.
--- page 3 ---
CC |

| likelihood and log-likelihood functions for the Bernoulli distribution and apply the
| concept of Maximum Likelihood Estimation (MLE) to estimate the parameter p,, the
probability of success. Implement the estimation in Python using both the analytical
(closed-form) solution and a numerical optimization approach, and interpret the
estimated value of p in the context of the observed data.

import numpy as np

np.random.seed(42)

data = np.random.binomial(1, 0.6, size=100)

Q4 [20]
| CO-4; Using the dataset (50 Startups sheet), build a regression model to identify which
a operational expenditures significantly affect Profit by applying dummy variables and
checking multicollinearity using VIF, and interpret the results. Write the Python code
in your answer book and provide an interpretation of the results.
| Q5 , [20]
ee a. Derive the mathematical expressions for estimating the parameters for a Normal [10]
| BL-4 distribution using MLE.
| sOat b. The following data show employees’, rates of defective work before and after a [10]
BL-3 change in the wage incentive plan. Compare the following two sets of data using
| | sign- test to see whether the change lowered the defective units produced. Use the
| 0.10 level of significance.
Before 8. 7 6 9 7} 10 8 6 5 8 | 10 8.
| After |6 5 8 6 9| 8/10 7 5 6/9 8
Q6 | (20)
a. | Develop a Multiple Linear Regression model using the insurance dataset (insurance [10]
CO-4; sheet) to predict annual health insurance charges based on age, bmi, and smoker status,
| ae while specifically explaining how you would handle the categorical smoker variable.
| Write the Python code in your answer book and provide an interpretation of the results.
| CO%5; b. Using the House Prices dataset (House_price sheet), can you demonstrate how to apply [10]
ee Ridge regularization to manage a high-dimensional feature set of 79 variables,

| BL-4

_ specifically explaining the mathematical difference in their penalty terms, how you
.

would utilize cross-validation to determine the optimal tuning parameter to balance the

bias-variance tradeoff? Write the Python code in your answer book and provide an

|
interpretation of the results.

kadai lelaieladelt Wadedeeiaielaieltel
--- page 4 ---
Q7

_ A car manufacturer wants to compare two assembly lines.

| import numpy as np

_ from scipy import stats

‘line_a= np.concatenate([np.ones(18), np.zeros(182)])
_line_b = np.concatenate([np.ones(25), np.zeros(575)])

nl, n2 = len(line_a), len(line_b)

_ pl, p2 = np.mean(line_a), np.mean(line_b)

_ Ata 5% significance level (alpha = 0.05), is there a significant difference in the

defect rates? Write the Python code in your answer book and provide an

_ interpretation of the results.

| CO-2; | a. |
| SO-1; |
— BL-3
|
| |

if
/CO-6; |b, |
SO-2; |

BL-4

_ A global technology firm is facing a 16% annual turnover rate. The People Operations

department has provided you with the IBM HR Analytics Attrition Dataset(IBM HR

_ sheet). You are tasked with developing a binary classification model that moves the

| company from reactive exit interviews to proactive retention strategies. Using Python

_ and the Scikit-Learn library, develop a predictive pipeline to determine the likelihood

“of employee attrition based on five key drivers: Age, MonthlyIncome,

_ TotalWorking Years, OverTime, and EnvironmentSatisfaction. Write the Python code

in your answer book and provide an interpretation of the results.

Z

FOI AOR RR +

[10]
````

## 2024-25 · Final + Re-Exam · Sem 4 · paper b6de7f60e1eb

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/STATISTICAL STRUCTURES IN DATA AND INFERENCE/Statistical Structures in Data and Inference, Sem IV, Final Exam 2024-25 & Re Exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30/04/2025
- Text: ocr (6 pages), mean OCR confidence 88.0

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
: Academic Year: 2024-2025 :
Program: B.Tech /MBATech/BTI . . Year: II/IV Semester: IV/VIII

Stream: Data Science,

Subject: Statistical Structures in Data and Inference Time: 3 hrs (10:00 am to 1:00 pm)
Date: 30/04/2025 : No. of Pages: 06

Marks: 100 .

Final Examination@4-25)/Re Examination (23 ~24)

Instructions: Candidates should read carefully the instructions printed on the cucstion paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory. .

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall___ 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql - Answer briefly: : ; [20]

a | A hospital uses three different brands of COVID- 19 test kits—X, Y, and Z. The hospital
purchases 30% of its test kits from brand X, 45% from brand Y, and 25% from brand

co? 3 Z.-Each brand has different false positive rates:Brand X gives a false positive result in (5]
BL-3. 3% of cases. Brand Y gives a false positive result in 5% of cases.Brand Z gives a false
: positive result in 2% of cases.A randomly selected test result is found to be a false
positive. What is the probability that the test was from brand Y?"
ee a O Explain ANOVA with suitable example and assumptions. : [5]
a c. | A pharmaceutical company claims that its new vitamin supplement increases
hemoglobin levels by an average of 1.8 g/dL, with a standard deviation of 0.5 g/dL. A
©0-2; health résearcher suspects that the actual increase might be different from this claim.To (5]

BL3 test this, they randomly sample 50 individuals who took the supplement and find that

their average hemoglobin increase is 1.6 g/dL. At a 5% significance level, conduct a

one-sample Z-test to determine whether the company's claim is statistically valid.
--- page 2 ---
d. | A company wants to predict employee productivity (measured in tasks completed per
week) based on the number of hours worked per week using a linear regression model.
After analyzing the data collected over six months, they observe that :
; i, The scatter plot of hours worked vs. productivity shows a curve instead of a
eo a straight-line trend. ; [5]
BE ii. The residual plot indicates increasing variance as hours worked increases
iii. The residuals are not normally distributed when plotted on a histogram.
Based on these observations, identify which regression assumptions are violated and-

explain the possible consequences of these violations.

Q2 [20]

a. | Using Linear Regression, predict an employee's salary based on their experience,
education level, and job position from the dataset given below: Split the dataset into
training and testing sets, fit the model, and evaluate its performance. Write the Python
code in your answer book and interpret the results.
import pandas as pd
import numpy asnp
# Set random seed for reproducibility
np.random.seed(123)

n_ samples = 200
# Generate synthetic employee salary dataset

CO-3; : ;
$0-2; experience_years = np.random.randint(1, 20, n samples) # Years of experience [10]

BL education_level = np.random.randint(1, 4, n samples) #1: Bachelor's, 2: Master's, 3:
PhD ©
job_position = np.random.randint(1, 6, n‘sampies) # Job level (1-5)
# Salary (Target) with some noise
salary = (experience_years * 1000) + (education_level * 8000) + (job_position *
3000) + np.random.randn(n_samples) * 10000
# Convert to DataFrame :
df= pd.DataFrame({
‘Experience (Years)': experience_years,

‘Education Level’: education_level,
--- page 3 ---
‘Job Position’: job_ position,

‘Salary’: salary

)

.co-1; | b. | Derive the mathematical expressions for estimating the parameters for a Binomial [10]
Nabe distribution using Maximum Likelihood Estimation (MLE). :
@ —_ : (20)

: a, | import numpy as np
import pandas as pd
import matplotlib.pyplot as pit
# Set random seed for reproducibility.
np.random.seed(42)
# Generate synthetic customer data
n_samples = 500
age = np.random.normal(loc=35, scale=10, size=n_samples)
income = np.random.normal(loc=60000, scale=15000, size=n_samples)
web. activity = np.random.uniform(0, 10, size=n_samples)
| #.Generate purchase decision (target variable) based on realistic factors

ae probability = 1 / (1 + np.exp(--3 + 0.05 * age + 0.00003 * income.+ 0.3 *

BL-4 [10]

web_activity)))
‘| purchase = (np.random.rand(n_samples) < probability).astype(int)
# Create a DataFrame
| df= pd.DataFrame({
‘Age’: age, —
‘Income’: income,
"Web. Activity’: web_activity,
‘Purchased’: purchase
3)
A company wants to predict whether a customer will purchase a product based on their
age, income, and online activity score. Given a dataset with these features, predict the

customer will purchase the product both for training and testing data set based on their
--- page 4 ---
age, fare, and class. Write the Python code in your answer book and provide an

interpretation of the results.

b. | How can we estimate the parameters mean and standard deviation of a normal [10]
distribution using Maximum Likelihood Estimation (MLE) in the below data set by
‘| implementing through python code.

co; ae nai ie ”p
SO-1; import scipy.optimize as opt
ie import scipy.stats as stats

# Generate example data from a normal distribution

np.random.seed(42)_. . ;

data = np.random.normal(loc=10, scale=3, size=100)

a | ae z (20)

a. | A researcher is analyzing the effectiveness of two different training programs on | [10]
employee performance. Two independent groups of employees were trained -using |-
different methods, and their post-training scores were recorded. The first group of 50 |.

employees had an average performance score of 75 with a standard deviation of 8, while

CO-2; the second group of 65 employees had an-average score of 70 with a standard deviation
SO-6; :
BL-3 | of 10.

(a) Compute the estimated standard error of the difference between the two means.
(b) At a significance level of a = 0.05, test whether there is a significant difference in
the mean performance scores between the two groups. Write a Python code and interpret

the results.

b. | A university wants to evaluate the effectiveness of an online learning platform by | [10]
comparing student performance before and after using the platform. A random sample

of 12 students took a test before using the platform and then took a similar test after

CO-2; one month of studying with the online resources. The scores (out of 100) are recorded
SO-6; | follows:
BL3 as follows:

Before: 55, 62, 70, 58, 65, 74, 80, 69, 72, 60, 77, 85
After: 65, 70, 75, 63, 72, 79, 85, 74, 78, 68, 82, 90
--- page 5 ---
Perform a paired t-test to determine whether the online learning platform has

significantly improved. student performance.

e Write a Python program to conduct the test.
« Interpret the results and conclude whether the learning platform had a

significant impact.

Define Lasso regression with their uses and application. Using Lasso regression, predict:
the body mass’ of penguins based on their bill_length_mm, . biil_depth_mm,

flipper | length_mm, island, sex and species. Split the dataset into training and testing

Q5 sets, train the model, and evaluate its performance. Write the Python code in your

CO-3; answer book and interpret the results. [20]
SO-2; : é

BL-4 import pandas as pd

import seaborn as sns
# Load dataset and drop missing values

df= sns.load_dataset("penguins").dropna()

Q6 [20]

a. | A large hospital hires most of its nurses from the two major universities in the area:
Over the last year, they have been giving a test.to the newly graduated nurses entering
the hospital to determine which school, if either, seems to educate its nurses better.
Based on the following scores (out of 100 possible points), help the personnel office of
the determine whether the schools differ in quality. Use the Mann_whitney U test with

a 10% level of significance.

CO2-; : Test Score
SO-1; [10]
BL-3 School A. | 97 69 73 84 16 92 90
SchoolB | 88 99 65 69 97 84 85
Test Score
School A | 88 84 87: 93
SchoolB | 89 - | 91 90 87 | 91 72
--- page 6 ---
b. | Bank of Lincoln is interested in reducing the amount of time people spend waiting to
see a personal banker. The bank is interested in the relationship between waiting time
(¥) in minutes and number of bankers on duty (X). Customers were randomly selected

with the data given below:

CO-3; ;
$O-2;, ~ | [10]
BL-4 :
‘ K 12, 3 5 4 2 6 1 3 4 3 3 2 4
Y | 12.8 | 11.3 | 3.2 |64 | 11.6 | 3.2 | 8.7 10.5 82/113 [94/128 | 82
Calculate mathematically the regression equation that best fit the data:
Q7 Ey ueesa F . : [20]
* | MacroSwift estimated last year that 35% of potential software buyers planned to wait
cos for an upgrade before purchasing the new operating system, Window Panes. After an
SO-1; advertising campaign, a survey of 3,000 people found 950 were still skeptical. At the | [10]
BL-3
5% significance level, can the company conclude that the proportion of skeptical people
has decreased? Write the Python code in your answer book and interpret the results.
b. | Using the "tips" dataset from Seaborn, analyze whether the total bill and tip amounts
, are significantly affected by the group size and the day of the week.Using Multivariate |:
Analysis of Variance (MANOVA), test whether there is a statistically significant
difference in the total bill and tip amount based on these factors.
CO-3; _ :
SO-2; import pandas as pd . : [10]
BL-4 }

import seaborn as sns
import numpy as np

# Load the tips dataset

df= sns.load_dataset("tips").dropna()
````

## 2024-25 · Final + Re-Exam · Sem 8 · paper 2d0f25c0ea1c

- Departments: Data Science
- Programmes: B.TECH INTEGRATED / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/4th YEAR/DATA SCIENCE/Sem_08/Statistical Structures in Data and Inference/Statistical Structures in Data and Inference Batch 2024-25 Final Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30/04/2025
- Text: ocr (6 pages), mean OCR confidence 91.2

````text
SVKM’S NMIMS i
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENG
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program: B.Tech /MBATech/BTI Year: II/IV Semester: [V/VIII
Stream: Data Science

Subject: Statistical Structures in Data and Inference Time: 3 hrs (10:00 am to 1:00 pm)
Date: 30/04/2025 No. of Pages: 06

Marks: 100

Final Examination@4-25)/Re Examination (23-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

(1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4__ questions.
3) In all___5__ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

rey

Ql Answer briefly: [20]
a. | A hospital uses three different brands of COVID-19 test kits—X, Y, and Z. The hospital
purchases 30% of its test kits from brand X, 45% from brand Y, and 25% from brand

CO; Z. Each brand has different false positive rates:Brand X gives a false positive result in (51
BL3. 3% of cases. Brand Y gives a false positive result in 5% of cases.Brand Z gives a false
positive result in 2% of cases.A randomly selected test result is found to be a false

C positive. What is the probability that the test was from brand Y?"

So : ms Explain ANOVA with suitable example and assumptions. [5]
ms c. | A pharmaceutical company claims that its new vitamin supplement increases
hemoglobin levels by an average of 1.8 g/dL, with a standard deviation of 0.5 g/dL. A

at health researcher suspects that the actual increase might be different from this claim.To 5]
BL-3. test this, they randomly sample 50 individuals who took the supplement and find that

their average hemoglobin increase is 1.6 g/dL. At a 5% significance level, conduct a

one-sample Z-test to determine whether the company's claim is statistically valid.
--- page 2 ---
A company wants to predict employee productivity (measured in tasks completed per
week) based on the number of hours worked per week using a linear regression model.

After analyzing the data collected over six months, they observe that :

i. The scatter plot of hours worked vs. productivity shows a curve instead of a

a straight-line trend. [5]
= ii. The residual plot indicates increasing variance as hours worked increases
iii. | The residuals are not normally distributed when plotted on a histogram.
Based on these observations, identify which regression assumptions are violated and
explain the possible consequences of these violations.

Q2 [20]
Using Linear Regression, predict an employee's salary based on their experience, e
education level, and job position from the dataset given below. Split the dataset into
training and testing sets, fit the model, and evaluate its performance. Write the Python
code in your answer book and interpret the results.
import pandas as pd
import numpy as np
# Set random seed for reproducibility
np.random.seed(123)
n_samples = 200
# Generate synthetic employee salary dataset

ca experience_years = np.random.randint(1, 20, n_samples) # Years of experience [10]
et education_level = np.random.randint(1, 4, n_samples) # 1: Bachelor's, 2: Master's, 3: »
PhD
job_position = np.random.randint(1, 6, n_sampies) # job level (1-5)
# Salary (Target) with some noise
salary = (experience_years * 1000) + (education_level * 8000) + (job_position *
3000) + np.random.randn(n_samples) * 10000
# Convert to DataFrame
df = pd.DataFrame({
‘Experience (Years)': experience_years,
‘Education Level’: education_level,
2
--- page 3 ---
‘Job Position’: job_ position, ,'

‘Salary’: salary

3)
co-1; | b..| Derive the mathematical expressions for estimating the parameters for a Binomial [10]
ea "| distribution using Maximum Likelihood Estimation (MLE).
Q3 ; - [20]
a. | import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Set random seed for reproducibility
np.random.seed(42)
# Generate synthetic customer data _—
n_samples = 500
age = np.random.normal(loc=35, scale=10, size=n_samples)
income = np.random.normal(loc=60000, scale=15000, size=n_samples)
web_activity = np.random.uniform(0, 10, size=n_samples)
#.Generate purchase decision (target variable) based on realistic factors .
at probability = 1 / (1 + np.exp(-(-3 + 0.05 * age + 0.00003 * income + 0.3 *

[10]
Bis web_activity))) .

purchase = (np.random.rand(n_samples) < probability).astype(int)
# Create a DataFrame
df = pd.DataFrame({
'Age': age,
‘Income’: income,
'Web_Activity': web_activity,
‘Purchased’: purchase
})
A company wants to predict whether a customer will purchase a product based on their
age, income, and online activity score. Given a dataset with these features, predict the

customer will purchase the product both for training and testing data set based on their
--- page 4 ---
age, fare, and class. Write the Python code in your answer book and provide an

interpretation of the results.

b. | How can we estimate the parameters mean and standard deviation of a normal [10]
distribution using Maximum Likelihood Estimation (MLE) in the below data set by
implementing through python code.

c0.2: import numpy as np

SO-1; import scipy.optimize as opt

= import scipy.stats as stats
# Generate example data from a normal distribution
np.random.seed(42)

data = np.random.normal(loc=10, scale=3, size=100)

Q4 [20]

ry

a. | A researcher is analyzing the effectiveness of two different training programs on | [10]
employee performance. Two independent groups of employees were trained using |-
different methods, and their post-training scores were recorded. The first group of 50 |.

employees had an average performance score of 75 with a standard deviation of 8, while

CO-2; the second group of 65 employees had an-average score of 70 with a standard deviation
SO-6;
BL-3 of 10.

(a) Compute the estimated standard error of the difference between the two means.
(b) At a significance level of a = 0.05, test whether there is a significant difference in
the mean performance scores between the two groups. Write a Python code and interpret

the results.

b. | A university wants to evaluate the effectiveness of an online learning platform by [10]
comparing student performance before and after using the platform. A random sample

of 12 students took a test before using the platform and then took a similar test after

CO-2; one month of studying with the online resources. The scores (out of 100) are recorded
SO-6;
BL-3 as follows:

Before: 55, 62, 70, 58, 65, 74, 80, 69, 72, 60, 77, 85
After: 65, 70, 75, 63, 72, 79, 85, 74, 78, 68, 82, 90
--- page 5 ---
Perform a paired t-test to determine whether the online learning platform has,

significantly improved student performance.

e Write a Python program to conduct the test.
e Interpret the results and conclude whether the learning platform had a

significant impact.

Define Lasso regression with their uses and application. Using Lasso regression, predict
the body mass of penguins based on their bill_length_mm, | biil_depth_mm,

flipper_length_mm, island, sex and species. Split the dataset into training and testing

Q5 sets, train the model, and evaluate its performance. Write the Python code in your

CO-3; answer book and interpret the results. vr [20]
SO-2;

BL-4 import pandas as pd

import seaborn as sns
# Load dataset and drop missing values

df= sns.load_dataset("penguins").dropna()

Q6 : [20]

a. | A large hospital hires most of its nurses from the two major universities in the area.
Over the last year, they have been giving a test to the newly graduated nurses entering
the hospital to determine which school, if either, seems to educate its nurses better.
Based on the following scores (out of 100 possible points), help the personnel office of
the determine whether the schools differ in quality. Use the Mann_whitney U test with

a 10% level of significance.

CO2-; Test Score
SO-1; [10]
BL-3 School A | 97 69 73 84 716 92 90
School B | 88 99 65 69 97 84 85
Test Score
School A | 88 84 87 93
School B_ | 89 91 90 87 91 72
--- page 6 ---
2
b. | Bank of Lincoln is interested in reducing the amount of time people spend waiting to
see a personal banker. The bank is interested in the relationship between waiting time
(Y) in minutes and number of bankers on duty (X). Customers were randomly selected
Gos: with the data given below:
SO-2; [10]
BL-4
xX 12 3 b} 4 2 6 1 3 4 3 3 2 4
Y | 12.8 | 11.3} 3.2 |64 | 11.6 [3.2187 ]10.5 [8.2 111.3 19.4] 12.8 |82
Calculate mathematically the regression equation that best fit the data.
Q7 (20) >
* MacroSwift estimated last year that 35% of potential software buyers planned to wait
co, for an upgrade before purchasing the new operating system, Window Panes. After an
SO-1; advertising campaign, a survey of 3,000 people found 950 were still skeptical. At the | [10]
= 5% significance level, can the company conclude that the proportion of skeptical people
has decreased? Write the Python code in your answer book and interpret the results.
b. | Using the "tips" dataset from Seaborn, analyze whether the total bill and tip amounts
are significantly affected by the group size and the day of the week.Using Multivariate
Analysis of Variance (MANOVA), test whether there is a statistically significant
difference in the total bill and tip amount based on these factors.
CO-3; ~
SO-2; import pandas as pd [10]
BL-4

import seaborn as sns
import numpy as np

# Load the tips dataset

df= sns.load_dataset("tips").dropna()
````

## 2023-24 · Final + Re-Exam · Sem 4 · paper aabfe715ce2a

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/STATISTICAL STRUCTURES IN DATA AND INFERENCE/Statistical Structures in Data and Inference, Sem-IV, Final & Re Exam 2022-23.pdf` (+1 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 89.7

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024 j
Program: B.Tech/MBA Tech Stream ;Data Science Year: [I Semester: IV

Subject: Statistical Structures in Data and Inference Time: __3___hrs(10 qm to 1pm _)
Date:_!8 /04/24 . No. of Pages:_ 4

Marks: 100
Final/Re Examination(2022-23)

Instructions: Candidates should read carefully the instructions printed on the quagti
and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any 4 __ questions.
3) Inall___5_ questions to be attempted.
4) All questions carry equal marks.
6 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql

Answer briefly: [20]
CO-;2 Ja. . .
PO- ;1 Explain the use of Two-way ANOVA with a suitable example. [5]
BL-1
CO-;1 |b.
PO- :1 What is Type I and Type II Error. {5]
BL-1
CO+;2. |e Explain how mathematically the standard deviation of the normal [5]
Oe distribution is calculated through maximum likelihood estimation.

eo-2 Fa
PO- :2 Explain R? in Linear Regression. {5]
BL-1
Q2 [20]
A #Python Libraries

import numpy as np

from scipy.optimize import minimize

from scipy.stats import norm
CO-3; Following are the sample observations for a random variable | [10]
PO-;1 (normally distributed) 25,22,27,26,21,32,29,19,31,34
BL-4

Write a Python program to find the most likely values for the
mean and standard deviation through maximum likelihood
estimation. Write down the python code in the answer book.
--- page 2 ---
B #Python Libraries

import numpy as np
from scipy import stats

¥

. Given a sample mean of 83, a sample standard deviation of 12.5,

CO-2; j : [10]
and a sample size of 22, write a Python program to test the

PO-2 : : . :

BL-33 hypothesis that the value of the population mean is 70 against the
alternative that it is more’than 70. Use the 0.025 significance
level. Write down the python code in the answer book.

Q3 [20]

AI | Let’s assume that 30 out of 70 people recommend KFC to their
friends.. To test this claim, a random sample of 150 people
obtained. Of these 150 people, 80 indicate that they recommend

bot KFC to their friend. Is this claim accurate? Use alpha = 0.05 to | [10]

BL3 test the hypothesis. Use python code to do testing of hypothesis.
Write down the python code in the answer book.

B #Python Libraries
import pandas as pd
df=pd.read_csv/(‘iris.csv')

CO-1; [10]

PO-;11

BL-3 In the above dataset(iris.csv) investigate whether iris species have
different average Sepal lengths or not using ANOVA. Write down
the python code in the answer book

Q4 [20]

A A ‘training program was conducted to improve participant’s
knowledge of the python language. Data of Test Results were
collected from a selected sample both before and after the python
training program.

roe before=[39,43,41,32,37,40,42,40,37,38] [10]

BL-4 after=[42,45,42,43,40,44,40,43,41,40]

Test the hypothesis that the training is effective to improve
participants’ knowledge of python language at a 5% level of

significance. Do a testing of hypothesis in python and cross check
--- page 3 ---
with pre-define library. Write down the python code in the answer
book. ;

¥

(hint: pair t test)

B The data set (profit.csv) consist of profit and different
expenditure and Sate of 10 random companies in USA. Do a
multiple regression in pythori and. interpret the result. Write down
the.python code in the answer book. [10]
#Python Libraries

import statsmodels.formula.api as smf

5 | | [20]

A A. Given the time between the arrival of two customers at a

cafeteria is exponentially distributed with rate 4 (Ae*'*), we have

road observed the time between the arrivals as X=(4.23, 5.27, 7.84, | [10]
BL-4 4.15,3.45). For which value of i is the probability of the observed

sample the largest? (hint: likelihood estimation).

B Briefly explain multiple regression. Write a program (Python) to
calculate regression coefficients to predict Rating based on f10)
Income, Limit, Cards and Balance (Data set: Credit.esv). Write

down the python code in the answer book.

Q6 [20]
A
How ridge regression is used to shrink estimates of the é
CO-;3 Be mss [10]
PO-;12 coefficients.
BL-4
B import pandas as ‘pd
df=pd.DataFrame({'Years_of Experience':[1,2,3,4,5,6,7,8,9,10],
. 'Salary':[48000,52000,65000,82000, 115000, 160000,210000,3150
CO-;1 00,512000,1100000]})
PO-;2 [10]
BL-1
Build a best polynomial regression model on the above data set.
Produce python code and analyze the output. Write down the
python code in the answer book.
Q7 (20]
--- page 4 ---
A A large hospital hires most of its nurses from the two major
universities in the area. Over the last year, they have been giving
a test to the newly graduated nurses entering the hospital to
determine which school, if either, seems to educate its nursés.
better. Based on the following scores, help the personnel office of

CO-;3 the hospital determine whether the schools differ in quality. Use
PO-;10 the Mann-Whitney U test with a 10 percent level of significance. | [10]
BL-4 (P)

Test Scores

SchoolA 97 69 73 84 76 92 90 88 84 87 93
SchoolB 88 99 65 69 97 84 85 89 91 90 87 91 72

B import statsmodels.api as sm
from sklearn import linear_model
import pandas as pd
df3=pd.DataFrame({'x1':[2.78,2.44,2.09,2.14,2.72,2.65,4.92,4.37

>

CO-;1 4.96,4.52,4.69,3.88], 'x2':[78,74,79,4,72,65,9,7,6,52,9,8],
PO-:2 [10]

BL-1 'y':[0,0,0,0,0,0,1,1,1,1,1,1]})

Build a logistic regression model on the above data set.
Produce python code and analyze the output. Write down the

python code in the answer book .
````

## 2023-24 · Re-Exam · Sem 4 · paper 9c8eba3514dd

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/STATISTICAL STRUCTURES IN DATA AND INFERENCE/Statistical Structures in Data & Inference , Re-exam 2022-23.pdf` (+1 identical copies)
- Text: ocr (4 pages), mean OCR confidence 89.3

````text
Ps
SVKM’S NMIMS
‘MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS EN
Academic Year: 2023-2024

Program: B.Tech/MBA Tech Stream ;Data Science Year: II Semester: IV

Subject: Statistical Structures in Data and Inference Time: 3 hes (jotooanto 1+00pm)
Date:_2¢ / é /24 ; No. of Pages: 4

Marks: _ 100 ;

Re Examination(2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.
2) Out of remaining questions, attempt any __4 _ questions.
3) In all___5_ questions to be attempted.
m 4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
CO-;2 |a. .
PO-:1 Explain the use of One-way MANOVA with a suitable example. | [5]
BL-1
CO-;1 |b. Describe the use of dummy or one-hot encoding variables in [5]
ay regression models.
CO-;2 |c. Explain how mathematically the mean of the normal distribution [5]
am | is calculated through maximum likelihood estimation.
CO-;2. | d.
PO- :2 What is Type I and Type II Error. [5]
BL-1
Q2 _ | 20]
A #Python Libraries
import pandas as pd
import numpy as np
from numpy import maximum
CO-3; ; Py pm [10]
PO-;1 from scipy.optimize import minimize ‘
BL-4

from scipy.stats import norm y
df=pd.DataFrame(np.random.normal(10,5,size=(100,2)),column
s=list((AB’))
--- page 2 ---
The — data set(df) has two variables A and B, both the
variables are Normally distributed with mean=10 and standard.
deviation=5. Do maximum likelihood estimation in Python to
calculate mean and standard deviation of Variables A and B.

Write down the python code-in the answer book.

B Explain how mathematically the parameters of the Binomial
CO-2; distribution is calculated through maximum likelihood | [10]
PO-2 er
BL-33 estimation.
Q3 [20]
A. Suppose we have randomly selected a stock for 100 days with up
and down
where: UP = 1: if a randomly selected stock is up for that day
and Down = 0: if a randomly selected stock is down for that day
=e | a
BL-3 Assuming that the stock is independent Bernoulli random
variables with unknown parameter (up rate). Do maximum | —
likelihood estimation in Python to calculate the proportion of up
in the stock. Write down the python code in the answer book.
B Suppose you are a company producing cookies. Each cookie is
supposed to contain 10 grams of sugar. The cookies are produced
by a machine that adds the sugar in a bowl before mixing
everything. You believe the machine does not add 10 grams of
sugar for each cookie. If your assumption is true, the machine
needs to be fixed. You stored the level of sugar of thirty cookies
Pont by cresting a distribution with 30 chservitiona vith. a mean of 10 [10]
BL-3 and a standard deviation of 0.05 in python.

sugar=np.random.normal(10,0.05,size=(30,))

<

Do a testing of hypothesis in python and cross check with pre-
define library, whether the level of sugar is different than the
--- page 3 ---
recipe at 0.01 level of significance. Write down the python code

in the answer book.

a (20

A How logistic regression is used for classification? Write a Python
program to build a logistic regression model on the following data
and predict the class for x1=3.46 and x2=59. Write down the
python code in the answer book.

Xi X2 y

3.78 71 0

2.44 65 0
CO-;3 2.09 47 0 [10]

a PO-;2° 0.14 84 0 P

BL-4 1.72 74 0

1.65 57 0

4.92 63 1

4.37 44 1

4.96 81 1

4.52 59 1

3.69 78 {1

5.88 58 1

B The cars.csv(motor trend car road test data) dataset is consist of

32 car brands and 11 attributes. Do one way ANOVA in python
and find out that whether there is any difference between average | [10]
displacement for different gears and am. Write down the python

code in the answer book.

Oo 0 [20]

A Two operators check the same dimension on the same sample of
10 parts. Below are the results. Is there a significant operator
measurement error?

-§.No——-Operator + -Operator27

CO-;3 3 62 60 [10]
PO-;10 4 59 58
BL-4 5 62 59

6 50 57

7 63 63 ; ‘

8 61 61

9 56 58

10 63 64
--- page 4 ---
Test at the 5% significance level. Do a testing of hypothesis in
python and cross check with pre-define library Write down th:
python code in the answer book.

(hint: Pair t test)

A large hospital hires most of its nurses from the two major
universities in the area. Over the last year, they have been giving
a test to the newly graduated nurses entering the hospital to
determine which school, if either, seems to educate its nurses
better. Based on the following scores, help the personnel office
of the hospital determine whether the schools differ in quality.

Use the Mann-Whitney U test with a 10. percent level of | [10]
significance. (P)
Test Scores
SchoiA 97 69 73 84 76 923 90 88 84 87 93
SchoolB 88 99 65 69 97 84 85 89 91 90 87 91 72
Q6 [20]
The cars.csv(motor trend car road test) dataset is used which
consist of 32 car brands and 11 attributes If there is any important
C0-3 difference, in mpg, displacement(disp) and wt, between the 110]
PO-;12 different gear, am and cyl or not. Perform MANOVA test in
Bot python to test the hypothesis. Write down the python code in the
answer book.
fas How qualitative predictors are incorporated into the regression [10]
BL- 1 model? Explain with an example.
\.Q7 [20]
Given the following set of data:
x 2 4 6 8
CO-;3 y 3 7 B 10
PO-;10 [10]
BL-4 er : : .
Develop the estimating equation (regression equation) that best
describes the data. (hint: Calculate parameters).
ton How ridge regression is used to shrink estimates of the [10]
BL-1 coefficients. .

>
````

## 2022-23 · Final + Re-Exam · Sem 4 · paper d97f7dd36933

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/STATISTICAL STRUCTURES IN DATA AND INFERENCE/Statistical Structures in Data and Inference, Sem-IV, Year 2022-23, Final Exam & Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (5 pages), mean OCR confidence 91.0

````text
SVKM’S NMIMS

~~ MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERI
Academic Year: 2022-2023
Program/s: MBA Tech/B.Tech Data Science Year: I] Semester: _ IV
Stream/s ;__ Data Science
Subject: Statistical Structures in Data and Inference Time: 3___ hrs (orooamto 1:00 pm)
Date:_ 25 / 04/2023 No. of Pages: S___
Marks: 100

Final Examination | Re ~ Examination.

Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

a 6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Qe Answer briefly: [20]
CcO-1 ; SO- | a.
fl Illustrate the assumption of ANOVA [5]
BL-2
CO-1 ; SO- | b.
e1 Indicate the difference between Ridge and lasso regression model? [5]
BL-2
CO-2 ; SO- | c.
How to estimate the likelihood function for binomial distribution for parameter
eh estimation? x
m BL-4 |
CO-1 ; SO- | d.
3 Explain Potential Problems of Regression [5]
BL-2
Q2 [20]
A Produce python code to calculate mean and standard deviation through
Maximum likelihood estimation in the below data set refer as df.
Python code:
CO-3; SO- import numpy as np
FS) from scipy.optimize import minimize =
BL-3 from scipy.stats import norm

np.random.seed(123)
N=500
--- page 2 ---
mu =5
sigma =9

df = np.random.normal(loc = mu, scale=sigma,size=(N,))

Explain how the parameters of the normal distribution is calculated through
CO-2; SO- [10]
maximum likelihood estimation

31 BL-1
Q3 : [20]
Al Before and after as objects containing the scores of python training in a
company. Find out whether the training program is effective or not.
Python code:
CO-3; SO-
/ from scipy import stats [5]
20 after = (12.2, 14.6, 13.4, 11.2, 12.7, 10.4, 15.8, 13.9, 9.5, 14.2]
= before = (13.5, 15.2, 13.6, 12.8, 13.7, 11.3, 16.5, 13.4, 8.7, 14.6] .
Produce python code and analyze the output
A.ll__| Below data hold plant heights from each sample
Python code:
G1 <- [8, 8, 9, 9, 9, 11, 12, 13, 13, 14, 15, 19]
CO-3; SO-
G2<- [11, 12, 13, 13, 14, 14, 14, 15, 16, 18, 18, 19] [5]
i Find out whether the mean height of both groups are same or not.
ors Produce python code and analyze the output
B Reena believes that 50% of first-time brides in the India are younger than their
grooms. She performs a hypothesis test to determine if the percentage is the
— same or different from 50%. Reena samples 100 first-time brides and 53 reply | [10]
on that they are younger than their grooms. Analyze whether what Reena believes
a is true or false at 1% level of significance.
Q4 [20]
A Four brands of flashlight batteries are to be compared by testing each brand in
five flashlights. Twenty flashlights are randomly selected and divided randomly
into four groups of five flashlights each. Then each group of flashlights uses a
different brand of battery. The lifetimes of the batteries, to the nearest hour,
CO-2; SO- are as follows.
52,12 Brand A Brand B Brand C Brand D (10)
BL-4 42 28 24 20
30 36 36 32
39 31 28 38
28 32 28 28
29 27 33 25
--- page 3 ---
Preliminary data analyses indicate that the independent samples come from
normal populations with equal standard deviations. At the 5% significance level,
does there appear to be a difference in mean lifetime among the four brands of

batteries?

CO-3; SO-;
BL-3

Anew type of corn seed has been developed and a team of agronomists wanted
to determine whether there was a significant difference between the types of
soils that they are planted in (loam, sandy, salty, clay) based on the yield of the
crop, amount of water required and amount of herbicide needed. four fields of
each type were chosen for the analysis. Based on the data determine whether
there is a significant difference between the results for each type of soil
condition.

Python code:

from statsmodels.formula.api import ols

from statsmodels.base.model import Model

from statsmodels.stats.multicomp import pairwise_tukeyhsd

import pandas as pd

import numpy as np

import statsmodels.api as sm

from statsmodels.multivariate.manova import MANOVA
df=pd.DataFrame({'Soil':np.repeat({'loam','sandy','salty’,'clay'],4),
'Yield':[76.7,60.5,96.1,88.1,66.9,55.4,50.5,64.1,62.8,45,47.8,75.6,46.3,61.5,62.
9,49.3],
‘Water':[29.5,32.1,40.7,45.1,23.9,29.1,18,14.5,25.9,15.9,36.1,27.7,31.8,16.8,25
.8,39.4],
'Herbicide':[7.5,6.3,4.2,4.9,1.1,5,4.8,3.7,2.9,1.2,4.1,6.3,7.4,1.9,2.4,5.2]})

[10]

Qs

[20]

CO-3; SO-;
BL-3

Briefly explain multiple regression. Find out the best multiple regression model
taking mpg as a dependent variable.

Python Code:

import statsmodels.api as sm

import statsmodels.formula.api as smf

mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
mtcars

Produce python code and analyze the output.

[10]

State the assumption of linear regression

{10]

Q6

[20]

Python Code:

[10]
--- page 4 ---
CO-3; SO-; import pandas as pd
BL-3 df = pd.DataFrame({'x':(1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22],
'y':[100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]})
Build a best polynomial regression model on the above data set.

Produce python code and analyze the output.

B Python Code:

from sklearn.metrics import confusion_matrix,classification_report
import statsmodels.api as sm
from sklearn import linear_model

import pandas as pd

COS;SO% df3=pd.DataFrame({'x1':[2.78,2.44,2.09,2.14,2.72,2.65,4.92,4.37,4.96,4.52,4.69 [10]
= ,3.88], 'x2':[78,74,79,4,72,65,9,7,6,52,9,8],
'y':[0,0,0,0,0,0,1,1,1,1,1,1]})
Briefly explain logistic regression and build a logistic regression model on the
above data set.
Produce python code, analyze the output and confusion matrix
Q7 [20]
A The table below shows the hours of relief provided by two analgesic drugs in 12
patients suffering from arthritis. Is there any evidence that one drug provides
longer relief than the other? (*Use sign test)
Case Drug A Drug B
a 2 35
2 3.6 5.7
3 2.6 2.9
CO-2; SO-; 4 2.6 2.4
BL-4 5 7.3 9.9 Cal
6 3.4 3:3
7 14.9 16.7
8 6.6 6
9 23 3.8
10 2 4
i 6.8 9.1
12 8.5 20.9
B The Data “Salary” contains 2008-09 nine-month academic salary for Assistant
~ = Professors, Associate Professors and Professors in a college in the U.S. First, | [10]

build a regression model considering salary as dependent variable and others as
--- page 5 ---
=

independent variable. Secondly build a regression model considering qualitative

variable as only independent variables and interpret the results.

C

oq
````

## 2022-23 · Re-Exam · Sem 4 · paper 9fcddc58c7fb

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/STATISTICAL STRUCTURES IN DATA AND INFERENCE/Statistical Structures in Data and Inference, Sem-IV, Batch 2021-22 & 2022-23, Re Exam.pdf` (+1 identical copies)
- Text: ocr (3 pages), mean OCR confidence 90.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023

Program/s: MBA Tech/B.Tech Data Science Year: Il Semester: __ IV

Stream/s ;__ Data Science }

Subject: Statistical Structures in Data and Inference Time: _3___hrs (40: eamto 4:00 pm)
Date:_28 / 06 / 2023 No. of Pages:__ 3

Marks: __100

Re-Examination (2021- 22] 2022- 23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
a> 6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
CO-1; SO-;1 a.
What is the difference between R square and adjusted R square? {S]
BL-2
CO-1;S0-;1 |b.
How to interpret alpha and beta in the results of a logistic regression model? [5]
BL-2
CO-2 ; SO- ;1 C
What’s the Difference Between a T-Test and Z-Test? [5]
BL-4
CO-1 ; SO- ;3 d. .
How is Hypothesis Testing using in Linear Regression? [5]
BL-2
Q2 [20]
( A Python code:
. import pandas as pd
import statsmodels.formula.api as smf
CO-3; SO-2; df1= pd.DataFrame({'x':[89,43,36,36,95, 10,66,34,38,20,26,29,48,64,6,5,36,66,72,40], | {10} | .
BL-4 ‘y':[21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]})
Check whether x has a non-linear relationship with Y or not.
Produce python code and analyze the output.
B The times required by three workers to perform an assembly-line task were recorded
on five randomly selected occasions. Here are the times, to the nearest minute.
Hari Ram Jay
CO-2; SO- 8 8 10
10 9 9 [10]
32,12
9 9 10
BL-4 i 8 it
10 10 9
--- page 2 ---
Preliminary data analyses indicate that the independent samples come from normal

populations with equal standard deviations. At the 5% significance level, does there |!

appear to be a difference in mean assembly-line task?

Q3

(20]

CO-3; SO-;2,5
BL-3

All

Before and after as objects containing the scores of python training in a company. Find
out whether the training program is effective or not.

Python code: ia

from scipy import stats

after = (12.2, 14.6, 13.4, 11.2, 12.7, 10.4, 15.8, 13.9, 9.5, 14.2]

before = (13.5, 15.2, 13.6, 12.8, 13.7, 11.3, 16.5, 13.4, 8.7, 14.6]

Produce python code and analyze the output

[5]

CO-3; SO-;2,5
BL-3

Al

Below data hold plant heights from each sample

Python code:

G1 <- [8, 8, 9, 9, 9, 11, 12, 13, 13, 14, 15, 19]

G2<- (11, 12, 13, 13, 14, 14, 14, 15, 16, 18, 18, 19] .
Find out whether the mean height of both groups are same or not.

Produce python code and analyze the output

[5]

CO-1; SO-;2,5
BL-4

Reena believes that 50% of first-time brides in the India are younger than their
grooms. She performs a hypothesis test to determine if the percentage is the same or
different from 50%. Reena samples 100 first-time brides and 53 reply that they are
younger than their grooms. Analyze whether what Reena believes is true or false at

1% level of significance.

[10]

a4

[20]

CO-3; SO-3;
BL-4

The Data “salary” contains 2008-09 nine-month academic salary for Assistant
Professors, Associate Professors and Professors in a college in the U.S. First, build a
regression model considering salary as dependent variable and others as independent
variable. Secondly build a regression model considering qualitative variable as only

independent variables and interpret the results.

{10]

CO-3; SO-;3
BL-3

Produce python code to calculate mean and standard deviation through Maximum
likelihood estimation in the below data set refer as df.

Python code:

import numpy as np

from scipy.optimize import minimize

from scipy.stats import norm

np.random.seed(123)

N=S00

mu =5

sigma =9

df = np.random.normal(loc = mu, scale=sigma,size=(N,))

{10]

Qs

(20]
--- page 3 ---
CO-1; SO-;1 Write down the steps of testing of Hypothesis with an examples. (10)
BL-2
Conse B Given the time between the arrival of two devotees at a temple is exponentially, F
- ei distributed with rate A, we have observed the time between the arrivals as (1.34, 3.67, | [10]
5.21, 4.15). For which value of A is the probability of the observed sample the largest?
a6 {20}
A Bank of India, Mumbai branch manager shows that the median number of savings
account customers per day is 64. A clerk from the same branch claims that it was more
than 64. The clerk found the number of savings accounts customers per day data for
CO-1; SO-;1 10 random days. Can we reject the branch manager's claim at a 0.05 significance level? | [10]
BL-2 (*Use sign test)
Day 1 2 3 4 S 6 7 8 9 10
Customers | 60 66 65 70 68 72 46 76 TE 7S
B Briefly explain multiple regression. Write a program(Python) on advertisement
COM SO: dataset to calculate regression coefficients to predict product sales based on | [10]
_— advertising budgets on TV, radio and in newspapers.
Q7 [20]
A A baseball coach wants to know if his team is representative of other teams in-scoring
runs. Nationally, the average number of runs scored by a team in a game is 5.7. He
CO-1; SO-2;
chooses five games at random in which his team scored 5, 9, 4, 11, and 8 runs. Is it [10]
ort likely that his team's scores could have come from the national distribution? Assume
the level of significance as 0.05.
B Briefly explain logistic regression. Build a logistic regression model on the above data
set. Produce python code, analyze the output and confusion matrix.
Python code:
CO-3; SO-2; from sklearn import linear model
BL-4 from sklearn.metrics import confusion_matrix,classification_report ml

df3=pd.DataFrame({'Age':(25,32,24,27,33,35,48,50,55,45,60,65],
'Salary':[15000,74000,79000,40000,72000,65000,20000,40000,60000,52000,40000,
45000], ‘y':[0,0,0,0,0,0,1,1,1,1,1,1]})
````

## 2021-22 · Final-Exam · Sem 4 · paper 1f4044a559ea

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/STATISTICAL STRUCTURES IN DATA AND INFERENCE/B Tech, Statistical Structures in Data and Inference, 2nd Year, Sem-IV, Final Exa_3a3866e5.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 April 2022
- Text: ocr (3 pages), mean OCR confidence 87.9

````text
. SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINE!
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2021-22

Programme: B.Tech (Data Science) Year: II Semester: IV
Subject: Statistical Structures in Data and Inference

Marks: 100
Date: 09 April 2022 : Time: 10.00 am to 1.00 pm

Durations: 3 (hrs)
No. of Pages: _3

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question
paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___is compulsory.

2) Out of remaining questions, attempt any __4__questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

om Answer briefly: marks
Col: a. What is point estimation?
S02: Define the following with an example: 5
BLI , 1. Estimator

2. Estimate
CO3; b. . . 7
SO]: Define steps performed in MLE with proper statistical 5
BL2 justification.
col: (oH
Sol; Mention advantage and disadvantages of non-parametric test. 5
BLI
CO2; d.
S06; Define Adjusted R? 5
BL4

a. Define what is unbiasedness.

Q2 Let X1,X2,X3 be a random sample of size 3 drawn from the
CO3; population with mean © test whether the following estimators are

. 10
SOl; unbiased:
BLS 1. Tl =(X1+X2)/2 + X3

2. T2=(X1 + X2 + X3)/3
--- page 2 ---
3
4

. T3 = (K1 + 3X2)/9 + 5X3
. T4= (Kl —- X2 + X3)

1.

Explain in brief what is Efficiency.

Q2 2. Define Relative efficiency and mention all 3 conditions for
it.
Col; 3. Explain consistency in detail also mention the properties of | 10
$06; consistency.
BL3
Q3 1. Find MLE of parameter @ for the pdf f(x, 9) = (1- 0) 84(x-
CO3; 1)
10
$02; where x = 0,1,2. ..,00
BL2 2. Mention Properties of MLE.
1. Find MLE of parameter 0 for the pdf f(x, 0) = 0(1- 8)*x-1
Q3 where x = 0,1,2. ..,00 ;
CO3; 2. A sample of 400 male students is found to have a mean 10
SOl; height of 67.47 inches. Can it be reasonably regarded as a
BL3 sample from a large population with mean height 67.39
inches and standard deviation 1.30 inches. Test for 5%
level of significance.
Q4 1. Explain all the assumptions of linear regression and
Col; mention model of linear regression with explaining all the
variables. 10
S06; 2. Mention the properties of OLS estimators.
BL6
Q4 1. Explain the Durbin Watson test:
co4: i. Define test statistic
S o7. ii. Explain the rules for autocorrelation 10
BL3. iii. | Assumptions of the Durbin Watson test
Q5
Col: 1, What is logistic distribution function?
7 2. What is its significance in logistic regression model? 10
S06; 3. Explain logit transformation of logistic regression model
BL2
Q5 1. Explain the difference between Point Estimation and
C04; Interval Estimation. 10
S07; 2. Explain Heteroscedasticity

2|3
--- page 3 ---
BL3

26 a For Wilcoxon signed rank test (for one sample) mention the:

Col; 1. Assumptions

Sol: 2. Hypothesis to be tested 10
, 3. Test statistic

BLI 4. Decision Rule

Q6. - b. For Mann whitney test mention the:
. 1, Assumptions

3 } 2 2. Hypothesis to be tested 10

BL2 3. Test statistic

4. Decision Rule

32
````

## 2021-22 · Re-Exam · Sem 4 · paper 4274d5fbfa23

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/STATISTICAL STRUCTURES IN DATA AND INFERENCE/Statistical Structures in Data and Inference, Sem-IV, Re-Exam, Year 2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 June 2022
- Text: ocr (3 pages), mean OCR confidence 87.6

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT &
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEE!

Academic Year: 2021-22

Programme: B. Tech (Data Science) Year: II Semester: IV
Subject: Statistical ‘Structures in Data and Inference
Marks: 100
Date: 07 June 2022 Time: 10.00 am to 1.00 pm

Durations: 3 (Hrs)
‘ No. of Pages: _O%
| Re-Examination (2021-22)

rt gH oer a

<

Instructions: Candidates should read carefully the instructions printed on
the question paper and on the cover of the Answer Book, which is provided
for their use.

1) 1) Question No. _1___is compulsory.

2) 2) Out of remaining questions, attempt any__4__questions.

3) 3) In all___5__ questions to be attempted.

4) 4) All questions carry equal marks.

5) 5) Answer to each new question to be started on a fresh page.

6) 6) Figures in brackets on the right hand side indicate full marks.
} 7) 7) Assume Suitable data if necessary.

Ql Answer briefly: marks
a. What is Interval estimation? —
. Define the following with an example:
Col; .
, 1. Null Hypothesis
SO2; . 5
BLI 2. Alternate Hypothesis
3. Simple Hypothesis
4. Composite Hypothesis
. coz; |b.
SO1; Define boot strapping and its use in statistics. 5
BL2
Col; c.
SOl; Mention advantage and disadvantages of non-parametric test. 5
BLI
--- page 2 ---
CO2;

S06; Explain the concept of Autocorrelation. 5
BL4
Q2 Define what is unbiasedness.
CO3; Let X1,X2,X3 be a random sample of size 3 drawn from the 10
S01; population with mean © test whether the following estimators are
BLS unbiased:
1. T1 = (X1+X2)/2 - X3
2. T2=(X1 - X2 + X3)/3
3. T3 =(K1 - 3X2)/9 + 5X3
4. T4=(X1—-X2+ X3)
1. Explain in brief what is Sufficiency, Efficiency
Q2 2. A random sample of size n is taken from uniform
: distribution over (0,0). Prove that 2X is an unbiased
Col; ; 10
S06: estimate for 0.
BL3
Q3 1. What is MLE? Generalize the steps involved in getting the
CO3; MLE of an estimate. 10
S02; 2. Mention Properties of MLE.
BL2
1. Find MLE of parameter 6 for the pdf f(x, @) = (1- 8) 0%(x-
Q3 1) 1) where x = 0,1,2....,00
CcO3; 2. A sample of 400 male students is found to have a mean 10
SOl; height of 67.47 inches. Can it be reasonably regarded as a
BL3 sample from a large population with mean height 69.39
inches and standard deviation 2.30 inches. Test for 5%
level of significance.
Q4 1. Explain all the assumptions of linear regression and
mention and mention the model of linear regression with
col; explaining all the variables. 10
S06; 2. Mention the properties of OLS estimators.
BL6
Q4 1. Explain are the 4 possibilities to make the decision to
; accept or to reject the Null hypothesis? explain with the
ag help of a table. 10
noe 2. Explain the concept of autocorrelation.
--- page 3 ---
. What is logistic distribution function?
COl1; 2. What is its significance in logistic regression model? 10
3. Explain logit transformation of logistic regression model

S06;
BL2
Q5 b. | 1. Explain Adjusted R-Square. 10
2. Explain Heteroscedasticity
. C04;
‘ S07;
' BL3
]
Q6 a. For One simple sign test mention the:
COl: 1. Assumptions
: 2. Hypothesis to be tested 10
Sol; 3. Test statistic
BLI 4. Decision Rule
Q6 b. For Mann Whitney test mention the:
Col: 1. Assumptions
S Ol: 2. Hypothesis to be tested 10
BL > 3. Test statistic
4. Decision Rule
````
