# Stochastic Processes: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 46c787809408

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_EXTC_7006/Stochastic Processes/ANS_Stochastic Processes(702EX0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (10 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Stochastic Processes
Date: 01 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Answer to each new question to be started on a fresh page.
9. Assume Suitable data if necessary
Q
1   Answer briefly:   [20]
a.   List the classification of stochastic processes based on the nature of sample space and
time parameter.
• Based on Time Parameter (2 Marks)
•   Discrete-Time Process – 1 mark   4
•   Continuous-Time Process – 1 mark
• Based on State (Sample Space) (2 Marks)
•   Discrete-State Process – 1 mark
•   Continuous-State Process – 1 mark
b   Explain how to find the mean value of the output of a linear system
4
********** 1 **********
--- page 2 ---
c   Define power spectral density of a stochastic process.
4
d.   Find the transfer function of RC Low filter
4
e.   With reference to the Queue Model, define the following terms:
4
a) Queue discipline
********** 2 **********

[Text in pictures on this page, read by OCR]
Answer with Marks Distribution:

1. Definition of output mean E[y(t)] - 1 Mark
¢ Mean value is the expected value of output: E[y(t)].
2. Expression for output of linear system — 1 Mark
e y(t) = i h(r)a(t — r)dr
3. Linearity of expectation - 1 Mark
(t)] = [&A(r) Bla (t — 7)Jar
4. Stationary input conclusion - 1 Mark

e Ifinput mean = pz: Ely(t)) = pr [eh (r)dr

1. Definition - 1 Mark:
© Power Spectral Density (PSD) S,,(f) represents how the power of a stochastic process x(t) is
distributed over frequency.
2. Relation with autocorrelation — 2 Marks:
e Fora wide-sense stationary (WSS) process, PSD is the Fourier Transform of the autocorrelation

function R(T):

oo
S.(f) = / R,(r)e PF dr
—00
3. Physical meaning / Note - 1 Mark:
¢ Indicates contribution of each frequency component to the process power.

Marking Scheme:

© Definition - 1 Mark

¢ Fourier relation with autocorrelation — 2 Marks

¢ Physical meaning / note - 1 Mark

1. Circuit Description - 1 Mark
© RC low-pass filter consists of a resistor R in series and a capacitor C’ across output.
© Input voltage: Vin, Output voltage: Viuz across C.
2. Impedance Relation — 1 Mark
itor i . _
© Capacitor impedance: Zo = jut

° Voltage divider formula:

Zc
Vout = Vin * ————-
out " R+Zo
3. Transfer Function - 1 Mark
. Vout 1
A (jw) = =

Vin 1+ jwRC
4. Conclusion / Frequency Response - 1 Mark
© Acts as low-pass filter, allowing low frequencies to pass, attenuating high frequencies.
Marking Scheme:

© Circuit description — 1 Mark
ider — 1 Mark

¢ Impedance / voltage di
¢ Transfer function derivation — 1 Mark

e Conclusion / frequency behavior — 1 Mark
--- page 3 ---
b) Customer behavior
c) Mean arrival rate
Explain the concepts of sample space and random variable with suitable examples.
1. Sample Space – 2 Marks
o Definition: The set of all possible outcomes of a random experiment.
o Example: Tossing a coin → S={H,T}S = \{H, T\}S={H,T}, Rolling a
die → S={1,2,3,4,5,6}S = \{1,2,3,4,5,6\}S={1,2,3,4,5,6}.
2. Random Variable – 2 Marks
o Definition: A function that assigns a numerical value to each
outcome in the sample space.
Q
o Example: Let XXX = number of heads in 2 coin tosses → 6
2
X({HH,HT,TH,TT})={2,1,1,0}X(   \{HH, HT, TH,   TT\}) =
\{2,1,1,0\}X({HH,HT,TH,TT})={2,1,1,0}.
Marking Scheme:
• Sample space definition – 1 Mark
• Sample space example – 1 Mark
• Random variable definition – 1 Mark
• Random variable example – 1 Mark
********** 3 **********

[Text in pictures on this page, read by OCR]
a) Queue Discipline - 1 Mark

© The rule or policy that determines the order in which customers are served in the queue.
e Examples: FIFO (First-In-First-Out), LIFO (Last-In-First-Out), Priority.
b) Customer Behavior - 1 Mark
* Describes the actions of customers in the queue, such as:
*   Balking: Refusing to join a long queue.
*   Reneging: Leaving the queue before service.
*   Jockeying: Switching between queues.
c) Mean Arrival Rate - 2 Marks

© Denoted by A, it is the average number of customers arriving per unit time at the queue.

* For a Poisson process:

Total arrivals
~ Total observation time
Marking Scheme:
© Queue discipline - 1 Mark
© Customer behavior — 1 Mark

© Mean arrival rate (definition + formula/example) - 2 Marks
--- page 4 ---
X and y are random variable taking values 1, -1, 1 and having joint probability distribution
given in table find the mean of x and y and cross covariance
x   y 1   -1   1
1   0   0.1   0.2
-1   0.3   0.1   0.2
1   0   0   0.1
7
Find the pdf function, mean and variance of uniform distribution given 𝑏< 𝑥< 𝑎
1. State PDF of uniform distribution → 2 marks
2. Derive/Write Mean → 2 marks   7
3. Derive/Write Variance → 2 marks
4. Mention support (optional) → 1 mark
a
Q   Consider 𝑥(𝑡) = (𝐴𝑠𝑖𝑛 𝑤 𝑡+ Ɵ) where A and Ɵ are independent variables and uniform
variables over (- 2k, 2k) and (–2π, 2π) respectively. Find mean autocorrelation and   10
3
autocovariance
********** 4 **********

[Text in pictures on this page, read by OCR]
Mark Distribution (4 Marks):

1. Mean of X (E|X}) - 1 Mark
* Correct formula: E[X] = }7, 30, ¢P(X = 2,Y = y)-05
© Correct calculation & value — 0.5

2. Mean of Y (E[Y}) - 1 Mark
* Correct formula: B[Y] = $7, 30, yP(X =2,Y =y)-05
© Correct calculation & value — 0.5

3. Cross-covariance (Cov(X, Y)) - 2 Marks
e Formula: Cou(X,Y) = E[XY] — E[X|E[Y|-05
¢ Correct calculation of E[XY] -0.5

* Correct substitution & final value - 1
--- page 5 ---
b   Two in depend random variable x & y have pdf defined by
{4𝑎𝑥 ,   0 ≤x ≤1
𝑓(x) =
0,   𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒
10
{4𝑏𝑦 ,   0 ≤y ≤1
𝑓(y) =
0,   𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒
Find the correlation of 𝑢= 𝑥+ 𝑦;𝑣= 𝑥−𝑦
********** 5 **********

[Text in pictures on this page, read by OCR]
Step 2: Autocorrelation R., (ty, t2) (4 marks)
R,(ty,t2) = E[2(ty)a(te)] = E[A*] - E[sin(wt; + @) sin(wty + 6))
* For A ~ U(—2k, 2k):

(=2k)? + (—2k)(2k) + (2k)? _ 16K?

B\A) =
. 3 3

* Using sina sin 8 = 3{cos(a — 8) — cos(a + 8)) and integrating over 6:

, 1
Bjsin(wts + 0) sin(wt2 + 8)] = 5 cos(w(tr ~ t))

2

8k?
R2(ti, tz) = TT 3 cos(w(tr —t2))= =z cos(w(ta —ty))

Step 3: Autocovariance C’,(t), t2) (3 marks)

Cr(tr, tz) = Re(ti,t2) — E|x(t1)|E\x(t2))

R(ti,t2) — 0

Caltasta) =F cos(u(ts ~ ta)

Step 4: Synoptic Table with Marks

Property Expression Marks
Mean Ejz(t)] = 0 3
Autocorrelation R,(t1,t2) = %£ cos(w(t — te)) 4
Autocovariance C.(ti,t2) = © cos(w(t: — t2)) 3

Total - 10
--- page 6 ---
Q a   The auto correlation function of stochastic process given by 𝑅(𝜏) = 𝑒+𝑎|𝜏| determine PSD
Each step 2 M
4   10
********** 6 **********

[Text in pictures on this page, read by OCR]
Step 1: Determine constants a and b (1 mark)

1
jf suede =1 > 20-1 = a= 3
0 2

1
[ Aby dy =
0

fx(@)

»=1— »=}
2

2x, fy(y) = 2y, OS ey

Step 2: Compute Means (2 marks)

1

nix)= [ 2-2rdr=2, gly)=2
i= [ a rr)

Step 3: Compute Variances (2 marks)

ahxX?) ‘2 1 7x2 sx)? = 2

B[X?|= f 2?-22de= 5, Var(X) = B[X*| — (B[X))* = |
0

Var(Y) = a Cov(X, Y) = 0 (independent)

Step 4: Compute u and v statistics (3 marks)
u=X+Y, v=X-Y

* Means:

4
XJ)+E|Y)=-,

Ez
o ;

= E[X)- E|Y) =
* Variances:

Var(u) = Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,¥) =

* Variances:

Var(u) = Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y) = ;

a
18

1
Var(v) = Var(X —Y) = 75 +
© Covariance:

Cov(u,

Cov(X + Y¥,X —Y) = Var(X) — Var(Y) =0

Step 5: Correlation (2 marks)

pa FAECOLECO) n°
ao

Step 6: Synoptic Table

Quantity Expression / Value Marks
Constants a=b=} 1
Means E|X] = E\Y] = 3, Elu] = 4, Ely) <0 2
Variances Var(X) = Var(¥) = 4, Var(u) = Var(v) =} 2
Covariance Cov(u,v) = 0 3
Correlation Pur = 0 2

Total Marks: 10
--- page 7 ---
b   Explain the properties of the Power Spectral Density (PSD) and derive the related
expressions with proof.
Any Five properties with proof 2 marks each
10
1. Property 1 — PSD is real and nonnegative (for real WSS processes)
2. Property 2 — Symmetry / Hermitian
3. Property 3 — Total power (Parseval relation)
4. Property 4 — Cross-PSD and conjugation relations
5. Property 5 — Filtering property (PSD through LTI system)
∞
a   If 𝑋(𝑡) is WSS and 𝑌(𝑡)=∫ ℎ(𝑢)𝑋(𝑡−𝑢)𝑑𝑢 then prove that
−∞
Q   i.   𝑅𝑋𝑌(𝜏) = 𝑅𝑋𝑋(𝜏) ∗ℎ(−𝜏)
ii.   𝑅𝑌𝑌(𝜏) = 𝑅𝑋𝑌(𝜏) ∗ℎ(𝜏)
5   10
iii.   𝑆𝑋𝑌(ɷ) = 𝑆𝑋𝑋(ɷ) 𝐻*(ɷ)
𝑖𝑣. 𝑆𝑌𝑌(ɷ) = |𝐻(ɷ)|2𝑆𝑋𝑋(ɷ)
********** 7 **********

[Text in pictures on this page, read by OCR]
Step 2: Plug in R(r)

Sx(w

oo
[ ele * dr
Since |r| splits the integral:

sxw)= fi crear [ ee dr
-oo 0

Wait: Note: If a > 0, €*'*! grows exponentially, so the integral diverges.
+ For PSD to exist, autocorrelation should decay: typically R(r) = e~*!"', a > 0

| will proceed assuming typo and autocorrelation is:

R(r)

Step 3: Split integral

0
sx(w)= emir [ ete dr
00

0
ewrdr + [ en(atiel gy
0

Step 4: Evaluate the integrals

1 fl bmrar = 1
90 a—jw

~ 1
> [ erlotielt gp —
fi

a+ jw
So:
1 1 (a+ jw) + (a — jw) 2a

Ss. = = =

x(w) ajo tatjo a +a? a@+u?
Step 5: Final PSD

2a
Sx(w) = a +w*

This is a Lorentzian spectrum, symmetric around w = 0.
--- page 8 ---
b   Consider a linear system with impulse 𝒉(𝒕) = 10 𝒆−𝒕sin 𝟐𝒕 𝒖(𝒕). Suppose that a WSS
process [X(t)] with 𝝁𝑿 = 8 is used to the input system. Find the mean value of the output
system.
10
a   Consider a circuit with input voltage {X(t)} and output voltage Y(t). If {X(t)} is a
Q   stationary process with mean zero and auto correlation function 𝑹𝑿𝑿(𝝉)=𝟑𝒆−𝟐|𝝉|and
6   if the system transfer function is H(𝝎) =1 find the following. (a) The mean of Y(t). 10
(b) The input power spectral density function 𝑺𝒀𝒀(𝝎) (c) The output power spectral
density function 𝑺𝒀𝒀(𝝎) (d) The ACF of the output.
********** 8 **********

[Text in pictures on this page, read by OCR]
Component Marks

Definitions & setup 1
Proof of (i) 3
Proof of (ii) 2
Proof of (iii) 2
Proof of {iv) 2

Total 10

‘Step

Work to show

State relation for LTI mean: For LTI system Y(t) — h + X(t) and WSS X(t), show

by — E[Y(t)] -/ h(u)E[X(t — u)] du. Mention interchange of expectation

and integral (ald since h absolutely integrable).

Use WSS property: E[X(t — u)] — jx (independent of t and u). Substitute to get

by — wx J h(u) du

Limit the integral by causality: note h(t) — 0 for t < 0 (factor u(t)), so

J h(u) du — Jo" 10e~ sin(2u) du.

Evaluate integral using standard formula: recal! [ e-™ sin(bu) du —
lo

a > 0. Identifya — 1, 6-2.

i * si -2 2
compute theintesat e“ sin(2u) du iis

2
Multiply by amplitude 10: f 10e™ sin(2u) du — 10- = — 4.
5

Compute output mean: pry — x x 4-8 x 4 — 32.

State final boxed result and comment: jy — 32. Optionally note this equals x H{(0)
where H(0) —   h(t)dt — 4.
--- page 9 ---
b   Apply the M/M/1 (∞/FCFS) queuing model to calculate the average number of
customers in the system and the average waiting time, given suitable arrival and
service rates
Q a
7   Describe the operating characteristics of Quique system   10
********** 9 **********

[Text in pictures on this page, read by OCR]
1. Mean:
py = E|Y(t)| = / h(u)E|X(t — u)|du = px / h(u)du = px H(0).

Since py = 0, py = 0.
2. PSD of input (Wiener-Khinchin):

2-2 12
= 2t| ender 3. =.
Sco(w) [. see a = 3° TTB +4

3. PSD of output:

= 2 =1- oe
Syy(w) = |H(w)|"S:2(w) = 1 - Sra(w) = GoG-
4. ACF of output (inverse FT):

sa | erie 7 imes appropriate constants. Directly,

1 f* ew 1 1 oie) _ 9 -2ir1
glt) = 35 [erate = 12-5, (= 3° ) =e :

w+4

(Or note R,, = 8, since H = 1)

Marks Distribution (Total = 10)

Step / Part Description Marks

1 State the given data and check system stability (¢ — 1
A/p<l)

2 Write formula for average number of customers in 2

system L — p/(1—p)

3 Write formula for average waiting time in system 2
W-1/(u-A)

4 Write formula for average number in queue L, — 2
e/(1—p)

5 Write formula for average waiting time in queue 1
W, — L,/d

6 Perform numerical calculation using given A and y 2
--- page 10 ---
b   Explain the concept of a "reproduction law" in the context of branching processes.
How does it influence the behavior of the process?
10
********** 10 **********

[Text in pictures on this page, read by OCR]
No

10

Total

Content

Arrival rate (A)

Service rate (u)

Traffic intensity (p)

Avg. no. in system (L)

Avg. no. in queue (L_q)

Avg. time in system (W,)

Avg. waiting time (W_q)

Probability system empty (Po)

Probability of n customers (P_)

Stability condition + interpretation

Marks

10 Marks
````
