# Digital Logic Design: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper f41d3487907a

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/BTech_IT_7001/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: mixed (14 pages), mean OCR confidence 73.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (IT)/MBA Tech (IT)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1; SO-1;   a.   Solve the following given conversions:   [05]
BL-3
i)   (675.625)10 = (? )16
ii)   (3287.5100098)10 = (? )8
iii)   (1001101)2 = ( )G
Solution:
i) (675.625)16 = (? )10 -2Marks
ii) (3287.5100098)10 = (? )8 -2Marks
iii) (1001101)2 = ( )G -1Mark
i)   (2A3.A)16
ii)   (6327.4051)8
iii)   (1101011)G
CO-2; SO-1;   b.   What are universal gates? Construct AND gate and OR gate using NAND   [05]
BL-1, 3
gates.
Solution:
Explanation-(1Marks)
A universal gate is a gate, which can implement any Boolean function without need to use any
other gate type. The NAND and NOR gates are universal gates.
In practice, this is advantageous since NAND and NOR gates are economical and easier to
fabricate and are the basic gates used in all IC digital logic families.
AND and OR diagram using NAND gates with expression at output of each
gate(2+2marks)
********** 1 **********
--- page 2 ---
AND gate using NAND   OR gate using NAND
CO-3; SO-1;   c.   Label and draw the circuit diagram of 2-to-4 line decoder and write its truth   [05]
BL-1
table and equation.
Solution:
Circuit diagram of 2-to-4-line decoder (2 M), Truth table(2M) and
Equations (1M)
CO-4; SO-1;   d.   Compare synchronous and asynchronous counter.   [05]
BL-2
Solution: (any five valid point- 5 Marks)
Points   Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous Counters,
Trigge   Counters, all the constituent   there is triggering of different flip-
r   flip-flops are triggered with   flops with different clock.
same clock simultaneously.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster as   asynchronous counter is
ion
compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are more
error-prone; they hardly produce   error-prone and produce decoding
Error
any decoding errors because   errors in the system.
Prone
each flip-flop is individually
clocked.
All the flip-flops in a   In an asynchronous counter, the
synchronous counter coordinate   output of one flip-flop acts as the
Compl   with the clock, hence its design   input of the next flip-flop, hence its
exity   and implementation is complex   design and implementation is quite
as compared to that of an   simple.
asynchronous counter.
A Synchronous counter can be   An Asynchronous counter can
operated in any desired count   operate only in a fixed count
Seque
sequence, as it could get   sequence, i.e., UP and DOWN.
nce
manipulated by changing the
clock sequence.
********** 2 **********
--- page 3 ---
There is no propagation delay   In case of asynchronous counters,
Delay   observed in case of Synchronous   there is a subsequent propagation
Counters.   delay from one flip-flop to another.
Q2   a.   Develop 4-bit Binary to Gray code converter.   [10]
CO-1; SO-1;   Solution: Truth table of 4-bit Binary to Gray code converter (02Marks)
BL-3
four k-map simplifications (04 Marks), with correct expressions (02
Marks),
logic diagram implementation (02 Marks)
Binary input   |   Gray code output   |
B3   B2   B1   B0   G3   G2   G1   G0
0   0   0   0   0   0   0   0
0   0   0   1   0   0   0   1
0   0   1   0   0   0   1   1
0   0   1   1   0   0   1   0
0   1   0   0   0   1   1   0
0   1   0   1   0   1   1   1
0   1   1   0   0   1   0   1
0   1   1   1   0   1   0   0
1   0   0   0   1   1   0   0
1   0   0   1   1   1   0   1
1   0   1   0   1   1   1   1
1   0   1   1   1   1   1   0
1   1   0   0   1   0   1   0
1   1   0   1   1   0   1   1
1   1   1   0   1   0   0   1
1   1   1   1   1   0   0   0
K-Map for G3:
G3 = B3
K-Map for G2:
K-Map for G1:
********** 3 **********
--- page 4 ---
K-Map for G0:
Q2   b.   Solve the following using Boolean algebra and implement using logic gates-   [10]
CO-2; SO-1;
BL-3   i) Y= ABC + A B C + A B C + ABC
ii) Y= A + B + CD̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
Solution:
i)   Simplification with Boolean laws mention at required steps(4Marks) +
Implementation (1 Marks)
ii)   Simplification with Boolean laws mention at required steps(4Marks) +
Implementation (1 Marks)
********** 4 **********
--- page 5 ---
Q3   a.   Demonstrate full adder circuit using logic gates with truth table and K-Map.   [10]
CO-3; SO-1;   Solution:
BL-2
Definition of full adder with block diagram(02Marks)
Truth table (02 Marks) & K-map solving (03 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A
one-bit full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the
operands, and Cin is a bit carried in from the next less significant stage. The full-adder is
usually a component in a cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers.
The circuit produces a two-bit output, output carry and sum typically represented by the
signals Cout and S
A B Cin Sum Carry
0 0 0   0   0
0 0 1   1   0
0 1 0   1   0
0 1 1   0   1
1 0 0   1   0
1 0 1   0   1
1 1 0   0   1
1 1 1   1   1
Q3   b.   Illustrate functioning of clocked “D” flip flop with block diagram, truth table,   [10]
CO-4; SO-1;   logic diagram and K-map.
BL-2
Solution:
Clocked “D” flip flop circuit diagram (4 Marks) and truth table (03 Marks)
+Working (03 Marks)
********** 5 **********
--- page 6 ---
Q4   a.   Solve the following expression using k-map & implement with minimum   [10]
CO-2; SO-1;   number of gates-
BL-3
Y = f(A, B,C,D) = m (1, 3,7,11, 15) + d(0,2,4)
Solution:
********** 6 **********
--- page 7 ---
K-Map entry (02 Marks) and correct Grouping with expression (06
Marks) + circuit implementation (02 Marks)
Q4   b.   Make a use of VHDL to write a code for implementing OR gate.   [10]
CO-5; SO-1;   Solution:
BL-3
5M Design code 5M Test bench code
DESIGN CODE for OR gate:
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;
Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;
entity or_gate is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
y : out STD_LOGIC);
end or_gate;
architecture Behavioral of or_gate is
begin
y <= a or b;
end Behavioral;
TESTBENCH CODE for OR gate:
library IEEE;
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity or_gate_tb is
end;
architecture bench of or_gate_tb is
component or_gate
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
y : out STD_LOGIC);
end component;
signal a: STD_LOGIC := '0';
********** 7 **********
--- page 8 ---
signal b: STD_LOGIC := '0';
signal y: STD_LOGIC;
begin
uut: or_gate port map ( a => a,
b => b,
y => y );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a.   Build the given function using single 8:1 multiplexer.   [10]
CO-3; SO-1;   F(A, B, C, D) = m (0, 3, 4, 5, 8, 9,12,15)
BL-3
Solution:
Design table (05 Marks) and Circuit diagram (05 Marks)
Q5   b.   Illustrate the operation of serial in serial out shift register with logic Diagram   [10]
CO-4; SO-1;   and waveforms.
BL-2
Solution:
Logic Diagram (04 Marks) +Waveforms (03 Marks) +Operation (03
Marks)
********** 8 **********
--- page 9 ---
This shift register is very similar to the SIPO above, except were before the
data was read directly in a parallel form from the outputs QA to QD, this time
the data is allowed to flow straight through the register and out of the other
end. Since there is only one output, the DATA leaves the shift register one bit
at a time in a serial pattern, hence the name Serial-in to Serial-Out Shift
Register or SISO.
The SISO shift register is one of the simplest of the four configurations as it
has only three connections, the serial input (SI) which determines what enters
the left hand flip-flop, the serial output (SO) which is taken from the output of
the right hand flip-flop and the sequencing clock signal (Clk). The logic circuit
diagram below shows a generalized serial-in serial-out shift register.
Well this type of Shift Register also acts as a temporary storage device or it
can act as a time delay device for the data, with the amount of time delay being
controlled by the number of stages in the register, 4, 8, 16 etc or by varying the
application of the clock pulses.
Q6   a.   Explain different modelling styles in VHDL in detail.   [10]
CO-5; BL-2 SO-1;   Solution: Three types 3M, 3M and 4M
********** 9 **********

[Text in pictures on this page, read by OCR]
= FLPLPLELFLEL— LAL

Q, | B | B | B |B | B | Bs By | Bost
2 oe: <5 SONS
Q [ o | 8 | B&B |B | & | B Bat | Bn

Sea, ee, ES

2. eo 2.
nn

Q, 0 0 0 0

> 4

By B,

_J_—
Output bit sequence

Figure2 Output Waveform of n-bit Right-Shift SISO Shift Register
--- page 10 ---
architecture HA_STRUCTURE of HALF_ADDER is
component XOR2
port (X, Y: in BIT; Z: out BIT);
end component;
component AND2
port (L, M: in BIT; N: out BIT);
end component;
begin
X1: XOR2 port map (A, B, SUM);
A1: AND2 port map (A, B, CARRY);
end HA_STRUCTURE;
•   The name of the architecture body is HA_STRUCTURE.
•   The entity declaration for HALF_ADDER specifies the interface ports for this architecture
body.
•   The architecture body is composed of two parts:
•   the declarative part (before the keyword begin) and the statement part (after the
keyword begin).
•   Two component declarations are present in the declarative part of the architecture
body. These declarations specify the interface of components that are used in the
architecture body. The components XOR2 and AND2 may either be predefined
components in a library
•   The declared components are instantiated in the statement part of the architecture body using
component instantiation statements. XI and A1 are the component labels for these component
instantiations. The first component instantiation statement, labeled XI, shows that signals A
and B (the input ports of the HALF_ADDER), are connected to the X and Y input ports of a
XOR2 component, while output port Z of this component is connected to output port SUM of
the HALF_ADDER entity.
architecture HA_CONCURRENT of HALF_ADDER is
begin
SUM <= A xor B after 8 ns;
CARRY <= A and B after 4 ns;
end HA_CONCURRENT;
The dataflow model for the HALF_ADDER is described using two concurrent signal assignment
statements
•   Delay information is included in the signal assignment statements using after clauses.
•   If either signal A or B, which are input port signals of HALF_ADDER entity, has an event, say
at time T, the right-hand-side expressions of both signal assignment statements are evaluated.
•   Signal SUM is scheduled to get the new value after 8 ns while signal CARRY is scheduled to
get the new value after 4 ns.
•   When simulation time advances to (T+4) ns, CARRY will get its new value and when
simulation time advances to (T+8) ns, SUM will get its new value. Thus, both signal
assignment statements execute concurrently.
•   Ordering of these statements in an architecture body is not important.
Behavioral Style Modelling
architecture DEC_SEQUENTIAL of DECODER2x4 is
begin process (A, B, ENABLE)
variable ABAR, BBAR: BIT; begin
ABAR := not A; - statement 1
BBAR := not B; - statement 2
if (ENABLE = '1')
then -statements 3
Z(3) <= not (A and B): - statement 4
********** 10 **********
--- page 11 ---
Z(0) <= not (ABAR and BBAR); ~ statement 5
Z(2) <= not (A and BBAR); - statement 6
Z(1 ) <= not (ABAR and B); - statement 7
else
Z<= "1111"; -statement8
end if;
end process;
end;
 A process statement, too, has
◼   a declarative part (between the keywords process and begin), and
◼   a statement part (between the keywords begin and end process).
The statements appearing within the statement part are sequential statements and are executed
sequentially.
Q6   b.   Design and implement Mod-8 asynchronous counter using JK Flip Flop.   [10]
CO-4; SO-1;   Solution: Diagram 3M,Truth Table 3M,Timing Diagram 4M
BL-1, 3
Q7   a.   With the help of truth table and K-Map develop the logic circuit of Priority   [05]
CO-3; SO-1;   Encoder.
BL-3
********** 11 **********

[Text in pictures on this page, read by OCR]
i 2 3 4 5 6 7 8 :
|
4 Clock i
| pulses Truth Table
0 AMOD-8 Ripple Counter

Input

CLK Outputs

Olpof * ‘ Pulses} A Bic
FFC 0 0 0 0
1 0 0 |

2 0 1 0

3 0 i i

op “g 4 1 0 0
— 5 i 0 |

6 | 1 0

a i i i

O/p of 8 0 0 0

FFA —

Fig. 9.6
--- page 12 ---
Solution: Truth Table 1M, K-Map 2M,Circuit Diagram 1M

PRIORITY ENCODER:

+ As the name indicates, the priority is given to inputs line.

+ Iftwo or more input lines are high at the same time i.e 1 at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priorit

nput TRUTH TABLE:

Y, INPUTS OUTPUTS Vi

D, Ds | D2] Di | Do | Yil Yo
Priority 0 0 0 0 x x oO

D, Encoder
——) ¥; 0 0 0 1 0 0 1
0

D, ——o 1
0 0 0 1 x 0 1
0 il x x 1 0 1
»west Priority Output 1 x x x ul 1 1

H
Diagram of Priority Fig.15

* There are four inputs Dp, D,,D,, D; and two outputs Y, and Y,

* D, has highest priority and Dy is at lowest priority.

* IfD,=1 irrespective of other inputs then output Y,Y)=11.

* D, is at highest priority so other inputs are considered as don’t care

K-map for Y, and Y
D,Dy _D,Dp A “
D,D, \_00___ 01 l= 10) D3DSN 00s 00

00] X 0 0 0 00] X 0 | :1 1:

ot! 1 1 1 1} ao} 0 | o | 0 | oO
of ia | a | | oa fit fa fa | ai
Y=D,+Ds Y,=D,+D,D, ¥ y
Fig. 16
LOGIC DIAGRAM OF PRIORITY ENCODER
Y,=D, +D,
Y, =D, +D,D,
D, Ds D, Dy

y

Fig. 17

FRR ICR] DA KH
--- page 13 ---
Q7   b.   Construct Canonical Product of Sum expression of   [05]
CO-3; SO-1;   Y=(A+B’) (B+C) (A+C’)
BL-3
Solution:
Q7   c.   Explain the Race around condition in JK flip-flop.   [05]
CO-4; SO-1;   Solution:
BL-2
Explanation (04) with diagram (01)
In JK Flip-flop – For J-K flip-flop, if J=K=1, and if clk=1 for a long period of time, then Q output will
toggle as long as CLK is high, which makes the output of the flip-flop unstable or uncertain. This
problem is called race around condition in J-K flip-flop. In JK flip flop as long as clock is high for the
input conditions J&K equals to the output changes or complements its output from 1–>0 and 0–>1.
This is called toggling output or uncontrolled changing or racing condition. Consider above J&K circuit
diagram as long as clock is high and J&K=11 then two upper and lower AND gates are only triggered by
the complementary outputs Q and Q(bar). I.e. in any condition according to the propagation delay one
gate will be enabled and another gate is disabled. If upper gate is disabled, then it sets the output and
in the next lower gate will be enabled which resets the flip flop output
Q7   d.   Solve the following:   [05]
CO-1; SO-1;
Subtract 28 from 15 using 1’s complement method.
BL-3
Solution:
One’s Compliment 2M
Addition 1M
Answer 2M
28-11100
15-01111
1’s Compliment 28- 00011
Add: 01111+00011=10010
********** 13 **********
--- page 14 ---
No Carry answer negative and one’s compliment 01101

FRR IC 7 I OH
````

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 5b99e4087dcd

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MBATech_IT_7041/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: mixed (14 pages), mean OCR confidence 73.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (IT)/MBA Tech (IT)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1; SO-1;   a.   Solve the following given conversions:   [05]
BL-3
i)   (675.625)10 = (? )16
ii)   (3287.5100098)10 = (? )8
iii)   (1001101)2 = ( )G
Solution:
i) (675.625)16 = (? )10 -2Marks
ii) (3287.5100098)10 = (? )8 -2Marks
iii) (1001101)2 = ( )G -1Mark
i)   (2A3.A)16
ii)   (6327.4051)8
iii)   (1101011)G
CO-2; SO-1;   b.   What are universal gates? Construct AND gate and OR gate using NAND   [05]
BL-1, 3
gates.
Solution:
Explanation-(1Marks)
A universal gate is a gate, which can implement any Boolean function without need to use any
other gate type. The NAND and NOR gates are universal gates.
In practice, this is advantageous since NAND and NOR gates are economical and easier to
fabricate and are the basic gates used in all IC digital logic families.
AND and OR diagram using NAND gates with expression at output of each
gate(2+2marks)
********** 1 **********
--- page 2 ---
AND gate using NAND   OR gate using NAND
CO-3; SO-1;   c.   Label and draw the circuit diagram of 2-to-4 line decoder and write its truth   [05]
BL-1
table and equation.
Solution:
Circuit diagram of 2-to-4-line decoder (2 M), Truth table(2M) and
Equations (1M)
CO-4; SO-1;   d.   Compare synchronous and asynchronous counter.   [05]
BL-2
Solution: (any five valid point- 5 Marks)
Points   Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous Counters,
Trigge   Counters, all the constituent   there is triggering of different flip-
r   flip-flops are triggered with   flops with different clock.
same clock simultaneously.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster as   asynchronous counter is
ion
compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are more
error-prone; they hardly produce   error-prone and produce decoding
Error
any decoding errors because   errors in the system.
Prone
each flip-flop is individually
clocked.
All the flip-flops in a   In an asynchronous counter, the
synchronous counter coordinate   output of one flip-flop acts as the
Compl   with the clock, hence its design   input of the next flip-flop, hence its
exity   and implementation is complex   design and implementation is quite
as compared to that of an   simple.
asynchronous counter.
A Synchronous counter can be   An Asynchronous counter can
operated in any desired count   operate only in a fixed count
Seque
sequence, as it could get   sequence, i.e., UP and DOWN.
nce
manipulated by changing the
clock sequence.
********** 2 **********
--- page 3 ---
There is no propagation delay   In case of asynchronous counters,
Delay   observed in case of Synchronous   there is a subsequent propagation
Counters.   delay from one flip-flop to another.
Q2   a.   Develop 4-bit Binary to Gray code converter.   [10]
CO-1; SO-1;   Solution: Truth table of 4-bit Binary to Gray code converter (02Marks)
BL-3
four k-map simplifications (04 Marks), with correct expressions (02
Marks),
logic diagram implementation (02 Marks)
Binary input   |   Gray code output   |
B3   B2   B1   B0   G3   G2   G1   G0
0   0   0   0   0   0   0   0
0   0   0   1   0   0   0   1
0   0   1   0   0   0   1   1
0   0   1   1   0   0   1   0
0   1   0   0   0   1   1   0
0   1   0   1   0   1   1   1
0   1   1   0   0   1   0   1
0   1   1   1   0   1   0   0
1   0   0   0   1   1   0   0
1   0   0   1   1   1   0   1
1   0   1   0   1   1   1   1
1   0   1   1   1   1   1   0
1   1   0   0   1   0   1   0
1   1   0   1   1   0   1   1
1   1   1   0   1   0   0   1
1   1   1   1   1   0   0   0
K-Map for G3:
G3 = B3
K-Map for G2:
K-Map for G1:
********** 3 **********
--- page 4 ---
K-Map for G0:
Q2   b.   Solve the following using Boolean algebra and implement using logic gates-   [10]
CO-2; SO-1;
BL-3   i) Y= ABC + A B C + A B C + ABC
ii) Y= A + B + CD̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
Solution:
i)   Simplification with Boolean laws mention at required steps(4Marks) +
Implementation (1 Marks)
ii)   Simplification with Boolean laws mention at required steps(4Marks) +
Implementation (1 Marks)
********** 4 **********
--- page 5 ---
Q3   a.   Demonstrate full adder circuit using logic gates with truth table and K-Map.   [10]
CO-3; SO-1;   Solution:
BL-2
Definition of full adder with block diagram(02Marks)
Truth table (02 Marks) & K-map solving (03 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A
one-bit full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the
operands, and Cin is a bit carried in from the next less significant stage. The full-adder is
usually a component in a cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers.
The circuit produces a two-bit output, output carry and sum typically represented by the
signals Cout and S
A B Cin Sum Carry
0 0 0   0   0
0 0 1   1   0
0 1 0   1   0
0 1 1   0   1
1 0 0   1   0
1 0 1   0   1
1 1 0   0   1
1 1 1   1   1
Q3   b.   Illustrate functioning of clocked “D” flip flop with block diagram, truth table,   [10]
CO-4; SO-1;   logic diagram and K-map.
BL-2
Solution:
Clocked “D” flip flop circuit diagram (4 Marks) and truth table (03 Marks)
+Working (03 Marks)
********** 5 **********
--- page 6 ---
Q4   a.   Solve the following expression using k-map & implement with minimum   [10]
CO-2; SO-1;   number of gates-
BL-3
Y = f(A, B,C,D) = m (1, 3,7,11, 15) + d(0,2,4)
Solution:
********** 6 **********
--- page 7 ---
K-Map entry (02 Marks) and correct Grouping with expression (06
Marks) + circuit implementation (02 Marks)
Q4   b.   Make a use of VHDL to write a code for implementing OR gate.   [10]
CO-5; SO-1;   Solution:
BL-3
5M Design code 5M Test bench code
DESIGN CODE for OR gate:
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;
Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;
entity or_gate is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
y : out STD_LOGIC);
end or_gate;
architecture Behavioral of or_gate is
begin
y <= a or b;
end Behavioral;
TESTBENCH CODE for OR gate:
library IEEE;
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity or_gate_tb is
end;
architecture bench of or_gate_tb is
component or_gate
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
y : out STD_LOGIC);
end component;
signal a: STD_LOGIC := '0';
********** 7 **********
--- page 8 ---
signal b: STD_LOGIC := '0';
signal y: STD_LOGIC;
begin
uut: or_gate port map ( a => a,
b => b,
y => y );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a.   Build the given function using single 8:1 multiplexer.   [10]
CO-3; SO-1;   F(A, B, C, D) = m (0, 3, 4, 5, 8, 9,12,15)
BL-3
Solution:
Design table (05 Marks) and Circuit diagram (05 Marks)
Q5   b.   Illustrate the operation of serial in serial out shift register with logic Diagram   [10]
CO-4; SO-1;   and waveforms.
BL-2
Solution:
Logic Diagram (04 Marks) +Waveforms (03 Marks) +Operation (03
Marks)
********** 8 **********
--- page 9 ---
This shift register is very similar to the SIPO above, except were before the
data was read directly in a parallel form from the outputs QA to QD, this time
the data is allowed to flow straight through the register and out of the other
end. Since there is only one output, the DATA leaves the shift register one bit
at a time in a serial pattern, hence the name Serial-in to Serial-Out Shift
Register or SISO.
The SISO shift register is one of the simplest of the four configurations as it
has only three connections, the serial input (SI) which determines what enters
the left hand flip-flop, the serial output (SO) which is taken from the output of
the right hand flip-flop and the sequencing clock signal (Clk). The logic circuit
diagram below shows a generalized serial-in serial-out shift register.
Well this type of Shift Register also acts as a temporary storage device or it
can act as a time delay device for the data, with the amount of time delay being
controlled by the number of stages in the register, 4, 8, 16 etc or by varying the
application of the clock pulses.
Q6   a.   Explain different modelling styles in VHDL in detail.   [10]
CO-5; BL-2 SO-1;   Solution: Three types 3M, 3M and 4M
********** 9 **********

[Text in pictures on this page, read by OCR]
= FLPLPLELFLEL— LAL

Q, | B | B | B |B | B | Bs By | Bost
2 oe: <5 SONS
Q [ o | 8 | B&B |B | & | B Bat | Bn

Sea, ee, ES

2. eo 2.
nn

Q, 0 0 0 0

> 4

By B,

_J_—
Output bit sequence

Figure2 Output Waveform of n-bit Right-Shift SISO Shift Register
--- page 10 ---
architecture HA_STRUCTURE of HALF_ADDER is
component XOR2
port (X, Y: in BIT; Z: out BIT);
end component;
component AND2
port (L, M: in BIT; N: out BIT);
end component;
begin
X1: XOR2 port map (A, B, SUM);
A1: AND2 port map (A, B, CARRY);
end HA_STRUCTURE;
•   The name of the architecture body is HA_STRUCTURE.
•   The entity declaration for HALF_ADDER specifies the interface ports for this architecture
body.
•   The architecture body is composed of two parts:
•   the declarative part (before the keyword begin) and the statement part (after the
keyword begin).
•   Two component declarations are present in the declarative part of the architecture
body. These declarations specify the interface of components that are used in the
architecture body. The components XOR2 and AND2 may either be predefined
components in a library
•   The declared components are instantiated in the statement part of the architecture body using
component instantiation statements. XI and A1 are the component labels for these component
instantiations. The first component instantiation statement, labeled XI, shows that signals A
and B (the input ports of the HALF_ADDER), are connected to the X and Y input ports of a
XOR2 component, while output port Z of this component is connected to output port SUM of
the HALF_ADDER entity.
architecture HA_CONCURRENT of HALF_ADDER is
begin
SUM <= A xor B after 8 ns;
CARRY <= A and B after 4 ns;
end HA_CONCURRENT;
The dataflow model for the HALF_ADDER is described using two concurrent signal assignment
statements
•   Delay information is included in the signal assignment statements using after clauses.
•   If either signal A or B, which are input port signals of HALF_ADDER entity, has an event, say
at time T, the right-hand-side expressions of both signal assignment statements are evaluated.
•   Signal SUM is scheduled to get the new value after 8 ns while signal CARRY is scheduled to
get the new value after 4 ns.
•   When simulation time advances to (T+4) ns, CARRY will get its new value and when
simulation time advances to (T+8) ns, SUM will get its new value. Thus, both signal
assignment statements execute concurrently.
•   Ordering of these statements in an architecture body is not important.
Behavioral Style Modelling
architecture DEC_SEQUENTIAL of DECODER2x4 is
begin process (A, B, ENABLE)
variable ABAR, BBAR: BIT; begin
ABAR := not A; - statement 1
BBAR := not B; - statement 2
if (ENABLE = '1')
then -statements 3
Z(3) <= not (A and B): - statement 4
********** 10 **********
--- page 11 ---
Z(0) <= not (ABAR and BBAR); ~ statement 5
Z(2) <= not (A and BBAR); - statement 6
Z(1 ) <= not (ABAR and B); - statement 7
else
Z<= "1111"; -statement8
end if;
end process;
end;
 A process statement, too, has
◼   a declarative part (between the keywords process and begin), and
◼   a statement part (between the keywords begin and end process).
The statements appearing within the statement part are sequential statements and are executed
sequentially.
Q6   b.   Design and implement Mod-8 asynchronous counter using JK Flip Flop.   [10]
CO-4; SO-1;   Solution: Diagram 3M,Truth Table 3M,Timing Diagram 4M
BL-1, 3
Q7   a.   With the help of truth table and K-Map develop the logic circuit of Priority   [05]
CO-3; SO-1;   Encoder.
BL-3
********** 11 **********

[Text in pictures on this page, read by OCR]
i 2 3 4 5 6 7 8 :
|
4 Clock i
| pulses Truth Table
0 AMOD-8 Ripple Counter

Input

CLK Outputs

Olpof * ‘ Pulses} A Bic
FFC 0 0 0 0
1 0 0 |

2 0 1 0

3 0 i i

op “g 4 1 0 0
— 5 i 0 |

6 | 1 0

a i i i

O/p of 8 0 0 0

FFA —

Fig. 9.6
--- page 12 ---
Solution: Truth Table 1M, K-Map 2M,Circuit Diagram 1M

PRIORITY ENCODER:

+ As the name indicates, the priority is given to inputs line.

+ Iftwo or more input lines are high at the same time i.e 1 at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priorit

nput TRUTH TABLE:

Y, INPUTS OUTPUTS Vi

D, Ds | D2] Di | Do | Yil Yo
Priority 0 0 0 0 x x oO

D, Encoder
——) ¥; 0 0 0 1 0 0 1
0

D, ——o 1
0 0 0 1 x 0 1
0 il x x 1 0 1
»west Priority Output 1 x x x ul 1 1

H
Diagram of Priority Fig.15

* There are four inputs Dp, D,,D,, D; and two outputs Y, and Y,

* D, has highest priority and Dy is at lowest priority.

* IfD,=1 irrespective of other inputs then output Y,Y)=11.

* D, is at highest priority so other inputs are considered as don’t care

K-map for Y, and Y
D,Dy _D,Dp A “
D,D, \_00___ 01 l= 10) D3DSN 00s 00

00] X 0 0 0 00] X 0 | :1 1:

ot! 1 1 1 1} ao} 0 | o | 0 | oO
of ia | a | | oa fit fa fa | ai
Y=D,+Ds Y,=D,+D,D, ¥ y
Fig. 16
LOGIC DIAGRAM OF PRIORITY ENCODER
Y,=D, +D,
Y, =D, +D,D,
D, Ds D, Dy

y

Fig. 17

FRR ICR] DA KH
--- page 13 ---
Q7   b.   Construct Canonical Product of Sum expression of   [05]
CO-3; SO-1;   Y=(A+B’) (B+C) (A+C’)
BL-3
Solution:
Q7   c.   Explain the Race around condition in JK flip-flop.   [05]
CO-4; SO-1;   Solution:
BL-2
Explanation (04) with diagram (01)
In JK Flip-flop – For J-K flip-flop, if J=K=1, and if clk=1 for a long period of time, then Q output will
toggle as long as CLK is high, which makes the output of the flip-flop unstable or uncertain. This
problem is called race around condition in J-K flip-flop. In JK flip flop as long as clock is high for the
input conditions J&K equals to the output changes or complements its output from 1–>0 and 0–>1.
This is called toggling output or uncontrolled changing or racing condition. Consider above J&K circuit
diagram as long as clock is high and J&K=11 then two upper and lower AND gates are only triggered by
the complementary outputs Q and Q(bar). I.e. in any condition according to the propagation delay one
gate will be enabled and another gate is disabled. If upper gate is disabled, then it sets the output and
in the next lower gate will be enabled which resets the flip flop output
Q7   d.   Solve the following:   [05]
CO-1; SO-1;
Subtract 28 from 15 using 1’s complement method.
BL-3
Solution:
One’s Compliment 2M
Addition 1M
Answer 2M
28-11100
15-01111
1’s Compliment 28- 00011
Add: 01111+00011=10010
********** 13 **********
--- page 14 ---
No Carry answer negative and one’s compliment 01101

FRR IC 7 I OH
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 8ef56c4d3654

- Departments: Computer Engineering, Cyber Security, Electronics and Telecommunication, Information Technology, Mechatronics
- Programmes: BTech CyberSecurity 7010, BTech EXTC 7006, BTech IT 7001, BTech Mechatronics 7004, Integrated Computer 7032, Integrated IT 7037, MBATech Computer 7047, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CyberSecurity_7010/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf` (+7 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Dec 2025
- Text: mixed (19 pages), mean OCR confidence 75.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 09 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q   Answer briefly:   [20
1   ]
CO-   a. Translate the following binary number 1011011.01101 into (i) decimal, (ii) octal, and (iii)   [05
1;
SO-   hexadecimal.   ]
1;
BL-   Solution:
2
Conversion of binary numbers into decimal
(1011011.01101)2
= (1 × 26) + (0 × 25) + (1 × 24) + (1 × 23) + (0 × 22) + (1 × 21)
+ (1 × 20) + (0 × 2−1) + (1 × 2−2) + (1 × 2−3) + (0 × 2−4)
+ (1 × 2−5)
= 64 + 0 + 16 + 8 + 0 + 2 + 1 + 0 + 0.25 + 0.125 + 0 + 0.03125
= (91.40625)10
(3 marks [1 mark for each step])
Conversion of binary numbers into octal(Grouping of 3 ones)
(1011011.01101)2 = (001 011 011.011 010)2 = (133.32)8 --------------------------------
(1 mark)
Conversion of binary numbers into hexadecimal(Group of 4 ones)
(1011011.01101)2 = (0101 1011.0110 1000)2 = (5𝐵. 68)16 ------------------------------
(1 mark)
********** 1 **********
--- page 2 ---
CO- b Solve the following using Boolean algebra and implement using logic gates.   [05
2;
SO-   .   Y=   ̅̅̅̅̅̅̅̅B̅̅̅̅+̅̅̅̅̅̅̅̅̅̅̅̅ A +   C̅̅̅̅D̅̅̅̅   ]
1;
BL-   Simplification with Boolean laws mention at required steps(4Marks) +
3
Implementation (1 Marks)
CO-   c. Label and draw the circuit diagram of 2-line to 4-line decoder. Also, write its truth table   [05
3;
SO-   and explain its working in brief.   ]
1;
BL-   Circuit diagram of 2-to-4-line decoder (3 Marks) and Truth table(2Marks)
1,2
Working with any one input case(01 Marks)
********** 2 **********
--- page 3 ---
CO- d Compare Combinational and Sequential logic circuits.   [05
4;
SO-   .   (Any five valid point- 5 Marks)   ]
1;
BL-
2
Q   a. Compare weighted and non-weighted codes.   [10
2   Explain the Binary to Gray code conversion process with the help of a circuit diagram and   ]
CO-   logical expressions. Also, translate the given Binary code (10110) into its equivalent Gray
1;
SO-   code.
1;
BL-
2   Compare weighted and non-weighted codes(5M)
Any 4 appropriate points --- 4M
Any 1 example each code --- 1M
Binary to Gray Code: (5M)
********** 3 **********

[Text in pictures on this page, read by OCR]
COMBINATIONAL CKT SEQUENTIAL CKT

. Its output is determined by the 1. Its output is determined by the present
present values of its input only. values of the input as well as past values

. Itdoes not have a memory. of the output.

. It does not have a feedback path 2. Ithas a memory and a feedback path
from output to Input. from output to input.

._ Its operation can be described by a 3. Its operation can be described by truth
truth table. table and timing diagram.

. It does not have a clock signal . 4. It may or may not have clock signal but

. Its action does not depend on clock most sequential ckt have a clock signal.
transition. 5. Its ckt is more complex than that of

. Its ckt is simpler than that of combinational ckts.
sequential logic ckt. 6. Itis built using basic gates and

._ It built using basic gates i.e combinational logic ckts.

NOT,AND,OR,NAND,NOR,XOR,XNOR 7. Ex:- flip flops, counters,shift registers.
etc.

. Ex:- Adder Subtractor,

multiplexer, demux.decoder,compar

ator,

Weighted Codes Non-Weighted Codes

Codes in which each bit position is assigned Codes in which no fixed weights are assigned
a fixed weight or value. The total value of _ to bit positions. The value of the code word
the code word is obtained by adding the cannot be directly obtained by adding bit

weights of the bits that are 1. weights.

Each digit has positional weight (like 8-4-2- Each digit does not represent a specific
1). positional weight.

Easy to perform arithmetic operations Difficult to perform arithmetic operations
because weights correspond to actual directly.

values.

Less efficient for error detection. More efficient for error detection and

correction purposes.
Examples are: i) Binary code ii)BCDCode Examples are: i) Gray Code (used to prevent
(weights: 8, 4, 2, 1) errors during transitions)
ii) Excess-3 Code (each decimal digit
represented by its 8, 4, 2, 1 code + 3)
--- page 4 ---
Circuit Diagram with process(3M) :
B3 G3

B2 )>

7486N

G2

B3(4)B2

B1 —) > B1(4)B2 $1

7486N

GO

Bo —)>
7486N
Conversion of a binary number to Gray code
A binary number can be converted to its Gray code when

B1(#)B0

(i) the first bit (MSB) of the Gray code is the same as the first bit of the binary number;
(ii) the second bit of the Gray code equals the exclusive-OR, of the first and second bits of
the binary number, i.e. it will be 1 if these binary code bits are different and 0 if they
are the same;
(iii) the third Gray code bit equals the exclusive-OR of the second and third bits of the
binary number, and so on.

logical expressions: (1M)
G3 = Bs

G2=B3®@B2
G1=B1@®B2

GO =B1#@B0

Conversion (1M)

FSC ICR 2c Gk ACK OK ok
--- page 5 ---
Ans: 11101
Q   b Define Minterm in Boolean algebra.   [10
2   .   Construct the given logic function f = ABC + BC’D + A’BC in the following steps:   ]
CO-   i) Develop the Truth Table.
2;
SO-   ii) Determine the corresponding Minterms.
1;
BL-   iii) Simplify the function using K-Map
1,3   iv) Implement the simplified function using NAND gates only.
Minterm definition (01 Marks)
2 marks for truth table , 2 marks for minterms , 4 marks for k-map, 2 marks for diagram
Given the logic function f = ABC+BC’D+A’BC
Variables: A,B,C,D
i)Truth table (A B C D → F)
I list all 16 rows; 1 means F=1, 0 means F=0
A B C D   ABC   BC’D   A’BC   F = ABC + BC'D + A'BC   Minterm
0   0   0   0   0   0   0   0
0   0   0   1   0   0   0   0
0   0   1   0   0   0   0   0
0   0   1   1   0   0   0   0
0   1   0   0   0   0   0   0
0   1   0   1   0   1   0   1   minterm 5
0   1   1   0   0   0   1   1   minterm 6
0   1   1   1   0   0   1   1   minterm 7
1   0   0   0   0   0   0   0
1   0   0   1   0   0   0   0
1   0   1   0   0   0   0   0
1   0   1   1   0   0   0   0
********** 5 **********

[Text in pictures on this page, read by OCR]
Step I The first bit MSB of the Gray code is the same as the first bit of the binary
number.

1 0 1 1 O Binary
Y
1 Gray

Step 2. Add the first bit of the binary digit to the second bit of the binary. The addition of
1 and 0 is 1. The result is the second bit of the Gray code.

1 1 0 Binary
+

1 1 Gray
Step 3 Add the second bit 0 to the third bit 1 of the binary.
! 1 0 Bin ra
+

11 1 Gray

Step 4 Add the third bit | to the fourth bit 1 and omit the carry. The exclusive OR addition
of | and | is 0. This is the fourth bit of the Gray code.

10 0 Binary
+

11 0 Gray
Step 5 Add the fourth bit | to the last bit of the binary.
1o. Binary
+

1110 1 Gray

As the conversion is complete. the Gray code of the binary 10110 is 11101.
--- page 6 ---
1   1   0   0   0   0   0   0
1   1   0   1   0   1   0   1   minterm 13
1   1   1   0   1   0   0   1   minterm 14
1   1   1   1   1   0   0   1   minterm 15
ii) Minterms where F=1: m(5,6,7,13,14,15).
minterm 5 – A’BC’D, minterm 6 – A’BCD’, minterm 7 – A’BCD
minterm 13 – ABC’D, minterm 14 – ABCD’,minterm 15 – ABCD
iii) Simplify using K Map.
Q   a. Develop a Full Subtractor combinational logic circuit by applying the K-map technique   [10
3   truth table, and implement the circuit using basic logic gates. Also,   ]
CO-   explain its operation brief.
3;
SO-   Definition of full Subtractor with block diagram(01Marks)
1;   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
BL-
3   Any Valid Circuit diagram & working (03 Marks)
********** 6 **********

[Text in pictures on this page, read by OCR]
Full-subtractor Just like a full-adder, we require a full-subtractor circuit for performing multibit
subtraction wherein a borrow from the previous bit position
may also be there. A full-subtractor will have three inputs,
A, (minuend), B, (subtrahend) and C,_, (borrow from the
previous stage) and two outputs, D, (difference) and C,
(borrow). Its truth table is given in Table 5.14. The K-map
for the output D, is exactly same as the K-map for 5, of the
adder circuit and therefore, its realisation is same as given
in Fig. 5.2la.
--- page 7 ---
Table 5.14 Truth Table of a Full-subtractor

Inputs Outputs
A, B C.., D, C,
0 0 0 0 0
0 0 l 1 1
0 I 0 1 1
0 1 l 0 1
1 0 0 1 0
1 0 1 0 0
1 1 0 0 0

The K-map for C, is given in Fig. 5.23a and its realisation is given in Fig. 5.23b. The simplified expression
for C, is _ _
C, =A, B,+4,C,. 4B, C,. (5.37)

Ay o—4

A,B,
A,B, B
Gs 00 01 ll 10 1 O—
7X

0 1

eo

Cy-10—

aioin

B, o

- Cy. —4
AnCy1 Bry oe
(a) (b)

Fig. 5.23 (a) K-map for C, (b) Realisation of C,

Cn can also be known as borrow(b) in subtractor

BC
AX 00 O01 11° «10
ft) 1 i

1| 1 1

(I) K-map for Difference

FSC ICR 7 Fo ACK ACK OK ok
--- page 8 ---
Circuit Diagram & working for any one case:
Q   b Develop a T Flip-Flop using a JK Flip-Flop. Derive the conversion logic and present the   [10
3   .   implementation with a neat and labeled diagram.   ]
CO-   Write the Conversion Logic and Available logic table details - (Marks 5)
4;
SO- 1;   The given flip-flop is JK flip-flop and the desired flip-flop is T flip-flop. Therefore,
BL-
3   consider the following characteristic table of JK flip-flop as Conversion logic
T Flip-Flop   Present   Next State
Input   State
T   Q(t)   Q(t + 1)
0   0   0
0   1   1
1   0   1
1   1   0
********** 8 **********
--- page 9 ---
We know that JK flip-flop has two inputs J & K. So, write down the excitation values
of JK flip-flop for each combination of present state and next state values. The following
table shows the characteristic table of T flip-flop along with the excitation inputs of JK
flip-flop.
T Flip-   Present   Next   JK Flip-Flop
Flop Input   State   State   Inputs
T   Q(t)   Q(t + 1)   J   K
0   0   0   0   x
0   1   0   x   1
1   0   1   1   x
1   1   1   x   0
1) Make K Map for getting input equation of JK flip flop - (Marks 3)
2) Logic diagram of Conversion of Flip Flop - (Marks 2)
Q   a. Solve the following expression using k-map to obtain the minimal POS expression &   [10
4   implement using basic gates.   ]
CO-   Y = f(W,X,Y,Z) = πM (3,5,7,11,15).d (0,8,12)
2;
SO-   Solution:
1;
BL-   K-Map entry (02 Marks) and correct Grouping with expression (06 Marks) + circuit
3
implementation (02 Marks)
Given expression F(W,X,Y,Z)=∏M(3,5,7,11,15) + d(0,8,12)
********** 9 **********
--- page 10 ---
F = 0 at minterms 3,5,7,11,15 and don’t-care terms at 0,8,12. The function is 1 for all other
combinations of W,X,Y,Z.
4-Variable K-Map Layout
00   01   11   10
00   0   1   3   2
01   4   5   7   6
10   12   13   15   14
11   8   9   11   10
Q   b   Outline the specifications of VHDL and develop the VHDL code for implementing a full-   [10
4   .   adder circuit.   ]
CO-   The Specifications of VHDL any 4 valid point (02 Marks)
5;
SO-   Full Adder block diagram with output expression (02 Marks)
1;   Final code with any correct logic(06 Marks)
BL-
2,3
The Specifications of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks simultaneously.
* Library support
********** 10 **********
--- page 11 ---
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
entity full_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
c : in STD_LOGIC;
s : out STD_LOGIC;
cy : out STD_LOGIC);
end full_adder;
architecture Behavioral of full_adder is
begin
s <= a xor b xor c;
cy <= (a and b) or (b and c) or (a and c);
end Behavioral;
TEST BENCH CODE:
library IEEE;
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
c : in STD_LOGIC;
s : out STD_LOGIC;
cy : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal c: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal cy: STD_LOGIC;
begin
uut: full_adder port map ( a => a,
b => b,
c => c,
s => s,
cy => cy );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
********** 11 **********
--- page 12 ---
b <= not b;
wait for 20 ns;
end process;
stimulus3: process
begin
c <= not c;
wait for 40 ns;
end process;
end;
Q   a. Build the given function using a single 8:1 multiplexer.   [10
5   F(A, B, C, D) = m (2,4,6,7,9,10,11,12,15)   ]
CO- 3;   Ans: Design table (05 Marks) and Circuit diagram (05 Marks)
SO-
1;
BL-
3
We can group 2-2 rows as values of A, B and C are
remaining same for 2 rows.
Then by observing value of D and output Y ,we can predict
output Y whether it will be 0, 1,D, and D’
*(D’ is D compliment or D Bar)
********** 12 **********

[Text in pictures on this page, read by OCR]
Inputs Output

A B Cc D Y
0 0 0 0 0
0 0 0 1 0
pn 0 0 | 0 Fi
0 0 1 1 0
—_ (0
0 1 0 1 0
— ee I |
amaue 0 eeeeli....d 2...
1 0 0 0 0
1 0 0 1 1
po mr an I I 259
= | nt... /....L...- r
] 1 0 0 1
1 1 0 1 0
po en een We WI? |
--- page 13 ---
Q   b   List the types of registers and explain the operation of serial in-parallel out shift   [10]
5   .   register with logic diagram. List of Register types(01 Marks)
CO-   Logic Diagram (04 Marks) +Waveforms/table (03 Marks) +Operation (03 Marks)
4;
SO- 1;   SIPO - In a SIPO register, data is shifted serially (one bit at a time) into the register on each
BL-   clock pulse, and the output is available in parallel from all flip-flops simultaneously.
1,2   Working Table:
Clock Q1 Q2 Q3 Q4
0   0   0   0   0
1   1   0   0   0
2   1   1   0   0
3   0   1   1   0
4   1   0   1   1
********** 13 **********

[Text in pictures on this page, read by OCR]
(ii) Second Method: A four variable truth table or logic expression can be realised by using an 8:1 multiplexer
instead of a 16:1 multiplexer. For this, partition the truth table as shown by dotted lines, Here the inputs 4, B,
and C are to be connected to S,, §, and S, select inputs respectively. Now, we observe the relationship between
input D and output Y for each group of two rows. There are four possible values of Y and these are 0), 1, D, and
D. These are given in Table 6.4. From this table, we note the output Y for each of the combinations of , B, and
C, and then make the connections accordingly, The implementation of this function using an 8:1 multiplexer
is shown in Fig, 6.4.
--- page 14 ---
Q   a. List and briefly explain all built-in datatypes in VHDL and give an example of each. Explain [10
6   in detail structural style of modelling.   ]
CO-   Datatypes ….. 5 marks
5;
SO- 1;   Explanation of structural modelling style ….. 5 marks
BL-
1,2
Structural modeling in VHDL describes a digital system as an interconnection of lower-
level components, similar to how a circuit diagram is constructed. It involves creating
individual VHDL entity-architecture pairs for each component, then instantiating these
components within a higher-level architecture and connecting them using signals. This style
is effective for describing complex designs by breaking them into smaller, reusable
modules.
Key characteristics
Component-based: The design is built by instantiating and connecting pre-defined
components.
Hierarchical: It allows for the creation of complex systems from simpler,
hierarchical blocks, making it suitable for large-scale designs.
Schematic-like: The code directly mirrors the structure of a circuit diagram with
blocks (components) and lines (signals).
********** 14 **********

[Text in pictures on this page, read by OCR]
Built-in Datatypes

O Scalar (single valued) signal types:
@ bit
@ boolean
@ integer
= Examples:
O A: in bit;
O G: out boolean;
O XK: out integer range -2**4 to 2**4-1;
Oo Aggregate (collection) signal types:
bit_vector: array of bits representing binary numbers
: signed: array of bits representing signed binary numbers
= Examples:
OD: in bit_vector(0 to 7);
O E: in bit_vector(7 downto 0);

O M: in signed (4 downto 0);
--signed 5 bit_vector binary number
--- page 15 ---
Component description: The individual components can be described using any
modeling style, including behavioral or dataflow, as long as they are defined as a
complete entity-architecture pair.
How it works
Define components: Create separate VHDL files or sections for each component
(e.g., half_adder, XOR_gate). Each component must have its own entity declaration
defining its ports and an architecture to describe its function.
Instantiate components: In the main architecture of your higher-level design, declare
the components you will use. This is typically done by creating a component
declaration based on the entity of each sub-module.
Label components: Give each instance of a component a unique label or label. This
is necessary for referring to a specific instance and its ports.
Map ports: Create instances of the components and map their ports to internal signals
or the top-level entity's ports.
Declare signals: Declare internal signal objects that will connect the output ports of one
component to the input ports of another.
Q   b Build and implement MOD-9 ripple up counter using T flip-flop. Give its Timing   [10
6   .   Diagram.   ]
CO- 4;   Design table with any correct logic & K-MAP (07) + Logical Diagram (02) +waveform (01)
SO-
1;
BL-
3
********** 15 **********
--- page 16 ---
jon P
gotwtiorne minimum number of flip-flops re, Stress
1. MS2" or 9<on oe ‘qired is
= . n=4
jgn the combinational logic cirey;
2. nine clock pulses. Feuit such that the flip-flops are clear after
The truth table of a 4-pit

a)
the output of the combin:

UP aes
counter is given in Table 5.42, where Yis

___— table 5-42 Truth table of abit Up counter with output Y
Clock Q; Ea a a 7
i ae ee ‘0
° ° rr
i ° ° ° 1
° 1 1
2 ° ° 1 3 1
3 ° ° i ;
4 ° 1 0 0 .
5 ° 1 0 i a
6 ° 1 1 a 1
7 o 1 1 1 1
8 1 ° o Cv) 1
9 1 ° o 1 o
10 1 ° 1 ° x
11 1 ° 1 1 x:
12 1 1 ° ° >
13 1 1 ° 1 x
L 14 1 1 1 oO x
15 1 1 1 1 x

(b) K-map for Y:

392
2,25 :00
00
ol
1l
10

FIC IGR 7 6 FR Ae
--- page 17 ---
Q   a.   Illustrate BCD to seven segment decoder with the help of block diagram and truth table.   [05
7   Block diagram(2M) +Truth table(3M)   ]
CO-
3;
SO-
1;
BL-
2
********** 17 **********

[Text in pictures on this page, read by OCR]
The logic circuit of Mod-9 asynchronous counter is shown in Fj B58)

Fig. 5.81 Mod-9 nine asynchronous counter

The waveforms of Mod-9 ripple counter are shown in Fig. 5.82,

ol ioe
att ppt I Tk
oj
fio Pod do do Po EF

t

Flip-flop
; is clear
Fig. 5.82 Waveforms of Mod-9 ripple counter
--- page 18 ---
Q   b Show the implementation of AND & OR logic gates using NAND gates.   [05
7   . AND and OR diagram using NAND gates with expression at output of each gate(2+3marks)   ]
CO-
2;
SO-
1;
BL-
2
AND gate using NAND
OR gate using NAND
Q   c. Explain the need of Master–Slave JK Flip-Flop. Illustrate the same with a logic diagram [05
7   and truth table.   ]
********** 18 **********

[Text in pictures on this page, read by OCR]
BCD to seven segment decoder is a circuit used to convert the input BCD into a form
suitable for the display. It has four input lines (A, B, C and D) and 7 output lines (a, b, ¢, d, e,
f and g) as shown in Figure 3. Considering common cathode type of arrangement, the truth

table for the decoder can be given as in Table I.

| > _
A—— -———> b
B BCD-to-Seven ->———> ©

BCD —_—4 segment _}+———>d Output lines
Input lines Cc decoder |» e
/—_———> f
D——_ W————>

Figure 3 BCD-to-Seven segment decoder

Table I Truth table for common cathode type BCD to seven segment decoder

[Decimal | Input lines Output lines Display
Digit [A] B]C]D]a|]b|c[d]e]f]g| Pattern

0 fO;O;ojortytytititjsioy B®
1 7O/0)/0)170/1/1/0;0];0;0 !

S [ee Peres ae eet

This table indicates the segments which are to be driven high to obtain certain decimal digit
at the output of the seven segment display. However, it is to be noted that in the case of
common anode type, the only change will be to interchange ones and zeros on the table. This

means that from the e so obtained one can get to know where low has to be driven

so as to obtain the required digit at the output.
--- page 19 ---
CO-   Need (1M)– It should cover avoid of race around condition
4;
SO-   Logic diagram using two JK F/F (2M)
1;
BL-   Truth table(2M)- Same as Negative edge trigger JK Flip flop
2
Q   d Solve (25)10 – (34)10 using 2’s complement method and show the final result in decimal [05
7   .   form.   ]
CO-   Binary equivalent of 25 is 011001
1;
SO-   Binary equivalent of 34 is 100010   [1M]
1;   To subtract 34 from 25 using 2’s complement, take 2’s complement of 34 and
BL-
3   add to 25.
1’s complement of 34 = 011101
+   1
2’s complement of 34 = 011110   [1M]
25  011001
2’s complement of 34  + 011110
110111   [1M]
No carry generated so Ans is -ve and in 2’s complement form
1’s complement of result = 001000
+   1
001001   [1M]
Ans is -9   [1M]
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 6e84340cbe1c

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_EXTC_7006/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026_6e84340cbe.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Dec 2025
- Text: mixed (19 pages), mean OCR confidence 78.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 09 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q   Answer briefly:   [20
1   ]
CO-   a. Translate the following binary number 1011011.01101 into (i) decimal, (ii) octal, and (iii)   [05
1;
SO-   hexadecimal.   ]
1;
BL-   Solution:
2
Conversion of binary numbers into decimal
(1011011.01101)2
= (1 × 26) + (0 × 25) + (1 × 24) + (1 × 23) + (0 × 22) + (1 × 21)
+ (1 × 20) + (0 × 2−1) + (1 × 2−2) + (1 × 2−3) + (0 × 2−4)
+ (1 × 2−5)
= 64 + 0 + 16 + 8 + 0 + 2 + 1 + 0 + 0.25 + 0.125 + 0 + 0.03125
= (91.40625)10
---------------------------------------------------- (3 marks [1 mark for each step])
Conversion of binary numbers into octal(Grouping of 3 ones)
(1011011.01101)2 = (001 011 011.011 010)2 = (133.32)8 --------------------------------
------------------------------------------------------------ (1 mark)
Conversion of binary numbers into hexadecimal(Group of 4 ones)
(1011011.01101)2 = (0101 1011.0110 1000)2 = (5𝐵. 68)16 ------------------------------
------------------------------------------------------------- (1 mark)
********** 1 **********
--- page 2 ---
CO- b Solve the following using Boolean algebra and implement using logic gates.   [05
2;
SO-   .   Y= A + B +   CD̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅   ]
1;
BL-   Simplification with Boolean laws mention at required steps(4Marks) +
3
Implementation (1 Marks)
CO-   c. Label and draw the circuit diagram of 2-line to 4-line decoder. Also, write its truth table   [05
3;
SO-   and explain its working in brief.   ]
1;
BL-   Circuit diagram of 2-to-4-line decoder (3 Marks) and Truth table(2Marks)
1,2
********** 2 **********

[Text in pictures on this page, read by OCR]
Decoders

on w W=A'B
B—lo Out, — X X=AB'
A—h Y=A'B
msb Z=AB
0 0 1 0 0 0
0 1 0 1 0 0
1 0 0 0 1 0
--- page 3 ---
CO- d Compare Combinational and Sequential logic circuits.   [05
4;
SO-   .   (Any five valid point- 5 Marks)   ]
1;
BL-
2
Q   a. Compare weighted and non-weighted codes.   [10
2   Explain the Binary to Gray code conversion process with the help of a circuit diagram and   ]
CO-   logical expressions. Also, translate the given Binary code (10110) into its equivalent Gray
1;
SO-   code.
1;
BL-
2   Compare weighted and non-weighted codes(5M)
Any 4 appropriate points --- 4M
Any 1 example each code --- 1M
Binary to Gray Code: (5M)
********** 3 **********

[Text in pictures on this page, read by OCR]
COMBINATIONAL CKT SEQUENTIAL CKT

Its output Is determined by the 1. Its output is determined by the present
present values of its input only. values of the input as well as past values
It does not have a memory. of the output.

It does not have a feedback path 2. Ithas a memory and a feedback path
from output to input. from output to input.

Its operation can be described by a 3. Its operation can be described by truth
truth table. table and timing diagram.

It does not have a clock signal . 4. It may or may not have clock signal but
Its action does not depend on clock most sequential ckt have a clock signal.
transition. 5. Its ckt is more complex than that of

Its ckt is simpler than that of combinational ckts.

sequential logic ckt. 6. It is built using basic gates and

It built using basic gates i.e combinational logic ckts.

NOT.AND,OR,NAND,NOR,XOR,XNOR 7. Ex: flip flops, counters.shift registers.
etc.

Ex:- Adder, Subtractor,

Weighted Codes Non-Weighted Codes

Codes in which each bit position is assigned Codes in which no fixed weights are assigned
a fixed weight or value. The total value of _ to bit positions. The value of the code word
the code word is obtained by adding the cannot be directly obtained by adding bit

weights of the bits that are 1. weights.

Each digit has positional weight (like 8-4-2- Each digit does not represent a specific
1). positional weight.

Easy to perform arithmetic operations Difficult to perform arithmetic operations
because weights correspond to actual directly.

values.

Less efficient for error detection. More efficient for error detection and

correction purposes.
Examples are: i) Binary code ii)BCD Code Examples are: i) Gray Code (used to prevent
(weights: 8, 4, 2, 1) errors during transitions)
ii) Excess-3 Code (each decimal digit
represented by its 8, 4, 2, 1 code + 3)
--- page 4 ---
Circuit Diagram with process(3M) :
B3 G3

B2 _)>

7486N

G2

B3(@)B2

o — nor *

7486N Bt @B2

BO _) > Go
7486N
Conversion of a binary number to Gray code

A binary number can be converted to its Gray code when

B1(4)BO

(i) the first bit (MSB) of the Gray code is the same as the first bit of the binary number;
(ii) the second bit of the Gray code equals the exclusive-OR, of the first and second bits of
the binary number, i.e. it will be | if these binary code bits are different and 0 if they
are the same;
(iii) the third Gray code bit equals the exclusive-OR of the second and third bits of the
binary number, and so on.

logical expressions: (1M)
G3 = B3

G2=B3®B2
G1=Bi@B2
GO=B1#BoO

Conversion (1M)

FIC 7) IC HOH
--- page 5 ---
Ans: 11101
Q   b Define Minterm in Boolean algebra.   [10
2   .   Construct the given logic function f = ABC + BC’D + A’BC in the following steps:   ]
CO-   i) Develop the Truth Table.
2;
SO-   ii) Determine the corresponding Minterms.
1;
BL-   iii) Simplify the function using K-Map
1,3   iv) Implement the simplified function using NAND gates only.
2 marks for truth table , 2 marks for minterms , 4 marks for k-map, 2 marks for diagram
Given the logic function f = ABC+BC’D+A’BC
Variables: A,B,C,D
i)Truth table (A B C D → F)
I list all 16 rows; 1 means F=1, 0 means F=0
A B C D   ABC   BC’D   A’BC   F = ABC + BC'D + A'BC   Minterm
0   0   0   0   0   0   0   0
0   0   0   1   0   0   0   0
0   0   1   0   0   0   0   0
0   0   1   1   0   0   0   0
0   1   0   0   0   0   0   0
0   1   0   1   0   1   0   1   minterm 5
0   1   1   0   0   0   1   1   minterm 6
0   1   1   1   0   0   1   1   minterm 7
1   0   0   0   0   0   0   0
1   0   0   1   0   0   0   0
1   0   1   0   0   0   0   0
1   0   1   1   0   0   0   0
********** 5 **********

[Text in pictures on this page, read by OCR]
Step 1 The first bit MSB of the Gray code is the same as the first bit of the binary
number.

1 0 1 1 O Binary
Y
1 Gray

Step 2. Add the first bit of the binary digit to the second bit of the binary. The addition of
1 and 0 is 1. The result is the second bit of the Gray code.

11 0 Binary
J

1 1 Gray
Step 3 Add the second bit 0 to the third bit 1 of the binary.

1 @ 1) 1 0 Bin m
+

11 1 Gray

Step 4 Add the third bit | to the fourth bit 1 and omit the carry. The exclusive OR addition
of | and | is 0. This is the fourth bit of the Gray code.

10 0 Binary
4
11d 0 Gray

Step 5 Add the fourth bit | to the last bit of the binary.

1 0 1 U_©@_O} Binary
Y
11 10 1 Gray

As the conversion is complete, the Gray code of the binary 10110 is 11101.
--- page 6 ---
1   1   0   0   0   0   0   0
1   1   0   1   0   1   0   1   minterm 13
1   1   1   0   1   0   0   1   minterm 14
1   1   1   1   1   0   0   1   minterm 15
ii) Minterms where F=1: m(5,6,7,13,14,15).
minterm 5 – A’BC’D, minterm 6 – A’BCD’, minterm 7 – A’BCD
minterm 13 – ABC’D, minterm 14 – ABCD’,minterm 15 – ABCD
iii) Simplify using K Map.
Q   a. Develop a Full Subtractor combinational logic circuit by applying the K-map technique   [10
3   truth table, and implement the circuit using basic logic gates. Also,   ]
CO-   explain its operation brief.
3;
SO-   Definition of full Subtractor with block diagram(01Marks)
1;   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
BL-
3   Any Valid Circuit diagram & working (03 Marks)
********** 6 **********

[Text in pictures on this page, read by OCR]
Full-subtractor Just like a full-adder, we require a full-subtractor circuit for performing multibit
subtraction wherein a borrow from the previous bit position
may also be there. A full-subtractor will have three inputs,
A, (minuend), B, (subtrahend) and C,_, (borrow from the
previous stage) and two outputs, D, (difference) and C,
(borrow). Its truth table is given in Table 5.14. The K-map
for the output D, is exactly same as the K-map for S, of the
adder circuit and therefore, its realisation is same as given
in Fig. 5.21a.
--- page 7 ---
Table 5.14 Truth Table of a Full-subtractor

Inputs Outputs
A B C., D, C,
0 0 0 0 0
0 0 l 1 1
0 1 0 1 1
0 1 1 0 1
1 0 0 1 0
1 0 l 0 0
1 1 0 0 0

The K-map for C, is given in Fig. 5.23a and its realisation is given in Fig. 5.23b. The simplified expression
for C. is

C,=4,B, +4, Ci +B, Ca (637)
A,B, A,By i o—
GX 0 of 1 hn o—
0 1 A, oo
C Cn
n~| O—
Gol
iN
B, o—
AyCy-1 Brn Cr
(a) (b)

Fig. 5.23 (a) K-map for C, (b) Realisation of C,

Cn can also be known as borrow(b) in subtractor

BC

AX 00 O1 11° 10
i) 1 1
1| 1 1

(I) K-map for Difference

FIC 7 IC OHH
--- page 8 ---
Circuit Diagram & working for any one case:
Q   b Develop a T Flip-Flop using a JK Flip-Flop. Derive the conversion logic and present the [10
3   .   implementation with a neat and labeled diagram.   ]
CO-   Write the Conversion Logic and Available logic table details - (Marks 5)
4;
SO- 1;   The given flip-flop is JK flip-flop and the desired flip-flop is T flip-flop. Therefore,
BL-
3   consider the following characteristic table of JK flip-flop as Conversion logic
T Flip-Flop   Present   Next State
Input   State
T   Q(t)   Q(t + 1)
0   0   0
0   1   1
1   0   1
1   1   0
********** 8 **********

[Text in pictures on this page, read by OCR]
Full Subtractor Expression
d=ABC+ABC+ABC+ABC
b = AC+AB+BC
Also,

d=A@BOC} or |d= > m(1.2.3.7)

b=ABC+ABC+ABC+ABC
b=C(AQB)+AB
--- page 9 ---
We know that JK flip-flop has two inputs J & K. So, write down the excitation values
of JK flip-flop for each combination of present state and next state values. The following
table shows the characteristic table of T flip-flop along with the excitation inputs of JK
flip-flop.
T Flip-   Present   Next   JK Flip-Flop
Flop Input   State   State   Inputs
T   Q(t)   Q(t + 1)   J   K
0   0   0   0   x
0   1   0   x   1
1   0   1   1   x
1   1   1   x   0
1) Make K Map for getting input equation of JK flip flop - (Marks 3)
2) Logic diagram of Conversion of Flip Flop - (Marks 2)
Q   a. Solve the following expression using k-map to obtain the minimal POS expression & [10
4   implement using basic gates.   ]
CO-   Y = f(W,X,Y,Z) = πM (3,5,7,11,15).d (0,8,12)
2;
SO-   Solution:
1;
BL-   K-Map entry (02 Marks) and correct Grouping with expression (06 Marks) + circuit
3
implementation (02 Marks)
Given expression F(W,X,Y,Z)=∏M(3,5,7,11,15) + d(0,8,12)
********** 9 **********
--- page 10 ---
F = 0 at minterms 3,5,7,11,15 and don’t-care terms at 0,8,12. The function is 1 for all other
combinations of W,X,Y,Z.
4-Variable K-Map Layout
00   01   11   10
00   0   1   3   2
01   4   5   7   6
10   12   13   15   14
11   8   9   11   10
Q   b   Outline the specifications of VHDL and develop the VHDL code for implementing a full- [10
4   .   adder circuit.   ]
CO-   The Specifications of VHDL any 4 valid point (02 Marks)
5;
SO-   Full Adder block diagram with output expression (02 Marks)
1;   Final code with any correct logic(06 Marks)
BL-
2,3
The Specifications of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks simultaneously.
* Library support
********** 10 **********
--- page 11 ---
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
entity full_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
c : in STD_LOGIC;
s : out STD_LOGIC;
cy : out STD_LOGIC);
end full_adder;
architecture Behavioral of full_adder is
begin
s <= a xor b xor c;
cy <= (a and b) or (b and c) or (a and c);
end Behavioral;
TEST BENCH CODE:
library IEEE;
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
c : in STD_LOGIC;
s : out STD_LOGIC;
cy : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal c: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal cy: STD_LOGIC;
begin
uut: full_adder port map ( a => a,
b => b,
c => c,
s => s,
cy => cy );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
********** 11 **********
--- page 12 ---
b <= not b;
wait for 20 ns;
end process;
stimulus3: process
begin
c <= not c;
wait for 40 ns;
end process;
end;
Q   a. Build the given function using a single 8:1 multiplexer.   [10
5   F(A, B, C, D) = m (2,4,6,7,9,10,11,12,15)   ]
CO- 3;   Ans: Design table (05 Marks) and Circuit diagram (05 Marks)
SO-
1;
BL-
3
We can group 2-2 rows as values of A, B and C are
remaining same for 2 rows.
Then by observing value of D and output Y ,we can predict
output Y whether it will be 0, 1,D, and D’
*(D’ is D compliment or D Bar)
********** 12 **********

[Text in pictures on this page, read by OCR]
Inputs Output

A B Cc D Y
0 0 0 0 0
0 0 0 1 0
— re = =—h—UmUmrm™t™~—S
0 0 1 1 0
— meme = ==
0 1 0 1 0
— rm = =)—hrerrrrtr—
haenee 0........./.....1.___ |
1 0 0 0 0
1 0 0 1 1
—— r 0 4 es 7.) Cl a ]
Le... en
1 1 0 0 1
1 1 0 1 0
po rod en — je ]
--- page 13 ---
Q   b   List the types of registers and explain the operation of serial in-parallel out shift   [10]
5   .   register with logic diagram.
CO-   Logic Diagram (04 Marks) +Waveforms/table (03 Marks) +Operation (03 Marks)
4;
SO- 1;   SIPO - In a SIPO register, data is shifted serially (one bit at a time) into the register on each
BL-   clock pulse, and the output is available in parallel from all flip-flops simultaneously.
1,2   Working Table:
Clock Q1 Q2 Q3 Q4
0   0   0   0   0
1   1   0   0   0
2   1   1   0   0
3   0   1   1   0
4   1   0   1   1
********** 13 **********

[Text in pictures on this page, read by OCR]
(ii) Second Method: A four variable truth table or logic expression can be realised by using an 8:1 multiplexer
instead of a 16:1 multiplexer. For this, partition the truth table as shown by dotted lines, Here the inputs 4, B,
and C are to be connected to S,, §, and S, select inputs respectively. Now, we observe the relationship between
input D and output Y for each group of two rows. There are four possible values of Y and these are 0), 1, D, and
D. These are given in Table 6.4. From this table, we note the output Y for each of the combinations of A, B, and
C, and then make the connections accordingly, The implementation of this function using an 8:1 multiplexer
is shown in Fig, 6.4.

Inputs Output

B Cc Y
0 0 0
0 l D
l 0 D
1 1 1

0 0 D
0 1 1

1 0 D
--- page 14 ---
Q   a. List and briefly explain all built-in datatypes in VHDL and give an example of each. Explain [10
6   in detail structural style of modelling.   ]
CO-   Datatypes ….. 5 marks
5;
SO- 1;   Explanation of structural modelling style ….. 5 marks
BL-
1,2
Structural modeling in VHDL describes a digital system as an interconnection of lower-
level components, similar to how a circuit diagram is constructed. It involves creating
individual VHDL entity-architecture pairs for each component, then instantiating these
components within a higher-level architecture and connecting them using signals. This style
is effective for describing complex designs by breaking them into smaller, reusable
modules.
Key characteristics
Component-based: The design is built by instantiating and connecting pre-defined
components.
Hierarchical: It allows for the creation of complex systems from simpler,
hierarchical blocks, making it suitable for large-scale designs.
Schematic-like: The code directly mirrors the structure of a circuit diagram with
blocks (components) and lines (signals).
********** 14 **********

[Text in pictures on this page, read by OCR]
Built-in Datatypes

O Scalar (single valued) signal types:
@ bit
®@ boolean
@ integer
= Examples:
O A: in bit;
O G: out boolean;
O kK: out integer range -2**4 to 2**4-1;
Oo Aggregate (collection) signal types:
bit_vector: array of bits representing binary numbers
: signed: array of bits representing signed binary numbers
= Examples:
O D: in bit_vector(0 to 7);
O EE: in bit_vector(7 downto 0);

O M: in signed (4 downto 0);
--signed 5 bit_vector binary number
--- page 15 ---
Component description: The individual components can be described using any
modeling style, including behavioral or dataflow, as long as they are defined as a
complete entity-architecture pair.
How it works
Define components: Create separate VHDL files or sections for each component
(e.g., half_adder, XOR_gate). Each component must have its own entity declaration
defining its ports and an architecture to describe its function.
Instantiate components: In the main architecture of your higher-level design, declare
the components you will use. This is typically done by creating a component
declaration based on the entity of each sub-module.
Label components: Give each instance of a component a unique label or label. This
is necessary for referring to a specific instance and its ports.
Map ports: Create instances of the components and map their ports to internal signals
or the top-level entity's ports.
Declare signals: Declare internal signal objects that will connect the output ports of one
component to the input ports of another.
Q   b   Build and implement MOD-9 ripple up counter using T flip-flop. Give its Timing   [10
6   .   Diagram.   ]
CO- 4;   Design table with any correct logic & K-MAP (07) + Logical Diagram (02) +waveform (01)
SO-
1;
BL-
3
********** 15 **********
--- page 16 ---
ic i
* pine clock pulses. Ste circuit such that the flip-

h tabu flops are clear after
The truth table of a 4-pj
(a) ie it UP counter is oj
the output of the combinatio, »°r iS given in Table 5.42, where Yis
. n: ie -42,
to 8 and it becomes 0 for count Sate Ttis equal to 1 for the counts 0

Table 5.42 Truth table of 4-bit U

Se Pic i
GiBEE aay B ‘Ounter with output Y
| —____j}__<s |

oO

7 _— Qo ¥
1 0 ° ° is

° 1 1
2 ° 0

1 ° 1
3 to) ° 1 : i
4 to)
: 7 1 ° ° 1

1 to) 1 1

6 ° 1 1 o 1
7 ° 1 1 1 1
8 1 to) i) ° 1
9 1 to) ° 1 °
10 1 ° 1 ° x
11 1 ° 1 1 x
12 1 1 ° ° x
13 1 1 ° 1 x
14 1 1 1 ° x
15 1 1 1 1 x

(b) K-map for Y:

2:20
oo

ol

11

10

FRR ICR 7 6 AC OH
--- page 17 ---
Q   a.   Illustrate BCD to seven segment decoder with the help of block diagram and truth table.   [05
7   Block diagram(2M) +Truth table(3M)   ]
CO-
3;
SO-
1;
BL-
2
********** 17 **********

[Text in pictures on this page, read by OCR]
The logic circuit of Mod-9 asynchronous counter is shown in Fj B58)

Fig. 5.81 Mod-9 nine asynchronous counter

The waveforms of Mod-9 ripple counter are shown in Fig. 5.82,

a—! i LJ | | | N
a H | ; ! ie
Optptti [Ok
oj
PaoPod go fo go gk
f

Flip-flop
; is clear
Fig. 5.82 Waveforms of Mod-9 ripple counter
--- page 18 ---
Q   b Show the implementation of AND & OR logic gates using NAND gates.   [05
7   . AND and OR diagram using NAND gates with expression at output of each gate(2+3marks)   ]
CO-
2;
SO-
1;
BL-
2
AND gate using NAND
OR gate using NAND
Q   c. Explain the need of Master–Slave JK Flip-Flop. Illustrate the same with a logic diagram [05
7   and truth table.   ]
********** 18 **********

[Text in pictures on this page, read by OCR]
BCD to seven segment decoder is a circuit used to convert the input BCD into a form
suitable for the display. It has four input lines (A, B, C and D) and 7 output lines (a, b, ¢, d, e,
f and g) as shown in Figure 3. Considering common cathode type of arrangement, the truth

table for the decoder can be given as in Table I.

> a
A——> [-———> b
B BCD-to-Seven ->———>¢

BCD ——> segment .}+———>d Output lines
Input lines c decoder |» e
+> f
D—— +> 9

Figure 3 BCD-to-Seven segment decoder

Table I Truth table for common cathode type BCD to seven segment decoder

[Decimal | Input lines Output lines Display
Digit [A] B)]Cc]D]a|b|c|d]e] tf] gj Pattern

0 fO;O;Osoriryaititysjoy
1 0;0;/0;1470/1/1)/0)0/0;0 !

S (ee here eae etl

This table indicates the segments which are to be driven high to obtain certain decimal digit
at the output of the seven segment dis} . However, it is to be noted that in the case of
common anode type, the only change will be to interchange ones and zeros on the table. This
means that from the truth table so obtained one can get to know where low has to be driven

so as to obtain the required digit at the output.
--- page 19 ---
CO-   Need (1M)– It should cover avoid of race around condition
4;
SO-   Logic diagram using two JK F/F (2M)
1;
BL-   Truth table(2M)- Same as Negative edge trigger JK Flip flop
2
Q   d Solve (25)10 – (34)10 using 2’s complement method and show the final result in decimal [05
7   .   form.   ]
CO-   Binary equivalent of 25 is 011001
1;
SO-   Binary equivalent of 34 is 100010   [1M]
1;   To subtract 34 from 25 using 2’s complement, take 2’s complement of 34 and
BL-
3   add to 25.
1’s complement of 34 = 011101
+   1
2’s complement of 34 = 011110   [1M]
25  011001
2’s complement of 34  + 011110
110111   [1M]
No carry generated so Ans is -ve and in 2’s complement form
1’s complement of result = 001000
+   1
001001   [1M]
Ans is -9   [1M]
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 77719594cc05

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/BTech_IT_7001/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: text (15 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (IT)/MBA Tech (IT)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Convert decimal number 175 in   [05]
SO-1;
BL-2   (i) Binary, (ii) Octal, and (iii) Hexadecimal number systems. Show all necessary steps of
conversion.
Solution:-
i.   Conversion in to Binary
Division Quotient   Reminder
175/2   87   1
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1
(175)10 = (10101111)2   --(02 Marks)
ii.   Conversion in to Octal Number
(175)10 = (10101111)2 =(010-101-111) = (257)8
--(1.5Marks)
iii.   Conversion in to Hexadecimal Number
(175)10 = (10101111)2 =(1010-1111) = (AF)16
--(1.5Marks)
********** 1 **********
--- page 2 ---
CO-2;   b. What is SOP and POS form in digital logic? Convert following equation in to canonical   [05]
SO-1;
BL-3   SOP form
𝐹 = A’B+CD’
Solution;-
SOP- Sum of Product Form and POS –Product of Sum form -----(01Marks)
SOP and POS are used for easy circuit implementation, efficient hardware design
and to solve K-map   ----(01 Mark)
F=A’B+CD’ in to canonical SOP form
F= A’B (C+C’) + CD’(A+A’)
= A’BC+A’BC’ + ACD’+A’CD’
= A’BC(D+D’)+A’BC’(D+D’) + ACD’(B+B’)+A’CD’(B+B’)
= A’BCD+A’BCD’+A’BC’D+A’BC’D’ + ABCD’+AB’CD’+A’BCD’+AB’CD’
F = A’BCD+A’BCD’+A’BC’D+A’BC’D’ + ABCD’+AB’CD’
----(03 Mark)
CO-3;   c. What is multiplexer? Implement 4:1 multiplexer and explain it with the help of truth   [05]
SO-1;
BL-1,2   table.
Solution:-
Multiplexer:-
A multiplexer is a combinational circuit that has many data inputs and a single output,
depending on select inputs.   ----(01 Mark)
----(01 Mark)
********** 2 **********
--- page 3 ---
----(02 Mark)
Select Inputs   Output
S1   S0   Y
0   0   D0
0   1   D1
1   0   D2
1   1   D3
----(01 Mark)
CO-4;   d. What is sequential logic? Draw the block diagram of sequential logic circuit and explain   [05]
SO-1;
BL-2   importance of memory element in the same.
Solution:-
Sequential Logic:-
It is a logic whose output depends on both present inputs and past outputs, utilizing memory
elements to store state information. .   ----(01 Mark)
---(02 Mark)
Explain memory element using any flip-flop.   ---(02 Mark)
Q2   a. Perform (125)10 –(200)10 operation using   [10]
CO-1;   a) 1’s complement method
SO-1;
BL-2   b) 2’s complement method
Write and explain all the steps and comment on the final result for each method
Solution:-
a) 1’s complement method
(125)10   --- Binary Number -- ( 1111101)2
(200)10   --- Binary Number -- ( 11001000)2 --1’s Complement— (00110111)
We add ( 1111101)2 + (00110111)2
0   1   1   1   1   1   0   1
0   0   1   1   0   1   1   1
Carry   0   1   1   1   1   1   1   1
1   0   1   1   0   1   0   0
No carry generated so answer is negative but not real
To get real answer take 1’s complement of the answer (01001011) = (-75)
********** 3 **********
--- page 4 ---
---(Answer to each step 01 Mark)
b) 2’s complement method
(125)10   --- Binary Number -- ( 1111101)2
(200)10   --- Binary Number -- ( 11001000)2 --1’s Complement— (00110111) +1=
2’s Complement – (00111000)
We add ( 1111101)2 + (00110111)2
0   1   1   1   1   1   0   1
0   0   1   1   1   0   0   0
Carry   0
1   0   1   1   0   1   0   0
No carry generated so answer is negative but not real
To get real answer take 2’s complement of the answer
(10110100) is (01001011) = (-75)
---(Answer to each step 01 Mark)
Q2   b. Minimize the following equation using K-map and implement same using a)Two   [10]
CO-2;   input logic gates only b) Three input logic gates where ever required
SO-1;
BL-1,3   F(A,B,C,D)= Σπ (1,3,5,9,11,12,13)+d(6,14)
ABCD   A’B’   A’B   AB   AB’
C’D’   1
C’D   1   1   1   1
CD   1   1
CD’   ×   ×
Y=C’D+ B’D+ABC’   ---(04 Mark)
********** 4 **********
--- page 5 ---
---(03+03 Mark)
Q3   a. Explain full subtractor with the help of truth table. Implement the same using 3-variable [10]
CO-3;   K-map and draw logic diagram of the same.
SO-1;
BL-3   Solution:-
A   B   bin   Difference (d)   Borrow
0   0   0   0   0
0   0   1   1   1
0   1   0   1   1
0   1   1   0   1
1   0   0   1   0
1   0   1   0   0
1   1   0   0   0
1   1   1   1   1
---(02 Mark)
Difference (d)=A⊕B⊕bin= A′B′bin+ AB′b′in+ A′Bb′in +ABbin   ---(03 Mark)
********** 5 **********
--- page 6 ---
Borrow,b=A′B′bin+A′Bb′in+A′Bbin+ABbin
---(03 Mark)
---(02 Mark)
Q3   b. Build a JK Flip Flop from the given SR Flip Flop.   [10]
CO-4;
SO-1;
BL-3
Conversion Table-04 Marks
K-Map for S input-02 Marks
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion Table

J-K Inputs Outputs S-R Inputs
ik Qp_ Qp+i |] S R
0 0 0 0 0 x
0 0 1 1 x te]
0 1 i) 0 0 x
0 1 1 0 0 1
1 0 0 1 1 0
1 it) 1 1 x i)
1 1 0 4 5 0
1 1 1 0 0 1
< oo om it 10
0 1 3
0 i) x oO i}
5 7
x ie) i
S =3Q

K-Map

Logic Diagram

Ss Qe
j
c
Ky
R Qp-}
K
ae 10
1 3 2
x 0 [+ x
5 7 6
0 0 1 0

R = KQp
--- page 7 ---
K-Map for R input-02 Marks
Conversion Diagram-02Marks
Q4   a. What is universal gate? What are the different types of universal gates? Implement   [10]
CO-2;   following using
SO-1;
BL-3   a)   (A+B) using all types of universal gates
b)   (A.B) using all types of universal gates
Solution:-
Universal gates are logic gates—specifically NAND and NOR—that can implement any
boolean function or construct any other logic gate (AND, OR, NOT, XOR, XNOR)
without needing other gate types.   ---(02 Mark)
(A+B) using NAND and NOR   ---(02 Mark each)
(A.B) using NAND and NOR
Q4   b. What are the features of VHDL and develop VHDL code for implementing a half-adder   [10]
CO-5;   circuit.
SO-1;
BL-2,3
Solution:-
Modeling in VHDL means the way we describe and represent a digital circuit using VHDL
code.
In simple words, it is the method of writing code to define how a circuit behaves or is
structured
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
********** 7 **********
--- page 8 ---
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used in
this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing a
computer program. The standard high-level programming language constructs (like C,
BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table of
design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0); begin
P1: process (bcd, S) begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case; led
<= S;
end process P1;
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is begin
********** 8 **********
--- page 9 ---
X <= a nand b; end
DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q5   a. Design 16:1 Multiplexer using 8:1 multiplexers. Explain all the steps properly. Also   [10]
CO-3;   implement following equation using 16:1 multiplexer
SO-1;
BL-3   F(A, B, C, D) = m (2,3,4, 5, 8,9 ,12)
Solution:-
To design 16:1 multiplexer using 8:1 multiplexers we need 2, 8:1 multiplexer and the
diagram is as shown in the following figure   ---(02+4.5 Mark)
F(A, B, C, D) = m (2,3,4, 5, 8,9 ,12)   ---(4.5 Mark)
********** 9 **********
--- page 10 ---
Q5   b. What is shift register? What are the different types of shift register? Explain any one with [10]
CO-4;   the help of 4 bit shift register.
SO-1;
BL-1,2   Solution:-
Shift registers are sequential logic circuits composed of cascaded flip-flops
that store and move binary data (bits) sideways, one bit at a time, triggered
by a clock signal.   ---(02 Mark)
Types of Shift register
•   Serial in Serial out (SISO) Shift Register
•   Serial in parallel out (SIPO) Shift Register
•   Parallel in Serial out (PISO) Shift Register
•   Parallel in Parallel out (PIPO) Shift Register   ---(02 Mark)
Serial in Serial out (SISO) Shift Register
Serial in parallel out (SIPO) Shift Register
Parallel in Parallel out (PIPO) Shift Register
********** 10 **********

[Text in pictures on this page, read by OCR]
1 1

oO o
°
Serial Input 1 ° 1 5
D Q D Q D Q Serial
Output
Flip Flop 1 Flip Flop 2 Flip Flop 3 Flip Flop 4

Clock

Parallel Output

Serial Input tT
D Q

beatae

D Q

Flip Flop 1 Flip Flop 2 Flip Flop 3 Flip Flop 4

Clock

Clear

Lie oh -fo oh -Jo che 0

Flip Flop 1 Flip Flop 2 Flip Flop 3 Flip Flop 4

Clock

ee ee

Parallel Output
--- page 11 ---
Parallel in Serial out (PISO) Shift Register
Q6   a. What are the important features of VHDL and develop VHDL code for implementing a   [10]
CO-5;   half-Subtractor circuit.
SO-1;
BL-1,2
Solution:
circuit.
The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_subtractor is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
Difference : out STD_LOGIC;
Borrow : out STD_LOGIC);
end half_subtractor;
architecture Behavioral of half_subtractor is
begin
Difference <= a xor b;
Borrow <= (not a) and b;
end Behavioral;
Q6   b. Design a n d implement MOD-6 Asynchronous up counter using T flip-flop. Explain   [10]
CO-4;   the sequence with the help of timing diagram.
SO-1;
BL-3   Solution:
********** 11 **********

[Text in pictures on this page, read by OCR]
Parallel input

\ fl
IT i

Flip flop 2 Flip flop 2 Flip flop Flip flop 4

Serial Output

Clock.
--- page 12 ---
To Design MOD-6 Asynchronous counter we needs 3 T flip-flops   ---(01 Mark)
Qc QB   QA Output (Y)
0   0   0   1
0   0   1   1
0   1   0   1
0   1   1   1
1   0   0   1
1   0   1   1
1   1   0   0
1   1   1   0
---(01 Mark)
---(02Marks for K-map-03Marks for diagram )
-   -------03Marks for timing diagram )
********** 12 **********
--- page 13 ---
Q7   a. What is encoder? Implement Decimal to BCD encoder with the help of truth table and   [05]
CO-3;   logic diagram.
SO-1;
BL-2
Solution:-
An encoder in digital logic is a combinational circuit that converts
multiple input lines into a smaller number of output lines (binary code).
The input and output in encoder works on 2n = m   -------01Marks
Decimal   BCD numbers
B3   B2   B1   B0
0   0   0   0   0
1   0   0   0   1
2   0   0   1   0
3   0   0   1   1
4   0   1   0   0
5   0   1   0   1
6   0   1   1   0
7   0   1   1   1
8   1   0   0   0
9   1   0   0   1
-------01Marks
-------01Marks
-------02Marks
********** 13 **********
--- page 14 ---
Q7   b. Explain De-Morgan’s law with the help of truth table. Simplify following equation using   [05]
CO-2;   De-Morgan’s law
SO-1;
BL-2   Y= {[(AB)’. A’]. [(AB)’. B]}’
Solution:
Y= {[(AB)’. A’]. [(AB)’. B]}’
Y= [(AB)’. A’]’ + [(AB)’. B]’
Y= [(AB)’]’+(A’)’ + [(AB)’]’+[ B’]’
Y=AB+A+AB+B
= A(B+1)+B(A+1)
Y= A+B
-------Each step 01Marks
Q7   c. Explain clocked SR flip-flop with the help of truth table. Also explain limitations of SR   [05]
CO-4;   flip-flop.
SO-1;
BL-2
------- 02Marks
------- 02Marks
Limitation of SR Flip-flop:- At S=R=1 condition we get invalid output or
Indeterminate output. To overcome this limitation we use JK-Flipflop. -- 02Marks
********** 14 **********

[Text in pictures on this page, read by OCR]
Q, One

State

No Change (NC)

Reset

Set

Indeterminate

1
0 1)
1 0
Lt} 1
1 1
Qo x
1
0

No Change (NC)
--- page 15 ---
Q7   d. Differentiate weighted and non-weighted code with the help of example - 01 mark each   [05]
CO-1;
SO-1;
BL-3   weighted code   non-weighted code
Each bit position has a fixed weight   No fixed weight assigned to bit positions
Weights are Predefined (e.g., 8, 4, 2, 1)   No positional weights
Used in arithmetic operations   Used in error detection and coding systems
Example is BCD   Gray code, Excess-3 code
Simple to understand   Slightly complex
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper c575c59d7de8

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/MBATech_IT_7041/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: text (15 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (IT)/MBA Tech (IT)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Convert decimal number 175 in   [05]
SO-1;
BL-2   (i) Binary, (ii) Octal, and (iii) Hexadecimal number systems. Show all necessary steps of
conversion.
Solution:-
i.   Conversion in to Binary
Division Quotient   Reminder
175/2   87   1
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1
(175)10 = (10101111)2   --(02 Marks)
ii.   Conversion in to Octal Number
(175)10 = (10101111)2 =(010-101-111) = (257)8
--(1.5Marks)
iii.   Conversion in to Hexadecimal Number
(175)10 = (10101111)2 =(1010-1111) = (AF)16
--(1.5Marks)
********** 1 **********
--- page 2 ---
CO-2;   b. What is SOP and POS form in digital logic? Convert following equation in to canonical   [05]
SO-1;
BL-3   SOP form
𝐹 = A’B+CD’
Solution;-
SOP- Sum of Product Form and POS –Product of Sum form -----(01Marks)
SOP and POS are used for easy circuit implementation, efficient hardware design
and to solve K-map   ----(01 Mark)
F=A’B+CD’ in to canonical SOP form
F= A’B (C+C’) + CD’(A+A’)
= A’BC+A’BC’ + ACD’+A’CD’
= A’BC(D+D’)+A’BC’(D+D’) + ACD’(B+B’)+A’CD’(B+B’)
= A’BCD+A’BCD’+A’BC’D+A’BC’D’ + ABCD’+AB’CD’+A’BCD’+AB’CD’
F = A’BCD+A’BCD’+A’BC’D+A’BC’D’ + ABCD’+AB’CD’
----(03 Mark)
CO-3;   c. What is multiplexer? Implement 4:1 multiplexer and explain it with the help of truth   [05]
SO-1;
BL-1,2   table.
Solution:-
Multiplexer:-
A multiplexer is a combinational circuit that has many data inputs and a single output,
depending on select inputs.   ----(01 Mark)
----(01 Mark)
********** 2 **********
--- page 3 ---
----(02 Mark)
Select Inputs   Output
S1   S0   Y
0   0   D0
0   1   D1
1   0   D2
1   1   D3
----(01 Mark)
CO-4;   d. What is sequential logic? Draw the block diagram of sequential logic circuit and explain   [05]
SO-1;
BL-2   importance of memory element in the same.
Solution:-
Sequential Logic:-
It is a logic whose output depends on both present inputs and past outputs, utilizing memory
elements to store state information. .   ----(01 Mark)
---(02 Mark)
Explain memory element using any flip-flop.   ---(02 Mark)
Q2   a. Perform (125)10 –(200)10 operation using   [10]
CO-1;   a) 1’s complement method
SO-1;
BL-2   b) 2’s complement method
Write and explain all the steps and comment on the final result for each method
Solution:-
a) 1’s complement method
(125)10   --- Binary Number -- ( 1111101)2
(200)10   --- Binary Number -- ( 11001000)2 --1’s Complement— (00110111)
We add ( 1111101)2 + (00110111)2
0   1   1   1   1   1   0   1
0   0   1   1   0   1   1   1
Carry   0   1   1   1   1   1   1   1
1   0   1   1   0   1   0   0
No carry generated so answer is negative but not real
To get real answer take 1’s complement of the answer (01001011) = (-75)
********** 3 **********
--- page 4 ---
---(Answer to each step 01 Mark)
b) 2’s complement method
(125)10   --- Binary Number -- ( 1111101)2
(200)10   --- Binary Number -- ( 11001000)2 --1’s Complement— (00110111) +1=
2’s Complement – (00111000)
We add ( 1111101)2 + (00110111)2
0   1   1   1   1   1   0   1
0   0   1   1   1   0   0   0
Carry   0
1   0   1   1   0   1   0   0
No carry generated so answer is negative but not real
To get real answer take 2’s complement of the answer
(10110100) is (01001011) = (-75)
---(Answer to each step 01 Mark)
Q2   b. Minimize the following equation using K-map and implement same using a)Two   [10]
CO-2;   input logic gates only b) Three input logic gates where ever required
SO-1;
BL-1,3   F(A,B,C,D)= Σπ (1,3,5,9,11,12,13)+d(6,14)
ABCD   A’B’   A’B   AB   AB’
C’D’   1
C’D   1   1   1   1
CD   1   1
CD’   ×   ×
Y=C’D+ B’D+ABC’   ---(04 Mark)
********** 4 **********
--- page 5 ---
---(03+03 Mark)
Q3   a. Explain full subtractor with the help of truth table. Implement the same using 3-variable [10]
CO-3;   K-map and draw logic diagram of the same.
SO-1;
BL-3   Solution:-
A   B   bin   Difference (d)   Borrow
0   0   0   0   0
0   0   1   1   1
0   1   0   1   1
0   1   1   0   1
1   0   0   1   0
1   0   1   0   0
1   1   0   0   0
1   1   1   1   1
---(02 Mark)
Difference (d)=A⊕B⊕bin= A′B′bin+ AB′b′in+ A′Bb′in +ABbin   ---(03 Mark)
********** 5 **********
--- page 6 ---
Borrow,b=A′B′bin+A′Bb′in+A′Bbin+ABbin
---(03 Mark)
---(02 Mark)
Q3   b. Build a JK Flip Flop from the given SR Flip Flop.   [10]
CO-4;
SO-1;
BL-3
Conversion Table-04 Marks
K-Map for S input-02 Marks
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion Table

J-K Inputs Outputs S-R Inputs
ik Qp_ Qp+i |] S R
0 0 0 0 0 x
0 0 1 1 x te]
0 1 i) 0 0 x
0 1 1 0 0 1
1 0 0 1 1 0
1 it) 1 1 x i)
1 1 0 4 5 0
1 1 1 0 0 1
< oo om it 10
0 1 3
0 i) x oO i}
5 7
x ie) i
S =3Q

K-Map

Logic Diagram

Ss Qe
j
c
Ky
R Qp-}
K
ae 10
1 3 2
x 0 [+ x
5 7 6
0 0 1 0

R = KQp
--- page 7 ---
K-Map for R input-02 Marks
Conversion Diagram-02Marks
Q4   a. What is universal gate? What are the different types of universal gates? Implement   [10]
CO-2;   following using
SO-1;
BL-3   a)   (A+B) using all types of universal gates
b)   (A.B) using all types of universal gates
Solution:-
Universal gates are logic gates—specifically NAND and NOR—that can implement any
boolean function or construct any other logic gate (AND, OR, NOT, XOR, XNOR)
without needing other gate types.   ---(02 Mark)
(A+B) using NAND and NOR   ---(02 Mark each)
(A.B) using NAND and NOR
Q4   b. What are the features of VHDL and develop VHDL code for implementing a half-adder   [10]
CO-5;   circuit.
SO-1;
BL-2,3
Solution:-
Modeling in VHDL means the way we describe and represent a digital circuit using VHDL
code.
In simple words, it is the method of writing code to define how a circuit behaves or is
structured
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
********** 7 **********
--- page 8 ---
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used in
this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing a
computer program. The standard high-level programming language constructs (like C,
BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table of
design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0); begin
P1: process (bcd, S) begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case; led
<= S;
end process P1;
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is begin
********** 8 **********
--- page 9 ---
X <= a nand b; end
DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q5   a. Design 16:1 Multiplexer using 8:1 multiplexers. Explain all the steps properly. Also   [10]
CO-3;   implement following equation using 16:1 multiplexer
SO-1;
BL-3   F(A, B, C, D) = m (2,3,4, 5, 8,9 ,12)
Solution:-
To design 16:1 multiplexer using 8:1 multiplexers we need 2, 8:1 multiplexer and the
diagram is as shown in the following figure   ---(02+4.5 Mark)
F(A, B, C, D) = m (2,3,4, 5, 8,9 ,12)   ---(4.5 Mark)
********** 9 **********
--- page 10 ---
Q5   b. What is shift register? What are the different types of shift register? Explain any one with [10]
CO-4;   the help of 4 bit shift register.
SO-1;
BL-1,2   Solution:-
Shift registers are sequential logic circuits composed of cascaded flip-flops
that store and move binary data (bits) sideways, one bit at a time, triggered
by a clock signal.   ---(02 Mark)
Types of Shift register
•   Serial in Serial out (SISO) Shift Register
•   Serial in parallel out (SIPO) Shift Register
•   Parallel in Serial out (PISO) Shift Register
•   Parallel in Parallel out (PIPO) Shift Register   ---(02 Mark)
Serial in Serial out (SISO) Shift Register
Serial in parallel out (SIPO) Shift Register
Parallel in Parallel out (PIPO) Shift Register
********** 10 **********

[Text in pictures on this page, read by OCR]
1 1

oO o
°
Serial Input 1 ° 1 5
D Q D Q D Q Serial
Output
Flip Flop 1 Flip Flop 2 Flip Flop 3 Flip Flop 4

Clock

Parallel Output

Serial Input tT
D Q

beatae

D Q

Flip Flop 1 Flip Flop 2 Flip Flop 3 Flip Flop 4

Clock

Clear

Lie oh -fo oh -Jo che 0

Flip Flop 1 Flip Flop 2 Flip Flop 3 Flip Flop 4

Clock

ee ee

Parallel Output
--- page 11 ---
Parallel in Serial out (PISO) Shift Register
Q6   a. What are the important features of VHDL and develop VHDL code for implementing a   [10]
CO-5;   half-Subtractor circuit.
SO-1;
BL-1,2
Solution:
circuit.
The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_subtractor is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
Difference : out STD_LOGIC;
Borrow : out STD_LOGIC);
end half_subtractor;
architecture Behavioral of half_subtractor is
begin
Difference <= a xor b;
Borrow <= (not a) and b;
end Behavioral;
Q6   b. Design a n d implement MOD-6 Asynchronous up counter using T flip-flop. Explain   [10]
CO-4;   the sequence with the help of timing diagram.
SO-1;
BL-3   Solution:
********** 11 **********

[Text in pictures on this page, read by OCR]
Parallel input

\ fl
IT i

Flip flop 2 Flip flop 2 Flip flop Flip flop 4

Serial Output

Clock.
--- page 12 ---
To Design MOD-6 Asynchronous counter we needs 3 T flip-flops   ---(01 Mark)
Qc QB   QA Output (Y)
0   0   0   1
0   0   1   1
0   1   0   1
0   1   1   1
1   0   0   1
1   0   1   1
1   1   0   0
1   1   1   0
---(01 Mark)
---(02Marks for K-map-03Marks for diagram )
-   -------03Marks for timing diagram )
********** 12 **********
--- page 13 ---
Q7   a. What is encoder? Implement Decimal to BCD encoder with the help of truth table and   [05]
CO-3;   logic diagram.
SO-1;
BL-2
Solution:-
An encoder in digital logic is a combinational circuit that converts
multiple input lines into a smaller number of output lines (binary code).
The input and output in encoder works on 2n = m   -------01Marks
Decimal   BCD numbers
B3   B2   B1   B0
0   0   0   0   0
1   0   0   0   1
2   0   0   1   0
3   0   0   1   1
4   0   1   0   0
5   0   1   0   1
6   0   1   1   0
7   0   1   1   1
8   1   0   0   0
9   1   0   0   1
-------01Marks
-------01Marks
-------02Marks
********** 13 **********
--- page 14 ---
Q7   b. Explain De-Morgan’s law with the help of truth table. Simplify following equation using   [05]
CO-2;   De-Morgan’s law
SO-1;
BL-2   Y= {[(AB)’. A’]. [(AB)’. B]}’
Solution:
Y= {[(AB)’. A’]. [(AB)’. B]}’
Y= [(AB)’. A’]’ + [(AB)’. B]’
Y= [(AB)’]’+(A’)’ + [(AB)’]’+[ B’]’
Y=AB+A+AB+B
= A(B+1)+B(A+1)
Y= A+B
-------Each step 01Marks
Q7   c. Explain clocked SR flip-flop with the help of truth table. Also explain limitations of SR   [05]
CO-4;   flip-flop.
SO-1;
BL-2
------- 02Marks
------- 02Marks
Limitation of SR Flip-flop:- At S=R=1 condition we get invalid output or
Indeterminate output. To overcome this limitation we use JK-Flipflop. -- 02Marks
********** 14 **********

[Text in pictures on this page, read by OCR]
Q, One

State

No Change (NC)

Reset

Set

Indeterminate

1
0 1)
1 0
Lt} 1
1 1
Qo x
1
0

No Change (NC)
--- page 15 ---
Q7   d. Differentiate weighted and non-weighted code with the help of example - 01 mark each   [05]
CO-1;
SO-1;
BL-3   weighted code   non-weighted code
Each bit position has a fixed weight   No fixed weight assigned to bit positions
Weights are Predefined (e.g., 8, 4, 2, 1)   No positional weights
Used in arithmetic operations   Used in error detection and coding systems
Example is BCD   Gray code, Excess-3 code
Simple to understand   Slightly complex
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 7e79274e1144

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_Computer_7002/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 2ac68178b6f0

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CyberSecurity_7010/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 4a131e5273a0

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_EXTC_7006/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 8dfc5c6a26aa

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_IT_7001/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper e51004da3125

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_Mechatronics_7004/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 487c35a322e3

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_Computer_7047/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper dcc04267fb30

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_IT_7041/Digital Logic Design/ANS_Digital Logic Design(702EX0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 6ccb69d96ed5

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/Integrated_Computer_7032/Digital Logic Design/ANS_Digital Logic Design(702EX0C014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper ae0afd404a59

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/Integrated_IT_7037/Digital Logic Design/ANS_Digital Logic Design(702EX0C014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (20 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/B. Tech (MXTC)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 3 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Digital Logic Design
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Translate the decimal number 10953.5 into its equivalent representations in   [05]
SO-1;
BL-2   (i) Octal, (ii) binary, and (iii) hexadecimal number systems. Show all necessary steps
of conversion.
Solution:
Conversion into octal
Divisio   Quotien Remainde
n   t   r
10953/8 1369   1
1369/8   171   1
171/8   21   3
21/8   2   5
2/8   0   2
----------------------------------------- (2 marks)
Multiplicatio   Resul   Integer   Fractional
n   t   Part   Part
0.5×8   4.0   4   0
0×8   0.0   0   0
********** 1 **********
--- page 2 ---
∴(10953.5)10 = (25311.4)8
----------------------------------------- (1 mark)
Conversion into binary
∴(10953.5)10 = (25311.4)8 = (010 101 011 001 001.100)2
----------------------------------------- (1 mark)
Conversion into hexadecimal
∴(10953.5)10 = (25311.4)8 = (0010 1010 1100 1001.1000)2 = (2𝐴𝐶9.8)16
----------------------------------------- (1 mark)
CO-2;   b. Solve the following using Boolean algebra and implement using logic gates.   [05]
SO-1;
BL-3   𝐹= 𝐴𝐵𝐶+ 𝐴′𝐵′𝐶+ 𝐴′𝐵𝐶+ 𝐴𝐵𝐶′ + 𝐴′𝐵′𝐶′
Simplification with Boolean laws mention at required steps(3 Marks) +
Implementation (2 Marks)
Circuit diagram:
CO-3;   c. Label and draw the circuit diagram of a 1:4 De-Multiplexer, write its truth table.   [05]
SO-1;
BL-1,2   Ans:
Circuit diagram of 1:4 demultiplexer (3 Marks) and Truth table(2Marks)
********** 2 **********

[Text in pictures on this page, read by OCR]
by) Fo ABC + AIBC + ABC 4 ABC!+a)R)c)

E F AR + Axel + ae |

= ARCCcH+e!) + Aa’Ctcl) +Alac
= AB yA\e)+aAlac
=Ae+A)C8\4eC)

= Agta” ‘CB) ye)

By OR laws P+P’=1 and Distributive laws P+QR=(P+Q). (P+R). Mention laws applied at each
--- page 3 ---
De-Multiplexer is a combinational circuit that performs the reverse operation of
Multiplexer. It has single input, ‘n’ selection lines and maximum of 2n outputs. The
input will be connected to one of these outputs based on the values of selection lines.
Since there are ‘n’ selection lines, there will be 2n possible combinations of zeros and
ones. So, each combination can select only one output. De-Multiplexer is also called
De-Mux.
1x4 De-Multiplexer
1x4 De-Multiplexer has one input I, two selection lines, s1 & s0 and four outputs Y3,
Y2, Y1 &Y0. The block diagram of 1x4 De-Multiplexer is shown in the following
figure.
The single input ‘I’ will be connected to one of the four outputs, Y3 to Y0 based
on the values of selection lines s1 & s0. The Truth table of 1x4 De-
Multiplexer is shown below.
********** 3 **********

[Text in pictures on this page, read by OCR]
Selection Inputs

S So Ys Yo
0 0 0 0
0 1 0 0
1 0 0 |
1 1 | 0

From the above Truth table, we can directly write the Boolean functions for each output as

Y3 = 81891
Yo = 8189'I
Y; = 81! s9I

Yo = 81'89'I

Outputs
--- page 4 ---
CO-4;   d. Compare synchronous counter and ripple counter.   [05]
SO-1;
BL-2   (Any five valid point- 5 Marks)
Points Synchronous Counter   Asynchronous Counter
In case of Synchronous   In case of Asynchronous
Trigge   Counters, all the constituent   Counters, there is triggering
r   flip-flops are triggered with   of different flip-flops with
same clock simultaneously.   different clock.
Operation speed of a   The operation speed of an
Operat
synchronous counter is faster   asynchronous counter is
ion
as compared to that of an   comparatively slower than a
Speed
asynchronous counter.   synchronous counter.
Synchronous Counters are less   Asynchronous Counters are
error-prone; they hardly   more error-prone and
Error
produce any decoding errors   produce decoding errors in
Prone
because each flip-flop is   the system.
individually clocked.
All the flip-flops in a   In an asynchronous counter,
synchronous counter coordinate the output of one flip-flop
Compl   with the clock, hence its design   acts as the input of the next
exity   and implementation is complex   flip-flop, hence its design
as compared to that of an   and implementation is quite
asynchronous counter.   simple.
********** 4 **********

[Text in pictures on this page, read by OCR]
We can implement these Boolean functions using Inverters & 3-input AND gates. The circuit diagram of 1x4 De-Multiplexer is
shown in the following figure.

I

St

So I Y3
Y2
V4
--- page 5 ---
A Synchronous counter can be   An Asynchronous counter
operated in any desired count   can operate only in a fixed
Seque
sequence, as it could get   count sequence, i.e., UP and
nce
manipulated by changing the   DOWN.
clock sequence.
There is no propagation delay   In case of asynchronous
observed in case of   counters, there is a
Delay   Synchronous Counters.   subsequent propagation
delay from one flip-flop to
another.
Q2   a. Compare and contrast BCD, Gray, and Excess-3 codes based on the following [10]
CO-1;   parameters:
SO-1;
BL-2   1.   Type of code (weighted/non-weighted)
2.   Range and bit representation
3.   Error detection capability
4.   Ease of arithmetic operations
5.   Applications in digital electronics.
Explain the conversion process of Gray to Binary with circuit diagram and logical
expressions and Translate the given Gray code (110101) into its equivalent Binary
code.
Comparision(5M):
Parameter   BCD (Binary Coded   Gray Code   Excess-3 Code
Decimal)
1. Type of   Weighted code (weights   Non-weighted code   Non-weighted code
Code   8, 4, 2, 1)
2. Range and   Each decimal digit (0–9)   Represents binary   Each decimal digit (0–
Bit   is represented by a 4-bit   numbers so that only   9) represented by
Representation   binary number (0000–   one bit changes   binary of (digit + 3),
1001).   between successive   i.e., 0011–1100 (4
values.   bits).
3. Error   Can detect certain invalid   Excellent for error   Has no direct error
Detection   combinations (e.g., 1010–   minimization in   detection ability, but
Capability   1111 unused). Limited   transitions (only one   avoids 0000 and 1111
error detection.   bit changes,   (used as invalid
reducing transition   codes).
errors).
4. Ease of   Arithmetic operations   Not suitable for   Arithmetic not
Arithmetic   (addition/subtraction) are   arithmetic; primarily   simple, since it’s a
Operations   complex, need correction   used for error-free   self-complementary
(e.g., +6 in BCD   data transmission   code (useful for
addition).   or shaft encoders.   complement
operations).
5. Applications   Used in digital displays,   Used in rotary   Used in self-
calculators, digital   encoders, analog-   complementing
clocks, and financial   to-digital   systems, decimal
systems where decimal   converters (ADCs),   arithmetic units, and
digits are handled.   error correction in   digital displays to
communication.   simplify 9’s
complement
operations.
********** 5 **********
--- page 6 ---
Gray to Binary Code: (5M)
Circuit Diagram with process (Any other valid correct logic circuit) (3M) :
logical expressions: (1M)
B3 = G3
Conversion and correct answer (1M):
********** 6 **********

[Text in pictures on this page, read by OCR]
Conversion from gray code to binary
Conversion of a Gray code into its binary form involves the reverse of the procedure given
above:
(i) The first binary bit (MSB) is the same as that of the first Gray code bit.
(ii) Ifthe second Gray bit is 0, the second binary bit is the same as that of the first binary;
if the second Gray bit is 1, the second binary bit is the inverse of its first binary bit.
(iii) Step 2 is repeated for each successive bit.
--- page 7 ---
Ans: 10011
Q2   b. Define Minterm and Maxterm with one example each.   [10]
CO-2;   Construct the canonical form of the following Boolean function using logic gates:
SO-1;
BL-1,3   Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
Minterm(01 Marks) and Maxterm(01 Marks)
Translate the following Boolean equation into its canonical form-(05 Marks)
Circuit using Logic gates AND- OR arrays (03 Marks)
Minterm:
Maxterm:
Canonical form: correct answer:
Y = 𝐴𝐵+ 𝐴𝐶̅ + 𝐵𝐶
********** 7 **********

[Text in pictures on this page, read by OCR]
Convert the Gray code 110101 to binary form.
Solution:
Step 1 Write the first binary bit 1 which is the MSB of the Gray code.

1 101 0 1. Gray
+

1 Binary

Step 2 The second bit of the Gray code is | and therefore the second bit of the binary is
0, i.e. inverse of the first binary bit “1”.

1 1 0 1 0 1 Gray
v
1 > 0 Binary

Step 3 The third bit of the Gray code is 0 and therefore the third bit of the binary is same
as that of the second binary bit, i.c.0 .

11 0 1 0 1. Gray
7

1075 0 Binary
--- page 8 ---
Q3   a. Design and explain full adder circuit using logic gates.
CO-3;
SO-1;   Definition of full adder with block diagram(01Marks)
BL-3   Truth table (02 Marks) & K-map solving with final expression (04 Marks)
Any Valid Circuit diagram & working (03 Marks)
A full adder adds binary numbers and accounts for values carried in as well as out. A one-bit
full adder adds three one-bit numbers, often written as A, B, and Cin; A and B are the operands,
and Cin is a bit carried in from the next less significant stage. The full-adder is usually a component   [10]
in a
A   B   Cin   Sum   Carry
0   0   0   0   0
0   0   1   1   0
0   1   0   1   0
0   1   1   0   1
1   0   0   1   0
1   0   1   0   1
1   1   0   0   1
1   1   1   1   1
cascade of adders, which add 8, 16, 32, etc. bit wide binary numbers. The circuit produces a two-bit
output, output carry and sum typically represented by the signals Cout and S
********** 8 **********
--- page 9 ---
Q3   b. Build a T Flip Flop from the given SR Flip Flop.   [10]
CO-4;   Write the Conversion Logic and design table details - (Marks 5)
SO-1; BL-3   Make K Map for getting input equation of SR flip flop - (Marks 3)
Logic diagram of Conversion of Flip Flop - (Marks 2)
********** 9 **********

[Text in pictures on this page, read by OCR]
© otep-i: ring the characteristics table of required tip-top and the excitation tabte of the existing (given) Tup-rop.
¢ Step-2: Find the expression of given flip-flop in terms of required flip-flop using K-map.
¢ Step-3: Find the circuit diagram of required flip-flop.

S-R Flip-Flop to T Flip-Flop: Following is the characteristics table of T flip-flop and excitation table of S-R flip-flop.
Excitation Table

Characteristic Table

Now, using K-map we get the expression for of S & R in terms of T.
--- page 10 ---
Q4   a. Solve the following expression using k-map & realize final expression   [10]
CO-2;   i) using Basic gates   ii) using NAND gates only
SO-1;
BL-3   Y = f(A,B,C,D) = m (1,3,4,5,7,9,11,13,15)
K-Map entry (02 Marks) and correct Grouping with expression (04 Marks) + circuit
implementation using Basic gates (02 Marks) and using NAND gates only (02 Marks)
F(A,B,C,D) = ∑ m(1,3,4,5,7,9,11,13,15)
00   01   11   10
00   0   1   0   0
01   1   1   1   1
10   1   1   1   1
11   0   0   0   0
Y=A’BC’+D
i) using Basic gates
********** 10 **********

[Text in pictures on this page, read by OCR]
Now, using K-map we get the expression for of S & R in terms of T.

S = TQn' & R = TQn Therefore, the circuit diagram for conversion of S-R flip-flop into T flip-flop is:

CLK
--- page 11 ---
Similar ii) using NAND gates: AND-OR array in above circuit can be replaced with NAND-
NAND array
Q4   b. Outline the features of VHDL and develop VHDL code for implementing a half-adder [10]
CO-5;   circuit.
SO-1;
BL-2,3   The features of VHDL any 4 valid point (02 Marks)
half Adder block diagram with output expression (02 Marks)
Final code with any correct logic(06 Marks)
The features of VHDL(02 Marks):
* Support for concurrent statements
- in actual digital systems all elements of the system are active simultaneously and
perform their tasks   simultaneously.
* Library support
- user defined and system predefined primitives
reside in a library system
* Sequential statements
- gives software-like sequential control (e.g. case,
if-then-else, loop)
* Technology independent
Final code:
Code:
Entity half_adder is
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end half_adder;
architecture Behavioral of half_adder is
begin
s <= a xor b;
c <= a and b;
end Behavioral;
TEST BENCH CODE:
library IEEE;
********** 11 **********
--- page 12 ---
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;
entity half_adder_tb is
end;
architecture bench of half_adder_tb is
component half_adder
Port ( a : in STD_LOGIC;
b : in STD_LOGIC;
s : out STD_LOGIC;
c : out STD_LOGIC);
end component;
signal a: STD_LOGIC :='0';
signal b: STD_LOGIC :='0';
signal s: STD_LOGIC;
signal c: STD_LOGIC;
begin
uut: half_adder port map ( a => a,
b => b,
s => s,
c => c );
stimulus1: process
begin
a <= not a;
wait for 10 ns;
end process;
stimulus2: process
begin
b <= not b;
wait for 20 ns;
end process;
end;
Q5   a. Build the given function using a single 8:1 multiplexer.   [10]
CO-3;   F(A, B, C, D) = m (0, 1, 3, 4, 8, 9,15)
SO-1;
BL-3   Any valid method –MSB method or LSB method
Design table (05 Marks) and Circuit diagram (05 Marks)
********** 12 **********
--- page 13 ---
Q5   b. Label and explain the operation of a 4 bit Bi-Directional Shift Register with suitable [10]
CO-4;   circuit diagram.
SO-1;
BL-1,2   Marks:
4 bit Bi-Directional Shift Register Diagram: 5 marks
Operation : 5 marks
********** 13 **********

[Text in pictures on this page, read by OCR]
e@ If a binary number is shifted left by one position then it is equivalent to multiplying the
original number by 2. Similarly if a binary number is shifted right by one position then it
is equivalent to dividing the original number by 2.

@ Hence if we want to use the shift register to multiply and divide the given binary number,
then we should be able to move the data in either left or right direction.

@ Such a register is called bi-directional register. A four bit bi-directional shift register is
shown in fig.

@ There are two serial inputs namely the serial right shift data input DR, and the serial left
shift data input DL along with a mode select input (M).

Block Diagram

Mode control (M)

Operation

S.N. Condition Operation

If M = 1, then the AND gates 1, 3, 5 and 7 are
enabled whereas the remaining AND gates 2,
4, 6 and 8 will be disabled.

1 With M = 1 — Shift right operation The data at Dp is shifted to right bit by bit
from FF-3 to FF-0 on the application of clock
pulses. Thus with M = 1 we get the serial right
shift operation.

When the mode control M is connected to 0
then the AND gates 2, 4, 6 and 8 are enabled
while 1, 3, 5 and 7 are disabled.

2 With M = 0 - Shift left operation The data at Dy, is shifted left bit by bit from FF-
0 to FF-3 on the application of clock pulses.
Thus with M = 0 we get the serial right shift
operation.
--- page 14 ---
Q6   a.   List different modelling types in VHDL and explain any two with appropriate [10]
CO-5;   examples.
SO-1;
BL-1,2   2 Marks: for listing the 4 types of modelling
8 Marks: 4 marks each for the description with example
There are 4 types of modeling styles in VHDL:
 1. Data flow modeling (Design Equations)
 Data flow modeling can be described based on the Boolean expression. It
shows how the data flows from input to output. It works on Concurrent
execution.
 2. Behavioral modeling (Explains Behaviour)
 Behavioral modeling is used to execute statements sequentially. It shows
that how the system performs according to the current statement.
 Behavioral modeling may contain Process statements, Sequential
statements, Signal assignment statements, and wait statements.
 3. Structural modeling (Connection of sub modules)
 Structural modeling is used to specify the functionality and structure of the
circuit.
 Structural modeling contain signal declarations, component instances, and
port maps in component instance.
 4. Hybrid/Mixed style modeling
 The mixed style modeling is any combination of behavior, data flow, and
structural modeling in a single architecture body. In mixed style of modeling
we could use component instantiation statements, concurrent signal
assignment statements, sequential signal assignment statement.
Example:
Behavioral modeling (Explains Behaviour)
In behavioral modeling sequential execution statements are used. The statements used
in this modeling style are allowed only inside PROCESSES, FUNCTIONS, or
PROCEDURES. Describing a circuit at the behavioral level is very similar to writing
a computer program. The standard high-level programming language constructs (like
C, BASIC), such as the FOR LOOP, WHILE LOOP, IF THEN ELSE, CASE, and
variable assignments are included here.
The statements are enclosed in a PROCESS block, and are executed sequentially.
When creating a behavioral description of a circuit, circuit is described in terms of its
operation over time.
In behavioral modeling we must require the behavior of design or simply truth table
of design. No need of logical circuit diagram.
architecture behavioral of Decoder is
signal S: bit_vector (3 downto 0);
begin
P1: process (bcd, S)
begin
case bcd is
when "00" => S <= "0001"
when "01" => S <= "0010"
when "10" => S <= "0100"
when "11" => S <= "1000"
end case;
led <= S;
end process P1;
********** 14 **********
--- page 15 ---
end behavioral;
Data Flow Modeling :
The view of data as flowing through a design, from input to output. A dataflow model
specifies the functionality of the entity without explicitly specifying its structure. This
functionality shows the flow of information through the entity, which is expressed
primarily using concurrent signal assignment statements and block statements. VHDL
code is inherently concurrent (parallel). Concurrent code is also called dataflow code.
Example Two input NAND gate
architecture DATAFLOW of NAND2 is
begin
X <= a nand b;
end DATAFLOW;
In above NAND gate code is described using single concurrent signal assignment
statement. A signal assignment is identified by the symbol " <=".
Q6   b. Build and implement MOD-6 ripple up counter using T flip-flop. Give its Timing [10]
CO-4;   Diagram.
SO-1;
BL-3   3 Marks: State Diagram and Mod 6 Ripple counter mean.
3 Marks: Truth Table and realization
3 Marks: Circuit
1Marks: Timing Diagram –Show after count 0 to 5 output restart at 000.
********** 15 **********
--- page 16 ---
Q7   a.   Classify different encoders and explain the basic concept of 4-to-2 priority encoder [05]
CO-3;   with the help of symbol, truth table.
SO-1;
BL-2   Types of Encoder(1M)
Priority encoder symbol/block diagram with concept(2M) and truth table(2M)
********** 16 **********

[Text in pictures on this page, read by OCR]
Truth Table

CLK Pulses| Qa | Qp | Qc
Number A B C

0 0 | 0] 0
| 0}; oj} |
2 0 1 | 0
3 0 l |
4 l 0} 0
5 l 0} |
6 | \ 0

To decode the count 6, i.e. 110 we sie
AND gate. The output of the AND gate
flip-flops. The circuit diagram is shown

nect the outputs of flip-flops A and B to, one:
may be connected to the reset input of all the
in figure 9.13(a).

Cc

A(MSD)
Clock 1—fJ | eee
pulse FF Qa Qs
Ip— FF
c B
IK Qa) aK %
RESET [CLR CLR
--- page 17 ---
Q7   b. Explain any one De-Morgan’s Theorem with the help of suitable circuit diagrams and [05]
CO-2;   prove the theorem using truth table.
SO-1;
BL-2
Any one De-Morgan’s Theorem (05 Marks): -
State (01) +Circuit diagram using logic gates (02) + Proof matching truth table
for LHS and RHS of theorem (02)
One Theorem example:
First De Morgan's Law states that when two or more input variables (A, B) are
OR’ed and then negated, the result is equal to the AND of the complements of the
individual input variables. (A+B)’ =A’. B’.
To prove this theorem, we can use the truth table as given below:
INPUTS   OUTPUTS
B   A   A + B   (A+B)’   A’   B’   A’.B’
0   0   0   1   1   1   1
0   1   1   0   0   1   0
1   0   1   0   1   0   0
1   1   1   0   0   0   0
NOR gate is equal to bubbled OR
********** 17 **********

[Text in pictures on this page, read by OCR]
PRIORITY ENCODER:
+ As the name indicates, the priority is given to inputs line.

* Iftwo or more input lines are high at the same time i.e | at the same time,
then the input line with high priority shall be considered.

* Block diagram and Truth table of Priority Encoder are shown in fig.15

Highest Priority

TRUTH TABLE:

Y, INPUTS OUTPUTS Vi
Priority 1) 0 0 0 x x 0
Encoder
0 0 0 t 0 0 1
Yo
0 0 1 x 0 1 1
0 1 x x 1 ) 1
t Priority Output 1 x x x 1 1 1
I
Block Diagram of Priority Fig.15

Encoder
--- page 18 ---
Q7   c. Explain the Race around condition in JK flip-flop and how it can be overcome.   [05]
CO-4;   Draw Race Around condition occur in Sequential logic circuit and how it can be
SO-1;
BL-4   overcome.
1. About Race Around Condition with diagram (Marks 3)
A race around condition occurs in sequential circuits, particularly in a JK flip-
flop when both J and K inputs are high, and the clock pulse is high for an
extended period. The output toggles multiple times within a single clock pulse,
making the final output unstable and uncertain.
Condition: The race around condition happens in a JK flip-flop when both the J and
K inputs are equal to 1 and the clock pulse is active (HIGH) for an extended period.
Mechanism: With J=K=1, the flip-flop is in a toggle state. If the clock pulse stays
high for too long, the output Q will flip from 0 to 1 and then back to 0 multiple times
within that single clock pulse.
Result: The final output of the flip-flop becomes unpredictable and unstable because
it is not clear what the final state will be after the clock pulse ends.
2. Overcome method (Marks 2)
(1) Use a master-slave JK flip-flop:
This configuration consists of two cascaded flip-flops: a master and a slave.
When the clock is HIGH, the master is enabled and the slave is disabled, so it updates
its state but doesn't affect the final output.
********** 18 **********
--- page 19 ---
When the clock goes LOW, the slave is enabled and captures the final, stable output
of the master from the previous clock cycle.
This prevents the output from toggling more than once per clock pulse.
(2) Use an edge-triggered flip-flop:
Edge-triggered flip-flops are sensitive only to the transition (edge) of the clock pulse,
either positive or negative.
This means the flip-flop's output changes only once at the moment the clock edge
occurs, regardless of how long the clock pulse stays high.
This inherent characteristic prevents the output from toggling multiple times within
a single clock pulse, thus eliminating the race around condition.
Q7   d. Solve the subtraction of the decimal numbers 78 – 87 using 1’s complement method [05]
CO-1;   and show the final result in decimal form.
SO-1;
BL-3   Solution:
Conversion of decimal numbers into binary
Divisio   Quotien Remainde
n   t   r
78/2   39   0
39/2   19   1
19/2   9   1
9/2   4   1
4/2   2   0
2/2   1   0
1/2   0   1
∴(78)10 = (1001110)2
Divisio   Quotien Remainde
n   t   r
87/2   43   1
43/2   21   1
21/2   10   1
10/2   5   0
5/2   2   1
2/2   1   0
1/2   0   1
********** 19 **********
--- page 20 ---
∴(87)10 = (1010111)2
𝑀= (1001110)2
𝑁= (1010111)2 --------------------------------- (1 mark)
Subtraction Using 1’s Complement
1’s Complement of N = (0101000)2 ------------ (1 mark)
∴100110 + 0101000 = 1110110 ------------ (1 mark)
Carry is not generated after addition.
1’s complement of sum = 0001001 ------------ (1 mark)
∴𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒= −(0001001)2 = −(9)10 ------------ (1 mark)
********** 20 **********
````
