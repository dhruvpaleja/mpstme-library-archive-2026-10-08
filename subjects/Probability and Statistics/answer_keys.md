# Probability and Statistics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper baa909fc83bb

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Probability and Statistics/ANS_Probability and Statistics(703BS0C003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Questions 1 is compulsory.
5. Solve any four out of remaining six questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
9. Use of scientific calculator is allowed.
Q1a) A discrete random variable X has the following probability distribution:
X: -3 -2 -1 0 1 2
P(X=x): k 2k 0.2 3k 0.1 2k
Find:
(i) Value of k
(ii) P(-2 < X < 1)
Solution:
Step 1: Using condition ΣP(X=x) = 1 (1 Mark)
k + 2k + 0.2 + 3k + 0.1 + 2k = 1
8k + 0.3 = 1
8k = 0.7
k = 0.7 / 8 = 0.0875   (1 Mark)
Step 2: Find required probability P(-2 < X < 1)
Values between -2 and 1 → X = -1, 0
P(-2 < X < 1) = P(-1) + P(0)   (1 Mark)
= 0.2 + 3k
= 0.2 + 3(0.0875)
= 0.2 + 0.2625
= 0.4625   (1 Mark)
Q.1b)
The joint probability distribution of X and Y is given by:
********** 1 **********
--- page 2 ---
P(X=x, Y=y) = k(3x + 2y), where x = 0,1,2 and y = 1,2,3
Find:
(i) Value of k
(ii) Marginal probability distribution of X
Solution:
Step 1: Use condition ΣΣ P(X,Y) = 1 (1 Mark)
Sum over all x and y:
k[(3(0)+2(1)) + (3(0)+2(2)) + (3(0)+2(3))
+ (3(1)+2(1)) + (3(1)+2(2)) + (3(1)+2(3))
+ (3(2)+2(1)) + (3(2)+2(2)) + (3(2)+2(3))]
= k[2 + 4 + 6 + 5 + 7 + 9 + 8 + 10 + 12]
= k[63]
⇒ k = 1/63   (1 Mark)
Step 2: Find marginal distribution of X
P(X=x) = Σ P(X=x, Y=y)
For X=0:
P(0) = k[(0+2)+(0+4)+(0+6)] = k(12) = 12/63
For X=1:
P(1) = k[(3+2)+(3+4)+(3+6)] = k(21) = 21/63
For X=2:
P(2) = k[(6+2)+(6+4)+(6+6)] = k(30) = 30/63 (2 Mark)
Q1c). Identify the type of correlation in each of the following cases:
i) b_yx = 1/2, b_xy = 2
ii) r² - 1 = 0
iii) r = -0.5
Solution:
i) (2 Marks)
Using relation: r = ±√(b_yx × b_xy)
r = √(1/2 × 2) = √1 = 1
Since both regression coefficients are positive, r = +1
Type: Perfect positive correlation
ii) (1 Mark)
Given: r² - 1 = 0 ⇒ r² = 1 ⇒ r = ±1
Type: Perfect correlation (positive or negative)
iii) (1 Mark)
********** 2 **********
--- page 3 ---
Given r = -0.5
Since r is negative and between -1 and 0,
Type: Moderate negative correlation
Q1 d) A bag contains 5 yellow balls, 4 black balls, and 3 white balls. One ball is drawn at random from the bag.
Find the probability that the ball drawn is:
(i) black
(ii) not white
Solution:
Step 1: Find the total number of balls
Total balls = 5 + 4 + 3 = 12
Step 2: Find P(black) (2 mark)
Number of black balls = 4
P(black) = Number of favorable outcomes / Total number of outcomes
P(black) = 4/12 = 1/3
Step 3: Find P(not white) (2 marks)
Not white means the ball can be yellow or black.
Number of not white balls = 5 + 4 = 9
P(not white) = 9/12 = ¾
Q.1e )A random sample of 50 items gives a mean of 4.8 and standard deviation 6.0. Test whether the sample is
drawn from a normal population with mean 5 at 5% level of significance.
Solution:
Step 1: State Hypotheses (1 Mark)
H₀: μ = 5 (population mean)
H₁: μ ≠ 5
Step 2: Test Statistic (1 Mark)
Since sample size is large (n > 30), use Z-test:
Z = (x̄ - μ) / (σ / √n)
Z = (4.8 - 5) / (6 / √50)
Z = (-0.2) / (6 / 7.071)
Z = (-0.2) / 0.848 ≈ -0.236
Step 3: Critical Value (1 Mark)
At 5% level (two-tailed), Z₀.₀₅ = 1.96
Step 4: Decision (1 Mark)
|Z| = 0.236 < 1.96
Fail to reject H₀
Conclusion: Sample can be regarded as drawn from population with mean 5
Q.2a)
The recovery rate of patients suffering from a certain disease is believed to be 82%. In a particular hospital, out
of 500 patients treated during a year, 435 recovered. Can the hospital be considered efficient at 5% level of
significance?
********** 3 **********
--- page 4 ---
Create the decision using test of proportion.
Solution:
Step 1: State the hypotheses (1 Mark)
H₀ : p = 0.82
H₁ : p > 0.82
Here, p is the true recovery proportion. Since we want to check whether the hospital is better than the believed
standard, this is a right-tailed test.
Step 2: Compute sample proportion and test statistic (2 Marks)
Given:
n = 500, x = 435
Sample proportion:
p̂ = x/n = 435/500 = 0.87
Standard error:
SE = √[p(1-p)/n] = √[0.82 × 0.18 / 500]
= √(0.1476 / 500)
= √0.0002952 ≈ 0.01718
Test statistic:
Z = (p̂ - p) / SE = (0.87 - 0.82) / 0.01718
= 0.05 / 0.01718 ≈ 2.91
Step 3: Critical value and decision rule (1 Mark)
At 5% level of significance for a right-tailed test,
Critical value of Z = 1.645
Reject H₀ if Z > 1.645
Step 4: Conclusion (2 Mark)
Calculated Z = 2.91 > 1.645
Therefore, reject H₀.
Conclusion: There is sufficient evidence at 5% level of significance to conclude that the hospital is efficient.
Q.2b)The joint probability density function is given by:
f(x,y) = kx²y, 0 ≤ x ≤ 1, 0 ≤ y ≤ 2
Find:
(i) the value of k
(ii) P(X ≤ 1/2, Y ≤ 1)
Solution:
Step 1: Normalization condition
∫₀¹ ∫₀² kx²y dy dx = 1   (1 mark)
= ∫₀¹ kx² [y²/2]₀² dx
= ∫₀¹ kx² × 2 dx   (1 mark)
= 2k ∫₀¹ x² dx = 2k(1/3) = 2k/3
⇒ 2k/3 = 1 ⇒ k = 3/2 (1 mark)
Step 2: Required probability setup
********** 4 **********
--- page 5 ---
P = ∫₀^{1/2} ∫₀¹ (3/2)x²y dy dx   (1 mark)
Step 3: Integration
= ∫₀^{1/2} (3/2)x² [y²/2]₀¹ dx   (1 mark)
= ∫₀^{1/2} (3/4)x² dx
= (3/4)(x³/3)₀^{1/2} = (1/4)(1/8)=1/32   (1 mark)
Q.2c) A continuous random variable X has probability density function
f(x) = { kx², 0 < x < 1
{ 0,   otherwise
Find:
(i) k
(ii) Mean of X
(iii) Variance of X
Solution:
Step 1: Use property ∫f(x)dx = 1 (1 Marks)
∫₀¹ kx² dx = 1
k[x³/3]₀¹ = 1
k(1/3) = 1
k = 3   (1 Marks)
Step 2: Find mean E(X)
E(X) = ∫ x f(x) dx   (1 Marks)
= ∫₀¹ x(kx²) dx
= k∫₀¹ x³ dx   (1 Marks)
= 3[x⁴/4]₀¹
= ¾   (1 Marks)
Step 3: Find E(X²)
E(X²) = ∫ x² f(x) dx
= ∫₀¹ x²(kx²) dx
= k∫₀¹ x⁴ dx
= 3[x⁵/5]₀¹
= 3/5   (1 Marks)
Step 4: Variance = E(X²) - [E(X)]²   (1 Marks)
Variance = 3/5 - (3/4)²
= 3/5 - 9/16
= 48/80 - 45/80
= 3/80   (1 Marks)
********** 5 **********
--- page 6 ---
Q3a)A die is thrown twice.
Let:
A: The number obtained on the first throw is even
B: The sum of the two numbers is greater than 8
Find:
(i) P(A)
(ii) P(B)
(iii) P(A ∩ B)
(iv) P(B|A)
(v) Check whether A and B are independent.
Solution:
Step 1: Total sample points (1 Mark)
Since a die is thrown twice, total outcomes = 6 × 6 = 36.
Step 2: Find P(A) (1 Mark)
Event A: first throw is even = {2, 4, 6}
Number of favorable outcomes for A = 3 × 6 = 18
Therefore,
P(A) = 18/36 = 1/2
Step 3: Find P(B) (1 Mark)
Event B: sum > 8, i.e. sums 9, 10, 11, 12
Favorable outcomes are:
(3,6), (4,5), (5,4), (6,3),
(4,6), (5,5), (6,4),
(5,6), (6,5),
(6,6)
Total favorable outcomes = 10
Therefore,
P(B) = 10/36 = 5/18
Step 4: Find P(A ∩ B) (1.5 Marks)
A ∩ B means first throw is even and sum > 8.
Possible outcomes are:
(4,5), (6,3), (4,6), (6,4), (6,5), (6,6)
Total favorable outcomes = 6
Therefore,
P(A ∩ B) = 6/36 = 1/6
Step 5: Find conditional probability and test independence (1.5 Marks)
P(B|A) = P(A ∩ B) / P(A) = (1/6) / (1/2) = 1/3
Now,
P(A)P(B) = (1/2) × (5/18) = 5/36
But,
P(A ∩ B) = 1/6 = 6/36
Since P(A ∩ B) ≠ P(A)P(B), the events A and B are not independent.
Final Answer:
********** 6 **********
--- page 7 ---
P(A) = 1/2, P(B) = 5/18, P(A ∩ B) = 1/6, P(B|A) = 1/3.
Hence, A and B are NOT independent.
Q.3b) The means of two simple samples of 1000 and 2000 items are 170 cm and 169 cm respectively. Can the
samples be regarded as drawn from the same population with standard deviation 10 cm at 5% level of
significance?
Solution:
Step 1: State the hypotheses (1 Mark)
H₀ : μ₁ = μ₂ (Both samples are drawn from the same population)
H₁ : μ₁ ≠ μ₂ (The samples are not drawn from the same population)
Since we are testing whether the two population means are equal, this is a two-tailed test.
Step 2: Write the given data (1 Mark)
For Sample 1: n₁ = 1000, x̄₁ = 170
For Sample 2: n₂ = 2000, x̄₂ = 169
Population standard deviation, σ = 10
Step 3: Use the Z-test statistic for difference of means (2 Marks)
Since the sample sizes are large and population standard deviation is known, we use:
Z = (x̄₁ - x̄₂) / [σ √(1/n₁ + 1/n₂)]
Substituting the values,
Z = (170 - 169) / [10 √(1/1000 + 1/2000)]
= 1 / [10 √(0.001 + 0.0005)]
= 1 / [10 √0.0015]
= 1 / [10 × 0.03873]
= 1 / 0.3873
≈ 2.58
Step 4: Critical value at 5% level of significance (1 Mark)
For a two-tailed test at 5% level of significance,
Critical value of Z = 1.96
Step 5: Decision and conclusion (1 Mark)
Calculated |Z| = 2.58
Since 2.58 > 1.96, we reject H₀.
Conclusion: The difference between the sample means is statistically significant. Hence, the two samples cannot
be regarded as drawn from the same population at 5% level of significance.
Q.3c)
A discrete random variable X has the following probability mass function:
X   0   1   2
P(X=x) 1/3 1/3 1/3
Find:
(i) Moment generating function M_X(t)
(ii) Mean
(iii) Variance
********** 7 **********
--- page 8 ---
Solution:
Step 1: Find the moment generating function
By definition,
M_X(t) = E(e^{tX})   (1 mark)
= Σ e^{tx} P(X=x)
So,
M_X(t) = (1/3)e^{0t} + (1/3)e^{t} + (1/3)e^{2t}   (1 mark)
= (1/3) + (1/3)e^{t} + (1/3)e^{2t}   (1 mark)
Step 2: Find mean using first derivative
Differentiate M_X(t):
M'_X(t) = (1/3)e^{t} + (2/3)e^{2t}   (1 mark)
Mean = E(X) = M'_X(0)
= (1/3) + (2/3)
= 1   (1 mark)
Step 3: Find variance using second derivative
Differentiate again:
M''_X(t) = (1/3)e^{t} + (4/3)e^{2t}   (1 mark)
E(X²) = M''_X(0)
= (1/3) + (4/3)
= 5/3   (1 mark)
Variance = E(X²) - [E(X)]²
= 5/3 - (1)²
= 5/3 - 1
= 2/3   (1 mark)
Q.4a)
A machine produces items with a probability of defect equal to 0.1. If 8 items are selected at random, find:
(i) Probability that exactly 2 items are defective
(ii) Probability that at most 2 items are defective
Use Binomial distribution.
Solution:
Step 1: Identify distribution and parameters (1 Mark)
Since each item has two outcomes (defective or not) with constant probability,
X ~ Binomial(n = 8, p = 0.1)
q = 1 - p = 0.9
Step 2: Formula of Binomial distribution (1 Mark)
P(X = x) = C(n,x) p^x q^(n-x)
Step 3: Find P(X = 2) (2 Marks)
P(X = 2) = C(8,2) (0.1)^2 (0.9)^6
********** 8 **********
--- page 9 ---
= 28 × 0.01 × 0.531441
≈ 28 × 0.00531441
≈ 0.1488
Step 4: Find P(X ≤ 2) (2 Marks)
P(X ≤ 2) = P(0) + P(1) + P(2)
P(0) = (0.9)^8 = 0.4305
P(1) = C(8,1)(0.1)(0.9)^7 = 8 × 0.1 × 0.4783 ≈ 0.3826
P(2) = 0.1488
P(X ≤ 2) = 0.4305 + 0.3826 + 0.1488
≈ 0.9619
Q.4b)
A machinist is expected to make engine parts with axle diameter of 1.75 cm. A random sample of 10 parts
shows a mean diameter of 1.85 cm with a standard deviation of 0.1 cm. On the basis of this sample, would you
say that the work of the machinist is inferior?
Test at 5% level of significance.
Solution:
Step 1: State the hypotheses (1 Mark)
H₀ : μ = 1.75 cm
H₁ : μ ≠ 1.75 cm
Since n = 10 is small, we use Student’s t-test.
Step 2: Write the given data (1 Mark)
n = 10,   x̄ = 1.85 cm, s = 0.1 cm, μ₀ = 1.75 cm
Step 3: Use the rewritten t-formula with (n−1) shown in denominator part (2 Marks)
Using
t = (x̄ − μ₀) / s √(n−1)
Substituting the values,
t = (1.85 − 1.75) / 0.1√(10−1) = (0.10) / 0.1√9
= (0.10)(3) / 0.1
= 3
Step 4: Critical value (1 Mark)
Degrees of freedom = n − 1 = 9
At 5% level of significance, critical value of t = 2.262
Step 5: Decision and conclusion (1 Mark)
Calculated t = 3
Since 3 > 2.262, reject H₀.
Conclusion: The sample mean differs significantly from 1.75 cm. Hence, the work of the machinist is inferior.
********** 9 **********
--- page 10 ---
Q.4c)
The following are the marks obtained by 10 students in Mathematics and Statistics. Using the least squares
method, find the regression line of Y on X.
X: 52 55 57 54 58 56 60 59 61 53
Y: 48 50 52 49 53 51 55 54 56 47
Solution:
Step 1: Write the regression equation and normal equations (1 Mark)
For the regression line of Y on X,
Y = a + bX
Using least squares method, the normal equations are:   (1 Mark)
ΣY = na + bΣX
ΣXY = aΣX + bΣX²
X   Y   X²   XY
52   48   2704   2496
55   50   3025   2750
57   52   3249   2964
54   49   2916   2646
58   53   3364   3074
56   51   3136   2856
60   55   3600   3300
59   54   3481   3186
61   56   3721   3416
53   47   2809   2491
ΣX = 565   ΣY = 515   ΣX² = 32005   ΣXY = 29179
Step 2: Find the required sums from the table (2 Marks for table +1 mark for summations)
n = 10
ΣX = 565
ΣY = 515
ΣX² = 32005
ΣXY = 29179
Step 3: Form the normal equations (1 Marks)
ΣY = na + bΣX
515 = 10a + 565b   ...(1)
ΣXY = aΣX + bΣX²
29179 = 565a + 32005b   ...(2)
Step 4: Solve the equations to find a and b (1 Marks)
Using the formula:
a = -4.3152
b = 0.9879
********** 10 **********
--- page 11 ---
Step 5: Write the regression line (1 Mark)
Therefore, the regression line of Y on X is:
Y = -4.3152 + 0.9879X
Q.5a)
A sample of size 12 gave a variance as 4.2 while another sample of size 16 gave a variance as 2.8. Can the two
samples be regarded as drawn from populations having the same variance?
Test at 5% level of significance.
Solution:
Step 1: State the hypotheses (1 Mark)
H₀ : σ₁² = σ₂²
H₁ : σ₁² ≠ σ₂²
To test equality of variances, we use F-test.
Step 2: Write the given data (1 Mark)
First sample: n₁ = 12, s₁² = 4.2
Second sample: n₂ = 16, s₂² = 2.8
Step 3: Find the unbiased estimates of variances (2 Marks)
Using the formula:
Estimate of population variance = n s² / (n−1)
First sample variance estimate = 12 × 4.2 / (12-1)
= 50.4 / 11
= 4.5818
Second sample variance estimate = 16 × 2.8 / (16-1)
= 44.8 / 15
= 2.9867
Step 4: Compute the F-ratio (1 Marks)
Take the larger estimated variance in the numerator.
F = 4.5818 / 2.9867
= 1.5341
Degrees of freedom are:
v₁ = n₁ − 1 = 11
v₂ = n₂ − 1 = 15
Step 5: Decision and conclusion (1 Mark)
At 5% level of significance, the table value of F for (11, 15) is approximately 2.5095.
Calculated F = 1.5341
Since 1.5341 < 2.5095, we do not reject H₀.
Conclusion: The difference between the two population variances is not significant. Hence, the samples may be
regarded as drawn from populations with the same variance.
********** 11 **********
--- page 12 ---
Q.5b)
The sugar contents in two random samples of a beverage are given below:
Sample 1 18 20 21 22 24
Sample 2 19 23 25 26 27 30
Test whether the two samples have the same mean.
Solution:
Step 1: Find sample sizes and sample means (1 Mark)
For Sample 1:
n₁ = 5,   x̄₁ = 105/5 = 21.0
For Sample 2:
n₂ = 6,   x̄₂ = 150/6 = 25.0
Step 2: Find s₁² and s₂² using shortcut formula (1 Marks)
Using,
s² = (Σx²/n )− (x̄)²
For Sample 1:
Σx₁² = 2225
s₁² = 2225/5 − (21.0)² = 4.00
For Sample 2:
Σx₂² = 3820
s₂² = 3820/6 − (25.0)² = 11.67
Step 3: State hypotheses and compute t-statistic
H₀ : μ₁ = μ₂
H₁ : μ₁ ≠ μ₂ (two-tailed)   (1 Marks)
Test statistic,
t = (x̄₁ − x̄₂) / √[((n₁s₁² + n₂s₂²)/(n₁+n₂−2)) (1/n₁ + 1/n₂)]   (1 Marks)
t = (21.0 − 25.0) / √[(( 5×4.00 + 6×11.67 )/(9)) (1/5 + 1/6)]
= -2.09   (1 Marks)
Step 4: Critical value and decision (1 Mark)
At α = 5%, two-tailed,
df = n₁ + n₂ − 2 = 9
Table value of t = 2.262
|t| = 2.09 < 2.262
Hence, accept H₀ at 5% level of significance.
Conclusion:
The difference between the two sample means is not significant.
Therefore, the two samples may be regarded as having the same mean.
********** 12 **********
--- page 13 ---
Q.5c)
The diameters of steel rods produced in a factory are normally distributed with mean 50 mm and standard
deviation 2 mm.
Find:
(i) The probability that a rod has diameter between 48 mm and 53 mm
(ii) The probability that a rod has diameter greater than 54 mm
(iii) The percentage of rods having diameter less than expectation.
Solution:
Step 1: Write the given data and standard normal transformation   (1 Mark)
Mean, μ = 50 mm
Standard deviation, σ = 2 mm
Let Z = (X − μ)/σ
Then Z follows standard normal distribution.
Step 2: Find P(48 < X < 53)
Convert X-values into Z-values:
For X = 48,
Z = (48 − 50)/2 = −1
For X = 53,
Z = (53 − 50)/2 = 1.5   (1 Marks)
Therefore,
P(48 < X < 53) = P(−1 < Z < 1.5)
= P(0 < Z < 1) + P(0 < Z < 1.5)
From normal tables:
P(0 < Z < 1) = 0.3413
P(0 < Z < 1.5) = 0.4332   (1 Marks)
Hence,
P(48 < X < 53) = 0.3413 + 0.4332 = 0.7745   (1 Marks)
Step 3: Find P(X > 54)
For X = 54,
Z = (54 − 50)/2 = 2
Therefore,
P(X > 54) = P(Z > 2)   (1 Marks)
= 0.5 − P(0 < Z < 2)
From normal table,
P(0 < Z < 2) = 0.4772   (1 Marks)
Hence,
P(X > 54) = 0.5 − 0.4772 = 0.0228
Step 4: Find P(X < 50)
Therefore,   (1 Marks)
P(X < 50) = P(Z < 0)
********** 13 **********
--- page 14 ---
= 0.5
Percentage of rods having diameter less than 50 mm
= 50%   (1 Marks)
Q.6a)
The probability that a machine works properly is 0.85, given that it was serviced. The probability that it works
properly without servicing is 0.30. Assume that the probability that the machine was serviced is 0.70. Apply
Bayes’ theorem to find the probability that the machine was serviced given that it works properly.
Soln:
Step 1: Define the events (1 Mark)
Let
B₁ = the machine was serviced
B₂ = the machine was not serviced
A = the machine works properly
Step 2: Write Bayes’ theorem formula (1 Mark)
P(B₁|A) = [P(B₁)P(A|B₁)] / [P(B₁)P(A|B₁) + P(B₂)P(A|B₂)]
Step 3: Write the given probabilities (1 Mark)
P(B₁) = 0.70
P(B₂) = 1 − 0.70 = 0.30
P(A|B₁) = 0.85
P(A|B₂) = 0.30
Step 4: Substitute the values in Bayes’ theorem (2 Marks)
P(B₁|A) = [(0.70)(0.85)] / [(0.70)(0.85) + (0.30)(0.30)]
= 0.595 / (0.595 + 0.09)
= 0.595 / 0.685
Step 5: Simplify and obtain the answer (1 Mark)
P(B₁|A) = 119 / 137
≈ 0.8686
Q.6b)
Evaluate Karl Pearson’s correlation coefficient from the following values using deviation method:
X 14 18 22 26 30 34 38
Y 8 11 14 17 20 23 26
Solution:
Step 1: Take assumed means and write the formula (1 Mark)
Take assumed means:
Aₓ = 26, Aᵧ = 17
Let
x = X − 26
y = Y − 17
Formula:
r = Σxy / √(Σx² · Σy²)
********** 14 **********
--- page 15 ---
X   Y   x = X−26   y = Y−17   x²   y²   xy
14   8   -12   -9   144   81   108
18   11   -8   -6   64   36   48
22   14   -4   -3   16   9   12
26   17   0   0   0   0   0
30   20   4   3   16   9   12
34   23   8   6   64   36   48
38   26   12   9   144   81   108
Σx² = 448   Σy² = 252   Σxy = 336
Step 2: Find the required sums from the table (2 Marks)
Σx = 0
Σy = 0
Σx² = 448
Σy² = 252
Σxy = 336
Step 3: Substitute in Karl Pearson’s formula (2 Marks)
r = Σxy / √(Σx² · Σy²)
= 336 / √(448 × 252)
= 336 / √112896
= 336 / 336
= 1
Step 4: Interpretation (1 Mark)
Since r = 1, there is perfect positive correlation between X and Y.
Q.6c)
A company has three training programs, and the management wants to determine whether there is a difference
in the average performance scores of employees under the three programs. The following data are the scores
of five randomly selected employees from each program. Perform a one-way ANOVA to determine whether
there is a significant difference in the mean scores of the three programs.
Program (Performance Scores)
1   2   3
42   50   40
45   52   41
44   49   39
43   51   42
46   53   38
HYPOTHESIS:
STEP 1. The hypotheses follow.
H₀: μ₁ = μ₂ = μ₃
Hₐ: At least one of the means is different from the others.   (1 mark)
STEP 2. The appropriate test statistic is the F test calculated from ANOVA.
STEP 3. The value of α is .05.
STEP 4. The degrees of freedom for this problem are 3 − 1 = 2 for the numerator
and 15 − 3 = 12 for the denominator. The critical F value is F₀.₀₅,₂,₁₂ = 3.89.   (1 mark)
********** 15 **********
--- page 16 ---
STEP 5.
Program (Performance Scores)
1   2   3
42   50   40
45   52   41
44   49   39
43   51   42
46   53   38
STEP 6.
Tᵢ: T₁ = 220 T₂ = 255 T₃ = 200   T = 675
nᵢ: n₁ = 5   n₂ = 5   n₃ = 5 N = 15
x̄ᵢ:   x̄₁ = 44.0   x̄₂ = 51.0   x̄₃ = 40.0   x̄ = 45.00   (2 mark)
SSC = 5(44.0 − 45.00)² + 5(51.0 − 45.00)² + 5(40.0 − 45.00)² = 310.00   (1 mark)
SSE = (42 − 44.0)² + (45 − 44.0)² + ... + (42 − 40.0)² + (38 − 40.0)² = 30.00   (1 mark)
df₍c₎ = 3 − 1 = 2
df₍E₎ = 15 − 3 = 12
df₍T₎ = 15 − 1 = 14
MSC = SSC / df₍c₎ = 310.00 / 2 = 155.00
MSE = SSE / df₍E₎ = 30.00 / 12 = 2.50
F = MSC / MSE = 155.00 / 2.50 = 62.00   (1 mark)
ACTION:
STEP 7. The decision is to reject the null hypothesis because the observed F value
of 62.00 is greater than the critical table F value of 3.89.
CONCLUSION:   (1 mark)
STEP 8. There is a significant difference in the mean performance scores of employees under the three training
programs.
Q.7a)
Identify whether the following two lines can be regression lines of X on Y and Y on X. If so, find the means of X
and Y: 4x + y = 9, x + 2y = 8
Solution:
Case 1:
Take 4x + y = 9 as regression of Y on X:
y = 9 − 4x, so b_yx = −4
Take x + 2y = 8 as regression of X on Y:
x = 8 − 2y, so b_xy = −2   (1 mark)
b_yx · b_xy = (−4)(−2) = 8 > 1
********** 16 **********
--- page 17 ---
Hence, in this arrangement the lines cannot be regression lines.   (1 mark)
Case 2:
Interchange the roles.
Take 4x + y = 9 as regression of X on Y:
x = (9 − y)/4, so b_xy = −1/4   (1 mark)
Take x + 2y = 8 as regression of Y on X:
y = (8 − x)/2, so b_yx = −1/2
b_yx · b_xy = (−1/2)(−1/4) = 1/8
Since 1/8 < 1, this arrangement is possible.   (1 mark)
Hence, after interchanging, the lines can represent regression lines.
Find the means of X and Y
If two lines are regression lines, they intersect at the point (x̄, ȳ).
So solve:
4x + y = 9
x + 2y = 8
solving
x̄ = 10/7 and ȳ = 23/7   (2 mark)
Q.7b) The following table gives the number of defects found in 100 electronic components. Fit a Poisson
distribution and obtain the expected frequencies.
Number of defects (x): 0 1 2 3 4
Observed frequency (f): 20 32 26 14 8
Solution:
Step 1: Write the given data and total frequency
x: 0, 1, 2, 3, 4
f: 20, 32, 26, 14, 8
Total frequency, N = 100
Step 2: Find the parameter of Poisson distribution
For Poisson distribution, parameter λ = mean = Σfx / N
Σfx = 0×20 + 1×32 + 2×26 + 3×14 + 4×8 = 158   (1 mark)
Therefore,
λ = 158/100 = 1.58   (1 mark)
Step 3: Write Poisson formula   (1 Mark)
P(X = x) = e^(−λ) λ^x / x!
x   P(X=x)   Expected frequency   Rounded
= N×P(X=x)
0   0.2060   20.60   21
1   0.3254   32.54   33
2   0.2571   25.71   26
3   0.1354   13.54   14
4   0.0535   5.35   5
Step 4: Calculate probabilities and expected frequencies (02 Marks)
Here λ = 1.58
********** 17 **********
--- page 18 ---
P(0) = e^(−1.58) = 0.2060
P(1) = e^(−1.58)(1.58) = 0.3254
P(2) = e^(−1.58)(1.58)² / 2! = 0.2571
P(3) = e^(−1.58)(1.58)³ / 3! = 0.1354
P(4) = e^(−1.58)(1.58)⁴ / 4! = 0.0535
Step 5: Final expected frequencies (1 Mark)
Expected frequency for x = 0 is 20.60 ≈ 21
Expected frequency for x = 1 is 32.54 ≈ 33
Expected frequency for x = 2 is 25.71 ≈ 26
Expected frequency for x = 3 is 13.54 ≈ 14
Expected frequency for x = 4 is 5.35 ≈ 5
Q.7c)
In a vaccination campaign in a certain town, a preventive vaccine was administered. The number of infection
cases is shown below:
Treatment   Infected   Not Infected
Vaccine   95   25
No Vaccine   70   30
Solution:
Step 1: State the hypotheses (1 Mark)
H₀: Vaccination and infection are independent.
H₁: Vaccination and infection are not independent.
We use the chi-square test of independence.
Step 2: Write the observed frequencies and totals
Observed frequencies are: (1 Mark)
a = 95, b = 25, c = 70, d = 30
Row totals: 120 and 100
Column totals: 165 and 55
Grand total N = 220
Step 3: Find the expected frequencies (2 Marks)
Expected frequency = (Row total × Column total) / Grand total
E₁₁ = (120 × 165) / 220 = 90.00
E₁₂ = (120 × 55) / 220 = 30.00
E₂₁ = (100 × 165) / 220 = 75.00
E₂₂ = (100 × 55) / 220 = 25.00
Infected   Not Infected
Vaccine   90.00   30.00
No Vaccine   75.00   25.00
Step 4: Compute chi-square statistic (2 Marks)
χ² = Σ (O − E)² / E
********** 18 **********
--- page 19 ---
χ² = (95 − 90.00)²/90.00 + (25 − 30.00)²/30.00 + (70 − 75.00)²/75.00 + (30 − 25.00)²/25.00
= 2.4444
Step 5: Degrees of freedom and table value (1 Mark)
For a 2 × 2 table,
df = (r − 1)(c − 1) = (2 − 1)(2 − 1) = 1
At 5% level of significance, table value of χ² = 3.84
Step 6: Decision (1 Mark)
Calculated χ² = 2.4444
Since 2.4444 > 3.84, reject H₀.
Vaccination and infection are associated. Hence, the vaccine is useful in checking infection.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 900a3a856c78

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSE_DS_7057/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (20 pages), mean OCR confidence 78.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA
Tech (Comp)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 29 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compuslory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
Q1 a) A class consists of 8 girls and 7 boys. If a committee of 4 students is chosen at random, compute
the probability that i) exactly 2 girls are selected, ii) atleast one girl is selected.
Solution:
Total ways = C(15,4) = 1365.   (1 mark)
(i) Favorable = C(8,2). C(7,2) = 28·21 = 588   (1 mark)
P(exactly 2 girls) = 588/1365 = 28/65.
(ii) P(at least one girl) = 1 − P(all boys)
= 1 − C(7,4)/C(15,4) = 1 − 35/1365 = 1330/1365 = 38/39.   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 b) The probability of mass function of a random variable X is zero except at the points X = 0, 1, 2. At these
points 𝑃(0) = 3𝑐3, 𝑃(1) = 4𝑐−10𝑐2, 𝑃(2) = 5𝑐−1 . Determine i) 𝑐 ii) 𝑃(𝑋< 1), 𝑃(1 < 𝑋≤2).
Solution:
We know that for probability mass function, the sum of all probabilities must be 1:
P(0) + P(1) + P(2) = 1   (1 Mark)
Substitute the given values:
3c³ + (4c – 10c²) + (5c – 1) = 1
Simplifying: 3c³ – 10c² + 9c – 2 = 0
Factoring gives: (c – 1)(3c² – 7c + 2) = 0
Thus, c = 1, 2, or 1/3. Only c = 1/3 gives non-negative probabilities.   (1 Mark)
(i) c = 1/3
(ii) P(X < 1) = 1/9,   P(1 < X ≤ 2) = 2/3   (2 Marks)
----------------------------------------------------------------------------------------------------------------------------
********** 1 **********
--- page 2 ---
Q1 c) The joint probability function of two discrete random variables 𝑋 and 𝑌 is given by 𝑓(𝑥, 𝑦) = 𝑐(2𝑥+
3𝑦), where 𝑥= 0, 1, 2 and 𝑦= 1, 2, 3 and 𝑓(𝑥, 𝑦) = 0, otherwise. Find i) the value of the constant 𝑐   ii)
Marginal probability function of 𝑋 and 𝑌.
Solution:
The probability distribution table :
y   1   2   3
x
0   3c   6c   7c   18c
1   5c   8c   11c   24c   (1 mark)
2   7c   10c   13c   30c
15   24c   33c
c
Since, 72c=1 this gives c = 1/72   (1 mark)
Marginal of X = 18/72, 24/72, 30/72   (1 mark)
Marginal of Y = 15/72, 24/72, 33/72   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 d) A discrete random variable 𝑋 takes the values 1,3,5 with probabilities 𝑃(𝑋= 1) = 0.3, 𝑃(𝑋= 3) =
0.4, 𝑃(𝑋= 5) = 0.3. Analyze the data to determine the coefficient of skewness.
Solution:
Mean
𝜇= ∑𝑥 𝑝(𝑥) = 1(0.3) + 3(0.4) + 5(0.3).
𝜇= 0.3 + 1.2 + 1.5 = 3.0.   (0.5 mark)
Variance:
𝐸[𝑋2] = 12(0.3) + 32(0.4) + 52(0.3)=11.4   (0.5 mark)
𝜎2 = 𝐸[𝑋2] −𝜇2 = 11.4 −(3.0)2 = 11.4 −9 = 2.4.   (0.5 mark)
Third central moment 𝝁𝟑= 𝑬[(𝑿−𝝁)𝟑]
𝜇3 = −2.4 + 0 + 2.4 = 0.   (0.5 maks)
Skewness
𝛾1 = 𝜇3 =   0 = 0.   (1 mark)
𝜎3   (√2.4)3
------------------------------------------------------------------------------------------------------------------- ---------
********** 2 **********
--- page 3 ---
Q1 e) A random sample of 100 individuals has a mean height of 160 cm and standard deviation of 10 cm.
Would it be reasonable to assume that the population mean height is 165? Apply the appropriate test of
significance for the mean and state your conclusion.
Solution:
----------------------------------------------------------------------------------------------------------------------------
Q1 f) If the lines of regression of sample are 𝑥 + 6𝑦 = 6 and 3𝑥 + 2𝑦 = 10, compute the correlation
coefficient between 𝑥 and 𝑦.
Solution:
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
********** 3 **********
--- page 4 ---
Q2 a) A medical test is used to detect a rare disease that affects 1% of the population. The test correctly
identifies a diseased person 98% of the time, but it also wrongly identifies a healthy person as positive 3%
of the time. If a person chosen at random tests positive, find the probability that the person actually does not
have the disease.
Solution:
Let D: diseased, P: positive.
P(D)=0.01, P(P|D)=0.98, P(P|Dᶜ)=0.03.   (2 marks)
P(Dᶜ|P) = [P(P|Dᶜ)P(Dᶜ)] / [P(P|D)P(D) + P(P|Dᶜ)P(Dᶜ)]   (2 marks)
= (0.03·0.99)/(0.98·0.01 + 0.03·0.99) = 0.0297/0.0395 = 297/395 ≈ 0.752.   (2 marks)
--------------------------------------------------------------------------------------------------------------------------
Q2 b) The two random variables X and Y have the joint probability density function (pdf) given by 𝑓(𝑥, 𝑦) =
𝐴𝑒−(2𝑥+𝑦) 𝑥, 𝑦 ≥0. Determine
(i) the value of A,
(ii) 𝑓(𝑦|𝑥).
Solution:
 
Since  f ( x , y ) dxdy = 1   ……………..   (1 mark)
−−

 Ae − (2 x + y ) dxdy = 1   ……………….   (1 mark)
0 0
Solving , we get A =2   ………………   (1 mark)
To find f(y|x) :

Marginal prob function of x is : Xf ( x ) =  Ae − (2 x + y ) dy = 2 e − 2 x , x  0   …….   (1 mark)
0
f ( x , y ) 2 e − (2 x + y )   − y
f ( y | x ) =   =   − 2 x = e   , y  0   ………………..   (2 marks)
f X ( x )   2 e
----------------------------------------------------------------------------------------------------------------------------
********** 4 **********
--- page 5 ---
Q2 c) Two groups 𝐴 and 𝐵, each consisting of 100 individuals are treated identically except that group 𝐴 is
given a serum while group 𝐵 (the control group) is not. It is observed that 75 individuals in group 𝐴 and 65
people in group 𝐵 recover from the disease. Using a 1% level of significance, test whether the serum is
effective in improving the recovery rate.
Solution:
---------------------------------------------------------------------------------------------------------------------------
Q3 a) A lot of 10 batteries contains 3 defective and 7 good ones. Two batteries are chosen one after another
without replacement.
(i) Compute the probability that both the selected batteries are good.
(ii) Find the probability that the second battery is good given that the first one tested is good.
(iii) Determine that the second battery is good if the first one tested is defective.
Solution:
(a) (7/10)·(6/9) = 42/90 = 7/15.   (2 marks)
(b) 6/9 = 2/3.   (2 marks)
(c) 7/9.   (2 marks)
--------------------------------------------------------------------------------------------------------------------------
********** 5 **********
--- page 6 ---
Q3 b) A random variable X has the given probability density function:
 e − x   x  0
f ( x ) = 
 0   otherwise
Derive the moment generating function and hence evaluate the first four moments about origin.
Solution
(2 marks)
(1 mark)
(1 mark)
(1 mark)
(1 mark)
------------------------------------------------------------------------------------------------------------------
********** 6 **********
--- page 7 ---
Q3 c) A sample of 200 fish of a particular kind taken at random from one end of a lake has mean weight of
20 lbs. and standard deviation of 2 lbs. At the other end of the lake, a sample of 80 fish of the same kind has
mean weight of 20.5 lbs. and standard deviation of 2 lbs. Apply an appropriate statistical test to examine
whether the difference between the mean weights is significant? (Use 5% level of significance)
Solution:
-------------------------------------------------------------------------------------------------------------------
********** 7 **********
--- page 8 ---
Q4 a) A small workshop records the number of machine breakdowns per day over 5 days as follows:
Number of breakdowns (x) 0 1 2 3 4
Frequency (f)   1 1 2 1 1
1. Fit a Poisson distribution to the data and
2. Calculate the expected frequencies
Solution:
(1 mark)
---------------------------------------------------------------------------------------------------------------------
********** 8 **********
--- page 9 ---
Q 4b) The following are the marks in Statistics (𝑋) and Mathematics (𝑌) of ten students
X   56   55   58   57   56   60   54   59   57   58
Y   68   67   67   65   68   70   66   68   66   70
Compute the coefficient of correlation and estimate marks in Mathematics of a student who scored 62 marks in
Statistics.
Solution:
********** 9 **********
--- page 10 ---
-----------------------------------------------------------------------------------------------------------------------------------------
Q 4c) A group of boys and girls were given an intelligence test. The results are as follows:
Boys   Girls
Mean   124   121
Standard deviation   12   10
number   18   14
Apply an appropriate statistical test to analyze whether the mean score of boys is significantly different from
that of girls at 5% of level of significance.
Solution:
********** 10 **********
--- page 11 ---
This formula can also be used to calculate
--------------------------------------------------------------------------------------------------------------------
Q5 a) i) A factory produces screws, and the probability of a screw being defective is 0.03. The screws are
packed in packets of 30. Out of a consignment of 800 packets, using Binomial distribution, compute the
number of packets that contain:
a) at least 2 defective screws
b) at most 2 defective screws.
Solution
-----------------------------------------------------------------------------------------------------------------------------------------
********** 11 **********
--- page 12 ---
Q5 a) ii) The lifetime of a certain type of battery is normally distributed with a mean of 400 hours and a
standard deviation of 45 hours. Compute the percentage of batteries that have a lifetime of at least 470 hours.
Solution:
-------------------------------------------------------------------------------------------------------------------
********** 12 **********
--- page 13 ---
Q 5b) The following table shows the result of opinion poll for three political parties 𝐴, 𝐵 and 𝐶. Analyze
the data using Chi-square test to determine whether the age of the respondent and their choice of party are
independent at 5% level of significance.
Party
Age   Total
A   B   C
20-35   25   20   25   70
35-50   20   25   35   80
Above 50   25   25   30   80
Total   70   70   90   230
Solution:
********** 13 **********
--- page 14 ---
Step 3: Compute ? statistic.

ieee He) pd
ea Sp ua Bul

all cells By
The contribution from each cell (rounded to three decimals) is:

Observed, Expected and contribution to x?

Age Party O E (O-E)/E

A 25 21.30 0.643
20-35 B 20 21.30 0.079

Cc 25 27.39 0.208

A 20 24.35 0.777 am
35-50 B 25 24.35 0.017 —

C 35 31.30 0.435

A 25 24.35 0.018
Above50 B 25 24.35 0.018
C 30 31.30 0.054

Summing the contributions gives

Xéat © 0.641 + 0.079 + 0.208 + 0.777 +0.017 +0.435 +0.018 + 0.018 + 0.054 = 2.246 = 2.25.—\ mw

Step 4: Degrees of freedom and critical value.
Number of rows r = 3, number of columns c = 3, so degrees of freedom

df = (r—1)(e—1) = (8-1)(3-1) =4.
At a = 0.05 and df = 4, the critical value from the x? table is

x2.05,4 = 9-488. — iM

Step 5: Decision.
Since x2, = 2.25 < 9.488 = x2,,, we accept Ho (fail to reject Ho). >» Im

Conclusion: At the 5% level of significance, age and party choice are independent.

FRR IC 7 I OH
--- page 15 ---
Q6 a) Calculate the Karl Pearson’s correlation coefficient from the following data
X   2   4   6   8   10   12   14
Y   50   45   40   35   30   25   20
Solution:
(3 marks)
(1 mark)
(1 mark)
(1 mark)
------------------------------------------------------------------------------------------------------------------
********** 15 **********
--- page 16 ---
Q6 b) A continuous random variable   has the probability density function
Compute   mean and variance.
Solution:
------------------------------------------------------------------------------------------------------------
********** 16 **********
--- page 17 ---
Q6 c) The nicotine contents in two random samples of tobacco are given below
Sample 1   21   24   25   26   27
Sample 2   22   27   28   30   31   36
Test whether the two populations have the same variance at 5% level of significance.
Solution:
-------------------------------------------------------------------------------------------------------------------------
********** 17 **********
--- page 18 ---
Q7 a i) In partially destroyed laboratory record of an analysis of correlation data, the following information
is available: the variance of 𝑋 is 9 , and the two regression equations are: 8𝑋– 10𝑌 + 66 = 0 &
40𝑋– 18𝑌 = 214. Using the given information determine
a) the means of 𝑋 and 𝑌 .
b) the correlation coefficient between 𝑋 and 𝑌.
c) standard deviation of 𝑌
Solution:
(1 marks)
(1 mark)
(1 marks)
(1 mark)
:
(1 mark)
---------------------------------------------------------------------------------------------------------------------------
********** 18 **********
--- page 19 ---
7a ii) Calculate the Spearman’s rank correlation coefficient from the following data.
X   10   12   18   18   15   40
Y   12   18   25   25   50   25
Solution:
(3 marks)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
********** 19 **********
--- page 20 ---
Q7 b) A mobile phone service provider found that its customers pay bills through three modes: cheques,
credit card and internet. It collected the samples of the number of days( after receiving the billing SMS/bill)
taken by customers under each mode of payment as shown below:
Cheque (𝑥1)   8   10   7   14   11
Credit card ( 𝑥2)   7   5   10   9   9
Internet (𝑥3)   12   9   13   12   14
Assuming that the three samples are drawn from normal populations with equal variances, analyze the data
to test whether the mean payment time is the same for all three modes at the 5% level of significance.
Solution:
-----------------------------------------------------------------------------------------------------------------------
********** 20 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 3d95a933a925

- Departments: Computer Engineering, Computer Science
- Programmes: BTech CS 7055, Integrated Computer 7032, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CS_7055/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: mixed (24 pages), mean OCR confidence 67.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA
Tech (Comp)
Year: II/IV   Semester III/Semester VII(Exam Year: 2025)
Subject: Probability and Statistics
Date: NA   Time: NA to NA (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This synoptic contains 25 pages.
2. Question No. 1 is compuslory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
Q1 a) A class consists of 8 girls and 7 boys. If a committee of 4 students is chosen at random, compute
the probability that i) exactly 2 girls are selected, ii) atleast one girl is selected.
Solution:
Total ways = C(15,4) = 1365.   (1 mark)
(i) Favorable = C(8,2). C(7,2) = 28·21 = 588   (1 mark)
P(exactly 2 girls) = 588/1365 = 28/65=0.4308
(ii) P(at least one girl) = 1 − P(all boys)
= 1 − C(7,4)/C(15,4) = 1 − 35/1365 = 1330/1365 = 38/39=0.9743   (1 mark)
Note: It can be solved using binomial distribution, and marks to be given accordingly
----------------------------------------------------------------------------------------------------------------------------
Q1 b) The probability of mass function of a random variable X is zero except at the points X = 0, 1, 2. At these
points 𝑃(0) = 3𝑐3, 𝑃(1) = 4𝑐−10𝑐2, 𝑃(2) = 5𝑐−1 . Determine i) 𝑐 ii) 𝑃(𝑋< 1), 𝑃(1 < 𝑋≤2).
Solution:
We know that for probability mass function, the sum of all probabilities must be 1:
P(0) + P(1) + P(2) = 1   (1 Mark)
Substitute the given values:
3c³ + (4c – 10c²) + (5c – 1) = 1
Simplifying: 3c³ – 10c² + 9c – 2 = 0
Factoring gives: (c – 1)(3c² – 7c + 2) = 0
Thus, c = 1, 2, or 1/3. Only c = 1/3 gives non-negative probabilities.   (1 Mark)
(i) c = 1/3=0.33
(ii) P(X < 1) = 1/9 =0.12,   P(1 < X ≤ 2) = 2/3 =0.67   (2 Marks)
----------------------------------------------------------------------------------------------------------------------------
********** 1 **********
--- page 2 ---
Q1 c) The joint probability function of two discrete random variables 𝑋 and 𝑌 is given by 𝑓(𝑥, 𝑦) = 𝑐(2𝑥+
3𝑦), where 𝑥= 0, 1, 2 and 𝑦= 1, 2, 3 and 𝑓(𝑥, 𝑦) = 0, otherwise. Find i) the value of the constant 𝑐   ii)
Marginal probability function of 𝑋 and 𝑌.
Solution:
The probability distribution table :
y   1   2   3
x
0   3c   6c   7c   18c
1   5c   8c   11c   24c   (1 mark)
2   7c   10c   13c   30c
15   24c   33c
c
Since, 72c=1 this gives c = 1/72   (1 mark)
Marginal of X = 18/72, 24/72, 30/72   (1 mark)
Marginal of Y = 15/72, 24/72, 33/72   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 d) A discrete random variable 𝑋 takes the values 1,3,5 with probabilities 𝑃(𝑋= 1) = 0.3, 𝑃(𝑋= 3) =
0.4, 𝑃(𝑋= 5) = 0.3. Analyze the data to determine the coefficient of skewness.
Solution:
Mean
𝜇= ∑𝑥 𝑝(𝑥) = 1(0.3) + 3(0.4) + 5(0.3).
𝜇= 0.3 + 1.2 + 1.5 = 3.0.   (0.5 mark)
Variance:
𝐸[𝑋2] = 12(0.3) + 32(0.4) + 52(0.3)=11.4   (0.5 mark)
𝜇2 = 𝜎2 = 𝐸[𝑋2] −𝜇2 = 11.4 −(3.0)2 = 11.4 −9 = 2.4.   (0.5 mark)
Or 𝝁𝟐= 𝑬[(𝑿−𝝁)𝟐] = ∑(𝑿−𝝁)𝟐. 𝒑𝒊
Third central moment 𝝁𝟑= 𝑬[(𝑿−𝝁)𝟑] = ∑(𝑿−𝝁)𝟑. 𝒑𝒊
𝜇3 = −2.4 + 0 + 2.4 = 0.   (0.5 maks)
Coefficient of Skewness
𝛾1 = 𝜇3 = 𝜇3 3 =   0 = 0.   (1 mark)
𝜎3   𝜇 ⁄ 2   (√2.4)3
----------------------------------------------------------------------------------------------------------------------------
Alternatively:
These formulas may be used and marks given, accordingly.
********** 2 **********
--- page 3 ---
----------------------------------------------------------------------------------------------------------------------------
Q1 e) A random sample of 100 individuals has a mean height of 160 cm and standard deviation of 10 cm.
Would it be reasonable to assume that the population mean height is 165? Apply the appropriate test of
significance for the mean and state your conclusion.
Solution:
----------------------------------------------------------------------------------------------------------------------------
Q1 f) If the lines of regression of sample are 𝑥 + 6𝑦 = 6 and 3𝑥 + 2𝑦 = 10, compute the correlation
coefficient between 𝑥 and 𝑦.
Solution:
(1 mark)
(1 mark)
********** 3 **********
--- page 4 ---
As both regression coefficients are negative, r is negative. Therefore 𝑟= − 1 (1 mark)
3
----------------------------------------------------------------------------------------------------------------------------
Q2 a) A medical test is used to detect a rare disease that affects 1% of the population. The test correctly
identifies a diseased person 98% of the time, but it also wrongly identifies a healthy person as positive 3%
of the time. If a person chosen at random tests positive, find the probability that the person actually does not
have the disease.
Solution:
Let D: person has disease, Dc: person does not have disease
P: test is positive.
P(D)=0.01, P(P|D)=0.98, P(P|Dᶜ)=0.03.   (2 marks)
By Baye’s theorem
P(Dᶜ|P) = [P(P|Dᶜ)P(Dᶜ)] / [P(P|D)P(D) + P(P|Dᶜ)P(Dᶜ)]   (2 marks)
= (0.03·0.99)/(0.98·0.01 + 0.03·0.99) = 0.0297/0.0395 = 297/395 ≈ 0.752.   (2 marks)
Note: Notations may be different.
--------------------------------------------------------------------------------------------------------------------------
Q2 b) The two random variables X and Y have the joint probability density function (pdf) given by 𝑓(𝑥, 𝑦) =
𝐴𝑒−(2𝑥+𝑦) 𝑥, 𝑦 ≥0. Determine
(i) the value of A,
(ii) 𝑓(𝑦|𝑥).
Solution:
 
Since  f ( x , y ) dxdy  1   ……………..   (1 mark)


 Ae  (2 x  y ) dxdy  1   ……………….   (1 mark)
0 0
Solving , we get A =2   ………………   (1 mark)
To find f(y|x) :

Marginal prob function of x is : Xf ( x )   Ae  (2 x  y ) dy  2 e  2 x , x  0   …….   (1 mark)
0
f ( x , y ) 2 e  (2 x  y )    y
f ( y | x )        2 x  e   , y  0   ………………..   (2 marks)
f X ( x )   2 e
----------------------------------------------------------------------------------------------------------------------------
Q2 c) Two groups 𝐴 and 𝐵, each consisting of 100 individuals are treated identically except that group 𝐴 is
given a serum while group 𝐵 (the control group) is not. It is observed that 75 individuals in group 𝐴 and 65
people in group 𝐵 recover from the disease. Using a 1% level of significance, test whether the serum is
effective in improving the recovery rate.
********** 4 **********
--- page 5 ---
Solution:
Alternatively, 𝑝̅ can calculated using the given formula
𝑝̅ = 𝑛1𝑝1̅̅̅̅+𝑛2𝑝2̅̅̅̅ ,
𝑛1+𝑛2
Marks to be given if notations are different.
Note: Chi square test maybe used. Marks to be allotted accordingly.
---------------------------------------------------------------------------------------------------------------------------
Q3 a) A lot of 10 batteries contains 3 defective and 7 good ones. Two batteries are chosen one after another
without replacement.
(i) Compute the probability that both the selected batteries are good.
(ii) Find the probability that the second battery is good given that the first one tested is good.
(iii) Determine that the second battery is good if the first one tested is defective.
Solution:
Given Defective batteries: 3, Good batteries: 7, Total : 10. Two batteries are chosen without
replacement
(a) Probability both selected batteries are good
P(first good battery selected) = 7   (0.5 marks)
10
P( second good battery selected) = 6   (0.5 marks)
9
P(selecting 2 good batteries) = 7 ∙ 6 = 7   (1 mark)
10 9   15
********** 5 **********
--- page 6 ---
(b) Probability second battery is good given first is good.
First is good. Therefore remaining good batteries: 6, and total : 9   (1 mark)
P(second battery is good|first is good) = 6 = 2   (1 mark)
9   3
(c) Probability second battery is good given first is defective.
First is defective, remaining defective batteries : 2, good batteries: 7, Total: 9   (1 mark)
P(second battery good|first is defective) = 7   (1 mark)
9
Alternatively:
a) P(two good batteries): 7𝐶 2 = 7   (2 marks)
10𝐶 2   15
b) P(second battery is good|first is good)= 6𝐶 1 = 2   (2 marks)
9𝐶 1   3
c) P(second battery good|first is defective)= 7𝐶 1 = 7   (2 marks)
9𝐶 1   9
--------------------------------------------------------------------------------------------------------------------------
Q3 b) A random variable X has the given probability density function:
 e  x   x  0
f ( x ) 
 0   otherwise
Derive the moment generating function and hence evaluate the first four moments about origin.
Solution
(2 marks)
(1 mark)
(1 mark)
(1 mark)
(1 mark)
Or
********** 6 **********
--- page 7 ---
------------------------------------------------------------------------------------------------------------------
Q3 c) A sample of 200 fish of a particular kind taken at random from one end of a lake has mean weight of
20 lbs. and standard deviation of 2 lbs. At the other end of the lake, a sample of 80 fish of the same kind has
mean weight of 20.5 lbs. and standard deviation of 2 lbs. Apply an appropriate statistical test to examine
whether the difference between the mean weights is significant? (Use 5% level of significance)
Solution:
-------------------------------------------------------------------------------------------------------------------
********** 7 **********
--- page 8 ---
Q4 a) A small workshop records the number of machine breakdowns per day over 5 days as follows:
Number of breakdowns (x) 0 1 2 3 4
Frequency (f)   1 1 2 1 1
1. Fit a Poisson distribution to the data and
2. Calculate the expected frequencies
Solution:
(1 mark)
0
---------------------------------------------------------------------------------------------------------------------
********** 8 **********
--- page 9 ---
Q 4b) The following are the marks in Statistics (𝑋) and Mathematics (𝑌) of ten students
X   56   55   58   57   56   60   54   59   57   58
Y   68   67   67   65   68   70   66   68   66   70
Compute the coefficient of correlation and estimate marks in Mathematics of a student who scored 62 marks in
Statistics.
Solution:
********** 9 **********
--- page 10 ---
Alternatively:
(2 marks)
Let the regression line Y on X be 𝑌= 𝐴+ 𝐵𝑋.
Normal Equations are
∑𝑌= 𝑛𝐴+ 𝐵∑𝑋, ∑𝑋𝑌= 𝐴∑𝑋+ 𝐵∑𝑋2
Therefore
675 = 10𝐴+ 570𝐵
38490 = 570𝐴+ 32520𝐵. On solving we get
𝐴= 39 and 𝐵= 0.5
𝑏𝑦𝑥= 0.5 (regression coefficent Y on X)   (0.5 mark)
Let the regression line X on Y be 𝑋= 𝐴+ 𝐵𝑌.
Normal Equations are
∑𝑋= 𝑛𝐴+ 𝐵∑𝑌, ∑𝑋𝑌= 𝐴∑𝑌+ 𝐵∑𝑌2
Therefore
570 = 10𝐴+ 675𝐵
********** 10 **********
--- page 11 ---
38490 = 675𝐴+ 45587𝐵. On solving we get
𝐴= 15.67 and 𝐵= 0.61
𝑏𝑥𝑦= 0.0286 (regression coefficent X on Y)   (0.5 mark)
Coefficient of correlation:
𝑟= √𝑏𝑦𝑥∙𝑏𝑥𝑦= √(0.5)(0.61) = 0.55   (1 mark)
regression line Y on X is 𝑌= 39 + 0.5𝑋.
When X=62, 𝑌= 39 + 0.5(62) = 70   (1 mark)
Note: coefficient of correlation can be calculated by Karl Pearson/Spearman rank method. Marks allotted
accordingly.
----------------------------------------------------------------------------------------------------------------------------- ------------
Q4c) A group of boys and girls were given an intelligence test. The results are as follows:
Boys   Girls
Mean   124   121
Standard deviation   12   10
number   18   14
Apply an appropriate statistical test to analyze whether the mean score of boys is significantly different from
that of girls at 5% of level of significance.
Solution:
********** 11 **********
--- page 12 ---
Alternatively

Given: Boys: 2, = 124, s; = 12, ny = 18; Girls: # = 121, 5) =10,n9=14. —» jm
Step 1: Hypotheses =

Ho : (voys = Heirs (nO difference in means) A
Hy : Hyoys F Hyirte (means are different) J-24
Step 2: Pooled Standard Deviation

(ny — 1)s? + (m2 — 1)83 17+ 144 + 13+ 100
eer = Ss = V124.933 + 11.18 —. 2™

Step 3: Standard Error (S.E.)

ae i Ia aL
SEB. fate = 118 jut 7g 7218 -0.3565 3.99 __ 1m
Step 4: Test Statistic

2-2, 124-121
t= SE. = 399 ©0752 og |

Step 5: Degrees of Freedom

df =n +m —-2=18+14-2=30 ,
Step 6: Critical t-value
Two-tailed test at a = 0.05, df = 30: torso 2.042 —-—_—_» im
Step 7: Decision _

|t| = 0.752 < 2.042 => Accept Ho ee de 7

Step 8: Conclusion —
At the 5% level of significance, there is no significant difference between the mean
ligence scores of boys and girls, un

FRR DF OK
--- page 13 ---
Q5 a) i) A factory produces screws, and the probability of a screw being defective is 0.03. The screws are
packed in packets of 30. Out of a consignment of 800 packets, using Binomial distribution, compute the
number of packets that contain:
a) at least 2 defective screws
b) at most 2 defective screws.
Solution
0.1668
0.1668=0.93985
800X0.93985=752
----------------------------------------------------------------------------------------------------------------------------- ------------
Q5 a) ii) The lifetime of a certain type of battery is normally distributed with a mean of 400 hours and a
standard deviation of 45 hours. Compute the percentage of batteries that have a lifetime of at least 470 hours.
Solution:
********** 13 **********
--- page 14 ---
-------------------------------------------------------------------------------------------------------------------
Alternatively:
𝑍= 𝑋−𝜇 𝜎, 𝑍= 470−400 = 1.56   (2 marks)
45
𝑃(𝑍≥1.55) = 0.5 −0.4394 = 0.0606   (2 marks)
Percentage of batteries having lifetime of atleast 470 hours is 0.0606𝑋100 ≈6%   (1 mark)
********** 14 **********
--- page 15 ---
Q 5b) The following table shows the result of opinion poll for three political parties 𝐴, 𝐵 and 𝐶. Analyze
the data using Chi-square test to determine whether the age of the respondent and their choice of party are
independent at 5% level of significance.
Party
Age   Total
A   B   C
20-35   25   20   25   70
35-50   20   25   35   80
Above 50   25   25   30   80
Total   70   70   90   230
Solution:
********** 15 **********
--- page 16 ---
Step 3: Compute ? statistic.

cys (Oj — Ei)?
i Dy Bi; i

all cells

The contribution from each cell (rounded to three decimals) is:

Observed, Expected and contribution to x?

Age Party O E (O-E)/E

A 25 21.30 0.643
20-35 B 20 21.30 0.079

Cc 25 27.39 0.208

A 20 24.35 0.777 am
35-50 B 25 24.35 0.017 —

C 35 31.30 0.435

A © 25 24.35 0.018
Above50 B 25 24.35 0.018
C 30 31.30 0.054

Summing the contributions gives

Xéat © 0.641 + 0.079 + 0.208 + 0.777 +0.017 +0.435 +0.018 + 0.018 + 0.054 = 2.246 = 2.25.—\ mw

Conclusion: At the 5% level of significance, age and party choice are independent.

Step 4: Degrees of freedom and critical value.
Number of rows r = 3, number of columns c = 3, so degrees of freedom

df = (r—1)(e—1) = (8-1)(3-1) =4.
At a = 0.05 and df = 4, the critical value from the x? table is

x2.05,4 = 9-488. — iM

Step 5: Decision.
Since x2, = 2.25 < 9.488 = x2,,, we accept Ho (fail to reject Ho). >» Im

FOI GRR
--- page 17 ---
Q6 a) Calculate the Karl Pearson’s correlation coefficient from the following data
X   2   4   6   8   10   12   14
Y   50   45   40   35   30   25   20
Solution:
(3 marks)
(1 mark)
(1 mark)
(1 mark)
------------------------------------------------------------------------------------------------------------------
Alternatively the actual mean method formula may be used:
********** 17 **********
--- page 18 ---
Q6 b) A continuous random variable   has the probability density function
Compute   mean and variance.
Solution:
------------------------------------------------------------------------------------------------------------
********** 18 **********
--- page 19 ---
Q6 c) The nicotine contents in two random samples of tobacco are given below
Sample 1   21   24   25   26   27
Sample 2   22   27   28   30   31   36
Test whether the two populations have the same variance at 5% level of significance.
Solution:
-------------------------------------------------------------------------------------------------------------------------
Alternatively,
Students may be evaluated as per the solution given below and similar step marks awarded
********** 19 **********
--- page 20 ---
7 3
S*= 2 - (%) =(8

Nn,
o7= Sr. G)424) _ 6,
ni! G
o3= HS = G08) _ 2,
N2-| 5

2
G =2-6 , H=63
Nj=6 ,n2=5

Step @ Hy: 6) =e
H.: & 763

Ste 2
P® F=Si = 216 -4o0% C Interchangin 672 Ga So thot
cS $3
Value of F IS greater than >)
Step @ a=s/. Wemn-l=S-
V5=n,-I= 4
Fy= 6-256!

ae 40} <Fyx => Accept No ot SLs.

FRI ID QR RK
--- page 21 ---
Q7 a i) In partially destroyed laboratory record of an analysis of correlation data, the following information
is available: the variance of 𝑋 is 9 , and the two regression equations are: 8𝑋– 10𝑌 + 66 = 0 &
40𝑋– 18𝑌 = 214. Using the given information determine
a) the means of 𝑋 and 𝑌 .
b) the correlation coefficient between 𝑋 and 𝑌.
c) standard deviation of 𝑌
Solution:
(1 marks)
(1 mark)
(1 marks)
(1 mark)
:
(1 mark)
---------------------------------------------------------------------------------------------------------------------------
********** 21 **********
--- page 22 ---
7a ii) Calculate the Spearman’s rank correlation coefficient from the following data.
X   10   12   18   18   15   40
Y   12   18   25   25   50   25
Solution:
(3 marks)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
********** 22 **********
--- page 23 ---
Q7 b) A mobile phone service provider found that its customers pay bills through three modes: cheques,
credit card and internet. It collected the samples of the number of days( after receiving the billing SMS/bill)
taken by customers under each mode of payment as shown below:
Cheque (𝑥1)   8   10   7   14   11
Credit card ( 𝑥2)   7   5   10   9   9
Internet (𝑥3)   12   9   13   12   14
Assuming that the three samples are drawn from normal populations with equal variances, analyze the data
to test whether the mean payment time is the same for all three modes at the 5% level of significance.
Solution:
Or
********** 23 **********
--- page 24 ---
Alternate way:

Ho = Meheque = Heredit = Hinternety 4, : At least one mean is different J— ( m
Given three samples: Cheque (x;), Credit Card (x2), Internet (x3).
x, :8,10,7,14,11, 22: 7,5,10,9,9, x3: 12,9,13,12,14
nm =Nn2=n3=5, N(tolal number of observations across all groups)=15, k=3
Define
T=>o%X, where i € {1,2,3} gel

T=VOX=50, M=) os =40, => Xs =60,
Next, the correction factor (CF) is

T? _ 150?
CF = | = 5 = 1500

Sum of squares between the samples/ columns (SSC) is

™M
T? 2 2 2 2
SSC = enor = 4 Oop = 5004-320 + 720 — 1500 = 40

Total sum of square is

SST = )> 2? — CF = 1600 — 1500 = 100
(as D2? = 530 + 336 + 734 = 1600)

Sum of squares within the samples/errors (SSE) o rt
SSE = SST — SSC = 100 — 40 = 60
Degrees of freedom:
dfo =k-1=2, dfg =N—-k=12, dfp=N-1=14
Mean squares:

msc = 55 _ 2 2, MsE====S=5 ~7? (™
EB

F- statistic:

= Msp 5 7400 —) ( laa

Foo5(2, 12) = 3.885

Critical value at a = 0.05:

Since
Fea) = 4.00 > 3.885 = Frit, J — IM

we reject Ho.
Conclusion: At the 5% level of significance, the mean payment time is not the same
for all three modes of payment.

FRI ID AFR RK
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 20f88396b46e

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Civil_7005/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 27fb10b9a35c

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CyberSecurity_7010/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper c90802a23794

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_EXTC_7006/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 0917a326c398

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_IT_7001/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper dc66c73ba47e

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Mechanical_7003/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 0f38f255de3d

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Mechatronics_7004/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 8ca63faa4547

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_IT_7041/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper e907833eae3d

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_IT_7037/Probability and Statistics/ANS_Probability and Statistics(702BS0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 6df22b05ba15

- Departments: Mechanical
- Programmes: Integrated Mechanical 7031
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_Mechanical_7031/Probability and Statistics/ANS_Probability and Statistics(702BS0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (13 pages), mean OCR confidence 35.6
- 20 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
®) 4) Qven- eve ) a=

eo 4 £=220
Ksome Ho! tm toon * ee
Ay M ti20y =
NBo-)20D
= = {, 28c¢ —_» im
ae Sal" esis ———.

At Stl, L9s @ for drow dusted feat 29 AX =1-9G—-» Im
: elem Yo te accepted —> im


eee —
im
=

a Dae e ee 7 a > as 34192.5 bay 3 =O,US_» Jw


Q2) a) Lot ne Soil temporodwre Y= Germinctin Sct).

N=, TA= 350 , TyYH=\VF , TAY = SsSus

: am
Tos ue SNE Syyy =
* rev Tay — Fn IM a
Jnin'= Gp ny eay> =
= 8 Caavd - (ase) (193)
oat
J a Cssue) -@<o)> Sa(Gui\—Gas> =

= —0.F420 ‘i im)
Te _—

FIC 2 I HH ar
--- page 3 ---
FC QI a iar
--- page 4 ---
(©e) M=8) Faye |Y= 24.62 “fom
2 ie
F4-F4-F) = - 295.44 T= 292.6 TW) = @yez
, #

r. 2 CA-H) C9)

J ocasay® sae
> ~295.94

1 293.5 yCeq 8p _

> lm

=— 0,4y430 os
z — im

Qs)» Meon=m=2o7— Ml. 2.07430 ~—-~ Im
z+ 68 = —_

a oe 2.045 > a O. WEF D {= 0. $893 — Pam

A ny

a ° \ 2 2 y S

pcm) 0.06868 | 9.243 |o,ayyS | 0.2443 | 0.08655] O.0\22¢ — 2

Et | 4-609 16-S4>2] 29 yyQ3] Jo.6ia>| 5. e856] o. gaye

¥@ '2@ 1@ [2 eG'leO 120 HS

O©2) D comple A> n=180, 7-68 ,S=10 +

Sample Qp> “M2=ls0 , Aa65 , Sretr —

Acume Ho! Ay = Mo
#,' NM, tM> ™ pa

standard err (se)= | Sty Se” _ ),92)) ——> 2m
wy “oe Oo =

iel= | 33 = 2.436 —_ 36

= a 621.96 — = im

\>ZK > Yo Is qected|

jal>24 rey

— im

FIC 7) IC HOH
--- page 5 ---
63) 9) Given! Mel2, 6-3 , N =too cm Sie 4 battery

=0.6- Area bet” zac Qz=1
atl | yz =0.5— 0,.3W8 = 0.1682 ~15. 8F°/, zm

2~ Zz) —— a
, —_— —_

2m

it) piace)= p(2<- a= Pra to fo leit 4 Za-2 |

=0.5- Aven bet” x-0hz-2
Fh itses =0.5 — 0 4992 = 0.0228 = 2. 28°/,

zZe-2 _—

i) Plocnct) = p (0.664220 .662)«hren bet™ 8.6640 0- “|

2 2% Area bes” p£Locé
4} = 2% 0,21 = 0, YIO = 49.08 1.

—046, o6b -

Tow}! 4 Bic} DIE] F] G4 | |a

Al [S] ISP te] 6] nw fi4l] fg ire

4S 180 146 |asloy | iz] se] oz }o2 | 46l'2

QRl}1 }o¢}/a]2> {lol +14 18 [9-1 6 — Im

Ro| 4 [is132 1/619 18 | F] F/I] to —- im

2™

de | 4 = v6 | \ \ u 5/16 ——s 10

4

*. Lae: {13-5 w= 2 —— im
—_—_ i

G=1.- = Hon?)

—_

> im
Si. mire erik: >)
\o?_ fo
= Vis 304 — . im

— _—_

FEISS (5 FC ICRF
--- page 6 ---
Hit Adbibctes ore, depend : tn Mi
Esipected values | »

Ue S public Be nat ie


Urban | 150 100 260
= s | om
Ruel | So lon 260 aan
tote) ; 250 QD Con ,
Ee 4 0-£) ~ 1g0-1S0) > Fol *4 480), @o-te) *
=
= O+4+6+4 =
= 80

=—_— 2 Cc

- = = B —>1M

5e/, LOS @ ooeacr-ike-t at S “Pd 3-Buls —o lt
—__—s {mM

a a

64) A) Let m= Nours Study Y= Werks
2 TAY = 2210 ) T4219 —" 2™

i's. » ey —-

Val

- Fd .
= boys = pid et Hal cat Enh = FT A i —_—_—_——4 dw)
nin — (i)? a =

Line » voqremion 2 (y-q)=byn(-)
>= 16.23+F.66>) | —= 19)

shen *=10 5 Y=Q2.423 sm
— —,

FEC 6 FC IG Ir
--- page 7 ---
FIC 7 IC OHH
--- page 8 ---
©4 &) pois _ Bit Ai2habutton
| 2 | Tote)
tloe | 3¢ | 5¢

2] Gel 6¢ lye 2M

2) toc nelac.

~Tekey | IFC | wd | BFC

Btc=) —. > Lm
Margin! Aahslordion 4» ‘.
pay [Lt SHE * =
Mangia dalutingy OP 4 .

ieee

PCr! 443) = Pra Ne Deplonr tA) ep bree es) fh) — sa

Ou) ¢ =) fzsume. ‘ 6 ape
6,”

6, cae » a > "Ft og
Wae6 , T4o> F9 ) ip = 13.1OF » im

Day = (850 P) S= Day) a.€ —— we

rar ares, > Soo Zrs-naC)~ 2.166) ___5 1m

Ys—} =—

ne Bn 8S. =1,6232 ——= ty

At Se], WS DOF = (m4 ne-D= (oS) a fa= 5.002 7m

2’. ELIA Wo Is accepted, ——= 1m

——

FOCI 9 FCI IC Ir
--- page 9 ---
FIC QF OH ar
--- page 10 ---
©5) i) Gal Ae Shdest ts (pow Science ® pGjeo.C L
im

Be Studeut f< v commence \ PCE) = 0 Me

; + puja) = 0.95 2 P(A/e)-0.00 —+ 2m
PCAla) = PCA) pHa) ——_ Im
pd pCM/A)+ PD P(e) =

> 0.864% 0.80

(o.cyo2ch @.ysxo.0) ~~ =
== ‘Us 68)M tien shinai 5 im
=O _—_—_
©») b) b) Given for) - pee ,olye)
lane ‘

cats at }'=6[4-4]= 0.9= && —oim
ae)" Fffesnen = = fine “(ots _. im

6[eahle [4-0

“No)= Elm) — (Eon) 0.3 {0.57% 0,06 ———= jm

—— 2M.

—_ H.. At least are velcle los dithered yen fd ebhicion

K= 9, mmMaeMses MHI T= FF Ta= 59 e-t2d¢nz281m

Covrectton [or mean Ccm)= f = 3y6c.6
Total sum 9 sqrowe, C88) = Taig = 122. way $i =
treatment cum 4. Somarre. Csev\. (= SAB coe = (09.2

“i hHoM

As Mi Nt (Sse) ates set = 122 P ~
TTreetmect meom Sqrone(Mst)= SST sy, ee
Ka
Bsr wean. Square CMse= SSE aa Fp j-20

* £= MST/Aqse = y9, 6367 ———= Lm isctod
Fol= 3.8853 114 & €>FK > He ts @

FOI 7 QF ICR Ir
--- page 11 ---
@e) 4) w=1.¢ A= No. 9 breakdowns


Poisson distbutin > peas ew"L Z!8 yg”

ae °
4) pines) = eg s\n

“1 ime -",

=o, Ata 28 oP. 0.F306

ity PCax2) =f- porea) = pr pore 0 »

a [‘°. \6634+0.293S] = 0. Caz0 —_
————

im

B= bever jump Aroffic Signals > pce)- oo
zg pan d= 0,30
D PGla)= Pare 80 - —

“pte) —o. 0 0-6 al

i 8 (AnB)_ 9.20 _ » 46 m
D Oh) ae eee

i) plavd- poap@-plars) = 0.8 ———>
@é) s)

Given '- n,=\oo a >220 => PiaZL = ose
= iT)

Vi2= 350 j Aas=fe p> = A2 =0.sty3 —
Ma a

<hesume. Yo: Pi=Pa oe
Ay Pr +Pa <i
p= A+A2 ~ 9.69233 3 q=0. 466+ — 1M
Ww Me

Stendaned em (Se) [eq Aad) =0.036[2 —» 2m

-_ =
Beet aes

= 0.995F¢—» I

At S*/. 10s 2fSs tise eiledfest ZK='.4G6 — iv

ean Re
--- page 12 ---
@3) 4 Cries qe K(n+v) , 04421, OL4et

© roe ‘
ee ia a Ddady=! > a 'ScCntS)dndy =|
«Sate as 1d Wty) =) a

ce(gseg yer ox[eed je GT
Naxginol dab bution a:

fn) = ae | (etd i a
oda |

~ [ree], e att _

nal Asbobition |S ° =
Moe ah al {Gr >4> -
> [29], ~ 4+3 ode) -
—s

o>» Mn Ce) = (Efe =) f= “yoPaton = | Ay — 1m

auf Mt Serene]
2 os o
~ +
“p< gr eats e st ce ~ 2»
A
“42 [1- a4 4 BT
t am 1
)
a= Frgcodnn tatine 413" Ie" = in

sal = patient [thes Ho ee

Aad = "(+4 ofthe) de = '(nifam = Tes oo Lie

= —

RK KKK RK KK 12
--- page 13 ---
@><) Giver : Miato Al=6.8 S)=t.5

YNo-8 t Yo= o.2 J ke 4 =
Hesume Ho. An eM
; — Im
4). Ae Ale =
Poded s.o Gp)= [¢ ae Bain 3? ool = 1.6380
Hi aha - 2 ——. * at

Shandancl envy (Ce)= $ pat. = 0.4767 51m

tt - _ Ee.

= pedis — im

=) thm! 346 ——> im

—_

--. lk]y toa > He ‘ —— im

=

FOI 7 2 FC CR
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 6c2c163135d3

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Probability and Statistics/ANS_Probability and Statistics(703BS0C003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Questions 1 is compulsory.
5. Solve any four out of remaining six questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
9. Use of scientific calculator is allowed.
Q.1a) A discrete random variable X has the following probability distribution:
X   0   1   2   3
P(X=x) A 2A 3A B
If the mean of X is 1.5, identify the values of A and B.
Solution:
Step 1: Use the condition ΣP(X)=1
A + 2A + 3A + B = 1
6A + B = 1 ...(1)   (1 Marks)
Step 2: Use the formula for mean
Mean
E(X) = ΣxP(X)   (1 Marks)
E(X) = 0·A + 1·2A + 2·3A + 3·B
= 2A + 6A + 3B
= 8A + 3B=1.5 …(2)   (1 Marks)
Solving
A = 0.15 and B = 0.1   (1 Marks)
Q.1b)
The joint probability distribution of X and Y is given by:
P(X=x, Y=y) = k(3x + 4y), where x = 1,2,3 and y = 0,1,2.
Find:
(i) the value of k
(ii) the marginal probability distribution of X.
Solution:
Step 1: Total probability = 1
ΣΣ k(3x + 4y) = 1   (1 mark)
Total = 81k ⇒ k = 1/81   (1 mark)
********** 1 **********
--- page 2 ---
Step 2: Marginal distribution of X
P(X=x) = Σ_y P(X=x, Y=y)
Step 3: Calculation
P(X=1)=k(3+7+11)=21k=21/81=7/27
P(X=2)=k(6+10+14)=30k=30/81=10/27
P(X=3)=k(9+13+17)=39k=39/81=13/27
Marginal distribution of X: {7/27, 10/27, 13/27}   (2 mark)
Q.1c)
Identify the type of correlation in each of the following cases:
(i) r = +1
(ii) r = -0.62
(iii) 2r² + r - 3 = 0
Solution:
Step 1: For r = +1
Since the correlation coefficient is exactly +1, the variables are perfectly positively correlated.
Answer: Perfect positive correlation. (1 mark)
Step 2: For r = -0.62
Since r is negative and its magnitude is moderately high, the variables show moderate negative correlation.
Answer: negative correlation.   (1 mark)
Step 3: Solve 2r² + r - 3 = 0
2r² + r - 3 = 0
(2r + 3)(r - 1) = 0
So, r = -3/2 or r = 1.   (1 mark)
Step 4: Interpret valid value of r (1 mark)
Since the correlation coefficient must lie between -1 and 1, r = -3/2 is not possible.
Hence valid value is r = 1.
Answer: Perfect positive correlation.   (1 mark)
Q.1d)
If three coins are thrown, find the probability of getting:
(i) exactly two heads
(ii) at least two heads
Solution:
Step 1: Total outcomes
Total outcomes = 8
Step 2: Exactly two heads   (1 mark)
Favorable outcomes: {HHT, HTH, THH} = 3
P = 3/8   (1 mark)
Step 3: At least two heads   (1 mark)
Outcomes: 2 heads (3) + 3 heads (1)
Total = 4
P = 4/8 = ½   (1 mark)
********** 2 **********
--- page 3 ---
Q1e)
A random sample of 100 items is taken from a population with known standard deviation σ = 10. The sample
mean is found to be 52. Test whether the population mean is greater than 50 at 5% level of significance.
Solution:
Step 1: State hypotheses (1 mark)
H₀: μ = 50
H₁: μ > 50
Step 2: Test statistic (Z-test) (1 mark)
Z = (x̄ - μ) / (σ/√n)
= (52 - 50) / (10/√100)
= 2 / 1 = 2
Step 3: Critical value (1 mark)
At 5% level (one-tailed), Zₐ = 1.645
Since Z = 2 > 1.645, reject H₀
Step 4: Conclusion (1 mark)
There is sufficient evidence to conclude that the population mean is greater than 50.
Q.2a)
In a survey, 200 out of 500 men were found to prefer a product, while 180 out of 400 women preferred the
same product. Find whether the proportions of men and women who prefer the product are equal at 5% level
of significance.
Solution:
Step 1:
State hypotheses
H₀: p₁ = p₂
H₁: p₁ ≠ p₂   (1 mark)
Step 2: Compute sample proportions
p₁ = 200/500 = 0.4
p₂ = 180/400 = 0.45   (1 mark)
Pooled proportion, P = (200 + 180) / (500 + 400) = 380/900 ≈ 0.422   (1 mark)
Step 3: Test statistic
Z = (p₁ - p₂) / √[P(1-P)(1/n₁ + 1/n₂)]   (1 mark)
= (0.4 - 0.45) / √[0.422×0.578(1/500 + 1/400)]
≈ -0.05 / 0.033 ≈ -1.52   (1 mark)
Step 4: Conclusion (1 mark)
At 5% level, critical value = ±1.96
Since |Z| = 1.52 < 1.96, do not reject H₀.
There is no significant difference between the proportions.   (1 mark)
Q.2b) The joint probability density function is:
f(x,y) = kxy, 0 ≤ x ≤ 2, 0 ≤ y ≤ 1
Find:
(i) k
(ii) P(X ≤ 1, Y ≤ 1/2)
Solution:
********** 3 **********
--- page 4 ---
Step 1: ∫₀² ∫₀¹ kxy dy dx = 1   (1 mark)
k ∫₀² x[x/2] dx = k∫₀² x²/2 dx (1 mark)
= k[ x³/6 ]₀² = k(8/6)=4k/3=1 ⇒ k=3/4 (1 mark)
Step 2: Required probability
P = ∫₀¹ ∫₀^{1/2} (3/4)xy dy dx   (1 mark)
Step 3: Integration
= (3/4) ∫₀¹ x[y²/2]₀^{1/2} dx
= (3/4) ∫₀¹ x(1/8) dx   (1 mark)
Step 4: Final answer (1 mark)
= 3/64
Q.2c)
A continuous random variable X has the probability density function:
f(x) = kx(2 - x), 0 ≤ x ≤ 2
0, otherwise.
Find:
(i) the value of k
(ii) the mean of X
(iii) the variance of X
Solution:
Step 1: Normalization condition
∫₀² kx(2 - x) dx = 1   (1 marks)
= k∫₀² (2x - x²) dx
= k [x² - x³/3]₀²   (1 marks)
= k (4 - 8/3) = k(4/3)
⇒ k = ¾   (1 marks)
Step 2: Mean E(X)
E(X) = ∫₀² x·f(x) dx = k∫₀² x²(2 - x) dx   (1 marks)
= k∫₀² (2x² - x³) dx
= k [2x³/3 - x⁴/4]₀²   (1 marks)
= k (16/3 - 16/4)
= k (16/3 - 4) = k(4/3)
= (3/4)(4/3) = 1
Step 3: E(X²)
E(X²) = k∫₀² x³(2 - x) dx   (1 marks)
= k∫₀² (2x³ - x⁴) dx
= k [2x⁴/4 - x⁵/5]₀²
= k (8 - 32/5)
= k (8/5) = (3/4)(8/5) = 6/5   (1 marks)
Step 4: Variance
Var(X) = E(X²) - [E(X)]²
= 6/5 - 1² = 1/5   (1 marks)
********** 4 **********
--- page 5 ---
Q.3a)
Two fair dice are thrown simultaneously.
Let A be the event that the sum of the numbers is even.
Let B be the event that at least one die shows 4.
Solution:
(i) Find P(A)
(ii) Find P(A ∩ B)
(iii) Find P(A|B)
Step 1: Total outcomes
Total sample space = 36 outcomes.
Step 2: Find P(A)
Sum is even when both numbers are even or both are odd.
Favorable outcomes = 18
P(A) = 18/36 = ½   (2 mark)
Step 3: Find P(A ∩ B)
B: at least one die is 4 → outcomes = {(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(1,4),(2,4),(3,4),(5,4),(6,4)} = 11
A ∩ B: sum even AND at least one 4 → {(4,2),(4,4),(4,6),(2,4),(6,4)} = 5
P(A ∩ B) = 5/36   (2 marks)
Step 4: Conditional probability
P(A|B) = P(A ∩ B) / P(B)   (1 mark)
P(B) = 11/36
P(A|B) = (5/36)/(11/36) = 5/11   (1 mark)
Q.3b)
A sample of 100 students from college A has mean score 68 with sample standard deviation s₁ = 10. A sample of
120 students from college B has mean score 65 with sample standard deviation s₂ = 12. Test at 5% level of
significance whether there is a significant difference between the mean scores of the two colleges.
Solution:
Step 1: State hypotheses (1 mark)
H₀: μ₁ = μ₂
H₁: μ₁ ≠ μ₂
Step 2: Test statistic formula (1 mark)
Z = (x̄₁ - x̄₂) / √[(s₁²/n₁) + (s₂²/n₂)]
Step 3: Substitution and calculation
x̄₁ = 68, x̄₂ = 65
s₁ = 10, s₂ = 12
n₁ = 100, n₂ = 120   (1 mark)
Z = (68 - 65) / √[(100/100) + (144/120)]
= 3 / √(1 + 1.2)
= 3 / √2.2 ≈ 2.02   (1 mark)
Step 4: Critical value (1 mark)
At 5% level, Z = ±1.96
Since |Z| = 2.02 > 1.96, reject H₀
Step 5: Conclusion (1 mark)
There is a significant difference between the mean scores of the two colleges.
********** 5 **********
--- page 6 ---
Q.3c)
A discrete random variable X takes values 0, 1, 2 with probability distribution:
P(X=x) = {1/4, 1/2, 1/4} respectively.
Determine Moment Generating Function (MGF), Coefficient of Skewness & Kurtosis
Solution:
Step 1: MGF (2 marks)
M_X(t) = Σ e^{tx} P(X=x)
= (1/4)e^{0} + (1/2)e^{t} + (1/4)e^{2t}
= 1/4 + (1/2)e^{t} + (1/4)e^{2t}
Step 2: Skewness
E(X³)=0+1/2+8/4=1/2+2=5/2   (1 mark)
μ₃ = E(X³) - 3μE(X²) + 2μ³   (1 mark)
= 5/2 - 3(1)(3/2) + 2(1)
= 5/2 - 9/2 + 2 = 0   (1 mark)
Step 3: Kurtosis
E(X⁴)=0+1/2+16/4=1/2+4=9/2   (1 mark)
μ₄ = E(X⁴) - 4μE(X³) + 6μ²E(X²) - 3μ⁴
= 9/2 - 4(1)(5/2) + 6(1)(3/2) - 3
= 9/2 -10 +9 -3 = ½   (1 mark)
β₂ = μ₄ / (Var)² = (1/2)/(1/2)² = 2
Kurtosis = 2   (1 mark)
Q.4a)
In a communication network, the number of packet errors per minute follows a Poisson distribution with mean
2.
Estimate:
(i) the probability that exactly 3 errors occur in a minute
(ii) the probability that at most 2 errors occur
(iii) the probability that at least 1 error occurs
Solution:
Step 1: Identify distribution
Given Poisson distribution with mean λ = 2
P(X = x) = e^{-λ} λ^x / x!   (1 mark)
Step 2: P(X = 3)
P(3) = e^{-2} * 2^3 / 3!
= e^{-2} * 8 / 6 = (4/3)e^{-2} ≈ 0.180   (2 mark)
Step 3: P(X ≤ 2)
P(0) = e^{-2}
P(1) = 2e^{-2}
P(2) = 2e^{-2}
P(X≤2)= e^{-2}(1 + 2 + 2) = 5e^{-2} ≈ 0.677   (2 marks)
Step 4: P(X ≥ 1)   (1 mark)
P(X≥1)=1 - P(0)=1 - e^{-2}
********** 6 **********
--- page 7 ---
Q.4b)
A software company compares average response time (ms) of two web servers.
Server A: n₁ = 8, x̄₁ = 120, s₁ = 10
Server B: n₂ = 10, x̄₂ = 110, s₂ = 15
Test at 5% level whether there is a significant difference in mean response times.
Solution:
Step 1: Hypotheses
H₀: μ₁ = μ₂
H₁: μ₁ ≠ μ₂   (1 mark)
Step 2:
S² = [(n₁)s₁² + (n₂)s₂²] / (n₁ + n₂ - 2)
= [8(100) + 10(225)] / 16
= (800 + 2250)/16 = 3050/16 ≈ 190.625   (1 mark)
Step 3: Test statistic
t = (x̄₁ - x̄₂) / √[S²(1/n₁ + 1/n₂)]   (1 mark)
= 10 / √[190.625(1/8 + 1/10)]
= 10 / √[190.625 × 0.225]
= 10 / √42.89 ≈ 10 / 6.55 ≈ 1.53   (1 mark)
Step 4: Critical value
df = 16, t₀.₀₅ ≈ 2.12   (1 mark)
|t| = 1.53 < 2.12 ⇒ Do not reject H₀
Step 5: Conclusion
No significant difference in response times.   (1 mark)
Q.4c)
x: 2 4 5 7 9 10 12 15
y: 3 5 6 7 8 9 11 12
Find regression line y on x using normal equations.
x   y   x²   xy
2   3   4   6
4   5   16   20
5   6   25   30
7   7   49   49
9   8   81   72
10   9   100   90
12   11   144   132
15   12   225   180
Σx = 64   Σy = 61   Σx² = 644   Σxy = 579
(04 marks)
Step 1: Write normal equations
Σy = na + bΣx
Σxy = aΣx + bΣx²   (1 mark)
********** 7 **********
--- page 8 ---
61 = 8a + 64b
601 = 64a + 700b   (1 mark)
Step 2: Solve equations
b ≈ 0.601, a ≈ 2.817   (1 mark)
Step 3: Regression equation
y = a + bx = 2.817 + 0.601x   (1 mark)
Q.5a)
Two independent samples of sizes 9 and 8 have sample variances 4.5 and 3.2 respectively. Test at 5% level
whether the population variances are equal.
Solution:
Step 1: Hypotheses (1 mark)
H₀: σ₁² = σ₂²
H₁: σ₁² ≠ σ₂²
Step 2: Estimate population variances (2 mark)
σ₁² ≈ (n₁ s₁²)/(n₁ - 1) = (9×4.5)/8 = 5.0625
σ₂² ≈ (n₂ s₂²)/(n₂ - 1) = (8×3.2)/7 ≈ 3.657
Step 3: Test statistic (1 mark)
F = Larger / Smaller = 5.0625 / 3.657 ≈ 1.38
Step 4: Degrees of freedom (1 mark)
v₁ = 8, v₂ = 7
Step 5: Critical value F₀.₀₅(8,7) ≈ 3.73
Since F < critical value, do not reject H₀
No significant difference in population variances.   (1 mark)
Q.5b)
The following data give the marks obtained by 8 students before and after training:
Before: 45 50 48 52 47 49 51 46
After: 48 53 50 55 49 52 54 48
Test at 5% level whether students benefited from training.
x₁   x₂   d = x₁ - x₂   d²
45   48   -3   9
50   53   -3   9
48   50   -2   4
52   55   -3   9
47   49   -2   4
49   52   -3   9
51   54   -3   9
46   48   -2   4
Σd = -21   Σd² = 57
Solution:
Step 1: Mean difference   (1 mark)
n=8, d̄ = Σd/n = -21/8 = -2.625
********** 8 **********
--- page 9 ---
s² = (1/n)Σd² − (d̄)² = 57/8 − (2.625)² = 0.234
Step 2: Standard deviation   (1 mark)
s = √0.234 = 0.484
Step 3: Test statistic
t = d̄ / (s/√(n−1))   (1 mark)
= -2.625/(0.484/√7) ≈ -14.34   (1 mark)
Step 4: Critical value   (1 mark)
df = 7, t₀.₀₅ = 1.895
Step 5: Conclusion (1 mark)
|t| > t₀.₀₅ ⇒ Reject H₀ ⇒ Students benefited
Q.5c)
The average daily number of units produced by a manufacturing plant is 520 units, with a standard deviation of
60 units. Assume that the number of units produced per day follows a normal distribution.
Compute:
(i) the probability that between 470 and 560 units are produced in a day
(ii) the probability that more than the expected number of units are produced in a day
Solution:
Step 1: Identify mean and standard deviation (2 marks)
Mean, μ = 520
Standard deviation, σ = 60
Step 2: Convert the limits into standard normal variates
For x = 470:
z = (470 - 520)/60 = -50/60 = -0.83
For x = 560:
z = (560 - 520)/60 = 40/60 = 0.67
Step 3: Find probability between the two values
P(470 < X < 560) = P(-0.83 < Z < 0.67)   (2 marks)
= P(0 < Z < 0.83) + P(0 < Z < 0.67)
= 0.2967 + 0.2486
= 0.5453   (1 marks)
Step 4: Probability of more than expected value
P(X > μ) = =P(Z > 0)
= 0.5
units are produced = 0.5
Q.6a) A cybersecurity system classifies incoming emails as Spam or Not Spam.
Based on past data:
- 40% of emails are Spam
- 60% are Not Spam
- The system correctly identifies Spam emails with probability 0.9
- It incorrectly classifies Not Spam emails as Spam with probability 0.2
If an email is classified as Spam, find the probability that it is actually Spam.
********** 9 **********
--- page 10 ---
Solution:
Step 1: Define events (1 mark)
B₁: Spam, B₂: Not Spam, A: classified as Spam
Step 2: Write Bayes theorem (2 mark)
P(B₁|A) = [P(B₁)P(A|B₁)] / [P(B₁)P(A|B₁) + P(B₂)P(A|B₂)]
Step 3: Substitute values (2 marks)
P(B₁|A) = (0.4×0.9) / [(0.4×0.9) + (0.6×0.2)]
= 0.36 / (0.36 + 0.12)
Step 4: Simplify (1 mark)
P(B₁|A) = 0.36 / 0.48 = 0.75
Q.6b) A placement officer wants to study the relationship between students’ rank in Aptitude Test and their
rank in Coding Test.
Aptitude Rank:   2 4 1 5 3 6 8 7
Coding Rank:   3 5 2 6 1 7 8 4
Evaluate Spearman’s rank correlation coefficient.
Solution:
Student   R₁   R₂   d = R₁-R₂   d²
P   2   3   -1   1
Q   4   5   -1   1
R   1   2   -1   1
S   5   6   -1   1
T   3   1   2   4
U   6   7   -1   1
V   8   8   0   0
W   7   4   3   9
Total   Σd = 0   Σd² = 18
(3 mark)
Step 1: Formula (1 mark)
R= 1 - [6Σd² / n(n² - 1)]
Step 2: Values
n = 8, Σd² = 18
Step 3: Substitution (1 marks)
R = 1 - [6×18 / 8(64 - 1)]
= 1 - [108 / 504]
Step 4: Result
R ≈ 0.7857 (1 mark)
********** 10 **********
--- page 11 ---
Q.6c) A company wants to compare the average number of tasks completed per day by employees using three
different software tools.
Tool A Tool B Tool C
22   18   25
24   20   27
26   19   24
23   17   26
25   21   28
21   16   23
Test at 5% level of significance whether there is a significant difference in mean productivity using one-way
ANOVA.
Solution:
STEP 1: State the hypotheses (1 mark)
H₀: μ₁ = μ₂ = μ₃
H₁: At least one of the means differs
STEP 2: Compute totals and means (1 mark)
For Tool A: T₁ = 22 + 24 + 26 + 23 + 25 + 21 = 141,   x̄₁ = 141/6 = 23.5
For Tool B: T₂ = 18 + 20 + 19 + 17 + 21 + 16 = 111,   x̄₂ = 111/6 = 18.5
For Tool C: T₃ = 25 + 27 + 24 + 26 + 28 + 23 = 153,   x̄₃ = 153/6 = 25.5
Grand total T = 141 + 111 + 153 = 405, N = 18
Grand mean x̄ = 405/18 = 22.5
STEP 3: Calculate between-group sum of squares (SSC) (1 mark)
SSC = n₁(x̄₁ − x̄)² + n₂(x̄₂ − x̄)² + n₃(x̄₃ − x̄)²
= 6(23.5 − 22.5)² + 6(18.5 − 22.5)² + 6(25.5 − 22.5)²
= 6(1)² + 6(−4)² + 6(3)²
= 6 + 96 + 54 = 156
STEP 4: Calculate within-group sum of squares (SSE) (2 marks)
For Tool A:
SSE₁ = (22−23.5)² + (24−23.5)² + (26−23.5)² + (23−23.5)² + (25−23.5)² + (21−23.5)²
= 2.25 + 0.25 + 6.25 + 0.25 + 2.25 + 6.25 = 17.5
For Tool B:
SSE₂ = (18−18.5)² + (20−18.5)² + (19−18.5)² + (17−18.5)² + (21−18.5)² + (16−18.5)²
= 0.25 + 2.25 + 0.25 + 2.25 + 6.25 + 6.25 = 17.5
For Tool C:
SSE₃ = (25−25.5)² + (27−25.5)² + (24−25.5)² + (26−25.5)² + (28−25.5)² + (23−25.5)²
= 0.25 + 2.25 + 2.25 + 0.25 + 6.25 + 6.25 = 17.5
Therefore, SSE = SSE₁ + SSE₂ + SSE₃ = 17.5 + 17.5 + 17.5 = 52.5
STEP 5: Degrees of freedom (1 mark)
Between groups: df₁ = k − 1 = 3 − 1 = 2
Within groups: df₂ = N − k = 18 − 3 = 15
STEP 6: Calculate MSC, MSE and F-ratio (1 mark)
MSC = SSC/df₁ = 156/2 = 78
********** 11 **********
--- page 12 ---
MSE = SSE/df₂ = 52.5/15 = 3.5
F = MSC/MSE = 78/3.5 = 22.29
STEP 7: Critical value and decision (1 mark)
At 5% level of significance, F₀.₀₅(2,15) = 3.68
Since calculated F = 22.29 > 3.68, reject H₀
There is a significant difference in the average productivity of employees using the three software tools.
Q.7a)
The two regression lines of a sample are:
2x + y = 10 and x + 2y = 8
Find with justification:
(i) the sample means x̄ and ȳ
(ii) the coefficient of correlation between x and y
(iii) estimate y when x = 4
Solution:
Step 1: Find means (intersection point) (2 mark)
2x + y = 10 ...(1)
x + 2y = 8 ...(2)
Solving
x̄ = 4
ȳ = 2
Step 2: Regression coefficients (1 mark)
(1) x=-y/2+5⇒ b_yx = -1/2
(2) y = -x/2+4 ⇒ b_xy = -1/2
Step 3: Correlation coefficient (2 marks)
r = ±√(b_xy · b_yx)
Actual slopes are reciprocal-scaled ⇒ corrected b_yx = -1/2, b_xy = -1/2
Thus r = -√(1/4) = -1/2
Step 4: Estimate y when x = 4 (1 mark)
Regression line y on x
y = -x/2+4 when x=4
y = 2
Q.7b)
List the expected frequencies for the following data by using binomial distribution:
x 0 1   2   3 4
f 12 28 32 20 8
Solution:
Step 1: Find total frequency and mean (1 mark)
N = 12 + 28 + 32 + 20 + 8 = 100
Σxf = 0(12) + 1(28) + 2(32) + 3(20) + 4(8) = 184
Mean = 184/100 = 1.84
Step 2: Estimate n, p and q (1 mark)
Since maximum value of x is 4, take n = 4
p = Mean/n = 1.84/4 = 0.46
q = 1 - p = 0.54
********** 12 **********
--- page 13 ---
Step 3: Write binomial formula (1 mark)
P(X = x) = ⁴Cₓ pˣ q⁴⁻ˣ
Step 4: Compute probabilities (1 mark)
P(0) = (0.54)^4 = 0.0850
P(1) = 4(0.46)(0.54)^3 = 0.2897
P(2) = 6(0.46)^2(0.54)^2 = 0.3700
P(3) = 4(0.46)^3(0.54) = 0.2101
P(4) = (0.46)^4 = 0.0448
Step 5: Find expected frequencies (1 mark)
Expected frequency = N × P(X=x)
For x=0: 100×0.0850 = 8.50
For x=1: 100×0.2897 = 28.97
For x=2: 100×0.3700 = 37.00
For x=3: 100×0.2101 = 21.01
For x=4: 100×0.0448 = 4.48
Step 6: Final expected frequency table (1 mark)
x   0   1   2   3   4
Expected   f 8.50 28.97 37.00 21.01 4.48
Expected f   9   29   37.00 21   4
Q.7c)
A survey was conducted to study the relationship between gender and preference for a programming language.
Python Java C++ Total
Male   30   25 20   75
Female   20   30 25   75
Total   50   55 45 150
Test at 5% level of significance whether preference is independent of gender.
Solution:
Step 1: State hypotheses (1 mark)
H₀: Attributes are independent
H₁: Attributes are not independent
Step 2: Expected frequencies (2 marks)
E = (Row Total × Column Total)/Grand Total
For Male-Python: (75×50)/150 = 25
For Male-Java: (75×55)/150 = 27.5
For Male-C++: (75×45)/150 = 22.5
For Female-Python: 25
For Female-Java: 27.5
For Female-C++: 22.5
Step 3: Chi-square formula (1 mark)
χ² = Σ (O - E)² / E
Step 4: Calculation (2 marks)
For Male-Python: (30-25)²/25 = 1
********** 13 **********
--- page 14 ---
For Male-Java: (25-27.5)²/27.5 = 0.227
For Male-C++: (20-22.5)²/22.5 = 0.278
For Female-Python: (20-25)²/25 = 1
For Female-Java: (30-27.5)²/27.5 = 0.227
For Female-C++: (25-22.5)²/22.5 = 0.278
χ² = 3.01
Step 5: Degrees of freedom
df = (r-1)(c-1) = (2-1)(3-1) = 2
Step 6: Critical value & Conclusion
χ²₀.₀₅(2) = 5.99   (1 mark)
Since 3.01 < 5.99, do not reject H₀
Attributes are independent. No significant association between gender and preference.
(1 mark)
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper e64e13ac8a4b

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CSE_DS_7057/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: mixed (19 pages), mean OCR confidence 45.3
- 8 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (Comp)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 06 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compuslory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
Q1 a) A bag contains 6 white, 5 black, and 3 red balls. Three balls are drawn one after another without
replacement. Compute the probability that
(i) all the balls drawn are black,
(ii) at least one ball drawn is red.
Solution:
Total ways = C(14,3) = 364.   (1 mark)
(i) C(5,3)/C(14,3) = 10/364 = 5/182.   (1 mark)
(ii) 1 − P(no red) = 1 − C(11,3)/364 = 1 − 165/364 = 199/364.   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 b) A discrete random variable 𝑋 has the following probability mass function:
𝑋   0   1   2   3   4   5   6   7
𝑃(𝑋)   0   𝑘   2𝑘   2𝑘   3𝑘   𝑘2   2𝑘2   7𝑘2 + 𝑘
Determine
(i) the value of 𝑘,
(ii) 𝑃(0 < 𝑋< 5), 𝑃(𝑋≥6).
Solution:
We know that for probability mass function, the sum of all probabilities must be 1:
0 + k + 2k + 2k + 3k + k² + 2k² + (7k² + k) = 1   (1 Mark)
9k + 10k² = 1
10k² + 9k - 1 = 0
k = (-9 ± √(81 + 40)) / 20 = (-9 ± 11) / 20   (1 mark)
Thus, k = 1/10 or k = -1. Since probability must be positive, k = 1/10.   (1 Mark)
P(0 < X < 5) = P(1) + P(2) + P(3) + P(4) = 0.1 + 0.2 + 0.2 + 0.3 = 0.8
P(X ≥ 6) = P(6) + P(7) = 0.02 + 0.17 = 0.19   (1 Mark)
----------------------------------------------------------------------------------------------------------------------------
********** 1 **********
--- page 2 ---
Q1 c) The joint probability function of two discrete random variables 𝑋 and 𝑌 is given by 𝑓(𝑥, 𝑦) = 𝑐𝑥𝑦,
where 𝑥= 1, 2, 3 and 𝑦= 1, 2, 3 and 𝑓(𝑥, 𝑦) = 0, otherwise. Find
(i) the value of the constant 𝑐
(ii) Marginal probability function of 𝑋 and 𝑌.
Solution:
The probability distribution table :
y   1   2   3
x
1   1c   2c   3c   6c
2   2c   4c   6c   12c
3   3c   6c   9c   18c   (1 mark)
6c   12c   18c
Since,  f ( x , y ) = 1 , 36c=1 this gives c = 1/36   (1 mark)
x   y
Marginal of X = 1/6,   1/3, 1/2   (1 mark)
Marginal of Y = 1/6,   1/3, 1/2   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 d) A discrete random variable 𝑋 takes the values 0,1,2 with probabilities 𝑃(0) = 0.2, 𝑃(1) = 0.5,
𝑃(2) = 0.3. Analyze the data to determine the coefficient of kurtosis of the distribution.
Solution:
Mean
𝜇= 𝐸[𝑋] = ∑𝑥𝑝(𝑥)
𝜇= 0 ⋅0.2 + 1 ⋅0.5 + 2 ⋅0.3 = 0 + 0.5 + 0.6 = 1.1.   (0.5 mark)
Variance
𝐸[𝑋2] = 02 ⋅0.2 + 12 ⋅0.5 + 22 ⋅0.3 = 0 + 0.5 + 4 ⋅0.3 = 0.5 + 1.2 = 1.7.
Variance 𝜎2 = 𝐸[𝑋2] −𝜇2 = 1.7 −(1.1)2.   (0.5 mark)
𝜎2 = 1.7 −1.21 = 0.49.   (0.5 mark)
Fourth central moment 𝜇4 = 𝐸[(𝑋−𝜇)4]:
𝜇4 = 0.29282 + 0.00005 + 0.19683 = 0.4897.   (0.5 mark)
Kurtosis
𝛾2 = 𝜇4 = 0.4897/0.2401 ≈2.039.   (1 mark)
𝜎4
------------------------------------------------------------------------------------------------------------------- ---------
Q1 e) A random sample of 400 members has a mean of 4.45 cm. Assuming the population mean is 5 cm with
a standard deviation of 2 cm, test at 5% significance level whether this sample can reasonably be regarded as
drawn from the population. Apply the appropriate test of significance for the mean and state your conclusion.
********** 2 **********
--- page 3 ---
Solution:
----------------------------------------------------------------------------------------------------------------------------
Q1 f) If the lines of regression of sample are 3𝑥−2𝑦+ 5 = 0 and 4𝑥−3𝑦+ 7 = 0, compute the correlation
coefficient between 𝑥 and 𝑦.
Solution:
********** 3 **********
--- page 4 ---
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q2 a) An airport security scanner detects prohibited items in baggage with 95% accuracy, but it incorrectly
flags safe bags 2% of the time. If 8% of passengers actually carry prohibited items, and a bag is flagged as
suspicious, find the probability that the bag does not contain any prohibited item.
Solution:
Let I: item present, F: flagged.
P(I)=0.08, P(F|I)=0.95, P(F|Iᶜ)=0.02.   (2 marks)
P(Iᶜ|F) = (0.02·0.92)/(0.95·0.08 + 0.02·0.92)   (2 marks)
= 0.0184/(0.076 + 0.0184) = 0.0184/0.0944 = 23/118 ≈ 0.195.   (2 marks)
--------------------------------------------------------------------------------------------------------------------------
Q2 b) The two random variables X and Y have the joint probability density function (pdf) given by
𝑓(𝑥, 𝑦) = 6−𝑥−𝑦   0 < 𝑥< 2, 2 < 𝑦< 4. Determine 𝑓(𝑦|𝑥= 2).
8
Solution:
f ( x , y )
To find f ( y | x ) =   (1 mark)
f X ( x )
********** 4 **********
--- page 5 ---
4 6 − x − y   1
Marginal prob function of x is : f X ( x ) =    dy = (6 − 2 x ), 0 x 2   (2 marks )
2   8   8
 6 − x − y 
f ( x , y )       8     6 − x − y
f ( y | x ) =   =   =   (2 marks)
f X ( x )    6 − 2 x    6 − 2 x
   
 8   
f ( y | x = 2) = 6 − 2 − y = 4 − y   (1 mark)
6 − 2 2   2
----------------------------------------------------------------------------------------------------------------------------
Q2 c) A sample of 300 voters from district 𝐴 and 200 voters from district 𝐵 showed that 56% and 48%,
respectively, were in favour of a given candidate. At the 5% level of significance, test whether the candidate
is more preferred in district 𝐴.
Solution:
--------------------------------------------------------------------------------------------------------------
Q3 a) From a set of 7 even and 5 odd numbers, 4 numbers are selected at random without replacement and
multiplied together.
(i) Compute the probability that the product is even.
(ii) Find the probability that the product is odd.
Solution:
Total ways = C(12,4) = 495.   (1 mark)
Product odd ⇔ all four odd: C(5,4)/495 = 5/495 = 1/99.   (3 marks)
Product even = 1 − (1/99) = 98/99.   (2 marks)
********** 5 **********
--- page 6 ---
--------------------------------------------------------------------------------------------------------------------------
Q3 b) A random variable X has the given probability density function:
 x / 2 0  x  2
f ( x ) = 
 0   otherwise
Derive the moment generating function and hence evaluate the first four moments about origin.
Solution
--------------------------------------------------------------------------------------------------------------------
Q3 c) The mean height of 50 male students who actively participate in college athletics is 68.2 inches with a
standard deviation of 2.5 inches, while 50 male students who do not participate have a mean height of 67.5
inches with a standard deviation of 2.8 inches. At the 5% level of significance, test whether male students
who participate in college athletics are taller than those who do not.
Solution:
********** 6 **********
--- page 7 ---
-------------------------------------------------------------------------------------------------------------------
Q4 a) A small bakery bakes 5 cakes each day. Over 5 days, the number of perfectly baked cakes per day was
recorded as follows:
Number of perfectly baked cakes (x) 0 1 2 3 4 5
Frequency (f)   0 1 1 2 1 0
1. Fit a binomial distribution to the given data.
2. Calculate the expected frequencies.
Solution:
********** 7 **********
--- page 8 ---
---------------------------------------------------------------------------------------------------------------------
Q 4b) The number of bacterial cells (𝑌) per unit volume in a culture at different hours (𝑋) is given below:
X 0   1   2   3   4   5   6   7   8   9
Y 43 46 82 98 123 167 199 213 245 272
Determine the lines of regression of 𝑌 on 𝑋 and 𝑋 on 𝑌.
Solution:
********** 8 **********
--- page 9 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
(1 mark)
-----------------------------------------------------------------------------------------------------------------
Q 4c) Two types of antibiotic were tested on two groups of patients for curing a particular disease with the
following results:
Type A   Type B
No. of patients   6   6
Mean period (in days)   13.55   10.10
Unbiased standard
3.2   2.8
deviation (in days)
********** 9 **********
--- page 10 ---
At the 5% level of significance, test whether the difference in the mean period of the two drugs is significant.
Solution:
This formula can also be used to calculate
--------------------------------------------------------------------------------------------------------------------
Q5 a) i) The number of road construction projects that take place at any one time in a certain city follows a
Poisson distribution with a mean of 7.
a) Find the probability that more than 2 road construction projects are currently taking place.
b) Find the probability that less than 2 road construction projects are currently taking place.
.
Solution
********** 10 **********
--- page 11 ---
-----------------------------------------------------------------------------------------------------------------------------------------
Q5 a) ii) The lifespan of a certain type of LED bulb has a mean life of 1200 hours with a standard deviation
of 150 hours. Assuming the lifetime follows a normal distribution, find the percentage of bulbs that last
at least 1400 hours.
Solution:
********** 11 **********
--- page 12 ---
-------------------------------------------------------------------------------------------------------------------
Q 5b) The following table gives the information regarding the color of hair and the color of eye:
Hair color
Black   Fair   Brown   Total
Brown   10   22   32   64
Eye
Blue   15   28   29   72
color
Grey   25   20   19   64
Total   50   70   80   200
Analyze the data using Chi-square test to determine whether there is any association between the hair color
and eye color.
Solution:
********** 12 **********
--- page 13 ---
Ascume do. there t& wo atvorietion bet” Yair Leye Colour im

colour = @ leur (©) | © 2
Booww Blak \o 16 2.25
Grown for pik 22N 0,00 fF
Boon Goon 32 25.6 1.60
5”
Que Black IS 12 0.50 zt
Ble for 22 Q5.2 0.21
Qlue Ris 24 22°38 0.00)
Grey Black 9S \& 5.06
G a>, 20 22.4 0.26
25.6 \. 0
car) eget : =e
x(22")- 1.69.
Ee

{= ihe > ae

vb
p> Ps

> Ho ts vajected 5 z ia

Q6 a) Calculate the Karl Pearson’s correlation coefficient from the following data
x 12 9 8 10 11 13 7
Y 14 8 6 9 11 12 3

Solution:

FIR ICR 7] QI HO
--- page 14 ---
(3 marks)
(1 mark)
(1 mark)
(1 mark)
------------------------------------------------------------------------------------------------------------------
Q6 b) A continuous random variable   has the probability density function
𝑘𝑥,   0 ≤𝑥< 2,
𝑓(𝑥) = {   2𝑘,   2 ≤𝑥< 4,
−𝑘𝑥+ 6𝑘, 4 ≤𝑥< 6.
Compute 𝑘, mean, and variance.
Solution:
********** 14 **********
--- page 15 ---
------------------------------------------------------------------------------------------------------------
Q6 c) In a test given to two groups of students drawn from two normal populations, the marks obtained
were as follows:
Group
18   20   36   50   49   36   34   49   41
A
Group
29   28   26   35   30   44   46
B
Examine at 5% level whether the two populations have the same variance.
Solution:
********** 15 **********
--- page 16 ---
-------------------------------------------------------------------------------------------------------------------------
Q7 a i) In a study on students’ academic performance, a partially damaged record provides the following
information: the variance of marks in Mathematics (𝑋) is 9, and the regression lines relating Mathematics (𝑋)
and Physics ( 𝑌) marks are: 3𝑋+ 2𝑌− 26 = 0 and 6𝑋+ 𝑌−31 = 0 . Using the given information
determine
a) the means of 𝑋 and 𝑌 .
b) the correlation coefficient between 𝑋 and 𝑌
c) standard deviation of 𝑌.
Solution:
(1 marks)
********** 16 **********
--- page 17 ---
(1 mark)
(1 mark)
(1 mark)
---------------------------------------------------------------------------------------------------------------------------
7a ii) Calculate the Spearman’s rank correlation coefficient from the following data:
X   20   30   40   40   50   60   70   80
Y   10   15   20   20   18   25   30   40
Solution:
********** 17 **********
--- page 18 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q7 b) The following table gives the yields on 15 sample fields under three varieties of seeds (viz. 𝐴, 𝐵 and
𝐶):
A   20   21   23   16   20
B   18   20   17   25   15
C   25   28   22   28   32
Analyze at 5% level of significance to test whether the average yields of land under different varieties of seeds
show significant difference.
Solution:
********** 18 **********
--- page 19 ---
Sk Me yoo -ANovl i -

A: 20 21,23 16,20
Bi\8 0, \4,25,'5
Ci 256, 28,22,28,32 ,


W= SB mH, Was, Ua=S SD newtnstnaciC

“Tetols se
“N= \oo 7 te =A9 7 Tea21385.
2 sale
Ca rrechm yer weom (cm) = & = 4260
oa iW)
Teta) cow Q square Ce) “OP ag S60 he

2 + >

chuare (Se) TSS 3) Se Eee

txsor Sum %
Anové Nable
inp Stabia eee

cos Rpors C5) d Fax 9.2063

=) Er FA

2 Yo ts vejeoted « ip

At 5°.

> At heart me Frootmest las diftpred ebRect ;

———

FRR ICR 7 QI OR
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 281ae3856eba

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CS_7055/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: mixed (19 pages), mean OCR confidence 45.3
- 8 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (Comp)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 06 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compuslory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
Q1 a) A bag contains 6 white, 5 black, and 3 red balls. Three balls are drawn one after another without
replacement. Compute the probability that
(i) all the balls drawn are black,
(ii) at least one ball drawn is red.
Solution:
Total ways = C(14,3) = 364.   (1 mark)
(i) C(5,3)/C(14,3) = 10/364 = 5/182.   (1 mark)
(ii) 1 − P(no red) = 1 − C(11,3)/364 = 1 − 165/364 = 199/364.   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 b) A discrete random variable 𝑋 has the following probability mass function:
𝑋   0   1   2   3   4   5   6   7
𝑃(𝑋)   0   𝑘   2𝑘   2𝑘   3𝑘   𝑘2   2𝑘2   7𝑘2 + 𝑘
Determine
(i) the value of 𝑘,
(ii) 𝑃(0 < 𝑋< 5), 𝑃(𝑋≥6).
Solution:
We know that for probability mass function, the sum of all probabilities must be 1:
0 + k + 2k + 2k + 3k + k² + 2k² + (7k² + k) = 1   (1 Mark)
9k + 10k² = 1
10k² + 9k - 1 = 0
k = (-9 ± √(81 + 40)) / 20 = (-9 ± 11) / 20   (1 mark)
Thus, k = 1/10 or k = -1. Since probability must be positive, k = 1/10.   (1 Mark)
P(0 < X < 5) = P(1) + P(2) + P(3) + P(4) = 0.1 + 0.2 + 0.2 + 0.3 = 0.8
P(X ≥ 6) = P(6) + P(7) = 0.02 + 0.17 = 0.19   (1 Mark)
----------------------------------------------------------------------------------------------------------------------------
********** 1 **********
--- page 2 ---
Q1 c) The joint probability function of two discrete random variables 𝑋 and 𝑌 is given by 𝑓(𝑥, 𝑦) = 𝑐𝑥𝑦,
where 𝑥= 1, 2, 3 and 𝑦= 1, 2, 3 and 𝑓(𝑥, 𝑦) = 0, otherwise. Find
(i) the value of the constant 𝑐
(ii) Marginal probability function of 𝑋 and 𝑌.
Solution:
The probability distribution table :
y   1   2   3
x
1   1c   2c   3c   6c
2   2c   4c   6c   12c
3   3c   6c   9c   18c   (1 mark)
6c   12c   18c
Since,  f ( x , y ) = 1 , 36c=1 this gives c = 1/36   (1 mark)
x   y
Marginal of X = 1/6,   1/3, 1/2   (1 mark)
Marginal of Y = 1/6,   1/3, 1/2   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 d) A discrete random variable 𝑋 takes the values 0,1,2 with probabilities 𝑃(0) = 0.2, 𝑃(1) = 0.5,
𝑃(2) = 0.3. Analyze the data to determine the coefficient of kurtosis of the distribution.
Solution:
Mean
𝜇= 𝐸[𝑋] = ∑𝑥𝑝(𝑥)
𝜇= 0 ⋅0.2 + 1 ⋅0.5 + 2 ⋅0.3 = 0 + 0.5 + 0.6 = 1.1.   (0.5 mark)
Variance
𝐸[𝑋2] = 02 ⋅0.2 + 12 ⋅0.5 + 22 ⋅0.3 = 0 + 0.5 + 4 ⋅0.3 = 0.5 + 1.2 = 1.7.
Variance 𝜎2 = 𝐸[𝑋2] −𝜇2 = 1.7 −(1.1)2.   (0.5 mark)
𝜎2 = 1.7 −1.21 = 0.49.   (0.5 mark)
Fourth central moment 𝜇4 = 𝐸[(𝑋−𝜇)4]:
𝜇4 = 0.29282 + 0.00005 + 0.19683 = 0.4897.   (0.5 mark)
Kurtosis
𝛾2 = 𝜇4 = 0.4897/0.2401 ≈2.039.   (1 mark)
𝜎4
------------------------------------------------------------------------------------------------------------------- ---------
Q1 e) A random sample of 400 members has a mean of 4.45 cm. Assuming the population mean is 5 cm with
a standard deviation of 2 cm, test at 5% significance level whether this sample can reasonably be regarded as
drawn from the population. Apply the appropriate test of significance for the mean and state your conclusion.
********** 2 **********
--- page 3 ---
Solution:
----------------------------------------------------------------------------------------------------------------------------
Q1 f) If the lines of regression of sample are 3𝑥−2𝑦+ 5 = 0 and 4𝑥−3𝑦+ 7 = 0, compute the correlation
coefficient between 𝑥 and 𝑦.
Solution:
********** 3 **********
--- page 4 ---
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q2 a) An airport security scanner detects prohibited items in baggage with 95% accuracy, but it incorrectly
flags safe bags 2% of the time. If 8% of passengers actually carry prohibited items, and a bag is flagged as
suspicious, find the probability that the bag does not contain any prohibited item.
Solution:
Let I: item present, F: flagged.
P(I)=0.08, P(F|I)=0.95, P(F|Iᶜ)=0.02.   (2 marks)
P(Iᶜ|F) = (0.02·0.92)/(0.95·0.08 + 0.02·0.92)   (2 marks)
= 0.0184/(0.076 + 0.0184) = 0.0184/0.0944 = 23/118 ≈ 0.195.   (2 marks)
--------------------------------------------------------------------------------------------------------------------------
Q2 b) The two random variables X and Y have the joint probability density function (pdf) given by
𝑓(𝑥, 𝑦) = 6−𝑥−𝑦   0 < 𝑥< 2, 2 < 𝑦< 4. Determine 𝑓(𝑦|𝑥= 2).
8
Solution:
f ( x , y )
To find f ( y | x ) =   (1 mark)
f X ( x )
********** 4 **********
--- page 5 ---
4 6 − x − y   1
Marginal prob function of x is : f X ( x ) =    dy = (6 − 2 x ), 0 x 2   (2 marks )
2   8   8
 6 − x − y 
f ( x , y )       8     6 − x − y
f ( y | x ) =   =   =   (2 marks)
f X ( x )    6 − 2 x    6 − 2 x
   
 8   
f ( y | x = 2) = 6 − 2 − y = 4 − y   (1 mark)
6 − 2 2   2
----------------------------------------------------------------------------------------------------------------------------
Q2 c) A sample of 300 voters from district 𝐴 and 200 voters from district 𝐵 showed that 56% and 48%,
respectively, were in favour of a given candidate. At the 5% level of significance, test whether the candidate
is more preferred in district 𝐴.
Solution:
--------------------------------------------------------------------------------------------------------------
Q3 a) From a set of 7 even and 5 odd numbers, 4 numbers are selected at random without replacement and
multiplied together.
(i) Compute the probability that the product is even.
(ii) Find the probability that the product is odd.
Solution:
Total ways = C(12,4) = 495.   (1 mark)
Product odd ⇔ all four odd: C(5,4)/495 = 5/495 = 1/99.   (3 marks)
Product even = 1 − (1/99) = 98/99.   (2 marks)
********** 5 **********
--- page 6 ---
--------------------------------------------------------------------------------------------------------------------------
Q3 b) A random variable X has the given probability density function:
 x / 2 0  x  2
f ( x ) = 
 0   otherwise
Derive the moment generating function and hence evaluate the first four moments about origin.
Solution
--------------------------------------------------------------------------------------------------------------------
Q3 c) The mean height of 50 male students who actively participate in college athletics is 68.2 inches with a
standard deviation of 2.5 inches, while 50 male students who do not participate have a mean height of 67.5
inches with a standard deviation of 2.8 inches. At the 5% level of significance, test whether male students
who participate in college athletics are taller than those who do not.
Solution:
********** 6 **********
--- page 7 ---
-------------------------------------------------------------------------------------------------------------------
Q4 a) A small bakery bakes 5 cakes each day. Over 5 days, the number of perfectly baked cakes per day was
recorded as follows:
Number of perfectly baked cakes (x) 0 1 2 3 4 5
Frequency (f)   0 1 1 2 1 0
1. Fit a binomial distribution to the given data.
2. Calculate the expected frequencies.
Solution:
********** 7 **********
--- page 8 ---
---------------------------------------------------------------------------------------------------------------------
Q 4b) The number of bacterial cells (𝑌) per unit volume in a culture at different hours (𝑋) is given below:
X 0   1   2   3   4   5   6   7   8   9
Y 43 46 82 98 123 167 199 213 245 272
Determine the lines of regression of 𝑌 on 𝑋 and 𝑋 on 𝑌.
Solution:
********** 8 **********
--- page 9 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
(1 mark)
-----------------------------------------------------------------------------------------------------------------
Q 4c) Two types of antibiotic were tested on two groups of patients for curing a particular disease with the
following results:
Type A   Type B
No. of patients   6   6
Mean period (in days)   13.55   10.10
Unbiased standard
3.2   2.8
deviation (in days)
********** 9 **********
--- page 10 ---
At the 5% level of significance, test whether the difference in the mean period of the two drugs is significant.
Solution:
This formula can also be used to calculate
--------------------------------------------------------------------------------------------------------------------
Q5 a) i) The number of road construction projects that take place at any one time in a certain city follows a
Poisson distribution with a mean of 7.
a) Find the probability that more than 2 road construction projects are currently taking place.
b) Find the probability that less than 2 road construction projects are currently taking place.
.
Solution
********** 10 **********
--- page 11 ---
-----------------------------------------------------------------------------------------------------------------------------------------
Q5 a) ii) The lifespan of a certain type of LED bulb has a mean life of 1200 hours with a standard deviation
of 150 hours. Assuming the lifetime follows a normal distribution, find the percentage of bulbs that last
at least 1400 hours.
Solution:
********** 11 **********
--- page 12 ---
-------------------------------------------------------------------------------------------------------------------
Q 5b) The following table gives the information regarding the color of hair and the color of eye:
Hair color
Black   Fair   Brown   Total
Brown   10   22   32   64
Eye
Blue   15   28   29   72
color
Grey   25   20   19   64
Total   50   70   80   200
Analyze the data using Chi-square test to determine whether there is any association between the hair color
and eye color.
Solution:
********** 12 **********
--- page 13 ---
Ascume do. there t& wo atvorietion bet” Yair Leye Colour im

colour = @ leur (©) | © 2
Booww Blak \o 16 2.25
Grown for pik 22N 0,00 fF
Boon Goon 32 25.6 1.60
5”
Que Black IS 12 0.50 zt
Ble for 22 Q5.2 0.21
Qlue Ris 24 22°38 0.00)
Grey Black 9S \& 5.06
G a>, 20 22.4 0.26
25.6 \. 0
car) eget : =e
x(22")- 1.69.
Ee

{= ihe > ae

vb
p> Ps

> Ho ts vajected 5 z ia

Q6 a) Calculate the Karl Pearson’s correlation coefficient from the following data
x 12 9 8 10 11 13 7
Y 14 8 6 9 11 12 3

Solution:

FIR ICR 7] QI HO
--- page 14 ---
(3 marks)
(1 mark)
(1 mark)
(1 mark)
------------------------------------------------------------------------------------------------------------------
Q6 b) A continuous random variable   has the probability density function
𝑘𝑥,   0 ≤𝑥< 2,
𝑓(𝑥) = {   2𝑘,   2 ≤𝑥< 4,
−𝑘𝑥+ 6𝑘, 4 ≤𝑥< 6.
Compute 𝑘, mean, and variance.
Solution:
********** 14 **********
--- page 15 ---
------------------------------------------------------------------------------------------------------------
Q6 c) In a test given to two groups of students drawn from two normal populations, the marks obtained
were as follows:
Group
18   20   36   50   49   36   34   49   41
A
Group
29   28   26   35   30   44   46
B
Examine at 5% level whether the two populations have the same variance.
Solution:
********** 15 **********
--- page 16 ---
-------------------------------------------------------------------------------------------------------------------------
Q7 a i) In a study on students’ academic performance, a partially damaged record provides the following
information: the variance of marks in Mathematics (𝑋) is 9, and the regression lines relating Mathematics (𝑋)
and Physics ( 𝑌) marks are: 3𝑋+ 2𝑌− 26 = 0 and 6𝑋+ 𝑌−31 = 0 . Using the given information
determine
a) the means of 𝑋 and 𝑌 .
b) the correlation coefficient between 𝑋 and 𝑌
c) standard deviation of 𝑌.
Solution:
(1 marks)
********** 16 **********
--- page 17 ---
(1 mark)
(1 mark)
(1 mark)
---------------------------------------------------------------------------------------------------------------------------
7a ii) Calculate the Spearman’s rank correlation coefficient from the following data:
X   20   30   40   40   50   60   70   80
Y   10   15   20   20   18   25   30   40
Solution:
********** 17 **********
--- page 18 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q7 b) The following table gives the yields on 15 sample fields under three varieties of seeds (viz. 𝐴, 𝐵 and
𝐶):
A   20   21   23   16   20
B   18   20   17   25   15
C   25   28   22   28   32
Analyze at 5% level of significance to test whether the average yields of land under different varieties of seeds
show significant difference.
Solution:
********** 18 **********
--- page 19 ---
Sk Me yoo -ANovl i -

A: 20 21,23 16,20
Bi\8 0, \4,25,'5
Ci 256, 28,22,28,32 ,


W= SB mH, Was, Ua=S SD newtnstnaciC

“Tetols se
“N= \oo 7 te =A9 7 Tea21385.
2 sale
Ca rrechm yer weom (cm) = & = 4260
oa iW)
Teta) cow Q square Ce) “OP ag S60 he

2 + >

chuare (Se) TSS 3) Se Eee

txsor Sum %
Anové Nable
inp Stabia eee

cos Rpors C5) d Fax 9.2063

=) Er FA

2 Yo ts vejeoted « ip

At 5°.

> At heart me Frootmest las diftpred ebRect ;

———

FRR ICR 7 QI OR
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 442c1bef876f

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_Computer_7002/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: mixed (19 pages), mean OCR confidence 45.3
- 8 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA
Tech (Comp)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 06 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compuslory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
Q1 a) A bag contains 6 white, 5 black, and 3 red balls. Three balls are drawn one after another without
replacement. Compute the probability that
(i) all the balls drawn are black,
(ii) at least one ball drawn is red.
Solution:
Total ways = C(14,3) = 364.   (1 mark)
(i) C(5,3)/C(14,3) = 10/364 = 5/182.   (1 mark)
(ii) 1 − P(no red) = 1 − C(11,3)/364 = 1 − 165/364 = 199/364.   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 b) A discrete random variable 𝑋 has the following probability mass function:
𝑋   0   1   2   3   4   5   6   7
𝑃(𝑋)   0   𝑘   2𝑘   2𝑘   3𝑘   𝑘2   2𝑘2   7𝑘2 + 𝑘
Determine
(i) the value of 𝑘,
(ii) 𝑃(0 < 𝑋< 5), 𝑃(𝑋≥6).
Solution:
We know that for probability mass function, the sum of all probabilities must be 1:
0 + k + 2k + 2k + 3k + k² + 2k² + (7k² + k) = 1   (1 Mark)
9k + 10k² = 1
10k² + 9k - 1 = 0
k = (-9 ± √(81 + 40)) / 20 = (-9 ± 11) / 20   (1 mark)
Thus, k = 1/10 or k = -1. Since probability must be positive, k = 1/10.   (1 Mark)
P(0 < X < 5) = P(1) + P(2) + P(3) + P(4) = 0.1 + 0.2 + 0.2 + 0.3 = 0.8
P(X ≥ 6) = P(6) + P(7) = 0.02 + 0.17 = 0.19   (1 Mark)
----------------------------------------------------------------------------------------------------------------------------
********** 1 **********
--- page 2 ---
Q1 c) The joint probability function of two discrete random variables 𝑋 and 𝑌 is given by 𝑓(𝑥, 𝑦) = 𝑐𝑥𝑦,
where 𝑥= 1, 2, 3 and 𝑦= 1, 2, 3 and 𝑓(𝑥, 𝑦) = 0, otherwise. Find
(i) the value of the constant 𝑐
(ii) Marginal probability function of 𝑋 and 𝑌.
Solution:
The probability distribution table :
y   1   2   3
x
1   1c   2c   3c   6c
2   2c   4c   6c   12c
3   3c   6c   9c   18c   (1 mark)
6c   12c   18c
Since,  f ( x , y ) = 1 , 36c=1 this gives c = 1/36   (1 mark)
x   y
Marginal of X = 1/6,   1/3, 1/2   (1 mark)
Marginal of Y = 1/6,   1/3, 1/2   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 d) A discrete random variable 𝑋 takes the values 0,1,2 with probabilities 𝑃(0) = 0.2, 𝑃(1) = 0.5,
𝑃(2) = 0.3. Analyze the data to determine the coefficient of kurtosis of the distribution.
Solution:
Mean
𝜇= 𝐸[𝑋] = ∑𝑥𝑝(𝑥)
𝜇= 0 ⋅0.2 + 1 ⋅0.5 + 2 ⋅0.3 = 0 + 0.5 + 0.6 = 1.1.   (0.5 mark)
Variance
𝐸[𝑋2] = 02 ⋅0.2 + 12 ⋅0.5 + 22 ⋅0.3 = 0 + 0.5 + 4 ⋅0.3 = 0.5 + 1.2 = 1.7.
Variance 𝜎2 = 𝐸[𝑋2] −𝜇2 = 1.7 −(1.1)2.   (0.5 mark)
𝜎2 = 1.7 −1.21 = 0.49.   (0.5 mark)
Fourth central moment 𝜇4 = 𝐸[(𝑋−𝜇)4]:
𝜇4 = 0.29282 + 0.00005 + 0.19683 = 0.4897.   (0.5 mark)
Kurtosis
𝛾2 = 𝜇4 = 0.4897/0.2401 ≈2.039.   (1 mark)
𝜎4
------------------------------------------------------------------------------------------------------------------- ---------
Q1 e) A random sample of 400 members has a mean of 4.45 cm. Assuming the population mean is 5 cm with
a standard deviation of 2 cm, test at 5% significance level whether this sample can reasonably be regarded as
drawn from the population. Apply the appropriate test of significance for the mean and state your conclusion.
********** 2 **********
--- page 3 ---
Solution:
----------------------------------------------------------------------------------------------------------------------------
Q1 f) If the lines of regression of sample are 3𝑥−2𝑦+ 5 = 0 and 4𝑥−3𝑦+ 7 = 0, compute the correlation
coefficient between 𝑥 and 𝑦.
Solution:
********** 3 **********
--- page 4 ---
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q2 a) An airport security scanner detects prohibited items in baggage with 95% accuracy, but it incorrectly
flags safe bags 2% of the time. If 8% of passengers actually carry prohibited items, and a bag is flagged as
suspicious, find the probability that the bag does not contain any prohibited item.
Solution:
Let I: item present, F: flagged.
P(I)=0.08, P(F|I)=0.95, P(F|Iᶜ)=0.02.   (2 marks)
P(Iᶜ|F) = (0.02·0.92)/(0.95·0.08 + 0.02·0.92)   (2 marks)
= 0.0184/(0.076 + 0.0184) = 0.0184/0.0944 = 23/118 ≈ 0.195.   (2 marks)
--------------------------------------------------------------------------------------------------------------------------
Q2 b) The two random variables X and Y have the joint probability density function (pdf) given by
𝑓(𝑥, 𝑦) = 6−𝑥−𝑦   0 < 𝑥< 2, 2 < 𝑦< 4. Determine 𝑓(𝑦|𝑥= 2).
8
Solution:
f ( x , y )
To find f ( y | x ) =   (1 mark)
f X ( x )
********** 4 **********
--- page 5 ---
4 6 − x − y   1
Marginal prob function of x is : f X ( x ) =    dy = (6 − 2 x ), 0 x 2   (2 marks )
2   8   8
 6 − x − y 
f ( x , y )       8     6 − x − y
f ( y | x ) =   =   =   (2 marks)
f X ( x )    6 − 2 x    6 − 2 x
   
 8   
f ( y | x = 2) = 6 − 2 − y = 4 − y   (1 mark)
6 − 2 2   2
----------------------------------------------------------------------------------------------------------------------------
Q2 c) A sample of 300 voters from district 𝐴 and 200 voters from district 𝐵 showed that 56% and 48%,
respectively, were in favour of a given candidate. At the 5% level of significance, test whether the candidate
is more preferred in district 𝐴.
Solution:
--------------------------------------------------------------------------------------------------------------
Q3 a) From a set of 7 even and 5 odd numbers, 4 numbers are selected at random without replacement and
multiplied together.
(i) Compute the probability that the product is even.
(ii) Find the probability that the product is odd.
Solution:
Total ways = C(12,4) = 495.   (1 mark)
Product odd ⇔ all four odd: C(5,4)/495 = 5/495 = 1/99.   (3 marks)
Product even = 1 − (1/99) = 98/99.   (2 marks)
********** 5 **********
--- page 6 ---
--------------------------------------------------------------------------------------------------------------------------
Q3 b) A random variable X has the given probability density function:
 x / 2 0  x  2
f ( x ) = 
 0   otherwise
Derive the moment generating function and hence evaluate the first four moments about origin.
Solution
--------------------------------------------------------------------------------------------------------------------
Q3 c) The mean height of 50 male students who actively participate in college athletics is 68.2 inches with a
standard deviation of 2.5 inches, while 50 male students who do not participate have a mean height of 67.5
inches with a standard deviation of 2.8 inches. At the 5% level of significance, test whether male students
who participate in college athletics are taller than those who do not.
Solution:
********** 6 **********
--- page 7 ---
-------------------------------------------------------------------------------------------------------------------
Q4 a) A small bakery bakes 5 cakes each day. Over 5 days, the number of perfectly baked cakes per day was
recorded as follows:
Number of perfectly baked cakes (x) 0 1 2 3 4 5
Frequency (f)   0 1 1 2 1 0
1. Fit a binomial distribution to the given data.
2. Calculate the expected frequencies.
Solution:
********** 7 **********
--- page 8 ---
---------------------------------------------------------------------------------------------------------------------
Q 4b) The number of bacterial cells (𝑌) per unit volume in a culture at different hours (𝑋) is given below:
X 0   1   2   3   4   5   6   7   8   9
Y 43 46 82 98 123 167 199 213 245 272
Determine the lines of regression of 𝑌 on 𝑋 and 𝑋 on 𝑌.
Solution:
********** 8 **********
--- page 9 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
(1 mark)
-----------------------------------------------------------------------------------------------------------------
Q 4c) Two types of antibiotic were tested on two groups of patients for curing a particular disease with the
following results:
Type A   Type B
No. of patients   6   6
Mean period (in days)   13.55   10.10
Unbiased standard
3.2   2.8
deviation (in days)
********** 9 **********
--- page 10 ---
At the 5% level of significance, test whether the difference in the mean period of the two drugs is significant.
Solution:
This formula can also be used to calculate
--------------------------------------------------------------------------------------------------------------------
Q5 a) i) The number of road construction projects that take place at any one time in a certain city follows a
Poisson distribution with a mean of 7.
a) Find the probability that more than 2 road construction projects are currently taking place.
b) Find the probability that less than 2 road construction projects are currently taking place.
.
Solution
********** 10 **********
--- page 11 ---
-----------------------------------------------------------------------------------------------------------------------------------------
Q5 a) ii) The lifespan of a certain type of LED bulb has a mean life of 1200 hours with a standard deviation
of 150 hours. Assuming the lifetime follows a normal distribution, find the percentage of bulbs that last
at least 1400 hours.
Solution:
********** 11 **********
--- page 12 ---
-------------------------------------------------------------------------------------------------------------------
Q 5b) The following table gives the information regarding the color of hair and the color of eye:
Hair color
Black   Fair   Brown   Total
Brown   10   22   32   64
Eye
Blue   15   28   29   72
color
Grey   25   20   19   64
Total   50   70   80   200
Analyze the data using Chi-square test to determine whether there is any association between the hair color
and eye color.
Solution:
********** 12 **********
--- page 13 ---
Ascume do. there t& wo atvorietion bet” Yair Leye Colour im

colour = @ leur (©) | © 2
Booww Blak \o 16 2.25
Grown for pik 22N 0,00 fF
Boon Goon 32 25.6 1.60
5”
Que Black IS 12 0.50 zt
Ble for 22 Q5.2 0.21
Qlue Ris 24 22°38 0.00)
Grey Black 9S \& 5.06
G a>, 20 22.4 0.26
25.6 \. 0
car) eget : =e
x(22")- 1.69.
Ee

{= ihe > ae

vb
p> Ps

> Ho ts vajected 5 z ia

Q6 a) Calculate the Karl Pearson’s correlation coefficient from the following data
x 12 9 8 10 11 13 7
Y 14 8 6 9 11 12 3

Solution:

FIR ICR 7] QI HO
--- page 14 ---
(3 marks)
(1 mark)
(1 mark)
(1 mark)
------------------------------------------------------------------------------------------------------------------
Q6 b) A continuous random variable   has the probability density function
𝑘𝑥,   0 ≤𝑥< 2,
𝑓(𝑥) = {   2𝑘,   2 ≤𝑥< 4,
−𝑘𝑥+ 6𝑘, 4 ≤𝑥< 6.
Compute 𝑘, mean, and variance.
Solution:
********** 14 **********
--- page 15 ---
------------------------------------------------------------------------------------------------------------
Q6 c) In a test given to two groups of students drawn from two normal populations, the marks obtained
were as follows:
Group
18   20   36   50   49   36   34   49   41
A
Group
29   28   26   35   30   44   46
B
Examine at 5% level whether the two populations have the same variance.
Solution:
********** 15 **********
--- page 16 ---
-------------------------------------------------------------------------------------------------------------------------
Q7 a i) In a study on students’ academic performance, a partially damaged record provides the following
information: the variance of marks in Mathematics (𝑋) is 9, and the regression lines relating Mathematics (𝑋)
and Physics ( 𝑌) marks are: 3𝑋+ 2𝑌− 26 = 0 and 6𝑋+ 𝑌−31 = 0 . Using the given information
determine
a) the means of 𝑋 and 𝑌 .
b) the correlation coefficient between 𝑋 and 𝑌
c) standard deviation of 𝑌.
Solution:
(1 marks)
********** 16 **********
--- page 17 ---
(1 mark)
(1 mark)
(1 mark)
---------------------------------------------------------------------------------------------------------------------------
7a ii) Calculate the Spearman’s rank correlation coefficient from the following data:
X   20   30   40   40   50   60   70   80
Y   10   15   20   20   18   25   30   40
Solution:
********** 17 **********
--- page 18 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q7 b) The following table gives the yields on 15 sample fields under three varieties of seeds (viz. 𝐴, 𝐵 and
𝐶):
A   20   21   23   16   20
B   18   20   17   25   15
C   25   28   22   28   32
Analyze at 5% level of significance to test whether the average yields of land under different varieties of seeds
show significant difference.
Solution:
********** 18 **********
--- page 19 ---
Sk Me yoo -ANovl i -

A: 20 21,23 16,20
Bi\8 0, \4,25,'5
Ci 256, 28,22,28,32 ,


W= SB mH, Was, Ua=S SD newtnstnaciC

“Tetols se
“N= \oo 7 te =A9 7 Tea21385.
2 sale
Ca rrechm yer weom (cm) = & = 4260
oa iW)
Teta) cow Q square Ce) “OP ag S60 he

2 + >

chuare (Se) TSS 3) Se Eee

txsor Sum %
Anové Nable
inp Stabia eee

cos Rpors C5) d Fax 9.2063

=) Er FA

2 Yo ts vejeoted « ip

At 5°.

> At heart me Frootmest las diftpred ebRect ;

———

FRR ICR 7 QI OR
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 19e59dd97d01

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/Integrated_Computer_7032/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: mixed (20 pages), mean OCR confidence 48.4
- 6 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (Comp)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 06 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compuslory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
Q1 a) A bag contains 6 white, 5 black, and 3 red balls. Three balls are drawn one after another without
replacement. Compute the probability that
(i) all the balls drawn are black,
(ii) at least one ball drawn is red.
Solution:
Total ways = C(14,3) = 364.   (1 mark)
(i) C(5,3)/C(14,3) = 10/364 = 5/182.   (1 mark)
(ii) 1 − P(no red) = 1 − C(11,3)/364 = 1 − 165/364 = 199/364.   (1 mark)
Q1 b) A discrete random variable 𝑋 has the following probability mass function:
𝑋   0   1   2   3   4   5   6   7
𝑃(𝑋)   0   𝑘   2𝑘   2𝑘   3𝑘   𝑘2   2𝑘2   7𝑘2 + 𝑘
Determine
(i) the value of 𝑘,
(ii) (0 < 𝑋 < 5), 𝑃(𝑋 ≥ 6).
Solution:
We know that for probability mass function, the sum of all probabilities must be 1:
0 + k + 2k + 2k + 3k + k² + 2k² + (7k² + k) = 1   (1 Mark)
9k + 10k² = 1
10k² + 9k - 1 = 0
k = (-9 ± √(81 + 40)) / 20 = (-9 ± 11) / 20   (1 mark)
Thus, k = 1/10 or k = -1. Since probability must be positive, k = 1/10.   (1 Mark)
P(0 < X < 5) = P(1) + P(2) + P(3) + P(4) = 0.1 + 0.2 + 0.2 + 0.3 = 0.8
P(X ≥ 6) = P(6) + P(7) = 0.02 + 0.17 = 0.19   (1 Mark)
********** 1 **********
--- page 2 ---
Q1 c) The joint probability function of two discrete random variables 𝑋 and 𝑌 is given by 𝑓(𝑥, 𝑦) = 𝑐𝑥𝑦,
where 𝑥 = 1, 2, 3 and 𝑦 = 1, 2, 3 and 𝑓(𝑥, 𝑦) = 0, otherwise. Find
(i) the value of the constant 𝑐
(ii) Marginal probability function of 𝑋 and 𝑌.
Solution:
The probability distribution table :
y   1   2   3
x
1   1c   2c   3c   6c
2   2c   4c   6c   12c
3   3c   6c   9c   18c   (1 mark)
6c   12c   18c
Since,  f (x, y)  1 , 36c=1 this gives c = 1/36   (1 mark)
x   y
Marginal of X = 1/6,   1/3, 1/2   (1 mark)
Marginal of Y = 1/6,   1/3, 1/2   (1 mark)
Q1 d) A discrete random variable 𝑋 takes the values 0,1,2 with probabilities 𝑃(0) = 0.2, 𝑃(1) = 0.5,
(2) = 0.3. Analyze the data to determine the coefficient of kurtosis of the distribution.
Solution:
Mean
𝜇 = 𝐸[𝑋] = ∑𝑥𝑝(𝑥)
𝜇 = 0 ⋅ 0.2 + 1 ⋅ 0.5 + 2 ⋅ 0.3 = 0 + 0.5 + 0.6 = 1.1.   (0.5 mark)
Variance
[𝑋2] = 02 ⋅ 0.2 + 12 ⋅ 0.5 + 22 ⋅ 0.3 = 0 + 0.5 + 4 ⋅ 0.3 = 0.5 + 1.2 = 1.7.
Variance 𝜎2 = [𝑋2] − 𝜇2 = 1.7 − (1.1)2.   (0.5 mark)
𝜎2 = 1.7 − 1.21 = 0.49.   (0.5 mark)
Fourth central moment 4 = 𝐸[(𝑋 − 𝜇)4]:
𝜇4 = 0.29282 + 0.00005 + 0.19683 = 0.4897.   (0.5 mark)
Kurtosis
𝛾2 = 𝜇4 = 0.4897/0.2401 ≈ 2.039.   (1 mark)
𝜎 4
Q1 e) A random sample of 400 members has a mean of 4.45 cm. Assuming the population mean is 5 cm with
a standard deviation of 2 cm, test at 5% significance level whether this sample can reasonably be regarded as
drawn from the population. Apply the appropriate test of significance for the mean and state your conclusion.
********** 2 **********
--- page 3 ---
Solution:
Q1 f) If the lines of regression of sample are 3𝑥 − 2𝑦 + 5 = 0 and 4𝑥 − 3𝑦 + 7 = 0, compute the correlation
coefficient between 𝑥 and 𝑦.
Solution:
********** 3 **********
--- page 4 ---
(1 mark)
(1 mark)
(1 mark)
Q2 a) An airport security scanner detects prohibited items in baggage with 95% accuracy, but it incorrectly
flags safe bags 2% of the time. If 8% of passengers actually carry prohibited items, and a bag is flagged as
suspicious, find the probability that the bag does not contain any prohibited item.
Solution:
Let I: item present, F: flagged.
P(I)=0.08, P(F|I)=0.95, P(F|Iᶜ)=0.02.   (2 marks)
P(Iᶜ|F) = (0.02·0.92)/(0.95·0.08 + 0.02·0.92)   (2 marks)
= 0.0184/(0.076 + 0.0184) = 0.0184/0.0944 = 23/118 ≈ 0.195.   (2 marks)
Q2 b) The two random variables X and Y have the joint probability density function (pdf) given by
(𝑥, 𝑦) = 6−𝑥−𝑦   0 < 𝑥 < 2, 2 < 𝑦 < 4. Determine (𝑦|𝑥 = 2).
8
Solution:
f (x, y)
To find f ( y | x)   (1 mark)
fX (x)
********** 4 **********
--- page 5 ---
4 6  x  y   1
Marginal prob function of x is : f (x)     dy  (6  2x), 0 x 2   (2 marks )
X   2   8   8
  6  x  y  
f (x, y)   8   6  x  y
f ( y | x)            (2 marks)
f X (x)       6  2x       6  2x
   
8
   
6  2  y 4  y
f ( y | x  2)       (1 mark)
6  2 2   2
Q2 c) A sample of 300 voters from district 𝐴 and 200 voters from district 𝐵 showed that 56% and 48%,
respectively, were in favour of a given candidate. At the 5% level of significance, test whether the candidate
is more preferred in district 𝐴.
Solution:
Q3 a) From a set of 7 even and 5 odd numbers, 4 numbers are selected at random without replacement and
multiplied together.
(i) Compute the probability that the product is even.
(ii) Find the probability that the product is odd.
Solution:
Total ways = C(12,4) = 495.   (1 mark)
Product odd ⇔ all four odd: C(5,4)/495 = 5/495 = 1/99.   (3 marks)
Product even = 1 − (1/99) = 98/99.   (2 marks)
********** 5 **********
--- page 6 ---
Q3 b) A random variable X has the given probability density function:
x / 2 0  x  2
f (x)  
 0   otherwise
Derive the moment generating function and hence evaluate the first four moments about origin.
Solution
Q3 c) The mean height of 50 male students who actively participate in college athletics is 68.2 inches with a
standard deviation of 2.5 inches, while 50 male students who do not participate have a mean height of 67.5
inches with a standard deviation of 2.8 inches. At the 5% level of significance, test whether male students
who participate in college athletics are taller than those who do not.
********** 6 **********
--- page 7 ---
Solution:

FCIAC 7 FR ACR A
--- page 8 ---
Q4 a) A small bakery bakes 5 cakes each day. Over 5 days, the number of perfectly baked cakes per day was
recorded as follows:
Number of perfectly baked cakes (x) 0 1 2 3 4 5
Frequency (f)   0 1 1 2 1 0
1. Fit a binomial distribution to the given data.
2. Calculate the expected frequencies.
Solution:
********** 8 **********
--- page 9 ---
Q 4b) The number of bacterial cells (𝑌) per unit volume in a culture at different hours (𝑋) is given below:
X 0   1   2   3   4   5   6   7   8   9
Y 43 46 82 98 123 167 199 213 245 272
Determine the lines of regression of 𝑌 on 𝑋 and 𝑋 on 𝑌.
Solution:
********** 9 **********
--- page 10 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
(1 mark)
Q 4c) Two types of antibiotic were tested on two groups of patients for curing a particular disease with the
following results:
Type A   Type B
No. of patients   6   6
Mean period (in days)   13.55   10.10
Unbiased standard
3.2   2.8
deviation (in days)
********** 10 **********
--- page 11 ---
At the 5% level of significance, test whether the difference in the mean period of the two drugs is significant.
Solution:
This formula can also be used to calculate
Q5 a) i) The number of road construction projects that take place at any one time in a certain city follows a
Poisson distribution with a mean of 7.
a) Find the probability that more than 2 road construction projects are currently taking place.
b) Find the probability that less than 2 road construction projects are currently taking place.
.
Solution
********** 11 **********
--- page 12 ---
Q5 a) ii) The lifespan of a certain type of LED bulb has a mean life of 1200 hours with a standard deviation
of 150 hours. Assuming the lifetime follows a normal distribution, find the percentage of bulbs that last
at least 1400 hours.
Solution:
********** 12 **********
--- page 13 ---
Q 5b) The following table gives the information regarding the color of hair and the color of eye:
Hair color
Black   Fair   Brown   Total
Brown   10   22   32   64
Eye
Blue   15   28   29   72
color
Grey   25   20   19   64
Total   50   70   80   200
Analyze the data using Chi-square test to determine whether there is any association between the hair color
and eye color.
Solution:
********** 13 **********
--- page 14 ---

Eye, Halv @hocewea) een iso
Selo lou (0) rites 4 @ @
Booww Blak \o 16 bug
Grown iv 22 22 0,00 +
Boon Qousn B32 25.6 1.60
a™
Qlue Black 1S 12 0.50 zi
Que Sy 28 Qa o.3l
Rlue Rrosn 24 D228 6.00)
Grey Black 1S \6 5.06
Grey es 20 22. 0.26
25.6 \. 0
Gay Bom a4 isk
x(22)- 1.69.
e

P= he et.
vi
Ae Se(, L0s Q pof= Cr) Cee Y 5S) Pur vgs — im
p> Pa

ay 5 Ng vaected , a
> ‘Sore ts ascociotho bet Rate & ore exlour

Q6 a) Calculate the Karl Pearson’s correlation coefficient from the following data
xX 12 9 8 10 11 13 7
Y 14 8 6 9 11 12 3

Solution:

FESR 7 Jo AGH CICK
--- page 15 ---
(3 marks)
(1 mark)
(1 mark)
(1 mark)
Q6 b) A continuous random variable   has the probability density function
𝑘𝑥,   0 ≤ 𝑥 < 2,
𝑓(𝑥) = {   2𝑘,   2 ≤ 𝑥 < 4,
−𝑘𝑥 + 6𝑘, 4 ≤ 𝑥 < 6.
Compute 𝑘, mean, and variance.
Solution:
********** 15 **********
--- page 16 ---
Q6 c) In a test given to two groups of students drawn from two normal populations, the marks obtained
were as follows:
Group
18   20   36   50   49   36   34   49   41
A
Group
29   28   26   35   30   44   46
B
Examine at 5% level whether the two populations have the same variance.
Solution:
********** 16 **********
--- page 17 ---
Q7 a i) In a study on students’ academic performance, a partially damaged record provides the following
information: the variance of marks in Mathematics (𝑋) is 9, and the regression lines relating Mathematics (𝑋)
and Physics ( ) marks are: 3𝑋 + 2𝑌 − 26 = 0 and 6𝑋 + 𝑌 − 31 = 0 . Using the given information
determine
a) the means of 𝑋 and 𝑌 .
b) the correlation coefficient between 𝑋 and 𝑌
c) standard deviation of 𝑌.
Solution:
(1 marks)
********** 17 **********
--- page 18 ---
(1 mark)
(1 mark)
(1 mark)
7a ii) Calculate the Spearman’s rank correlation coefficient from the following data:
X   20   30   40   40   50   60   70   80
Y   10   15   20   20   18   25   30   40
Solution:
********** 18 **********
--- page 19 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q7 b) The following table gives the yields on 15 sample fields under three varieties of seeds (viz. 𝐴, 𝐵 and
𝐶):
A   20   21   23   16   20
B   18   20   17   25   15
C   25   28   22   28   32
Analyze at 5% level of significance to test whether the average yields of land under different varieties of seeds
show significant difference.
Solution:
********** 19 **********
--- page 20 ---
KK Me woo A Nova: te

A: 20 21,23 16,20
BI\@ 20, \4,25 15
Ci 25, 28,22,28,32 ,


K= 3) Wi=B, Mars, Va=S =» natitnsnel
L im

—

“Tetols
T= \oo , te =A9 7 ale IS5u

—_Gravd Total C @)= W+te +te +320 A i

Tote) sum 4 sqnane Ces) Sco AM _

2 2. Qa
Peeatmert sum Na anal =(s etevTe | on eo Se ee)

Squowe (ce) > Tss — SST sae ee IE

tExsor Sum ay
Aniové table

Los Q per 212) > Fa = 9.2263
>) Cr FA

2 Ho fs vejested . [| ae

At 5°.


=

FEC 9.0) FcR ok
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 7a9572290173

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Civil_7005/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper b52ac6d78d7d

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CyberSecurity_7010/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 87823044189f

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_EXTC_7006/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 842e651a520d

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_IT_7001/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 09006095d273

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Mechanical_7003/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 05a52c5eff5f

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Mechatronics_7004/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper a2bfbfcd9997

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_IT_7041/Probability and Statistics/ANS_Probability and Statistics(702BS0C076)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper ab02c915c278

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/Integrated_Computer_7032/Probability and Statistics/ANS_Probability and Statistics(702BS0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: mixed (19 pages), mean OCR confidence 45.3
- 8 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (Comp)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 06 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compuslory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
Q1 a) A bag contains 6 white, 5 black, and 3 red balls. Three balls are drawn one after another without
replacement. Compute the probability that
(i) all the balls drawn are black,
(ii) at least one ball drawn is red.
Solution:
Total ways = C(14,3) = 364.   (1 mark)
(i) C(5,3)/C(14,3) = 10/364 = 5/182.   (1 mark)
(ii) 1 − P(no red) = 1 − C(11,3)/364 = 1 − 165/364 = 199/364.   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 b) A discrete random variable 𝑋 has the following probability mass function:
𝑋   0   1   2   3   4   5   6   7
𝑃(𝑋)   0   𝑘   2𝑘   2𝑘   3𝑘   𝑘2   2𝑘2   7𝑘2 + 𝑘
Determine
(i) the value of 𝑘,
(ii) 𝑃(0 < 𝑋< 5), 𝑃(𝑋≥6).
Solution:
We know that for probability mass function, the sum of all probabilities must be 1:
0 + k + 2k + 2k + 3k + k² + 2k² + (7k² + k) = 1   (1 Mark)
9k + 10k² = 1
10k² + 9k - 1 = 0
k = (-9 ± √(81 + 40)) / 20 = (-9 ± 11) / 20   (1 mark)
Thus, k = 1/10 or k = -1. Since probability must be positive, k = 1/10.   (1 Mark)
P(0 < X < 5) = P(1) + P(2) + P(3) + P(4) = 0.1 + 0.2 + 0.2 + 0.3 = 0.8
P(X ≥ 6) = P(6) + P(7) = 0.02 + 0.17 = 0.19   (1 Mark)
----------------------------------------------------------------------------------------------------------------------------
********** 1 **********
--- page 2 ---
Q1 c) The joint probability function of two discrete random variables 𝑋 and 𝑌 is given by 𝑓(𝑥, 𝑦) = 𝑐𝑥𝑦,
where 𝑥= 1, 2, 3 and 𝑦= 1, 2, 3 and 𝑓(𝑥, 𝑦) = 0, otherwise. Find
(i) the value of the constant 𝑐
(ii) Marginal probability function of 𝑋 and 𝑌.
Solution:
The probability distribution table :
y   1   2   3
x
1   1c   2c   3c   6c
2   2c   4c   6c   12c
3   3c   6c   9c   18c   (1 mark)
6c   12c   18c
Since,  f ( x , y ) = 1 , 36c=1 this gives c = 1/36   (1 mark)
x   y
Marginal of X = 1/6,   1/3, 1/2   (1 mark)
Marginal of Y = 1/6,   1/3, 1/2   (1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q1 d) A discrete random variable 𝑋 takes the values 0,1,2 with probabilities 𝑃(0) = 0.2, 𝑃(1) = 0.5,
𝑃(2) = 0.3. Analyze the data to determine the coefficient of kurtosis of the distribution.
Solution:
Mean
𝜇= 𝐸[𝑋] = ∑𝑥𝑝(𝑥)
𝜇= 0 ⋅0.2 + 1 ⋅0.5 + 2 ⋅0.3 = 0 + 0.5 + 0.6 = 1.1.   (0.5 mark)
Variance
𝐸[𝑋2] = 02 ⋅0.2 + 12 ⋅0.5 + 22 ⋅0.3 = 0 + 0.5 + 4 ⋅0.3 = 0.5 + 1.2 = 1.7.
Variance 𝜎2 = 𝐸[𝑋2] −𝜇2 = 1.7 −(1.1)2.   (0.5 mark)
𝜎2 = 1.7 −1.21 = 0.49.   (0.5 mark)
Fourth central moment 𝜇4 = 𝐸[(𝑋−𝜇)4]:
𝜇4 = 0.29282 + 0.00005 + 0.19683 = 0.4897.   (0.5 mark)
Kurtosis
𝛾2 = 𝜇4 = 0.4897/0.2401 ≈2.039.   (1 mark)
𝜎4
------------------------------------------------------------------------------------------------------------------- ---------
Q1 e) A random sample of 400 members has a mean of 4.45 cm. Assuming the population mean is 5 cm with
a standard deviation of 2 cm, test at 5% significance level whether this sample can reasonably be regarded as
drawn from the population. Apply the appropriate test of significance for the mean and state your conclusion.
********** 2 **********
--- page 3 ---
Solution:
----------------------------------------------------------------------------------------------------------------------------
Q1 f) If the lines of regression of sample are 3𝑥−2𝑦+ 5 = 0 and 4𝑥−3𝑦+ 7 = 0, compute the correlation
coefficient between 𝑥 and 𝑦.
Solution:
********** 3 **********
--- page 4 ---
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q2 a) An airport security scanner detects prohibited items in baggage with 95% accuracy, but it incorrectly
flags safe bags 2% of the time. If 8% of passengers actually carry prohibited items, and a bag is flagged as
suspicious, find the probability that the bag does not contain any prohibited item.
Solution:
Let I: item present, F: flagged.
P(I)=0.08, P(F|I)=0.95, P(F|Iᶜ)=0.02.   (2 marks)
P(Iᶜ|F) = (0.02·0.92)/(0.95·0.08 + 0.02·0.92)   (2 marks)
= 0.0184/(0.076 + 0.0184) = 0.0184/0.0944 = 23/118 ≈ 0.195.   (2 marks)
--------------------------------------------------------------------------------------------------------------------------
Q2 b) The two random variables X and Y have the joint probability density function (pdf) given by
𝑓(𝑥, 𝑦) = 6−𝑥−𝑦   0 < 𝑥< 2, 2 < 𝑦< 4. Determine 𝑓(𝑦|𝑥= 2).
8
Solution:
f ( x , y )
To find f ( y | x ) =   (1 mark)
f X ( x )
********** 4 **********
--- page 5 ---
4 6 − x − y   1
Marginal prob function of x is : f X ( x ) =    dy = (6 − 2 x ), 0 x 2   (2 marks )
2   8   8
 6 − x − y 
f ( x , y )       8     6 − x − y
f ( y | x ) =   =   =   (2 marks)
f X ( x )    6 − 2 x    6 − 2 x
   
 8   
f ( y | x = 2) = 6 − 2 − y = 4 − y   (1 mark)
6 − 2 2   2
----------------------------------------------------------------------------------------------------------------------------
Q2 c) A sample of 300 voters from district 𝐴 and 200 voters from district 𝐵 showed that 56% and 48%,
respectively, were in favour of a given candidate. At the 5% level of significance, test whether the candidate
is more preferred in district 𝐴.
Solution:
--------------------------------------------------------------------------------------------------------------
Q3 a) From a set of 7 even and 5 odd numbers, 4 numbers are selected at random without replacement and
multiplied together.
(i) Compute the probability that the product is even.
(ii) Find the probability that the product is odd.
Solution:
Total ways = C(12,4) = 495.   (1 mark)
Product odd ⇔ all four odd: C(5,4)/495 = 5/495 = 1/99.   (3 marks)
Product even = 1 − (1/99) = 98/99.   (2 marks)
********** 5 **********
--- page 6 ---
--------------------------------------------------------------------------------------------------------------------------
Q3 b) A random variable X has the given probability density function:
 x / 2 0  x  2
f ( x ) = 
 0   otherwise
Derive the moment generating function and hence evaluate the first four moments about origin.
Solution
--------------------------------------------------------------------------------------------------------------------
Q3 c) The mean height of 50 male students who actively participate in college athletics is 68.2 inches with a
standard deviation of 2.5 inches, while 50 male students who do not participate have a mean height of 67.5
inches with a standard deviation of 2.8 inches. At the 5% level of significance, test whether male students
who participate in college athletics are taller than those who do not.
Solution:
********** 6 **********
--- page 7 ---
-------------------------------------------------------------------------------------------------------------------
Q4 a) A small bakery bakes 5 cakes each day. Over 5 days, the number of perfectly baked cakes per day was
recorded as follows:
Number of perfectly baked cakes (x) 0 1 2 3 4 5
Frequency (f)   0 1 1 2 1 0
1. Fit a binomial distribution to the given data.
2. Calculate the expected frequencies.
Solution:
********** 7 **********
--- page 8 ---
---------------------------------------------------------------------------------------------------------------------
Q 4b) The number of bacterial cells (𝑌) per unit volume in a culture at different hours (𝑋) is given below:
X 0   1   2   3   4   5   6   7   8   9
Y 43 46 82 98 123 167 199 213 245 272
Determine the lines of regression of 𝑌 on 𝑋 and 𝑋 on 𝑌.
Solution:
********** 8 **********
--- page 9 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
(1 mark)
-----------------------------------------------------------------------------------------------------------------
Q 4c) Two types of antibiotic were tested on two groups of patients for curing a particular disease with the
following results:
Type A   Type B
No. of patients   6   6
Mean period (in days)   13.55   10.10
Unbiased standard
3.2   2.8
deviation (in days)
********** 9 **********
--- page 10 ---
At the 5% level of significance, test whether the difference in the mean period of the two drugs is significant.
Solution:
This formula can also be used to calculate
--------------------------------------------------------------------------------------------------------------------
Q5 a) i) The number of road construction projects that take place at any one time in a certain city follows a
Poisson distribution with a mean of 7.
a) Find the probability that more than 2 road construction projects are currently taking place.
b) Find the probability that less than 2 road construction projects are currently taking place.
.
Solution
********** 10 **********
--- page 11 ---
-----------------------------------------------------------------------------------------------------------------------------------------
Q5 a) ii) The lifespan of a certain type of LED bulb has a mean life of 1200 hours with a standard deviation
of 150 hours. Assuming the lifetime follows a normal distribution, find the percentage of bulbs that last
at least 1400 hours.
Solution:
********** 11 **********
--- page 12 ---
-------------------------------------------------------------------------------------------------------------------
Q 5b) The following table gives the information regarding the color of hair and the color of eye:
Hair color
Black   Fair   Brown   Total
Brown   10   22   32   64
Eye
Blue   15   28   29   72
color
Grey   25   20   19   64
Total   50   70   80   200
Analyze the data using Chi-square test to determine whether there is any association between the hair color
and eye color.
Solution:
********** 12 **********
--- page 13 ---
Ascume do. there t& wo atvorietion bet” Yair Leye Colour im

colour = @ leur (©) | © 2
Booww Blak \o 16 2.25
Grown for pik 22N 0,00 fF
Boon Goon 32 25.6 1.60
5”
Que Black IS 12 0.50 zt
Ble for 22 Q5.2 0.21
Qlue Ris 24 22°38 0.00)
Grey Black 9S \& 5.06
G a>, 20 22.4 0.26
25.6 \. 0
car) eget : =e
x(22")- 1.69.
Ee

{= ihe > ae

vb
p> Ps

> Ho ts vajected 5 z ia

Q6 a) Calculate the Karl Pearson’s correlation coefficient from the following data
x 12 9 8 10 11 13 7
Y 14 8 6 9 11 12 3

Solution:

FIR ICR 7] QI HO
--- page 14 ---
(3 marks)
(1 mark)
(1 mark)
(1 mark)
------------------------------------------------------------------------------------------------------------------
Q6 b) A continuous random variable   has the probability density function
𝑘𝑥,   0 ≤𝑥< 2,
𝑓(𝑥) = {   2𝑘,   2 ≤𝑥< 4,
−𝑘𝑥+ 6𝑘, 4 ≤𝑥< 6.
Compute 𝑘, mean, and variance.
Solution:
********** 14 **********
--- page 15 ---
------------------------------------------------------------------------------------------------------------
Q6 c) In a test given to two groups of students drawn from two normal populations, the marks obtained
were as follows:
Group
18   20   36   50   49   36   34   49   41
A
Group
29   28   26   35   30   44   46
B
Examine at 5% level whether the two populations have the same variance.
Solution:
********** 15 **********
--- page 16 ---
-------------------------------------------------------------------------------------------------------------------------
Q7 a i) In a study on students’ academic performance, a partially damaged record provides the following
information: the variance of marks in Mathematics (𝑋) is 9, and the regression lines relating Mathematics (𝑋)
and Physics ( 𝑌) marks are: 3𝑋+ 2𝑌− 26 = 0 and 6𝑋+ 𝑌−31 = 0 . Using the given information
determine
a) the means of 𝑋 and 𝑌 .
b) the correlation coefficient between 𝑋 and 𝑌
c) standard deviation of 𝑌.
Solution:
(1 marks)
********** 16 **********
--- page 17 ---
(1 mark)
(1 mark)
(1 mark)
---------------------------------------------------------------------------------------------------------------------------
7a ii) Calculate the Spearman’s rank correlation coefficient from the following data:
X   20   30   40   40   50   60   70   80
Y   10   15   20   20   18   25   30   40
Solution:
********** 17 **********
--- page 18 ---
(2 marks)
(1 mark)
(1 mark)
(1 mark)
----------------------------------------------------------------------------------------------------------------------------
Q7 b) The following table gives the yields on 15 sample fields under three varieties of seeds (viz. 𝐴, 𝐵 and
𝐶):
A   20   21   23   16   20
B   18   20   17   25   15
C   25   28   22   28   32
Analyze at 5% level of significance to test whether the average yields of land under different varieties of seeds
show significant difference.
Solution:
********** 18 **********
--- page 19 ---
Sk Me yoo -ANovl i -

A: 20 21,23 16,20
Bi\8 0, \4,25,'5
Ci 256, 28,22,28,32 ,


W= SB mH, Was, Ua=S SD newtnstnaciC

“Tetols se
“N= \oo 7 te =A9 7 Tea21385.
2 sale
Ca rrechm yer weom (cm) = & = 4260
oa iW)
Teta) cow Q square Ce) “OP ag S60 he

2 + >

chuare (Se) TSS 3) Se Eee

txsor Sum %
Anové Nable
inp Stabia eee

cos Rpors C5) d Fax 9.2063

=) Er FA

2 Yo ts vejeoted « ip

At 5°.

> At heart me Frootmest las diftpred ebRect ;

———

FRR ICR 7 QI OR
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 6a78ece7036c

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_IT_7037/Probability and Statistics/ANS_Probability and Statistics(702BS0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper a3c70abcb3fa

- Departments: Mechanical
- Programmes: Integrated Mechanical 7031
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_Mechanical_7031/Probability and Statistics/ANS_Probability and Statistics(702BS0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (11 pages), mean OCR confidence 37.3
- 27 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CIVIL)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech
Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Probability and Statistics
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
9. Use of scientific calculator is allowed.
********** 1 **********
--- page 2 ---
) \ :
@)) S) Glew My=t Mi=s Ma= 28 pay =1uo

~ Cordaed w ements '
TS ene
2,
Ai ab» BOS ria —

Ma=Ms- oud nt Ube yes Lm
Alu = wu tala 6a) yt) alu) = oS

@
» 4) Given'- ye 180 ; a1, S=\yo |
THrcume Hor Ys

tin Rane | mae
7-4 =| Po-WVso0
§/Iu tyo/ Key’

fev X= Sef, & two piled dest a Zy

tele

= +268 3544 PN rare

“(96 — in

x ral Sev a)
| ee | P Rpse) ae

@i) e) noe, la) a BATY-Fa0 Simldanesusly

F168 ay = {= Bc Sere 7)
— Bi)
Me ott eS boy= <b—=s> 1m
Be A+W-E=0 1's Yo <qu? ue
ee) Tee As 9 » bya ab —s Lm

FIC 2 I HH ar
--- page 3 ---
02) @) w-& ree 294 ) Ne 1996 , LAY = ee ke.
ae Noche [pore
SNe! Vices die 3524

[ns -&)> aI nzy-o4y)>
= 8 Uadi2¢°)— Corsdcro2%)
=F iy

le Cevah ~ — (229) ar) Capa Ulezey7

= 0.99689 — Am
—————— Tae

——, lw

©2) ») Njemn =m 2 Sim NG 21.96 —> Im

SD. Lan aa
spa 6 > p= 196 . 1.96 = ONG S q-0- 0S a

y
—————
2 Enpectes eee
x“ © t 2 a b

Per) | 0.0665] 0.2649 4 0.344} 0.240010 .0664 ——= 2
EO) | 6.46 [25:99 | a4. |Z Q@) | 5-56 om
~@ =e) '2@) ©
©) Savuple 5 Wj=20 WHY , Gals ie
Sowple: m2-180 , H-ya ) 8 =3.6

1M

Se
se- | syst - 0.1¢%6 aie os) eu

vy View —=—

j=] AA) 2Ja08 —-» 20

Se

At 5+], Los 2-for shoo chased test Xh=1.96 —a10
> ijk > Ho ts veyected =

FC QI a iar
--- page 4 ---
:

= vy yonstor -
©3) a) Crvew } W = 200 )C=20 N= doe iP Coxisha ef


= 0.0. dpm ber’ o£ 2-2
—< | =0.0-oOugF2
‘a2

= 6.0228
aps le
gee

= 0.5 - tron bet” of 1.0
ae er So. 04 o.yaaz
4.5 = 0.068
=6.680e

Lip) pleoeriea0d)= pacze)< Ares bet” 4 Q |
=— 2K Areo bee’? 5 Qez}
a \ = 28.813

= 0.6826
; za 68.26-/,
————

@3 © Guew vet

4

~ € lo lo (2 ty | 16 [2

Niaiipst Co | 6S |= | Fo | Qo. | Rs

Ri- Youre
Renee | Ge | > y 2, ee '

2™

“2”

2m

Se jim

Ro= Conk

“Slow panko: y 3 a fs atid

Af-e.22)| © Jo.2gt sol] o ° ° D

J JN J J
Sed? =o, 5 Kumeo 2

e Senet

1™M

im
6 (0. SH Coe AS)
cae
= © .482\ —> 1»

FOR OR

im
--- page 5 ---
yy. Thon owe dependect. 8

Ered Vrelues |


Gedvote | 8ai5 56.0C (Sas | aco
on- as ay
N ae 62.6 ic sal ia A Melee ae (Ge =——
~Tote9 ee) Jo. i -. Ute | Yoo
pol) (80 o=y (Go- cent, 4-(190-106.26)
8.5 56.28 Raa
Ecce Cues), (sox 63S)"

52.S Ga. =e
= B.6Y2B +0, 644+ 1 FFIH EOF Y FIISFY 42.9 659— 9 LY
= 3s Sip Ss) i ’ ‘

So oe

2
2 = - =Co A Vie SS =. &
At Sef, ee Dof= Or Net) CHE) =9 5 fro Saal —eim
q 2 - . \ i) :
propa > He ts ea iM

@i) 9) s a) Seve et =
ya6 Ta IBS , SY=42t , eae Wee
ED tales a = = (eR. ame
Ta ae 2S & Ali CS i pe
eis lea 504 NG ea ea

ieee eaaye Ee a)

=) sear 4804 .6028.(") | —= 1m

When »=92 5 Y=4l.9193 i)
a ———
Hie a

FIC DI EH ar
--- page 6 ---
©4) &)) dao cae eee * ”

2 —> 1m
es ©.3 ©.Y ' ——

as ee Wrens A 1

t 2= 3 Hi
ay bo 6.y O.2 O62
ai) pemer, Y=3) = preos' a O80 A aa ee
a ; ‘ Oo
= 0.| + 0.00 = OS =
+ POD + per, D+pe, ») (ee
= 0.06 FO1+0.) + O11 +0.) 40.05 = 0.6

——

—s—o 1M

oo) e) fsume Ho. Gy € aces i
oti 6 > 6g Tae

)= Sz = 324 Ay = zal = Guas 66.¢ eee

) ————————

M2 = @5, Ts = 280.) Aa Bi = wagnttey So) 2 iat

Taye =, (ap) Oe UN

yn — ————

2
Mea) eS al

Dee eo, So - FC) Cam

Yo Lr aes

; area
ae ee BG Ae) a)
ae ee : oe

= i
At of, 9s % pore Gy ‘ we)= Ur) fom 6.3882» 1m)
FLED Yo Is accegsted) cage

a

--- page 7 ---
©8) 2) tet aH bs produced by made > plaasorlero.2
pow is produced Ly Mochive B =) Cee o.uUS

Se Ceh=0or , p(a)oees a p(elense—s 24

plefay=, eco ncrle) oe
— pe). poole). ) pla) +p: pole
= ce) 20 KO, BiG ass

Co Sfo.0d ya: (oicso08)-1C8.26n086)"

= 9.3906 Beene O nS es,
eae nem

—
———

@5) b) Given foy= 26 =») ayers
=e ©   , ohemse -


2™
= = an ety ae Ot : ae
AX 4
EOP) = “Cteaninn Se odo
~alareyl~ a [eke 2] =
= BH 0.2

FR CK

FR RK

im
--- page 8 ---

R=2 WEMe=Va=5 uate

2 3) /

Sample Teale th = Se , Ta=42, Ta238 3S Good tote) (a) -162—>1m

» Cewection for mem Ccom)= G? = 1449.6
wn

—

pe

——$

“\

Treatment Sum 4 Sqrove. Csst) TELE acm =}16.2..7'

ii
-, Bowr sum J Squowesr Csse) =tee-sq = 19:6 =

aH Treotmet wean Teh OD ae -~ €8,.y
iy

i ae =—
ser | =Wieom Squowe ( MSE) a malo,

——

Soe awe 7 Los
agen a 2 ee EP Gee im
: aR ee ee

At K=Ge/, Z voF= Ges pike)» G1) 53 9303 =F a

——$——

~. £>f&K Dd Ho ts véyccted = in

©6)_2 Given P -8.001¢ ; y = 600 p Ni= 80 Ses tie ay
it fe) ee 0q> iw

ui
°

>) POA el) = plo s1)= p(s) 40) — omy (Pass am
as pe ee


8) pooderpced=1-yoreiDe ogee


FOC IGICK QR rR AR x
--- page 9 ---

Be Spyies Wes af NRE OS im

B ADB = es Lett. 2 pine) ee

oe 0.26.
DS - pa
) p@]s) re erat Bar SOS, . 21s 2M

———_—
—

"ty PCa) eB Gres dem obi’ 6 Gio Ot So

PCA) 0.6 a =

BD) pChvd)= pt p@)—plans)= oF

1M
@6) ¢) Given: VUj= 20 ,A=B0 ia See OG ee
— y > 200 ta ——

Sug Ss —
Mesto Are. > Re Bway Hs uf

yy! B AP2 rab ts veduced : es

Ps a 0.1888 > 4 = 0-81! a in

——

ee lroGrs) = 0.03713 ——=» Im

ae = },8850_
RS aes = i

At 51. 5S QR for one Teiled Fesh > XK= 1.6YC—» Ly
Lz|> Zn > Ho hs reyeciey : ee re :

Ld,

FOC IGCK QR rR OR Rx
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
--- page 11 ---
| @3)_B) Giver ForD= j

odin), 9414]
o , othomsise .
Sal 1
Moc) =f Sp co5 Re Pe do = > Sars) é da im:

= al Cie aE ee ot a | alee ana mg nice
= ap Stel] ite
= Catedn = a! (G-mddn = 2 = 0.088 -——> Le

——

b>) 2) ©) Gitar m=I2 , Hx 18.6 SIF2 fe on sm
V2 =10 y Fa =16.9. - n=. ||

| nitYs-2 —— ——


ee pote

t4|= | #2 |- |2 Segkeab| ess th
0.9554 | ———

Tae
se Atte tA Yots recta

FRI ICR 7 FI OH
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 56e9ae7dfd29

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Probability and Statistics/ANS_Probability and Statistics(703BS0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 May 2025
- Text: mixed (6 pages), mean OCR confidence 74.7
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Probability and Statistics
Date: 10 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Q.1. is compulsory
4. Figure in right hand side indicates full marks
5. Out of remaining questions, attempt any 4
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitbale data if necessary
SET B synoptics
Q1
a   2
2
b   1. a=1/81   2
2. P(0<X<5)=8/27   2
c   4
d H0: mean=57.4
H1: mean not equal to 57.4
ztab=1.96
********** 1 **********
--- page 2 ---
zcal=2.067

HO is rejected

e | formula
r=0.8
Q2
Solution To answer the question, we first evaluate the marginal PDFs of X
and Y:
fro = f frveprdy= f corayae [ e dy
—00 0 0
_ | e* x>0
0 otherwise
oo oo oo
froy= f favienar= [ eomds=e [ e*dx
oo 0 0
ale” y20
~ [0 otherwise
Now, fx (a) fy (y) = e*e-Y = e+) = fyy (x,y), which means that X and Y are
independent. a
b Solution Hp : p =P, i.e. the hospital is not efficient.
H,:p<P.
One-tailed (left-tailed) test is to be used.
Let LOS be 1%. Therefore, z, =—2.33.
—P 3
z= Po where p= = 0.0084
PQ 640
n
P = 0.1726, Q =0.8274
_ _ 0.0984 — 0.1726 =-496
c | mean=2
variance=2
Q3

(a) PAU BI= PLA + PLB] PLAN B]=0.4+ 0.5 -0.3 = 0.6
(b) ANB] = PLA]- PAB] =04-03=0.1

(c) From the De Morgan’s second law, PIAV B]= PAN B]=1— PLAN B]=0.7

FIC 2 I HH ar
--- page 3 ---
Solution Ho: x; =X, (or My = Lb).
Ay %>%
Right-tailed test is to be used.
Let LOS be 1%. Therefore, z, = 2.33.

(The two populations are assumed to have SD s 6; = s; and 03 = s»)

_ _ 72-70

8? 6

32 36
Izl<zy

Therefore, the difference between X , and X , (41; and 4) is not significant at
1% level, ie. Hg is accepted and H, is rejected.
That is, statistically we cannot concluede that boys perform better than girls.

c | mean=5
variance=3
Coefficient of skewness=0
Q4
@] 4a Given mean =\ = 1.6
JA yar -1.6/7 @)2
p(x=ay=! _e (1.6)
a ca
(a) P(atleast one ) = P(X > 1) = 1— P(X = 0) = 0.7981 {2 M]
(b) P(atmost one ) = P(X <1) = P(X = 0) + P(X = 1) = 0.5249 {2 M]
(c) P(None ) = P(X = 0) = 0.2019 {2 M}
Db] Let X= Height of the mother

Y=Height of the daughter
n= 8, 2X =522, NY =530, © X? = 34110, XY = 34604

X = UA = B= 65.25,
Y = XY = 580 — 66,25 {1 MJ
bye = en = 0.434 2M
Hence, Regression equation of Y on X is
Y ~Y = Dyp(X —X)
Y = 37.93 + 0.434X {1 M]
When X = 64.5,Y = 65.923 {2 M]

FC QI a iar
--- page 4 ---
Hp: The die is unbiased {1 M]
Hy: The die is biased (1 Mj
LOS
Vous = 2 = 11.07 {1 Mj
Test statistics:
Expected frequency of each number is =22! = 44 {1 M]
table [2M]
Observed | Expected frequency | (O; — E,)?
52 my 64
4 my 100
58 my 196
28 4 256
32 am ier
0 a 6
264 264
= 17.6362 1M]
We reject Ho 1M]
Q5
a Solution Refer to Note 2 under F-test. To conclude that the two samples have

been drawn from the same population, we have to check first that the variances
of the populations do not differ significantly and then check that the sample
means (and hence the population means) do not differ significantly.

a2 _ 8x12 ~2_ 11X2°5

oy = = 137; O2=— 9 275
6; 2.
= = 2 _ 5.007 with v, = 10 and vy = .
Go; 137 °

From the F-table, Fo 95 (10, 7) = 3.64.
IfHy: 6} =G3 and Ay: 6} # G3, then, Hy is accepted, since F < F gos,

That is, the variances of the populations from which samples are drawn may
be regarded as equal.

_ X, 7% _ -6:9
ns; +nys3 1 + 1 (3 )E+4)
nytn,-2 Jl m ny 17 sou
=-©9 ___ 1905
0-6864

and v=n,+n,—-2=17

From the f-table f 95 (V= 17) = 2.11.

If Ho: X¥; =X and H,: x, # X5, then Hp is rejected, since It! > fo 95.

That is, the means of two samples (and so the populations) differ
significantly.

Therefore, the two samples could not have been drawn from the same normal
population.

b | T=240
CF=3468
SST=84
SSTR=16.8
SSE=67

FIC 7) IC HOH
--- page 5 ---
Source of Sum of DF Mean Square F statistic

variation Squares
Between SSTR (SSC) | r-1=2 MSTR(MSC)= SSTR(SSC) | ,_MSTR(MSC)
Samples =16.8 r-l MSE
=84 =1.13
Within Samples | SSE =67.2 | N-r=9 MSE= SSE
-r
= 7.466
Total SST = 84 N-1=11
Fecal = 1.13
Ftab = 4.26

HO is accepted
the mean yields.

Q6)a

Solution P(T) = P(the coin is a true coin) = 2

P(F) = P(the coin is a false coin) = _
Let A = Event of getting all heads in 4 tosses
1 101 01.1
Then P(A/T) = ~x =x =x ==— and P(A/F)=1.
ain 2 2 2 2 16 (air)
By Bayes’ theorem,
P(F)x P(A/F)
P(F)x P(A/F)+ P(T)x P(A/T)
1
4 xl _16
1

dy 3ytl 19
4 4°16

P(FIA) =

Db solution Here x= 1550, s =120,n=25 and p= 1600.
Left-tailed test is to be used. LOS be 5%.
¥-m _ -50V24

—— > = =-2.04 and v=24
s/jn-1 120

Now t=

tos for one-tailed test = f) , for two-tailed test (for v= 24) = 1.71.
We see that Itl > Ifp I.

Therefore, Hy is rejected and H, is accepted at 5% LOS. That is, the claim of
the company cannot be accepted at 5% LOS.

FIC DI EH ar
--- page 6 ---
Cc Given: mean=j1 = 68, standard deviation = 0 = 3

(a) When X = 72,2
P(X > 72) = P(z > 1.33) = 0.0918
Number of students with more than 72 kgs =28 (2.5 M]
(b) When X = 64, 2 = Ss# = 4-68 — _1.33 P(X < 64) = P(z < -1.33) = 0.0918
Number of students have marks less than or equal to 64 kgs =28 (2.5 M]
(c) When X = 65,2
When X = 71,z= *#=45
P(65 < X < 71) = P(-1< X <1) = 6826
Required Number of students=205 [3 M]

Q7 | a| Mean=2.84
p=0.568
q=.432

Req freq. 2,10,26,34,22,6

b| X ony : x=3650y + 61250
Y on X : y=3137x +537
r=0.7766

Cc m =400 , m=200, DP, =.5, Py=02 {1 M)
Step 1 Null hypothesis
Ho: Dy = Be {1 M}
Step 2 Alternate hypothesis
Hy: DP, AD» 1 M)

Step 3 Level of significance

tab = 1.96 {1 Mj
Step 4 Test statistics
[2 MI
Pp = bnithm _ 9.4, Q=1-P=06

Py

= 7.07

(2M)
Step 5 Conclusion:
Since Zeal > Zab

We reject Ho

FIC 6 I HF
````

## 2024-25 · Re-Exam · Sem 2 · Answer key · paper c42c3346ce08

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Probability and Statistics/ANS_Probability and Statistics(703BS0C003)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2025
- Text: mixed (7 pages), mean OCR confidence 74.3
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 2 Re-exam(Exam Year: 2024-2025)
Subject: Probability and Statistics
Date: 09 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Q.1. is compulsory
4. Figure in right hand side indicates full marks
5. Out of remaining questions, attempt any 4
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitbale data if necessary
Q1
a   2
2
b   1.   a=1/81   2
2. P(X<3)=1/9   2
********** 1 **********
--- page 2 ---
c
2
2
d H0: a sample from population
with mean weight 56 kgs and standard deviation 25 kgs.   1
H1: Sample cannot be regraded as one coming from the population   2
ztab=1.645   1
zcal=4.48
H0 is rejected
e Formula   2
r=0.7512   2
Q2
a
2
2
2
********** 2 **********
--- page 3 ---
b

Solution Let P and p denote the population and sample proportions of
shoppers not making a purchase.
Hy: p=P
H,:p>P,sincep=0.7 and P=0.6
One-tailed (right-tailed) test is to be used.
Let LOS be 5%. Therefore, z, = 1.645.

= p-P __ 0.7-0.6 = 1443

PQ [06x04
n 50

Izl< zm

Therefore, the difference between p and P is not significant at 5% level,
i.e., Hy is accepted and H, is rejected.
That is, the sample results are consistent with the claim of the salesman.

c | Mean =3
Variance=3

Q3

Aj=txt=t-o0.125
4-2 8

p[B| a= 1404) a. ]

pta| p= L401 5, ppp = PLA _ 1/8) _ 3

PLB] P[A|B] (1/3) 8
13 11

P[AV BI = PlA]+ PIBJ- PLA B]= 3+ 5-5 = 5 =05

=> PAA B]= PLAIP[B

= 0.375

b m =700 , ng=300 , 7, =250, 7 =300, 0, =30, o2=40,
Step 1 Null hypothesis
Hy: =F
Step 2 Alternate hypothesis
Hy :%, FF {1M
Step 3 Level of

a

ignificance
0.01 Zab = 2.58 {l M}
Step 4 Test statistics

Step 5 Conclusion
Since zcat > 2tab
We reject Ho

c | mean=3
variance=15
Coefficient of skewness=-1.480

Q4

FC QI a iar
--- page 4 ---
da Probability of defective item =p = 20% = 0.2
Probability of non-defective item =q = 1 — p = 80% = 0.8

Total number of items =n=5

(a) Probability that none of defective =P(0) => Cy(0.2)°(0.8)°=0.3277 2M
(b) Probability that one defective item =P(1) =° C,(0.2)!(0.8)'=0.4096 2M
(0) P(L< X <4) = P(2) + P(3) =* C2(0.2)?(0.8)$ +9 C3(0.2)5(0.8)? = 0.256 2M

b} Straight line is y = ag + aux
The two normal equations are
Sy =nant+a ox
n=7, dla = 113, Soa? = 1983, Sy = 182,d> vy = 3186

Tag + 113a; = 182 ‘(1 M]
113a9 + 1983a, = 3186 ‘{1 M]
ao = 0.82,a; = 1.56 ‘(1 M]
The equation of straight line is y=0.82+1.56x
When x = 30, y = 47.82 ‘(2 M]
c
Ho: The die is unbiased [1 M)
Hy: The die is biased {1 Mj)
LOS
Xiab = XG {1 Mj
Test
Expected frequency of each number is =28 = 44 {t M]
table [2M]
Observed | Expected frequency | (0, — B)2] 2===
40 At 46
32 4 144
28 4 256
58 4 196
54 44 100
52 44 64 1.4545
264 264 17.6362
Xeat flM]

Since Xiu > Xiab
We reject Hy {1 M]

FIC 7) IC HOH
--- page 5 ---
Q5

2
a Solution x, = Mean of sample | = = = 24.6

X, = Mean of sample 2 = “ = 29.0
5? = Variance of sample 1 = : L(x, — 24.6)? = 4.24

s3 = Variance of sample 2 = : Xx; — 29.0" = 18.0

6?= : x 4.24 = 5.30 and v=4; 63 -§ x 18.0 = 21.60 and v=5

Ho: 67 = 63; Wy: G7 #65
53 _ 21-60
6) 5-30
Fyos (5, 4) = 6.26.
Since F< Fos, Hy is accepted. Therefore, the variances of the two populations
can be regarded as equal.

F= =407

_ X,~%Xy _ -4-4
niemsy(1 1) (Ze G4
nj +n,—2 ny Ny 9 5 6
—4-4
= =-1.92
2-2943

and v=9.

From t-table, Fo 95 (V = 9) = 2.26.

If Hp: 3 =X, and Hy: X, # Xy, Hp is accepted, since It| < Fos.

That is, the means of two samples (and hence the populations) do not differ

significantly. Therefore, the two samples could have been drawn from the same
normal population.

b | T=330
CF=7260
SST=330
SSTR=190
SSE=140

FIC DI EH ar
--- page 6 ---
2
Fcal = 8.14
Ftab = 3.8853   1
1
H0 is rejected. Statistically we conclude that there is significant difference between
the mean yields.   1
Q6 a
1
1
1
3
b   1
1
1
2
1
********** 6 **********
--- page 7 ---
c | Given: mean=j: = 14, standard deviation = 0 = 2.5

(a) When X = 12,2 = ~# = 254 = 0.8
When X = 15,2 = X=# = 454 =04

o 25
P(12< X < 15) = P(—0.8 < X < 0.4) = 0.1554 + 0.2881 = 0.4435

Number of students score between 12 and 15 = [3 M]
(b) When X = 18,2 = ~# = #4 =16
P(X > 18) = P(z > 1.6) = 0.0548
Number of students score above 18 =55 {2.5 M]
(c) P(X < 18) = P(z < 1.6) = 0.9452
Number of students score above 18 =945 [2.5 M]
Q7 | a| mean=0.61
Req. frequencies 109,66,20,4,1,
b | Formula
y=16x+20
x=40,y=660

Step 1 Null hypothesis

Ho : Py = Pa {1 Mj
Step 2 Alternate hypothesis

Hy: DP, # Pe {1 Mj
Step 3. Level of significance

a =5% = 0.05, Zab = 1.96 {1 Mj
Step 4 Test statistics

(2 M)
P= bnsbans — 01.525, Q=1-P=0A475
Pi —Po

Zeal = SS — = -13
Pa

(2M)
Step 5 Conclusion:
Since Zeal < Zab
We accept Ho

FIC 7 IC OHH
````
