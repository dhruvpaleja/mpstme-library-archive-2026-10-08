# Digital Circuits and Computer Architecture: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 55a396458934

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CS_7055/Digital Circuits and Computer Architecture/ANS_Digital Circuits and Computer Architecture(702CS0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: mixed (12 pages), mean OCR confidence 57.1
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Digital Circuits and Computer Architecture
Date: 28 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Discuss the importance of Universal Gates and explain with the help
SO- 1;
of logic diagrams.
BL-1
Ans. 1 mark for importance
1 mark for AND using NAND and NOR
1 mark for OR using NAND and NOR
1 mark for NOT using NAND and NOR
1 mark for XOR using NAND and NOR
CO- 2;   b.   Write the difference between Combinational Logic and Sequential
SO-1;
Logic Circuit.
BL-2
Ans   1 mark for each point
********** 1 **********
--- page 2 ---
CO- 3;   c.   Draw and describe the block diagram of the Von Neumann
SO- 3;
architecture, explaining the data flow during program execution.
BL-3
ANS Diagram – 2 marks
Explanation of each block is 4 marks
explaining the data flow during program execution. ( 4 marks )
with the examples ADD R1, LOCA
CO-4;   d.   Explain the basic elements of cache memory with a neat block
SO-2;
diagram.
BL-4
Ans
Each point for 1 mark
********** 2 **********
--- page 3 ---
a.   Apply the Karnaugh map method to minimize the given Boolean
function. Explain each step and illustrate the simplified circuit with a
[10]
logic diagram.
f (A, B, C, D, E) = ∑m (1,4,8,10,11,20,22,24,25,26) + ∑d (0,12,16,17)
Ans.   for plotting of k-map – 2 marks
for grouping of k-map -2 marks
for logic expression -2 marks
for steps -2 marks
for logic diagram – 2 marks
Q2
CO-2;
SO-1;
BL-3,4
b.   Design a 3-bit synchronous down counter. Analyze and justify each
[10]
step of your design process, including the choice of flip-flops,
********** 3 **********
--- page 4 ---
excitation table, state transition diagram, waveform and logic
equations. Draw the complete circuit diagram for your design.
Ans.   State Diagram (2 marks)
Logic Diagram (4 marks)
Waveform (3 marks)
a.   Explain the concept of shift registers and their main operations.
Q3
Describe how data is loaded and shifted out in a PISO shift register [10]
CO-
2,3;   with the help of diagram.
SO-6;   Ans
BL-3,4   main operations (5 marks)
********** 4 **********
--- page 5 ---
PISO shift register (5 marks)
b.   List and explain list of registers used in Von Numaan Architecture,
Analyze the complete execution of the instruction ADD R1, LOCA
stored at memory location 1000.
[10]
Given that the initial value of R1 = 50 and LOCA = 5000, explain how
the instruction is fetched, decoded, and executed using the sequence
of micro-operations.
Ans.
• Memory Buffer Register (MBR):- Contains a word to
be stored in memory or sent to I/O unit, or is used to
receive a word from memory or from the I/O unit.
• Memory Address Register (MAR):- Specifies the
address in memory of the word to be written from or
read into the MBR.
•   Instruction Register (IR):- Content the 8-bit opcode
instruction being executed.
********** 5 **********
--- page 6 ---
•   Instruction Buffer Register (IBR):- Employed to hold
temporarily the right hand instruction from a word in
memory.
• Program Counter (PC):- Contains the address of the
next instruction-pair to be fetched from memory.
• Accumulator   (AC)   ,   Multiplier   Quotient
(MQ) :Employed to hold temporarily operands and
results of ALU operations.
a.   Apply Booth’s Algorithm to perform signed multiplication for (8 × –
Q4
5). Draw and explain the complete flowchart showing each step of the [10]
CO-3;
algorithm.
SO-2;
BL-3,4 Ans.
********** 6 **********
--- page 7 ---
Step   A   Q   Q₋₁ (Q₀, Operation   After
(before) (before)   Q₋₁) (A ← …) Arithmetic
Right
Shift (A Q
Q₋₁)
Initial   0000   1011   0 —   Initialize   —
Step   0000   1011   0   (1,0) A = A –   1100 0101,
1   M = 0000   Q₋₁ = 1
– 1000 =
1000
Step   1100   0101   1   (1,1)   No   1110 0010,
2   operation   Q₋₁ = 1
Step   1110   0010   1   (0,1) A = A +   0011 0001,
3   M = 1110   Q₋₁ = 0
+ 1000 =
0110
Step   0011   0001   0   (1,0) A = A –   1101 1000,
4   M =   Q₋₁ = 1
0011 –
1000 =
1011
********** 7 **********
--- page 8 ---
b.   Analyze and differentiate various addressing modes used in a
processor. Explain the working of each addressing mode with suitable
[10]
diagrams and examples, and justify their significance in efficient
instruction execution.
Ans. 1 mark for each addressing and diagram
a. Direct addressing mode
b. Register indirect addressing mode
c. Based addressing mode
d. Indexed addressing mode
e. Based indexed addressing mode
f. String addressing mode.
a.   Identify and explain the major components of a processor, and apply
your understanding to compare and contrast the characteristics of [10]
RISC and CISC architectures.
Ans. Major components 5 marks
Q5
CO-
3,4;
SO-1;
BL-3,4
RISC and CISC architectures. (5 marks)
********** 8 **********
--- page 9 ---
b.   Explain the working principle of an SR flip-flop. Describe the
importance of cache memory and distinguish between different cache [10]
memory mapping techniques.
Ans. For SR 3 marks
Cache memory Importance – 4 marks
Mapping – 3 marks
a.   Explain the difference between Static RAM (SRAM) and Dynamic
RAM (DRAM). Further, consider an 8-way set associative cache
consisting of 512 lines with a line size of 16 words. The CPU generates [10]
a 28-bit address of a word in main memory. Determine the number of
bits in the TAG, SET, and WORD fields respectively.
Ans.   Difference 5 marks
Great — step-by-step:
Q6   • Line size = 16 words → WORD (block offset) bits =
CO-4;   log⁡2 16 = 4.
SO-3;   •   Total lines = 512 and associativity = 8 → number of sets =
BL-2,3   512/8 = 64→ SET bits = log⁡2 64 = 6.
• TAG bits = total address bits − (SET + WORD) = 28 −(6 +
4) = 18.
Answer: TAG = 18 bits, SET = 6 bits, WORD = 4 bits.
b.   Draw and explain the block diagram of an I/O module and discuss its
importance in a computer system. Further, design a Decimal-to-BCD
[10]
encoder using a suitable block diagram, truth table, and logic
diagram.
********** 9 **********
--- page 10 ---
Ans. Diagram and explanation 5 marks
a.   Analyze and implement the given Boolean function using an 8:1
Q7
multiplexer. Further, define the structure and functions of a
CO-
1,4;   computer, and critically discuss the major functions performed by a   [10]
SO-6;   computer system with the help of a neat and well-labeled diagram.
BL-4,6
f (A, B, C, D) = πM (0,3,5,8,9,1012,14)
********** 10 **********
--- page 11 ---
Ans.
•   Structure : The way in which components relate to each other.
•   Function : The operation of individual components as part of
the structure.
•   All computer functions are:
• Data processing
• Data storage
• Data movement
•   Control
b.   Solve as directed
1. Prove the following Boolean Expression
(A + B) (AC + C) (B + AC) = AB   [10]
2. If AB + CD =0, then prove that
AB + C (A +D )= AB + BD + BD + ACD
Ans.   1.
2.
********** 11 **********
--- page 12 ---
Solution:

LHS   =AB+C(A+D)+0
= AB+C(A+D)+AB-+CD (given that AB-+CD = 0)
= AB+AC+CD+AB+CD
= B(A+.A)+D(C+C)+AC
=B+D+AC

RHS   =AB+BD+BD+4+ACD+0
= AB+BD+BD+ACD+AB+CD (given that AB+CD =0)
= B(A+ 4)+BD+BD+4ACD+CD
= B+D)+BD+4ACD+CD
= B+BD+ACD+CD

= B+D+ACD+CD ( A+ AB = A+B)
=B+DQ+C)+ACD

= B+D+DAC

=B+D+AC ( A+AB=A+B)

Hence, L.H.S = R.H.S

FRR ICR] DA KH
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 10c4f30bbb50

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/BTech_CSE_DS_7057/Digital Circuits and Computer Architecture/ANS_Digital Circuits and Computer Architecture(702CS0C002)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: mixed (8 pages), mean OCR confidence 51.0
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: Digital Circuits and Computer Architecture
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 8 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Simplify the following Boolean expression,
𝐴+ 𝐵[𝐴𝐶+ (𝐵+ 𝐶̅)𝐷]
CO- 1;   Final Answer
SO- 1;   [5]
BL-1   𝐴+ 𝐵𝐷
b.   What is an encoder? Draw the truth table of 4 lines to the 2-line priority
encoder.
Defination 2 marks
Truth table 3 marks
CO-2;   D3   D2   D1   D0   Y1   Y0   Valid
SO-1;   (V)   [5]
BL-4
0   0   0   0   X   X   0
0   0   0   1   0   0   1
0   0   1   X   0   1   1
0   1   X   X   1   0   1
1   X   X   X   1   1   1
CO- 3;   c.   Discuss the MIPS addressing mode.   [5]
SO- 1;
********** 1 **********
--- page 2 ---
BL-1   Each addressing mode – 1 mark
d.   Explain the instruction format.
CO- 3;   Format – 2 marks
SO- 1   Explanation 3 marks   [5]
BL-1   • Opcode → Specifies the operation (ADD, SUB, LOAD, etc.)
• Operands → Specify data or addresses (registers/memory)
A   Minimize the following boolean function-
F(A, B, C, D) = Σm(0, 1, 2, 5, 7, 8, 9, 10, 13, 15)
Q2
CO-2;   [10]
SO-1;
BL-2
B   Explain the race-around condition observed in J-K flip-flop and describe
the technique to avoid it in practical circuits.
The race-around condition occurs in a J-K flip-flop when both inputs J and
K are HIGH (1) and the clock pulse remains HIGH for a duration longer
than the propagation delay of the flip-flop. In this situation, the output
keeps toggling repeatedly (0 → 1 → 0 → 1 …) as long as the clock is
active. This happens because the output is fed back to the input, causing
the flip-flop to change state continuously within one clock period. As a
result, the final output becomes uncertain or unpredictable, this behaviour
CO-2;   is known as the race-around condition.
SO-1;   [10]
BL-2   Methods to overcome the race-around condition:
1. Reduce the clock pulse width:
Keep the clock pulse less than the propagation delay of the flip-
flop so that only one toggle occurs.
2. Use Edge-Triggered Flip-Flop:
Design the circuit so that the output changes only at the rising or
falling edge of the clock pulse.
3. Use Master-Slave J-K Flip-Flop:
The master-slave configuration uses two flip-flops — the master
responds to the clock’s leading edge, and the slave responds to the
trailing edge.
********** 2 **********
--- page 3 ---
This ensures that the output changes only once per clock cycle,
completely eliminating the race-around problem.
A   Design Full Substractor using NOR gate.
Q3
CO-2;   [10]
SO-2;
BL-4
B   Design a 3-bit down synchronous counter using J-K flip-flop.
CO-2;
SO-2;   [10]
BL-4
********** 3 **********
--- page 4 ---
2 S e) x
° { | K |
\ ° x \
\ rl x 6

FIC 7) IC HOH
--- page 5 ---
A   Design a Full Adder using 8: 1 multiplexer.
Q4
CO- 2;   [10]
SO-2;
BL- 3
CO-3; B
SO-2;   Develop a circuit for the conversion of S-R flip-flop to J-K flip-flop.   [10]
BL-3
********** 5 **********
--- page 6 ---
Jonvesies “) BS-R EL +o s-K FF

J OR | Gal oah os | &

oe | 6 | \ “| ©
©) 4 {© a \
| 6) G | \ °o
{16 ! \ x °
| | oO \ \ o
\ \ | oO ° \

Excitavies Table

Qn Qh a SR

ao ra) °o x

= { | 16)

\ roo) to) \
x @)

FIC 6 I HF
--- page 7 ---
A   Discuss program control instructions including branching, looping, and
conditional execution.
Explanation 2 marks
Each branching with example 2 marks
Q5
Type   Instruction   Purpose
CO-3;   Example   [10]
SO-1;
Unconditional   J LABEL   Direct jump
BL-2
Branch
Conditional Branch   BEQ, BNE   Decision making
Looping   BNE, ADDI   Repetition
Conditional   SLT + BEQ   Logical conditions
Execution
Subroutine Control   JAL, JR   Function calls
B   Explain the memory hierarchy with a neat diagram. Discuss the
CO-3;   characteristics of each level
SO-1;   [10]
BL-1   Diagram 2 marks
Explanation of each memory 2 marks
A   Compare Direct Mapping, Associative Mapping, and Set-Associative
Q6
Mapping in terms of performance, cost, and complexity.   [10]
CO-4;
SO-1;   For each feature 2 marks each
********** 7 **********
--- page 8 ---
BL- 2   Feature   Direct   Associative   Set-Associative
Mapping   Mapping   Mapping
Placement   Fixed line Any line   Any line within a set
Speed   Fastest   Slowest   Moderate
Hit Rate   Lowest   Highest   Medium to High
Miss Type   High   Low conflict Reduced conflict miss
conflict   miss
miss
Hardware   Simple   Complex   Moderately complex
(comparators
)
Cost   Low   High   Medium
Complexity   Very low   Very high   Moderate
Flexibility   Very low   Very high   Medium
B   What are I/O channels and I/O processors? Explain their role in improving
CO-4;
SO-1   system performance.   [10]
BL- 2
explanation
A   Explain the functional units of a computer system with a neat block
Q7
diagram. Discuss the role of each unit in executing a program.
CO-4;   [10]
SO-1;   Explanation 5 marks
BL-1
Role – 5 marks
B   Describe the Booth’s multiplication algorithm with a step-by-step example
CO-3;
SO-1;   Steps 6 marks   [10]
BL-1
Example 4 marks
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper cb1e21e20517

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CS_7055/Digital Circuits and Computer Architecture/ANS_Digital Circuits and Computer Architecture(702CS0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (14 pages), mean OCR confidence 57.9
- 5 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Digital Circuits and Computer Architecture
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   Define all basic logic gates and represent each with its standard logic
SO- 1;
symbol and truth table.
BL-1
Ans. Each logic gate for 1 mark
CO- 1;   b.   Distinguish between Combinational and Sequential Logic Circuits with
SO-1;
suitable examples.
BL-2
Ans. Each difference 1 marks
CO- 3;   c.   Using a sample instruction, demonstrate how operands and operations are
SO- 3;
represented in machine language.
BL-3
********** 1 **********
--- page 2 ---
Ans.
CO-4;   d.   Analyze the concept of memory hierarchy in computer systems. Explain
SO-2;
its structure and significance in improving system performance.
BL-4
Ans.
Each memory explanation 1 marks
a.   Define a Multiplexer and explain its working principle.
Draw the logic diagram of an 8:1 line multiplexer and implement the
[10]
Q2   Boolean function F (A, B, C, D) = ∑m (0,1,2,4,6,9,12) using a 4:1
CO-2;   Multiplexer.
SO-1;
BL-3,4   Ans.   Define – 2marks
Explanation 3 marks
Implementation for 5 marks
********** 2 **********
--- page 3 ---
b.   Explain the Race-Around Condition observed in JK Flip-Flops.
Design a 4-bit Synchronous Up Counter using JK Flip-Flops and   [10]
illustrate its circuit diagram and operation clearly.
Ans. Race-Around Condition – 2 marks 2 marks for waveform
Design -6 makes
Q3   a.   Design a Gray to Binary code convertor by following design steps of
[10]
CO-2,3;   combinational logic design procedure.
SO-6;   Ans. Each step 2 marks
BL-3,4
********** 3 **********
--- page 4 ---
1 i) 0 0 1 1 1 1

K-map simplification ms

ForA ForB
G,Gp G,G,
G,G\_ 00 01 11 10 GG 00 01 11 10

00] o |G)} o FG o] ofo fata)

01} o |G) o olf7 | 1} 0 | o

un} o 1G] 0 fa nf} o}o ia | 1)
= a aes gg 1
101 @)] 0 |@]| o wolf1 | 1}] o} 0

= (G; © G) GG, + G,OG)G,G,
= (G;® G,) Gi BGo) + G3 B G2) (G, ® G,)
= (G;®G,) @ (G,® Gy)
B = (G,G, + G,G)G, + (GG, + G,G,)G,
= (G; OG,)G, + (G, © GG,
= (GyGGz)G; +(G3 ®G2)G,
= G;8G;,8G,

FIC 7) IC HOH
--- page 5 ---
b.   Describe the basic operations performed by Shift Registers with suitable
examples. Explain in detail the execution process performed by the
CPU for the instruction MUL R1, LOCA
[10]
Assume initially R1 = 10h, LOCA = 5000h, and the complete
instruction is stored at memory location 1000h. Illustrate and explain all
the steps involved in instruction execution clearly.
Ans.   basic operations performed by Shift Registers 4 marks
MUL R1, LOCA – 4 marks
Steps – 2 marks
********** 5 **********
--- page 6 ---
a.   Design a Full Adder using the steps of combinational logic design and
derive its logic expression. Discuss the disadvantages of an n-bit
[10]
Parallel Adder and explain how these limitations can be overcome in
digital systems
Ans. Each step of Full Adder 5 marks and n-bit Parallel disadvantages for 5
marks
Q4
CO-3;
SO-2;
BL-3,4
********** 6 **********
--- page 7 ---
b.   Explain the data transfer and manipulation operations performed by the
CPU in detail. Design and describe the sequence of micro-operations
[10]
involved during program control and subroutine call and return
mechanisms with suitable diagrams.
Ans.   1. Data Transfer Operations (3 marks)
Data transfer operations move data between registers, memory, and I/O
devices.
They are executed using register transfer micro-operations such as:
Operation Type Example   Description
********** 7 **********
--- page 8 ---
Register to   R1 ← R2   Copies data between CPU
Register   registers.
Register to   MAR ← R1, MDR   Moves data from register
Memory   ← M[MAR]   to memory.
Memory to   R1 ← M[MAR]   Loads data from memory
Register   to register.
I/O to Register   R1 ← INPORT   Reads data from input
device.
Register to I/O   OUTPORT ← R1   Sends data to output
device.
2. Data Manipulation Operations (3 Marks)
Performed through arithmetic and logical micro-operations:
Type   Examples   Function
Arithme ADD, SUB, INC, DEC,   Perform calculations
tic   MUL, DIV   using ALU.
Logical   AND, OR, XOR, NOT   Perform bitwise
operations.
Shift   SHL, SHR, ROL, ROR   Shift or rotate bits.
Micro-operations Example:
T1: MAR ← PC
T2: MDR ← M[MAR]
T3: IR ← MDR
T4: AC ← AC + R1
3. Program Control Operations (2 marks)
These operations alter the sequence of instruction execution.
Type   Description
Branching (Conditional /   Changes program counter (PC)
Unconditional)   value.
Interrupt Handling   Transfers control to interrupt
service routine.
Subroutine Call and Return   Transfers control to subroutine
and returns back.
4. Sequence of Micro-operations for Program Control(1 marks)
(a) Branch Instruction
1. Decode branch instruction
2. If condition = TRUE → PC ← Branch Address
3. Else → PC ← PC + 1
5. Subroutine Call and Return Mechanism
(a) Subroutine CALL
When the CPU executes a CALL instruction:
********** 8 **********
--- page 9 ---
Step   Micro-Operation   Description
1   MAR ← SP   Load stack pointer.
2   M[SP] ← PC   Save return address on stack.
3   SP ← SP – 1   Decrement stack pointer.
PC ← Subroutine
4   Load subroutine starting address.
Address
(b) Subroutine RETURN
Step   Micro-Operation   Description
1   SP ← SP + 1   Increment stack pointer.
2   PC ← M[SP]   Retrieve return address from stack.
Continue
3   Resume main program.
Execution
6. Diagram: Subroutine Call and Return (1 mark)
a.   Design an Octal to Binary Encoder with the help of a truth table and
Q5   logic diagram. Explain Intel 8086 CISC architectures with neat and   [10]
CO-3,4;   labeled diagrams.
SO-1;
BL-3,4   Ans.   Octal to Binary Encoder (5 marks)
Octal to binary Encoder has 8 input lines one for each octal digit and 3 output
lines that generates the binary code depending on which of the one input
********** 9 **********
--- page 10 ---
line output of 8 input lines is activated. The truth table for octal to binary
encoder is shown in Table 2.10.
Table 2.10: Truth Table For Octal To Binary Encoder
Intel 8086 (5 marks)
********** 10 **********
--- page 11 ---
b.   Explain the working principles of single-level and multi-level cache
memory, focusing on their impact on performance and data access
efficiency. Consider, for a cache with 4 blocks and the following memory
reference sequence:
5, 4, 6, 3, 4, 0, 2, 5, 3, 0, 6, 7, 11, 3, 5   [10]
Calculate the hit ratio for:
1. Direct Mapping using LRU replacement
2. 2-Way Set Associative Mapping using LRU replacement
Ans.   For diagram 3 marks
Explanation 3 marks
Numerical 4 marks (2 marks for each method)
1) Direct Mapping (4 lines). Mapping used: line = address % 4
(Direct-mapped has one slot per line — no replacement decision.)
St Addr Line (= addr %   Hit /   Cache (lines 0..3)
ep   ess   4)   Miss   after access
1   5   1   Miss   [None, 5, None,
None]
2   4   0   Miss   [4, 5, None, None]
3   6   2   Miss   [4, 5, 6, None]
4   3   3   Miss   [4, 5, 6, 3]
5   4   0   Hit   [4, 5, 6, 3]
6   0   0   Miss   [0, 5, 6, 3]
7   2   2   Miss   [0, 5, 2, 3]
8   5   1   Hit   [0, 5, 2, 3]
9   3   3   Hit   [0, 5, 2, 3]
10   0   0   Hit   [0, 5, 2, 3]
11   6   2   Miss   [0, 5, 6, 3]
12   7   3   Miss   [0, 5, 6, 7]
13   11   3   Miss   [0, 5, 6, 11]
14   3   3   Miss   [0, 5, 6, 3]
15   5   1   Hit   [0, 5, 6, 3]
********** 11 **********
--- page 12 ---
Direct-mapped summary: Hits = 5 out of 15 → Hit ratio = 5/15 =
0.3333 (33.33%)
2) 2-Way Set-Associative (4 lines, 2 ways → 2 sets).
• Number of sets = 4 / 2 = 2.
•   Set index = address % 2 (set 0 or set 1).
• Each set holds up to 2 blocks; LRU replacement inside each set.
We show set contents as [MRU, ..., LRU]
St Addr Set (= addr %   Hit /   Set contents after
ep   ess   2)   Miss   access (set0, set1)
1   5   1   Miss   [ [], [5] ]
2   4   0   Miss   [ [4], [5] ]
3   6   0   Miss   [ [6,4], [5] ]
4   3   1   Miss   [ [6,4], [3,5] ]
5   4   0   Hit   [ [4,6], [3,5] ]
6   0   0   Miss   [ [0,4], [3,5] ]
7   2   0   Miss   [ [2,0], [3,5] ]
8   5   1   Hit   [ [2,0], [5,3] ]
9   3   1   Hit   [ [2,0], [3,5] ]
10   0   0   Hit   [ [0,2], [3,5] ]
11   6   0   Miss   [ [6,0], [3,5] ]
12   7   1   Miss   [ [6,0], [7,3] ]
13   11   1   Miss   [ [6,0], [11,7] ]
14   3   1   Miss   [ [6,0], [3,11] ]
15   5   1   Miss   [ [6,0], [5,3] ]
2-way set-assoc summary: Hits = 4 out of 15 → Hit ratio = 4/15 ≈
0.2667 (26.67%)
a.   Illustrate and analyze the MOS-based Static RAM (SRAM) cell.
Discuss how read and write operations are performed in SRAM, focusing [10]
on how data is stored, accessed, and maintained using control signals and
transistors.
Ans.
Q6
CO-4;
SO-3;
BL-2,3
********** 12 **********
--- page 13 ---
b.   Differentiate between an I/O Program and an I/O Channel. Explain the
necessity of a DMA (Direct Memory Access) controller with suitable   [10]
illustration."
Ans.   Aspect   I/O Program   I/O Channel
A dedicated hardware
A set of instructions written component (or
by the CPU to control and   controller) that manages
Definition
manage input/output   I/O operations
operations directly.   independently of the
CPU.
The I/O channel
CPU executes all I/O
controls data transfer
instructions; CPU is directly
once it receives a
Control   responsible for transferring
command from the
data between I/O devices
CPU, reducing CPU
and memory.
involvement.
High — CPU must wait for Low — CPU initiates
CPU
I/O operations to complete   the operation, and the
Involveme
(busy waiting or interrupt-   I/O channel handles it
nt
driven).   autonomously.
Executes a channel
Executed as part of the main program (set of I/O
Execution program’s instruction   instructions)
sequence.   independently of the
CPU.
Faster and more
Slower, as the CPU is
efficient, as the channel
Speed   frequently interrupted by
operates concurrently
I/O operations.
with the CPU.
Direct Memory Access
Programmed I/O and
(DMA) controllers and
Example Interrupt-driven I/O
Channel I/O systems in
methods.
mainframes.
Used in systems
Suitable for simple or low-   requiring high-speed or
Use Case
speed I/O devices.   large-volume data
transfers.
a.   Analyze and explain the major functional components of a computer
system with suitable illustration. Also, simplify the following Boolean
Q7
function using a Karnaugh Map:   [10]
CO-1,4;
SO-6;   F(A, B, C, D, E) = ∑m(0, 5, 6, 8, 9, 10, 11, 16, 20, 24, 25, 26, 27, 29,
BL-4,6   31)
Ans.
********** 13 **********
--- page 14 ---
b.   State and prove the D-Morgens Theorem with the help of truth Table,
Also simplify the following expression using Boolean Algebra
[10]
i. (x + x y) (x + y) + y z = y + z
ii. w y z + w z + y z +x y z = w y +w z + x z
Ans.
********** 14 **********
````
