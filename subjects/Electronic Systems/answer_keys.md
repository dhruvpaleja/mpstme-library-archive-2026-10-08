# Electronic Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 6f464921a8e5

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Mechatronics_7004/Electronic Systems/ANS_Electronic Systems(702MH0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: mixed (15 pages), mean OCR confidence 71.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Electronic Systems
Date: 02 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Answer briefly:
Q1. CO- 1; SO- 1;   a.   Briefly explain Photodiode?   [04]
BL-1
Symbol-01 Mark
Explanation- 3 mark
CO- 3; SO- 1;   b. Draw a CMOS transmission gate circuit schematic. What gives it the   [04]
BL-1   name "transmission gate"?
********** 1 **********

[Text in pictures on this page, read by OCR]
. The CMOS transmission gate consists of one nMOS and one pMOS transistor, connected

in parallel.

. The gate voltages applied to these two transistors are also set to be complementary

signals.

. Thus, the CMOS TG operates as a bidirectional switch between the nodes A and B which

is controlled by signal C.

. If the control signal C is
* logic-high, i.e., equal to Vpp, then both transistors are turned on and provide a low-

resistance current path between the nodes A and B.

* low, then both transistors will be off, and the path between the nodes A and B will be

an open circuit. This condition is also called the high-impedance state.
--- page 2 ---
CO- 4; SO- 1;   c.   Briefly explain the working principle of Linear Regulated Power   [04]
BL-2   Supply
This is the conventional method of obtaining DC out of the input AC
supply. A linear power supply requires larger semiconductor devices
to regulate the output voltage and generates more heat resulting in
lower energy efficiency. Linear Power Supplies are widely used in
low-noise amplifiers, test equipment, control circuits. In addition, they
are also used in data acquisition and signal processing.
All the power supply systems that needs simple regulation and where
efficiency is not a concern, the LPS circuits are used. As the electrical
noise is lower, the LPS is used in powering sensitive analog circuitry.
Block Diagram-2 marks
Explanation-3 marks
CO- 4; SO- 1;   d.   [04]
What do you mean by Slew Rate of Op-amp? How is it important?
BL-2
The slew rate (SR) of an op-amp is the maximum rate at which the
output voltage can change in response to input voltage.
When the SR is too slow for the input, distortion results.
For example when a input sine wave is applied to a voltage follower
it produces a triangular output waveform.
The triangular waveform results because the op-amp simply cannot
move fast enough to follow the sine wave input.
This happens because voltage change in the second stage ( Voltage
Amplifier(s) ) is limited by the charging and discharging of capacitors.
The slew rate is expressed as : SR = ∆VO/∆t .The unit of SR is volts
per microseconds.
********** 2 **********
--- page 3 ---
CO- 4; SO- 1;   e.   Briefly describe the I to V converter using an Op-amp circuit.   [04]
BL-2
Circuit Diagram-01 Mark
Explanation-03 Marks
CO- 1; SO- 1;   a.   With the help of suitable diagram, explain the input and output   [10]
Q2.
BL-2   characteristics of Common Base configuration
Input Characteristics - 05 Marks
Input Characteristics - 05 Marks
CO- 3; SO- 1;   b.   Describe the IC-555 timer using a pin diagram. Give a detailed   [10]
BL-2   description of its astable operating mode.
********** 3 **********

[Text in pictures on this page, read by OCR]
Current to voltage Converter(! to V converter)

A current to voltage converter or I to V converter is an electronic circuit
that takes current as the input and produces voltage as the output. This section
discusses about the op-amp based current to voltage converter.

An op-amp based current to voltage converter produces an output voltage
when current is applied to its inverting terminal. The circuit diagram of an op-
amp based current to voltage converter is shown in the following figure.

a
{In the circult shown above, the non-inverting Input terminal of the op-amp Is

connected to ground. That means zero volts i epalied at its non-inverting input
terminal

According to the virtual short concept, the voltage atthe inverting input
‘terminal of an op-amp wil be equal to the voltage at its non-inverting input ve
terminal. So, the voltage at the inverting input terminal of the op-amp will be

zero volts,

The nodal equation at the inverting terminal's node is —

Thus, the output voltage, Vo of current to voltage converter is the (negative)
product of the feedback resistance, Ry and the input current, I;. Observe that
the output voltage, Vo is having a negative sign, which indicates that there

exists a 180° phase difference between the input current and output voltage.

We can re-write the above equation as —

Vo
—=-R
Ti f
The above equation represents the ratio of the output voltage Vp and the input
current J;, and it is equal to the negative of feedback resistance, Ry. The ratio
of output voltage Vo and input current J; is called as Transresistance.

We know that the ratio of output and input of a circuit is called as gain. So, the
gain of a current to voltage converter is its trans resistance and it is equal to
the (negative) feedback resistance Ry .
--- page 4 ---
Ground [4] 8 | +Vec

Trigger i 7 | Discharge
555
Output [3 | [6 | Threshold
Reset F] rs | Control Voltage

Pin Diagram IC-555 timer- 04 Marks

Vcc

3 [-—O Output

“TL

== 0.01pF

sseeee Discharge Path
—— Charging Path

Comparator 1
+ —
. R
s a
ta 3
> a
2 C Output

omparator 2

14

FIC 7) IC HOH
--- page 5 ---
Initially, on power-up, the flip-flop is RESET (and hence the output of
the timer is low). As a result, the discharge transistor is driven to
saturation (as it is connected to Q’). The capacitor C of the timing
circuit is connected at Pin 7 of the IC 555 and will discharge through
the transistor. The output of the timer at this point is low. The voltage
across the capacitor is nothing but the trigger voltage. So, while
discharging, if the capacitor voltage becomes less than 1/3 VCC,
which is the reference voltage to trigger comparator (comparator 2),
the output of the comparator 2 will become high. This will SET the
flip-flop and hence the output of the timer at pin 3 goes to HIGH.
This high output will turn OFF the transistor. As a result, the capacitor
C starts charging through the resistors R1 and R2. Now, the capacitor
voltage is same as the threshold voltage (as pin 6 is connected to the
capacitor resistor junction). While charging, the capacitor voltage
increases exponentially towards VCC and the moment it crosses 2/3
VCC, which is the reference voltage to threshold comparator
(comparator 1), its output becomes high.
As a result, the flip-flop is RESET. The output of the timer falls to
LOW. This low output will once again turn on the transistor which
provides a discharge path to the capacitor. Hence the capacitor C will
discharge through the resistor R2. And hence the cycle continues.
CO- 1; SO- 1;   a.   Determine VCE and IC in the voltage-divider biased transistor
Q3   BL-5   [10]
circuit. Assume β=50 and IE = IB + IC
********** 5 **********

[Text in pictures on this page, read by OCR]
Waveforms Of Capacitor Voltage And Output Voltage

; Charging
Capacitor Through R1 And R2
Voltage
Discharging
Through R2
2/3V.. : |
1/3V.,
Output
Voltage

be TON >

—> |rorr |—

— T+—
--- page 6 ---
Vth, Rth – 2 marks; Ib 1 mark; Ic-3 marks
Vce-3 marks Equivalent circuit – 1mark
CO- 2; SO- 1;   b.   Explain how an operational amplifier-based Wein Bridge oscillator works   [10]
BL-3   using a circuit schematic.
********** 6 **********

[Text in pictures on this page, read by OCR]
Ie - pee = = 50x35.935uA
TH DC E
=1.797mA
Here I, =I, +I, =1.797mMA +35.935uA
“I, =1.833mA
Vor = Voc —1Re —TpRz
= 20-1.797x1-1.833x1
=16.37V
--- page 7 ---
Circuit Diagram-04 Marks
Explanation-06 Marks
CO- 3; SO- 1;   a.   Describe in brief how CMOS is built and how a CMOS inverter   [10]
Q4
BL-2   operates.
Circuit Diagram-03 Marks
Construction-03 Marks
Working Principle -04 Marks
********** 7 **********

[Text in pictures on this page, read by OCR]
It comprises the NMOS transistor that has N++ regions at the
source and drain terminal and p-type substrate. similarly, the
PMOS transistor has two P++ regions and an n-type substrate.

Here, G, S, and D specifies the Gate,
Source, and Drain terminal of the NMOS and PMOS.

+ Let's consider the two states of the CMOS, when the input voltage (A) is 0
and 1.

+a) Ain the diagram is the input voltage that is fed to the NMOS and
PMOS transistors. When the input voltage (A) = OV, the PMOS conducts,
and NMOS will remain in the OFF A’ will become 1 when A is 0. Let's
represent such condition in the form of NO and NC switches, as shown
below.

* It means that the output voltage is considered as logic 1 because the
PMOS switch is closed and the NMOS switch at the bottom is open.

b) Similarly, when the input voltage A = 1, A’ will be 0. In such a state, the
PMOS will be OFF, and NMOS will conduct. Such state is represented
below.

It means that the output is 0 when the input is 1. The output voltage is
considered as logic 0 because the PMOS switch at the top is open and the
NMOS switch is closed.

+0

Input Cd

PMOS OFF NMOS ON
--- page 8 ---
CO- 4; SO- 1;   b.   Explain Logarithmic Amplifier that employs operational amplifier   [10]
BL-2
CO- 4; SO- 2;   a.   Utilizing a circuit diagram, illustrate the functioning of a Integrator   [10]
Q5
BL-2   circuit that employs an operational amplifier.
********** 8 **********

[Text in pictures on this page, read by OCR]
When the diode is forward biased, the current flowing through the diode is

Ip IeeVPOVD (2)
Where,
|, is the saturation current of the diode,
\V; is the voltage drop across diode, when it is in forward bias,
Vz is the diode's thermal equivalent voltage.
The KVL equation around the feedback loop of the op amp will be

0-Vi-Vo =0
Vi=-Vo

Substituting the value of V; in Equation 2, we get

l= IeVonvn) (3)

VJRq = geen)
--- page 9 ---
Circuit – 4
marks
Operation- 6 marks
CO-2; SO- 1;   b. Draw the pin diagram of Op-amp (IC-741) and derive the expression   [10]
BL-3   of gain for non-inverting mode.
Noninverting Amplifier:
There are times when we wish to have an output signal of the same
polarity as the input signal. In this case, the OP-amp is connected
as noninverting amplifier as shown in Fig.4. The input signal is
applied to the noninverting input (+). The output is applied back to
the input through the feedback circuit formed by feedback resistor
Rf and input resistance Ri. Note that resistors Rf and Ri form a
voltage divide at the inverting input (–). This produces *negative
feedback in the circuit. Note that Ri is grounded. Since the input
signal is applied to the noninverting input (+), the output signal
will be non-inverted i.e., the output signal will be in phase with
the input signal. Hence, the amplifier.
********** 9 **********

[Text in pictures on this page, read by OCR]
As before, point 4 will be treated as virtual ground.

Yo-Yo Yo = _,
Xo WjaC ~~ se ~~ °¥0
s = j@in the Laplace notation.
= i, Att, 68.26 (a) e
Yay é 4 § Xe
Ret yo i i,
% Vol 1
2 = st Ad
Vin vy, sCR ©
1
4 = -L
v SCR

Yo

~   L

Fig. 68.13
It is seen from above that output (right-hand
side expression) is an integral of the input, with an inversion and a scale factor of 1/CR.

2)

sre VG &
Offset Null] 1] 741 Op. Amp. | 8 | Not Connected (NC)

Inverting (—)} 2 7 | V+ (Power)

Non-Inverting (+) } 3 6 | Output

(Power) V-| 4 p=----= i 5 | Offset Null
--- page 10 ---
Fig.4 Non-inverting Amplifier
Voltage gain
If we assume that we are not at saturation, the potential at point A
is the same as Vin. Since the input impedance of OP-amp is very
high, all of the current that flows through Rf also flows through
Ri. Keeping these things in mind, we have,
Voltage across Ri = Vin – 0; Voltage across Rf = Vout – Vin,
Now   Current through Ri = Current through Rf
Or
Or   VinRf = VoutRi - VinRi
Vout / Vin = (Rf + Ri) / Ri
Therefore, closed loop voltage gain ACL = 1 + Rf / Ri
The following points may be noted about the noninverting amplifier:
ACL = 1 + Rf / Ri; The voltage gain of noninverting amplifier also
depends upon the values of Rf and Ri.
The voltage gain of a non-inverting amplifier can be made
equal to or greater than 1.
The voltage gain of a non- inverting amplifier will always be greater
than the gain of an equivalent inverting amplifier by a value of 1.
If an inverting amplifier has a gain of 150, the equivalent
noninverting amplifier will have a gain of 151.
The voltage gain is positive. This is not surprising because output
signal is in phase with the input signal.
Pin diagram – 3 marks
Derivation-7 marks
CO- 2; SO- 1;   a.   In the following clamper circuit, if the diode is assumed to be ideal and   [06]
BL-2   the value of resistance RL is very large, then draw the approximate
output waveform at steady condition
Q6
********** 10 **********
--- page 11 ---
5 marks
CO- 1; SO- 1;   b.   Explain Forward and Reverse Bias characteristics of pn junction diode   [06]
BL-2
In a piece of sc, if one half is doped by p type impurity and the other half is
doped by n type impurity, a PN junction is formed. The plane dividing the
two halves or zones is called PN junction. As shown in the fig the n type
material has high concentration of free electrons, while p type material has
high concentration of holes. Therefore, at the junction there is a tendency of
free electrons to diffuse over to the P side and the holes to the N side. This
process is called diffusion. As the free electrons move across the junction
from N type to P type, the donor atoms become positively charged. Hence a
positive charge is built on the N-side of the junction. The free electrons that
cross the junction uncover the negative acceptor ions by filing the holes.
Therefore, a negative charge is developed on the p –side of the junction. This
net negative charge on the p side prevents further
diffusion of electrons into the p side. Similarly, the net positive charge on the
N side repels the hole crossing from p side to N side. Thus a barrier sis set up
near the junction which prevents the further movement of charge carriers i.e.
electrons and holes. As a consequence of induced electric field across the
depletion layer, an electrostatic potential difference is established between P
and N regions, which are called the potential barrier, junction barrier,
diffusion potential or contact potential, Vo. The magnitude of the contact
potential Vo varies with doping levels and temperature. Vo is 0.3V for Ge
and 0.72 V for Si.
********** 11 **********
--- page 12 ---
Symbol of PN Junction Diode
The electrostatic field across the junction caused by the positively charged N-
Type region tends to drive the holes away from the junction and negatively
charged p type regions tend to drive the electrons away from the junction. The
majority holes diffusing out of the P region leave behind negatively charged
acceptor atoms bound to the lattice, thus exposing a negatives pace charge in
a previously neutral region. Similarly, electrons diffusing from the N region
expose positively ionized donor atoms and a double space charge builds up at
the junction as shown in the fig.
It is noticed that the space charge layers are of opposite sign to the majority
carriers diffusing into them, which tends to reduce the diffusion rate. Thus
the double space of the layer causes an electric field to be set up across the
junction directed from N to P regions, which is in such a direction to inhibit
the diffusion of majority electrons and holes as illustrated in fig. The shape
of the charge density, ρ, depends upon how diode id doped. Thus the junction
region is depleted of mobile charge carriers. Hence it is called depletion
layer, space region, and transition region. The depletion region is of the order
of 0.5µm thick. There are no mobile carriers in this narrow depletion region.
Hence no current flows across the junction and the system is in equilibrium.
Forward Biased Junction Diode
When a diode is connected in a Forward Bias condition, a negative voltage
is applied to the N-type material and a positive voltage is applied to the P-
type material. If this external voltage becomes greater than the value of the
potential barrier, approx. 0.7 volts for silicon and 0.3 volts for germanium,
the potential barriers opposition will be overcome and current will start to
flow. This is because the negative voltage pushes or repels electrons towards
the junction giving them the energy to cross over and combine with the holes
being pushed in the opposite direction towards the junction by the positive
voltage. This results in a characteristics curve of zero current flowing up to
this voltage point, called the "knee" on the static curves and then a high
current flow through the diode with little increase in the external voltage as
shown below.
Forward Characteristics Curve for a Junction Diode
********** 12 **********
--- page 13 ---
Diode Forward Characteristics
The application of a forward biasing voltage on the junction diode results in
the depletion layer becoming very thin and narrow which represents a low
impedance path through the junction thereby allowing high currents to flow.
The point at which this sudden increase in current takes place is represented
on the static I-V characteristics curve above as the "knee" point.
Reverse Biased Junction Diode
When a diode is connected in a Reverse Bias condition, a positive voltage is
applied to the N-type material and a negative voltage is applied to the P-type
material. The positive voltage applied to the N-type material attracts
electrons towards the positive electrode and away from the junction, while
the holes in the P-type end are also attracted away from the junction towards
the negative electrode. The net result is that the depletion layer grows wider
due to a lack of electrons and holes and presents a high impedance path,
almost an insulator. The result is that a high potential barrier is created thus
preventing current from flowing through the semiconductor material.
Reverse Characteristics Curve for a Junction Diode
Diode Reverse Characteristics
Sometimes this avalanche effect has practical applications in voltage
stabilizing circuits where a series limiting resistor is used with the diode to
limit this reverse breakdown current to a pre-set maximum value thereby
producing a fixed voltage output across the diode. These types of diodes are
commonly known as Zener Diodes.
CO- 2; SO- 1;   c. What is the significance of ripple factor in a rectifier circuit? Discuss   [08]
BL-2   the full wave bridge rectifier circuit along with capacitor filter in detail.
Significance of ripple factor in a rectifier circuit -03 Marks
FWR Circuit-03 Marks
********** 13 **********

[Text in pictures on this page, read by OCR]
Vz j Reverse Voltage, (-VR )

100 (80 60 40 20 0
1
i)
/ 10nA
!
' Reverse 100nA
Reverse 1 Bias
Breakdown _| || Region 1uA
Region i
a 10uA
i)
!
| ; 100uA
1
1 imaA

Reverse Current, (-Ip )
--- page 14 ---
Capacitor Filter-2 Marks
Explanation-2 marks
Q7. CO- 2; SO- 1;   a.
[05]
BL-1   Inverting Schmitt Trigger using Op-amp
Circuit Diagram -2 marks
Waveform-1 mark
Explanation-2 marks
CO- 4; SO- 1;   b.   Ideal and Practical Opamp   [05]
BL-1
5 points-5 marks
********** 14 **********
--- page 15 ---
CO- 3; SO- 1;   c.
[05]
BL-3   BJT as switch
Figure-02 Marks
Explanation-03 Marks
CO- 5; SO- 1;   d.   High Pass Filter using Op-map   [05]
BL-1
Circuit-2 marks
Explanation-3 marks
********** 15 **********

[Text in pictures on this page, read by OCR]
A high pass filter will allow the frequencies which are higher than the cut-off frequency and attenuate the
frequencies lower than the cut off frequency. In some cases, this filter is also termed as ‘Low-Cut’ filter or
‘Base-cut’ filter. By connecting a passive RC high pass filter circuit to the inverting or non-inverting terminal of
the op-amp gives us first order active high pass filter. The passive RC high pass filter circuit connected to the
non-inverting terminal of the unity gain operational amplifier is shown below.

Active High Pass Filter with High Voltage Gain:

The operation is same as that of the passive high pass filter, but the input signal is amplified by the amplifier at
the output. The amount of amplification depends on the gain of the amplifier. The magnitude of the pass band
gain is equal to 1 + (R,/R,). Where R3 is the feedback resistor in @ (ohms) and R, is the input resistor. The circuit
of active high pass filter with amplification is given below.
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 3027ac673486

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Mechatronics_7004/Electronic Systems/ANS_Electronic Systems(702MH0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: mixed (15 pages), mean OCR confidence 66.5
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Electronic Systems
Date: 29 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Answer briefly:
Q1. CO- 1; SO- 1;   a.   Briefly explain LED?   [04]
BL-1
Symbol-01 Mark
Explanation- 3 mark
CO- 3; SO- 1;   b.   Draw the circuit diagram of CMOS transmission gate. Why is it called as   [04]
BL-1   transmission gate?
********** 1 **********

[Text in pictures on this page, read by OCR]
. The CMOS transmission gate consists of one nMOS and one pMOS transistor, connected

in parallel.

. The gate voltages applied to these two transistors are also set to be complementary

signals.

. Thus, the CMOS TG operates as a bidirectional switch between the nodes A and B which

is controlled by signal C.

. If the control signal C is
* logic-high, i.e., equal to Vpp, then both transistors are turned on and provide a low-

resistance current path between the nodes A and B.

* low, then both transistors will be off, and the path between the nodes A and B will be

an open circuit. This condition is also called the high-impedance state.
--- page 2 ---
CO- 4; SO- 1;   c.   What is SMPS and how it works?   [04]
BL-2
Like other types of power supply, a SMPS power supply transfers
power from a source usually an AC outlet to a DC device. What sets
the SMPS apart is its ability to regulate the output voltage. It can
increase or decrease the output voltage to maintain a constant output
regardless of changes in load. This dual ability gives it an advantage
over linear regulators, which can only regulate the output down (that
is, they can only decrease the voltage, not increase it).
CO- 4; SO- 1;   d.   [04]
What do you mean by CMRR of Op-amp? How is it important?
BL-2
CO- 4; SO- 1;   e.   What is I to V Converter? List down any of its two applications.   [04]
BL-2
********** 2 **********

[Text in pictures on this page, read by OCR]
© The ability of amplifier to reject the common-mode
signals (unwanted signals) while amplifying the
differential signal (desired signal).

e

© Ratio of open-loop gain, A, to common-mode gain, A,,

A,,

CMRR= CMRR= 20 log

= The higher the CMRR, the better, in which the open-loop
gain is high and common-mode gain is low.

= CMRR is usually expressed in dB & decreases with
frequency.
--- page 3 ---
Circuit Diagram-01 Mark
Explanation-03 Marks
CO- 1; SO- 1;   a.   With the help of suitable diagram, explain the active mode of   [10]
Q2.
BL-2   operation of PNP Transistor.
Circuit Diagram-03 Marks
Explanation - 07 Marks
CO- 3; SO- 1;   b.   With the help of pin diagram explain the IC-555 timer. Provide a   [10]
BL-2   comprehensive description of its monostable operational mode.
********** 3 **********

[Text in pictures on this page, read by OCR]
Current to voltage Converter(! to V converter)

A current to voltage converter or I to V converter is an electronic circuit
that takes current as the input and produces voltage as the output. This section
discusses about the op-amp based current to voltage converter.

An op-amp based current to voltage converter produces an output voltage
when current is applied to its inverting terminal. The circuit diagram of an op-
amp based current to voltage converter is shown in the following figure.

a
{In the circult shown above, the non-inverting Input terminal of the op-amp Is

connected to ground. That means zero volts i epalied at its non-inverting input
terminal

According to the virtual short concept, the voltage atthe inverting input
‘terminal of an op-amp wil be equal to the voltage at its non-inverting input ve
terminal. So, the voltage at the inverting input terminal of the op-amp will be

zero volts,

The nodal equation at the inverting terminal's node is —

Thus, the output voltage, Vo of current to voltage converter is the (negative)
product of the feedback resistance, Ry and the input current, I;. Observe that
the output voltage, Vo is having a negative sign, which indicates that there

exists a 180° phase difference between the input current and output voltage.

We can re-write the above equation as —

Vo
—=-R
Ti f
The above equation represents the ratio of the output voltage Vp and the input
current J;, and it is equal to the negative of feedback resistance, Ry. The ratio
of output voltage Vo and input current J; is called as Transresistance.

We know that the ratio of output and input of a circuit is called as gain. So, the
gain of a current to voltage converter is its trans resistance and it is equal to
the (negative) feedback resistance Ry .
--- page 4 ---
Ground [4] 8 | +Vcc

Trigger i 7 | Discharge
555
Output [3 | [6 | Threshold
Reset F] rs | Control Voltage

Pin Diagram IC-555 timer- 04 Marks

Vee (+5 to+15V)

Trigger
$Vec _ ie _____ Pulse
8} 4 2
3g Voc Te Capacitor
R2 RI ( Voltage. Ve
555 :
7

Monostable 1
Monostable
t Output
3 Se.
6 OUT |}
1 f )
0 | J 2 t=117RI1C1)

IN

Negative
Trigger _| start = 5 1
Pulse
c c2

TI Fw

When a negative ( OV) pulse is applied to the trigger input (pin 2) of the Monostable
configured 555 Timer oscillator, the internal comparator, (comparator No‘) detects this
input and “sets” the state of the flip-flop, changing the output from a “LOW” state to a
“HIGH’ state. This action in turn turns “OFF” the discharge transistor connected to pin 7,
thereby removing the short circuit across the external timing capacitor, C1.

This action allows the timing capacitor to start to charge up through resistor, R1 until the
voltage across the capacitor reaches the threshold (pin 6) voltage of 2/3Vcc set up by the
internal voltage divider network. At this point the comparators output goes “HIGH” and
“resets” the flip-flop back to its original state which in turn turns “ON” the transistor and
discharges the capacitor to ground through pin 7. This causes the output to change its
state back to the original stable “LOW” value awaiting another trigger pulse to start the
timing process over again. Then as before, the Monostable Multivibrator has only “ONE”

stable state.

FIC 7) IC HOH
--- page 5 ---
CO- 1; SO- 1;   a.   For the given BJT biasing circuit, calculate the coordinates of Q-point
BL-5   (Assume VBE=0.7 V, β=100).
Q3   [10]
Vth, Rth – 2 marks; Ib 1 mark; Ic-3 marks
Vce-3 marks Equivalent circuit – 1mark
CO- 2; SO- 1;   b.   Construct the Instrumentation amplifier using Op-amp and obtain its output   [10]
BL-3   expression.
********** 5 **********

[Text in pictures on this page, read by OCR]
The Monostable 555 Timer circuit triggers on a negative-going pulse applied to pin 2 and
this trigger pulse must be much shorter than the output pulse width allowing time for the
timing capacitor to charge and then discharge fully. Once triggered, the 555 Monostable
will remain in this “HIGH” unstable output state until the time period set up by the Ry x Cy.
network has elapsed. The amount of time that the output voltage remains “HIGH” or ata

logic “1” level, is given by the following time constant equation.
T=11R,C,

Where, tis in seconds, R is in Q and C in Farads.

5x10°

R
Vr = 2 Veg = x10 = 3.33 V
T* RitRy So   tpxio? +5x10°
10x5
Re a0 ee
ying KVL to the base circuit we get,
Vr-IpRp- Vee - (1+B)Iy Re = 0
— Vr-Vee _ 3.33 -0.7 48.86 pA

Re+(+B)Re 333x104 (101)500 —
Io = Blg = 100x 48.86 PA = 4.886 mA
Ig = 4.935 mA
ving KVL to collector circuit we have,
= 10-—4,886x 1- 4.935x 0.5 = 2.6465 V
--- page 6 ---
Circuit Diagram-04 Marks
Derivation of output-06 Marks
CO- 3; SO- 1;   a.   Briefly explain the construction of CMOS and working principle of   [10]
Q4
BL-2   CMOS Inverter
********** 6 **********

[Text in pictures on this page, read by OCR]
It comprises the NMOS transistor that has N++ regions at the
source and drain terminal and p-type substrate. similarly, the
PMOS transistor has two P++ regions and an n-type substrate.

Here, G, S, and D specifies the Gate
Source, and Drain terminal of the NMOS and PMOS.

+ Let's consider the two states of the CMOS, when the input voltage (A) is 0
and 1.

+a) Ain the diagram is the input voltage that is fed to the NMOS and
PMOS transistors. When the input voltage (A) = OV, the PMOS conducts,
and NMOS will remain in the OFF A' will become 1 when A is 0. Let's
represent such condition in the form of NO and NC switches, as shown
below.

+ It means that the output voltage is considered as logic 1 because the
PMOS switch is closed and the NMOS switch at the bottom is open.

b) Similarly, when the input voltage A = 1, A’ will be 0. In such a state, the
PMOS will be OFF, and NMOS will conduct. Such state is represented
below.

It means that the output is 0 when the input is 1. The output voltage is
considered as logic 0 because the PMOS switch at the top is open and the
NMOS switch is closed.

+0

Input Cd

PMOS OFF NMOS ON
--- page 7 ---
Circuit Diagram-03 Marks
Construction-03 Marks
Working Principle -04 Marks
CO- 4; SO- 1;   b. What is the significance of Precision Rectifiers? Explain the operation   [10]
BL-2   of Full wave Precision Rectifier.
Significance- 3 marks
The op-amp circuits used as rectifiers are called precision rectifiers.
Usually, the AC voltages below the forward voltage drop of 0.7V of a
diode cannot be rectified. To overcome such problems, we use
precision rectifiers.
The precision rectifier has the capability of rectifying voltages which
are of smaller magnitude than the forward voltage drops. The
application of these diodes is in AM detectors where only information
is required in the signal with negligible power.
Circuit Diagram-03 Marks
Explanation-4 Marks
********** 7 **********

[Text in pictures on this page, read by OCR]
To make a full-wave precision rectifier circuit, | have just added a summing amplifier to the output of the
previously mentioned half-wave rectifier circuit. From the point, P1 to point P2 is the basic precision rectifier
circuit and the diode is so configured that we get a negative voltage at the output.

From the point, P2 to point P3 is the summing amplifier, the output from the precision rectifier is fed to the
summing amplifier through the resistor R3. The value of the resistor R3 is half of R5 or you can say it's R5/2 that is
how we are setting a 2X gain out of the op-amp.

The input from the point P1 is also fed to the summing amplifier with the help of the resistor R4, the resistors R4
and RS are responsible for setting the gain of the op-amp to 1X.

Since the output from the Point P2 is fed directly to the summing amplifier with the gain of 2X, that means the
output voltage will be 2-times the input voltage. Let's assume the input voltage is 2V peak, so we will get a 4V
peak at the output. At the same time, we are directly feeding the input to the summing amplifier with a gain of 1X.

Now when the summing operation happens we get a summed up voltage at the output which is (-4V) + (+2V) =
-2V and as the op-amp at the output. As the op-amp is configured as an inverting amplifier, we will get +2V at the
‘output which is the point P3.

The same thing happens when the negative peak of the input signal is applied.
--- page 8 ---
CO- 4; SO- 2;   a.   Utilizing a circuit diagram, illustrate the functioning of a Differentiator   [10]
Q5
BL-2   circuit that employs an operational amplifier.
Circuit – 4 marks
Operation- 6 marks
CO-2; SO- 1;   b. Draw the pin diagram of Op-amp (IC-741) and derive the expression   [10]
BL-3   of gain for inverting mode.
An OP-amp has an infinite input impedance. This means that there is zero
current at the inverting input. If there is zero current through the input
impedance, then there must be no voltage drop between the inverting and
non- inverting inputs. This means that voltage at the inverting input (–) is
zero (point A) because the other input (+) is grounded. The 0V at the
inverting input terminal (point A) is referred to as virtual ground. This
condition is illustrated in Fig.3. The point A is said to be at virtual ground
because it is at 0V but is not physically connected to the ground (i.e. VA =
0V).
********** 8 **********

[Text in pictures on this page, read by OCR]
sre VG &
Offset Null] 1] 741 Op. Amp. | 8 | Not Connected (NC)

Inverting (—)} 2 7 | V+ (Power)

Non-Inverting (+) } 3 6 | Output

(Power) V-| 4 p=----= i 5 | Offset Null
--- page 9 ---
Fig.3   (i)   (ii)
Referring to Fig. 3(ii), the current I1 to the inverting input is zero. Therefore,
current Iin flowing through Ri entirely flows through feedback resistor Rf. In
other words, If = Iin.
Now
And
Since If = Iin,   V0 /(- Rf) = (Vin) / Ri
Therefore, Voltage gain ACL = (Vout / Vin) = - (Rf / Ri)
The negative sign indicates that output signal is inverted as compared to the
input signal. The following points may be noted about the inverting
amplifier:
(i)   The closed-loop voltage gains (ACL) of an inverting amplifier is the
ratio of the feedback resistance Rf to the input resistance Ri. The closed-
loop voltage gain is independent of the OP-amp’s internal open-loop voltage
gain. Thus the negative feedback stabilises the voltage gains.
(ii)   The inverting amplifier can be designed for unity gain. Thus if Rf =
Ri, then voltage gain ACL = –1. Therefore, the circuit provides a unity voltage
gain with 180° phase inversion.
(iii)   If Rf is some multiple of Ri, the amplifier gain is constant. For
example, if Rf = 10 Ri, then ACL = –10 and the circuit provides a voltage gain
of exactly 10 along with a 180° phase inversion from the input signal. If we
select precise resistor values for Rf and Ri, we can obtain a wide range of
voltage gains. Thus the inverting amplifier provides constant voltage gain.
CO- 2; SO- 1;   a. Draw the output waveform across R1 of the following circuit.   [06]
BL-2
Q6
********** 9 **********
--- page 10 ---
CO- 1; SO- 1;   b. How does the PN Diode work in different biasing conditions? Also   [06]
BL-2   draw its VI-characteristics.
In a piece of sc, if one half is doped by p type impurity and the other half is
doped by n type impurity, a PN junction is formed. The plane dividing the
two halves or zones is called PN junction. As shown in the fig the n type
material has high concentration of free electrons, while p type material has
high concentration of holes. Therefore, at the junction there is a tendency of
free electrons to diffuse over to the P side and the holes to the N side. This
process is called diffusion. As the free electrons move across the junction
from N type to P type, the donor atoms become positively charged. Hence a
positive charge is built on the N-side of the junction. The free electrons that
cross the junction uncover the negative acceptor ions by filing the holes.
Therefore, a negative charge is developed on the p –side of the junction. This
net negative charge on the p side prevents further
diffusion of electrons into the p side. Similarly, the net positive charge on the
N side repels the hole crossing from p side to N side. Thus a barrier sis set up
near the junction which prevents the further movement of charge carriers i.e.
electrons and holes. As a consequence of induced electric field across the
depletion layer, an electrostatic potential difference is established between P
and N regions, which are called the potential barrier, junction barrier,
diffusion potential or contact potential, Vo. The magnitude of the contact
potential Vo varies with doping levels and temperature. Vo is 0.3V for Ge
and 0.72 V for Si.
********** 10 **********

[Text in pictures on this page, read by OCR]
During the positive half cycle, the diode remains to turn off for a small part of the input
waveform. This is because of the DC source (3V) at the anode. To make the diode forward
biased, the anode should more positive than the cathode.

V1 > (3+0.7)V .... Tum on condition
Where
V1 = input voltage
0.7V is the forward voltage drop
As the diode turns on, the capacitor charges till the peak value.
-V1 + VC1+0.7+3 = 0
VC1= 10-37
VC1=6.3V

During the negative half-cycle, the diode remains off. To determine output voltage, apply KVL
to the loop.

V1+VC1+V,=0
10 +6.3+V,=0
V,=-16.3V

Output voltage clamps and swings from -16.3 V to 3.7 V.
--- page 11 ---
Symbol of PN Junction Diode
The electrostatic field across the junction caused by the positively charged N-
Type region tends to drive the holes away from the junction and negatively
charged p type regions tend to drive the electrons away from the junction. The
majority holes diffusing out of the P region leave behind negatively charged
acceptor atoms bound to the lattice, thus exposing a negatives pace charge in
a previously neutral region. Similarly, electrons diffusing from the N region
expose positively ionized donor atoms and a double space charge builds up at
the junction as shown in the fig.
It is noticed that the space charge layers are of opposite sign to the majority
carriers diffusing into them, which tends to reduce the diffusion rate. Thus
the double space of the layer causes an electric field to be set up across the
junction directed from N to P regions, which is in such a direction to inhibit
the diffusion of majority electrons and holes as illustrated in fig. The shape
of the charge density, ρ, depends upon how diode id doped. Thus the junction
region is depleted of mobile charge carriers. Hence it is called depletion
layer, space region, and transition region. The depletion region is of the order
of 0.5µm thick. There are no mobile carriers in this narrow depletion region.
Hence no current flows across the junction and the system is in equilibrium.
Forward Biased Junction Diode
When a diode is connected in a Forward Bias condition, a negative voltage
is applied to the N-type material and a positive voltage is applied to the P-
type material. If this external voltage becomes greater than the value of the
potential barrier, approx. 0.7 volts for silicon and 0.3 volts for germanium,
the potential barriers opposition will be overcome and current will start to
flow. This is because the negative voltage pushes or repels electrons towards
the junction giving them the energy to cross over and combine with the holes
being pushed in the opposite direction towards the junction by the positive
voltage. This results in a characteristics curve of zero current flowing up to
this voltage point, called the "knee" on the static curves and then a high
current flow through the diode with little increase in the external voltage as
shown below.
Forward Characteristics Curve for a Junction Diode
********** 11 **********
--- page 12 ---
Diode Forward Characteristics
The application of a forward biasing voltage on the junction diode results in
the depletion layer becoming very thin and narrow which represents a low
impedance path through the junction thereby allowing high currents to flow.
The point at which this sudden increase in current takes place is represented
on the static I-V characteristics curve above as the "knee" point.
Reverse Biased Junction Diode
When a diode is connected in a Reverse Bias condition, a positive voltage is
applied to the N-type material and a negative voltage is applied to the P-type
material. The positive voltage applied to the N-type material attracts
electrons towards the positive electrode and away from the junction, while
the holes in the P-type end are also attracted away from the junction towards
the negative electrode. The net result is that the depletion layer grows wider
due to a lack of electrons and holes and presents a high impedance path,
almost an insulator. The result is that a high potential barrier is created thus
preventing current from flowing through the semiconductor material.
Reverse Characteristics Curve for a Junction Diode
Diode Reverse Characteristics
Sometimes this avalanche effect has practical applications in voltage
stabilizing circuits where a series limiting resistor is used with the diode to
limit this reverse breakdown current to a pre-set maximum value thereby
producing a fixed voltage output across the diode. These types of diodes are
commonly known as Zener Diodes.
CO- 2; SO- 1;   c.   What is the significance of ripple factor in a rectifier circuit? Discuss the full   [08]
BL-2   wave bridge rectifier circuit along with waveforms in detail.
significance of ripple factor in a rectifier circuit -03 Marks
FWR Circuit-03 Marks
********** 12 **********

[Text in pictures on this page, read by OCR]
Vz j Reverse Voltage, (-VR )

100 (80 60 40 20 0
1
i)
/ 10nA
!
' Reverse 100nA
Reverse 1 Bias
Breakdown _| || Region 1uA
Region i
a 10uA
i)
!
| ; 100uA
1
1 imaA

Reverse Current, (-Ip )
--- page 13 ---
Capacitor Filter-2 Marks
Q7. CO- 2; SO- 1;   a.
BL-1   Logarithmic Amplifier using Op-Amp   [05]
The analysis of the circuit of Fig. 9 mirrors that of Fig. 8. Imposing iR
= iC, we now get (vI −0)/R =C d(0−vO)/dt, or dvO(t)=(−1/RC) vI (t) dt.
Changing t to the dummy integration variable ξ and then integrating
both sides from0 to t yields
Fig. The Op – Amp Integrator.
--------------- (2)
where vO(0) is the value of the output at t = 0. This value depends on
the charge initially stored in the capacitor. Equation (2) indicates that
the output is proportional to the time integral of the input—hence the
name. The proportionality constant is set by R and C, but its units are
now s−1. Mirroring the analysis of the inverting amplifier, you can
readily verify that   Ri =R & Ro = 0. Thus, if the driving source has
an output resistance Rs , in order to apply Eq. (2) we must replace R
with Rs + R.
The op amp integrator, also called a precision integrator because of
the high degree of accuracy with which it can implement Eq. (2), is a
workhorse of electronics. It finds wide application in function
generators (triangle and sawtooth wave generators), active filters
(state-variable and biquad filters, switched-capacitor filters), analog-
to-digital converters (dual-slope converters, quantized-feedback
converters), and analog controllers (PID controllers).
CO- 3; SO- 1;   c.
[05]
BL-3   BJT as switch
********** 13 **********
--- page 14 ---
Figure-02 Marks
Explanation-03 Marks
CO- 4; SO- 1;   b.   Slew Rate of Op-amp
[05]
BL-1
The slew rate (SR) of an op-amp is the maximum rate at which the
output voltage can change in response to input voltage.
When the SR is too slow for the input, distortion results.
For example when a input sine wave is applied to a voltage follower
it produces a triangular output waveform.
The triangular waveform results because the op-amp simply cannot
move fast enough to follow the sine wave input.
This happens because voltage change in the second stage ( Voltage
Amplifier(s) ) is limited by the charging and discharging of capacitors.
The slew rate is expressed as : SR = ∆VO/∆t .The unit of SR is volts
per microseconds.
CO- 5; SO- 1;   d.   Band Pass Filter using Op-map
[05]
BL-1
The first stage of the filter will be the high pass stage that uses the
capacitor to block any DC biasing from the source.
This design has the advantage of producing a relatively flat
asymmetrical pass band frequency response with one half representing
the low pass response and the other half representing high pass
response as shown.
********** 14 **********

[Text in pictures on this page, read by OCR]
High Pass Low Pass

Filter Stage Amplification Filter Stage
—— C1

rem h | E N)
Av MN .e)
Vin R1 Ra __
c2 Vout

R3 |
Ov
--- page 15 ---
High Pass Low Pass Band Pass

-3dB | -5 ee == ——

FRR IC 7 DA HOH
````
