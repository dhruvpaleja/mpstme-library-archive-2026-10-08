# Classical Control Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 4d766e03691d

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_Mechatronics_7004/Classical Control Systems/ANS_Classical Control Systems(702MH0C019)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Classical Control Systems
Date: 11 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Answer to each new question to be started on a fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary.
Q.1   Attempt the following -   (20)
CO-   a Definition of order 1.5 Marks   (05)
1 ;   Definition of type   1.5 Marks
SO-
Example of order   1 Mark
1 ;
BL – 2   Example of type   1 Mark
CO-   b Investigate the stability using Routh Hurwitz Criterion.   (05)
3 ;
SO-   F(s) = s4+s3+ 20s2+ 9s +100=0
1 ;
BL - 2
Ans: System is unstable.
CO-   c Explanation of Angle of Arrival 03 Marks   (05)
5 ;   Example.   02 Marks
SO-
1 ;
BL - 2
CO-   d A linear time invariant system is characterized by the state variable model. Comment on
4 ;   controllability of the system.
SO-
1 ;   ẋ (t) = [ 1   −1] 1 x(t) +   [ 0 ]   u(t)
BL - 3   2   1
Ans :
(02)
AB=[ 1 ] n=2
−1
(02)
Qc = [B AB] = [ 0   −1] 1
1
(01)
Det of Qc= -1 Rank=2   n=2 Completely Controllable
********** 1 **********
--- page 2 ---
Q.2   a Reduce the given block diagram and obtain the transfer function using Block Diagram   (02)
CO-   Reduction Rules.   (02)
2 ;   (02)
SO-
1 ;   (02)
BL - 3   (02)
Step
marki
ng
Ans :
CO- 2; b Determine transfer function using Masson’s Gain Formula.   (02)
SO-1;   (02)
BL - 3
(02)
(02)
(02)
Step
marki
ng
Ans :
i)   No of forward paths = k = 2
ii)   P1 = G1 G2 G3 G4
P2 = G1 G5
iii)   No of individual loop gains = 4
L11 = - G1G2H3
L21 = - G2G3H2
L31 = - G4H1
********** 2 **********
--- page 3 ---
L41 = G5H1H2
iv)   There are two combinations of two non - touching loops. :
L12 = L11 X L31 = G1G2H3G4H1
v)   There are no three non - touching loops.
vi)   ∆ = 1 −(𝐿11 + 𝐿21 + 𝐿31 + 𝐿41) + (𝐿12)
All loops touch P1 and P2
∆1 = 1
∆2 = 1
𝐺1𝐺2𝐺3𝐺4 + 𝐺1𝐺5
𝑇. 𝐹. =
1 + 𝐺1𝐺2𝐻3 + 𝐺2𝐺3𝐻2 + 𝐺4𝐻1 + 𝐺5𝐻1𝐻2 + 𝐺1𝐺2𝐺3𝐺4𝐻1𝐻3
Q.3   a A unity feedback system has   (10)
CO- 3;   𝒌
SO-1;   𝑮(𝒔) =
BL - 4   𝒔(𝒔+ 𝟐)(𝒔+ 𝟒)
Predict the range of k so that system is stable.
Ans :
i)   The Characteristic is given by
F(s) = 1+G(s) H(s) = 0
Here H(s) = 1
F(s) = s3 + 6s2 + 8s + k = 0
ii)   The range of k is 0 < k < 48
CO- 4; b A feedback system is having the closed loop transfer function:   (02)
SO-1;   𝐶(𝑠)   100(𝑠+10)   (02)
BL - 6   =   (02)
𝑅(𝑠)   𝑠 (𝑠+3)(𝑠+12)   (02)
Construct a state model for the system.   (02)
Step
Ans :   marki
ng
0   1   0   0
ẋ (t) = [ 0   0   1 ] x(t) + [ 0 ]   r(t)
0 −36 −15   1
y(t) = [1000 10 0] x(t) + [0] r(t)
Q.4   a The second order system is given by   (02)
CO- 2;   (02)
SO-1;   𝑪(𝒔)   𝟐𝟓   (02)
BL - 3   =   (02)
𝑹(𝒔)   𝒔𝟐+ 𝟔𝒔+ 𝟐𝟓
(02)
Compute i) Natural frequency ii) Damping ratio iii) Settling Time
iv)   Peak time v) Peak Overshoot
Ans :
i)   Natural frequency = 5 rad/s
ii)   Damping ratio = 0.6
********** 3 **********
--- page 4 ---
iii)   Settling time = 0.55 sec
iv)   Peak Time = 0.785 sec
v)   Peak Overshoot = 9.487 %
CO- 2; b A unity feedback system has   (02)
SO-1;   𝟐𝟎(𝒔+ 𝟑)   (06)
BL - 3   𝑮(𝒔) =
(𝒔+ 𝟏)(𝒔+ 𝟔)
(02)
Determine: i) Type of the system   ii) All error coefficients
iii) Steady state error when subjected to a step of magnitude 2.
Ans :
i)   Type of the system =0
ii)   All error coefficients KP=10, KV=0, Ka=0
iii)   Steady state error when subjected to a step of magnitude 2 = 0.18
Q. 5 a Sketch Bode plot for the open loop transfer function. Indicate gain and phase margin. Also
CO- 5;   Predict on stability
SO-1;   𝟏𝟎
BL - 5   𝑮(𝒔)𝑯(𝒔) =
𝒔 (𝒔+ 𝟐)(𝒔+ 𝟒)
Ans :
i)   Stepwise solution and Plot
ii)   Gain Margin = 32 dB and Phase Margin = 85 degree   (08)
iii)   Wpc = 2.83 rad / sec and Wgc = 0.125 rad / sec   (02)
iv)   Comment on stability : Since GM & PM are both positive, the given system is (02)
marginally Stable.   (02)
CO- 1; b Explanation of any three standard test signals with mathematical equation and diagram.   (06)
SO-1;
BL - 2
2 Marks for each standard test signal with mathematical equation and diagram
Q.6   a Sketch the root locus for unity feedback system whose open loop forward transfer function is
CO- 3;   given by   (02)
SO-1;   𝒌   (02)
BL- 5   𝑮(𝒔) =   (02)
𝒔(𝒔+ 𝟐)(𝒔+ 𝟒)
(02)
Ans :
(02)
(02)
i)   P-Z=3
(02)
ii)   No of Asymptotes = 3
iii)   Angle of Asymptotes= 600, 1800 , 3000
iv)   Centroid   = - 2
v)   Valid Breakaway points are at s= - 0.85
vi)   Intersection of Imaginary Axis s = +j 2.83 and s = -j 2.83
vii)   Graph
********** 4 **********
--- page 5 ---
CO- 2; b Explanation Force – Voltage Analogy   (02)
SO-1;   Mathematical Relation   (02)
BL - 2
Comparative Table   (02)
Q.7   a Using Nyquist Criterion, investigate closed loop stability of the system whose open loop   (2.5)
CO- 3;   transfer function is given by   (2.5)
SO-1;   𝟓𝟎   (2.5)
BL - 5   𝑮(𝒔)𝑯(𝒔) =   (2.5)
(𝒔+ 𝟏)(𝒔+ 𝟐)
Ans :
i)   Stepwise solution
ii)   P = 0
iii)   Draw the Nyquist Contour:
a. For Path a-b
b. For Path b-c-d
c. For Path d-e
iv)   Since there are no encirclements about (-1 + j 0) point, therefore N= 0.
Hence, System is stable.
CO- 5; b Explanation of PID Controller in detail.   (06)
SO-1;   Block Diagram of PID Controller   (02)
BL - 2
Equation of PID Controller   (02)
********** 5 **********
````
