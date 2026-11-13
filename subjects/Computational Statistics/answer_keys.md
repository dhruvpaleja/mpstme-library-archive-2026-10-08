# Computational Statistics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper e1d62772a766

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSBS_7036/Computational Statistics/ANS_Computational Statistics(702BS0C074)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Computational Statistics
Date: 28 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure to the right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
a.   Proportion explained (R²): 88.65%
Significant predictors: Training Hours and Experience
Training Hours interpretation: +1.852 increase in performance per hour
CO-1; SO- 1;   Model significance: Significant (p = 0.0012)
5
BL-1
1. R² interpretation – 1 mark
2. Predictor significance (p-values) – 2 marks
3. Coefficient interpretation – 1 mark
4. F-test conclusion – 1 mark
b.
Factor   High-Loading Variables   Likely Factor
Name
Factor   Product Quality, Reliability, Design   Product
1   Attributes
Factor   Brand Image, Advertisement Appeal,   Brand
CO- 1; SO- 1;
2   Social Media Presence   Communication   5
BL-4
Factor   Customer Loyalty, Repeat Purchase Intent,   Customer
3   Price Perception   Relationship
1. Identification of Factor 1 – 1 mark
2. Identification of Factor 2 – 1 mark
3. Identification of Factor 3 – 1 mark
********** 1 **********
--- page 2 ---
4. Discussion of strategy implications – 2 marks
c.   The main objective of LDA is to find a linear combination of predictor variables
that best separates two or more classes (groups).
It projects the data onto a lower-dimensional space (discriminant axis) such that the
between-class variance is maximized and the within-class variance is minimized.
This helps in classification and dimensionality reduction.
(2 marks)
Key Assumptions of LDA
1. Multivariate Normality:
CO-2; SO-2;   The predictors (independent variables) are normally distributed within each
class.   5
BL-4
2. Equal Covariance Matrices (Homogeneity of Variance):
The covariance matrices of the predictors are the same across all classes.
3. Independence of Observations:
Observations are assumed to be independent of each other.
4. No Multicollinearity:
Predictors should not be highly correlated; redundancy reduces the model’s
discriminating power.
5. Linearity:
The relationship between each predictor and the discriminant function is
assumed to be linear.
(3 marks)
d. import math
# Given list
numbers = [4, 9, 16, 20, 25, 40, 49, 55, 64, 81]
# Initialize counter
count = 0
# Check for perfect squares
for n in numbers:
root = math.isqrt(n)   # Integer square root
CO-3; SO-1;   if root * root == n:   # Check if it's a perfect square
5
BL-5   count += 1
print("Number of perfect squares:", count)
Correct use of list and loop – 1 mark
Checking perfect square logic – 2 marks
Counting and incrementing correctly – 1 mark
Correct output display – 1 mark
********** 2 **********
--- page 3 ---
Q2
a.
CO- 1; SO-2;
10
BL-3
Mean of y₁ and y₂ – 2 marks
Variance of y₂ – 2 marks
Covariance computation – 3 marks
Independence conclusion – 1 mark
Distribution of y₂ – 2 marks
b.
CO- 2; SO-6;
10
BL-3
Mean calculation – 1 mark
Covariance matrix computation – 2 marks
Eigenvalues – 2 marks
Eigenvectors – 2 marks
Variance explained – 1 mark
Final interpretation and tabulation – 2 marks
Q3
********** 3 **********

[Text in pictures on this page, read by OCR]
Component Eigenvalue Eigenvector % Variance

PC1 8.83 [1, 1.24] 99.5%

PC? a.04 [1, -0.80] 0.596

Covariance Matrix:

3.50 4.30
u— he ss
--- page 4 ---
a.
CO-1; SO-1;
BL-3   Partitioning and setup – 2 marks   10
Inverse of Σ₂₂ – 2 marks
Conditional mean – 3 marks
Conditional variance – 2 marks
Probability computation – 1 mark
b.
CO- 2; SO-6;
10
BL-3
Pairwise distance computation – 2 marks
First merge (A,B) – 1 mark
Cluster formation (D,E,F) – 2 marks
Merge of (A,B,C) – 2 marks
Dendrogram with correct hierarchy – 3 marks
Q4
a.   R2=0.973
Adjusted R2=0.962   10
Standard error = 2.1
Residuals are small and random
Predicted values & residuals – 3 marks
CO- 1; SO-6;   R², Adjusted R², Standard Error – 3 marks
BL-2   Residual plot explanation – 2 marks
Interpretation of results – 2 marks
********** 4 **********

[Text in pictures on this page, read by OCR]
Step Merge Distance Resulting Clusters

1 AB 1414 {A,B}
2 DE 1414 {DE}
3 {DE}, F 1414 {DEF
4 {A.B}, C 2,000 {A,B,C}

3 {A,B,C}, {D,E.F} 7.616 Final Cluster
--- page 5 ---
b.
CO-1; SO-2;
10
BL-4
Mean vectors – 1 mark
Within-group scatter matrices – 3 marks
Between-group scatter matrix – 3 marks
Wilks’ Lambda computation – 2 marks
Conclusion – 1 mark
Q5
a. A textile factory inspects fabric rolls based on Thickness (mm) and Tensile Strength
(MPa).Two quality groups are:
Thickness   Strength   Quality
0.50   5.2   Accept
0.55   5.5   Accept
0.60   5.8   Accept
0.45   5.0   Accept
0.70   6.4   Reject
0.75   6.7   Reject
0.80   6.9   Reject   10
CO-2; SO-1;
BL-4
Determinants computation – 2 marks
Covariance matrix inverse – 3 marks
Mahalanobis distances – 3 marks
Discriminant function & classification – 2 marks
********** 5 **********

[Text in pictures on this page, read by OCR]
Mean (A) (9, 7)

Mean (B) (5.5, 4.5)

Ww (2.5, -1.5], [-1.5, 2.5]
H (14.7, 10.5], 110.5, 7.5]
Wilks' Lambda (/\) 0.0439

Conclusion Significant difference between Branch A & Branch B

For Accept (A):
ga = —0.51n(0.000086) — 0.5(2.422)
= —0.5(—9.36) — 1.211 = 4.68 — 1.211 = 3.47
For Reject (R):
gr = —0.5ln(0.000131) — 0.5(6.686)

= —0.5(—8.94) — 3.343 = 4.47 — 3.343 = 1.13
--- page 6 ---
b.   1. Linearity (2 marks)
The linear regression model assumes a linear relationship between the dependent
variable (Y) and each independent variable (X).
2. Independence of Errors (2 marks)
The residuals (errors) should be independent of each other.
This means that the value of one error term should not depend on another.
3. Homoscedasticity (Constant Variance) (2 marks)
The variance of the residuals should remain constant across all fitted values.
If residuals increase or decrease as fitted values change, it indicates heteroscedasticity.
CO- 1; SO-6;
This can be visually checked using a Residuals vs Fitted Values plot.   10
BL-2
4. Normality of Errors (2 marks)
The residuals should follow a normal distribution with mean 0.
This assumption is required for constructing valid confidence intervals and
significance tests.
5. No Multicollinearity (2 marks)
The independent variables should not be highly correlated with each other.
High correlation inflates the variance of regression coefficients and makes estimates
unstable.
Q6
a.
CO-1; SO- 1;
10
BL-2
Mean and slope–intercept calculation – 3 marks
Regression equation – 2 marks
Error variance (σ²) – 1 mark
Variance of first fitted value – 2 marks
Variance of first residual – 2 marks
b.
CO-2; SO- 1;
10
BL-5
1. Mean vectors – 1 mark
2. Within-class scatter matrices – 3 marks
3. Mean difference – 1 mark
4. Discriminant vector www calculation – 3 marks
********** 6 **********

[Text in pictures on this page, read by OCR]
Regression Line Y = 4,977 + 2.516X
Error Variance (07) SSE / (n-2)
Variance of first fitted value Var(¥,) = 0.0365

Variance of first residual Var(e,) = 0.0252

Mean (Fit) (2, 2)

Mean (Unfit) (7, 7)
Sw (4, 0], £0, 41]
fa — pe [-5, -5]

w= Sy" (en — pe) (-1.25, -1.25) or normalized (-0.707, -0.707)
--- page 7 ---
5. Interpretation – 2 marks
Q7
CO-2; SO- 1;   a. Cluster 1: {P1, P2, P3}   10
BL-3   Cluster 2: {P4, P5, P6}
After the second iteration, centroids do not change:
C1=(2.33,1.67),C2=(6.67,5)
1. Distance calculations & assignments (Iteration 1) – 3 marks
2. New centroid computation – 2 marks
3. Distance calculations (Iteration 2) – 3 marks
4. Final centroids & interpretation – 2 marks
********** 7 **********
--- page 8 ---
CO-3; SO- 1;   b. class Student:   10
BL-2   def __init__(self, name, roll_number, marks):
self.name = name
self.roll_number = roll_number
self.marks = marks # list of 5 subject marks
def total_marks(self):
return sum(self.marks)
def average_marks(self):
return self.total_marks() / len(self.marks)
def grade(self):
avg = self.average_marks()
if avg >= 90:
return 'A'
elif avg >= 75:
return 'B'
elif avg >= 60:
return 'C'
else:
return 'D'
def display_details(self):
print("Student Details")
print("Name:", self.name)
print("Roll Number:", self.roll_number)
print("Marks:", self.marks)
print("Total Marks:", self.total_marks())
print("Average Marks:", round(self.average_marks(), 2))
print("Grade:", self.grade())
student1 = Student("Rahul Sharma", 101, [85, 78, 92, 88, 80])
student1.display_details()
Class definition and constructor – 2 marks
Total marks method – 2 marks
Average marks method – 2 marks
Grade determination logic – 2 marks
Display and output formatting – 2 marks
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 07db7bb79dfc

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CSBS_7036/Computational Statistics/ANS_Computational Statistics(702BS0C074)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Computational Statistics
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure to the right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
a. Q1. R Square = 0.8192, i.e., 81.92% of the variation in Sales is explained by
Advertising and Price.
(1 mark)
Q2. Both predictors significantly affect Sales since their p-values are less than 0.05.
Advertising (p = 0.0003 < 0.05) and Price (p = 0.0189 < 0.05).
(2 marks)
CO-1; SO- 1;
5
BL-1   Q3. A one-unit increase in Advertising increases Sales by 2.845 units, keeping Price
constant.
(1 mark)
Q4. Sales = 45.231 + 2.845(Advertising) - 1.502(Price)
(1 mark)
b. Q1. Factor 1 (≥0.70): Concept Understanding (0.80), Problem-Solving Skills (0.75),
Critical Thinking (0.70)
Underlying factor: Cognitive Skills
(1 mark)
Factor 2 (≥0.70): Teaching Style (0.85), Feedback and Support (0.70), Instructor
CO- 1; SO- 1;   Clarity (0.88)
5
BL-4   Underlying factor: Teaching Effectiveness
(1 mark)
Factor 3 (≥0.70): Peer Interaction (0.85), Group Projects (0.80), Motivation to Learn
(0.65 – moderately high)
Underlying factor: Collaborative Learning & Motivation
(1 mark)
********** 1 **********
--- page 2 ---
Q2. Strengthening Cognitive Skills through problem-based learning and analytical
exercises.Enhancing Teaching Effectiveness via improved feedback systems and clear
instruction.Promoting Collaborative Learning & Motivation by increasing peer
activities and group-based projects.
(2 marks)
c. Objective:
To reduce the dimensionality of a dataset by transforming correlated variables into a
smaller number of uncorrelated variables called principal components that capture
most of the variance in the data.
(2 marks)
Key assumptions:
CO-2; SO-2;
5
BL-4   1. Linearity exists among variables.
2. Large variances correspond to important structure in the data.
3. The principal components are orthogonal to each other.
4. The data should be scaled and standardized before applying PCA.
(3 marks)
d. numbers = [35, 70, 14, 49, 40, 105, 140, 21, 50, 75]
count = 0
for n in numbers:
if n % 5 == 0 and n % 7 == 0:
count += 1
CO-3; SO-1;
print(count)   5
BL-5
Output: 4
(5 marks)
Q2
a.   Mean of y
E(y) = 3
(2 marks)
Variance of y
Var(y) = 5.8
(4 marks)
CO- 1; SO-2;
Distribution of y   10
BL-3
y ~ N(3, 5.8)
(1 mark)
Probability Calculation
P(y > 2) = 0.661
(3 marks)
b.   Covariance matrix: [[3.125, 2.5], [2.5, 2.571]]
CO- 2; SO-6;
Eigenvalues: 5.503, 0.193   10
BL-3
Proportion of total variance explained:
********** 2 **********
--- page 3 ---
PC₁ = 96.8%
PC₂ = 3.2%
Mean calculation for X₁ and X₂ – 1 mark
Centering the data – 1 mark
Covariance matrix calculation – 2 marks
Eigenvalue computation – 3 marks
Proportion of variance explained – 2 marks
Final interpretation and result – 1 mark
Q3
a.   Writing the conditional mean formula – 2 marks
E(Y | X = x) = μᵧ + ρ(σᵧ / σₓ)(x − μₓ)
Substitution and computation of expected IQ – 3 marks
= 105 + 0.7(12 / 15)(130 − 110) = 116.2
Writing the conditional variance formula – 2 marks
CO-1; SO-1;
Var(Y | X = x) = σᵧ²(1 − ρ²)   10
BL-3
Substitution and computation of variance – 2 marks
= 12²(1 − 0.7²) = 73.44
Final presentation of both results – 1 mark
b. Compute pairwise Euclidean distances
AB = √((2−1)² + (3−2)²) = √2 = 1.41
AC = √((3−1)² + (2−2)²) = √4 = 2.00
AD = √((6−1)² + (5−2)²) = √34 = 5.83
AE = √((7−1)² + (6−2)²) = √52 = 7.21
AF = √((8−1)² + (5−2)²) = √58 = 7.62
CO- 2; SO-6;   BC = √((3−2)² + (2−3)²) = √2 = 1.41
10
BL-3   BD = √((6−2)² + (5−3)²) = √20 = 4.47
BE = √((7−2)² + (6−3)²) = √34 = 5.83
BF = √((8−2)² + (5−3)²) = √40 = 6.32
CD = √((6−3)² + (5−2)²) = √18 = 4.24
CE = √((7−3)² + (6−2)²) = √32 = 5.66
CF = √((8−3)² + (5−2)²) = √34 = 5.83
DE = √((7−6)² + (6−5)²) = √2 = 1.41
DF = √((8−6)² + (5−5)²) = √4 = 2.00
********** 3 **********
--- page 4 ---
EF = √((8−7)² + (5−6)²) = √2 = 1.41
(2 marks)
• Minimum distance = 1.41 (pairs AB, BC, DE, EF)
→ Form clusters {A, B, C} and {D, E, F}
• Next, compute distance between clusters:
Distance({A,B,C}, {D,E,F}) = min(distance between any pair across clusters)
= min(CD, CE, CF) = 4.24
Merge both clusters at 4.24
Final cluster: {A, B, C, D, E, F}
(4 marks)
Clusters formed:
1. {A, B, C}
2. {D, E, F}
Merged at 4.24 into one cluster
(2 marks)
(2 marks)
Q4
a.   10
CO- 1; SO-6;   R² = 0.874
BL-2
********** 4 **********
--- page 5 ---
Adjusted R² = 0.779
Standard error = 0.63
Model fits the data well.
Mean calculation – 1 mark
Coefficients estimation – 3 marks
Regression equation – 1 mark
Fitted values and residuals – 2 marks
R² and adjusted R² – 2 marks
Interpretation – 1 mark
b.   Group means
Engineering mean = (87.67, 65)
Business mean = (71, 77.5)
Overall mean = (81, 70)
Within-group scatter matrix (W)
W = [[14.67, 20.0], [20.0, 62.5]]
Total scatter matrix (T)
T = [[348, -230], [-230, 250]]
Between-group scatter matrix (H)
H = [[333.33, -250], [-250, 187.5]]
CO-1; SO-2;   Wilks’ Lambda
10
BL-4   Λ = |W| / |T| = 516.67 / 34100 = 0.0152
Conclusion
Since Λ ≈ 0.015 (very small), there is a significant difference between the
Engineering and Business programs in terms of Mathematics and Communication
scores.
1. Group means computed – 1 mark
2. Within scatter W – 3 marks
3. Total scatter T – 2 marks
4. Between scatter H – 1 mark
5. Wilks’ Lambda value ≈ 0.0152 – 2 marks
6. Conclusion of significant difference – 1 mark
********** 5 **********
--- page 6 ---
Q5
a.   |C_G| = 2.39, |C_D| = 8.48
g_G(x) = −5.616
10
g_D(x) = −7.055
CO-2; SO-1;   Decision: Good
BL-4
1. Covariance determinants and inverses – 2 marks
2. Computation for g_G(x) – 3 marks
3. Computation for g_D(x) – 2 marks
4. Comparison and classification decision – 2 marks
5. Final conclusion – 1 mark
b.   1. R-Squared (Coefficient of Determination)
o Measures the proportion of variation in the dependent variable explained
by all independent variables.
o Value ranges from 0 to 1; higher values indicate better fit.
o Example: R² = 0.85 means 85% of variation in Y is explained by Xs.
(2 marks)
2. Adjusted R-Squared
o Adjusts R² for the number of predictors in the model.
o Prevents overestimation of model fit when unnecessary variables are
added.
o Formula: Adjusted R² = 1 − (1−R²)(n−1)/(n−k−1)
(2 marks)
3. Standard Error of the Estimate (SEE)
o Measures the average distance that observed values fall from the
regression line.
CO- 1; SO-6;
o A smaller SEE indicates a tighter fit of data points around the regression 10
BL-2
line.
(1 mark)
4. F-Statistic (Overall Significance Test)
o Tests whether at least one independent variable has a significant linear
relationship with the dependent variable.
o A high F value with low p-value (<0.05) indicates a statistically
significant model.
(2 marks)
5. p-Values and t-Statistics for Coefficients
o Used to test the significance of individual predictors.
o   If p < 0.05, the variable significantly contributes to explaining Y.
(1 mark)
6. Root Mean Squared Error (RMSE)
o Square root of the average of squared residuals.
********** 6 **********
--- page 7 ---
o Lower RMSE values indicate better predictive accuracy.
(1 mark)
7. Residual Analysis (Graphical Evaluation)
o Plots residuals vs. fitted values to check assumptions of linearity,
homoscedasticity, and independence.
o Helps detect outliers and model misspecification.
(1 mark)
Q6
a. Regression equation:
Y=33.88+1.57X
Residual variance: s² = 4.59
Var(b₁) = 0.0124
Var(b₀) = 4.09
Interpretation:
CO-1; SO- 1;
Each additional hour of training increases productivity by about 1.57 points.   10
BL-2
The small variances indicate stable coefficient estimates.
1. Mean calculation – 1 mark
2. Regression coefficients (b₀, b₁) – 2 marks
3. Residuals and SSE – 2 marks
4. Variance of coefficients – 3 marks
5. Regression equation and interpretation – 2 marks
b. Mean vectors:
μ₁ = (3.0, 3.75), μ₂ = (7.0, 8.0)
Within-class scatter: S_W = [[4, 1], [1, 4.75]]
Linear Discriminant vector: w = (−0.819, −0.722)
CO-2; SO- 1;
1. Mean vector computation – 1 mark   10
BL-5
2. Within-class scatter for each group – 3 marks
3. Total within-class scatter – 1 mark
4. Inverse and computation of w – 3 marks
5. Interpretation – 2 marks
Q7
CO-2; SO- 1;   a. Final clusters:   10
BL-3   C1 → {P1, P2, P3}
C2 → {P4, P7}
C3 → {P5, P6}
Final centroids: (3, 3), (5.5, 7.5), (7.5, 5.5)
1. Distance computation for Iteration 1 – 3 marks
2. Cluster formation (Iteration 1) – 2 marks
3. New centroids (Iteration 1) – 2 marks
********** 7 **********
--- page 8 ---
4. Iteration 2 and convergence – 2 marks
5. Final cluster summary – 1 mark
CO-3; SO- 1;   b. # Define the Rectangle class   10
BL-2   class Rectangle:
def __init__(self, length, width):
self.length = length
self.width = width
def area(self):
return self.length * self.width
def perimeter(self):
return 2 * (self.length + self.width)
def is_square(self):
return self.length == self.width
# Main program
def main():
# Create two rectangle objects
rect1 = Rectangle(5, 5) # Square
rect2 = Rectangle(8, 4) # Rectangle
# Display details for rect1
print("Rectangle 1:")
print("Length:", rect1.length, "Width:", rect1.width)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())
print("Is Square?", rect1.is_square())
print()
# Display details for rect2
print("Rectangle 2:")
print("Length:", rect2.length, "Width:", rect2.width)
print("Area:", rect2.area())
print("Perimeter:", rect2.perimeter())
print("Is Square?", rect2.is_square())
# Run the program
if __name__ == "__main__":
main()
********** 8 **********
````
