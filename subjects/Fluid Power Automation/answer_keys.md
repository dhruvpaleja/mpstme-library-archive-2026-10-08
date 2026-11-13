# Fluid Power Automation: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 00c570b92f96

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_Mechatronics_7004/Fluid Power Automation/ANS_Fluid Power Automation(702MH0E020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Dec 2025
- Text: ocr (11 pages), mean OCR confidence 85.2
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS

SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Fluid Power Automation
Date: 05 Dec 2025 Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. | is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Inall 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.

Ql.

a) Classification of pneumatic directional control valves (DCV) based on design principle. - 02 M
e Poppet valve
e Spool valve
Classification of pneumatic DCVs based on method of operation. - 03 M
e Direct operated
e Pilot operated
e Manual, Mechanical, Electric, Pneumatic. Electro-pneumatic and Spring operated.

b) ISO Symbol for Pneumatic FRL unit. - 02 M

ISO Symbol for 4/3 solenoid actuated spring return DCV with float centre. - 03 M
AB
pt

FSR 7 ok OR ARR oR
--- page 2 ---
c) Advantages of DC solenoids. — 03 M
e No burning through
e High switching frequency
e Softer switching
e Insensitive to overloading
Disadvantages of DC solenoids. — 02 M
e Slower in operation
e Higher price
e Higher control expenditure

d) Diagram of closed loop hydraulic position control circuit. -02 M

M

T
| Cylinder

sigral
potentiometer

A B

KAAS Pe ok
< I<
Sarvo valve

a BD LA pk oc;

a i

Feedbac« + ¥o
potentio- w=) [>
meter

Amplifier

Analysis of its operation emphasizing the role of feedback. — 03 M

A closed-loop hydraulic position control system is designed to accurately position a hydraulic actuator
by continuously comparing its actual position with a desired setpoint and adjusting the control signal
accordingly. The system typically includes a hydraulic cylinder, a proportional or servo valve, a
position sensor such as potentiometer and a controller. When a position command is given, the
controller sends a signal to the valve, regulating fluid flow and pressure to move the actuator. The
position sensor simultaneously measures the actual displacement and sends this feedback to the
controller. The controller compares the actual position with the desired position and generates an error
signal, which is used to adjust the valve opening until the actuator reaches the commanded position.
Feedback plays a crucial role in enhancing the accuracy, stability, and responsiveness of the system.
If the actuator overshoots or undershoots the target, the feedback loop detects the deviation and
instantly corrects the valve control signal to bring the actuator back to the precise position. This
continuous error correction minimizes steady state error, reduces oscillations, and compensates for
external disturbances such as load variations or supply pressure fluctuations. As a result, closed-loop
hydraulic position control systems achieve high precision and repeatability, making them ideal for
applications like CNC machines, robotic arms, and automated manufacturing systems.

FR 2 ok CR AK oR
--- page 3 ---
Q2.
a) Design diagram of a hydraulic circuit for speed and direction control of a Bidirectional hydraulic
motor using Hydraulic Pump, Tank, Filter, Pressure relief valve (PRV), Flow control valve
(FCV), 4/3 Manually operated spring centered DCV with Tandem center . - 10 M

ATES
L|
We
OL...
e Ae

b) Design diagram of a hydraulic circuit using double acting cylinder, 4/2 solenoid actuated
spring return DCV, Pressure relief valve (PRV) and Flow control valve (FCV) with check valve
for the pressing operation. - 05 M

© BI
a=
pwe
(Dw12)
=
LCS lorax
Cl
Al |B rely
v1 |! x
owse Tt TW pz2s + —(f) 021. : Wh petx
P| [rt a ae
ls P T t

FOCI ICO IC ACA CA ka
--- page 4 ---
Design diagram of an electrical control circuit using push buttons, proximity sensor, relays and
solenoids. - 05 M

1 2 3 4 5
+24V0 a -

3 Th 21

s5E K1 K1
4 14 24
Bi] &
——
at
a,
42
Al AI y4

K1 K2
OF a x
ove <>
Q3.

a) Identification of the components used in the given pneumatic actuation system. - 05 M
Double acting pneumatic cylinder with magnetic piston, external piston rod thread and adjustable
cushioning (2 numbers), Flow control valve (FCV) with check valve (2 numbers), 5/2 Directional
control valve, pneumatically actuated Impulse Valve (2 numbers), 3/2 Directional control valve
mechanically actuated, Spring return with Roller lever (4 numbers) and 3/2 Directional control valve
push button actuated

Explanation of the operation of the given pneumatic actuation system. - 05 M

The figure represents a two-cylinder pneumatic sequencing for the sequence A+ B+ A- B-.

This is a non-overlapping sequence as no signal conflict happens in it.

In this circuit two double acting cylinders A and B are controlled using roller lever operated 3/2 DCVs
as limit valves and 5/2 impulse valves as the main control valves. When the start push-button So is
pressed, compressed air is supplied to extend cylinder A (A+). As A reaches its forward end position,
it actuates a roller lever-operated 3/2 valve S2, which sends a pilot signal to the 5/2 valve controlling
cylinder B, causing it to extend (B+). Thus, the forward stroke of cylinder B depends on the completion
of the forward stroke of cylinder A, establishing a sequential interlock.

Once cylinder B reaches its forward end position, it actuates another roller lever-operated 3/2 valve S4
that sends a signal to reverse the 5/2 valve controlling cylinder A, causing A to retract (A—). When A
reaches its retracted position, it triggers another limit valve S; that pilots the 5/2 valve of cylinder B,
initiating its retraction (B—). This completes the desired sequence A+ B+ A— B-.

b) Block diagram of a PLC based closed loop pneumatic force control system. - 05 M

Discussion of its operation with reference to control technique. - 03 M

Comparison with open loop system. -02 M

A closed-loop pneumatic force control system is designed to maintain a desired force output from a
pneumatic actuator by continuously adjusting air pressure based on feedback signals. In such a system,
the pneumatic cylinder applies force to a workpiece, and a force sensor measures the actual output.
The signal from this sensor is fed to a PLC controller, which compares it with the desired setpoint. The
controller then sends a control signal to a proportional pressure control valve, adjusting the air supply

FR ok RAK oR
--- page 5 ---
to correct any deviation between the actual and desired force. This ensures precise, stable force control
during pressing, clamping, or assembly operations in industrial automation.

In this system, cascade control is achieved by using two nested feedback loops an inner loop for
pressure control and an outer loop for force control. The inner loop ensures that the valve regulates
pressure quickly and accurately, while the outer loop uses force feedback to fine-tune the actuator’s
performance. The outer loop determines the required pressure to achieve the desired force and sends
that setpoint to the inner pressure loop. This hierarchical control structure enhances system stability,
responsiveness, and accuracy, making the cascade-controlled pneumatic system highly suitable for
industrial applications where consistent and repeatable force output is critical.

Comparison: A PLC-based closed-loop pneumatic force control system continuously monitors and
adjusts the output force using feedback from a force sensor, ensuring high precision and stability even
under varying loads or pressure conditions. The PLC compares the actual force with the desired
setpoint and modulates the proportional valve to minimize any error, resulting in accurate and
repeatable control. In contrast, an open-loop system operates without feedback; it relies solely on
preset valve positions or air pressure settings, making it simpler but less accurate, as it cannot
compensate for disturbances or system variations. Thus, the closed-loop system provides superior
accuracy, adaptability, and consistency, while the open-loop system is suitable only for less critical or
cost-sensitive applications.

Force control

Command
Con- value
trol Actual value force
Actual value

PLC pressure

Actual value pressure (diagnosis)

Ly E
> > i les } Cylinders Sensor]
DOOG USE

U FE

>) DOOG i

F 5

Pressure control valve

Q4.

a) Comparison between Pneumatic and Hydraulic actuation systems based on energy carrier,
components used, power density, parameters, efficiency, linear movements, path accuracy,
controlling techniques, advantages, limitations and applications. - 07M
Discussion of applications of pneumatic actuation system in the following industries. — 03 M

e Food processing industry

e Packaging industry

e Wood industry

e Paper industry

e Printing and Processing industry
e Automobile industry

--- page 6 ---
b) The design of printing application requires extending a double acting pneumatic cylinder and
retracting it after a time delay of 5 seconds which can be provided using timer relays.
This circuit can be implemented using an electro-pneumatic system with 5/2 impulse valve, FCVs with
check valves, magnetic reed switches, relay, push button, timer relay and solenoids.
Design diagram of a pneumatic circuit a ee components and symbols. - 05 M

A

riot

nay

iT oJ L wm nied

12
ald \ vA RY
V| V5

1

Design diagram of an electrical control circuit using push button, relay, magnetic reed switches,
timer relay and solenoids. — 05 M

1 2 3 4

+24 + T
so E--\ K1\ 2 -€4

Bt of 82 |I\|_

ft

KD] epol vi4Ztxy Hr

OV

FOCI 6 ACE ACH a Ak a
--- page 7 ---
QS.

a) The application requires pneumatic sequencing circuit for two cylinders A and B for the
operating sequence A+, B+, B- , A-. This is an overlapping circuit which can be implemented using
an electro-pneumatic system with 5/2 solenoid actuated spring return DCVs, FCVs with check valves,
magnetic reed switches, relays, push button and solenoids.

Design diagram of a pneumatic circuit using appropriate components and symbols. - 05 M

B1 B2 B3 B4
| 1 I I

En a |,
"Zl Ill Ay
; Y2 ia a

Design diagram of an electrical control circuit using push button, relays, magnetic reed
switches and solenoids. — 05 M

+24V
B2 B4 B3
Ki K2

sof-\ «1 Koy) K2\ |EO\L 3\ [EO

BID
1 K3 7

ka Ki K2 K3
K1 K2 as K3 a5 K4 2 ran eX

ov

FRR 7 fk ck ak oR &
--- page 8 ---
b) The PLC based control system will require less number of wires as compared to the relay based
controller. In this the control is provided through the program rather than electrical hardwired
contoller.

Interfacing diagram showing the connection of sensor, switches and solenoids to PLC I/O
modules. - 03 M

INPUT OUTPUT
MODULES MODULES

START S2
MAGNETIC REED SWITCH B1

MAGNETIC REED SWITCH B2 DCV SOLENOID Z1
MAGNETIC REED SWITCH B3 PLC DCV SOLENOID Z2
MAGNETIC REED SWITCH B4
The ladder logic program with proper addressing. — 07 M
start2 bl x4 ki
] IL }] {|} {{
T Ue we u
ki
4 |
Ud
b2 kL k2
4 | jj {
Ut Ut v
2
4 {L
Ut
b4 k2 3
4} IL jj {
Ut Ue u
k3
4) fh
Ud
b3 k3 ka
—! IL 4} fL {)
T UE Y
ki zi
{)
k2 3 22

t tt {)

FCI ACO ACH ACH a Ak a
--- page 9 ---
Q6.
a) Diagram of a power steering mechanism using a priority valve and Ackerman / Articulated
steering. - 04M

SHUT OFF VALVE TANE
Pp
cr
PCV
P T
STEERING
R
t I
A
B B

Explanation of the operation of power steering mechanism using priority valve. - 06 M

A priority valve is a flow control device used in hydraulic systems to ensure that critical functions
receive a steady flow of hydraulic fluid before supplying the remaining flow to secondary functions.
It generally consists of a valve body, inlet port from the pump, control flow port, excess flow port,
spool or piston, and a spring mechanism. The spool is positioned such that when fluid enters from the
inlet, it first directs flow to the control flow port until a preset flow rate or pressure is achieved. Once
this requirement is met, the spool shifts to allow the remaining fluid to pass through the excess flow
port to auxiliary circuits.

In power steering operation, when the hydraulic pump supplies fluid, the priority valve maintains a
constant flow to Ackerman or articulated steering mechanism regardless of variations in system load
or pump output. If the flow demand increases or pump speed decreases, the valve automatically
restricts or blocks flow to secondary circuits to ensure uninterrupted operation of the priority function.
When the flow is not needed by the control port circuit then the secondary circuit connected to the
excess flow port receives the fluid supply. This makes the priority valve vital in hydraulic actuation
systems, as it ensures safety, reliability, and efficient energy use by maintaining performance of critical
operations even under fluctuating supply conditions.

b) Block diagram of a proportional hydraulic system showing various components. - 05 M
Explanation of the operation of proportional hydraulic system. - 05 M

electrical Ba
input _ MRAM Proportional solenoid Proportional uae draulic FAR
sional a a : with directional valve Mumma ne eeetine
P current/position conversion sition pressure valve cylinder,
current/force conversion (ug as, motor

cases
voltage

FCIAC OQ) ACR ACH AK a
--- page 10 ---
Q7.
a) Comparison between the open hydraulic circuit and closed hydraulic circuit based on
construction, fluid flow path, advantages, disadvantages, applications. - 05 M

b) Diagram of a rotary pneumatic actuator. - 02 M
Explanation of its operation. - 03 M
1 Pressure port 30 04¢0¢8 67 8 9
2 Pressure port

3 End position cushioning

4 Housing
4 Piston

6 = Shaft

7 Pinion

& Gear rack
9 Magnetic ring

A rack-and-pinion type rotary pneumatic actuator converts compressed air energy into rotational
motion using a rack-and-pinion mechanism. Its construction includes a rigid housing that encloses a
piston fitted with a linear rack, which meshes with a pinion mounted on the output shaft. End covers
seal the chamber and supports the shaft, while airports allow controlled supply and exhaust of
compressed air. Seals and bearings ensure smooth movement and prevent leakage.

Operation of the actuator is straightforward, when compressed air is supplied to one side of the piston,
it moves linearly, driving the rack and causing the pinion and output shaft to rotate. Reversing the air
supply moves the piston in the opposite direction, rotating the shaft accordingly. The rotation angle is
typically limited, often between 90° and 180°, making it suitable for valve actuation and industrial
automation. This design provides fast, reliable, and controllable rotational motion in pneumatic
systems.

c) Discussion about the components of a controllable load unit used in closed loop continuous

hydraulic system. - 05 M
The load unit consists of a working cylinder with position transducer and a load cylinder for the
generation of a counter force. By using this assembly and more control technology components,
general functions and properties of closed-loop and open-loop positioning systems can be understood.
The assembly specifically designed to perform control technology exercises in the laboratory includes
the following components and accessories:

e Hydraulic cylinder in mill type design for position control (working cylinder).

e Load cylinder with damping buffer (counter force).

e Wire rope sensor for position feedback (with measuring rope).

e Mounting rail for proximity switch.

e Transparent plastic cover with scale for position feedback.

e Hydraulic connections via self-sealing coupling plugs.

e Component plate of the Rexroth component system to mount the assembly into the mounting

grid of the workstation.

FRR AOR AIO 7 0) AC ACH Ak a
--- page 11 ---
d) Classification of amplifiers used in a proportional hydraulic system. - 03 M
e Plug in amplifier
e Modular amplifier
e Euro card amplifier
e On board electronics (OBE) amplifier
Benefits of the modular amplifier. - 02 M
e Din Rail mountable
e No card holder required
e Internal Ramp Generator
e Comes with an Enable option

FAR 7] RR A RR
````
