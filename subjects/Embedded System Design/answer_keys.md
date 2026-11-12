# Embedded System Design: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 1b4d687ec1dd

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_EXTC_7006/Embedded System Design/ANS_Embedded System Design(702EX0E008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Embedded System Design
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
Q1   Answer briefly:   [20]
CO-1; SO-1;   a.   List design metrics of embedded system and describe any four how it helps to [05]
BL-1
check system performance.
List design metrics-6-8 (1M)
Any four for system performance(4M)
CO-4; SO-1;   b.   What is RS 232 used for data communication explain with its features. Explain [05]
BL-1, 2
the role of handshaking signal used in RS232 communication protocol.
RS-232 serial communication standard meaning and basics(1M)
Role of handshaking signal used in RS232 communication protocol with
name and use of each handshaking signal.(4M)
********** 1 **********
--- page 2 ---
CO-3; SO-1;   c.   Explain multitasking concept with respect to RTOS   [05]
BL-2
Basic of time slicing technique(1M) and explanation(4M)
********** 2 **********
--- page 3 ---
CO-5; SO-1;   d.   Compare between compiler and cross compiler.   [05]
BL-2
Any five valid point(5M)
Q2   a.   Define and list the main types of embedded memories. Explain the role of [10]
CO-1; BL-1,2 SO-1;   memory in embedded system and Compare between SRAM and DRAM.
Main types of embedded memories (3M). Explain the role of memory in
embedded system(2M) and Compare between SRAM and DRAM-Any five
valid point(5M)
********** 3 **********
--- page 4 ---
Q2   b.   Classify different embedded communication protocols. Identify and Discuss [10]
CO-2; SO-1;   the communication protocol, which is used for industrial control system.
BL-2,3
Classification different embedded communication protocols(2M)+
Identify communication protocol, which is used for industrial control
system-CAN(1M)+features and discussion (7M)
********** 4 **********
--- page 5 ---
Q3   a.   Develop an interfacing diagram of single Seven Segment Display with 8051 [10]
CO-5; SO-6;   microcontroller and write a program in assembly or embedded C to display
BL-3
even digit continuously on Common Anode type seven-segment display.
Interfacing Diagram (2M)
Program -lookup table-Value to be loaded as per common anode type for
even number between 0 to 9 (2M) ,Program either in assembly or embedded
C with comment(6M)
Program with any other way with correct logic (with comment)
Interfacing Diagram:
********** 5 **********
--- page 6 ---
Program either with C or Assembly:
Assembly:
START:
MOV P3,#00H
COUNT1:
MOV P1,#0C0H
ACALL DELAY
MOV P1,#0A4H
ACALL DELAY
MOV P1,#99H
ACALL DELAY
MOV P1,#82H
ACALL DELAY
MOV P1,#90H
ACALL DELAY
SJMP COUNT1
DELAY: MOV TMOD,#10H
MOV R0,#14H
REPEAT: MOV TL1,#0AEH
MOV TH1,#3CH
SETB TR1
WAIT: JNB TF1,WAIT
CLR TR1
CLR TF1
DJNZ R0,REPEAT
********** 6 **********
--- page 7 ---
RET
END
Q3   b.   List the serious problems that can arise in semaphores. Also, demonstrate the [10]
CO-3; SO-1;   priority inversion problem that arises in shared data space in an RTOS with a
BL1,2
suitable example.
List serious problem(1M)-Priority inversion and Deadlock
priority inversion problem with diagram (9M)
Q4   a.   Classify different computational models in embedded system design. Design [10]
CO-4; SO-1;   an Automatic Tea/Coffee vending Machine using a state machine model with
BL-2
a suitable diagram.
Different computational models in embedded system design(2M)+ an
Automatic Tea/Coffee vending Machine using a state machine model with
a suitable diagram.(8M)
********** 7 **********
--- page 8 ---
Q4   b.   Explain the simulator tool used in embedded system development. Also, [10]
CO-5; SO-1;   illustrate advantages and limitation of simulator based debugging techniques.
BL-2
The simulator tool used in embedded system development- explanation
(6M) Also, illustrate advantages(2M) and limitation of simulator based
debugging techniques.(2M)
********** 8 **********
--- page 9 ---
The simulator-based debugging techniques are simple and straightforward.

Other advantages are:

No need for original Target Board

It is purely software oriented.

IDEs software support simulates the CPU of the target board.

Users only needs to know about the memory map of various devices within the target board
and the firmware should Agowaiterondke basesngf Machine using a state

Since real hardware rschiot medphivedl atheallentiveane. development can start well in advance
immediately after the device interface and memory maps are finalized.

This saves development time.

Simulate I/O peripherals

It provides the option to simulate various I/O peripherals.

Using simulator’s, 1/O support we can edit the values for I/O registers ad can be used as the
input/output value in the firmware execution. Hence it eliminates the need for connection

I/O devices for debugging the firmware.

Advantages of Simulator Based Debugging

* Simulates Abnormal Conditions

* With simulator’s simulation support we can input any desired value for any parameter during
debugging the firmware and can observe the control flow of firmware.

* It helps the developer in simulating abnormal operational environment for firmware and
helps the firmware developer to study the behavior of the firmware under abnormal input
conditions..

Limitations OF Simulator Based Debugging

Deviation from Real Behaviour

Simulation-based firmware debugging is always carried out in a development environment
where the developer may not be able to debug the firmware under all possible combinations
of input.

Under certain operating conditions we may get some particular result and it need not be the
same when the firmware runs in a production environment.

Lack of Real timeliness

The major limitation is that it is not real-time in behavior.

The debugging is developer driven and it is no way capable of creating a real time behavior.
Moreover, ina real application the I/O condition may be varying or unpredictable.

FIC QF OH ar
--- page 10 ---
Q5   a.   Classify core of an embedded system. Explain the design process in embedded [10]
CO-1; SO-1;   system with diagram and systematic steps.
BL-2
Classification core of an embedded system(3M)
Design process in embedded system with diagram (4M) and systematic
steps(3M).
Q5   b.   Illustrate the process, thread and task in RTOS with diagram. Explain task [10]
CO-3; SO-1;   management function of RTOS in detail steps.
BL1,2
The process, thread and task in RTOS –concept with diagram(5M)
Task management function of RTOS in detail steps.(5M)
********** 10 **********
--- page 11 ---
Q6   a.   Classify basic approaches for embedded Firmware design and Develop an [10]
CO-4; SO-1;   interfacing diagram for Stepper motor with 8051 microcontroller and write an
BL-3
embedded C program to rotate the motor 90° in the anticlockwise direction.
Types basic approaches for embedded Firmware design (1M)
Interfacing Diagram (2M)
Program -Program either in assembly or embedded C(5M) with comment
(3M) If motor step angle is 1.8° per pulse counter for 90° rotation is
decimal 50 as (1.8°*50= 90°)
Program with any other way with correct logic (with comment)
• Two basic approaches for firmware design.
– Conventional Procedure based Firmware Design/Super Loop Design.
– Embedded Operating System Based Design.
Q6   b.   Develop a Smart Chocolate Vending System by specifying its suitable [10]
CO-5; SO-2;   requirements. Outline the hardware architecture with the help of a block
BL-3
diagram.
Smart Chocolate Vending System:
Basic explanation and Requirements(4M)
********** 11 **********
--- page 12 ---
Hardware specifications components(Unit) and Diagram with brief
explanation (6M)
Q7   a.   Explain system on chip (SOC) concept in embedded system with example.   [05]
CO-1; SO-1;   System On Chip any valid concept2M) and any one valid Example
BL-2
explanation (3M)
System On Chip concept:
❖ A system-on-a-chip (SoC) is a system on a VLSI chip that has all
needed analog as well as digital circuits, processors and software.
❖ A system-on-a-chip (SoC) is a microchip with all the necessary
electronic circuits and   parts for a given system, such as a
smartphone or wearable computer, on a single   integrated   circuit
(IC).
❖ System-on-a-chip technology is used in small, increasingly complex
consumer electronic devices.
❖ Some such devices have more processing power and memory than a
typical 10-year- old desktop computer.
❖ Example, single-chip mobile phone.
Example:
Q7   b.   Compare mailboxes and pipes used in data communication.   [05]
CO3; SO-1;   Any five valid point(5M)
BL-2
********** 12 **********
--- page 13 ---
Q7   c.   How to debug the product, if not function as per expected behavior even bug [05]
CO-5; SO-1;   free firmware embedded system. Explain the procedures and tools involves for
BL-2
the same.
to debug the product, if not function as per expected behavior even bug free
firmware embedded system Used target hardware Debugging
(1M)+Procedures(3M)+List of tools and explanation of any four (6M)
********** 13 **********
--- page 14 ---
Q7   d. How does core play a role in embedded system design? Explain [05]
CO-1; SO-1;   microcontroller -based system design with one example.
BL-1,2
Important of core (2M)+any one application microcontroller -based
system design with basic diagram(3M)
********** 14 **********
````
