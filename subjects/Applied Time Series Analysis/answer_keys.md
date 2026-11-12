# Applied Time Series Analysis: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 3e293bd7d8fc

- Departments: AI and Machine Learning, Artificial Intelligence
- Programmes: BTech AI 7012, BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIML_7053/Applied Time Series Analysis/ANS_Applied Time Series Analysis(702DB0E007)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: mixed (14 pages), mean OCR confidence 87.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024
Program/s: B.Tech   Year: IV Semester: VII
Stream/s : AI/AIML
Subject: Applied Time Series Analysis   Time: 03 hrs (______to_______)
Date:   /   / 2024   No. of Pages: 14
Marks: 100
Final Examination/Re-Examination ( Re-exam year)
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.
1) Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain moving average method and its application in time sires analysis. Also
write the equations for the moving average of odd order and then explain how even
order moving average is cantered with the help of equation.
CO-1 ;
Component   Description   Marks
SO-1 ;   [05]
Concept & Application   Definition and practical uses 2
BL-2
Equation for Odd Order MA Formula and brief example   1.5
Centering of Even Order MA Explanation with equation   1.5
Total   5 Marks
b.   For the given data compute the seasonal index of all the seasons (quarter).
Year   Q1   Q2   Q3   Q4
2003   72   68   80   70
2004   76   70   82   74
2005   74   66   84   80
CO-1 ;   2006   76   74   84   78
SO-1 ;   [05]
BL-3
The Data is collected quarterly.
Yearly
Year   Q1   Q2   Q3   Q4
Avg
2003   72   68   80   70   72.5
1
--- page 2 ---
2004   76   70   82   74   75.5
2005   74   66   84   80   76
2006   76   74   84   78   78
Quarterly Avg   74.5   69.5   82.5   75.5   75.5
0.9867   0.9205   1.0927
Seasonal Index   55   3   15   1
Table ----(2.5 M)
Final calculation of Index ---(2.5M)
c.   Define Autocorrelation Function (ACF) and Partial Autocorrelation Function
(PACF). How are they useful in identifying ARMA models?
Define Autocorrelation Function (ACF): +1.5 marks
Define Partial Autocorrelation Function (PACF): 1.5 marks
Usefulness in Identifying ARMA Models: +2 marks
CO-3 ;
Model   ACF Pattern   PACF Pattern
SO-1 ;   [05]
AR(p)   Tails off gradually Cuts off after lag p
BL-2
MA(q)   Cuts off after lag q   Tails off gradually
ARMA(p, q)   Both ACF and PACF —
tail off gradually
Thus, by examining ACF and PACF plots, we can determine the order (p, q) of
ARMA models:
   Identify the cutoff in PACF → possible AR(p) order
   Identify the cutoff in ACF → possible MA(q) order
d.   Explain the steps involved in forecasting using ARIMA models in brief.
The ARIMA (AutoRegressive Integrated Moving Average) model is used to
forecast nonstationary time series by combining autoregressive (AR),
differencing (I), and moving average (MA) components.
CO-3 ;
SO-1 ;   Steps in Forecasting Using ARIMA: (+1 marks for each steps)   [05]
BL-2
1. Model Identification:
Plot the series to check trend or seasonality. Use differencing to make it
stationary.
ACF and PACF plots help identify suitable values of p (AR order), d
(difference order), and q (MA order).
2
--- page 3 ---
2. Parameter Estimation:
Estimate model coefficients using methods like Maximum Likelihood or
Least Squares.
3. Diagnostic Checking:
Check residuals — they should be random (white noise).
Use ACF of residuals or Ljung–Box test for verification.
4. Forecasting:
Use the fitted ARIMA(p, d, q) model to predict future values based on
past data and errors.
Forecasts include confidence intervals.
5. Model Evaluation:
Compare forecasts with actual data using accuracy measures such as
MAPE or RMSE, and update the model if needed.
Consider a time series
X = [6 ,2, 1, 4, -1, 9, 7, 2, 0, 7]
Compute the auto covariance and auto correlation coefficients up to lag 3. (between
original time series and its lag1, lag2 and lag 3)   [10]
[Note: You can use excel for the calculation. Write the formula used and solution
of every step in the answer sheet].
Formula – 3 M
Table and calculation – 5 M
Final Ans – 2 M
xt-   xt-   xt-
xbar   xbar   xbar
(xt-   * xt-   * xt-   * xt-
xt-   xt-1 -   xt-2 -   xt-3 -   xbar) 1 -   2 -   3 -
Q2a   Xt   Xt-1   xt-2   xt-3   xbar   xbar   xbar   xbar   2   xbar   xbar   xbar
CO-3;   6   2.3   5.29
SO-2;   2   6   -1.7   2.3   2.89   -3.91
BL-3   1   2   6   -2.7   -1.7   2.3   7.29   4.59   -6.21
4   1   2   6   0.3   -2.7   -1.7   2.3   0.09   -0.81   -0.51   0.69
-1   4   1   2   -4.7   0.3   -2.7   -1.7   22.09   -1.41   12.69   7.99
-   -
9   -1   4   1   5.3   -4.7   0.3   -2.7   28.09   24.91   1.59   14.31
-
7   9   -1   4   3.3   5.3   -4.7   0.3   10.89   17.49   15.51   0.99
2   7   9   -1   -1.7   3.3   5.3   -4.7   2.89   -5.61   -9.01   7.99
-   -
0   2   7   9   -3.7   -1.7   3.3   5.3   13.69   6.29   12.21   19.61
-
7   0   2   7   3.3   -3.7   -1.7   3.3   10.89   12.21   -5.61   10.89
xbar   3.7
3
--- page 4 ---
SUM((x
t-
xbar)2)   104.1
Varianc
e of Xt   10.41
SUM(xt
-xbar *
xt-1 -   -
xbar)   20.49
SUM(xt
-xbar *
xt-2 -   -
xbar)   34.78
Lag1_a   -
utocova   2.276
riance   67
Lag2_a   -
utocova   4.347
riance   5
Lag3_a   -
utocova   0.767
riance   14
Lag1_a
utocorre   -
lation_c   0.218
off   7
Lag2_a
utocorre   -
lation_c   0.417
off   63
lag3_au   -
tocorell   0.073
ation   69
A supermarket chain wants to forecast weekly demand for a popular product for
the next three months. Historical sales data show a relatively stable pattern with
small random fluctuations. Explain which exponential smoothing method would
be most appropriate for generating forecasts for the upcoming weeks. Also,
describe the terms/components included in the model, discuss the role of the
smoothing parameter and how it can be determined, and explain how you would
assess the accuracy of the forecasts.
Q2b
Choosing the Model Terms (3 Marks)
CO-1;   Since the data show a stable pattern without trend or seasonality, the   [10]
SO-1;
appropriate model is Simple Exponential Smoothing (SES).
BL-2
 The SES model assumes the series fluctuates around a constant level, with
random noise.
 The model uses only a level component (no trend or seasonal terms).
 The formula for SES is:
Y  t  1   Y t   ( 1   ) Y t  1   ( 1   ) 2 Y t  2     ( 1   ) n Y t  n  
where:
o α = smoothing parameter (0 < α ≤ 1)
Role and Determination of the Smoothing Parameter (4 Marks)
4
--- page 5 ---
 The smoothing parameter α determines how much weight is given to
recent observations.
o High α (close to 1): gives more weight to recent data → forecasts
respond quickly to changes.
o Low α (close to 0): gives more weight to older data → smoother
forecasts, less responsive to short-term fluctuations.
 Choosing α:
o   It can be selected subjectively based on how stable or volatile the
data are.
o More commonly, α is estimated statistically by minimizing an in-
sample error measure such as Sum of Squared Errors (SSE) or
Mean Squared Error (MSE).
 Once α is determined, forecasts for the next 12 weeks can be generated
recursively using the model.
Assessing Forecast Accuracy (3 Marks)
   Forecast accuracy is evaluated using out-of-sample data or cross-
validation.
 Common measures include:
o Mean Absolute Error (MAE)
o Root Mean Squared Error (RMSE)
o Mean Absolute Percentage Error (MAPE)
   Additionally, residual analysis is important: residuals (forecast errors)
should resemble white noise (no pattern or autocorrelation).
 Comparing SES with alternative methods (e.g., Holt’s or moving averages)
can confirm suitability.
A company records monthly sales revenue (in Rupees 000s) and the corresponding
advertising expenditure (in Rupees 000s) over six months as shown below:
Month   Advertising (x)   Sales (y)
1   10   25
2   12   27
3   15   32
Q3a
4   18   35
CO-1;
SO-2;   5   20   37   [10]
BL-3   6   22   40
i. Determine the value of slope and intercept for a linear regression model y=
a+bx using Excel.
ii. Predict the value of y at x =24 using this model.
Determine the MSE for the model (show squared error for each row).
Step (i) Determine slope and intercept using Excel (4 Marks)
5
--- page 6 ---
1. Slope (b):
Use Excel formula: =SLOPE(range_y, range_x)
b=1.24
2. Intercept (a):
Use Excel formula: =INTERCEPT(range_y, range_x)
a= 12.5667
Marks:
 Slope correct: 2 marks
   Intercept correct: 2 marks
Step (ii) Predict y at x = 24 (3 Marks)
Regression equation:
ypred= 12.5667+1.2435x
ypred =12.5667+1.2435×24=42.4107
 Correct formula / substitution: 1 mark
 Correct forecast value: 2 marks
Step (iii) Determine MSE (3 Marks)
MSE = 0.1749
Marks:
   Correct squared errors: 1 mark
   Correct sum / division by n: 1 mark
   Correct final MSE: 1 mark
x   y   Predicted y^   Error (e=y−y^)   Squared Error
=12.5667+1.2435x   (e2)
10   2 12.5667+1.2435(10)≈25.00 25−25.002=−0.0   (−0.002)2≈0.000
5 2   02   0
12   2 12.5667+1.2435(12)≈27.49 27−27.490=−0.4   (−0.490)2≈0.240
7 0   90   1
15   3 12.5667+1.2435(15)≈31.21 32−31.219=0.78   (0.781)2≈0.6100
2 9   1
18   3 12.5667+1.2435(18)≈34.94 35−34.948=0.05   (0.052)2≈0.0027
5 8   2
20   3 12.5667+1.2435(20)≈37.43 37−37.437=−0.4   (−0.437)2≈0.191
7 7   37   0
22   4 12.5667+1.2435(22)≈39.92 40−39.924=0.07   (0.076)2≈0.0058
0 4   6
6
--- page 7 ---
Su   ∑e2≈1.0496
m
Derive the forecast equation for T+2 if ARIMA modelling at time stamp t is
ARIMA(3,1,1)
Q3b
CO-3;   --------(5 M)   [10]
SO-2;
BL-4
--------(5M)
Q4a   (i)   1. Determine the order of ARIMA model based on following graphs along with
CO-3;   justification. Consider the original data is differenced 2 times.
[07]
SO-2;
BL-4
7
--- page 8 ---
2. Suppose the differenced series shows an ACF that tails off gradually, while
PACF cuts off sharply after lag 1. Propose the most likely ARIMA structure
and justify.
1.
ARIMA ( 2,2,0) or (2,2,1) or (1,2,1) or (0,2,1)   2 mark
Justification   3 marks
2.
2 marks
PACF cutoff ⇒ AR process.
Cutoff at lag 1 ⇒ AR(1).
With differencing: ARIMA(1,1,0).
(ii) Two ARIMA models are fitted to the same data:
 Model A: log-likelihood = –200, k=3.
 Model B: log-likelihood = –195, k=5.
CO-3;   Compute AIC for both models and identify which is preferred.
[03]
SO-2;
BL-3
Model A: AIC = 400+6=406. (1 mark)
Model B: AIC = 390+10=400. (1 mark)
8
--- page 9 ---
Model B preferred (lower AIC). (1mark)
(i)   Define the concept of overfitting in time-series models. Give one example of how
overfitting can occur when selecting ARIMA orders using ACF/PACF.
Q4b
CO-3;   Overfitting: including unnecessary parameters that fit noise rather than
SO-2;   signal. (2 marks)   [05]
BL-2   Example: choosing AR(4) when true process is AR(1) just because of
small random spikes in ACF/PACF. (2 marks)
Leads to poor out-of-sample forecasting. (1 mark)
(ii)   In the context of time series regression with ARIMA errors, explain why
minimizing the sum of squared ηt (one-step-ahead forecast errors) instead of the
true residuals can lead to problems.
CO-3;
SO-1;   [05]
BL-5
(i)   Suppose you are analyzing a company's sales data for forecasting. The Augmented
Dickey-Fuller (ADF) test results on this sales data are as follows:
   Test statistic: -3.00
   p-value: 0.07
   Critical value at 5% significance: -2.95
(a) Is the sales time series suitable for direct forecasting using ARIMA
models based on these ADF results?
(b) What steps would you recommend to prepare the data before applying
Q5a   any forecasting model based on these ADF test findings?
CO-3;
[05]
SO-2;   The ADF test statistic is -3.00 and the critical value at 5% significance is -
BL-5   2.95. Since -3.00 < -2.95, the null hypothesis of a unit root
(nonstationarity) is rejected. However, the p-value is 0.07, slightly above
0.05, indicating borderline significance. (+2 marks)
Conclusion: The series is likely stationary or borderline stationary but not
definitively stationary. (+2 marks)
Recommended steps:
Due to borderline results, it is advisable to perform further differencing
once and/or check stationarity visually (plots) and with other tests. Only
after confirming stationarity should ARIMA or other forecasting models
9
--- page 10 ---
be applied. Nonstationary series need differencing to avoid spurious
forecasting results. (+1 marks)
(ii) Suppose you have residuals from an ARIMA model:
Residuals = {0.4, -0.2, 0.1, -0.3, 0.2, -0.1, 0.5, -0.4, 0.2, 0.5}
The sample autocorrelation coefficients at lag 1 and lag 2 are 0.3 and 0.2
respectively. The critical value of the chi-square distribution at 5% significance
level and 2 degrees of freedom is 5.99.
1.Calculate the Ljung-Box Q statistic up to lag 2.
2.Determine if the residuals are significantly uncorrelated at 5% significance level.
3.State what this implies about the adequacy of the ARIMA model.
CO-3;
SO-2;   [05]
BL-5   1.Calculating the Ljung-Box Q statistic:
Q = 1.8 (+ 2 for correct formula and value)
2.Compare Q=1.8 with critical value 5.99. Since 1.8<5.991, we fail to reject the null
hypothesis. The residuals are not significantly auto correlated up to lag 2 at 5%
significance. ( +2 Marks)
d)Implication:
This means the ARIMA model's residuals pass the Ljung-Box test for autocorrelation at
lag 2, indicating a satisfactory model fit in terms of independence of residuals. ( +1 marks
)
Explain the components of an ARIMA model in detail. How does an ARIMA
model differ from an ARMA model? Illustrate your answer with relevant points.
Q5b
CO-3;   Introduction (brief overview) + 1 marks
Explanation of AR component   + 2 marks   [10]
SO-1;
BL-2   Explanation of I (differencing) component +2 marks
Explanation of MA component   +2 marks
Clear distinction between ARIMA and ARMA   +2 marks
Conclusion (summary of significance)   +1 marks
What is white noise for time series analysis? Explain the criteria for a time series
process to be mentioned as white noise? Also, Considering multiplicative time
series decomposition, describe all the steps of time series decomposition.
Component   Description   Marks
Q6a   Definition   of   white Clear   concept   with
1.5
CO-4;   noise   equation
[10]
SO-1;   Importance   in   time
Need for white noise   0.5
BL-2   series analysis
Criteria for white noise   All criteria listed clearly 2
Concept   of
multiplicative   Formula + when to use   1
decomposition
10
--- page 11 ---
Steps of multiplicative Clear   stepwise
4
decomposition   procedure with formulas
Graphical
Clear mention of plots   1
representation note
Total   10 Marks
Explain the concept of bootstrapping and bagging? Also, Explain how
bootstrapping and bagging may improve the forecasting accuracy?
CO-4;   Section   Marks
SO-1;   Bootstrapping concept, steps, and   [10]
BL-2   mathematical representation   4
Bagging concept, steps, and equation   3
Improvement in forecasting accuracy
3
(comparison table + explanation)
Total   10 Marks
Consider the following hierarchical time series structure shown in figure below:
 Level 0: Total
 Level 1: Group A and Group B
 Level 2: Subgroups under A (AA, AB, AC) and under B (BA, BB)
Q7a
CO-4;
[10]
SO-2;
BL-2   The forecast on the each level is
𝑌̂Total,t = 1000 ,
𝑌̂A,t = 650 , 𝑌̂B,t = 400 ,
𝑌̂AA,t = 300, 𝑌̂AB,t = 250 , 𝑌̂AC,t = 150 , 𝑌̂AA,t = 200, 𝑌̂AB,t = 250
1. Identify the incoherence at each level of the hierarchy. (3 marks)
2. Apply the proportional reconciliation method to adjust forecasts at each
level so that the final forecasts become coherent with the total of 1000. (7
marks)
11
--- page 12 ---
Hierarchical Structure:
* Level 0: Total
* Level 1: Group A and Group B

* Level 2: Subgroups under A (AA, AB, AC) and under B (BA, BB)

Step 1: Non-Coherent Initial Forecasts
Let's assume we have the following non-coherent forecasts:

* Total Forecast:

Yrrotale = 1000

* Level 1 (Groups A and B):
Yay = 650
Ype = 400

(Note: The sum of these forecasts is 650 + 400 = 1050, which exceeds the Total forecast of

1000. Hence, they are non-coherent.)

* Level 2 (Subgroups under A and B):

*° Group A:
Yau = 300
Yapy = 250
Yacu = 150

(Sum = 300 + 250 + 150 = 700, which does not match Group A's forecast of 650.)

* Group B:
Yeas = 200
Yops = 250

(Sum = 200 + 250 = 450, which does not match Group B's forecast of 400.)

Step 2: Proportion Calculation to Achieve Coherence

1. Adjust Level 1 Forecasts (Group A and B)
‘To make the forecasts coherent, we need to redistribute the forecasts for Groups A and B based on

their initial proportions.

Calculate Proportions for Level 1:

+ The total initial forecast for Level 1 is 650 + 400 = 1050.
Proportions:

Ps 0.619

Yau 400

Ps © 0.381

1050 1050
Adjust Forecasts: Now, we adjust the forecasts for Group A and Group B to match the Total forecast
of 1000:

Yar = Ps * Yrovae = 0.619 x 1000 ~ 619

Yau = Ps x Yrotate =

381 x 1000 ~ 381

12
--- page 13 ---
------2M
-----3M
Give an example of complex seasonality and explain how such seasonality can be
Q7b
modelled? Also, Explain the Prophet model and how it is different from the
CO-4;   [10]
ARIMA class of models?
SO-2;
13
--- page 14 ---
BL-2
Section   Marks
Example and explanation of complex
3
seasonality
Methods to model complex seasonality 2
Prophet   model   (structure   and
3
components)
Comparison: Prophet vs ARIMA   2
Total   10 Marks
14
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 2a0008f78545

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_AI_7051/Applied Time Series Analysis/ANS_Applied Time Series Analysis(702DB0E007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: mixed (19 pages), mean OCR confidence 79.7

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (ARTIFICIALINTELLIGENCE)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: Applied Time Series Analysis
Date: 14 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly
CO- A Explain what is meant by “white noise” in time-series analysis and describe the conditions   5
1   that a time series must satisfy to be classified as white noise.
BL-
2
1. Definition (1 Mark):
SO-   White noise is a time series consisting of completely random observations with no
1   predictable pattern, trend, or structure.
2. Conditions (3 Marks):
3. Significance (1 Mark):
White noise indicates pure randomness and is used to check whether a time series model has
successfully captured all underlying patterns.
CO- B Given the table of time-series values for each season, apply the method for computing seasonal 5
1   indices to calculate the seasonal index for every season and show all steps of your calculation.
BL-
Year   Q1   Q2   Q3   Q4
3
2003   65   70   78   72
SO-   2004   68   72   80   74
1   2005   70   74   82   76
2006   72   76   84   78
Year   Q1   Q2   Q3   Q4
2003   65   70   78   72
********** 1 **********
--- page 2 ---
2004   68   72   80   74
2005   70   74   82   76
2006   72   76   84   78
Season wise avg   68.75   73   81   75
Over all AVG   74.4375
Seasonal Index   0.923594   0.980688   1.088161   1.007557
Table – 2.5 marks
Calculation with all steps – 2.5 marks
CO- C Explain what is meant by an autocorrelation plot (ACF) and a partial autocorrelation plot   5
3   (PACF) of time-series data, and describe how these plots are used in time-series modelling.
BL-
2
1. Definition of ACF (1 Mark):
SO-   Autocorrelation Function (ACF) measures the correlation between a time series and its
1   lagged values at different lags.
2. Definition of PACF (1 Mark):
Partial Autocorrelation Function (PACF) measures the correlation between a time series and
its lagged values after removing the effect of intermediate lags.
3. Key Difference (1 Mark):
ACF includes both direct and indirect correlations, whereas PACF shows only direct
correlation at a specific lag.
4. Use in Time Series Modelling (2 Marks):
•   Model Identification (1 Mark):
ACF and PACF help in identifying appropriate ARIMA models:
o ACF cuts off → suggests MA(q) model
o PACF cuts off → suggests AR(p) model
•   Order Selection (1 Mark):
Used to determine the values of p (AR terms) and q (MA terms) for model building.
CO- D First odder differencing can make non stationary time series stationary. Prove it by   5
3   considering the time series 𝑦𝑡= 𝛽0 + 𝛽1𝑡+ 𝜀𝑡 , where t is the time component.
BL-
2
SO-
1
********** 2 **********
--- page 3 ---
Derivation – 2.5 Marks
Stationarity Condition proof --- 2.5 Marks
Q2   A Consider the time series:   10
CO-   𝑋= [9,7,8,10,12,11,13,15,14,16,17,15]
Then
3
1. Compute the mean and variance.
BL-
2. Calculate autocovariance at lag1, lag2 and lag3.
3   3. Compute autocorrelation coefficients at lag 1, lag 2 and lag3.
SO-   4. Comment on whether the series shows positive correlation.
1   [You may use MS excel for solving the above question and write every step of calculation.]
xt-xbar   xt-xbar   xt-xbar
xt-1 -   xt-2 -   (xt-   * xt-1 -   * xt-2 -   * xt-3 -
Xt   Xt-1   xt-2   Xt-3   xt-xbar   xbar   xbar   xt-3*xbar   xbar)2   xbar   xbar   xbar
9   -3.25   10.5625
7   9   -5.25   -3.25   27.5625   17.0625
8   7   9   -4.25   -5.25   -3.25   18.0625   22.3125   13.8125
10   8   7   9   -2.25   -4.25   -5.25   -3.25   5.0625   9.5625   11.8125   7.3125
12   10   8   7   -0.25   -2.25   -4.25   -5.25   0.0625   0.5625   1.0625   1.3125
11   12   10   8   -1.25   -0.25   -2.25   -4.25   1.5625   0.3125   2.8125   5.3125
13   11   12   10   0.75   -1.25   -0.25   -2.25   0.5625   -0.9375   -0.1875   -1.6875
15   13   11   12   2.75   0.75   -1.25   -0.25   7.5625   2.0625   -3.4375   -0.6875
14   15   13   11   1.75   2.75   0.75   -1.25   3.0625   4.8125   1.3125   -2.1875
16   14   15   13   3.75   1.75   2.75   0.75   14.0625   6.5625   10.3125   2.8125
17   16   14   15   4.75   3.75   1.75   2.75   22.5625   17.8125   8.3125   13.0625
15   17   16   14   2.75   4.75   3.75   1.75   7.5625   13.0625   10.3125   4.8125
********** 3 **********
--- page 4 ---
xbar   12.25
SUM((xt-xbar)2)   118.25
Variance of Xt   9.854167
SUM(xt-xbar * xt-1 - xbar)   93.1875
SUM(xt-xbar * xt-2 - xbar)   56.125
Lag1_autocovariance   8.471591
Lag2_autocovariance   5.6125
Lag3_autocovariance   3.340278
Lag1_autocorrelation_coff   0.859696
Lag2_autocorrelation_coff   0.569556
Lag3_autocorrelation_coff   0.338971
Table 4 marks
Formulas 2 Marks
Calculation 4 Marks
CO- B Explain the idea of simple exponential smoothing in time-series forecasting, and derive 10
1   the component form of its forecasting equation and smoothing equation, interpreting the
meaning of each term.
BL-
Also, write down the equations for Holt’s trend model (double exponential smoothing) and
2   the Holt’s seasonal additive model, and explain in your own words what each term in these
SO-   models represents and how it contributes to the forecast.
1
Synoptic answer:
Idea of Simple Exponential Smoothing (SES) (1 Marks)
Simple Exponential Smoothing is a forecasting technique for data with no trend or seasonality,
where forecasts are weighted averages of past observations, with more weight given to recent
data.
Forecasting Equation (Component Form)
Smoothing Equation (4 Marks)
********** 4 **********
--- page 5 ---
The forecast at time T’ + 1 is equal to a weighted average between the most recent observation
yr and the previous forecast 97:

Iruyr = Wr + (1-e)9q7r-15
where 0 < a < Lis the smoothing parameter. Similarly, we can write the fitted values as
Gera = Me + (1-9 ye
fort = 1,...,T. (Recall that fitted values are simply one-step forecasts of the training data.)

The process has to start somewhere, so we let the first fitted value at time 1 be denoted by f9
(which we will have to estimate). Then

Yon = yi + (1— alo
Gao = Oye + (1— a)Gon
943 = ays + (1— @)9 312

rp = yr +(1—a)ip yo

Urn = or + (1- airy.
Substituting each equation into the following equation, we obtain
Iojp = aya + (1— a) lay; + (1 — a)éo]
= ay + a(1 — a)yr + (1— a)*lo
Gag = ays + (1— a)[ay. + a(1 — a)y: + (1 — a)65]
=ay3 + a(1—a)y + a(1 —a)’y + (1—a)*ly

Tl
Irur = Yall — a)’yp_j + (1- a)? ly.
j-0

The last term becomes tiny for large T. So, the weighted average form leads to the same
forecast Equation (8.1).

Component form

Forecast equation jj, shit = ty
Smoothing equation f= oy + (L- a),

Methods with trend - Holt’s linear trend --- 2.5 Marks

FIC DI EH ar
--- page 6 ---
Holt’s seasonal additive model ---- 2.5 marks
Q3   A A researcher is analyzing a time series representing daily stock prices. The following results   5
CO-   are obtained from the Augmented Dickey-Fuller (ADF) test:
3   •   Test Statistic = −2.45
•   Critical Values:
BL-   1. 1% level = −3.60
4   2. 5% level = −2.93
SO-   3. 10% level = −2.60
1   •   p-value = 0.12
Answer below questions
1.   State the null and alternative hypotheses of the ADF test.
2. Based on the test statistic and critical values, determine whether the series is
stationary or non-stationary at:
• 1% significance level
• 5% significance level
• 10% significance level
3.   Interpret the p-value and explain whether it supports your conclusion.
4. Suggest and justify any transformation that can make the series stationary.
Synoptic Answer
1. Hypotheses: 1 Mark
•   𝐻0: Series is non-stationary (has unit root)
********** 6 **********
--- page 7 ---
•   𝐻1: Series is stationary
2. Decision using Test Statistic: ---(2 marks)
Given ADF = −2.45
•   At 1%: −2.45 > −3.60 → Fail to reject 𝐻0
•   At 5%: −2.45 > −2.93 → Fail to reject 𝐻0
•   At 10%: −2.45 > −2.60 → Fail to reject 𝐻0
Series is non-stationary at all levels
3. p-value Interpretation: (1 mark)
•   p = 0.12 > 0.05 → Not significant
Supports non-stationarity
4. Transformations: (1 mark)
•   First differencing
CO- B Write an appropriate equation in terms of coefficients of AR terms (for ex. Φ), coefficients of 5
3   MA terms (for ex. Θ), white noise (for ex. Є) and back shift notation (for ex. B) for below
BL-   given ARIMA models
ARIMA(3,1,2)(1,2,1)12 and ARIMA (4,2,3).
3
SO-
1
CO- C Explain the idea behind the Maximum Likelihood Estimation (MLE) method for estimating   5
3   parameters of a probability distribution, and describe how it uses observed data to choose the
“most likely” parameter values.
BL-
2
SO-
1
********** 7 **********
--- page 8 ---
Parameter estimation ]

We want to estimate the parameters of an ARMA(p,q) model.
We will assume (for now) that:

1. The model order (p and q) is known, and

2. The data has zero mean.

If (2) is not a reasonable assumption, we can subtract the sample mean 4,
fit a zero-mean ARMA model,

o(B)X; = O(B)Wi,

to the mean-corrected time series X; = Y; — y,
and then use X; + ¥ as the model for Y;.
1 Mark

Parameter estimation: Maximum likelihood estimator

One approach:

Assume that {X,} is Gaussian, that is, (B)X; = 6(B)W;, where W; is
1.i.d. Gaussian.

Choose @;, 4; to maximize the likelihood:
L(é, 6, 0”) = £4,002 (Xi, tee Xn);

where fs 9,2 18 the joint (Gaussian) density for the given ARMA model.
(c.f. choosing the parameters that maximize the probability of the data.)

2 Marks

FIC QF EH 1
--- page 9 ---
2 Marks
CO- D A forecasting model was fitted to daily temperature data. The residuals obtained are:   5
3
BL-   {0.5,−0.3,0.2,−0.1,0.4,−0.2,0.1,−0.4,0.3,−0.2}.
5
The autocorrelation coefficients at lag1 and lag2 are 0.40 and 0.10 respectively.
SO-
Given n=10 and χ20.05,2=5.99, apply the Ljung–Box test to determine whether residuals are
1   significantly uncorrelated up to lag 2 at the 5% significance level.
Synoptic answer:
1. Hypotheses (1 Mark):
•   H0: Residuals are uncorrelated (white noise)
•   H1: Residuals are autocorrelated
2. Test Statistic Formula (1 Mark):
********** 9 **********
--- page 10 ---
Q4   A After first differencing, the following patterns are observed:   5
CO-   • ACF: Significant spikes at lag 1 and lag 2, then cuts off
1   • PACF: Gradual decay
Answer below
BL-   1.   Identify the suitable ARIMA model.
4   2. Explain the reasoning.
SO-
1   Synoptic Answer:
Reasoning (3 Marks)
•   Differenced once → d = 1
• ACF cuts off at lag 2 → MA(2)
• PACF tails off → confirms MA
Model: ARIMA(0,1,2) (2 marks)
CO- B Write a difference between ARMA, ARIMA and SARIMA models. Also, Provide example   5
1   of each with proper set of equations.
BL-
Difference (2 marks)
3
SO-
1   Model   Meaning   Use   Differencing   Seasonality
AutoRegressive   Stationary
ARMA(p,q)   Not required No
Moving Average   data
Non-
ARMA with   ( d )
ARIMA(p,d,q)   stationary   No
Integration   differencing
data
SARIMA(p,d,q)(P,D,   Seasonal   ( d, D )
Seasonal ARIMA   Yes
Q)(_s)   data   differencing
********** 10 **********
--- page 11 ---
CO- C   i.   Explain the idea of time-series regression with a suitable example and a clear   10
3   equation and interpret the meaning of each term in the model.
ii.   Next, describe all the necessary assumptions for linear time-series regression, and
BL-
explain why each assumption is important for valid inference.
2   iii.   Finally, list the main accuracy measures used for this regression, write their
SO-   formulas, and briefly interpret what each measure tells you about the model’s
1   performance.
1. Idea of Time Series Regression (2 Marks)
********** 11 **********
--- page 12 ---
2. Assumptions of Linear Time Series Regression (4 Marks)

1. Linearity (1 Mark):
Relationship between Y; and X;, is linear
— Ensures correct model specification
2. Independence of Errors (1 Mark):
Residuals are not autocorrelated
— Important for unbiased estimates
3. Homoscedasticity (1 Mark):
Constant variance of errors
— Ensures reliable standard errors
4. Normality of Errors (1 Mark):
Errors are normally distributed

— Needed for hypothesis testing

Accuracy Measures (4 Marks)
(a) Mean Squared Error (MSE) (1 Mark)

1   «
MSE = yh -¥,)

— Measures average squared error (penalizes large errors}

(b) R-Square (R’) (1 Mark)

SS he
rR =|- res
S Stat

= Proportion of variance explained by model

(c) Adjusted R-Square (Corrected R?) (0.5 Mark)

_ S8yeq/(n — k — 1)
R=1-|—=—"" __
( S Sto /(n — 1) )

> Adjusts for number of predictors

(d) AIC (Akaike Information Criterion) (0.75 Mark)

AIC = -2In(L) + 2k

e I: Likelihood, k: number of parameters

— Lower AIC = better model (balance of fit & complexity)
(e) BIC (Bayesian Information Criterion) (0.75 Mark)
BIC = —2In(L) + kln(n)

= Stronger penalty for complexity than AIC

FRR ICR] DA KH
--- page 13 ---
Q5   A Write a difference between   5
CO-   1. Autoregression and Multiple regression
2. Autoregression and moving average models
3
BL-
5
SO-
1
CO- B A time series analyst fits the following models:   5
3   •   ARIMA(1,1,1)
BL-   •   ARIMA(2,1,2)
•   ARIMA(3,1,1)
5
The results are:
SO-   • Number of observations 𝑛= 40
1   •   Log-Likelihood = −110
Answer the questions below:
1. Calculate AIC values for all models.
2. Calculate AICc values for all models.
3.   Select the best model based on: AIC and AICc.
4. Comment on whether the selected model changes when using AIC vs AICc.
AIC & AICc Model Selection
********** 13 **********
--- page 14 ---
AICc Calculation (2 Marks):
Model Selection (0.5 Mark):
•   Based on AIC: ARIMA(1,1,1) (lowest = 226)
•   Based on AICc: ARIMA(1,1,1) (lowest = 226.67)
CO- C Write the equation of an ARIMA(3,1,1) model using backshift (B) notation. Then explain the
3   general form of this equation and show how to carry out two-step ahead forecasting. Also 10
explain the concept of interval forecasting in this context.
BL-
2
SO-
1
4 Marks
********** 14 **********
--- page 15 ---
3 Marks
3 marks
Q6   A Describe the below types of graphs with proper diagram and one application of each   10
CO-   1. Time plot
2. Seasonal plot
1
3. Seasonal sub series plot
BL-   4. LAG plot
2
SO-
1. Time Plot (2.5 Marks)
1   Description (1.5 Marks):
A time plot represents the values of a time series against time in chronological order. It helps
in identifying patterns such as trend, seasonality, and irregular fluctuations.
Application (1 Mark):
Used for analyzing stock prices, temperature changes, and sales trends over time.
2. Seasonal Plot (2.5 Marks)
Description (1.5 Marks):
A seasonal plot shows data for each season (e.g., months or quarters) across different years,
allowing comparison of seasonal patterns and variations.
Application (1 Mark):
Used in monthly or quarterly sales analysis to compare seasonal behavior across years.
3. Seasonal Subseries Plot (2.5 Marks)
Description (1.5 Marks):
This plot groups observations by season and displays them along with their averages, helping
to analyze variation within each season and consistency across years.
********** 15 **********
--- page 16 ---
Application (1 Mark):
Used to study monthly demand patterns and detect stable or changing seasonal effects.
4. Lag Plot (2.5 Marks)
Description (1.5 Marks):
A lag plot displays the relationship between a time series and its lagged values (Yt vs Yt−k)
helping to detect autocorrelation and underlying structure.
Application (1 Mark):
Used to identify randomness or dependence in data and assist in selecting appropriate AR
models.
CO- B   i.   Explain the concept of Grouped Time Series.   10
4   ii.   How is it different from hierarchical time series?
iii.   Illustrate with an example showing multiple aggregation paths
BL-
iv.   Explain the challenges involved in forecasting grouped data.
2
SO-   Synoptic ANS:
1
1. Concept of Grouped Time Series (3 Marks)
Grouped Time Series refers to a collection of time series that are organized across multiple
grouping variables, where each observation can belong to more than one group
simultaneously.
•   Unlike simple structures, data can be aggregated along different dimensions (e.g.,
region, product, category).
•   It results in overlapping group structures rather than a single hierarchy.
2. Difference from Hierarchical Time Series (3 Marks)
Basis   Hierarchical Time Series   Grouped Time Series
Structure (1 Mark)   Tree-like (single path)   Network-like (multiple paths)
Aggregation (1 Mark)   One parent per node   Multiple aggregation paths
Region & Product grouping
Example (1 Mark)   Country → State → City
simultaneously
3. Example with Multiple Aggregation Paths (2 Marks)
Consider sales data classified by:
•   Region: North, South
•   Product: A, B
Series formed:
•   Total Sales
•   Region-wise: North, South
•   Product-wise: A, B
•   Combined: North-A, North-B, South-A, South-B
********** 16 **********
--- page 17 ---
Example: North-A sales contribute to:
•   Total Sales
•   North Region total
•   Product A total
This shows multiple aggregation paths, a key feature of grouped time series.
4. Challenges in Forecasting Grouped Data (2 Marks)
1. Aggregation Inconsistency: Forecasts at different levels may not match totals
2. Complex Dependencies: Same data affects multiple groups
3. Model Complexity: Requires reconciliation methods (bottom-up, top-down, optimal
combination)
Q7   A What is forecast reconciliation? Explain why it is necessary in hierarchical and grouped time 10
CO-   series forecasting. Discuss how reconciliation improves forecast accuracy and business
consistency with suitable explanation.
4
BL-
2   1. Definition of Forecast Reconciliation (2 Marks)
SO-   Forecast reconciliation is the process of adjusting independently generated forecasts at
different levels of a hierarchy or groups so that they become consistent (coherent) with
1   aggregation constraints.
That is, lower-level forecasts add up exactly to higher-level forecasts.
2. Need for Reconciliation in Hierarchical & Grouped Time Series (4 Marks)
1. Aggregation Consistency (1 Mark):
Independent forecasts may not sum correctly across levels (e.g., regional ≠ total).
2. Multiple Aggregation Paths (1 Mark):
In grouped time series, one series contributes to multiple groups, causing
inconsistencies.
3. Avoid Conflicting Forecasts (1 Mark):
Different levels may give contradictory results if not reconciled.
4. Business Requirement (1 Mark):
Organizations need a single consistent forecast for planning and decision-making.
3. How Reconciliation Improves Forecast Accuracy (2 Marks)
1. Combines Information (1 Mark):
Uses information from all levels (top-down + bottom-up), improving prediction
quality.
2. Reduces Errors (1 Mark):
Optimal combination methods reduce variance and improve overall forecast
accuracy.
4. Improvement in Business Consistency (2 Marks)
1. Unified Planning (1 Mark):
Same forecast is used across departments (sales, finance, operations).
2.   Better Decision Making (1 Mark):
Ensures proper inventory control, budgeting, and resource allocation.
CO- B Explain below with all set of equations in detail   10
4   1. Prophet Model
2. Vector auto regression
********** 17 **********
--- page 18 ---
BL-
2   1. Prophet Model (5 Marks)
SO-
(a) Idea (1 Mark):
1
The Prophet model is an additive time series model that decomposes data into trend,
seasonality, and holiday effects, suitable for business time series with strong seasonal
patterns.
2. Vector Auto Regression (VAR) (5 Marks)
(a) Idea (1 Mark):
VAR models multiple time series variables together, where each variable depends on its own
past values and past values of other variables.
********** 18 **********
--- page 19 ---
(d) Interpretation (1 Mark):
•   Each variable depends on its own past + others’ past
•   Captures interdependence between multiple time series
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper aa284d55a2dd

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_AI_7051/Applied Time Series Analysis/ANS_Applied Time Series Analysis(702DB0E007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: mixed (18 pages), mean OCR confidence 76.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (ARTIFICIALINTELLIGENCE)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Applied Time Series Analysis
Date: 10 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly
CO-1 A Explain the basic steps in time series forecasting in brief.   5
BL-2
SO-1
Each Step --- 1 marks
Total --- 5 marks
CO-1 B Given the quarterly time series data below, compute the seasonal indices using 5
BL-3   the simple average method.
SO-1   Year   Q1   Q2   Q3   Q4
2010   50   60   70   65
2011   55   65   75   70
2012   60   70   80   75
2013   65   75   85   80
Year   Q1   Q2   Q3   Q4
2010   50   60   70   65
2011   55   65   75   70
2012   60   70   80   75
2013   65   75   85   80
Season wise
avg   57.5   67.5   77.5   72.5
********** 1 **********
--- page 2 ---
Over all
AVG   68.75
Seasonal
Index   0.836364   0.981818   1.127273   1.054545
Calculation table --- 3 marks
Calculation of the solution – 2 Marks
CO-3 C Explain seasonal differencing in time series. Also explain its importance in time   5
BL-2   series forecasting.
SO-1   Seasonal Differencing (2 Marks):
Seasonal differencing is a method used to remove seasonality from a time series
by subtracting the value of the same period in the previous season. It is
mathematically given as:
Yt′ = Yt−Yt−s
where s is the seasonal period (e.g., s=12 for monthly data with yearly
seasonality). This transformation helps eliminate repeating seasonal patterns.
Importance in Time Series Forecasting (3 Marks):
•   It helps to make the time series stationary, which is required for models
like ARIMA/SARIMA.
•   It removes seasonal fluctuations, improving model accuracy.
•   It makes patterns in ACF and PACF clearer, aiding in model identification
and parameter selection.
CO-3 D Derive the equation of Augmented Dickey–Fuller (ADF) model type 1 using the   5
BL-2   ARIMA(1,0,0).
SO-1
********** 2 **********
--- page 3 ---
Q2   A Consider the time series:   10
CO-3   𝑋= [5,6,7,9,11,10,12,14,13,15,16,14]
BL-3   Then
SO-1   1. Compute the mean and variance.
2. Calculate autocovariance at lag1, lag2 and lag3.
3. Compute autocorrelation coefficients at lag 1, lag 2 and lag3.
4. Comment on whether the series shows positive correlation.
[You may use MS excel for solving the above question and write every step of
calculation.]
xt-   xt-   (xt-   xt-   xt-   xt-
xt-   Xt-   xba   xt-   xt-2 3*x xba   xba   xbar   xbar
Xt   Xt-1 2   3   r   1 -   -   bar   r)2   r *   *   * xt-
********** 3 **********
--- page 4 ---
xb xba   xt-1   xt-2   3 -
ar   r   -   -   xbar
xba   xbar
r
5   -6   36
6   5   -5   -6   25   30
7   6   5   -4   -5   -6   16   20   24
9   7   6   5   -2   -4   -5   -6   4   8   10   12
11   9   7   6   0   -2   -4   -5   0   0   0   0
10   11   9   7   -1   0   -2   -4   1   0   2   4
12   10   11   9   1   -1   0   -2   1   -1   0   -2
14   12   10   11   3   1   -1   0   9   3   -3   0
13   14   12   10   2   3   1   -1   4   6   2   -2
15   13   14   12   4   2   3   1   16   8   12   4
16   15   13   14   5   4   2   3   25   20   10   15
14   16   15   13   3   5   4   2   9   15   12   6
-------6 Marks
xbar   11
SUM((xt-xbar)2)   146
Variance of Xt   12.17
SUM(xt-xbar * xt-1 - xbar)   109
SUM(xt-xbar * xt-2 - xbar)   69
Lag1_autocovariance   9.909
Lag2_autocovariance   6.9
Lag3_autocovariance   4.111
Lag1_autocorrelation_coff   0.814
Lag2_autocorrelation_coff   0.567
Lag3_autocorrelation_coff   0.338
------ 4 Marks
CO-1 B Compare exponential smoothing and multiple linear regression as forecasting 10
BL-2   techniques for time series data. Discuss their advantages and limitations, model
SO-1   complexity, assumptions, and suitability for different time series components.
1. Exponential Smoothing (3 Marks)
• Advantages: Simple, less data required, good for short-term forecasting
•   Disadvantages: Cannot include external variables, limited for complex
patterns
• Complexity: Low
********** 4 **********
--- page 5 ---
•   Suitability: Works well for level, trend, seasonality (univariate data)
2. Multiple Linear Regression (3 Marks)
• Advantages: Handles multiple predictors, flexible
•   Disadvantages: Sensitive to multicollinearity, requires assumptions
• Complexity: High
•   Suitability: Useful when external variables influence the series
3. Assumptions (2 Marks)
•   Exponential Smoothing: Smooth structure, no strong randomness
•   Regression: Linearity, independence, homoscedasticity, no
multicollinearity
4. Model Complexity & Comparison (2 Marks)
•   Exponential smoothing → Simple, fewer parameters
•   Regression → Complex, multiple coefficients
Q3   A A data analyst is examining a time series of weekly commodity prices. The results 5
CO-3   obtained from the Augmented Dickey-Fuller (ADF) test are as follows:
BL-4   • ADF Test Statistic = −3.05
SO-1   •   Critical Values:
• 1% level = −3.75
• 5% level = −3.00
• 10% level = −2.65
•   p-value = 0.04
Answer the following:
1. Formulate the null and alternative hypotheses for the ADF test.
2. Using the test statistic and critical values, decide whether the series is
stationary at:
• 1% level of significance
• 5% level of significance
• 10% level of significance
3. Analyze the p-value and discuss whether it confirms your decision.
4. If the series were non-stationary, suggest appropriate transformations to
achieve stationarity and justify your choice.
Hypotheses: 1Mark
•   H₀: The series has a unit root (non-stationary)
•   H₁: The series is stationary
Decision (Test Statistic = −3.05): 2 Marks
********** 5 **********
--- page 6 ---
• At 1%: −3.05 > −3.75 → Do not reject H₀ → Non-stationary
• At 5%: −3.05 < −3.00 → Reject H₀ → Stationary
• At 10%: −3.05 < −2.65 → Reject H₀ → Stationary
p-value Interpretation: 1 Mark
p-value = 0.04 < 0.05 → Reject H₀ → Supports stationarity (at 5% level)
Conclusion & Transformation: 1 Mark
The series is stationary at 5% and 10% levels but not at 1%.
If non-stationary, apply first differencing or log-differencing to achieve
stationarity.
CO-3 B Write an appropriate equation in terms of coefficients of AR terms (for ex. Φ), 5
BL-3   coefficients of MA terms (for ex. Θ), white noise (for ex. Є) and back shift notation
SO-1   (for ex. B) for below given ARIMA models
ARIMA(2,1,3)(2,1,2)12 and ARIMA (3,1,2).
3 Marks
2 Marks
CO-3 C Write equation of Augmented Dickey–Fuller (ADF) type 0, type 1 and type 2 5
BL-2   models and explain significance of each term in those equations.
SO-1
********** 6 **********
--- page 7 ---
CO-3 D After fitting an ARIMA model to monthly sales data, the following residuals were 5
BL-5   obtained:
SO-1   {0.6, −0.4, 0.3, −0.2, 0.5, −0.3, 0.2, −0.5, 0.4, −0.1}.
The autocorrelation coefficients at lag 1 and lag 2 are 0.35 and 0.15 respectively.
Given n=10 and χ0.05,2 2   = 5.99 , use the Ljung–Box test to check if residuals are
uncorrelated up to lag 2 at the 5% significance level.
Fail to reject H0
Conclusion (1 Mark)
Residuals are uncorrelated (white noise) up to lag 2. The ARIMA model is
adequate.
********** 7 **********
--- page 8 ---
Q4   A After applying first-order differencing to a time series, the following observations 5
CO-1   are made:
BL-4   • ACF: Shows a gradual decay over several lags
SO-1   • PACF: Displays significant spikes at lag 1 and lag 2, then cuts off
Answer the following:
1. Suggest an appropriate ARIMA model for the series.
2. Justify your choice based on the behavior of ACF and PACF plots.
1. Identified Model (2 Marks)
ARIMA(2,1,0)
2. Reasoning (3 Marks)
•   First differencing applied → d = 1
• PACF cuts off after lag 2 → indicates AR(2) component
• ACF shows gradual decay → supports AR model
• No sharp cutoff in ACF → no MA component (q = 0)
CO-1 B Explain the Diagnostic checking test of residuals after forecasting by an ARIMA   5
BL-3   model. Also write the need of this test.
SO-1
Diagnostic Checking of Residuals in ARIMA (3 Marks):
After fitting an ARIMA model, diagnostic checking is performed on the residuals
(errors) to verify whether the model is adequate. Ideally, residuals should behave
like white noise (i.e., no autocorrelation, constant variance, and zero mean). The
main checks include:
•   Autocorrelation Check: Using ACF/PACF plots of residuals to ensure no
significant autocorrelation remains.
•   Statistical Test: The Ljung–Box test is commonly used to test whether
residuals are independently distributed (no autocorrelation).
• Normality Check: Residuals are checked (via histogram or Q-Q plot) to
see if they follow a normal distribution.
If residuals show patterns, the model is not adequate and needs refinement.
Need/Importance of Diagnostic Test (2 Marks):
• To ensure the model has captured all the information in the data.
• To validate that residuals are random (white noise), confirming model
adequacy.
• To improve forecasting accuracy by identifying model misspecification.
CO-3 C A company aims to forecast quarterly demand for its product using multiple   10
BL-2   influencing factors such as product price, marketing budget, and seasonal
SO-1   discounts.
Data available:
• Demand: Quarterly demand values
•   Price: Product price for each quarter
• Marketing_Expense: Quarterly marketing expenditure
•   Discount: Seasonal discount offered
Answer the following:
********** 8 **********
--- page 9 ---
1. Describe the steps involved in building a predictive model for forecasting
demand.
2. Explain how you would select the most relevant predictor variables for the
model.
3. Discuss any two performance metrics you would use to evaluate the
accuracy of the model.
1. Steps to Build the Model (4 Marks)
• Data Preparation: Handle missing values, outliers, and scale variables
•   Exploratory Analysis: Check relationships between demand and predictors
• Model Selection: Use multiple linear regression or suitable model
• Model Training: Fit the model using historical data
•   Validation: Split data into train-test or use cross-validation
2. Selection of Predictor Variables (3 Marks)
• Use correlation analysis to identify strong relationships
• Apply statistical tests (p-values) to check significance
• Remove variables causing multicollinearity (VIF check)
• Use methods like stepwise regression or regularization
3. Evaluation Metrics (3 Marks)
• Mean Squared Error (MSE):
Measures average squared difference between actual and predicted values
→ Lower value indicates better model
• R² (Coefficient of Determination):
Measures proportion of variance explained by model
→ Value closer to 1 indicates better fit
Q5   A Explain SARIMA model with proper set of equations. Give proper significance of 5
CO-3   each parameter of the same model.
BL-5
SO-1
********** 9 **********
--- page 10 ---
CO-3 B A researcher fits three competing time series models to quarterly demand data. 5
BL-5   The estimated number of parameters (including variance) and log-likelihood
SO-1   values are given below:
Model   Parameters (k)   Log-Likelihood
Model A   3   − 95
Model B   5   − 90
Model C   7   − 88
The total number of observations is n=30.
Answer the following:
1. Calculate the Akaike Information Criterion (AIC) for each model.
2. Calculate the Corrected AIC (AICc) for each model.
3. Determine the most suitable model based on AIC and AICc.
4. Explain why AICc is preferred over AIC for small sample sizes.
Parameters
Model   Log-Likelihood   AIC   AICc
(k)
Model A   3   -95   196   196.9231
Model B   5   -90   190   192.5
Model C   7   -88   190   195.0909
---------3 marks
********** 10 **********
--- page 11 ---
Model selection changes slightly → AICc prefers Model B due to penalty for
more parameters.
AICc is more reliable for small sample sizes.
---- 2 Marks
CO-3 C A time series analyst models a dataset using an ARIMA(2,1,2) process.   10
BL-2
SO-1   1. Write the model equation using backshift (B) operator notation.
2. Describe the general structure of the ARIMA model, including AR, I, and
MA components.
3. Demonstrate how to obtain a two-step ahead forecast from the model.
4. Explain the idea of prediction intervals (interval forecasting) and their
importance in time series forecasting.
---- 2 marks
----- 2 Marks
********** 11 **********
--- page 12 ---
Step 2: Expand the Equation
First expand the left-hand side:

(1— dB — ¢2B’ — B+ $1 B? + b2B*)y,
Now rearrange terms:

[1 — (1+ 4:)B + (d; — $2) B? + dB |y,

Step 3: Convert into Time Domain

Replace backshift terms with actual time values:
ye — (1+ diya t+ (b1 — b2)yr-2 + boys = er + Orera + Boe1-2
Rewriting:

ye = (1+ di)y1 — (b1 — $2)y-2 — Goes + r+ O1era + B2€1-2

Step 4: Two-Step Ahead Forecast Equation

To forecast yr+2, write:

yrs2 = (1+ d:)yrsi — (b1 — da) yr — doyr1 + ersa + Hers + borer

Step 5: Take Expectations (Forecasting Step)

For forecasting, we assume future errors are zero:
ers = €T12 = 0

So the final forecast becomes:

Orszir = (1+ br)Grsyr — (¢1 — b2)yr — doyr-1 + O2€7

4 marks

Assuming €; ~ N(0, a?)

95% prediction interval
Vrenit 1.96, Vrsnjr
where vy4p)7 is estimated forecast variance.

B Vy+1\7 = 6? for all ARIMA models

= Multi-step prediction intervals for ARIMA(0,0,q):
q

Ye = et + > b.¢-i-
i=1
h-1
Vrjteh = 67 [+ Sa. forh=2,3,....
i=1

---- 2 Marks

FRR ICR] DA KH
--- page 13 ---
Q6   A A company wants to estimate monthly demand for its product to improve   10
CO-1   inventory planning. To reduce fluctuations in the data, they use the Simple
BL-2   Moving Average (SMA) method with a 4-month window.
SO-1
The monthly demand data for the last 12 months (in units) is given below:
Demand = [120, 130, 125, 135, 140, 145, 150, 155, 160, 165, 170, 175]
(Here, 175 represents the most recent month)
Answer the following:
1. Calculate the Simple Moving Average (SMA) for all possible months
using a 4-month window.
2. State any two advantages of the Simple Moving Average method.
3. State any two limitations of the Simple Moving Average method.
4. Explain how the results would change if a 6-month window is used
instead of a 4-month window.
2. Advantages (2 Marks)
• Simple and easy to compute
• Smooths short-term fluctuations
3. Limitations (2 Marks)
• Gives equal weight to all observations
• Lags behind actual trend
4. Effect of 6-Month Window (2 Marks)
• Produces smoother values
• More lag in response to changes
• Reduces noise but may miss short-term variations
********** 13 **********
--- page 14 ---
CO-4 B Explain the concepts of hierarchical time series and grouped time series with 10
BL-2   the help of a suitable tree structure. Describe the bottom-up forecasting
SO-1   approach with an example and compare it with the top-down approach. Also,
briefly explain the concept of forecast reconciliation using matrix
representation.
1. Hierarchical & Grouped Time Series (3 Marks)
•   Hierarchical Time Series:
Data organized in a tree-like structure (e.g., Total Sales → Region →
City).
Each level aggregates the lower levels.
• Grouped Time Series:
Data grouped in multiple ways (not strictly hierarchical), e.g., by
region and product category simultaneously.
Tree Example:
Total Sales
├── Region A
│ ├── City 1
│ └── City 2
└── Region B
├── City 3
└── City 4
2. Bottom-Up Approach (2 Marks)
•   Forecast is generated at the lowest level (disaggregated level)
• Then aggregated upward
Example:
Forecast sales for each city, then sum to get region and total sales
More accurate at detailed level
Requires large data and may accumulate noise
3.Top-Down Approach (2 Marks)
•   Forecast is made at the top level
• Then distributed to lower levels using proportions
Example:
Forecast total sales, then allocate to regions based on past ratios
Simple and less data required
Less accurate at lower levels
4. Forecast Reconciliation (3 Marks)
• Ensures forecasts at all levels are consistent (coherent)
********** 14 **********
--- page 15 ---
Adjusts forecasts so that:
Sum of lower levels = higher level forecast
Q7   A Consider the following hierarchical time series structure shown in figure   10
CO-4   below:
BL-2
SO-1   • Level 0: Total
• Level 1: Group A and Group B
• Level 2: Subgroups under A (AA, AB, AC) and under B (BA, BB)
The forecast on the each level is
𝑌̂Total,t = 1000 ,
𝑌̂A,t = 650 , 𝑌̂B,t = 400 ,
𝑌̂AA,t = 300, 𝑌̂AB,t = 250 , 𝑌̂AC,t = 150 , 𝑌̂AA,t = 200, 𝑌̂AB,t = 250
1. Identify the incoherence at each level of the hierarchy. (3 marks)
2. Apply the proportional reconciliation method to adjust forecasts at each
level so that the final forecasts become coherent with the total of 1000. (7
marks)
********** 15 **********
--- page 16 ---
Hierarchical Structure:
* Level 0: Total
* Level 1: Group A and Group B

* Level 2: Subgroups under A (AA, AB, AC) and under B (BA, BB)

Step 1: Non-Coherent | | Forecasts
Let's assume we have the following non-coherent forecasts:

* Total Forecast:

Yrrotae = 1000

* Level 1 (Groups A and B):
Yas = 650
Ype = 400

(Note: The sum of these forecasts is 650 + 400 = 1050, which exceeds the Total forecast of

1000. Hence, they are non-coherent.)

* Level 2 (Subgroups under A and B):

*° Group A:
Vary = 300
Yapy = 250
Yaou = 150

(Sum = 300 + 250 + 150 = 700, which does not match Group A's forecast of 650.)

* Group B:
Yeas = 200
Yops = 250

(Sum = 200 + 250 = 450, which does not match Group B's forecast of 400.)

-1.5M

Step 2: Proportion Calculation to Achieve Coherence

1. Adjust Level 1 Forecasts (Group A and B)
To make the forecasts coherent, we need to redistribute the forecasts for Groups A and B based on

their initial proportions.

Calculate Proportions for Level 1:

* The total initial forecast for Level 1 is 650 + 400 = 1050.

Proportions:

Yau 50

Py = = 22° ~ 0.619
1050 1050

Py — 2B — 400 ~ 9 381
1050 1050

Adjust Forecasts: Now, we adjust the forecasts for Group A and Group B to match the Total forecast
of 1000:

Yau = Pa < Vrovae = 0.619 x 1000 © 619

Yau = Pe = Yroae = 0-381 x 1000 ~ 381

FRR ICR 7 6 AC OH
--- page 17 ---
------2M
-----3M
CO-4 B Define complex seasonality and distinguish it from simple seasonality. Also,   10
BL-2
explain the concept of Vector Autoregression (VAR) and highlight how it
SO-1
differs from other time series models.
1. Complex vs Simple Seasonality (4 Marks)
• Simple Seasonality:
o Single repeating pattern at a fixed interval
o Example: Monthly data with yearly seasonality (period = 12)
o Easy to model using standard seasonal methods (e.g., SARIMA)
• Complex Seasonality:
o Multiple seasonal patterns present simultaneously
o Example: Daily data with weekly + yearly seasonality
********** 17 **********
--- page 18 ---
o More difficult to model
Difference:
• Simple → one seasonal cycle
• Complex → multiple overlapping seasonal cycles
2. Vector Autoregression (VAR) (3 Marks)
• VAR is a multivariate time series model
• Each variable depends on its own past values and past values of other
variables
General form:
3. Difference from Other Time Series Models (3 Marks)
• ARIMA:
o Univariate (single variable)
o Does not capture interaction between variables
• VAR:
o Multivariate
o Captures interdependence among variables
********** 18 **********
````
