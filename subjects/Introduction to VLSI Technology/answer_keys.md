# Introduction to VLSI Technology: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 9a7ce7b16518

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_EXTC_7006/Introduction to VLSI Technology/ANS_Introduction to VLSI Technology(702EX0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (28 pages), mean OCR confidence 77.8
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to VLSI Technology
Date: 08 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 28 pages.
2. Section I. is compulsory
3. Attempt any 4 questions of Section II.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   (Section I)Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Explain the concepts of regularity and hierarchy.   [04]
2 marks each
Hierarchy in VLSI:
Definition: The process of dividing a complex system into
smaller, more manageable sub-modules recursively (a "divide
and conquer" approach).
Function: It breaks down a massive design into levels—such as
System Chip Macro Blocks Cells Transistors.
Purpose: It simplifies the design process, allowing teams to
handle smaller components without worrying about the entire
chip at once.
Example: A 64-bit adder is broken down into four 16-bit adders,
which are further divided into smaller 4-bit adders.
Regularity in VLSI:
Definition: The practice of maximizing the use of similar or
identical structural blocks (regular structures) throughout a
design.
********** 1 **********
--- page 2 ---
Function: It relies on creating a "library" of standard cells, such
as RAM/ROM arrays, registers, or multipliers, that can be
reused.
Purpose:
Reduced Verification: Only a few unique modules need to be
designed and verified rather than the entire chip, saving
significant time and effort.
Optimized Performance: Using identical structures allows for
improved layout efficiency and predictable timing.
Simplified Design: Simplifies the design of complex systems
into a "plug-and-play" model.
Example: A memory array (RAM) is a highly regular structure,
where one bit cell is designed and then replicated millions of
times.
CO-2, SO-1, BL-2   b.   Sketch and discuss C-V characteristics of N-channel E-   [04]
MOSFET.
2 marks for characteristics and 2 marks for explanation of
regions.
• To find the C-V characteristics, respective voltage is
varied and the capacitance is measures as a function of
the voltage.
• Each terminal of the MOSFET has a capacitance with the
other terminals.
• These capacitances are non-linear and voltage dependent.
********** 2 **********
--- page 3 ---
• But the main capacitance is between the Gate and the
Substrate due to the oxide layer.
• Depletion region
• When a small positive bias voltage is applied to the Gate,
holes from the substrate are driven away from the Gate,
resulting in a low carrier density, so the capacitance is
low.
• Inversion region
• At larger gate bias still, near the semiconductor surface
the conduction band edge is brought close to the Fermi
level, populating the surface with electrons in an
inversion layer or n-channel at the interface between the
semiconductor and the oxide. This results in a
capacitance increase, as shown in the right part of figure.
• Accumulation region
• When a negative gate-source voltage (gate –ve, source
+ve) is applied, it creates a p-channel at the surface of
the n region, analogous to the n-channel case, but with
opposite polarities of charges and voltages. The increase
in hole density corresponds to increase in capacitance,
shown in the left part of right figure.
CO-4, SO-1, BL-3   c.   Draw the circuit of a CMOS inverter and state its main   [04]
advantages as compared to other inverters (2 points).
2 marks for diagram and 2 marks for advantages.
Main Advantages
********** 3 **********
--- page 4 ---
Extremely Low Power Consumption: Since one
transistor is always off in a steady state, there is no direct
DC path from VDD to ground. Power is only consumed
during the momentary switching transition, leading to high
power efficiency.
High Noise Immunity & Rail-to-Rail Swing: The circuit
exhibits strong resistance to noise and provides a full
voltage swing (from VDD to ground), making it robust for
digital logic.
High Packing Density: Due to the simple, symmetric
structure, it is highly suitable for VLSI.
CO-3, SO-1, BL-2   d.   Explain clock jitter and clock skew with example and   [04]
waveforms.
2 marks each
********** 4 **********
--- page 5 ---
Os
wir LS LS BS ne

Clock with jitter

—* | — patahold time
~ \ rr requirement
Data - ae

Rs samples data with tt
= hold time
NY
LN

_Daia hold time violation caused by uncertainty
rs

Clock Skew

The Difference in arrival of clock at two consecutive pins of a SSquential element.

ee be
Ken
{ ace

ed ee

WJ
\Towcesr nam
\

~~
A
QO?

Sources of s!
Wire mismatch RY: interconnect length)
Differences i ut capacitance on the clock
«Varying number of Buffers input interconnect length

Clock Skew

Positive skew: if the capture clock comes late than the a ig
N

ee SETUP CHECK
det LIL
LAY (CAPTURE CLOCK

POSITIVE SKEW

FIC DI EH ar
--- page 6 ---
CO-5, SO-1, BL-2   e.   Explain what are EDA tools and their overall importance in   [04]
VLSI design.
EDA tools are essential software tools that streamline the
creation, simulation, verification, and testing of electronic
systems, particularly integrated circuits (ICs). These tools
automate complex tasks, allowing engineers to efficiently
produce advanced electronic components.
In the realm of development, the use of EDA tools for VLSI is
indispensable, managing the intricacies of circuits that may
comprise over a billion components.
For instance, they are used to significantly accelerating the time-
to-market for new products. Furthermore, these tools, enable
designers   to   evaluate   multiple   architectural   variants
concurrently.
Without EDA resources, the process would be considerably
slower and more susceptible to errors.
The significance of Electronic Design Automation (EDA) tools
in VLSI design is paramount. These sophisticated applications
form the backbone of modern   electronic engineering,
streamlining the design, simulation, and testing processes of
integrated circuits and printed circuit boards. By automating
complex tasks, EDA tools enhance productivity and minimize
********** 6 **********
--- page 7 ---
errors, ensuring that designs adhere to rigorous industry
standards.
(Section II) Attempt any 4   [80]
Q1   a.   Explain VLSI design styles in detail.   [10]
CO-1, SO-1, BL-2   Diagram – 2 marks, Detailed explanation of each style -8
marks
********** 7 **********
--- page 8 ---
Q1   b.   Design CMOS circuit and stick diagram for the given Boolean   [10]
CO-3, SO-1, BL-4   expression.
Y = [A (D + E) + BC]’
CMOS circuit – 5 marks, stick diagram – 5 marks
(multiple stick diagram configurations are possible, any
valid one is acceptable)
********** 8 **********
--- page 9 ---
Q2   a.   Draw the circuit diagram and VTC of a real MOS inverter with   [10]
CO-2, SO-1, BL-2   n-type D MOSFET load and explain the working.
********** 9 **********
--- page 10 ---
Circuit diagram — 3 marks, VTC- 3 marks, explanation — 4

marks

E-nMOS inverter with D-nMOS as load

Voo

* The driver device is an

enhancement-type nMOS
transistor, with Vijgriver) > 0 |
* The load is a depletion-type 4

nMOS transistor, with Vyjioaq) < 0 o+

. . Vasioes™ © V_sV.
* Since Gatey\,,4) is connected to ho ot = “08 cever
Sourceticagyr Ves(ioad) = 9 + o—|{_+
* Hence load transistor is always Vin Vos,sever
ON
E-nMOS inverter with D-nMOS as load
Voo
* Circuit configuration T
* M1 (driver): enhancement-type nMOS Load transistor, M2
+ M2 {Jead): depletion-type nMOS (active It ,
load 1
* Connections “I
* Drain of M2 > VDD 4
* Source of M2 > Vout o+
* Gate of M2 > Source (Vout) > VGS2=0V Vasioea™ © V_ sv,
* Drain of M1 > Vout bo on "08 ,aetver

* Source of M1 > GND
* Gate of M1 > Vin + o—|{—_+
* Since a depletion nMOS has negative Vin Vos,siver
threshold voltage, it conducts even

Driver transistor, M1
when Vosttoaa)=0 ,

E-nMOS inverter with D-nMOS as load

Yeo Voo

Case 1: Vin = LOW (0 V) a won
* Transistor states Load transistor, M2

* M1 (enhancement):
+ VGS1=0V > OFF °

* M2 (depletion): ~

* Since VGS2>VT > ON Ve +
©
Vasioas™ 9

* Output behavior
+ No path to ground (M1 OFF) + Vous = Vine iver
+ M2 pulls the output upward

Yo
* Output rises close to VDD + o— f+
Vin™ Vas.atver

* Output voltage

* VOH=VDD ‘
Driver transistor, M1
+ Result
* Output is logic HIGH = =

E-nMOS inverter with D-nMOS as load

Case 2: Vin = HIGH (Vin = VDD) Yoo Yoo

M2 is on
\ Load transistor, M2

‘asjoas™
ho Vou * V8 ver

* Transistor states
* M1:
+ VGS1=VDD > ON
+ M2:
+ Remains ON
* Output behavior Mn
* Current flows from VDD > M2 >
M1 GND

* Io1= loa :
* Vout is pulled to ground (OV) through M1

* Output voltage
* Logic LOW (close to 0 V)

o+

Driver transistor, M1

FRR ICR 7 OI HOH
--- page 11 ---
Q2   b.   Draw the block diagram of ASIC design flow and explain all   [10]
CO-2, SO-1, BL-2   the stages in brief.
Block diagram – 2 marks, Explanation of all stages – 8
marks
Q3   a.   Implement NAND, NOR and EX-NOR gates using CMOS   [10]
CO-4, SO-1, BL-3   logic. Also draw their stick diagram.
CMOS circuits – 2+2+3 marks, stick diagrams – 1 mark
each
********** 11 **********
--- page 12 ---
2 INPUT — CMOS NAND GATE

| 4 Wh
_ooF
a 4

NOR gate in CMOS
--- page 13 ---
Q3   b.   Develop CMOS circuit of clocked SR flip flop.   [10]
CO-3, SO-1, BL-4   Gate level circuit diagram – 3 marks, equations – 1 mark,
CMOS circuit diagram – 6 marks
(Any other valid gate level circuit and its CMOS circuit is
also acceptable)
********** 13 **********
--- page 14 ---
Q4   a.   Develop the truth table of the given Boolean expression and   [10]
CO-3, SO-1, BL-4   implement the circuit using transmission gates.
Y = A’B’C’ + A’B’C + A’BC + AB’C’
Truth table – 4 marks, circuit – 6 marks
Q4   b.   List any four popular schematic capture tools. Discuss their key   [10]
CO-5, SO-1, BL-2   features and importance.
List- 2 marks, features – 4 marks, importance – 4 marks
Schematic capture tools in VLSI design are specialized
software applications used to create a visual representation of
electronic circuits, connecting components to form the logical
********** 14 **********
--- page 15 ---
foundation of a chip before layout. In modern VLSI design,
these tools serve as the frontend operation, allowing designers
to move from a conceptual circuit diagram to a tangible netlist
that can be simulated and subsequently converted into a
physical GDSII layout.
Popular Schematic Capture Tools in VLSI
The industry is dominated by large EDA vendors, with
emerging open-source alternatives gaining traction for
educational and startup use.
Cadence Virtuoso Schematic Editor: The industry standard for
custom IC, analog, and mixed-signal design.
Synopsys Custom Compiler: A modern environment focusing
on schematic-driven layout and automation for advanced
nodes.
Siemens EDA (Mentor Graphics) Tanner S-Edit: Highly
popular in academic and medium-complexity analog design,
featuring tight integration with T-Spice.
Silvaco Gateway: A robust schematic-driven design tool for
analog/mixed-signal ASICs.
Open-Source Alternatives (XCircuit, KiCad, Electric): Used
frequently for research, hobbyist projects, and educational
purposes to learn the basic VLSI flow.
Key Features of VLSI Schematic Capture Tools
Hierarchical Design Management: Allows breaking complex
designs into manageable blocks, sub-circuits, and hierarchies.
Schematic-Driven Layout (SDL): Enables automatic creation of
the physical layout directly from the schematic connectivity.
Built-in Electrical Rules Check (ERC): Identifies potential
errors, such as floating inputs, shorted outputs, or unconnected
pins, before simulation.
SPICE Integration: Allows immediate circuit simulation for
functional and timing verification, often with embedded
simulators like Spectre (Cadence) or T-Spice (Tanner).
********** 15 **********
--- page 16 ---
Advanced Library Management: Provides extensive libraries of
standard cells, transistors, and components, with support for
custom symbol creation.
Netlist Generation: Produces a text-based netlist (e.g., SPICE,
Verilog, CDL) that connects the schematic to layout and
verification tools.
Importance of Schematic Capture in VLSI Flow
Schematic capture is critical because it represents the "Design
Intent."
Foundation for Verification: The schematic is used to simulate
the circuit's behavior under different input conditions to verify
functionality before fabrication.
Layout-vs-Schematic (LVS) Verification: The final layout is
compared against the schematic netlist to ensure that the
physical implementation matches the intended design, a
necessary step for tape-out.
Error Reduction: By using ERC and simulation tools, errors are
identified early, reducing the need for costly redesigns
(Engineering Change Orders).
Documentation and Design Reuse: Schematic diagrams serve
as the primary documentation of the design and allow for the
reuse of hierarchical blocks in future projects.
In summary, for high-end custom IC design, Cadence Virtuoso
is dominant, while Tanner S-Edit is heavily used in analog
design environments. For open-source, the XCircuit/Magic
combination is standard.
Q5   a.   Analyze the following circuit to find out if there is any setup or   [10]
CO-3, SO-1, BL-4   hold violation.
Hold analysis – 5 marks, setup analysis – 5 marks
********** 16 **********
--- page 17 ---
tin 6 ns
FF1 tax 9 1S FF2

tin 1 ms tin _1_ns
DQ Pim 2s tmm2ns | P Q
tmin Ln Lf tene-gmin 9 DS
nin

tetk-qmax 11 ns

tax |2 ns
tin 2 ns tin 2 nS thota 2 ns
CLK hold
tmax 3 NS | tmax 3 ns teetup 4 ns
tin 5 ms
tax 9 0S
Solution:
Hold Analysis:

When a hold check is performed, we have to consider two things-
¢ Minimum Delay along the data path.

e Maximum Delay along the clock path.

Data path is: CLK->FF1/CLK ->FF1/Q ->Inverter ->FF2/D

Delay in Data path
= min(wire delay to the clock input of FF1) + min(Clk-to-Q delay of FF1)

+min(cell delay of inverter) + min(2 wire delay- "Qof FF1-to-inverter" and

“inverter-to-D of FF2")
=Td = 1+9+6+(1+1)=18ns

Clock path is: CLK-> buffer -> FF2/CLK

Clock path Delay
= max(wire delay from CLK to Buffer input) + max(cell delay of Buffer)

+ max(wire delay from Buffer output to FF2/CLK pin) + (hold time of FF2)
=Telk = 3+9+3+2 = 17 ns

Hold Slack = Td - Tclk = 18ns -17ns = 1ns
Since Hold Slack is positive-> No hold Violation.

Setup Analysis:
When a setup check is performed, we have to consider two things-

e Maximum Delay along the data path.
¢ Minimum Delay along the clock path.

Data path is: CLK->FF1/CLK ->FF1/Q ->Inverter ->FF2/D

Delay in Data path
= max(wire delay to the clock input of FF1) + max(Clk-to-Q delay of FF1)

+max(cell delay of inverter) + max(2 wire delay- "Qof FF1-to-inverter"

and "inverter-to-D of FF2")
=Td = 2+114+9+(2+2) = 26ns

FRR ICR] AC OH
--- page 18 ---
Q5   b.   Draw the switching characteristics and discuss interconnect   [10]
CO-2, SO-1, BL-2   effects of MOS inverter. Define propagation delay times with
waveforms.
Switching characteristics – 4 marks, interconnect effects – 3
marks, delay time definition – 3 marks
********** 18 **********
--- page 19 ---
The parasitic capacitance
associated with MOSFET

— Cyy, Cg, gate overlap with diffusion

— Cyp, Cy, voltage dependant junction
capacitance

— C,, the thin-oxide capacitance over
the gate area

— C,,, the limped interconnect
Capacitance

— Load capacitance C,,,.4=
+ Copa + Cub, +Ci.+C
C.p,, and C,,, have no effect on the
transient behavior of the circuit,
since Vcp=0
+ The delay times calculated using
Cioag May slightly overestimate the
actual inverter delay
— Charging, discharging

C...+C

gdin * \“gd.p

Delay-time definitions

Yq

Vou ~—
Vso Vso = Vor +1/ 2(Vox —Vor) =1/ 2(Vox+Vor)

Vou an Text = ti—to

tie =t3—te

— ae TPHL + TPLH
Vou P=

Viow =Vor+0.1- Vou—Vor)
ve ‘Voor =Vor +0.9-(Vor—Vor)

Ton = tts

Trice = tD—te

Cutput voltage rise and fall times.

FRR ICR 7 QI OR
--- page 20 ---
Calculation of delay time

+ The simplest approach for calculating the
propagation delay times tpy, and tp,

— Estimating the average capacitance current during
charge down and charge up


TPHL =
Tavg, HL Tavg, HL
TPLH = =
Tavg, Le Tove, LH

1

Tove, HL = plicn = Von, Vou = Vor) +ic (Vin = Vor, Vour = V 50%)
1

Tovg, LH = gic (Vin = Vor, Vou = V 50%) +ic Vin = Vor, Vou = Vor)|

Estimation of interconnect parasitics

+ The load
- Classical approach
=>capacitive and lumped
+ Internal parasitic capacitance
of the transistor

+ Interconnect (line)
capacitances

+ Input capacitances of the fan-
out gates
+ Now, the interconnect line
itself
— Three dimensional structure in
metal and/or polysilicon
+ Non-negligible resistance
+ The (length/width) ratio of the
wire > distributed > making
the interconnect a true
transmission line
+ An interconnect is rarely
isolated from other influence

An inverter driving three other inverters over
interconnection lines.

Q6 a. Explain briefly how CAD technology is utilized in VLSI [05]
CO-1, SO-1, BL-2 design.

CAD technology divides into three categories:
= Synthesis Tools (Synopsys®)

= Layout Tools (Cadence®)

= Simulation and Verification Tools

FRI ICR DO) A RH
--- page 21 ---
Synthesis Tools

a High-Level Synthesis tools automate the design
phase in the top level of the design hierarchy:
= Based on Hardware-Description Languages (HDL)
> VHDL, Verilog, etc.
« Determining the types and quantities of modules to
be included in the design using accurate estimate of
lower level design features (area and delay).

a Logic Synthesis and optimization tools can then
be used to customize the design to particular
needs, such as area minimization, low power,
etc.

Layout Tools

a Circuit Optimization tools deal with the d
in the transistor schematic levels:
» Transistor sizing for delay minimization
* Reliability issues: process variations, noise.

a tools concern with the physical level of
the design, i.e., how circuits are actually built on
the IC:

= Standard Layout CAD tools are Floorplanning,
Place-and-route, and Module generation

* Sophisticated Layout CAD tools are goal driven and
include some degree of optimization functions

a Time spent on debugging and correcting a
design has been increasing exponentially as
each generation passed.

= Higher penalty is paid if a design flaw is detected
later in the design process.

= Simulation and verification are the most mature area
in VLSI CAD

a Goal of all simulation tools is to determine if the
design meets the required specifications at a
particular design stage.

FI ICR D7 FAC HOH
--- page 22 ---
Q6   b.   Explain the effect of different values of VDS on the channel   [05]
CO-2, SO-1, BL-2   formation and ID in E-MOSFET.
********** 22 **********
--- page 23 ---
Vos

(b) Larger Vpg value

¢ The relative electron density is reduced at the
Drain end of the channel.

¢ Non-uniform channel width

* Depletion region widens near the Drain end
of the channel as n-type D is more positive
w.r.t p-type SS.

* Hence, Ip does not increase in proportion to
Vps at larger values of Vps.

Ip

Vv
ps
Vpsisat)

(C) Vos = Vpsysaty

¢ The induced electron density at the drain
terminal is zero as the effective voltage of the
channel at the drain terminal is just equal to
T

¢ Channel width is zero at the Drain end

* Depletion region widens even more near the
Drain end of the channel as n-type D is even
more positive w.r.t p-type SS.

* Hence, Ip stops increasing at this value of Vps ,
known as Vos (saturation).

Ip

'
' Saturation
{region

Vos

Vpsisat)

(4) Vos > Vosisat)

FIR ICR 2 I OH
--- page 24 ---
Q6   c.   Sketch and label the steps of CMOS n-Well fabrication   [05]
CO-4, SO-1, BL-2   process. (no explanation needed).
Each step – 0.5 marks
n-well Process :
The process steps involved in the n-well process are shown in
Figure below.
The process starts with a p-substrate.
Step 1 : A thin layer of SiO2 is deposited which will serve as a
the pad oxide.
Step 2 : Deposition of a thicker sacrificial silicon nitride layer
by chemical vapour deposition (CVD).
Step 3 : A plasma etching process using the complementary of
the active area mask to create trenches used for insulating the
devices.
Step 4 : The trenches are filled with SiO2 which is called as the
field oxide.
Step 5 : To provide flat surface chemical mechanical
planerization is performed and also sacrificial nitride is
removed.
Step 6 : The n-well mask is used to expose only the n-well
areas, after this implant and annealing sequence is applied to
adjust the well doping. This is followed by second implant step
to adjust the threshold voltage of the PMOS transistor.
Step 7 : Implant step is performed to adjust the threshold
voltage of NMOS transistor.
********** 24 **********
--- page 25 ---
Step 8 : A thin layer of gate oxide and polysilicon is chemically
deposited and patterned with the help of polysilicon mask.
Step 9 : Ion implantation to dope the source and drain regions
of the PMOS (p+) and NMOS (n+) transistors, this will also
form n + polysilicon gate and p+ polysilicon gate for NMOS
and PMOS transistors respectively. Hence this process is called
as self aligned process.
Step 10 : Then the oxide or nitride spacers are formed by
chemical vapour deposition.
Step 11 : In this step contact or via holes are etched, metal is
deposited and patterned. After the deposition of last metal layer
final passivation or overglass is deposited for protection.
********** 25 **********
--- page 26 ---
Q6   d.   Write the RTL Verilog code for a half adder and develop a   [05]
CO-5, SO-1, BL-3   corresponding test bench to verify its functionality.
********** 26 **********
--- page 27 ---
2 marks for code, 3 marks for test bench code
Code for half adder:
Code for test bench ($display is optional, marks to be given
even if $display is not there):
********** 27 **********
--- page 28 ---
“timescale i1ns/ips
module tb_half_adder;

reg a;

reg b;

wire sum;
wire carry;

// Instantiate the Half Adder
half_adder uut (

-a(a),

-b(b),

-sum(sum),

-carry(carry)

)3

initial begin
$display("A B | SUM CARRY");
$display("--------------

// Test all input combinations
a = @; b = @; #10;
$display("%b %b | %b %b", a, b, sum, carry);

a= 0; b=1; #10;
$display("%b %b | %b %b", a, b, sum, carry);

a= 1; b = 0; #10;
$display("%b %b | %b %b", a, b, sum, carry);

a=1; b= 1; #10;
$display("“%b %b | %b %b", a, b, sum, carry);

$finish;
end

FI ICR 2 QA HH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper fb95c6e3f279

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_EXTC_7006/Introduction to VLSI Technology/ANS_Introduction to VLSI Technology(702EX0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: mixed (25 pages), mean OCR confidence 80.5
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to VLSI Technology
Date: 04 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 25 pages.
2. Section I. is compulsory
3. Attempt any 4 questions of Section II.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   (Section I)Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Explain the concepts of modularity and locality.   [04]
2 marks each
Modularity enables large, complex chips to be broken down into
smaller, manageable functional units or blocks.
Definition: Each block has a well-defined function and specific
interfaces (inputs/outputs).
Independent Design: Modules can be designed, verified, and
optimized independently by different teams or tools.
Reusability: Modular components can be stored in a library and
reused in future designs, reducing time-to-market.
Example: In a processor design, modules like the Arithmetic
Logic Unit (ALU), Register File, and Cache Controller are
developed separately, then combined.
Locality dictates that electrical connections should be made
between physically neighboring components or blocks, limiting
the need for long global wires.
Interconnect Optimization: By placing communicating modules
close to each other, the design reduces wire length, which
********** 1 **********
--- page 2 ---
minimizes signal delay, power consumption, and RC time
constants.
Reduced Routing Congestion: It lowers the complexity of wiring
(routing) across the chip, aiding CAD tools in physical layout.
Example: Placing frequently communicating units—like
memory and   its controller—side-by-side on the silicon
floorplan.
CO-2, SO-1, BL-2   b.   Discuss the purpose of RTL gate synthesis in ASIC design flow.   [04]
2 marks for any one diagram and 2 marks for explanation.
• Logic synthesis is the process of converting the RTL code
into a gate-level representation using a logical synthesis
tool .
•   It produces a netlist that gives the interconnection of
logic gates.
CO-4, SO-1, BL-3   c.   Define the following transient characteristics of the CMOS   [04]
inverter: rise time, fall time, propagation delay, dynamic power.
1 mark each
********** 2 **********
--- page 3 ---
CO-3, SO-1, BL-2   d.   Explain setup time and hold time with example and waveforms.   [04]
2 marks each for setup time and hold time.
********** 3 **********
--- page 4 ---
CO-5, SO-1, BL-2   e.   Explain what are EDA tools and their overall importance in   [04]
VLSI design.
EDA tools are essential software tools that streamline the
creation, simulation, verification, and testing of electronic
systems, particularly integrated circuits (ICs). These tools
automate complex tasks, allowing engineers to efficiently
produce advanced electronic components.
In the realm of development, the use of EDA tools for VLSI is
indispensable, managing the intricacies of circuits that may
comprise over a billion components.
For instance, they are used to significantly accelerating the time-
to-market for new products. Furthermore, these tools, enable
designers   to   evaluate   multiple   architectural   variants
concurrently.
Without EDA resources, the process would be considerably
slower and more susceptible to errors.
The significance of Electronic Design Automation (EDA) tools
in VLSI design is paramount. These sophisticated applications
form the backbone of modern   electronic engineering,
streamlining the design, simulation, and testing processes of
integrated circuits and printed circuit boards. By automating
complex tasks, EDA tools enhance productivity and minimize
errors, ensuring that designs adhere to rigorous industry
standards.
********** 4 **********
--- page 5 ---
(Section II) Attempt any 4   [80]
Q1   a.   Explain how CAD technology is used in VLSI design for   [10]
CO-1, SO-1, BL-2   synthesis, layout and simulation.
3+3+4 marks for each tool
********** 5 **********
--- page 6 ---
Synthesis Tools

a High-Level Synthesis tools automate the design
phase in the top level of the design hierarchy:
= Based on Hardware-Description Languages (HDL)
> VHDL, Verilog, etc.
« Determining the types and quantities of modules to
be included in the design using accurate estimate of
lower level design features (area and delay).

a Logic Synthesis and optimization tools can then
be used to customize the design to particular
needs, such as area minimization, low power,
etc.

Layout Tools

a Circuit Optimization tools deal with the d
in the transistor schematic levels:
» Transistor sizing for delay minimization
* Reliability issues: process variations, noise.

a tools concern with the physical level of
the design, i.e., how circuits are actually built on
the IC:

= Standard Layout CAD tools are Floorplanning,
Place-and-route, and Module generation

* Sophisticated Layout CAD tools are goal driven and
include some degree of optimization functions

a Time spent on debugging and correcting a
design has been increasing exponentially as
each generation passed.

= Higher penalty is paid if a design flaw is detected
later in the design process.

= Simulation and verification are the most mature area
in VLSI CAD

a Goal of all simulation tools is to determine if the
design meets the required specifications at a
particular design stage.

FIC 6 I HF
--- page 7 ---
Q1   b.   Design CMOS circuit and stick diagram for the given Boolean   [10]
CO-3, SO-1, BL-4   expression.
Y = [(AB + C). (D + E)]’
Circuit-5 marks, stick diagram-5 marks
(multiple stick diagram configurations are possible, any
valid one is acceptable)
********** 7 **********
--- page 8 ---
VDD

pDIFF

nDIFF

GND

Q2 a. Describe the working of a resistive load MOS inverter with [10]
CO-2, SO-1, BL-2 circuit diagram.

FOCI 9 FCI IC Ir
--- page 9 ---
Q2   b.   Describe the structure of N-channel E-MOSFET with a   [10]
CO-2, SO-1, BL-2   diagram, and explain its working with the help of drain
characteristics.
Construction diagram -3 marks, description – 2 marks,
characteristics – 3 marks, working explanation – 2 marks
********** 9 **********
--- page 10 ---
N channel E-MOSFET working

* Voltage applied between Gate and Source (Vs) Electrons attracted to positive gate _,Region depleted of
(induced n - channel) - type carriers (holes)
* Positive voltage to Gate
* Ground (0 V) to Source
+ Substrate (p-type) connected to Source (0 V)
* tve.voltage at G causes polarization of charges in SiO,
layer.

* Electrons in p-type SS (minority carriers) attracted to the Ig=0A —ae ees
+ve Gate Go— + »
* A pathway of electrons is formed near Gate, between D : —+
ands. Vos :
* This pathway is called induced channel or inversion layer.
* Depletion region formed around Drain, Source and n- a
channel.

by positive gate

Channel formation in the n-channel
‘enhancement type MOSFET

¢ Now we expect current I, to flow from D to S through
n-channel.

¢ But no current flows, because initially, for low values
of Vgs, n-channel is weak and cannot conduct current.

* To make n-channel strong, more electrons need to be
attracted to the channel.

¢ If we increase magnitude of V,, in the positive
direction, the concentration of electrons near the SiO,
surface increases.

¢ Ata particular value of V,, there is a measurable
current flow between drain and source.

* This value of V,, is called threshold voltage denoted
by V;.

* The conductivity of the channel is enhanced by
increasing the V,, and thus pulling more electrons
into the channel.

¢ For any voltage below the threshold value, there is no
channel.

* Since the channel does not exist with V,, = 0 V and
"enhanced" by the application of a positive gate to
source voltage, this type of MOSFET is called an
enhancement type MOSFET.

FRR ICR 7 OI HOH
--- page 11 ---
Q3   a.   Implement AND, OR and EX-OR gates using CMOS logic.   [10]
CO-4, SO-1, BL-3   Also draw their stick diagram.
CMOS circuits – 2+2+3 marks, stick diagrams – 1 mark
each
AND GATE:
********** 11 **********
--- page 12 ---
\v substrate connection

Vout

demarcation line

p well connection

NOR GATE:

FRR ICR] DA KH
--- page 13 ---
EX-OR GATE:

DR ROR RK 13 FRR RR
--- page 14 ---
Q3 b. Develop CMOS circuit of clocked D flip flop. [10]
CO-3, SO-1, BL-4

FRR IC 7 I OH
--- page 15 ---
Gate level circuit diagram – 3 marks, equations – 1 mark,
CMOS circuit diagram – 6 marks
(Any other valid gate level circuit and its CMOS circuit is
also acceptable)
Consider EN=CK.
Q4   a.   Develop the truth table of the given Boolean expression and   [10]
CO-3, SO-1, BL-4   implement the circuit using transmission gates.
Y = A’BC’ + AB’C’ + AB’C + ABC
Truth table – 4 marks, circuit – 6 marks
Q4   b.   Discuss the key features and importance of simulation and   [10]
CO-5, SO-1, BL-2   analysis EDA tools of Synopsis, Cadence and Siemens.
3+4+3 marks
Synopsys, Cadence, and Siemens EDA (formerly Mentor
Graphics) dominate the Electronic Design Automation (EDA)
market, providing the critical software tools required to design,
simulate, and manufacture modern, increasingly complex
integrated circuits (ICs), 3D-ICs, and printed circuit boards
(PCBs). Together, these companies control approximately 75%
of the global EDA market as of 2024, enabling semiconductor
companies to achieve first-pass silicon success.
********** 15 **********
--- page 16 ---
1. Synopsys Simulation and Analysis Tools
Synopsys is considered a leader in digital design, synthesis, and
verification, often serving as the "full-stack" provider for
complex digital ICs.
Key Features & Tools:
VCS (Functional Verification): High-performance simulation
for Verilog, SystemVerilog, and VHDL, designed to find bugs
faster.
Design Compiler & Fusion Compiler: Industry standard for
digital logic synthesis, translating HDL code into gates, with
Fusion Technology unifying synthesis, place-and-route, and
signoff.
VC Formal & PrimeTime: Formal verification (proving design
correctness) and Static Timing Analysis (STA) tools to ensure
timing constraints are met.
Synopsys.ai: A suite of AI-driven tools (VSO.ai, ASO.ai,
DSO.ai) that automate verification, analog design space
exploration, and physical implementation, enabling 10x
productivity boosts.
Importance: Synopsys tools are crucial for managing the
immense complexity of modern SoCs, specifically in digital
design synthesis and ensuring design functionality before
tapeout.
2. Cadence Simulation and Analysis Tools
Cadence Design Systems is widely recognized for its "gold
standard" Virtuoso suite for custom/analog design and its
strong system-level analysis tools.
Key Features & Tools:
Spectre Simulation Platform: SPICE-level simulation for
analog, RF, and mixed-signal circuits, providing high accuracy
for transistor-level design.
Virtuoso ADE Suite: Comprehensive environment for custom
analog/mixed-signal layout, schematic entry, and verification.
Xcelium Logic Simulator: Fast, parallel simulation for complex
digital and mixed-signal designs.
********** 16 **********
--- page 17 ---
Allegro X & Sigrity X Platform: Industry-leading PCB design,
layout, and signal/power integrity (SI/PI) analysis tools.
Cadence.ai: Tools designed to automate PCB design and chip
design flows, incorporating generative AI for routing.
Importance: Cadence tools excel in analog and mixed-signal
design, custom IC verification, and PCB layout, offering
comprehensive solutions for both silicon and system-level
connectivity.
3. Siemens EDA Simulation and Analysis Tools
Siemens EDA (formerly Mentor Graphics) offers a robust,
specialized portfolio that excels in physical verification,
testability, and system-level modeling, complementing the
wider Siemens industrial software ecosystem.
Key Features & Tools:
Calibre Platform: The industry-standard "gold" tool for
physical verification (Design Rule Checking-DRC and Layout
vs. Schematic-LVS) and Design for Manufacturing (DFM).
Questa Verification Platform: Automates functional
verification and debugging of complex SoCs and FPGAs.
Veloce CS: A hardware emulation and prototyping platform for
fast system validation, bridging software and hardware.
Tessent: Advanced test and Design for Test (DFT) features to
ensure high yield and silicon lifecycle management.
HyperLynx & Solido: HyperLynx handles high-speed PCB
analysis, while Solido provides AI-based variation-aware
design for characterization.
Importance: Siemens tools are critical for signoff physical
verification (Calibre), manufacturing testability, and managing
complex 3D-IC design through advanced multi-physics
simulation.
Q5   a.   Analyze the following circuit and find out the setup and hold   [10]
CO-3, SO-1, BL-4   time at input A for proper functioning of the circuit. Calculate
maximum operating frequency of the circuit. (Neglect wire
delay. Tsu: setup time, Thd: hold time, Tc2q: clock-to-Q
delay).
********** 17 **********
--- page 18 ---
Each step — 2 marks

lns US U6
[a >
U7
6ns
9 ns
DFFs :
Tsu = 3 ns
Thd = 4 ns
Tc2q =5 ns

Solution:
Step1: Find out the maximum Register to register Delay.

Max Register to Register Delay
= (clk-to-Q delay of U2) + (cell delay of U3) + (all wire delay) + (setup time of U1)
=5+8+3=16ns.
Note:
« There are 2 register to register paths
o U2 -> U3 ->U1 (Delay=5+8+3=16ns)
o U1 -> U4 -> U2 ( Delay=5+7+3=15ns)

« We have to pick maximum one.

Step2: Find Out Setup Time:

Asetup time = Setup time of Flipflop + Max (Data path Delay) - min(Clock path Delay)
= (Setup time of Flipflop + A2D max delay) - (Clk path min delay)


=3+(1+8)-2=10ns

Step3: Find Out Hold Time:

Ahold time = Hold time of Flipflop + max(Clock path Delay) - min( Data path delay)
=( Hold time of Flipflop + Clk path max delay) - (A2D max delay)

= Thd + Tpd U8 - (Tpd U7 + Tpd U4+wire delay)

=4+2-(1+7)=-2ns

Step4: Find out Clock to Out Time:

Clock to Out

= Cell delay of U8 + Clk-to-Q delay of FlipFlop+ Cell delay of U5+ Cell delay of U6+ (all wire delay)
= Tpd U8+ U2 Tc2q + U5 Tpd + U6 Tpd

=2+5+9+6=22ns

FR ICR 7] QA HH
--- page 19 ---
Q5   b.   Explain the concept of Network-on-Chip (NoC). State the   [10]
CO-2, SO-1, BL-2   advantages and disadvantages of NoC as compared to bus
architecture (5 points).
Explanation – 5 marks, comparison – 5 marks
What is Network-on-Chip (NoC)?
A Network-on-Chip (NoC) is an advanced communication
architecture used in System-on-Chip (SoC) designs, where
multiple components (like processors, memory blocks, and IP
cores) communicate with each other using a network-like
structure instead of traditional shared buses.
Think of it like a mini internet inside a chip:
Components = nodes (like computers)
Links = wires connecting them
Routers = direct data packets efficiently
Key Features
Packet-based communication (data broken into packets)
Routers and links connect cores
Supports parallel data transfer
Uses topologies like mesh, torus, or ring
********** 19 **********
--- page 20 ---
NoC vs Bus Architecture

1. Advantages of NoC over Bus Architecture

Feature NoC Bus Architecture
Scalability Highly scalable (easy to add cores) Limited scalability
Performance High throughput, parallel communication _ Bottleneck due to shared bus
Latency Lower latency with proper routing Increases with more devices
Bandwidth High bandwidth (multiple paths) Limited (single shared path)
Power Efficiency More efficient for large systems Less efficient as load increases
Modularity Easy to design modular systems Harder to expand or modify

2. Disadvantages of NoC (Compared to Bus)

Aspect NoC Drawback
Design Complexity More complex (routers, protocols, topology design)
Area Overhead Requires more silicon (routers + links)
Power Overhead Routers consume extra power
Latency (Small Systems) Higher than bus for very small systems
Verification Difficulty Harder to test and debug
Q6 a. Explain VLSI design flow in brief with block diagram. [05]

CO-1, SO-1, BL-2
Simplified VLSI Design Flow
ehaviora ‘unctional Circuit
Es — = ic

Functional Vritcation | ‘unctional Verification | iret Verieation Verification

Logic a
Layout
(Gate-Level) Logic Desi: | Physical Design | ical Desizn :
‘epresentation oe sii ——, y is Representatio

} Logie Veritcation | Verification Physical Verification

— End

Synthesis Phase

FRI ICR DO) A RH
--- page 21 ---
Q6   b.   Discuss the significance of Routing in ASIC design flow.   [05]
CO-2, SO-1, BL-2
Q6   c.   Sketch and label the steps of CMOS n-Well fabrication   [05]
CO-4, SO-1, BL-2   process. (no explanation needed).
Each step – 0.5 marks
n-well Process :
The process steps involved in the n-well process are shown in
Figure below.
The process starts with a p-substrate.
Step 1 : A thin layer of SiO2 is deposited which will serve as a
the pad oxide.
Step 2 : Deposition of a thicker sacrificial silicon nitride layer
by chemical vapour deposition (CVD).
Step 3 : A plasma etching process using the complementary of
the active area mask to create trenches used for insulating the
devices.
********** 21 **********
--- page 22 ---
Step 4 : The trenches are filled with SiO2 which is called as the
field oxide.
Step 5 : To provide flat surface chemical mechanical
planerization is performed and also sacrificial nitride is
removed.
Step 6 : The n-well mask is used to expose only the n-well
areas, after this implant and annealing sequence is applied to
adjust the well doping. This is followed by second implant step
to adjust the threshold voltage of the PMOS transistor.
Step 7 : Implant step is performed to adjust the threshold
voltage of NMOS transistor.
Step 8 : A thin layer of gate oxide and polysilicon is chemically
deposited and patterned with the help of polysilicon mask.
Step 9 : Ion implantation to dope the source and drain regions
of the PMOS (p+) and NMOS (n+) transistors, this will also
form n + polysilicon gate and p+ polysilicon gate for NMOS
and PMOS transistors respectively. Hence this process is called
as self aligned process.
Step 10 : Then the oxide or nitride spacers are formed by
chemical vapour deposition.
Step 11 : In this step contact or via holes are etched, metal is
deposited and patterned. After the deposition of last metal layer
final passivation or overglass is deposited for protection.
********** 22 **********
--- page 23 ---
Q6   d.   Write the RTL Verilog code for a full adder and develop a   [05]
CO-5, SO-1, BL-3   corresponding test bench to verify its functionality.
********** 23 **********
--- page 24 ---
2 marks for code, 3 marks for test bench code
Code for full adder:
Code for test bench ($display is optional, marks to be given
even if $display is not there):
********** 24 **********
--- page 25 ---
initial begin
$display("A B Cin | SUM Cout");
$display("-------------------

// Test all input combinations
a=0; b=; cin=0; #10;
$display("%b %b %b | %b %b", a, b, cin, sum, cout);

a=0; b=; cin=1; #10;
$display("%b %b %b | %b %b", a, b, cin, sum, cout);

a=0; b=1; cin=0; #10;
$display("%b %b %b | %b %b", a, b, cin, sum, cout);

a=0; b=1; cin=1; #10;
$display("%b %b %b | %b %b", a, b, cin, sum, cout);

a=1; b=0; cin=0; #10;
$display("%b %b %b | %b %b", a, b, cin, sum, cout);

a=1; b=; cin=1; #10;
$display("%b %b %b | %b %b", a, b, cin, sum, cout);

a=1; b=1; cin=0; #10;
$display("%b %b %b | %b %b", a, b, cin, sum, cout);

a=1; b=1; cin=1; #10;
$display("%b %b %b | %b %b", a, b, cin, sum, cout);

$finish;
end

endmodule

FI ICR AC KH
````
