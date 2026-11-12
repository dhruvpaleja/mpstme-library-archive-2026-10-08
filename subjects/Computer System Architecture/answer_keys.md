# Computer System Architecture: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 846e4f849302

- Departments: Computer Engineering
- Programmes: DIPLOMA IN COMPUTER ENGINEERING - 7073
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/DIPLOMA IN COMPUTER ENGINEERING - 7073/COMPUTER SYSTEM ARCHITECTURE/ANS_COMPUTER SYSTEM ARCHITECTURE(701EX0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: COMPUTER SYSTEM ARCHITECTURE
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Q1 is compulsory
5. Out of remaining question attempt any 4 question
6. In all total 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1. Answer Briefly:   [20 M]
a. Explain which cache replacement strategy (LRU, FIFO, or LFU) would provide a better hit ratio for the
given sequence of memory references when the cache has 4 lines, and justify your answer briefly.: 3, 4,
2, 2, 1, 4, 5, 2, 6, 7, 4, 2, 1, 2, 3, 4, 2, 1, 2, 1, 3, 4, 1, 5, 2.   [05M]
For the given sequence of memory references:
3, 4, 2, 2, 1, 4, 5, 2, 6, 7, 4, 2, 1, 2, 3, 4, 2, 1, 2, 1, 3, 4, 1, 5, 2 with cache size = 4 lines:
•   FIFO (First-In-First-Out): Replaces the oldest entry first, without considering usage
frequency.
•   LRU (Least Recently Used): Replaces the cache line that has not been used for the longest
time.
•   LFU (Least Frequently Used): Replaces the cache line used least frequently.
Result:
When the sequence is simulated, LRU achieves a higher hit ratio because it adapts better to
temporal locality — recently used data tends to be reused.
Conclusion: LRU performs better than FIFO and LFU for this reference pattern.
b. Describe the three types of instruction code formats used in a basic computer and explain their structure
and significance.   [05M]
A basic computer uses three instruction code formats:
1. Memory Reference Instruction:
o Format: [Opcode (3 bits)] [Address (12 bits)]
o Example: AND 875 (performs logical AND with memory content at address 875).
2. Register Reference Instruction:
o Format: [Opcode (3 bits)] [0] [Register Operation (12 bits)]
o Used for operations within CPU registers like CLA (Clear Accumulator).
3. Input-Output Instruction:
o Format: [Opcode (3 bits)] [1] [I/O Operation (12 bits)]
********** 1 **********
--- page 2 ---
o Used for data transfer between I/O devices and accumulator.
Significance: Enables flexibility in addressing memory, registers, and I/O devices using a compact
instruction design.
c. Compare and contrast Computer Architecture and Computer Organization by applying relevant examples
to highlight their differences in system design and functionality.   [05M]
Aspect   Computer Architecture   Computer Organization
Describes the functional behavior,   Refers to the operational structure and
Definition
instruction set, and design of a system.   physical components.
Logic design, instruction formats, addressing Hardware implementation, data transfer,
Focus
modes.   control signals.
Example   ISA design (e.g., RISC or CISC).   Control unit design, pipeline implementation.
Concerned
What system does.   How system does it.
With
Example   How Intel CPU implements instruction fetch-
Intel x86 (architecture).
System   execute cycle (organization).
✅ Conclusion: Architecture defines what a computer is capable of, while organization defines how it is
implemented.
d. Illustrate and analyze the SISD and SIMD architectures with suitable diagrams, and evaluate how they
differ in terms of data processing and instruction execution capabilities.   [05M]
1. SISD (Single Instruction Single Data):
o One control unit and one processing element.
o Executes one instruction on one data item at a time.
o Example: Traditional uniprocessor systems.
o Diagram:
o CU → PE → Memory
2. SIMD (Single Instruction Multiple Data):
o One control unit but multiple processing elements.
o Executes one instruction on multiple data items simultaneously.
o Example: Vector processors, GPUs.
o Diagram:
o CU → PE1, PE2, PE3, ... PEn → Memory
Evaluation:
• SISD is efficient for sequential tasks.
• SIMD enhances performance in data-parallel applications like image processing and matrix
operations.
✅ Conclusion: SIMD provides higher throughput for parallel data operations compared to SISD.
********** 2 **********
--- page 3 ---
Q2.
a. Explain the IAS computer model proposed by Von Neumann, highlighting its key components and the
concept of stored program architecture.   [10M]
Answer:
The IAS (Institute for Advanced Study) Computer, designed by John Von Neumann in 1946, was one
of the earliest digital computers and served as a model for most modern computer systems.
1. Von Neumann Architecture – Concept:
•   Introduced the idea of the stored program concept, where data and instructions are both stored in
the same memory.
• The computer fetches and executes instructions sequentially unless altered by control instructions.
2. Major Components of IAS Computer:
1. Memory Unit:
o Stores both instructions and data.
o Each word had 40 bits, divided into two 20-bit instructions.
2. Arithmetic Logic Unit (ALU):
o Performs arithmetic and logical operations such as addition, subtraction, AND, OR, etc.
3. Control Unit:
o Fetches, decodes, and executes instructions from memory.
o Generates control signals to coordinate operations among components.
4. Input/Output Unit:
o Used for reading data into memory and writing results out from memory.
5. Registers (in Control Unit):
o Memory Buffer Register (MBR): Holds data read or written to memory.
o Memory Address Register (MAR): Holds the address of data or instruction.
o Instruction Register (IR): Holds the current instruction being executed.
o Accumulator (AC): Temporarily stores arithmetic results.
o Program Counter (PC): Holds address of next instruction to be executed.
b. Discuss the classification of computer instructions in detail and illustrate each category with suitable
examples showing their application in program execution.   [10M]
Answer:
Computer instructions are classified based on their operation type and purpose. Each instruction tells
the CPU what operation to perform and on which data.
1. Classification of Instructions:
Type   Purpose   Example   Explanation
Move data between registers,   Copies content of register B
1. Data Transfer Instructions   MOV A, B
memory, and I/O.   into A.
Adds contents of A and B;
2. Arithmetic Instructions   Perform mathematical operations. ADD A, B
result stored in A.
Perform bitwise logical   Performs logical AND
3. Logical Instructions   AND A, B
operations.   between A and B.
4. Branch or Control Transfer Change the sequence of   Jumps to address 2050 for
JMP 2050
Instructions   execution.   next instruction.
********** 3 **********
--- page 4 ---
Type   Purpose   Example   Explanation
Enable data transfer between CPU IN 01H, OUT Input from or output to
5. Input/Output Instructions
and peripherals.   02H   device ports.
6. Shift and Rotate   Rotates accumulator bits left
Shift or rotate bits in registers.   RLC A
Instructions   through carry.
7. Compare and Test   Compare data values or check   Compares A and B; sets flags
CMP A, B
Instructions   conditions.   accordingly.
PUSH B, POP Save and restore register data
8. Stack Instructions   Manage data using stack memory.
C   using stack.
2. Example Program:
Example to add two numbers stored in memory:
MOV A, [2000H]
ADD A, [2001H]
MOV [2002H], A
HLT
• Fetch data from 2000H and 2001H.
• Perform addition.
•   Store result at 2002H.
Q3.
a. Identify and explain the essential characteristics that define a computer memory system, highlighting their
role in system performance.   [10M]
Answer:
A computer memory system is responsible for storing data and instructions required for processing.
The performance of a computer greatly depends on how efficiently the memory system operates.
Key Characteristics of Memory Systems:
1. Storage Capacity:
o Defines how much data or number of instructions the memory can hold.
o Measured in bytes, kilobytes, megabytes, gigabytes, etc.
o Example: 8 GB RAM, 512 GB SSD.
2. Access Time (Speed):
o Time required to read or write data from/to memory.
o Faster access time leads to better system performance.
o Cache memory has the lowest access time; secondary storage has the highest.
3. Memory Cycle Time:
o The total time required to complete one read/write operation and prepare for the next.
o Determines how quickly consecutive operations can be executed.
4. Cost per Bit:
o Memory is designed by balancing cost and performance.
o Faster memories (like cache, registers) are expensive per bit compared to slower ones
(like hard disks).
5. Volatility:
o Determines whether the memory retains data when power is turned off.
o Volatile: RAM (data lost when power off)
o Non-Volatile: ROM, Flash, HDD.
6. Physical Size (Density):
o Refers to the amount of memory stored per unit area on a chip.
********** 4 **********
--- page 5 ---
o Higher density allows more storage in less space.
7. Organization (Hierarchy):
o Memory is organized in levels: Registers → Cache → Main Memory → Secondary
Memory → Tertiary Storage.
o Balances speed, cost, and capacity.
b. Describe the concept of a micro-programmed control unit, and explain how it functions in the execution of
control signals using microinstructions.   [10M]
Answer:
The micro-programmed control unit is a type of control unit in which the control signals required for
instruction execution are generated by microinstructions stored in a control memory.
1. Concept:
•   Instead of hardwiring the control signals, they are stored as microprograms in a control store
(ROM).
• Each machine instruction is implemented by a sequence of microinstructions forming a
microprogram.
2. Components of Micro-programmed Control Unit:
1. Control Memory (CM):
Stores the microinstructions that define the control signals for each CPU operation.
2. Control Address Register (CAR):
Holds the address of the next microinstruction to be fetched.
3. Control Data Register (CDR):
Holds the microinstruction fetched from the control memory.
4. Microinstruction Decoder:
Decodes the microinstruction and generates appropriate control signals.
5. Sequencing Logic:
Determines the address of the next microinstruction (sequential or branch).
3. Working Principle:
• The Instruction Register (IR) holds the instruction fetched from main memory.
• The microprogram sequencer uses the opcode from IR to select the starting address of the
corresponding microprogram.
• Each microinstruction specifies control signals to perform operations like ALU function, data
movement, or memory access.
•   After executing one microinstruction, control moves to the next one until the instruction cycle
completes.
********** 5 **********
--- page 6 ---
Q4.
a. Define and describe the concept of Superscalar Architecture, outlining its main features and advantages in
modern processors.   [10M]
A Superscalar Architecture is a type of CPU design that allows multiple instructions to be issued and
executed simultaneously during a single clock cycle.
1. Definition:
• A superscalar processor contains multiple execution units (such as ALU, FPU, Load/Store units)
to perform parallel instruction execution.
•   It increases instruction-level parallelism (ILP) without requiring changes in the program itself.
2. Key Features:
1. Multiple Pipelines:
o Processor can fetch, decode, and execute multiple instructions in parallel.
o Example: Dual or Quad pipeline processors.
2. Instruction Dispatch and Scheduling:
o Uses a dynamic instruction scheduling mechanism to assign instructions to available
execution units.
3. Out-of-Order Execution:
o   Instructions can execute as soon as operands are available, even if earlier instructions are still
running.
4. Register Renaming:
o Avoids data hazards by using different physical registers for temporary results.
5. Branch Prediction:
o Predicts instruction flow to keep the pipelines full and reduce stalls.
4. Advantages:
• Higher instruction throughput.
•   Better CPU utilization.
• Improved performance for independent instructions.
5. Disadvantages:
• Complex hardware design.
•   Inefficient for programs with strong data dependencies.
b. Explain the purpose and functioning of a Status Register in a CPU, and discuss how its flags assist in
instruction execution.   [10M]
Answer:
The Status Register, also known as the Program Status Word (PSW) or Flag Register, is a special
register in the CPU that indicates the outcome of arithmetic or logical operations and controls the
processor’s operation flow.
1. Purpose:
•   Stores flag bits that represent the status of the processor after an operation.
• Used by conditional branch and control instructions to make execution decisions.
********** 6 **********
--- page 7 ---
2. Common Flags in Status Register:
Flag Name   Symbol   Meaning / Condition
Set if there is a carry out from MSB during addition or borrow during
Carry Flag   C
subtraction.
Zero Flag   Z   Set if the result of an operation is zero.
Sign Flag   S   Reflects the sign of the result (1 for negative, 0 for positive).
Overflow Flag   O / V   Set when arithmetic overflow occurs (result exceeds range).
Parity Flag   P   Set if number of 1s in result is even.
Auxiliary Carry
AC   Used in BCD arithmetic operations.
Flag
Interrupt Flag   I   Enables or disables CPU interrupt recognition.
3. Working Example:
Example instruction:
MOV A, 05H
ADD A, 0BH
•   Result = 10H
• Carry Flag (C) = 0 (no carry)
• Zero Flag (Z) = 0 (result not zero)
• Sign Flag (S) = 0 (positive result)
If instruction was:
SUB A, A
Then Result = 0 → Z = 1 (Zero flag set).
4. Importance in Execution:
• Used in conditional branching (e.g., JZ, JC, JNZ) to control program flow.
•   Provides feedback to the CPU about arithmetic and logical results.
Conclusion:
The Status Register plays a crucial role in decision-making within the CPU, influencing how the processor
responds to operation results and controlling the flow of program execution.
Q5.
a. Describe and differentiate between software and hardware interrupts in a computer system and explain
their working with suitable examples.   [10M]
Answer:
An interrupt is a signal that temporarily halts the normal execution of a program to give attention to a
higher-priority task. After handling the interrupt, the CPU resumes its previous task.
1. Types of Interrupts:
Interrupts are broadly classified as:
********** 7 **********
--- page 8 ---
• Hardware Interrupts
• Software Interrupts
(1) Hardware Interrupts
• Generated by external hardware devices to get the CPU’s attention.
• They are asynchronous, meaning they can occur at any time.
• Example devices: Keyboard, Disk controller, Printer, I/O ports.
Example:
•   Pressing a key on the keyboard generates an interrupt signal to the CPU to read the character.
•   In 8085, hardware interrupts include: TRAP, RST7.5, RST6.5, RST5.5, INTR.
Working:
1. Hardware sends an interrupt request signal.
2. CPU finishes the current instruction.
3. CPU disables further interrupts and jumps to a predefined Interrupt Service Routine (ISR).
4. Executes ISR, then returns to main program.
(2) Software Interrupts
• Generated by program instructions intentionally during execution.
• They are synchronous, as they occur due to program logic.
• Used for system calls, debugging, or communication with OS.
Example:
•   In 8085, RST n instructions (e.g., RST 1, RST 2) generate software interrupts.
•   In modern systems, INT n (like INT 21H in DOS) invokes operating system routines.
Working:
1. Instruction like INT 21H is executed by CPU.
2. CPU jumps to ISR defined for software interrupt number 21H.
3. After completion, CPU resumes main program.
(3) Difference Between Hardware and Software Interrupts
Aspect   Hardware Interrupt   Software Interrupt
Source   External hardware device Internal instruction in program
Nature Asynchronous   Synchronous
Purpose Handle external events   Perform system-level functions
Example Keyboard input, I/O signal INT 21H, RST 5
********** 8 **********
--- page 9 ---
Aspect   Hardware Interrupt   Software Interrupt
Priority Usually fixed   Defined by software design
Control CPU-controlled signal line Triggered by executing instruction
Conclusion:
Both hardware and software interrupts are essential for efficient CPU operation — hardware interrupts
manage real-time external events, while software interrupts manage system and program-level services.
b. Explain the main elements of a machine instruction in detail, describing the role of each field with suitable
examples   [10M]
Answer:
A machine instruction is a binary-coded operation that tells the CPU what action to perform and on
which data.
It is the lowest-level representation of a program understandable by the processor.
1. Elements of a Machine Instruction
Element   Description   Example
Operation Code (Opcode)   Specifies the operation to be performed.   ADD, SUB, MOV, AND, etc.
Specifies the location of operands (memory,
Address Field(s)   Address like 2050H
register, or I/O).
Mode Field (Addressing   Determines how the operand’s address is   Direct, Immediate, Register
Mode)   interpreted.   modes
Specifies which register(s) are used for
Register Field(s)   Register A, B, C, etc.
operation.
Example: MVI A, 32H (32H is
Immediate Data Field   Contains data directly within the instruction.
immediate data)
Next Instruction Address   Used in branch/jump instructions to specify
JMP 2500H
Field (optional)   next instruction location.
2. Example of a Typical Machine Instruction
Example 1:
MOV A, B
• Opcode: MOV
• Source Register: B
•   Destination Register: A
• Function: Copies content of register B into A.
Example 2:
ADD M
• Opcode: ADD
• Operand: Memory location addressed by HL pair.
********** 9 **********
--- page 10 ---
• Function: Adds memory content to accumulator.
3. Instruction Format Example (8085 Microprocessor):
| Opcode (8 bits) | Operand (8 bits) |
|<------ Instruction Word (16 bits) ----->|
4. Explanation of Fields:
• Opcode Field: Defines the function (e.g., addition, subtraction).
• Operand Field: Specifies source or destination data.
• Addressing Field: Defines how operand’s address is obtained.
5. Significance:
• Enables CPU to decode and execute instructions correctly.
•   Defines interaction between processor and memory/registers.
• Helps in instruction classification (data transfer, arithmetic, control, etc.).
Conclusion:
Each machine instruction is composed of fields that specify what operation to perform, where to find
operands, and where to store results, forming the basic structure of CPU communication and execution.
Q6.
a. Explain the concept of coprocessors in a computer system, describe their role in
enhancing performance, and illustrate their working with a neat diagram.
Answer:
A coprocessor is an auxiliary processor designed to assist the main CPU in performing specialized tasks
such as mathematical computations, signal processing, or graphics operations.
1. Definition:
A coprocessor works alongside the main processor to execute specific operations faster and more
efficiently than the general-purpose CPU could perform alone.
2. Purpose:
• To reduce the CPU load by offloading complex and repetitive tasks.
• To increase computational performance for tasks like floating-point arithmetic, encryption, and
graphics rendering.
********** 10 **********
--- page 11 ---
3. Types of Coprocessors:
1. Mathematical Coprocessor (FPU):
o Performs floating-point operations.
o Example: Intel 8087 used with 8086 CPU.
2. Graphics Coprocessor (GPU):
o Handles graphical rendering and image processing tasks.
o Example: NVIDIA and AMD GPUs.
3. I/O Coprocessor:
o Manages input/output operations to reduce CPU overhead.
4. Signal Processing Coprocessor:
o Used for audio, video, and signal transformations in real-time applications.
4. Working Principle:
• The main CPU detects a special instruction meant for the coprocessor.
•   It transfers control of that instruction to the coprocessor.
• The coprocessor performs the operation and returns the result to the CPU.
6. Example:
•   In Intel 8086–8087 architecture:
o 8086 CPU performs integer operations.
o 8087 coprocessor performs floating-point arithmetic via shared instruction set.
7. Advantages:
• Improved speed and efficiency for specific operations.
•   Parallel execution between CPU and coprocessor.
•   Better system performance in scientific and multimedia applications.
Conclusion:
A coprocessor enhances the system’s performance by offloading specialized computational tasks,
allowing the CPU to focus on general processing. This design principle forms the foundation for modern
multicore and GPU-based systems.
b. Classify the types of machine instructions based on their operations, and illustrate each
category with suitable examples demonstrating their use in program execution.
********** 11 **********
--- page 12 ---
Answer:
Machine instructions can be classified according to the type of operation they perform on data. Each
instruction defines a specific operation executed by the CPU during the instruction cycle.
1. Classification of Machine Instructions:
Type of Instruction   Purpose / Operation   Example   Description
1. Data Transfer   Move data between registers, MOV A, B, LDA   Copies data from source to
Instructions   memory, and I/O devices.   2000H   destination.
2. Arithmetic   Perform arithmetic operations ADD B, SUB C,   Performs addition, subtraction,
Instructions   on data.   INR A   increment, or decrement.
Execute bitwise logical   ANA B, ORA C,   Performs AND, OR, XOR, and
3. Logical Instructions
operations.   XRA D   compare operations.
4. Branch (Control   Change sequence of program JMP 2500H, JC Jumps to another address based
Transfer) Instructions   execution.   3000H   on conditions.
Manage data transfer between IN 01H, OUT   Reads input or writes output
5. I/O Instructions
CPU and external devices.   02H   through I/O ports.
6. Shift and Rotate   Manipulate bits within   Shifts or rotates bits left or
RLC, RAR
Instructions   registers.   right.
7. Stack and Subroutine Handle data on stack or call   PUSH B, POP D, Saves data or transfers control
Instructions   subroutines.   CALL 2500H   to subprogram.
8. Machine Control   Control overall system   Stop execution, no operation,
HLT, NOP, DI, EI
Instructions   operation.   disable/enable interrupts.
3. Significance:
•   Simplifies understanding of instruction functionalities.
• Enables structured program design and efficient CPU utilization.
• Forms the base for instruction set design in microprocessors.
Conclusion:
Machine instructions are classified based on their function and operation type, helping the CPU execute
tasks systematically — from data transfer and arithmetic processing to control and I/O operations.
Q7.
a. Explain the key advantages and disadvantages of a superscalar architecture.
Answer:
A superscalar architecture allows a processor to execute multiple instructions simultaneously during
one clock cycle using multiple execution units.
********** 12 **********
--- page 13 ---
Advantages:
1. Increased Performance: Multiple instructions executed in parallel improve CPU throughput.
2. Better CPU Utilization: Efficient use of available hardware units like ALUs and FPUs.
3. Higher Instruction-Level Parallelism (ILP): Enhances speed without increasing clock frequency.
4. Reduced Execution Time: Multiple pipelines shorten total program execution time.
5. Dynamic Scheduling: Hardware can reorder instructions to reduce dependency delays.
Disadvantages:
1. Complex Hardware Design: Requires advanced instruction decoding and hazard detection.
2. Increased Power Consumption: More parallel units consume more energy.
3. Diminishing Returns: Parallelism is limited by data dependencies in instructions.
4. Higher Cost: More transistors and complex control logic increase design cost.
5. Compiler Dependency: Needs optimized instruction scheduling from compilers.
Conclusion:
Superscalar processors improve speed through parallel execution but demand complex hardware and careful
instruction scheduling.
b. Describe and compare the concepts of direct mapping and set-associative mapping in
cache memory organization with neat diagrams.
Answer:
Cache mapping defines how main memory blocks are placed into cache lines. Two common techniques
are Direct Mapping and Set-Associative Mapping.
1. Direct Mapping:
Each block of main memory is mapped to only one possible cache line.
Formula:
Cache Line = (Block Number) mod (Number of Cache Lines)
Advantages:
• Simple and fast mapping logic.
• Easy to implement.
Disadvantages:
• High conflict misses when two blocks map to the same line.
• Poor performance for certain access patterns.
2. Set-Associative Mapping:
********** 13 **********
--- page 14 ---
Memory blocks are mapped to a set of lines, and any block can be placed in any line within that set.
Example: In 2-way set associative mapping, two cache lines form one set.
Diagram:
Main Memory → Cache
Block 0 → Set 0 (Line 0 or 1)
Block 1 → Set 1 (Line 2 or 3)
Block 2 → Set 0 (Line 0 or 1)
Advantages:
• Reduced conflict misses.
•   Flexible placement policy (LRU replacement possible).
Disadvantages:
•   Slightly more complex hardware.
• Slower access than direct mapping.
3. Comparison Table:
Feature   Direct Mapping   Set-Associative Mapping
Placement   One fixed location Multiple possible locations within a set
Flexibility   Low   High
Conflict Misses High   Low
Complexity   Simple   Moderate
Speed   Fast   Slightly slower
Conclusion:
Direct mapping is simple but prone to conflicts, whereas set-associative mapping balances speed and
flexibility, offering better cache performance.
c. Explain the instruction cycle in a basic computer system.
Answer:
The instruction cycle is the process by which a computer fetches, decodes, and executes an instruction
from memory.
Stages of Instruction Cycle:
1. Fetch Cycle:
o The control unit fetches the next instruction from memory using the Program Counter (PC).
o The instruction is stored in the Instruction Register (IR).
o Example: IR ← M[PC] and PC ← PC + 1
********** 14 **********
--- page 15 ---
2. Decode Cycle:
o The instruction in IR is decoded to determine the operation to be performed and the operands
required.
3. Execute Cycle:
o The control signals are generated to perform the operation (e.g., arithmetic, logic, or memory
access).
4. Memory Access (if required):
o For load/store instructions, data is read from or written to memory.
5. Write Back:
o The result is stored back into a register or memory location.
Conclusion:
The instruction cycle ensures systematic execution of every instruction, forming the core of CPU
operation.
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper e7b5debda557

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/COMPUTER SYSTEM ARCHITECTURE/ANS_COMPUTER SYSTEM ARCHITECTURE(701EX0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: COMPUTER SYSTEM ARCHITECTURE
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Q1 is compulsory
5. Out of remaining question attempt any 4 question
6. In all total 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1. Answer Briefly:   [20 M]
a. Explain which cache replacement strategy (LRU, FIFO, or LFU) would provide a better hit ratio for the
given sequence of memory references when the cache has 4 lines, and justify your answer briefly.: 3, 4,
2, 2, 1, 4, 5, 2, 6, 7, 4, 2, 1, 2, 3, 4, 2, 1, 2, 1, 3, 4, 1, 5, 2.   [05M]
For the given sequence of memory references:
3, 4, 2, 2, 1, 4, 5, 2, 6, 7, 4, 2, 1, 2, 3, 4, 2, 1, 2, 1, 3, 4, 1, 5, 2 with cache size = 4 lines:
•   FIFO (First-In-First-Out): Replaces the oldest entry first, without considering usage
frequency.
•   LRU (Least Recently Used): Replaces the cache line that has not been used for the longest
time.
•   LFU (Least Frequently Used): Replaces the cache line used least frequently.
Result:
When the sequence is simulated, LRU achieves a higher hit ratio because it adapts better to
temporal locality — recently used data tends to be reused.
Conclusion: LRU performs better than FIFO and LFU for this reference pattern.
b. Describe the three types of instruction code formats used in a basic computer and explain their structure
and significance.   [05M]
A basic computer uses three instruction code formats:
1. Memory Reference Instruction:
o Format: [Opcode (3 bits)] [Address (12 bits)]
o Example: AND 875 (performs logical AND with memory content at address 875).
2. Register Reference Instruction:
o Format: [Opcode (3 bits)] [0] [Register Operation (12 bits)]
o Used for operations within CPU registers like CLA (Clear Accumulator).
3. Input-Output Instruction:
o Format: [Opcode (3 bits)] [1] [I/O Operation (12 bits)]
********** 1 **********
--- page 2 ---
o Used for data transfer between I/O devices and accumulator.
Significance: Enables flexibility in addressing memory, registers, and I/O devices using a compact
instruction design.
c. Compare and contrast Computer Architecture and Computer Organization by applying relevant examples
to highlight their differences in system design and functionality.   [05M]
Aspect   Computer Architecture   Computer Organization
Describes the functional behavior,   Refers to the operational structure and
Definition
instruction set, and design of a system.   physical components.
Logic design, instruction formats, addressing Hardware implementation, data transfer,
Focus
modes.   control signals.
Example   ISA design (e.g., RISC or CISC).   Control unit design, pipeline implementation.
Concerned
What system does.   How system does it.
With
Example   How Intel CPU implements instruction fetch-
Intel x86 (architecture).
System   execute cycle (organization).
✅ Conclusion: Architecture defines what a computer is capable of, while organization defines how it is
implemented.
d. Illustrate and analyze the SISD and SIMD architectures with suitable diagrams, and evaluate how they
differ in terms of data processing and instruction execution capabilities.   [05M]
1. SISD (Single Instruction Single Data):
o One control unit and one processing element.
o Executes one instruction on one data item at a time.
o Example: Traditional uniprocessor systems.
o Diagram:
o CU → PE → Memory
2. SIMD (Single Instruction Multiple Data):
o One control unit but multiple processing elements.
o Executes one instruction on multiple data items simultaneously.
o Example: Vector processors, GPUs.
o Diagram:
o CU → PE1, PE2, PE3, ... PEn → Memory
Evaluation:
• SISD is efficient for sequential tasks.
• SIMD enhances performance in data-parallel applications like image processing and matrix
operations.
✅ Conclusion: SIMD provides higher throughput for parallel data operations compared to SISD.
********** 2 **********
--- page 3 ---
Q2.
a. Explain the IAS computer model proposed by Von Neumann, highlighting its key components and the
concept of stored program architecture.   [10M]
Answer:
The IAS (Institute for Advanced Study) Computer, designed by John Von Neumann in 1946, was one
of the earliest digital computers and served as a model for most modern computer systems.
1. Von Neumann Architecture – Concept:
•   Introduced the idea of the stored program concept, where data and instructions are both stored in
the same memory.
• The computer fetches and executes instructions sequentially unless altered by control instructions.
2. Major Components of IAS Computer:
1. Memory Unit:
o Stores both instructions and data.
o Each word had 40 bits, divided into two 20-bit instructions.
2. Arithmetic Logic Unit (ALU):
o Performs arithmetic and logical operations such as addition, subtraction, AND, OR, etc.
3. Control Unit:
o Fetches, decodes, and executes instructions from memory.
o Generates control signals to coordinate operations among components.
4. Input/Output Unit:
o Used for reading data into memory and writing results out from memory.
5. Registers (in Control Unit):
o Memory Buffer Register (MBR): Holds data read or written to memory.
o Memory Address Register (MAR): Holds the address of data or instruction.
o Instruction Register (IR): Holds the current instruction being executed.
o Accumulator (AC): Temporarily stores arithmetic results.
o Program Counter (PC): Holds address of next instruction to be executed.
b. Discuss the classification of computer instructions in detail and illustrate each category with suitable
examples showing their application in program execution.   [10M]
Answer:
Computer instructions are classified based on their operation type and purpose. Each instruction tells
the CPU what operation to perform and on which data.
1. Classification of Instructions:
Type   Purpose   Example   Explanation
Move data between registers,   Copies content of register B
1. Data Transfer Instructions   MOV A, B
memory, and I/O.   into A.
Adds contents of A and B;
2. Arithmetic Instructions   Perform mathematical operations. ADD A, B
result stored in A.
Perform bitwise logical   Performs logical AND
3. Logical Instructions   AND A, B
operations.   between A and B.
4. Branch or Control Transfer Change the sequence of   Jumps to address 2050 for
JMP 2050
Instructions   execution.   next instruction.
********** 3 **********
--- page 4 ---
Type   Purpose   Example   Explanation
Enable data transfer between CPU IN 01H, OUT Input from or output to
5. Input/Output Instructions
and peripherals.   02H   device ports.
6. Shift and Rotate   Rotates accumulator bits left
Shift or rotate bits in registers.   RLC A
Instructions   through carry.
7. Compare and Test   Compare data values or check   Compares A and B; sets flags
CMP A, B
Instructions   conditions.   accordingly.
PUSH B, POP Save and restore register data
8. Stack Instructions   Manage data using stack memory.
C   using stack.
2. Example Program:
Example to add two numbers stored in memory:
MOV A, [2000H]
ADD A, [2001H]
MOV [2002H], A
HLT
• Fetch data from 2000H and 2001H.
• Perform addition.
•   Store result at 2002H.
Q3.
a. Identify and explain the essential characteristics that define a computer memory system, highlighting their
role in system performance.   [10M]
Answer:
A computer memory system is responsible for storing data and instructions required for processing.
The performance of a computer greatly depends on how efficiently the memory system operates.
Key Characteristics of Memory Systems:
1. Storage Capacity:
o Defines how much data or number of instructions the memory can hold.
o Measured in bytes, kilobytes, megabytes, gigabytes, etc.
o Example: 8 GB RAM, 512 GB SSD.
2. Access Time (Speed):
o Time required to read or write data from/to memory.
o Faster access time leads to better system performance.
o Cache memory has the lowest access time; secondary storage has the highest.
3. Memory Cycle Time:
o The total time required to complete one read/write operation and prepare for the next.
o Determines how quickly consecutive operations can be executed.
4. Cost per Bit:
o Memory is designed by balancing cost and performance.
o Faster memories (like cache, registers) are expensive per bit compared to slower ones
(like hard disks).
5. Volatility:
o Determines whether the memory retains data when power is turned off.
o Volatile: RAM (data lost when power off)
o Non-Volatile: ROM, Flash, HDD.
6. Physical Size (Density):
o Refers to the amount of memory stored per unit area on a chip.
********** 4 **********
--- page 5 ---
o Higher density allows more storage in less space.
7. Organization (Hierarchy):
o Memory is organized in levels: Registers → Cache → Main Memory → Secondary
Memory → Tertiary Storage.
o Balances speed, cost, and capacity.
b. Describe the concept of a micro-programmed control unit, and explain how it functions in the execution of
control signals using microinstructions.   [10M]
Answer:
The micro-programmed control unit is a type of control unit in which the control signals required for
instruction execution are generated by microinstructions stored in a control memory.
1. Concept:
•   Instead of hardwiring the control signals, they are stored as microprograms in a control store
(ROM).
• Each machine instruction is implemented by a sequence of microinstructions forming a
microprogram.
2. Components of Micro-programmed Control Unit:
1. Control Memory (CM):
Stores the microinstructions that define the control signals for each CPU operation.
2. Control Address Register (CAR):
Holds the address of the next microinstruction to be fetched.
3. Control Data Register (CDR):
Holds the microinstruction fetched from the control memory.
4. Microinstruction Decoder:
Decodes the microinstruction and generates appropriate control signals.
5. Sequencing Logic:
Determines the address of the next microinstruction (sequential or branch).
3. Working Principle:
• The Instruction Register (IR) holds the instruction fetched from main memory.
• The microprogram sequencer uses the opcode from IR to select the starting address of the
corresponding microprogram.
• Each microinstruction specifies control signals to perform operations like ALU function, data
movement, or memory access.
•   After executing one microinstruction, control moves to the next one until the instruction cycle
completes.
********** 5 **********
--- page 6 ---
Q4.
a. Define and describe the concept of Superscalar Architecture, outlining its main features and advantages in
modern processors.   [10M]
A Superscalar Architecture is a type of CPU design that allows multiple instructions to be issued and
executed simultaneously during a single clock cycle.
1. Definition:
• A superscalar processor contains multiple execution units (such as ALU, FPU, Load/Store units)
to perform parallel instruction execution.
•   It increases instruction-level parallelism (ILP) without requiring changes in the program itself.
2. Key Features:
1. Multiple Pipelines:
o Processor can fetch, decode, and execute multiple instructions in parallel.
o Example: Dual or Quad pipeline processors.
2. Instruction Dispatch and Scheduling:
o Uses a dynamic instruction scheduling mechanism to assign instructions to available
execution units.
3. Out-of-Order Execution:
o   Instructions can execute as soon as operands are available, even if earlier instructions are still
running.
4. Register Renaming:
o Avoids data hazards by using different physical registers for temporary results.
5. Branch Prediction:
o Predicts instruction flow to keep the pipelines full and reduce stalls.
4. Advantages:
• Higher instruction throughput.
•   Better CPU utilization.
• Improved performance for independent instructions.
5. Disadvantages:
• Complex hardware design.
•   Inefficient for programs with strong data dependencies.
b. Explain the purpose and functioning of a Status Register in a CPU, and discuss how its flags assist in
instruction execution.   [10M]
Answer:
The Status Register, also known as the Program Status Word (PSW) or Flag Register, is a special
register in the CPU that indicates the outcome of arithmetic or logical operations and controls the
processor’s operation flow.
1. Purpose:
•   Stores flag bits that represent the status of the processor after an operation.
• Used by conditional branch and control instructions to make execution decisions.
********** 6 **********
--- page 7 ---
2. Common Flags in Status Register:
Flag Name   Symbol   Meaning / Condition
Set if there is a carry out from MSB during addition or borrow during
Carry Flag   C
subtraction.
Zero Flag   Z   Set if the result of an operation is zero.
Sign Flag   S   Reflects the sign of the result (1 for negative, 0 for positive).
Overflow Flag   O / V   Set when arithmetic overflow occurs (result exceeds range).
Parity Flag   P   Set if number of 1s in result is even.
Auxiliary Carry
AC   Used in BCD arithmetic operations.
Flag
Interrupt Flag   I   Enables or disables CPU interrupt recognition.
3. Working Example:
Example instruction:
MOV A, 05H
ADD A, 0BH
•   Result = 10H
• Carry Flag (C) = 0 (no carry)
• Zero Flag (Z) = 0 (result not zero)
• Sign Flag (S) = 0 (positive result)
If instruction was:
SUB A, A
Then Result = 0 → Z = 1 (Zero flag set).
4. Importance in Execution:
• Used in conditional branching (e.g., JZ, JC, JNZ) to control program flow.
•   Provides feedback to the CPU about arithmetic and logical results.
Conclusion:
The Status Register plays a crucial role in decision-making within the CPU, influencing how the processor
responds to operation results and controlling the flow of program execution.
Q5.
a. Describe and differentiate between software and hardware interrupts in a computer system and explain
their working with suitable examples.   [10M]
Answer:
An interrupt is a signal that temporarily halts the normal execution of a program to give attention to a
higher-priority task. After handling the interrupt, the CPU resumes its previous task.
1. Types of Interrupts:
Interrupts are broadly classified as:
********** 7 **********
--- page 8 ---
• Hardware Interrupts
• Software Interrupts
(1) Hardware Interrupts
• Generated by external hardware devices to get the CPU’s attention.
• They are asynchronous, meaning they can occur at any time.
• Example devices: Keyboard, Disk controller, Printer, I/O ports.
Example:
•   Pressing a key on the keyboard generates an interrupt signal to the CPU to read the character.
•   In 8085, hardware interrupts include: TRAP, RST7.5, RST6.5, RST5.5, INTR.
Working:
1. Hardware sends an interrupt request signal.
2. CPU finishes the current instruction.
3. CPU disables further interrupts and jumps to a predefined Interrupt Service Routine (ISR).
4. Executes ISR, then returns to main program.
(2) Software Interrupts
• Generated by program instructions intentionally during execution.
• They are synchronous, as they occur due to program logic.
• Used for system calls, debugging, or communication with OS.
Example:
•   In 8085, RST n instructions (e.g., RST 1, RST 2) generate software interrupts.
•   In modern systems, INT n (like INT 21H in DOS) invokes operating system routines.
Working:
1. Instruction like INT 21H is executed by CPU.
2. CPU jumps to ISR defined for software interrupt number 21H.
3. After completion, CPU resumes main program.
(3) Difference Between Hardware and Software Interrupts
Aspect   Hardware Interrupt   Software Interrupt
Source   External hardware device Internal instruction in program
Nature Asynchronous   Synchronous
Purpose Handle external events   Perform system-level functions
Example Keyboard input, I/O signal INT 21H, RST 5
********** 8 **********
--- page 9 ---
Aspect   Hardware Interrupt   Software Interrupt
Priority Usually fixed   Defined by software design
Control CPU-controlled signal line Triggered by executing instruction
Conclusion:
Both hardware and software interrupts are essential for efficient CPU operation — hardware interrupts
manage real-time external events, while software interrupts manage system and program-level services.
b. Explain the main elements of a machine instruction in detail, describing the role of each field with suitable
examples   [10M]
Answer:
A machine instruction is a binary-coded operation that tells the CPU what action to perform and on
which data.
It is the lowest-level representation of a program understandable by the processor.
1. Elements of a Machine Instruction
Element   Description   Example
Operation Code (Opcode)   Specifies the operation to be performed.   ADD, SUB, MOV, AND, etc.
Specifies the location of operands (memory,
Address Field(s)   Address like 2050H
register, or I/O).
Mode Field (Addressing   Determines how the operand’s address is   Direct, Immediate, Register
Mode)   interpreted.   modes
Specifies which register(s) are used for
Register Field(s)   Register A, B, C, etc.
operation.
Example: MVI A, 32H (32H is
Immediate Data Field   Contains data directly within the instruction.
immediate data)
Next Instruction Address   Used in branch/jump instructions to specify
JMP 2500H
Field (optional)   next instruction location.
2. Example of a Typical Machine Instruction
Example 1:
MOV A, B
• Opcode: MOV
• Source Register: B
•   Destination Register: A
• Function: Copies content of register B into A.
Example 2:
ADD M
• Opcode: ADD
• Operand: Memory location addressed by HL pair.
********** 9 **********
--- page 10 ---
• Function: Adds memory content to accumulator.
3. Instruction Format Example (8085 Microprocessor):
| Opcode (8 bits) | Operand (8 bits) |
|<------ Instruction Word (16 bits) ----->|
4. Explanation of Fields:
• Opcode Field: Defines the function (e.g., addition, subtraction).
• Operand Field: Specifies source or destination data.
• Addressing Field: Defines how operand’s address is obtained.
5. Significance:
• Enables CPU to decode and execute instructions correctly.
•   Defines interaction between processor and memory/registers.
• Helps in instruction classification (data transfer, arithmetic, control, etc.).
Conclusion:
Each machine instruction is composed of fields that specify what operation to perform, where to find
operands, and where to store results, forming the basic structure of CPU communication and execution.
Q6.
a. Explain the concept of coprocessors in a computer system, describe their role in
enhancing performance, and illustrate their working with a neat diagram.
Answer:
A coprocessor is an auxiliary processor designed to assist the main CPU in performing specialized tasks
such as mathematical computations, signal processing, or graphics operations.
1. Definition:
A coprocessor works alongside the main processor to execute specific operations faster and more
efficiently than the general-purpose CPU could perform alone.
2. Purpose:
• To reduce the CPU load by offloading complex and repetitive tasks.
• To increase computational performance for tasks like floating-point arithmetic, encryption, and
graphics rendering.
********** 10 **********
--- page 11 ---
3. Types of Coprocessors:
1. Mathematical Coprocessor (FPU):
o Performs floating-point operations.
o Example: Intel 8087 used with 8086 CPU.
2. Graphics Coprocessor (GPU):
o Handles graphical rendering and image processing tasks.
o Example: NVIDIA and AMD GPUs.
3. I/O Coprocessor:
o Manages input/output operations to reduce CPU overhead.
4. Signal Processing Coprocessor:
o Used for audio, video, and signal transformations in real-time applications.
4. Working Principle:
• The main CPU detects a special instruction meant for the coprocessor.
•   It transfers control of that instruction to the coprocessor.
• The coprocessor performs the operation and returns the result to the CPU.
6. Example:
•   In Intel 8086–8087 architecture:
o 8086 CPU performs integer operations.
o 8087 coprocessor performs floating-point arithmetic via shared instruction set.
7. Advantages:
• Improved speed and efficiency for specific operations.
•   Parallel execution between CPU and coprocessor.
•   Better system performance in scientific and multimedia applications.
Conclusion:
A coprocessor enhances the system’s performance by offloading specialized computational tasks,
allowing the CPU to focus on general processing. This design principle forms the foundation for modern
multicore and GPU-based systems.
b. Classify the types of machine instructions based on their operations, and illustrate each
category with suitable examples demonstrating their use in program execution.
********** 11 **********
--- page 12 ---
Answer:
Machine instructions can be classified according to the type of operation they perform on data. Each
instruction defines a specific operation executed by the CPU during the instruction cycle.
1. Classification of Machine Instructions:
Type of Instruction   Purpose / Operation   Example   Description
1. Data Transfer   Move data between registers, MOV A, B, LDA   Copies data from source to
Instructions   memory, and I/O devices.   2000H   destination.
2. Arithmetic   Perform arithmetic operations ADD B, SUB C,   Performs addition, subtraction,
Instructions   on data.   INR A   increment, or decrement.
Execute bitwise logical   ANA B, ORA C,   Performs AND, OR, XOR, and
3. Logical Instructions
operations.   XRA D   compare operations.
4. Branch (Control   Change sequence of program JMP 2500H, JC Jumps to another address based
Transfer) Instructions   execution.   3000H   on conditions.
Manage data transfer between IN 01H, OUT   Reads input or writes output
5. I/O Instructions
CPU and external devices.   02H   through I/O ports.
6. Shift and Rotate   Manipulate bits within   Shifts or rotates bits left or
RLC, RAR
Instructions   registers.   right.
7. Stack and Subroutine Handle data on stack or call   PUSH B, POP D, Saves data or transfers control
Instructions   subroutines.   CALL 2500H   to subprogram.
8. Machine Control   Control overall system   Stop execution, no operation,
HLT, NOP, DI, EI
Instructions   operation.   disable/enable interrupts.
3. Significance:
•   Simplifies understanding of instruction functionalities.
• Enables structured program design and efficient CPU utilization.
• Forms the base for instruction set design in microprocessors.
Conclusion:
Machine instructions are classified based on their function and operation type, helping the CPU execute
tasks systematically — from data transfer and arithmetic processing to control and I/O operations.
Q7.
a. Explain the key advantages and disadvantages of a superscalar architecture.
Answer:
A superscalar architecture allows a processor to execute multiple instructions simultaneously during
one clock cycle using multiple execution units.
********** 12 **********
--- page 13 ---
Advantages:
1. Increased Performance: Multiple instructions executed in parallel improve CPU throughput.
2. Better CPU Utilization: Efficient use of available hardware units like ALUs and FPUs.
3. Higher Instruction-Level Parallelism (ILP): Enhances speed without increasing clock frequency.
4. Reduced Execution Time: Multiple pipelines shorten total program execution time.
5. Dynamic Scheduling: Hardware can reorder instructions to reduce dependency delays.
Disadvantages:
1. Complex Hardware Design: Requires advanced instruction decoding and hazard detection.
2. Increased Power Consumption: More parallel units consume more energy.
3. Diminishing Returns: Parallelism is limited by data dependencies in instructions.
4. Higher Cost: More transistors and complex control logic increase design cost.
5. Compiler Dependency: Needs optimized instruction scheduling from compilers.
Conclusion:
Superscalar processors improve speed through parallel execution but demand complex hardware and careful
instruction scheduling.
b. Describe and compare the concepts of direct mapping and set-associative mapping in
cache memory organization with neat diagrams.
Answer:
Cache mapping defines how main memory blocks are placed into cache lines. Two common techniques
are Direct Mapping and Set-Associative Mapping.
1. Direct Mapping:
Each block of main memory is mapped to only one possible cache line.
Formula:
Cache Line = (Block Number) mod (Number of Cache Lines)
Advantages:
• Simple and fast mapping logic.
• Easy to implement.
Disadvantages:
• High conflict misses when two blocks map to the same line.
• Poor performance for certain access patterns.
2. Set-Associative Mapping:
********** 13 **********
--- page 14 ---
Memory blocks are mapped to a set of lines, and any block can be placed in any line within that set.
Example: In 2-way set associative mapping, two cache lines form one set.
Diagram:
Main Memory → Cache
Block 0 → Set 0 (Line 0 or 1)
Block 1 → Set 1 (Line 2 or 3)
Block 2 → Set 0 (Line 0 or 1)
Advantages:
• Reduced conflict misses.
•   Flexible placement policy (LRU replacement possible).
Disadvantages:
•   Slightly more complex hardware.
• Slower access than direct mapping.
3. Comparison Table:
Feature   Direct Mapping   Set-Associative Mapping
Placement   One fixed location Multiple possible locations within a set
Flexibility   Low   High
Conflict Misses High   Low
Complexity   Simple   Moderate
Speed   Fast   Slightly slower
Conclusion:
Direct mapping is simple but prone to conflicts, whereas set-associative mapping balances speed and
flexibility, offering better cache performance.
c. Explain the instruction cycle in a basic computer system.
Answer:
The instruction cycle is the process by which a computer fetches, decodes, and executes an instruction
from memory.
Stages of Instruction Cycle:
1. Fetch Cycle:
o The control unit fetches the next instruction from memory using the Program Counter (PC).
o The instruction is stored in the Instruction Register (IR).
o Example: IR ← M[PC] and PC ← PC + 1
********** 14 **********
--- page 15 ---
2. Decode Cycle:
o The instruction in IR is decoded to determine the operation to be performed and the operands
required.
3. Execute Cycle:
o The control signals are generated to perform the operation (e.g., arithmetic, logic, or memory
access).
4. Memory Access (if required):
o For load/store instructions, data is read from or written to memory.
5. Write Back:
o The result is stored back into a register or memory location.
Conclusion:
The instruction cycle ensures systematic execution of every instruction, forming the core of CPU
operation.
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 7fadea7158b2

- Departments: Information Technology
- Programmes: DIPLOMA IN INFORMATION TECHNOLOGY - 7075
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/DIPLOMA IN INFORMATION TECHNOLOGY - 7075/COMPUTER SYSTEM ARCHITECTURE/ANS_COMPUTER SYSTEM ARCHITECTURE(701EX0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: COMPUTER SYSTEM ARCHITECTURE
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Q1 is compulsory
5. Out of remaining question attempt any 4 question
6. In all total 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1. Answer Briefly:   [20 M]
a. Explain which cache replacement strategy (LRU, FIFO, or LFU) would provide a better hit ratio for the
given sequence of memory references when the cache has 4 lines, and justify your answer briefly.: 3, 4,
2, 2, 1, 4, 5, 2, 6, 7, 4, 2, 1, 2, 3, 4, 2, 1, 2, 1, 3, 4, 1, 5, 2.   [05M]
For the given sequence of memory references:
3, 4, 2, 2, 1, 4, 5, 2, 6, 7, 4, 2, 1, 2, 3, 4, 2, 1, 2, 1, 3, 4, 1, 5, 2 with cache size = 4 lines:
•   FIFO (First-In-First-Out): Replaces the oldest entry first, without considering usage
frequency.
•   LRU (Least Recently Used): Replaces the cache line that has not been used for the longest
time.
•   LFU (Least Frequently Used): Replaces the cache line used least frequently.
Result:
When the sequence is simulated, LRU achieves a higher hit ratio because it adapts better to
temporal locality — recently used data tends to be reused.
Conclusion: LRU performs better than FIFO and LFU for this reference pattern.
b. Describe the three types of instruction code formats used in a basic computer and explain their structure
and significance.   [05M]
A basic computer uses three instruction code formats:
1. Memory Reference Instruction:
o Format: [Opcode (3 bits)] [Address (12 bits)]
o Example: AND 875 (performs logical AND with memory content at address 875).
2. Register Reference Instruction:
o Format: [Opcode (3 bits)] [0] [Register Operation (12 bits)]
o Used for operations within CPU registers like CLA (Clear Accumulator).
3. Input-Output Instruction:
o Format: [Opcode (3 bits)] [1] [I/O Operation (12 bits)]
********** 1 **********
--- page 2 ---
o Used for data transfer between I/O devices and accumulator.
Significance: Enables flexibility in addressing memory, registers, and I/O devices using a compact
instruction design.
c. Compare and contrast Computer Architecture and Computer Organization by applying relevant examples
to highlight their differences in system design and functionality.   [05M]
Aspect   Computer Architecture   Computer Organization
Describes the functional behavior,   Refers to the operational structure and
Definition
instruction set, and design of a system.   physical components.
Logic design, instruction formats, addressing Hardware implementation, data transfer,
Focus
modes.   control signals.
Example   ISA design (e.g., RISC or CISC).   Control unit design, pipeline implementation.
Concerned
What system does.   How system does it.
With
Example   How Intel CPU implements instruction fetch-
Intel x86 (architecture).
System   execute cycle (organization).
✅ Conclusion: Architecture defines what a computer is capable of, while organization defines how it is
implemented.
d. Illustrate and analyze the SISD and SIMD architectures with suitable diagrams, and evaluate how they
differ in terms of data processing and instruction execution capabilities.   [05M]
1. SISD (Single Instruction Single Data):
o One control unit and one processing element.
o Executes one instruction on one data item at a time.
o Example: Traditional uniprocessor systems.
o Diagram:
o CU → PE → Memory
2. SIMD (Single Instruction Multiple Data):
o One control unit but multiple processing elements.
o Executes one instruction on multiple data items simultaneously.
o Example: Vector processors, GPUs.
o Diagram:
o CU → PE1, PE2, PE3, ... PEn → Memory
Evaluation:
• SISD is efficient for sequential tasks.
• SIMD enhances performance in data-parallel applications like image processing and matrix
operations.
✅ Conclusion: SIMD provides higher throughput for parallel data operations compared to SISD.
********** 2 **********
--- page 3 ---
Q2.
a. Explain the IAS computer model proposed by Von Neumann, highlighting its key components and the
concept of stored program architecture.   [10M]
Answer:
The IAS (Institute for Advanced Study) Computer, designed by John Von Neumann in 1946, was one
of the earliest digital computers and served as a model for most modern computer systems.
1. Von Neumann Architecture – Concept:
•   Introduced the idea of the stored program concept, where data and instructions are both stored in
the same memory.
• The computer fetches and executes instructions sequentially unless altered by control instructions.
2. Major Components of IAS Computer:
1. Memory Unit:
o Stores both instructions and data.
o Each word had 40 bits, divided into two 20-bit instructions.
2. Arithmetic Logic Unit (ALU):
o Performs arithmetic and logical operations such as addition, subtraction, AND, OR, etc.
3. Control Unit:
o Fetches, decodes, and executes instructions from memory.
o Generates control signals to coordinate operations among components.
4. Input/Output Unit:
o Used for reading data into memory and writing results out from memory.
5. Registers (in Control Unit):
o Memory Buffer Register (MBR): Holds data read or written to memory.
o Memory Address Register (MAR): Holds the address of data or instruction.
o Instruction Register (IR): Holds the current instruction being executed.
o Accumulator (AC): Temporarily stores arithmetic results.
o Program Counter (PC): Holds address of next instruction to be executed.
b. Discuss the classification of computer instructions in detail and illustrate each category with suitable
examples showing their application in program execution.   [10M]
Answer:
Computer instructions are classified based on their operation type and purpose. Each instruction tells
the CPU what operation to perform and on which data.
1. Classification of Instructions:
Type   Purpose   Example   Explanation
Move data between registers,   Copies content of register B
1. Data Transfer Instructions   MOV A, B
memory, and I/O.   into A.
Adds contents of A and B;
2. Arithmetic Instructions   Perform mathematical operations. ADD A, B
result stored in A.
Perform bitwise logical   Performs logical AND
3. Logical Instructions   AND A, B
operations.   between A and B.
4. Branch or Control Transfer Change the sequence of   Jumps to address 2050 for
JMP 2050
Instructions   execution.   next instruction.
********** 3 **********
--- page 4 ---
Type   Purpose   Example   Explanation
Enable data transfer between CPU IN 01H, OUT Input from or output to
5. Input/Output Instructions
and peripherals.   02H   device ports.
6. Shift and Rotate   Rotates accumulator bits left
Shift or rotate bits in registers.   RLC A
Instructions   through carry.
7. Compare and Test   Compare data values or check   Compares A and B; sets flags
CMP A, B
Instructions   conditions.   accordingly.
PUSH B, POP Save and restore register data
8. Stack Instructions   Manage data using stack memory.
C   using stack.
2. Example Program:
Example to add two numbers stored in memory:
MOV A, [2000H]
ADD A, [2001H]
MOV [2002H], A
HLT
• Fetch data from 2000H and 2001H.
• Perform addition.
•   Store result at 2002H.
Q3.
a. Identify and explain the essential characteristics that define a computer memory system, highlighting their
role in system performance.   [10M]
Answer:
A computer memory system is responsible for storing data and instructions required for processing.
The performance of a computer greatly depends on how efficiently the memory system operates.
Key Characteristics of Memory Systems:
1. Storage Capacity:
o Defines how much data or number of instructions the memory can hold.
o Measured in bytes, kilobytes, megabytes, gigabytes, etc.
o Example: 8 GB RAM, 512 GB SSD.
2. Access Time (Speed):
o Time required to read or write data from/to memory.
o Faster access time leads to better system performance.
o Cache memory has the lowest access time; secondary storage has the highest.
3. Memory Cycle Time:
o The total time required to complete one read/write operation and prepare for the next.
o Determines how quickly consecutive operations can be executed.
4. Cost per Bit:
o Memory is designed by balancing cost and performance.
o Faster memories (like cache, registers) are expensive per bit compared to slower ones
(like hard disks).
5. Volatility:
o Determines whether the memory retains data when power is turned off.
o Volatile: RAM (data lost when power off)
o Non-Volatile: ROM, Flash, HDD.
6. Physical Size (Density):
o Refers to the amount of memory stored per unit area on a chip.
********** 4 **********
--- page 5 ---
o Higher density allows more storage in less space.
7. Organization (Hierarchy):
o Memory is organized in levels: Registers → Cache → Main Memory → Secondary
Memory → Tertiary Storage.
o Balances speed, cost, and capacity.
b. Describe the concept of a micro-programmed control unit, and explain how it functions in the execution of
control signals using microinstructions.   [10M]
Answer:
The micro-programmed control unit is a type of control unit in which the control signals required for
instruction execution are generated by microinstructions stored in a control memory.
1. Concept:
•   Instead of hardwiring the control signals, they are stored as microprograms in a control store
(ROM).
• Each machine instruction is implemented by a sequence of microinstructions forming a
microprogram.
2. Components of Micro-programmed Control Unit:
1. Control Memory (CM):
Stores the microinstructions that define the control signals for each CPU operation.
2. Control Address Register (CAR):
Holds the address of the next microinstruction to be fetched.
3. Control Data Register (CDR):
Holds the microinstruction fetched from the control memory.
4. Microinstruction Decoder:
Decodes the microinstruction and generates appropriate control signals.
5. Sequencing Logic:
Determines the address of the next microinstruction (sequential or branch).
3. Working Principle:
• The Instruction Register (IR) holds the instruction fetched from main memory.
• The microprogram sequencer uses the opcode from IR to select the starting address of the
corresponding microprogram.
• Each microinstruction specifies control signals to perform operations like ALU function, data
movement, or memory access.
•   After executing one microinstruction, control moves to the next one until the instruction cycle
completes.
********** 5 **********
--- page 6 ---
Q4.
a. Define and describe the concept of Superscalar Architecture, outlining its main features and advantages in
modern processors.   [10M]
A Superscalar Architecture is a type of CPU design that allows multiple instructions to be issued and
executed simultaneously during a single clock cycle.
1. Definition:
• A superscalar processor contains multiple execution units (such as ALU, FPU, Load/Store units)
to perform parallel instruction execution.
•   It increases instruction-level parallelism (ILP) without requiring changes in the program itself.
2. Key Features:
1. Multiple Pipelines:
o Processor can fetch, decode, and execute multiple instructions in parallel.
o Example: Dual or Quad pipeline processors.
2. Instruction Dispatch and Scheduling:
o Uses a dynamic instruction scheduling mechanism to assign instructions to available
execution units.
3. Out-of-Order Execution:
o   Instructions can execute as soon as operands are available, even if earlier instructions are still
running.
4. Register Renaming:
o Avoids data hazards by using different physical registers for temporary results.
5. Branch Prediction:
o Predicts instruction flow to keep the pipelines full and reduce stalls.
4. Advantages:
• Higher instruction throughput.
•   Better CPU utilization.
• Improved performance for independent instructions.
5. Disadvantages:
• Complex hardware design.
•   Inefficient for programs with strong data dependencies.
b. Explain the purpose and functioning of a Status Register in a CPU, and discuss how its flags assist in
instruction execution.   [10M]
Answer:
The Status Register, also known as the Program Status Word (PSW) or Flag Register, is a special
register in the CPU that indicates the outcome of arithmetic or logical operations and controls the
processor’s operation flow.
1. Purpose:
•   Stores flag bits that represent the status of the processor after an operation.
• Used by conditional branch and control instructions to make execution decisions.
********** 6 **********
--- page 7 ---
2. Common Flags in Status Register:
Flag Name   Symbol   Meaning / Condition
Set if there is a carry out from MSB during addition or borrow during
Carry Flag   C
subtraction.
Zero Flag   Z   Set if the result of an operation is zero.
Sign Flag   S   Reflects the sign of the result (1 for negative, 0 for positive).
Overflow Flag   O / V   Set when arithmetic overflow occurs (result exceeds range).
Parity Flag   P   Set if number of 1s in result is even.
Auxiliary Carry
AC   Used in BCD arithmetic operations.
Flag
Interrupt Flag   I   Enables or disables CPU interrupt recognition.
3. Working Example:
Example instruction:
MOV A, 05H
ADD A, 0BH
•   Result = 10H
• Carry Flag (C) = 0 (no carry)
• Zero Flag (Z) = 0 (result not zero)
• Sign Flag (S) = 0 (positive result)
If instruction was:
SUB A, A
Then Result = 0 → Z = 1 (Zero flag set).
4. Importance in Execution:
• Used in conditional branching (e.g., JZ, JC, JNZ) to control program flow.
•   Provides feedback to the CPU about arithmetic and logical results.
Conclusion:
The Status Register plays a crucial role in decision-making within the CPU, influencing how the processor
responds to operation results and controlling the flow of program execution.
Q5.
a. Describe and differentiate between software and hardware interrupts in a computer system and explain
their working with suitable examples.   [10M]
Answer:
An interrupt is a signal that temporarily halts the normal execution of a program to give attention to a
higher-priority task. After handling the interrupt, the CPU resumes its previous task.
1. Types of Interrupts:
Interrupts are broadly classified as:
********** 7 **********
--- page 8 ---
• Hardware Interrupts
• Software Interrupts
(1) Hardware Interrupts
• Generated by external hardware devices to get the CPU’s attention.
• They are asynchronous, meaning they can occur at any time.
• Example devices: Keyboard, Disk controller, Printer, I/O ports.
Example:
•   Pressing a key on the keyboard generates an interrupt signal to the CPU to read the character.
•   In 8085, hardware interrupts include: TRAP, RST7.5, RST6.5, RST5.5, INTR.
Working:
1. Hardware sends an interrupt request signal.
2. CPU finishes the current instruction.
3. CPU disables further interrupts and jumps to a predefined Interrupt Service Routine (ISR).
4. Executes ISR, then returns to main program.
(2) Software Interrupts
• Generated by program instructions intentionally during execution.
• They are synchronous, as they occur due to program logic.
• Used for system calls, debugging, or communication with OS.
Example:
•   In 8085, RST n instructions (e.g., RST 1, RST 2) generate software interrupts.
•   In modern systems, INT n (like INT 21H in DOS) invokes operating system routines.
Working:
1. Instruction like INT 21H is executed by CPU.
2. CPU jumps to ISR defined for software interrupt number 21H.
3. After completion, CPU resumes main program.
(3) Difference Between Hardware and Software Interrupts
Aspect   Hardware Interrupt   Software Interrupt
Source   External hardware device Internal instruction in program
Nature Asynchronous   Synchronous
Purpose Handle external events   Perform system-level functions
Example Keyboard input, I/O signal INT 21H, RST 5
********** 8 **********
--- page 9 ---
Aspect   Hardware Interrupt   Software Interrupt
Priority Usually fixed   Defined by software design
Control CPU-controlled signal line Triggered by executing instruction
Conclusion:
Both hardware and software interrupts are essential for efficient CPU operation — hardware interrupts
manage real-time external events, while software interrupts manage system and program-level services.
b. Explain the main elements of a machine instruction in detail, describing the role of each field with suitable
examples   [10M]
Answer:
A machine instruction is a binary-coded operation that tells the CPU what action to perform and on
which data.
It is the lowest-level representation of a program understandable by the processor.
1. Elements of a Machine Instruction
Element   Description   Example
Operation Code (Opcode)   Specifies the operation to be performed.   ADD, SUB, MOV, AND, etc.
Specifies the location of operands (memory,
Address Field(s)   Address like 2050H
register, or I/O).
Mode Field (Addressing   Determines how the operand’s address is   Direct, Immediate, Register
Mode)   interpreted.   modes
Specifies which register(s) are used for
Register Field(s)   Register A, B, C, etc.
operation.
Example: MVI A, 32H (32H is
Immediate Data Field   Contains data directly within the instruction.
immediate data)
Next Instruction Address   Used in branch/jump instructions to specify
JMP 2500H
Field (optional)   next instruction location.
2. Example of a Typical Machine Instruction
Example 1:
MOV A, B
• Opcode: MOV
• Source Register: B
•   Destination Register: A
• Function: Copies content of register B into A.
Example 2:
ADD M
• Opcode: ADD
• Operand: Memory location addressed by HL pair.
********** 9 **********
--- page 10 ---
• Function: Adds memory content to accumulator.
3. Instruction Format Example (8085 Microprocessor):
| Opcode (8 bits) | Operand (8 bits) |
|<------ Instruction Word (16 bits) ----->|
4. Explanation of Fields:
• Opcode Field: Defines the function (e.g., addition, subtraction).
• Operand Field: Specifies source or destination data.
• Addressing Field: Defines how operand’s address is obtained.
5. Significance:
• Enables CPU to decode and execute instructions correctly.
•   Defines interaction between processor and memory/registers.
• Helps in instruction classification (data transfer, arithmetic, control, etc.).
Conclusion:
Each machine instruction is composed of fields that specify what operation to perform, where to find
operands, and where to store results, forming the basic structure of CPU communication and execution.
Q6.
a. Explain the concept of coprocessors in a computer system, describe their role in
enhancing performance, and illustrate their working with a neat diagram.
Answer:
A coprocessor is an auxiliary processor designed to assist the main CPU in performing specialized tasks
such as mathematical computations, signal processing, or graphics operations.
1. Definition:
A coprocessor works alongside the main processor to execute specific operations faster and more
efficiently than the general-purpose CPU could perform alone.
2. Purpose:
• To reduce the CPU load by offloading complex and repetitive tasks.
• To increase computational performance for tasks like floating-point arithmetic, encryption, and
graphics rendering.
********** 10 **********
--- page 11 ---
3. Types of Coprocessors:
1. Mathematical Coprocessor (FPU):
o Performs floating-point operations.
o Example: Intel 8087 used with 8086 CPU.
2. Graphics Coprocessor (GPU):
o Handles graphical rendering and image processing tasks.
o Example: NVIDIA and AMD GPUs.
3. I/O Coprocessor:
o Manages input/output operations to reduce CPU overhead.
4. Signal Processing Coprocessor:
o Used for audio, video, and signal transformations in real-time applications.
4. Working Principle:
• The main CPU detects a special instruction meant for the coprocessor.
•   It transfers control of that instruction to the coprocessor.
• The coprocessor performs the operation and returns the result to the CPU.
6. Example:
•   In Intel 8086–8087 architecture:
o 8086 CPU performs integer operations.
o 8087 coprocessor performs floating-point arithmetic via shared instruction set.
7. Advantages:
• Improved speed and efficiency for specific operations.
•   Parallel execution between CPU and coprocessor.
•   Better system performance in scientific and multimedia applications.
Conclusion:
A coprocessor enhances the system’s performance by offloading specialized computational tasks,
allowing the CPU to focus on general processing. This design principle forms the foundation for modern
multicore and GPU-based systems.
b. Classify the types of machine instructions based on their operations, and illustrate each
category with suitable examples demonstrating their use in program execution.
********** 11 **********
--- page 12 ---
Answer:
Machine instructions can be classified according to the type of operation they perform on data. Each
instruction defines a specific operation executed by the CPU during the instruction cycle.
1. Classification of Machine Instructions:
Type of Instruction   Purpose / Operation   Example   Description
1. Data Transfer   Move data between registers, MOV A, B, LDA   Copies data from source to
Instructions   memory, and I/O devices.   2000H   destination.
2. Arithmetic   Perform arithmetic operations ADD B, SUB C,   Performs addition, subtraction,
Instructions   on data.   INR A   increment, or decrement.
Execute bitwise logical   ANA B, ORA C,   Performs AND, OR, XOR, and
3. Logical Instructions
operations.   XRA D   compare operations.
4. Branch (Control   Change sequence of program JMP 2500H, JC Jumps to another address based
Transfer) Instructions   execution.   3000H   on conditions.
Manage data transfer between IN 01H, OUT   Reads input or writes output
5. I/O Instructions
CPU and external devices.   02H   through I/O ports.
6. Shift and Rotate   Manipulate bits within   Shifts or rotates bits left or
RLC, RAR
Instructions   registers.   right.
7. Stack and Subroutine Handle data on stack or call   PUSH B, POP D, Saves data or transfers control
Instructions   subroutines.   CALL 2500H   to subprogram.
8. Machine Control   Control overall system   Stop execution, no operation,
HLT, NOP, DI, EI
Instructions   operation.   disable/enable interrupts.
3. Significance:
•   Simplifies understanding of instruction functionalities.
• Enables structured program design and efficient CPU utilization.
• Forms the base for instruction set design in microprocessors.
Conclusion:
Machine instructions are classified based on their function and operation type, helping the CPU execute
tasks systematically — from data transfer and arithmetic processing to control and I/O operations.
Q7.
a. Explain the key advantages and disadvantages of a superscalar architecture.
Answer:
A superscalar architecture allows a processor to execute multiple instructions simultaneously during
one clock cycle using multiple execution units.
********** 12 **********
--- page 13 ---
Advantages:
1. Increased Performance: Multiple instructions executed in parallel improve CPU throughput.
2. Better CPU Utilization: Efficient use of available hardware units like ALUs and FPUs.
3. Higher Instruction-Level Parallelism (ILP): Enhances speed without increasing clock frequency.
4. Reduced Execution Time: Multiple pipelines shorten total program execution time.
5. Dynamic Scheduling: Hardware can reorder instructions to reduce dependency delays.
Disadvantages:
1. Complex Hardware Design: Requires advanced instruction decoding and hazard detection.
2. Increased Power Consumption: More parallel units consume more energy.
3. Diminishing Returns: Parallelism is limited by data dependencies in instructions.
4. Higher Cost: More transistors and complex control logic increase design cost.
5. Compiler Dependency: Needs optimized instruction scheduling from compilers.
Conclusion:
Superscalar processors improve speed through parallel execution but demand complex hardware and careful
instruction scheduling.
b. Describe and compare the concepts of direct mapping and set-associative mapping in
cache memory organization with neat diagrams.
Answer:
Cache mapping defines how main memory blocks are placed into cache lines. Two common techniques
are Direct Mapping and Set-Associative Mapping.
1. Direct Mapping:
Each block of main memory is mapped to only one possible cache line.
Formula:
Cache Line = (Block Number) mod (Number of Cache Lines)
Advantages:
• Simple and fast mapping logic.
• Easy to implement.
Disadvantages:
• High conflict misses when two blocks map to the same line.
• Poor performance for certain access patterns.
2. Set-Associative Mapping:
********** 13 **********
--- page 14 ---
Memory blocks are mapped to a set of lines, and any block can be placed in any line within that set.
Example: In 2-way set associative mapping, two cache lines form one set.
Diagram:
Main Memory → Cache
Block 0 → Set 0 (Line 0 or 1)
Block 1 → Set 1 (Line 2 or 3)
Block 2 → Set 0 (Line 0 or 1)
Advantages:
• Reduced conflict misses.
•   Flexible placement policy (LRU replacement possible).
Disadvantages:
•   Slightly more complex hardware.
• Slower access than direct mapping.
3. Comparison Table:
Feature   Direct Mapping   Set-Associative Mapping
Placement   One fixed location Multiple possible locations within a set
Flexibility   Low   High
Conflict Misses High   Low
Complexity   Simple   Moderate
Speed   Fast   Slightly slower
Conclusion:
Direct mapping is simple but prone to conflicts, whereas set-associative mapping balances speed and
flexibility, offering better cache performance.
c. Explain the instruction cycle in a basic computer system.
Answer:
The instruction cycle is the process by which a computer fetches, decodes, and executes an instruction
from memory.
Stages of Instruction Cycle:
1. Fetch Cycle:
o The control unit fetches the next instruction from memory using the Program Counter (PC).
o The instruction is stored in the Instruction Register (IR).
o Example: IR ← M[PC] and PC ← PC + 1
********** 14 **********
--- page 15 ---
2. Decode Cycle:
o The instruction in IR is decoded to determine the operation to be performed and the operands
required.
3. Execute Cycle:
o The control signals are generated to perform the operation (e.g., arithmetic, logic, or memory
access).
4. Memory Access (if required):
o For load/store instructions, data is read from or written to memory.
5. Write Back:
o The result is stored back into a register or memory location.
Conclusion:
The instruction cycle ensures systematic execution of every instruction, forming the core of CPU
operation.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper f04f4aa0381d

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/COMPUTER SYSTEM ARCHITECTURE/ANS_COMPUTER SYSTEM ARCHITECTURE(701EX0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER SYSTEM ARCHITECTURE
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Q1 is compulsory
5. Out of remaining question attempt any 4 question
6. In all total 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
a. Explain which cache replacement strategy (LRU, FIFO, or LFU) would provide a better hit ratio for the
given sequence of memory references when the cache has 4 lines, and justify your answer briefly.: 3, 4,
2, 2, 1, 3, 5, 1, 6, 5, 4, 1, 1, 3, 3, 1, 2, 1, 2, 1, 3, 4, 1, 5, 2.
Result (hit counts): LRU = 14 hits, FIFO = 14 hits, LFU = 16 hits.
Winner: LFU.
Why: The reference stream contains several items that repeat many times (especially 1, 2, 3). LFU keeps the
most frequently used blocks in the 4-line cache, so it retains those high-frequency items and yields more hits
(16) than LRU/FIFO (both 14). LRU and FIFO evict based on recency or arrival order and therefore miss
more when a low-recent-but-high-frequency item gets evicted; LFU avoids that by privileging long-term
frequency.
b. Describe the concept of interrupts in a computer system and illustrate how they facilitate communication
between hardware and the CPU.
Definition: An interrupt is a signal (hardware or software) that temporarily halts the CPU’s current
execution flow and causes it to transfer control to a special routine (an interrupt service routine, ISR) to
handle an event. After the ISR finishes, normal execution resumes.
Key points / types:
• Sources: hardware interrupts (I/O devices, timers), software interrupts (system calls,
exceptions/traps).
• Maskable vs Non-maskable: Maskable interrupts can be disabled by the CPU; non-maskable (NMI)
cannot.
********** 1 **********
--- page 2 ---
• Handling steps: device/CPU raises interrupt → CPU finishes current instruction (or as defined) →
saves CPU state (PC, registers) → jumps to ISR (via interrupt vector) → ISR services the event →
restores saved state → resumes interrupted program.
• Uses: asynchronous I/O handling, timers, error/exception handling, system calls.
c. Demonstrate your understanding of computer operations by listing and explaining the four main
functions   performed   by   a   computer   system   with   suitable   examples?
[05M]
Input — receive data and instructions from input devices (keyboard, sensors).
1. Processing — perform computations and logical operations on the input (CPU/ALU execution).
2. Storage — store data and instructions temporarily or permanently (RAM, cache, disk).
3. Output — present processed results to users or other systems (display, actuator, file, network).
(Control/co-ordination is sometimes listed as a fifth function — the CPU’s control unit orchestrates the
other four.)
d. Illustrate and analyze the MISD and MIMD architectures with suitable diagrams and evaluate how they
differ in terms of data processing and instruction execution capabilities.   [05M]
Instruction vs data model
o MISD: several processors apply different computations to the same data. Useful where
multiple distinct analyses on identical input are required (e.g., redundant/independent
computations or some fault-tolerant voting schemes). Extremely uncommon as a general-
purpose architecture.
o MIMD: processors run different instruction streams on different data sets. This is the
mainstream parallel architecture (multiprocessors, multicore CPUs, clusters).
• Data processing capabilities
o MISD: good for pipelined transformations on a single data stream or for N-version
redundancy (detect faults by comparing different computations on same data). Throughput
limited by ability to feed the same data to all processors; not scalable for general-purpose
parallel data processing.
o MIMD: highly scalable for data-parallel and task-parallel problems because each processor
works independent data; supports coarse- and fine-grained parallelism.
•   Instruction execution capabilities
o MISD: processors execute different algorithms on identical input — coordination is about
synchronising on the single data. Limited concurrency benefits for diverse tasks.
o MIMD: each processor executes its own program; supports asynchronous execution,
independent control flows, and richer parallel task scheduling.
• Complexity & practicality
o MISD: conceptually useful in niche fault-tolerance/pipeline designs, but uncommon in real
systems; complex to design and inefficient for most workloads.
o MIMD: widely used (multicore CPUs, clusters). More flexible, better load balancing, and
more broadly applicable.
Evaluation (when to prefer each)
********** 2 **********
--- page 3 ---
• Prefer MISD only for special cases: hardware redundancy, certain pipeline stages where same data
must be processed differently or for independent verification of results (fault-tolerant/voting
systems).
• Prefer MIMD for almost all parallel computing needs — independent tasks or independent data
chunks, scalable parallelism, heterogeneous workloads.
Q2
a. Describe the main structural components of a computer system and explain the internal
structural blocks of the CPU with the help of a neat diagram. [10M]
Solution:
1. Structural Components of a Computer System:
A computer system consists of five main functional blocks, as shown below:
Main Structural Blocks:
1. Input Unit:
o Accepts data and instructions from the user.
o Converts human-readable form to machine-readable form (binary).
o Examples: Keyboard, Mouse, Scanner.
2. Memory Unit:
o Stores data, instructions, and intermediate results.
o Types:
▪ Primary memory: RAM, ROM
▪ Secondary memory: Hard disk, SSD, CD-ROM
o Acts as a bridge between CPU and I/O devices.
3. Arithmetic Logic Unit (ALU):
o Performs arithmetic operations (addition, subtraction, etc.)
o Performs logical operations (comparison, AND, OR, NOT).
o Works under control of the Control Unit.
4. Control Unit (CU):
o Directs the flow of data and instructions within the CPU.
o Fetches, decodes, and executes instructions.
o Coordinates all components of the computer.
5. Output Unit:
o Converts processed data into human-understandable form.
o Examples: Monitor, Printer, Speaker.
2. Structural Components of CPU:
The Central Processing Unit (CPU) is the “brain” of the computer. It consists of:
• Control Unit (CU):
o Directs the sequence of operations.
o   Interprets and sends control signals to other units.
• Arithmetic and Logic Unit (ALU):
********** 3 **********
--- page 4 ---
o Performs computation and logical decision-making.
•   Register Array:
o High-speed temporary storage locations.
o Includes:
▪ Program Counter (PC): Holds the address of next instruction.
▪   Instruction Register (IR): Holds the current instruction.
▪ Accumulator (ACC): Stores intermediate arithmetic results.
▪ General-purpose registers: Temporarily store data/addresses.
b. Illustrate and explain the concept of instruction format in computer architecture and apply it to show
how various instruction fields define the operation of a CPU. [10M]
Solution:
1. Definition:
An instruction format specifies the layout or structure of bits within an instruction word that tells the CPU
what operation to perform and on which operands.
Each instruction in machine language typically consists of several fields:
+------------+-------------+-------------+-------------+
| Opcode   | Address/Reg | Address/Reg | Address/Reg |
+------------+-------------+-------------+-------------+
2. Main Fields in an Instruction Format:
Field   Description
Opcode Field   Specifies the operation to be performed (e.g., ADD, SUB, LOAD).
Address Field(s) Specifies the memory location(s) or register(s) involved in the operation.
Mode Field   Specifies the addressing mode (direct, indirect, immediate, etc.).
Register Field   Identifies the register(s) used for the operation.
Flag/Control Bits Indicate conditional or control information (e.g., branching).
3. Types of Instruction Formats:
1. Zero-Address Format:
o Used in stack-based architecture.
o Operands are implicitly on the stack.
o Example:
o ADD ; pops two values, adds, pushes result
2. One-Address Format:
o One explicit operand; accumulator used implicitly.
o Example:
o ADD X → ACC = ACC + X
3. Two-Address Format:
o Specifies two operands (source and destination).
o Example:
********** 4 **********
--- page 5 ---
o MOV R1, R2 → R1 = R2
4. Three-Address Format:
o Specifies three operands (two sources and one destination).
o Example:
o ADD R1, R2, R3 → R1 = R2 + R3
4. Example:
For a 16-bit instruction format:
+--------+--------+--------+--------+
| 4 bits | 4 bits | 4 bits | 4 bits |
| Opcode | Reg1   | Reg2   | Reg3   |
+--------+--------+--------+--------+
Example:
ADD R1, R2, R3
• Opcode = 0001 (ADD)
• Reg1 = Destination (R1)
• Reg2, Reg3 = Operands
5. Importance of Instruction Format:
•   Defines CPU decoding logic and instruction set architecture (ISA).
•   Affects instruction length, execution speed, and hardware complexity.
• Determines how efficiently the processor uses memory and registers.
Q3.
a. Define and describe the concept of Memory Hierarchy in a computer system. Explain its levels and the
need for organizing memory in a hierarchical structure. [10M]
Solution:
1. Definition:
The Memory Hierarchy in a computer system refers to the arrangement of different types of memories
based on their speed, cost, and capacity to achieve a balance between performance and cost.
It provides a structure where the fastest but smallest and expensive memories are placed closest to the
CPU, while slower but larger and cheaper memories are placed farther away.
3. Levels of Memory Hierarchy:
Level   Type   Speed   Cost/Bit Capacity   Example
L0   Registers   Very High Very High Very Low CPU Registers
L1   Cache Memory   High   High   Low   L1/L2/L3 Cache
L2   Main Memory (RAM) Medium Medium Moderate DRAM, SDRAM
L3   Secondary Memory Low   Low   High   HDD, SSD
********** 5 **********
--- page 6 ---
Level   Type   Speed   Cost/Bit Capacity   Example
L4   Tertiary Memory   Very Low Very Low Very High Optical Disks, Cloud Storage
4. Need for Memory Hierarchy:
• Speed mismatch between CPU and memory (CPU is much faster than main memory).
• Cost optimization – faster memories are expensive; slower ones are cheaper.
•   Efficient data access – frequently used data kept closer to CPU.
• Improves system performance by reducing average access time.
5. Working Principle:
a. The temporal locality and spatial locality principles are used:
o Temporal locality: recently accessed data is likely to be accessed again.
o Spatial locality: data near recently accessed locations is likely to be accessed soon.
b. Data moves between levels depending on usage frequency.
The memory hierarchy ensures that the CPU gets data quickly without significantly increasing cost. It
effectively bridges the speed gap between the processor and memory, resulting in better performance and
efficiency.
b. Illustrate and explain the concept of a Hardwired Control Unit. Demonstrate how control signals are
generated in this unit and compare it briefly with a Microprogrammed Control Unit.   [10M]
Solution:
1. Definition:
A Hardwired Control Unit (HCU) is a control unit in which control signals are generated by fixed
electronic circuits using combinational logic (gates, decoders, flip-flops, and counters).
It directly translates the instruction opcode into control signals without using microinstructions.
3. Working:
1. The Instruction Register (IR) receives the binary instruction from memory.
2. The Decoder interprets the opcode and sends signals to the Control Logic Unit.
3. The Control Logic Unit uses sequential and combinational circuits to generate specific control
signals for each CPU operation (fetch, decode, execute, store).
4. These control signals coordinate the operation of ALU, registers, and memory.
4. Features:
Feature   Description
Implementation Uses hardware (logic gates, flip-flops).
Speed   Very fast (direct signal generation).
********** 6 **********
--- page 7 ---
Feature   Description
Flexibility   Less flexible; modification requires hardware change.
Complexity   Increases with instruction set complexity.
5. Advantages:
•   Faster execution since control signals are generated directly.
•   Suitable for simple instruction sets (RISC processors).
• Low control memory requirement.
6. Disadvantages:
•   Difficult to modify or upgrade (hardware redesign needed).
• Complex wiring for large instruction sets.
• Not suitable for CISC (Complex Instruction Set Computing).
7. Comparison with Microprogrammed Control Unit:
Aspect   Hardwired Control Unit Microprogrammed Control Unit
Implementation Logic gates, circuits   Microinstructions in control memory
Speed   Faster   Slower
Flexibility   Low   High (easy to modify)
Complexity   Complex for large ISAs   Easier to implement
Use   RISC processors   CISC processors
Conclusion:
A Hardwired Control Unit provides high-speed control signal generation using dedicated hardware
circuits, ideal for processors requiring fast execution. However, it lacks flexibility compared to
microprogrammed units, which trade off speed for easier modification and scalability.
Q4
a. Define and describe the Von Neumann system architecture. List and explain its main components and
their functions within a general computer system. [10M]
Solution:
1. Definition:
The Von Neumann Architecture (also known as the stored-program architecture) is a computer model
proposed by John von Neumann in 1945.
It describes how a computer system is organized to store both data and instructions in the same memory
and execute programs sequentially.
2. Key Concept:
********** 7 **********
--- page 8 ---
• Both instructions and data share the same memory space.
• The CPU fetches instructions one by one from memory, decodes, and executes them.
• This model is the foundation for most modern computer systems.
4. Major Components and Functions:
Component   Function
Input Unit   Accepts data and instructions from external sources.
Memory Unit   Stores both program instructions and data. Divided into addressable cells.
Arithmetic Logic Unit
Performs arithmetic and logical operations.
(ALU)
Fetches instructions from memory, decodes, and directs ALU and registers to
Control Unit (CU)
execute them.
Registers   High-speed small storage in CPU for temporary data.
Output Unit   Displays or outputs the processed results.
5. Features of Von Neumann Architecture:
• Shared memory for instructions and data.
•   Sequential instruction execution (fetch → decode → execute).
• Uses bus system for data and instruction transfer.
•   Basis of the stored program concept.
6. Limitations:
• Von Neumann Bottleneck: Since both data and instructions share the same bus, simultaneous fetch
and execution cannot occur, causing delays.
• Limited parallelism.
Conclusion:
The Von Neumann architecture laid the foundation for modern computing by introducing the stored-
program concept. It provides a clear and structured model for executing programs, although it suffers from
memory bottleneck limitations in high-speed computing systems.
********** 8 **********
--- page 9 ---
b. Explain and interpret the role of the Status Register (also called the Flag Register) in a CPU. Describe the
different status flags and their significance in instruction execution. [10M]
Solution:
1. Definition:
A Status Register (or Flag Register) is a special-purpose register in the CPU that holds information about
the current state or outcome of arithmetic and logical operations performed by the ALU.
These flags are used by the processor to make decisions during program execution (e.g., branching,
conditional operations).
2. Purpose:
•   Indicates conditions resulting from operations (like zero, carry, overflow).
• Guides control flow of programs (e.g., “jump if zero,” “jump if carry”).
• Helps in error detection and status monitoring.
3. General Format of Status Register:
Example (8-bit flag register layout):
+---+---+---+---+---+---+---+---+
| S | Z | AC| P | CY| O | N | I |
+---+---+---+---+---+---+---+---+
4. Common Flags and Their Meanings:
Flag Name   Symbol   Description
Set if an arithmetic operation produces a carry out of the most significant bit
Carry Flag   CY
(addition) or borrow (subtraction).
Zero Flag   Z   Set if the result of an operation is zero.
Sign Flag   S   Indicates the sign of the result (1 for negative, 0 for positive).
Parity Flag   P   Set if the number of 1’s in the result is even; cleared if odd.
Auxiliary Carry   Used for Binary-Coded Decimal (BCD) operations — set if there is a carry
AC
Flag   from bit 3 to bit 4.
Overflow Flag O / V   Indicates arithmetic overflow when the result exceeds representable range.
Interrupt Flag   I   Enables or disables interrupts (1 = enabled, 0 = disabled).
Negative Flag   N   Indicates a negative result (similar to sign flag in some architectures).
5. Example:
Suppose two 8-bit numbers are added:
11110000 (+240)
+ 11110000 (+240)
********** 9 **********
--- page 10 ---
= 11100000 (overflow)
Here, the Carry and Overflow flags are set to 1, indicating a carry beyond 8 bits and arithmetic overflow.
6. Uses of Status Register:
• Supports conditional branching instructions:
o Example: JZ (Jump if Zero), JC (Jump if Carry).
• Aids in decision making in programs.
• Helps in debugging and error detection.
Conclusion:
The Status Register plays a crucial role in CPU operation by storing condition flags that describe the
result of arithmetic or logic operations. These flags enable conditional execution and efficient program
control flow in computer systems.
Q5
a.   Illustrate the system bus structure in a computer system and explain in detail the different types of
buses along with their functions and roles in data transfer. [10M]
Solution:
1. Definition:
A bus in a computer system is a communication pathway through which data, control signals, and
addresses are transmitted between the different components of the computer such as the CPU, memory, and
I/O devices.
The bus acts as a shared transmission medium connecting all major components.
3. Types of System Buses:
Type of Bus   Direction   Main Function
Data Bus   Bi-directional   Transfers actual data between CPU, memory, and I/O.
Address Bus Uni-directional (from CPU) Carries memory or I/O addresses that the CPU wants to access.
Control Bus Bi-directional   Carries control and timing signals to coordinate data transfers.
4. Explanation of Each Bus:
(i) Data Bus:
• Function: Transfers data between the CPU, memory, and I/O devices.
• Width: The number of data lines (8, 16, 32, 64 bits) determines how much data can be transferred at
once.
•   Direction: Bi-directional — CPU can read or write data.
• Example:
o During a read operation, data moves from memory → CPU.
o During a write operation, data moves from CPU → memory.
********** 10 **********
--- page 11 ---
(ii) Address Bus:
• Function: Carries address information of data or instructions that the CPU wants to read or write.
•   Direction: Uni-directional — only from CPU to memory/I/O devices.
• Width: Determines the maximum addressable memory.
o Example: A 32-bit address bus can access 232 = 4 GBof memory.
(iii) Control Bus:
• Function: Transmits control and timing signals between CPU and other components to manage
operations.
•   Direction: Bi-directional (some signals from CPU, some to CPU).
• Examples of Control Signals:
o Memory Read / Write: Controls data transfer between CPU and memory.
o I/O Read / Write: Controls communication with I/O devices.
o Clock signal: Synchronizes all operations.
o Interrupt Request (IRQ): Indicates peripheral needs CPU attention.
o Bus Request / Grant: Used in DMA operations.
5. Working of System Bus:
• The CPU places the address on the address bus.
• The control bus specifies whether it’s a read or write operation.
• Data is then transferred via the data bus.
• The synchronization ensures efficient communication between components.
6. Importance of Bus System:
• Reduces complex wiring by providing shared communication paths.
• Enables modular design — components can easily communicate.
• Improves system scalability and speed.
Conclusion:
The system bus is the backbone of the computer’s communication system. It integrates address, data, and
control buses to facilitate smooth and synchronized data transfer between CPU, memory, and I/O devices.
b. Explain and interpret the elements (fields) of a machine instruction. Describe the role of each field in
enabling the CPU to perform operations effectively. [10M]
Solution:
1. Definition:
********** 11 **********
--- page 12 ---
A machine instruction is a binary-coded operation that tells the CPU what operation to perform and on
which data.
It is the basic executable unit of a program stored in main memory.
Each instruction contains several fields, known as the elements of instruction format.
Elements (Fields) of a Machine Instruction:
Element / Field   Description
Specifies the operation to be performed (e.g., ADD, SUB, LOAD, STORE). It
Opcode (Operation Code)
tells the CPU which arithmetic/logic action to take.
Operand(s) / Address   Identifies the data or memory location(s) on which the operation acts. Can
Field(s)   refer to register, memory, or immediate data.
Mode Field (Addressing   Specifies how to interpret the address field — e.g., direct, indirect, immediate,
Mode)   or register addressing.
Identifies which register(s) are involved in the operation (for RISC
Register Field
architectures).
Condition Code / Flag   Indicates conditional execution or status information after an operation (e.g.,
Field   zero, carry).
Next Instruction Field /
Used in branch or jump instructions to specify the next instruction’s address.
Jump Address
4. Example of Instruction Format:
For a 16-bit instruction:
+--------+--------+--------+--------+
| 4 bits | 4 bits | 4 bits | 4 bits |
| Opcode | Reg1   | Reg2   | Reg3   |
+--------+--------+--------+--------+
Example:
ADD R1, R2, R3
• Opcode: 0001 → ADD operation
• Reg1: Destination register (R1)
• Reg2, Reg3: Source registers (R2 and R3)
5. Example Explanation:
Instruction: LOAD R1, 2000
• Opcode: LOAD
• Operand: Memory address 2000
• Meaning: Load data from memory location 2000 into register R1.
6. Role of Each Element:
********** 12 **********
--- page 13 ---
• Opcode: Defines operation type.
• Operand fields: Identify data or location for operation.
• Mode field: Defines how operands are accessed.
•   Register/Flag fields: Determine where to store or how to modify results.
Conclusion:
A machine instruction is composed of several fields that together direct the CPU on what operation to
perform and where to perform it. Understanding these elements is crucial for designing efficient instruction
sets and ensuring smooth program execution.
Q6
a. Differentiate and explain the RISC and CISC computer architectures in terms of their design
philosophy, instruction set characteristics, and performance considerations. [10M]
Solution:
1. Introduction:
Computer architectures can be broadly classified into RISC (Reduced Instruction Set Computer) and
CISC (Complex Instruction Set Computer) based on the number and complexity of instructions they
use.
2. RISC (Reduced Instruction Set Computer):
• RISC architecture focuses on simplifying the instruction set for faster execution.
• Each instruction is designed to execute in one clock cycle, improving performance and
throughput.
Characteristics of RISC:
Feature   Description
Instruction Length Fixed-length (typically 32 bits)
Execution Speed One instruction per clock cycle
Addressing Modes Few (usually 3–5)
Instruction Set   Small and simple
Registers   Large number of general-purpose registers
Pipelining   Highly efficient and easy to implement
Examples   ARM, MIPS, SPARC, RISC-V
Advantages of RISC:
•   Simplifies hardware design.
• High performance due to pipelining.
•   Easier compiler optimization.
•   Consistent instruction timing.
Disadvantages of RISC:
•   Requires more instructions for complex operations.
********** 13 **********
--- page 14 ---
•   Larger program size compared to CISC.
3. CISC (Complex Instruction Set Computer):
• CISC architecture includes a large set of complex instructions, each capable of performing multiple
operations.
• Focuses on reducing the number of instructions per program.
Characteristics of CISC:
Feature   Description
Instruction Length Variable (8 to 64 bits or more)
Execution Speed   Slower, may take multiple cycles
Addressing Modes Many (up to 15 or more)
Instruction Set   Large and complex
Registers   Fewer general-purpose registers
Pipelining   Difficult to implement efficiently
Examples   Intel x86, VAX, Motorola 68000
Advantages of CISC:
• Compact programs due to complex instructions.
•   Easier assembly-level programming.
•   Efficient for memory-limited systems.
Disadvantages of CISC:
• Slower execution due to complex decoding.
•   Difficult to pipeline efficiently.
• More complex hardware design.
4. Comparison Table:
Aspect   RISC   CISC
Instruction Count   Fewer   Large
Instruction Size   Fixed   Variable
Execution Time   1 cycle/instruction Multiple cycles/instruction
Hardware Complexity Simple   Complex
Pipelining   Easy to implement Difficult
Registers   Many   Few
Examples   ARM, MIPS   Intel x86, VAX
b. Classify and explain the types of machine instructions based on address references, illustrating each
with suitable examples.
********** 14 **********
--- page 15 ---
Solution:
1. Introduction:
Machine instructions can be classified based on the number of address fields used to specify operands
and results in the instruction format.
The address field tells the CPU where the operands are located (registers, memory, or immediate).
2. Classification of Machine Instructions Based on Address Reference:
Type   Address Fields General Format   Example
Zero-Address Instructions None   OP   PUSH, POP, ADD
One-Address Instructions One   OP A   LOAD A, NOT A
Two-Address Instructions Two   OP A, B   MOV A, B
Three-Address Instructions Three   OP A, B, C   ADD A, B, C
3. Explanation of Each Type:
(i) Zero-Address Instruction:
• Used in stack-based architectures.
• Operands are implicitly stored on the stack.
• Example:
• PUSH A
• PUSH B
• ADD
→ Adds top two elements on the stack.
✅ Advantage: No explicit address field; shorter instruction size.
❌ Disadvantage: More stack operations; slower for large programs.
(ii) One-Address Instruction:
• Uses accumulator architecture.
• One operand is implicitly the accumulator, and the other is explicitly given.
Example:
LOAD A   ; Acc ← M[A]
ADD B   ; Acc ← Acc + M[B]
STORE C   ; M[C] ← Acc
✅ Advantage: Simple to design and understand.
❌ Disadvantage: Frequent memory access through accumulator.
********** 15 **********
--- page 16 ---
(iii) Two-Address Instruction:
• Both operands are explicitly mentioned.
• One operand also acts as the destination.
Example:
ADD A, B   ; A ← A + B
✅ Advantage: Reduces number of instructions.
❌ Disadvantage: More bits required for instruction storage.
(iv) Three-Address Instruction:
•   Contains three operands — two sources and one destination.
• Common in RISC processors.
Example:
ADD A, B, C ; A ← B + C
✅ Advantage: Allows complex operations in a single instruction.
❌ Disadvantage: Larger instruction size.
4. Summary Table:
Type   Operands Specified   Typical Architecture Example
Zero-Address Implicit (Stack)   Stack-based   ADD
One-Address Accumulator   Single Accumulator ADD A
Two-Address Source & Destination   Register–Memory   ADD A, B
Three-Address Two Sources + Destination RISC   ADD A, B, C
Conclusion:
The number of address references in machine instructions determines the complexity, size, and execution
efficiency of a processor. Modern processors, especially RISC systems, often favor three-address formats
for improved performance and pipelining.
Q7.
a. Explain and summarize the advantages and disadvantages of a Superscalar architecture in modern
processors. [10M]
Solution:
1. Definition:
A Superscalar architecture allows a processor to execute more than one instruction per clock cycle
by using multiple execution units.
It improves the instruction-level parallelism (ILP) of a CPU.
********** 16 **********
--- page 17 ---
2. Key Concept:
• Multiple pipelines operate simultaneously.
• The processor fetches, decodes, and executes several instructions in parallel.
•   Out-of-order and speculative execution techniques are often used.
3. Advantages of Superscalar Architecture:
Advantage   Explanation
Increased Performance   Executes multiple instructions per clock cycle.
Efficient Resource Utilization   Uses multiple ALUs, FPUs, and pipelines simultaneously.
Higher Instruction Throughput   Parallel instruction issue enhances overall speed.
Supports Pipelining and Parallelism Enables multiple functional units to work concurrently.
Reduced Program Execution Time Achieves better CPU utilization and shorter execution times.
4. Disadvantages of Superscalar Architecture:
Disadvantage   Explanation
Complex Hardware Design   Requires advanced instruction scheduling and hazard detection logic.
Increased Power Consumption   Parallel execution units increase power usage.
Performance gain reduces after certain instruction-level parallelism is
Diminishing Returns
reached.
Dependency Management
Data and control dependencies between instructions limit parallel execution.
Issues
b. Describe and analyze the concept of Virtual Memory in computer systems. Also, explain what is meant
by a logical address space and how it differs from physical memory.
Solution:
1. Definition:
Virtual Memory is a memory management technique that gives an application the illusion of having a
large, continuous memory space even when the physical RAM is limited.
It uses a portion of secondary storage (like a hard disk or SSD) to simulate main memory.
2. Key Concept:
Virtual memory enables:
• Execution of programs larger than physical memory.
•   Isolation and protection of processes.
•   Efficient memory utilization through paging or segmentation.
********** 17 **********
--- page 18 ---
3. Working Principle:
• The CPU generates logical addresses during program execution.
• These are mapped to physical addresses by the Memory Management Unit (MMU).
• When required data is not present in RAM, a page fault occurs and data is fetched from secondary
storage.
4. Logical Address Space:
Term   Explanation
Logical Address (Virtual Address) The address generated by the CPU during program execution.
Physical Address   The actual address in the main memory (RAM).
Logical Address Space   The range of all possible logical addresses a process can generate.
Example:
If a CPU supports 32-bit addressing, the logical address space = 2³² = 4 GB, regardless of actual physical
RAM size.
5. Address Mapping Diagram:
CPU
| (Generates Logical Address)
v
+----------------------------+
| Memory Management Unit   |
| (MMU)   |
+----------------------------+
| (Translates)
v
Physical Memory (RAM)
6. Advantages of Virtual Memory:
Advantage   Explanation
Efficient Memory Use   Only needed parts of a program are loaded into memory.
Isolation   Each process operates in its own logical address space.
Large Program Execution Enables execution of programs larger than physical memory.
Protection   Prevents one process from accessing another’s memory.
7. Disadvantages of Virtual Memory:
Disadvantage   Explanation
Reduced Performance Frequent swapping (paging) causes delay.
********** 18 **********
--- page 19 ---
Disadvantage   Explanation
Increased Disk Wear Excessive paging can reduce disk lifespan.
Complex Management Requires sophisticated hardware (MMU) and OS algorithms.
c. Define and explain the concept of a Bus in a computer system. Describe the main types of system buses
and their functions. [5M]
Solution:
1. Definition:
A Bus is a communication pathway that connects various components of a computer system (CPU,
memory, I/O devices) and allows the transfer of data, address, and control signals among them.
2. Types of Buses:
Bus Type   Purpose   Example Signal
Transfers actual data between CPU, memory, and I/O   Data values (e.g., 8-bit, 16-bit, 32-
Data Bus
devices.   bit)
Address   Carries the memory addresses of data/instructions to be   Memory location address (e.g.,
Bus   accessed.   0x3F0A)
Control Bus Carries control signals that coordinate all activities.   Read/Write, Interrupt, Clock signals
4. Functionality Summary:
Bus   Function
Data Bus   Bi-directional; used for transferring data.
Address Bus Uni-directional; specifies memory location.
Control Bus Bi-directional; synchronizes system operations.
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 92115e40f145

- Departments: Information Technology
- Programmes: DIPLOMA IN INFORMATION TECHNOLOGY - 7075
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/DIPLOMA IN INFORMATION TECHNOLOGY - 7075/COMPUTER SYSTEM ARCHITECTURE/ANS_COMPUTER SYSTEM ARCHITECTURE(701EX0C006)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER SYSTEM ARCHITECTURE
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Q1 is compulsory
5. Out of remaining question attempt any 4 question
6. In all total 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
a. Explain which cache replacement strategy (LRU, FIFO, or LFU) would provide a better hit ratio for the
given sequence of memory references when the cache has 4 lines, and justify your answer briefly.: 3, 4,
2, 2, 1, 3, 5, 1, 6, 5, 4, 1, 1, 3, 3, 1, 2, 1, 2, 1, 3, 4, 1, 5, 2.
Result (hit counts): LRU = 14 hits, FIFO = 14 hits, LFU = 16 hits.
Winner: LFU.
Why: The reference stream contains several items that repeat many times (especially 1, 2, 3). LFU keeps the
most frequently used blocks in the 4-line cache, so it retains those high-frequency items and yields more hits
(16) than LRU/FIFO (both 14). LRU and FIFO evict based on recency or arrival order and therefore miss
more when a low-recent-but-high-frequency item gets evicted; LFU avoids that by privileging long-term
frequency.
b. Describe the concept of interrupts in a computer system and illustrate how they facilitate communication
between hardware and the CPU.
Definition: An interrupt is a signal (hardware or software) that temporarily halts the CPU’s current
execution flow and causes it to transfer control to a special routine (an interrupt service routine, ISR) to
handle an event. After the ISR finishes, normal execution resumes.
Key points / types:
• Sources: hardware interrupts (I/O devices, timers), software interrupts (system calls,
exceptions/traps).
• Maskable vs Non-maskable: Maskable interrupts can be disabled by the CPU; non-maskable (NMI)
cannot.
********** 1 **********
--- page 2 ---
• Handling steps: device/CPU raises interrupt → CPU finishes current instruction (or as defined) →
saves CPU state (PC, registers) → jumps to ISR (via interrupt vector) → ISR services the event →
restores saved state → resumes interrupted program.
• Uses: asynchronous I/O handling, timers, error/exception handling, system calls.
c. Demonstrate your understanding of computer operations by listing and explaining the four main
functions   performed   by   a   computer   system   with   suitable   examples?
[05M]
Input — receive data and instructions from input devices (keyboard, sensors).
1. Processing — perform computations and logical operations on the input (CPU/ALU execution).
2. Storage — store data and instructions temporarily or permanently (RAM, cache, disk).
3. Output — present processed results to users or other systems (display, actuator, file, network).
(Control/co-ordination is sometimes listed as a fifth function — the CPU’s control unit orchestrates the
other four.)
d. Illustrate and analyze the MISD and MIMD architectures with suitable diagrams and evaluate how they
differ in terms of data processing and instruction execution capabilities.   [05M]
Instruction vs data model
o MISD: several processors apply different computations to the same data. Useful where
multiple distinct analyses on identical input are required (e.g., redundant/independent
computations or some fault-tolerant voting schemes). Extremely uncommon as a general-
purpose architecture.
o MIMD: processors run different instruction streams on different data sets. This is the
mainstream parallel architecture (multiprocessors, multicore CPUs, clusters).
• Data processing capabilities
o MISD: good for pipelined transformations on a single data stream or for N-version
redundancy (detect faults by comparing different computations on same data). Throughput
limited by ability to feed the same data to all processors; not scalable for general-purpose
parallel data processing.
o MIMD: highly scalable for data-parallel and task-parallel problems because each processor
works independent data; supports coarse- and fine-grained parallelism.
•   Instruction execution capabilities
o MISD: processors execute different algorithms on identical input — coordination is about
synchronising on the single data. Limited concurrency benefits for diverse tasks.
o MIMD: each processor executes its own program; supports asynchronous execution,
independent control flows, and richer parallel task scheduling.
• Complexity & practicality
o MISD: conceptually useful in niche fault-tolerance/pipeline designs, but uncommon in real
systems; complex to design and inefficient for most workloads.
o MIMD: widely used (multicore CPUs, clusters). More flexible, better load balancing, and
more broadly applicable.
Evaluation (when to prefer each)
********** 2 **********
--- page 3 ---
• Prefer MISD only for special cases: hardware redundancy, certain pipeline stages where same data
must be processed differently or for independent verification of results (fault-tolerant/voting
systems).
• Prefer MIMD for almost all parallel computing needs — independent tasks or independent data
chunks, scalable parallelism, heterogeneous workloads.
Q2
a. Describe the main structural components of a computer system and explain the internal
structural blocks of the CPU with the help of a neat diagram. [10M]
Solution:
1. Structural Components of a Computer System:
A computer system consists of five main functional blocks, as shown below:
Main Structural Blocks:
1. Input Unit:
o Accepts data and instructions from the user.
o Converts human-readable form to machine-readable form (binary).
o Examples: Keyboard, Mouse, Scanner.
2. Memory Unit:
o Stores data, instructions, and intermediate results.
o Types:
▪ Primary memory: RAM, ROM
▪ Secondary memory: Hard disk, SSD, CD-ROM
o Acts as a bridge between CPU and I/O devices.
3. Arithmetic Logic Unit (ALU):
o Performs arithmetic operations (addition, subtraction, etc.)
o Performs logical operations (comparison, AND, OR, NOT).
o Works under control of the Control Unit.
4. Control Unit (CU):
o Directs the flow of data and instructions within the CPU.
o Fetches, decodes, and executes instructions.
o Coordinates all components of the computer.
5. Output Unit:
o Converts processed data into human-understandable form.
o Examples: Monitor, Printer, Speaker.
2. Structural Components of CPU:
The Central Processing Unit (CPU) is the “brain” of the computer. It consists of:
• Control Unit (CU):
o Directs the sequence of operations.
o   Interprets and sends control signals to other units.
• Arithmetic and Logic Unit (ALU):
********** 3 **********
--- page 4 ---
o Performs computation and logical decision-making.
•   Register Array:
o High-speed temporary storage locations.
o Includes:
▪ Program Counter (PC): Holds the address of next instruction.
▪   Instruction Register (IR): Holds the current instruction.
▪ Accumulator (ACC): Stores intermediate arithmetic results.
▪ General-purpose registers: Temporarily store data/addresses.
b. Illustrate and explain the concept of instruction format in computer architecture and apply it to show
how various instruction fields define the operation of a CPU. [10M]
Solution:
1. Definition:
An instruction format specifies the layout or structure of bits within an instruction word that tells the CPU
what operation to perform and on which operands.
Each instruction in machine language typically consists of several fields:
+------------+-------------+-------------+-------------+
| Opcode   | Address/Reg | Address/Reg | Address/Reg |
+------------+-------------+-------------+-------------+
2. Main Fields in an Instruction Format:
Field   Description
Opcode Field   Specifies the operation to be performed (e.g., ADD, SUB, LOAD).
Address Field(s) Specifies the memory location(s) or register(s) involved in the operation.
Mode Field   Specifies the addressing mode (direct, indirect, immediate, etc.).
Register Field   Identifies the register(s) used for the operation.
Flag/Control Bits Indicate conditional or control information (e.g., branching).
3. Types of Instruction Formats:
1. Zero-Address Format:
o Used in stack-based architecture.
o Operands are implicitly on the stack.
o Example:
o ADD ; pops two values, adds, pushes result
2. One-Address Format:
o One explicit operand; accumulator used implicitly.
o Example:
o ADD X → ACC = ACC + X
3. Two-Address Format:
o Specifies two operands (source and destination).
o Example:
********** 4 **********
--- page 5 ---
o MOV R1, R2 → R1 = R2
4. Three-Address Format:
o Specifies three operands (two sources and one destination).
o Example:
o ADD R1, R2, R3 → R1 = R2 + R3
4. Example:
For a 16-bit instruction format:
+--------+--------+--------+--------+
| 4 bits | 4 bits | 4 bits | 4 bits |
| Opcode | Reg1   | Reg2   | Reg3   |
+--------+--------+--------+--------+
Example:
ADD R1, R2, R3
• Opcode = 0001 (ADD)
• Reg1 = Destination (R1)
• Reg2, Reg3 = Operands
5. Importance of Instruction Format:
•   Defines CPU decoding logic and instruction set architecture (ISA).
•   Affects instruction length, execution speed, and hardware complexity.
• Determines how efficiently the processor uses memory and registers.
Q3.
a. Define and describe the concept of Memory Hierarchy in a computer system. Explain its levels and the
need for organizing memory in a hierarchical structure. [10M]
Solution:
1. Definition:
The Memory Hierarchy in a computer system refers to the arrangement of different types of memories
based on their speed, cost, and capacity to achieve a balance between performance and cost.
It provides a structure where the fastest but smallest and expensive memories are placed closest to the
CPU, while slower but larger and cheaper memories are placed farther away.
3. Levels of Memory Hierarchy:
Level   Type   Speed   Cost/Bit Capacity   Example
L0   Registers   Very High Very High Very Low CPU Registers
L1   Cache Memory   High   High   Low   L1/L2/L3 Cache
L2   Main Memory (RAM) Medium Medium Moderate DRAM, SDRAM
L3   Secondary Memory Low   Low   High   HDD, SSD
********** 5 **********
--- page 6 ---
Level   Type   Speed   Cost/Bit Capacity   Example
L4   Tertiary Memory   Very Low Very Low Very High Optical Disks, Cloud Storage
4. Need for Memory Hierarchy:
• Speed mismatch between CPU and memory (CPU is much faster than main memory).
• Cost optimization – faster memories are expensive; slower ones are cheaper.
•   Efficient data access – frequently used data kept closer to CPU.
• Improves system performance by reducing average access time.
5. Working Principle:
a. The temporal locality and spatial locality principles are used:
o Temporal locality: recently accessed data is likely to be accessed again.
o Spatial locality: data near recently accessed locations is likely to be accessed soon.
b. Data moves between levels depending on usage frequency.
The memory hierarchy ensures that the CPU gets data quickly without significantly increasing cost. It
effectively bridges the speed gap between the processor and memory, resulting in better performance and
efficiency.
b. Illustrate and explain the concept of a Hardwired Control Unit. Demonstrate how control signals are
generated in this unit and compare it briefly with a Microprogrammed Control Unit.   [10M]
Solution:
1. Definition:
A Hardwired Control Unit (HCU) is a control unit in which control signals are generated by fixed
electronic circuits using combinational logic (gates, decoders, flip-flops, and counters).
It directly translates the instruction opcode into control signals without using microinstructions.
3. Working:
1. The Instruction Register (IR) receives the binary instruction from memory.
2. The Decoder interprets the opcode and sends signals to the Control Logic Unit.
3. The Control Logic Unit uses sequential and combinational circuits to generate specific control
signals for each CPU operation (fetch, decode, execute, store).
4. These control signals coordinate the operation of ALU, registers, and memory.
4. Features:
Feature   Description
Implementation Uses hardware (logic gates, flip-flops).
Speed   Very fast (direct signal generation).
********** 6 **********
--- page 7 ---
Feature   Description
Flexibility   Less flexible; modification requires hardware change.
Complexity   Increases with instruction set complexity.
5. Advantages:
•   Faster execution since control signals are generated directly.
•   Suitable for simple instruction sets (RISC processors).
• Low control memory requirement.
6. Disadvantages:
•   Difficult to modify or upgrade (hardware redesign needed).
• Complex wiring for large instruction sets.
• Not suitable for CISC (Complex Instruction Set Computing).
7. Comparison with Microprogrammed Control Unit:
Aspect   Hardwired Control Unit Microprogrammed Control Unit
Implementation Logic gates, circuits   Microinstructions in control memory
Speed   Faster   Slower
Flexibility   Low   High (easy to modify)
Complexity   Complex for large ISAs   Easier to implement
Use   RISC processors   CISC processors
Conclusion:
A Hardwired Control Unit provides high-speed control signal generation using dedicated hardware
circuits, ideal for processors requiring fast execution. However, it lacks flexibility compared to
microprogrammed units, which trade off speed for easier modification and scalability.
Q4
a. Define and describe the Von Neumann system architecture. List and explain its main components and
their functions within a general computer system. [10M]
Solution:
1. Definition:
The Von Neumann Architecture (also known as the stored-program architecture) is a computer model
proposed by John von Neumann in 1945.
It describes how a computer system is organized to store both data and instructions in the same memory
and execute programs sequentially.
2. Key Concept:
********** 7 **********
--- page 8 ---
• Both instructions and data share the same memory space.
• The CPU fetches instructions one by one from memory, decodes, and executes them.
• This model is the foundation for most modern computer systems.
4. Major Components and Functions:
Component   Function
Input Unit   Accepts data and instructions from external sources.
Memory Unit   Stores both program instructions and data. Divided into addressable cells.
Arithmetic Logic Unit
Performs arithmetic and logical operations.
(ALU)
Fetches instructions from memory, decodes, and directs ALU and registers to
Control Unit (CU)
execute them.
Registers   High-speed small storage in CPU for temporary data.
Output Unit   Displays or outputs the processed results.
5. Features of Von Neumann Architecture:
• Shared memory for instructions and data.
•   Sequential instruction execution (fetch → decode → execute).
• Uses bus system for data and instruction transfer.
•   Basis of the stored program concept.
6. Limitations:
• Von Neumann Bottleneck: Since both data and instructions share the same bus, simultaneous fetch
and execution cannot occur, causing delays.
• Limited parallelism.
Conclusion:
The Von Neumann architecture laid the foundation for modern computing by introducing the stored-
program concept. It provides a clear and structured model for executing programs, although it suffers from
memory bottleneck limitations in high-speed computing systems.
********** 8 **********
--- page 9 ---
b. Explain and interpret the role of the Status Register (also called the Flag Register) in a CPU. Describe the
different status flags and their significance in instruction execution. [10M]
Solution:
1. Definition:
A Status Register (or Flag Register) is a special-purpose register in the CPU that holds information about
the current state or outcome of arithmetic and logical operations performed by the ALU.
These flags are used by the processor to make decisions during program execution (e.g., branching,
conditional operations).
2. Purpose:
•   Indicates conditions resulting from operations (like zero, carry, overflow).
• Guides control flow of programs (e.g., “jump if zero,” “jump if carry”).
• Helps in error detection and status monitoring.
3. General Format of Status Register:
Example (8-bit flag register layout):
+---+---+---+---+---+---+---+---+
| S | Z | AC| P | CY| O | N | I |
+---+---+---+---+---+---+---+---+
4. Common Flags and Their Meanings:
Flag Name   Symbol   Description
Set if an arithmetic operation produces a carry out of the most significant bit
Carry Flag   CY
(addition) or borrow (subtraction).
Zero Flag   Z   Set if the result of an operation is zero.
Sign Flag   S   Indicates the sign of the result (1 for negative, 0 for positive).
Parity Flag   P   Set if the number of 1’s in the result is even; cleared if odd.
Auxiliary Carry   Used for Binary-Coded Decimal (BCD) operations — set if there is a carry
AC
Flag   from bit 3 to bit 4.
Overflow Flag O / V   Indicates arithmetic overflow when the result exceeds representable range.
Interrupt Flag   I   Enables or disables interrupts (1 = enabled, 0 = disabled).
Negative Flag   N   Indicates a negative result (similar to sign flag in some architectures).
5. Example:
Suppose two 8-bit numbers are added:
11110000 (+240)
+ 11110000 (+240)
********** 9 **********
--- page 10 ---
= 11100000 (overflow)
Here, the Carry and Overflow flags are set to 1, indicating a carry beyond 8 bits and arithmetic overflow.
6. Uses of Status Register:
• Supports conditional branching instructions:
o Example: JZ (Jump if Zero), JC (Jump if Carry).
• Aids in decision making in programs.
• Helps in debugging and error detection.
Conclusion:
The Status Register plays a crucial role in CPU operation by storing condition flags that describe the
result of arithmetic or logic operations. These flags enable conditional execution and efficient program
control flow in computer systems.
Q5
a.   Illustrate the system bus structure in a computer system and explain in detail the different types of
buses along with their functions and roles in data transfer. [10M]
Solution:
1. Definition:
A bus in a computer system is a communication pathway through which data, control signals, and
addresses are transmitted between the different components of the computer such as the CPU, memory, and
I/O devices.
The bus acts as a shared transmission medium connecting all major components.
3. Types of System Buses:
Type of Bus   Direction   Main Function
Data Bus   Bi-directional   Transfers actual data between CPU, memory, and I/O.
Address Bus Uni-directional (from CPU) Carries memory or I/O addresses that the CPU wants to access.
Control Bus Bi-directional   Carries control and timing signals to coordinate data transfers.
4. Explanation of Each Bus:
(i) Data Bus:
• Function: Transfers data between the CPU, memory, and I/O devices.
• Width: The number of data lines (8, 16, 32, 64 bits) determines how much data can be transferred at
once.
•   Direction: Bi-directional — CPU can read or write data.
• Example:
o During a read operation, data moves from memory → CPU.
o During a write operation, data moves from CPU → memory.
********** 10 **********
--- page 11 ---
(ii) Address Bus:
• Function: Carries address information of data or instructions that the CPU wants to read or write.
•   Direction: Uni-directional — only from CPU to memory/I/O devices.
• Width: Determines the maximum addressable memory.
o Example: A 32-bit address bus can access 232 = 4 GBof memory.
(iii) Control Bus:
• Function: Transmits control and timing signals between CPU and other components to manage
operations.
•   Direction: Bi-directional (some signals from CPU, some to CPU).
• Examples of Control Signals:
o Memory Read / Write: Controls data transfer between CPU and memory.
o I/O Read / Write: Controls communication with I/O devices.
o Clock signal: Synchronizes all operations.
o Interrupt Request (IRQ): Indicates peripheral needs CPU attention.
o Bus Request / Grant: Used in DMA operations.
5. Working of System Bus:
• The CPU places the address on the address bus.
• The control bus specifies whether it’s a read or write operation.
• Data is then transferred via the data bus.
• The synchronization ensures efficient communication between components.
6. Importance of Bus System:
• Reduces complex wiring by providing shared communication paths.
• Enables modular design — components can easily communicate.
• Improves system scalability and speed.
Conclusion:
The system bus is the backbone of the computer’s communication system. It integrates address, data, and
control buses to facilitate smooth and synchronized data transfer between CPU, memory, and I/O devices.
b. Explain and interpret the elements (fields) of a machine instruction. Describe the role of each field in
enabling the CPU to perform operations effectively. [10M]
Solution:
1. Definition:
********** 11 **********
--- page 12 ---
A machine instruction is a binary-coded operation that tells the CPU what operation to perform and on
which data.
It is the basic executable unit of a program stored in main memory.
Each instruction contains several fields, known as the elements of instruction format.
Elements (Fields) of a Machine Instruction:
Element / Field   Description
Specifies the operation to be performed (e.g., ADD, SUB, LOAD, STORE). It
Opcode (Operation Code)
tells the CPU which arithmetic/logic action to take.
Operand(s) / Address   Identifies the data or memory location(s) on which the operation acts. Can
Field(s)   refer to register, memory, or immediate data.
Mode Field (Addressing   Specifies how to interpret the address field — e.g., direct, indirect, immediate,
Mode)   or register addressing.
Identifies which register(s) are involved in the operation (for RISC
Register Field
architectures).
Condition Code / Flag   Indicates conditional execution or status information after an operation (e.g.,
Field   zero, carry).
Next Instruction Field /
Used in branch or jump instructions to specify the next instruction’s address.
Jump Address
4. Example of Instruction Format:
For a 16-bit instruction:
+--------+--------+--------+--------+
| 4 bits | 4 bits | 4 bits | 4 bits |
| Opcode | Reg1   | Reg2   | Reg3   |
+--------+--------+--------+--------+
Example:
ADD R1, R2, R3
• Opcode: 0001 → ADD operation
• Reg1: Destination register (R1)
• Reg2, Reg3: Source registers (R2 and R3)
5. Example Explanation:
Instruction: LOAD R1, 2000
• Opcode: LOAD
• Operand: Memory address 2000
• Meaning: Load data from memory location 2000 into register R1.
6. Role of Each Element:
********** 12 **********
--- page 13 ---
• Opcode: Defines operation type.
• Operand fields: Identify data or location for operation.
• Mode field: Defines how operands are accessed.
•   Register/Flag fields: Determine where to store or how to modify results.
Conclusion:
A machine instruction is composed of several fields that together direct the CPU on what operation to
perform and where to perform it. Understanding these elements is crucial for designing efficient instruction
sets and ensuring smooth program execution.
Q6
a. Differentiate and explain the RISC and CISC computer architectures in terms of their design
philosophy, instruction set characteristics, and performance considerations. [10M]
Solution:
1. Introduction:
Computer architectures can be broadly classified into RISC (Reduced Instruction Set Computer) and
CISC (Complex Instruction Set Computer) based on the number and complexity of instructions they
use.
2. RISC (Reduced Instruction Set Computer):
• RISC architecture focuses on simplifying the instruction set for faster execution.
• Each instruction is designed to execute in one clock cycle, improving performance and
throughput.
Characteristics of RISC:
Feature   Description
Instruction Length Fixed-length (typically 32 bits)
Execution Speed One instruction per clock cycle
Addressing Modes Few (usually 3–5)
Instruction Set   Small and simple
Registers   Large number of general-purpose registers
Pipelining   Highly efficient and easy to implement
Examples   ARM, MIPS, SPARC, RISC-V
Advantages of RISC:
•   Simplifies hardware design.
• High performance due to pipelining.
•   Easier compiler optimization.
•   Consistent instruction timing.
Disadvantages of RISC:
•   Requires more instructions for complex operations.
********** 13 **********
--- page 14 ---
•   Larger program size compared to CISC.
3. CISC (Complex Instruction Set Computer):
• CISC architecture includes a large set of complex instructions, each capable of performing multiple
operations.
• Focuses on reducing the number of instructions per program.
Characteristics of CISC:
Feature   Description
Instruction Length Variable (8 to 64 bits or more)
Execution Speed   Slower, may take multiple cycles
Addressing Modes Many (up to 15 or more)
Instruction Set   Large and complex
Registers   Fewer general-purpose registers
Pipelining   Difficult to implement efficiently
Examples   Intel x86, VAX, Motorola 68000
Advantages of CISC:
• Compact programs due to complex instructions.
•   Easier assembly-level programming.
•   Efficient for memory-limited systems.
Disadvantages of CISC:
• Slower execution due to complex decoding.
•   Difficult to pipeline efficiently.
• More complex hardware design.
4. Comparison Table:
Aspect   RISC   CISC
Instruction Count   Fewer   Large
Instruction Size   Fixed   Variable
Execution Time   1 cycle/instruction Multiple cycles/instruction
Hardware Complexity Simple   Complex
Pipelining   Easy to implement Difficult
Registers   Many   Few
Examples   ARM, MIPS   Intel x86, VAX
b. Classify and explain the types of machine instructions based on address references, illustrating each
with suitable examples.
********** 14 **********
--- page 15 ---
Solution:
1. Introduction:
Machine instructions can be classified based on the number of address fields used to specify operands
and results in the instruction format.
The address field tells the CPU where the operands are located (registers, memory, or immediate).
2. Classification of Machine Instructions Based on Address Reference:
Type   Address Fields General Format   Example
Zero-Address Instructions None   OP   PUSH, POP, ADD
One-Address Instructions One   OP A   LOAD A, NOT A
Two-Address Instructions Two   OP A, B   MOV A, B
Three-Address Instructions Three   OP A, B, C   ADD A, B, C
3. Explanation of Each Type:
(i) Zero-Address Instruction:
• Used in stack-based architectures.
• Operands are implicitly stored on the stack.
• Example:
• PUSH A
• PUSH B
• ADD
→ Adds top two elements on the stack.
✅ Advantage: No explicit address field; shorter instruction size.
❌ Disadvantage: More stack operations; slower for large programs.
(ii) One-Address Instruction:
• Uses accumulator architecture.
• One operand is implicitly the accumulator, and the other is explicitly given.
Example:
LOAD A   ; Acc ← M[A]
ADD B   ; Acc ← Acc + M[B]
STORE C   ; M[C] ← Acc
✅ Advantage: Simple to design and understand.
❌ Disadvantage: Frequent memory access through accumulator.
********** 15 **********
--- page 16 ---
(iii) Two-Address Instruction:
• Both operands are explicitly mentioned.
• One operand also acts as the destination.
Example:
ADD A, B   ; A ← A + B
✅ Advantage: Reduces number of instructions.
❌ Disadvantage: More bits required for instruction storage.
(iv) Three-Address Instruction:
•   Contains three operands — two sources and one destination.
• Common in RISC processors.
Example:
ADD A, B, C ; A ← B + C
✅ Advantage: Allows complex operations in a single instruction.
❌ Disadvantage: Larger instruction size.
4. Summary Table:
Type   Operands Specified   Typical Architecture Example
Zero-Address Implicit (Stack)   Stack-based   ADD
One-Address Accumulator   Single Accumulator ADD A
Two-Address Source & Destination   Register–Memory   ADD A, B
Three-Address Two Sources + Destination RISC   ADD A, B, C
Conclusion:
The number of address references in machine instructions determines the complexity, size, and execution
efficiency of a processor. Modern processors, especially RISC systems, often favor three-address formats
for improved performance and pipelining.
Q7.
a. Explain and summarize the advantages and disadvantages of a Superscalar architecture in modern
processors. [10M]
Solution:
1. Definition:
A Superscalar architecture allows a processor to execute more than one instruction per clock cycle
by using multiple execution units.
It improves the instruction-level parallelism (ILP) of a CPU.
********** 16 **********
--- page 17 ---
2. Key Concept:
• Multiple pipelines operate simultaneously.
• The processor fetches, decodes, and executes several instructions in parallel.
•   Out-of-order and speculative execution techniques are often used.
3. Advantages of Superscalar Architecture:
Advantage   Explanation
Increased Performance   Executes multiple instructions per clock cycle.
Efficient Resource Utilization   Uses multiple ALUs, FPUs, and pipelines simultaneously.
Higher Instruction Throughput   Parallel instruction issue enhances overall speed.
Supports Pipelining and Parallelism Enables multiple functional units to work concurrently.
Reduced Program Execution Time Achieves better CPU utilization and shorter execution times.
4. Disadvantages of Superscalar Architecture:
Disadvantage   Explanation
Complex Hardware Design   Requires advanced instruction scheduling and hazard detection logic.
Increased Power Consumption   Parallel execution units increase power usage.
Performance gain reduces after certain instruction-level parallelism is
Diminishing Returns
reached.
Dependency Management
Data and control dependencies between instructions limit parallel execution.
Issues
b. Describe and analyze the concept of Virtual Memory in computer systems. Also, explain what is meant
by a logical address space and how it differs from physical memory.
Solution:
1. Definition:
Virtual Memory is a memory management technique that gives an application the illusion of having a
large, continuous memory space even when the physical RAM is limited.
It uses a portion of secondary storage (like a hard disk or SSD) to simulate main memory.
2. Key Concept:
Virtual memory enables:
• Execution of programs larger than physical memory.
•   Isolation and protection of processes.
•   Efficient memory utilization through paging or segmentation.
********** 17 **********
--- page 18 ---
3. Working Principle:
• The CPU generates logical addresses during program execution.
• These are mapped to physical addresses by the Memory Management Unit (MMU).
• When required data is not present in RAM, a page fault occurs and data is fetched from secondary
storage.
4. Logical Address Space:
Term   Explanation
Logical Address (Virtual Address) The address generated by the CPU during program execution.
Physical Address   The actual address in the main memory (RAM).
Logical Address Space   The range of all possible logical addresses a process can generate.
Example:
If a CPU supports 32-bit addressing, the logical address space = 2³² = 4 GB, regardless of actual physical
RAM size.
5. Address Mapping Diagram:
CPU
| (Generates Logical Address)
v
+----------------------------+
| Memory Management Unit   |
| (MMU)   |
+----------------------------+
| (Translates)
v
Physical Memory (RAM)
6. Advantages of Virtual Memory:
Advantage   Explanation
Efficient Memory Use   Only needed parts of a program are loaded into memory.
Isolation   Each process operates in its own logical address space.
Large Program Execution Enables execution of programs larger than physical memory.
Protection   Prevents one process from accessing another’s memory.
7. Disadvantages of Virtual Memory:
Disadvantage   Explanation
Reduced Performance Frequent swapping (paging) causes delay.
********** 18 **********
--- page 19 ---
Disadvantage   Explanation
Increased Disk Wear Excessive paging can reduce disk lifespan.
Complex Management Requires sophisticated hardware (MMU) and OS algorithms.
c. Define and explain the concept of a Bus in a computer system. Describe the main types of system buses
and their functions. [5M]
Solution:
1. Definition:
A Bus is a communication pathway that connects various components of a computer system (CPU,
memory, I/O devices) and allows the transfer of data, address, and control signals among them.
2. Types of Buses:
Bus Type   Purpose   Example Signal
Transfers actual data between CPU, memory, and I/O   Data values (e.g., 8-bit, 16-bit, 32-
Data Bus
devices.   bit)
Address   Carries the memory addresses of data/instructions to be   Memory location address (e.g.,
Bus   accessed.   0x3F0A)
Control Bus Carries control signals that coordinate all activities.   Read/Write, Interrupt, Clock signals
4. Functionality Summary:
Bus   Function
Data Bus   Bi-directional; used for transferring data.
Address Bus Uni-directional; specifies memory location.
Control Bus Bi-directional; synchronizes system operations.
********** 19 **********
````
