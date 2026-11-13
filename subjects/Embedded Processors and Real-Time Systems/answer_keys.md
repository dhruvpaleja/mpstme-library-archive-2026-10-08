# Embedded Processors and Real-Time Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 9fde26f0e0a4

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_EXTC_7006/Embedded Processors and Real-Time Systems/ANS_Embedded Processors and Real-Time Systems(702EX0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (4 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Embedded Processors and Real-Time Systems
Date: 15 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
a.
[5]
********** 1 **********

[Text in pictures on this page, read by OCR]
Program Status Word ( PSW ) and Flags


Carry flag PSWw7 cy

Auxiliary carry flag PSW.6 AC

Available to the user for general purpose PSW.5 =

Register Bank selector bit 1 Psw.4 RS1

Register Bank selector bit 0 PSW.3 RSO

Overflow flag Psw2 ov

User define bit PSW1 =

Parity flag Set/Reset odd/even parity PsW.0 P

RSI RSO Register Bank Address

0 0 Bank 0 00H-07H
0 1 Bank 1 O08H-OFH
1 0 Bank 2 10H-17H

1 1 Bank 3 18H-1FH
--- page 2 ---
b.   [5]
c. data segment   [5]
num1 dw 0ABCDh
num2 dw 1234h
result dw ?
data ends
code segment
start: assume ds: data, cs: code
mov ax,data
mov ds,ax
mov ax,num1
add ax,num2
mov result,ax
mov ax,4c00h
int 21h
code ends
end start
d. SPI is a synchronous serial communication protocol used for short-distance   [5]
communication between a master device and one or more slave devices (like
ADC, DAC, sensors, memory, etc.).
Full-duplex communication (simultaneous send & receive)
High speed (faster than I²C)
Simple hardware interface
No addressing (uses chip select lines)
********** 2 **********

[Text in pictures on this page, read by OCR]
Microprocessor vs. Microcontroller

Microprocessor Microcontroller
Dependent on other chips for many * Single chip computer which has
functions so hardware size increases. everything in-built.

CPU is stand-alone, RAM, ROM, I/O, , CPU, RAM, ROM, I/O and timer are
timer are separate.

Designer can decide on the amount
of ROM, RAM and I/O ports.

all on a single chip.
* fix amount of on-chip ROM, RAM,

I/O ports.
Program memory and data memory .
are same. + Uses different program and data
Suited to processing information in wc
computer systems. * Suited to control of I/O devices
Powerful addressing mode. requiring a minimum component count.
Data bus: 32,64,128 bits wide. * Extremely compact instructions.
Clock rate > 1GHz. + Data bus: 8,16 bits wide.
general-purpose. * 10 to 20 MHz.
Expensive. * single-purpose.

* Cheap.
--- page 3 ---
a.
Q2
[10]
b. Interfacing diagram of 8051 with motor (5M)
[10]
Explanation (5M)
a. Interfacing diagram of LPC2148 with keyboard (5M)   [10]
Q3
Explanation (5M)
b.   [10]
a.   1) 24 MHz (1M)   [10]
Q4   2) 32 KB RAM using 16 KB devices (Two devices) (1M)
3) Mapping table (4M)
4) Interfacing Diagram with 8086 (4M)
b. Explanation of Wi-Fi communication (5M)   [10]
Explanation LoRa technology (5M)
********** 3 **********

[Text in pictures on this page, read by OCR]
H Address Bus (20- bit)

i Bi
H (16 bit)

ALU Data bus (16 bit) =

“ if Internal Bus

{ Communication’ Control | 8086 Bus
H Registers Logic
H Instruction queue
| QBus

1 (@bit)

Execution Unit (EU) Bus Interface Unit (BIU)
--- page 4 ---
a. Crystal frequency calculation (2M)
Assembly language program (8M)
ORG 0000H
MOV R0,#05H
MOV TMOD,#20H
MOV TH1,# 0FDh
MOV SCON,#50H
SETB TR1
MOV SBUF,#'N'
Q5   L2:   JNB TI,L2
CLR TI   [10]
MOV SBUF,#'M'
L3:   JNB TI,L3
CLR TI
MOV SBUF,#'I'
L4:   JNB TI,L4
CLR TI
MOV SBUF,#'M'
L5:   JNB TI,L5
CLR TI
MOV SBUF,#'S'
L6:   JNB TI,L6
b.
Any 10 instructions (1M each)   [10]
a.
Q6   Illustrate the circuit diagram(4M)
[10]
Program(6M)
b. Digram (4M)   [10]
Explaination (6M)
a. Concept of memory segmentation with diagram (4M)   [10]
Q7
Calculate the physical addresses using segment and offset values with
suitable examples (6M)
b. Discussion of sensors (2M)   [10]
Discussion of actuators(2M)
Methods of connection, data transfer (4M)
Examples (2M)
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 50136221e843

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_EXTC_7006/Embedded Processors and Real-Time Systems/ANS_Embedded Processors and Real-Time Systems(702EX0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2026
- Text: mixed (6 pages), mean OCR confidence 95.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Embedded Processors and Real-Time Systems
Date: 11 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:
a.
[5]
b. data segment
num1 db 34h
num2 db 12h
res dw ?
data ends
code segment   [5]
start: assume ds:data, cs:code
mov ax,data
mov ds,ax
mov al,num1
mov bl,num2
********** 1 **********

[Text in pictures on this page, read by OCR]
P3 Bit Function SFR Significance

P3.0 RxD SBUEF __|Réeeive data pin for serial port in UART mode.
P31 TxD SBUEF _| Tmsmit data pin for serial port in UART mode.
P3.2 INTO TCON. 1 | Fxtemltnterupt

P3.3 INTI TCON.3 | Extem2l Interrupt

P3.4 TO TLO External Timer / Counter 0 input pin.

P3 . 5 T 1 TL 1 External Timer / Counter 1 input pin.

P3.6 WR . External memory write pulse.

P3.7 =—_— External memory read pulse.

RD -
--- page 2 ---
mul al,bl
mov res,ax
mov ax,4c00h
int 21h
code ends
end start
c.
[5]
Diagram 2M
Explanation 3M
d. SPI (Serial Peripheral Interface) Communication Protocol
SPI is a synchronous serial communication protocol used for short-distance
communication between a master device and one or more slave devices (like
ADC, DAC, sensors, memory, etc.).
Basic Features of SPI
Full-duplex communication (simultaneous send & receive)
High speed (faster than I²C)
Simple hardware interface
No addressing (uses chip select lines)   [5]
SPI Signals (4-wire interface)
1. MOSI (Master Out Slave In)
Data from master to slave
2. MISO (Master In Slave Out)
Data from slave to master
3. SCLK (Serial Clock)
Clock generated by master
4. SS/CS (Slave Select / Chip Select)
Used to select slave device (active low)
********** 2 **********
--- page 3 ---
a.
Q2
[10]
With proper example
b.
Digram (4M)
Explaination (6M)
Q3   a. Interfacing diagram (4M)
Explanation of interfacing of DAC with ARM (6M)
********** 3 **********

[Text in pictures on this page, read by OCR]
Address Bus (20- bit)

AH | AL | AX
BH | BL_| Bx

(16 bit)

ALU Data bus (16 bit)

Execution Unit (EU) Bus Interface Unit (BIU)
--- page 4 ---
b.
(TMOD 4M)
(Any mode with diagram 6M)
a.   1) 18 MHz (1M)
Q4   2) 32 KB EPROM using 16 KB devices (Two devices) (1M)
3) Mapping table (4M)
4) Interfacing Diagram with 8086 (4M)
b. Explanation of Bluetooth communication (5M)
Explanation Zigbee technology (5M)
Q5   a. Crystal frequency calculation (2M)
Assembly language program (8M)
b. Rotate (5M)
Shift instructions (5M)
[10]
a.   4M
Q6   Circuit diagram
Program.   6M
********** 4 **********
--- page 5 ---
b.
Digram (4M)
Explaination (6M)
a. 1.Concept of memory segmentation with diagram (4M)
2. Calculate the physical addresses using segment and offset values
with suitable examples (6M)
Q7
********** 5 **********

[Text in pictures on this page, read by OCR]
Memory Segments
y g 000

Segment 00H
Registers 200008

. DATA
DS: |2000H oFFFFH
ss: | 5000H STACK S0000H
5FFFFH
ES: |7000H 70000H
EXTRA 7FFFFH

cs; | 3000H

30000H
CODE 3FFFFH

Segments are < or = 64K and can overlap.
Note that the Code segment is < 64K since 7F FFFH is the
highest address.
--- page 6 ---
Hardware debugging tools
Hardware debugging tools are
1. Magnifying Glass(Lens)

2. Multimeter

3. Digital CRO

4. Logic Analyzer

5. Function Generator
````
