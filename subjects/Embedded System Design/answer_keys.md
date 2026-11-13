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

[Text in pictures on this page, read by OCR]
Elow Control

+ If one of the device sends data at a very fast rate and other device cannot
absorb the data rate, flow control is used.

* RS 232 has signals (handshake signals) that can be used for flow control.
--- page 2 ---
CO-3; SO-1;   c.   Explain multitasking concept with respect to RTOS   [05]
BL-2
Basic of time slicing technique(1M) and explanation(4M)
********** 2 **********

[Text in pictures on this page, read by OCR]
3. RTS (Request To Send)
> Once DTE receives the DSR, it prepares itself for the data transfer.

» = Itinitializes the memory pointer and the byte counter.
>» Itthen sends the RTS signal to the DCE to inform that it is ready for the data transfer.

4. CTS (Clear To Send)

> Once a stable contact is established with the Remote MODEM, the DCE send CTS to
DTE.

» This begins the data transmission between DTE and Remote MODEM through DCE.

3. RTS (Request To Send)
> Once DTE receives the DSR, it prepares itself for the data transfer.

» = Itinitializes the memory pointer and the byte counter.
>» Itthen sends the RTS signal to the DCE to inform that it is ready for the data transfer.

4. CTS (Clear To Send)

> Once a stable contact is established with the Remote MODEM, the DCE send CTS to
DTE.

» This begins the data transmission between DTE and Remote MODEM through DCE.

Multitasking:(Multithreading)

* This is the best way to handle this situation.

= If more than one tasks of same priority are ready, the RTOS can allow each task to run for a
small CPU “time-slice”.

* If the task is not completed, RTOS will switch to the other task and even that will run for the
same time-slice. Thus, each task gets to run for a small amount of time periodically.

* Hence atleast smal! tasks will get completed faster than the long ones, but at the same time,

the long tasks are also getting executed so will not remain pending for too long.
* This method is also called time-sharing as the CPU time is shared between multiple tasks.
* Itis very important that the switching time between tasks is small, so that a user should feel

as if all the tasks are running “simultaneously”.

* Though this method gives a good performance, it is very complex to implement. Dedicated
hardware is required to perform rapid task switching, which in turn increases the cost.

= Any of the above methods can be used depending upon the system cost, service criteria etc,

* The choice of the correct scheduling method is very important as it can really improve the
system performance.
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

[Text in pictures on this page, read by OCR]
Compiler Vs Cross Compil

Native Compiler :-

= Translates Program for same Hardware

* Itis used to make programs for same hardware & OS it is installed on
= Itis dependent on Hardware & OS

= Itcan generate executable file like .exe

* TurboC or GCC (GNU Compiler Collection) is a native Compiler

Cross Compiler:-

* Translates Program for different hardware

* Itis used to make programs for other hardware like AVR/ARM
= Itis Independent of Hardware & OS

= Itcan generate RAW code .hex

* Keil is a cross Compiler

oe
%

o
%

oe
Og

oe
%

o
%

oe
Og

Embedded Memories

An essential integral part of a processor/controller-based
embedded system.

On-chip memory - Some processors/controllers contain built-
in memory.

Off-chip memory — External memory

Embedded system designers must be aware of the different
types of memories.

In a most embedded systems, two types of memory are used,
ROM and RAM.

ROM (Program storage memory)
>» Stores the program instruction and constant data (Look up table).
--- page 4 ---
Q2   b.   Classify different embedded communication protocols. Identify and Discuss [10]
CO-2; SO-1;   the communication protocol, which is used for industrial control system.
BL-2,3
Classification different embedded communication protocols(2M)+
Identify communication protocol, which is used for industrial control
system-CAN(1M)+features and discussion (7M)
********** 4 **********

[Text in pictures on this page, read by OCR]
ROM

* Can be classified into different types, depending on the
fabrication, erasing and programming technique.
>» Masked ROM
> PROM (OTP)
> EPROM
> EEPROM
> FLASH
> NVRAM

Static RAM Vs Dynamic RAM

Static RAM ynamic RAM

Stores data in the form of | Stores data in the form of
voltage. | charges.
Basic element - flip-flops | Basic element - MOS

| transistor gates.

Fastest | Slower than SRAM.
Costly | Cheaper

Refreshing circuitry not Refreshing circuitry is
required. required for restore
charge.

CAN (Controller Area Network)

* ACAN is an asynchronous serial bus network that connects devices, sensors and actuators
in a system or sub-system for control applications.

* Multi-master communication protocol.
* First developed by Robert Bosch in 1986.
“ Compact
* Twisted Pair Bus line.
* Highest Baud Rate is |Mbps.
** Robust in noisy environments.
* CAN uses a message-oriented transmission protocol.

*» There are no defined addresses, just defined messages.
* Itis present in both physical and data link layer of OSI layers.
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

[Text in pictures on this page, read by OCR]
CAN (Controller Area Network)

* It was designed for automotive applications needing data rates of up to 1 Mbps and high
levels of embedded communication system for microcontrollers, as well as a standard
communication network for industrial control system.

* CAN provides two communication services: the sending of a message (data frame
transmission) and the requesting of a message (remote transmission request, RTR).

After CAN

Engine Anti-
Control Lock
Brakes

CAI CCAN

High Speed g Zz Low Speed

f3)
AN CAI
Trans- Active
mission] Suspen:

Control sion
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

[Text in pictures on this page, read by OCR]
Priority Inversion

* This is a serious bug that arises due to semaphores.
= Assume there are three tasks A (Highest priority), B (Medium priority) and C (Lowest priority).

* There is a semaphore "S" shared by task.

Pek Ages
« Here priority inversion will occur as follows: Sieiets
= C gets ready. aki Dadsignele
* Since no other task is read, scheduler makes C running. ‘shits Rs mac an —
* Ctakes S. maces \
= Now B gets ready. ee \ \
Taka
* Since B is of higher priority than C, scheduler switches to B. \
Hence B starts running and C goes into ready state. ™ \
aS

* During the execution of B, A gets ready.

re. $$ $$

(BES The ek the mucropeocener in excusing

Priority Inversion

* Since A is of higher priority than B, scheduler switches to A.

* Hence A starts running and B and C go into ready state.

= Now A wants to take the semaphore S.

* ButS is already taken by C, hence A gets blocked, waiting for C to release the semaphore.
* After A gets blocked, scheduler makes B running as it is higher priority than C.

* Thus, although A had higher priority than B and C, it will have to wait for both B and C to complete.
* This will badly affect the timing for high priority task A, especially if B is a long task.

* This problem is called priority inversion.

+ It can be solved by “Priority Inheritance”(also called Promotion).

+ Here, after A gets blocked, the priority of C gets

* Hence the scheduler will execute C instead of B boosted’ toa same level as A.

* Once C releases the semaphore. the priorities will get restored beck.

+ Now A can get into running state.

* Thus, A will not have to wait for the task B to get completed.
--- page 8 ---
Q4   b.   Explain the simulator tool used in embedded system development. Also, [10]
CO-5; SO-1;   illustrate advantages and limitation of simulator based debugging techniques.
BL-2
The simulator tool used in embedded system development- explanation
(6M) Also, illustrate advantages(2M) and limitation of simulator based
debugging techniques.(2M)
********** 8 **********

[Text in pictures on this page, read by OCR]
Model:

A model is a formal system consisting of objects & composition rules.

It is hard to make a decision on which model should be followed in particular system design.
Most often designers switch between variety of models from requirement specification to

implementation.

Data Flow Graph/Diagram (DFG) Model

Control Data Flow Graph/Diagram (CDFG) Mode
State Machine Mode!

Sequential Program Model
Concurrent/Communicating Process Mode

Object Oriented Mode

State Machine Model :

= Example-2: Automatic Tea/Coffee vending Machine
* Requirements:
* 1, Tea/Coffee vending machine is initiated by user by inserting 5 Rs. Coin,

* 2. After inserting Coin, user can select either coffee /tea / press cancel order and take back the
coin.

= Events: ‘Insert Coin’ ‘Tea Button Pressed’, ‘Coffee Button Pressed’,
‘Cancel Button Pressed’, ‘Coffee Dispensed’and ‘Tea Dispensed’
* States: A= ‘OFF/wait for coin’, B= ‘wait for user i/p’, C= "Dispense Tea’ and

D=’Dispense Coffee’.

Simulator and emulators are two important tools used in embedded system development.
Simulator is a software tool used for simulating the various conditions for checking the functionality of the
application firmware.
It is a host-based program that simulates the functionality and instruction set of the target processor.
The features of Simulator based debugging are :
1. Purely software based
2. Doesn’t require a real target system
3. Very primitive
4. Lack of Real —time behavior.
Simulation is used whenever trying things in the physical world would be inconvenient, expensive.
Simulation allows experimenter to try things with more control over parameters and better insight into the
results.
Simulating an embedded computer system can be broken down into five main parts:
The computer board itself, the piece of hardware containing one or more processor, executing the embedded
software.
The software running on the computer board. This includes the user applications , also the boot ROM or BIOS,
hardware drivers, OS and various libraries.
The communication network or networks that the board is connected to and over which the software
communicates with software on other computers.
The environment in which the computer operates and that it measures using sensors and affects using actuators.
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

[Text in pictures on this page, read by OCR]
CORE OF EMBEDDED SYSTEMS

* Almost 80% of the embedded systems are processor/controller based.
** The processor may be a microprocessor or a microcontroller or a digital signal processor,
depending on the domain and application.

“» An embedded system processor chip or core can be one of the following:
1. General Purpose Processor (GPP).
2. Application Specific System Processor (ASSP).

3. Multiprocessor system using General Purpose processors (GPP) and Application
specific Instruction Processors (ASIPs).

4. GPP cores or ASIP cores are integrated into either an Application Specific Integrated
Circuit (ASIC) or Very Large Scale Integrated Circuit (VLSI) circuit or an FPGA core
integrated with processor units ina VLSI (ASIC) chip.
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

[Text in pictures on this page, read by OCR]
Task/Process management

* Deals with setting up the memory space for the tasks, loading the task’s code into the memory
space, allocating system resources, setting up a task control block(TCB) for the task and
task/process termination/deletion.

* ATCB is used for holding the information corresponding to a task.

* TCB usually contains the following set of information.

TASK ID: task identifier number.

TASK STATE: the current state of the task.

TASK TYPE: task type. Indicates what is the type for this task. The task can be a hard real time or soft real time
or background task.

TASK PRIORITY: task priority ( EX: Task priority is higher for task with priority=1)

Vv TASK CONTEXT POINTER: context pointer. Pointer of context saving.

v TASK MEMORY POINTER: pointers to the code memory, data memory and stack memory for the task.

Vv TASK SYSTEM RESOURCE POINTER: pointers to systems resources (semaphores, mutex ete ) used by task.
TASK POINTERS: pointers to other TCBs.

* Task management service utilizes the TCB of a task in the following way
Vv Creates a TCB for a task on creating task.

¥ Delete/Remove the TCB of a task when the task is terminated or deleted.
V Reads the TCB to get the state of task.

v Update the TCB with updated parameters on need basis.

¥ Modify the TCB to change the priority of the task dynamically.
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

[Text in pictures on this page, read by OCR]
Mobile Phone on a SoC

A SYSTEM ON CHIP

ouses
Embeds:
> Multiple processors,
> memories,
> multiple standard source
proc solutions (IP Cores),
AND

> Logic and analog units
--- page 13 ---
Q7   c.   How to debug the product, if not function as per expected behavior even bug [05]
CO-5; SO-1;   free firmware embedded system. Explain the procedures and tools involves for
BL-2
the same.
to debug the product, if not function as per expected behavior even bug free
firmware embedded system Used target hardware Debugging
(1M)+Procedures(3M)+List of tools and explanation of any four (6M)
********** 13 **********

[Text in pictures on this page, read by OCR]
Mailboxes

« It is very similar to a queue.
= It has two advantages over a queue.
i. Messages can be retrieved in the order of priority or in the order of FIFO.
ii. A timeout can be specified so that a task does not remain permanently blocked
incase it is trying to read from an empty mailbox.
« Typically, the functions to add and read messages are called in the following
manner:

SendMsg (Mbid, msgpl, priority), /also inserts the prior ty of the message tn the matlbox
RecetveMsg (Mbid, timeout); // reads in order of priority vith a max fimeouf
CheckMsg /WfdJ /! reads tn order of FIFO

Pipes
+ Pipes are more advanced structures.
* Here the length of the message is not fixed as compared to queue or mailbox.
+ It is implemented by dynamically allotting memory for the messages.
+ The number of bytes is specified during adding or reading messages into the pipes.

‘Ss

* The data type of the messages passed and that which is defined should be the same else the
compiler will generate an error.

* The messages can be read by a wrong task. This should be prevented by careful programming.

+ Since the messages are shared data, they should be protected against misuse else there would be
shared data bugs.
--- page 14 ---
Q7   d. How does core play a role in embedded system design? Explain [05]
CO-1; SO-1;   microcontroller -based system design with one example.
BL-1,2
Important of core (2M)+any one application microcontroller -based
system design with basic diagram(3M)
********** 14 **********

[Text in pictures on this page, read by OCR]
TARGET HARDWARE DEBUGGING

= Even though firmware is bug free embedded product need not function as per expected
behavior.

* This is because of dry soldering, missing connections, un-noticed errors in PCB etc.

= Debugging the target board is the only way to sort out these issues.

Hardware debugging involves

* Monitoring various signals of target board.

= Checking connection between components.
* Circuit continuity checking.

Hardware debugging tools
Hardware debugging tools are
1, Magnifying Glass(Lens)

2. Multimeter

3. Digital CRO

4. Logic Analyzer

5. Function Generator

TARGET HARDWARE DEBUGGIN

Magnifying Glass(lens)

Itis a visual inspection tool.

* Surface of target board can be examined for dry soldering, improper soldering, track damage etc..
® Magnifying station incorporates magnifying glass attached to CFL tubes,

* The station may incorporate multiple lens.

* Mainlens acts as visual inspection tool.

* Other small lens is used for magnifying small area of the board for thorough inspection.

Multimeter

* Multimeteris used for measuring various electrical quantities.

* Primary debugging tool for physical contact based hardware debugging.

* Mainly used for checking circuit continuity, signal value, polarity, measuring supply voltage.
* Both analogand digital versions are available.

* Digital versions have better readability and accuracy.

Digital CRO

® CROis used for waveform capturing and analysis, measurement of signal strength etc.

* It is a very good tool in analyzing interference noise in power line and other signal lines.

* They are available in both analog and digital form

® Digital CROs are suitable for high frequency support and best suited or target board debugging.
````
