# Control System Engineering: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper ac437b137c63

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_EXTC_7006/Control System Engineering/ANS_Control System Engineering(702EX0C035)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (14 pages), mean OCR confidence 69.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Control System Engineering
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Label and draw block diagram of closed-loop control systems and write advantages [05]
SO-1;
BL-2   and disadvantages of closed loop control system.
Block diagram of closed-loop control systems (3M) and write advantages (1M) and
disadvantages of closed loop control system. (1M)
********** 1 **********
--- page 2 ---
CO-2;   b.   List the different time-domain specifications of a second-order control system, and [05]
SO-1;
BL-1,2   explain the following time response specifications with the help of a waveform:
(i)   Rise time (ii) Delay time
Types of time-domain specifications of a second-order control system(1)+ Rise
time (2) Delay time(2) -- with waveforms
********** 2 **********
--- page 3 ---
CO-4;   c.   Classify the different compensators used in electrical systems, and compare the lead [05]
SO-1;
BL-2   compensator and lag compensator.
List the different compensators used in electrical systems (1M), compare the lead
compensator, and lag compensator (4M)-any 4 valid point.
CO-5;   d. Explain the concepts of state variables analysis with diagram and define state, state [05]
SO-1;
BL-2   variables and state vector with respect to it.
Concepts of state variables analysis with diagram (2M)and define state, state
variables and state vector with respect to it.(3M-1M each)
Q2   a.   Classify the basic controllers used in control systems. Explain the Proportional [10]
CO-1;   Integral (PI) control mode action with a mathematical expression. Also, implement
SO-1;
BL-2   and describe a Proportional Integral electronic controller used in a system with its
output expression.
Classify the basic controllers used in control systems (2). The proportional
Integral control mode action with a mathematical expression (3) Also, Circuit
Diagram and describe a proportional-Integral electronic controller used in a
system with its output expression (3+2)
In control systems, controllers are classified based on how the control signal depends
on the error signal e(t):
1. Proportional (P) Controller
Output is proportional to the error.
2. Integral (I) Controller
Output depends on the accumulation (integration) of error over time.
3. Derivative (D) Controller
Output depends on the rate of change of error.
4. Composite Controllers
o PI Controller (Proportional + Integral)
o PD Controller (Proportional + Derivative)
o PID Controller (Proportional + Integral + Derivative)
********** 3 **********
--- page 4 ---
Proportional Integral control mode action with a mathematical
expression: -
Proportional Integral electronic controller circuit diagram used in a
system with o/p expression-example using Op-Amp
Q2   b. Solve for the transfer function of the given system using block diagram reduction [10]
CO-1;   rules.
SO-1;
BL-3   Block diagram reduction rules- give marks accordingly correct steps follows.
Final answers correct with proper reduction techniques (10)
********** 4 **********
--- page 5 ---
Q3   a. The open-loop transfer function of a unity feedback control system is given by   [10]
CO-2;
SO-1;   30
BL-3   𝐺(𝑆) =
𝑆(𝑆+ 2)(𝑆+ 3)
Determine the stability of the system using Routh-Hurwitz criterion.
Create Characteristics equation (02) Correct Routh arrays with entry (02)
calculation (04) Comment on stability (02)
The System is marginally Stable.
G(s) = 30 / [ s(s+2)(s+3) ]
Step 1: Characteristic Equation
1 + G(s) = 0
s(s+2)(s+3) + 30 = 0
s^3 + 5s^2 + 6s + 30 = 0
Step 2: Routh Array
s^3 : 1   6
s^2 : 5   30
s^1 : 0   0
s^0 : 30
Step 3: Special Case (Row of Zeros)
Auxiliary equation from s^2 row:
5s^2 + 30 = 0
s = ±j√6
Differentiate: 10s
********** 5 **********
--- page 6 ---
Replace s^1 row with coefficients of 10s
Step 4: Stability Check
First column elements: 1, 5, 10, 30
All positive => no sign changes.
Roots on imaginary axis => marginal stability.
Final Answer: The system is Marginally Stable (Critically Stable)
Q3   b. Develop the Bode plot and determine the gain crossover frequency and phase [10]
CO-3;   crossover frequency for a unity feedback control system with the given open-loop
SO-1;
BL-3   transfer function.
100
𝐺(𝑆) =
(𝑆)(𝑆+ 5)
Magnitude plot and phase plot till mathematical equations (5) +both correct
graph/plot (4) + gain crossover frequency: 9.4 rad/s and phase crossover
frequency-infinity from graph (1)
********** 6 **********
--- page 7 ---
Q4   a. Apply the root locus method to the given control system and comment on the stability [10]
CO-2;   of the system.
SO-1;
BL-3
********** 7 **********
--- page 8 ---
10
𝐺(𝑠)𝐻(𝑠) =
𝑆(𝑆+ 4)
Proper steps-(3) +correct equations answers in each step(3)+root locus
diagram(3)+comment on stability(1)
Given System: G(s)H(s) = 10 / [s(s+4)]
1. Characteristic Equation
For unity feedback, characteristic equation is:
1 + G(s)H(s) = 0
1 + 10/[s(s+4)] = 0
s(s+4) + 10 = 0
s² + 4s + 10 = 0
2. Open Loop Poles and Zeros
Open-loop poles: s = 0 and s = -4
Open-loop zeros: None
3. Root Locus Features
• Number of branches = 2 (equal to number of poles)
• Real-axis locus exists between s = -4 and s = 0
• Centroid of asymptotes = (sum of poles - sum of zeros)/(n-m) = (-4)/2 = -2
• Asymptote angles = ±90°
4. Closed Loop Poles
Solve s² + 4s + 10 = 0
s = [-4 ± √(16 - 40)]/2
s = -2 ± j√6
5. Stability Comment
Both closed-loop poles have real part = -2, which lies in the left half of the s-plane.
Hence, the system is STABLE.
The poles are complex conjugates, so the response is underdamped and oscillatory with
decay.
6. Final Answer
Using root locus method, the branches start from poles at 0 and -4, meet on the real axis,
and move as complex conjugates toward infinity along ±90° asymptotes through centroid -
2. Since the closed-loop poles are at s = -2 ± j√6, the system is stable.
********** 8 **********
--- page 9 ---
Q4   b. Construct the Polar plot for the given control system   [10]
CO-3;   1
SO-1;   𝐺(𝑆) =
BL-3   𝑆2(𝑆+ 4)
Polar plot steps with mathematical derivation equation (6) + Magnitude and
Phase calculation for W varies from 0 to infinity (2) +Polar plot (2)
Given Transfer Function:
G(s) = 1 / [s²(s+4)]
1. Substitute s = jω
G(jω) = 1 / [(jω)² (jω + 4)]
(jω)² = -ω²
Therefore,
G(jω) = -1 / [ω²(4 + jω)]
2. Magnitude
|G(jω)| = 1 / [ω² √(16 + ω²)]
3. Phase Angle
∠G(jω) = -[180° + tan⁻¹(ω/4)]
4. Key Points for Polar Plot
At ω → 0:
|G(jω)| → ∞ , ∠G(jω) → -180°
At ω = 4 rad/s:
|G(jω)| = 1 / [16√32] = 0.0110
∠G(jω) = -(180° + 45°) = -225°
At ω → ∞:
|G(jω)| → 0 , ∠G(jω) → -270°
********** 9 **********
--- page 10 ---
5. Nature of Plot
The polar plot starts from negative real axis at infinite radius, rotates clockwise through
third quadrant, and approaches the positive imaginary axis as magnitude tends to zero.
6. Final Answer
Hence, the polar plot of G(s)=1/[s²(s+4)] starts at angle -180° for ω=0 and ends at angle -
270° for ω→∞ with decreasing magnitude.
Q5   a. Explain the significance of the Root locus technique. Also explain the following [10]
CO-2;   parameters with respect to Root locus:
SO-1;
BL-2   (i)   Breakaway point
(ii)   Asymptotes.
(iii)   Angles of departure.
(iv)   Centroid
Significance of the Root locus technique (2) +parameter (2 marks each)
Q5   b. Find the transfer function of a system defined by the following state-space model   [10]
CO-5; SO-1;   𝑋̇ = [−2 −3] 1 𝑋+ [0 1] 𝑢   and   𝑌= [1 2] 𝑋
BL-1,3   0
Comparing with standard State model equations and find individual matrix and
final Formula of TF based on individual matrix (5)
Calculation of matrix and final answers (5)
********** 10 **********
--- page 11 ---
Let's solve it step by step using the state-space to transfer function method.
We are given:
X=AX+Bu, Y=CX

Where:

a=[ Ar a=(). c=[1 2]

Step 1: Transfer Function Formula

Y(s) l
G(s) = —— =C(sIl—A) B
U(s)

Step 2: Find si —A

aaa[t? nm

0 s+3

Step 3: Find Determinant

sl — A| = (s+ 2)(s+ 3)

Step 4: Find Inverse of sf — A

1 st3 1
(sf — A)? = "s

(s+2)(s+3) | 0 a+2

Step 5: Multiply with B

1 s+3 1 } fo
sI — A) 1B = ——_—__
( (s +2)(s+3) 0 s+2] Hl

7 1 fe
~ (s+ 2)(s+3) [s+ 2}

Step 6: Multiply with C

G(s) = C(sI — A) 'B

7 . 1 1
7(s)=|1 2 ————_—
G(s) (s+ 2)(8+3) [et

FRI ICR 7 FI OH
--- page 12 ---
Q6   a. Determine the transfer function of the system represented by the given signal flow [10]
CO-1;   graph using Mason’s gain formula.
SO-1;
BL-3
Mason’s Gain formula (2) + final transfer function using masons gain with all
steps (8)
Systematic approach
1. Calculate forward path gain Pi for each forward path i.
2. Calculate all loop transfer functions
3. Consider non-touching loops 2 at a time
4. Consider non-touching loops 3 at a time etc
5. Calculate Δ from steps 2,3,4 and 5
6. Calculate Δi as portion of Δ not touching forward path i
Final Answer:
********** 12 **********
--- page 13 ---
Q6   b. For a unity feedback control system with the given open-loop transfer function, [10]
CO-2;   determine:
SO-1;
BL-3   i) The position, velocity, and acceleration error constants.
ii) The steady-state errors corresponding to step, ramp, and parabolic inputs.
30
𝐺(𝑆) =
S2(𝑆+ 1)(𝑆+ 5)
i) The position, velocity, and acceleration error constants. [Formula 3 mark(1
mark each) and answers 2 marks]
ii) The steady-state errors corresponding to step, ramp, and parabolic inputs.
Formula 3 mark (1 mark each) and answers 2 marks]
. Error Constants
Position constant: Kp = lim(s→0) G(s)
Kp = ∞ (due to s² in denominator)
Velocity constant: Kv = lim(s→0) sG(s)
Kv = ∞
Acceleration constant: Ka = lim(s→0) s²G(s)
Ka = lim(s→0) 30 / [(s+1)(s+5)] = 30/5 = 6
2. Steady State Errors
For step input: ess = 1 / (1 + Kp) = 0
For ramp input: ess = 1 / Kv = 0
For parabolic input: ess = 1 / Ka = 1/6 = 0.1667
Final Answer
Kp = ∞
Kv = ∞
Ka = 6
Step error = 0
Ramp error = 0
Parabolic error = 1/6
Q7   a.   Illustrate with proper steps, how a lag compensator is designed using the Bode plot [10]
CO-4;   technique. Also, mention the purpose of each step.
SO-1;
BL-2   All valid steps with basic content or flow chart with proper information and
value (10M)-distribute marks equally based on correct steps till end.
Q7   b.   List the standard test input signals used in control systems. Explain the following with [05]
CO-2;   their mathematical equations and graphical representations:
SO-1;
BL-1,2   i) Unit step input signal.
ii) Ramp input signal.
Types of the standard test input signals used in control systems (01).
i) Unit step input (2M) with waveforms and mathematical expressions.
ii) Ramp input signal. (2M) with waveforms and mathematical expressions.
********** 13 **********
--- page 14 ---
Q7   c. The closed loop transfer function of a system is given by   [05]
CO-3;
SO-1;
BL-2
i) Damping Ratio(ξ) -(2M)
ii) Underdamped Natural frequency (Wn) – (2M)
iii) Damped Natural frequency (Wd)-(1M)
Given closed loop transfer function:
T(s) = 64 / (s² + 8s + 64)
Standard Form
Compare with:
T(s) = ωn² / (s² + 2ξωn s + ωn²)
Comparison
ωn² = 64 ⇒ ωn = 8 rad/s
2ξωn = 8
Calculations
Damping ratio ξ = 0.50
Undamped natural frequency ωn = 8 rad/s
Damped natural frequency ωd = ωn√(1-ξ²) = 6.93 rad/s
Final Answer
i) ξ = 0.5
ii) ωn = 8 rad/s
iii) ωd = 6.93 rad/s
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 83a7c8e0f943

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_EXTC_7006/Control System Engineering/ANS_Control System Engineering(702EX0C035)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (21 pages), mean OCR confidence 57.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Control System Engineering
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly: 2 synoptic   [20]
CO-1;   a. Define the transfer function in control systems and derive the transfer function for a [05]
SO-1;
BL-2   closed-loop system.
Definition (1) the transfer function in control systems and derive the transfer
function for a closed-loop system with block diagram (4).
********** 1 **********
--- page 2 ---
x

Franskey. function Of Closed _[o0e —

control system - 3

te rc
SMaehi 36 Tr

pes

|

3 Sy Fos) G@ts 3 ae ase
a ‘S baescls ie

I}

Reso
1D

donsiclex a —_clesed (oop ‘controls site

WS shown in above. fig.

ldet 3

+

—Resd= Rehence- ite signd

—s += conholed output

BCs) = feedbacle signal:

on

Fo - octuatting signa | :
at His 5 Feedback “path T- fF»

1 es ¢ ati d- a
above 7) 2
| a Ets» = Ro- Bes) — 3)
Parry Res)
|} Cicoe

st: Foss ie Reeser MOSIC'S). o--

FIC 2 I HH ar
--- page 3 ---
CO-2;   b.   List the different time-domain specifications of a second-order control system, and [05]
SO-1;
BL-1,2   explain the following time response specifications with the help of a waveform:
(i) Rise time (ii) Settling time.
Types of time-domain specifications of a second-order control system (1) + Rise
time(2) Settling time (2) -- with waveforms
********** 3 **********
--- page 4 ---
CO-4;   c.   Classify the different compensators used in electrical systems, and explain the lag [05]
SO-1;
BL-2   compensator with its pole-zero configuration and the effect of adding it to a given
system.
Three types compensators (1) + Explanation of lag compensator with its pole-
zero configuration (2) and the effect of adding it to a given system (2).
Three types compensators-Lead, Lag, Lag-lead compensators etc.
********** 4 **********
--- page 5 ---
CO-5;   d. What is State space analysis and explain the concepts of state variables with diagram [05]
SO-1;
BL-2   and examples.
State space analysis (2) and explain the concepts of state variables with diagram
and examples (3)
State space analysis is an powerful and modern approach for the design and analysis
of control systems.
• The conventional or old methods for the design and analysis of control systems is
based on transfer function method.
• The transfer function method for design and analysis had many drawbacks such as..
– Transfer function is defined under zero initial conditions – Applicable to LTI
systems – SISO systems – Does not provide the information regarding internal state
of the system
********** 5 **********
--- page 6 ---
• Initial conditions can be incorporated in the system design
• State equations are highly compatible for simulation on analog or digital computers.
Q2   a.   Classify the basic controllers used in control systems. Explain the Integral (I) control [10]
CO-1;   mode action with a mathematical expression. Also, implement and describe an
SO-1;
BL-2   Integral electronic controller used in a system with its output expression.
Classify the basic controllers used in control systems (2). The Integral control
mode action with a mathematical expression (3) Also, Circuit Diagram and
describe a Integral electronic controller used in a system with its output
expression (3+2)
In control systems, controllers are classified based on how the control signal depends on
the error signal e(t):
1. Proportional (P) Controller
Output is proportional to the error.
2. Integral (I) Controller
Output depends on the accumulation (integration) of error over time.
3. Derivative (D) Controller
Output depends on the rate of change of error.
4. Composite Controllers
o PI Controller (Proportional + Integral)
o PD Controller (Proportional + Derivative)
o PID Controller (Proportional + Integral + Derivative)
Integral control mode action with a mathematical expression: -
********** 6 **********
--- page 7 ---
>

7 4
} Be. 2) Ta a! ecortl of act on Ps
The conte | action ea) ww hic t

rec l

actucdtting Siymel 0d ©PIO8 signa! er i
cy

ce to sate Of chung ox ole

fontroller js cated (ntegre | contre! ow<ton
ST Let
mtt = Or af conto)le?
cs 2 od ves) Sin CActuating signe“
The ley , 7
C+ > pt dm wd
aol
COL D= Wy-dmCct)
at
plas S-ect.dt= mcr >
iy
ace y= | feddt +100) =<
mr: J
seer
ky = mtegra ( cons tant
m co) = oP of Sycte hr cwhen Cr rey>o|
Faking jFT
yaesd= al eg)
an
} >
mes)
} Ee Ki S

| ae contre) achon

can be Beprensented
ask

Integral electronic controller circuit diagram used in a system with
o/p expression: -

FIC 7 IC OHH
--- page 8 ---
D> Enteqra| Uectronic contolle. <>

Los Inteprel fons +

~e \out

The Implementation Of inteqral mode
& kt which nds 4 response oF

HAST of | yectdt + mo) 7)
FP as

regu res

TF ue express the a6dve 9g” i'n terms of VOHages
then opove - u€dn be Obteined by Simply

fOnsiidering a Cntegratiing okt nq Cw Ih a

ahth Cdn be ne pleynented by u Sing OP~9p% fy
Fro atove Fig O/P qt pt Bf =
sah VUinde
ae inadft) +V
ae 0
orp at pe ®
V out a Gv dept Voy’ & 2)
Ro
Vo“ tntegra| COnst -
4 4
Com , a
Paring any In eq! dd)
‘Out ~ yn cr Ws
Ak = AC ecto =Vvin |
= ae 9)
Q2 b. | Solve for the transfer function of the given system using block diagram reduction rules. | [10]

FIC QF EH 1
--- page 9 ---
CO-1;
SO-1;
BL-3
Block diagram reduction rules- give marks accordingly correct steps follows.
Final answers correct with proper reduction techniques (10)
********** 9 **********
--- page 10 ---
Q3   a. The open-loop transfer function of a feedback control system is given by   [10]
CO-2;
SO-1;   𝐾
BL-3   𝐺(𝑆)𝐻(𝑆) =
𝑆(𝑆+ 2)(𝑆+ 4)(𝑆+ 8)
Where K is positive Determine the range of K for the stability of the system using Routh-
Hurwitz criterion.
Create Characteristics equation (2) Correct Routh arrays with entry (2) calculation
of 1st row all elements(4) Range of K calculation (2)
Hence applying Routh-Hurwitz criterion,
********** 10 **********
--- page 11 ---
Q3   b. Define the Gain Crossover Frequency and Phase Crossover Frequency using a [10]
CO-3;   properly labeled general Bode plot.
SO-1;
BL-3   Develop the magnitude Bode plot for a unity feedback control system with the given
open loop transfer function.
80
𝐺(𝑆) =
(𝑆)(𝑆+ 2)(𝑆+ 20)
Gain Crossover Frequency and Phase Crossover Frequency using a properly
labeled general Bode plot (3)
Magnitude plot calculation till mathematical equations (4) +Magnitude plot (3)
Gain Crossover Frequency and Phase Crossover Frequency:-
Generalized Bode plot Steps: -
🔹 1. Convert to Standard Form
G(s)=K(1+s/z)sn(1+s/p)
********** 11 **********
--- page 12 ---
🔹 2. Substitute s=jω
🔹 3. Identify Elements
•   Gain K
•   Poles and zeros
•   Corner (break) frequencies
🔹 4. Magnitude Plot (dB)
•   Start with 20log⁡K20\log K20logK
•   Slope rules:
o P → −20 B/
o Z → +20 B/
• Change slope at each break frequency
Q4   a. Apply the root locus method to the given control system and comment on the stability of [10]
CO-2;   the system.
SO-1;
BL-3   8
𝐺(𝑠)𝐻(𝑠) =
𝑆(𝑆+ 2)
********** 12 **********
--- page 13 ---
Proper steps-(3) +correct equations answers in each step (3) +root locus diagram
(3) +comment on stability (1)
Q4   b. Construct the Polar plot for the given control system   [10]
CO-3;
SO-1;   10
BL-3   𝐺(𝑆) =
𝑆(𝑆+ 1)
Polar plot steps with mathematical derivation equation (6) + Magnitude and Phase
calculation for W varies from 0 to infinity (2) +Polar plot (2)
********** 13 **********
--- page 14 ---
Q5   a. Explain the significance of the Root locus technique, also describe the following [10]
CO-2;   parameters with respect to Root locus:
SO-1;
BL-2   (i)   Break point
(ii)   Angles of arrival.
(iii)   Centroid
Significance of the Root locus technique (4) +parameter (2 marks each)
********** 14 **********
--- page 15 ---
Significance of Root Locus Technique
The Root Locus technique is a graphical method used in control systems to analyze
how the poles of a closed-loop system move in the s-plane as a system parameter
(usually gain K) varies.
Importance:
• Determines stability of the system.
• Shows how transient response (overshoot, settling time) changes with gain.
•   Helps in controller design (like PID) by selecting K to achieve desired performance.
Parameters:
Q5   b. Determine the transfer function of a system defined by the following state-space [10]
CO-5;   equations.
SO-1;
BL-1,3
𝑋̇ = [−0 −2] 5 𝑋+ [1 1] 𝑢   and   𝑌= [1 1] 𝑋
−1
Comparing with standard State model equations and find individual matrix and
final Formula of TF based on individual matrix (5)
Calculation of matrix and final answers (5)
********** 15 **********
--- page 16 ---
Q6   a. Determine the transfer function of the system represented by the given signal flow graph [10]
CO-1;   using Mason’s gain formula.
SO-1;
BL-3
Mason’s Gain formula (2) + final transfer function using masons gain with all steps
(8)
Any other way correct answer
********** 16 **********
--- page 17 ---
Q6   b. For a unity feedback control system with the given open-loop transfer function, [10]
CO-2;   determine:
SO-1;
BL-3   i) The position, velocity, and acceleration error constants.
ii) The steady-state errors corresponding to step, ramp, and parabolic inputs.
10(𝑆+ 2)
𝐺(𝑆) =
S2(S2 + 2𝑆+ 5)
i) The position, velocity, and acceleration error constants. [Formula 3 mark(1 mark
each) and answers-2 marks]
ii) The steady-state errors corresponding to step, ramp, and parabolic inputs.
Formula 3 mark (1 mark each) and answers-2 marks]
Q7   a. Explain the steps involved in designing a lead compensator using the Bode plot.   [10]
CO-4;
SO-1;
BL-2
********** 17 **********
--- page 18 ---
11.4.6 Design of Lead Compensator Using Bode Plot

Let the open-loop transfer function of the uncompensated system be G(s). The object;
design a lead compensator G,, (s) for G(s) so that the compensated system G (< tive
the desired system requirements lhe steps for determining the transfer function al
Ppensated system G,. (<) using Bode plot are explained below:

Sty
iggy,
the com,
Step 1: If the open-loop transfer function of the system G(s) has a variable K, thenc (
otherwise G, (s)= KG(s). WIS Gy,
Step 2: Depending on the input and TYPE of the system, the variable
open-loop transfer function of the uncompensated system is dete

K Present jp, the
either the steady-state error or the static error constant of the s

FmIned based
system :
The static error constants of the system are

Position error constant, K. = Lt G, (s)
Po sso
Velocity error constant, K, = Lt sG, (s)
P

Acceleration error constant, K,= Lt $°G, (s)
P

The relation between the steady-state error and static error constant based on the TYPE of
the system and input applied to the system can be referred to Table 5.5 of Chapter 3

Step 3: Construct the Bode plot for the uncompensated system with gain K obtained

in the previous step and determine the frequency domain specifications of

system (i.e., phase margin, gain margin, phase crossover frequency an

crossover frequency). Let the phase margin of the uncompensated system be »,

Step 4: Let the desired phase margin of the system be (p,.)

((Px.),),.. 28

|, With a tolerance ¢, determine

((Pa)a)oey = (Pm)y ~Pa + ©

where € = 5 to 10.

Step 5: Determine @ using sin((p,, ), ).. _l-a

Ita

1). .
Step 6: Determine - 1010s in dB, Let it be A.
a
ad system
Step 7: Determine the frequency from the magnitude plot of the uncompensated a ot
for the magnitude of AdB. Let this frequency be the new gain crossover fq

(%)

new

1
Step 8: Determine T using (o,. ).. = = Ja’

FR ICR 7] QA HH
--- page 19 ---
Q7   b.   List the standard test input signals used in control systems. Explain the following with [05]
CO-2;   their mathematical equations and graphical representations:
SO-1;
BL-1,2   i) Unit ramp input
ii) Impulse input signal.
Types of the standard test input signals used in control systems (01).
i) Unit ramp input (2)
ii)Impulse input signal. (2) both standard inputs with waveforms and mathematical
expressions
Standard Test Signals: -
– Step signal (Sudden change)
– Ramp signal (Constant velocity)
– Parabolic signal (Constant acceleration)
– Impulse signal (Sudden shock)
– Sinusoidal signal
********** 19 **********
--- page 20 ---
Q7   c. The closed loop transfer function of a system is given by   [05]
CO-3;
SO-1;
BL-2
i) Damping Ratio(ξ) -(2)
ii) Underdamped Natural frequency (Wn) – (2)
iii) Damped Natural frequency (Wd)-(1)
Correct Formula and answers (Equal weightage)
********** 20 **********
--- page 21 ---
Given transfer function:

C(s) 25
R(s) 8? +65 +25

Step 1: Compare with standard second-order form

Standard form:

2
wh

3? + 2¢w,8 + w?

Comparing:
© w= 25S, =5
« 2¢w, =6

Step 2: Find damping ratio ¢

,
2¢(5) =6 > ¢= D = 0.6

Step 3: Damped natural frequency wy
wy = wal — C2 = 5/1 — (0.6)?
= 5V1-—0.36 = 5V0.64 =5 x 08=4

Final Answers:

i)¢ = 0.6
ii) w, = 5 rad/s

iii) wa = 4 rad/s

FI ICR D7 FAC HOH
````
