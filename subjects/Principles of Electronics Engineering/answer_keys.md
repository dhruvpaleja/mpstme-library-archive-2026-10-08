# Principles of Electronics Engineering: answer keys

Answer keys and model answers published on the portal, newest first.

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 8860d75d2729

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/BTech_CSBS_7036/Principles of Electronics Engineering/ANS_Principles of Electronics Engineering(702EX0C004)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Apr 2025
- Text: mixed (13 pages), mean OCR confidence 81.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Principles of Electronics Engineering
Date: 28 Apr 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1;   a.   What is junction capacitance? Also discuss varactor diode in
SO-1;   5
detail.
BL-1
Junction Capacitance
Junction capacitance is the capacitance that forms at the p-n junction of
a semiconductor due to the charge storage in the depletion region. It occurs
because a p-n junction behaves like a parallel plate capacitor, where the
depletion region acts as the dielectric, and the p-type and n-type regions
act as conductive plates.
Types of Junction Capacitance
1. Depletion Capacitance (Cd)
o Occurs due to the depletion region in a reverse-biased p-
Answer   n junction.   5
Where,
ε is the permittivity,
A is the junction area, and
W is the depletion width.
Increases with forward bias and decreases with reverse bias.
2. Diffusion Capacitance (Cf)
********** 1 **********
--- page 2 ---
o Observed in a forward-biased junction due to charge
storage.
o Higher in forward bias, negligible in reverse bias.
Varactor Diode (Varicap or Tuning Diode)
A varactor diode is a special type of semiconductor diode that exploits
junction capacitance to function as a variable capacitor. It is used in
applications where electronic tuning is required.
Working Principle
•   The varactor diode operates in reverse bias, meaning no
significant current flows.
•   The width of the depletion region varies with the applied voltage,
changing the capacitance.
•   Higher reverse voltage → Wider depletion region → Lower
capacitance
• Lower reverse voltage → Narrower depletion region →
Higher capacitance.
CO-2;   b.
SO- 1;   Compare NPN and PNP-type transistors.   5
BL-2
Answer   5
CO- 3;   c.
SO-1 ;   Explain the working of enhancement MOSFET.   5
BL-2
********** 2 **********

[Text in pictures on this page, read by OCR]
Feature NPN Transistor PNP Transistor

Full Form Negative-Positive-Negative Positive-Negative-Positive

Structure A thin p-type layer between two A thin n-type layer between two p-
n-type layers type layers

Majority Carriers Electrons (Fast carriers) Holes (Slower carriers)

Minority Holes Electrons

Carriers

Current Flow Electrons flow from emitter to Holes flow from emitter to
collector collector

Powering Mode Activated when base is HIGH Activated when base is LOW

(positive voltage) (negative voltage)
--- page 3 ---
Answer   5
CO-4;   d.   List the basic gates, draw their symbolic representation and
SO-1;   5
write their truth table.
BL-1
Logic gates are fundamental building blocks of digital circuits. The three
basic gates are:
1. AND Gate (with symbol and truth table)   2 MARKS
Answer
2. OR Gate (with symbol and truth table)   2 MARKS
3. NOT Gate (with symbol and truth table)   1 MARKS
Q2   A
CO-1;   Summarise line and load regulation using a zener diode.   10
SO-1;
BL-2
Answer
********** 3 **********

[Text in pictures on this page, read by OCR]
2. Working Principle of Enhancement MOSFET

(i) OFF State (V_GS = OV)
¢ No conducting channel exists between Drain (D) and Source (S).
¢ The MOSFET behaves as an open circuit.

¢ No current flows (I_D = 0A).

(ii) ON State (V_GS > V_TH for N-Channel)

¢ When a positive voltage is applied to the gate, it attracts electrons from the p-

type substrate, forming a conductive N-channel between drain and source.
¢ Ifa voltage V_DS is applied, current I_D flows from drain to source.

¢ The channel width increases with higt V V_GS, increasing current flow.

1. Line Regulation (Stability Against Input Voltage Changes)

¢ Definition: Line regulation ensures that the output voltage remains constant

even when the input voltage (V_in) fluctuates.
¢ Working with Zener Diode:
¢ The Zener diode is connected in reverse bias across the load.

e When V_in increases, the excess voltage is dropped across the series

resistor (R_s), keeping V_out constant.

e¢ When V_in decreases, the Zener maintains conduction, ensuring a steady
V_out.
--- page 4 ---
2. Load Regulation (Stability Against Load Current Changes)

© Definition: Load regulation ensures that V_out remains steady even when the

load resistance (R_L) changes, which affects the load current (I_L).

¢ Working with Zener Diode:

¢ When IL increases, the Zener diode supplies less current to compensate

and maintain V_out.

¢ When LL decreases, the Zener diode draws more current to stabilize V_out.

Determine for Ig, Ic, Vce, Wc, and Vg for the circuit shown.

$$$ Vee = 12 V

Ty

Q2 es Ro-= 1202
CO-2; Yc 10
Sou LG) ps
Is
BL-3 b Ip
+
Step 1: Calculate Base Current (I_B)
Using Kirchhoff's Voltage Law (KVL) at the base circuit:
Vec = IpRp + Vee
Inez Voc — Vee
B Rp
1, . BV -0.7V
2 100k2
_ 113V
* ~ 100, 0000
Ip = 113A
Answer

Step 2: Calculate Collector Current (I_C)

Using the current gain relation:
Ic = BIp
Ic = 150 x 113A

Ic = 16.95mA

Step 3: Calculate Emitter Current (I_E)
Since Ip = Ip + Ic:
In = 113A +16.95mA

Ip ~17.06mA

FIC 7) IC HOH
--- page 5 ---
Q3   A
Explain the construction and working of n-channel JFET.
CO-3;   10
SO-1;   Also, draw and explain its drain characteristics.
BL-2
Answer   10
********** 5 **********

[Text in pictures on this page, read by OCR]
1. Construction of N-Channel JFET

A Junction Field-Effect Transistor (JFET) is a three-terminal semiconductor device

that controls current flow using an electric field. The N-channel JFET consists of:

¢ N-Type Semiconductor Channel: A bar of N-type semiconductor material forms

the conduction channel.

© Gate (G): Two heavily doped P-type regions (forming a PN junction) are
embedded inside the N-channel.

¢ Drain (D): The terminal where the output current flows out.
© Source (S): The terminal where the current enters.

¢ Gate-Source Junction: The PN junction between the gate and channel controls

current flow. Vv

2. Working of N-Channel JFET

(i) When Veg = OV and Vps > OV
© The drain current (I_D) starts flowing from drain to source.
© Since the gate is at zero voltage, the channel remains open, allowing maximum
current flow.
(ii) When Vos < OV (Negative Bias)
© The PN junction between the gate and channel becomes reverse biased.
¢ This causes a depletion region to expand, narrowing the channel.

¢ As the channel narrows, I_D decreases.
--- page 6 ---
Q3   B
CO-3;
Develop the expressions for VGS, ID, VDS, VG, VD, and VS for 10
SO-1;   a voltage divider-biased n channel JFET circuit.
BL-3
10
Answer
********** 6 **********

[Text in pictures on this page, read by OCR]
A voltage divider bias is a common method used to stabilize the operating point

an N-channel JFET. The circuit typically consists of:
* Asource resistor Rs
© Adrain resistor Rp
* Agate voltage divider network (R) and Re)

e A JFET transistor with parameters such os Ip (drain current) and Ves (gate-

source voltage).

3. Gate-Source Voltage (Vis)
The gate-source voltage is given by:
Ves = Va — Vs
Since Vg is set by the voltage divider and Vg depends on Ip, the equation becomes:

Ves = Ve —InRs
--- page 7 ---
Q4   A
Draw and explain the construction, working and VI
CO-1;   10
SO-1;   characteristics of the pn junction diode.
BL-2
5
Answer
5
********** 7 **********

[Text in pictures on this page, read by OCR]
2. Working of PN Junction Diode

The operation of a PN junction diode depends on the applied voltage:

(i) Zero Bias (No External Voltage)

e At equilibrium, diffusion of electrons and holes occurs, leading to the formation

of a depletion region.

© The built-in potential (V;,;) prevents further movement of charge carriers.

(ii) Forward Bias (V > 0)

¢ The P-region is connected to the positive terminal and the N-region to the

negative terminal.
¢ The depletion region shrinks, allowing current to flow.

* When the applied voltage exceeds the built-in potential (V;,;), charge carriers

move freely.
--- page 8 ---
Q4   B   Derive the IB, IC and VCE expression of the fixed bias circuit
CO-2;   using CE configuration in BJT.   10
SO-1;
BL-3
3
Answer
3
3
Circuit: 1 marks
********** 8 **********

[Text in pictures on this page, read by OCR]
(iii) Reverse Bias (V < 0)
¢ The P-region is connected to the negative terminal and the N-region to the
positive terminal.

¢ The depletion region widens, preventing current flow.

e¢ Asmall leakage current (due to minority carriers) flows, but when the reverse
voltage exceeds the breakdown voltage, the diode undergoes avalanche

breakdown.

Regions:
1. Forward Bias Region:
e As voltage increases, current increases exponentially.

¢ The diode conducts current beyond the threshold voltage (= 0.7V for

silicon, 0.3V for germanium).
2. Reverse Bias Region:
e Asmall leakage current flows.

e At breakdown voltage, current increases sharply.

Applying Kirchhoff's Voltage Law (KVL) to the collector-emitter loop
Veo = IcRe + Ver

Rearranging for Vor:
Ver = Veo — IcRc

Substituting Ic:
--- page 9 ---
Q5   A
What is a rectifier? Summarise the working of the full wave
CO-1;
SO-1;   bridge rectifier circuit along with the circuit diagram and   10
BL-1,
waveform.
2
A rectifier is an electronic circuit that converts alternating current (AC)
into direct current (DC). It allows current to flow in only one direction,
effectively "rectifying" the AC signal.   (2 marks)
Full-Wave Bridge Rectifier Circuit
A full-wave bridge rectifier is a type of rectifier that uses four diodes
arranged in a bridge configuration to convert both halves of the AC input
into a pulsating DC output.
Working Principle:
1. Positive Half-Cycle: During the positive half of the AC input,
the two diodes (D1 and D2) are forward biased, and the other
two (D3 and D4) are reverse biased. This allows current to flow
through the load resistor (R) in one direction, producing a
Answer
positive output.
2. Negative Half-Cycle: During the negative half of the AC input,
the diodes (D3 and D4) become forward biased, while D1 and
D2 become reverse biased. This reverses the direction of current
through the load resistor but still produces a positive output,
completing the full cycle.
Thus, a full-wave bridge rectifier provides a unidirectional current flow
for both halves of the AC cycle, resulting in a smoother DC output
compared to a half-wave rectifier.
Circuit Diagram: 2 marks
Waveform: 2 marks
Explanation: 4 marks each
Q5   B
Demonstrate the concept of full subtractor using logic gate
CO-4;   10
SO-1;   circuits, k map and truth table.
BL-4
********** 9 **********
--- page 10 ---
Answer

Truth Table

The truth table for the full subtractor is as follows:

A B B; D (Difference) Bont (Borrow)
0 0 0 0 0
0 0 1 1 1
0 1 0 1 1
i) 1 1 0 1
1 0 0 1 0
1 0 1 0 0
1 1 i) 0 0
1 1 1 1 Vv 0

D=AGBO@By

The K-map for D would look like:

AB\Bin |0 1

For the borrow output Bout, the simplified Boolean expression derived from the truth
table is:

Bow = (A+B) + (A+ Bin) + (B+ Bin)
The K-map for Bou; would look like:
AB\ Bi

00 01
01 11
10 1 0
11 0 0

The difference D can be derived using the XOR operation:
D=A@B@Bny
Where © represents the XOR operation.

Borrow Output Bout:

The borrow output Bout is 1 if the subtraction of the bits results in a borrow. It can be

derived using the following Boolean expression:
Bow = (A+B) + (A+ Bun) + (B+ Bin)
Circuit: 2 marks
Truth Table: 2 marks
Expression: 2 marks

Realization: 4 marks

10

FRR ICR 7 OI HOH
--- page 11 ---
A   Determine the Q point values for the gate biasing circuit if
VGG = -2 V, VGS(off) = -6 V, IDSS = 4 mA, VDD = 12V and RD
= 400Ω.
Q6
CO-3;   10
SO-1;
BL-3
Answer   10
********** 11 **********

[Text in pictures on this page, read by OCR]
Step 1: Calculate Vos
The gate-source voltage Vag is given by the equation:

Ves = Va — Vs

Since Vg (the gate voltage) is Veg, and assuming Vs = 0 V (no source resistor is

given), we have:

Vas = Vag = -2V

The Shockley equation for the drain current Ip in a JFET is:

Ves \*
Ip = Inss (: - nu.)
GS(off)

Substitute the given values:

2

-2V

Ip = 4mA { 1 —- ——
? ( =)

Simplify the expression:

12
Ip =ama (1-5)

Vpp = IpRp + Vos
Rearrange to solve for Vps:
Vos = Vop — InRp
Substitute the values:
Vps = 12V — (1.78mA x 400)
Vps = 12V — 0.712 V

Vps © 11.29V
--- page 12 ---
Q6   B   Inspect the workings of the SR Flip Flop and T flip flop
CO-4;   using a neat diagram.   10
SO-1;
BL-2
Answer   10
Circuit: 3 marks
Truth table: 3 marks
Explanation: 4 marks
Q7   A
CO-4;   Compare multiplexer and demultiplexer.   10
SO-1;
BL-2
********** 12 **********

[Text in pictures on this page, read by OCR]
An SR Flip-Flop is a basic type of bistable multivibrator that has two inputs: S (Set)
and R (Reset). It stores one bit of data, and it has two stable states: one for storing a
logic 1 and the other for storing a logic 0. The SR Flip-Flop is widely used in memory
storage applications.

Truth Table for SR Flip-Flop:

S (Set) R (Reset) Q (Output) Q (Complement)
0 0 Q Q

1 i) 1 0

0 1 0 1

1 1 Invalid Undefined

Working of SR Flip-Flop:
1. S =1,R =0: This sets the output Q to 1.
2. S = 0, R = 1: This resets the output Q to 0.
3. S = 0, R = 0: The output Q retains its previous state.

4. S$ =1,R = 1: This condition is undefined or invalid in a basic SR flip-flop.
--- page 13 ---
Answer   10
8 points atleast
Q7   B   Illustrate the input and output characteristics of CB
CO-2;   configuration using the NPN transistor. Explain in detail 10
SO-1;
BL-2   different regions of operation.
Input characteristics: 4 marks
Answer   10
Output characteristics: 6 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
Feature Multiplexer (MUX) Demultiplexer (DEMUX)

Function Selects one input from many and Routes one input to one of many
sends it to a single output output lines

Number of Multiple inputs (2 inputs, where Single input

Inputs n = number of select lines)

Number of One output Multiple outputs (2" outputs, where

Outputs n = number of select lines)

Control Lines 2° control lines for selecting an 2" control lines for selecting an
input output

Main Purpose To combine multiple signals into To distribute a single signal to
a single output line multiple output lines

Application Data selection, routing, switching _Data distribution, broadcasting
.
````

## 2024-25 · Re-Exam · Sem 2 · Answer key · paper f638b59c096e

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/BTech_CSBS_7036/Principles of Electronics Engineering/ANS_Principles of Electronics Engineering(702EX0C004)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: I/Sem 2 Re-exam(Exam Year: 2024-2025)
Subject: Principles of Electronics Engineering
Date: 01 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1;   a.
SO-1;   Summarize piecewise linear model of pn junction diode.   5
BL-2
Answer   5
CO-   b.
2,3 ;   Compare BJT and JFET .   5
SO-1;
BL-2
********** 1 **********

[Text in pictures on this page, read by OCR]
The diode can be modeled in two conditions:
1. Forward Bias (Vp > Vr):
© The diode is conducting.
© The voltage across the diode is approximately Vr.
¢ The equivalent circuit consists of:
¢ A fixed voltage source (V7) in series with
¢ Asmall dynamic resistance (rq).

e The current through the diode is given by:
V-V;
Ip =——*

Ta
--- page 2 ---
Answer   5
CO-3 ;   c.   Define channel width modulation, pinch off condition and
SO-1 ;   5
drain to source saturation current.
BL-1
Answer   5
********** 2 **********

[Text in pictures on this page, read by OCR]
Feature BUT JFET

Structure Has three layers: Emitter (E), Base Has three terminals: Drain (D),
(B), Collector (C) Gate (G), Source (S)

Types NPN, PNP N-channel, P-channel

Control Controlled by current at the base Controlled by voltage at the gate

Mechanism

Carrier Type Uses both electrons and holes Uses only electrons or holes

(bipolar) (unipolar)

Operation Current amplification Voltage amplification

Input Impedance _Low (because base current is High (because gate current is
required) almost zero)

Output Moderate to high High

Impedance

Control Base current (IB) Gate-source voltage (VGS)

Parameter

Linearity More linear at low frequencies Less linear but good for high-

frequency applications

Power Higher due to base current Lower due to negligible gate

Consumption requirement current

Gain High voltage and current gain Moderate gain

Speed Slower than JFETs due to charge Faster switching speed
storage

Noise Higher noise due to charge Lower noise due to unipolar

carrier recombination Operation

1. Channel Width Modulation (A Effect)

Definition:
Channel width modulation is the variation in the effective width of the conductive
channel in a JFET (Junction Field-Effect Transistor) or MOSFET due to an increase in

drain-to-source voltage (V_DS) beyond the pinch-off voltage (V_P).
Explanation:

e In JFETs/MOSFETs, the channel between source and drain is controlled by the
gate voltage (V_GS).

¢ As V_DS increases, the depletion region at the drain end expands, narrowing the

conductive channel. 1
--- page 3 ---
CO-4;   d.   List the exclusive gates, draw their symbolic representation
SO-1 ;   5
and write their truth table.
BL-1
Answer   5
Q2   A   Outline the zener and avalanche mechanism in the diode.
10
CO-1;
SO-1;
********** 3 **********

[Text in pictures on this page, read by OCR]
© This effect is similar to Early effect in BJTs.
e It results in a small increase in drain current (I_D) even in saturation (constant

current) mode, reducing the ideality of the transistor.

Mathematical Representation:
Ip = Ipvsar) X (1+ AVps)
where:
. Ip(s.ar) = Drain saturation current,
© X= Channel length modulation parameter,

¢ Vps = Drain-to-source voltage.

Pinch-off occurs in a JFET when the gate-to-source voltage Vag is reduced enough

that the depletion regions from both sides meet, fully closing the conductive channel.
Explanation:
¢ When Vos = Vp (pinch-off voltage), the channel is completely depleted.

* Beyond this, increasing Vps does not increase current significantly, and the JFET

enters saturation (constant current region).
--- page 4 ---
BL-2
Answer   10
Q2   B
For a fixed bias, CE circuit, determine Ic, Vcc, β and RB. If
CO-2;   10
SO-;   IB =20μA, IE = 6mA, VCE = 8V and RC = 2.2 kΩ.
BL-3
Answer   10
********** 4 **********

[Text in pictures on this page, read by OCR]
When a high reverse bias is applied, the electric field in the depletion region

becomes very strong.

This strong field breaks covalent bonds in the semiconductor, generating free

electron-hole pairs.
The newly generated carriers rapidly increase current flow.

Since the breakdown voltage is well-controlled, Zener diodes use this

mechanism for voltage regulation.

Step 1: Determine Collector Current (Jc)

For a CE transistor, the emitter current is related to the collector current as:
Ip =Io +Ip
Rearranging:
Ic = Ip — Ip
Substituting values:
Ic = (6 x 10°*) — (20 x 10°)

Ic = 5.98mA
--- page 5 ---
Q3   A
Explain the construction and working of p-channel JFET.
CO-3;   10
SO-;   Also, draw and explain its drain characteristics.
BL-2
Answer   10
********** 5 **********

[Text in pictures on this page, read by OCR]
Step 3: Determine Current Gain (3)

The current gain 6 (DC current gain of BJT) is:

Substituting values:

5.98 x 10-3
20 x 10-6

B = 299

B=

The main channel is made of p-type semiconductor material.

Two n-type regions (forming the Gate terminals) are diffused on either side of

the channel.
The Source (S) and Drain (D) are connected to the ends of the p-channel.
The Gate (G) is connected to both n-type regions, forming a PN junction.

The device is normally ON and requires a negative gate voltage (V_GS < 0) to

control current flow.

(i) No Bias Condition (V¢s = 0)

¢ When no voltage is applied between Gate (G) and Source (S), the p-channel

remains open.

© Current flows from Source to Drain due to a small potential difference.

(ii) Reverse Gate Bias Condition (Vos < 0)

¢ When a negative voltage is applied to the gate (making it more negative than

the source), the depletion region expands.
© The effective width of the p-channel decreases, reducing drain current Ip.

¢ More negative Vgs — More depletion — Lower Ip.

Pinch-Off Condition (V¢s = Vp)

¢ When Vas reaches a critical negative voltage Vp (pinch-off voltage), the

depletion regions completely close the channel.

© At this point, current flow stops (Ip = 0).

(iv) Saturation Region (Vps > Vos — Vp)

© If Vpg increases further after pinch-off, the current remains constant, and the

JFET operates in saturation mode.
--- page 6 ---
Q3   B
CO-3;   Develop the expressions for VGS, ID, VDS, VG, VD, and VS for
10
SO-;   a fixed bias n channel JFET circuit.
BL-3
Answer   10
********** 6 **********

[Text in pictures on this page, read by OCR]
(i) Gate Voltage Vc

Since the gate is connected to a fixed negative voltage through Rg, and no current

flows into the gate in a JFET:
Va = Vac

For an N-channel JFET, Vg is typically negative to keep the device in cutoff or active

region.

(ii) Gate-to-Source Voltage Vos
The gate-to-source voltage is given by:
Ves = Ve — Vs
If the source resistor Rs is not present, then Vs = 0, so:
Ves = Ve
Otherwise, if Rs exists, then:
Vs = IpRs
So,

Vv
Vas = Ve — InRs

(iii) Drain Current Ip

The Shockley’s equation governs the JFET operation:

Voo\?
Ip = Ipss (1 - ‘s)

where:
¢ Ipgzg is the maximum drain current at Vos = 0.
¢ Vp is the pinch-off voltage where Ip becomes zero.

For a fixed bias circuit, Vag is set by the biasing resistor, so Ip follows from the

above equation.
--- page 7 ---
Q4   A
Draw and explain the construction, working and VI
CO-1;   10
SO-;   characteristics of the zener diode.
BL-2
Answer   10
********** 7 **********

[Text in pictures on this page, read by OCR]
1. Construction of Zener Diode

¢ The Zener diode is a heavily doped PN junction diode.

¢ Due to heavy doping, the depletion layer is very thin (~1,1m), and the

breakdown voltage is well-defined.

¢ It is designed to operate in reverse bias mode beyond a specific breakdown

voltage (Vz).

¢ The Zener diode’s structure is similar to a normal diode, but it has a precise

breakdown voltage.

(i) Forward Bias Region (V > 0)
¢ When a Zener diode is forward biased, it behaves like a normal diode.

e It starts conducting when the applied voltage exceeds 0.7V (Si) or 0.3V (Ge).

(ii) Reverse Bias Region (V < 0)
¢ When a reverse voltage is applied, a very small leakage current flows initially.
¢ Ata specific Zener breakdown voltage (Vz), the current increases sharply.
© The diode maintains a constant voltage (Vz) even if the current changes.

¢ This property makes it useful for voltage regulation.

Zener Breakdown Mechanisms
© Zener Breakdown (for Vz < 5V)
¢ Due to high electric field, electrons break away from covalent bonds.
¢ This generates a large number of charge carriers, increasing current.
¢ Avalanche Breakdown (for Vz > 5V)

e Electrons gain kinetic energy and collide with atoms, creating more charge

carriers.

© This leads to carrier multiplication and high current flow.
--- page 8 ---
Q4   B
Derive the IB, IC and VCE expression of the voltage divider
CO-2;   10
SO-;   bias circuit using CE configuration in BJT.
BL-3
Answer   10
********** 8 **********

[Text in pictures on this page, read by OCR]
(i) Expression for Base Current Ip
The base voltage Vp is determined by the voltage divider network formed by R;
and Ro:

Ry

Va = Vcc X =———
'B cox BTR

Now, the base-emitter voltage Vx; for the transistor is typically around 0.7V (for

silicon BJTs):

Vp = Ver + Ve

where Vs is the emitter voltage, given by:
Ve =IeRe

In the approximation that Iz ~ Ic (since Iz = I¢ + Ip and Ig is much smaller
than Ic):

Vp =0.7V +IcRe

Now, the base current Iz is related to the base voltage by the equation:

Now, the base current I is related to the base voltage by the equation:

where Fz is the equivalent base resistance, which is given by:

Ry, Ry

Rp = (Ril|R2) = Rik

Thus, the base current Ig is:
--- page 9 ---
Q5   A   Describe the working of the half wave rectifier and centre
CO-1;   tapped full wave rectifier circuit along with the circuit   10
SO-;
BL-2   diagram and waveform.
Circuit diagram: 3 marks
Answer   Explanation: 4 marks   10
Waveform: 3 marks
Q5   B
Demonstrate the concept of full adder using logic gate
CO-4;   10
SO-;   circuits, k map and truth table.
BL-2
Truth table: 3 marks
Expressions: 2 marks
Answer   10
Kmap: 3marks
Circuit: 2 marks
********** 9 **********

[Text in pictures on this page, read by OCR]
(ii) Expression for Collector Current Ic

Using the current gain ( of the BJT:
Ic = Ip

So, the collector current Ig is:

Voc x we — 0.7
IT,= i+ Re
c=B8x Rp

The collector-emitter voltage is determined by applying Kirchhoff's Volta
in the output loop:

Ver = Ve — Ve
The collector voltage Vo is:
Ve = Veo — IcRe
The emitter voltage Vz is:
Ve = IpgRe 7 IcRr
Thus, the collector-emitter voltage Vo is:

Ver = Veco — Re —IcRz
--- page 10 ---
A   Determine IDQ, VGSQ, VD, VS, VDS, VDG the following for the
network shown
Q6
CO-3;   [20]
SO-;
BL-3
10
Q6   B
CO-4;   10
SO-;   With a neat diagram, inspect the working of JK Flip Flop.
BL-2
Circuit diagram: 3 marks
Truth table: 3 marks   10
Explanation: 4 marks
Q7   A
CO-4;   Compare Latches and Flip flops.   10
SO-;
BL-2
********** 10 **********
--- page 11 ---
10
Q7   B   Illustrate the input and output characteristics of CE
CO-2;   configuration using the NPN transistor. Explain in detail   10
SO-s;
BL-2   different regions of operation.
Input characteristics: 4 marks
10
Output characteristics: 6 marks
********** 11 **********

[Text in pictures on this page, read by OCR]
Latches Flip flops

Latches are level triggered devices. _ Flip flops are edge triggered devices.

Flip flops can be classified as

No further classification for latches. asynchronous and synchronous.

Latches can be clocked or clockless. Flip flops are always clocked.
Latches are operated only with Flip flops are worked with both clock
binary inputs. and binary inputs.
Latches are faster as compared to Flip flops are slow compared to the
flip flops. latches.
Latches are constructed from logic Flip flops are constructed from
gates. latches along with an additional clock

signal.
````
