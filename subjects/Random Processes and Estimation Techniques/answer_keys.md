# Random Processes and Estimation Techniques: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 4356ac342a51

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AIML_7053/Random Processes and Estimation Techniques/ANS_Random Processes and Estimation Techniques(702AI0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (18 pages), mean OCR confidence 73.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Random Processes and Estimation Techniques
Date: 03 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
a.   [04]
CO- 1;
SO- 1;   Define strict sense stationary process and wide sense stationary process
BL-1
Ans. A strict-sense stationary process (SSS) is one where the entire probability
distribution is time-invariant, meaning the statistical properties do not change
over time. A wide-sense stationary process (WSS), also known as weak-sense
stationary, is a less strict condition where the mean is constant and the
autocorrelation function only depends on the time difference between two
points. All SSS processes are WSS, but the reverse is not always true.
********** 1 **********
--- page 2 ---
b.   State the following types of systems and provide one example for each of   [04]
CO- 2;   them.
SO- 1;
BL-2   (i)   Linear systems
(ii)   Memoryless systems
Ans.
********** 2 **********
--- page 3 ---
c.   Explain Bernoulli process. In a sequence of independent Bernoulli trials,   [04]
CO-3;   where the probability of success (p) is 0.4, explain what it means to say that
SO-1;
BL-2   the sixth success occurs on the tenth trial.
Ans. A Bernoulli process is a sequence of independent and identical experiments
(called Bernoulli trials) where:
• Each trial has two possible outcomes — Success (S) or Failure (F).
• The probability of success (p) remains constant for every trial.
• The outcome of one trial does not affect the outcome of another
(independent trials).
There is about a 6.7% chance that in this Bernoulli process (where each trial
has a 40% chance of success), the 6th success will occur exactly on the 10th
trial — meaning we got 5 successes in the first 9 trials and one more success
on the 10th.
d   A researcher wants to estimate the average monthly salary of employees in a   [04]
large IT based company. She collects data from a random sample of 50
employees. While reviewing her methods, she wants to ensure that the
CO-4;
SO-1 ;   estimator she uses (e.g., sample mean) is reliable and accurate. Explain the
BL-2   criteria that the researcher should consider when selecting a good estimator.
For each criterion, give an example in the context of this salary survey.
********** 3 **********
--- page 4 ---
Ans
CO- 5;   e   [04]
SO- 1;   Explain type I and type II errors with proper examples.
BL-2
Ans.
Q2   a   A random process is given by 𝑥(𝑡) = 𝐴𝑐𝑜𝑠(𝑤𝑜𝑡+ 𝜃) where 𝐴 and 𝑤𝑜 are   [10]
CO-1;   constants and θ is a uniformly distributed random variable over the interval
SO-1;
BL-5   (0, 2π). Prove that the given process is wide sense stationary process.
********** 4 **********
--- page 5 ---
Ans. Solution: Given X(t) = Acos(wot + @); where A and wy are constants and
0 — (0,27); fo(@) = x. The 0 is uniformly distributed between 0 to 27. The
distribution shown in Fig. 7.12.

fo
4°)

1/211

~
0 ano

Fig. 7.7

If mean value and auto correlation function of r.p is a function of time, ‘t’ then it is
not stationary.

1. Expectation or mean value:

__ Qa
BIx(] =X = [ x(t) fo(0)d0

=0
Qa 1
a | A cos(wot + 6).—dé
9 20

=0
2a

=— cos(wot + 0)d0
2m Jo-o
A,. :

on 2, Bin(wot + Ayla"
A... .

= 37 Bin (wot + 27) — sin wot]

A,. ,
= —[sin wot — sin wot]
20

=0

-. E[X (t)] = X(t) = 0. It is constant.

FIC DI EH ar
--- page 6 ---
b   Let X(t) be a wide-sense stationary (WSS) random process with   [10]
autocorrelation function
− (| 10) 𝜏|
CO-2;   𝑅𝑥𝑥(𝜏) = (0.66) . 𝑒
SO-1;
BL-3
Solve for the Power Spectral Density (PSD) 𝑆𝑥𝑥(𝜔) of the process. Also
identify the value of 𝑆𝑥𝑥(𝜔) at 𝜔= 0.1.
********** 6 **********
--- page 7 ---
Ans.
a   For the given random process by   [10]
Q3
CO-1;   𝑥(𝑡) = 𝑐𝑜𝑠(𝑡+ 𝜃)
SO-1;   where 𝜃 is a random variable uniformly distributed over the interval (0, 2π).
BL-3
Solve and check if the given random process is mean-ergodic or not?
Ans
********** 7 **********
--- page 8 ---
b   Explain the power spectral density function (or spectral density or power   [10]
spectrum) of a stationary process.
The power spectrum density function of a zero mean WSS process X(t) is
CO-2;
SO-1;   given by
BL-2,3
{1,   |𝑤} < 𝑤𝑜
𝑆𝑋𝑋(𝑤) =
0,   𝑒𝑙𝑠𝑒𝑤ℎ𝑒𝑟𝑒
Solve for the autocorrelation function.
Ans
********** 8 **********
--- page 9 ---
a   The transition probability matrix of a Markov chain {Xn}n=1,2,3,….. with three   [10]
states as follows.
0.2 0.5 0.3
𝑃= [ 0.5 0.4 0.1 ]
0.3 0.4 0.3
Q4
The initial distribution is
CO-3 ;
SO- 1;
BL-3   𝑃0 = [0.6 0.3 0.1]
Solve for:
(i)   P (X2 = 3)
(ii)   P (X2 = 2)
(iii)   P [X3 = 2, X2 = 3, X1 = 3, X0 = 2]
********** 9 **********
--- page 10 ---
Ans.
b   An auto company decided to introduce a new six-cylinder car whose mean   [10]
petrol consumption is claimed to be lower than that of existing auto engine. It
CO-5 ;   was found that the mean petrol consumption for 50 cars was 10 km/litre with
SO- 1;
BL-4   a standard deviation of 3.5 km per litre. Test for the company at 5% level of
significance, the claim that in the new petrol consumption is 9.5 km per litre
on average.
********** 10 **********
--- page 11 ---
Ans.
a   Explain how the good estimate of the population standard deviation 𝜎 is   [10]
Q5   obtained for a random sample 𝑥1, 𝑥2, … , 𝑥𝑛from a normal distribution using
CO-4;   maximum likelihood estimator (MLE). State any assumptions you use (e.g.
SO-1;
BL-2   whether the mean 𝜇is known or unknown) and give the final expression for
the MLE of 𝜎.
Ans.
********** 11 **********
--- page 12 ---
b   A market research company wants to know if the proportion of people   [10]
shopping online has increased. In a survey conducted last year, 220 out of 500
CO- 5;   respondents said they preferred online shopping. In a survey conducted this
SO- 1;   year, 290 out of 520 respondents said they preferred online shopping.
BL-4   Test for 1% level of significance, whether there has been an increase in the
proportion of people who prefer online shopping.
Ans.
********** 12 **********
--- page 13 ---
a   The Westview High School nurse is interested in knowing the average height   [10]
of seniors at this school, but she does not have enough time to examine the
records of all 430 seniors. She randomly selects 48 students and finds the
sample mean to be 64.5 inches and the sample standard deviation to be 2.3
inches.
Q6   Solve for:
CO-4;   (i)   the estimated standard error of the mean.
SO-1;
BL-3   (ii)   Construct a 90% confidence interval for the mean height of all
seniors at Westview High School.
(iii)   Suppose the Nurse wants to reduce the chances of errors in her
estimates, what should she do.
(iv)   Apply your understanding of estimation principles to suggest
what Nurse can do to reduce the chances of errors in her
estimates.
********** 13 **********
--- page 14 ---
Ans.
• To reduce sampling error and get more precise estimates, the nurse
should increase the sample size.
•   Justification: The standard error is inversely proportional to the
square root of the sample size:
So, larger n → smaller , SE → narrower confidence interval → more
accurate estimate of the population mean.
--------(3M)
b   Let x be a random variable that represents weight loss (in pounds) after   [10]
following a certain diet for 6 months. After extensive study, it is found that x
CO-5 ;   has a normal distribution with σ = 5.7 pounds. A new modification of the diet
SO- 1;
BL-4   has been implemented. A random sample of n=21 people use the modified diet
for 6 months. For these people, the sample standard deviation of weight loss
is s= 4.1 pounds.
********** 14 **********
--- page 15 ---
Test at 1% level of significance, does this result indicate that the variance of
weight loss for the modified diet is different (either way) from the variance of
weight loss for the original diet. Assume weight loss for each diet follows a
normal distribution
Ans.
Q7   a   [10]
Suppose that customers arrive at a bank according to a poisson process with a
CO-3;
SO-1;   mean rate of 3 per minute.
BL-3
********** 15 **********
--- page 16 ---
Solve for the probability that during a time interval of 2 min
(i)   exactly 4 customers arrive
(ii)   more than 4 customers arrive
(iii)   fewer than 4 customer in 2 minute interval.
Ans.
********** 16 **********
--- page 17 ---
b   A consumer electronics lab compared the battery life of two brands of   [10]
smartphones.
• For Brand X, a sample of 10 phones gave an average battery life of
18.5 hours with a standard deviation of 2.1 hours.
CO-5 ;
SO- 1;   • For Brand Y, a sample of 8 phones gave an average battery life of
BL- 4   20.9 hours with a standard deviation of 1.8 hours.
At the 1% level of significance, test whether Brand X has lower average battery
life than Brand Y.
Ans.
-------(1M)
Pooled variance
********** 17 **********
--- page 18 ---
2 (m —1)s7 + (m2 — 1)85
? ny +n2—2
Substitute values:

Co (10 — 1)(2.1)? + (8 — 1)(1.8)?

? 10+8-2
_ 9(4.41) +7(3.24) _ 39.69+ 22.68 62.37 _
a = Tp 7 38981

5, = V3.8981 = 1.9743
(3M)

Standard error (for difference in means)

1 4.
SE = 8)\/ — + —
ny nz

= 1.9743 x = 1.9743 x V0.225 — 1.9743 x 0.4743 = 0.9366

-——-(2M)

Test statistic
Z1—Z2_ 185-209 -24 _
SE 0.9366 0.9366

$=

—2.562

Degrees of freedom:

df —n, +n.—2-—16

For one-tailed test at a — 0.01 anddf = 16:
teritical = —2.583
Compare:
tealculated = —2.562 > —2.583

So, we fail to reject Hp at the 1% level (just barely — it’s very close).

At a 5% level, we would reject Ho.
=—~-(2M)

FR ICR 7] QA HH
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper c9fb2c81876d

- Departments: AI and Machine Learning, Artificial Intelligence
- Programmes: BTech AI 7012, BTech AIML 7053, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AIML_7053/Random Processes and Estimation Techniques/ANS_Random Processes and Estimation Techniques(702AI0C024)_2025-2026_c9fb2c8187.pdf` (+2 identical copies)
- Printed on paper: max marks: 100
- Text: mixed (20 pages), mean OCR confidence 66.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025
Program: B. Tech.   Stream: AIML   Year: II   Semester: III
Subject: Random Processes and Estimation Techniques   Time: _____ hrs (______to_______)
Date:   /   / 2024   No. of Pages:
Marks: 100
Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
1) Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Q1
Answer briefly:
a.   [04]
CO- 1;
SO- 1;   Define strict sense stationary process and wide sense stationary process
BL-1
Ans. A strict-sense stationary process (SSS) is one where the entire probability
distribution is time-invariant, meaning the statistical properties do not change
over time. A wide-sense stationary process (WSS), also known as weak-sense
stationary, is a less strict condition where the mean is constant and the
autocorrelation function only depends on the time difference between two
points. All SSS processes are WSS, but the reverse is not always true.
1
--- page 2 ---
CO- 2;   b.   State the following types of systems and provide one example for each of them.   [04]
SO- 1;   (i)   Linear systems
BL-2   (ii)   Memoryless systems
Ans.
2
--- page 3 ---
c.   Explain Bernoulli process. In a sequence of independent Bernoulli trials, where   [04]
CO-3;   the probability of success (p) is 0.4, explain what it means to say that the sixth
SO-1;
BL-2   success occurs on the tenth trial.
Ans. A Bernoulli process is a sequence of independent and identical experiments
(called Bernoulli trials) where:
• Each trial has two possible outcomes — Success (S) or Failure (F).
• The probability of success (p) remains constant for every trial.
• The outcome of one trial does not affect the outcome of another
(independent trials).
There is about a 6.7% chance that in this Bernoulli process (where each trial has
a 40% chance of success), the 6th success will occur exactly on the 10th trial
— meaning we got 5 successes in the first 9 trials and one more success on the
10th.
d   A researcher wants to estimate the average monthly salary of employees in a   [04]
CO-4;
SO-1 ;   large IT based company. She collects data from a random sample of 50
BL-2   employees. While reviewing her methods, she wants to ensure that the estimator
3
--- page 4 ---
she uses (e.g., sample mean) is reliable and accurate. Explain the criteria that the
researcher should consider when selecting a good estimator. For each criterion,
give an example in the context of this salary survey.
Ans
CO- 5;   e   [04]
SO- 1;   Explain type I and type II errors with proper examples.
BL-2
Ans.
Answer any four from Q2 to Q7
Q2   a   A random process is given by 𝑥(𝑡) = 𝐴𝑐𝑜𝑠(𝑤𝑜𝑡+ 𝜃) where 𝐴 and 𝑤𝑜 are   [10]
CO-1;   constants and θ is a uniformly distributed random variable over the interval (0,
SO-1;
BL-5   2π). Prove that the given process is wide sense stationary process.
4
--- page 5 ---
Ans. Solution: Given X(t) = Acos(wot + 6); where A and wy are constants and
0 — (0,27); fo(@) = x. The 0 is uniformly distributed between 0 to 27. The
distribution shown in Fig. 7.12.

fot
4°”

1/211

0 211

Fig. 7.7

If mean value and auto correlation function of r.p is a function of time, ‘¢’ then it is
not stationary.

1. Expectation or mean value:
2a

E[X()] = X(t) = i a(t) fo(0)d0

4=0

Qa
- | Acos(wot + 9).+-d0
6 2a

=0

A ft
=— cos(wot + 0)d0
2m Jo=0

A .
= 3; Bin(wot + 6)|2"
A... '
= Jy Bin (wot + 27) — sin wot]
7
A... :
= >, sin wot — sin wot]

=0

-, E[X(t)] = X(t) = 0. It is constant.
--- page 6 ---
b   Let X(t) be a wide-sense stationary (WSS) random process with autocorrelation   [10]
function
− (| 10) 𝜏|
CO-2;   𝑅𝑥𝑥(𝜏) = (0.66) . 𝑒
SO-1;
BL-3
Solve for the Power Spectral Density (PSD) 𝑆𝑥𝑥(𝜔) of the process. Also
identify the value of 𝑆𝑥𝑥(𝜔) at 𝜔= 0.1.
6
--- page 7 ---
Ans.
a   For the given random process by   [10]
Q3
CO-1;   𝑥(𝑡) = 𝑐𝑜𝑠(𝑡+ 𝜃)
SO-1;   where 𝜃 is a random variable uniformly distributed over the interval (0, 2π).
BL-3
Solve and check if the given random process is mean-ergodic or not?
Ans
7
--- page 8 ---
b   Explain the power spectral density function (or spectral density or power   [10]
spectrum) of a stationary process.
The power spectrum density function of a zero mean WSS process X(t) is given
CO-2;
SO-1;   by
BL-2,3
{1,   |𝑤} < 𝑤𝑜
𝑆𝑋𝑋(𝑤) =
0,   𝑒𝑙𝑠𝑒𝑤ℎ𝑒𝑟𝑒
Solve for the autocorrelation function.
8
--- page 9 ---
Ans
a   The transition probability matrix of a Markov chain {Xn}n=1,2,3,….. with three   [10]
Q4   states as follows.
0.2 0.5 0.3
CO-3 ;
SO- 1;   𝑃= [ 0.5 0.4 0.1 ]
BL-3   0.3 0.4 0.3
9
--- page 10 ---
The initial distribution is

P°=[06 03 0.1]

Solve for:
(i) P(X) =3)
(ii)   P(X2=2)
(iii) =P [X3 = 2, X2 =3, Xi =3, Xo = 2]

Ans.

10
--- page 11 ---
b   An auto company decided to introduce a new six-cylinder car whose mean petrol   [10]
consumption is claimed to be lower than that of existing auto engine. It was found
CO-5 ;
SO- 1;   that the mean petrol consumption for 50 cars was 10 km/litre with a standard
BL-4   deviation of 3.5 km per litre. Test for the company at 5% level of significance,
the claim that in the new petrol consumption is 9.5 km per litre on average.
Ans.
a   Explain how the good estimate of the population standard deviation 𝜎 is obtained   [10]
Q5
for a random sample 𝑥1, 𝑥2, … , 𝑥𝑛from a normal distribution using maximum
CO-4;
SO-1;   likelihood estimator (MLE). State any assumptions you use (e.g. whether the
BL-2
mean 𝜇is known or unknown) and give the final expression for the MLE of 𝜎.
11
--- page 12 ---
Ans.

Kin NU, 2),

—— Fee a 9-8

A 3 é Be ot

a

Nar oO

12
--- page 13 ---
b   A market research company wants to know if the proportion of people shopping   [10]
online has increased. In a survey conducted last year, 220 out of 500 respondents
CO- 5;   said they preferred online shopping. In a survey conducted this year, 290 out of
SO- 1;   520 respondents said they preferred online shopping.
BL-4   Test for 1% level of significance, whether there has been an increase in the
proportion of people who prefer online shopping.
Ans.
13
--- page 14 ---
Q6   a   The Westview High School nurse is interested in knowing the average height of   [10]
seniors at this school, but she does not have enough time to examine the records
CO-4;   of all 430 seniors. She randomly selects 48 students and finds the sample mean
SO-1;
BL-3   to be 64.5 inches and the sample standard deviation to be 2.3 inches.
14
--- page 15 ---
Solve for:
(i)   the estimated standard error of the mean.
(ii)   Construct a 90% confidence interval for the mean height of all
seniors at Westview High School.
(iii)   Suppose the Nurse wants to reduce the chances of errors in her
estimates, what should she do.
(iv)   Apply your understanding of estimation principles to suggest what
Nurse can do to reduce the chances of errors in her estimates.
Ans.
• To reduce sampling error and get more precise estimates, the nurse
should increase the sample size.
•   Justification: The standard error is inversely proportional to the square
root of the sample size:
15
--- page 16 ---
So, larger n → smaller , SE → narrower confidence interval → more accurate
estimate of the population mean.
--------(3M)
b   Let x be a random variable that represents weight loss (in pounds) after following   [10]
a certain diet for 6 months. After extensive study, it is found that x has a normal
distribution with σ = 5.7 pounds. A new modification of the diet has been
implemented. A random sample of n=21 people use the modified diet for 6
CO-5 ;   months. For these people, the sample standard deviation of weight loss is s= 4.1
SO- 1;
BL-4   pounds.
Test at 1% level of significance, does this result indicate that the variance of
weight loss for the modified diet is different (either way) from the variance of
weight loss for the original diet. Assume weight loss for each diet follows a
normal distribution
Ans.
16
--- page 17 ---
a   Suppose that customers arrive at a bank according to a poisson process with a   [10]
mean rate of 3 per minute.
Q7   Solve for the probability that during a time interval of 2 min
CO-3;   (i)   exactly 4 customers arrive
SO-1;
BL-3   (ii)   more than 4 customers arrive
(iii)   fewer than 4 customer in 2 minute interval.
17
--- page 18 ---
Ans.

Let X(t) be the number of customers arrive at a bank in the time interval of t.
(i) Mean rate, 4 = 3 per minute

Time interval, t= 2 per minute

No. of arrivals, n= 4

Skt n
& (f) follows a Poisson process, P [X (f) =n] = oS
ni

&MO@@T ec 6
4! HAL

4 customers arrive in | _ sal) Fra
minute time a egies) =

= 0.1339

(ii) Mean rate, 2 = 3 per minute

Time interval, t = 2 per minute

No. of arrivals, n= more than 4.

P[more than 4 customers in 2 min. interval]

= P[X(2) > 4] = 1 - P[X(2) <4]

= 1= [P EX (2) = 0] + PIX 2) = 1] + PIX (2) =2|
+P |X (2) =3] + P[X 2) = 4]
eo 26 2 Ge eg 88

Fa ac ik, Mie cae St, ct oethl

= 1-¢°[14+6+18+36+54] = 1-—e¢7° [115]
=0.715
(iii) Mean rate, A = 3 per minute

Time interval, t= 2 per minute

No. of arrivals, n = fewer than 4

fewer than 4 customer
in 2 minute interval

= P[X(2) <4]

= P[X (2) = 0) + P[X (2) = 1] + P [X (2) = 2] + PIX (2) =3]

ee 6? e° 6! e° 6" e76 6

=O. oo rats
=e | eee = (7°) 61) = 0.1512

18
--- page 19 ---
b   A consumer electronics lab compared the battery life of two brands of   [10]
smartphones.
• For Brand X, a sample of 10 phones gave an average battery life of
18.5 hours with a standard deviation of 2.1 hours.
CO-5 ;
SO- 1;   • For Brand Y, a sample of 8 phones gave an average battery life of 20.9
BL- 4   hours with a standard deviation of 1.8 hours.
At the 1% level of significance, test whether Brand X has lower average battery life
than Brand Y.
Ans.
-------(1M)
Pooled variance
19
--- page 20 ---
2 (m —1)s} + (nz — 1)83
§p ny +ng—2

Substitute values:

a (10 — 1)(2.1)? + (8 — 1)(1.8)?

. 10+8-2
_ 9(4.41) +7(3.24) _ 39.694 22.68 62.37 _
a 3 Tg 7 3:8981

8» — V3.8981 = 1.9743
(3M)

Standard error (for difference in means)

Test statistic

1 —%2 _ 185-209   —24

t= SE 0.9366 0.9366 —

—2.562

Degrees of freedom:
df =n, +n.—-2=—16
(2M)

For one-tailed test ata = 0.01 anddf = 16:
teritical = —2.583
Compare:
tealculated = —2.562 > —2.583

So, we fail to reject Hp at the 1% level (just barely — it’s very close).

At a 5% level, we would reject Hp.
——-(2M)

20
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 7512d4c2f1f1

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AIDS_7056/Random Processes and Estimation Techniques/ANS_Random Processes and Estimation Techniques(702AI0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (20 pages), mean OCR confidence 73.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Random Processes and Estimation Techniques
Date: 10 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO- 1;   a.   What do you mean by random processes ? How random processes are   [04]
SO- 1;
BL-1   classified?
Ans. A random process (also called a stochastic process) is a collection of
random variables that represent how a quantity changes with time (or
another parameter) in an uncertain or random way.   (2M)
(i)   Discrete time, discrete state random process.
(ii)   Discrete time, continuous state random process.
(iii)   Continuous time, discrete state random process.
(iv)   Continuous time, continuous state random process.   (2M)
b.   Explain the following types of systems and provide one example for each of   [04]
CO- 2;   them.
SO- 1;
BL-2   (i)   Linear Time-Invariant systems
(ii)   Causal systems
********** 1 **********
--- page 2 ---
1. Linear Time-Invariant (LTI) Systems

Definition:
Asystem is Linear Time-Invariant (LTI) if it satisfies:

e Linearity: Additivity and homogeneity (scaling).

¢ Time Invariance: A time shift in the input causes the same time shift in the output.

Example:
y(t) = 2x(t) + 3a(t — 1)

This system is linear (output is a linear combination of inputs) and time-invariant (a delay in input causes

an equal delay in output).
2. Causal Systems

Definition:
Asystem is causal if the output at any time t depends only on the present and past values of the input,
not on future values.

Example:
y(t) = x(t) + a(t — 2)

This system is causal because it uses the current and past inputs only (no future input terms).

2M each
co-3; | ¢. Show that the mean and the variance of the Poisson random process is given | [04]
SO-1;
BL-2 by At.

FIC 2 I HH ar
--- page 3 ---
Mean – 1M
Variance- 1M
CO-4;   d   Explain confidence level and significance level with one practical example.   [04]
SO-1 ;
BL-2   Also show the relation between confidence level and significance level.
********** 3 **********
--- page 4 ---
(1 Mark)
CO- 5;   e   Compare null and alternate hypothesis. Also explain the significance of one   [04]
SO- 1;
BL-2   tailed and two tailed test in hypothesis testing.
********** 4 **********
--- page 5 ---
Comparision of null alternate 2M
Significance of one taile/2 tail – 2 M
Answer any four from Q2 to Q7
a   Consider the random process   [10]
Q2   𝑥(𝑡) = 𝐴𝑐𝑜𝑠(100𝑡+ 𝜃)
CO-1;
SO-1;   where A and θ are independent variables. A is a random variable with mean 0
BL-5   and variance 1. θ is uniformly distributed in [-π,π ]. Prove that X(t) is WSS
process.
********** 5 **********
--- page 6 ---
Given: X(t) =A cos (100 t+ 8)

E [A] =0, Var(A)= 1

> E[A)| = Vara] + [Ela]]’ = 1+0 = 1 =)
Here, '6' is uniformly distributed in [-1, 1]
1 1
= Af) — ea aah —~1s0sn

To prove: X(t) is a WSS process
ie, To prove: (i) E [X()] = constant
(ii) R (4,2) = a function of (t, — f)

Proof :

(Gi) E[X@] = £[A cos (100t + 6)]

= EA] E [cos (100¢ + 6)]
[’ A and @ are independent variables]

=0 [- E(4) =]

@) RG.) = EKG) XO)
= E [A cos 100t, + 8) A cos (100 ft + 4)]
= E[A?]E [cos (100 t; + @) cos (100 tf, + 4)]

FIC 6 I HF
--- page 7 ---
Condition of WSS-1 M
Mean calculation- 3M
ACF -6M
b   The autocorrelation function of the random telegraph process is given by   [10]
CO-2;   𝑅𝑋𝑋(𝜏) = 𝑒−2𝛼|𝜏|.
SO-1;
BL-3   Solve for the power spectral density (PSD) of the given random telegraph
process.
2M
2M
6M
********** 7 **********
--- page 8 ---
a   A random process is given by 𝑋(𝑡) = 𝐴 𝑐𝑜𝑠 𝑤 𝑡+ 𝐵 𝑠𝑖𝑛 𝑤 𝑡 where A and B   [10]
Q3
are random variable such that E(A) = 0 = E(B), E(AB) = 0 and 𝐸(𝐴2) = 𝐸(𝐵2).
CO-1;
SO-1;   Solve and check whether the given process is mean ergodic or not.
BL-3
********** 8 **********
--- page 9 ---
Given random process
X(t) = Acos(wt) + B sin(wt)

where

A, B are random variables such that

E(A)=0, E(B)=0, E(AB)=0, E(A’) = E(B?) =o’.

Step 1: Find the mean function E[X (t)]
E{X (t)] = E[A] cos(wt) + E[B] sin(wt) = 0- cos(wt) + 0+ sin(wt) = 0.

Mean function:
E[X(t)| =0

Step 2: Find the autocorrelation function Ry (ti, te)

We have:
Rx (ti, te) = B[X (ti) X(ta)].
Substitute X(t):
Rx (ti, t2) = E\(A cos(wt;) + Bsin(wt)))(A cos(wt) + B sin(wt2))].
Expanding:
Rx(ti, tz) = E[A”| cos(wty) cos(wt2) + E[B?] sin(wt;) sin(wt,) + E|AB|(cos(wt;) sin(wtg) + sin(wt,) cos(wtg)).
Given E(AB) = 0 and E[A?] — E[B?] = o?, we get:
Rx(ti, te) = 2” [ cos(wty) cos(wt2) + sin(wt)) sin(wt)].
Use the trigonometric identity:
cos a cos b + sin asin b = cos(a — b).

Thus:

Rx(t,t2) = 0? cos[w(ti — te)) |

Step 4: Check for mean ergodicity

A process is mean ergodic if the time average of a single realization equals the ensemble mean as T +

iLe.,

_ 1 ft ,
lim z/ X(t) dt = E[X(t)}.

T-00
We already have E[X(t)] = 0.

So we need to check if the time average converges to 0.

Compute the time average mean of one realization:

_ 1 T 1 T .
Xp = z/ X(t) dt = z/ (Acos(wt) + B sin(wt)) dt.

FIC QF OH ar
--- page 10 ---
Cal of Mean – 4M
Cal of time average- 5M
Condition of mean ergodic- 1M
CO-2;   b   Identify whether the following systems are linear and time invariant or not.   [10]
SO-1;   (i)   𝑦(𝑡) = 5𝑥(𝑡) −3
BL-2,3   (ii)   𝑦(𝑡) = 𝑥(𝑡) + 𝑥(𝑡−1)
********** 10 **********
--- page 11 ---
Linearity and time invariant 5 marks each
a   Suppose, the probability of a dry day (state 0) following a rainy day (state 1)   [10]
Q4   is 1/3 and that the probability of a rainy day following a dry day is 1/2. Given
CO-3 ;   that May 1 is a dry day, Solve for the probability that (a) May 3 is also a dry
SO- 1;
BL-3   day and (b) May 5 is also a dry day.
********** 11 **********
--- page 12 ---
Ans. Solution :

.'. The tpm of the Markov Chain is

BS.
ames i oi
pola ATES |
Ral as i 2
3 313

s = ro 4

The probability of a dry day following a rainy day is -

> PIR+D] = 3
The probability of a rainy day following a dry day is 5
> P[D=R] = $ 5

[\" If the tpm of a chain is a stochastic matrix, then

the sum of all elements of any row is equal to 1}

FRR ICR] DA KH
--- page 13 ---
b   The mean height of 50 male students who showed above average participation   [10]
in college athletics was 68.2 inches with a standard deviation of 2.5 inches;
CO-5 ;   while 50 male students who showed no interest in such participation had a
SO- 1;
BL-4   mean height of 67.5 inches with a standard deviation of 2.8 inches.
Test at 5% level of significance,the hypothesis that male students who
participate in college athletics are taller than other male students.
********** 13 **********
--- page 14 ---
a   Explain how the good estimate of the probability of success p is obtained for   [10]
a random sample 𝑥1, 𝑥2, … , 𝑥𝑛 drawn from a population that follows a
Q5
binomial distribution using maximum likelihood estimator (MLE). State any
CO-3;
SO-1;   assumptions you use and give the final expression for the MLE probability of
BL-2
success p.
********** 14 **********
--- page 15 ---
b   A company has the head office at Calcutta and a branch at Bombay. The   [10]
personnel director wanted to know if the workers at the two places would like
the introduction of a new, plan of work and a survey was conducted for this
CO- 5;
SO- 1;   purpose. Out of a sample of 500 workers at Calcutta, 62% favoured the new
BL-4   plan. At Bombay out of a sample of 400 workers, 41% were against the new
plan. Test if there is any significant difference between the two groups in their
attitude towards the new plan at 5% level.
********** 15 **********
--- page 16 ---
a   Jon Ackobsen, an overzealous graduate student, has just completed a 700-   [10]
page dissertation. Jon typed his paper himself and is interested in knowing the
average number of typographical errors per page, but he does not want to read
through the entire document. Knowing a little bit about business statistics, Jon
randomly selects 40 pages from his dissertation to review and finds that the
average number of typos per page is 4.3, with a sample standard deviation of
Q6   1.2 typos per page.
CO-4;
SO-1;   (a) Calculate the estimated standard error of the mean.
BL-3
(b) Construct a 90% confidence interval for the true average number of
typographical errors per page in Jon’s dissertation.
(c) Based on the confidence interval, what can Jon infer about the overall
quality of his typing? For example, can he be reasonably confident that his
average number of typos per page is below 5? Explain briefly.
********** 16 **********
--- page 17 ---
Inference about overall typing quality
• The confidence interval tells us that, with 90% confidence, the true
average number of typos per page lies between 3.98 and 4.62.
• Since the upper bound (4.62) is below 5, Jon can reasonably
conclude that the average number of typos per page is likely below
5.
• This suggests his typing quality is fairly good, though there are still
some errors.
---------(3M)
b   It is believed that the precision (as measured by the variance) of an instrument   [10]
is no more than 0.16. State the null and alternative hypotheses to test this
belief. Test at 1% level of significance, whether the following 11
CO-5 ;   measurements taken on the same subject using this instrument support this
SO- 1;
BL-4   claim:
2.5, 2.3, 2.4, 2.3, 2.5, 2.7, 2.5, 2.6, 2.6, 2.7, 2.5
********** 17 **********
--- page 18 ---
a   If 𝑋(𝑡) is a Gaussian process with mean 𝜇(𝑡) = 7 and 𝐶(𝑡1, 𝑡2) =   [10]
Q7   5 . 𝑒−0.1|𝑡1 − 𝑡2| then solve for the probability that
CO-3;   (i)   𝑋(9) ≤4.
SO-1;
BL-3   (ii)   𝑋(11) ≤11.
********** 18 **********
--- page 19 ---
b   [10]
A certain injection administered to each of 12 patients resulted in
the following increases of blood pressure:
CO-5 ;   5, 2, 8, -1, 3, 0, 6, -2, 1, 5, 0, 4
SO- 1;
BL- 4   Test at 5% level of significance whether it can be concluded that
the injection will be, in general, accompanied by an increase in
B.P?
********** 19 **********
--- page 20 ---
Solution: Given: n= 12

¥:/5)2)8/-1/3/0]/6/-2/1]5]0]74 [Sx=31

Z aia z
2,| 2 [2 |e [=e] so [et 2 | oF | a ag

= ee 31 we
z s = fp = 258 ie., x = 2.58

2, 28
n

s -@ = 8s — (258)? = 15.417 — 6.656
ie, 7 = 8.761 > 5 =2.96

1, Hy :x=(«=0) [No increase of blood pressure]

2. Hy: x>(u>0) [One-tailed test (right)]

3, a=5% = 005, di=n-1=12-1=01

4. Table value |¢| = 1.796 [From Table T3]

5. Calculate :
pe fe 2 B= 0”
(Se gaa ES
va — 1. vil

6. Conclusion :
Here, Cal t > table t
Le., 2.89 > 1.796
So, we reject Hp
noiaulono

i.e., we may conclude that the injection is accompanied by an increase in B.P.

FRI ICR DO) A RH
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 8ae528991375

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AIML_7053/Random Processes and Estimation Techniques/ANS_Random Processes and Estimation Techniques(702AI0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (20 pages), mean OCR confidence 73.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Random Processes and Estimation Techniques
Date: 10 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO- 1;   a.   What do you mean by random processes ? How random processes are   [04]
SO- 1;
BL-1   classified?
Ans. A random process (also called a stochastic process) is a collection of
random variables that represent how a quantity changes with time (or
another parameter) in an uncertain or random way.   (2M)
(i)   Discrete time, discrete state random process.
(ii)   Discrete time, continuous state random process.
(iii)   Continuous time, discrete state random process.
(iv)   Continuous time, continuous state random process.   (2M)
b.   Explain the following types of systems and provide one example for each of   [04]
CO- 2;   them.
SO- 1;
BL-2   (i)   Linear Time-Invariant systems
(ii)   Causal systems
********** 1 **********
--- page 2 ---
1. Linear Time-Invariant (LTI) Systems

Definition:
Asystem is Linear Time-Invariant (LTI) if it satisfies:

e Linearity: Additivity and homogeneity (scaling).

¢ Time Invariance: A time shift in the input causes the same time shift in the output.

Example:
y(t) = 2x(t) + 3a(t — 1)

This system is linear (output is a linear combination of inputs) and time-invariant (a delay in input causes

an equal delay in output).
2. Causal Systems

Definition:
Asystem is causal if the output at any time t depends only on the present and past values of the input,
not on future values.

Example:
y(t) = x(t) + a(t — 2)

This system is causal because it uses the current and past inputs only (no future input terms).

2M each
co-3; | ¢. Show that the mean and the variance of the Poisson random process is given | [04]
SO-1;
BL-2 by At.

FIC 2 I HH ar
--- page 3 ---
Mean – 1M
Variance- 1M
CO-4;   d   Explain confidence level and significance level with one practical example.   [04]
SO-1 ;
BL-2   Also show the relation between confidence level and significance level.
********** 3 **********
--- page 4 ---
(1 Mark)
CO- 5;   e   Compare null and alternate hypothesis. Also explain the significance of one   [04]
SO- 1;
BL-2   tailed and two tailed test in hypothesis testing.
********** 4 **********
--- page 5 ---
Comparision of null alternate 2M
Significance of one taile/2 tail – 2 M
Answer any four from Q2 to Q7
a   Consider the random process   [10]
Q2   𝑥(𝑡) = 𝐴𝑐𝑜𝑠(100𝑡+ 𝜃)
CO-1;
SO-1;   where A and θ are independent variables. A is a random variable with mean 0
BL-5   and variance 1. θ is uniformly distributed in [-π,π ]. Prove that X(t) is WSS
process.
********** 5 **********
--- page 6 ---
Given: X(t) =A cos (100 t+ 8)

E [A] =0, Var(A)= 1

> E[A)| = Vara] + [Ela]]’ = 1+0 = 1 =)
Here, '6' is uniformly distributed in [-1, 1]
1 1
= Af) — ea aah —~1s0sn

To prove: X(t) is a WSS process
ie, To prove: (i) E [X()] = constant
(ii) R (4,2) = a function of (t, — f)

Proof :

(Gi) E[X@] = £[A cos (100t + 6)]

= EA] E [cos (100¢ + 6)]
[’ A and @ are independent variables]

=0 [- E(4) =]

@) RG.) = EKG) XO)
= E [A cos 100t, + 8) A cos (100 ft + 4)]
= E[A?]E [cos (100 t; + @) cos (100 tf, + 4)]

FIC 6 I HF
--- page 7 ---
Condition of WSS-1 M
Mean calculation- 3M
ACF -6M
b   The autocorrelation function of the random telegraph process is given by   [10]
CO-2;   𝑅𝑋𝑋(𝜏) = 𝑒−2𝛼|𝜏|.
SO-1;
BL-3   Solve for the power spectral density (PSD) of the given random telegraph
process.
2M
2M
6M
********** 7 **********
--- page 8 ---
a   A random process is given by 𝑋(𝑡) = 𝐴 𝑐𝑜𝑠 𝑤 𝑡+ 𝐵 𝑠𝑖𝑛 𝑤 𝑡 where A and B   [10]
Q3
are random variable such that E(A) = 0 = E(B), E(AB) = 0 and 𝐸(𝐴2) = 𝐸(𝐵2).
CO-1;
SO-1;   Solve and check whether the given process is mean ergodic or not.
BL-3
********** 8 **********
--- page 9 ---
Given random process
X(t) = Acos(wt) + B sin(wt)

where

A, B are random variables such that

E(A)=0, E(B)=0, E(AB)=0, E(A’) = E(B?) =o’.

Step 1: Find the mean function E[X (t)]
E{X (t)] = E[A] cos(wt) + E[B] sin(wt) = 0- cos(wt) + 0+ sin(wt) = 0.

Mean function:
E[X(t)| =0

Step 2: Find the autocorrelation function Ry (ti, te)

We have:
Rx (ti, te) = B[X (ti) X(ta)].
Substitute X(t):
Rx (ti, t2) = E\(A cos(wt;) + Bsin(wt)))(A cos(wt) + B sin(wt2))].
Expanding:
Rx(ti, tz) = E[A”| cos(wty) cos(wt2) + E[B?] sin(wt;) sin(wt,) + E|AB|(cos(wt;) sin(wtg) + sin(wt,) cos(wtg)).
Given E(AB) = 0 and E[A?] — E[B?] = o?, we get:
Rx(ti, te) = 2” [ cos(wty) cos(wt2) + sin(wt)) sin(wt)].
Use the trigonometric identity:
cos a cos b + sin asin b = cos(a — b).

Thus:

Rx(t,t2) = 0? cos[w(ti — te)) |

Step 4: Check for mean ergodicity

A process is mean ergodic if the time average of a single realization equals the ensemble mean as T +

iLe.,

_ 1 ft ,
lim z/ X(t) dt = E[X(t)}.

T-00
We already have E[X(t)] = 0.

So we need to check if the time average converges to 0.

Compute the time average mean of one realization:

_ 1 T 1 T .
Xp = z/ X(t) dt = z/ (Acos(wt) + B sin(wt)) dt.

FIC QF OH ar
--- page 10 ---
Cal of Mean – 4M
Cal of time average- 5M
Condition of mean ergodic- 1M
CO-2;   b   Identify whether the following systems are linear and time invariant or not.   [10]
SO-1;   (i)   𝑦(𝑡) = 5𝑥(𝑡) −3
BL-2,3   (ii)   𝑦(𝑡) = 𝑥(𝑡) + 𝑥(𝑡−1)
********** 10 **********
--- page 11 ---
Linearity and time invariant 5 marks each
a   Suppose, the probability of a dry day (state 0) following a rainy day (state 1)   [10]
Q4   is 1/3 and that the probability of a rainy day following a dry day is 1/2. Given
CO-3 ;   that May 1 is a dry day, Solve for the probability that (a) May 3 is also a dry
SO- 1;
BL-3   day and (b) May 5 is also a dry day.
********** 11 **********
--- page 12 ---
Ans. Solution :

.'. The tpm of the Markov Chain is

BS.
ames i oi
pola ATES |
Ral as i 2
3 313

s = ro 4

The probability of a dry day following a rainy day is -

> PIR+D] = 3
The probability of a rainy day following a dry day is 5
> P[D=R] = $ 5

[\" If the tpm of a chain is a stochastic matrix, then

the sum of all elements of any row is equal to 1}

FRR ICR] DA KH
--- page 13 ---
b   The mean height of 50 male students who showed above average participation   [10]
in college athletics was 68.2 inches with a standard deviation of 2.5 inches;
CO-5 ;   while 50 male students who showed no interest in such participation had a
SO- 1;
BL-4   mean height of 67.5 inches with a standard deviation of 2.8 inches.
Test at 5% level of significance,the hypothesis that male students who
participate in college athletics are taller than other male students.
********** 13 **********
--- page 14 ---
a   Explain how the good estimate of the probability of success p is obtained for   [10]
a random sample 𝑥1, 𝑥2, … , 𝑥𝑛 drawn from a population that follows a
Q5
binomial distribution using maximum likelihood estimator (MLE). State any
CO-3;
SO-1;   assumptions you use and give the final expression for the MLE probability of
BL-2
success p.
********** 14 **********
--- page 15 ---
b   A company has the head office at Calcutta and a branch at Bombay. The   [10]
personnel director wanted to know if the workers at the two places would like
the introduction of a new, plan of work and a survey was conducted for this
CO- 5;
SO- 1;   purpose. Out of a sample of 500 workers at Calcutta, 62% favoured the new
BL-4   plan. At Bombay out of a sample of 400 workers, 41% were against the new
plan. Test if there is any significant difference between the two groups in their
attitude towards the new plan at 5% level.
********** 15 **********
--- page 16 ---
a   Jon Ackobsen, an overzealous graduate student, has just completed a 700-   [10]
page dissertation. Jon typed his paper himself and is interested in knowing the
average number of typographical errors per page, but he does not want to read
through the entire document. Knowing a little bit about business statistics, Jon
randomly selects 40 pages from his dissertation to review and finds that the
average number of typos per page is 4.3, with a sample standard deviation of
Q6   1.2 typos per page.
CO-4;
SO-1;   (a) Calculate the estimated standard error of the mean.
BL-3
(b) Construct a 90% confidence interval for the true average number of
typographical errors per page in Jon’s dissertation.
(c) Based on the confidence interval, what can Jon infer about the overall
quality of his typing? For example, can he be reasonably confident that his
average number of typos per page is below 5? Explain briefly.
********** 16 **********
--- page 17 ---
Inference about overall typing quality
• The confidence interval tells us that, with 90% confidence, the true
average number of typos per page lies between 3.98 and 4.62.
• Since the upper bound (4.62) is below 5, Jon can reasonably
conclude that the average number of typos per page is likely below
5.
• This suggests his typing quality is fairly good, though there are still
some errors.
---------(3M)
b   It is believed that the precision (as measured by the variance) of an instrument   [10]
is no more than 0.16. State the null and alternative hypotheses to test this
belief. Test at 1% level of significance, whether the following 11
CO-5 ;   measurements taken on the same subject using this instrument support this
SO- 1;
BL-4   claim:
2.5, 2.3, 2.4, 2.3, 2.5, 2.7, 2.5, 2.6, 2.6, 2.7, 2.5
********** 17 **********
--- page 18 ---
a   If 𝑋(𝑡) is a Gaussian process with mean 𝜇(𝑡) = 7 and 𝐶(𝑡1, 𝑡2) =   [10]
Q7   5 . 𝑒−0.1|𝑡1 − 𝑡2| then solve for the probability that
CO-3;   (i)   𝑋(9) ≤4.
SO-1;
BL-3   (ii)   𝑋(11) ≤11.
********** 18 **********
--- page 19 ---
b   [10]
A certain injection administered to each of 12 patients resulted in
the following increases of blood pressure:
CO-5 ;   5, 2, 8, -1, 3, 0, 6, -2, 1, 5, 0, 4
SO- 1;
BL- 4   Test at 5% level of significance whether it can be concluded that
the injection will be, in general, accompanied by an increase in
B.P?
********** 19 **********
--- page 20 ---
Solution: Given: n= 12

¥:/5)2)8/-1/3/0]/6/-2/1]5]0]74 [Sx=31

Z aia z
2,| 2 [2 |e [=e] so [et 2 | oF | a ag

= ee 31 we
z s = fp = 258 ie., x = 2.58

2, 28
n

s -@ = 8s — (258)? = 15.417 — 6.656
ie, 7 = 8.761 > 5 =2.96

1, Hy :x=(«=0) [No increase of blood pressure]

2. Hy: x>(u>0) [One-tailed test (right)]

3, a=5% = 005, di=n-1=12-1=01

4. Table value |¢| = 1.796 [From Table T3]

5. Calculate :
pe fe 2 B= 0”
(Se gaa ES
va — 1. vil

6. Conclusion :
Here, Cal t > table t
Le., 2.89 > 1.796
So, we reject Hp
noiaulono

i.e., we may conclude that the injection is accompanied by an increase in B.P.

FRI ICR DO) A RH
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 53cbdb58ddd6

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AI_7012/Random Processes and Estimation Techniques/ANS_Random Processes and Estimation Techniques(702AI0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (20 pages), mean OCR confidence 73.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Random Processes and Estimation Techniques
Date: 10 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO- 1;   a.   What do you mean by random processes ? How random processes are   [04]
SO- 1;
BL-1   classified?
Ans. A random process (also called a stochastic process) is a collection of
random variables that represent how a quantity changes with time (or
another parameter) in an uncertain or random way.   (2M)
(i)   Discrete time, discrete state random process.
(ii)   Discrete time, continuous state random process.
(iii)   Continuous time, discrete state random process.
(iv)   Continuous time, continuous state random process.   (2M)
b.   Explain the following types of systems and provide one example for each of   [04]
CO- 2;   them.
SO- 1;
BL-2   (i)   Linear Time-Invariant systems
(ii)   Causal systems
********** 1 **********
--- page 2 ---
1. Linear Time-Invariant (LTI) Systems

Definition:
Asystem is Linear Time-Invariant (LTI) if it satisfies:

e Linearity: Additivity and homogeneity (scaling).

¢ Time Invariance: A time shift in the input causes the same time shift in the output.

Example:
y(t) = 2x(t) + 3a(t — 1)

This system is linear (output is a linear combination of inputs) and time-invariant (a delay in input causes

an equal delay in output).
2. Causal Systems

Definition:
Asystem is causal if the output at any time t depends only on the present and past values of the input,
not on future values.

Example:
y(t) = x(t) + a(t — 2)

This system is causal because it uses the current and past inputs only (no future input terms).

2M each
co-3; | ¢. Show that the mean and the variance of the Poisson random process is given | [04]
SO-1;
BL-2 by At.

FIC 2 I HH ar
--- page 3 ---
Mean – 1M
Variance- 1M
CO-4;   d   Explain confidence level and significance level with one practical example.   [04]
SO-1 ;
BL-2   Also show the relation between confidence level and significance level.
********** 3 **********
--- page 4 ---
(1 Mark)
CO- 5;   e   Compare null and alternate hypothesis. Also explain the significance of one   [04]
SO- 1;
BL-2   tailed and two tailed test in hypothesis testing.
********** 4 **********
--- page 5 ---
Comparision of null alternate 2M
Significance of one taile/2 tail – 2 M
Answer any four from Q2 to Q7
a   Consider the random process   [10]
Q2   𝑥(𝑡) = 𝐴𝑐𝑜𝑠(100𝑡+ 𝜃)
CO-1;
SO-1;   where A and θ are independent variables. A is a random variable with mean 0
BL-5   and variance 1. θ is uniformly distributed in [-π,π ]. Prove that X(t) is WSS
process.
********** 5 **********
--- page 6 ---
Given: X(t) =A cos (100 t+ 8)

E [A] =0, Var(A)= 1

> E[A)| = Vara] + [Ela]]’ = 1+0 = 1 =)
Here, '6' is uniformly distributed in [-1, 1]
1 1
= Af) — ea aah —~1s0sn

To prove: X(t) is a WSS process
ie, To prove: (i) E [X()] = constant
(ii) R (4,2) = a function of (t, — f)

Proof :

(Gi) E[X@] = £[A cos (100t + 6)]

= EA] E [cos (100¢ + 6)]
[’ A and @ are independent variables]

=0 [- E(4) =]

@) RG.) = EKG) XO)
= E [A cos 100t, + 8) A cos (100 ft + 4)]
= E[A?]E [cos (100 t; + @) cos (100 tf, + 4)]

FIC 6 I HF
--- page 7 ---
Condition of WSS-1 M
Mean calculation- 3M
ACF -6M
b   The autocorrelation function of the random telegraph process is given by   [10]
CO-2;   𝑅𝑋𝑋(𝜏) = 𝑒−2𝛼|𝜏|.
SO-1;
BL-3   Solve for the power spectral density (PSD) of the given random telegraph
process.
2M
2M
6M
********** 7 **********
--- page 8 ---
a   A random process is given by 𝑋(𝑡) = 𝐴 𝑐𝑜𝑠 𝑤 𝑡+ 𝐵 𝑠𝑖𝑛 𝑤 𝑡 where A and B   [10]
Q3
are random variable such that E(A) = 0 = E(B), E(AB) = 0 and 𝐸(𝐴2) = 𝐸(𝐵2).
CO-1;
SO-1;   Solve and check whether the given process is mean ergodic or not.
BL-3
********** 8 **********
--- page 9 ---
Given random process
X(t) = Acos(wt) + B sin(wt)

where

A, B are random variables such that

E(A)=0, E(B)=0, E(AB)=0, E(A’) = E(B?) =o’.

Step 1: Find the mean function E[X (t)]
E{X (t)] = E[A] cos(wt) + E[B] sin(wt) = 0- cos(wt) + 0+ sin(wt) = 0.

Mean function:
E[X(t)| =0

Step 2: Find the autocorrelation function Ry (ti, te)

We have:
Rx (ti, te) = B[X (ti) X(ta)].
Substitute X(t):
Rx (ti, t2) = E\(A cos(wt;) + Bsin(wt)))(A cos(wt) + B sin(wt2))].
Expanding:
Rx(ti, tz) = E[A”| cos(wty) cos(wt2) + E[B?] sin(wt;) sin(wt,) + E|AB|(cos(wt;) sin(wtg) + sin(wt,) cos(wtg)).
Given E(AB) = 0 and E[A?] — E[B?] = o?, we get:
Rx(ti, te) = 2” [ cos(wty) cos(wt2) + sin(wt)) sin(wt)].
Use the trigonometric identity:
cos a cos b + sin asin b = cos(a — b).

Thus:

Rx(t,t2) = 0? cos[w(ti — te)) |

Step 4: Check for mean ergodicity

A process is mean ergodic if the time average of a single realization equals the ensemble mean as T +

iLe.,

_ 1 ft ,
lim z/ X(t) dt = E[X(t)}.

T-00
We already have E[X(t)] = 0.

So we need to check if the time average converges to 0.

Compute the time average mean of one realization:

_ 1 T 1 T .
Xp = z/ X(t) dt = z/ (Acos(wt) + B sin(wt)) dt.

FIC QF OH ar
--- page 10 ---
Cal of Mean – 4M
Cal of time average- 5M
Condition of mean ergodic- 1M
CO-2;   b   Identify whether the following systems are linear and time invariant or not.   [10]
SO-1;   (i)   𝑦(𝑡) = 5𝑥(𝑡) −3
BL-2,3   (ii)   𝑦(𝑡) = 𝑥(𝑡) + 𝑥(𝑡−1)
********** 10 **********
--- page 11 ---
Linearity and time invariant 5 marks each
a   Suppose, the probability of a dry day (state 0) following a rainy day (state 1)   [10]
Q4   is 1/3 and that the probability of a rainy day following a dry day is 1/2. Given
CO-3 ;   that May 1 is a dry day, Solve for the probability that (a) May 3 is also a dry
SO- 1;
BL-3   day and (b) May 5 is also a dry day.
********** 11 **********
--- page 12 ---
Ans. Solution :

.'. The tpm of the Markov Chain is

BS.
ames i oi
pola ATES |
Ral as i 2
3 313

s = ro 4

The probability of a dry day following a rainy day is -

> PIR+D] = 3
The probability of a rainy day following a dry day is 5
> P[D=R] = $ 5

[\" If the tpm of a chain is a stochastic matrix, then

the sum of all elements of any row is equal to 1}

FRR ICR] DA KH
--- page 13 ---
b   The mean height of 50 male students who showed above average participation   [10]
in college athletics was 68.2 inches with a standard deviation of 2.5 inches;
CO-5 ;   while 50 male students who showed no interest in such participation had a
SO- 1;
BL-4   mean height of 67.5 inches with a standard deviation of 2.8 inches.
Test at 5% level of significance,the hypothesis that male students who
participate in college athletics are taller than other male students.
********** 13 **********
--- page 14 ---
a   Explain how the good estimate of the probability of success p is obtained for   [10]
a random sample 𝑥1, 𝑥2, … , 𝑥𝑛 drawn from a population that follows a
Q5
binomial distribution using maximum likelihood estimator (MLE). State any
CO-3;
SO-1;   assumptions you use and give the final expression for the MLE probability of
BL-2
success p.
********** 14 **********
--- page 15 ---
b   A company has the head office at Calcutta and a branch at Bombay. The   [10]
personnel director wanted to know if the workers at the two places would like
the introduction of a new, plan of work and a survey was conducted for this
CO- 5;
SO- 1;   purpose. Out of a sample of 500 workers at Calcutta, 62% favoured the new
BL-4   plan. At Bombay out of a sample of 400 workers, 41% were against the new
plan. Test if there is any significant difference between the two groups in their
attitude towards the new plan at 5% level.
********** 15 **********
--- page 16 ---
a   Jon Ackobsen, an overzealous graduate student, has just completed a 700-   [10]
page dissertation. Jon typed his paper himself and is interested in knowing the
average number of typographical errors per page, but he does not want to read
through the entire document. Knowing a little bit about business statistics, Jon
randomly selects 40 pages from his dissertation to review and finds that the
average number of typos per page is 4.3, with a sample standard deviation of
Q6   1.2 typos per page.
CO-4;
SO-1;   (a) Calculate the estimated standard error of the mean.
BL-3
(b) Construct a 90% confidence interval for the true average number of
typographical errors per page in Jon’s dissertation.
(c) Based on the confidence interval, what can Jon infer about the overall
quality of his typing? For example, can he be reasonably confident that his
average number of typos per page is below 5? Explain briefly.
********** 16 **********
--- page 17 ---
Inference about overall typing quality
• The confidence interval tells us that, with 90% confidence, the true
average number of typos per page lies between 3.98 and 4.62.
• Since the upper bound (4.62) is below 5, Jon can reasonably
conclude that the average number of typos per page is likely below
5.
• This suggests his typing quality is fairly good, though there are still
some errors.
---------(3M)
b   It is believed that the precision (as measured by the variance) of an instrument   [10]
is no more than 0.16. State the null and alternative hypotheses to test this
belief. Test at 1% level of significance, whether the following 11
CO-5 ;   measurements taken on the same subject using this instrument support this
SO- 1;
BL-4   claim:
2.5, 2.3, 2.4, 2.3, 2.5, 2.7, 2.5, 2.6, 2.6, 2.7, 2.5
********** 17 **********
--- page 18 ---
a   If 𝑋(𝑡) is a Gaussian process with mean 𝜇(𝑡) = 7 and 𝐶(𝑡1, 𝑡2) =   [10]
Q7   5 . 𝑒−0.1|𝑡1 − 𝑡2| then solve for the probability that
CO-3;   (i)   𝑋(9) ≤4.
SO-1;
BL-3   (ii)   𝑋(11) ≤11.
********** 18 **********
--- page 19 ---
b   [10]
A certain injection administered to each of 12 patients resulted in
the following increases of blood pressure:
CO-5 ;   5, 2, 8, -1, 3, 0, 6, -2, 1, 5, 0, 4
SO- 1;
BL- 4   Test at 5% level of significance whether it can be concluded that
the injection will be, in general, accompanied by an increase in
B.P?
********** 19 **********
--- page 20 ---
Solution: Given: n= 12

¥:/5)2)8/-1/3/0]/6/-2/1]5]0]74 [Sx=31

Z aia z
2,| 2 [2 |e [=e] so [et 2 | oF | a ag

= ee 31 we
z s = fp = 258 ie., x = 2.58

2, 28
n

s -@ = 8s — (258)? = 15.417 — 6.656
ie, 7 = 8.761 > 5 =2.96

1, Hy :x=(«=0) [No increase of blood pressure]

2. Hy: x>(u>0) [One-tailed test (right)]

3, a=5% = 005, di=n-1=12-1=01

4. Table value |¢| = 1.796 [From Table T3]

5. Calculate :
pe fe 2 B= 0”
(Se gaa ES
va — 1. vil

6. Conclusion :
Here, Cal t > table t
Le., 2.89 > 1.796
So, we reject Hp
noiaulono

i.e., we may conclude that the injection is accompanied by an increase in B.P.

FRI ICR DO) A RH
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper e73209748b47

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_AI_7051/Random Processes and Estimation Techniques/ANS_Random Processes and Estimation Techniques(702AI0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (20 pages), mean OCR confidence 73.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Random Processes and Estimation Techniques
Date: 10 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
CO- 1;   a.   What do you mean by random processes ? How random processes are   [04]
SO- 1;
BL-1   classified?
Ans. A random process (also called a stochastic process) is a collection of
random variables that represent how a quantity changes with time (or
another parameter) in an uncertain or random way.   (2M)
(i)   Discrete time, discrete state random process.
(ii)   Discrete time, continuous state random process.
(iii)   Continuous time, discrete state random process.
(iv)   Continuous time, continuous state random process.   (2M)
b.   Explain the following types of systems and provide one example for each of   [04]
CO- 2;   them.
SO- 1;
BL-2   (i)   Linear Time-Invariant systems
(ii)   Causal systems
********** 1 **********
--- page 2 ---
1. Linear Time-Invariant (LTI) Systems

Definition:
Asystem is Linear Time-Invariant (LTI) if it satisfies:

e Linearity: Additivity and homogeneity (scaling).

¢ Time Invariance: A time shift in the input causes the same time shift in the output.

Example:
y(t) = 2x(t) + 3a(t — 1)

This system is linear (output is a linear combination of inputs) and time-invariant (a delay in input causes

an equal delay in output).
2. Causal Systems

Definition:
Asystem is causal if the output at any time t depends only on the present and past values of the input,
not on future values.

Example:
y(t) = x(t) + a(t — 2)

This system is causal because it uses the current and past inputs only (no future input terms).

2M each
co-3; | ¢. Show that the mean and the variance of the Poisson random process is given | [04]
SO-1;
BL-2 by At.

FIC 2 I HH ar
--- page 3 ---
Mean – 1M
Variance- 1M
CO-4;   d   Explain confidence level and significance level with one practical example.   [04]
SO-1 ;
BL-2   Also show the relation between confidence level and significance level.
********** 3 **********
--- page 4 ---
(1 Mark)
CO- 5;   e   Compare null and alternate hypothesis. Also explain the significance of one   [04]
SO- 1;
BL-2   tailed and two tailed test in hypothesis testing.
********** 4 **********
--- page 5 ---
Comparision of null alternate 2M
Significance of one taile/2 tail – 2 M
Answer any four from Q2 to Q7
a   Consider the random process   [10]
Q2   𝑥(𝑡) = 𝐴𝑐𝑜𝑠(100𝑡+ 𝜃)
CO-1;
SO-1;   where A and θ are independent variables. A is a random variable with mean 0
BL-5   and variance 1. θ is uniformly distributed in [-π,π ]. Prove that X(t) is WSS
process.
********** 5 **********
--- page 6 ---
Given: X(t) =A cos (100 t+ 8)

E [A] =0, Var(A)= 1

> E[A)| = Vara] + [Ela]]’ = 1+0 = 1 =)
Here, '6' is uniformly distributed in [-1, 1]
1 1
= Af) — ea aah —~1s0sn

To prove: X(t) is a WSS process
ie, To prove: (i) E [X()] = constant
(ii) R (4,2) = a function of (t, — f)

Proof :

(Gi) E[X@] = £[A cos (100t + 6)]

= EA] E [cos (100¢ + 6)]
[’ A and @ are independent variables]

=0 [- E(4) =]

@) RG.) = EKG) XO)
= E [A cos 100t, + 8) A cos (100 ft + 4)]
= E[A?]E [cos (100 t; + @) cos (100 tf, + 4)]

FIC 6 I HF
--- page 7 ---
Condition of WSS-1 M
Mean calculation- 3M
ACF -6M
b   The autocorrelation function of the random telegraph process is given by   [10]
CO-2;   𝑅𝑋𝑋(𝜏) = 𝑒−2𝛼|𝜏|.
SO-1;
BL-3   Solve for the power spectral density (PSD) of the given random telegraph
process.
2M
2M
6M
********** 7 **********
--- page 8 ---
a   A random process is given by 𝑋(𝑡) = 𝐴 𝑐𝑜𝑠 𝑤 𝑡+ 𝐵 𝑠𝑖𝑛 𝑤 𝑡 where A and B   [10]
Q3
are random variable such that E(A) = 0 = E(B), E(AB) = 0 and 𝐸(𝐴2) = 𝐸(𝐵2).
CO-1;
SO-1;   Solve and check whether the given process is mean ergodic or not.
BL-3
********** 8 **********
--- page 9 ---
Given random process
X(t) = Acos(wt) + B sin(wt)

where

A, B are random variables such that

E(A)=0, E(B)=0, E(AB)=0, E(A’) = E(B?) =o’.

Step 1: Find the mean function E[X (t)]
E{X (t)] = E[A] cos(wt) + E[B] sin(wt) = 0- cos(wt) + 0+ sin(wt) = 0.

Mean function:
E[X(t)| =0

Step 2: Find the autocorrelation function Ry (ti, te)

We have:
Rx (ti, te) = B[X (ti) X(ta)].
Substitute X(t):
Rx (ti, t2) = E\(A cos(wt;) + Bsin(wt)))(A cos(wt) + B sin(wt2))].
Expanding:
Rx(ti, tz) = E[A”| cos(wty) cos(wt2) + E[B?] sin(wt;) sin(wt,) + E|AB|(cos(wt;) sin(wtg) + sin(wt,) cos(wtg)).
Given E(AB) = 0 and E[A?] — E[B?] = o?, we get:
Rx(ti, te) = 2” [ cos(wty) cos(wt2) + sin(wt)) sin(wt)].
Use the trigonometric identity:
cos a cos b + sin asin b = cos(a — b).

Thus:

Rx(t,t2) = 0? cos[w(ti — te)) |

Step 4: Check for mean ergodicity

A process is mean ergodic if the time average of a single realization equals the ensemble mean as T +

iLe.,

_ 1 ft ,
lim z/ X(t) dt = E[X(t)}.

T-00
We already have E[X(t)] = 0.

So we need to check if the time average converges to 0.

Compute the time average mean of one realization:

_ 1 T 1 T .
Xp = z/ X(t) dt = z/ (Acos(wt) + B sin(wt)) dt.

FIC QF OH ar
--- page 10 ---
Cal of Mean – 4M
Cal of time average- 5M
Condition of mean ergodic- 1M
CO-2;   b   Identify whether the following systems are linear and time invariant or not.   [10]
SO-1;   (i)   𝑦(𝑡) = 5𝑥(𝑡) −3
BL-2,3   (ii)   𝑦(𝑡) = 𝑥(𝑡) + 𝑥(𝑡−1)
********** 10 **********
--- page 11 ---
Linearity and time invariant 5 marks each
a   Suppose, the probability of a dry day (state 0) following a rainy day (state 1)   [10]
Q4   is 1/3 and that the probability of a rainy day following a dry day is 1/2. Given
CO-3 ;   that May 1 is a dry day, Solve for the probability that (a) May 3 is also a dry
SO- 1;
BL-3   day and (b) May 5 is also a dry day.
********** 11 **********
--- page 12 ---
Ans. Solution :

.'. The tpm of the Markov Chain is

BS.
ames i oi
pola ATES |
Ral as i 2
3 313

s = ro 4

The probability of a dry day following a rainy day is -

> PIR+D] = 3
The probability of a rainy day following a dry day is 5
> P[D=R] = $ 5

[\" If the tpm of a chain is a stochastic matrix, then

the sum of all elements of any row is equal to 1}

FRR ICR] DA KH
--- page 13 ---
b   The mean height of 50 male students who showed above average participation   [10]
in college athletics was 68.2 inches with a standard deviation of 2.5 inches;
CO-5 ;   while 50 male students who showed no interest in such participation had a
SO- 1;
BL-4   mean height of 67.5 inches with a standard deviation of 2.8 inches.
Test at 5% level of significance,the hypothesis that male students who
participate in college athletics are taller than other male students.
********** 13 **********
--- page 14 ---
a   Explain how the good estimate of the probability of success p is obtained for   [10]
a random sample 𝑥1, 𝑥2, … , 𝑥𝑛 drawn from a population that follows a
Q5
binomial distribution using maximum likelihood estimator (MLE). State any
CO-3;
SO-1;   assumptions you use and give the final expression for the MLE probability of
BL-2
success p.
********** 14 **********
--- page 15 ---
b   A company has the head office at Calcutta and a branch at Bombay. The   [10]
personnel director wanted to know if the workers at the two places would like
the introduction of a new, plan of work and a survey was conducted for this
CO- 5;
SO- 1;   purpose. Out of a sample of 500 workers at Calcutta, 62% favoured the new
BL-4   plan. At Bombay out of a sample of 400 workers, 41% were against the new
plan. Test if there is any significant difference between the two groups in their
attitude towards the new plan at 5% level.
********** 15 **********
--- page 16 ---
a   Jon Ackobsen, an overzealous graduate student, has just completed a 700-   [10]
page dissertation. Jon typed his paper himself and is interested in knowing the
average number of typographical errors per page, but he does not want to read
through the entire document. Knowing a little bit about business statistics, Jon
randomly selects 40 pages from his dissertation to review and finds that the
average number of typos per page is 4.3, with a sample standard deviation of
Q6   1.2 typos per page.
CO-4;
SO-1;   (a) Calculate the estimated standard error of the mean.
BL-3
(b) Construct a 90% confidence interval for the true average number of
typographical errors per page in Jon’s dissertation.
(c) Based on the confidence interval, what can Jon infer about the overall
quality of his typing? For example, can he be reasonably confident that his
average number of typos per page is below 5? Explain briefly.
********** 16 **********
--- page 17 ---
Inference about overall typing quality
• The confidence interval tells us that, with 90% confidence, the true
average number of typos per page lies between 3.98 and 4.62.
• Since the upper bound (4.62) is below 5, Jon can reasonably
conclude that the average number of typos per page is likely below
5.
• This suggests his typing quality is fairly good, though there are still
some errors.
---------(3M)
b   It is believed that the precision (as measured by the variance) of an instrument   [10]
is no more than 0.16. State the null and alternative hypotheses to test this
belief. Test at 1% level of significance, whether the following 11
CO-5 ;   measurements taken on the same subject using this instrument support this
SO- 1;
BL-4   claim:
2.5, 2.3, 2.4, 2.3, 2.5, 2.7, 2.5, 2.6, 2.6, 2.7, 2.5
********** 17 **********
--- page 18 ---
a   If 𝑋(𝑡) is a Gaussian process with mean 𝜇(𝑡) = 7 and 𝐶(𝑡1, 𝑡2) =   [10]
Q7   5 . 𝑒−0.1|𝑡1 − 𝑡2| then solve for the probability that
CO-3;   (i)   𝑋(9) ≤4.
SO-1;
BL-3   (ii)   𝑋(11) ≤11.
********** 18 **********
--- page 19 ---
b   [10]
A certain injection administered to each of 12 patients resulted in
the following increases of blood pressure:
CO-5 ;   5, 2, 8, -1, 3, 0, 6, -2, 1, 5, 0, 4
SO- 1;
BL- 4   Test at 5% level of significance whether it can be concluded that
the injection will be, in general, accompanied by an increase in
B.P?
********** 19 **********
--- page 20 ---
Solution: Given: n= 12

¥:/5)2)8/-1/3/0]/6/-2/1]5]0]74 [Sx=31

Z aia z
2,| 2 [2 |e [=e] so [et 2 | oF | a ag

= ee 31 we
z s = fp = 258 ie., x = 2.58

2, 28
n

s -@ = 8s — (258)? = 15.417 — 6.656
ie, 7 = 8.761 > 5 =2.96

1, Hy :x=(«=0) [No increase of blood pressure]

2. Hy: x>(u>0) [One-tailed test (right)]

3, a=5% = 005, di=n-1=12-1=01

4. Table value |¢| = 1.796 [From Table T3]

5. Calculate :
pe fe 2 B= 0”
(Se gaa ES
va — 1. vil

6. Conclusion :
Here, Cal t > table t
Le., 2.89 > 1.796
So, we reject Hp
noiaulono

i.e., we may conclude that the injection is accompanied by an increase in B.P.

FRI ICR DO) A RH
````

## 2023-24 · Re-Exam · Sem 3 · Answer key · paper 1f3148de6602

- Departments: AI and Data Science, AI and Machine Learning
- Programmes: BTech AIDS 7056, BTech AIML 7053
- Source: `02_Question_Papers/2023/Sem_03/Re-Exam/BTech_AIDS_7056/Random Processes and Estimation Techniques/ANS_Random Processes and Estimation Techniques(702AI0C005)_2023-2024.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (18 pages), mean OCR confidence 73.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Random Processes and Estimation Techniques
Date: 03 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
a.   [04]
CO- 1;
SO- 1;   Define strict sense stationary process and wide sense stationary process
BL-1
Ans. A strict-sense stationary process (SSS) is one where the entire probability
distribution is time-invariant, meaning the statistical properties do not change
over time. A wide-sense stationary process (WSS), also known as weak-sense
stationary, is a less strict condition where the mean is constant and the
autocorrelation function only depends on the time difference between two
points. All SSS processes are WSS, but the reverse is not always true.
********** 1 **********
--- page 2 ---
b.   State the following types of systems and provide one example for each of   [04]
CO- 2;   them.
SO- 1;
BL-2   (i)   Linear systems
(ii)   Memoryless systems
Ans.
********** 2 **********
--- page 3 ---
c.   Explain Bernoulli process. In a sequence of independent Bernoulli trials,   [04]
CO-3;   where the probability of success (p) is 0.4, explain what it means to say that
SO-1;
BL-2   the sixth success occurs on the tenth trial.
Ans. A Bernoulli process is a sequence of independent and identical experiments
(called Bernoulli trials) where:
• Each trial has two possible outcomes — Success (S) or Failure (F).
• The probability of success (p) remains constant for every trial.
• The outcome of one trial does not affect the outcome of another
(independent trials).
There is about a 6.7% chance that in this Bernoulli process (where each trial
has a 40% chance of success), the 6th success will occur exactly on the 10th
trial — meaning we got 5 successes in the first 9 trials and one more success
on the 10th.
d   A researcher wants to estimate the average monthly salary of employees in a   [04]
large IT based company. She collects data from a random sample of 50
employees. While reviewing her methods, she wants to ensure that the
CO-4;
SO-1 ;   estimator she uses (e.g., sample mean) is reliable and accurate. Explain the
BL-2   criteria that the researcher should consider when selecting a good estimator.
For each criterion, give an example in the context of this salary survey.
********** 3 **********
--- page 4 ---
Ans
CO- 5;   e   [04]
SO- 1;   Explain type I and type II errors with proper examples.
BL-2
Ans.
Q2   a   A random process is given by 𝑥(𝑡) = 𝐴𝑐𝑜𝑠(𝑤𝑜𝑡+ 𝜃) where 𝐴 and 𝑤𝑜 are   [10]
CO-1;   constants and θ is a uniformly distributed random variable over the interval
SO-1;
BL-5   (0, 2π). Prove that the given process is wide sense stationary process.
********** 4 **********
--- page 5 ---
Ans. Solution: Given X(t) = Acos(wot + @); where A and wy are constants and
0 — (0,27); fo(@) = x. The 0 is uniformly distributed between 0 to 27. The
distribution shown in Fig. 7.12.

fo
4°)

1/211

~
0 ano

Fig. 7.7

If mean value and auto correlation function of r.p is a function of time, ‘t’ then it is
not stationary.

1. Expectation or mean value:

__ Qa
BIx(] =X = [ x(t) fo(0)d0

=0
Qa 1
a | A cos(wot + 6).—dé
9 20

=0
2a

=— cos(wot + 0)d0
2m Jo-o
A,. :

on 2, Bin(wot + Ayla"
A... .

= 37 Bin (wot + 27) — sin wot]

A,. ,
= —[sin wot — sin wot]
20

=0

-. E[X (t)] = X(t) = 0. It is constant.

FIC DI EH ar
--- page 6 ---
b   Let X(t) be a wide-sense stationary (WSS) random process with   [10]
autocorrelation function
− (| 10) 𝜏|
CO-2;   𝑅𝑥𝑥(𝜏) = (0.66) . 𝑒
SO-1;
BL-3
Solve for the Power Spectral Density (PSD) 𝑆𝑥𝑥(𝜔) of the process. Also
identify the value of 𝑆𝑥𝑥(𝜔) at 𝜔= 0.1.
********** 6 **********
--- page 7 ---
Ans.
a   For the given random process by   [10]
Q3
CO-1;   𝑥(𝑡) = 𝑐𝑜𝑠(𝑡+ 𝜃)
SO-1;   where 𝜃 is a random variable uniformly distributed over the interval (0, 2π).
BL-3
Solve and check if the given random process is mean-ergodic or not?
Ans
********** 7 **********
--- page 8 ---
b   Explain the power spectral density function (or spectral density or power   [10]
spectrum) of a stationary process.
The power spectrum density function of a zero mean WSS process X(t) is
CO-2;
SO-1;   given by
BL-2,3
{1,   |𝑤} < 𝑤𝑜
𝑆𝑋𝑋(𝑤) =
0,   𝑒𝑙𝑠𝑒𝑤ℎ𝑒𝑟𝑒
Solve for the autocorrelation function.
Ans
********** 8 **********
--- page 9 ---
a   The transition probability matrix of a Markov chain {Xn}n=1,2,3,….. with three   [10]
states as follows.
0.2 0.5 0.3
𝑃= [ 0.5 0.4 0.1 ]
0.3 0.4 0.3
Q4
The initial distribution is
CO-3 ;
SO- 1;
BL-3   𝑃0 = [0.6 0.3 0.1]
Solve for:
(i)   P (X2 = 3)
(ii)   P (X2 = 2)
(iii)   P [X3 = 2, X2 = 3, X1 = 3, X0 = 2]
********** 9 **********
--- page 10 ---
Ans.
b   An auto company decided to introduce a new six-cylinder car whose mean   [10]
petrol consumption is claimed to be lower than that of existing auto engine. It
CO-5 ;   was found that the mean petrol consumption for 50 cars was 10 km/litre with
SO- 1;
BL-4   a standard deviation of 3.5 km per litre. Test for the company at 5% level of
significance, the claim that in the new petrol consumption is 9.5 km per litre
on average.
********** 10 **********
--- page 11 ---
Ans.
a   Explain how the good estimate of the population standard deviation 𝜎 is   [10]
Q5   obtained for a random sample 𝑥1, 𝑥2, … , 𝑥𝑛from a normal distribution using
CO-4;   maximum likelihood estimator (MLE). State any assumptions you use (e.g.
SO-1;
BL-2   whether the mean 𝜇is known or unknown) and give the final expression for
the MLE of 𝜎.
Ans.
********** 11 **********
--- page 12 ---
b   A market research company wants to know if the proportion of people   [10]
shopping online has increased. In a survey conducted last year, 220 out of 500
CO- 5;   respondents said they preferred online shopping. In a survey conducted this
SO- 1;   year, 290 out of 520 respondents said they preferred online shopping.
BL-4   Test for 1% level of significance, whether there has been an increase in the
proportion of people who prefer online shopping.
Ans.
********** 12 **********
--- page 13 ---
a   The Westview High School nurse is interested in knowing the average height   [10]
of seniors at this school, but she does not have enough time to examine the
records of all 430 seniors. She randomly selects 48 students and finds the
sample mean to be 64.5 inches and the sample standard deviation to be 2.3
inches.
Q6   Solve for:
CO-4;   (i)   the estimated standard error of the mean.
SO-1;
BL-3   (ii)   Construct a 90% confidence interval for the mean height of all
seniors at Westview High School.
(iii)   Suppose the Nurse wants to reduce the chances of errors in her
estimates, what should she do.
(iv)   Apply your understanding of estimation principles to suggest
what Nurse can do to reduce the chances of errors in her
estimates.
********** 13 **********
--- page 14 ---
Ans.
• To reduce sampling error and get more precise estimates, the nurse
should increase the sample size.
•   Justification: The standard error is inversely proportional to the
square root of the sample size:
So, larger n → smaller , SE → narrower confidence interval → more
accurate estimate of the population mean.
--------(3M)
b   Let x be a random variable that represents weight loss (in pounds) after   [10]
following a certain diet for 6 months. After extensive study, it is found that x
CO-5 ;   has a normal distribution with σ = 5.7 pounds. A new modification of the diet
SO- 1;
BL-4   has been implemented. A random sample of n=21 people use the modified diet
for 6 months. For these people, the sample standard deviation of weight loss
is s= 4.1 pounds.
********** 14 **********
--- page 15 ---
Test at 1% level of significance, does this result indicate that the variance of
weight loss for the modified diet is different (either way) from the variance of
weight loss for the original diet. Assume weight loss for each diet follows a
normal distribution
Ans.
Q7   a   [10]
Suppose that customers arrive at a bank according to a poisson process with a
CO-3;
SO-1;   mean rate of 3 per minute.
BL-3
********** 15 **********
--- page 16 ---
Solve for the probability that during a time interval of 2 min
(i)   exactly 4 customers arrive
(ii)   more than 4 customers arrive
(iii)   fewer than 4 customer in 2 minute interval.
Ans.
********** 16 **********
--- page 17 ---
b   A consumer electronics lab compared the battery life of two brands of   [10]
smartphones.
• For Brand X, a sample of 10 phones gave an average battery life of
18.5 hours with a standard deviation of 2.1 hours.
CO-5 ;
SO- 1;   • For Brand Y, a sample of 8 phones gave an average battery life of
BL- 4   20.9 hours with a standard deviation of 1.8 hours.
At the 1% level of significance, test whether Brand X has lower average battery
life than Brand Y.
Ans.
-------(1M)
Pooled variance
********** 17 **********
--- page 18 ---
2 (m —1)s7 + (m2 — 1)85
? ny +n2—2
Substitute values:

Co (10 — 1)(2.1)? + (8 — 1)(1.8)?

? 10+8-2
_ 9(4.41) +7(3.24) _ 39.69+ 22.68 62.37 _
a = Tp 7 38981

5, = V3.8981 = 1.9743
(3M)

Standard error (for difference in means)

1 4.
SE = 8)\/ — + —
ny nz

= 1.9743 x = 1.9743 x V0.225 — 1.9743 x 0.4743 = 0.9366

-——-(2M)

Test statistic
Z1—Z2_ 185-209 -24 _
SE 0.9366 0.9366

$=

—2.562

Degrees of freedom:

df —n, +n.—2-—16

For one-tailed test at a — 0.01 anddf = 16:
teritical = —2.583
Compare:
tealculated = —2.562 > —2.583

So, we fail to reject Hp at the 1% level (just barely — it’s very close).

At a 5% level, we would reject Ho.
=—~-(2M)

FR ICR 7] QA HH
````
