# Logic Design and Computer Organization: answer keys

Answer keys and model answers published on the portal, newest first.

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
