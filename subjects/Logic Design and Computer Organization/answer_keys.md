# Logic Design and Computer Organization: answer keys

Answer keys and model answers published on the portal, newest first.

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 7bae18013fe5

- Departments: Data Science
- Programmes: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND ENGINEERING (DATA SCIENCE) - 7011
- Source: `00_Original_Downloads/2024/Semester II/67783__Final-Exam__context_fixed.zip :: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND ENGINEERING (DATA SCIENCE) - 7011/Logic Design and Computer Organization/ANS_Final-Exam_Logic Design and Computer Organization(702CO0C053)_Semester II_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 May 2025
- Text: mixed (8 pages), mean OCR confidence 76.7
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Logic Design and Computer Organization
Date: 06 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 8 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Perform the given conversion,
= (41938)10   (1M)
= (1010001111010010)2   (2M)   [5]
= (121722)8   (2M)
b.   Y=(A+C+D)(B+C′)(A′+D′)   [5]
c.   [5]
d.   [5]
********** 1 **********
--- page 2 ---
Q2

Static RAM Dynamic RAM

1 Static RAM contains less | Dynamic RAM contains more memory
memory cells per unit area. | cells as compared to static RAM per unit
area.

2 It less access time hence | Its access time is greater than static
faster memories RAMs.

3 Static RAM _ consists of | Dynamic RAM stores the data as a charge
number of flip-flops. Each | on the capacitor. It consists of MOSFET
flip-flop stores one bit. and the capacitor for each cell.

4 Refreshing circuitry is not| Refreshing circuitry is required to
required. maintain the charge on the capacitors after
every few milliseconds. Extra hardware is
required to control refreshing. This makes

system design complicated.

5 Cost is more. Cost is less.

Full Subtractors

The disadvantage of a half subtractor is overcome by full subtractor. The full subtractor is a
combinational circuit with three inputs A,B,C and two output D and C’. A is the 'minuend’, B
is ‘subtrahend’, C is the ‘borrow’ produced by the previous stage, D is the difference output
and C' is the borrow output.

Truth Table

fl
0)

FIC 2 I HH ar
--- page 3 ---
Circuit Diagram

A BC

sl | me

L P LY D=A+B+C
ee. eee
I ey, AC+AB+BC

. ——

Control Unit (3M)

Arithmetic Logic Unit (4 M) 0
registers (3) a
Dividend (D) = 1319 = 11012
Divisor (d) = 319 = 00112
Number of bits (7) = 4
Initial Accumulator (A) = 00002
Initial Quotient (Q) = 11012
Perform 4 iterations (since n = 4)
Non-Restoring Division Table
Step Operation A (Accumulator) Q (Quotient) Action (Qo)
Initial Start 0000 1101
Q3 1 Shift Left (A, Q) 0001 1010
A= A -~ d(0001 - 0011) 1110 1010 0 (Negative)
2 Shift Left (A, Q) 1101 0100
A=A+d(1101 + 0011) Wi 0100 0 (Negative)
3 Shift Left (A, Q) 1110 1000
A= A+ d(1110 + 0011) 0001 1000 1 (Positive)
4 Shift Left (A, Q) 0011 0000
A= A-~d (0011-0011) 0000 0001 1 (Positive)
(1
0]

FC QI a iar
--- page 4 ---
MEMORY
INTERFACE

a ed
ino CBOE al

|

1 STREAM

1 4 BYTE

1 3 QUEUE

{ 8-8US 2

H =

| 35 i

i \

1 1

i ! CONTROL

L | SYSTEM

1 &u ¢ A-BUS

| AH AL
H BH BL
H cr cL ARITHMETIC
I DH DL LOGIC UNIT
1 SP
H BP
! Si
i Bi [OPERANDS].
| FLAGS: J |
FIGURE 2-7 8086 internal block diagram. (Intel Corp.)
Diagram 4 M
explanation 6 M
(1
0)
Q4 D.
Output
} FS > OFF 2 FFA > FEO
l |
CuK

FIC 7) IC HOH
--- page 5 ---
b.   The IEEE Standard for Floating-Point Arithmetic (IEEE 754) is a technical
standard for floating-point computation which was established in 1985 by
the Institute of Electrical and Electronics Engineers (IEEE). The standard
addressed many problems found in the diverse floating-point
implementations that made them difficult to use reliably and reduced their
portability. IEEE Standard 754 floating point is the most common
representation today for real numbers on computers, including Intel-based
PC’s, Macs, and most Unix platforms.
There are several ways to represent floating point number but IEEE 754 is
the most efficient in most cases. IEEE 754 has 3 basic components:
1.   The Sign of Mantissa –
This is as simple as the name. 0 represents a positive number while 1
represents a negative number.
2.   The Biased exponent –
The exponent field needs to represent both positive and negative
exponents. A bias is added to the actual exponent in order to get the stored
exponent.
3.   The Normalised Mantissa –
The mantissa is part of a number in scientific notation or a floating-point
number, consisting of its significant digits. Here we have only 2 digits, i.e. O
and 1. So a normalised mantissa is one with only one 1 to the left of the
decimal.
********** 5 **********
--- page 6 ---
IEEE 754 numbers are divided into two based on the above three
components: single precision and double precision.
a.   Booth algorithm gives a procedure for multiplying binary integers in signed 2’s
complement   representation in   efficient   way,   i.e.,   less   number   of
additions/subtractions required
Q5   [1
0]
(A,Q)=0001 1100
Converting to decimal:
********** 6 **********

[Text in pictures on this page, read by OCR]
Single Precision (32-bit)
IEEE 754 Single Precision consists of:
© 1-bit sign: 0 (positive number)
¢ 8-bit exponent: F + 127
10 + 127 = 13719 = 100010012
* 23-bit mantissa (excluding the leading 1):

00111010110010000000000

Thus, the Single Precision IEEE 754 Representation:
0 10001001 00111010110010000000000
Double Precision (64-bit)
IEEE 754 Double Precision consists of:
¢ 1-bit sign: 0 (positive number)
« 11-bit exponent: F + 1023

10 + 1023 = 1033; = 10000001001,

* 52-bit mantissa (excluding the leading 1):

0011101011001000000000000000000000000000000000000000

Thus, the Double Precision IEEE 754 Representation:

0 10000001001 0011101011001000000000000000000000000000000000000000

Step A (Accumulator) Q (Multiplier) Qs Operation

Initial 0000 0100 ti) Initial values

1 0000 0100 0 No operation (Qs, Q-: = 00)

Shift 0000 0010 0 Arithmetic Right Shift (ARS)

2 0000 0010 ft) No operation (Qo, Q-: = 00)

Shift 0000 0001 tt) Arithmetic Right Shift (ARS)

3 0000 0001 0 No operation (Qe, Q-: = 00)

Shift 0000 0000 1 Arithmetic Right Shift (ARS)

4 0111 0000 1 A=A+M (A = 0000 + 0111 = 0111)

Shift 0011 1000 i) Arithmetic Right Shift (ARS)
--- page 7 ---
b.
[1
0]
a.   Programmed I/O. 3M
Q6   Interrupt- initiated I/O. 3M   [1
Direct memory access (DMA). 4M
0]
b.   [1
❖ The addressing mode is divided into following groups,
1) Register addressing mode   0]
2) Immediate addressing mode
3) Memory addressing mode
4) String addressing mode
5) I/O addressing mode
6) Implied addressing mode
❖ The different memory addressing modes available are :
1) Direct memory addressing mode.
2) Register indirect addressing mode.
3) Register relative addressing mode.
4) Based indexed addressing mode.
5) Relative based indexed addressing mode
********** 7 **********

[Text in pictures on this page, read by OCR]
" SUPER FAST
‘SUPER EXPENSIVE
TINY CAPACITY

CPU CACHE

FASTER
EXPENSIVE
‘SMALL CAPACITY

EDO, SD-RAM, DDR-SDRAM, RD-RAM PHYSICAL MEMORY

FAST
ED REASONABLY

PRICI
and More... AVERAGE CAPACITY

SOLID STATE MEMORY AVERAGE SPEED
‘SSD, Flash Drive PRICED REASONABLY
AVERAGE CAPACITY

Mechanical Hard D VIRTUAL MEMORY

CHEAP
LARGE CAPACTITY

A Simplified Computer Memory Hierarchy
Illustration: Ryan J. Leng

Feature Volatile Memory Non-Volatile Memory

Definition Memory that requires power to retain Memory that retains data even when power is
data. turned off.

Examples RAM (Random Access Memory), Cache ROM (Read-Only Memory), SSDs, HDDs, Flash
Memory Memory

Data Retention Loses data when power is off. Retains data permanently.

Speed Very fast (used for active processing). Slower compared to volatile memory.

Usage Temporary storage for active programs Permanent storage for operating systems,
and processes, applications, and files.

Cost Generally more expensive per unit of More affordable per unit of storage.
storage.

Power Requires continuous power supply. Does not require power to store data.

Dependency
--- page 8 ---
a.   data segment   [1
num1 dw h   0]
num2 db 12h
quo db ?
rem db ?
data ends
code segment
start: assume ds:data, cs:code
Q7   mov ax,data
mov ds,ax
mov ax,num1
div num2
mov quo,al
mov rem,ah
mov ax,4c00h
int 21h
code ends
end start
b.   K-Map entry (02 Marks) and correct Grouping with expression (06   [1
Marks) + circuit implementation (02 Marks)   0]
Y = A̅D + B̅CD + AB̅C̅
********** 8 **********
````

## 2024-25 · Re-Exam · Sem 2 · Answer key · paper c8a60981940a

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/BTech_CSE_DS_7011/Logic Design and Computer Organization/ANS_Logic Design and Computer Organization(702CO0C053)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2025
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: I/Sem 2 Re-exam(Exam Year: 2024-2025)
Subject: Logic Design and Computer Organization
Date: 08 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 7 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   (32667)10
(0111 1111 1001 1011)2   [5]
(37715)8
b.   [5]
Y = B̅D + A̅C + AC̅ + A̅B̅D
c.   [5]
********** 1 **********
--- page 2 ---
d.   [5]
a.
Q2
[10]
BINARY TO GRAY CODE
BINARY CODE   GRAY CODE
0   0   0   0   OFF   OFF   OFF   OFF
0   0   0   1   OFF   OFF   OFF   ON
0   0   1   0   OFF   OFF   ON   ON
0   0   1   1   OFF   OFF   ON   OFF
********** 2 **********
--- page 3 ---
0   1   0   0   OFF   ON   ON   OFF
0   1   0   1   OFF   ON   ON   ON
0   1   1   0   OFF   ON   OFF   ON
0   1   1   1   OFF   ON   OFF   OFF
1   0   0   0   ON   ON   OFF   OFF
1   0   0   1   ON   ON   OFF   ON
1   0   1   0   ON   ON   ON   ON
1   0   1   1   ON   ON   ON   OFF
1   1   0   0   ON   OFF   ON   OFF
1   1   0   1   ON   OFF   ON   ON
1   1   1   0   ON   OFF   OFF   ON
1   1   1   1   ON   OFF   OFF   OFF
b.
Describe the various functional units of basic digital/computer system with
suitable diagram.
A computer consists of six main components namely,
1. Input unit
2. Central Processing Unit
3. Memory unit
4. Arithmetic & logical unit,
5. Control unit and
6. Output unit   [10]
a.   [10]
Q3
********** 3 **********
--- page 4 ---
b.   Diagram of 8086 Processor =4 Marks   [10]
EU Explanation = 6 Marks
a.   1. SR flip flop. (5M)   [10]
Diagram(2M),
Q4
Explanation (3M)
2. D flip flop (5M) (Diagram, and Excitation table)
Diagram(2M),
Explanation (3M)
b.   The IEEE Standard for Floating-Point Arithmetic (IEEE 754) is a technical   [10]
standard for floating-point computation which was established in 1985 by the
Institute of Electrical and Electronics Engineers (IEEE). The standard
addressed many problems found in the diverse floating-point
implementations that made them difficult to use reliably and reduced their
portability. IEEE Standard 754 floating point is the most common
representation today for real numbers on computers, including Intel-based
PC’s, Macs, and most Unix platforms.
There are several ways to represent floating point number but IEEE 754 is the
most efficient in most cases. IEEE 754 has 3 basic components:
********** 4 **********

[Text in pictures on this page, read by OCR]
Non-Restoring Division Table

Step Operation A (Accumulator) Q (Quotient) Action (Qo)
Initial Start 0000 1101
1 Shift Left (A, Q) 0001 1010

A= A -~ d(0001 - 0011) 1110 1010 0 (Negative)
2 Shift Left (A, Q) 1101 0100

A= A+d(1101 + 0011) Wi 0100 0 (Negative)
3 Shift Left (A, Q) 1110 1000

A= A+ d(1110 + 0011) 0001 1000 1 (Positive)
4 Shift Left (A, Q) 0011 0000

A= A- d(0011 - 0011) 0000 0001 1 (Positive)

MEMORY
INTERFACE

1 €u 2 A-BUS

AH. AL
BH BL
cH cL ARITHMETIC
i DH DL LOGIC UNIT
1 3P
i BP
! St
a ‘OPERANDS i}

FLAGS J LI

FIGURE 2-7 8086 internal block diagram. (Inte! Corp.)
--- page 5 ---
1.   The Sign of Mantissa –
This is as simple as the name. 0 represents a positive number while 1
represents a negative number.
2.   The Biased exponent –
The exponent field needs to represent both positive and negative exponents.
A bias is added to the actual exponent in order to get the stored exponent.
3.   The Normalised Mantissa –
The mantissa is part of a number in scientific notation or a floating-point
number, consisting of its significant digits. Here we have only 2 digits, i.e. O
and 1. So a normalised mantissa is one with only one 1 to the left of the
decimal.
IEEE 754 numbers are divided into two based on the above three
components: single precision and double precision.
Final IEEE 754 Single-Precision Representation (32-bit)
0 10000010 01010100000000000000000
Final IEEE 754 Double-Precision Representation (64-bit)
0 10000000010 0101010000000000000000000000000000000000000000000
000
a.
Q5
[10]
AQ=0000 1110 = 18
********** 5 **********

[Text in pictures on this page, read by OCR]
Step A (4-bit) Q (4-bit) (Multiplier) Q, Operation

Initial 0000 0011 0 Initialization

1 0000 0011 ty) (Qo Q-1 = 00 — Shift Right)
2 0000 0001 1 Shift Right

3 1010 0001 1 (Q0.Q-1+=11-A=A-M)
4 1101 1000 1 Shift Right

5 0011 1000 1 (QoQ-1=10 -A=A+M)
6 0001 1100 0 Shift Right

7 0000 1110 0 Shift Right (Final Step)
--- page 6 ---
b.
[10]
a.   Working Principle of a USB Interface
A Universal Serial Bus (USB) interface is a standard communication protocol used
for connecting peripherals (e.g., keyboards, mice, flash drives) to a computer or other
host devices. It operates based on the following principles:
1. Host-Device Architecture
A USB system consists of a host (e.g., computer) and one or more
devices (e.g., USB flash drive, keyboard).
The host manages communication and supplies power to connected
devices.
2. Serial Data Transmission
USB transfers data serially (bit by bit) to reduce the number of required
data lines.
Uses differential signaling (D+ and D-) for noise reduction.
3. Plug and Play (PnP) and Hot Swapping
Devices can be plugged in or removed without restarting the system.
The host automatically detects and configures the device using drivers.
Q6   4. Power Supply
USB ports provide +5V power to connected devices, enabling them to   [10]
function without an external power source.
5. Data Transfer Modes
USB supports different transfer speeds and types based on device
requirements:
Control Transfer: Used for configuration and setup.
Bulk Transfer: Used for large, non-time-sensitive data (e.g., file
transfers).
Isochronous Transfer: Used for real-time data (e.g., audio/video
streaming).
Interrupt Transfer: Used for time-sensitive small data (e.g., keyboards,
mice).
6. Multiple Device Connection (USB Hub)
A USB hub allows multiple devices to connect to a single USB port.
Uses a tree topology for managing multiple connections.
7. Versions and Speed
USB 1.0/1.1: 1.5 Mbps (Low Speed) and 12 Mbps (Full Speed)
USB 2.0: 480 Mbps (High Speed)
USB 3.0/3.1: 5 Gbps to 10 Gbps (SuperSpeed)
********** 6 **********

[Text in pictures on this page, read by OCR]
MOTHERBOARD

Types of cache memory
Cache memory is fast and expensive. Traditionally, it is categorized
as "levels" that describe its closeness and accessibility to the
microprocessor,
There are three general cache levels:

L1 cache, or primary cache, is extremely fast but relatively small,
and is usually embedded in the processor chip as CPU eache.

L2 cache, or secondary cache, is offen more capacious than L1.
L2 cache may be embeddec
clip or coprocessor and have a high-speed alternative system bus
conmecting the cache and CPU. That way it doesut get slowed by
traffic on the main system bus

on the CPU, or it can be om a separate

Level 3 (L3) cache is specialized memory developed to improve the
performance of L1 and L2.L] or L2 can be significantly faster than
L3, though L3 is usually double the speed of DRAM.

With multicore processors, each core can have dedicated L1 and L2
cache, but they can share an L3 cache. If an L3 cache references an
instruction, it is usually elevated to a higher level of cache.

Figure 1.2 Simplified View of Major Elements of a Muldcore Computer
--- page 7 ---
USB 4.0: Up to 40 Gbps
b.   ❖ The addressing mode is divided into following groups,   [10]
1) Register addressing mode
2) Immediate addressing mode
3) Memory addressing mode
4) String addressing mode
5) I/O addressing mode
6) Implied addressing mode
❖ The different memory addressing modes available are :
1) Direct memory addressing mode.
2) Register indirect addressing mode.
3) Register relative addressing mode.
4) Based indexed addressing mode.
5) Relative based indexed addressing mode
a.   data segment   [10]
num1 dw 56abh
num2 dw 1232h
prodl dw ?
prodh dw ?
data ends
code segment
start: assume ds:data, cs:code
Q7
mov ax,data
mov ds,ax
mov ax,num1
mul num2
mov prodl,ax
mov prodh,dx
mov ax,4c00h
int 21h
code ends
end start
b.   [10]
K-Map entry (02 Marks) and correct Grouping with expression (06
Marks) + circuit implementation (02 Marks)
Y = A̅B̅D̅ + A̅BC + ABC̅
********** 7 **********
````
